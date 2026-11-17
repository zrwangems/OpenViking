---
type: simulink-block
title: '3-Zone Pipe (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Pipes & Fittings'
documentation_page: '3zonepipe2p'
documentation_source_path: 'ref/3zonepipe2p.html'
language: en
---

# 3-Zone Pipe (2P)

## Ports
```yaml
ports:
- name: Z
  summary: Zone length fractions physical signal
  direction: output
- name: A
  summary: Pipe opening two-phase fluid
  direction: conserving
- name: B
  summary: Pipe opening two-phase fluid
  direction: conserving
- name: H
  summary: Pipe wall thermal
  direction: conserving
```

### Output

### **Z** — Zone length fractions physical signal

Vector with the length fractions of the liquid, mixed-phase, and vapor
zones in the pipe.
### Conserving

### **A** — Pipe opening two-phase fluid

Opening through which the two-phase fluid flows into or out of the
pipe. Ports **A** and **B** can each
function as either inlet or outlet. Thermal conduction is allowed
between the two-phase fluid ports and the fluid internal to the pipe
(though its impact is typically relevant only at near zero flow
rates).

### **B** — Pipe opening two-phase fluid

Opening through which the two-phase fluid flows into or out of the
pipe. Ports **A** and **B** can each
function as either inlet or outlet. Thermal conduction is allowed
between the two-phase fluid ports and the fluid internal to the pipe
(though its impact is typically relevant only at near zero flow
rates).

### **H** — Pipe wall thermal

