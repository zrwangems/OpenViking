---
type: simulink-block
title: 'Minimum Jerk Polynomial Trajectory'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Motion Planning'
documentation_page: 'minimumjerkpolynomialtrajectory'
documentation_source_path: 'ref/minimumjerkpolynomialtrajectory.html'
language: en
---

# Minimum Jerk Polynomial Trajectory

## Ports

### Input

### **Time** — Time point along trajectory scalar | vector

Time point along the trajectory, specified as a scalar or vector.

- When the time is specified as a scalar, this value is synced with simulation
  time and is used to specify the time point for sampling the trajectory. The
  block outputs a vector of the trajectory variables at that instance in
  time.
- If the time is specified as a vector, the block outputs a matrix with each
  column corresponding to each element of the vector.

**Data Types:** `single` | `double`

### **Waypoints** — Waypoints positions along trajectory *n*-by-*p* matrix

Positions of waypoints of the trajectory at given time points, specified as an
*n*-by-*p* matrix. *n* is the
dimension of the trajectory and *p* is the number of
waypoints.

**Data Types:** `single` | `double`

### **TimePoints** — Time points for waypoints of trajectory *p*-element row vector

Time points for the waypoints of the trajectory, specified as a
*p*-element row vector. *p* is the number of
waypoints.

**Data Types:** `single` | `double`

### **VelBC** — Velocity boundary conditions for waypoints *n*-by-*p* matrix

Velocity boundary conditions for waypoints, specified as an
*n*-by-*p* matrix. Each row sets the velocity
boundary for the corresponding dimension of the trajectory *n* at
each of *p* waypoints.

By default, the block uses a value of `0` at the boundary
waypoints and `NaN` at the intermediate waypoints.

#### Dependencies

To enable this input port, select `Show boundary conditions input ports`.

**Data Types:** `single` | `double`

### **AccelBC** — Acceleration boundary conditions for waypoints *n*-by-*p* matrix

Acceleration boundary conditions for waypoints, specified as an
*n*-by-*p* matrix. Each row sets the acceleration
boundary for the corresponding dimension of the trajectory *n* at
each of *p* waypoints.

By default, the block uses a value of `0` at the boundary
waypoints and `NaN` at the intermediate waypoints.

#### Dependencies

To enable this input port, select `Show boundary conditions input ports`.

**Data Types:** `single` | `double`

### **JerkBC** — Jerk boundary conditions for waypoints *n*-by-*p* matrix

Jerk boundary conditions for waypoints, specified as an
*n*-by-*p* matrix. Each row sets the jerk boundary
for the corresponding dimension of the trajectory *n* at each of
*p* waypoints.

By default, the block uses a value of `0` at the boundary
waypoints and `NaN` at the intermediate waypoints.

#### Dependencies

To enable this input port, select `Show boundary conditions input ports`.

**Data Types:** `single` | `double`
### Output

### **q** — Positions of trajectory *n*-element vector | *n*-by-*m* matrix

Positions of the trajectory, returned as an *n*-element vector or
*n*-by-*m* matrix.

- If you specify a scalar for the `Time` input with an
  *n*-dimensional trajectory, the output is a vector with
  *n*-elements.
- If you specify a vector of *m*-elements for the `Time` input, the output is an
  *n*-by-*m* matrix.

**Data Types:** `single` | `double`

### **qd** — Velocities of trajectory *n*-element vector | *n*-by-*m* matrix

Velocities of the trajectory, returned as an *n*-element vector
or *n*-by-*m* matrix.

- If you specify a scalar for the `Time` input with an
  *n*-dimensional trajectory, the output is a vector with
  *n*-elements.
- If you specify a vector of *m*-elements for the `Time` input, the output is an
  *n*-by-*m* matrix.

**Data Types:** `single` | `double`

### **qdd** — Accelerations of trajectory *n*-element vector | *n*-by-*m* matrix

Accelerations of the trajectory, returned as an *n*-element
vector or *n*-by-*m* matrix.

- If you specify a scalar for the `Time` input with an
  *n*-dimensional trajectory, the output is a vector with
  *n*-elements.
- If you specify a vector of *m*-elements for the `Time` input, the output is an
  *n*-by-*m* matrix.

**Data Types:** `single` | `double`

### **qddd** — Jerks of trajectory *n*-element vector | *n*-by-*m* matrix

Jerks of the trajectory, returned as an *n*-element vector or
*n*-by-*m* matrix.

- If you specify a scalar for the `Time` input with an
  *n*-dimensional trajectory, the output is a vector with
  *n*-elements.
- If you specify a vector of *m*-elements for the `Time` input, the output is an
  *n*-by-*m* matrix.

