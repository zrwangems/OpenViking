---
type: simulink-block
title: 'Simulation 3D Vehicle with Ground Following'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Vehicles (requires Simulink 3D Animation)'
documentation_page: 'simulation3dvehiclewithgroundfollowing'
documentation_source_path: 'ref/simulation3dvehiclewithgroundfollowing.html'
language: en
---

# Simulation 3D Vehicle with Ground Following

## Ports

### Input

### **X** — Longitudinal position of vehicle scalar

Longitudinal position of the vehicle along the *X*-axis of the
scene. **X** is in the
inertial *Z*-downcoordinate system. Units are in
meters.

### **Y** — Lateral position of vehicle scalar

Lateral position of the vehicle along the *Y*-axis of the
scene. **Y** is in the
inertial *Z*-downcoordinate system. Units are in
meters.

### **Yaw** — Yaw orientation angle of vehicle scalar

Yaw orientation angle of the vehicle along the *Z*-axis of the
scene. **Yaw** is in the
inertial *Z*-downcoordinate system.
Units are in radians.

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

## Parameters

### Vehicle Parameters

### **Type** — Type of vehicle `Muscle car` (default) | `Sedan` | `Sport utility vehicle` | `Small pickup truck` | `Hatchback` | `Box truck` | `Formula Student Vehicle` | `Custom`

Select the type of vehicle. To obtain the dimensions of each vehicle type, see these reference pages:

- `Muscle car` — Muscle Car
- `Sedan` — Sedan
- `Sport utility vehicle` — Sport Utility Vehicle
- `Small pickup truck` — Small Pickup Truck
- `Hatchback` — Hatchback
- `Box truck` —
  Box Truck
- `Formula student vehicle` — Formula
  Student Vehicle

#### Dependencies

Selecting `Custom` enables parameters that allow you to import a
custom mesh for your vehicle.

### **Path to custom mesh, MeshPath** — Path to custom mesh `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_MuscleCar.SK_MuscleCar` (default) | valid path

Path to custom mesh.

To create a custom vehicle mesh, see Prepare Custom Vehicle Mesh for the Unreal Editor.

**Example:** `/MathWorksSimulation/Vehicles/Muscle/Meshes/SK_Sedan.SK_Sedan`

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Track width in custom mesh, TrackWidth** — Track width `1.9` (default) | scalar

Track width in custom mesh, in m.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Wheel base in custom mesh, WheelBase** — Wheel base `3` (default) | scalar

Wheel base in custom mesh, in m.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Wheel radius in custom mesh, WheelRadius** — Wheel radius `0.35` (default) | scalar

Wheel radius in custom mesh, in m.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Color** — Color of vehicle `Red` (default) | `Orange` | `Yellow` | `Green` | `Blue` | `Black` | `White` | `Silver`

Select the color of the vehicle.

### **Initial position [X, Y, Z], InitialPos (m)** — Initial vehicle position `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial vehicle position along the *X*-axis,
*Y*-axis, and *Z*-axis in the inertial
*Z*-down coordinate system, in m.

### **Initial rotation [Roll, Pitch, Yaw], InitialRot (rad)** — Initial angle of vehicle rotation `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Initial angle of vehicle rotation, in rad. The angle of rotation is defined by the
roll, pitch, and yaw of the vehicle.

### **Name, ActorName** — Name of vehicle `SimulinkVehicle1` (default) | vehicle name

Name of vehicle. By default, when you use the block in your model, the block sets
the **Name** parameter to
`SimulinkVehicleX`. The value of
`X` depends on the number of
Simulation 3D Vehicle with Ground Following blocks that you have in
your model.

### **Sample time, SampleTime** — Sample time `-1` (default) | positive scalar

Sample time, *Ts*. The graphics frame rate
is the inverse of the sample time.

If you set the sample time to `-1`, the block uses the sample
time specified in the Simulation 3D Scene Configuration block.

### Light Controls

### **Enable light controls** — Option to control vehicle lights `off` (default) | `on`

Select whether to control the vehicle headlights. Use the enabled parameters
to set the light parameters, including headlight intensity.

#### Dependencies

