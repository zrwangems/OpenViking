---
type: simulink-block
title: 'Pipe (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'pipe2p'
documentation_source_path: 'ref/pipe2p.html'
language: en
---

# Pipe (2P)

## Ports

### Conserving

### **A** — Inlet or outlet two-phase fluid

Two-phase fluid conserving port associated with the inlet or outlet of the pipe.
The block has no intrinsic directionality.

### **B** — Inlet or outlet two-phase fluid

Two-phase fluid conserving port associated with the inlet or outlet of the pipe.
The block has no intrinsic directionality.

### **H** — Temperature of pipe wall thermal

Thermal conserving port representing the temperature of the pipe wall.

## Parameters

### Geometry

### **Pipe length** — The length of the pipe `5 m` (default) | positive scalar

The length of the pipe along the direction of flow.

### **Cross-sectional area** — The internal area of the pipe `0.01 m^2` (default) | positive scalar

The internal area of the pipe normal to the direction of the flow. This area is
constant along the length of the pipe.

### **Hydraulic diameter** — Diameter of an equivalent cylindrical pipe with the same cross-sectional area `0.1 m` (default) | positive scalar

Diameter of an equivalent pipe with a circular cross section. In a cylindrical
pipe, the hydraulic diameter is the same as its actual diameter.

### Friction and Heat Transfer

### **Aggregate equivalent length of local resistances** — The combined length of all local resistances present in the pipe `0.1 m` (default) | positive scalar

The combined length of all local resistances present in the pipe. Local
resistances include bends, fittings, armatures, and pipe inlets and outlets. The
effect of the local resistances is to increase the effective length of the pipe
segment. This length is added to the geometrical pipe length only for pressure loss
calculations. The fluid volume inside the pipe depends only on the pipe geometrical
length, defined by the **Pipe length** parameter.

### **Internal surface absolute roughness** — Average depth of all surface defects on the internal surface of the pipe `15e-6 m` (default) | positive scalar

Average depth of all surface defects on the internal surface of the pipe, which
affects the pressure loss in the turbulent flow regime.

### **Laminar flow upper Reynolds number limit** — The Reynolds number above which flow begins to transition from laminar to turbulent `2000` (default) | positive scalar

The Reynolds number above which flow begins to transition from laminar to
turbulent. This number equals the maximum Reynolds number corresponding to fully
developed laminar flow.

### **Turbulent flow lower Reynolds number limit** — The Reynolds number below which flow begins to transition from turbulent to laminar `4000` (default) | positive scalar

The Reynolds number below which flow begins to transition from turbulent to
laminar. This number equals to the minimum Reynolds number corresponding to fully
developed turbulent flow.

### **Shape factor for laminar flow viscous friction** — Effect of pipe geometry on the viscous friction losses `64` (default) | positive scalar

Dimensionless factor that encodes the effect of pipe cross-sectional geometry on
the viscous friction losses in the laminar flow regime. Typical values are 64 for a
circular cross section, 57 for a square cross section, 62 for a rectangular cross
section with an aspect ratio of 2, and 96 for a thin annular cross section [1].

### **Nusselt number for laminar flow heat transfer** — Ratio of convective to conductive heat transfer `3.66` (default) | positive scalar

Ratio of convective to conductive heat transfer in the laminar flow regime. Its
value depends on the pipe cross-sectional geometry and pipe wall thermal boundary
conditions, such as constant temperature or constant heat flux. Typical value is 3.66,
for a circular pipe cross section with constant wall temperature [2].

### Effects and Initial Conditions

### **Enable fluid inertia** — Whether to model fluid inertia off (default) | on

Select this check box to model fluid inertia, the resistance of the fluid to rapid
acceleration.

### **Initial fluid energy specification** — Thermodynamic variable to use in defining initial conditions `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Thermodynamic variable in terms of which to define the initial conditions of the
block.

The value for the **Initial fluid energy specification** parameter limits the
available initial states for the two-phase fluid. When **Initial fluid energy
specification** is:

- `Temperature` — Specify an initial state that is a
  subcooled liquid or superheated vapor. You cannot specify a liquid-vapor mixture
  because the temperature is constant across the liquid-vapor mixture
  region.
