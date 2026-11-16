---
type: simulink-block
title: 'Interface (2P-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Fluid Network Interfaces'
documentation_page: 'interface2ptl'
documentation_source_path: 'ref/interface2ptl.html'
language: en
---

# Interface (2P-TL)

## Ports

### Conserving

### **2P** — Two-phase port two-phase fluid

Two-phase fluid conserving port associated with the two-phase fluid at the
interface.

### **TL** — Fluid port thermal liquid

Thermal liquid conserving port associated with the thermal liquid at the
interface.

## Parameters

### **Cross-sectional area at ports 2P and TL** — Port area `0.01` `m^2` (default) | positive scalar

Cross-sectional area of the thermal liquid and two-phase fluid ports.

### **Two-phase fluid subcooled liquid check** — Two-phase fluid subcooled conditions check `None` (default) | `Warning` | `Error`

Action to perform when the fluid at port **2P** does not
meet subcooled conditions.

## Libraries

Simscape / Fluids / Fluid Network Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Two-phase fluid and thermal liquid network interface

The Interface (2P-TL) block represents a flow connection
between a two-phase fluid network and a thermal liquid network. Pressure, temperature,
and mass flow rate are equal at the interface. The block does not transfer the fluid
properties of each fluid network across the interface. To conserve fluid properties,
ensure that the Thermal Liquid Properties (TL) block and
the Two-Phase Fluid Properties (2P) block have the same
settings.

The fluid at the **2P** port must remain subcooled. You can use the
**Two-phase fluid subcooled liquid check** parameter to choose what
action the block performs if the fluid does not meet this condition.

### Mass and Momentum Balance

The block conserves mass such that

m˙TL+m˙2P=0,

where:

- m˙TL is the mass flow rate into port
  **TL**.
- m˙2P is the mass flow rate into port
  **2P**.

The port pressures are equal:

PTL=P2P.

### Energy Balance

The temperature is constant between the two fluid ports. The block calculates the energy
balance over the interface as

ΦTL+Φ2P=m˙TLuTL+pTLvTL+wTL22+m˙2Pu2P+p2Pv2P+w2P22,

where:

- *ΦTL* is the energy flow rate
  into port **TL**.
- *Φ2P* is the energy flow rate
  into port **2P**.
- *hTL* is the specific internal
  energy at port **TL**.
- *h2P* is the specific internal
  energy at port **2P**.
- *vTL* is the specific volume
  at port **TL**.
- *v2P* is the specific volume
  at port **2P**.
- *wTL* is the flow velocity at
  port **TL**

  wTL=m˙TLvTLS,
- *w2P* is the flow velocity at
  port **2P**

  w2P=m˙2Pv2PS.
- *S* is the value of the **Cross-sectional
  area at ports 2P and TL** parameter.
