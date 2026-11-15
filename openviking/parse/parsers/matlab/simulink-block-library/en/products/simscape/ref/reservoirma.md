---
type: simulink-block
title: 'Reservoir (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Moist Air Models / Elements'
documentation_page: 'reservoirma'
documentation_source_path: 'ref/reservoirma.html'
language: en
---

# Reservoir (MA)

## Ports

### Input

### **P** — Reservoir pressure, Pa physical signal

Physical signal port that controls the reservoir pressure.

#### Dependencies

To enable this port, select **Provide input signal for
pressure**.

### **T** — Reservoir temperature, K physical signal

Physical signal port that controls the reservoir temperature.

#### Dependencies

To enable this port, select **Provide input signal for
temperature**.

### **W** — Reservoir humidity, unitless physical signal

Physical signal port that controls the reservoir humidity level. To
select the quantity that the control signal represents, use the
**Reservoir humidity specification**
parameter.

#### Dependencies

To enable this port, select **Provide input signal for
humidity** and set the **Reservoir humidity
specification** parameter to one of theses
options:

- `Relative humidity`
- `Specific humidity`
- `Mole fraction`
- `Humidity ratio`

### **Tw** — Reservoir wet-bulb temperature, K physical signal

Physical signal port that controls the reservoir wet-bulb temperature.

#### Dependencies

To enable this port, select **Provide input signal for
humidity** and set the **Reservoir humidity
specification** parameter to `Wet-bulb
temperature`.

### **G** — Reservoir trace gas level, unitless physical signal

Physical signal port that controls the reservoir trace gas level. To
select the quantity that the control signal represents, use the
**Reservoir trace gas specification**
parameter.

#### Dependencies

To enable this port, select **Provide input signal for
trace gas**.

### **D** — Reservoir water droplet mass ratio, unitless physical signal

Physical signal port that controls the reservoir mass ratio of water
droplets to moist air.

#### Dependencies

To enable this port, select **Provide input signal for
water droplets**.
### Conserving

### **A** — Reservoir inlet moist air

Moist air conserving port associated with the reservoir inlet.

## Parameters

### **Provide input signal for pressure** — Method to specify pressure `off` (default) | `on`

Method to use to specify the pressure in the reservoir. If you clear this
check box, the block models pressure based on the value of the
**Reservoir pressure** parameter or atmospheric
pressure. If you select this check box, the block models pressure based on
the value of the signal at port **P**.

### **Reservoir pressure specification** — Specification method for reservoir pressure `Atmospheric pressure` (default) | `Specified pressure`

Specification method for the reservoir pressure:

- `Atmospheric pressure` — Use the
  atmospheric pressure specified by the Moist Air
  Properties (MA) block connected to the
  circuit.
- `Specified pressure` — Specify a
  value by using the **Reservoir pressure**
  parameter.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
pressure** check box.

### **Reservoir pressure** — Pressure in reservoir `0.101325 MPa` (default) | positive scalar

Pressure in the reservoir. This pressure remains constant during
simulation.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
pressure** check box and set **Reservoir pressure
specification** to `Specified
pressure`.

### **Provide input signal for temperature** — Method to specify reservoir temperature `off` (default) | `on`

Method to use to specify the temperature in the reservoir. If you clear
this check box, the block models temperature based on the value of the
**Reservoir temperature** parameter or atmospheric
temperature. If you select this check box, the block models trace gas based
on the value of the signal at port **T**.

### **Reservoir temperature specification** — Specification method for reservoir temperature `Atmospheric temperature` (default) | `Specified temperature`

Specification method for the reservoir temperature:

- `Atmospheric temperature` — Use
  the atmospheric temperature specified by the Moist
  Air Properties (MA) block connected to the
  circuit.
- `Specified temperature` — Specify
  a value by using the **Reservoir temperature**
  parameter.

### **Reservoir temperature** — Temperature in reservoir `293.15 K` (default) | positive scalar

Temperature in the reservoir. This temperature remains constant during
simulation.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
temperature** check box and set **Reservoir
temperature specification** to `Specified
temperature`.

### **Provide input signal for humidity** — Method to specify humidity `off` (default) | `on`

Method to use to specify the humidity in the reservoir. If you clear this
check box, the block models humidity based on the value of the based on the
value of the **Reservoir humidity specification**
parameter. If you select this check box, the block models trace gas based on
the value of the signal at port **W** or
**Tw**.

### **Reservoir humidity specification** — Specification method for reservoir humidity `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Specification method for the reservoir humidity:

- `Relative humidity` ― Specify humidity
  using the relative humidity.
- `Specific humidity` ― Specify humidity
  using the specific humidity.
- `Mole fraction` ― Specify humidity using
  the water vapor mole fraction.
- `Humidity ratio` ― Specify humidity using
  the humidity ratio.
- `Wet-bulb temperature` ― Specify humidity
  using the wet-bulb temperature.

### **Reservoir relative humidity** — Relative humidity in reservoir `0.5` (default) | scalar in the range of [0,1]

Relative humidity in the reservoir. This value remains constant during
simulation.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
humidity** check box and set **Reservoir humidity
specification** to `Relative
humidity`.

### **Reservoir specific humidity** — Specific humidity in reservoir `0.01` (default) | scalar in the range of [0,1]

Specific humidity in the reservoir. This value remains constant during
simulation.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
humidity** check box and set **Reservoir humidity
specification** to `Specific
humidity`.

### **Reservoir water vapor mole fraction** — Water vapor mole fraction in reservoir `0.01` (default) | scalar in the range of [0,1]

Water vapor mole fraction in the reservoir. This value remains constant
during simulation.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
humidity** check box and set **Reservoir humidity
specification** to `Mole
fraction`.

### **Reservoir humidity ratio** — Humidity ratio in reservoir `0.01` (default) | scalar in the range of [0,1]

Humidity ratio in the reservoir. This value remains constant during
simulation.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
humidity** check box and set **Reservoir humidity
specification** to `Humidity
ratio`.

### **Reservoir wet-bulb temperature** — Wet-bulb temperature in reservoir `287 K` (default) | positive scalar

Wet-bulb temperature in the reservoir. This value remains constant during
simulation.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
humidity** check box and set **Reservoir humidity
specification** to `Wet-bulb
temperature`.

### **Provide input signal for trace gas** — Method to specify trace gas `off` (default) | `on`

Method to use to specify the trace gas in the reservoir. If you clear this
check box, the block models trace gas based on the value of the
**Reservoir trace gas mass fraction** or
**Reservoir trace gas mole fraction** parameters. If
you select this check box, the block models trace gas based on the value of
the signal at port **G**.

### **Reservoir trace gas specification** — Specification method for trace gas `Mass fraction` (default) | `Mole fraction`

Specification method for the reservoir trace gas:

- `Mass fraction` ― Specify the trace gas
  mass fraction.
- `Mole fraction` ― Specify the trace gas
  mole fraction.

### **Reservoir trace gas mass fraction** — Trace gas mass fraction in reservoir `0.001` (default) | scalar in the range of [0,1]

Trace gas mass fraction in the reservoir. This value remains constant
during simulation.

#### Dependencies

To enable this parameter, select **Provide input signal for
trace gas** and set **Reservoir trace gas
specification** to `Mass
fraction`.

### **Reservoir trace gas mole fraction** — Trace gas mole fraction in reservoir `0.001` (default) | scalar in the range of [0,1]

Trace gas mole fraction in the reservoir. This value remains constant
during simulation.

#### Dependencies

To enable this parameter, select **Provide input signal for
trace gas** and set **Reservoir trace gas
specification** to `Mole
fraction`.

### **Provide input signal for water droplets** — Method to specify water droplets mass ratio `off` (default) | `on`

Method to use to specify the water droplets mass ratio in the reservoir.
If you clear this check box, the block models water droplets based on the
value of the **Reservoir mass ration of water droplets to moist
air** parameter. If you select this check box, the block models
water droplets based on the value of the signal at port
**D**.

### **Reservoir mass ration of water droplets to moist air** — Water droplet mass ratio in reservoir `0` (default) | positive scalar

Mass ratio of water droplets to moist air in the reservoir.

#### Dependencies

To enable this parameter, clear the **Provide input signal for
water droplets** check box.

### **Relative humidity at saturation** — Relative humidity above which condensation occurs `1` (default) | positive scalar

Relative humidity above which condensation occurs.

### **Cross-sectional area at port A** — Area normal to flow path at reservoir inlet `0.01 m^2` (default) | positive scalar

Cross-sectional area of the reservoir inlet.

### **Inputs outside valid range** — Action to take when signal values are outside of valid range `Warn and limit to valid values` (default) | `Limit to valid values` | `Error`

Action for the block to take when the input signal values are outside of
valid range:

- `Limit to valid values` ― The block
  limits the input signal to the minimum or maximum valid values, but
  does not issue a warning.
- `Warn and limit to valid values` ― The
  block issues a warning and limits the input signal to the minimum
  or maximum valid values.
