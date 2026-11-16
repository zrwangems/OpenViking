---
type: simulink-block
title: 'Driving Radar Data Generator'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Cuboid Scenario Simulation / Scenarios in Simulink'
documentation_page: 'drivingradardatagenerator'
documentation_source_path: 'ref/drivingradardatagenerator.html'
language: en
---

# Driving Radar Data Generator

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

### **Clustered detections** — Clustered object detections Simulink bus containing MATLAB structure

Clustered object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).

With clustered detections, the block outputs a single detection per target,
where each detection is the centroid of the unclustered detections for that
target.

You can pass object detections from these sensors and other sensors to a
tracker, such as a Multi-Object Tracker block, and generate tracks.

The structure contains these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | Nonnegative integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures of length set by the **Maximum number of reported detections** parameter. Only `NumDetections` of these are actual detections. |

Each object detection structure contains these
properties.

| Property | Definition |
| --- | --- |
| `Time` | Measurement time |
| `Measurement` | Object measurements |
| `MeasurementNoise` | Measurement noise covariance matrix |
| `SensorIndex` | Unique ID of the sensor |
| `ObjectClassID` | Object classification |
| `MeasurementParameters` | Parameters used by initialization functions of nonlinear Kalman tracking filters |
| `ObjectAttributes` | Additional information passed to tracker |

- For rectangular coordinates, `Measurement` and
  `MeasurementNoise` are reported in the rectangular coordinate
  system specified by the **Coordinate system** parameter.
- For spherical coordinates, `Measurement` and
  `MeasurementNoise` are reported in the spherical coordinate
  system, which is based on the sensor rectangular coordinate system.

**`Measurement` and `MeasurementNoise`**

| **Coordinate System** | `Measurement` and `MeasurementNoise` Coordinates |
| --- | --- |
| `Body` | This table shows how coordinates are affected by the **Enable range rate measurements** parameter.  | **Enable range rate measurements** | Coordinates | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Sensor rectangular` |
| `Sensor spherical` | This table shows how coordinates are affected by the **Enable elevation angle measurements** and **Enable range rate measurements** parameters.  | **Enable range rate measurements** | **Enable elevation angle measurements** | Coordinates | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` | |

For `ObjectAttributes`, this table describes the additional information
used for tracking.

**`ObjectAttributes`**

| Attribute | Definition |
| --- | --- |
| `TargetIndex` | Identifier of the actor, `ActorID`, that generated the detection. For false alarms, this value is negative. |
| `SNR` | Signal-to-noise ratio of the detection. Units are in dB. |

For `MeasurementParameters`, the measurements are relative to the
parent frame. When you set the **Coordinate system** parameter to
`Body`, the parent frame is the ego vehicle body. When you set
**Coordinate system** to `Sensor rectangular` or
`Sensor spherical`, the parent frame is the sensor.

**`MeasurementParameters`**

| Parameter | Definition |
| --- | --- |
| `Frame` | Enumerated type indicating the frame used to report measurements. When `Frame` is set to `'rectangular'`, detections are reported in Cartesian coordinates. When `Frame` is set to `'spherical'`, detections are reported in spherical coordinates. |
| `OriginPosition` | 3-D vector offset of the sensor origin from the parent frame origin. |
| `Orientation` | Orientation of the radar sensor coordinate system with respect to the parent frame. |
| `HasVelocity` | Indicates whether measurements contain velocity or range rate components. |
| `HasElevation` | Indicates whether measurements contain elevation components. |

#### Dependencies

To enable this port, on the **Parameters** tab, set the
**Target reporting format** parameter to
`Clustered detections`.

### **Tracks** — Object tracks Simulink bus containing MATLAB structure

Object tracks, returned as a Simulink bus containing a MATLAB structure. See Create Nonvirtual Buses (Simulink).

This table shows the structure fields.

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `Tracks` | Array of track structures of a length set by the **Maximum number of tracks** parameter. Only the first `NumTracks` of these are actual tracks. |

This table shows the fields of each track structure.

