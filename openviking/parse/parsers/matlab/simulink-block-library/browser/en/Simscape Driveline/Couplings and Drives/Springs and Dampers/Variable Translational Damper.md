---
type: simulink-block
title: 'Variable Translational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Couplings and Drives / Springs and Dampers'
documentation_page: 'variabletranslationaldamper'
documentation_source_path: 'ref/variabletranslationaldamper.html'
language: en
---

# Variable Translational Damper

## Ports

`B`
:   Physical signal input port representing the variable translational damping
    coefficient.

`C`
:   Translational conserving port.

`R`
:   Translational conserving port.

## Parameters

**Minimum damping coefficient**
:   Minimum value allowed for the variable damping coefficient. The physical
    signal input saturates below the specified value. The parameter must be
    greater than or equal to zero. The default value is `0`
    `N/(m/s)`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Translational viscous damper with variable damping coefficient

The block represents a translational viscous damper with variable damping coefficient.
A physical signal input port provides the magnitude of the translational damping
coefficient. The magnitude of the damping force is equal to the product of the physical
signal input and the relative linear velocity between the two translational conserving
ports. A minimum damping coefficient prevents non-physical negative damping values.

The translational damping force satisfies the following expression:

F={B.v,B≥BminBmin⋅v,B<Bmin,

The parameters are:

- *F* — Force transmitted through the translational
  damper between the two translational conserving ports
- *B* — Viscous damping coefficient
- *Bmin* — Minimum allowed
  damping coefficient
- *v* — Relative linear velocity measured between the
  two translational conserving ports
- *vR* — Linear velocity of port
  R
- *vC* — Linear velocity of port
  C

The block applies equal and opposite damping forces on the two translational
conserving ports. The sign of the damping force acting on port R is equal to the sign of
the relative linear velocity. A positive linear velocity corresponds to a positive
damping force acting on port R, and a negative damping force of equal magnitude acting
on port C.

### Assumptions and Limitations

- The block represents strictly viscous damping.
- The value of the damping coefficient must be greater than or equal to
  zero.
