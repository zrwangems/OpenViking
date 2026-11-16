---
type: simulink-block
title: 'Pipe Bend (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Pipes & Fittings'
documentation_page: 'pipebendg'
documentation_source_path: 'ref/pipebendg.html'
language: en
---

# Pipe Bend (G)

## Ports

### Conserving

### **A** — Liquid port gas

Gas conserving port associated with the liquid entry or exit port

### **B** — Liquid port gas

Gas conserving port associated with the liquid entry or exit port

## Parameters

### **Pipe diameter** — Pipe diameter `0.01 m` (default) | positive scalar

Diameter of the pipe.

### **Bend radius** — Bend circle radius `0.04 m` (default) | positive scalar

Radius of the circle formed by the pipe bend.

### **Bend angle** — Bend angle `90 deg` (default) | positive scalar

Swept degree of the pipe bend.

### **Internal surface absolute roughness** — Pipe wall roughness `15e-6 m` (default) | positive scalar

Pipe wall absolute roughness. The block uses this parameter to determine the Darcy
friction factor, which contributes to pressure loss in the pipe.

### **Enable dynamic compressibility** — Option to model pressure dynamics in the gas channel `On` (default) | `Off`

Option to model the pressure dynamics in the gas channel. If you clear this
checkbox, the block removes the pressure derivative terms from the component energy and
mass conservation equations.

### **Nominal temperature** — Temperature at nominal operating conditions `293.15 K` (default) | scalar

Gas temperature at nominal operating conditions. The block uses this value to
calculate the nominal density to use in the mass and energy conservation equation when
dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Nominal pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Gas pressure at nominal operating conditions. The block uses this value to calculate
the nominal density to use in the mass and energy conservation equation when dynamic
compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** checkbox.

### **Initial pressure** — Pressure at the start of simulation `0.101325 MPa` (default) | scalar

Pressure in the gas channel at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Initial pressure priority** — Pressure parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial pressure** parameter
when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

#### Dependencies

To enable this parameter, select **Enable dynamic
compressibility**.

### **Initial temperature** — Temperature at the start of simulation `293.15 K` (default) | scalar

Temperature in the gas channel at the start of simulation.

### **Initial temperature priority** — Temperature parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial temperature**
parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

## Libraries

Simscape / Fluids / Gas / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2025a: Optionally model dynamic compressibility

The Pipe Bend (G) block can now optionally model dynamic compressibility by using the **Enable dynamic compressibility** parameter. Previously, this block always modeled pressure dynamics, which can cause models to take longer to achieve steady state. Clear the **Enable dynamic compressibility** parameter to prevent dynamic compressibility modeling.

## Description

Pipe bend segment in a gas network

The Pipe Bend (G) block represents a curved pipe in a gas network. You can define the pipe
characteristics to calculate losses due to friction and pipe curvature. The block models
losses with hydraulic loss coefficients and the results may be more accurate for lower speed
flows where you can neglect compressible flow effects.

### Pipe Curvature Loss Coefficient

The coefficient for pressure losses due to geometry changes comprises an angle
correction factor, *C*angle, and a bend coefficient,
*C*bend:

Kloss=CangleCbend.

The block calculates *Cangle* as:

Cangle=0.0148θ−3.9716⋅10−5θ2,

where *θ* is the value of the **Bend
angle** parameter, in degrees.

The block calculates *Cbend* from the tabulated
ratio of the bend radius, *r*, to the pipe diameter, *d*,
for 90° bends from data based on Crane [1]:

Diagram displaying 90° pipe bend

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

The block interpolates the friction factor,
*f*T, for clean commercial steel from tabular data
based on the pipe diameter [1]. This table contains the pipe friction data for clean
commercial steel pipe with flow in the zone of complete turbulence.

| Nominal size (mm) | 5 | 10 | 15 | 20 | 25 | 32 | 40 | 50 | 72.5 | 100 | 125 | 150 | 225 | 350 | 609.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Friction factor, *fT* | .035 | .029 | .027 | .025 | .023 | .022 | .021 | .019 | .018 | .017 | .016 | .015 | .014 | .013 | .012 |

The correction factor is valid for a ratio of bend radius to diameter
between 1 and 24. Beyond this range, the block employs nearest-neighbor
extrapolation.

### Losses Due to Friction in Laminar Flows

The pressure loss formulations are the same for the flow at ports **A**
and **B**.

When the flow in the pipe is fully laminar, or below *Re* = 2000, the
pressure loss over the bend is

Δploss=μλ2ρId2AL2m˙port,

where:

- *μ* is the relative humidity.
- *λ* is the Darcy friction factor constant, which is 64 for
  laminar flow.
- *ρI* is the internal fluid density.
- *d* is the pipe diameter.
- *L* is the bend length segment, which is the product of the
  **Bend radius** and the **Bend angle** parameters: Lbend=rbendθ.
- *A* is the pipe cross-sectional area, π4d2.
- m˙port is the mass flow rate at the respective port.

### Losses due to Friction in Turbulent Flows

When the flow is fully turbulent, or greater than *Re* = 4000, the
pressure loss in the pipe is:

Δploss=(fDL2d+Kloss2)m˙port|m˙port|2ρIA2,

where *f*D is the Darcy friction
factor. The block approximates this value by using the empirical Haaland equation and the
**Internal surface absolute roughness** parameter. The block takes the
differential over each half of the pipe segment, between port **A** to an
internal node, and between the internal node and port **B**.

### Pressure Differential

The block calculates the pressure loss over the bend based on the internal fluid volume
pressure, *pI* :

pA−pI=Δploss,A

pB−pI=Δploss,B

### Mass Balance

Mass conservation relates the mass flow rates to the dynamics of the pressure and
temperature of the internal node representing the gas volume. When you select
**Enable dynamic compressibility**, the mass balance is

∂M∂pdpIdt+∂M∂TdTIdt=m˙A+m˙B,

where:

- ∂M∂p is the partial derivative of the mass of the gas volume with respect
  to pressure at constant temperature and volume.
- ∂M∂T is the partial derivative of the mass of the gas volume with respect
  to temperature at constant pressure and volume.
- *pI* is the pressure of the gas volume.
- *TI* is the temperature of the gas volume.
- *t* is time.
- m˙A and m˙B are the mass flow rates at ports
  **A** and **B**, respectively. The flow rate at a
  port is positive when gas flows into the block through that port.

When you clear the **Enable dynamic compressibility** checkbox, the mass
flow into the pipe equals the mass flow out of the pipe

m˙A+m˙B=0.

### Energy Balance

Energy conservation relates the energy and heat flow rates to the dynamics of the
pressure and temperature of the internal node that represents the gas volume. When you
select **Enable dynamic compressibility**, the energy balance is

∂U∂pdpIdt+∂U∂TdTIdt=ΦA+ΦB,

where:

- ∂U∂p is the partial derivative of the internal energy of the gas volume
  with respect to pressure at constant temperature and volume.
- ∂U∂T is the partial derivative of the internal energy of the gas volume
  with respect to temperature at constant pressure and volume.
- *ΦA* and
  *ΦB* are the energy flow rates at ports
  **A** and **B**, respectively.

When you clear the **Enable dynamic compressibility** check box, the
energy balance is

ρ0cpVdTdt=ΦA+ΦB,

where:

- *cp* is the gas specific heat.
- *V* is the pipe volume.
- *ρ0* is the gas density. The block
  calculates this constant value from the **Nominal liquid
  temperature** and **Nominal liquid pressure**
  parameters.
