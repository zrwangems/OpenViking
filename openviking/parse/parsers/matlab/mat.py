# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""MAT-file metadata and bounded value previews (no MATLAB execution)."""

from __future__ import annotations

from pathlib import Path
from typing import Any


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


def parse_mat(path: str | Path) -> tuple[str, list[str]]:
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
        hdf_previews: dict[str, str] = {}
        hdf_shapes: dict[str, tuple[int, ...] | None] = {}
        hdf_dtypes: dict[str, str] = {}
        with h5py.File(path, "r") as handle:
            values = {name: handle[name] for name in handle.keys() if name != "#refs#"}
            # HDF5 datasets are closed with the file; capture bounded previews now.
            for name, dataset in values.items():
                hdf_shapes[name] = getattr(dataset, "shape", None)
                hdf_dtypes[name] = str(getattr(dataset, "dtype", "group"))
                try:
                    if isinstance(dataset, h5py.Group):
                        hdf_previews[name] = "group fields: " + ", ".join(dataset.keys())
                        continue
                    sample = (
                        dataset[()]
                        if dataset.size <= 12
                        else dataset[tuple(0 for _ in dataset.shape)]
                    )
                    hdf_previews[name] = _preview(sample)
                except (OSError, ValueError, RuntimeError) as exc:
                    hdf_previews[name] = f"preview unavailable: {exc}"
        fmt = "MAT v7.3 (HDF5)"
    else:
        hdf_previews = {}
        hdf_shapes = {}
        hdf_dtypes = {}
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
        f"格式：{fmt}。数组只生成有界预览，完整数值仍保留在原始 MAT 文件中。",
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
                f"{path.name}: SciPy 无法恢复至少一个 MATLAB opaque 对象的变量名，仅保留类型信息"
            )
        preview = (
            (hdf_previews.get(name) or _preview(value))
            .replace("|", "\\|")
            .replace("\r", "")
            .replace("\n", "<br>")
        )
        lines.append(f"| {name} | {dimensions} | {kind} | {preview} |")
        count += 1
    if not count:
        lines.append("| - | - | - | 未读取到顶层变量 |")
    lines.extend(["", f"原始文件头：`{str(header).strip()}`", ""])
    return "\n".join(lines), warnings
