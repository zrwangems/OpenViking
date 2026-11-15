---
type: simulink-block
title: 'Rotational Friction'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Rotational Elements'
documentation_page: 'rotationalfriction'
documentation_source_path: 'ref/rotationalfriction.html'
language: en
---

# Rotational Friction

## Ports

### Conserving

### **R** — Rod mechanical rotational

Mechanical rotational conserving port associated with the rod, that is, the moving
body.

### **C** — Case mechanical rotational

Mechanical rotational conserving port associated with the case, that is, the
stationary body.

## Parameters

### **Breakaway friction torque** — Sum of Coulomb and the static frictions `25 N*m` (default) | scalar

The breakaway friction torque, which is the sum of the Coulomb and the static
frictions. It must be greater than or equal to the **Coulomb friction
torque** value.

### **Breakaway friction velocity** — Peak angular velocity for Stribeck friction `0.1 rad/s` (default) | positive scalar

The angular velocity at which the Stribeck friction is at its peak. At this point,
the sum of the Stribeck and Coulomb friction is the **Breakaway friction
torque**. This parameter specifies the velocity threshold, which affects the
tradeoff between the simulation accuracy and speed.

### **Coulomb friction torque** — Friction that opposes rotation `20 N*m` (default) | scalar

The Coulomb friction torque, which is the friction that opposes rotation with a
constant torque at any velocity.

### **Viscous friction coefficient** — Proportionality coefficient `0.001 N*m/(rad/s)` (default) | nonnegative scalar

Proportionality coefficient between the friction torque and the relative angular
velocity. The parameter value must be greater than or equal to zero.

## Libraries

Simscape / Foundation Library / Mechanical / Rotational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Friction in contact between rotating bodies

The Rotational Friction block represents friction in
contact between rotating bodies. The friction torque is simulated as a function of relative
velocity and is assumed to be the sum of Stribeck, Coulomb, and viscous components, as shown
in the following figure.

The Stribeck friction, *T*S, is the negatively
sloped characteristics taking place at low velocities [1]. The Coulomb friction,
*T*C, results in a constant torque at any velocity.
The viscous friction, *T*V, opposes motion with the
torque directly proportional to the relative velocity. The sum of the Coulomb and Stribeck
frictions at the vicinity of zero velocity is often referred to as the breakaway friction,
*T*brk. The friction is approximated with the
following equations:

T=2e(Tbrk−TC)⋅exp(−(ωωSt)2)⋅ωωSt+TC⋅tanh(ωωCoul)+fω

ωSt=ωbrk2

ωCoul=ωbrk/10

ω=ωR−ωC

where

- *T* is friction torque.
- *T*C is Coulomb friction torque.
- *T*brk is breakaway friction torque.
- *ω*brk is breakaway friction velocity.
- *ω*St is Stribeck velocity threshold.
- *ω*Coul is Coulomb velocity threshold.
- *ω*R and
  *ω*C are absolute angular velocities of ports
  **R** and **C**, respectively.
- *ω* is relative velocity.
- *f* is viscous friction coefficient.

The exponential function used in the Stribeck portion of the force equation is continuous
and decays at velocity magnitudes greater than the breakaway friction velocity.

The hyperbolic tangent function used in the Coulomb portion of the force equation ensures
that the equation is smooth and continuous through *ω* = 0, but quickly reaches its full value at nonzero velocities.

The block positive direction is from port **R** to port
**C**. This means that if the port **R** velocity is
greater than that of port **C**, the block transmits torque from
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
