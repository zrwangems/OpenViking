---
type: simulink-block
title: 'Custom Tire Force and Torque'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Multibody Dynamics / Loads'
documentation_page: 'customtireforceandtorque'
documentation_source_path: 'ref/customtireforceandtorque.html'
language: en
---

# Custom Tire Force and Torque

## Ports

### Geometry

### **B** — Base geometry geometry

Base geometry that represents the surface that the tire contacts. You must connect
this port to an Infinite
Plane or Grid
Surface block.
### Frame

### **F** — Follower frame frame

Follower frame that represents the tire. The frame origin is located at the center
of the tire.
### Input

### **ft** — Tire force, *N* physical signal

Physical signal input port that receives the computed custom tire force. Use the
outputs from the Custom Tire Force and Torque block to
compute the tire force. You must compute the tire force with respect to the contact
frame of the tire.

The input contains three parts:

- Fx is the longitudinal force tangential to the contact
  plane and aligns with the *x*-axis of the contact frame.
- Fy is the lateral force, which is orthogonal to the
  plane defined by Fx and Fz.
- Fz is the normal force that is normal to the contact
  plane at the contact point.

The force must be nonnegative. If the block receives a negative force, the block
clips the value to zero. In addition, you must ensure the units are consistent during
the simulation.

### **tt** — Tire torque, *N\*m* physical signal

Physical signal input port that receives the computed custom tire torque. Use the
outputs from the Custom Tire Force and Torque block to
compute the tire torque. You must compute the tire torque with respect to the contact
frame of the tire.

The input contains three parts:

- Mx is the overturning moment.
- My is the rolling resistance moment.
- Mz is the aligning torque.

You must ensure the units are consistent during the simulation.
### Output

### **con** — Contact signal, unitless physical signal

Physical signal output port that indicates whether the tire and contact surface
have a valid contact. When they are in contact and the contact is valid, the signal
equals `1`, otherwise the signal equals `0`.

If the follower frame is below the contact surface, the tire and the surface have
an invalid contact and the block does not apply force and torque to the tire.

#### Dependencies

To enable this port, under **Sensing**, select
**Contact Signal**.

#### Linear Velocity

### **vx** — Relative longitudinal velocity, *m/s* physical signal

Physical signal output port that outputs the relative velocity between the
follower frame and the contact point on the geometry along the
*x*-direction of the contact frame. The value has a unit of
length/time.

#### Dependencies

To enable this port, under **Sensing > Linear Velocity**,
select **Relative Longitudinal Velocity**.

### **vy** — Relative lateral velocity, *m/s* physical signal

Physical signal output port that outputs the relative velocity between the
follower frame and the contact point on the geometry along the
*y*-direction of the contact frame. The value has a unit of
length/time.

#### Dependencies

To enable this port, under **Sensing > Linear Velocity**,
select **Relative Lateral Velocity**.

#### Yaw

### **psid** — Yaw velocity, *rad/s* physical signal

Physical signal output port that outputs the first derivative of the yaw angle.
The value has a unit of angle/time.

#### Dependencies

To enable this port, under **Sensing > Yaw**, select
**Velocity**.

#### Camber

### **gamma** — Camber angle, *rad* physical signal

Physical signal output port that outputs the camber angle of the tire. The value
has a unit of angle.

#### Dependencies

To enable this port, under **Sensing > Camber**, select
**Angle**.

### **gammad** — Camber velocity, *rad/s* physical signal

Physical signal output port that outputs the first derivative of the camber angle.
The value has a unit of angle/time.

#### Dependencies

To enable this port, under **Sensing > Camber**, select
**Velocity**.

#### Spin

### **omega** — Spin velocity, *rad/s* physical signal

Physical signal output port that provides the first derivative of the spin angle.
The value has a unit of angle/time.

#### Dependencies

To enable this port, under **Sensing > Spin**, select
**Velocity**.

#### Tire Radius

### **rl** — Loaded radius, *m* physical signal

Physical signal output port that provides the distance from the center of the tire
to the contact point between the tire and the contact surface. The value has a unit of
length.

#### Dependencies

To enable this port, under **Sensing > Tire Radius**, select
**Loaded Radius**.

### **rho** — Radial deflection, *m* physical signal

Physical signal output port that provides the difference between the tire radius
specified in the **Tire Radius** parameter and loaded radius output
from the **rl** port. The value has a unit of length.

