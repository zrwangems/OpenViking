---
type: simulink-block
title: 'System-Level Heat Exchanger (2P-2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid'
documentation_page: 'systemlevelheatexchanger2p2p'
documentation_source_path: 'ref/systemlevelheatexchanger2p2p.html'
language: en
---

# System-Level Heat Exchanger (2P-2P)

## Ports
```yaml
ports:
- name: Q1
  summary: Rate of heat transfer to two-phase fluid 1, W physical signal
  direction: output
- name: Q2
  summary: Rate of heat transfer to two-phase fluid 2, W physical signal
  direction: output
- name: A1
  summary: Two-phase fluid port on side 1 two-phase fluid
  direction: conserving
- name: B1
  summary: Two-phase fluid port on side 1 two-phase fluid
  direction: conserving
- name: A2
  summary: Two-phase fluid port on side 2 two-phase fluid
  direction: conserving
- name: B2
  summary: Two-phase fluid port on side 2 two-phase fluid
  direction: conserving
```

### Output

### **Q1** — Rate of heat transfer to two-phase fluid 1, W physical signal

Rate of heat transfer to the first two-phase fluid network, returned as a physical
signal, in W. The physical signals at ports **Q1** and
**Q2** are usually equal in value with opposite sign. However, if
you select **Enable wall thermal mass**, then these two signals may
have different values because the wall may absorb and release some of the heat being
transferred.

### **Q2** — Rate of heat transfer to two-phase fluid 2, W physical signal

Rate of heat transfer to the second two-phase fluid network, returned as a
physical signal, in W. The physical signals at ports **Q1** and
**Q2** are usually equal in value with opposite sign. However, if
you select **Enable wall thermal mass**, then these two signals may
have different values because the wall may absorb and release some of the heat being
transferred.
### Conserving

### **A1** — Two-phase fluid port on side 1 two-phase fluid

Inlet or outlet port associated with the first two-phase fluid network.

### **B1** — Two-phase fluid port on side 1 two-phase fluid

Inlet or outlet port associated with the first two-phase fluid network.

### **A2** — Two-phase fluid port on side 2 two-phase fluid

Inlet or outlet port associated with the second two-phase fluid network.

### **B2** — Two-phase fluid port on side 2 two-phase fluid

