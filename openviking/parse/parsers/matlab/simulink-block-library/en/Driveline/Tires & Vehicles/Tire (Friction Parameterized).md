---
type: simulink-block
title: 'Tire (Friction Parameterized)'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles'
documentation_page: 'tirefrictionparameterized'
documentation_source_path: 'ref/tirefrictionparameterized.html'
language: en
---

# Tire (Friction Parameterized)

## Ports

### Input

### **N** — Normal force, N physical signal

Physical signal input port associated with the normal force acting on
the tire, in N. The normal force is positive if it acts downward on the
tire, pressing it against the pavement.

### **M** — Friction coefficients, unitless physical signal | two-element vector

Physical signal input port associated with the unitless static and kinetic friction
coefficients, *μs* and
*μk*, respectively.
Provide the friction coefficients as a two-element vector, specified in
the order [*μs*,
*μk*].

#### Dependencies

To enable this port, set **Friction model** to
`Physical signal friction
coefficients`.
### Output

### **S** — Slip, unitless or in rad/s physical signal

Physical signal output port associated with the slip between the tire and road, unitless
or in rad/s. When you set **Output type** to:

- `Relative`, the port outputs
  unitless, relative slip.
- `Absolute`, the port outputs
  absolute slip in rad/s.
### Conserving

### **A** — Axle mechanical rotational

Mechanical rotational conserving port associated with the axle.

### **H** — Hub mechanical rotational

Mechanical rotational port associated with the wheel hub.

## Parameters

### Main

### **Rolling radius** — Unloaded tire-wheel radius `0.3` `m` (default) | positive scalar

Distance between the pavement and the center of the tire.

### **Slip output type** — Relative or absolute switch option `Relative` (default) | `Absolute`

Whether the block uses a relative or absolute slip friction
parameterization.

### **Friction model** — Friction model `Fixed kinetic friction coefficient` (default) | `Table lookup kinetic friction coefficient` | `Physical signal friction coefficients`

Friction model the block uses during the simulation. When you select:

- `Fixed kinetic friction
  coefficient`, the block uses the constant
  static and kinetic friction coefficients that you
  specify.
- `Table lookup kinetic friction
  coefficient`, you can specify friction
  using a table lookup. The block treats the static
  coefficient as a constant and treats the kinetic coefficient
  as a constant or function of tire slip. Use this setting to
  simulate tire dynamics under constant pavement
  conditions.
- `Physical signal friction
  coefficients`, the block enables port
  **M** for you to provide
  [*μs*,
  *μk*]. Use
  this setting to simulate tire dynamics under variable
  pavement conditions.

### **Static friction coefficient** — Static friction coefficient `0.90` (default) | positive scalar

Ratio of the allowable longitudinal force to the normal force allowed before the tire
begins to slip, *μs*. The value
of this parameter must be greater than either the **Kinetic
friction coefficient** parameter or the largest value in
the **Kinetic friction coefficient vector**
parameter.

#### Dependencies

To enable this parameter, set **Friction model** to `Fixed
kinetic friction coefficient` or `Table
lookup kinetic friction coefficient`.

### **Kinetic friction coefficient** — Kinetic friction coefficient `0.70` (default) | positive scalar

Ratio of the longitudinal force transferred to the road to the normal force allowed
during tire slip, *μk*. The
ratio must be greater than zero.

#### Dependencies

To enable this parameter, set **Friction model**
to `Fixed kinetic friction
coefficient`.

### **Tire slip vector** — Tire slip `[0, .02, .06, .15, .6, 1]` `rad/s` (default) | vector

Reference tire slip. The elements in this vector correspond one-to-one
with the **Kinetic friction coefficient vector**
parameter. If the **Tire slip vector** parameter
contains only nonnegative values, the block assumes the
slip-versus-friction function to be symmetric about the slip
axis.

#### Dependencies

To enable this parameter, set **Friction model**
to `Table lookup kinetic friction
coefficient`.

### **Kinetic friction coefficient vector** — Kinetic friction coefficient `[.89, .88, .8, .75, .7, .7]` (default) | vector

Kinetic friction coefficient for a given tire slip. The elements in this vector
correspond one-to-one with the **Tire slip vector**
parameter. The vectors must be the same size.

#### Dependencies

To enable this parameter, set **Friction model**
to `Table lookup kinetic friction
coefficient`.

### **Interpolation method** — Interpolation method `Linear` (default) | `Smooth`

Interpolation method for the lookup table to process the tire slip-kinetic friction
coefficient characteristic. To prioritize performance, select
`Linear`. To produce a continuous curve
with continuous first-order derivatives, select
`Smooth`.

