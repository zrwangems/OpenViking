# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0

from pathlib import Path

import pytest

from openviking.parse.directory_scan import scan_directory
from openviking.parse.output import LocalParseOutputStore
from openviking.parse.parsers.directory import DirectoryParser
from openviking.parse.parsers.matlab.classification import (
    ACTION_AGGREGATE,
    ACTION_ATTACH,
    ACTION_EXCLUDE,
    ACTION_IMPORT,
    SUMMARY_ON_DEMAND,
    SUMMARY_ORIGINAL,
    categories_for,
    classify_directory,
    classify_path,
    project_table,
    resolve_redundancy,
)

SAMPLE = Path(__file__).parents[2] / "matlab_repos" / "matlab-ingest-fixture"


def test_extensions_can_have_multiple_categories():
    assert categories_for(".sldd") == ("ZIP/工具容器", "数据/目标二进制")
    assert categories_for(".ctf") == ("ZIP/工具容器", "加密/保护")
    assert categories_for(".hex") == ("数据/目标二进制",)
    assert categories_for(".m") == ("可读文本",)


def test_location_changes_tags_and_action():
    source = classify_path("src/controller.c")
    assert source["categories"] == ["可读文本"]
    assert source["tags"] == []
    assert source["action"] == ACTION_IMPORT

    generated = classify_path("Model_ert_rtw/controller.c")
    assert generated["action"] == ACTION_EXCLUDE
    assert "codegen" in generated["tags"]

    runtime = classify_path("slprj/rsim/Model/model.mat")
    assert runtime["action"] == ACTION_EXCLUDE
    assert {"runtime", "slprj"} <= set(runtime["tags"])

    firmware_build = classify_path("build/fw.hex")
    assert firmware_build["action"] == ACTION_EXCLUDE
    assert {"codegen", "target"} <= set(firmware_build["tags"])

    firmware_delivery = classify_path("deliver/fw.hex")
    assert firmware_delivery["action"] == ACTION_ATTACH
    assert "target" not in firmware_delivery["tags"]

    mapping = classify_path("build/fw.map")
    assert mapping["action"] == ACTION_EXCLUDE
    assert "build" in mapping["tags"]


def test_build_directories_are_labelled():
    slprj = classify_directory("slprj/ert/Model")
    assert slprj["categories"] == ["派生/缓存"]
    assert "slprj" in slprj["tags"]
    assert slprj["action"] == ACTION_EXCLUDE

    rtw = classify_directory("Model_ert_rtw")
    assert "codegen" in rtw["tags"]


@pytest.mark.asyncio
async def test_directory_import_writes_multilabel_manifest(tmp_path):
    project = tmp_path / "proj"
    (project / "src").mkdir(parents=True)
    (project / "slprj" / "ert" / "Model").mkdir(parents=True)
    (project / "Model_ert_rtw").mkdir(parents=True)
    (project / "build").mkdir()
    (project / "deliver").mkdir()
    (project / "model.ssc").write_text("component Marker\nend\n", encoding="utf-8")
    (project / "src" / "controller.c").write_text("int f(void) { return 1; }\n", encoding="utf-8")
    (project / "slprj" / "ert" / "Model" / "generated.c").write_text("int g;\n", encoding="utf-8")
    (project / "Model_ert_rtw" / "generated.h").write_text("int g;\n", encoding="utf-8")
    (project / "build" / "fw.hex").write_text(":00000001FF\n", encoding="utf-8")
    (project / "deliver" / "fw.hex").write_text(":00000001FF\n", encoding="utf-8")
    (project / "proj.prj").write_text("<MATLABProject/>", encoding="utf-8")
    (project / "resources" / "project" / "hash").mkdir(parents=True)
    (project / "resources" / "project" / "hash" / "state.xml").write_text(
        '<Info location="model.slx" type="File"/>', encoding="utf-8"
    )

    store = LocalParseOutputStore(tmp_path / "artifacts")
    result = await DirectoryParser().parse(project, parse_output_store=store)
    root = Path(result.artifact_ref.root)

    import json

    manifest = json.loads(
        (root / "proj" / "matlab-classification.json").read_text(encoding="utf-8")
    )
    assert manifest["schema"] == "ov.matlab.classification/1"
    imported = {item["path"] for item in manifest["files"]}
    assert "src/controller.c" in imported
    assert "model.ssc" in imported
    assert "deliver/fw.hex" in imported

    skipped_doc = json.loads((root / "proj" / "skipped.json").read_text(encoding="utf-8"))
    skipped = {item["path"]: item for item in skipped_doc["entries"]}
    assert "slprj" in skipped["slprj/ert/Model/generated.c"]["tags"]
    assert "codegen" in skipped["Model_ert_rtw/generated.h"]["tags"]
    assert {"codegen", "target"} <= set(skipped["build/fw.hex"]["tags"])
    assert all(item["reason"] == "matlab build/cache" for item in skipped.values())

    # A .c file is source text here, so the manifest counts the readable category.
    assert manifest["summary"]["categories"]["可读文本"] >= 2

    # Project state is recorded, not imported.
    assert "proj.prj" not in imported
    assert "resources/project/hash/state.xml" not in imported
    assert not (root / "proj" / "resources").exists()
    assert manifest["projects"] == [
        {
            "root": ".",
            "prj": "proj.prj",
            "resources": 1,
            "bytes": len(b'<Info location="model.slx" type="File"/>'),
            "categories": {},
            "files": [{"path": "resources/project/hash/state.xml", "target": "model.slx"}],
        }
    ]