| Field | Definition |
| --- | --- |
| `TrackID` | Unique track identifier used to distinguish multiple tracks. |
| `BranchID` | Unique track branch identifier used to distinguish multiple track branches. |
| `SourceIndex` | Unique source index used to distinguish tracking sources in a multiple tracker environment. |
| `UpdateTime` | Time at which the track is updated. Units are in seconds. |
| `Age` | Number of times the track was updated. |
| `State` | Value of state vector at the update time. |
| `StateCovariance` | Uncertainty covariance matrix. |
| `ObjectClassID` | Integer value representing the object classification. The value `0` represents an unknown classification. Nonzero classifications apply only to confirmed tracks. |
| `TrackLogic` | Confirmation and deletion logic type. This value is always `'History'` for radar sensors, to indicate history-based logic. |
| `TrackLogicState` | Current state of the track logic type, returned as a 1-by-*K* logical array. *K* is the number of latest track logical states recorded. In the array, `1` denotes a hit and `0` denotes a miss. |
| `IsConfirmed` | Confirmation status. This field is `true` if the track is confirmed to be a real target. |
| `IsCoasted` | Coasting status. This field is `true` if the track is updated without a new detection. |
| `IsSelfReported` | Indicate if the track is reported by the tracker. This field is used in a track fusion environment. It is returned as `true` by default. |
| `ObjectAttributes` | Additional information about the track. |

For more details about these fields, see `objectTrack`.

The block outputs only confirmed tracks, which are tracks to which the block
assigns at least *M* detections during the first
*N* updates after track initialization. To specify the
values *M* and *N*, use the **M and N
for the M-out-of-N confirmation** parameter.

#### Dependencies

To enable this port, on the **Parameters** tab, set the
**Target reporting format** parameter to
`Tracks`.

### **Detections** — Unclustered object detections Simulink bus containing MATLAB structure

Unclustered object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).

With unclustered detections, the block outputs all detections, and a target
can have multiple detections.

You can pass object detections from these sensors and other sensors to a
tracker, such as a Multi-Object Tracker block, and generate tracks.

The structure must contain these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures of length set by the **Maximum number of reported detections** parameter. Only `NumDetections` of these are actual detections. |

Each object detection structure contains these
properties.

| Property | Definition |
| --- | --- |
| `Time` | Measurement time |
| `Measurement` | Object measurements |
| `MeasurementNoise` | Measurement noise covariance matrix |
| `SensorIndex` | Unique ID of the sensor |
| `ObjectClassID` | Object classification |
| `MeasurementParameters` | Parameters used by initialization functions of nonlinear Kalman tracking filters |
| `ObjectAttributes` | Additional information passed to tracker |

- For rectangular coordinates, `Measurement` and
  `MeasurementNoise` are reported in the rectangular coordinate
  system specified by the **Coordinate system** parameter.
- For spherical coordinates, `Measurement` and
  `MeasurementNoise` are reported in the spherical coordinate
  system, which is based on the sensor rectangular coordinate system.

**`Measurement` and `MeasurementNoise`**

| **Coordinate System** | `Measurement` and `MeasurementNoise` Coordinates |
| --- | --- |
| `Body` | This table shows how coordinates are affected by the **Enable range rate measurements** parameter.  | **Enable range rate measurements** | Coordinates | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Sensor rectangular` |
| `Sensor spherical` | This table shows how coordinates are affected by the **Enable elevation angle measurements** and **Enable range rate measurements** parameters.  | **Enable range rate measurements** | **Enable elevation angle measurements** | Coordinates | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` | |

For `ObjectAttributes`, this table describes the additional information
used for tracking.

**`ObjectAttributes`**

| Attribute | Definition |
| --- | --- |
| `TargetIndex` | Identifier of the actor, `ActorID`, that generated the detection. For false alarms, this value is negative. |
| `SNR` | Signal-to-noise ratio of the detection. Units are in dB. |

For `MeasurementParameters`, the measurements are relative to the
parent frame. When you set the **Coordinate system** parameter to
`Body`, the parent frame is the ego vehicle body. When you set
**Coordinate system** to `Sensor rectangular` or
`Sensor spherical`, the parent frame is the sensor.

**`MeasurementParameters`**

| Parameter | Definition |
| --- | --- |
| `Frame` | Enumerated type indicating the frame used to report measurements. When `Frame` is set to `'rectangular'`, detections are reported in Cartesian coordinates. When `Frame` is set to `'spherical'`, detections are reported in spherical coordinates. |
| `OriginPosition` | 3-D vector offset of the sensor origin from the parent frame origin. |
| `Orientation` | Orientation of the radar sensor coordinate system with respect to the parent frame. |
| `HasVelocity` | Indicates whether measurements contain velocity or range rate components. |
| `HasElevation` | Indicates whether measurements contain elevation components. |

#### Dependencies

To enable this port, on the **Parameters** tab, set the
**Target reporting format** parameter to
`Detections`.

## Parameters

### Parameters

#### Sensor Identification