Thermal boundary condition at the outer surface of the pipe wall. Use
this port to capture heat exchange of various kinds—for example,
conductive, convective, or radiative—between the pipe wall and the
environment. Heat exchange between the inner surface of the wall and the
fluid is captured directly in the block.
## Parameters
```yaml
parameters:
- name: Pipe length
  summary: Distance between the ports of the pipe 5 m (default) | positive scalar with units of length
  group: Geometry
- name: Cross-sectional area
  summary: Internal area normal to the direction of the flow 0.01 m^2 (default) | positive scalar with units of area
  group: Geometry
- name: Hydraulic diameter
  summary: Diameter of a cylindrical pipe with the given cross-sectional area 0.1 m (default) | positive scalar in units of
    length
  group: Geometry
- name: Elevation gain from port A to port B
  summary: Constant pipe elevation differential 0 m (default) | scalar
  group: Geometry
- name: Gravitational acceleration
  summary: Gravitational acceleration 9.81 m/s^2 (default) | scalar
  group: Geometry
- name: Aggregate equivalent length of local resistances
  summary: Minor pressure loss in the pipe expressed as a length 1 m (default) | positive scalar in units of length
  group: Viscous Friction
- name: Internal surface absolute roughness
  summary: Average depth of surface defects on the internal surface of the pipe 15e-6 m (default) | positive scalar in units
    of length
  group: Viscous Friction
- name: Laminar flow upper Reynolds number limit
  summary: Reynolds number below which the flow is laminar 2e+3 (default) | positive unitless scalar
  group: Viscous Friction
- name: Turbulent flow lower Reynolds number limit
  summary: Reynolds number above which the flow is turbulent 4e+3 (default) | positive unitless scalar
  group: Viscous Friction
- name: Shape factor for laminar flow viscous friction
  summary: Dimensionless factor used to capture the effect of geometry on viscous friction losses 64 (default) | positive
    unitless scalar
  group: Viscous Friction
- name: External environment heat transfer coefficient
  summary: Heat transfer coefficient between the environment and the pipe wall 100 W/(m^2*K) (default) | positive scalar with
    units of power/(area\*temperature)
  group: Heat Transfer
- name: Wall thickness
  summary: Average thickness of the pipe wall material 0 m (default) | positive scalar with units of length
  group: Heat Transfer
- name: Wall thermal conductivity
  summary: Thermal conductivity of the pipe wall material 390 W/(m*K) (default) | positive scalar with units of power/(length\*temperature)
  group: Heat Transfer
- name: Wall specific heat
  summary: Heat capacity per unit mass of pipe wall material 390 J/kg/K (default) | positive scalar with units of energy/(mass\*temperature)
  group: Heat Transfer
- name: Wall density
  summary: Mass density of the pipe wall material 9e3 kg/m^3 (default) | positive scalar with units of mass/volume
  group: Heat Transfer
- name: Ratio of external fins surface area to no-fin surface area
  summary: Ratio of heat transfer surface area with external fins to that without 0 (default) | positive unitless scalar
  group: Heat Transfer
- name: External fin efficiency
  summary: Ratio of actual to ideal heat exchange rates with external fins 0.5 (default) | positive unitless scalar
  group: Heat Transfer
- name: Ratio of internal fins surface area to no-fin surface area
  summary: Ratio of heat transfer surface area with internal fins to that without 0 (default) | positive unitless scalar
  group: Heat Transfer
- name: Internal fin efficiency
  summary: Ratio of actual to ideal heat exchange rates with internal fins 0.5 (default) | positive unitless scalar
  group: Heat Transfer
- name: Heat transfer coefficient model
  summary: Method of calculating heat transfer coefficient between fluid and wall Correlation for flow inside tubes (default)
    | Colburn equation
  group: Heat Transfer
- name: Coefficients [a, b, c] for a\*Re^b\*Pr^c in liquid zone
  summary: Colburn equation coefficients in liquid zone [.023, .8, .33] (default) | three-element vector of positive scalars
  group: Heat Transfer
- name: Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone
  summary: Cavallini-Zecchin equation coefficients in mixture zone [.05, .8, .33] (default) | three-element vector of positive
    scalars
  group: Heat Transfer
- name: Coefficients [a, b, c] for a\*Re^b\*Pr^c in vapor zone
  summary: Colburn equation coefficients in vapor zone [.023, .8, .33] (default) | three-element vector of positive scalars
  group: Heat Transfer
- name: Nusselt number for laminar flow heat transfer
  summary: Ratio of convective to conductive heat exchange rates in the laminar flow regime 3.66 (default)
  group: Heat Transfer
- name: Initial fluid energy specification
  summary: Thermodynamic variable whose initial value to set Temperature (default) | Vapor quality | Vapor void fraction |
    Specific enthalpy | Specific internal energy
  group: Effects and Initial Conditions Tab
- name: Initial pressure
  summary: Absolute pressure at the start of simulation 0.101325 MPa (default) | scalar with units of pressure
  group: Effects and Initial Conditions Tab
- name: Initial temperature
  summary: Absolute temperature at the start of simulation 293.15 K (default) | scalar or two-element vector with units of
    temperature
  group: Effects and Initial Conditions Tab
- name: Initial vapor quality
  summary: Mass fraction of vapor at the start of simulation 0.5 (default) | unitless scalar between 0 and 1
  group: Effects and Initial Conditions Tab
- name: Initial vapor void fraction
  summary: Volume fraction of vapor at the start of simulation 0.5 (default) | unitless scalar between 0 and 1
  group: Effects and Initial Conditions Tab
- name: Initial specific enthalpy
  summary: Specific enthalpy at the start of simulation 1500 kJ/kg (default) | scalar with units of energy/mass
  group: Effects and Initial Conditions Tab
- name: Initial specific internal energy
  summary: Specific internal energy at the start of simulation 1500 kJ/kg (default) | scalar with units of energy/mass
  group: Effects and Initial Conditions Tab
```

### Geometry

### **Pipe length** — Distance between the ports of the pipe `5 m` (default) | positive scalar with units of length

Distance between the ports of the pipe. The liquid, two-phase, and
vapor zones each comprise a fraction of this distance. The zone
fractions can vary but their aggregate length, being the same as the
distance of the pipe, is fixed.

### **Cross-sectional area** — Internal area normal to the direction of the flow `0.01 m^2` (default) | positive scalar with units of area

Internal area of the pipe normal to the direction of flow. The cross
section of the pipe is assumed to be constant throughout its
length.

### **Hydraulic diameter** — Diameter of a cylindrical pipe with the given cross-sectional area `0.1 m` (default) | positive scalar in units of length

Ratio of the opening area of a cross section of the pipe to the
perimeter of that area. The pipe is not required to be cylindrical, and
its cross-section have any shape. This parameter gives the diameter that
a general cross section would have if it were circular.

### **Elevation gain from port A to port B** — Constant pipe elevation differential `0 m` (default) | scalar