def test_location_outranks_extension_for_build_scripts():
    startup = classify_path("run_all.bat")
    assert startup["action"] == ACTION_IMPORT
    assert startup["summary"] == SUMMARY_ORIGINAL
    assert "startup" in startup["tags"]

    in_build = classify_path("build/run_all.bat")
    assert in_build["action"] == ACTION_EXCLUDE
    assert "build" in in_build["tags"]

    # A .map is an attachment wherever it sits, and nothing is extracted up front.
    mapping = classify_path("deliver/fw.map")
    assert mapping["action"] == ACTION_ATTACH
    assert mapping["summary"] == SUMMARY_ON_DEMAND


def test_project_files_only_reach_the_aggregation_table():
    project = classify_path("Plant.prj")
    assert project["action"] == ACTION_AGGREGATE
    assert project["categories"] == ["可读文本"]

    state = classify_path("resources/project/hash/file.xml")
    assert state["action"] == ACTION_AGGREGATE

    nested = classify_path("model/SI/resources/project/hash/file.xml")
    assert nested["action"] == ACTION_AGGREGATE


def test_unknown_extension_is_kept_and_marked():
    unknown = classify_path("data/params.zzz")
    assert unknown["action"] == ACTION_IMPORT
    assert unknown["summary"] == SUMMARY_ORIGINAL
    assert "unclassified" in unknown["tags"]

    # The extensions that used to fall through now have a category of their own.
    for name in ("shot.gif", "shot.jpg", "scene.svg", "scene.wrl"):
        labels = classify_path(name)
        assert labels["categories"] == ["图像/三维模型"]
        assert "unclassified" not in labels["tags"]


def test_export_with_a_generated_source_is_redundant():
    redundancy = resolve_redundancy(
        None,
        ["fig/plot.fig", "fig/plot.png", "report.m", "report.html", "run.mat", "run.csv"],
    )

    assert redundancy.redundant == {
        "fig/plot.png": "fig/plot.fig",
        "report.html": "report.m",
        "run.csv": "run.mat",
    }


def test_package_copy_is_a_duplicate_of_the_project_one(tmp_path):
    (tmp_path / "Vehicle.slx").write_bytes(b"PK\x03\x04plant")
    model_fmu = tmp_path / "model" / "Plant.fmu"
    packaged_fmu = tmp_path / "packages" / "Plant.fmu"
    for path in (model_fmu, packaged_fmu):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"fmu-bytes")

    redundancy = resolve_redundancy(
        tmp_path, ["model/Plant.fmu", "packages/Plant.fmu", "Vehicle.slx"]
    )

    assert redundancy.duplicates == {"packages/Plant.fmu": "model/Plant.fmu"}

    generated = resolve_redundancy(None, ["Plant.slx", "Plant.fmu"])
    assert generated.redundant == {"Plant.fmu": "Plant.slx"}


def test_app_screenshot_is_only_flagged_as_possible_redundant():
    redundancy = resolve_redundancy(None, ["app/panel.mlapp", "app/panel.png"])

    assert redundancy.possible == {"app/panel.png": "app/panel.mlapp"}
    assert redundancy.redundant == {}


def test_fixture_account_and_project_table():
    result = scan_directory(SAMPLE)

    assert len(result.processable) == 1146
    assert len(result.aggregated) == 2204
    assert [item.rel_path for item in result.duplicates] == ["packages/VvcFmuEngExl.fmu"]
    flagged = [item for item in result.processable if "possible_redundant" in item.tags]
    assert len(flagged) == 5

    table = project_table((item.rel_path, item.path) for item in result.aggregated)
    assert len(table) == 13
    root_project = table[0]
    assert root_project["root"] == "."
    assert root_project["prj"] == "MatlabIngestFixture.prj"
    assert root_project["resources"] == 771
    assert root_project["categories"]["design"] > 0
    assert sum(item["resources"] for item in table) == 2191
    assert len(root_project["files"]) == 771
    categorized = [row for row in root_project["files"] if row.get("category")]
    assert {row["category"] for row in categorized} <= {
        "design",
        "derived",
        "test",
        "artifact",
        "none",
    }
    assert all(row.get("target") for row in categorized)

def test_editor_backup_is_excluded_and_workbook_is_read_as_cells():
    """Editor leftovers stay out of the tree; a spreadsheet is parsed, not copied."""
    backup = classify_path("src/old_script.m.asv")
    assert backup["action"] == ACTION_EXCLUDE
    assert backup["reason"] == "matlab derived file"

    workbook = classify_path("model/Plant/Calibrations/SiEngineData.xlsx")
    assert workbook["action"] == ACTION_IMPORT
    assert workbook["summary"] == "parse"
    assert workbook["categories"] == ["数据/目标二进制"]
