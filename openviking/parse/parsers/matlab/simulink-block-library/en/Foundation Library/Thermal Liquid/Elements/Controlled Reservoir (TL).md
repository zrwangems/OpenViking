---
type: simulink-block
title: 'Controlled Reservoir (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'controlledreservoirtl'
documentation_source_path: 'ref/controlledreservoirtl.html'
language: en
---

# Controlled Reservoir (TL)

## Ports

### Input

### **T** — Temperature control signal, K physical signal

Physical signal port that provides the reservoir temperature control signal.
### Conserving

### **A** — Reservoir inlet thermal liquid

Thermal liquid conserving port associated with the reservoir inlet.

## Parameters

### **Reservoir pressure specification** — Specification method for reservoir pressure `Atmospheric pressure` (default) | `Specified pressure`

Specification method for the reservoir pressure:

- `Atmospheric pressure` — Use the atmospheric
  pressure specified by a Thermal Liquid Settings (TL)
  or Thermal Liquid Properties (TL) block connected to
  the circuit.
- `Specified pressure` — Specify a value by using
  the **Reservoir pressure** parameter.

### **Reservoir pressure** — Pressure in reservoir `0.101325 MPa` (default)

Desired pressure in the reservoir. This pressure remains constant during simulation.

#### Dependencies

Enabled when the **Reservoir pressure specification** parameter
is set to `Specified pressure`.

### **Cross-sectional area at port A** — Area normal to flow path at reservoir inlet `0.01 m^2` (default)

Cross-sectional area of the reservoir inlet pipe. The block uses this area to
determine the characteristic length of the pipe along which heat conduction occurs.

## Libraries

Simscape / Foundation Library / Thermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015a**

## Description

Thermal liquid reservoir at time-varying temperature

The Controlled Reservoir (TL) block represents an infinite
reservoir at fixed pressure and variable temperature. The reservoir and its inlet can be at
atmospheric pressure or at a specified pressure. Port **A**, a thermal liquid
conserving port, represents the reservoir inlet. Port **T**, a physical
signal port, provides the reservoir temperature control signal.

The inlet temperature depends on the direction of liquid flow. If the liquid flows into
the reservoir, the inlet temperature equals that of the upstream liquid and the reservoir acts
as a heat sink. If liquid flows out of the reservoir, the inlet temperature equals that of the
reservoir and the reservoir acts as a heat source.

To ensure a smooth temperature change at the reservoir inlet during liquid flow reversal,
the block includes heat conduction along a length equal to the effective diameter of the inlet
pipe. This diameter is a function of the specified cross-sectional area of the inlet
pipe.
