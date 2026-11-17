---
type: simulink-block
title: 'Heat Exchanger (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'heatexchangertl'
documentation_source_path: 'ref/heatexchangertl.html'
language: en
---

# Heat Exchanger (TL)

## Ports
```yaml
ports:
- name: A1
  summary: Thermal liquid port thermal liquid
  direction: conserving
- name: B1
  summary: Thermal liquid port thermal liquid
  direction: conserving
- name: H2
  summary: Entrance temperature of controlled fluid 2 thermal
  direction: conserving
- name: C2
  summary: Heat capacity rate physical signal
  direction: input
- name: HC2
  summary: Heat transfer coefficient physical signal
  direction: input
```

### Conserving

### **A1** — Thermal liquid port thermal liquid

Opening for thermal liquid to enter and exit its side of the heat
exchanger.

### **B1** — Thermal liquid port thermal liquid

Opening for thermal liquid to enter and exit its side of the heat
exchanger.

### **H2** — Entrance temperature of controlled fluid 2 thermal

Entrance temperature of controlled fluid 2.
### Input

### **C2** — Heat capacity rate physical signal

Instantaneous value of the heat capacity rate for the controlled flow.

### **HC2** — Heat transfer coefficient physical signal

Instantaneous value of the heat transfer coefficient between the controlled flow
and the wall.
## Parameters
```yaml
parameters:
- name: Flow arrangement
  summary: Manner in which the flows align in the heat exchanger Parallel or counter flow (default) | Shell and tube | Cross
    flow | Generic - effectiveness table
  group: Common
- name: Number of shell passes
  summary: Number of times the flow traverses the shell before exiting 1 (default) | unitless scalar
  group: Common
- name: Cross flow type
  summary: Mixing condition in each of the flow channels Both fluids mixed (default) | Both fluids unmixed | Thermal liquid
    mixed & Controlled Fluid unmixed | Thermal liquid unmixed & Controlled Fluid mixed
  group: Common
- name: Number of heat transfer units vector, NTU
  summary: Number of transfer units at each breakpoint in lookup table for heat exchanger effectiveness unitless numerical
    array
  group: Common
- name: Thermal capacity ratio vector, CR
  summary: Thermal capacity ratio at each breakpoint in lookup table for heat exchanger effectiveness unitless numerical array
  group: Common
- name: Effectiveness table, E(NTU,CR)
  summary: Heat exchanger effectiveness at each breakpoint in lookup table over the number of transfer units and thermal capacity
    ratio unitless numerical array
  group: Common
- name: Wall thermal resistance
  summary: Resistance of the wall to heat flow by thermal conduction 0 K/W (default) | scalar with units of temperature over
    power
  group: Common
- name: Enable wall thermal mass
  summary: Option to model wall thermal mass off (default) | on
  group: Common
- name: Wall mass
  summary: Heat exchanger wall mass 1 kg (default) | positive scalar
  group: Common
- name: Wall specific heat
  summary: Heat exchanger wall specific heat 490 J/(K*kg) (default) | positive scalar
  group: Common
- name: Minimum free-flow area
  summary: Cross-sectional area of the flow channel at its narrowest point 0.01 m^2 (default) | scalar with units of length
    squared
  group: Thermal Liquid
- name: Thermal liquid volume
  summary: Total volume of fluid in the thermal liquid flow channel 0.01 m^3 (default) | scalar with units of length squared
  group: Thermal Liquid
- name: Hydraulic diameter for pressure loss
  summary: Effective diameter of the flow channel at its narrowest point 0.1 m (default) | scalar with units of length
  group: Thermal Liquid
- name: Laminar flow upper Reynolds number limit
  summary: Start of transition between laminar and turbulent zones 2000 (default) | unitless scalar
  group: Thermal Liquid
- name: Turbulent flow lower Reynolds number limit
  summary: End of transition between laminar and turbulent zones 4000 (default) | unitless scalar
  group: Thermal Liquid
- name: Pressure loss model
  summary: Mathematical model for pressure loss by viscous friction Pressure loss coefficient (default) | Correlation for
    flow inside tubes | Tabulated data - Darcy friction factor vs. Reynolds number | Tabulated data - Euler number vs. Reynolds
    number
  group: Thermal Liquid
- name: Pressure loss coefficient
  summary: Aggregate loss coefficient for all flow resistances between the ports 0.1 (default) | unitless scalar
  group: Thermal Liquid
- name: Length of flow path from inlet to outlet
  summary: Distance traveled from port to port 1 m (default) | scalar with units of length
  group: Thermal Liquid
- name: Aggregate equivalent length of local resistances
  summary: Aggregate minor pressure loss expressed as a length 0.1 m (default) | scalar with units of length
  group: Thermal Liquid
- name: Internal surface absolute roughness
  summary: Mean height of surface protrusions behind wall friction 15e-6 m (default) | scalar with units of length
  group: Thermal Liquid
- name: Laminar friction constant for Darcy friction factor
  summary: Pressure loss correction for flow cross section in laminar flow conditions 64 (default) | unitless scalar
  group: Thermal Liquid
- name: Reynolds number vector for Darcy friction factor
  summary: Reynolds number at each breakpoint in lookup table for Darcy friction factor unitless numerical array
  group: Thermal Liquid
- name: Darcy friction factor vector
  summary: Darcy friction factor at each breakpoint in lookup table over Reynolds number unitless numerical array
  group: Thermal Liquid
- name: Reynolds number vector for Euler number
  summary: Reynolds number at each breakpoint in lookup table for Euler number unitless numerical array
  group: Thermal Liquid
- name: Euler number vector
  summary: Euler number at each breakpoint in lookup table over Reynolds number unitless numerical array
  group: Thermal Liquid
- name: Heat transfer coefficient model
  summary: Mathematical model for heat transfer between fluid and wall Constant heat transfer coefficient (default) | Correlation
    for flow inside tubes | Tabulated data - Colburn factor vs. Reynolds number | Tabulated data - Nusselt number vs. Reynolds
    number and Prandtl number
  group: Thermal Liquid
- name: Heat transfer surface area
  summary: Effective surface area used in heat transfer between fluid and wall 0.4 m^2 (default) | scalar with units of length
    squared
  group: Thermal Liquid
- name: Liquid-wall heat transfer coefficient
  summary: Heat transfer coefficient for convection between fluid and wall 100 W/(K*m^2) (default) | scalar
  group: Thermal Liquid
- name: Length of flow path for heat transfer
  summary: Characteristic length traversed in heat transfer between fluid and wall 1 m (default) | scalar with units of length
  group: Thermal Liquid
- name: Nusselt number for laminar flow heat transfer
  summary: Constant assumed for Nusselt number in laminar flow 3.66 (default) | positive unitless scalar
  group: Thermal Liquid
- name: Reynolds number vector for Colburn factor
  summary: Values of the Reynolds number at which to specify the Colburn factor data unitless numerical array
  group: Thermal Liquid
- name: Colburn factor vector
  summary: Colburn factor at each breakpoint in lookup table over Reynolds number unitless numerical array
  group: Thermal Liquid
- name: Reynolds number vector for Nusselt number
  summary: Reynolds number at each breakpoint in lookup table for Nusselt number unitless numerical array
  group: Thermal Liquid
- name: Prandtl number vector for Nusselt number
  summary: Prandtl number at each breakpoint in lookup table for Nusselt number unitless numerical array
  group: Thermal Liquid
- name: Nusselt number table, Nu (Re,Pr)
  summary: Nusselt number at each breakpoint in lookup table over Reynolds and Prandtl numbers unitless numerical array
  group: Thermal Liquid
- name: Fouling factor
  summary: Measure of thermal resistance due to fouling deposits 1e-4 K*m^2/W (default) | scalar with units of temperature
    over power
  group: Thermal Liquid
- name: Minimum liquid-wall heat transfer coefficient
  summary: Lower bound for the heat transfer coefficient 1 W/(m^2 * K) (default) | scalar with units of power/area/temperature
  group: Thermal Liquid
- name: Heat transfer surface area
  summary: Aggregate heat transfer surface area on the controlled fluid side 0.4 m^2 (default) | scalar with units of length
    squared
  group: Controlled Fluid
- name: Fouling factor
  summary: Measure of thermal resistance due to fouling deposits 1e-4 K*m^2/W (default) | scalar with units of length squared
    times temperature over power
  group: Controlled Fluid
- name: Minimum fluid-wall heat transfer coefficient
  summary: Lower bound for the heat transfer coefficient 1 W/(m^2 * K) (default) | scalar with units of power/area/temperature
  group: Controlled Fluid
- name: Enable Thermal Liquid dynamic compressibility
  summary: Setting for liquid compressibility in heat exchanger On (default) | Off | scalar
  group: Effects and Initial Conditions
- name: Thermal Liquid nominal temperature
  summary: Temperature at nominal operating conditions 293.15 K (default) | scalar
  group: Effects and Initial Conditions
- name: Thermal Liquid nominal pressure
  summary: Pressure at nominal operating conditions 0.101325 MPa (default) | scalar
  group: Effects and Initial Conditions
- name: Thermal Liquid initial temperature
  summary: Temperature in the thermal liquid channel at the start of simulation 293.15 K (default) | scalar with units of
    temperature
  group: Effects and Initial Conditions
- name: Thermal Liquid initial pressure
  summary: Pressure in the thermal liquid channel at the start of simulation 0.101325 MPa (default) | scalar with units of
    pressure
  group: Effects and Initial Conditions
```

