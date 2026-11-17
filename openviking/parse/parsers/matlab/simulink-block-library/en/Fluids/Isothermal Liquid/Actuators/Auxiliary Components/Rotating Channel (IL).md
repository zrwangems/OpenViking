---
type: simulink-block
title: 'Rotating Channel (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'rotatingchannelil'
documentation_source_path: 'ref/rotatingchannelil.html'
language: en
---

# Rotating Channel (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port isothermal liquid
  direction: conserving
- name: W
  summary: Angular velocity, rad/s physical signal
  direction: input
```

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port.
### Input

### **W** — Angular velocity, rad/s physical signal

Rotating shaft angular velocity in rad/s, specified as a physical
signal.
## Parameters
```yaml
parameters:
- name: Channel area
  summary: Shaft channel cross-sectional area 1e-3 m^2 (default) | positive scalar
  group: ''
- name: Port B radius of rotation
  summary: Rotation radius 0.01 m (default) | positive scalar
  group: ''
- name: Discharge coefficient
  summary: Discharge coefficient 0.64 (default) | positive scalar
  group: ''
- name: Critical Reynolds number
  summary: Upper Reynolds number limit for laminar flow 150 (default) | positive scalar
  group: ''
```

### **Channel area** — Shaft channel cross-sectional area `1e-3` m^2 (default) | positive scalar

Shaft channel cross-sectional area for liquid entry/exit.

### **Port B radius of rotation** — Rotation radius `0.01` m (default) | positive scalar

Radius of swept circle of pipe rotation, specified at port
**B**.

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

Correction factor that accounts for discharge losses in theoretical
flows.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the orifice.
## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Rotating pipe with a fluid channel in an isothermal liquid network

The Rotating Channel (IL) block models a rotating pipe with a fluid channel in an
isothermal liquid network. The pipe angular velocity is set by a physical signal at port
**W**. Ports **A** and **B** are
isothermal liquid inlet and outlet ports.

Fluid passing through a rotating channel experiences pressure changes due to
resistance passing through the casing orifice and due to the fluid angular momentum. An
internal connection to an Orifice (IL) block accounts for
the local resistances. The pressure change in the block is modeled as:

P=ρAW2rB22,

where:

- *ρ*A is the fluid density at port
  **A**.
- *W* is the shaft angular velocity, received as a physical
  signal at port **W**.
- *r*B is the radius of rotation at
  port **B**.

The isothermal liquid outlet port can be connected to a Rotating Cylinder Force (IL) block to model
components such as a Rotating Single-Acting Actuator (IL).

### Assumptions and Limitations

- The effects of fluid inertia are not calculated.
- The pipe angular velocity is assumed to be constant or changes very
  slowly.
