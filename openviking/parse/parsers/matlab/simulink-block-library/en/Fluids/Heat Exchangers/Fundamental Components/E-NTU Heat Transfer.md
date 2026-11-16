---
type: simulink-block
title: 'E-NTU Heat Transfer'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'entuheattransfer'
documentation_source_path: 'ref/entuheattransfer.html'
language: en
---

# E-NTU Heat Transfer

## Ports

### Input

### **C1** — Fluid 1 thermal capacity physical signal

Physical signal input port for the thermal capacity rate of fluid 1.
The thermal capacity rate is the mass flow rate multiplied by the
specific heat coefficient for the fluid.

### **C2** — Fluid 2 thermal capacity physical signal

Physical signal input port for the thermal capacity rate of fluid 2.
The thermal capacity rate is the mass flow rate multiplied by the
specific heat coefficient for the fluid.

### **HC1** — Fluid 1 heat transfer coefficient physical signal

Physical signal input port for the heat transfer coefficient between
fluid 1 and the interface wall.

### **HC2** — Fluid 2 heat transfer coefficient physical signal

Physical signal input port for the heat transfer coefficient between
fluid 2 and the interface wall.
### Conserving

### **H1** — Fluid 1 thermal inlet temperature thermal

Thermal conserving port associated with the inlet temperature of fluid
1.

### **H2** — Fluid 2 thermal inlet temperature thermal

Thermal conserving port associated with the inlet temperature of
fluid.

## Parameters

### **Flow arrangement** — Manner in which the flows align in the heat exchanger `Parallel or counter flow` (default) | `Shell and tube` | `Cross flow` | `Generic — effectiveness table`

Heat exchanger geometry. Select `Generic —
effectiveness table` to model other heat exchanger
geometries based on tabular effectiveness data.

In the `Parallel or counter flow` configuration,
the relative flow directions of fluids 1 and 2 determine whether the heat
exchanger is based on parallel or counter flows. The flow directions depend
on the remainder of the Simscape
Fluids™ model.

### **Wall thermal resistance** — Resistance of the wall to heat flow by thermal conduction `0 K/W` (default) | positive scalar

Thermal resistance of the interface wall separating the two heat exchanger
fluids.

### **Number of shell passes** — Number of times the flow traverses the shell before exiting `1` (default) | positive scalar

Number of times the flow traverses the shell before exiting.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Shell and tube`.

### **Cross flow type** — Mixing condition in each of the flow channels `Both fluids mixed` (default) | `Both fluids unmixed` | `Controlled Fluid 1 mixed & Controlled Fluid 2 unmixed` | `Controlled Fluid 1 unmixed & Controlled Fluid 2 mixed`

Fluid mixing configuration. The fluids can be mixed or unmixed. The block
uses the mixing configuration to determine which empirical heat transfer
correlations to use. Mixed flow means that the fluid is free to move in the
transverse direction as it travels along the flow path. Unmixed flow means
that the fluid is restricted to travel only along the flow path. For
example, a side with fins is considered an unmixed flow.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Cross flow`.

### **Number of heat transfer units vector, NTU** — Number of transfer units at each breakpoint in lookup table for heat exchanger effectiveness `[.5, 1, 2, 3, 4, 5]` (default) | vector of positive scalars

*M*-element vector of NTU values at which to specify the
effectiveness tabular data. The number of transfer units (NTU) is a
dimensionless parameter defined as

NTU=AsUCmin,

where:

- *A*S is the heat
  transfer surface area.
- *U* is the overall heat transfer
  coefficient.
- *C*min is the smallest
  of the thermal capacity rates for the hot and cold
  fluids.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Generic — effectiveness
table`.

### **Thermal capacity ratio vector, CR** — Thermal capacity ratio at each breakpoint in lookup table for heat exchanger effectiveness `[0, .25, .5, .75, 1]` (default) | vector of positive scalars

*N*-element vector of thermal capacity ratios at which to
specify the effectiveness tabular data. The thermal capacity ratio is the fraction

Cr=CminCmax,

where *C*min and
*C*max are the minimum and
maximum thermal capacity rates.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Generic — effectiveness
table`.

### **Effectiveness table, E(NTU,CR)** — Heat exchanger effectiveness at each breakpoint in lookup table over the number of transfer units and thermal capacity ratio `[.3, .3, .3, .3, .3; .6, .55, .5, .47, .43; .85, .76, .68, .61, .55; .94, .83, .72, .65, .58; .98, .86, .75, .66, .58; .99, .86, .75, .66, .58]` (default) | table of positive scalars

