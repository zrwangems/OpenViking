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
from openviking.parse.parsers.matlab.coverage import render_coverage
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
from openviking.parse.parsers.matlab.slx import parse_slx, system_json_documents
from openviking.parse.parsers.matlab.stateflow import parse_stateflow, render_stateflow
from openviking.parse.parsers.matlab.structure import (
    structure_block_document,
    structured_data,
    validate_structured_document,
    without_structured_data,
)
from openviking.parse.parsers.matlab.structured import (
    parse_fig_tree,
    parse_mlapp,
    parse_mldatx,
    parse_mlx_notebook,
    parse_requirement_set,
    parse_sldd_tree,
    protected_metadata,
)
from openviking.parse.parsers.matlab.templates import render_block_template
from openviking.parse.registry import ParserRegistry

SAMPLE = Path(__file__).parents[2] / "matlab_repos" / "matlab-ingest-fixture"
CONTROLLER = (
    SAMPLE
    / "model"
    / "VirtualVehicle"
    / "VirtualVehicle"
    / "Controller"
    / "HevIpsPowertrainController.slx"
)


def flatten(system):
    yield system
    for child in system.children:
        yield from flatten(child)


def test_slx_nested_systems_ports_parameters_and_branches():
    model = parse_slx(CONTROLLER)
    systems = list(flatten(model))
    documents = system_json_documents(model)

    assert len(systems) == 32
    assert len(documents) == len(systems)
    assert any(system.inputs for system in systems)
    assert any(system.outputs for system in systems)
    assert documents["main.json"]["type"] == "simulink-model"
    assert "IPS_Supervisory_Control/main.json" in documents
    assert "Accel_Pedal_to_Traction_Wheel_Torque_Request.json" in documents
    assert not any(path.endswith("/index.json") or path == "index.json" for path in documents)
    for path, document in documents.items():
        assert document["schema"] == "ov.matlab.simulink/1"
        assert document["type"] == ("simulink-model" if path == "main.json" else "simulink-subsystem")
        assert isinstance(document["blocks"], list)
        assert isinstance(document["edges"], list)
        assert set(document) >= {"system", "system_ref", "subsystem_types", "children"}
        assert "```mermaid" not in json.dumps(document)
    total_edges = sum(len(document["edges"]) for document in documents.values())
    assert total_edges == sum(len(system.edges) for system in systems)
    assert (
        documents["IPS_Supervisory_Control/Generator_Control.ON.GenControl/main.json"]["type"]
        == "simulink-subsystem"
    )
def test_system_json_stays_compact_and_keeps_instance_parameters():
    documents = system_json_documents(parse_slx(CONTROLLER), language="zh-CN")
    power_path = next(
        path for path in documents if path.endswith("Mech_To_Elec_Power_Estimate.json")
    )
    power = documents[power_path]
    payload = json.dumps(power, ensure_ascii=False)
    assert "Lookup_n-D" in payload
    assert power["blocks"]
    assert any(
        block["params"].get("Table") == "PlntEM2EffTbl" for block in power["blocks"]
    )
    assert "逼近 N 维函数" not in payload
    assert len(payload) < 10_000
def test_block_library_resource_pack_keeps_block_documents_only(tmp_path):
    """The resource carries block pages: no hand-written index, no rule-based L0/L1."""

    from openviking.parse.parsers.matlab.library_pack import build_tree, pack

    library = tmp_path / "library"
    operations = library / "zh" / "Simulink" / "Math Operations"
    operations.mkdir(parents=True)
    (library / "zh" / "index.md").write_text("# Library\n", encoding="utf-8")
    (library / "zh" / "Simulink" / "index.md").write_text("# Simulink\n", encoding="utf-8")
    (operations / "index.md").write_text("# Math Operations\n", encoding="utf-8")
    (operations / "Abs.md").write_text(
        "---\ntype: simulink-block\n---\n\n# Abs\n\n## 描述\n\n输出输入信号的绝对值。\n",
        encoding="utf-8",
    )

    build_tree(library, tmp_path / "stage", "simulink-block-library")
    staged = tmp_path / "stage" / "simulink-block-library"
    assert (staged / "zh" / "Simulink" / "Math Operations" / "Abs.md").is_file()
    assert not list(staged.rglob("index.md"))
    assert not list(staged.rglob(".abstract.md"))
    assert not list(staged.rglob(".overview.md"))

    result = pack(staged, tmp_path / "simulink-block-library.ovpack", "simulink-block-library")
    assert result["root_uri"] == "viking://resources/simulink-block-library"
    assert result["abstracts"] == 0
    assert result["members_validated"] > 0


