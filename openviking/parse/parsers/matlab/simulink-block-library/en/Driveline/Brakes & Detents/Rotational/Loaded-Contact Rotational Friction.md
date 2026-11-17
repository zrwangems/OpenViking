---
type: simulink-block
title: 'Loaded-Contact Rotational Friction'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes & Detents / Rotational'
documentation_page: 'loadedcontactrotationalfriction'
documentation_source_path: 'ref/loadedcontactrotationalfriction.html'
language: en
---

# Loaded-Contact Rotational Friction

## Ports
```yaml
ports:
- name: N
  summary: Normal force physical signal
  direction: input
- name: B
  summary: Base mechanical rotational
  direction: conserving
- name: F
  summary: Follower mechanical rotational
  direction: conserving
- name: H
  summary: Heat flow thermal
  direction: conserving
```

### Input

### **N** — Normal force physical signal

Physical signal port associated with the
normal force. This signal is positive or zero. A
signal of less than zero is interpreted as
zero.
### Conserving

### **B** — Base mechanical rotational

Rotational conserving port associated with the
driving (base) surface.

### **F** — Follower mechanical rotational

Rotational conserving port associated with the
driven (follower) surface.

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
## Parameters
```yaml
parameters:
- name: Geometry model
  summary: Parameterization method Define effective radius (default) | Define annular region
  group: Geometry
- name: Effective torque radius
  summary: Effective friction surface radius 130 mm (default) | positive scalar
  group: Geometry
- name: Friction surface outside diameter
  summary: Friction surface outer diameter 150 mm (default) | positive scalar
  group: Geometry
- name: Friction surface inside diameter
  summary: Friction surface inner diameter 100 mm (default) | positive scalar less than outer diameter
  group: Geometry
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
  summary: Kinetic friction coefficient 0.3 (default) | positve scalar
  group: Friction
- name: Kinetic friction coefficient vector
  summary: Kinetic friction coefficient [.3, .22, .19] (default) | [.3, .28, .25] | vector
  group: Friction
- name: Kinetic friction coefficient matrix
  summary: Kinetic friction coefficient [.34, .32, .3; .3, .28, .25; .25, .2, .15] (default) | matrix
  group: Friction
- name: Friction coefficient interpolation method
  summary: Extrapolation method Linear (default) | Smooth
  group: Friction
- name: Friction coefficient extrapolation method
  summary: Interpolation method Linear (default) | Nearest | Error
  group: Friction
- name: Velocity tolerance
  summary: Relative velocity locking threshold 0.001 rad/s (default) | scalar
  group: Friction
- name: Threshold force
  summary: Normal contact force threshold 1 N (default) | scalar
  group: Friction
- name: Viscous drag torque coefficient
  summary: Viscous drag torque 0 N*m/(rad/s) (default) | nonnegative scalar
  group: Viscous Losses
- name: Initial state
  summary: Initial clutch state Unlocked (default) | Locked
  group: Initial Conditions
- name: Friction fault
  summary: Option to model friction fault Add fault
  group: Faults
- name: Behavior when faulted
  summary: Response to fault trigger Cannot transmit power (default) | Cannot unlock
  group: Faults
- name: Thermal mass
  summary: Thermal mass 50 kJ/K (default) | scalar
  group: Thermal Port
- name: Initial temperature
  summary: Initial temperature 300 K (default) | scalar
  group: Thermal Port
```

### Geometry

### **Geometry model** — Parameterization method `Define effective radius` (default) | `Define annular region`

Parameterization method for the loaded-contact
friction model:

- `Define effective
  radius` — Provide a value for
  the friction effective radius.
- `Define annular
  region` — Define the friction
  effective radius in terms of the inside and
  outside diameters of the friction surface. If you
  select this option, the panel changes from its
  default.

#### Dependencies

The value of this parameter affects the
visibility of other parameters in the
**Geometry** settings.

### **Effective torque radius** — Effective friction surface radius `130` `mm` (default) | positive scalar

Effective radius
*r*eff.
The value must be greater than zero.

#### Dependencies

This parameter is visible only if the
**Geometry model** parameter is
set to `Define effective
radius`.

### **Friction surface outside diameter** — Friction surface outer diameter `150` `mm` (default) | positive scalar

Outside diameter, 2 \*
*ro*, of
the friction surfaces. Must be greater than
zero.

#### Dependencies

This parameter is visible only if the
**Geometry model** parameter is
set to `Define annular
region`.

### **Friction surface inside diameter** — Friction surface inner diameter `100` `mm` (default) | positive scalar less than outer diameter

Inside diameter, 2 \*
*ri*, of
the friction surfaces. Must be greater than zero,
but less than the friction surface outside
diameter.

#### Dependencies

This parameter is visible only if the
**Geometry model** parameter is
set to `Define annular
region`.

### Friction

The table shows how the visibility of some ports, parameters, and
settings depends on the option that you choose for other
parameters.

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
  angular velocity between discs.
- `Temperature-dependent friction
  coefficients` — Define the
  kinetic friction coefficient by table lookup based
  on the temperature.
- `Temperature and
  velocity-dependent friction
  coefficients` — Define the
  kinetic friction coefficient by table lookup based
  on the temperature and the relative angular
  velocity between discs.

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

