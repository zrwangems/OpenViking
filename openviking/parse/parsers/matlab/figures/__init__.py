# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""FIG (MATLAB figure) reading: chart type, series data, labels and axes.

The public entry point is :func:`parse_figure`, which returns the
``ov.matlab.figure/2`` payload and the auxiliary ``.npy`` files for series too
large to inline.
"""

from __future__ import annotations

from openviking.parse.parsers.matlab.figures.catalog import (
    KIND_LABELS,
    PLOT_GALLERY_URL,
    PLOT_TYPES,
    PlotType,
    functions_for,
    gallery_size,
    kinds,
    plot_type,
)
from openviking.parse.parsers.matlab.figures.classify import ChartType, classify
from openviking.parse.parsers.matlab.figures.extract import FIGURE_SCHEMA, parse_figure
from openviking.parse.parsers.matlab.figures.text import figure_text

__all__ = [
    "FIGURE_SCHEMA",
    "KIND_LABELS",
    "PLOT_GALLERY_URL",
    "PLOT_TYPES",
    "ChartType",
    "PlotType",
    "classify",
    "figure_text",
    "functions_for",
    "gallery_size",
    "kinds",
    "parse_figure",
    "plot_type",
]
