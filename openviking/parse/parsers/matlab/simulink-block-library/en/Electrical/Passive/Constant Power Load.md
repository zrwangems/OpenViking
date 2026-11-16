---
type: simulink-block
title: 'Constant Power Load'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'constantpowerload'
documentation_source_path: 'ref/constantpowerload.html'
language: en
---

# Constant Power Load

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the constant power load
positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the constant power load
negative terminal.

## Parameters

### Main

### **Load type** — Load type `DC` (default) | `AC`

Type of load. Select `DC` to use this load
with a DC supply or `AC` to use this load with
an AC supply.

### **Power consumed** — Power consumed `100` `W` (default) | scalar

Nominal power that the block consumes.

#### Dependencies

To enable this parameter, set **Load Type** to
`DC`.

### **Minimum supply voltage** — Minimum DC supply voltage `20` `V` (default) | scalar

Minimum voltage the DC supply needs to give the block to act as a
constant power load.

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

Transition voltage width used to ensure smooth transitions between
the block's behaviors when the supply voltage drops
below the **Minimum supply
voltage** or becomes negative.

#### Dependencies

To enable this parameter, set **Load Type** to
`DC`.

### **Active power consumed** — Active power consumed `500` `W` (default) | scalar

Active power that the block consumes.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### **Reactive power consumed** — Reactive power consumed `0` `V*A` (default) | scalar

Reactive power that the block consumes.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### **Rated frequency** — Rated frequency `60` `Hz` (default) | scalar

Rated frequency.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### **Minimum supply voltage (RMS)** — Minimum AC supply voltage `200` `V` (default) | scalar

Minimum voltage, in RMS, the AC supply needs to give the block to act
as a constant power load.

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

Option to add an open-circuit fault in the Constant Power Load block.

To add a fault, click the **Add fault**
hyperlink.

### **Open-circuit conductance** — Open-circuit conductance `1e-4` `S` (default) | scalar

Conductance during the open-circuit state.

#### Dependencies

To enable this parameter, add a fault to the Constant Power Load block by
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

**Introduced in R2020a**

### R2024a: Improved support for inductive nodes

Prior to R2024a, to connect the Constant Power Load block to
an inductive node, you had to provide a large parasitic resistance. From R2024a, if
you set the **Load type** parameter to
`AC`, you can connect this block to an inductive node
by specifying the **Voltage time constant**, **Initial
supply voltage (RMS)**, and **Initial supply voltage
angle** parameters.

## Description

Constant power load for DC or AC supply

The Constant Power Load block implements a constant power load for a DC or AC
supply.

If you set the **Load type** parameter to
`DC`:

- The block outputs a nominal rated power as long as the voltage from the DC
  supply is greater than or equal to the **Minimum supply
  voltage** parameter value.
- When the voltage from the DC supply drops below the
  **Minimum supply voltage**
  parameter value, the load behavior changes and the block
  acts as a constant resistance. If the supply voltage
  becomes negative, the block acts as a constant reverse
  conductance.

To ensure smooth transitions between these behaviors, the block uses a
third-order polynomial spline with continuous derivatives. You can
specify the width of this transition using the **Transition
voltage width** parameter.

If you set the **Load type** parameter to
`AC`:

- The block outputs a nominal rated power at steady state as long as the
  voltage from the AC supply is greater than or equal to the **Minimum
  supply voltage (RMS)** parameter value. The block calculates
  the RMS power in harmonic approximation so that the block can calculate the
  power for AC voltage signals with time-dependent amplitudes. If the time
  scale of the amplitude change is comparable to the period of the alternating
  current, the instantaneous power briefly changes during the transition
  period.
- When the voltage from the AC supply drops below the
  **Minimum supply voltage (RMS)**
  parameter value, the load behavior changes and the block
  models a load with constant impedance.

For more information about the equations for the
`AC` load type in a three-phase system, see the Equations
section of the Constant Power Load
(Three-Phase) block.

### Faults

To model a fault in the Constant Power Load block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Constant Power Load block allows you to model
an electrical fault as an open circuit. The block can trigger fault events at a
specific time.

### Load-Flow Analysis

If the block is in a network that is compatible
with the frequency-time simulation mode, you can perform a load-flow analysis on the
network. A load-flow analysis provides steady-state values that you can use to
initialize a machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode.
