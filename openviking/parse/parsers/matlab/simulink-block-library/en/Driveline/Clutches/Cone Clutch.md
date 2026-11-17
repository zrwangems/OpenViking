---
type: simulink-block
title: 'Cone Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'coneclutch'
documentation_source_path: 'ref/coneclutch.html'
language: en
---

# Cone Clutch

## Ports
```yaml
ports:
- name: N
  summary: Normal force physical signal
  direction: input
- name: X
  summary: Shift linkage position physical signal
  direction: output
- name: B
  summary: Base mechanical rotational
  direction: conserving
- name: F
  summary: Follower mechanical rotational
  direction: conserving
- name: H
  summary: Heat flow thermal
  direction: conserving
- name: S
  summary: Shift linkage mechanical rotational
  direction: conserving
```

### Input

### **N** — Normal force physical signal

Physical signal port associated with the
normal force. This signal is positive or zero. A
signal of less than zero is interpreted as
zero.

#### Dependencies

This port is visible only if, in the
**Geometry** settings, the
**Shift linkage control**
parameter is set to `Physical
signal`. For more information, see
Shift linkage control and Geometry Parameter Dependencies.
### Output

### **X** — Shift linkage position physical signal

Physical signal port associated with shift
linkage position.

#### Dependencies

This port is visible only when, in the
**Geometry** settings, the
**Shift linkage control**
parameter is set to `Conserving
port`. For more information, see
Shift linkage control and Geometry Parameter Dependencies.
### Conserving

### **B** — Base mechanical rotational

Mechanical rotational conserving port
associated with the driving (base) shaft. The
clutch motion is measured as the
*slip*
*ω* =
*ωF*–
*ωB*, the angular velocity of
follower relative to base.

### **F** — Follower mechanical rotational

Mechanical rotational conserving port
associated with the driven or follower
shaft

### **H** — Heat flow thermal

Thermal conserving port associated with heat
flow.

#### Dependencies

This port is visible only when, in the
**Friction** settings, the
**Friction model** parameter is
set to `Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction model and Friction Parameter Dependencies.

### **S** — Shift linkage mechanical rotational

Mechanical rotational conserving port
associated with shift linkage.

#### Dependencies

This port is visible only when, in the
**Geometry** settings, the
**Shift linkage control**
parameter is set to `Conserving
port`. For more information, see
Shift linkage control and Geometry Parameter Dependencies.
## Parameters
```yaml
parameters:
- name: Contact surface maximum diameter
  summary: Outer diameter 150 mm (default) | positive scalar
  group: Geometry
- name: Contact surface minimum diameter
  summary: Inner diameter 100 mm (default) | positive scalar
  group: Geometry
- name: Cone half angle
  summary: Cone half angle 12 deg (default) | positive scalar
  group: Geometry
- name: Shift linkage control
  summary: Shift linkage model Physical signal (default) | Conserving port
  group: Geometry
- name: Hard stop at back of shift linkage
  summary: Hard stop option on (default) | off
  group: Shift Linkage
- name: Ring-hub clearance when disengaged
  summary: Ring-hub clearance 3 mm (default) | nonnegative scalar
  group: Shift Linkage
- name: Ring stop stiffness
  summary: Ring stop stiffness 10e5 N/m (default) | nonnegative scalar
  group: Shift Linkage
- name: Ring stop damping
  summary: Ring stop damping 1e3 N/(m/s) (default) | nonnegative scalar
  group: Shift Linkage
- name: Shift linkage viscous friction coefficient
  summary: Shift linkage viscous friction 100 N/(m/s) (default) | positive scalar
  group: Shift Linkage
- name: Linkage travel direction
  summary: Disengagement travel direction Positive shift linkage displacement engages clutch (default) | Negative shift linkage
    displacement engages clutch
  group: Shift Linkage
- name: Friction model
  summary: Friction model Fixed kinetic friction coefficient (default) | Velocity-dependent kinetic friction coefficient |
    Temperature-dependent friction coefficients | Temperature and velocity-dependent friction coefficients
  group: Friction
- name: Relative velocity vector
  summary: Relative velocity [0, 100, 1000] rad/s (default) | vector
  group: Friction