### Common

### **Flow arrangement** — Manner in which the flows align in the heat exchanger `Parallel or counter flow` (default) | `Shell and tube` | `Cross flow` | `Generic - effectiveness table`

Manner in which the flows align in the heat exchanger. The flows can run parallel
to each other, counter to each other, or across each other. They can also run in a
pressurized shell, one through tubes enclosed in the shell, the other around those
tubes. Other flow arrangements are possible through a generic parameterization based
on tabulated effectiveness data and requiring little detail about the heat
exchanger.

### **Number of shell passes** — Number of times the flow traverses the shell before exiting `1` (default) | unitless scalar

Number of times the flow traverses the shell before exiting.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Shell and tube`.

### **Cross flow type** — Mixing condition in each of the flow channels `Both fluids mixed` (default) | `Both fluids unmixed` | `Thermal liquid mixed & Controlled Fluid unmixed` | `Thermal liquid unmixed & Controlled Fluid mixed`

Mixing condition in each of the flow channels. Mixing in this context is the
lateral movement of fluid as it proceeds along its flow channel toward the outlet. The
flows remain separate from each other. Unmixed flows are common in channels with
plates, baffles, or fins. This setting reflects in the effectiveness of the heat
exchanger, with unmixed flows being most effective and mixed flows being least.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Shell and tube`.

