---
type: simulink-block
title: 'Pipe (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'pipeg'
documentation_source_path: 'ref/pipeg.html'
language: en
---

# Pipe (G)

## Ports
```yaml
ports:
- name: A
  summary: Inlet or outlet gas
  direction: conserving
- name: B
  summary: Inlet or outlet gas
  direction: conserving
- name: H
  summary: Temperature of pipe wall thermal
  direction: conserving
```

### Conserving

### **A** — Inlet or outlet gas

Gas conserving port associated with the inlet or outlet of the
pipe. This block has no intrinsic directionality.

### **B** — Inlet or outlet gas

Gas conserving port associated with the inlet or outlet of the
pipe. This block has no intrinsic directionality.

### **H** — Temperature of pipe wall thermal

Thermal conserving port associated with the temperature of the
pipe wall. This temperature may differ from the temperature of the
gas volume.
## Parameters
```yaml
parameters:
- name: Pipe length
  summary: The length of the pipe 5 m (default)
  group: Geometry
- name: Cross-sectional area
  summary: The internal area of the pipe 0.01 m^2 (default)
  group: Geometry
- name: Hydraulic diameter
  summary: Diameter of an equivalent cylindrical pipe with the same cross-sectional area 0.1 m (default)
  group: Geometry
- name: Aggregate equivalent length of local resistances
  summary: The combined length of all local resistances present in the pipe 0.1 m (default)
  group: Friction and Heat Transfer
- name: Internal surface absolute roughness
  summary: Average depth of all surface defects on the internal surface of the pipe 15e-6 m (default)
  group: Friction and Heat Transfer
- name: Laminar flow upper Reynolds number limit
  summary: The Reynolds number above which flow begins to transition from laminar to turbulent 2000 (default)
  group: Friction and Heat Transfer
- name: Turbulent flow lower Reynolds number limit
  summary: The Reynolds number below which flow begins to transition from turbulent to laminar 4000 (default)
  group: Friction and Heat Transfer
- name: Shape factor for laminar flow viscous friction
  summary: Effect of pipe geometry on the viscous friction losses 64 (default)
  group: Friction and Heat Transfer
- name: Nusselt number for laminar flow heat transfer
  summary: Ratio of convective to conductive heat transfer 3.66 (default)
  group: Friction and Heat Transfer
- name: Enable dynamic compressibility
  summary: Select whether to model gas pressure dynamics On (default) | Off
  group: Effects and Initial Conditions
- name: Enable fluid inertia
  summary: Select whether to model gas inertia Off (default) | On
  group: Effects and Initial Conditions
- name: Initial pressure
  summary: Gas pressure at the start of simulation 0.101325 MPa (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial pressure priority
  summary: Pressure parameter priority High (default) | Low | None
  group: Effects and Initial Conditions
- name: Initial temperature
  summary: Temperature at the start of simulation 293.15 K (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial temperature priority
  summary: Temperature parameter priority High (default) | Low | None
  group: Effects and Initial Conditions
- name: Nominal pressure
  summary: Nominal gas pressure 0.101325 MPa (default) | positive scalar
  group: Effects and Initial Conditions
- name: Nominal temperature
  summary: Nominal gas temperature 293.15 K (default) | positive scalar
  group: Effects and Initial Conditions
- name: Initial mass flow rate from port A to port B
  summary: Mass flow rate at time zero 0 kg/s (default) | scalar
  group: Effects and Initial Conditions
- name: Initial mass flow rate priority
  summary: Mass flow rate parameter priority High (default) | Low | None
  group: Effects and Initial Conditions
```

### Geometry

### **Pipe length** — The length of the pipe `5 m` (default)

The length of the pipe along the direction of flow.

### **Cross-sectional area** — The internal area of the pipe `0.01 m^2` (default)

The internal area of the pipe normal to the direction of the flow.

### **Hydraulic diameter** — Diameter of an equivalent cylindrical pipe with the same cross-sectional area `0.1 m` (default)

Diameter of an equivalent cylindrical pipe with the same
cross-sectional area.

### Friction and Heat Transfer

### **Aggregate equivalent length of local resistances** — The combined length of all local resistances present in the pipe `0.1 m` (default)

