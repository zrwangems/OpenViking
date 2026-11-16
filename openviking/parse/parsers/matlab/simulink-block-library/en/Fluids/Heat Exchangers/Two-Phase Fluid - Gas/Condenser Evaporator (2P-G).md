---
type: simulink-block
title: 'Condenser Evaporator (2P-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid - Gas'
documentation_page: 'condenserevaporator2pg'
documentation_source_path: 'ref/condenserevaporator2pg.html'
language: en
---

# Condenser Evaporator (2P-G)

## Ports

### Conserving

### **A1** — Two-phase fluid port two-phase fluid

Inlet or outlet port associated with the two-phase fluid.

### **B1** — Two-phase fluid port two-phase fluid

Inlet or outlet port associated with the two-phase fluid.

### **A2** — Gas port gas

Inlet or outlet port associated with the gas.

### **B2** — Gas port gas

Inlet or outlet port associated with the gas.
### Output

### **Z** — Two-phase fluid zone length fractions physical signal

Three-element vector of the zone length fractions in the two-phase
fluid channel, returned as a physical signal. The vector takes the form
[L, M, V], where L is the sub-cooled liquid, M is the liquid-vapor
mixture, and V is the superheated vapor.

## Parameters

### Configuration

### **Flow arrangement** — Flow path alignment `Cross flow` (default) | `Parallel flow` | `Counter flow`

Flow path alignment between heat exchanger sides. The available flow
arrangements are:

- `Parallel flow`. The flows run in
  the same direction.
- `Counter flow`. The flows run
  parallel to each other, in the opposite directions.
- `Cross flow`. The flows run
  perpendicular to each other.

### **Cross flow arrangement** — Thermal mixing condition in each of the flow channels `Both fluids unmixed` (default) | `Both fluids mixed` | `Two-Phase Fluid 1 mixed & Gas 2 unmixed` | `Two-Phase Fluid 1 unmixed & Gas 2 mixed`

Select whether each of the fluids can mix in its channel. Mixed flow
means that the fluid is free to move in the transverse direction as it
travels along the flow path. Unmixed flow means that the fluid is
restricted to travel only along the flow path. For example, a side with
fins is considered an unmixed flow.

#### Dependencies

To enable this parameter, set **Flow
arrangement** to `Cross
flow`.

### **Wall thermal resistance** — Resistance of the wall to heat flow by thermal conduction `0 K/W` (default) | positive scalar

Thermal resistance of the interface wall separating the two heat
exchanger fluids.

### **Cross-sectional area at port A1** — Flow area at port A1 `0.01 m^2` (default) | positive scalar

Flow area at the two-phase fluid port **A1**.

### **Cross-sectional area at port B1** — Flow area at port B1 `0.01 m^2` (default) | positive scalar

Flow area at the two-phase fluid port **B1**.

### **Cross-sectional area at port A2** — Flow area at port A2 `0.01` m^2 (default) | positive scalar

Flow area at the gas port **A2**.

### **Cross-sectional area at port B2** — Flow area at port B2 `0.01` m^2 (default) | positive scalar

Flow area at the gas fluid port **B2**.

### **Enable wall thermal mass** — Option to model wall thermal mass `off` (default) | `on`

Whether to model the heat exchanger wall thermal mass. Modeling the wall thermal
mass introduces a delay in the transient response of the wall to changes in
temperature or heat flux. If you clear **Enable wall thermal
mass**, the block assumes that the wall is thin enough for the transient
response to be instantaneous on the time scale of the heat transfer.

### **Wall mass** — Heat exchanger wall mass `1 kg` (default) | positive scalar

Mass of the heat exchanger wall. The block uses this value to calculate the wall thermal mass.

#### Dependencies

To enable this parameter, select **Enable wall thermal mass**.

### **Wall specific heat** — Heat exchanger wall specific heat `490 J/(K*kg)` (default) | positive scalar

Specific heat of the heat exchanger wall. The block uses this value to calculate the wall thermal mass.

#### Dependencies

To enable this parameter, select **Enable wall thermal mass**.

### Two-Phase Fluid 1

### **Number of tubes** — Number of two-phase fluid tubes `25` (default) | positive scalar

Number of two-phase fluid tubes.

### **Total length of each tube** — Total length of each two-phase fluid tube `1 m` (default) | positive scalar

Total length of each two-phase fluid tube.

### **Tube cross section** — Cross-sectional shape of a tube `Circular` (default) | `Rectangular` | `Annular` | `Generic`

Cross-sectional shape of a tube. Use
`Generic` to specify an arbitrary
cross-sectional geometry.

### **Tube inner diameter** — Internal diameter of a single tube `0.05 m` (default) | positive scalar

Internal diameter of the cross-section of one tube. The cross-section
and diameter are uniform along the tube. The size of the diameter
influences the pressure loss and heat transfer calculations.

#### Dependencies

To enable this parameter, set **Tube
cross-section** to
`Circular`.

### **Tube width** — Internal width of a single tube `0.05 m` (default) | positive scalar

Internal width of the cross-section of one tube. The cross-section and
width are uniform along the tube. The width and height influence the
pressure loss and heat transfer calculations.

#### Dependencies

To enable this parameter, set **Tube
cross-section** to
`Rectangular`.

### **Tube height** — Internal height of a single tube `0.05 m` (default) | positive scalar

Internal height of one tube. The cross-section and height are uniform
along the tube. The width and height influence the pressure loss and
heat transfer calculations.

#### Dependencies

To enable this parameter, set **Tube
cross-section** to
`Rectangular`.

### **Annulus inner diameter (heat transfer surface)** — Smaller diameter of annular cross-section `0.05 m` (default) | positive scalar

Smaller diameter of the annular cross-section of one tube. The
cross-section and inner diameter are uniform along the tube. The inner
diameter influences the pressure loss and heat transfer calculations.
Heat transfer occurs through the inner surface of the annulus.

#### Dependencies

To enable this parameter, set **Tube
cross-section** to
`Annular`.

### **Annulus outer diameter** — Larger diameter of annular cross-section `0.1 m` (default) | positive scalar

Larger diameter of the annular cross-section of one tube. The
cross-section and outer diameter are uniform along the tube. The outer
diameter influences the pressure loss and heat transfer
calculations.

#### Dependencies

To enable this parameter, set **Tube
cross-section** to
`Annular`.

### **Cross-sectional area per tube** — Internal area normal to flow in a single tube `0.002 m^2` (default) | positive scalar

Internal flow area of each tube.

#### Dependencies

To enable this parameter, set **Tube
cross-section** to
`Generic`.

### **Wetted perimeter of tube cross-section for pressure loss** — Perimeter of tube cross-section that fluid touches `0.15 m` (default) | positive scalar

Perimeter of the tube cross-section that the fluid touches. The
cross-section and perimeter are uniform along the tube. This value is
applied in pressure loss calculations.

#### Dependencies

To enable this parameter, set **Tube
cross-section** to
`Generic`.

