---
type: simulink-block
title: 'Simulation 3D Camera'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'simulation3dcamera'
documentation_source_path: 'simulation3dcamera.html'
language: en
---

# Simulation 3D Camera

## Ports

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

### **Depth** — Object depth from 0 m to 1000 m *m*-by-*n* array of object depths

Object depth for each pixel in the image, output as an
*m*-by-*n* array. *m* is the
vertical resolution of the image, and *n* is the horizontal
resolution of the image. Depth is in the range from 0 to 1000 meters.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output depth**.

**Data Types:** `double`

### **Labels** — Label identifiers *m*-by-*n* array of label identifiers

Label identifier for each pixel in the image, output as an
*m*-by-*n* array. *m* is the
vertical resolution of the image, and *n* is the horizontal
resolution of the image.

The table shows the object IDs used in the default scenes that are selectable from
the Simulation 3D Scene Configuration block. If you are using a custom scene,
in the Unreal® Editor, you can assign new object types to unused IDs.. If a
scene contains an object that does not have an assigned ID, that object is assigned an
ID of `0`. The detection of lane markings is not
supported.

| ID | Type |
| --- | --- |
| `0` | None/default |
| `1` | Building |
| `2` | *Not used* |
| `3` | Other |
| `4` | Pedestrians |
| `5` | Pole |
| `6` | Lane Markings |
| `7` | Road |
| `8` | Sidewalk |
| `9` | Vegetation |
| `10` | Vehicle |
| `11` | *Not used* |
| `12` | Generic traffic sign |
| `13` | Stop sign |
| `14` | Yield sign |
| `15` | Speed limit sign |
| `16` | Weight limit sign |
| `17-18` | *Not used* |
| `19` | Left and right arrow warning sign |
| `20` | Left chevron warning sign |
| `21` | Right chevron warning sign |
| `22` | *Not used* |
| `23` | Right one-way sign |
| `24` | *Not used* |
| `25` | School bus only sign |
| `26-38` | *Not used* |
| `39` | Crosswalk sign |
| `40` | *Not used* |
| `41` | Traffic signal |
| `42` | Curve right warning sign |
| `43` | Curve left warning sign |
| `44` | Up right arrow warning sign |
| `45-47` | *Not used* |
| `48` | Railroad crossing sign |
| `49` | Street sign |
| `50` | Roundabout warning sign |
| `51` | Fire hydrant |
| `52` | Exit sign |
| `53` | Bike lane sign |
| `54-56` | *Not used* |
| `57` | Sky |
| `58` | Curb |
| `59` | Flyover ramp |
| `60` | Road guard rail |
| 61 | Bicyclist |
| `62-66` | *Not used* |
| `67` | Deer |
| `68-70` | *Not used* |
| `71` | Barricade |
| `72` | Motorcycle |
| `73-255` | *Not used* |

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output semantic segmentation**.

**Data Types:** `uint8`

**Note**

Enabling `Labels` requires `Sim 3D Semantic` actor
with the tag `SemanticSegmentationSensor<N>` to be placed at the same
position. N is the sensor identifier. The Simulation 3D Camera block instantiates
the `Sim 3D Camera` and `Sim 3d Semantic` when the
`Labels` output is enabled.

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

These intrinsic camera parameters are equivalent to the properties of a `cameraIntrinsics` (Computer Vision Toolbox) object. To obtain the intrinsic parameters for your camera, use
the Camera Calibrator app. An arbitrary combination of intrinsic camera
parameters produces invalid images. The Simulation 3D Camera block supports a maximum field of view
of 95 degrees with distortions. For a list of the maximum fields of view for different
camera models, see Fisheye Calibration Basics (Computer Vision Toolbox).

For details about the camera calibration process, see Using the Single Camera Calibrator App (Computer Vision Toolbox) and
What Is Camera Calibration? (Computer Vision Toolbox).

### **Focal length (pixels)** — Focal length of camera `[1109, 1109]` (default) | 1-by-2 positive integer vector

Specify the focal length of the camera as a 1-by-2 positive integer vector of the
form [*fx*, *fy*]. Units are in pixels.

*fx* = *F* ×
*sx*

*fy* = *F* ×
*sy*

