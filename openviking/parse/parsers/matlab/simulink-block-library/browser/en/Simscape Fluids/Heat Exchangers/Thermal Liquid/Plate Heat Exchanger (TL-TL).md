---
type: simulink-block
title: 'Plate Heat Exchanger (TL-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'plateheatexchangertltl'
documentation_source_path: 'ref/plateheatexchangertltl.html'
language: en
---

# Plate Heat Exchanger (TL-TL)

## Ports

### Conserving

### **A1** — Thermal liquid 1 inlet or outlet thermal liquid

Inlet or outlet port associated with thermal liquid 1.

### **B1** — Thermal liquid 1 inlet or outlet thermal liquid

Inlet or outlet port associated with thermal liquid 1.

### **A2** — Thermal liquid 2 inlet or outlet thermal liquid

Inlet or outlet port associated with thermal liquid 2.

### **B2** — Thermal liquid 2 inlet or outlet thermal liquid

Inlet or outlet port associated with thermal liquid 2.

## Parameters

### Configuration

### **Flow arrangement** — Flow path alignment `Counter flow` (default) | `Parallel flow`

Flow path alignment across the heat exchanger. The available flow
arrangements are:

- `Parallel flow` — The flows run
  in the same direction.
- `Counter flow` — The flows run
  parallel to each other, in the opposite directions.

  The e-NTU calculations are based on the value of this
  parameter, regardless of the actual flow direction between
  ports **A1** and **B1**
  and between ports **A2** and
  **B2** during simulation.

### **Number of plates** — Number of plates in heat exchanger `25` (default) | positive scalar

Number of plates in the heat exchanger. Fluid flows across both sides of each plate,
including the end plate and start plate.

### **Plate length** — Length of plates `1` `m` (default) | positive scalar

Length of each plate. This value is the longer side of the plate and the flow axis of
the fluid.

### **Plate width** — Width of plates `0.5` `m` (default) | positive scalar

Width of each plate.

### **Spacing between plates** — Space between plates `5e-3` `m` (default) | positive scalar

Gap between each plate. This parameter value usually equals the
corrugation depth.

### **Corrugation pattern specification** — Option for specifying corrugation pattern `Surface area enlargement factor` (default) | `Chevron geometry`

Whether you specify the surface area enlargement factor directly or
the block calculates the enlargement factor from a specified chevron
geometry.

### **Surface area enlargement factor** — Multiplier that accounts for increased plate area `1.17` (default) | positive scalar

Multiplier that accounts for the increase in plate surface area due to corrugation. If
each plate is perfectly flat, the value of this parameter is 1.
Otherwise, this value is the ratio of the actual total surface area to
the area of the two-dimensional projection of the plate shape.

#### Dependencies

To enable this parameter, set **Corrugation pattern
specification** to `Surface area
enlargement factor`.

### **Corrugation chevron angle** — Angle of chevron on plate `60` `deg` (default) | positive scalar

Angle of the chevron corrugation on each plate. This value is
*β* in this plate diagram:

#### Dependencies

To enable this parameter, set **Corrugation pattern
specification** to `Chevron
geometry`.

### **Corrugation depth to pitch ratio** — Ratio of chevron depth to pitch `0.28` (default) | positive scalar

Ratio of the chevron corrugation depth to the corrugation pitch. The
corrugation pitch is the corrugation wavelength. The value of this
parameter is *b/λ* in this diagram:

#### Dependencies

To enable this parameter, set **Corrugation pattern
specification** to `Chevron
geometry`.

### **Enable plate thermal resistance** — Option to model plate thermal resistance `off` (default) | on

Option to model plate thermal resistance. If you select this check
box, the block uses the values of the **Plate
thickness** and **Plate thermal
conductivity** parameters to calculate the thermal
resistance through each plate. If you clear this check box, the block
does not model the effects of thermal resistance through the
plates.

### **Enable plate thermal mass** — Option to model plate thermal mass `off` (default) | `on`

Whether to model the plate thermal mass. Modeling the plate thermal
mass introduces a delay in the transient response of the plate to
changes in temperature or heat flux. If you clear **Enable plate
thermal mass**, the block assumes that the plate is thin
enough for the transient response to be instantaneous on the time scale
of the heat transfer.

### **Plate thickness** — Thickness of plates `5e-4` `m` (default) | positive scalar

Thickness of each plate in the heat exchanger.