### **Perimeter of tube cross-section for heat transfer** — Perimeter of a single tube for heat transfer calculations `0.15 m` (default) | positive scalar

Tube perimeter for heat transfer calculations. This is often the same
as the tube perimeter, but in cases such as the annular cross-section,
this may be only the inner or outer diameter, depending on the
heat-transferring surface. The cross-section and tube perimeter are
uniform along the tube.

#### Dependencies

To enable this parameter, set **Tube
cross-section** to
`Generic`.

### **Pressure loss model** — Method of pressure loss calculation due to viscous friction `Correlation for flow inside tubes` (default) | `Pressure loss coefficient`

Method of pressure loss calculation due to viscous friction. The
settings are:

- `Pressure loss coefficient`. Use
  this setting to calculate the pressure loss based on an
  empirical loss coefficient.
- `Correlation for flow inside
  tubes`. Use this setting to calculate the
  pressure loss based on the pipe flow correlation.

### **Pressure loss coefficient, delta\_p/(0.5\*rho\*v^2)** — Empirical loss coefficient for all pressure losses in the channel `10` (default)

Empirical loss coefficient for all pressure losses in the channel.
This value accounts for wall friction and minor losses due to bends,
elbows, and other geometry changes in the channel.

The loss coefficient can be calculated from a nominal operating
condition or be tuned to fit experimental data. It is defined as:

ξ=Δp12ρv2,

where *Δp* is the pressure drop,
*ρ* is the two-phase fluid density, and
*v* is the flow velocity.

#### Dependencies

To enable this parameter, set **Pressure loss
model** to `Pressure loss
coefficient`.

### **Local resistance specification** — Method for quantifying pressure losses `Aggregate equivalent length` (default) | `Local loss coefficient`

Method for quantifying pressure losses in the Haaland
correlation.

#### Dependencies

To enable this parameter, set **Pressure loss
model** to `Correlation for flow inside
tubes`.

### **Aggregate equivalent length of local resistances** — Combined length of all local resistances per tube `0.1 m` (default) | positive scalar

Combined length of all local resistances per tube. This value is the
length of tubing that results in the same pressure losses as the sum of
all minor losses in the tube due to resistances such as bends, tees, or
unions. A longer combined length results in larger pressure losses. The
block adds the value of this parameter to the **Total length of
each tube** parameter in the calculations of pressure loss
due to friction.

#### Dependencies

To enable this parameter, set **Pressure loss
model** to `Correlation for flow inside
tubes` and **Local resistance
specification** to `Aggregate equivalent
length`.

### **Total local loss coefficient** — Pressure loss coefficient `0.1` (default) | positive scalar

Local pressure loss coefficient over the system. You can use this
parameter to calibrate your system to match experimental results.

#### Dependencies

To enable this parameter, set **Pressure loss
model** to `Correlation for flow inside
tubes` and **Local resistance
specification** to `Local loss
coefficient`.

### **Internal surface absolute roughness** — Mean surface roughness height `15e-6 m` (default) | positive scalar

Mean height of tube surface defects. A rougher wall results in larger
pressure losses in the turbulent regime for pressure loss calculated
with the Haaland correlation.

#### Dependencies

To enable this parameter, set either:

- **Pressure loss model**
- **Heat transfer coefficient
  model**

to `Correlation for flow inside
tubes`.

### **Laminar flow upper Reynolds number limit** — Largest Reynolds number that indicates laminar flow `2000` (default) | positive scalar

Largest Reynolds number that indicates laminar flow. Between this
value and the **Turbulent flow lower Reynolds number**,
the flow regime is transitional.

#### Dependencies

To enable this parameter, set **Pressure loss
model** to `Correlations for
tubes`.

### **Turbulent flow lower Reynolds number limit** — Smallest Reynolds number that indicates turbulent flow `4000` (default) | positive scalar

Smallest Reynolds number that indicates turbulent flow. Between this
value and the **Laminar flow upper Reynolds number
limit**, the flow regime is transitional.

#### Dependencies

To enable this parameter, set **Pressure loss
model** to `Correlations for
tubes`.

### **Laminar friction constant for Darcy friction factor** — Coefficient of pressure loss due to viscous friction in laminar flows `64` (default) | positive scalar

Coefficient in pressure loss equations for viscous friction in laminar
flows. This parameter may also be known as the *shape
factor*. The default value corresponds to a circular tube
cross-section.

#### Dependencies

To enable this parameter, set **Pressure loss
model** to `Correlations for
tubes`.

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

Three-element vector containing the empirical coefficients of the
Colburn equation. Each fluid zone has a distinct Nusselt number, which
is calculated by the Colburn equation per zone. The general form of the
Colburn equation is:

Nu=aRebPrc.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Colburn
equation`.

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone** — Cavallini-Zecchin equation coefficients in mixture zone `[.05, .8, .33]` (default) | three-element vector of positive scalars

Three-element vector containing the empirical coefficients of the
Cavallini-Zecchin equation. Each fluid zone has a distinct Nusselt
number, which is calculated in the mixture zone by the Cavallini-Zecchin equation:

Nu=aReSLbPrSLc{[(ρSLρSV−1)xOut+1]1+b−[(ρSLρSV−1)xIn+1]1+b}(1+b)(ρSLρSV−1)(xOut−xIn).

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Colburn
equation`.

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in vapor zone** — Colburn equation coefficients in vapor zone `[.023, .8, .33]` (default) | three-element vector of positive scalars

Three-element vector containing the empirical coefficients of the
Colburn equation. Each fluid zone has a distinct Nusselt number, which
is calculated by the Colburn equation per zone. The general form of the
Colburn equation is:

Nu=aRebPrc.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Colburn
equation`.

### **Laminar flow Nusselt number** — Ratio of convective to conductive heat transfer in the laminar flow regime `3.66` (default) | positive scalar

Ratio of convective to conductive heat transfer in the laminar flow
regime. The fluid Nusselt number influences the heat transfer rate and
depends on the tube cross-section.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Correlation for flow inside
tubes`.

### **Fouling factor** — Additional thermal resistance due to fouling deposits `0.1 m^2*K/kW` (default) | positive scalar

Additional thermal resistance due to fouling layers on the surfaces of
the wall. In real systems, fouling deposits grow over time, however, the
growth is slow enough to be assumed constant during the
simulation.

### **Total fin surface area** — Total heat transfer surface area of fins `0 m^2` (default) | positive scalar

Total heat transfer surface area of both sides of all fins touching
the two-phase fluid. For example, if the fin is rectangular, the surface
area is double the area of the rectangle.

The total heat transfer surface area is the sum of the channel surface
area and the effective fin surface area, which is the product of the
**Fin efficiency** and the **Total fin
surface area**.

### **Fin efficiency** — Ratio of actual-to-ideal transfer rates for fin `0.5` (default) | positive scalar in the range [0,1]

Ratio of actual heat transfer to ideal heat transfer through the fins
touching the two-phase fluid if the entire fin is at the primary heat
transfer surface temperature.

