# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""MAT-file structure and complete, searchable array exports (no MATLAB execution)."""

from __future__ import annotations

import hashlib
import io
import json
import re
from pathlib import Path
from typing import Any, Iterator


def _preview(value: Any, limit: int = 12) -> str:
    try:
        import numpy as np

        if isinstance(value, np.ndarray):
            if value.dtype.names:
                fields = ", ".join(value.dtype.names)
                return f"struct fields: {fields}"
            if value.dtype == object:
                flat = value.ravel()
                return "; ".join(_preview(item, 3) for item in flat[:3]) or "empty cell"
            if value.size <= limit:
                return np.array2string(value, threshold=limit, edgeitems=4)
            flat = value.ravel()
            return f"first values: {np.array2string(flat[:limit], precision=6)}"
    except ImportError:
        pass
    text = repr(value)
    return text if len(text) <= 300 else text[:297] + "..."


def _walk_arrays(value: Any, path: str, depth: int = 0) -> Iterator[tuple[str, Any]]:
    """Yield every scalar/string/numeric array, including struct and cell members."""
    import numpy as np
    from scipy import sparse

    if depth > 64:
        return
    if sparse.issparse(value):
        yield path, value
        return
    if isinstance(value, np.ndarray):
        if value.dtype.names:
            for index, item in enumerate(value.flat):
                for field in value.dtype.names:
                    yield from _walk_arrays(item[field], f"{path}[{index + 1}].{field}", depth + 1)
            return
        if value.dtype == object:
            for index, item in enumerate(value.flat):
                yield from _walk_arrays(item, f"{path}[{index + 1}]", depth + 1)
            return
        yield path, value
        return
    # MatlabOpaque stores its recoverable metadata in an ``arr`` field. The
    # opaque object itself remains explicitly marked as not fully recoverable.
    fields = getattr(value, "_fieldnames", None)
    if fields:
        for field in fields:
            if field in {"s0", "s1", "s2"}:
                continue
            try:
                item = getattr(value, field)
            except (AttributeError, ValueError):
                continue
            yield from _walk_arrays(item, f"{path}.{field}", depth + 1)


def _npy_document(array: Any) -> bytes:
    """Serialize an N-D array as a standalone .npy file (dtype and shape inside)."""
    import numpy as np

    buffer = io.BytesIO()
    np.save(buffer, np.ascontiguousarray(array), allow_pickle=False)
    return buffer.getvalue()


def _npy_dtype(array: Any) -> str:
    import numpy as np

    dtype = np.asarray(array).dtype
    return dtype.name if dtype.names is None else "struct"


def _is_scalar(array: Any) -> bool:
    import numpy as np

    return array.size == 1 and array.ndim <= 2 and not np.issubdtype(
        array.dtype, np.complexfloating
    )


def _matlab_class(value: Any) -> str:
    try:
        import numpy as np
        from scipy import sparse

        if sparse.issparse(value):
            return "double"
        dtype = np.asarray(value).dtype
        if dtype.names:
            return "struct"
        if dtype.kind == "f":
            return "double" if dtype.itemsize <= 8 else "single"
        if dtype.kind == "c":
            return "double"
        if dtype.kind == "b":
            return "logical"
        if dtype.kind in {"i", "u"}:
            return dtype.name
        if dtype.kind in {"U", "S"}:
            return "char"
        return str(dtype)
    except ImportError:
        return str(getattr(value, "dtype", type(value).__name__))


