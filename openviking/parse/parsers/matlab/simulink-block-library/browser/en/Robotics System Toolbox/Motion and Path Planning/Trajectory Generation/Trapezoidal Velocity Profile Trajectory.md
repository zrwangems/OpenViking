---
type: simulink-block
title: 'Trapezoidal Velocity Profile Trajectory'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Motion and Path Planning / Trajectory Generation'
documentation_page: 'trapezoidalvelocityprofiletrajectory'
documentation_source_path: 'ref/trapezoidalvelocityprofiletrajectory.html'
language: en
---

# Trapezoidal Velocity Profile Trajectory

## Ports

### Input

### **Time** — Time point along trajectory scalar | vector

Time point along trajectory, specified as a scalar or vector. In general, when
specified as a scalar, this value is synced with simulation time and is used to
specify the time point for sampling the trajectory. The block outputs a vector of the
trajectory variables at that instant in time. If the time is specified as a vector,
the block outputs a matrix with each column corresponding to each element of the
vector.

**Data Types:** `single` | `double`

### **Waypoints** — Waypoint positions along trajectory *n*-by-*p* matrix

Positions of waypoints of the trajectory at given time points, specified as an
*n*-by-*p* matrix, where *n* is
the dimension of the trajectory and *p* is the number of
waypoints.

#### Dependencies

To enable this input, set **Waypoint source** to
`External`.

### **PeakVel** — Peak velocity of the velocity profile `[1;2]` (default) | scalar | *n*-element vector | *n*-by-(*p* – 1) matrix

Peak velocity of the profile segment, specified as a scalar, vector, or matrix.
This peak velocity is the highest velocity achieved during the trapezoidal velocity
profile.

A scalar value is applied to all elements of the trajectory and between all
waypoints. An *n*-element vector is applied to each element of the
trajectory between all waypoints. An *n*-by-(*p* –
1) matrix is applied to each element of the trajectory for each waypoint.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`. Set **Parameter 1**
or **Parameter 2** to `Peak Velocity`. Then, set
**Parameter source** to `External`.

**Data Types:** `single` | `double`

### **Accel** — Acceleration of the velocity profile `[2;2]` (default) | scalar | *n*-element vector | *n*-by-(*p* – 1) matrix

Acceleration of the velocity profile, specified as a scalar, vector, or matrix.
This acceleration defines the constant acceleration from zero velocity to the
**Peak velocity** value.

A scalar value is applied to all elements of the trajectory and between all
waypoints. An *n*-element vector is applied to each element of the
trajectory between all waypoints. An *n*-by-(*p* –
1) matrix is applied to each element of the trajectory for each waypoint.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`. Set **Parameter 1**
or **Parameter 2** to `Acceleration`. Then, set
**Parameter source** to `External`.

**Data Types:** `single` | `double`

### **EndTime** — Duration of trajectory segment `[1;2]` (default) | scalar | *n*-element vector | *n*-by-(*p* – 1) matrix

Duration of trajectory segment, specified as a scalar, vector, or matrix.

A scalar value is applied to all elements of the trajectory and between all
waypoints. An *n*-element vector is applied to each element of the
trajectory between all waypoints. An *n*-by-(*p* –
1) matrix is applied to each element of the trajectory for each waypoint.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`. set **Parameter 1**
or **Parameter 2** to `End Time`. Then, set
**Parameter source** to `External`.

**Data Types:** `single` | `double`

### **AccelTime** — Duration of acceleration phase of velocity profile `[1;1]` (default) | scalar | *n*-element vector | *n*-by-(*p* – 1) matrix

Duration of acceleration phase of velocity profile, specified as a scalar, vector,
or matrix.

A scalar value is applied to all elements of the trajectory and between all
waypoints. An *n*-element vector is applied to each element of the
trajectory between all waypoints. An *n*-by-(*p* –
1) matrix is applied to each element of the trajectory for each waypoint.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`. set **Parameter 1**
or **Parameter 2** to `Acceleration Time`. Then,
set **Parameter source** to `External`.

**Data Types:** `single` | `double`
### Output

### **q** — Position of trajectory scalar | vector | matrix

Position of the trajectory, specified as a scalar, vector, or matrix. If you
specify a scalar for the `Time` input with an
*n*-dimensional trajectory, the output is a vector with
*n* elements. If you specify a vector of *m*
elements for the `Time` input, the output is an
*n*-by-*m* matrix.

**Data Types:** `single` | `double`

### **qd** — Velocity of trajectory scalar | vector | matrix

Velocity of the trajectory, specified as a scalar, vector, or matrix. If you
specify a scalar for the `Time` input with an
*n*-dimensional trajectory, the output is a vector with
*n* elements. If you specify a vector of *m*
elements for the `Time` input, the output is an
*n*-by-*m* matrix.

**Data Types:** `single` | `double`

### **qdd** — Acceleration of trajectory scalar | vector | matrix

