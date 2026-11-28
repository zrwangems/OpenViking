# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0

import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path
from xml.etree.ElementTree import fromstring as ET_fromstring

import pytest

from openviking.parse.output import LocalParseOutputStore, resolve_artifact_doc_root
from openviking.parse.parsers.directory import DirectoryParser
from openviking.parse.parsers.matlab import matlab_requested
from openviking.parse.parsers.matlab._zip import read_xml_member
from openviking.parse.parsers.matlab.figures import parse_figure
from openviking.parse.parsers.matlab.keydes import KeydesLibrary
from openviking.parse.parsers.matlab.mat import parse_mat, parse_mat_documents
from openviking.parse.parsers.matlab.parser import MatlabParser
from openviking.parse.parsers.matlab.slx import Block, parse_slx, system_json_documents
from openviking.parse.parsers.matlab.stateflow import (
    STATE_FLOW_SCHEMA,
    _label_text,
    _parse_chart,
    chart_json,
    parse_stateflow,
    transition_label,
)
from openviking.parse.parsers.matlab.structured import (
    parse_mlapp,
    parse_mldatx,
    parse_mlx_notebook,
    parse_requirement_set,
    parse_sldd_tree,
    protected_metadata,
    sldd_entry_rows,
)
from openviking.parse.parsers.matlab.workbook import parse_workbook, workbook_text
from openviking.parse.registry import ParserRegistry

SAMPLE = Path(__file__).parents[2] / "matlab_repos" / "matlab-ingest-fixture"
CONTROLLER = (
    SAMPLE
    / "model"
    / "VirtualVehicle"
    / "VirtualVehicle"
    / "Controller"
    / "HevIpsPowertrainController.slx"
)


def flatten(system):
    yield system
    for child in system.children:
        yield from flatten(child)


def test_slx_nested_systems_ports_parameters_and_branches():
    model = parse_slx(CONTROLLER)
    systems = list(flatten(model))
    documents = system_json_documents(model)

    assert len(systems) == 32
    assert len(documents) == len(systems)
    assert any(system.inputs for system in systems)
    assert any(system.outputs for system in systems)
    assert documents["main.json"]["type"] == "simulink-model"
    assert "IPS_Supervisory_Control/main.json" in documents
    assert "Accel_Pedal_to_Traction_Wheel_Torque_Request.json" in documents
    assert not any(path.endswith("/index.json") or path == "index.json" for path in documents)
    for path, document in documents.items():
        assert document["schema"] == "ov.matlab.simulink/1"
        assert document["type"] == (
            "simulink-model" if path == "main.json" else "simulink-subsystem"
        )
        assert isinstance(document["blocks"], list)
        assert isinstance(document["edges"], list)
        assert set(document) >= {"system", "system_ref", "subsystem_types", "children"}
        assert "```mermaid" not in json.dumps(document)
        for block in document["blocks"]:
            assert set(block) == {
                "name",
                "key",
                "description",
                "ports",
            }
        for edge in document["edges"]:
            assert set(edge) == {"from", "to", "signal"}
            assert isinstance(edge["from"], list) and len(edge["from"]) == 2
            assert edge["to"] and all(
                isinstance(target, list) and len(target) == 2 for target in edge["to"]
            )
        for child in document["children"]:
            assert set(child) == {"name", "path", "system_ref", "type"}

    total_rows = sum(len(document["edges"]) for document in documents.values())
    total_edges = sum(len(system.edges) for system in systems)
    assert 0 < total_rows <= total_edges
    assert any(
        len(edge["to"]) > 1
        for document in documents.values()
        for edge in document["edges"]
    )
    assert (
        documents["IPS_Supervisory_Control/Generator_Control.ON.GenControl/main.json"]["type"]
        == "simulink-subsystem"
    )
def test_system_json_carries_a_description_per_block_instead_of_parameters():
    documents = system_json_documents(parse_slx(CONTROLLER), language="zh-CN")
    power_path = next(
        path for path in documents if path.endswith("Mech_To_Elec_Power_Estimate.json")
    )
    power = documents[power_path]
    payload = json.dumps(power, ensure_ascii=False)
    assert "Lookup_n-D" in payload
    assert power["blocks"]
    assert all("params" not in block for block in power["blocks"])
    descriptions = [block["description"] for block in power["blocks"]]
    assert any("PlntEM2EffTbl" in text for text in descriptions)
    assert any("逼近 N 维函数" in text for text in descriptions)
    assert all("{" not in text for text in descriptions)
    assert power["coverage"]["described_blocks"] <= power["coverage"]["blocks"]
    assert len(payload) < 20_000

def test_block_descriptions_are_chinese_by_default():
    documents = system_json_documents(parse_slx(CONTROLLER))
    power_path = next(
        path for path in documents if path.endswith("Mech_To_Elec_Power_Estimate.json")
    )
    descriptions = [
        block["description"] for block in documents[power_path]["blocks"] if block["description"]
    ]
    assert descriptions
    assert any("逼近 N 维函数" in text for text in descriptions)


def test_keydes_default_language_is_chinese():
    library = KeydesLibrary()
    block = Block(sid="1", name="Gain", block_type="Gain", parameters={"Gain": "3.5"})
    _, description = library.describe(block)
    assert "将输入乘以常量" in description


def test_keydes_renders_instance_values_into_the_template():
    library = KeydesLibrary()
    block = Block(
        sid="1",
        name="Gain",
        block_type="Gain",
        parameters={"Gain": "100", "Multiplication": "Matrix(K*u)", "SampleTime": "-1"},
    )
    key, description = library.describe(block, "en")
    assert key == "Gain"
    assert "100" in description
    assert "matrix product" in description
    assert "{" not in description


def test_keydes_uses_the_english_template_for_parameter_names():
    library = KeydesLibrary()
    block = Block(sid="1", name="Gain", block_type="Gain", parameters={"Gain": "3.5"})
    _, description = library.describe(block, "zh-CN")
    assert "将输入乘以常量" in description
    assert "3.5" in description
    assert "{" not in description


def test_keydes_matches_documented_parameter_names_to_slx_names():
    library = KeydesLibrary()
    block = Block(
        sid="9",
        name="Lookup",
        block_type="Lookup_n-D",
        parameters={
            "NumberOfTableDimensions": "1",
            "Table": "Tbl",
            "BreakpointsForDimension1": "[1 2 3]",
        },
    )
    _, description = library.describe(block, "en")
    assert "Tbl" in description
    assert "[1 2 3]" in description


def test_keydes_leaves_blocks_without_a_template_undescribed():
    library = KeydesLibrary()
    unlinked = Block(
        sid="1",
        name="LPF",
        block_type="Reference",
        parameters={"SourceBlock": "autolibutils/LPF IC", "SourceType": ""},
    )
    assert library.describe(unlinked, "en") == ("LPF IC", None)
    assert library.describe(Block(sid="2", name="Sub", block_type="SubSystem"), "en") == (
        None,
        None,
    )

def test_slx_deduplicates_colliding_directory_names():
    model = parse_slx(CONTROLLER)
    documents = system_json_documents(model)
    assert len(documents) == len(set(documents))


def walk_states(node):
    for state in node.get("states", []):
        yield state
        yield from walk_states(state)


def walk_paths(node, prefix=()):
    for state in node.get("states", []):
        path = (*prefix, state["name"])
        yield "/".join(path), state
        yield from walk_paths(state, path)


def find_state(chart, name):
    return next(state for state in walk_states(chart) if state["name"] == name)


def find_by_path(chart, path):
    return next(state for current, state in walk_paths(chart) if current == path)


def all_transitions(node):
    yield from node.get("transitions", [])
    for state in node.get("states", []):
        yield from all_transitions(state)
    for function in node.get("functions", []):
        yield from all_transitions(function)


def all_data(node):
    yield from node.get("data", [])
    for state in node.get("states", []):
        yield from all_data(state)
    for function in node.get("functions", []):
        yield from all_data(function)


def all_flows(node):
    if "flow" in node:
        yield node["flow"]
    for state in node.get("states", []):
        yield from all_flows(state)
    for function in node.get("functions", []):
        yield from all_flows(function)


def walk_flow(flow):
    """Every statement of a flow document, nested cases included."""
    if "entries" in flow:
        for entry in flow["entries"]:
            yield from walk_flow(entry)
        return
    yield flow
    for statement in flow.get("then", []):
        yield from walk_flow(statement)
    for case in flow.get("cases", []):
        yield from walk_flow(case)


def all_functions(node):
    yield from node.get("functions", [])
    for state in node.get("states", []):
        yield from all_functions(state)
    for function in node.get("functions", []):
        yield from all_functions(function)