#### Dependencies

To enable this parameter, select **Enable plate thermal resistance**
or **Enable plate thermal mass**.

### **Plate density** — Density of plate `7800 kg/m^3` (default) | positive scalar

Density of the plate. The block uses this value to calculate the plate
thermal mass.

#### Dependencies

To enable this parameter, select **Enable plate thermal mass**.

### **Plate specific heat** — Specific heat of plate `490 J/(K*kg)` (default) | positive scalar

Specific heat of the plate. The block uses this value to calculate the
plate thermal mass.

#### Dependencies

To enable this parameter, select **Enable plate thermal mass**.

### **Plate thermal conductivity** — Thermal conductivity through plate `15` `W/(K*m)` (default) | positive scalar

Thermal conductivity of each plate.

#### Dependencies

To enable this parameter, select **Enable plate thermal
resistance**.

### **Cross-sectional area at port A1** — Flow area at port A1 `0.01 m^2` (default) | positive scalar

Flow area at the thermal liquid 1 port **A1**.

### **Cross-sectional area at port B1** — Flow area at port B1 `0.01 m^2` (default) | positive scalar

Flow area at the thermal liquid 1 port **B1**.

### **Cross-sectional area at port A2** — Flow area at port A2 `0.01` m^2 (default) | positive scalar

Flow area at the thermal liquid 2 port **A2**.

### **Cross-sectional area at port B2** — Flow area at port B2 `0.01` m^2 (default) | positive scalar

Flow area at the thermal liquid 2 port **B2**.

### Thermal Liquid 1

### **Pressure loss model** — Method of pressure loss calculation from viscous friction `Correlation for flow between corrugated plates` (default) | `Friction factor`

Method of pressure loss calculation due to viscous friction for
thermal liquid 1. The settings are:

- `Friction factor` — The block
  calculates the pressure loss based on a constant Darcy
  friction factor for flow between the plate passages,
  specified by the **Darcy friction factor for flow
  between corrugated plates** parameter.
- `Correlation for flow between corrugated
  plates` — The block uses the Martin
  correlation for plate heat exchangers with the chevron or
  herringbone pattern to calculate the pressure loss.

### **Darcy friction factor for flow between corrugated plates** — Constant Darcy friction factor `1.7` (default) | positive scalar

Constant Darcy friction factor to use to calculate the pressure
loss.

If you have data for the pressure loss across the heat exchanger,
*Δpdata*, and the mass
flow rate through the heat exchanger,
*ṁdata*, the value of
this parameter is

fdarcy=DhS2Lp[2ρ(Δpdatam˙data2)−ξportsSport].

If you do not have data for
*ξports*, use the
default value of the **Loss coefficient for inlet and outlet
manifolds and ports** parameter in this expression. If you
have multiple data points for
*Δpdata* and
*ṁdata*, use a least
squares fit to find
*fdarcy*.

If you know the loss coefficient value,
*ξloss*, for your heat
exchanger, then *fDarcy =
ξloss Dh /
LP*.

#### Dependencies

To enable this parameter, set **Pressure loss
model** to `Friction
factor`.

### **Loss coefficient for inlet and outlet manifolds and ports** — Pressure loss coefficient for inlet and outlet manifolds and ports `1.5` (default) | positive scalar

Pressure loss coefficient that accounts for losses at the inlet and
outlet manifolds and ports on the thermal liquid 1 side.

### **Heat transfer coefficient model** — Method of calculating heat transfer coefficient `Correlation for flow between corrugated plates` (default) | `Colburn equation`

Method of calculating the heat transfer coefficient for thermal liquid
1. The available settings are:

- `Colburn equation` — Use this
  setting to calculate the heat transfer coefficient by
  defining the variables *a*,
  *b*, and *c* of
  the Colburn equation. Use this option to fit the heat
  transfer results to the experimental data by estimating the
  coefficients.
- `Correlation for flow between corrugated
  plates` — Use this setting to calculate the
  heat transfer coefficient based on the plate geometry data
  and the Martin correlation.

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c** — Colburn equation coefficients `[.141, .748, .333]` (default) | three-element vector