### **Initial fluid energy specification** — Initial state of the two-phase fluid `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

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

### **Initial two-phase fluid pressure** — Fluid pressure at the start of simulation `0.101325 MPa` (default) | positive scalar

Fluid pressure at the start of the simulation.

### **Initial two-phase fluid temperature** — Temperature at the start of simulation `293.15 K` (default) | positive scalar | two-element vector

Temperature in the two-phase fluid channel at the start of simulation.
This parameter can be a scalar or a two-element vector. A scalar value
represents the mean initial temperature in the channel. A vector value
represents the initial temperature at the inlet and outlet in the form
[`inlet`, `outlet`]. The block
calculates a linear gradient between the two ports. The inlet and the
outlet ports are identified according to the initial flow
direction.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to
`Temperature`.

### **Initial two-phase fluid vapor quality** — Vapor mass fraction at the start of simulation `0.5` (default) | positive scalar in the range [0,1] | two-element vector

Vapor mass fraction in the two-phase fluid channel at the start of
simulation. This parameter can be a scalar or a two-element vector. A
scalar value represents the mean initial vapor quality in the channel. A
vector value represents the initial vapor quality at the inlet and
outlet in the form [`inlet`,
`outlet`]. The block calculates a linear gradient
between the two ports. The inlet and the outlet ports are identified
according to the initial flow direction.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Vapor
quality`.

### **Initial two-phase fluid vapor void fraction** — Vapor volume fraction at the start of simulation `0.5` (default) | positive scalar in the range [0,1] | two-element vector

Vapor volume fraction in the two-phase fluid channel at the start of
simulation. This parameter can be a scalar or a two-element vector. A
scalar value represents the mean initial void fraction in the channel. A
vector value represents the initial void fraction at the inlet and
outlet in the form [`inlet`,
`outlet`]. The block calculates a linear gradient
between the two ports. The inlet and the outlet ports are identified
according to the initial flow direction.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Vapor void
fraction`.

### **Initial two-phase fluid specific enthalpy** — Enthalpy per unit mass at the start of simulation `1500 kJ/kg` (default) | positive scalar | two-element vector

Enthalpy per unit mass in the two-phase fluid channel at the start of
simulation. This parameter can be a scalar or a two-element vector. A
scalar value represents the mean initial specific enthalpy in the
channel. A vector value represents the initial specific enthalpy at the
inlet and outlet in the form [`inlet`,
`outlet`]. The block calculates a linear gradient
between the two ports. The inlet and the outlet ports are identified
according to the initial flow direction.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Specific
enthalpy`.

### **Initial two-phase fluid specific internal energy** — Internal energy per unit mass at the start of simulation `1500 kJ/kg` (default) | positive scalar | two-element vector

Internal energy per unit mass in the two-phase fluid channel at the
start of simulation. This parameter can be a scalar or a two-element
vector. A scalar value represents the mean initial specific internal
energy in the channel. A vector value represents the initial specific
internal energy at the inlet and outlet in the form
[`inlet`, `outlet`]. The block
calculates a linear gradient between the two ports. The inlet and the
outlet ports are identified according to the initial flow
direction.

#### Dependencies

To enable this parameter, set **Initial fluid energy
specification** to `Specific internal
energy`.

### Gas 2

### **Flow geometry** — Gas flow configuration `Flow inside one or more tubes` (default) | `Flow perpendicular to bank of circular tubes` | `Generic`

Gas flow path. The flow can run externally over a set of tubes or
internal to a tube or set of tubes. You can also specify a generic
parameterization based on empirical values.

### **Number of tubes** — Number of gas tubes `25` (default) | positive scalar

Number of gas tubes. More tubes result in higher pressure losses due
to viscous friction, but a larger amount of surface area for heat
transfer.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes`.

### **Total length of each tube** — Total length of each gas tube `1 m` (default) | positive scalar

Total length of each gas tube.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes`.

### **Tube cross section** — Cross-sectional shape of a tube `Circular` (default) | `Rectangular` | `Annular` | `Generic`

Cross-sectional shape of one tube. Set to
`Generic` to specify an arbitrary
cross-sectional geometry.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes`.

### **Tube inner diameter** — Internal diameter of a single tube `0.05 m` (default) | positive scalar

Internal diameter of the cross-section of one tube. The cross-section
and diameter are uniform along the tube. The size of the diameter
influences the pressure loss and heat transfer calculations.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
**Tube cross-section** to
`Circular`.

### **Tube width** — Internal width of a single tube `0.05 m` (default) | positive scalar

Internal width of the cross-section of one tube. The cross-section and
width are uniform along the tube. The width and height influence the
pressure loss and heat transfer calculations.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
**Tube cross-section** to
`Rectangular`.

### **Tube height** — Internal height of a single tube `0.05 m` (default) | positive scalar

Internal height of one tube. The cross-section and height are uniform
along the tube. The width and height influence the pressure loss and
heat transfer calculations.

#### Dependencies

To enable this parameter, set **Flow geometry**
parameterization of `Flow inside one or more
tubes` and **Tube cross-section**
to `Rectangular`.

### **Annulus inner diameter (heat transfer surface)** — Smaller diameter of annular cross-section `0.05 m` (default) | positive scalar

Smaller diameter of the annular cross-section of one tube. The
cross-section and inner diameter are uniform along the tube. The inner
diameter influences the pressure loss and heat transfer calculations.
Heat transfer occurs through the inner surface of the annulus.

#### Dependencies

To enable this parameter, set **Flow geometry**
parameterization of `Flow inside one or more
tubes` and **Tube cross-section**
to `Annular`.

### **Annulus outer diameter** — Larger diameter of annular cross-section `0.1 m` (default) | positive scalar

Larger diameter of the annular cross-section of one tube. The
cross-section and outer diameter are uniform along the tube. The outer
diameter influences the pressure loss and heat transfer
calculations.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
**Tube cross-section** to
`Annular`.

### **Cross-sectional area per tube** — Internal flow area in each tube `0.002 m^2` (default) | positive scalar

Internal flow area of each tube.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
**Tube cross-section** to
`Generic`.

### **Wetted perimeter of tube cross-section for pressure loss** — Perimeter of tube cross-section that fluid touches `0.15 m` (default) | positive scalar

Perimeter of the tube cross-section that the fluid touches. The
cross-section and perimeter are uniform along the tube. This value is
applied in pressure loss calculations.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
**Tube cross-section** to
`Generic`.

### **Perimeter of tube cross-section for heat transfer** — Perimeter of a single tube for heat transfer calculations `0.15 m` (default) | positive scalar

Tube perimeter for heat transfer calculations. This is often the same
as the tube perimeter, but in cases such as the annular cross-section,
this may be only the inner or outer diameter, depending on the
heat-transferring surface. The cross-section and tube perimeter are
uniform along the tube.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
**Tube cross-section** to
`Generic`.

