---
type: simulink-block
title: 'Rotational Mechanical Converter (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'rotationalmechanicalconverterma'
documentation_source_path: 'ref/rotationalmechanicalconverterma.html'
language: en
---

# Rotational Mechanical Converter (MA)

## Ports
```yaml
ports:
- name: q
  summary: Rotation of port R relative to port C, rad physical signal
  direction: input
- name: W
  summary: Rate of condensation leaving system, kg/s physical signal
  direction: output
- name: F
  summary: Vector physical signal containing pressure, temperature, humidity, and trace gas levels data physical signal vector
  direction: output
- name: A
  summary: Converter inlet moist air
  direction: conserving
- name: H
  summary: Temperature inside converter thermal
  direction: conserving
- name: R
  summary: Rod mechanical rotational
  direction: conserving
- name: C
  summary: Case mechanical rotational
  direction: conserving
- name: S
  summary: Inject or extract moisture and trace gas moist air source
  direction: conserving
```

### Input

### **q** — Rotation of port R relative to port C, rad physical signal

Input physical signal that passes the position information from a
Simscape™
Multibody™ joint. Connect this port to the position sensing port
**q** of the joint. For more information, see Connecting Simscape Networks to Simscape Multibody Joints.

#### Dependencies

To enable this port, set the **Interface
rotation** parameter to `Provide input
signal from Multibody joint`.
### Output

### **W** — Rate of condensation leaving system, kg/s physical signal

Physical signal output port that measures the rate of condensation
that leaves the system. This value does not include the portion of
condensation that is entrained as water droplets.

### **F** — Vector physical signal containing pressure, temperature, humidity, and trace gas levels data physical signal vector

Physical signal output port that outputs a vector signal. The vector
contains the pressure (in Pa), temperature (in K), moisture level, and
trace gas level measurements inside the component. Use the
Measurement Selector (MA) block to unpack this
vector signal.
### Conserving

### **A** — Converter inlet moist air

Moist air conserving port associated with the converter inlet.

### **H** — Temperature inside converter thermal

Thermal conserving port associated with the temperature of the moist
air mixture inside the converter.

### **R** — Rod mechanical rotational

Mechanical rotational conserving port associated with the moving
interface.

### **C** — Case mechanical rotational

Mechanical rotational conserving port associated with the converter
casing.

### **S** — Inject or extract moisture and trace gas moist air source

Connect this port to port **S** of a block from the
Moisture & Trace Gas Sources library to add or remove moisture and
trace gas. For more information, see Using Moisture and Trace Gas Sources.

#### Dependencies