Inlet or outlet port associated with the second two-phase fluid network.
## Parameters
```yaml
parameters:
- name: Flow arrangement at nominal operating conditions
  summary: Flow path alignment Counter flow - Two-Phase Fluid 1 flows from A to B, Two-Phase Fluid 2 flows from B to A (default)
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
  summary: Nominal operating condition Heat transfer from Two-Phase Fluid 1 to Two-Phase Fluid 2 (default) | Heat transfer
    from Two-Phase Fluid 2 to Two-Phase Fluid 1
  group: Two-Phase Fluid 1
- name: Nominal mass flow rate
  summary: Mass flow rate between two-phase fluid 1 ports during nominal operating condition 0.001 kg/s (default) | positive
    scalar
  group: Two-Phase Fluid 1
- name: Nominal pressure drop
  summary: Pressure drop between two-phase fluid 1 ports during nominal operating condition 0.01 MPa (default) | positive
    scalar
  group: Two-Phase Fluid 1
- name: Pressure specification
  summary: Select method of pressure specification Inlet pressure (default) | Saturation pressure at specified condensing
    temperature | Saturation pressure at specified evaporating temperature
  group: Two-Phase Fluid 1
- name: Nominal inlet pressure
  summary: Pressure at the two-phase fluid 1 inlet 1 MPa (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal saturation temperature
  summary: Use nominal saturation temperature to specify pressure 313.15 K (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Inlet condition specification
  summary: Select quantity to describe the inlet condition of the two-phase fluid 1 Specific enthalpy (default) | Temperature
    | Vapor quality
  group: Two-Phase Fluid 1
- name: Nominal inlet specific enthalpy
  summary: Specific enthalpy at the two-phase fluid 1 inlet 440 kJ/kg (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal inlet temperature
  summary: Temperature at the two-phase fluid 1 inlet 313.15 K (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal inlet vapor quality
  summary: Vapor quality at the two-phase fluid 1 inlet 1 (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Heat transfer capacity specification
  summary: How to specify heat transfer capacity of two-phase fluid 1 Rate of heat transfer (default) | Outlet condition
  group: Two-Phase Fluid 1
- name: Nominal rate of heat transfer
  summary: Rate of heat transfer 0.1 kW (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Outlet condition specification
  summary: Select quantity for outlet condition specification Specific enthalpy (default) | Subcooling | Superheating | Vapor
    quality
  group: Two-Phase Fluid 1
- name: Nominal outlet specific enthalpy
  summary: Specific enthalpy at the two-phase fluid 1 outlet 250 kJ/kg (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 1
- name: Nominal subcooling
  summary: Degree of temperature below the liquid saturation temperature at the two-phase fluid 1 outlet 5 deltaK (default)
    | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal superheating
  summary: Degree of temperature above the vapor saturation temperature at the two-phase fluid 1 outlet 5 deltaK (default)
    | positive scalar
  group: Two-Phase Fluid 1
- name: Nominal outlet vapor quality
  summary: Vapor mass fraction at the two-phase fluid 1 outlet 0 (default) | scalar in the range [0,1]
  group: Two-Phase Fluid 1
- name: Two-phase fluid 1 volume
  summary: Total volume of two-phase fluid 1 0.001 m^3 (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Initialize two-phase fluid 1 to nominal operating conditions
  summary: Option for initializing two-phase fluid 1 on (default) | off
  group: Two-Phase Fluid 1
- name: Initial fluid energy specification
  summary: Initial state of the two-phase fluid 1 Specific enthalpy (default) | Temperature | Vapor quality | Vapor void fraction
    | Specific internal energy
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid 1 pressure
  summary: Fluid 1 pressure at start of simulation 0.101325 MPa (default) | positive scalar
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid 1 specific enthalpy
  summary: Enthalpy per unit mass at start of simulation 1500 kJ/kg (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid 1 temperature
  summary: Temperature at start of simulation 293.15 K (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid 1 vapor quality
  summary: Vapor mass fraction at start of simulation 0.5 (default) | scalar in the range [0,1] | two-element vector
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid 1 vapor void fraction
  summary: Vapor volume fraction at start of simulation 0.5 (default) | scalar in the range [0,1] | two-element vector
  group: Two-Phase Fluid 1
- name: Initial two-phase fluid 1 specific internal energy
  summary: Internal energy per unit mass at start of simulation 1500 kJ/kg (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 1
- name: Nominal mass flow rate
  summary: Mass flow rate between two-phase fluid 2 ports during nominal operating condition 0.001 kg/s (default) | positive
    scalar
  group: Two-Phase Fluid 2
- name: Nominal pressure drop
  summary: Pressure drop between two-phase fluid 2 ports during nominal operating condition 0.01 MPa (default) | positive
    scalar
  group: Two-Phase Fluid 2
- name: Pressure specification
  summary: Select method of pressure specification Inlet pressure (default) | Saturation pressure at specified condensing
    temperature | Saturation pressure at specified evaporating temperature
  group: Two-Phase Fluid 2
- name: Nominal inlet pressure
  summary: Pressure at the two-phase fluid side inlet 1 MPa (default) | positive scalar
  group: Two-Phase Fluid 2
- name: Nominal saturation temperature
  summary: Use nominal saturation temperature to specify pressure 243.15 K (default) | positive scalar
  group: Two-Phase Fluid 2
- name: Inlet condition specification
  summary: Select quantity to describe inlet condition of the two-phase fluid 2 Specific enthalpy (default) | Temperature
    | Vapor quality
  group: Two-Phase Fluid 2
- name: Nominal inlet specific enthalpy
  summary: Specific enthalpy at the two-phase fluid 2 inlet 250 kJ/kg (default) | positive scalar
  group: Two-Phase Fluid 2
- name: Nominal inlet temperature
  summary: Temperature at the two-phase fluid 2 inlet 237.15 K (default) | positive scalar
  group: Two-Phase Fluid 2
- name: Nominal inlet vapor quality
  summary: Vapor quality at the two-phase fluid 2 inlet 0.1 (default) | positive scalar
  group: Two-Phase Fluid 2
- name: Two-phase fluid 2 volume
  summary: Total volume of two-phase fluid 2 0.001 m^3 (default) | positive scalar
  group: Two-Phase Fluid 2
- name: Initialize two-phase fluid 2 to nominal operating conditions
  summary: Option for initializing two-phase fluid 2 on (default) | off
  group: Two-Phase Fluid 2
- name: Initial fluid energy specification
  summary: Initial state of the two-phase fluid 2 Specific enthalpy (default) | Temperature | Vapor quality | Vapor void fraction
    | Specific internal energy
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 pressure
  summary: Fluid 2 pressure at start of simulation 0.101325 MPa (default) | positive scalar
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 specific enthalpy
  summary: Enthalpy per unit mass at start of simulation 1500 kJ/kg (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 temperature
  summary: Temperature at start of simulation 293.15 K (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 vapor quality
  summary: Vapor mass fraction at start of simulation 0.5 (default) | scalar in the range [0,1] | two-element vector
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 vapor void fraction
  summary: Vapor volume fraction at start of simulation 0.5 (default) | scalar in the range [0,1] | two-element vector
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 specific internal energy
  summary: Internal energy per unit mass at start of simulation 1500 kJ/kg (default) | positive scalar | two-element vector
  group: Two-Phase Fluid 2
- name: a in Nu = a\*Re^b\*Pr^c for two-phase fluid 1 liquid
  summary: Correlation coefficient for subcooled liquid in two-phase fluid 1 0.023 (default) | positive scalar
  group: Correlation Coefficients
- name: a in Nu = a\*Re^b\*Pr^c for two-phase fluid 1 mixture
  summary: Correlation coefficient for liquid-vapor mixture in two-phase fluid 1 0.005 (default) | positive scalar
  group: Correlation Coefficients
- name: a in Nu = a\*Re^b\*Pr^c for two-phase fluid 1 vapor
  summary: Correlation coefficient for superheated vapor in two-phase fluid 1 0.023 (default) | positive scalar
  group: Correlation Coefficients
- name: b in Nu = a\*Re^b\*Pr^c for two-phase fluid 1
  summary: Reynolds number exponent in correlation for two-phase fluid 1 0.8 (default) | positive scalar
  group: Correlation Coefficients
- name: c in Nu = a\*Re^b\*Pr^c for two-phase fluid 1
  summary: Prandtl number exponent in correlation for two-phase fluid 1 0.33 (default) | positive scalar
  group: Correlation Coefficients
- name: a in Nu = a\*Re^b\*Pr^c for two-phase fluid 2 liquid
  summary: Correlation coefficient for subcooled liquid in two-phase fluid 2 0.023 (default) | positive scalar
  group: Correlation Coefficients
- name: a in Nu = a\*Re^b\*Pr^c for two-phase fluid 2 mixture
  summary: Correlation coefficient for liquid-vapor mixture in two-phase fluid 2 0.005 (default) | positive scalar
  group: Correlation Coefficients
- name: a in Nu = a\*Re^b\*Pr^c for two-phase fluid 2 vapor
  summary: Correlation coefficient for superheated vapor in two-phase fluid 2 0.023 (default) | positive scalar
  group: Correlation Coefficients
- name: b in Nu = a\*Re^b\*Pr^c for two-phase fluid 2
  summary: Reynolds number exponent in correlation for two-phase fluid 2 0.8 (default) | positive scalar
  group: Correlation Coefficients
- name: c in Nu = a\*Re^b\*Pr^c for two-phase fluid 2
  summary: Prandtl number exponent in correlation for two-phase fluid 2 0.33 (default) | positive scalar
  group: Correlation Coefficients
```

### Configuration

### **Flow arrangement at nominal operating conditions** — Flow path alignment `Counter flow - Two-Phase Fluid 1 flows from A to B, Two-Phase Fluid 2 flows from B to A` (default) | `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

Flow path alignment between the heat exchanger sides at nominal operating
condition. The available flow arrangements are:

- `Counter flow - Two-Phase Fluid 1 flows from A to B, Two-Phase
  Fluid 2 flows from B to A` — The flows run parallel to each
  other, in the opposite directions.
- `Parallel flow - Both fluids flow from A to B` —
  The flows run in the same direction.
- `Cross flow - Both fluids flow from A to B` — The
  flows run perpendicular to each other.

The choice between parallel flow and counter flow affects how the block determines
the size of the heat exchanger. The counter flow setting is the most effective, and
needs the smallest size to meet the specified performance. Conversely, parallel flow
is the least effective, and needs the biggest size to meet the specified performance.

Flow direction at the nominal condition (from A to B, or from B to A) only affects
the model initialization, when you select **Initialize two-phase fluid 1 to
nominal operating conditions** or **Initialize two-phase fluid 2 to
nominal operating conditions**. If you set different initial operating
conditions, the flow directions can be different.

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

Flow area at the two-phase fluid 1 port **A1**.

### **Cross-sectional area at port B1** — Flow area at port B1 `0.01 m^2` (default) | positive scalar

Flow area at the two-phase fluid 1 port **B1**.

### **Cross-sectional area at port A2** — Flow area at port A2 `0.01 m^2` (default) | positive scalar

Flow area at the two-phase fluid 2 port **A2**.

### **Cross-sectional area at port B2** — Area normal to flow at port B2 `0.01 m^2` (default) | positive scalar