### **Pressure loss model** — Method of pressure loss calculation due to viscous friction `Correlation for flow inside tubes` (default) | `Euler number per tube row` | `Pressure loss coefficient` | `Correlation for flow over tube bank`

Method of pressure loss calculation due to viscous friction. Different
models are available for different flow configurations. The settings are:

- `Correlation for flow inside
  tubes`. Use this setting to calculate the
  pressure loss with the Haaland correlation.
- `Pressure loss coefficient`. Use
  this setting to calculate the pressure loss based on an
  empirical loss coefficient.
- `Euler number per tube row`. Use
  this setting to calculate the pressure loss based on an
  empirical Euler number.
- `Correlation for flow over tube
  bank`. Use this setting to calculate the
  pressure loss based on the Hagen number.

The pressure loss models available depend on the **Flow
geometry** setting.

#### Dependencies

When **Flow geometry** is set to
`Flow inside one or more tubes`,
**Pressure loss model** can be set to either:

- `Pressure loss
  coefficient`.
- `Correlation for flow inside
  tubes`.

When **Flow geometry** is set to
`Flow perpendicular to bank of circular
tubes`, **Pressure loss model**
can be set to either:

- `Correlation for flow over tube
  bank`.
- `Euler number per tube
  row`.

When **Flow geometry** is set to
`Generic`, the **Pressure loss
model** parameter is disabled. Pressure loss is
calculated empirically with the **Pressure loss coefficient,
delta\_p/(0.5\*rho\*v^2)** parameter.

### **Pressure loss coefficient, delta\_p/(0.5\*rho\*v^2)** — Empirical loss coefficient for all pressure losses in the channel `10` (default) | positive scalar

Empirical loss coefficient for all pressure losses in the channel.
This value accounts for wall friction and minor losses due to bends,
elbows, and other geometry changes in the channel.

The loss coefficient can be calculated from a nominal operating
condition or be tuned to fit experimental data. It is defined as:

ξ=Δp12ρv2,

where *Δp* is the pressure drop,
*ρ* is the gas density, and *v* is
the flow velocity.

#### Dependencies

To enable this parameter, set either:

- **Flow geometry** to
  `Flow inside one or more
  tubes` and **Pressure loss
  model** to `Pressure loss
  coefficient`.
- **Flow geometry** to
  `Generic`.

### **Local resistance specification** — Method for quantifying pressure losses `Aggregate equivalent length` (default) | `Local loss coefficient`

Method for quantifying pressure losses in the Haaland
correlation.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
**Pressure loss model** to
`Correlation for flow inside
tubes`.

### **Aggregate equivalent length of local resistances** — Combined length of all local resistances per tube `0.1 m` (default) | positive scalar

Combined length of all local resistances per tube. This value is the
length of tubing that results in the same pressure losses as the sum of
all minor losses in the tube due to resistances such as bends, tees, or
unions. A longer combined length results in larger pressure losses. The
block adds the value of this parameter to the **Total length of
each tube** parameter in the calculations of pressure loss
due to friction.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes`,
**Pressure loss model** to
`Correlations for flow inside tubes`,
and **Local resistance specification** to
`Aggregate equivalent length`.

### **Total local loss coefficient** — Pressure loss coefficient `0.1` (default) | positive scalar

Local pressure loss coefficient over the system. You can use this
parameter to calibrate your system to match experimental results.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes`,
**Pressure loss model** to
`Correlation for flow inside tubes`,
and **Local resistance specification** to
`Local loss coefficient`.

### **Internal surface absolute roughness** — Mean surface roughness height `15e-6 m` (default) | positive scalar

Mean height of tube surface defects. A rougher wall results in larger
pressure losses in the turbulent regime for pressure loss calculated
with the Haaland correlation.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
either:

- **Pressure loss model**
- **Heat transfer coefficient
  model**

to `Correlation for flow inside
tubes`.

### **Laminar flow upper Reynolds number limit** — Largest Reynolds number that indicates laminar flow `2000` (default) | positive scalar

Largest Reynolds number that indicates laminar flow. Between this
value and the **Turbulent flow lower Reynolds number
limit**, the flow regime is transitional.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
**Pressure loss model** to
`Correlation for flow inside
tubes`.

### **Turbulent flow lower Reynolds number limit** — Smallest Reynolds number that indicates turbulent flow `4000` (default) | positive scalar

Smallest Reynolds number that indicates turbulent flow. Between this
value and the **Laminar flow upper Reynolds number
limit**, the flow regime is transitional between the
laminar and turbulent regimes.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes` and
**Pressure loss model** to
`Correlation for flow inside
tubes`.

### **Laminar friction constant for Darcy friction factor** — Coefficient of pressure loss due to viscous friction in laminar flows `64` (default) | positive scalar

Coefficient in pressure loss equations for viscous friction in laminar
flows. This parameter is also known as the *shape
factor*. The default value corresponds to a circular tube
cross-section.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Correlation for flow inside tubes`,
**Tube cross section** to
`Generic`, and **Pressure loss
model** to `Correlation for flow inside
tubes`.

### **Heat transfer coefficient model** — Method of calculating heat transfer coefficient between fluid and wall `Correlation for flow over tube bank` (default) | `Colburn equation` | `Correlation for flow inside tubes`

Method of calculating the heat transfer coefficient between the fluid
and the wall. The available settings are:

- `Colburn equation`. Use this
  setting to calculate the heat transfer coefficient with
  user-defined variables *a*,
  *b*, and *c* of
  the Colburn equation.
- `Correlation for flow over tube
  bank`. Use this setting to calculate the
  heat transfer coefficient based on the tube bank correlation
  using the Hagen number.
- `Correlation for flow inside
  tubes`. Use this setting to calculate the
  heat transfer coefficient for pipe flows with the Gnielinski
  correlation.

#### Dependencies

To enable this parameter, set **Flow geometry**
to either:

- `Flow perpendicular to bank of circular
  tubes`.
- `Flow inside one or more
  tubes`.

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c** — Colburn equation coefficients `[0.023, 0.8, 0.33]` (default) | three-element vector

Three-element vector containing the empirical coefficients of the
Colburn equation. The Colburn equation is a formulation for calculating
the Nusselt Number. The general form of the Colburn equation is:

Nu=aRebPrc.

When the **Heat transfer coefficient model** is set
to `Colburn equation` and **Flow
geometry** is set to `Flow inside one or more
tubes`, or **Flow geometry** is set to
`Generic`, the default Colburn equation is:

Nu=0.023Re0.8Pr1/3.

When the **Heat transfer coefficient
model** is set to `Colburn
equation` and **Flow geometry** is set
to `Flow perpendicular to bank of circular
tubes`, the default Colburn equation is:

Nu=0.27Re0.63Pr0.36.

#### Dependencies

To enable this parameter, set:

1. **Flow geometry** to either:

   - `Flow inside one or more
     tubes`
   - `Flow perpendicular to bank of
     circular tubes`

   and **Heat transfer coefficient
   model** to `Colburn
   equation`.
