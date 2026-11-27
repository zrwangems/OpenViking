# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Name the chart a saved graphics object draws.

A FIG file carries no "chart type" field: it stores the graphics primitives
(``Line``, ``Bar``, ``Surface`` …) that a plotting function created, plus their
properties. The type is therefore read from the object class first and refined
from properties and the parent axes, so that a ``scatter`` is reported as a
scatter plot even though the class name only says ``Scatter``, and a
``plot(x,y,'o')`` line is reported as marker-only.
"""

from __future__ import annotations

from dataclasses import dataclass

from openviking.parse.parsers.matlab.figures.catalog import KIND_LABELS
from openviking.parse.parsers.matlab.figures.nodes import FigureNode, text

# Object class (legacy letter already resolved) -> figure kind.
_CLASS_KINDS = {
    "line": "line",
    "stair": "stairs",
    "errorbar": "errorbar",
    "area": "area",
    "scatter": "scatter",
    "bubblechart": "bubble",
    "bubblechart3": "bubble",
    "bubblecloud": "bubble",
    "bar": "bar",
    "stem": "stem",
    "pie": "pie",
    "histogram": "histogram",
    "histogram2": "histogram",
    "heatmap": "heatmap",
    "contour": "contour",
    "functioncontour": "contour",
    "surface": "surface",
    "functionsurface": "surface",
    "image": "image",
    "quiver": "quiver",
    "boxchart": "boxchart",
    "wordcloud": "wordcloud",
    "parallelcoordinatesplot": "parallel",
    "patch": "patch",
    # Internal HG2 class names still written by hgsave on newer releases.
    "graph2d.lineseries": "line",
    "graph2d.stairseries": "stairs",
    "graph2d.errorbarseries": "errorbar",
    "graph2d.areaseries": "area",
    "graph2d.barseries": "bar",
    "graph2d.patch": "patch",
    "graph2d.contourgroup": "contour",
    "graph2d.scatterplot": "scatter",
    "graph3d.surfaceplot": "surface",
    "graph3d.contourgroup": "contour",
    "graph3d.quivergroup": "quiver",
    "graph3d.barseries": "bar",
    "graph3d.scatterplot": "scatter",
    "specgraph.stemseries": "stem",
    "specgraph.stem3series": "stem",
    "specgraph.areaseries": "area",
    "specgraph.barseries": "bar",
    "specgraph.contourgroup": "contour",
    "specgraph.errorbarseries": "errorbar",
    "specgraph.quivergroup": "quiver",
    "specgraph.scattergroup": "scatter",
    "specgraph.surfaceplot": "surface",
    "specgraph.piechart": "pie",
    "specgraph.stairseries": "stairs",
}

# Objects that describe a chart instead of being data.
_DECORATIONS = {
    "legend": "legend",
    "colorbar": "colorbar",
    "text": "text",
    "rectangle": "rectangle",
    "linedecoration": "decoration",
    "axestoolbar": "decoration",
    "interactionaxes": "decoration",
}

_AXES_CLASSES = {"axes", "polaraxes", "geographicaxes", "uiaxes", "mapaxes"}


@dataclass(frozen=True)
class ChartType:
    """What one saved object draws."""

    kind: str
    subtype: str = ""
    confidence: str = "class"
    source_class: str = ""

    @property
    def label(self) -> str:
        base = KIND_LABELS.get(self.kind, self.kind)
        return f"{base}（{self.subtype}）" if self.subtype else base


def is_axes(node: FigureNode) -> bool:
    return node.object_type.lower() in _AXES_CLASSES


def decoration_role(node: FigureNode) -> str | None:
    """``legend``/``colorbar``/``text`` for decorations, None for data objects."""
    return _DECORATIONS.get(node.object_type.lower())


def _axes_parent(node: FigureNode, parent: FigureNode | None) -> str:
    if parent is not None and is_axes(parent):
        return parent.class_name
    return ""


def classify(node: FigureNode, parent: FigureNode | None = None) -> ChartType | None:
    """Chart type of one primitive, or None when it draws no data."""
    name = node.object_type.lower()
    if name in {"figure", "text", "uicontrol", "uipanel", "uibuttongroup", "hggroup"}:
        return None
    if is_axes(node) or name in {"tiled", "tiledchartlayout", "legend", "colorbar"}:
        return None
    if decoration_role(node):
        return None
    kind = _CLASS_KINDS.get(name)
    if kind is None:
        # A saved custom chart still shows its class name; keep it visible.
        if node.children:
            return ChartType(kind="unknown", subtype=name or "object", source_class=name)
        return None
    axes_parent = _axes_parent(node, parent)
    return _refine(kind, node, axes_parent)


def _refine(kind: str, node: FigureNode, axes_parent: str) -> ChartType:
    subtype = ""
    confidence = "class"
    if axes_parent == "PolarAxes" and kind in {"line", "scatter", "bubble", "histogram"}:
        return ChartType(kind="polar", subtype=kind, source_class=node.object_type)
    if axes_parent == "GeographicAxes" and kind in {"line", "scatter", "bubble"}:
        return ChartType(kind="geo", subtype=kind, source_class=node.object_type)
    if kind == "line":
        if node.has("ZData"):
            subtype = "3d"
        line_style = text(node.get("LineStyle"))
        marker = text(node.get("Marker"))
        if line_style in {"none", ""} and marker not in {"", "none", "<none>"}:
            subtype = "仅标记"
    elif kind == "scatter":
        if node.has("ZData"):
            subtype = "3d"
        if axes_parent == "Axes" and node.has("ThetaData"):
            return ChartType(kind="polar", subtype="scatter", source_class=node.object_type)
    elif kind == "bar":
        layout = text(node.get("BarLayout")).lower()
        horizontal = text(node.get("Horizontal")).lower() == "on"
        if layout.startswith("stacked"):
            subtype = "堆叠"
        elif layout.startswith("grouped"):
            subtype = ""
        if horizontal:
            subtype = f"{subtype}水平" if subtype else "水平"
        if node.has("ZData"):
            subtype = f"{subtype}3d" if subtype else "3d"
    elif kind == "surface":
        face = text(node.get("FaceColor")).lower()
        edge = text(node.get("EdgeColor")).lower()
        if face == "none":
            return ChartType(kind="mesh", subtype="", source_class=node.object_type)
        if edge == "none" and face in {"interp", "texturemap"}:
            subtype = "着色"
        if node.has("Faces") or node.has("Vertices"):
            subtype = subtype or "多边形"
    elif kind == "patch":
        if axes_parent:
            subtype = "填充"
    elif kind == "image":
        if node.has("XData") and text(node.get("CDataMapping")).lower() == "scaled":
            subtype = "imagesc"
    elif kind == "histogram" and node.object_type.lower() == "histogram2":
        subtype = "二维"
    elif kind == "pie":
        if node.has("ZData"):
            subtype = "3d"
    elif kind == "stem":
        if node.has("ZData"):
            subtype = "3d"
    elif kind == "contour":
        if node.has("ZLocation"):
            subtype = "3d"
    return ChartType(
        kind=kind, subtype=subtype, confidence=confidence, source_class=node.object_type
    )