Flow area at the two-phase fluid 2 port **B2**.

### Two-Phase Fluid 1

### **Nominal operating condition** — Nominal operating condition `Heat transfer from Two-Phase Fluid 1 to Two-Phase Fluid 2` (default) | `Heat transfer from Two-Phase Fluid 2 to Two-Phase Fluid 1`

Nominal operating condition:

- `Heat transfer from Two-Phase Fluid 1 to Two-Phase Fluid
  2` — Side 1 is cooled and side 2 is heated.
- `Heat transfer from Two-Phase Fluid 2 to Two-Phase Fluid
  1` — Side 2 is cooled and side1 is heated.

This setting relates only to the nominal operating condition parameters. It does
not mean that heat transfer can only happen in the specified direction during
simulation.

### **Nominal mass flow rate** — Mass flow rate between two-phase fluid 1 ports during nominal operating condition `0.001 kg/s` (default) | positive scalar

Mass flow rate from port **A1** to port **B1**
during the nominal operating condition.

### **Nominal pressure drop** — Pressure drop between two-phase fluid 1 ports during nominal operating condition `0.01 MPa` (default) | positive scalar

Pressure drop from port **A1** to port **B1**
during the nominal operating condition.

### **Pressure specification** — Select method of pressure specification `Inlet pressure` (default) | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

Select the method of pressure specification:

- `Inlet pressure` — Specify the nominal inlet
  pressure.
- `Saturation pressure at specified saturation
  temperature` — Specify the nominal saturation temperature.

### **Nominal inlet pressure** — Pressure at the two-phase fluid 1 inlet `1 MPa` (default) | positive scalar

Pressure at the two-phase fluid 1 inlet of the heat exchanger during nominal
operating condition.

#### Dependencies

To enable this parameter, set **Pressure specification** to
`Inlet pressure`.

### **Nominal saturation temperature** — Use nominal saturation temperature to specify pressure `313.15 K` (default) | positive scalar

Saturation temperature at the two-phase fluid 1 outlet of the heat exchanger
during nominal operating condition. The pressure in the heat exchanger is the
corresponding saturation pressure. The nominal saturation temperature must be less
than the critical temperature.

#### Dependencies

To enable this parameter, set **Pressure specification** to
`Saturation pressure at specified saturation
temperature`.

### **Inlet condition specification** — Select quantity to describe the inlet condition of the two-phase fluid 1 `Specific enthalpy` (default) | `Temperature` | `Vapor quality`

Quantity used to describe the inlet condition of the fluid at the nominal
operating condition: temperature, specific enthalpy, or vapor quality.

### **Nominal inlet specific enthalpy** — Specific enthalpy at the two-phase fluid 1 inlet `440 kJ/kg` (default) | positive scalar

Specific enthalpy at the two-phase fluid 1 inlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet condition specification**
to `Specific enthalpy`.

### **Nominal inlet temperature** — Temperature at the two-phase fluid 1 inlet `313.15 K` (default) | positive scalar

Temperature at the two-phase fluid 1 inlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet condition specification**
to `Temperature`.

### **Nominal inlet vapor quality** — Vapor quality at the two-phase fluid 1 inlet `1` (default) | positive scalar

Vapor quality, defined as the mass fraction of vapor in a liquid-vapor mixture, at
the two-phase fluid 1 inlet of the heat exchanger during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **Inlet condition specification**
to `Vapor quality`.

### **Heat transfer capacity specification** — How to specify heat transfer capacity of two-phase fluid 1 `Rate of heat transfer` (default) | `Outlet condition`

Whether to specify the performance of the heat exchanger for two-phase fluid 1 at
the nominal operating condition directly, by the rate of heat transfer, or indirectly,
by the outlet condition.

### **Nominal rate of heat transfer** — Rate of heat transfer `0.1 kW` (default) | positive scalar

Rate of heat transfer. The **Nominal Operating condition**
parameter determines the network that the heat transfers from and to:

- If **Nominal operating condition** is `Heat
  transfer from two-phase fluid 1 to two-phase fluid 2`, this
  parameter is the rate of the heat transfer from the two-phase fluid side 1 to side
  2 during the nominal operating condition.
- If **Nominal operating condition** is `Heat
  transfer from two-phase fluid 2 to two-phase fluid 1`, this
  parameter is the rate of the heat transfer from the two-phase fluid side 2 to side
  1 during the nominal operating condition.

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
  `Heat transfer from two-phase fluid 1 to two-phase fluid
  2`.
- `Superheating` — Specify the nominal superheating.
  This option is available if you set **Nominal operating
  condition** to `Heat transfer from two-phase fluid 2 to
  two-phase fluid 1`.
- `Vapor quality` — Specify the nominal vapor
  quality.

#### Dependencies

To enable this parameter, set **Heat transfer capacity
specification** to `Outlet condition`.

### **Nominal outlet specific enthalpy** — Specific enthalpy at the two-phase fluid 1 outlet `250 kJ/kg` (default) | positive scalar | two-element vector

Specific enthalpy at the two-phase fluid 1 outlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Outlet condition
specification** to `Specific enthalpy`.

### **Nominal subcooling** — Degree of temperature below the liquid saturation temperature at the two-phase fluid 1 outlet `5 deltaK` (default) | positive scalar

Degree of temperature below the liquid saturation temperature at the two-phase
fluid 1 outlet of the heat exchanger during the nominal operating condition.

#### Dependencies

To enable this parameter, set **Outlet condition
specification** to `Subcooling`.

### **Nominal superheating** — Degree of temperature above the vapor saturation temperature at the two-phase fluid 1 outlet `5 deltaK` (default) | positive scalar

Degree of temperature above the vapor saturation temperature at the two-phase
fluid 1 outlet of the heat exchanger during the nominal operating condition.

#### Dependencies

To enable this parameter, set **Outlet condition
specification** to `Superheating`.

### **Nominal outlet vapor quality** — Vapor mass fraction at the two-phase fluid 1 outlet `0` (default) | scalar in the range [0,1]

Two-phase fluid vapor quality, defined as the mass fraction of vapor in a
liquid-vapor mixture, at the two-phase fluid 1 outlet of the heat exchanger during the
nominal operating condition.

If using this option, the initial pressure cannot be higher than the critical
pressure.

#### Dependencies

To enable this parameter, set **Outlet condition
specification** to `Vapor quality`.

### **Two-phase fluid 1 volume** — Total volume of two-phase fluid 1 `0.001 m^3` (default) | positive scalar

Total volume of two-phase fluid 1 inside the heat exchanger.

### **Initialize two-phase fluid 1 to nominal operating conditions** — Option for initializing two-phase fluid 1 `on` (default) | `off`

