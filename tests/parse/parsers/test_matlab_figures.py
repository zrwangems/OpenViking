# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""FIG parsing: chart type, series data, labels and the R2025b plot catalog."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest
from scipy.io import savemat

from openviking.parse.output import LocalParseOutputStore
from openviking.parse.parsers.matlab.figures import (
    KIND_LABELS,
    PLOT_TYPES,
    classify,
    figure_text,
    gallery_size,
    kinds,
    parse_figure,
)
from openviking.parse.parsers.matlab.figures.catalog import FUNCTION_BY_KIND
from openviking.parse.parsers.matlab.figures.extract import _EXTRACTORS, FIGURE_SCHEMA
from openviking.parse.parsers.matlab.figures.nodes import FigureNode
from openviking.parse.parsers.matlab.parser import MatlabParser

# The FIG container stores each object as these five fields; keep the fixtures
# in that shape so the reader is exercised the way a saved figure exercises it.
_NODE = np.dtype([("type", "O"), ("handle", "O"), ("properties", "O"), ("children", "O")])

GALLERY_FIXTURES = Path("tests/matlab_repos/matlab-ingest-fixture")


def _node(object_type: str, properties: dict | None = None, children=()) -> np.ndarray:
    array = np.zeros((1, 1), dtype=_NODE)
    array[0, 0]["type"] = object_type
    array[0, 0]["handle"] = 1.0
    array[0, 0]["properties"] = dict(properties or {})
    kids = np.zeros((1, len(children)), dtype=_NODE)
    for index, child in enumerate(children):
        kids[0, index] = child[0, 0]
    array[0, 0]["children"] = kids
    return array


def _figure(children=(), name="图窗", number=1.0) -> np.ndarray:
    return _node("f", {"Name": name, "Number": number}, children)


def _axes(children=(), position=(0.13, 0.11, 0.775, 0.815), **properties):
    props = {"Position": np.array([list(position)]), **properties}
    return _node("a", props, children)


def _text(value: str, position=(0.5, -0.06, 1.0), rotation=0.0):
    return _node(
        "t",
        {"String": value, "Position": np.array([list(position)]), "Rotation": rotation},
    )


def _cellstr(*items: str) -> np.ndarray:
    """A MATLAB cellstr: one cell per string, not a char matrix."""
    return np.array([np.array([item]) for item in items], dtype=object)


def _write(tmp_path: Path, name: str, figure: np.ndarray) -> Path:
    target = tmp_path / name
    savemat(str(target), {"hgS_070000": figure}, format="5", do_compression=False)
    return target


# --- catalog ------------------------------------------------------------------------


def test_catalog_covers_the_r2025b_gallery():
    """Every gallery function is registered, and every kind has an extractor."""
    assert gallery_size() >= 80
    for function, plot in PLOT_TYPES.items():
        assert plot.kind in KIND_LABELS, function
        assert plot.category, function
        assert plot.docs.startswith("https://www.mathworks.com/help/"), function
    for kind in kinds():
        assert kind in _EXTRACTORS or kind in {"composite", "widget", "unknown"}, kind
    # The gallery groups that the page shows as columns all survived.
    categories = {plot.category for plot in PLOT_TYPES.values()}
    assert {"线图", "散点与气泡图", "数据分布图", "离散数据图", "极坐标图"} <= categories
    assert "scatter" in FUNCTION_BY_KIND and "bar" in FUNCTION_BY_KIND


# --- type detection ------------------------------------------------------------------


def test_line_chart_keeps_values_and_name(tmp_path):
    figure = _figure(
        [
            _axes(
                [
                    _node(
                        "l",
                        {
                            "XData": np.array([[0.0, 1.0, 2.0]]),
                            "YData": np.array([[0.0, 1.0, 8.0]]),
                            "DisplayName": "速度",
                            "LineStyle": "-",
                            "Marker": "none",
                        },
                    )
                ]
            )
        ]
    )
    payload, files = parse_figure(_write(tmp_path, "line.fig", figure))
    assert payload["schema"] == FIGURE_SCHEMA
    assert payload["summary"]["chart_types"] == {"line": 1}
    chart = payload["charts"][0]
    assert chart["type"] == "line"
    assert chart["series"][0]["name"] == "速度"
    assert chart["series"][0]["values"]["x"] == [0.0, 1.0, 2.0]
    assert chart["series"][0]["values"]["y"] == [0.0, 1.0, 8.0]
    assert files == {}


