# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read the object payload of a FIG file saved by MATLAB R2014b or newer.

Such a figure keeps no handle tree: ``hgS_080000`` is empty and the objects are
written as MCOS records into ``__function_workspace__``. That workspace is a
mini MAT file holding ``struct{MCOS}`` → opaque ``FileWrapper__`` → one cell
array, where the cell mixes the serialized property store with the property
values themselves.

What this module reads out of it:

* the class inventory of the figure, taken from the store's own name table
  (it lists the MATLAB classes saved in the file, e.g. ``Line``, ``Bar``,
  ``Surface``, ``TiledChartLayout``);
* the plotted values that the store keeps as plain arrays, as candidate
  ``(x, y)`` pairs and as matrices, with the cell position they came from;
* labels (axis titles, legend entries, display names) that were saved as text.

The exact property names of those values live in MATLAB's private index tables
and are not decoded yet, so the values are reported as candidates with their
ranges and shapes rather than as named series.
"""

from __future__ import annotations

import io
import struct
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# MATLAB classes that draw data, as they appear in the store's name table.
CHART_CLASSES = (
    "Line",
    "Stair",
    "ErrorBar",
    "Area",
    "Scatter",
    "BubbleChart",
    "BubbleCloud",
    "Bar",
    "Stem",
    "Pie",
    "Histogram",
    "Histogram2",
    "Heatmap",
    "Contour",
    "Surface",
    "Image",
    "Quiver",
    "BoxChart",
    "WordCloud",
    "ParallelCoordinatesPlot",
    "GraphPlot",
    "ScatterHistogramChart",
    "StackedLineChart",
    "TiledChartLayout",
)

# Layout classes: they tell us about subplots and rulers, not about data.
LAYOUT_CLASSES = ("Axes", "PolarAxes", "GeographicAxes", "Figure", "Text", "Legend", "ColorBar")

_CLASS_HINTS = {name.lower(): name for name in CHART_CLASSES + LAYOUT_CLASSES}

_MC_DOUBLE = 6
_MC_CHAR = 4
_MC_CELL = 1
_MC_STRUCT = 2
_MC_OPAQUE = 17


def _tag(buffer: bytes, pos: int) -> tuple[int, int, int, int]:
    """(type, byte count, data start, next element) of the MAT element at pos."""
    word = struct.unpack("<I", buffer[pos : pos + 4])[0]
    if word >> 16:
        return word & 0xFFFF, word >> 16, pos + 4, pos + 8
    nbytes = struct.unpack("<I", buffer[pos + 4 : pos + 8])[0]
    return word, nbytes, pos + 8, pos + 8 + nbytes + ((8 - nbytes % 8) % 8)


@dataclass
class _Header:
    cls: int
    dims: tuple[int, ...]
    name_pos: int
    name_bytes: int
    body: int
    end: int


def _header(buffer: bytes, pos: int) -> _Header:
    ntype, _, data, end = _tag(buffer, pos)
    if ntype != 14:
        raise ValueError(f"no matrix at {pos} (type {ntype})")
    _, _, flags_start, after_flags = _tag(buffer, data)
    flags = struct.unpack("<I", buffer[flags_start : flags_start + 4])[0]
    ntype, nbytes, dims_start, after_dims = _tag(buffer, after_flags)
    if ntype == 5 and nbytes and nbytes % 4 == 0:
        dims = struct.unpack("<%di" % (nbytes // 4), buffer[dims_start : dims_start + nbytes])
        _, name_bytes, _, after_name = _tag(buffer, after_dims)
        return _Header(flags & 0xFF, dims, after_dims, name_bytes, after_name, end)
    return _Header(flags & 0xFF, (), after_flags, nbytes, after_dims, end)


def _find_wrapper_cell(buffer: bytes, pos: int = 8, depth: int = 0) -> int | None:
    """Position of the FileWrapper__ cell array, walking struct/opaque nesting."""
    if depth > 8 or pos >= len(buffer) - 7:
        return None
    header = _header(buffer, pos)
    if header.cls == _MC_CELL:
        return pos
    if header.cls == _MC_STRUCT:
        _, flen_bytes, flen_start, cursor = _tag(buffer, header.body)
        if not flen_bytes:
            return None
        field_length = struct.unpack("<i", buffer[flen_start : flen_start + 4])[0]
        _, names_bytes, _, cursor = _tag(buffer, cursor)
        for _ in range(max(1, names_bytes // max(field_length, 1))):
            if cursor >= len(buffer) - 7:
                return None
            found = _find_wrapper_cell(buffer, cursor, depth + 1)
            if found is not None:
                return found
            _, _, _, cursor = _tag(buffer, cursor)
        return None
    if header.cls == _MC_OPAQUE:
        _, _, _, cursor = _tag(buffer, header.body)
        _, _, _, cursor = _tag(buffer, cursor)
        return _find_wrapper_cell(buffer, cursor, depth + 1)
    return None


def _load_matrix(buffer: bytes, pos: int, name: str = "v") -> Any:
    """Load one element as a named variable, so a MAT reader decodes all of it.

    The stored elements are unnamed; the name element is rewritten in place with
    the same byte length, so every following offset stays valid.
    """
    from scipy.io import loadmat

    header = _header(buffer, pos)
    patched = bytearray(buffer)
    if header.name_bytes <= 4:
        text = name[:4].encode()
        patched[header.name_pos : header.name_pos + 8] = struct.pack(
            "<I", (len(text) << 16) | 1
        ) + text.ljust(4, b"\x00")
    else:
        patched[header.name_pos : header.name_pos + 8] = struct.pack("<II", 1, header.name_bytes)
        patched[header.name_pos + 8 : header.name_pos + 8 + header.name_bytes] = (
            name.encode().ljust(header.name_bytes, b"\x00")
        )
    document = b" " * 124 + b"\x00\x01IM" + bytes(patched[pos : header.end])
    return loadmat(io.BytesIO(document), squeeze_me=False, struct_as_record=True)[name[:4]]


@dataclass
class Entry:
    """One slot of the FileWrapper cell array."""

    index: int
    kind: str
    text: str = ""
    shape: tuple[int, ...] = ()
    values: Any = None
    fields: tuple[str, ...] = ()
    metadata: tuple[int, ...] = ()


@dataclass
class Payload:
    """Whatever the workspace yielded for one figure."""

    entries: list[Entry] = field(default_factory=list)
    store: bytes = b""
    store_names: list[str] = field(default_factory=list)
    classes: list[str] = field(default_factory=list)


def _entry_from(index: int, value: Any) -> Entry:
    import numpy as np

    if not isinstance(value, np.ndarray):
        return Entry(index=index, kind="other")
    if value.dtype.names:
        return Entry(index=index, kind="struct", fields=tuple(value.dtype.names), values=value)
    if value.dtype == object:
        items = [item for item in value.ravel() if isinstance(item, np.ndarray)]
        return Entry(index=index, kind="nested", values=items)
    if value.dtype.kind in {"U", "S"}:
        text = "".join(str(item) for item in value.ravel()).strip()
        return Entry(index=index, kind="text", text=text, shape=value.shape)
    if value.dtype.kind in {"i", "u"}:
        flat = [int(item) for item in value.ravel()[:8]]
        if value.size >= 6 and flat and flat[0] == 3707764736:
            return Entry(
                index=index, kind="metadata", metadata=tuple(int(i) for i in value.ravel())
            )
        return Entry(index=index, kind="bytes", shape=value.shape, values=value)
    if value.dtype.kind == "f":
        return Entry(index=index, kind="numbers", shape=value.shape, values=value)
    return Entry(index=index, kind="other", values=value)


def _store_names(store: bytes) -> list[str]:
    """The name table inside the property store (UTF-8, NUL separated)."""
    if len(store) < 40:
        return []
    header = struct.unpack("<10I", store[:40])
    limit = min(header[2], len(store))
    names: list[str] = []
    pos = 40
    while pos < limit - 1:
        end = store.find(b"\x00", pos)
        if end <= pos:
            break
        names.append(store[pos:end].decode("latin-1"))
        pos = end + 1
    return names


def read_payload(path: str | Path) -> Payload:
    """Decode the R2025b object payload of one FIG file."""
    from scipy.io import loadmat

    source = Path(path)
    values = loadmat(str(source), squeeze_me=False, struct_as_record=True)
    workspace = values.get("__function_workspace__")
    if workspace is None:
        return Payload()
    buffer = workspace.tobytes()
    cell_pos = _find_wrapper_cell(buffer)
    if cell_pos is None:
        return Payload()
    cell = _load_matrix(buffer, cell_pos)
    payload = Payload()
    for index in range(cell.shape[0]):
        payload.entries.append(_entry_from(index, cell[index, 0]))
    store_entry = next(
        (
            entry
            for entry in payload.entries
            if entry.kind == "bytes" and entry.shape and entry.shape[0] > 1000
        ),
        None,
    )
    if store_entry is not None:
        payload.store = bytes(store_entry.values.tobytes())
        payload.store_names = _store_names(payload.store)
    payload.classes = [
        _CLASS_HINTS[name.lower()] for name in payload.store_names if name.lower() in _CLASS_HINTS
    ]
    return payload


def _is_series(value: Any) -> bool:
    import numpy as np

    array = np.asarray(value, dtype=float).ravel()
    if array.size < 16 or array.size > 4_000_000:
        return False
    if not np.isfinite(array).any():
        return False
    return float(np.nanmin(array)) != float(np.nanmax(array))


def candidates(payload: Payload) -> dict[str, Any]:
    """Plotted values found in the payload, as pairs, matrices and vectors."""
    import numpy as np

    numeric = [
        (entry.index, np.asarray(entry.values, dtype=float))
        for entry in payload.entries
        if entry.kind == "numbers"
    ]
    pairs: list[dict[str, Any]] = []
    for position, (left_index, left) in enumerate(numeric):
        for right_index, right in numeric[position + 1 :][:3]:
            if left.size != right.size or left.size < 16:
                continue
            a, b = left.ravel(), right.ravel()
            if np.allclose(a, b):
                continue  # the same tick cache twice
            pairs.append(
                {
                    "cells": [left_index, right_index],
                    "points": int(a.size),
                    "x_like": [float(np.nanmin(a)), float(np.nanmax(a))],
                    "y_like": [float(np.nanmin(b)), float(np.nanmax(b))],
                    "x_monotonic": bool(np.all(np.diff(a) >= 0)),
                    "x": a.tolist() if a.size <= 5000 else None,
                    "y": b.tolist() if b.size <= 5000 else None,
                }
            )
            break
    matrices: list[dict[str, Any]] = []
    vectors: list[dict[str, Any]] = []
    for entry in payload.entries:
        if entry.kind == "numbers" and len(entry.shape) >= 2 and min(entry.shape) > 1:
            array = np.asarray(entry.values, dtype=float)
            matrices.append(
                {
                    "cell": entry.index,
                    "shape": list(entry.shape),
                    "range": [float(np.nanmin(array)), float(np.nanmax(array))],
                }
            )
        elif entry.kind == "numbers" and _is_series(entry.values):
            array = np.asarray(entry.values, dtype=float).ravel()
            vectors.append(
                {
                    "cell": entry.index,
                    "points": int(array.size),
                    "range": [float(np.nanmin(array)), float(np.nanmax(array))],
                }
            )
    labels = [entry.text for entry in payload.entries if entry.kind == "text" and entry.text]
    return {
        "classes": payload.classes,
        "series_pairs": pairs,
        "matrices": matrices,
        "vectors": vectors[:40],
        "labels": labels[:60],
        "store_bytes": len(payload.store),
        "store_names": len(payload.store_names),
    }
