---
type: simulink-block
title: 'Pipe (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'pipema'
documentation_source_path: 'ref/pipema.html'
language: en
---

# Pipe (MA)

## Ports

### Output

### **W** — Rate of condensation leaving system, kg/s physical signal

Physical signal output port that measures the rate of condensation
that leaves the system. If you select **Condensation on wall
surface** this port reports the total rate of water vapor
condensation, which includes the condensation from a saturated moist air
volume as well as the condensation on the pipe wall. This value does not
include the portion of condensation that is entrained as water droplets.

### **F** — Vector physical signal containing pressure, temperature, humidity, and trace gas levels data physical signal vector

Physical signal output port that outputs a vector signal. The vector
contains the pressure (in Pa), temperature (in K), humidity level, and
trace gas level measurements inside the component. Use the
Measurement Selector (MA) block to unpack this
vector signal.
### Conserving

### **A** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the
pipe. This block has no intrinsic directionality.

### **B** — Inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet of the
pipe. This block has no intrinsic directionality.

### **H** — Temperature of pipe wall thermal

Thermal conserving port associated with the temperature of the pipe
wall. The block includes the convective heat transfer between the moist
air mixture inside the pipe and the pipe wall.

### **S** — Inject or extract moisture and trace gas moist air source

Connect this port to port **S** of a block from the
Moisture & Trace Gas Sources library to add or remove moisture and
trace gas. For more information, see Using Moisture and Trace Gas Sources.

#### Dependencies

This port is visible only if you set the **Moisture and
trace gas source** parameter to
`Controlled`.

## Parameters

### Main

### **Pipe length** — Length of the pipe `5 m` (default)

Length of the pipe along the direction of flow.

### **Cross-sectional area** — Internal area of the pipe `0.01 m^2` (default)

Internal area of the pipe normal to the direction of the flow.

### **Hydraulic diameter** — Diameter of an equivalent cylindrical pipe with the same cross-sectional area `0.1 m` (default)

Diameter of an equivalent cylindrical pipe with the same
cross-sectional area.

### Friction and Heat Transfer

### **Aggregate equivalent length of local resistances** — Combined length of all local resistances present in the pipe `0.1 m` (default)

Combined length of all local resistances present in the pipe. Local
resistances include bends, fittings, armatures, and pipe inlets and
outlets. The effect of the local resistances is to increase the
effective length of the pipe segment. This length is added to the
geometrical pipe length only for friction calculations. The moist air
volume depends only on the pipe geometrical length, defined by the
**Pipe length** parameter.

### **Internal surface absolute roughness** — Average depth of all surface defects on the internal surface of the pipe `15e-6 m` (default)

Average depth of all surface defects on the internal surface of the
pipe, which affects the pressure loss in the turbulent flow
regime.

### **Laminar flow upper Reynolds number limit** — Reynolds number above which flow begins to transition from laminar to turbulent `2000` (default)

Reynolds number above which flow begins to transition from laminar to
turbulent. This number equals the maximum Reynolds number corresponding
to the fully developed laminar flow.

### **Turbulent flow lower Reynolds number limit** — Reynolds number below which flow begins to transition from turbulent to laminar `4000` (default)

Reynolds number below which flow begins to transition from turbulent
to laminar. This number equals to the minimum Reynolds number
corresponding to the fully developed turbulent flow.

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

### Moisture and Trace Gas

### **Condensation on wall surface** — Model the effect of wall condensation on a cold pipe surface in contact with a moist air volume `Off` (default) | `On`

Select this check box to model the effect of wall condensation on a
cold pipe surface in contact with a moist air volume. For more
information, see Effect of Condensation on Wall Surface.
In default configuration, the block does not model this effect and
accounts for water vapor condensation only at 100% relative humidity, as
described in Convective Heat Transfer
and Saturation and Condensation.

### **Relative humidity at saturation** — Relative humidity above which condensation occurs `1` (default)

Relative humidity above which condensation occurs.

### **Water vapor condensation time constant** — Time scale for condensation `1e-3 s` (default) | positive scalar

Characteristic time scale at which an oversaturated moist air volume
returns to saturation by condensing out excess moisture.

### **Water droplets evaporation time constant** — Time scale for evaporation `1e-3 s` (default) | positive scalar

Characteristic time scale at which water droplets evaporate to
vapor.

