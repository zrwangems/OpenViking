---
type: simulink-block
title: 'Belt-Cable Spool'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Belts and Cables'
documentation_page: 'beltcablespool'
documentation_source_path: 'ref/beltcablespool.html'
language: en
---

# Belt-Cable Spool

## Ports

### Frame

### **R** — Local reference frame frame

Reference frame for attachment of the spool to the remainder of a
multibody model.
### Belt-Cable

### **A** — Spool cable attachment point belt-cable

Point of tangency between the center line of the cord and pitch circle
of the spool.

## Parameters

### **Pitch Radius** — Distance from the center of the spool to the center line of the cord `10 cm` (default) | positive scalar in units of length

Distance from the center of the spool to the running axis of the cord
measured in the arc within which contact occurs. In compound pulley systems,
the differences in pitch radii often determine the ratio at which speed is
reduced or torque is augmented.

### **Sensing** — Selection of kinematic variables to sense `Unchecked` (default) | Checked

Selection of kinematic variables to sense. Select a check box to expose a
physical signal port for the corresponding variable. The variables available
for sensing are:

- **Spool Angle A** — Angle, measured in the
  *xy* plane of the reference frame, from the
  local *x*-axis to the line between the frame
  origin and point of contact **A**.

  If the point of contact is above the
  *xz*-plane (in the +*y*-region
  of the reference frame), the angle is positive. If the point of
  contact is below the *xz*-plane, the angle is
  negative. The angle is zero when the point of contact happens to
  be exactly in the *xz*-plane.

  The angle is not modular. Rather than be constrained to a
  360-degree range—snapping back to the beginning of the range
  after completing a turn—the measured value changes continuously
  with repeated turns. Every turn that the drum makes adds (or
  subtracts) 2π to the measurement.

  Use port **qpa** for this measurement.
- **Fleet Angle A** — Angle from the
  *xy*-plane of the reference frame to the
  cord at point of contact **A**. The
  *xy*-plane is the same as the center plane
  of the drum.

  If the cord approaches the point of contact from above the
  *xy*-plane (in the +*z*
  region of the reference frame), the angle is positive. If the
  cord approaches from below, the angle is negative. The angle is
  zero when the cord approaches the point of contact in the center
  plane of the drum.

  The angle is modular, which is to say that its value is
  bound—here, between -π/2 to +π/2. This range is open. The measured value can
  vary between -π/2 and +π/2, but it cannot hit either limit.

  Note that if the **Drum Belt-Cable
  Alignment** parameter of the Belt-Cable Properties block is set to
  `Monitored Planar`, the pulley
  assembly is required to be planar, and the fleet angle is
  therefore always zero. To model a nonplanar assembly, use the
  default setting for that parameter:
  `Unrestricted`.

  Use port **qfa** for this measurement.

## Libraries

Simscape / Multibody / Belts and Cables

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Source and sink of cord in a pulley system

The Belt-Cable Spool block represents a cylindrical drum on which to
wind (and from which to unwind) the cord of a pulley system. The spool marks an end to
the cord and the point at which a motor or other power source often pulls on a load. A
Belt-Cable
End block generally marks the second tip of the cord, to which the
load itself is commonly attached. Depending on whether it is winding or unwinding, the
spool can behave as an infinite source of cord or as an infinite sink of the
same.

The spool serves as an interface between the belt-cable domain specific to pulley
systems and the frame domain general to all other multibody components. The belt-cable
port (**A**) identifies the tip of the cord to be wound on the spool
and the relative placement of that tip within a pulley system. A frame port
(**R**) identifies the reference frame of the spool and its
placement in the broader multibody model.

The degrees of freedom of the spool are a function of the joint by which the spool
connects to other components. It is common for a revolute joint to provide those degrees
of freedom; they reduce in this case to rotation about a single axis (that of the
spool). Actuation inputs, specified directly through the joint by means of torque or
motion signals, serve to drive the spool and to wind (or unwind) the cord.

The cord enters and exits the drum in tangency with the drum circumference. Consistent
with the right-hand rule, the winding is in a counterclockwise direction about the
rotation axis of the drum. This axis is by definition the *z*-axis of
the local reference frame (**R**). To reverse the direction of the
winding, you must flip the local reference frame so that the *z*-axis
points in the opposite direction—for example, by the application of a frame rotation
through a Rigid
Transform block.

The surface of the spool (smooth or grooved) is not considered in the model. In
addition, the cord is assumed to wrap around the spool in a circle that is of constant
radius (that of the *pitch* circle) and coplanar with the transverse
cross section of the winch. Changes in spool radius due to winding are ignored.

By default, the cord can enter and exit a spool at an angle to its center plane
(*θ* in the figure). This angle can vary during simulation—for
example, due to translation of the spool on a prismatic joint. While the contact point
is always in the center plane of the spool, the spool can move when mounted on a joint.
The cord can also be constrained to enter and exit the spool in its center plane.
Whether this constraint is enforced depends on the settings of the Belt-Cable
Properties block.

The inertia of the spool and of the cord wound on it are also ignored. To capture the
inertia of a spool of fixed mass, use the Cylindrical
Solid or Inertia block. Consider the Cylindrical
Solid block if solid geometry is important in the model. To capture
the variable mass properties of a cord as it winds on, and unwinds from, the spool, use
a block from the Variable Solids library—for example Variable Cylindrical
Solid or General Variable Mass.