Option to initialize the two-phase fluid to nominal operating conditions or
specified values. If you select this parameter, the block initializes the two-phase
fluid to the nominal operating conditions. If you clear this check box, you can
specify the initial conditions directly with additional parameters.

### **Initial fluid energy specification** — Initial state of the two-phase fluid 1 `Specific enthalpy` (default) | `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

Quantity used to describe the initial state of the side 1 fluid: temperature,
vapor quality, vapor void fraction, specific enthalpy, or specific internal
energy.

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

To enable this parameter, clear the **Initialize two-phase fluid 1 to
nominal operating conditions** check box.

### **Initial two-phase fluid 1 pressure** — Fluid 1 pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Two-phase fluid 1 pressure at the start of the simulation.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 1 to
nominal operating conditions** check box.

### **Initial two-phase fluid 1 specific enthalpy** — Enthalpy per unit mass at start of simulation `1500 kJ/kg` (default) | positive scalar | two-element vector

Two-phase fluid 1 specific enthalpy at the start of simulation. If the value is a
scalar, then the initial specific enthalpy is assumed uniform. If the value is a
two-element vector, then the initial specific enthalpy is assumed to vary linearly
between ports **A1** and **B1**, with the first
element corresponding to port **A1** and the second element
corresponding to port **B1**.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 1 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Specific
enthalpy`.

### **Initial two-phase fluid 1 temperature** — Temperature at start of simulation `293.15 K` (default) | positive scalar | two-element vector

Two-phase fluid 1 temperature at the start of simulation. If the value is a
scalar, then the initial temperature is assumed uniform. If the value is a two-element
vector, then the initial temperature is assumed to vary linearly between ports
**A1** and **B1**, with the first element
corresponding to port **A1** and the second element corresponding to
port **B1**.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 1 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Temperature`.

### **Initial two-phase fluid 1 vapor quality** — Vapor mass fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Two-phase fluid 1 vapor quality, defined as the mass fraction of vapor in a
liquid-vapor mixture, at the start of simulation. If the value is a scalar, then the
initial vapor quality is assumed uniform. If the value is a two-element vector, then
the initial vapor quality is assumed to vary linearly between ports
**A1** and **B1**, with the first element
corresponding to port **A1** and the second element corresponding to
port **B1**.

If using this option, the initial pressure cannot be higher than the critical
pressure.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 1 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Vapor
quality`.

### **Initial two-phase fluid 1 vapor void fraction** — Vapor volume fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Two-phase fluid 1 vapor void fraction, defined as the volume fraction of vapor in
a liquid-vapor mixture,at the start of simulation. If the value is a scalar, then the
initial vapor void fraction is assumed uniform. If the value is a two-element vector,
then the initial vapor void fraction is assumed to vary linearly between ports
**A1** and **B1**, with the first element
corresponding to port **A1** and the second element corresponding to
port **B1**.

If using this option, the initial pressure cannot be higher than the critical
pressure.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 1 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Vapor void
fraction`.

### **Initial two-phase fluid 1 specific internal energy** — Internal energy per unit mass at start of simulation `1500 kJ/kg` (default) | positive scalar | two-element vector

Two-phase fluid 1 specific internal energy at the start of simulation. If the
value is a scalar, then the initial specific internal energy is assumed uniform. If
the value is a two-element vector, then the initial specific internal energy is
assumed to vary linearly between ports **A1** and
**B1**, with the first element corresponding to port
**A1** and the second element corresponding to port
**B1**.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 1 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Specific internal
energy`.

### Two-Phase Fluid 2

### **Nominal mass flow rate** — Mass flow rate between two-phase fluid 2 ports during nominal operating condition `0.001 kg/s` (default) | positive scalar

Mass flow rate from port **A2** to port **B2**
during the nominal operating condition.

### **Nominal pressure drop** — Pressure drop between two-phase fluid 2 ports during nominal operating condition `0.01 MPa` (default) | positive scalar

Pressure drop from port **A2** to port **B2**
during the nominal operating condition.

### **Pressure specification** — Select method of pressure specification `Inlet pressure` (default) | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

Select the method of pressure specification:

- `Inlet pressure` — Specify the nominal inlet
  pressure.
- `Saturation pressure at specified saturation
  temperature` — Specify the nominal saturation temperature.

### **Nominal inlet pressure** — Pressure at the two-phase fluid side inlet `1 MPa` (default) | positive scalar

Pressure at the two-phase fluid 2 inlet of the heat exchanger during nominal
operating condition.

#### Dependencies

To enable this parameter, set **Pressure specification** to
`Inlet pressure`.

### **Nominal saturation temperature** — Use nominal saturation temperature to specify pressure `243.15 K` (default) | positive scalar

Saturation temperature at the two-phase fluid 2 outlet of the heat exchanger
during nominal operating condition. The pressure in the heat exchanger is the
corresponding saturation pressure. The nominal saturation temperature must be less
than the critical temperature.

#### Dependencies

To enable this parameter, set **Pressure specification** to
`Saturation pressure at specified saturation
temperature`.

### **Inlet condition specification** — Select quantity to describe inlet condition of the two-phase fluid 2 `Specific enthalpy` (default) | `Temperature` | `Vapor quality`

Quantity used to describe the inlet condition of the fluid at the nominal
operating condition: temperature, specific enthalpy, or vapor quality.

### **Nominal inlet specific enthalpy** — Specific enthalpy at the two-phase fluid 2 inlet `250 kJ/kg` (default) | positive scalar

Specific enthalpy at the two-phase fluid 2 inlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet condition specification**
to `Specific enthalpy`.

### **Nominal inlet temperature** — Temperature at the two-phase fluid 2 inlet `237.15 K` (default) | positive scalar

Temperature at the two-phase fluid 2 inlet of the heat exchanger during the
nominal operating condition.

#### Dependencies

To enable this parameter, set **Inlet condition specification**
to `Temperature`.

### **Nominal inlet vapor quality** — Vapor quality at the two-phase fluid 2 inlet `0.1` (default) | positive scalar

Vapor quality, defined as the mass fraction of vapor in a liquid-vapor mixture, at
the two-phase fluid 2 inlet of the heat exchanger during the nominal operating
condition.

#### Dependencies

To enable this parameter, set **Inlet condition specification**
to `Vapor quality`.

### **Two-phase fluid 2 volume** — Total volume of two-phase fluid 2 `0.001 m^3` (default) | positive scalar

Total volume of two-phase fluid 2 inside the heat exchanger.

### **Initialize two-phase fluid 2 to nominal operating conditions** — Option for initializing two-phase fluid 2 `on` (default) | `off`

Option to initialize the two-phase fluid to nominal operating conditions or
specified values. If you select this parameter, the block initializes the two-phase
fluid to the nominal operating conditions. If you clear this check box, you can
specify the initial conditions directly with additional parameters.

### **Initial fluid energy specification** — Initial state of the two-phase fluid 2 `Specific enthalpy` (default) | `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