Elevation differential for across the pipe.

### **Gravitational acceleration** — Gravitational acceleration `9.81 m/s^2` (default) | scalar

Gravitational acceleration in the pipe environment.

### Viscous Friction

### **Aggregate equivalent length of local resistances** — Minor pressure loss in the pipe expressed as a length `1 m` (default) | positive scalar in units of length

Combined length of all local resistances present in the pipe. Local
resistances include bends, fittings, armatures, and pipe inlets and
outlets. The effect of the local resistances is to increase the
effective length of the pipe. This length is added to the geometrical
pipe length for friction calculations.

### **Internal surface absolute roughness** — Average depth of surface defects on the internal surface of the pipe `15e-6 m` (default) | positive scalar in units of length

Average depth of all surface defects on the internal surface of the
pipe. The surface defects affect the pressure loss across the pipe in
the turbulent flow regime.

### **Laminar flow upper Reynolds number limit** — Reynolds number below which the flow is laminar `2e+3` (default) | positive unitless scalar

Reynolds number above which the pipe flow begins to transition from
laminar to turbulent. This value is the maximum Reynolds number
corresponding to fully developed laminar flow.

### **Turbulent flow lower Reynolds number limit** — Reynolds number above which the flow is turbulent `4e+3` (default) | positive unitless scalar

Reynolds number below which the pipe flow begins to transition from
turbulent to laminar. This value is the minimum Reynolds number
corresponding to fully developed turbulent flow.

### **Shape factor for laminar flow viscous friction** — Dimensionless factor used to capture the effect of geometry on viscous friction losses `64` (default) | positive unitless scalar

Dimensionless factor used to capture the effects of cross-sectional
geometry on the viscous friction losses incurred in the laminar flow
regime. Typical values are `64` for a circular cross
section, `57` for a square cross section, and
`62` for a rectangular cross section with an aspect
ratio of 2.

### Heat Transfer

### **External environment heat transfer coefficient** — Heat transfer coefficient between the environment and the pipe wall `100 W/(m^2*K)` (default) | positive scalar with units of power/(area\*temperature)

Heat transfer coefficient for heat exchange between the environment
(at port **H**) and the outer surface of the pipe wall.
If this parameter is set to `inf`, then the thermal
resistance between the environment and the wall is assumed to be zero.
The pipe wall then has a uniform temperature equal to that associated
with port **H**.

### **Wall thickness** — Average thickness of the pipe wall material `0 m` (default) | positive scalar with units of length

Average thickness of the pipe wall material. If this value is set to
`0`, then both thermal resistance due to conduction
through the pipe wall and thermal storage due to the thermal mass of the
pipe wall are assumed to be negligible.

### **Wall thermal conductivity** — Thermal conductivity of the pipe wall material `390 W/(m*K)` (default) | positive scalar with units of power/(length\*temperature)

Thermal conductivity of the pipe wall material. If this parameter is
set to `inf`, then thermal resistance due to conduction
through the pipe wall is assumed to be negligible.

### **Wall specific heat** — Heat capacity per unit mass of pipe wall material `390 J/kg/K` (default) | positive scalar with units of energy/(mass\*temperature)

Heat capacity per unit mass of the pipe wall material. If this
parameter is set to `0`, then thermal storage due to
the thermal mass of the pipe is assumed to be negligible.

### **Wall density** — Mass density of the pipe wall material `9e3 kg/m^3` (default) | positive scalar with units of mass/volume

Mass density of the pipe wall material. If this parameter is set to
`0`, then thermal storage due to the thermal mass
of the pipe wall is assumed to be negligible.

### **Ratio of external fins surface area to no-fin surface area** — Ratio of heat transfer surface area with external fins to that without `0` (default) | positive unitless scalar

Ratio of the total heat transfer surface area of the fins on the
external side of the pipe wall to that of the pipe wall without any
fins. The presence of fins serves to enhance the convective heat
transfer between the pipe wall and the environment.

### **External fin efficiency** — Ratio of actual to ideal heat exchange rates with external fins `0.5` (default) | positive unitless scalar

Ratio of the actual heat exchange rate between the external fins and
the environment to its ideal value (if the fins were entirely held at
the temperature of the pipe wall). This parameter is a function of fin
geometry.