### **Fraction of condensate entrained as water droplets** — Fraction of condensate in water droplets `1` (default) | scalar in the range [0,1]

Fraction of the condensate in the moist air that is entrained as water
droplets.

### **Moisture and trace gas source** — Model moisture and trace gas levels `None` (default) | `Constant` | `Controlled`

This parameter controls visibility of port **S** and
provides these options for modeling moisture and trace gas levels inside
the component:

- `None` — No moisture or trace gas is
  injected into or extracted from the block. Port
  **S** is hidden. This is the
  default.
- `Constant` — Moisture and trace gas
  are injected into or extracted from the block at a constant
  rate. The same parameters as in the Moisture
  Source (MA) and Trace Gas
  Source (MA) blocks become available in the
  **Moisture and Trace Gas** section of the
  block interface. Port **S** is hidden.
- `Controlled` — Moisture and trace gas
  are injected into or extracted from the block at a time-varying
  rate. Port **S** is exposed. Connect the
  Controlled Moisture Source
  (MA) and Controlled Trace Gas
  Source (MA) blocks to this port.

### **Moisture added or removed** — Select whether the block adds or removes moisture as water vapor or water droplets `Water vapor` (default) | `Water droplets`

Select whether the block adds or removes moisture as water vapor or
water droplets.

#### Dependencies

To enable this parameter, set **Moisture and trace gas
source** to `Constant`.

### **Water vapor evaporated from liquid or condensed to liquid** — How the block adds or removes water vapor `off` (default) | `on`

Select how the block adds or removes water vapor. If you clear this
check box, the enthalpy of the added or removed moisture corresponds to
the enthalpy of water vapor, which is greater than that of liquid
water.

If you select this check box, the enthalpy of the added or removed
moisture corresponds to the enthalpy of liquid water, which is less than
that of water vapor. When water vapor is added, it evaporates from
liquid and the latent heat is contributed by the connected fluid volume.
When water vapor is removed, it condenses to liquid and the latent heat
is released to the connected fluid volume.

#### Dependencies

To enable this parameter, set **Moisture and trace gas
source** to `Constant` and
**Moisture added or removed** to
`Water vapor`.

### **Rate of moisture added** — Constant mass flow rate through the block `0 kg/s` (default)

Water vapor or water droplets mass flow rate through the block. A
positive value adds moisture to the connected moist air volume. A
negative value extracts moisture from that volume.

#### Dependencies

To enable this parameter, set **Moisture and trace gas
source** to `Constant`.

### **Added moisture temperature specification** — Select specification method for the temperature of added moisture `Atmospheric temperature` (default) | `Specified temperature`

Select a specification method for the moisture temperature:

- `Atmospheric temperature` —
  Use the atmospheric temperature, specified by the Moist
  Air Properties (MA) block connected to the
  circuit.
- `Specified temperature` —
  Specify a value by using the **Temperature of added
  moisture** parameter.

#### Dependencies

To enable this parameter, set **Moisture and trace gas
source** to `Constant`.

### **Temperature of added moisture** — Moisture temperature `293.15 K` (default)

Enter the desired temperature of added moisture. This temperature
remains constant during simulation. The block uses this value to
evaluate the specific enthalpy of the added moisture only. The specific
enthalpy of removed moisture is based on the temperature of the
connected moist air volume.

#### Dependencies

To enable this parameter, set **Added moisture
temperature specification** to `Specified
temperature`.

### **Rate of trace gas added** — Constant mass flow rate through the block `0 kg/s` (default)

Trace gas mass flow rate through the block. A positive value adds
trace gas to the connected moist air volume. A negative value extracts
trace gas from that volume.

#### Dependencies

To enable this parameter, set **Moisture and trace gas
source** to `Constant`.

### **Added trace gas temperature specification** — Select specification method for the temperature of added trace gas `Atmospheric temperature` (default) | `Specified temperature`

Select a specification method for the trace gas temperature:

- `Atmospheric temperature` —
  Use the atmospheric temperature, specified by the Moist
  Air Properties (MA) block connected to the
  circuit.
- `Specified temperature` —
  Specify a value by using the **Temperature of added
  trace gas** parameter.

#### Dependencies

To enable this parameter, set **Moisture and trace gas
source** to `Constant`.

### **Temperature of added trace gas** — Trace gas temperature `293.15 K` (default)

