---
type: simulink-block
title: 'Fusion Radar Sensor'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Tracking Scenario and Sensor Models'
documentation_page: 'fusionradarsensor'
documentation_source_path: 'ref/fusionradarsensor.html'
language: en
---

# Fusion Radar Sensor

## Ports
```yaml
ports:
- name: Platforms
  summary: Target platform poses Simulink® bus containing MATLAB® structure
  direction: input
- name: INS
  summary: Radar reference platform pose from INS Simulink bus containing MATLAB structure
  direction: input
- name: Time
  summary: Current simulation time nonnegative scalar
  direction: input
  data_types: double
- name: Clustered Detections
  summary: Clustered object detections Simulink bus containing MATLAB structure
  direction: output
- name: Tracks
  summary: Object tracks Simulink bus containing MATLAB structure
  direction: output
- name: Detections
  summary: Unclustered object detections Simulink bus containing MATLAB structure
  direction: output
- name: Configuration
  summary: Current sensor configuration Simulink bus containing MATLAB structure
  direction: output
```

### Input

### **Platforms** — Target platform poses Simulink® bus containing MATLAB® structure

Target platform poses expressed in the reference platform coordinates, specified
as a Simulink bus containing a MATLAB structure. The reference platform is the
mounting platform of the radar sensor. For more details about buses, see Create Nonvirtual Buses (Simulink).
The structure has these fields.

| Field | Description |
| --- | --- |
| `NumPlatforms` | Number of platforms, specified as a nonnegative integer. |
| `Platforms` | Platforms poses, specified as an array of platform pose structures. The block reads only as many platform poses as the number of platforms specified in `NumPlatforms`. |

The fields of each platform pose structure are:

| Field | Description |
| --- | --- |
| `PlatformID` | Unique identifier for the target platform, specified as a positive integer. |
| `ClassID` | User-defined integer used to classify the type of target platform, specified as a nonnegative integer. `0` is reserved for unclassified platform types and is the default value. |
| `Position` | Position of target platform in the reference platform body frame, specified as a real-valued 1-by-3 vector. Units are in meters. |
| `Velocity` | Velocity of the target platform in the reference platform body frame, specified as a real-valued 1-by-3 vector. Units are in meters per second. |
| `Acceleration` | Acceleration of the target platform in the reference platform body frame, specified as a real-valued 1-by-3 vector. Units are in meters per second-squared. |
| `Orientation` | Orientation of the target platform with respect to the reference platform body frame, specified as a 3-by-3 rotation matrix. Orientation defines the frame rotation from the platform coordinate system to the target body coordinate system. |
| `AngularVelocity` | Angular velocity of the target platform in the reference platform body frame, specified as a real-valued 1-by-3 vector. The magnitude of the vector defines the angular speed. Units are in degrees per second. The default is `[0 0 0]`. |

You can use the Tracking Scenario
Reader block to generate target platform poses expressed in the scenario
frame. Then use the Scenario To
Platform block to obtain target platform poses in the reference platform
frame.

### **INS** — Radar reference platform pose from INS Simulink bus containing MATLAB structure

Radar reference platform pose information from an inertial navigation system
(INS), specified as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).
The structure includes pose information for the radar platform provided by the INS.
The INS structure has these fields.

|  |  |
| --- | --- |
| **Field** | **Definition** |
| `Position` | Position of the platform in the scenario frame, specified as a real-valued 1-by-3 vector. Units are in meters. |
| `Velocity` | Velocity of the platform in the scenario frame, specified as a real-valued 1-by-3 vector. Units are in m/s. |
| `Orientation` | Orientation of the platform body frame with respect to the scenario frame, specified as a 3-by-3 real-valued rotation matrix. The rotation is from the scenario frame to the platform body frame. This is also referred to as a parent-to-child rotation. |

#### Dependencies

To enable this port, select the **Enable INS** check
box.

### **Time** — Current simulation time nonnegative scalar

Current simulation time, specified as a nonnegative scalar. Note that the sensor
generates reports only at simulation times corresponding to integer multiples of the
update interval, which is the reciprocal of the specified **Update rate
(Hz)** parameter. Units are in seconds.

#### Dependencies

To enable this port, set the **Source of target truth time**
parameter to `Input port`.

If you do not enable this port, then the block uses the current Simulink
simulation time.

**Data Types:** `double`
### Output

### **Clustered Detections** — Clustered object detections Simulink bus containing MATLAB structure

Clustered object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).

With clustered detections, the block outputs a single detection per target, where
each detection is the centroid of the unclustered detections for that target.

The structure contains these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | Nonnegative integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures of length set by the **Maximum number of target reports** parameter. Only the first `NumDetections` of these are actual detections. |

Each object detection structure contains these fields.

| Fields | Definition |
| --- | --- |
| `Time` | Measurement time |
| `Measurement` | Object measurements |
| `MeasurementNoise` | Measurement noise covariance matrix |
| `SensorIndex` | Unique ID of the sensor |
| `ObjectClassID` | Object classification |
| `ObjectAttributes` | Additional information passed to tracker |
| `MeasurementParameters` | Parameters used by initialization functions of nonlinear Kalman tracking filters |

- For rectangular coordinates, the block reports `Measurement`
  and `MeasurementNoise` in the rectangular coordinate system
  specified by the **Coordinate system** parameter.
- For spherical coordinates, the block reports `Measurement` and
  `MeasurementNoise` in the spherical coordinate system
  specified by the **Coordinate system** parameter.

**`Measurement` and `MeasurementNoise`**

