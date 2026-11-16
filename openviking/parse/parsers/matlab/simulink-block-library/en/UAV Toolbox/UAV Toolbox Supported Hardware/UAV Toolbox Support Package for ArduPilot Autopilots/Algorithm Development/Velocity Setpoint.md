---
type: simulink-block
title: 'Velocity Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'velocitysetpoint'
documentation_source_path: 'ardupilot/ref/velocitysetpoint.html'
language: en
---

# Velocity Setpoint

## Ports

### Output

### **Port\_1** — Velocity setpoint vector

Vehicle Velocity setpoint (m/s) in the NED frame from ArduPilot’s guidance
system.

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

Reads velocity setpoint

The Velocity Setpoint block reads the velocity setpoints (m/s) of the vehicle in the
North-East-Down (NED) frame as set by ArduPilot’s guidance system based on the current
flight mode.

- North (N): Positive direction points towards the North (geographical
  north).
- East (E): Positive direction points towards the East (perpendicular to North,
  in the horizontal plane).
- Down (D): Positive direction points downward, towards the Earth's center
  (vertical component).
