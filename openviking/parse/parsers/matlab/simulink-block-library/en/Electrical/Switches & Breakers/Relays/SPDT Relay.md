---
type: simulink-block
title: 'SPDT Relay'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers / Relays'
documentation_page: 'spdtrelay'
documentation_source_path: 'ref/spdtrelay.html'
language: en
---

# SPDT Relay

## Ports

### Input

### **PS** — Physical signal control physical signal

Physical signal input port that energizes and de-energizes the
relay.

#### Dependencies

To enable this port, in the **Main** settings, set the
**Control port** parameter to
`PS`.
### Output

### **x** — Relay state physical signal

State of the relay in terms of the
**C**–**S1**
and
**C**–**S2** connections:

- 1 — Closed connection
- 0 — Open connection

#### Dependencies

To enable this port, in the **Main** settings, set the **State
port** parameter to
`Visible`.
### Conserving

### **S1** — Normally closed contact electrical

Electrical conserving port associated with the normally closed contact.

### **C** — Common contact electrical

Electrical conserving port associated with the common contact.

### **S2** — Normally open contact electrical

Electrical conserving port associated with the normally open contact.

### **+** — Winding positive terminal electrical

Electrical conserving port associated with the winding positive voltage terminal. The
current through the winding controls the relay state.

#### Dependencies

To enable this port, in the **Main** settings, set the
**Control port** parameter to
`Electrical`.

### **-** — Winding negative terminal electrical

Electrical conserving port associated with the winding negative voltage terminal The
current through the winding controls the relay state.

#### Dependencies

To enable this port, in the **Main** settings, set the
**Control port** parameter to
`Electrical`.

## Parameters

### Main

### **Control port** — Input port choice `PS` (default) | `Electrical`

Relay state control method:

- `PS` —
  **PS** physical signal input
  port
- `Electrical` —
  **+** and **-**
  electrical conserving ports associated with the relay
  winding terminals

The table shows how this parameter affects the visibility of other
parameters in the **Main** settings. To learn how to
read the table, see Parameter Dependencies.

****Control Port** Parameter
Dependencies**

| **Control port** | |
| --- | --- |
| `PS` | `Electrical` |
| **Closed resistance** | **Closed resistance** |
| **Open conductance** | **Open conductance** |
| **Threshold** |
| **State port** | **State port** |
| **Common port** |

### **Closed resistance** — Connected contact resistance `0.01` `Ohm` (default) | positive scalar

Resistance across closed relay contacts. The parameter value must be
greater than zero.

### **Open conductance** — Open-circuit conductance `1e-8` `1/Ohm` (default) | positive scalar

Conductance across open relay contacts. The parameter value must be
greater than zero.

### **Threshold** — Relay threshold `0` (default) | nonnegative scalar

If the physical signal input is above the threshold value, the relay is energized.
Conversely, if the physical signal input falls is the threshold value,
the relay is de-energized.

#### Dependencies

To enable this parameter, set **Control port** to
`PS`.

### **State port** — Relay state output port visibility `Hidden` (default) | `Visible`

Visibility of the physical signal port that outputs the relay state. The port outputs a
vector of length two, with the first element corresponding to the
**C**–**S1**
connection and the second to the
**C**–**S2**
connection. The elements are `1` if the corresponding
connection is closed, and `0` otherwise.

### **Common port** — Common port location `Adjacent to switch ports` (default) | `Across from switch ports`

Location of the common port, **C**, relative to the
**S1** and **S2** ports.

#### Dependencies

To enable this parameter, set **Control port** to
`PS`.

### Winding

To enable these parameters, in the **Main** settings, set the
**Control port** parameter to
`Electrical`.

### **Rated voltage** — Rated voltage `5` `V` (default) | positive scalar

Standard voltage applied to the operating coil under normal operating conditions. The
current threshold depends on the value of this parameter.

### **Percent rated voltage to energize** — Percent rated voltage to energize `75` (default) | positive scalar

Minimum percent of the rated voltage required to energize the relay.
The current threshold depends on the value of this parameter.

### **Percent rated voltage to de-energize** — Percent rated voltage to de-energize `25` (default) | positive scalar

Percent of the rated voltage required to de-energize the relay. The current threshold
depends on the value of this parameter.

### **Winding inductance** — Winding inductance `0.08` `H` (default) | positive scalar

Winding inductance.

