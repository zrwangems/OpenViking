---
type: simulink-block
title: 'Constant Power Load (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'constantpowerloadthreephase'
documentation_source_path: 'ref/constantpowerloadthreephase.html'
language: en
---

# Constant Power Load (Three-Phase)

## Ports
```yaml
ports:
- name: '~'
  summary: Three-phase voltage electrical
  direction: conserving
- name: a
  summary: Phase A voltage electrical
  direction: conserving
- name: b
  summary: Phase B voltage electrical
  direction: conserving
- name: c
  summary: Phase C voltage electrical
  direction: conserving
```

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
```yaml
parameters:
- name: Electrical connection
  summary: Electrical connection Composite three-phase ports (default) | Expanded three-phase ports
  group: Main
- name: Rated electrical frequency
  summary: Rated electrical frequency 60 Hz (default) | positive scalar
  group: Main
- name: Active power consumed
  summary: Active power consumed 1 kW (default) | scalar
  group: Main
- name: Reactive power consumed
  summary: Reactive power consumed 0 A*kV (default) | scalar
  group: Main
- name: Minimum supply voltage (phase-to-phase RMS)
  summary: Minimum supply voltage 100 V (default) | positive scalar
  group: Main
- name: Voltage time constant
  summary: Voltage dynamics time constant 0.01 s (default) | positive scalar
  group: Main
- name: Initial supply voltage (phase-to-phase RMS)
  summary: Initial terminal voltage 200 V (default) | positive scalar
  group: Main
- name: Initial supply voltage angle
  summary: Terminal voltage angle of phase A at time zero 0 deg (default) | scalar
  group: Main
- name: Parasitic conductance to electrical reference
  summary: Parasitic conductance to electrical reference 1e-6 S (default) | nonnegative scalar
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

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical
conserving ports with a single block port. You can use composite
three-phase ports to build models that correspond to single-line
diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a
three-phase system using three separate electrical conserving
ports.

### **Rated electrical frequency** — Rated electrical frequency `60` `Hz` (default) | positive scalar

*Since R2023a*

Rated electrical frequency.

### **Active power consumed** — Active power consumed `1` `kW` (default) | scalar

Active power consumed by the block.

### **Reactive power consumed** — Reactive power consumed `0` `A*kV` (default) | scalar

Reactive power consumed by the block.

### **Minimum supply voltage (phase-to-phase RMS)** — Minimum supply voltage `100` `V` (default) | positive scalar

Minimum voltage, in phase-to-phase RMS, that the supply needs for the block to act as a
constant power load.

### **Voltage time constant** — Voltage dynamics time constant `0.01` `s` (default) | positive scalar

*Since R2023a*

Time constant associated with the transients of the terminal voltage measurement.

### **Initial supply voltage (phase-to-phase RMS)** — Initial terminal voltage `200` `V` (default) | positive scalar

*Since R2023a*

Terminal voltage, in phase-to-phase RMS, at time zero.

### **Initial supply voltage angle** — Terminal voltage angle of phase A at time zero `0` `deg` (default) | scalar

*Since R2023a*

Terminal voltage angle of phase A at time zero.

### **Parasitic conductance to electrical reference** — Parasitic conductance to electrical reference `1e-6` `S` (default) | nonnegative scalar

*Since R2023a*

Parasitic conductance to electrical reference.

### Faults

### **Open circuit fault** — Option to add open circuit fault `Add fault` (default)

Option to add an open-circuit fault in the Constant Power Load (Three-Phase) block.

To add a fault, click the **Add fault**
hyperlink.

### **Open-circuit conductance** — Open-circuit conductance `1e-4` `S` (default) | scalar

Conductance during the open-circuit state.

#### Dependencies

To enable this parameter, add a fault to the Constant Power Load (Three-Phase) block by
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

### R2023a: Improved support for inductive nodes

Prior to R2023a, to connect the Constant Power Load
(Three-Phase) block to an inductive node, you had to provide a
large parasitic resistance. From R2023a, you can connect this block to an inductive
node by specifying the **Rated electrical frequency**,
**Voltage time constant**, **Initial supply voltage
(phase-to-phase RMS)**, **Initial supply voltage
angle**, and **Parasitic conductance to the electrical
reference** parameters. If your model saved in an earlier release
contains this block you must set appropriate values to these parameters.

Additionally, the **Modeling option** parameter of the block has been
renamed to **Electrical connection** and moved to the
**Main** section.

## Description

Three-phase constant power load

The Constant Power Load (Three-Phase) block implements a
constant power load for a three-phase supply.

The block outputs a nominal rated power as long as the voltage from the three-phase
supply is equal to or greater than the value specified for the **Minimum supply
voltage (phase-to-phase RMS)** parameter.

When the voltage from the three-phase supply drops below the value of
**Minimum supply voltage (phase-to-phase
RMS)**, the load behavior changes and the block models a
load with constant impedance.

### Equations

When the voltage from the three-phase supply is greater than the value specified
for the **Minimum supply voltage (phase-to-phase RMS)** parameter,
the block acts in constant PQ mode.

The active and reactive power are defined by:

P=32VpkIpkcos(φV−φI)Q=32VpkIpksin(φV−φI)

where:

- *Vpk* is the voltage peak
  magnitude.
- φI=φV−atan(QP) is the phase of the current.
- Ipk=23PVpkcos(φV−φI) is the current peak magnitude.

During the first period, the peak current is equal to 0 A.

When the voltage from the three-phase supply is less than or equal to the value
specified for the **Minimum supply voltage (phase-to-phase RMS)**
parameter, the block acts in constant Z mode.

The active and reactive power are defined by:

P=32Vpk2RR2+X2Q=32Vpk2XR2+X2

where:

- R=V2line RMSminPP2+Q2 is the constant resistance.
- X=V2line RMSminQP2+Q2 is the constant reactance.
- *Vline
  RMSmin* is the
  **Minimum supply voltage (phase-to-phase
  RMS)**.

### Load-Flow Analysis

If the block is in a network that is compatible with
frequency-time simulation mode, you can perform a load-flow analysis on the network.
A load-flow analysis provides steady-state values that you can use to initialize a
machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode.

### Faults

To model a fault in the Constant Power Load (Three-Phase) block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Constant Power Load (Three-Phase) block allows
you to model an electrical fault as an open circuit. The block can trigger fault
events at a specific time.
