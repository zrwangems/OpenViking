---
type: simulink-block
title: 'Current Ang Velocity'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'currentangvelocity'
documentation_source_path: 'ardupilot/ref/currentangvelocity.html'
language: en
---

# Current Ang Velocity

## Ports

### Output

### **Port\_1** — Current angular velocity vector

Current Angular velocity along the *-x*,
*-y*, and *-z* axes as measured by the
vehicle's gyroscope.

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

Reads current angular velocity

The Current Ang Velocityblock outputs the angular velocities (in rad/s)
along the *x-*, *y-*, and *z-*
axes as measured by the vehicle's gyroscope.
