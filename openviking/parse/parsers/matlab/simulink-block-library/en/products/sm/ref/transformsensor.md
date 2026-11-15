---
type: simulink-block
title: 'Transform Sensor'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Multibody Dynamics / Sensors'
documentation_page: 'transformsensor'
documentation_source_path: 'ref/transformsensor.html'
language: en
---

# Transform Sensor

## Ports

### Frame

### **B** — Base frame frame

Frame port associated with the base frame.

### **F** — Follower frame frame

Frame port associated with the follower frame.
### Output

### **q** — Angle of rotation, rad physical signal

Angle of rotation, returned as a scalar. The angle indicates the rotation of the
follower frame with respect to the base frame about the axis specified by the vector
output by port **axs**. The angle falls in the range [0, π].

Use ports **q** and **axs** to output the
rotation signals using the axis-angle parameterization. For more information, see
Rotational Measurements. The setting of the **Measurement Frame** parameter does not
affect the expression of this signal.

#### Dependencies

To enable this port, under **Rotation**, select
**Angle**.

### **axs** — Axis of rotation, unitless physical signal

Axis of rotation, returned as a 3-by-1 unit vector. Use ports
**q** and **axs** to output the rotation signals
using the axis-angle parameterization.

The setting of the **Measurement Frame** parameter does not
affect the expression of this signal.

#### Dependencies

To enable this port, under **Rotation**, select
**Axis**.

### **Q** — Quaternion, unitless physical signal

Relative rotation, returned as a quaternion. For more information about the
quaternions, see Rotational Measurements.

The setting of the **Measurement Frame** parameter does not
affect the expression of this signal.

#### Dependencies

To enable this port, under **Rotation**, select
**Quaternion**.

### **R** — Rotation matrix, unitless physical signal

Relative rotation, returned as a 3-by-3 matrix. For more information about the
rotation matrix, see Rotational Measurements. The setting of the **Measurement
Frame** parameter does not affect the expression of this signal.

#### Dependencies

To enable this port, under **Rotation**, select
**Transform**.

### **seq** — Angles of three successive rotations, rad physical signal

Relative rotation, returned as a 3-by-1 vector. The vector contains the angles for
the three successive elementary rotations that represent the rotation of the follower
frame with respect to the base frame.

The three rotations are about an intermediate frame and can be one of 12 different
rotation sequences. For more information about the rotation sequence measurements, see
Rotational Measurements. The setting of the **Measurement Frame** parameter does not
affect the expression of this signal.

#### Dependencies

To enable this port, under **Rotation**, select
**Rotation Sequence**.

### **wx** — *X*-component of relative angular velocity, rad/s physical signal

*X*-component of the relative angular velocity between the two
frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Angular Velocity**, select
**Omega X**.

### **wy** — *Y*-component of relative angular velocity, rad/s physical signal

*Y*-component of the relative angular velocity between the two
frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Angular Velocity**, select
**Omega Y**.

### **wz** — *Z*-component of relative angular velocity, rad/s physical signal

*Z*-component of the relative angular velocity between the two
frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Angular Velocity**, select
**Omega Z**.

### **w** — Relative angular velocity, rad/s physical signal

Angular velocity of the follower frame with respect to the base frame, returned as
a 3-by-1 vector. The setting of the **Measurement Frame** parameter
affects the expression of this signal.

#### Dependencies

To enable this port, under **Angular Velocity**, select
**Omega XYZ**.

### **Qd** — Relative angular velocity expressed as time derivative of quaternion, unitless physical signal

Relative angular velocity, returned as a 4-by-1 vector that equals the time
derivative of the signal from port **Q**. The setting of the
**Measurement Frame** parameter does not affect the expression of
this signal.

#### Dependencies

To enable this port, under **Angular Velocity**, select
**Quaternion**.

### **Rd** — Relative angular velocity expressed as time derivative of rotation matrix, unitless physical signal

Relative angular velocity, returned as a 3-by-3 matrix. The matrix equals the time
derivative of the signal from port **R**. The setting of the
**Measurement Frame** parameter does not affect the expression of
this signal.

#### Dependencies

To enable this port, under **Angular Velocity**, select
**Transform**.

### **seqd** — Relative angular velocity expressed as time derivative of rotation sequence angles, rad/s physical signal

Relative angular velocity, returned as a 3-by-1 vector. The vector equals the time
derivative of the output from the port **seq**. The setting of the
**Measurement Frame** parameter does not affect the expression of
this signal.

#### Dependencies

To enable this port, under **Angular Velocity**, select
**Rotation Sequence**.

### **bx** — *X*-component of relative angular acceleration, rad/s^2 physical signal

*X*-component of the relative angular acceleration between the
two frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Angular Acceleration**, select
**Alpha X**.

