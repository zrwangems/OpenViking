---
type: simulink-block
title: 'Cooling Tower (TL-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Moist Air'
documentation_page: 'coolingtowertlma'
documentation_source_path: 'ref/coolingtowertlma.html'
language: en
---

# Cooling Tower (TL-MA)

## Ports

### Input

### **M** — Mass flow rate, kg/s physical signal

Mass flow rate of the moist air entering the cooling tower.

#### Dependencies

To enable this port, set **Moist air operating
conditions** to `Provided by input
signals` and **Flow rate input signal
specification** to `Mass flow
rate`.

### **V** — Volumetric flow rate, m^3/s physical signal

Volumetric flow rate of the moist air entering the cooling
tower.

#### Dependencies

To enable this port, set **Moist air operating
conditions** to `Provided by input
signals` and **Flow rate input signal
specification** to `Volumetric flow
rate`.

### **Pwr** — Fan power, W physical signal

Fan power that drives the moist air through the cooling tower.

#### Dependencies

To enable this port, set **Moist air operating
conditions** to `Provided by input
signals` and set **Flow rate input signal
specification** to `Fan
power`.

### **P** — Pressure, Pa physical signal

Pressure of the moist air entering the cooling tower.

#### Dependencies

To enable this port, set **Moist air operating
conditions** to `Provided by input
signals`.

### **T** — Temperature, K physical signal

Dry-bulb temperature of the moist air entering the cooling
tower.

#### Dependencies

To enable this port, set **Moist air operating
conditions** to `Provided by input
signals`.

### **W** — Measure of humidity, unitless physical signal

Relative humidity, specific humidity, water vapor mole fraction, or humidity ratio of
the moist air entering the cooling tower. Use the **Humidity
input signal specification** parameter to specify the type
of humidity input signal.

#### Dependencies

To enable this port, set **Moist air operating conditions** to
`Provided by input signals` and
**Humidity input signal specification** any
option except `Wet-bulb
temperature`.

### **Tw** — Wet-bulb temperature, K physical signal

Wet-bulb temperature of the moist air entering the cooling
tower.

#### Dependencies

To enable this port, set **Moist air operating conditions** to
`Provided by input signals` and
**Humidity input signal specification** to
`Wet-bulb temperature`.

### **Vm** — Volumetric flow rate, m^3/s physical signal

Volumetric flow rate of the thermal liquid that replenishes the water
lost to evaporation and drift.

#### Dependencies

To enable this port, select **Model cold-water
basin** and clear the **Automatically replenish
lost water** check box.

### **Tm** — Temperature, K physical signal

Temperature of the thermal liquid that replenishes the water lost to evaporation and
drift.

#### Dependencies

To enable this port, select **Model cold-water
basin** and clear the **Automatically replenish
lost water** check box.
### Output

### **Q** — Heat transfer, W physical signal

Total sensible and latent heat transfer between the moist air and
thermal liquid.

### **E** — Evaporation rate, kg/s physical signal

Evaporation rate of the thermal liquid.

### **L** — Liquid level, m physical signal

Depth of the thermal liquid in the cooling tower basin.

#### Dependencies

To enable this port, select **Model cold-water
basin** and clear the **Automatically replenish
lost water** check box.

### **Pwr** — Fan power, W physical signal

Fan power required for moist air flow in the cooling tower.

#### Dependencies

To enable this port, set **Moist air operating
conditions** to `Provided by input
signals`, **Flow rate input signal
specification** to either `Mass flow
rate` or `Volumetric flow
rate` and select **Output fan
power**.
### Conserving

### **A1** — Thermal liquid inlet thermal liquid

Thermal liquid conserving port associated with the inlet on the thermal liquid
side.

### **B1** — Thermal liquid outlet thermal liquid

Thermal liquid conserving port associated with the outlet on the thermal liquid
side.

### **A2** — Moist air inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet on the moist air
side.

#### Dependencies

To enable this port, set **Moist air operating
conditions** to `Moist air domain
port`.

### **B2** — Moist air inlet or outlet moist air

Moist air conserving port associated with the inlet or outlet on the moist air
side.

#### Dependencies

To enable this port, set **Moist air operating
conditions** to `Moist air domain
port`.

## Parameters

### Thermal Liquid 1

### **Flow arrangement** — Flow arrangement of moist air and thermal liquid `Counter flow` (default) | `Cross flow`

Flow arrangement for flow in the cooling tower. The thermal liquid
always flows down within the cooling tower. If you select
`Counter flow`, the moist air flows upwards
through the fill material. If you select `Cross
flow`, the moist air flows horizontally across the fill
material.

### **Nominal capacity specification** — Method for specifying size of system `Water volumetric flow rate` (default) | `Water mass flow rate` | `Rate of cooling in cooling tower` | `Rate of cooling in evaporator`

Method for specifying the size of the cooling tower. You can specify the water mass or
volumetric flow rate of water entering the tower, or you can specify the
rate of cooling in the evaporator in the refrigeration loop connected to
the tower or in the cooling tower.

### **Nominal water mass flow rate** — Mass flow rate at nominal conditions `42.7` `kg/s` (default) | positive scalar

Mass flow rate of the thermal liquid entering the tower at nominal operating conditions.
The block uses this value to size the cooling tower.

#### Dependencies

To enable this parameter, set **Nominal capacity
specification** to `Water mass flow
rate`.

### **Nominal water volumetric flow rate** — Volumetric flow rate at nominal conditions `154` `m^3/hr` (default) | positive scalar

Volumetric flow rate of the thermal liquid entering the tower at nominal operating
conditions. The block uses this value to size the cooling tower.

#### Dependencies

To enable this parameter, set **Nominal capacity
specification** to `Water volumetric flow
rate`.

### **Nominal cooling tower heat transfer** — Heat transfer at nominal conditions `1000` `kW` (default) | positive scalar