Enter the desired temperature of added trace gas. This temperature
remains constant during simulation. The block uses this value to
evaluate the specific enthalpy of the added trace gas only. The specific
enthalpy of removed trace gas is based on the temperature of the
connected moist air volume.

#### Dependencies

To enable this parameter, set **Added trace gas
temperature specification** to `Specified
temperature`.

### Initial Conditions

### **Initial pressure** — Moist air pressure at the start of simulation `0.101325 MPa` (default) | positive scalar

Moist air pressure at the start of the simulation.

### **Initial pressure priority** — Pressure parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial
pressure** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

### **Initial temperature** — Temperature at the start of simulation `293.15 K` (default) | positive scalar

Initial moist air temperature.

### **Initial temperature priority** — Temperature parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial
temperature** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

### **Initial humidity specification** — Humidity specification `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Method to specify the initial moist air humidity.

### **Initial relative humidity** — Relative humidity at the start of simulation `0.5` (default) | scalar in the range of [0,1]

Relative humidity in the moist air at the start of the simulation. The
relative humidity is the ratio of the water vapor partial pressure to
the water vapor saturation pressure, or the ratio of the water vapor
mole fraction to the water vapor mole fraction at saturation.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Relative
humidity`.

### **Initial relative humidity priority** — Relative humidity parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial relative
humidity** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Relative
humidity`.

### **Initial specific humidity** — Specific humidity at the start of simulation `0.01` (default) | scalar in the range of [0,1]

Specific humidity in the moist air at the start of simulation. The
specific humidity is the mass fraction of water vapor to the combined
total mass of water vapor, trace gas, and dry air.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Specific
humidity`.

### **Initial specific humidity priority** — Specific humidity parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial specific
humidity** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Specific
humidity`.

### **Initial water vapor mole fraction** — Mole fraction of water vapor at the start of simulation `0.01` (default) | scalar in the range [0,1]

Mole fraction of the water vapor in the moist air channel at the start
of simulation. The water vapor mole fraction is relative to the combined
molar quantity of water vapor, trace species, and dry air.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Mole
fraction`.

### **Initial water vapor mole fraction priority** — Water vapor mole fraction humidity parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial water vapor mole
fraction** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Mole
fraction`.

### **Initial humidity ratio** — Humidity ratio at the start of simulation `0.01` (default) | scalar in the range [0,1]

Humidity ratio in the moist air channel at the start of the
simulation. The humidity ratio is the ratio of the mass of water vapor
to the mass of dry air and trace gas.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Humidity
ratio`.

### **Initial humidity ratio priority** — Humidity ratio parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial humidity ratio
humidity** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Humidity
ratio`.

### **Initial wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | scalar in the range [0,1]

Wet-bulb temperature at the start of the simulation. The block uses
this value to calculate humidity.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Wet-bulb
temperature`.

### **Initial wet-bulb temperature priority** — Wet-bulb temperature parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial wet-bulb
temperature** parameter when initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Wet-bulb
temperature`.

### **Initial trace gas specification** — Measurement type of trace gas `Mass fraction` (default) | `Mole fraction`

Measurement type of trace gas.

### **Initial trace gas mass fraction** — Amount of trace gas in the moist air channel `0.001` (default) | scalar in the range [0,1]

Amount of trace gas in the moist air by mass fraction at the start of
the simulation. The mass fraction is relative to the combined total mass
of water vapor, trace gas, and dry air.

The block ignores this parameter if the **Trace gas
model** parameter in the Moist Air Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **Initial trace gas
specification** to `Mass
fraction`.

### **Initial trace gas mass fraction priority** — Trace gas mass fraction parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial trace gas mass
fraction priority** parameter when initializing the
block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, set **Initial trace gas
specification** to `Mass
fraction`.

### **Initial trace gas mole fraction** — Mole fraction of trace gas at the start of simulation `0.001` (default) | scalar in the range [0,1]

Amount of trace gas in the moist air channel by mole fraction at the
start of the simulation. The mole fraction is relative to the combined
molar total of water vapor, trace gas, and dry air.

The block ignores this parameter if the **Trace gas
model** parameter in the Moist Air Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **Initial trace gas
specification** to `Mole
fraction`.

### **Initial trace gas mole fraction priority** — Trace gas mole fraction parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial trace gas mole
fraction priority** parameter when initializing the
block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

