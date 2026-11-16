---
type: simulink-block
title: 'Simulation 3D Robot'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3drobot'
documentation_source_path: 'ref/simulation3drobot.html'
language: en
---

# Simulation 3D Robot

## Ports

### Input

### **Config** — Robot input joint configuration vector

Robot input joint configuration, specified as an *N*-element
vector. *N* is the number of movable joints in the robot joint
configuration in the rigid body tree, specified by the **Rigid body
tree** parameter.

#### Dependencies

To enable this port, select either the **Enable config
input signal** or **Enable grasp
settings input signals** parameter.

### **Translation** — Robot base translation vector

Robot base translation, specified as a three-element row vector, in the form
[*x*, *y* , *z*].
*x*, *y* , and *z* are the
translations along the *x*, *y*, and
*z* axes respectively. Units are in meters.

#### Dependencies

To enable this port, select the **Enable
translation and rotation input signals** parameter.

### **Rotation** — Robot base rotation vector

Robot base rotation, specified as a three-element row vector, in the form
[*yaw*, *pitch*, *roll*].
*yaw*, *pitch*, and *roll* are
the rotations about the *z*, *y*, and
*x* axes respectively. Units are in radians.

#### Dependencies

To enable this port, select the **Enable
translation and rotation input signals** parameter.

### **TargetActor** — Name of target actor to grasp fixed-sized string scalar | variable-sized uint8 array

Name of target actor to grasp, specified as fixed-sized string scalar or
variable-sized uint8 array.

#### Dependencies

To enable this port, select the **Enable grasp
settings input signals** parameter.

### **ActivateTargetGrasp** — Grasp target actor boolean

Grasp the target actor, specified as a boolean `1`
(`true`) to grasp target actor or boolean `0`
(`false`) to release target actor.

#### Dependencies

To enable this port, select the **Enable grasp
settings input signals** parameter.

### **GraspRegionTranslation** — Translational distance needed to automatically grasp target actor vector

Maximum translational distance allowed between the end effector and target actor
before the end effector automatically grasps the target actor, specified as a
three-element row vector, in the form [*x*, *y* ,
*z*]. *x*, *y* , and
*z* are the translation differences between the end effector and
the target actor along the *x*, *y*, and
*z* axes respectively. Units are in meters.

#### Dependencies

To enable this port, select the **Enable target
actor grasp region as an input signal** parameter.

### **GraspRegionRotation** — Rotational distance needed to automatically grasp target actor vector

Maximum rotational distance allowed between the end effector and target actor
before the end effector automatically grasps the target actor, specified as a
three-element row vector, in the form [*yaw*,
*pitch*, *roll*]. *yaw*,
*pitch*, and *roll* are the rotations differences
between the end effector and the target actor about the *z*,
*y*, and *x* axes respectively. Units are in
radians.

#### Dependencies

To enable this port, select the **Enable target
actor grasp region as an input signal** parameter.

### **TargetEETranslation** — Translational difference between end effector and target actor vector

Translational difference between end effector and target actor, specified as a
three-element row vector, in the form [*x*, *y* ,
*z*]. *x*, *y* , and
*z* are the translation differences between the end effector and
the target actor along the *x*, *y*, and
*z* axes respectively. Units are in meters.

#### Dependencies

To enable this port, select the **End effector to
target actor offset as an input signal** parameter.

### **TargetEERotation** — Rotational difference between end effector and target actor vector

Rotational difference between end effector and target actor, specified as a
three-element row vector, in the form [*yaw*,
*pitch*, *roll*]. *yaw*,
*pitch*, and *roll* are the rotations differences
between the end effector and the target actor about the *z*,
*y*, and *x* axes respectively. Units are in
radians.

#### Dependencies

To enable this port, select the **End effector to
target actor offset as an input signal** parameter.
### Output

### **GroundTruthConfiguration** — Ground truth for robot configuration vector

Ground truth for robot configuration, output as an *N*-element
vector. *N* is the number of movable joints in the robot joint
configuration in the rigid body tree, specified by the **Rigid body
tree** parameter.

#### Dependencies

To enable this port, select the **Enable ground
truth config output signal** parameter.

### **IsTargetGrasped** — Target actor grasped status boolean

Target actor grasped status, output as a boolean `1`
(`true`) if the end effector is grasping the target actor or
boolean `0` (`false`) if the end effector is not
grasping the target actor.

#### Dependencies

To enable this port, select the **Enable target
grasped status output signal** parameter.

### **GroundTruthTranslation** — Robot input joint configuration vector

Ground truth translation of robot base, output as a three-element row vector, in
the form [*x*, *y* , *z*].
*x*, *y* , and *z* are the
translations along the *x*, *y*, and
*z* axes respectively. Units are in meters.

#### Dependencies