The combined length of all local resistances present in the pipe.
Local resistances include bends, fittings, armatures, and pipe inlets
and outlets. The effect of the local resistances is to increase the
effective length of the pipe segment. This length is added to the
geometrical pipe length only for friction calculations. The gas volume
depends only on the pipe geometrical length, defined by the
**Pipe length** parameter.

### **Internal surface absolute roughness** — Average depth of all surface defects on the internal surface of the pipe `15e-6 m` (default)

Average depth of all surface defects on the internal surface of the
pipe, which affects the pressure loss in the turbulent flow
regime.

### **Laminar flow upper Reynolds number limit** — The Reynolds number above which flow begins to transition from laminar to turbulent `2000` (default)

The Reynolds number above which flow begins to transition from laminar
to turbulent. This number equals the maximum Reynolds number
corresponding to fully developed laminar flow.

### **Turbulent flow lower Reynolds number limit** — The Reynolds number below which flow begins to transition from turbulent to laminar `4000` (default)

The Reynolds number below which flow begins to transition from
turbulent to laminar. This number equals to the minimum Reynolds number
corresponding to fully developed turbulent flow.

### **Shape factor for laminar flow viscous friction** — Effect of pipe geometry on the viscous friction losses `64` (default)

Dimensionless factor that encodes the effect of pipe cross-sectional
geometry on the viscous friction losses in the laminar flow regime.
Typical values are 64 for a circular cross section, 57 for a square
cross section, 62 for a rectangular cross section with an aspect ratio
of 2, and 96 for a thin annular cross section [1].

### **Nusselt number for laminar flow heat transfer** — Ratio of convective to conductive heat transfer `3.66` (default)

Ratio of convective to conductive heat transfer in the laminar flow
regime. Its value depends on the pipe cross-sectional geometry and pipe
wall thermal boundary conditions, such as constant temperature or
constant heat flux. Typical value is 3.66, for a circular cross section
with constant wall temperature [2].

### Effects and Initial Conditions

### **Enable dynamic compressibility** — Select whether to model gas pressure dynamics `On` (default) | `Off`

Select whether to account for the dynamic compressibility of gas.
Dynamic compressibility gives the gas density a dependence on pressure,
impacting the transient response of the system at small time scales.
Disable dynamic compressibility if you want to reach steady state
quickly during simulation or to simplify model initialization.

### **Enable fluid inertia** — Select whether to model gas inertia `Off` (default) | `On`

Select whether to account for the gas flow inertia. Flow inertia
provides resistance to changes in mass flow rate.

#### Dependencies

To enable this check box, select the **Enable dynamic
compressibility** check box.

### **Initial pressure** — Gas pressure at the start of simulation `0.101325 MPa` (default) | positive scalar

Gas pressure at the start of the simulation.

#### Dependencies

To enable this parameter, select the **Enable dynamic
compressibility** check box. If the block does not
model dynamic compressibility, it does not need a value for initial
gas pressure.

### **Initial pressure priority** — Pressure parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial
pressure** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, select the **Enable dynamic
compressibility** check box.

### **Initial temperature** — Temperature at the start of simulation `293.15 K` (default) | positive scalar

Initial gas temperature.

### **Initial temperature priority** — Temperature parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial
temperature** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

### **Nominal pressure** — Nominal gas pressure `0.101325 MPa` (default) | positive scalar

Nominal gas pressure.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** check box.

### **Nominal temperature** — Nominal gas temperature `293.15 K` (default) | positive scalar

Nominal gas temperature.

#### Dependencies

To enable this parameter, clear the **Enable dynamic
compressibility** check box.

### **Initial mass flow rate from port A to port B** — Mass flow rate at time zero `0 kg/s` (default) | scalar

Mass flow rate from port **A** to port
**B** at time zero.

#### Dependencies

To enable this parameter, select the **Enable fluid
inertia** check box.

### **Initial mass flow rate priority** — Mass flow rate parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial mass flow rate
from port A to port B** parameter when initializing the
block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, select the **Enable fluid
inertia** check box.
## Libraries