| **Coordinate System** | `Measurement` and `MeasurementNoise` Coordinates |
| --- | --- |
| Scenario | This table shows how coordinates are affected by the **Enable range rate measurements** parameter.  | **Enable range rate measurements** | Coordinates | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Body` |
| `Sensor rectangular` |
| `Sensor spherical` | This table shows how coordinates are affected by the **Enable elevation angle measurements** and **Enable range rate measurements** parameters.  | **Enable range rate measurements** | **Enable elevation angle measurements** | Coordinates | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` |  `az` is the azimuth angle, `el` is the elevation angle, `rng` is the range, and `rr` is the range rate. Units for angles are in degrees. |

The `ObjectAttributes` structure has these fields.

**`ObjectAttributes`**

| Attribute | Definition |
| --- | --- |
| `TargetIndex` | `PlatformID` of the target platform that corresponds to the detection, returned as a positive integer. For false alarms, this value is negative. |
| `SNR` | Signal-to-noise ratio of the detection. Units are in dB. |

The `MeasurementParameters` field can contain at least one
measurement parameter structure, representing the transformation from the platform body frame to
the sensor looking angle frame. If you specify the INS information through the
**INS** input port and you also specify the **Coordinate
system** parameter as `scenario`, the
`MeasurementParameters` field also contains an additional measurement
parameter structure, representing the transformation from the scenario frame to the reference
platform body frame. Each measurement parameter structure has these fields.

|  |  |
| --- | --- |
| **Field** | **Description** |
| `Frame` | Enumerated type indicating the frame used to report measurements. When detections are reported using a rectangular coordinate system, `Frame` is set to `'rectangular'`. When detections are reported in spherical coordinates, `Frame` is set to `'spherical'`. |
| `OriginPosition` | Position offset of the origin of the child frame relative to the parent frame, represented as a 3-by-1 vector. |
| `OriginVelocity` | Velocity offset of the origin of the child frame relative to the parent frame, represented as a 3-by-1 vector. |
| `Orientation` | 3-by-3 real-valued orthonormal frame rotation matrix. The direction of the rotation depends on the `IsParentTochild` field. |
| `IsParentToChild` | A logical scalar indicating if `Orientation` performs a frame rotation from the parent coordinate frame to the child coordinate frame. If `false`, `Orientation` instead performs a frame rotation from the child coordinate frame to the parent coordinate frame. |
| `HasElevation` | A logical scalar indicating if elevation is included in the measurement. For measurements reported in a rectangular frame, if `HasElevation` is `false`, the measurements are reported assuming 0 degrees of elevation. |
| `HasAzimuth` | A logical scalar indicating if azimuth is included in the measurement. |
| `HasRange` | A logical scalar indicating if range is included in the measurement. |
| `HasVelocity` | A logical scalar indicating if the reported detections include velocity measurements.  - For measurements reported in a rectangular frame, if   `HasVelocity` is   `false`, the measurements are reported   as `[x y z]`. If   `HasVelocity` is   `true`, measurements are reported as   `[x y z vx vy vz]`. - For measurements reported in a spherical frame, if   `HasVelocity` is   `false`, the measurements are reported   as `[az el rng]`. If   `HasVelocity` is   `true`, measurements are reported as   `[az;el;rng;rr]`. |

#### Dependencies

To enable this port, select the **Target reporting format**
parameter to `Clustered detections`.

### **Tracks** — Object tracks Simulink bus containing MATLAB structure

Object tracks, returned as a Simulink bus containing a MATLAB structure. See Create Nonvirtual Buses (Simulink).

Each structure has these fields.

| Field | Description |
| --- | --- |
| `NumTracks` | Number of tracks |
| `IsValidTime` | False when you request updates between block invocation intervals |
| `Tracks` | Array of track structures of a length set by the **Maximum number of target reports** parameter. Only the first `NumTracks` of these are actual tracks. |

This table shows the fields of each track structure.

| Field | Definition |
| --- | --- |
| `TrackID` | Unique track identifier used to distinguish multiple tracks. |
| `BranchID` | Unique track branch identifier used to distinguish multiple track branches. |
| `SourceIndex` | Unique source index used to distinguish tracking sources in a multiple tracker environment. |
| `UpdateTime` | Time at which the track is updated. Units are in seconds. |
| `Age` | Number of times the track was updated. |
| `State` | Value of state vector at the update time. |
| `StateCovariance` | Uncertainty covariance matrix of the state estimate error. |
| `ObjectClassID` | Integer value representing the object classification. The value `0` represents an unknown classification. Nonzero classifications apply only to confirmed tracks. |
| `TrackLogic` | Confirmation and deletion logic type. This value is always `'History'` for radar sensors, to indicate history-based logic. |
| `TrackLogicState` | Current state of the track logic type, returned as a 1-by-*K* logical array. *K* is the number of latest logical track states recorded. In the array, `1` denotes a hit and `0` denotes a miss. |
| `IsConfirmed` | Confirmation status. This field is `true` if the track is confirmed to be a real target. |
| `IsCoasted` | Coasting status. This field is `true` if the track is updated without a new detection. |
| `IsSelfReported` | Indicate if the track is reported by the tracker. This field is used in a track fusion environment. It is returned as `true` by default. |
| `ObjectAttributes` | Additional information about the track. |

For more details about these fields, see `objectTrack`.

The block outputs only confirmed tracks, which are tracks that are assigned at
least *M* detections during the first *N* updates
after track initialization. To specify the values *M* and
*N*, use the **M and N for the M-out-of-N
confirmation** parameter.

#### Dependencies

To enable this port, set the **Target reporting format**
parameter to `Tracks`.

### **Detections** — Unclustered object detections Simulink bus containing MATLAB structure

Unclustered object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, see Create Nonvirtual Buses (Simulink).

With unclustered detections, the block outputs all detections, and a target can
have multiple detections.

The structure contains these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | Nonnegative integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures of length set by the **Maximum number of target reports** parameter. Only the first `NumDetections` of these are actual detections. |

