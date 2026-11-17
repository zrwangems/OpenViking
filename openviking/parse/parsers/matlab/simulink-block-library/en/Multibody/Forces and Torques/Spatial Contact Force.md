---
type: simulink-block
title: 'Spatial Contact Force'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'spatialcontactforce'
documentation_source_path: 'ref/spatialcontactforce.html'
language: en
---

# Spatial Contact Force

## Ports
```yaml
ports:
- name: B
  summary: Base geometry geometry
  direction: input
- name: F
  summary: Follower geometry geometry
  direction: input
- name: fnz
  summary: Normal contact force magnitude, N physical signal
  direction: input
- name: ffrxy
  summary: Friction force, N physical signal
  direction: input
- name: con
  summary: Contact signal, unitless physical signal
  direction: output
- name: pen
  summary: Penetration depth, m physical signal
  direction: output
- name: sep
  summary: Separation distance, m physical signal
  direction: output
- name: vn
  summary: Relative normal velocity, m/s physical signal
  direction: output
- name: vt
  summary: Relative tangential velocity, m/s physical signal
  direction: output
- name: fn
  summary: Normal force, N physical signal
  direction: output
- name: fnm
  summary: Normal force magnitude, N physical signal
  direction: output
- name: tn
  summary: Torque resulting from normal force, N\*m physical signal
  direction: output
- name: ffr
  summary: Frictional force, N physical signal
  direction: output
- name: ffrm
  summary: Frictional force magnitude, N physical signal
  direction: output
- name: tfr
  summary: Torque resulting from frictional force, N\*m physical signal
  direction: output
- name: ft
  summary: Total contact force, N physical signal
  direction: output
- name: tt
  summary: Torque resulting from total contact force, N\*m physical signal
  direction: output
- name: Rb
  summary: Base rotation, unitless physical signal
  direction: output
- name: pb
  summary: Base translation, unitless physical signal
  direction: output
- name: Rf
  summary: Follower rotation, unitless physical signal
  direction: output
- name: pf
  summary: Follower translation, unitless physical signal
  direction: output
```

### Geometry

### **B** — Base geometry geometry

Geometry port associated with the base geometry.

### **F** — Follower geometry geometry

Geometry port associated with the follower geometry.
### Input

### **fnz** — Normal contact force magnitude, N physical signal

Physical signal input port that accepts the normal contact force magnitude between
the two geometries. The block clips negative values to zero.

When modeling contacts that involve a point cloud, the input signal must be a
1-by-*N* array, where *N* equals the number of
points. Each column of the array specifies the normal contact force on one of the
points. The size and order of the input signals must match the size and order of the
points specified in the Point Could block. The force is
resolved in the contact frame of the point.

When modeling contacts between other types of geometries, the input signal must be
a scalar that specifies the normal contact force.

#### Dependencies

To enable this port, in the **Normal Force** section, set
**Method** to `Provided by
Input`.

### **ffrxy** — Friction force, N physical signal

Physical signal input port that accepts the frictional force between the two
geometries.

When modeling contacts that involve a point cloud, the input signal must be a
2-by-*N* matrix, where *N* equals the number of
points. Each column of the matrix specifies the *x*-component and
*y*-component of the applied frictional force on one of the points.
The size and order of the input signals must match the size and order of the points
specified in the Point Could block. The force is
resolved in the contact frame of the point.

When modeling contacts between other types of geometries, the input signal must be
a 2-by-1 array that specifies the *x*-component and
*y*-component of the applied frictional force resolved in the
contact frame.

#### Dependencies

To enable this port, in the **Frictional Force** section, set
**Method** to `Provided by
Input`.
### Output

### **con** — Contact signal, unitless physical signal

Physical signal output port that outputs the contact status of the two
geometries.

When modeling contacts that involve a point cloud, the output is a
1-by-*N* array, where *N* equals the number of
points. Each column of the array indicates the status of the corresponding point. The
point contacts the other geometry if the value is 1. Otherwise, the value is 0.

When modeling contacts between other types of geometries, the output is a scalar
that indicates whether the geometries are in contact. The geometries are in contact if
the output is 1 or separated if the output is 0.