where:

- *F* is the focal length in world units, typically
  millimeters.
- [*sx*, *sy*] are the number of pixels per
  world unit in the *x* and *y* direction,
  respectively.

This parameter is equivalent to the `FocalLength` (Computer Vision Toolbox)
property of a `cameraIntrinsics` object.

### **Optical center (pixels)** — Optical center of camera `[640, 360]` (default) | 1-by-2 positive integer vector

Specify the optical center of the camera as a 1-by-2 positive integer vector of
the form [*cx*,*cy*]. Units are in pixels.

This parameter is equivalent to the `PrincipalPoint` (Computer Vision Toolbox) property of a `cameraIntrinsics`
object.

### **Image size (pixels)** — Image size produced by camera `[720, 1280]` (default) | 1-by-2 positive integer vector

Specify the image size produced by the camera as a 1-by-2 positive integer vector
of the form [*mrows*,*ncols*]. Units are in pixels.
The maximum image size that you can specify is `[1080,1920]`.

This parameter is equivalent to the `ImageSize` (Computer Vision Toolbox)
property of a `cameraIntrinsics` object.

### **Radial distortion coefficients** — Radial distortion coefficients `[0, 0]` (default) | real-valued 2-element vector | real-valued 3-element vector | real-valued 6-element vector

Specify the radial distortion coefficients as a real-valued 2-element, 3-element, or 6-element vector. Radial distortion is the displacement of image points along radial lines extending from the principal point.

- As image points move away from the principal point (positive radial displacement), image magnification decreases and a pincushion-shaped distortion occurs on the image.
- As image points move toward the principal point (negative radial displacement), image magnification increases and a barrel-shaped distortion occurs on the image.

The camera sensor calculates the (*x*d,*y*d) radial-distorted location of a point using a two-coefficient, three-coefficient, or six-coefficient formula. This table shows the various formulas, where:

- (*x*,*y*) = undistorted pixel locations
- *k*1,*k*2,*k*3,*k*4,*k*5,*k*6 = radial distortion coefficients of the lens
- *r*2 = *x*2 + *y*2

