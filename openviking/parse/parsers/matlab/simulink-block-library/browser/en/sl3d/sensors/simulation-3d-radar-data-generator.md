---
type: simulink-block
title: 'Simulation 3D Radar Data Generator'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'simulation3dradardatagenerator'
documentation_source_path: 'simulation3dradardatagenerator.html'
language: en
---

# Simulation 3D Radar Data Generator

## Ports

### Output

### **Clustered detections** — Clustered object detections Simulink® bus containing MATLAB® structure

Clustered object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).

With clustered detections, the block outputs a single detection per target, where
each detection is the centroid of the unclustered detections for that target.

The structure contains these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of valid detections | Nonnegative integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures of length set by the **Maximum number of target reports** parameter. Only `NumDetections` of these are actual detections. |

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
  `MeasurementNoise` are reported in the rectangular
  coordinate system specified by the **Coordinate frame used to report
  detections** parameter.
- For spherical coordinates, `Measurement` and
  `MeasurementNoise` are reported in the spherical coordinate
  system, which is based on the sensor rectangular coordinate system.

**`Measurement` and
`MeasurementNoise`**

| **Coordinate System** | `Measurement` and `MeasurementNoise` Coordinates |
| --- | --- |
| `Body` | This table shows how coordinates are affected by the **Enable range rate measurements** parameter.  | **Enable range rate measurements** | Coordinates | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Sensor rectangular` |
| `Sensor spherical` | This table shows how coordinates are affected by the **Enable elevation angle measurements** and **Enable range rate measurements** parameters.  | **Enable range rate measurements** | **Enable elevation angle measurements** | Coordinates | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` | |

For `ObjectAttributes`, this table describes the additional
information used for tracking.

**`ObjectAttributes`**

| Attribute | Definition |
| --- | --- |
| `TargetIndex` | Identifier of the actor, `ActorID`, that generated the detection. For false alarms, this value is negative. |
| `SNR` | Signal-to-noise ratio of the detection. Units are in dB. |

For `MeasurementParameters`, the measurements are relative
to the parent frame. When you set the **Coordinate frame used to report
detections** parameter to `Body`, the parent frame is the
ego vehicle body. When you set **Coordinate frame used to report
detections** to `Sensor rectangular` or `Sensor
spherical`, the parent frame is the sensor.

**`MeasurementParameters`**

| Parameter | Definition |
| --- | --- |
| `Frame` | Enumerated type indicating the frame used to report measurements. When `Frame` is set to `'rectangular'`, detections are reported in Cartesian coordinates. When `Frame` is set to `'spherical'`, detections are reported in spherical coordinates. |
| `OriginPosition` | 3-D vector offset of the sensor origin from the parent frame origin. |
| `Orientation` | Orientation of the radar sensor coordinate system with respect to the parent frame. |
| `HasVelocity` | Indicates whether measurements contain velocity or range rate components. |
| `HasElevation` | Indicates whether measurements contain elevation components. |

#### Dependencies

To enable this port, on the **Parameters** tab, set
**Format of generated target reports** to `Clustered
detections`.

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

For more details about these fields, see `objectTrack` (Automated Driving Toolbox).

The block outputs only confirmed tracks, which are tracks to which the block
assigns at least *M* detections during the first *N*
updates after track initialization. To specify the values *M* and
*N*, use the **M and N for the M-out-of-N
confirmation** parameter.

#### Dependencies

To enable this port, on the **Parameters** tab, set
**Format of generated target reports** to
`Tracks`.

### **Detections** — Unclustered object detections Simulink bus containing MATLAB structure

Unclustered object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).

With unclustered detections, the block outputs all detections, and a target can
have multiple detections.

You can pass object detections from these sensors and other sensors to a tracker,
such as a Multi-Object
Tracker (Automated Driving Toolbox) block, and generate tracks.

The structure must contain these fields:

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of valid detections | integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures of length set by the **Maximum number of target reports** parameter. Only `NumDetections` of these are actual detections. |

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
  `MeasurementNoise` are reported in the rectangular
  coordinate system specified by the **Coordinate frame used to report
  detections** parameter.
