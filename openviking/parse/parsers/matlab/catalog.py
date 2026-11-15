# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Match SLX block identities directly against the packaged Markdown library."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from openviking.parse.parsers.matlab.library import catalog_entries, slug

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
    """Resolve an SLX BlockType or library basename to a local Markdown page."""
    candidates = [source_block.rsplit("/", 1)[-1], _ALIASES.get(block_type, ""), block_type]
    entries = catalog_entries()
    category_by_name = {_normalize(category): family for family, category, _, _ in entries}
    source_families = {
        category_by_name[_normalize(part)]
        for part in source_block.split("/")[:-1]
        if _normalize(part) in category_by_name
    }
    # The original library path distinguishes duplicate names such as
    # Sinks/Display from Dashboard/Display. Fall back for renamed libraries.
    ordered_entries = sorted(
        entries,
        key=lambda entry: (
            bool(source_families) and entry[0] not in source_families,
            entry[0] == "commonly-used-blocks",
        ),
    )
    for candidate in candidates:
        normalized = _normalize(candidate)
        for family, _, name, _ in ordered_entries:
            if normalized and normalized == _normalize(name):
                return family, name
    return None


def export_catalog(directory: str | Path) -> list[Path]:
    """Rebuild category indexes from the block documents themselves."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    entries = catalog_entries()
    families: dict[str, tuple[str, list[tuple[str, str]]]] = {}
    for family, category, name, summary in entries:
        families.setdefault(family, (category, []))[1].append((name, summary))
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
        f"共 **{len(families)}** 个官方目录、**{len(entries)}** 个目录条目、**{len({name for _, _, name, _ in entries})}** 个不同块名。每块保存用途、所属库、端口、参数和特性。Separate Toolboxes/Blocksets 不属于这里的 Simulink 基础产品目录。",
        "",
    ]
    written = []
    for family, (category, blocks) in families.items():
        index.append(f"- [{category}]({family}/index.md)：{len(blocks)} 个")
        lines = [
            "---",
            "type: simulink-block-family",
            f"family: {family}",
            "---",
            "",
            f"# {category}",
            "",
            "| 块名称 | 官方文档摘要 |",
            "| --- | --- |",
        ]
        for name, summary in blocks:
            lines.append(f"| [{name}]({slug(name)}.md) | {summary.replace('|', chr(92) + '|')} |")
        target = directory / family / "index.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written.append(target)
    target = directory / "index.md"
    target.write_text("\n".join(index) + "\n", encoding="utf-8")
    written.append(target)
    return written


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Simulink category indexes from Markdown")
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    for output in export_catalog(args.directory):
        print(output)
