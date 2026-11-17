---
type: simulink-block
title: 'Simulation 3D Camera Get'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Utilities'
documentation_page: 'simulation3dcameraget'
documentation_source_path: 'simulation3dcameraget.html'
language: en
---

# Simulation 3D Camera Get

## Ports
```yaml
ports:
- name: Image
  summary: 3D output camera image *m*-by-*n*-by-3 array of RGB triplet values
  direction: output
  data_types: int8 | uint8
```

### Output

### **Image** — 3D output camera image *m*-by-*n*-by-3 array of RGB triplet values

3D output camera image, returned as an *m*-by-*n*-by-3 array of RGB triplet values. *m* is the vertical resolution of the image, and *n* is the horizontal resolution of the image.

**Data Types:** `int8` | `uint8`
## Parameters
```yaml
parameters:
- name: Sensor identifier
  summary: Number to identify unique sensor 0 (default) | positive integer
  group: ''
- name: Parent name
  summary: Name of parent Scene Origin (default) | character vector
  group: ''
- name: Coordinate system
  summary: Coordinate system for actor transformation Default (default) | MATLAB | ISO8855 | AERO | VRML | SAE
  group: ''
- name: Mounting location
  summary: Sensor mounting location Origin (default) | Front bumper | Rear bumper | Right mirror | Left mirror | Rearview
    mirror | Hood center | Roof center
  group: ''
- name: Specify offset
  summary: Specify offset from mounting location off (default) | on
  group: ''
- name: Relative translation [X, Y, Z]
  summary: Translation offset from mounting location [0,0,0] (default) | real-valued 1-by-3 vector
  group: ''
- name: Relative rotation [Roll, Pitch, Yaw]
  summary: Rotational offset from mounting location [0,0,0] (default) | real-valued 1-by-3 vector
  group: ''
- name: Sample time
  summary: Sample time -1 (default) | positive scalar
  group: ''
- name: Horizontal resolution
  summary: Pixels uint32(1280) (default) | scalar
  group: ''
- name: Vertical resolution
  summary: Pixels uint32(720) (default) | scalar
  group: ''
- name: Horizontal field of view
  summary: Field of view single(60) (default) | scalar
  group: ''
```

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

### **Coordinate system** — Coordinate system for actor transformation `Default` (default) | `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

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

### **Mounting location** — Sensor mounting location `Origin` (default) | `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center`

Sensor mounting location.

- When **Parent name** is `Scene
  Origin`, the block mounts the sensor to the origin of the scene,
  and **Mounting location** can be set to
  `Origin` only. During simulation, the sensor remains
  stationary.
- When **Parent name** is the name of a vehicle (for example,
  `SimulinkVehicle1`) the block mounts the sensor to one
  of the predefined mounting locations described in the table. During simulation,
  the sensor travels with the vehicle. For example, the
  table provides the mounting locations in the ISO 8855 standard coordinate
  system.