- For spherical coordinates, `Measurement` and
  `MeasurementNoise` are reported in the spherical coordinate
  system, which is based on the sensor rectangular coordinate system.

**`Measurement` and
`MeasurementNoise`**

| **Coordinate System** | `Measurement` and `MeasurementNoise` Coordinates |
| --- | --- |
| `Body` | This table shows how coordinates are affected by the **Enable range rate measurements** parameter.  | **Enable range rate measurements** | Coordinates | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Sensor rectangular` |
| `Sensor spherical` | This table shows how coordinates are affected by the **Enable elevation angle measurements** and **Enable range rate measurements** parameters.  | **Enable range rate measurements** | **Enable elevation angle measurements** | Coordinates | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` | |

For `ObjectAttributes`, this table describes the additional
information used for tracking.

**`ObjectAttributes`**

| Attribute | Definition |
| --- | --- |
| `TargetIndex` | Identifier of the actor, `ActorID`, that generated the detection. For false alarms, this value is negative. |
| `SNR` | Signal-to-noise ratio of the detection. Units are in dB. |

For `MeasurementParameters`, the measurements are relative
to the parent frame. When you set the **Coordinate frame used to report
detections** parameter to `Body`, the parent frame is the
ego vehicle body. When you set **Coordinate frame used to report
detections** to `Sensor rectangular` or `Sensor
spherical`, the parent frame is the sensor.

**`MeasurementParameters`**

| Parameter | Definition |
| --- | --- |
| `Frame` | Enumerated type indicating the frame used to report measurements. When `Frame` is set to `'rectangular'`, detections are reported in Cartesian coordinates. When `Frame` is set to `'spherical'`, detections are reported in spherical coordinates. |
| `OriginPosition` | 3-D vector offset of the sensor origin from the parent frame origin. |
| `Orientation` | Orientation of the radar sensor coordinate system with respect to the parent frame. |
| `HasVelocity` | Indicates whether measurements contain velocity or range rate components. |
| `HasElevation` | Indicates whether measurements contain elevation components. |

#### Dependencies

To enable this port, on the **Parameters** tab, set
**Format of generated target reports** to
`Detections`.

## Parameters

### Mounting

#### Sensor Identification

### **Sensor identifier** — Unique sensor identifier `1` (default) | positive integer

Unique sensor identifier, specified as a positive integer. Use this parameter to
distinguish between detections or tracks that come from different sensors in a
multisensor system. Specify a unique value for each sensor.

### **Parent name** — Name of parent vehicle `Scene Origin` (default) | vehicle name

Name of the parent to which the sensor is mounted, specified as `Scene
Origin` or as the name of an actor in your model. The actor names that
you can select correspond to the **Name** parameters of the
simulation 3D vehicle blocks in your model. If you select `Scene
Origin`, the block places a sensor at the scene origin.

**Example:** `SimulinkVehicle1`

### **Coordinate system** — Coordinate system for actor transformation `Default` (default) | `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

*Since R2025a*

Specify the coordinate system that the actor uses for
translation and rotation in the 3D environment.

- `Default` – World coordinate system
- `MATLAB` – MATLAB coordinate system
- `ISO8855` – ISO 8855 standard coordinate system
- `AERO` – SAE coordinate system
- `VRML` – X3D ISO standard coordinate system
- `SAE` – SAE coordinate system

For more details on the different coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `MATLAB`

#### Sensor Mounting

### **Mounting location** — Sensor mounting location `Origin` (default)

Sensor mounting location.

- When **Parent name** is `Scene
  Origin`, the block mounts the sensor to the origin of the scene.
  You can set the **Mounting location** to
  `Origin` only. During simulation, the sensor remains
  stationary.