Three-element vector that contains the empirical coefficients of the Colburn equation
for the thermal liquid 1. The Colburn equation is a formulation for
calculating the Nusselt number.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Colburn
equation`.

### **Coefficients for Martin correlation** — Martin correlation coefficients `[.122, .374, .333]` (default) | three-element vector

Three-element vector that contains the coefficients
*c1*,
*c2*, and
*c3* that the block uses
to calculate the Nusselt number by using the Martin correlation for the
thermal liquid 1:

Nu=c1(fDarcyRe2sin2β)c2Prc3.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Correlation for flow between
corrugated plates`.

### **Fouling factor** — Thermal resistance from fouling deposits `0.1` `K*m^2/kW` (default) | positive scalar

Additional thermal resistance due to fouling layers on the surfaces of
the wall for the thermal liquid 1. In real systems, fouling deposits
grow over time. However, the growth is slow enough that the block
assumes the fouling is constant during the simulation.

### **Initial thermal liquid 1 pressure** — Thermal liquid pressure at start of simulation `0.101325` `MPa` (default) | positive scalar

Thermal liquid 1 pressure at the start of the simulation.

### **Initial thermal liquid 1 temperature** — Thermal liquid temperature at start of simulation `293.15` `K` (default) | positive scalar

Temperature in the thermal liquid 1 at the start of the simulation. This parameter can
be a scalar or a two-element vector. A scalar value represents the mean
initial temperature in the fluid flow. A vector value represents the
initial temperature at the inlet and outlet in the form
[`inlet`, `outlet`]. The block
calculates a linear gradient between the two ports. The initial flow
direction determines the inlet and outlet ports.

### Thermal Liquid 2

### **Pressure loss model** — Method of pressure loss calculation from viscous friction `Correlation for flow between corrugated plates` (default) | `Friction factor`

Method of pressure loss calculation due to viscous friction for
thermal liquid 2. The settings are:

- `Friction factor` — The block
  calculates the pressure loss based on a constant Darcy
  friction factor for flow between the plate passages,
  specified by the **Darcy friction factor for flow
  between corrugated plates** parameter.
- `Correlation for flow between corrugated
  plates` — The block uses the Martin
  correlation for plate heat exchangers with the chevron or
  herringbone pattern to calculate the pressure loss.

### **Darcy friction factor for flow between corrugated plates** — Constant Darcy friction factor `1.7` (default) | positive scalar

Constant Darcy friction factor to use to calculate the pressure
loss.

If you have data for the pressure loss across the heat exchanger,
*Δpdata*, and the mass
flow rate through the heat exchanger,
*ṁdata*, the value of
this parameter is

fdarcy=DhS2Lp[2ρ(Δpdatam˙data2)−ξportsSport].

If you do not have data for
*ξports*, use the
default value of the **Loss coefficient for inlet and outlet
manifolds and ports** parameter in this expression. If you
have multiple data points for
*Δpdata* and
*ṁdata*, use a least
squares fit to find
*fdarcy*.

If you know the loss coefficient value,
*ξloss*, for your heat
exchanger, then *fDarcy =
ξloss Dh /
LP*.

#### Dependencies

To enable this parameter, set **Pressure loss
model** to `Friction
factor`.

### **Loss coefficient for inlet and outlet manifolds and ports** — Pressure loss coefficient for inlet and outlet manifolds and ports `1.5` (default) | positive scalar

Pressure loss coefficient that accounts for losses at the inlet and
outlet manifolds and ports on the thermal liquid 2 side.

### **Heat transfer coefficient model** — Method of calculating heat transfer coefficient `Correlation for flow between corrugated plates` (default) | `Colburn equation`

Method of calculating the heat transfer coefficient for thermal liquid
2. The available settings are:

- `Colburn equation` — Use this
  setting to calculate the heat transfer coefficient by
  defining the variables *a*,
  *b*, and *c* of
  the Colburn equation. Use this option to fit the heat
  transfer results to the experimental data by estimating the
  coefficients.
- `Correlation for flow between corrugated
  plates` — Use this setting to calculate the
  heat transfer coefficient based on the plate geometry data
  and the Martin correlation.

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c** — Colburn equation coefficients `[.141, .748, .333]` (default) | three-element vector

Three-element vector that contains the empirical coefficients of the Colburn equation
for the thermal liquid 2. The Colburn equation is a formulation for
calculating the Nusselt number.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Colburn
equation`.

### **Coefficients for Martin correlation** — Martin correlation coefficients `[.122, .374, .333]` (default) | three-element vector

Three-element vector that contains the coefficients
*c1*,
*c2*, and
*c3* that the block uses
to calculate the Nusselt number by using the Martin correlation for the
thermal liquid 2:

Nu=c1(fDarcyRe2sin2β)c2Prc3.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Correlation for flow between
corrugated plates`.

