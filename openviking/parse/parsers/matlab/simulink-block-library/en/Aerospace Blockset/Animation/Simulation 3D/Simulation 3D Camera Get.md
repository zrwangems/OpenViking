---
type: simulink-block
title: 'Simulation 3D Camera Get'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dcameraget'
documentation_source_path: 'simulation3dcameraget.html'
language: en
---

# Simulation 3D Camera Get

## Ports

### Output

### **Image** — 3D output camera image *m*-by-*n*-by-3 array of RGB triplet values

3D output camera image, returned as an *m*-by-*n*-by-3 array of RGB triplet values. *m* is the vertical resolution of the image, and *n* is the horizontal resolution of the image.

**Data Types:** `int8` | `uint8`

## Parameters

#### Mounting

### **Sensor identifier** — Number to identify unique sensor `0` (default) | positive integer

Unique sensor identifier, specified as a positive integer. This number is used to
identify a specific sensor. The sensor identifier distinguishes between sensors in a
multi-sensor system.

**Example:** 2

### **Parent name** — Name of parent `Scene Origin` (default) | character vector

Parent name. Block provides a list of parent actors in the model. If you select
`Scene Origin`, the block places a sensor at the scene
origin.

**Example:** `SimulinkVehicle1`

### **Mounting location** — Sensor mounting location `Origin` (default) | `Nose` | `Cockpit` | `CockpitRight` | `CockpitLeft` | `FuselageTop` | `Tail` | `Down` | `Front` | `Back` | `Right` | `Left` | `Top` | `Bottom`

Sensor mounting location.

- When **Parent name** is `Scene
  Origin`, the block mounts the sensor to the origin of the scene,
  and **Mounting location** can be set to
  `Origin` only. During simulation, the sensor remains
  stationary.
- When **Parent name** is the name of a vehicle (for example,
  `SimulinkVehicle1`) the block mounts the sensor to one
  of the predefined mounting locations described in the table. During simulation,
  the sensor travels with the vehicle.

The `Mounting Location` is one of
`Nose`, `Cockpit`,
`CockpitRight`,
`CockpitLeft`,`FuselageTop`,
`Tail`, or `Down` when the vehicle
is one of Airliner, Air Transport, General Aviation, Helicopter, Light Helicopter, Multirotor, or Sky Hogg.

The `Mounting Location` is one of
`Front`, `Back`,
`Right`, `Left`,
`Top`, `Bottom`, or
`Down` when the vehicle is one of CubeSat or SmallSat.

**Example:** `Origin`

### **Specify offset** — Specify offset from mounting location `off` (default) | `on`

Select this parameter to specify an offset from the mounting location.

### **Relative translation [X, Y, Z]** — Translation offset from mounting location `[0,0,0]` (default) | real-valued 1-by-3 vector

Specify a translation offset from the mount location, about the vehicle coordinate system
*X*, *Y*, and *Z* axes. Units are in meters.

- The *X*-axis points forward from the vehicle.
- The *Y*-axis points to the left of the vehicle, as viewed
  when facing forward.
- The *Z*-axis points up.

**Example:** `[0,0,0.01]`

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Relative rotation [Roll, Pitch, Yaw]** — Rotational offset from mounting location `[0,0,0]` (default) | real-valued 1-by-3 vector

Specify a rotational offset from the mounting location, about the vehicle coordinate system
*X*, *Y*, and *Z* axes. Units are in degrees.

- *Roll angle* is the angle of rotation about the *X*-axis of the vehicle coordinate system. A positive roll
  angle corresponds to a clockwise rotation when looking in the positive direction of
  the *X*-axis.
- *Pitch angle* is the angle of rotation about the *Y*-axis of the vehicle coordinate system. A positive pitch
  angle corresponds to a clockwise rotation when looking in the positive direction of
  the *Y*-axis.
- *Yaw angle* is the angle of rotation about the *Z* of the vehicle coordinate system. A positive yaw angle
  corresponds to a clockwise rotation when looking in the positive direction of the
  *Z*-axis.

**Example:** `[0,0,10]`

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time of the block in seconds. The 3D simulation environment frame rate is the
inverse of the sample time.

If you set the sample time to `-1`, the block uses the sample time
specified in the Simulation 3D Scene Configuration block.

#### Parameter

### **Horizontal resolution** — Pixels `uint32(1280)` (default) | `scalar`

Horizontal image resolution, in pixels.

### **Vertical resolution** — Pixels `uint32(720)` (default) | `scalar`

Vertical image resolution, in pixels.

### **Horizontal field of view** — Field of view `single(60)` (default) | `scalar`

Horizontal field of view (FOV), in deg.

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2025a: Mounting parameter name changes

These **Mounting** parameter names have changed.

| Old parameter name | New parameter name |
| --- | --- |
| **Sensor identification** | **Sensor identifier** |
| **Vehicle name** | **Parent name** |
| **Vehicle mounting location** | **Mounting location** |

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Camera Get block requires
Simulink
3D Animation.

## Description

Camera image

**Note**

Simulating models with the Simulation 3D Camera Get block requires
Simulink®
3D Animation™.

The Simulation 3D Camera Get block provides an interface to an ideal camera
in the 3D visualization environment. The image output is a red, green, and blue (RGB)
array.

If you set the sample time to `-1`, the block uses the sample time
specified in the Simulation 3D Scene Configuration block. To use this sensor,
ensure that the Simulation 3D Scene Configuration block is in your
model.

**Tip**

Verify that the Simulation 3D Scene
Configuration block executes before the Simulation 3D Camera Get
block. That way, the Unreal Engine® 3D visualization environment prepares the data before the Simulation 3D
Camera Get block receives it. To check the block execution order, right-click the
blocks and select **Properties**. On the **General** tab,
confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Camera Get — `1`

For more information about execution order, see Control and Display Execution Order.
