---
type: simulink-block
title: 'Worm and Gear Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Gears and Couplings / Gears'
documentation_page: 'wormandgearconstraint'
documentation_source_path: 'ref/wormandgearconstraint.html'
language: en
---

# Worm and Gear Constraint

## Ports
```yaml
ports:
- name: B
  summary: Base frame frame
  direction: unspecified
- name: F
  summary: Follower frame frame
  direction: unspecified
```

### Frame

### **B** — Base frame frame

Connection frame on the worm body.

### **F** — Follower frame frame

Connection frame on the gear body.
## Parameters
```yaml
parameters:
- name: Worm Direction
  summary: Winding direction of the worm thread Right-Hand (default) | Left-Hand
  group: ''
- name: Worm Lead Angle
  summary: Angle between the worm thread and rotation plane 10 deg (default) | positive scalar between 0 and 180 in units
    of angle
  group: ''
- name: Specification Method
  summary: Gear geometry parameterization Center Distance and Ratio (default) | Pitch Circle Radii
  group: ''
- name: Center Distance
  summary: Distance between the worm and gear centers 20 cm (default) | positive scalar in units of length
  group: ''
- name: Ratio (Ng/Nw)
  summary: Ratio of gear teeth to worm threads 1 (default) | positive unitless scalar
  group: ''
- name: Worm Radius
  summary: Radius of the worm pitch circle 10 cm (default) | positive scalar in units of length
  group: ''
- name: Gear Radius
  summary: Radius of the gear pitch circle 10 cm (default) | positive scalar in units of length
  group: ''
```

### **Worm Direction** — Winding direction of the worm thread `Right-Hand` (default) | `Left-Hand`

Winding direction of the worm thread relative to the base frame z-axis. As
viewed from the base frame origin, a right-hand thread is one that wraps
around the base frame z-axis in a counterclockwise direction. A left-hand
thread is one that wraps in a clockwise direction. This parameter determines
the relative directions of motion of the worm and gear bodies.

### **Worm Lead Angle** — Angle between the worm thread and rotation plane `10` `deg` (default) | positive scalar between `0` and `180` in units of angle

Angle between the tangent to the worm thread and the plane perpendicular
to the base frame z-axis. The lead angle impacts the gear rotation
corresponding to a full worm revolution.

### **Specification Method** — Gear geometry parameterization `Center Distance and Ratio` (default) | `Pitch Circle Radii`

Parameterization for specifying the worm and gear geometries. You can
specify the gear dimensions in terms of the distance between the gear
centers or the individual gear radii.

### **Center Distance** — Distance between the worm and gear centers `20` `cm` (default) | positive scalar in units of length

Distance between the worm and gear centers. This distance must equal that
enforced by rigid transforms, joints, and any other constraints located
between the gear bodies and the common carrier body.

#### Dependencies

This parameter is enabled when the **Specification
Method** parameter is set to `Center Distance
and Ratio`.

### **Ratio (Ng/Nw)** — Ratio of gear teeth to worm threads `1` (default) | positive unitless scalar

Ratio of gear teeth to worm threads, or *starts*. This
ratio impacts the torque transmitted between the worm and gear.

#### Dependencies

This parameter is enabled when the **Specification
Method** parameter is set to `Center Distance
and Ratio`.

### **Worm Radius** — Radius of the worm pitch circle `10` `cm` (default) | positive scalar in units of length

Radius of the worm pitch circle. This is the distance between the worm
rotation axis and the tooth-thread contact point. This parameter impacts the
torque transmitted between the worm and gear.

#### Dependencies

This parameter is enabled when the **Specification
Method** parameter is set to `Pitch Circle
Radius`.

### **Gear Radius** — Radius of the gear pitch circle `10` `cm` (default) | positive scalar in units of length

Radius of the gear pitch circle. This is the distance between the gear
rotation axis and the tooth-thread contact point. This parameter impacts the
torque transmitted between the worm and gear.

#### Dependencies

This parameter is enabled when the **Specification
Method** parameter is set to `Pitch Circle
Radius`.
## Libraries

Simscape / Multibody / Gears and Couplings / Gears

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Kinematic constraint between worm and gear bodies with perpendicular non-intersecting rotation axes

The Worm and Gear Constraint block represents a kinematic constraint
between worm and gear bodies held at a right angle. The base frame port identifies the
connection frame on the worm and the follower frame port identifies the connection frame
on the gear. The rotation axes coincide with the connection frame
*z*-axes. The worm and gear rotate at a fixed velocity ratio determined
by the gear pitch radii or tooth-thread ratio.

The worm thread direction can follow either right-hand or left-hand conventions. The
convention used determines the relative directions of the worm and gear rotational
velocities. A right-hand convention causes the worm and gear to rotate in the same
direction about the respective z-axes. A left-hand convention causes the worm and gear
to rotate in opposite directions instead.

The block represents only the kinematic constraint characteristic to a worm-and-gear
system. Gear inertia and geometry are solid properties that you must specify using solid
blocks. The gear constraint model is ideal. Backlash and gear losses due to Coulomb and
viscous friction between teeth are ignored. You can, however, model viscous friction at
joints by specifying damping coefficients in the joint blocks.

### Gear Geometry

The rack-and-pinion constraint is parameterized in terms of the dimensions of the
worm and gear pitch circles. The pitch circles are imaginary circles concentric with
the worm and gear bodies and tangent to the thread contact point. The pitch radii,
labeled `RB` and
`RF` in the figure, are the radii
that the worm and gear would have if they were reduced to friction cylinders in
mutual contact.

### Gear Assembly

Gear constraints occur in closed kinematic loops. The figure shows the closed-loop
topology of a simple worm-and-gear model. Joint blocks connect the worm and gear
bodies to a common fixture or carrier, defining the maximum degrees of freedom
between them. A Worm and Gear Constraint block connects the worm and
gear bodies, eliminating one degree of freedom and effectively coupling the worm and
gear motions.

### Assembly Requirements

The block imposes special restrictions on the relative positions and orientations
of the gear connection frames. The restrictions ensure that the gears assemble only
at distances and angles suitable for meshing. The block enforces the restrictions
during model assembly, when it first attempts to place the gears in mesh, but relies
on the remainder of the model to keep the gears in mesh during simulation.

**Position Restrictions**

- The distance between the base and follower frame
  *z*-axes, denoted dB-F in the
  figure, must be equal to the distance between the gear centers.
- The translational offset between the base and follower frame origins
  along the follower frame *z*-axis, denoted
  ΔZF in the figure, must be zero.

**Orientation Restrictions**

- The *z*-axes of the base and follower frames must be
  perpendicular to each other. The *z*-axes are shown in
  blue in the figure.
- The cross product of the follower frame *z*-axis with
  the base frame *z*-axis must be a vector aimed from the
  follower frame origin to the base frame *z*-axis. The
  *z*-axes and their cross-product vector are shown
  in the figure. The cross product is defined as z^F×z^B.