#### Dependencies

To enable this port, in the **Sensing** section, select
**Contact Signal**.

### **pen** — Penetration depth, m physical signal

Physical signal output port that outputs the penetration depth between the two
geometries.

When modeling contacts that involve a point cloud, the output is a
1-by-*N* array, where *N* equals the number of
points. Each column of the array indicates the status of the corresponding point. If
the point is penetrating the other geometry, the value is positive and equals the
penetration depth. Otherwise, the value is 0.

When modeling contacts between other types of geometries, the output is a scalar
that indicates whether the geometries are penetrating each other. If they are
penetrating each other, the output is positive. Otherwise, the output is 0.

#### Dependencies

To enable this port, in the **Sensing** section, select
**Penetration Depth**.

### **sep** — Separation distance, m physical signal

Physical signal output port that outputs the separation distance between the two
geometries.

When modeling contacts that involve a point cloud, the output is a
1-by-*N* array, where *N* equals the number of
points. Each column of the array indicates the status of the corresponding point. If
the point is not penetrating the other geometry, the value is nonnegative and equals
the minimum distance between the point and the other geometry. Otherwise, the output
is negative and the absolute value equals the penetration depth.

When modeling contacts between other types of geometries, the output is a scalar.
If they are not penetrating each other, the output is nonnegative and equals the
minimum distance between the two geometries. Otherwise, the output is negative and the
absolute value equals the penetration depth.

#### Dependencies

To enable this port, in the **Sensing** section, select
**Separation Distance**.

### **vn** — Relative normal velocity, m/s physical signal

Physical signal output port that provides the *z*-component of
the relative velocity between the contact points of the base and follower
geometries.

When modeling contacts that involve a point cloud, the output is a
1-by-*N* array, where *N* equals the number of
points. Each column of the array equals the *z*-component of the
relative velocity between the corresponding point and the contact point on the other
geometry. The relative velocity is resolved in the corresponding contact frame.

When modeling contacts between other types of geometries, the output is a scalar
that equals the *z*-component of the relative velocity between the
contact points of the two geometries. The output is resolved in the contact
frame.

#### Dependencies

To enable this port, in the **Sensing** section, select
**Relative Normal Velocity**.

### **vt** — Relative tangential velocity, m/s physical signal

Physical signal output port that outputs the relative tangential velocity between
the contact points of the base and follower geometries.

When modeling contacts that involve a point cloud, the output is a
2-by-*N* matrix, where *N* equals the number of
points. Each column of the array equals the *x*-component and
*y*-component of the relative velocity between the corresponding
point and the contact point on the other geometry. The relative velocity is resolved
in the corresponding contact frame.

When modeling contacts between other types of geometries, the output is a 2-by-1
array that equals the *x*-component and
*y*-component of the relative velocity between the contact points of
the two geometries. The output is resolved in the contact frame.

#### Dependencies

To enable this port, in the **Sensing** section, select
**Relative Tangential Velocity**.

#### Force/Torque

### **fn** — Normal force, N physical signal

Physical signal output port for the normal force between two contact geometries. The block
resolves the measurement in the coordinates of the specified resolution frame, and
the setting of the **Direction** parameter affects the sign of the
measurement.

When modeling contacts that involve a point cloud, the output is a 3-by-*N* array, where *N* represents the number of points. Each column of the array represents a 3-D vector that indicates the normal force at the corresponding point.

When modeling contacts between other types of geometries, the output represents a 3-D vector that indicates the normal force.

#### Dependencies

To enable this port, in the **Force/Torque** section, select **Normal Force**.

### **fnm** — Normal force magnitude, N physical signal

Physical signal output port for the magnitude of the normal force. The
**Direction** and **Resolution Frame**
parameters do not affect the measurement.

When modeling contacts that involve a point cloud, the output is a 1-by-*N*
array, where *N* equals the number of points. Each column of the
array is the magnitude of the normal force at the corresponding point.

When modeling contacts between other types of geometries, the output is the magnitude of the normal force.

#### Dependencies

To enable this port, in the **Force/Torque** section, select **Normal Force Magnitude**.

