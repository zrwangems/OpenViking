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
    # Mermaid treats a literal ``\\n`` as label text and HTML ``<br>`` labels
    # currently break Studio's strict SVG/XML parser. Keep generated labels
    # single-line and escape the edge-label delimiter.
    return (
        value.replace('"', "'")
        .replace("\\n", " ")
        .replace("\n", " ")
        .replace("\r", "")
        .replace("|", "&#124;")
        .replace("(", "&#40;")
        .replace(")", "&#41;")
    )


def _child_directory(system: System) -> str:
    siblings = system.parent.children if system.parent else []
    duplicates = sum(_slug(s.name) == _slug(system.name) for s in siblings)
    suffix = f"_{system.ref.removeprefix('system_')}" if duplicates > 1 else ""
    return _slug(system.name) + suffix


def system_documents(model: System, language: str = "en") -> dict[str, str]:
    """Return compact system pages with directories only for nested systems.

    The model root and systems with children use ``main.md``. A leaf system is
    one sibling Markdown file, for example ``xCU/xCU_Output.md``.
    """
    del language  # Model identifiers and values are never localized.
    documents: dict[str, str] = {}

    def visit(system: System, directory: str, is_root: bool = False) -> None:
        if is_root:
            path = "main.md"
        elif system.children:
            path = f"{directory}/main.md"
        else:
            path = f"{directory}.md"
        documents[path] = _render_system(system, is_root)
        for child in system.children:
            child_dir = (
                f"{directory}/{_child_directory(child)}" if directory else _child_directory(child)
            )
            visit(child, child_dir)

    visit(model, "", True)
    return documents