Acceleration of the trajectory, specified as a scalar, vector, or matrix. If you
specify a scalar for the `Time` input with an
*n*-dimensional trajectory, the output is a vector with
*n* elements. If you specify a vector of *m*
elements for the `Time` input, the output is an
*n*-by-*m* matrix.

**Data Types:** `single` | `double`

## Parameters

### **Waypoint source** — Source for waypoints `Internal` (default) | `External`

Specify `External` to specify the **Waypoints**
and **Time points** parameters as block inputs instead of block
parameters.

### **Waypoints** — Waypoint positions along trajectory *n*-by-*p* matrix

Positions of waypoints of the trajectory at given time points, specified as an
*n*-by-*p* matrix, where *n* is the
dimension of the trajectory and *p* is the number of waypoints.

### **Number of parameters** — Number of velocity profile parameters `0` (default) | `1` | `2`

Number of velocity profile parameters, specified as `0`,
`1`, or `2`. Increasing this value adds
**Parameter 1** and **Parameter 2** for specifying
parameters for the velocity profile.

### **Parameter 1** — Velocity profile parameter `Peak Velocity` | `Acceleration` | `End Time` | `Acceleration Time`

Velocity profile parameter, specified as `Peak Velocity`,
`Acceleration`, `End Time`, or `Acceleration
Time`. Setting this parameter creates a parameter in the mask with this value
as its name.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`.

If **Parameter Source** is set to `Internal`,
this parameter creates a parameter in the mask with this value as its name.

If **Parameter Source** is set to `External`,
this parameter creates an input port based on this value.

### **Parameter 2** — Velocity profile parameter `Peak Velocity` | `Acceleration` | `End Time` | `Acceleration Time`

Velocity profile parameter, specified as `Peak Velocity`,
`Acceleration`, `End Time`, or `Acceleration
Time`. Setting this parameter creates a parameter in the mask with this value
as its name.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`2`.

If **Parameter Source** is set to `Internal`,
this parameter creates a parameter in the mask with this value as its name.

If **Parameter Source** is set to `External`,
this parameter creates an input port based on this value.

### **Parameter source** — Source for waypoints `Internal` (default) | `External`

Specify `External` to specify the velocity profile parameters as
block inputs instead of block parameters.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`.

### **Peak velocity** — Peak velocity of the velocity profile `[1;2]` (default) | scalar | *n*-element vector | *n*-by-(*p* – 1) matrix

Peak velocity of the profile segment, specified as a scalar, vector, or matrix. This
peak velocity is the highest velocity achieved during the trapezoidal velocity
profile.

A scalar value is applied to all elements of the trajectory and between all
waypoints. An *n*-element vector is applied to each element of the
trajectory between all waypoints. An *n*-by-(*p* – 1)
matrix is applied to each element of the trajectory for each waypoint.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`. Then, set **Parameter
1** or **Parameter 2** to `Peak
Velocity`.

**Data Types:** `single` | `double`

### **Acceleration** — Acceleration of the velocity profile `[2;2]` (default) | scalar | *n*-element vector | *n*-by-(*p* – 1) matrix

Acceleration of the velocity profile, specified as a scalar, vector, or matrix. This
acceleration defines the constant acceleration from zero velocity to the **Peak
velocity** value.

A scalar value is applied to all elements of the trajectory and between all
waypoints. An *n*-element vector is applied to each element of the
trajectory between all waypoints. An *n*-by-(*p* – 1)
matrix is applied to each element of the trajectory for each waypoint.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`. Then, set **Parameter
1** or **Parameter 2** to
`Acceleration`.

**Data Types:** `single` | `double`

### **End time** — Duration of trajectory segment `[1;2]` (default) | scalar | *n*-element vector | *n*-by-(*p* – 1) matrix

Duration of trajectory segment, specified as a scalar, vector, or matrix.

A scalar value is applied to all elements of the trajectory and between all
waypoints. An *n*-element vector is applied to each element of the
trajectory between all waypoints. An *n*-by-(*p* – 1)
matrix is applied to each element of the trajectory for each waypoint.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`. Then, set **Parameter
1** or **Parameter 2** to `End
Time`.

**Data Types:** `single` | `double`

### **Acceleration time** — Duration of acceleration phase of velocity profile `[1;1]` (default) | scalar | *n*-element vector | *n*-by-(*p* – 1) matrix

Duration of acceleration phase of velocity profile, specified as a scalar, vector,
or matrix.

A scalar value is applied to all elements of the trajectory and between all
waypoints. An *n*-element vector is applied to each element of the
trajectory between all waypoints. An *n*-by-(*p* – 1)
matrix is applied to each element of the trajectory for each waypoint.

#### Dependencies

To enable this parameter, set **Number of parameters** to
`1` or `2`. Then, set **Parameter
1** or **Parameter 2** to `Acceleration
Time`.

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

Generate trajectories through multiple waypoints using trapezoidal velocity profiles

The Trapezoidal Velocity Profile Trajectory block generates a trajectory
through a given set of waypoints that follow a trapezoidal velocity profile. The block outputs
positions, velocities, and accelerations for a trajectory based on the given waypoints and
velocity profile parameters.