This port is visible only if you set the **Moisture and
trace gas source** parameter to
`Controlled`.
## Parameters
```yaml
parameters:
- name: Mechanical orientation
  summary: Select the converter orientation Pressure at A causes positive rotation of R relative to C (default) | Pressure
    at A causes negative rotation of R relative to C
  group: Main
- name: Interface rotation
  summary: Select method to determine relative port positions Calculate from angular velocity of port R relative to port C
    (default) | Provide input signal from Multibody joint
  group: Main
- name: Initial interface rotation
  summary: Rotational offset of port R relative to port C at the start of simulation 0 m (default)
  group: Main
- name: Interface volume displacement
  summary: Displaced moist air volume per unit rotation 0.01 m^3/rad (default)
  group: Main
- name: Dead volume
  summary: Volume of moist air when the interface rotation is 0 1e-5 m^3 (default)
  group: Main
- name: Cross-sectional area at port A
  summary: Area normal to flow path at the converter inlet 0.01 m^2 (default)
  group: Main
- name: Environment pressure specification
  summary: Select a specification method for the environment pressure Atmospheric pressure (default) | Specified pressure
  group: Main
- name: Environment pressure
  summary: Pressure outside the converter 0.101325 MPa (default)
  group: Main
- name: Relative humidity at saturation
  summary: Relative humidity above which condensation occurs 1 (default)
  group: Moisture and Trace Gas
- name: Water vapor condensation time constant
  summary: Time scale for condensation 1e-3 s (default) | positive scalar
  group: Moisture and Trace Gas
- name: Water droplets evaporation time constant
  summary: Time scale for evaporation 1e-3 s (default) | positive scalar
  group: Moisture and Trace Gas
- name: Fraction of condensate entrained as water droplets
  summary: Fraction of condensate in water droplets 1 (default) | scalar in the range [0,1]
  group: Moisture and Trace Gas
- name: Moisture and trace gas source
  summary: Model moisture and trace gas levels None (default) | Constant | Controlled
  group: Moisture and Trace Gas
- name: Moisture added or removed
  summary: Select whether the block adds or removes moisture as water vapor or water droplets Water vapor (default) | Water
    droplets
  group: Moisture and Trace Gas
- name: Water vapor evaporated from liquid or condensed to liquid
  summary: How the block adds or removes water vapor off (default) | on
  group: Moisture and Trace Gas
- name: Rate of moisture added
  summary: Constant mass flow rate through the block 0 kg/s (default)
  group: Moisture and Trace Gas
- name: Added moisture temperature specification
  summary: Select specification method for the temperature of added moisture Atmospheric temperature (default) | Specified
    temperature
  group: Moisture and Trace Gas
- name: Temperature of added moisture
  summary: Moisture temperature 293.15 K (default)
  group: Moisture and Trace Gas
- name: Rate of trace gas added
  summary: Constant mass flow rate through the block 0 kg/s (default)
  group: Moisture and Trace Gas
- name: Added trace gas temperature specification
  summary: Select specification method for the temperature of added trace gas Atmospheric temperature (default) | Specified
    temperature
  group: Moisture and Trace Gas
- name: Temperature of added trace gas
  summary: Trace gas temperature 293.15 K (default)
  group: Moisture and Trace Gas
- name: Initial pressure
  summary: Moist air pressure at the start of simulation 0.101325 MPa (default) | positive scalar
  group: Initial Conditions
- name: Initial pressure priority
  summary: Pressure parameter priority High (default) | Low | None
  group: Initial Conditions
- name: Initial temperature
  summary: Temperature at the start of simulation 293.15 K (default) | positive scalar
  group: Initial Conditions
- name: Initial temperature priority
  summary: Temperature parameter priority High (default) | Low | None
  group: Initial Conditions
- name: Initial humidity specification
  summary: Humidity specification Relative humidity (default) | Specific humidity | Mole fraction | Humidity ratio | Wet-bulb
    temperature
  group: Initial Conditions
- name: Initial relative humidity
  summary: Relative humidity at the start of simulation 0.5 (default) | scalar in the range of [0,1]
  group: Initial Conditions
- name: Initial relative humidity priority
  summary: Relative humidity parameter priority High (default) | Low | None
  group: Initial Conditions
- name: Initial specific humidity
  summary: Specific humidity at the start of simulation 0.01 (default) | scalar in the range of [0,1]
  group: Initial Conditions
- name: Initial specific humidity priority
  summary: Specific humidity parameter priority High (default) | Low | None
  group: Initial Conditions
- name: Initial water vapor mole fraction
  summary: Mole fraction of water vapor at the start of simulation 0.01 (default) | scalar in the range [0,1]
  group: Initial Conditions
- name: Initial water vapor mole fraction priority
  summary: Water vapor mole fraction humidity parameter priority High (default) | Low | None
  group: Initial Conditions
- name: Initial humidity ratio
  summary: Humidity ratio at the start of simulation 0.01 (default) | scalar in the range [0,1]
  group: Initial Conditions
- name: Initial humidity ratio priority
  summary: Humidity ratio parameter priority High (default) | Low | None
  group: Initial Conditions
- name: Initial wet-bulb temperature
  summary: Wet-bulb temperature at the start of simulation 287 K (default) | scalar in the range [0,1]
  group: Initial Conditions
- name: Initial wet-bulb temperature priority
  summary: Wet-bulb temperature parameter priority High (default) | Low | None
  group: Initial Conditions
- name: Initial trace gas specification
  summary: Measurement type of trace gas Mass fraction (default) | Mole fraction
  group: Initial Conditions
- name: Initial trace gas mass fraction
  summary: Amount of trace gas in the moist air channel 0.001 (default) | scalar in the range [0,1]
  group: Initial Conditions
- name: Initial trace gas mass fraction priority
  summary: Trace gas mass fraction parameter priority High (default) | Low | None
  group: Initial Conditions
- name: Initial trace gas mole fraction
  summary: Mole fraction of trace gas at the start of simulation 0.001 (default) | scalar in the range [0,1]
  group: Initial Conditions
- name: Initial trace gas mole fraction priority
  summary: Trace gas mole fraction parameter priority High (default) | Low | None
  group: Initial Conditions
- name: Initial mass ratio of water droplets to moist air
  summary: Ratio of water droplets to moist air 0 (default) | positive scalar
  group: Initial Conditions
- name: Initial mass ratio of water droplets to moist air priority
  summary: Mass ratio of water droplets to moist air parameter priority High (default) | Low | None
  group: Initial Conditions
```