- name: Temperature vector
  summary: Temperature [280, 300, 320] K (default) | increasing vector
  group: Friction
- name: Static friction coefficient
  summary: Static friction coefficient 0.35 (default) | scalar
  group: Friction
- name: Static friction coefficient vector
  summary: Static friction coefficient [.4, .38, .36] (default) | vector
  group: Friction
- name: Kinetic friction coefficient
  summary: Kinetic friction coefficient 0.3 (default) | positive scalar
  group: Friction
- name: Kinetic friction coefficient vector
  summary: Kinetic friction coefficient [.3, .22, .19] (default) | [.3, .28, .25] | vector
  group: Friction
- name: Kinetic friction coefficient matrix
  summary: Kinetic friction coefficient [.34, .32, .3; .3, .28, .25; .25, .2, .15] (default) | matrix
  group: Friction
- name: Friction coefficient interpolation method
  summary: Interpolation method Linear (default) | Smooth
  group: Friction
- name: Friction coefficient extrapolation method
  summary: Extrapolation method Linear (default) | Nearest | Error
  group: Friction
- name: Velocity tolerance
  summary: Relative velocity locking threshold 0.001 rad/s (default) | scalar
  group: Friction
- name: Threshold force
  summary: Normal contact force threshold 1 N (default) | scalar
  group: Friction
- name: Viscous friction coefficient
  summary: Viscous friction 0 (default) | nonnegative scalar
  group: Friction
- name: Initial state
  summary: Initial clutch state Unlocked (default) | Locked
  group: Initial Conditions
- name: Clutch fault
  summary: Option to model friction fault Add fault
  group: Faults
- name: Behavior when faulted
  summary: Clutch friction fault response Cannot transmit power (default) | Cannot unlock
  group: Faults
- name: Thermal mass
  summary: Thermal mass 50 kJ/K (default) | scalar
  group: Thermal Port
- name: Initial temperature
  summary: Initial temperature 300 K (default) | scalar
  group: Thermal Port
```

### Geometry

The table shows how the visibility of some parameters depends on the
option that you choose for other parameters.

**Geometry Parameter Dependencies**

| **Geometry** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **Contact surface maximum diameter** | | | | | | |
| **Contact surface minimum diameter** | | | | | | |
| **Cone half angle** | | | | | | |
| **Shift linkage control** | | | | | | |
| `Physical signal` | | | `Conserving port` | | | |
| Exposes physical signal input port **N** | | | Exposes:  - Conserving port   **S** - Physical signal output port   **X** - **Shift Linkage** settings | | | |

### **Contact surface maximum diameter** — Outer diameter `150` `mm` (default) | positive scalar

Outer conical diameter
*do*.

### **Contact surface minimum diameter** — Inner diameter `100` `mm` (default) | positive scalar

Inner conical diameter
*di*.

### **Cone half angle** — Cone half angle `12` `deg` (default) | positive scalar

Half opening angle *α* of the
cone geometry.

### **Shift linkage control** — Shift linkage model `Physical signal` (default) | `Conserving port`

Shift linkage control model:

- `Physical signal`
  — Expose physical signal ports
  **N**, which inputs the normal
  force, and **X**, which outputs
  for the shift linkage travel.
- `Conserving port`
  — Expose conserving port,
  **S**, which is associated with
  shift linkage control.

#### Dependencies

The visibility of **Shift
Linkage** settings and ports
**S**, **X**,
and **N** depend on this setting.
For more information, see Geometry Parameter Dependencies.

### Shift Linkage

These settings are visible only if, in the
**Geometry** settings, the **Shift
linkage control** parameter is set to
`Conserving port`. For more
information, see Shift linkage control and Geometry Parameter Dependencies.

### **Hard stop at back of shift linkage** — Hard stop option `on` (default) | `off`

Whether to include a hard stop at the back of
the shift linkage.

### **Ring-hub clearance when disengaged** — Ring-hub clearance `3` `mm` (default) | nonnegative scalar

Ring-hub clearance when disengaged

### **Ring stop stiffness** — Ring stop stiffness `10e5` `N/m` (default) | nonnegative scalar

Ring stops stiffness

### **Ring stop damping** — Ring stop damping `1e3` `N/(m/s)` (default) | nonnegative scalar

Ring stop damping

### **Shift linkage viscous friction coefficient** — Shift linkage viscous friction `100` `N/(m/s)` (default) | positive scalar

Shift linkage viscous friction
coefficient

### **Linkage travel direction** — Disengagement travel direction `Positive shift linkage displacement engages clutch` (default) | `Negative shift linkage displacement engages clutch`

Linkage travel direction that disengages the
clutch

### Friction

The table shows how the visibility of some ports, parameters, and
settings depends on the option that you choose for other parameters.

**Friction Parameter Dependencies**

| **Friction** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **Friction model** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| Exposes:  - Conserving port   **H** - Thermal parameters in the   **Friction** settings - **Thermal Port** settings | | Exposes:  - Conserving port   **H** - Thermal parameters in the   **Friction** settings - **Thermal Port** settings | |
| - | - | | **Temperature vector** | | **Temperature vector** | |
| - | **Relative velocity vector** | | - | | **Relative velocity vector** | |
| **Static friction coefficient** | **Static friction coefficient** | | **Static friction coefficient vector** | | **Static friction coefficient vector** | |
| **Kinetic friction coefficient** | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient matrix** | |
| - | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | |
| - | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | |
| **Velocity tolerance** | **Velocity tolerance** | | **Velocity tolerance** | | **Velocity tolerance** | |
| **Threshold force** | **Threshold force** | | **Threshold force** | | **Threshold force** | |
| **Viscous friction coefficient** | **Viscous friction coefficient** | | **Viscous friction coefficient** | | **Viscous friction coefficient** | |

### **Friction model** — Friction model `Fixed kinetic friction coefficient` (default) | `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