- `Vapor quality` — Specify an initial state that is a
  liquid-vapor mixture. You cannot specify a subcooled liquid or a superheated
  vapor because the liquid mass fraction is 0 and 1, respectively, across the
  whole region. Additionally, the block limits the pressure to below the critical
  pressure.
- `Vapor void fraction` — Specify an initial state that
  is a liquid-vapor mixture. You cannot specify a subcooled liquid or a
  superheated vapor because the liquid mass fraction is 0 and 1, respectively,
  across the whole region. Additionally, the block limits the pressure to below
  the critical pressure.
- `Specific enthalpy` — Specify the specific enthalpy of
  the fluid. The block does not limit the initial state.
- `Specific internal energy` — Specify the specific
  internal energy of the fluid. The block does not limit the initial state.

### **Initial pressure** — Absolute pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Pressure in the pipe at the start of simulation, specified against absolute
zero.

### **Initial temperature** — Absolute temperature at start of simulation `293.15 K` (default) | positive scalar

Temperature in the pipe at the start of simulation, specified against absolute
zero.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Temperature`.

### **Initial vapor quality** — Mass fraction of vapor at start of simulation `0.5` (default) | unitless scalar between 0 and 1

Mass fraction of vapor in the pipe at the start of simulation.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Vapor quality`.

### **Initial vapor void fraction** — Volume fraction of vapor at start of simulation `0.5` (default) | unitless scalar between 0 and 1

Volume fraction of vapor in the pipe at the start of simulation.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Vapor void fraction`.

### **Initial specific enthalpy** — Specific enthalpy at start of simulation `1500 kJ/kg` (default) | positive scalar

Specific enthalpy of the fluid in the pipe at the start of simulation.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Specific enthalpy`.

### **Initial specific internal energy** — Specific internal energy at start of simulation `1500 kJ/kg` (default) | positive scalar