def keys_of(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from keys_of(item)
    elif isinstance(value, list):
        for item in value:
            yield from keys_of(item)


def test_stateflow_charts_name_every_component_and_keep_actions():
    charts = parse_stateflow(CONTROLLER)
    assert [chart.name for chart in charts] == [
        "IPS Supervisory Control",
        "IPS Supervisory Control/Operating_Modes.EngOnCalc/Check Power/Timer",
    ]

    timer = chart_json(charts[1])
    assert timer["schema"] == STATE_FLOW_SCHEMA
    assert timer["summary"] == {
        "states": 3,
        "functions": 0,
        "notes": 0,
        "transitions": 5,
        "events": 0,
        "data": 2,
        "messages": 0,
    }
    states = {state["name"]: state for state in timer["states"]}
    assert states["Wait"]["during"] == "Out = 0;"
    assert states["TimerDone"]["during"] == "Out = 1;"
    assert not any("states" in state for state in timer["states"])
    timed = next(item for item in timer["transitions"] if item.get("event") == "after(0.1, sec)")
    assert (timed["from"], timed["to"]) == ("Wait", "TimerDone")
    assert next(item for item in timer["transitions"] if item.get("condition") == "In")["from"] == (
        "StartTimer"
    )
    default = next(item for item in timer["transitions"] if item.get("initial"))
    assert "from" not in default
    assert default["to"] == "StartTimer"

    supervisory = chart_json(charts[0])
    operating = find_state(supervisory, "Operating_Modes")
    assert operating["parallel"] is True
    assert operating["entry"] == operating["during"]
    driving = find_state(supervisory, "Driving")
    assert driving in operating["states"]
    assert find_state(supervisory, "EV")["entry"] == "OpMode = 1;\nEngPwrCmd = 0;\nMotMode = 1;"
    assert find_state(supervisory, "EV") in driving["states"]
    assert find_state(supervisory, "Low_Power_Charge_Sustain") in find_state(
        supervisory, "HEV"
    )["states"]
    assert len(list(all_transitions(supervisory))) == 35
    # Names repeat below different parents, so those references carry the path.
    references = [
        item.get("from") for item in all_transitions(supervisory) if item.get("from")
    ] + [item.get("to") for item in all_transitions(supervisory) if item.get("to")]
    assert "Operating_Modes/Wait1" in references
    assert "Driving/Wait" not in references
    op_mode = find_state(supervisory, "Low_Power_Charge_Sustain")["functions"][0]
    assert op_mode["name"] == "OpMode3"
    assert op_mode["kind"] == "simulink"
    assert op_mode["block"].endswith("Low_Power_Charge_Sustain.OpMode3")
    assert op_mode["inputs"][:2] == ["WhlPwrCmd", "ChrgPwr"]
    assert op_mode["outputs"] == ["EngPwrCmd", "MotPwrCmd"]


def test_stateflow_data_keeps_type_precision_and_fixed_point_props():
    chart = chart_json(
        parse_stateflow(
            SAMPLE
            / "model"
            / "StateflowExamples"
            / "DashboardBoilerExample"
            / "sfDashboardBoiler.slx"
        )[0]
    )
    data = {item["name"]: item for item in all_data(chart)}
    assert data["reference"]["props"] == {
        "method": "SF_CUSTOM_INTEGER_TYPE",
        "primitive": "SF_DOUBLE_TYPE",
        "isSigned": "1",
        "wordLength": "8",
        "slope": "1",
        "bias": "-15",
    }
    assert data["temp"]["props"] == {
        "primitive": "SF_UINT16_TYPE",
        "isSigned": "1",
        "wordLength": "8",
        "slope": "0.390625",
        "bias": "-15",
    }


def test_stateflow_data_keeps_fraction_length_for_binary_point_types():
    chart = chart_json(
        parse_stateflow(
            SAMPLE
            / "model"
            / "StateflowExamples"
            / "FixedPointMandelbrotSetExample"
            / "sf_mandelbrot_fixpt.slx"
        )[0]
    )
    data = {item["name"]: item for item in all_data(chart)}
    assert data["c"]["props"] == {
        "method": "SF_CUSTOM_INTEGER_TYPE",
        "primitive": "SF_DOUBLE_TYPE",
        "isSigned": "1",
        "wordLength": "16",
        "slope": "2^0",
        "bias": "0",
        "fractionLength": "13",
    }
    assert data["cn"]["props"]["fractionLength"] == "26"


def test_stateflow_example_data_keeps_type_props():
    counts = {"data": 0, "wordLength": 0, "bias": 0, "slope": 0, "fractionLength": 0}
    for path in stateflow_examples():
        for chart in parse_stateflow(path):
            for item in chart.data:
                counts["data"] += 1
                for key in ("wordLength", "bias", "slope", "fractionLength"):
                    if key in item.props:
                        counts[key] += 1
    assert counts == {
        "data": 1365,
        "wordLength": 1134,
        "bias": 30,
        "slope": 22,
        "fractionLength": 29,
    }


def test_stateflow_sfx_keeps_hierarchy_notes_and_matlab_functions():
    chart = chart_json(parse_stateflow(SAMPLE / "model" / "TargetStateChart.sfx")[0])
    assert chart["schema"] == STATE_FLOW_SCHEMA
    assert chart["chart"] == "TargetStateChart"
    assert chart["summary"] == {
        "states": 12,
        "functions": 3,
        "notes": 9,
        "transitions": 20,
        "events": 12,
        "data": 8,
        "messages": 0,
    }

    status = chart["states"][0]
    assert status["name"] == "Status"
    assert status["parallel"] is True
    connected = find_state(chart, "Connected")
    loaded = find_state(chart, "Loaded")
    assert connected in status["states"]
    assert loaded in connected["states"]
    assert find_state(chart, "Running") in loaded["states"]
    assert find_state(chart, "Running")["entry"] == "EnterRunningState();"
    assert find_state(chart, "Disconnected")["entry"].endswith(
        "notify(tg_, 'Disconnected');\nend"
    )
    assert connected["exit"] == "notify(tg_, 'Disconnecting');\ntg_.disconnectTarget();"

    # Notes stay with the state whose transitions they explain.
    assert any(
        note.startswith("% Path taken when user executes\n% tg.connect")
        for note in connected["notes"]
    )
    assert all("DOCTYPE" not in note for note in connected["notes"])
    assert not any("DOCTYPE" in json.dumps(chart, ensure_ascii=False) for _ in [0])

    # A transition through a junction is written as the path it makes.
    initial = [item for item in loaded["transitions"] if item.get("initial")]
    assert {item["to"] for item in initial} == {"NotRunning", "PostStart"}
    guarded = next(item for item in initial if item["to"] == "PostStart")
    assert guarded["via"][0]["condition"] == "runningOnConnect_"
    assert "Running" in {item["to"] for item in loaded["transitions"]}
    assert not any("junction" in json.dumps(chart, ensure_ascii=False).lower() for _ in [0])

    functions = {function["name"]: function for function in chart["functions"]}
    assert functions["EnterUnloadedState"]["kind"] == "matlab"
    assert "Stopped" in functions["EnterUnloadedState"]["notifies"]
    assert functions["EnterRunningState"]["body"].startswith("% The 'Running' state")

    data = {item["name"]: item for item in chart["data"]}
    assert data["disconnectEV_"]["initial_value"] == "false"
    assert data["disconnectEV_"]["scope"] == "LOCAL_DATA"
    assert {item["name"] for item in chart["events"]} >= {"connected", "disconnect", "loaded"}


def test_stateflow_output_carries_no_machine_identifiers():
    charts = [
        chart_json(chart)
        for chart in parse_stateflow(SAMPLE / "model" / "TargetStateChart.sfx")
    ] + [chart_json(chart) for chart in parse_stateflow(CONTROLLER)]
    for chart in charts:
        keys = set(keys_of(chart))
        assert not keys & {"id", "ssid", "SSID", "chart_id", "parent", "path"}
        assert "chart_id" not in json.dumps(chart)
        for transition in all_transitions(chart):
            assert set(transition) <= {
                "from",
                "to",
                "via",
                "event",
                "condition",
                "condition_action",
                "action",
                "order",
                "initial",
                "inner",
                "loop",
            }
            for name in (transition.get("from"), transition.get("to")):
                assert name is None or not name.isdigit()


def test_stateflow_generic_chart_components(tmp_path):
    chart_xml = """<?xml version="1.0" encoding="utf-8"?>
<chart id="7">
  <P Name="name">Generic Chart</P>
  <P Name="actionLanguage">1</P>
  <Children>
    <state SSID="1">
      <P Name="labelString">Top
entry, during:
  x = 1;
exit:
  x = 0;
on E1:
  y = 1;
bind:
  z = 1;</P>
      <P Name="type">OR_STATE</P>
      <P Name="decomposition">CLUSTER_STATE</P>
      <Children>
        <state SSID="2">
          <P Name="labelString">&lt;html&gt;&lt;body&gt;&lt;p&gt;% note text&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</P>
          <P Name="type">GROUP_STATE</P>
          <P Name="isNoteBox">1</P>
        </state>
        <box SSID="3">
          <P Name="labelString">Box label</P>
        </box>
        <truthTable SSID="4">
          <P Name="conditionTable">[x &gt; 0]</P>
          <P Name="actionTable">y = 1;</P>
        </truthTable>
        <state SSID="8">
          <P Name="labelString">Done</P>
          <P Name="type">OR_STATE</P>
        </state>
        <state SSID="9">
          <P Name="labelString">Idle</P>
          <P Name="type">OR_STATE</P>
        </state>
        <junction SSID="5">
          <P Name="type">CONNECTIVE_JUNCTION</P>
        </junction>
        <transition SSID="6">
          <P Name="labelString">E1[x &gt; 0]{y = 2;}/z = 3;</P>
          <P Name="executionOrder">2</P>
          <src><P Name="SSID">1</P></src>
          <dst><P Name="SSID">5</P></dst>
        </transition>
        <transition SSID="7">
          <P Name="labelString">[y == 3]</P>
          <P Name="executionOrder">1</P>
          <src><P Name="SSID">5</P></src>
          <dst><P Name="SSID">8</P></dst>
        </transition>
        <transition SSID="10">
          <P Name="labelString">after(1, sec)</P>
          <P Name="executionOrder">3</P>
          <src><P Name="SSID">9</P></src>
          <dst><P Name="SSID">1</P></dst>
        </transition>
        <event SSID="12"><P Name="name">E1</P><P Name="scope">INPUT_EVENT</P><P Name="trigger">RISING_EDGE_EVENT</P></event>
        <data SSID="13" name="x"><P Name="scope">INPUT_DATA</P><P Name="dataType">double</P></data>
      </Children>
    </state>
    <state SSID="20">
      <P Name="labelString">Second</P>
      <P Name="type">OR_STATE</P>
      <Children>
        <state SSID="21">
          <P Name="labelString">Idle</P>
          <P Name="type">OR_STATE</P>
        </state>
        <transition SSID="22">
          <P Name="labelString">[x &lt; 0]</P>
          <P Name="executionOrder">1</P>
          <src><P Name="SSID">20</P></src>
          <dst><P Name="SSID">21</P></dst>
        </transition>
      </Children>
    </state>
  </Children>
</chart>
"""
    source = tmp_path / "Generic.sfx"
    with zipfile.ZipFile(source, "w") as archive:
        archive.writestr("simulink/stateflow/chart_7.xml", chart_xml)

    chart = chart_json(parse_stateflow(source)[0])
    assert chart["summary"] == {
        "states": 6,
        "functions": 1,
        "notes": 1,
        "transitions": 3,
        "events": 1,
        "data": 1,
        "messages": 0,
    }
    top = find_state(chart, "Top")
    assert top["entry"] == top["during"] == "x = 1;"
    assert top["exit"] == "x = 0;"
    assert top["on"] == [{"event": "E1", "actions": "y = 1;"}]
    assert top["bind"] == "z = 1;"
    assert find_state(chart, "Box label")["box"] is True
    assert top["notes"] == ["% note text"]
    assert top["data"] == [
        {
            "name": "x",
            "scope": "INPUT_DATA",
            "type": "double",
            "size": "未声明",
        }
    ]
    assert top["events"] == [
        {"name": "E1", "scope": "INPUT_EVENT", "trigger": "RISING_EDGE_EVENT"}
    ]
    function = top["functions"][0]
    assert function["kind"] == "truth_table"
    assert function["name"] == "truth table 1"
    assert function["properties"] == {"conditionTable": "[x > 0]", "actionTable": "y = 1;"}

    # Two states are called Idle, so every reference to them carries the path.
    paths = {path for path, _ in walk_paths(chart)}
    assert {"Top/Idle", "Second/Idle"} <= paths
    references = {
        item[key]
        for item in all_transitions(chart)
        for key in ("from", "to")
        if item.get(key, "").endswith("Idle")
    }
    assert references == {"Top/Idle", "Second/Idle"}

    # The junction on the Top -> Done path carries its own condition into the path.
    through = next(
        item
        for item in top["transitions"]
        if item["from"] == "Top" and item["to"] == "Done"
    )
    assert through["event"] == "E1"
    assert through["condition"] == "x > 0"
    assert through["condition_action"] == "y = 2;"
    assert through["action"] == "z = 3;"
    assert through["via"] == [{"condition": "y == 3", "order": "1"}]
    assert not chart.get("junctions")


def test_stateflow_transition_count_counts_states_not_junctions(tmp_path):
    chart_xml = """<?xml version="1.0" encoding="utf-8"?>
<chart id="7">
  <P Name="name">Branching</P>
  <P Name="actionLanguage">2</P>
  <Children>
    <state SSID="1">
      <P Name="labelString">A</P>
      <P Name="type">OR_STATE</P>
      <P Name="decomposition">CLUSTER_STATE</P>
    </state>
    <state SSID="2">
      <P Name="labelString">B</P>
      <P Name="type">OR_STATE</P>
    </state>
    <state SSID="3">
      <P Name="labelString">C</P>
      <P Name="type">OR_STATE</P>
    </state>
    <junction SSID="10">
      <P Name="type">CONNECTIVE_JUNCTION</P>
    </junction>
    <transition SSID="11">
      <P Name="executionOrder">1</P>
      <dst><P Name="SSID">1</P></dst>
    </transition>
    <transition SSID="12">
      <P Name="labelString">[go]</P>
      <P Name="executionOrder">1</P>
      <src><P Name="SSID">1</P></src>
      <dst><P Name="SSID">10</P></dst>
    </transition>
    <transition SSID="13">
      <P Name="labelString">[b]</P>
      <P Name="executionOrder">1</P>
      <src><P Name="SSID">10</P></src>
      <dst><P Name="SSID">2</P></dst>
    </transition>
    <transition SSID="14">
      <P Name="labelString">[c]</P>
      <P Name="executionOrder">2</P>
      <src><P Name="SSID">10</P></src>
      <dst><P Name="SSID">3</P></dst>
    </transition>
    <transition SSID="15">
      <P Name="labelString">[back]</P>
      <P Name="executionOrder">1</P>
      <src><P Name="SSID">2</P></src>
      <dst><P Name="SSID">1</P></dst>
    </transition>
    <transition SSID="16">
      <P Name="labelString">[next]</P>
      <P Name="executionOrder">1</P>
      <src><P Name="SSID">3</P></src>
      <dst><P Name="SSID">2</P></dst>
    </transition>
  </Children>
</chart>
"""
    source = tmp_path / "Branching.sfx"
    with zipfile.ZipFile(source, "w") as archive:
        archive.writestr("simulink/stateflow/chart_7.xml", chart_xml)

    chart = chart_json(parse_stateflow(source)[0])
    # Six transition segments in the XML, but one of them only reaches the
    # junction: what is counted is every way from a state (or the entry) to a
    # state, so the branch out of the junction counts once per state it reaches.
    assert chart["summary"]["transitions"] == 5
    forwarded = {
        (item.get("from"), item.get("to"), item.get("condition"))
        for item in chart["transitions"]
    }
    assert forwarded == {
        (None, "A", None),
        ("A", "B", "go"),
        ("A", "C", "go"),
        ("B", "A", "back"),
        ("C", "B", "next"),
    }


def test_stateflow_flow_steps_are_not_counted_as_transitions():
    chart = chart_json(
        parse_stateflow(
            STATE_FLOW_EXAMPLES / "PatternWizard" / "sf_pw_ifelseifelseifelse_.sfx"
        )[0]
    )
    # Four branches run here, but a flow chart changes no state: the steps are
    # branches, not transitions, and counting them made the numbers incomparable.
    assert len(chart["flow"]["cases"]) == 4
    assert chart["summary"]["transitions"] == 0


def test_stateflow_example_unnamed_ports_are_named_in_english():
    document = example_documents("LaunchAbortController", "sf_launchabort.slx")[0]
    references = {
        transition[key]
        for transition in all_transitions(document)
        if transition.get("port")
        for key in ("from", "to")
        if key in transition
    }
    assert {"Abort port 1", "Abort port 2", "AbortLogic port 1"} <= references
    # A port on the chart itself has no owner to name it after.
    aircraft = example_documents("Actuator Control", "sf_aircraft_lib.slx")[0]
    chart_ports = {
        transition[key]
        for transition in all_transitions(aircraft)
        if transition.get("port")
        for key in ("from", "to")
        if key in transition
    }
    assert "port 1" in chart_ports
    # The fallbacks are English whatever they name, and no name is a number.
    for payload in (document, aircraft):
        text = json.dumps(payload, ensure_ascii=False)
        assert "的端口" not in text
        assert "里的 decision" not in text


RICH_TEXT_LABEL = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body align="left" style=" font-family:'Helvetica'; font-size:12px; color:#ff0000;">
<p align="left" style=" margin-top:0px; text-indent:0px;"><span style=" font-size:10px;">Idle </span><span style=" color:#00ff00;">mode</span></p>
<p align="left" style=" margin-top:0px; text-indent:0px;"><span style=" font-family:'Courier New';">entry: x = 1;</span></p></body></html>"""


def test_rich_text_label_keeps_its_words_and_drops_its_styling():
    text = _label_text(RICH_TEXT_LABEL)
    assert text == "Idle mode\nentry: x = 1;"
    # Neither the markup nor the styling it carries reaches the text.
    for leftover in ("<", ">", "font-family", "font-size", "color", "ff0000", "Helvetica"):
        assert leftover not in text
    # An ordinary label has no markup and must come back untouched, condition
    # signs included.
    assert _label_text("[a < b]") == "[a < b]"
    assert _label_text("Idle\nentry:\n x = 1;") == "Idle\nentry:\n x = 1;"
    assert _label_text("") == ""


def test_rich_text_state_label_names_the_state_and_keeps_its_actions():
    root = ET_fromstring(
        '<chart SSID="1"><P Name="name">rich</P>'
        '<state SSID="2"><P Name="type">OR_STATE</P>'
        '<P Name="labelString" /></state></chart>'
    )
    # A doctype cannot sit inside an XML string, so the rich text is attached
    # to the property directly, exactly as the chart XML carries it.
    root.find("./state/P[@Name='labelString']").text = RICH_TEXT_LABEL
    chart = _parse_chart(root, "chart_1.xml")
    document = chart_json(chart)
    state = document["states"][0]
    assert state["name"] == "Idle mode"
    assert state["entry"] == "x = 1;"
    assert "ff0000" not in json.dumps(document)


STATE_FLOW_EXAMPLES = SAMPLE / "model" / "StateflowExamples"


def stateflow_examples():
    return sorted(
        path
        for path in STATE_FLOW_EXAMPLES.rglob("*")
        if path.suffix.lower() in {".slx", ".sfx"}
    )


def example_documents(name, filename=None):
    documents = []
    for path in STATE_FLOW_EXAMPLES.rglob(filename or "*.slx"):
        for chart in parse_stateflow(path):
            if chart.name == name:
                documents.append(chart_json(chart))
    return documents


def test_stateflow_examples_all_parse_and_are_complete():
    files = stateflow_examples()
    assert len(files) == 211
    charts = 0
    for path in files:
        documents = [chart_json(chart) for chart in parse_stateflow(path)]
        charts += len(documents)
        for document in documents:
            assert document["schema"] == STATE_FLOW_SCHEMA
            assert not set(keys_of(document)) & {"id", "ssid", "chart_id", "parent", "path"}
            paths = {display for display, _ in walk_paths(document)}
            names = {item.split("/")[-1] for item in paths}
            assert len(list(walk_states(document))) == document["summary"]["states"], path
            assert len(list(all_functions(document))) == document["summary"]["functions"], path
            for transition in all_transitions(document):
                if transition.get("port"):
                    continue
                for key in ("from", "to"):
                    value = transition.get(key)
                    assert value is None or value in paths or value in names, (
                        path,
                        document["chart"],
                        key,
                        value,
                    )
            assert not re.search(r"里的 decision \d", json.dumps(document))
            assert "的端口" not in json.dumps(document, ensure_ascii=False), path
            payload = json.dumps(document, ensure_ascii=False)
            for marker in ("<!DOCTYPE", "<span", "font-family", "font-size"):
                assert marker not in payload, (path, document["chart"], marker)
            for flow in all_flows(document):
                for statement in walk_flow(flow):
                    target = statement.get("to")
                    assert target is None or target in paths or target in names, (
                        path,
                        document["chart"],
                        target,
                    )
    assert charts == 276


def test_stateflow_example_chart_kinds():
    kinds = {}
    for path in stateflow_examples():
        for chart in parse_stateflow(path):
            kinds.setdefault(chart.chart_type, []).append(chart.name)
    assert kinds["state chart"]
    assert kinds["MATLAB function"]
    assert kinds["state transition table"]
    assert kinds["truth table"]

    wrapper = next(
        chart
        for chart in parse_stateflow(
            STATE_FLOW_EXAMPLES
            / "AutomaticTransmissionUsingDurationOperatorExample"
            / "sf_car_using_duration.slx"
        )
        if chart.chart_type == "MATLAB function"
    )
    document = chart_json(wrapper)
    assert document["type"] == "MATLAB function"
    assert document["functions"][0]["kind"] == "matlab"
    assert document["functions"][0]["signature"].startswith("function out = fcn(gear)")
    assert document["functions"][0]["body"].startswith("%#codegen")
    assert "transitions" not in document  # the call that runs the function is plumbing


def test_stateflow_example_truth_table_reads_its_table():
    document = example_documents("ClimateController")[0]
    assert document["type"] == "truth table"
    table = document["functions"][0]["truth_table"]
    assert document["functions"][0]["kind"] == "truth_table"
    assert document["functions"][0]["name"] == "fcn"
    assert table["conditions"] == [
        {"name": "Hot", "test": "t > T_thresh", "values": ["T", "T", "-", "-"]},
        {"name": "Dry", "test": "h < H_thresh", "values": ["T", "-", "T", "-"]},
    ]
    assert table["decisions"] == ["CoolOn,HumidOn", "CoolOn", "HeatOn,HumidOn", "HeatOn"]
    assert [item["name"] for item in table["actions"]][0] == (
        "Turn On Cooling (This implicitly reduces humidity)"
    )
    assert table["actions"][0]["action"] == "CoolOn:\ncooler = 1;\nheater = 0;\nhumidifier = 0;"
    # The table is the source, the generated code is what actually runs.
    assert document["functions"][0]["body"].startswith("aVarTruthTableCondition_1")


def test_transition_label_keeps_a_matlab_transpose():
    assert transition_label("[A' * B > 0]")["condition"] == "A' * B > 0"
    parts = transition_label("[x' > 0]{y = 1;}")
    assert parts["condition"] == "x' > 0"
    assert parts["condition_action"] == "y = 1;"
    # A quote in front of a value still opens a string.
    assert transition_label("[strcmp(s,'abc')]")["condition"] == "strcmp(s,'abc')"


def test_stateflow_example_names_the_action_language():
    # Chart actions are written in MATLAB by default; these charts say C.
    assert example_documents("Traffic Controller")[0]["action_language"] == "MATLAB"
    c_chart = example_documents("SaturationEnabled")[0]
    assert c_chart["action_language"] == "C"


def test_stateflow_example_state_transition_table_is_a_state_machine():
    document = example_documents("Debouncer Logic Table")[0]
    assert document["type"] == "state transition table"
    states = {state["name"]: state for state in walk_states(document)}
    assert set(states) == {"ON", "ON_TO_OFF", "OFF_TO_ON", "OFF"}
    assert states["ON"] == {"name": "ON", "generated": True, "entry": "y = 1;"}
    assert any(
        transition.get("from") == "ON" and transition.get("condition") == "u == 0"
        for transition in all_transitions(document)
    )


def test_stateflow_example_atomic_subchart_ports_and_history():
    document = example_documents("Bang-Bang\nController", "sf_boiler.slx")[0]
    assert document["sample_time"] == "1"
    heater = document["states"][0]
    assert heater["name"] == "Heater" and heater["box"] is True
    assert heater["ports"] == ["turnOff"]
    on = find_state(document, "On")
    assert on["subchart"] is True
    assert on["ports"] == ["turnOff"]
    assert on["active_state_output"] == "SELF_ACTIVITY"
    exiting = [
        transition
        for transition in all_transitions(document)
        if transition.get("port") and transition.get("to") == "turnOff"
    ]
    assert exiting and exiting[0]["condition"] == "warm()"

    variant = example_documents("Lamp", "sfVariantLampExample.slx")[0]
    assert variant["variant"] == "CODE_COMPILE"
    # A history junction is the memory of the state that owns it.
    assert find_state(variant, "Dimmer1")["history"] is True
    assert find_state(variant, "Dimmer2")["history"] is True


def test_stateflow_example_messages_and_functions():
    documents = []
    for path in STATE_FLOW_EXAMPLES.rglob("sf_message_strings.slx"):
        for chart in parse_stateflow(path):
            documents.append(chart_json(chart))
    receiver = next(item for item in documents if item["chart"] == "Receiver")
    message = next(item for item in receiver["data"] if "message" in item)
    assert (message["name"], message["message"]["queue_length"]) == ("M", "10")

    graphical = example_documents("Bang-Bang\nController", "sf_boiler.slx")[0]
    function = next(item for item in graphical["functions"] if item["name"] == "flash_LED")
    assert function["name"] == "flash_LED"
    assert function["kind"] == "graphical"
    # A graphical function's flow chart reads as its branches, not its junctions.
    cases = function["flow"]["cases"]
    assert [case.get("when") for case in cases][:2] == ["boiler == ON", None]
    assert "LED=OFF" in json.dumps(function, ensure_ascii=False)

    simulink = example_documents("shift_logic", "sf_car.slx")[0]
    function = next(item for item in all_functions(simulink) if item["kind"] == "simulink")
    assert function["name"] == "calc_th"
    assert function["block"] == "selection_state.calc_th"


def test_stateflow_flow_chart_reads_as_if_else_without_junctions():
    else_if = chart_json(
        parse_stateflow(
            STATE_FLOW_EXAMPLES / "PatternWizard" / "sf_pw_ifelseifelseifelse_.sfx"
        )[0]
    )
    assert else_if["flow"] == {
        "comment": "%comment",
        "cases": [
            {"when": "condition1", "do": "action1"},
            {"when": "condition2", "do": "action2"},
            {"when": "condition3", "do": "action3"},
            {"do": "action4"},
        ],
    }
    switch = chart_json(
        parse_stateflow(STATE_FLOW_EXAMPLES / "PatternWizard" / "sf_pw_switch4_.sfx")[0]
    )
    assert switch["flow"]["cases"] == [
        {"when": "case1", "do": "action1"},
        {"when": "case2", "do": "action2"},
        {"when": "case3", "do": "action3"},
        {"when": "case4", "do": "action4"},
        {"do": "defaultAction"},
    ]
    assert not re.search(r"里的 decision \d", json.dumps(switch, ensure_ascii=False))


def test_stateflow_flow_chart_writes_loops_as_loops():
    model = STATE_FLOW_EXAMPLES / "FixedPointMandelbrotSetExample" / "sf_mandelbrot_fixpt.slx"
    chart = next(
        chart_json(chart) for chart in parse_stateflow(model) if chart.name == "Chart"
    )
    flow = next(item for item in chart["functions"] if item["name"] == "mandel_fix")["flow"]
    assert flow["do"][0].startswith("a0 = fi(a, 1, 16, 13);")
    inner = flow["then"][0]["cases"][0]
    assert inner["when"] == "cn < 4 && ii < local_colors"
    assert inner["loop"] is True
    assert any("ii = ii + 1;" in text for text in inner["do"])
    # The whole chart loops rows and columns and leaves through the state.
    entries = chart["flow"]["entries"]
    assert {entry.get("from") for entry in entries} == {None, "Wait"}
    nested = next(entry for entry in entries if entry.get("from") is None)
    cases = nested["then"][0]["cases"]
    assert cases[0]["when"] == "i <= pix_h"
    assert cases[1]["to"] == "Wait"


def test_sldd_entries_dimensions_types_and_references():
    dictionary = (
        SAMPLE
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatMBSEModel"
        / "ModelData"
        / "asbCubeSatArchInterfaceData.sldd"
    )
    tree = parse_sldd_tree(dictionary)
    assert tree["entry_count"] == 6
    assert tree["references"] == ["asbCubeSatModelData.sldd"]
    assert tree["classes"] == {
        "Simulink.Parameter": 3,
        "Simulink.ConfigSet": 2,
        "Simulink.Bus": 1,
    }
    by_name = {entry["name"]: entry for entry in tree["entries"]}
    assert by_name["altitude"]["value"]["class"] == "Simulink.Parameter"
    assert by_name["altitude"]["value"]["Value"] == "4000000.0"
    assert by_name["ACSConfigSet"]["value"]["class"] == "Simulink.ConfigSet"

    rows = sldd_entry_rows(tree)
    altitude = next(row for row in rows if row["name"] == "altitude")
    assert altitude["class"] == "Simulink.Parameter"
    assert altitude["value"] == "4000000.0"
    assert altitude["complexity"] is None
    assert altitude["storage"] == "Auto"
    assert altitude["dimensions"] == [1, 1]
    assert altitude["dtype"] == "auto"
    assert altitude["unit"] is None
    assert altitude["last_modified"] == "20210206T043926.586625"
    assert altitude["last_modified_by"] == "The MathWorks, Inc."
    assert altitude["uuid"] == "fa2b4ae4-c15f-40b5-b2d7-83c715c6f939"
    assert altitude["namespace"] == "dacaf35e-55a5-454d-a7c1-93db038a210e"
    assert altitude["is_derived"] is False
    for column in (
        "status",
        "complexity",
        "min",
        "max",
        "unit",
        "argument",
        "storage",
        "data_source",
        "last_modified",
        "last_modified_by",
    ):
        assert column in altitude
def test_slx_block_ports_edges_and_children_have_no_generated_ids():
    model = parse_slx(
        SAMPLE / "model" / "asbCubeSatMBSE" / "CubeSatMBSEModel" / "asbCubeSatArchModel.slx"
    )
    document = system_json_documents(model)["main.json"]
    blocks = {block["name"]: block for block in document["blocks"]}

    # Port names come from the file: the ModelReference port lists and the
    # subsystem's own Inport/Outport blocks.
    space = blocks["Space Environment"]
    assert space["ports"] == {"in": ["CubeSatStates"], "out": ["Env"]}
    assert "source_block" not in space
    assert "block_type" not in space
    assert "id" not in space

    edge = next(
        item for item in document["edges"] if item["from"] == ["Space Environment", "Env"]
    )
    assert edge["signal"] is None
    assert len(edge["to"]) >= 2
    assert all(target[1] for target in edge["to"])
    assert len([item for item in document["edges"] if item["from"] == ["Space Environment", "Env"]]) == 1

    for child in document["children"]:
        assert "block_id" not in child
        assert child["path"].endswith(".json")


def test_slx_unnamed_ports_fall_back_to_port_index():
    documents = system_json_documents(parse_slx(CONTROLLER))
    document = documents["main.json"]
    lookup = next(block for block in document["blocks"] if block["name"] == "ChargeFactor")
    # The block type only feeds the key; it is not written into the document.
    assert lookup["key"] == "Lookup_n-D"
    assert lookup["ports"]["in"] == [1]
    assert "source_block" not in lookup
    assert "block_type" not in lookup


@pytest.mark.asyncio
async def test_sldd_arrays_go_to_npy_and_original_is_dropped(tmp_path):
    np = pytest.importorskip("numpy")
    dictionary = (
        SAMPLE
        / "model"
        / "VirtualVehicle"
        / "EngineData"
        / "Dictionaries"
        / "CiEngineCore.sldd"
    )
    result = await MatlabParser().parse(
        dictionary, parse_output_store=LocalParseOutputStore(tmp_path)
    )
    root = Path(result.artifact_ref.root) / "CiEngineCore"
    assert not list(root.glob("*.sldd"))
    assert result.meta["original_preserved"] is False
    rows = {
        row["name"]: row
        for row in map(
            json.loads, (root / "entries.jsonl").read_text(encoding="utf-8").splitlines()
        )
    }

    mep = rows["PlntEngCIGIMepMap"]
    assert mep["dimensions"] == [15, 16]
    assert mep["dtype"] == "double"
    assert mep["complexity"] == "real"
    assert "value" not in mep
    assert mep["format"] == "npy"
    assert mep["data"] == "0008_PlntEngCIGIMepMap.npy"
    matrix = np.load(root / mep["data"])
    assert matrix.shape == (15, 16)
    assert matrix[0, 0] == pytest.approx(0.0)
    assert matrix[1, 0] == pytest.approx(158686.535, rel=1e-6)
    assert matrix[2, 0] == pytest.approx(343074.266, rel=1e-6)

    turb = rows["PlntEngCITurbEff"]
    assert turb["dimensions"] == [60, 80, 6]
    assert turb["data"] == "0003_PlntEngCITurbEff.npy"
    # .npy carries the shape itself: no flattening, no index columns, no manifest.
    cube = np.load(root / turb["data"])
    assert cube.shape == (60, 80, 6)
    assert not list(root.glob("*.csv"))
    assert not (root / "data").exists()


@pytest.mark.asyncio
async def test_sldd_one_dimensional_values_stay_inline(tmp_path):
    dictionary = (
        SAMPLE
        / "model"
        / "VirtualVehicle"
        / "EngineData"
        / "Dictionaries"
        / "CiEngineCore.sldd"
    )
    result = await MatlabParser().parse(
        dictionary, parse_output_store=LocalParseOutputStore(tmp_path)
    )
    root = Path(result.artifact_ref.root) / "CiEngineCore"
    rows = [
        json.loads(line)
        for line in (root / "entries.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    inline = [row for row in rows if "value" in row]
    external = [row for row in rows if "data" in row]
    assert external
    assert all("data" not in row for row in inline)
    # Only a 1x1 value is allowed to carry numbers in the JSONL line.
    assert all(row["dimensions"] == [1, 1] for row in inline)
    assert all(list(map(int, row["dimensions"])) != [1, 1] or "value" not in row for row in external)


def test_slx_rejects_missing_model_root(tmp_path):
    path = tmp_path / "invalid.slx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("simulink/blockdiagram.xml", "<BlockDiagram />")
    with pytest.raises(ValueError, match="no model root System"):
        parse_slx(path)


def test_zip_xml_member_limit(tmp_path):
    path = tmp_path / "oversized.slx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("simulink/blockdiagram.xml", b"x" * 17)
    with zipfile.ZipFile(path) as archive:
        with pytest.raises(ValueError, match="16-byte XML safety limit"):
            read_xml_member(archive, "simulink/blockdiagram.xml", max_bytes=16)


def load_npy(documents, name):
    """Read a .npy document from a parser result without touching the disk."""
    np = pytest.importorskip("numpy")
    return np.load(io.BytesIO(documents[name]))


def test_mat_v73_hdf5_full_array_export(tmp_path):
    h5py = pytest.importorskip("h5py")
    path = tmp_path / "large.mat"
    with h5py.File(path, "w") as handle:
        handle.create_dataset("trajectory", data=[[1.0, 2.0], [3.0, 4.0]])
        handle.create_dataset("nested/speed", data=[5.0, 6.0])
    content, warnings = parse_mat(path)
    entries = [json.loads(line) for line in content.splitlines()]
    header = entries[0]
    assert header["kind"] == "file"
    assert header["schema"] == "ov.matlab.entries/1"
    assert header["mat_version"] == "v7.3"
    trajectory = next(item for item in entries if item.get("name") == "trajectory")
    assert trajectory["dims"] == [2, 2]
    assert trajectory["format"] == "npy"
    assert trajectory["dtype"] == "float64"
    documents, warnings = parse_mat_documents(path)
    assert "entries.jsonl" in documents
    assert not any(name.endswith("variables.json") for name in documents)
    matrix = load_npy(documents, trajectory["data"])
    assert matrix.shape == (2, 2)
    assert matrix.tolist() == [[1.0, 2.0], [3.0, 4.0]]
    assert not warnings
    nested = next(item for item in entries if item.get("name") == "nested/speed")
    assert load_npy(documents, nested["data"]).tolist() == [5.0, 6.0]


def test_mat_three_dimensional_array_round_trips_through_npy(tmp_path):
    np = pytest.importorskip("numpy")
    savemat = pytest.importorskip("scipy.io").savemat
    path = tmp_path / "cube.mat"
    cube = np.arange(1, 25, dtype=float).reshape(4, 3, 2)
    savemat(path, {"cube": cube})
    documents, warnings = parse_mat_documents(path)
    entries = [json.loads(line) for line in documents["entries.jsonl"].splitlines()]
    row = next(item for item in entries if item.get("name") == "cube")
    assert row["dims"] == [4, 3, 2]
    assert row["format"] == "npy"
    assert row["data"].endswith(".npy")
    assert np.array_equal(load_npy(documents, row["data"]), cube)
    assert not warnings


@pytest.mark.asyncio
async def test_mat_with_unexpandable_references_keeps_its_bytes(tmp_path):
    """When a part cannot be expanded, the original stays the only complete copy."""
    h5py = pytest.importorskip("h5py")
    source = tmp_path / "signals.mat"
    with h5py.File(source, "w") as handle:
        handle.create_dataset("signals", (2,), dtype=h5py.special_dtype(ref=h5py.Reference))
    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "signals"
    assert (root / "signals.mat").read_bytes() == source.read_bytes()
    assert result.meta["original_preserved"] is True
    assert any("HDF5 引用数组" in warning for warning in result.warnings)


@pytest.mark.asyncio
async def test_mat_that_cannot_be_read_keeps_its_bytes(tmp_path, monkeypatch):
    """A v7.3 MAT without h5py degrades to the original plus a warning."""
    source = tmp_path / "recorded.mat"
    source.write_bytes(b"\x89HDF\r\n\x1a\n" + b"\x00" * 32)

    def unreadable(path):
        raise RuntimeError("MAT v7.3 parsing requires h5py")

    monkeypatch.setattr(
        "openviking.parse.parsers.matlab.parser.parse_mat_documents", unreadable
    )
    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "recorded"
    assert (root / "recorded.mat").read_bytes() == source.read_bytes()
    assert result.meta["original_preserved"] is True
    assert result.meta["parse_status"] == "original-only"
    assert "h5py" in result.meta["parse_error"]
    assert any("MAT 解析失败" in warning for warning in result.warnings)


@pytest.mark.asyncio
async def test_parsed_containers_are_not_stored_as_originals(tmp_path):
    """A file whose content is fully parsed is kept only as that parsed content."""
    store = LocalParseOutputStore(tmp_path / "artifacts")
    parser = MatlabParser()
    notebook = SAMPLE / "model" / "asbCubeSatMBSE" / "MissionAnalysis" / "mappingToolboxAnalysis.mlx"
    for source, folder, document in (
        (SAMPLE / "model" / "TargetStateChart.sfx", "TargetStateChart", "stateflow.json"),
        (SAMPLE / "data" / "flames.mat", "flames", "entries.jsonl"),
        (notebook, "mappingToolboxAnalysis", "notebook.json"),
    ):
        result = await parser.parse(source, parse_output_store=store)
        root = Path(result.artifact_ref.root) / folder
        assert (root / document).is_file(), document
        assert not list(root.glob(f"*{source.suffix}")), source.name
        assert result.meta["original_preserved"] is False
        # Without the bytes, meta still says which source produced the output.
        assert result.meta["source_bytes"] == source.stat().st_size
        assert result.meta["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()


def test_mat_wide_higher_dimension_array_stays_one_file(tmp_path):
    np = pytest.importorskip("numpy")
    savemat = pytest.importorskip("scipy.io").savemat
    path = tmp_path / "wide.mat"
    wide = np.arange(2 * 65 * 65, dtype=float).reshape(2, 65, 65)
    savemat(path, {"wide": wide})
    documents, warnings = parse_mat_documents(path)
    entries = [json.loads(line) for line in documents["entries.jsonl"].splitlines()]
    row = next(item for item in entries if item.get("name") == "wide")
    # A CSV grid would need 4225 columns here; .npy keeps the shape as it is.
    assert row["dims"] == [2, 65, 65]
    assert [name for name in documents if name.endswith(".npy")] == [row["data"]]
    assert np.array_equal(load_npy(documents, row["data"]), wide)
    assert warnings == []


def test_mat_scalars_stay_in_the_jsonl_and_arrays_go_to_npy(tmp_path):
    np = pytest.importorskip("numpy")
    savemat = pytest.importorskip("scipy.io").savemat
    path = tmp_path / "mixed.mat"
    savemat(path, {"gain": np.array([[2.5]]), "vector": np.array([[1.0, 2.0, 3.0]])})
    documents, _ = parse_mat_documents(path)
    entries = [json.loads(line) for line in documents["entries.jsonl"].splitlines()]
    gain = next(item for item in entries if item.get("name") == "gain")
    vector = next(item for item in entries if item.get("name") == "vector")
    assert gain["value"] == 2.5 and "data" not in gain
    assert "value" not in vector
    assert [name for name in documents if name.endswith(".npy")] == [vector["data"]]
    assert load_npy(documents, vector["data"]).tolist() == [[1.0, 2.0, 3.0]]


def test_mat_sparse_array_is_exported_in_full(tmp_path):
    sparse = pytest.importorskip("scipy.sparse")
    savemat = pytest.importorskip("scipy.io").savemat
    path = tmp_path / "sparse.mat"
    savemat(path, {"matrix": sparse.csc_matrix([[0.0, 1.5], [2.5, 0.0]])})
    documents, warnings = parse_mat_documents(path)
    entries = [json.loads(line) for line in documents["entries.jsonl"].splitlines()]
    row = next(item for item in entries if item.get("name") == "matrix")
    assert row["sparse"] is True
    assert load_npy(documents, row["data"]).tolist() == [[0.0, 1.5], [2.5, 0.0]]
    assert not warnings


def test_mlx_blocks_are_code_markdown_and_output():
    live_script = SAMPLE / "model" / "asbCubeSatMBSE" / "MissionAnalysis" / "mappingToolboxAnalysis.mlx"
    notebook, files = parse_mlx_notebook(live_script)
    kinds = {block["type"] for block in notebook["blocks"]}
    assert kinds == {"code", "markdown", "output"}
    assert notebook["counts"] == {
        "code": sum(block["type"] == "code" for block in notebook["blocks"]),
        "markdown": sum(block["type"] == "markdown" for block in notebook["blocks"]),
        "output": sum(block["type"] == "output" for block in notebook["blocks"]),
    }
    assert all(set(block) >= {"type", "content"} for block in notebook["blocks"])
    assert "heading" not in notebook
    assert "cells" not in notebook and "outputs" not in notebook

    # A heading and the text under it stay in one markdown block.
    markdown = [block["content"] for block in notebook["blocks"] if block["type"] == "markdown"]
    assert (
        "## Run the Simulation\n\nRun the simulation if the simulation output object out "
        "does not exist." in markdown
    )

    code = [block["content"] for block in notebook["blocks"] if block["type"] == "code"]
    assert 'arch.model = "asbCubeSatArchModel";' in code[0]
    assert code[0].endswith("end")

    # Every output follows the code block that produced it, and images point at saved files.
    for index, block in enumerate(notebook["blocks"]):
        if block["type"] != "output":
            continue
        previous = index - 1
        while previous >= 0 and notebook["blocks"][previous]["type"] == "output":
            previous -= 1
        assert previous < 0 or notebook["blocks"][previous]["type"] == "code"
        if block["media"] == "image":
            assert block["content"] in files
    assert any(block.get("media") == "image" for block in notebook["blocks"])
    assert files and all(name.startswith("outputs/") for name in files)
def test_fig_chart_type_and_values_are_kept(tmp_path):
    np = pytest.importorskip("numpy")
    scipy_io = pytest.importorskip("scipy.io")
    node = np.dtype([("type", "O"), ("handle", "O"), ("properties", "O"), ("children", "O")])
    line = np.zeros((1, 1), dtype=node)
    line[0, 0]["type"] = "l"
    line[0, 0]["properties"] = {
        "XData": np.array([[0.0, 1.0]]),
        "YData": np.array([[2.0, 3.0]]),
        "DisplayName": "speed",
    }
    axes = np.zeros((1, 1), dtype=node)
    axes[0, 0]["type"] = "a"
    axes[0, 0]["properties"] = {"Title": "speed"}
    axes[0, 0]["children"] = line
    figure = np.zeros((1, 1), dtype=node)
    figure[0, 0]["type"] = "f"
    figure[0, 0]["properties"] = {"Name": "plot"}
    figure[0, 0]["children"] = axes
    scipy_io.savemat(tmp_path / "plot.fig", {"hgS_070000": figure})

    payload, files = parse_figure(tmp_path / "plot.fig")
    assert payload["schema"] == "ov.matlab.figure/2"
    assert payload["summary"]["chart_types"] == {"line": 1}
    series = payload["charts"][0]["series"][0]
    assert series["name"] == "speed"
    assert series["values"] == {"x": [0.0, 1.0], "y": [2.0, 3.0]}
    assert payload["charts"][0]["axes"]["title"] == "speed"
    assert files == {}


@pytest.mark.asyncio
async def test_figure_series_beyond_the_inline_limit_is_saved_as_npy(tmp_path):
    """A long series keeps every value in an .npy file next to figure.json."""
    np = pytest.importorskip("numpy")
    savemat = pytest.importorskip("scipy.io").savemat
    node = np.dtype([("type", "O"), ("handle", "O"), ("properties", "O"), ("children", "O")])
    line = np.zeros((1, 1), dtype=node)
    line[0, 0]["type"] = "l"
    line[0, 0]["properties"] = {
        "XData": np.linspace(0, 1, 2000).reshape(1, -1),
        "YData": np.linspace(0, 2, 2000).reshape(1, -1),
    }
    axes = np.zeros((1, 1), dtype=node)
    axes[0, 0]["type"] = "a"
    axes[0, 0]["children"] = line
    figure = np.zeros((1, 1), dtype=node)
    figure[0, 0]["type"] = "f"
    figure[0, 0]["children"] = axes
    source = tmp_path / "long.fig"
    savemat(source, {"hgS_070000": figure})

    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "long"
    figure_json = json.loads((root / "figure.json").read_text(encoding="utf-8"))
    assert figure_json["summary"]["chart_types"] == {"line": 1}
    series = figure_json["charts"][0]["series"][0]
    assert series["points"] == 2000
    data_ref = series["values"]["y"]
    assert (root / data_ref["data"]).is_file()
    assert np.load(root / data_ref["data"]).shape == (2000,)
    assert (root / "figure.md").is_file()
    assert "线图" in (root / "figure.md").read_text(encoding="utf-8")
    # The values live in the artifact, so the original bytes are not kept.
    assert not (root / "long.fig").exists()
    assert result.meta["original_preserved"] is False


def test_mldatx_keeps_all_suites_cases_and_results(tmp_path):
    path = tmp_path / "tests.mldatx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "testSuite.xml",
            '<TestSuite name="battery"><TestCase name="heat"><Result verdict="pass"/></TestCase></TestSuite>',
        )
    tree = parse_mldatx(path)
    names = {item["name"] for item in tree["tests"]}
    assert {"battery", "heat"} <= names
    assert any(item["tag"] == "Result" for item in tree["tests"])
    assert tree["members"][0]["name"] == "testSuite.xml"
    assert tree["unparsed_member_count"] == 0
    assert tree["kind"] == "simulink-test"


def _sdi_mldatx(tmp_path: Path) -> Path:
    """A Simulation Data Inspector session: runs, checked signals, Parquet chunks."""
    path = tmp_path / "WindTurbineSDI.mldatx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "runs/sdi_run_data.json",
            json.dumps(
                [
                    {
                        "id": 2875,
                        "Date": 1734028869,
                        "OutputMetaData": {
                            "Model": "WEC_StateMachine",
                            "ModelVersion": "9.80",
                            "SLVersion": "Simulink 25.1 (R2025a)",
                            "SolverName": "ode23t",
                            "SolverType": "Variable-Step",
                            "SolverMaxStepSize": "16",
                            "StartTime": 0,
                            "StopTime": 800,
                            "SimTime": 1.049781,
                            "StopEventDescription": "Reached stop time of 800",
                        },
                    }
                ]
            ),
        )
        archive.writestr("runs/sdi_inspect.json", '{"currentRunID": 2875}')
        archive.writestr(
            "runs/parquetSignalStorageMetadataRun2875.json",
            json.dumps([{"signalId": 2920, "dataStorageId": [11], "timeStorageId": [0]}]),
        )
        archive.writestr(
            "views/sdi_checked_signals.xml",
            "<sdi><Version>1.0</Version><Signals><Sig1>"
            "<SignalName>wTurbine</SignalName><Port>1</Port>"
            "<BlockPath><Element>WEC_StateMachine/Wind Turbine/Transfer Fcn</Element></BlockPath>"
            "<Plots><Element>3</Element></Plots>"
            "<Color><r>0</r><g>0.44705882352941179</g><b>0.74117647058823533</b></Color>"
            "<ID>2920</ID></Sig1></Signals></sdi>",
        )
        archive.writestr(
            "views/sdi_view_meta_data.xml",
            "<sdi><Version>2.13</Version><SubPlots><SubPlot3><ID>3</ID>"
            "<Tmin>-16</Tmin><Tmax>816</Tmax><Ymin>-1.0</Ymin><Ymax>22.6</Ymax>"
            "<visualizationID>timeplotplugin</visualizationID></SubPlot3></SubPlots></sdi>",
        )
        archive.writestr(
            "compression/compression_flag.json", '{"CompressionFlag": true}'
        )
        archive.writestr("parquet/run2875/0", b"PAR1" * 8)
        archive.writestr("metadata/thumbnail.png", b"\x89PNG")
    return path


def test_mldatx_sdi_session_keeps_runs_and_signals(tmp_path):
    """An SDI session is run settings and viewed signals, not a test suite."""
    tree = parse_mldatx(_sdi_mldatx(tmp_path))
    assert tree["kind"] == "sdi"
    run = tree["runs"][0]
    assert run["model"] == "WEC_StateMachine"
    assert run["solver"] == {"name": "ode23t", "type": "Variable-Step", "max_step": 16}
    assert run["stop_time"] == 800
    assert run["simulated_time"] == pytest.approx(1.049781)
    assert run["recorded_at"].startswith("2024-12-12")
    assert run["stored_signals"] == [{"signal_id": 2920, "data": [11]}]
    signal = tree["signals"][0]
    assert signal["name"] == "wTurbine"
    assert signal["block_path"] == "WEC_StateMachine/Wind Turbine/Transfer Fcn"
    assert signal["color"] == "#0072BD"
    assert tree["views"][0]["time_range"] == [-16.0, 816.0]
    assert tree["views"][0]["visualization"] == "timeplotplugin"
    assert tree["compression"] == {"enabled": True}
    assert tree["signal_data"] == {"format": "parquet", "chunks": 1, "bytes": 32}
    # The samples live in the Parquet chunk, so the archive stays the only copy.
    assert tree["unparsed_members"] == ["parquet/run2875/0"]
    assert tree["suites"] == [] and tree["tests"] == []


@pytest.mark.asyncio
async def test_sdi_session_is_written_as_its_own_page(tmp_path):
    source = _sdi_mldatx(tmp_path)
    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "WindTurbineSDI"
    payload = json.loads((root / "session.json").read_text(encoding="utf-8"))
    assert payload["kind"] == "sdi"
    assert payload["runs"][0]["model"] == "WEC_StateMachine"
    assert not (root / "tests.json").exists()
    assert (root / "WindTurbineSDI.mldatx").is_file()
    assert result.meta["original_preserved"] is True


def test_mldatx_without_a_known_layout_only_indexes_its_members(tmp_path):
    """A layout neither reader knows is indexed, not guessed at."""
    path = tmp_path / "session.mldatx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("notes/readme.txt", "handover")
    tree = parse_mldatx(path)
    assert tree["kind"] == "generic"
    assert tree["members"] == [{"name": "notes/readme.txt", "bytes": 8}]
    assert "left to the description stage" in tree["boundary"]


@pytest.mark.asyncio
async def test_test_file_with_non_xml_members_keeps_its_bytes(tmp_path):
    """Non-XML test data is listed, not decoded, so the container stays too."""
    source = tmp_path / "tests.mldatx"
    with zipfile.ZipFile(source, "w") as archive:
        archive.writestr(
            "testSuite.xml",
            '<TestSuite name="battery"><TestCase name="heat"/></TestSuite>',
        )
        archive.writestr("battery/inputs.mat", b"\x00mat")
    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "tests"
    payload = json.loads((root / "tests.json").read_text(encoding="utf-8"))
    assert payload["unparsed_members"] == ["battery/inputs.mat"]
    assert (root / "tests.mldatx").is_file()
    assert result.meta["original_preserved"] is True


def test_requirement_set_extracts_requirements_and_links(tmp_path):
    path = tmp_path / "requirements.slreqx"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "requirements.xml",
            '<requirements><requirement id="R1"><description>Battery below 45 C</description>'
            '</requirement><link source="R1" target="block_42"/></requirements>',
        )
    tree = parse_requirement_set(path)
    assert tree["requirements"][0]["id"] == "R1"
    assert "Battery below 45 C" in json.dumps(tree, ensure_ascii=False)
    assert tree["links"][0]["attributes"]["target"] == "block_42"


def test_mlapp_keeps_classdef_and_component_tree(tmp_path):
    scipy_io = pytest.importorskip("scipy.io")
    path = tmp_path / "panel.mlapp"
    document = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>"
        '<w:p><w:pPr><w:pStyle w:val="code"/></w:pPr><w:r><w:t>classdef panel &lt; matlab.apps.AppBase</w:t></w:r></w:p>'
        '<w:p><w:pPr><w:pStyle w:val="text"/></w:pPr><w:r><w:t>Battery panel</w:t></w:r></w:p>'
        "</w:body></w:document>"
    )
    buffer = io.BytesIO()
    scipy_io.savemat(buffer, {"components": {"Type": "uifigure", "Name": "panel"}})
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("matlab/document.xml", document)
        archive.writestr("appdesigner/appModel.mat", buffer.getvalue())
    tree, files = parse_mlapp(path)
    assert "classdef panel" in tree["code"]
    assert tree["components"] is not None
    assert tree["component_status"] == "parsed"
    assert "code.m" in files


@pytest.mark.asyncio
async def test_mlapp_keeps_only_the_classdef_source(tmp_path):
    scipy_io = pytest.importorskip("scipy.io")
    path = tmp_path / "panel.mlapp"
    document = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>"
        '<w:p><w:pPr><w:pStyle w:val="code"/></w:pPr><w:r><w:t>classdef panel &lt; matlab.apps.AppBase</w:t></w:r></w:p>'
        '<w:p><w:pPr><w:pStyle w:val="text"/></w:pPr><w:r><w:t>Battery panel</w:t></w:r></w:p>'
        "</w:body></w:document>"
    )
    buffer = io.BytesIO()
    scipy_io.savemat(buffer, {"components": {"Type": "uifigure", "Name": "panel"}})
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("matlab/document.xml", document)
        archive.writestr("appdesigner/appModel.mat", buffer.getvalue())

    store = LocalParseOutputStore(tmp_path / "artifacts")
    result = await MatlabParser().parse(path, parse_output_store=store)
    root = Path(result.artifact_ref.root)
    files = [
        item.name
        for item in root.iterdir()
        if item.is_file() and item.name != ".artifact_manifest.json"
    ]
    # Only the classdef source is kept, at the root, named after the app.
    assert files == ["panel.mlapp.m"]
    assert "classdef panel" in (root / "panel.mlapp.m").read_text(encoding="utf-8")
    assert not (root / "panel").exists()
    assert result.meta["original_preserved"] is False


@pytest.mark.asyncio
async def test_unreadable_mlapp_keeps_the_original_file(tmp_path):
    path = tmp_path / "broken.mlapp"
    path.write_bytes(b"not-a-zip")
    store = LocalParseOutputStore(tmp_path / "artifacts")
    result = await MatlabParser().parse(path, parse_output_store=store)
    root = Path(result.artifact_ref.root)
    files = [
        item.name
        for item in root.iterdir()
        if item.is_file() and item.name != ".artifact_manifest.json"
    ]
    assert files == ["broken.mlapp"]
    assert (root / "broken.mlapp").read_bytes() == b"not-a-zip"
    assert result.meta["original_preserved"] is True


def test_protected_metadata_is_verifiable(tmp_path):
    path = tmp_path / "secret.p"
    path.write_bytes(b"\x00pcode-bytes")
    metadata = protected_metadata(path, "pcode")
    assert metadata["parse_status"] == "opaque"
    assert metadata["original_preserved"] is True
    assert len(metadata["sha256"]) == 64


@pytest.mark.asyncio
async def test_parser_keeps_protected_original_and_requirement_json(tmp_path):
    store = LocalParseOutputStore(tmp_path / "artifacts")
    protected = tmp_path / "secret.slxp"
    protected.write_bytes(b"protected-model")
    result = await MatlabParser().parse(protected, parse_output_store=store)
    root = Path(result.artifact_ref.root)
    assert (root / "secret" / "secret.slxp").read_bytes() == b"protected-model"
    metadata = json.loads((root / "secret" / "metadata.json").read_text(encoding="utf-8"))
    assert metadata["original_preserved"] is True

    requirements = tmp_path / "requirements.slreqx"
    with zipfile.ZipFile(requirements, "w") as archive:
        archive.writestr(
            "requirements.xml",
            '<requirements><requirement id="R1"><description>Battery below 45 C</description>'
            "</requirement></requirements>",
        )
    result = await MatlabParser().parse(requirements, parse_output_store=store)
    root = Path(result.artifact_ref.root)
    assert not (root / "requirements" / "requirements.slreqx").exists()
    rows = [
        json.loads(line)
        for line in (root / "requirements" / "requirements.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]
    assert rows[0]["id"] == "R1"
    assert "Battery below 45 C" in rows[0]["description"]


def test_mat_shapes_struct_fields_and_m_source():
    flames = SAMPLE / "data" / "flames.mat"
    content, warnings = parse_mat(flames)
    entries = [json.loads(line) for line in content.splitlines()]
    variable = next(item for item in entries if item.get("name") == "X")
    assert variable["dims"] == [100, 100]
    assert variable["class"] == "uint8"
    assert not warnings

    documents, warnings = parse_mat_documents(flames)
    image = load_npy(documents, variable["data"])
    assert image.shape == (100, 100)
    assert "entries.jsonl" in documents
    # One flat workspace per .mat: arrays carry no directory of their own.
    assert variable["data"].count("/") == 0
    assert all("/" not in name for name in documents if name.endswith(".npy"))
    assert not warnings

    dataset = (
        SAMPLE
        / "model"
        / "VirtualVehicle"
        / "Electrical"
        / "Plant"
        / "Calibrations"
        / "DeepLearningBattery"
        / "TransientBatteryTestDataset.mat"
    )
    agent, _ = parse_mat(dataset)
    # SciPy names the recoverable array of an opaque object differently across
    # versions (``._ObjectMetadata`` vs ``.arr``); either way it is exported.
    assert "opaque_object" in agent or "DLBatteryTestData[1]._ObjectMetadata" in agent

@pytest.mark.asyncio
async def test_builtin_parser_writes_real_nested_artifact(tmp_path):
    store = LocalParseOutputStore(tmp_path)
    parser = MatlabParser()
    result = await parser.parse(CONTROLLER, parse_output_store=store)
    root = Path(result.artifact_ref.root)
    docs = [
        path
        for path in root.rglob("*.json")
        if json.loads(path.read_text(encoding="utf-8")).get("schema") == "ov.matlab.simulink/1"
    ]

    assert result.meta["system_count"] == 32
    assert result.meta["block_count"] == 478
    assert result.meta["stateflow_chart_count"] == 2
    assert result.meta["stateflow_state_count"] == 28
    assert result.meta["stateflow_function_count"] == 9
    assert result.meta["stateflow_note_count"] == 0
    assert result.meta["stateflow_transition_count"] == 40
    assert len(docs) == 32
    model_root = root / "HevIpsPowertrainController"
    assert (model_root / "main.json").is_file()
    assert (model_root / "IPS_Supervisory_Control" / "main.json").is_file()
    assert (model_root / "Accel_Pedal_to_Traction_Wheel_Torque_Request.json").is_file()
    timer = model_root / "stateflow" / "IPS_Supervisory_Control_Operating_Modes.EngOnCalc_Check_Power_Timer.json"
    assert "after(0.1, sec)" in timer.read_text(encoding="utf-8")
    chart_link = json.loads(
        (model_root / "IPS_Supervisory_Control" / "main.json").read_text(encoding="utf-8")
    )["stateflow"][0]
    assert chart_link == {
        "chart": "IPS Supervisory Control",
        "path": "stateflow/IPS_Supervisory_Control.json",
    }
    assert (model_root / "stateflow" / "IPS_Supervisory_Control.json").is_file()
    # Every child path in a system JSON resolves inside the artifact.
    for document in docs:
        payload = json.loads(document.read_text(encoding="utf-8"))
        for child in payload.get("children", []):
            assert (document.parent / child["path"]).resolve().is_file(), (document, child["path"])
    assert (root / ".artifact_manifest.json").is_file()
    assert result.parser_name == "MatlabParser"
    assert not (model_root / "HevIpsPowertrainController.slx").exists()
    assert not list(model_root.rglob("*.md"))
@pytest.mark.asyncio
async def test_whole_joint_project_upload_including_p_code(tmp_path):
    store = LocalParseOutputStore(tmp_path)
    result = await DirectoryParser().parse(
        SAMPLE,
        matlab=True,
        parse_output_store=store,
        strict=True,
        preserve_structure=True,
        language="zh-CN",
    )
    root = Path(result.artifact_ref.root)

    assert result.warnings == []
    assert result.meta["unsupported_files"] == []
    # 74 = the previous 73 plus the editor backup, which the rules table excludes.
    assert len(result.meta["skipped_files"]) == 74
    assert any(item["path"].endswith(".asv") for item in result.meta["skipped_files"])
    system_pages = [
        path
        for path in root.rglob("*.json")
        if json.loads(path.read_text(encoding="utf-8")).get("schema") == "ov.matlab.simulink/1"
    ]
    assert len(system_pages) > 500
    base = root / "matlab-ingest-fixture"
    assert (base / "data" / "flames" / "entries.jsonl").is_file()
    assert not list((base / "data" / "flames").glob("*.mat"))
    # Arrays of one MAT file are siblings of entries.jsonl, not a data/ level.
    assert not (base / "data" / "flames" / "data").exists()
    assert list((base / "data" / "flames").glob("*.npy"))
    assert (
        base
        / "model"
        / "asbCubeSatMBSE"
        / "MissionAnalysis"
        / "mappingToolboxAnalysis"
        / "notebook.json"
    ).is_file()
    assert list(
        (
            base
            / "model"
            / "asbCubeSatMBSE"
            / "MissionAnalysis"
            / "mappingToolboxAnalysis"
            / "outputs"
        ).glob("*.png")
    )
    dictionary = (
        base
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatMBSEModel"
        / "ModelData"
        / "asbCubeSatArchInterfaceData"
    )
    assert (dictionary / "entries.jsonl").is_file()
    assert not list(dictionary.glob("*.sldd"))
    assert not (dictionary / "data").exists()
    assert (base / "src" / "detectChangeOrbitalElements.m").is_file()
    assert not (base / "src" / "detectChangeOrbitalElements.m.md").exists()
    assert list((base / "bin").rglob("*.dll"))
    # Unpackable sources are the file itself: no wrapper folder, no metadata.
    assert (base / "bin" / "AddOnInstaller.exe").is_file()
    assert not (base / "bin" / "AddOnInstaller").exists()
    assert (base / "bin" / "ingest_firmware.hex").is_file()
    assert (base / "bin" / "visionzynq-target-eventhandler.elf").is_file()
    assert list((base / "model" / "VirtualVehicle" / "PassVeh" / "Plant").glob("*.STL"))
    assert (base / "build").exists() is False  # generated files are skipped, not imported
    assert (base / "slprj").exists() is False
    assert (base / "skipped.json").is_file()
    assert (base / "matlab-classification.json").is_file()
    # Installer packages keep only the source bytes; no manifest is produced.
    assert (base / "packages" / "IngestFixtureSupport.mlpkginstall").is_file()
    assert not (base / "packages" / "IngestFixtureSupport").exists()
    assert (base / "packages" / "IngestFixtureApp.mlappinstall").is_file()
    assert not (base / "packages" / "IngestFixtureApp").exists()
    assert (base / "packages" / "asbCubeSatMBSEProject" / "manifest.json").is_file()

    # P-code is imported as the original file, with no sidecar.
    pcode = base / "src" / "autoblkscheckparams.p"
    assert pcode.is_file()
    assert pcode.read_bytes() == (SAMPLE / "src" / "autoblkscheckparams.p").read_bytes()
    assert not (base / "src" / "autoblkscheckparams").exists()
    sources = [path for path in SAMPLE.rglob("*") if path.is_file()]
    # The fixture grows with each official example corpus that lands in it.
    assert len(sources) > 3000


@pytest.mark.asyncio
async def test_directory_import_keeps_one_folder_per_slx_model(tmp_path):
    """Single-system models in one folder must not overwrite each other's main.json."""
    plant = SAMPLE / "model" / "VirtualVehicle" / "PassVeh" / "Plant"
    names = ["SteeringSystem", "NoSuspension", "IMUSensor"]
    source = tmp_path / "plant"
    source.mkdir()
    for name in names:
        shutil.copyfile(plant / f"{name}.slx", source / f"{name}.slx")

    result = await DirectoryParser().parse(
        source,
        matlab=True,
        parse_output_store=LocalParseOutputStore(tmp_path / "artifacts"),
        preserve_structure=True,
    )
    root = Path(result.artifact_ref.root)
    systems = {
        json.loads(path.read_text(encoding="utf-8"))["system"]: path
        for path in root.rglob("main.json")
    }

    assert set(names) <= set(systems)
    for name in names:
        assert systems[name].parent.name == name


@pytest.mark.parametrize("value", [True, "true", "TRUE", 1, "yes"])
def test_matlab_argument_reads_as_a_declaration(value):
    assert matlab_requested(value) is True


@pytest.mark.parametrize("value", [False, "false", "0", "", None, 0, "off"])
def test_matlab_argument_is_not_declared_by_a_negative_value(value):
    assert matlab_requested(value) is False


def test_registry_no_longer_claims_matlab_extensions():
    """No extension selects the MATLAB parser by itself any more."""
    registry = ParserRegistry()
    for suffix in (".slx", ".sldd", ".mlx", ".mat", ".m", ".p"):
        assert registry.get_parser_for_file(f"model{suffix}") is None
    # It is still registered, just reachable by name.
    assert isinstance(registry.get_parser("matlab"), MatlabParser)


@pytest.mark.asyncio
async def test_explicit_arg_routes_one_file_to_the_matlab_parser(tmp_path):
    path = tmp_path / "notes.m"
    path.write_text("function y=notes()\ny=1;\nend\n", encoding="utf-8")
    store = LocalParseOutputStore(tmp_path / "artifacts")

    declared = await ParserRegistry().parse(path, matlab=True, parse_output_store=store)
    ordinary = await ParserRegistry().parse(path, parse_output_store=store)

    assert declared.parser_name == "MatlabParser"
    assert ordinary.parser_name != "MatlabParser"


@pytest.mark.asyncio
async def test_directory_without_the_argument_imports_nothing_as_matlab(tmp_path):
    """A tree of models is an ordinary directory unless args.matlab=true was given."""
    plant = SAMPLE / "model" / "VirtualVehicle" / "PassVeh" / "Plant"
    source = tmp_path / "plant"
    source.mkdir()
    shutil.copyfile(plant / "SteeringSystem.slx", source / "SteeringSystem.slx")
    (source / "notes.m").write_text("x = 1;\n", encoding="utf-8")

    result = await DirectoryParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root)

    assert not list(root.rglob("main.json"))
    assert not (root / "plant" / "matlab-classification.json").exists()
    assert "matlab_classification" not in result.meta
    processed = {item["path"]: item["parser"] for item in result.meta["processed_files"]}
    # .m is ordinary text here: written as the file itself, never as a model page.
    assert processed["notes.m"] == "direct"
    assert [item["path"] for item in result.meta["unsupported_files"]] == ["SteeringSystem.slx"]


