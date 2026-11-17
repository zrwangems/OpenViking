---
type: simulink-block
title: 'System-Level Condenser Evaporator (2P-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid - Moist Air'
documentation_page: 'systemlevelcondenserevaporator2pma'
documentation_source_path: 'ref/systemlevelcondenserevaporator2pma.html'
language: en
---

# System-Level Condenser Evaporator (2P-MA)

## Ports
```yaml
ports:
- name: Q1
  summary: Rate of heat transfer to two-phase fluid, W physical signal
  direction: output
- name: Q2
  summary: Rate of heat transfer to moist air, W physical signal
  direction: output
- name: W
  summary: Moist air condensation rate, kg/s physical signal
  direction: output
- name: A1
  summary: Two-phase fluid port two-phase fluid
  direction: conserving
- name: B1
  summary: Two-phase fluid port two-phase fluid
  direction: conserving
- name: A2
  summary: Moist air port moist air
  direction: conserving
- name: B2
  summary: Moist air port moist air
  direction: conserving
```

### Output

### **Q1** — Rate of heat transfer to two-phase fluid, W physical signal

Rate of heat transfer to two-phase fluid, returned as a physical signal, in W. The
physical signals at ports **Q1** and **Q2** are
usually equal in value with opposite sign. However, if you select **Enable
wall thermal mass**, then these two signals may have different values
because the wall may absorb and release some of the heat being transferred.

### **Q2** — Rate of heat transfer to moist air, W physical signal

Rate of heat transfer to moist air, returned as a physical signal, in W. The
physical signals at ports **Q1** and **Q2** are
usually equal in value with opposite sign. However, if you select **Enable
wall thermal mass**, then these two signals may have different values
because the wall may absorb and release some of the heat being transferred.

### **W** — Moist air condensation rate, kg/s physical signal

Water condensation rate that leaves the moist air flow, returned as a physical
signal. The value of this port does not include the portion of condensation that is
entrained as water droplets. The condensate does not accumulate on the heat transfer
surface.
### Conserving

### **A1** — Two-phase fluid port two-phase fluid

Inlet or outlet port associated with the two-phase fluid.

### **B1** — Two-phase fluid port two-phase fluid

Inlet or outlet port associated with the two-phase fluid.

### **A2** — Moist air port moist air

Inlet or outlet port associated with the moist air.

### **B2** — Moist air port moist air

