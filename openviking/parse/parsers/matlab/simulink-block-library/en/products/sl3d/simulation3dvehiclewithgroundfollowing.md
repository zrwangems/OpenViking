---
type: simulink-block
title: 'Simulation 3D Vehicle with Ground Following'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Actors'
documentation_page: 'simulation3dvehiclewithgroundfollowing'
documentation_source_path: 'simulation3dvehiclewithgroundfollowing.html'
language: en
---

# Simulation 3D Vehicle with Ground Following

## Ports

### Input

### **X** — Longitudinal position of vehicle scalar

Longitudinal position of the vehicle along the *X*-axis of the
scene.

The *X* value of the **Initial position [X, Y, Z]** parameter must match the
value of this port at the start of simulation.

### **Y** — Lateral position of vehicle scalar

Lateral position of the vehicle along the *Y*-axis of the
scene.

The *Y* value of the **Initial position [X, Y, Z]** parameter must match the
value of this port at the start of simulation.

### **Yaw** — Yaw orientation angle of vehicle scalar

Yaw orientation angle of the vehicle along the *Z*-axis of the
scene.
.

The yaw value of the **Initial rotation [Roll, Pitch, Yaw]** parameter must match the value of
this port at the start of simulation.

### **Light controls** — Vehicle light controls 1-by-6 vector

Light controls input signal, specified as a 1-by-6 Boolean vector. Each element of the
vector turns a specific vehicle light on or off, as indicated in this table. A value of
1 turns the light on; a value of 0 turns the light off.

| Vector Element | Vehicle Light |
| --- | --- |
| (1,1) | Headlight high beam |
| (1,2) | Headlight low beam |
| (1,3) | Brake |
| (1,4) | Reverse |
| (1,5) | Left signal |
| (1,6) | Right signal |

#### Dependencies

To create this port, on the **Light Controls** tab, select
**Enable light controls**.

**Data Types:** `Boolean`
### Output

### **Location** — Location of vehicle real-valued 1-by-3 vector

(*X*, *Y*, *Z*) location
of the vehicle in the scene, returned as a real-valued 1-by-3 vector. This location is
based on the vehicle origin, which is on the ground, at the geometric center of the
vehicle.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location and
orientation**.

**Data Types:** `double`

### **Orientation** — Orientation of vehicle real-valued 1-by-3 vector

Yaw, pitch, and roll orientation angles of the vehicle about the
*Z*-axis, *Y*-axis, and
*X*-axes of the scene, respectively, returned as a real-valued
1-by-3 vector. This orientation is based on the vehicle origin, which is on the
ground, at the geometric center of the vehicle.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location and
orientation**.

**Data Types:** `double`

## Parameters

### Vehicle Parameters

### **Type** — Type of vehicle `Muscle car` (default) | `Sedan` | `Sport utility vehicle` | `Small pickup truck` | `Hatchback` | `Box truck` | `Custom`

Select the type of vehicle. To obtain the dimensions of each vehicle type, see these reference pages:

- `Muscle car` — Muscle Car (Automated Driving Toolbox)
- `Sedan` — Sedan (Automated Driving Toolbox)
- `Sport utility vehicle` — Sport Utility Vehicle (Automated Driving Toolbox)
- `Small pickup truck` — Small Pickup Truck (Automated Driving Toolbox)
- `Hatchback` — Hatchback (Automated Driving Toolbox)
- `Box truck` —Box Truck (Automated Driving Toolbox)

#### Dependencies

Selecting `Custom` enables parameters that allow you to import a
custom mesh for your vehicle.

### **Path to custom mesh** — Path to custom mesh `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_MuscleCar.SK_MuscleCar` (default) | valid path

Path to custom mesh.

To create a custom vehicle mesh, see Prepare Custom Vehicle Mesh for the Unreal Editor (Automated Driving Toolbox).

**Example:** `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_Sedan.SK_Sedan`

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Track width in custom mesh (m)** — Track width `1.9` (default) | scalar

Track width in custom mesh, in m.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Wheel base in custom mesh (m)** — Wheel base `3` (default) | scalar

Wheel base in custom mesh, in m.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Wheel radius in custom mesh (m)** — Wheel radius `0.35` (default) | scalar

Wheel radius in custom mesh, in m.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Color** — Color of vehicle `Red` (default) | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver`

Select the color of the vehicle.

### **Coordinate system** — Coordinate system for actor transformation `ISO8855` (default) | `Default` | `MATLAB` | `AERO` | `VRML` | `SAE`

*Since R2025a*

Specify the coordinate system that the actor uses for
translation and rotation in the 3D environment.

- `Default` – World coordinate system
- `MATLAB` – MATLAB® coordinate system
- `ISO8855` – ISO 8855 standard coordinate system
- `AERO` – SAE coordinate system
- `VRML` – X3D ISO standard coordinate system
- `SAE` – SAE coordinate system

For more details on the different coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `MATLAB`

### **Initial position [X, Y, Z]** — Initial vehicle position `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial vehicle position along the *X*-axis,
*Y*-axis, and *Z*-axis of the scene.

Set the *X* and *Y* values of this parameter
to match the **X** and **Y** input port values at
the start of simulation.

### **Initial rotation [Roll, Pitch, Yaw]** — Initial angle of vehicle rotation `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial angle of vehicle rotation. The angle of rotation is defined by the roll,
pitch, and yaw of the vehicle.

Set the yaw value of this parameter to match the **Yaw** input
port value at the start of simulation.