- When **Parent name** is the name of a vehicle, the block
  mounts the sensor to one of the predefined mounting locations described in the
  table. During simulation, the sensor travels with the vehicle. For example, the
  table provides the mounting locations in the ISO 8855 standard coordinate
  system.

  | Mounting Location | Description | Orientation Relative to Vehicle Origin [Roll, Pitch, Yaw] (deg) |
  | --- | --- | --- |
  | `Origin` | Forward-facing sensor mounted to the vehicle origin, which is on the ground and at the geometric center of the vehicle (see Coordinate Systems in Simulink 3D Animation).  Vehicle with sensor mounted at origin | [0, 0, 0] |
  | `Front bumper`  `Front center` | Forward-facing sensor mounted to the front bumper  Vehicle with sensor mounted at front bumper | [0, 0, 0] |
  | `Rear bumper`  `Rear center` | Backward-facing sensor mounted to the rear bumper  Vehicle with sensor mounted at rear bumper | [0, 0, 180] |
  | `Right mirror` | Downward-facing sensor mounted to the right side-view mirror  Vehicle with sensor mounted at right side-view mirror | [0, –90, 0] |
  | `Left mirror` | Downward-facing sensor mounted to the left side-view mirror  Vehicle with sensor mounted at left side-view mirror | [0, –90, 0] |
  | `Rearview mirror` | Forward-facing sensor mounted to the rearview mirror, inside the vehicle  Vehicle with sensor mounted at rearview mirror | [0, 0, 0] |
  | `Hood center` | Forward-facing sensor mounted to the center of the hood  Vehicle with sensor mounted at hood center | [0, 0, 0] |
  | `Roof center` | Forward-facing sensor mounted to the center of the roof  Vehicle with sensor mounted at roof center | [0, 0, 0] |

  The
  *X*-*Y*-*Z* mounting
  location of the sensor relative to the vehicle depends on the vehicle type. To
  specify the vehicle type, use the **Type** parameter of the
  Simulation 3D Vehicle
  with Ground Following to which you mount the sensor. To obtain the
  *X*-*Y*-*Z* mounting
  locations for a vehicle type, see the reference page for that vehicle.

### **Specify offset** — Specify offset from mounting location `off` (default) | `on`

Select this parameter to specify an offset from the mounting location by using the
**Relative translation [X, Y, Z]** and **Relative rotation
[Roll, Pitch, Yaw]** parameters.

### **Relative translation [X, Y, Z]** — Translation offset relative to mounting location `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Translation offset relative to the mounting location of the sensor, specified as a
real-valued 1-by-3 vector of the form [*X*, *Y*,
*Z*].

You can mount the sensor to a vehicle by setting **Parent name**
to the name of that vehicle. The origin is the mounting location specified in the
**Mounting location** parameter. This origin is different from the
vehicle origin, which is the geometric center of the vehicle. You can also mount the
sensor to the scene origin by setting **Parent name** to
`Scene Origin`.

**Example:** `[0,0,0.01]`

### **Relative rotation [Roll, Pitch, Yaw]** — Rotational offset relative to mounting location `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Rotational offset relative to the mounting location of the sensor, specified as a
real-valued 1-by-3 vector of the form [*Roll*,
*Pitch*, *Yaw*]. Roll, pitch, and yaw are the
angles of rotation about the *X*-, *Y*-, and
*Z*-axes, respectively.

You can mount the sensor to a vehicle by setting **Parent name**
to the name of that vehicle. The origin is the mounting location specified in the
**Mounting location** parameter. This origin is different from the
vehicle origin, which is the geometric center of the vehicle. You can also mount the
sensor to the scene origin by setting **Parent name** to
`Scene Origin`.

**Example:** `[0,0,10]`

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time of the block, in seconds, specified as a positive scalar. The 3D simulation
environment frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block inherits its sample time from
the Simulation 3D Scene Configuration block.

### Parameters

#### Detection Reporting

### **Enable elevation angle measurements** — Enable radar to measure target elevation angles `on` (default) | `off`

Select this check box to model a radar sensor that can estimate target
elevation.

### **Enable range rate measurements** — Enable radar to measure target range rates `on` (default) | `off`

Select this check box to enable the radar to measure range rates from target
detections.