Heat transfer between the thermal liquid and moist air in the tower at
nominal operating conditions. The block uses this value to size the
cooling tower.

#### Dependencies

To enable this parameter, set **Nominal capacity
specification** to `Rate of cooling in
cooling tower`.

### **Nominal evaporator heat transfer** — Evaporator heat transfer at nominal conditions `800` `kW` (default) | positive scalar

Heat transfer of the evaporator in the refrigeration loop connected to the cooling tower
at nominal operating conditions. The block uses this value to size the
cooling tower. The block assumes that the heat transfer between the
thermal liquid and moist air in the cooling tower is 1.25 times the
value of this parameter.

#### Dependencies

To enable this parameter, set **Nominal capacity
specification** to `Rate of cooling in
evaporator`.

### **Nominal hot-water inlet temperature** — Thermal liquid inlet temperature `35` `degC` (default) | positive scalar

Temperature of the thermal liquid entering the heat exchanger at
nominal operating conditions. The block uses this value to size the
cooling tower.

### **Nominal cold-water outlet temperature** — Thermal liquid outlet temperature `29.44` `degC` (default) | positive scalar

Temperature of the thermal liquid as it flows out of the heat
exchanger after it has cooled at nominal operating conditions. The block
uses this value to size the cooling tower.

### **Model cold-water basin** — Option to model thermal liquid side 1 as a tank `on` (default) | `off`

Select this parameter to model the cold-water basin on the thermal liquid side as a
tank. If you clear this parameter, connect a Tank
(TL) block to port **B1** to model
the cold water basin.

### **Basin cross-sectional area** — Area of basin `8` `m^2` (default) | positive scalar

Cross-sectional area of the basin that holds the cooled water in the
tower.

#### Dependencies

To enable this parameter, select **Model cold-water
basin**.

### **Cross-sectional area at port A1** — Flow area of thermal liquid inlet `0.01` `m^2` (default) | positive scalar

Flow area of the thermal liquid inlet.

### **Cross-sectional area at port B1** — Flow area of thermal liquid outlet `0.01` `m^2` (default) | positive scalar

Flow area of the thermal liquid outlet.

### **Drift rate as fraction of water flow** — Drift rate of thermal liquid `0` (default) | positive scalar

Fraction of the thermal liquid flow that is lost to drift. The drift accounts for liquid
droplets that have blow of the cooling tower without evaporating.

### **Automatically replenish lost water** — Option to automatically replenish lost water on thermal liquid 1 side `on` (default) | `off`

Select this parameter to have the block automatically replace water lost to evaporation
or drift. If you clear this parameter, the block enables the physical
signal ports **Vm** and **Tm** for you
to specify the volumetric flow rate and temperature of the water that
replenishes the basin.

#### Dependencies

To enable this parameter, select **Model cold-water
basin**.

### **Temperature of make-up water** — Temperature of replenishing water `15` `degC` (default) | positive scalar

Temperature of the water the block uses to automatically replenish
water lost from the thermal liquid side due to evaporation and drift.

#### Dependencies

To enable this parameter, select **Model cold-water
basin** and **Automatically replenish lost
water**.

### **Initialize thermal liquid to nominal operating conditions** — Option for initializing thermal liquid `on` (default) | `off`

Option to initialize the thermal liquid to nominal operating
conditions or specified values. If you select this parameter, the block
initializes the thermal liquid to the nominal operating conditions. If
you clear this parameter, you can specify the initial conditions
directly with additional parameters.

#### Dependencies

To enable this parameter, select **Model cold-water
basin**.

### **Initial basin liquid temperature** — Basin temperature at start of simulation `29.44` `degC` (default) | positive scalar

Thermal liquid temperature in the cold water basin at the start of simulation.

#### Dependencies

To enable this parameter, select **Model cold-water basin** and clear
the **Initialize thermal liquid to nominal operating
conditions** check box.

### **Initial basin liquid level** — Basin level at start of simulation `0.2` `m` (default) | positive scalar

Thermal liquid depth of the cold water basin at the start of
simulation.

#### Dependencies

To enable this parameter, select **Model cold-water
basin**.

### **Gravitational acceleration** — Acceleration of gravity constant `9.81` `m/s^2` (default) | positive scalar

Constant for the acceleration of gravity.

#### Dependencies

To enable this parameter, select **Model cold-water
basin**.

### Moist Air 2

### **Moist air operating conditions** — Method to specify moist air conditions `Provided by input signals` (default) | `Moist air domain ports`

Method the block uses to specify the moist air conditions during
simulation. If you select `Provided by input
signals`, the block enables physical signal ports that
you can use to specify the moist air temperature, pressure, and flow
rate. If you select `Moist air domain ports`,
the block enables moist air ports **A2** and
**B2** and you can connect the block to a moist air
network.

### **Flow rate input signal specification** — Method to specify actual moist air flow rate `Volumetric flow rate` (default) | `Mass flow rate` | `Fan power`

Method to specify the actual moist air flow rate. When **Moist
air operating conditions** is `Provided by
input signals`, the block uses the flow rate specified
by this parameter and the temperature and pressure to describe the moist
air operating conditions.

- If you select `Mass flow rate`,
  the block enables port **M**.
- If you select `Volumetric flow
  rate`, the block enables port
  **V**.
- If you select `Fan power`, the
  block enables port **Pwr**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Provided by input
signals`.

### **Output fan power** — Option to output fan power `off` (default) | `on`

Select this parameter to output the calculated fan power needed for
flow as a physical signal at port **Pwr**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Provided by input
signals` and **Flow rate input signal
specification** to either `Mass flow
rate` or `Volumetric flow
rate`.

### **Nominal fan power** — Fan power at nominal operating conditions `7.5` `kW` (default) | positive scalar

