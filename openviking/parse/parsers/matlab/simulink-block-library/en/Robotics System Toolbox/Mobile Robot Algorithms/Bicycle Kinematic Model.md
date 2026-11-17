---
type: simulink-block
title: 'Bicycle Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Mobile Robot Algorithms'
documentation_page: 'bicyclekinematicmodel'
documentation_source_path: 'ref/bicyclekinematicmodel.html'
language: en
---

# Bicycle Kinematic Model

## Ports
```yaml
ports:
- name: v
  summary: Vehicle speed numeric scalar
  direction: input
- name: psi
  summary: Steering angle numeric scalar
  direction: input
- name: omega
  summary: Steering angular velocity numeric scalar
  direction: input
- name: state
  summary: Pose of vehicle three-element vector
  direction: output
- name: stateDot
  summary: Derivatives of state output three-element vector
  direction: output
```

### Input

### **v** — Vehicle speed numeric scalar

Vehicle speed, specified in meters per second.

### **psi** — Steering angle numeric scalar

Steering angle of the vehicle, specified in radians.

#### Dependencies

To enable this port, set the `Vehicle
inputs` parameter to `Vehicle Speed & Steering
Angle`.

### **omega** — Steering angular velocity numeric scalar

Angular velocity of the vehicle, specified in radians per second. A positive value
steers the vehicle left and negative values steer the vehicle right.

#### Dependencies

To enable this port, set the `Vehicle
inputs` parameter to `Vehicle Speed & Heading Angular
Velocity`.
### Output

### **state** — Pose of vehicle three-element vector

Current *xy*-position and orientation of the vehicle, specified
as a *[x y theta]* vector in meters and radians.

### **stateDot** — Derivatives of `state` output three-element vector

The linear and angular velocities of the vehicle, specified as a *[xDot
yDot thetaDot]* vector in meters per second and radians per second. The
linear and angular velocities are calculated by taking the derivative of the `state`
output.
## Parameters
```yaml
parameters:
- name: Vehicle inputs
  summary: Type of speed and directional inputs for vehicle Vehicle Speed & Steering Angle (default) | Vehicle Speed & Heading
    Angular Velocity
  group: ''
- name: Wheel base
  summary: Distance between front and rear axles 1 (default) | positive numeric scalar
  group: ''
- name: Vehicle speed range
  summary: Minimum and maximum vehicle speeds [-Inf Inf] (default) | two-element vector
  group: ''
- name: Maximum steering angle
  summary: Max turning radius pi/4 (default) | numeric scalar
  group: ''
- name: Initial state
  summary: Initial pose of vehicle [0;0;0] (default) | three-element vector
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Vehicle inputs** — Type of speed and directional inputs for vehicle `Vehicle Speed & Steering Angle` (default) | `Vehicle Speed & Heading Angular Velocity`

Type of speed and directional inputs for vehicle, specified as one of these
options:

- `Vehicle Speed & Steering Angle` — Vehicle speed in meters
  per second with a steering angle in radians.
- `Vehicle Speed & Heading Angular Velocity` — Vehicle speed
  in meters per second with a heading angular velocity in radians per second.

### **Wheel base** — Distance between front and rear axles `1` (default) | positive numeric scalar

The wheel base refers to the distance between the front and rear vehicle axles,
specified in meters.

### **Vehicle speed range** — Minimum and maximum vehicle speeds `[-Inf Inf]` (default) | two-element vector

The wheel speed range is a two-element vector that provides the minimum and maximum
vehicle wheel speeds, [*MinSpeed MaxSpeed*], specified in radians per
second.

### **Maximum steering angle** — Max turning radius `pi/4` (default) | numeric scalar

The maximum steering angle, refers to the maximum amount the vehicle can be steered
to the right or left, specified in radians. This property is used to validate the
user-provided state input.

If `Maximum steering angle` is set to `pi/2`, it
results in a minimum turning radius of zero meters.

### **Initial state** — Initial pose of vehicle `[0;0;0]` (default) | three-element vector

The initial *x*-, `y`-position
and orientation, *theta*, of the vehicle.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate model using
  the MATLAB® interpreter. For more information, see Interpreted Execution vs. Code Generation (Simulink).
- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change.

**Tunable:** No
## Libraries

Robotics System Toolbox / Mobile Robot Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Compute car-like vehicle motion using bicycle kinematic model

The Bicycle Kinematic Model block creates a bicycle vehicle model to
simulate simplified car-like vehicle dynamics. This model represents a vehicle with two axles
defined by the length between the axles, `Wheel base`. The
front wheel can be turned with steering angle `psi`. The
vehicle heading `theta` is defined at the center of the rear axle.

Bicycle kinematic model diagram with x, y, theta, psi, velocity, wheel base, and turning radius labeled
