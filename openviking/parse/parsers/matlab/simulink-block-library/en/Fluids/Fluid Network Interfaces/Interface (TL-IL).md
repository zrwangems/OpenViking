---
type: simulink-block
title: 'Interface (TL-IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Fluid Network Interfaces'
documentation_page: 'interfacetlil'
documentation_source_path: 'ref/interfacetlil.html'
language: en
---

# Interface (TL-IL)

## Ports
```yaml
ports:
- name: TL
  summary: Liquid port thermal liquid
  direction: conserving
- name: IL
  summary: Liquid port isothermal liquid
  direction: conserving
- name: H
  summary: Liquid port isothermal liquid
  direction: conserving
```

### Conserving

### **TL** — Liquid port thermal liquid

Entry or exit port to the thermal liquid network.

### **IL** — Liquid port isothermal liquid

Entry or exit port to the isothermal liquid network.

#### Dependencies

To enable this port, set **Fluids domain
interface** to `Thermal Liquid (TL) -
Isothermal Liquid (IL)`.

### **H** — Liquid port isothermal liquid

Entry or exit port to the hydraulics (isothermal) liquid
network.

#### Dependencies

To enable this port, set **Fluids domain
interface** to `Thermal Liquid (TL) -
Hydraulic (H)`.
## Parameters
```yaml
parameters:
- name: Fluids domain interface
  summary: Connecting library types Thermal Liquid (TL) - Isothermal Liquid (IL) (default) | Thermal Liquid (TL) - Hydraulic
    (H)
  group: ''
- name: Temperature specification
  summary: Isothermal network temperature Constant (default) | Controlled
  group: ''
- name: Interface temperature
  summary: Isothermal network temperature 293.15 K (default) | positive scalar
  group: ''
- name: Cross-sectional area at port TL
  summary: Thermal liquid port area 0.01 m^2 (default) | positive scalar
  group: ''
```

### **Fluids domain interface** — Connecting library types `Thermal Liquid (TL) - Isothermal Liquid (IL)` (default) | `Thermal Liquid (TL) - Hydraulic (H)`

Specifies the connecting library types.

### **Temperature specification** — Isothermal network temperature `Constant` (default) | `Controlled`

Sets the isothermal network temperature. In the
`Constant` setting, you can specify the
isothermal network temperature in the **Hydraulic
temperature** parameter. In the
`Controlled` setting, the temperature in the
isothermal network is set by the thermal network.

### **Interface temperature** — Isothermal network temperature `293.15 K` (default) | positive scalar

Specifies the fluid temperature transmitted from the thermal liquid
network to the hydraulic or isothermal liquid network.

#### Dependencies

To enable this parameter, set **Temperature
specification** to
`Constant`.

### **Cross-sectional area at port TL** — Thermal liquid port area `0.01 m^2` (default) | positive scalar

Cross-sectional area of the thermal liquid port.
## Libraries

Simscape / Fluids / Fluid Network Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Connection between thermal and isothermal networks

The Interface block is a connector between thermal and isothermal fluid networks. The
fluid mass flow rate and pressure are matched between the networks, but fluid properties
are not passed between the two networks. To maintain fluid properties between the
thermal and isothermal components of your model, connect an Isothermal Liquid Predefined Properties (IL) block with the
desired properties to the isothermal network side.

You can connect Thermal Liquid library blocks with Isothermal Liquid library or
Hydraulics (Isothermal) library blocks. The temperature set in the isothermal system can
either be `Constant` or `Controlled`.
In the case of a `Controlled` temperature system, the
isothermal network temperature is set by the thermal liquid temperature. In the
`Constant` temperature setting, you specify the isothermal
network temperature directly.

### Thermal Liquid - Isothermal Liquid

When **Fluids domain interface** is set to `Thermal Liquid
(TL) - Isothermal Liquid (IL)`, the mass flow rate is conserved
over the two mass-flow-rate-based networks:

m˙TL+m˙IL=0,

where:

- m˙TL is the mass flow rate at the
  thermal liquid interface.
- m˙IL is the mass flow rate at the
  isothermal liquid interface.

The fluid absolute pressure is maintained between the thermal,
internal, and isothermal sections of the Interface block:

pTL=pIL.

### Thermal Liquid - Hydraulics (Isothermal)

The Hydraulics (Isothermal) Liquid library is based on volumetric flow rate. To
maintain flow continuity between both sides of the interface, the volumetric flow
rate is multiplied by the fluid density:

m˙TL+qHρH=0,

where:

- *q*H is the Hydraulics
  (Isothermal) volumetric flow rate.
- *ρ*H is the local Hydraulics
  (Isothermal) fluid density.

The Hydraulics (Isothermal) Liquid library blocks are constructed in terms of
gauge pressures. Pressure is converted to absolute pressure internally to match the
thermal network pressure:

pH+patm=pTL.
