---
type: simulink-block
title: 'Elbow (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Pipes & Fittings'
documentation_page: 'elbowma'
documentation_source_path: 'ref/elbowma.html'
language: en
---

# Elbow (MA)

## Ports
```yaml
ports:
- name: A
  summary: Inlet or outlet moist air
  direction: conserving
- name: B
  summary: Inlet or outlet moist air
  direction: conserving
```

### Conserving

### **A** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the
pipe. This block has no intrinsic directionality.

### **B** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the
pipe. This block has no intrinsic directionality.
## Parameters
```yaml
parameters:
- name: Elbow type
  summary: Bend geometry Smoothly curved (default) | Sharp-edged (Miter)
  group: ''
- name: Elbow internal diameter
  summary: Pipe internal diameter 0.01 m (default) | positive scalar
  group: ''
- name: Elbow angle
  summary: Pipe curve angle 90 deg (default) | positive scalar
  group: ''
- name: Laminar flow pressure ratio
  summary: Pressure ratio at which flow transitions between laminar and turbulent regimes 0.999 (default) | positive scalar
  group: ''
```

### **Elbow type** — Bend geometry `Smoothly curved` (default) | `Sharp-edged (Miter)`

Bend specification of the pipe segment. When you set this parameter to
`Sharp-edged (Miter)`, the block introduces a
sharp change in flow direction, such as at a pipe joint, and models the flow
losses using a separate set of empirical data from gradually turning pipe
segments.

### **Elbow internal diameter** — Pipe internal diameter `0.01 m` (default) | positive scalar

Internal diameter of the pipe elbow segment.

### **Elbow angle** — Pipe curve angle `90 deg` (default) | positive scalar

Angle of the swept pipe curve.

### **Laminar flow pressure ratio** — Pressure ratio at which flow transitions between laminar and turbulent regimes `0.999` (default) | positive scalar

Pressure ratio at which the moist air flow transitions between the laminar
and turbulent regimes.
## Libraries

Simscape / Fluids / Moist Air / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To
model water droplets, select **Enable entrained water droplets** in the
Moist Air Properties
(MA) block connected to your moist air network.

## Description

Pipe turn in an moist air network

The Elbow (MA) block models flow in a pipe turn in a moist air network. The block
calculates pressure losses due to pipe turns, but omits the effect of viscous friction.
The block models losses with hydraulic loss coefficients and the results may be more
accurate for lower speed flows where you can neglect compressible flow effects.

You can model a smoothly curved or sharp-edged pipe elbow by setting the
**Elbow type** parameter to `Smoothly
curved` or `Sharp-edged (Miter)`,
respectively. To model a smooth pipe with a 90o bend that
models losses due to friction, you can also use the Pipe Bend
(MA) block.

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

The values provided by Crane are valid for diameters up to 600
millimeters. The friction factor for larger diameters or for wall roughness beyond
this range is calculated by nearest-neighbor extrapolation.

When the **Elbow type** parameter is `Sharp-edged
(Miter)`, the block calculates the loss coefficient
*K* for the bend angle, *α*, according to
Crane [1].

| *α* | 0° | 15° | 30° | 45° | 60° | 75° | 90° |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 2 *fT* | 4 *fT* | 8 *fT* | 15 *fT* | 25 *fT* | 40 *fT* | 60 *fT* |

Diagram displaying Mitre bends and a table for K values and corresponding bend angles.

### Mass Flow Rate

The block conserves mass through the pipe segment

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

where the subscript *w* denotes water vapor, the
subscript *g* denotes trace gas, and the subscript
*d* denotes water droplets.

The mass flow rate through the elbow is

m˙=A2ρ¯KΔp[Δp2+Δpcrit2]1/4,

where:

- *A* is the flow area.
- ρ¯ is the average fluid density.
- *Δp* is the pipe segment pressure difference,
  *pA* –
  *pB*.

The critical pressure difference,
*Δpthreshold*, is the threshold for
transition between laminar and turbulent flow

Δpthreshold=pA+pb2(1−Blam),

where:

- *pA* is the pressure at port
  **A**.
- *pB* is the pressure at port
  **B**.
- *Blam* is the value of the
  **Laminar flow pressure ratio** parameter.

### Energy Balance

The block balances energy such that

ΦA+ΦB=0,

where:

- *ϕA* is the energy flow rate
  at port **A**.
- *ϕB* is the energy flow rate
  at port **B**.