def _write_semantic_slx(path: Path):
    def block(kind, name, sid, properties="", system=""):
        return (
            f'<Block BlockType="{kind}" Name="{name}" SID="{sid}">{properties}'
            + (f'<System Ref="{system}"/>' if system else "")
            + "</Block>"
        )

    root = """<System>
      <Block BlockType="SubSystem" Name="Enabled" SID="1"><System Ref="system_1"/></Block>
      <Block BlockType="SubSystem" Name="Variants" SID="2"><P Name="Variant">on</P><P Name="VariantControlMode">expression</P><System Ref="system_2"/></Block>
      <Block BlockType="ConnectionPort" Name="Electrical +" SID="3"><P Name="Port">1</P><P Name="Side">Left</P><P Name="Domain">electrical</P></Block>
      <Block BlockType="ConnectionPort" Name="Electrical -" SID="4"><P Name="Port">2</P><P Name="Side">Right</P><P Name="Domain">electrical</P></Block>
      <Block BlockType="PMIOPort" Name="Torque" SID="5"><P Name="Port">3</P><P Name="Side">Right</P></Block>
      <Line><P Name="Src">3#rconn:1</P><P Name="Dst">4#lconn:1</P></Line>
    </System>"""
    enabled = """<System><Block BlockType="EnablePort" Name="Enable" SID="11"><P Name="StatesWhenEnabling">held</P></Block>
      <Block BlockType="TriggerPort" Name="Trigger" SID="12"><P Name="TriggerType">rising</P></Block></System>"""
    variants = '<System><Block BlockType="SubSystem" Name="High power" SID="21"><P Name="VariantControl">V == 1</P><System Ref="system_3"/></Block></System>'
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "simulink/blockdiagram.xml",
            '<BlockDiagram><Model><System Ref="system_root"/></Model></BlockDiagram>',
        )
        for ref, xml in (("root", root), ("1", enabled), ("2", variants), ("3", "<System/>")):
            archive.writestr(f"simulink/systems/system_{ref}.xml", xml)


