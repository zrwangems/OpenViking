# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read a FIG file saved as MAT v7.3 (HDF5) with h5py.

``hgsave -v7.3`` writes the figure as HDF5 (the format meant for figures over
2 GB). Unlike the R2025b default, such a file keeps the handle tree in
``hgS_070000``: a struct with ``type``, ``handle``, ``properties``, ``children``
and ``special`` per object, exactly the shape the MAT v5 reader expects. This
module decodes that tree with h5py so the same extraction layer applies.

MAT v7.3 stores each value as an HDF5 dataset tagged with ``MATLAB_class``:
``char`` is a code array (UTF-16 when ``MATLAB_int_decode`` is 2), ``cell`` is a
dataset of references, and a struct array is a group whose fields are reference
datasets of the same shape.
"""

from __future__ import annotations

import struct
from pathlib import Path
from typing import Any

from openviking.parse.parsers.matlab.figures.nodes import FigureNode, number, text

_EMPTY_CLASSES = {"canonical empty"}


def _matlab_class(obj: Any) -> str:
    value = obj.attrs.get("MATLAB_class")
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("latin-1")
    if hasattr(value, "tobytes"):
        return value.tobytes().decode("latin-1").rstrip("\x00")
    return str(value)


def _fields(obj: Any) -> list[str]:
    """MATLAB_fields is a 1-D array of per-character byte arrays."""
    raw = obj.attrs.get("MATLAB_fields")
    if raw is None:
        return []
    names = []
    for name in raw:
        if isinstance(name, bytes):
            names.append(name.decode("latin-1"))
        else:
            names.append(b"".join(bytes(item) for item in name).decode("latin-1"))
    return names


def _decode_char(dataset: Any) -> str:
    codes = dataset[()]
    if hasattr(codes, "ravel"):
        codes = codes.ravel()
    data = b"".join(struct.pack("<H", int(code) & 0xFFFF) for code in codes)
    if dataset.attrs.get("MATLAB_int_decode") == 2:
        return data.decode("utf-16-le", errors="replace").rstrip("\x00")
    return data.decode("latin-1", errors="replace").rstrip("\x00")


def _decode(handle: Any, owner: Any) -> Any:
    """One stored value as a Python object."""
    import h5py
    import numpy as np

    if isinstance(handle, h5py.Reference):
        handle = owner[handle]
    if handle is None:
        return None
    matlab_class = _matlab_class(handle)
    if isinstance(handle, h5py.Dataset):
        if matlab_class == "char":
            return _decode_char(handle)
        if handle.attrs.get("MATLAB_empty") or matlab_class in _EMPTY_CLASSES:
            return []
        if handle.dtype == object:  # a cell or a struct array: stored as references
            references = handle[()]
            if hasattr(references, "ravel"):
                return [_decode(ref, handle.file) for ref in references.ravel()]
            return _decode(references, handle.file)
        data = handle[()]
        if isinstance(data, np.ndarray) and data.dtype.kind in {"i", "u", "f", "b"}:
            return data
        return data
    if isinstance(handle, h5py.Group):
        fields = _fields(handle)
        if not fields:
            return {}
        values = {field: handle[field] for field in fields}
        reference_fields = [
            value
            for value in values.values()
            if isinstance(value, h5py.Dataset) and value.dtype == object
        ]
        if len(reference_fields) == len(values) and reference_fields:
            shape = reference_fields[0].shape
            if len(shape) > 1 and all(value.shape == shape for value in reference_fields):
                elements = []
                for index in range(shape[0] * shape[1]):
                    row, column = divmod(index, shape[1])
                    elements.append(
                        {
                            field: _decode(values[field][row, column], handle.file)
                            for field in fields
                        }
                    )
                return elements
        return {field: _decode(value, handle.file) for field, value in values.items()}
    return None


def _node(value: Any, depth: int = 0) -> FigureNode | None:
    """Turn one decoded object struct into a FigureNode."""
    if not isinstance(value, dict):
        return None
    node = FigureNode(
        type=text(value.get("type")) if not isinstance(value.get("type"), str) else value["type"],
        handle=number(value.get("handle")),
    )
    properties = value.get("properties")
    if isinstance(properties, dict):
        node.properties = properties
    children = value.get("children")
    if isinstance(children, dict):
        children = [children]
    if isinstance(children, list) and depth < 32:
        for child in children:
            child_node = _node(child, depth + 1)
            if child_node is not None:
                node.children.append(child_node)
    return node


def load_handle_tree(path: str | Path) -> tuple[list[FigureNode], dict[str, Any]]:
    """Figure roots and a small report, read from a MAT v7.3 FIG file."""
    try:
        import h5py
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise NotImplementedError(
            "FIG files saved as MAT v7.3 need h5py; install OpenViking with the 'matlab' extra"
        ) from exc

    source = Path(path)
    roots: list[FigureNode] = []
    report: dict[str, Any] = {
        "variables": [],
        "skipped_variables": [],
        "mat_version": "MATLAB 7.3 (HDF5)",
        "handle_tree": "",
        "mcos_containers": [],
        "handle_tree_empty": False,
    }
    with h5py.File(source, "r") as archive:
        for name in archive.keys():
            if name.startswith("#"):
                continue
            report["variables"].append(name)
            if name.startswith("hgS_"):
                report["handle_tree"] = name
            if name.startswith("hgM_"):
                report["mcos_containers"].append(name)
        tree_name = report["handle_tree"] or "hgS_070000"
        if tree_name in archive:
            decoded = _decode(archive[tree_name], archive)
            items = decoded if isinstance(decoded, list) else [decoded]
            for item in items:
                node = _node(item)
                if node is not None and node.type:
                    roots.append(node)
            report["handle_tree_empty"] = not roots
    figures = [node for node in roots if node.object_type == "figure"]
    if not figures:
        figures = [item for node in roots for item in node.walk() if item.object_type == "figure"]
    if not figures:
        figures = roots
    return figures, report