### **Ratio of internal fins surface area to no-fin surface area** — Ratio of heat transfer surface area with internal fins to that without `0` (default) | positive unitless scalar

Ratio of the total heat transfer surface area of the fins on the
internal side of the pipe wall to that of the pipe wall without any
fins. The presence of fins serves to enhance the convective heat
transfer between the pipe wall and the fluid.

### **Internal fin efficiency** — Ratio of actual to ideal heat exchange rates with internal fins `0.5` (default) | positive unitless scalar

Ratio of the actual heat exchange rate between the internal fins and
the environment to its ideal value (if the fins were entirely held at
the temperature of the pipe wall). This parameter is a function of fin
geometry.

### **Heat transfer coefficient model** — Method of calculating heat transfer coefficient between fluid and wall `Correlation for flow inside tubes` (default) | `Colburn equation`

Method of calculating the heat transfer coefficient between the fluid
and the wall. The available settings are:

- `Colburn equation`. Use this
  setting to calculate the heat transfer coefficient with
  user-defined variables *a*,
  *b*, and *c*. In
  the liquid and vapor zones, the heat transfer coefficient is
  based on the Colburn equation. In the liquid-vapor mixture
  zone, the heat transfer coefficient is based on the
  Cavallini-Zecchin equation.
- `Correlation for flow inside
  tubes`. Use this setting to calculate the
  heat transfer coefficient for pipe flows. In the liquid and
  vapor zones, the heat transfer coefficient is calculated
  with the Gnielinski correlation. In the liquid-vapor mixture
  zone, the heat transfer coefficient is calculated with the
  Cavallini-Zecchin equation.

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in liquid zone** — Colburn equation coefficients in liquid zone `[.023, .8, .33]` (default) | three-element vector of positive scalars

Three-element vector that contains the empirical coefficients of the
Colburn equation. Each fluid zone has a distinct Nusselt number, which
the block calculates by using the Colburn equation for each zone. The
general form of the Colburn equation is:

Nu=aRebPrc.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Colburn
equation`.

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone** — Cavallini-Zecchin equation coefficients in mixture zone `[.05, .8, .33]` (default) | three-element vector of positive scalars

Three-element vector that contains the empirical coefficients for the
Cavallini-Zecchin equation. Each fluid zone has a distinct Nusselt
number, which the block calculates in the mixture zone by using the
Cavallini-Zecchin equation:

Nu=aReSLbPrSLc{[(ρSLρSV−1)xOut+1]1+b−[(ρSLρSV−1)xIn+1]1+b}(1+b)(ρSLρSV−1)(xOut−xIn).

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Colburn
equation`.

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in vapor zone** — Colburn equation coefficients in vapor zone `[.023, .8, .33]` (default) | three-element vector of positive scalars

Three-element vector that contains the empirical coefficients of the
Colburn equation. Each fluid zone has a distinct Nusselt number, which
the block calculates by using the Colburn equation for each zone. The
general form of the Colburn equation is:

Nu=aRebPrc.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Colburn
equation`.

### **Nusselt number for laminar flow heat transfer** — Ratio of convective to conductive heat exchange rates in the laminar flow regime `3.66` (default)

Ratio of convective to conductive heat exchange rates in the laminar
flow regime. This parameter is a function of pipe cross section
geometry. Typical values are `3.66` for a circular
cross section, `2.98` for a square cross section, and
`3.39` for a rectangular cross section with an
aspect ratio of 2.

### Effects and Initial Conditions Tab

### **Initial fluid energy specification** — Thermodynamic variable whose initial value to set `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

Thermodynamic variable in terms of which to define the initial
conditions of the component.

The value for **Initial fluid energy specification** parameter limits the
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

### **Initial pressure** — Absolute pressure at the start of simulation `0.101325 MPa` (default) | scalar with units of pressure

Pressure in the pipe at the start of simulation, specified against
absolute zero.

### **Initial temperature** — Absolute temperature at the start of simulation `293.15 K` (default) | scalar or two-element vector with units of temperature

Fluid temperature in the pipe at the start of simulation. This
parameter can be a scalar or a 2-element vector. If it is a scalar, the
initial temperature is assumed to be uniform throughout the pipe. If it
is a vector, the initial temperature is assumed to vary linearly between
the ports. The first vector element gives the initial temperature at the
inlet and the second vector element that at the outlet.