### **Add measurement noise to observations** — Enable addition of noise to radar sensor measurements `on` (default) | `off`

Select this parameter to add noise to the radar measurements. Otherwise, the
measurements have no noise. Even if you clear this parameter, the measurement noise
covariance matrix, which is reported in the `MeasurementNoise` field
of the generated detections output, represents the measurement noise that is added
when you select **Add noise to measurements**.

### **Enable generation of reports from false observations** — Enable creating false alarm radar detections `on` (default) | `off`

Select this parameter to enable creating false alarm radar measurements. If you
clear this parameter, the radar reports only actual detections.

### **Maximum number of target reports** — Maximum number of detections or tracks `50` (default) | positive integer

Specify the maximum number of detections or tracks that the sensor reports as a
positive integer. The sensor reports detections in the order of increasing distance
from the sensor until reaching this maximum number.

### **Format of generated target reports** — Format of generated target reports `Clustered detections` (default) | `Tracks` | `Detections`

Format of generated target reports, specified as one of these options:

- `Clustered detections` — The block generates target
  reports as *clustered detections*, where each target is
  reported as a single detection that is the centroid of the unclustered target
  detections. The block returns clustered detections at the Clustered detections
  output port.
- `Tracks` — The block generates target reports as
  *tracks*, which are clustered detections that have been
  processed by a tracking filter. The block returns clustered detections at the
  Tracks output port.
- `Detections` — The block generates target reports as
  *unclustered detections*, where each target can have
  multiple detections. The block returns clustered detections at the Detections
  output port.

### **Coordinate frame used to report detections** — Coordinate system of reported detections `Body` (default) | `Sensor rectangular` | `Sensor spherical`

Coordinate system of reported detections, specified as one of these options:

- `Body` — Detections are reported in the rectangular body
  system of the ego vehicle.
- `Sensor rectangular` — Detections are reported in the
  rectangular body system of the radar sensor.
- `Sensor spherical` — Detections are reported in a spherical
  coordinate system that is centered at the radar sensor and aligned with the
  orientation of the radar on the ego vehicle.

### Measurements

#### Resolution Settings

### **Azimuthal resolution (deg)** — Azimuth resolution of radar `4` (default) | positive real scalar

Azimuth resolution of the radar, specified as a positive scalar. The
*azimuth resolution* defines the minimum separation in azimuth
angle at which the radar can distinguish between two targets. The azimuth resolution
is typically the 3 dB downpoint of the azimuth angle beamwidth of the radar. Units are
in degrees.

### **Elevation resolution (deg)** — Elevation resolution of radar `5` (default) | positive real scalar

Elevation resolution of the radar, specified as a positive scalar. The
*elevation resolution* defines the minimum separation in
elevation angle at which the radar can distinguish between two targets. The elevation
resolution is typically the 3 dB downpoint of the elevation angle beamwidth of the
radar. Units are in degrees.

#### Dependencies

To enable this parameter, select the **Enable elevation angle
measurements** check box.

### **Range resolution (m)** — Range resolution of radar `2.5` (default) | positive real scalar

Range resolution of the radar in meters, specified as a positive real scalar. The
*range resolution* defines the minimum separation in range at
which the radar can distinguish between two targets. Units are in meters.

### **Range rate resolution (m/s)** — Range rate resolution of radar `0.5` (default) | positive real scalar

Range rate resolution of the radar, specified as a positive real scalar. The
*range rate resolution* defines the minimum separation in range
rate at which the radar can distinguish between two targets. Units are in meters per
second.

#### Dependencies

To enable this parameter, on the **Parameters** tab, select the
**Enable range rate measurements** check box.

#### Bias Settings

### **Azimuth bias fraction** — Azimuth bias fraction of radar `0.1` (default) | nonnegative scalar

Azimuth bias fraction of the radar, specified as a nonnegative scalar.
*Azimuth bias* is expressed as a fraction of the azimuth
resolution specified in the **Azimuth resolution (deg)** parameter.
This value sets a lower bound on the azimuthal accuracy of the radar and is
dimensionless.

