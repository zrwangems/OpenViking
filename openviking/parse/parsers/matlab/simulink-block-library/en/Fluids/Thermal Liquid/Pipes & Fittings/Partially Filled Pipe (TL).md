---
type: simulink-block
title: 'Partially Filled Pipe (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pipes & Fittings'
documentation_page: 'partiallyfilledpipetl'
documentation_source_path: 'ref/partiallyfilledpipetl.html'
language: en
---

# Partially Filled Pipe (TL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port thermal liquid
  direction: conserving
- name: B
  summary: Liquid port thermal liquid
  direction: conserving
- name: AL
  summary: Relative liquid level of connected block, m physical signal
  direction: input
- name: L
  summary: Pipe liquid level, m physical signal
  direction: output
```

### Conserving

### **A** — Liquid port thermal liquid

Thermal liquid conserving port. Port **A** is always
higher than port **B**. When port
**A** is submerged, m˙A=m˙B.. When port **A** is exposed, m˙A=0.

### **B** — Liquid port thermal liquid

Thermal liquid conserving port. Port **A** is always
higher than port **B**. When port
**A** is submerged, m˙A=m˙B. When port **A** is exposed, any flow
into or out of port **B** changes the liquid level in
the pipe. A dry or partially dry pipe can only be filled through port
**B**.
### Input

### **AL** — Relative liquid level of connected block, m physical signal

Relative liquid level of the connected block in m, specified as a
physical signal. If the signal at **AL** is positive,
the pipe end is submerged. Otherwise the port is exposed.
### Output

### **L** — Pipe liquid level, m physical signal

Liquid level in the pipe in m, returned as a physical signal..
## Parameters
```yaml
parameters:
- name: Pipe length
  summary: Pipe length 5 m (default) | positive scalar
  group: Geometry
- name: Cross-sectional area
  summary: Pipe cross-sectional area 0.01 m^2 (default) | positive scalar
  group: Geometry
- name: Hydraulic diameter
  summary: Hydraulic diameter 0.1128 m (default) | positive scalar
  group: Geometry
- name: Elevation drop from port A to port B
  summary: Vertical distance between A and B 5 m (default) | positive scalar
  group: Geometry
- name: Initial liquid level
  summary: Starting liquid level 5 m (default) | positive scalar
  group: Geometry
- name: Liquid level below zero
  summary: Whether to notify if no liquid is in pipe Error (default) | None | Warning
  group: Geometry
- name: Gravitational acceleration
  summary: Acceleration of gravity 9.81 m/s^2 (default) | positive scalar
  group: Geometry
- name: Aggregate equivalent length of local resistances
  summary: Contribution of pipe geometry to hydraulic losses 1 m (default) | positive scalar
  group: Friction
- name: Internal surface absolute roughness
  summary: Pipe wall roughness 15e-6 m (default) | positive scalar
  group: Friction
- name: Laminar flow upper Reynolds number limit
  summary: Laminar flow upper threshold 2000 (default) | positive scalar
  group: Friction
- name: Turbulent flow lower Reynolds number limit
  summary: Turbulent flow lower threshold 4000 (default) | positive scalar
  group: Friction
- name: Laminar friction constant for Darcy friction factor
  summary: Pipe friction constant for laminar flows 64 (default) | positive scalar
  group: Friction
- name: Initial liquid temperature
  summary: Liquid temperature at start of simulation 293.15 K (default)
  group: Initial Conditions
