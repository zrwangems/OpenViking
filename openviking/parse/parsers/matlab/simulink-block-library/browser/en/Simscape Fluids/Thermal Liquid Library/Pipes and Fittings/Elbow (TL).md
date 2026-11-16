---
type: simulink-block
title: 'Elbow (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Pipes and Fittings'
documentation_page: 'elbowtl'
documentation_source_path: 'ref/elbowtl.html'
language: en
---

# Elbow (TL)

## Ports

### Conserving

### **A** — Pipe bend entrance or exit thermal liquid

Thermal liquid conserving port associated with the liquid entrance or
exit of the pipe bend.

### **B** — Pipe bend entrance or exit thermal liquid

Thermal liquid conserving port associated with the liquid entrance or
exit of the pipe bend.

## Parameters

### **Elbow type** — Bend geometry `Smoothly curved` (default) | `Sharp-edged (Miter)`

Bend specification of the pipe segment. A sharp-edged, or mitre, bend
introduces a sharp change in flow direction, such as at a pipe joint, and
the flow losses are modeled by a separate set of empirical data from
gradually-turning pipe segments.

### **Elbow internal diameter** — Pipe internal diameter `0.01 m` (default) | positive scalar

Internal diameter of the pipe elbow segment.

### **Elbow angle** — Pipe curve angle `90 deg` (default) | positive scalar

Angle of the swept pipe curve.

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

Upper Reynolds number limit for laminar flow through the pipe segment.

## Libraries

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Pipe turn in a thermal liquid network

The Elbow (TL) block represents flow in a pipe turn in
a thermal liquid network. Pressure losses due to pipe turns are calculated, but the
block omits the effects of viscous friction.

Two **Elbow type** settings are available:
`Smoothly-curved` and `Sharp-edged
(Miter)`. For a smooth pipe with a 90° bend and losses due to friction,
you can also use the Pipe Bend (TL) block.

### Loss Coefficients

When the **Elbow type** parameter is `Smoothly
curved`, the block calculates the loss coefficient as:

K=30fTCangle.

The block calculates
*Cangle*, the angle correction factor,
from Keller [2] as

Cangle=0.0148θ−3.9716⋅10−5θ2,

where *θ* is the value of the **Bend
angle** parameter in degrees. The block defines the friction factor,
*f*T, as the value for clean commercial
steel. The block then interpolates the values from tabular data based on the
internal elbow diameter for *fT* based on
Crane [1]. This table contains the pipe friction data for clean commercial steel
pipe with flow in the zone of complete turbulence.

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

The values from Crane are valid for diameters up to 600 millimeters.
The friction factor for larger diameters or for wall roughness beyond this range is
calculated by nearest-neighbor extrapolation.

When the **Elbow type** parameter is `Sharp-edged
(Miter)`, the block calculates the loss coefficient
*K* for the bend angle, *α*, according to
Crane [1].

| *α* | 0° | 15° | 30° | 45° | 60° | 75° | 90° |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 2 *fT* | 4 *fT* | 8 *fT* | 15 *fT* | 25 *fT* | 40 *fT* | 60 *fT* |

Diagram displaying Mitre bends and a table for K values and corresponding bend angles.

### Mass Flow Rate

Mass is conserved through the pipe segment:

m˙A+m˙B=0.

The mass flow rate through the elbow is calculated as:

m˙=A2ρ¯KΔp[Δp2+Δpcrit2]1/4,

where:

- *A* is the flow area.
- ρ¯ is the average fluid density.
- *Δp* is the pipe segment pressure difference,
  *p*A –
  *p*B.

The critical pressure difference,
*Δp*crit, is the pressure differential
associated with the **Critical Reynolds number**,
*Re*crit, the flow regime transition
point between laminar and turbulent flow:

Δpcrit=ρ¯2K(νRecritD)2,

where

- *ν* is the fluid kinematic viscosity.
- *D* is the elbow internal diameter.

### Energy Balance

The block balances energy such that

ΦA+ΦB=0,

where:

- *ϕA* is the energy flow rate
  at port **A**.
- *ϕB* is the energy flow rate
  at port **B**.