**Data Types:** `single` | `double`

### **TimeOfArrival** — Time of arrival at each waypoint *p*-element vector

Time of arrival at each waypoint, returned as a *p*-element
vector. *p* is the number of waypoints.

**Data Types:** `single` | `double`

### **PolynomialCoefs** — Polynomial coefficients *n*(*p*`–``1`)-by-`8` matrix

Polynomial coefficients, returned as an
*n*(*p*`–``1`)-by-`8`
matrix. *n* is the dimension of the trajectory and
*p* is the number of waypoints. Each set of *n*
rows defines the coefficients for the polynomial that described each variable
trajectory.

#### Dependencies

To enable this output port, select `Show polynomial coefficients output port`.

**Data Types:** `single` | `double`

### **Status** — Status of trajectory generation three-element vector of the form `[SingularityStatus MaxIterStatus MaxTimeStatus]`

Status of trajectory generation, returned as a three-element vector of the form
`[SingularityStatus
MaxIterStatus
MaxTimeStatus]`.

*SingularityStatus* returned as `0` or
`1` indicates the occurrence of singularity. If singularity occurs
reduce the `Maximum segment time` to `Minimum segment time` ratio.

*MaxIterStatus* returned as `0` or
`1` indicates if the number of iterations for the solver has
exceeded `Maximum iterations`.

*MaxTimeStatus* returned as `0` or
`1` indicates if the time for the solver has exceeded `Maximum time`.

#### Dependencies

To enable this output port, select `Show status output port`.

**Data Types:** `uint8`

## Parameters

### **Show boundary conditions input ports** — Accept boundary condition inputs `off` (default) | `on`

Select this parameter to input the velocity, acceleration, and jerk boundary
conditions, at the `VelBC`, `AccelBC`, and `JerkBC` ports, respectively.

**Tunable:** No

### **Show polynomial coefficients output port** — Output polynomial coefficients `off` (default) | `on`

Select this parameter to output polynomial coefficients at the `PolynomialCoefs` port.

**Tunable:** No

### **Show status output port** — Output status `off` (default) | `on`

Select this parameter to output status at the `Status` port.

**Tunable:** No

### **Time allocation** — Enable time allocation `off` (default) | `on`

Enable to specify time allocation for the trajectory using the `Time
weight`, `Minimum segment time`, `Maximum segment time`, `Maximum iterations`, and `Maximum time` parameters.

**Tunable:** No

### **Time weight** — Weight for time allocation `100` (default) | positive scalar

Weight for time allocation, specified as a positive scalar.

**Tunable:** No

#### Dependencies

To enable this parameter, select `Time
allocation`.

### **Minimum segment time** — Minimum time segment length `0.1` (default) | positive scalar | (*p*`–``1`)-element positive row vector

Minimum time segment length, specified as a positive scalar or
(*p*`–``1`)-element positive row
vector. *p* is the number of waypoints.

**Tunable:** No

#### Dependencies

To enable this parameter, select `Time
allocation`.

### **Maximum segment time** — Maximum time segment length `1` (default) | positive scalar | (*p*`–``1`)-element positive row vector

Maximum time segment length, specified as a positive scalar or
(*p*`–``1`)-element positive row
vector. *p* is the number of waypoints.

**Tunable:** No

#### Dependencies

To enable this parameter, select `Time
allocation`.

### **Maximum iterations** — Maximum iterations for solver `1500` (default) | positive integer scalar

Maximum iterations for solver, specified as a positive integer scalar.

**Tunable:** No

#### Dependencies

To enable this parameter, select `Time
allocation`.

### **Maximum time** — Maximum time for solver `10` (default) | positive scalar

Maximum time for solver, specified as a positive scalar.

**Tunable:** No

#### Dependencies

To enable this parameter, select `Time
allocation`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Select the type of simulation to run from these options:

- `Interpreted execution` — Simulate model using
  the MATLAB® interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode,
  you can debug the source code of the block.
- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.

**Tunable:** No

## Libraries

UAV Toolbox / Algorithms Robotics System Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Generate minimum jerk polynomial trajectories through multiple waypoints

The Minimum Jerk Polynomial Trajectory block generates minimum jerk
polynomial trajectories that pass through the waypoints at the times specified in time points.
The block outputs positions, velocities, accelerations, jerks, and time of arrival for
achieving this trajectory based on the `Time` input.

The block also accepts boundary conditions for waypoints. The block also outputs the
coefficients for the polynomials and status of the trajectory generation.

The initial and final values of positions, velocities, accelerations, and jerks of the
trajectory are held constant outside the time period defined in `TimePoints` input.
