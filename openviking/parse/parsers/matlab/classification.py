# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Multi-label classification and location rules for MATLAB project files.

One extension can belong to several categories (``.sldd`` is both a container
and a data dictionary, ``.ctf`` is a container and protected) and can carry
several tags. The tags are location dependent: a ``.c`` file is project source
in ``src/`` but generated code under ``*_rtw/`` or ``slprj/``, and a ``.hex``
file is a build output in ``build/`` but a delivery attachment elsewhere.
"""

from __future__ import annotations

import fnmatch
from pathlib import Path
from typing import Iterable, Optional, Sequence

CATEGORY_TEXT = "可读文本"
CATEGORY_CONTAINER = "ZIP/工具容器"
CATEGORY_DATA = "数据/目标二进制"
CATEGORY_NATIVE = "Windows 原生"
CATEGORY_OPAQUE = "加密/保护"
CATEGORY_DERIVED = "派生/缓存"

# Base category per extension. Multi-category entries are explicit.
_EXTENSION_CATEGORY: dict[str, tuple[str, ...]] = {
    ".m": (CATEGORY_TEXT,),
    ".mdl": (CATEGORY_TEXT,),
    ".ssc": (CATEGORY_TEXT,),
    ".tlc": (CATEGORY_TEXT,),
    ".c": (CATEGORY_TEXT,),
    ".h": (CATEGORY_TEXT,),
    ".cpp": (CATEGORY_TEXT,),
    ".hpp": (CATEGORY_TEXT,),
    ".mk": (CATEGORY_TEXT,),
    ".bat": (CATEGORY_TEXT,),
    ".rsp": (CATEGORY_TEXT,),
    ".rtw": (CATEGORY_TEXT,),
    ".tmf": (CATEGORY_TEXT,),
    ".map": (CATEGORY_TEXT,),
    ".hex": (CATEGORY_DATA,),
    ".s19": (CATEGORY_DATA,),
    ".html": (CATEGORY_TEXT,),
    ".prj": (CATEGORY_TEXT,),
    ".asv": (CATEGORY_TEXT,),
    ".dmr": (CATEGORY_DATA,),
    ".tlh": (CATEGORY_TEXT,),
    ".tmw": (CATEGORY_DATA,),
    ".stl": (CATEGORY_DATA,),
    ".png": (CATEGORY_DATA,),
    ".py": (CATEGORY_TEXT,),
    ".xlsx": (CATEGORY_DATA,),
    ".xml": (CATEGORY_TEXT,),
    ".json": (CATEGORY_TEXT,),
    ".yaml": (CATEGORY_TEXT,),
    ".yml": (CATEGORY_TEXT,),
    ".csv": (CATEGORY_TEXT,),
    ".txt": (CATEGORY_TEXT,),
    ".ini": (CATEGORY_TEXT,),
    ".arxml": (CATEGORY_TEXT,),
    ".dbc": (CATEGORY_TEXT,),
    ".ldf": (CATEGORY_TEXT,),
    ".a2l": (CATEGORY_TEXT,),
    ".md": (CATEGORY_TEXT,),
    ".slx": (CATEGORY_CONTAINER,),
    ".sldd": (CATEGORY_CONTAINER, CATEGORY_DATA),
    ".mlx": (CATEGORY_CONTAINER,),
    ".mlapp": (CATEGORY_CONTAINER,),
    ".mlproj": (CATEGORY_CONTAINER,),
    ".mltbx": (CATEGORY_CONTAINER,),
    ".mlappinstall": (CATEGORY_CONTAINER,),
    ".mlpkginstall": (CATEGORY_CONTAINER,),
    ".sltx": (CATEGORY_CONTAINER,),
    ".slreqx": (CATEGORY_CONTAINER,),
    ".slmx": (CATEGORY_CONTAINER,),
    ".mldatx": (CATEGORY_CONTAINER,),
    ".sfx": (CATEGORY_CONTAINER,),
    ".fmu": (CATEGORY_CONTAINER,),
    ".ctf": (CATEGORY_CONTAINER, CATEGORY_OPAQUE),
    ".jar": (CATEGORY_CONTAINER,),
    ".mat": (CATEGORY_DATA,),
    ".fig": (CATEGORY_DATA,),
    ".mdf": (CATEGORY_DATA,),
    ".mf4": (CATEGORY_DATA,),
    ".blf": (CATEGORY_DATA,),
    ".elf": (CATEGORY_DATA,),
    ".bin": (CATEGORY_DATA,),
    ".mexw64": (CATEGORY_NATIVE,),
    ".mexw32": (CATEGORY_NATIVE,),
    ".dll": (CATEGORY_NATIVE,),
    ".exe": (CATEGORY_NATIVE,),
    ".lib": (CATEGORY_NATIVE,),
    ".obj": (CATEGORY_NATIVE,),
    ".pdb": (CATEGORY_NATIVE,),
    ".p": (CATEGORY_OPAQUE,),
    ".slxp": (CATEGORY_OPAQUE,),
    ".mdlp": (CATEGORY_OPAQUE,),
    ".sscp": (CATEGORY_OPAQUE,),
    ".slxc": (CATEGORY_DERIVED,),
    ".autosave": (CATEGORY_DERIVED,),
}

# Tags that describe the file itself, independent of where it sits.
INHERENT_TAGS: dict[str, tuple[str, ...]] = {
    ".slxc": ("slprj", "runtime"),
}

BUILD_DIR_NAMES = frozenset({"slprj", "sfprj"})
BUILD_DIR_GLOBS = ("*_rtw",)
PROJECT_BUILD_DIR_NAMES = frozenset({"codegen"})
BUILD_OUTPUT_DIR_NAMES = frozenset({"build", "output", "out", "target", "release", "debug"})
RUNTIME_DIR_NAMES = frozenset({"rsim", "raccel", "sim"})

DERIVED_EXTS = frozenset({".slxc", ".autosave"})
ALWAYS_EXCLUDED_EXTS = frozenset({".rtw", ".tmf"})
TARGET_OUTPUT_EXTS = frozenset({".hex", ".s19", ".elf", ".bin"})
GENERATED_CODE_EXTS = frozenset({".c", ".h", ".cpp", ".hpp", ".html", ".arxml", ".a2l"})
BUILD_SCRIPT_EXTS = frozenset({".mk", ".bat", ".rsp"})
NATIVE_BUILD_EXTS = frozenset({".mexw64", ".mexw32", ".dll", ".exe", ".lib", ".obj", ".pdb"})
SLPRJ_BUILD_EXTS = frozenset({".lib", ".obj", ".pdb", ".mk", ".bat", ".rsp"})

ACTION_IMPORT = "import"
ACTION_EXCLUDE = "exclude"
ACTION_ATTACH = "attach"
ACTION_PARSE = "parse"


def categories_for(ext: str) -> tuple[str, ...]:
    return _EXTENSION_CATEGORY.get(ext.lower(), (CATEGORY_TEXT,))


def _relative_parts(rel_path: str | Path) -> tuple[str, ...]:
    return tuple(part for part in Path(rel_path).parts if part not in {"", "."})


def _matches(name: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(name.casefold(), pattern) for pattern in patterns)


def _build_dir(rel_parts: Sequence[str]) -> Optional[tuple[int, str]]:
    """Return the outermost build-directory part and its index, if any."""
    for index, part in enumerate(rel_parts[:-1]):
        name = part.casefold()
        if name in BUILD_DIR_NAMES or _matches(name, BUILD_DIR_GLOBS):
            return index, name
        if name in PROJECT_BUILD_DIR_NAMES or name in BUILD_OUTPUT_DIR_NAMES:
            return index, name
    return None


def _is_runtime_location(rel_parts: Sequence[str]) -> bool:
    lowered = [part.casefold() for part in rel_parts]
    if "slprj" in lowered:
        after = lowered[lowered.index("slprj") + 1 :]
        return bool(after) and after[0] in RUNTIME_DIR_NAMES
    return False


def _build_output_location(rel_parts: Sequence[str]) -> bool:
    return any(part.casefold() in BUILD_OUTPUT_DIR_NAMES for part in rel_parts[:-1])


def _location_label(rel_parts: Sequence[str], build: Optional[tuple[int, str]]) -> str:
    if build is not None:
        index, name = build
        suffix = " → ".join(rel_parts[index:])
        return f"{suffix}/" if not suffix.endswith("/") else suffix
    if _build_output_location(rel_parts):
        return "构建输出目录"
    return "工程目录"


def classify_path(
    rel_path: str | Path,
    *,
    build_dir_check=None,
) -> dict[str, object]:
    """Classify one project-relative path into categories, tags and an action.

    ``build_dir_check`` accepts an absolute path and lets the caller add folders
    discovered from ``Simulink.fileGenControl``. It is optional so the function
    can also run on a bare relative path in tests.
    """
    parts = _relative_parts(rel_path)
    ext = Path(parts[-1]).suffix.lower() if parts else ""
    build = _build_dir(parts)
    runtime = _is_runtime_location(parts)
    generated = build is not None or _build_output_location(parts)

    tags: list[str] = list(INHERENT_TAGS.get(ext, ()))
    if build is not None:
        name = build[1]
        if name in BUILD_DIR_NAMES or name == "sfprj":
            tags.append("slprj")
        if _matches(name, BUILD_DIR_GLOBS) or name in PROJECT_BUILD_DIR_NAMES:
            tags.append("codegen")
        if ext in BUILD_SCRIPT_EXTS or ext in NATIVE_BUILD_EXTS or ext == ".map":
            tags.append("build")
        if ext in SLPRJ_BUILD_EXTS and "slprj" not in tags:
            tags.append("slprj")
    if runtime:
        for tag in ("runtime", "slprj"):
            if tag not in tags:
                tags.append(tag)
    if ext in TARGET_OUTPUT_EXTS and generated:
        for tag in ("codegen", "target"):
            if tag not in tags:
                tags.append(tag)
    if ext in GENERATED_CODE_EXTS and generated and "codegen" not in tags:
        tags.append("codegen")

    action = ACTION_IMPORT
    reason = "工程目录内导入"
    if build is not None:
        action, reason = ACTION_EXCLUDE, "matlab build/cache"
    elif ext in DERIVED_EXTS or ext in ALWAYS_EXCLUDED_EXTS:
        action, reason = ACTION_EXCLUDE, "matlab derived file"
    elif ext in TARGET_OUTPUT_EXTS and _build_output_location(parts):
        action, reason = ACTION_EXCLUDE, "matlab build output"
    elif ext in TARGET_OUTPUT_EXTS:
        action, reason = ACTION_ATTACH, "交付附件"
    elif ext == ".map" and not generated:
        action, reason = ACTION_IMPORT, "单独交付的映射文件"
    elif ext == ".stl":
        action, reason = ACTION_ATTACH, "三维模型附件"

    return {
        "path": Path(*parts).as_posix(),
        "extension": ext,
        "categories": list(categories_for(ext)),
        "tags": tags,
        "location": _location_label(parts, build),
        "action": action,
        "reason": reason,
    }


def classify_directory(rel_path: str | Path) -> dict[str, object]:
    """Labels for a directory that is pruned as build/cache before its files."""
    parts = _relative_parts(rel_path)
    lowered = [part.casefold() for part in parts]
    tags: list[str] = []
    if any(part in BUILD_DIR_NAMES or part == "sfprj" for part in lowered):
        tags.append("slprj")
    if any(_matches(part, BUILD_DIR_GLOBS) for part in lowered):
        tags.append("codegen")
    if any(part in PROJECT_BUILD_DIR_NAMES for part in lowered):
        tags.append("codegen")
    if any(part in RUNTIME_DIR_NAMES for part in lowered):
        for tag in ("runtime", "slprj"):
            if tag not in tags:
                tags.append(tag)
    if any(part in BUILD_OUTPUT_DIR_NAMES for part in lowered):
        tags.append("build")
    return {
        "path": Path(*parts).as_posix(),
        "extension": "",
        "categories": [CATEGORY_DERIVED],
        "tags": list(dict.fromkeys(tags)),
        "location": "构建/缓存目录",
        "action": ACTION_EXCLUDE,
        "reason": "matlab build/cache",
    }


def summarize(files: Iterable[dict[str, object]]) -> dict[str, object]:
    """Count categories and tags; a file may add to more than one counter."""
    category_counts: dict[str, int] = {}
    tag_counts: dict[str, int] = {}
    extension_counts: dict[str, int] = {}
    for item in files:
        for category in item.get("categories", []):
            category_counts[category] = category_counts.get(category, 0) + 1
        for tag in item.get("tags", []):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        ext = str(item.get("extension") or "")
        if ext:
            extension_counts[ext] = extension_counts.get(ext, 0) + 1
    return {
        "categories": category_counts,
        "tags": tag_counts,
        "extensions": extension_counts,
    }
