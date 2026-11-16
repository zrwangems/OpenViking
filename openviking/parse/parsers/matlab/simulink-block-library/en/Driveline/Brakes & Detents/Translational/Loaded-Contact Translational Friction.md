---
type: simulink-block
title: 'Loaded-Contact Translational Friction'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes & Detents / Translational'
documentation_page: 'loadedcontacttranslationalfriction'
documentation_source_path: 'ref/loadedcontacttranslationalfriction.html'
language: en
---

# Loaded-Contact Translational Friction

## Ports

### Input

### **N** — Normal force physical signal

Physical signal port associated with the
normal force. This signal is positive or zero. A
signal of less than zero is interpreted as
zero.
### Conserving

### **B** — Base mechanical translational

Translational conserving port associated with
the driving surface.

### **F** — Follower mechanical translational

Translational conserving port associated with
the driven surface.

### **H** — Heat flow thermal

Thermal conserving port associated with heat
flow.

#### Dependencies

To enable this parameter, set
**Friction model** to
`Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`.

## Parameters

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

### **Relative velocity vector** — Relative velocity `[0, .1, 1]` `m/s` (default) | vector

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

This parameter is only visible when you set
the **Friction model** parameter
to `Temperature-dependent friction
coefficients` or
`Temperature and velocity-dependent
friction coefficients`. For more
information, see Friction Parameter Dependencies.

### **Kinetic friction coefficient** — Kinetic friction coefficient `0.3` (default) | positive scalar

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

### **Velocity tolerance** — Relative velocity locking threshold `0.001` `m/s` (default) | scalar

Relative velocity below which the two surfaces
can lock. The surfaces lock if the torque across
the **B** and
**F** translational ports is less
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

### **Viscous drag torque coefficient** — Viscous drag torque `0` `N/(m/s)` (default) | nonnegative scalar

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
  Translational ports **B** and
  **F** are initially locked
  together.
- `Unlocked` —
  Translational ports **B** and
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

To enable this parameter, first enable
faults for the block by clicking the
**Add fault** hyperlink.

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

Simscape / Driveline / Brakes & Detents / Translational

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

The Loaded-Contact Translational Friction block now supports the Simscape faults interface. To
learn more, see Introduction to Simscape Faults.

## Description

Loaded-contact friction between two sliding surfaces

The  Loaded-Contact Translational Friction
block simulates friction between two sliding surfaces loaded with a normal
force.

The block is implemented as a structural component based on the
Fundamental Friction Clutch block.
From the locked state, the two surfaces unlock if the exerted force exceeds
the static friction, as defined by the static coefficient of friction and
current normal force. For details on how the locking and unlocking are
modeled, see the Fundamental Friction Clutch
block reference page.

Force is transmitted for normal forces larger than the **Threshold
force** parameter.

### Equations

The block simulates friction between two sliding surfaces loaded with
a normal force. When the two sliding surfaces are not locked, the
friction force is determined with these equations:

F = N· μ · sign(vrel)+Fvisc ,

Fvisc = μvisc· vrel ,

where:

- *F* is the transmitted
  force.
- *N* is the normal
  force.
- *μ* is the friction
  coefficient.
- *vrel*
  is the relative velocity.
- *Fvisc*
  is the viscous drag force.
- *μvisc*
  is the viscous drag force coefficient.

### Velocity-Dependent Model

You can model the effects of translational velocity change by
selecting a velocity-dependent model. To choose a velocity-dependent
model, in the **Friction** settings, set the
**Friction model** parameter to
`Velocity-dependent kinetic friction
coefficient`.

For the velocity-dependent model these related parameters become
visible in the **Friction** settings:

- **Relative velocity
  vector**
- **Kinetic friction coefficient
  vector**
- **Friction coefficient interpolation
  method**
- **Friction coefficient extrapolation
  method**

### Thermal Model

You can model the effects of heat flow and temperature change by
selecting a temperature-dependent model. To choose a
temperature-dependent model, in the **Friction**
settings, set the **Friction model** parameter to
`Temperature-dependent friction
coefficients`.

For the temperature-dependent model, thermal port
**H** and these settings are visible:

- In the **Friction** settings:

  - **Temperature
    vector**
  - **Static friction coefficient
    vector**
  - **Kinetic friction coefficient
    vector**
  - **Friction coefficient interpolation
    method**
  - **Friction coefficient extrapolation
    method**
- In the **Thermal Port** settings:

  - **Thermal mass**
  - **Initial
    Temperature**

### Thermal, Velocity-Dependent Model

You can model the effects of translational velocity change and heat
flow by selecting a velocity-dependent and temperature-dependent
model. To choose a model that depends on both velocity and
temperature, in the **Friction** settings, set the
**Friction model** parameter to
`Temperature and velocity-dependent friction
coefficients`.

For the velocity-dependent and temperature-dependent model, thermal
port **H** and these related settings and
parameters become visible:

- In the **Friction** settings:

  - **Relative velocity
    vector**
  - **Temperature
    vector**
  - **Static friction coefficient
    vector**
  - **Kinetic friction coefficient
    matrix**
  - **Friction coefficient interpolation
    method**
  - **Friction coefficient extrapolation
    method**
- In the **Thermal Port** settings:

  - **Thermal mass**
  - **Initial
    Temperature**

### Faults

To model a fault in the Loaded-Contact Translational Friction block, in the
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

- The model does not account for body mass. Add mass
  terms externally to the **B** and
  **F** ports as required.
- The model computes the transmitted force assuming a
  uniform distribution of the normal force.
