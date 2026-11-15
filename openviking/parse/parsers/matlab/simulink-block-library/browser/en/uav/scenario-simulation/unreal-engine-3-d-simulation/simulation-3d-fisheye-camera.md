---
type: simulink-block
title: 'Simulation 3D Fisheye Camera'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine 3-D Simulation'
documentation_page: 'simulation3dfisheyecamera'
documentation_source_path: 'ref/simulation3dfisheyecamera.html'
language: en
---

# Simulation 3D Fisheye Camera

## Ports

### Input

### **Rel Translation** — Relative translation of sensor from mounting point (m) `[0 0 0]` (default) | real-valued 1-by-3 vector of form [*X* *Y* *Z*]

Relative translation of the sensor from its mounting point on the vehicle, in meters, specified
as a real-valued 1-by-3 vector of the form [*X*
*Y*
*Z*].

#### Dependencies

To enable this port, select the **Input** parameter next to the
**Relative
translation [X, Y, Z] (m)** parameter. For more details, see Sensor Position Transformation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rel Rotation** — Relative rotation of sensor from mounting point (deg) `[0 0 0]` (default) | real-valued 1-by-3 vector of form [*Roll* *Pitch* *Yaw*]

Relative rotation of the sensor from its mounting point on the vehicle, in degrees, specified
as a real-valued 1-by-3 vector of the form [*Roll*
*Pitch*
*Yaw*].

#### Dependencies

To enable this port, select the **Input** parameter next to the
**Relative
rotation [Roll, Pitch, Yaw] (deg)** parameter. For more details,
see Sensor Position Transformation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### Output

### **Image** — 3D output camera image *m*-by-*n*-by-3 array of RGB triplet values

3D output camera image, returned as an *m*-by-*n*-by-3 array of RGB triplet values. *m* is the vertical resolution of the image, and *n* is the horizontal resolution of the image.

**Data Types:** `int8` | `uint8`

### **Translation** — Sensor location real-valued 1-by-3 vector

Sensor location along the *X*-axis, *Y*-axis,
and *Z*-axis of the scene. The
**Translation** values are in the world coordinates of the
scene. In this coordinate system, the *Z*-axis points up from the
ground. Units are in meters.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output location
(m) and orientation (rad)**.

**Data Types:** `double`

### **Rotation** — Sensor orientation real-valued 1-by-3 vector

Roll, pitch, and yaw sensor orientation about the *X*-axis,
*Y*-axis, and *Z*-axis of the
scene. The
**Rotation** values are in the world
coordinates of the scene. These values are positive in the clockwise
direction when looking in the positive directions of these axes.
Units are in radians.

#### Dependencies

To enable this port, on the **Ground Truth** tab,
select **Output
location (m) and orientation (rad)**.

**Data Types:** `double`

## Parameters

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

### **Mounting location** — Sensor mounting location `Origin` (default) | ...

Sensor mounting location. By default, the block places the sensor relative to the
scene or vehicle origin, depending on the **Parent name**
parameter.

- When **Parent name** is `Scene
  Origin`, the block mounts the sensor relative to the scene
  origin, and during simulation, the sensor remains stationary.
- When **Parent name** is the name of a vehicle, the block
  mounts the sensor relative to the vehicle origin, and during simulation, the
  sensor travels with the vehicle.

To specify the relative position and orientation of the sensor with
respect to the scene or vehicle origin, use the **Relative translation [X, Y, Z]
(m)** and **Relative rotation [Roll, Pitch, Yaw] (deg)**
parameters.

The location of vehicle origin depends on the vehicle type. To
select the vehicle type, specify the **Type** parameter of the Simulation 3D UAV
Vehicle block to which you are mounting the sensor. Visit the reference page
for each vehicle type for more information on the vehicle dimensions and location of the
vehicle origin

### **Specify offset** — Specify offset from mounting location `On` (default)

Select this parameter to specify an offset from the mounting location by using the **Relative
translation [X, Y, Z] (m)** and **Relative
rotation [Roll, Pitch, Yaw] (deg)**
parameters.

