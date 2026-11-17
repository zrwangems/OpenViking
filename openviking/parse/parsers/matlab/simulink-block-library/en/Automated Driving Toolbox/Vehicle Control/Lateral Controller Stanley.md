---
type: simulink-block
title: 'Lateral Controller Stanley'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Vehicle Control'
documentation_page: 'lateralcontrollerstanley'
documentation_source_path: 'ref/lateralcontrollerstanley.html'
language: en
---

# Lateral Controller Stanley

## Ports
```yaml
ports:
- name: RefPose
  summary: Reference pose [*x*, *y*, *Θ*] vector
  direction: input
  data_types: single | double
- name: CurrPose
  summary: Current pose [*x*, *y*, *Θ*] vector
  direction: input
  data_types: single | double
- name: CurrVelocity
  summary: Current longitudinal velocity real scalar
  direction: input
  data_types: single | double
- name: Direction
  summary: Driving direction of vehicle 1 (forward motion) | -1 (reverse motion)
  direction: input
- name: Curvature
  summary: Curvature of path real scalar
  direction: input
- name: CurrYawRate
  summary: Current yaw rate real scalar
  direction: input
- name: CurrSteer
  summary: Current steering angle real scalar
  direction: input
- name: SteerCmd
  summary: Steering angle command real scalar
  direction: output
```

### Input

### **RefPose** — Reference pose [*x*, *y*, *Θ*] vector

Reference pose, specified as an [*x*, *y*,
*Θ*] vector. *x* and *y* are in
meters, and *Θ* is in degrees.

*x* and *y* specify the reference point to steer the vehicle toward. *Θ* specifies the orientation angle of the path at this reference point and is positive in the counterclockwise direction.

- For a vehicle in forward motion, the reference point is the point on the path that is closest to the center of the vehicle's front axle.

  Vehicle in forward motion with reference point on path marked. Units are in world coordinates.
- For a vehicle in reverse motion, the reference point is the point on the path that is closest to the center of the vehicle's rear axle.

  Vehicle in reverse motion with reference point on path marked. Units are in world coordinates.

**Data Types:** `single` | `double`

### **CurrPose** — Current pose [*x*, *y*, *Θ*] vector

Current pose of the vehicle, specified as an [*x*, *y*,
*Θ*] vector. *x* and *y* are in
meters, and *Θ* is in degrees.

*x* and *y* specify the location of the vehicle, which is
defined as the center of the vehicle's rear axle.

*Θ* specifies the orientation angle of the vehicle at location (*x*,*y*) and is positive in the counterclockwise direction.

Vehicle with pose marked. Units are in world coordinates.

For more details on vehicle pose, see Coordinate Systems in Automated Driving Toolbox.

**Data Types:** `single` | `double`

### **CurrVelocity** — Current longitudinal velocity real scalar

Current longitudinal velocity of the vehicle, specified as a real scalar. Units are in meters
per second.

- If the vehicle is in forward motion, then this value must be greater than 0.
- If the vehicle is in reverse motion, then this value must be less than 0.
- A value of 0 represents a vehicle that is not in motion.

**Data Types:** `single` | `double`

### **Direction** — Driving direction of vehicle `1` (forward motion) | `-1` (reverse motion)

Driving direction of the vehicle, specified as `1` for forward
motion or `-1` for reverse motion. The driving direction determines
the position error and angle error used to compute the steering angle command. For
more details, see Algorithms.

### **Curvature** — Curvature of path real scalar

Curvature of the path at the reference point, in radians per meter, specified as a
real scalar.

- For a vehicle in forward motion, the reference point is the point on the path
  that is closest to the center of the vehicle's front axle.

  Vehicle in forward motion with reference point on path marked. Units are in world coordinates.
- For a vehicle in reverse motion, the reference point is the point on the path
  that is closest to the center of the vehicle's rear axle.

  Vehicle in reverse motion with reference point on path marked. Units are in world coordinates.

You can obtain the curvature of a path from the **Curvatures**
output port of a Path Smoother
Spline block. You can also obtain curvatures of lane boundaries from the
output lane boundary structures of a Scenario
Reader block.

#### Dependencies

To enable this port, set **Vehicle model** to
`Dynamic bicycle model`.

### **CurrYawRate** — Current yaw rate real scalar

Current yaw rate of the vehicle, in degrees per second, specified as a real
scalar. The current yaw rate is the rate of change in the angular velocity of the
vehicle.

#### Dependencies

To enable this port, set **Vehicle model** to
`Dynamic bicycle model`.

### **CurrSteer** — Current steering angle real scalar

Current steering angle of the vehicle, in degrees, specified as a real scalar.
This value is positive in the counterclockwise direction.

Vehicle with front wheels turned and steering angle marked

For more details, see Coordinate Systems in Automated Driving Toolbox.

#### Dependencies

To enable this port, set **Vehicle model** to
`Dynamic bicycle model`.
### Output

### **SteerCmd** — Steering angle command real scalar

Steering angle command, in degrees, returned as a real scalar. This value is
positive in the counterclockwise direction.

Vehicle with front wheels turned and steering angle marked

