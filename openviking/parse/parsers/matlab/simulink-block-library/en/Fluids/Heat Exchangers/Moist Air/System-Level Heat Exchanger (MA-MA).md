---
type: simulink-block
title: 'System-Level Heat Exchanger (MA-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Moist Air'
documentation_page: 'systemlevelheatexchangermama'
documentation_source_path: 'ref/systemlevelheatexchangermama.html'
language: en
---

# System-Level Heat Exchanger (MA-MA)

## Ports

### Output

### **Q1** — Rate of heat transfer to moist air 1, W physical signal

Rate of heat transfer to moist air 1, returned as a physical signal,
in W. The physical signals at ports **Q1** and
**Q2** are usually equal in value with opposite
sign. However, if you select **Enable wall thermal
mass**, then these two signals may have different values
because the wall may absorb and release some of the heat being
transferred.

### **Q2** — Rate of heat transfer to moist air 2, W physical signal

Rate of heat transfer to moist air 2, returned as a physical signal,
in W. The physical signals at ports **Q1** and
**Q2** are usually equal in value with opposite
sign. However, if you select **Enable wall thermal
mass**, then these two signals may have different values
because the wall may absorb and release some of the heat being
transferred.

### **W1** — Moist air 1 condensation rate, kg/s physical signal

Water condensation rate that leaves the moist air 1 flow, returned as
a physical signal. The value of this port does not include the portion
of condensation that is entrained as water droplets. The condensate does
not accumulate on the heat transfer surface.

### **W2** — Moist air 2 condensation rate, kg/s physical signal

Water condensation rate that leaves the moist air 2 flow, returned as
a physical signal. The value of this port does not include the portion
of condensation that is entrained as water droplets. The condensate does
not accumulate on the heat transfer surface.
### Conserving

### **A1** — Moist air port on side 1 moist air

Inlet or outlet port associated with the moist air on side 1.

### **B1** — Moist air port on side 1 moist air

Inlet or outlet port associated with the moist air on side 1.

### **A2** — Moist air port on side 2 moist air

Inlet or outlet port associated with the moist air on side 2.

### **B2** — Moist air port on side 2 moist air

Inlet or outlet port associated with the moist air on side 2.

## Parameters

### Configuration

### **Flow arrangement at nominal operating conditions** — Flow path alignment `Parallel flow - Both fluids flow from A to B` (default) | `Counter flow - Moist Air 1 flows from A to B, Moist Air 2 flows from B to A` | `Cross flow - Both fluids flow from A to B`

Flow path alignment between the heat exchanger sides at nominal
operating condition. The available flow arrangements are:

- `Parallel flow - Both fluids flow from A to
  B` — The flows run parallel to each other,
  in the opposite directions.
- `Parallel flow - Both fluids flow from A to
  B` — The flows run in the same
  direction.
- `Cross flow - Both fluids flow from A to
  B` — The flows run perpendicular to each
  other.

The choice between parallel flow and counter flow affects how the
block determines the size of the heat exchanger. The counter flow
setting is the most effective, and needs the smallest size to meet the
specified performance. Conversely, parallel flow is the least effective,
and needs the biggest size to meet the specified performance.

Flow direction at the nominal condition (from A to B, or from B to A)
only affects the model initialization, when you select
**Initialize moist air 1 to nominal operating
conditions** or **Initialize moist air 2 to nominal
operating conditions**. If you set different initial
operating conditions, the flow directions can be different.

After the block determines the size of the heat exchanger, this
setting does not play a role in how the block calculates the heat
transfer during simulation. Instead, the heat transfer depends on the
flow directions during simulation. For example, if you set the parameter
to parallel flow but set up the model to run in counter flow, then the
rate of heat transfer during simulation will not match the specified
performance, even if the rest of the boundary conditions are the
same.

If you set the parameter to cross flow, then the block models the flow
paths as perpendicular inside the heat exchanger, so the flow directions
during simulation do not matter.

### **Enable wall thermal mass** — Whether to enable effect of thermal mass on heat transfer surface `off` (default) | `on`

Whether to enable the effect of thermal mass on the heat transfer
surface. When you select this parameter, the block introduces additional
dynamics to the simulation and takes longer to reach steady state, but
this parameter does not affect the results at steady-state simulation.

### **Wall mass** — Mass of heat transfer surface `1 kg` (default) | positive scalar

Mass of the heat transfer surface.

#### Dependencies

To enable this parameter, select **Enable wall thermal
mass**.

### **Wall specific heat** — Specific heat of heat transfer surface `490 J/(K*kg)` (default) | positive scalar

Specific heat of the heat transfer surface.

#### Dependencies

To enable this parameter, select **Enable wall thermal
mass**.

### **Initialize wall temperature to nominal operating conditions** — Option for initializing wall temperature `on` (default) | `off`

Option to initialize the wall temperature to nominal operating
conditions or specified values. If you select this parameter, the block
calculates the initial wall temperature from the nominal operating
conditions specified for both fluid sides. If you clear this parameter,
you can specify the initial wall temperature directly with the
**Initial wall temperature** parameter.

#### Dependencies

