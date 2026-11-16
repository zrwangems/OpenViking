---
type: simulink-block
title: 'Controlled Reservoir (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'controlledreservoirg'
documentation_source_path: 'ref/controlledreservoirg.html'
language: en
---

# Controlled Reservoir (G)

## Ports

### Input

### **P** — Pressure control signal, Pa physical signal

Physical signal port that provides the reservoir pressure control
signal.

### **T** — Temperature control signal, K physical signal

Physical signal port that provides the reservoir temperature
control signal.
### Conserving

### **A** — Reservoir inlet gas

Gas conserving port associated with the reservoir inlet.

## Parameters

### **Cross-sectional area at port A** — Area normal to flow path at the reservoir inlet `0.01 m^2` (default)

The cross-sectional area of the reservoir inlet, in the direction normal
to gas flow path.

## Libraries

Simscape / Foundation Library / Gas / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Boundary conditions for gas network at time-varying pressure and temperature

The Controlled Reservoir (G) block represents an infinite
reservoir at variable pressure and temperature. Port **A**, a gas
conserving port, represents the reservoir inlet. Port **P**, a physical
signal port, provides the reservoir pressure control signal. Port
**T**, a physical signal port, provides the reservoir temperature
control signal.

The volume of gas inside the reservoir is assumed infinite.
Therefore, the flow is assumed quasi-steady.

Gas enters and leaves the reservoir at the reservoir pressure,
but its temperature is determined by the direction of gas flow. If
gas flows into the reservoir, its temperature is determined by the
gas network upstream. The reservoir acts as a heat sink. If gas flows
out of the reservoir, its temperature equals that of the reservoir.
The reservoir acts as a heat source.

### Assumptions and Limitations

- Gas in the reservoir is quasi-steady.