2. **Flow geometry** to
   `Generic`.

### **Laminar flow Nusselt number** — Ratio of convective to conductive heat transfer in the laminar flow regime `3.66` (default) | positive scalar

Ratio of convective to conductive heat transfer in the laminar flow
regime. The fluid Nusselt number influences the heat transfer rate and
depends on the tube cross-section.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow inside one or more tubes`,
**Tube cross-section** to
`Generic`, and **Heat transfer
parameterization** to `Correlation for flow
inside tubes`.

### **Tube bank grid arrangement** — Geometrical placement of tube rows in the bank `Inline` (default) | `Staggered`

Alignment of tubes in a tube bank. Rows are either in line with their
neighbors, or staggered.

- `Inline`: All tube rows are
  located directly behind each other.
- `Staggered`: Tubes of the one
  tube row are located at the gap between tubes of the
  previous tube row.

Tube alignment influences the Nusselt number and the heat transfer
rate.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow perpendicular to bank of circular
tubes`.

### **Number of tube rows along flow direction** — Number of two-phase fluid tube rows in the tube bank `5` (default) | positive scalar

Number of two-phase fluid tube rows in a tube bank. The rows are
aligned with the direction of gas flow.

#### Dependencies

To enable this parameter, set **Flow geometry**to
`Flow perpendicular to bank of circular
tubes`.

### **Number of tube segments in each tube row** — Number of two-phase fluid tubes in each row of the tube bank `5` (default) | positive scalar

Number of two-phase fluid tubes in each row of a tube bank. This
measurement is perpendicular to the gas flow.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow perpendicular to bank of circular
tubes`.

### **Length of each tube segment in a tube row** — Length of each two-phase fluid tube `1 m` (default) | positive scalar

Length of each tube that spans a tube row. All tubes in a tube bank
are the same length.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow perpendicular to bank of circular
tubes`.

### **Tube outer diameter** — External diameter of a single two-phase fluid tube `0.05 m` (default) | positive scalar

Outer diameter of a two-phase fluid tube. The cross-section is uniform
along a tube and so the diameter is constant throughout. This value
influences the losses in the flow across a tube bank due to viscous
friction.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow perpendicular to bank of circular
tubes`.

### **Longitudinal tube pitch (along flow direction)** — Center-to-center distance between two-phase fluid tube rows `0.15 m` (default) | positive scalar

Distance between tube centers of the two-phase fluid tubes, aligned
with the direction of flow of the gas.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow perpendicular to bank of circular
tubes`.

### **Transverse tube pitch (perpendicular to flow direction)** — Center-to-center distance between two-phase fluid tubes in a row `0.15` m (default) | positive scalar

Distance between the tube centers in a row of two-phase fluid tubes.
This measurement is perpendicular to the gas flow direction. See Heat Transfer Coefficient for Flows Across a Tube Bank for
more information.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow perpendicular to bank of circular
tubes`.

### **Euler number per tube row, delta\_p/(N\*0.5\*rho\*v^2)** — Euler number for each row of the tube bank `10` (default) | positive scalar

Empirical coefficient for pressure drop across one tube row. The Euler
number is the ratio between pressure drop and fluid momentum:

Eu=ΔpN12ρv2,

where *N* is the **Number of
tube rows along flow direction**, *Δp* is
the pressure drop, *ρ* is the gas mixture density, and
*v* is the flow velocity.

Each tube row is located in a plane perpendicular to the gas
flow.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Flow perpendicular to bank of circular
tubes` and **Pressure loss model**
to `Euler number per tube row`.

### **Minimum free-flow area** — Smallest total flow area between inlet and outlet `0.01 m^2` (default) | positive scalar

Smallest total cross-sectional flow area between inlet and outlet. If
the channel is a collection of ducts, tubes, slots, or grooves, the
value of this parameter is the sum of the smallest areas at the minimum
flow area point. This parameter is the area where the fluid velocity is
highest. For example, if the fluid flows perpendicular to a bank of
tubes, the value of this parameter is the sum of the gaps between the
tubes in one cross-section where the sum of the gaps is smallest is
smallest.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Generic`.

### **Heat transfer surface area without fins** — Total area of the heat transfer surface excluding fins `2 m^2` (default) | positive scalar

Total area of the heat transfer surface, excluding fins.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Generic`.

### **Gas volume inside heat exchanger** — Total volume of gas in the heat exchanger `0.05 m^3` (default) | positive scalar

Total volume of gas in the heat exchanger.

#### Dependencies

To enable this parameter, set **Flow geometry**
to `Generic`.

### **Fouling factor** — Additional thermal resistance due to fouling deposits `0.1 m^2*K/kW` (default) | positive scalar

Additional thermal resistance due to fouling layers on the surfaces of
the wall. In real systems, fouling deposits grow over time. However, the
growth is slow enough to be assumed constant during the simulation.

### **Total fin surface area** — Total heat transfer surface area of all fins `0 m^2` (default) | positive scalar

Total heat transfer surface area of both sides of all fins touching
the gas. For example, if the fin is rectangular, the surface area is
double the area of the rectangle.

The total heat transfer surface area is the sum of the channel surface
area and the effective fin surface area, which is the product of the
**Fin efficiency** and the **Total fin
surface area**.

### **Fin efficiency** — Ratio of actual-to-ideal transfer rates for fin `0.5` (default) | positive scalar in the range [0,1]

Ratio of actual heat transfer to ideal heat transfer through the fins
touching the gas if the entire fin is at the primary heat transfer
surface temperature.

### **Initial gas pressure** — Gas pressure at the start of simulation `0.101325 MPa` (default) | positive scalar

Gas pressure at the start of the simulation.

### **Initial gas temperature** — Temperature at the start of simulation `293.15 K` (default) | positive scalar | two-element vector

Temperature in the gas channel at the start of the simulation. This
parameter can be a scalar or a two-element vector. A scalar value
represents the mean initial temperature in the channel. A vector value
represents the initial temperature at the inlet and outlet in the form
[`inlet`, `outlet`]. The block
calculates a linear gradient between the two ports. The inlet and the
outlet ports are identified according to the initial flow
direction.

## Libraries

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Gas

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

### R2025a: Model thermal mass of heat exchanger wall

Select **Wall thermal dynamics** to model the thermal mass of the
heat exchanger wall.

## Description

Heat exchanger between gas and two-phase fluid networks

The Condenser Evaporator (2P-G) block models a heat exchanger with one
two-phase fluid network, which flows between ports **A1** and
**B1**, and one gas network, which flows between ports
**A2** and **B2**. The heat exchanger can act as a
condenser or as an evaporator. The fluid streams can be aligned in parallel, counter, or
cross-flow configurations.

**Example Heat Exchanger for Refrigeration Applications**

You can model the gas side as flow within tubes, flow around the two-phase fluid
tubing, or by an empirical, generic parameterization.