Parameterization method to model the kinetic
friction coefficient. The options and default
values for this parameter depend on the friction
model that you select for the block. The options are:

- `Fixed kinetic friction
  coefficient` — Provide a fixed
  value for the kinetic friction coefficient.
- `Velocity-dependent kinetic
  friction coefficient` — Define
  the kinetic friction coefficient by
  one-dimensional table lookup based on the relative
  angular velocity between disks.
- `Temperature-dependent friction
  coefficients` — Define the
  kinetic friction coefficient by table lookup based
  on the temperature.
- `Temperature and
  velocity-dependent friction
  coefficients` — Define the
  kinetic friction coefficient by table lookup based
  on the temperature and the relative angular
  velocity between disks.

#### Dependencies

The friction model setting affects the
visibility of other parameters, settings, and
ports. For more information, see Friction Parameter Dependencies.

### **Relative velocity vector** — Relative velocity `[0, 100, 1000]` `rad/s` (default) | vector

Input values for the relative velocity as a
vector. The values in the vector must increase
from left to right. The minimum number of values
depends on the interpolation method that you
select. For linear interpolation, provide at least
two values per dimension. For smooth
interpolation, provide at least three values per
dimension.

#### Dependencies

This parameter is visible only when the
**Friction model** parameter is
set to `Velocity-dependent kinetic
friction coefficient` or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Temperature vector** — Temperature `[280, 300, 320]` `K` (default) | increasing vector

Input values for the temperature as a vector.
The minimum number of values depends on the
interpolation method that you select. For linear
interpolation, provide at least two values per
dimension. For smooth interpolation, provide at
least three values per dimension. The values in
the vector must increase from left to
right.

#### Dependencies

This parameter is visible only when the
**Friction model** parameter is
set to `Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Static friction coefficient** — Static friction coefficient `0.35` (default) | scalar

Static or peak value of the friction
coefficient. The static friction coefficient must
be greater than the kinetic friction
coefficient.

#### Dependencies

This parameter is visible only when the
**Friction model** parameter is
set to `Fixed kinetic friction
coefficient` or
`Velocity-dependent kinetic friction
coefficient`. For more information,
see Friction Parameter Dependencies.

### **Static friction coefficient vector** — Static friction coefficient `[.4, .38, .36]` (default) | vector

Static, or peak, values of the friction
coefficient as a vector. The vector must have the
same number of elements as the temperature vector.
Each value must be greater than the value of the
corresponding element in the kinetic friction
coefficient vector.

#### Dependencies

This parameter is visible only when the
**Friction model** parameter is
set to `Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Kinetic friction coefficient** — Kinetic friction coefficient `0.3` (default) | positive scalar