To enable this port, select the **Enable ground
truth translation and rotation output signal** parameter.

### **GroundTruthRotation** — Robot input joint configuration vector

Ground truth rotation of robot base, output as a three-element row vector, in the
form [*yaw*, *pitch*, *roll*].
*yaw*, *pitch*, and *roll* are
the rotations about the *z*, *y*, and
*x* axes respectively. Units are in radians.

#### Dependencies

To enable this port, select the **Enable ground
truth translation and rotation output signal** parameter.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Parameters

### **Input type** — Robot model source `RigidBodyTree Object` (default) | `Robot Library`

Robot model source, specified as either `RigidBodyTree
Object` or `Robot Library`:

- `RigidBodyTree Object` — Specify a `rigidBodyTree` object from the
  MATLAB® workspace.
- `Robot Library` — Select a robot rigid body tree
  model from the Robotics System Toolbox™ Robot Library Data. For more information, see Robotics System Toolbox Robot Library Data.

### **Rigid body tree** — Robot rigid body tree model `twoJointRigidBodyTree` (default) | `rigidBodyTree` object | Robot name in Robot Library

Robot rigid body tree model, specified as a `rigidBodyTree` object or the name of a rigid body tree model in the
Robotics System Toolbox Robot Library Data depending on the value of the **Input type** parameter:

- `RigidBodyTree Object` — Specify a `rigidBodyTree` object from the
  MATLAB workspace.
- `Robot Library` — Select a robot rigid body tree
  model from the Robotics System Toolbox Robot Library Data. For more information, see Robotics System Toolbox Robot Library Data.

### **Actor name** — Name of actor to represent robot in Unreal Engine scene `SimulinkRobot1` (default) | string scalar

Name of actor to represent the robot in Unreal Engine scene, specified as a string scalar.

### **Use existing Simulink 3D actor specified in the actor name prompt** — Use an existing actor in the Unreal Engine scene to represent the robot `off` (default) | `on`

Select this parameter to use an existing actor in the Unreal Engine scene to represent the robot. When you select this parameter, the
Simulation 3D Robot uses the actor in the scene with the name specified by
the **Actor name** parameter. If this parameter is cleared, the
Simulation 3D Robot creates a new actor with the specified actor name in the
scene to represent the robot.

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time of the block, in seconds, specified as a positive scalar. The 3D simulation
environment frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block inherits its sample time from
the Simulation 3D Scene Configuration block.

### Initial Values

### **Initial base translation** — Initial translation of robot base `[0 0 0]` (default)

Initial translation of the robot base, specified as a three-element row vector, in
the form [*x*, *y* , *z*].
*x*, *y* , and *z* are the
translations along the *x*, *y*, and
*z* axes respectively. Units are in meters.

### **Initial base rotation** — Initial rotation of robot base `[0 0 0]` (default)

Initial rotation of the robot base, specified as a three-element row vector, in
the form [*yaw*, *pitch*, *roll*].
*yaw*, *pitch*, and *roll* are
the rotations about the *z*, *y*, and
*x* axes respectively. Units are in radians.

### **Initial joint configuration** — Initial joint configuration `[0 0]` (default) | *N*-element row vector

Initial joint configuration, specified as an *N*-element vector.
*N* is equal to the number of movable joints in the rigid body
tree.

### Grasp Settings

### **End effector** — End-effector body name `tool` (default)

Use the **Select body** button to select an end-effector body
name from one of the rigid bodies in the robot rigid body tree.

#### Dependencies

To enable this parameter, select the **Enable grasp
settings input signals** parameter.

### **End effector to target actor offset as an input signal** — `off` (default) | `on`

Select this parameter to enable input of translation and rotation difference
between the end effector and the target actor at the **TargetEETranslation**
and **TargetEERotation** input ports, respectively.

Clear this parameter to specify the translation and rotation difference using the
**End effector to target translation** and **End
effector to target actor rotation** parameters.

#### Dependencies

To enable this parameter, select the **Enable grasp
settings input signals** parameter.

### **End effector to target actor translation** — `[0 0 0]` (default) |

Translation difference between the end effector and the target actor to grasp,
specified as a three-element row vector, in the form [*x*, *y*, *z*]. *x*, *y* , and
*z* are the translations along the *x*,
*y*, and *z* axes respectively. Units are in
meters.

#### Dependencies

To enable this parameter, select the **Enable grasp
settings input signals** parameter.

### **End effector to target actor rotation** — `[0 0 0]` (default) |

Rotation difference between the end effector and the target actor to grasp,
specified as a three-element row vector, in the form [*yaw*,
*pitch*, *roll*]. *yaw*,
*pitch*, and *roll* are the rotations about the
*z*, *y*, and *x* axes
respectively. Units are in radians.

#### Dependencies

