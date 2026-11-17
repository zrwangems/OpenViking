---
type: simulink-block
title: 'Reservoir (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'reservoirg'
documentation_source_path: 'ref/reservoirg.html'
language: en
---

# Reservoir (G)

## Ports
```yaml
ports:
- name: A
  summary: Reservoir inlet gas
  direction: conserving
```

### Conserving

### **A** — Reservoir inlet gas

Gas conserving port associated with the reservoir inlet.
## Parameters
```yaml
parameters:
- name: Reservoir pressure specification
  summary: Select specification method for reservoir pressure Atmospheric pressure (default) | Specified pressure
  group: ''
- name: Reservoir pressure
  summary: Pressure in the reservoir 0.101325 MPa (default)
  group: ''
- name: Reservoir temperature
  summary: Temperature in the reservoir 293.15 K (default)
  group: ''
- name: Cross-sectional area at port A
  summary: Area normal to flow path at the reservoir inlet 0.01 m^2 (default)
  group: ''
```

### **Reservoir pressure specification** — Select specification method for reservoir pressure `Atmospheric pressure` (default) | `Specified pressure`

Select a specification method for the reservoir pressure:

- `Atmospheric pressure` — Use the
  atmospheric pressure, specified by the Gas Properties
  (G) block connected to the circuit.
- `Specified pressure` —
  Specify a value by using the **Reservoir pressure** parameter.

### **Reservoir pressure** — Pressure in the reservoir `0.101325 MPa` (default)

Enter the desired pressure in the reservoir. This pressure remains
constant during simulation.

#### Dependencies

Enabled when the **Reservoir pressure specification** parameter
is set to `Specified pressure`.

### **Reservoir temperature** — Temperature in the reservoir `293.15 K` (default)

Enter the desired temperature in the reservoir. This temperature
remains constant during simulation.

### **Cross-sectional area at port A** — Area normal to flow path at the reservoir inlet `0.01 m^2` (default)

The cross-sectional area of the reservoir inlet, in the direction
normal to gas flow path.
## Libraries

Simscape / Foundation Library / Gas / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Boundary conditions for gas network at constant pressure and temperature

The Reservoir (G) block represents an infinite reservoir at
fixed pressure and temperature. The reservoir and its inlet can be at atmospheric
pressure or at a specified pressure. Port **A**, a gas conserving port,
represents the reservoir inlet.

The volume of gas inside the reservoir is assumed infinite.
Therefore, the flow is assumed quasi-steady.

Gas enters and leaves the reservoir at the reservoir pressure,
but its temperature is determined by the direction of gas flow. If
gas flows into the reservoir, its temperature is determined by the
gas network upstream. The reservoir acts as a heat sink. If gas flows
out of the reservoir, its temperature equals that of the reservoir.
The reservoir acts as a heat source.

This block also functions as a reference point for pressure and temperature measurements in a
gas network. These measurements are relative to the reservoir pressure and temperature,
respectively. Connect the reservoir to port **B** of a
Pressure and Temperature Sensor (G) block to measure
relative pressure and temperature of a node connected to the **A** port
of the sensor.

### Assumptions and Limitations

- Reservoir pressure and temperature are constant.
- Gas in the reservoir is quasi-steady.
