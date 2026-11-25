# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0

import csv
import io
import json
import shutil
import zipfile
from pathlib import Path

import pytest

from openviking.parse.output import LocalParseOutputStore
from openviking.parse.parsers.directory import DirectoryParser
from openviking.parse.parsers.matlab._zip import read_xml_member
from openviking.parse.parsers.matlab.keydes import KeydesLibrary
from openviking.parse.parsers.matlab.mat import parse_mat, parse_mat_documents
from openviking.parse.parsers.matlab.parser import MatlabParser
from openviking.parse.parsers.matlab.slx import Block, parse_slx, system_json_documents
from openviking.parse.parsers.matlab.stateflow import chart_json, parse_stateflow
from openviking.parse.parsers.matlab.structured import (
    parse_fig_tree,
    parse_mlapp,
    parse_mldatx,
    parse_mlx_notebook,
    parse_requirement_set,
    parse_sldd_tree,
    protected_metadata,
    sldd_entry_rows,
)
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
        assert document["type"] == (
            "simulink-model" if path == "main.json" else "simulink-subsystem"
        )
        assert isinstance(document["blocks"], list)
        assert isinstance(document["edges"], list)
        assert set(document) >= {"system", "system_ref", "subsystem_types", "children"}
        assert "```mermaid" not in json.dumps(document)
        for block in document["blocks"]:
            assert set(block) == {
                "name",
                "block_type",
                "source_block",
                "key",
                "description",
                "ports",
            }
        for edge in document["edges"]:
            assert set(edge) == {"from", "to", "signal"}
            assert isinstance(edge["from"], list) and len(edge["from"]) == 2
            assert edge["to"] and all(
                isinstance(target, list) and len(target) == 2 for target in edge["to"]
            )
        for child in document["children"]:
            assert set(child) == {"name", "path", "system_ref", "type"}

    total_rows = sum(len(document["edges"]) for document in documents.values())
    total_edges = sum(len(system.edges) for system in systems)
    assert 0 < total_rows <= total_edges
    assert any(
        len(edge["to"]) > 1
        for document in documents.values()
        for edge in document["edges"]
    )
    assert (
        documents["IPS_Supervisory_Control/Generator_Control.ON.GenControl/main.json"]["type"]
        == "simulink-subsystem"
    )
def test_system_json_carries_a_description_per_block_instead_of_parameters():
    documents = system_json_documents(parse_slx(CONTROLLER), language="zh-CN")
    power_path = next(
        path for path in documents if path.endswith("Mech_To_Elec_Power_Estimate.json")
    )
    power = documents[power_path]
    payload = json.dumps(power, ensure_ascii=False)
    assert "Lookup_n-D" in payload
    assert power["blocks"]
    assert all("params" not in block for block in power["blocks"])
    descriptions = [block["description"] for block in power["blocks"]]
    assert any("PlntEM2EffTbl" in text for text in descriptions)
    assert any("逼近 N 维函数" in text for text in descriptions)
    assert all("{" not in text for text in descriptions)
    assert power["coverage"]["described_blocks"] <= power["coverage"]["blocks"]
    assert len(payload) < 20_000

def test_keydes_renders_instance_values_into_the_template():
    library = KeydesLibrary()
    block = Block(
        sid="1",
        name="Gain",
        block_type="Gain",
        parameters={"Gain": "100", "Multiplication": "Matrix(K*u)", "SampleTime": "-1"},
    )
    key, description = library.describe(block, "en")
    assert key == "Gain"
    assert "100" in description
    assert "matrix product" in description
    assert "{" not in description


def test_keydes_uses_the_english_template_for_parameter_names():
    library = KeydesLibrary()
    block = Block(sid="1", name="Gain", block_type="Gain", parameters={"Gain": "3.5"})
    _, description = library.describe(block, "zh-CN")
    assert "将输入乘以常量" in description
    assert "3.5" in description
    assert "{" not in description


