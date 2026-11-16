---
type: simulink-block
title: 'Ang Velocity Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'angvelocitysetpoint'
documentation_source_path: 'ardupilot/ref/angvelocitysetpoint.html'
language: en
---

# Ang Velocity Setpoint

## Ports

### Output

### **Port\_1** — Angular velocity setpoint vector

Angular velocity setpoint (rad/s) along the *x-*,
*y-*, and *z-* axes from the
ArduPilot's position controller.

**Data Types:** `single`

## Parameters

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

Reads angular velocity setpoint

The Ang Velocity Setpoint block outputs the values for angular velocity
setpoint (in rad/s) along the *x-*, *y-*, and
*z-* axes as set by ArduPilot's position controller.