### **tn** — Torque resulting from normal force, N\*m physical signal

Physical signal output port for the torque resulting from the normal force. The measurement is
the cross product of the normal force and the position vector of the contact point
relative to the specified resolution frame. The **Direction**
parameter affects the sign of the measurement.

When modeling contacts that involve a point cloud, the output is a 3-by-*N* array, where *N* represents the number of points. Each column of the array represents a 3-D vector that indicates the torque due to the normal force at the corresponding point.

When modeling contacts between other types of geometries, the output represents a 3-D vector that indicates the torque due to the normal force.

#### Dependencies

To enable this port, in the **Force/Torque** section, select **Normal Torque**.

### **ffr** — Frictional force, N physical signal

Physical signal output port for the frictional force between two contact geometries. The block
resolves the measurement in the coordinates of the specified resolution frame, and
the setting of the **Direction** parameter affects the sign of the
measurement.

When modeling contacts that involve a point cloud, the output is a 3-by-*N* array, where *N* represents the number of points. Each column of the array represents a 3-D vector that indicates the frictional force at the corresponding point.

When modeling contacts between other types of geometries, the output represents a 3-D vector that indicates the frictional force.

#### Dependencies

To enable this port, in the **Force/Torque** section, select **Frictional Force**.

### **ffrm** — Frictional force magnitude, N physical signal

Physical signal output port for the magnitude of the frictional force between two contact
geometries. The **Direction** and **Resolution
Frame** parameters do not affect the measurement.

When modeling contacts that involve a point cloud, the output is a 1-by-*N*
array, where *N* equals the number of points. Each column of the
array is the magnitude of the frictional force at the corresponding point.

When modeling contacts between other types of geometries, the output is the magnitude of the normal contact force.

#### Dependencies

To enable this port, in the **Force/Torque** section, select **Frictional Force Magnitude**.

### **tfr** — Torque resulting from frictional force, N\*m physical signal

Physical signal output port for the torque resulting from the frictional force.
The measurement is the cross product of the frictional force and the position vector
of the contact point relative to the specified resolution frame. The
**Direction** parameter affects the sign of the
measurement.

When modeling contacts that involve a point cloud, the output is a 3-by-*N* array, where *N* represents the number of points. Each column of the array represents a 3-D vector that indicates the torque due to the frictional force at the corresponding point.

When modeling contacts between other types of geometries, the output represents a 3-D vector that indicates the torque due to the frictional force.

#### Dependencies

To enable this port, in the **Force/Torque** section, select **Frictional Torque**.

### **ft** — Total contact force, N physical signal

Physical signal output port for the total contact force between two contact geometries. The
total contact force includes normal and frictional forces. The block resolves the
measurement in the coordinates of the specified resolution frame, and the setting of
the **Direction** parameter affects the sign of the
measurement.

When modeling contacts that involve a point cloud, the output is a 3-by-*N* array, where *N* represents the number of points. Each column of the array represents a 3-D vector that indicates the total contact force at the corresponding point.

When modeling contacts between other types of geometries, the output represents a 3-D vector that indicates the total contact force.

#### Dependencies

To enable this port, in the **Force/Torque** section, select **Total Force**.

### **tt** — Torque resulting from total contact force, N\*m physical signal

Physical signal output port for the total contact torque resulting from the contact force. The
measurement is the cross product of the contact force and the position vector of the
contact point relative to the specified resolution frame. The
**Direction** parameter affects the sign of the
measurement.

When modeling contacts that involve a point cloud, the output is a 3-by-*N* array, where *N* represents the number of points. Each column of the array represents a 3-D vector that indicates the contact torque due to the total contact force at the corresponding point.

When modeling contacts between other types of geometries, the output represents a 3-D vector that indicates the torque due to the total contact force.

#### Dependencies

To enable this port, in the **Force/Torque** section, select **Total Torque**.

#### Contact Frame

### **Rb** — Base rotation, unitless physical signal

Physical signal port that outputs the rotation matrix of the contact frame with
respect to the reference frame of the base geometry.

