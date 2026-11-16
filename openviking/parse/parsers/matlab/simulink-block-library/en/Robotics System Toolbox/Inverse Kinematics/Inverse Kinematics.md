---
type: simulink-block
title: 'Inverse Kinematics'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Inverse Kinematics'
documentation_page: 'inversekinematics'
documentation_source_path: 'ref/inversekinematics.html'
language: en
---

# Inverse Kinematics

## Ports

### Input

### **Pose** — End-effector pose 4-by-4 homogeneous transform

End-effector pose, specified as a 4-by-4 homogeneous transform. This transform
defines the desired position and orientation of the rigid body specified in the
**End effector** parameter.

**Data Types:** `single` | `double`

### **Weights** — Weights for pose tolerances six-element vector

Weights for pose tolerances, specified as a six-element vector. The first three
elements of the vector correspond to the weights on the error in orientation for the
desired pose. The last three elements of the vector correspond to the weights on the
error in the *xyz* position for the desired pose.

**Data Types:** `single` | `double`

### **InitialGuess** — Initial guess of robot configuration vector

Initial guess of robot configuration, specified as a vector of joint positions.
The number of positions is equal to the number of nonfixed joints in the
**Rigid body tree** parameter. Use this initial guess to help guide
the solver to a desired robot configuration. However, the solution is not guaranteed
to be close to this initial guess.

**Data Types:** `single` | `double`
### Output

### **Config** — Robot configuration solution vector

Robot configuration that solves the desired end-effector pose, specified as a
vector. A robot configuration is a vector of joint positions for the rigid body tree
model. The number of positions is equal to the number of nonfixed joints in the
**Rigid body tree** parameter.

**Data Types:** `single` | `double`

### **Info** — Solution information bus

Solution information, returned as a bus. The solution information bus contains
these elements:

- `Iterations` — Number of iterations run by the
  algorithm.
- `PoseErrorNorm` — The magnitude of the error between
  the pose of the end effector in the solution and the desired end-effector
  pose.
- `ExitFlag` — Code that gives more details on the
  algorithm execution and what caused it to return. For the exit flags of each
  algorithm type, see Exit Flags.
- `Status` — Character vector describing whether the
  solution is within the tolerance (`1`) or is the best possible
  solution the algorithm could find (`2`).

## Parameters

### Block Parameters

### **Rigid body tree** — Rigid body tree model `twoJointRigidBodyTree` (default) | `rigidBodyTree` object

Rigid body tree model, specified as a `rigidBodyTree` object. Create the robot model in the MATLAB® workspace before specifying in the block mask.

### **End effector** — End-effector name `'tool'` | `Select body`

End-effector name for desired pose. To see a list of bodies on the `rigidBodyTree` object, specify the **Rigid body tree**
parameter, then click **Select body**.

### **Show solution diagnostic outputs** — Enable info port `on` (default) | `off`

Select to enable the **Info** port and get diagnostic info for
the solver solution.

### Solver Parameters

### **Solver** — Algorithm for solving inverse kinematics `BFGS Gradient Projection` (default) | `Levenberg-Marquardt` | `fminconsqp`

Specify the algorithm to use for solving inverse kinematics as `BFGS
Gradient Projection`, `Levenberg-Marquardt`, or
`fminconsqp`. For details on each algorithm, see Inverse Kinematics Algorithms.

The `fminconsqp` algorithm requires Optimization Toolbox™.

### **Enforce joint limits** — Enforce rigid body tree joint limits `on` (default) | `off`

Select to enforce the joint limits specified in the **Rigid body
tree** model.

### **Maximum iterations** — Maximum number of iterations `1500` (default) | positive integer

Maximum number of iterations to optimize the solution, specified as a positive
integer. Increasing the number of iterations can improve the solution at the cost of
execution time.

### **Maximum time** — Maximum number of seconds `10` (default) | positive scalar

Specify the maximum number of seconds to run the algorithm, before timing it out,
as a positive scalar. Increasing the maximum time can improve the solution at the cost
of execution time.