Quantity used to describe the initial state of the side 2 fluid.

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

To enable this parameter, clear the **Initialize two-phase fluid 2 to
nominal operating conditions** check box.

### **Initial two-phase fluid 2 pressure** — Fluid 2 pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Two-phase fluid 2 pressure at the start of the simulation.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 2 to
nominal operating conditions** check box.

### **Initial two-phase fluid 2 specific enthalpy** — Enthalpy per unit mass at start of simulation `1500 kJ/kg` (default) | positive scalar | two-element vector

Two-phase fluid 2 specific enthalpy at the start of simulation. If the value is a
scalar, then the initial specific enthalpy is assumed uniform. If the value is a
two-element vector, then the initial specific enthalpy is assumed to vary linearly
between ports **A2** and **B2**, with the first
element corresponding to port **A2** and the second element
corresponding to port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 2 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Specific
enthalpy`.

### **Initial two-phase fluid 2 temperature** — Temperature at start of simulation `293.15 K` (default) | positive scalar | two-element vector

Two-phase fluid 2 temperature at the start of simulation. If the value is a
scalar, then the initial temperature is assumed uniform. If the value is a two-element
vector, then the initial temperature is assumed to vary linearly between ports
**A2** and **B2**, with the first element
corresponding to port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 2 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Temperature`.

### **Initial two-phase fluid 2 vapor quality** — Vapor mass fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Two-phase fluid 2 vapor quality, defined as the mass fraction of vapor in a
liquid-vapor mixture, at the start of simulation. If the value is a scalar, then the
initial vapor quality is assumed uniform. If the value is a two-element vector, then
the initial vapor quality is assumed to vary linearly between ports
**A2** and **B2**, with the first element
corresponding to port **A2** and the second element corresponding to
port **B2**.

If using this option, the initial pressure cannot be higher than the critical
pressure.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 2 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Vapor
quality`.

### **Initial two-phase fluid 2 vapor void fraction** — Vapor volume fraction at start of simulation `0.5` (default) | scalar in the range [0,1] | two-element vector

Two-phase fluid 2 vapor void fraction, defined as the volume fraction of vapor in
a liquid-vapor mixture,at the start of simulation. If the value is a scalar, then the
initial vapor void fraction is assumed uniform. If the value is a two-element vector,
then the initial vapor void fraction is assumed to vary linearly between ports
**A2** and **B2**, with the first element
corresponding to port **A2** and the second element corresponding to
port **B2**.

If using this option, the initial pressure cannot be higher than the critical
pressure.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 2 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Vapor void
fraction`.

### **Initial two-phase fluid 2 specific internal energy** — Internal energy per unit mass at start of simulation `1500 kJ/kg` (default) | positive scalar | two-element vector

Two-phase fluid 2 specific internal energy at the start of simulation. If the
value is a scalar, then the initial specific internal energy is assumed uniform. If
the value is a two-element vector, then the initial specific internal energy is
assumed to vary linearly between ports **A2** and
**B2**, with the first element corresponding to port
**A2** and the second element corresponding to port
**B2**.

#### Dependencies

To enable this parameter, clear the **Initialize two-phase fluid 2 to
nominal operating conditions** check box and set **Initial fluid
energy specification** to `Specific internal
energy`.

### Correlation Coefficients

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 1 liquid** — Correlation coefficient for subcooled liquid in two-phase fluid 1 `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function
of the Reynolds number and Prandtl number for subcooled liquid in two-phase fluid 1.
The default value is based on the Colburn equation.

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 1 mixture** — Correlation coefficient for liquid-vapor mixture in two-phase fluid 1 `0.005` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function
of the Reynolds number and Prandtl number for liquid-vapor mixture in two-phase fluid
1. The default value is based on the Cavallini and Zecchin correlation.

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 1 vapor** — Correlation coefficient for superheated vapor in two-phase fluid 1 `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for superheated vapor in two-phase fluid 1. The
default value is based on the Colburn equation.

### **b in Nu = a\*Re^b\*Pr^c for two-phase fluid 1** — Reynolds number exponent in correlation for two-phase fluid 1 `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for two-phase fluid 1. The same value applies
to subcooled liquid, liquid-vapor mixture, and superheated vapor.

### **c in Nu = a\*Re^b\*Pr^c for two-phase fluid 1** — Prandtl number exponent in correlation for two-phase fluid 1 `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for two-phase fluid 1. The same value applies
to subcooled liquid, liquid-vapor mixture, and superheated vapor.

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 2 liquid** — Correlation coefficient for subcooled liquid in two-phase fluid 2 `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for subcooled liquid in two-phase fluid 2. The
default value is based on the Colburn equation.

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 2 mixture** — Correlation coefficient for liquid-vapor mixture in two-phase fluid 2 `0.005` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for liquid-vapor mixture in two-phase fluid 2.
The default value is based on the Cavallini and Zecchin correlation.

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 2 vapor** — Correlation coefficient for superheated vapor in two-phase fluid 2 `0.023` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for superheated vapor in two-phase fluid 2. The
default value is based on the Colburn equation.

### **b in Nu = a\*Re^b\*Pr^c for two-phase fluid 2** — Reynolds number exponent in correlation for two-phase fluid 2 `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for two-phase fluid 2. The same value applies
to subcooled liquid, liquid-vapor mixture, and superheated vapor.

### **c in Nu = a\*Re^b\*Pr^c for two-phase fluid 2** — Prandtl number exponent in correlation for two-phase fluid 2 `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for two-phase fluid 2. The same value applies
to subcooled liquid, liquid-vapor mixture, and superheated vapor.
## Libraries

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

### R2023b: Specify initial wall temperature

If you select **Enable wall thermal mass** and clear the
**Initialize wall temperature to nominal operating conditions** check
box, you can use the new **Initial wall temperature** parameter to specify
the initial conditions directly.

## Description

Heat exchanger based on performance data between two two-phase fluid networks

The System-Level Heat Exchanger (2P-2P) block models a heat
exchanger between two distinct two-phase fluid networks. Each network has its own set of fluid
properties.

The block uses performance data from the heat exchanger datasheet, rather than the
detailed geometry of the exchanger. Either or both sides of the heat exchanger can condense or
vaporize fluid as a result of the heat exchange. You can also use this block as an internal
heat exchanger in a refrigeration system. An internal heat exchanger improves refrigeration
system efficiency by providing additional heat exchange between the outlet of the condenser
and the outlet of the evaporator.

You parameterize the block by the nominal operating condition. The heat exchanger is sized
to match the specified performance at the nominal operating condition at steady state.

Each side of the heat exchanger approximates the liquid zone, mixture zone, and vapor zone
based on the change in enthalpy along the flow path.