def test_block_library_language_pack_puts_products_at_the_root(tmp_path):
    """A single-language pack must not nest everything under ``zh/``."""

    from openviking.parse.parsers.matlab.library_pack import build_tree

    library = tmp_path / "library"
    for language in ("zh", "en"):
        product = library / language / "Simulink"
        product.mkdir(parents=True)
        (library / language / "index.md").write_text(
            f"# Library ({language})\n", encoding="utf-8"
        )
        (product / "index.md").write_text("# Simulink\n", encoding="utf-8")
        (product / "Abs.md").write_text(
            "---\ntype: simulink-block\n---\n\n# Abs\n\n## 描述\n\n绝对值。\n",
            encoding="utf-8",
        )

    build_tree(library, tmp_path / "stage", "simulink-block-library-zh", language="zh")
    staged = tmp_path / "stage" / "simulink-block-library-zh"
    assert (staged / "Simulink" / "Abs.md").is_file()
    assert not (staged / "zh").exists()
    assert not (staged / "en").exists()
    assert not list(staged.rglob("index.md"))


def test_slx_deduplicates_colliding_directory_names():
    model = parse_slx(CONTROLLER)
    documents = system_json_documents(model)
    assert len(documents) == len(set(documents))


def test_stateflow_states_actions_default_transition_and_conditions():
    charts = parse_stateflow(CONTROLLER)
    assert [chart.chart_id for chart in charts] == ["798", "962"]

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
    dictionary = (
        SAMPLE
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatMBSEModel"
        / "ModelData"
        / "asbCubeSatArchInterfaceData.sldd"
    )
    tree = parse_sldd_tree(dictionary)
    assert tree["entry_count"] == 6
    assert tree["references"] == ["asbCubeSatModelData.sldd"]
    assert tree["classes"] == {
        "Simulink.Parameter": 3,
        "Simulink.ConfigSet": 2,
        "Simulink.Bus": 1,
    }
    by_name = {entry["name"]: entry for entry in tree["entries"]}
    assert by_name["altitude"]["value"]["class"] == "Simulink.Parameter"
    assert by_name["altitude"]["value"]["Value"] == "4000000.0"
    assert by_name["ACSConfigSet"]["value"]["class"] == "Simulink.ConfigSet"

    content = parse_sldd(dictionary)
    assert "| altitude | Simulink.Parameter | 1 × 1 | auto | 4000000.0 |" in content
    assert "SolverName=FixedStepDiscrete" in content
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
    live_script = SAMPLE / "model" / "asbCubeSatMBSE" / "MissionAnalysis" / "mappingToolboxAnalysis.mlx"
    content = parse_mlx(live_script)
    assert "## Run the Simulation" in content
    assert "CubeSat Mission Analysis with Mapping Toolbox" in content
    assert "```matlab" in content
    assert 'arch.model = "asbCubeSatArchModel"' in content

    notebook, files = parse_mlx_notebook(live_script)
    kinds = [cell["type"] for cell in notebook["cells"]]
    assert "heading" in kinds and "text" in kinds and "code" in kinds
    code = "\n".join(cell["source"] for cell in notebook["cells"] if cell["type"] == "code")
    assert 'arch.model = "asbCubeSatArchModel"' in code
    assert any(output["type"] == "image" for output in notebook["outputs"])
    assert files and all(name.startswith("outputs/") for name in files)