Inlet or outlet port associated with the moist air.
## Parameters
```yaml
parameters:
- name: Flow arrangement at nominal operating conditions
  summary: Flow path alignment Counter flow - Two-Phase Fluid 1 flows from A to B, Moist Air 2 flows from B to A (default)
    | Parallel flow - Both fluids flow from A to B | Cross flow - Both fluids flow from A to B
  group: Configuration
- name: Enable wall thermal mass
  summary: Whether to enable effect of thermal mass on heat transfer surface off (default) | on
  group: Configuration
- name: Wall mass
  summary: Mass of heat transfer surface 1 kg (default) | positive scalar
  group: Configuration
- name: Wall specific heat
  summary: Specific heat of heat transfer surface 490 J/(K*kg) (default) | positive scalar
  group: Configuration
- name: Initialize wall temperature to nominal operating conditions
  summary: Option for initializing wall temperature on (default) | off
  group: Configuration
- name: Initial wall temperature
  summary: Initial temperature of wall 293.15 K (default) | positive scalar or two-element vector
  group: Configuration
- name: Cross-sectional area at port A1
  summary: Flow area at port A1 0.01 m^2 (default) | positive scalar
  group: Configuration
- name: Cross-sectional area at port B1
  summary: Flow area at port B1 0.01 m^2 (default) | positive scalar
  group: Configuration
- name: Cross-sectional area at port A2
  summary: Flow area at port A2 0.01 m^2 (default) | positive scalar
  group: Configuration
- name: Cross-sectional area at port B2
  summary: Area normal to flow at port B2 0.01 m^2 (default) | positive scalar
  group: Configuration
- name: Nominal operating condition
  summary: Select whether nominal operating condition corresponds to condenser or evaporator Condenser - heat transfer from
    Two-Phase Fluid 1 to Moist Air 2 (default) | Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid 1
  group: Two-Phase Fluid 1
- name: Nominal mass flow rate
  summary: Mass flow rate between two-phase ports during nominal operating condition 0.001 kg/s (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal pressure drop
  summary: Pressure drop between two-phase ports during nominal operating condition 0.01 MPa (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Pressure specification
  summary: Select method of pressure specification Inlet pressure (default) | Saturation pressure at specified condensing
    temperature | Saturation pressure at specified evaporating temperature
  group: Two-Phase Fluid 1
- name: Nominal inlet pressure
  summary: Pressure at the two-phase fluid side inlet 1 MPa (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal condensing temperature
  summary: Use nominal condensing temperature to specify pressure 313.15 K (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal evaporating temperature
  summary: Use nominal evaporating temperature to specify pressure 243.15 K (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Inlet condition specification
  summary: Select quantity to describe the inlet condition of the two-phase fluid Specific enthalpy (default) | Temperature
    | Vapor quality
  group: Two-Phase Fluid 1
- name: Nominal inlet specific enthalpy
  summary: Specific enthalpy at the two-phase fluid side inlet 440 kJ/kg (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal inlet temperature
  summary: Temperature at the two-phase fluid side inlet 313.15 K (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal inlet vapor quality
  summary: Vapor quality at the two-phase fluid side inlet 1 (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Heat transfer capacity specification
  summary: How to specify heat transfer capacity of the two-phase fluid Rate of heat transfer (default) | Outlet condition
  group: Two-Phase Fluid 1
- name: Nominal rate of heat transfer
  summary: Rate of heat transfer 0.1 kW (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Outlet condition specification
  summary: Select quantity for outlet condition specification Specific enthalpy (default) | Subcooling | Superheating | Vapor
    quality
  group: Two-Phase Fluid 1
- name: Nominal outlet specific enthalpy
  summary: Specific enthalpy at the two-phase fluid side outlet 250 kJ/kg (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 1
- name: Nominal subcooling
  summary: Degree of temperature below the liquid saturation temperature at the two-phase fluid side outlet 5 deltaK (default)
    | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal superheating
  summary: Degree of temperature above the vapor saturation temperature at the two-phase fluid side outlet 5 deltaK (default)
    | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal outlet vapor quality
  summary: Vapor mass fraction at the two-phase fluid side outlet 0 (default) | scalar in the range [0,1]
  group: Two-Phase Fluid 1
- name: Two-phase fluid volume
  summary: Total volume of two-phase fluid 0.001 m^3 (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Initialize two-phase fluid to nominal operating conditions
  summary: Option for initializing two-phase fluid on (default) | off
  group: Two-Phase Fluid 1
- name: Initial fluid energy specification
  summary: Initial state of the two-phase fluid Specific enthalpy (default) | Temperature | Vapor quality | Vapor void fraction
    | Specific internal energy
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid pressure
  summary: Fluid pressure at start of simulation 0.101325 MPa (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid specific enthalpy
  summary: Enthalpy per unit mass at start of simulation 1500 kJ/kg (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid temperature
  summary: Temperature at start of simulation 293.15 K (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid vapor quality
  summary: Vapor mass fraction at start of simulation 0.5 (default) | scalar in the range [0,1] | two-element vector
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid vapor void fraction
  summary: Vapor volume fraction at start of simulation 0.5 (default) | scalar in the range [0,1] | two-element vector
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid specific internal energy
  summary: Internal energy per unit mass at start of simulation 1500 kJ/kg (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 1
- name: Nominal mass flow rate
  summary: Mass flow rate between moist air ports during nominal operating condition 0.1 kg/s (default) | positive scalar
  group: Moist Air 2
- name: Nominal pressure drop
  summary: Pressure drop between moist air ports during nominal operating condition 0.001 MPa (default) | positive scalar
  group: Moist Air 2
- name: Nominal inlet pressure
  summary: Pressure at the moist air side inlet 0.101325 MPa (default) | positive scalar
  group: Moist Air 2
- name: Nominal inlet temperature
  summary: Temperature at the moist air side inlet 293.15 K (default) | positive scalar
  group: Moist Air 2
- name: Inlet humidity specification
  summary: Quantity used to describe the humidity level at the moist air side inlet Relative humidity (default) | Specific
    humidity | Mole fraction | Humidity ratio | Wet-bulb temperature
  group: Moist Air 2
- name: Nominal inlet relative humidity
  summary: Relative humidity at the inlet 0.5 (default) | scalar in the range [0,1]
  group: Moist Air 2
- name: Nominal inlet specific humidity
  summary: Specific humidity at the inlet 0.01 (default) | scalar in the range [0,1]
  group: Moist Air 2
- name: Nominal inlet water vapor mole fraction
  summary: Mole fraction of water vapor at the inlet 0.01 (default) | scalar in the range [0,1]
  group: Moist Air 2
- name: Nominal inlet humidity ratio
  summary: Humidity ratio at the inlet 0.01 (default) | positive scalar in the range [0,1]
  group: Moist Air 2
- name: Nominal inlet wet-bulb temperature
  summary: Wet-bulb temperature at the start of simulation 287 K (default) | positive scalar in the range [0,1]
  group: Moist Air 2
- name: Inlet trace gas specification
  summary: Quantity used to describe trace gas level at the inlet Mass fraction (default) | Mole fraction
  group: Moist Air 2
- name: Nominal inlet trace gas mass fraction
  summary: Mass fraction of trace gas at the inlet 0.001 (default) | scalar in the range [0,1]
  group: Moist Air 2
- name: Nominal inlet trace gas mole fraction
  summary: Mole fraction of trace gas at the inlet 0.001 (default) | scalar in the range [0,1]
  group: Moist Air 2
- name: Moist air volume
  summary: Total volume of moist air in the heat exchanger 0.1 m^3 (default) | positive scalar
  group: Moist Air 2
- name: Initialize moist air to nominal operating conditions
  summary: Option for initializing moist air on (default) | off
  group: Moist Air 2
- name: Initial moist air pressure
  summary: Moist air pressure at start of simulation 0.101325 MPa (default) | positive scalar
  group: Moist Air 2
- name: Initial moist air temperature
  summary: Moist air temperature at start of simulation 293.15 K (default) | positive scalar | two-element vector
  group: Moist Air 2
- name: Initial humidity specification
  summary: Quantity used to describe the initial humidity level Relative humidity (default) | Specific humidity | Mole fraction
    | Humidity ratio | Wet-bulb temperature
  group: Moist Air 2
- name: Initial moist air relative humidity
  summary: Relative humidity at start of simulation 0.5 (default) | scalar in the range [0,1] | two-element vector
  group: Moist Air 2
- name: Initial moist air specific humidity
  summary: Specific humidity at start of simulation 0.01 (default) | scalar in the range [0,1] | two-element vector
  group: Moist Air 2
- name: Initial moist air water vapor mole fraction
  summary: Mole fraction of water vapor at start of simulation 0.01 (default) | scalar in the range [0,1] | two-element vector
  group: Moist Air 2
- name: Initial moist air humidity ratio
  summary: Humidity ratio at start of simulation 0.01 (default) | positive scalar in the range [0,1] | two-element vector
  group: Moist Air 2
- name: Initial moist air wet-bulb temperature
  summary: Wet-bulb temperature at the start of simulation 287 K (default) | positive scalar in the range [0,1]
  group: Moist Air 2
- name: Initial trace gas specification
  summary: Quantity used to describe initial trace gas level Mass fraction (default) | Mole fraction
  group: Moist Air 2
- name: Initial moist air trace gas mass fraction
  summary: Mass fraction of trace gas at start of simulation 0.001 (default) | scalar in the range [0,1] | two-element vector
  group: Moist Air 2
- name: Initial moist air trace gas mole fraction
  summary: Mole fraction of trace gas at start of simulation 0.001 (default) | scalar in the range [0,1] | two-element vector
  group: Moist Air 2
- name: Initial mass ratio of water droplets to moist air
  summary: Ratio of water droplets to moist air 0 (default) | positive scalar
  group: Moist Air 2
- name: Relative humidity at saturation
  summary: Relative humidity point of condensation 1 (default) | nonnegative scalar
  group: Moist Air 2
- name: Water vapor condensation time constant
  summary: Time scale for condensation 1e-3 s (default) | positive scalar
  group: Moist Air 2
- name: Water droplets evaporation time constant
  summary: Time scale for evaporation 1e-3 s (default) | positive scalar
  group: Moist Air 2
- name: Fraction of condensate entrained as water droplets
  summary: Fraction of condensate in water droplets 1 (default) | scalar in the range [0,1]
  group: Moist Air 2
- name: a in Nu = a\*Re^b\*Pr^c for two-phase fluid liquid
  summary: Correlation coefficient for subcooled liquid in two-phase fluid 0.023 (default) | positive scalar
  group: Correlation Coefficients
- name: a in Nu = a\*Re^b\*Pr^c for two-phase fluid mixture
  summary: Correlation coefficient for liquid-vapor mixture in two-phase fluid 0.005 (default) | positive scalar
  group: Correlation Coefficients
- name: a in Nu = a\*Re^b\*Pr^c for two-phase fluid vapor
  summary: Correlation coefficient for superheated vapor in two-phase fluid 0.023 (default) | positive scalar
  group: Correlation Coefficients
- name: b in Nu = a\*Re^b\*Pr^c for two-phase fluid
  summary: Reynolds number exponent in correlation for two-phase fluid 0.8 (default) | positive scalar
  group: Correlation Coefficients
- name: c in Nu = a\*Re^b\*Pr^c for two-phase fluid
  summary: Prandtl number exponent in correlation for two-phase fluid 0.33 (default) | positive scalar
  group: Correlation Coefficients
- name: a in Nu = a\*Re^b\*Pr^c for moist air
  summary: Correlation coefficient for moist air 0.005 (default) | positive scalar
  group: Correlation Coefficients
- name: b in Nu = a\*Re^b\*Pr^c for moist air
  summary: Reynolds number exponent in correlation for moist air 0.8 (default) | positive scalar
  group: Correlation Coefficients
- name: c in Nu = a\*Re^b\*Pr^c for moist air
  summary: Prandtl number exponent in correlation for moist air 0.33 (default) | positive scalar
  group: Correlation Coefficients
```

### Configuration

### **Flow arrangement at nominal operating conditions** — Flow path alignment `Counter flow - Two-Phase Fluid 1 flows from A to B, Moist Air 2 flows from B to A` (default) | `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

Flow path alignment between the heat exchanger sides at nominal operating
condition. The available flow arrangements are:

- `Counter flow - Two-Phase Fluid 1 flows from A to B, Moist Air 2
  flows from B to A` — The flows run parallel to each other, in the
  opposite directions.
- `Parallel flow - Both fluids flow from A to B` —
  The flows run in the same direction.
- `Cross flow - Both fluids flow from A to B` — The
  flows run perpendicular to each other.

The choice between parallel flow and counter flow affects how the block determines
the size of the heat exchanger. The counter flow setting is the most effective, and
needs the smallest size to meet the specified performance. Conversely, parallel flow
is the least effective, and needs the biggest size to meet the specified performance.

Flow direction at the nominal condition (from A to B, or from B to A) only affects
the model initialization, when you select **Initialize two-phase fluid to
nominal operating conditions** or **Initialize moist air to nominal
operating conditions**. If you set different initial operating conditions,
the flow directions can be different.

After the block determines the size of the heat exchanger, this setting does not
play a role in how the block calculates the heat transfer during simulation. Instead,
the heat transfer depends on the flow directions during simulation. For example, if
you set the parameter to parallel flow but set up the model to run in counter flow,
then the rate of heat transfer during simulation will not match the specified
performance, even if the rest of the boundary conditions are the same.