### Heat Transfer

The block divides the two-phase fluid 1 flow and the two-phase fluid 2 flow each into
three segments of equal size and calculates heat transfer between the fluids is in each
segment. For simplicity, the equation in this section are for one segment.

If you clear the **Enable wall thermal mass** check box, then the heat
balance in the heat exchanger is

Qseg,2P1+Qseg,2P2=0,

where:

- *Q*seg,2P1 is the heat flow rate from the
  wall that is the heat transfer surface to two-phase fluid 1 in the segment.
- *Q*seg,2P2 is the heat flow rate from the
  wall to two-phase fluid 2 in the segment.

If you select **Enable wall thermal mass**, then the heat balance in
the heat exchanger is

Qseg,2P1+Qseg,2P2=−MwallcpwallNdTseg,walldt,

where:

- *M*wall is the mass of the wall.
- *c*pwall is the
  specific heat of the wall.
- *N* = 3 is the number of segments.
- *T*seg,wall is the average wall temperature
  in the segment.
- *t* is time.

The heat flow rate from the wall to two-phase fluid 1 in the segment is

Qseg,2P1=UAseg,2P1(Tseg,wall−Tseg,2P1),

where:

- *UAseg,2P1* is the weighted-average heat
  transfer conductance for two-phase fluid 1 in the segment.
- *Tseg,2P1* is the weighted-average fluid
  temperature for two-phase fluid 1 in the segment.

The heat flow rate from the wall to the two-phase fluid 2 in the segment is

Qseg,2P2=UAseg,2P2(Tseg,wall−Tseg,2P2),

where:

- *UAseg,2P2* is the weighted-average heat
  transfer conductance for two-phase fluid 2 in the segment.
- *Tseg,2P2* is the weighted-average fluid
  temperature for two-phase fluid 2 in the segment.

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

### Two-Phase Fluid 1 Heat Transfer Correlation

The block calculates the heat transfer conductance in both two-phase fluids by using the
same expressions.

If the segment is subcooled liquid, then the heat transfer conductance is

UAseg,L,2P1=aL,2P1(Reseg,L,2P1)b2P1(Prseg,L,2P1)c2P1kseg,L,2P1G2P1N,

where:

- *a*L,2P1,
  *b*2P1, and
  *c*2P1 are the coefficients of the Nusselt
  number correlation. These coefficients are block parameters in the **Correlation
  Coefficients** section.
- *Re*seg,L,2P1 is the average liquid Reynolds
  number for the segment.
- *Pr*seg,L,2P1 is the average liquid Prandtl
  number for the segment.
- *k*seg,L,2P1 is the average liquid thermal
  conductivity for the segment.
- *G*2P1 is the geometry scale factor for the
  two-phase fluid 1 side of the heat exchanger. The block calculates the geometry scale
  factor so that the total heat transfer over all segments matches the specified
  performance at the nominal operating conditions.

The average liquid Reynolds number is

Reseg,L,2P1=m˙seg,2P1Dref,2P1μseg,L,2P1Sref,2P1,

where:

- m˙seg,2P1 is the mass flow rate through the segment.
- *μ*seg,L,2P1 is the average liquid dynamic
  viscosity for the segment.
- *D*ref,2P1 is an arbitrary reference
  diameter.
- *S*ref,2P1 is an arbitrary reference flow
  area.

**Note**

The *D*ref,2P1 and
*S*ref,2P1 terms are included in this equation
for unit calculation purposes only, to make
*Re*seg,L,2P1 nondimensional. The values of
*D*ref,2P1 and
*S*ref,2P1 are arbitrary because the
*G*2P1 calculation overrides these values.

Similarly, if the segment is superheated vapor, then the heat transfer conductance
is

UAseg,V,2P1=aV,2P1(Reseg,V,2P1)b2P1(Prseg,V,2P1)c2P1kseg,V,2P1G2P1N,

where:

- *a*V,2P1,
  *b*2P1, and
  *c*2P1 are the coefficients of the Nusselt
  number correlation. These coefficients appear as block parameters in the
  **Correlation Coefficients** section.
- *Re*seg,V,2P1 is the average vapor Reynolds
  number for the segment.
- *Pr*seg,V,2P1 is the average vapor Prandtl
  number for the segment.
- *k*seg,V,2P1 is the average vapor thermal
  conductivity for the segment.

The average vapor Reynolds number is

Reseg,V,2P1=m˙seg,2P1Dref,2P1μseg,V,2P1Sref,2P1,

where *μ*seg,V,2P1 is the average vapor dynamic
viscosity for the segment.

If the segment is liquid-vapor mixture, then the heat transfer conductance is

UAseg,M,2P1=aM,2P1(Reseg,SL,2P1)b2P1CZ(Prseg,SL,2P1)c2P1kseg,SL,2P1G2P1N,

where:

- *a*M,2P1,
  *b*2P1, and
  *c*2P1 are the coefficients of the Nusselt
  number correlation. These coefficients appear as block parameters in the
  **Correlation Coefficients** section.
- *Re*seg,SL,2P1 is the saturated liquid
  Reynolds number for the segment.
- *Pr*seg,SL,2P1 is the saturated liquid
  Prandtl number for the segment.
- *k*seg,SL,2P1 is the saturated liquid
  thermal conductivity for the segment.
- *CZ* is the Cavallini and Zecchin term.

The saturated liquid Reynolds number is

Reseg,SL,2P1=m˙seg,2P1Dref,2P1μseg,SL,2P1Sref,2P1,

where *μ*seg,SL,2P1 is the saturated liquid
dynamic viscosity for the segment.

The Cavallini and Zecchin term is

CZ=((νseg,SV,2P1νseg,SL,2P1−1)(xseg,out,2P1+1))1+b2P1−((νseg,SV,2P1νseg,SL,2P1−1)(xseg,in,2P1+1))1+b2P1(1+b2P1)(νseg,SV,2P1νseg,SL,2P1−1)(xseg,out,2P1−xseg,in,2P1),

where:

- *ν*seg,SL,2P1 is the saturated liquid
  specific volume for the segment.
- *ν*seg,SV,2P1 is the saturated vapor
  specific volume for the segment.
- *x*seg,in,2P1 is the vapor quality at the
  segment inlet.
- *x*seg,out,2P1 is the vapor quality at the
  segment outlet.

The expression is based on the work of Cavallini and Zecchin [5], which
derives a heat transfer coefficient correlation at a local vapor quality
*x*. Equations for the liquid-vapor mixture are obtained by averaging
Cavallini and Zecchin’s correlation over the segment from
*x*seg,in,2P1 to
*x*seg,out,2P1.

### Two-Phase Fluid 1 Weighted Average

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