#### Dependencies

To enable this parameter, set **Initial trace gas
specification** to `Mole
fraction`.

### **Initial mass ratio of water droplets to moist air** — Ratio of water droplets to moist air `0` (default) | positive scalar

Initial mass ratio of water droplets to moist air.

### **Initial mass ratio of water droplets to moist air priority** — Mass ratio of water droplets to moist air parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial mass ratio of
water droplets to moist air priority** parameter when
initializing the block.

Set this parameter to `High` to define your
initial conditions. You may need to set this parameter to
`Low` or `None` if
this initial condition conflicts with the initial conditions of another
block.

## Libraries

Simscape / Foundation Library / Moist Air / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: Updated options for initial conditions

You can now specify initial conditions for the block as parameters.

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To model water droplets, select **Enable entrained water droplets** in the Moist Air Properties (MA) block connected to your moist air network.

### R2024a: Numerical improvement for low-flow computation in pipes

To improve accuracy for pressure drop inside the pipe at low-speed flows, the
momentum balance computations in the Pipe (MA) block
have been changed slightly. There may be slight differences in simulation results
compared to previous releases, especially when Mach number is low.

### R2022b: Model effect of condensation on wall surface

The block has a new parameter, **Condensation on wall surface**,
that lets you model the effect of wall condensation on a cold pipe surface in
contact with a moist air volume. For more information, see Effect of Condensation on Wall Surface. In the
default configuration, with this parameter set to `Off`,
the block functions as in previous releases.

In R2023b, this parameter has been replaced with a check box. The default value
and block functionality are the same as in previous releases.

## Description

Rigid conduit for moist air flow

The Pipe (MA) block models pipe flow dynamics in a
moist air network due to viscous friction losses and convective heat transfer with the
pipe wall. The pipe contains a constant volume of moist air. The pressure and
temperature evolve based on the compressibility and thermal capacity of this moist air
volume. Liquid water condenses out of the moist air volume when it reaches saturation.
Choked flow occurs when the outlet reaches sonic condition.

**Caution**

Air flow through this block can choke. If a Mass Flow Rate Source
(MA) block or a Controlled Mass Flow Rate Source
(MA) block connected to the Pipe
(MA) block specifies a greater mass flow rate than the possible
choked mass flow rate, the simulation generates an error. For more information, see
Choked Flow.

The block equations use these symbols. Subscripts `a`,
`w`, `g`, and `d` indicate the
properties of dry air, water vapor, trace gas, and water droplets, respectively.
Subscript `ws` indicates water vapor at saturation. Subscripts
`A`, `H`, and `S` indicate the
appropriate port. Subscript `I` indicates the properties of the
internal moist air volume.

|  |  |
| --- | --- |
| m˙ | Mass flow rate |
| *Φ* | Energy flow rate |
| *Q* | Heat flow rate |
| *p* | Pressure |
| *ρ* | Density |
| *R* | Specific gas constant |
| *V* | Volume of moist air inside the converter |
| *c*p | Specific heat at constant volume |
| *h* | Specific enthalpy |
| *u* | Specific internal energy |
| *x* | Mass fraction (*x*w is specific humidity, which is another term for water vapor mass fraction) |
| *y* | Mole fraction |
| *φ* | Relative humidity |
| *r* | Humidity ratio |
| *r*d | Mass ratio of water droplets to moist air |
| *T* | Temperature |
| *t* | Time |

### Mass and Energy Balance

The net flow rates into the moist air volume inside the converter are

m˙net=m˙A−m˙condense+m˙wS+m˙gS+m˙d,evapΦnet=ΦA+QH+ΦS−(1−λd)m˙condensehdm˙w,net=m˙wA−m˙condense+m˙wS+m˙d,evapm˙g,net=m˙gA+m˙gSm˙d,net=m˙dA+m˙dS+λdm˙condense−m˙d,evap

where:

- m˙condense is the rate of
  condensation.
- m˙d,evap is the rate of water droplet
  evaporation.
- *Φ*condense is the rate of energy
  loss from the condensed water.
- *λd* is the value of the
  **Fraction of condensate entrained as water droplets**
  parameter.
- *Φ*S is the rate of energy added
  by the sources of moisture and trace gas. m˙wS and m˙gS are the mass flow rates of water and gas, respectively,
  through port **S**. The values of m˙wS, m˙gS, and *Φ*S are
  determined by the moisture and trace gas sources connected to port
  **S** of the converter.

