# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Read Simulink SLX system XML without requiring a MATLAB installation."""

from __future__ import annotations

import posixpath
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
    # Port names the SLX file states for this block: the <List ListType="InputPortNames">
    # lists of a ModelReference block, keyed by one-based port index.
    port_names: dict[str, dict[int, str]] = field(default_factory=dict)
    port_counts: dict[str, int] = field(default_factory=dict)


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
            # R2025b writes <ModelInformation><Subsystem><System Ref=.../>.
            # Older releases use <Model><System Ref=.../>.
            root_ref_element = root_xml.find("./Subsystem/System")
        if root_ref_element is None:
            # Block libraries store the root under <Library><System>.
            root_ref_element = root_xml.find("./Library/System")
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
                for prop in node.findall("./PortCounts"):
                    for kind in ("in", "out"):
                        if (prop.get(kind) or "").isdigit():
                            block.port_counts[kind] = int(prop.get(kind))
                for kind, list_type in (
                    ("in", "InputPortNames"),
                    ("out", "OutputPortNames"),
                ):
                    names: dict[int, str] = {}
                    for prop in node.findall(f'./List[@ListType="{list_type}"]/P'):
                        index = re.fullmatch(r"port(\d+)", prop.get("Name") or "")
                        text = (prop.text or "").strip()
                        if index and text:
                            names[int(index.group(1)) + 1] = text
                    if names:
                        block.port_names[kind] = names
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


def _slug(value: str) -> str:
    value = re.sub(r"[^\w.-]+", "_", value, flags=re.UNICODE).strip("._")
    return value or "subsystem"


def _child_directory(system: System) -> str:
    siblings = system.parent.children if system.parent else []
    duplicates = sum(_slug(s.name) == _slug(system.name) for s in siblings)
    suffix = f"_{system.ref.removeprefix('system_')}" if duplicates > 1 else ""
    return _slug(system.name) + suffix


def _endpoint(value: str) -> tuple[str, str]:
    match = re.fullmatch(r"(.*)#(?:in|out|[lr]?conn):(.+)", value, flags=re.IGNORECASE)
    return (match.group(1), match.group(2)) if match else (value, "?")


def _endpoint_kind(value: str) -> str:
    match = re.fullmatch(r".*#(in|out|[lr]?conn):.+", value, flags=re.IGNORECASE)
    return match.group(1) if match else "port"


def system_json_documents(model: System, language: str = "en") -> dict[str, dict]:
    """Return one JSON object per system, keyed by its resource path.

    The model root and systems with children use ``main.json``. A leaf system is
    one sibling JSON file, for example ``xCU/xCU_Output.json``. The document is
    the primary representation: each block carries its ports (by name when the
    file states one, otherwise by port index) and parameters, and each line
    carries one source endpoint and every destination it fans out to.
    """
    documents: dict[str, dict] = {}

    def visit(system: System, directory: str, is_root: bool = False) -> None:
        if is_root:
            path = "main.json"
        elif system.children:
            path = f"{directory}/main.json"
        else:
            path = f"{directory}.json"
        documents[path] = _system_json(system, is_root, path, language)
        for child in system.children:
            child_dir = (
                f"{directory}/{_child_directory(child)}" if directory else _child_directory(child)
            )
            visit(child, child_dir)

    visit(model, "", True)
    return documents


def _port_sort_key(index: str) -> tuple[int, int, str]:
    return (0, int(index), "") if str(index).isdigit() else (1, 0, str(index))


def _port_names(system: System) -> dict[str, dict[str, dict[int, str]]]:
    """Port names the SLX file itself states, per block and port index.

    Subsystem blocks take the names of the Inport/Outport blocks inside the
    referenced system; ModelReference blocks take their ``InputPortNames`` /
    ``OutputPortNames`` lists; port blocks are named after the block. Ordinary
    blocks store no port names in Simulink, so their ports stay unnamed here and
    fall back to the port index when written.
    """
    child_systems = {child.ref: child for child in system.children}
    names: dict[str, dict[str, dict[int, str]]] = {}
    for block in system.blocks:
        entry = {kind: dict(values) for kind, values in block.port_names.items()}
        child = child_systems.get(block.system_ref)
        if child is not None:
            for kind, child_ports in (("in", child.inputs), ("out", child.outputs)):
                named = {}
                for port in child_ports:
                    index = port.parameters.get("Port", "1")
                    if index.isdigit() and port.name:
                        named[int(index)] = port.name
                if named:
                    entry[kind] = named
        self_kind = {
            "Inport": "out",
            "Outport": "in",
            "ConnectionPort": "conn",
            "PMIOPort": "conn",
        }.get(block.block_type)
        # A port block has exactly one port of its own; the ``Port`` parameter is
        # its position in the parent system's port list, not this port's index.
        if self_kind and block.name:
            entry.setdefault(self_kind, {})[1] = block.name
        names[block.sid] = entry
    return names