### **Winding series resistance** — Winding series resistance `12.5` `Ohm` (default) | positive scalar

Resistance between the winding terminals. The current threshold depends on the value of
this parameter.

### **Winding parallel conductance** — Winding parallel conductance `1e-9` `1/Ohm` (default) | positive scalar

Winding conductance.

### Mechanical

### **Time-to-break C-S1 connection** — Delay time for breaking connection **C**–**S1** `0` `s` (default) | nonnegative scalar

Mechanical switching time for breaking the connection between ports
**C** and **S1** when the relay is
energized.

### **Time-to-make C-S1 connection** — Delay time for making connection **C**–**S1** `0` `s` (default) | nonnegative scalar

Mechanical switching time for making the connection between ports **C**
and **S1** when the relay is de-energized.

### **Time-to-break C-S2 connection** — Delay time for breaking connection **C**–**S2** `0` `s` (default) | nonnegative scalar

Mechanical switching time for breaking the connection between ports
**C** and **S2** when the relay is
energized.

### **Time-to-make C-S2 connection** — Delay time for making connection **C**–**S2** `0` `s` (default) | nonnegative scalar

Mechanical switching time for making the connection between ports **C**
and **S2** when the relay is de-energized.

### Faults

### **Switch fault** — Option to add switch fault `Add fault`

Option to add a switch fault.

To add a fault, click the **Add fault**
hyperlink.

### **Switch fault** — Switch fault model `C-S1 stuck closed` (default) | `C-S2 stuck closed` | `C open circuit (no path to S1 or S2)` | `Degraded contact resistance`

Switch fault model.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Switch fault**
parameter.

### **Trigger type** — Trigger type `Always on` (default) | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

Trigger type, specified as one of these options:

- `Always On` — The fault injects at the start of the
  simulation.
- `Timed` — The fault injects when the simulation time
  reaches the value you specify for the **Trigger fault at time**
  parameter.
- `Behavioral` — The fault injects as a result of fault
  parameter values during simulation. Setting **Trigger type** to
  `Behavioral` enables block parameters that define
  the failure conditions.
- `Additional triggers` — The fault injects as a result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. The
    block enters the faulted state when the trigger condition becomes true
    for the first time and remains in the faulted state for the rest of the
    simulation. To learn more, see Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Switch fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Switch fault** parameter and
set **Trigger type** to
`Timed`.

### **Maximum permissible load current** — Maximum permissible load current `inf` `A` (default) | positive scalar

Current threshold for a fault transition. The block enters the faulted state if the current
continuously exceeds this value for a period longer than the value of the **Time to
fail when exceeding current** parameter.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Switch fault** parameter and
set **Trigger type** to
`Behavioral`.

### **Time to fail when exceeding current** — Time to fail when exceeding current `1` `s` (default) | positive scalar

Amount of time that the current must continuously exceed the maximum permissible current
before a fault triggers.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Switch fault** parameter and
set **Trigger type** to
`Behavioral`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Switch fault** parameter and
set **Trigger type** to
`Additional triggers`.

### **Degraded contact resistance C-S1** — Degraded contact resistance **C**–**S1** `1e-9` `Ohm` (default) | positive scalar

Degraded resistance of the faulted **S1**
contact.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Switch fault** parameter and
set **Switch fault** to
`Degraded contact resistance`.

### **Degraded contact resistance C-S2** — Degraded contact resistance **C**–**S2** `1e-9` `Ohm` (default) | positive scalar

Degraded resistance of the faulted **S2**
contact.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Switch fault** parameter and
set **Switch fault** to
`Degraded contact resistance`.

### **Time constant for degraded contact resistance** — Time constant for degraded contact resistance `1e-3` (default) | positive scalar

Time constant for contact resistance to fall into degraded status. The
degraded contact resistances for **S1** and
**S2** have the same time constant.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Switch fault** parameter and
set **Switch fault** to
`Degraded contact resistance`.

### **Winding fault** — Option to add winding fault `Add fault`

Option to add a winding fault.

To add a fault, click the **Add fault**
hyperlink.

#### Dependencies

To enable this parameter, set **Control port** to
`Electrical`.

### **Time constant for winding open circuit transition** — Time constant for winding to fail `1e-3` `s` (default) | positive scalar

