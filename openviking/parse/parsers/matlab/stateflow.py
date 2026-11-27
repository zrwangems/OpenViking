# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Stateflow chart XML to structured JSON.

A chart is written the way a person reads it in Simulink: states nest the way
they nest on the canvas, each state carries its entry/during/exit/on actions
and the transitions drawn inside it, and every other chart component (MATLAB,
Simulink and graphical functions, truth tables, atomic subcharts and their
ports, junctions, note boxes, events, data, messages) sits in the container it
was drawn in.

Nothing in the output is a machine identifier. States, transitions and
everything else are referred to by name; when the same name is used more than
once in a chart, the reference is the path through the nesting that separates
them. Junctions have no name on the canvas, so a transition that runs through
one is written as the path it makes; a transition that enters a history
junction is written as a transition into the state whose substates it restores.
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

STATE_FLOW_SCHEMA = "ov.matlab.stateflow/4"

#: Elements that own a nested view. Everything below one of these belongs to it.
_CONTAINER_TAGS = {"chart", "state", "box", "function", "truthTable", "machine"}

#: Chart kinds Stateflow records; anything else is a plain state chart.
_CHART_TYPES = {
    "EML_CHART": "MATLAB function",
    "TRUTHTABLE_CHART": "truth table",
    "STATE_EVENT_TABLE_CHART": "state transition table",
}
_MACHINES = {"MOORE_MACHINE": "Moore", "MEALY_MACHINE": "Mealy"}
#: The language chart actions are written in, as Stateflow stores it. The
#: corpus settles the two numbers: charts with 2 use ``end``, ``~=`` and ``%``,
#: charts with 1 use ``//`` and ``!=``.
_ACTION_LANGUAGES = {"1": "C", "2": "MATLAB"}

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
_LINKS_GID = re.compile(r"\s*%GID[0-9a-fA-F_]+")

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
    is_subchart: bool = False
    generated: bool = False
    order: str = ""
    description: str = ""
    simulink_block: str = ""
    action_subsystem: bool = False
    history: bool = False
    ports: list[str] = field(default_factory=list)

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
    table: dict | None = None

    @property
    def signature(self) -> str:
        """The function's own declaration, as written in the chart or the script."""
        first = _first_line(self.script) if self.script.lstrip().startswith("function") else ""
        return first or _first_line(self.label)

    @property
    def name(self) -> str:
        return _function_name(self.signature)

    @property
    def body(self) -> str:
        return _function_body(self.script)

    @property
    def notifies(self) -> list[str]:
        return _unique(_CALL.findall(self.script))


@dataclass
class Port:
    ssid: str
    name: str
    state: str
    kind: str = ""

    @property
    def label(self) -> str:
        return self.name.strip()


@dataclass
class Junction:
    ssid: str
    junction_type: str
    parent: str = ""
    label: str = ""

    @property
    def is_history(self) -> bool:
        return self.junction_type == "HISTORY_JUNCTION"


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


# Type attributes Stateflow stores under props/type and props/type/fixpt.
_TYPE_PROP_NAMES = (
    "method",
    "primitive",
    "isSigned",
    "wordLength",
    "slope",
    "bias",
    "fractionLength",
)


@dataclass
class Data:
    ssid: str
    name: str
    scope: str
    data_type: str
    size: str
    initial_value: str = ""
    parent: str = ""
    range: list[str] = field(default_factory=list)
    logged: bool = False
    queue_length: str = ""
    queue_overflow: str = ""
    from_workspace: bool = False
    props: dict[str, str] = field(default_factory=dict)

    @property
    def is_message(self) -> bool:
        return bool(self.queue_length or self.queue_overflow)


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
    chart_type: str = "state chart"
    action_language: str = "未声明"
    parallel: bool = False
    sample_time: str = ""
    machine: str = ""
    variant: str = ""
    app: bool = False
    execute_at_initialization: bool = False
    initialize_output: bool = False
    states: list[State] = field(default_factory=list)
    functions: list[Function] = field(default_factory=list)
    notes: list[Note] = field(default_factory=list)
    junctions: list[Junction] = field(default_factory=list)
    transitions: list[Transition] = field(default_factory=list)
    data: list[Data] = field(default_factory=list)
    events: list[Event] = field(default_factory=list)
    ports: list[Port] = field(default_factory=list)


def _props(element) -> dict[str, str]:
    return {p.get("Name"): p.text or "" for p in element.findall("./P") if p.get("Name")}