def test_subsystem_types_controls_variant_choices_and_physical_ports(tmp_path):
    path = tmp_path / "semantic.slx"
    _write_semantic_slx(path)
    model = parse_slx(path)
    documents = system_json_documents(model)
    assert model.subsystem_types == ["subsystem"]
    assert model.children[0].subsystem_types == ["enabled", "triggered"]
    assert model.children[1].subsystem_types == ["variant"]
    root = documents["main.json"]
    assert root["type"] == "simulink-model"
    enabled = documents["Enabled.json"]
    assert any("held" in block["description"] for block in enabled["blocks"])
    variants = documents["Variants/main.json"]
    assert variants["type"] == "simulink-subsystem"
    root_blocks = {block["name"]: block for block in root["blocks"]}
    assert root_blocks["Variants"]["key"] is None
    variant_blocks = {block["name"]: block for block in variants["blocks"]}
    assert variant_blocks["High power"]["key"] is None
    assert variant_blocks["High power"]["description"] == ""
    by_name = {block["name"]: block for block in root["blocks"]}
    model_blocks = {block.name: block for block in model.blocks}
    assert model_blocks["Electrical +"].block_type == "ConnectionPort"
    assert by_name["Electrical +"]["key"] == "ConnectionPort"
    assert by_name["Electrical +"]["description"] == ""
    assert by_name["Electrical +"]["ports"]["conn"] == ["Electrical +"]
    assert model_blocks["Torque"].block_type == "PMIOPort"
    assert by_name["Torque"]["ports"]["conn"] == ["Torque"]
