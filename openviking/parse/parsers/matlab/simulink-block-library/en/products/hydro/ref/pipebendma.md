---
type: simulink-block
title: 'Pipe Bend (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Pipes and Fittings'
documentation_page: 'pipebendma'
documentation_source_path: 'ref/pipebendma.html'
language: en
---

# Pipe Bend (MA)

## Ports

### Conserving

### **A** — Liquid port moist air

Moist air conserving port associated with the liquid entry or exit port.

### **B** — Liquid port moist air

Moist air conserving port associated with the liquid entry or exit port.

## Parameters

### Main

### **Pipe diameter** — Pipe diameter `0.01 m` (default) | positive scalar

Diameter of the pipe.

### **Bend radius** — Bend circle radius `0.04 m` (default) | positive scalar

Radius of the circle formed by the pipe bend.

### **Bend angle** — Bend angle `90 deg` (default) | positive scalar

Swept degree of the pipe bend.

### **Internal surface absolute roughness** — Pipe wall roughness `15e-6 m` (default) | positive scalar

Pipe wall absolute roughness. The block uses this parameter to determine the Darcy
friction factor, which contributes to pressure loss in the pipe.

### Effects and Initial Conditions

### **Initial pressure** — Moist air pressure at the start of simulation `0.101325 MPa` (default) | positive scalar

Moist air pressure at the start of the simulation.

### **Initial pressure priority** — Pressure parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial pressure** parameter
when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

### **Initial temperature** — Temperature at the start of simulation `293.15 K` (default) | positive scalar

Initial moist air temperature.

### **Initial temperature priority** — Temperature parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial temperature**
parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

### **Initial humidity specification** — Humidity specification `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Method to specify the initial moist air humidity.

### **Initial relative humidity** — Relative humidity at the start of simulation `0.5` (default) | scalar in the range of [0,1]

Relative humidity in the moist air at the start of the simulation. The relative
humidity is the ratio of the water vapor partial pressure to the water vapor
saturation pressure, or the ratio of the water vapor mole fraction to the water vapor
mole fraction at saturation.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Relative humidity`.

### **Initial relative humidity priority** — Relative humidity parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial relative humidity**
parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Relative humidity`.

### **Initial specific humidity** — Specific humidity at the start of simulation `0.01` (default) | scalar in the range of [0,1]

Specific humidity in the moist air at the start of simulation. The specific
humidity is the mass fraction of water vapor to the combined total mass of water
vapor, trace gas, and dry air.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Specific humidity`.

### **Initial specific humidity priority** — Specific humidity parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial specific humidity**
parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Specific humidity`.

### **Initial water vapor mole fraction** — Mole fraction of water vapor at the start of simulation `0.01` (default) | scalar in the range [0,1]

Mole fraction of the water vapor in the moist air channel at the start of
simulation. The water vapor mole fraction is relative to the combined molar quantity
of water vapor, trace species, and dry air.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Mole fraction`.

### **Initial water vapor mole fraction priority** — Water vapor mole fraction humidity parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial water vapor mole
fraction** parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Mole fraction`.

### **Initial humidity ratio** — Humidity ratio at the start of simulation `0.01` (default) | scalar in the range [0,1]

Humidity ratio in the moist air channel at the start of the simulation. The
humidity ratio is the ratio of the mass of water vapor to the mass of dry air and
trace gas.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Humidity ratio`.

### **Initial humidity ratio priority** — Humidity ratio parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial humidity ratio
humidity** parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Humidity ratio`.

### **Initial wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | scalar in the range [0,1]