Time constant for the winding to fail. This constant is the
characteristic time that describes a transition from a normal state to
an open circuit. You can calculate this value as the time it takes for
the response to reach 63% of its steady-state value when the fault
occurs.

#### Dependencies

To enable this parameter, set **Control port** to
`Electrical`and click the **Add
fault** hyperlink for the **Winding
fault** parameter.

### **Trigger type** — Trigger type `Always on` (default) | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

Trigger type, specified as one of these options:

- `Always On` — The fault injects at the start of the
  simulation.
- `Timed` — The fault injects when the simulation time
  reaches the value you specify for the **Trigger fault at time**
  parameter.
- `Behavioral` — The fault injects as a result of fault
  parameter values during simulation. Setting **Trigger type** to
  `Behavioral` enables block parameters that define
  the failure conditions.
- `Additional triggers` — The fault injects as a result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. The
    block enters the faulted state when the trigger condition becomes true
    for the first time and remains in the faulted state for the rest of the
    simulation. To learn more, see Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Winding fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter:

- Set **Control port** to
  `Electrical`.
- Click the **Add fault** hyperlink for
  the **Winding fault** parameter.
- Set **Trigger type** to
  `Timed`.

### **Maximum permissible winding voltage** — Maximum permissible winding voltage `inf` `V` (default) | positive scalar

Maximum voltage for the relay winding. The block enters the faulted
state if the voltage exceeds this value for the
*k*th time, where
*k* is the value of the **Number of events
to fail when exceeding voltage** parameter.

#### Dependencies

To enable this parameter:

- Set **Control port** to
  `Electrical`.
- Click the **Add fault** hyperlink for
  the **Winding fault** parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Number of events to fail when exceeding voltage** — Number of events to fail when exceeding voltage `1` (default) | positive scalar integer

Number of times the relay must exceed the winding voltage threshold
before a open-circuit winding fault triggers.

#### Dependencies

To enable this parameter:

- Set **Control port** to
  `Electrical`.
- Click the **Add fault** hyperlink for
  the **Winding fault** parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Maximum permissible winding current** — Maximum permissible winding current `inf` `A` (default) | positive scalar

Current threshold for a fault transition. The block enters the faulted
state if the current continuously exceeds this value for a period longer
than the value of the **Time to fail when exceeding winding
current** parameter.

#### Dependencies

To enable this parameter:

- Set **Control port** to
  `Electrical`.
- Click the **Add fault** hyperlink for
  the **Winding fault** parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Time to fail when exceeding winding current** — Time to fail when exceeding winding current `1` `s` (default) | positive scalar

Amount of time that the current must continuously exceed the maximum permissible current
before a fault triggers.

#### Dependencies

To enable this parameter:

- Set **Control port** to
  `Electrical`.
- Click the **Add fault** hyperlink for
  the **Winding fault** parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter:

- Set **Control port** to
  `Electrical`.
- Click the **Add fault** hyperlink for
  the **Winding fault** parameter.
- Set **Trigger type** to
  `Additional
  triggers`.

## Libraries

Simscape / Electrical / Switches & Breakers / Relays

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

### R2024a: Implement faults using the Simscape faults interface

The SPDT Relay block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

As a result of this change, the parameter names and dependencies in the
**Faults** settings have changed.

### R2023a: Implement temporal or behavioral triggers for faults using a single parameter

The **Enable temporal trigger** and **Enable behavioral trigger** parameters have been removed and are replaced with the **Fault
trigger** parameter. You can set the **Fault trigger**
parameter to `Temporal` or `Behavioral`.
You can enable only one trigger.

If you created a model in an earlier release and enabled both temporal and behavioral
triggers, now only the temporal trigger is enabled. Therefore, the simulation results are
different if the behavioral trigger causes the fault in your model.

If you want to trigger a fault at a specific time, set the **Fault trigger**
parameter to `Temporal`. If you want to determine whether a system
fails and, if so, when it fails, set the **Fault Trigger** parameter to
`Behavioral`.

## Description

Single-pole, double-throw relay with delays and faults

The SPDT Relay block models a single-pole, double-throw
relay. The block has three potential states:

- De-energized — The common contact, **C**, is
  connected to the normally closed contact, **S1**.
- Energized — The common contact, **C**, is
  connected to the normally open contact, **S2**.
- Open Circuit — The relay is open. The common contact,
  **C**, is not connected to the normally closed contact,
  **S1**, or the normally open contact,
  **S2**.