To enable this parameter, select **Enable wall thermal
mass**.

### **Initial wall temperature** — Initial temperature of wall `293.15 K` (default) | positive scalar or two-element vector

Initial temperature of the wall. If you specify a scalar, the block
assumes that the initial wall temperature is uniform. If you specify a
two-element vector, then the block assumes that the initial wall
temperature varies linearly between ports **A1** and
**A2** and ports **B1** and
**B2**. The first element corresponds to the
temperature at ports **A1** and **A2**
and the second element corresponds to the temperature at ports
**B1** and **B2**.

#### Dependencies

To enable this parameter, select **Enable wall thermal
mass** and clear the **Initialize wall
temperature to nominal operating conditions** check
box.

### **Cross-sectional area at port A1** — Flow area at port A1 `0.01 m^2` (default) | positive scalar

Flow area at the moist air port **A1**.

### **Cross-sectional area at port B1** — Flow area at port B1 `0.01 m^2` (default) | positive scalar

Flow area at the moist air port **B1**.

### **Cross-sectional area at port A2** — Flow area at port A2 `0.01 m^2` (default) | positive scalar

Flow area at the moist air port **A2**.

### **Cross-sectional area at port B2** — Area normal to flow at port B2 `0.01 m^2` (default) | positive scalar

Flow area at the moist air port **B2**.

### Moist Air 1

### **Nominal operating condition** — Nominal operating condition `Heat transfer from Moist Air 1 to Moist Air 2` (default) | `Heat transfer from Moist Air 2 to Moist Air 1`

Nominal operating condition:

- `Heat transfer from Moist Air 1 to Moist Air
  2` — The moist air 1 is cooled and the moist
  air 2 is heated.
- `Heat transfer from Moist Air 2 to Moist Air
  1` — The moist air 2 is cooled and the moist
  air 1 is heated.

This setting relates only to the nominal operating condition
parameters. It does not mean that heat transfer can only happen in the
specified direction during simulation.

### **Nominal mass flow rate** — Mass flow rate between moist air 1 ports during nominal operating condition `0.1 kg/s` (default) | positive scalar

Mass flow rate from port **A1** to port
**B1** during the nominal operating
condition.

### **Nominal pressure drop** — Pressure drop between moist air 1 ports during nominal operating condition `0.01 MPa` (default) | positive scalar

Pressure drop from port **A1** to port
**B1** during the nominal operating
condition.

### **Nominal inlet pressure** — Pressure at the moist air 1 inlet `0.101325 MPa` (default) | positive scalar

Pressure at the moist air 1 inlet of the heat exchanger during nominal
operating condition.

### **Nominal inlet temperature** — Temperature at the moist air 1 inlet `333.15 K` (default) | positive scalar

Temperature at the moist air 1 inlet of the heat exchanger during the
nominal operating condition.

### **Inlet humidity specification** — Quantity used to describe the humidity level at the moist air 1 side inlet `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Select quantity used to describe the humidity level at the inlet
during the nominal operating condition.

### **Nominal inlet relative humidity** — Relative humidity at the inlet `0.5` (default) | scalar in the range [0,1]

Relative humidity at the moist air 1 inlet of the heat exchanger
during the nominal operating conditions.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Relative
humidity`.

### **Nominal inlet specific humidity** — Specific humidity at the inlet `0.01` (default) | scalar in the range [0,1]

Specific humidity, defined as the mass fraction of water vapor in a
moist air 1 mixture, at the moist air inlet of the heat exchanger during
the nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Specific
humidity`.

### **Nominal inlet water vapor mole fraction** — Mole fraction of water vapor at the inlet `0.01` (default) | scalar in the range [0,1]

Mole fraction of water vapor in a moist air 1 mixture at the moist air
inlet of the heat exchanger during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Mole
fraction`.

### **Nominal inlet humidity ratio** — Humidity ratio at the inlet `0.01` (default) | positive scalar in the range [0,1]

Humidity ratio, defined as the mass ratio of water vapor to dry air
and trace gas, at the moist air 1 inlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Humidity
ratio`.