### Main

### **Mechanical orientation** — Select the converter orientation `Pressure at A causes positive rotation of R relative to C` (default) | `Pressure at A causes negative rotation of R relative to C`

Select the alignment of moving interface with respect to the volume of
moist air inside the converter:

- `Pressure at A causes positive rotation of R
  relative to C` — Increase in the moist
  air volume results in a positive rotation of port
  **R** relative to port
  **C**.
- `Pressure at A causes negative rotation of R
  relative to C` — Increase in the moist
  air volume results in a negative rotation of port
  **R** relative to port
  **C**.

### **Interface rotation** — Select method to determine relative port positions `Calculate from angular velocity of port R relative to port C` (default) | `Provide input signal from Multibody joint`

Select method to determine rotation of port **R**
relative to port **C**:

- `Calculate from angular velocity of port R
  relative to port C` — Calculate rotation
  from relative port angular velocities, based on the block
  equations. This is the default method.
- `Provide input signal from Multibody
  joint` — Enable the input physical
  signal port **q** to pass the rotation
  information from a Multibody joint. Use this method only when
  you connect the converter to a Multibody joint by using a
  Rotational Multibody
  Interface block. For more information, see
  How to Pass Position Information.

### **Initial interface rotation** — Rotational offset of port R relative to port C at the start of simulation `0 m` (default)

Rotational offset of port **R** relative to port
**C** at the start of simulation. A value of 0
corresponds to an initial moist air volume equal to **Dead
volume**.

#### Dependencies

Enabled when the **Interface rotation** parameter
is set to `Calculate from angular velocity of port R
relative to port C`.

- If **Mechanical orientation** is
  `Pressure at A causes positive rotation of R
  relative to C`, the parameter value must be
  greater than or equal to 0.
- If **Mechanical orientation** is
  `Pressure at A causes negative rotation of R
  relative to C`, the parameter value must be
  less than or equal to 0.

### **Interface volume displacement** — Displaced moist air volume per unit rotation `0.01 m^3/rad` (default)

Displaced moist air volume per unit rotation of the moving
interface.

### **Dead volume** — Volume of moist air when the interface rotation is 0 `1e-5 m^3` (default)

Volume of moist air when the interface rotation is 0.

### **Cross-sectional area at port A** — Area normal to flow path at the converter inlet `0.01 m^2` (default)

Cross-sectional area of the converter inlet, in the direction normal
to the moist air flow path.

### **Environment pressure specification** — Select a specification method for the environment pressure `Atmospheric pressure` (default) | `Specified pressure`

Select a specification method for the environment pressure:

- `Atmospheric pressure` — Use
  the atmospheric pressure, specified by the Moist
  Air Properties (MA) block connected to the
  circuit.
- `Specified pressure` — Specify
  a value by using the **Environment pressure**
  parameter.

### **Environment pressure** — Pressure outside the converter `0.101325 MPa` (default)

Pressure outside the converter acting against the pressure of the
converter moist air volume. A value of 0 indicates that the converter
expands into vacuum.

#### Dependencies

Enabled when the **Environment pressure
specification** parameter is set to
`Specified pressure`.

### Moisture and Trace Gas

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

## Description

Interface between moist air and mechanical rotational networks

The Rotational Mechanical Converter (MA) block models
an interface between a moist air network and a mechanical rotational network. The block
converts moist air pressure into mechanical torque and vice versa. You can use it as a
building block for rotary actuators.

The converter contains a variable volume of moist air. The pressure and temperature
evolve based on the compressibility and thermal capacity of this moist air volume.
Liquid water condenses out of the moist air volume when it reaches saturation. The
**Mechanical orientation** parameter lets you specify whether an
increase in the moist air volume inside the converter results in a positive or negative
rotation of port **R** relative to port **C**.

The block equations use these symbols. Subscripts `a`,
`w`, `g`, and `d` indicate the
properties of dry air, water vapor, trace gas, and water droplets, respectively. Subscript
`ws` indicates water vapor at saturation. Subscripts
`A`, `H`, and `S` indicate the
appropriate port. Subscript `I` indicates the properties of the internal
moist air volume.

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

The net flow rates into the moist air volume inside the converter are

