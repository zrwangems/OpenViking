# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0

import csv
import io
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote

import pytest
from markdown_it import MarkdownIt

from openviking.parse.output import LocalParseOutputStore
from openviking.parse.parsers.directory import DirectoryParser
from openviking.parse.parsers.matlab._zip import read_xml_member
from openviking.parse.parsers.matlab.catalog import find_block, find_block_reference
from openviking.parse.parsers.matlab.formats import parse_additional
from openviking.parse.parsers.matlab.library import (
    block_references,
    normalize_block_document,
    read_block_document,
)
from openviking.parse.parsers.matlab.mat import parse_mat, parse_mat_documents
from openviking.parse.parsers.matlab.parser import MatlabParser
from openviking.parse.parsers.matlab.scripts import parse_m_file, parse_mlx
from openviking.parse.parsers.matlab.sldd import parse_sldd
from openviking.parse.parsers.matlab.slx import parse_slx, system_documents
from openviking.parse.parsers.matlab.stateflow import parse_stateflow, render_stateflow
from openviking.parse.parsers.matlab.templates import render_block_template
from openviking.parse.registry import ParserRegistry

SAMPLE = Path(__file__).parents[2] / "matlab_repos" / "DRLHevIps5_4"


def flatten(system):
    yield system
    for child in system.children:
        yield from flatten(child)


def test_slx_nested_systems_ports_parameters_and_branches():
    model = parse_slx(SAMPLE / "DRLHevIps.slx")
    systems = list(flatten(model))
    documents = system_documents(model)

    assert len(systems) == 65
    assert len(documents) == len(systems)
    assert any(system.inputs for system in systems)
    assert any(system.outputs for system in systems)
    assert documents["main.md"].startswith("---\ntype: simulink-model\n")
    assert "xCU/xCU_Output.md" in documents
    assert "xCU/xCU/main.md" in documents
    assert not any(path.endswith("/index.md") or path == "index.md" for path in documents)
    for path, content in documents.items():
        if path != "main.md":
            assert content.startswith("---\ntype: simulink-subsystem\n"), path
        assert [line for line in content.splitlines() if line.startswith("## ")] == [
            "## 逻辑流程图",
            "## 模型说明",
            "## 块参数",
        ]
        assert content.index("## 逻辑流程图") < content.index("## 模型说明")
        assert "## 块知识模板" not in content
        assert "## 连接表" not in content
        assert "```mermaid" in content
    assert any("DRL_single" in path for path in documents)

    battery = parse_slx(SAMPLE / "Bat" / "Bat.slx")
    battery_doc = system_documents(battery)["main.md"]
    assert "BattTemp" in battery_doc
    assert "BattSoc" in battery_doc
    assert "Bidirectional DC-DC" in battery_doc
    assert "Plimit" in battery_doc
    # Every parsed edge remains in Mermaid, including unresolved endpoints.
    mermaid = battery_doc.split("```mermaid", 1)[1].split("```", 1)[0]
    assert sum(" -->|" in line or " ---|" in line for line in mermaid.splitlines()) == len(
        battery.edges
    )
    # Branch elements must become independent destinations, not disappear.
    assert sum(edge.destination == "465#in:1" for edge in battery.edges) == 1
    assert "464#out:1" in {edge.source for edge in battery.edges}


def test_model_pages_stay_compact_and_keep_instance_parameters():
    documents = system_documents(parse_slx(SAMPLE / "DRLHevIps.slx"), language="zh-CN")
    power_path = next(path for path in documents if path.endswith("Mech_to_Elec_Power_Estimate.md"))
    power = documents[power_path]
    assert "Lookup_n-D" in power
    assert "BreakpointsForDimension1" in power
    assert "`Table` = `MotMapEff'`" in power
    assert "逼近 N 维函数" not in power
    assert len(power) < 10_000

    battery = system_documents(parse_slx(SAMPLE / "Bat" / "Bat.slx"))["main.md"]
    assert "Constant" in battery
    assert "Datasheet Battery" in battery


def test_slx_deduplicates_colliding_directory_names():
    model = parse_slx(SAMPLE / "DRLHevIps.slx")
    documents = system_documents(model)
    assert len(documents) == len(set(documents))