### **Nominal inlet wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Wet-bulb temperature at the moist air 1 inlet of the heat exchanger
during the nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Wet-bulb
temperature`.

### **Inlet trace gas specification** — Quantity used to describe trace gas level at the inlet `Mass fraction` (default) | `Mole fraction`

Select quantity used to describe the trace gas level at the inlet
during the nominal operating condition: mass fraction or mole
fraction.

### **Nominal inlet trace gas mass fraction** — Mass fraction of trace gas at the inlet `0.001` (default) | scalar in the range [0,1]

Mass fraction of trace gas in a moist air 1 mixture at the moist air
inlet of the heat exchanger during the nominal operating
condition.

This parameter is ignored if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is set to
`None`.

#### Dependencies

To enable this parameter, set **Inlet trace gas
specification** to `Mass
fraction`.

### **Nominal inlet trace gas mole fraction** — Mole fraction of trace gas at the inlet `0.001` (default) | scalar in the range [0,1]

Mole fraction of trace gas in a moist air 1 mixture at the moist air
inlet of the heat exchanger during the nominal operating
condition.

This parameter is ignored if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is set to
`None`.

#### Dependencies

To enable this parameter, set **Inlet trace gas
specification** to `Mole
fraction`.

### **Heat transfer capacity specification** — How to specify heat transfer capacity of moist air 1 `Rate of heat transfer` (default) | `Outlet condition`

Whether to specify the performance of the heat exchanger for the moist
air 1 at the nominal operating condition directly, by the rate of heat
transfer, or indirectly, by the outlet condition.

#### Dependencies

To enable this parameter, set **Nominal operating
condition** to `Heat transfer from Moist
Air 2 to Moist Air 1`.

### **Nominal rate of heat transfer** — Rate of heat transfer `1 kW` (default) | positive scalar

Rate of heat transfer. The **Nominal Operating
condition** parameter determines the network that the heat
transfers from and to:

- If **Nominal operating condition** is
  `Heat transfer from Moist Air 1 to Moist Air
  2`, this parameter is the rate of the heat
  transfer from the moist air 1 to the moist air 2 during the
  nominal operating condition.
- If **Nominal operating condition** is
  `Heat transfer from Moist Air 2 to Moist Air
  1`, this parameter is the rate of the heat
  transfer from the moist air 1 to the moist air 2 during the
  nominal operating condition.

#### Dependencies

To enable this parameter, set either:

- **Nominal operating condition** to
  `Heat transfer from Moist Air 1 to Moist
  Air 2`.
- **Nominal operating condition** to
  `Heat transfer from Moist Air 2 to Moist
  Air 1` and **Heat transfer
  capacity specification** to
  `Rate of heat
  transfer`.

### **Nominal outlet temperature** — Outlet temperature `323.15 K` (default) | positive scalar

Temperature at the outlet of the moist air 1 side of the heat
exchanger during the nominal operating condition.

#### Dependencies

To enable this parameter, set **Nominal operating
condition** to `Heat transfer from Moist
Air 2 to Moist Air 1` and **Heat transfer
capacity specification** to `Outlet
condition`.

### **Moist air 1 volume** — Total volume of moist air on side 1 of the heat exchanger `0.1 m^3` (default) | positive scalar

Total volume of moist air on side 1 of the heat exchanger.

### **Initialize moist air 1 to nominal operating conditions** — Option for initializing moist air 1 `on` (default) | `off`

Option to initialize the moist air 1 to nominal operating conditions
or specified values. If you select this parameter, the block initializes
the moist air 1 to the nominal operating conditions. If you clear this
check box, you can specify the initial conditions directly with
additional parameters.

### **Initial moist air 1 pressure** — Moist air 1 pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Moist air 1 pressure at the start of the simulation.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box.

### **Initial moist air 1 temperature** — Moist air temperature at start of simulation `293.15 K` (default) | positive scalar | two-element vector

Moist air 1 temperature at the start of simulation. If the value is a
scalar, then the initial temperature is assumed uniform. If the value is
a two-element vector, then the initial temperature is assumed to vary
linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box.

### **Initial humidity specification** — Quantity used to describe the initial humidity level `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Select quantity used to describe the initial humidity level: relative
humidity, specific humidity, water vapor mole fraction, or humidity
ratio.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box.

### **Initial moist air 1 relative humidity** — Relative humidity at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Moist air 1 relative humidity at the start of simulation. If the value
is a scalar, then the initial relative humidity is assumed uniform. If
the value is a two-element vector, then the initial relative humidity is
assumed to vary linearly between ports **A1** and
**B1**, with the first element corresponding to
port **A1** and the second element corresponding to
port **B1**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Relative humidity`.

### **Initial moist air 1 specific humidity** — Specific humidity at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Moist air 1 specific humidity, defined as the mass fraction of water
vapor in a moist air mixture, at the start of simulation. If the value
is a scalar, then the initial specific humidity is assumed uniform. If
the value is a two-element vector, then the initial specific humidity is
assumed to vary linearly between ports **A1** and
**B1**, with the first element corresponding to
port **A1** and the second element corresponding to
port **B1**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Specific humidity`.

### **Initial moist air 1 water vapor mole fraction** — Mole fraction of water vapor at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of water vapor in a moist air 1 mixture at the start of
simulation. If the value is a scalar, then the initial mole fraction is
assumed uniform. If the value is a two-element vector, then the initial
mole fraction is assumed to vary linearly between ports
**A1** and **B1**, with the first
element corresponding to port **A1** and the second
element corresponding to port **B1**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Mole fraction`.

### **Initial moist air 1 humidity ratio** — Humidity ratio at start of simulation `0.01` (default) | positive scalar in the range [0,1] | two-element vector

Moist air 1 humidity ratio, defined as the mass ratio of water vapor
to dry air and trace gas, at the start of simulation. If the value is a
scalar, then the initial humidity ratio is assumed uniform. If the value
is a two-element vector, then the initial humidity ratio is assumed to
vary linearly between ports **A1** and
**B1**, with the first element corresponding to
port **A1** and the second element corresponding to
port **B1**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Humidity ratio`.

