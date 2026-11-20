# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Load per-block description templates generated from the local block library.

The template catalog lives next to the scraped Markdown in
``openviking-engineering-resources``.  It is generated deterministically from
the official description and parameter YAML, so this module only maps a
Simulink block to its catalog entry and renders the model's own parameter
values into it.  It never calls a language model or the network.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Mapping

SCHEMA = "ov.matlab.block-description-templates/1"
_ASSET_URI = (
    "viking://resources/openviking-engineering-resources/"
    "matlab/{language}/simulink-block-library/templates.json"
)
_CONFIG_LIMIT = 6
_VALUE_LIMIT = 90
_DESCRIPTION_LIMIT = 900

# SLX BlockType -> name used by the official block library.  Duplicate names
# are still disambiguated by product/library path in the scorer.
BLOCK_TYPE_ALIASES = {
    "Add": "Sum",
    "Subtract": "Sum",
    "Sum of Elements": "Sum",
    "Logic": "Logical Operator",
    "RelationalOperator": "Relational Operator",
    "SubSystem": "Subsystem",
    "Inport": "Inport",
    "Outport": "Outport",
    "S-Function": "S-Function",
    "MATLABSystem": "MATLAB System",
    "DataStoreMemory": "Data Store Memory",
    "DataStoreRead": "Data Store Read",
    "DataStoreWrite": "Data Store Write",
    "UnitDelay": "Unit Delay",
    "Lookup_n-D": "n-D Lookup Table",
    "LookupNDDirect": "Direct Lookup Table (n-D)",
    "Math": "Math Function",
    "Signum": "Sign",
    "Saturate": "Saturation",
    "RateTransition": "Rate Transition",
    "UnitConversion": "Unit Conversion",
    "FirstOrderHold": "First Order Hold",
    "TransferFcn": "Transfer Fcn",
    "ModelReference": "Model Reference",
    "ToWorkspace": "To Workspace",
    "TriggerPort": "Trigger",
    "Concatenate": "Vector Concatenate",
    "Stop": "Stop Simulation",
    "Rounding": "Rounding Function",
    "Trigonometry": "Trigonometric Function",
    "DiscreteIntegrator": "Discrete-Time Integrator",
    "Lookup": "Lookup Table Dynamic",
    "InitialCondition": "Initial Condition",
    "ForEach": "For Each Subsystem",
    "LampBlock": "Lamp",
    "SliderBlock": "Slider",
    "RotarySwitchBlock": "Rotary Switch",
    "PushButtonBlock": "Push Button",
    "SimscapeComponentBlock": "Simscape Component",
    "PMIOPort": "Connection Port",
}

_SOURCE_PRODUCT_ALIASES = {
    "simscapefoundationlibrary": "simscape",
    "fllib": "hydro",
    "powerlib": "sps",
    "powersys": "sps",
    "eelib": "sps",
    "smlib": "sm",
}


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def _clip(value: Any, limit: int) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


@dataclass(frozen=True)
class OfficialTemplate:
    key: str
    title: str
    product: str
    category: str
    page: str
    summary: str
    parameters: tuple[tuple[str, str], ...] = field(default_factory=tuple)
    source: str = ""

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any]) -> "OfficialTemplate":
        raw_parameters = payload.get("parameters") or []
        parameters = []
        for item in raw_parameters:
            if not isinstance(item, Mapping):
                continue
            slot = str(item.get("slot") or "").strip()
            if slot:
                parameters.append((slot, str(item.get("label") or slot).strip()))
        return cls(
            key=str(payload.get("key") or ""),
            title=str(payload.get("title") or ""),
            product=str(payload.get("product") or ""),
            category=str(payload.get("category") or ""),
            page=str(payload.get("page") or ""),
            summary=str(payload.get("summary") or "").strip(),
            parameters=tuple(parameters),
            source=str(payload.get("source") or ""),
        )


