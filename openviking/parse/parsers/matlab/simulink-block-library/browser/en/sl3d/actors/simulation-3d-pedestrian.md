---
type: simulink-block
title: 'Simulation 3D Pedestrian'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Actors'
documentation_page: 'simulation3dpedestrian'
documentation_source_path: 'simulation3dpedestrian.html'
language: en
---

# Simulation 3D Pedestrian

## Ports

### Input

### **Y** — Lateral position of pedestrian scalar

Lateral position of the pedestrian along the *Y*-axis of the
scene.

The *Y* value of the **Initial position [X,
Y, Z]** parameter must match the value of this port at the start of
simulation.

To specify multiple positions at port **Y** along an entire
pedestrian path, first define a time series of *Y* waypoints in
MATLAB®. Then, feed these waypoints to **Y** by using a From Workspace (Simulink) block. To learn how to select and specify waypoints, see the
Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) example.

### **X** — Longitudinal position of pedestrian scalar

Longitudinal position of the pedestrian along the *X*-axis of
the scene.

The *X* value of the **Initial position [X,
Y, Z]** parameter must match the value of this port at the start of
simulation.

To specify multiple positions at port **X** along an entire
pedestrian path, first define a time series of *X* waypoints in
MATLAB. Then, feed these waypoints to **X** by using a From Workspace (Simulink) block. To learn how to select and specify waypoints, see the
Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) example.

### **Yaw** — Yaw orientation angle of pedestrian scalar

Yaw orientation angle of the pedestrian along the *Z*-axis of
the scene.

The yaw value of the **Initial rotation [Roll,
Pitch, Yaw]** parameter must match the value of this port at the start of
simulation.

To specify multiple orientation angles at port **Yaw** along an
entire pedestrian path, first define a time series of yaw waypoints in MATLAB. Then, feed these waypoints to **Yaw** by using a
From Workspace (Simulink) block. To learn how to
select and specify waypoints, see the Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) example.
### Output

### **Location** — Location of pedestrian real-valued 1-by-3 vector

(*X*, *Y*, *Z*) location
of the pedestrian in the scene, returned as a real-valued 1-by-3 vector. This location
is based on the pedestrian origin, which is on the ground, at the geometric center of
the pedestrian.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location and
orientation**.

**Data Types:** `double`

### **Orientation** — Orientation of pedestrian real-valued 1-by-3 vector

Yaw, pitch, and roll orientation angles of the pedestrian about the
*Z*-axis, *Y*-axis, and
*X*-axes of the scene, respectively, returned as a real-valued
1-by-3 vector. This orientation is based on the pedestrian origin, which is on the
ground, at the geometric center of the pedestrian.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location and
orientation**.

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

### **Coordinate system** — Coordinate system for actor transformation `ISO8855` (default) | `Default` | `MATLAB` | `AERO` | `VRML` | `SAE`

*Since R2025a*

Specify the coordinate system that the actor uses for
translation and rotation in the 3D environment.

- `Default` – World coordinate system
- `MATLAB` – MATLAB coordinate system
- `ISO8855` – ISO 8855 standard coordinate system
- `AERO` – SAE coordinate system
- `VRML` – X3D ISO standard coordinate system
- `SAE` – SAE coordinate system

For more details on the different coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `MATLAB`

### **Initial position [X, Y, Z]** — Initial pedestrian position `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial pedestrian position along the *X*-axis,
*Y*-axis, and *Z*-axis of the scene.

Set the *X* and *Y* values of this parameter
to match the **X** and **Y** input port values at
the start of simulation.

### **Initial yaw** — Initial angle of pedestrian rotation `0` (default) | real-valued scalar

Initial yaw angle of pedestrian rotation.

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

### **Output location and orientation** — Output location and orientation of pedestrian `off` (default) | `on`

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

**Introduced in R2024a**

### R2025a: Set coordinate system parameter

Set the **Coordinate system** parameter in
the Simulation 3D Pedestrian block to represent the coordinate system for actor transformation
in the 3D environment.

## Description

Implement pedestrian in 3D environment

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

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.