def _system_json(system: System, is_root: bool, path: str, language: str) -> dict:
    block_names = {block.sid: block.name for block in system.blocks}
    port_names = _port_names(system)
    ports: dict[str, dict[str, dict[str, object]]] = {
        block.sid: {"in": {}, "out": {}, "conn": {}} for block in system.blocks
    }
    unresolved: list[dict] = []
    seen_unresolved: set[tuple[str, str, str]] = set()

    def port_value(sid: str, kind: str, index: str) -> object:
        if str(index).isdigit():
            named = port_names.get(sid, {}).get(kind, {}).get(int(index))
            return named or int(index)
        return index

    def add_port(sid: str, kind: str, index: str) -> None:
        bucket = "conn" if kind in {"conn", "lconn", "rconn"} else kind
        if sid not in ports:
            key = (sid, str(index), bucket)
            if key not in seen_unresolved:
                seen_unresolved.add(key)
                unresolved.append({"sid": sid, "port": index, "kind": bucket})
            return
        if bucket not in ports[sid]:
            bucket = "out"
        ports[sid][bucket].setdefault(str(index), port_value(sid, bucket, index))

    edge_documents: list[dict] = []
    edge_index: dict[tuple[str, str, str], dict] = {}
    for edge in system.edges:
        source_sid, source_port = _endpoint(edge.source)
        destination_sid, destination_port = _endpoint(edge.destination)
        source_kind = _endpoint_kind(edge.source)
        destination_kind = _endpoint_kind(edge.destination)
        if edge.kind == "physical-conserving" or "conn" in {source_kind, destination_kind}:
            source_kind = destination_kind = "conn"
        add_port(source_sid, source_kind, source_port)
        add_port(
            destination_sid,
            destination_kind if destination_kind in {"in", "conn"} else "in",
            destination_port,
        )
        key = (source_sid, source_port, edge.name)
        row = edge_index.get(key)
        if row is None:
            row = {
                "from": [
                    block_names.get(source_sid, ""),
                    port_value(
                        source_sid,
                        "conn" if source_kind in {"conn", "lconn", "rconn"} else source_kind,
                        source_port,
                    ),
                ],
                "to": [],
                "signal": edge.name or None,
            }
            edge_index[key] = row
            edge_documents.append(row)
        destination = [
            block_names.get(destination_sid, ""),
            port_value(
                destination_sid,
                "conn" if destination_kind == "conn" else "in",
                destination_port,
            ),
        ]
        if destination not in row["to"]:
            row["to"].append(destination)

    for block in system.blocks:
        for kind in ("in", "out", "conn"):
            count = block.port_counts.get(kind, 0)
            if not count:
                count = max(port_names.get(block.sid, {}).get(kind, {}) or [0])
            for index in range(1, count + 1):
                ports[block.sid][kind].setdefault(
                    str(index), port_value(block.sid, kind, str(index))
                )

    blocks = []
    for block in system.blocks:
        block_ports = {}
        for kind, values in ports[block.sid].items():
            if not values:
                continue
            block_ports[kind] = [values[index] for index in sorted(values, key=_port_sort_key)]
        blocks.append(
            {
                "name": block.name,
                "block_type": block.block_type,
                "source_block": block.source_block,
                "ports": block_ports,
                "params": _display_parameters(block),
            }
        )

    children = []
    for child in system.children:
        if not child.owner:
            continue
        child_dir = _child_directory(child)
        base = posixpath.dirname(path)
        child_abs = posixpath.join(
            base, f"{child_dir}/main.json" if child.children else f"{child_dir}.json"
        )
        child_path = posixpath.relpath(child_abs, base or ".")
        children.append(
            {
                "name": child.name,
                "path": child_path,
                "system_ref": child.ref,
                "type": "simulink-subsystem",
            }
        )

    document = {
        "schema": "ov.matlab.simulink/1",
        "system": system.name,
        "system_ref": system.ref,
        "type": "simulink-model" if is_root else "simulink-subsystem",
        "subsystem_types": system.subsystem_types,
        "execution": {},
        "blocks": blocks,
        "edges": edge_documents,
        "description": "",
        "children": children,
        "coverage": {
            "blocks": len(blocks),
            "edges": len(edge_documents),
            "unresolved_endpoints": len(unresolved),
        },
    }
    if unresolved:
        document["unresolved_endpoints"] = unresolved
    return document
