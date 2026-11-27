# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Build and cache artifacts that a MATLAB/Simulink import must skip.

``slprj/`` and ``<model>_*_rtw/`` are derived: deleting them only forces a
rebuild, so importing their generated ``.c``/``.h``/``.obj``/``.slxc`` files
adds noise to a resource directory and is never knowledge. The behavior is the
same idea as ``.gitignore``; the built-in rules are equivalent to::

    slprj/
    sfprj/
    *_rtw/
    codegen/
    *.slxc
    *.autosave

Where those folders appear is not fixed. Unless ``Simulink.fileGenControl`` has
moved them, Simulink writes the cache to ``slprj`` and the generated code to
``<model>_<target>_rtw`` inside the folder MATLAB is working in (``pwd``), which
can be any folder of the project and differs between sessions. They are
therefore matched by name at any depth of the imported tree, not only next to
the model. Relative ``CacheFolder`` / ``CodeGenFolder`` values are resolved
against ``pwd`` too and become fixed only after ``setConfig``.

MATLAB is not installed where OpenViking runs, so the setting cannot be queried
through the API. Instead the project's ``.m`` scripts are read statically and the
``CacheFolder`` / ``CodeGenFolder`` expressions are evaluated for the literal
path shapes MATLAB users write (``fullfile``, ``pwd``, ``mfilename``, string
concatenation, variables). Folders that resolve to an absolute path outside the
project fall back to their last path component, which is what identifies them
inside the imported tree. Unresolved expressions (``getenv``, ``tempdir``,
``matlabroot``) contribute nothing and the built-in defaults still apply. The
same holds when the folders were changed through the Simulink preferences UI:
their contents are still pruned because ``slprj/``, ``*_rtw/`` and ``*.slxc``
are recognised on their own.
"""

from __future__ import annotations

import fnmatch
import os
import posixpath
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

# Derived folder names, matched case-insensitively at any depth below the import
# root. ``slprj``/``sfprj`` and ``*_rtw`` are Simulink-specific, so they are
# always skipped; ``codegen`` is also used by other toolchains and only counts
# inside a MATLAB/Simulink project.
DEFAULT_BUILD_DIR_NAMES = frozenset({"slprj", "sfprj"})
DEFAULT_BUILD_DIR_GLOBS = ("*_rtw",)
PROJECT_BUILD_DIR_NAMES = frozenset({"codegen"})
DEFAULT_DERIVED_FILE_GLOBS = ("*.slxc", "*.autosave")
PROJECT_DERIVED_FILE_GLOBS: tuple[str, ...] = ()

# MATLAB keeps per-project file state (categories, target paths, digests) in
# ``<project>/resources/project/<hash>/*.xml``. Thousands of tiny XML files
# describe bookkeeping, not knowledge, so they are aggregated, never imported.
PROJECT_RESOURCES_DIR = "resources"
PROJECT_RESOURCES_STATE_DIR = "project"

# Files that make an arbitrary directory a MATLAB/Simulink project. ``.m`` and
# ``.mat`` alone are ambiguous (Objective-C, generic binary data), so only
# model, dictionary, Live Script and project formats count.
PROJECT_MARKER_SUFFIXES = frozenset(
    {
        ".slx",
        ".mdl",
        ".sldd",
        ".slxp",
        ".mdlp",
        ".mlx",
        ".mlapp",
        ".mlproj",
        ".slreqx",
        ".slmx",
        ".mldatx",
        ".sfx",
        ".ssc",
        ".sscp",
    }
)

_PROJECT_SCAN_MAX_ENTRIES = 20000
_SCRIPT_MAX_BYTES = 2 * 1024 * 1024
_SCRIPT_MAX_FILES = 2000
_MAX_BUILD_FOLDERS = 64
_EVAL_MAX_DEPTH = 8
_ROOT = "\x00project-root\x00"
_FILE_GEN_CALL = "Simulink.fileGenControl"
_FOLDER_FIELDS = {"cachefolder": "cache", "codegenfolder": "codegen"}


class MatlabBuildIgnore:
    """Filters derived MATLAB/Simulink folders and cache files for one import root.

    Folder names learned from ``Simulink.fileGenControl`` and the generic
    ``codegen/`` name are resolved lazily once per import and cached, so the
    tree is inspected at most once even though every directory is checked.
    """

    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self._is_matlab_project: Optional[bool] = None
        self._custom_folders: Tuple[Tuple[str, ...], ...] = ()

    def is_build_dir(self, path: Path) -> bool:
        """True for slprj/, <model>_*_rtw/, codegen/ and detected custom folders."""
        name = path.name.casefold()
        if name in DEFAULT_BUILD_DIR_NAMES or any(
            fnmatch.fnmatch(name, pattern) for pattern in DEFAULT_BUILD_DIR_GLOBS
        ):
            return True
        if not self.is_matlab_project():
            return False
        if name in PROJECT_BUILD_DIR_NAMES:
            return True
        parts = _relative_parts(path, self.root)
        return any(
            len(parts) >= len(folder) and parts[-len(folder) :] == folder
            for folder in self._custom_folders
        )

    def is_derived_file(self, path: Path) -> bool:
        """True for stand-alone build artifacts such as ``model.slxc``."""
        name = path.name.casefold()
        if any(fnmatch.fnmatch(name, pattern) for pattern in DEFAULT_DERIVED_FILE_GLOBS):
            return True
        return self.is_matlab_project() and any(
            fnmatch.fnmatch(name, pattern) for pattern in PROJECT_DERIVED_FILE_GLOBS
        )

    def is_matlab_project(self) -> bool:
        """Whether the import root contains MATLAB/Simulink project files."""
        if self._is_matlab_project is None:
            self._is_matlab_project = looks_like_matlab_project(self.root)
            if self._is_matlab_project:
                self._custom_folders = detect_build_folders(self.root)
        return self._is_matlab_project


def matlab_ignore_for(root: Path) -> MatlabBuildIgnore:
    """Return the build/cache rules for an import root.

    The default folder and cache-file patterns apply to any directory import;
    MATLAB-specific additions (``codegen/`` and the folders named in
    ``Simulink.fileGenControl``) activate when the tree contains a project.
    Editor backups (``*.asv``) are not cache files but a stale copy of a source
    file, so the ingest table excludes them instead of the scanner.
    """
    return MatlabBuildIgnore(Path(root).resolve())


def looks_like_matlab_project(root: Path) -> bool:
    """Bounded search of the whole tree for MATLAB/Simulink project markers."""
    root = Path(root)
    for path in _walk_files(root, limit=_PROJECT_SCAN_MAX_ENTRIES):
        if path.suffix.casefold() in PROJECT_MARKER_SUFFIXES:
            return True
    return False


def detect_build_folders(root: Path) -> Tuple[Tuple[str, ...], ...]:
    """Read ``Simulink.fileGenControl`` calls from the project and resolve the folders."""
    folders: List[Tuple[str, ...]] = []
    for script in _walk_files(root, suffix=".m", limit=_SCRIPT_MAX_FILES):
        if script.stat().st_size > _SCRIPT_MAX_BYTES:
            continue
        try:
            text = script.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if _FILE_GEN_CALL not in text:
            continue
        for value in _file_gen_folder_values(text):
            folder = _folder_suffix(value)
            if folder and folder not in folders:
                folders.append(folder)
        if len(folders) >= _MAX_BUILD_FOLDERS:
            break
    return tuple(folders)


def _walk_files(
    root: Path,
    suffix: Optional[str] = None,
    limit: int = _SCRIPT_MAX_FILES,
) -> Iterable[Path]:
    """Yield project files in a stable order, never descending into build folders."""
    root = Path(root)
    count = 0
    for dir_path, dir_names, file_names in os.walk(root, topdown=True):
        current = Path(dir_path)
        dir_names[:] = sorted(
            name for name in dir_names if not name.startswith(".") and not _is_build_name(name)
        )
        for name in sorted(file_names):
            if suffix is not None and not name.casefold().endswith(suffix):
                continue
            path = current / name
            if path.is_symlink() or not path.is_file():
                continue
            count += 1
            if count > limit:
                return
            yield path


def _is_build_name(name: str) -> bool:
    folded = name.casefold()
    if folded in DEFAULT_BUILD_DIR_NAMES or folded in PROJECT_BUILD_DIR_NAMES:
        return True
    return any(fnmatch.fnmatch(folded, pattern) for pattern in DEFAULT_BUILD_DIR_GLOBS)


def project_resources_index(rel_parts: Sequence[str]) -> Optional[int]:
    """Index of the ``resources`` part when it is followed by ``project``.

    The index also names the project root: the parts before it. ``None`` means
    the path is not project state and is classified by its own category.
    """
    lowered = [part.casefold() for part in rel_parts]
    for index, part in enumerate(lowered[:-1]):
        if part == PROJECT_RESOURCES_DIR and lowered[index + 1] == PROJECT_RESOURCES_STATE_DIR:
            return index
    return None


def _relative_parts(path: Path, root: Path) -> Tuple[str, ...]:
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        parts = (path.name,)
    return tuple(part.casefold() for part in parts)


# ---------------------------------------------------------------------------
# Static reading of Simulink.fileGenControl calls
# ---------------------------------------------------------------------------


def _file_gen_folder_values(text: str) -> List[str]:
    """Return the applied CacheFolder/CodeGenFolder values of one M script.

    Only values that reach a ``setConfig`` call are returned: assignments that
    are never applied do not change where MATLAB writes, so they must not
    change what the import skips. Each expression is evaluated with the local
    variables known at that statement, because startup scripts often build the
    path from ``pwd`` first.
    """
    statements = _split_statements(text)
    variables: Dict[str, str] = {}
    fields: Dict[str, Dict[str, str]] = {}
    applied: List[Tuple[str, Dict[str, str]]] = []

    for statement in statements:
        assignment = re.match(r"^\s*([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)\s*=\s*(.+)$", statement)
        if assignment:
            target, expression = assignment.group(1), assignment.group(2).strip()
            if "." in target:
                owner, field = target.split(".", 1)
                kind = _FOLDER_FIELDS.get(field.casefold())
                if kind:
                    fields.setdefault(owner, {})[kind] = expression
            else:
                variables[target] = expression

        for args in _file_gen_calls(statement):
            action = (
                _string_literal(args[0]).casefold() if args and _string_literal(args[0]) else ""
            )
            if action == "reset":
                applied.clear()
                continue
            if action not in {"setconfig", "set"}:
                continue
            for index in range(1, len(args) - 1):
                key = _string_literal(args[index])
                if not key:
                    continue
                key_folded = key.casefold()
                if key_folded == "config":
                    owner = args[index + 1].strip()
                    for expression in fields.get(owner, {}).values():
                        applied.append((expression, dict(variables)))
                elif key_folded in _FOLDER_FIELDS:
                    applied.append((args[index + 1], dict(variables)))

    values = []
    for expression, variables_at_use in applied:
        value = _evaluate(expression, variables_at_use)
        if value:
            values.append(value)
    return values


def _file_gen_calls(statement: str) -> List[List[str]]:
    """Extract argument lists of Simulink.fileGenControl(...) calls in a statement."""
    calls: List[List[str]] = []
    start = 0
    while True:
        index = statement.find(_FILE_GEN_CALL, start)
        if index == -1:
            break
        paren = statement.find("(", index + len(_FILE_GEN_CALL))
        if paren == -1:
            break
        end = _matching_paren(statement, paren)
        if end == -1:
            break
        calls.append(_split_top_level(statement[paren + 1 : end], ","))
        start = end + 1
    return calls


def _matching_paren(text: str, open_index: int) -> int:
    depth = 0
    quote = ""
    index = open_index
    while index < len(text):
        char = text[index]
        if quote:
            if char == quote:
                if index + 1 < len(text) and text[index + 1] == quote:
                    index += 1
                else:
                    quote = ""
        elif char in "'\"":
            quote = char
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return -1


def _split_statements(text: str) -> List[str]:
    """Split M source into statements, dropping comments and joining continuations."""
    joined: List[str] = []
    pending = ""
    for raw in text.splitlines():
        line = _strip_line_comment(raw)
        stripped = line.rstrip()
        if stripped.endswith("..."):
            pending += stripped[:-3] + " "
            continue
        joined.append(pending + line)
        pending = ""
    if pending:
        joined.append(pending)

    statements: List[str] = []
    current: List[str] = []
    quote = ""
    for char in "\n".join(joined):
        if quote:
            current.append(char)
            if char == quote:
                quote = ""
            continue
        if char in "'\"":
            quote = char
            current.append(char)
            continue
        if char == ";":
            statements.append("".join(current).strip())
            current = []
            continue
        if char == "\n":
            statements.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    statements.append("".join(current).strip())
    return [statement for statement in statements if statement]


def _strip_line_comment(line: str) -> str:
    quote = ""
    index = 0
    while index < len(line):
        char = line[index]
        if quote:
            if char == quote:
                if index + 1 < len(line) and line[index + 1] == quote:
                    index += 1
                else:
                    quote = ""
        elif char in "'\"" and not _inside_transpose(line, index):
            quote = char
        elif char == "%":
            return line[:index]
        index += 1
    return line


def _inside_transpose(line: str, index: int) -> bool:
    """A single quote after a value is MATLAB's transpose, not a string start."""
    if line[index] != "'" or index == 0:
        return False
    previous = line[index - 1]
    return previous.isalnum() or previous in ")]}_.'"


