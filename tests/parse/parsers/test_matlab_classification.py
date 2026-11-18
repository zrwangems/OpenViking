# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0

from pathlib import Path

import pytest

from openviking.parse.output import LocalParseOutputStore
from openviking.parse.parsers.directory import DirectoryParser
from openviking.parse.parsers.matlab.classification import (
    ACTION_ATTACH,
    ACTION_EXCLUDE,
    ACTION_IMPORT,
    categories_for,
    classify_directory,
    classify_path,
)


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

    store = LocalParseOutputStore(tmp_path / "artifacts")
    result = await DirectoryParser().parse(project, parse_output_store=store)
    root = Path(result.artifact_ref.root)

    import json

    manifest = json.loads((root / "matlab-classification.json").read_text(encoding="utf-8"))
    assert manifest["schema"] == "ov.matlab.classification/1"
    imported = {item["path"] for item in manifest["files"]}
    assert "src/controller.c" in imported
    assert "model.ssc" in imported
    assert "deliver/fw.hex" in imported

    skipped_doc = json.loads((root / "skipped.json").read_text(encoding="utf-8"))
    skipped = {item["path"]: item for item in skipped_doc["entries"]}
    assert "slprj" in skipped["slprj"]["tags"]
    assert "codegen" in skipped["Model_ert_rtw"]["tags"]
    assert "build" in skipped["build"]["tags"]

    # A .c file is source text here, so the manifest counts the readable category.
    assert manifest["summary"]["categories"]["可读文本"] >= 2