If you set the parameter to cross flow, then the block models the flow paths as
perpendicular inside the heat exchanger, so the flow directions during simulation do
not matter.

### **Enable wall thermal mass** — Whether to enable effect of thermal mass on heat transfer surface `off` (default) | `on`

Whether to enable the effect of thermal mass on the heat transfer surface. When
you select this parameter, the block introduces additional dynamics to the simulation
and takes longer to reach steady state, but this parameter does not affect the results
at steady-state simulation.

If the fluid properties at the outlet, such as flow rate direction or fluid state,
oscillate unexpectedly during simulation, selecting this parameter may help stabilize
the results.

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

Option to initialize the wall temperature to nominal operating conditions or
specified values. If you select this parameter, the block calculates the initial wall
temperature from the nominal operating conditions specified for both fluid sides. If
you clear this parameter, you can specify the initial wall temperature directly with
the **Initial wall temperature** parameter.

#### Dependencies

To enable this parameter, select **Enable wall thermal
mass**.

### **Initial wall temperature** — Initial temperature of wall `293.15 K` (default) | positive scalar or two-element vector

Initial temperature of the wall. If you specify a scalar, the block assumes that
the initial wall temperature is uniform. If you specify a two-element vector, then the
block assumes that the initial wall temperature varies linearly between ports
**A1** and **A2** and ports
**B1** and **B2**. The first element corresponds
to the temperature at ports **A1** and **A2** and
the second element corresponds to the temperature at ports **B1** and
**B2**.

#### Dependencies

To enable this parameter, select **Enable wall thermal mass**
and clear the **Initialize wall temperature to nominal operating
conditions** check box.

### **Cross-sectional area at port A1** — Flow area at port A1 `0.01 m^2` (default) | positive scalar

Flow area at the two-phase fluid port **A1**.

### **Cross-sectional area at port B1** — Flow area at port B1 `0.01 m^2` (default) | positive scalar

Flow area at the two-phase fluid port **B1**.

### **Cross-sectional area at port A2** — Flow area at port A2 `0.01 m^2` (default) | positive scalar

Flow area at the moist air port **A2**.

### **Cross-sectional area at port B2** — Area normal to flow at port B2 `0.01 m^2` (default) | positive scalar

Flow area at the moist air port **B2**.

### Two-Phase Fluid 1

### **Nominal operating condition** — Select whether nominal operating condition corresponds to condenser or evaporator `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air 2` (default) | `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid 1`

Nominal operating condition:

- `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
  2` — The two-phase fluid is cooled and the moist air is
  heated.
- `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid 1` — The moist air is cooled and the two-phase fluid is heated.

This setting relates only to the nominal operating condition parameters. It does
not mean that heat transfer can only happen in the specified direction during
simulation.

### **Nominal mass flow rate** — Mass flow rate between two-phase ports during nominal operating condition `0.001 kg/s` (default) | positive scalar

Mass flow rate from port **A1** to port **B1**
during the nominal operating condition.

### **Nominal pressure drop** — Pressure drop between two-phase ports during nominal operating condition `0.01 MPa` (default) | positive scalar

Pressure drop from port **A1** to port **B1**
during the nominal operating condition.

### **Pressure specification** — Select method of pressure specification `Inlet pressure` (default) | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

Select the method of pressure specification:

- `Inlet pressure` — Specify the nominal inlet
  pressure.
- `Saturation pressure at specified condensing
  temperature` — Specify the nominal condensing temperature. This
  option is available if you set **Nominal operating condition** to
  `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
  2`.
- `Saturation pressure at specified evaporating
  temperature` — Specify the nominal evaporating temperature. This
  option is available if you set **Nominal operating condition** to
  `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid
  1`.

### **Nominal inlet pressure** — Pressure at the two-phase fluid side inlet `1 MPa` (default) | positive scalar

Pressure at the two-phase fluid inlet of the heat exchanger during nominal
operating condition.

#### Dependencies

To enable this parameter, set **Pressure specification** to
`Inlet pressure`.

### **Nominal condensing temperature** — Use nominal condensing temperature to specify pressure `313.15 K` (default) | positive scalar

Liquid saturation temperature at the two-phase fluid outlet of the heat exchanger
during nominal operating condition. The pressure in the heat exchanger is the
corresponding saturation pressure. The nominal condensing temperature must be less
than the critical temperature.

#### Dependencies

To enable this parameter, set **Nominal operating condition**
to `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
2` and **Pressure specification** to
`Saturation pressure at specified condensing
temperature`.

### **Nominal evaporating temperature** — Use nominal evaporating temperature to specify pressure `243.15 K` (default) | positive scalar

Vapor saturation temperature at the two-phase fluid outlet of the heat exchanger
during nominal operating condition. The pressure in the heat exchanger is the
corresponding saturation pressure. The nominal evaporating temperature must be less
than the critical temperature.

#### Dependencies

To enable this parameter, set **Nominal operating condition**
to `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid
1` and **Pressure specification** to
`Saturation pressure at specified evaporating
temperature`.

### **Inlet condition specification** — Select quantity to describe the inlet condition of the two-phase fluid `Specific enthalpy` (default) | `Temperature` | `Vapor quality`

Quantity used to describe the inlet condition of the fluid at the nominal
operating condition: temperature, specific enthalpy, or vapor quality.

### **Nominal inlet specific enthalpy** — Specific enthalpy at the two-phase fluid side inlet `440 kJ/kg` (default) | positive scalar

Specific enthalpy at the two-phase fluid inlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet condition specification**
to `Specific enthalpy`.

### **Nominal inlet temperature** — Temperature at the two-phase fluid side inlet `313.15 K` (default) | positive scalar

Temperature at the two-phase fluid inlet of the heat exchanger during the nominal
operating condition.

#### Dependencies

To enable this parameter, set **Inlet condition specification**
to `Temperature`.

### **Nominal inlet vapor quality** — Vapor quality at the two-phase fluid side inlet `1` (default) | positive scalar

Vapor quality, defined as the mass fraction of vapor in a liquid-vapor mixture, at
the two-phase fluid inlet of the heat exchanger during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **Inlet condition specification**
to `Vapor quality`.

### **Heat transfer capacity specification** — How to specify heat transfer capacity of the two-phase fluid `Rate of heat transfer` (default) | `Outlet condition`

Whether to specify the performance of the heat exchanger for the two-phase fluid
at the nominal operating condition directly, by the rate of heat transfer, or
indirectly, by the outlet condition.

### **Nominal rate of heat transfer** — Rate of heat transfer `0.1 kW` (default) | positive scalar

Rate of heat transfer. The **Nominal Operating condition**
parameter determines the network that the heat transfers from and to:

- If **Nominal operating condition** is `Condenser
  - heat transfer from Two-Phase Fluid 1 to Moist Air 2`, this
  parameter is the rate of the heat transfer from the two-phase fluid to the moist
  air during the nominal operating condition.
- If **Nominal operating condition** is `Evaporator
  - heat transfer from Moist Air 2 to Two-Phase Fluid 1` , this
  parameter is the rate of the heat transfer from the moist air to the two-phase
  fluid during the nominal operating condition.

#### Dependencies

To enable this parameter, set **Heat transfer capacity
specification** to `Rate of heat
transfer`.

### **Outlet condition specification** — Select quantity for outlet condition specification `Specific enthalpy` (default) | `Subcooling` | `Superheating` | `Vapor quality`

Select the quantity for outlet condition specification:

- `Specific enthalpy` — Specify the nominal specific
  enthalpy.
- `Subcooling` — Specify the nominal subcooling. This
  option is available if you set **Nominal operating condition** to
  `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
  2`.
- `Superheating` — Specify the nominal superheating.
  This option is available if you set **Nominal operating
  condition** to `Evaporator - heat transfer from Moist Air 2
  to Two-Phase Fluid 1`.
- `Vapor quality` — Specify the nominal vapor
  quality.

#### Dependencies

To enable this parameter, set **Heat transfer capacity
specification** to `Outlet condition`.

