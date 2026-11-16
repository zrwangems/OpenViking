# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Match SLX block identities directly against the packaged Markdown library."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from openviking.parse.parsers.matlab.library import (
    BlockReference,
    block_references,
    catalog_entries,
    slug,
)

# Actual SourceBlock roots do not always equal documentation product IDs.
# Unknown roots remain external even when a third-party block has an official-
# sounding name. Add aliases only from observed MathWorks library metadata.
_SOURCE_PRODUCT_ALIASES = {
    "simscapefoundationlibrary": "simscape",
    "fllib": "hydro",
    "powerlib": "sps",
    "powersys": "sps",
    "eelib": "sps",
    "smlib": "sm",
}


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


def find_block_reference(block_type: str, source_block: str = "") -> BlockReference | None:
    """Resolve by original library path before falling back to a unique name.

    Matching a metadata-only entry is useful during ingestion, but does not
    imply that its full document has been scraped; callers must inspect
    ``full_document``. Product and category components disambiguate duplicate
    names such as Sinks/Display and Dashboard/Display.
    """
    candidates = [source_block.rsplit("/", 1)[-1], _ALIASES.get(block_type, ""), block_type]
    source_parts = [_normalize(part) for part in source_block.split("/")[:-1]]
    source_parts = [part for part in source_parts if part]
    known_products = {_normalize(ref.product_id) for ref in block_references()} | {
        _normalize(ref.product_name) for ref in block_references()
    }
    if source_parts:
        source_root = source_parts[0]
        product_alias = _SOURCE_PRODUCT_ALIASES.get(source_root)
        if source_root not in known_products and not product_alias:
            return None

    def score(reference: BlockReference) -> tuple[int, int, int, int]:
        product_tokens = {_normalize(reference.product_id), _normalize(reference.product_name)}
        product_match = bool(product_tokens.intersection(source_parts)) or (
            bool(source_parts)
            and _SOURCE_PRODUCT_ALIASES.get(source_parts[0]) == reference.product_id
        )
        library_parts = {_normalize(part) for part in reference.library_path}
        path_matches = len(library_parts.intersection(source_parts))
        common = "Commonly Used Blocks" in reference.library_path
        # Path evidence outranks document availability. Otherwise a duplicate
        # name can silently select a template from the wrong product.
        return (product_match, path_matches, not common, reference.full_document)

    for candidate in candidates:
        normalized = _normalize(candidate)
        if not normalized:
            continue
        matches = [ref for ref in block_references() if _normalize(ref.name) == normalized]
        if matches:
            return max(matches, key=score)
    return None


def find_block(block_type: str, source_block: str = "") -> tuple[str, str] | None:
    """Resolve only blocks with a packaged full English/Chinese document."""
    reference = find_block_reference(block_type, source_block)
    if not reference or not reference.full_document:
        return None
    if reference.product_id == "simulink" and "commonlyusedblocks" in {
        _normalize(part) for part in source_block.split("/")
    }:
        return "simulink/commonly-used-blocks", reference.name
    relative = reference.resource_path("en")
    if not relative or not relative.startswith("en/"):
        return None
    family = relative.removeprefix("en/").rsplit("/", 1)[0]
    return family, reference.name


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
