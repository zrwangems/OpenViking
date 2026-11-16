---
type: simulink-block
title: 'Disc Friction Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'discfrictionclutch'
documentation_source_path: 'ref/discfrictionclutch.html'
language: en
---

# Disc Friction Clutch

## Ports

### Input

### **P** — Pressure physical signal

Physical signal input port for the applied pressure between the clutch
plates, in Pascals. The block saturates signals less than zero to
zero.
### Conserving

### **B** — Base mechanical rotational

Rotational conserving port associated with the driving, or base,
shaft.

### **F** — Follower mechanical rotational

Rotational conserving port associated with the driven, or follower,
shaft.

### **H** — Heat flow thermal

Thermal conserving port associated with heat flow.

#### Dependencies

This port is visible only when, in the
**Friction** settings, the **Friction
model** parameter is set to
`Temperature-dependent friction
coefficients` or `Temperature and
velocity-dependent friction coefficients`. For more
information, see Friction Parameter Dependencies
and Friction model.

## Parameters

### Geometry

### **Geometry model** — Geometry parameterization method `Define effective radius` (default) | `Define annular region`

Parameterization method for modeling the clutch friction
geometry.

#### Dependencies

The **Effective torque radius** parameter is
visible only If this parameter is set to `Define
effective radius`:

These parameters are visible only If this parameter is set to
`Define annular region`:

- **Friction surface outside
  diameter**
- **Friction surface inside
  diameter**

### **Effective torque radius** — Moment arm radius `130``mm` (default) | positive scalar

Effective moment arm radius,
*reff*, that determines the
kinetic friction torque inside the clutch.

#### Dependencies

This parameter is visible only if the **Geometry
model** parameter is set to `Define
effective radius`.

### **Friction surface outside diameter** — Friction surface outer diameter `150` `mm` (default) | positive scalar

Diameter, 2*ro*, across the
outer edge of the friction disc annulus.

#### Dependencies

This parameter is visible only if the **Geometry
model** parameter is set to `Define annular
region`.

### **Friction surface inside diameter** — Friction surface inner diameter `100` `mm` (default) | nonnegative scalar

Diameter, 2*ri*, across the
inner edge of the friction disc annulus.

#### Dependencies

This parameter is visible only if the **Geometry
model** parameter is set to `Define annular
region`.

### **Number of friction surfaces** — number of friction surfaces `4` (default) | positive scalar integer

Number, *N*, of friction-generating contact surfaces
inside the clutch.

### **Engagement piston area** — Pressure application area `0.001` `m^2` (default) | positive scalar

Effective area, *A*, of the clutch piston when the
piston is applying pressure across the clutch.

### **Directionality** — Allowable slip directions `Bidirectional` (default) | `Unidirectional`

Slip directions the clutch allows between its plates. A bidirectional
clutch allows positive and negative slip velocities. A unidirectional
clutch allows only positive slip velocities.

The unidirectional clutch is equivalent to a friction clutch connected
in parallel to a one-way clutch that disengages only when the slip
velocity becomes positive. To model a unidirectional clutch with slip in
the negative direction, reverse the base and follower port
connections.

### Friction

The table shows how the visibility of some ports, parameters, and settings depends
on the option that you choose for other parameters.

**Friction Parameter Dependencies**

| **Friction** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **Friction model** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| Exposes:  - Conserving port **H** - **Thermal Port** settings | | Exposes:  - Conserving port **H** - **Thermal Port** settings | |
| - | **Relative velocity vector** | | - | | **Relative velocity vector** | |
| - | - | | **Temperature vector** | | **Temperature vector** | |
| **Static friction coefficient** | **Static friction coefficient** | | **Static friction coefficient vector** | | **Static friction coefficient vector** | |
| **Kinetic friction coefficient** | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient matrix** | |
| - | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | |
| - | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | |
| **De-rating factor** | **De-rating factor** | | **De-rating factor** | | **De-rating factor** | |
| **Clutch velocity tolerance** | **Clutch velocity tolerance** | | **Clutch velocity tolerance** | | **Clutch velocity tolerance** | |
| **Engagement threshold pressure** | **Engagement threshold pressure** | | **Engagement threshold pressure** | | **Engagement threshold pressure** | |

### **Friction model** — Friction model `Fixed kinetic friction coefficient` (default) | `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

