---
type: simulink-block
title: 'Simulation 3D Vision Detection Generator'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine Scenario Simulation / Sensors (requires Simulink 3D Animation)'
documentation_page: 'simulation3dvisiondetectiongenerator'
documentation_source_path: 'ref/simulation3dvisiondetectiongenerator.html'
language: en
---

# Simulation 3D Vision Detection Generator

## Ports

### Output

### **Object Detections** — Object detections Simulink bus containing MATLAB® structure

Object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).
The structure has the form shown in this table.

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | Integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures of length set by the **Maximum number of reported detections** parameter. Only `NumDetections` of these detections are actual detections. |

The object detection structure contains these properties.

| Property | Definition |
| --- | --- |
| `Time` | Measurement time |
| `Measurement` | Object measurements |
| `MeasurementNoise` | Measurement noise covariance matrix |
| `SensorIndex` | Unique ID of the sensor |
| `ObjectClassID` | Object classification |
| `MeasurementParameters` | Parameters used by initialization functions of nonlinear Kalman tracking filters |
| `ObjectAttributes` | Additional information passed to tracker |

The `Measurement` field reports the position and velocity of a
measurement in the coordinate system of the sensor. This field is a real-valued column
vector of the form [*x*; *y*; *z*;
*vx*; *vy*; *vz*]. The
`MeasurementNoise` field is a 6-by-6 matrix that reports the
measurement noise covariance for each coordinate in the `Measurement`
field.

The `MeasurementParameters` field is a structure that has these
fields.

| Parameter | Definition |
| --- | --- |
| `Frame` | Enumerated type indicating the frame used to report measurements. The Simulation 3D Vision Detection Generator block reports detections in sensor Cartesian coordinates, which is a rectangular coordinate frame. Therefore, for this block, `Frame` is always set to `'rectangular'`. |
| `OriginPosition` | Offset of the sensor origin from the ego vehicle origin, returned as a vector of the form [*x*, *y*, *z*]. The block derives these values from the *x*, *y*, and *z* mounting position of the sensor. For more details, see the **Mounting** parameters of this block. |
| `Orientation` | Orientation of the sensor coordinate frame with respect to the ego vehicle coordinate frame, returned as a 3-by-3 real-valued orthonormal matrix. The block derives these values from the *yaw*, *pitch*, and *roll* mounting orientation of the sensor. For more details, see the **Mounting** parameters of this block. |
| `HasVelocity` | Indicates whether measurements contain velocity. |

The `ObjectClassID` property of each detection has a value that
corresponds to an object ID. The table shows the object IDs used in the default scenes
that you can select from the Simulation 3D Scene
Configuration block. If you are using a custom scene, in the Unreal® Editor, you can assign new object types to unused IDs. For more details,
see Apply Labels to Unreal Scene Elements for Semantic Segmentation and Object Detection. If a scene
contains an object that does not have an assigned ID, that object is assigned an ID of
`0`. The block detects objects only of class
`Vehicle`, such as vehicles created by using Simulation 3D
Vehicle with Ground Following blocks, or of class
`Road`.

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

The `ObjectAttributes` property of each detection is a
structure that has these fields.

| Field | Definition |
| --- | --- |
| `TargetIndex` | Identifier of the actor, `ActorID`, that generated the detection. For false alarms, this value is negative. |

#### Dependencies

To enable this output port, on the **Parameters** tab, set the
**Types of detections generated by sensor** parameter to
`Lanes and objects`, `Objects
only`, or `Lanes with occlusion`.

### **Lane Detections** — Lane boundary detections Simulink bus containing MATLAB structure

Lane boundary detections, returned as a Simulink bus containing a MATLAB structure. The structure has these fields.

| Field | Description | Type |
| --- | --- | --- |
| `Time` | Lane detection time | Real scalar |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `SensorIndex` | Unique identifier of sensor | Positive integer |
| `NumLaneBoundaries` | Number of lane boundary detections | Nonnegative integer |
| `LaneBoundaries` | Lane boundary detections starting from the leftmost lane with respect to the ego vehicle. | Array of `clothoidLaneBoundary` objects |