Water vapor mass conservation relates the water vapor mass flow rate to the
dynamics of the humidity level in the internal moist air volume

dxwIdtρIV+xwIm˙net=m˙w,net

Similarly, trace gas mass conservation relates the trace gas mass flow rate to the
dynamics of the trace gas level in the internal moist air volume

dxgIdtρIV+xgIm˙net=m˙g,net

The water droplets mass conservation equation relates the water droplet mass flow
rate to the entrained water droplet dynamics in the internal moist air volume

drdIdtρIV+rdIm˙net=m˙d,net.

Mixture mass conservation relates the mixture mass flow rate to the dynamics of
the pressure, temperature, and mass fractions of the internal moist air
volume:

(1pIdpIdt−1TIdTIdt)ρIV+Ra−RwRI(m˙w,net−xwm˙net)+Ra−RgRI(m˙g,net−xgm˙net)+ρIV˙=m˙net

where V˙ is the rate of change of the converter volume.

Finally, energy conservation relates the energy flow rate to the dynamics of the
pressure, temperature, and mass fractions of the internal moist air volume:

(cpI−RI+rdcpd)VρIdTIdt+uaIm˙MA,net+(uwI−uaI)m˙w,net+(ugI−uaI)m˙g,net+hdm˙d,net=Φnet−pIV˙

The equation of state relates the mixture density to the pressure and temperature:

pI=ρIRITI

The mixture specific gas constant is

RI=xaIRa+xwIRw+xgIRg

### Momentum Balance

The momentum balance for each half of the pipe models the pressure drop due to
momentum flux and viscous friction:

pA−pI=(m˙AS)2⋅(TIpI−TApA)RI+ΔpAIpB−pI=(m˙BS)2⋅(TIpI−TBpB)RI+ΔpBI

where:

- *p* is the pressure at port **A**, port
  **B**, or internal node I, as indicated by the
  subscript.
- *ρ* is the density at port **A**, port
  **B**, or internal node I, as indicated by the
  subscript.
- *S* is the cross-sectional area of the pipe.
- *Δp*AI and
  *Δp*BI are pressure losses due
  to viscous friction.

The pressure losses due to viscous friction,
*Δp*AI and
*Δp*BI, depend on the flow regime. The
Reynolds numbers for each half of the pipe are defined as:

ReA=|m˙A|⋅DhS⋅μIReB=|m˙B|⋅DhS⋅μI

where:

- *D*h is the hydraulic diameter of
  the pipe.
- *μ*I is the dynamic viscosity at
  the internal node.

If the Reynolds number is less than the value of the **Laminar flow upper
Reynolds number limit** parameter, then the flow is in the laminar flow
regime. If the Reynolds number is greater than the value of the **Turbulent
flow lower Reynolds number limit** parameter, then the flow is in the
turbulent flow regime.

In the laminar flow regime, the pressure losses due to viscous friction
are:

ΔpAIlam=fshapem˙A⋅μI2ρI⋅Dh2⋅S⋅L+Leqv2ΔpBIlam=fshapem˙B⋅μI2ρI⋅Dh2⋅S⋅L+Leqv2

where:

- *f*shape is the value of the
  **Shape factor for laminar flow viscous friction**
  parameter.
- *L*eqv is the value of the
  **Aggregate equivalent length of local resistances**
  parameter.

In the turbulent flow regime, the pressure losses due to viscous friction
are:

ΔpAItur=fDarcyAm˙A⋅|m˙A|2ρI⋅Dh⋅S2⋅L+Leqv2ΔpBItur=fDarcyBm˙B⋅|m˙B|2ρI⋅Dh⋅S2⋅L+Leqv2

where *f*Darcy is the Darcy friction
factor at port **A** or **B**, as indicated by the
subscript.

The Darcy friction factors are computed from the Haaland correlation:

fDarcyA=[−1.8log10(6.9ReA+(εrough3.7Dh)1.11)]−2fDarcyB=[−1.8log10(6.9ReB+(εrough3.7Dh)1.11)]−2

where *ε*rough is the value of the
**Internal surface absolute roughness** parameter.

