---
type: simulink-block
title: 'Simulation 3D UAV Vehicle'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine 3-D Simulation'
documentation_page: 'simulation3duavvehicle'
documentation_source_path: 'ref/simulation3duavvehicle.html'
language: en
---

# Simulation 3D UAV Vehicle

## Ports

### Input

### **Translation** — Translated position of UAV vector

Translated position of the UAV, specified as a 1-by-3 vector

If **Use geospatial coordinates for inputs and initial
values** parameter is disabled, specify the input as the *X*-, *Y*-, and *Z*-positions of the UAV in the Unreal Engine world
coordinate frame. Units are in meter.

If **Use geospatial coordinates for inputs and initial
values** is enabled,specify the input as the latitude, longitude, and
altitude of the UAV in meter. The block places the UAV in Unreal Engine by evaluating
the translation relative to the `GeoOrigin` that you specified.

For more information on the coordinate systems, see Coordinate Systems for Unreal Engine Simulation in UAV Toolbox.

**Data Types:** `double`

### **Rotation** — Rotation of UAV vector | matrix

Rotation of the UAV, specified as a 1-by-3 vector or a 17-by-3 matrix. You can
specify this input as a 1-by-3 vector for any value of the **Type**
parameter, but if Type is `Custom`, you can alternatively specify
Rotation as a 17-by-3 matrix.

- 1-by-3 vector

  Contains the yaw, pitch, and roll angles of the UAV body, in radians. The UAV
  rotors rotate at a fixed angular velocity of 250 RPM (1500 deg/sec).
- 17-by-3 matrix

  This table summarizes the rows of the rotation matrix.

  - Each angular velocity row contains the angular velocities around the X-,
    Y-, and Z- axes of the corresponding `UAV_RotorN` mesh that
    you set up when exporting the mesh to Unreal Engine. Units are in
    revolutions per minute (RPM).
  - Each rotation angles row contains the yaw, pitch, and roll angles of the
    corresponding UAV mesh part, in radians.

  | Matrix Row | UAV Mesh Part |
  | --- | --- |
  | 1 | `UAV_Body` rotation angles |
  | 2 | `UAV_Motor1` rotation angles |
  | 3 | `UAV_Rotor1` angular velocities |
  | 4 | `UAV_Motor2` rotation angles |
  | 5 | `UAV_Rotor2` angular velocities |
  | 6 | `UAV_Motor3` rotation angles |
  | 7 | `UAV_Rotor3` angular velocities |
  | 8 | `UAV_Motor4` rotation angles |
  | 9 | `UAV_Rotor4` angular velocities |
  | 10 | `UAV_Motor5` rotation angles |
  | 11 | `UAV_Rotor5` angular velocities |
  | 12 | `UAV_Motor6` rotation angles |
  | 13 | `UAV_Rotor6` angular velocities |
  | 14 | `UAV_Motor7` rotation angles |
  | 15 | `UAV_Rotor7` angular velocities |
  | 16 | `UAV_Motor8` rotation angles |
  | 17 | `UAV_Rotor8` angular velocities |

If you clear the **Use geospatial coordinates for inputs and
initial values** parameter, the UAV body rotation angles are relative to
the Unreal Engine world coordinate frame.

If you select the **Use geospatial coordinates for inputs and
initial values** parameter, the UAV body rotation angles are relative to
the local ENU frame at the current position of the UAV.

For more information on the coordinate systems, see Coordinate Systems for Unreal Engine Simulation in UAV Toolbox.

**Data Types:** `double`

### **GeoOrigin** — Geospatial coordinates of Unreal Engine world origin vector

Geospatial coordinates of the Unreal Engine world origin, specified in the form [*latitude*
*longitude*
*altitude*]. *latitude* and
*longitude* are in degrees, and *altitude* is in
meters.

#### Dependencies

To enable this port, select the **Use geospatial coordinates for inputs
and initial values** parameter.

**Data Types:** `double`

## Parameters

### Vehicle Parameters

### **Type** — Type of vehicle `Quadcopter` (default) | `Fixed wing` | `Custom`

Select the type of vehicle. To obtain the dimensions of each vehicle type, see
these reference pages:

- `Quadcopter` — Quadrotor
- `Fixed wing` — Fixed Wing
  Aircraft
- `Custom` — Custom UAV. For more details
  on custom UAV mesh, visit Prepare Custom UAV Vehicle Mesh for the Unreal Editor

### **Path to custom mesh** — Reference path to the custom UAV mesh asset `/MathWorksUAVContent/UAVs/HexaRotorUAV/HexaRotor.HexaRotor` (default) | valid asset reference path

Reference path to the custom UAV mesh asset.