Fan power at nominal operating conditions. Datasheets typically
provide this value.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Provided by input
signals` and either:

- Set **Flow rate input signal
  specification** to `Fan
  power`.
- Set **Flow rate input signal
  specification** to `Mass flow
  rate` or `Volumetric flow
  rate` and select **Output fan
  power**.

### **Humidity input signal specification** — Quantity used to describe actual humidity level at tower moist air inlet `Wet-bulb temperature` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Relative humidity`

Physical quantity to use to specify the actual humidity level of the
moist air entering the cooling tower. If you select
`Relative humidity`, `Specific
humidity`, `Mole fraction`, or
`Humidity ratio`, the humidity level is the
signal at port **W**. If you select
`Wet-bulb temperature`, the humidity level
is the signal at port **Tw**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Provided by input
signals`.

### **Input signals outside valid range** — Method to handle invalid signal values `Warn and limit to valid values` (default) | `Limit to valid values` | `Error`

Select what the block does if the physical input signal that
represents the moist air attributes is outside of the valid range:

- `Limit to valid values` — The
  block limits the signal to valid values and does not warn
  you.
- `Warn and limit to valid values`
  — The block limits the signal to valid values and issues a
  warning.
- `Error` — The block issues an
  error and the simulation ends.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Provided by input
signals`.

### **Specify full moist air nominal condition** — Option to specify moist air nominal conditions `off` (default) | `on`

Select this parameter to provide the nominal inlet pressure, nominal inlet temperature,
nominal inlet humidity level, and nominal inlet trace gas level.

If you clear this parameter, you only specify the nominal inlet
wet-bulb temperature, and the block calculates or assumes the other
nominal conditions. Use this option if your manufacture datasheet only
provides the nominal wet-bulb temperature.

### **Nominal flow rate specification** — Option to specify moist air flow rate `Volumetric flow rate` (default) | `Mass flow rate`

Whether to specify the moist air flow rate at nominal conditions as a
mass or volumetric flow rate.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition**.

### **Nominal moist air mass flow rate** — Nominal mass flow rate `36` `kg/s` (default) | positive scalar

Moist air mass flow rate at nominal operating conditions.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition** and set **Nominal flow rate
specification** to `Mass flow
rate`.

### **Nominal moist air volumetric flow rate** — Nominal volumetric flow rate `30` `m^3/s` (default) | positive scalar

Moist air volumetric flow rate at nominal operating conditions.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition** and set **Nominal flow rate
specification** to `Volumetric flow
rate`.

### **Nominal moist air pressure loss** — Pressure drop between moist air ports during nominal operating condition `250` `Pa` (default) | positive scalar

Pressure drop from port **A2** to port
**B2** during the nominal operating
conditions.

If the cooling tower datasheet does not include this value, you can
estimate it from the nominal fan power,
*Φfannom*.
The nominal pressure loss is

ΔpMAnom=ΦfannomηfanqMAnom,

where
*qMAnom*
is the value of the **Nominal moist air volumetric flow
rate** parameter and
*ηfan* is the fan
efficiency, which you can estimate. A reasonable value is around
`0.3`.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports` and select **Specify full moist air
nominal condition**.

### **Nominal inlet pressure** — Pressure at moist air side inlet `0.101325` `MPa` (default) | positive scalar

Pressure at the inlet of the moist air side of the cooling tower
during nominal operating condition.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition**.

### **Nominal inlet temperature** — Temperature at moist air side inlet `34.28` `degC` (default) | positive scalar

Temperature at the inlet of the moist air side of the cooling tower
during the nominal operating condition.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition**.

### **Nominal humidity specification** — Quantity used to describe humidity level at nominal conditions `Wet-bulb temperature` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Relative humidity`

Whether to describe the moist air humidity level at nominal operating
conditions using the relative humidity, specific humidity, water vapor
mole fraction, or humidity ratio.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition**.

### **Nominal inlet relative humidity** — Relative humidity at inlet `0.5` (default) | scalar in the range [0,1]

Relative humidity at the inlet of the moist air side of the cooling
tower during the nominal operating conditions.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition** and set **Nominal humidity
specification** to `Relative
humidity`.

### **Nominal inlet specific humidity** — Specific humidity at inlet `0.0167` (default) | scalar in the range [0,1]

Specific humidity, defined as the mass fraction of water vapor in a
moist air mixture, at the inlet of the moist air side of the cooling
tower during the nominal operating conditions.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition** and set **Nominal humidity
specification** to `Specific
humidity`.

### **Nominal inlet water vapor mole fraction** — Mole fraction of water vapor at inlet `0.0266` (default) | scalar in the range [0,1]

Mole fraction of water vapor in a moist air mixture at the inlet of
the moist air side of the cooling tower during the nominal operating
conditions.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition** and set **Nominal humidity
specification** to `Mole
fraction`.

### **Nominal inlet humidity ratio** — Humidity ratio at inlet `0.017` (default) | scalar in the range [0,1]

Humidity ratio, defined as the mass ratio of water vapor to dry air
and trace gas, at the inlet of the moist air side of the cooling tower
during the nominal operating conditions.

#### Dependencies

To enable this parameter, select **Specify full moist air
nominal condition** and set **Nominal humidity
specification** to `Humidity
ratio`.

### **Nominal inlet wet-bulb temperature** — Wet-bulb temperature at moist air inlet `25.56` `degC` (default) | positive scalar

Wet-bulb temperature at the moist air inlet in nominal operating
conditions.

#### Dependencies

To enable this parameter, either:

- Clear the **Specify full moist air nominal
  condition** check box.
- Select **Specify full moist air nominal
  condition** and set **Nominal
  humidity specification** to
  `Wet-bulb
  temperature`.

### **Nominal trace gas specification** — Quantity used to describe nominal trace gas level `Mass fraction` (default) | `Mole fraction`