def test_stateflow_states_actions_default_transition_and_conditions():
    charts = parse_stateflow(SAMPLE / "DRLHevIps.slx")
    assert [chart.chart_id for chart in charts] == ["824", "988"]

    timer = render_stateflow(charts[1])
    assert len(charts[1].states) == 3
    assert len(charts[1].transitions) == 5
    assert "### StartTimer" in timer
    assert "Out = 0;" in timer
    assert "after(0.1, sec)" in timer
    assert "[*] --> s1" in timer
    assert "s12 --> s2 : after(0.1, sec)" in timer
    assert "INPUT_DATA" in timer
    assert "OUTPUT_DATA" in timer

    supervisory = render_stateflow(charts[0])
    assert len(charts[0].states) == 34
    assert len(charts[0].transitions) == 35
    assert "EngOnReq = EngOnCalc" in supervisory
    assert 'state "HEV" as s10 {' in supervisory


def test_sldd_entries_dimensions_types_and_references():
    content = parse_sldd(SAMPLE / "HevIps.sldd")
    assert "| VCU_Mode | Simulink.Parameter | 1 × 1 | auto | 2.0;" in content
    assert "Condition=VCU_Mode == 3" not in content  # no duplicated nested wrapper
    assert "| DRLEMS | Simulink.VariantExpression | 未声明 | 未声明 | VCU_Mode == 3" in content
    assert "`VehCong.sldd`" in content
    assert "共提取 **4** 个条目" in content

    config = parse_sldd(SAMPLE / "VehCong.sldd")
    assert config.count("SolverName=ode4") == 1  # ConfigSet fields must not be duplicated.


def test_slx_rejects_missing_model_root(tmp_path):
    path = tmp_path / "invalid.slx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("simulink/blockdiagram.xml", "<BlockDiagram />")
    with pytest.raises(ValueError, match="no model root System"):
        parse_slx(path)


def test_zip_xml_member_limit(tmp_path):
    path = tmp_path / "oversized.slx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("simulink/blockdiagram.xml", b"x" * 17)
    with zipfile.ZipFile(path) as archive:
        with pytest.raises(ValueError, match="16-byte XML safety limit"):
            read_xml_member(archive, "simulink/blockdiagram.xml", max_bytes=16)


def test_mat_v73_hdf5_full_array_export(tmp_path):
    h5py = pytest.importorskip("h5py")
    path = tmp_path / "large.mat"
    with h5py.File(path, "w") as handle:
        handle.create_dataset("trajectory", data=[[1.0, 2.0], [3.0, 4.0]])
        handle.create_dataset("nested/speed", data=[5.0, 6.0])
    content, warnings = parse_mat(path)
    assert "MAT v7.3 (HDF5)" in content
    assert "| trajectory | 2 × 2 |" in content
    documents, warnings = parse_mat_documents(path)
    csv_path = next(name for name in documents if "trajectory" in name and name.endswith(".csv"))
    rows = list(csv.reader(io.StringIO(documents[csv_path])))
    assert rows == [
        ["row", "column", "value"],
        ["1", "1", "1"],
        ["1", "2", "2"],
        ["2", "1", "3"],
        ["2", "2", "4"],
    ]
    assert not warnings
    nested = next(name for name in documents if "nested_speed" in name)
    assert documents[nested].splitlines() == ["dim_1,value", "1,5", "2,6"]


def test_mat_sparse_array_is_exported_in_full(tmp_path):
    sparse = pytest.importorskip("scipy.sparse")
    savemat = pytest.importorskip("scipy.io").savemat
    path = tmp_path / "sparse.mat"
    savemat(path, {"matrix": sparse.csc_matrix([[0.0, 1.5], [2.5, 0.0]])})
    documents, warnings = parse_mat_documents(path)
    csv_path = next(name for name in documents if name.endswith(".csv"))
    assert list(csv.reader(io.StringIO(documents[csv_path]))) == [
        ["row", "column", "value"],
        ["1", "1", "0"],
        ["1", "2", "1.5"],
        ["2", "1", "2.5"],
        ["2", "2", "0"],
    ]
    assert not warnings


def test_mlx_preserves_headings_text_and_code():
    content = parse_mlx(SAMPLE / "RunSACEMS.mlx")
    assert "## 版本内容" in content
    assert "仿真结果实验" in content
    assert "```matlab" in content
    assert "rlSimulinkEnv(mdl,agentblk,obsInfo,actInfo)" in content


