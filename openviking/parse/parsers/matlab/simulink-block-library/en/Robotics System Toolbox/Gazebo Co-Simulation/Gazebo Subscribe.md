---
type: simulink-block
title: 'Gazebo Subscribe'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Gazebo Co-Simulation'
documentation_page: 'gazebosubscribe'
documentation_source_path: 'ref/gazebosubscribe.html'
language: en
---

# Gazebo Subscribe

## Ports
```yaml
ports:
- name: IsNew
  summary: Status of custom messages in the previous time step 0 (default) | 1
  direction: output
  data_types: Boolean
- name: Msg
  summary: Gazebo custom message bus
  direction: output
  data_types: bus
```

### Output

### **IsNew** — Status of custom messages in the previous time step `0` (default) | `1`

Status of the custom message received, output as a Boolean, which indicates
whether the block output `Msg` was received in the previous time
step.

**Data Types:** `Boolean`

### **Msg** — Gazebo custom message bus

Gazebo custom message, output as a bus signal, with elements relevant to the
specific `Topic` and `Message type`.

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
  summary: Topic name of custom message /my_topic (default) | string
  group: ''
- name: Message type
  summary: Gazebo custom message type gazebo_msgs/TestPose (default) | string
  group: ''
- name: Sample time
  summary: Sampling time of input 0.001 (default) | positive
  group: ''
```

### **Topic source** — Source for specifying topic `From Gazebo` (default) | `Specify your own`

To get a topic from an existing Gazebo simulation, select `From
Gazebo`. Click the **Select** button to see a list of
available topics. To connect to a Gazebo simulation, click **Configure Gazebo
network and simulation settings** in the block mask.

To enter a custom topic without an active Gazebo connection, select `Specify
your own`. Use the `Topic` parameter to type the name of the
message.

### **Topic** — Topic name of custom message `/my_topic` (default) | string

Topic name of custom message, specified as a string.

To get a topic from an existing Gazebo simulation, select `From
Gazebo`. Click the **Select** button to see a list of
available topics. To connect to a Gazebo simulation, click **Configure Gazebo
network and simulation settings** in the block mask.

To specify a topic without connecting, select `Specify your
own`.

### **Message type** — Gazebo custom message type `gazebo_msgs/TestPose` (default) | string

Click **Select** to get a list of message types available in
Gazebo. If you choose your `Topic` from a connected Gazebo simulation,
this parameter is set automatically.

### **Sample time** — Sampling time of input `0.001` (default) | positive

Sample time indicates the interval at which messages are received from the Gazebo
simulator.
## Libraries

Robotics System Toolbox / Gazebo Co-Simulation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Receive custom messages from Gazebo server

The Gazebo Subscribe block receives custom messages from Gazebo server
based on the topic and message type that the block specifies. The block outputs the latest
message received as a bus signal, `Msg`, and a Boolean,
`IsNew`, which indicates whether a message was received during the
previous time step.

To receive custom messages, connect to a Gazebo simulation. Open the block mask and click
**Configure Gazebo network and simulation settings**. For more information
see Configure Gazebo Simulation.

This block is part of a co-simulation interface between MATLAB® and Gazebo for exchanging data and sending commands.