### **Unique identifier of sensor** — Unique sensor identifier `0` (default) | positive integer

Specify the unique sensor identifier as a positive integer. Use this
parameter to distinguish between detections or tracks that come from different
sensors in a multisensor system. Specify a unique value for each sensor. If you
do not update **Unique identifier of sensor** from the default
value of `0`, then the radar returns an error at the start of
simulation.

### **Update rate (Hz)** — Sensor update rate `10` (default) | positive real scalar

Specify the sensor update rate in hertz as a positive real scalar. The
reciprocal of the update rate must be an integer multiple of the simulation
time interval. The radar generates new reports at intervals defined by this
reciprocal value. Any sensor update requested between update intervals contains
no detections or tracks.

#### Sensor Mounting

### **Translation [ X, Y, Z ] relative to ego origin (m)** — Sensor location on ego vehicle (m) `[3.4, 0, 0.2]` (default) | 1-by-3 real-valued vector of form [*x* *y* *z*]

Specify the sensor location on the ego vehicle body frame in meters as a
1-by-3 real-valued vector of the form [*x*
*y*
*z*]. This parameter defines the coordinates of the sensor
along the *x*-axis, *y*-axis, and
*z*-axis relative to the ego vehicle origin, where:

- The *x*-axis points forward from the
  vehicle.
- The *y*-axis points to the left of the
  vehicle.
- The *z*-axis points up from the ground.

The default value corresponds to a radar that is mounted at the center of
the front grill of a sedan.

For more details on the ego vehicle coordinate system, see Coordinate Systems in Automated Driving Toolbox.

### **Rotation [Yaw, Pitch, Roll] relative to ego's frame (deg)** — Mounting rotation angles of radar `[0 0 0]` (default) | 1-by-3 real-valued vector of form [*z*yaw *y*pitch *x*roll]

Specify the mounting rotation angles of the radar in degrees as a 1-by-3
real-valued vector of form [*z*yaw
*y*pitch
*x*roll]. This parameter defines the
intrinsic Euler angle rotation of the sensor around the
*z*-axis, *y*-axis, and
*x*-axis with respect to the ego vehicle body frame,
where:

- *z*yaw, or *yaw
  angle*, rotates the sensor around the
  *z*-axis of the ego vehicle.
- *y*pitch, or *pitch
  angle*, rotates the sensor around the
  *y*-axis of the ego vehicle. This rotation is relative
  to the sensor position that results from the
  *z*yaw rotation.
- *x*roll, or *roll
  angle*, rotates the sensor about the
  *x*-axis of the ego vehicle. This rotation is relative
  to the sensor position that results from the
  *z*yaw and
  *y*pitch rotations.

These angles are clockwise-positive when looking in the forward direction of
the *z*-axis, *y*-axis, and
*x*-axis, respectively. If you visualize sensor data from a
bird's-eye view perspective, then the yaw angle is counterclockwise-positive
because you are viewing the data in the negative direction of the *z*-axis, which points up from the ground.

For more details on this coordinate system, see Coordinate Systems in Automated Driving Toolbox.

#### Detection Reporting

### **Enable elevation angle measurements** — Enable radar to measure target elevation angles `off` (default) | `on`

Select this parameter to model a radar sensor that can estimate target
elevation.

### **Enable range rate measurements** — Enable radar to measure target range rates `on` (default) | `off`

Select this parameter to enable the radar to measure range rates from target
detections.

### **Add noise to measurements** — Enable addition of noise to radar sensor measurements `on` (default) | `off`

Select this parameter to add noise to the radar measurements. Otherwise, the
measurements have no noise. Even if you clear this parameter, the measurement
noise covariance matrix, which is reported in the
`MeasurementNoise` field of the generated detections
output, represents the measurement noise that is added when **Add noise
to measurements** is selected.

### **Enable false reports** — Enable creating false alarm radar detections `on` (default) | `off`

Select this parameter to enable creating false alarm radar measurements. If
you clear this parameter, the radar reports only actual detections.

### **Enable occlusion** — Enable line-of-sight occlusion `on` (default) | `off`

Select this parameter to enable line-of-sight occlusion, where the radar
generates detection only from objects for which the radar has a direct line of
sight. For example, with this parameter enabled, the radar does not generate a
detection for a vehicle that is behind another vehicle and blocked from
view.

### **Maximum number of target reports** — Maximum number of detections or tracks `50` (default) | positive integer

Specify the maximum number of detections or tracks that the sensor reports
as a positive integer. The sensor reports detections in the order of increasing
distance from the sensor until reaching this maximum number.