You can:

- Control the relay state using the physical signal input port or electrical
  conserving ports.
- Output the relay state.
- Delay the breaking and making of either or both of the connections.
- Introduce a behavioral or temporal fault that results in a stuck
  connection, an open circuit, or degraded contact resistance.

### Relay State Control

The block has two control variants:

- Physical signal (PS) control — The state of the relay depends
  on how the value of the input physical signal compares to the relay
  threshold. The relay threshold, *th*, is the value that
  you by specify for the **Threshold** parameter.
- Electrical control — The state of the relay depends on how the
  current through the positive and negative electrical conserving ports,
  which represent the relay winding, compares to the relay upper and lower
  thresholds. The upper and lower thresholds depend on the values that you
  specify for the parameters in the **Winding**
  settings.

For the PS control variant, at the start of simulation:

- If the input signal, *PS*, is less than or equal to
  *th*, the relay is de-energized and the common
  contact, **C**, connects to the normally closed
  contact, **S1**.
- If the input signal, *PS*, greater than
  *th*, the relay is energized and
  **C** connects to the normally open contact,
  **S2**.

After the simulation starts, if *PS* rises above *th*,
the block goes from a de-energized state to an energized state :

- The
  **C**–**S1**
  connection breaks after the delay specified in **Time-to-break
  C-S1 connection**.
- The
  **C**–**S2**
  connection closes after the delay specified in **Time-to-make
  C-S2 connection**.

If the block goes from an energized state to a de-energized state, that is
*PS* falls to or below *th*:

- The
  **C**–**S2**
  connection breaks after the delay specified in **Time-to-break
  C-S2 connection**.
- The
  **C**–**S1**
  connection closes after the delay specified in **Time-to-make
  C-S1 connection**.

For the electrical control variant, the upper and lower thresholds depend on the specified
values for the **Rated voltage**, **Percent rated voltage
to energize**, **Percent rated voltage to
de-energize**, and **Winding series resistance**
parameters. The rated current is:

irated=Vratedrcoil.

The equation for the upper current threshold,
*ienergized*, is:

ienergized\_current=Rated Voltage\*Percent rated voltage to energizeWinding series resistance .

The equation for the lower current threshold,
*ide-energized*, is:

ide−energized\_current=Rated Voltage\*Percent rated voltage to de−energizeWinding series resistance .

At the start of simulation:

- If the control current is less than
  *ienergized*, the common
  contact, **C**, connects to the normally closed
  contact, **S1**.
- If the control current is greater than
  *ienergized*, the relay
  is energized and **C** connects to the normally open
  contact, **S2**.

After the start of simulation, if the current rises above
*ienergized*, the block goes from a
de-energized state to an energized state:

- The
  **C**–**S1**
  connection breaks after the delay specified in **Time-to-break
  C-S1 connection**.
- The
  **C**–**S2**
  connection closes after the delay specified in **Time-to-make
  C-S2 connection**.

If the current falls below *ide-energized*, the
block goes from an energized state to a de-energized state:

- The
  **C**–**S2**
  connection breaks after the delay specified in **Time-to-break
  C-S2 connection**.
- The
  **C**–**S1**
  connection closes after the delay specified in **Time-to-make
  C-S1 connection**.

### Output the Relay State

To view the relay state, expose port **x**, a physical signal port that
outputs the state of each connection. To expose the **x** port, in
the **Main** settings, set **State port** to
`Visible`.

The table shows how the state of the relay relates to the state of the
connections. A closed connection has a state of 1. An open connection has a state of
0.

**Relay and Connection States**

| **C**–**S1** Connection State | **C**–**S2** Connection State | Relay State |
| --- | --- | --- |
| 1 | 0 | De-energized |
| 0 | 1 | Energized |
| 0 | 0 | Open Circuit |

### Connection Delays

You can specify delays for making and breaking connections in the
**Mechanical** settings. The table shows how the make and brake
time delays affect the connections between contacts **S1** and
**S2** and the common contact, **C**.

