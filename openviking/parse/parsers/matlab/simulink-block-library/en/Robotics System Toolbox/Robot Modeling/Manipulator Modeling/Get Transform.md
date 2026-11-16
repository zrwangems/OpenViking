---
type: simulink-block
title: 'Get Transform'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Modeling / Manipulator Modeling'
documentation_page: 'gettransformblock'
documentation_source_path: 'ref/gettransformblock.html'
language: en
---

# Get Transform

## Ports

### Input

### **Config** — Robot configuration vector

Robot configuration, specified as a vector of positions for all
nonfixed joints in the robot model, as set by the **Rigid body
tree** parameter. You can also generate this vector for a
complex robot using the `homeConfiguration` or
`randomConfiguration`
functions inside a Constant or MATLAB
Function block.
### Output

### **Transform** — Homogeneous transform 4-by-4 matrix

Homogeneous transform, returned as a 4-by-4 matrix.

## Parameters

### **Rigid body tree** — Robot model `twoJointRigidBodyTree` (default) | `RigidBodyTree` object

Robot model, specified as a `rigidBodyTree` object. You
can also import a robot model from an URDF (Unified Robot Description
Formation) file using `importrobot`.

The default robot model, `twoJointRigidBodyTree`, is a
robot with revolute joints and two degrees of freedom.

### **Target body** — Target body name body name

Target body name, specified as a body name from the robot model specified
in **Rigid body tree**. To access body names from the robot
model, click **Select body**. The target frame is the
coordinate system you want to transform points into.

### **Source body** — Source body name body name

Source body name, specified as a body name from the robot model specified
in **Rigid body tree**.To access body names from the robot
model, click **Select body**. The source frame is the
coordinate system you want points transformed from.

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

Get transform between body frames

The Get Transform block returns the homogeneous transformation between
body frames on the **Rigid body tree** robot model. Specify a `rigidBodyTree` object for the robot model, and select a source and target
body in the block.

The block uses **Config**, the robot configuration (joint positions)
input, to calculate the transformation from the source body to the target body. This
transformation is used to convert coordinates from the source to the target body. To
convert to base coordinates, use the base body name as the **Target
body** parameter.
