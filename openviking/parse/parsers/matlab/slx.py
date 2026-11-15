# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read Simulink SLX system XML without requiring a MATLAB installation."""

from __future__ import annotations

import re
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member
from openviking.parse.parsers.matlab.catalog import find_block
from openviking.parse.parsers.matlab.templates import render_block_template


@dataclass
class Block:
    sid: str
    name: str
    block_type: str
    parameters: dict[str, str] = field(default_factory=dict)
    source_block: str = ""
    system_ref: str = ""


@dataclass
class Edge:
    source: str
    destination: str
    name: str = ""
    kind: str = "signal"


@dataclass
class System:
    ref: str
    name: str
    blocks: list[Block] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)
    children: list["System"] = field(default_factory=list)
    parent: "System | None" = field(default=None, repr=False)
    parameters: dict[str, str] = field(default_factory=dict)
    owner: Block | None = field(default=None, repr=False)

    @property
    def subsystem_types(self) -> list[str]:
        """Classify execution semantics from actual SLX blocks and parameters."""
        types: list[str] = []
        by_type = {block.block_type: block for block in self.blocks}
        owner_parameters = self.owner.parameters if self.owner else {}
        if (
            self.block_type in {"VariantSubSystem", "VariantAssemblySubSystem"}
            or owner_parameters.get("Variant") == "on"
        ):
            types.append(
                "variant-assembly"
                if "Assembly" in self.block_type or "VariantAssemblyType" in owner_parameters
                else "variant"
            )
        if "Configurable Subsystem" in owner_parameters.get("SourceBlock", ""):
            types.append("configurable")
        if "EnablePort" in by_type:
            types.append("enabled")
        trigger = by_type.get("TriggerPort")
        if trigger:
            if trigger.parameters.get("TriggerType") == "function-call":
                types.append("function-call")
            else:
                types.append("triggered")
        if "ActionPort" in by_type:
            types.append("action")
        for block_type, name in (
            ("ForEach", "for-each"),
            ("ForIterator", "for-iterator"),
            ("WhileIterator", "while-iterator"),
            ("ResetPort", "resettable"),
            ("MessageTrigger", "message-triggered"),
        ):
            if block_type in by_type:
                types.append(name)
        listener = by_type.get("EventListener")
        if listener:
            event = listener.parameters.get("EventType", "event").lower().replace(" ", "-")
            types.append(f"event-function:{event}")
        if not types:
            types.append("subsystem")
        if owner_parameters.get("TreatAsAtomicUnit") == "on":
            types.append("atomic")
        if owner_parameters.get("Mask") == "on":
            types.append("masked")
        if owner_parameters.get("SourceBlock"):
            types.append("library-linked")
        return types

    @property
    def block_type(self) -> str:
        return self.owner.block_type if self.owner else "SubSystem"

    @property
    def physical_ports(self) -> list[Block]:
        return _ports(self.blocks, "ConnectionPort", "PMIOPort")

    @property
    def inputs(self) -> list[Block]:
        return _ports(self.blocks, "Inport")

    @property
    def outputs(self) -> list[Block]:
        return _ports(self.blocks, "Outport")

    @property
    def control_ports(self) -> list[Block]:
        return _ports(
            self.blocks,
            "EnablePort",
            "TriggerPort",
            "ActionPort",
            "ResetPort",
            "ForEach",
            "ForIterator",
            "WhileIterator",
            "MessageTrigger",
            "EventListener",
        )


def _ports(blocks: Iterable[Block], *kinds: str) -> list[Block]:
    def number(block: Block) -> tuple[int, str]:
        try:
            return int(block.parameters.get("Port", "1")), block.name
        except ValueError:
            return 1, block.name

    return sorted((b for b in blocks if b.block_type in kinds), key=number)