#### Dependencies

To enable this output port, on the **Parameters** tab, set the
**Types of detections generated by sensor** parameter to
`Lanes and objects`, `Lanes
only`, or `Lanes with occlusion`.

### **Actor Truth** — Ground truth of actor poses Simulink bus containing MATLAB structure

Ground truth of actor poses in the simulation environment, returned as a
Simulink bus containing a MATLAB structure.

The structure has these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumActors` | Number of actors | Nonnegative integer |
| `Time` | Current simulation time | Real-valued scalar |
| `Actors` | Actor poses | `NumActors`-length array of actor pose structures |

Each actor pose structure in `Actors` has these fields.

| Field | Description |
| --- | --- |
| `ActorID` | Scenario-defined actor identifier, specified as a positive integer. |
| *In R2024b:*  `FrontAxlePosition` | Front-axle position of the vehicle, specified as a three-element row vector in the form [*x* *y* *z*]. Units are in meters.  **Note**  If the driving scenario does not contain a front-axle trajectory for at least one vehicle, then the `ActorPoses` structure does not contain this field. |
| `Position` | Position of actor, specified as a real-valued vector of the form [*x* *y* *z*]. Units are in meters. |
| `Velocity` | Velocity (*v*) of actor in the *x*- *y*-, and *z*-directions, specified as a real-valued vector of the form [*v**x* *v**y* *v**z*]. Units are in meters per second. |
| `Roll` | Roll angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `Pitch` | Pitch angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `Yaw` | Yaw angle of actor, specified as a real-valued scalar. Units are in degrees. |
| `AngularVelocity` | Angular velocity (*ω*) of actor in the *x*-, *y*-, and *z*-directions, specified as a real-valued vector of the form [*ω**x* *ω**y* *ω**z*]. Units are in degrees per second. |

The pose of the ego vehicle is excluded from the `Actors`
array.

#### Dependencies

To enable this output port, on the **Ground Truth** tab, select
the **Output actor truth** parameter.

### **Lane Truth** — Ground truth of lane boundaries Simulink bus containing MATLAB structure

Ground truth of lane boundaries in the simulation environment, returned as a
Simulink bus containing a MATLAB structure.

The structure has these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumLaneBoundaries` | Number of lane boundaries | Nonnegative integer |
| `Time` | Current simulation time | Real scalar |
| `LaneBoundaries` | Lane boundaries starting from the leftmost lane with respect to the ego vehicle. | `NumLaneBoundaries`-length array of lane boundary structures |

Each lane boundary structure in `LaneBoundaries` has these
fields.