def test_mat_shapes_struct_fields_and_m_source():
    content, warnings = parse_mat(SAMPLE / "DriveCycle" / "WLTC.mat")
    assert "| WLTC | 1800 × 2 |" in content
    assert not warnings

    documents, warnings = parse_mat_documents(SAMPLE / "DriveCycle" / "WLTC.mat")
    csv_path = next(name for name in documents if name.endswith(".csv"))
    rows = list(csv.reader(io.StringIO(documents[csv_path])))
    assert len(rows) == 3601
    assert rows[0] == ["row", "column", "value"]
    assert rows[-1][:2] == ["1800", "2"]
    assert not warnings

    agent, _ = parse_mat(SAMPLE / "Result" / "DRLEMSagent.mat")
    assert "DRLEMSagent" in agent
    assert "struct fields: _TypeSystem, _Class, _ObjectMetadata" in agent
    assert "DRLEMSagent[1]._ObjectMetadata" in agent

    source = parse_m_file(SAMPLE / "Eng" / "Eng_param_Handle.m")
    assert "type: matlab-code" in source
    assert "```matlab" in source


@pytest.mark.asyncio
async def test_builtin_parser_writes_real_nested_artifact(tmp_path):
    store = LocalParseOutputStore(tmp_path)
    parser = MatlabParser()
    result = await parser.parse(SAMPLE / "DRLHevIps.slx", parse_output_store=store)
    root = Path(result.artifact_ref.root)
    docs = [
        path
        for path in root.rglob("*.md")
        if "type: simulink-model" in path.read_text(encoding="utf-8")
        or "type: simulink-subsystem" in path.read_text(encoding="utf-8")
    ]

    assert result.meta["system_count"] == 65
    assert result.meta["block_count"] > 1000
    assert result.meta["stateflow_chart_count"] == 2
    assert result.meta["stateflow_state_count"] == 37
    assert result.meta["stateflow_transition_count"] == 40
    assert len(docs) == 65
    model_root = root / "DRLHevIps"
    assert (model_root / "main.md").is_file()
    assert (model_root / "xCU" / "xCU_Output.md").is_file()
    assert not (model_root / "xCU" / "xCU_Output").exists()
    timer = model_root / "stateflow" / "chart_988.md"
    assert "after(0.1, sec)" in timer.read_text(encoding="utf-8")
    # Read the persisted artifact back and verify every generated relative link.
    for document in docs:
        content = document.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^)]+\.md)\)", content):
            assert (document.parent / link).resolve().is_file(), (document, link)
    assert (root / ".artifact_manifest.json").is_file()
    assert result.parser_name == "MatlabParser"
    assert not (root / "DRLHevIps" / "DRLHevIps.slx").exists()
    for document in root.rglob("*.md"):
        content = document.read_text(encoding="utf-8")
        if "```mermaid" in content:
            assert "\\n" not in content


@pytest.mark.asyncio
async def test_whole_joint_project_upload_including_p_code(tmp_path):
    store = LocalParseOutputStore(tmp_path)
    result = await DirectoryParser().parse(
        SAMPLE,
        parse_output_store=store,
        strict=True,
        preserve_structure=True,
        language="zh-CN",
    )
    root = Path(result.artifact_ref.root)

    assert result.warnings == []
    system_pages = [
        path
        for path in root.rglob("*.md")
        if "type: simulink-model" in path.read_text(encoding="utf-8")
        or "type: simulink-subsystem" in path.read_text(encoding="utf-8")
    ]
    assert len(system_pages) == 85
    assert not any(
        path.name == "index.md" and "simulink-" in path.read_text(encoding="utf-8")
        for path in system_pages
    )
    power = next(root.rglob("Mech_to_Elec_Power_Estimate.md")).read_text(encoding="utf-8")
    assert "逼近 N 维函数" not in power
    assert "Output absolute value of input" not in power
    assert (root / "DRLHevIps5_4" / "DriveCycle" / "WLTC.mat.md").is_file()
    assert (root / "DRLHevIps5_4" / "RunSACEMS.mlx.md").is_file()
    assert "P_max_kW" in (root / "DRLHevIps5_4" / "Eng" / "Eng_param.mat.md").read_text(
        encoding="utf-8"
    )
    # M source remains a code resource, without a duplicate generated MD page.
    assert (root / "DRLHevIps5_4" / "Eng" / "Eng_param.m").is_file()
    assert not (root / "DRLHevIps5_4" / "Eng" / "Eng_param.m.md").exists()
    assert not (root / "DRLHevIps5_4" / "Eng" / "Eng_param.mat").exists()
    wltc = root / "DRLHevIps5_4" / "DriveCycle"
    csv_path = next((wltc / "data").glob("*.csv"))
    with csv_path.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.reader(stream))
    assert len(rows) == 3601

    # Binary containers and opaque P-code are represented only by parsed artifacts.
    pcode = root / "DRLHevIps5_4" / "VCU_Mode_Change"
    assert not (pcode / "VCU_Mode_Change.p").exists()
    assert "parse_status: opaque" in (pcode / "index.md").read_text(encoding="utf-8")
    sources = [path for path in SAMPLE.rglob("*") if path.is_file()]
    assert len(sources) == 23
    for source in sources:
        if source.suffix.lower() not in {".m"}:
            assert not list(root.rglob(source.name)), source.name