def parse_slx(path: str | Path) -> System:
    """Parse the complete subsystem hierarchy and connectivity from an SLX file."""
    path = Path(path)
    try:
        archive = zipfile.ZipFile(path)
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Not a valid SLX archive: {path.name}") from exc

    with archive:
        root_xml = _archive_xml(archive, "simulink/blockdiagram.xml")
        model = root_xml.find("./Model")
        root_ref_element = model.find("./System") if model is not None else None
        if root_ref_element is None:
            raise ValueError(f"SLX archive has no model root System: {path.name}")
        root_ref = root_ref_element.get("Ref", "")
        if not root_ref:
            raise ValueError(f"SLX model root System has no Ref: {path.name}")
        systems: dict[str, System] = {}
        pending: list[tuple[System, Block]] = []

        def read_system(
            ref: str, name: str, parent: System | None, owner: Block | None = None
        ) -> System:
            member = f"simulink/systems/{ref}.xml"
            element = _archive_xml(archive, member)
            system = System(ref=ref, name=name, parent=parent, owner=owner)
            systems[ref] = system
            for prop in element.findall("./P"):
                key = prop.get("Name")
                if key:
                    system.parameters[key] = prop.text or ""
            for node in element.findall("./Block"):
                sid = node.get("SID", "")
                block = Block(
                    sid=sid,
                    name=node.get("Name", sid or "Unnamed"),
                    block_type=node.get("BlockType", "Unknown"),
                )
                for prop in node.findall("./P"):
                    key = prop.get("Name")
                    if key:
                        block.parameters[key] = prop.text or ""
                instance = node.find("./InstanceData")
                if instance is not None:
                    for prop in instance.findall("./P"):
                        key = prop.get("Name")
                        if key:
                            block.parameters[key] = prop.text or ""
                block.source_block = block.parameters.get("SourceBlock", "")
                child_ref = node.find("./System")
                if child_ref is not None:
                    block.system_ref = child_ref.get("Ref", "")
                system.blocks.append(block)
                if block.system_ref:
                    pending.append((system, block))
            for line in element.findall("./Line"):
                _read_line(line, system.edges)
            return system

        root = read_system(root_ref, path.stem, None)
        for parent, block in pending:
            # A system can only be referenced once in the XML hierarchy. Preserve
            # unresolved references as blocks instead of silently dropping them.
            if block.system_ref in systems:
                continue
            child = read_system(block.system_ref, block.name, parent, block)
            parent.children.append(child)
        return root


def _archive_xml(archive: zipfile.ZipFile, name: str):
    try:
        return ET.fromstring(read_xml_member(archive, name))
    except KeyError as exc:
        raise ValueError(f"SLX archive is missing {name}") from exc


def _read_line(
    line, edges: list[Edge], inherited_source: str = "", inherited_name: str = ""
) -> None:
    props = {p.get("Name"): p.text or "" for p in line.findall("./P")}
    source = props.get("Src", inherited_source)
    name = props.get("Name", inherited_name)
    destination = props.get("Dst", "")
    if source and destination:
        kind = (
            "physical-conserving"
            if "conn:" in source.lower() or "conn:" in destination.lower()
            else "signal"
        )
        edges.append(Edge(source=source, destination=destination, name=name, kind=kind))
    for branch in line.findall("./Branch"):
        _read_line(branch, edges, source, name)


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
_SIMPLE_BLOCKS = {
    "Add",
    "Sum",
    "Or",
    "And",
    "Logic",
    "RelationalOperator",
    "Product",
    "Gain",
    "BusCreator",
    "BusSelector",
    "Mux",
    "Demux",
    "Terminator",
    "Ground",
}


def _display_parameters(block: Block) -> dict[str, str]:
    return {
        k: v
        for k, v in block.parameters.items()
        if k not in _UI_PARAMETERS and not k.startswith("SID")
    }


def _cell(value: str) -> str:
    return (value or " ").replace("|", "\\|").replace("\r", "").replace("\n", "<br>")