### **Elevation bias fraction** — Elevation bias fraction of radar `0.1` (default) | nonnegative scalar

Elevation bias fraction of the radar, specified as a nonnegative scalar.
*Elevation bias* is expressed as a fraction of the elevation
resolution specified in the **Elevation resolution (deg)** parameter.
This value sets a lower bound on the elevation accuracy of the radar and is
dimensionless.

#### Dependencies

To enable this parameter, select the **Enable elevation angle
measurements** check box.

### **Range bias fraction** — Range bias fraction `0.05` (default) | nonnegative scalar

Range bias fraction of the radar, specified as a nonnegative scalar. Range bias is
expressed as a fraction of the range resolution specified by the **Range
resolution (m)** property. This property sets a lower bound on the range
accuracy of the radar and is dimensionless.

### **Range rate bias fraction** — Range rate bias fraction `0.05` (default) | nonnegative scalar

Range rate bias fraction of the radar, specified as a nonnegative scalar. Range
rate bias is expressed as a fraction of the range rate resolution specified by the
**Range rate resolution (m/s)** parameter. This property sets a
lower bound on the range rate accuracy of the radar and is dimensionless.

#### Dependencies

To enable this parameter, select the **Enable range rate
measurements** check box.

#### Detector Settings

### **Total angular field of view [AZ, EL] (deg)** — Angular field of view of radar `[20 5]` (default) | 1-by-2 positive real-valued vector of form `[azfov,elfov]`

Angular field of view of the radar, specified as a 1-by-2 positive real-valued
vector of the form `[azfov elfov]`. The field of view defines the
total angular extent spanned by the sensor. The azimuth field of view,
`azfov`, must lie in the interval (0, 360]. The elevation field of
view, `elfov`, must lie in the interval (0, 180]. Units are in
degrees

### **Range limits [MIN, MAX] (m)** — Minimum and maximum range of radar `[0 150]` (default) | 1-by-2 nonnegative real-valued vector of form `[min max]`

Minimum and maximum range of the radar, specified as a 1-by-2 nonnegative
real-valued vector of the form `[min max]`. The radar does not detect
targets that are outside this range. The maximum range, `max`, must
be greater than the minimum range, `min`. Units are in meters.

### **Range rate limits [MIN, MAX] (m/s)** — Minimum and maximum range rate of radar (m/s) `[-100 100]` (default) | 1-by-2 real-valued vector of form `[min max]`

Minimum and maximum range rate of radar as a 1-by-2 real-valued vector of the form
`[min max]`. The radar does not detect targets that are outside
this range rate. The maximum range rate, `max`, must be greater than
the minimum range rate, `min`. Units are in meters per second.

#### Dependencies

To enable this parameter, select the **Enable range rate
measurements** check box.

### **Detection probability** — Probability of detecting a target `0.9` (default) | scalar in range (0, 1]

Probability of detecting a target as a scalar, specified as a scalar in the range
(0, 1]. This quantity defines the probability of detecting a target with a radar
cross-section, with the radar cross-section specified by the **Reference
target RCS (dBsm)** parameter at the reference detection range specified by
the **Reference target range (m)** parameter. Units are
dimensionless.

### **False alarm rate** — False alarm report rate `1e-06` (default) | positive real scalar in range [10–7, 10–3]

False alarm report rate within each radar resolution cell, specified as a positive
real scalar in the range [10–7,
10–3]. The block determines resolution cells from the
**Azimuth resolution (deg)** and **Range resolution
(m)** parameters and, when enabled, from the **Elevation resolution
(deg)** and **Range rate resolution (m/s)** parameters.
Units are dimensionless.

### **Reference target range (m)** — Reference range for given probability of detection `100` (default) | positive real scalar

Reference range for the given probability of detection and the given reference
radar cross-section (RCS) , specified as a positive real scalar. The
*reference range* is the range at which a target having a radar
cross-section specified by the **Reference target RCS (dBsm)**
parameter is detected with a probability of detection specified by the
**Detection probability** parameter. Units are in meters.