### **Initial moist air 1 wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Wet-bulb temperature at the start of the simulation. The block uses
this value to calculate humidity.

This parameter can be a scalar or a two-element vector. A scalar value
represents the mean initial wet-bulb temperature in the channel. A
vector value represents the initial wet-bulb temperature at the inlet
and outlet in the form [`inlet`,
`outlet`]. The block calculates a linear gradient
between the two ports. The inlet and the outlet ports are identified
according to the initial flow direction.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Wet-bulb temperature`.

### **Initial trace gas specification** — Quantity used to describe initial trace gas level `Mass fraction` (default) | `Mole fraction`

Select the quantity used to describe the trace gas level at the start
of simulation: mass fraction or mole fraction.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box.

### **Initial moist air 1 trace gas mass fraction** — Mass fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mass fraction of trace gas in a moist air 1 mixture at the start of
simulation. If the value is a scalar, then the initial mass fraction is
assumed uniform. If the value is a two-element vector, then the initial
mass fraction is assumed to vary linearly between ports
**A1** and **B1**, with the first
element corresponding to port **A1** and the second
element corresponding to port **B1**.

This parameter is ignored if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is set to
`None`.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box and set
**Initial trace gas specification** to
`Mass fraction`.

### **Initial moist air 1 trace gas mole fraction** — Mole fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of trace gas in a moist air 1 mixture at the start of
simulation. If the value is a scalar, then the initial mole fraction is
assumed uniform. If the value is a two-element vector, then the initial
mole fraction is assumed to vary linearly between ports
**A1** and **B1**, with the first
element corresponding to port **A1** and the second
element corresponding to port **B1**.

This parameter is ignored if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is set to
`None`.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box and set
**Initial trace gas specification** to
`Mole fraction`.

### **Initial mass ratio of water droplets to moist air** — Ratio of water droplets to moist air `0` (default) | positive scalar

Initial mass ratio of water droplets to moist air.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
1 to nominal operating conditions** check box.

### **Relative humidity at saturation** — Relative humidity point of condensation `1` (default) | nonnegative scalar

Relative humidity point of condensation. Condensation occurs above
this value. In most cases, this value is 1, that is, 100%. A value
greater than 1 indicates a supersaturated vapor.

### **Water vapor condensation time constant** — Time scale for condensation `1e-3 s` (default) | positive scalar

Characteristic time scale at which an oversaturated moist air volume
returns to saturation by condensing out excess humidity.

### **Water droplets evaporation time constant** — Time scale for evaporation `1e-3 s` (default) | positive scalar

Characteristic time scale at which water droplets evaporate to
vapor.

### **Fraction of condensate entrained as water droplets** — Fraction of condensate in water droplets `1` (default) | scalar in the range [0,1]

Fraction of the condensate in the moist air that is entrained as water
droplets.

### Moist Air 2

### **Nominal mass flow rate** — Mass flow rate between moist air 2 ports during nominal operating condition `0.1 kg/s` (default) | positive scalar

Mass flow rate from port **A2** to port
**B2** during the nominal operating
condition.

### **Nominal pressure drop** — Pressure drop between moist air 2 ports during nominal operating condition `0.001 MPa` (default) | positive scalar

Pressure drop from port **A2** to port
**B2** during the nominal operating
condition.

### **Nominal inlet pressure** — Pressure at the moist air 2 side inlet `0.101325 MPa` (default) | positive scalar

Pressure at the moist air 2 inlet of the heat exchanger during nominal
operating condition.

### **Nominal inlet temperature** — Temperature at the moist air 2 side inlet `293.15 K` (default) | positive scalar

Temperature at the moist air 2 inlet of the heat exchanger during the
nominal operating condition.

### **Inlet humidity specification** — Quantity used to describe the humidity level at the moist air side inlet `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Select quantity used to describe the humidity level at the inlet
during the nominal operating condition.

### **Nominal inlet relative humidity** — Relative humidity at the inlet `0.5` (default) | scalar in the range [0,1]

Relative humidity at the moist air 2 inlet of the heat exchanger
during the nominal operating conditions.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Relative
humidity`.

### **Nominal inlet specific humidity** — Specific humidity at the inlet `0.01` (default) | scalar in the range [0,1]

Specific humidity, defined as the mass fraction of water vapor in a
moist air mixture, at the moist air 2 inlet of the heat exchanger during
the nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Specific
humidity`.

### **Nominal inlet water vapor mole fraction** — Mole fraction of water vapor at the inlet `0.01` (default) | scalar in the range [0,1]

Mole fraction of water vapor in a moist air mixture at the moist air 2
inlet of the heat exchanger during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Mole
fraction`.

### **Nominal inlet humidity ratio** — Humidity ratio at the inlet `0.01` (default) | positive scalar in the range [0,1]

Humidity ratio, defined as the mass ratio of water vapor to dry air
and trace gas, at the moist air 2 inlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Humidity
ratio`.

### **Nominal inlet wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Wet-bulb temperature at the moist air 2 inlet of the heat exchanger
during the nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet humidity
specification** to `Wet-bulb
temperature`.

### **Inlet trace gas specification** — Quantity used to describe trace gas level at the inlet `Mass fraction` (default) | `Mole fraction`

