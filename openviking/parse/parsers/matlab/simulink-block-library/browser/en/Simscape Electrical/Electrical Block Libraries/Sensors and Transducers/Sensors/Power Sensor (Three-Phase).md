---
type: simulink-block
title: 'Power Sensor (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Sensors'
documentation_page: 'powersensorthreephase'
documentation_source_path: 'ref/powersensorthreephase.html'
language: en
---

# Power Sensor (Three-Phase)

## Ports

### Conserving

### **~1** — Three-phase port electrical

Expandable three-phase
electrical port.

### **~2** — Three-phase port electrical

Expandable three-phase
electrical port.
### Output

### **P** — Active power physical

Physical signal port associated with the active power
measurements.

### **Q** — Reactive power physical

Physical signal port associated with the reactive power
measurements.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **Load type** — Load type `Balanced` (default) | `Unbalanced`

Type of load. Select `Balanced` if the three-phase branches are
balanced, `Unbalanced` if the branches are not
balanced.

### **Rated frequency** — Rated frequency `60` `Hz` (default) | scalar

Rated frequency.

#### Dependencies

To enable this parameter, set **Load Type** to
`Unbalanced`.

### **Downstream configuration** — Downstream configuration `Without neutral` (default) | `With neutral`

Whether the downstream configuration is with or without neutral.

#### Dependencies

To enable this parameter, set **Load Type** to
`Unbalanced`.

### **Neutral conductor resistance divided by phase conductor resistance** — Ratio of neutral conductor resistance over phase conductor resistance `1` (default) | scalar

Ratio of neutral conductor resistance over phase conductor resistance, RneutralRphase..

#### Dependencies

To enable this parameter, set **Downstream
configuration** to `With
neutral`.

## Libraries

Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Three-phase ideal active and reactive power sensor

The Power Sensor (Three-Phase) block implements an ideal sensor for
active and reactive power measurement in balanced or unbalanced three-phase
branches.

For balanced branches, the block returns the correct value of the active and reactive
power at all time instants. This is the preferred option for a load-flow
analysis.

For unbalanced branches, to estimate the magnitude and phase, the block measures the phasors
of the three voltages and currents independently by using a one-moving-period Fourier
transform. For this reason, the output magnitude and phase are zero during the first
period.

### Unbalanced Branches Equations

The equivalent balanced phase voltage, current, and apparent power are:

Ve=13VabRMS2+VbcRMS2+VcaRMS2Ie=IaRMS2+IbRMS2+IcRMS2+ρI2nRMS3Se=3VeIe

where

- *VabRMS*,
  *VbcRMS*,
  and
  *VcaRMS*
  are the three phase-to-phase RMS voltages.
- *IaRMS*,
  *IbRMS*,
  and
  *IcRMS*
  are the RMS currents that flow through each of the three
  branches.
- *ρ* is the ratio of neutral conductor resistance over
  phase conductor resistance, specified by the Neutral
  conductor resistance divided by phase conductor resistance
  parameter.
- *InRMS*
  is the RMS neutral current.

The active power is then defined by:

P=VaRMSIaRMScos(φVa−φIa)+VbRMSIbRMScos(φVb−φIb)+VcRMSIcRMScos(φVc−φIc),

where:

- *VaRMS*,
  *VbRMS*,
  and
  *VcRMS*
  are the voltages of phase a, b, and c respectively.
- *φVa*,
  *φVb*,
  and *φVc*
  are the phase shifts of the *a*-phase,
  *b*-phase, and *c*-phase
  voltages.
- *φIa*,
  *φIb*,
  and *φIc*
  are the phase shifts of the *a*-phase,
  *b*-phase, and *c*-phase
  currents.

To compute the reactive power, the block first calculates its absolute value and
then finds the sign by looking at the sign of the phase shift:

abs(Q)=Se2−P2sign(Q)=sign(φ)Q=abs(Q)\*sign(Q)

where *φ =
φV\* -
φI\**. The
*\** symbol denotes the central phase in the
*[-π,π]* range.

### Load-Flow Analysis

If the block is in a network that is compatible
with the frequency-time simulation mode, you can perform a load-flow analysis on the
network. A load-flow analysis provides steady-state values that you can use to
initialize a machine.

For more information, see Perform a Load-Flow Analysis Using Simscape Electrical and Frequency and Time Simulation Mode.
