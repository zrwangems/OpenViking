---
type: simulink-block
title: 'Bevel Gear Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Gears and Couplings / Gears'
documentation_page: 'bevelgearconstraint'
documentation_source_path: 'ref/bevelgearconstraint.html'
language: en
---

# Bevel Gear Constraint

## Ports

### Frame

### **B** — Base frame frame

Connection frame on the base bevel gear.

### **F** — Follower frame frame

Connection frame on the follower bevel gear.

## Parameters

### **Base Gear Radius** — Radius of the base gear pitch circle `10` `cm` (default) | positive scalar with units of length

Radius of the base gear pitch circle. The pitch circle is concentric with
the gear and tangent to the tooth contact points. The gear radii impact the
torque transmission between the base and follower gear bodies.

### **Follower Gear Radius** — Radius of the follower gear pitch circle `10` `cm` (default) | positive scalar with units of length

Radius of the follower gear pitch circle. The pitch circle is concentric
with the gear and tangent to the tooth contact points. The gear radii impact
the torque transmission between the base and follower gear bodies.

### **Shaft Axes** — Parameterization for the gear shaft angle `Perpendicular` (default) | `Arbitrarily Oriented`

Parameterization for the intersection angle between the bevel gear shafts.
Select `Perpendicular` to align the gear shafts at
a right angle. Select `Arbitrarily Oriented` to
align the gear shafts at any angle from `0` to
`180`
`deg`.

### **Angle Between Shafts** — Angle between the base and follower shafts `90` `deg` (default) | positive scalar

Angle between the imaginary lines extending from the base and follower
frame z-axes. The angle must in the range of
`0`–`180`
`deg`. The actual angle between the base and follower
gears, typically set through rigid transforms, joints, and occasionally
other constraints, must be the same as that specified here.

#### Dependencies

This parameter is enabled when the **Shaft Axes**
parameter is set to `Arbitrarily
Oriented`.

## Libraries

Simscape / Multibody / Gears and Couplings / Gears

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Kinematic constraint between two bevel gear bodies with angled intersecting rotation axes

The Bevel Gear Constraint block represents a kinematic constraint
between two gear bodies with intersecting rotation axes held at a specified angle. The
base and follower frame ports identify the connection frames on the gear bodies. The
gear rotation axes coincide with the connection frame *z*-axes. The
gears rotate at a fixed velocity ratio determined by the gear pitch
radii.

The block represents only the kinematic constraint characteristic to a bevel gear
system. Gear inertia and geometry are solid properties that you must specify using solid
blocks. The gear constraint model is ideal. Backlash and gear losses due to Coulomb and
viscous friction between teeth are ignored. You can, however, model viscous friction at
joints by specifying damping coefficients in the joint blocks.

### Gear Geometry

The bevel gear constraint is parameterized in terms of the dimensions of the gear
pitch circles. The pitch circles are imaginary circles concentric with the gear
bodies and tangent to the tooth contact point. The pitch radii, labeled
`RB` and
`RF` in the figure, are the outer
radii that the gears would have if they were reduced to friction cones in mutual
contact.

### Gear Assembly

Gear constraints occur in closed kinematic loops. The figure shows the closed-loop
topology of a simple bevel gear model. Joint blocks connect the gear bodies to a
common fixture or carrier, defining the maximum degrees of freedom between them. A
Bevel Gear Constraint block connects the gear bodies, eliminating
one degree of freedom and effectively coupling the gear motions.

### Assembly Requirements

The block imposes special restrictions on the relative positions and orientations
of the gear connection frames. The restrictions ensure that the gears assemble only
at distances and angles suitable for meshing. The block enforces the restrictions
during model assembly, when it first attempts to place the gears in mesh, but relies
on the remainder of the model to keep the gears in mesh during simulation.

**Position Restrictions**

- The distance between the base and follower frame origins must be such
  that, at the given shaft angle and pitch radii, the gear pitch circles
  are tangent to each other. This distance, denoted
  *d*B-F, follows from the law
  of cosines:

  dB−F=RB2+RF2−2RBRFcos(π−θ),

  where *R*B is
  the pitch radius of the base gear,
  *R*F is the pitch radius of
  the follower gear, and *θ*Shaft
  is the intersection angle between the rotation axes.
- The distance between the base and follower frame origins along the
  *z*-axis of the base frame, denoted
  *Δz*B, must be equal to:

  ΔzB=RF·sin(θShaft)
- The distance between the base and follower frame origins along the
  *z*-axis of the follower frame, denoted
  *Δz*F, must be equal to:

  ΔzF=RB·sin(θShaft)

**Orientation Restrictions**

- The imaginary lines extending from the base and follower z-axes must
  intersect at the shaft angle set in the block dialog box. The angle is
  denoted θB-F in the figure. If the
  **Shaft Axes** parameter is set to
  `Perpendicular`, the angle is
  90°.
