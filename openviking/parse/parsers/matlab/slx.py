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


_FLOW_ITEM_LIMIT = 40

_MATH_TEMPLATES = {
    "exp": "e^({0})",
    "log": "ln({0})",
    "log10": "log10({0})",
    "log2": "log2({0})",
    "sqrt": "√({0})",
    "square": "({0})^2",
    "reciprocal": "1 / ({0})",
    "magnitude^2": "|{0}|^2",
    "pow": "{0} ^ {1}",
}


def _code(value: str) -> str:
    """Inline code for one model identifier."""
    cleaned = (value or "").replace("`", "'").replace("\n", " ").replace("\r", "").strip()
    return f"`{cleaned}`"


def _linked(block: Block, child: System | None) -> str:
    if child is None:
        return _code(block.name)
    base = _child_directory(child)
    target = f"{base}/main.md" if child.children else f"{base}.md"
    return f"[{block.name}]({target})"


def _child_port(child: System | None, direction: str, port: str) -> str:
    if child is None:
        return ""
    ports = child.inputs if direction == "in" else child.outputs
    for item in ports:
        if item.parameters.get("Port", "1") == port:
            return item.name
    return ""


def _port_order(ports: Iterable[str]) -> list[str]:
    return sorted(ports, key=lambda port: (0, int(port)) if port.isdigit() else (1, port))


def _unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def _processing_order(system: System) -> list[Block]:
    """Blocks from sources to sinks; cycles keep their declaration order."""
    by_sid = {block.sid: block for block in system.blocks}
    fans_out: dict[str, list[str]] = {}
    waiting = {block.sid: 0 for block in system.blocks}
    for edge in system.edges:
        source, _ = _endpoint(edge.source)
        destination, _ = _endpoint(edge.destination)
        if source not in by_sid or destination not in by_sid:
            continue
        fans_out.setdefault(source, []).append(destination)
        waiting[destination] += 1
    ready = [block.sid for block in system.blocks if waiting[block.sid] == 0]
    ordered: list[Block] = []
    visited: set[str] = set()
    while ready:
        sid = ready.pop(0)
        if sid in visited:
            continue
        visited.add(sid)
        ordered.append(by_sid[sid])
        for destination in fans_out.get(sid, []):
            waiting[destination] -= 1
            if waiting[destination] == 0:
                ready.append(destination)
    ordered.extend(block for block in system.blocks if block.sid not in visited)
    # Read top to bottom: a block is described after the blocks feeding it.
    position = {block.sid: index for index, block in enumerate(system.blocks)}
    depth = {block.sid: 0 for block in system.blocks}
    for block in ordered:
        for edge in system.edges:
            source, _ = _endpoint(edge.source)
            destination, _ = _endpoint(edge.destination)
            if destination == block.sid and source in depth and source != destination:
                depth[block.sid] = max(depth[block.sid], depth[source] + 1)
    return sorted(ordered, key=lambda block: (depth[block.sid], position[block.sid]))


def _source_expression(block: Block) -> str:
    parameters = block.parameters
    if block.block_type == "Constant":
        return f"常量 {_code(parameters.get('Value', '1'))}"
    if block.block_type == "Ground":
        return "常量 0"
    if block.block_type == "From":
        return f"取 {_code(parameters.get('GotoTag', ''))}"
    if block.block_type == "Clock":
        return "仿真时间"
    return ""


