---
type: simulink-block
title: 'Variable Rotational Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'variablerotationalspring'
documentation_source_path: 'ref/variablerotationalspring.html'
language: en
---

# Variable Rotational Spring

## Ports

`K`
:   Physical signal input port representing the variable spring
    stiffness.

`C`
:   Rotational conserving port.

`R`
:   Rotational conserving port.

## Parameters

**Minimum spring rate**
:   Minimum value allowed for the spring rate (stiffness). The physical signal
    input saturates below the specified value. The parameter must be greater
    than zero. The default value is `0.01`. The default unit is
    `(N*m/rad)`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Rotational spring with variable spring stiffness

The block represents a torsional spring with variable spring stiffness. A physical
signal input port provides the value of the variable spring stiffness. The magnitude of
the spring torque is equal to the product of the physical signal input and the relative
angular displacement between the two rotational conserving ports. A minimum spring rate
value prevents non-physical values.

The rotational spring torque satisfies the following expression:

T={K⋅θK≥KminKmin⋅θK<Kmin,

The parameters are:

- *T* — Torque transmitted through the spring
- *K* — Spring rate (stiffness)
- *Kmin* — Minimum allowable
  spring rate (stiffness)
- *θ* — Relative angular displacement measured between
  the two rotational conserving ports according to θ=θinit+θR−θC
- *θinit* — Initial angular
  deformation between the two rotational conserving ports
- *θR* — Absolute angular
  displacement of rotational conserving port R
- *θC* — Absolute angular
  displacement of rotational conserving port C

The block applies equal and opposite spring torques on the two rotational conserving
ports. The sign of the spring torque acting on port R is equal to the sign of the
relative angular velocity. A positive relative angular velocity corresponds to a
positive damping torque acting on port R, and a negative damping torque of equal
magnitude acting on port C.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

### Assumptions and Limitations

The value of the spring rate must be greater than zero.
