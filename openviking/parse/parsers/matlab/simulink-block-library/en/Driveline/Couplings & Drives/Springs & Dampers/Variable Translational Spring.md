---
type: simulink-block
title: 'Variable Translational Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'variabletranslationalspring'
documentation_source_path: 'ref/variabletranslationalspring.html'
language: en
---

# Variable Translational Spring

## Ports

### Input

### **K** — Variable spring coefficient, N/m physical signal

Physical signal input port associated with variable spring
stiffness.
### Conserving

### **C** — Base port mechanical translational

Mechanical translational conserving port associated with the negative spring end. The
positive direction is from port **R** to port
**C**.

### **R** — Follower port mechanical translational

Mechanical translational conserving port associated with the positive spring end. The
positive direction is from port **R** to port
**C**.

## Parameters

### **Minimum spring rate** — Spring rate limit value `1` `N/m` (default) | positive scalar

Minimum value allowed for the spring rate. The physical signal input
saturates below the specified value.

## Libraries

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Translational spring with variable spring stiffness

The Variable Translational Spring block represents a
translational spring with variable stiffness. A physical signal input port provides the
variable spring stiffness. The magnitude of the spring force is equal to the product of
the physical signal input and the relative linear displacement between the two
translational conserving ports. A minimum spring rate prevents nonphysical
values.

The translational spring force satisfies the following expression:

F={K⋅x,K≥KminKmin⋅x,K<Kmin

where:

- *F* is the force transmitted through the spring between the
  two translational conserving ports.
- *K* is the spring rate coefficient.
- *Kmin* is the minimum allowed spring
  rate.
- *x* is the relative displacement between the two
  translational conserving ports according to x=xinit+xR−xC.
- *xinit* is the initial spring
  deformation.
- *xR* is the absolute displacement of
  the translational conserving port **R**.
- *xC* is the absolute displacement of
  the translational conserving port **C**.

The block applies equal and opposite spring forces on the two translational conserving
ports. The sign of the spring force acting on port **R** is equal to
the sign of the relative linear displacement between the two ports. A positive linear
velocity corresponds to a positive spring force acting on port **R**,
and a negative spring force of equal magnitude acting on port
**C**.

### Assumptions and Limitations

The block limits the value of the variable spring stiffness to remain above zero.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
