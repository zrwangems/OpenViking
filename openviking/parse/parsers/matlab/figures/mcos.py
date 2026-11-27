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


def store_bounds(store: bytes) -> tuple[int, int]:
    """``(start, end)`` byte bounds of the store's value stream.

    The first ten uint32 words of a store are a directory whose third word ends
    the name table and whose sixth and seventh words bound the value stream.
    The values are per file, so they must be read, not assumed.
    """
    if len(store) < 40:
        return 0, 0
    header = struct.unpack("<10I", store[:40])
    start = min(max(header[5], 40), len(store))
    end = min(max(header[6], start), len(store))
    return start, end


def property_records(payload: Payload) -> list[tuple[int, int, str]]:
    """``(flag, reference, property name)`` records of the store's value stream.

    A record is three uint32 words: a flag, a reference and the index of the
    property name. The stream is re-synchronised word by word, so a record of a
    different width elsewhere does not shift everything after it.
    """
    import numpy as np

    if not payload.store:
        return []
    start, end = store_bounds(payload.store)
    if end <= start:
        return []
    words = np.frombuffer(payload.store[start:end], dtype="<u4")
    properties = {
        index: name
        for index, name in enumerate(payload.store_names)
        if name and ("_" in name or name.endswith("Mode"))
    }
    limit = len(payload.entries) + 8
    records: list[tuple[int, int, str]] = []
    position = 0
    while position < len(words) - 2:
        flag, reference, name_index = (
            int(words[position]),
            int(words[position + 1]),
            int(words[position + 2]),
        )
        if flag in (0, 1) and name_index in properties and reference < limit:
            records.append((flag, reference, properties[name_index]))
            position += 3
        else:
            position += 1
    return records


# Properties whose value is a plotted array. The store keeps the coordinates a
# chart needs immediately before the value it is drawn from.
_DATA_PROPERTIES = (
    "XData_I",
    "YData_I",
    "ZData_I",
    "ThetaData_I",
    "RData_I",
    "Values_I",
    "BinEdges_I",
    "Counts_I",
)

# A histogram keeps its bin edges on the other side of the counts.
_HISTOGRAM_PROPERTIES = ("BinEdges_I", "Counts_I")

# Properties whose value is a string shown with the chart (labels, legends).
_TEXT_PROPERTIES = ("String_I", "Label_I", "DisplayName_I", "Title_I")

# Values of one object are stored as a run of arrays, and the record for a data
# property points at that run: its plotted array is three slots past the
# reference, with the coordinates the chart needs right before it.
_PRIMARY_OFFSET = 3
_INLINE_LIMIT = 5000


def _array_at(payload: Payload, slot: int, smallest: int = 3):
    """The numeric slot as an ndarray, or None when it is not usable data."""
    import numpy as np

    if not 0 <= slot < len(payload.entries):
        return None
    entry = payload.entries[slot]
    if entry.kind != "numbers":
        return None
    array = np.asarray(entry.values, dtype=float)
    if array.size < smallest or not np.isfinite(array).any():
        return None
    return array


def _value_blocks(payload: Payload) -> list[dict[str, Any]]:
    """Value runs of the serialized objects, one per plotted array.

    Each run is the plotted array (``primary``) plus the coordinate arrays
    stored right before it. A run that turns out to be the coordinates of a
    longer run is dropped, which also removes the duplicate record that
    ``XData`` leaves behind for charts whose x is stored inside the y run.
    """
    blocks: list[dict[str, Any]] = []
    for _flag, reference, name in property_records(payload):
        if name not in _DATA_PROPERTIES:
            continue
        primary_slot = reference + _PRIMARY_OFFSET
        primary = _array_at(payload, primary_slot)
        if primary is None or _is_limit_table(primary):
            continue
        shape = tuple(primary.shape)
        wanted = primary.size if min(shape) == 1 else min(shape)
        leading: list[tuple[int, Any]] = []
        slot = primary_slot - 1
        while len(leading) < 3:
            array = _array_at(payload, slot, smallest=wanted)
            if array is None or array.size != wanted:
                break
            leading.insert(0, (slot, array))
            slot -= 1
        blocks.append(
            {
                "property": name,
                "primary_slot": primary_slot,
                "primary": primary,
                "leading": leading,
            }
        )
    coordinates = {slot for block in blocks for slot, _ in block["leading"]}
    kept: list[dict[str, Any]] = []
    seen: set[tuple[Any, ...]] = set()
    for block in blocks:
        if block["primary_slot"] in coordinates:
            continue
        key = (block["primary_slot"], tuple(slot for slot, _ in block["leading"]))
        if key in seen:
            continue
        seen.add(key)
        kept.append(block)
    return kept


