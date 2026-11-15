# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0

import csv
import io
import json
import zipfile
from pathlib import Path

import pytest

from openviking.parse.output import LocalParseOutputStore
from openviking.parse.parsers.directory import DirectoryParser
from openviking.parse.parsers.matlab._zip import read_xml_member
from openviking.parse.parsers.matlab.catalog import find_block
from openviking.parse.parsers.matlab.formats import parse_additional
from openviking.parse.parsers.matlab.mat import parse_mat, parse_mat_documents
from openviking.parse.parsers.matlab.parser import MatlabParser
from openviking.parse.parsers.matlab.scripts import parse_m_file, parse_mlx
from openviking.parse.parsers.matlab.sldd import parse_sldd
from openviking.parse.parsers.matlab.slx import parse_slx, system_documents
from openviking.parse.parsers.matlab.stateflow import parse_stateflow, render_stateflow
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
    assert all(path == "index.md" or path.endswith("/index.md") for path in documents)
    assert all("## 信号逻辑流程图" in content for content in documents.values())
    assert all("```mermaid" in content for content in documents.values())
    assert any("DRL_single" in path for path in documents)

    battery = parse_slx(SAMPLE / "Bat" / "Bat.slx")
    battery_doc = system_documents(battery)["index.md"]
    assert "BattTemp" in battery_doc
    assert "BattSoc" in battery_doc
    assert "Bidirectional DC-DC" in battery_doc
    assert "Plimit" in battery_doc
    # Branch elements must become independent destinations, not disappear.
    assert sum(edge.destination == "465#in:1" for edge in battery.edges) == 1
    assert "464#out:1" in {edge.source for edge in battery.edges}


def test_resource_add_inlines_block_library_markdown_directly():
    documents = system_documents(parse_slx(SAMPLE / "DRLHevIps.slx"))
    power = next(
        content
        for path, content in documents.items()
        if path.endswith("Mech_to_Elec_Power_Estimate/index.md")
    )
    assert "## 块知识模板" in power
    assert "### n-D Lookup Table" in power
    assert "Approximate n-dimensional function" in power
    assert "#### 端口" in power
    assert "#### 参数说明" in power
    assert "BreakpointsForDimension1" in power
    assert "https://" not in power
    # The instance value is not overwritten by the generic template.
    assert "`Table` = `MotMapEff'`" in power

    battery = system_documents(parse_slx(SAMPLE / "Bat" / "Bat.slx"))["index.md"]
    assert "### Constant" in battery
    assert "### Datasheet Battery" not in battery


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

    opaque, _ = parse_mat(SAMPLE / "Result" / "DRLEMSagent.mat")
    assert "DRLEMSagent" in opaque
    assert "MATLAB opaque 对象" in opaque

    source = parse_m_file(SAMPLE / "Eng" / "Eng_param_Handle.m")
    assert "type: matlab-code" in source
    assert "```matlab" in source


@pytest.mark.asyncio
async def test_builtin_parser_writes_real_nested_artifact(tmp_path):
    store = LocalParseOutputStore(tmp_path)
    parser = MatlabParser()
    result = await parser.parse(SAMPLE / "DRLHevIps.slx", parse_output_store=store)
    root = Path(result.artifact_ref.root)
    docs = list(root.rglob("index.md"))

    assert result.meta["system_count"] == 65
    assert result.meta["block_count"] > 1000
    assert result.meta["stateflow_chart_count"] == 2
    assert result.meta["stateflow_state_count"] == 37
    assert result.meta["stateflow_transition_count"] == 40
    assert len(docs) == 65
    timer = next(root.rglob("Timer/stateflow_988.md"))
    assert "after(0.1, sec)" in timer.read_text(encoding="utf-8")
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
        SAMPLE, parse_output_store=store, strict=True, preserve_structure=True
    )
    root = Path(result.artifact_ref.root)

    assert result.warnings == []
    assert len(list(root.rglob("index.md"))) == 86
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