Simscape / Foundation Library / Gas / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2025a: Optional dynamic compressibility and fluid inertia modeling

Two new check boxes, **Enable dynamic compressibility** and
**Enable fluid inertia**, provide options for modeling gas
dynamic compressibility and inertia. The block parameterization options have also
changed. Instead of specifying initial targets for block variables, you now specify
initial parameter values and priorities in the **Effects and Initial
Conditions** section.

### R2024a: Numerical improvement for low-flow computation in pipes

To improve accuracy for pressure drop inside the pipe at low-speed flows, the
momentum balance computations in the Pipe (G) block
have been changed slightly. There may be slight differences in simulation results
compared to previous releases, especially when Mach number is low.

## Description

Rigid conduit for gas flow

The Pipe (G) block models pipe flow dynamics in a gas network.
The block accounts for viscous friction losses and convective heat transfer with the
pipe wall. The pipe contains a constant volume of gas. The pressure and temperature
evolve based on the compressibility and thermal capacity of this gas volume. Choking
occurs when the outlet reaches the sonic condition.

**Caution**

Gas flow through this block can choke. If a Mass Flow Rate Source
(G) block or a Controlled Mass Flow Rate Source
(G) block connected to the Pipe
(G) block specifies a greater mass flow rate than the possible
choked mass flow rate, you get a simulation error. For more information, see Choked Flow.

### Mass Balance

Mass conservation relates the mass flow rates to the dynamics of the pressure and temperature
of the internal node representing the gas volume. When you select **Enable
dynamic compressibility**, the mass balance is

∂M∂p⋅dpIdt+∂M∂T⋅dTIdt=m˙A+m˙B

where:

- ∂M∂p is
  the partial derivative of the mass of the gas volume with respect
  to pressure at constant temperature and volume.
- ∂M∂T is
  the partial derivative of the mass of the gas volume with respect
  to temperature at constant pressure and volume.
- *p*I is the
  pressure of the gas volume.
- *T*I is the
  temperature of the gas volume.
- *t* is time.
- m˙A and m˙B are
  mass flow rates at ports A and B, respectively. Flow rate associated
  with a port is positive when it flows into the block.

When you clear the **Enable dynamic compressibility** checkbox,
the mass flow into the pipe equals the mass flow out of the pipe

m˙A+m˙B=0

### Energy Balance

Energy conservation relates the energy and heat flow rates to the dynamics of the pressure and
temperature of the internal node representing the gas volume. When you select
**Enable dynamic compressibility**, the energy balance
is

∂U∂p⋅dpIdt+∂U∂T⋅dTIdt=ΦA+ΦB+QH

where:

- ∂U∂p is
  the partial derivative of the internal energy of the gas volume with
  respect to pressure at constant temperature and volume.
- ∂U∂T is
  the partial derivative of the internal energy of the gas volume with
  respect to temperature at constant pressure and volume.
- *Φ*A and
  *Φ*B are energy flow rates at
  ports **A** and **B**, respectively.
- *Q*H is heat flow rate at port
  **H**.

When you clear the **Enable dynamic compressibility** check box,
the energy balance is

ρ0⋅cp⋅V⋅dTdt=ΦA+ΦB+QH

where:

- *cp* is the gas specific
  heat.
- *V* is the pipe volume.
- *ρ0* is the gas density. The
  block calculates this constant value from the **Nominal liquid
  temperature** and **Nominal liquid
  pressure** parameters.

### Partial Derivatives for Perfect and Semiperfect Gas Models

The partial derivatives of the mass *M* and the internal energy
*U* of the gas volume, with respect to pressure and temperature at
constant volume, depend on the gas property model. For perfect and semiperfect gas models,
the equations are:

∂M∂p=VρIpI∂M∂T=−VρITI∂U∂p=V(hIZRTI−1)∂U∂T=VρI(cpI−hITI)

where:

- *ρ*I is
  the density of the gas volume.
- *V* is the volume of gas.
- *h*I is the
  specific enthalpy of the gas volume.
- *Z* is the compressibility factor.
- *R* is the specific gas constant.
- *c*pI is the
  specific heat at constant pressure of the gas volume.

### Partial Derivatives for Real Gas Model