Each object detection structure contains these fields.

| Fields | Definition |
| --- | --- |
| `Time` | Measurement time |
| `Measurement` | Object measurements |
| `MeasurementNoise` | Measurement noise covariance matrix |
| `SensorIndex` | Unique ID of the sensor |
| `ObjectClassID` | Object classification |
| `ObjectAttributes` | Additional information passed to tracker |
| `MeasurementParameters` | Parameters used by initialization functions of nonlinear Kalman tracking filters |

- For rectangular coordinates, the block reports `Measurement`
  and `MeasurementNoise` in the rectangular coordinate system
  specified by the **Coordinate system** parameter.
- For spherical coordinates, the block reports `Measurement` and
  `MeasurementNoise` in the spherical coordinate system
  specified by the **Coordinate system** parameter.

**`Measurement` and `MeasurementNoise`**

| **Coordinate System** | `Measurement` and `MeasurementNoise` Coordinates |
| --- | --- |
| Scenario | This table shows how coordinates are affected by the **Enable range rate measurements** parameter.  | **Enable range rate measurements** | Coordinates | | --- | --- | | `on` | `[x;y;z;vx;vy;vz]` | | `off` | `[x;y;z]` | |
| `Body` |
| `Sensor rectangular` |
| `Sensor spherical` | This table shows how coordinates are affected by the **Enable elevation angle measurements** and **Enable range rate measurements** parameters.  | **Enable range rate measurements** | **Enable elevation angle measurements** | Coordinates | | --- | --- | --- | | `on` | `on` | `[az;el;rng;rr]` | | `on` | `off` | `[az;rng;rr]` | | `off` | `on` | `[az;el;rng]` | | `off` | `off` | `[az;rng]` |  `az` is the azimuth angle, `el` is the elevation angle, `rng` is the range, and `rr` is the range rate. Units for angles are in degrees. |

The `ObjectAttributes` structure has these fields.

**`ObjectAttributes`**

| Attribute | Definition |
| --- | --- |
| `TargetIndex` | `PlatformID` of the target platform that corresponds to the detection, returned as a positive integer. For false alarms, this value is negative. |
| `SNR` | Signal-to-noise ratio of the detection. Units are in dB. |

The `MeasurementParameters` field can contain at least one
measurement parameter structure, representing the transformation from the platform body frame to
the sensor looking angle frame. If you specify the INS information through the
**INS** input port and you also specify the **Coordinate
system** parameter as `scenario`, the
`MeasurementParameters` field also contains an additional measurement
parameter structure, representing the transformation from the scenario frame to the reference
platform body frame. Each measurement parameter structure has these fields.

|  |  |
| --- | --- |
| **Field** | **Description** |
| `Frame` | Enumerated type indicating the frame used to report measurements. When detections are reported using a rectangular coordinate system, `Frame` is set to `'rectangular'`. When detections are reported in spherical coordinates, `Frame` is set to `'spherical'`. |
| `OriginPosition` | Position offset of the origin of the child frame relative to the parent frame, represented as a 3-by-1 vector. |
| `OriginVelocity` | Velocity offset of the origin of the child frame relative to the parent frame, represented as a 3-by-1 vector. |
| `Orientation` | 3-by-3 real-valued orthonormal frame rotation matrix. The direction of the rotation depends on the `IsParentTochild` field. |
| `IsParentToChild` | A logical scalar indicating if `Orientation` performs a frame rotation from the parent coordinate frame to the child coordinate frame. If `false`, `Orientation` instead performs a frame rotation from the child coordinate frame to the parent coordinate frame. |
| `HasElevation` | A logical scalar indicating if elevation is included in the measurement. For measurements reported in a rectangular frame, if `HasElevation` is `false`, the measurements are reported assuming 0 degrees of elevation. |
| `HasAzimuth` | A logical scalar indicating if azimuth is included in the measurement. |
| `HasRange` | A logical scalar indicating if range is included in the measurement. |
| `HasVelocity` | A logical scalar indicating if the reported detections include velocity measurements.  - For measurements reported in a rectangular frame, if   `HasVelocity` is   `false`, the measurements are reported   as `[x y z]`. If   `HasVelocity` is   `true`, measurements are reported as   `[x y z vx vy vz]`. - For measurements reported in a spherical frame, if   `HasVelocity` is   `false`, the measurements are reported   as `[az el rng]`. If   `HasVelocity` is   `true`, measurements are reported as   `[az;el;rng;rr]`. |

#### Dependencies

To enable this port, set the **Target reporting format**
parameter to `Detections`.

### **Configuration** — Current sensor configuration Simulink bus containing MATLAB structure

Configuration, returned as a Simulink bus containing a MATLAB structure. You can use this port to determine objects falling within the
radar beam during object execution. The structure has these fields:

| Field | Description | Type |
| --- | --- | --- |
| `NumConfigurations` | Number of valid configurations | integer |
| `Configurations` | Configuration structures | Array of `NumConfigurations` configuration structures |

The configuration structure has these fields.

|  |  |
| --- | --- |
| **Field** | **Description** |
| `SensorIndex` | Unique sensor index, returned as a positive integer. |
| `IsValidTime` | Valid detection time, returned as `true` or `false`. `IsValidTime` is `false` when detection updates are requested between update intervals specified by the update rate. |
| `IsScanDone` | `IsScanDone` is `true` when the sensor has completed a scan. |
| `FieldOfView` | Field of view of the sensor, returned as a 2-by-1 vector of positive real values, [`azfov`;`elfov`]. `azfov` and `elfov` represent the field of view in azimuth and elevation, respectively. Units are in degrees. |
| `RangeLimits` | Minimum and maximum range of the sensor, in meters, specified as a 1-by-2 nonnegative real-valued vector of the form `[rmin,rmax]`. Units are in meters. |
| `RangeRateLimits` | Minimum and maximum range rate of the sensor, in meters per second, specified as a 1-by-2 real-valued vector of the form `[rrmin,rrmax]`. Units are in meters. |
| `MeasurementParameters` | Sensor measurement parameters, returned as an array of structures containing the coordinate frame transforms needed to transform positions and velocities in the top-level frame to the current sensor frame. For details on `MeasurementParameters`, see `Measurement Parameters`. |

