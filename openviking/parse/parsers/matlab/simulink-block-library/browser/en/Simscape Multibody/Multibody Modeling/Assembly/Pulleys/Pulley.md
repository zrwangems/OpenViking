---
type: simulink-block
title: 'Pulley'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Assembly / Pulleys'
documentation_page: 'pulley'
documentation_source_path: 'ref/pulley.html'
language: en
---

# Pulley

## Ports

### Frame

### **R** — Local reference frame frame

Reference frame by which to connect the pulley to the frame network of
a multibody model.
### Belt-Cable

### **A** — Pulley cord tangency point belt-cable

Point of tangency between the center line of the cord and the pitch
circle of the pulley. The cord wraps around the pulley counterclockwise
from port **A** to port **B**.

### **B** — Pulley cord tangency point belt-cable

Point of tangency between the center line of the cord and the pitch
circle of the pulley. The cord wraps around the pulley counterclockwise
from port **A** to port **B**.

## Parameters

### **Pitch Radius** — Distance from the center of the pulley to the center line of the cord `10 cm` (default) | positive scalar in units of length

Distance from the center of the pulley to the centerline of the cord at
any point of contact. In compound pulley systems, the differences in pitch
radii often determine the ratio at which speed is reduced or torque is
augmented.

### **Initial Wrap Angle** — Minimum wrap angle of a pulley at the start of simulation `0.0 deg` (default) | positive scalar in degrees

**Lower Bound** — Specify the lower bound on the initial
wrap angle of the pulley. The wrap angle at the beginning of simulation is
greater than or equal to this specified value.

### **Sensing** — Selection of kinematic variables to sense `Unchecked` (default) | Checked

Selection of kinematic variables to sense. Select a check box to expose a
physical signal port for the corresponding variable. The variables available
for sensing are:

- **Wrap Angle** — Angle from the point of
  contact associated with port **A** to that
  associated with port **B**. This angle is
  measured in the center (*xy*) plane of the
  pulley. It is always equal to or greater than zero, with its
  value increasing by `2π` for each revolution
  made counterclockwise about the local *z*-axis.
  Use port **qwrp** for this measurement.

  The figure shows the wrap angle between the contact points
  (**A** and **B** of a
  pulley). The local reference frame indicates the
  *x*-axis (horizontal) and the
  *y*-axis (vertical) of the pulley.
- **Pulley Angle A** — Angle, measured in the
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

  **Pulley Angles A and B**
- **Pulley Angle B** — Angle, measured in the
  *xy* plane of the reference frame, from the
  local *x*-axis to the line between the frame
  origin and point of contact **B**.

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

  Use port **qpb** for this measurement.
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

  **Fleet Angle A**
- **Fleet Angle B** — Angle from the
  *xy*-plane of the reference frame to the
  cord at point of contact **B**. The
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

  Use port **qfb** for this measurement.

## Libraries

Simscape / Multibody / Belts and Cables

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Wheel wrapped in a cord for the transmission of torque and motion

The Pulley block represents a grooved or toothed wheel wrapped in a
cord, an arrangement used frequently in the transmission of torque and motion in part
for the mechanical advantage that it can provide. The pulley (or sprocket if toothed) is
*ideal*: massless and frictionless, with zero slip permitted
between its surface and the surrounding cord, itself idealized as taut and inextensible.
Use the pulley singly or as part of a compound pulley system such as the block and
tackle of a hoist or the timing belt of a car engine.

The pulley has one local reference frame (frame port **R**) and two
cord tangency points (belt-cable ports **A** and
**B**). The reference frame is placed with its origin at the center of
the pulley and its *z*-axis along the rotation axis of the same. The
cord tangency points coincide with the locations at which the cord meets or separates
from the pulley. These locations can change during simulation. The belt or cable wraps
around the pulley from port **A** to port **B** so as
to trace a counterclockwise arc about the *z*-axis.

In a closed-loop system of two pulleys—such as a belt drive—the connections of the
belt-cable ports determine whether the cord geometry is *crossed* or
*open*. As shown in the following schematic, in a system of
pulleys in which the *z*-axes are aligned in parallel, if port
**A** of one connects to port **A** of another,
then the cord is crossed; if port **A** of one connects to port
**B** of another, then the cord is open. The effect is the same if
instead of switching the port connections, one of the frames is flipped so that the
*z*-axes of the pulleys are anti-parallel.

The degrees of freedom of the pulley depend entirely on the joints and constraints (if
any) to which it connects. Attaching a pulley to a case by means of a revolute joint
imparts to the pulley one rotational degree of freedom relative to the case; one is then
free to rotate relative to the other. Fixing the pulley to another pulley, by means of a
direct connection, a rigid transform, or a weld joint, constrains the two so that if one
rotates, then so must the other.

By default, the cord can enter and exit a pulley at an angle to its center plane
(*θ* in the figure). This angle can vary during simulation—for
example, due to translation of the pulley on a prismatic joint. While the contact point
is always in the center plane of the pulley, the pulley can move when mounted on a
joint. The cord can also be constrained to enter and exit the pulley in its center
plane. Whether this constraint is enforced depends on the settings of the
Belt-Cable
Properties block.

The pulleys must remain at distances that preserve the natural length of the cord.
This length is computed from the initial placements of the pulleys and it is fixed: the
cord can neither stretch nor slacken during simulation. The length calculations include
the arc lengths of the cord about the pulleys. The contact between them is idealized as
slipless, with a contact point on the cord always moving at the same instantaneous
velocity as its counterpart on the pulley.

Note that the frame and belt-cable ports belong to different multibody domains. As a
rule, ports connect only to like ports—frame ports to other frame ports, belt-cable
ports to other belt-cable ports. The belt-cable domain has the special requirement that
each network or belt-cable connection lines connect to one (and no more than one)
Belt-Cable
Properties block. It is through that block that the visualization of
the cord is configured and the length of the same is (on diagram update)
computed.

The visualization of the cord is in the form of a pitch line. The cord meets and
separates from the pulley tangent to its circumference. The arc of contact between the
cord and the pulley is called the pitch arc. The pitch line of the cord is the sum of
the line segments between different pulleys and of their respective pitch arcs. The line
segments between the pulleys are shown as rectilinear, consistent with the constraint
that no slackening is allowed to take place.

Combine the Pulley block with the Belt-Cable
Spool block to retrieve from a winch, and to return to it,
additional lengths of cord. An example application is the lowering and raising of the
hook block of a tower crane. Use the Belt-Cable End block
to define an end point to the cord. The end point contains a frame for connection to a
load, fixture, or other part of a multibody model.