class OfficialBlockCatalog:
    """In-memory index of ``templates.json`` entries."""

    def __init__(self, templates: Iterable[OfficialTemplate], language: str = "en") -> None:
        self.language = "zh-CN" if str(language).lower().startswith("zh") else "en"
        self.templates = tuple(templates)
        self._index: dict[str, list[OfficialTemplate]] = {}
        for template in self.templates:
            for key in self._keys(template):
                self._index.setdefault(key, []).append(template)

    @classmethod
    def from_dict(cls, payload: Mapping[str, Any], language: str = "en") -> "OfficialBlockCatalog":
        if payload.get("schema") not in {None, SCHEMA}:
            raise ValueError(f"unsupported block template schema: {payload.get('schema')}")
        return cls(
            (OfficialTemplate.from_dict(item) for item in payload.get("templates") or []),
            language=language,
        )

    @classmethod
    def from_text(cls, text: str, language: str = "en") -> "OfficialBlockCatalog":
        return cls.from_dict(json.loads(text), language=language)

    @staticmethod
    def _keys(template: OfficialTemplate) -> set[str]:
        keys = {
            _norm(template.title),
            _norm(template.page),
            _norm(Path(template.source).stem),
            _norm(Path(template.key).name),
        }
        return {key for key in keys if key}

    def _score(
        self, template: OfficialTemplate, block_type: str, source_block: str
    ) -> tuple:
        product = _norm(template.product)
        category = _norm(template.category)
        source_products = {_norm(part) for part in source_block.split("/")[:-1] if part}
        source_products |= {
            _SOURCE_PRODUCT_ALIASES[part]
            for part in source_products
            if part in _SOURCE_PRODUCT_ALIASES
        }
        source_path = {_norm(part) for part in Path(template.source).parts[:-1]}
        alias = _norm(BLOCK_TYPE_ALIASES.get(block_type, block_type))
        return (
            bool(source_products & ({product, category} | source_path)),
            len(source_products & source_path),
            _norm(template.title) == alias,
            product in {"simulink", ""},
            category == "commonlyusedblocks",
            bool(template.parameters),
        )

    def resolve(self, block_type: str, source_block: str = "") -> OfficialTemplate | None:
        candidates = [BLOCK_TYPE_ALIASES.get(block_type, block_type), block_type]
        if source_block:
            candidates.append(source_block.rsplit("/", 1)[-1])
        found: list[OfficialTemplate] = []
        seen: set[str] = set()
        for candidate in candidates:
            for template in self._index.get(_norm(candidate), ()):
                if template.key not in seen:
                    seen.add(template.key)
                    found.append(template)
        if not found:
            return None
        return max(found, key=lambda template: self._score(template, block_type, source_block))

    def render(
        self, template: OfficialTemplate, parameters: Mapping[str, str]
    ) -> str | None:
        zh = self.language.startswith("zh")
        values: list[str] = []
        used: set[str] = set()
        for slot, label in template.parameters:
            for candidate in (part.strip() for part in slot.split("|")):
                if not candidate or candidate in used:
                    continue
                value = parameters.get(candidate)
                if value is None or not str(value).strip():
                    continue
                used.add(candidate)
                text = f"{label} 为 {_clip(value, _VALUE_LIMIT)}" if zh else (
                    f"{label} is {_clip(value, _VALUE_LIMIT)}"
                )
                values.append(text)
                break
            if len(values) >= _CONFIG_LIMIT:
                break
        summary = _clip(template.summary, _DESCRIPTION_LIMIT).rstrip()
        if not summary:
            return None
        if values:
            config = "，".join(values) + "。" if zh else "; ".join(values) + "."
            leads = ("：", ":", "为", "是", "包括", "如下", "以下", "取决于")
            if summary.endswith(leads):
                summary = summary.rstrip("：:") + "：" + config
            else:
                if not summary.endswith(("。", "！", "？", ".", "!", "?")):
                    summary += "。" if zh else "."
                summary += (" 本块配置：" if zh else " Configuration: ") + config
        elif summary.endswith(("：", ":")):
            summary = summary.rstrip("：:") + ("。" if zh else ".")
        return summary

    def describe(self, block: Any, parameters: Mapping[str, str] | None = None) -> str | None:
        template = self.resolve(block.block_type, block.source_block)
        if template is None:
            return None
        return self.render(template, parameters if parameters is not None else block.parameters)


def _candidate_paths(language: str) -> list[Path]:
    language_dir = "zh" if language.startswith("zh") else "en"
    root = os.environ.get("OPENVIKING_MATLAB_BLOCK_LIBRARY")
    candidates: list[Path] = []
    if root:
        base = Path(root).expanduser()
        if base.is_file():
            candidates.append(base)
        else:
            candidates.extend(
                [
                    base / "matlab" / language_dir / "simulink-block-library" / "templates.json",
                    base / language_dir / "simulink-block-library" / "templates.json",
                    base / "simulink-block-library" / "templates.json",
                    base / "templates.json",
                ]
            )
    candidates.append(
        Path(__file__).resolve().parent / "simulink-block-library" / language_dir / "templates.json"
    )
    return candidates


@lru_cache(maxsize=8)
def _load_local_catalog(path: str, language: str) -> OfficialBlockCatalog | None:
    file = Path(path)
    if not file.is_file():
        return None
    try:
        return OfficialBlockCatalog.from_text(file.read_text(encoding="utf-8"), language=language)
    except (OSError, ValueError, json.JSONDecodeError):
        return None


def load_catalog(language: str = "en") -> OfficialBlockCatalog | None:
    """Load from a configured local checkout, if present.

    ``OPENVIKING_MATLAB_BLOCK_LIBRARY`` may point at ``templates.json``, the
    language directory, the ``simulink-block-library`` directory or the
    ``openviking-engineering-resources`` repository root.
    """
    for path in _candidate_paths(language):
        catalog = _load_local_catalog(str(path), language)
        if catalog is not None:
            return catalog
    return None


@lru_cache(maxsize=8)
def _load_uri_catalog(text: str, language: str) -> OfficialBlockCatalog | None:
    try:
        return OfficialBlockCatalog.from_text(text, language=language)
    except (ValueError, json.JSONDecodeError):
        return None


async def load_catalog_for_parse(language: str = "en", viking_fs: Any = None):
    """Load the local catalog, then the imported OpenViking asset, then None."""
    catalog = load_catalog(language)
    if catalog is not None or viking_fs is None:
        return catalog
    language_dir = "zh" if str(language).lower().startswith("zh") else "en"
    uri = _ASSET_URI.format(language=language_dir)
    try:
        text = await viking_fs.read_file(uri)
    except Exception:
        return None
    if not text:
        return None
    return _load_uri_catalog(text, "zh-CN" if language_dir == "zh" else "en")