def _npy_name(index: int, path: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", path).strip("._")[:80] or "array"
    digest = hashlib.sha256(path.encode("utf-8")).hexdigest()[:8]
    return f"data/{index:04d}_{stem}_{digest}.npy"


def parse_mat_documents(path: str | Path) -> tuple[dict[str, str | bytes], list[str]]:
    """Return the entries JSONL page and lossless .npy documents for all arrays.

    Only a 1x1 value is written into the JSONL line; every other array becomes a
    ``.npy`` file, which carries its own dtype and shape and needs no index
    columns, no flattening and no separate metadata to be read back exactly.

    Opaque MATLAB objects are still bounded by SciPy's format support: their
    recoverable arrays are exported, and a warning says that the object itself
    was not reconstructed. No original MAT bytes are turned into text resources.
    """
    path = Path(path)
    warnings: list[str] = []
    try:
        from scipy.io import loadmat
    except ImportError as exc:
        raise RuntimeError(
            "MAT parsing requires scipy; install OpenViking with the 'matlab' extra"
        ) from exc

    try:
        with path.open("rb") as stream:
            is_hdf5 = stream.read(8) == b"\x89HDF\r\n\x1a\n"
        if is_hdf5:
            raise NotImplementedError("MAT v7.3 uses HDF5")
        values = loadmat(path, squeeze_me=False, struct_as_record=True)
        fmt = "MAT v5/v7 (SciPy)"
    except NotImplementedError:
        try:
            import h5py
        except ImportError as exc:
            raise RuntimeError(
                "MAT v7.3 parsing requires h5py; install OpenViking with the 'matlab' extra"
            ) from exc
        arrays: list[tuple[str, Any]] = []
        hdf_shapes: dict[str, tuple[int, ...] | None] = {}
        hdf_dtypes: dict[str, str] = {}
        hdf_previews: dict[str, str] = {}
        with h5py.File(path, "r") as handle:
            values = {name: handle[name] for name in handle.keys() if name != "#refs#"}
            for name, dataset in values.items():
                hdf_shapes[name] = getattr(dataset, "shape", None)
                hdf_dtypes[name] = str(getattr(dataset, "dtype", "group"))
                if isinstance(dataset, h5py.Group):
                    hdf_previews[name] = "group fields: " + ", ".join(dataset.keys())
                else:
                    hdf_previews[name] = _preview(dataset[()])

            def collect_dataset(name: str, dataset: Any) -> None:
                if name.startswith("#refs#") or "/#refs#/" in name:
                    return
                if isinstance(dataset, h5py.Dataset):
                    if h5py.check_dtype(ref=dataset.dtype) is not None:
                        # Simulink signal-editor files store HDF5 references;
                        # they point at #refs# objects rather than numeric data.
                        hdf_previews[name] = (
                            f"HDF5 reference array {getattr(dataset, 'shape', '')}".strip()
                        )
                        warnings.append(
                            f"{path.name}: `{name}` 是 HDF5 引用数组，"
                            "引用目标未作为数组展开；原件保留"
                        )
                        return
                    arrays.append((name, dataset[()]))

            handle.visititems(collect_dataset)
        fmt = "MAT v7.3 (HDF5)"
    else:
        hdf_shapes = {}
        hdf_dtypes = {}
        hdf_previews = {}
        arrays = []
        for name, value in values.items():
            if name.startswith("__"):
                continue
            export_name = "opaque_object" if name == "None" else name
            arrays.extend(_walk_arrays(value, export_name))

    header = values.get("__header__", b"")
    if isinstance(header, bytes):
        header = header.decode("latin-1", errors="replace")
    documents: dict[str, str] = {}
    entries: list[dict[str, Any]] = [
        {
            "kind": "file",
            "schema": "ov.matlab.entries/1",
            "file": path.name,
            "mat_version": "v7.3" if fmt.startswith("MAT v7.3") else "v7",
            "header": str(header).strip() or None,
            "entry_count": len(arrays),
        }
    ]
    for index, (array_path, value) in enumerate(arrays, 1):
        import numpy as np
        from scipy import sparse

        dense = np.asarray(value.toarray() if sparse.issparse(value) else value)
        row: dict[str, Any] = {
            "kind": "value",
            "name": array_path,
            "class": _matlab_class(value),
            "dims": [int(part) for part in dense.shape],
            "complex": "complex" in str(dense.dtype),
            "sparse": sparse.issparse(value),
        }
        if _is_scalar(dense):
            row["value"] = _scalar_json(dense.reshape(-1)[0])
        else:
            name = _npy_name(index, array_path)
            documents[name] = _npy_document(dense)
            row["data"] = name
            row["format"] = "npy"
            row["dtype"] = _npy_dtype(dense)
        entries.append(row)
    documents["entries.jsonl"] = (
        "\n".join(json.dumps(entry, ensure_ascii=False) for entry in entries) + "\n"
    )
    return documents, warnings


def _scalar_json(value: Any) -> Any:
    """JSON-native inline value for a 1x1 array; only such values stay in JSONL."""
    import numpy as np

    item = np.asarray(value)
    if item.dtype.kind in {"U", "S"}:
        return str(value).strip()
    if item.dtype.kind == "b":
        return bool(value)
    if item.dtype.kind in {"i", "u"}:
        return int(value)
    return float(value)


def parse_mat(path: str | Path) -> tuple[str, list[str]]:
    documents, warnings = parse_mat_documents(path)
    return documents["entries.jsonl"], warnings