### **Target reporting format** — Format of generated target reports `Clustered detections` (default) | `Tracks` | `Detections`

Specify the format of generated target reports as one of these
options:

- `Clustered detections` — The block generates target
  reports as *clustered detections*, where each target
  is reported as a single detection that is the centroid of the unclustered
  target detections. The block returns clustered detections at the
  **Clustered detections** output port.
- `Tracks` — The block generates target reports as
  *tracks*, which are clustered detections that
  have been processed by a tracking filter. The block returns clustered
  detections at the **Tracks** output port.
- `Detections` — The block generates target reports as
  *unclustered detections*, where each target can
  have multiple detections. The block returns clustered detections at the
  **Detections** output port.

### **Coordinate system** — Coordinate system of reported detections `Body` (default) | `Sensor rectangular` | `Sensor spherical`

Coordinate system of reported detections, specified as one of these options:

- `Body` — Detections are reported in the
  rectangular body system of the ego vehicle.
- `Sensor rectangular` — Detections are reported in
  the rectangular body system of the radar sensor.
- `Sensor spherical` — Detections are reported in a
  spherical coordinate system that is centered at the radar sensor and
  aligned with the orientation of the radar on the ego vehicle.

#### Port Settings

### **Source of output bus name** — Source of output bus name `Auto` (default) | `Property`

Source of output bus name, specified as one of these options:

- `Auto` — The block automatically creates a
  bus name.
- `Property` — Specify the bus name by using
  the **Specify an output bus name** parameter.

### **Specify an output bus name** — Name of output bus `BusDrivingRadarDataGenerator` (default) | valid bus name

Specify the name of the actor poses bus returned in the
**Actors** output port.

To enable this parameter, set the **Source of output bus
name** parameter to `Property`.

### Measurements

#### Resolution Settings

### **Azimuth resolution (deg)** — Azimuth resolution of radar `4` (default) | positive real scalar

Specify the azimuth resolution of the radar in degrees as a positive scalar.
The *azimuth resolution* defines the minimum separation in
azimuth angle at which the radar can distinguish between two targets. The
azimuth resolution is typically the 3 dB downpoint of the azimuth angle
beamwidth of the radar.

### **Elevation resolution (deg)** — Elevation resolution of radar `5` (default) | positive real scalar

Specify the elevation resolution of the radar in degrees as a positive real
scalar. The *elevation resolution* defines the minimum
separation in elevation angle at which the radar can distinguish between two
targets. The elevation resolution is typically the 3 dB downpoint in elevation
angle beamwidth of the radar.

#### Dependencies

To enable this parameter, on the **Parameters** tab,
select the **Enable elevation angle measurements**
parameter.

### **Range resolution (m)** — Range resolution of radar `2.5` (default) | positive real scalar

Specify the range resolution of the radar in meters as a positive real
scalar. The *range resolution* defines the minimum
separation in range at which the radar can distinguish between two
targets.

### **Range rate resolution (m/s)** — Range rate resolution of radar `0.5` (default) | positive real scalar

Specify the range rate resolution of the radar in meters per second as a
positive real scalar. The *range rate resolution* defines
the minimum separation in range rate at which the radar can distinguish between
two targets.

#### Dependencies

To enable this parameter, on the **Parameters** tab,
select the **Enable range rate resolution**
parameter.

#### Bias Settings

### **Azimuth bias fraction** — Azimuth bias fraction of radar `0.1` (default) | nonnegative scalar

Specify the azimuth bias fraction of the radar as a nonnegative scalar.
*Azimuth bias* is expressed as a fraction of the
azimuth resolution specified in the **Azimuth resolution
(deg)** parameter. This value sets a lower bound on the azimuthal
accuracy of the radar and is dimensionless.

### **Elevation bias fraction** — Elevation bias fraction of radar `0.1` (default) | nonnegative scalar

Specify the elevation bias fraction of the radar as a nonnegative scalar.
*Elevation bias* is expressed as a fraction of the
elevation resolution specified by the **Elevation resolution
(deg)** parameter. This value sets a lower bound on the elevation
accuracy of the radar and is dimensionless.

#### Dependencies

To enable this parameter, on the **Parameters** tab,
select the **Enable elevation angle measurements**
parameter.

### **Range bias fraction** — Range bias fraction `0.05` (default) | nonnegative scalar

Specify the range bias fraction of the radar as a nonnegative scalar. Range
bias is expressed as a fraction of the range resolution specified by the
**Range resolution (m)** property. This property sets a
lower bound on the range accuracy of the radar and is dimensionless.