### **Reference target RCS (dBsm)** — Reference radar cross-section for given probability of detection `0` (default) | real scalar

Reference radar cross-section (RCS) for a given probability of detection and
reference range, specified as a real scalar. The *reference RCS*
is the RCS value at which a target is detected with a probability specified by the
**Detection probability** parameter at the specified
**Reference target range (m)** parameter value. Values are
expressed in dBsm.

### **Center frequency (Hz)** — Center frequency of radar band `77e9` (default) | positive real scalar

Center frequency of the radar band, specified as a positive scalar. Units are in
Hz.

#### Random Number Generator Settings

### **Select method to specify initial seed** — Method to specify random number generator seed `Repeatable` (default) | `Specify seed` | `Not repeatable`

Method to set the random number generator seed as one of the options in the
table.

| Option | Description |
| --- | --- |
| `Repeatable` | The block generates a random initial seed for the first simulation and reuses this seed for all subsequent simulations. Select this parameter to generate repeatable results from the statistical sensor model. To change this initial seed, at the MATLAB command prompt, enter: `clear all`. |
| `Specify seed` | Specify your own random initial seed for reproducible results by using the **Initial seed** parameter. |
| `Not repeatable` | The block generates a new random initial seed after each simulation run. Select this parameter to generate nonrepeatable results from the statistical sensor model. |

### **Initial seed** — Random number generator seed `0` (default) | nonnegative integer less than 232

Random number generator seed, specified as a nonnegative integer less than
232.

#### Dependencies

To enable this parameter, set the **Select method to specify initial
seed** parameter to `Specify seed`.

#### Sampling settings

### **Actor types to oversample** — Actor type for improved target detection `Simulation 3D Vehicles` (default) | `None` | `Simulation 3D Actors` | `All Actors`

*Since R2025a*

Select the actor type in the 3D environment around which to improve target
detection. This parameter enables the senor to oversample rays towards the specified
actor types, improving target detection. Set the parameter as one of the options in
the table.

| Option | Description |
| --- | --- |
| `None` | Disable improved target detection. |
| `Simulation 3D Vehicles` | Enable improved target detection around any vehicle within the sensor field of view. |
| `Simulation 3D Actors` | Enable improved target detection around any actor created using classes or blocks within the sensor field of view. |
| `All Actors` | Enable improved target detection around any actor within the sensor field of view. |

For more information on target detection, see Target Detection.

#### Tips

- Oversampling rays toward actors in the 3D environment increases detection
  accuracy around the actor and requires more computational resources.

## Libraries

Simulink 3D Animation / Simulation 3D / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2025a: Enable improved target detection

Use the **Actor types to oversample** parameter in the
**Measurements** tab to enable improved target detection around a
specified actor object. You can set the parameter to one of these options.

- `None`
- `Simulation 3D Vehicles`
- `Simulation 3D Actors`
- `All Actors`

### R2025a: Set coordinate system parameter

Set the **Coordinate system** parameter in
the Simulation 3D Radar Data Generator block to represent the coordinate system for actor transformation
in the 3D environment.

## Description

Generate radar sensor detections and tracks

**Note**

Simulating models with the Simulation 3D Radar Data Generator block requires Radar Toolbox.

The Simulation 3D Radar Data Generator block generates detection and track reports of targets from
a radar sensor model. Use this block to generate sensor data from actors in the 3D simulation
environment. This environment is rendered using the Unreal Engine® from Epic Games®.

The Simulation 3D Radar Data Generator block can generate clustered or unclustered detections with
added random noise and can also generate false alarm detections. You can also generate tracks.
Use the **Format of generated target reports** parameter to specify whether
targets are output as clustered detections, unclustered detections, or tracks.

**Tip**

The Simulation 3D Scene Configuration
block must execute before the Simulation 3D Radar Data Generator block. That way, the Unreal Engine 3D visualization environment prepares the data before the
Simulation 3D Radar Data Generator block receives it. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Radar Data Generator — `1`

For more information about execution order, see Control and Display Execution Order (Simulink).

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.