|  |  |
| --- | --- |
| **Field** | **Description** |
| `Coordinates` | Lane boundary coordinates, specified as a real-valued *N*-by-3 matrix, where *N* is the number of lane boundary coordinates. Lane boundary coordinates define the position of points on the boundary at specified longitudinal distances away from the ego vehicle, along the center of the road.  - In MATLAB, specify these distances by using the   `'XDistance'` name-value pair argument of   the `laneBoundaries` function. - In Simulink, specify these distances by using the   **Distances from ego vehicle for computing   boundaries (m)** parameter of the Scenario   Reader block or the **Distance from parent   for computing lane boundaries** parameter of the   Simulation 3D Vision Detection Generator   block.  This matrix also includes the boundary coordinates at zero distance from the ego vehicle. These coordinates are to the left and right of the ego-vehicle origin, which is located under the center of the rear axle. Units are in meters. |
| `Curvature` | Lane boundary curvature at each row of the `Coordinates` matrix, specified as a real-valued *N*-by-1 vector. *N* is the number of lane boundary coordinates. Units are in radians per meter. |
| `CurvatureDerivative` | Derivative of lane boundary curvature at each row of the `Coordinates` matrix, specified as a real-valued *N*-by-1 vector. *N* is the number of lane boundary coordinates. Units are in radians per square meter. |
| `HeadingAngle` | Initial lane boundary heading angle, specified as a real scalar. The heading angle of the lane boundary is relative to the ego vehicle heading. Units are in degrees. |
| `LateralOffset` | Lateral offset of the ego vehicle position from the lane boundary, specified as a real scalar. An offset to a lane boundary to the left of the ego vehicle is positive. An offset to the right of the ego vehicle is negative. Units are in meters. In this image, the ego vehicle is offset 1.5 meters from the left lane and 2.1 meters from the right lane.  Ego vehicle in a driving lane |
| `BoundaryType` | Type of lane boundary marking, specified as one of these values:  - `'Unmarked'` — No physical lane marker   exists - `'Solid'`  — Single unbroken line - `'Dashed'` — Single line of dashed lane   markers - `'DoubleSolid'` — Two unbroken lines - `'DoubleDashed'` — Two dashed lines - `'SolidDashed'` — Solid line on the left and   a dashed line on the right - `'DashedSolid'` — Dashed line on the left and   a solid line on the right |
| `Strength` | Saturation strength of the lane boundary marking, specified as a real scalar from 0 to 1. A value of `0` corresponds to a marking whose color is fully unsaturated. The marking is gray. A value of `1` corresponds to a marking whose color is fully saturated. |
| `Width` | Lane boundary width, specified as a positive real scalar. In a double-line lane marker, the same width is used for both lines and for the space between lines. Units are in meters. |
| `Length` | Length of dash in dashed lines, specified as a positive real scalar. In a double-line lane marker, the same length is used for both lines. |
| `Space` | Length of space between dashes in dashed lines, specified as a positive real scalar. In a dashed double-line lane marker, the same space is used for both lines. |

The number of returned lane boundary structures depends on the **Maximum
number of reported lanes** parameter value.

#### Dependencies

To enable this output port, on the **Ground Truth** tab, select
the **Output lane truth** parameter.

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
  the table. During simulation, the sensor travels with the vehicle.