def test_registry_routes_all_matlab_extensions():
    registry = ParserRegistry()
    for suffix in (".slx", ".sldd", ".mlx", ".mat", ".m", ".p"):
        assert isinstance(registry.get_parser_for_file(f"model{suffix}"), MatlabParser)


def test_block_templates_follow_resource_language():
    chinese = render_block_template("Abs", language="zh-CN")[1]
    english = render_block_template("Abs", language="en")[1]
    assert "输出输入信号的绝对值" in chinese
    assert "Abs 模块输出输入信号的绝对值" in chinese
    assert "Output absolute value of input" in english
    assert "Abs 模块输出输入信号的绝对值" not in english


def test_standard_library_and_external_library_matching():
    assert find_block("Logic") == ("simulink/logic-and-bit-operations", "Logical Operator")
    assert find_block("Reference", "autolibdcdc/Bidirectional DC-DC") is None
    assert find_block_reference("Reference", "autolibdcdc/Bidirectional DC-DC") is None
    assert find_block("Display", "simulink/Sinks/Display") == ("simulink/sinks", "Display")
    assert find_block("Inport", "simulink/Sources/Inport") == ("simulink/sources", "In1")
    assert find_block("Gain", "simulink/Commonly Used Blocks/Gain") == (
        "simulink/commonly-used-blocks",
        "Gain",
    )
    assert find_block("MatrixConcatenate", "simulink/Matrix Operations/Matrix Concatenate") == (
        "simulink/matrix-operations",
        "Matrix Concatenate",
    )


def test_real_browser_blocks_are_retained_and_non_block_leaves_are_removed():
    root = Path(__file__).parents[3] / "openviking/parse/parsers/matlab/simulink-block-library"
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    removed = {
        (item["product"], tuple(item["path"]), item["name"])
        for item in manifest["reconciliation"]["excluded_non_block_entries"]
    }
    for product in ("Vision HDL Toolbox", "Wireless HDL Toolbox"):
        assert (root / "en" / product / "Subsystem.md").is_file()
        assert (root / "en" / product / "Subsystem1.md").is_file()
    assert (root / "en/Simulink/Dashboard/Wireless Icons/Network.md").is_file()
    assert len(removed) == 56
    assert (root / "en/libsb2sl/ALG/1VarPoly.md").is_file()
    assert (root / "en/Aerospace Blockset/Equations of Motion/6DOF.md").is_file()
    for product in ("Automated Driving Toolbox", "Computer Vision Toolbox", "DSP System Toolbox"):
        assert not (root / "en" / product / "Info.md").exists()
        assert not (root / "zh" / product / "Info.md").exists()
    assert not (root / "en/Report Generator/Launch Report.md").exists()
    assert not (root / "zh/Simulink/Blocksets & Toolboxes.md").exists()
    for name, documentation_path in {
        "Floating Scope": "../simulink/slref/scopeviewer.html",
        "XY Graph": "../simulink/slref/record.html",
        "Subsystem Reference": "../simulink/slref/subsystem.html",
    }.items():
        reference = next(
            ref for ref in block_references() if ref.product_id == "hdlcoder" and ref.name == name
        )
        assert reference.documentation_path == documentation_path

    scope = (root / "en/Simulink/Sinks/Scope.md").read_text(encoding="utf-8")
    floating = (root / "en/Simulink Extras/Additional Sinks/Floating Bar Plot.md").read_text(
        encoding="utf-8"
    )
    assert "product_id: 'simulink'" in scope
    assert "product_id: 'simulink-extras'" in floating
    assert "## Ports" in scope and "## Parameters" in scope
    assert "## Ports" in floating and "## Parameters" in floating