#### Dependencies

This parameter is active when the **Initial fluid energy
specification** option is set to
`Temperature`.

### **Initial vapor quality** — Mass fraction of vapor at the start of simulation `0.5` (default) | unitless scalar between 0 and 1

Vapor quality, or mass fraction of vapor, in the pipe at the start of
simulation. This parameter can be a scalar or a 2-element vector. If it
is a scalar, the initial vapor quality is assumed to be uniform
throughout the pipe. If it is a vector, the initial vapor quality is
assumed to vary linearly between the ports. The first vector element
gives the initial vapor quality at the inlet and the second vector
element that at the outlet.

#### Dependencies

This parameter is active when the **Initial fluid energy
specification** option is set to `Vapor
quality`.

### **Initial vapor void fraction** — Volume fraction of vapor at the start of simulation `0.5` (default) | unitless scalar between 0 and 1

Vapor void fraction, or vapor volume fraction, in the pipe at the
start of simulation. This parameter can be a scalar or a 2-element
vector. If it is a scalar, the initial vapor void fraction is assumed to
be uniform throughout the pipe. If it is a vector, the initial vapor
void fraction is assumed to vary linearly between the ports. The first
vector element gives the initial vapor void fraction at the inlet and
the second vector element that at the outlet.

#### Dependencies

This parameter is active when the **Initial fluid energy
specification** option is set to `Vapor
void fraction`.

### **Initial specific enthalpy** — Specific enthalpy at the start of simulation `1500 kJ/kg` (default) | scalar with units of energy/mass

Specific enthalpy of the fluid in the pipe at the start of simulation.
This parameter can be a scalar or a 2-element vector. If it is a scalar,
the initial specific enthalpy is assumed to be uniform throughout the
pipe. If it is a vector, the initial specific enthalpy is assumed to
vary linearly between the ports. The first vector element gives the
initial specific enthalpy at the inlet and the second vector element
that at the outlet.

#### Dependencies

This parameter is active when the **Initial fluid energy
specification** option is set to `Specific
enthalpy`.

### **Initial specific internal energy** — Specific internal energy at the start of simulation `1500 kJ/kg` (default) | scalar with units of energy/mass

Specific internal energy of the fluid in the pipe at the start of
simulation. This parameter can be a scalar or a 2-element vector. If it
is a scalar, the initial specific internal energy is assumed to be
uniform throughout the pipe. If it is a vector, the initial specific
internal energy is assumed to vary linearly between the ports. The first
vector element gives the initial specific internal energy at the inlet
and the second vector element that at the outlet.

#### Dependencies

This parameter is active when the **Initial fluid energy
specification** option is set to `Specific
internal energy`.
## Libraries

Simscape / Fluids / Two-Phase Fluid / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2023b: Model elevation gain and hydrostatic pressure

The 3-Zone Pipe (2P) block now allows you to model
elevation gain and hydrostatic pressure. Use the new **Elevation gain from
port A to port B** and **Gravitational
acceleration** parameters to control these effects.

### R2022b: Parameterize using a new heat transfer coefficient model

The 3-Zone Pipe (2P) block now allows you to more
explicitly control the heat transfer process. You can set the new **Heat
transfer coefficient model** parameter to:

- `Correlation for flow inside tubes` — The
  Gnielinski correlation predicts heat transfer of turbulent flows in
  subcooled liquid or superheated vapor zones, and the Cavallini-Zecchin
  correlation predicts the heat transfer of turbulent flows in the
  liquid-vapor mixture zone. The block predefines the coefficients
  *a*, *b*, and
  *c*. This is how the block operates in previous
  releases.
- `Colburn equation` — The block allows you to
  define the coefficients *a*, *b*, and
  *c* for each flow zone by using the
  **Coefficients [a, b, c] for a\*Re^b\*Pr^c in liquid
  zone**, **Coefficients [a, b, c] for a\*Re^b\*Pr^c in
  mixture zone**, and **Coefficients [a, b, c] for
  a\*Re^b\*Pr^c in vapor zone** parameters. You specify these
  parameters as three-element vectors where the first element is
  *a*, the second is *b*, and the
  third is *c*.

## Description