def test_keydes_matches_documented_parameter_names_to_slx_names():
    library = KeydesLibrary()
    block = Block(
        sid="9",
        name="Lookup",
        block_type="Lookup_n-D",
        parameters={
            "NumberOfTableDimensions": "1",
            "Table": "Tbl",
            "BreakpointsForDimension1": "[1 2 3]",
        },
    )
    _, description = library.describe(block, "en")
    assert "Tbl" in description
    assert "[1 2 3]" in description


def test_keydes_leaves_blocks_without_a_template_undescribed():
    library = KeydesLibrary()
    unlinked = Block(
        sid="1",
        name="LPF",
        block_type="Reference",
        parameters={"SourceBlock": "autolibutils/LPF IC", "SourceType": ""},
    )
    assert library.describe(unlinked, "en") == ("LPF IC", None)
    assert library.describe(Block(sid="2", name="Sub", block_type="SubSystem"), "en") == (
        None,
        None,
    )

def test_slx_deduplicates_colliding_directory_names():
    model = parse_slx(CONTROLLER)
    documents = system_json_documents(model)
    assert len(documents) == len(set(documents))


def test_stateflow_states_actions_default_transition_and_conditions():
    charts = parse_stateflow(CONTROLLER)
    assert [chart.chart_id for chart in charts] == ["798", "962"]

    timer = chart_json(charts[1])
    assert len(timer["states"]) == 3
    assert len(timer["transitions"]) == 5
    assert any(state["name"] == "StartTimer" for state in timer["states"])
    assert "Out = 0;" in json.dumps(timer, ensure_ascii=False)
    assert "after(0.1, sec)" in json.dumps(timer, ensure_ascii=False)
    assert timer["transitions"][1]["from_name"] == "StartTimer"

    supervisory = chart_json(charts[0])
    assert len(supervisory["states"]) == 34
    assert len(supervisory["transitions"]) == 35
    assert "EngOnReq = EngOnCalc" in json.dumps(supervisory, ensure_ascii=False)
    assert any(state["name"] == "HEV" for state in supervisory["states"])
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

    rows = sldd_entry_rows(tree)
    altitude = next(row for row in rows if row["name"] == "altitude")
    assert altitude["class"] == "Simulink.Parameter"
    assert altitude["value"] == "4000000.0"
    assert altitude["complexity"] is None
    assert altitude["storage"] == "Auto"
    assert altitude["dimensions"] == [1, 1]
    assert altitude["dtype"] == "auto"
    assert altitude["unit"] is None
    assert altitude["last_modified"] == "20210206T043926.586625"
    assert altitude["last_modified_by"] == "The MathWorks, Inc."
    assert altitude["uuid"] == "fa2b4ae4-c15f-40b5-b2d7-83c715c6f939"
    assert altitude["namespace"] == "dacaf35e-55a5-454d-a7c1-93db038a210e"
    assert altitude["is_derived"] is False
    for column in (
        "status",
        "complexity",
        "min",
        "max",
        "unit",
        "argument",
        "storage",
        "data_source",
        "last_modified",
        "last_modified_by",
    ):
        assert column in altitude
def test_slx_block_ports_edges_and_children_have_no_generated_ids():
    model = parse_slx(
        SAMPLE / "model" / "asbCubeSatMBSE" / "CubeSatMBSEModel" / "asbCubeSatArchModel.slx"
    )
    document = system_json_documents(model)["main.json"]
    blocks = {block["name"]: block for block in document["blocks"]}

    # Port names come from the file: the ModelReference port lists and the
    # subsystem's own Inport/Outport blocks.
    space = blocks["Space Environment"]
    assert space["ports"] == {"in": ["CubeSatStates"], "out": ["Env"]}
    assert space["source_block"] == ""
    assert "id" not in space

    edge = next(
        item for item in document["edges"] if item["from"] == ["Space Environment", "Env"]
    )
    assert edge["signal"] is None
    assert len(edge["to"]) >= 2
    assert all(target[1] for target in edge["to"])
    assert len([item for item in document["edges"] if item["from"] == ["Space Environment", "Env"]]) == 1

    for child in document["children"]:
        assert "block_id" not in child
        assert child["path"].endswith(".json")


