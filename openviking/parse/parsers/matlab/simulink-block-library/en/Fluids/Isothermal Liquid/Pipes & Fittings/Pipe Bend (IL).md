---
type: simulink-block
title: 'Pipe Bend (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'pipebendil'
documentation_source_path: 'ref/pipebendil.html'
language: en
---

# Pipe Bend (IL)

## Ports

### Conserving

### **A** — Liquid port isothermal liquid

Liquid entry or exit port.

### **B** — Liquid port isothermal liquid

Liquid entry or exit port.

## Parameters

### **Pipe diameter** — Pipe diameter `0.01 m` (default) | positive scalar

Diameter of the pipe.

### **Bend radius** — Bend circle radius `0.04 m` (default) | positive scalar

Radius of the circle formed by the pipe bend.

### **Bend angle** — Bend angle `90 deg` (default) | positive scalar

Swept degree of the pipe bend.

### **Elevation gain from port A to port B** — Pipe elevation change `0 m` (default) | scalar

Elevation change along the length of the pipe from port
**A** to port **B**.

### **Gravitational acceleration** — Gravitational acceleration `9.81 m/s^2` (default) | scalar

Gravitational acceleration. The block only uses this parameter if the
value of the **Elevation gain from port A to port B**
parameter is not `0`.

### **Internal surface absolute roughness** — Pipe wall roughness `15e-6 m` (default) | positive scalar

Pipe wall absolute roughness. This parameter is used to determine the
Darcy friction factor, which contributes to pressure loss in the
pipe.

### **Enable dynamic compressibility** — Whether to model fluid compressibility `off` (default) | `on`

Whether to model any change in fluid mass due to fluid compressibility.
When you select **Fluid compressibility**, mass changes due
to varying fluid density in the segment are calculated. The fluid volume in
the pipe remains constant. In the Isothermal Liquid library, all blocks
calculate density as a function of pressure.

### **Initial liquid pressure** — Pipe pressure at beginning of simulation `0.101325 MPa` (default) | positive scalar

Pipe pressure at the beginning of the simulation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2025a: Model changes in pipe bend elevation

Use the **Elevation gain from port A to port B** parameter to
specify an elevation change along the length of the pipe bend.

## Description

Pipe bend segment in an isothermal liquid network

The Pipe Bend (IL) block models a curved pipe in an isothermal liquid network. You can
define the pipe characteristics to calculate losses due to friction and pipe curvature
and optionally model fluid compressibility.

### Pipe Curvature Loss Coefficient

The coefficient for pressure losses due to geometry changes comprises an angle
correction factor, *C*angle, and a bend
coefficient, *C*bend:

Kloss=CangleCbend.

The block calculates
*Cangle* as:

Cangle=0.0148θ−3.9716⋅10−5θ2,

where *θ* is the value of the **Bend
angle** parameter, in degrees.

The block calculates *Cbend* from the tabulated
ratio of the bend radius, *r*, to the pipe diameter,
*d*, for 90° bends from data based on Crane [1]:

Diagram displaying 90° pipe bend

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

The block interpolates the friction factor, *f*T,
for clean commercial steel from tabular data based on the pipe diameter [1]. This
table contains the pipe friction data for clean commercial steel pipe with flow in
the zone of complete turbulence.

| Nominal size (mm) | 5 | 10 | 15 | 20 | 25 | 32 | 40 | 50 | 72.5 | 100 | 125 | 150 | 225 | 350 | 609.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Friction factor, *fT* | .035 | .029 | .027 | .025 | .023 | .022 | .021 | .019 | .018 | .017 | .016 | .015 | .014 | .013 | .012 |

The correction factor is valid for a ratio of bend radius to
diameter between 1 and 24. Beyond this range, the block employs nearest-neighbor
extrapolation.

### Losses Due to Friction in Laminar Flows

The pressure loss formulations are the same for the flow at ports
**A** and **B**.

When the flow in the pipe is fully laminar, or below *Re* = 2000,
the pressure loss over the bend is:

Δploss=μλ2ρId2AL2m˙port,

where:

- *μ* is the fluid dynamic viscosity.
- *λ* is the Darcy friction factor constant, which is
  64 for laminar flow.
- *ρ*I is the internal fluid
  density.
- *d* is the pipe diameter.
- *L* is the bend length segment, the product of the
  **Bend radius** and the **Bend
  angle**: Lbend=rbendθ.
- *A* is the pipe cross-sectional area, π4d2.
- m˙port is the mass flow rate at the respective port.

### Losses due to Friction in Turbulent Flows

When the flow is fully turbulent, or greater than *Re* = 4000, the
pressure loss in the pipe is:

Δploss=(fDL2d+Kloss2)m˙port|m˙port|2ρIA2,

where *f*D is the Darcy
friction factor. This is approximated by the empirical Haaland equation and is based
on the **Internal surface absolute roughness**. The differential is
taken over half of the pipe segment, between port **A** to an
internal node, and between the internal node and port **B**.

### Pressure Differential for Incompressible Fluids

When the flow is incompressible, the pressure loss over the bend is

pA−pB=Δploss,A−Δploss,B+ρIgΔz,

where *g* is the value of the
**Gravitational acceleration** parameter and
*Δz* is the value of the **Elevation gain from port A
to port B** parameter.

### Pressure Differential for Compressible Fluids

When the flow is compressible, the block calculates the pressure loss over the bend based
on the internal fluid volume pressure, *p*I,

pA−pI=Δploss,A+ρIgΔz2pB−pI=Δploss,B−ρIgΔz2

### Mass Conservation

When you clear the **Enable dynamic compressibility** checkbox, the mass
flow into the pipe equals the mass flow out of the pipe

m˙A+m˙B=0.

When you select **Enable dynamic
compressibility**, the difference between the mass flow into and out of
the pipe depends on the fluid density change due to compressibility

m˙A+m˙B=p˙IdρIdpIV,

where *V* is the product of the pipe
cross-sectional area and bend length, *AL*.