def test_fig_tree_keeps_handle_objects(tmp_path):
    scipy_io = pytest.importorskip("scipy.io")
    scipy_io.savemat(
        tmp_path / "plot.fig",
        {
            "figure": {
                "Type": "figure",
                "Children": [{"Type": "axes", "Title": "speed"}],
            }
        },
    )
    tree = parse_fig_tree(tmp_path / "plot.fig")
    assert tree["schema"] == "ov.matlab.figure/1"
    rendered = json.dumps(tree, ensure_ascii=False)
    assert "figure" in tree["objects"]
    assert "axes" in rendered and "speed" in rendered


def test_mldatx_keeps_all_suites_cases_and_results(tmp_path):
    path = tmp_path / "tests.mldatx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "testSuite.xml",
            '<TestSuite name="battery"><TestCase name="heat"><Result verdict="pass"/></TestCase></TestSuite>',
        )
    tree = parse_mldatx(path)
    names = {item["name"] for item in tree["tests"]}
    assert {"battery", "heat"} <= names
    assert any(item["tag"] == "Result" for item in tree["tests"])
    assert tree["members"][0]["name"] == "testSuite.xml"


def test_requirement_set_extracts_requirements_and_links(tmp_path):
    path = tmp_path / "requirements.slreqx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "requirements.xml",
            '<requirements><requirement id="R1"><description>Battery below 45 C</description>'
            '</requirement><link source="R1" target="block_42"/></requirements>',
        )
    tree = parse_requirement_set(path)
    assert tree["requirements"][0]["id"] == "R1"
    assert "Battery below 45 C" in json.dumps(tree, ensure_ascii=False)
    assert tree["links"][0]["attributes"]["target"] == "block_42"


def test_mlapp_keeps_classdef_and_component_tree(tmp_path):
    scipy_io = pytest.importorskip("scipy.io")
    path = tmp_path / "panel.mlapp"
    document = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>"
        '<w:p><w:pPr><w:pStyle w:val="code"/></w:pPr><w:r><w:t>classdef panel &lt; matlab.apps.AppBase</w:t></w:r></w:p>'
        '<w:p><w:pPr><w:pStyle w:val="text"/></w:pPr><w:r><w:t>Battery panel</w:t></w:r></w:p>'
        "</w:body></w:document>"
    )
    buffer = io.BytesIO()
    scipy_io.savemat(buffer, {"components": {"Type": "uifigure", "Name": "panel"}})
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("matlab/document.xml", document)
        archive.writestr("appdesigner/appModel.mat", buffer.getvalue())
    tree, files = parse_mlapp(path)
    assert "classdef panel" in tree["code"]
    assert tree["components"] is not None
    assert tree["component_status"] == "parsed"
    assert "code.m" in files


def test_protected_metadata_is_verifiable(tmp_path):
    path = tmp_path / "secret.p"
    path.write_bytes(b"\x00pcode-bytes")
    metadata = protected_metadata(path, "pcode")
    assert metadata["parse_status"] == "opaque"
    assert metadata["original_preserved"] is True
    assert len(metadata["sha256"]) == 64


