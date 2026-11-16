---
type: simulink-block
title: 'Current Attitude'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'currentattitude'
documentation_source_path: 'ardupilot/ref/currentattitude.html'
language: en
---

# Current Attitude

## Ports

### Output

### **Port\_1** — Current attitude vector

Current attitude of the vehicle (roll, pitch, and yaw angles) as determined
by ArduPilot's Attitude Heading Reference System (AHRS).

**Data Types:** `single`

## Parameters

### **Output as** — Output format for the current attitude `Euler(ZYX)` (default) | `Quaternion(ZYX)`

Select the output format for the current attitude. This parameter allows you to
choose between representing the current attitude as Euler angles or as a Quaternion.

- `Euler (ZYX)`: Select this option to output
  the current attitude in Euler angles format, using the ZYX convention,
  which represents the rotation in roll, pitch, and yaw angles.
- `Quaternion (WXYZ)`: Select this option to
  output the current attitude in quaternion format, which consists of a
  four-part hyper-complex number (W, X, Y, Z).

### **Sample time** — Time interval to read data `-1` (default)

The time interval at which the block reads values from the ArduPilot
Autopilot.

## Libraries

UAV Toolbox Support Package for ArduPilot Autopilots / Controller Interface Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025b**

## Description

Reads current attitude

The Current Attitude block outputs the current attitude of the vehicle
(roll, pitch, and yaw angles) as determined by ArduPilot's Attitude Heading Reference
System (AHRS).