To enable this parameter, select the **Enable grasp
settings input signals** parameter.

### **Enable region-based target actor grasp approach** — Grasp target actors automatically when target actors are within specified bounds of end effector `off` (default) | `on`

Select this parameter to automatically grasp target actors using the end effector
when target actors are within specified region of the end effector.

#### Dependencies

To enable this parameter, select the **Enable grasp
settings input signals** parameter.

### **Enable target actor grasp region as an input signal** — Specify regions for grasping target actor at input ports `off` (default) | `on`

Select this parameter to enable input of grasp regions at the
**GraspRegionTranslation** and **GraspRegionRotation** input
ports.

Clear this parameter to specify the grasp regions using the **End effector to
target actor grasp region translation difference** and **End effector to
target actor grasp region rotation difference** parameters.

#### Dependencies

To enable this parameter, select the **Enable
region-based target actor grasp approach** parameter.

### **End effector to target actor grasp region translation difference** — Translation difference of grasp region `[0.2 0.2 0.2]` (default)

Translation difference of grasp region, specified as a three-element row vector,
in the form [*x*, *y* , *z*].
*x*, *y* , and *z* are the
translations along the *x*, *y*, and
*z* axes respectively. Units are in meters.

#### Dependencies

To enable this parameter, select the **Enable
region-based target actor grasp approach** parameter.

### **End effector to target actor grasp region rotation difference** — Rotation difference of grasp region `[0 0 0]` (default)

Rotation difference of grasp region, specified as a three-element row vector, in
the form [*yaw*, *pitch* , *roll*].
*yaw*, *pitch*, and *roll* are
the rotations about the z, y, and x axes respectively. Units are in radians.

#### Dependencies

To enable this parameter, select the **Enable
region-based target actor grasp approach** parameter.

### rigidBodyTree Geometry Settings

Set the parameters in this tab to enable the visualization of the rigid body tree
geometry in the 3D visualization environment.

#### Visual Geometry Visualization

### **Enable visual geometry visualization in 3D scene** — Add rigid body tree visual geometry in 3D visualization environment `on` (default) | `off`

Select this parameter to add rigid body tree visual geometry in the 3D
visualization environment.

#### Collision Geometry Visualization

### **Enable collision geometry visualization in 3D scene** — Visualize rigid body tree collision geometry in 3D visualization environment `off` (default) | `on`

Select this parameter to visualize rigid body tree collision geometry in the 3D
visualization environment.

### **Collision geometry color** — Color of the rigid body tree collision geometry `[0 1 0]` (default) | vector

Color of the rigid body tree collision geometry being visualized in the 3D
visualization environment, specified as a three-element row vector.

### **Collision geometry transparency** — Transparency of the rigid body tree collision geometry `0.1` (default) | scalar

Transparency of the rigid body tree collision geometry being visualized in the 3D
visualization environment, specified as a scalar.

### Inputs

### **Enable config input signal** — Specify desired robot configurations at input port `on` (default) | `off`

Select this parameter to specify desired robot configurations at the
**Config** input port.

#### Dependencies

To enable this parameter, clear the **Enable grasp
settings input signals** parameter.

### **Enable grasp settings input signals** — `off` (default) | `on`

Select this parameter to enable the **Grasp Settings** tab to
control how the robot grasps target actors, and the **TargetActor** and
**ActivateTargetGrasp** input ports.

### **Enable translation and rotation input signals** — Specify translation and rotation of robot base at input ports `off` (default) | `on`

Select this parameter to specify the translation and rotation of the robot base at
the **Translation** and **Rotation** ports, respectively. Enable
this port for rigid body tree models of mobile robots and mobile manipulator
robots.

### Outputs

### **Enable ground truth config output signal** — Output ground truth configuration `off` (default) | `on`

Select this parameter to output the ground truth configuration at the
**GroundTruthConfig** output port.

### **Enable target grasped status output signal** — Output grasp status `off` (default) | `on`

Select this parameter to output the grasping status of the end effector at the
**IsTargetGrasped** output port.

### **Enable ground truth translation and rotation output signal** — Output ground truth pose of robot base `off` (default) | `on`

Select this parameter to output ground truth pose of robot base at the
**GroundTruthTranslation** and **GroundTruthRotation** output
ports.

## Libraries

Robotics System Toolbox / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Implement robot in 3D environment

**Note**

Simulating models with the Simulation 3D Robot block requires
Simulink®
3D Animation™.

The Simulation 3D Robot implements a robot in a 3D simulation environment using
Unreal Engine®.

To use this block, ensure that the Simulation 3D Scene
Configuration block is in your model. If you set the **Sample
time** parameter of the Simulation 3D Robot block to
`-1`, the block inherits the sample time specified in the Simulation
3D Scene Configuration block.
