---
type: simulink-block
title: 'Simulation 3D Bicyclist'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Actors'
documentation_page: 'simulation3dbicyclist'
documentation_source_path: 'simulation3dbicyclist.html'
language: en
---

# Simulation 3D Bicyclist

## Ports
```yaml
ports:
- name: Y
  summary: Lateral position of bicyclist scalar
  direction: input
- name: X
  summary: Longitudinal position of bicyclist scalar
  direction: input
- name: Yaw
  summary: Yaw orientation angle of bicyclist scalar
  direction: input
- name: Location
  summary: Location of bicyclist real-valued 1-by-3 vector
  direction: output
  data_types: double
- name: Orientation
  summary: Orientation of bicyclist real-valued 1-by-3 vector
  direction: output
  data_types: double
```

### Input

### **Y** — Lateral position of bicyclist scalar

Lateral position of the bicyclist along the *Y*-axis of the
scene.

The *Y* value of the **Initial position [X,
Y, Z]** parameter must match the value of this port at the start of
simulation.

To specify multiple positions at port **Y** along an entire
bicyclist path, first define a time series of *Y* waypoints in
MATLAB®. Then, feed these waypoints to **Y** by using a From Workspace (Simulink) block. To learn how to select and specify waypoints, see the
Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) example.

### **X** — Longitudinal position of bicyclist scalar

Longitudinal position of the bicyclist along the *X*-axis of
the scene.

The *X* value of the **Initial position [X,
Y, Z]** parameter must match the value of this port at the start of
simulation.

To specify multiple positions at port **X** along an entire
bicyclist path, first define a time series of *X* waypoints in
MATLAB. Then, feed these waypoints to **X** by using a From Workspace (Simulink) block. To learn how to select and specify waypoints, see the
Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) example.

### **Yaw** — Yaw orientation angle of bicyclist scalar

Yaw orientation angle of the bicyclist along the *Z*-axis of
the scene.

The yaw value of the **Initial rotation [Roll,
Pitch, Yaw]** parameter must match the value of this port at the start of
simulation.

To specify multiple orientation angles at port **Yaw** along an
entire bicyclist path, first define a time series of yaw waypoints in MATLAB. Then, feed these waypoints to **Yaw** by using a
From Workspace (Simulink) block. To learn how to
select and specify waypoints, see the Select Waypoints for Unreal Engine Simulation (Automated Driving Toolbox) example.
### Output

### **Location** — Location of bicyclist real-valued 1-by-3 vector

(*X*, *Y*, *Z*) location
of the bicyclist in the scene, returned as a real-valued 1-by-3 vector. This location
is based on the bicyclist origin, which is on the ground, at the geometric center of
the bicyclist.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location and
orientation**.

**Data Types:** `double`

### **Orientation** — Orientation of bicyclist real-valued 1-by-3 vector

Yaw, pitch, and roll orientation angles of the bicyclist about the
*Z*-axis, *Y*-axis, and
*X*-axes of the scene, respectively, returned as a real-valued
1-by-3 vector. This orientation is based on the bicyclist origin, which is on the
ground, at the geometric center of the bicyclist.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location and
orientation**.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Scale
  summary: Scale factor for bicyclist [1, 1, 1] (default) | real-valued 1-by-3 vector
  group: Bicyclist Parameters
- name: Coordinate system
  summary: Coordinate system for actor transformation ISO8855 (default) | Default | MATLAB | AERO | VRML | SAE
  group: Bicyclist Parameters
- name: Initial position [X, Y, Z]
  summary: Initial bicyclist position [0, 0, 0] (default) | real-valued 1-by-3 vector
  group: Bicyclist Parameters
- name: Initial rotation [Roll, Pitch, Yaw]
  summary: Initial angle of bicyclist rotation [0, 0, 0] (default) | real-valued 1-by-3 vector
  group: Bicyclist Parameters
- name: Name
  summary: Name of bicyclist SimulinkBicyclist1 (default) | bicyclist name
  group: Bicyclist Parameters
- name: Sample time
  summary: Sample time -1 (default) | positive scalar
  group: Bicyclist Parameters
- name: Output location and orientation
  summary: Output location and orientation of pedestrian off (default) | on
  group: Ground Truth
```

### Bicyclist Parameters

### **Scale** — Scale factor for bicyclist `[1, 1, 1]` (default) | real-valued 1-by-3 vector

Scale factor for the bicyclist along the *X*-axis,
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

### **Initial position [X, Y, Z]** — Initial bicyclist position `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial bicyclist position along the *X*-axis,
*Y*-axis, and *Z*-axis of the scene.

Set the *X* and *Y* values of this parameter
to match the **X** and **Y** input port values at
the start of simulation.

### **Initial rotation [Roll, Pitch, Yaw]** — Initial angle of bicyclist rotation `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial angle of bicyclist rotation. The angle of rotation is defined by the roll,
pitch, and yaw of the bicyclist.

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
the Simulation 3D Bicyclist block to represent the coordinate system for actor transformation
in the 3D environment.

## Description

Implement bicyclist in 3D environment

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

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.
