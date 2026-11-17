---
type: simulink-block
title: 'Point on Surface Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Constraints'
documentation_page: 'pointonsurfaceconstraint'
documentation_source_path: 'ref/pointonsurfaceconstraint.html'
language: en
---

# Point on Surface Constraint

## Ports
```yaml
ports:
- name: B
  summary: Base frame frame
  direction: output
- name: F
  summary: Follower frame frame
  direction: output
- name: f
  summary: Constraint force vector
  direction: output
- name: t
  summary: Constraint torque vector
  direction: output
```

### Geometry

### **B** — Base frame frame

Geometry port associated with the constraint surface specified by blocks like the
Infinite
Plane block.
### Frame

### **F** — Follower frame frame

Follower frame whose origin is confined to the 2-D surface connected to the port
**B** of the Point on Surface
Constraint block. The origin of the follower frame
moves on the 2-D surface and has five degrees of freedom (three
rotational and two translational).
### Output

### **f** — Constraint force vector

Constraint force that acts between the point and surface, returned as a vector. See
Measure Joint Constraint Forces for more information. If you set the
 **Resolution Frame**  parameter to
`Base`, the sensed force is with respect to
the reference frame of the surface that connects to port
**B**.

#### Dependencies

To enable this port, under **Constraint Force/Torque Sensing**, select
**Force Vector**.

### **t** — Constraint torque vector

Constraint torque that acts between the point and surface, returned as a vector. See
Force and Torque Sensing for more information. If you set the
 **Resolution Frame**  parameter to
`Base`, the sensed torque is with respect
to the reference frame of the surface that connects to the port
**B**.

#### Dependencies

To enable this port, under **Constraint Force/Torque Sensing**, select
**Torque Vector**.
## Parameters
```yaml
parameters:
- name: Direction
  summary: Measurement direction Follower on Base (default) | Base on Follower
  group: ''
- name: Resolution Frame
  summary: Frame to resolve measurements Base (default) | Follower
  group: ''
- name: Force Vector
  summary: Whether to sense constraint force off (default) | on
  group: ''
- name: Torque Vector
  summary: Whether to sense constraint torque off (default) | on
  group: ''
```

### **Direction** — Measurement direction `Follower on Base` (default) | `Base on Follower`

Direction in which to measure the constraint force and torque. Reversing this direction
changes the sign of the measurements. See Force and Torque Measurement Direction for more information.

### **Resolution Frame** — Frame to resolve measurements `Base` (default) | `Follower`

Frame used to resolve the measured vector quantities. See Selecting a Measurement Frame for more information.

### **Force Vector** — Whether to sense constraint force `off` (default) | `on`

Select this parameter to expose the port **f**, which
outputs the constraint force vector between **B** and
**F** frames.

### **Torque Vector** — Whether to sense constraint torque `off` (default) | `on`

Select this parameter to expose the port **t**, which
outputs the constraint torque vector between **B** and
**F** frames.
## Libraries

Simscape / Multibody / Constraints

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Kinematic constraint between frame origin and 2-D surface

The Point on Surface Constraint block confines a point to a
2-D surface. The frame attached to the point has five degrees of freedom (three
rotational and two translational). This animation shows an example of using the
Point on Surface Constraint block to constrain one
vertex of a brick to a plane. The vertex translates and rotates on the plane. Note that
the gravity is in the -*Z* direction, and there is no contact between
the brick and plane.

Point on Surface Constraint Example

The Point on Surface Constraint block has two ports:
**F** and **B**. Port **F** is a
frame port whose origin corresponds to the point. Port **B** is a
geometry port that you connect to the geometry of a 2-D surface. Currently, the
Point on Surface Constraint block supports only the
Infinite
Plane block.

You can use this block to sense the constraint forces and torques between the point and 2-D
surface. The forces and torques are resolved in either the base or follower frame, based
on the setting of the **Resolution Frame** parameter.