Parameterization method to model the kinetic friction coefficient. The
options and default values for this parameter depend on the friction
model that you select for the block. The options are:

- `Fixed kinetic friction
  coefficient` — Provide a fixed value
  for the kinetic friction coefficient.
- `Velocity-dependent kinetic friction
  coefficient` — Define the kinetic
  friction coefficient by one-dimensional table lookup based
  on the relative angular velocity between discs.
- `Temperature-dependent friction
  coefficients` — Define the kinetic
  friction coefficient by table lookup based on the
  temperature.
- `Temperature and velocity-dependent friction
  coefficients` — Define the kinetic
  friction coefficient by table lookup based on the
  temperature and the relative angular velocity between
  discs.

#### Dependencies

The friction model setting affects the visibility of other
parameters, settings, and ports. For more information, see Friction Parameter Dependencies.

### **Relative velocity vector** — Relative velocity `[0, 100, 1000]` `rad/s` (default) | vector

Input values for the relative velocity as a vector. The values in the
vector must increase from left to right. The minimum number of values
depends on the interpolation method that you select. For linear
interpolation, provide at least two values per dimension. For smooth
interpolation, provide at least three values per dimension.

#### Dependencies

This parameter is visible only if the **Friction
model** parameter is set to
`Velocity-dependent kinetic friction
coefficient` or `Temperature and
velocity-dependent friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Temperature vector** — Temperature `[280, 300, 320]` `K` (default) | increasing vector

Input values for the temperature as a vector. The minimum number of
values depends on the interpolation method that you select. For linear
interpolation, provide at least two values per dimension. For smooth
interpolation, provide at least three values per dimension. The values
in the vector must increase from left to right.

#### Dependencies

This parameter is visible only if the **Friction
model** parameter is set to
`Temperature-dependent friction
coefficients` or `Temperature and
velocity-dependent friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Static friction coefficient** — Static friction coefficient `0.35` (default) | positive scalar

Static or peak value of the friction coefficient. The static friction
coefficient must be greater than the kinetic friction
coefficient.

#### Dependencies

This parameter is visible only when the **Friction
model** parameter is set to `Fixed kinetic
friction coefficient` or
`Velocity-dependent kinetic friction
coefficient`. For more information, see Friction Parameter Dependencies.

### **Static friction coefficient vector** — Static friction coefficient `[.4, .38, .36]` (default) | vector

Static, or peak, values of the friction coefficient as a vector. The
vector must have the same number of elements as the temperature vector.
Each value must be greater than the value of the corresponding element
in the kinetic friction coefficient vector.

#### Dependencies

