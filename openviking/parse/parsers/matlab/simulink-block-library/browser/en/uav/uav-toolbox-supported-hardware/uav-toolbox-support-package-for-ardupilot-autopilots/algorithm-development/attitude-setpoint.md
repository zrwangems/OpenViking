---
type: simulink-block
title: 'Attitude Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'attitudesetpoint'
documentation_source_path: 'ardupilot/ref/attitudesetpoint.html'
language: en
---

# Attitude Setpoint

## Ports

### Output

### **Port\_1** — Attitude setpoint vector

Attitude setpoint for the vehicle from the ArduPilot's position
controller.

**Data Types:** `single`

## Parameters

### **Output as** — Output format for the attitude setpoint `Euler(ZYX)` (default) | `Quaternion(ZYX)`

Select the output format for the attitude setpoint. This parameter allows you
choose whether to represent the attitude as Euler angles or as a quaternion.

- `Euler (ZYX)`: Select this option to output
  the attitude setpoint in Euler angles format, using the ZYX convention,
  which represents the rotation in roll, pitch, and yaw angles.
- `Quaternion (WXYZ)`: Select this option to
  output the attitude in quaternion format, which consists of a four-part
  hyper-complex number (W, X, Y, Z).

### **Sample time** — Interval at which the block reads values `-1` (default)

The time interval at which the block reads values from the ArduPilot
autopilot.

## Libraries

UAV Toolbox Support Package for ArduPilot Autopilots / Controller Interface Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025b**

## Description

Reads attitude setpoint

This block outputs the vehicle’s attitude setpoint as determined by ArduPilot's position
controller.