#### Dependencies

To enable this port, select the **Enable radar configuration
output** check box.
## Parameters
```yaml
parameters:
- name: Unique identifier of sensor
  summary: Unique sensor identifier 0 (default) | positive integer
  group: Parameters
- name: Update rate (Hz)
  summary: Sensor update rate 10 (default) | positive real scalar
  group: Parameters
- name: Translation [ X, Y, Z ] relative to platform origin (m)
  summary: Mounting location of radar on platform [0,0,0] (default) | 1-by-3 real-valued vector of form [x,y,z]
  group: Parameters
- name: Rotation [Yaw,Pitch,Roll] relative to platform's frame (deg)
  summary: Mounting angles of radar [0 0 0] (default) | 1-by-3 real-valued vector of form [*z*yaw *y*pitch *x*roll]
  group: Parameters
- name: Enable elevation angle measurements
  summary: Enable radar to measure target elevation angles off (default) | on
  group: Parameters
- name: Enable range rate measurements
  summary: Enable radar to measure target range rates off (default) | on
  group: Parameters
- name: Add noise to measurements
  summary: Enable addition of noise to radar sensor measurements on (default) | off
  group: Parameters
- name: Enable false reports
  summary: Enable creating false alarm radar detections on (default) | off
  group: Parameters
- name: Enable occlusion
  summary: Enable line-of-sight occlusion on (default) | off
  group: Parameters
- name: Maximum number of target reports
  summary: Maximum number of detections or tracks 100 (default) | positive integer
  group: Parameters
- name: Target reporting format
  summary: Format of generated target reports Clustered detections (default) | Tracks | Detections
  group: Parameters
- name: Coordinate system
  summary: Coordinate system of reported detections Body (default) | Sensor rectangular | Sensor spherical | Scenario
  group: Parameters
- name: Source of target truth time
  summary: Source of target truth time Auto (default) | Input port
  group: Parameters
- name: Enable INS
  summary: Enable INS input port off (default) | on
  group: Parameters
- name: Source of output target report bus name
  summary: Source of output target report bus name Auto (default) | Property
  group: Parameters
- name: Specify an output target report bus name
  summary: Name of target report output bus BusFusionRadarSensor (default) | valid bus name
  group: Parameters
- name: Enable radar configuration output
  summary: Enable radar configuration output off (default) | on
  group: Parameters
- name: Source of output config bus name
  summary: Source of output config bus name Auto (default) | Property
  group: Parameters
- name: Specify an output config bus name
  summary: Name of sensor configuration output bus BusFusionRadarSensorConfig (default) | valid bus name
  group: Parameters
- name: Azimuth resolution (deg)
  summary: Azimuth resolution of radar 1 (default) | positive scalar
  group: Measurements
- name: Elevation resolution (deg)
  summary: Elevation resolution of radar 5 (default) | positive scalar
  group: Measurements
- name: Range resolution (m)
  summary: Range resolution of radar 100 (default) | positive real scalar
  group: Measurements
- name: Range rate resolution (m/s)
  summary: Range rate resolution of radar 10 (default) | positive real scalar
  group: Measurements
- name: Azimuth bias fraction
  summary: Azimuth bias fraction of radar 0.1 (default) | nonnegative scalar
  group: Measurements
- name: Elevation bias fraction
  summary: Elevation bias fraction of radar 0.1 (default) | nonnegative scalar
  group: Measurements
- name: Range bias fraction
  summary: Range bias fraction 0.05 (default) | nonnegative scalar
  group: Measurements
- name: Range rate bias fraction
  summary: Range rate bias fraction 0.05 (default) | nonnegative scalar
  group: Measurements
- name: Total angular field of view [AZ, EL] (deg)
  summary: Angular field of view of radar [1 5] (default) | 1-by-2 positive real-valued vector of form [azfov,elfov]
  group: Measurements
- name: Range limits [MIN, MAX] (m)
  summary: Minimum and maximum range of radar [0 100e3] (default) | 1-by-2 nonnegative real-valued vector of form [min max]
  group: Measurements
- name: Range rate limits [MIN, MAX] (m/s)
  summary: Minimum and maximum range rate of radar (m/s) [-200, 200] (default) | 1-by-2 real-valued vector of form [min max]
  group: Measurements
- name: Detection probability
  summary: Probability of detecting a target 0.9 (default) | scalar in range (0, 1]
  group: Measurements
- name: False alarm rate
  summary: False alarm report rate 1e-06 (default) | positive real scalar in range [10–7, 10–3]
  group: Measurements
- name: Reference target range (m)
  summary: Reference target range 1000e3 (default) | positive real scalar
  group: Measurements
- name: Reference target RCS (dBsm)
  summary: Reference target radar cross-section 0 (default) | real scalar
  group: Measurements
- name: Center frequency (Hz)
  summary: Center frequency of radar band 300e6 (default) | positive real scalar
  group: Measurements
- name: Filter initialization function name
  summary: Kalman filter initialization function initcvekf (default) | function name
  group: Measurements
- name: M and N for the M-out-of-N confirmation
  summary: Threshold for track confirmation [2 3] (default) | 1-by-2 vector of positive integers
  group: Measurements
- name: P and R for the P-out-of-R deletion
  summary: Threshold for track deletion [5 5] (default) | 1-by-2 vector of positive integers
  group: Measurements
- name: Random number generation
  summary: Method to specify random number generator seed Repeatable (default) | Specify seed | Not repeatable
  group: Measurements
- name: Initial seed
  summary: Random number generator seed 0 (default) | nonnegative integer less than 232
  group: Measurements
- name: Target profiles definition
  summary: Method to specify target profiles From Scenario Reader block (default) | MATLAB expression | Parameters
  group: Target Profiles
- name: MATLAB expression for target profiles
  summary: MATLAB expression for target profiles MATLAB structure | MATLAB structure array | valid MATLAB expression
  group: Target Profiles
- name: Unique target identifiers
  summary: Scenario-defined target identifier [] (default) | positive integer | length-*L* vector of unique positive integers
  group: Target Profiles
- name: Target classification identifiers
  summary: User-defined classification identifier 0 (default) | integer | length-*L* vector of integers
  group: Target Profiles
- name: Length of target cuboids (m)
  summary: Length of target cuboids 0 (default) | positive real scalar | length-*L* vector of positive values
  group: Target Profiles
- name: Width of target cuboids (m)
  summary: Width of target cuboids 0 (default) | positive real scalar | length-*L* vector of positive values
  group: Target Profiles
- name: Height of target cuboids (m)
  summary: Height of target cuboids 0 (default) | positive real scalar | length-*L* vector of positive values
  group: Target Profiles
- name: Rotational center of target cuboids (m)
  summary: Rotational center of target cuboids {[0, 0, 0]} (default) | length-*L* cell array of real-valued 1-by-3 vectors
  group: Target Profiles
- name: Target signatures
  summary: Target signatures {rcsSignature} (default) | length-*L* cell array
  group: Target Profiles
```

