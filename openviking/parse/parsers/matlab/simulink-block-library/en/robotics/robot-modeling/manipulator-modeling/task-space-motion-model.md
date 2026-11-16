---
type: simulink-block
title: 'Task Space Motion Model'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Modeling / Manipulator Modeling'
documentation_page: 'taskspacemotionmodelblock'
documentation_source_path: 'ref/taskspacemotionmodelblock.html'
language: en
---

# Task Space Motion Model

## Ports

### Input

### **refPose** — Desired end-effector pose 4-by-4 matrix

Homogenous transformation matrix representing the desired end-effector pose,
specified in meters.

### **refVel** — Desired end-effector velocities 6-element vector

6-element vector representing the desired linear and angular velocities of the end
effector, specified in meters per second and radians per second.

### **FExt** — External forces 6-by-*m* matrix

6-by-*m* matrix representing external forces, where each column
is a wrench in the form `[Fx; Fy; Fz; Tx; Ty; Tz]`.
`Fx`, `Fy`, and `Fz` are the
forces in the *x*-, *y*-, and
*z*-axes, in Newtons. `Tx`, `Ty`,
and `Tz` are the torques about the *x*-,
*y*-, and *z*-axes, in Newton-meters.
*m* is the number of bodies in the `rigidBodyTree` object in the **Rigid body
tree** parameter. Each of the *m* wrenches act on the
rigid body frame of the corresponding index in the rigid body tree. For example, the
third column of `FExt` specifies the wrench acting on the third
rigid body in the rigid body tree.

#### Dependencies

To enable this port, set the `Show external
force input` parameter to `on`.
### Output

### **q** — Joint positions *n*-element vector

Joint positions output as an *n*-element vector in radians or
meters, where *n* is the number of nonfixed joints in the `rigidBodyTree` object in the `Rigid body
tree` parameter.

### **qd** — Joint velocities *n*-element

Joint velocities output as an *n*-element vector in radians per
second or meters per second, where *n* is the number of nonfixed
joints in the `rigidBodyTree` object in the `Rigid body
tree` parameter.

### **qdd** — Joint accelerations *n*-element

Joint accelerations output as an *n*-element in radians per
second squared or meters per second squared, where *n* is the number
of nonfixed joints in the `rigidBodyTree` object in the `Rigid body
tree` parameter.

## Parameters

### **Rigid body tree** — Rigid body tree `twoJointRigidBodyTree` object (default) | `RigidBodyTree` object

Robot model, specified as a `RigidBodyTree` object. You can also
import a robot model from an URDF (Unified Robot Description Formation) file using
`importrobot`.

The default robot model, `twoJointRigidBodyTree`, is a robot with
revolute joints and two degrees of freedom.

### **End effector** — End effector body `tool` (default)

This parameter defines the body that will be used as the end effector, and for which
the task space motion is defined. The property must correspond to a body name in the
`rigidBodyTree` object of the property.
Click **Select body** to select a body from the
`rigidBodyTree`. If the `rigidBodyTree` is updated
without also updating the end effector, the body with the highest index is assigned by
default.

### **Proportional gain** — Proportional gain for PD Control `500*eye(6)` (default) | 6-by-6 matrix

Proportional gain for proportional-derivative (PD) control, specified as a 6-by-6
matrix.

### **Derivative gain** — Derivative gain for PD Control `100*eye(6)` (default) | 6-by-6 matrix

Derivative gain for proportional-derivative (PD) control, specified as a 6-by-6
matrix.

### **Joint damping** — Damping ratios `[1 1]` (default) | *n*-element vector | scalar

Damping ratios on each joint, specified as a scalar or *n*-element
vector, where *n* is the number of nonfixed joints in the `rigidBodyTree` object in the `Rigid body
tree` parameter.

### **Show external force input** — Display `FExt` port `off` (default) | `on`

Click the check-box to enable this parameter to input external forces using the
`FExt`
port.

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
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
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

Task Space Motion Model now supports code generation with disabled dynamic memory
allocation. For more information about disabling dynamic memory allocation, see Set Dynamic Memory Allocation Threshold (MATLAB Coder).

## Description

Model rigid body tree motion given task-space inputs

The Task Space Motion Model block models the closed-loop task-space motion
of a manipulator, specified as a `rigidBodyTree` object. The motion model behavior
is defined using proportional-derivative (PD) control.

For more details about the equations of motion, see Task-Space Motion Model.