def test_marker_only_line_is_reported_as_scatter_like(tmp_path):
    figure = _figure(
        [
            _axes(
                [
                    _node(
                        "l",
                        {
                            "XData": np.array([[1.0]]),
                            "YData": np.array([[2.0]]),
                            "LineStyle": "none",
                            "Marker": "o",
                        },
                    )
                ]
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "markers.fig", figure))
    assert payload["charts"][0]["type"] == "line"
    assert payload["charts"][0]["subtype"] == "仅标记"


def test_scatter_and_bar_in_tiled_subplots(tmp_path):
    layout = _node(
        "matlab.graphics.layout.TiledChartLayout",
        {"GridSize": np.array([[1.0, 2.0]])},
        [
            _axes(
                [
                    _node(
                        "matlab.graphics.chart.primitive.Scatter",
                        {
                            "XData": np.array([[1.0, 2.0, 3.0]]),
                            "YData": np.array([[4.0, 5.0, 6.0]]),
                            "SizeData": np.array([[10.0, 20.0, 30.0]]),
                        },
                    )
                ],
                position=(0.13, 0.11, 0.33, 0.815),
                Title="散点",
            ),
            _axes(
                [
                    _node(
                        "matlab.graphics.chart.primitive.Bar",
                        {
                            "XEndPoints": np.array([[1.0, 2.0]]),
                            "YEndPoints": np.array([[3.0, 9.0]]),
                            "BarLayout": "grouped",
                        },
                    )
                ],
                position=(0.57, 0.11, 0.33, 0.815),
                Title="柱",
            ),
        ],
    )
    payload, _ = parse_figure(_write(tmp_path, "subplots.fig", _figure([layout])))
    assert payload["summary"]["chart_types"] == {"scatter": 1, "bar": 1}
    assert payload["summary"]["has_subplots"] is True
    first, second = payload["charts"]
    assert first["subplot"]["rows"] == 1 and first["subplot"]["columns"] == 2
    assert first["subplot"]["column"] == 1
    assert second["subplot"]["column"] == 2
    assert first["series"][0]["values"]["size"] == [10.0, 20.0, 30.0]
    assert second["series"][0]["values"]["y"] == [3.0, 9.0]


def test_horizontal_stacked_bar_subtype(tmp_path):
    figure = _figure(
        [
            _axes(
                [
                    _node(
                        "matlab.graphics.chart.primitive.Bar",
                        {
                            "YData": np.array([[1.0, 2.0]]),
                            "BarLayout": "stacked",
                            "Horizontal": "on",
                        },
                    )
                ]
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "barh.fig", figure))
    assert payload["charts"][0]["type"] == "bar"
    assert "水平" in payload["charts"][0]["subtype"]
    assert "堆叠" in payload["charts"][0]["subtype"]


def test_surface_without_face_color_is_a_mesh(tmp_path):
    mesh = _figure(
        [
            _axes(
                [
                    _node(
                        "matlab.graphics.chart.primitive.Surface",
                        {
                            "XData": np.array([[0.0, 1.0]]),
                            "YData": np.array([[0.0, 1.0]]),
                            "ZData": np.array([[1.0, 2.0], [3.0, 4.0]]),
                            "FaceColor": "none",
                        },
                    )
                ]
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "mesh.fig", mesh))
    assert payload["charts"][0]["type"] == "mesh"
    assert payload["charts"][0]["series"][0]["shapes"]["z"] == [2, 2]


def test_polar_and_geographic_axes_keep_their_coordinates(tmp_path):
    polar = _figure(
        [
            _node(
                "matlab.graphics.axis.PolarAxes",
                {"Position": np.array([[0.13, 0.11, 0.775, 0.815]])},
                [
                    _node(
                        "matlab.graphics.chart.primitive.Line",
                        {"ThetaData": np.array([[0.0, 1.5]]), "RData": np.array([[1.0, 2.0]])},
                    )
                ],
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "polar.fig", polar))
    chart = payload["charts"][0]
    assert chart["type"] == "polar"
    assert chart["series"][0]["values"]["theta"] == [0.0, 1.5]

    geo = _figure(
        [
            _node(
                "matlab.graphics.axis.GeographicAxes",
                {},
                [
                    _node(
                        "matlab.graphics.chart.primitive.Line",
                        {
                            "LatitudeData": np.array([[39.9, 31.2]]),
                            "LongitudeData": np.array([[116.4, 121.5]]),
                        },
                    )
                ],
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "geo.fig", geo))
    assert payload["charts"][0]["type"] == "geo"
    assert payload["charts"][0]["series"][0]["values"]["latitude"] == [39.9, 31.2]


# --- labels, axes and annotations ----------------------------------------------------


def test_titles_labels_legend_and_annotations(tmp_path):
    figure = _figure(
        [
            _axes(
                [
                    _node("l", {"XData": np.array([[0.0, 1.0]]), "YData": np.array([[0.0, 1.0]])}),
                    _node("matlab.graphics.illustration.Legend", {"String": _cellstr("甲", "乙")}),
                    _text("转速曲线", position=(0.5, 1.01)),
                    _text("时间 (s)", position=(0.5, -0.06)),
                    _text("转速 (rpm)", position=(-0.06, 0.5), rotation=90.0),
                    _text("峰值 3200", position=(0.7, 0.8)),
                ],
                XScale="log",
                XLim=np.array([[0.0, 10.0]]),
                XGrid="on",
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "labels.fig", figure))
    chart = payload["charts"][0]
    assert chart["axes"]["title"] == "转速曲线"
    assert chart["axes"]["x_label"] == "时间 (s)"
    assert chart["axes"]["y_label"] == "转速 (rpm)"
    assert chart["axes"]["x_scale"] == "log"
    assert chart["axes"]["x_lim"] == [0.0, 10.0]
    assert chart["axes"]["grid"] == ["x"]
    assert chart["legend"] == ["甲", "乙"]
    assert [item["text"] for item in chart["annotations"]] == ["峰值 3200"]


# --- kinds that carry their data in other properties ---------------------------------


def test_histogram_heatmap_pie_and_quiver(tmp_path):
    figure = _figure(
        [
            _axes(
                [
                    _node(
                        "matlab.graphics.chart.primitive.Histogram",
                        {
                            "Data": np.array([[1.0, 2.0, 2.0, 3.0]]),
                            "BinEdges": np.array([[0.5, 1.5, 2.5, 3.5]]),
                            "Values": np.array([[1.0, 2.0, 1.0]]),
                        },
                    ),
                    _node(
                        "matlab.graphics.chart.primitive.Heatmap",
                        {
                            "ColorData": np.array([[1.0, 2.0], [3.0, 4.0]]),
                            "XDisplayLabels": _cellstr("a", "b"),
                            "YDisplayLabels": _cellstr("c", "d"),
                        },
                    ),
                    _node(
                        "matlab.graphics.chart.primitive.Pie",
                        {
                            "XData": np.array([[30.0, 70.0]]),
                            "TextLabels": _cellstr("甲", "乙"),
                        },
                    ),
                    _node(
                        "matlab.graphics.chart.primitive.Quiver",
                        {
                            "XData": np.array([[0.0, 1.0]]),
                            "YData": np.array([[0.0, 1.0]]),
                            "UData": np.array([[1.0, 0.0]]),
                            "VData": np.array([[0.0, 1.0]]),
                        },
                    ),
                ]
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "kinds.fig", figure))
    types = [chart["type"] for chart in payload["charts"]]
    assert types == ["histogram", "heatmap", "pie", "quiver"]
    histogram, heatmap, pie, quiver = payload["charts"]
    assert histogram["series"][0]["values"]["bin_edges"] == [0.5, 1.5, 2.5, 3.5]
    assert histogram["series"][0]["values"]["counts"] == [1.0, 2.0, 1.0]
    assert heatmap["series"][0]["values"]["matrix"] == [[1.0, 2.0], [3.0, 4.0]]
    assert heatmap["series"][0]["values"]["x_labels"] == ["a", "b"]
    assert pie["series"][0]["values"]["values"] == [30.0, 70.0]
    assert pie["series"][0]["values"]["labels"] == ["甲", "乙"]
    assert quiver["series"][0]["values"]["u"] == [1.0, 0.0]


def test_large_series_is_written_as_npy(tmp_path):
    count = 2000
    figure = _figure(
        [
            _axes(
                [
                    _node(
                        "matlab.graphics.chart.primitive.Line",
                        {
                            "XData": np.linspace(0, 1, count).reshape(1, -1),
                            "YData": np.linspace(0, 2, count).reshape(1, -1),
                        },
                    )
                ]
            )
        ]
    )
    payload, files = parse_figure(_write(tmp_path, "long.fig", figure))
    series = payload["charts"][0]["series"][0]
    assert series["points"] == count
    assert len(files) == 2
    data_ref = series["values"]["y"]
    assert data_ref["shape"] == [count]
    assert data_ref["points"] == count
    written = [name for name in files if name.endswith("_y.npy")]
    assert written and written[0] == f"long/{data_ref['data']}"
    loaded = np.load(__import__("io").BytesIO(files[written[0]]))
    assert loaded.shape == (count,)
    assert loaded[-1] == pytest.approx(2.0)


# --- real fixtures and the text view -------------------------------------------------


def test_gui_figure_lists_its_controls(tmp_path):
    source = (
        GALLERY_FIXTURES
        / "model/StateflowExamples/ModelingACdPlayerradioUsingStateTransitionTableExample/sfcdplayergui_STT.fig"
    )
    payload, _ = parse_figure(source)
    assert payload["charts"] == []
    texts = [widget["text"] for widget in payload["widgets"]]
    assert "PLAY" in texts and "Eject Disc" in texts
    assert any(widget["class"].lower() == "uibuttongroup" for widget in payload["widgets"])
    assert payload["figures"][0]["name"] == "sfcdplayergui_STT"


def test_teapotdemo_fixture_reads_its_axes():
    payload, files = parse_figure(GALLERY_FIXTURES / "data/teapotdemo.fig")
    # The demo draws its surface from a callback, so only the axes are saved.
    assert payload["summary"]["axes_count"] == 1
    assert payload["figures"][0]["name"] == "Untitled"
    assert "uicontrol" in {widget["class"].lower() for widget in payload["widgets"]}
    assert files == {}


def test_text_view_names_type_labels_and_data(tmp_path):
    figure = _figure(
        [
            _axes(
                [
                    _node(
                        "matlab.graphics.chart.primitive.Scatter",
                        {
                            "XData": np.array([[1.0, 2.0]]),
                            "YData": np.array([[3.0, 4.0]]),
                            "DisplayName": "样本",
                        },
                    ),
                    _text("测量点", position=(0.5, 1.01)),
                ],
                XLabel="电压",
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "text.fig", figure))
    page = figure_text(payload)
    assert "散点图" in page
    assert "测量点" in page
    assert "电压" in page
    assert "样本" in page
    assert "2 个点" in page


def test_unknown_primitive_is_kept_visible(tmp_path):
    figure = _figure(
        [
            _axes(
                [
                    _node(
                        "matlab.graphics.chart.primitive.CustomThing",
                        {"XData": np.array([[1.0]])},
                        [_node("l", {"XData": np.array([[1.0]]), "YData": np.array([[1.0]])})],
                    )
                ]
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "custom.fig", figure))
    assert payload["charts"][0]["type"] == "unknown"
    assert payload["charts"][0]["subtype"] == "customthing"


def test_classify_reads_properties_not_only_class_names():
    line = FigureNode(type="l", properties={"LineStyle": ["none"], "Marker": ["o"]})
    assert classify(line).subtype == "仅标记"
    scatter = FigureNode(type="matlab.graphics.chart.primitive.Scatter", properties={})
    assert classify(scatter).kind == "scatter"
    bar = FigureNode(
        type="matlab.graphics.chart.primitive.Bar",
        properties={"Horizontal": ["on"], "BarLayout": ["grouped"]},
    )
    assert classify(bar).subtype == "水平"


# --- the R2025b corpus in tests/matlab_repos/matlab-ingest-fixture/fig --------------


def test_legacy_hg2_class_names_are_read(tmp_path):
    """hgsave on newer releases writes internal names such as graph2d.lineseries."""
    figure = _figure(
        [
            _axes(
                [
                    _node(
                        "graph2d.lineseries",
                        {"XData": np.array([[1.0, 2.0]]), "YData": np.array([[3.0, 4.0]])},
                    )
                ]
            )
        ]
    )
    payload, _ = parse_figure(_write(tmp_path, "legacy.fig", figure))
    assert payload["charts"][0]["type"] == "line"
    assert payload["charts"][0]["series"][0]["values"]["y"] == [3.0, 4.0]


def test_r2025b_figure_yields_its_classes_and_plotted_values():
    """R2025b keeps no handle tree; classes and arrays come from the MCOS payload."""
    payload, files = parse_figure(GALLERY_FIXTURES / "fig/01_line_basic.fig")
    assert payload["status"] == "parsed_mcos"
    assert payload["read"]["handle_tree_empty"] is True
    assert payload["read"]["mcos_objects"] is True
    assert files == {}
    mcos = payload["mcos"]
    assert {"Line", "Figure", "Axes"} <= set(mcos["classes"])
    assert mcos["entries"] > 100
    pair = mcos["series_pairs"][0]
    assert pair["points"] == 200
    assert pair["x_like"] == pytest.approx([0.0, 2 * 3.141592653589793], abs=1e-6)
    assert pair["y_like"] == pytest.approx([-1.0, 1.0], abs=1e-3)
    assert "Line: sin(x)" in mcos["labels"]
    page = figure_text(payload)
    assert "MCOS" in page and "Line" in page


def test_r2025b_container_reads_a_sample_of_the_corpus():
    """The container layer must open every saved variant, not one lucky file."""
    from openviking.parse.parsers.matlab.figures.mcos import read_payload

    sample = [
        "02_line_multi_legend.fig",
        "19_bar_basic.fig",
        "28_histogram.fig",
        "30_pie.fig",
        "33_scatter.fig",
        "43_heatmap.fig",
        "48_surf.fig",
        "65_quiver.fig",
        "75_image_rgb.fig",
        "84_polarplot.fig",
        "88_geoplot.fig",
        "106_subplot_2x2.fig",
        "119_uifigure.fig",
        "137_fig_hgsave_v6.fig",
        "138_fig_saveas.fig",
    ]
    for name in sample:
        payload = read_payload(GALLERY_FIXTURES / "fig" / name)
        assert payload.entries, name
        assert payload.store, name
        assert payload.store_names, name


@pytest.mark.asyncio
async def test_r2025b_figure_keeps_its_bytes_until_properties_are_named(tmp_path):
    """A partial MCOS read still ships figure.json/figure.md and the source bytes."""
    source = GALLERY_FIXTURES / "fig/01_line_basic.fig"
    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "01_line_basic"
    figure = json.loads((root / "figure.json").read_text(encoding="utf-8"))
    assert figure["status"] == "parsed_mcos"
    assert figure["mcos"]["classes"]
    assert (root / "figure.md").is_file()
    assert "MCOS" in (root / "figure.md").read_text(encoding="utf-8")
    assert (root / "01_line_basic.fig").is_file()
    assert result.meta["original_preserved"] is True


def test_mat_v73_figure_is_reported_instead_of_raising():
    payload, files = parse_figure(GALLERY_FIXTURES / "fig/136_fig_hgsave_v73.fig")
    assert payload["status"] == "unsupported_v73"
    assert files == {}
    assert any("v7.3" in warning for warning in payload["warnings"])


def test_hgsave_v6_corpus_file_reads_its_series():
    """One corpus file keeps a handle tree and yields real plotted values."""
    payload, _ = parse_figure(GALLERY_FIXTURES / "fig/137_fig_hgsave_v6.fig")
    assert payload["status"] == "parsed"
    chart = payload["charts"][0]
    assert chart["type"] == "line"
    assert len(chart["series"]) == 30
    assert chart["series"][0]["points"] == 30
    assert chart["axes"]["title"] == "format test"
    assert chart["axes"]["x_lim"] == [0.0, 30.0]


def test_property_names_recovered_from_the_store_stream():
    """Differencing two figures recovers the property names the store records."""
    from openviking.parse.parsers.matlab.figures.mcos import property_names_seen, read_payload

    basic = property_names_seen(read_payload(GALLERY_FIXTURES / "fig/01_line_basic.fig"))
    loglog = property_names_seen(read_payload(GALLERY_FIXTURES / "fig/07_line_loglog.fig"))
    assert len(basic) > 300
    assert "XData_I" in basic or "YData_I" in basic
    # 07 is the same script with log scales: only the log-axis properties are new.
    extra = set(loglog) - set(basic)
    assert {
        "XScale_I",
        "YScale_I",
        "ScaleMode",
        "Scale_I",
        "MinorTickMode",
        "MinorTick_I",
        "XMinorGrid_I",
        "YMinorGrid_I",
    } <= extra


def test_r2025b_series_are_named_arrays_not_guesses():
    """The plotted array sits three slots past its record, its x right before it."""
    from openviking.parse.parsers.matlab.figures.mcos import read_payload, series

    found = series(read_payload(GALLERY_FIXTURES / "fig/01_line_basic.fig"))
    assert len(found) == 1
    item = found[0]
    assert item["property"] == "YData_I"
    assert item["points"] == 200
    assert item["x"][0] == pytest.approx(0.0)
    assert item["x"][-1] == pytest.approx(2 * 3.141592653589793, abs=1e-6)
    assert item["y"][0] == pytest.approx(0.0, abs=1e-3)
    assert max(item["y"]) == pytest.approx(1.0, abs=1e-3)
    assert item["index"] is False


def test_r2025b_series_match_the_handle_tree_of_the_same_figure():
    """137 stores the same figure as an old handle tree and as a MCOS payload."""
    from openviking.parse.parsers.matlab.figures.mcos import read_payload, series

    source = GALLERY_FIXTURES / "fig/137_fig_hgsave_v6.fig"
    payload, _ = parse_figure(source)
    truth = [
        (item["points"], tuple(item["ranges"]["x"]), tuple(item["ranges"]["y"]))
        for chart in payload["charts"]
        for item in chart["series"]
    ]
    assert len(truth) == 30
    found = {
        (item["points"], tuple(item["x_range"]), tuple(item["y_range"]))
        for item in series(read_payload(source))
    }
    for points, x_range, y_range in truth:
        assert (points, x_range, y_range) in found


def test_r2025b_surface_keeps_its_matrix_and_coordinates():
    from openviking.parse.parsers.matlab.figures.mcos import read_payload, series

    found = series(read_payload(GALLERY_FIXTURES / "fig/48_surf.fig"))
    assert len(found) == 1
    item = found[0]
    assert item["property"] == "ZData_I"
    assert item["shape"] == [60, 60]
    assert item["x"][0] == pytest.approx(1.0) and item["x"][-1] == pytest.approx(60.0)
    assert item["y"][0] == pytest.approx(1.0) and item["y"][-1] == pytest.approx(60.0)
    assert item["z_range"][0] == pytest.approx(-6.5142, abs=1e-3)
    assert item["z_range"][1] == pytest.approx(8.0918, abs=1e-3)


def test_r2025b_subplots_give_one_series_each():
    """A 2×2 tiled figure yields four data runs, not one merged blob."""
    from openviking.parse.parsers.matlab.figures.mcos import read_payload, series

    found = series(read_payload(GALLERY_FIXTURES / "fig/106_subplot_2x2.fig"))
    assert len(found) == 4
    assert sorted(item["points"] for item in found) == [6, 14, 20, 100]


def test_r2025b_histogram_keeps_its_bin_edges():
    from openviking.parse.parsers.matlab.figures.mcos import read_payload, series

    (item,) = series(read_payload(GALLERY_FIXTURES / "fig/28_histogram.fig"))
    assert item["points"] == 40
    assert len(item["bin_edges"]) == 41
    assert item["x"] == pytest.approx(item["bin_edges"][:-1])
    assert item["x_range"] == pytest.approx([-3.7, 3.66], abs=1e-2)
    assert item["y_range"][1] == pytest.approx(161.0)


def test_r2025b_texts_are_the_strings_the_figure_shows():
    from openviking.parse.parsers.matlab.figures.mcos import read_payload, texts

    line = texts(read_payload(GALLERY_FIXTURES / "fig/01_line_basic.fig"))
    assert "x" in line and "sin(x)" in line
    tiled = texts(read_payload(GALLERY_FIXTURES / "fig/107_tiledlayout_mixed.fig"))
    assert {"pie", "surf", "bar", "line", "50%"} <= set(tiled)
    gui = texts(read_payload(GALLERY_FIXTURES / "fig/112_gui_controls.fig"))
    assert {"File", "Parameters"} <= set(gui)


def test_property_names_read_the_stream_bounds_from_the_file():
    """The stream moves with the file size; a fixed window only fit one figure."""
    from openviking.parse.parsers.matlab.figures.mcos import (
        property_names_seen,
        read_payload,
        store_bounds,
    )

    small = read_payload(GALLERY_FIXTURES / "fig/43_heatmap.fig")
    start, end = store_bounds(small.store)
    assert end - start < 4552
    assert property_names_seen(small)
    large = read_payload(GALLERY_FIXTURES / "fig/106_subplot_2x2.fig")
    wide = property_names_seen(large)
    assert {"XData_I", "YData_I"} <= set(wide)