### **Number of heat transfer units vector, NTU** — Number of transfer units at each breakpoint in lookup table for heat exchanger effectiveness unitless numerical array

Number of transfer units at each breakpoint in the lookup table for the heat
exchanger effectiveness number. The table is two-way, with both the number of transfer
units and the thermal capacity ratio serving as independent coordinates. The block
inter- and extrapolates the breakpoints to obtain the effectiveness at any number of
transfer units. Interpolation is `linear` and extrapolation is
`nearest`.

The numbers specified must be greater than zero and increase monotonically from
left to right. The size of the vector must equal the number of rows in the
**Effectiveness table** parameter. If the table has
*m* rows and *n* columns, the vector for the
number of transfer units must be *m* elements long.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Generic - effectiveness table`.

### **Thermal capacity ratio vector, CR** — Thermal capacity ratio at each breakpoint in lookup table for heat exchanger effectiveness unitless numerical array

Thermal capacity ratio at each breakpoint in lookup table for heat exchanger
effectiveness. The table is two-way, with both the number of transfer units and the
heat capacity rate ratio serving as independent coordinates. The block inter- and
extrapolates the breakpoints to obtain the effectiveness at any thermal capacity
ratio. Interpolation is `linear` and extrapolation is
`nearest`.

The thermal capacity ratios must be greater than zero and increase monotonically
from left to right. The size of the vector must equal the number of columns in the
**Nusselt number table** parameter. If the table has
*m* rows and *n* columns, the vector for the
thermal capacity ratio must be *n* elements long. The thermal
capacity ratio is the fraction of minimum over maximum heat capacity rates.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Generic - effectiveness table`.

### **Effectiveness table, E(NTU,CR)** — Heat exchanger effectiveness at each breakpoint in lookup table over the number of transfer units and thermal capacity ratio unitless numerical array

Heat exchanger effectiveness at each breakpoint in its lookup table over the
number of transfer units and thermal capacity ratio. The block inter- and extrapolates
the breakpoints to obtain the effectiveness at any pair of number of transfer units
and thermal capacity ratio. Interpolation is `linear` and
extrapolation is `nearest`.

The effectiveness values must be not be negative. They must align from top to
bottom in order of increasing number of transfer units and from left to right in order
of increasing thermal capacity ratio. The number of rows must equal the size of the
**Number of heat transfer units vector** parameter, and the number
of columns must equal the size of the **Thermal capacity ratio
vector** parameter.

#### Dependencies

To enable this parameter, set **Flow arrangement** to
`Generic - effectiveness table`.

### **Wall thermal resistance** — Resistance of the wall to heat flow by thermal conduction `0 K/W` (default) | scalar with units of temperature over power

Resistance of the wall to heat flow by thermal conduction, and the inverse of
thermal conductance, or the product of thermal conductivity with the ratio of surface
area to length. Wall resistance adds to convective and fouling resistances to
determine the overall heat transfer coefficient between the flows.

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

### Thermal Liquid

### **Minimum free-flow area** — Cross-sectional area of the flow channel at its narrowest point `0.01 m^2` (default) | scalar with units of length squared