def test_slx_unnamed_ports_fall_back_to_port_index():
    documents = system_json_documents(parse_slx(CONTROLLER))
    document = documents["main.json"]
    lookup = next(block for block in document["blocks"] if block["name"] == "ChargeFactor")
    assert lookup["block_type"] == "Lookup_n-D"
    assert lookup["ports"]["in"] == [1]
    assert lookup["source_block"] == ""


@pytest.mark.asyncio
async def test_sldd_multidimensional_values_are_csv_and_original_is_dropped(tmp_path):
    dictionary = (
        SAMPLE
        / "model"
        / "VirtualVehicle"
        / "EngineData"
        / "Dictionaries"
        / "CiEngineCore.sldd"
    )
    result = await MatlabParser().parse(
        dictionary, parse_output_store=LocalParseOutputStore(tmp_path)
    )
    root = Path(result.artifact_ref.root) / "CiEngineCore"
    assert not list(root.glob("*.sldd"))
    assert result.meta["original_preserved"] is False
    rows = {
        row["name"]: row
        for row in map(
            json.loads, (root / "entries.jsonl").read_text(encoding="utf-8").splitlines()
        )
    }

    mep = rows["PlntEngCIGIMepMap"]
    assert mep["dimensions"] == [15, 16]
    assert mep["dtype"] == "double"
    assert mep["complexity"] == "real"
    assert "value" not in mep
    assert mep["data"] == "0008_PlntEngCIGIMepMap.csv"
    matrix = list(csv.reader(io.StringIO((root / mep["data"]).read_text(encoding="utf-8"))))
    assert len(matrix) == 15 and len(matrix[0]) == 16
    assert matrix[0][:4] == ["0.0", "0.0", "0.0", "0.0"]
    assert float(matrix[1][0]) == pytest.approx(158686.535, rel=1e-6)
    assert float(matrix[2][0]) == pytest.approx(343074.266, rel=1e-6)

    turb = rows["PlntEngCITurbEff"]
    assert turb["dimensions"] == [60, 80, 6]
    assert turb["data"] == "0003_PlntEngCITurbEff.csv"
    turb_rows = (root / turb["data"]).read_text(encoding="utf-8").splitlines()
    assert turb_rows[0] == "dim_1,dim_2,dim_3,value"
    assert len(turb_rows) == 60 * 80 * 6 + 1
    assert not (root / "data").exists()