@pytest.mark.asyncio
async def test_legacy_mdl_requirements_and_binary_metadata(tmp_path):
    mdl = SAMPLE / "src" / "slctrlobsolete.mdl"
    result = await MatlabParser().parse(
        mdl, parse_output_store=LocalParseOutputStore(tmp_path / "mdl")
    )
    root = Path(result.artifact_ref.root)
    assert (root / "slctrlobsolete" / "main.json").is_file()

    req = (
        SAMPLE
        / "model"
        / "asbCubeSatMBSE"
        / "CubeSatRequirements"
        / "ACSRequirements.slreqx"
    )
    result = await MatlabParser().parse(
        req, parse_output_store=LocalParseOutputStore(tmp_path / "req")
    )
    root = Path(result.artifact_ref.root)
    requirements = (root / "ACSRequirements" / "requirements.jsonl").read_text(
        encoding="utf-8"
    )
    assert "CubeSat" in requirements
    assert (root / "ACSRequirements" / "links.jsonl").is_file()

    mex = SAMPLE / "src" / "componentinfo.mexw64"
    store = LocalParseOutputStore(tmp_path / "mex")
    result = await MatlabParser().parse(mex, parse_output_store=store)
    root = Path(result.artifact_ref.root)
    assert result.artifact_ref.root_type == "file"
    assert result.meta["parse_status"] == "original-only"
    assert (root / "componentinfo.mexw64").read_bytes() == mex.read_bytes()
    assert sorted(path.name for path in root.iterdir()) == [
        ".artifact_manifest.json",
        "componentinfo.mexw64",
    ]