Smallest total cross-sectional flow area between inlet and outlet. If the channel
is a collection of ducts, tubes, slots, or grooves, the value of this parameter is the
sum of the smallest areas at the minimum flow area point. This parameter is the area
where the fluid velocity is highest. For example, if the fluid flows perpendicular to
a bank of tubes, the value of this parameter is the sum of the gaps between the tubes
in one cross-section where the sum of the gaps is smallest is smallest.

### **Thermal liquid volume** — Total volume of fluid in the thermal liquid flow channel `0.01 m^3` (default) | scalar with units of length squared

Total volume of fluid contained in the thermal liquid flow channel.

### **Hydraulic diameter for pressure loss** — Effective diameter of the flow channel at its narrowest point `0.1 m` (default) | scalar with units of length

Effective inner diameter of the flow at its narrowest point. For channels not
circular in cross section, that diameter is of an imaginary circle equal in area to
the flow cross section. Its value is the ratio of the minimum free-flow area to a
fourth of its gross perimeter.

If the channel is a collection of ducts, tubes, slots, or grooves, the gross
perimeter is the sum of the perimeters in the collection. If the channel is a single
pipe or tube and it is circular in cross section, the hydraulic diameter is the same
as the true diameter.

### **Laminar flow upper Reynolds number limit** — Start of transition between laminar and turbulent zones `2000` (default) | unitless scalar

Start of transition between laminar and turbulent zones. Above this number,
inertial forces take hold and the flow grows progressively turbulent. The default
value is characteristic of circular pipes and tubes with smooth surfaces.

### **Turbulent flow lower Reynolds number limit** — End of transition between laminar and turbulent zones `4000` (default) | unitless scalar

End of transition between laminar and turbulent zones. Below this number, viscous
forces take hold and the flow grows progressively laminar. The default value is
characteristic of circular pipes and tubes with smooth surfaces.

### **Pressure loss model** — Mathematical model for pressure loss by viscous friction `Pressure loss coefficient` (default) | `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

Mathematical model for pressure loss by viscous friction. This setting determines
which expressions to use for calculation and which block parameters to specify as
input. See the Heat Exchanger Interface (TL) block
for the calculations by parameterization.

### **Pressure loss coefficient** — Aggregate loss coefficient for all flow resistances between the ports `0.1` (default) | unitless scalar

Aggregate loss coefficient for all flow resistances in the flow channel including
the wall friction responsible for major loss and the local resistances, due to bends,
elbows, and other geometry changes, responsible for minor loss.

The loss coefficient is an empirical dimensionless number commonly used to express
the pressure loss due to viscous friction. It can be calculated from experimental data
or, in some cases, obtained from product data sheets.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Pressure loss coefficient`.

### **Length of flow path from inlet to outlet** — Distance traveled from port to port `1 m` (default) | scalar with units of length

Total distance the flow must travel to reach across the ports. In multi-pass
shell-and-tube exchangers, the total distance is the sum over all shell passes. In
tube bundles, corrugated plates, and other channels in which the flow is split into
parallel branches, it is the distance covered in a single branch. The longer the flow
path, the steeper the major pressure loss due to viscous friction at the wall.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Correlation for flow inside tubes` or
`Tabulated data - Darcy friction factor vs Reynolds
number`.

### **Aggregate equivalent length of local resistances** — Aggregate minor pressure loss expressed as a length `0.1 m` (default) | scalar with units of length

Aggregate minor pressure loss expressed as a length. This length is that which all
local resistances, such as elbows, tees, and unions, would add to the flow path if in
their place was a simple wall extension. The larger the equivalent length, the steeper
the minor pressure loss due to the local resistances.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Correlation for flow inside tubes`.

### **Internal surface absolute roughness** — Mean height of surface protrusions behind wall friction `15e-6 m` (default) | scalar with units of length

Mean height of the surface protrusions from which wall friction arises. Higher
protrusions mean a rougher wall for more friction and so a steeper pressure loss.
Surface roughness features in the Haaland correlation from which the Darcy friction
factor derives and on which the pressure loss calculation depends.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Correlation for flow inside tubes`.

### **Laminar friction constant for Darcy friction factor** — Pressure loss correction for flow cross section in laminar flow conditions `64` (default) | unitless scalar

Pressure loss correction for flow cross section in laminar flow conditions. This
parameter is commonly referred to as the shape factor. Its ratio to the Reynolds
number gives the Darcy friction factor for the pressure loss calculation in the
laminar zone. The default value belongs to cylindrical pipes and tubes.