| **Mechanical** Settings | Relay State | **C**–**S1** Connection State | **C**–**S2** Connection State | Results, with **C**–**S1** in Yellow and **C**–**S2** in Blue |
| --- | --- | --- | --- | --- |
| | Parameter | Value | | --- | --- | | **Time-to-break C-S1 connection** | `0` | | **Time-to-make C-S1 connection** | `0` | | **Time-to-break C-S2 connection** | `0` | | **Time-to-make C-S2 connection** | `0` | | De-energized | 1 | 0 |  |
| Energized | 0 | 1 |
| | Parameter | Value | | --- | --- | | **Time-to-break C-S1 connection** | > `0` | | **Time-to-make C-S1 connection** | `0` | | **Time-to-break C-S2 connection** | `0` | | **Time-to-make C-S2 connection** | `0` | | De-energized | 1 | 0 |  |
| Energized | 1, 0 | 1 |
| | Parameter | Value | | --- | --- | | **Time-to-break C-S1 connection** | `0` | | **Time-to-make C-S1 connection** | > `0` | | **Time-to-break C-S2 connection** | `0` | | **Time-to-make C-S2 connection** | `0` | | De-nergized | 0, 1 | 0 |  |
| Energized | 0 | 1 |
| | Parameter | Value | | --- | --- | | **Time-to-break C-S1 connection** | `0` | | **Time-to-make C-S1 connection** | `0` | | **Time-to-break C-S2 connection** | > `0` | | **Time-to-make C-S2 connection** | `0` | | De-nergized | 1 | 1, 0 |  |
| Energized | 0 | 1 |
| | Parameter | Value | | --- | --- | | **Time-to-break C-S1 connection** | `0` | | **Time-to-make C-S1 connection** | `0` | | **Time-to-break C-S2 connection** | `0` | | **Time-to-make C-S2 connection** | > `0` | | De-nergized | 1 | 0 |  |
| Energized | 0 | 0, 1 |

### Faults

To model a fault in the SPDT Relay block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

You can add a switch fault or an open-circuit fault to the winding. If you add a
switch fault, you can set the **Switch fault** parameter to:

- `C-S1 stuck closed`
- `C-S2 stuck closed`
- `C open circuit (no path to S1 or S2)`
- `Degraded contact resistance`

You can specify how and when faults occur by using the **Trigger
type** parameter.

For more information about adding faults to blocks and
specifying fault triggers, see Introduction to Simscape Faults.

****C**–**S1** Stuck
Closed Fault**

The **C**–**S1** stuck closed
fault occurs if the common contact, **C**, becomes
mechanically, electrically, or chemically stuck to the normally closed contact,
**S1**. Causes of this type of fault include:

- Contact welding, possibly due to an inrush current or breaking
  current that exceeds the rating or load short circuit.
- Mechanical damage.
- Insulation deterioration.
- Inductive voltage.

The table shows the faulted state for a
**C**–**S1** stuck
closed fault.

| Connection | State |
| --- | --- |
| **C**–**S1** | 1 |
| **C**–**S2** | 0 |

A **C**–**S1** stuck closed
behavioral fault can occur only if the load current exceeds the current
threshold for a period of time that exceeds the behavioral trigger time
threshold. That is, the behavioral fault can occur only if:

iload>ith,

and

ti>i\_th>tth\_b,

where:

- *iload* is the load
  current.
- *ith* is the value of the
  **Maximum permissible load current**
  parameter.
- *ti>i\_th* is the time that
  the current threshold is exceeded.
- *tth\_b* is the value of
  the **Time to fail when exceeding current**
  parameter.

When a fault occurs, if
**C**–**S1** is:

- Closed —
  **C**–**S1**
  remains closed for the rest of the simulation.
- Open —
  **C**–**S1**
  the fault does not take effect unless the relay becomes de-energized
  and the
  **C**–**S1**
  connection closes. Once closed, the
  **C**–**S1**
  connection remains closed for the rest of the simulation.

****C**–**S2** Stuck Closed
Fault**

The **C**–**S2** stuck closed
fault occurs if the common contact, **C**, becomes
mechanically, electrically, or chemically stuck to the normally closed contact,
**S2**. Causes of this type of fault include:

- Contact welding, possibly due to an inrush current or breaking
  current that exceeds the rating or load short circuit.
- Mechanical damage.
- Insulation deterioration.

The table shows the faulted state for a
**C**–**S2** stuck
closed fault.

| Connection | State |
| --- | --- |
| **C**–**S1** | 0 |
| **C**–**S2** | 1 |

A **C**–**S2** stuck closed
behavioral fault can occur only if the load current exceeds the current
threshold for a period of time that exceeds the behavioral trigger time
threshold. That is, the behavioral fault can occur only if:

iload>ith,

and

ti>i\_th>tth\_b,

where:

- *iload* is the load
  current.
- *ith* is the specified
  value for the **Maximum permissible load current**
  parameter.
- *ti>i\_th* is the time that
  the current threshold is exceeded.
- *tth\_b* is the specified
  value for the **Time to fail when exceeding
  current** parameter.

When a fault occurs, if
**C**–**S2** is:

- Closed —
  **C**–**S2**
  remains closed for the rest of the simulation.
- Open — The
  **C**–**S2**
  the fault does not take effect unless the relay becomes energized
  and the
  **C**–**S2**
  connection closes. Once closed, the
  **C**–**S2**
  connection remains closed for the rest of the simulation.

****C** Open Circuit (No Path to **S1** or
**S2**) Fault**

The **C** open circuit (no path to **S1** or
**S2**) fault occurs if the common contact,
**C**, becomes mechanically stuck in an open position. This
type of fault can happen if:

- There is contact damage or deterioration.
- The switch connector becomes mechanically stuck in the middle of
  the relay.

The table shows the faulted state for a **C** open
circuit (no path to **S1** or
**S2**) fault.

| Connection | State |
| --- | --- |
| **C**–**S1** | 0 |
| **C**–**S2** | 0 |

A **C** open circuit behavioral fault can occur only if the load current
exceeds the current threshold for a period of time that exceeds the behavioral
trigger time threshold. That is, the behavioral fault can occur only if:

iload>ith,

and

ti>i\_th>tth\_b,

where:

- *iload* is the load
  current.
- *ith* is the value of the
  **Maximum permissible load current**
  parameter.
- *ti>i\_th* is the period of
  time during which the current threshold is exceeded.
- *tth\_b* is the value of
  the **Time to fail when exceeding current**
  parameter.

When the temporal fault threshold is exceeded, if:

- The relay is in the open-circuit state, that is, one connection
  has been broken, and the other connection has not yet been made, the
  relay remains open for the rest of the simulation.
- Either the
  **C**–**S1**
  or
  **C**–**S2**
  connection is closed, the fault does not take effect unless the
  relay is energized or de-energized and the closed connection is
  broken. If the connection is broken, the relay becomes an
  open-circuit, and remains open for the rest of the
  simulation.

When the behavioral fault thresholds are exceeded, if:

- The relay is in the open-circuit state, that is, one connection
  has been broken, and the other connection has not yet been made, the
  relay remains open for the rest of the simulation.
- Either the
  **C**–**S1**
  or
  **C**–**S2**
  connection is closed, the relay state immediately becomes an open
  circuit and remains an open circuit for the rest of the
  simulation.

**Degraded Contact Resistance Fault**

Causes of the degraded contact resistance fault include:

- Overuse-induced overload conditions. High inrush currents and
  voltages can cause overload conditions, as can excessive switching
  of the relay. Overload conditions ultimately trigger electrical
  arching, which generates heat that degrades the contact
  material.
- Chemical contamination that interferes with the operation of the
  relay contacts. Contaminants, which can include oxidation films or
  foreign particles, tend to produce high or unstable contact
  resistance readings.
- End of relay life.

The table shows the faulted state for a degraded contact resistance
fault.

| Connection | State |
| --- | --- |
| **C**–**S1** | 0 or 1. The contact resistance is degraded. |
| **C**–**S2** | 0 or 1. The contact resistance is degraded. |

When a temporal fault occurs, the degraded contact resistances of **S1**
and **S2** are:

rcontact\_s1(t)=rcontact\_fault\_s1−(rcontact\_fault\_s1−rcontact)sech(t−tth\_tτ),

rcontact\_s2(t)=rcontact\_fault\_s2−(rcontact\_fault\_s2−rcontact)sech(t−tth\_tτ),

where:

- *rcontact\_fault\_s1* is the
  final value of the faulted **S1** contact
  resistance.
- *rcontact\_fault\_s2* is the
  final value of the faulted **S2** contact
  resistance.
- *rcontact* is the
  unfaulted **S1** and
  **S2** contact resistance.

A degraded contact resistance behavioral fault can occur only if the load current exceeds
the current threshold for a period of time that exceeds the behavioral trigger
time threshold. That is, the behavioral fault can occur only if:

iS1−C>ith,