### **by** — *Y*-component of relative angular acceleration, rad/s^2 physical signal

*Y*-component of the relative angular acceleration between the
two frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Angular Acceleration**, select
**Alpha Y**.

### **bz** — *Z*-component of relative angular acceleration, rad/s^2 physical signal

*Z*-component of the relative angular acceleration between the
two frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Angular Acceleration**, select
**Alpha Z**.

### **b** — Relative angular acceleration, rad/s^2 physical signal

Angular acceleration of the follower frame with respect to the base frame,
returned as a 3-by-1 vector. The setting of the **Measurement Frame**
parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Angular Acceleration**, select
**Alpha XYZ**.

### **Qdd** — Relative angular acceleration expressed as second time derivative of quaternion, unitless physical signal

Relative angular acceleration, returned as a 4-by-1 vector. The setting of the
**Measurement Frame** parameter does not affect the expression of
this signal.

#### Dependencies

To enable this port, under **Angular Acceleration**, select
**Quaternion**.

### **Rdd** — Relative angular acceleration expressed as second time derivative of rotation matrix, unitless physical signal

Relative angular acceleration, returned as a 3-by-3 matrix. The setting of the
**Measurement Frame** parameter does not affect the expression of
this signal.

#### Dependencies

To enable this port, under **Angular Acceleration**, select
**Transform**.

### **x** — *X*-component of relative translation, m physical signal

*X*-component of the relative translation between the two frames,
returned as a scalar. The setting of the **Measurement Frame**
parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Translation**, select
**X**.

### **y** — *Y*-component of relative translation, m physical signal

*Y*-component of the relative translation between the two frames,
returned as a scalar. The setting of the **Measurement Frame**
parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Translation**, select
**Y**.

### **z** — *Z*-component of relative translation, m physical signal

*Z*-component of the relative translation between the two frames,
returned as a scalar. The setting of the **Measurement Frame**
parameter affects the expression of this signal.

Because both the Cartesian and cylindrical coordinate systems have the
*z*-axis, the Transform Sensor block
has only one output port for both coordinate systems.

#### Dependencies

To enable this port, under **Translation**, select
**Z**.

### **p** — Relative translation, m physical signal

Translation of the follower frame with respect to the base frame, returned as a
3-by-1 vector expressed in the Cartesian coordinate system. The setting of the
**Measurement Frame** parameter affects the expression of this
signal.

#### Dependencies

To enable this port, under **Translation**, select
**XYZ**.

### **rad** — Cylindrical radius coordinate of relative translation, m physical signal

Cylindrical radius coordinate of the relative translation vector, returned as a
nonegative scalar. The setting of the **Measurement Frame** parameter
affects the expression of this signal.

#### Dependencies

To enable this port, under **Translation**, select
**Radius**.

### **azm** — Azimuth of relative translation, rad physical signal

Azimuth of the relative translation vector, returned as scalar. The angle falls in
the range of [-π, π). The azimuth is undefined if the origins of the base and follower
frames coincide with each other. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

Because the azimuth exists in both the cylindrical and spherical coordinate
systems, the Transform Sensor block has only one output
port for both coordinate systems.

#### Dependencies

To enable this port, under **Translation**, select
**Azimuth**.

### **dst** — Spherical radius coordinate of relative translation, m physical signal

Spherical radius coordinate of the relative translation vector, returned as a
scalar. The value equals the distance between the origins of the base and follower
frames. The setting of the **Measurement Frame** parameter affects
the expression of this signal.

#### Dependencies

To enable this port, under **Translation**, select
**Distance**.

### **inc** — Inclination of relative translation, rad physical signal

Inclination of the relative translation vector, expressed in the spherical
coordinate system, returned as a scalar. The angle falls in the range of [-π/2, π/2].
The setting of the **Measurement Frame** parameter affects the
expression of this signal.

#### Dependencies

To enable this port, under **Translation**, select
**Inclination**.

### **vx** — *X*-coordinate of relative linear velocity, m/s physical signal

*X*-component of the relative linear velocity between the two
frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Velocity**, select
**X**.

### **vy** — *Y*-coordinate of relative linear velocity, m/s physical signal

*Y*-component of the relative linear velocity between the two
frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Velocity**, select
**Y**.

### **vz** — *Z*-coordinate of relative linear velocity, m/s physical signal

*Z*-component of the relative linear velocity between the two
frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

Because both the Cartesian and cylindrical coordinate systems have the
*z*-axis, the Transform Sensor block
has only one output port for both coordinate systems.

#### Dependencies

To enable this port, under **Velocity**, select
**Z**.

### **v** — Relative linear velocity, m/s physical signal

