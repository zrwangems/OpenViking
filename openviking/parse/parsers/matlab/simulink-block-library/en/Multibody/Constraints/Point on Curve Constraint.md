---
type: simulink-block
title: 'Point on Curve Constraint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Constraints'
documentation_page: 'pointoncurveconstraint'
documentation_source_path: 'ref/pointoncurveconstraint.html'
language: en
---

# Point on Curve Constraint

## Ports

### Geometry

### **B** — Base frame frame

Geometry port associated with the curve defined by the Spline block.
### Frame

### **F** — Follower frame frame

Follower frame whose origin is confined to the curve connected to port
**B**.
### Output

### **f** — Constraint force vector

Constraint force that acts between the point and curve, returned as a
vector. See Measure Joint Constraint Forces for more information. If you set the
 **Resolution Frame**  parameter to
`Base`, the sensed force is with respect to
the reference frame of the curve connected to port
**B**.

#### Dependencies

To enable this port, under **Constraint Force/Torque
Sensing**, select **Force
Vector**.

### **t** — Constraint torque vector

Constraint torque that acts between the point and curve, returned as a
vector. See Force and Torque Sensing for more information. If you set the
 **Resolution Frame**  parameter to
`Base`, the sensed torque is with respect
to the reference frame of the curve connected to the port
**B**.

#### Dependencies

To enable this port, under **Constraint Force/Torque
Sensing**, select **Torque
Vector**.

## Parameters

### **Direction** — Measurement direction `Follower on Base` (default) | `Base on Follower`

Direction in which to measure the constraint force and torque. Reversing
this direction changes the sign of the measurements. See Force and Torque Measurement Direction for more information.

### **Resolution Frame** — Frame to resolve measurements `Base` (default) | `Follower`

Frame used to resolve the measured vector quantities. See Selecting a Measurement Frame for more information.

### **Force Vector** — Whether to sense constraint force `off` (default) | `on`

Select this parameter to expose port **f**, which outputs
the constraint force vector between the **B** and
**F** frames.

### **Torque Vector** — Whether to sense constraint torque `off` (default) | `on`

Select this parameter to expose port **t**, which outputs
the constraint torque vector between the **B** and
**F** frames.

## Libraries

Simscape / Multibody / Constraints

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Kinematic constraint between frame origin and curved path

The Point on Curve Constraint block confines a point to
a curve. The frame attached to the point is free to rotate depending on other
constraints in the model. Use the Point on Curve
Constraint block to model point-on-curve constraints, such as that
between a roller coaster and a track or a cam follower and a cam.

Examples of Point-on-Curve Constraints

The Point on Curve Constraint block has two ports:
**F** and **B**. Port **F** is a
frame port whose origin corresponds to the point. Port **B** is a
geometry port that you connect to a curve. Avoid curves with sharp changes in slope, as
these can cause simulation issues.

You can use this block to sense the constraint forces and torques between the point
and curve. Based on the setting of the **Resolution Frame** parameter,
the block resolves the forces and torques in either the base or follower frame.
