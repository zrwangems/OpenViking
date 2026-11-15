---
type: simulink-block
title: 'Read Data'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Access in Simulink'
documentation_page: 'readdataros2'
documentation_source_path: 'ref/readdataros2.html'
language: en
---

# Read Data

## Ports

### Output

### **IsNew** — New message indicator logical scalar

New message indicator, returned as a logical scalar. If the output is
`1`, then the block loaded a new message from the ROS 2 bag file at
the corresponding time. This output can be used to trigger subsystems for processing
new messages.

**Data Types:** `Boolean`

### **Msg** — ROS 2 message nonvirtual bus

ROS 2 message, returned as a nonvirtual bus. Messages are returned in the order
they are stored in the ROS 2 bag file and synced with the simulation time.

**Data Types:** `bus`

## Parameters

### **Topic** — Topic name to extract from log file string scalar | character vector

Specify the name of the topic to extract from the log file. This topic must exist in
the loaded ROS 2 bag file. Click **Select**  to inspect the available
topics and select a specific topic.

### **Sample time** — Interval between outputs `-1` (default) | scalar

Specify the interval between outputs. In simulation, the sample time follows
simulation time rather than wall-clock time.

The default value indicates that the block sample time is inherited. For more
information about the inherited sample time type, see Specify Sample Time (Simulink).

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2025a: Read unregistered message types

You can now play unregistered message types from a ROS 2 bag file.

### R2024a: MCAP Storage Format Support

You can now read data from a bag folder containing one or more MCAP files.

## Description

Play back data from ROS 2 log file

The Read Data block plays back ROS 2 bag log files by outputting the most
recent message from the log file, based on the current simulation time. You must load a ROS 2
bag file in DB3 or MCAP file format and specify a topic, using the **Topic**
parameter, to get a stream of messages from the file. The block outputs messages of this topic
from the file in sync with the simulation time. If a folder contains multiple ROS 2 bag files,
you can also read them using the Read Data block by loading the
`metadata` file with `.yaml` extension.

In the Read Data block mask, select **Load logfile data**
to specify a ROS 2 bag file to load. In the **Load Logfile** dialog box,
specify the full path to the log file, or select Browse and navigate to the bag file you want
to load. To start playback at a certain point in the file, specify **Start time
offset** in seconds. To specify how long the block plays back this file from the
specified start time, specify **Duration** in seconds. By default, the block
outputs all messages for the specified topic in the file.
