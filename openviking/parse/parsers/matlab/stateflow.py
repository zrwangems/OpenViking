# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Stateflow chart XML to structured JSON.

A chart is written the way a person reads it in Simulink: states nest the way
they nest on the canvas, each state carries its entry/during/exit/on actions,
the transitions drawn inside a state are listed there, and the chart's other
components (MATLAB and Simulink functions, note boxes, junctions, events, data)
sit in the container they were drawn in.

Nothing in the output is a machine identifier. States, transitions and
everything else are referred to by name; when the same name is used more than
once in a chart, the reference is the path through the nesting that separates
them. Junctions have no name on the canvas, so a transition that runs through
one is written as the path it makes: from the source state, through the
junction's own condition and action, to the state it ends in.
"""

from __future__ import annotations

import html
import re
import textwrap
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member

STATE_FLOW_SCHEMA = "ov.matlab.stateflow/3"

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

#: A transition is followed through this many junctions at most, and a single
#: source may branch into this many paths; beyond either the junction hops stay
#: as their own entries instead of being written as whole paths.
_MAX_JUNCTION_HOPS = 8
_MAX_JUNCTION_PATHS = 32


@dataclass
class State:
    ssid: str
    label: str
    state_type: str
    decomposition: str = ""
    parent: str = ""
    active_state_output: str = ""
    is_box: bool = False

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
        return _function_name(self.label)

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
    parent: str = ""


@dataclass
class Chart:
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
                        is_box=element.tag == "box",
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
                    parent=parent,
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


def chart_file_name(chart: Chart) -> str:
    """Return the file name a chart is written under, derived from its name."""
    return f"stateflow/{_slug(chart.name)}.json"


def _slug(value: str) -> str:
    value = re.sub(r"[^\w.-]+", "_", value, flags=re.UNICODE).strip("._")
    return value or "stateflow"


class _Overflow(Exception):
    """A junction graph branches too far to be written as whole paths."""


@dataclass
class _Container:
    ssid: str
    kind: str  # "chart", "state" or "function"
    item: object | None = None
    states: list[str] = field(default_factory=list)
    functions: list[str] = field(default_factory=list)
    transitions: list[dict] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    data: list[dict] = field(default_factory=list)
    events: list[dict] = field(default_factory=list)


#: A component the chart leaves unnamed still needs a name to be referred to.
_UNNAMED = {
    "truth_table": "truth table",
    "graphical": "graphical function",
    "matlab": "function",
    "simulink": "function",
}


def _references(chart: Chart) -> tuple[dict[str, str], dict[str, str]]:
    """Return the name and path of every state and function, keyed by the XML id.

    Names are what the output uses; the id only exists inside the parser to tie
    a transition's endpoints back to what they point at, and never reaches the
    JSON.
    """
    parents: dict[str, str] = {}
    names: dict[str, str] = {}
    unnamed: Counter[str] = Counter()
    for state in chart.states:
        name = state.name.strip()
        if not name:
            unnamed["state"] += 1
            name = f"unnamed state {unnamed['state']}"
        names[state.ssid] = name
        parents[state.ssid] = state.parent
    for function in chart.functions:
        name = function.name.strip()
        if not name:
            fallback = _UNNAMED.get(function.kind, "function")
            unnamed[fallback] += 1
            name = f"{fallback} {unnamed[fallback]}"
        names[function.ssid] = name
        parents[function.ssid] = function.parent

    def walk(ssid: str, seen: tuple[str, ...] = ()) -> str:
        name = names.get(ssid, "")
        parent = parents.get(ssid, "")
        if not parent or parent not in names or parent in seen:
            return name
        return f"{walk(parent, (*seen, ssid))}/{name}"

    return names, {ssid: walk(ssid) for ssid in names}


def _reference(names: dict[str, str], paths: dict[str, str]) -> dict[str, str]:
    """Name every state and function; qualify repeated names with their path."""
    counts = Counter(names.values())
    return {
        ssid: paths[ssid] if counts[name] > 1 else name for ssid, name in names.items()
    }


def _order_key(transition: Transition) -> int:
    try:
        return int(transition.order)
    except (TypeError, ValueError):
        return 0


def _transition_parts(transition: Transition) -> dict[str, str]:
    parts = transition_label(transition.label)
    return {
        "event": parts["event"],
        "condition": parts["condition"],
        "condition_action": parts["condition_action"],
        "action": parts["transition_action"],
    }


def _junction_label(junction: Junction, index: int, paths: dict[str, str],
                    names: dict[str, str]) -> str:
    """Name a junction by the container it sits in; it has no name of its own."""
    container = paths.get(junction.parent) or names.get(junction.parent, "")
    return f"{container or 'chart'} 里的 junction {index}"


def _junction_paths(
    transition: Transition,
    out_edges: dict[str, list[Transition]],
    junction_ssids: dict[str, Junction],
) -> list[tuple[list[Transition], str]]:
    """Follow a transition through the junctions it enters.

    Returns the transitions it passes and the state it finally reaches; a
    junction that branches yields one entry per branch.
    """
    found: list[tuple[list[Transition], str]] = []

    def walk(prefix: list[Transition], node: str, seen: frozenset[str]) -> None:
        if len(found) >= _MAX_JUNCTION_PATHS or len(prefix) > _MAX_JUNCTION_HOPS:
            raise _Overflow
        edges = out_edges.get(node, []) if node in junction_ssids else []
        if not edges:
            found.append((prefix, node))
            return
        for edge in edges:
            if edge.destination in seen:
                raise _Overflow
            walk([*prefix, edge], edge.destination, seen | {edge.destination})

    first = transition.destination
    walk([transition], first, frozenset({first}) if first in junction_ssids else frozenset())
    return found


def _collapse(chart: Chart, names: dict[str, str], paths: dict[str, str]) -> dict[str, list[dict]]:
    """Write each transition as the state-to-state path it describes.

    Junctions carry no name on the canvas, so instead of naming them the
    transition runs from its source through the junction's own condition and
    action to the state it ends in; a junction that branches becomes one entry
    per branch, each with its own order.
    """
    ref = _reference(names, paths)
    junction_ssids = {junction.ssid: junction for junction in chart.junctions}
    junction_index = {
        junction.ssid: position
        for position, junction in enumerate(chart.junctions, start=1)
    }
    out_edges: dict[str, list[Transition]] = defaultdict(list)
    for transition in chart.transitions:
        if transition.source in junction_ssids:
            out_edges[transition.source].append(transition)
    for edges in out_edges.values():
        edges.sort(key=_order_key)

    def junction_ref(ssid: str) -> str:
        junction = junction_ssids[ssid]
        return _junction_label(junction, junction_index[ssid], paths, names)

    def raw(transition: Transition, destination: str) -> dict:
        source = ref.get(transition.source) or (
            junction_ref(transition.source) if transition.source in junction_ssids else None
        )
        target = ref.get(destination) or (
            junction_ref(destination) if destination in junction_ssids else None
        )
        payload = {
            "from": source,
            "to": target,
            **_transition_parts(transition),
            "order": transition.order,
        }
        if not source:
            payload.pop("from")
            payload["initial"] = True
        return _compact(payload)

    scoped: dict[str, list[dict]] = defaultdict(list)
    followed: set[str] = set()
    for transition in chart.transitions:
        if transition.source in junction_ssids:
            continue
        try:
            found = _junction_paths(transition, out_edges, junction_ssids)
        except _Overflow:
            scoped[transition.scope].append(raw(transition, transition.destination))
            continue
        for prefix, destination in found:
            followed.update(step.ssid for step in prefix[1:])
            head = prefix[0]
            payload = {
                "from": ref.get(head.source),
                "to": ref.get(destination),
                **_transition_parts(head),
                "order": head.order,
            }
            if prefix[1:]:
                payload["via"] = [
                    _compact({**_transition_parts(step), "order": step.order})
                    for step in prefix[1:]
                ]
            if not payload["from"]:
                payload.pop("from")
                payload["initial"] = True
            if not payload.get("to"):
                # The path ends on a junction nothing continues from, so it
                # leaves the state (or the chart entry) without a target.
                payload.pop("to", None)
            scoped[transition.scope].append(_compact(payload))

    # A junction nothing leads into still carries a condition of its own; keep it
    # rather than dropping what the chart says.
    for transition in chart.transitions:
        if transition.source in junction_ssids and transition.ssid not in followed:
            scoped[transition.scope].append(raw(transition, transition.destination))
            followed.add(transition.ssid)
    return scoped


def _is_function_interface(item: Data) -> bool:
    """Function arguments live in the function entry, not in the chart's data list."""
    return item.scope in {"FUNCTION_INPUT_DATA", "FUNCTION_OUTPUT_DATA"}