The block uses the Effectiveness-NTU (E-NTU) method to model heat transfer through the
shared wall. Fouling on the exchanger walls, which increases thermal resistance and
reduces the heat exchange between the two fluids, is also modeled. You can also
optionally model fins on both the gas and two-phase fluid sides. Pressure loss due to
viscous friction on both sides of the exchanger can be modeled analytically or by
generic parameterization, which you can use to tune to your own data.

You can model the two-phase fluid side as flow within a tube or a set of tubes. The
two-phase fluid tubes use a boundary-following model to track the sub-cooled liquid (L),
vapor-liquid mixture (M), and super-heated vapor (V) in three zones. The relative amount
of space a zone occupies in the system is called a *zone length
fraction* within the system.

**Zone Length Fractions in the Two-Phase Fluid Piping**

The sum of the zone length fractions in the two-phase fluid tubing equals
`1`. Port **Z** returns the zone
length fractions as a vector of physical signals for each of the three phases: [L, M,
V].

### Heat Exchanger Configuration

The heat exchanger effectiveness is based on the selected heat exchanger
configuration, the fluid properties in each phase, the tube geometry and flow
configuration on each side of the exchanger, and the usage and size of fins.

**Flow Arrangement**

The **Flow arrangement** parameter assigns the relative flow
paths between the two sides:

- `Parallel flow` indicates the fluids are
  moving in the same direction.
- `Counter flow` indicates the fluids are
  moving in parallel, but opposite directions.
- `Cross flow` indicates the fluids are
  moving perpendicular to each other.

**Thermal Mixing**

When **Flow arrangement** is set to `Cross
flow`, use the **Cross flow arrangement**
parameter to indicate whether the two-phase fluid or gas flows are separated
into multiple paths by baffles or walls. Without these separations, the flow can
mix freely and is considered *mixed*. Both fluids, one fluid,
or neither fluid can be mixed in the cross-flow arrangement. Mixing homogenizes
the fluid temperature along the direction of flow of the second fluid, and
varies perpendicular to the second fluid flow.

Unmixed flows vary in temperature both along and perpendicular to the flow
path of the second fluid.

**Sample Cross-Flow Configurations**

Note that the flow direction during simulation does not impact the selected
flow arrangement setting. The ports on the block do not reflect the physical
positions of the ports in the physical heat exchange system.

All flow arrangements are single-pass, which means that the fluids do not make
multiple turns in the exchanger for additional points of heat transfer. To model
a multi-pass heat exchanger, you can arrange multiple Condenser Evaporator
(2P-G) blocks in series or in parallel.

For example, to achieve a two-pass configuration on the two-phase fluid side
and a single-pass configuration on the gas side, you can connect the two-phase
fluid sides in series and the gas sides to the same input in parallel (such as
two Flow Rate Source blocks with half of the total mass flow rate), as shown
below.

**Flow Geometry**

The **Flow geometry** parameter sets the gas flow arrangement
as either inside a tube or set of tubes, or perpendicular to a tube bank. You
can also specify an empirical, generic configuration. The two-phase fluid always
flows inside a tube or set of tubes.

When **Flow geometry** is set to `Flow
perpendicular to bank of circular tubes`, use the
**Tube bank grid arrangement** parameter to define the
two-phase fluid tube bank alignment as either `Inline`
or `Staggered`. The red, downward-pointing arrow
indicates the direction of gas flow. The Inline figure also shows the
**Number of tube rows along flow direction** and the
**Number of tube segments in each tube row** parameters.
Here, *flow direction* refers to the gas flow, and
*tube* refers to the two-phase fluid tubing. The
**Length of each tube segment in a tube row** parameter is
indicated in the Staggered figure.

**Fins**

The heat exchanger configuration does not have fins when the **Total
fin surface area** parameter is `0 m^2`. Fins
introduce additional surface area for heat transfer. Each fluid side has a
separate fin area and parameters that describe the fins in that fluid. For
example, when the gas flows inside the tubes and the two-phase fluid flows
outside of the tubes, the **Total fin surface area** and
**Fin efficiency** parameters in the **Gas
2** section describe the fins protruding into the tube. The
**Total fin surface area** and **Fin
efficiency** parameters in the **Two-Phase Fluid
1** section describe the fins outside of the tubes.

### Effectiveness-NTU Heat Transfer

The heat transfer rate is calculated for each fluid phase. In accordance with the
three fluid zones that occur on the two-phase fluid side of the heat exchanger, the
heat transfer rate is calculated in three sections.

The convective heat transfer in a zone is

Qzone=ϵCMin(TIn,G−TIn,2P),

where:

- *C*Min is the lesser of the
  heat capacity rates of the two fluids in that zone. The heat capacity
  rate is the product of the fluid specific heat,
  *c*p, and the fluid mass
  flow rate. *C*Min is always
  positive.
- *T*In,2P is the zone inlet
  temperature of the two-phase fluid.
- *T*In,G is the zone inlet
  temperature of the gas.
- *ε* is the heat exchanger effectiveness.

Effectiveness is a function of the heat capacity rate and the number
of transfer units, *NTU*, and also varies based on the heat
exchanger flow arrangement. The *NTU* is calculated as:

NTU=zCMinR,

where:

- *z* is the individual zone length fraction.
- *R* is the total thermal resistance between the two
  flows, due to convection, conduction, and any fouling on the tube walls:

  R=1U2PATh,2P+F2PATh,2P+RW+FGATh,G+1UGATh,G,

  where:

  - *U* is the convective heat transfer
    coefficient of the respective fluid.
  - *F* is the **Fouling
    factor** on the two-phase fluid or gas side,
    respectively.
  - *R*W is the
    **Thermal resistance through heat transfer
    surface**.
  - *A*Th is the heat
    transfer surface area of the respective side of the
    exchanger. *A*Th is
    the sum of the wall surface area,
    *A*W, and the
    **Total fin surface area**,
    *A*F:

    ATh=AW+ηFAF,

    where
    *η*F is the
    **Fin efficiency**.

The total convective heat transfer rate between the fluids is the sum of the heat
transferred in the three zones by the subcooled liquid
(*QL*), liquid-vapor mixture
(*QM*), and superheated vapor
(*QV*):

Q=∑QZ=QL+QM+QV.

**Effectiveness by Flow Arrangement**

The heat exchanger effectiveness varies according to its flow configuration
and the mixing in each fluid. Below are the formulations for effectiveness
calculated in the liquid and vapor zones for each configuration. The
effectiveness is ε=1−exp(−NTU) for all configurations in the mixture zone.

- When **Flow arrangement** is set to
  `Parallel flow`:

  ϵ=1−exp[−NTU(1+CR)]1+CR
- When **Flow arrangement** is set to
  `Counter flow`:

  ϵ=1−exp[−NTU(1−CR)]1−CRexp[−NTU(1−CR)]
- When **Flow arrangement** is set to
  `Cross flow` and **Cross flow
  arrangement** is set to `Both fluids
  unmixed`:

  ϵ=1−exp{NTU0.22CR[exp(−CRNTU0.78)−1]}
