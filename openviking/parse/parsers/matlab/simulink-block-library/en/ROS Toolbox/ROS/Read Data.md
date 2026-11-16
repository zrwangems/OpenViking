---
type: simulink-block
title: 'Read Data'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'readdata'
documentation_source_path: 'ref/readdata.html'
language: en
---

# Read Data

## Ports

### Output

### **IsNew** — New message indicator `0` | `1`

New message indicator, returned as a logical. If the output is `1`, then a new message was loaded from the rosbag file at that time. This output can be used to trigger subsystems for processing new messages received.

### **Msg** — ROS message nonvirtual bus

ROS message, returned as a nonvirtual bus. Messages are output in the order they are stored in the rosbag and synced with the simulation time.

**Data Types:** `bus`

## Parameters

### **Topic** — Topic name to extract from log file string

Topic name to extract from log file, specified as a string. This topic must exist in the loaded rosbag. Click the **Load rosbag file** Use **Select ...** to inspect the topics available and select a specific topic.

### **Sample time** — Interval between outputs `–1` (default) | scalar

Interval between outputs, specified as a scalar. In simulation, the sample time follows simulation time and not actual wall-clock time.

This default value indicates that the block sample time is *inherited*.

For more information about the inherited sample time type, see Specify Sample Time (Simulink).

## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

## Description

Play back data from log file

The Read Data block plays back rosbag logfiles by outputting the most recent message from the log file based on the current simulation time. You must load a rosbag log file (`.bag`) and specify the `Topic` in the block mask to get a stream of messages from the file. Messages on this topic are output from the file in sync with the simulation time.

In the Read Data block mask, click **Load log file data** to specify a rosbag log file (`.bag`) to load. In the **Load Log File** window, specify a **Start time offset**, in seconds, to start playback at a certain point in the file. **Duration** specifies how long the block should play back this file in seconds. By default, the block outputs all messages for the specific `Topic` in the file.