The shape factor derives for certain shapes from the solution of the Navier-Stokes
equations. A square duct has a shape factor of `56`, a rectangular
duct with aspect ratio of 2:1 has a shape factor of `62`, and an
annular tube has a shape factor of `96`, as does a slender conduit
between parallel plates.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Correlation for flow inside tubes`.

### **Reynolds number vector for Darcy friction factor** — Reynolds number at each breakpoint in lookup table for Darcy friction factor unitless numerical array

Reynolds number at each breakpoint in the lookup table for the Darcy friction
factor. The block inter- and extrapolates the breakpoints to obtain the Darcy friction
factor at any Reynolds number. Interpolation is `linear` and
extrapolation is `nearest`.

The Reynolds numbers must be greater than zero and increase monotonically from
left to right. They can span across laminar, transient, and turbulent zones. Their
number must equal the size of the **Darcy friction factor vector**
parameter, with which they are to combine to complete the tabulated
breakpoints.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Tabulated data - Darcy friction factor vs. Reynolds
number`.

### **Darcy friction factor vector** — Darcy friction factor at each breakpoint in lookup table over Reynolds number unitless numerical array

Darcy friction factor at each breakpoint in its lookup table over the Reynolds
number. The block inter- and extrapolates the breakpoints to obtain the Darcy friction
factor at any Reynolds number. Interpolation is `linear` and
extrapolation is `nearest`.

The Darcy friction factors must not be negative and they must align from left to
right in order of increasing Reynolds number. Their number must equal the size of the
**Reynolds number vector for Darcy friction factor** parameter,
with which they are to combine to complete the tabulated breakpoints.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Tabulated data - Darcy friction factor vs. Reynolds
number`.

### **Reynolds number vector for Euler number** — Reynolds number at each breakpoint in lookup table for Euler number unitless numerical array

Reynolds number at each breakpoint in the lookup table for the Euler number. The
block inter- and extrapolates the breakpoints to obtain the Euler number at any
Reynolds number. Interpolation is `linear` and extrapolation is
`nearest`.

The Reynolds numbers must be greater than zero and increase monotonically from
left to right. They can span across laminar, transient, and turbulent zones. Their
number must equal the size of the **Euler number vector** parameter,
with which they are to combine to complete the tabulated breakpoints.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Tabulated data - Euler number vs. Reynolds
number`.

### **Euler number vector** — Euler number at each breakpoint in lookup table over Reynolds number unitless numerical array

Euler number at each breakpoint in its lookup table over the Reynolds number. The
block inter- and extrapolates the breakpoints to obtain the Euler number at any
Reynolds number. Interpolation is `linear` and extrapolation is
`nearest`.

The Euler numbers must not be negative and they must align from left to right in
order of increasing Reynolds number. Their number must equal the size of the
**Reynolds number vector for Euler number** parameter, with which
they are to combine to complete the tabulated breakpoints.

#### Dependencies

To enable this parameter, set **Pressure loss model** to
`Tabulated data - Euler number vs. Reynolds
number`.

### **Heat transfer coefficient model** — Mathematical model for heat transfer between fluid and wall `Constant heat transfer coefficient` (default) | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

Mathematical model for heat transfer between fluid and wall. The choice of model
determines which expressions to apply and which parameters to specify for heat
transfer calculation. See the E-NTU Heat Transfer block for the calculations by
parameterization.

### **Heat transfer surface area** — Effective surface area used in heat transfer between fluid and wall `0.4 m^2` (default) | scalar with units of length squared

Effective surface area used in heat transfer between fluid and wall. The effective
surface area is the sum of primary and secondary surface areas, or those of the wall,
where it is exposed to fluid, and of the fins, if any are used. Fin surface area is
normally scaled by a fin efficiency factor.

### **Liquid-wall heat transfer coefficient** — Heat transfer coefficient for convection between fluid and wall `100 W/(K*m^2)` (default) | scalar

Heat transfer coefficient for convection between fluid and wall. Resistance due to
fouling is captured separately in the **Fouling factor** parameter.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Constant heat transfer
coefficient`.

### **Length of flow path for heat transfer** — Characteristic length traversed in heat transfer between fluid and wall `1 m` (default) | scalar with units of length

Characteristic length traversed in heat transfer between fluid and wall. This
length factors in the calculation of the hydraulic diameter from which the heat
transfer coefficient and the Reynolds number, as defined in the tabulated heat
transfer parameterizations, derives.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Tabulated data - Colburn factor vs. Reynolds
number` or `Tabulated data - Nusselt number vs. Reynolds
number and Prandtl number`.

### **Nusselt number for laminar flow heat transfer** — Constant assumed for Nusselt number in laminar flow `3.66` (default) | positive unitless scalar