- When **Flow arrangement** is set to
  `Cross flow` and **Cross flow
  arrangement** is set to `Both fluids
  mixed`:

  ϵ=[11−exp(−NTU)+CR1−exp(−CRNTU)−1NTU]−1

When one fluid is mixed and the other unmixed, the equation for
effectiveness depends on the relative heat capacity rates of the fluids.
When **Flow arrangement** is set to `Cross
flow` and **Cross flow arrangement**
is set to either `Two-Phase Fluid 1 mixed & Gas 2
unmixed` or `Two-Phase Fluid 1 unmixed
& Gas 2 mixed`:

- When the fluid with Cmax is mixed and the
  fluid with Cmin is unmixed:

  ϵ=1CR(1−exp{−CR{1−exp(−NTU)}})
- When the fluid with Cmin is mixed and the
  fluid with Cmax is unmixed:

  ϵ=1−exp{−1CR[1−exp(−CRNTU)]}

*C*R denotes the ratio
between the heat capacity rates of the two fluids:

CR=CMinCMax.

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

### Conductive Heat Transfer

The conductive heat transfer in a zone is

Qcond=Tout,2P−Tout,GRcond,

where:

- *Tout,2P* is the zone outlet
  temperature of the two-phase fluid.
- *Tout,g* is the zone outlet
  temperature of the gas.
- *Rcond* is the total
  conductive thermal resistance between the two flows,

  Rcond=Dhk2PAW,2P+F2PAW,2P+RW+FGAW,G+DhkGAW,G,

  where:

  - *AW* is the wall
    surface area.
  - *k* is the thermal conductivity of each
    fluid.
  - *DH* is the
    hydraulic diameter.

The total heat transfer is the sum of the convective and conductive heat transfer.
The conductive heat transfer is negligible compared to the convective heat transfer.
When the flow rate is zero, the convective heat transfer is also zero. However,
because heat transfer from convection and conduction operate independently of each
other, there is still conductive heat transfer even when the convective heat
transfer is zero.

### Two-Phase Fluid Correlations

**Heat Transfer Coefficient**

The convective heat transfer coefficient varies according to the fluid Nusselt number:

U=NukDH,

where:

- *Nu* is the zone mean Nusselt number, which
  depends on the flow regime.
- *k* is the fluid phase thermal
  conductivity.
- *D*H is tube hydraulic
  diameter.

For turbulent flows in the subcooled liquid or superheated vapor zones, the
Nusselt number is calculated with the Gnielinski correlation:

Nu=fD8(Re−1000)Pr1+12.7f8(Pr2/3−1),

where:

- *Re* is the fluid Reynolds number.
- *Pr* is the fluid Prandtl number.

For turbulent flows in the liquid-vapor mixture zone, the Nusselt number is
calculated with the Cavallini-Zecchin correlation:

Nu=aReSLbPrSLc{[(ρSLρSV−1)xOut+1]1+b−[(ρSLρSV−1)xIn+1]1+b}(1+b)(ρSLρSV−1)(xOut−xIn).

where:

- *Re*SL is the Reynolds
  number of the saturated liquid.
- *Pr*SL is the Prandtl
  number of the saturated liquid.
- *ρ*SL is the density of
  the saturated liquid.
- *ρ*SV is the density of
  the saturated vapor.
- *a*= 0.05, *b* = 0.8, and
  *c*= 0.33.

For laminar flows, the Nusselt number is set by the **Laminar flow
Nusselt number** parameter.

For transitional flows, the Nusselt number is a blend between the laminar and
turbulent Nusselt numbers.

**Empirical Nusselt Number Formulation**

When the **Heat transfer coefficient model** parameter is set
to `Colburn equation`, the Nusselt number for the
subcooled liquid and superheated vapor zones is calculated by the empirical the
Colburn equation:

Nu=aRebPrc,

where *a*, *b*, and
*c* are defined in the **Coefficients [a, b, c] for
a\*Re^b\*Pr^c in liquid zone** and **Coefficients [a, b, c]
for a\*Re^b\*Pr^c in vapor zone** parameters.

The Nusselt number for liquid-vapor mixture zones is calculated with the
Cavallini-Zecchin equation, with the coefficients specified in the
**Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone**
parameter.

**Pressure Loss**

The pressure loss due to viscous friction varies depending on flow regime and
configuration. The pressure loss calculation uses the overall density, which is
the total fluid mass divided by the total fluid volume. When the
**Pressure loss model** parameter is
`Correlation for flow inside tubes`, the pressure
loss due to friction depends on the Darcy friction factor.

For turbulent flows, when the Reynolds number is above the **Turbulent
flow lower Reynolds number limit** parameter, the block calculates
the pressure loss due to friction in terms of a calculated Darcy friction
factor. The pressure differential between port **A1** and the
internal node I1 is:

pA1−pI1=fD,Am˙A1|m˙A1|2ρDHACS2(L+LAdd2),

where:

- m˙A1 is the total flow rate
  through port **A1**.
- *fD,A* is the Darcy
  friction factor according to the Haaland correlation. When the
  **Local resistance specification** parameter is
  `Aggregate equivalent length`,

  fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2,

  where
  *ε*R is the value of the
  **Internal surface absolute roughness**
  parameter. The friction factor is dependent on the Reynolds number,
  and the block calculates this value at both ports for each
  liquid.
- *L* is the value of the **Total length of
  each tube** parameter.
- *L*Add is the value of the
  **Aggregate equivalent length of local
  resistances** parameter, which is the equivalent length
  of a tube that introduces the same amount of loss as the sum of the
  losses due to other local resistances in the tube.
- *ACS* is the tube
  cross-sectional area.

The pressure differential between port **B1**
and internal node I1 is:

pB1−pI1=fD,Bm˙B1|m˙B1|2ρDHACS2(L+LAdd2),

where m˙B1 is the total flow rate through port
**B1**.

When the **Local resistance specification** parameter is
`Aggregate equivalent length`, the Darcy friction
factor at port **B1** is:

fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2.

When the **Local resistance specification** parameter is
`Local loss coefficient`, the Darcy friction
factors at ports **A1** and **B1** are

fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)

where *Clocalloss*
is the value of the **Total local loss coefficient** parameter.

For laminar flows, when the Reynolds number is below the **Laminar
flow upper Reynolds number limit** parameter, the block calculates
the pressure loss due to friction in terms of the **Laminar friction
constant for Darcy friction factor** parameter,
*λ*. *λ* is a user-defined parameter when
**Tube cross-section** is
`Generic`. Otherwise, the block calculates the
value internally. The pressure differential between port **A1**
and internal node I1 is:

pA1−pI1=λμm˙A12ρDH2ACS(L+LAdd2),

where *μ* is the fluid dynamic viscosity.
The pressure differential between port **B1** and internal node
I1 is:

pB1−pI1=λμm˙B12ρDH2ACS(L+LAdd2).

For transitional flows, the pressure differential due to viscous friction is a
smoothed blend between the values for laminar and turbulent pressure
losses.

