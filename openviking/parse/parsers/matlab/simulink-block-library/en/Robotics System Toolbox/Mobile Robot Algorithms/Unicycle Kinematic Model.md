---
type: simulink-block
title: 'Unicycle Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Mobile Robot Algorithms'
documentation_page: 'unicyclekinematicmodel'
documentation_source_path: 'ref/unicyclekinematicmodel.html'
language: en
---

# Unicycle Kinematic Model

## Ports
```yaml
ports:
- name: dϕ/dt
  summary: Angular velocity of wheel numeric scalar
  direction: input
- name: v
  summary: Vehicle speed numeric scalar
  direction: input
- name: ω
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

### **dϕ/dt** — Angular velocity of wheel numeric scalar

Angular velocity of the wheel in radians per second.

#### Dependencies

To enable this port, set the `Vehicle
inputs` parameter to `Wheel Speed & Heading Angular
Velocity`.

### **v** — Vehicle speed numeric scalar

Vehicle speed, specified in meters per second.

#### Dependencies

To enable this port, set the `Vehicle
inputs` parameter to `Vehicle Speed & Heading Angular
Velocity`.

### **ω** — Steering angular velocity numeric scalar

Angular velocity of the vehicle, specified in radians per second. A positive value
steers the vehicle left and negative values steer the vehicle right.
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
  summary: Type of speed and directional inputs for vehicle Vehicle Speed & Heading Angular Velocity (default) | Wheel Speed
    & Heading Angular Velocity
  group: ''
- name: Wheel radius
  summary: Wheel radius of vehicle 0.1 (default) | positive numeric scalar
  group: ''
- name: Wheel speed range
  summary: Minimum and Maximum vehicle speeds [-Inf Inf] (default) | two-element vector
  group: ''
- name: Initial state
  summary: Distance between front and rear axles [0;0;0] (default) | three-element vector
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Vehicle inputs** — Type of speed and directional inputs for vehicle `Vehicle Speed & Heading Angular Velocity` (default) | `Wheel Speed & Heading Angular Velocity`

Type of speed and directional inputs to control the vehicle. Options are:

- `Vehicle Speed & Heading Angular Velocity` —
  Vehicle speed in meters per second with a heading angular velocity in radians per
  second..
- `Wheel Speed & Heading Angular Velocity` — Wheel
  speed in radians per second with a heading angular velocity in radians per
  second.

### **Wheel radius** — Wheel radius of vehicle `0.1` (default) | positive numeric scalar

The wheel radius of the vehicle, specified in meters.

### **Wheel speed range** — Minimum and Maximum vehicle speeds `[-Inf Inf]` (default) | two-element vector

The minimum and maximum wheel speeds, specified in radians per second.

### **Initial state** — Distance between front and rear axles `[0;0;0]` (default) | three-element vector

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

Compute vehicle motion using unicycle kinematic model

The Unicycle Kinematic Model block creates a unicycle vehicle model to
simulate simplified car-like vehicle dynamics. This model approximates a vehicle as a unicycle
with a given wheel radius, `Wheel radius`,
that can spin in place according to a steering angular velocity, `ω`.

Unicycle kinematic model diagram with x, y, theta, velocity, steering velocity and wheel radius labeled
