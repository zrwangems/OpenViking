---
type: simulink-block
title: 'Constant Current Load (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'constantcurrentloadthreephase'
documentation_source_path: 'ref/constantcurrentloadthreephase.html'
language: en
---

# Constant Current Load (Three-Phase)

## Ports

### Conserving

### **~** — Three-phase voltage electrical

Expandable three-phase
electrical port associated with the three-phase
voltage.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### Main

### **Consumed current (RMS)** — Root mean square consumed current `1` `A` (default) | scalar

Root mean square current consumed by the block.

### **Minimum supply voltage (phase-to-phase RMS)** — Minimum supply voltage `10` `V` (default) | scalar

Minimum voltage, in phase-to-phase RMS, that the supply must provide for the block to
act as a current load.

### Faults

### **Open circuit fault** — Option to add open circuit fault `Add fault` (default)

Option to add an open-circuit fault in the Constant Current Load (Three-Phase) block.

To add a fault, click the **Add fault**
hyperlink.

### **Open-circuit conductance** — Open-circuit conductance `1e-4` `S` (default) | scalar

Conductance during the open-circuit state.

#### Dependencies

To enable this parameter, add a fault to the Constant Current Load (Three-Phase) block by
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

Maximum permissible power value. If the power exceeds this value for
longer than the **Time to fail when exceeding power**
parameter value, then the block enters the faulted state.

#### Dependencies

To enable this parameter, set **Trigger Type** to
`Behavioral`.

### **Time to fail when exceeding power** — Maximum length of time the power exceeds the threshold `1` `s` (default)

Maximum length of time that the power can exceed the maximum
permissible value without triggering the fault.

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

Three-phase constant current load

The Constant Current Load (Three-Phase) block implements a constant
current load for a three-phase supply.

This block consumes a current equal to the value of the **Consumed current
(RMS)** parameter as long as the voltage from the three-phase supply is
equal to or greater than the value specified for the **Minimum supply voltage
(phase-to-phase RMS)** parameter.

When the voltage from the three-phase supply drops below the value of
**Minimum supply voltage (phase-to-phase RMS)**, the load behaviour
changes and the block models a load with constant resistance.

### Equations

If the three-phase voltages are balanced, the phase-to-phase RMS voltage is defined by this equation:

VlineRMS=(va−vdc)2+(vb−vdc)2+(vc−vdc)2,

where vdc=va+vb+vc3.

The currents for each of the three phases are defined by this equation:

ik(t)=vk(t)Requiv,

where *Requiv* is the
equivalent resistance and depends on value of the **Minimum supply voltage
(phase-to-phase RMS)** parameter.

If the voltage from the three-phase supply is greater than the value specified for the
**Minimum supply voltage (phase-to-phase RMS)** parameter, the
equivalent resistance is defined by:

Requiv=vpk2IRMSconsumed,

where *vpk* is the
voltage peak magnitude and
*IRMSconsumed*
is the value of the **Consumed current (RMS)** parameter.

If the voltage from the three-phase supply is less than the value specified for
the **Minimum supply voltage (phase-to-phase RMS)** parameter, the
equivalent resistance is defined by:

Requiv=vphRMSminIRMSconsumed,

where vphRMSmin=vlineRMSmin3 is the phase-to-ground RMS minimum voltage.

### Faults

To model a fault in the Constant Current Load (Three-Phase) block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Constant Current Load (Three-Phase) block allows you to
model an electrical fault as an open circuit. The block can trigger fault events
either:

- At a specific time
- When a power limit is exceeded for longer than a specific time
  interval

### Load-Flow Analysis

If the block is in a network that is compatible
with frequency-time simulation mode, you can perform a load-flow analysis on the
network. A load-flow analysis provides steady-state values that you can use to
initialize a machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode.
