# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""MAT-file structure and complete, searchable array exports (no MATLAB execution)."""

from __future__ import annotations

import csv
import hashlib
import io
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


def _array_csv(value: Any) -> str:
    """Serialize an N-D array without truncation; indices are one-based."""
    import numpy as np
    from scipy import sparse

    array = value.toarray() if sparse.issparse(value) else np.asarray(value)
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    complex_values = np.issubdtype(array.dtype, np.complexfloating)
    if array.ndim == 2:
        indices = ["row", "column"]
    else:
        indices = [f"dim_{index + 1}" for index in range(array.ndim)]
    writer.writerow([*indices, "real", "imag"] if complex_values else [*indices, "value"])
    for index in np.ndindex(array.shape):
        item = array[index]
        coordinates = [str(part + 1) for part in index]
        if complex_values:
            writer.writerow([*coordinates, _number(item.real), _number(item.imag)])
        else:
            writer.writerow([*coordinates, _number(item)])
    return output.getvalue()


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
    lines = [
        "---",
        "type: matlab-data",
        "---",
        "",
        f"# {path.name}",
        "",
        f"格式：{fmt}。所有可读取的数值、逻辑和字符数组均完整导出为 CSV，不使用预览截断。CSV 索引从 1 开始，浮点数使用可往返精度。",
        "",
        "| 变量 | 维度 | MATLAB / 存储类型 | 结构字段或值预览 |",
        "| --- | --- | --- | --- |",
    ]
    count = 0
    for name, value in values.items():
        if name.startswith("__"):
            continue
        shape = hdf_shapes[name] if name in hdf_shapes else getattr(value, "shape", None)
        dtype = hdf_dtypes[name] if name in hdf_dtypes else getattr(value, "dtype", None)
        kind = str(dtype) if dtype is not None else type(value).__name__
        dimensions = " × ".join(str(v) for v in shape) if shape is not None else "未知"
        if name == "None":
            name = "未知名（MATLAB opaque 对象）"
            warnings.append(
                f"{path.name}: SciPy 无法恢复 MATLAB opaque 对象本身及其变量名；已完整导出其中可读取的数组"
            )
        preview = (
            hdf_previews.get(name, _preview(value))
            .replace("|", "\\|")
            .replace("\r", "")
            .replace("\n", "<br>")
        )
        lines.append(f"| {name} | {dimensions} | {kind} | {preview} |")
        count += 1
    if not count:
        lines.append("| - | - | - | 未读取到顶层变量 |")

    documents = {f"{path.name}.md": ""}
    lines.extend(["", "## 全量数组数据", ""])
    if arrays:
        lines.extend(["| 数组路径 | 维度 | 类型 | 完整数据 |", "| --- | --- | --- | --- |"])
        for index, (array_path, value) in enumerate(arrays, 1):
            name = _csv_name(index, array_path)
            documents[name] = _array_csv(value)
            shape = getattr(value, "shape", ())
            dimensions = " × ".join(str(part) for part in shape) or "标量"
            escaped_path = array_path.replace("|", "\\|")
            lines.append(
                f"| `{escaped_path}` | {dimensions} | `{getattr(value, 'dtype', type(value).__name__)}` | [{name.removeprefix('data/')}]({name}) |"
            )
    else:
        lines.append("未读取到可导出的数组。")
    lines.extend(["", f"原始文件头：`{str(header).strip()}`", ""])
    documents[f"{path.name}.md"] = "\n".join(lines)
    return documents, warnings


def parse_mat(path: str | Path) -> tuple[str, list[str]]:
    documents, warnings = parse_mat_documents(path)
    return documents[f"{Path(path).name}.md"], warnings