For more details, see Coordinate Systems in Automated Driving Toolbox.
## Parameters
```yaml
parameters:
- name: Vehicle model
  summary: Vehicle model Kinematic bicycle model (default) | Dynamic bicycle model
  group: ''
- name: Position gain of forward motion
  summary: Position gain of vehicle in forward motion 2.5 (default) | positive real scalar
  group: ''
- name: Position gain of reverse motion
  summary: Position gain of vehicle in reverse motion 2.5 (default) | positive real scalar
  group: ''
- name: Yaw rate feedback gain
  summary: Yaw rate feedback gain 2.5 (default) | nonnegative real scalar
  group: ''
- name: Steering angle feedback gain
  summary: Steering angle feedback gain 2.5 (default) | nonnegative real scalar
  group: ''
- name: Wheelbase of vehicle (m)
  summary: Distance between front and rear axle 2.8 (default) | real scalar
  group: ''
- name: Vehicle mass (kg)
  summary: Vehicle mass 1575 (default) | positive real scalar
  group: ''
- name: Longitudinal distance from center of mass to front axle (m)
  summary: Distance to front axle 1.2 (default) | positive real scalar
  group: ''
- name: Longitudinal distance from center of mass to rear axle (m)
  summary: Distance to rear axle 1.6 (default) | positive real scalar
  group: ''
- name: Front tire corner stiffness (N/rad)
  summary: Cornering stiffness of front tires 19000 (default) | positive real scalar
  group: ''
- name: Maximum steering angle (deg)
  summary: Maximum allowed steering angle 35 (default) | real scalar in the range (0, 180)
  group: ''
```

### **Vehicle model** — Vehicle model `Kinematic bicycle model` (default) | `Dynamic bicycle model`

Select the type of vehicle model to set the Stanley method control law used by the
block.

- `Kinematic bicycle model` — Kinematic bicycle model for
  path following in low-speed environments such as parking lots, where inertial
  effects are minimal
- `Dynamic bicycle model` — Dynamic bicycle model for
  path following in high-speed environments such as highways, where inertial effects
  are more pronounced

### **Position gain of forward motion** — Position gain of vehicle in forward motion `2.5` (default) | positive real scalar

Position gain of the vehicle when it is in forward motion, specified as a positive
scalar. This value determines how much the position error affects the steering angle.
Typical values are in the range [1, 5]. Increase this value to increase the magnitude of
the steering angle.

### **Position gain of reverse motion** — Position gain of vehicle in reverse motion `2.5` (default) | positive real scalar

Position gain of the vehicle when it is in reverse motion, specified as a positive
scalar. This value determines how much the position error affects the steering angle.
Typical values are in the range [1, 5]. Increase this value to increase the magnitude of
the steering angle.

### **Yaw rate feedback gain** — Yaw rate feedback gain `2.5` (default) | nonnegative real scalar

Yaw rate feedback gain, specified as a nonnegative real scalar. This value
determines how much weight is given to the current yaw rate of the vehicle when the
block computes the steering angle command.

#### Dependencies

To enable this parameter, set **Vehicle model** to
`Dynamic bicycle model`.

### **Steering angle feedback gain** — Steering angle feedback gain `2.5` (default) | nonnegative real scalar

Steering angle feedback gain, specified as a nonnegative real scalar. This value
determines how much the difference between the current steering angle command,
**SteerCmd**, and the current steering angle,
**CurrSteer**, affects the next steering angle command.

#### Dependencies

To enable this parameter, set **Vehicle model** to
`Dynamic bicycle model`.

### **Wheelbase of vehicle (m)** — Distance between front and rear axle `2.8` (default) | real scalar

Distance between the front and rear axle of the vehicle, in meters, specified as a
real scalar. This value applies only when the vehicle is in forward motion, that is,
when the **Direction** input port is `1`.

#### Dependencies

To enable this parameter, set **Vehicle model** to
`Kinematic bicycle model`.

### **Vehicle mass (kg)** — Vehicle mass `1575` (default) | positive real scalar

Vehicle mass, in kilograms, specified as a positive real scalar.

#### Dependencies

To enable this parameter, set **Vehicle model** to
`Dynamic bicycle model`.

### **Longitudinal distance from center of mass to front axle (m)** — Distance to front axle `1.2` (default) | positive real scalar

Longitudinal distance from the vehicle's center of mass to its front wheel axle, in
meters, specified as a positive real scalar.

#### Dependencies

To enable this parameter, set **Vehicle model** to
`Dynamic bicycle model`.

### **Longitudinal distance from center of mass to rear axle (m)** — Distance to rear axle `1.6` (default) | positive real scalar

Longitudinal distance from the vehicle's center of mass to its rear wheel axle, in
meters, specified as a positive real scalar.

#### Dependencies

To enable this parameter, set **Vehicle model** to
`Dynamic bicycle model`.

### **Front tire corner stiffness (N/rad)** — Cornering stiffness of front tires `19000` (default) | positive real scalar

Cornering stiffness of front tires, in Newtons per radian, specified as a positive
real scalar.

#### Dependencies

To enable this parameter, set **Vehicle model** to
`Dynamic bicycle model`.

### **Maximum steering angle (deg)** — Maximum allowed steering angle `35` (default) | real scalar in the range (0, 180)

Maximum allowed steering angle of the vehicle, in degrees, specified as a real
scalar in the range (0, 180).

The output from the **SteerCmd** port is saturated to the range
[–*M*, *M*], where *M* is the value
of the **Maximum steering angle (deg)** parameter.

- Values below –*M* are set to –*M*.
- Values above *M* are set to *M*.
## Libraries

Automated Driving Toolbox / Vehicle Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Control steering angle of vehicle for path following by using Stanley method

The Lateral Controller Stanley block computes the steering angle command,
in degrees, that adjusts the current pose of a vehicle to match a reference pose, given the
vehicle's current velocity and direction. The controller computes this command using the
Stanley method [1], whose control law is
based on both a kinematic and dynamic bicycle model. To change between models, use the
**Vehicle model** parameter.

- The kinematic bicycle model is suitable for path following in low-speed environments
  such as parking lots, where inertial effects are minimal.
- The dynamic bicycle model is suitable for path following in high-speed environments
  such as highways, where inertial effects are more pronounced. This vehicle model provides
  additional parameters that describe the dynamics of the vehicle.
