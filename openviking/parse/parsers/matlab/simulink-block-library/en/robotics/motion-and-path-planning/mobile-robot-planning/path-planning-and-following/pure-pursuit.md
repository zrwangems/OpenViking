---
type: simulink-block
title: 'Pure Pursuit'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Motion and Path Planning / Mobile Robot Planning / Path Planning and Following'
documentation_page: 'purepursuit'
documentation_source_path: 'ref/purepursuit.html'
language: en
---

# Pure Pursuit

## Ports

### Input

### **Pose** — Current vehicle pose `[x y theta]` vector

Current vehicle pose, specified as an `[x y theta]`
vector, which corresponds to the *x-y* position and
orientation angle, *theta*. Positive angles are
measured counterclockwise from the positive
*x*-axis.

### **Waypoints** — Waypoints [ ] (default) | *n*-by-2 array

Waypoints, specified as an *n*-by-2 array of
`[x y]` pairs, where *n* is the
number of waypoints. You can generate the waypoints using path planners
like `mobileRobotPRM` or specify
them as an array in Simulink®.

### **Desired Linear Velocity** — Linear velocity scalar in meters per second

Desired linear velocity, specified as a scalar in meters per second.
The controller assumes that the vehicle drives at a constant linear
velocity and that the computed angular velocity is independent of the
linear velocity.

#### Dependencies

To enable this port, select the **Specify desired linear
velocity from input port** parameter.

### **Lookahead Distance** — Look-ahead distance scalar in meters per second

Look-ahead distance, specified as a scalar in meters per second. The
look-ahead distance changes the response of the controller. A vehicle
with a higher look-ahead distance produces smooth paths but takes larger
turns at corners. A vehicle with a smaller look-ahead distance follows
the path closely and takes sharp turns, but oscillate along the path.
For more information on the effects of look-ahead distance, see Pure Pursuit Controller.

#### Dependencies

To enable this port, select the **Specify lookahead
distance from input port** parameter.
### Output

### **Linear Velocity** — Linear velocity scalar in meters per second

Linear velocity, returned as a scalar in meters per second.

**Data Types:** `double`

### **Angular Velocity** — Angular velocity scalar in radians per second

Angular velocity, returned as a scalar in radians per second.

**Data Types:** `double`

### **Target Direction** — Target direction for vehicle scalar in radians

Target direction for the vehicle, returned as a scalar in radians. The
forward direction of the vehicle is considered zero radians, with
positive angles measured counterclockwise. This output can be used as
the input to the **TargetDir** port for the Vector Field Histogram (Navigation Toolbox)
block.

#### Dependencies

To enable this port, select the **Show Target Direction
output port** parameter.

## Parameters

### **Specify desired linear velocity from input port** — Enable input port for desired linear velocities `off` (default) | `on`

Select this parameter to enable input of desired linear velocities at the
**Desired Linear
Velocity** input port.

Clear this parameter to specify desired linear velocity using the
**Desired linear velocity
(m/s)** parameter

### **Desired linear velocity (m/s)** — Linear velocity `0.1` (default) | scalar

Desired linear velocity, specified as a scalar in meters per second. The
controller assumes that the vehicle drives at a constant linear velocity and
that the computed angular velocity is independent of the linear
velocity.

#### Dependencies

To enable this parameter, clear the **Specify desired linear
velocity from input port** parameter.

### **Maximum angular velocity (rad/s)** — Angular velocity `1.0` (default) | scalar

Maximum angular velocity, specified as a scalar in radians per second. The
controller saturates the absolute angular velocity output at the given
value.

### **Specify lookahead distance from input port** — Enable input port for look-ahead distances `off` (default) | `on`

Select this parameter to enable input of look-ahead distances at the **Lookahead
Distance** input port.

Clear this parameter to specify desired linear velocity using the
**Lookahead distance
(m)** parameter

### **Lookahead distance (m)** — Look-ahead distance `1.0` (default) | scalar

Look-ahead distance, specified as a scalar in meters. The look-ahead
distance changes the response of the controller. A vehicle with a higher
look-ahead distance produces smooth paths but takes larger turns at corners.
A vehicle with a smaller look-ahead distance follows the path closely and
takes sharp turns, but oscillate along the path. For more information on the
effects of look-ahead distance, see Pure Pursuit Controller.

#### Dependencies

To enable this parameter, clear the **Specify lookahead
distance from input port** parameter.

### **Show Target Direction output port** — Target direction indicator `off` (default) | `on`

Select this parameter to enable the **Target Direction** output
port. This port gives the target direction as an angle in radians from the
forward position, with positive angles measured counterclockwise.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

- `Interpreted execution` — Simulate
  model using the MATLAB® interpreter. This option shortens startup time but has
  a slower simulation speed than `Code
  generation`. In this mode, you can debug the source
  code of the block.
- `Code generation` — Simulate model
  using generated C code. The first time you run a simulation,
  Simulink generates C code for the block. The C code is reused
  for subsequent simulations, as long as the model does not change.
  This option requires additional startup time, but the speed of the
  subsequent simulations is comparable to `Interpreted
  execution`.

**Tunable:** No

## Libraries

Robotics System Toolbox / Mobile Robot Algorithms Navigation Toolbox / Control Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

### R2024a: Specify linear velocity and look-ahead distance at input ports, and renamed output ports

The Pure Pursuit block has two sets of changes:

1. You can now specify the desired linear velocity at the **Desired Linear
   Velocity** input port by selecting the **Specify
   desired linear velocity from input port**
   parameter.
2. You can now specify the desired linear velocity at the **Lookahead
   Distance** input port by selecting the **Specify
   lookahead distance from input port** parameter.
3. The output ports and a parameter have new names. This table shows the
   names prior to R2024a, and the names for R2024a and after.

   | Name Prior to R2024a | Name for R2024a and after |
   | --- | --- |
   | **LinVel** output port | **Linear Velocity** output port |
   | **AngVel** output port | **Angular Velocity** output port |
   | **TargetDir** output port | **Target Direction** output port |
   | **Show TargetDir output port** parameter | **Show Target Direction output port** parameter |

## Description

Linear and angular velocity control commands

The Pure Pursuit block computes linear and angular velocity commands for
following a path using a set of waypoints and the current pose of a car-like or
differential-drive vehicle. The block takes updated poses to update velocity commands
for the vehicle to follow a path along a desired set of waypoints. Use the
**Max angular velocity** and **Desired linear
velocity** parameters to update the velocities based on the performance of
the vehicle.

The look-ahead distance port and parameter compute a look-ahead point on the path, which is an
instantaneous local goal for the vehicle. The angular velocity command is computed based
on this point. Changing the look-ahead distance has a significant impact on the
performance of the algorithm. A higher look-ahead distance results in a smoother
trajectory for the vehicle, but can cause the vehicle to cut corners along the path. Too
low of a look-ahead distance can result in oscillations in tracking the path, causing
unstable behavior. For more information on the pure pursuit algorithm, see Pure Pursuit Controller.
