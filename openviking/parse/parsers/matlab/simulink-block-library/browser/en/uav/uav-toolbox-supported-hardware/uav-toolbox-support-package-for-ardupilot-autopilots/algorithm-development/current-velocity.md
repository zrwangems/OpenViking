---
type: simulink-block
title: 'Current Velocity'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'currentvelocity'
documentation_source_path: 'ardupilot/ref/currentvelocity.html'
language: en
---

# Current Velocity

## Ports

### Output

### **Port\_1** — Current velocity vector

Vehicle's current velocity in microseconds in the NED (North-East-Down)
frame.

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

Reads current velocity

The Current Velocity block outputs the vehicle's current velocity (in
m/s) in the NED (North-East-Down) frame, which is a geographic coordinate system used in
navigation.

- North (N): Positive direction points towards the North (geographical
  north).
- East (E): Positive direction points towards the East (perpendicular to North,
  in the horizontal plane).
- Down (D): Positive direction points downward, towards the Earth's center
  (vertical component).