Pipe with phase-changing fluid in a two-phase fluid network

The 3-Zone Pipe (2P) block models a pipe with a phase-changing
fluid. Each fluid phase is called a *zone*, which is a fractional
value between 0 and 1. Zones do not mix. The block uses a boundary-following
model to track the sub-cooled liquid (L), vapor-liquid mixture (M), and super-heated
vapor (V) in three zones. The relative amount of space a zone occupies in the system is
called a *zone length fraction* within the system.

Port **H** is a thermal port that represents the environmental
temperature. The rate of heat transfer between the fluid and the environment depends on
the fluid phase of each zone. The block models the pipe wall and the pipe wall
temperature in each zone may be different. The fluid dynamic compressibility and the
fluid zone thermal capacity impact the fluid pressure and temperature.

### Heat Transfer Between the Fluid and the Wall

The convective heat transfer coefficient between the fluid and the wall,
*αF*, varies per zone according to
the Nusselt number

αF=NukDH,

where:

- `Nu` is the zone Nusselt number.
- *k* the average fluid thermal conductivity.
- *DH* is the value of the
  **Hydraulic diameter** parameter, the equivalent
  diameter of a non-circular pipe.

The Nusselt number used in the heat transfer coefficient is the greater of the
turbulent- and laminar-flow Nusselt numbers.

For turbulent flows in the subcooled liquid or superheated vapor zones, the
Nusselt number is calculated with the Gnielinski correlation

Nu=f8(Re−1000)Pr1+12.7( f8)1/2(Pr2/3−1),

where:

- `Re` is the zone average Reynolds number.
- `Pr` is the zone average Prandtl number.
- *f* is the Darcy friction factor, calculated from the
  Haaland correlation

  1f=−1.8log10[(εDH3.7)1.11+6.9Re],

  where *ε* is the value of the
  **Internal surface absolute
  roughness**parameter.

For turbulent flows in the liquid-vapor mixture zone, the Nusselt number is
calculated with the Cavallini-Zecchin correlation

Nu=aReSLbPrSLc{[(ρSLρSV−1)xOut+1]1+b−[(ρSLρSV−1)xIn+1]1+b}(1+b)(ρSLρSV−1)(xOut−xIn),

where:

- *ReSL* is the Reynolds number
  of the saturated liquid.
- *PrSL* is the Prandtl number
  of the saturated liquid.
- *ρSL* is the density of the
  saturated liquid.
- *ρSV* is the density of the
  saturated vapor.
- *a*= 0.05, *b* = 0.8, and
  *c*= 0.33.

When fins are modeled on the pipe internal surface, the heat transfer coefficient is

αF=NukDH(1+ηIntsInt),

where:

- *η*Int is the value of the
  **Internal fin efficiency** parameter.
- *s*Int is the value of the
  **Ratio of internal fins surface area to no-fin surface
  area** parameter.

For laminar flows, the Nusselt number is the value of the **Laminar flow
Nusselt number** parameter.

**Empirical Nusselt Number Formulation**

When the **Heat transfer coefficient model** parameter is `Colburn equation`, the block calculates the Nusselt number for the
subcooled liquid and superheated vapor zones by using the empirical
Colburn equation

Nu=aRebPrc,

where *a*, *b*, and
*c* are values in the **Coefficients [a, b, c] for
a\*Re^b\*Pr^c in liquid zone** and **Coefficients [a, b, c]
for a\*Re^b\*Pr^c in vapor zone** parameters.

The block calculates the Nusselt number for liquid-vapor mixture zones by using the
Cavallini-Zecchin equation with the variables in the
**Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone**
parameter.

**Specific Enthalpy**

The heat transfer rate from the fluid is based on the change in specific
enthalpy in each zone

Q=m˙Q(ΔhL+ΔhM+ΔhV),

where m˙Q is the mass flow rate for heat transfer. It is the pipe inlet
mass flow rate, either m˙A or m˙B, depending on the direction of fluid
flow.

In the liquid and vapor zones, the change in specific enthalpy is defined as

Δh=cp(TH−TI)[1−exp(−zSWm˙Qcp(αF−1+αE−1))],

where:

- *cp* is the specific heat
  of the liquid or vapor.
- *TH* is the environmental
  temperature.