### Parameters

#### Sensor Identification

### **Unique identifier of sensor** — Unique sensor identifier `0` (default) | positive integer

Unique sensor identifier, specified as a positive integer. Use this parameter to
distinguish between detections or tracks that come from different sensors in a
multisensor system. Specify a unique value for each sensor. If you do not update
**Unique identifier of sensor** from the default value of
`0`, then the radar returns an error at the start of
simulation.

### **Update rate (Hz)** — Sensor update rate `10` (default) | positive real scalar

Sensor update rate, specified as a positive real scalar. The radar generates new
reports at intervals defined by the reciprocal of this value. For example, if the
update rate is `10` Hz, then the sensor generates detections every
0.1 seconds. A sensor update request between update intervals contains no detections
or tracks. Units are in Hz.

#### Sensor Mounting

### **Translation [ X, Y, Z ] relative to platform origin (m)** — Mounting location of radar on platform `[0,0,0]` (default) | 1-by-3 real-valued vector of form `[x,y,z]`

Sensor location of the radar on the reference platform, specified as a 1-by-3
real-valued vector of the form `[x,y,z]`. This parameter defines the
coordinates of the sensor along the *x*-axis,
*y*-axis, and *z*-axis relative to the platform
origin. Units are in meters.

### **Rotation [Yaw,Pitch,Roll] relative to platform's frame (deg)** — Mounting angles of radar `[0 0 0]` (default) | 1-by-3 real-valued vector of form [*z*yaw *y*pitch *x*roll]

Mounting angles of the radar, specified as a 1-by-3 real-valued vector of form
[*z*yaw
*y*pitch
*x*roll]. This parameter defines the intrinsic
Euler angle rotation of the sensor around the *z*-axis,
*y*-axis, and *x*-axis with respect to the
platform frame, where:

- *z*yaw, or *yaw
  angle*, rotates the sensor around the *z*-axis of
  the platform frame.
- *y*pitch, or *pitch
  angle*, rotates the sensor around the *y*-axis of
  the platform frame. This rotation is relative to the sensor position that results
  from the *z*yaw rotation.
- *x*roll, or *roll
  angle*, rotates the sensor about the *x*-axis of the
  platform frame. This rotation is relative to the sensor position that results from
  the *z*yaw and
  *y*pitch rotations.

Units are in degrees.

#### Detection Reporting

### **Enable elevation angle measurements** — Enable radar to measure target elevation angles `off` (default) | `on`

Select this check box to model a radar sensor that can measure target
elevation.

### **Enable range rate measurements** — Enable radar to measure target range rates `off` (default) | `on`

Select this check box to enable the radar to measure range rates from target
detections.

### **Add noise to measurements** — Enable addition of noise to radar sensor measurements `on` (default) | `off`

Select this parameter to add noise to the radar measurements. Otherwise, the
measurements have no noise. Even if you clear this parameter, the measurement noise
covariance matrix, which is reported in the `MeasurementNoise` field
of the generated detections output, represents the measurement noise that is added
when **Add noise to measurements** is selected.

### **Enable false reports** — Enable creating false alarm radar detections `on` (default) | `off`

Select this parameter to enable creating false alarm radar measurements. If you
clear this parameter, the radar reports only actual detections.

### **Enable occlusion** — Enable line-of-sight occlusion `on` (default) | `off`

Select this parameter to enable line-of-sight occlusion from extended objects. If
you enable this parameter, the sensor models two types of occlusion, self occlusion
and inter-object occlusion. Self occlusion occurs when one side of an extended object
occludes another side. Inter-object occlusion occurs when one extended object stands
in the line of sight of another extended object or a point target. Both extended
objects and point targets can be occluded by extended objects, but a point target
cannot occlude another point target or an extended object.

### **Maximum number of target reports** — Maximum number of detections or tracks `100` (default) | positive integer

Maximum number of detections or tracks that the sensor reports, specified as a
positive integer. The sensor reports detections in order of increasing distance from
the sensor until reaching this maximum number.

