---
type: simulink-block
title: 'Winding'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'winding'
documentation_source_path: 'ref/winding.html'
language: en
---

# Winding

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal of
the block.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal of
the block.

### **N** — North terminal magnetic

Magnetic conserving port associated with the north terminal of the
block.

### **S** — South terminal magnetic

Magnetic conserving port associated with the south terminal of the
block.

## Parameters

### Main

### **Number of winding turns** — Winding turn count `10` (default) | positive number

Number of wire turns on the transformer winding.

### **Winding resistance** — Series resistance `1e-3` `Ohm` (default) | positive number

Power loss in the winding.

### **Leakage reluctance** — Parallel reluctance `1e5` `1/H` (default) | positive number

Magnetic flux loss in the winding. If you do not want to model the
leakage internally to the Winding block, set this parameter to
`inf`.

### **Parallel conductance** — Parallel conductance `0` `1/Ohm` (default) | positive number

Parallel leakage path, Simulation of some circuits may require the
presence of a small parallel conductance.

### Thermal Port

### **Thermal port** — Whether to model thermal port `Omit` (default) | `Model`

Whether to model the thermal port of the winding. The thermal port
reports the winding resistance losses.

### **Measurement temperature** — Measurement temperature `25` `K` (default)

The temperature for which the winding parameters are quoted.

#### Dependencies

To enable this parameter, set **Thermal port** to
`Model`.

### **Resistance temperature coefficient** — Resistance temperature coefficient `3.93e-3` `1/K` (default)

Coefficient α in the equation relating resistance to temperature, as
described in Thermal Model for Actuator Blocks. The default value is for
copper.

#### Dependencies

To enable this parameter, set **Thermal port** to
`Model`.

### **Winding Thermal mass** — Thermal mass for winding `100` `J/K` (default)

The thermal mass value for the winding. The thermal mass is the energy
required to raise the temperature by one degree.

#### Dependencies

To enable this parameter, set **Thermal port** to
`Model`.

### Faults

### **Winding fault** — Option to model fault in winding `Add fault` (default)

Option to model a fault in the Winding block.

To add a fault, click the **Add fault**
hyperlink.

### **Location of fault node (% of total turns from - terminal)** — Percentage of turns in the subinductor that is in contact with the – port of the faulted winding `50` (default) | scalar in the range (0,100)

Faults are enabled by segmenting the faulted winding into two coupled
subinductors, connected in a series. The inductance is proportional to
the square of the number of turns in the respective segment, and the
series resistance of each subinductor is proportional to the number of
turns in each segment. The parallel conductance spans both segments.

This parameter indicates the percentage of turns that are assigned to
the subinductor that is in contact with the **–** port
of the faulted winding. The remaining turns are assigned to the other
subinductor. The default value is `50`, which means
that the overall inductance of the faulted winding is divided into two
equal, coupled subinductors.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Winding fault** parameter.

### **Short-circuit turns** — Select whether fault results in one of the segments being short-circuited `No` (default) | `To negative terminal` | `To positive terminal`

Select whether the fault results in one of the subinductor segments
being short-circuited:

- `No` — The fault does not
  produce a short circuit.
- `To negative terminal` — The
  fault short-circuits the subinductor that is in contact with the
  **–** port of the block.
- `To positive terminal` — The
  fault short-circuits the subinductor that is in contact with the
  **+** port of the block.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink in the
**Winding fault** parameter.

### **Open-circuit at fault node** — Select whether to apply an open-circuit fault between the segments `No` (default) | `Yes`

Select whether to apply an open-circuit fault between the two
subinductor segments. Even with an open-circuit fault, the
characteristics of the subinductors are still related because they are
magnetically coupled even in the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink in the **Winding fault**
parameter.

### **Ground fault** — Select whether fault results in one of the segments being short-circuited `No` (default) | `Negative terminal side of fault node` | `Positive terminal side of fault node`

Select whether, in case of fault, there is a path for current to flow
towards the ground node:

- `No` — The fault does not
  result in a connection to ground.
- `Negative terminal side of fault
  node` — The side that is in contact with
  the **–** port of the block is connected to
  ground.
- `Positive terminal side of fault
  node` — The side that is in contact with
  the **+** port of the block is connected to
  ground.

If the **Open-circuit at fault node** parameter is
set to `Yes`, you must specify which side
(negative or positive) is connected to ground. If there is no open
circuit, the two options behave similarly. Physically, this corresponds
to a breakdown in the insulation between the windings and the grounded
core or chassis.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink in the **Winding fault**
parameter.

### **Conductance of faulted ground path** — Mutual coupling between the two subinductors `0` `1/Ohm` (default) | nonnegative scalar

Conductance of the current path to ground. For example, if the path to
ground is through the core material, then specify a small conductance
value depending on the core material being used. For highly conductive
core material or for chassis-shorts, specify a higher conductance value.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink in the
**Winding fault** parameter and set
**Ground fault** to `Negative
terminal side of fault node` or
`Positive terminal side of fault
node`.

### **Fault transition time constant** — Time constant for the transition to faulted state `1e-3` `s` (default) | positive scalar

Time constant associated with the transition to the faulted state, as
described in Faults.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink in the **Winding fault**
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
    **Condition** parameter at each time step. To model
    irreversible faults, select the **Trigger stays on once
    activated** parameter in the Property Inspector. The block
    enters the faulted state when the trigger condition becomes true for the
    first time and remains in the faulted state for the rest of the
    simulation. To model reversible faults, clear the **Trigger
    stays on once activated** parameter. The block enters the
    faulted state when the trigger condition is true and enters the
    unfaulted state when the trigger condition is false. To learn more, see
    Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink in the **Winding fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink in the