### **Fouling factor** — Thermal resistance from fouling deposits `0.1` `K*m^2/kW` (default) | positive scalar

Additional thermal resistance due to fouling layers on the surfaces of
the wall for the thermal liquid 2. In real systems, fouling deposits
grow over time. However, the growth is slow enough that the block
assumes the fouling is constant during the simulation.

### **Initial thermal liquid 2 pressure** — Thermal liquid pressure at start of simulation `0.101325` `MPa` (default) | positive scalar

Thermal liquid 2 pressure at the start of the simulation.

### **Initial thermal liquid 2 temperature** — Thermal liquid temperature at start of simulation `293.15` `K` (default) | positive scalar | two-element vector

Temperature in the thermal liquid 1 at the start of the simulation. This parameter can
be a scalar or a two-element vector. A scalar value represents the mean
initial temperature in the fluid flow. A vector value represents the
initial temperature at the inlet and outlet in the form
[`inlet`, `outlet`]. The block
calculates a linear gradient between the two ports. The initial flow
direction determines the inlet and outlet ports.

## Libraries

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

### R2025a: Model thermal mass of heat exchanger plates

Select **Plate thermal dynamics** to model the thermal mass of
the heat exchanger plates.

## Description

Plate geometry heat exchanger between two thermal liquid networks

The Plate Heat Exchanger (TL-TL) block models a plate
heat exchanger between two thermal liquid networks. The block models the heat transfer
between the two thermal liquids based on the effectiveness-NTU method. Heat transfer can
occur in either direction between the two fluids.

The block uses the Effectiveness-NTU (E-NTU) method to model heat transfer through the
shared plate walls. You can also account for heat transfer through the plate itself by
selecting the **Enable plate thermal resistance** parameter. The block
models fouling on the exchanger walls, which increases thermal resistance and reduces
the heat exchange between the two fluids.

### Plate Heat Exchanger Geometry

Plate heat exchangers consist of a series of clamped-together plates. Each plate
has portholes for the fluid to flow through and gaskets around the portholes and the
plate sides to contain the liquid. The gasket pattern alternates between the plates
so that on each side of the plate, one fluid flows across the plate while the other
fluid flows through it. This results in alternating layers of hot and cold fluid.
This figure shows a section of counter-flow in a plate heat exchanger.

This figure shows an individual plate and a cross-section of two adjacent plates.
In the individual plate image, the thick lines represent the gaskets and the dotted
lines represent the plate corrugation. The block assumes that the flow channel gap
between the plates equals the corrugation depth, *b*.

On this plate, one fluid flows from the top-right port hole across the plate to
the bottom-right port hole. The other fluid flows through the gasket on the two
left-side portholes and not touch the plate on this side. The plate corrugation
patterns increase structural stiffness, surface area, and turbulence.

Because fluid flows along both sides of each plate, the total fluid volume is

Vtotal=(Np+1)bLpWp,

where:

- *Np* is the value of the
  **Number of plates** parameter.
- *Lp* is the value of the
  **Plate length** parameter.
- *Wp* is the value of the
  **Plate width** parameter.
- *b* is the value of the **Spacing between
  plates** parameter.

The volume of each fluid is half of the total volume. The flow cross-sectional
area, *S*, for each fluid is

S=(Np+1)2bWp.

The total projected surface area of the plates, assuming no corrugation, is

Atotal,proj=2NpLpWp.

Each fluid has half of the total heat transfer surface area

ATL1=ATL2=Atotal,actual2=ϕNpLpWp,

where the area enlargement factor, *ϕ*, accounts for the
increased surface area due to the corrugation

ϕ=Atotal,actualAtotal,proj=1+1+(πbλ)2+41+(πb2λ)26.

The hydraulic diameter for each fluid is

Dh=2bϕ(Np+1Np).

### Effectiveness-NTU Heat Transfer

The convective heat transfer between the fluids is

Q=ϵCMin(TIn,TL1−TIn,TL2),

where:

- *CMin* is the lesser of the
  heat capacity rates of the two fluids. The heat capacity rate is the
  product of the fluid specific heat,
  *cp*, and the fluid mass
  flow rate. *CMin* is always
  positive.