### **Target reporting format** — Format of generated target reports `Clustered detections` (default) | `Tracks` | `Detections`

Format of generated target reports, specified as one of these options:

- **Clustered detections** — The block generates target reports
  as *clustered detections*, where each target is reported as a
  single detection that is the centroid of the unclustered target detections. The
  block returns clustered detections at the **Clustered
  detections** output port.
- **Tracks** — The block generates target reports as
  *tracks*, which are clustered detections that have been
  processed by a tracker. The block returns tracks at the
  **Tracks** output port.
- **Detections** — The block generates target reports as
  *unclustered detections*, where each target can have
  multiple detections. The block returns clustered detections at the
  **Detections** output port.

### **Coordinate system** — Coordinate system of reported detections `Body` (default) | `Sensor rectangular` | `Sensor spherical` | `Scenario`

Coordinate system of reported detections, specified as one of these options:

- `Body` — Detections are reported in the rectangular
  body system of the sensor platform.
- `Sensor rectangular` — Detections are reported in
  the sensor rectangular body coordinate system.
- `Sensor spherical` — Detections are reported in a
  spherical coordinate system that is centered at the radar sensor and aligned
  with the orientation of the radar on the platform.
- `Scenario` — Detections are reported in the
  rectangular scenario coordinate frame. To use this option, you must specify the
  **INS** input port.

#### Inputs and Outputs

### **Source of target truth time** — Source of target truth time `Auto` (default) | `Input port`

Source of target truth time, specified as one of these options:

- `Auto` — The block uses the current Simulink simulation time.
- `Input port` — The block uses the time provided on
  the `Time` input port of the block.

### **Enable INS** — Enable INS input port `off` (default) | `on`

Select this parameter to allow input of INS data using the
**INS** input port.

### **Source of output target report bus name** — Source of output target report bus name `Auto` (default) | `Property`

Source of the output target report bus name, specified as one of these
options:

- `Auto` — The block automatically creates a bus
  name.
- `Property` — Specify the bus name by using the
  **Specify an output target report bus name** parameter.

This bus name applies to the  **Clustered detections**,
**Tracks**, and **Detections** output
ports.

### **Specify an output target report bus name** — Name of target report output bus `BusFusionRadarSensor` (default) | valid bus name

Name of the target report bus to be returned in the output port, specified as a
valid bus name. This bus name applies to the  **Clustered
detections**, **Tracks**, and
**Detections** output ports.

#### Dependencies

To enable this parameter, set the **Source of output target report bus
name** parameter to `Property`.

### **Enable radar configuration output** — Enable radar configuration output `off` (default) | `on`

Enable the **Configuration** output port.

### **Source of output config bus name** — Source of output config bus name `Auto` (default) | `Property`

Source of bus name of the **Configuration** output port,
specified as one of these options:

- `Auto` — The block automatically creates a bus
  name.
- `Property` — Specify the bus name by using the
  **Specify an output config bus name** parameter.

#### Dependencies

To enable this parameter, select the **Enable radar configuration
output** check box.

### **Specify an output config bus name** — Name of sensor configuration output bus `BusFusionRadarSensorConfig` (default) | valid bus name

Specify the name of the radar configuration bus returned in the
**Configuration** output port.

#### Dependencies

To enable this parameter, set the **Source of output config bus
name** parameter to `Property`.

### Measurements

#### Resolution settings

### **Azimuth resolution (deg)** — Azimuth resolution of radar `1` (default) | positive scalar

Azimuth resolution of the radar, specified as a positive scalar. The
*azimuth resolution* defines the minimum separation in the
azimuth angle at which the radar can distinguish between two targets. The azimuth
resolution is typically the 3 dB downpoint of the azimuth angle beamwidth of the
radar. Units are in degrees.

### **Elevation resolution (deg)** — Elevation resolution of radar `5` (default) | positive scalar

Elevation resolution of the radar, specified as a positive scalar. The
*elevation resolution* defines the minimum separation in the
elevation angle at which the radar can distinguish between two targets. The elevation
resolution is typically the 3 dB downpoint of the elevation angle beamwidth of the
radar. Units are in degrees.

#### Dependencies

To enable this parameter, select the **Enable elevation angle
measurements** check box.

### **Range resolution (m)** — Range resolution of radar `100` (default) | positive real scalar

Range resolution of the radar in meters, specified as a positive real scalar. The
*range resolution* defines the minimum separation in the range
at which the radar can distinguish between two targets. Units are in meters.

### **Range rate resolution (m/s)** — Range rate resolution of radar `10` (default) | positive real scalar

Range rate resolution of the radar, specified as a positive real scalar. The
*range rate resolution* defines the minimum separation in the
range rate at which the radar can distinguish between two targets. Units are in meters
per second.

#### Dependencies

To enable this parameter, on the **Parameters** tab, select the
**Enable range rate measurements** check box.

#### Bias settings

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
resolution (m)** property. This parameter sets a lower bound on the range
accuracy of the radar and is dimensionless.

### **Range rate bias fraction** — Range rate bias fraction `0.05` (default) | nonnegative scalar

Range rate bias fraction of the radar, specified as a nonnegative scalar. Range
rate bias is expressed as a fraction of the range rate resolution specified by the
**Range rate resolution (m/s)** parameter. This parameter sets a
lower bound on the range rate accuracy of the radar and is dimensionless.

#### Dependencies

To enable this parameter, select the **Enable range rate
measurements** check box.

#### Detector settings

### **Total angular field of view [AZ, EL] (deg)** — Angular field of view of radar `[1 5]` (default) | 1-by-2 positive real-valued vector of form `[azfov,elfov]`