Select quantity used to describe the trace gas level at the inlet
during the nominal operating condition: mass fraction or mole
fraction.

### **Nominal inlet trace gas mass fraction** — Mass fraction of trace gas at the inlet `0.001` (default) | scalar in the range [0,1]

Mass fraction of trace gas in a moist air mixture at the moist air 2
inlet of the heat exchanger during the nominal operating
condition.

This parameter is ignored if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is set to
`None`.

#### Dependencies

To enable this parameter, set **Inlet trace gas
specification** to `Mass
fraction`.

### **Nominal inlet trace gas mole fraction** — Mole fraction of trace gas at the inlet `0.001` (default) | scalar in the range [0,1]

Mole fraction of trace gas in a moist air mixture at the moist air 2
inlet of the heat exchanger during the nominal operating
condition.

This parameter is ignored if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is set to
`None`.

#### Dependencies

To enable this parameter, set **Inlet trace gas
specification** to `Mole
fraction`.

### **Moist air 2 volume** — Total volume of moist air on side 2 of the heat exchanger `0.1 m^3` (default) | positive scalar

Total volume of moist air on side 2 of the heat exchanger.

### **Initialize moist air 2 to nominal operating conditions** — Option for initializing moist air `on` (default) | `off`

Option to initialize the moist air 2 to nominal operating conditions
or specified values. If you select this parameter, the block initializes
the moist air to the nominal operating conditions. If you clear this
check box, you can specify the initial conditions directly with
additional parameters.

### **Initial moist air 2 pressure** — Moist air pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Moist air 2 pressure at the start of the simulation.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box.

### **Initial moist air 2 temperature** — Moist air temperature at start of simulation `293.15 K` (default) | positive scalar | two-element vector

Moist air 2 temperature at the start of simulation. If the value is a
scalar, then the initial temperature is assumed uniform. If the value is
a two-element vector, then the initial temperature is assumed to vary
linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box.

### **Initial humidity specification** — Quantity used to describe the initial humidity level `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Select quantity used to describe the initial humidity level: relative
humidity, specific humidity, water vapor mole fraction, or humidity
ratio.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box.

### **Initial moist air 2 relative humidity** — Relative humidity at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Moist air 2 relative humidity at the start of simulation. If the value
is a scalar, then the initial relative humidity is assumed uniform. If
the value is a two-element vector, then the initial relative humidity is
assumed to vary linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Relative humidity`.

### **Initial moist air 2 specific humidity** — Specific humidity at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Moist air 2 specific humidity, defined as the mass fraction of water
vapor in a moist air mixture, at the start of simulation. If the value
is a scalar, then the initial specific humidity is assumed uniform. If
the value is a two-element vector, then the initial specific humidity is
assumed to vary linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Specific humidity`.

### **Initial moist air 2 water vapor mole fraction** — Mole fraction of water vapor at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of water vapor in a moist air 2 mixture at the start of
simulation. If the value is a scalar, then the initial mole fraction is
assumed uniform. If the value is a two-element vector, then the initial
mole fraction is assumed to vary linearly between ports
**A2** and **B2**, with the first
element corresponding to port **A2** and the second
element corresponding to port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Mole fraction`.

### **Initial moist air 2 humidity ratio** — Humidity ratio at start of simulation `0.01` (default) | positive scalar in the range [0,1] | two-element vector

Moist air 2 humidity ratio, defined as the mass ratio of water vapor
to dry air and trace gas, at the start of simulation. If the value is a
scalar, then the initial humidity ratio is assumed uniform. If the value
is a two-element vector, then the initial humidity ratio is assumed to
vary linearly between ports **A2** and
**B2**, with the first element corresponding to
port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Humidity ratio`.

### **Initial moist air 2 wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Wet-bulb temperature at the start of the simulation. The block uses
this value to calculate humidity.

This parameter can be a scalar or a two-element vector. A scalar value
represents the mean initial wet-bulb temperature in the channel. A
vector value represents the initial wet-bulb temperature at the inlet
and outlet in the form [`inlet`,
`outlet`]. The block calculates a linear gradient
between the two ports. The inlet and the outlet ports are identified
according to the initial flow direction.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box and set
**Initial humidity specification** to
`Wet-bulb temperature`.

### **Initial trace gas specification** — Quantity used to describe initial trace gas level `Mass fraction` (default) | `Mole fraction`

Select the quantity used to describe the trace gas level at the start
of simulation: mass fraction or mole fraction.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box.

### **Initial moist air 2 trace gas mass fraction** — Mass fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mass fraction of trace gas in a moist air mixture at the start of
simulation. If the value is a scalar, then the initial mass fraction is
assumed uniform. If the value is a two-element vector, then the initial
mass fraction is assumed to vary linearly between ports
**A2** and **B2**, with the first
element corresponding to port **A2** and the second
element corresponding to port **B2**.

This parameter is ignored if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is set to
`None`.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box and set
**Initial trace gas specification** to
`Mass fraction`.

