# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Extract chart type, series data and annotations from a MATLAB FIG file.

The output keeps what the figure says about itself — which chart it is, the
values it plots, the titles, axis labels, legend entries and free text — and
drops the rendering-only property noise that made the old object dump
unusable. Values too large to inline are written next to the JSON as .npy
files and referenced, so no plotted number is lost.
"""

from __future__ import annotations

import io
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

from openviking.parse.parsers.matlab.figures.catalog import (
    KIND_LABELS,
    PLOT_GALLERY_URL,
    gallery_size,
)
from openviking.parse.parsers.matlab.figures.classify import (
    ChartType,
    classify,
    decoration_role,
    is_axes,
)
from openviking.parse.parsers.matlab.figures.nodes import (
    FigureNode,
    load_figure_objects,
    numbers,
    text,
)

FIGURE_SCHEMA = "ov.matlab.figure/2"

# Values per series kept inside figure.json; larger series go to .npy files.
INLINE_LIMIT = 500

_BOUNDARY = (
    "Handle-tree figures (hgS_070000, everything saved before R2014b and hgsave -v6) "
    "are read for chart type, plotted values, titles, axis labels, legend and free "
    "text. Since R2014b the object graph is written as MCOS objects (hgS_080000 is "
    "empty, hgM_070000/080000 carry opaque records), which this reader does not "
    "decode yet. Pixels are never rendered and callbacks never run; MAT v7.3 "
    "(HDF5) files cannot be read with scipy at all."
)

STATUS_PARSED = "parsed"
STATUS_MCOS_ONLY = "unreadable_mcos"
STATUS_V73 = "unsupported_v73"

_SKIP_CHILDREN = {"legend", "colorbar", "text", "rectangle", "decoration", "uicontrol"}


@dataclass
class Series:
    """One plotted data series."""

    name: str
    fields: dict[str, Any]

    @property
    def points(self) -> int:
        for value in self.fields.values():
            count = _count(value)
            if count:
                return count
        return 0


def _count(value: Any) -> int:
    if isinstance(value, list):
        return sum(_count(item) for item in value) if value else 0
    return 0 if value is None else 1


def _flatten(value: Any) -> list[float]:
    if isinstance(value, list):
        result: list[float] = []
        for item in value:
            result.extend(_flatten(item))
        return result
    if isinstance(value, bool) or value is None:
        return []
    if isinstance(value, (int, float)):
        return [float(value)]
    return []


def _range(value: Any) -> list[float] | None:
    flat = [item for item in _flatten(value) if not math.isnan(item)]
    if not flat:
        return None
    return [min(flat), max(flat)]


def _arr(node: FigureNode, *names: str) -> Any:
    for name in names:
        value = node.get(name)
        if value is None:
            continue
        converted = numbers(value)
        if _count(converted):
            return converted
    return None


def _flag(node: FigureNode, name: str) -> str:
    return text(node.get(name)).lower()


# --- per-kind series extraction -------------------------------------------------


def _line(node: FigureNode, chart: ChartType) -> list[Series]:
    name = _series_name(node, "线")
    if chart.kind == "polar":
        return [Series(name, {"theta": _arr(node, "ThetaData"), "r": _arr(node, "RData")})]
    if chart.kind == "geo":
        return [
            Series(
                name,
                {
                    "latitude": _arr(node, "LatitudeData"),
                    "longitude": _arr(node, "LongitudeData"),
                },
            )
        ]
    fields = {"x": _arr(node, "XData"), "y": _arr(node, "YData")}
    if node.has("ZData"):
        fields["z"] = _arr(node, "ZData")
    return [Series(name, fields)]


def _stairs(node: FigureNode, chart: ChartType) -> list[Series]:
    return [
        Series(
            _series_name(node, "阶梯"),
            {"x": _arr(node, "XData"), "y": _arr(node, "YData")},
        )
    ]


def _errorbar(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {"x": _arr(node, "XData"), "y": _arr(node, "YData")}
    for key, names in (
        ("y_negative", ("YNegativeDelta",)),
        ("y_positive", ("YPositiveDelta",)),
        ("x_negative", ("XNegativeDelta",)),
        ("x_positive", ("XPositiveDelta",)),
    ):
        value = _arr(node, *names)
        if value is not None:
            fields[key] = value
    return [Series(_series_name(node, "误差棒"), fields)]


def _area(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {"x": _arr(node, "XData"), "y": _arr(node, "YData")}
    base = numbers(node.get("BaseValue"))
    if _count(base):
        fields["base"] = base
    return [Series(_series_name(node, "面积"), fields)]


def _scatter(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {"x": _arr(node, "XData"), "y": _arr(node, "YData")}
    if node.has("ZData"):
        fields["z"] = _arr(node, "ZData")
    size = _arr(node, "SizeData")
    if size is not None:
        fields["size"] = size
    color = _arr(node, "CData", "ColorData")
    if color is not None:
        fields["color"] = color
    return [Series(_series_name(node, "散点"), fields)]


def _bubble(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {
        "x": _arr(node, "XData"),
        "y": _arr(node, "YData"),
        "size": _arr(node, "SizeData"),
    }
    if node.has("ZData"):
        fields["z"] = _arr(node, "ZData")
    color = _arr(node, "ColorData")
    if color is not None:
        fields["color"] = color
    return [Series(_series_name(node, "气泡"), fields)]


def _bar(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {
        "x": _arr(node, "XEndPoints", "XData"),
        "y": _arr(node, "YEndPoints", "YData"),
    }
    color = _arr(node, "CData")
    if color is not None:
        fields["color"] = color
    base = numbers(node.get("BaseValue"))
    if _count(base):
        fields["base"] = base
    category = node.get("CategoryCount") or node.get("Categories")
    categories = numbers(category)
    if _count(categories):
        fields["categories"] = categories
    return [Series(_series_name(node, "柱"), fields)]


def _stem(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {"x": _arr(node, "XData"), "y": _arr(node, "YData")}
    if node.has("ZData"):
        fields["z"] = _arr(node, "ZData")
    return [Series(_series_name(node, "针"), fields)]


def _pie(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {"values": _arr(node, "XData", "YData")}
    labels = _string_list(node.get("TextLabels"))
    series = Series(_series_name(node, "扇区"), fields)
    series.fields["labels"] = labels or None
    return [series]


def _histogram(node: FigureNode, chart: ChartType) -> list[Series]:
    fields: dict[str, Any] = {}
    data = _arr(node, "Data")
    if data is not None:
        fields["data"] = data
    for key, names in (
        ("bin_edges", ("BinEdges",)),
        ("counts", ("Values", "BinCounts")),
        ("bin_counts", ("BinCounts",)),
    ):
        value = _arr(node, *names)
        if value is not None and key not in fields:
            fields[key] = value
    if "counts" in fields and "bin_counts" in fields:
        fields.pop("bin_counts")
    return [Series(_series_name(node, "直方图"), fields)]


def _heatmap(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {"matrix": _arr(node, "ColorData")}
    x = _arr(node, "XData")
    y = _arr(node, "YData")
    if x is not None:
        fields["x"] = x
    if y is not None:
        fields["y"] = y
    xlabels = _string_list(node.get("XDisplayLabels"))
    ylabels = _string_list(node.get("YDisplayLabels"))
    if xlabels:
        fields["x_labels"] = xlabels
    if ylabels:
        fields["y_labels"] = ylabels
    return [Series(_series_name(node, "热力"), fields)]


def _surface(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {
        "x": _arr(node, "XData"),
        "y": _arr(node, "YData"),
        "z": _arr(node, "ZData"),
    }
    color = _arr(node, "CData")
    if color is not None:
        fields["color"] = color
    return [Series(_series_name(node, "曲面"), {k: v for k, v in fields.items() if v})]


def _contour(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {"z": _arr(node, "ZData"), "x": _arr(node, "XData"), "y": _arr(node, "YData")}
    levels = _arr(node, "LevelList", "Levels")
    if levels is not None:
        fields["levels"] = levels
    return [Series(_series_name(node, "等高线"), {k: v for k, v in fields.items() if v})]


def _image(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {"cdata": _arr(node, "CData")}
    for key, names in (("x", ("XData",)), ("y", ("YData",)), ("alpha", ("AlphaData",))):
        value = _arr(node, *names)
        if value is not None:
            fields[key] = value
    return [Series(_series_name(node, "图像"), fields)]


def _quiver(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {
        "x": _arr(node, "XData"),
        "y": _arr(node, "YData"),
        "u": _arr(node, "UData"),
        "v": _arr(node, "VData"),
    }
    for key, name in (("z", "ZData"), ("w", "WData")):
        value = _arr(node, name)
        if value is not None:
            fields[key] = value
    return [Series(_series_name(node, "矢量"), {k: v for k, v in fields.items() if v})]


def _patch(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {
        "x": _arr(node, "XData"),
        "y": _arr(node, "YData"),
        "z": _arr(node, "ZData"),
        "color": _arr(node, "CData"),
        "faces": _arr(node, "Faces"),
        "vertices": _arr(node, "Vertices"),
    }
    return [Series(_series_name(node, "面片"), {k: v for k, v in fields.items() if v})]


def _boxchart(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {"x": _arr(node, "XData"), "y": _arr(node, "YData")}
    return [Series(_series_name(node, "箱线"), {k: v for k, v in fields.items() if v})]


def _wordcloud(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {
        "words": _string_list(node.get("WordData")),
        "sizes": _arr(node, "SizeData"),
    }
    return [Series(_series_name(node, "词云"), {k: v for k, v in fields.items() if v})]


def _parallel(node: FigureNode, chart: ChartType) -> list[Series]:
    fields = {
        "data": _arr(node, "Data", "CoordinateData"),
        "group": _arr(node, "GroupData"),
        "coordinates": _string_list(node.get("CoordinateDataLabels")),
    }
    return [Series(_series_name(node, "平行坐标"), {k: v for k, v in fields.items() if v})]


_EXTRACTORS = {
    "line": _line,
    "stairs": _stairs,
    "errorbar": _errorbar,
    "area": _area,
    "scatter": _scatter,
    "bubble": _bubble,
    "swarm": _scatter,
    "spy": _scatter,
    "bar": _bar,
    "stem": _stem,
    "pie": _pie,
    "histogram": _histogram,
    "heatmap": _heatmap,
    "surface": _surface,
    "mesh": _surface,
    "contour": _contour,
    "image": _image,
    "quiver": _quiver,
    "patch": _patch,
    "slice": _surface,
    "stream": _surface,
    "boxchart": _boxchart,
    "wordcloud": _wordcloud,
    "parallel": _parallel,
    "geo": _line,
    "polar": _line,
}


def _series_name(node: FigureNode, default: str) -> str:
    for key in ("DisplayName", "Name"):
        value = text(node.get(key))
        if value and value.lower() not in {"data", "none"}:
            return value
    return default


def _string_list(value: Any) -> list[str]:
    """A MATLAB char array, char matrix or cellstr into a list of strings."""
    if value is None:
        return []
    import numpy as np

    raw = value
    while isinstance(raw, np.ndarray) and raw.size == 1:
        raw = raw.reshape(-1)[0]
    if isinstance(raw, np.ndarray):
        if raw.dtype == object:
            return [item for entry in raw.flat for item in _string_list(entry)]
        if raw.dtype.kind not in {"U", "S"}:
            return []
        if raw.ndim <= 1:
            items = [str(entry) for entry in raw.flat]
            if not items:
                return []
            # A char array arrives one character per element; a cellstr arrives
            # as whole words, one element each.
            if all(len(item) <= 1 for item in items):
                joined = "".join(items).strip()
                return [joined] if joined else []
            return [item for item in items if item.strip()]
        return [
            row.strip() for row in ("".join(str(c) for c in line) for line in raw) if row.strip()
        ]
    if isinstance(raw, list):
        return [item for entry in raw for item in _string_list(entry)]
    value_text = text(raw)
    return [value_text] if value_text else []


# --- axes description -----------------------------------------------------------


def _vector(node: FigureNode, name: str) -> list[float] | None:
    value = numbers(node.get(name))
    flat = _flatten(value)
    return flat or None


def _tick_labels(node: FigureNode, name: str) -> list[str]:
    labels = _string_list(node.get(name))
    return [label for label in labels if label]


def _axes_info(axes: FigureNode) -> dict[str, Any]:
    info: dict[str, Any] = {}
    labels = _axis_labels(axes)
    for key in ("title", "x_label", "y_label", "z_label"):
        if labels.get(key):
            info[key] = labels[key]
    if labels.get("annotations"):
        info["labels_from"] = "text-position"
    for key, names in (
        ("x_scale", ("XScale",)),
        ("y_scale", ("YScale",)),
        ("z_scale", ("ZScale",)),
    ):
        value = _flag(axes, names[0])
        if value and value != "linear":
            info[key] = value
    for key, names in (
        ("x_lim", ("XLim",)),
        ("y_lim", ("YLim",)),
        ("z_lim", ("ZLim",)),
        ("theta_lim", ("ThetaLim",)),
        ("r_lim", ("RLim",)),
        ("color_lim", ("CLim",)),
        ("latitude_lim", ("LatitudeLimits",)),
        ("longitude_lim", ("LongitudeLimits",)),
    ):
        value = _vector(axes, names[0])
        if value:
            info[key] = value
    for key, names in (("x_tick", ("XTick",)), ("y_tick", ("YTick",)), ("z_tick", ("ZTick",))):
        value = _vector(axes, names[0])
        if value and len(value) <= 64:
            info[key] = value
    for key, names in (
        ("x_tick_label", ("XTickLabel",)),
        ("y_tick_label", ("YTickLabel",)),
    ):
        value = _tick_labels(axes, names[0])
        if value:
            info[key] = value
    grid = [axis for axis in "xyz" if _flag(axes, f"{axis.upper()}Grid") == "on"]
    if grid:
        info["grid"] = grid
    view = _vector(axes, "View")
    if view:
        info["view"] = view
    colorbar = axes.child_of("colorbar")
    if colorbar:
        info["colorbar"] = {
            "label": text(colorbar[0].get("LabelString", "Label")) or None,
        }
    return info


def _text_children(axes: FigureNode) -> list[FigureNode]:
    return [
        child
        for child in axes.children
        if child.object_type.lower() == "text" or decoration_role(child) == "text"
    ]


def _position(node: FigureNode) -> list[float] | None:
    flat = _flatten(numbers(node.get("Position")))
    return flat if len(flat) >= 2 else None


_NUMERIC = re.compile(r"^[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$")


def _is_label_text(value: str) -> bool:
    """A label is text; a bare number is a handle left by an older save."""
    return bool(value) and not _NUMERIC.match(value)


def _axis_labels(axes: FigureNode) -> dict[str, Any]:
    """Title and axis labels, read from text children by where they sit."""
    found = {"title": "", "x_label": "", "y_label": "", "z_label": "", "annotations": []}
    for key, source in (("title", "Title"), ("x_label", "XLabel"), ("y_label", "YLabel")):
        direct = text(axes.get(source))
        if _is_label_text(direct):
            found[key] = direct

    candidates: dict[str, list[tuple[float, str]]] = {
        "title": [],
        "x_label": [],
        "y_label": [],
        "z_label": [],
    }
    for child in _text_children(axes):
        value = text(child.get("String", "Text"))
        if not _is_label_text(value):
            continue
        position = _position(child)
        rotation = _flatten(numbers(child.get("Rotation")))
        rotation = rotation[0] if rotation else 0.0
        role = "annotation"
        if position is not None:
            x, y = position[0], position[1]
            z = position[2] if len(position) > 2 else 1.0
            if y >= 0.95:
                role = "title"
                weight = abs(y - 1.0)
            elif y <= 0.05:
                role = "x_label"
                weight = abs(y) + abs(x - 0.5)
            elif x <= 0.05:
                role = "y_label"
                weight = abs(x) + abs(y - 0.5)
            elif abs(rotation - 90) < 1 and z > 0.9 and 0.3 < y < 0.7:
                role = "z_label"
                weight = abs(y - 0.5)
            else:
                weight = 0.0
        else:
            weight = 0.0
        if role == "annotation":
            found["annotations"].append({"text": value, "position": position})
        else:
            candidates[role].append((weight, value))
    for role, items in candidates.items():
        if items and not found[role]:
            items.sort(key=lambda item: item[0])
            found[role] = items[0][1]
            for _, extra in items[1:]:
                found["annotations"].append({"text": extra, "position": None})
    return found


def _legend(axes: FigureNode) -> list[str]:
    for child in axes.children:
        if decoration_role(child) != "legend":
            continue
        entries = _string_list(child.get("String"))
        if entries:
            return entries
        texts = [
            text(grand.get("String"))
            for grand in child.walk()
            if grand.object_type.lower() == "text"
        ]
        entries = [entry for entry in texts if entry]
        if entries:
            return entries
    return []


def _figure_widgets(node: FigureNode) -> list[dict[str, Any]]:
    widgets = []
    for item in node.walk():
        if item.object_type.lower() not in {"uicontrol", "uipanel", "uibuttongroup", "uitable"}:
            continue
        widgets.append(
            {
                "class": item.object_type,
                "style": text(item.get("Style")) or None,
                "text": text(item.get("String", "Title")) or None,
                "tag": text(item.get("Tag")) or None,
            }
        )
    return widgets


def _collect_axes(node: FigureNode, seen: set[int]) -> list[FigureNode]:
    axes: list[FigureNode] = []
    for child in node.children:
        if id(child) in seen:
            continue
        if is_axes(child):
            seen.add(id(child))
            axes.append(child)
            continue
        axes.extend(_collect_axes(child, seen))
    return axes


def _layout(figure: FigureNode, axes: Sequence[FigureNode]) -> dict[str, Any]:
    """Rows/columns of the subplot grid, from tiledlayout or axes positions."""
    positions = [_position(axes_item) for axes_item in axes]
    positions = [position for position in positions if position]
    lefts = sorted({round(position[0], 2) for position in positions}) if positions else []
    bottoms = (
        sorted({round(position[1], 2) for position in positions}, reverse=True) if positions else []
    )
    layout: dict[str, Any] = {"lefts": lefts, "bottoms": bottoms}
    for item in figure.walk():
        if item.object_type.lower() in {"tiledchartlayout", "tiled"}:
            grid = _flatten(numbers(item.get("GridSize")))
            if len(grid) >= 2 and grid[0] and grid[1]:
                layout.update(rows=int(grid[0]), columns=int(grid[1]), source="tiledlayout")
                return layout
    if len(axes) <= 1:
        layout.update(rows=1, columns=1, source="single")
        return layout
    if not positions:
        layout.update(rows=1, columns=len(axes), source="order")
        return layout
    layout.update(rows=len(bottoms), columns=len(lefts), source="axes-position")
    return layout


def _subplot_cell(axes: FigureNode, layout: dict[str, Any], ordinal: int) -> dict[str, Any]:
    rows = layout.get("rows", 1)
    columns = layout.get("columns", 1)
    lefts = layout.get("lefts") or []
    bottoms = layout.get("bottoms") or []
    cell: dict[str, Any] = {"rows": rows, "columns": columns}
    position = _position(axes)
    if position and lefts and bottoms:
        left, bottom = round(position[0], 2), round(position[1], 2)
        cell["column"] = min(range(len(lefts)), key=lambda i: abs(lefts[i] - left)) + 1
        cell["row"] = min(range(len(bottoms)), key=lambda i: abs(bottoms[i] - bottom)) + 1
        cell["position"] = [round(value, 4) for value in position]
        return cell
    # No usable positions: fall back to the order the axes were saved in.
    cell["row"] = (ordinal - 1) // columns + 1
    cell["column"] = (ordinal - 1) % columns + 1
    return cell


# --- encoding ---------------------------------------------------------------------


def _encode(series: Sequence[Series]) -> tuple[list[dict[str, Any]], dict[str, bytes]]:
    files: dict[str, bytes] = {}
    encoded: list[dict[str, Any]] = []
    for index, item in enumerate(series, 1):
        entry: dict[str, Any] = {"name": item.name, "points": item.points}
        values: dict[str, Any] = {}
        shapes: dict[str, Any] = {}
        ranges: dict[str, Any] = {}
        for field_name, value in item.fields.items():
            if value is None:
                continue
            count = _count(value)
            if not count:
                continue
            shapes[field_name] = _shape(value)
            value_range = _range(value)
            if value_range:
                ranges[field_name] = value_range
            if count <= INLINE_LIMIT:
                values[field_name] = value
                continue
            data_path, data_bytes = _npy(
                f"series/{index:04d}_{_slug(item.name)}_{field_name}.npy", value
            )
            files[data_path] = data_bytes
            values[field_name] = {"data": data_path, "shape": shapes[field_name], "points": count}
        if values:
            entry["values"] = values
        if shapes:
            entry["shapes"] = shapes
        if ranges:
            entry["ranges"] = ranges
        encoded.append(entry)
    return encoded, files


def _shape(value: Any) -> list[int]:
    if isinstance(value, list):
        if value and isinstance(value[0], list):
            inner = _shape(value[0])
            return [len(value)] + inner
        return [len(value)]
    return []


def _slug(name: str) -> str:
    cleaned = "".join(char if char.isalnum() or char in "-_" else "-" for char in name)
    cleaned = "-".join(part for part in cleaned.split("-") if part)
    return (cleaned or "series")[:32]


def _npy(path: str, value: Any) -> tuple[str, bytes]:
    import numpy as np

    filled = _nan_fill(value)
    try:
        array = np.array(filled, dtype=float)
    except ValueError:
        # Ragged lists: keep the numbers as JSON instead.
        import json

        return path.replace(".npy", ".json"), json.dumps(value).encode("utf-8")
    buffer = io.BytesIO()
    np.save(buffer, array, allow_pickle=False)
    return path, buffer.getvalue()


def _nan_fill(value: Any) -> Any:
    if isinstance(value, list):
        return [_nan_fill(item) for item in value]
    if value is None:
        return float("nan")
    return value


# --- assembly ---------------------------------------------------------------------


def parse_figure(path: str | Path) -> tuple[dict[str, Any], dict[str, bytes]]:
    """Parse one FIG file into ``ov.matlab.figure/2`` plus auxiliary data files."""
    source = Path(path)
    try:
        figures, report = load_figure_objects(source)
    except NotImplementedError as exc:
        # MAT v7.3 (HDF5) figures: scipy refuses before anything can be read.
        return _status_payload(source, STATUS_V73, str(exc)), {}
    folder = source.stem
    charts: list[dict[str, Any]] = []
    files: dict[str, bytes] = {}
    figure_entries: list[dict[str, Any]] = []
    widgets: list[dict[str, Any]] = []
    warnings: list[str] = []

    for figure_index, figure in enumerate(figures, 1):
        axes_nodes = _collect_axes(figure, set())
        layout = _layout(figure, axes_nodes)
        widgets.extend(_figure_widgets(figure))
        figure_entries.append(
            {
                "index": figure_index,
                "name": text(figure.get("Name")) or None,
                "number": numbers(figure.get("Number")) or None,
                "axes": len(axes_nodes),
                "layout": {"rows": layout.get("rows"), "columns": layout.get("columns")},
            }
        )
        for axes_index, axes in enumerate(axes_nodes, 1):
            groups: dict[tuple[str, str], list[FigureNode]] = {}
            for child in axes.children:
                chart = classify(child, axes)
                if chart is None:
                    continue
                groups.setdefault((chart.kind, chart.subtype), []).append(child)
            if not groups and axes.children:
                warnings.append(f"{axes_index}: 坐标轴内没有可识别数据对象")
            for (kind, subtype), nodes in groups.items():
                chart_type = classify(nodes[0], axes) or ChartType(kind=kind, subtype=subtype)
                series: list[Series] = []
                extractor = _EXTRACTORS.get(kind)
                for node in nodes:
                    if extractor is None:
                        series.append(Series(_series_name(node, KIND_LABELS.get(kind, kind)), {}))
                        continue
                    series.extend(extractor(node, chart_type))
                encoded, data_files = _encode(series)
                files.update({f"{folder}/{name}": data for name, data in data_files.items()})
                charts.append(
                    {
                        "index": len(charts) + 1,
                        "type": kind,
                        "type_label": KIND_LABELS.get(kind, kind),
                        "subtype": subtype or None,
                        "source_class": chart_type.source_class or nodes[0].object_type,
                        "type_confidence": chart_type.confidence,
                        "figure": figure_index,
                        "axes_index": axes_index,
                        "subplot": _subplot_cell(axes, layout, axes_index),
                        "axes": _axes_info(axes),
                        "legend": _legend(axes),
                        "series": encoded,
                        "annotations": _axis_labels(axes)["annotations"],
                    }
                )

    counts: dict[str, int] = {}
    for chart in charts:
        counts[chart["type"]] = counts.get(chart["type"], 0) + 1
    status = STATUS_PARSED
    if not charts and report.get("handle_tree_empty") and report.get("mcos_containers"):
        status = STATUS_MCOS_ONLY
        warnings.append(
            "该文件由 R2014b 之后的 MATLAB 保存：句柄树 hgS_080000 为空，图形对象以 MCOS 记录"
            "（hgM_070000/080000）存放，当前解析器还读不了，需要 MCOS 解码或 MATLAB CLI"
        )
    payload: dict[str, Any] = {
        "schema": FIGURE_SCHEMA,
        "status": status,
        "figure": source.stem,
        "figures": figure_entries,
        "charts": charts,
        "widgets": widgets,
        "summary": {
            "chart_count": len(charts),
            "chart_types": counts,
            "series_count": sum(len(chart["series"]) for chart in charts),
            "axes_count": sum(entry["axes"] for entry in figure_entries),
            "has_subplots": any(
                (chart.get("subplot") or {}).get("rows", 1)
                * (chart.get("subplot") or {}).get("columns", 1)
                > 1
                for chart in charts
            ),
            "gallery_function_count": gallery_size(),
            "gallery": PLOT_GALLERY_URL,
        },
        "read": {
            **report,
            "mcos_objects": bool(report.get("mcos_containers")),
        },
        "warnings": warnings,
        "boundary": _BOUNDARY,
    }
    return payload, files


def _status_payload(source: Path, status: str, detail: str) -> dict[str, Any]:
    """A FIG file this reader cannot open, reported instead of raising."""
    return {
        "schema": FIGURE_SCHEMA,
        "status": status,
        "figure": source.stem,
        "figures": [],
        "charts": [],
        "widgets": [],
        "summary": {
            "chart_count": 0,
            "chart_types": {},
            "series_count": 0,
            "axes_count": 0,
            "has_subplots": False,
            "gallery_function_count": gallery_size(),
            "gallery": PLOT_GALLERY_URL,
        },
        "read": {"detail": detail},
        "warnings": [f"无法解析：{detail}"],
        "boundary": _BOUNDARY,
    }
