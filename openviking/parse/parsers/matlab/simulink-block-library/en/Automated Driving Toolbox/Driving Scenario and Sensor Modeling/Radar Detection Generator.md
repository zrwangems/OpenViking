---
type: simulink-block
title: 'Radar Detection Generator'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'radardetectiongenerator'
documentation_source_path: 'ref/radardetectiongenerator.html'
language: en
---

# Radar Detection Generator

## Ports

### Input

### **Actors** — Scenario actor poses Simulink bus containing MATLAB® structure

Scenario actor poses in ego vehicle coordinates, specified as a
Simulink bus containing a MATLAB structure.

The structure must contain these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumActors` | Number of actors | Nonnegative integer |
| `Time` | Current simulation time | Real-valued scalar |
| `Actors` | Actor poses | `NumActors`-length array of actor pose structures |

Each actor pose structure in `Actors` must contain
these fields.

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

### **Detections** — Detections Simulink bus containing MATLAB structure

Object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).

You can pass object detections from these sensors and other sensors to
a tracker, such as a Multi-Object Tracker block, and generate tracks.

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures of length set by the **Maximum number of reported detections** parameter. Only `NumDetections` of these are actual detections. |

Each object detection structure contains these properties.

| Property | Definition |
| --- | --- |
| `Time` | Measurement time |
| `Measurement` | Object measurements |
| `MeasurementNoise` | Measurement noise covariance matrix |
| `SensorIndex` | Unique ID of the sensor |
| `ObjectClassID` | Object classification |
| `MeasurementParameters` | Parameters used by initialization functions of nonlinear Kalman tracking filters |
| `ObjectAttributes` | Additional information passed to tracker |

- For Cartesian coordinates,
  `Measurement` and
  `MeasurementNoise` are reported in
  the coordinate system specified by the **Coordinate
  system used to report detections** parameter.
- For spherical coordinates,
  `Measurement` and
  `MeasurementNoise` are reported in
  the spherical coordinate system based on the sensor
  Cartesian coordinate system.

**Measurement and Measurement Noise**

| **Coordinate System Used to Report Detections** | Measurement and Measurement Noise Coordinates |
| --- | --- |
| `'Ego Cartesian'` | **Coordinate dependence on **Enable range rate measurements****  | **Enable range rate measurements** | Coordinates | | --- | --- | | true | `[x;y;z;vx;vy;vz]` | | false | `[x;y;z]` | |
| `'Sensor Cartesian'` |
| `'Sensor spherical'` | **Coordinate dependence on **Enable elevation angle measurements** and **Enable range rate measurements****  | **Enable range rate measurements** | **Enable elevation angle measurements** | Coordinates | | --- | --- | --- | | true | true | `[az;el;rng;rr]` | | true | false | `[az;rng;rr]` | | false | true | `[az;el;rng]` | | false | false | `[az;rng]` | |

**`MeasurementParameters`**

| Parameter | Definition |
| --- | --- |
| `Frame` | Enumerated type indicating the frame used to report measurements. When `Frame` is set to `'rectangular'`, detections are reported in Cartesian coordinates. When `Frame` is set `'spherical'`, detections are reported in spherical coordinates. |
| `OriginPosition` | 3-D vector offset of the sensor origin from the ego vehicle origin. The vector is derived from the `SensorLocation` and `Height` properties specified in the `radarDetectionGenerator`. |
| `Orientation` | Orientation of the radar sensor coordinate system with respect to the ego vehicle coordinate system. The orientation is derived from the `Yaw`, `Pitch`, and `Roll` properties of the `radarDetectionGenerator`. |
| `HasVelocity` | Indicates whether measurements contain velocity or range rate components. |
| `HasElevation` | Indicates whether measurements contain elevation components. |

The `ObjectAttributes` property of each detection
is a structure with these fields.

| Field | Definition |
| --- | --- |
| `TargetIndex` | Identifier of the actor, `ActorID`, that generated the detection. For false alarms, this value is negative. |
| `SNR` | Signal-to-noise ratio of the detection. Units are in dB. |

## Parameters

### Parameters

#### Sensor Identification

### **Unique identifier of sensor** — Unique sensor identifier 1 (default) | positive integer

Unique sensor identifier, specified as a positive integer. The sensor
identifier distinguishes detections that come from different sensors in
a multisensor system. If a model contains multiple sensor blocks with
the same sensor identifier, the Bird's-Eye Scope displays an
error.

**Example:** `5`

### **Required interval between sensor updates (s)** — Required time interval `0.1` (default) | positive real scalar

Required time interval between sensor updates, specified as a positive
real scalar. The value of this parameter must be an integer multiple of
the **Actors** input port data interval. Updates
requested from the sensor between update intervals contain no
detections. Units are in seconds.

#### Sensor Extrinsics

### **Sensor's (x,y) position (m)** — Location of the radar sensor center `[3.4 0]` (default) | real-valued 1-by-2 vector

Location of the radar sensor center, specified as a real-valued 1-by-2
vector. The **Sensor's (x,y) position (m)** and
**Sensor's height (m)** parameters define the
coordinates of the radar sensor with respect to the ego vehicle
coordinate system. The default value corresponds to a radar mounted at
the center of the front grill of a sedan. Units are in meters.

### **Sensor's height (m)** — Radar sensor height above the ground plane `0.2` (default) | positive real scalar

Radar sensor height above the ground plane, specified as a positive
real scalar. The height is defined with respect to the vehicle ground
plane. The **Sensor's (x,y) position (m)** and
**Sensor's height (m)** parameters define the
coordinates of the radar sensor with respect to the ego vehicle
coordinate system. The default value corresponds to a radar mounted at
the center of the front grill of a sedan. Units are in meters.

**Example:** `0.25`

### **Yaw angle of sensor mounted on ego vehicle (deg)** — Yaw angle of sensor `0` (default) | real scalar

Yaw angle of radar sensor, specified as a real scalar. Yaw angle is
the angle between the center line of the ego vehicle and the downrange
axis of the radar sensor. A positive yaw angle corresponds to a
clockwise rotation when looking in the positive direction of the
*z*-axis of the ego vehicle coordinate system.
Units are in degrees.

**Example:** `-4.0`

### **Pitch angle of sensor mounted on ego vehicle (deg)** — Pitch angle of sensor `0` (default) | real scalar

Pitch angle of sensor, specified as a real scalar. The pitch angle is
the angle between the downrange axis of the radar sensor and the
*x-y* plane of the ego vehicle coordinate system. A
positive pitch angle corresponds to a clockwise rotation when looking in
the positive direction of the *y*-axis of the ego
vehicle coordinate system. Units are in degrees.

**Example:** `3.0`

### **Roll angle of sensor mounted on ego vehicle (deg)** — Roll angle of sensor `0` (default) | real scalar

Roll angle of the radar sensor, specified as a real scalar. The roll
angle is the angle of rotation of the downrange axis of the radar around
the *x*-axis of the ego vehicle coordinate system. A
positive roll angle corresponds to a clockwise rotation when looking in
the positive direction of the *x*-axis of the
coordinate system. Units are in degrees.

#### Port Settings

### **Source of output bus name** — Source of output bus name `Auto` (default) | `Property`

Source of output bus name, specified as `Auto` or
`Property`. If you choose `Auto`,
the block will automatically create a bus name. If you choose
`Property`, specify the bus name using the
**Specify an output bus name** parameter.

**Example:** `Property`

### **Specify an output bus name** — Name of output bus no default

Name of output bus.

#### Dependencies

To enable this parameter, set the **Source of output bus
name** parameter to `Property`.

#### Detection Reporting

### **Maximum number of reported detections** — Maximum number of reported detections `50` (default) | positive integer

Maximum number of detections reported by the sensor, specified as a
positive integer. Detections are reported in order of increasing
distance from the sensor until the maximum number is reached.

**Example:** `100`

### **Coordinate system used to report detections** — Coordinate system of reported detections `Ego Cartesian` (default) | `Sensor Cartesian` | `Sensor Spherical`

Coordinate system of reported detections, specified as one of these values:

- `Ego Cartesian` —
  Detections are reported in the ego vehicle Cartesian
  coordinate system.
- `Sensor Cartesian`—
  Detections are reported in the sensor Cartesian coordinate
  system.
- `Sensor spherical` —
  Detections are reported in a spherical coordinate system.
  This coordinate system is centered at the radar and aligned
  with the orientation of the radar on the ego vehicle.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB interpreter. This option shortens startup time. In `Interpreted
  execution` mode, you can debug the source code of the block.
- `Code generation` — Simulate the model using generated C/C++
  code. The first time you run a simulation, Simulink generates C/C++ code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional startup
  time.

### Measurements

#### Accuracy Settings

### **Azimuthal resolution of radar (deg)** — Azimuth resolution of radar `4.0` (default) | positive real scalar

Azimuth resolution of the radar, specified as a positive real scalar.
The azimuth resolution defines the minimum separation in azimuth angle
at which the radar can distinguish two targets. The azimuth resolution
is typically the 3dB-downpoint in azimuth angle beamwidth of the radar.
Units are in degrees.

**Example:** `6.5`

### **Elevation resolution of radar (deg)** — Elevation resolution of radar `10.0` (default) | positive real scalar

Elevation resolution of the radar, specified as a positive real
scalar. The elevation resolution defines the minimum separation in
elevation angle at which the radar can distinguish two targets. The
elevation resolution is typically the 3dB-downpoint in elevation angle
beamwidth of the radar. Units are in degrees.

**Example:** `3.5`

#### Dependencies

To enable this parameter, select the **Enable elevation
angle measurements** check box.

### **Range resolution of radar (m)** — Range resolution of radar `2.5` (default) | positive real scalar

Range resolution of the radar, specified as a positive real scalar.
The range resolution defines the minimum separation in range at which
the radar can distinguish between two targets. Units are in
meters.

**Example:** `5.0`

### **Range rate resolution of radar (m/s)** — Range rate resolution of the radar `0.5` (default) | positive real scalar

Range rate resolution of the radar, specified as a positive real
scalar. The range rate resolution defines the minimum separation in
range rate at which the radar can distinguish between two targets. Units
are in meters per second.

**Example:** `0.75`

#### Dependencies

To enable this parameter, select the **Enable range rate
measurements** check box.

#### Bias Settings

### **Fractional azimuthal bias component of radar** — Azimuth bias fraction `0.1` (default) | nonnegative real scalar

Azimuth bias fraction of the radar, specified as a nonnegative real
scalar. The azimuth bias is expressed as a fraction of the azimuth
resolution specified in the **Azimuthal resolution of radar
(deg)** parameter. Units are dimensionless.

**Example:** 0.3

### **Fractional elevation bias component of radar** — Elevation bias fraction `0.1` (default) | nonnegative real scalar

Elevation bias fraction of the radar, specified as a nonnegative real
scalar. The elevation bias is expressed as a fraction of the elevation
resolution specified in the **Elevation resolution of radar
(deg)** parameter. Units are dimensionless.

**Example:** 0.2

#### Dependencies

To enable this parameter, select the **Enable elevation
angle measurements** check box.

### **Fractional range bias component of radar** — Range bias fraction `0.05` (default) | nonnegative real scalar

Range bias fraction of the radar, specified as a nonnegative real
scalar. Range bias is expressed as a fraction of the range resolution
specified in the **Range resolution of radar (m)**
parameter. Units are dimensionless.

**Example:** `0.15`

### **Fractional range rate bias component of radar** — Range rate bias fraction of the radar `0.05` (default) | nonnegative real scalar

Range rate bias fraction of the radar, specified as a nonnegative real
scalar. Range rate bias is expressed as a fraction of the range rate
resolution specified in **Range rate resolution of radar
(m)** parameter. Units are dimensionless.

**Example:** `0.2`

#### Dependencies

To enable this parameter, select the **Enable range rate
measurements** check box.

#### Detector Settings

### **Total angular field of view for radar (deg)** — Field of view of radar sensor `[20 5]` (default) | real-valued 1-by-2 vector of positive values

Field of view of radar sensor, specified as a real-valued 1-by-2
vector of positive values, `[azfov elfov]`. The field
of view defines the angular extent spanned by the sensor. Each component
must lie in the interval (0,180]. Targets outside of the field of view
of the radar are not detected. Units are in degrees.

**Example:** `[14 7]`

### **Maximum detection range (m)** — Maximum detection range `150` (default) | positive real scalar

Maximum detection range, specified as a positive real scalar. The
radar cannot detect a target beyond this range. Units are in
meters.

**Example:** `250`

### **Minimum and maximum range rates that can be reported** — Minimum and maximum detection range rates `[-100 100]` (default) | real-valued 1-by-2 vector

Minimum and maximum detection range rates, specified as a real-valued
1-by-2 vector. The radar cannot detect a target outside of this range
rate interval. Units are in meters per second.

**Example:** `[-200 200]`

#### Dependencies

To enable this parameter, select the **Enable range rate
measurements** check box.

### **Detection probability** — Probability of detecting a target `0.9` (default) | positive real scalar less than or equal to 1

Probability of detecting a target, specified as a positive real scalar
less than or equal to one. This quantity defines the probability of
detecting target that has a radar cross-section specified by the
**Radar cross section at which detection probability is
achieved (dBsm)** parameter at the reference detection
range specified by the **Range where detection probability is
achieved (m)** parameter.

**Example:** `0.95`

### **Rate at which false alarms are reported** — False alarm rate `1e-6` (default) | positive real scalar

False alarm rate within a radar resolution cell, specified as a
positive real scalar in the range [10–7,
10–3]. Units are dimensionless.

**Example:** `1e-5`

### **Range where detection probability is achieved (m):** — Reference range for given probability of detection `100` (default) | positive real scalar

Reference range for a given probability of detection, specified as a
positive real scalar. The reference range is the range when a target
having a radar cross-section specified by **Radar cross section
at which detection probability is achieved (dBsm)** is
detected with a probability of specified by **Detection
probability**. Units are in meters.

**Example:** `150`

### **Radar cross section at which detection probability is achieved (dBsm)** — Reference radar cross-section for given probability of detection `0.0` (default) | nonnegative real scalar

Reference radar cross-section (RCS) for given probability of
detection, specified as a nonnegative real scalar. The reference RCS is
the value at which a target is detected with probability specified by
**Detection probability**. Units are in
dBsm.

**Example:** `2.0`

#### Measurement Settings

### **Enable elevation angle measurements** — Enable radar to measure elevation `off` (default) | `on`

Select this check box to model a radar that can measure target
elevation angles.

### **Enable range rate measurements** — Enable radar to measure range rate `on` (default) | `off` | `on`

Select this check box to model a radar that can measure target range
rate.

### **Add noise to measurements** — Enable adding noise to radar sensor measurements `on` (default) | `off`

Select this check box to add noise to radar sensor measurements.
Otherwise, the measurements are noise-free. The
`MeasurementNoise` property of each detection is
always computed and is not affected by the value you specify for the
**Add noise to measurements** parameter. By leaving
this check box `off`, you can pass the sensor's ground
truth measurements into a Multi-Object Tracker block.

### **Enable false detections** — Enable creating false alarm radar detections `on` (default) | `off`

Select this check box to enable reporting false alarm radar
measurements. Otherwise, only actual detections are reported.

### **Enable occlusion** — Enable line-of-sight occlusion `on` (default) | `off`

Select this parameter to enable line-of-sight occlusion, where the
radar generates detections only from objects with a direct line of
sight.

#### Random Number Generator Settings

### **Select method to specify initial seed** — Method to specify random number generator seed `Repeatable` (default) | `Specify seed` | `Not repeatable`

Method to set the random number generator seed, specified as one of
the options in the table.

| Option | Description |
| --- | --- |
| `Repeatable` | The block generates a random initial seed for the first simulation and reuses this seed for all subsequent simulations. Select this parameter to generate repeatable results from the statistical sensor model. To change this initial seed, at the MATLAB command prompt, enter: `clear all`. |
| `Specify seed` | Specify your own random initial seed for reproducible results by using the **Specify seed** parameter. |
| `Not repeatable` | The block generates a new random initial seed after each simulation run. Select this parameter to generate nonrepeatable results from the statistical sensor model. |

### **Initial seed** — Random number generator seed `0` (default) | nonnegative integer less than 232

Random number generator seed, specified as a nonnegative integer less
than 232.

**Example:** `2001`

#### Dependencies

To enable this parameter, set the `Random Number
Generator Settings` parameter to `Specify
seed`.

### Actor Profiles

### **Select method to specify actor profiles** — Method to specify actor profiles `From Scenario Reader block` (default) | `Parameters` | `MATLAB expression`

Method to specify actor profiles, which are the physical and radar characteristics of all actors in the driving scenario, specified as one of these options:

- `From Scenario Reader block` — The block obtains
  the actor profiles from the scenario specified by the Scenario Reader block or RoadRunner Scenario Reader block.
- `Parameters` — The block obtains the actor profiles from the parameters that become enabled on the **Actor Profiles** tab.
- `MATLAB expression` — The block obtains the actor
  profiles from the MATLAB expression specified by the **MATLAB expression for
  actor profiles** parameter.

### **MATLAB expression for actor profiles** — MATLAB expression for actor profiles `struct('ClassID',0,'Length',4.7,'Width',1.8,'Height',1.4,'OriginOffset',[-1.35,0,0])` (default) | MATLAB structure | MATLAB structure array | valid MATLAB expression

MATLAB expression for actor profiles, specified as a MATLAB structure, a MATLAB structure array, or a valid MATLAB expression that produces such a structure or structure array.

If your Scenario Reader block reads data from a `drivingScenario` object, to obtain the actor profiles directly from this
object, set this expression to call the `actorProfiles` function on the object. For example:
`actorProfiles(scenario)`.

**Example:** `struct('ClassID',5,'Length',5.0,'Width',2,'Height',2,'OriginOffset',[-1.55,0,0])`

#### Dependencies

To enable this parameter, set the **Select method to specify actor profiles** parameter to `MATLAB expression`.

### **Unique identifier for actors** — Scenario-defined actor identifier `[]` (default) | positive integer | length-*L* vector of unique positive integers

Scenario-defined actor identifier, specified as a positive integer or
length-*L* vector of unique positive integers.
*L* must equal the number of actors input into the
**Actor** input port. The vector elements must
match `ActorID` values of the actors. You can specify
**Unique identifier for actors** as
`[]`. In this case, the same actor profile
parameters apply to all actors.

**Example:** `[1,2]`

#### Dependencies

To enable this parameter, set the **Select method to
specify actor profiles** parameter to
`Parameters`.

### **User-defined integer to classify actors** — User-defined classification identifier `0` (default) | integer | length-*L* vector of integers

User-defined classification identifier, specified as an integer or
length-*L* vector of integers. When
**Unique identifier for actors** is a vector, this
parameter is a vector of the same length with elements in one-to-one
correspondence to the actors in **Unique identifier for
actors**. When **Unique identifier for
actors** is empty, `[]`, you must specify
this parameter as a single integer whose value applies to all
actors.

**Example:** `2`

#### Dependencies

To enable this parameter, set the **Select method to
specify actor profiles** parameter to
`Parameters`.

### **Length of actors cuboids (m)** — Length of cuboid `4.7` (default) | positive real scalar | length-*L* vector of positive values

Length of cuboid, specified as a positive real scalar or
length-*L* vector of positive values. When
**Unique identifier for actors** is a vector, this
parameter is a vector of the same length with elements in one-to-one
correspondence to the actors in **Unique identifier for
actors**. When **Unique identifier for
actors** is empty, `[]`, you must specify
this parameter as a positive real scalar whose value applies to all
actors. Units are in meters.

**Example:** 6.3

#### Dependencies

To enable this parameter, set the **Select method to
specify actor profiles** parameter to
`Parameters`.

### **Width of actors cuboids (m)** — Width of cuboid `4.7` (default) | positive real scalar | length-*L* vector of positive values

Width of cuboid, specified as a positive real scalar or
length-*L* vector of positive values. When
**Unique identifier for actors** is a vector, this
parameter is a vector of the same length with elements in one-to-one
correspondence to the actors in **Unique identifier for
actors**. When **Unique identifier for
actors** is empty, `[]`, you must specify
this parameter as a positive real scalar whose value applies to all
actors. Units are in meters.

**Example:** 4.7

#### Dependencies

To enable this parameter, set the **Select method to
specify actor profiles** parameter to
`Parameters`.

### **Height of actors cuboids (m)** — Height of cuboid `4.7` (default) | positive real scalar | length-*L* vector of positive values

Height of cuboid, specified as a positive real scalar or
length-*L* vector of positive values. When
**Unique identifier for actors** is a vector, this
parameter is a vector of the same length with elements in one-to-one
correspondence to the actors in **Unique identifier for
actors**. When **Unique identifier for
actors** is empty, `[]`, you must specify
this parameter as a positive real scalar whose value applies to all
actors. Units are in meters.

**Example:** `2.0`

#### Dependencies

To enable this parameter, set the **Select method to
specify actor profiles** parameter to
`Parameters`.

### **Rotational center of actors from bottom center (m)** — Rotational center of the actor { [ -1.35, 0, 0 ] } (default) | length-*L* cell array of real-valued 1-by-3 vectors

Rotational center of the actor, specified as a
length-*L* cell array of real-valued 1-by-3
vectors. Each vector represents the offset of the rotational center of
the actor from the bottom-center of the actor. For vehicles, the offset
corresponds to the point on the ground beneath the center of the rear
axle. When **Unique identifier for actors** is a
vector, this parameter is a cell array of vectors with cells in
one-to-one correspondence to the actors in **Unique identifier
for actors**. When **Unique identifier for
actors** is empty, `[]`, you must specify
this parameter as a cell array of one element containing the offset
vector whose values apply to all actors. Units are in meters.

**Example:** [ -1.35, .2, .3 ]

#### Dependencies

To enable this parameter, set the **Select method to
specify actor profiles** parameter to
`Parameters`.

### **Radar cross section pattern (dBsm)** — Radar cross-section `{[10,10;10,10]}` (default) | real-valued *Q*-by-*P* matrix | length-*L* cell array of real-valued *Q*-by-*P* matrices

Radar cross-section (RCS) of actor, specified as a real-valued
*Q*-by-*P* matrix or
length-*L* cell array of real-valued
*Q*-by-*P* matrices.
*Q* is the number of elevation angles specified by
the corresponding cell in the **Elevation angles defining
RCSPattern (deg)** parameter. *P* is the
number of azimuth angles specified by the corresponding cell in
**Azimuth angles defining RCSPattern (deg)**
property. When **Unique identifier for actors** is a
vector, this parameter is a cell array of matrices with cells in
one-to-one correspondence to the actors in **Unique identifier
for actors**. *Q* and *P*
can vary in the cell array. When **Unique identifier for
actors** is empty, `[]`, you must specify
this parameter as a cell array with one element containing a matrix
whose values apply to all actors. Units are in dBsm.

**Example:** [10 14 10; 9 13 9]

#### Dependencies

To enable this parameter, set the **Select method to
specify actor profiles** parameter to
`Parameters`.

### **Azimuth angles defining RCSPattern (deg)** — Azimuth angles of radar cross-section pattern `{[-180 180]}` (default) | length-*L* cell array of real-valued *P*-length vectors

Azimuth angles of radar cross-section pattern, specified as a
length-*L* cell array of real-valued
*P*-length vectors. Each vector represents the
azimuth angles of the *P*-columns of the radar cross
section specified in **Radar cross section pattern
(dBsm)**. When **Unique identifier for
actors** is a vector, this parameter is a cell array of
vectors with cells in one-to-one correspondence to the actors in
**Unique identifier for actors**.
*P* can vary in the cell array. When
**Unique identifier for actors** is empty,
`[]`, you must specify this parameter as a cell
array with one element containing a vector whose values apply to all
actors. Units are in degrees. Azimuth angles lie in the range -180° to
180° and must be in strictly increasing order.

When the radar cross sections specified in the cells of
**Radar cross section pattern (dBsm)** all have the
same dimensions, you need only specify a cell array with one element
containing the azimuth angle vector.

**Example:** `[-90:90]`

#### Dependencies

To enable this parameter, set the **Select method to
specify actor profiles** parameter to
`Parameters`.

### **Elevation angles defining RCSPattern (deg)** — Elevation angles of radar cross-section pattern `{[-90 90]}` (default) | length-*L* cell array of real-valued *Q*-length vectors

Elevation angles of radar cross-section pattern, specified as a
length-*L* cell array of real-valued
*Q*-length vectors. Each vector represent the
elevation angles of the *Q*-columns of the radar cross
section specified in **Radar cross section pattern
(dBsm)**. When **Unique identifier for
actors** is a vector, this parameter is a cell array of
vectors with cells in one-to-one correspondence to the actors in
**Unique identifier for actors**.
*Q* can vary in the cell array. When
**Unique identifier for actors** is empty,
`[]`, you must specify this parameter as a cell
array with one element containing a vector whose values apply to all
actors. Units are in degrees. Elevation angles lie in the range -90° to
90° and must be in strictly increasing order.

When the radar cross sections that are specified in the cells of
**Radar cross section pattern (dBsm)** all have the
same dimensions, you need only specify a cell array with one element
containing an elevation angle vector.

**Example:** `[-25:25]`

#### Dependencies

To enable this parameter, set the **Select method to
specify actor profiles** parameter to
`Parameters`.

## Libraries

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

### R2021a: `radarDetectionGenerator` System object and Radar Detection Generator block are not recommended

The `radarDetectionGenerator`
System object™ and Radar Detection Generator block are not recommended
unless you require C/C++ code generation. Instead, use the `drivingRadarDataGenerator`
System object and Driving
Radar Data Generator, respectively. These new radar sensors provide
additional properties for modeling radar sensors, including the ability to generate
tracks and clustered detections.

There are no current plans to remove the `radarDetectionGenerator` System object or Radar Detection Generator block. MATLAB code and Simulink models that use these features will continue to run. You can still import `radarDetectionGenerator` objects into the Driving Scenario Designer app. However, the app updates the parameters of the imported sensor to reflect the parameters of a `drivingRadarDataGenerator` object. In addition, when you export a scenario containing a `radarDetectionGenerator` sensor to MATLAB code or to a Simulink model, the app exports the sensor as a `drivingRadarDataGenerator` object or Driving Radar Data Generator block, respectively.

**Update Code**

In MATLAB code, replace all instances of `radarDetectionGenerator` with `drivingRadarDataGenerator`. In addition, update all `radarDetectionGenerator` properties with their equivalent `drivingRadarDataGenerator` properties, as shown in the table. The properties not listed in the table are either specific only to `drivingRadarDataGenerator` or identical in both objects.

| `radarDetectionGenerator` Properties | Equivalent `drivingRadarDataGenerator` Properties |
| --- | --- |
| `UpdateInterval` | `UpdateRate` |
| `SensorLocation`  `Height` | `MountingLocation` |
| `Yaw`  `Pitch`  `Roll` | `MountingAngles` |
| `MaxRange` | `RangeLimits` |
| `MaxNumDetectionsSource` | `MaxNumReportsSource` |
| `MaxNumDetections` | `MaxNumReports` |
| `ActorProfiles` | `Profiles` |

This table shows sample code for creating a `drivingRadarDataGenerator` object instead of a `radarDetectionGenerator` object.

| Discouraged Usage | Recommended Replacement |
| --- | --- |
| ```     radar = radarDetectionGenerator( ...         'SensorLocation',[-1 0], ...         'Height',0.2, ...         'Yaw',180, ...         'Pitch',0, ...         'Roll',0, ...         'MaxRange',50); ``` | ```     radar = drivingRadarDataGenerator( ...         'MountingLocation',[-1 0 0.2], ...         'MountingAngles',[180 0 0], ...         'RangeLimits',[0 50]); ``` |

To generate detections from target poses at each simulation time step, replace the `dets = radarDetectionGenerator(targets,time)` syntax with `dets = drivingRadarDataGenerator(targets,time)`.

**Update Models**

In Simulink models, replace all Radar Detection Generator blocks with Driving Radar Data Generator blocks. In the Driving Radar Data Generator blocks, update the parameter values in the same way you would update the `drivingRadarDataGenerator` property values described in the Update Code section.

If your model contains a separate block that clusters detections, you can remove it because the Driving Radar Data Generator block clusters detections by default.

For example, in this model, the Sensor Simulation subsystem outputs concatenated detections from Radar Detection Generator blocks into a separate block that clusters the detections.

A Simulink model with radar detections being input to a detection clustering block

In this model, the Sensor Simulation subsystem outputs concatenated, clustered detections from Driving Radar Data Generator blocks directly into the next part of the model pipeline.

A Simulink model without the detection clustering block

## Description

Create detection objects from radar measurements

The Radar Detection Generator block generates detections from radar
measurements taken by a radar sensor mounted on an ego vehicle. Detections are derived
from simulated actor poses and are generated at intervals equal to the sensor update
interval. By default, detections are referenced to the coordinate system of the ego
vehicle. The generator can simulate real detections with added random noise and also
generate false alarm detections. A statistical model generates the measurement noise,
true detections, and false positives. The random numbers generated by the statistical
model are controlled by random number generator settings on the
**Measurements** tab. You can use the Radar Detection
Generator to create input to a Multi-Object
Tracker block. When building scenarios and sensor models using the Driving Scenario
Designer app, the radar sensors exported to Simulink® are output as Radar Detection Generator blocks.
