---
type: simulink-block
title: 'PX4 Timestamp'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4timestamp'
documentation_source_path: 'px4/ref/px4timestamp.html'
language: en
---

# PX4 Timestamp

## Ports

### Output

### **Timestamp** — Absolute timestamp uint64

Absolute timestamp from the PX4 Autopilot, returned as
`uint64`.

**Data Types:** `uint64`

## Parameters

### **Sample time** — Interval at which the block reads values `0.01` (default) | any non-negative value that is a multiple of 0.01 | -1

Enter the time interval at which the block reads values from the Pixhawk
Autopilot.

When you set this parameter to `-1`, Simulink determines the best sample time for the block based on the block
context within the model.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Output absolute timestamp from the PX4 Autopilot to a Simulink model

The PX4 timestamp block gets the time since start in microseconds from
the PX4 Autopilot into the Simulink® Model. This timestamp information is absolute, ensuring it never wraps or
goes backwards. The output datatype of timestamp is `uint64`.