```

### Geometry

### **Pipe length** — Pipe length `5 m` (default) | positive scalar

Pipe length.

### **Cross-sectional area** — Pipe cross-sectional area `0.01 m^2` (default) | positive scalar

Cross-sectional area of the pipe.

### **Hydraulic diameter** — Hydraulic diameter `0.1128 m` (default) | positive scalar

Hydraulic diameter used in calculations of the pipe Reynolds number.
For non-circular pipes, the hydraulic diameter is the effective diameter
of the fluid in the pipe. For circular pipes, the hydraulic diameter and
pipe diameter are the same.

### **Elevation drop from port A to port B** — Vertical distance between A and B `5 m` (default) | positive scalar

Vertical change in elevation of the pipe. Port **A**
is always higher than port **B**.

### **Initial liquid level** — Starting liquid level `5 m` (default) | positive scalar

Liquid level in the pipe at the beginning of the simulation.

### **Liquid level below zero** — Whether to notify if no liquid is in pipe `Error` (default) | `None` | `Warning`

Whether to notify if no liquid is in the pipe. Set this parameter to
`Warning` if you would like to receive a
warning when this occurs during simulation. Set the parameter to
`Error` if you would like the simulation to
stop when this occurs.

### **Gravitational acceleration** — Acceleration of gravity `9.81 m/s^2` (default) | positive scalar

Acceleration of gravity constant.

### Friction

### **Aggregate equivalent length of local resistances** — Contribution of pipe geometry to hydraulic losses `1 m` (default) | positive scalar

Length of pipe that would produce the equivalent hydraulic losses as
would a pipe with bends, area changes, or other non-uniform
attributes.

### **Internal surface absolute roughness** — Pipe wall roughness `15e-6 m` (default) | positive scalar

Pipe wall absolute roughness. This parameter is used to determine the
Darcy friction factor, which contributes to pressure loss in the
pipe.

### **Laminar flow upper Reynolds number limit** — Laminar flow upper threshold `2000` (default) | positive scalar

Upper Reynolds number limit to laminar flow. Beyond this number, the
fluid regime is transitional and approaches the turbulent regime and
becomes fully turbulent at the **Turbulent flow lower Reynolds
number limit**.

### **Turbulent flow lower Reynolds number limit** — Turbulent flow lower threshold `4000` (default) | positive scalar

Lower Reynolds number limit for turbulent flow. Below this number, the
flow regime is transitional and approaches laminar flow and becomes
fully laminar at the **Laminar flow upper Reynolds number
limit**.

### **Laminar friction constant for Darcy friction factor** — Pipe friction constant for laminar flows `64` (default) | positive scalar

Pipe friction constant for laminar flows. The laminar Darcy friction
factor captures the contribution of wall friction in pressure loss
calculations.

### Initial Conditions

### **Initial liquid temperature** — Liquid temperature at start of simulation `293.15` `K` (default)

Liquid temperature at the beginning of the simulation.
## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Pipe with variable liquid volume in an thermal liquid system

The Partially Filled Pipe (TL) block represents a pipe with
the capacity for varying internal liquid levels. The pipe may also become completely dry
during simulation.

In addition to liquid connections at ports **A** and
**B**, port **AL** receives the inlet liquid level
from connected blocks as a physical signal. If the value at **AL** is
greater than zero, **A** is submerged. If the value at
**AL** is less than or equal to zero, the port is exposed. The pipe
liquid level is transmitted as a physical signal to connecting blocks at port
**L**.

Port **A** is always higher than port **B**. If port
**A** becomes exposed, the pipe can be filled through port
**B**. When fluid enters the pipe through port
**B**, the mass flow rate through port **A** is 0
until the pipe is fully filled, at which point m˙A=−m˙B.

### When to Use the Partially Filled Pipe (TL) Block

This block can be used in conjunction with the Tank
(TL) block when fluid levels are expected to fall below the tank
inlet. Multiple Partially Filled Pipe (TL) blocks can
also be connected in series or parallel. However, because the block can only be
filled at port **B**, if port **A** of one block
in a parallel configuration becomes exposed, it may not be possible to refill this
pipe if its connection at port **B** cannot refill the pipe.

### Pressure Loss Over the Pipe

The pressure differential over the pipe,
*p*A –
*p*B, comprises losses due to wall
friction and hydrostatic pressure differences between the liquid surface height and
the liquid height at port **A**:

pA−pB=Δploss+Δpelev.

Friction losses depend on the fluid regime in the pipe. If the flow is laminar,
the friction losses are:

Δploss=−m˙BυfsL^2Dh2A2,

where:

- *ν* is the fluid kinematic viscosity.
- *f*S is the **Laminar
  friction constant for Darcy friction factor**.
- L^ is the sum of the pipe length and its
  **Aggregate equivalent length of local
  resistances**, in proportion to the pipe fill level: L^=(L+Ladd)llmax.
- *l*, *lmax*
  are the liquid level and the **Elevation drop from port A to
  port B**, respectively.
- *D*h is the pipe hydraulic
  diameter. If the pipe cross-section is not circular, the hydraulic
  diameter is the equivalent circular diameter.

If the flow is turbulent, the friction losses are:

Δploss=−m˙B|m˙B|fL^2ρDh2A2.

*f* is the Darcy friction factor for turbulent flows, which is determined
by the empirical Haaland correlation:

f={−1.8log10[6.9Re+(ε3.7Dh)1.11]}−2,

where *ε* is the **Internal surface
absolute roughness** parameter. The Reynolds number is based on the
mass flow rate at port **B** and the pipe hydraulic
diameter.

The hydrostatic pressure difference is Δpelev=ρgl.

### Mass Flow Rate

The flow in the pipe is dictated by the internal fluid level and the conditions at port
**B**. The pipe can be filled or drained at
**B** if the pipe is partially empty. If the pipe is fully
filled, m˙A=m˙B., and mass is conserved:

m˙A+m˙B=0.

The block determines the mass of fluid in the pipe by the
relative fill level of the pipe:

M=ρALllmax.

### Energy Balance

The block balances energy flow such that when port **A** is submerged,

McvdTdt=ϕA+ϕB−m˙Bgl.

When port **A** is exposed,

McvdTdt=ϕA+ϕB−m˙Bh−m˙Bgl,

where *cv* is the
specific heat at constant volume, *T* is the fluid temperature, and
*h* is the specific enthalpy.

### Assumptions and Limitations

This block does not account for dynamic compressibility or fluid inertia, and does
not model the dynamics of air (or second liquid) in the pipe.
