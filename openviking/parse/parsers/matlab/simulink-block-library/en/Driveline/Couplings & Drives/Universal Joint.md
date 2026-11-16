---
type: simulink-block
title: 'Universal Joint'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'universaljoint'
documentation_source_path: 'ref/universaljoint.html'
language: en
---

# Universal Joint

## Ports

### Conserving

### **B** — Base shaft mechanical rotational

Conserving rotational port associated with the base shaft.

### **F** — Follower shaft mechanical rotational

Conserving rotational port associated with the follower shaft.
### Input

### **A** — Intersection angle physical signal

Physical signal input port for the intersection angle.

## Parameters

j

### **Maximum joint angle** — Maximum joint intersection angle, *A* `pi/4` `rad` (default) | 0 ≤ *A* < pi/2 | scalar

Maximum intersection angle the joint allows. This angle measures the
rotation between base and follower shafts about the base shaft pin. The
value of this angle must fall in the range 0≤A<pi/2 rad.

### **Joint compliance** — Compliance model `off` (default) | `on`

Compliance model for the block:

- `off` — Do not model stiffness
  and damping.
- `on` — Model stiffness and
  damping.

### **Joint stiffness** — Stiffness coefficient, k `1e6` `N*m/rad` (default) | scalar

Linear spring stiffness of the joint in terms of the follower-shaft
component of the angular velocity ratio. The spring stiffness accounts for
elastic energy storage in the joint due to material compliance.

#### Dependencies

To enable this parameter, select **Joint
compliance**.

### **Joint damping** — Damping coefficient, b `1e3` `N*m/(rad/s)` (default) | scalar

Linear damping coefficient of the joint in terms of the follower-shaft
component of the angular velocity ratio. The damping coefficient accounts
for energy dissipation in the joint due to material compliance.

#### Dependencies

To enable this parameter, select **Joint
compliance**.

### **Initial base shaft angle** — Initial base shaft angle `0` `rad` (default) | scalar

Rotation angle of the base shaft about its length axis at the beginning of
simulation.

### **Initial torque from base to follower shaft** — Initial torque `0` `N*m` (default) | scalar

Torque that the base shaft transfers to the follower shaft at the
beginning of simulation. This torque determines the initial state of
material compliance at the joint. Set this value to greater than zero to
preload the shafts with torque. Changing this value alters the initial
transient response due to material compliance.

#### Dependencies

To enable this parameter, select **Joint
compliance**.

## Libraries

Simscape / Driveline / Couplings & Drives

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2025a: Enumeration Updates

The **Joint compliance** parameter now uses a check box. This
parameter used a drop down in previous releases.

## Description

Rotational coupling between two driveline shafts

The Universal Joint block represents a rotational
coupling between two driveline shafts. The coupling transfers torque between the shafts
so they spin as a unit under an applied load. Two rotational degrees of freedom,
internal to the coupling, allow the shafts to connect at an angle. This intersection
angle varies according to the physical signal input from port **A**.
Optional compliance, modeled as a parallel spring-damper set, allows the coupling to
deform under load.

You can use the Universal Joint block as a connection
between two rotational driveline components, for example, between the driving and driven
shafts in an automobile drive train.

The ratio of the shaft angular velocities depends on two parameters: the intersection
angle between the two shafts and the rotation angle of the base shaft. A physical signal
input provides the intersection angle while a property inspector parameter provides the
initial base shaft angle. These two angles fix the ratio of the two shaft angular
velocities according to the nonlinear equation:

ωF=cos(A)1−sin2(A)⋅cos2(θB)ωB,

where:

- *ωF* and
  *tF* are the angular
  velocity and torque of the follower shaft about its length axis,
  respectively.
- *ωB* and
  *tB* are the angular
  velocity and torque of the base shaft about its length axis,
  respectively.
- *θB* is the rotation angle of the
  base shaft about its length axis.
- *A* is the intersection angle between base and follower
  shafts about the base shaft pin.

The two schematics in the figure illustrate the equation parameters. In
each schematic, the left shaft represents the base shaft, while the right shaft
represents the follower shaft. The right schematic shows the coupling seen in the left
schematic after the shafts spin 90° about their length axes (dashed line
segments).

In the figure, the intersection angle is the angle between the two
shafts about the pin of the base shaft. The absolute value of this angle must fall in
the range `0 ≤ A < Maximum intersection angle`. The base shaft angle
is the angle of the base shaft about its length axis. The base shaft angle is also the
time-integral of the base shaft angular velocity,
*ωB*.

### Compliance

You can incorporate the effects of compliance in the universal joint torque
transfer. When you clear **Joint compliance**,

ωF=cos(A)1−sin2(A)⋅cos2(θB)ωBtB=−cos(A)1−sin2(A)⋅cos2(θB)tF

When you select **Joint compliance**,

θC=θF−cos(A)1−sin2(A)⋅cos2(θB)θBtB=−cos(A)1−sin2(A)⋅cos2(θB)tFtF=bωC+kθC

where:

- *k* is the value of the **Joint
  stiffness** parameter.
- *b* is the value of the **Joint
  damping** parameter.
- *θC* is the torsional
  compliance angle.
- *ωC* is the torsional
  compliance angular velocity.
