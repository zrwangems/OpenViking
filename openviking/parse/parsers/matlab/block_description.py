# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Deterministic block descriptions for Simulink system JSON.

The description is rendered from :mod:`block_templates`.  Values are taken from
the block parameters already read from the SLX/MDL file, so the same input
always produces the same output and no language model is involved.
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any

from openviking.parse.parsers.matlab.block_templates import GENERIC, TEMPLATES, BlockTemplate

if TYPE_CHECKING:  # pragma: no cover - imported only for type checkers
    from openviking.parse.parsers.matlab.slx import Block

# Presentation-only parameters that say nothing about what a block computes.
_UI_PARAMETERS = {
    "Position",
    "ZOrder",
    "ShowName",
    "HideAutomaticName",
    "FontSize",
    "FontName",
    "FontWeight",
    "FontAngle",
    "ForegroundColor",
    "BackgroundColor",
    "DropShadow",
    "NameLocation",
    "NamePlacement",
    "IconDisplay",
    "PortRotation",
    "BlockRotation",
    "BlockMirror",
    "LibraryVersion",
    "RTWMemSecFuncInitTerm",
    "RTWMemSecFuncExecute",
    "RTWMemSecDataParameters",
    "RTWMemSecDataConstants",
    "RTWMemSecDataInternal",
    "ContentPreviewEnabled",
    "RefBlkName",
    "VectorParamsAs1DForOutWhenUnconnected",
}

# These are represented by dedicated template fields or appended as a note.
_NON_CONFIGURATION = {"SourceBlock", "ReferenceBlock", "Description"}

_CONFIG_LIMIT = 12
_CONFIG_VALUE_LIMIT = 80
_CONFIG_TEXT_LIMIT = 900
_VALUE_LIMIT = 160


def _collapse(value: Any) -> str:
    """Make one XML/MDL value safe for a single-line sentence."""
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text


def _clip(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: max(0, limit - 1)].rstrip() + "…"


def display_parameters(parameters: dict[str, str]) -> dict[str, str]:
    """Return parameters that describe behaviour, not layout."""
    return {
        key: value
        for key, value in parameters.items()
        if key not in _UI_PARAMETERS and not key.startswith("SID")
    }


def _config_items(parameters: dict[str, str]) -> list[tuple[str, str]]:
    return [
        (key, _collapse(value))
        for key, value in display_parameters(parameters).items()
        if key not in _NON_CONFIGURATION and _collapse(value)
    ]


def _config_summary(items: list[tuple[str, str]], language: str) -> str:
    if not items:
        return "无额外配置" if language.startswith("zh") else "no extra configuration"
    shown = []
    for key, value in items[:_CONFIG_LIMIT]:
        shown.append(f"{key}={_clip(value, _CONFIG_VALUE_LIMIT)}")
    text = "，".join(shown) if language.startswith("zh") else ", ".join(shown)
    remaining = len(items) - len(shown)
    if remaining:
        text += f"，另有 {remaining} 项" if language.startswith("zh") else f", {remaining} more"
    return _clip(text, _CONFIG_TEXT_LIMIT)


def _source_block(block: "Block", language: str) -> str:
    explicit = block.source_block or block.parameters.get("SourceBlock", "")
    if explicit:
        return _collapse(explicit)
    if block.block_type and block.block_type not in {
        "SubSystem",
        "Reference",
        "ModelReference",
        "Unknown",
    }:
        return f"built-in/{block.block_type}"
    return "未指定库来源" if language.startswith("zh") else "unspecified"


class _Values(dict):
    def __init__(self, values: dict[str, Any], language: str) -> None:
        super().__init__(values)
        self._missing = "默认" if language.startswith("zh") else "default"

    def __missing__(self, key: str) -> str:
        return self._missing


def template_for(block_type: str) -> BlockTemplate:
    """Return the template used for a block type (never ``None``)."""
    return TEMPLATES.get(block_type, GENERIC)


def describe_block(block: "Block", language: str = "en") -> str:
    """Render one block description from its template and own parameters."""
    zh = str(language).lower().startswith("zh")
    template = template_for(block.block_type)
    items = _config_items(block.parameters)
    values: dict[str, Any] = {
        key: _clip(_collapse(value), _VALUE_LIMIT)
        for key, value in display_parameters(block.parameters).items()
    }
    values.setdefault("Port", "1")
    values.update(
        {
            "name": _collapse(block.name),
            "block_type": block.block_type or "Unknown",
            "source_block": _source_block(block, "zh" if zh else "en"),
            "config": _config_summary(items, "zh" if zh else "en"),
            "param_count": len(items),
        }
    )
    text = (template.zh if zh else template.en).format_map(_Values(values, "zh" if zh else "en"))
    note = _clip(_collapse(block.parameters.get("Description")), 300)
    if note:
        text += f" 模型内块描述：{note}" if zh else f" Model block description: {note}"
    return text
