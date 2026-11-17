---
type: simulink-block
title: 'Simulation 3D Fisheye Camera'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Sensors'
documentation_page: 'simulation3dfisheyecamera'
documentation_source_path: 'simulation3dfisheyecamera.html'
language: en
---

# Simulation 3D Fisheye Camera

## Ports
```yaml
ports:
- name: Rel Translation
  summary: Relative translation of sensor from mounting point [0 0 0] (default) | real-valued 1-by-3 vector of form [*X* *Y*
    *Z*]
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Rel Rotation
  summary: Relative rotation of sensor from mounting point [0 0 0] (default) | real-valued 1-by-3 vector of form [*Roll* *Pitch*
    *Yaw*]
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Image
  summary: 3D output camera image *m*-by-*n*-by-3 array of RGB triplet values
  direction: output
  data_types: int8 | uint8
- name: Translation
  summary: Sensor location real-valued 1-by-3 vector
  direction: output
  data_types: double
- name: Rotation
  summary: Sensor orientation real-valued 1-by-3 vector
  direction: output
  data_types: double
```

### Input

### **Rel Translation** — Relative translation of sensor from mounting point `[0 0 0]` (default) | real-valued 1-by-3 vector of form [*X* *Y* *Z*]

Relative translation of the sensor from its mounting point on the vehicle, specified
as a real-valued 1-by-3 vector of the form [*X*
*Y*
*Z*].

#### Dependencies

To enable this port, select the **Input** parameter next to the
**Relative
translation [X, Y, Z]** parameter. For more details, see Sensor Position Transformation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rel Rotation** — Relative rotation of sensor from mounting point `[0 0 0]` (default) | real-valued 1-by-3 vector of form [*Roll* *Pitch* *Yaw*]

Relative rotation of the sensor from its mounting point on the vehicle, specified
as a real-valued 1-by-3 vector of the form [*Roll*
*Pitch*
*Yaw*].

#### Dependencies

To enable this port, select the **Input** parameter next to the
**Relative rotation [Roll, Pitch, Yaw]** parameter. For more details,
see Sensor Position Transformation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Image** — 3D output camera image *m*-by-*n*-by-3 array of RGB triplet values

3D output camera image, returned as an *m*-by-*n*-by-3 array of RGB triplet values. *m* is the vertical resolution of the image, and *n* is the horizontal resolution of the image.

**Data Types:** `int8` | `uint8`

### **Translation** — Sensor location real-valued 1-by-3 vector

Sensor location along the *X*-axis, *Y*-axis,
and *Z*-axis of the scene.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output
location and orientation**.

**Data Types:** `double`

### **Rotation** — Sensor orientation real-valued 1-by-3 vector

Roll, pitch, and yaw sensor orientation about the *X*-axis,
*Y*-axis, and *Z*-axis of the
scene.

#### Dependencies

To enable this port, on the **Ground Truth** tab,
select **Output location and
orientation**.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Sensor identifier
  summary: Unique sensor identifier 1 (default) | positive integer
  group: Mounting
- name: Parent name
  summary: Name of parent vehicle Scene Origin (default) | vehicle name
  group: Mounting
- name: Coordinate system
  summary: Coordinate system for actor transformation Default (default) | MATLAB | ISO8855 | AERO | VRML | SAE
  group: Mounting
- name: Mounting location
  summary: Sensor mounting location Origin (default) | Front bumper | Rear bumper | Right mirror | Left mirror | Rearview
    mirror | Hood center | Roof center | ...
  group: Mounting
- name: Specify offset
  summary: Specify offset from mounting location off (default) | on
  group: Mounting
- name: Relative translation [X, Y, Z]
  summary: Translation offset relative to mounting location [0, 0, 0] (default) | real-valued 1-by-3 vector
  group: Mounting
- name: Relative rotation [Roll, Pitch, Yaw]
  summary: Rotational offset relative to mounting location [0, 0, 0] (default) | real-valued 1-by-3 vector
  group: Mounting
- name: Sample time
  summary: Sample time -1 (default) | positive scalar
  group: Mounting
- name: Distortion center (pixels)
  summary: Center of distortion [640, 360] (default) | real-valued 1-by-2 vector
  group: Parameters