For en example on how to obtain this path from Unreal® editor, visit Visualize VTOL UAV Mission Over Urban Environment.

#### Dependencies

To enable this parameter, set the **Type** parameter to
`Custom`.

### **Color** — Color of vehicle `Black` (default) | `Orange` | `Yellow` | `Green` | `Blue` | `Red` | `White` | `Silver`

Select the color of the vehicle.

#### Dependencies

To enable this parameter, set the **Type** parameter to
`Quadcopter` or `Fixed
wing`.

### **Name** — Name of vehicle `SimulinkVehicle1` (default) | vehicle name

Name of vehicle. By default, when you use the block in your model, the block sets
the **Name** parameter to
`SimulinkVehicleX`. The value of
`X` depends on the number of
Simulation 3D UAV Vehicle blocks that you have in your model.

The vehicle name appears as a selection in the **Parent name**
parameter of any UAV Toolbox Simulation 3D sensor blocks within the same model as the vehicle. With
the **Parent name** parameter, you can select the vehicle on which to
mount the sensor.

### **Use geospatial coordinates for inputs and initial values** — Use geospatial coordinates for port inputs and initial values `off` (default) | `on`

Select this parameter to use geospatial coordinates for port inputs and initial
values in the form.

### Initial Values

### **Initial Translation (m)** — Initial vehicle position `[0 0 0]` (default) | vector

Specify the initial position of your vehicle in one of these forms:

- [*X*
  *Y*
  *Z*] when you clear the **Use geospatial coordinates
  for inputs and initial values** parameter. *X*,
  *Y*, and *Z* are the translation along the
  *X*-axis, *Y*-axis, and
  *Z*-axis, respectively, in the inertial
  *Z*-down coordinate system, in meters.
- [*latitude*
  *longitude*
  *altitude*] when you enable the **Use geospatial
  coordinates for inputs and initial values** parameter. You must
  specify *latitude* and *longitude* in degrees,
  and *altitude* in meters.

### **Initial Georeference Origin (LLA)** — Initial georeference origin `[0 0 0]` (default) | vector

Specify the initial georeference origin in the form [*latitude*
*longitude*
*altitude*], You must specify *latitude* and
*longitude* in degrees, and *altitude* in
meters.

#### Dependencies

To enable this parameter, select the **Use geospatial coordinates for
inputs and initial values** parameter.

### **Initial Rotation (rad)** — Initial angles of vehicle rotation `[0 0 0]` (default) | vector | matrix

Initial rotation of the UAV. The dimensions of this parameter depend on the value
of the**Type** parameter. You can specify this parameter as a 1-by-3
vector for any value of the **Type** parameter, but if Type is
`Custom`, you can alternatively specify this parameter as a 17-by-3
matrix.

Refer to **Rotation** input for more details on how to specify this
value.

### Sample Time

### **Sample time** — Sample time `-1` (default) | scalar

Sample time, *Ts*, specified as a positive
scalar in seconds. The graphics frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block uses the sample
time specified in the Simulation 3D Scene Configuration block.

## Libraries

UAV Toolbox / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

### R2025a: Rotation input for custom UAV Type

The Simulation 3D UAV Vehicle block now accepts a 17-by-3 matrix for the rotation input when you set
the **Type** parameter to `Custom`.

The first row specifies the rotation angles of the UAV body. After that, each even row
specifies the rotation angles for UAV motors 1 through 8, while each odd row specifies the
angular velocities for the corresponding rotor.

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D UAV Vehicle block requires
Simulink
3D Animation.

### R2023a: Support for specifying geospatial coordinates

You can select the **Use geospatial coordinates for inputs and initial
values** parameter to specify inputs and initial values using geospatial
coordinates.

## Description

Place UAV vehicle in 3D visualization

**Note**

Simulating models with the Simulation 3D UAV Vehicle block requires
Simulink®
3D Animation™.

The Simulation 3D UAV Vehicle block implements an unmanned aerial vehicle
(UAV) in a 3D simulation environment. This environment is rendered using the Unreal Engine® from Epic Games®. The block uses the input (*X*, *Y*,
*Z*) position and input (*roll*,
*pitch*, *yaw*) attitude of the UAV in the simulation.

To use this block, ensure that the Simulation 3D Scene Configuration block
is in your model. If you set the **Sample time** parameter of the
Simulation 3D UAV Vehicle block to `-1`, the block inherits
the sample time specified in the Simulation 3D Scene Configuration
block.

**Tip**

The Simulation 3D UAV Vehicle block must
execute before the Simulation 3D Scene Configuration block. That way, the
Simulation 3D UAV Vehicle block prepares the signal data before the
Unreal Engine 3D visualization environment receives it. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Vehicle — `-1`

For more information about execution order, see Block Execution Order.
