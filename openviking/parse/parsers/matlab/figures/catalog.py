# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""The R2025b plot gallery as a registry of figure kinds.

MathWorks classifies plotting functions into twelve groups on the R2025b
"Types of MATLAB Plots" page. Each function is listed here with the group it
belongs to, the figure kind its saved object belongs to, and the primitive
class the saved figure carries, so a FIG file can be named by the function that
produced it and not only by the object class.
"""

from __future__ import annotations

from dataclasses import dataclass

PLOT_GALLERY_URL = (
    "https://www.mathworks.com/help/releases/R2025b/matlab/creating_plots/"
    "types-of-matlab-plots.html"
)


@dataclass(frozen=True)
class PlotType:
    """One plotting function of the R2025b gallery."""

    function: str
    category: str
    kind: str
    label: str
    object_class: str = ""

    @property
    def docs(self) -> str:
        return f"https://www.mathworks.com/help/releases/R2025b/matlab/ref/{self.function}.html"


LINE = "线图"
SCATTER = "散点与气泡图"
DISTRIBUTION = "数据分布图"
DISCRETE = "离散数据图"
GEOGRAPHIC = "地理图"
POLAR = "极坐标图"
CONTOUR = "等高线图"
VECTOR = "矢量场图"
SURFACE = "曲面与网格图"
VOLUME = "体数据可视化"
ANIMATION = "动画"
IMAGE = "图像"

_CATEGORY_LABELS = {
    LINE: "线图",
    SCATTER: "散点与气泡图",
    DISTRIBUTION: "数据分布图",
    DISCRETE: "离散数据图",
    GEOGRAPHIC: "地理图",
    POLAR: "极坐标图",
    CONTOUR: "等高线图",
    VECTOR: "矢量场图",
    SURFACE: "曲面与网格图",
    VOLUME: "体数据可视化",
    ANIMATION: "动画",
    IMAGE: "图像",
}

# (function, category, kind) taken from the R2025b gallery table, column by column.
_GALLERY: tuple[tuple[str, str, str], ...] = (
    ("plot", LINE, "line"),
    ("plot3", LINE, "line"),
    ("stairs", LINE, "stairs"),
    ("errorbar", LINE, "errorbar"),
    ("area", LINE, "area"),
    ("stackedplot", LINE, "composite"),
    ("loglog", LINE, "line"),
    ("semilogx", LINE, "line"),
    ("semilogy", LINE, "line"),
    ("fplot", LINE, "line"),
    ("fplot3", LINE, "line"),
    ("fimplicit", LINE, "line"),
    ("scatter", SCATTER, "scatter"),
    ("scatter3", SCATTER, "scatter"),
    ("bubblechart", SCATTER, "bubble"),
    ("bubblechart3", SCATTER, "bubble"),
    ("swarmchart", SCATTER, "swarm"),
    ("swarmchart3", SCATTER, "swarm"),
    ("spy", SCATTER, "spy"),
    ("histogram", DISTRIBUTION, "histogram"),
    ("histogram2", DISTRIBUTION, "histogram"),
    ("scatterhistogram", DISTRIBUTION, "composite"),
    ("boxchart", DISTRIBUTION, "boxchart"),
    ("piechart", DISTRIBUTION, "pie"),
    ("donutchart", DISTRIBUTION, "pie"),
    ("wordcloud", DISTRIBUTION, "wordcloud"),
    ("bubblecloud", DISTRIBUTION, "bubble"),
    ("heatmap", DISTRIBUTION, "heatmap"),
    ("parallelplot", DISTRIBUTION, "parallel"),
    ("bar", DISCRETE, "bar"),
    ("barh", DISCRETE, "bar"),
    ("bar3", DISCRETE, "bar"),
    ("bar3h", DISCRETE, "bar"),
    ("pareto", DISCRETE, "bar"),
    ("stem", DISCRETE, "stem"),
    ("stem3", DISCRETE, "stem"),
    ("geoplot", GEOGRAPHIC, "geo"),
    ("geoscatter", GEOGRAPHIC, "geo"),
    ("geobubble", GEOGRAPHIC, "geo"),
    ("polarplot", POLAR, "polar"),
    ("polarhistogram", POLAR, "polar"),
    ("polarscatter", POLAR, "polar"),
    ("polarbubblechart", POLAR, "polar"),
    ("compassplot", POLAR, "polar"),
    ("fpolarplot", POLAR, "polar"),
    ("contour", CONTOUR, "contour"),
    ("contourf", CONTOUR, "contour"),
    ("contour3", CONTOUR, "contour"),
    ("contourslice", CONTOUR, "contour"),
    ("fcontour", CONTOUR, "contour"),
    ("quiver", VECTOR, "quiver"),
    ("quiver3", VECTOR, "quiver"),
    ("feather", VECTOR, "quiver"),
    ("surf", SURFACE, "surface"),
    ("surfc", SURFACE, "surface"),
    ("surfl", SURFACE, "surface"),
    ("ribbon", SURFACE, "surface"),
    ("pcolor", SURFACE, "surface"),
    ("fsurf", SURFACE, "surface"),
    ("fimplicit3", SURFACE, "surface"),
    ("mesh", SURFACE, "mesh"),
    ("meshc", SURFACE, "mesh"),
    ("meshz", SURFACE, "mesh"),
    ("fmesh", SURFACE, "mesh"),
    ("waterfall", SURFACE, "surface"),
    ("streamline", VOLUME, "stream"),
    ("streamslice", VOLUME, "stream"),
    ("streamparticles", VOLUME, "stream"),
    ("streamribbon", VOLUME, "stream"),
    ("streamtube", VOLUME, "stream"),
    ("coneplot", VOLUME, "quiver"),
    ("slice", VOLUME, "slice"),
    ("animatedline", ANIMATION, "line"),
    ("comet", ANIMATION, "line"),
    ("comet3", ANIMATION, "line"),
    ("image", IMAGE, "image"),
    ("imagesc", IMAGE, "image"),
)

# Saved-figure primitives that older FIG files still carry even though the
# gallery lists no R2025b function for them.
_LEGACY_GALLERY: tuple[tuple[str, str, str], ...] = (
    ("pie", DISTRIBUTION, "pie"),
    ("pie3", DISTRIBUTION, "pie"),
    ("rose", POLAR, "polar"),
    ("fill", SURFACE, "patch"),
    ("fill3", SURFACE, "patch"),
    ("patch", SURFACE, "patch"),
    ("scatterhist", DISTRIBUTION, "composite"),
    ("subplot", LINE, "composite"),
    ("tiledlayout", LINE, "composite"),
)

_OBJECT_CLASSES = {
    "plot": "Line",
    "plot3": "Line",
    "stairs": "Stair",
    "errorbar": "ErrorBar",
    "area": "Area",
    "scatter": "Scatter",
    "scatter3": "Scatter",
    "bubblechart": "BubbleChart",
    "bubblechart3": "BubbleChart3",
    "swarmchart": "Scatter",
    "swarmchart3": "Scatter",
    "bar": "Bar",
    "barh": "Bar",
    "bar3": "Bar",
    "bar3h": "Bar",
    "pareto": "Bar",
    "stem": "Stem",
    "stem3": "Stem",
    "histogram": "Histogram",
    "histogram2": "Histogram2",
    "boxchart": "BoxChart",
    "piechart": "Pie",
    "donutchart": "Pie",
    "heatmap": "Heatmap",
    "wordcloud": "WordCloud",
    "bubblecloud": "BubbleCloud",
    "parallelplot": "ParallelCoordinatesPlot",
    "contour": "Contour",
    "contourf": "Contour",
    "contour3": "Contour",
    "fcontour": "FunctionContour",
    "quiver": "Quiver",
    "quiver3": "Quiver",
    "feather": "Quiver",
    "surf": "Surface",
    "surfc": "Surface",
    "surfl": "Surface",
    "ribbon": "Surface",
    "pcolor": "Surface",
    "fsurf": "FunctionSurface",
    "fimplicit3": "FunctionSurface",
    "mesh": "Surface",
    "meshc": "Surface",
    "meshz": "Surface",
    "fmesh": "FunctionSurface",
    "waterfall": "Surface",
    "slice": "Surface",
    "image": "Image",
    "imagesc": "Image",
    "geoplot": "Line",
    "geoscatter": "Scatter",
    "geobubble": "BubbleChart",
    "polarplot": "Line",
    "polarhistogram": "Histogram",
    "polarscatter": "Scatter",
    "polarbubblechart": "BubbleChart",
    "spy": "Line",
    "animatedline": "Line",
    "comet": "Line",
    "comet3": "Line",
    "streamline": "Line",
    "streamslice": "Line",
    "streamtube": "Surface",
    "streamribbon": "Surface",
    "streamparticles": "Line",
    "coneplot": "Quiver",
    "scatterhistogram": "ScatterHistogramChart",
    "stackedplot": "StackedLineChart",
    "plotmatrix": "Axes",
}

PLOT_TYPES: dict[str, PlotType] = {}
for _function, _category, _kind in _GALLERY:
    PLOT_TYPES[_function] = PlotType(
        function=_function,
        category=_category,
        kind=_kind,
        label=_CATEGORY_LABELS[_category],
        object_class=_OBJECT_CLASSES.get(_function, ""),
    )
for _function, _category, _kind in _LEGACY_GALLERY:
    PLOT_TYPES.setdefault(
        _function,
        PlotType(
            function=_function,
            category=_category,
            kind=_kind,
            label=_CATEGORY_LABELS[_category],
            object_class=_OBJECT_CLASSES.get(_function, ""),
        ),
    )

KIND_LABELS = {
    "line": "线图",
    "stairs": "阶梯图",
    "errorbar": "误差棒图",
    "area": "面积图",
    "scatter": "散点图",
    "bubble": "气泡图",
    "swarm": "蜂群图",
    "bar": "柱状图",
    "stem": "针状图",
    "pie": "饼图",
    "histogram": "直方图",
    "boxchart": "箱线图",
    "heatmap": "热力图",
    "wordcloud": "词云",
    "parallel": "平行坐标图",
    "spy": "稀疏矩阵图",
    "contour": "等高线图",
    "surface": "曲面图",
    "mesh": "网格图",
    "image": "图像",
    "quiver": "矢量图",
    "patch": "填充图",
    "slice": "切片图",
    "stream": "流线图",
    "geo": "地理图",
    "polar": "极坐标图",
    "composite": "组合图",
    "widget": "界面控件",
    "unknown": "未识别图形",
}

FUNCTION_BY_KIND: dict[str, list[str]] = {}
for _type in PLOT_TYPES.values():
    FUNCTION_BY_KIND.setdefault(_type.kind, []).append(_type.function)


def kinds() -> list[str]:
    """Every figure kind the registry knows about."""
    return sorted(KIND_LABELS)


def functions_for(kind: str) -> list[str]:
    """The R2025b functions that produce one kind, in gallery order."""
    return list(FUNCTION_BY_KIND.get(kind, []))


def plot_type(function: str) -> PlotType | None:
    return PLOT_TYPES.get(function)


def gallery_size() -> int:
    """Number of distinct R2025b gallery functions covered."""
    return len(PLOT_TYPES)
