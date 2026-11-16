---
type: simulink-block
title: 'Position Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'positionsetpoint'
documentation_source_path: 'ardupilot/ref/positionsetpoint.html'
language: en
---

# Position Setpoint

## Ports

### Output

### **Port\_1** — Position setpoint vector

Vehicle's desired position (in meters) with respect to the origin in the
NED (North-East-Down) frame

**Data Types:** `single`

## Parameters

### **Sample time** — Interval at which the block reads values `-1` (default)

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

Reads position setpoint

The Position Setpoint block outputs the vehicle's desired position (in
meters) with respect to the origin in the NED (North-East-Down) frame, which is a
coordinate system used in navigation. This is used to describe the position relative to a
reference point, typically the starting location of the vehicle.

- North (N): Positive direction points towards the North (geographical
  north).
- East (E): Positive direction points towards the East (perpendicular to North,
  in the horizontal plane).
- Down (D): Positive direction points downward, towards the Earth's center
  (vertical component).