### **Range rate bias fraction** — Range rate bias fraction `0.05` (default) | nonnegative scalar

Specify the range rate bias fraction of the radar as a nonnegative scalar.
Range rate bias is expressed as a fraction of the range rate resolution
specified by the **Range rate resolution (m/s)** parameter.
This property sets a lower bound on the range rate accuracy of the radar and is
dimensionless.

#### Dependencies

To enable this parameter, on the **Parameters** tab,
select the **Enable range rate measurements**
parameter.

#### Detector Settings

### **Total angular field of view [AZ, EL] (deg)** — Angular field of view of radar `[20 5]` (default) | 1-by-2 positive real-valued vector of form `[azfov, elfov]`

Specify the angular field of view of the radar in degrees as a 1-by-2
positive real-valued vector of the form `[azfov elfov]`. The
field of view defines the total angular extent spanned by the sensor. The
azimuth field of view, `azfov`, must lie in the interval (0,
360]. The elevation field of view, `elfov`, must lie in the
interval (0, 180].

### **Range limits [MIN, MAX] (m)** — Minimum and maximum range of radar `[0 150]` (default) | 1-by-2 nonnegative real-valued vector of form `[min max]`

Specify the minimum and maximum range of the radar in meters as a 1-by-2
nonnegative real-valued vector of the form `[min max]`. The
radar does not detect targets that are outside this range. The maximum range,
`max`, must be greater than the minimum range,
`min`.

### **Range rate limits [MIN, MAX] (m/s)** — Minimum and maximum range rate of radar (m/s) `[-100 100]` (default) | 1-by-2 real-valued vector of form `[min max]`

Specify the minimum and maximum range rate of radar in meters per second as
a 1-by-2 real-valued vector of the form `[min max]`. The radar
does not detect targets that are outside this range rate. The maximum range
rate, `max`, must be greater than the minimum range rate,
`min`.

#### Dependencies

To enable this parameter, on the **Parameters** tab,
select the **Enable range rate measurements**
parameter.

### **Detection probability** — Probability of detecting a target `0.9` (default) | scalar in range (0, 1]

Specify the probability of detecting a target as a scalar in the range (0,
1]. This quantity defines the probability of detecting a target with a radar
cross-section, with the radar cross-section specified by the
**Reference target RCS (dBsm)** parameter at the reference
detection range specified by the **Reference target range
(m)** parameter.

### **False alarm rate** — False alarm report rate `1e-06` (default) | positive real scalar in range [10–7, 10–3]

Specify the false alarm report rate within each radar resolution cell as a
positive real scalar in the range [10–7,
10–3]. Units are dimensionless. The block
determines resolution cells from the **Azimuth resolution
(deg)** and **Range resolution (m)** parameters
and, when enabled, from the **Elevation resolution (deg)** and
**Range rate resolution (m/s)** parameters.

### **Reference target range (m)** — Reference range for given probability of detection `100` (default) | positive real scalar

Specify the reference range for the given probability of detection and the
given reference radar cross-section (RCS) in meters as a positive real scalar.
The *reference range* is the range at which a target
having a radar cross-section specified by the **Reference target RCS
(dBsm)** parameter is detected with a probability of detection
specified by the **Detection probability** parameter.

### **Reference target RCS (dBsm)** — Reference radar cross-section for given probability of detection `0` (default) | real scalar

Specify the reference radar cross-section (RCS) for a given probability of
detection and reference range in decibel square meters as a real scalar. The
*reference RCS* is the RCS value at which a target is
detected with a probability specified by the **Detection
probability** parameter at the specified **Reference target
range (m)** parameter value.

### **Center frequency (Hz)** — Center frequency of radar band `77e9` (default) | positive real scalar

Specify the center frequency of the radar band in hertz as a positive
scalar.

#### Tracker Settings

### **Filter initialization function name** — Kalman filter initialization function `initcvekf` (default) | function name

Specify the Kalman filter initialization function as a function handle or as
a character vector or string scalar of the name of a valid Kalman filter
initialization function.

The table shows the initialization functions that you can use to specify
**Filter initialization function name**.