Quantity the block uses to describe the trace gas level at nominal
operating conditions.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports` and select **Specify full moist air
nominal condition**.

### **Nominal inlet trace gas mass fraction** — Mass fraction of trace gas at inlet `6e-4` (default) | scalar in the range [0,1]

Mass fraction of the trace gas in a moist air mixture at the inlet of
the moist air side of the cooling tower during nominal operating
conditions.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`, select **Specify full moist air
nominal condition**, and set **Nominal trace
gas specification** to `Mass
fraction`.

### **Nominal inlet trace gas mole fraction** — Mole fraction of trace gas at inlet `4e-4` (default) | scalar in the range [0,1]

Mole fraction of the trace gas in a moist air mixture at the inlet of
the moist air side of the cooling tower during nominal operating
conditions.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`, select **Specify full moist air
nominal condition**, and set **Nominal trace
gas specification** to `Mole
fraction`.

### **Moist air volume** — Total volume of moist air in cooling tower `24` `m^3` (default) | positive scalar

Total volume of the moist air in the cooling tower.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`.

### **Cross-sectional area at port A2** — Area of moist air inlet or outlet `4` `m^2` (default) | positive scalar

Flow area of the moist air inlet or outlet.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`.

### **Cross-sectional area at port B2** — Area of moist air inlet or outlet `4` `m^2` (default) | positive scalar

Flow area of the moist air inlet or outlet.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`.

### **Initialize moist air to nominal operating conditions** — Option for initializing moist air `on` (default) | `off`

Select this parameter to initialize the moist air to the nominal
operating conditions. If you clear this parameter, you can specify the
initial conditions directly.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`.

### **Initial moist air pressure** — Moist air pressure at start of simulation `0.101325` `MPa` (default) | positive scalar

Moist air pressure at the start of the simulation.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports` and clear the **Initialize moist air
to nominal operating conditions** check box.

### **Initial moist air temperature** — Moist air temperature at start of simulation `34.28` `degC` (default) | scalar | two-element vector

Moist air temperature at the start of simulation. If the value is a
scalar, then the initial temperature is uniform. If the value is a
two-element vector, then the initial temperature varies linearly between
ports **A2** and **B2**, with the
first element corresponding to port **A2** and the
second element corresponding to port **B2**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports` and clear the **Initialize moist air
to nominal operating conditions** check box.

### **Initial humidity specification** — Quantity used to describe initial humidity level `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Whether to describe the initial moist air humidity level using the
relative humidity, specific humidity, water vapor mole fraction, or
humidity ratio.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports` and clear the **Initialize moist air
to nominal operating conditions** check box.

### **Initial moist air relative humidity** — Relative humidity at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Moist air relative humidity at the start of simulation. If the value
is a scalar, then the initial relative humidity is uniform. If the value
is a two-element vector, then the initial relative humidity varies
linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`, clear the **Initialize moist air to
nominal operating conditions** check box, and set
**Initial humidity specification** to
`Relative humidity`.

### **Initial moist air specific humidity** — Specific humidity at start of simulation `0.0167` (default) | scalar in the range [0,1] | two-element vector

Moist air specific humidity, defined as the mass fraction of water
vapor in a moist air mixture, at the start of simulation. If the value
is a scalar, then the initial specific humidity is uniform. If the value
is a two-element vector, then the initial specific humidity varies
linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`, clear the **Initialize moist air to
nominal operating conditions** check box, and set
**Initial humidity specification** to
`Specific humidity`.

### **Initial moist air water vapor mole fraction** — Mole fraction of water vapor at start of simulation `0.0266` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of the water vapor in a moist air mixture at the start
of simulation. If the value is a scalar, then the initial mole fraction
is uniform. If the value is a two-element vector, then the initial mole
fraction varies linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`, clear the **Initialize moist air to
nominal operating conditions** check box, and set
**Initial humidity specification** to
`Mole fraction`.

### **Initial moist air humidity ratio** — Humidity ratio at start of simulation `0.017` (default) | scalar in the range [0,1] | two-element vector

Moist air humidity ratio, defined as the mass ratio of water vapor to
dry air and trace gas, at the start of simulation. If the value is a
scalar, then the initial humidity ratio is uniform. If the value is a
two-element vector, then the initial humidity ratio varies linearly
between ports **A2** and **B2**, with
the first element corresponding to port **A2** and the
second element corresponding to port **B2**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`, clear the **Initialize moist air to
nominal operating conditions** check box, and set
**Initial humidity specification** to
`Humidity ratio`.

### **Initial moist air wet-bulb temperature** — Wet-bulb temperature at start of simulation `25.56` `degC` (default) | positive scalar

Wet-bulb temperature of the moist air mixture at the start of
simulation. If the value is a scalar, then the initial mole fraction is
uniform. If the value is a two-element vector, then the initial mole
fraction varies linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`, clear the **Initialize moist air to
nominal operating conditions** check box, and set
**Initial humidity specification** to
`Wet-bulb temperature`.

### **Initial trace gas specification** — Quantity used to describe initial trace gas level `Mass fraction` (default) | `Mole fraction`

Whether to use the mass fraction or mole fraction to describe the
trace gas level at the start of simulation.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports` and clear the **Initialize moist air
to nominal operating conditions** check box.

### **Initial moist air trace gas mass fraction** — Mass fraction of trace gas at start of simulation `6e-4` (default) | scalar in the range [0,1]

Mass fraction of the trace gas in a moist air mixture at the start of
simulation. If the value is a scalar, then the initial mass fraction is
uniform. If the value is a two-element vector, then the initial mass
fraction varies linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`, clear the **Initialize moist air to
nominal operating conditions** check box, and set
**Initial trace gas specification** to
`Mass fraction`.

