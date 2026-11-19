# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Explicit parser coverage for unsupported or non-local SLX content."""

from __future__ import annotations

import zipfile
from pathlib import Path

from openviking.parse.parsers.matlab.catalog import find_block, find_block_reference
from openviking.parse.parsers.matlab.slx import System


def _flatten(system: System):
    yield system
    for child in system.children:
        yield from _flatten(child)


def _one_line(value: str) -> str:
    """SLX wraps long SourceBlock values; keep the identifier on one line."""
    return " ".join(value.split())


def render_coverage(path: str | Path, model: System) -> str:
    path = Path(path)
    systems = list(_flatten(model))
    source_blocks = {
        _one_line(block.source_block): (
            block.block_type,
            find_block_reference(block.block_type, _one_line(block.source_block)),
        )
        for system in systems
        for block in system.blocks
        if block.source_block
    }
    standard = sorted(
        name for name, (_, match) in source_blocks.items() if match and match.full_document
    )
    metadata_only = sorted(
        name for name, (_, match) in source_blocks.items() if match and not match.full_document
    )
    external = sorted(name for name, (_, match) in source_blocks.items() if not match)
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
    stateflow = sorted(
        n for n in names if n.startswith("simulink/stateflow/chart_") and n.endswith(".xml")
    )
    workspaces = sorted(n for n in names if n.endswith(".mxarray"))
    lines = [
        "---",
        "type: simulink-parser-coverage",
        "---",
        "",
        f"# {path.stem} 解析覆盖清单",
        "",
        f"- 已展开本地子系统：**{len(systems)}**",
        f"- 已解析块：**{sum(len(system.blocks) for system in systems)}**",
        f"- 已解析含分支连线：**{sum(len(system.edges) for system in systems)}**",
        f"- 守恒网络连线：**{sum(edge.kind == 'physical-conserving' for system in systems for edge in system.edges)}**（无向，不解释为输入输出）",
        f"- 物理守恒端口：**{sum(len(system.physical_ports) for system in systems)}**",
        f"- 子系统类型：{', '.join(sorted({kind for system in systems for kind in system.subsystem_types}))}",
        "",
        "## 标准库引用",
        "",
    ]
    lines.extend(
        f"- `{name}`：已匹配本地 R2025b 完整块文档 `{find_block(block_type, name)}`；实例参数保留在子系统页。"
        for name, (block_type, match) in sorted(source_blocks.items())
        if match and match.full_document
    )
    if not standard:
        lines.append("无。")
    lines.extend(["", "## 仅匹配官方目录元数据", ""])
    lines.extend(
        f"- `{name}`：产品 `{match.product_name}`，目录 `{' / '.join(match.library_path)}`；完整中英文正文待补，未伪造端口和参数。"
        for name, (_, match) in sorted(source_blocks.items())
        if match and not match.full_document
    )
    if not metadata_only:
        lines.append("无。")
    lines.extend(["", "## 未展开的外部库引用", ""])
    lines.extend(f"- `{name}`：保留库路径和实例参数，本地无其实现 XML。" for name in external)
    if not external:
        lines.append("无。")
    lines.extend(["", "## Stateflow", ""])
    lines.extend(
        f"- `{name}`：已展开到对应子系统的 `stateflow/chart_<chart-id>.json`，包含状态层级、动作原文和转移；不执行事件调度。"
        for name in stateflow
    )
    if not stateflow:
        lines.append("未发现 Stateflow chart XML。")
    lines.extend(["", "## MATLAB 二进制工作区数据", ""])
    lines.extend(f"- `{name}`：已发现，未将其当作信号逻辑执行或反序列化。" for name in workspaces)
    if not workspaces:
        lines.append("无。")
    lines.extend(
        [
            "",
            "## Compile 约束",
            "",
            "引用本模型时必须同时检查对应子系统的 `main.json` 或叶子系统 JSON。上述未展开项是明确的未知边界，不得根据块名补写实现，也不得声称模型已完成动态仿真验证。",
            "",
        ]
    )
    return "\n".join(lines)


def coverage_json(path: str | Path, model: System) -> dict:
    """Return the same coverage facts as ``render_coverage`` as a JSON object."""
    path = Path(path)
    systems = list(_flatten(model))
    source_blocks = {
        _one_line(block.source_block): block.block_type
        for system in systems
        for block in system.blocks
        if block.source_block
    }
    standard = []
    metadata_only = []
    external = []
    for name, block_type in sorted(source_blocks.items()):
        match = find_block_reference(block_type, name)
        if match and match.full_document:
            standard.append(name)
        elif match:
            metadata_only.append(name)
        else:
            external.append(name)
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
    stateflow = sorted(
        n for n in names if n.startswith("simulink/stateflow/chart_") and n.endswith(".xml")
    )
    workspaces = sorted(n for n in names if n.endswith(".mxarray"))
    return {
        "schema": "ov.matlab.simulink-coverage/1",
        "model": path.stem,
        "systems": len(systems),
        "blocks": sum(len(system.blocks) for system in systems),
        "edges": sum(len(system.edges) for system in systems),
        "conserving_edges": sum(
            edge.kind == "physical-conserving" for system in systems for edge in system.edges
        ),
        "physical_ports": sum(len(system.physical_ports) for system in systems),
        "subsystem_types": sorted({kind for system in systems for kind in system.subsystem_types}),
        "standard_library_references": standard,
        "metadata_only_references": metadata_only,
        "external_library_references": external,
        "stateflow_charts": stateflow,
        "workspace_data": workspaces,
        "boundary": "Unresolved external library content is not inferred from block names.",
    }
