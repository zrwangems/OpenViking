---
type: simulink-block
title: 'Velocity Profiler'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'velocityprofiler'
documentation_source_path: 'ref/velocityprofiler.html'
language: en
---

# Velocity Profiler

## Ports

### Input

### **Directions** — Driving directions along path *M*-by-1 vector of 1s (forward motion) and –1s (reverse motion)

Driving directions of the vehicle along the length of the path, specified as an
*M*-by-1 vector of 1s (forward motion) and –1s (reverse motion).
Each vector element represents the driving direction of the vehicle at the
corresponding cumulative path length specified by the **CumLengths**
input port. *M* is the number of driving directions and must be equal
to the lengths of the **CumLengths** and
**Curvatures** inputs.

You can obtain **Directions** from the output of a Path Smoother
Spline block.

### **CumLengths** — Cumulative path lengths *M*-by-1 vector of monotonically increasing real-valued elements

Cumulative path lengths, in meters, specified as an *M*-by-1
vector of monotonically increasing real-valued elements. Each vector element
represents a point along the path. *M* is the number of cumulative
path lengths and must be equal to the lengths of the **Directions**
and **Curvatures** inputs.

You can obtain **CumLengths** from the output of a Path Smoother
Spline block.

### **Curvatures** — Signed path curvatures along path *M*-by-1 real-valued vector

Signed path curvatures along the length of the path, in radians per meter,
specified as an *M*-by-1 real-valued vector. Each vector element
represents the curvature of the path at the corresponding cumulative path length
specified by the **CumLengths** input port. *M* is
the number of curvatures and must be equal to the lengths of the
**Directions** and **CumLengths** inputs.

You can obtain **Curvatures** from the output of a Path Smoother
Spline block.

### **StartVelocity** — Longitudinal velocity of vehicle at start of path real scalar

Longitudinal velocity of the vehicle at the start of the path, in meters per
second, specified as a real scalar.

### **EndVelocity** — Longitudinal velocity of vehicle at end of path real scalar

Longitudinal velocity of the vehicle at the end of the path, in meters per second,
specified as a real scalar.
### Output

### **Velocities** — Velocity profile along path *M*-by-1 real-valued vector

Velocity profile along the length of the path, in meters per second, returned as
an *M*-by-1 real-valued column vector. Each vector element represents
a reference longitudinal velocity for the vehicle at the corresponding cumulative path
length specified by the **CumLengths** input port.
*M* is the number of velocities and is equal to the length of
**CumLengths**.

The output velocity values satisfy the speed, acceleration, and jerk constraints
specified in the parameters of the Velocity Profiler block. You can use
this output as the reference velocity for a vehicle controller.

**Velocities** is a variable-size output with the limitations
described in Variable-Size Signal Limitations (Simulink).

### **Times** — Vehicle times of arrival for velocity profile *M*-by-1 real-valued vector

Vehicle times of arrival for the velocity profile specified in
**Velocities**, returned as an *M*-by-1
real-valued vector. *M* is the number of vehicle times of arrival and
is equal to the length of **Velocities**. Units are in
seconds.

Each vector element represents the time that a vehicle traveling at velocity
*v* arrives at cumulative path length *p*, where:

- *v* is the corresponding velocity returned by the
  **Velocities** output port.
- *p* is the corresponding cumulative path length specified
  by the **CumLengths** input port.

Use **Times** to visualize the velocity profile over time, as
shown in the Velocity Profile of Straight Path and Velocity Profile of Path with Curve and Direction Change examples.

**Times** is a variable-size output with the limitations
described in Variable-Size Signal Limitations (Simulink).

#### Dependencies

To enable this port, select the **Show Times output port**
parameter.

## Parameters

### **Maximum longitudinal acceleration (m/s^2)** — Maximum longitudinal acceleration of vehicle `3` (default) | positive real scalar

Maximum longitudinal acceleration of the vehicle, in meters per second squared,
specified as a positive real scalar.

When developing a longitudinal controller, this parameter must be equal to the
corresponding parameter in the Longitudinal
Controller Stanley block. Otherwise, the vehicle is unable to run the
generated velocity profile.

### **Maximum longitudinal deceleration (m/s^2)** — Maximum longitudinal deceleration of vehicle `6` (default) | positive real scalar

Maximum longitudinal deceleration of the vehicle, in meters per second squared,
specified as a positive real scalar.

When developing a longitudinal controller, this parameter must be equal to the
corresponding parameter in the Longitudinal
Controller Stanley block. Otherwise, the vehicle is unable to run the
generated velocity profile.

### **Maximum allowable speed (m/s)** — Maximum allowable speed along path `10` (default) | positive real scalar

Maximum allowable speed of the vehicle along the path, in meters per second,
specified as a positive real scalar. Use this parameter to constrain the speed of the
vehicle based on passenger comfort or speed limit requirements.

When the path length is too short for the vehicle to reach this maximum speed, the
block calculates a smaller maximum speed that satisfies the path length
constraint.

In the output velocity profile, the speed of the vehicle is constrained to
[–*V*max,
*V*max], where
*V*max is the value of this parameter.

### **Maximum longitudinal jerk (m/s^3)** — Maximum longitudinal jerk `1` (default) | positive real scalar

Maximum longitudinal jerk of the vehicle along the path, in meters per second cubed,
specified as a positive real scalar.

In the output velocity profile, the longitudinal jerk of the vehicle is constrained
to [–*J*max,
*J*max], where
*J*max is the value of this parameter.

### **Maximum lateral acceleration (m/s^2)** — Maximum lateral acceleration `1` (default) | positive real scalar

Maximum lateral acceleration of the vehicle along the path, in meters per second
squared, specified as a positive real scalar.

In the output velocity profile, the lateral acceleration of the vehicle is
constrained to [–*A*max,
*A*max], where
*A*max is the value of this parameter.

### **Show Times output port** — Output times of arrival for velocity profile `off` (default) | `on`

Select this parameter to enable the **Times** output port.

### **Sample time** — Sample time of block `-1` (default) | positive real scalar

Sample time of the block, in seconds, specified as `-1` or as a
positive real scalar. The default of `-1` means that the block inherits
its sample time from upstream blocks.

Because the Velocity Profiler block outputs variable-size signals,
the sample time of the block must be discrete (nonzero). If the block inherits its
sample time from upstream blocks, those blocks must also have discrete sample
times.

### **Simulate using** — Type of simulation to run `Code Generation` (default) | `Interpreted Execution`

- `Code generation` — Simulate the model using generated C/C++
  code. The first time you run a simulation, Simulink generates C/C++ code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional startup
  time.
- `Interpreted execution` — Simulate the model using the
  MATLAB® interpreter. This option shortens startup time. In `Interpreted
  execution` mode, you can debug the source code of the block.

## Libraries

Automated Driving Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Generate velocity profile of vehicle path given kinematic constraints

The Velocity Profiler block generates a velocity profile of a driving path
that satisfies this set of specified kinematic constraints:

- The maximum allowable speed of the vehicle
- The maximum longitudinal acceleration and deceleration of the vehicle
- The maximum longitudinal jerk of the
  vehicle
- The maximum lateral
  acceleration of the vehicle

Specify the cumulative lengths along the path and the driving directions and
curvatures at each point along the path. You can obtain these values from the output of a
Path Smoother
Spline block. Also specify the longitudinal velocity of the vehicle at the start and
end of the path.

Use the generated velocity profile as the input reference velocities of a longitudinal
controller, as shown in the Automated Parking Valet in Simulink example.
