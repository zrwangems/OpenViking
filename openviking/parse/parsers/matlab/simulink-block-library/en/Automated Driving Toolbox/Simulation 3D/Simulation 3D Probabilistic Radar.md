---
type: simulink-block
title: 'Simulation 3D Probabilistic Radar'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dprobabilisticradar'
documentation_source_path: 'ref/simulation3dprobabilisticradar.html'
language: en
---

# Simulation 3D Probabilistic Radar

## Ports
```yaml
ports:
- name: Detections
  summary: Object detections Simulink bus containing MATLAB® structure
  direction: output
```

### Output

### **Detections** — Object detections Simulink bus containing MATLAB® structure

Object detections, returned as a Simulink bus containing a MATLAB structure. For more details about buses, Create Nonvirtual Buses (Simulink).
The structure has this form.

| Field | Description | Type |
| --- | --- | --- |
| `NumDetections` | Number of detections | integer |
| `IsValidTime` | False when updates are requested at times that are between block invocation intervals | Boolean |
| `Detections` | Object detections | Array of object detection structures of length set by the **Maximum reported** parameter. Only `NumDetections` of these detections are actual detections. |

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

- For Cartesian coordinates, `Measurement` and
  `MeasurementNoise` are reported in the coordinate system
  specified by the **Coordinate system** parameter.
- For spherical coordinates, `Measurement` and
  `MeasurementNoise` are reported in the spherical coordinate
  system based on the sensor Cartesian coordinate system.
  `MeasurementParameters` is reported in sensor Cartesian
  coordinates.

**Measurement and MeasurementNoise**

| **Coordinate System Used to Report Detections** | Measurement and MeasurementNoise Coordinates |
| --- | --- |
| `'Ego Cartesian'` | This table shows the coordinate dependence when you enable or disable range rate measurements using the **Enable range rate measurements** parameter.  | Range rate measurements | Coordinates | | --- | --- | | Enabled | `[x;y;z;vx;vy;vz]` | | Disabled | `[x;y;z]` | |
| `'Sensor Cartesian'` |
| `'Sensor spherical'` | This table shows the coordinate dependence when you enable or disable the range rate and elevation angle measurements, by using the **Enable range rate measurements** and **Enable elevation angle measurements** parameters, respectively.  | Range rate measurements | Elevation angle measurements | Coordinates | | --- | --- | --- | | Enabled | Enabled | `[az;el;rng;rr]` | | Enabled | Disabled | `[az;rng;rr]` | | Disabled | Enabled | `[az;el;rng]` | | Disabled | Disabled | `[az;rng]` | |

**Measurement Parameters**

| Parameter | Definition |
| --- | --- |
| `Frame` | Enumerated type that indicates the frame used to report measurements. When `Frame` is set to `'rectangular'`, detections are reported in Cartesian coordinates. When `Frame` is set to `'spherical'`, detections are reported in spherical coordinates. |
| `OriginPosition` | 3D vector offset of the sensor origin from the ego vehicle origin. The vector is derived from the location and height of the sensor, as specified by the **Mounting location** parameter and the *Z* value of the **Relative translation [X, Y, Z] (m)** parameter, respectively. |
| `Orientation` | Orientation of the radar sensor coordinate system with respect to the ego vehicle coordinate system. The orientation is derived from the roll, pitch, and yaw values specified in the **Relative rotation [Roll, Pitch, Yaw] (deg)** parameter. |
| `HasVelocity` | Indicates whether measurements contain velocity or range rate components. |
| `HasElevation` | Indicates whether measurements contain elevation components. |

The `ObjectAttributes` property of each detection is a
structure with these fields.

| Field | Definition |
| --- | --- |
| `TargetIndex` | Identifier of the actor, `ActorID`, that generated the detection. For false alarms, this value is negative. |
| `SNR` | Signal-to-noise ratio of the detection. Units are in decibels. |