The kinetic, or Coulomb, friction coefficient.
The coefficient must be greater than zero.

#### Dependencies

This parameter is visible only when the
**Friction model** parameter is
set to `Fixed kinetic friction
coefficient`. For more information,
see Friction Parameter Dependencies.

### **Kinetic friction coefficient vector** — Kinetic friction coefficient `[.3, .22, .19]` (default) | `[.3, .28, .25]` | vector

Output values for kinetic friction coefficient
as a vector. All values must be greater than
zero.

If the **Friction model**
parameter is set to

- `Velocity-dependent kinetic
  friction coefficient` — The
  vector must have same number of elements as
  relative velocity vector.
- `Temperature-dependent friction
  coefficients` — The vector
  must have the same number of elements as the
  temperature vector.

#### Dependencies

This parameter is visible only when the
**Friction model** parameter is
set to `Velocity-dependent kinetic
friction coefficient` or
`Temperature-dependent friction
coefficients`. For more information,
see Friction Parameter Dependencies.

### **Kinetic friction coefficient matrix** — Kinetic friction coefficient `[.34, .32, .3; .3, .28, .25; .25, .2, .15]` (default) | matrix

Output values for kinetic friction coefficient
as a matrix. All the values must be greater than
zero. The size of the matrix must equal the size
of the matrix that is the result of the
temperature vector × the kinetic friction
coefficient relative velocity vector.

#### Dependencies

This parameter is visible only when the
**Friction model** parameter is
set to `Temperature and
velocity-dependent friction
coefficients`. For more information,
see Friction Parameter Dependencies.

### **Friction coefficient interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Interpolation method for approximating the
output value when the input value is between two
consecutive grid points:

- `Linear` —
  Select this option to get the best
  performance.
- `Smooth` —
  Select this option to produce a continuous curve
  with continuous first-order derivatives.

For more information on interpolation
algorithms, see the PS Lookup
Table (1D) block reference page.

#### Dependencies

This parameter is visible only when the
**Friction model** parameter is
set to `Velocity-dependent kinetic
friction coefficient`,
`Temperature-dependent friction
coefficients`, or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Friction coefficient extrapolation method** — Extrapolation method `Linear` (default) | `Nearest` | `Error`

Extrapolation method for determining the
output value when the input value is outside the
range specified in the argument list:

- `Linear` —
  Select this option to produce a curve with
  continuous first-order derivatives in the
  extrapolation region and at the boundary with the
  interpolation region.
- `Nearest` —
  Select this option to produce an extrapolation
  that does not go above the highest point in the
  data or below the lowest point in the data.
- `Error` —
  Select this option to avoid going into the
  extrapolation mode when you want your data to be
  within the table range. If the input signal is
  outside the range of the table, the simulation
  stops and generates an error.

For more information on extrapolation
algorithms, see the PS Lookup
Table (1D) block reference page.

#### Dependencies

This parameter is visible only when the
**Friction model** parameter is
set to `Velocity-dependent kinetic
friction coefficient`,
`Temperature-dependent friction
coefficients`, or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Velocity tolerance** — Relative velocity locking threshold `0.001` `rad/s` (default) | scalar

Relative velocity below which the two surfaces
can lock. The surfaces lock if the torque across
the **B** and
**F** rotational ports is less
than the product of the effective radius, the
static friction coefficient, and the applied
normal force.

### **Threshold force** — Normal contact force threshold `1` `N` (default) | scalar

The normal force applied to the physical
signal port **N** is applied to
the contact only if the amount of force exceeds
the value of the **Threshold
force** parameter. Forces below the
**Threshold force** are not
applied so there is no transmitted frictional
torque.

### **Viscous friction coefficient** — Viscous friction `0` (default) | nonnegative scalar

Viscous friction coefficient.

### Initial Conditions

### **Initial state** — Initial clutch state `Unlocked` (default) | `Locked`

Clutch state at the start of simulation. The
clutch can be in one of two states, locked and
unlocked. A locked clutch constrains the base and
follower shafts to spin at the same velocity, that
is, as a single unit. An unlocked clutch allows
the two shafts to spin at different velocities,
resulting in slip between the clutch
plates.