For real gas model, the partial derivatives of the mass *M* and the internal
energy *U* of the gas volume, with respect to pressure and temperature at
constant volume, are:

∂M∂p=VρIβI∂M∂T=−VρIαI∂U∂p=V(ρIhIβI−TIαI)∂U∂T=VρI(cpI−hIαI)

where:

- *β* is the isothermal bulk
  modulus of the gas volume.
- *α* is the isobaric thermal
  expansion coefficient of the gas volume.

### Momentum Balance

The momentum balance for each half of the pipe models the pressure drop due to momentum flux
and viscous friction. If the pipe does not model fluid inertia, then the momentum
balance for each half of the pipe is

pA−pI=(m˙AS)2⋅(1ρI−1ρA)+ΔpAIpB−pI=(m˙BS)2⋅(1ρI−1ρB)+ΔpBI

where:

- *p* is the gas pressure at port **A**,
  port **B**, or internal node I, as indicated by the
  subscript.
- *ρ* is the density at port **A**, port
  **B**, or internal node I, as indicated by the
  subscript.
- *S* is the cross-sectional area of
  the pipe.
- *Δp*AI and *Δp*BI are
  pressure losses due to viscous friction.

When you select **Enable fluid inertia**, the momentum balance for
each half of the pipe has an additional inertial term

pA−pI=(m˙AS)2⋅(1ρI−1ρA)+ΔpAI+inertiaApB−pI=(m˙BS)2⋅(1ρI−1ρB)+ΔpBI+inertiaB

inertiaA=L2S⋅dm˙AdtinertiaB=L2S⋅dm˙Bdt

where *L* is the pipe length.

The heat exchanged with the pipe wall through port **H** is added to the
energy of gas volume represented by the internal node via the energy conservation
equation (see Energy Balance). Therefore, the momentum
balances for each half of the pipe, between port **A** and the
internal node and between port **B** and the internal node, are
assumed to be adiabatic processes. The adiabatic relations are:

hA+12(m˙AρAS)2=hI+12(m˙AρIS)2hB+12(m˙BρBS)2=hI+12(m˙BρIS)2

where *h* is the specific enthalpy at port **A**, port
**B**, or internal node I, as indicated by the
subscript.

The pressure losses due to viscous friction, *Δp*AI and *Δp*BI,
depend on the flow regime. The Reynolds numbers for each half of the
pipe are defined as:

ReA=|m˙A|⋅DhS⋅μIReB=|m˙B|⋅DhS⋅μI

where:

- *D*h is the
  hydraulic diameter of the pipe.
- *μ*I is
  the dynamic viscosity at internal node.

If the Reynolds number is less than the **Laminar flow
upper Reynolds number limit** parameter value, then the flow
is in the laminar flow regime. If the Reynolds number is greater than
the **Turbulent flow lower Reynolds number limit** parameter
value, then the flow is in the turbulent flow regime.

In the laminar flow regime, the pressure losses due to viscous
friction are:

ΔpAIlam=fshapem˙A⋅μI2ρI⋅Dh2⋅S⋅L+Leqv2ΔpBIlam=fshapem˙B⋅μI2ρI⋅Dh2⋅S⋅L+Leqv2

where:

- *f*shape is
  the **Shape factor for laminar flow viscous friction** parameter
  value.
- *L*eqv is
  the **Aggregate equivalent length of local resistances** parameter
  value.

In the turbulent flow regime, the pressure losses due to viscous
friction are:

ΔpAItur=fDarcyAm˙A⋅|m˙A|2ρI⋅Dh⋅S2⋅L+Leqv2ΔpBItur=fDarcyBm˙B⋅|m˙B|2ρI⋅Dh⋅S2⋅L+Leqv2

where *f*Darcy is the Darcy friction factor at port
**A** or **B**, as indicated by the
subscript.

The Darcy friction factors are computed from the Haaland correlation:

fDarcyA=[−1.8log10(6.9ReA+(εrough3.7Dh)1.11)]−2fDarcyB=[−1.8log10(6.9ReB+(εrough3.7Dh)1.11)]−2

where *ε*rough is
the **Internal surface absolute roughness** parameter
value.