def _operation(block: Block, arguments: list[str]) -> str:
    """Describe what one block computes from its input expressions."""
    kind = block.block_type
    parameters = block.parameters
    if kind == "Sum":
        signs = (parameters.get("Inputs") or "++").replace("|", "").replace(" ", "")
        expression = ""
        for index, argument in enumerate(arguments):
            sign = signs[index] if index < len(signs) else "+"
            if index == 0:
                expression = f"−{argument}" if sign == "-" else argument
            else:
                expression += (" − " if sign == "-" else " + ") + argument
        return expression
    if kind == "Product":
        signs = parameters.get("Inputs") or "*"
        expression = arguments[0] if arguments else "?"
        for index, argument in enumerate(arguments[1:], start=1):
            sign = signs[index] if index < len(signs) else "*"
            expression += (" ÷ " if sign == "/" else " × ") + argument
        return expression
    if kind == "Gain":
        gain = parameters.get("Gain", "1")
        return arguments[0] if gain in {"", "1"} else f"{_code(gain)} × {arguments[0]}"
    if kind == "Saturate":
        lower = parameters.get("LowerLimit", "-inf")
        upper = parameters.get("UpperLimit", "inf")
        return f"{arguments[0]} 限制在 [{_code(lower)}, {_code(upper)}]"
    if kind == "Switch":
        criteria = parameters.get("Criteria", "u2 >= Threshold")
        if len(arguments) < 3:
            return f"按 {_code(criteria)} 在输入之间切换（{', '.join(arguments)}）"
        return (
            f"控制量 {arguments[1]}满足 {_code(criteria)} 时取 {arguments[0]}，"
            f"否则取 {arguments[2]}"
        )
    if kind == "Abs":
        return f"|{arguments[0]}|"
    if kind == "Signum":
        return f"sign({arguments[0]})"
    if kind == "Math":
        operator = parameters.get("Operator", "")
        template = _MATH_TEMPLATES.get(operator)
        if template:
            return template.format(*arguments)
        return f"{operator}({', '.join(arguments)})"
    if kind == "Lookup_n-D":
        table = parameters.get("Table", "?")
        text = f"按（{', '.join(arguments)}）查表 {_code(table)}"
        extrapolation = parameters.get("ExtrapMethod")
        return text + (f"，外插方式 {_code(extrapolation)}" if extrapolation else "")
    if kind == "RelationalOperator":
        return f"{arguments[0]} {parameters.get('Operator', '')} {arguments[1]}"
    if kind == "Logic":
        operator = parameters.get("Operator", "AND")
        operator = {"AND": "且", "OR": "或", "NAND": "与非", "NOR": "或非"}.get(operator, operator)
        return f" {operator} ".join(arguments)
    if kind == "MinMax":
        function = parameters.get("Function", "min")
        return f"{function}({', '.join(arguments)})"
    if kind == "Bias":
        return f"{arguments[0]} + {_code(parameters.get('Bias', '0'))}"
    if kind == "CheckDynamicLowerBound":
        return f"{arguments[0]} 与动态下限比较"
    if kind == "DataTypeConversion":
        return f"{arguments[0]} 转为 {_code(parameters.get('OutDataTypeStr', ''))}"
    if kind in {"UnitDelay", "Memory"}:
        return f"{arguments[0]} 延后一步"
    if kind == "Trigonometry":
        return f"{parameters.get('Operator', 'sin')}({', '.join(arguments)})"
    if kind == "Rounding Function":
        return f"按 {_code(parameters.get('Operator', ''))} 取整 {arguments[0]}"
    return ""