def _slug(value: str) -> str:
    value = re.sub(r"[^\w.-]+", "_", value, flags=re.UNICODE).strip("._")
    return value or "subsystem"


def _mermaid_text(value: str) -> str:
    return value.replace('"', "'").replace("\n", " ").replace("\r", "")


def _system_path(system: System) -> str:
    names: list[str] = []
    current = system.parent
    while current is not None:
        names.append(_slug(current.name))
        current = current.parent
    return "/".join(reversed(names))


def _child_directory(system: System) -> str:
    siblings = system.parent.children if system.parent else []
    duplicates = sum(_slug(s.name) == _slug(system.name) for s in siblings)
    suffix = f"_{system.ref.removeprefix('system_')}" if duplicates > 1 else ""
    return _slug(system.name) + suffix


def system_documents(model: System) -> dict[str, str]:
    """Return nested ``subsystem/index.md`` documents for a parsed model."""
    documents: dict[str, str] = {}
    paths: list[tuple[System, str]] = []

    def visit(system: System, directory: str, is_root: bool = False) -> None:
        path = "index.md" if is_root else f"{directory}/index.md"
        paths.append((system, path))
        documents[path] = _render_system(system, directory, is_root)
        for child in system.children:
            child_dir = (
                f"{directory}/{_child_directory(child)}" if directory else _child_directory(child)
            )
            visit(child, child_dir)

    visit(model, "", True)
    types = sorted({kind for system, _ in paths for kind in system.subsystem_types})
    index = ["", "## 全模型子系统类型索引", "", "| 类型 | 子系统 |", "| --- | --- |"]
    for kind in types:
        members = [
            f"[{system.name}]({path})" for system, path in paths if kind in system.subsystem_types
        ]
        index.append(f"| `{kind}` | {'；'.join(members)} |")
    documents["index.md"] += "\n".join(index) + "\n"
    return documents