When the Reynolds number is between the **Laminar flow upper Reynolds number
limit** and the **Turbulent flow lower Reynolds number
limit** parameter values, the flow is in transition between laminar
flow and turbulent flow. The pressure losses due to viscous friction during the
transition region follow a smooth connection between those in the laminar flow
regime and those in the turbulent flow regime.

### Convective Heat Transfer

The convective heat transfer equation between the pipe wall and the internal gas
volume is:

QH=Qconv+kISsurfDh(TH−TI)

*S*surf is the pipe surface area,
*S*surf =
4*S**L*/*D*h.
Assuming an exponential temperature distribution along the pipe, the convective heat
transfer is

Qconv=|m˙avg|cpavg(TH−Tin)(1−exp(−hcoeffSsurf|m˙avg|cpavg))

where:

- *T*in is the inlet temperature depending
  on flow direction.
- m˙avg=(m˙A−m˙B)/2 is the average mass flow rate from port **A** to
  port **B**.
- cpavg is the specific heat evaluated at the average temperature.

The heat transfer coefficient, *h*coeff, depends
on the Nusselt number:

hcoeff=NukavgDh

where *k*avg is the thermal conductivity evaluated
at the average temperature. The Nusselt number depends on the flow regime. The Nusselt
number in the laminar flow regime is constant and equal to the value of the
**Nusselt number for laminar flow heat transfer** parameter. The
Nusselt number in the turbulent flow regime is computed from the Gnielinski
correlation:

Nutur=fDarcy8(Reavg−1000)Pravg1+12.7fDarcy8(Pravg2/3−1)

where *Pr*avg is the Prandtl number evaluated at
the average temperature. The average Reynolds number is

Reavg=|m˙avg|DhSμavg

where *μ*avg is the dynamic viscosity evaluated at
the average temperature. When the average Reynolds number is between the **Laminar
flow upper Reynolds number limit** and the **Turbulent flow lower
Reynolds number limit** parameter values, the Nusselt number follows a smooth
transition between the laminar and turbulent Nusselt number values.

### Choked Flow

The choked mass flow rates out of the pipe at ports **A** and
**B** are:

m˙Achoked=ρA⋅aA⋅Sm˙Bchoked=ρB⋅aB⋅S

where *a*A and
*a*B is the speed of sound at ports
**A** and **B**, respectively.

The unchoked pressure at port **A** or **B** is the value of
the corresponding Across variable at that port:

pAunchoked=A.ppBunchoked=B.p

The choked pressures at ports **A** and **B** are obtained
by substituting the choked mass flow rates into the momentum balance equations for
the pipe:

pAchoked=pI+(m˙AchokedS)2⋅(1ρI−1ρA)+ΔpAIchokedpBchoked=pI+(m˙BchokedS)2⋅(1ρI−1ρB)+ΔpBIchoked

*Δp*AIchoked and
*Δp*BIchoked are
the pressure losses due to viscous friction, assuming that the choking has occurred.
They are computed similar to *Δp*AI and
*Δp*BI, with the mass flow rates at
ports **A** and **B** replaced by the choked mass
flow rate values.

Depending on whether choking has occurred, the block assigns either the choked or unchoked
pressure value as the actual pressure at the port. Choking can occur at the pipe
outlet, but not at the pipe inlet. Therefore, if *p*Aunchoked
≥ *p*I, then port **A** is an inlet and *p*A =
*p*Aunchoked. If *p*Aunchoked
< *p*I, then port **A** is an outlet and

pA={pAunchoked,if pAunchoked≥pAchokedpAchoked,if pAunchoked<pAchoked

Similarly, if *p*Bunchoked
≥ *p*I, then port **B** is an inlet and *p*B =
*p*Bunchoked. If *p*Bunchoked
< *p*I, then port **B** is an outlet and

pB={pBunchoked,if pBunchoked≥pBchokedpBchoked,if pBunchoked<pBchoked

### Assumptions and Limitations

- The pipe wall is perfectly rigid.
- The flow is fully developed. Friction losses and heat
  transfer do not include entrance effects.
- The effect of gravity is negligible.
- This block does not model supersonic flow.
