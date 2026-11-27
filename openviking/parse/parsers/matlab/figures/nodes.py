# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read the handle tree of a MATLAB FIG file into plain Python nodes.

A FIG file is a MAT container whose variables (``hgS_070000`` and, since
R2014b, ``hgM_070000``) hold the graphics object tree. Only ``hgS_070000`` is
readable without MATLAB: it stores ``type``, ``handle``, ``properties``,
``children`` and ``special`` fields per object. ``hgM_070000`` holds the MCOS
object model as opaque structures (``_TypeSystem``/``_Class``/``_ObjectMetadata``)
that a MAT reader cannot decode, so it is recorded and skipped.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

# Legacy (HG1) single-letter object codes, as written by savefig before R2014b.
_LEGACY_TYPES = {
    "f": "figure",
    "a": "axes",
    "l": "line",
    "t": "text",
    "u": "uicontrol",
    "p": "patch",
    "s": "surface",
    "i": "image",
    "r": "rectangle",
    "h": "hggroup",
    "g": "uimenu",
    "c": "uicontextmenu",
    "b": "uipanel",
}

_CLASS_PREFIXES = (
    "matlab.graphics.chart.primitive.",
    "matlab.graphics.chart.container.",
    "matlab.graphics.chart.decoration.",
    "matlab.graphics.chart.",
    "matlab.graphics.axis.",
    "matlab.graphics.illustration.",
    "matlab.graphics.primitive.",
    "matlab.graphics.layout.",
    "matlab.graphics.",
    "matlab.ui.control.",
    "matlab.ui.container.",
    "matlab.ui.",
    "uitools.",
)

_NODE_FIELDS = ("type", "handle", "properties", "children")


@dataclass
class FigureNode:
    """One graphics object: its class, handle, raw properties and children."""

    type: str = ""
    handle: float | None = None
    properties: dict[str, Any] = field(default_factory=dict)
    children: list["FigureNode"] = field(default_factory=list)

    @property
    def class_name(self) -> str:
        """Class name without the ``matlab.graphics.`` packaging."""
        name = (self.type or "").strip()
        for prefix in _CLASS_PREFIXES:
            if name.startswith(prefix):
                return name[len(prefix) :]
        return name

    @property
    def object_type(self) -> str:
        """Normalized object type: legacy letters resolved, class names kept."""
        name = (self.type or "").strip()
        if len(name) == 1 and name in _LEGACY_TYPES:
            return _LEGACY_TYPES[name]
        return self.class_name

    def get(self, *names: str) -> Any:
        """Case-insensitive property lookup, first match wins."""
        for name in names:
            if name in self.properties:
                return self.properties[name]
            lowered = name.lower()
            for key, value in self.properties.items():
                if key.lower() == lowered:
                    return value
        return None

    def has(self, *names: str) -> bool:
        return self.get(*names) is not None

    def child_of(self, *types: str) -> list["FigureNode"]:
        wanted = {t.lower() for t in types}
        return [child for child in self.children if child.object_type.lower() in wanted]

    def walk(self) -> Iterator["FigureNode"]:
        yield self
        for child in self.children:
            yield from child.walk()


def _is_struct(value: Any) -> bool:
    names = getattr(getattr(value, "dtype", None), "names", None)
    return bool(names)


def _first(value: Any) -> Any:
    """First element of a possibly wrapped MATLAB value, without losing arrays."""
    shape = getattr(value, "shape", None)
    if shape is not None and getattr(value, "size", 0) == 1:
        return value.reshape(-1)[0]
    if isinstance(value, (list, tuple)) and len(value) == 1:
        return value[0]
    return value


def _field(value: Any, name: str) -> Any:
    if _is_struct(value):
        if name in (value.dtype.names or ()):
            return value[name]
        return None
    if isinstance(value, dict):
        return value.get(name)
    return getattr(value, name, None)


def _flatten_objects(value: Any) -> list[Any]:
    """Every struct in a MATLAB array of objects, in file order."""
    if value is None:
        return []
    import numpy as np

    if isinstance(value, np.ndarray):
        if value.dtype == object:
            items: list[Any] = []
            for item in value.flat:
                items.extend(_flatten_objects(item))
            return items
        if _is_struct(value):
            return list(value.flat)
        return []
    if _is_struct(value) or isinstance(value, dict):
        return [value]
    if isinstance(value, (list, tuple)):
        items = []
        for item in value:
            items.extend(_flatten_objects(item))
        return items
    return []


def _properties(value: Any) -> dict[str, Any]:
    """Property map of one object, keeping raw MATLAB values."""
    raw = _field(value, "properties")
    if raw is None:
        raw = _field(value, "Properties")
    if raw is None:
        return {}
    raw = _first(raw)
    if _is_struct(raw):
        return {name: raw[name] for name in (raw.dtype.names or ())}
    if isinstance(raw, dict):
        return dict(raw)
    return {}


def build_node(value: Any, depth: int = 0) -> FigureNode:
    """Recursively convert one stored object and its children."""
    node = FigureNode(
        type=str(_text(_first(_field(value, "type") or _field(value, "Type")) or "")),
        handle=_number(_first(_field(value, "handle") or _field(value, "Handle"))),
        properties=_properties(value),
    )
    if depth > 32:
        return node
    raw_children = _field(value, "children")
    if raw_children is None:
        raw_children = _field(value, "Children")
    for child in _flatten_objects(raw_children):
        node.children.append(build_node(child, depth + 1))
    return node


