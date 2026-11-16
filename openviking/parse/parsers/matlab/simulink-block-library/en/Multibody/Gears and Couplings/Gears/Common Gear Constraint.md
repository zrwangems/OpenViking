---
type: simulink-block
title: 'Common Gear Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Gears and Couplings / Gears'
documentation_page: 'commongearconstraint'
documentation_source_path: 'ref/commongearconstraint.html'
language: en
---

# Common Gear Constraint

## Ports

### Frame

### **B** — Base frame frame

Connection frame on the base gear body.

### **F** — Follower frame frame

Connection frame on the follower gear body.

## Parameters

### **Type** — Type of meshing between the base and follower gear bodies `External` (default) | `Internal`

Type of meshing between the base and follower gear bodies. Select
`External` if both gears have outward-facing
teeth. Select `Internal` if one gear has
inward-facing teeth. Such a gear is known as a ring gear. The gear with the
greater pitch radius serves as the ring gear.

### **Center Distance** — Distance between the base and follower gear centers `20` `cm` (default) | positive scalar in units of length

Distance between the centers of the base and follower gear bodies. This
distance is the sum of the base and follower gear pitch radii.

#### Dependencies

This parameter is enabled when the **Specification
Method** parameter is set to `Center Distance
and Ratio`.

### **Gear Ratio (Nf/Nb)** — Ratio of follower gear teeth to base gear teeth `1.0` (default) | unitless positive scalar

Number of follower gear teeth divided by the number of base gear teeth.
The block uses this ratio to determine the speed and torque transmitted
between the base and follower gear shafts.

#### Dependencies

This parameter is enabled when the **Specification
Method** parameter is set to `Center Distance
and Ratio`.

### **Base Gear Radius** — Radius of the pitch circle of the base gear body `10` `cm` (default) | positive scalar in units of length

Radius of the pitch circle of the base gear body. The pitch circle is an
imaginary circle concentric with the gear body and tangent to the tooth
contact point.

#### Dependencies

This parameter is enabled when the **Specification
Method** parameter is set to `Pitch Circle
Radii`.

### **Follower Gear Radius** — Radius of the pitch circle of the follower gear body `10` `cm` (default) | positive scalar in units of length

Radius of the pitch circle of the follower gear body. The pitch circle is
an imaginary circle concentric with the gear body and tangent to the tooth
contact point.

#### Dependencies

This parameter is enabled when the **Specification
Method** parameter is set to `Pitch Circle
Radii`.

## Libraries

Simscape / Multibody / Gears and Couplings / Gears

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Kinematic constraint between two coplanar spur gear bodies with parallel rotation axes

The Common Gear Constraint block represents a kinematic constraint
between two coplanar spur gear bodies with parallel rotation axes. The gear meshing can
be external to both gears or internal to one of the gears. The base and follower frame
ports identify the connection frames on the spur gear bodies. The gear rotation axes
coincide with the frame *z*-axes.

The block represents only the kinematic constraint characteristic to a spur gear
system. Gear inertia and geometry are solid properties that you must specify using solid
blocks. The gear constraint model is ideal. Backlash and gear losses due to Coulomb and
viscous friction between teeth are ignored. You can, however, model viscous friction at
joints by specifying damping coefficients in the joint blocks.

### Gear Geometry

The common gear constraint is parameterized in terms of the dimensions of the gear
pitch circles. A pitch circle is an imaginary circle concentric with the gear body
and tangent to the tooth contact point. The pitch radii, labeled
`RB` and
`RF` in the figure, are the radii
that the gears would have if they were reduced to friction cylinders in mutual contact.

### Gear Assembly

Gear constraints occur in closed kinematic loops. The figure shows the closed-loop
topology of a simple common gear model. Joint blocks connect the gear bodies to a
common fixture or carrier, defining the maximum degrees of freedom between them. A
Common Gear Constraint block connects the gear bodies,
eliminating one degree of freedom and effectively coupling the two gear
motions.

### Assembly Requirements

The block imposes special restrictions on the relative positions and orientations
of the gear connection frames. The restrictions ensure that the gears assemble only
at distances and angles suitable for meshing. The block enforces the restrictions
during model assembly, when it first attempts to place the gears in mesh, but relies
on the remainder of the model to keep the gears in mesh during simulation.

**Position Restrictions**

- The distance between the *z*-axes of the base and
  follower frame, denoted *d*B-F
  in the figure, must equal the distance between the gear centers. This
  constraint ensures that the rotation axes of the gears are at the proper
  distance for meshing.
- The follower frame origin must lie on the *xy* plane
  of the base frame. This constraint ensures that the pitch circle of one
  gear is coplanar with the pitch circle of the other.

**Orientation Restrictions**

- The *z*-axes of the base and follower frames must
  point in the same direction. This constraint ensures that the gear
  rotation axes are parallel to each other. The figure shows the
  *z*-axes of the base and follower frames pointing
  out of the screen.