Angular field of view of the radar, specified as a 1-by-2 positive real-valued
vector of the form `[azfov elfov]`. The field of view defines the
angular extent spanned by the sensor. The azimuth field of view
`azfov` must lie in the interval (0, 360]. The elevation field of
view `elfov` must lie in the interval (0, 180]. Units are in
degrees

### **Range limits [MIN, MAX] (m)** — Minimum and maximum range of radar `[0 100e3]` (default) | 1-by-2 nonnegative real-valued vector of form `[min max]`

Minimum and maximum range of the radar, specified as a 1-by-2 nonnegative
real-valued vector of the form `[min max]`. The radar does not detect
targets that are outside this range. The maximum range `max` must be
greater than the minimum range `min`. Units are in meters.

### **Range rate limits [MIN, MAX] (m/s)** — Minimum and maximum range rate of radar (m/s) `[-200, 200]` (default) | 1-by-2 real-valued vector of form `[min max]`

Minimum and maximum range rate of radar, specified as a 1-by-2 real-valued vector
of the form `[min max]`. The radar does not detect targets that are
outside this range rate. The maximum range rate `max` must be greater
than the minimum range rate `min`. Units are in meters per
second.

#### Dependencies

To enable this parameter, select the **Enable range rate
measurements** check box.

### **Detection probability** — Probability of detecting a target `0.9` (default) | scalar in range (0, 1]

Probability of detecting a target, specified as a scalar in the range (0, 1]. This
parameter defines the probability of detecting a target that has a radar cross-section
(RCS) specified by the **Reference target RCS (dBsm)** parameter and
is at the range specified by the **Reference target range (m)**
parameter. Units are dimensionless.

### **False alarm rate** — False alarm report rate `1e-06` (default) | positive real scalar in range [10–7, 10–3]

False alarm report rate within each radar resolution cell, specified as a positive
real scalar in the range [10–7,
10–3]. The block determines resolution cells from the
**Azimuth resolution (deg)** and **Range resolution
(m)** parameters and, when enabled, from the **Elevation resolution
(deg)** and **Range rate resolution (m/s)** parameters.
Units are dimensionless.

### **Reference target range (m)** — Reference target range `1000e3` (default) | positive real scalar

Reference target range for the given probability of detection and the given
reference radar cross-section (RCS), specified as a positive real scalar. The
*reference range* is the range at which a target having a radar
cross-section specified by the **Reference target RCS (dBsm)**
parameter is detected with a probability of detection specified by the
**Detection probability** parameter. Units are in meters.

### **Reference target RCS (dBsm)** — Reference target radar cross-section `0` (default) | real scalar

Reference target radar cross-section (RCS) for a given probability of detection
and reference range, specified as a real scalar. The *reference
RCS* is the RCS value at which a target is detected with a probability
specified by the **Detection probability** parameter at the specified
**Reference target range (m)** parameter value. Values are
expressed in dBsm.

### **Center frequency (Hz)** — Center frequency of radar band `300e6` (default) | positive real scalar

Center frequency of the radar band, specified as a positive scalar. Units are in
Hz.

#### Tracker Setting

### **Filter initialization function name** — Kalman filter initialization function `initcvekf` (default) | function name

Kalman filter initialization function, specified as the name of a valid Kalman
filter initialization function.

This table shows the initialization functions you can use to specify
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

You can also write your own initialization function. The function must have this
syntax.

```
filter = filterInitializationFcn(detection)
```

The
input to this function is a detection report like those created by an `objectDetection` object. The output of this function must be a tracking
filter object, such as `trackingKF`, `trackingEKF`, `trackingUKF`, or `trackingABF`.

To guide you in writing this function, you can examine the details of one of the
functions in the table in MATLAB.

```
type initcvekf
```

#### Dependencies

To enable this parameter, set the **Target reporting format**
parameter to `Tracks`.

### **M and N for the M-out-of-N confirmation** — Threshold for track confirmation `[2 3]` (default) | 1-by-2 vector of positive integers

Threshold for track confirmation, specified as a 1-by-2 vector of positive
integers of the form `[M N]`. A track is confirmed if it receives at
least `M` detections in the last `N` updates.
`M` must be less than or equal to `N`.

- When setting `M`, take into account the probability of
  object detection for the sensors. The probability of detection depends on
  factors such as occlusion or clutter. You can reduce `M` when
  tracks fail to be confirmed or increase `M` when too many false
  detections are assigned to tracks.
- When setting `N`, consider the number of times you want the
  tracker to update before it makes a confirmation decision. For example, if a
  tracker updates every 0.05 seconds, and you want to allow 0.5 seconds to make a
  confirmation decision, set `N = 10`.

#### Dependencies

To enable this parameter, set the **Target reporting format**
parameter to `Tracks`.

### **P and R for the P-out-of-R deletion** — Threshold for track deletion `[5 5]` (default) | 1-by-2 vector of positive integers

Threshold for track deletion, specified as a 1-by-2 vector of positive integers of
the form `[P R]`. If a confirmed track is not assigned to any
detection `P` times in the last `R` tracker updates,
then the track is deleted. `P` must be less than or equal to
`R`.

- To reduce how long the radar maintains tracks, decrease `R`
  or increase `P`.
- To maintain tracks for a longer time, increase `R` or
  decrease `P`.

#### Dependencies

To enable this parameter, set the **Target reporting format**
parameter to `Tracks`.

#### Random Number Generator Settings

### **Random number generation** — Method to specify random number generator seed `Repeatable` (default) | `Specify seed` | `Not repeatable`

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

To enable this parameter, set the **Random number generation**
parameter to `Specify seed`.

### Target Profiles

### **Target profiles definition** — Method to specify target profiles `From Scenario Reader block` (default) | `MATLAB expression` | `Parameters`

Method to specify target profiles, specified as one of
`Parameters`, `MATLAB expression`,
`From Scenario Reader block`. Profiles are the physical and
radar characteristics of targets in the scenario.

