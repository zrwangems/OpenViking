# Copyright (c) 2026 Beijing Volcano Engine Corporation.
# SPDX-License-Identifier: AGPL-3.0
"""Render a parsed FIG file as text, so its content can be searched.

The JSON keeps the exact values; this page says in words what the figure shows,
which is what a reader (or a retrieval step) needs: chart types, subplot
positions, titles, axis labels, legend entries and the size and range of each
plotted series.
"""

from __future__ import annotations

from typing import Any

_KIND_WORDS = {
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
    "unknown": "未识别图形",
}


def _fmt_range(value: Any) -> str:
    if not isinstance(value, list) or len(value) != 2:
        return ""
    return f"{_fmt_num(value[0])} 到 {_fmt_num(value[1])}"


def _fmt_num(value: Any) -> str:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, int):
        return str(value)
    if abs(value) >= 1e5 or (value and abs(value) < 1e-3):
        return f"{value:.4g}"
    return f"{round(value, 4):g}"


def _series_line(series: dict[str, Any]) -> str:
    name = series.get("name") or "数据"
    points = series.get("points") or 0
    shapes = series.get("shapes") or {}
    ranges = series.get("ranges") or {}
    shape = next((value for value in shapes.values() if value), None)
    pieces = [f"{name}：{points} 个点"]
    if shape and len(shape) > 1:
        pieces.append("形状 " + "×".join(str(item) for item in shape))
    for field, label in (("x", "x"), ("y", "y"), ("z", "z"), ("r", "r"), ("theta", "θ")):
        if field in ranges:
            pieces.append(f"{label} 范围 {_fmt_range(ranges[field])}")
    if "counts" in ranges:
        pieces.append(f"计数范围 {_fmt_range(ranges['counts'])}")
    if "size" in ranges:
        pieces.append(f"点大小范围 {_fmt_range(ranges['size'])}")
    return "，".join(pieces)


def _axes_line(axes: dict[str, Any]) -> str:
    parts = []
    for key, label in (
        ("title", "标题"),
        ("x_label", "X 轴"),
        ("y_label", "Y 轴"),
        ("z_label", "Z 轴"),
    ):
        if axes.get(key):
            parts.append(f"{label} “{axes[key]}”")
    for key, label in (("x_scale", "X 轴刻度"), ("y_scale", "Y 轴刻度"), ("z_scale", "Z 轴刻度")):
        if axes.get(key):
            parts.append(f"{label} {axes[key]}")
    return "；".join(parts)


def figure_text(payload: dict[str, Any]) -> str:
    """A readable page for one parsed figure."""
    lines: list[str] = []
    figures = payload.get("figures") or []
    charts = payload.get("charts") or []
    summary = payload.get("summary") or {}

    names = "、".join(str(entry.get("name") or "未命名") for entry in figures if entry.get("name"))
    title = payload.get("figure") or "图窗"
    lines.append(f"# 图窗 {title}")
    lines.append("")
    head = [
        f"{len(figures)} 个图窗" if figures else "1 个图窗",
        f"{summary.get('axes_count', 0)} 个坐标轴",
        f"{summary.get('chart_count', 0)} 个图形对象",
    ]
    if names:
        head.append(f"名称：{names}")
    types = summary.get("chart_types") or {}
    if types:
        head.append(
            "类型："
            + "、".join(
                f"{_KIND_WORDS.get(kind, kind)} {count} 个" for kind, count in types.items()
            )
        )
    lines.append("，".join(head) + "。")
    lines.append("")

    for chart in charts:
        kind = chart.get("type", "unknown")
        label = _KIND_WORDS.get(kind, chart.get("type_label") or kind)
        subtype = chart.get("subtype")
        heading = f"## 图 {chart.get('index')}：{label}"
        if subtype:
            heading += f"（{subtype}）"
        lines.append(heading)
        subplot = chart.get("subplot") or {}
        if subplot.get("rows", 1) * subplot.get("columns", 1) > 1:
            lines.append(
                f"- 子图位置：{subplot.get('rows')}×{subplot.get('columns')} 网格，"
                f"第 {subplot.get('row')} 行第 {subplot.get('column')} 列"
            )
        axes_line = _axes_line(chart.get("axes") or {})
        if axes_line:
            lines.append(f"- 坐标轴：{axes_line}")
        legend = chart.get("legend") or []
        if legend:
            lines.append("- 图例：" + "、".join(legend))
        for series in chart.get("series") or []:
            lines.append("- 数据：" + _series_line(series))
        for annotation in chart.get("annotations") or []:
            if annotation.get("text"):
                lines.append(f"- 标注：“{annotation['text']}”")
        lines.append("")

    widgets = payload.get("widgets") or []
    if widgets:
        lines.append("## 界面控件")
        for widget in widgets:
            pieces = [widget.get("class") or "控件"]
            if widget.get("style"):
                pieces.append(str(widget["style"]))
            if widget.get("text"):
                pieces.append(f"“{widget['text']}”")
            if widget.get("tag"):
                pieces.append(f"tag={widget['tag']}")
            lines.append("- " + "，".join(pieces))
        lines.append("")

    mcos = payload.get("mcos") or {}
    if mcos and not mcos.get("error"):
        lines.append("## MCOS 对象载荷（R2014b 之后的保存格式）")
        classes = mcos.get("classes") or []
        if classes:
            lines.append("- 文件里登记的对象类：" + "、".join(classes))
        pairs = mcos.get("series_pairs") or []
        if pairs:
            lines.append(f"- 候选数据序列 {len(pairs)} 组：")
            for pair in pairs[:8]:
                lines.append(
                    f"  · {pair['points']} 点，x {_fmt_range(pair['x_like'])}，"
                    f"y {_fmt_range(pair['y_like'])}（槽 {pair['cells'][0]}、{pair['cells'][1]}）"
                )
        matrices = mcos.get("matrices") or []
        if matrices:
            shapes = "、".join("×".join(str(v) for v in item["shape"]) for item in matrices[:6])
            lines.append(f"- 矩阵数据 {len(matrices)} 个：{shapes}")
        labels = [label for label in (mcos.get("labels") or []) if label][:10]
        if labels:
            lines.append("- 图内文字：" + "、".join(f"“{label}”" for label in labels))
        if not classes and not pairs and not matrices:
            lines.append("- 只解出对象记录，没有找到可用的数值数组。")
        lines.append("")

    if not charts and not widgets and not mcos:
        lines.append("文件里没有可识别的图形对象。")
        lines.append("")

    warnings = payload.get("warnings") or []
    for warning in warnings:
        lines.append(f"- 注意：{warning}")
    return "\n".join(lines).strip() + "\n"
