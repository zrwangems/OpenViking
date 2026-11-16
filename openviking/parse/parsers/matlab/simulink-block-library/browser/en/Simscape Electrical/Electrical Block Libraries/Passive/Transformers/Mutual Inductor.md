---
type: simulink-block
title: 'Mutual Inductor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Transformers'
documentation_page: 'mutualinductor'
documentation_source_path: 'ref/mutualinductor.html'
language: en
---

# Mutual Inductor

## Ports

### Conserving

### **1+** — Positive terminal of the primary winding electrical

Electrical conserving port associated with the primary winding
positive terminal.

### **1-** — Negative terminal of the primary winding electrical

Electrical conserving port associated with the primary winding
negative terminal.

### **2+** — Positive terminal of the secondary winding electrical

Electrical conserving port associated with the secondary winding
positive terminal.

### **2-** — Negative terminal of the secondary winding electrical

Electrical conserving port associated with the secondary winding
negative terminal.

## Parameters

### Main

### **Inductance L1** — Nominal inductance value in the primary winding `10` `H` (default) | positive scalar

The nominal inductance value in the primary winding.

### **Inductance L2** — Nominal inductance value in the secondary winding `0.1` `H` (default) | positive scalar

The nominal inductance value in the secondary winding.

### **Coefficient of coupling** — Mutual inductance coupling between windings 0.9 (default) | scalar in the range [-1,1]

Coefficient of coupling that defines the mutual inductance between the
primary and secondary windings. To reverse one of the winding
directions, use a negative value.

Do not use magnitudes very close to 1, such as 0.999, because these
values introduce fast simulation dynamics. To set the coefficients of
coupling to 1 while also retaining the correct low-frequency behavior,
blocking DC, use the Mutual Inductor
block in the Simscape Foundation library and select the
**Perfect coupling – no leakage** parameter.

### **Tolerance (%)** — Inductor tolerance, in percent 20 (default)

The inductor tolerance as defined on the manufacturer datasheet.
Datasheets typically provide a tolerance percentage for a given inductor
type. Therefore, this value is the same for both windings.

### **L1 tolerance application** — Select how to apply tolerance to primary winding `None — use nominal value` (default) | `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

Select how to apply tolerance during simulation to the primary
winding:

- `None — use nominal value`
  — The block does not apply tolerance, it uses the nominal
  inductance value.
- `Random tolerance` — The block
  applies random offset to the inductance value, within the
  tolerance value limit. You can choose Uniform or Gaussian
  distribution for calculating the random number by using the
  **Tolerance distribution**
  parameter.
- `Apply maximum tolerance value`
  — The inductance is increased by the specified tolerance
  percent value.
- `Apply minimum tolerance value`
  — The inductance is decreased by the specified tolerance
  percent value.

### **L1 tolerance distribution** — Select the distribution type for primary winding `Uniform` (default) | `Gaussian`

Select the distribution type for random tolerance:

- `Uniform` — Uniform
  distribution
- `Gaussian` — Gaussian
  distribution

#### Dependencies

Enabled when the **L1 tolerance application**
parameter is set to `Random
tolerance`.

### **L1 number of standard deviations for quoted tolerance** — Used for calculating the Gaussian random number for primary winding 4 (default)

Number of standard deviations for calculating the Gaussian random
number.

#### Dependencies

Enabled when the **L1 tolerance distribution**
parameter is set to `Gaussian`.

### **L2 tolerance application** — Select how to apply tolerance to secondary winding `None — use nominal value` (default) | `Random tolerance` | `Apply maximum tolerance value` | `Apply minimum tolerance value`

Select how to apply tolerance during simulation to the secondary
winding:

- `None — use nominal value`
  — The block does not apply tolerance, it uses the nominal
  inductance value.
- `Random tolerance` — The block
  applies random offset to the inductance value, within the
  tolerance value limit. You can choose Uniform or Gaussian
  distribution for calculating the random number by using the
  **Tolerance distribution**
  parameter.
- `Apply maximum tolerance value`
  — The inductance is increased by the specified tolerance
  percent value.
- `Apply minimum tolerance value`
  — The inductance is decreased by the specified tolerance
  percent value.

### **L2 tolerance distribution** — Select the distribution type for secondary winding `Uniform` (default) | `Gaussian`

Select the distribution type for random tolerance:

- `Uniform` — Uniform
  distribution
- `Gaussian` — Gaussian
  distribution

#### Dependencies

Enabled when the **L2 tolerance application**
parameter is set to `Random
tolerance`.

### **L2 number of standard deviations for quoted tolerance** — Used for calculating the Gaussian random number for secondary winding `4` (default)

