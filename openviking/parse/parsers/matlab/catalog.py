# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Official Simulink library categories and block-name matching."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from openviking.parse.parsers.matlab.catalog_data import _CATALOG, _CATEGORY_TITLES

_ALIASES = {
    "Add": "Sum",
    "Subtract": "Sum",
    "Sum of Elements": "Sum",
    "Sum": "Sum",
    "Gain": "Gain",
    "Product": "Product, Matrix Multiply",
    "Logic": "Logical Operator",
    "RelationalOperator": "Relational Operator",
    "SubSystem": "Subsystem",
    "Inport": "Inport",
    "Outport": "Outport",
    "Reference": "",
    "S-Function": "S-Function",
    "MATLABSystem": "MATLAB System",
    "DataStoreMemory": "Data Store Memory",
    "DataStoreRead": "Data Store Read",
    "DataStoreWrite": "Data Store Write",
    "UnitDelay": "Unit Delay",
    "Lookup_n-D": "n-D Lookup Table",
    "Math": "Math Function",
    "Signum": "Sign",
    "Saturate": "Saturation",
    "RateTransition": "Rate Transition",
    "UnitConversion": "Unit Conversion",
    "FirstOrderHold": "First Order Hold",
    "TransferFcn": "Transfer Fcn",
    "ModelReference": "Model",
    "ToWorkspace": "To Workspace",
    "TriggerPort": "Trigger",
    "Second-Order Integrator": "Second-Order Integrator",
}


def _normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def find_block(block_type: str, source_block: str = "") -> tuple[str, str] | None:
    """Resolve an SLX BlockType or library basename to an official category/page."""
    candidates = [source_block.rsplit("/", 1)[-1], _ALIASES.get(block_type, ""), block_type]
    category_by_name = {_normalize(title): family for family, title in _CATEGORY_TITLES.items()}
    source_families = {
        category_by_name[_normalize(part)]
        for part in source_block.split("/")[:-1]
        if _normalize(part) in category_by_name
    }
    # Use the original library path to distinguish duplicate names such as
    # Sinks/Display from Dashboard/Display. Fall back for renamed libraries.
    families = sorted(
        _CATALOG.items(),
        key=lambda item: (
            bool(source_families) and item[0] not in source_families,
            item[0] == "commonly-used-blocks",
        ),
    )
    for candidate in candidates:
        normalized = _normalize(candidate)
        for family, names in families:
            for name in names:
                if normalized and normalized == _normalize(name):
                    return family, name
    return None


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def export_catalog(
    directory: str | Path,
    subtitles: dict[tuple[str, str], str] | None = None,
) -> list[Path]:
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    subtitles = subtitles or {}
    written = []
    total = sum(len(names) for names in _CATALOG.values())
    unique_documents = len({name for names in _CATALOG.values() for name in names})
    index = [
        "---",
        "type: simulink-block-catalog",
        "release: R2025b",
        "directory_contract: mathworks-simulink-blocks-by-category",
        "---",
        "",
        "# Simulink 块知识库",
        "",
        "目录与 MathWorks R2025b Simulink Blocks 分类列表一致。内容已从官方块文档抽取并保存在本地，不需要联网跳转。",
        "",
        f"共 **{len(_CATALOG)}** 个官方目录、**{total}** 个目录条目、**{unique_documents}** 个不同块名。每块保存用途、所属库、端口、参数和特性。Separate Toolboxes/Blocksets 不属于这里的 Simulink 基础产品目录。",
        "",
    ]
    for family, names in _CATALOG.items():
        title = _CATEGORY_TITLES[family]
        index.append(f"- [{title}]({family}/index.md)：{len(names)} 个")
        lines = [
            "---",
            "type: simulink-block-family",
            f"family: {family}",
            "---",
            "",
            f"# {title}",
            "",
            "| 块名称 | 官方文档摘要 |",
            "| --- | --- |",
        ]
        for name in names:
            summary = subtitles.get((family, name), "本地文档待抓取").replace("|", "\\|")
            lines.append(f"| [{name}]({_slug(name)}.md) | {summary} |")
        target = directory / family / "index.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written.append(target)
    target = directory / "index.md"
    target.write_text("\n".join(index) + "\n", encoding="utf-8")
    written.append(target)
    return written


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export official Simulink category indexes")
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    for output in export_catalog(args.directory):
        print(output)