def _number(value: Any) -> float | None:
    """One numeric property value, or None when it is empty or not a number."""
    raw = _first(value)
    if raw is None:
        return None
    import numpy as np

    if isinstance(raw, np.ndarray):
        if raw.size == 0 or raw.dtype.kind not in {"i", "u", "f", "b"}:
            return None
        raw = raw.reshape(-1)[0].item()
    try:
        number = float(raw)
    except (TypeError, ValueError):
        return None
    if math.isnan(number) or math.isinf(number):
        return None
    return number


def _text(value: Any) -> str:
    """MATLAB char array or string into a stripped Python string."""
    if value is None:
        return ""
    value = _first(value)
    if isinstance(value, str):
        return value.strip()
    import numpy as np

    if isinstance(value, np.ndarray):
        if value.size == 0:
            return ""
        if value.dtype.kind in {"U", "S"}:
            if value.ndim <= 1:
                return "".join(str(item) for item in value.flat).strip()
            rows = ["".join(str(item) for item in row.flat).rstrip() for row in value]
            return "\n".join(row for row in rows if row).strip()
        if value.dtype == object:
            return "\n".join(filter(None, (_text(item) for item in value.flat))).strip()
        return ""
    if isinstance(value, (list, tuple)):
        return "\n".join(filter(None, (_text(item) for item in value))).strip()
    return str(value).strip()


def load_figure_objects(path: str | Path) -> tuple[list[FigureNode], dict[str, Any]]:
    """Load a FIG file (MAT v5 or v7.3); returns the figure roots and a small report."""
    source = Path(path)
    try:
        from scipy.io import loadmat
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError(
            "FIG parsing requires scipy; install OpenViking with the 'matlab' extra"
        ) from exc
    try:
        values = loadmat(source, squeeze_me=False, struct_as_record=True)
    except NotImplementedError:
        # MAT v7.3 (HDF5) figures keep their handle tree; h5py reads that one.
        from openviking.parse.parsers.matlab.figures.hdf5 import load_handle_tree

        return load_handle_tree(source)
    roots: list[FigureNode] = []
    report: dict[str, Any] = {
        "variables": [],
        "skipped_variables": [],
        "mat_version": "",
        "handle_tree": "",
        "mcos_containers": [],
        "handle_tree_empty": False,
    }
    for name, value in values.items():
        if name == "__header__":
            report["mat_version"] = _header_version(value)
            continue
        if name == "__function_workspace__":
            # Saved GUI callback workspace; carries no graphics structure.
            report["skipped_variables"].append(name)
            continue
        if name.startswith("__"):
            continue
        report["variables"].append(name)
        if name.startswith("hgS_"):
            report["handle_tree"] = name
            report["handle_tree_empty"] = getattr(value, "size", 0) == 0
        if name.startswith("hgM_"):
            report["mcos_containers"].append(name)
        for item in _flatten_objects(value):
            node = build_node(item)
            if _looks_like_object(node):
                roots.append(node)

    figures = [node for node in roots if node.object_type == "figure"]
    if not figures:
        figures = _figures_inside(roots)
    if not figures and roots:
        figures = [roots[0]]
    return figures, report


def _looks_like_object(node: FigureNode) -> bool:
    return bool(node.type) or bool(node.properties) or bool(node.children)


def _figures_inside(nodes: list[FigureNode]) -> list[FigureNode]:
    found: list[FigureNode] = []
    for node in nodes:
        for item in node.walk():
            if item.object_type == "figure":
                found.append(item)
    return found


def _header_version(value: Any) -> str:
    try:
        text = value.tobytes().decode("latin-1") if hasattr(value, "tobytes") else str(value)
    except Exception:  # pragma: no cover - defensive
        return ""
    return text.strip()


def text(value: Any) -> str:
    return _text(value)


def number(value: Any) -> float | None:
    return _number(value)


def first(value: Any) -> Any:
    return _first(value)


def _clean(item: Any) -> Any:
    if isinstance(item, list):
        return [_clean(entry) for entry in item]
    if isinstance(item, bool):
        return item
    if isinstance(item, (int, float)):
        number_value = float(item)
        if math.isnan(number_value) or math.isinf(number_value):
            return None
        return item
    return None


def numbers(value: Any) -> Any:
    """Numeric MATLAB array as a vector or nested lists, NaN/Inf as null.

    The ``{1x1 cell}`` wrapper every saved property carries is removed, a row or
    column vector becomes a flat list, and a real matrix keeps its shape.
    """
    if value is None:
        return []
    import numpy as np

    raw = value
    # Unwrap the {1x1 cell} wrapper of a saved property, never a 1-element array.
    while isinstance(raw, np.ndarray) and raw.dtype == object and raw.size == 1:
        raw = raw.reshape(-1)[0]
    while isinstance(raw, (list, tuple)) and len(raw) == 1 and not isinstance(raw[0], str):
        raw = raw[0]
    if raw is None:
        return []
    if isinstance(raw, np.ndarray):
        if raw.dtype.kind in {"U", "S", "O"}:
            return []
        while raw.ndim > 1 and raw.shape[0] == 1:
            raw = raw[0]
        if raw.ndim == 2 and raw.shape[1] == 1:
            raw = raw[:, 0]
        return _clean(raw.tolist()) if raw.ndim else _clean(raw.item())
    if isinstance(raw, (bool, int, float)):
        return _clean(raw)
    if isinstance(raw, list):
        return _clean(raw)
    return []