### **Relative translation [X, Y, Z] (m)** — Translation offset relative to mounting location `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Translation offset relative to the mounting location of the sensor, specified as a
real-valued 1-by-3 vector of the form [*X*, *Y*,
*Z*]. Units are in
meters.

If you mount the sensor to a
vehicle by setting **Parent name** to the name of that vehicle, then
*X*, *Y*, and *Z* are in
the vehicle coordinate system, where:

- The *X*-axis points forward from the vehicle.
- The *Y*-axis points to the left of the vehicle, as
  viewed when looking in the forward direction of the vehicle.
- The *Z*-axis points up.

The origin is the mounting location specified in the **Mounting
location** parameter. This origin is different from the vehicle origin,
which is the geometric center of the vehicle.

If you mount the sensor to the
scene origin by setting **Parent name** to `Scene
Origin`, then *X*, *Y*, and
*Z* are in the world coordinates of the scene.

For more details about the vehicle and
world coordinate systems, see Coordinate Systems for Unreal Engine Simulation in UAV Toolbox.

**Example:** `[0,0,0.01]`

#### Adjust Relative Translation During Simulation

To adjust the relative translation of the sensor during simulation, enable the
**Rel Translation** input port by selecting the
**Input** parameter next to the **Relative translation [X,
Y, Z] (m)** parameter. For more details about the relative translation and
rotation of this sensor, see Sensor Position Transformation.

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Relative rotation [Roll, Pitch, Yaw] (deg)** — Rotational offset relative to mounting location `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Rotational offset relative to the mounting location of the sensor, specified as a
real-valued 1-by-3 vector of the form [*Roll*,
*Pitch*, *Yaw*]. Roll, pitch, and yaw are the
angles of rotation about the *X*-, *Y*-, and
*Z*-axes, respectively. Units are in
degrees.

If you mount the sensor to a
vehicle by setting **Parent name** to the name of that vehicle, then
*X*, *Y*, and *Z* are in
the vehicle coordinate system, where:

- The *X*-axis points forward from the vehicle.
- The *Y*-axis points to the left of the vehicle, as
  viewed when looking in the forward direction of the vehicle.
- The *Z*-axis points up.
- Roll, pitch, and yaw are clockwise-positive when looking in the forward
  direction of the *X*-axis, *Y*-axis,
  and *Z*-axis, respectively. If you view a scene from a 2D
  top-down perspective, then the yaw angle (also called the orientation angle)
  is counterclockwise-positive because you are viewing the scene in the
  negative direction of the *Z*-axis.

The origin is the mounting location specified in the **Mounting
location** parameter. This origin is different from the vehicle origin,
which is the geometric center of the vehicle.

If you mount the sensor to the
scene origin by setting **Parent name** to `Scene
Origin`, then *X*, *Y*, and
*Z* are in the world coordinates of the scene.

For more details about the vehicle and world
coordinate systems, see Coordinate Systems for Unreal Engine Simulation in UAV Toolbox.

**Example:** `[0,0,10]`

#### Adjust Relative Rotation During Simulation

To adjust the relative rotation of the sensor during simulation, enable the
**Rel Rotation** input port by selecting the
**Input** parameter next to the **Relative rotation [Roll,
Pitch, Yaw] (deg)** parameter. For more details about the relative
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

### **Output location (m) and orientation (rad)** — Output location and orientation of sensor `off` (default) | `on`

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

**Introduced in R2019b**

### R2025a: Performance optimization

The sensor models in the Unreal Engine executable now run at the same sample rate set in the Simulation 3D blocks. This software update improves the frame rate and model execution time.

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Fisheye Camera block requires
Simulink
3D Animation.

## Description

Fisheye camera sensor model in 3D simulation environment

**Note**

Simulating models with the Simulation 3D Fisheye Camera block requires
Simulink®
3D Animation™ and Computer Vision Toolbox™.

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

For more information about execution order, see How Unreal Engine Simulation for Automated Driving Works (Automated Driving Toolbox).