| Initialization Function | Function Definition |
| --- | --- |
| `initcaabf` | Initialize constant-acceleration alpha-beta Kalman filter |
| `initcvabf` | Initialize constant-velocity alpha-beta Kalman filter |
| `initcakf` | Initialize constant-acceleration linear Kalman filter. |
| `initcvkf` | Initialize constant-velocity linear Kalman filter. |
| `initcaekf` | Initialize constant-acceleration extended Kalman filter. |
| `initctekf` | Initialize constant-turnrate extended Kalman filter. |
| `initcvekf` | Initialize constant-velocity extended Kalman filter. |
| `initcaukf` | Initialize constant-acceleration unscented Kalman filter. |
| `initctukf` | Initialize constant-turnrate unscented Kalman filter. |
| `initcvukf` | Initialize constant-velocity unscented Kalman filter. |

You can also write your own initialization function. The function must have
the following
syntax:

```
filter = filterInitializationFcn(detection)
```

The
input to this function is a detection report like those created by an `objectDetection` object. The output of this function must be a
tracking filter object, such as `trackingKF`, `trackingEKF`, `trackingUKF`, or `trackingABF`.

To guide you in writing this function, you can examine the details of the
supplied functions from within MATLAB. For example:

```
type initcvekf
```

#### Dependencies

To enable this parameter, on the **Parameters** tab, set
the **Target reporting format** parameter to
`Tracks`.

### **M and N for the M-out-of-N confirmation** — Threshold for track confirmation `[2 3]` (default) | 1-by-2 vector of positive integers

Specify the threshold for track confirmation as a 1-by-2 vector of positive
integers of the form `[M N]`. A track is confirmed if it
receives at least `M` detections in the last
`N` updates. `M` must be less than or
equal to `N`.

- When setting `M`, take into account the
  probability of object detection for the sensors. The probability of
  detection depends on factors such as occlusion or clutter. You can
  reduce `M` when tracks fail to be confirmed or
  increase `M` when too many false detections are
  assigned to tracks.
- When setting `N`, consider the number of times you
  want the tracker to update before it makes a confirmation decision.
  For example, if a tracker updates every 0.05 seconds, and you want to
  allow 0.5 seconds to make a confirmation decision, set `N =
  10`.

#### Dependencies

To enable this parameter, on the **Parameters** tab, set
the **Target reporting format** parameter to
`Tracks`.

### **P and R for the P-out-of-R deletion** — Threshold for track deletion `[5 5]` (default) | 1-by-2 vector of positive integers

Specify the threshold for track deletion as a two-element vector of 1-by-2
vector of positive integers of the form `[P R]`. If a
confirmed track is not assigned to any detection `P` times in
the last `R` tracker updates, then the track is deleted.
`P` must be less than or equal to
`R`.

#### Dependencies

To enable this parameter, on the **Parameters** tab, set
the **Target reporting format** parameter to
`Tracks`.

#### Random Number Generator Settings

### **Random number generation** — Method to specify random number generator seed `Repeatable` (default) | `Specify seed` | `Not repeatable`

Specify the method to set the random number generator seed as one of the
options in the table.

| Option | Description |
| --- | --- |
| `Repeatable` | The block generates a random initial seed for the first simulation and reuses this seed for all subsequent simulations. Select this parameter to generate repeatable results from the statistical sensor model. To change this initial seed, at the MATLAB command prompt, enter: `clear all`. |
| `Specify seed` | Specify your own random initial seed for reproducible results by using the **Initial seed** parameter. |
| `Not repeatable` | The block generates a new random initial seed after each simulation run. Select this parameter to generate nonrepeatable results from the statistical sensor model. |

### **Initial seed** — Random number generator seed `0` (default) | nonnegative integer less than 232

Specify the random number generator seed as a nonnegative integer less than
232.

#### Dependencies

To enable this parameter, set the **Random number
generation** parameter to `Specify
seed`.

### Target Profiles

### **Target profiles definition** — Method to specify target profiles `From Scenario Reader block` (default) | `MATLAB expression` | `Parameters`

Specify the method to specify target profiles, which are the physical and
radar characteristics of all targets in the driving scenario, as one of these options:

- `Parameters` — The block obtains the
  target profiles from the parameters enabled on the **Target
  Profiles** tab when you select this option.
- `MATLAB expression` — The block obtains
  the actor profiles from the MATLAB expression specified by the **MATLAB expression
  for target profiles** parameter.
- `From Scenario Reader block` — The block
  obtains the actor profiles from the scenario specified by the Scenario Reader block or RoadRunner Scenario Reader block.

### **MATLAB expression for target profiles** — MATLAB expression for target profiles MATLAB structure | MATLAB structure array | valid MATLAB expression

Specify the MATLAB expression for actor profiles, as a MATLAB structure, a MATLAB structure array, or a valid MATLAB expression that produces such a structure or structure
array.

