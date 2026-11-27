"""Plan-level checks for the 65 MATLAB file types.

These tests use the committed ingest fixture, not generated approximations, so a
regression in any of the documented container formats is caught early.
"""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

from openviking.parse.parsers.matlab.formats import archive_manifest
from openviking.parse.parsers.matlab.mdl import parse_mdl
from openviking.parse.parsers.matlab.measurement import parse_measurement
from openviking.parse.parsers.matlab.packages import (
    fmu_metadata,
    jar_metadata,
    package_metadata,
)
from openviking.parse.parsers.matlab.figures import parse_figure
from openviking.parse.parsers.matlab.structured import (
    parse_mldatx,
    parse_requirement_set,
    parse_sldd_tree,
    protected_metadata,
    sldd_entry_rows,
)

SAMPLE = Path(__file__).resolve().parents[2] / "matlab_repos" / "matlab-ingest-fixture"


def test_legacy_mdl_library_blocks_and_nested_edges():
    model = parse_mdl(SAMPLE / "src" / "slctrlobsolete.mdl")
    assert model.name == "slctrlobsolete"
    assert len(model.blocks) == 2
    assert [child.name for child in model.children] == ["Input Point", "Output Point"]
    assert all(child.edges for child in model.children)


def test_sldd_entries_keep_bus_elements_and_config_components():
    dictionary = (
        SAMPLE
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatMBSEModel"
        / "ModelData"
        / "asbCubeSatArchInterfaceData.sldd"
    )
    rows = {row["name"]: row for row in sldd_entry_rows(parse_sldd_tree(dictionary))}
    assert rows["altitude"]["dimensions"] == [1, 1]
    assert rows["h_table"]["dimensions"] == [5, 1]
    assert [item["name"] for item in rows["GNCtoPowerBus"]["elements"]] == [
        "InSunView",
        "SunAngle",
    ]
    assert rows["GNCtoPowerBus"]["elements"][0]["dtype"] == "boolean"
    assert "Simulink.SolverCC" in rows["CubeSatConfigSet"]["components"]


def test_requirement_set_and_link_set_expand_ids_and_targets():
    base = SAMPLE / "model" / "asbCubeSatMBSE" / "CubeSatRequirements"
    requirements = parse_requirement_set(base / "ACSRequirements.slreqx")
    rows = requirements["requirements"]
    assert len(rows) == 22
    assert {row["id"] for row in rows} >= {"1", "3", "4"}
    assert rows[0]["title"] == "Attitude Control Modes"
    assert "CubeSat shall" in rows[0]["description"]

    links = parse_requirement_set(base / "asbCubeSatArchModel.slmx")["links"]
    assert len(links) == 17
    assert links[0]["requirement"] == "SystemRequirements:1"
    assert links[0]["element"] == ":1"
    assert links[0]["type"] == "Implement"


def test_mldatx_expands_suites_cases_inputs_and_criteria(tmp_path):
    path = (
        SAMPLE
        / "model"
        / "asbCubeSatMBSE"
        / "MissionAnalysis"
        / "SystemTests"
        / "systemTests.mldatx"
    )
    tree = parse_mldatx(path)
    assert tree["coverage"] == {"suites": 2, "cases": 1}
    suites = {suite["name"]: suite for suite in tree["suites"]}
    assert suites["conopsTests"]["parent"] == "systemTests"
    case = suites["conopsTests"]["cases"][0]
    assert case["name"] == "Verify visual imagery"
    assert case["inputs"]["SystemUnderTest"]["model"]["Name"]["text"] == "asbCubeSatArchModel"
    assert "CustomCriteria" in case["criteria"]


def test_fig_reports_axes_and_widgets():
    payload, files = parse_figure(SAMPLE / "data" / "teapotdemo.fig")
    assert payload["schema"] == "ov.matlab.figure/2"
    assert payload["summary"]["axes_count"] == 1
    assert payload["figures"][0]["name"] == "Untitled"
    assert files == {}


def test_fmu_packages_and_jar_expose_plan_metadata():
    fmu = SAMPLE / "packages" / "VvcFmuEngExl.fmu"
    manifest = fmu_metadata(fmu, archive_manifest(fmu))
    assert manifest["model"]["name"] == "VvcFmuEngExl"
    assert manifest["model"]["fmi_version"] == "2.0"
    assert len(manifest["variables"]) == 11

    project = SAMPLE / "packages" / "MatlabIngestFixture.mlproj"
    project_manifest = package_metadata(project, archive_manifest(project))
    assert project_manifest["project"]["title"] == "MatlabIngestFixture"

    toolbox = SAMPLE / "packages" / "IngestFixtureToolbox.mltbx"
    toolbox_manifest = package_metadata(toolbox, archive_manifest(toolbox))
    assert toolbox_manifest["toolbox"]["version"] == "1.0"
    assert toolbox_manifest["toolbox"]["release_compatibility"]["start"] == "R2014b"

    support = SAMPLE / "packages" / "IngestFixtureSupport.mlpkginstall"
    support_manifest = package_metadata(support, archive_manifest(support))
    assert support_manifest["support_package"]["hardware"] == "Generic Fixture Board"

    template = SAMPLE / "packages" / "asbCubeSatMBSEProject.sltx"
    template_manifest = package_metadata(template, archive_manifest(template))
    assert template_manifest["template"]["name"] == (
        "CubeSat Model-Based System Engineering Project"
    )
    assert "Aerospace Blockset" in template_manifest["template"]["required_products"]

    jar = SAMPLE / "packages" / "addons.jar"
    jar_manifest = jar_metadata(jar, archive_manifest(jar))
    assert jar_manifest["java_manifest"]["Manifest-Version"] == "1.0"
    assert any(name.endswith(".class") for name in jar_manifest["classes"])


def test_measurement_channels_and_protected_metadata():
    for name in ("ingest_measurement.mdf", "ingest_measurement.mf4", "ingest_canlog.blf"):
        documents, _ = parse_measurement(SAMPLE / "data" / name)
        payload = json.loads(documents["channels.json"])
        assert payload["channels"], name
        assert payload["parse_status"] == "parsed", name
        assert any(key.startswith("data/") for key in documents), name

    pcode = protected_metadata(SAMPLE / "src" / "autoblkscheckparams.p", "pcode")
    assert pcode["version_hint"]
    slxp = protected_metadata(
        SAMPLE / "packages" / "EvPowertrainController2EM.slxp", "slxp"
    )
    assert slxp["container"] == "zip"
    assert slxp["members"]
    assert zipfile.is_zipfile(SAMPLE / "packages" / "EvPowertrainController2EM.slxp")
