---
type: simulink-block
title: 'Dynamic Load'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'dynamicload'
documentation_source_path: 'ref/dynamicload.html'
language: en
---

# Dynamic Load

## Ports
```yaml
ports:
- name: P
  summary: Real power, W physical signal
  direction: input
- name: Q
  summary: Reactive power, V\*A physical signal
  direction: input
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Input

### **P** — Real power, W physical signal

Physical signal port associated with real power, specified as a
scalar.

### **Q** — Reactive power, V\*A physical signal

Physical signal port associated with reactive power, specified as a
scalar.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the dynamic load positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the dynamic load negative
terminal.
## Parameters
```yaml
parameters:
- name: Load type
  summary: Load type DC (default) | AC
  group: Main
- name: Minimum supply voltage
  summary: Minimum DC supply voltage 20 V (default) | scalar
  group: Main
- name: Minimum consumed power
  summary: Minimum consumed power 1e-3 W (default) | scalar
  group: Main
- name: Reverse conductance
  summary: Reverse conductance 1e-6 S (default) | scalar
  group: Main
- name: Transition voltage width
  summary: Transition voltage width 1e-3 V (default) | scalar
  group: Main
- name: Rated frequency
  summary: Rated frequency 60 Hz (default) | scalar
  group: Main
- name: Minimum supply voltage (RMS)
  summary: Minimum AC supply voltage 200 V (default) | scalar
  group: Main
- name: Voltage time constant
  summary: Time constant for voltage dynamics 0.01 s (default) | positive scalar
  group: Main
- name: Initial supply voltage (RMS)
  summary: Initial terminal voltage 300 V (default) | positive scalar
  group: Main
- name: Initial supply voltage angle
  summary: Initial angle of terminal voltage 0 deg (default) | scalar
  group: Main
- name: Open circuit fault
  summary: Option to add open circuit fault Add fault (default)
  group: Faults
- name: Open-circuit conductance
  summary: Open-circuit conductance 1e-4 S (default) | scalar
  group: Faults
- name: Trigger fault at time
  summary: Time before entering faulted state 0 s (default) | nonnegative scalar
  group: Faults
```

### Main

### **Load type** — Load type `DC` (default) | `AC`

Type of load. Select `DC` to use this load
with a DC supply or `AC` to use this load with
an AC supply.

### **Minimum supply voltage** — Minimum DC supply voltage `20` `V` (default) | scalar

Minimum voltage the DC supply needs to give the block to act as a
constant power load.

#### Dependencies

To enable this parameter, set **Load Type** to
`DC`.

### **Minimum consumed power** — Minimum consumed power `1e-3` `W` (default) | scalar

Minimum amount of power consumed by the block.

#### Dependencies

To enable this parameter, set **Load Type** to
`DC`.

### **Reverse conductance** — Reverse conductance `1e-6` `S` (default) | scalar

Value of the reverse conductance when the supply voltage becomes
negative.

#### Dependencies

To enable this parameter, set **Load Type** to
`DC`.

### **Transition voltage width** — Transition voltage width `1e-3` `V` (default) | scalar

Transition voltage width. This value is used to ensure smooth
transitions between the block's behaviors when the
supply voltage drops below the **Minimum
supply voltage** or becomes
negative.

#### Dependencies

To enable this parameter, set **Load Type** to
`DC`.

### **Rated frequency** — Rated frequency `60` `Hz` (default) | scalar

Rated frequency.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### **Minimum supply voltage (RMS)** — Minimum AC supply voltage `200` `V` (default) | scalar

Minimum voltage, in RMS, that the AC supply needs to give the block to act as a dynamic
load.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### **Voltage time constant** — Time constant for voltage dynamics `0.01` `s` (default) | positive scalar

*Since R2024a*

Time constant associated with the transients of the terminal voltage
measurement.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### **Initial supply voltage (RMS)** — Initial terminal voltage `300` `V` (default) | positive scalar

*Since R2024a*

Terminal voltage, in RMS, at time zero.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### **Initial supply voltage angle** — Initial angle of terminal voltage `0` `deg` (default) | scalar

*Since R2024a*

Angle of the terminal voltage at time zero.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### Faults

### **Open circuit fault** — Option to add open circuit fault `Add fault` (default)

Option to add an open-circuit fault in the Dynamic Load block.

To add a fault, click the **Add fault**
hyperlink.

### **Open-circuit conductance** — Open-circuit conductance `1e-4` `S` (default) | scalar

Conductance during the open-circuit state.

#### Dependencies

To enable this parameter, add a fault to the Dynamic Load block by
clicking the **Add fault** hyperlink in the
**Open circuit fault** parameter.

After you create the fault, you can change the properties in
the **Fault Inspector** window. When you open a block that has a fault, the
**Open Fault Inspector** hyperlink appears instead of the **Add
fault** hyperlink. For an example that shows how to include faults, see Analyze a DC Armature Winding Fault.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Timed`.
## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