@pytest.mark.asyncio
async def test_unpackable_and_installer_files_resolve_as_file_nodes(tmp_path):
    """Only the source file is produced, and it resolves as one flat file node."""
    store = LocalParseOutputStore(tmp_path / "artifacts")
    cases = [
        ("src/autoblkscheckparams.p", "autoblkscheckparams.p"),
        ("src/componentinfo.mexw64", "componentinfo.mexw64"),
        ("bin/fmu2ProxyWrapper.dll", "fmu2ProxyWrapper.dll"),
        ("bin/AddOnInstaller.exe", "AddOnInstaller.exe"),
        ("bin/GecodeDriver.lib", "GecodeDriver.lib"),
        ("bin/lcccrt0.obj", "lcccrt0.obj"),
        ("bin/libMatlabCppSharedLib25_2.pdb", "libMatlabCppSharedLib25_2.pdb"),
        ("packages/IngestFixtureApp.mlappinstall", "IngestFixtureApp.mlappinstall"),
        ("packages/IngestFixtureSupport.mlpkginstall", "IngestFixtureSupport.mlpkginstall"),
    ]
    for rel_path, name in cases:
        source = SAMPLE / rel_path
        result = await MatlabParser().parse(source, parse_output_store=store)
        root = Path(result.artifact_ref.root)
        assert result.artifact_ref.root_type == "file", rel_path
        assert result.meta["original_preserved"] is True, rel_path
        assert result.meta["parse_status"] == "original-only", rel_path
        entries = sorted(
            path.name for path in root.iterdir() if path.name != ".artifact_manifest.json"
        )
        assert entries == [name], rel_path
        assert (root / name).read_bytes() == source.read_bytes(), rel_path
        resolved = await resolve_artifact_doc_root(store, result.artifact_ref)
        assert resolved.root_is_file is True, rel_path
        assert resolved.doc_name == name, rel_path
        assert resolved.doc_rel == name, rel_path