Linear velocity of the follower frame with respect to the base frame, returned as
a 3-by-1 vector expressed in Cartesian coordinate system. The setting of the
**Measurement Frame** parameter affects the expression of this
signal.

#### Dependencies

To enable this port, under **Velocity**, select
**XYZ**.

### **vrad** — Cylindrical radius coordinate of relative linear velocity, m/s physical signal

Cylindrical radius coordinate of the relative linear velocity, returned as a
scalar. The setting of the **Measurement Frame** parameter affects
the expression of this signal.

#### Dependencies

To enable this port, under **Velocity**, select
**Radius**.

### **vazm** — Azimuth coordinate of relative linear velocity, rad/s physical signal

Azimuth coordinate of the relative linear velocity, returned as a scalar. The
setting of the **Measurement Frame** parameter affects the expression
of this signal.

Because the azimuth coordinate exists in both the cylindrical and spherical
coordinate systems, the Transform Sensor block has only
one output port for both coordinate systems.

#### Dependencies

To enable this port, under **Velocity**, select
**Azimuth**.

### **vdst** — Spherical radius coordinate of relative linear velocity, m/s physical signal

Spherical radius coordinate of the relative linear velocity, returned as a scalar.
The setting of the **Measurement Frame** parameter affects the
expression of this signal.

#### Dependencies

To enable this port, under **Velocity**, select
**Distance**.

### **vinc** — Inclination coordinate of relative linear velocity, rad/s physical signal

Inclination coordinate of the relative linear velocity, expressed in the spherical
coordinate system, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Velocity**, select
**Inclination**.

### **ax** — *X*-component of relative linear acceleration, m/s^2 physical signal

*X*-component of the relative linear acceleration between the two
frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Acceleration**, select
**X**.

### **ay** — *Y*-component of relative linear acceleration, m/s^2 physical signal

*Y*-component of the relative linear acceleration between the two
frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

#### Dependencies

To enable this port, under **Acceleration**, select
**Y**.

### **az** — *Z*-component of relative linear acceleration, m/s^2 physical signal

*Z*-component of the relative linear acceleration between the two
frames, returned as a scalar. The setting of the **Measurement
Frame** parameter affects the expression of this signal.

Because both the Cartesian and cylindrical coordinate systems have the
*z*-axis, the Transform Sensor block
has only one output port for both coordinate systems.

#### Dependencies

To enable this port, under **Acceleration**, select
**Z**.

### **a** — Relative linear acceleration, m/s^2 physical signal

Linear acceleration of the follower frame with respect to the base frame, returned
as a 3-by-1 vector expressed in Cartesian coordinate system. The setting of the
**Measurement Frame** parameter affects the expression of this
signal.

#### Dependencies

To enable this port, under **Acceleration**, select
**XYZ**.

### **arad** — Cylindrical radius coordinate of relative linear acceleration, m/s^2 physical signal

Cylindrical radius coordinate of the relative linear acceleration, returned as a
scalar. The setting of the **Measurement Frame** parameter affects
the expression of this signal.

#### Dependencies

To enable this port, under **Acceleration**, select
**Radius**.

### **aazm** — Azimuth coordinate of relative linear acceleration, rad/s^2 physical signal

Azimuth coordinate of the relative linear acceleration, returned as a scalar. The
setting of the **Measurement Frame** parameter affects the expression
of this signal.

Because the azimuth coordinate exists in both cylindrical and spherical coordinate
systems, the Transform Sensor block has only one output
port for both coordinate systems.

#### Dependencies

To enable this port, under **Acceleration**, select
**Azimuth**.

### **adst** — Spherical radius coordinate of relative linear acceleration, m/s^2 physical signal

Spherical radius coordinate of the relative linear acceleration, returned as a
scalar. The setting of the **Measurement Frame** parameter affects
the expression of this signal.

#### Dependencies

To enable this port under **Acceleration**, select
**Distance**.

### **ainc** — Inclination coordinate of relative linear acceleration, rad/s^2 physical signal

Inclination coordinate of the relative linear acceleration, expressed in the
spherical coordinate system, specified as a scalar. The setting of the
**Measurement Frame** parameter affects the expression of this
signal.

#### Dependencies

To enable this port, under **Acceleration**, select
**Inclination**.

## Parameters

### **Measurement Frame** — Frame to use to express measurements `World` (default) | `Base` | `Follower` | `Non-Rotating Base` | `Non-Rotating Follower`

Frame to use to specify how to express and where to observe the measured quantiles.
The specification of this parameter does not affect the rotational quantities.

**Measurement Frame Types**