ΔL=|min(hseg,out,2P1,hseg,SL,2P1)−min(hseg,in,2P1,hseg,SL,2P1)|⋅UAseg,M,2P1⋅UAseg,V,2P1ΔM=|min(max(hseg,out,2P1,hseg,SL,2P1),hseg,SV,2P1)−min(max(hseg,in,2P1,hseg,SL,2P1),hseg,SV,2P1)|⋅UAseg,L,2P1⋅UAseg,V,2P1ΔV=|max(hseg,out,2P1,hseg,SV,2P1)−max(hseg,in,2P1,hseg,SV,2P1)|⋅UAseg,L,2P1⋅UAseg,M,2P1

where:

- *h*seg,in,2P1 is the specific enthalpy at
  the segment inlet.
- *h*seg,out,2P1 is the specific enthalpy at
  the segment outlet.
- *h*seg,SL,2P1 is the saturated liquid
  specific enthalpy for the segment.
- *h*seg,SV,2P1 is the saturated vapor
  specific enthalpy for the segment.

The weighted-average two-phase fluid 1 heat transfer conductance for the segment is
therefore

UAseg,2P1=wL(UAseg,L,2P1)+wV(UAseg,V,2P1)+wM(UAseg,M,2P1).

The weighted-average fluid 1 temperature for the segment is

Tseg,2P1=wL(UAseg,L,2P1)Tseg,L,2P1+wV(UAseg,V,2P1)Tseg,V,2P1+wM(UAseg,M,2P1)Tseg,M,2P1UAseg,2P1,

where:

- *T*seg,L,2P1 is the average liquid
  temperature for the segment.
- *T*seg,V,2P1 is the average vapor
  temperature for the segment.
- *T*seg,M,2P1 is the average mixture
  temperature for the segment, which is the saturated liquid temperature.

### Two-Phase Fluid 2 Heat Transfer Correlation

If the segment is subcooled liquid, then the heat transfer conductance is

UAseg,L,2P2=aL,2P2(Reseg,L,2P2)b2P2(Prseg,L,2P2)c2P2kseg,L,2P2G2P2N,

where:

- *a*L,2P2,
  *b*L,2P2, and
  *c*L,2P2 are the coefficients of the Nusselt
  number correlation. These coefficients are block parameters in the **Correlation
  Coefficients** section.
- *Re*seg,L,2P2 is the average liquid Reynolds
  number for the segment.
- *Pr*seg,L,2P2 is the average liquid Prandtl
  number for the segment.
- *k*seg,L,2P2 is the average liquid thermal
  conductivity for the segment.
- *G*2P2 is the geometry scale factor for the
  two-phase fluid 2 side of the heat exchanger. The block calculates the geometry scale
  factor so that the total heat transfer over all segments matches the specified
  performance at the nominal operating conditions.

The average liquid Reynolds number is

Reseg,L,2P2=m˙seg,2P2Dref,2P2μseg,L,2P2Sref,2P2,

where:

- m˙seg,2P2 is the mass flow rate through the segment.
- *μ*seg,L,2P2 is the average liquid dynamic
  viscosity for the segment.
- *D*ref,2P2 is an arbitrary reference
  diameter.
- *S*ref,2P2 is an arbitrary reference flow
  area.

**Note**

The *D*ref,2P2 and
*S*ref,2P2 terms are included in this equation
for unit calculation purposes only, to make
*Re*seg,L,2P2 nondimensional. The values of
*D*ref,2P and
*S*ref,2P2 are arbitrary because the
*G*2P2 calculation overrides these values.

Similarly, if the segment is superheated vapor, then the heat transfer conductance
is

UAseg,V,2P2=aV,2P2(Reseg,V,2P2)b2P2(Prseg,V,2P2)c2P2kseg,V,2P2G2P2N,

where:

- *a*V,2P2,
  *b*V,2P2, and
  *c*V,2P2 are the coefficients of the Nusselt
  number correlation. These coefficients appear as block parameters in the
  **Correlation Coefficients** section.
- *Re*seg,V,2P2 is the average vapor Reynolds
  number for the segment.
- *Pr*seg,V,2P2 is the average vapor Prandtl
  number for the segment.
- *k*seg,V,2P2 is the average vapor thermal
  conductivity for the segment.

The average vapor Reynolds number is

Reseg,V,2P2=m˙seg,2P2Dref,2P2μseg,V,2P2Sref,2P2,

where *μ*seg,V,2P2 is the average vapor dynamic
viscosity for the segment.

If the segment is liquid-vapor mixture, then the heat transfer conductance is

UAseg,M,2P2=aM,2P2(Reseg,SL,2P2)b2P2CZ(Prseg,SL,2P2)c2P2kseg,SL,2P2G2P2N,

where:

- *a*M,2P2,
  *b*L,2P2, and
  *c*L,2P2 are the coefficients of the Nusselt
  number correlation. These coefficients appear as block parameters in the
  **Correlation Coefficients** section.
- *Re*seg,SL,2P2 is the saturated liquid
  Reynolds number for the segment.
- *Pr*seg,SL,2P2 is the saturated liquid
  Prandtl number for the segment.
- *k*seg,SL,2P2 is the saturated liquid
  thermal conductivity for the segment.
- *CZ* is the Cavallini and Zecchin term.

The saturated liquid Reynolds number is

Reseg,SL,2P2=m˙seg,2P2Dref,2P2μseg,SL,2P2Sref,2P2,

where *μ*seg,SL,2P2 is the saturated liquid
dynamic viscosity for the segment.

The Cavallini and Zecchin term is

CZ=((νseg,SV,2P2νseg,SL,2P2−1)(xseg,out,2P2+1))1+b2P2−((νseg,SV,2P2νseg,SL,2P2−1)(xseg,in,2P2+1))1+b2P2(1+b2P2)(νseg,SV,2P2νseg,SL,2P2−1)(xseg,out,2P2−xseg,in,2P2),

where:

- *ν*seg,SL,2P2 is the saturated liquid
  specific volume for the segment.
- *ν*seg,SV,2P2 is the saturated vapor
  specific volume for the segment.
- *x*seg,in,2P2 is the vapor quality at the
  segment inlet.
- *x*seg,out,2P2 is the vapor quality at the
  segment outlet.

The expression is based on the work of Cavallini and Zecchin [5], which
derives a heat transfer coefficient correlation at a local vapor quality
*x*. Equations for the liquid-vapor mixture are obtained by averaging
Cavallini and Zecchin’s correlation over the segment from
*x*seg,in,2P2 to
*x*seg,out,2P2.

### Two-Phase Fluid 2 Weighted Average

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