### **Initial moist air 2 trace gas mole fraction** — Mole fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of trace gas in a moist air 2 mixture at the start of
simulation. If the value is a scalar, then the initial mole fraction is
assumed uniform. If the value is a two-element vector, then the initial
mole fraction is assumed to vary linearly between ports
**A2** and **B2**, with the first
element corresponding to port **A2** and the second
element corresponding to port **B2**.

This parameter is ignored if the **Trace gas model**
parameter in the Moist Air Properties (MA) block is set to
`None`.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box and set
**Initial trace gas specification** to
`Mole fraction`.

### **Initial mass ratio of water droplets to moist air** — Ratio of water droplets to moist air `0` (default) | positive scalar

Initial mass ratio of water droplets to moist air.

#### Dependencies

To enable this parameter, clear the **Initialize moist air
2 to nominal operating conditions** check box.

### **Relative humidity at saturation** — Relative humidity point of condensation `1` (default) | nonnegative scalar

Relative humidity point of condensation. Condensation occurs above
this value. In most cases, this value is 1, that is, 100%. A value
greater than 1 indicates a supersaturated vapor.

### **Water vapor condensation time constant** — Time scale for condensation `1e-3 s` (default) | positive scalar

Characteristic time scale at which an oversaturated moist air volume
returns to saturation by condensing out excess humidity.

### **Water droplets evaporation time constant** — Time scale for evaporation `1e-3 s` (default) | positive scalar

Characteristic time scale at which water droplets evaporate to
vapor.

### **Fraction of condensate entrained as water droplets** — Fraction of condensate in water droplets `1` (default) | scalar in the range [0,1]

Fraction of the condensate in the moist air that is entrained as water
droplets.

### Correlation Coefficients

### **a in Nu = a\*Re^b\*Pr^c for moist air 1** — Correlation coefficient for moist air 1 `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a
function of the Reynolds number and Prandtl number for moist air 1. The
default value is based on the Colburn equation.

### **b in Nu = a\*Re^b\*Pr^c for moist air 1** — Reynolds number exponent in correlation for moist air 1 `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a
function of the Reynolds number and Prandtl number for moist air 1. The
default value is based on the Colburn equation.

### **c in Nu = a\*Re^b\*Pr^c for moist air 1** — Prandtl number exponent in correlation for moist air 1 `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a
function of the Reynolds number and Prandtl number for moist air 1. The
default value is based on the Colburn equation.

### **a in Nu = a\*Re^b\*Pr^c for moist air 2** — Correlation coefficient for moist air 2 `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a
function of the Reynolds number and Prandtl number for moist air 2. The
default value is based on the Colburn equation.

### **b in Nu = a\*Re^b\*Pr^c for moist air 2** — Reynolds number exponent in correlation for moist air 2 `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a
function of the Reynolds number and Prandtl number for moist air 2. The
default value is based on the Colburn equation.

### **c in Nu = a\*Re^b\*Pr^c for moist air 2** — Prandtl number exponent in correlation for moist air 2 `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a
function of the Reynolds number and Prandtl number for moist air 2. The
default value is based on the Colburn equation.

## Libraries

Simscape / Fluids / Heat Exchangers / Moist Air

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Heat exchanger based on performance data between two moist air networks

The System-Level Heat Exchanger (MA-MA) block models a
heat exchanger based on performance data between two distinct moist air networks. Each
network has its own set of fluid properties.

The block uses performance data from the heat exchanger datasheet, rather than the
detailed geometry of the exchanger. You can adjust the size and performance of the heat
exchanger during design iterations, or model heat exchangers with uncommon geometries.
You can also use this block to model heat exchangers with a certain level of performance
at an early design stage, when detailed geometry data is not yet available. You
parameterize the block by the nominal operating condition. The heat exchanger is sized
to match the specified performance at the nominal operating condition at steady
state.

Both moist air sides model water vapor condensation based on convective water vapor
mass transfer with the heat transfer surface. The block removes condensed water from the
moist air flow.

### Heat Transfer

The block divides each moist air flow into three segments of equal size and
calculates heat transfer between the fluids is in each segment. For simplicity, the
equation in this section are for one segment.

If you clear the **Enable wall thermal mass** check box, then the
heat balance in the heat exchanger is

Qseg,MA1+Qseg,MA2=0,

where:

- *Qseg,MA1* is the heat flow rate
  from the wall that is the heat transfer surface to the moist air side 1 in
  the segment.
- *Qseg,MA2* is the heat flow rate
  from the wall to the moist air side 2 in the segment.

If you select **Enable wall thermal mass**, then the heat balance
in the heat exchanger is

Qseg,MA1+Qseg,MA2=−MwallcpwallNdTseg,walldt,

where:

- *M*wall is the mass of the
  wall.
- *c*pwall is
  the specific heat of the wall.
- *N* = 3 is the number of segments.
- *T*seg,wall is the average wall
  temperature in the segment.
- *t* is time.

The heat flow rate from the wall to each segment it segment is

Qseg,MA=UAseg,MAc¯pseg,MA(h¯seg,wall−h¯seg,MA)+m˙w,seg,condhl,wall,

where:

- *UA*seg,MA is the heat transfer
  conductance for the moist air in the segment.