def _state_json(state: State, name: str) -> dict:
    parallel = state.state_type == "AND_STATE" or state.decomposition == "PARALLEL_STATE"
    payload = {
        "name": name,
        "parallel": True if parallel else "",
        "box": True if state.is_box else "",
        "active_state_output": state.active_state_output,
        **state_actions(state.label),
    }
    return _compact(payload)


def _function_json(function: Function, name: str, data: list[Data]) -> dict:
    own = [item for item in data if item.parent == function.ssid]
    payload = {
        "name": name,
        "kind": function.kind,
        "signature": function.signature,
        "block": function.block,
        "inputs": [item.name for item in own if item.scope == "FUNCTION_INPUT_DATA"],
        "outputs": [item.name for item in own if item.scope == "FUNCTION_OUTPUT_DATA"],
        "notifies": function.notifies,
        "properties": function.properties,
        "body": function.body,
    }
    return _compact(payload)


def _data_json(item: Data) -> dict:
    return _compact(
        {
            "name": item.name,
            "scope": item.scope,
            "type": item.data_type,
            "size": item.size,
            "initial_value": item.initial_value,
        }
    )


def _event_json(event: Event) -> dict:
    return _compact(
        {
            "name": event.name,
            "scope": event.scope,
            "trigger": event.trigger,
            "tag": event.tag,
        }
    )