def _system_explanation(system: System) -> list[str]:
    """Explain how signals flow and are computed, not how many blocks exist."""
    blocks = {block.sid: block for block in system.blocks}
    children = {child.owner.sid: child for child in system.children if child.owner}
    signal_edges = [edge for edge in system.edges if edge.kind != "physical-conserving"]
    conserved_edges = [edge for edge in system.edges if edge.kind == "physical-conserving"]
    signal_blocks: set[str] = set()
    for edge in signal_edges:
        signal_blocks.update((_endpoint(edge.source)[0], _endpoint(edge.destination)[0]))
    input_ports: dict[str, set[str]] = {}
    output_ports: dict[str, set[str]] = {}
    for edge in signal_edges:
        source_sid, source_port = _endpoint(edge.source)
        destination_sid, destination_port = _endpoint(edge.destination)
        input_ports.setdefault(destination_sid, set()).add(destination_port)
        output_ports.setdefault(source_sid, set()).add(source_port)

    def destination_text(sid: str, port: str) -> str:
        block = blocks.get(sid)
        if block is None:
            return f"端点 {_code(sid)}"
        if block.block_type == "Outport":
            return f"输出 {_code(block.name)}"
        child = children.get(sid)
        text = _linked(block, child)
        port_name = _child_port(child, "in", port)
        if port_name:
            return f"{text} 的 {_code(port_name)} 口"
        if len(input_ports.get(sid, ())) > 1:
            return f"{text} 的 {port} 口"
        return text

    arguments: dict[str, dict[str, str]] = {}
    destinations: dict[str, list[str]] = {}
    outputs_of: dict[tuple[str, str], list[str]] = {}
    for edge in signal_edges:
        source_sid, source_port = _endpoint(edge.source)
        destination_sid, destination_port = _endpoint(edge.destination)
        if destination_sid not in blocks:
            continue
        text = destination_text(destination_sid, destination_port)
        if source_sid in blocks:
            source = _linked(blocks[source_sid], children.get(source_sid))
            label = _child_port(children.get(source_sid), "out", source_port)
            if label:
                source += f" 的 {_code(label)} 口"
            elif len(output_ports.get(source_sid, ())) > 1:
                source += f" 的 {source_port} 口"
            arguments.setdefault(destination_sid, {})[destination_port] = source
            destinations.setdefault(source_sid, []).append(text)
            outputs_of.setdefault((source_sid, source_port), []).append(text)

    items: list[str] = []
    for block in _processing_order(system):
        if conserved_edges and block.sid not in signal_blocks:
            continue
        ports = arguments.get(block.sid, {})
        names = [ports[port] for port in _port_order(ports)]
        if block.block_type == "Outport":
            continue
        if block.block_type == "Inport":
            targets = _unique(destinations.get(block.sid, []))
            suffix = f" → {'、'.join(targets)}" if targets else "（未连接）"
            items.append(f"输入 {_code(block.name)}{suffix}")
            continue
        if block.block_type in {"ConnectionPort", "PMIOPort"}:
            targets = _unique(destinations.get(block.sid, []))
            suffix = f" ↔ {'、'.join(targets)}" if targets else ""
            items.append(f"守恒端口 {_code(block.name)}{suffix}")
            continue
        child = children.get(block.sid)
        if child is not None:
            parts: list[str] = []
            if names:
                parts.append(f"输入 {'、'.join(names)}")
            output_ports = {port.parameters.get("Port", "1") for port in child.outputs}
            for port in _port_order(output_ports | set(outputs_of.get((block.sid, ""), []))):
                targets = _unique(outputs_of.get((block.sid, port), []))
                label = _child_port(child, "out", port)
                head = f"{port} 口" + (f"（{_code(label)}）" if label else "")
                parts.append(f"{head} → {'、'.join(targets)}" if targets else f"{head}（无下游）")
            items.append(f"{_linked(block, child)}：{'；'.join(parts)}")
            continue
        if not names:
            operation = _source_expression(block)
            if not operation:
                # Nothing to explain without inputs and a known source; the
                # block table below still lists it.
                continue
        elif block.block_type in {"Scope", "Display", "ToWorkspace", "Terminator"}:
            operation = f"接收 {'、'.join(names)}"
        else:
            operation = _operation(block, names) or "、".join(names)
        targets = _unique(destinations.get(block.sid, []))
        suffix = f" → {'、'.join(targets)}" if targets else ""
        items.append(f"{_linked(block, child)}：{operation}{suffix}")

    lines: list[str] = []
    if conserved_edges:
        links = []
        for edge in conserved_edges:
            source_sid, _ = _endpoint(edge.source)
            destination_sid, _ = _endpoint(edge.destination)
            source = (
                _linked(blocks[source_sid], children.get(source_sid))
                if source_sid in blocks
                else _code(source_sid)
            )
            destination = (
                _linked(blocks[destination_sid], children.get(destination_sid))
                if destination_sid in blocks
                else _code(destination_sid)
            )
            links.append(f"{source} ↔ {destination}")
        if links:
            lines.append(f"守恒连接（双向）：{'、'.join(_unique(links))}。")
    if items:
        if lines:
            lines.append("")
        lines.extend(f"- {item}" for item in items[:_FLOW_ITEM_LIMIT])
        if len(items) > _FLOW_ITEM_LIMIT:
            lines.append(f"- 其余 {len(items) - _FLOW_ITEM_LIMIT} 个节点的处理见流程图。")
    return lines


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
        # Only the block name: the type is already in the block table below.
        lines.append(f'  {node}{shape_left}"{_mermaid_text(block.name)}"{shape_right}')
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
        source_sid, _ = _endpoint(edge.source)
        destination_sid, _ = _endpoint(edge.destination)
        connector = "---" if edge.kind == "physical-conserving" else "-->"
        # Unnamed signals stay unlabeled: the graph already shows the wiring and
        # the system explanation names the ports each value enters.
        label = f"|{_mermaid_text(edge.name)}|" if edge.name else ""
        lines.append(f"  b{_slug(source_sid)} {connector}{label} b{_slug(destination_sid)}")
    lines.extend(["```", "", "## 系统说明", ""])
    lines.extend(_system_explanation(system))
    lines.extend(
        [
            "",
            "| 接口类别 | 端口 | 名称 |",
            "| --- | --- | --- |",
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
                f"| {category} | {_cell(port.parameters.get('Port', '1'))} | {_cell(port.name)} |"
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
        name = f"{_cell(edge.name)}：" if edge.name else ""
        lines.append(
            f"| 守恒连接（双向） | {_cell(source_port)} ↔ {_cell(destination_port)} "
            f"| {name}{_cell(source_name)} ↔ {_cell(destination_name)} |"
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
        lines.append("| - | - | 无显式接口端口 |")
    lines.extend(
        [
            "",
            f"执行语义：`{', '.join(system.subsystem_types)}`。"
            "具体调度由 Simulink 求解器、采样时间和控制端口共同决定，流程图布局不表示执行顺序。",
            "",
            "## 块参数",
            "",
            "| 块 | 类型 | 参数 |",
            "| --- | --- | --- |",
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
                f"| {param_text} |"
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
        lines.append(f"| {name} | {source} | {param_text or '-'} |")
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
