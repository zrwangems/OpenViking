---
type: simulink-block
title: 'Differential Drive Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Modeling / Mobile Robot Modeling'
documentation_page: 'differentialdrivekinematicmodel'
documentation_source_path: 'ref/differentialdrivekinematicmodel.html'
language: en
---

# Differential Drive Kinematic Model

## Ports

### Input

### **dϕL/dt** — Left wheel speed numeric scalar

Left wheel speed of the vehicle, specified in radians per second.

#### Dependencies

To enable this port, set the `Vehicle
inputs` parameter to `Wheel Speeds`.

### **dϕR/dt** — Right wheel speed numeric scalar

Right wheel speed of the vehicle, specified in radians per second.

#### Dependencies

To enable this port, set the `Vehicle
inputs` parameter to `Wheel Speeds`.

### **v** — Vehicle speed numeric scalar

Vehicle speed, specified in meters per second.

#### Dependencies

To enable this port, set the `Vehicle
inputs` parameter to `Vehicle Speed & Heading Angular
Velocity`.

### **ɷ** — Angular velocity of vehicle numeric scalar

Angular velocity of the vehicle, specified in radians per second. A positive value
steers the vehicle left and negative values steer the vehicle right.

#### Dependencies

To enable this port, set the `Vehicle
inputs` parameter to `Vehicle Speed & Heading Angular
Velocity`.
### Output

### **state** — Pose of vehicle three-element vector

Current position and orientation of the vehicle, specified as a [*x y
theta*] vector in meters and radians.

### **stateDot** — Derivatives of `state` output three-element vector

The current linear and angular velocities of the vehicle specified as a
[*xDot yDot thetaDot*] vector in meters per second and radians per
second. The linear and angular velocities are calculated by taking the derivative of
the `state`
output.

## Parameters

### **Vehicle inputs** — Type of speed and directional inputs for vehicle `Wheel Speeds` (default) | `Vehicle Speed & Heading Angular Velocity`

The format of the model input commands

- `Wheel Speeds` — Angular speeds of the two wheels in
  radians per second.
- `Vehicle Speed & Heading Angular Velocity` —
  Vehicle speed in meters per second with a heading angular velocity in radians per
  second.

### **Wheel radius** — Wheel radius of vehicle `0.05` (default) | positive numeric scalar

The radius of the wheels on the vehicle, specified in meters.

### **Wheel speed range** — Minimum and maximum vehicle speeds `[-Inf Inf]` (default) | two-element vector

The wheel speed range is a two-element vector that provides the minimum and maximum
vehicle wheel speeds, [*MinSpeed MaxSpeed*], specified in radians per
second.

### **Track width** — Track length of vehicle from wheel to wheel `0.2` (default) | numeric scalar

Length of the track from the left wheel to right wheel, specified in meters.

### **Initial state** — Initial pose of the vehicle `[0;0;0]` (default) | three-element vector

The initial *xy*-position and orientation, *θ*, of
the vehicle.

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

Compute vehicle motion using differential drive kinematic model

The Differential Drive Kinematic Model block creates a differential-drive
vehicle model to simulate simplified vehicle dynamics. This model approximates a vehicle with
a single fixed axle and wheels separated by a specified track width `Track width`.
Each of the wheels can be driven independently using speed inputs, `dϕL/dt` and `dϕR/dt`, for the left and right wheels respectively.
Vehicle speed and heading is defined from the axle center.

Differential drive kinematic model diagram with x, y, theta, velocity, track width, and wheel radius labeled