Selecting this parameter:

- Creates the input port `Light
  controls`.
- Enables these light parameters.

  | Lights | Light Parameters |
  | --- | --- |
  | **Headlights** | - **Headlight color** - **High beam   intensity** - **Low beam   intensity** - **High beam cone half   angle** - **Low beam cone half   angle** - **Left headlight beam   orientation** - **Right headlight beam   orientation** |
  | **Brake lights** | **Brake light intensity** |
  | **Reverse lights** | **Reverse light intensity** |
  | **Turn signal lights** | - **Turn signal light   intensity** - **Period** - **Pulse width** |

#### Headlights

### **Headlight color [R,G,B], HeadlightColor** — Headlight color `[1,1,1]` (default) | 1-by-3 vector of RGB triplet values

Headlight color, specified as a normalized 1-by-3 vector of RGB triplet
values.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `int8` | `uint8`

### **High beam intensity, HighBeamIntensity** — High beam intensity `100000` (default) | positive scalar

High beam intensity, in cd.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Low beam intensity, LowBeamIntensity** — Low beam intensity `60000` (default) | positive scalar

Low beam intensity, in cd.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **High beam cone half angle, HighBeamConeAngle** — High beam cone half angle `1.22` (default) | positive scalar less than pi/2

High beam cone half angle, in rad.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Low beam cone half angle, LowBeamConeAngle** — Low beam cone half angle `1.22` (default) | positive scalar less than pi/2

Low beam cone half angle, in rad.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Left headlight beam orientation [Pitch, Yaw], LeftHeadlightOrientation** — Left headlight beam orientation `[0,0]` (default) | 1-by-2 vector with values between -pi and pi

Pitch and yaw orientation of the left headlight beam orientation in the
*Z*-down coordinate system, specified as a 1-by-2 vector,
in rad. The first element of the vector, `[1,1]`, is the pitch
angle. The second element of the vector, `[1,2]`, is the yaw
angle.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Right headlight beam orientation [Pitch, Yaw], RightHeadlightOrientation** — Right headlight beam orientation `[0,0]` (default) | 1-by-2 vector with values between -pi and pi

Pitch and yaw orientation of the right headlight beam orientation in the
*Z*-down coordinate system, specified as a 1-by-2 vector,
in rad. The first element of the vector, `[1,1]`, is the pitch
angle. The second element of the vector, `[1,2]`, is the yaw
angle.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

#### Brake Lights

### **Brake light intensity, BrakelightIntensity** — Brake light intensity `500` (default) | positive scalar

Brake light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

#### Reverse Lights

### **Reverse light intensity, ReverselightIntensity** — Reverse light intensity `500` (default) | positive scalar

Reverse light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

#### Turn Signal Lights

### **Turn signal light intensity, SignallightIntensity** — Turn signal light intensity `500` (default) | positive scalar

Turn signal light intensity, in cd/m^2.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Period, SignallightPeriod** — Turn signal light period `1` (default) | positive scalar

Turn signal light period, in s.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

### **Pulse width, SignalPulseWidth** — Pulse width `50` (default) | positive scalar less than 100

Turn signal light pulse width, specified as a percent of the period.

#### Dependencies

To enable this parameter, select **Enable light
controls**.

**Data Types:** `double`

## Libraries

Automated Driving Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components Simulink 3D Animation / Simulation 3D / Actors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Vehicle with Ground Following block requires
Simulink
3D Animation.

## Description

Implement vehicle that follows ground in 3D environment

**Note**

Simulating models with the Simulation 3D Vehicle with Ground Following block requires
Simulink®
3D Animation™.

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

The block input uses the vehicle Z-down
*right-handed* (RH) *Cartesian* coordinate system
defined in SAE J6701. The coordinate system is inertial and
initially aligned with the vehicle geometric center:

- *X*-axis — Along vehicle longitudinal axis, points forward
- *Y*-axis — Along vehicle lateral axis, points to the right
- *Z*-axis — Points downward

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

For more information about execution order, see Control and Display Execution Order.

You can configure the Simulation 3D Vehicle with Ground Following block to
import custom meshes and control vehicle lights.