| Mounting Location | Description | Orientation Relative to Vehicle Origin [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | Forward-facing sensor mounted to the vehicle origin, which is on the ground and at the geometric center of the vehicle (see Coordinate Systems in Simulink 3D Animation)  Vehicle with sensor mounted at origin | [0, 0, 0] |
| `Front bumper`  `Front center` | Forward-facing sensor mounted to the front bumper  Vehicle with sensor mounted at front bumper | [0, 0, 0] |
| `Rear bumper`  `Rear center` | Backward-facing sensor mounted to the rear bumper  Vehicle with sensor mounted at rear bumper | [0, 0, 180] |
| `Right mirror` | Downward-facing sensor mounted to the right side-view mirror  Vehicle with sensor mounted at right side-view mirror | [0, –90, 0] |
| `Left mirror` | Downward-facing sensor mounted to the left side-view mirror  Vehicle with sensor mounted at left side-view mirror | [0, –90, 0] |
| `Rearview mirror` | Forward-facing sensor mounted to the rearview mirror, inside the vehicle  Vehicle with sensor mounted at rearview mirror | [0, 0, 0] |
| `Hood center` | Forward-facing sensor mounted to the center of the hood  Vehicle with sensor mounted at hood center | [0, 0, 0] |
| `Roof center` | Forward-facing sensor mounted to the center of the roof  Vehicle with sensor mounted at roof center | [0, 0, 0] |

The (*X*, *Y*, *Z*)
location of the sensor relative to the vehicle depends on the vehicle type. To specify
the vehicle type, use the **Type** parameter of the Simulation 3D Vehicle with
Ground Following block to which you are mounting.

For example, the tables show the *X*,
*Y*, and *Z* locations of sensors in the ISO
8855 standard coordinate system.

**Box Truck — Sensor Locations Relative to Vehicle Origin**

| Mounting Location | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 5.10 | 0 | 0.60 |
| `Rear bumper` | –5 | 0 | 0.60 |
| `Right mirror` | 2.90 | 1.60 | 2.10 |
| `Left mirror` | 2.90 | –1.60 | 2.10 |
| `Rearview mirror` | 2.60 | 0.20 | 2.60 |
| `Hood center` | 3.80 | 0 | 2.10 |
| `Roof center` | 1.30 | 0 | 4.20 |

**Hatchback — Sensor Locations Relative to Vehicle Origin**

| Mounting Location | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 1.93 | 0 | 0.51 |
| `Rear bumper` | –1.93 | 0 | 0.51 |
| `Right mirror` | 0.43 | –0.84 | 1.01 |
| `Left mirror` | 0.43 | 0.84 | 1.01 |
| `Rearview mirror` | 0.32 | 0 | 1.27 |
| `Hood center` | 1.44 | 0 | 1.01 |
| `Roof center` | 0 | 0 | 1.57 |

**Muscle Car — Sensor Locations Relative to Vehicle Origin**

| Mounting Location | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 2.47 | 0 | 0.45 |
| `Rear bumper` | –2.47 | 0 | 0.45 |
| `Right mirror` | 0.43 | –1.08 | 1.01 |
| `Left mirror` | 0.43 | 1.08 | 1.01 |
| `Rearview mirror` | 0.32 | 0 | 1.20 |
| `Hood center` | 1.28 | 0 | 1.14 |
| `Roof center` | –0.25 | 0 | 1.58 |

**Sedan — Sensor Locations Relative to Vehicle Origin**

| Mounting Location | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 2.42 | 0 | 0.51 |
| `Rear bumper` | –2.42 | 0 | 0.51 |
| `Right mirror` | 0.59 | –0.94 | 1.09 |
| `Left mirror` | 0.59 | 0.94 | 1.09 |
| `Rearview mirror` | 0.43 | 0 | 1.31 |
| `Hood center` | 1.46 | 0 | 1.11 |
| `Roof center` | –0.45 | 0 | 1.69 |

**Small Pickup Truck — Sensor Locations Relative to Vehicle Origin**

| Mounting Location | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 3.07 | 0 | 0.51 |
| `Rear bumper` | –3.07 | 0 | 0.51 |
| `Right mirror` | 1.10 | –1.13 | 1.52 |
| `Left mirror` | 1.10 | 1.13 | 1.52 |
| `Rearview mirror` | 0.85 | 0 | 1.77 |
| `Hood center` | 2.22 | 0 | 1.59 |
| `Roof center` | 0 | 0 | 2.27 |

**Sport Utility Vehicle — Sensor Locations Relative to Vehicle Origin**

| Mounting Location | X (m) | Y (m) | Z (m) |
| --- | --- | --- | --- |
| `Front bumper` | 2.42 | 0 | 0.51 |
| `Rear bumper` | –2.42 | 0 | 0.51 |
| `Right mirror` | 0.60 | –1 | 1.35 |
| `Left mirror` | 0.60 | 1 | 1.35 |
| `Rearview mirror` | 0.39 | 0 | 1.55 |
| `Hood center` | 1.58 | 0 | 1.39 |
| `Roof center` | –0.56 | 0 | 2 |

**Example:** `Origin`

### **Specify offset** — Specify offset from mounting location `off` (default) | `on`

Select this parameter to specify an offset from the mounting location.

### **Relative translation [X, Y, Z]** — Translation offset from mounting location `[0,0,0]` (default) | real-valued 1-by-3 vector

Specify a translation offset from the mount location, about the
*X*, *Y*, and *Z* axes.

**Example:** `[0,0,0.01]`

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Relative rotation [Roll, Pitch, Yaw]** — Rotational offset from mounting location `[0,0,0]` (default) | real-valued 1-by-3 vector

Specify a rotational offset from the mounting location, about the
*X*, *Y*, and *Z* axes.

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

**Introduced in R2022b**

### R2025a: Mounting parameter name changes

These **Mounting** parameter names have changed.

| Old parameter name | New parameter name |
| --- | --- |
| **Sensor identification** | **Sensor identifier** |
| **Vehicle name** | **Parent name** |
| **Vehicle mounting location** | **Mounting location** |

### R2025a: Set coordinate system parameter

Set the **Coordinate system** parameter in
the Simulation 3D Camera Get block to represent the coordinate system for actor transformation
in the 3D environment.

## Description

Camera image

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

For more information about execution order, see Control and Display Execution Order (Simulink).

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.
