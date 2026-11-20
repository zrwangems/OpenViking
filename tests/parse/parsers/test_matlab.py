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
from openviking.parse.parsers.matlab.block_description import describe_block
from openviking.parse.parsers.matlab.block_templates import TEMPLATES
from openviking.parse.parsers.matlab.mat import parse_mat, parse_mat_documents
from openviking.parse.parsers.matlab.parser import MatlabParser
from openviking.parse.parsers.matlab.slx import parse_slx, system_json_documents
from openviking.parse.parsers.matlab.stateflow import chart_json, parse_stateflow
from openviking.parse.parsers.matlab.structured import (
    parse_fig_tree,
    parse_mlapp,
    parse_mldatx,
    parse_mlx_notebook,
    parse_requirement_set,
    parse_sldd_tree,
    protected_metadata,
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
def test_system_json_stays_compact_and_keeps_instance_configuration_in_description():
    documents = system_json_documents(parse_slx(CONTROLLER), language="zh-CN")
    power_path = next(
        path for path in documents if path.endswith("Mech_To_Elec_Power_Estimate.json")
    )
    power = documents[power_path]
    payload = json.dumps(power, ensure_ascii=False)
    assert "Lookup_n-D" in payload
    assert power["blocks"]
    assert any(
        "PlntEM2EffTbl" in block["description"] for block in power["blocks"]
    )
    assert "逼近 N 维函数" not in payload
    assert len(payload) < 10_000

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

    from openviking.parse.parsers.matlab.structured import sldd_entry_rows

    rows = sldd_entry_rows(tree)
    altitude = next(row for row in rows if row["name"] == "altitude")
    assert altitude["class"] == "Simulink.Parameter"
    assert altitude["value"] == "4000000.0"
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


def test_mlx_preserves_headings_text_and_code():
    live_script = SAMPLE / "model" / "asbCubeSatMBSE" / "MissionAnalysis" / "mappingToolboxAnalysis.mlx"
    notebook, files = parse_mlx_notebook(live_script)
    kinds = [cell["type"] for cell in notebook["cells"]]
    assert "heading" in kinds and "markdown" in kinds and "code" in kinds
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
    assert (
        base
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatMBSEModel"
        / "ModelData"
        / "asbCubeSatArchInterfaceData"
        / "entries.jsonl"
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
    assert "expression" in root_blocks["Variants"]["description"]
    assert any("V == 1" in block["description"] for block in variants["blocks"])
    by_name = {block["name"]: block for block in root["blocks"]}
    assert by_name["Electrical +"]["block_type"] == "ConnectionPort"
    assert "electrical" in by_name["Electrical +"]["description"]
    assert by_name["Electrical +"]["ports"]["conn"] == [1]
    assert by_name["Torque"]["block_type"] == "PMIOPort"
    assert by_name["Torque"]["ports"]["conn"] == [3]
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


def test_blocks_have_template_description_instead_of_params():
    model = parse_slx(CONTROLLER)
    assert system_json_documents(model, language="zh-CN") == system_json_documents(
        model, language="zh-CN"
    )
    for language in ("en", "zh-CN"):
        documents = system_json_documents(model, language=language)
        for document in documents.values():
            for block in document["blocks"]:
                assert "params" not in block, block
                assert block["description"].strip(), block

    zh = system_json_documents(model, language="zh-CN")
    descriptions = [
        block["description"]
        for document in zh.values()
        for block in document["blocks"]
    ]
    assert any(text.startswith("输出端口") for text in descriptions)
    assert any("增益模块" in text and "1/100" in text for text in descriptions)


def test_every_fixture_block_type_resolves_to_its_own_template():
    types = set()
    for path in Path(__file__).parents[2].joinpath("matlab_repos").rglob("*.slx"):
        try:
            model = parse_slx(path)
        except ValueError:
            continue
        stack = [model]
        while stack:
            system = stack.pop()
            stack.extend(system.children)
            for block in system.blocks:
                types.add(block.block_type)
                assert describe_block(block, "zh-CN").strip(), block
    assert types
    assert types <= set(TEMPLATES), sorted(types - set(TEMPLATES))


def test_unknown_block_type_uses_generic_template_with_its_parameters():
    from openviking.parse.parsers.matlab.block_description import template_for
    from openviking.parse.parsers.matlab.block_templates import GENERIC
    from openviking.parse.parsers.matlab.slx import Block

    block = Block(
        sid="99",
        name="ToolboxOnly",
        block_type="SomeToolboxBlock",
        parameters={"Algorithm": "fast", "Threshold": "3", "Position": "[0, 0, 10, 10]"},
        source_block="toolbox/Some Toolbox Block",
    )
    assert template_for(block.block_type) is GENERIC
    description = describe_block(block, "zh-CN")
    assert "SomeToolboxBlock" in description
    assert "toolbox/Some Toolbox Block" in description
    assert "Algorithm=fast" in description
    assert "Threshold=3" in description
    assert "Position" not in description