def _flag(props: dict[str, str], key: str) -> bool:
    return props.get(key, "") == "1"


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


def _function_name(signature: str) -> str:
    body = signature.removeprefix("function").strip()
    matched = _SIGNATURE.match(body) or _CALL_SIGNATURE.match(body)
    return matched.group("name") if matched else body


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
            # After a value a single quote is MATLAB's transpose (x'), not the
            # start of a string; reading it as one swallows the rest of the block.
            previous = text[index - 1] if index else ""
            if char == "'" and (previous.isalnum() or previous in "_)]}.'"):
                index += 1
                continue
            quote = char
        elif char == opener:
            depth += 1
        elif char == closer:
            depth -= 1
            if depth == 0:
                return text[start + 1 : index], index + 1
        index += 1
    return text[start + 1 :], len(text)


_LEADING_COMMENT = re.compile(
    r"\s*((?://[^\n]*|/\*.*?\*/|(?:^[ \t]*%[^\n]*)[ \t]*(?:\n|$))\s*)+", re.S
)


def _leading_comment(label: str) -> re.Match | None:
    """The comment a transition label starts with, which prefaces the guard."""
    matched = _LEADING_COMMENT.match(label)
    if matched is None or not matched.group(0).strip():
        return None
    return matched


def transition_label(label: str) -> dict[str, str]:
    """Split a transition label into event, condition, condition action and action.

    The order in a Stateflow transition label is
    ``event [condition] {condition action} / transition action``; brackets and
    braces only count at the top level, so MATLAB indexing inside a condition or
    a ``...`` line continuation stays in its block.
    """
    comment = _leading_comment(label)
    if comment:
        label = label[comment.end() :]
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
        "comment": " ".join(comment.group(0).split()) if comment else "",
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


#: Stateflow can store a label as Qt rich text: a whole HTML document whose
#: styling says nothing about the chart. Only the words in it matter.
_RICH_TEXT = re.compile(
    r"(?is)<!doctype\s+html|<html\b"
    r"|</?(?:body|head|style|p|span|div|br|li|ul|ol|table|tr|td|b|i|font)\b"
)


def _label_text(label: str) -> str:
    """The words of a label, with any rich-text markup and its styling removed.

    Styling is the trap: keeping it puts font names, sizes and colours into a
    state's name or into the text of a note. An ordinary label never contains
    markup, so it comes back unchanged, and the ``<`` of a condition stays.
    """
    if not label or not _RICH_TEXT.search(label):
        return label
    text = re.sub(r"(?is)<!doctype[^>]*>", "", label)
    text = re.sub(r"(?is)<(style|head)\b.*?</\1>", "", text)
    text = re.sub(r"(?i)<br\s*/?>|</(?:p|div|li|tr)\s*>", "\n", text)
    text = re.sub(r"<[^>]*>", "", text)
    lines = (re.sub(r"[ \t]+", " ", line).strip() for line in html.unescape(text).splitlines())
    return "\n".join(line for line in lines if line)


def _description(value: str) -> str:
    text = _LINKS_GID.sub("", value)
    return text.replace("{}", "").strip()


def _truth_table(element) -> dict:
    """Read a truth table's conditions, decisions and actions.

    Stateflow stores the table as two cell arrays: one row per condition (its
    name, its test, then a ``T``/``F``/``-`` per decision column) followed by a
    row that names the action of each column, and one row per action.
    """

    def cells(prop: str) -> tuple[list[str], int, int]:
        array = next(
            (item for item in element.findall("./Array") if item.get("PropName") == prop), None
        )
        if array is None:
            return [], 0, 0
        dimension = (array.get("Dimension") or "0*0").split("*")
        rows, columns = int(dimension[0]), int(dimension[1])
        return [(cell.text or "") for cell in array.findall("./Cell")], rows, columns

    predicates, rows, columns = cells("predicateArray")
    actions, action_rows, action_columns = cells("actionArray")
    if not predicates or not rows:
        return {}

    def at(values: list[str], row: int, column: int, height: int) -> str:
        index = row + column * height
        return values[index].strip() if index < len(values) else ""

    conditions = [
        {
            "name": at(predicates, row, 0, rows),
            "test": at(predicates, row, 1, rows),
            "values": [at(predicates, row, column, rows) for column in range(2, columns)],
        }
        for row in range(rows - 1)
    ]
    decisions = [at(predicates, rows - 1, column, rows) for column in range(2, columns)]
    return _compact(
        {
            "conditions": [item for item in (_compact(c) for c in conditions) if item],
            "decisions": [item for item in decisions if item],
            "actions": [
                _compact(
                    {
                        "name": at(actions, row, 0, action_rows),
                        "action": at(actions, row, 1, action_rows),
                    }
                )
                for row in range(action_rows)
            ]
            if action_columns
            else [],
        }
    )


