---
type: simulink-block
title: 'Polynomial Trajectory'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'polynomialtrajectory'
documentation_source_path: 'ref/polynomialtrajectory.html'
language: en
---

# Polynomial Trajectory

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

### **Waypoints** — Waypoint positions along trajectory *n*-by-*p* matrix

Positions of waypoints of the trajectory at given time points, specified as an
*n*-by-*p* matrix, where *n* is
the dimension of the trajectory and *p* is the number of waypoints.
If you specify the **Method** as `B-spline`, these
waypoints actually define the control points for the convex hull of the B-spline, but
the first and last waypoint are still met.

#### Dependencies

To enable this input, set **Waypoint Source** to
`External`.

### **TimePoints** — Time points for waypoints of trajectory *p*-element vector

Time points for waypoints of trajectory, specified as a
*p*-element vector.

#### Dependencies

To enable this input, set **Waypoint Source** to
`External`.

### **VelBC** — Velocity boundary conditions for waypoints *n*-by-*p* matrix

Velocity boundary conditions for waypoints, specified as an
*n*-by-*p* matrix. Each row corresponds to the
velocity at each of the *p* waypoints for the respective variable in
the trajectory.

#### Dependencies

To enable this input, set **Method** to `Cubic
Polynomial` or `Quintic Polynomial` and
**Parameter Source** to `External`.

### **AccelBC** — Acceleration boundary conditions for trajectory *n*-by-*p* matrix

Acceleration boundary conditions for waypoints, specified as an
*n*-by-*p* matrix. Each row corresponds to the
acceleration at each of the *p* waypoints for the respective variable
in the trajectory.

#### Dependencies

To enable this parameter, set **Method** to `Quintic
Polynomial` and **Parameter Source** to
`External`.
### Output

### **q** — Position of trajectory scalar | vector | matrix

Position of the trajectory, specified as a scalar, vector, or matrix. If you
specify a scalar for the **Time** input with an
*n*-dimensional trajectory, the output is a vector with
*n* elements. If you specify a vector of *m*
elements for the **Time** input, the output is an
*n*-by-*m* matrix.

**Data Types:** `single` | `double`

### **qd** — Velocity of trajectory scalar | vector | matrix

Velocity of the trajectory, specified as a scalar, vector, or matrix. If you
specify a scalar for the **Time** input with an
*n*-dimensional trajectory, the output is a vector with
*n* elements. If you specify a vector of *m*
elements for the **Time** input, the output is an
*n*-by-*m* matrix.

**Data Types:** `single` | `double`

### **qdd** — Acceleration of trajectory scalar | vector | matrix

Acceleration of the trajectory, specified as a scalar, vector, or matrix. If you
specify a scalar for the **Time** input with an
*n*-dimensional trajectory, the output is a vector with
*n* elements. If you specify a vector of *m*
elements for the **Time** input, the output is an
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
dimension of the trajectory and *p* is the number of waypoints. If you
specify the **Method** as `B-spline`, these waypoints
actually define the control points for the convex hull of the B-spline, but the first
and last waypoint are still met.

#### Dependencies

To specify this parameter in the block mask, set **Waypoint
Source** to `Internal`.

### **Time points** — Time points for waypoints of trajectory *p*-element vector

Time points for waypoints of trajectory, specified as a *p*-element
vector, where *p* is the number of waypoints.

#### Dependencies

To specify this parameter in the block mask, set **Waypoint
Source** to `Internal`.

### **Method** — Method for trajectory generation `Cubic Polynomial` (default) | `Quintic Polynomial` | `B-Spline`

Method for trajectory generation, specified as either `Cubic
Polynomial`, `Quintic Polynomial`, or
`B-Spline`.

### **Parameter source** — Source for waypoints `Internal` (default) | `External`

Specify `External` to specify the **Velocity boundary
conditions** and **Acceleration boundary conditions**
parameters as block inputs instead of block parameters.

### **Velocity boundary conditions** — Velocity boundary conditions for waypoints `zeroes(2,5)` (default) | *n*-by-*p* matrix

Velocity boundary conditions for waypoints, specified as an
*n*-by-*p* matrix. Each row corresponds to the
velocity at each of the *p* waypoints for the respective variable in
the trajectory.

#### Dependencies

To enable this input, set **Method** to `Cubic
Polynomial` or `Quintic Polynomial`.

### **Acceleration boundary conditions** — Acceleration boundary conditions for trajectory *n*-by-*p* matrix

Acceleration boundary conditions for waypoints, specified as an
*n*-by-*p* matrix. Each row corresponds to the
acceleration at each of the *p* waypoints for the respective variable
in the trajectory.

#### Dependencies

To enable this parameter, set **Method** to `Quintic
Polynomial`.

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

## Libraries

Robotics System Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Generate polynomial trajectories through waypoints

The Polynomial Trajectory block generates trajectories to travel through
waypoints at the given time points using either cubic, quintic, or B-spline polynomials. The
block outputs positions, velocities, and accelerations for achieving this trajectory based on
the **Time** input. For B-spline polynomials, the waypoints actually define
the control points for the convex hull of the B-spline instead of the actual waypoints, but
the first and last waypoint are still met.

The initial and final values are held constant outside the time period defined in
**Time points**.