| Mounting Location | Description | Orientation Relative to Vehicle Origin [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | Forward-facing sensor mounted to the vehicle origin, which is on the ground and at the geometric center of the vehicle (see Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox)  Vehicle with sensor mounted at origin | [0, 0, 0] |
| `Front bumper`  `Front center` | Forward-facing sensor mounted to the front bumper  Vehicle with sensor mounted at front bumper | [0, 0, 0] |
| `Rear bumper`  `Rear center` | Backward-facing sensor mounted to the rear bumper  Vehicle with sensor mounted at rear bumper | [0, 0, 180] |
| `Right mirror` | Downward-facing sensor mounted to the right side-view mirror  Vehicle with sensor mounted at right side-view mirror | [0, –90, 0] |
| `Left mirror` | Downward-facing sensor mounted to the left side-view mirror  Vehicle with sensor mounted at left side-view mirror | [0, –90, 0] |
| `Rearview mirror` | Forward-facing sensor mounted to the rearview mirror, inside the vehicle  Vehicle with sensor mounted at rearview mirror | [0, 0, 0] |
| `Hood center` | Forward-facing sensor mounted to the center of the hood  Vehicle with sensor mounted at hood center | [0, 0, 0] |
| `Roof center` | Forward-facing sensor mounted to the center of the roof  Vehicle with sensor mounted at roof center | [0, 0, 0] |

Roll, pitch, and yaw are clockwise-positive
when looking in the positive direction of the *X*-axis,
*Y*-axis, and *Z*-axis, respectively. When
looking at a vehicle from above, the yaw angle (the orientation angle) is
counterclockwise-positive because you are looking in the negative direction of the
axis.

The
*X*-*Y*-*Z* mounting
location of the sensor relative to the vehicle depends on the vehicle type. To specify
the vehicle type, use the **Type** parameter of the Simulation 3D Vehicle with
Ground Following to which you mount the sensor. To obtain the
*X*-*Y*-*Z* mounting
locations for a vehicle type, see the reference page for that vehicle.

To determine the location of the sensor in world coordinates, open the sensor block. Then,
on the **Ground Truth** tab, select the **Output location (m) and orientation
(rad)** parameter and inspect the data from the
**Translation** output port.

### **Specify offset** — Specify offset from mounting location `off` (default) | `on`

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

For more details about the vehicle and world
coordinate systems, see Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox.

**Example:** `[0,0,0.01]`

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

For more details about the vehicle and world coordinate systems, see Coordinate Systems for Unreal Engine Simulation in Automated Driving Toolbox.

**Example:** `[0,0,10]`

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time of the block, in seconds, specified as a positive scalar. The 3D simulation
environment frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block inherits its sample time from
the Simulation 3D Scene Configuration block.

### Parameters

#### Detection Reporting

### **Types of detections generated by sensor** — Types of detections generated by sensor `Lanes and objects` (default) | `Objects only` | `Lanes only` | `Lanes with occlusion`

Types of detections generated by the sensor, specified as one of these options:

- `Lanes and objects` — Detect lanes and objects. No
  road information is used to occlude actors.
- `Objects only` — Detect objects only.
- `Lanes only` — Detection lanes only.
- `Lanes with occlusion` — Detect lane and objects.
  Objects in the camera field of view can impair the ability of the sensor to
  detect lanes.

### **Maximum number of reported detections** — Maximum number of reported detections `50` (default) | positive integer

Maximum number of detections reported by the sensor, specified as a positive
integer. Detections are reported in order of increasing distance from the sensor until
the maximum number is reached.

**Example:** `100`

### **Maximum number of reported lanes** — Maximum number of reported lanes `30` (default) | positive integer

Maximum number of reported lanes, specified as a positive integer.

**Example:** `100`

### **Distance from parent for computing lane boundaries** — Distances from parent frame at which to compute lane boundaries `0:0.5:9.5` (default) | *N*-element real-valued vector

Distances from the parent frame at which to compute the lane boundaries, specified
as an *N*-element real-valued vector. *N* is the
number of distance values. *N* should not exceed 100. Units are in
meters.

The *parent* is the frame to which the sensor is mounted,
such as the ego vehicle. The **Parent name** parameter determines the
parent frame. Distances are relative to the origin of the parent frame.

When detecting lanes from rear-facing cameras, specify negative distances. When
detecting lanes from front-facing cameras, specify positive distances.

By default, the block computes a lane boundary every 0.5 meters over the range
from 0 to 9.5 meters ahead of the parent.

**Example:** `1:0.1:10` computes a lane boundary every 0.1 meters over
the range from 1 to 10 meters ahead of the parent.

#### Output Port Settings

### **Source of object bus name** — Source of object bus name `Auto` (default) | `Property`

Source of object bus name, specified as `Auto` or
`Property`. If you select `Auto`,
the block creates a bus name. If you select `Property`,
specify the bus name by using the **Object bus name**
parameter.

### **Object bus name** — Object bus name `BusObjectDetections` | valid bus name

Object bus name, specified as a valid bus name.

#### Dependencies

To enable this parameter, set the **Source of object bus name**
parameter to `Property`.

### **Source of output lane bus name** — Source of output lane bus name `Auto` (default) | `Property`

Source of output lane bus name, specified as `Auto` or
`Property`. If you select `Auto`,
the block creates a bus name. If you select `Property`,
specify the bus name by using the **Specify an output lane bus name**
parameter.

### **Specify an output lane bus name** — Lane bus name `BusLaneDetections` (default) | valid bus name

Lane bus name, specified as a valid bus name.

#### Dependencies

To enable this parameter, set the **Source of output lane bus
name** parameter to `Property`.

### Measurements

### **Maximum detection range (m)** — Maximum detection range `150` (default) | positive real scalar

Maximum detection range, specified as a positive real scalar. The vision sensor
cannot detect objects beyond this range. Units are in meters.

**Example:** `250`

#### Object Detector Settings

### **Bounding box accuracy (pixels)** — Bounding box accuracy `5` (default) | positive real scalar

Bounding box accuracy, specified as a positive real scalar. This quantity defines
the accuracy with which the detector can match a bounding box to a target. Units are
in pixels.

**Example:** `9`

### **Smoothing filter noise intensity (m/s^2)** — Noise intensity used for filtering position and velocity measurements `5` (default) | positive real scalar

Noise intensity used for filtering position and velocity measurements, specified
as a positive real scalar. Noise intensity defines the standard deviation of the
process noise of the internal constant-velocity Kalman filter used in a vision sensor.
The filter models the process noise by using a piecewise-constant white noise
acceleration model. Noise intensity is typically of the order of the maximum
acceleration magnitude expected for a target. Units are in meters per second
squared.

**Example:** `2`

### **Maximum detectable object speed (m/s)** — Maximum detectable object speed `50` (default) | nonnegative real scalar

Maximum detectable object speed, specified as a nonnegative real scalar. Units are
in meters per second.

**Example:** `20`

### **Maximum allowed occlusion for detector** — Maximum allowed occlusion of an object `0.5` (default) | real scalar in the range [0 1)

Maximum allowed occlusion of an object, specified as a real scalar in the range [0
1). *Occlusion* is the fraction of the total surface area of an
object that is not visible to the sensor. A value of 1 indicates that the object is
fully occluded. Units are dimensionless.

**Example:** `0.2`

### **Minimum detectable image size of an object (pixels)** — Minimum height and width of an object `[15,15]` (default) | 1-by-2 vector of positive values

Minimum height and width of an object that the vision sensor detects within an
image, specified as a `[minHeight,minWidth]` vector of positive
values. The 2-D projected height of an object must be greater than or equal to
`minHeight`. The projected width of an object must be greater than
or equal to `minWidth`. Units are in pixels.

**Example:** `[25 20]`

### **Probability of detecting a target** — Probability of detection `0.9` (default) | positive real scalar less than or equal to 1

Probability of detecting a target, specified as a positive real scalar less than
or equal to 1. This quantity defines the probability that the sensor detects a
detectable object. A *detectable object* is an object that
satisfies the minimum detectable size, maximum range, maximum speed, and maximum
allowed occlusion constraints.

**Example:** `0.95`

### **Number of false positives per image** — Number of false detections generated by vision sensor per image `0.1` (default) | nonnegative real scalar

Number of false detections generated by the vision sensor per image, specified as
a nonnegative real scalar.

**Example:** `1.0`

#### Lane Detector Settings

### **Minimum lane size in image (pixels)** — Maximum size of lane `[20,3]` (default) | 1-by-2 real-valued vector

Minimum size of a projected lane marking in the camera image that the sensor can
detect after accounting for curvature, specified as a 1-by-2 real-valued vector of the
form `[minHeight, minWidth]`. Lane markings must exceed both of these
values to be detected. Units are in pixels.

### **Accuracy of lane boundary (pixels)** — Accuracy of lane boundary `3` (default) | positive real scalar

Accuracy of lane boundaries, specified as a positive real scalar. This parameter
defines the accuracy with which the lane sensor can place a lane boundary. Units are
in pixels.

**Example:** `2.5`

#### Random Number Generator Settings

### **Add noise to measurements** — Enable adding noise to vision sensor measurements `on` (default) | `off`

Select this parameter to add noise to vision sensor measurements. Otherwise, the
measurements are noise-free. The `MeasurementNoise` property of
each detection is always computed and is not affected by the value you specify for the
**Add noise to measurements** parameter.

### **Select method to specify initial seed** — Method to specify random number generator seed `Repeatable` (default) | `Specify seed` | `Not repeatable`

Method to set the random number generator seed, specified as one of the options in
the table.

| Option | Description |
| --- | --- |
| `Repeatable` | The block generates a random initial seed for the first simulation and reuses this seed for all subsequent simulations. Select this parameter to generate repeatable results from the statistical sensor model. To change this initial seed, at the MATLAB command prompt, enter: `clear all`. |
| `Specify seed` | Specify your own random initial seed for reproducible results by using the **Initial seed** parameter. |
| `Not repeatable` | The block generates a new random initial seed after each simulation run. Select this parameter to generate nonrepeatable results from the statistical sensor model. |

### **Initial seed** — Random number generator seed `1` (default) | nonnegative integer less than 232

Random number generator seed, specified as a nonnegative integer less than
232.

**Example:** `2001`

#### Dependencies

To enable this parameter, set the **Select method to specify initial
seed** parameter to `Specify seed`.

### Camera Intrinsics

### **Focal length (pixels)** — Camera focal length `[800,800]` (default) | two-element real-valued vector

Camera focal length, in pixels, specified as a two-element real-valued vector. See
also the `FocalLength`
property of `cameraIntrinsics`.

**Example:** `[480,320]`

### **Optical center (pixels)** — Optical center of camera `[320,240]` (default) | two-element real-valued vector

Optical center of the camera, in pixels, specified as a two-element real-valued
vector. See also the `PrincipalPoint` property of `cameraIntrinsics`.

**Example:** `[480,320]`

### **Image size (pixels)** — Image size produced by camera `[480,640]` (default) | two-element vector of positive integers

Image size produced by the camera, in pixels, specified as a two-element vector of
positive integers. See also the `ImageSize`
property of `cameraIntrinsics`.

**Example:** `[240,320]`

### **Radial distortion coefficients** — Radial distortion coefficients `[0,0]` (default) | two-element real-valued vector | three-element real-valued vector

Radial distortion coefficients, specified as a two-element or three-element
real-valued vector. For details on setting these coefficients, see the `RadialDistortion` property of `cameraIntrinsics`.

**Example:** `[1,1]`

### **Tangential distortion coefficients** — Tangential distortion coefficients `[0,0]` (default) | two-element real-valued vector

Tangential distortion coefficients, specified as a two-element real-valued vector.
For details on setting these coefficients, see the `TangentialDistortion` property of
`cameraIntrinsics`.

**Example:** `[1,1]`

### **Skew of the camera axes** — Skew angle of camera axes `0` (default) | real scalar

Skew angle of the camera axes, specified as a real scalar. See also the `Skew` property of
`cameraIntrinsics`.

**Example:** `0.1`

### Ground Truth

### **Output actor truth** — Output ground truth of actors `off` (default) | `on`

Select this parameter to output the ground truth of actors on the **Actor
Truth** output port.

### **Output lane truth** — Output ground truth of lane boundaries `off` (default) | `on`

Select this parameter to output the ground truth of lane boundaries on the
**Lane Truth** output port.

## Libraries

Automated Driving Toolbox / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Vision Detection Generator block requires
Simulink
3D Animation.

## Description

Detect objects and lanes from measurements in 3D simulation environment

**Note**

Simulating models with the Simulation 3D Vision Detection Generator block requires
Simulink®
3D Animation™.

The Simulation 3D Vision Detection Generator block generates detections
from camera measurements taken by a vision sensor mounted on an ego vehicle in a 3D simulation
environment. This environment is rendered using the Unreal Engine® from Epic Games®. The block derives detections from simulated actor poses that are based on
cuboid (box-shaped) representations of the actors in the scenario. For more details, see Algorithms.

The block generates detections at intervals equal to the sensor update interval.
Detections are referenced to the coordinate system of the sensor. The block can simulate real
detections that have added random noise and also generate false positive detections. A
statistical model generates the measurement noise, true detections, and false positives. To
control the random numbers that the statistical model generates, use the random number
generator settings on the **Measurements** tab of the block.

If you set **Sample time** to `-1`, the block uses the
sample time specified in the Simulation 3D Scene Configuration block. To use
this sensor, you must include a Simulation 3D Scene Configuration block in your
model.

**Tip**

The Simulation 3D Scene Configuration
block must execute before the Simulation 3D Vision Detection Generator block.
That way, the Unreal Engine 3D visualization environment prepares the data before the Simulation 3D
Vision Detection Generator block receives it. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Vision Detection Generator —
  `1`

For more information about execution order, see How Unreal Engine Simulation for Automated Driving Works.