def chart_json(chart: Chart) -> dict:
    """Return one chart as the JSON document written next to its subsystem."""
    names, paths = _references(chart)
    scoped = _collapse(chart, names, paths)

    containers: dict[str, _Container] = {"": _Container("", "chart")}
    for state in chart.states:
        containers[state.ssid] = _Container(state.ssid, "state", state)
    for function in chart.functions:
        containers[function.ssid] = _Container(function.ssid, "function", function)

    def place(ssid: str) -> _Container:
        return containers.get(ssid) or containers[""]

    for state in chart.states:
        place(state.parent).states.append(state.ssid)
    for function in chart.functions:
        place(function.parent).functions.append(function.ssid)
    for scope, transitions in scoped.items():
        place(scope).transitions.extend(transitions)
    for note in chart.notes:
        place(note.parent).notes.append(note.text)
    for item in chart.data:
        if _is_function_interface(item):
            continue
        place(item.parent).data.append(_data_json(item))
    for event in chart.events:
        place(event.parent).events.append(_event_json(event))

    def render(container: _Container) -> dict:
        if container.kind == "state":
            payload = _state_json(container.item, names[container.ssid])
        elif container.kind == "function":
            payload = _function_json(container.item, names[container.ssid], chart.data)
        else:
            payload = {}
        if container.states:
            payload["states"] = [render(containers[ssid]) for ssid in container.states]
        if container.functions:
            payload["functions"] = [render(containers[ssid]) for ssid in container.functions]
        if container.transitions:
            payload["transitions"] = container.transitions
        if container.notes:
            payload["notes"] = container.notes
        if container.data:
            payload["data"] = container.data
        if container.events:
            payload["events"] = container.events
        return payload

    chart_level = render(containers[""])
    total_transitions = sum(len(items) for items in scoped.values())
    payload = {
        "schema": STATE_FLOW_SCHEMA,
        "chart": chart.name,
        "action_language": chart.action_language,
        "summary": {
            "states": len(chart.states),
            "functions": len(chart.functions),
            "notes": len(chart.notes),
            "transitions": total_transitions,
            "events": len(chart.events),
            "data": len([item for item in chart.data if not _is_function_interface(item)]),
        },
        **chart_level,
    }
    return payload