Number of standard deviations for calculating the Gaussian random
number.

#### Dependencies

Enabled when the **L2 tolerance distribution**
parameter is set to `Gaussian`.

### Resistance

### **Series resistance, [R\_primary R\_secondary]** — Equivalent series resistance of the primary and secondary winding `[0.001, 0.001]` `Ohm` (default)

Equivalent series resistance of the primary and secondary winding,
specified as a two-element vector. The first number corresponds to the
primary winding, the second number to the secondary winding. For a
faulted winding, the block allocates the resistance to each segment in
proportion to the number of turns in that segment.

### **Parallel conductance, [G\_primary G\_secondary]** — Parallel leakage path associated with the primary and secondary winding `[1e-9,1e-9]` `1/Ohm` (default)

Parallel leakage path associated with the primary and secondary
winding, specified as a two-element vector. The first number corresponds
to the primary winding, the second number to the secondary winding. The
parallel conductances are placed directly across the + and – terminals
of the primary and secondary winding, respectively.

### Operating Limits

### **Enable operating limits** — Select `Yes` to enable reporting when the operational limits are exceeded `No` (default) | `Yes`

Select `Yes` to enable reporting when the operational
limits are exceeded. The associated parameters in the
**Operating Limits** section become visible to let
you select the reporting method and specify the operating limits in
terms of power and current.

### **Reporting when operating limits exceeded** — Select the reporting method `Warn` (default) | `Error`

Select what happens when an operating limit is exceeded:

- `Warn` — The block issues a
  warning.
- `Error` — Simulation stops
  with an error.

#### Dependencies

Enabled when the **Enable operating limits**
parameter is set to `Yes`.

### **Saturation current** — Inductor saturation current `1` `A` (default)

Inductor saturation current, as defined in the manufacturer
datasheets. If the net current into the primary and secondary windings
exceeds this value, the core material enters saturation, and the block
reports an operating limits violation. That is, the block compares the
limit against |*i*1 +
*i*2|, where currents are defined as being positive when
they are into the + nodes.

#### Dependencies

Enabled when the **Enable operating limits**
parameter is set to `Yes`.

### **Power rating** — Maximum power dissipation in the inductor `1` `A` (default)

Maximum instantaneous (total) power dissipation in the resistance and
conductance elements associated with the mutual inductor. If the total
power (including both primary and secondary winding) exceeds this
number, the block reports an operating limits violation.

#### Dependencies

Enabled when the **Enable operating limits**
parameter is set to `Yes`.

### Faults

### **Mutual inductor fault** — Option to model fault in mutual inductor `Add fault` (default)

Option to model a fault in the Mutual Inductor block.

To add a fault, click the **Add fault**
hyperlink.

### **Faulted winding** — Select winding to use for fault modeling `Primary` (default) | `Secondary`

Select whether the faults occur in the primary or secondary
winding.

#### Dependencies

To enable this parameter, add a fault to the Mutual Inductor block by
clicking the **Add fault** hyperlink in the
**Mutual inductor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Location of fault node (% of total turns from - terminal)** — Percentage of turns in the subinductor that is in contact with the – port of the faulted winding `50` (default) | scalar in the range (0,100)

In practice, faults are enabled by segmenting the faulted winding into
two coupled subinductors, connected in a series. The inductance is
proportional to the square of the number of turns in the respective
segment, and the series resistance of each subinductor is proportional
to the number of turns in each segment. The parallel conductance spans
both segments.

This parameter indicates the percentage of turns that are assigned to
the subinductor that is in contact with the – port of the faulted
winding. The remaining turns are assigned to the other subinductor. The
default value is `50`, which means that the overall
inductance of the faulted winding is divided into two equal, coupled
subinductors.

#### Dependencies

To enable this parameter, add a fault to the Mutual Inductor block by
clicking the **Add fault** hyperlink in the
**Mutual inductor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Short-circuit turns** — Select whether fault results in one of the segments being short-circuited `No` (default) | `To negative terminal` | `To positive terminal`

Select whether the fault results in one of the subinductor segments
being short-circuited:

- `No` — The fault does not
  produce a short circuit.
- `To negative terminal` — The
  fault short-circuits the subinductor that is in contact with the
  – port of the block.
- `To positive terminal` — The
  fault short-circuits the subinductor that is in contact with the
  + port of the block.

#### Dependencies

To enable this parameter, add a fault to the Mutual Inductor block by
clicking the **Add fault** hyperlink in the
**Mutual inductor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Open-circuit at fault node** — Select whether to apply an open-circuit fault between the segments `No` (default) | `Yes`

