---
type: simulink-block
title: 'Rotation Trajectory'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'rotationtrajectory'
documentation_source_path: 'ref/rotationtrajectory.html'
language: en
---

# Rotation Trajectory

## Ports

### Input

### **Time** — Time point along trajectory scalar | vector

Time point along the trajectory, specified as a scalar or vector. In general,
when specified as a scalar, this value is synced with simulation time and is used to
specify the time point for sampling the trajectory. The block outputs a vector of the
trajectory variables at that instant in time. If the time is specified as a vector,
the block outputs a matrix with each column corresponding to each element of the
vector.

**Data Types:** `single` | `double`

### **R0** — Initial orientation four-element quaternion vector | 3-by-3 rotation matrix

Initial orientation, specified as a four-element quaternion vector or 3-by-3
rotation matrix. The function generates a trajectory that starts at the initial
orientation, **R0**, and goes to the final orientation,
**RF**.

**Example:** `[1 0 0 0]'`

#### Dependencies

To enable this input, set the **Waypoint source** to
`External`.

To specify quaternions, set **Rotation Format** parameter to
`Quaternion`.

To specify rotation matrices, set **Rotation Format** parameter
to `Rotation`.

**Data Types:** `single` | `double`

### **RF** — Final orientation four-element vector | 3-by-3 rotation matrix

Initial orientation, specified as a four-element vector or 3-by-3 rotation matrix.
The function generates a trajectory that starts at the initial orientation,
**R0**, and goes to the final orientation,
**RF**.

**Example:** `[0 0 1 0]'`

#### Dependencies

To enable this input, set the **Waypoint source** to
`External`.

To specify quaternions, set **Rotation Format** parameter to
`Quaternion`.

To specify rotation matrices, set **Rotation Format** parameter
to `Rotation`.

**Data Types:** `single` | `double`

### **TimeInterval** — Start and end times for trajectory two-element vector

Start and end times for the trajectory, specified as a two-element vector.

**Example:** `[0 10]`

#### Dependencies

To enable this input, set the **Waypoint source** to
`External`.

**Data Types:** `single` | `double`

### **TSTime** — Time scaling time points scalar | *p*-element vector

Time scaling time points, specified as a scalar or n *p*-element
vector, where *p* is the number of points for time scaling. By
default, the time scaling is a linear time scaling spanning the
**TimeInterval**. Specify the actual time scaling values in
**TimeScaling**.

If the **Time** input is specified at a time not specified by
these points, interpolation is used to find the right scaling time.

#### Dependencies

To enable this parameter, select the **Use custom time
scaling** check box and set **Parameter source** to
`External`.

To specify a scalar, the **Time** input must be a
scalar.

**Data Types:** `single` | `double`

### **TimeScaling** — Time scaling vector and first two derivatives three-element vector | 3-by-*p* matrix

Time scaling vector and its first two derivatives, specified as a three element
vector or a 3-by-*p* matrix, where *m* is the length
of **TSTime**. By default, the time scaling is a linear time scaling
spanning the **TimeInterval**.

For a nonlinear time scaling, specify the values of the time points in the first
row. The second and third rows are the velocity and acceleration of the time points,
respectively. For example, to follow the path with a linear velocity to the halfway
point, and then jump to the end, the time-scaling would
be:

```
s(1,:) = [0 0.25 0.5 1 1 1] % Position
s(2,:) = [1    1   1 0 0 0] % Velocity
s(3,:) = [0    0   0 0 0 0] % Acceleration
```

#### Dependencies

To enable this parameter, select the **Use custom time
scaling** check box and set **Parameter source** to
`External`.

To specify a three-element vector, the **Time** and
**TSTime** inputs must be a scalar.

**Data Types:** `single` | `double`
### Output

### **R** — Orientation vectors 4-by-*m* quaternion array | 3-by-3-by-*m* rotation matrix array

Orientation vectors, returned as a 4-by-*m* quaternion array or
3-by-3-by-*m* rotation matrix array, where *m* is
the number of points in the input to **Time**.

#### Dependencies

To get a quaternion array, set **Rotation Format** parameter to
`Quaternion`.

To get a rotation matrix array, set **Rotation Format**
parameter to `Rotation`.

### **omega** — Orientation angular velocity 3-by-*m* matrix

Orientation angular velocity, returned as a 3-by-*m* matrix,
where *m* is the number of points in the input to
**Time**.

### **alpha** — Orientation angular acceleration 3-by-*m* matrix

Orientation angular acceleration, returned as a 3-by-*m* matrix,
where *m* is the number of points in the input to
**Time**.

## Parameters