Constant assumed for Nusselt number in laminar flow. The Nusselt number factors in
the calculation of the heat transfer coefficient between fluid and wall, on which the
heat transfer rate depends. The default value belongs to cylindrical pipes and tubes.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Correlation for flow inside
tubes`.

### **Reynolds number vector for Colburn factor** — Values of the Reynolds number at which to specify the Colburn factor data unitless numerical array

Reynolds number at each breakpoint in the lookup table for the Colburn factor. The
block inter- and extrapolates the breakpoints to obtain the Colburn factor at any
Reynolds number. Interpolation is `linear` and extrapolation is
`nearest`.

The Reynolds numbers must be greater than zero and increase monotonically from
left to right. They can span across laminar, transient, and turbulent zones. Their
number must equal the size of the **Colburn factor vector**
parameter, with which they are to combine to complete the tabulated
breakpoints.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Tabulated data - Colburn factor vs. Reynolds
number`.

### **Colburn factor vector** — Colburn factor at each breakpoint in lookup table over Reynolds number unitless numerical array

Colburn factor at each breakpoint in its lookup table over the Reynolds number.
The block inter- and extrapolates the breakpoints to obtain the Euler number at any
Reynolds number. Interpolation is `linear` and extrapolation is
`nearest`.

The Colburn factors must not be negative and they must align from left to right in
order of increasing Reynolds number. Their number must equal the size of the
**Reynolds number vector for Colburn factor** parameter, with which
they are to combine to complete the tabulated breakpoints.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Tabulated data - Colburn factor vs. Reynolds
number`.

### **Reynolds number vector for Nusselt number** — Reynolds number at each breakpoint in lookup table for Nusselt number unitless numerical array

Reynolds number at each breakpoint in the lookup table for the Nusselt number. The
table is two-way, with both Reynolds and Prandtl numbers serving as independent
coordinates. The block inter- and extrapolates the breakpoints to obtain the Nusselt
number at any Reynolds number. Interpolation is `linear` and
extrapolation is `nearest`.

The Reynolds numbers must be greater than zero and increase monotonically from
left to right. They can span across laminar, transient, and turbulent zones. The size
of the vector must equal the number of rows in the **Nusselt number
table** parameter. If the table has *m* rows and
*n* columns, the Reynolds number vector must be
*m* elements long.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Tabulated data - Nusselt number vs. Reynolds
number and Prandtl number`.

### **Prandtl number vector for Nusselt number** — Prandtl number at each breakpoint in lookup table for Nusselt number unitless numerical array

Prandtl number at each breakpoint in the lookup table for the Nusselt number. The
table is two-way, with both Reynolds and Prandtl numbers serving as independent
coordinates. The block inter- and extrapolates the breakpoints to obtain the Nusselt
number at any Prandtl number. Interpolation is `linear` and
extrapolation is `nearest`.