and

ti1>i\_th>tth\_b,

where:

- *iload* is the load
  current.
- *ith* is the value of the
  **Maximum permissible load current**
  parameter.
- *ti1>i\_th* is the period
  of time during which the current threshold for the connection
  **C-S1** is exceeded.
- *tth\_b* is the value of
  the **Time to fail when exceeding current**
  parameter.

For a behavior-triggered fault, if iS1−C>ith continuously over the time interval
*tth\_b*,

rcontact\_s1(t)=rcontact\_fault\_s1−(rcontact\_fault\_s1−rcontact)sech(ti1>i\_th−tth\_bτ),

where:

- *iS1-C* is the common
  contact to normally closed contact,
  **C**–**S1**,
  current.
- *ith* is the specified
  value for the **Maximum permissible load current**
  parameter.
- *tth\_b* is the specified
  value for the **Time to fail when exceeding
  current** parameter.
- *rcontact\_fault\_s1* is the
  final value of the faulted **S1** contact
  resistance.
- *rcontact* is the
  unfaulted **S1** contact resistance.
- *τ* is specified value for the **Time
  constant for degraded contact resistance**
  parameter.

Likewise, for a
**C**–**S2**
connection, if

iS2−C>ith

and

ti2>i\_th>tth\_b,

then the degraded contact resistance is:

rcontact\_s2(t)=rcontact\_fault\_s2−(rcontact\_fault\_s2−rcontact)sech(ti2>i\_th−tth\_bτ),

where:

- *iS2-C* is the common
  contact to normally closed contact,
  **C**–**S2**,
  current.
- *rcontact\_fault\_s2* is the
  final value of the faulted **S2** contact
  resistance

When the temporal fault threshold is exceeded, for both the
**C**–**S1**
and the **C**–**S2**
connections, the contact resistance is immediately degraded and remains degraded
for the rest of the simulation.

When the behavioral fault thresholds are exceeded for
**C**–**S1**,
in terms of *iS1-C*, the resistance for
the **C**–**S1**
connection is degraded after the specified value for the **Time to fail
when exceeding current** parameter and remains degraded for the
rest of the simulation.

When the behavioral fault thresholds are exceeded for
**C**–**S2**,
in terms of *iS2-C*, the resistance for
the **C**–**S2**
connection is degraded after the specified value for the **Time to fail
when exceeding current** parameter and remains degraded for the
rest of the simulation.

**Winding failed open circuit**

The open-circuit winding fault is available only for the electrical control
variant. An open circuit in the winding coil can cause this type of
fault.

The table shows the faulted state for a winding failed open circuit
fault.

| Connection | State |
| --- | --- |
| **C**–**S1** | 1 |
| **C**–**S2** | 0 |

For timed faults, the block approximates the winding current as:

Ldidt+Ri=vwinding\*sech(t−tth\_tτ),

where :

- *L* is the winding inductance.
- *R* is the winding resistance.
- *i* is the winding current.
- *vwinding* is the voltage
  across the winding.
- *tth\_t* is the value of
  the **Trigger fault at time** parameter.
- *τ* is the value of the **Time constant
  for winding open circuit transition** parameter.

A winding failed open circuit behavioral fault can occur only if one of these conditions
is met:

- The winding current exceeds the current threshold for a period of
  time that exceeds the behavioral trigger time threshold.
- The winding voltage exceeds the voltage threshold for a number of
  times that exceeds the threshold for the number of voltage
  overloads.

That is, the behavioral fault can occur only if:

iwinding>ith

and then

ti>i\_th>tth\_b,

where:

- *iwinding* is the winding
  current.
- *ith* is the specified
  value for the **Maximum permissible winding
  current** parameter.
- *ti>i\_th* is the time that
  the current threshold is exceeded.
- *tth\_b* is the specified
  value for the **Time to fail when exceeding
  current** parameter.

or if:

vwinding>vth,

and then

Nv>v\_th>Nth,

where:

- *vwinding* is the winding
  voltage.
- *vth* is the specified
  value for the **Maximum permissible winding
  voltage** parameter.
- *Nv>v\_th* is the number of
  times that the voltage threshold is exceeded.
- *Nth* is the specified
  value for the **Number of events to fail when exceeding
  voltage** parameter.

Once a fault triggers, the
**C**–**S1**
remains closed for the rest of the simulation.