m˙net=m˙A−m˙condense+m˙wS+m˙gS+m˙d,evapΦnet=ΦA+QH+ΦS−(1−λd)m˙condensehdm˙w,net=m˙wA−m˙condense+m˙wS+m˙d,evapm˙g,net=m˙gA+m˙gSm˙d,net=m˙dA+m˙dS+λdm˙condense−m˙d,evap

where:

- m˙condense is the rate of condensation.
- m˙d,evap is the rate of water droplet
  evaporation.
- *Φ*condense is the rate of energy loss
  from the condensed water.
- *λd* is the value of the
  **Fraction of condensate entrained as water droplets**
  parameter.
- *Φ*S is the rate of energy added by the
  sources of moisture and trace gas. m˙wS and m˙gS are the mass flow rates of water and gas, respectively, through
  port **S**. The values of m˙wS, m˙gS, and *Φ*S are determined
  by the moisture and trace gas sources connected to port **S** of
  the converter.

Water vapor mass conservation relates the water vapor mass flow rate to the dynamics of
the humidity level in the internal moist air volume

dxwIdtρIV+xwIm˙net=m˙w,net

Similarly, trace gas mass conservation relates the trace gas mass flow rate to the
dynamics of the trace gas level in the internal moist air volume

dxgIdtρIV+xgIm˙net=m˙g,net

The water droplets mass conservation equation relates the water droplet mass flow rate to
the entrained water droplet dynamics in the internal moist air volume

drdIdtρIV+rdIm˙net=m˙d,net.

Mixture mass conservation relates the mixture mass flow rate to the dynamics of the
pressure, temperature, and mass fractions of the internal moist air volume:

(1pIdpIdt−1TIdTIdt)ρIV+Ra−RwRI(m˙w,net−xwm˙net)+Ra−RgRI(m˙g,net−xgm˙net)+ρIV˙=m˙net

where V˙ is the rate of change of the converter volume.

Finally, energy conservation relates the energy flow rate to the dynamics of the pressure,
temperature, and mass fractions of the internal moist air volume:

(cpI−RI+rdcpd)VρIdTIdt+uaIm˙MA,net+(uwI−uaI)m˙w,net+(ugI−uaI)m˙g,net+hdm˙d,net=Φnet−pIV˙

The equation of state relates the mixture density to the pressure and temperature:

pI=ρIRITI

The mixture specific gas constant is

RI=xaIRa+xwIRw+xgIRg

The converter volume depends on the rotation of the moving interface:

V=Vdead+Dintθintεint

where:

- *V*dead is the dead volume.
- *D*int is the interface volume
  displacement.
- *θ*int is the interface
  rotation.
- *ε*int is the mechanical orientation
  coefficient. If **Mechanical orientation** is
  `Pressure at A causes positive rotation of R relative to
  C`, *ε*int = 1. If **Mechanical orientation** is
  `Pressure at A causes negative rotation of R relative to
  C`, *ε*int = –1.

If you connect the converter to a Multibody joint, use the physical signal input port
**q** to specify the rotation of port **R**
relative to port **C**. Otherwise, the block calculates the interface
rotation from relative port angular velocities. The interface rotation is zero when the
moist air volume inside the converter is equal to the dead volume. Then, depending on
the **Mechanical orientation** parameter value:

- If `Pressure at A causes positive rotation of R relative to
  C`, the interface rotation increases when the moist air volume
  increases from dead volume.
- If `Pressure at A causes negative rotation of R relative to
  C`, the interface rotation decreases when the moist air volume
  increases from dead volume.

The torque balance on the mechanical interface is

τint=(penv−pI)Dintεint

where:

- *τ*int is the torque from port
  **R** to port **C**.
- *p*env is the environment pressure.

Flow resistance and thermal resistance are not modeled in the converter:

pA=pITH=TI

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

### Assumptions and Limitations

- The converter casing is perfectly rigid.
- Flow resistance between the converter inlet and the moist air volume
  is not modeled. Connect a Local Restriction
  (MA) block or a Flow Resistance
  (MA) block to port **A** to model
  pressure losses associated with the inlet.
- Thermal resistance between port **H** and the moist
  air volume is not modeled. Use Thermal library blocks to model thermal
  resistances between the moist air mixture and the environment, including
  any thermal effects of a chamber wall.
- The moving interface is perfectly sealed.
- The block does not model the mechanical effects of the moving
  interface, such as hard stops, friction, and inertia.