### **Initial moist air trace gas mole fraction** — Mole fraction of trace gas at start of simulation `4e-4` (default) | scalar in the range [0,1]

Mole fraction of the trace gas in a moist air mixture at the start of
simulation. If the value is a scalar, then the initial mole fraction is
uniform. If the value is a two-element vector, then the initial mole
fraction varies linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`, clear the **Initialize moist air to
nominal operating conditions** check box, and set
**Initial trace gas specification** to
`Mole fraction`.

### **Initial mass ratio of water droplets to moist air** — Ratio of water droplets to moist air `0` (default) | positive scalar

Initial mass ratio of water droplets to moist air.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports` and clear the **Initialize moist air
to nominal operating conditions** check box.

### **Relative humidity at saturation** — Relative humidity above which condensation occurs `1` (default) | positive scalar

Relative humidity above which condensation occurs in the tower.

### **Water vapor condensation time constant** — Time scale for condensation `1e-3 s` (default) | positive scalar

Characteristic time scale at which an oversaturated moist air volume returns to
saturation by condensing out excess humidity.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`.

### **Water droplets evaporation time constant** — Time scale for evaporation `1e-3 s` (default) | positive scalar

Characteristic time scale at which water droplets evaporate to
vapor.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`.

### **Fraction of condensate entrained as water droplets** — Fraction of condensate in water droplets `1` (default) | scalar in the range [0,1]

Fraction of the condensate in the moist air that is entrained as water
droplets.

#### Dependencies

To enable this parameter, set **Moist air operating
conditions** to `Moist air domain
ports`.

## Libraries

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Moist Air

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the
moist air domain can now model water droplets suspended in a moist air flow. To model water
droplets, select **Enable entrained water droplets** in the Moist Air Properties
(MA) block connected to your moist air network.

## Description

Cooling tower between a thermal liquid and moist air network

The Cooling Tower (TL-MA) block models a cooling tower
between moist air and a thermal liquid network. The block models sensible and latent
heat transfer from the thermal liquid side to the moist air side based on an analogous
effectiveness-NTU method for heat and water vapor mass transfer. The thermal liquid side
represents the water in the tower while the moist air side represents the environmental
air. The block is performance based rather than geometry based, which means that the
block sizes the cooling tower to match the nominal operating conditions that you
specify.

### Cooling Tower Geometry

Large HVAC systems use cooling towers to reject heat from water to the environment
in applications where the amount of heat is too large for regular water-air heat
exchangers to be practical. In a cooling tower, the hot water and air are in direct
contact, which allows some of the water to evaporate into the air and cools the rest
of the water by the evaporative cooling effect.

A cooling tower works by spreading and spraying hot water from the top of the
tower over a large area to encourage it to evaporate into the air. Typically, there
is a fill material underneath the spray nozzles with a large surface area that
allows the water to form a thin film and spread out. The fill material increases the
contact area between the water and the air for more evaporation. Because there is no
heat source, the latent heat needed to turn liquid water into water vapor comes from
the water itself. As a result, the water that did not evaporate cools. The cold
water collects at the bottom of the cooling tower in a basin, and can be returned to
the HVAC system.

You can use the **Flow arrangement** parameter to specify if the
cooling tower uses a cross flow or counter flow. This block only models direct-flow
cooling towers, which means the water is in direct contact with the air. The block
also only models mechanical-draft cooling towers, where a fan moves the air through
the cooling tower.

This figure shows a diagram of a counter-flow, direct-contact, induced
mechanical-draft cooling tower.

Diagram of counter flow direct-contact, induced mechanical-draft cooling tower

This figure shows a diagram of a direct-contact, induced mechanical-draft cooling
tower with two air entries.

Cross flow direct-contact, induced mechanical-draft cooling tower with double air entry

### Heat Transfer and Evaporation Rate

The combined heat and water vapor mass transfer is

Qcombined=ϵQcombined,max=ϵCmin(h¯sTLin−h¯MAin),

where:

- *Qcombined,max* is the
  theoretically maximum combined heat and water vapor mass transfer, Qcombined,max=Cmin(h¯sTLin−h¯MAin).
- h¯*sTLin*
  is the enthalpy of the saturated moist air evaluated at the temperature
  of the inlet at the thermal liquid side.
- h¯*MAin*
  is the mixture enthalpy of the moist air at the inlet.
- *Cmin* is the smaller capacity
  ratio between the moist air and thermal liquid.

When **Flow arrangement** is `Counter
flow`, the effectiveness factor, *ε*, is

ϵ=1−exp[−(1−CR)NTU]1−CRexp[−(1−CR)NTU],

where *CR* is the capacity ratio and
*NTU* is the number of transfer units.

When **Flow arrangement** is `Cross
flow`, the block assumes that one fluid is mixed and the other is
unmixed. If the fluid with the lower value for *C* is
unmixed,

ϵ=1−exp(−CR[1−exp(−NTU)])CR.

Typically, the moist air will have the lower value for *C*. If
the fluid with the lower value for *C* is mixed,

ϵ=1−exp[−1−exp(−CR∗NTU)CR].

The capacity ratio is

CR=CminCmax=min{CTL,CMA}max{CTL,CMA}.

*CMA* and
*CTL* are the capacity rates for the
moist air and thermal liquid, respectively,

CTL=m˙TLcpTLc¯sTLCMA=m˙agMA

where:

- *ṁTL* is the thermal liquid
  mass flow rate.
- *cpTL*
  is the thermal liquid specific heat at constant pressure.
- *ṁagMA*
  is the mass flow rate of the dry air and trace gas.

The number of transfer units, *NTU*, is

NTU=UMAACminc¯pMA,

where:

- *A* is the heat transfer surface area.
- *UMA* is the heat transfer
  conductance on the moist air side.
- c¯*pMA*
  is the moist air specific heat at constant pressure.