### Faults

To modify the faults, create a fault and, in the block dialog, click
**Open fault properties**. In the Property
Inspector, click the **Fault behavior** link to
open the faults.

### **Clutch fault** — Option to model friction fault `Add fault`

Whether to model a fault in the block. To add
a fault, click the **Add fault**
hyperlink.

### **Behavior when faulted** — Clutch friction fault response `Cannot transmit power` (default) | `Cannot unlock`

Fault response. You can select the clutch
faulting as either:

- `Cannot transmit
  power`
- `Cannot
  unlock`

#### Dependencies

To enable this parameter, enable faults for
the block by clicking the **Add
fault** hyperlink.

### Thermal Port

**Thermal Port** settings are visible only when, in
the  **Friction** settings, the **Friction
model**  parameter is set to
`Temperature-dependent friction
coefficients` or `Temperature and
velocity-dependent friction coefficients`. For
more information, see Friction Parameter Dependencies.

### **Thermal mass** — Thermal mass `50` `kJ/K` (default) | scalar

Thermal energy required to change the
component temperature by a single degree. The
greater the thermal mass, the more resistant the
component is to temperature change.

#### Dependencies

This parameter is only visible when, in the
 **Friction** settings, the
**Friction model**  parameter is
set to `Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Initial temperature** — Initial temperature `300` `K` (default) | scalar

Component temperature at the start of
simulation. The initial temperature alters the
component efficiency according to an efficiency
vector that you specify, affecting the starting
meshing or friction losses.

#### Dependencies

This parameter is only visible when, in the
 **Friction** settings, the
**Friction model**  parameter is
set to `Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.
## Libraries

Simscape / Driveline / Clutches

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2025a: Parameter name change

The **Viscous drag torque coefficient** parameter
is now the **Viscous friction coefficient**
parameter.

### R2025a: Enumeration updates

The **Hard stop at back of shift linkage** parameter
now uses a check box. This parameter used a drop down in previous
releases.

### R2024a: Model faults with the Simscape faults interface

The Cone Clutch block now supports the Simscape faults interface. To
learn more, see Introduction to Simscape Faults.

## Description

Cone clutch with plates that engage when normal force exceeds threshold

The Cone Clutch block represents a friction
clutch with a conical contact interface. The conical interface reduces the
normal force required for clutch engagement by creating a wedging action
between the clutch components, a cone and a cup. Cone clutch applications
include synchromesh gearboxes, which synchronize the drive and driven shaft
speeds to enable smoother engagement between transmission gears.

The cup component connects rigidly to the drive shaft, spinning with it as a
unit. The cone component connects rigidly to the driven shaft, which sits in
axial alignment with the drive shaft. The clutch engages when the cone
slides toward the cup and presses tightly against its internal surface.
Friction at the cone-cup contact interface enables the clutch to transmit
rotational power between the drive and driven shafts. The friction model of
this block includes both static and kinetic friction contributions, the
latter of which leads to power dissipation during slip between the cone and
cup components.

The Cone Clutch block is based on the
Fundamental Friction
Clutch block. For the complete friction clutch
model, see Fundamental Friction
Clutch. This section discusses the specialized model
implemented in the Cone Clutch block.

When you apply a normal force, *FN*,
the Cone Clutch block can apply two kinds of
friction, kinetic and static, to the driveline motion. The clutch applies
kinetic friction torque only when one driveline axis is spinning relative to
the other driveline axis. The clutch applies static friction torque when the
two driveline axes lock and spin together. The block iterates through
multistep testing to determine when to lock and unlock the clutch.

### Clutch Geometry and Variables

The figure shows the cone clutch geometry.

**Clutch Variables**