def _split_top_level(text: str, separators: str) -> List[str]:
    parts: List[str] = []
    current: List[str] = []
    depth = 0
    quote = ""
    index = 0
    while index < len(text):
        char = text[index]
        if quote:
            current.append(char)
            if char == quote:
                if index + 1 < len(text) and text[index + 1] == quote:
                    current.append(text[index + 1])
                    index += 1
                else:
                    quote = ""
        elif char in "'\"":
            quote = char
            current.append(char)
        elif char in "([{":
            depth += 1
            current.append(char)
        elif char in ")]}":
            depth -= 1
            current.append(char)
        elif depth == 0 and char in separators:
            parts.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        index += 1
    parts.append("".join(current).strip())
    return [part for part in parts if part]


def _string_literal(expression: str) -> Optional[str]:
    expression = expression.strip()
    if len(expression) < 2 or expression[0] not in "'\"" or expression[-1] != expression[0]:
        return None
    quote = expression[0]
    inner = expression[1:-1]
    return inner.replace(quote + quote, quote)


# ---------------------------------------------------------------------------
# Path evaluation
# ---------------------------------------------------------------------------


def _folder_suffix(value: str) -> Optional[Tuple[str, ...]]:
    if not value:
        return None
    normalized = value.replace("\\", "/")
    if normalized.startswith(_ROOT):
        relative = normalized[len(_ROOT) :].strip("/")
        return _components(relative)
    if re.match(r"^[A-Za-z]:/", normalized) or normalized.startswith("/"):
        # Absolute paths belong to the machine that ran MATLAB; its last
        # component is still the folder's identity inside the project tree.
        components = _components(normalized)
        return components[-1:] or None
    return _components(normalized)


