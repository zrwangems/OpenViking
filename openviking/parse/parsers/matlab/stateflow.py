# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Stateflow chart XML to structured JSON.

A chart is written as the state machine a reader needs: the state hierarchy,
each state's entry/during/exit actions, the transitions with their event,
condition and actions, and the other chart components (note boxes, junctions,
MATLAB and Simulink functions, events, data). Layout properties such as
window position, zoom, colours and label HTML are dropped.
"""

from __future__ import annotations

import html
import re
import textwrap
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member

STATE_FLOW_SCHEMA = "ov.matlab.stateflow/2"

#: Elements that own a nested view. Everything below one of these belongs to it.
_CONTAINER_TAGS = {"chart", "state", "box", "function", "truthTable", "machine"}
_STATE_TAGS = {"state", "box"}
_FUNCTION_TAGS = {"function", "truthTable"}
_COMPONENT_TAGS = {
    "state",
    "box",
    "junction",
    "transition",
    "data",
    "event",
    "function",
    "truthTable",
}

_ACTION_ALIASES = {
    "entry": "entry",
    "en": "entry",
    "during": "during",
    "du": "during",
    "exit": "exit",
    "ex": "exit",
    "bind": "bind",
}
_ACTION_HEADER = re.compile(
    r"^\s*(?:(?P<keywords>"
    r"(?:entry|en|during|du|exit|ex|bind)(?:\s*,\s*(?:entry|en|during|du|exit|ex|bind))*)"
    r"|on\s+(?P<event>[^\s:]+))\s*:\s*(?P<rest>.*)$",
    re.IGNORECASE,
)
_CALL = re.compile(r"notify\s*\(\s*[^,]+,\s*['\"]([^'\"]+)['\"]")
_SIGNATURE = re.compile(r"^\s*(?:\[[^\]]*\]|[\w.]+)\s*=\s*(?P<name>\w+)\s*\(")
_CALL_SIGNATURE = re.compile(r"^\s*(?P<name>\w+)\s*\(")


@dataclass
class State:
    ssid: str
    label: str
    state_type: str
    decomposition: str = ""
    parent: str = ""
    active_state_output: str = ""

    @property
    def name(self) -> str:
        for line in self.label.splitlines():
            if line.strip() and not _ACTION_HEADER.match(line):
                return line.strip()
        return self.ssid


@dataclass
class Function:
    ssid: str
    label: str
    kind: str
    parent: str = ""
    block: str = ""
    script: str = ""
    properties: dict[str, str] = field(default_factory=dict)

    @property
    def signature(self) -> str:
        return _first_line(self.label)

    @property
    def name(self) -> str:
        return _function_name(self.label) or self.ssid

    @property
    def body(self) -> str:
        return _function_body(self.script)

    @property
    def notifies(self) -> list[str]:
        return _unique(_CALL.findall(self.script))


@dataclass
class Junction:
    ssid: str
    junction_type: str
    parent: str = ""

    @property
    def name(self) -> str:
        return f"Junction {self.ssid}"


@dataclass
class Note:
    ssid: str
    text: str
    parent: str = ""


@dataclass
class Transition:
    ssid: str
    source: str
    destination: str
    label: str
    order: str
    scope: str = ""


@dataclass
class Data:
    ssid: str
    name: str
    scope: str
    data_type: str
    size: str
    initial_value: str = ""
    parent: str = ""


@dataclass
class Event:
    ssid: str
    name: str
    scope: str
    trigger: str
    tag: str = ""


@dataclass
class Chart:
    chart_id: str
    name: str
    action_language: str
    states: list[State] = field(default_factory=list)
    functions: list[Function] = field(default_factory=list)
    notes: list[Note] = field(default_factory=list)
    junctions: list[Junction] = field(default_factory=list)
    transitions: list[Transition] = field(default_factory=list)
    data: list[Data] = field(default_factory=list)
    events: list[Event] = field(default_factory=list)


def _props(element) -> dict[str, str]:
    return {p.get("Name"): p.text or "" for p in element.findall("./P") if p.get("Name")}


def _first_line(value: str) -> str:
    return next((line.strip() for line in value.splitlines() if line.strip()), "")


def _join(left: str, right: str) -> str:
    left, right = left.rstrip(), right.rstrip()
    if not left:
        return right.strip()
    if not right.strip():
        return left.strip()
    return f"{left}\n{right.strip()}"


def _unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))


def _compact(payload: dict) -> dict:
    """Drop empty values; ``None`` stays where it marks the chart level."""
    return {key: value for key, value in payload.items() if value not in ("", [], {})}


def state_actions(label: str) -> dict[str, object]:
    """Split a state label into its named action groups.

    Stateflow writes ``entry``/``during``/``exit``/``bind`` (with ``en``/``du``/
    ``ex`` shorthand and combined headers such as ``entry, during:``) and
    ``on <event>`` groups, each followed by the statements that belong to it.
    """
    groups: dict[str, list[str]] = {}
    on_actions: list[tuple[str, list[str]]] = []
    target: list[str] | None = None
    for line in label.splitlines():
        header = _ACTION_HEADER.match(line)
        if header:
            rest = header.group("rest")
            if header.group("event"):
                target = []
                on_actions.append((header.group("event"), target))
            else:
                names = [
                    _ACTION_ALIASES[item.strip().lower()]
                    for item in header.group("keywords").split(",")
                ]
                target = groups.setdefault(names[0], [])
                for name in names[1:]:
                    groups[name] = target
            if rest.strip():
                target.append(rest)
            continue
        if target is not None:
            target.append(line)
    actions: dict[str, object] = {name: _clean_body(lines) for name, lines in groups.items()}
    if on_actions:
        actions["on"] = [
            {"event": event, "actions": _clean_body(lines)} for event, lines in on_actions
        ]
    return actions


def _clean_body(lines: list[str]) -> str:
    return textwrap.dedent("\n".join(lines)).strip()


def _function_name(label: str) -> str:
    signature = _first_line(label)
    matched = _SIGNATURE.match(signature) or _CALL_SIGNATURE.match(signature)
    return matched.group("name") if matched else signature


def _function_body(script: str) -> str:
    lines = script.splitlines()
    if lines and lines[0].lstrip().startswith("function"):
        lines = lines[1:]
    return _clean_body(lines)


def _read_block(text: str, start: int, opener: str) -> tuple[str, int]:
    closer = {"(": ")", "[": "]", "{": "}"}[opener]
    depth, quote, index = 0, "", start
    while index < len(text):
        char = text[index]
        if quote:
            if char == quote:
                quote = ""
        elif char in "\"'":
            quote = char
        elif char == opener:
            depth += 1
        elif char == closer:
            depth -= 1
            if depth == 0:
                return text[start + 1 : index], index + 1
        index += 1
    return text[start + 1 :], len(text)


def transition_label(label: str) -> dict[str, str]:
    """Split a transition label into event, condition, condition action and action.

    The order in a Stateflow transition label is
    ``event [condition] {condition action} / transition action``; brackets and
    braces only count at the top level, so MATLAB indexing inside a condition or
    a ``...`` line continuation stays in its block.
    """
    event: list[str] = []
    parts = {"condition": "", "condition_action": "", "transition_action": ""}
    buffer: list[str] = []
    index, parens = 0, 0
    while index < len(label):
        char = label[index]
        if char == "(":
            parens += 1
        elif char == ")":
            parens = max(0, parens - 1)
        if parens == 0 and char in "[{/":
            event.append("".join(buffer))
            buffer = []
            if char == "/":
                parts["transition_action"] = label[index + 1 :].strip()
                break
            block, index = _read_block(label, index, char)
            key = "condition" if char == "[" else "condition_action"
            parts[key] = _join(parts[key], block)
            continue
        buffer.append(char)
        index += 1
    event.append("".join(buffer))
    return {
        "event": "\n".join(part.strip() for part in event if part.strip()).strip(),
        "condition": parts["condition"].strip(),
        "condition_action": parts["condition_action"].strip(),
        "transition_action": parts["transition_action"].strip(),
    }


def _container(parents: dict, element, root) -> str:
    current = parents.get(element)
    while current is not None and current is not root:
        if current.tag in _CONTAINER_TAGS:
            return current.get("SSID", "")
        current = parents.get(current)
    return ""


def _note_text(label: str) -> str:
    text = re.sub(r"(?is)<(style|head)\b.*?</\1>", "", label)
    text = re.sub(r"(?i)<br\s*/?>|</p>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    lines = (re.sub(r"[ \t]+", " ", line).strip() for line in html.unescape(text).splitlines())
    return "\n".join(line for line in lines if line)


def _parse_chart(root, member: str) -> Chart:
    props = _props(root)
    chart = Chart(
        chart_id=root.get("id") or Path(member).stem.removeprefix("chart_"),
        name=props.get("name", Path(member).stem),
        action_language=props.get("actionLanguage", "未声明"),
    )
    parents = {child: parent for parent in root.iter() for child in parent}
    for element in root.iter():
        if element.tag not in _COMPONENT_TAGS:
            continue
        element_props = _props(element)
        parent = _container(parents, element, root)
        if element.tag in _STATE_TAGS or element.tag in _FUNCTION_TAGS:
            state_type = (
                "BOX"
                if element.tag == "box"
                else "TRUTH_TABLE"
                if element.tag == "truthTable"
                else element_props.get("type", "未知")
            )
            if element_props.get("isNoteBox") == "1":
                chart.notes.append(
                    Note(
                        ssid=element.get("SSID", ""),
                        text=_note_text(element_props.get("labelString", "")),
                        parent=parent,
                    )
                )
            elif state_type == "FUNC_STATE" or element.tag in _FUNCTION_TAGS:
                simulink = element.find("./simulink")
                eml = element.find("./eml")
                eml_props = _props(eml) if eml is not None else {}
                simulink_props = _props(simulink) if simulink is not None else {}
                truth_table = (
                    element if element.tag == "truthTable" else element.find(".//truthTable")
                )
                if eml_props.get("isEML") == "1":
                    kind = "matlab"
                elif simulink_props.get("isSimulinkFcn") == "1":
                    kind = "simulink"
                elif element.tag == "truthTable" or truth_table is not None:
                    kind = "truth_table"
                else:
                    kind = "graphical"
                table_props = (
                    {
                        item.get("Name"): item.text or ""
                        for item in truth_table.iter("P")
                        if item.get("Name")
                    }
                    if truth_table is not None
                    else {}
                )
                chart.functions.append(
                    Function(
                        ssid=element.get("SSID", ""),
                        label=element_props.get("labelString", ""),
                        kind=kind,
                        parent=parent,
                        block=simulink_props.get("blockName", ""),
                        script=eml_props.get("script", ""),
                        properties=table_props,
                    )
                )
            else:
                active_output = element.find("./activeStateOutput")
                chart.states.append(
                    State(
                        ssid=element.get("SSID", ""),
                        label=element_props.get("labelString", ""),
                        state_type=state_type,
                        decomposition=element_props.get("decomposition", ""),
                        parent=parent,
                        active_state_output=_props(active_output).get("activityMode", "")
                        if active_output is not None
                        else "",
                    )
                )
        elif element.tag == "junction":
            chart.junctions.append(
                Junction(
                    ssid=element.get("SSID", ""),
                    junction_type=element_props.get("type", ""),
                    parent=parent,
                )
            )
        elif element.tag == "transition":
            source = element.find("./src/P[@Name='SSID']")
            destination = element.find("./dst/P[@Name='SSID']")
            chart.transitions.append(
                Transition(
                    ssid=element.get("SSID", ""),
                    source=source.text if source is not None and source.text else "",
                    destination=destination.text
                    if destination is not None and destination.text
                    else "",
                    label=element_props.get("labelString", ""),
                    order=element_props.get("executionOrder", "未声明"),
                    scope=parent,
                )
            )
        elif element.tag == "data":
            size = element.find("./props/array/P[@Name='size']")
            initial = element.find("./props/P[@Name='initialValue']")
            chart.data.append(
                Data(
                    ssid=element.get("SSID", ""),
                    name=element.get("name", ""),
                    scope=element_props.get("scope", "未声明"),
                    data_type=element_props.get("dataType", "未声明"),
                    size=size.text if size is not None and size.text else "未声明",
                    initial_value=initial.text if initial is not None and initial.text else "",
                    parent=parent,
                )
            )
        elif element.tag == "event":
            chart.events.append(
                Event(
                    ssid=element.get("SSID", ""),
                    name=element_props.get("name", ""),
                    scope=element_props.get("scope", "未声明"),
                    trigger=element_props.get("trigger", "未声明"),
                    tag=element_props.get("tag", ""),
                )
            )
    return chart


def parse_stateflow(path: str | Path) -> list[Chart]:
    path = Path(path)
    charts = []
    with zipfile.ZipFile(path) as archive:
        names = sorted(
            n
            for n in archive.namelist()
            if n.startswith("simulink/stateflow/chart_") and n.endswith(".xml")
        )
        for name in names:
            root = ET.fromstring(read_xml_member(archive, name))
            charts.append(_parse_chart(root, name))
    return charts


def chart_system_path(chart: Chart) -> str:
    """Return the Simulink subsystem names used to place this chart."""
    return "/".join(_slug(part) for part in chart.name.split("/") if part)


def _slug(value: str) -> str:
    value = re.sub(r"[^\w.-]+", "_", value, flags=re.UNICODE).strip("._")
    return value or "stateflow"


def _component_names(chart: Chart) -> dict[str, str]:
    names = {state.ssid: state.name for state in chart.states}
    names.update({function.ssid: function.name for function in chart.functions})
    names.update({junction.ssid: junction.name for junction in chart.junctions})
    return names


def _component_kinds(chart: Chart) -> dict[str, str]:
    kinds = {state.ssid: "state" for state in chart.states}
    kinds.update({function.ssid: "function" for function in chart.functions})
    kinds.update({junction.ssid: "junction" for junction in chart.junctions})
    return kinds


def _paths(chart: Chart) -> dict[str, str]:
    parents = {state.ssid: state.parent for state in chart.states}
    parents.update({function.ssid: function.parent for function in chart.functions})
    names = _component_names(chart)

    def walk(ssid: str, seen: tuple[str, ...] = ()) -> str:
        name = names.get(ssid, ssid)
        parent = parents.get(ssid, "")
        if not parent or parent in seen or parent not in names:
            return name
        return f"{walk(parent, (*seen, ssid))}/{name}"

    return {ssid: walk(ssid) for ssid in names}


def _state_json(state: State, path: str) -> dict:
    payload = {
        "id": state.ssid,
        "name": state.name,
        "path": path,
        "type": state.state_type,
        "decomposition": state.decomposition,
        "parent": state.parent or None,
        "active_state_output": state.active_state_output,
        **state_actions(state.label),
    }
    return _compact(payload)


def _function_json(function: Function, path: str, data: list[Data]) -> dict:
    own = [item for item in data if item.parent == function.ssid]
    payload = {
        "id": function.ssid,
        "name": function.name,
        "path": path,
        "kind": function.kind,
        "parent": function.parent or None,
        "signature": function.signature,
        "block": function.block,
        "inputs": [item.name for item in own if item.scope == "FUNCTION_INPUT_DATA"],
        "outputs": [item.name for item in own if item.scope == "FUNCTION_OUTPUT_DATA"],
        "notifies": function.notifies,
        "properties": function.properties,
        "body": function.body,
    }
    return _compact(payload)


def chart_json(chart: Chart) -> dict:
    """Return one chart as the JSON document written next to its subsystem."""
    names = _component_names(chart)
    kinds = _component_kinds(chart)
    paths = _paths(chart)

    def endpoint(ssid: str) -> tuple[str | None, str | None, str]:
        if not ssid:
            return None, None, "default"
        return ssid, names.get(ssid), kinds.get(ssid, "unknown")

    transitions = []
    for transition in chart.transitions:
        source, source_name, source_kind = endpoint(transition.source)
        target, target_name, target_kind = endpoint(transition.destination)
        payload = {
            "id": transition.ssid,
            "order": transition.order,
            "from": source,
            "from_name": source_name,
            "from_kind": source_kind,
            "to": target,
            "to_name": target_name,
            "to_kind": target_kind,
            **({"scope": transition.scope} if transition.scope else {}),
            **_name_of("scope_name", transition.scope, names),
            **transition_label(transition.label),
        }
        transitions.append(_compact(payload))

    return {
        "schema": STATE_FLOW_SCHEMA,
        "chart_id": chart.chart_id,
        "chart": chart.name,
        "action_language": chart.action_language,
        "summary": {
            "states": len(chart.states),
            "functions": len(chart.functions),
            "notes": len(chart.notes),
            "junctions": len(chart.junctions),
            "transitions": len(chart.transitions),
            "events": len(chart.events),
            "data": len([item for item in chart.data if not _is_function_interface(item)]),
        },
        "states": [_state_json(state, paths[state.ssid]) for state in chart.states],
        "functions": [
            _function_json(function, paths[function.ssid], chart.data)
            for function in chart.functions
        ],
        "notes": [
            _compact(
                {
                    "id": note.ssid,
                    "text": note.text,
                    "parent": note.parent or None,
                    **_name_of("parent_name", note.parent, names),
                }
            )
            for note in chart.notes
        ],
        "junctions": [
            _compact(
                {
                    "id": junction.ssid,
                    "name": junction.name,
                    "type": junction.junction_type,
                    "parent": junction.parent or None,
                    **_name_of("parent_name", junction.parent, names),
                }
            )
            for junction in chart.junctions
        ],
        "transitions": transitions,
        "events": [
            _compact(
                {
                    "id": event.ssid,
                    "name": event.name,
                    "scope": event.scope,
                    "trigger": event.trigger,
                    "tag": event.tag,
                }
            )
            for event in chart.events
        ],
        "data": [
            _compact(
                {
                    "id": item.ssid,
                    "name": item.name,
                    "scope": item.scope,
                    "data_type": item.data_type,
                    "size": item.size,
                    "initial_value": item.initial_value,
                    "parent": item.parent or None,
                    **_name_of("parent_name", item.parent, names),
                }
            )
            for item in chart.data
            if not _is_function_interface(item)
        ],
    }


def _name_of(key: str, ssid: str, names: dict[str, str]) -> dict[str, str]:
    return {key: names[ssid]} if ssid in names else {}


def _is_function_interface(item: Data) -> bool:
    """Function arguments live in the function entry, not in the chart's data list."""
    return item.scope in {"FUNCTION_INPUT_DATA", "FUNCTION_OUTPUT_DATA"}