ΔL=|min(hseg,out,2P2,hseg,SL,2P2)−min(hseg,in,2P2,hseg,SL,2P2)|⋅UAseg,M,2P2⋅UAseg,V,2P2ΔM=|min(max(hseg,out,2P2,hseg,SL,2P2),hseg,SV,2P2)−min(max(hseg,in,2P2,hseg,SL,2P2),hseg,SV,2P2)|⋅UAseg,L,2P2⋅UAseg,V,2P2ΔV=|max(hseg,out,2P2,hseg,SV,2P2)−max(hseg,in,2P2,hseg,SV,2P2)|⋅UAseg,L,2P2⋅UAseg,M,2P2

where:

- *h*seg,in,2P2 is the specific enthalpy at
  the segment inlet.
- *h*seg,out,2P2 is the specific enthalpy at
  the segment outlet.
- *h*seg,SL,2P2 is the saturated liquid
  specific enthalpy for the segment.
- *h*seg,SV,2P2 is the saturated vapor
  specific enthalpy for the segment.

The weighted-average two-phase fluid 2 heat transfer conductance for the segment is
therefore

UAseg,2P2=wL(UAseg,L,2P2)+wV(UAseg,V,2P2)+wM(UAseg,M,2P2).

The weighted-average fluid 2 temperature for the segment is

Tseg,2P2=wL(UAseg,L,2P2)Tseg,L,2P2+wV(UAseg,V,2P2)Tseg,V,2P2+wM(UAseg,M,2P2)Tseg,M,2P2UAseg,2P2,

where:

- *T*seg,L,2P2 is the average liquid
  temperature for the segment.
- *T*seg,V,2P2 is the average vapor
  temperature for the segment.
- *T*seg,M,2P2 is the average mixture
  temperature for the segment, which is the saturated liquid temperature.

### Pressure Loss

The pressure losses on the two-phase fluid 1 side are

pA,2P1−p2P1=K2P12m˙A,2P1m˙2A,2P1+m˙2thres,2P12ρavg,2P1pB,2P1−p2P1=K2P12m˙B,2P1m˙2B,2P1+m˙2thres,2P12ρavg,2P1

where:

- *p*A,2P1 and
  *p*B,2P1 are the pressures at ports
  **A1** and **B1**, respectively.
- *p*2P1 is internal two-phase fluid 1
  pressure at which the heat transfer is calculated.
- m˙A,2P1 and m˙B,2P1 are the mass flow rates into ports **A1** and
  **B1**, respectively.
- *ρ*avg,2P1 is the average two-phase fluid 1
  density over all segments.
- m˙thres,2P1 is the laminar threshold for pressure loss, approximated as 1e-4 of
  the nominal mass flow rate. The block calculates the pressure loss coefficient,
  *K*2P1, so that
  *p*A,2P1 –
  *p*B,2P1 matches the nominal pressure loss at
  the nominal mass flow rate.

The pressure losses on the two-phase fluid 2 side are

pA,2P2−p2P2=K2P22m˙A,2P2m˙2A,2P2+m˙2thres,2P22ρavg,2P2pB,2P2−p2P2=K2P22m˙B,2P2m˙2B,2P2+m˙2thres,2P22ρavg,2P2

where:

- *p*A,2P2 and
  *p*B,2P2 are the pressures at ports
  **A2** and **B2**, respectively.
- *p*2P2 is internal two-phase fluid 2
  pressure at which the heat transfer is calculated.
- m˙A,2P2 and m˙B,2P2 are the mass flow rates into ports **A2** and
  **B2**, respectively.
- *ρ*avg,2P2 is the average two-phase fluid 2
  density over all segments.
- m˙thres,2P2 is the laminar threshold for pressure loss, approximated as 1e-4 of
  the nominal mass flow rate. The block calculates the pressure loss coefficient,
  *K*2P2, so that
  *p*A,2P2 –
  *p*B,2P2 matches the nominal pressure loss at
  the nominal mass flow rate.

### Two-Phase Fluid 1 Mass and Energy Conservation

The mass conservation equation for the overall two-phase fluid 1 flow is

(dp2P1dt∑segments(∂ρseg,2P1∂p)+∑segments(duseg,2P1dt∂ρseg,2P1∂u))V2P1N=m˙A,2P1+m˙B,2P1,

where:

- ∂ρseg,2P1∂p is the partial derivative of density with respect to pressure for the
  segment.
- ∂ρseg,2P1∂u is the partial derivative of density with respect to specific internal
  energy for the segment.
- *u*seg,2P1 is the specific internal energy
  for the segment.
- *V*2P1 is the total two-phase fluid 1
  volume.

The summation is over all segments.

**Note**

Although the block divides the two-phase fluid 1 flow into *N*=3
segments for heat transfer calculations, it assumes all segments are at the same internal
pressure, *p*2P1. Consequentially,
*p*2P1 is outside of the summation.

The energy conservation equation for each segment is

duseg,2P1dtM2P1N+useg,2P1(m˙seg,in,2P1−m˙seg,out,2P1)=Φseg,in,2P1−Φseg,out,2P1+Qseg,2P1,

where:

- *M*2P1 is the total two-phase fluid 1
  mass.
- m˙seg,in,2P1 and m˙seg,out,2P1 are the mass flow rates into and out of the segment.
- *Φ*seg,in,2p1 and
  *Φ*seg,out,2p1 are the energy flow rates into
  and out of the segment.

The block assumes the mass flow rates between segments are linearly distributed between
the values of m˙A,2P1 and m˙B,2P1.

### Two-Phase Fluid 2 Mass and Energy Conservation

The mass conservation equation for the overall two-phase fluid 2 flow is

(dp2P2dt∑segments(∂ρseg,2P2∂p)+∑segments(duseg,2P2dt∂ρseg,2P2∂u))V2P2N=m˙A,2P2+m˙B,2P2,

where:

- ∂ρseg,2P2∂p is the partial derivative of density with respect to pressure for the
  segment.
- ∂ρseg,2P2∂u is the partial derivative of density with respect to specific internal
  energy for the segment.
- *u*seg,2P2 is the specific internal energy
  for the segment.
- *V*2P2 is the total two-phase fluid 2
  volume.

The summation is over all segments.

**Note**

Although the block divides the two-phase fluid 2 flow into *N*=3
segments for heat transfer calculations, it assumes all segments are at the same internal
pressure, *p*2P2. Consequentially,
*p*2P2 is outside of the summation.

The energy conservation equation for each segment is

duseg,2P2dtM2P2N+useg,2P2(m˙seg,in,2P2−m˙seg,out,2P2)=Φseg,in,2P2−Φseg,out,2P2+Qseg,2P2,

where:

- *M*2P2 is the total two-phase fluid 2
  mass.
- m˙seg,in,2P2 and m˙seg,out,2P2 are the mass flow rates into and out of the segment.
- *Φ*seg,in,2p2 and
  *Φ*seg,out,2p2 are the energy flow rates into
  and out of the segment.

The block assumes the mass flow rates between segments are linearly distributed between
the values of m˙A,2P2 and m˙B,2P2.