### **Name** — Name of vehicle `SimulinkVehicle1` (default) | vehicle name

Name of vehicle. By default, when you use the block in your model, the block sets
the **Name** parameter to
`SimulinkVehicleX`. The value of
`X` depends on the number of
Simulation 3D Vehicle with Ground Following blocks that you have in
your model.

The vehicle name appears as a selection in the **Parent name**
parameter of any Automated Driving Toolbox™ Simulation 3D sensor blocks within the same model as the vehicle. With
the **Parent name** parameter, you can select the vehicle on which to
mount the sensor.

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time, *Ts*, in seconds. The
graphics frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block uses the sample
time specified in the Simulation 3D Scene Configuration block.

### Light Controls

### **Enable light controls** — Control vehicle lights `off` (default) | `on`

Select whether to control the vehicle headlights. Use the enabled parameters to
set the light parameters, including headlight intensity.

#### Dependencies

Selecting this parameter:

- Creates the input port `Light controls`
- Enables these light parameters.

  | Lights | Light Parameters |
  | --- | --- |
  | **Headlights** | - **Headlight color** - **High beam intensity** - **Low beam intensity** - **High beam cone half angle** - **Low beam cone half angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **Brake lights** | **Brake light intensity** |
  | **Reverse lights** | **Reverse light intensity** |
  | **Turn signal lights** | - **Turn signal light intensity** - **Period** - **Pulse width** |

#### Headlights

### **Headlight color [R,G,B]** — Headlight color `[1,1,1]` (default) | 1-by-3 array of RGB triplet values

Headlight color, specified as a normalized 1-by-3 array of RGB triplet
values.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `int8` | `uint8`

### **High beam intensity (cd)** — High beam intensity `100000` (default) | positive scalar

High beam intensity, in cd.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Low beam intensity (cd)** — Low beam intensity `60000` (default) | positive scalar

Low beam intensity, in cd.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **High beam cone half angle (deg)** — High beam cone half angle `70` (default) | positive scalar less than or equal to 90

High beam cone half angle, in deg.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Low beam cone half angle (deg)** — Low beam cone half angle `70` (default) | positive scalar less than or equal to 90

Low beam cone half angle, in deg.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Left headlight beam orientation [Pitch, Yaw] (deg)** — Left headlight beam orientation [Pitch, Yaw] (deg) `[0,0]` (default) | 1-by-2 array with values between -180 and 180

Pitch and yaw orientation of the left headlight beam orientation in the
*Z*-up coordinate system, specified as a 1-by-2 array, in deg.
The first element of the array, `[1,1]`, is the pitch angle. The
second element of the array, `[1,2]` is the yaw angle.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Right headlight beam orientation [Pitch, Yaw] (deg)** — Right headlight beam orientation `[0,0]` (default) | 1-by-2 array with values between -180 and 180

Pitch and yaw orientation of the right headlight beam orientation in the
*Z*-up coordinate system, specified as a 1-by-2 array, in deg.
The first element of the array, `[1,1]`, is the pitch angle. The
second element of the array, `[1,2]` is the yaw angle.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

#### Brake Lights

### **Brake light intensity (cd/m^2)** — Intensity `500` (default) | positive scalar

Brake light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

#### Reverse Lights

### **Reverse light intensity (cd/m^2)** — Intensity `500` (default) | positive scalar

Reverse light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

#### Turn Signal Lights

### **Turn signal light intensity (cd/m^2)** — Intensity `500` (default) | positive scalar

Turn signal light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Period (s)** — Turn signal light period `1` (default) | positive scalar

Turn signal light period, in s.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Pulse width (% of period)** — Pulse width `50` (default) | positive scalar less than 100

Turn signal light pulse width, as a percent of the period.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### Ground Truth

### **Output location and orientation** — Output location and orientation of vehicle `off` (default) | `on`

Select this parameter to output the location and orientation of the vehicle at the
**Location** and **Orientation** ports,
respectively.

## Libraries

Automated Driving Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components Simulink 3D Animation / Simulation 3D / Actors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2025a: Set coordinate system parameter

Set the **Coordinate system** parameter in
the Simulation 3D Vehicle with Ground Following block to represent the coordinate system for actor transformation
in the 3D environment.

## Description

Implement vehicle that follows ground in 3D environment

The Simulation 3D Vehicle with Ground Following block implements a vehicle
with four wheels in a 3D simulation environment. This environment is rendered using the
Unreal Engine® from Epic Games®. The block uses the input (*X*, *Y*)
position and yaw angle of the vehicle to adjust the elevation, roll angle, and pitch angle of
the vehicle so that it follows the ground terrain. The block determines the vehicle velocity
and heading and adjusts the steering angle and rotation for each wheel. Use this block for
automated driving applications.

To use this block, ensure that the Simulation 3D Scene Configuration block
is in your model. If you set the **Sample time** parameter of the
Simulation 3D Vehicle with Ground Following block to `-1`,
the block inherits the sample time specified in the Simulation 3D Scene
Configuration block.

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.

**Tip**

The Simulation 3D Vehicle with Ground
Following block must execute before the Simulation 3D Scene
Configuration block. That way, the Simulation 3D Vehicle with Ground
Following block prepares the signal data before the Unreal Engine 3D visualization environment receives it. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Vehicle with Ground Following —
  `-1`

For more information about execution order, see Control and Display Execution Order (Simulink).

You can configure the Simulation 3D Vehicle with Ground Following block to
import custom meshes and control vehicle lights.
