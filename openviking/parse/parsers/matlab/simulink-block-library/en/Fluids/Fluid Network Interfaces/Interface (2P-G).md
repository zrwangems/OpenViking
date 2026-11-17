---
type: simulink-block
title: 'Interface (2P-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Fluid Network Interfaces'
documentation_page: 'interface2pg'
documentation_source_path: 'ref/interface2pg.html'
language: en
---

# Interface (2P-G)

## Ports
```yaml
ports:
- name: 2P
  summary: Two-phase port two-phase fluid
  direction: conserving
- name: G
  summary: Fluid port gas
  direction: conserving
```

### Conserving

### **2P** — Two-phase port two-phase fluid

Two-phase fluid conserving port associated with the two-phase fluid at the
interface.

### **G** — Fluid port gas

Gas conserving port associated with the gas at the interface.
## Parameters
```yaml
parameters:
- name: Cross-sectional area at ports 2P and G
  summary: Port area 0.01 m^2 (default) | positive scalar
  group: ''
- name: Two-phase fluid superheated vapor check
  summary: Two-phase fluid superheated conditions check None (default) | Warning | Error
  group: ''
```

### **Cross-sectional area at ports 2P and G** — Port area `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the two-phase fluid and gas ports.

### **Two-phase fluid superheated vapor check** — Two-phase fluid superheated conditions check `None` (default) | `Warning` | `Error`

Action to perform when the fluid at port **2P** does not
meet superheated conditions.
## Libraries

Simscape / Fluids / Fluid Network Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Two-phase fluid and gas network interface

The Interface (2P-G) block represents a flow connection
between a two-phase fluid network and a gas network. Pressure, temperature, and mass
flow rate are equal at the interface. The block does not transfer the fluid properties
of each fluid network across the interface. To conserve fluid properties, ensure that
the Gas Properties (G) block and the
Two-Phase Fluid Properties (2P) block have
corresponding settings.

The fluid at the **2P** port must remain superheated. You can use the
**Two-phase fluid superheated vapor check** parameter to choose
what action the block performs if the fluid does not meet this condition.

### Mass and Momentum Balance

The block conserves mass such that

m˙2P+m˙G=0,

where:

- m˙G is the mass flow rate into port
  **G**.
- m˙2P is the mass flow rate into port
  **2P**.

The port pressures are equal:

PG=P2P.

### Energy Balance

The temperature is constant between the two fluid ports. The block calculates the energy
balance over the interface as

ΦG+Φ2P=m˙GhG+wG22+m˙2Ph2P+w2P22,

where:

- *ΦG* is the energy flow rate
  into port **G**.
- *Φ2P* is the energy flow rate
  into port **2P**.
- *hG* is the specific enthalpy
  at port **G**.
- *h2P* is the specific enthalpy
  at port **2P**.
- *vG* is the specific volume at
  port **G**.
- *v2P* is the specific volume
  at port **2P**.
- *wG* is the flow velocity at
  port **G** such that

  wG=m˙GvGS,

  where *S* is the value of the
  **Cross-sectional area at ports 2P and G**
  parameter.
- *w2P* is the flow velocity at
  port **2P** such that

  w2P=m˙2Pv2PS.