This parameter is visible only if the **Friction
model** parameter is set to
`Temperature-dependent friction
coefficients` or `Temperature and
velocity-dependent friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Kinetic friction coefficient** — Kinetic friction coefficient `0.3` (default) | positive scalar

The kinetic, or Coulomb, friction coefficient. The coefficient must be
greater than zero.

#### Dependencies

This parameter is visible only if the **Friction
model** parameter is set to `Fixed kinetic
friction coefficient`. For more information, see
Friction Parameter Dependencies.

### **Kinetic friction coefficient vector** — Kinetic friction coefficient `[.3, .22, .19]` (default) | `[.3, .28, .25]` | positive vector

Output values for kinetic friction coefficient as a vector. All values
must be greater than zero.

If the **Friction model** parameter is set to

- `Velocity-dependent kinetic friction
  coefficient` — The vector must have
  same number of elements as relative velocity vector.
- `Temperature-dependent friction
  coefficients` — The vector must have
  the same number of elements as the temperature
  vector.

#### Dependencies

This parameter is visible only if the **Friction
model** parameter is set to
`Velocity-dependent kinetic friction
coefficient` or `Temperature-dependent
friction coefficients`. For more information, see
Friction Parameter Dependencies.

### **Kinetic friction coefficient matrix** — Kinetic friction coefficient `[.34, .32, .3; .3, .28, .25; .25, .2, .15]` (default) | positive matrix

Output values for kinetic friction coefficient as a matrix. All the
values must be greater than zero. The size of the matrix must equal the
size of the matrix that is the result of the temperature vector ×
the kinetic friction coefficient relative velocity vector.

#### Dependencies

This parameter is visible only if the **Friction
model** parameter is set to `Temperature
and velocity-dependent friction coefficients`. For
more information, see Friction Parameter Dependencies.

### **Friction coefficient interpolation method** — Extrapolation method `Linear` (default) | `Smooth`

Interpolation method for approximating the output value when the input
value is between two consecutive grid points:

- `Linear` — Select this option
  to get the best performance.
- `Smooth` — Select this option
  to produce a continuous curve with continuous first-order
  derivatives.

For more information on interpolation algorithms, see the PS Lookup Table (1D)
block reference page.

#### Dependencies

This parameter is visible only if the **Friction
model** parameter is set to
`Velocity-dependent kinetic friction
coefficient`, `Temperature-dependent
friction coefficients`, or `Temperature
and velocity-dependent friction coefficients`. For
more information, see Friction Parameter Dependencies.

### **Friction coefficient extrapolation method** — Interpolation method `Linear` (default) | `Nearest` | `Error`

Extrapolation method for determining the output value when the input
value is outside the range specified in the argument list:

- `Linear` — Select this
  option to produce a curve with continuous first-order
  derivatives in the extrapolation region and at the boundary
  with the interpolation region.
- `Nearest` — Select this
  option to produce an extrapolation that does not go above
  the highest point in the data or below the lowest point in
  the data.
- `Error` — Select this
  option to avoid going into the extrapolation mode when you
  want your data to be within the table range. If the input
  signal is outside the range of the table, the simulation
  stops and generates an error.

For more information on extrapolation algorithms, see the PS Lookup Table (1D)
block reference page.

#### Dependencies

This parameter is visible only if the **Friction
model** parameter is set to
`Velocity-dependent kinetic friction
coefficient`, `Temperature-dependent
friction coefficients`, or `Temperature
and velocity-dependent friction coefficients`. For
more information, see Friction Parameter Dependencies.

### **De-rating factor** — De-rating factod `1` (default) | positive scalar

Dimensionless de-rating factor, *D*, that accounts
for clutch disc wear by proportionately reducing clutch friction.

### **Clutch velocity tolerance** — Relative velocity locking threshold `0.001` `rad/s` (default) | nonnegative scalar

Maximum slip velocity at which the clutch can lock. The slip velocity
is the signed difference between the base and follower shaft angular
velocities, that is, w=wF−wB. If the kinetic friction torque is nonzero and the
transferred torque is within the static friction torque limits, then the
clutch locks if the actual slip velocity falls below the velocity
tolerance.

### **Engagement threshold pressure** — Normal contact force threshold `100` `Pa` (default) | nonnegative scalar

Minimum pressure *Pth* at
which the clutch engages. If the pressure input signal falls below this
threshold, the clutch automatically disengages.

### Viscous Losses

### **Viscous friction coefficient** — Viscous friction `0` `N*m/(rad/s)` (default) | nonnegative scalar

Viscous friction coefficient *μ* applied to the
relative slip *ω* between the base and follower
axes.

### Initial Conditions

### **Initial state** — Initial clutch state `Unlocked` (default) | `Locked`

Clutch state at the start of simulation. The clutch can be in one of
two states, locked and unlocked. A locked clutch constrains the base and
follower shafts to spin at the same velocity, that is, as a single unit.
An unlocked clutch allows the two shafts to spin at different
velocities, resulting in slip between the clutch plates.

### Faults

To modify the faults, create a fault and, in the block dialog, click
**Open fault properties**. In the Property Inspector, click the
**Fault behavior** link to open the faults.

### **Friction fault** — Option to model clutch failure `Add fault`

Whether to model a clutch fault in the block. To add a fault, click
the **Add fault** hyperlink.

### **Behavior when faulted** — Clutch fault response `Cannot transmit power` (default) | `Cannot unlock`

Clutch response when a fault is triggered. You can select the clutch
faulting as either:

- `Cannot transmit power`
- `Cannot unlock`

#### Dependencies

To enable this parameter, enable faults for the block by clicking
the **Add fault** hyperlink.

### Thermal Port

**Thermal Port** settings are visible only when, in the
 **Friction** settings, the **Friction model** parameter is set to `Temperature-dependent friction