- `Error` ― Simulation stops with an
  error.

#### Dependencies

To enable this parameter, select at least one of these parameters:

- **Provide input signal for
  pressure**
- **Provide input signal for
  temperature**
- **Provide input signal for
  humidity**
- **Provide input signal for trace
  gas**
- **Provide input signal for water
  droplets**

## Libraries

Simscape / Foundation Library / Moist Air / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: Model a controlled reservoir

The Controlled Reservoir (MA)  and
Reservoir (MA) blocks have been combined into the
Reservoir (MA) block. Select the
**Provide input signal for pressure**, **Provide input
signal for temperature**, **Provide input signal for
humidity**, **Provide input signal for trace gas**,
and **Provide input signal for water droplets** check boxes to
control the reservoir conditions by using input signals. Otherwise, you can control
the reservoir conditions by using the block parameters.

If you use a Controlled Reservoir (MA)  in your
custom composite components, you must update the composite component code:

- Old syntax: `source =
  foundation.moist_air.elements.controlled_reservoir;`
- New syntax: `source =
  foundation.moist_air.elements.reservoir;`

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To model water droplets, select **Enable entrained water droplets** in the Moist Air Properties (MA) block connected to your moist air network.

### R2023a: Use wet-bulb temperature to specify humidity

The block now has an option to specify humidity by using the wet-bulb temperature.
Wet-bulb temperature is a method of measuring humidity that involves wrapping a wet
cloth around a thermometer, so that you can measure the temperature including energy
loss due to evaporation. Traditional psychrometers output data in the form of
wet-bulb temperature.

## Description

Boundary conditions for moist air network at constant pressure, temperature, moisture, and trace gas levels

The Reservoir (MA) block sets boundary conditions in a
moist air network. The volume of moist air inside the reservoir is assumed infinite.
Therefore, the flow is assumed quasi-steady. Moist air leaves the reservoir at the
reservoir pressure, temperature, specific humidity, and trace gas mass fraction. Moist
air enters the reservoir at the reservoir pressure, but the temperature, specific
humidity, and trace gas mass fraction are determined by the moist air network
upstream.

You specify the reservoir pressure, temperature, amount of humidity, amount of trace
gas, and amount of water droplets with block parameter values or physical signals. The
block ignores parameters and physical signals related to trace gas or water droplets if
in the Moist Air Properties (MA) block, **Trace
gas model** is `None` or the **Enable
entrained water droplets** check box is cleared, respectively.

You can specify humidity as one of:

- Relative humidity, *φ*w
- Specific humidity, *x*w
- Water vapor mole fraction, *y*w
- Humidity ratio, *r*w
- Wet-bulb temperature, *T*w

You can specify trace gas as one of:

- Trace gas mass fraction, *x*g
- Trace gas mole fraction, *y*g

These humidity and trace gas quantities are related to each other as follows:

φw=ywppwsyw=xwRwRrw=xw1−xwyg=xgRgRxa+xw+xg=1R=xaRa+xwRw+xgRg

where:

- *p* is the pressure.
- *R* is the specific gas constant.

Subscripts `a`, `w`, and `g`
indicate the properties of dry air, water vapor, and trace gas, respectively. Subscript
`ws` indicates water vapor at saturation.

The block calculates the wet-bulb temperature implicitly as

xw=(1−xg(T))(ha(Tw)−ha(T))+xg(hg(Tw)−hg(T))+xws(Tw)1−xws(Tw)Δhfg(Tw)(ha(Tw)−ha(T))(hw(Tw)−hw(T))+11−xws(Tw)Δhfg(Tw)

where:

- *T* is the temperature.
- *T*w is the wet-bulb
  temperature.
- *x*w(*T*) is the
  specific humidity.
- *x*g(*T*) is the
  trace gas mass fraction.
- *x*ws(*T*w)
  is the specific humidity of saturation at the wet bulb temperature.
- *h*a(*T*) is the
  specific enthalpy of the dry air.
- *h*a(*T*w)
  is the specific enthalpy of the dry air at the wet bulb temperature.
- *h*g(*T*) is the
  specific enthalpy of the trace gas.
- *h*g(*T*w)
  is the specific enthalpy of the trace gas at the wet bulb temperature.
- *h*w(*T*) is the
  specific enthalpy of the water vapor.
- *h*w(*T*w)
  is the specific enthalpy of the water vapor at the wet bulb temperature.
- *Δh*fg(*T*w)
  is the specific enthalpy of vaporization of water vapor at the wet-bulb
  temperature.
