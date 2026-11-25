# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Render one block description per block from the ``slxkeydes`` templates.

Every block in a Simulink model gets a key (:mod:`block_keys`), the key selects
a description template, and the template's ``{parameter}`` placeholders are
replaced with the values the instance carries. The result is one sentence that
says what the block does and how its parameters are set, instead of the raw
parameter dictionary the system JSON used to repeat.

Templates live next to this module under ``slxkeydes/{en,zh}``. They are built
and checked in ``openviking-engineering-resources`` (``matlab/simulink/slxkeydes``)
and copied here so an import needs nothing but this package; point
``OPENVIKING_MATLAB_KEYDES_DIR`` at another tree to override them.
"""

from __future__ import annotations

import json
import os
import re
import threading
from pathlib import Path
from typing import TYPE_CHECKING

from openviking.parse.parsers.matlab.block_keys import block_key

if TYPE_CHECKING:  # pragma: no cover - imported only for type checkers
    from openviking.parse.parsers.matlab.slx import Block

KEYDES_DIR_ENV = "OPENVIKING_MATLAB_KEYDES_DIR"
MAX_VALUE_CHARS = 120

_PLACEHOLDER = re.compile(r"\{([^{}]+)\}")
_WHITESPACE = re.compile(r"\s+")
# Clause separators in both template languages; a clause is dropped when one of
# its placeholders has no value at all.
_SEPARATOR = re.compile(r"([；、,;])")
_REPEATED_SEPARATOR = re.compile(r"([；、，,;])(?:\s*[；、，,;])+")
_SPACE_BEFORE_PUNCTUATION = re.compile(r"\s+([；、，。：,;])")
_TOKEN = re.compile(r"\x01(\d+)\x01")


def keydes_root() -> Path:
    """Return the template tree, honouring ``OPENVIKING_MATLAB_KEYDES_DIR``."""
    override = os.environ.get(KEYDES_DIR_ENV, "").strip()
    if override:
        return Path(override).expanduser()
    return Path(__file__).resolve().parent / "slxkeydes"


def template_language(language: str | None) -> str:
    """Map an import language (``zh``, ``zh-CN``, ``en``) to a template tree."""
    return "zh" if str(language or "").lower().startswith("zh") else "en"


def _collapse(value: object) -> str:
    return _WHITESPACE.sub(" ", str(value or "")).strip()


def _identity(value: object) -> str:
    """Compare parameter values the way Simulink writes them: ignore spacing."""
    return _WHITESPACE.sub("", str(value or "")).casefold()


def _one_line(value: object, limit: int = MAX_VALUE_CHARS) -> str:
    text = _collapse(value)
    if len(text) > limit:
        return text[:limit].rstrip() + "…"
    return text


def _parameter_name(value: object) -> str:
    """Compare template parameter names with SLX parameter names.

    A template names a parameter the way its documentation page does (``Sample
    time (-1 for inherited)``, ``Table data``); the SLX file stores the identifier
    the API uses (``SampleTime``, ``Table``). Lowercase alphanumerics up to the
    first parenthesis make the two comparable, and :meth:`KeydesLibrary._bind`
    accepts a prefix relation for the rest.
    """
    return re.sub(r"[^0-9a-z]+", "", str(value or "").split("(")[0].casefold())


def _common_prefix(left: str, right: str) -> int:
    length = 0
    for a, b in zip(left, right, strict=False):
        if a != b:
            break
        length += 1
    return length


def _tidy(text: str) -> str:
    text = _SPACE_BEFORE_PUNCTUATION.sub(r"\1", _collapse(text))
    text = _REPEATED_SEPARATOR.sub(r"\1", text)
    return text.strip(" ；、，,;")


def _drop_empty_clauses(text: str, values: dict[str, str]) -> str:
    """Drop clauses that carry no words, or no value at all.

    A clause whose placeholder has neither an instance nor a default value would
    keep wording such as "打开根输入端口映射器工具的选项 按钮" without its value, and a
    clause that is nothing but a placeholder renders as a bare "[]" or "auto".
    Both are dropped here.
    """
    parts = _SEPARATOR.split(text)
    kept: list[str] = []
    for index in range(0, len(parts), 2):
        segment = parts[index]
        separator = parts[index + 1] if index + 1 < len(parts) else ""
        if any(not values.get(token.group(0), "") for token in _TOKEN.finditer(segment)):
            continue
        if not _TOKEN.sub("", segment).strip():
            continue
        kept.extend([segment, separator])
    return "".join(kept)


class KeydesLibrary:
    """Templates from one ``slxkeydes`` tree, cached per key and language."""

    def __init__(self, root: str | Path | None = None) -> None:
        self.root = Path(root) if root is not None else keydes_root()
        self._lock = threading.Lock()
        self._index: dict[str, dict[str, str]] = {}
        self._templates: dict[tuple[str, str], dict | None] = {}

    def available(self) -> bool:
        return (self.root / "en" / "index.json").is_file()

    def _load_index(self, tree: str) -> dict[str, str]:
        with self._lock:
            cached = self._index.get(tree)
        if cached is not None:
            return cached
        entries: dict[str, str] = {}
        index_path = self.root / tree / "index.json"
        if index_path.is_file():
            try:
                rows = json.loads(index_path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                rows = []
            for row in rows if isinstance(rows, list) else []:
                key = _collapse(row.get("key"))
                relative = row.get("file")
                if key and relative:
                    entries.setdefault(key.casefold(), str(relative))
        with self._lock:
            self._index[tree] = entries
        return entries

    def template(self, key: str, language: str = "en") -> dict | None:
        """Return the parsed template for ``key``, or ``None`` when it has none."""
        tree = template_language(language)
        cache_key = (tree, key)
        with self._lock:
            if cache_key in self._templates:
                return self._templates[cache_key]
        document: dict | None = None
        relative = self._load_index(tree).get(key.casefold())
        if relative:
            path = self.root / tree / relative
            try:
                if path.is_file():
                    document = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                document = None
        with self._lock:
            self._templates[cache_key] = document
        return document

    def describe(self, block: "Block", language: str = "en") -> tuple[str | None, str | None]:
        """Return ``(key, description)`` for one block.

        ``key`` is ``None`` for a subsystem, which the parser expands instead of
        describing. ``description`` is ``None`` when the key has no template.
        """
        key = block_key(block)
        if not key:
            return None, None
        document = self.template(key, language)
        if document is None:
            return key, None
        return key, self._render(document, self._values(block, key, document, language))

    def _values(self, block: "Block", key: str, document: dict, language: str) -> list[str]:
        """One value per template parameter, in template order.

        English templates name parameters and state defaults exactly as the
        documentation and the MATLAB dialog do. The Chinese templates translate
        both, so the English template of the same key supplies the name to look
        the instance up by and the value to fall back to. Both trees are
        generated parameter by parameter from the same documentation section, so
        the two lists line up; a parameter the English template lacks keeps its
        own name and default.
        """
        tree = template_language(language)
        english = document if tree == "en" else (self.template(key, "en") or {})
        english_params = english.get("params") or []
        parameters = document.get("params") or []
        instance: dict[str, str] = {}
        for name, value in block.parameters.items():
            instance.setdefault(_parameter_name(name), _one_line(value))
        names: list[str] = []
        defaults: list[str] = []
        for index, parameter in enumerate(parameters):
            source = english_params[index] if index < len(english_params) else parameter
            names.append(_parameter_name(source.get("name")))
            defaults.append(_one_line(source.get("default")))
        bound = self._bind(names, instance)
        return [bound.get(index) or defaults[index] for index in range(len(parameters))]

    def _bind(self, names: list[str], instance: dict[str, str]) -> dict[int, str]:
        """Match template parameters to the instance's parameter names.

        Names are matched in three steps: identical, then one name being a
        prefix of the other (``Table`` for ``Table data``, ``Port`` for ``Port
        number``), longest shared prefix first, one instance parameter used at
        most once so ``Port number`` wins over ``Port dimensions``. A prefix
        match that stays ambiguous is left unbound and falls back to the
        documented default rather than guessing.
        """
        bound: dict[int, str] = {}
        used: set[str] = set()
        for index, name in enumerate(names):
            if name and name in instance and name not in used:
                bound[index] = instance[name]
                used.add(name)
        candidates: list[tuple[int, int, int, list[tuple[int, str]]]] = []
        for index, name in enumerate(names):
            if index in bound or len(name) < 4:
                continue
            options = [
                (_common_prefix(name, candidate), candidate)
                for candidate in instance
                if candidate not in used
                and len(candidate) >= 4
                and (candidate.startswith(name) or name.startswith(candidate))
            ]
            if options:
                shared = max(option[0] for option in options)
                candidates.append((len(options), -shared, index, options))
        candidates.sort(key=lambda item: (item[0], item[1], item[2]))
        for _, _, index, options in candidates:
            options.sort(key=lambda option: -option[0])
            best = options[0]
            if len(options) > 1 and options[1][0] == best[0]:
                continue
            if best[1] in used:
                continue
            used.add(best[1])
            bound[index] = instance[best[1]]
        return bound

    def _parameter_index(self, document: dict, name: str) -> int | None:
        wanted = _identity(name)
        for index, parameter in enumerate(document.get("params") or []):
            if _identity(parameter.get("name")) == wanted:
                return index
        return None

    def _choose_text(self, document: dict, values: list[str]) -> str:
        for variant in document.get("variants") or []:
            when = variant.get("when") or {}
            if when and self._matches(document, values, when):
                return str(variant.get("text") or document.get("text") or "")
        return str(document.get("text") or "")

    def _matches(self, document: dict, values: list[str], when: dict) -> bool:
        for name, allowed in when.items():
            index = self._parameter_index(document, name)
            if index is None:
                return False
            expected = {_identity(option) for option in allowed or []}
            if _identity(values[index]) not in expected:
                return False
        return True

    def _render(self, document: dict, values: list[str]) -> str:
        text = self._choose_text(document, values)
        tokens: dict[str, str] = {}

        def tokenize(match: re.Match) -> str:
            index = self._parameter_index(document, match.group(1))
            token = f"\x01{len(tokens)}\x01"
            tokens[token] = values[index] if index is not None else ""
            return token

        marked = _PLACEHOLDER.sub(tokenize, text)
        marked = _drop_empty_clauses(marked, tokens)
        return _tidy(_TOKEN.sub(lambda match: tokens[match.group(0)], marked))


_default_library: KeydesLibrary | None = None
_default_lock = threading.Lock()


def default_library() -> KeydesLibrary:
    """The template tree bundled with this package, loaded once per process."""
    global _default_library
    with _default_lock:
        if _default_library is None:
            _default_library = KeydesLibrary()
        return _default_library