| Measurement Frame | Description |
| --- | --- |
| `World` | The world frame is an inertial frame. |
| `Base` | The base frame of the Transform Sensor block. It is a non-inertial frame. |
| `Follower` | The follower frame of the Transform Sensor block. It is a non-inertial frame. |
| `Non-Rotating Base` | The non-rotating base frame is an inertial frame that is always instantaneously coincident with the base frame of the Transform Sensor block. |
| `Non-Rotating Follower` | The non-rotating follower frame is an inertial frame that is always instantaneously coincident with the follower frame of the Transform Sensor block. |

The non-rotating base and non-rotating follower frames are not actual frames that
move through space and exist over time. Therefore, the measurements expressed in the
non-rotating frames do not support standard derivative relationships. If the block uses
a non-rotating frame as the measurement frame, the expressed acceleration measurements
often do not involve centripetal and Coriolis terms.

### **Sequence for Rotation Sequence** — Sequence of rotation axis `X-Y-X` (default) | `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

Sequence of the rotation axis for three successive elementary rotations. See Rotation Sequence Measurements for more
information.

#### Dependencies

To enable this parameter, under **Rotation**, select
**Rotation Sequence**.

## Libraries

Simscape / Multibody / Frames and Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Sensor that measures the relative spatial relationship between two frames

The Transform Sensor block measures the relative spatial
relationship between frames connected to ports **F** and
**B** of the block. The measured quantities include the relative pose,
velocity, and acceleration, which are time-varying physical signals.

You can measure the absolute translational or rotational quantities of a frame by
connecting the frame ports **F** and **B** of the block to
this frame and the world frame of the model, respectively.

The default block units are meter-kilogram-second or MKS (SI). You can use the
Simulink-PS Converter or PS-Simulink Converter block to specify the units of an input or output
signal, respectively.

### Measurement Frame

The measurement frame is:

- The frame to use to express the measured quantities.
- The location where the observer observes how the measured quantities change over
  time.

The selection of the measurement frame does not affect the rotational quantities. To see
whether a particular quantity is affected, see the Output section.

The Transform Sensor block has five different options for
the **Measurement Frame** parameter. For more information about these
options, see the **Measurement Frame** parameter in the Parameters section.

### Rotational and Translational Measurements

The block has four parameterizations to express the measured rotations: angle-axis,
quaternion, rotation matrix, and rotation sequence. To enable these parameterizations, in
the block dialog box, under **Rotation**, select corresponding parameters.
For example, select the **Angle** and **Axis** parameters
to use the angle-axis parameterization or select the **Quaternion**,
**Transform**, or **Rotation Sequence** parameter to use
the quaternion, rotation matrix, or rotation sequence parameterization.

Also, the block has various parameterizations to express rotational velocities and
accelerations: *x-*, *y-*, and *z-*
coordinates; the time derivatives of a quaternion or rotation sequence; or matrix. To enable
these parameterizations, you can select the corresponding parameters under **Angular
Velocity** or **Angular Acceleration**. For more information,
see Rotational Measurements.

The block has three coordinate systems to express the translational measurements:
Cartesian, cylindrical, and spherical. You can select one or more of them at the same time.
For more information, see Translational Measurements.

The tables summarize the coordinates of the three systems, and the images show the
diagrams of these coordinate systems. For simplicity purpose, in the images, specify the
**Measurement Frame** parameter as `Base`.

**Cartesian Coordinates**

| Coordinate | Description |
| --- | --- |
| **X** | The projection of the vector `BF` on the *x*-axis of the measurement frame. |
| **Y** | The projection of the vector `BF` on the *y*-axis of the measurement frame. |
| **Z** | The projection of the vector `BF` on the *z*-axis of the measurement frame. |

Cartesian Coordinate System

**Cylindrical Coordinates**

| Coordinate | Description |
| --- | --- |
| **Radius** | The length of the projection of the vector `BF`, in the *x-y* plane of the measurement frame. |
| **Azimuth** | The angle of the `Radius` with respect to the positive *x*-axis of the measurement frame. The angle falls in the range of [-π, π). |
| **Z** | The projection of the vector `BF` on the *z*-axis of the measurement frame. |

Cylindrical Coordinate System

**Spherical Coordinates**

| Coordinate | Description |
| --- | --- |
| **Distance** | The distance between origins of the base and follower frames. |
| **Azimuth** | The angle of the projection of the vector `BF` in the *x-y* plane with respect to the positive *x*-axis. The angle is resolved in the measurement frame and falls in the range of [-π, π). |
| **Inclination** | The angle of the vector `BF` with respect to the *x-y* plane of the measurement frame. The angle falls in the range of [-π/2, π/2]. |

Spherical Coordinate System

To use a specific coordinate system, select the corresponding parameters. For example,
if you want to use the Cartesian system to express the measured relative linear velocity of
the follower frame, under **Velocity**, select the **X**,
**Y**, and **Z** parameters.