def _parse_chart(root, member: str) -> Chart:
    props = _props(root)
    chart = Chart(
        name=props.get("name", Path(member).stem),
        chart_type=_CHART_TYPES.get(props.get("type", ""), "state chart"),
        action_language=_ACTION_LANGUAGES.get(
            props.get("actionLanguage", ""), "未声明"
        ),
        parallel=props.get("decomposition") == "SET_CHART",
        sample_time=props.get("sampleTime", ""),
        machine=_MACHINES.get(props.get("stateMachineType", ""), ""),
        execute_at_initialization=_flag(props, "executeAtInitialization"),
        initialize_output=_flag(props, "initializeOutput"),
    )
    variant = root.find("./variant")
    if variant is not None:
        chart.variant = _props(variant).get("activationTime", "")
    app = root.find("./stateflowApp")
    if app is not None and _flag(_props(app), "isApp"):
        chart.app = True

    parents = {child: parent for parent in root.iter() for child in parent}
    ports: list[Port] = []

    for element in root.iter():
        tag = element.tag
        if tag == "port":
            element_props = _props(element)
            ports.append(
                Port(
                    ssid=element.get("SSID") or element.get("id") or "",
                    name=_label_text(element_props.get("labelString", "")),
                    state=element_props.get("parent", ""),
                    kind=element_props.get("pType", ""),
                )
            )
            continue
        if tag == "truthTable":
            # Normally a truth table is the body of a FUNC_STATE, which reads it
            # itself; one drawn on its own is a truth table function.
            owner = parents.get(element)
            if owner is not None and _props(owner).get("type") == "FUNC_STATE":
                continue
            chart.functions.append(
                _parse_function(element, _props(element), _container(parents, element, root))
            )
            continue
        if tag not in {"state", "box", "junction", "transition", "data", "event"}:
            continue
        element_props = _props(element)
        parent = _container(parents, element, root)
        if tag in {"state", "box"}:
            state_type = element_props.get("type", "BOX" if tag == "box" else "未知")
            if _flag(element_props, "isNoteBox"):
                chart.notes.append(
                    Note(
                        ssid=element.get("SSID", ""),
                        text=_label_text(element_props.get("labelString", "")),
                        parent=parent,
                    )
                )
            elif state_type == "FUNC_STATE":
                chart.functions.append(_parse_function(element, element_props, parent))
            else:
                chart.states.append(
                    State(
                        ssid=element.get("SSID", ""),
                        label=_label_text(element_props.get("labelString", "")),
                        state_type=state_type,
                        decomposition=element_props.get("decomposition", ""),
                        parent=parent,
                        active_state_output=_activity_output(element),
                        is_box=tag == "box" or state_type == "GROUP_STATE",
                        is_subchart=element_props.get("superState") == "SUBCHART",
                        generated=_flag(element_props, "isAutoCreated")
                        or _autogen(element),
                        order=element_props.get("executionOrder", ""),
                        description=_description(element_props.get("description", "")),
                        **(_simulink_state(element, element_props)),
                    )
                )
        elif tag == "junction":
            chart.junctions.append(
                Junction(
                    ssid=element.get("SSID", ""),
                    junction_type=element_props.get("type", ""),
                    parent=parent,
                    label=_label_text(element_props.get("labelString", "")).strip(),
                )
            )
        elif tag == "transition":
            source = element.find("./src/P[@Name='SSID']")
            destination = element.find("./dst/P[@Name='SSID']")
            chart.transitions.append(
                Transition(
                    ssid=element.get("SSID", ""),
                    source=source.text if source is not None and source.text else "",
                    destination=destination.text
                    if destination is not None and destination.text
                    else "",
                    label=_label_text(element_props.get("labelString", "")),
                    order=element_props.get("executionOrder", "未声明"),
                    scope=parent,
                )
            )
        elif tag == "data":
            chart.data.append(_parse_data(element, element_props, parent))
        elif tag == "event":
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

    chart.ports = ports
    for junction in chart.junctions:
        if junction.is_history:
            for state in chart.states:
                if state.ssid == junction.parent:
                    # A history junction is the state's memory: re-entering it
                    # resumes the substate that was active last time.
                    state.history = True
    for state in chart.states:
        state.ports = _unique(
            [port.label for port in ports if port.state == state.ssid and port.label]
        )
    return chart


