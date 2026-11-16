---
type: simulink-block
title: 'Ultrasonic Detection Generator'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'ultrasonicdetectiongenerator'
documentation_source_path: 'ref/ultrasonicdetectiongenerator.html'
language: en
---

# Ultrasonic Detection Generator

## Ports

### Input

### **Actors** — Scenario actor poses Simulink bus containing MATLAB® structure

Scenario actor poses in ego vehicle coordinates, specified as a Simulink bus containing a MATLAB structure.

The structure must contain these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumActors` | Number of actors | Nonnegative integer |
| `Time` | Current simulation time | Real-valued scalar |
| `Actors` | Actor poses | `NumActors`-length array of actor pose structures |

Each actor pose structure in `Actors` must contain these
fields.

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
### Output

### **Detections** — Object detections Simulink bus containing MATLAB structure

Object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).

You can pass object detections from these sensors and other sensors to a tracker,
such as a Multi-Object
Tracker block, and generate tracks.

The structure must contain these fields.

| Property | Description |
| --- | --- |
| `Time` | Measurement time |
| `Measurement` | Distance measurement to the closest object |
| `MeasurementNoise` | Measurement noise covariance matrix |
| `SensorIndex` | Unique ID of the sensor |
| `ObjectClassID` | Object classification |
| `ObjectAttributes` | Additional information passed to tracker |
| `MeasurementParameters` | Parameters used by initialization functions of nonlinear Kalman tracking filters |

This table describes the additional information in the
`ObjectAttributes` property.

**`ObjectAttributes`**

| Attribute | Definition |
| --- | --- |
| `TargetIndex` | Identifier of the actor, `ActorID`, that generated the detection. For false alarms, this value is negative. |
| `PointOnTarget` | Coordinate of the point on the detected object that the sensor used to compute the distance measurement. It is in the vehicle coordinate system. Use this for visualizing detections in the Bird's-Eye Scope app. |

For `MeasurementParameters`, the measurements are relative to
the parent frame. The parent frame is the ego vehicle body.

**`MeasurementParameters`**

| Parameter | Definition |
| --- | --- |
| `Frame` | Enumerated type indicating the frame used to report measurements. The `Frame` is always set to `'spherical'` and the detections are reported in spherical coordinates for Ultrasonic Detection Generator. |
| `OriginPosition` | 3-D vector offset of the sensor origin from the parent frame origin. |
| `OriginVelocity` | Velocity of the sensor coordinate system with respect to the parent frame. |
| `IsParentToChild` | Logical scalar indicating if `Orientation` performs a frame rotation from the parent coordinate frame to the child coordinate frame. When `IsParentToChild` is false, then `Orientation` performs a frame rotation from the child coordinate frame to the parent coordinate frame. |
| `HasAzimuth` | Indicates whether measurements contain azimuth components. |
| `HasRange` | Indicates whether measurements contain range components. Always `true` for Ultrasonic Detection Generator. |
| `HasElevation` | Indicates whether measurements contain elevation components. Always `false` for Ultrasonic Detection Generator. |
| `HasVelocity` | Indicates whether measurements contain velocity or range rate components. Always `false` for Ultrasonic Detection Generator. |
| `FieldOfView` | 2-D vector containing the azimuth and elevation field of view values of the sensor. |

## Parameters

### Parameters

#### Sensor Identification

### **Unique identifier of sensor** — Unique sensor identifier `0` (default) | positive integer

Specify the unique sensor identifier as a positive integer. Use this parameter to
distinguish between detections or tracks that come from different sensors in a
multisensor system. Specify a unique value for each sensor. If you do not update
**Unique identifier of sensor** from the default value of
`0`, then the radar returns an error at the start of
simulation.

#### Sensor Mounting

### **Translation [ X, Y, Z ] relative to ego origin (m)** — Sensor location on ego vehicle (m) `[3.4, 0, 0.2]` (default) | 1-by-3 real-valued vector of form [*x* *y* *z*]

Specify the sensor location on the ego vehicle body frame in meters as a 1-by-3
real-valued vector of the form [*x*
*y*
*z*]. This parameter defines the coordinates of the sensor along the
*x*-axis, *y*-axis, and *z*-axis
relative to the ego vehicle origin, where:

- The *x*-axis points forward from the vehicle.
- The *y*-axis points to the left of the vehicle.
- The *z*-axis points up from the ground.

The default value corresponds to a radar that is mounted at the center of the
front grill of a sedan.

For more details on the ego vehicle coordinate system, see Coordinate Systems in Automated Driving Toolbox.

### **Rotation [Yaw, Pitch, Roll] relative to ego's frame (deg)** — Mounting rotation angles of radar `[0 0 0]` (default) | 1-by-3 real-valued vector of form [*z*yaw *y*pitch *x*roll]

Specify the mounting rotation angles of the radar in degrees as a 1-by-3
real-valued vector of form [*z*yaw
*y*pitch
*x*roll]. This parameter defines the intrinsic
Euler angle rotation of the sensor around the *z*-axis,
*y*-axis, and *x*-axis with respect to the ego
vehicle body frame, where:

- *z*yaw, or *yaw
  angle*, rotates the sensor around the *z*-axis of
  the ego vehicle.
- *y*pitch, or *pitch
  angle*, rotates the sensor around the *y*-axis of
  the ego vehicle. This rotation is relative to the sensor position that results
  from the *z*yaw rotation.
- *x*roll, or *roll
  angle*, rotates the sensor about the *x*-axis of the
  ego vehicle. This rotation is relative to the sensor position that results from
  the *z*yaw and
  *y*pitch rotations.

These angles are clockwise-positive when looking in the forward direction of the
*z*-axis, *y*-axis, and
*x*-axis, respectively. If you visualize sensor data from a
bird's-eye view perspective, then the yaw angle is counterclockwise-positive because
you are viewing the data in the negative direction of the *z*-axis, which points up from the ground.

For more details on this coordinate system, see Coordinate Systems in Automated Driving Toolbox.

#### Sensor Configuration

### **Field of view [horizontalFOV, verticalFOV] (deg)** — Angular field of view of ultrasonic sensor `[70 35]` (default) | 1-by-2 positive real-valued vector of form `[horizontalFOV verticalFOV]`

Angular field of view of the ultrasonic sensor, specified as a 1-by-2 positive
real-valued vector of the form `[horizontalFOV verticalFOV]`. The
field of view defines the total angular extent spanned by the sensor. You must specify
the horizontal field of view `horizontalFOV` in the range (0, 360],
and the elevation field of view `verticalFOV` in the range (0, 180].
The range of vertical field of view is narrow to avoid detections from the ground.
Units are in degrees.

### **Detection ranges [minDetOnlyRange, minDistRange, maxDistRange] (m)** — Detection range vector of ultrasonic sensor (m) `[0.03 0.15 5.5]` (default) | 1-by-3 nonnegative real-valued vector of form `[minDetOnlyRange minDistRange maxDistRange]`

Detection range vector of the ultrasonic sensor, specified as a 1-by-3 nonnegative
real-valued vector of the form `[minDetOnlyRange minDistRange
maxDistRange]`, where `minDetOnlyRange < minDistRange <
maxDistRange`. Units are in meters. These values determine the detections
and distance values returned by the ultrasonic sensor.

- When the detected object is at a distance between
  `minDistRange` and `maxDistRange`, the
  sensor returns a positive distance value.
- When the detected object is at a distance between
  `minDetOnlyRange` and `minDistRange`, the
  sensor detects the object, but cannot determine the distance and returns a value
  of `0`.
- When the object is at a distance below `minDetOnlyRange` or
  above `maxDistRange`, the sensor returns an empty cell
  array.

### **Update rate (Hz)** — Sensor update rate `10` (default) | positive real scalar

Specify the sensor update rate in hertz as a positive real scalar. The reciprocal
of the update rate must be an integer multiple of the simulation time interval. The
radar generates new reports at intervals defined by this reciprocal value. Any sensor
update requested between update intervals contains no detections or tracks.

#### Port Settings

### **Source of output bus name** — Source of output bus name `Auto` (default) | `Property`

Source of output bus name, specified as one of these options:

- `Auto` — The block automatically creates a bus
  name.
- `Property` — Specify the bus name by using the
  **Specify an output bus name** parameter.

### **Specify an output bus name** — Name of output bus `BusDrivingRadarDataGenerator` (default) | valid bus name

Specify the name of the actor poses bus returned in the
**Actors** output port.

To enable this parameter, set the **Source of output bus name**
parameter to `Property`.

### Actor Profiles

### **Target profiles definition** — Method to specify target profiles `Parameters` (default) | `MATLAB expression` | `From Scenario Reader block`

Specify the method to specify target profiles, which are the physical and radar
characteristics of all targets in the driving scenario, as one of these options:

- `Parameters` — The block obtains the target
  profiles from the parameters enabled on the **Target Profiles**
  tab when you select this option.
- `MATLAB expression` — The block obtains the actor
  profiles from the MATLAB expression specified by the **MATLAB expression for target
  profiles** parameter.
- `From Scenario Reader block` — The block obtains
  the actor profiles from the scenario specified by the Scenario
  Reader block or RoadRunner
  Scenario Reader block.

### **MATLAB expression for target profiles** — MATLAB expression for target profiles MATLAB structure | MATLAB structure array | valid MATLAB expression

Specify the MATLAB expression for actor profiles, as a MATLAB structure, a MATLAB structure array, or a valid MATLAB expression that produces such a structure or structure array.

If your Scenario Reader block reads data from a `drivingScenario` object, to obtain the actor profiles directly from this
object, set this expression to call the `actorProfiles` function on the object. For example:
`actorProfiles(scenario)`.

The default target profile expression produces a MATLAB structure and has this form:

```
struct('ClassID',0,'Length',4.7,'Width',1.8,'Height',1.4, ...
'OriginOffset',[-1.35 0 0],'RCSPattern',[10 10;10 10], ...
'RCSAzimuthAngles',[-180 180],'RCSElevationAngles',[-90 90])
```

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `MATLAB
expression`.

### **Unique identifier for actors** — Scenario-defined actor identifier `[]` (default) | positive integer | length-*L* vector of unique positive integers

Specify the scenario-defined actor identifier as a positive integer or
length-*L* vector of unique positive integers. *L*
must equal the number of actors input into the **Actors** input port.
The vector elements must match `ActorID` values of the actors. You
can specify **Unique identifier for actors** as
`[]`. In this case, the same actor profile parameters apply to all
actors.

**Example:** `[1 2]`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **User-defined integer to classify actors** — User-defined classification identifier `0` (default) | integer | length-*L* vector of integers

Specify the user-defined classification identifier as an integer or
length-*L* vector of integers. When **Unique identifier for
actors** is a vector, this parameter is a vector of the same length with
elements in one-to-one correspondence to the actors in **Unique identifier for
actors**. When **Unique identifier for actors** is empty,
`[]`, you must specify this parameter as a single integer whose
value applies to all actors.

**Example:** `2`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Length of actors' cuboids (m)** — Length of actor cuboids `4.7` (default) | positive real scalar | length-*L* vector of positive values

Specify the length of actor cuboids as a positive real scalar or
length-*L* vector of positive values. When **Unique
identifier for actors** is a vector, this parameter is a vector of the same
length with elements in one-to-one correspondence to the actors in **Unique
identifier for actors**. When **Unique identifier for
actors** is empty, `[]`, you must specify this parameter
as a positive real scalar whose value applies to all actors. Units are in
meters.

**Example:** `6.3`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Width of actors' cuboids (m)** — Width of actor cuboids `1.8` (default) | positive real scalar | length-*L* vector of positive values

Specify the width of actor cuboids as a positive real scalar or
length-*L* vector of positive values. When **Unique
identifier for actors** is a vector, this parameter is a vector of the same
length with elements in one-to-one correspondence to the actors in **Unique
identifier for actors**. When **Unique identifier for
actors** is empty, `[]`, you must specify this parameter
as a positive real scalar whose value applies to all actors. Units are in
meters.

**Example:** `4.7`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Height of actors' cuboids (m)** — Height of actor cuboids `1.4` (default) | positive real scalar | length-*L* vector of positive values

Specify the height of actor cuboids as a positive real scalar or
length-*L* vector of positive values. When **Unique
identifier for actors** is a vector, this parameter is a vector of the same
length with elements in one-to-one correspondence to the actors in **Unique
identifier for actors**. When **Unique identifier for
actors** is empty, `[]`, you must specify this parameter
as a positive real scalar whose value applies to all actors. Units are in
meters.

**Example:** `2.0`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Rotational center of actors from bottom center (m)** — Rotational center of actors `{[-1.35, 0, 0]}` (default) | length-*L* cell array of real-valued 1-by-3 vectors

Specify the rotational center of actors as a length-*L* cell
array of real-valued 1-by-3 vectors. Each vector represents the offset of the
rotational center of an actor from the bottom-center of the actor. For vehicles, the
offset corresponds to the point on the ground beneath the center of the rear axle.
When **Unique identifier for actors** is a vector, this parameter is
a cell array of vectors with cells in one-to-one correspondence to the actors in
**Unique identifier for actors**. When **Unique identifier
for actors** is empty, `[]`, you must specify this
parameter as a cell array of one element containing an offset vector whose values
apply to all actors. Units are in meters.

**Example:** `{[-1.35, 0.2, 0.3]}`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

## Libraries

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Generate ultrasonic sensor detections from driving scenario or RoadRunner Scenario

The Ultrasonic Detection Generator block generates detection of targets
from an ultrasonic sensor mounted on the ego vehicle. Use this block to generate sensor data
from a driving scenario containing actors and trajectories, which you can read from a Scenario Reader
block.

At intervals equal to the sensor update interval, the block outputs distance from the
sensor to the closest point of the detected target. This block also provides parameters to
specify dimensions and properties of the objects in the scenario. For visualization of
ultrasonic detections using the Bird's-Eye Scope app,
this block also outputs the 3-D coordinate of the closest point on the detected object.

You can use the block with vehicle actors in Driving Scenario and RoadRunner Scenario simulations.

You can use the Ultrasonic Detection Generator to create input to a Multi-Object
Tracker block. When building scenarios and sensor models using the Driving Scenario
Designer app, the ultrasonic sensors exported to Simulink® are output as Ultrasonic Detection Generator blocks.
