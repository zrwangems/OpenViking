---
type: simulink-block
title: 'Rolling Resistance'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles / Tire Subcomponents'
documentation_page: 'rollingresistance'
documentation_source_path: 'ref/rollingresistance.html'
language: en
---

# Rolling Resistance

## Ports

### Input

### **N** — Normal force, N physical signal

Physical signal input port associated with the normal force, in N. The positive force
direction is down.

### **T** — Tread friction force, N physical signal

Physical signal input port associated with the friction force from the road on the tire,
in N. The positive force direction is forwards.

#### Dependencies

To enable this port, set **Resistance model** to
`Pressure and velocity dependent (Magic
Formula)`.
### Conserving

### **H** — Wheel hub, m/s mechanical translational

Mechanical translational conserving port associated with the wheel hub, in m/s.

## Parameters

### **Resistance model** — Rolling resistance computational modeling method `Constant coefficient` (default) | `Pressure and velocity dependent (SAE J2542)` | `Pressure and velocity dependent (Magic Formula)`

Method to compute the rolling resistance on a wheel hub. The parameter has
three options:

- `Constant coefficient`
- `Pressure and velocity dependent (SAE
  J2542)`
- `Pressure and velocity dependent (Magic
  Formula)`

### **Constant coefficient** — Resistance coefficient for rolling tire `0.015` (default) | positive scalar

Constant coefficient value to compute the rolling resistance.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Constant coefficient`.

### **Tire pressure** — Inflation pressure of rolling tire `250e3` `Pa` (default) | positive scalar

Constant inflation pressure of the rolling tire.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (SAE
J2542)` or `Pressure and velocity dependent
(Magic Formula)`.

### **Alpha** — Approximating coefficient α `-0.003` (default) | scalar

SAE J2452 coefficient for the pressure and velocity parameterization. You determine this
value using empirical data in accordance with SAE J2452.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (SAE
J2542)`.

### **Beta** — Approximating coefficient β `0.97` (default) | scalar

SAE J2452 coefficient for the pressure and velocity parameterization. You determine this
value using empirical data in accordance with SAE J2452.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (SAE
J2542)`.

### **Coefficient A** — Approximating coefficient A `84e-4` (default) | positive scalar

SAE J2452 coefficient for the pressure and velocity parameterization. You determine this
value using empirical data in accordance with SAE J2452.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (SAE
J2542)`.

### **Coefficient B** — Approximating coefficient B `6.2e-4` `s/m` (default) | nonnegative scalar

SAE J2452 coefficient for the pressure and velocity parameterization. You determine this
value using empirical data in accordance with SAE J2452.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (SAE
J2542)`.

### **Coefficient C** — Approximating coefficient C `1.6e-4` `s^2/m^2` (default) | nonnegative scalar

SAE J2452 coefficient for the pressure and velocity parameterization. You determine this
value using empirical data in accordance with SAE J2452.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (SAE
J2542)`.

### **Tire nominal pressure, NOMPRES** — Nominal tire pressure `240e3` `Pa` (default) | positive scalar

Nominal tire pressure. `NOMPRES` it the TIR file
identifier.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (Magic
Formula)`.

### **Tire nominal vertical load, FNOMIN** — Normal force `4000` `N` (default) | positive scalar

Nominal normal force, *Fz0*, on
tire. `FNOMIN` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (Magic
Formula)`.

### **Nominal hub longitudinal speed, LONGVL** — Nominal hub longitudinal speed `16` `m/s` (default) | positive scalar

Nominal hub longitudinal speed. `LONGVL` is the TIR file
identifier.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (Magic
Formula)`.

### **Q-coefficient parameters [qsy1 qsy2 qsy3 qsy4 qsy5 qsy6 qsy7 qsy8]** — Magic Formula Q-coefficients `[.0082, 0, .0014, .001, 0, 0, 1.08, -.5]` `1` (default) | vector of length 8

Magic Formula Q coefficients. `qsy1`,…,
`qsy8` correspond to the TIR file identifiers.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (Magic
Formula)`.

### **Scale factor of rolling resistance, LMY** — Rolling resistance `1` (default) | positive scalar

Scale factor of the rolling resistance,
*λMY*.
`LMY` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Resistance model** to
`Pressure and velocity dependent (Magic
Formula)`.

### **Velocity threshold** — Velocity when full rolling resistance force is transmitted to rolling hub `0.001` `m/s` (default) | positive scalar

Minimum velocity that attains the maximum amount of rolling
resistance.

## Libraries

Simscape / Driveline / Tires & Vehicles / Tire Subcomponents

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

### R2023a: Magic Formula compatibility enhancements

The block is now compatible with the Magic Formula. You can set **Resistance
model** to `Pressure and velocity dependent (Magic
Formula)` to enable Magic Formula resistance parameters.

## Description

Model rolling resistance

The Rolling Resistance block represents the resistance force
that acts on the wheel hub due to the rolling resistance at the road-wheel contact
surface. The block can use a constant resistance coefficient of the pressure and
velocity dependence of the SAE J2452 standard, or the Magic Formula. The resistance
force is zero when the normal force acting at the wheel-road surface is less than or
equal to zero.

### Constant Resistance Coefficient Parameterization

When you set **Resistance model** to `Constant
coefficient`, the rolling resistance is directly proportional to
the resistance coefficient *F* = *Nμ*, where:

- *F* is the rolling resistance force.
- *N* is the normal force.
- *μ* is the rolling resistance coefficient.

The rolling resistance coefficient has a hyperbolic form that eliminates discontinuity at *vhub* = 0

μ=μ0⋅tanh(4⋅vhubvthreshold),

where:

- *μ0* is the asymptotic rolling
  resistance coefficient.
- *vhub* is the hub velocity.
- *vthreshold* is the threshold
  velocity.

### Pressure and Velocity Dependent Parameterization

When you set **Resistance model** to `Pressure and velocity
dependent (SAE J2542)`, the block uses the formula:

F=(PP0)α(NN0)βN0⋅(A+B|vhub|+Cvhub2)tanh(4vhubvthreshold),

where:

- *P* is the tire pressure.
- *vhub* is the hub velocity.
- *α, β, A, B, and C* are the approximating
  coefficients.
- *P0* is 1 Pascal (Pa).
- *N0* is 1 Newton (N).

In this equation, the parameters *P0* and
*N0* remove the physical units from
each exponential expression base.

When you set **Resistance model** to `Pressure and velocity
dependent (Magic Formula)`, the block uses the Magic Formula to
calculate rolling resistance as

F=FZ0λMy(qsy1+qsy2FX,TreadFZ0+qsy3|VHV0|+qsy4(VHV0)4)(FZFZ0)qsy7(pipi0)qsy8tanh(4vhubvthreshold),

where:

- *FZ0* is the **Tire
  nominal vertical load, FNOMIN** parameter.
- *λMy* is the **Scale
  factor of rolling resistance, LMY** parameter.
- *qsy1,...,qsy8*
  are the elements of the **Q-coefficient parameters [qsy1 qsy2
  qsy3 qsy4 qsy5 qsy6 qsy7 qsy8]** parameter.
- *V0* is the **Hub
  nominal longitudinal speed, LONGVL** parameter.
- *pi* is the **Tire
  pressure** parameter.
- *pi0* is the **Tire
  nominal pressure, NOMPRES** parameter.
- *VH* is the wheel hub
  longitudinal velocity.
- *FX,Tread* is the longitudinal
  friction force exerted by the road on the tire tread.
- *FZ* is the vertical load on
  the tire.

The `tanh` expressions in this parameterization
smoothly change the sign of the resistance force when
*vhub = 0*.