def _autogen(element) -> bool:
    autogen = element.find("./autogen")
    return autogen is not None and _flag(_props(autogen), "isAutoCreated")


def _activity_output(element) -> str:
    active = element.find("./activeStateOutput")
    return _props(active).get("activityMode", "") if active is not None else ""


def _simulink_state(element, element_props: dict[str, str]) -> dict:
    simulink = element.find("./simulink")
    if simulink is None:
        return {}
    simulink_props = _props(simulink)
    if not (_flag(simulink_props, "isComponent") or _flag(simulink_props, "isActionSubsystem")):
        return {}
    return {
        "simulink_block": simulink_props.get("blockName", ""),
        "action_subsystem": _flag(simulink_props, "isActionSubsystem"),
    }


def _parse_function(element, element_props: dict[str, str], parent: str) -> Function:
    simulink = element.find("./simulink")
    eml = element.find("./eml")
    table = element if element.tag == "truthTable" else element.find("./truthTable")
    eml_props = _props(eml) if eml is not None else {}
    simulink_props = _props(simulink) if simulink is not None else {}
    if _flag(eml_props, "isEML"):
        kind = "matlab"
    elif _flag(simulink_props, "isSimulinkFcn"):
        kind = "simulink"
    elif table is not None:
        kind = "truth_table"
    else:
        kind = "graphical"
    return Function(
        ssid=element.get("SSID") or element.get("id") or "",
        label=_label_text(element_props.get("labelString", "")),
        kind=kind,
        parent=parent,
        block=simulink_props.get("blockName", ""),
        script=eml_props.get("script", ""),
        properties={
            item.get("Name"): item.text or ""
            for item in (table.iter("P") if table is not None else [])
            if item.get("Name") and item.get("Name") not in {"isTruthTable", "useEML", "checksum"}
        },
        table=_truth_table(table) if table is not None else None,
    )


def _data_type_props(element) -> dict[str, str]:
    """Keep the type attributes that describe precision and scaling."""
    type_node = element.find("./props/type")
    if type_node is None:
        return {}
    found = {
        item.get("Name"): item.text or ""
        for item in type_node.findall("./P")
        if item.get("Name")
    }
    fixpt = type_node.find("./fixpt")
    if fixpt is not None:
        found.update(
            {
                item.get("Name"): item.text or ""
                for item in fixpt.findall("./P")
                if item.get("Name")
            }
        )
    return {name: found[name] for name in _TYPE_PROP_NAMES if found.get(name)}


def _parse_data(element, element_props: dict[str, str], parent: str) -> Data:
    props = element.find("./props")
    size = element.find("./props/array/P[@Name='size']")
    initial = element.find("./props/P[@Name='initialValue']")
    minimum = element.find("./props/range/P[@Name='minimum']")
    maximum = element.find("./props/range/P[@Name='maximum']")
    logging = element.find("./loggingInfo")
    message = element.find("./message")
    message_props = _props(message) if message is not None else {}
    return Data(
        ssid=element.get("SSID", ""),
        name=element.get("name", ""),
        scope=element_props.get("scope", "未声明"),
        data_type=element_props.get("dataType", "未声明"),
        size=size.text if size is not None and size.text else "未声明",
        initial_value=initial.text if initial is not None and initial.text else "",
        parent=parent,
        range=[
            item.text or ""
            for item in (minimum, maximum)
            if item is not None and item.text is not None
        ],
        logged=logging is not None and _flag(_props(logging), "logSignal"),
        queue_length=message_props.get("queueLength", ""),
        queue_overflow=message_props.get("queueOverflowDiagnostic", ""),
        from_workspace=_flag(_props(props) if props is not None else {}, "initFromWorkspace"),
        props=_data_type_props(element),
    )


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
        "comment": parts["comment"],
        "event": parts["event"],
        "condition": parts["condition"],
        "condition_action": parts["condition_action"],
        "action": parts["transition_action"],
    }


@dataclass
class _Path:
    steps: list[Transition]
    node: str
    #: "state" for a state, "loop" for a junction the path comes back to,
    #: "dead-end" for a junction nothing continues from, "history" for a
    #: history junction.
    ends: str