@pytest.mark.asyncio
async def test_parser_keeps_protected_original_and_requirement_json(tmp_path):
    store = LocalParseOutputStore(tmp_path / "artifacts")
    protected = tmp_path / "secret.slxp"
    protected.write_bytes(b"protected-model")
    result = await MatlabParser().parse(protected, parse_output_store=store)
    root = Path(result.artifact_ref.root)
    assert (root / "secret" / "secret.slxp").read_bytes() == b"protected-model"
    metadata = json.loads((root / "secret" / "secret.slxp.json").read_text(encoding="utf-8"))
    assert metadata["original_preserved"] is True

    requirements = tmp_path / "requirements.slreqx"
    with zipfile.ZipFile(requirements, "w") as archive:
        archive.writestr(
            "requirements.xml",
            '<requirements><requirement id="R1"><description>Battery below 45 C</description>'
            "</requirement></requirements>",
        )
    result = await MatlabParser().parse(requirements, parse_output_store=store)
    root = Path(result.artifact_ref.root)
    tree = json.loads((root / "requirements.slreqx.json").read_text(encoding="utf-8"))
    assert tree["requirements"][0]["id"] == "R1"
    assert "Battery below 45 C" in tree["requirements"][0]["text"]


def test_mat_shapes_struct_fields_and_m_source():
    flames = SAMPLE / "data" / "flames.mat"
    content, warnings = parse_mat(flames)
    assert "| X | 100 × 100 | uint8 |" in content
    assert not warnings

    documents, warnings = parse_mat_documents(flames)
    csv_path = next(name for name in documents if name.endswith(".csv"))
    rows = list(csv.reader(io.StringIO(documents[csv_path])))
    assert len(rows) == 10001
    assert rows[0] == ["row", "column", "value"]
    assert rows[-1][:2] == ["100", "100"]
    assert not warnings

    dataset = (
        SAMPLE
        / "model"
        / "VirtualVehicle"
        / "Electrical"
        / "Plant"
        / "Calibrations"
        / "DeepLearningBattery"
        / "TransientBatteryTestDataset.mat"
    )
    agent, _ = parse_mat(dataset)
    assert "struct fields: _TypeSystem, _Class, _ObjectMetadata" in agent
    assert "DLBatteryTestData[1]._ObjectMetadata" in agent

    source = parse_m_file(SAMPLE / "src" / "detectChangeOrbitalElements.m")
    assert "type: matlab-code" in source
    assert "```matlab" in source