def test_library_browser_manifest_counts_and_canonical_layout():
    root = Path(__file__).parents[3] / "openviking/parse/parsers/matlab/simulink-block-library"
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["release"] == "R2025b"
    assert manifest["tree_source"] == "scripts/matlab/tree_full.md"
    totals = manifest["totals"]
    assert totals["products"] == 75
    assert totals["products_with_blocks"] == 75
    assert totals["block_occurrences"] == 4736
    assert totals["unique_product_document_paths"] == 3850
    assert totals["full_document_occurrences"] == {"en": 4736, "zh": 4736}
    assert totals["full_documents"] == {"en": 3850, "zh": 3850}
    assert totals["pending_documents"] == {"en": 0, "zh": 0}
    assert totals["tree_only_occurrences"] == 0
    assert manifest["reconciliation"]["tree_directories"] == 741
    assert manifest["reconciliation"]["matched_blocks"] == 4736
    assert manifest["reconciliation"]["tree_only_blocks"] == 0
    assert manifest["reconciliation"]["verified_override_blocks"] == 753
    assert len(manifest["reconciliation"]["excluded_non_block_entries"]) == 56
    assert not (root / "browser").exists()
    assert not (root / "catalog").exists()
    assert not (root / "products").exists()
    assert (root / "README.md").is_file()
    products = {product["id"]: product for product in manifest["products"]}
    assert products["simulink"]["block_occurrences"] == 574
    assert products["stateflow"]["block_occurrences"] == 4
    assert products["simscape"]["block_occurrences"] == 272
    assert products["simscape-root"]["block_occurrences"] == 0
    assert products["simscape-battery"]["block_occurrences"] == 45
    assert products["sps"]["block_occurrences"] == 405
    assert "matlab" not in products
    assert len(list((root / "en/Simulink/Commonly Used Blocks").glob("*.md"))) == 24
    assert (root / "zh/Simulink/Quick Insert/index.md").is_file()
    assert (root / "zh/DDS Blockset/Take DDS Sample.md").is_file()
    assert not (root / "zh/DDS Blockset/Model DDS Applications in Simulink").exists()

    for language in ("en", "zh"):
        browser = root / language
        assert len(list(browser.rglob("*.md"))) == 5553
        root_index = (browser / "index.md").read_text(encoding="utf-8")
        entries = re.findall(r"^- \[(.*?)\]", root_index, re.MULTILINE)
        assert len(entries) == 75
        assert entries[:3] == ["Simulink", "Aerospace Blockset", "Audio Toolbox"]
        assert entries[-3:] == [
            "Vehicle Network Toolbox",
            "Vision HDL Toolbox",
            "Wireless HDL Toolbox",
        ]
        assert "5G Toolbox" not in entries
        for local_entry in (
            "Communications Toolbox HDL Support",
            "DSP System Toolbox HDL Support",
            "Fixed-Point Designer HDL Support",
            "Motor Control Blockset HDL Support",
            "Report Generator",
            "Simulink Extras",
            "Battery",
            "Electrical",
            "Foundation Library",
            "Utilities",
            "libsb2sl",
        ):
            assert (browser / local_entry / "index.md").is_file()
        assert not (browser / "aeroblks").exists()
        assert not (browser / "5g").exists()
        for index in browser.rglob("index.md"):
            text = index.read_text(encoding="utf-8")
            assert len(text.splitlines()) >= 3, index
            assert "- [" in text or "0 blocks" in text or "0 块" in text, index
    assert "# Simulink 库浏览器" in (root / "zh/index.md").read_text()

    unique_documents = set()
    tree_only_occurrences = 0
    for product in products.values():
        for library in product["libraries"]:
            for block in library["blocks"]:
                for language in ("en", "zh"):
                    document = block["documents"][language]
                    resource = root / block["resource_paths"][language]
                    assert resource.is_file()
                    if not block["documentation_path"]:
                        tree_only_occurrences += 1
                        assert document["status"] == "tree_only"
                        assert "documentation_status: tree_only" in resource.read_text(
                            encoding="utf-8"
                        )
                        continue
                    assert document["status"] == "available"
                    path = root / document["path"]
                    assert path.is_file()
                    unique_documents.add(path)
                    assert resource.read_bytes() == path.read_bytes()
    assert tree_only_occurrences == 2 * totals["tree_only_occurrences"]
    assert len(unique_documents) == 2 * totals["unique_product_document_paths"]