@pytest.mark.asyncio
async def test_sldd_one_dimensional_values_stay_inline(tmp_path):
    dictionary = (
        SAMPLE
        / "model"
        / "VirtualVehicle"
        / "EngineData"
        / "Dictionaries"
        / "CiEngineCore.sldd"
    )
    result = await MatlabParser().parse(
        dictionary, parse_output_store=LocalParseOutputStore(tmp_path)
    )
    root = Path(result.artifact_ref.root) / "CiEngineCore"
    rows = [
        json.loads(line)
        for line in (root / "entries.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    inline = [row for row in rows if "value" in row]
    assert inline
    assert all("data" not in row for row in inline)
    assert all(row["dimensions"] and len(row["dimensions"]) == 2 for row in inline)


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
    payload = json.loads(content)
    assert payload["mat_version"] == "v7.3"
    trajectory = next(item for item in payload["variables"] if item["name"] == "trajectory")
    assert trajectory["dims"] == [2, 2]
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


def test_mlx_blocks_are_code_markdown_and_output():
    live_script = SAMPLE / "model" / "asbCubeSatMBSE" / "MissionAnalysis" / "mappingToolboxAnalysis.mlx"
    notebook, files = parse_mlx_notebook(live_script)
    kinds = {block["type"] for block in notebook["blocks"]}
    assert kinds == {"code", "markdown", "output"}
    assert notebook["counts"] == {
        "code": sum(block["type"] == "code" for block in notebook["blocks"]),
        "markdown": sum(block["type"] == "markdown" for block in notebook["blocks"]),
        "output": sum(block["type"] == "output" for block in notebook["blocks"]),
    }
    assert all(set(block) >= {"type", "content"} for block in notebook["blocks"])
    assert "heading" not in notebook
    assert "cells" not in notebook and "outputs" not in notebook

    # A heading and the text under it stay in one markdown block.
    markdown = [block["content"] for block in notebook["blocks"] if block["type"] == "markdown"]
    assert (
        "## Run the Simulation\n\nRun the simulation if the simulation output object out "
        "does not exist." in markdown
    )

    code = [block["content"] for block in notebook["blocks"] if block["type"] == "code"]
    assert 'arch.model = "asbCubeSatArchModel";' in code[0]
    assert code[0].endswith("end")

    # Every output follows the code block that produced it, and images point at saved files.
    for index, block in enumerate(notebook["blocks"]):
        if block["type"] != "output":
            continue
        previous = index - 1
        while previous >= 0 and notebook["blocks"][previous]["type"] == "output":
            previous -= 1
        assert previous < 0 or notebook["blocks"][previous]["type"] == "code"
        if block["media"] == "image":
            assert block["content"] in files
    assert any(block.get("media") == "image" for block in notebook["blocks"])
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
    metadata = json.loads((root / "secret" / "metadata.json").read_text(encoding="utf-8"))
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
    rows = [
        json.loads(line)
        for line in (root / "requirements" / "requirements.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]
    assert rows[0]["id"] == "R1"
    assert "Battery below 45 C" in rows[0]["description"]


def test_mat_shapes_struct_fields_and_m_source():
    flames = SAMPLE / "data" / "flames.mat"
    content, warnings = parse_mat(flames)
    payload = json.loads(content)
    variable = next(item for item in payload["variables"] if item["name"] == "X")
    assert variable["dims"] == [100, 100]
    assert variable["class"] == "uint8"
    assert not warnings

    documents, warnings = parse_mat_documents(flames)
    csv_path = next(name for name in documents if name.endswith(".csv"))
    rows = list(csv.reader(io.StringIO(documents[csv_path])))
    assert len(rows) == 10001
    assert rows[0] == ["row", "column", "value"]
    assert rows[-1][:2] == ["100", "100"]
    assert "variables.json" in documents
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
    assert "DLBatteryTestData[1]._ObjectMetadata" in agent

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
    assert (base / "data" / "flames" / "flames.mat").is_file()
    assert (base / "data" / "flames" / "variables.json").is_file()
    assert (
        base
        / "model"
        / "asbCubeSatMBSE"
        / "MissionAnalysis"
        / "mappingToolboxAnalysis"
        / "notebook.json"
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
    dictionary = (
        base
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatMBSEModel"
        / "ModelData"
        / "asbCubeSatArchInterfaceData"
    )
    assert (dictionary / "entries.jsonl").is_file()
    assert not list(dictionary.glob("*.sldd"))
    assert not (dictionary / "data").exists()
    assert (base / "src" / "detectChangeOrbitalElements.m").is_file()
    assert not (base / "src" / "detectChangeOrbitalElements.m.md").exists()
    assert list((base / "bin").rglob("*.dll"))
    assert (base / "bin" / "AddOnInstaller" / "metadata.json").is_file()
    assert (base / "bin" / "ingest_firmware.hex").is_file()
    assert (base / "bin" / "visionzynq-target-eventhandler.elf").is_file()
    assert list((base / "model" / "VirtualVehicle" / "PassVeh" / "Plant").glob("*.STL"))
    assert (base / "build").exists() is False  # generated files are skipped, not imported
    assert (base / "slprj").exists() is False
    assert (base / "skipped.json").is_file()
    assert (base / "matlab-classification.json").is_file()
    assert (base / "packages" / "IngestFixtureSupport" / "manifest.json").is_file()
    assert (base / "packages" / "asbCubeSatMBSEProject" / "manifest.json").is_file()

    # Opaque P-code keeps the original bytes plus verified metadata.
    pcode = base / "src" / "autoblkscheckparams" / "autoblkscheckparams.p"
    assert pcode.is_file()
    metadata = json.loads(
        (pcode.parent / "metadata.json").read_text(encoding="utf-8")
    )
    assert metadata["parse_status"] == "opaque"
    assert metadata["sha256"]
    sources = [path for path in SAMPLE.rglob("*") if path.is_file()]
    assert len(sources) == 2717


@pytest.mark.asyncio
async def test_directory_import_keeps_one_folder_per_slx_model(tmp_path):
    """Single-system models in one folder must not overwrite each other's main.json."""
    plant = SAMPLE / "model" / "VirtualVehicle" / "PassVeh" / "Plant"
    names = ["SteeringSystem", "NoSuspension", "IMUSensor"]
    source = tmp_path / "plant"
    source.mkdir()
    for name in names:
        shutil.copyfile(plant / f"{name}.slx", source / f"{name}.slx")

    result = await DirectoryParser().parse(
        source,
        parse_output_store=LocalParseOutputStore(tmp_path / "artifacts"),
        preserve_structure=True,
    )
    root = Path(result.artifact_ref.root)
    systems = {
        json.loads(path.read_text(encoding="utf-8"))["system"]: path
        for path in root.rglob("main.json")
    }

    assert set(names) <= set(systems)
    for name in names:
        assert systems[name].parent.name == name


def test_registry_routes_all_matlab_extensions():
    registry = ParserRegistry()
    for suffix in (".slx", ".sldd", ".mlx", ".mat", ".m", ".p"):
        assert isinstance(registry.get_parser_for_file(f"model{suffix}"), MatlabParser)


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
    assert any("held" in block["description"] for block in enabled["blocks"])
    variants = documents["Variants/main.json"]
    assert variants["type"] == "simulink-subsystem"
    root_blocks = {block["name"]: block for block in root["blocks"]}
    assert root_blocks["Variants"]["key"] is None
    variant_blocks = {block["name"]: block for block in variants["blocks"]}
    assert variant_blocks["High power"]["key"] is None
    assert variant_blocks["High power"]["description"] == ""
    by_name = {block["name"]: block for block in root["blocks"]}
    assert by_name["Electrical +"]["block_type"] == "ConnectionPort"
    assert by_name["Electrical +"]["key"] == "ConnectionPort"
    assert by_name["Electrical +"]["description"] == ""
    assert by_name["Electrical +"]["ports"]["conn"] == ["Electrical +"]
    assert by_name["Torque"]["block_type"] == "PMIOPort"
    assert by_name["Torque"]["ports"]["conn"] == ["Torque"]
@pytest.mark.asyncio
async def test_legacy_mdl_requirements_and_binary_metadata(tmp_path):
    mdl = SAMPLE / "src" / "slctrlobsolete.mdl"
    result = await MatlabParser().parse(
        mdl, parse_output_store=LocalParseOutputStore(tmp_path / "mdl")
    )
    root = Path(result.artifact_ref.root)
    assert (root / "slctrlobsolete" / "main.json").is_file()

    req = (
        SAMPLE
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatRequirements"
        / "ACSRequirements.slreqx"
    )
    result = await MatlabParser().parse(
        req, parse_output_store=LocalParseOutputStore(tmp_path / "req")
    )
    root = Path(result.artifact_ref.root)
    requirements = (root / "ACSRequirements" / "requirements.jsonl").read_text(
        encoding="utf-8"
    )
    assert "CubeSat" in requirements
    assert (root / "ACSRequirements" / "links.jsonl").is_file()

    mex = SAMPLE / "src" / "componentinfo.mexw64"
    result = await MatlabParser().parse(
        mex, parse_output_store=LocalParseOutputStore(tmp_path / "mex")
    )
    root = Path(result.artifact_ref.root)
    metadata = json.loads(
        (root / "componentinfo" / "metadata.json").read_text(encoding="utf-8")
    )
    assert metadata["parse_status"] == "opaque"
    assert (root / "componentinfo" / "componentinfo.mexw64").is_file()