- *TIn,TL1*
  is the zone inlet temperature of the thermal liquid 1.
- *TIn,TL2*
  is the zone inlet temperature of the thermal liquid 2.
- *ε* is the heat exchanger effectiveness.

Effectiveness is a function of the heat capacity rate and the number
of transfer units, *NTU*, and varies based on the heat exchanger
flow arrangement. *NTU* is

NTU=1CMinR,

where:

- *R* is the total thermal resistance between the two
  flows due to convection, conduction, and any fouling on the plates:

  R=1UTL1ATL1+FTL1ATL1+RW+FTL2ATL2+1UTL2ATL2,

  where:

  - *U* is the convective heat transfer
    coefficient of the respective thermal liquid.
  - *F* is the value of the **Fouling
    factor** parameter on the thermal liquid 1 or 2
    side.
  - *RW* is the
    thermal resistance through the plates. If you select
    **Enable plate thermal resistance**, RW=tNpLpWpkp, where *t* is the value of
    the **Plate thickness** parameter and
    *kp* is the
    value of the **Plate thermal conductivity**
    parameter.

    If you clear the **Enable plate thermal
    resistance** check box,
    *RW =
    0*.

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

**Effectiveness by Flow Arrangement**

The heat exchanger effectiveness varies according to the flow configuration.
The effectiveness is ε=1−exp(−NTU) for all flow arrangements.

When **Flow arrangement** is `Parallel
flow`

ϵ=1−exp[−NTU(1+CR)]1+CR.

When **Flow arrangement** is `Counter
flow`

ϵ=1−exp[−NTU(1−CR)]1−CRexp[−NTU(1−CR)].

*C*R is the ratio between the heat
capacity rates of the two fluids:

CR=CMinCMax.

### Conductive Heat Transfer

The conductive heat transfer in a zone is

Qcond=Tout,TL1−Tout,TL2Rcond,

where:

- *Tout,TL1*
  is the zone outlet temperature of the thermal liquid 1.
- *Tout,TL2*
  is the zone outlet temperature of the thermal liquid 2.
- *Rcond* is the total
  conductive thermal resistance between the two flows,

  Rcond=DhkTL1AW,TL1+FTL1AW,TL1+RW+FTL2AW,TL2+DhkTL2AW,TL2,

  where:

  - *AW* is the wall
    surface area.
  - *k* is the thermal conductivity of each
    fluid.
  - *DH* is the
    hydraulic diameter.

The total heat transfer is the sum of the convective and conductive heat transfer.
The conductive heat transfer is negligible compared to the convective heat transfer.
When the flow rate is zero, the convective heat transfer is also zero. However,
because heat transfer from convection and conduction operate independently of each
other, there is still conductive heat transfer even when the convective heat
transfer is zero.

### Pressure Loss

For both fluids and pressure loss parameterizations, the pressure loss between
each port and the internal node is

pA−pI=ξportsm˙A|m˙A|4ρSport,A2+fDarcyLpm˙A|m˙A|4ρDhS2pB−pI=ξportsm˙B|m˙B|4ρSport,B2+fDarcyLpm˙B|m˙B|4ρDhS2

where:

- *ṁA* is the mass flow rate through
  port **A1** or **A2** when the block
  calculates the values for the thermal liquid 1 and thermal liquid 2
  networks, respectively.
- *ṁB* is the mass flow rate through
  port **B1** or **B2**, when the block
  calculates the values for the thermal liquid 1 and thermal liquid 2
  networks, respectively.
- *ρ* is the fluid density.
- *ξports* is the value of the
  **Loss coefficient for inlet and outlet manifolds and
  ports** parameter.
- *Sport,A* is the value of the
  **Cross-sectional area at port A1** or
  **Cross-sectional area at port A2** parameter, when the
  block calculates the values for the thermal liquid 1 and thermal liquid 2
  networks, respectively.
- *Sport,B* is the value of the
  **Cross-sectional area at port B1** or
  **Cross-sectional area at port B2** parameter, when the
  block calculates the values for the thermal liquid 1 and thermal liquid 2
  networks, respectively.

When the **Pressure loss model** parameter is
`Friction factor`, you use the **Darcy friction
factor for flow between corrugated plates** parameter to specify a
single constant friction factor for the fluid.
*fDarcy* is the value of the
**Darcy friction factor for flow between corrugated plates**
parameter.

