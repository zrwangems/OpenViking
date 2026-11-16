---
type: simulink-block
title: 'System-Level Condenser Evaporator (2P-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid - Thermal Liquid'
documentation_page: 'systemlevelcondenserevaporator2ptl'
documentation_source_path: 'ref/systemlevelcondenserevaporator2ptl.html'
language: en
---

# System-Level Condenser Evaporator (2P-TL)

## Ports

### Output

### **Q1** — Rate of heat transfer to two-phase fluid, W physical signal

Rate of heat transfer to two-phase fluid, returned as a physical signal, in W. The
physical signals at ports **Q1** and **Q2** are
usually equal in value with opposite sign. However, if you select **Enable
wall thermal mass**, then these two signals may have different values
because the wall may absorb and release some of the heat being transferred.

### **Q2** — Rate of heat transfer to thermal liquid, W physical signal

Rate of heat transfer to thermal liquid, returned as a physical signal, in W. The
physical signals at ports **Q1** and **Q2** are
usually equal in value with opposite sign. However, if you select **Enable
wall thermal mass**, then these two signals may have different values
because the wall may absorb and release some of the heat being transferred.
### Conserving

### **A1** — Two-phase fluid port two-phase fluid

Inlet or outlet port associated with the two-phase fluid.

### **B1** — Two-phase fluid port two-phase fluid

Inlet or outlet port associated with the two-phase fluid.

### **A2** — Thermal liquid port thermal liquid

Inlet or outlet port associated with the thermal liquid.

### **B2** — Thermal liquid port thermal liquid

Inlet or outlet port associated with the thermal liquid.

## Parameters

### Configuration

### **Flow arrangement at nominal operating conditions** — Flow path alignment `Counter flow - Two-Phase Fluid 1 flows from A to B, Thermal Liquid 2 flows from B to A` (default) | `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

Flow path alignment between the heat exchanger sides at nominal operating
condition. The available flow arrangements are:

- `Counter flow - Two-Phase Fluid 1 flows from A to B, Thermal
  Liquid 2 flows from B to A` — The flows run parallel to each
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
the model initialization, when you select **Initialize two-phase fluid to
nominal operating conditions** or **Initialize thermal liquid to
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

Flow area at the two-phase fluid port **A1**.

### **Cross-sectional area at port B1** — Flow area at port B1 `0.01 m^2` (default) | positive scalar

Flow area at the two-phase fluid port **B1**.

### **Cross-sectional area at port A2** — Flow area at port A2 `0.01 m^2` (default) | positive scalar

Flow area at the thermal liquid port **A2**.

### **Cross-sectional area at port B2** — Area normal to flow at port B2 `0.01 m^2` (default) | positive scalar

Flow area at the thermal liquid port **B2**.

### Two-Phase Fluid 1

### **Nominal operating condition** — Select whether nominal operating condition corresponds to condenser or evaporator `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal Liquid 2` (default) | `Evaporator - heat transfer from Thermal Liquid 2 to Two-Phase Fluid 1`

Nominal operating condition:

- `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal
  Liquid 2` — The two-phase fluid is cooled and the thermal liquid is
  heated.
- `Evaporator - heat transfer from Thermal Liquid 2 to Two-Phase
  Fluid 1`  — The thermal liquid is cooled and the two-phase fluid is
  heated.

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
  `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal Liquid
  2`.
- `Saturation pressure at specified evaporating
  temperature` — Specify the nominal evaporating temperature. This
  option is available if you set **Nominal operating condition** to
  `Evaporator - heat transfer from Thermal Liquid 2 to Two-Phase Fluid
  1` .

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
to `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal Liquid
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
to `Evaporator - heat transfer from Thermal Liquid 2 to Two-Phase Fluid
1`  and **Pressure specification** to
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
  - heat transfer from Two-Phase Fluid 1 to Thermal Liquid 2`, this
  parameter is the rate of the of heat transfer from the two-phase fluid to the
  thermal liquid during the nominal operating condition.
- If **Nominal operating condition** is `Evaporator
  - heat transfer from Thermal Liquid 2 to Two-Phase Fluid 1` , this
  parameter is the rate of the of heat transfer from the thermal liquid to the
  two-phase fluid during the nominal operating condition.

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
  `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal Liquid
  2`.
- `Superheating` — Specify the nominal superheating.
  This option is available if you set **Nominal operating
  condition** to `Evaporator - heat transfer from Thermal
  Liquid 2 to Two-Phase Fluid 1` .
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

### Thermal Liquid 2

### **Nominal mass flow rate** — Mass flow rate between thermal liquid ports during nominal operating condition `0.1 kg/s` (default) | positive scalar

Mass flow rate from port **A2** to port **B2**
during the nominal operating condition.

### **Nominal pressure drop** — Pressure drop between thermal liquid ports during nominal operating condition `0.01 MPa` (default) | positive scalar

Pressure drop from port **A2** to port **B2**
during the nominal operating condition.