**Winding fault** parameter and set **Trigger type** to
`Timed`.

### **Maximum permissible voltage** — Voltage threshold to fault transition `100` `V` (default) | positive scalar

Voltage threshold to a fault transition. If the voltage value exceeds
this threshold a certain number of times, specified by the
**Number of events to fail when exceeding voltage**
parameter value, then the block enters the fault state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink in the
**Winding fault** parameter and set **Trigger type** to
`Behavioral`.

### **Number of events to fail when exceeding voltage** — Maximum number of times the voltage can exceed the threshold `1` (default) | positive scalar

Number of voltage overshoots that the inductor can withstand before
the fault transition begins. This block does not check the time spent in
the overvoltage condition, only the number of transitions.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink in the
**Winding fault** parameter and set **Trigger type** to
`Behavioral`.

### **Maximum permissible current** — Current threshold for fault transition `1` `A` (default) | positive scalar

Current threshold for a fault transition. The block enters the faulted state if the current
continuously exceeds this value for a period longer than the value of the **Time to
fail when exceeding current** parameter.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink in the
**Winding fault** parameter and set **Trigger type** to
`Behavioral`.

### **Time to fail when exceeding current** — Maximum length of time the current exceeds the threshold `1` `s` (default) | nonnegative scalar

Amount of time that the current must continuously exceed the maximum permissible current
before a fault triggers.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink in the
**Winding fault** parameter and set **Trigger type** to
`Behavioral`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink in the
**Winding fault** parameter and set **Trigger type** to `Additional
triggers`.

## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2025a: Model Reversible Conditional Faults

You can now model reversible conditional faults in the Winding block by clearing the
**Trigger stays on once activated** parameter. The block enters the
faulted state when the trigger condition is true and enters the unfaulted state when the
trigger condition is false.

Before R2025a, the block enters the faulted state when the trigger condition becomes true
for the first time and remains in the faulted state for the rest of the simulation.

If you create a model before R2025a and enable a conditional fault in the Winding
block, the block now selects the **Trigger stays on once activated**
parameter by default for backward compatibility.

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

Electromagnetic converter with ohmic and magnetic flux losses

The Winding block represents an electromagnetic converter
with winding resistance and leakage reluctance. You can use this block as a base
component for building custom transformers. For an ideal electromagnetic converter, see
the Electromagnetic Converter.

When you apply a positive current across the electrical ports of the block, a positive
magnetomotive force (MMF) is induced across the magnetic terminals.

F=Ni

Where:

- *ℱ* is the MMF across the magnetic terminals of the
  block
- *N* is the number of winding turns
- *i* is the current through the winding

When you apply a positive time-varying flux across the magnetic terminals
of the block, a negative voltage is induced across the electrical terminals of the block.

v=−Ndϕdt+N2Rldidt+Rwi

Where:

- *φ* is the flux through the magnetic terminals of the
  block
- *i* is the current through the electrical terminals of
  the block
- *ℛl* is the leakage
  reluctance
- *Rw* is the winding
  resistance
- *ℱ* is the magnetomotive force across the magnetic
  terminals of the block
- *v* is the voltage drop across the electrical terminals
  of the block

This figure shows the equivalent circuit for the block.

In the diagram, *φ*mp corresponds to the main-path
flux and *φ* to the total flux. You can set the initial condition for
the total flux in the block's **Variables** tab.

### Faults

To model a fault in the Winding block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

Instantaneous changes in the winding parameters are unphysical. Therefore, when
the Winding block enters the faulted state,
short-circuit and open-circuit voltages transition to their faulted values over a
period of time based on this formula:

*`CurrentValue`* =
*`FaultedValue`* –
(*`FaultedValue`* –
*`UnfaultedValue`*) · `sech`(∆t
/ τ)

where:

- ∆t is time since the onset of the fault condition.
- τ is user-defined time constant associated with the fault
  transition.

For short-circuit faults, the conductance of the short-circuit path also changes
according to the `sech`(∆t / τ) function from a small value
(representing an open-circuit path) to a large value.

Faultable windings often require that you use the fixed-step local solver,
especially if your model transitions to a faulted state that includes short
circuits. For more information, see Making Optimal Solver Choices for Physical Simulation.

**Fault Triggers**

You specify how and when faults occur by using the **Trigger type**
parameter.

If you set the **Trigger type** to `Behavioral`,
the Winding block triggers fault events when:

- The current continuously exceeds the value of the
  **Maximum permissible current** parameter for a
  duration longer than the value of the **Time to fail when
  exceeding current** parameter.
- The voltage exceeds the **Maximum permissible
  voltage** a certain number of times, specified by the
  **Number of events to fail when exceeding
  voltage** parameter value.

If you set the **Trigger
type** to `Conditional`, you can choose whether faults
in the Winding block are reversible *(since R2025a)*. To model irreversible faults, click
**Open fault properties** to open the Property Inspector and select the
**Trigger stays on once activated** parameter. The block enters the faulted
state when the trigger condition becomes true for the first time and remains in the faulted
state for the rest of the simulation. To model reversible faults, clear the **Trigger
stays on once activated** parameter. The block enters the faulted state when the
trigger condition is true and enters the unfaulted state when the trigger condition is
false.

For more information about adding faults to blocks and
specifying fault triggers, see Introduction to Simscape Faults.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