### **Nominal outlet specific enthalpy** — Specific enthalpy at the two-phase fluid side outlet `250 kJ/kg` (default) | positive scalar | two-element vector

Specific enthalpy at the two-phase fluid outlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Outlet condition
specification** to `Specific enthalpy`.

### **Nominal subcooling** — Degree of temperature below the liquid saturation temperature at the two-phase fluid side outlet `5 deltaK` (default) | positive scalar

Degree of temperature below the liquid saturation temperature at the two-phase
fluid outlet of the heat exchanger during the nominal operating condition.

#### Dependencies

To enable this parameter, set **Outlet condition
specification** to `Subcooling`.

### **Nominal superheating** — Degree of temperature above the vapor saturation temperature at the two-phase fluid side outlet `5 deltaK` (default) | positive scalar

Degree of temperature above the vapor saturation temperature at the two-phase
fluid outlet of the heat exchanger during the nominal operating condition.

#### Dependencies

To enable this parameter, set **Outlet condition
specification** to `Superheating`.

### **Nominal outlet vapor quality** — Vapor mass fraction at the two-phase fluid side outlet `0` (default) | scalar in the range [0,1]

Two-phase fluid vapor quality, defined as the mass fraction of vapor in a
liquid-vapor mixture, at the two-phase fluid outlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Outlet condition
specification** to `Vapor quality`.

### **Two-phase fluid volume** — Total volume of two-phase fluid `0.001 m^3` (default) | positive scalar

Total volume of two-phase fluid inside the heat exchanger.

### **Initialize two-phase fluid to nominal operating conditions** — Option for initializing two-phase fluid `on` (default) | `off`

Option to initialize the two-phase fluid to nominal operating conditions or
specified values. If you select this parameter, the block initializes the two-phase
fluid to the nominal operating conditions. If you clear this check box, you can
specify the initial conditions directly with additional parameters.

### **Initial fluid energy specification** — Initial state of the two-phase fluid `Specific enthalpy` (default) | `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

Quantity used to describe the initial state of the fluid.

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

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid to
nominal operating conditions** check box.

### **Initial two-phase fluid pressure** — Fluid pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Two-phase fluid pressure at the start of the simulation.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid to
nominal operating conditions** check box.

### **Initial two-phase fluid specific enthalpy** — Enthalpy per unit mass at start of simulation `1500 kJ/kg` (default) | positive scalar | two-element vector

Two-phase fluid specific enthalpy at the start of simulation. If the value is a
scalar, then the initial specific enthalpy is assumed uniform. If the value is a
two-element vector, then the initial specific enthalpy is assumed to vary linearly
between ports **A1** and **B1**, with the first
element corresponding to port **A1** and the second element
corresponding to port **B1**.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Specific
enthalpy`.

### **Initial two-phase fluid temperature** — Temperature at start of simulation `293.15 K` (default) | positive scalar | two-element vector

Two-phase fluid temperature at the start of simulation. If the value is a scalar,
then the initial temperature is assumed uniform. If the value is a two-element vector,
then the initial temperature is assumed to vary linearly between ports
**A1** and **B1**, with the first element
corresponding to port **A1** and the second element corresponding to
port **B1**.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Temperature`.

### **Initial two-phase fluid vapor quality** — Vapor mass fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Two-phase fluid vapor quality, defined as the mass fraction of vapor in a
liquid-vapor mixture, at the start of simulation. If the value is a scalar, then the
initial vapor quality is assumed uniform. If the value is a two-element vector, then
the initial vapor quality is assumed to vary linearly between ports
**A1** and **B1**, with the first element
corresponding to port **A1** and the second element corresponding to
port **B1**.

If using this option, the initial pressure cannot be higher than the critical
pressure.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Vapor
quality`.

### **Initial two-phase fluid vapor void fraction** — Vapor volume fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Two-phase fluid vapor void fraction, defined as the volume fraction of vapor in a
liquid-vapor mixture,at the start of simulation. If the value is a scalar, then the
initial vapor void fraction is assumed uniform. If the value is a two-element vector,
then the initial vapor void fraction is assumed to vary linearly between ports
**A1** and **B1**, with the first element
corresponding to port **A1** and the second element corresponding to
port **B1**.

If using this option, the initial pressure cannot be higher than the critical
pressure.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Vapor void
fraction`.

### **Initial two-phase fluid specific internal energy** — Internal energy per unit mass at start of simulation `1500 kJ/kg` (default) | positive scalar | two-element vector

Two-phase fluid specific internal energy at the start of simulation. If the value
is a scalar, then the initial specific internal energy is assumed uniform. If the
value is a two-element vector, then the initial specific internal energy is assumed to
vary linearly between ports **A1** and **B1**, with
the first element corresponding to port **A1** and the second element
corresponding to port **B1**.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Specific internal
energy`.

### Moist Air 2

### **Nominal mass flow rate** — Mass flow rate between moist air ports during nominal operating condition `0.1 kg/s` (default) | positive scalar

Mass flow rate from port **A2** to port **B2**
during the nominal operating condition.

### **Nominal pressure drop** — Pressure drop between moist air ports during nominal operating condition `0.001 MPa` (default) | positive scalar

Pressure drop from port **A2** to port **B2**
during the nominal operating condition.

### **Nominal inlet pressure** — Pressure at the moist air side inlet `0.101325 MPa` (default) | positive scalar

Pressure at the moist air inlet of the heat exchanger during nominal operating
condition.

### **Nominal inlet temperature** — Temperature at the moist air side inlet `293.15 K` (default) | positive scalar

Temperature at the moist air inlet of the heat exchanger during the nominal
operating condition.

### **Inlet humidity specification** — Quantity used to describe the humidity level at the moist air side inlet `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Select quantity used to describe the humidity level at the inlet during the
nominal operating condition.

### **Nominal inlet relative humidity** — Relative humidity at the inlet `0.5` (default) | scalar in the range [0,1]

Relative humidity at the moist air inlet of the heat exchanger during the nominal
operating condition.

#### Dependencies

To enable this parameter, set **Inlet humidity specification**
to `Relative humidity`.

### **Nominal inlet specific humidity** — Specific humidity at the inlet `0.01` (default) | scalar in the range [0,1]

Specific humidity, defined as the mass fraction of water vapor in a moist air
mixture, at the moist air inlet of the heat exchanger during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **Inlet humidity specification**
to `Specific humidity`.

### **Nominal inlet water vapor mole fraction** — Mole fraction of water vapor at the inlet `0.01` (default) | scalar in the range [0,1]

Mole fraction of water vapor in a moist air mixture at the moist air inlet of the
heat exchanger during the nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet humidity specification**
to `Mole fraction`.

### **Nominal inlet humidity ratio** — Humidity ratio at the inlet `0.01` (default) | positive scalar in the range [0,1]

Humidity ratio, defined as the mass ratio of water vapor to dry air and trace gas,
at the moist air inlet of the heat exchanger during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **Inlet humidity specification**
to `Humidity ratio`.

### **Nominal inlet wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Wet-bulb temperature at the moist air inlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet humidity specification**
to `Wet-bulb temperature`.

### **Inlet trace gas specification** — Quantity used to describe trace gas level at the inlet `Mass fraction` (default) | `Mole fraction`

Select quantity used to describe the trace gas level at the inlet during the
nominal operating condition: mass fraction or mole fraction.

### **Nominal inlet trace gas mass fraction** — Mass fraction of trace gas at the inlet `0.001` (default) | scalar in the range [0,1]

Mass fraction of trace gas in a moist air mixture at the moist air inlet of the
heat exchanger during the nominal operating condition.

This parameter is ignored if the **Trace gas model** parameter in
the Moist Air Properties (MA) block is set to `None`.

#### Dependencies

To enable this parameter, set **Inlet trace gas specification**
to `Mass fraction`.

### **Nominal inlet trace gas mole fraction** — Mole fraction of trace gas at the inlet `0.001` (default) | scalar in the range [0,1]

Mole fraction of trace gas in a moist air mixture at the moist air inlet of the
heat exchanger during the nominal operating condition.

