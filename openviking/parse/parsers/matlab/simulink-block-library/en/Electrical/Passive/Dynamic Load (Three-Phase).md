---
type: simulink-block
title: 'Dynamic Load (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'dynamicloadthreephase'
documentation_source_path: 'ref/dynamicloadthreephase.html'
language: en
---

# Dynamic Load (Three-Phase)

## Ports

### Input

### **P** — Real power, W physical signal

Physical signal port associated with real power, specified as a
scalar.

### **Q** — Reactive power, V\*A physical signal

Physical signal port associated with reactive power, specified as a
scalar.
### Conserving

### **~** — Three-phase voltage electrical

Composite three-phase
port associated with the three-phase voltage.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`.

### **a** — Phase A voltage electrical

Expanded three-phase
port associated with the phase A voltage.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **b** — Phase B voltage electrical

Expanded three-phase
port associated with the phase B voltage.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

### **c** — Phase C voltage electrical

Expanded three-phase
port associated with the phase C voltage.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`.

## Parameters

### Main

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

When you select `Composite three-phase ports`, the
**~** conserving port represents a composite three-phase
port.

When you select `Expanded three-phase ports`, the
**a**, **b**, and **c** conserving ports
represent the individual phases of a three-phase system.

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` (default) | positive scalar

*Since R2023a*

Rated electrical frequency.

### **Minimum supply voltage (phase-to-phase RMS)** — Minimum supply voltage `100` `V` (default) | scalar

Minimum voltage, in phase-to-phase RMS, that the supply needs for the block to act as a
dynamic load.

### **Voltage time constant** — Voltage dynamics time constant `0.01` `s` (default) | positive scalar

*Since R2023a*

Time constant associated with the transients of the terminal voltage measurement.

### **Initial supply voltage (phase-to-phase RMS)** — Initial terminal voltage `200` `V` (default) | positive scalar

*Since R2023a*

Terminal voltage, in phase-to-phase RMS, at time zero.

### **Initial supply voltage angle** — Terminal voltage angle of phase A at time zero `0` `deg` (default) | scalar

*Since R2023a*

Terminal voltage angle of phase A at time zero.

### **Parasitic conductance to electrical reference** — Parasitic conductance to electrical reference `0` `S` (default) | nonnegative scalar

*Since R2023a*

Parasitic conductance to electrical reference.

### Faults

### **Open circuit fault** — Option to add open circuit fault `Add fault` (default)

Option to add an open-circuit fault in the Dynamic Load (Three-Phase) block.

To add a fault, click the **Add fault**
hyperlink.

### **Open-circuit conductance** — Open-circuit conductance `1e-4` `S` (default) | scalar

Conductance during the open-circuit state.

#### Dependencies

To enable this parameter, add a fault to the Dynamic Load (Three-Phase) block by
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

**Introduced in R2019a**

### R2023a: Improved support for inductive nodes

Prior to R2023a, to connect the Dynamic Load (Three-Phase)
block to an inductive node, you had to provide a large parasitic resistance. From
R2023a, you can connect this block to an inductive node by specifying the
**Rated electrical frequency**, **Voltage time
constant**, **Initial supply voltage (phase-to-phase
RMS)**, **Initial supply voltage angle**, and
**Parasitic conductance to the electrical reference**
parameters. As a result of this change, the **Minimum active
power** parameter has been removed. If your model saved in an earlier
release contains this block you must set appropriate values to the new
parameters.

Additionally, the **Modeling option** parameter of the block has been
renamed to **Electrical connection** and moved to the
**Main** section.

### R2020b: Library path change

The Dynamic Load
(Three-Phase) block has been moved from the **Simscape** > **Electrical** > **Passive** > **RLC Assemblies** library to the **Simscape** > **Electrical** > **Passive** library.

If you have a script that depends on the library path or the Simscape component path of
this block, update it to reflect these changes.

## Description

Balanced three-phase dynamic load

The Dynamic Load (Three-Phase) block models a balanced
dynamic load for a balanced three-phase supply.

This table shows how the block calculates the consumed active and reactive power based on
the voltage from the supply, *V*.

| Range of *V* Values | Consumed Active and Reactive Power |
| --- | --- |
| V>Vmin | Pactual=PinQactual=Qin |
| V<Vmin | The block models a load with an impedance equal to:  R=Vmin2PinPin2+Qin2X=Vmin2QinPin2+Qin2Z=R2+X2 |

In these equations:

- *Vmin* is the value of the Minimum supply voltage (phase-to-phase RMS)
  parameter.
- *Pactual* is the consumed active
  power of the Dynamic Load (Three-Phase)
  block.
- *Pin* is the input active power of
  the Dynamic Load (Three-Phase) block,
  determined by external input port **P**.
- *Qactual* is the consumed reactive
  power of the Dynamic Load (Three-Phase)
  block.
- *Qin* is the input reactive power
  of the Dynamic Load (Three-Phase) block,
  determined by external input port **Q**.

The Dynamic Load (Three-Phase) block consumes or generates
active power depending on the polarity of input active power
*Pin*. If
*Pin* > 0, the block consumes active
power. If *Pin* < 0, the block generates
active power.

### Faults

To model a fault in the Dynamic Load (Three-Phase) block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Dynamic Load (Three-Phase) block allows you to
model an electrical fault as an open circuit. The block can trigger fault events at
a specific time.

### Load-Flow Analysis

If the block is in a network that is compatible
with the frequency-time simulation mode, you can perform a load-flow analysis on the
network. A load-flow analysis provides steady-state values that you can use to
initialize a machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode.
