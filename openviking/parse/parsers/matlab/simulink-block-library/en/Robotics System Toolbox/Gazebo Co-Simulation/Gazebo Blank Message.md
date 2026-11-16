---
type: simulink-block
title: 'Gazebo Blank Message'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazeboblankmessage'
documentation_source_path: 'ref/gazeboblankmessage.html'
language: en
---

# Gazebo Blank Message

## Ports

### Output

### **Msg** — Blank message bus

Blank message, returns as a bus signal with elements relevant to the specific
`Message type`. The `Msg` output always outputs
the most recent message received.

There are seven different message types with specific fields:

- `ApplyLinkWrench`:

  - `model_name` –– Variable-size `uint8`
    array representing the name of the model in the Gazebo simulator.
  - `link_name` –– Variable-size `uint8`
    array representing the name of the link in the model in the Gazebo
    simulator.
  - `force_type` –– Variable-size `uint8`
    array specified as `'SET'` or `'ADD'`.
    `'SET'` overwrites any existing force message for the
    specified duration. `'ADD'` adds the value with existing
    messages.
  - `Fx, fy, fz` –– `double` values
    specifying the amount of force applied to the Gazebo model link in world
    coordinates and Newtons.
  - `torque_type` –– Variable-size `uint8`
    array specified as `'SET'` or `'ADD'`.
    `'SET'` overwrites any existing torque message for the
    specified duration. `'ADD'` adds the value with existing
    messages.
  - `Tx, ty, tz` –– `double` values
    specifying the amount of torque applied to the Gazebo model link in world
    coordinates and Newton-meters.
  - `duration` –– Bus containing seconds and nanoseconds as
    `double` integers, which specify how long to apply the
    torque in simulation time.

- `ApplyJointTorque`:

  - `model_name` –– Variable-size `uint8`
    array representing the name of the model in the Gazebo simulator.
  - `joint_name` –– Variable-size `uint8`
    array representing the name of the joint in the model in the Gazebo
    simulator.
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

### **Message type** — Type of message `ApplyLinkWrench` (default) | `ApplyJointTorque` | `SetLinkWorldPose` | `SetLinkLinearVelocity` | `SetLinkAngularVelocity` | `SetJointPosition` | `SetJointVelocity`

Click **Select** to get a list of message types available in
Gazebo.

### **Sample time** — Sampling time of input `0.001` (default) | positive

Sample time indicates when, during simulation, the block produces outputs and if
appropriate, updates its internal state.

## Libraries

Robotics System Toolbox / Gazebo Co-Simulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Create blank Gazebo command

The Gazebo Blank Message block creates a blank Gazebo message or a command
based on the specified type. The block output is a bus signal that contains the required
elements for the type of command. Use a Bus Assignment block to modify specific
fields in the bus signal. The bus signal initializes with zero value (ground).

To create blank Gazebo command, connect to a Gazebo simulation. Open the block mask and
click **Configure Gazebo network and simulation settings**. For more
information see Configure Gazebo Simulation.

This block is part of a co-simulation interface between MATLAB® and Gazebo for exchanging data and sending commands. To see a basic example,
check Perform Co-Simulation Between Simulink and Gazebo.
