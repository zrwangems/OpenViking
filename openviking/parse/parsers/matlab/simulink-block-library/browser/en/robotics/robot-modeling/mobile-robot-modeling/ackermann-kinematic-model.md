---
type: simulink-block
title: 'Ackermann Kinematic Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Modeling / Mobile Robot Modeling'
documentation_page: 'ackermannkinematicmodel'
documentation_source_path: 'ref/ackermannkinematicmodel.html'
language: en
---

# Ackermann Kinematic Model

## Ports

### Input

### **v** — Vehicle speed numeric scalar

Vehicle speed, specified in meters per second.

### **dψ/dt** — Steering angular velocity numeric scalar

Steering angular velocity of the vehicle, specified in radians per second.
### Output

### **state** — State of vehicle four-element vector

Current *xy*-position, orientation, and steering angle, specified
as [*x y θ ψ*], in meters and radians.

### **stateDot** — Derivatives of `state` output four-element vector

The linear and angular velocities of the vehicle, specified as a [*xDot
yDot thetaDot psiDot*] vector in meters per second and radians per second.
The linear and angular velocities are calculated by taking the time derivatives of the
`state`
output.

## Parameters

### **Wheel base** — Distance between front and rear axles `1` (default) | positive numeric scalar

The wheel base refers to the distance between the front and rear vehicle axles,
specified in meters.

### **Vehicle speed range** — Minimum and maximum vehicle speeds `[-Inf Inf]` (default) | two-element vector

The wheel speed range is a two-element vector that provides the minimum and maximum
vehicle wheel speeds, [*MinSpeed MaxSpeed*], specified in radians per
second.

### **Maximum steering angle** — Maximum steering angle `pi/4` (default) | positive numeric scalar

The maximum steering angle, refers to the maximum amount the vehicle can be steered
to the right or left, specified in radians. The default value is
`pi/4`.

### **Initial state** — Initial state of vehicle `[0;0;0;0]` (default) | four-element vector

The initial *x*-, `y`-position,
heading angle, *theta*, and steering angle, *psi*, of
the vehicle.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate model using
  the MATLAB® interpreter. For more information, see Interpreted Execution vs. Code Generation (Simulink).
- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
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

Car-like vehicle motion using Ackermann kinematic model

The Ackermann Kinematic Model block creates a car-like vehicle model that
uses Ackermann steering. This model represents a vehicle with two axles separated by the
distance, `Wheel base`. The
state of the vehicle is defined as a four-element vector, [*x y θ ψ*], with
an global *xy-*position, vehicle heading, *θ*, and steering
angle, *ψ*. The vehicle heading and *xy*-position are
defined at the center of the rear axle. Angles are specified in radians and the global
positions are specified in meters. The steering input for the vehicle is given as `dψ/dt`, in
radians per second.

Ackermann kinematic model diagram with x, y, theta, psi, velocity, wheel base, and turning radius labeled
