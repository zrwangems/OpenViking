---
type: simulink-block
title: 'Current Time'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'ROS 2'
documentation_page: 'currenttimeros2'
documentation_source_path: 'ref/currenttimeros2.html'
language: en
---

# Current Time

## Ports

### Output

### **Time** — ROS 2 time bus | scalar

ROS 2 time, returned as a bus signal or a scalar. The `Output
format` parameter determines the format of this output port. The bus
represents a `builtin_interfaces/Time` ROS 2 message with
`sec` and `nanosec` elements. The scalar is the
ROS 2 time in seconds. If the block does not receive a time from the
`/clock` topic, this output is `0`.

**Data Types:** `bus` | `double`

## Parameters

### **Output format** — Format of ROS 2 time `bus` (default) | `double`

Format of ROS 2 `Time` output, specified as either
`bus` or `double`.

### **Sample time** — Interval between outputs `-1` (default) | numeric scalar

Interval between outputs, specified as a numeric scalar.

For more information, see Specify Sample Time (Simulink).

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Retrieve current ROS 2 time or system time

The Current Time block outputs the current ROS 2 time. ROS 2 time is based
on the system clock of your computer or the `/clock` topic being published on
the ROS 2 network.

If the `use_sim_time` ROS 2 parameter is set to `true`,
the block returns the simulation time published on the `/clock` topic.
Otherwise, the block returns the system time of your machine.

Current time block workflow. Step 1. Node starts. Step 2. Check if the /use\_sim\_time ROS parameter is true. Step 3. If true, subscribe to the /clock topic and wait to receive time. If false, get system time. Step 4. Output the received time as the current time.
