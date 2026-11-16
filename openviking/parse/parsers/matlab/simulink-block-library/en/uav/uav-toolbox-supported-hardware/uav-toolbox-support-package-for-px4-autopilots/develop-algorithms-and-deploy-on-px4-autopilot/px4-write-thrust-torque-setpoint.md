---
type: simulink-block
title: 'PX4 Write Thrust & Torque Setpoint'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4writethrusttorquesetpoint'
documentation_source_path: 'px4/ref/px4writethrusttorquesetpoint.html'
language: en
---

# PX4 Write Thrust & Torque Setpoint

## Ports

### Input

### **Thrust** — Thrust setpoint vector

Specify the desired thrust setpoint along *x-*,
*y-*, and *z-*axes of the vehicle
body. The specified inputs are normalized to the range
`[-1,1]` in the vehicle body FRD frame.

**Data Types:** `single`

### **Torque** — Torque setpoint vector

Specify the desired torque setpoint about the *x-*,
*y-*, and *z-*axes of the vehicle
body. The specified inputs are normalized to the range
`[-1,1]` in the vehicle body FRD frame.

**Data Types:** `single`

## Parameters

Not documented in R2025b.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Publish the thrust and torque setpoints to uORB topics

The block writes motor and servo actuator values by directly publishing thrust and
torque setpoints to the `vehicle_thrust_setpoint` and
`vehicle_torque_setpoint` uORB topics. This block accepts two inputs,
thrust and torque, each as a 1-by-3 vector. The thrust setpoint is along, and the torque
setpoint is about, the *x-*, *y-*, and
*z-* body axes. Both inputs are normalized to the range
`[-1,1]` in the vehicle body FRD frame.