@pytest.mark.asyncio
async def test_xlsx_cells_are_read_instead_of_the_workbook_bytes(tmp_path):
    """A project spreadsheet is a table: every sheet is stored as cells."""
    source = (
        SAMPLE
        / "model"
        / "VirtualVehicle"
        / "SI"
        / "Plant"
        / "Calibrations"
        / "MappedEngine"
        / "SiEngineData.xlsx"
    )
    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "SiEngineData"

    assert sorted(path.name for path in root.iterdir()) == ["workbook.json", "workbook.md"]
    payload = json.loads((root / "workbook.json").read_text(encoding="utf-8"))
    assert payload["schema"] == "ov.matlab.workbook/1"
    assert payload["parse_status"] == "parsed"
    assert payload["summary"]["sheet_names"] == ["Firing Data", "Nonfiring Data"]
    firing = payload["sheets"][0]
    assert firing["range"].startswith("A1:")
    assert firing["header"][:4] == ["Name:", "Torque", "EngSpd", "AirMassFlwRate"]
    # Numbers stay numbers; a blank cell stays a hole instead of shifting the row.
    assert firing["cells"][2][0] == "Data:"
    assert isinstance(firing["cells"][2][1], float)
    assert firing["cells"][3][0] is None
    assert isinstance(firing["cells"][3][1], float)
    assert result.meta["original_preserved"] is False
    assert result.meta["sheet_count"] == 2
    assert result.meta["cell_count"] > 2000
    assert result.meta["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    page = (root / "workbook.md").read_text(encoding="utf-8")
    assert "## Firing Data" in page
    assert "Torque" in page


@pytest.mark.asyncio
async def test_xlsx_formulas_dates_and_merged_ranges_are_kept(tmp_path):
    """Cells carry their formula, a date-formatted number, and merged ranges."""
    openpyxl = pytest.importorskip("openpyxl")
    import datetime

    source = tmp_path / "calibration.xlsx"
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Table"
    sheet["A1"] = "speed"
    sheet["B1"] = "torque"
    sheet["A2"] = 100
    sheet["B2"] = "=A2*2"
    sheet["A3"] = datetime.date(2026, 5, 4)
    sheet["A3"].number_format = "yyyy-mm-dd"
    sheet["C1"] = True
    sheet.merge_cells("D1:E1")
    sheet["D1"] = "merged label"
    workbook.save(source)

    payload = parse_workbook(source)
    table = payload["sheets"][0]
    assert table["formulas"] == {"B2": "=A2*2"}
    # openpyxl stores the formula without a cached result, so the cell has no value.
    assert table["cells"][1][1] is None
    assert table["cells"][2][0] == "2026-05-04"
    assert table["cells"][0][2] is True
    assert table["merged"] == ["D1:E1"]
    assert "=A2*2" in workbook_text(payload)


@pytest.mark.asyncio
async def test_unreadable_workbook_keeps_its_bytes(tmp_path):
    """A renamed or damaged workbook is kept as the file itself."""
    source = tmp_path / "legacy.xlsx"
    source.write_bytes(b"not a zip at all")
    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "legacy"
    assert (root / "legacy.xlsx").read_bytes() == source.read_bytes()
    payload = json.loads((root / "workbook.json").read_text(encoding="utf-8"))
    assert payload["parse_status"] == "unreadable"
    assert result.meta["original_preserved"] is True
    assert any("单元格读取失败" in warning for warning in result.warnings)


@pytest.mark.asyncio
async def test_project_spreadsheet_is_routed_to_the_project_parser(tmp_path):
    """Inside a project the workbook is read as cells, not as a document page."""
    source = tmp_path / "plant"
    source.mkdir()
    shutil.copyfile(
        SAMPLE / "model" / "VirtualVehicle" / "PassVeh" / "Plant" / "SteeringSystem.slx",
        source / "SteeringSystem.slx",
    )
    shutil.copyfile(
        SAMPLE
        / "model"
        / "VirtualVehicle"
        / "Electrical"
        / "Plant"
        / "Calibrations"
        / "MappedMotor"
        / "EM1"
        / "MappedMotorDataset.xlsx",
        source / "MappedMotorDataset.xlsx",
    )
    result = await DirectoryParser().parse(
        source,
        matlab=True,
        parse_output_store=LocalParseOutputStore(tmp_path / "artifacts"),
    )
    root = Path(result.artifact_ref.root) / "plant"
    workbook = json.loads(
        (root / "MappedMotorDataset" / "workbook.json").read_text(encoding="utf-8")
    )
    assert workbook["sheets"][0]["name"] == "MBC Data"
    assert workbook["sheets"][0]["header"][:3] == ["Name:", "MtrSpd", "MtrTrq"]
    processed = {item["path"]: item["parser"] for item in result.meta["processed_files"]}
    assert processed["MappedMotorDataset.xlsx"] == "MatlabParser"


@pytest.mark.asyncio
async def test_template_members_are_expanded_into_the_tree(tmp_path):
    """A template archive ships its project: every fsroot member is parsed."""
    source = SAMPLE / "packages" / "asbCubeSatMBSEProject.sltx"
    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "asbCubeSatMBSEProject"
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))

    assert manifest["expansion"]["member_count"] == 46
    assert manifest["expansion"]["expanded"] == 46
    assert manifest["expansion"]["failed"] == []
    assert result.meta["expanded_member_count"] == 46
    # The archive bytes are gone once every member has been read.
    assert not list(root.glob("*.sltx"))
    assert result.meta["original_preserved"] is False
    members = root / "members" / "asbCubeSatMBSE"
    model = json.loads(
        (
            members
            / "CubeSatMBSEModel"
            / "CubeSatPlant"
            / "VehicleDynamics"
            / "asbCubeSatVehiclePlant"
            / "main.json"
        ).read_text(encoding="utf-8")
    )
    assert model["schema"] == "ov.matlab.simulink/1"
    assert model["blocks"], "model blocks are read out of the archive member"
    assert (members / "ProjectTasks" / "projectStartup.m").is_file()
    dictionary = members / "CubeSatMBSEModel" / "ModelData" / "asbCubeSatArchInterfaceData"
    assert (dictionary / "entries.jsonl").is_file()
    assert (members / "CubeSatRequirements" / "SystemRequirements" / "requirements.jsonl").is_file()