### **Nominal inlet pressure** — Pressure at the thermal liquid side inlet `0.101325 MPa` (default) | positive scalar

Pressure at the thermal liquid inlet of the heat exchanger during nominal
operating condition.

### **Nominal inlet temperature** — Temperature at the thermal liquid side inlet `293.15 K` (default) | positive scalar

Temperature at the thermal liquid inlet of the heat exchanger during the nominal
operating condition.

### **Thermal liquid volume** — Total volume of thermal liquid in the heat exchanger `0.001 m^3` (default) | positive scalar

Total volume of thermal liquid in the heat exchanger.

### **Initialize thermal liquid to nominal operating conditions** — Option for initializing thermal liquid `on` (default) | `off`

Option to initialize the thermal liquid to nominal operating conditions or
specified values. If you select this parameter, the block initializes the thermal
liquid to the nominal operating conditions. If you clear this check box, you can
specify the initial conditions directly with additional parameters.

### **Initial thermal liquid pressure** — Thermal liquid pressure at start of simulation `0.101325 MPa` (default) | positive scalar

Thermal liquid pressure at the start of the simulation.

#### Dependencies

To enable this parameter, clear the **Initialize thermal liquid to
nominal operating conditions** check box.

### **Initial thermal liquid temperature** — Thermal liquid temperature at start of simulation `293.15 K` (default) | positive scalar | two-element vector

Thermal liquid temperature at the start of simulation. If the value is a scalar,
then the initial temperature is assumed uniform. If the value is a two-element vector,
then the initial temperature is assumed to vary linearly between ports
**A2** and **B2**, with the first element
corresponding to port **A2** and the second element corresponding to
port **B2**.

#### Dependencies

To enable this parameter, clear the **Initialize thermal liquid to
nominal operating conditions** check box.

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

### **a in Nu = a\*Re^b\*Pr^c for thermal liquid** — Correlation coefficient for thermal liquid `0.005` (default) | positive scalar

Proportionality constant in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for thermal liquid. The default value is based
on the Colburn equation.

### **b in Nu = a\*Re^b\*Pr^c for thermal liquid** — Reynolds number exponent in correlation for thermal liquid `0.8` (default) | positive scalar

Reynolds number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for thermal liquid. The default value is based
on the Colburn equation.

### **c in Nu = a\*Re^b\*Pr^c for thermal liquid** — Prandtl number exponent in correlation for thermal liquid `0.33` (default) | positive scalar

Prandtl number exponent in the correlation of the Nusselt number as a function of
the Reynolds number and Prandtl number for thermal liquid. The default value is based
on the Colburn equation.

## Libraries

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Thermal Liquid

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

### R2023b: Specify initial wall temperature

If you select **Enable wall thermal mass** and clear the
**Initialize wall temperature to nominal operating conditions** check
box, you can use the new **Initial wall temperature** parameter to specify
the initial conditions directly.

## Description

Heat exchanger based on performance data between two-phase fluid and thermal liquid networks

The System-Level Condenser Evaporator (2P-TL) block models
a heat exchanger between a two-phase fluid network and a thermal liquid network.

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
based on the change in enthalpy along the flow path.

This block is similar to the Condenser Evaporator (TL-2P)
block, but uses a different parameterization model. The table compares the two blocks:

| Condenser Evaporator (TL-2P) | System-Level Condenser Evaporator (2P-TL) |
| --- | --- |
| Block parameters are based on the heat exchanger geometry | Block parameters are based on performance and operating conditions |
| Heat exchanger geometry may be limited by the available geometry parameter options | Model is independent of the specific heat exchanger geometry |
| You can adjust the block for different performance requirements by tuning geometry parameters, such as fin sizes and tube lengths | You can adjust the block for different performance requirements by directly specifying the desired heat and mass flow rates |
| You can select between parallel, counter, or cross flow configurations | You can select between parallel, counter, or cross-flow arrangement at nominal operating conditions to help with sizing |
| Predictively accurate results over a wide range of operating conditions, subject to the applicability of the E-NTU equations and the heat transfer coefficient correlations | Very accurate results around the specified operating condition; accuracy may decrease far away from the specified operating conditions |
| Heat transfer calculations account for the variation of temperature along the flow path by using the E-NTU model | Heat transfer calculations approximate the variation of temperature along the flow path by dividing it into three segments |
| Accounts for different fluid properties and heat transfer coefficients for subcooled liquid, liquid-vapor mixture, and superheated vapor | Accounts for different fluid properties and heat transfer coefficients for subcooled liquid, liquid-vapor mixture, and superheated vapor |
| Keeps track of variable zone length fractions for subcooled liquid, liquid-vapor mixture, and superheated vapor regions based on the geometry | Approximates the effect of subcooled liquid, liquid-vapor mixture, and superheated vapor regions using weighting factors based on the difference in enthalpy between inlet and outlet |

### Heat Transfer

The block divides the two-phase fluid flow and the thermal liquid flow each into three
segments of equal size and calculates heat transfer between the fluids is in each segment.
For simplicity, the equation in this section are for one segment.