@pytest.mark.asyncio
async def test_builtin_parser_writes_real_nested_artifact(tmp_path):
    store = LocalParseOutputStore(tmp_path)
    parser = MatlabParser()
    result = await parser.parse(CONTROLLER, parse_output_store=store)
    root = Path(result.artifact_ref.root)
    docs = [
        path
        for path in root.rglob("*.json")
        if json.loads(path.read_text(encoding="utf-8")).get("schema") == "ov.matlab.simulink/1"
    ]

    assert result.meta["system_count"] == 32
    assert result.meta["block_count"] == 478
    assert result.meta["stateflow_chart_count"] == 2
    assert result.meta["stateflow_state_count"] == 37
    assert result.meta["stateflow_transition_count"] == 40
    assert len(docs) == 32
    model_root = root / "HevIpsPowertrainController"
    assert (model_root / "main.json").is_file()
    assert (model_root / "IPS_Supervisory_Control" / "main.json").is_file()
    assert (model_root / "Accel_Pedal_to_Traction_Wheel_Torque_Request.json").is_file()
    timer = model_root / "stateflow" / "chart_962.json"
    assert "after(0.1, sec)" in timer.read_text(encoding="utf-8")
    # Every child path in a system JSON resolves inside the artifact.
    for document in docs:
        payload = json.loads(document.read_text(encoding="utf-8"))
        for child in payload.get("children", []):
            assert (document.parent / child["path"]).resolve().is_file(), (document, child["path"])
    assert (model_root / "coverage.json").is_file()
    assert (root / ".artifact_manifest.json").is_file()
    assert result.parser_name == "MatlabParser"
    assert not (model_root / "HevIpsPowertrainController.slx").exists()
    assert not list(model_root.rglob("*.md"))
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
    assert result.meta["unsupported_files"] == []
    assert len(result.meta["skipped_files"]) == 73
    system_pages = [
        path
        for path in root.rglob("*.json")
        if json.loads(path.read_text(encoding="utf-8")).get("schema") == "ov.matlab.simulink/1"
    ]
    assert len(system_pages) > 500
    base = root / "matlab-ingest-fixture"
    assert (base / "data" / "flames.mat.md").is_file()
    assert (
        base
        / "model"
        / "asbCubeSatMBSE"
        / "MissionAnalysis"
        / "mappingToolboxAnalysis"
        / "mappingToolboxAnalysis.mlx.json"
    ).is_file()
    assert list(
        (
            base
            / "model"
            / "asbCubeSatMBSE"
            / "MissionAnalysis"
            / "mappingToolboxAnalysis"
            / "outputs"
        ).glob("*.png")
    )
    assert (
        base
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatMBSEModel"
        / "ModelData"
        / "asbCubeSatArchInterfaceData.sldd.json"
    ).is_file()
    assert (base / "src" / "detectChangeOrbitalElements.m").is_file()
    assert not (base / "src" / "detectChangeOrbitalElements.m.md").exists()
    assert list((base / "bin").rglob("*.dll"))
    assert (base / "bin" / "AddOnInstaller" / "metadata.json").is_file()
    assert (base / "bin" / "ingest_firmware.hex").is_file()
    assert (base / "bin" / "visionzynq-target-eventhandler.elf").is_file()
    assert list((base / "model" / "VirtualVehicle" / "PassVeh" / "Plant").glob("*.STL"))
    assert (base / "build").exists() is False  # generated files are skipped, not imported
    assert (base / "slprj").exists() is False
    assert (base / "packages" / "IngestFixtureSupport" / "manifest.json").is_file()
    assert (base / "packages" / "asbCubeSatMBSEProject" / "manifest.json").is_file()

    # Opaque P-code keeps the original bytes plus verified metadata.
    pcode = base / "src" / "autoblkscheckparams" / "autoblkscheckparams.p"
    assert pcode.is_file()
    metadata = json.loads(
        (pcode.parent / "autoblkscheckparams.p.json").read_text(encoding="utf-8")
    )
    assert metadata["parse_status"] == "opaque"
    assert metadata["sha256"]
    sources = [path for path in SAMPLE.rglob("*") if path.is_file()]
    assert len(sources) == 2718
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


def test_coverage_keeps_wrapped_library_paths_on_one_line():
    model = parse_slx(CONTROLLER)
    coverage = render_coverage(CONTROLLER, model)
    assert "- `simulink/Discontinuities/Saturation Dynamic`：" in coverage
    assert "- `simulink/Logic and Bit Operations/Compare To Constant`：" in coverage
    assert "\nDynamic`：" not in coverage


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
        validate_structured_document(text)
        validate_structured_document(chinese_text)
    logical = (english / "Simulink/Logic and Bit Operations/Logical Operator.md").read_text(
        encoding="utf-8"
    )
    assert "Perform specified logical operation on input" in logical
    assert "## Ports" in logical
    assert "## Parameters" in logical
    assert "**Operator**" in logical
    assert "## Block Characteristics" in logical
    assert structured_data(logical, "ports")
    assert structured_data(logical, "parameters")

    absolute = (english / "Simulink/Math Operations/Abs.md").read_text(encoding="utf-8")
    ports = structured_data(absolute, "ports")
    parameters = structured_data(absolute, "parameters")
    assert [port["direction"] for port in ports[:2]] == ["input", "output"]
    assert ports[0]["name"] == "Port_1"
    assert "double" in ports[0]["data_types"]
    zero_crossing = next(item for item in parameters if item["block_parameter"] == "ZeroCross")
    assert zero_crossing["default"] == "'on'"
    assert zero_crossing["type"] == "character vector | string"

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