|  |  |  |
| --- | --- | --- |
| **Coefficients** | **Formula** | **Description** |
| `[k1, k2]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4) | This model is equivalent to the two-coefficient model used by the `RadialDistortion` (Computer Vision Toolbox) property of a `cameraIntrinsics` object. |
| `[k1, k2, k3]` | *x*d = *x*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6)  *y*d = *y*(1 + *k*1*r*2 + *k*2*r*4 + *k*3*r*6) | This model is equivalent to the three-coefficient model used by the `RadialDistortion` (Computer Vision Toolbox) property of a `cameraIntrinsics` object. |
| `[k1, k2, k3, k4, k5, k6]` | xd=x×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6yd=y×1+k1r2+​k2r4+k3r61+k4r2+k5r4+k6r6 | The six-coefficient model is based on the OpenCV radial distortion model.  **Note**  The Camera Calibrator app does not support this model. To calibrate a camera using this model, see Camera Calibration and 3D Reconstruction in the OpenCV documentation. |

### **Tangential distortion coefficients** — Tangential distortion coefficients `[0, 0]` (default) | real-valued 2-element vector

Specify the tangential distortion coefficients as a real-valued 2-element vector. Tangential distortion occurs when the lens and the image plane are not parallel.

Comparison of zero tangential distortion and tangential distortion.

The camera sensor calculates the tangential distorted location of a point, (*x*d, *y*d), using this formula:

*x*d = *x* + [2*p*1*xy* + *p*2 × (*r*2 + 2*x*2)]

*y*d = *y* + [*p*1 × (*r*2 + 2*y*2) + 2*p*2*xy*]

where:

- *x*, *y* = undistorted pixel locations
- *p*1, *p*2 = tangential distortion coefficients of the lens
- *r*2 = *x*2 + *y*2

The undistorted pixel locations appear in normalized image coordinates, with the origin at the optical center. The coordinates are expressed in world units.

This parameter is equivalent to the `TangentialDistortion` (Computer Vision Toolbox) property of a `cameraIntrinsics` object.

### **Axis skew** — Skew angle of camera axes `0` (default) | nonnegative real-valued scalar

Specify the skew angle of the camera axes as a nonnegative real-valued scalar. If
the *X*-axis and *Y*-axis are exactly
perpendicular, then the skew must be `0`. Units are
dimensionless.

This parameter is equivalent to the `Skew` (Computer Vision Toolbox) property of a
`cameraIntrinsics` object.

### **Visualize field of view** — Option to visualize camera field of view `off` (default) | `on`

*Since R2025a*

Select this parameter to visualize the camera coverage in the 3D environment. This
parameter enables visualization of the field of view with a segmented sphere to
annotate the boundaries and extent of the field of view.

### **Field of view range (m)** — Visualization range `61` (default) | positive real scalar

*Since R2025a*

Specify the visualization range of camera coverage. This parameter sets the radius
of the segmented sphere. Units are in meters.

#### Dependencies

To enable this parameter, select the **Visualize field of
view** parameter.

### Ground Truth

### **Output depth** — Output depth map `off` (default) | `on`

Select this parameter to output a depth map at the **Depth**
port.

### **Output semantic segmentation** — Output semantic segmentation map of label IDs `off` (default) | `on`

Select this parameter to output a semantic segmentation map of label IDs at the **Labels** port.

### **Output location and orientation** — Output location and orientation of sensor `off` (default) | `on`

Select this parameter to output the translation and rotation of the
sensor at the **Translation** and
**Rotation** ports,
respectively.

## Libraries

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2025a: Visualize camera field of view

Use these parameters in the **Parameters** tab to visualize the camera
field of view and set the visualization range of camera coverage in the 3D environment.

- **Visualize field of view**
- **Field of view range (m)**

### R2025a: Set coordinate system parameter

Set the **Coordinate system** parameter in
the Simulation 3D Camera block to represent the coordinate system for actor transformation
in the 3D environment.

### R2025a: Performance optimization

The sensor models in the Unreal Engine executable now run at the same sample rate set in the Simulation 3D blocks. This software update improves the frame rate and model execution time.

## Description

Camera sensor model with lens in 3D simulation environment

The Simulation 3D Camera block provides an interface to a camera with a
lens in a 3D simulation environment. This environment is rendered using the Unreal Engine® from Epic Games®. The sensor is based on the ideal pinhole camera model, with a lens added to
represent a full camera model, including lens distortion. This camera model supports a field
of view of up to 150 degrees without distortions. For more details, see Algorithms.

If you set **Sample time** to `-1`, the block uses the
sample time specified in the Simulation 3D Scene
Configuration block. To use this sensor, you must include a Simulation 3D
Scene Configuration block in your model.

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.

The block outputs images captured by the camera during simulation. You can use these
images to visualize and verify your driving algorithms. In addition, on the **Ground
Truth** tab, you can select options to output the ground truth data for developing
depth estimation and semantic segmentation algorithms. You can also output the location and
orientation of the camera in the world coordinate system of the scene. The image shows the
block with all ports enabled.

Simulation 3D Camera block with all ports enabled

The table summarizes the ports and how to enable them.

| Port | Description | Parameter for Enabling Port | Sample Visualization |
| --- | --- | --- | --- |
| **Image** | Outputs an RGB image captured by the camera | n/a | Sample image output of a city scene |
| **Depth** | Outputs a depth map with values from 0 m to 1000 meters | **Output depth** | Sample depth output of a city scene |
| **Labels** | Outputs a semantic segmentation map of label IDs that correspond to objects in the scene | **Output semantic segmentation** | Sample image semantic segmentation of a city scene |
| **Translation** | Outputs the location of the camera in the world coordinate system | **Output location and orientation** | n/a |
| **Rotation** | Outputs the orientation of the camera in the world coordinate system | **Output location and orientation** | n/a |

**Note**

The Simulation 3D Scene Configuration
block must execute before the Simulation 3D Camera block. That way, the
Unreal Engine 3D visualization environment prepares the data before the Simulation 3D
Camera block receives it. To check the block execution order, right-click the
blocks and select **Properties**. On the **General** tab,
confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Camera — `1`

For more information about execution order, see Control and Display Execution Order (Simulink).