This parameter is ignored if the **Trace gas model** parameter in
the Moist Air Properties (MA) block is set to `None`.

#### Dependencies

To enable this parameter, set **Inlet trace gas specification**
to `Mole fraction`.

### **Moist air volume** — Total volume of moist air in the heat exchanger `0.1 m^3` (default) | positive scalar

Total volume of moist air in the heat exchanger.

### **Initialize moist air to nominal operating conditions** — Option for initializing moist air `on` (default) | `off`

Option to initialize the moist air to nominal operating conditions or specified
values. If you select this parameter, the block initializes the moist to the nominal
operating conditions. If you clear this check box, you can specify the initial
conditions directly with additional parameters.

### **Initial moist air pressure** — Moist air pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Moist air pressure at the start of the simulation.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box.

### **Initial moist air temperature** — Moist air temperature at start of simulation `293.15 K` (default) | positive scalar | two-element vector

Moist air temperature at the start of simulation. If the value is a scalar, then
the initial temperature is assumed uniform. If the value is a two-element vector, then
the initial temperature is assumed to vary linearly between ports
**A2** and **B2**, with the first element
corresponding to port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box.

### **Initial humidity specification** — Quantity used to describe the initial humidity level `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Select quantity used to describe the initial humidity level: relative humidity,
specific humidity, water vapor mole fraction, or humidity ratio.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box.

### **Initial moist air relative humidity** — Relative humidity at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Moist air relative humidity at the start of simulation. If the value is a scalar,
then the initial relative humidity is assumed uniform. If the value is a two-element
vector, then the initial relative humidity is assumed to vary linearly between ports
**A2** and **B2**, with the first element
corresponding to port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box and set **Initial humidity
specification** to `Relative humidity`.

### **Initial moist air specific humidity** — Specific humidity at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Moist air specific humidity, defined as the mass fraction of water vapor in a
moist air mixture, at start of simulation. If the value is a scalar, then the initial
specific humidity is assumed uniform. If the value is a two-element vector, then the
initial specific humidity is assumed to vary linearly between ports
**A2** and **B2**, with the first element
corresponding to port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box and set **Initial humidity
specification** to `Specific humidity`.

### **Initial moist air water vapor mole fraction** — Mole fraction of water vapor at start of simulation `0.01` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of water vapor in a moist air mixture at the start of simulation. If
the value is a scalar, then the initial mole fraction is assumed uniform. If the value
is a two-element vector, then the initial mole fraction is assumed to vary linearly
between ports **A2** and **B2**, with the first
element corresponding to port **A2** and the second element
corresponding to port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box and set **Initial humidity
specification** to `Mole fraction`.

### **Initial moist air humidity ratio** — Humidity ratio at start of simulation `0.01` (default) | positive scalar in the range [0,1] | two-element vector

Moist air humidity ratio, defined as the mass ratio of water vapor to dry air and
trace gas, at the start of simulation. If the value is a scalar, then the initial
humidity ratio is assumed uniform. If the value is a two-element vector, then the
initial humidity ratio is assumed to vary linearly between ports
**A2** and **B2**, with the first element
corresponding to port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box and set **Initial humidity
specification** to `Humidity ratio`.

### **Initial moist air wet-bulb temperature** — Wet-bulb temperature at the start of simulation `287 K` (default) | positive scalar in the range [0,1]

Wet-bulb temperature at the start of the simulation. The block uses this value to
calculate humidity.

This parameter can be a scalar or a two-element vector. A scalar value represents
the mean initial wet-bulb temperature in the channel. A vector value represents the
initial wet-bulb temperature at the inlet and outlet in the form
[`inlet`, `outlet`]. The block calculates a linear
gradient between the two ports. The inlet and the outlet ports are identified
according to the initial flow direction.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box and set **Initial humidity
specification** to `Wet-bulb
temperature`.

### **Initial trace gas specification** — Quantity used to describe initial trace gas level `Mass fraction` (default) | `Mole fraction`

Select quantity used to describe the trace gas level at the start of simulation:
mass fraction or mole fraction.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box.

### **Initial moist air trace gas mass fraction** — Mass fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mass fraction of trace gas in a moist air mixture at the start of simulation. If
the value is a scalar, then the initial mass fraction is assumed uniform. If the value
is a two-element vector, then the initial mass fraction is assumed to vary linearly
between ports **A2** and **B2**, with the first
element corresponding to port **A2** and the second element
corresponding to port **B2**.

This parameter is ignored if the **Trace gas model** parameter in
the Moist Air Properties (MA) block is set to `None`.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box and set **Initial trace gas
specification** to `Mass fraction`.

### **Initial moist air trace gas mole fraction** — Mole fraction of trace gas at start of simulation `0.001` (default) | scalar in the range [0,1] | two-element vector

Mole fraction of trace gas in a moist air mixture at the start of simulation. If
the value is a scalar, then the initial mole fraction is assumed uniform. If the value
is a two-element vector, then the initial mole fraction is assumed to vary linearly
between ports **A2** and **B2**, with the first
element corresponding to port **A2** and the second element
corresponding to port **B2**.

This parameter is ignored if the **Trace gas model** parameter in
the Moist Air Properties (MA) block is set to `None`.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box and set **Initial trace gas
specification** to `Mole fraction`.

### **Initial mass ratio of water droplets to moist air** — Ratio of water droplets to moist air `0` (default) | positive scalar

Initial mass ratio of water droplets to moist air.

#### Dependencies

To enable this parameter, clear the **Initialize moist air to nominal
operating conditions** check box.

### **Relative humidity at saturation** — Relative humidity point of condensation `1` (default) | nonnegative scalar

Relative humidity point of condensation. Condensation occurs above this value. In
most cases, this value is 1, that is, 100%. A value greater than 1 indicates a
supersaturated vapor.

### **Water vapor condensation time constant** — Time scale for condensation `1e-3 s` (default) | positive scalar

Characteristic time scale at which an oversaturated moist air volume returns to
saturation by condensing out excess humidity.

### **Water droplets evaporation time constant** — Time scale for evaporation `1e-3 s` (default) | positive scalar

Characteristic time scale at which water droplets evaporate to vapor.

### **Fraction of condensate entrained as water droplets** — Fraction of condensate in water droplets `1` (default) | scalar in the range [0,1]

Fraction of the condensate in the moist air that is entrained as water
droplets.

### Correlation Coefficients

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid liquid** — Correlation coefficient for subcooled liquid in two-phase fluid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for subcooled liquid in two-phase fluid. The
default value is based on the Colburn equation.

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid mixture** — Correlation coefficient for liquid-vapor mixture in two-phase fluid `0.005` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for liquid-vapor mixture in two-phase fluid.
The default value is based on the Cavallini and Zecchin correlation.

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid vapor** — Correlation coefficient for superheated vapor in two-phase fluid `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for superheated vapor in two-phase fluid. The
default value is based on the Colburn equation.

### **b in Nu = a\*Re^b\*Pr^c for two-phase fluid** — Reynolds number exponent in correlation for two-phase fluid `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for two-phase fluid. The same value applies to
subcooled liquid, liquid-vapor mixture, and superheated vapor.

### **c in Nu = a\*Re^b\*Pr^c for two-phase fluid** — Prandtl number exponent in correlation for two-phase fluid `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for two-phase fluid. The same value applies to
subcooled liquid, liquid-vapor mixture, and superheated vapor.

### **a in Nu = a\*Re^b\*Pr^c for moist air** — Correlation coefficient for moist air `0.005` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for moist air. The default value is based on
the Colburn equation.

### **b in Nu = a\*Re^b\*Pr^c for moist air** — Reynolds number exponent in correlation for moist air `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for moist air. The default value is based on
the Colburn equation.

### **c in Nu = a\*Re^b\*Pr^c for moist air** — Prandtl number exponent in correlation for moist air `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for moist air. The default value is based on
the Colburn equation.
## Libraries

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Moist Air

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the
moist air domain can now model water droplets suspended in a moist air flow. To model water
droplets, select **Enable entrained water droplets** in the Moist Air Properties
(MA) block connected to your moist air network.