def _components(relative: str) -> Optional[Tuple[str, ...]]:
    parts = []
    for part in posixpath.normpath(relative).split("/"):
        if part in ("", ".", ".."):
            continue
        parts.append(part.casefold())
    return tuple(parts) or None


def _evaluate(expression: str, variables: Dict[str, str], depth: int = 0) -> Optional[str]:
    expression = expression.strip()
    if not expression or depth > _EVAL_MAX_DEPTH:
        return None

    if expression.startswith("[") and expression.endswith("]"):
        pieces = [
            _evaluate(piece, variables, depth + 1)
            for piece in re.split(r"[\s,;]+", expression[1:-1])
            if piece
        ]
        return "".join(pieces) if pieces and all(p is not None for p in pieces) else None

    call = re.fullmatch(r"([A-Za-z_][\w.]*)\s*\((.*)\)", expression, re.S)
    if call:
        return _evaluate_call(call.group(1), _split_top_level(call.group(2), ","), variables, depth)

    literal = _string_literal(expression)
    if literal is not None:
        return literal

    if re.fullmatch(r"[A-Za-z_]\w*", expression):
        if expression == "pwd":
            return _ROOT
        value = variables.get(expression)
        if value is not None:
            return _evaluate(value, variables, depth + 1)
    return None


def _evaluate_call(
    name: str, args: Sequence[str], variables: Dict[str, str], depth: int
) -> Optional[str]:
    if name == "pwd":
        return _ROOT
    if name == "mfilename":
        return _ROOT
    if name == "filesep":
        return "/"
    if name == "fileparts":
        return _evaluate(args[0], variables, depth + 1) if args else None
    if name in ("fullfile", "strcat", "char"):
        values = [_evaluate(arg, variables, depth + 1) for arg in args]
        if not values or any(value is None for value in values):
            return None
        if name == "fullfile":
            return posixpath.join(*(_trim_separator(str(value)) for value in values))
        return "".join(str(value) for value in values)
    return None


def _trim_separator(value: str) -> str:
    return value.replace("\\", "/").rstrip("/")