### **Rotation format** — Format for orientations `Quaternion` (default) | `Rotation Matrix`

Select `Rotation Matrix` to specify the **Initial
rotation** and **Final rotation** as 3-by-3 rotation
matrices and get the orientation output (port **R**) as a rotation
matrix array. By default, the initial and final rotations are specified as four-element
quaternion vectors.

### **Waypoint source** — Source for waypoints `Internal` (default) | `External`

Specify `External` to specify the **Initial
rotation**, **Final rotation**, and **Time
interval** parameters as block inputs instead of block parameters.

### **Initial rotation** — Initial orientation `[1 0 0 0]'` (default) | four-element quaternion vector | 3-by-3 rotation matrix

Initial orientation, specified as a four-element quaternion vector or 3-by-3
rotation matrix. The function generates a trajectory that starts at the
**Initial rotation** and goes to the **Final
rotation**.

#### Dependencies

To specify quaternions, set **Rotation Format** parameter to
`Quaternion`.

To specify rotation matrices, set **Rotation Format** parameter
to `Rotation`.

**Data Types:** `single` | `double`

### **Final rotation** — Final orientation `[0 0 1 0]'` (default) | four-element vector | 3-by-3 rotation matrix

Final orientation, specified as a four-element vector or 3-by-3 rotation matrix. The
function generates a trajectory that starts at the **Initial rotation**
and goes to the **Final rotation**.

#### Dependencies

To specify quaternions, set **Rotation Format** parameter to
`Quaternion`.

To specify rotation matrices, set **Rotation Format** parameter
to `Rotation`.

**Data Types:** `single` | `double`

### **Time interval** — Start and end times for trajectory `[0 10]` (default) | two-element vector

Start and end times for the trajectory, specified as a two-element vector.

**Data Types:** `single` | `double`

### **Use custom time scaling** — Enable custom time scaling `off` (default) | `on`

Enable to specify custom time scaling for the trajectory using the
**Parameter Source**, **Time scaling time**, and
**Time scaling values** parameters.

### **Parameter source** — Source for waypoints `Internal` (default) | `External`

Specify `External` to specify the **Time scaling
time** and **Time scaling values** parameters as block
inputs instead of block parameters.

#### Dependencies

To enable this parameter, select the **Use custom time scaling**
check box.

### **Time scaling time** — Time scaling time points `2:0.1:3` (default) | scalar | *p*-element vector

Time scaling time points, specified as a scalar or *p*-element
vector, where *p* is the number of points for time scaling. By default,
the time scaling is a linear time scaling spanning the **Time
interval**. Specify the actual time scaling values in **Time scaling
values**.

If the **Time** input is specified at a time not specified by these
points, interpolation is used to find the right scaling time.

#### Dependencies

To enable this parameter, select the **Use custom time scaling**
check box.

To specify a scalar, the **Time** input must be a scalar.

**Data Types:** `single` | `double`

### **Time scaling values** — Time scaling vector and first two derivatives `[0:0.1:1; ones(1,11); zeros(1,11)]` (default) | three-element vector | 3-by-*m* matrix

Time scaling vector and its first two derivatives, specified as a three-element
vector or 3-by-*p* matrix, where *p* is the length of
**Time scaling time**. By default, the time scaling is a linear time
scaling spanning the **Time interval**.

For a nonlinear time scaling, specify the values of the time points in the first
row. The second and third rows are the velocity and acceleration of the time points,
respectively. For example, to follow the path with a linear velocity to the halfway
point, and then jump to the end, the time-scaling would
be:

```
s(1,:) = [0 0.25 0.5 1 1 1] % Position
s(2,:) = [1    1   1 0 0 0] % Velocity
s(3,:) = [0    0   0 0 0 0] % Acceleration
```

#### Dependencies

To enable this parameter, select the **Use custom time scaling**
check box.

To specify a three-element vector, the **Time** and
**TSTime** inputs must be a scalar.

**Data Types:** `single` | `double`

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate model using
  the MATLAB® interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode, you
  can debug the source code of the block.
- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.

**Tunable:** No

## Libraries

Robotics System Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Generate trajectory between two orientations

The Rotation Trajectory block generates an interpolated trajectory between
two rotation matrices. The block outputs the rotation at the times given by the
**Time** input, which can be a scalar or vector.

The trajectory is computed using quaternion spherical linear interpolation (SLERP) and
finds the shortest path between points. Select the **Use custom time
scaling** check box to compute using a custom time scaling. The block uses linear
time scaling by default.

The initial and final values are held constant outside the time period defined in the
**Time interval** parameter.