def series(payload: Payload) -> list[dict[str, Any]]:
    """Plotted data as ``x``/``y`` (or ``x``/``y``/``z``) series.

    Verified against ``137_fig_hgsave_v6.fig``, which carries the same kind of
    figure twice: the 30 line series recovered here match the handle tree's
    ``XData``/``YData`` in length and range, with no series the handle tree does
    not have. Over the gallery corpus a coordinate array precedes the values in
    466 of 659 runs; the rest are drawn against a ``1:n`` index.
    """
    import numpy as np

    found: list[dict[str, Any]] = []
    for block in _value_blocks(payload):
        primary = block["primary"]
        leading = [array for _slot, array in block["leading"]]
        shape = list(primary.shape)
        item: dict[str, Any] = {
            "property": block["property"],
            "shape": shape,
            "points": int(primary.size),
        }
        flat = primary.ravel()
        if block["property"] in _HISTOGRAM_PROPERTIES:
            edges = _array_at(payload, block["primary_slot"] + 1, smallest=flat.size + 1)
            if edges is not None and edges.size == flat.size + 1:
                edges = edges.ravel()
                item["bin_edges"] = _listed(edges)
                item["x"] = _listed(edges[:-1])
                item["y"] = _listed(flat)
                item["x_range"] = [float(edges[0]), float(edges[-1])]
                item["y_range"] = [float(np.nanmin(flat)), float(np.nanmax(flat))]
                found.append(item)
                continue
        if min(shape) == 1:
            x = leading[-1].ravel() if leading else np.arange(1, flat.size + 1, dtype=float)
            y = flat
            item["index"] = not leading
            item["x"] = _listed(x)
            item["y"] = _listed(y)
            item["x_range"] = [float(np.nanmin(x)), float(np.nanmax(x))]
            item["y_range"] = [float(np.nanmin(y)), float(np.nanmax(y))]
        else:
            x = leading[0].ravel() if leading else None
            y = leading[1].ravel() if len(leading) > 1 else None
            z = primary
            item["x"] = _listed(x) if x is not None else None
            item["y"] = _listed(y) if y is not None else None
            item["z"] = _listed(z)
            item["x_range"] = [float(np.nanmin(x)), float(np.nanmax(x))] if x is not None else None
            item["y_range"] = [float(np.nanmin(y)), float(np.nanmax(y))] if y is not None else None
            item["z_range"] = [float(np.nanmin(z)), float(np.nanmax(z))]
        found.append(item)
    return found


def _is_limit_table(array) -> bool:
    """``[xlim; ylim; zlim]`` is stored like data but is the axes' own range."""
    shape = array.shape
    return len(shape) == 2 and shape[1] == 2 and shape[0] in (2, 3)


def _listed(array) -> list[float] | None:
    """The array as plain floats, or None when it is too large to inline."""
    import numpy as np

    if array is None or np.size(array) > _INLINE_LIMIT:
        return None
    return [float(value) for value in np.asarray(array, dtype=float).ravel()]


def texts(payload: Payload) -> list[str]:
    """Strings the figure shows: axis labels, titles, legends, annotations.

    They are stored like data: the record names the property, and the string
    sits at the same offset past its reference. ``XLabel``/``YLabel`` of a plain
    line figure come out as the two strings its author typed.
    """
    found: list[str] = []
    names = set(payload.store_names)
    for _flag, reference, name in property_records(payload):
        if name not in _TEXT_PROPERTIES:
            continue
        slot = reference + _PRIMARY_OFFSET
        if not 0 <= slot < len(payload.entries):
            continue
        entry = payload.entries[slot]
        if entry.kind != "text" or not entry.text or entry.text in found:
            continue
        if entry.text in names:
            # Schema names ("Axes Camera", property groups) are not figure text.
            continue
        found.append(entry.text)
    return found


def property_names_seen(
    payload: Payload, start: int | None = None, end: int | None = None
) -> list[str]:
    """Property names referenced by the store's value stream.

    The stream interleaves a value reference, a flag and the index of the
    property name it belongs to, so scanning for words that are property-name
    indices recovers which properties a figure serialized. Verified by diffing
    two figures that differ in one property set (log scales add XScale_I,
    ScaleMode, MinorTick_I …). The name-to-value link is not decoded yet.
    """
    import numpy as np

    if not payload.store:
        return []
    words = np.frombuffer(payload.store[: (len(payload.store) // 4) * 4], dtype="<u4")
    properties = {
        index: name
        for index, name in enumerate(payload.store_names)
        if name and ("_" in name or name.endswith("Mode"))
    }
    if start is None or end is None:
        first, last = store_bounds(payload.store)
        start = first if start is None else start
        end = last if end is None else end
    seen: list[str] = []
    for position in range(start // 4, min(end // 4, len(words))):
        index = int(words[position])
        name = properties.get(index)
        if name and (not seen or seen[-1] != name):
            seen.append(name)
    return seen


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
            if np.allclose(b, np.arange(1, b.size + 1)) or float(np.nanmax(a)) == float(
                np.nanmin(a)
            ):
                continue  # patch face indices, not plotted values
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
            if _is_limit_table(array) or entry.shape == (16, 16):
                # Axis ranges and the 16×16 cursor bitmap are stored like data.
                continue
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