Wet-bulb temperature at the start of the simulation. The block uses this value to
calculate moisture.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Wet-bulb
temperature`.

### **Initial wet-bulb temperature priority** — Wet-bulb temperature parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial wet-bulb
temperature** parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

#### Dependencies

To enable this parameter, set **Initial humidity
specification** to `Wet-bulb
temperature`.

### **Initial trace gas specification** — Measurement type of trace gas `Mass fraction` (default) | `Mole fraction`

Measurement type of trace gas.

### **Initial trace gas mass fraction** — Amount of trace gas in the moist air channel `0.001` (default) | scalar in the range [0,1]

Amount of trace gas in the moist air by mass fraction at the start of the
simulation. The mass fraction is relative to the combined total mass of water vapor,
trace gas, and dry air.

The block ignores this parameter if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **Initial trace gas
specification** to `Mass fraction`.

### **Initial trace gas mass fraction priority** — Trace gas mass fraction parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial trace gas mass fraction
priority** parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

#### Dependencies

To enable this parameter, set **Initial trace gas
specification** to `Mass fraction`.

### **Initial trace gas mole fraction** — Mole fraction of trace gas at the start of simulation `0.001` (default) | scalar in the range [0,1]

Amount of trace gas in the moist air channel by mole fraction at the start of the
simulation. The mole fraction is relative to the combined molar total of water vapor,
trace gas, and dry air.

The block ignores this parameter if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is
`None`.

#### Dependencies

To enable this parameter, set **Initial trace gas
specification** to `Mole fraction`.

### **Initial trace gas mole fraction priority** — Trace gas mole fraction parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial trace gas mole fraction
priority** parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

#### Dependencies

To enable this parameter, set **Initial trace gas
specification** to `Mole fraction`.

### **Initial mass ratio of water droplets to moist air** — Ratio of water droplets to moist air `0` (default) | positive scalar

Initial mass ratio of water droplets to moist air.

### **Initial mass ratio of water droplets to moist air priority** — Mass ratio of water droplets to moist air parameter priority `High` (default) | `Low` | `None`

Priority the solver assigns to the **Initial mass ratio of water droplets
to moist air priority** parameter when initializing the block.

Set this parameter to `High` to define your initial
conditions. You may need to set this parameter to `Low` or
`None` if this initial condition conflicts with the initial
conditions of another block.

### **Relative humidity at saturation** — Relative humidity point of condensation `1` (default) | scalar in the range [0,1]

Relative humidity point of condensation. Condensation occurs above this value. A
value greater than 1 indicates a supersaturated vapor.

### **Water vapor condensation time constant** — Time scale for condensation `1e-3 s` (default) | positive scalar

Characteristic time scale at which an oversaturated moist air volume returns to
saturation by condensing out excess moisture.

### **Water droplets evaporation time constant** — Time scale for evaporation `1e-3 s` (default) | positive scalar

Characteristic time scale at which water droplets evaporate to vapor.

### **Fraction of condensate entrained as water droplets** — Fraction of condensate in water droplets `1` (default) | scalar in the range [0,1]

Fraction of the condensate in the moist air that is entrained as water
droplets.

## Libraries

Simscape / Fluids / Moist Air / Pipes & Fittings

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the
moist air domain can now model water droplets suspended in a moist air flow. To model water
droplets, select **Enable entrained water droplets** in the Moist Air Properties
(MA) block connected to your moist air network.

### R2024b: Updated options for initial conditions

You can now specify initial conditions for the block as
parameters.

## Description

Pipe bend segment in a moist air network

The Pipe Bend (MA) block represents a curved pipe in a moist air network. You can define
the pipe characteristics to calculate losses due to friction and pipe curvature. The block
models losses with hydraulic loss coefficients and the results may be more accurate for lower
speed flows where you can neglect compressible flow effects.

### Pipe Curvature Loss Coefficient

The coefficient for pressure losses due to geometry changes comprises an angle
correction factor, *Cangle*, and a bend coefficient,
*Cbend*:

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
*fT*, for clean commercial steel from tabular data
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

### Mass and Energy Balance

The net flow rates into the moist air volume inside the pipe bend are

m˙total=m˙A+m˙B-m˙w,cond-m˙w,conv+m˙d,evapm˙w,total=m˙wA+m˙wB-m˙w,cond-m˙w,conv+m˙d,evapm˙g,total=m˙gA+m˙gBm˙d,total=m˙dA+m˙dB+λd(m˙w,cond+m˙w,conv)-m˙d,evap

where:

- m˙ is the mass flow rate. The subscript *w* denotes
  water vapor, the subscript *g* denotes trace gas, and the subscript
  *d* denotes water droplets.
- *λd* is the value of the **Fraction
  of condensate entrained as water droplets** parameter.
- m˙w,cond is the rate of water vapor condensation
  due to a saturated fluid volume.
- m˙w,conv is the rate of condensation on the wall
  surface.
- m˙d,evap is the rate of water droplet
  evaporation.
- *Φ* is the energy flow rate.

The mass conservation equations for the mixture relate the pressure, temperature, and
internal moist air volume mass fractions

(1pIdpIdt−1TIdTIdt)ρIV+Ra−RwRI(m˙w,total−xwm˙total)+Ra−RgRI(m˙g,total−xgm˙total)=m˙total,

where:

- *pI* is the pressure of the internal volume.
- *ρI* is the density of the internal volume.
- *TI* is the temperature of the internal
  volume.
- *V* is the volume.
- *Ra*,
  *Rg*,
  *Rw*, and
  *RI* are the specific gas constants of the
  air, gas, water vapor, and internal volume, respectively.
- *xw* is the specific humidity.
- *xg* is the trace gas mass fraction.

The energy conservation equation relates the energy flow rate to the pressure,
temperature, and internal moist air volume mass fractions

(cpI−RI+rdcpdI)VρIdTIdt+uaIm˙MA,total+(uwI−uaI)m˙w,total+(ugI−uaI)m˙g,total+hdIm˙d,total=     ϕA+ϕB−(1−λd)(m˙w,condhdI),

where:

- *uI* is the internal energy.
- *cpI* is the specific heat.
- *rd* is the mass ratio of water droplets
  to moist air.
- *cpdI* is the water
  droplet specific heat.
- m˙d,total is the total water droplet mass flow rate.
- *hdI* is the water droplet specific
  enthalpy.
- *ϕA* is the energy flow rate at port
  **A**.
- *ϕB* is the energy flow rate at port
  **B**.
- m˙w,cond is the rate of water vapor condensation
  due to a saturated fluid volume.
- *λd* is the value of the
  **Fraction of condensate entrained as water droplets**
  parameter.
- *ϕA* is the energy flow rate at port
  **A**.
- *ϕB* is the energy flow rate at port
  **B**.

The mass conservation equation for the water droplets relates the water vapor mass flow
rate to the internal moist air volume moisture level

dxwIdtρIV+xwIm˙total=m˙w,total.

The trace gas mass conservation equation relates the trace gas mass flow rate to the
internal moist air volume trace gas level

dxgIdtρIV+xgIm˙total=m˙g,total.

The water droplets mass conservation equation relates the water droplet mass flow rate
to the entrained water droplet dynamics in the internal moist air volume

drdIdtρIV+rdIm˙total=m˙d,total.