coefficients` or `Temperature and velocity-dependent
friction coefficients`. For more information, see Friction Parameter Dependencies.

### **Thermal mass** — Thermal mass `50` `kJ/K` (default) | scalar

Thermal energy required to change the component temperature by a
single degree. The greater the thermal mass, the more resistant the
component is to temperature change.

#### Dependencies

This parameter is visible only when, in the **Friction** settings, the **Friction model** parameter is set to `Temperature-dependent
friction coefficients` or `Temperature
and velocity-dependent friction coefficients`. For
more information, see Friction Parameter Dependencies.

### **Initial temperature** — Initial temperature `300` `K` (default) | scalar

Component temperature at the start of simulation. The initial
temperature alters the component efficiency according to an efficiency
vector that you specify, affecting the starting meshing or friction
losses. The default value is `300`
`K`.

#### Dependencies

This parameter is only visible when, in the **Friction** settings, the **Friction model** parameter is set to `Temperature-dependent
friction coefficients` or `Temperature
and velocity-dependent friction coefficients`. For
more information, see Friction Parameter Dependencies.

## Libraries

Simscape / Driveline / Clutches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2025a: Parameter name change

The **Viscous drag torque coefficient** parameter is now the
**Viscous friction coefficient** parameter.

### R2024a: Model faults with the Simscape faults interface

The Disc Friction Clutch block now supports the Simscape faults interface. To learn more,
see Introduction to Simscape Faults.

## Description

Friction clutch with disc plates that engage when plate pressure exceeds threshold

The Disc Friction Clutch block represents a friction
clutch with two flat friction plate sets that come into contact to engage. The clutch
engages when the applied plate pressure exceeds an engagement threshold pressure. Once
engaged, the plates experience frictional torques that enable them to transmit power
between the base and follower driveshafts.

The clutch can be bidirectional or unidirectional. A bidirectional clutch can slip in
the positive and negative directions. A unidirectional clutch can slip only in the
positive direction. The slip direction is positive if the follower shaft spins faster
than the base shaft and negative if it slips slower. The block defines the slip velocity
as the difference

ω=ωF−ωB,

where:

- *ω* is the relative angular velocity or slip
  velocity.
- *ωF* is the angular velocity of
  the follower driveshaft.
- *ωB* is the angular velocity of
  the base driveshaft.

The block provides a physical signal input port **P** for the applied
pressure between the clutch plates. The applied pressure must be greater than or equal
to zero. If the input signal falls below zero, the block treats the plate pressure as
zero.

### Equations

The Disc Friction Clutch block is a simplified
implementation of the Fundamental Friction Clutch block. The
Fundamental Friction Clutch requires the kinetic
and static friction limit torques as input signals. The Disc Friction
Clutch does not require the input data. Instead, the block
calculates the kinetic and static friction from the clutch parameters and the input
pressure signal *P*.

When you apply a pressure signal above threshold, such that the applied pressure
equals or exceeds the pressure threshold, that is, P≥Pth, the block can apply two kinds of friction to the driveline
motion, kinetic and static. The clutch applies kinetic friction torque only when one
driveline axis is spinning relative to the other driveline axis. The clutch applies
static friction torque when the two driveline axes lock and spin together. The block
iterates through multistep testing to determine when to lock and unlock the
clutch.

**Kinetic Friction**

The kinetic friction torque opposes the relative slip and is applied with an
overall minus sign. Mathematically, the kinetic friction is the positive sum of
viscous drag and surface contact friction torques:

τk=μ⋅ω+τcontact.

- *τK* is the kinetic friction
  torque.
- *μ* is the viscous drag coefficient.
- *ω* is the relative angular velocity, or slip
  velocity.
- *τcontact* is the contact
  torque.

The contact friction is a product of six factors such that

τcontact=kK⋅D⋅N⋅reff⋅Pfric⋅A≥0,

where:

- *kK* is the dimensionless
  coefficient of kinetic friction of clutch discs, which is a function
  of *ω*.
- *D* is the clutch de-rating factor.
- *N* is the number of friction surfaces.
- *reff* is the effective
  torque radius, that is, the effective moment arm of clutch friction
  force.
- *Pfric* is the clutch
  friction capacity, such that Pfric=max[(P−Pth),0].
- *A* is the engagement surface area.

You specify the kinetic friction coefficient,
*kK*, as either a constant or a
tabulated discrete function of relative angular velocity *ω*.
The tabulated function is assumed to be symmetric for positive and negative
values of the relative angular velocity. Therefore, specify
*kK* for positive values of
*ω* only.

The clutch applies a normal force from its piston as the product of the clutch
friction capacity, *Pfric*, and
engagement surface area, *A*, on each of *N*
friction surfaces. The pressure signal, *P*, should be
nonnegative. If *P* is less than the pressure threshold.
*Pth*, the clutch applies no
friction at all.

The *effective torque radius*,
*reff*, is the effective moment
arm of clutch friction force, measured from the driveline axis, at which the
kinetic friction forces are applied at the frictional surfaces. It is related to
the geometry of the friction surface by:

reff=23ro3−ri3ro2−ri2,

where, for a friction surface, modeled as an annular disc:

- *ro* is the outer disc
  radius.
- *ri* is the inner disc
  radius.

The *clutch de-rating factor*, *D*,
accounts for clutch wear. For a new clutch, *D* is one. For a
clutch approaching a *uniform wear* state:

D→34(ro+ ​ri)2ro2+rori+ ​ri2.

**Static Friction**

The static friction limit is related to the kinetic friction, setting
*ω* to zero and replacing the kinetic with the static
friction coefficient:

τS=kS⋅D⋅N⋅reff⋅Pfric⋅A≥0.

where:

- *τS* is the static
  friction torque limit, which is the product of the static friction
  peak factor and the kinetic friction torque as *ω*
  approaches 0.
- *kK* is the dimensionless
  coefficient of static friction of clutch discs.
- *D* is the clutch de-rating factor.
- *N* is the number of friction surfaces.
- *reff* is the effective
  torque radius, that is, the effective moment arm of clutch friction
  force.
- *Pfric* is the clutch
  friction capacity, such that Pfric=max[(P−Pth),0].
- *A* is the engagement surface area.

kS>kK, so that the torque *τ* needed across the
clutch to unlock it by overcoming static friction is larger than the kinetic
friction at the instant of unlocking, when ω=0..

The *static friction torque range* or limits are then
defined symmetrically as

τS≡τS+=−τS−.

**Wait State: Locking and Unlocking**

The Wait state of the Disc Friction Clutch is
identical to the Wait state of the Fundamental Friction
Clutch, with the replacement of the positive kinetic
friction condition, τK>0, by the positive clutch friction capacity condition, the
applied pressure equals or exceeds the pressure threshold, that is, P≥Pth.

**Power Dissipated by the Clutch**

The power dissipated by the clutch is the absolute value of the product of
slip velocity, *ω*, and the kinetic friction torque,
*τK*, that is, |ω⋅τK|. The clutch dissipates power only if it is both slipping, ω≠0, and applying kinetic friction, τk>0.

### Velocity-Dependent and Temperature-Dependent Friction Models

**Velocity-Dependent Model**

You can model the effects of rotational velocity change by selecting a
velocity-dependent model. To choose a velocity-dependent model, in the
**Friction** settings, set the **Friction
model** parameter to `Velocity-dependent kinetic
friction coefficient`. For information about a friction model
that depends on both velocity and temperature, see Thermal, Velocity-Dependent Model.

For the velocity-dependent model these related parameters become visible in
the **Friction** settings:

- **Relative velocity vector**
- **Kinetic friction coefficient vector**
- **Friction coefficient interpolation
  method**
- **Friction coefficient extrapolation
  method**

**Thermal Model**

You can model the effects of heat flow and temperature change by selecting a
temperature-dependent model. To choose a temperature-dependent model, in the
**Friction** settings, set the **Friction
model** parameter to `Temperature-dependent friction
coefficients`. For information about a friction model that
depends on both velocity and temperature, see Thermal, Velocity-Dependent Model.

**Thermal, Velocity-Dependent Model**

You can model the effects of rotational velocity change and heat flow by
selecting a velocity-dependent and temperature-dependent model. To choose a
model that depends on both velocity and temperature, in the
**Friction** settings, set the **Friction
model** parameter to `Temperature and
velocity-dependent friction coefficients`.

### Faults

To model a fault in the Disc Friction Clutch block, in the
**Faults** section, click the **Add fault** hyperlink next
to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

You can choose either or both of these settings for block faulting. When you
trigger a fault, the block responds according to the setting of the
**Behavior when faulted** parameter for the remainder of the
simulation. The fault options are:

- `Cannot transmit power`
- `Cannot unlock`
