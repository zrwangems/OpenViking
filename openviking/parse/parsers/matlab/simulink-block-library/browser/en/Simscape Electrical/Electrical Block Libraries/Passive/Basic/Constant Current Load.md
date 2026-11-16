---
type: simulink-block
title: 'Constant Current Load'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Basic'
documentation_page: 'constantcurrentload'
documentation_source_path: 'ref/constantcurrentload.html'
language: en
---

# Constant Current Load

## Ports

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the constant current load
positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the constant current load
negative terminal.

## Parameters

### Main

### **Load type** — Load type `DC` (default) | `AC`

Type of load. Select `DC` to use this load
with a DC supply or `AC` to use this load with
an AC supply.

### **Consumed current** — Current consumed `1` `A` (default) | scalar

Current consumed by the block.

#### Dependencies

To enable this parameter, set **Load Type** to
`DC`.

### **Minimum supply voltage** — Minimum DC supply voltage `5` `V` (default) | scalar

Minimum voltage the DC supply needs to give the block to act as a
constant current load.

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
block behaviors when the supply voltage drops below
the value of the **Minimum supply
voltage** parameter or becomes
negative.

#### Dependencies

To enable this parameter, set **Load Type** to
`DC`.

### **Consumed current (RMS)** — Root mean square consumed current `100` `A` (default) | scalar

Root mean square current consumed by the block.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### **Rated frequency** — Rated frequency `60` `Hz` (default) | scalar

Rated frequency.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### **Minimum supply voltage (RMS)** — Minimum AC supply voltage `200` `V` (default) | scalar

Minimum voltage, in RMS, that the AC supply must provide for the block to act as a
constant current load.

#### Dependencies

To enable this parameter, set **Load Type** to
`AC`.

### Faults

### **Open circuit fault** — Option to add open circuit fault `Add fault` (default)

Option to add an open-circuit fault in the Constant Current Load block.

To add a fault, click the **Add fault**
hyperlink.

### **Open-circuit conductance** — Open-circuit conductance `1e-4` `S` (default) | scalar

Conductance during the open-circuit state.

#### Dependencies

To enable this parameter, add a fault to the Constant Current Load block by
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

### **Maximum permissible power** — Power threshold to fault transition `inf` `W` (default)

Maximum permissible power value. If the power exceeds this value for longer than the
**Time to fail when exceeding power** parameter
value, then the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding power** — Maximum length of time the power exceeds the threshold `1` `s` (default)

Maximum length of time that the power can exceed the maximum permissible value without
triggering the fault.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Constant current load for DC or AC supply

The Constant Current Load block implements a constant current load for
a DC or AC supply.

If you set the **Load type** parameter to
`DC`:

- The consumed current of this block is equal to the value of the
  **Consumed current** parameter as long as the voltage
  from the DC supply is equal to or greater than the value specified for the
  **Minimum supply voltage** parameter.
- When the voltage from the DC supply drops below
  **Minimum supply voltage**, the
  load behavior changes and the block models a resistive
  load. If the supply voltage becomes negative, the block
  models a small open-circuit conductance.

To ensure smooth transitions between these behaviors, the block uses a
third-order polynomial spline with continuous derivatives. You can
specify the width of this transition using the **Transition
voltage width** parameter.

If you set the **Load type** parameter to `AC`:

- The root mean square consumed current of this block is equal to the value
  of the **Consumed current (RMS)** parameter as long as the
  voltage from the AC supply is equal to or greater than the value specified
  for the **Minimum supply voltage (RMS)** parameter.
- When the voltage from the AC supply drops below the
  **Minimum supply voltage (RMS)**
  parameter, the load behavior changes and the block
  models a load with constant resistance.

### Equations

If you set the **Load type** parameter to
`AC`, the block calculates the peak voltage,
*Vpk*, through harmonic
approximation of the instantaneous voltage by using a one-period-integrated Fourier
transform:

Re=f0∫v sin(2πf0t)Im=f0∫v sin(2πf0t+π2)Vpk=2Re2+Im2

During the first period, the peak voltage is equal to `0`
`V`. The current is defined by this equation:

i(t)=V(t)Requiv,

where *Requiv* is the
equivalent resistance and depends on the value of the **Minimum supply
voltage (RMS)** parameter.

If the voltage from the three-phase supply is greater than the value specified for the
**Minimum supply voltage (RMS)** parameter, the equivalent
resistance is defined by:

Requiv=Vpk2IRMSconsumed,

where *Vpk* is the
voltage peak magnitude and
*IRMSconsumed*
is the value of the **Consumed current (RMS)** parameter.

If the voltage from the three-phase supply is less than the value specified for the
**Minimum supply voltage (RMS)** parameter, the equivalent
resistance is defined by:

Requiv=VRMSminIRMSconsumed,

where
*VRMSmin* is
the value of the **Minimum supply voltage (RMS)** parameter.

### Faults

To model a fault in the Constant Current Load block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Constant Current Load block allows you to model an
electrical fault as an open circuit. The block can trigger fault events
either:

- At a specific time
- When a power limit is exceeded for longer than a specific time
  interval

### Load-Flow Analysis

If the block is in a network that is compatible
with the frequency-time simulation mode, you can perform a load-flow analysis on the
network. A load-flow analysis provides steady-state values that you can use to
initialize a machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode.