For more information on interpolation algorithms, see the PS Lookup Table (1D)
block reference page.

#### Dependencies

To enable this parameter, set **Friction model** to `Table
lookup kinetic friction coefficient`.

### **Extrapolation method** — Extrapolation method `Linear` (default) | `Nearest` | `Error`

Extrapolation method for the lookup table to process the tire slip-kinetic friction
coefficient characteristic. To produce:

- `Linear` — Select this option to produce
  a curve with continuous first-order derivatives in the
  extrapolation region and at the boundary with the
  interpolation region.
- `Nearest` — Select this option to produce
  an extrapolation that does not go above the highest point in
  the data or below the lowest point in the data.
- `Error` — Select this option to avoid
  going into the extrapolation mode when you want your data to
  be within the table range. If the input signal is outside
  the range of the table, the simulation stops and generates
  an error.

For more information on extrapolation algorithms, see the PS Lookup Table (1D)
block reference page.

#### Dependencies

To enable this parameter, set **Friction model** to `Table
lookup kinetic friction coefficient`.

### Dynamics

### **Compliance** — Dynamical compliance model `No compliance - Suitable for HIL simulation` (default) | `Specify stiffness and damping`

Model for the dynamical compliance of the tire.

- `No compliance - Suitable for HIL
  simulation` — The block ignores dynamical
  compliance.
- `Specify stiffness and damping` — The
  block treats the tire as a stiff, dampened spring that deforms
  under load.

### **Longitudinal stiffness** — Longitudinal stiffness `1e6` `N/m` (default) | positive scalar

Tire longitudinal stiffness, *CFx*.

#### Dependencies

To enable this parameter, set **Compliance** to
`Specify stiffness and damping`.

### **Longitudinal damping** — Longitudinal damping `1000` `N/(m/s)` (default) | positive scalar

Tire longitudinal damping, *bFx*.

#### Dependencies

To enable this parameter, set **Compliance** to
`Specify stiffness and damping`.

### **Inertia** — Inertia option `No inertia` (default) | `Specify inertia and initial velocity`

Whether to simulate tire rotational inertia. When you select

- `No inertia` — The block ignores
  inertia.
- `Specify inertia and initial
  velocity` — The block treats the tire as a
  stiff, dampened spring that deforms under load.

#### Dependencies

To enable this parameter, set **Inertia** to
`Specify inertia and initial
velocity`.

### **Tire inertia** — Tire rotational inertia `1` `kg*m^2` (default) | positive scalar

Rotational inertia, *Iw*, of
the wheel-tire assembly.

#### Dependencies

To enable this parameter, set **Inertia** to
`Specify inertia and initial
velocity`.

### **Initial velocity** — Initial rotational velocity `0` `rad/s` (default) | scalar

Initial angular velocity, *Ω(0)*, of the tire.

#### Dependencies

To enable this parameter, set **Inertia** to `Specify
inertia and initial velocity`.

### Rolling Resistance

### **Rolling resistance** — Rolling resistance option `off` (default) | `on`

Whether to simulate rolling resistance.

### **Resistance model** — Rolling resistance option `Constant coefficient` (default) | `Pressure and velocity dependent`

Whether to simulate the rolling resistance of the tire. When you
select

- `Constant coefficient` — The block
  ignores rolling resistance.
- `Pressure and velocity dependent` —
  Include rolling resistance.

### **Constant coefficient** — Proportionality constant `0.015` (default) | positive scalar

Coefficient that sets the proportionality between the normal force and
the rolling resistance force. The parameter must be greater than
zero.

#### Dependencies

To enable this parameter, select **Rolling resistance** and set
**Resistance model** to `Constant
coefficient`.

### **Tire pressure** — Tire pressure `250e3` `Pa` (default) | positive scalar

Inflation pressure of the tire. The parameter must be greater than
zero.

#### Dependencies

To enable this parameter, select **Rolling resistance** and set
**Resistance model** to `Pressure
and velocity dependent`.

### **Alpha** — Tire pressure equation exponent `-0.003` (default) | scalar

Exponent of the tire pressure in the model equation.

#### Dependencies

To enable this parameter, select **Rolling
resistance** and set **Resistance
model** to `Pressure and velocity
dependent`.

### **Beta** — Normal force equation exponent `0.97` (default) | scalar

Exponent of the normal force model equation.

#### Dependencies

To enable this parameter, select **Rolling
resistance** and set **Resistance
model** to `Pressure and velocity
dependent`.

### **Coefficient A** — Velocity-independent force component *A* `84e-4` (default) | positive scalar

Velocity-independent force component in the model equation. The parameter must be
greater than zero.

#### Dependencies

