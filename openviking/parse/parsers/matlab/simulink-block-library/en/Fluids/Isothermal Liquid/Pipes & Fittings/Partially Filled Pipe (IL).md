---
type: simulink-block
title: 'Partially Filled Pipe (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'partiallyfilledpipeil'
documentation_source_path: 'ref/partiallyfilledpipeil.html'
language: en
---

# Partially Filled Pipe (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Fluid entry or exit to the pipe. Port **A** is always
higher than port **B**. When port
**A** is submerged, m˙A=m˙B.. When port **A** is exposed, m˙A=0.

### **B** — Liquid port isothermal liquid

Fluid entry or exit to the pipe. Port **A** is always
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

## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Pipe with variable liquid volume in an isothermal liquid system

The Partially Filled Pipe (IL) block models a pipe with the capacity for varying
internal liquid levels. The pipe may also become completely dry during
simulation.

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

### When to Use the Partially Filled Pipe (IL) Block

This block can be used in conjunction with the Tank (IL) block when fluid levels
are expected to fall below the tank inlet. Multiple Partially Filled Pipe (IL)
blocks can also be connected in series or parallel. However, because a partially
filled pipe can only be filled at port **B**, if port
**A** of one block in a parallel configuration becomes exposed,
it may not be possible to refill this pipe if its connection at port
**B** cannot refill the pipe.

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

*f* is the Darcy friction factor for turbulent flows, which is
determined by the empirical Haaland correlation:

f={−1.8log10[6.9Re+(ε3.7Dh)1.11]}−2,

where *ε* is the **Internal surface
absolute roughness**. The Reynolds number is based on the mass flow
rate at port **B** and the pipe hydraulic diameter.

The hydrostatic pressure difference is Δpelev=ρgl.

### Mass Flow Rate

The flow in the pipe is dictated by the internal fluid level and the conditions at
port **B**. The pipe can be filled or drained at
**B** if the pipe is partially empty. If the pipe is fully
filled, m˙A=m˙B., and mass is conserved:

m˙A+m˙B=0.

The mass of fluid in the pipe is determined by the relative fill
level of the pipe:

M=ρALllmax.

### Assumptions and Limitations

This block does not account for dynamic compressibility or fluid inertia, and does
not model the dynamics of air (or second liquid) in the pipe.