def test_block_library_indexes_render_complete_navigation():
    root = (
        Path(__file__).parents[3]
        / "openviking"
        / "parse"
        / "parsers"
        / "matlab"
        / "simulink-block-library"
    )
    parser = MarkdownIt("commonmark")
    indexes = sorted(root.glob("*/**/index.md"))
    assert len(indexes) == 1634

    for index in indexes:
        text = index.read_text(encoding="utf-8")
        tokens = parser.parse(text)
        links = [
            child
            for token in tokens
            if token.type == "inline"
            for child in (token.children or [])
            if child.type == "link_open"
        ]
        expected_children = {
            path.relative_to(index.parent).as_posix() + "/index.md"
            for path in index.parent.iterdir()
            if path.is_dir()
        } | {path.name for path in index.parent.glob("*.md") if path.name != "index.md"}
        actual_children = {
            unquote(link.attrGet("href")) for link in links if link.attrGet("href") != "../index.md"
        }
        assert actual_children == expected_children, index
        assert len(links) == len(expected_children) + (index.parent.name not in {"en", "zh"}), index

        for link in links:
            href = link.attrGet("href")
            assert not re.search(r"\s", href), (index, href)
            assert (index.parent / unquote(href)).is_file(), (index, href)

        if index.parent.name not in {"en", "zh"}:
            assert any(link.attrGet("href") == "../index.md" for link in links), index


def test_toolbox_matching_uses_original_product_and_library_path():
    chart = find_block_reference("Chart", "stateflow/Chart")
    assert chart.product_id == "stateflow"
    assert chart.name == "Chart"
    assert chart.full_document

    resistor = find_block_reference(
        "Resistor", "simscape/Foundation Library/Electrical/Electrical Elements/Resistor"
    )
    assert resistor.product_id == "simscape"
    assert resistor.library_path[-2:] == ("Electrical Elements", "Elements") or (
        "Electrical Elements" in resistor.library_path
    )
    assert "Linear resistor" in resistor.summary
    assert resistor.full_document

    spectrum = find_block_reference("Spectrum Analyzer", "dsp/Sinks/Spectrum Analyzer")
    assert spectrum.product_id == "dsp"
    assert find_block("Chart", "stateflow/Chart") == ("stateflow", "Chart")
    chart_page = render_block_template("Chart", "stateflow/Chart", language="zh-CN")[1]
    assert "用有限状态机实现控制逻辑" in chart_page
    assert "完整中英文正文尚未抓取" not in chart_page
    pending = render_block_template(
        "Resistor",
        "simscape/Foundation Library/Electrical/Electrical Elements/Resistor",
        language="zh-CN",
    )[1]
    assert "完整中英文正文尚未抓取" not in pending
    assert "Official product:" not in pending


def test_scraped_block_knowledge_is_local_and_complete():
    root = (
        Path(__file__).parents[3]
        / "openviking"
        / "parse"
        / "parsers"
        / "matlab"
        / "simulink-block-library"
    )
    assert not (
        Path(__file__).parents[3]
        / "openviking"
        / "parse"
        / "parsers"
        / "matlab"
        / "block_templates.json"
    ).exists()
    english = root / "en"
    chinese = root / "zh"
    documents = [path for path in english.rglob("*.md") if path.name != "index.md"]
    chinese_documents = [path for path in chinese.rglob("*.md") if path.name != "index.md"]
    assert len(documents) == len(chinese_documents) == 4736
    assert len(list(english.glob("*/index.md"))) == 75
    for page in documents:
        relative = page.relative_to(english)
        chinese_page = chinese / relative
        assert chinese_page.is_file(), relative
        text = page.read_text(encoding="utf-8")
        chinese_text = chinese_page.read_text(encoding="utf-8")
        assert re.search(r"documentation_release: R20\d\d[ab]", text)
        assert "language: en" in text
        assert "## 中文" not in text
        assert "language: zh-CN" in chinese_text
        assert re.search(r"[\u4e00-\u9fff]", chinese_text)
    logical = (english / "Simulink/Logic and Bit Operations/Logical Operator.md").read_text(
        encoding="utf-8"
    )
    assert "Perform specified logical operation on input" in logical
    assert "## Ports" in logical
    assert "## Parameters" in logical
    assert "**Operator**" in logical
    assert "## Block Characteristics" in logical

    # Alternative configurations point to the real Sum documentation, not a guessed page.
    total = (english / "Simulink/Math Operations/Add.md").read_text(encoding="utf-8")
    assert "documentation_page: 'sum'" in total
    assert "Add, Subtract, Sum of Elements" in total
    assert "Add or subtract inputs" in total

    dashboard = english / "Simulink/Dashboard/Knob.md"
    strings = english / "Simulink/String/String Constant.md"
    additional = english / (
        "Simulink/Additional Math & Discrete/Additional Math: Increment - Decrement/"
        "Increment Real World.md"
    )
    assert dashboard.is_file()
    assert strings.is_file()
    assert additional.is_file()
    assert "# Continuous" in (english / "Simulink/Continuous/index.md").read_text(encoding="utf-8")
    assert "documentation_release: R2025b" in logical
    assert not (root / "datetime").exists()
    assert "# Messages & Events" in (english / "Simulink/Messages & Events/index.md").read_text(
        encoding="utf-8"
    )