Select whether to apply an open-circuit fault between the two
subinductor segments. The default is `No`. Even
with an open-circuit fault, the characteristics of the subinductors are
still related because they are magnetically coupled even in the faulted
state.

#### Dependencies

To enable this parameter, add a fault to the Mutual Inductor block by
clicking the **Add fault** hyperlink in the
**Mutual inductor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Ground fault** — Select whether fault results in one of the segments being short-circuited `No` (default) | `Negative terminal side of fault node` | `Positive terminal side of fault node`

Select whether, in case of fault, there is a path for current to flow
towards the ground node:

- `No` — The fault does not
  result in a connection to ground.
- `Negative terminal side of fault
  node` — The side that is in contact with
  the – port of the block is connected to ground.
- `Positive terminal side of fault
  node` — The side that is in contact with
  the + port of the block is connected to ground.

If the **Open-circuit at fault node** parameter is
set to `Yes`, you need to specify which side
(negative or positive) is connected to ground. If there is no open
circuit, the two options behave similarly. Physically, this corresponds
to a breakdown in the insulation between the windings and the grounded
core or chassis.

#### Dependencies

To enable this parameter, add a fault to the Mutual Inductor block by
clicking the **Add fault** hyperlink in the
**Mutual inductor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Conductance of faulted ground path** — Mutual coupling between the two subinductors `0` `1/Ohm` (default) | nonnegative scalar

If there is a ground fault, this parameter represents conductance of
the current path to ground. For example, if the path to ground is
through the core material, then specify a small conductance value
depending on the core material being used. For highly conductive core
material or for chassis-shorts, specify a higher conductance value.

#### Dependencies

To enable this parameter, add a fault to the Mutual Inductor block by
clicking the **Add fault** hyperlink in the
**Mutual inductor fault** parameter and set
**Ground fault** to `Negative
terminal side of fault node` or
`Positive terminal side of fault
node`..

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Fault transition time constant** — Time constant for the transition to faulted state `1e-3` `s` (default) | positive scalar

Time constant associated with the transition to the faulted state, as
described in Faults.

#### Dependencies

To enable this parameter, add a fault to the Mutual Inductor block by
clicking the **Add fault** hyperlink in the
**Mutual inductor fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.

### **Maximum permissible voltage** — Voltage threshold to fault transition `100` `V` (default) | positive scalar

Define the voltage threshold to a fault transition. If the voltage
value exceeds this threshold a certain number of times, specified by the
**Number of events to fail when exceeding voltage**
parameter value, then the block starts entering the fault state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Number of events to fail when exceeding voltage** — Maximum number of times the voltage can exceed the threshold `1` (default) | positive scalar

Because the physical mechanism underlying voltage-based failures
depends on one or more partial discharge events occurring, this
parameter allows you to set the number of voltage overshoots that the
inductor can withstand before the fault transition begins. Note that the
block does not check the time spent in the overvoltage condition, only
the number of transitions.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Maximum permissible current** — Current threshold to fault transition `1` `A` (default) | positive scalar

Current threshold to a fault transition. If the current exceeds this
value for longer than the **Time to fail when exceeding
current** parameter value, then the block enters the
faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding current** — Maximum length of time the current exceeds the threshold `1` `s` (default) | nonnegative scalar

Maximum length of time that the current can exceed the maximum
permissible value without triggering the fault.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

## Libraries

Simscape / Electrical / Passive / Transformers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

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

Mutual inductor model with nominal inductance optional tolerances for each winding, operating limits and faults

The Mutual Inductor block lets you model a mutual
inductor (two-winding transformer) with nominal inductance tolerances for each winding.
The model includes the following effects:

- Tolerances
- Operating Limits
- Faults

You can turn these modeling options on and off independently of each other.

In the unfaulted state, the following equations describe the Mutual
Inductor block behavior:

v1=L1diL1dt+​MdiL2dt+iL1R1

v2=L2diL2dt+​MdiL1dt+iL2R2

M=kL1L2

where:

- *v1* and
  *v2* are voltages across the
  primary and secondary winding, respectively.
- *L1* and
  *L2* are inductances of the
  primary and secondary winding.
- *R1* and
  *R2* are series resistances of
  the primary and secondary winding.
- *M* is mutual inductance.
- *k* is coefficient of coupling. To reverse one of the winding
  directions, use a negative value.
- *t* is time.

A parallel conductance is placed across the + and – terminals of the primary and
secondary windings, so that *iL1* =
*i1* –
*G1**v1*, where *G1* is the parallel
conductance of the primary winding, and *i1* is
the terminal current into the primary. Similar definitions and equation apply to
*iL2*.