When the Reynolds number is between the **Laminar flow upper Reynolds
number limit** and the **Turbulent flow lower Reynolds number
limit** parameter values, the flow is in transition between laminar
flow and turbulent flow. The pressure losses due to viscous friction during the
transition region follow a smooth connection between those in the laminar flow
regime and those in the turbulent flow regime.

The heat exchanged with the pipe wall through port **H** is added
to the energy of the moist air volume represented by the internal node via the
energy conservation equation (see Mass and Energy Balance). Therefore,
the momentum balances for each half of the pipe, between port **A**
and the internal node and between port **B** and the internal node,
are assumed to be adiabatic processes. The adiabatic relations are:

hA−hI=(RIm˙AS)2[(TIpI)2−(TApA)2]hB−hI=(RIm˙BS)2[(TIpI)2−(TBpB)2]

where *h* is the specific enthalpy at port
**A**, port **B**, or internal node I, as
indicated by the subscript.

### Convective Heat Transfer

The convective heat transfer equation between the pipe wall and the internal moist
air volume is:

QH=Qconv+kISsurfDh(TH−TI)

*S*surf is the pipe surface area,
*S*surf =
4*S**L*/*D*h.
If **Condensation on wall surface** is off, and assuming an
exponential temperature distribution along the pipe, the convective heat transfer is

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

### Saturation and Condensation

The equations in this section account for the condensation that happens when the
volume of moist air becomes saturated. For additional equations that account for
wall surface condensation, when the **Condensation on wall
surface** check box is selected, see Effect of Condensation on Wall Surface.

When the moist air volume reaches saturation, condensation may occur. The specific
humidity at saturation is

xwsI=φwsRIRwpwsIpI

where:

- *φ*ws is the relative humidity at
  saturation (typically 1).
- *p*wsI is the water vapor saturation
  pressure evaluated at *T*I.

The rate of condensation is

m˙condense={0,if xwI≤xwsIxwI−xwsIτcondenseρIV,if xwI>xwsI

where *τ*condense is the value of the
**Water vapor condensation time constant** parameter.

The rate of evaporation is

m˙d,evap=xwsI−xwIxwsIτevaprdIρIV,

where *τ*evap is the value of the **Water
droplets evaporation time constant** parameter.

### Effect of Condensation on Wall Surface

Moist air blocks that contain an internal volume of fluid (such as chambers,
converters, and so on) model water vapor condensation when this volume of fluid
becomes fully saturated with water vapor, that is, at 100% relative humidity.
However, water vapor can also condense on a cold surface even if the volume of air
as a whole has not yet reached saturation. The ability to model this effect in
Pipe (MA) blocks is important because many HVAC
systems contain pipes and ducts. If these pipes and ducts are not well insulated,
their surface could get cold, and condensation on wall surface occurs. Note that
this effect does not replace the condensation that occurs when the bulk moist air
volume reaches 100% relative humidity, both effects can occur simultaneously.

To model the effect of wall condensation on a cold pipe surface in contact with a
moist air volume, select the **Condensation on wall surface** check
box. In this case, the convective heat transfer equation needs to account for both
sensible and latent heat, and the block has an additional equation that calculates
the rate of water vapor condensation on the surface.

If **Condensation on wall surface** is on, the combined
convective heat transfer is

Qcombinedconv=|m˙ag|(h¯H−h¯in)(1−exp(−hcoeffSsurf|m˙avg|cpavg))

where:

- m˙ag is the mass flow rate of dry air and trace gas at the
  inlet.
- h¯H is the mixture enthalpy per unit mass of dry air and trace
  gas at the wall.
- h¯in is the mixture enthalpy per unit mass of dry air and trace
  gas at the inlet.

This equation is similar to the equation in Convective Heat Transfer, but the
temperature difference has been replaced by the mixture enthalpy difference. Because
the mixture enthalpy depends on both the temperature and the composition of the
moist air, the mixture enthalpy difference accounts for both a change in temperature
and a change in the moisture content. In other words, it captures both sensible and
latent heat effects. The exponent term and the correlations that go into computing
the heat transfer coefficient remain the same as before because the model is derived
based on the analogy between heat and mass transfer. For more information, see [3].

To simplify the derivations, the equation uses the mixture enthalpy per unit mass
of dry air and trace gas, as opposed to the mixture enthalpy per unit mass of the
mixture, because the amount of dry air and trace gas does not change during the
water vapor condensation process. To ensure that the equation remains consistent,
the mixture enthalpy difference is multiplied by the mass flow rate of dry air and
trace gas, m˙ag, as opposed to the total mixture mass flow rate, m˙.

The mixture enthalpy per unit mass of dry air and trace gas at the inlet is

h¯in=hagin+Winhwin

where:

- hagin is the specific enthalpy of dry air and trace gas at the
  inlet.
- hwin is the specific enthalpy of water vapor at the
  inlet.
- *W*in is the humidity ratio at the
  inlet.

The mixture enthalpy per unit mass of dry air and trace gas at the wall is

h¯H=hagH+WHhwH

where:

- hagH is the specific enthalpy of dry air and trace gas at the
  wall.
- hwH is the specific enthalpy of water vapor at the
  wall.
- *W*H is the humidity ratio at the
  wall, defined as

  WH=min{Win,WsH}

  where *W*sH is the saturation
  humidity ratio based on the wall temperature.

The `min` function in the previous equation provides the switch
between “dry” and “wet” heat transfer:

- When the wall temperature is above the dew point, then
  *W*sH >
  *W*in, therefore, condensation
  is not occurring and (h¯H−h¯in) represents difference in temperature only.
- When the wall temperature is below the dew point, then
  *W*sH <
  *W*in, therefore, condensation
  is occurring and (h¯H−h¯in) represents difference in both temperature and humidity
  content.

The rate of water vapor condensation on the wall surface is

m˙condenseH=|m˙ag|(Win−WH)(1−exp(−hcoeffSsurf|m˙avg|cpavg))

This equation is similar to the combined convective heat transfer equation because
the amount of water vapor condensing on the wall is the same as the convective mass
transfer from the moist air to the pipe wall. The exponent term is also the same
because of the heat and mass transfer analogy used. For more information, see [3].

The energy associated with the water condensed on the pipe wall is

ΦcondenseH=m˙condenseH(hwH−ΔhvapH)

where *Δh*vapH is the specific enthalpy of
vaporization at the wall temperature.

The sensible portion of the convective heat transfer between the pipe wall and the
moist air is

Qconv=Qcombinedconv+ΦcondenseH

This equation has a plus sign because *Q* is negative when it is
cooling the moist air. Therefore, adding ΦcondenseH, which is a positive value, removes the latent portion of the heat
transfer.

The block then uses this *Q*conv value in
the first equation in Convective Heat Transfer to calculate
the heat transfer at thermal port **H**.

### Choked Flow

The unchoked pressure at port **A** or **B** is
the value of the corresponding Across variable at that port:

pAunchoked=A.ppBunchoked=B.p

However, the port pressure variables used in the momentum balance equations,
*p*A and
*p*B, do not necessarily coincide with
the pressure across variables `A.p` and `B.p`
because the pipe outlet may choke. Choked flow occurs when the downstream pressure
is sufficiently low. At that point, the flow depends only on the conditions at the
inlet. Therefore, when choked, the outlet pressure
(*p*A or
*p*B, whichever is the outlet) cannot
decrease further even if the pressure downstream, represented by
`A.p` or `B.p`, continues to decrease.

Choking can occur at the pipe outlet, but not at the pipe inlet. Therefore, if
port **A** is the inlet, then
*p*A = `A.p`. If port
**A** is the outlet, then

pA={A.p,if A.p≥pAchokedpAchoked,if A.p<pAchoked

Similarly, if port **B** is the inlet, then
*p*B = `B.p`. If port
**B** is the outlet, then

pB={B.p,if B.p≥pBchokedpBchoked,if B.p<pBchoked

The choked pressures at ports **A** and **B**
are derived from the momentum balance by assuming the outlet velocity is equal to
the speed of sound:

pAchoked−pI=pAchoked(pAchokedTIpITA−1)cpAcvI+ΔpAIpBchoked−pI=pBchoked(pBchokedTIpITB−1)cpBcvI+ΔpBI

### Assumptions and Limitations

- The pipe wall is perfectly rigid.
- The flow is fully developed. Friction losses and heat transfer do not
  include entrance effects.
- The effect of gravity is negligible.
- Fluid inertia is negligible.
- This block does not model supersonic flow.
- The equations for wall condensation are based on the analogy between heat
  and mass transfer, and are therefore valid only when the Lewis number (Le)
  is close to 1. This is a reasonable assumption for a moist air mixture. For
  more information, see [3].
