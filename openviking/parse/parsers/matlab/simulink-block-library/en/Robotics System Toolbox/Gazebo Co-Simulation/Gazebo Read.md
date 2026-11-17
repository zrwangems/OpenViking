---
type: simulink-block
title: 'Gazebo Read'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazeboread'
documentation_source_path: 'ref/gazeboread.html'
language: en
---

# Gazebo Read

## Ports
```yaml
ports:
- name: IsNew
  summary: Status of messages in the previous time step 0 (default) | 1
  direction: output
  data_types: Boolean
- name: Msg
  summary: Gazebo message bus
  direction: output
  data_types: bus
```

### Output

### **IsNew** — Status of messages in the previous time step `0` (default) | `1`

Status of the message received, output as a Boolean, which indicates whether the
block output `Msg` was received in the previous time step.

**Data Types:** `Boolean`

### **Msg** — Gazebo message bus

Gazebo message, output as a bus signal, with elements relevant to the specific
`Topic` and `Message type`.

The `Msg` output always outputs the most recent message
received.

**Data Types:** `bus`
## Parameters
```yaml
parameters:
- name: Topic source
  summary: Source for specifying topic From Gazebo (default) | Specify your own
  group: ''
- name: Topic
  summary: Topic name of message /my_topic (default) | string
  group: ''
- name: Message type
  summary: Gazebo message type gazebo_msgs/Pose (default) | gazebo_msgs/Image | gazebo_msgs/IMU | gazebo_msgs/LaserScan |
    gazebo_msgs/JointState | gazebo_msgs/LinkState
  group: ''
- name: Sample time
  summary: Sampling time of input 0.001 (default) | positive scalar
  group: ''
- name: Number of Joint Axis
  summary: Number of joint axis 2 (default) | positive integer in range [1, 100]
  group: ''
```

### **Topic source** — Source for specifying topic `From Gazebo` (default) | `Specify your own`

To get a topic from an existing Gazebo simulation, select `From
Gazebo`. Click the **Select** button to see a list of
available topics. To connect to a Gazebo simulation, click **Configure Gazebo
network and simulation settings** in the block mask.

To enter a custom topic without an active Gazebo connection, select
`Specify your own`. Use the `Topic`
parameter to type the name of the message.

### **Topic** — Topic name of message `/my_topic` (default) | string

Topic name of message, specified as a string.

To get a topic from an existing Gazebo simulation, select `From
Gazebo`. Click the **Select** button to see a list of
available topics. To connect to a Gazebo simulation, click **Configure Gazebo
network and simulation settings** in the block mask.

To specify a topic without connecting, select `Specify your
own`.

### **Message type** — Gazebo message type `gazebo_msgs/Pose` (default) | `gazebo_msgs/Image` | `gazebo_msgs/IMU` | `gazebo_msgs/LaserScan` | `gazebo_msgs/JointState` | `gazebo_msgs/LinkState`

Click **Select** to get a list of message types available in
Gazebo. If you choose your `Topic` from a connected Gazebo
simulation, this parameter is set automatically.

### **Sample time** — Sampling time of input `0.001` (default) | positive scalar

Sample time indicates when, during simulation, the block produces outputs and if
appropriate, updates its internal state.

### **Number of Joint Axis** — Number of joint axis `2` (default) | positive integer in range `[1, 100]`

Select `Make Joint Axis Related Bus Signal to Fixed Dimensions`
to convert the joint-axis-related bus signal from variable dimension to fixed dimension.
Then specify the number of joint axis.

#### Dependencies

To enable this parameter, set `Message type` to
`gazebo_msgs/JointState` and select the `Make Joint Axis
Related Bus Signal to Fixed Dimensions` check box.
## Libraries

Robotics System Toolbox / Gazebo Co-Simulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Receive messages from Gazebo server

The Gazebo Read block receives messages from the Gazebo server based on the
topic and message type that the block specifies. The block outputs the latest message received
as a bus signal, `Msg`, and a Boolean, `IsNew`, which
indicates whether a message was received during the previous time step.

To receive messages from Gazebo server, connect to a Gazebo simulation. Open the block
mask and click **Configure Gazebo network and simulation settings**. For more
information see Configure Gazebo Simulation.

This block is part of a co-simulation interface between MATLAB® and Gazebo for exchanging data and sending commands. To see a basic example,
check Perform Co-Simulation Between Simulink and Gazebo