To enable this parameter, select **Rolling
resistance** and set **Resistance
model** to `Pressure and velocity
dependent`.

### **Coefficient B** — Velocity-dependent force component *B* `6.2e-4` `s/m` (default) | positive scalar

Velocity-dependent force component in the model equation. The parameter must be greater
than zero.

#### Dependencies

To enable this parameter, select **Rolling
resistance** and set **Resistance
model** to `Pressure and velocity
dependent`.

### **Coefficient C** — Velocity-dependent force component *C* `1.6e-4` `s^2/m^2` (default) | positive scalar

Force component that depends on the square of the velocity term in the model equation.
The parameter must be greater than zero.

#### Dependencies

To enable this parameter, select **Rolling
resistance** and set **Resistance
model** to `Pressure and velocity
dependent`.

### **Velocity threshold** — Wheel hub velocity threshold for mathematical slip model `0.001` `m/s` (default) | positive scalar

Velocity at which the block applies the full rolling resistance. This parameter ensures
that the force remains continuous during velocity direction changes,
which increases the numerical stability of the simulation. The parameter
must be greater than zero.

#### Dependencies

To enable this parameter, select **Rolling resistance**.

### Advanced

### **Traction velocity tolerance** — Traction velocity tolerance `0.01` `m/s` (default) | positive scalar

Magnitude of the relative velocity between the tire and ground at which the tire regains
traction. If this value is too low, the tire does not gain traction. If
this value is too high, the tire velocity changes suddenly when the tire
gains traction, which can result in an unstable simulation. The
parameter must be greater than zero.

### **Engagement threshold force** — Engagement threshold force `10` `N` (default) | positive scalar

Threshold force at which block applies the normal force to the tire. If this value is
too low, the tire gains and loses traction rapidly. If this value is too
high, the block produces unrealistically low static and dynamic friction
forces. The parameter must be greater than zero.

### **Initial traction state** — Initial traction state `Tire is initially slipping` (default) | `Tire is initially in traction`

Option to have the tire in traction or slipping at the start of
simulation.

## Libraries

Simscape / Driveline / Tires & Vehicles

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

### R2025a: Enumeration Updates

The **Rolling resistance** parameter now uses a check box. This
parameter used a drop down in previous releases.

### R2024b: Improve compliance and inertia

The block locations of the inertias and compliance to be more accurate during
acceleration. The block uses new definitions of absolute and relative slip to more
closely reflect the Tire (Magic Formula) block.
Models that contain the Tire (Friction Parameterized)
block generate different outputs in R2024b than in previous releases.

### R2022b: Select slip output type

You can now model relative tire slip, which is consistent with the Tire
(Magic Formula) block. To select between relative and absolute
slip, set **Output type** to `Relative` or
`Absolute`. The output at port **S** is now
multiplied by `-1` compared to versions prior to R2024b.

## Description

Tire with friction parameterized in terms of static and kinetic coefficients

The Tire (Friction Parameterized) block represents a tire
with friction parameterized in terms of static and kinetic coefficients. The static
friction coefficient, *μs*, determines the
applied torque at which the tire loses traction and begins to slip. The kinetic friction
coefficient, *μk*, determines the amount of
torque that the tire transmits to the pavement once it begins to slip. The tire regains
traction when its relative velocity over the pavement falls below the specified traction
velocity tolerance.

To increase the fidelity of the tire model, specify properties such as tire compliance,
inertia, and rolling resistance. Note that these properties increase the complexity of
the tire model and can slow down simulation. Consider ignoring tire compliance and
inertia if simulating the model in real time or when preparing the model for
hardware-in-the-loop (HIL) simulation.

### Wheel Slip

When you set **Slip output type** to `Relative`,
the block outputs the relative slip velocity as a unitless physical signal at port
**S**, such that

S=−Vx−rwΩ−rwu˙|Vx|,

where:

- *Vx* is the wheel hub
  longitudinal velocity at port **H**.
- *rw* is the rolling
  radius.
- *Ω* is the wheel axle angular velocity at port
  **A**.

When you set **Slip output type** to
`Absolute`, port **S** outputs the
absolute contact point slip velocity in a rotational form such that

S=−Vx−rwΩ−rwu˙rw,

where *u* is the time-rate of change in
longitudinal deformation and *u/rw* is
equivalent to the rotational velocity of the spring and damper in the logged
simulation results.

When you set **Slip output type** to `Absolute`,
the block uses the friction model of the Fundamental Friction Clutch block. The figure demonstrates how the
block implements slip:

Model diagram depicting how the block implements slip.

When you set **Compliance** to `No
compliance - Suitable for HIL simulation`, the block sets u˙=0.
