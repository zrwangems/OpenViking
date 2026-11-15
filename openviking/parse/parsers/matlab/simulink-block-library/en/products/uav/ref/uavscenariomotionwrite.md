---
type: simulink-block
title: 'UAV Scenario Motion Write'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / UAV Cuboid Scenario Simulation'
documentation_page: 'uavscenariomotionwrite'
documentation_source_path: 'ref/uavscenariomotionwrite.html'
language: en
---

# UAV Scenario Motion Write

## Ports

### Input

### **Position** — Position 1-by-3 vector

Specify input position of platform in input coordinate frame as a 1-by-3
vector.

### **Orientation** — Orientation quaternion 1-by-4 vector

Specify input orientation of platform in input coordinate frame as a 1-by-4 vector
quaternion.

### **Velocity** — Velocity 1-by-3 vector

Specify input velocity of platform in input coordinate frame as a 1-by-3
vector.

### **Acceleration** — Acceleration 1-by-3 vector

Specify input acceleration of platform in input coordinate frame as a 1-by-3
vector.

### **AngularVelocity** — Angular Velocity 1-by-3 vector

Specify input angular velocity of platform in input coordinate frame, specified as
a 1-by-3 vector.

## Parameters

### **Platform name** — Platform name `'UAV'` (default) | string

Use **Select** to choose a platform name string from the UAV
Scenario.

### **Coordinate frame of input motion** — Coordinate frame of input motion `'NED'` (default) | `ENU`

Specify coordinate frame of input motion as
`'NED'`(North-East-Down) or
`'ENU'`(East-North-Up).

## Libraries

UAV Toolbox / UAV Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Update platform motion in UAV scenario simulation

Use this block to update the motion state of a platform in a UAV scenario simulation with
input signals at each time step. The block takes the position, orientation, velocity,
acceleration, and angular velocity as inputs to update the motion state bus of the specified
platform. However, this block does not move the platform based on velocity and acceleration
inputs as there is no kinematic model being simulated in the UAV Scenario.

To use this block, ensure that UAV Scenario
Configuration block is in your model.

This block uses the sample time specified in the UAV Scenario Configuration
block.