- *TI* is the liquid inlet
  temperature.
- *z* is the fluid zone length fraction.
- *αE* is the heat transfer
  coefficient between the wall and the environment.
- *SW* is wall surface area

  SW=4ADHL,

  where:

  - *A* is the value of the
    **Cross-sectional area**
    parameter.
  - *L* is the value of the
    **Pipe length** parameter.

  The wall surface area does not include fin area,
  which is set by the **Ratio of external fins surface area to
  no-fin surface area** and **Ratio of internal
  fins surface area to no-fin surface area** parameters.
  Fins are set in proportion to the wall surface area. A value of
  `0` means there are no fins on the pipe
  wall.

In the liquid-vapor mixture zone, the change in specific enthalpy is
calculated as

Δh=(TH−TS)zSWm˙Q(αF−1+αE−1),

where *TS* is the
fluid saturation temperature. It is assumed that the liquid-vapor mixture is
always at this temperature.

**Heat Transfer Rate**

The total heat transfer between the fluid and the pipe wall is the sum of the
heat transfer in each fluid phase

QF=QF,L+QF,V+QF,M.

The heat transfer rate between the fluid and the pipe in the
liquid zone is

QF,L=m˙Qcp,L[TW,L−min(TI,TS)][1−exp(−zLSWαLm˙Qcp,L)].

where *TW,L* is the
temperature of the wall surrounding the liquid zone.

The heat transfer rate between the fluid and the pipe in the mixture zone is

QF,M=(TH−TSat)zMSWαM.

The heat transfer rate between the fluid and the pipe in the vapor zone is

QF,V=m˙Qcp,V[TW,V−min(TI,TSat)][1−exp(−zVSWαVm˙Qcp,V)],

where *TW,V* is the
temperature of the wall surrounding the vapor zone.

### Heat Transfer Between the Wall and the Environment

If the pipe wall has a finite thickness, the heat transfer coefficient between the
wall and the environment, *αE*, is defined by

1αE=1αW+1αExt(1+ηExtsExt),

where *α*W is the heat
transfer coefficient due to conduction through the wall

αW=kWDHln(1+tWDH),

and where:

- *kW* is the value of the
  **Wall thermal conductivity** parameter.
- *tW* is the value of the
  **Wall thickness** parameter.
- *αExt* is the value of the
  **External environment heat transfer coefficient**
  parameter.
- *ηExt* is the value of the
  **External fin efficiency** parameter.
- *sExt* is the value of the
  **Ratio of external fins surface area to no-fin surface
  area** parameter.

If the wall does not have thermal mass, the heat transfer coefficient between the
wall and environment equals the heat transfer coefficient of the environment,
*α*Ext.

**Heat Transfer Rate**

The heat transfer rate between each wall zone and the environment is

QH,zone=(TH−TW)zSWαE.

The total heat transfer between the wall and the environment is

QH=QH,L+QH,V+QH,M.

**Governing Differential Equations**

The heat transfer rate depends on the thermal mass of the wall,
*CW*

CW=cp,WρWSW(tW+tW2DH),

where:

- *c*p,W is the value of the
  **Wall specific heat** parameter.
- *ρW* is the value of the
  **Wall density** parameter.

The governing equations for heat transfer between the fluid and the external
environment for the liquid zone are

QH,L−QF,L=CW[zLdTW,Ldt+max(dzLdt,0)(TW,L−TW,M)],

for the mixture zone are

QH,M−QF,M=CW[zMdTW,Mdt+min(dzLdt,0)(TW,L−TW,M)+min(dzVdt,0)(TW,V−TW,M)],

and for the vapor zone are

QH,V−QF,V=CW[zVdTW,Vdt+max(dzVdt,0)(TW,V−TW,M)].

### Momentum Balance

Two factors determine the pressure differential over the pipe: the changes in
pressure due to changes in density, and changes in pressure due to friction at the
pipe walls.

For turbulent flows, when the Reynolds number is above the value of the
**Turbulent flow lower Reynolds number limit** parameter, the
block calculates the pressure loss in terms of the Darcy friction factor. The
pressure differential between port **A** and the internal node I is

pA−pI=(1ρI−1ρA\*)(m˙AS)2+fAm˙A|m˙A|2ρIDHS2(L+LAdd2)+Δphydrostatic2,