When the **Pressure loss model** parameter is
`Correlation for flow between corrugated plates`, the
block calculates the Darcy friction factor based on the plate geometry data and
Reynolds number from [3].

The Reynolds number is Re=m˙DhμS, where *μ* is the dynamic viscosity. When the
Reynolds number is between 200 and 1000,

fDarcy=[cosβ0.18tanβ+0.36sinβ+64Recosβ+1−cosβ3.8(597Re+3.85)]−2.

When the Reynolds number is greater than 2000,

fDarcy=[cosβ0.18tanβ+0.36sinβ+1(1.8lnRe−1.5)2cosβ+1−cosβ3.8∗39Re0.289]−2.

The block uses a smooth cubic transition between these regions and for Reynolds
numbers between 1000 and 2000. For Reynolds numbers below 200, the block calculates
*fDarcy* from a laminar friction
constant that ensures numerical robustness as the flow goes to 0.

### Heat Transfer Coefficient

The heat transfer coefficient, *U*, is

U=NukDh,

where *k* is the fluid thermal conductivity. The
heat transfer calculations depend on the value of the **Heat transfer
coefficient model** parameter.

**Colburn Equation**

When **Heat transfer coefficient model** is
`Colburn equation`, the block calculates the heat
transfer coefficient from data by using the Colburn correlation
coefficients.

The Nusselt number is

Nu=aRebPrc,

where *a*, *b*, and
*c* are the first, second, and third elements in the
**Coefficients [a, b, c] for a\*Re^b\*Pr^c** parameter and
*Pr* is the Prandtl number.

**Correlation for Flow Between Corrugated Plates**

When **Heat transfer coefficient model** is
`Correlation for flow between corrugated plates`,
the block calculates the heat transfer coefficient based on the plate geometry
data. The Nusselt number from [3] is

Nu=c1(fDarcyRe2sin2β)c2Prc3,

where:

- *c1*,
  *c2*, and
  *c3* are the first,
  second, and third elements in the **Coefficients for Martin
  correlation** parameter.
- *Pr* is the Prandtl number.

### Plate Thermal Mass

If you select **Enable plate thermal mass**, the block models the heat
exchanger plate thermal mass, which introduces a delay in the plate's transient
response to changes in temperature or heat flux. If you model thermal mass, the
plate stores heat in its bounds. This heat storage slows the transition between
steady states so that a thermal perturbation on one side does not immediately
manifest on the other side. The lag persists until the heat flow rates from the two
sides balance.

If you select **Enable plate thermal mass**, the wall energy conservation
is

(Mplatecp,plate2)dTplateTL,1dt=−QTL,1−Q(Mplatecp,plate2)dTplateTL,2dt=−QTL,2+Q

where:

- *Mplate* is the mass of the
  plates, which the block calculates from the plate geometry parameters and
  the **Plate density** parameter.
- *cp,plate* is the value of the
  **Plate specific heat** parameter.
- *Tplate* is the effective plate
  temperature. The block uses this value to model the transient response. You
  cannot measure this value.

The heat transfer to each fluid is

QTL,1=CTL,1(TplateTL,1−TinTL,1)(1−e−NTUTL,1)QTL,2=CTL,2(TplateTL,2−TinTL,2)(1−e−NTUTL,2)

where:

- *Tin* is the fluid inlet
  temperature on each side.
- *C* is the heat capacity rate for each fluid.

The number of heat transfer units between the fluid and the plate on each side is

NTUTL,1=UTL,1ATL,1CTL,1NTUTL,2=UTL,2ATL,2CTL,2

where *A* is the total plate surface area and
*U* is the heat transfer coefficient.

### Conservation Equations

The total mass accumulation rate for both thermal liquids is

dMTL1dt=m˙A1+m˙B1dMTL2dt=m˙A2+m˙B2

where m˙i is the mass flow rate of the fluid through
a port **i**.

The energy conservation equations are

MTL1duTL1dt+uTL1(m˙A1+m˙B1)=ϕA1+ϕB1−QMTL2duTL2dt+uTL2(m˙A2+m˙B2)=ϕA2+ϕB2+Q

where *ϕi* is the energy
flow rate at a port **i**.

The heat transferred to or from one thermal liquid, *Q*, equals
the heat transferred from or to the other thermal liquid.
