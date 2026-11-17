# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Add and read machine-readable data in Simulink block Markdown pages.

The generated YAML is an index of the original knowledge, not a second copy of
it. Port and parameter prose stays in Markdown, so restructuring cannot discard
dependencies, examples, equations, tables, or domain-specific explanations.
"""

from __future__ import annotations

import re
from typing import Any

import yaml

_SECTION_NAMES = {
    "ports": ("Ports", "端口"),
    "parameters": ("Parameters", "参数"),
}
_RECORD_HEADING = re.compile(r"^### \*\*(.+?)\*\*\s+[—-]\s*(.*)$")
_GROUP_HEADING = re.compile(r"^### (?!\*\*)(.+?)\s*$")
_DIRECTIONS = {
    "input": "input",
    "inputs": "input",
    "输入": "input",
    "output": "output",
    "outputs": "output",
    "输出": "output",
    "conserving": "conserving",
    "守恒端口": "conserving",
}
_PARAMETER_KEYS = {
    "block parameter": "block_parameter",
    "parameter": "block_parameter",
    "模块参数": "block_parameter",
    "参数": "block_parameter",
    "type": "type",
    "类型": "type",
    "values": "values",
    "value": "values",
    "值": "values",
    "default": "default",
    "默认值": "default",
}


def _plain(value: str) -> str:
    value = value.strip()
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = value.replace("**", "").replace(r"\_", "_")
    return value.strip()


def _programmatic_value(line: str) -> tuple[str, str] | None:
    row = line.strip().strip("|").strip()
    match = re.fullmatch(r"\*\*(.+?)\*\*\s*[:：]?\s*(.*)", row)
    if not match:
        return None
    key = _PARAMETER_KEYS.get(_plain(match.group(1)).strip().rstrip(":：").lower())
    if not key:
        return None
    # Enum tables often contain literal pipes. Keep the complete value instead
    # of treating every pipe as a reliable Markdown cell separator.
    value = match.group(2).strip().lstrip("|").strip()
    return key, _plain(value)


def _record_data(kind: str, content: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    group = ""
    for line in content.splitlines():
        heading = _RECORD_HEADING.match(line)
        if heading:
            current = {
                "name": _plain(heading.group(1)),
                "summary": _plain(heading.group(2)),
            }
            if kind == "ports":
                current["direction"] = (
                    group if group in {"input", "output", "conserving"} else "unspecified"
                )
            else:
                current["group"] = group
            records.append(current)
            continue
        plain_group = _GROUP_HEADING.match(line)
        if plain_group:
            title = _plain(plain_group.group(1))
            if kind == "ports":
                direction = _DIRECTIONS.get(title.lower())
                if direction:
                    for record in records:
                        if record["direction"] == "unspecified":
                            record["direction"] = direction
                if direction:
                    group = direction
                    current = None
            else:
                group = title
                current = None
            continue
        if current is None:
            continue
        data_types = re.fullmatch(
            r"\*\*(?:Data Types|数据类型)\s*[:：]\*\*\s*(.*)", line.strip()
        ) or re.fullmatch(r"\*\*(?:Data Types|数据类型)[:：]\*\*\s*(.*)", line.strip())
        if kind == "ports" and data_types:
            current["data_types"] = _plain(data_types.group(1))
            continue
        if kind == "parameters":
            programmatic = _programmatic_value(line)
            if programmatic:
                current[programmatic[0]] = programmatic[1]
    return records


def _section_span(document: str, names: tuple[str, ...]) -> re.Match[str] | None:
    return re.search(
        rf"^## (?:{'|'.join(map(re.escape, names))})\n(.*?)(?=^## |\Z)",
        document,
        re.MULTILINE | re.DOTALL,
    )


def without_structured_data(document: str) -> str:
    """Remove generated indexes; the remaining Markdown is the lossless source."""
    return re.sub(r"(?m)^```yaml\n(?:ports|parameters):(?:.|\n)*?^```\n\n?", "", document)


def structure_block_document(document: str) -> str:
    """Insert deterministic YAML indexes while preserving every source line."""
    result = document
    for kind, names in _SECTION_NAMES.items():
        match = _section_span(result, names)
        if not match:
            chinese = "language: zh-CN" in result
            display_name = names[1] if chinese else names[0]
            missing = "R2025b 官方文档未提供。" if chinese else "Not documented in R2025b."
            result = result.rstrip() + (
                f"\n\n## {display_name}\n\n```yaml\n{kind}: []\n```\n\n{missing}\n"
            )
            continue
        original_content = without_structured_data(match.group(1))
        records = _record_data(kind, original_content)
        payload = yaml.safe_dump(
            {kind: records},
            allow_unicode=True,
            sort_keys=False,
            width=120,
        ).rstrip()
        knowledge = original_content.strip()
        if not knowledge:
            chinese = "language: zh-CN" in result
            knowledge = "R2025b 官方文档未提供。" if chinese else "Not documented in R2025b."
        content = f"```yaml\n{payload}\n```\n\n{knowledge}\n"
        result = result[: match.start(1)] + content + result[match.end(1) :]
    return result


def structured_data(document: str, kind: str) -> list[dict[str, Any]]:
    """Return the typed port or parameter records from a block document."""
    if kind not in _SECTION_NAMES:
        raise ValueError(f"Unknown block data kind: {kind}")
    match = _section_span(document, _SECTION_NAMES[kind])
    if not match:
        return []
    blocks = re.findall(r"^```yaml\n(.*?)^```", match.group(1), re.MULTILINE | re.DOTALL)
    if len(blocks) != 1:
        raise ValueError(f"Expected one {kind} YAML block, found {len(blocks)}")
    payload = yaml.safe_load(blocks[0])
    if not isinstance(payload, dict) or set(payload) != {kind}:
        raise ValueError(f"Malformed {kind} YAML block")
    records = payload[kind]
    if not isinstance(records, list) or not all(isinstance(item, dict) for item in records):
        raise ValueError(f"{kind} must be a list of mappings")
    return records


def validate_structured_document(document: str) -> None:
    """Check that both indexes are parseable and exactly match the Markdown."""
    for kind, names in _SECTION_NAMES.items():
        match = _section_span(document, names)
        if not match:
            raise ValueError(f"Missing {kind} section")
        records = structured_data(document, kind)
        expected = _record_data(kind, without_structured_data(match.group(1)))
        if records != expected:
            raise ValueError(f"Stale or incomplete {kind} YAML index")