When modeling contacts that involve a point cloud, the output is a 3-D array that
has *N* 3-by-3 matrices, where *N* equals the number
of points in the point cloud. Each 3-by-3 matrix is a rotation matrix that maps the
vectors in the corresponding contact frame to vectors in the reference frame of the
base geometry. If a point is not in contact with the other geometry, the corresponding
matrix is an identity matrix.

When modeling contacts between other types of geometries, the output is a 3-by-3
rotation matrix that maps the vectors in the contact frame to vectors in the reference
frame of the base geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Base Rotation**.

### **pb** — Base translation, unitless physical signal

Physical signal port that outputs the location of the contact point with respect
to the reference frame of the base geometry.

When modeling contacts that involve a point cloud, the output is a
3-by-*N* array, where *N* equals the number of
points. Each column of the array indicates the coordinates of a point with respect to
the reference frame of the base geometry. If a point is not in contact with the other
geometry, the coordinates are `[0 0 0]`.

When modeling contacts between other types of geometries, the output is a 3-by-1
array that contains the coordinates of the contact point with respect to the reference
frame of the base geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Base Translation**.

### **Rf** — Follower rotation, unitless physical signal

Physical signal port that outputs the rotation matrix of the contact frame with
respect to the reference frame of the follower geometry.

When modeling contacts that involve a point cloud, the output is a 3-D array that
has *N* 3-by-3 matrices, where *N* equals the number
of points in the point cloud. Each 3-by-3 matrix is a rotation matrix that maps the
vectors in the corresponding contact frame to vectors in the reference frame of the
follower geometry. If a point is not in contact with the other geometry, the
corresponding matrix is an identity matrix.

When modeling contacts between other types of geometries, the output is a 3-by-3
rotation matrix that maps the vectors in the contact frame to vectors in the reference
frame of the follower geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Follower Rotation**.

### **pf** — Follower translation, unitless physical signal

Physical signal port that outputs the location of the contact point with respect
to the reference frame of the follower geometry.

When modeling contacts that involve a point cloud, the output is a
3-by-*N* array, where *N* equals the number of
points. Each column of the array indicates the coordinates of a point with respect to
the reference frame of the follower geometry. If a point is not in contact with the
other geometry, the coordinates are `[0 0 0]`.

When modeling contacts between other types of geometries, the output is a 3-by-1
array that contains the coordinates of the contact point with respect to the reference
frame of the follower geometry.

#### Dependencies

To enable this port, in the **Sensing > Contact Frame**
section, select **Follower Translation**.
## Parameters
```yaml
parameters:
- name: Method
  summary: Method to specify normal contact force Smooth Spring-Damper (default) | Provided by Input
  group: Normal Force
- name: Stiffness
  summary: Resistance of contact spring to geometric penetration 1e6 N/m (default) | scalar
  group: Normal Force
- name: Damping
  summary: Resistance of contact damper to motion while geometries are penetrating 1e3 N/(m/s) (default) | scalar
  group: Normal Force
- name: Transition Region Width
  summary: Region over which spring-damper force raises to its full value 1e-4 m (default) | scalar
  group: Normal Force
- name: Method
  summary: Method to specify frictional force Smooth Stick-Slip (default) | None | Provided by Input
  group: Frictional Force
- name: Coefficient of Static Friction
  summary: Ratio of magnitude of frictional force to the magnitude of normal force when tangential velocity is close to zero
    0.5 (default) | nonnegative scalar
  group: Frictional Force
- name: Coefficient of Dynamic Friction
  summary: Ratio of magnitude of frictional force to magnitude of normal force when tangential velocity is large 0.3 (default)
    | nonnegative scalar
  group: Frictional Force
- name: Critical Velocity
  summary: Velocity that determines blending between static and dynamic coefficients of friction 1e-3 m/s (default) | scalar
  group: Frictional Force
- name: Direction
  summary: Measurement direction Base on Follower (default) | Follower on Base
  group: Sensing
- name: Resolution Frame
  summary: Frame used to resolve measurements Contact (default) | Base | Follower
  group: Sensing
- name: Detect Contact Start and End
  summary: Detect start and end of contacts as zero-crossing events off (default) | on
  group: Zero-Crossings
```

### Normal Force

