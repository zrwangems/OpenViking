---
type: simulink-block
title: 'Current Time'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS'
documentation_page: 'currenttime'
documentation_source_path: 'ref/currenttime.html'
language: en
---

# Current Time

## Ports

### Output

### **Time** — ROS time bus | scalar

ROS time, returned as a bus signal or a scalar. The bus represents a `rosgraph_msgs/Clock` ROS message with `Sec` and `NSec` elements. The scalar is the ROS time in seconds. If no time has been received on the `/clock` topic, the block outputs `0`.

**Data Types:** `bus` | `double`

## Parameters

### **Output format** — Format of ROS time `bus` (default) | `double`

Format of ROS `Time` output, specified as either `bus` or `double`.

### **Sample time** — Interval between outputs `-1` (default) | numeric scalar

Interval between outputs, specified as a numeric scalar.

For more information, see Specify Sample Time (Simulink).

## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Retrieve current ROS time or system time

The Current Time block outputs the current ROS or system time. ROS Time is based on the system clock of your computer or the `/clock` topic being published on the ROS node.

Use this block to synchronize your simulation time with your connected ROS node.

If the `use_sim_time` ROS parameter is set to `true`, the block returns the simulation time published on the `/clock` topic. Otherwise, the block returns the system time of your machine.

Current time block workflow. Step 1. Node start. Step 2. Check whether /use\_sim\_time ROS parameter is true. Step 3. If true, subscribe to /clock topic and wait to receive time. If false, get system time. Step 4. Output the received time as the current time.