### R2024a: New moisture specification options

The block has new options for the **Inlet humidity specification** and
**Initial humidity specification** parameters. This option, called
`Wet-bulb temperature`, allows you to input data in the form of a
wet-bulb temperature.

### R2023b: Specify initial wall temperature

If you select **Enable wall thermal mass** and clear the
**Initialize wall temperature to nominal operating conditions** check
box, you can use the new **Initial wall temperature** parameter to specify
the initial conditions directly.

## Description

Heat exchanger based on performance data between two-phase fluid and moist air networks

The System-Level Condenser Evaporator (2P-MA) block models
a heat exchanger between a two-phase fluid network and a moist air network.

The block can act as a condenser or as an evaporator in a refrigeration system, depending
on the direction of heat transfer. The block uses performance data from the heat exchanger
datasheet, rather than the detailed geometry of the exchanger. You can adjust the size and
performance of the heat exchanger during design iterations, or model heat exchangers with
uncommon geometries. You can also use this block to model heat exchangers with a certain level
of performance at an early design stage, when detailed geometry data is not yet
available.

You parameterize the block by the nominal operating condition. The heat exchanger is sized
to match the specified performance at the nominal operating condition at steady state.

The Two-Phase Fluid 1 side approximates the liquid zone, mixture zone, and vapor zone
based on the change in enthalpy along the flow path. The Moist Air 2 side models water vapor
condensation based on convective water vapor mass transfer with the heat transfer surface.
Condensed water is removed from the moist air flow.

This block is similar to the Condenser Evaporator (2P-MA)
block, but uses a different parameterization model. The table compares the two blocks:

| Condenser Evaporator (2P-MA) | System-Level Condenser Evaporator (2P-MA) |
| --- | --- |
| Block parameters are based on the heat exchanger geometry | Block parameters are based on performance and operating conditions |
| Heat exchanger geometry may be limited by the available geometry parameter options | Model is independent of the specific heat exchanger geometry |
| You can adjust the block for different performance requirements by tuning geometry parameters, such as fin sizes and tube lengths | You can adjust the block for different performance requirements by directly specifying the desired heat and mass flow rates |
| You can select between parallel, counter, or cross flow configurations | You can select between parallel, counter, or cross-flow arrangement at nominal operating conditions to help with sizing |
| Predictively accurate results over a wide range of operating conditions, subject to the applicability of the E-NTU equations and the heat transfer coefficient correlations | Very accurate results around the specified operating condition; accuracy may decrease far away from the specified operating conditions |
| Heat transfer calculations account for the variation of temperature along the flow path by using the E-NTU model | Heat transfer calculations approximate the variation of temperature along the flow path by dividing it into three segments |
| Accounts for different fluid properties and heat transfer coefficients for subcooled liquid, liquid-vapor mixture, and superheated vapor | Accounts for different fluid properties and heat transfer coefficients for subcooled liquid, liquid-vapor mixture, and superheated vapor |
| Keeps track of variable zone length fractions for subcooled liquid, liquid-vapor mixture, and superheated vapor regions based on the geometry | Approximates the effect of subcooled liquid, liquid-vapor mixture, and superheated vapor regions using weighting factors based on the difference in enthalpy between inlet and outlet |
| Accounts for water vapor condensation and the latent heat on the moist air flow | Accounts for water vapor condensation and the latent heat on the moist air flow |

### Heat Transfer

The block divides the two-phase fluid flow and the moist air flow each into three
segments of equal size and calculates heat transfer between the fluids is in each segment.
For simplicity, the equation in this section are for one segment.

If you clear the **Enable wall thermal mass** check box, then the heat
balance in the heat exchanger is

Qseg,2P+Qseg,MA=0,

where:

- *Q*seg,2P is the heat flow rate from the
  wall that is the heat transfer surface to the two-phase fluid in the segment.
- *Q*seg,MA is the heat flow rate from the
  wall to the moist air in the segment.

If you select **Enable wall thermal mass**, then the heat balance in
the heat exchanger is

Qseg,2P+Qseg,MA=−MwallcpwallNdTseg,walldt,

where:

- *M*wall is the mass of the wall.
- *c*pwall is the
  specific heat of the wall.
- *N* = 3 is the number of segments.
- *T*seg,wall is the average wall temperature
  in the segment.
- *t* is time.

The heat flow rate from the wall to the two-phase fluid in the segment is

Qseg,2P=UAseg,2P(Tseg,wall−Tseg,2P),

where:

- *UA*seg,2P is the weighted-average heat
  transfer conductance for the two-phase fluid in the segment.
- *T*seg,2P is the weighted-average fluid
  temperature for the two-phase fluid in the segment.

The heat flow rate from the wall to the moist air in the segment is

Qseg,MA=UAseg,MAc¯pseg,MA(h¯seg,wall−h¯seg,MA)+m˙w,seg,condhl,wall,

where:

- *UA*seg,MA is the heat transfer conductance
  for the moist air in the segment.
- c¯pseg,MA is the moist air mixture specific heat per unit mass of dry air and
  trace gas in the segment.
- h¯seg,wall is the moist air mixture enthalpy per unit mass of dry air and trace
  gas at the average wall segment temperature.
- h¯seg,MA is the moist air mixture enthalpy per unit mass of dry air and trace
  gas in the segment.
- m˙w,seg,cond is the rate of water vapor condensation on the wall surface.
- *h*l,wall is the specific enthalpy of liquid
  water at the average wall segment temperature.

Using mixture enthalpy in this equation accounts for both differences in temperature and
differences in humidity due to condensation [3].

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

**Note**

For the moist air quantities, the bar above the symbols indicates that they are
quantities for mixture divided by the mass of dry air and trace gas only, as opposed to
dividing by the mass of the whole mixture. The whole mixture includes dry air, water
vapor, and trace gas.

### Two-Phase Fluid Heat Transfer Correlation

If the segment is subcooled liquid, then the heat transfer conductance is

UAseg,L,2P=aL,2P(Reseg,L,2P)b2P(Prseg,L,2P)c2Pkseg,L,2PG2PN,

where:

- *a*L,2P,
  *b*2P, and
  *c*2P are the coefficients of the Nusselt
  number correlation. These coefficients are block parameters in the **Correlation
  Coefficients** section.
- *Re*seg,L,2P is the average liquid Reynolds
  number for the segment.
- *Pr*seg,L,2P is the average liquid Prandtl
  number for the segment.
- *k*seg,L,2P is the average liquid thermal
  conductivity for the segment.
- *G*2P is the geometry scale factor for the
  two-phase fluid side of the heat exchanger. The block calculates the geometry scale
  factor so that the total heat transfer over all segments matches the specified
  performance at the nominal operating conditions.

The average liquid Reynolds number is

Reseg,L,2P=m˙seg,2PDref,2Pμseg,L,2PSref,2P,

where:

- m˙seg,2P is the mass flow rate through the segment.
- *μ*seg,L,2P is the average liquid dynamic
  viscosity for the segment.
- *D*ref,2P is an arbitrary reference
  diameter.
- *S*ref,2P is an arbitrary reference flow
  area.

**Note**

The *D*ref,2P and
*S*ref,2P terms are included in this equation
for unit calculation purposes only, to make
*Re*seg,L,2P nondimensional. The values of
*D*ref,2P and
*S*ref,2P are arbitrary because the
*G*2P calculation overrides these values.

Similarly, if the segment is superheated vapor, then the heat transfer conductance
is

UAseg,V,2P=aV,2P(Reseg,V,2P)b2P(Prseg,V,2P)c2Pkseg,V,2PG2PN,

where:

- *a*V,2P,
  *b*2P, and
  *c*2P are the coefficients of the Nusselt
  number correlation. These coefficients appear as block parameters in the
  **Correlation Coefficients** section.
- *Re*seg,V,2P is the average vapor Reynolds
  number for the segment.