If your Scenario Reader block reads data from a `drivingScenario` object, to obtain
the actor profiles directly from this object, set this expression to call the
`actorProfiles` function on the
object. For example: `actorProfiles(scenario)`.

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
length-*L* vector of unique positive integers.
*L* must equal the number of actors input into the
**Actors** input port. The vector elements must match
`ActorID` values of the actors. You can specify
**Unique identifier for actors** as `[]`.
In this case, the same actor profile parameters apply to all actors.

**Example:** `[1 2]`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to
`Parameters`.

### **User-defined integer to classify actors** — User-defined classification identifier `0` (default) | integer | length-*L* vector of integers

Specify the user-defined classification identifier as an integer or
length-*L* vector of integers. When **Unique
identifier for actors** is a vector, this parameter is a vector of
the same length with elements in one-to-one correspondence to the actors in
**Unique identifier for actors**. When **Unique
identifier for actors** is empty, `[]`, you must
specify this parameter as a single integer whose value applies to all
actors.

**Example:** `2`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to
`Parameters`.

### **Length of actors' cuboids (m)** — Length of actor cuboids `4.7` (default) | positive real scalar | length-*L* vector of positive values

Specify the length of actor cuboids as a positive real scalar or
length-*L* vector of positive values. When **Unique
identifier for actors** is a vector, this parameter is a vector of
the same length with elements in one-to-one correspondence to the actors in
**Unique identifier for actors**. When **Unique
identifier for actors** is empty, `[]`, you must
specify this parameter as a positive real scalar whose value applies to all
actors. Units are in meters.

**Example:** `6.3`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to
`Parameters`.

### **Width of actors' cuboids (m)** — Width of actor cuboids `1.8` (default) | positive real scalar | length-*L* vector of positive values

Specify the width of actor cuboids as a positive real scalar or
length-*L* vector of positive values. When **Unique
identifier for actors** is a vector, this parameter is a vector of
the same length with elements in one-to-one correspondence to the actors in
**Unique identifier for actors**. When **Unique
identifier for actors** is empty, `[]`, you must
specify this parameter as a positive real scalar whose value applies to all
actors. Units are in meters.

**Example:** `4.7`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to
`Parameters`.

### **Height of actors' cuboids (m)** — Height of actor cuboids `1.4` (default) | positive real scalar | length-*L* vector of positive values

Specify the height of actor cuboids as a positive real scalar or
length-*L* vector of positive values. When **Unique
identifier for actors** is a vector, this parameter is a vector of
the same length with elements in one-to-one correspondence to the actors in
**Unique identifier for actors**. When **Unique
identifier for actors** is empty, `[]`, you must
specify this parameter as a positive real scalar whose value applies to all
actors. Units are in meters.

**Example:** `2.0`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to
`Parameters`.

### **Rotational center of actors from bottom center (m)** — Rotational center of actors `{[-1.35, 0, 0]}` (default) | length-*L* cell array of real-valued 1-by-3 vectors

Specify the rotational center of actors as a length-*L*
cell array of real-valued 1-by-3 vectors. Each vector represents the offset of
the rotational center of an actor from the bottom-center of the actor. For
vehicles, the offset corresponds to the point on the ground beneath the center
of the rear axle. When **Unique identifier for actors** is a
vector, this parameter is a cell array of vectors with cells in one-to-one
correspondence to the actors in **Unique identifier for
actors**. When **Unique identifier for actors** is
empty, `[]`, you must specify this parameter as a cell array
of one element containing an offset vector whose values apply to all actors.
Units are in meters. The center of rotation is defined according to the
convention detailed in Actor and Vehicle Positions and Dimensions.

**Example:** `{[-1.35, 0.2, 0.3]}`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to
`Parameters`.

### **Radar cross section pattern (dBsm)** — Radar cross-section `{[10, 10; 10, 10]}` (default) | real-valued *Q*-by-*P* matrix | length-*L* cell array of real-valued *Q*-by-*P* matrices

Specify the radar cross-section (RCS) of actors as a real-valued
*Q*-by-*P* matrix or
length-*L* cell array of real-valued
*Q*-by-*P* matrices. *Q*
is the number of elevation angles specified by the corresponding cell in the
**Elevation angles defining RCSPattern (deg)** parameter.
*P* is the number of azimuth angles specified by the
corresponding cell in **Azimuth angles defining RCSPattern
(deg)** parameter. When **Unique identifier for
actors** is a vector, this parameter is a cell array of matrices
with cells in one-to-one correspondence to the actors in **Unique
identifier for actors**. The values of *Q* and
*P* can differ between cells. When **Unique
identifier for actors** is empty, `[]`, you must
specify this parameter as a cell array with one element containing a matrix
whose values apply to all actors. Units are in dBsm.