@pytest.mark.asyncio
async def test_binary_containers_are_the_resource_themselves(tmp_path):
    """A jar or ctf expands into nothing readable: the file is the resource."""
    store = LocalParseOutputStore(tmp_path / "artifacts")
    cases = [
        ("packages/addons.jar", "addons", "jar"),
        ("packages/mps_check.ctf", "mps_check", "ctf"),
    ]
    for rel_path, folder, kind in cases:
        source = SAMPLE / rel_path
        result = await MatlabParser().parse(source, parse_output_store=store)
        root = Path(result.artifact_ref.root) / folder
        assert sorted(path.name for path in root.iterdir()) == sorted(
            [source.name, "manifest.json"]
        ), rel_path
        assert (root / source.name).read_bytes() == source.read_bytes(), rel_path
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        assert manifest["type"] == kind
        assert manifest["members"], rel_path
        assert "原件作为资源保留" in manifest["boundary"]
        assert result.meta["original_preserved"] is True, rel_path


@pytest.mark.asyncio
async def test_toolbox_members_are_expanded_but_binaries_are_not(tmp_path):
    """A toolbox archive ships its source; its binaries are only named."""
    source = SAMPLE / "packages" / "IngestFixtureToolbox.mltbx"
    result = await MatlabParser().parse(
        source, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "IngestFixtureToolbox"

    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    expansion = manifest["expansion"]
    assert expansion["member_count"] == 6
    # The two scripts and the FMU (a model with a readable interface) expand; the
    # nested packages stay in the manifest only.
    assert expansion["expanded"] == 3
    assert expansion["failed"] == []
    reasons = {item["member"].rsplit("/", 1)[-1]: item["reason"] for item in expansion["skipped"]}
    assert set(reasons) == {"addons.jar", "asbCubeSatMBSEProject.sltx", "mps_check.ctf"}
    assert all("无可检索语义" in reason for reason in reasons.values())
    members = root / "members"
    assert (members / "detectChangeOrbitalElements.m").is_file()
    assert (members / "projectStartup.m").is_file()
    fmu = next(members.rglob("modelDescription.xml"))
    assert "VvcFmuEngExl" in fmu.read_text(encoding="utf-8")
    assert result.meta["expanded_member_count"] == 3
    assert result.meta["original_preserved"] is False


@pytest.mark.asyncio
async def test_project_archive_members_already_in_the_tree_are_not_duplicated(tmp_path):
    """A project export repeats its own tree: only what the tree lacks is added."""
    project = tmp_path / "proj"
    (project / "src").mkdir(parents=True)
    kept = project / "src" / "keep.m"
    kept.write_text("function y=keep()\ny=1;\nend\n", encoding="utf-8")
    shutil.copyfile(
        SAMPLE / "model" / "VirtualVehicle" / "PassVeh" / "Plant" / "SteeringSystem.slx",
        project / "SteeringSystem.slx",
    )
    archive = project / "packages" / "ExportedProject.mlproj"
    archive.parent.mkdir()
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr("fsroot/ExportedProject.prj", "project file")
        bundle.writestr("fsroot/src/keep.m", kept.read_text(encoding="utf-8"))
        bundle.writestr("fsroot/src/only_in_archive.m", "function y=f()\ny=2;\nend\n")
        bundle.writestr("fsroot/bin/engine.dll", b"MZ\x00\x00")

    result = await DirectoryParser().parse(
        project,
        matlab=True,
        parse_output_store=LocalParseOutputStore(tmp_path / "artifacts"),
    )
    root = Path(result.artifact_ref.root) / "proj" / "packages" / "ExportedProject"
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    expansion = manifest["expansion"]
    assert expansion["expanded"] == 2  # the .prj and the member the tree lacks
    reasons = {item["member"]: item["reason"] for item in expansion["skipped"]}
    assert reasons["fsroot/src/keep.m"] == "工程里已有同名同内容文件"
    assert "无可检索语义" in reasons["fsroot/bin/engine.dll"]
    members = root / "members"
    assert (members / "src" / "only_in_archive.m").is_file()
    assert not (members / "src" / "keep.m").exists()
    assert not (members / "bin").exists()


@pytest.mark.asyncio
async def test_archive_members_are_kept_when_the_tree_is_not_there(tmp_path):
    """The same archive imported on its own keeps every member it can read."""
    archive = tmp_path / "Alone.mlproj"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr("fsroot/src/keep.m", "function y=keep()\ny=1;\nend\n")
        bundle.writestr("fsroot/bin/engine.dll", b"MZ\x00\x00")
    result = await MatlabParser().parse(
        archive, parse_output_store=LocalParseOutputStore(tmp_path / "artifacts")
    )
    root = Path(result.artifact_ref.root) / "Alone"
    assert (root / "members" / "src" / "keep.m").is_file()
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["expansion"]["expanded"] == 1
    assert [item["member"] for item in manifest["expansion"]["skipped"]] == ["fsroot/bin/engine.dll"]
