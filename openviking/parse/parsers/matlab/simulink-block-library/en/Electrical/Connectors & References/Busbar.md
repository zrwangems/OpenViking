---
type: simulink-block
title: 'Busbar'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'busbar'
documentation_source_path: 'ref/busbar.html'
language: en
---

# Busbar

## Ports

### Output

### **Vt** — Voltage physical signal

Physical signal port associated with the voltage measurement. The value is reported in
per-unit, i.e. phase-to-phase root mean square voltage divided by the
**Rated busbar voltage (phase-to-phase
RMS)**.

#### Dependencies

This port is visible only when, in the **Parameters** settings, the
**Measurement ports** parameter is set to
`Yes`.

### **ph** — Phase physical signal

Physical signal port associated with the voltage phase measurement.

#### Dependencies

This port is visible only when, in the **Parameters** settings, the
**Measurement ports** parameter is set to
`Yes`.

### **P** — Active power physical signal

Physical signal port associated with the active (real) power measurement.

#### Dependencies

This port is visible only when, in the **Parameters** settings, the
**Number of connections** parameter is set to
`2`, `3`, or
`4` and the **Measurement
ports** parameter is set to
`Yes`.

### **Q** — Reactive power physical signal

Physical signal port associated with the reactive (imaginary) power measurement.

#### Dependencies

This port is visible only when, in the **Parameters** settings, the
**Number of connections** parameter is set to
`2`, `3`, or
`4` and the **Measurement
ports** parameter is set to
`Yes`.
### Conserving

### **~1** — Three-phase connection 1 electrical

Composite three-phase electrical conserving port associated with the
first three-phase connection.

### **~2** — Three-phase connection 2 electrical

Composite three-phase electrical conserving port associated with the
second three-phase connection.

#### Dependencies

This port is visible only when, in the **Parameters** settings, the
**Number of connections** parameter is set to
`2`, `3`, or
`4`.

### **~3** — Three-phase connection 3 electrical

Composite three-phase electrical conserving port associated with the
third three-phase connection..

#### Dependencies

This port is visible only when, in the **Parameters** settings, the
**Number of connections** parameter is set to
`3` or
`4`.

### **~4** — Three-phase connection 4 electrical

Composite three-phase electrical conserving port associated with the
fourth three-phase connection.

#### Dependencies

This port is visible only when, in the **Parameters** settings, the
**Number of connections** parameter is set to
`4`.

## Parameters

### **Number of connections** — Number of port connections `2` (default) | `1` | `3` | `4`

Number of port connections that are exposed on the block.

The number of exposed ports on the block correlates to this parameter.

### **Rated busbar voltage (phase-to-phase RMS)** — Busbar rated voltage `sqrt(3) * 100 / sqrt(2)` `V` (default)

Rated phase-to-phase root mean square voltage of the busbar.

### **Network frequency** — Network frequency `60` `Hz` (default)

Frequency of the connected network.

### **Measurement ports** — Measurement port exposure `No` (default) | `Yes`

Visibility for the voltage, phase, active power, and reactive power physical signal
output measurement ports.

#### Dependencies

Ports **Vt** and **ph** are visible
only when this parameter is set to
`Yes`.

Ports **P** and **Q** are visible only when this
parameter is set to `Yes` and, in the
**Parameters** settings, the **Number of
connections** parameter is set to
`2`, `3`, or
`4`.

## Libraries

Simscape / Electrical / Connectors & References

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Load flow analysis busbar connector

The Busbar block is a connector for load-flow analysis. Use
this block with three-phase Simscape™
Electrical™ networks that are compatible with frequency-time simulation mode. After
completing simulation, the block adds an annotation showing the voltage, phase, active
power, and reactive power at each of its three-phase electrical conserving ports at the
time the simulation started. For the annotation to be added, Simscape logging must be enabled.

The block will simulate in time-based simulation mode, however it will not add the
annotation with initial load flow results unless the network is compatible with
frequency-time simulation mode and, on the Solver Configuration block, you check
`Start simulation from steady state`.
However, when using time-based simulation mode, the block calculates approximate values
for voltage, phase, active and reactive powers. You can view these values from
Simscape logging or by exposing the optional measurement ports on the block. The
level of approximation depends on how balanced the system is and on the level of
harmonics present.