- *Pr*seg,V,2P is the average vapor Prandtl
  number for the segment.
- *k*seg,V,2P is the average vapor thermal
  conductivity for the segment.

The average vapor Reynolds number is

Reseg,V,2P=m˙seg,2PDref,2Pμseg,V,2PSref,2P,

where *μ*seg,V,2P is the average vapor dynamic
viscosity for the segment.

If the segment is liquid-vapor mixture, then the heat transfer conductance is

UAseg,M,2P=aM,2P(Reseg,SL,2P)b2PCZ(Prseg,SL,2P)c2Pkseg,SL,2PG2PN,

where:

- *a*M,2P,
  *b*2P, and
  *c*2P are the coefficients of the Nusselt
  number correlation. These coefficients appear as block parameters in the
  **Correlation Coefficients** section.
- *Re*seg,SL,2P is the saturated liquid
  Reynolds number for the segment.
- *Pr*seg,SL,2P is the saturated liquid
  Prandtl number for the segment.
- *k*seg,SL,2P is the saturated liquid thermal
  conductivity for the segment.
- *CZ* is the Cavallini and Zecchin term.

The saturated liquid Reynolds number is

Reseg,SL,2P=m˙seg,2PDref,2Pμseg,SL,2PSref,2P,

where *μ*seg,SL,2P is the saturated liquid
dynamic viscosity for the segment.

The Cavallini and Zecchin term is

CZ=((νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P+1))1+b2P−((νseg,SV,2Pνseg,SL,2P−1)(xseg,in,2P+1))1+b2P(1+b2P)(νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P−xseg,in,2P),

where:

- *ν*seg,SL,2P is the saturated liquid
  specific volume for the segment.
- *ν*seg,SV,2P is the saturated vapor specific
  volume for the segment.
- *x*seg,in,2P is the vapor quality at the
  segment inlet.
- *x*seg,out,2P is the vapor quality at the
  segment outlet.

The expression is based on the work of Cavallini and Zecchin [5], which
derives a heat transfer coefficient correlation at a local vapor quality
*x*. Equations for the liquid-vapor mixture are obtained by averaging
Cavallini and Zecchin’s correlation over the segment from
*x*seg,in,2P to
*x*seg,out,2P.

### Two-Phase Fluid Weighted Average

The two-phase fluid flow through a segment may not be entirely represented as either
subcooled liquid, superheated vapor, or liquid-vapor mixture. Instead, each segment may
consist of a combination of these. The block approximates this condition by computing
weighting factors (*w*L,
*w*V, and
*w*M) based on the change in specific enthalpy
across the segment and the saturated liquid and vapor specific enthalpies. The block assumes
that the specific enthalpy across the segment varies piecewise linearly from inlet to
outlet, with the breakpoints corresponding to the saturation boundaries for liquid and
vapor. The zone with a larger heat transfer coefficient has a steeper slope than the zone
with a lower heat transfer coefficient.

wL=ΔLΔL+ΔM+ΔVwV=ΔVΔL+ΔM+ΔVwM=1−wL−wV

