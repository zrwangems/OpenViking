---
type: simulink-block
title: 'Gazebo Apply Command'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazeboapplycommand'
documentation_source_path: 'ref/gazeboapplycommand.html'
language: en
---

# Gazebo Apply Command

## Ports

### Input

### **Cmd** — Gazebo Command bus

Gazebo command message, specified as a bus. The command is an instruction for a
specified model link or joint. Specify the model name as part of the bus signal using
the Gazebo Select
Entity block.

There are seven different command types with specific fields:

- `ApplyLinkWrench`:

  - `model_name` –– Variable-size `uint8`
    array representing the name of the model in the Gazebo simulator. You can
    specify this field using the Gazebo
    Select Entity block.
  - `link_name` –– Variable-size `uint8`
    array representing the name of the link in the model in the Gazebo
    simulator. You can specify this field using the Gazebo
    Select Entity block.
  - `force_type` –– Variable-size `uint8`
    array specified as `'SET'` or `'ADD'`.
    `'SET'` overwrites any existing force command for the
    specified duration. `'ADD'` adds the value with existing
    commands.
  - `Fx, fy, fz` –– `double` values
    specifying the amount of force applied to the Gazebo model link in world
    coordinates and Newtons.
  - `torque_type` –– Variable-size `uint8`
    array specified as `'SET'` or `'ADD'`.
    `'SET'` overwrites any existing torque command for the
    specified duration. `'ADD'` adds the value with existing
    commands.
  - `Tx, ty, tz` –– `double` values
    specifying the amount of torque applied to the Gazebo model link in world
    coordinates and Newton-meters.
  - `duration` –– Bus containing seconds and nanoseconds as
    `double` integers, which specify how long to apply the
    torque in simulation time.

- `ApplyJointTorque`:

  - `model_name` –– Variable-size `uint8`
    array representing the name of the model in the Gazebo simulator. You can
    specify this field using the Gazebo
    Select Entity block.
  - `joint_name` –– Variable-size `uint8`
    array representing the name of the joint in the model in the Gazebo
    simulator. You can specify this field using the Gazebo
    Select Entity block.
  - `index` –– `uint32` integer that
    identifies which joint axis the torque should be applied to.
  - `effort` –– `double` scalar value
    specifying the amount of torque or force to apply to the joint.
  - `duration` –– Bus containing seconds and nanoseconds as
    `double` integers, which specify how long to apply the
    torque in simulation time.

- `SetLinkWorldPose`:

  - `model_name` –– Variable-size `uint8`
    array representing the name of the model in the Gazebo simulator.
  - `link_name` –– Variable-size `uint8`
    array representing the name of the link in the model in the Gazebo
    simulator.
  - `world_pose` –– Bus containing position and orientation
    as `[x
    y
    z]` and `[x
    y
    z
    w]`
    `double` vectors, respectively.
  - `duration` –– Bus containing seconds and nanoseconds as
    `double` integers, which specify how long to apply the
    torque in simulation time.

- `SetLinkLinearVelocity`:

  - `model_name` –– Variable-size `uint8`
    array representing the name of the model in the Gazebo simulator.
  - `link_name` –– Variable-size `uint8`
    array representing the name of the link in the model in the Gazebo
    simulator.
  - `velocity` –– Bus containing linear velocity as
    `[x
    y
    z]`
    `double` vector.
  - `duration` –– Bus containing seconds and nanoseconds as
    `double` integers, which specify how long to apply the
    torque in simulation time.

- `SetLinkAngularVelocity`:

  - `model_name` –– Variable-size `uint8`
    array representing the name of the model in the Gazebo simulator.
  - `link_name` –– Variable-size `uint8`
    array representing the name of the link in the model in the Gazebo
    simulator.
  - `velocity` –– Bus containing angular velocity as
    `[x
    y
    z]`
    `double` vector.
  - `duration` –– Bus containing seconds and nanoseconds as
    `double` integers, which specify how long to apply the
    torque in simulation time.

- `SetJointPosition`:

  - `model_name` –– Variable-size `uint8`
    array representing the name of the model in the Gazebo simulator.
  - `joint_name` –– Variable-size `uint8`
    array representing the name of the joint in the model in the Gazebo
    simulator.
  - `index` –– `uint32` integer that
    identifies which joint axis the torque should be applied to.
  - `position` –– `double` scalar value
    representing the joint position.
  - `duration` –– Bus containing seconds and nanoseconds as
    `double` integers, which specify how long to apply the
    torque in simulation time.

- `SetJointVelocity`:

  - `model_name` –– Variable-size `uint8`
    array representing the name of the model in the Gazebo simulator.
  - `joint_name` –– Variable-size `uint8`
    array representing the name of the joint in the model in the Gazebo
    simulator.
  - `index` –– `uint32` integer that
    identifies which joint axis the torque should be applied to.
  - `velocity` –– `double` scalar value
    representing the joint velocity.
  - `duration` –– Bus containing seconds and nanoseconds as
    `double` integers, which specify how long to apply the
    torque in simulation time.

  **Note**

  `SetJointVelocity` uses the *Set Instantaneous
  Velocity* method to set the joint velocity. For more information
  see, Setting Velocity on Links And Joints.

**Note**

- If a `duration` is `1.005` seconds, it
  would be `1` second and `5000000` nanoseconds
  as a bus.

**Data Types:** `bus`

## Parameters

### **Command type** — Type of command `ApplyLinkWrench` (default) | `ApplyJointTorque` | `SetLinkWorldPose` | `SetLinkLinearVelocity` | `SetLinkAngularVelocity` | `SetJointPosition` | `SetJointVelocity`

Click **Select** to get a list of command types available in
Gazebo. The input `Cmd` must contain the correct command message
structure that matches this type.

### **Sample time** — Sampling time of input `0.001` (default) | positive

Sample time indicates the interval which commands are sent to the Gazebo
simulator.

## Libraries

Robotics System Toolbox / Gazebo Co-Simulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Send command to Gazebo simulator

The Apply Command block sends commands to a Gazebo simulation. The block
accepts a command message, input as a bus signal, and sends the command to the Gazebo server.

To send command messages, connect to a Gazebo simulation. Open the block mask and click
**Configure Gazebo network and simulation settings**. For more information
see Configure Gazebo Simulation.

This block is part of a co-simulation interface between MATLAB® and Gazebo for exchanging data and sending commands. To see a basic example,
check Perform Co-Simulation Between Simulink and Gazebo.