**Example:** `{[10 14 10; 9 13 9]}`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to
`Parameters`.

### **Azimuth angles defining RCSPattern (deg)** — Azimuth angles of radar cross-section pattern `{[-180 180]}` (default) | length-*L* cell array of real-valued *P*-length vectors

Specify the azimuth angles of radar cross-section patterns as a
length-*L* cell array of real-valued
*P*-length vectors. Each vector represents the azimuth angles
of the *P* columns of the radar cross-section specified in
**Radar cross section pattern (dBsm)**. When
**Unique identifier for actors** is a vector, this
parameter is a cell array of vectors with cells in one-to-one correspondence to
the actors in **Unique identifier for actors**. The value of
*P* can differ between cells. When **Unique
identifier for actors** is empty, `[]`, you must
specify this parameter as a cell array with one element containing a vector
whose values apply to all actors. Units are in degrees. Azimuth angles lie in
the range –180° to 180° and must be in strictly increasing order.

When the radar cross-sections specified in the cells of **Radar
cross section pattern (dBsm)** all have the same dimensions, you
need only specify a cell array with one element containing the azimuth angle
vector.

**Example:** `{[-90 90]}`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to
`Parameters`.

### **Elevation angles defining RCSPattern (deg)** — Elevation angles of radar cross-section pattern `{[-90 90]}` (default) | length-*L* cell array of real-valued *Q*-length vectors

Specify the elevation angles of radar cross-section patterns as a
length-*L* cell array of real-valued
*Q*-length vectors. Each vector represent the elevation angles
of the *Q* columns of the radar cross-section specified in
**Radar cross section pattern (dBsm)**. When
**Unique identifier for actors** is a vector, this
parameter is a cell array of vectors with cells in one-to-one correspondence to
the actors in **Unique identifier for actors**. The value of
*Q* can differ between cells. When **Unique
identifier for actors** is empty, `[]`, you must
specify this parameter as a cell array with one element containing a vector
whose values apply to all actors. Units are in degrees. Elevation angles lie in
the range –90° to 90° and must be in strictly increasing order.

When the radar cross-sections that are specified in the cells of
**Radar cross section pattern (dBsm)** all have the same
dimensions, you need only specify a cell array with one element containing an
elevation angle vector.

**Example:** `{[-25 25]}`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to
`Parameters`.

## Libraries

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- For driving scenario workflows, the Driving Radar Data Generator
  block supports:

  - Rapid accelerator mode simulation.
  - Standalone deployment using Simulink
    Coder™ and for Simulink
    Real-Time™ targets.
- For RoadRunner Scenario workflows, the Driving Radar Data
  Generator block supports standalone deployment using ready-to-run
  packages. For more information about generating ready-to-run packages for your
  Simulink model, see Publish Ready-to-Run Actor Behaviors for Reuse and Simulation Performance.

## Version History

**Introduced in R2021a**

### R2024a: Usage with RoadRunner Scenario simulation does not require registering the sensor model using `addSensors` function

Starting in R2024a, Simulink automatically instantiates a `SensorSimulation` object and adds sensors defined in the model to the RoadRunner scenario. Hence, registering Driving Radar Data Generator block manually using the `addSensors` function is not required. For more information on the new workflow, see the Add Sensors to RoadRunner Scenario Using Simulink example.

In releases prior to R2024a, you must manually register the block as a sensor model using the `addSensors` function. For more information, see Adding sensors manually using `addSensors` function is not required for Simulink models.

## Description

Generate radar sensor detections or track reports from driving scenario or RoadRunner Scenario

The Driving Radar Data Generator block generates detection or track
reports of targets from an automotive radar sensor model. Use this block to generate sensor
data from a driving scenario containing actors and trajectories, which you can read from a
Scenario Reader
block.

The Driving Radar Data Generator block can simulate clustered or
unclustered detections with added random noise and also generate false alarm detections.
You can fuse the generated detections with other sensor data and track objects by using a
Multi-Object
Tracker block. You can also output tracks directly from the Driving Radar
Data Generator block. To configure whether targets are output as clustered
detections, unclustered detections, or tracks, use the **Target reporting
format** parameter.

You can use the block with vehicle actors in Driving Scenario and RoadRunner Scenario simulations. For more information, see Add Sensors to RoadRunner Scenario Using Simulink example.