ΔL=|min(hseg,out,2P,hseg,SL,2P)−min(hseg,in,2P,hseg,SL,2P)|⋅UAseg,M,2P⋅UAseg,V,2PΔM=|min(max(hseg,out,2P,hseg,SL,2P),hseg,SV,2P)−min(max(hseg,in,2P,hseg,SL,2P),hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,V,2PΔV=|max(hseg,out,2P,hseg,SV,2P)−max(hseg,in,2P,hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,M,2P

where:

- *h*seg,in,2P is the specific enthalpy at the
  segment inlet.
- *h*seg,out,2P is the specific enthalpy at
  the segment outlet.
- *h*seg,SL,2P is the saturated liquid
  specific enthalpy for the segment.
- *h*seg,SV,2P is the saturated vapor specific
  enthalpy for the segment.

The weighted-average two-phase fluid heat transfer conductance for the segment is
therefore

UAseg,2P=wL(UAseg,L,2P)+wV(UAseg,V,2P)+wM(UAseg,M,2P).

The weighted-average fluid temperature for the segment is

Tseg,2P=wL(UAseg,L,2P)Tseg,L,2P+wV(UAseg,V,2P)Tseg,V,2P+wM(UAseg,M,2P)Tseg,M,2PUAseg,2P,

where:

- *T*seg,L,2P is the average liquid
  temperature for the segment.
- *T*seg,V,2P is the average vapor temperature
  for the segment.
- *T*seg,M,2P is the average mixture
  temperature for the segment, which is the saturated liquid temperature.

### Moist Air Heat Transfer Correlation

The heat transfer conductance is

UAseg,MA=aMA(Reseg,MA)bMA(Prseg,MA)cMAkseg,MAGMAN,

where:

- *a*MA,
  *b*MA, and
  *c*MA are the coefficients of the Nusselt
  number correlation. These coefficients are block parameters in the **Correlation
  Coefficients** section.
- *Re*seg,MA is the average Reynolds number
  for the segment.
- *Pr*seg,MA is the average Prandtl number for
  the segment.
- *k*seg,MA is the average thermal
  conductivity for the segment.
- *G*MA is the geometry scale factor for the
  moist air side of the heat exchanger. The block calculates the geometry scale factor so
  that the total heat transfer over all segments matches the specified performance at the
  nominal operating conditions.

The average Reynolds number is

Reseg,MA=m˙seg,MADref,MAμseg,MASref,MA,

where:

- m˙seg,MA is the mass flow rate through the segment.
- *μ*seg,MA is the average dynamic viscosity
  for the segment.
- *D*ref,MA is an arbitrary reference
  diameter.
- *S*ref,MA is an arbitrary reference flow
  area.

**Note**

The *D*ref,MA and
*S*ref,MA terms are included in this equation
for unit calculation purposes only, to make
*Re*seg,MA nondimensional. The values of
*D*ref,MA and
*S*ref,MA are arbitrary because the
*G*MA calculation overrides these values.

### Moist Air Condensation

The equation describing the heat flow rate from the wall to the moist air in the segment
(the last equation in the Heat Transfer section) uses the average
moist air mixture enthalpy, h¯seg,MA, and the wall segment moist air mixture enthalpy, h¯seg,wall.

The average moist air mixture enthalpy is based on the temperature and humidity of the
moist air flow through the segment:

h¯seg,MA=hseg,ag,MA+Wseg,MAhseg,w,MA,

where:

- *h*seg,ag,MA is the average specific
  enthalpy of dry air and trace gas for the segment.
- *h*seg,w,MA is the average specific enthalpy
  of water vapor for the segment.
- *W*seg,MA is the humidity ratio of the
  segment.

The wall segment moist air mixture enthalpy is based on the temperature and humidity at
the wall segment:

h¯seg,wall=hseg,ag,wall+Wseg,wallhseg,w,wall,

where:

- *h*seg,ag,wall is the specific enthalpy of
  dry air and trace gas at the wall segment temperature.
- *h*seg,w,wall is the specific enthalpy of
  water vapor at the wall segment temperature.
- *W*seg,wall is the humidity ratio at the
  wall segment:

  Wseg,wall=min(Wseg,MA,Wseg,s,wall),

  where *W*seg,s,wall is the saturated
  humidity ratio at the wall segment temperature. In other words, the humidity ratio at
  the wall is the same as the humidity ratio of the moist air flow but not more than the
  maximum that can be supported at the wall segment temperature.

When *W*seg,s,wall <
*W*seg,MA, water vapor condensation occurs on the
wall surface. The rate of water vapor condensation is

m˙w,seg,cond=UAseg,MAc¯pseg,MA(Wseg,MA−Wseg,wall).

The block assumes that the condensed water is drained from the wall surface and is thus
removed from the moist air flow downstream.

### Pressure Loss

The pressure losses on the two-phase fluid side are

pA,2P−p2P=K2P2m˙A,2Pm˙2A,2P+m˙2thres,2P2ρavg,2PpB,2P−p2P=K2P2m˙B,2Pm˙2B,2P+m˙2thres,2P2ρavg,2P

where:

- *p*A,2P and
  *p*B,2P are the pressures at ports
  **A1** and **B1**, respectively.
- *p*2P is internal two-phase fluid pressure
  at which the heat transfer is calculated.
- m˙A,2P and m˙B,2P are the mass flow rates into ports **A1** and
  **B1**, respectively.
- *ρ*avg,2P is the average two-phase fluid
  density over all segments.
- m˙thres,2P is the laminar threshold for pressure loss, approximated as 1e-4 of
  the nominal mass flow rate. The block calculates the pressure loss coefficient,
  *K*2P, so that
  *p*A,2P –
  *p*B,2P matches the nominal pressure loss at
  the nominal mass flow rate.

The pressure losses on the moist air side are

pA,MA−pMA=KMA2m˙A,MAm˙2A,MA+m˙2thres,MA2ρavg,2PpB,MA−pMA=KMA2m˙B,MAm˙2B,MA+m˙2thres,MA2ρavg,MA

where:

- *p*A,MA and
  *p*B,MA are the pressures at ports
  **A2** and **B2**, respectively.
- *p*MA is internal moist air pressure at
  which the heat transfer is calculated.
- m˙A,MA and m˙B,MA are the mass flow rates into ports **A2** and
  **B2**, respectively.
- *ρ*avg,MA is the average moist air density
  over all segments.
- m˙thres,MA is the laminar threshold for pressure loss, approximated as 1e-4 of
  the nominal mass flow rate. The block calculates the pressure loss coefficient,
  *K*MA, so that
  *p*A,MA –
  *p*B,MA matches the nominal pressure loss at
  the nominal mass flow rate.

### Two-Phase Fluid Mass and Energy Conservation

The mass conservation equation for the overall two-phase fluid flow is

(dp2Pdt∑segments(∂ρseg,2P∂p)+∑segments(duseg,2Pdt∂ρseg,2P∂u))V2PN=m˙A,2P+m˙B,2P,

where:

- ∂ρseg,2P∂p is the partial derivative of density with respect to pressure for the
  segment.
- ∂ρseg,2P∂u is the partial derivative of density with respect to specific internal
  energy for the segment.
- *u*seg,2P is the specific internal energy
  for the segment.
- *V*2P is the total two-phase fluid
  volume.

The summation is over all segments.

**Note**

Although the block divides the two-phase fluid flow into *N*=3
segments for heat transfer calculations, it assumes all segments are at the same internal
pressure, *p*2P. Consequentially,
*p*2P is outside of the summation.

The energy conservation equation for each segment is

duseg,2PdtM2PN+useg,2P(m˙seg,in,2P−m˙seg,out,2P)=Φseg,in,2P−Φseg,out,2P+Qseg,2P,

where:

- *M*2P is the total two-phase fluid
  mass.
- m˙seg,in,2P and m˙seg,out,2P are the mass flow rates into and out of the segment.
- *Φ*seg,in,2p and
  *Φ*seg,out,2p are the energy flow rates into
  and out of the segment.

The block assumes the mass flow rates between segments are linearly distributed between
the values of m˙A,2P and m˙B,2P.

### Moist Air Mass and Energy Conservation

The mass conservation for the overall moist air mixture flow is

(dpMAdt∑segments(∂ρseg,MA∂p)+∑segments(dTseg,MAdt∂ρseg,MA∂T+dxw,seg,MAdt∂ρseg,MA∂xw+dxg,seg,MAdt∂ρseg,MA∂xg))VMAN=m˙A,MA+m˙B,MA−∑segments(m˙w,seg,cond+m˙w,seg,conv)+∑segmentsm˙d,seg,evap,

where:

- ∂ρseg,MA∂p is the partial derivative of density with respect to pressure for the
  segment.
- ∂ρseg,MA∂T is the partial derivative of density with respect to temperature for
  the segment.
- ∂ρseg,MA∂xw is the partial derivative of density with respect to specific humidity
  for the segment.
- ∂ρseg,MA∂xg is the partial derivative of density with respect to trace gas mass
  fraction for the segment.
- *x*w,seg,MA is the *specific
  humidity*, also referred to as the water vapor mass fraction, for the
  segment.
- *x*g,seg,MA is the trace gas mass fraction
  for the segment.
- *V*MA is the total moist air volume.
- m˙w,seg,conv is the rate of condensation on the
  wall surface for the segment.
- m˙d,seg,evap is the rate of water droplet
  evaporation for the segment.

The summation is over all segments.

**Note**

Although the block divides the moist air flow into *N*=3 segments for
heat transfer calculations, it assumes all segments are at the same internal pressure,
*p*MA. Consequentially,
*p*MA is outside of the summation.

The energy conservation equation for each segment is

dTseg,MAdt(c¯seg,MA−Rseg)MMAN+ua,seg,MA(m˙seg,in,MA−m˙seg,out,MA)+(uw,seg,MA−ua,seg,MA)(m˙w,seg,in,MA−m˙w,seg,out,MA)+(ug,seg,MA−ua,seg,MA)(m˙g,seg,in,MA−m˙g,seg,out,MA)+hd(m˙d,seg,in,MA−m˙d,seg,out,MA)=Φseg,in,MA−Φseg,out,MA+Qseg,MA−(1−λd)(m˙w,seg,condhd+m˙w,seg,convhl,wall),

where:

- *ua,seg,MA* is the dry air specific internal
  energy for the segment.
- *ug,seg,MA* is the trace gas specific
  internal energy for the segment.
- *uw,seg,MA* is the water vapor specific
  internal energy for the segment.
- *MMA* is the total moist air mass.
- m˙seg,in,MA and m˙seg,out,MA are the moist air mass flow rates into and out of the segment.
- m˙w,seg,in,MA and m˙w,seg,out,MA are the water vapor mass flow rates into and out of the
  segment.
- m˙g,seg,in,MA and m˙g,seg,out,MA are the trace gas mass flow rates into and out of the segment.
- m˙d,seg,in,MA and m˙d,seg,out,MA are the water droplets mass flow rate into and out of the
  segment.
- *Rseg* is the segment volume specific gas
  constant.
- *Φ*seg,in,MA and
  *Φ*seg,out,MA are the energy flow rates into
  and out of the segment.
- *hd* is the water droplet specific enthalpy
  in the segment.
- *λd* is the value of the **Fraction
  of condensate entrained as water droplets** parameter.

The block assumes the mass flow rates between segments are linearly distributed between
the values of m˙A,MA and m˙B,MA.

The water vapor mass conservation equation for each segment is

dxw,seg,MAdtMMAN+xw,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙w,seg,in,MA−m˙w,seg,out,MA−m˙w,seg,cond−m˙w,seg,conv+m˙d,seg,evap.

The trace gas mass conservation equation for each segment is

dxg,seg,MAdtMMAN+xg,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙g,seg,in,MA−m˙g,seg,out,MA.

The water droplet mass balance conservation equation for each segment is

drd,segdtMMAN+rd,seg(m˙seg,in,MA−m˙seg,out,MA)=m˙d,seg,in−m˙d,seg,out+λd(m˙w,seg,cond+m˙w,seg,conv)−m˙d,seg,evap,

where *rd,seg* is the mass ratio
of the water droplets to the moist air in the fluid volume in the segment.

**Note**

If the **Trace gas model** parameter is
`None` in the Moist Air Properties
(MA) block, the moist air network does not model trace gas. In this
case, in the System-Level Condenser Evaporator (2P-MA) block, the conservation equation for trace gas is set to
0.

If you clear the **Enable entrained water droplets** in the
 Moist Air Properties (MA) block, the moist air network
does not model entrained water droplets. In this case, in the System-Level Condenser Evaporator (2P-MA) block, the
conservation equation for water droplets is set to 0.

### Assumptions and Limitations

- When determining the heat exchanger size, the block ignores the value of the **Fraction of condensate entrained as water droplets** parameter and assumes that the condensate is not entrained as droplets.