Specific internal energy of the fluid in the pipe at the start of
simulation.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Specific internal
energy`.

### **Phase change time constant** — Characteristic duration of a phase-change event `0.1 s` (default) | positive scalar

Characteristic time to equilibrium of a phase-change event taking place in the
pipe. This constant introduces a time lag into the transition between phases. Increase
this parameter value to slow the rate of phase change or decrease it to speed the
rate.

## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

### R2024a: Numerical improvement for low-flow computation in pipes

To improve accuracy for pressure drop inside the pipe at low-speed flows, the momentum
balance computations in the Pipe (2P) block have been changed
slightly. There may be slight differences in simulation results compared to previous
releases, especially when Mach number is low.

## Description

Rigid conduit for fluid flow in two-phase fluid systems

The Pipe (2P) block models the flow dynamics of a two-phase
fluid inside a rigid pipe. The dynamic compressibility and thermal capacity of the fluid are
assumed non-negligible. The two-phase fluid conserving ports **A** and
**B** represent the pipe inlets. The thermal conserving port
**H** represents the pipe wall, through which heat transfer with the pipe
surroundings occurs.

### Fluid Inertia

The block provides an option to model fluid inertia, the resistance to sudden changes in
mass flow rate. By default, fluid inertia modeling is turned off. This setting is
appropriate when the pressure forces driving the flow far exceed the inertial forces acting
on the flow.

The default setting reduces computational costs and is recommended for most models.
However, fluid inertia can become important if the mass flow rate changes rapidly. In such
cases, turning fluid inertia modeling on can help improve simulation accuracy.

### Energy Balance

Energy conservation in the pipe is observed through the equation:

Mu˙I+(m˙A+m˙B)uI=ϕA+ϕB+QH,

where:

- *M* is the fluid mass inside the pipe.
- *u*I is the specific internal energy of
  the fluid inside the pipe.
- *ϕ*A is the energy flow rate into the pipe
  through port A.
- *ϕ*B is the energy flow rate into the pipe
  through port B.
- *Q*H is the heat flow rate into the pipe
  through the pipe wall, represented by port **H**.

**Heat Flow Rate**

Heat transfer between the pipe wall and the internal fluid volume is modeled as a
convective process, with the heat flow rate computed as:

QH=hcoeffSsurf(TH−TI),

where:

- *h*coeff is the average heat transfer
  coefficient in the pipe.
- *S*Surf is the pipe surface area.
- *T*H is the pipe wall
  temperature.
- *T*I is the temperature of the fluid in
  the pipe.

The calculation of the heat transfer coefficient depends on the fluid phase. In the
subcooled liquid and superheated vapor phases, the coefficient is:

h\*coeff=k\*INu\*Dh,

where the asterisk denotes a value specific to the phase considered
(liquid or vapor) and:

- `Nu` is the average Nusselt number in the pipe.
- `k`I is the average thermal conductivity
  in the pipe.
- *D*h is the hydraulic diameter of the
  pipe (that which a cross section of general shape would have if it were made
  circular).

In a two-phase mixture, the same coefficient is:

hMcoeff=kMI,SLNuMDh,

where the subscript `M` denotes a value specific to
the two-phase mixture and the `SL` subscript indicates a value obtained
for the saturated liquid.

**Nusselt Number**

In laminar flows, the Nusselt number is assumed constant and equal to the value
specified in the block dialog box. The laminar flow Nusselt number applies when the
Reynolds number is smaller than the value entered for the **Laminar flow upper
Reynolds number limit** parameter.

The turbulent flow Nusselt number applies when the Reynolds number is greater than the
value entered for the **Laminar flow upper Reynolds number limit**
parameter. In the transitional region between laminar and turbulent flow, a cubic
polynomial function blends the two Nusselt numbers. This blending ensures a smooth
transition between flow regimes.

In the liquid and vapor phases, the Nusselt number for turbulent flow follows from the
Gnielinski correlation:

Nu\*=f8(Re\*−1000)Pr\*I1+12.7f8(Pr\*I2/3−1),

where, as before, the asterisk denotes the phase considered and:

- *f* is the friction factor of the pipe.
- `Re` is the Reynolds number.
- *Pr*I is the Prandtl number.

The friction factor is calculated as:

f={−1.8log10[6.9Re\*+(ϵr3.7)1.11]}-2,

where *ε*r is the roughness of
the pipe. The Reynolds number is calculated as:

Re\*=|m˙Avg|DhvI\*SνI\*,

where the subscript `Avg` denotes an average value
between the ports and:

- *S* is the cross-sectional area of the pipe.
- *v*I is the specific volume.
- *ν*I is the kinematic viscosity.

In the two-phase mixture, the Nusselt number for turbulent flow follows from the
Cavallini and Zecchin correlation:

NuM=0.05[(1−xI+xIvSVvSL)ReSL]0.8PrSL0.33,

where the subscript `SL` denotes a value for saturated
liquid, the `SV` subscript a value for saturated vapor, and:

- *x*I is the vapor quality.
- *v* is the specific volume.

The Reynolds number of the saturated liquid is calculated as:

ReSL=|m˙Avg|DhvSLSνSL,

### Mass Balance

Mass conservation in the pipe is observed through the equation:

[(∂ρ∂p)up˙I+(∂ρ∂u)pu˙I]V=m˙A+m˙B+ϵM,

where:

- *ρ* is the fluid density.
- *p*I is the pressure inside the
  pipe.
- *V* is the volume of fluid in the pipe.
- m˙A is the mass flow rate into the pipe through port
  **A**.
- m˙B is the mass flow rate into the pipe through port
  **B**.
- *∊*M is a correction term that accounts
  for the smoothing of the density partial derivatives across phase transition
  boundaries.

The block blends the density partial derivatives of the various domains using a cubic
polynomial function. At a vapor quality of 0–0.1, this function blends the derivatives of
the subcooled liquid and two-phase mixture domains. At a vapor quality of 0.9–1, it blends
those of the two-phase mixture and superheated vapor domains. The correction term in the
mass conservation equation,

ϵM=M−V/vIτ,

is added to correct for the numerical errors introduced by the cubic
polynomial function, with:

- *M* as the fluid mass in the pipe, computed from the equation:

  M˙=m˙A+m˙B,
- *v*I as the specific volume of the fluid
  in the pipe.
- *τ* as the phase-change time constant—the characteristic
  duration of a phase-change event. This constant ensures that phase changes do not
  occur instantaneously, effectively introducing a time lag whenever they occur.

### Momentum Balance

The momentum balance equations are defined separately for each half pipe section. In the
half pipe adjacent to port **A**:

pA−pI=m˙AS|m˙AS(νI−νA)|+Fvisc,A+IA,

where:

- *p*A is the pressure at port
  **A**.
- *S* is the cross-sectional area of the pipe.
- *ν*A is the specific volume of the fluid
  at port **A**.
- *F*visc,A is the viscous friction force in
  the half pipe adjacent to port **A**.
- *I*A is the fluid inertia at port
  **A**:

  IA=m¨AL2S

  The parameter *L* is the pipe length.

In the half pipe adjacent to port **B**:

pB−pI=m˙BS|m˙BS(νI−νB)|+Fvisc,B+IB,

where:

- *p*B is the pressure at port
  **B**.
- *ν*B is the specific volume of the fluid
  at port **B**.
- *F*visc,B is the viscous friction force in
  the half pipe adjacent to port **B**.
- *I*B is the fluid inertia at port
  **B**:

  IB=m¨BL2S

The fluid inertia terms, *I*A and
*I*B, are zero when the **Enable fluid
inertia** check box is cleared, that is, when fluid inertia modeling is off. The
calculation of the viscous friction forces,
*F*visc,A and
*F*visc,B depends on the flow regime, laminar or
turbulent.

**Viscous Friction Force in Laminar Flows**

In the laminar regime—that is, when the Reynolds number is smaller than the
**Laminar flow upper Reynolds number limit** value specified in the
block dialog box—the viscous friction force in the half pipe adjacent to port
**A** is

Fvisc,Alaminar=fshapeLeffνIm˙A4Dh2S,

while in the half pipe adjacent to port **B** it is

Fvisc,Blaminar=fshapeLeffνIm˙B4Dh2S,

where:

- *f*shape is the pipe shape
  factor.
- *L*eff is the effective pipe
  length—the sum of the pipe length and the aggregate equivalent length of
  local resistances.
- *D*h is the hydraulic diameter of the
  pipe.

**Viscous Friction Force in Turbulent Flows**

In the turbulent regime—that is, when the Reynolds number is greater than the
**Turbulent flow lower Reynolds number limit** value specified in the
block dialog box—the viscous friction force in the half pipe adjacent to port
**A** is

Fvisc,Aturbulent=m˙A|m˙A|fALeffνI4DHS2,

while in the half pipe adjacent to port **B** it is

Fvisc,Bturbulent=m˙B|m˙B|fBLeffνI4DHS2,

where:

- *f*A is the Darcy friction factor for
  turbulent flow in the half pipe adjacent to port **A**.
- *f*B is the Darcy friction factor for
  turbulent flow in the half pipe adjacent to port **B**.

The Darcy friction factor for turbulent flow in the half pipe adjacent to
port **A** follows from the Haaland equation as

fA=1{−1.8log10[6.9ReA+(ϵr3.7)1.11]}2,

and in the half pipe adjacent to port **B** as

fB=1{−1.8log10[6.9ReB+(ϵr3.7)1.11]}2,

where:

- *∊*r is the relative roughness of the
  pipe.
- *Re*A is the Reynolds number in the half
  pipe adjacent to port **A**,

  ReA=|m˙A|DhvISνI.
- *Re*B is the Reynolds number in the half
  pipe adjacent to port **B**,

  ReB=|m˙B|DhvISνI.

A cubic polynomial function is used to blend the friction losses in the transition
region between laminar flow and turbulent flow.

### Assumptions and Limitations

- The pipe wall is rigid.
- The flow is fully developed.
- The effect of gravity is negligible.
- Heat transfer is calculated with respect to the temperature of the fluid volume in
  the pipe. To model temperature gradient due to heat transfer along a long pipe, connect
  multiple Pipe (2P) blocks in series.