def _junction_paths(
    transition: Transition,
    out_edges: dict[str, list[Transition]],
    junction_ssids: dict[str, Junction],
) -> list[_Path]:
    """Follow a transition through the junctions it enters.

    Returns the transitions it passes and where it ends; a junction that
    branches yields one entry per branch. A history junction ends the path by
    restoring the substates of the state that owns it, and a path that loops
    back through a junction it already passed ends at that junction.
    """
    found: list[_Path] = []

    def walk(prefix: list[Transition], node: str, seen: frozenset[str]) -> None:
        if len(found) >= _MAX_JUNCTION_PATHS or len(prefix) > _MAX_JUNCTION_HOPS:
            raise _Overflow
        junction = junction_ssids.get(node)
        if junction is None:
            found.append(_Path(prefix, node, "state"))
            return
        if junction.is_history:
            found.append(_Path(prefix, node, "history"))
            return
        edges = out_edges.get(node, [])
        if not edges:
            found.append(_Path(prefix, node, "dead-end"))
            return
        for edge in edges:
            if edge.destination in seen:
                found.append(_Path([*prefix, edge], edge.destination, "loop"))
                continue
            walk([*prefix, edge], edge.destination, seen | {edge.destination})

    first = transition.destination
    walk([transition], first, frozenset({first}) if first in junction_ssids else frozenset())
    return found


def _port_refs(chart: Chart, ref: dict[str, str]) -> dict[str, str]:
    """Name every atomic subchart port; a port without a label gets its owner."""
    ports: dict[str, str] = {}
    unnamed: Counter[str] = Counter()
    for port in chart.ports:
        owner = ref.get(port.state, "")
        if port.label:
            ports[port.ssid] = port.label
        else:
            unnamed[owner] += 1
            # The port has no label of its own, so it is named the way every
            # other unnamed component is: an English ordinal inside its owner.
            ports[port.ssid] = (
                f"{owner} port {unnamed[owner]}" if owner else f"port {unnamed[owner]}"
            )
    return ports


def _flow_scopes(chart: Chart) -> set[str]:
    """Containers whose junctions describe a flow rather than a state change.

    A flow is what runs between states: steps, branching junctions, loops and
    ends. A container holds one when its junction graph has a way on that never
    reaches a state (a dead end) or comes back on itself (a loop); otherwise its
    junctions only route a transition from one state to another and the
    transition reads better on its own.
    """
    junctions = {junction.ssid: junction for junction in chart.junctions}
    outgoing: dict[str, list[Transition]] = defaultdict(list)
    incoming: dict[str, list[Transition]] = defaultdict(list)
    for transition in chart.transitions:
        outgoing[transition.source].append(transition)
        if transition.destination in junctions:
            incoming[transition.destination].append(transition)

    def reaches_state(start: str) -> bool:
        stack, seen = [start], set()
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            for transition in outgoing.get(node, []):
                target = transition.destination
                if target not in junctions:
                    return True
                stack.append(target)
        return False

    def has_cycle(start: str) -> bool:
        stack = [(start, frozenset())]
        while stack:
            node, path = stack.pop()
            for transition in outgoing.get(node, []):
                target = transition.destination
                if target not in junctions:
                    continue
                if target in path:
                    return True
                stack.append((target, path | {target}))
        return False

    scopes: set[str] = set()
    for ssid, junction in junctions.items():
        if not incoming.get(ssid):
            continue
        if not outgoing.get(ssid) or has_cycle(ssid):
            scopes.add(junction.parent or "")
    return scopes


def _inside(parents: dict[str, str], ssid: str, container: str) -> bool:
    current = parents.get(ssid, "")
    seen: set[str] = set()
    while current and current not in seen:
        if current == container:
            return True
        seen.add(current)
        current = parents.get(current, "")
    return False


