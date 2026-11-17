---
type: simulink-block
title: 'Velocity Product Torque'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Manipulator Algorithms'
documentation_page: 'velocityproducttorque'
documentation_source_path: 'ref/velocityproducttorque.html'
language: en
---

# Velocity Product Torque

## Ports
```yaml
ports:
- name: Config
  summary: Robot configuration vector
  direction: input
- name: JointVel
  summary: Joint velocities vector
  direction: input
- name: JointTorq
  summary: Joint torques vector
  direction: output
```

### Input

### **Config** — Robot configuration vector

Robot configuration, specified as a vector of positions for all
nonfixed joints in the robot model, as set by the **Rigid body
tree** parameter. You can also generate this vector for a
complex robot using the `homeConfiguration` or
`randomConfiguration`
functions inside a Constant or MATLAB
Function block.

### **JointVel** — Joint velocities vector

Joint velocities, specified as a vector. The number of joint
velocities is equal to the degrees of freedom (number of nonfixed
joints) of the robot.
### Output

### **JointTorq** — Joint torques vector

Joint torques, specified as a vector. Each element corresponds to a
torque applied to a specific joint. The number of joint torques is equal
to the degrees of freedom (number of nonfixed joints) of the
robot.
## Parameters
```yaml
parameters:
- name: Rigid body tree
  summary: Robot model twoJointRigidBodyTree (default) | RigidBodyTree object
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

### **Rigid body tree** — Robot model `twoJointRigidBodyTree` (default) | `RigidBodyTree` object

Robot model, specified as a `rigidBodyTree` object. You
can also import a robot model from an URDF (Unified Robot Description
Formation) file using `importrobot`.

The default robot model, `twoJointRigidBodyTree`, is a
robot with revolute joints and two degrees of freedom.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

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

Robotics System Toolbox / Manipulator Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Joint torques that cancel velocity-induced forces

The Velocity Product Torque block returns the torques that cancel the
velocity-induced forces for the given robot configuration (joint positions) and joint
velocities for the **Rigid body tree** robot model.