*M*-by-*N* matrix with the heat
exchanger effectiveness values. The matrix rows correspond to the different
values specified in the **Number of heat transfer units vector,
NTU** parameter. The matrix columns correspond to the values
specified in the **Thermal capacity ratio vector, CR**
parameter.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Generic — effectiveness
table`.

### **Enable wall thermal mass** — Option to model wall thermal mass `off` (default) | `on`

Whether to model the heat exchanger wall thermal mass. Modeling the wall thermal
mass introduces a delay in the transient response of the wall to changes in
temperature or heat flux. If you clear **Enable wall thermal
mass**, the block assumes that the wall is thin enough for the transient
response to be instantaneous on the time scale of the heat transfer.

### **Wall mass** — Heat exchanger wall mass `1 kg` (default) | positive scalar

Mass of the heat exchanger wall. The block uses this value to calculate the wall thermal mass.

#### Dependencies

To enable this parameter, select **Enable wall thermal mass**.

### **Wall specific heat** — Heat exchanger wall specific heat `490 J/(K*kg)` (default) | positive scalar

Specific heat of the heat exchanger wall. The block uses this value to calculate the wall thermal mass.

#### Dependencies

To enable this parameter, select **Enable wall thermal mass**.

### Controlled Fluid 1

### **Heat transfer surface area** — Aggregate heat transfer surface area on the controlled fluid 1 side `0.01 m^2` (default) | positive scalar

Aggregate surface area on fluid 1 side for heat transfer between the
cold and hot fluids.

### **Fouling factor** — Measure of thermal resistance due to fouling deposits `1e-4 K*m^2/W` (default) | positive scalar

Empirical parameter used to quantify the increased thermal resistance
due to dirt deposits on the heat transfer surface.

### **Minimum fluid-wall heat transfer coefficient** — Lower bound for the heat transfer coefficient `1 W/(m^2 * K)` (default) | positive scalar

Smallest allowed value of the heat transfer coefficient. The heat
transfer coefficient specified through physical signal ports HC1
saturates at this value. The block uses the heat transfer coefficient to
calculate the heat transfer rate between fluids 1 and 2 as described in
Heat Transfer Rate.

### Controlled Fluid 2

### **Heat transfer surface area** — Aggregate heat transfer surface area on the controlled fluid 2 side `0.01 m^2` (default) | positive scalar

Aggregate surface area on fluid 2 side for heat transfer between the
cold and hot fluids.

### **Fouling factor** — Measure of thermal resistance due to fouling deposits `1e-4 K*m^2/W` (default) | positive scalar

Empirical parameter used to quantify the increased thermal resistance
due to dirt deposits on the heat transfer surface.

### **Minimum fluid-wall heat transfer coefficient** — Lower bound for the heat transfer coefficient `1 W/(m^2 * K)` (default) | positive scalar

Smallest allowed value of the heat transfer coefficient. The heat
transfer coefficient specified through physical signal ports HC2
saturates at this value. The block uses the heat transfer coefficient to
calculate the heat transfer rate between fluids 1 and 2 as described in
Heat Transfer Rate.

## Libraries

Simscape / Fluids / Heat Exchangers / Fundamental Components

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2025a: Model thermal mass of heat exchanger wall

Select **Wall thermal dynamics** to model the thermal mass of the
heat exchanger wall.

## Description

Detailed heat transfer model between two general fluids

The E-NTU Heat Transfer block models the heat exchange between two
general fluids based on the standard Effectiveness-NTU method. The fluid thermal
properties are specified explicitly through Simscape™ physical signals. Combine with the Heat Exchanger Interface (TL) or Heat Exchanger Interface
(G) blocks to model the pressure drop and temperature change between
the inlet and outlet of a heat exchanger.

The block dialog box provides a choice of common heat exchanger
configurations. These include concentric-pipe with parallel and counter
flows, shell-and-tube with one or more shell passes, and cross-flow
with mixed and unmixed flows. A generic configuration lets you model
other heat exchangers based on tabular effectiveness data.

**Heat Exchanger Configurations**

### Heat Transfer Rate

The E-NTU model defines the heat transfer rate between fluids 1 and 2 in terms of
an effectiveness parameter *ε*

Q=ϵQMax,0<ε<1,

where:

- *Q* is the net heat transfer rate.
- *Q*Max is the maximum possible
  heat transfer rate between fluid 1 and fluid 2 at a given set of
  operating conditions.
- *ε* is the effectiveness parameter.

If you clear the **Enable wall thermal mass** checkbox,

−Q1=Q2=Q,

where *Q*1 and
*Q*2 are the heat transfer rates into
fluid 1 and fluid 2.

The maximum possible heat transfer rate between the two fluids is

QMax=CMin(T1,In−T2,In),

where:

- *C*Min is the minimum value of
  the thermal capacity rate:

  CMin=min(m˙1cp,1,m˙2cp,2)
- *T*1,In and
  *T*2,In are the inlet
  temperatures of fluid 1 and fluid 2.
- m˙1 and m˙2 are the mass flow rates of fluid 1 and fluid 2 into
  the heat exchanger volume through the inlet.
- *c*p,1 and
  *c*p,2 are the specific heat
  coefficients at constant pressure of fluid 1 and fluid 2. The
  **Minimum fluid-wall heat transfer coefficient**
  parameter in the block dialog box sets a lower bound on the allowed
  values of the heat transfer coefficients.

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

### Heat Exchanger Effectiveness

The heat exchanger effectiveness calculations depend on the flow arrangement type
selected in the block dialog box. For all but `Generic —
effectiveness table`, the block computes the thermal exchange
effectiveness through analytical expressions written in terms of the number of
transfer units (NTU) and thermal capacity ratio. The number of transfer units is
defined as

NTU=UOverallAHeatCMin=1CMinROverall,

where:

- *NTU* is the number of transfer units.
- *U*Overall is the overall heat
  transfer coefficient between fluid 1 and fluid 2.
- *R*Overall is the overall
  thermal resistance between fluid 1 and fluid 2.
- *A*Heat is aggregate area of
  the primary and secondary, or finned, heat transfer surfaces.

The thermal capacity ratio is defined as

Crel=CMinCMax

where:

- *C*rel is the thermal capacity
  ratio.

The overall heat transfer coefficient and thermal resistance used in the NTU
calculation are functions of the heat transfer mechanisms at work. These mechanisms
include convective heat transfer between the fluids and the heat exchanger interface
and conduction through the interface wall [2]:

ROverall=1UOverallAHeat=1U1A1+RFoul,1+RWall+RFoul,2+1U2A2,

where:

- *U*1 and
  *U*2 are the heat transfer
  coefficients between fluid 1 and the interface wall and between fluid 2
  and the interface wall.
- *A*1 and
  *A*2 are the heat transfer
  surface areas on the fluid-1 and fluid-2 sides.
- *R*Foul,1 and
  *R*Foul,2 are the fouling
  resistances on the fluid-1 and fluid-2 sides. The fouling resistance is
  equal to the fouling factor parameter divided by the heat transfer
  surface area.
- *R*Wall is the interface wall
  thermal resistance.

**Heat Transfer From Fluid 1 to Fluid 2**

The tables show some of the analytical expressions used to compute the heat
exchange effectiveness [1].
The parameter *N* refers to the number of shell passes and the
parameter *ε*1 to the effectiveness for a
single shell pass.

|  |  |
| --- | --- |
| **Concentric Tubes** | |
| Counter Flow | ε={1−exp[−NTU(1−Crel)]1−Crelexp[−NTU(1−Crel)],if Crel<1NTU1+NTU,if Crel=1 |
| Parallel Flow | ε=1−exp[−NTU(1+Crel)]1+Crel |
| **Shell and Tube** | |
| One shell pass and two, four, or six tube passes | ε1=21+Crel+1+Crel21+exp(−NTU1+Crel2)1−exp(−NTU1+Crel2) |
| *N* Shell Passes and 2*N*, 4*N*, or 6*N* Tube Passes | ε=[(1−ε1Crel)/(1−ε1)]N−1[(1−ε1Crel)/(1−ε1)]N−Crel |
| **Cross Flow (Single Pass)** | |
| Both Fluids Unmixed | ε=1−exp(exp(−CrelNTU0.78)−1CrelNTU−0.22) |
| Both Fluids Mixed | ε=111−exp(−NTU)+Crel1−exp(−CrelNTU)−1NTU |
| *C*Max mixed, *C*Min unmixed | ε=1Crel(1−exp(−Crel(1−exp(−NTU)))) |
| *C*Max unmixed, *C*Min mixed | ε=1−exp(−1Crel(1−exp(−CrelNTU))) |

### Wall Thermal Mass

If you select **Enable wall thermal mass**, the block models the heat
exchanger wall thermal mass, which introduces a delay in the wall's transient response to
changes in temperature or heat flux. If you model thermal mass, the wall stores heat in its
bounds. This heat storage slows the transition between steady states so that a thermal
perturbation on one side does not immediately manifest on the other side. The lag persists
until the heat flow rates from the two sides balance.

If you select **Enable wall thermal mass**, the wall energy conservation is

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

where:

- *Mwall* is the value of the **Wall
  mass** parameter.
- *cp,wall* is the value of the
  **Wall specific heat** parameter.
- *Twall* is the effective wall temperature
  on each side. The block uses this value to model the transient response. You cannot
  measure this value.

The heat transfer to each fluid is

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

where:

- *Tin* is the fluid inlet temperature on each side.
- *C* is the heat capacity rate for each fluid.

The number of heat transfer units between the fluid and the wall on each side is

NTU1=U1A1C1NTU2=U2A2C2

where *A* is the wall surface area and *U* is the heat transfer coefficient.
