---
type: simulink-block
title: 'Translational Friction'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'translationalfriction'
documentation_source_path: 'ref/translationalfriction.html'
language: en
---

# Translational Friction

## Ports
```yaml
ports:
- name: R
  summary: Rod mechanical translational
  direction: conserving
- name: C
  summary: Case mechanical translational
  direction: conserving
```

### Conserving

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the rod, that is, the
moving body.

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the case, that is, the
stationary body.
## Parameters
```yaml
parameters:
- name: Breakaway friction force
  summary: Sum of Coulomb and the static frictions 25 N (default) | scalar
  group: ''
- name: Breakaway friction velocity
  summary: Peak velocity for Stribeck friction 0.1 m/s (default) | positive scalar
  group: ''
- name: Coulomb friction force
  summary: Friction that opposes motion 20 N (default) | scalar
  group: ''
- name: Viscous friction coefficient
  summary: Proportionality coefficient 100 N/(m/s) (default) | nonnegative scalar
  group: ''
```

### **Breakaway friction force** — Sum of Coulomb and the static frictions `25 N` (default) | scalar

The breakaway friction force, which is the sum of the Coulomb and the static
frictions. It must be greater than or equal to the **Coulomb friction
force** value.

### **Breakaway friction velocity** — Peak velocity for Stribeck friction `0.1 m/s` (default) | positive scalar

The velocity at which the Stribeck friction is at its peak. At this point, the sum
of the Stribeck and Coulomb friction is the **Breakaway friction
force**. This parameter specifies the velocity threshold, which affects the
tradeoff between the simulation accuracy and speed.

### **Coulomb friction force** — Friction that opposes motion `20 N` (default) | scalar

The Coulomb friction force, which is the friction that opposes motion with a
constant force at any velocity.

### **Viscous friction coefficient** — Proportionality coefficient `100 N/(m/s)` (default) | nonnegative scalar

Proportionality coefficient between the friction force and the relative velocity.
The parameter value must be greater than or equal to zero.
## Libraries

Simscape / Foundation Library / Mechanical / Translational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Friction in contact between moving bodies

The Translational Friction block represents friction in
contact between moving bodies. The friction force is simulated as a function of relative
velocity and is assumed to be the sum of Stribeck, Coulomb, and viscous components, as shown
in the following figure.

The Stribeck friction, *F*S, is the negatively
sloped characteristics taking place at low velocities [1]. The Coulomb friction,
*F*C, results in a constant force at any velocity.
The viscous friction, *F*V, opposes motion with the
force directly proportional to the relative velocity. The sum of the Coulomb and Stribeck
frictions at the vicinity of zero velocity is often referred to as the breakaway friction,
*F*brk. The friction is approximated with the
following equations:

F=2e(Fbrk−FC)⋅exp(−(vvSt)2)⋅vvSt+FC⋅tanh(vvCoul)+fv

vSt=vbrk2

vCoul=vbrk/10

v=vR−vC

where

- *F* is friction force.
- *F*C is Coulomb friction.
- *F*brk is breakaway friction.
- *v*brk is breakaway friction velocity.
- *v*St is Stribeck velocity threshold.
- *v*Coul is Coulomb velocity threshold.
- *v*R and
  *v*C are absolute velocities of ports
  **R** and **C**, respectively.
- *v* is relative velocity.
- *f* is viscous friction coefficient.

The exponential function used in the Stribeck portion of the force equation is continuous
and decays at velocity magnitudes greater than the breakaway friction velocity.

The hyperbolic tangent function used in the Coulomb portion of the force equation ensures
that the equation is smooth and continuous through *v* = 0, but quickly reaches its full value at nonzero velocities.

The block positive direction is from port **R** to port
**C**. This means that if the port **R** velocity is
greater than that of port **C**, the block transmits force from
**R** to **C**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