Do not set the magnitude of the coupling coefficient to values close to 1, such as
0.999, because these values introduce fast simulation dynamics. To set the coefficients
of coupling to 1 while also retaining the correct low-frequency behavior, blocking DC,
use the Mutual Inductor block in the
Simscape Foundation library and select the **Perfect coupling – no
leakage** parameter.

Simscape™ and Simscape
Electrical™ libraries include several blocks than can model the same type of transformer device. However, these blocks make different modeling assumptions. To choose the right block for your application, you must understand how these assumptions impact the block behavior as a function of frequency. For more information, see Choose Blocks to Model Transformers.

### Tolerances

You can apply tolerances separately for each winding. Datasheets typically provide
a tolerance percentage for a given inductor type. Therefore, this value is the same
for both windings. The table shows how the block applies tolerances to the nominal
inductance value and calculates inductance based on the selected tolerance
application option for the winding, **L1 tolerance application** or
**L2 tolerance application**.

| Option | Inductance Value |
| --- | --- |
| `None — use nominal value` | *L* |
| `Random tolerance` | Uniform distribution: *L* · (1 – *tol* + 2· *tol*· `rand`)  Gaussian distribution: *L* · (1 + *tol* · `randn` / *nSigma*) |
| `Apply maximum tolerance value` | *L* · (1 + *tol* ) |
| `Apply minimum tolerance value` | *L* · (1 – *tol* ) |

In the table:

- *L* is nominal inductance for the primary or secondary
  winding, **Inductance L1** or **Inductance
  L2** parameter value.
- *tol* is fractional tolerance, **Tolerance
  (%)** /100.
- *nSigma* is the value you provide for the
  **Number of standard deviations for quoted tolerance**
  parameter.
- `rand` and `randn` are standard
  MATLAB® functions for generating uniform and normal distribution
  random numbers.

**Note**

If you choose the `Random tolerance` option and you
are in "Fast Restart" mode, the random tolerance value is updated on every
simulation if at least one between the fractional tolerance,
*tol*, or the **Number of standard deviations for
quoted tolerance**, *nSigma*, is set to Run-time
and is defined with a variable (even if you do not modify that variable).

### Operating Limits

Inductors are typically rated with a particular saturation current, and possibly
with a maximum allowable power dissipation. You can specify operating limits in
terms of these values, to generate warnings or errors if the inductor is driven
outside its specification.

When an operating limit is exceeded, the block can either generate a warning or
stop the simulation with an error. For more information, see the Operating Limits parameters section.

### Faults

To model a fault in the Mutual Inductor block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

Instantaneous changes in inductor parameters are unphysical. Therefore, when the
Mutual Inductor block enters the faulted state,
short-circuit and open-circuit voltages transition to their faulted values over a
period of time based on this formula:

*`CurrentValue`* =
*`FaultedValue`* –
(*`FaultedValue`* –
*`UnfaultedValue`*) · `sech`(∆t
/ τ)

where:

- ∆t is time since the onset of the fault condition.
- τ is the value of the **Fault transition time constant**
  parameter.

For short-circuit faults, the conductance of the short-circuit path also changes
according to the `sech`(∆t / τ) function from a small value
(representing an open-circuit path) to a large value.

The Mutual Inductor block lets you select whether
the faults occur in the primary or secondary winding. The block models the faulted
winding as a faulted inductor. The unfaulted winding is coupled to the faulted
winding. As a result, the actual equations involve a total of three coupled
windings: two for the faulted winding and one for the unfaulted winding. The
coupling between the primary and secondary windings is defined by the
**Coefficient of coupling** parameter.

The block can trigger the start of fault transition:

- At a specific time.
- After voltage exceeds the maximum permissible value a certain number of
  times.
- When current exceeds the maximum permissible value for longer than a
  specific time interval.

If you want to trigger a fault at a specific time, in the
**Fault Inspector** window, set **Trigger type** to
`Timed`. If you want to determine whether a system fails and, if
so, when it fails, in the **Fault Inspector** window, set **Trigger
type** to `Behavioral`.

If you select the behavioral trigger, the component fails as soon as one of the
trigger conditions is true.

Faultable inductors often require that you use the fixed-step local solver,
especially if your model transitions to a faulted state that includes short
circuits. For more information, see Making Optimal Solver Choices for Physical Simulation.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.

The **Primary current** and **Secondary
current** variables let you specify a high-priority target for the
initial inductor current in the respective winding at the start of simulation.