def _render_system(system: System, directory: str, is_root: bool) -> str:
    blocks = {b.sid: b for b in system.blocks}
    lines = [
        "---",
        "type: simulink-subsystem",
        f"system_ref: {system.ref}",
        f"subsystem_types: [{', '.join(system.subsystem_types)}]",
        "---",
        "",
        f"# {system.name}",
        "",
        f"源文件系统 ID：`{system.ref}`。本页由 SLX XML 确定性生成，不执行模型，也不推断未在文件中出现的动态语义。",
        "",
        "## 子系统类型与执行控制",
        "",
        "类型：" + "、".join(f"`{kind}`" for kind in system.subsystem_types) + "。",
        "",
        "| 控制块 | 类型 | SID | 参数 |",
        "| --- | --- | --- | --- |",
    ]
    for block in system.control_ports:
        params = "<br>".join(
            f"`{_cell(key)}` = `{_cell(value)}`"
            for key, value in sorted(_display_parameters(block).items())
        )
        lines.append(
            f"| {_cell(block.name)} | {block.block_type} | {block.sid} | {params or '-'} |"
        )
    if not system.control_ports:
        lines.append("| - | 无显式执行控制块 | - | - |")
    if "variant" in system.subsystem_types and system.owner:
        lines.extend(
            [
                "",
                "可变子系统配置："
                + "；".join(
                    f"`{key}` = `{value}`"
                    for key, value in sorted(system.owner.parameters.items())
                    if key.startswith("Variant") or key in {"LabelModeActiveChoice", "EmptyChoice"}
                ),
            ]
        )
    lines.extend(
        [
            "",
            "## 输入",
            "",
            "| 端口 | 信号 | 源块 SID |",
            "| --- | --- | --- |",
        ]
    )
    for port in system.inputs:
        lines.append(f"| {port.parameters.get('Port', '1')} | {_cell(port.name)} | {port.sid} |")
    if not system.inputs:
        lines.append("| - | 无显式 Inport | - |")
    lines.extend(["", "## 输出", "", "| 端口 | 信号 | 目标块 SID |", "| --- | --- | --- |"])
    for port in system.outputs:
        lines.append(f"| {port.parameters.get('Port', '1')} | {_cell(port.name)} | {port.sid} |")
    if not system.outputs:
        lines.append("| - | 无显式 Outport | - |")

    lines.extend(
        [
            "",
            "## 物理端口与物理信号端口",
            "",
            "`ConnectionPort` 与 Simscape 子系统的 `PMIOPort` 都是守恒网络节点，不分输入输出。网络域只采用 XML 明示值，未知时不根据端口左右位置猜测。Simscape 有向物理信号由 SSC 的 inputs / outputs 表达。",
            "",
            "| 名称 | 端口类型 | 方向 / 位置 | 网络域 | SID |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for port in system.physical_ports:
        direction = port.parameters.get("Side", "bidirectional / conserving")
        kind = "conserving"
        domain = port.parameters.get("Domain") or port.parameters.get("PortDomain") or "未声明"
        lines.append(
            f"| {_cell(port.name)} | {kind} | {_cell(direction)} | {_cell(domain)} | {port.sid} |"
        )
    if not system.physical_ports:
        lines.append("| - | 无显式物理端口 | - | - | - |")

    dependency_blocks = [
        block
        for block in system.blocks
        if block.block_type
        in {"ModelReference", "Reference", "S-Function", "MATLABSystem", "SimscapeComponentBlock"}
        or block.source_block
    ]
    if dependency_blocks:
        lines.extend(
            ["", "## 模型引用与外部依赖", "", "| 块 | 类型 | 引用 / 实现 |", "| --- | --- | --- |"]
        )
        for block in dependency_blocks:
            reference = (
                block.parameters.get("ModelName")
                or block.source_block
                or block.parameters.get("FunctionName")
                or block.parameters.get("SystemName")
                or "未声明"
            )
            lines.append(f"| {_cell(block.name)} | {block.block_type} | `{_cell(reference)}` |")

    lines.extend(["", "## 子系统", ""])
    if is_root:
        lines.append("- [解析覆盖清单](coverage.md)：Stateflow、外部库和二进制工作区边界")
    if system.children:
        for child in system.children:
            kinds = ", ".join(child.subsystem_types)
            variant = ""
            if child.owner and "variant" in system.subsystem_types:
                variant = child.owner.parameters.get("VariantControl", "")
            lines.append(
                f"- [{child.name}]({_child_directory(child)}/index.md) (`{child.ref}`; `{kinds}`"
                + (f"; VariantControl=`{_cell(variant)}`" if variant else "")
                + ")"
            )
    else:
        lines.append("无嵌套子系统。")

    lines.extend(
        [
            "",
            "## 可配置块",
            "",
            "仅列出带业务参数的块及引用块；Add、And、Or 等简单运算的连接关系保留在流程图中。",
            "",
            "| 块 | 类型 / 库来源 | SID | 参数 |",
            "| --- | --- | --- | --- |",
        ]
    )
    rows = 0
    block_templates: dict[str, tuple[str, str]] = {}
    for block in system.blocks:
        if block.block_type in {
            "Inport",
            "Outport",
            "ConnectionPort",
            "PMIOPort",
            "EnablePort",
            "TriggerPort",
            "ActionPort",
            "ResetPort",
        }:
            continue
        params = _display_parameters(block)
        if block.block_type == "SubSystem" and not params:
            continue
        if block.block_type in _SIMPLE_BLOCKS and not params:
            continue
        if not params and not block.source_block and block.block_type in _SIMPLE_BLOCKS:
            continue
        if not params and not block.source_block:
            continue
        param_text = "<br>".join(f"`{_cell(k)}` = `{_cell(v)}`" for k, v in sorted(params.items()))
        source = block.block_type + (
            f" / `{_cell(block.source_block)}`" if block.source_block else ""
        )
        catalog_match = find_block(block.block_type, block.source_block)
        if catalog_match:
            family, canonical = catalog_match
            source += f" / 目录：`{family}/{_cell(canonical)}`"
            rendered_template = render_block_template(block.block_type, block.source_block)
            if rendered_template:
                canonical_name, template_markdown = rendered_template
                block_templates.setdefault(
                    f"{family}/{canonical_name}", (canonical_name, template_markdown)
                )
        lines.append(f"| {_cell(block.name)} | {source} | {block.sid} | {param_text or '-'} |")
        rows += 1
    if not rows:
        lines.append("| - | - | - | 无 |")

    if block_templates:
        lines.extend(
            [
                "",
                "## 块知识模板",
                "",
                "以下内容在资源添加时由原始 `BlockType` / `SourceBlock` 匹配本地 R2025b 模板并内联。"
                "同名块只展开一次，各实例自己的配置仍以上表为准。",
            ]
        )
        for canonical_name, template_markdown in block_templates.values():
            lines.extend(["", f"### {canonical_name}", "", template_markdown, ""])

    lines.extend(["", "## 信号逻辑流程图", "", "```mermaid", "flowchart LR"])
    for block in system.blocks:
        node = f"b{_slug(block.sid)}"
        shape_left, shape_right = (
            ("([", "])") if block.block_type in {"Inport", "Outport"} else ("[", "]")
        )
        label = f"{block.name}\\n{block.block_type}"
        lines.append(f'  {node}{shape_left}"{_mermaid_text(label)}"{shape_right}')
    for edge in system.edges:
        source_sid, source_port = _endpoint(edge.source)
        destination_sid, destination_port = _endpoint(edge.destination)
        if source_sid not in blocks or destination_sid not in blocks:
            continue
        if edge.kind == "physical-conserving":
            label = (
                edge.name
                or f"{_endpoint_kind(edge.source)}:{source_port} ↔ {_endpoint_kind(edge.destination)}:{destination_port}"
            )
            lines.append(
                f"  b{_slug(source_sid)} ---|{_mermaid_text(label)}| b{_slug(destination_sid)}"
            )
        else:
            label = edge.name or f"out:{source_port} → in:{destination_port}"
            lines.append(
                f"  b{_slug(source_sid)} -->|{_mermaid_text(label)}| b{_slug(destination_sid)}"
            )
    lines.extend(
        [
            "```",
            "",
            "## 连接表",
            "",
            "| 信号 / 网络 | 端点 A | 端点 B | 语义 |",
            "| --- | --- | --- | --- |",
        ]
    )
    if system.edges:
        for edge in system.edges:
            source_sid, source_port = _endpoint(edge.source)
            destination_sid, destination_port = _endpoint(edge.destination)
            source = blocks.get(source_sid)
            destination = blocks.get(destination_sid)
            source_kind = "out" if edge.kind == "signal" else _endpoint_kind(edge.source)
            destination_kind = "in" if edge.kind == "signal" else _endpoint_kind(edge.destination)
            semantic = "有向信号" if edge.kind == "signal" else "守恒网络连接（无输入输出方向）"
            lines.append(
                f"| {_cell(edge.name) or '-'} | {_cell(source.name if source else source_sid)} ({source_kind}:{source_port}) "
                f"| {_cell(destination.name if destination else destination_sid)} ({destination_kind}:{destination_port}) | {semantic} |"
            )
    else:
        lines.append("| - | 无显式连线 | - |")
    lines.append("")
    return "\n".join(lines)


def _endpoint(value: str) -> tuple[str, str]:
    match = re.fullmatch(r"(.*)#(?:in|out|[lr]?conn):(.+)", value, flags=re.IGNORECASE)
    return (match.group(1), match.group(2)) if match else (value, "?")


def _endpoint_kind(value: str) -> str:
    match = re.fullmatch(r".*#(in|out|[lr]?conn):.+", value, flags=re.IGNORECASE)
    return match.group(1) if match else "port"