### **Method** — Method to specify normal contact force `Smooth Spring-Damper` (default) | `Provided by Input`

Method to specify the normal contact force, specified as either
`Smooth Spring-Damper` or `Provided by
Input`.

Select `Smooth Spring-Damper` to use the modified
spring-damper method to model the normal contact force, or select
`Provided by Input` to input a custom force as the normal
contact force.

### **Stiffness** — Resistance of contact spring to geometric penetration 1e6 `N/m` (default) | scalar

Resistance of the contact spring to geometric penetration, specified as a scalar.
The spring stiffness is constant during the contact. The larger the value of the
spring stiffness, the harder the contact between the geometries.

#### Dependencies

To enable this parameter, in the **Normal Force** section, set
**Method** to `Smooth
Spring-Damper`.

### **Damping** — Resistance of contact damper to motion while geometries are penetrating 1e3 `N/(m/s)` (default) | scalar

Resistance of the contact damper to motion while the geometries are penetrating,
specified as a scalar. The damping coefficient is a constant value that represents the
lost energy from colliding geometries. The larger the value of the damping
coefficient, the more energy is lost when geometries collide and the faster the
contact vibrations are dampened. Use a value of zero to model perfectly elastic
collisions, which conserve energy.

#### Dependencies

To enable this parameter, in the **Normal Force** section, set
**Method** to `Smooth
Spring-Damper`.

### **Transition Region Width** — Region over which spring-damper force raises to its full value 1e-4 `m` (default) | scalar

Region over which the spring-damper force raises to its full value, specified as a
scalar. The smaller the region, the sharper the onset of contact and the smaller the
time step required for the solver. Reducing the transition region improves model
accuracy while expanding the transition region improves simulation speed.

#### Dependencies

To enable this parameter, in the **Normal Force** section, set
**Method** to `Smooth
Spring-Damper`.

### Frictional Force

### **Method** — Method to specify frictional force `Smooth Stick-Slip` (default) | `None` | `Provided by Input`

Method to specify the frictional force, specified as `Smooth
Stick-Slip`, `None`, or `Provided
by Input`.

Select `None` to omit friction, `Smooth
Stick-Slip` to use the modified stick-slip method to compute the
frictional force, or `Provided by Input` to input a custom
frictional force.

### **Coefficient of Static Friction** — Ratio of magnitude of frictional force to the magnitude of normal force when tangential velocity is close to zero 0.5 (default) | nonnegative scalar

Ratio of the magnitude of the frictional force to the magnitude of the normal
force when the tangential velocity is close to zero, specified as a positive
scalar.

This value is determined by the material properties of the contacting geometries.
The value of this parameter is often less than one, although values greater than one
are possible for high-friction materials. In most cases, this value should be higher
than the coefficient of dynamic friction.

#### Dependencies

To enable this parameter, in the **Frictional Force** section,
set **Method** to `Smooth
Stick-Slip`.

### **Coefficient of Dynamic Friction** — Ratio of magnitude of frictional force to magnitude of normal force when tangential velocity is large 0.3 (default) | nonnegative scalar

Ratio of the magnitude of the frictional force to the magnitude of the normal
force when the tangential velocity is large, specified as a nonnegative scalar.

This value is determined by the material properties of the contacting geometries.
The value of this parameter is often less than one, although values greater than one
are possible for high-friction materials. In most cases, this value should be less
than the coefficient of static friction.

#### Dependencies

To enable this parameter, in the **Frictional Force** section,
set **Method** to `Smooth
Stick-Slip`.

### **Critical Velocity** — Velocity that determines blending between static and dynamic coefficients of friction 1e-3 `m/s` (default) | scalar

Velocity that determines the blending between the static and dynamic coefficients
of friction, specified as a scalar.

When the critical velocity is equal to the magnitude of the tangential velocity,
the effective coefficient of friction is equal to the value of the
**Coefficient of Static Friction** parameter. As the magnitude of
the tangential velocity increases beyond the specified critical velocity, the
effective coefficient of friction asymptotically approaches the value of the
**Coefficient of Dynamic Friction** parameter.

#### Dependencies