def test_block_document_structuring_preserves_body_and_is_idempotent():
    document = """---
type: simulink-block
---
# Example

## 端口

### 输入

### **u** — 输入信号 scalar

信号说明。

**数据类型：** `double` | `single`

## 参数

### 主要参数

### **增益** — 增益值 `1` (default)

参数说明与依赖。

#### 编程使用

|  |  |
| --- | --- |
| **模块参数：** | `Gain` |
| **类型：** | character vector |
| **值：** | `'1'` | `'2'` |
| **默认值：** | `'1'` |

## 描述

完整知识正文。
"""
    structured = structure_block_document(document)
    assert [line for line in without_structured_data(structured).splitlines() if line.strip()] == [
        line for line in document.splitlines() if line.strip()
    ]
    assert structured_data(structured, "ports") == [
        {
            "name": "u",
            "summary": "输入信号 scalar",
            "direction": "input",
            "data_types": "double | single",
        }
    ]
    parameter = structured_data(structured, "parameters")[0]
    assert parameter["group"] == "主要参数"
    assert parameter["block_parameter"] == "Gain"
    assert parameter["values"] == "'1' | '2'"
    assert parameter["default"] == "'1'"
    validate_structured_document(structured)
    assert structure_block_document(structured) == structured


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
    content, kind = parse_additional(
        SAMPLE / "model" / "VirtualVehicle" / "Electrical" / "Plant" / "FuelCell.ssc"
    )
    assert kind == "ssc"
    assert "nodes" in content and "inputs" in content
    assert "不归类为输入输出" in content
    assert "component (Propagation = blocks) FuelCell" in content
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
    documents = system_json_documents(model)
    assert model.subsystem_types == ["subsystem"]
    assert model.children[0].subsystem_types == ["enabled", "triggered"]
    assert model.children[1].subsystem_types == ["variant"]
    root = documents["main.json"]
    assert root["type"] == "simulink-model"
    enabled = documents["Enabled.json"]
    assert any(block["params"].get("StatesWhenEnabling") == "held" for block in enabled["blocks"])
    variants = documents["Variants/main.json"]
    assert variants["type"] == "simulink-subsystem"
    root_blocks = {block["name"]: block for block in root["blocks"]}
    assert root_blocks["Variants"]["params"]["VariantControlMode"] == "expression"
    assert any(
        block["params"].get("VariantControl") == "V == 1" for block in variants["blocks"]
    )
    by_name = {block["name"]: block for block in root["blocks"]}
    assert by_name["Electrical +"]["block_type"] == "ConnectionPort"
    assert by_name["Electrical +"]["params"]["Domain"] == "electrical"
    assert by_name["Electrical +"]["ports"]["conn"] == [1]
    assert by_name["Torque"]["block_type"] == "PMIOPort"
    assert by_name["Torque"]["ports"]["conn"] == [3]
def test_additional_formats_text_containers_and_opaque_originals(tmp_path):
    ssc = (
        SAMPLE
        / "model"
        / "VirtualVehicle"
        / "Electrical"
        / "Plant"
        / "FuelCell.ssc"
    )
    content, kind = parse_additional(ssc)
    assert kind == "ssc"
    assert "nodes" in content and "inputs" in content
    assert "不归类为输入输出" in content

    mdl = SAMPLE / "src" / "slctrlobsolete.mdl"
    content, kind = parse_additional(mdl)
    assert kind == "mdl" and "BlockType 声明" in content

    req = (
        SAMPLE
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatRequirements"
        / "ACSRequirements.slreqx"
    )
    content, _ = parse_additional(req)
    assert "The CubeSat shall have" in content
    assert "slrequirements/data.xml" in content

    mex = SAMPLE / "src" / "componentinfo.mexw64"
    content, kind = parse_additional(mex)
    assert kind == "mexw64" and "不反汇编、不执行" in content

    class_file = (
        SAMPLE
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatMBSEModel"
        / "ModelData"
        / "componentType.m"
    )
    class_doc = parse_m_file(class_file)
    assert "matlab_kind: class" in class_doc
    assert "classdef：`componentType`，继承 `uint8`" in class_doc
