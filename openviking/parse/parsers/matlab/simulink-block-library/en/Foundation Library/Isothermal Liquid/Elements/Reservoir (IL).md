---
type: simulink-block
title: 'Reservoir (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'reservoiril'
documentation_source_path: 'ref/reservoiril.html'
language: en
---

# Reservoir (IL)

## Ports

### Input

### **P** — Pressure control signal, Pa physical signal

Physical signal port that provides the reservoir pressure control signal. The
signal saturates when its value drops below the minimum valid pressure specified by
the Isothermal Liquid Properties (IL) block connected
to the circuit.

#### Dependencies

This port is visible only if you set the **Reservoir type**
parameter to `Controlled`.
### Conserving

### **A** — Reservoir inlet isothermal liquid

Isothermal liquid conserving port associated with the reservoir inlet.

## Parameters

### **Reservoir type** — Specify whether reservoir pressure can change during simulation `Constant` (default) | `Controlled`

Select whether the reservoir pressure can change during simulation:

- `Constant` — The reservoir pressure remains constant
  during simulation. Port **P** is hidden.
- `Controlled` — The input physical signal at port
  **P** specifies the reservoir pressure, which can vary during
  simulation.

### **Reservoir pressure specification** — Specification method for reservoir pressure `Atmospheric pressure` (default) | `Specified pressure`

Specification method for the reservoir pressure:

- `Atmospheric pressure` — Use the atmospheric
  pressure specified by the Isothermal Liquid Properties
  (IL) block connected to the circuit.
- `Specified pressure` — Specify a value by using
  the **Reservoir pressure** parameter.

#### Dependencies

Enabled when the **Reservoir type** parameter is set to
`Constant`.

### **Reservoir pressure** — Pressure in reservoir `0.101325 MPa` (default) | positive scalar

Desired pressure in the reservoir. This pressure remains constant during simulation.
The specified pressure cannot be greater than the atmospheric pressure specified by the
Isothermal Liquid Properties (IL) block connected to
the circuit.

#### Dependencies

Enabled when the **Reservoir pressure specification** parameter
is set to `Specified pressure`.

## Libraries

Simscape / Foundation Library / Isothermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Isothermal liquid reservoir at constant or time-varying pressure

The Reservoir (IL) block represents an infinite reservoir
of isothermal liquid. Use this block to set the boundary condition in an isothermal liquid
network. The liquid in the reservoir can be at a constant pressure, either atmospheric or
specified by a block parameter. You can also control the pressure inside the reservoir by
using the physical signal input port **P**. Port **A**, an
isothermal liquid conserving port, represents the reservoir inlet.

The block icon changes depending on the values of the **Reservoir type**
and **Reservoir pressure specification** parameters.

| Reservoir Type | Reservoir Pressure Specification | Block Icon |
| --- | --- | --- |
| `Constant` | `Atmospheric pressure` |  |
| `Specified pressure` |  |
| `Controlled` | |  |

### Assumptions and Limitations

- The volume of liquid inside the reservoir is assumed infinite. Therefore, the flow
  is assumed quasi-steady.
- There is no flow resistance between port **A** and the reservoir
  interior.