def test_standard_library_and_external_library_matching():
    assert find_block("Logic") == ("logic-and-bit-operations", "Logical Operator")
    assert find_block("Reference", "autolibdcdc/Bidirectional DC-DC") is None
    assert find_block("Display", "simulink/Sinks/Display") == ("sinks", "Display")
    assert find_block("Inport", "simulink/Sources/Inport") == ("sources", "Inport")
    assert find_block("MatrixConcatenate", "simulink/Matrix Operations/Matrix Concatenate") == (
        "matrix-operations",
        "Matrix Concatenate",
    )


def test_scraped_block_knowledge_is_local_and_complete():
    root = Path(__file__).parents[3] / "openviking" / "simulink-block-library"
    assert not (
        Path(__file__).parents[3]
        / "openviking"
        / "parse"
        / "parsers"
        / "matlab"
        / "block_templates.json"
    ).exists()
    documents = [path for path in root.glob("*/*.md") if path.name != "index.md"]
    assert len(documents) == 341
    assert len({path.parent.name for path in documents}) == 20
    assert not any("https://" in path.read_text(encoding="utf-8") for path in documents)
    manifest = json.loads(
        (
            Path(__file__).parents[3] / "scripts" / "matlab" / "simulink-block-manifest.json"
        ).read_text(encoding="utf-8")
    )
    assert len(manifest) == 341
    for entry in manifest:
        family = entry["category"].lower().replace(" & ", "-").replace(" ", "-")
        slug = "".join(
            character if character.isalnum() else "-" for character in entry["name"].lower()
        ).strip("-")
        while "--" in slug:
            slug = slug.replace("--", "-")
        page = root / family / f"{slug}.md"
        assert page.is_file(), entry
        text = page.read_text(encoding="utf-8")
        assert "documentation_release: R2025b" in text
        assert "## Description" in text or "## Ports" in text or "## Parameters" in text

    logical = (root / "logic-and-bit-operations" / "logical-operator.md").read_text(
        encoding="utf-8"
    )
    assert "Perform specified logical operation on input" in logical
    assert "## Ports" in logical
    assert "## Parameters" in logical
    assert "**Operator**" in logical
    assert "## Block Characteristics" in logical

    # Alternative configurations point to the real Sum documentation, not a guessed page.
    total = (root / "math-operations" / "sum.md").read_text(encoding="utf-8")
    assert "documentation_page: 'sum'" in total
    assert "Add, Subtract, Sum of Elements" in total
    assert "Add or subtract inputs" in total

    dashboard = root / "dashboard" / "knob.md"
    strings = root / "string" / "string-constant.md"
    additional = root / "additional-math-and-discrete" / "increment-real-world.md"
    assert dashboard.is_file()
    assert strings.is_file()
    assert additional.is_file()
    assert "# Continuous" in (root / "continuous" / "index.md").read_text(encoding="utf-8")
    assert "documentation_release: R2025b" in logical
    assert not (root / "datetime").exists()
    assert "# Messages & Events" in (root / "messages-events" / "index.md").read_text(
        encoding="utf-8"
    )


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
    document = system_documents(model)["index.md"]
    assert "守恒网络连接（无输入输出方向）" in document
    assert "rconn:1 ↔ lconn:1" in document
    assert not any("conn:" in line and "-->" in line for line in document.splitlines())
    assert "## 模型引用与外部依赖" in document
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
    root = documents["index.md"]
    assert "## 全模型子系统类型索引" in root
    assert "StatesWhenEnabling" in documents["Enabled/index.md"]
    assert "VariantControlMode" in documents["Variants/index.md"]
    assert "VariantControl=`V == 1`" in documents["Variants/index.md"]
    assert "| Electrical + | conserving | Left | electrical | 3 |" in root
    assert "| Torque | conserving | Right | 未声明 | 5 |" in root
    assert "守恒网络连接（无输入输出方向）" in root


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
