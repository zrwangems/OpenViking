# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0

import json
from pathlib import Path

import pytest

from openviking.parse.output import LocalParseOutputStore
from openviking.parse.parsers.matlab.block_description import describe_block
from openviking.parse.parsers.matlab.official_block_templates import (
    OfficialBlockCatalog,
    load_catalog,
    load_catalog_for_parse,
)
from openviking.parse.parsers.matlab.parser import MatlabParser
from openviking.parse.parsers.matlab.slx import Block, parse_slx, system_json_documents

CONTROLLER = (
    Path(__file__).parents[2]
    / "matlab_repos"
    / "matlab-ingest-fixture"
    / "model"
    / "VirtualVehicle"
    / "VirtualVehicle"
    / "Controller"
    / "HevIpsPowertrainController.slx"
)


def _payload(language="zh-CN"):
    zh = language.startswith("zh")
    gain_summary = (
        "将输入乘以常数。Gain 模块将输入乘以常数值或增益。"
        if zh
        else "The Gain block multiplies the input by a constant value, or gain."
    )
    gain_label = "增益" if zh else "Gain"
    return {
        "schema": "ov.matlab.block-description-templates/1",
        "release": "R2025b",
        "language": language,
        "templates": [
            {
                "key": "Simulink/Commonly Used Blocks/Gain",
                "title": "Gain",
                "product": "simulink",
                "category": "Commonly Used Blocks",
                "page": "gain",
                "summary": gain_summary,
                "parameters": [{"slot": "Gain", "label": gain_label}],
                "source": "Simulink/Commonly Used Blocks/Gain.md",
            },
            {
                "key": "HDL Coder/Math Operations/Gain",
                "title": "Gain",
                "product": "hdlcoder",
                "category": "Math Operations",
                "page": "gain",
                "summary": "HDL Coder 的 Gain。",
                "parameters": [{"slot": "Gain", "label": "Gain"}],
                "source": "HDL Coder/Math Operations/Gain.md",
            },
            {
                "key": "Simulink/Lookup Tables/n-D Lookup Table",
                "title": "n-D Lookup Table",
                "product": "simulink",
                "category": "Lookup Tables",
                "page": "ndlookuptable",
                "summary": "近似 n 维函数。",
                "parameters": [
                    {"slot": "TableSource | Table", "label": "Table data"},
                ],
                "source": "Simulink/Lookup Tables/n-D Lookup Table.md",
            },
        ],
    }


def _catalog(language="zh-CN"):
    return OfficialBlockCatalog.from_dict(_payload(language), language=language)


def test_official_template_precedes_type_template_and_fills_parameters():
    block = Block(
        sid="1",
        name="Gain",
        block_type="Gain",
        parameters={"Gain": "5", "Position": "[0, 0, 10, 10]"},
    )
    description = describe_block(block, "zh-CN", _catalog())
    assert description.startswith("将输入乘以常数")
    assert "增益 为 5" in description
    assert "Gain 模块" in description
    assert "Position" not in description


def test_deduplicates_same_name_by_simulink_product_and_category():
    entry = _catalog().resolve("Gain", "")
    assert entry is not None
    assert entry.key == "Simulink/Commonly Used Blocks/Gain"


def test_composite_parameter_slot_uses_the_present_block_parameter():
    block = Block(
        sid="2",
        name="Lookup",
        block_type="Lookup_n-D",
        parameters={"Table": "PlntTable", "NumberOfTableDimensions": "2"},
    )
    description = describe_block(block, "zh-CN", _catalog())
    assert "Table data 为 PlntTable" in description


def test_missing_official_entry_falls_back_to_type_template():
    block = Block(sid="3", name="Custom", block_type="MadeUpToolboxBlock")
    description = describe_block(block, "zh-CN", _catalog())
    assert "MadeUpToolboxBlock" in description
    assert description.strip()


def test_english_catalog_renders_english_configuration():
    catalog = OfficialBlockCatalog.from_dict(_payload("en"), language="en")
    block = Block(sid="1", name="Gain", block_type="Gain", parameters={"Gain": "5"})
    description = describe_block(block, "en", catalog)
    assert "multiplies the input" in description
    assert "Configuration:" in description


def test_load_catalog_from_local_library_root(monkeypatch, tmp_path):
    root = tmp_path / "library"
    target = root / "matlab" / "zh" / "simulink-block-library" / "templates.json"
    target.parent.mkdir(parents=True)
    target.write_text(json.dumps(_payload(), ensure_ascii=False), encoding="utf-8")
    monkeypatch.setenv("OPENVIKING_MATLAB_BLOCK_LIBRARY", str(root))
    catalog = load_catalog("zh-CN")
    assert catalog is not None
    assert catalog.resolve("Gain", "").key == "Simulink/Commonly Used Blocks/Gain"


def test_system_json_uses_the_official_catalog():
    documents = system_json_documents(
        parse_slx(CONTROLLER), language="zh-CN", catalog=_catalog()
    )
    descriptions = [
        block["description"]
        for document in documents.values()
        for block in document["blocks"]
    ]
    assert any(text.startswith("将输入乘以常数") for text in descriptions)
    assert all(text.strip() for text in descriptions)
    assert all("params" not in block for document in documents.values() for block in document["blocks"])


@pytest.mark.asyncio
async def test_parser_loads_catalog_from_configured_local_library(monkeypatch, tmp_path):
    root = tmp_path / "library"
    target = root / "matlab" / "zh" / "simulink-block-library" / "templates.json"
    target.parent.mkdir(parents=True)
    target.write_text(json.dumps(_payload(), ensure_ascii=False), encoding="utf-8")
    monkeypatch.setenv("OPENVIKING_MATLAB_BLOCK_LIBRARY", str(root))
    result = await MatlabParser().parse(
        CONTROLLER,
        language="zh-CN",
        parse_output_store=LocalParseOutputStore(tmp_path / "art"),
    )
    output = Path(result.artifact_ref.root)
    descriptions = [
        block.get("description", "")
        for document in output.rglob("*.json")
        for block in json.loads(document.read_text(encoding="utf-8")).get("blocks", [])
    ]
    assert any(text.startswith("将输入乘以常数") for text in descriptions)


@pytest.mark.asyncio
async def test_load_catalog_from_openviking_asset(monkeypatch):
    class FakeVikingFS:
        async def read_file(self, uri):
            assert uri.endswith(
                "openviking-engineering-resources/matlab/zh/simulink-block-library/templates.json"
            )
            return json.dumps(_payload(), ensure_ascii=False)

    monkeypatch.delenv("OPENVIKING_MATLAB_BLOCK_LIBRARY", raising=False)
    catalog = await load_catalog_for_parse("zh-CN", FakeVikingFS())
    assert catalog is not None
    assert catalog.resolve("Gain", "").key == "Simulink/Commonly Used Blocks/Gain"


@pytest.mark.asyncio
async def test_missing_asset_is_silent_fallback(monkeypatch):
    class MissingVikingFS:
        async def read_file(self, uri):
            raise FileNotFoundError(uri)

    monkeypatch.delenv("OPENVIKING_MATLAB_BLOCK_LIBRARY", raising=False)
    assert await load_catalog_for_parse("zh-CN", MissingVikingFS()) is None