def test_resource_add_structures_block_pages_without_rewriting_source_files():
    expected = {
        "en": [
            "## Ports",
            "## Parameters",
            "## Libraries",
            "## Block Characteristics",
            "## Extended Capabilities",
            "## Version History",
            "## Description",
        ],
        "zh-CN": [
            "## 端口",
            "## 参数",
            "## 所属库",
            "## 模块特性",
            "## 扩展功能",
            "## 版本历史",
            "## 描述",
        ],
    }
    for language, headings in expected.items():
        document = read_block_document("simulink/math-operations", "Abs", language=language)
        assert [line for line in document.splitlines() if line.startswith("## ")] == headings
        assert document.index(headings[0]) < document.index(headings[-1])
        expected_summary = (
            "输出输入信号的绝对值" if language == "zh-CN" else "Output absolute value of input"
        )
        assert expected_summary in document

    # Aliases in older source documents are normalized only in the add-resource output.
    document = read_block_document("simulink/messages-events", "Receive", language="zh-CN")
    assert "## 描述" in document
    assert "## 说明" not in document


def test_block_document_normalization_preserves_body_and_is_idempotent():
    document = """---
type: simulink-block
---
# Example
Summary.

## 说明
Details.

## 库
Simulink / Examples

## 端口
Input and output.
"""
    normalized = normalize_block_document(document, language="zh-CN")
    assert normalized.index("## 端口") < normalized.index("## 所属库")
    assert normalized.index("## 所属库") < normalized.index("## 描述")
    assert normalized.endswith("Summary.\n\nDetails.\n")
    assert normalize_block_document(normalized, language="zh-CN") == normalized


def test_real_simscape_model_preserves_conserving_network_semantics():
    path = (
        Path(__file__).parents[2]
        / "matlab_repos"
        / "SimscapeBattery"
        / "detailedThermalModel_demo.slx"
    )
    model = parse_slx(path)
    assert len(model.edges) == 8
    assert all(edge.kind == "physical-conserving" for edge in model.edges)
    document = system_documents(model)["main.md"]
    assert "---|未命名守恒连接 · rconn:1 ↔ lconn:1|" in document
    assert "守恒连接（双向）" in document
    assert not any("conn:" in line and "-->" in line for line in document.splitlines())
    assert "## 块参数" in document
    assert "SimscapeComponentBlock" in document


def _write_semantic_slx(path: Path):
    def block(kind, name, sid, properties="", system=""):
        return (
            f'<Block BlockType="{kind}" Name="{name}" SID="{sid}">{properties}'
            + (f'<System Ref="{system}"/>' if system else "")
            + "</Block>"
        )

    root = """<System>
      <Block BlockType="SubSystem" Name="Enabled" SID="1"><System Ref="system_1"/></Block>
      <Block BlockType="SubSystem" Name="Variants" SID="2"><P Name="Variant">on</P><P Name="VariantControlMode">expression</P><System Ref="system_2"/></Block>
      <Block BlockType="ConnectionPort" Name="Electrical +" SID="3"><P Name="Port">1</P><P Name="Side">Left</P><P Name="Domain">electrical</P></Block>
      <Block BlockType="ConnectionPort" Name="Electrical -" SID="4"><P Name="Port">2</P><P Name="Side">Right</P><P Name="Domain">electrical</P></Block>
      <Block BlockType="PMIOPort" Name="Torque" SID="5"><P Name="Port">3</P><P Name="Side">Right</P></Block>
      <Line><P Name="Src">3#rconn:1</P><P Name="Dst">4#lconn:1</P></Line>
    </System>"""
    enabled = """<System><Block BlockType="EnablePort" Name="Enable" SID="11"><P Name="StatesWhenEnabling">held</P></Block>
      <Block BlockType="TriggerPort" Name="Trigger" SID="12"><P Name="TriggerType">rising</P></Block></System>"""
    variants = '<System><Block BlockType="SubSystem" Name="High power" SID="21"><P Name="VariantControl">V == 1</P><System Ref="system_3"/></Block></System>'
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "simulink/blockdiagram.xml",
            '<BlockDiagram><Model><System Ref="system_root"/></Model></BlockDiagram>',
        )
        for ref, xml in (("root", root), ("1", enabled), ("2", variants), ("3", "<System/>")):
            archive.writestr(f"simulink/systems/system_{ref}.xml", xml)