The combined heat and water vapor mass transfer,
*Qcombined*, accounts for the
sensible heat transfer, latent heat, and energy debit due to lost liquid,

Qcombined=Q+Δhfgeffm˙e+hleffm˙e,

where:

- *Q* is the sensible heat transfer between thermal
  liquid and moist air in the cooling tower. The block calculates this
  value with Q=Qcombined−hweffm˙e. This term represents the portion of the cooling due
  to the temperature difference between the thermal liquid and moist
  air.
- *Δhfgeff*
  is the water vapor specific enthalpy of vaporization. When multiplied by
  *ṁe*, this term gives
  the latent heat transfer between the thermal liquid and moist air in the
  cooling tower. This term represents the portion of the cooling due to
  the energy extracted from the liquid water when converted into water
  vapor.
- *hleff*
  is the liquid water specific enthalpy. When multiplied by
  *ṁe*, this term gives
  the energy debited from the energy balance of the thermal liquid flow
  due to the removal of a portion of the liquid.

The evaporation rate in the cooling tower is

m˙e=Cmin(Wseff−WMAin)[1−exp(−NTU)],

where:

- *Wseff*
  is the effective saturated humidity ratio.
- *WMAin*
  is the humidity ratio at the moist air inlet.

The effective saturated humidity ratio is

Wseff=Ra+G(Rg−Ra)Rw(pφwspws(Teff)−1),

where:

- *Ra* is the specific gas
  constant of dry air.
- *G* is the trace gas ratio.
- *Rg* is the specific gas
  constant of the trace gas.
- *RW* is the specific gas
  constant of the water vapor.
- *p* is the pressure.
- *φws* is the value of the
  **Relative humidity at saturation**
  parameter.
- *pws(Teff)*
  is the water vapor saturation pressure evaluated at the effective liquid
  film surface temperature.

The effective liquid film surface temperature is

Teff=TTLin−h¯sTLin−h¯seffc¯sTL,

where:

- *TTLin*
  is the temperature of the thermal liquid at the inlet.
- c¯*sTL*
  is the specific heat of the saturated moist air along the saturation
  curve when evaluated at the temperature of the thermal liquid.
- h¯*seff*
  is the saturated mixture enthalpy along the liquid film surface

  h¯seff=h¯MAin+ϵ(h¯sTLin−h¯MAin)1−exp(−NTU).

The heat transfer conductance at the moist air side,
*UMAA*, is

UMAA=max{(m˙MAμMA)bPrMAck(DrefSref)ba,NulamkMA}Gfill,

where:

- *UMA* is the heat transfer
  coefficient.
- *ṁMA* is the moist air mass
  flow rate.
- *μMA* is the moist air dynamic
  viscosity.
- *a* is the coefficient for the proportionality in the
  Nusselt number correlation.
- *b* is the coefficient for the Reynolds number
  exponent in the Nusselt number correlation.
- *c* is the coefficient for the Prandtl number
  exponent in the Nusselt number correlation.
- *PrMA* is the moist air
  Prandtl number.
- *kMA* is the thermal
  conductivity of the moist air.
- *Dref* is an arbitrary
  diameter. The block uses this value with
  *Sref* to
  nondimensionalize with respect to length.
- *Sref* is the flow area
  corresponding to *Dref*.
- *Nulam* is 3.66, which is the
  theoretical Nusselt number for a laminar flow through a circular
  pipe.
- *Gfill* is the geometry scale
  factor for the cooling tower fill material. The block calculates this
  value at nominal operating conditions.

### Cooling Tower Sizing

The block sizes the cooling tower to match the nominal performance at nominal
operating conditions. On the thermal liquid side, the **Nominal capacity
specification** parameter specifies how the block determines the
nominal data:

- `Water mass flow rate` or `Water
  volumetric flow rate` — The block infers the nominal
  capacity from the nominal flow rate and the nominal inlet and outlet
  temperatures.
- `Rate of cooling in cooling tower` or
  `Rate of cooling in evaporator` — The block
  infers the nominal flow rate from the nominal capacity.

On the moist air side, the nominal data depends on the **Specify full
moist air nominal conditions** parameter.

If you clear the **Specify full moist air nominal conditions**
check box, the only nominal condition you specify is the value of the
**Nominal inlet wet-bulb temperature** parameter. Use this
option if your manufacturer datasheet provides only the nominal wet-bulb
temperature. The block calculates the other nominal conditions:

- The block calculates the nominal inlet temperature based on the value
  of the **Nominal inlet wet-bulb temperature** parameter
  so that the relative humidity is 50%.
- The block calculates the nominal flow rate from the nominal water flow
  rate so that the capacity ratio at nominal operating condition is
  `1`.

The block assumes that the nominal inlet pressure is atmospheric and that there is
no nominal trace gas..

If you select **Specify full moist air nominal conditions**, you
must specify the nominal inlet pressure, nominal inlet temperature, nominal inlet
humidity level, and nominal inlet trace gas level.

The block uses nominal operating conditions to solve for the geometry scale factor
for the cooling tower fill material,
*Gfill*. This value describes the size of
the cooling tower. The block inverts the expression for the heat transfer
conductance of the moist air side, *UMAA*,
and calculates *Gfill* from the heat
transfer conductance at nominal operating conditions. The block then uses
*Gfill* to calculate the heat
transfer conductance on the moist air side at actual operating conditions during
simulation. The block does not model convective heat transfer in the thermal liquid
film.

*Gfill* at nominal operating conditions is

Gfill=(UMAA)nom(m˙MAnomμMAnom)bPrMAnomckMAnom(DrefSref)ba,

where the subscript *nom* denotes the variable
value at the specified nominal operating condition.

The block solves for
*(UMAA)nom*
with

(UMAA)nom=Cminnomc¯pMA,nomNTUnom.

The block calculates
*NTUnom* by inverting the applicable
effectiveness equation.