def _collapse(
    chart: Chart,
    names: dict[str, str],
    paths: dict[str, str],
    overflowed: set[str] | None = None,
) -> dict[str, list[dict]]:
    """Write each transition as the state-to-state path it describes.

    Junctions carry no name on the canvas, so instead of naming them the
    transition runs from its source through the junction's own condition and
    action to the state it ends in; a junction that branches becomes one entry
    per branch, each with its own order.
    """
    ref = _reference(names, paths)
    junction_ssids = {junction.ssid: junction for junction in chart.junctions}
    out_edges: dict[str, list[Transition]] = defaultdict(list)
    for transition in chart.transitions:
        if transition.source in junction_ssids:
            out_edges[transition.source].append(transition)
    for edges in out_edges.values():
        edges.sort(key=_order_key)

    port_refs = _port_refs(chart, ref)

    def endpoint(node: str, history: bool = False) -> tuple[str | None, dict]:
        """Resolve one end of a transition to what the reader should see."""
        junction = junction_ssids.get(node)
        if junction is not None and junction.is_history:
            return ref.get(junction.parent), {"history": True}
        if node in port_refs:
            return port_refs[node], {"port": True}
        return ref.get(node), {}

    def raw(transition: Transition, destination: str) -> dict:
        source, source_flags = endpoint(transition.source)
        target, target_flags = endpoint(destination)
        payload = {
            "from": source,
            "to": target,
            **source_flags,
            **target_flags,
            **_transition_parts(transition),
            "order": transition.order,
        }
        if not transition.source:
            payload.pop("from")
            payload["initial"] = True
        # A junction has no name on the canvas, so an end that is one is left
        # out rather than given a number the chart does not show.
        if source is None:
            payload.pop("from", None)
        if target is None:
            payload.pop("to", None)
        return _compact(payload)

    scoped: dict[str, list[dict]] = defaultdict(list)
    followed: set[str] = set()
    for transition in chart.transitions:
        if transition.source in junction_ssids:
            continue
        try:
            found = _junction_paths(transition, out_edges, junction_ssids)
        except _Overflow:
            # The junctions branch too far to be written as whole paths; the
            # container is then better read as a flow chart.
            if overflowed is not None:
                overflowed.add(transition.scope)
            scoped[transition.scope].append(raw(transition, transition.destination))
            continue
        for path in found:
            prefix, destination, ends = path.steps, path.node, path.ends
            followed.update(step.ssid for step in prefix[1:])
            head = prefix[0]
            source, source_flags = endpoint(head.source)
            target, target_flags = endpoint(destination)
            payload = {
                "from": source,
                "to": target,
                **source_flags,
                **_transition_parts(head),
                "order": head.order,
            }
            if ends == "loop":
                # The path comes back to a junction it already passed, so it
                # stops there; the junction is not named, it is marked.
                payload["loop"] = True
            elif ends != "dead-end":
                payload.update(target_flags)
            steps = [
                _compact({**_transition_parts(step), "order": step.order})
                for step in prefix[1:]
            ]
            steps = [
                step
                for step in steps
                if set(step) - {"order"}
            ]
            if steps:
                payload["via"] = steps
            if not payload["from"]:
                payload.pop("from")
                payload["initial"] = True
            if not payload.get("to"):
                # The path ends on a junction nothing continues from: inside a
                # function that is the end of its flow, which returns; at chart
                # level it is the entry action itself.
                payload.pop("to", None)
                if ends == "dead-end" and _flow_ends_here(chart, head.scope):
                    payload["return"] = True
            scoped[transition.scope].append(_compact(payload))

    # A junction nothing leads into still carries a condition of its own; keep it
    # rather than dropping what the chart says.
    for transition in chart.transitions:
        if transition.source in junction_ssids and transition.ssid not in followed:
            scoped[transition.scope].append(raw(transition, transition.destination))
            followed.add(transition.ssid)
    return scoped


def _flow_ends_here(chart: Chart, scope: str) -> bool:
    """Whether running into a junction with no way on ends the flow.

    Inside a function that is the function returning. A chart that is one flow
    chart (no states, several decisions) ends there too. A single dangling
    junction in a chart that wraps one function is a drawing artifact instead,
    so nothing is said about it.
    """
    if scope and _in_function(chart, scope):
        return True
    return not chart.states and len(chart.junctions) > 1


def _in_function(chart: Chart, ssid: str) -> bool:
    functions = {function.ssid for function in chart.functions}
    parent = {state.ssid: state.parent for state in chart.states}
    current = ssid
    seen: set[str] = set()
    while current and current not in seen:
        if current in functions:
            return True
        seen.add(current)
        current = parent.get(current, "")
    return False


def _as_list(value) -> list:
    return list(value) if isinstance(value, list) else [value]


