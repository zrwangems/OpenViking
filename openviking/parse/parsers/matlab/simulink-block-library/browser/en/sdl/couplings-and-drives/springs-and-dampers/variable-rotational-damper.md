---
type: simulink-block
title: 'Variable Rotational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Couplings and Drives / Springs and Dampers'
documentation_page: 'variablerotationaldamper'
documentation_source_path: 'ref/variablerotationaldamper.html'
language: en
---

# Variable Rotational Damper

## Ports

### Input

### **B** — Variable damping coefficient physical signal

Physical signal input port associated with the variable damping coefficient.
### Conserving

### **C** — Base port rotational mechanical

Rotational mechanical conserving port associated with the base.

### **R** — Follower port rotational mechanical

Rotational mechanical conserving port associated with the follower.

## Parameters

### **Minimum damping coefficient** — Damping limit value `0` `N*m/(rad/s)` (default) | nonnegative scalar

Minimum value allowed for the damping coefficient. The physical signal
input saturates below this level.

## Libraries

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Rotational damper with variable damping coefficient

The Variable Rotational Damper block represents a rotational
viscous damper with a variable damping coefficient. A physical signal input port
provides the magnitude of the damping coefficient. The magnitude of the damping torque
is equal to the product of the physical signal input and the relative angular velocity
between the two rotational conserving ports, **R** and
**C**. A minimum damping coefficient prevents nonphysical negative
damping values.

The damping torque satisfies the following expression:

T={B⋅ωB≥BminBmin⋅ωB<Bmin,

where

- *T* is the torque transmitted through damper.
- *B* is the viscous damping coefficient.
- *ω* is the relative angular velocity measured between the two
  rotational conserving ports according to ω=ωR−ωC.
- *ωR* is the angular velocity of the
  rotational conserving port **R**.
- *ωC* is the angular velocity of the
  rotational conserving port **C**.

The block applies equal and opposite damping torques on the rotational conserving ports. The
sign of the damping torque acting on port **R** is equal to the sign of
the relative angular velocity. A positive relative angular velocity corresponds to a
positive damping torque acting on port **R**, and a negative damping
torque of equal magnitude acting on port **C**.

### Assumptions and Limitations

- The block represents only viscous damping.
- The value of the damping coefficient must be equal to or greater than
  zero.