- `Parameters` — The block obtains the target
  profiles from these parameters:

  - **Unique target identifiers**
  - **Target classification identifiers**
  - **Length of target cuboids (m)**
  - **Width of target cuboids (m)**
  - **Height of target cuboids (m)**
  - **Rotational center of target cuboids (m)**
  - **Target signatures**
- `MATLAB expression` — The block obtains the target
  profiles from the MATLAB expression specified by the **MATLAB expression for target
  profiles** parameter.
- `From Scenario Reader block` — The block obtains
  the platforms profiles from the Tracking
  Scenario Reader block.

### **MATLAB expression for target profiles** — MATLAB expression for target profiles MATLAB structure | MATLAB structure array | valid MATLAB expression

Specify the MATLAB expression for target profiles, as a MATLAB structure, a MATLAB structure array, or a valid MATLAB expression that produces such a structure or structure array.

You can use the outputs from the `platformProfiles` object function of the `trackingScenario` object to specify target profiles.

The default target profile expression produces a MATLAB structure and has this form.

```
struct('ClassID',0,'Dimensions', ...
'Length',0,'Width',0,'Height',0,'OriginOffset',[0 0 0]), ...
'Signatures',{rcsSignature})
```

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `MATLAB
expression`.

### **Unique target identifiers** — Scenario-defined target identifier `[]` (default) | positive integer | length-*L* vector of unique positive integers

Specify the scenario-defined target identifier as a positive integer or
length-*L* vector of unique positive integers. *L*
must equal the number of targets input into the **Platforms** input
port. The vector elements must match `PlatformID` values of the
targets. You can specify **Unique target identifiers** as
`[]`. In this case, the same target profile parameters apply to all
targets.

**Example:** `[1 2]`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Target classification identifiers** — User-defined classification identifier `0` (default) | integer | length-*L* vector of integers

Specify the user-defined classification identifier as an integer or
length-*L* vector of integers. When **Unique target
identifiers** is a vector, this parameter is a vector of the same length
with elements in one-to-one correspondence to the targets in **Unique target
identifiers**. When **Unique target identifiers** is
empty, `[]`, you must specify this parameter as a single integer
whose value applies to all targets.

**Example:** `2`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Length of target cuboids (m)** — Length of target cuboids `0` (default) | positive real scalar | length-*L* vector of positive values

Specify the length of target cuboids as a positive real scalar or
length-*L* vector of positive values. When **Unique target
identifiers** is a vector, this parameter is a vector of the same length
with elements in one-to-one correspondence to the targets in **Unique target
identifiers**. When **Unique target identifiers** is
empty, `[]`, you must specify this parameter as a positive real
scalar whose value applies to all targets. Units are in meters.

**Example:** `6.3`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Width of target cuboids (m)** — Width of target cuboids `0` (default) | positive real scalar | length-*L* vector of positive values

Specify the width of target cuboids as a positive real scalar or
length-*L* vector of positive values. When **Unique target
identifiers** is a vector, this parameter is a vector of the same length
with elements in one-to-one correspondence to the targets in **Unique target
identifiers**. When **Unique target identifiers** is
empty, `[]`, you must specify this parameter as a positive real
scalar whose value applies to all targets. Units are in meters.

**Example:** `4.7`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Height of target cuboids (m)** — Height of target cuboids `0` (default) | positive real scalar | length-*L* vector of positive values

Specify the height of target cuboids as a positive real scalar or
length-*L* vector of positive values. When **Unique target
identifiers** is a vector, this parameter is a vector of the same length
with elements in one-to-one correspondence to the targets in **Unique target
identifiers**. When **Unique target identifiers** is
empty, `[]`, you must specify this parameter as a positive real
scalar whose value applies to all targets. Units are in meters.

**Example:** `2.0`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Rotational center of target cuboids (m)** — Rotational center of target cuboids `{[0, 0, 0]}` (default) | length-*L* cell array of real-valued 1-by-3 vectors

Specify the rotational center of target cuboids as a length-*L*
cell array of real-valued 1-by-3 vectors. Each vector represents the offset of the
rotational center of a target cuboid from the center of the target. The center of
rotation is defined according to the convention detailed in the Dimensions property of the platform input argument. When
**Unique target identifiers** is a vector, this parameter is a cell
array of vectors with cells in one-to-one correspondence to the targets in
**Unique target identifiers**. When **Unique target
identifiers** is empty, `[]`, you must specify this
parameter as a cell array of one element containing an offset vector whose values
apply to all targets. Units are in meters.

**Example:** `{[-1.35, 0.2, 0.3]}`

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.

### **Target signatures** — Target signatures `{rcsSignature}` (default) | length-*L* cell array

Target signatures, specified as a length-*L* cell array of `rcsSignature` objects
that specify the RCS signatures of the targets. *L* is the number of
targets specified in the **Platforms** input port.

#### Dependencies

To enable this parameter, set the **Target profiles
definition** parameter to `Parameters`.
## Libraries

Sensor Fusion and Tracking Toolbox / Tracking Scenario and Sensor Models

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

### R2023a: Simulink buses do not show in workspace

As of R2023a, the Simulink buses created by this block no longer show in MATLAB workspace.

## Description

Generate radar sensor detections and tracks

The Fusion Radar Sensor block reads target platform poses and generates
detection and track reports from targets based on a radar sensor model. Currently, the
Fusion Radar Sensor block supports only non-scanning mode. The Fusion
Radar Sensor block can generate clustered or unclustered detections with added
random noise and can also generate false alarm detections. You can also generate tracks from
the Fusion Radar Sensor block. Use the **Target reporting
format** parameter to specify sensor outputs as clustered detections, unclustered
detections, or tracks.