def _flow_statements(
    chart: Chart,
    scope: str,
    names: dict[str, str],
    ports: dict[str, str],
) -> dict:
    """Write a flow chart as the if/else structure its junctions encode.

    A flow chart is a graph of steps and junctions. Read as text, the junctions
    say nothing on their own: a junction with one way on is a link, and one with
    several ways on is the place where the chart picks a branch. So the links
    are followed through and every branching junction becomes a list of cases
    in the order the chart tries them, the way a person reads the diagram. A
    step that jumps back to a branch already taken is marked ``loop``.
    """
    junction_ssids = {junction.ssid for junction in chart.junctions}
    edges: dict[str, list[Transition]] = defaultdict(list)
    for transition in chart.transitions:
        if transition.scope == scope:
            edges[transition.source].append(transition)
    for items in edges.values():
        items.sort(key=_order_key)

    def effect(node: str) -> dict | None:
        if node in ports:
            return {"to": ports[node], "port": True}
        if node in names:
            return {"to": names[node]}
        return None

    def details(transition: Transition) -> dict:
        parts = transition_label(transition.label)
        body = [text for text in (parts["condition_action"], parts["transition_action"]) if text]
        payload = {
            "comment": parts["comment"],
            "event": parts["event"],
            "when": parts["condition"],
            "do": body[0] if len(body) == 1 else body,
        }
        return _compact(payload)

    def merge(statement: dict, following: dict) -> dict:
        """Join two steps that happen one after the other."""
        merged = dict(statement)
        for key, value in following.items():
            if key in merged and key in {"do", "then"}:
                merged[key] = _as_list(merged[key]) + _as_list(value)
            else:
                merged.setdefault(key, value)
        return merged

    def conflicting(statement: dict, following: dict) -> bool:
        """Whether two steps each say something about how they are entered."""
        return bool(set(statement) & set(following) & {"when", "event", "comment"})

    def walk(transition: Transition, seen: frozenset[str]) -> list[dict]:
        """The steps that follow one transition, in the order they run."""
        steps = [details(transition)]
        node = transition.destination
        while True:
            reached = effect(node)
            if reached is not None:
                steps[-1] = merge(steps[-1], reached)
                return steps
            if node not in junction_ssids:
                return steps
            if node in seen:
                steps[-1] = merge(steps[-1], {"loop": True})
                return steps
            onwards = edges.get(node, [])
            if not onwards:
                # Nothing continues from here: the flow ends, which is the
                # function returning or the chart being done with this step.
                return steps
            if len(onwards) == 1:
                step = onwards[0]
                detail = details(step)
                if conflicting(steps[-1], detail):
                    steps.append(detail)
                else:
                    steps[-1] = merge(steps[-1], detail)
                node = step.destination
                continue
            branches = cases(onwards, seen | {node})
            if set(steps[-1]) & {"do", "when"}:
                steps.append({"cases": branches})
            else:
                steps[-1] = merge(steps[-1], {"cases": branches})
            return steps

    def cases(onwards: list[Transition], seen: frozenset[str]) -> list[dict]:
        built = []
        for transition in onwards:
            steps = walk(transition, seen)
            if not steps:
                continue
            head, *rest = steps
            if rest:
                head = merge(head, {"then": rest})
            if not head:
                # The branch does nothing and goes nowhere: it is the way out
                # of the chart, which needs no line of its own.
                continue
            built.append(head)
        # ``else if`` chains read as one list of cases: a branch that only holds
        # another list of cases is lifted into this one.
        if len(built) > 1 and list(built[-1]) == ["cases"]:
            built[-1:] = built[-1]["cases"]
        return built

    entries = {
        source: items for source, items in edges.items() if source not in junction_ssids
    }
    if len(entries) == 1 and "" in entries:
        # Everything starts at the chart entry: the flow is one statement list.
        statements: list[dict] = []
        for transition in entries[""]:
            statements.extend(walk(transition, frozenset()))
        if not statements:
            return {}
        first, *rest = statements
        payload: dict[str, object] = dict(first)
        if rest:
            payload["then"] = rest
        return payload

    # Some steps start from a state (a state that holds a flow chart), so each
    # starting point becomes one entry of the flow.
    body: list[dict] = []
    for source in sorted(entries, key=lambda item: names.get(item, "")):
        for transition in entries[source]:
            steps = walk(transition, frozenset())
            if not steps:
                continue
            head, *rest = steps
            entry = {"from": names.get(source)} if source else {}
            head = merge(entry, head)
            if rest:
                head["then"] = _as_list(head.get("then", [])) + rest
            body.append(head)
    return {"entries": body} if body else {}