To enable this parameter, in the **Frictional Force** section,
set **Method** to `Smooth
Stick-Slip`.

### Sensing

#### Force/Torque

### **Direction** — Measurement direction `Base on Follower` (default) | `Follower on Base`

Measurement direction, specified as one of these values:

- `Base on Follower` — The block senses the force and torque that the base geometry exerts on the follower geometry.
- `Follower on Base` — The block senses the force and torque that the follower geometry exerts on the base geometry.

This parameter affects only the vector outputs under the **Force/Torque** section. Reversing the direction changes the sign of the measurements. For more information, see Force and Torque Measurement Direction.

### **Resolution Frame** — Frame used to resolve measurements `Contact` (default) | `Base` | `Follower`

Frame used to resolve the measurements, specified as one of these values:

- `Contact` — The block resolves the measurements in the coordinates of the contact frame.
- `Base` — The block resolves the measurements in the coordinates of the base frame.
- `Follower` — The block resolves the measurements in the coordinates of the follower frame.

This parameter affects only the vector outputs under the **Force/Torque** section.

### Zero-Crossings

### **Detect Contact Start and End** — Detect start and end of contacts as zero-crossing events off (default) | on

Select to detect the start and end of each contact as zero-crossing events. The
zero-crossing events occur when the separation distance changes from positive or zero
to negative and vice versa.
## Libraries

Simscape / Multibody / Forces and Torques

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

### R2025a: Measure contact forces and torques as vectors and resolve measurements using base, follower, or contact frame

You can now output normal, frictional, and total contact forces and torques as 3-D
vectors. By using the **Direction** parameter, you can specify whether the
output represents the force and torque exerted by the base geometry on the follower geometry
or vice versa. You can also resolve these vector outputs in the coordinates of either the
base, follower, or contact frame.

### R2023b: Use input forces and measure contact quantities for point cloud and grid surface

You can now use input forces to model contacts that involve a point cloud or a grid
surface and measure the corresponding contact quantities. When one of the geometries is a
point cloud, the signals of the input forces must be arrays that specify forces for every
point in the cloud, and the measured contact quantities are arrays that contain information
for every point in the cloud.

For the point cloud and grid surface contact pair, the Spatial Contact
Force block supports zero-crossing detection. The zero-crossing events
only occur when the separation distance changes from positive or zero to negative and vice
versa.

### R2023b: Measure the penetration depth between two geometries

Measure the penetration depth between two contact geometries. The value equals the
overlap distance when two geometries collide and equals zero when the geometries are not in
contact.

### R2023b: The **Separation Distance** parameter will be removed

The **Separation Distance** parameter will be removed in a future
release. Use the **Penetration Depth** parameter instead.

### R2023b: Behavior change non-scalar outputs

An inconsistent dimensions error appears if you compile a model that has a
Spatial Contact Force block that outputs a non-scalar
signal directly to any Simscape block except the PS-Simulink Converter block.

To avoid the error, use a PS Signal
Specification block to connect each non-scalar output signal of the
Spatial Contact Force block with the corresponding Simscape
blocks and explicitly specify the dimension of the output signal.

## Description

Model spatial contact between two geometries

The Spatial Contact Force block models the contact between
a pair of geometries in 3-D space. You can use the built-in penalty method or provide custom
normal and friction force laws to model a contact.

### Supported Geometries

The Spatial Contact Force block can model contacts
between a variety of geometry pairs. You can use the geometries exported from the solid
blocks in the Body Elements sublibrary or the geometries of the point and surface blocks in
the Curves and Surfaces sublibrary.

All the exported geometries are convex hull representations of the corresponding solids
even though some of the solids may have concave shapes. The figure shows the true geometry
and convex hull representation of an L-shape solid.

True geometry and convex hull representation of an L-shape solid.

Note that when computing inertial properties, the solid blocks use the true
geometry.