The Prandtl numbers must be greater than zero and increase monotonically from left
to right. They can span across laminar, transient, and turbulent zones. The size of
the vector must equal the number of columns in the **Nusselt number
table** parameter. If the table has *m* rows and
*n* columns, the Prandtl number vector must be *n*
elements long.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Tabulated data - Nusselt number vs. Reynolds
number and Prandtl number`.

### **Nusselt number table, Nu (Re,Pr)** — Nusselt number at each breakpoint in lookup table over Reynolds and Prandtl numbers unitless numerical array

Nusselt number at each breakpoint in its lookup table over the Reynolds and
Prandtl numbers. The block inter- and extrapolates the breakpoints to obtain the
Nusselt number at any pair of Reynolds and Prandtl numbers. Interpolation is
`linear` and extrapolation is `nearest`. By
determining the Nusselt number, the table feeds the calculation from which the heat
transfer coefficient between fluid and wall derives.

The Nusselt numbers must be greater than zero. They must align from top to bottom
in order of increasing Reynolds number and from left to right in order of increasing
Prandtl numbers. The number of rows must equal the size of the **Reynolds
number vector for Nusselt number** parameter, and the number of columns
must equal the size of the **Prandtl number vector for Nusselt
number** parameter.

#### Dependencies

To enable this parameter, set **Heat transfer coefficient
model** to `Tabulated data - Nusselt number vs. Reynolds
number and Prandtl number`.

### **Fouling factor** — Measure of thermal resistance due to fouling deposits `1e-4 K*m^2/W` (default) | scalar with units of temperature over power

Measure of thermal resistance due to fouling deposits which over time tend to
build on the exposed surfaces of the wall. The deposits, as they impose between the
fluid and wall a new solid layer through which heat must traverse, add to the heat
transfer path an extra thermal resistance. Fouling deposits grow slowly and the
resistance due to them is accordingly assumed constant during simulation.

### **Minimum liquid-wall heat transfer coefficient** — Lower bound for the heat transfer coefficient `1 W/(m^2 * K)` (default) | scalar with units of power/area/temperature

Lower bound for the heat transfer coefficient between fluid and wall. If
calculation returns a lower heat transfer coefficient, this bound replaces the
calculated value.

### Controlled Fluid

### **Heat transfer surface area** — Aggregate heat transfer surface area on the controlled fluid side `0.4 m^2` (default) | scalar with units of length squared

Aggregate heat transfer surface area on the controlled fluid side

### **Fouling factor** — Measure of thermal resistance due to fouling deposits `1e-4 K*m^2/W` (default) | scalar with units of length squared times temperature over power

Measure of thermal resistance due to fouling deposits which over time tend to
build on the exposed surfaces of the wall. The deposits, as they impose between the
controlled fluid and wall a new solid layer through which heat must traverse, add to
the heat transfer path an extra thermal resistance. Fouling deposits grow slowly and
the resistance due to them is accordingly assumed constant during simulation.

### **Minimum fluid-wall heat transfer coefficient** — Lower bound for the heat transfer coefficient `1 W/(m^2 * K)` (default) | scalar with units of power/area/temperature

Lower bound for the heat transfer coefficient between the controlled fluid and
wall. If calculation returns a lower heat transfer coefficient, this bound replaces
the calculated value.

### Effects and Initial Conditions

### **Enable Thermal Liquid dynamic compressibility** — Setting for liquid compressibility in heat exchanger `On` (default) | `Off` | scalar

Option to model the pressure dynamics inside the heat exchanger. Setting this
parameter to `Off` removes the pressure derivative terms from
the component energy and mass conservation equations. The pressure inside the heat
exchanger is then reduced to the weighted average of the two port pressures.

### **Thermal Liquid nominal temperature** — Temperature at nominal operating conditions `293.15 K` (default) | scalar

Thermal liquid temperature at nominal operating conditions. The block uses this
value to calculate the nominal density to use in the mass and energy conservation
equation when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable Thermal Liquid dynamic
compressibility** checkbox.

### **Thermal Liquid nominal pressure** — Pressure at nominal operating conditions `0.101325 MPa` (default) | scalar

Thermal liquid pressure at nominal operating conditions. The block uses this value
to calculate the nominal density to use in the mass and energy conservation equation
when dynamic compressibility is disabled.

#### Dependencies

To enable this parameter, clear the **Enable Thermal Liquid dynamic
compressibility** checkbox.

### **Thermal Liquid initial temperature** — Temperature in the thermal liquid channel at the start of simulation `293.15 K` (default) | scalar with units of temperature

Temperature in the thermal liquid channel at the start of simulation

### **Thermal Liquid initial pressure** — Pressure in the thermal liquid channel at the start of simulation `0.101325 MPa` (default) | scalar with units of pressure

Pressure in the thermal liquid channel at the start of simulation.

#### Dependencies

To enable this parameter, select **Enable Thermal Liquid dynamic
compressibility** .
## Libraries

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016a**

### R2025a: Model thermal mass of heat exchanger wall

Select **Wall thermal dynamics** to model the thermal mass of the heat
exchanger wall.

### R2024a: Heat Exchanger (TL) block only models E-NTU modeling option

The **Modeling option** parameter has been removed, and the modeling
options are now two separate blocks. The Heat Exchanger (TL) block uses the
heat transfer model that was previously used when **Modeling option** was
`E-NTU Model`. To use the block model used when
**Modeling option** was `Simple model`, see the
Specific Dissipation Heat
Exchanger (TL) block.

## Description

Heat exchanger for systems with thermal liquid and controlled flows

The Heat Exchanger (TL) block models the cooling and
heating of fluids through conduction over a thin wall. The properties of a single-phase
thermal liquid are defined on the **Thermal Liquid** tab. The second fluid is
a controlled fluid, which is specified only by the user-defined parameters on the
**Controlled Fluid** tab. It does not receive any properties from the
domain fluid network. The heat exchange between the fluids is based on the thermal liquid
sensible heat.

### Heat Transfer Model

The block heat transfer model derives from the Effectiveness-NTU method. The
steady-state heat transfer is determined based on a coefficient relating ideal to real
losses in the system:

Q=ϵ QMax,

where

- *Q* the actual heat transfer rate.
- *Q*Max is the ideal heat transfer
  rate.
- *ε* is the heat exchanger effectiveness, which is based on the
  ratio of heat capacity rates, CMinCMax, and the exchanger Number of Transfer Units:

  NTU=1RCMin,

  where *R* is the overall thermal resistance, which
  is discussed in Thermal Resistance below.
  *C*Min is the lesser heat capacity rate of
  the two fluids and *C*Max is the greater heat
  capacity rate of the two fluids. The heat capacity rate is calculated as C=cpm˙.

Additionally, the exchanger effectiveness depends on the number of passes between the
fluids and the fluid mixing conditions. For a list of the effectiveness expressions, see
the E-NTU Heat Transfer block. Connect an
E-NTU Heat Transfer block to a Heat
Exchanger (TL) block to specify the heat transfer properties in with the E-NTU method.

The fluid properties that the block uses in heat transfer calculations are the average between the value at the inlet and the value in the fluid volume.

### Flow Arrangement

Use the **Flow arrangement** parameter to define the flow
configuration in terms of pipe orientation or effectiveness tables. When using the
shell-and-tube configuration, you can select the number of passes in the exchanger. A
multi-pass exchanger resembles the image below.

A single-pass exchanger resembles the image below.

Other flow arrangements are possible through a generic parameterization by tabulated
effectiveness data. This table does not require specific heat exchanger configuration
details, such as flow arrangement, mixing, and passes, for modeling the heat transfer
between the fluids.

### Mixing Condition

Use the **Cross flow type** parameter to model flows that are not
restricted by baffles or walls, which homogenizes fluid temperature along the direction of
flow of the second fluid and varies perpendicular to the second fluid flow. Unmixed flows
vary in temperature both along and perpendicular to the flow direction of the second
fluid. An example of a heat exchanger with one mixed and one unmixed fluid resembles the
configuration below.

A heat exchanger with two unmixed fluids resembles the configuration below.

In counter and parallel flow arrangements, longitudinal temperature variation in one
fluid results in a longitudinal change in temperature variation in the second fluid and
mixing is not taken into account.

### Effectiveness Curves

Shell-and-tube exchangers with multiple passes (**iv.b**-**e** in the figure for 2, 3, and 4
passes) are the most effective type of heat exchanger. For single-pass heat exchangers,
the counter-flow configuration (**ii**) is the most
effective, and parallel flow (**i**) is the least.

Cross-flow exchangers are intermediate in effectiveness, with mixing condition playing
a factor. They are most effective when both flows are unmixed (**iii.a**) and least effective when both flows are mixed (**iii.b**). Mixing just the flow with the smallest heat capacity rate (**iii.c**) lowers the effectiveness more than mixing just the flow
with the largest heat capacity rate (**iii.d**).

### Thermal Resistance

The overall thermal resistance, *R*, is the sum of the local
resistances to heat transfer due to convection, conduction, and fouling along the heat
exchanger walls.

R=1U1A1+F1A1+RW+F2A2+1U2A2,

where:

- *U*1 is the heat transfer coefficient
  between the thermal liquid and the wall.
- *U*2 is the heat transfer coefficient
  between the controlled fluid and the wall, which is received as a physical signal at
  port **HC2**.
- *F*1 is the thermal liquid
  **Fouling factor**.
- *F*2 is the controlled fluid
  **Fouling factor**.
- *A*1 is the thermal liquid **Heat
  transfer surface area**.
- *A*2 is the controlled fluid
  **Heat transfer surface area**.
- *R*W is the **Wall thermal
  resistance**.

The heat transfer coefficients depend on the heat exchanger configuration and fluid
properties. See the E-NTU Heat Transfer reference page for more information.

### Wall Thermal Mass

If you select **Enable wall thermal mass**, the block models the heat
exchanger wall thermal mass, which introduces a delay in the wall's transient response to
changes in temperature or heat flux. If you model thermal mass, the wall stores heat in its
bounds. This heat storage slows the transition between steady states so that a thermal
perturbation on one side does not immediately manifest on the other side. The lag persists
until the heat flow rates from the two sides balance.

If you select **Enable wall thermal mass**, the wall energy conservation is

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

where:

- *Mwall* is the value of the **Wall
  mass** parameter.
- *cp,wall* is the value of the
  **Wall specific heat** parameter.
- *Twall* is the effective wall temperature
  on each side. The block uses this value to model the transient response. You cannot
  measure this value.

The heat transfer to each fluid is

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

where:

- *Tin* is the fluid inlet temperature on each side.
- *C* is the heat capacity rate for each fluid.

The number of heat transfer units between the fluid and the wall on each side is

NTU1=U1A1C1NTU2=U2A2C2

where *A* is the wall surface area and *U* is the heat transfer coefficient.

### Composite Structure

When the Heat Exchanger (TL) block is a composite of the Heat
Exchanger Interface (TL) and E-NTU
Heat Transfer blocks:
