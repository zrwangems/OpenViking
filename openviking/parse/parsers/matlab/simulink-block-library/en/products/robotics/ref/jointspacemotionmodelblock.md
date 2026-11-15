---
type: simulink-block
title: 'Joint Space Motion Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Modeling / Manipulator Modeling'
documentation_page: 'jointspacemotionmodelblock'
documentation_source_path: 'ref/jointspacemotionmodelblock.html'
language: en
---

# Joint Space Motion Model

## Ports

### Input

### **qRef** — Joint positions *n*-element vector

*n*-element vector representing the desired joint positions of
radians, where *n* is the number of nonfixed joints in the `rigidBodyTree` object of the `Rigid body
tree` parameter.

#### Dependencies

To enable this port, set the `Motion
Type` parameter to `Computed Torque Control`,
`PD Control`, or `Independent Joint
Motion`.

### **qRefDot** — Joint velocities *n*-element vector

*n*-element vector representing the desired joint velocities of
radians per second, where *n* is the number of nonfixed joints in the
`rigidBodyTree` object of the `Rigid body
tree` parameter.

#### Dependencies

To enable this port, set the `Motion
Type` parameter to `Computed Torque Control`,
or `Independent Joint Motion`.

### **qRefDDot** — Joint accelerations *n*-element vector

*n*-element vector representing the desired joint velocities of
radians per second squared, where *n* is the number of nonfixed
joints in the `rigidBodyTree` object of the `Rigid body
tree` parameter.

#### Dependencies

To enable this port, set the `Motion
Type` parameter to `Computed Torque Control`,
`PD Control`, or `Independent Joint
Motion`.

### **FExt** — External forces acting on system 6-by-*m* matrix

A 6-by-*m* matrix of external forces for the *m*
bodies in the `rigidBodyTree` object of the `Rigid body
tree` parameter.

#### Dependencies

To enable this port, set the `Show external
force input` parameter to `on`.
### Output

### **q** — Joint positions *n*-element vector

Joint positions output as an *n*-element vector in radians or
meters, where *n* is the number of nonfixed joints in the `rigidBodyTree` object of the `Rigid body
tree` parameter.

### **qd** — Joint velocities *n*-element vector

Joint velocities output as an *n*-element vector in radians per
second or meters per second, where *n* is the number of nonfixed
joints in the `rigidBodyTree` object of the `Rigid body
tree` parameter

### **qdd** — Joint accelerations *n*-element vector

Joint accelerations output as an *n*-element vector in radians
per second squared or meters per second squared, where *n* is the
number of nonfixed joints in the `rigidBodyTree` object of the `Rigid body
tree` parameter

## Parameters

### **Rigid body tree** — Robot model `twoJointRigidBodyTree` (default) | `RigidBodyTree` object

Robot model, specified as a `rigidBodyTree` object. You can also import
a robot model from an URDF (Unified Robot Description Formation) file using `importrobot`.

The default robot model, `twoJointRigidBodyTree`, is a manipulator
with revolute joints and two degrees of freedom.

### **Motion Type** — Type of motion computed by motion model `Computed Torque Control` (default) | `Independent Joint Motion` | `PD Control` | `Open Loop Dynamics`

Type of motion, specified as a string scalar or character vector that defines the
closed-loop joint-space behavior that the object models. Options are:

- `Computed Torque Control` — Compensates for full-body
  dynamics and assigns the error dynamics specified in the `Natural
  frequency` and `Damping
  ratio` parameters.
- `Independent Joint Motion` — Models each joint as an
  independent second order system using the error dynamics specified by the `Natural
  frequency` and `Damping
  ratio` parameters.
- `PD Control` — Uses proportional-derivative (PD)
  control on the joints based on the specified `Proportional
  gain` and `Derivative
  gain` parameters.
- `Open Loop Dynamics` — Disables inputs except for
  `FExt`
  if `Show external
  force input` is enabled. This is an open-loop configuration.

### **Specification format** — Inputs to control robot `Damping Ratio / Natural Frequency` (default) | `Step Response`

Inputs to control the robot system. Options are:

- `Damping Ratio / Natural Frequency` — Setting the
  natural frequency using the `Natural
  frequency` parameter of the system in Hz, and the damping ratio using
  the `Damping
  ratio` parameter.
- `Step Response` — Model at discrete time-steps with a
  fixed settling time and overshoot using the `Settling
  time` and the `Overshoot` parameters.

#### Dependencies

To enable this parameter, set the `Motion
Type` parameter to `Computed Torque Control` or
`Independent Joint Motion`.

### **Damping ratio** — Damping ratio of system `1` (default) | numeric scalar

Damping ratio use to decay system oscillations. A value of `1`
results in no damping, whereas `0` fully dampens the system.

#### Dependencies

To enable this parameter, set the `Specification
format` parameter to `Damping Ratio / Natural
Frequency`.

### **Natural frequency** — Natural frequency of system `10` (default) | numeric scalar

Frequency of the system oscillations if unimpeded, specified in Hz.

#### Dependencies

To enable this parameter, set the `Specification
format` parameter to `Damping Ratio / Natural
Frequency`.

### **Settling time** — Settling time of system `0.59` (default) | numeric scalar

The time taken for each joint to reach steady state, measured in seconds.

#### Dependencies

To enable this parameter, set the `Specification
format` parameter to `Step Response`.

### **Overshoot** — System overshoot `0.0` (default) | numeric scalar

The maximum value that the system exceeds the target position.

#### Dependencies

To enable this parameter, set the `Specification
format` parameter to `Step Response`.

### **Proportional gain** — Proportional gain for PD Control `100` (default) | *n*-by-*n* matrix | scalar

Proportional gain for proportional-derivative (PD) control, specified as a scalar or
*n*-by-*n* matrix, where *n* is the
number of nonfixed joints in the `rigidBodyTree` object of the `Rigid body
tree` parameter.

#### Dependencies

To enable this parameter, set the `Specification
format` parameter to `PD Control`.

### **Derivative gain** — Derivative gain for PD control `10` (default) | *n*-by-*n* matrix | scalar

Derivative gain for proportional-derivative (PD) control, specified as a scalar or
*n*-by-*n* matrix, where *n* is the
number of nonfixed joints in the `rigidBodyTree` object of the `Rigid body
tree` parameter

#### Dependencies

To enable this parameter, set the `Specification
format` parameter to `PD Control`.

### **Show external force input** — Display `FExt` port `off` (default) | `on`

Enable this parameter to input external forces using the `FExt`
port.

#### Dependencies

To enable this parameter, set the `Motion
Type` parameter to `Computed Torque Control`,
`PD Control`, or `Open Loop
Dynamics`.

### **Initial joint configuration** — Initial joint positions `0` (default) | *n*-element vector | scalar

Initial joint positions, specified as a *n*-element vector or
scalar in radians. *n* is the number of nonfixed joints in the `rigidBodyTree` object in the `Rigid body
tree` parameter.

### **Initial joint velocities** — Initial joint velocities `0` (default) | *n*-element vector | scalar

Initial joint velocities, specified as a *n*-element vector or
scalar in radians per second. *n* is the number of nonfixed joints in
the `rigidBodyTree` object in the `Rigid body
tree` parameter.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate model using
  the MATLAB® interpreter. For more information, see Interpreted Execution vs. Code Generation (Simulink).
- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change.

**Tunable:** No

## Libraries

Robotics System Toolbox / Manipulator Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

### R2024a: Static memory allocation support

Joint Space Motion Model now supports code generation with disabled dynamic memory
allocation. For more information about disabling dynamic memory allocation, see Set Dynamic Memory Allocation Threshold (MATLAB Coder).

## Description

Model rigid body tree motion given joint-space inputs

The Joint Space Motion Model block models the closed-loop joint-space
motion of a manipulator robot, specified as a `rigidBodyTree` object. The motion model behavior is defined by the `Motion Type`
parameter.

For more details about the equations of motion, see Joint-Space Motion Model.