The Spatial Contact Force block does not model contacts
between certain geometry pairs. This table lists the supported pairs.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | **Convex Hull of Solid** | **Disk** | **Grid Surface** | **Infinite Plane** | **Point** | **Point Cloud** |
| **Convex Hull of Solid** | Yes | Yes | No | Yes | Yes | Yes |
| **Disk** | Yes | No | No | Yes | No | No |
| **Grid Surface** | No | No | No | No | Yes | Yes |
| **Infinite Plane** | Yes | Yes | No | No | Yes | Yes |
| **Point** | Yes | No | Yes | Yes | No | No |
| **Point Cloud** | Yes | No | Yes | Yes | No | No |

### Contact Forces

The image shows how the Spatial Contact Force block
models a spatial contact problem between two 3-D geometries. In this case, the contact is
between a blue base geometry and a red follower geometry and there is one contact
point.

During contact, each geometry has a contact frame. The contact frames are always
coincident and located at the contact point. The *xy*-planes of the contact
frames define the contact plane. The *z*-direction of the contact frames is
an outward normal vector for the base geometry, but an inward normal vector for the follower
geometry. During continuous contact, the contact frames move around the geometry as the
contact point moves.

The block applies contact forces to the geometries at the origin of the contact frames
in accordance with Newton's Third Law:

1. The normal force, fn, which is aligned with the *z*-axis of the contact
   frame. This force pushes the geometries apart in order to reduce penetration.
2. The frictional force, ff, which lies in the contact plane. This force opposes the relative
   tangential velocities between the geometries.

To specify a normal contact force, in the **Normal Force** section, set
the **Method** parameter to `Smooth Spring-Damper`
or `Provided by Input`. If you select `Smooth
Spring-Damper`, the normal force is:

fn=s(d,w)⋅(k⋅d+b⋅d'),

where:

- fn is the normal force applied in equal-and-opposite fashion to each
  contacting geometry.
- d is the penetration depth between two contacting geometries.
- w is the transition region width specified in the block.
- d' is the first time derivative of the penetration depth.
- k is the normal-force stiffness specified in the block.
- b is the normal-force damping specified in the block.
- s(d,w) is the smoothing function.

The force law is smoothed near the onset of penetration. When *d* < *w*, the smoothing function increases continuously and monotonically over the
interval [0, *w*]. The function is 0 when *d* = 0, the function is 1 when *d* = *w*, and the function has zero derivative with respect to *d*
at the endpoints of the interval.

To better detect contacts when the value of the **Transition Region
Width** parameter is small, the Spatial Contact
Force block supports optional zero-crossing detection. The zero-crossing
events only occur when the separation distance changes from positive or zero to negative and
vice versa.

**Note**

The zero-crossing detection of the Spatial Contact
Force block is different than the zero-crossing detection of other
Simulink® blocks, such as From File and Integrator, because the force equation of the Spatial Contact
Force is continuous. For more information about zero-crossing detection
in Simulink blocks, see Zero-Crossing Detection.

To specify a frictional force, in the **Frictional Force** section, set
the **Method** parameter to `Smooth Stick-Slip`,
`Provided by Input`, or `None`. If you
select `Smooth Stick-Slip`, the frictional force is always directly
opposed to the direction of the relative velocity at the contact point and is related to the
normal force through a coefficient of friction that varies depending on the magnitude of the
relative velocity:

|ff|=μ⋅|fn|,

where:

- ff is the frictional force.
- fn is the normal force.
- μ is the effective coefficient of friction.

The effective coefficient of friction is a function of the values of the
**Coefficient of Static Friction**, **Coefficient of Dynamic
Friction**, and **Critical Velocity** parameters, and the
magnitude of the relative tangential velocity. At high relative velocities, the value of the
effective coefficient of friction is close to that of the coefficient of dynamic friction.
At the critical velocity, the effective coefficient of friction achieves a maximum value
that is equal to the coefficient of static friction. The graph shows the basic relationship
in the typical case where μstatic > μdynamic. In this case, the model is able to approximate stiction with a higher
effective coefficient of friction near small tangential velocities.

plot of effective coefficient of friction

When modeling contacts that involve a point cloud, the Spatial Contact
Force block calculates the contact quantities for each point and the
output signals have the same order as the points specified in the Point
Could block. For the points that are not in contact with the other
geometry, the measured values are zero. When using input forces, the size and order of the
input signals must match the size and order of the points specified in the
Point Could block.
