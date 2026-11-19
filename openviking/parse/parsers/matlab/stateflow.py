# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Stateflow chart XML to structured JSON states, transitions and data."""

from __future__ import annotations

import re
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

from defusedxml import ElementTree as ET

from openviking.parse.parsers.matlab._zip import read_xml_member


@dataclass
class State:
    ssid: str
    label: str
    state_type: str
    parent: str = ""

    @property
    def name(self) -> str:
        return next((line.strip() for line in self.label.splitlines() if line.strip()), self.ssid)

    @property
    def actions(self) -> str:
        lines = self.label.splitlines()
        return "\n".join(lines[1:]).strip() if len(lines) > 1 else ""


@dataclass
class Transition:
    ssid: str
    source: str
    destination: str
    label: str
    order: str


@dataclass
class Data:
    ssid: str
    name: str
    scope: str
    data_type: str
    size: str


@dataclass
class Chart:
    chart_id: str
    name: str
    action_language: str
    states: list[State] = field(default_factory=list)
    transitions: list[Transition] = field(default_factory=list)
    data: list[Data] = field(default_factory=list)


def _props(element) -> dict[str, str]:
    return {p.get("Name"): p.text or "" for p in element.findall("./P") if p.get("Name")}


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
            props = _props(root)
            chart = Chart(
                chart_id=root.get("id", Path(name).stem.removeprefix("chart_")),
                name=props.get("name", Path(name).stem),
                action_language=props.get("actionLanguage", "未声明"),
            )
            for element in root.findall(".//state"):
                state_props = _props(element)
                chart.states.append(
                    State(
                        ssid=element.get("SSID", ""),
                        label=state_props.get("labelString", ""),
                        state_type=state_props.get("type", "未知"),
                        parent=state_props.get("subviewer", chart.chart_id),
                    )
                )
            for element in root.findall(".//transition"):
                transition_props = _props(element)
                source = element.find("./src/P[@Name='SSID']")
                destination = element.find("./dst/P[@Name='SSID']")
                chart.transitions.append(
                    Transition(
                        ssid=element.get("SSID", ""),
                        source=source.text if source is not None and source.text else "",
                        destination=destination.text
                        if destination is not None and destination.text
                        else "",
                        label=transition_props.get("labelString", ""),
                        order=transition_props.get("executionOrder", "未声明"),
                    )
                )
            # Chart-level data defines the external interface. Data nested below
            # Simulink Function states belongs to those functions, not this chart.
            for element in root.findall("./Children/data"):
                data_props = _props(element)
                size = element.find("./props/array/P[@Name='size']")
                chart.data.append(
                    Data(
                        ssid=element.get("SSID", ""),
                        name=element.get("name", ""),
                        scope=data_props.get("scope", "未声明"),
                        data_type=data_props.get("dataType", "未声明"),
                        size=size.text if size is not None and size.text else "未声明",
                    )
                )
            charts.append(chart)
    return charts


def chart_system_path(chart: Chart) -> str:
    """Return the Simulink subsystem names used to place this chart."""
    return "/".join(_slug(part) for part in chart.name.split("/") if part)


def _slug(value: str) -> str:
    value = re.sub(r"[^\w.-]+", "_", value, flags=re.UNICODE).strip("._")
    return value or "stateflow"


def chart_json(chart: Chart) -> dict:
    """Return the chart as a JSON object with states, transitions and data."""
    states = {state.ssid: state for state in chart.states}
    return {
        "schema": "ov.matlab.stateflow/1",
        "chart_id": chart.chart_id,
        "chart": chart.name,
        "action_language": chart.action_language,
        "states": [
            {
                "id": state.ssid,
                "name": state.name,
                "parent": state.parent,
                "parent_name": states[state.parent].name
                if state.parent in states
                else "Chart",
                "type": state.state_type,
                "label": state.label,
                "actions": state.actions,
            }
            for state in chart.states
        ],
        "transitions": [
            {
                "id": transition.ssid,
                "from": transition.source,
                "from_name": states[transition.source].name
                if transition.source in states
                else "[*]",
                "to": transition.destination,
                "to_name": states[transition.destination].name
                if transition.destination in states
                else "[*]",
                "label": transition.label,
                "order": transition.order,
            }
            for transition in chart.transitions
        ],
        "data": [
            {
                "id": item.ssid,
                "name": item.name,
                "scope": item.scope,
                "data_type": item.data_type,
                "size": item.size,
            }
            for item in chart.data
        ],
    }