where:

- *ρI* is the fluid density at
  internal node I.
- *ρA\** is the fluid density at
  port **A**, which is the same as
  *ρA* when the flow is
  steady-state. When the flow is transient, the block calculates
  *ρA\** from the fluid
  internal state at the internal node I with the adiabatic expression

  uA\*+pAρA\*+12(m˙AρA\*S)2=h+12(m˙AρS)2,

  where:

  - *h* is the average specific enthalpy, h=hLzL+hVzV+hMzM.
  - *ρ* is the average density, ρ=ρLzL+ρMzM+ρVzV.
- m˙A is the mass flow rate through
  port **A**.
- *L* is the value of the **Pipe
  length** parameter.
- *LAdd* is the value of the
  **Aggregate equivalent length of local
  resistances** parameter, which is the equivalent length of
  a tube that introduces the same amount of loss as the sum of the losses
  due to other local resistances.
- Δphydrostatic=MVgΔz is the hydrostatic pressure, where:

  - *M* is the total fluid mass in the
    pipe.
  - *V* is the total fluid volume which is
    the volume of the pipe.
  - *g* is the value of the
    **Gravitational acceleration**
    parameter.
  - *Δz* is the value of the
    **Elevation gain from port A to port
    B** parameter.

The Darcy friction factor depends on the Reynolds number, which the
block calculates at both ports.

The pressure differential between port **B** and internal node I is

pB−pI=(1ρI−1ρB\*)(m˙BS)2+fBm˙B|m˙B|2ρIDHS2(L+LAdd2)−Δphydrostatic2,

where:

- *ρB\** is the fluid density at
  port **B**, which is the same as
  *ρB* when the flow is
  steady-state. When the flow is transient, the block calculates
  *ρB\** from the fluid
  internal state with the adiabatic expression

  uB\*+pBρB\*+12(m˙BρB\*S)2=h+12(m˙BρS)2.
- m˙B is the mass flow rate through
  port **B**.

For laminar flows, when the Reynolds number is below the value of the
**Laminar flow upper Reynolds number limit** parameter, the
block calculates the pressure loss due to friction in terms of the **Laminar
friction constant for Darcy friction factor** parameter,
*λ*. The pressure differential between port
**A** and internal node I is

pA−pI=(1ρI−1ρA\*)(m˙AS)2+λμm˙A2ρIDH2S(L+LAdd2)+Δphydrostatic2,

where *μ* is the average fluid dynamic viscosity

μ=μLzL+μMzM+μVzV.

The pressure differential between port **B** and internal node I is

pB−pI=(1ρI−1ρB\*)(m˙BS)2+λμm˙B2ρIDH2S(L+LAdd2)−Δphydrostatic2.

For transitional flows, the block smooths the pressure differential due to viscous
friction between the values for laminar and turbulent pressure losses.

### Mass Balance

The total mass accumulation rate is

dMdt=m˙A+m˙B.

In terms of the fluid zones, the mass accumulation rate is a
function of the change in density, *ρ*, with respect to pressure,
*p*, and the fluid specific internal energy,
*u*

dMdt=[(∂ρ∂p)udpdt+(∂ρ∂u)pduoutdt+ρLdzLdt+ρMdzMdt+ρVdzVdt]V,

where *uout* is the
specific internal energy after all heat transfer has occurred.

### Energy Balance

The energy conservation equation is

Mduoutdt+(m˙A+m˙B)uout=ϕA+ϕB+QF−m˙avggΔz,

where:

- *ϕA* is the energy flow rate
  at port **A**.
- *ϕB* is the energy flow rate
  at port **B**.
- *QF* is the heat transfer rate
  between the fluid and the wall.
- m˙avg=m˙A−m˙B2.

### Assumptions and Limitations

- The pipe wall is perfectly rigid.
- The flow is fully developed. Friction losses and heat transfer do not
  include entrance effects.
- Fluid inertia is negligible.
- The block models gravitational effects at a bulk-system level and does not
  model the separation of liquid and vapor within the pipe due to gravity.
- When the pressure is above the fluid critical pressure, large values of
  thermal fluid properties (such as Prandtl number, thermal conductivity, and
  specific heat) may not accurately reflect the heat exchange in the
  pipe.
