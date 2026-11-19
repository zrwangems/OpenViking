# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Parse legacy text ``.mdl`` models into the same system tree as ``.slx``."""

from __future__ import annotations

import re
from pathlib import Path

from openviking.parse.parsers.matlab.slx import Block, Edge, System

_TOKEN = re.compile(r'"(?:[^"\\]|\\.)*"|\[[^\]]*\]|[{}]|[^\s{}]+')
_SCALAR_SKIP = {"BlockType", "Name", "SID"}


def _unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        return value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return value


def _parse_entries(tokens: list[str], index: int) -> tuple[list[tuple[str, object]], int]:
    entries: list[tuple[str, object]] = []
    while index < len(tokens) and tokens[index] != "}":
        key = tokens[index]
        index += 1
        if index >= len(tokens):
            break
        if tokens[index] == "{":
            value, index = _parse_entries(tokens, index + 1)
            if index < len(tokens) and tokens[index] == "}":
                index += 1
        else:
            value = _unquote(tokens[index])
            index += 1
        entries.append((key, value))
    return entries, index


def _scalars(entries: list[tuple[str, object]]) -> dict[str, str]:
    return {key: str(value) for key, value in entries if isinstance(value, str)}


def _sections(entries: list[tuple[str, object]], name: str) -> list[list[tuple[str, object]]]:
    return [value for key, value in entries if key == name and isinstance(value, list)]


def _collect_lines(entries: list[tuple[str, object]]) -> list[dict[str, str]]:
    lines: list[dict[str, str]] = []
    for key, value in entries:
        if key == "Line" and isinstance(value, list):
            lines.append(_scalars(value))
            for branch in _sections(value, "Branch"):
                lines.extend(_collect_lines(branch))
        elif key == "Branch" and isinstance(value, list):
            lines.extend(_collect_lines(value))
    return lines


def _parse_system(
    entries: list[tuple[str, object]],
    name: str,
    ref: str,
    owner: Block | None = None,
) -> System:
    system = System(ref=ref, name=name, owner=owner)
    block_entries = [
        (key, value) for key, value in entries if key == "Block" and isinstance(value, list)
    ]
    by_name: dict[str, str] = {}
    for index, (_, block_entry) in enumerate(block_entries, start=1):
        props = _scalars(block_entry)
        block_name = props.get("Name", f"block_{index}")
        sid = props.get("SID") or f"mdl_{ref}_{index}"
        block = Block(
            sid=sid,
            name=block_name,
            block_type=props.get("BlockType", ""),
            parameters={key: value for key, value in props.items() if key not in _SCALAR_SKIP},
            source_block=props.get("SourceBlock", "") or props.get("ReferenceBlock", ""),
        )
        system.blocks.append(block)
        by_name.setdefault(block_name, sid)
        nested = _sections(block_entry, "System")
        if nested:
            child = _parse_system(
                nested[0],
                name=f"{block_name}",
                ref=f"{ref}_{index}",
                owner=block,
            )
            system.children.append(child)
        if block.block_type == "SubSystem" and not nested:
            # A subsystem block without a System section is an external or
            # unexpanded reference; keep it in the coverage boundary.
            pass

    for line in _collect_lines(entries):
        source = line.get("SrcBlock", "")
        destination = line.get("DstBlock", "")
        if not source or not destination:
            continue
        source_sid = by_name.get(source, f"name_{source}")
        destination_sid = by_name.get(destination, f"name_{destination}")
        system.edges.append(
            Edge(
                source=f"{source_sid}#out:{line.get('SrcPort', '1')}",
                destination=f"{destination_sid}#in:{line.get('DstPort', '1')}",
                name=line.get("Name", ""),
                kind="physical-conserving"
                if line.get("LineType", "").casefold() == "connection"
                else "signal",
            )
        )
    return system


def parse_mdl(path: str | Path) -> System:
    """Read a text MDL model and return its system tree."""
    path = Path(path)
    text = path.read_text(encoding="utf-8", errors="replace")
    tokens = _TOKEN.findall(text)
    entries, _ = _parse_entries(tokens, 0)
    model_name = path.stem
    model_entries = entries
    for key, value in entries:
        if key in {"Model", "Library"} and isinstance(value, list):
            model_entries = value
            model_name = _scalars(value).get("Name", model_name)
            break
    systems = _sections(model_entries, "System")
    if not systems:
        return System(ref="mdl_root", name=model_name)
    return _parse_system(systems[0], name=model_name, ref="mdl_root")
