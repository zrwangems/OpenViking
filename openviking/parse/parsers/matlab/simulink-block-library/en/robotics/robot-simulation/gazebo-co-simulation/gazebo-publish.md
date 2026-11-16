---
type: simulink-block
title: 'Gazebo Publish'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Simulation / Gazebo Co-Simulation'
documentation_page: 'gazebopublish'
documentation_source_path: 'ref/gazebopublish.html'
language: en
---

# Gazebo Publish

## Ports

### Input

### **Msg** — Gazebo custom message bus

Gazebo custom message, specified as a bus signal, with elements relevant to the
specific `Topic` and `Message type`.

**Data Types:** `bus`

## Parameters

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

Sample time indicates the interval at which messages are sent to the Gazebo
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

Send custom messages to Gazebo server

The Gazebo Publish block sends custom messages to Gazebo server based on
the topic and message type that the block specifies.

To send custom messages, connect to a Gazebo simulation. Open the block mask and click
**Configure Gazebo network and simulation settings**. For more information
see Configure Gazebo Simulation.

This block is part of a co-simulation interface between MATLAB® and Gazebo for exchanging data and sending commands.
