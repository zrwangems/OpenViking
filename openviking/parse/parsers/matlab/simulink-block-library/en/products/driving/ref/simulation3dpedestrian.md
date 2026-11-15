---
type: simulink-block
title: 'Simulation 3D Pedestrian'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine Scenario Simulation / Scene and Vehicle Configuration (requires Simulink 3D Animation)'
documentation_page: 'simulation3dpedestrian'
documentation_source_path: 'ref/simulation3dpedestrian.html'
language: en
---

# Simulation 3D Pedestrian

## Ports

### Input

### **Y** — Lateral position of pedestrian scalar

Lateral position of the pedestrian along the *Y*-axis of the
scene. **Y** is in the inertial
*Z*-up coordinate system. Units are in meters.

The *Y* value of the **Initial
position [X, Y, Z] (m)** parameter must match the value of this port at the start of
simulation.

To specify multiple positions at port **Y** along an entire
pedestrian path, first define a time series of *Y* waypoints in
MATLAB®. Then, feed these waypoints to **Y** by using a From Workspace (Simulink) block. To learn how to select and specify waypoints, see the
Select Waypoints for Unreal Engine Simulation example.

### **X** — Longitudinal position of pedestrian scalar

Longitudinal position of the pedestrian along the *X*-axis of
the scene. **X** is in the inertial
*Z*-up coordinate system. Units are in meters.

The *X* value of the **Initial
position [X, Y, Z] (m)** parameter must match the value of this port at the start of
simulation.

To specify multiple positions at port **X** along an entire
pedestrian path, first define a time series of *X* waypoints in
MATLAB. Then, feed these waypoints to **X** by using a From Workspace (Simulink) block. To learn how to select and specify waypoints, see the
Select Waypoints for Unreal Engine Simulation example.

### **Yaw** — Yaw orientation angle of pedestrian scalar

Yaw orientation angle of the pedestrian along the *Z*-axis of
the scene. **Yaw** is in the inertial
*Z*-up coordinate system.

The yaw value of the **Initial rotation [Roll,
Pitch, Yaw] (deg)** parameter must match the value of this port at the start of
simulation.

To specify multiple orientation angles at port **Yaw** along an
entire pedestrian path, first define a time series of yaw waypoints in MATLAB. Then, feed these waypoints to **Yaw** by using a
From Workspace (Simulink) block. To learn how to
select and specify waypoints, see the Select Waypoints for Unreal Engine Simulation example.
### Output

### **Location** — Location of pedestrian real-valued 1-by-3 vector

(*X*, *Y*, *Z*) location
of the pedestrian in the scene, returned as a real-valued 1-by-3 vector. This location
is based on the pedestrian origin, which is on the ground, at the geometric center of
the pedestrian. **Location** values
are in the inertial *Z*-up world coordinate system. Units are in
meters.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location (m) and orientation
(rad)**.

**Data Types:** `double`

### **Orientation** — Orientation of pedestrian real-valued 1-by-3 vector

Yaw, pitch, and roll orientation angles of the pedestrian about the
*Z*-axis, *Y*-axis, and
*X*-axes of the scene, respectively, returned as a real-valued
1-by-3 vector. This orientation is based on the pedestrian origin, which is on the
ground, at the geometric center of the pedestrian. **Orientation** values are in the inertial
*Z*-up coordinate system. Units are in radians.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location (m) and orientation
(rad)**.

**Data Types:** `double`

## Parameters

### Pedestrian Parameters

### **Type** — Type of pedestrian `Male 1` (default) | `Male 2` | `Male 3` | `Female 1` | `Female 2` | `Female 3` | `Child`

Type of pedestrian, specified as one of the following options:

- `Male 1`
- `Male 2`
- `Male 3`
- `Female 1`
- `Female 2`
- `Female 3`
- `Child`

### **Scale** — Scale factor for pedestrian `[1, 1, 1]` (default) | real-valued 1-by-3 vector

Scale factor for the pedestrian along the *X*-axis,
*Y*-axis, and *Z*-axis.

### **Initial position [X, Y, Z] (m)** — Initial pedestrian position `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial pedestrian position along the *X*-axis,
*Y*-axis, and *Z*-axis of the scene. This position is in the inertial *Z*-up
coordinate system. Units are in meters.

Set the *X* and *Y* values of this parameter
to match the **X** and **Y** input port values at
the start of simulation.

### **Initial yaw (deg)** — Initial angle of pedestrian rotation `0` (default) | real-valued scalar

Initial yaw angle of pedestrian rotation. Units are
in degrees.

Set the yaw value of this parameter to match the **Yaw** input
port value at the start of simulation.

### **Name** — Name of pedestrian `SimulinkPedestrian1` (default) | pedestrian name

Name of pedestrian. By default, when you use the block in your model, the block
sets the **Name** parameter to
`SimulinkPedestrianX`. The value of
`X` depends on the number of
Simulation 3D Pedestrian blocks that you have in your model.

The pedestrian name appears as a selection in the **Parent name**
parameter of any Simulation 3D sensor blocks within the same model as the pedestrian.
With the **Parent name** parameter, you can select the pedestrian on
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

Simulating models with the Simulation 3D Pedestrian block requires
Simulink
3D Animation.

## Description

Implement pedestrian in 3D environment

**Note**

Simulating models with the Simulation 3D Pedestrian block requires
Simulink®
3D Animation™.

The Simulation 3D Pedestrian block implements a pedestrian in a 3D
simulation environment. The block uses the input (*X*,
*Y*) position and yaw angle of the pedestrian to adjust the elevation,
roll angle, and pitch angle so that the pedestrian follows the ground terrain. The block
determines the pedestrian velocity and heading and adjusts the movement to be idle, walk, or
run, appropriately.

To use this block, ensure that the Simulation 3D Scene Configuration block
is in your model. If you set the **Sample time** parameter of the
Simulation 3D Pedestrian block to `-1`, the block inherits
the sample time specified in the Simulation 3D Scene Configuration
block.

The
block input uses the pedestrian *Z*-up right-handed (RH) Cartesian
coordinate system defined in SAE J670 [1] and ISO 8855 [2]. The coordinate system is
inertial and initially aligned with the pedestrian feet:

- The *X*-axis is along the longitudinal axis of the pedestrian and
  points forward.
- The *Y*-axis is along the lateral axis of the pedestrian and
  points to the left.
- The *Z*-axis points upward.

The yaw, pitch, and roll angles of the *Z*-axis,
*Y*-axis, and *X*-axis, respectively, are positive in
the clockwise directions, when looking in the positive directions of these axes. Pedestrians
are placed in the world coordinate system of the scenes. For more details, see Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox.