- name: Image size (pixels)
  summary: Image size produced by camera [720, 1280] (default) | real-valued 1-by-2 vector of positive integers
  group: Parameters
- name: Mapping coefficients
  summary: Polynomial coefficients for projection function [320, 0, 0, 0] (default) | real-valued 1-by-4 vector
  group: Parameters
- name: Stretch matrix
  summary: Transforms point from sensor plane to camera plane [1, 0; 0, 1] (default) | real-valued 2-by-2 matrix
  group: Parameters
- name: Output location and orientation
  summary: Output location and orientation of sensor off (default) | on
  group: Ground Truth
```

### Mounting

### **Sensor identifier** — Unique sensor identifier `1` (default) | positive integer

Specify the unique identifier of the sensor. In a multisensor system, the sensor identifier
enables you to distinguish between sensors. When you add a new sensor block to your
model, the **Sensor identifier** of that block is *N*
+ 1, where *N* is the highest **Sensor identifier**
value among the existing sensor blocks in the model.

**Example:** `2`

### **Parent name** — Name of parent vehicle `Scene Origin` (default) | vehicle name

Name of the parent to which the sensor is mounted, specified as `Scene
Origin` or as the name of a vehicle in your model. The vehicle names
that you can select correspond to the **Name** parameters of the
simulation 3D vehicle blocks in your model. If you select `Scene
Origin`, the block places a sensor at the scene origin.

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

### **Mounting location** — Sensor mounting location `Origin` (default) | `Front bumper` | `Rear bumper` | `Right mirror` | `Left mirror` | `Rearview mirror` | `Hood center` | `Roof center` | ...

Sensor mounting location. By default, the block places the sensor relative to the
scene or vehicle origin, depending on the **Parent name**
parameter.

- When **Parent name** is `Scene
  Origin`, the block mounts the sensor to the origin of the
  scene. You can set the **Mounting location** to
  `Origin` only. During simulation, the sensor
  remains stationary.
- When **Parent name** is the name of a vehicle, the block
  mounts the sensor to one of the predefined mounting locations described in
  the table. During simulation, the sensor travels with the vehicle. For example, the table provides the mounting
  locations in the ISO 8855 standard coordinate system.

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

The
*X*-*Y*-*Z* mounting
location of the sensor relative to the vehicle depends on the vehicle type. To specify
the vehicle type, use the **Type** parameter of the Simulation 3D Vehicle with
Ground Following to which you mount the sensor. To obtain the
*X*-*Y*-*Z* mounting
locations for a vehicle type, see the reference page for that vehicle.

To determine the location of the sensor, open the sensor block. Then,
on the **Ground Truth** tab, select the **Output location and
orientation** parameter and inspect the data from the
**Translation** output port.

### **Specify offset** — Specify offset from mounting location `off` (default) | `on`

Select this parameter to specify an offset from the mounting location by using the **Relative translation [X, Y, Z]** and **Relative rotation [Roll, Pitch, Yaw]**
parameters.

### **Relative translation [X, Y, Z]** — Translation offset relative to mounting location `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Translation offset relative to the mounting location of the sensor, specified as a
real-valued 1-by-3 vector of the form [*X*, *Y*,
*Z*].

You can mount the sensor to a vehicle by setting **Parent
name** to the name of that vehicle. The origin is the mounting location
specified in the **Mounting location** parameter. This origin is
different from the vehicle origin, which is the geometric center of the vehicle. You can
also mount the sensor to the scene origin by setting **Parent name** to
`Scene Origin`.

For more details about the coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `[0,0,0.01]`

#### Adjust Relative Translation During Simulation