This parameter is only visible when you set
the **Friction model** parameter
to `Velocity-dependent kinetic
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

This parameter is only visible when you set
the **Friction model** parameter
to `Temperature-dependent friction
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

this parameter is visible only when the
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

This parameter is only visible when you set
the **Friction model** parameter
to `Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Kinetic friction coefficient** — Kinetic friction coefficient `0.3` (default) | positve scalar

The kinetic, or Coulomb, friction coefficient.
The coefficient must be greater than zero.

#### Dependencies

This parameter is only visible when you set
the **Friction model** parameter
to `Fixed kinetic friction
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

This parameter is only visible when you set
the **Friction model** parameter
to `Velocity-dependent kinetic
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

This parameter is only visible when you set
the **Friction model** parameter
to `Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Friction coefficient interpolation method** — Extrapolation method `Linear` (default) | `Smooth`

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

This parameter is only visible when you set
the **Friction model** parameter
to `Velocity-dependent kinetic
friction coefficient`,
`Temperature-dependent friction
coefficients`, or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Friction coefficient extrapolation method** — Interpolation method `Linear` (default) | `Nearest` | `Error`

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

This parameter is only visible when you set
the **Friction model** parameter
to `Velocity-dependent kinetic
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
applied, so there is no transmitted frictional
torque.

### Viscous Losses

### **Viscous drag torque coefficient** — Viscous drag torque `0` `N*m/(rad/s)` (default) | nonnegative scalar

Viscous drag coefficient,
*μvisc*,
for computing the drag torque. The coefficient
depends on the type of operating fluid, fluid
temperature, and the maximum distance between the
surfaces.

### Initial Conditions

### **Initial state** — Initial clutch state `Unlocked` (default) | `Locked`

State of the internal
Fundamental Friction
Clutch block state at the start of simulation.

- `Locked` —
  Rotational ports **B** and
  **F** are initially locked
  together.
- `Unlocked` —
  Rotational ports **B** and
  **F** are initially sliding
  relative to each other.

### Faults

To modify the faults, create a fault and, in the block dialog, click
**Open fault properties**. In the Property
Inspector, click the **Fault behavior** link to
open the faults.

### **Friction fault** — Option to model friction fault `Add fault`

Whether to model a fault in the block. To add
a fault, click the **Add fault**
hyperlink.

### **Behavior when faulted** — Response to fault trigger `Cannot transmit power` (default) | `Cannot unlock`

Behavior when a fault is triggered. You can
select the faulting between the surfaces as either:

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
velocity-dependent friction
coefficients`.

### **Thermal mass** — Thermal mass `50` `kJ/K` (default) | scalar

Thermal energy required to change the
component temperature by a single degree. The
greater the thermal mass, the more resistant the
component is to temperature change.

#### Dependencies

To enable this parameter, set
**Friction model**  to
`Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`.

### **Initial temperature** — Initial temperature `300` `K` (default) | scalar

Thermal energy required to change the
component temperature by a single degree. The
greater the thermal mass, the more resistant the
component is to temperature change.

#### Dependencies

To enable this parameter, set
**Friction model**  to
`Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`.
## Libraries

Simscape / Driveline / Brakes & Detents / Rotational

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

### R2024a: Model faults with the Simscape faults interface

The Loaded-Contact Rotational Friction block now supports the Simscape faults interface. To
learn more, see Introduction to Simscape Faults.

## Description

Loaded-contact friction between two rotating surfaces

The Loaded-Contact Rotational Friction block
simulates friction between two rotating surfaces loaded with a normal force.

The block is implemented as a structural component based on the
Fundamental Friction Clutch block.
From the locked state, the two surfaces unlock if the transmitted torque
exceeds the static friction, as defined by the static coefficient of
friction and current normal force. For details on how the locking and
unlocking are modeled, see the Fundamental Friction
Clutch block reference page.

Torque is transmitted for normal forces larger than the **Threshold
force** parameter.

### Equations

The block simulates friction between two rotating surfaces loaded with
a normal force. When the two rotating surfaces are not locked, the
transmitted torque is determined with the following
equations:

τ = N· μ· reff · sign(ω) + τvisc ,

reff= 23⋅ro3−ri3ro2−ri2 ,

τvisc = μvisc· ω ,

where:

- *τ* is the transmitted
  torque.
- *N* is the normal
  force.
- *μ* is the friction
  coefficient.
- *reff*
  is the effective radius.
- *ro*
  is the surface outside radius.
- *ri*
  is the surface inside radius.
- *ω* is the relative angular
  velocity.
- *τvisc*
  is the viscous drag torque.
- *μvisc*
  is the viscous friction coefficient.

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

To model a fault in the Loaded-Contact Rotational Friction block, in the
**Faults** section, click the **Add fault** hyperlink next
to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

When you trigger a fault, the clutch responds according to the
**Behavior when faulted** setting for the
remainder of the simulation. The fault options are:

- `Cannot transmit
  power`
- `Cannot
  unlock`

### Limitations and Assumptions

- The model does not account for inertia. Add inertia
  terms externally to the **B** and
  **F** ports as required.
- The model computes the torque assuming a uniform
  distribution of the normal force.
