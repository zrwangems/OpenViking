---
type: simulink-block
title: 'Simulation 3D Bicyclist'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dbicyclist'
documentation_source_path: 'ref/simulation3dbicyclist.html'
language: en
---

# Simulation 3D Bicyclist

## Ports

### Input

### **Y** — Lateral position of bicyclist scalar

Lateral position of the bicyclist along the *Y*-axis of the
scene. **Y** is in the inertial
*Z*-up coordinate system. Units are in meters.

The *Y* value of the **Initial
position [X, Y, Z] (m)** parameter must match the value of this port at the start of
simulation.

To specify multiple positions at port **Y** along an entire
bicyclist path, first define a time series of *Y* waypoints in
MATLAB®. Then, feed these waypoints to **Y** by using a From Workspace (Simulink) block. To learn how to select and specify waypoints, see the
Select Waypoints for Unreal Engine Simulation example.

### **X** — Longitudinal position of bicyclist scalar

Longitudinal position of the bicyclist along the *X*-axis of
the scene. **X** is in the inertial
*Z*-up coordinate system. Units are in meters.

The *X* value of the **Initial
position [X, Y, Z] (m)** parameter must match the value of this port at the start of
simulation.

To specify multiple positions at port **X** along an entire
bicyclist path, first define a time series of *X* waypoints in
MATLAB. Then, feed these waypoints to **X** by using a From Workspace (Simulink) block. To learn how to select and specify waypoints, see the
Select Waypoints for Unreal Engine Simulation example.

### **Yaw** — Yaw orientation angle of bicyclist scalar

Yaw orientation angle of the bicyclist along the *Z*-axis of
the scene. **Yaw** is in the
*Z*-up coordinate system.

The yaw value of the **Initial rotation [Roll,
Pitch, Yaw] (deg)** parameter must match the value of this port at the start of
simulation.

To specify multiple orientation angles at port **Yaw** along an
entire bicyclist path, first define a time series of yaw waypoints in MATLAB. Then, feed these waypoints to **Yaw** by using a
From Workspace (Simulink) block. To learn how to
select and specify waypoints, see the Select Waypoints for Unreal Engine Simulation example.
### Output

### **Location** — Location of bicyclist real-valued 1-by-3 vector

(*X*, *Y*, *Z*) location
of the bicyclist in the scene, returned as a real-valued 1-by-3 vector. This location
is based on the bicyclist origin, which is on the ground, at the geometric center of
the bicyclist. **Location** values are
in the inertial *Z*-up world coordinate system. Units are in
meters.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location (m) and orientation
(rad)**.

**Data Types:** `double`

### **Orientation** — Orientation of bicyclist real-valued 1-by-3 vector

Yaw, pitch, and roll orientation angles of the bicyclist about the
*Z*-axis, *Y*-axis, and
*X*-axes of the scene, respectively, returned as a real-valued
1-by-3 vector. This orientation is based on the bicyclist origin, which is on the
ground, at the geometric center of the bicyclist. **Orientation** values are in the inertial
*Z*-up coordinate system. Units are in radians.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location (m) and orientation
(rad)**.

**Data Types:** `double`

## Parameters

### Bicyclist Parameters

### **Scale** — Scale factor for bicyclist `[1, 1, 1]` (default) | real-valued 1-by-3 vector

Scale factor for the bicyclist along the *X*-axis,
*Y*-axis, and *Z*-axis.

### **Initial position [X, Y, Z] (m)** — Initial bicyclist position `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial bicyclist position along the *X*-axis,
*Y*-axis, and *Z*-axis of the scene. This position is in the inertial *Z*-up
coordinate system. Units are in meters.

Set the *X* and *Y* values of this parameter
to match the **X** and **Y** input port values at
the start of simulation.

### **Initial rotation [Roll, Pitch, Yaw] (deg)** — Initial angle of bicyclist rotation `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial angle of bicyclist rotation. The angle of rotation is defined by the roll,
pitch, and yaw of the bicyclist. Units are in
degrees.

Set the yaw value of this parameter to match the **Yaw** input
port value at the start of simulation.

### **Name** — Name of bicyclist `SimulinkBicyclist1` (default) | bicyclist name

Name of bicyclist. By default, when you use the block in your model, the block
sets the **Name** parameter to
`SimulinkBicyclistX`. The value of
`X` depends on the number of
Simulation 3D Bicyclist blocks that you have in your model.

The bicyclist name appears as a selection in the **Parent name**
parameter of any Simulation 3D sensor blocks within the same model as the bicyclist.
With the **Parent name** parameter, you can select the bicyclist on
which to mount the sensor.

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time, *Ts*, in seconds. The
graphics frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block uses the sample
time specified in the Simulation 3D Scene Configuration block.

### Ground Truth

### **Output location (m) and orientation (rad)** — Output location and orientation of pedestrian `off` (default) | `on`

Select this parameter to output the location and orientation of the pedestrian at
the **Location** and **Orientation** ports,
respectively.

## Libraries

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Actors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Bicyclist block requires
Simulink
3D Animation.

## Description

Implement bicyclist in 3D environment

**Note**

Simulating models with the Simulation 3D Bicyclist block requires
Simulink®
3D Animation™.

The Simulation 3D Bicyclist block implements a bicyclist in a 3D simulation
environment. The block uses the input (*X*, *Y*)
position and yaw angle of the bicyclist to adjust the elevation, roll angle, and pitch angle
so that the bicyclist follows the ground terrain. The block determines the bicyclist velocity
and heading and adjusts the movement to be idle, pedaling, or braking, appropriately.

To use this block, ensure that the Simulation 3D Scene Configuration block
is in your model. If you set the **Sample time** parameter of the
Simulation 3D Pedestrian block to `-1`, the block inherits
the sample time specified in the Simulation 3D Scene Configuration
block.

The
block input uses the bicyclist *Z*-up right-handed (RH) Cartesian
coordinate system defined in SAE J670 [1] and ISO 8855 [2]. The coordinate system is
inertial and initially aligned with the bicyclist-ground contact line between the two wheels:

- The *X*-axis is along the longitudinal axis of the bicyclist and
  points forward.
- The *Y*-axis is along the lateral axis of the bicyclist and
  points to the left.
- The *Z*-axis points upward.

The yaw, pitch, and roll angles of the *Z*-axis,
*Y*-axis, and *X*-axis, respectively, are positive in
the clockwise directions, when looking in the positive directions of these axes. Bicyclists
are placed in the world coordinate system of the scenes. For more details, see Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox.