The `ObjectClassID` property of each detection has a value that
corresponds to an object ID. The table shows the object IDs used in the default scenes
that are selectable from the Simulation 3D Scene
Configuration block. If you are using a custom scene, in the Unreal® Editor, you can assign new object types to unused IDs. For more details,
see Apply Labels to Unreal Scene Elements for Semantic Segmentation and Object Detection. If a scene
contains an object that does not have an assigned ID, that object is assigned an ID of
`0`. The detection of lane markings is not supported.

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
## Parameters
```yaml
parameters:
- name: Sensor identifier
  summary: Unique sensor identifier 1 (default) | positive integer
  group: Mounting
- name: Parent name
  summary: Name of parent vehicle Scene Origin (default) | vehicle name
  group: Mounting
- name: Mounting location
  summary: Sensor mounting location Origin (default) | Front bumper | Rear bumper | Right mirror | Left mirror | Rearview
    mirror | Hood center | Roof center | ...
  group: Mounting
- name: Specify offset
  summary: Specify offset from mounting location off (default) | on
  group: Mounting
- name: Relative translation [X, Y, Z] (m)
  summary: Translation offset relative to mounting location [0, 0, 0] (default) | real-valued 1-by-3 vector
  group: Mounting
- name: Relative rotation [Roll, Pitch, Yaw] (deg)
  summary: Rotational offset relative to mounting location [0, 0, 0] (default) | real-valued 1-by-3 vector
  group: Mounting
- name: Sample time
  summary: Sample time -1 (default) | positive scalar
  group: Mounting
- name: Azimuthal resolution of radar (deg)
  summary: Azimuth resolution of radar 4 (default) | positive real scalar
  group: Parameters
- name: Elevation resolution of radar (deg)
  summary: Elevation resolution of radar 5 (default) | positive real scalar
  group: Parameters
- name: Range resolution of radar (m)
  summary: Range resolution of radar 2.5 (default) | positive real scalar
  group: Parameters
- name: Range rate resolution of radar (m/s)
  summary: Range rate resolution of the radar 0.5 (default) | positive real scalar
  group: Parameters
- name: Fractional azimuthal bias component
  summary: Azimuth bias fraction 0.1 (default) | nonnegative real scalar
  group: Parameters
- name: Fractional elevation bias component
  summary: Elevation bias fraction 0.1 (default) | nonnegative real scalar
  group: Parameters
- name: Fractional range bias component
  summary: Range bias fraction 0.05 (default) | nonnegative real scalar
  group: Parameters
- name: Fractional range rate bias component
  summary: Range rate bias fraction 0.05 (default) | nonnegative real scalar
  group: Parameters
- name: Field of view (deg)
  summary: Field of view [20, 5] (default) | positive real-valued 1-by-2 vector
  group: Parameters
- name: Detection ranges (m)
  summary: Detection range [1, 150] (default) | positive real-valued 1-by-2 vector
  group: Parameters
- name: Range rates (m/s)
  summary: Minimum and maximum detection range rates [-100, 100] (default) | real-valued 1-by-2 vector
  group: Parameters
- name: Detection probability
  summary: Probability that radar detects a target 0.9 (default) | real scalar in the range (0, 1]
  group: Parameters
- name: False alarm rate
  summary: False alarm rate 1e-6 (default) | positive real scalar in range [10–7, 10–3]
  group: Parameters
- name: 'Detection probability range (m):'
  summary: Reference range for given probability of detection 100 (default) | positive real scalar
  group: Parameters
- name: Reference radar cross section (dBsm)
  summary: Reference radar cross section for given probability of detection 0 (default) | real scalar
  group: Parameters
- name: Enable elevation angle measurements
  summary: Enable radar to measure elevation on (default) | off
  group: Parameters
- name: Enable range rate measurements
  summary: Enable radar to measure range rate on (default) | off
  group: Parameters
- name: Enable measurement noise
  summary: Enable adding noise to radar sensor measurements on (default) | off
  group: Parameters
- name: Enable false detections
  summary: Enable reporting false alarm radar detections on (default) | off
  group: Parameters
- name: Random number generator method
  summary: Method to set random number generator seed Repeatable (default) | Specify seed | Not repeatable
  group: Parameters
- name: Initial seed
  summary: Random number generator seed 0 (default) | scalar in range [0, 232)
  group: Parameters
- name: Maximum reported
  summary: Maximum number of reported detections 50 (default) | positive integer
  group: Parameters
- name: Coordinate system
  summary: Coordinate system of reported detections Ego Cartesian (default) | Sensor Cartesian | Sensor spherical
  group: Parameters
- name: Specify output bus name
  summary: Specify name of output bus off (default) | on
  group: Parameters
- name: Output bus name
  summary: Name of output bus BusSimulation3DRadarTruthSensor (default) | valid bus name
  group: Parameters
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

#### Accuracy Settings

### **Azimuthal resolution of radar (deg)** — Azimuth resolution of radar `4` (default) | positive real scalar

Azimuth resolution of the radar, specified as a positive real scalar. The azimuth
resolution defines the minimum separation in azimuth angle at which the radar can
distinguish between two targets. The azimuth resolution is typically the 3dB-downpoint
in azimuth angle beamwidth of the radar. Units are in degrees.

**Example:** `6.5`

#### Dependencies

Azimuth resolution must be less than or equal to the azimuth field of view
specified in the `Field of view (deg)` parameter.

### **Elevation resolution of radar (deg)** — Elevation resolution of radar `5` (default) | positive real scalar

Elevation resolution of the radar, specified as a positive real scalar. The
elevation resolution defines the minimum separation in elevation angle at which the
radar can distinguish between two targets. The elevation resolution is typically the
3dB-downpoint in elevation angle beamwidth of the radar. Units are in degrees.

**Example:** `3.5`

#### Dependencies

To enable this parameter, on the **Parameters** tab, in the
**Radar model** section, select **Enable elevation angle
measurements**.

Elevation resolution must be less than or equal to the elevation field of view
specified in the `Field of view (deg)` parameter.

### **Range resolution of radar (m)** — Range resolution of radar `2.5` (default) | positive real scalar

Range resolution of the radar, specified as a positive real scalar. The range
resolution defines the minimum separation in range at which the radar can distinguish
between two targets. Units are in meters.

**Example:** `5.0`

### **Range rate resolution of radar (m/s)** — Range rate resolution of the radar `0.5` (default) | positive real scalar

Range rate resolution of the radar, specified as a positive real scalar. The range
rate resolution defines the minimum separation in range rate at which the radar can
distinguish between two targets. Units are in meters per second.

**Example:** `0.75`

#### Dependencies

To enable this parameter, on the **Parameters** tab, in the
**Radar model** section, select **Enable range rate
measurements**.

#### Bias Settings

### **Fractional azimuthal bias component** — Azimuth bias fraction `0.1` (default) | nonnegative real scalar

Azimuth bias fraction of the radar, specified as a nonnegative real scalar. The
azimuth bias is expressed as a fraction of the azimuth resolution specified in the
**Azimuthal resolution of radar (deg)** parameter. Units are
dimensionless.

**Example:** 0.3

### **Fractional elevation bias component** — Elevation bias fraction `0.1` (default) | nonnegative real scalar

Elevation bias fraction of the radar, specified as a nonnegative real scalar. The
elevation bias is expressed as a fraction of the elevation resolution specified in the
**Elevation resolution of radar (deg)** parameter. Units are
dimensionless.

**Example:** 0.2

#### Dependencies

To enable this parameter, on the **Parameters** tab, in the
**Radar model** section, select **Enable elevation angle
measurements**.

### **Fractional range bias component** — Range bias fraction `0.05` (default) | nonnegative real scalar

Range bias fraction of the radar, specified as a nonnegative real scalar. Range
bias is expressed as a fraction of the range resolution specified in the
**Range resolution of radar (m)** parameter. Units are
dimensionless.

**Example:** `0.15`

### **Fractional range rate bias component** — Range rate bias fraction `0.05` (default) | nonnegative real scalar

Range rate bias fraction of the radar, specified as a nonnegative real scalar.
Range rate bias is expressed as a fraction of the range rate resolution specified in
the **Range rate resolution of radar (m/s)** parameter. Units are
dimensionless.

**Example:** `0.2`

#### Dependencies

To enable this parameter, on the **Parameters** tab, in the
**Radar model** section, select **Enable range rate
measurements**.

#### Detector Settings

### **Field of view (deg)** — Field of view `[20, 5]` (default) | positive real-valued 1-by-2 vector

Field of view of the radar, specified as a positive real-valued 1-by-2 vector of
the form `[azfov, elfov]`. `azfov` is the azimuth
angle field of view. `elfov` is the elevation
angle field of view. The field of view defines the angular extent spanned by the
sensor. Each component must lie in the interval (0,180]. Targets outside of the field
of view of the radar are not detected. Units are in degrees.

**Example:** `[14 7]`

### **Detection ranges (m)** — Detection range `[1, 150]` (default) | positive real-valued 1-by-2 vector

Detection range, in meters, at which the radar can detect a target.

- To set only a maximum detection range, specify this parameter as a positive
  real scalar. By default, the minimum detection range is 0.
- To set both a minimum and maximum detection range, specify this parameter as a
  positive real-valued 1-by-2 vector of the form `[min,
  max]`.

**Example:** `250`

### **Range rates (m/s)** — Minimum and maximum detection range rates `[-100, 100]` (default) | real-valued 1-by-2 vector

Minimum and maximum detection range rates, specified as a real-valued 1-by-2
vector. The radar can detect targets only within this range rate interval. Units are
in meters per second.

**Example:** `[-200 200]`

#### Dependencies

To enable this parameter, on the **Parameters** tab, in the
**Radar model** section, select **Enable range rate
measurements**.

### **Detection probability** — Probability that radar detects a target `0.9` (default) | real scalar in the range (0, 1]

Probability that the radar detects a target, specified as a real scalar in the
range (0, 1]. This quantity defines the probability of detecting a target that has a
radar cross section specified by the **Reference radar cross section
(dBsm)** parameter, at the reference detection range specified by the
**Detection probability range (m)** parameter.

For more information about how the probabilistic detection parameters relate to
each other, see Probabilistic Radar Detection Parameters.

**Example:** `0.95`

### **False alarm rate** — False alarm rate `1e-6` (default) | positive real scalar in range [10–7, 10–3]

False alarm rate within a radar resolution cell, specified as a positive real
scalar in the range [10–7,
10–3]. Units are dimensionless.

**Example:** `1e-5`

### **Detection probability range (m):** — Reference range for given probability of detection `100` (default) | positive real scalar

Reference range for a given probability of detection, specified as a positive real
scalar. The reference range is the range at which the radar detects targets that have
a radar cross section specified by **Reference radar cross section
(dBsm)** with a probability of detection specified by the
**Detection probability** parameter. Units are in meters.

For more information about how the probabilistic detection parameters relate to
each other, see Probabilistic Radar Detection Parameters.

**Example:** `150`

### **Reference radar cross section (dBsm)** — Reference radar cross section for given probability of detection `0` (default) | real scalar

Reference radar cross section (RCS) for a given probability of detection,
specified as a real scalar. The reference radar cross section (RCS) defines the RCS
value of targets at the range specified by **Detection probability range
(m)**, for the radar to detect those targets with the probability specified
by **Detection probability**. Units are in decibels per square
meter.

For more information about how the probabilistic detection parameters relate to
each other, see Probabilistic Radar Detection Parameters.

**Note**

An alternative unit for radar cross section value is
m2. You can convert the RCS value to in
m2 to dBsm using the following equation and specify it
in the **Reference radar cross section (dBsm)** parameter:

|  |  |
| --- | --- |
| RCS in dBsm = 10 log (RCS in m2) | **(1)** |

**Example:** `2.0`

#### Radar Model

### **Enable elevation angle measurements** — Enable radar to measure elevation `on` (default) | `off`

Select this parameter to model a radar that can measure target elevation angles.
This parameter enables the **Elevation resolution of radar (deg)**
and **Fractional elevation bias component** parameters.

### **Enable range rate measurements** — Enable radar to measure range rate `on` (default) | `off`

Select this parameter to model a radar that can measure target range rates. This
parameter enables the **Range rate resolution of radar (m/s)**,
**Fractional range bias component**, and **Range rates
(m/s)** parameters.

### **Enable measurement noise** — Enable adding noise to radar sensor measurements `on` (default) | `off`

Select this parameter to add noise to radar sensor measurements. Otherwise, the
measurements are noise-free. The `MeasurementNoise` property of
each detection is always computed and is not affected by the value you specify for the
**Enable measurement noise** parameter. By not selecting this
parameter, you can pass the sensor ground truth measurements into a Multi-Object
Tracker block.

### **Enable false detections** — Enable reporting false alarm radar detections `on` (default) | `off`

Select this parameter to enable reporting false alarm radar measurements.
Otherwise, only actual detections are reported.

### **Random number generator method** — Method to set random number generator seed `Repeatable` (default) | `Specify seed` | `Not repeatable`

Method to set the random number generator seed, specified as one of the options in
the table.

| Option | Description |
| --- | --- |
| `Repeatable` | The block generates a random initial seed for the first simulation and reuses this seed for all subsequent simulations. Select this parameter to generate repeatable results from the statistical sensor model. To change this initial seed, at the MATLAB command prompt, enter `clear all`. |
| `Specify seed` | Specify your own random initial seed for reproducible results by using the **Specify seed** parameter. |
| `Not repeatable` | The block generates a new random initial seed after each simulation run. Select this parameter to generate nonrepeatable results from the statistical sensor model. |

### **Initial seed** — Random number generator seed `0` (default) | scalar in range [0, 232)

Random number generator seed, specified as a scalar in the range [0,
232)

**Example:** `2001`

#### Dependencies

To enable this parameter, set the **Random number generator
method** parameter to `Specify seed`.

#### Detection Reporting

### **Maximum reported** — Maximum number of reported detections `50` (default) | positive integer

Maximum number of reported detections, specified as a positive integer. Units are
dimensionless.

**Example:** `35`

### **Coordinate system** — Coordinate system of reported detections `Ego Cartesian` (default) | `Sensor Cartesian` | `Sensor spherical`

Coordinate system of reported detections, specified as one of these values:

- `Ego Cartesian` — The radar reports detections in
  the ego vehicle Cartesian coordinate system.
- `Sensor Cartesian`— The radar reports detections in the
  sensor Cartesian coordinate system.
- `Sensor spherical` — The radar reports detections
  in the spherical coordinate system. This coordinate system is centered at the
  radar and aligned with the orientation of the radar on the ego vehicle.

### **Specify output bus name** — Specify name of output bus `off` (default) | `on`

Select this parameter to specify the name of the bus that the block outputs to the
base workspace. Specify this name in the **Output bus name**
parameter.

### **Output bus name** — Name of output bus `BusSimulation3DRadarTruthSensor` (default) | valid bus name

Name of the bus that the block outputs to the base workspace.

#### Dependencies

To enable this parameter, select the **Specify output bus
name** parameter.
## Libraries

Automated Driving Toolbox / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019b**

### R2024a: Requires Simulink 3D Animation

Simulating models with the Simulation 3D Probabilistic Radar block requires
Simulink
3D Animation.

## Description

Probabilistic radar sensor model in 3D simulation environment

**Note**

Simulating models with the Simulation 3D Probabilistic Radar block requires
Simulink®
3D Animation™.

The Simulation 3D Probabilistic Radar block provides an interface to the
probabilistic radar sensor in a 3D simulation environment. This environment is rendered using
the Unreal Engine® from Epic Games®. You can specify the radar model and accuracy, bias, and detection parameters.
The block uses the sample time to capture the radar detections and outputs a list of object
detection reports. To configure the probabilistic radar signatures of actors in the 3D
environment across all radars in your model, use a Simulation 3D Probabilistic
Radar Configuration block. If you do not specify the radar signatures using the
Simulation 3D Probabilistic
Radar Configuration block, the radar cross section values of all the targets will be
`-20` dBsm.

If you set **Sample time** to `-1`, the block uses the
sample time specified in the Simulation 3D Scene Configuration block. To use
this sensor, you must include a Simulation 3D Scene Configuration block in your
model.

**Tip**

The Simulation 3D Scene Configuration
block must execute before the Simulation 3D Probabilistic Radar block. That
way, the Unreal Engine 3D visualization environment prepares the data before the Simulation 3D
Probabilistic Radar block receives it. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Probabilistic Radar — `1`

For more information about execution order, see How Unreal Engine Simulation for Automated Driving Works.