- c¯pseg,MA is the moist air mixture specific heat per unit mass of
  dry air and trace gas in the segment.
- h¯seg,wall is the moist air mixture enthalpy per unit mass of dry air
  and trace gas at the average wall segment temperature.
- h¯seg,MA is the moist air mixture enthalpy per unit mass of dry air
  and trace gas in the segment.
- m˙w,seg,cond is the rate of water vapor condensation on the wall
  surface.
- *h*l,wall is the specific enthalpy
  of liquid water at the average wall segment temperature.

Using mixture enthalpy in this equation accounts for both differences in
temperature and differences in humidity due to condensation [3].

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

**Note**

In equations, the bar above the variables indicates that they are quantities
for the moist air mixture divided by the mass of dry air and trace gas only, as
opposed to dividing by the mass of the whole mixture. The whole mixture includes
dry air, water vapor, and trace gas.

### Moist Air Heat Transfer Correlation

The heat transfer conductance on each side of the heat exchanger is

UAseg,MA=aMA(Reseg,MA)bMA(Prseg,MA)cMAkseg,MAGMAN,

where:

- *a*MA,
  *b*MA, and
  *c*MA are the coefficients of
  the Nusselt number correlation. These coefficients are block parameters in
  the **Correlation Coefficients** section.
- *Reseg,MA* is the average Reynolds
  number for the segment.
- *Prseg,MA* is the average Prandtl
  number for the segment.
- *kseg,MA* is the average thermal
  conductivity for the segment.
- *GMA* is the geometry scale factor
  for the moist air side of the heat exchanger. The block calculates the
  geometry scale factor so that the total heat transfer over all segments
  matches the specified performance at the nominal operating
  conditions.

The average Reynolds number is

Reseg,MA=m˙seg,MADref,MAμseg,MASref,MA,

where:

- m˙seg,MA is the mass flow rate through the segment.
- *μseg,MA* is the average dynamic
  viscosity for the segment.
- *Dref,MA* is an arbitrary
  reference diameter.
- *Sref,MA* is an arbitrary
  reference flow area.

**Note**

The *Dref,MA* and
*Sref,MA* terms are included in
this equation for unit calculation purposes only, to make
*Reseg,MA* nondimensional. The
values of *Dref,MA* and
*Sref,MA* are arbitrary because
the *GMA* calculation overrides these
values.

### Condensation

The equation that describes the heat flow rate from the wall to the moist air in
the segment uses the average moist air mixture enthalpy, h¯seg,MA, and the wall segment moist air mixture enthalpy, h¯seg,wall.

The average moist air mixture enthalpy is based on the temperature and humidity of
the moist air flow through the segment

h¯seg,MA=hseg,ag,MA+Wseg,MAhseg,w,MA,

where:

- *h*seg,ag,MA is the average
  specific enthalpy of dry air and trace gas for the segment.
- *h*seg,w,MA is the average
  specific enthalpy of water vapor for the segment.
- *W*seg,MA is the humidity ratio of
  the segment.

The wall segment moist air mixture enthalpy is based on the temperature and
humidity at the wall segment

h¯seg,wall=hseg,ag,wall+Wseg,wallhseg,w,wall,

where:

- *h*seg,ag,wall is the specific
  enthalpy of dry air and trace gas at the wall segment temperature.
- *h*seg,w,wall is the specific
  enthalpy of water vapor at the wall segment temperature.
- *W*seg,wall is the humidity ratio
  at the wall segment:

  Wseg,wall=min(Wseg,MA,Wseg,s,wall),

  where *W*seg,s,wall is the
  saturated humidity ratio at the wall segment temperature. In other words,
  the humidity ratio at the wall is the same as the humidity ratio of the
  moist air flow but not more than the maximum that can be supported at the
  wall segment temperature.

When *W*seg,s,wall <
*W*seg,MA, water vapor condensation
occurs on the wall surface. The rate of water vapor condensation is

m˙w,seg,cond=UAseg,MAc¯pseg,MA(Wseg,MA−Wseg,wall).

The block assumes that the condensed water is drained from the wall surface and is
thus removed from the moist air flow downstream.

### Pressure Loss

The pressure losses on each side of the heat exchanger are

pA,MA−pMA=KMA2m˙A,MAm˙2A,MA+m˙2thres,MA2ρavg,2PpB,MA−pMA=KMA2m˙B,MAm˙2B,MA+m˙2thres,MA2ρavg,MA

where:

- *pA,MA* and
  *pB,MA* are the pressures at
  ports **A1** and **B1** or
  **A2** and **B2**.
- *pMA* is internal moist air
  pressure at which the heat transfer is calculated.
- m˙A,MA and m˙B,MA are the mass flow rates into ports **A1**
  and **B1** or **A2** and
  **B2**.
- *ρ*avg,MA is the average moist air
  density over all segments.
- m˙thres,MA is the laminar threshold for pressure loss, approximated
  as 1e-4 of the nominal mass flow rate. The block calculates the pressure
  loss coefficient, *K*MA, so that
  *p*A,MA –
  *p*B,MA matches the nominal
  pressure loss at the nominal mass flow rate.

