---
type: simulink-block
title: 'PX4 uORB Message'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4uorbmessage'
documentation_source_path: 'px4/ref/px4uorbmessage.html'
language: en
---

# PX4 uORB Message

## Ports

Not documented in R2025b.

## Parameters

### **Topic** — Name of the uORB topic for creating the blank uORB message vehicle\_gps\_position (default) | One of the uORB topic

Select the name of the uORB topic for the block to create a blank message. Click
**Select** to browse the topic names available in the
`px4/Firmware/msg` directory that you downloaded.

### **Sample time** — Interval between outputs `Inf` (default) | numeric scalar

Enter the time interval at which the block provides blank uORB messages.

The default value indicates that the block output never changes. Using this value
speeds the simulation and code generation by eliminating the need to recompute the block
output. Otherwise, the block outputs a new blank message at each interval of **Sample time**.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 uORB Read and Write Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Create a blank message using specified uORB topic

The PX4 uORB Message block creates a Simulink® nonvirtual bus with a blank message corresponding to the selected uORB topic.
The block creates uORB message bus that work with `PX4 uORB Write`
block.

### Output

### **Msg** — Blank uORB message nonvirtual bus

Blank uORB message, returned as a nonvirtual bus. The type of uORB message is
specified using the parameter, `Topic`. All elements of the bus are
initialized to 0. Connect a Bus Assignment block to modify specific fields in the
message.

**Data Types:** `bus`
