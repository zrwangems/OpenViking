# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""MAT-file structure and complete, searchable array exports (no MATLAB execution)."""

from __future__ import annotations

import csv
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


def _number(value: Any) -> str:
    import numpy as np

    scalar = np.asarray(value).reshape(-1)[0]
    if np.issubdtype(scalar.dtype, np.floating):
        return format(float(scalar), ".17g")
    if np.issubdtype(scalar.dtype, np.complexfloating):
        return format(complex(scalar), ".17g")
    if np.issubdtype(scalar.dtype, np.bool_):
        return "true" if bool(scalar) else "false"
    return str(scalar.item() if hasattr(scalar, "item") else scalar)


_MAX_CSV_COLUMNS = 4096


def _is_scalar(array: Any) -> bool:
    import numpy as np

    return array.size == 1 and array.ndim <= 2 and not np.issubdtype(
        array.dtype, np.complexfloating
    )


def _csv_grid(array: Any) -> tuple[list[list[str]], dict[str, Any]]:
    """Lay an array out as a 2-D grid of values, plus the JSONL pointer fields.

    A CSV cell is a single number, so only a 2-D grid is native: vectors become a
    single column, matrices keep their rows and columns, and anything with three
    or more dimensions is flattened column-major (MATLAB order) to
    ``dims[0] x prod(dims[1:])`` and reported as ``order: F`` so it can be
    reshaped back losslessly. A grid too wide to read as one matrix falls back to
    a long table with one row per element and explicit index columns.
    """
    import numpy as np

    shape = [int(part) for part in array.shape]
    complex_values = np.issubdtype(array.dtype, np.complexfloating)
    pointer: dict[str, Any] = {}
    if not shape or min(shape) == 1 or len(shape) == 1:
        grid = [[_cell(item)] for item in array.reshape(-1, order="F")]
        rows, cols = len(grid), 1
    elif len(shape) == 2:
        grid = [
            [_cell(array[row, column]) for column in range(shape[1])]
            for row in range(shape[0])
        ]
        rows, cols = shape[0], shape[1]
    elif int(np.prod(shape[1:])) > _MAX_CSV_COLUMNS:
        rows, cols = int(np.prod(shape)), len(shape) + (2 if complex_values else 1)
        header = [f"dim_{index + 1}" for index in range(len(shape))]
        header += ["real", "imag"] if complex_values else ["value"]
        grid = [header]
        # Column-major (MATLAB) order, matching the flat grid layout above.
        for index in _matlab_index_order(shape):
            coordinates = [str(part + 1) for part in index]
            item = array[index]
            if complex_values:
                grid.append([*coordinates, _number(item.real), _number(item.imag)])
            else:
                grid.append([*coordinates, _cell(item)])
        pointer["layout"] = "long"
        pointer["shape"] = shape
        return grid, pointer
    else:
        flat = np.reshape(array, (shape[0], int(np.prod(shape[1:]))), order="F")
        grid = [
            [_cell(flat[row, column]) for column in range(flat.shape[1])]
            for row in range(flat.shape[0])
        ]
        rows, cols = int(flat.shape[0]), int(flat.shape[1])
        pointer["order"] = "F"
        pointer["shape"] = shape
    if complex_values and "layout" not in pointer:
        interleaved = []
        dense = np.asarray(array)
        flat = np.reshape(dense, (-1,), order="F")
        for row in range(rows):
            line: list[str] = []
            for column in range(cols):
                item = flat[row * cols + column]
                line.extend([_number(item.real), _number(item.imag)])
            interleaved.append(line)
        grid = interleaved
        cols *= 2
    pointer["rows"] = rows
    pointer["cols"] = cols
    return grid, pointer


def _matlab_index_order(shape: list[int]):
    from itertools import product

    for index in product(*[range(part) for part in reversed(shape)]):
        yield tuple(reversed(index))


def _cell(value: Any) -> str:
    import numpy as np

    item = np.asarray(value)
    if item.dtype.kind in {"U", "S"}:
        return str(value).strip()
    return _number(value)


def _grid_csv(grid: list[list[str]]) -> str:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerows(grid)
    return output.getvalue()


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


def _csv_name(index: int, path: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", path).strip("._")[:80] or "array"
    digest = hashlib.sha256(path.encode("utf-8")).hexdigest()[:8]
    return f"data/{index:04d}_{stem}_{digest}.csv"


def parse_mat_documents(path: str | Path) -> tuple[dict[str, str], list[str]]:
    """Return a summary page and lossless CSV documents for all readable arrays.

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
            grid, pointer = _csv_grid(dense)
            name = _csv_name(index, array_path)
            documents[name] = _grid_csv(grid)
            row["data"] = name
            row.update(pointer)
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