### R2024a: Improved support for inductive nodes and bidirectional active power input

Prior to R2024a, to connect the Dynamic Load block to an
inductive node, you had to provide a large parasitic resistance. From R2024a, if you
set the **Load type** parameter to `AC`,
you can connect this block to an inductive node by specifying the **Voltage
time constant**, **Initial supply voltage (RMS)**, and
**Initial supply voltage angle** parameters. As a result of
this change, the **Minimum active power** parameter has been
removed. If your model saved in an earlier release contains this block you must set
appropriate values to the new parameters.

The Dynamic Load block now also consumes or
generates active power depending on the polarity of input active power
*Pin*. If
*Pin* is greater than 0, the block
consumes active power. If *Pin* is less than
0, the block generates active power.

## Description

Dynamic load for DC or AC supply

The Dynamic Load block implements a dynamic load for a DC or AC
supply.

If you set the **Load type** parameter to
`DC`:

- The consumed power of the block is equal to the **P**
  port as long as it is greater than the value of the **Minimum
  consumed power** parameter and the voltage from the DC supply
  is equal to or greater than the value specified for the **Minimum
  supply voltage** parameter.
- When the voltage from the DC supply drops below the
  **Minimum supply voltage**, the
  load behavior changes and the block acts as a resistive
  load. If the supply voltage becomes negative, the block
  acts as an open circuit conductance.

To ensure smooth transitions between these behaviors, the block uses a
third-order polynomial spline with continuous derivatives. You can
specify the width of this transition using the **Transition
voltage width** parameter.

If you set the **Load type** parameter to `AC`,
this table shows how the block calculates the consumed active and reactive power based
on the voltage from the supply, *V*.

| Range of *V* Values | Consumed Active and Reactive Power |
| --- | --- |
| V>Vmin | Pactual=PinQactual=Qin |
| V<Vmin | The block models a load with an impedance equal to:R=Vmin2PinPin2+Qin2X=Vmin2QinPin2+Qin2Z=R2+X2 |

In these equations:

- *Vmin* is the value of the Minimum supply voltage (RMS)
  parameter.
- *Pin* is the input active power of
  the Dynamic Load block, determined by
  external input port **P**.
- *Pactual* is the consumed active
  power of the Dynamic Load block.
- *Qin* is the input reactive power
  of the Dynamic Load block, determined by
  external input port **Q**.
- *Qactual* is the consumed reactive
  power of the Dynamic Load block.

The Dynamic Load block consumes or generates active
power depending on the polarity of input active power
*Pin*. If
*Pin* is greater than 0, the block
consumes active power. If *Pin* is less than 0,
the block generates active power.

### Faults

To model a fault in the Dynamic Load block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Dynamic Load block allows you to model an
electrical fault as an open circuit. The block can trigger fault events at a
specific time.

### Load-Flow Analysis

If the block is in a network that is compatible
with the frequency-time simulation mode, you can perform a load-flow analysis on the
network. A load-flow analysis provides steady-state values that you can use to
initialize a machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode.