**Empirical Pressure Loss Formulation**

When **Pressure loss model** is set to `Pressure
loss coefficient`, the pressure losses due to viscous friction
are calculated with an empirical pressure loss coefficient,
*ξ*.

The pressure differential between port **A2** and internal
node I2 is:

pA2−pI2=12ξm˙A2|m˙A2|2ρACS2.

The pressure differential between port
**B2** and internal node I2 is:

pB2−pI2=12ξm˙B2|m˙B2|2ρACS2.

### Gas Correlations

**Heat Transfer Coefficient for Flows Inside One or More Tubes**

When the gas **Flow geometry** parameter is set to
`Flow inside one or more tubes`, the Nusselt number
is calculated according to the Gnielinski correlation in the same manner as
two-phase subcooled liquid or superheated vapor.

**Heat Transfer Coefficient for Flows Across a Tube Bank**

When the gas **Flow geometry** parameter is set to
`Flow perpendicular to bank of circular tubes`, the
Nusselt number is calculated based on the Hagen number, Hg, and depends on the
**Tube bank grid arrangement** setting:

Nu={0.404Lq1/3(Re+1Re+1000)0.1,Inline0.404Lq1/3,Staggered

where:

Lq={1.18Pr(4lT/π−DlL)Hg(Re),Inline0.92Pr(4lT/π−DlD)Hg(Re),Staggered with lL≥D0.92Pr(4lTlL/π−D2lLlD)Hg(Re),Staggered with lL<D

- *D* is the **Tube outer
  diameter**.
- *lL* is the
  **Longitudinal tube pitch (along flow
  direction)**, the distance between the tube centers
  along the flow direction. *Flow direction* refers
  to the gas flow.
- *lT* is the
  **Transverse tube pitch (perpendicular to flow
  direction)**, shown in the figure below. The transverse
  pitch is the distance between the centers of the two-phase fluid
  tubing in one row.
- *l*D is the diagonal tube
  spacing, calculated as lD=(lT2)2+lL2.

For more information on calculating the Hagen number, see [3].

The longitudinal and transverse pitch distances are the same for both grid
bank arrangement types.

**Cross-Section of Two-Phase Fluid Tubing with Pitch Measurements**

**Empirical Nusselt Number Formulation**

When the **Heat transfer coefficient model** is set to
`Colburn equation` or when **Flow
geometry** is set to `Generic`, the
Nusselt number is calculated by the empirical the Colburn equation:

Nu=aRebPrc,

where *a*, *b*, and
*c* are the values defined in the **Coefficients
[a, b, c] for a\*Re^b\*Pr^c** parameter.

**Pressure Loss for Flow Inside Tubes**

When the gas **Flow geometry** parameter is `Flow
inside one or more tubes`, the pressure loss is calculated the
same way as for two-phase flows, with the respective Darcy friction factor,
density, mass flow rates, and pipe lengths of the gas side.

**Pressure Loss for Flow Across Tube Banks**

When the gas **Flow geometry** parameter is `Flow
perpendicular to bank of circular tubes`, the Hagen number is
used to calculate the pressure loss due to viscous friction. The pressure
differential between port **A2** and internal node I2 is:

pA2−pI2=12μ2NRρD2Hg(Re),

where:

- *μ* is the fluid dynamic viscosity.
- *NR* is the
  **Number of tube rows along flow direction**.
  This is the number of two-phase fluid tube rows along the gas flow
  direction.

The pressure differential between port **B2**
and internal node I2 is:

pB2−pI2=12μ2NRρD2Hg(Re).

**Empirical Pressure Loss Formulation**

When the **Pressure loss model** parameter is
`Euler number per tube row` or when the
**Flow geometry** parameter is
`Generic`, the pressure loss due to viscous
friction is calculated with a pressure loss coefficient, in terms of the Euler
number, *Eu*:

Eu=ξNR,

where *ξ* is the empirical pressure loss
coefficient.

The pressure differential between port **A2** and internal
node I2 is:

pA2−pI2=12NREum˙A2|m˙A2|2ρACS2.

The pressure differential between port
**B2** and internal node I1 is:

pB2−pI2=12NREum˙B2|m˙B2|2ρACS2.

### Wall Thermal Mass

If you select **Enable wall thermal mass**, the block models the heat
exchanger wall thermal mass, which introduces a delay in the wall's transient
response to changes in temperature or heat flux. If you model thermal mass, the wall
stores heat in its bounds. This heat storage slows the transition between steady
states so that a thermal perturbation on one side does not immediately manifest on
the other side. The lag persists until the heat flow rates from the two sides
balance.

If you select **Enable wall thermal mass**, the wall energy conservation
is

(Mwallcp,wall2)dTwall2Pdt=−Q2P+Q(Mwallcp,wall2)dTwallGdt=−QG−Q

where:

- *Mwall* is the value of the
  **Wall mass** parameter.
- *cp,wall* is the value of the
  **Wall specific heat** parameter.
- *Twall* is the effective wall
  temperature on each side. The block uses this value to model the transient
  response. You cannot measure this value.

The heat transfer to each fluid is

Q2P=C2P(Twall2P−Tin2P)(1−e−NTU2P)QG=CG(TwallG−TinG)(1−e−NTUG)

where:

- *Tin* is the fluid inlet
  temperature on each side.
- *C* is the heat capacity rate for each fluid.

The number of heat transfer units between the fluid and the wall on each side is

NTU2P=U2PA2PC2PNTUG=UGAGCG

where *A* is the wall surface area and
*U* is the heat transfer coefficient.

### Conservation Equations

**Two-Phase Fluid**

The total mass accumulation rate in the two-phase fluid is defined as:

dM2Pdt=m˙A1+m˙B1,

where:

- *M2P* is the total mass of
  the two-phase fluid.
- m˙A1 is the mass flow rate of
  the fluid at port **A1**.
- m˙B1 is the mass flow rate of
  the fluid at port **B1**.

The flow is positive when flowing into the block through the
port.

The energy conservation equation relates the change in specific internal
energy to the heat transfer by the fluid:

M2Pdu2Pdt+u2P(m˙A1+m˙B1)=ϕA1+ϕB1−Q,

where:

- *u*2P is the two-phase
  fluid specific internal energy.
- *φ*A1 is the energy flow
  rate at port **A1**.
- *φ*B1 is the energy flow
  rate at port **B1**.
- *Q* is heat transfer rate, which is positive when
  leaving the two-phase fluid volume.

**Gas**

The total mass accumulation rate in the gas is defined as:

dMGdt=m˙A2+m˙B2.

The energy conservation equation is:

MGduGdt+uG(m˙A2+m˙B2)=ϕA2+ϕB2+Q,

where:

- *ϕ*A2 is the energy flow
  rate at port **A2**.
- *ϕ*B2 is the energy flow
  rate at port **B2**.

The heat transferred to or from the gas, *Q*, is
equal to the heat transferred from or to the two-phase fluid.