def _render_system(system: System, is_root: bool) -> str:
    """Render the graph, model contract, and every block's parameters."""
    blocks = {block.sid: block for block in system.blocks}
    lines = [
        "---",
        f"type: {'simulink-model' if is_root else 'simulink-subsystem'}",
        f"system_ref: {system.ref}",
        f"subsystem_types: [{', '.join(system.subsystem_types)}]",
        "---",
        "",
        f"# {system.name}",
        "",
        "## 逻辑流程图",
        "",
        "```mermaid",
        "flowchart LR",
    ]
    for block in system.blocks:
        node = f"b{_slug(block.sid)}"
        shape_left, shape_right = (
            ("([", "])") if block.block_type in {"Inport", "Outport"} else ("[", "]")
        )
        label = f"{block.name} / {block.block_type}"
        lines.append(f'  {node}{shape_left}"{_mermaid_text(label)}"{shape_right}')
    unresolved: dict[str, str] = {}
    for edge in system.edges:
        source_sid, source_port = _endpoint(edge.source)
        destination_sid, destination_port = _endpoint(edge.destination)
        for sid, endpoint in ((source_sid, edge.source), (destination_sid, edge.destination)):
            if sid not in blocks:
                unresolved.setdefault(sid, endpoint)
    for sid, endpoint in unresolved.items():
        lines.append(f'  b{_slug(sid)}["未解析端点 / {_mermaid_text(endpoint)}"]')
    for edge in system.edges:
        source_sid, source_port = _endpoint(edge.source)
        destination_sid, destination_port = _endpoint(edge.destination)
        if edge.kind == "physical-conserving":
            label = edge.name or (
                f"未命名守恒连接 · {_endpoint_kind(edge.source)}:{source_port} ↔ "
                f"{_endpoint_kind(edge.destination)}:{destination_port}"
            )
            lines.append(
                f"  b{_slug(source_sid)} ---|{_mermaid_text(label)}| b{_slug(destination_sid)}"
            )
        else:
            label = edge.name or f"未命名信号 · out:{source_port} → in:{destination_port}"
            lines.append(
                f"  b{_slug(source_sid)} -->|{_mermaid_text(label)}| b{_slug(destination_sid)}"
            )
    lines.extend(
        [
            "```",
            "",
            "## 模型说明",
            "",
            f"该层包含 {len(system.blocks)} 个块和 {len(system.edges)} 条连接。"
            "有向信号与无向守恒连接均按 SLX 连线绘制。",
            "",
            "| 接口类别 | 端口 | 名称 | SID |",
            "| --- | --- | --- | --- |",
        ]
    )
    for category, ports in (
        ("输入", system.inputs),
        ("输出", system.outputs),
        ("守恒端口（双向）", system.physical_ports),
        ("执行控制", system.control_ports),
    ):
        for port in ports:
            lines.append(
                f"| {category} | {_cell(port.parameters.get('Port', '1'))} "
                f"| {_cell(port.name)} | {port.sid} |"
            )
    for edge in system.edges:
        if edge.kind != "physical-conserving":
            continue
        source_sid, source_port = _endpoint(edge.source)
        destination_sid, destination_port = _endpoint(edge.destination)
        source_name = blocks[source_sid].name if source_sid in blocks else edge.source
        destination_name = (
            blocks[destination_sid].name if destination_sid in blocks else edge.destination
        )
        lines.append(
            f"| 守恒连接（双向） | {_cell(source_port)} ↔ {_cell(destination_port)} "
            f"| {_cell(edge.name or '未命名')}：{_cell(source_name)} ↔ {_cell(destination_name)} "
            f"| {_cell(source_sid)} ↔ {_cell(destination_sid)} |"
        )
    if not any(
        (
            system.inputs,
            system.outputs,
            system.physical_ports,
            system.control_ports,
            any(edge.kind == "physical-conserving" for edge in system.edges),
        )
    ):
        lines.append("| - | - | 无显式接口端口 | - |")
    lines.extend(
        [
            "",
            f"执行语义：`{', '.join(system.subsystem_types)}`。"
            "具体调度由 Simulink 求解器、采样时间和控制端口共同决定，流程图布局不表示执行顺序。",
            "",
            "模型目的：源模型未提供显式用途说明，不从块名推断工程目的。",
            "",
            "## 块参数",
            "",
            "| 块 | 类型 | SID | 参数 |",
            "| --- | --- | --- | --- |",
        ]
    )
    children = {child.owner.sid: child for child in system.children if child.owner}
    rows = 0
    if system.owner:
        owner_params = _display_parameters(system.owner)
        if owner_params:
            param_text = "<br>".join(
                f"`{_cell(key)}` = `{_cell(value)}`" for key, value in sorted(owner_params.items())
            )
            lines.append(
                f"| 当前子系统 / {_cell(system.owner.name)} | {system.owner.block_type} "
                f"| {system.owner.sid} | {param_text} |"
            )
            rows += 1
    for block in system.blocks:
        child = children.get(block.sid)
        if child:
            child_path = f"{_child_directory(child)}/{'main.md' if child.children else ''}"
            if not child.children:
                child_path = f"{_child_directory(child)}.md"
            name = f"[{_cell(block.name)}]({child_path})"
        else:
            name = _cell(block.name)
        params = _display_parameters(block)
        if block.block_type in {"ConnectionPort", "PMIOPort"}:
            params = {**params, "Direction": "bidirectional / conserving"}
        param_text = "<br>".join(
            f"`{_cell(key)}` = `{_cell(value)}`" for key, value in sorted(params.items())
        )
        source = block.block_type + (
            f" / `{_cell(block.source_block)}`" if block.source_block else ""
        )
        lines.append(f"| {name} | {source} | {block.sid} | {param_text or '-'} |")
        rows += 1
    if not rows:
        lines.append("| - | 无内部节点 | - | - |")
    if is_root:
        lines.extend(["", "- [解析覆盖清单](coverage.md)"])
    lines.append("")
    return "\n".join(lines)


def _endpoint(value: str) -> tuple[str, str]:
    match = re.fullmatch(r"(.*)#(?:in|out|[lr]?conn):(.+)", value, flags=re.IGNORECASE)
    return (match.group(1), match.group(2)) if match else (value, "?")


def _endpoint_kind(value: str) -> str:
    match = re.fullmatch(r".*#(in|out|[lr]?conn):.+", value, flags=re.IGNORECASE)
    return match.group(1) if match else "port"