def test_subsystem_types_controls_variant_choices_and_physical_ports(tmp_path):
    path = tmp_path / "semantic.slx"
    _write_semantic_slx(path)
    model = parse_slx(path)
    documents = system_documents(model)
    assert model.subsystem_types == ["subsystem"]
    assert model.children[0].subsystem_types == ["enabled", "triggered"]
    assert model.children[1].subsystem_types == ["variant"]
    root = documents["main.md"]
    assert "type: simulink-model" in root
    assert "StatesWhenEnabling" in documents["Enabled.md"]
    assert "VariantControlMode" in documents["Variants/main.md"]
    assert "VariantControl` = `V == 1" in documents["Variants/main.md"]
    assert "| Electrical + | ConnectionPort | 3 |" in root
    assert "Domain` = `electrical" in root
    assert "| Torque | PMIOPort | 5 |" in root
    assert "bidirectional / conserving" in root


def test_additional_formats_text_containers_and_opaque_originals(tmp_path):
    ssc = (
        Path(__file__).parents[2]
        / "matlab_repos"
        / "SimscapeBattery"
        / "batteryCellHeatConvection.ssc"
    )
    content, kind = parse_additional(ssc)
    assert kind == "ssc"
    assert "nodes" in content and "inputs" in content
    assert "不归类为输入输出" in content

    mdl = tmp_path / "legacy.mdl"
    mdl.write_text('Model {\n Block {\n BlockType "Inport"\n Name "u"\n }\n}', encoding="utf-8")
    content, kind = parse_additional(mdl)
    assert kind == "mdl" and "| `Inport` | 1 |" in content

    req = tmp_path / "requirements.slreqx"
    with zipfile.ZipFile(req, "w") as archive:
        archive.writestr(
            "requirements.xml",
            "<requirements><description>Battery shall remain below 45 C</description></requirements>",
        )
    content, _ = parse_additional(req)
    assert "Battery shall remain below 45 C" in content
    assert "requirements.xml" in content

    mex = tmp_path / "solver.mexa64"
    mex.write_bytes(b"\x7fELF-opaque")
    content, kind = parse_additional(mex)
    assert kind == "mexa64" and "不反汇编、不执行" in content

    class_file = tmp_path / "+physics" / "@Battery" / "Battery.m"
    class_file.parent.mkdir(parents=True)
    class_file.write_text(
        "classdef Battery < handle\n%% model\nmethods\nfunction obj = Battery()\nend\nend\nend\n",
        encoding="utf-8",
    )
    class_doc = parse_m_file(class_file)
    assert "matlab_kind: class" in class_doc
    assert "MATLAB package：`physics`" in class_doc
    assert "classdef：`Battery`，继承 `handle`" in class_doc
    assert "类方法目录：`@Battery`" in class_doc

    registry = ParserRegistry()
    for suffix in (
        ".mdl",
        ".ssc",
        ".sscp",
        ".fig",
        ".mlapp",
        ".mlappinstall",
        ".mltbx",
        ".prj",
        ".mlproj",
        ".slreqx",
        ".slmx",
        ".mldatx",
        ".sfx",
        ".fmu",
        ".tlc",
        ".slxp",
        ".mdlp",
        ".slxc",
        ".autosave",
        ".mexa64",
        ".mexw64",
        ".mexmaci64",
        ".mexmaca64",
        ".asv",
    ):
        assert isinstance(registry.get_parser_for_file(f"asset{suffix}"), MatlabParser), suffix