### Moist Air Mass and Energy Conservation

The mass conservation on each side of the heat exchanger for the overall moist air
mixture flow is

(dpMAdt∑segments(∂ρseg,MA∂p)+∑segments(dTseg,MAdt∂ρseg,MA∂T+dxw,seg,MAdt∂ρseg,MA∂xw+dxg,seg,MAdt∂ρseg,MA∂xg))VMAN=m˙A,MA+m˙B,MA−∑segments(m˙w,seg,cond+m˙w,seg,conv)+∑segmentsm˙d,seg,evap,

where:

- ∂ρseg,MA∂p is the partial derivative of density with respect to
  pressure for the segment.
- ∂ρseg,MA∂T is the partial derivative of density with respect to
  temperature for the segment.
- ∂ρseg,MA∂xw is the partial derivative of density with respect to
  specific humidity for the segment.
- ∂ρseg,MA∂xg is the partial derivative of density with respect to trace
  gas mass fraction for the segment.
- *xw,seg,MA* is the
  *specific humidity*, also referred to as the water
  vapor mass fraction, for the segment.
- *xg,seg,MA* is the trace gas mass
  fraction for the segment.
- *VMA* is the total moist air
  volume.
- m˙w,seg,conv is the rate of
  condensation on the wall surface for the segment.
- m˙d,seg,evap is the rate of water
  droplet evaporation for the segment.

The summation is over all segments.

**Note**

Although the block divides each moist air flow into *N*=3
segments for heat transfer calculations, it assumes all segments on one side are
at the same internal pressure, *p*MA.
Consequentially, *p*MA is outside of the
summation.

The energy conservation equation for each segment is

dTseg,MAdt(c¯seg,MA−Rseg)MMAN+ua,seg,MA(m˙seg,in,MA−m˙seg,out,MA)+(uw,seg,MA−ua,seg,MA)(m˙w,seg,in,MA−m˙w,seg,out,MA)+(ug,seg,MA−ua,seg,MA)(m˙g,seg,in,MA−m˙g,seg,out,MA)+hd(m˙d,seg,in,MA−m˙d,seg,out,MA)=Φseg,in,MA−Φseg,out,MA+Qseg,MA−(1−λd)(m˙w,seg,condhd+m˙w,seg,convhl,wall),

where:

- *ua,seg,MA* is the dry air
  specific internal energy for the segment.
- *ug,seg,MA* is the trace gas
  specific internal energy for the segment.
- *uw,seg,MA* is the water vapor
  specific internal energy for the segment.
- *MMA* is the total moist air
  mass.
- m˙seg,in,MA and m˙seg,out,MA are the moist air mass flow rates into and out of the
  segment.
- m˙w,seg,in,MA and m˙w,seg,out,MA are the water vapor mass flow rates into and out of the
  segment.
- m˙g,seg,in,MA and m˙g,seg,out,MA are the trace gas mass flow rates into and out of the
  segment.
- m˙d,seg,in,MA and m˙d,seg,out,MA are the water droplets mass flow rate into and out of the
  segment.
- *Rseg* is the segment volume
  specific gas constant.
- *Φ*seg,in,MA and
  *Φ*seg,out,MA are the energy
  flow rates into and out of the segment.
- *hd* is the water droplet specific
  enthalpy in the segment.
- *λd* is the value of the
  **Fraction of condensate entrained as water droplets**
  parameter.

The block assumes the mass flow rates between segments are linearly distributed
between the values of m˙A,MA and m˙B,MA.

The water vapor mass conservation equation for each segment is

dxw,seg,MAdtMMAN+xw,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙w,seg,in,MA−m˙w,seg,out,MA−m˙w,seg,cond−m˙w,seg,conv+m˙d,seg,evap.

The trace gas mass conservation equation for each segment is

dxg,seg,MAdtMMAN+xg,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙g,seg,in,MA−m˙g,seg,out,MA.

The water droplet mass balance conservation equation for each segment is

drd,segdtMMAN+rd,seg(m˙seg,in,MA−m˙seg,out,MA)=m˙d,seg,in−m˙d,seg,out+λd(m˙w,seg,cond+m˙w,seg,conv)−m˙d,seg,evap,

where *rd,seg* is the
mass ratio of the water droplets to the moist air in the fluid volume in the
segment.

**Note**

If the **Trace gas model** parameter is
`None` in the Moist Air
Properties (MA) block, the moist air network does not model
trace gas. In this case, in the System-Level Heat Exchanger (MA-MA) block on the corresponding side of
the heat exchanger, the conservation equation for trace gas is set to 0.

If you clear the **Enable entrained water droplets** in the
 Moist Air Properties (MA) block, the moist
air network does not model entrained water droplets. In this case, in the
System-Level Heat Exchanger (MA-MA) block on the corresponding side of the heat exchanger, the
conservation equation for water droplets is set to 0.

### Assumptions and Limitations

- When determining the heat exchanger size, the block ignores the value of
  the **Fraction of condensate entrained as water droplets**
  parameters and assumes that the condensate is not entrained as
  droplets.