def state_transition_count(chart: Chart) -> int:
    """Count the transitions drawn from one state to another.

    A junction is a point on a transition, not a transition of its own, so an
    arrow leaving a state that branches at a junction counts once for each
    state it can reach. Segments that only run between junctions, the steps of
    a flow chart (which change no state) and a transition in or out of a
    subchart port (which ends outside the chart's states) are left out: what is
    counted is the chart's state graph, the same thing a reader traces on the
    canvas, so the number is comparable between charts.
    """
    junctions = {junction.ssid: junction for junction in chart.junctions}
    states = {state.ssid for state in chart.states}
    out_edges: dict[str, list[Transition]] = defaultdict(list)
    for transition in chart.transitions:
        if transition.source in junctions:
            out_edges[transition.source].append(transition)
    total = 0
    for transition in chart.transitions:
        if transition.source in junctions:
            continue
        reached: set[str] = set()
        stack, seen = [transition.destination], set()
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            junction = junctions.get(node)
            if junction is not None:
                if junction.is_history:
                    # Entering a history junction resumes the substates of the
                    # state that owns it, so the transition ends in that state.
                    reached.add(junction.parent)
                else:
                    stack.extend(edge.destination for edge in out_edges.get(node, []))
            elif node in states:
                reached.add(node)
        total += len(reached & states)
    return total


def _is_function_interface(item: Data) -> bool:
    """Function arguments live in the function entry, not in the chart's data list."""
    return item.scope in {"FUNCTION_INPUT_DATA", "FUNCTION_OUTPUT_DATA"}


def _state_json(state: State, name: str) -> dict:
    parallel = state.state_type == "AND_STATE" or state.decomposition in {
        "PARALLEL_STATE",
        "SET_STATE",
    }
    payload = {
        "name": name,
        "parallel": True if parallel and not state.is_box else "",
        "box": True if state.is_box else "",
        "subchart": True if state.is_subchart else "",
        "history": True if state.history else "",
        "generated": True if state.generated else "",
        "order": state.order,
        "description": state.description,
        "active_state_output": state.active_state_output,
        "simulink_block": state.simulink_block,
        "action_subsystem": True if state.action_subsystem else "",
        "ports": state.ports,
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
        "truth_table": function.table or {},
        # For a truth table the table is the source and the body is what
        # Stateflow generates from it; both are kept, the table first.
        "body": function.body,
    }
    return _compact(payload)


def _data_json(item: Data) -> dict:
    return _compact(
        {
            "name": item.name,
            "scope": item.scope,
            "type": item.data_type,
            "props": item.props,
            "size": item.size,
            "initial_value": item.initial_value,
            "range": item.range,
            "logged": True if item.logged else "",
            "from_workspace": True if item.from_workspace else "",
            "message": _compact(
                {
                    "queue_length": item.queue_length,
                    "queue_overflow": item.queue_overflow,
                }
            )
            if item.is_message
            else {},
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
    port_refs = _port_refs(chart, _reference(names, paths))
    flow_scopes = _flow_scopes(chart)
    if not chart.states and chart.chart_type in {"MATLAB function", "truth table"}:
        # These charts exist to wrap one function; the call that runs it is
        # plumbing rather than behaviour, so it is left out.
        scoped: dict[str, list[dict]] = {}
    else:
        overflowed: set[str] = set()
        collapsed = _collapse(chart, names, paths, overflowed)
        flow_scopes |= overflowed
        scoped = {
            scope: items for scope, items in collapsed.items() if scope not in flow_scopes
        }
    flows = {
        scope: _flow_statements(
            chart,
            scope,
            names,
            port_refs,
        )
        for scope in flow_scopes
    }
    flows = {scope: flow for scope, flow in flows.items() if flow}

    containers: dict[str, _Container] = {"": _Container("", "chart")}
    for state in chart.states:
        containers[state.ssid] = _Container(state.ssid, "state", state)
    for function in chart.functions:
        if function.ssid:
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
        if container.ssid in flows:
            payload["flow"] = flows[container.ssid]
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
    messages = len([item for item in chart.data if item.is_message])
    return _compact({
        "schema": STATE_FLOW_SCHEMA,
        "chart": chart.name,
        "type": chart.chart_type,
        "parallel": True if chart.parallel else "",
        "action_language": chart.action_language,
        "sample_time": chart.sample_time,
        "machine": chart.machine,
        "variant": chart.variant,
        "app": True if chart.app else "",
        "execute_at_initialization": True if chart.execute_at_initialization else "",
        "initialize_output": True if chart.initialize_output else "",
        "summary": {
            "states": len(chart.states),
            "functions": len(chart.functions),
            "notes": len(chart.notes),
            "transitions": state_transition_count(chart),
            "events": len(chart.events),
            "data": len([item for item in chart.data if not _is_function_interface(item)]),
            "messages": messages,
        },
        **chart_level,
    })