When **Flow arrangement** is `Counter
flow`,

NTUnom=11−CRnomln(1−ϵnomCRnom1−ϵnom),

where *CRnom* is the
capacity ratio and ϵnom=QcombinednomQcombined,maxnom with *Qcombined*,
*Qcombined,max*, and
*CRnom* evaluated at the nominal
operating conditions.

When **Flow arrangement** is `Cross
flow` and the fluid with the lower value for *C*
is mixed

NTUnom=−ln[1+CRnomln(1−ϵnom)]CRnom.

If the fluid with the lower value for *C* is unmixed,

NTUnom=−ln[1+ln(1−ϵnomCRnom)CRnom].

### Thermal Liquid Equations

The pressure of the thermal liquid when it enters the cooling tower at port
**A1** is

pTLA1=pMA,

where *pMA* is the moist
air pressure inside the cooling tower. Because the block assumes that water loss due
to evaporation is small, the thermal liquid mass flow rate is equal to the port
**A1** inflow rate, m˙TL=m˙TLA1.

The steady state mass balance equation for the thermal liquid is

m˙TLA1−m˙e−λm˙TLA1=m˙TLfill,out,

where:

- *λ* is the value of the **Drift rate as
  fraction of water flow** parameter. The drift accounts for
  liquid droplets that blow out of the cooling tower without evaporating.
- *ṁTLfill,out*
  is the mass flow rate of the thermal liquid at the exit point of the
  fill material.

The steady state mass balance equation for the thermal liquid is

ΦTLA1−Qcombined−λΦTLA1=ΦTLfill,out,

where:

- *ΦTLA1*
  is the energy flow rate at port **A1**.
- *ΦTLfill,out*
  is the energy flow rate out of the fill material.

If you select **Model cold-water basin**, the block models an
internal tank with the tank outlet at the bottom of the tank. Because the water in
the tank must be replenished, the thermal liquid mass and energy conservation
equations have two additional source terms,
*ṁTLmakeup*
and
*ΦTLmakeup*.

When you select **Automatically replenish lost water**,

m˙TLmakeup=m˙e+λm˙TLA1ΦTLmakeup=m˙TLmakeuphTLmakeup

where *hTLmakeup*
is the thermal liquid specific enthalpy specified by the **Temperature of
make-up water** parameter.

If you clear the **Automatically replenish lost water** check
box, you can specify the volumetric flow rate and temperature of the tank make-up
water with ports **Vm** and **Tm**, respectively.
Port **L** outputs the liquid level in the basin. The make-up water
terms are

m˙TLmakeup=ρTL(pMA,Tmu)VmuΦTLmakeup=m˙TLmakeuphTL(pMA,Tmu)

where:

- *pMA* is the moist air
  pressure in the cooling tower.
- *Tmu* is the temperature of
  the make-up water, which is the value of the signal at port
  **Tm**.
- *ρTL(pMA,Tmu)*
  is the thermal liquid density evaluated at the moist air pressure and
  make-up water temperature.
- *hTL(pMA,Tmu)*
  is the thermal liquid specific enthalpy evaluated at the moist air
  pressure and make-up water temperature.

If you select **Model cold-water basin**, the block models an
internal tank.
*ṁTLfill,out* and
*ΦTLA1*
define the input flows of the internal tank. Port **B1** is the
outlet of the internal tank.

If you clear the **Model cold-water basin** check box,

m˙TLB1=−m˙TLfill,outΦTLB1=−ΦTLfill,out

Port **B1** acts as a flow rate source for any downstream
components. Connect a Tank
(TL) block to port **B1** to model the cold
water basin. The **Inlet height** parameter of the
Tank (TL) block must be larger than the liquid
level in the tank.

### Moist Air Equations

The behavior of the moist air side of the block depends on the **Moist air
operating conditions** parameter.

**Physical Signals**

When you set **Moist air operating conditions** to
`Provided by input signals`, the block enables
physical signal ports that you can use to specify the moist air attributes:

- Port **P** is the input signal for the moist air
  inlet pressure. The moist air pressure,
  *pMA*, is equal to
  the value of this signal.
- Port **T** is the input signal for the moist air
  dry-bulb temperature.
- The flow rate input port depends on the **Flow rate input
  signal specification** parameter:

  | Value of **Flow rate input signal specification** | Enabled Port | Port Meaning |
  | --- | --- | --- |
  | `Mass flow rate` | **M** | Moist air mixture mass flow rate |
  | `Volumetric flow rate` | **V** | Moist air mixture volumetric flow rate |
  | `Fan power` | **Pwr** | Moist air fan power |
- The humidity level input port depends on the **Humidity
  input signal specification** parameter:

  | Value of **Humidity input signal specification** | Enabled Port | Port Meaning |
  | --- | --- | --- |
  | `Relative humidity` | **W** | Moist air inlet relative humidity |
  | `Specific humidity` | **W** | Moist air inlet specific humidity |
  | `Mole fraction` | **W** | Moist air inlet water vapor mole fraction |
  | `Humidity ratio` | **W** | Moist air inlet humidity ratio |
  | `Wet-bulb temperature` | **Tw** | Moist air inlet wet-bulb temperature |

  When **Flow rate input signal specification** is
  `Mass flow rate` or
  `Volumetric flow rate`, the block uses
  the signal at port **M** or **V**
  to calculate the moist air mixture mass flow rate that enters the
  cooling tower,
  *ṁMAin*.
  The dry air and trace gas flow rate is

  m˙agMA=m˙MAin1+WMAin.

  The block calculates the humidity ratio,
  *WMAin*,
  from the input signals at ports **P**,
  **T**, and **W** or
  **Tw**.

  When **Flow rate input signal specification** is
  `Fan power`, the fan power,
  *Φfan*, is
  proportional to the cube of the volumetric flow rate,
  *q*, and pressure gain across the fan,
  *Δp*.

  The moist air mixture volumetric flow rate is

  qMA=(PwrΦfannom)1/3qMAnom,

  where:
- *Pwr* is the value of the signal at port
  **Pwr**.
- *Φfannom*
  is the value of the **Nominal fan power**
  parameter.
- *qMAnom*
  is the nominal volumetric flow rate. If you select **Specify
  full moist air nominal condition**,
  *qMAnom*
  is the value of the **Nominal moist air volumetric flow
  rate** parameter. If you clear **Specify full
  moist air nominal condition**, the block calculates
  *qMAnom*
  from the nominal water flow rate so that the capacity ratio is
  one.

When **Moist air operating conditions** is
`Provided by input signals`, the block does not
model trace gas.

**Moist Air Domain Ports**

When you set **Moist air operating conditions** to
`Moist air domain ports`, the block enables the
moist air ports **A2** and **B2**, which you
can connect to a moist air network. Because the direction of the moist air flow
does not matter in this block, either port **A2** or
**B2** can be the inlet. The dry air and trace gas flow
rate is

m˙agMA=m˙MAin1+WMAin,

where:

- *ṁMAin*
  is the moist air mixture mass flow rate at port
  **A2** or **B2**.
- *WMAin*
  is the moist air mixture humidity ratio at port
  **A2** or **B2**.

The moist air mixture mass conservation equation is

dMMAdt=m˙MAA2+m˙MAB2+m˙e,

where:

- *ṁMAA2*
  and
  *ṁMAB2*
  are the mass flow rates at ports **A2** and
  **B2**.
- *MMA* is the total mixture
  mass of the moist air volume.

The water vapor mass conservation equation is

MMAdxwMAdt+xwMA(m˙MAA2+m˙MAB2+m˙e)=m˙wMAA2+m˙wMAB2+m˙e,

where
*xwMA* is
the specific humidity of the moist air volume and
*ṁwMAA2*
and
*ṁwMAB2*
are the water vapor mass flow rates at ports **A2** and
**B2**.

The trace gas mass conservation equation is

MMAdxgMAdt+xgMA(m˙MAA2+m˙MAB2+m˙e)=m˙gMAA2+m˙gMAB2,

where
*xgMA* is
the trace gas mass fraction of the moist air volume and
*ṁgMAA2*
and
*ṁgMAB2*
are the trace gas mass flow rates at ports **A2** and
**B2**.

The water droplet mass conservation equation is

MMAdrdMAdt+rdMA(m˙MAA2+m˙MAB2+m˙e)=m˙dMAA2+m˙dMAB2,

where:

- *rdMA*
  is the mass ratio of the water droplets to the moist air.
- *ṁdMAA2*
  and
  *ṁdMAB2*
  are the water droplet mass flow rates at ports
  **A2** and **B2**.

The moist air mixture energy conservation equation is

MMAduMAdt+uMA(m˙MAA2+m˙MAB2+m˙e)=ΦMAA2+ΦMAB2+Qcombined,

where *uMA* is the
mixture specific internal energy of the moist air volume and
*ΦMAA2*
and *ΦMAB2* are
the moist air mixture energy flow rates at ports **A2** and
**B2**.

The pressure loss of the moist air in the cooling tower is

ΔpMA=(qMAqMAnom)2ΔpMAnom,

where:

- *ΔpMAnom*
  is the value of the **Nominal moist air pressure
  loss** parameter.
- *qMAnom*
  is the value of the **Nominal moist air volumetric flow
  rate** parameter.
- *qMA* is the volumetric
  flow rate of moist air through the cooling tower.

### Using the Cooling Tower in a Model

When using the Cooling Tower (TL-MA), follow these
guidelines:

- If you clear the **Model cold-water basin** check
  box, you must connect the cooling tower port **B1** to
  a Tank
  (TL) block.
- When modeling transient situations such as startup or shutdown,
  connect the cooling tower port **A1** to port
  **A** of a Partially Filled Pipe (TL) block to avoid a
  possible nonphysical situation of liquid flowing out of port
  **A1**. During startup and shutdown, port
  **A1** may be exposed to the environment, which
  means there is no liquid present. The partially-filled pipe handles this
  scenario by allowing the liquid level to fall along the pipe while port
  **A1** is exposed, if necessary.
- Some cooling towers may use a pressure source to force water out of
  the spray nozzles and spread the water over a wider area, which causes a
  pressure drop at the inlet. To model pressure drop through the spray
  nozzles, connect a block that models pressure loss, such as an
  Orifice (TL),
  Local
  Resistance (TL), or Flow Resistance (TL) block, to port
  **A1** of the cooling tower.
- The Cooling Tower (TL-MA) block models
  a direct-contact cooling tower. To model an indirect-contact cooling
  tower, connect the thermal liquid side of the Cooling
  Tower (TL-MA) block to one side of a Heat Exchanger
  (TL-TL) block. In this configuration, the other side
  of the heat exchanger block represents the thermal liquid flowing into
  and out of the cooling tower, and the block models the heat transfer
  from the coil inside the cooling tower.
- If you set **Moist air operating conditions** to
  `Moist air domain ports`, you can model a
  mechanical forced-draft or an induced-draft cooling tower. To model a
  forced-draft cooling tower, connect a Fan
  (MA) block to the moist air inlet side of the tower.
  To model an induced-draft cooling tower, connect a Fan
  (MA) block to the moist air outlet side. If you set
  **Moist air operating conditions** to
  `Provided by input signals`, the block does
  not distinguish between forced-draft or induced-draft cooling
  towers.

### Assumptions and Limitations

- The block only models a mechanical-draft cooling tower, which means a fan
  moves the moist air through the tower.
- The block only models a direct-contact cooling tower, which means the
  thermal liquid is in direct contact with the moist air.