| Parameter | Definition | Significance |
| --- | --- | --- |
| *d*o | Outer diameter of the conical contact surface | *See the preceding figure* |
| *d*i | Inner diameter of the conical contact surface | *See the preceding figure* |
| *α* | Cone half angle | *See the preceding figure* |
| *ω* | Relative angular velocity (slip) | *ω*F – *ω*B |
| *ω*Tol | Slip tolerance for clutch locking | *See the following model* |
| *F*N | Normal force applied to conical surfaces | Normal force applied, if greater than threshold: *F*N > *F*th |
| *α* | Cone half-angle | *See the preceding figure* |
| *r*eff | Effective torque radius | Effective moment arm of clutch friction force |
| *k*K | Kinetic friction coefficient | Dimensionless coefficient of kinetic friction of conical friction surfaces. Function of *ω*. |
| *k*S | Static friction coefficient | Dimensionless coefficient of static friction of conical friction surfaces. |
| *τ*K | Kinetic friction torque | *See the following model* |
| *τ*S | Static friction torque limit | (static friction peak factor)·(kinetic friction torque for *ω* → 0)  (*See the following model*) |

### Relation to Fundamental Friction Clutch

The Cone Clutch block is based on the
Fundamental Friction
Clutch block. Instead of requiring the
kinetic and static friction limit torques as input signals, the
Cone Clutch block calculates
the kinetic and static friction from the clutch parameters and the
input normal force signal
*FN*.

**Kinetic Friction**

The kinetic friction torque is the product of four
factors:

τK=kK⋅FN⋅reff⋅sgn(ω)

The kinetic friction torque opposes the relative slip and is
applied with an overall minus sign. It changes sign when
*ω* changes sign.

You specify the kinetic friction coefficient,
*kK*, as
either a constant or a tabulated discrete function of
relative angular velocity, *ω*. The
tabulated function is assumed to be symmetric for positive
and negative values of the relative angular velocity.
Therefore, specify
*k*K for
positive values of *ω* only.

The effective torque radius,
*reff*, is
the effective radius, measured from the driveline axis, at
which the kinetic friction forces are applied at the
frictional surfaces. It is related to the geometry of the
conical friction surface geometry by:

reff=13sinαdo3−di3do2−di2

*do* and
*di* are
the contact surface maximum and minimum diameters,
respectively.

**Static Friction**

The static friction limit is related to the kinetic friction,
setting *ω* to zero and replacing the
kinetic with the static friction coefficient:

TS=kS⋅FN⋅reff≥0

*k*S
>
*k*K, so that the torque, *τ*,
needed across the clutch to unlock it by overcoming static
friction is larger than the kinetic friction at the instant
of unlocking, when *ω* = 0.

The static friction limit defines symmetric *static
friction torque limits* as:

τS≡τS+=−τS−

The range
[*τ*S–,
*τ*S+]
is used by the Fundamental Friction Clutch.

**Engagement and Locking Conditions**

The clutch engages (transmits torque) when the conical
friction surfaces are subject to a positive normal force and
generate kinetic friction: *F*N
> 0 and *τK*>
0.

The clutch locks if and only if it is engaged, and the slip is
less than the velocity tolerance: |*ω*| <
*ω*Tol.

**Power Dissipated by the Clutch**

The power dissipated by the clutch is
|*ω*·*τK*|.
The clutch dissipates power only if it is both slipping (ω ≠ 0) and applying kinetic friction (*τK*
> 0).

### Velocity-Dependent Model

You can model the effects of rotational velocity change by selecting a
velocity-dependent model. To choose a velocity-dependent model, in
the **Friction** settings, set the
**Friction model** parameter to
`Velocity-dependent kinetic friction
coefficient`. For information about a friction
model that depends on both velocity and temperature, see Thermal, Velocity-Dependent Model.

### Thermal Model

You can model the effects of heat flow and temperature change by
selecting a temperature-dependent model. To choose a
temperature-dependent model, in the **Friction**
settings, set the **Friction model** parameter to
`Temperature-dependent friction
coefficients`. For information about a friction
model that depends on both velocity and temperature, see Thermal, Velocity-Dependent Model.

### Thermal, Velocity-Dependent Model

You can model the effects of rotational velocity change and heat flow
by selecting a velocity-dependent and temperature-dependent model.
To choose a model that depends on both velocity and temperature, in
the **Friction** settings, set the
**Friction model** parameter to
`Temperature and velocity-dependent friction
coefficients`.

### Faults

To model a fault in the Cone Clutch block, in the
**Faults** section, click the **Add fault** hyperlink next
to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

When you trigger a fault, the block responds according to the setting
of the **Behavior when faulted** parameter for the
remainder of the simulation. The fault options are:

- `Cannot transmit
  power`
- `Cannot
  unlock`