To adjust the relative translation of the sensor during simulation, enable the
**Rel Translation** input port by selecting the
**Input** parameter next to the **Relative translation [X, Y,
Z]** parameter. For more details about the relative translation and
rotation of this sensor, see Sensor Position Transformation.

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Relative rotation [Roll, Pitch, Yaw]** — Rotational offset relative to mounting location `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Rotational offset relative to the mounting location of the sensor, specified as a
real-valued 1-by-3 vector of the form [*Roll*,
*Pitch*, *Yaw*]. Roll, pitch, and yaw are the
angles of rotation about the *X*-, *Y*-, and
*Z*-axes, respectively.

You can mount the sensor to a vehicle by setting **Parent
name** to the name of that vehicle. The origin is the mounting location
specified in the **Mounting location** parameter. This origin is
different from the vehicle origin, which is the geometric center of the vehicle. You can
also mount the sensor to the scene origin by setting **Parent name** to
`Scene Origin`.

For more details about the coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `[0,0,10]`

#### Adjust Relative Rotation During Simulation

To adjust the relative rotation of the sensor during simulation, enable the
**Rel Rotation** input port by selecting the
**Input** parameter next to the **Relative rotation
[Roll, Pitch, Yaw]** parameter. For more details about the relative
translation and rotation of this sensor, see Sensor Position Transformation.

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time of the block, in seconds, specified as a positive scalar. The 3D simulation
environment frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block inherits its sample time from
the Simulation 3D Scene Configuration block.

### Parameters

These intrinsic camera parameters are equivalent to the properties of a `fisheyeIntrinsics` (Computer Vision Toolbox)
object. To obtain the intrinsic parameters for your camera, use the Camera
Calibrator app.

For details about the fisheye camera calibration process, see Using the Single Camera Calibrator App (Computer Vision Toolbox) and
Fisheye Calibration Basics (Computer Vision Toolbox).

### **Distortion center (pixels)** — Center of distortion `[640, 360]` (default) | real-valued 1-by-2 vector

Center of distortion, specified as real-valued 2-element vector. Units are in
pixels.

### **Image size (pixels)** — Image size produced by camera `[720, 1280]` (default) | real-valued 1-by-2 vector of positive integers

Image size produced by the camera, specified as a real-valued 1-by-2 vector of
positive integers of the form [*mrows*,*ncols*].
Units are in pixels.

### **Mapping coefficients** — Polynomial coefficients for projection function `[320, 0, 0, 0]` (default) | real-valued 1-by-4 vector

Polynomial coefficients for the projection function described by Scaramuzza's
Taylor model [1], specified as a real-valued
1-by-4 vector of the form `[a0 a2 a3 a4]`.

**Example:** `[320, -0.001, 0, 0]`

### **Stretch matrix** — Transforms point from sensor plane to camera plane `[1, 0; 0, 1]` (default) | real-valued 2-by-2 matrix

Transforms a point from the sensor plane to a pixel in the camera image plane. The
misalignment occurs during the digitization process when the lens is not parallel to
sensor.

**Example:** `[0, 1; 0, 1]`

### Ground Truth

### **Output location and orientation** — Output location and orientation of sensor `off` (default) | `on`

Select this parameter to output the translation and rotation of the
sensor at the **Translation** and
**Rotation** ports,
respectively.
## Libraries

UAV Toolbox / Simulation 3D Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2025a: Set coordinate system parameter

Set the **Coordinate system** parameter in
the Simulation 3D Fisheye Camera block to represent the coordinate system for actor transformation
in the 3D environment.

### R2025a: Performance optimization

The sensor models in the Unreal Engine executable now run at the same sample rate set in the Simulation 3D blocks. This software update improves the frame rate and model execution time.

## Description

Fisheye camera sensor model in 3D simulation environment

**Note**

Simulating models with the Simulation 3D Fisheye Camera block requires Computer Vision Toolbox™.

The Simulation 3D Fisheye Camera block provides an interface to a camera
with a fisheye lens in a 3D simulation environment. This environment is rendered using the
Unreal Engine® from Epic Games®. The sensor is based on the fisheye camera model proposed by Scaramuzza [1]. This model supports a
field of view of up to 195 degrees. The block outputs an image with the specified camera
distortion and size. You can also output the location and orientation of the camera in the
world coordinate system of the scene.

If you set **Sample time** to `-1`, the block uses the
sample time specified in the Simulation 3D Scene Configuration block. To use
this sensor, you must include a Simulation 3D Scene Configuration block in your
model.

**Tip**

The Simulation 3D Scene Configuration
block must execute before the Simulation 3D Fisheye Camera block. That way,
the Unreal Engine 3D visualization environment prepares the data before the Simulation 3D
Fisheye Camera block receives it. To check the block execution order, right-click
the blocks and select **Properties**. On the **General**
tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Fisheye Camera — `1`

For more information about execution order, see Control and Display Execution Order (Simulink).

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.