#### Dependencies

To enable this parameter, set the **Solver** parameter to
either `BFGS Gradient Projection` or
`Levenberg-Marquardt`.

### **Gradient tolerance** — Threshold on gradient of cost function `1e-7` (default) | positive scalar

Threshold on the gradient of the cost function, specified as a positive scalar.
The algorithm stops if the magnitude of the gradient falls below this threshold. A low
gradient magnitude usually indicates that the solver has converged to a solution.

### **Solution tolerance** — Threshold on pose error `1e-6` (default) | positive scalar

Threshold on the magnitude of the error between the end-effector pose generated
from the solution and the desired pose, specified as a positive scalar. The
`Weights` specified for each component of the pose are included
in this calculation.

### **Step tolerance** — Minimum step size `1e-14` (default) | positive scalar

Minimum step size allowed by the solver, specified as a positive scalar. Smaller
step sizes usually mean that the solution is close to convergence.

### **Error change tolerance** — Threshold on change in pose error `1e-12` (default) | positive scalar

Threshold on the change in end-effector pose error between iterations, specified
as a positive scalar. The algorithm returns if the changes in all elements of the pose
error are smaller than this threshold.

#### Dependencies

This parameter is enabled when the **Solver** is
`Levenberg-Marquardt`.

### **Use error damping** — Enable error damping `on` (default) | `off`

Select the check box to enable error damping, then specify the `Damping
bias` parameter.

#### Dependencies

This parameter is enabled when the **Solver** is
`Levenberg-Marquardt`.

### **Damping bias** — Damping on cost function 0.0025 (default) | positive scalar

Damping on cost function, specified as a positive scalar. The Levenberg-Marquardt
algorithm has a damping feature controlled by this scalar that works with the cost
function to control the rate of convergence.

#### Dependencies

This parameter is enabled when the **Solver** is
`Levenberg-Marquardt` and **Use error damping**
is `on`.

### **Constraint tolerance** — Threshold of the constraint violations `1e-6` (default) | nonnegative numeric scalar

Specify the threshold of constraint violations as a nonnegative numeric scalar.
This indicates how much violation in joint position limits the solver allows.

#### Dependencies

To enable this parameter, set the **Solver** parameter to
`fminconsqp`.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate model using
  the MATLAB interpreter. This option shortens startup time but has a slower
  simulation speed than `Code generation`. In this mode,
  you can debug the source code of the block.
- `Code generation` — Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations, as long as the model does not change. This option requires additional
  startup time, but the speed of the subsequent simulations is comparable to
  `Interpreted execution`.

**Tunable:** No

## Libraries

Robotics System Toolbox / Manipulator Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code for some hardware boards may fail to compile for models containing an
Inverse Kinematics block if the **Maximum time** parameter
of the Inverse Kinematics block is set to a finite value. To deploy to these
boards, set **Maximum time** to `Inf`.

## Version History

**Introduced in R2018b**

### R2025a: `fmincon` available as IK solver algorithm

The Inverse Kinematics block now supports using the `fmincon`
SQP solver as the IK solver. See the **Solver**
parameter for more information.

This algorithm requires Optimization Toolbox.

## Description

Compute joint configurations to achieve an end-effector pose

The Inverse Kinematics block uses an inverse kinematic (IK) solver to
calculate joint configurations for a desired end-effector pose based on a specified rigid body
tree model. Create a rigid body tree model for your robot using the `rigidBodyTree` class. The rigid body tree model defines all the joint constraints
that the solver enforces.

Specify the `RigidBodyTree` parameter and the desired end effector inside
the block mask. You can also tune the algorithm parameters in the **Solver
Parameters** tab.

Input the desired end-effector **Pose**, the **Weights**
on pose tolerance, and an **InitialGuess** for the joint configuration. The
solver outputs a robot configuration, **Config**, that satisfies the
end-effector pose within the tolerances specified in the **Solver
Parameters** tab.