If you clear the **Enable wall thermal mass** check box, then the heat
balance in the heat exchanger is

Qseg,2P+Qseg,TL=0,

where:

- *Q*seg,2P is the heat flow rate from the
  wall that is the heat transfer surface to the two-phase fluid in the segment.
- *Q*seg,TL is the heat flow rate from the
  wall to the thermal liquid in the segment.

If you select **Enable wall thermal mass**, then the heat balance in
the heat exchanger is

Qseg,2P+Qseg,TL=−MwallcpwallNdTseg,walldt,

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

The heat flow rate from the wall to the thermal liquid in the segment is

Qseg,TL=UAseg,TL(Tseg,wall−Tseg,TL),

where:

- *UA*seg,TL is the heat transfer conductance
  for the thermal liquid in the segment.
- *T*seg,TL is the average liquid temperature
  in the segment.

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

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

### Thermal Liquid Heat Transfer Correlation

The heat transfer conductance is

UAseg,TL=aTL(Reseg,TL)bTL(Prseg,TL)cTLkseg,TLGTLN,

where:

- *a*TL,
  *b*TL, and
  *c*TL are the coefficients of the Nusselt
  number correlation. These coefficients are block parameters in the **Correlation
  Coefficients** section.
- *Re*seg,TL is the average Reynolds number
  for the segment.
- *Pr*seg,TL is the average Prandtl number for
  the segment.
- *k*seg,TL is the average thermal
  conductivity for the segment.
- *G*TL is the geometry scale factor for the
  thermal liquid side of the heat exchanger. The block calculates the geometry scale
  factor so that the total heat transfer over all segments matches the specified
  performance at the nominal operating conditions.

The average Reynolds number is

Reseg,TL=m˙seg,TLDref,TLμseg,TLSref,TL,

where:

- m˙seg,TL is the mass flow rate through the segment.
- *μ*seg,TL is the average dynamic viscosity
  for the segment.
- *D*ref,TL is an arbitrary reference
  diameter.
- *S*ref,TL is an arbitrary reference flow
  area.

**Note**

The *D*ref,TL and
*S*ref,TL terms are included in this equation
for unit calculation purposes only, to make
*Re*seg,TL nondimensional. The values of
*D*ref,TL and
*S*ref,TL are arbitrary because the
*G*TL calculation overrides these values.

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

The pressure losses on the thermal liquid side are

pA,TL−pTL=KTL2m˙A,TLm˙2A,TL+m˙2thres,TL2ρavg,TLpB,TL−pTL=KTL2m˙B,TLm˙2B,TL+m˙2thres,TL2ρavg,TL

where:

- *p*A,TL and
  *p*B,TL are the pressures at ports
  **A2** and **B2**, respectively.
- *p*TL is internal thermal liquid pressure at
  which the heat transfer is calculated.
- m˙A,TL and m˙B,TL are the mass flow rates into ports **A2** and
  **B2**, respectively.
- *ρ*avg,TL is the average thermal liquid
  density over all segments.
- m˙thres,TL is the laminar threshold for pressure loss, approximated as 1e-4 of
  the nominal mass flow rate. The block calculates the pressure loss coefficient,
  *K*TL, so that
  *p*A,TL –
  *p*B,TL matches the nominal pressure loss at
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

### Thermal Liquid Mass and Energy Conservation

The mass conservation for the overall thermal liquid flow is

(dpTLdt∑segments(∂ρseg,TL∂p)+∑segments(dTseg,TLdt∂ρseg,TL∂T))VTLN=m˙A,TL+m˙B,TL,

where:

- ∂ρseg,TL∂p is the partial derivative of density with respect to pressure for the
  segment.
- ∂ρseg,TL∂T is the partial derivative of density with respect to temperature for
  the segment.
- *T*seg,TL is the temperature for the
  segment.
- *V*TL is the total thermal liquid
  volume.

The summation is over all segments.

**Note**

Although the block divides the thermal liquid flow into *N*=3
segments for heat transfer calculations, it assumes all segments are at the same internal
pressure, *pTL*. Consequentially,
*pTL* is outside of the summation.

The energy conservation equation for each segment is

(dpTLdt∂useg,TL∂p+dTseg,TLdt∂useg,TL∂T)MTLN+useg,TL(m˙seg,in,TL−m˙seg,out,TL)=Φseg,in,TL−Φseg,out,TL+Qseg,TL,

where:

- ∂useg,TL∂p is the partial derivative of specific internal energy with respect to
  pressure for the segment.
- ∂useg,TL∂T is the partial derivative of specific internal energy with respect to
  temperature for the segment.
- *M*TL is the total thermal liquid
  mass.
- m˙seg,in,TL and m˙seg,out,TL are the mass flow rates into and out of the segment.
- *Φ*seg,in,TL and
  *Φ*seg,out,TL are the energy flow rates into
  and out of the segment.

The block assumes the mass flow rates between segments are linearly distributed between
the values of m˙A,TL and m˙B,TL.