#### Dependencies

To enable this port, under **Sensing > Tire Radius**, select
**Radial Deflection**.

#### Contact Frame

### **Rb** — Base rotation, unitless physical signal

Physical signal port that outputs a 3-by-3 rotation matrix that maps the vectors
in the contact frame to vectors in the reference frame of the base geometry. The
output signal is resolved in the reference frame associated with the base
geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Base Rotation**.

### **pb** — Base translation, *m* physical signal

Physical signal port that outputs a 3-by-1 vector that contains the coordinates of
the origin of the contact frame resolved in the reference frame of the base
geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Base Translation**.

### **Rf** — Follower rotation, unitless physical signal

Physical signal port that outputs a 3-by-3 rotation matrix that maps vectors in
the contact frame to vectors in the reference frame of the follower geometry. The
output signal is resolved in the reference frame associated with the follower
geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Follower Rotation**.

### **pf** — Follower translation, *m* physical signal

Physical signal port that outputs a 3-by-1 vector that contains the coordinates of
the origin of the contact frame resolved in the reference frame of the follower
geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Follower Translation**.

## Parameters

### **Tire Radius** — Radius of tire `1 m` (default) | positive scalar

Radius of the tire, specified as a positive scalar with a unit of length.

### **Contact Frame Computation Method** — Method to use to compute location and orientation of the contact frame `Weighted Penetration` (default) | `Closest Point`

Method to use to compute the location and orientation of the contact frame,
specified as:

- `Closest Point`: Use this method for on-road driving
  conditions where single-point contact is sufficient.
- `Weighted Penetration`: Use this method for
  rough-ground driving conditions that involve multi-point contacts, such as
  off-road scenarios.

You can use the computed data to develop custom tire models.

## Libraries

Simscape / Multibody / Forces and Torques

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2024b: Compute radial deflection and loaded radius

You can use the **rl** and **rho** ports to compute
the loaded radius and radial deflection for your custom tire model. The loaded radius is the
distance from the center of the tire to the contact point between the tire and the contact
surface, and the radial deflection is the difference between the loaded radius and tire
radius specified in the **Tire Radius** parameter.

## Description

Compute interactions and spatial relationships between tire and ground surface

The Custom Tire Force and Torque block computes the
interactions and spatial relationships between a tire and the ground surface.

To model a custom tire, use the outputs from the block to compute the tire force and
torque. Then, loop these signals into the block as inputs. The image shows the diagram of a
custom tire model.

You must calculate the tire force and torque relative to the contact frame of the tire.
The contact frame is at the contact point and the *z*-axis of the frame is
perpendicular to the contact plane. The tire force must be nonnegative. If the tire force is
negative, the block clips the input force to zero. Additionally, you must maintain consistent
units for force and torque throughout the simulation.

The follower frame is at the center of the tire. The image shows the follower and contact
frames of the tire at zero configuration.

The yaw, camber, and spin angles correspond to a
*y*-*x*-*z* sequence rotation about the
follower frame of a tire.

The block has two methods to calculate the data that characterizes the interactions and
spatial relationships between the tire and the ground. The closest point method determines the
contact point by finding the point on the ground surface that is closest to the center of the
tire and lies in the plane of the tire. The contact normal vector is at the contact point and
perpendicular to the contact patch at the contact point.

For scenarios where tires experience multiple-point contact, such as off-road terrain or
obstacles like speed bumps, use the weighted-penetration method. To simplify the computation
due to the irregularities of the contact surface, this method computes an equivalent contact
plane at each simulation time step to approximate the actual contact area. The contact point
is the nearest point on this equivalent plane to the center of the tire. The contact normal
vector is at the contact point and perpendicular to the equivalent plane. For example, the
image shows how the weighted-penetration method computes the equivalent plane, contact point,
and normal vector when a tire encounters a ramp.

The weighted-penetration normal vector, *n*, is orthogonal to the
equivalent contact plane.

**Note**

When using the weighted-penetration method, the contact point may not lie on the actual
ground geometry. For example, the contact point may be below or above the ground surface if
the contact area is locally convex or concave.

You can use the **con** port to indicate whether the tire and the surface
have a valid contact. If the tire and the surface are not in contact or the contact is not
valid, all sensed outputs, such as the tire force, tire torque, and camber angle, become
zero.
