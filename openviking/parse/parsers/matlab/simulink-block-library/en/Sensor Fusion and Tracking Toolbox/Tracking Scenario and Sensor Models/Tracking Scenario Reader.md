---
type: simulink-block
title: 'Tracking Scenario Reader'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Tracking Scenario and Sensor Models'
documentation_page: 'trackingscenarioreader'
documentation_source_path: 'ref/trackingscenarioreader.html'
language: en
---

# Tracking Scenario Reader

## Ports
```yaml
ports:
- name: Platform Poses
  summary: Platform pose information Simulink® bus containing MATLAB® structure
  direction: input
- name: Platforms
  summary: Information of platforms in the scenario Simulink bus containing MATLAB structure
  direction: output
- name: Simulation Time
  summary: Current simulation time nonnegative scalar
  direction: output
- name: Coverage Configurations
  summary: Coverage configurations in the scenario Simulink bus containing MATLAB structure
  direction: output
- name: Detections
  summary: Detection list Simulink bus containing MATLAB structure
  direction: output
- name: Sensor Configuratons
  summary: Sensor configurations in the scenario Simulink bus containing MATLAB structure
  direction: output
- name: Emissions
  summary: Radar and sonar emissions in the scenario Simulink bus containing MATLAB structure
  direction: output
- name: Emitter Configurations
  summary: Emitter configurations in the scenario Simulink bus containing MATLAB structure
  direction: output
- name: Point Clouds
  summary: Point clouds Simulink bus containing MATLAB structure
  direction: output
```

### Input

### **Platform Poses** — Platform pose information Simulink® bus containing MATLAB® structure

Platform pose information, specified as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumPlatforms` | Number of valid platforms, specified as a nonnegative integer. |
| `Platforms` | Platforms, specified as an array of platform pose structures. The first `NumPlatforms` of these structures are actual platform poses. |

The fields of each platform structure is:

| Field | Description |
| --- | --- |
| `PlatformID` | Unique platform identifier, specified as a positive integer. |
| `ClassID` | Platform classification identifier, specified as a nonnegative integer |
| `Position` | Position of the platform, specified as a 3-element real-valued vector.  - If the `IsEarthCentered` property of the   scenario is set to `false`, specify the position as   a three element Cartesian state [`x`,   `y`, `z`] in meters. - If the `IsEarthCentered` property of the   scenario is set to `true`, specify the position as   a three element geodetic state: `latitude` in   degrees, `longitude` in degrees, and   `altitude` in meters. |
| `Velocity` | Velocity of the platform, specified as a 3-element real-valued vector in m/s. |
| `Acceleration` | Acceleration of the platform, specified as a 3-element real-valued vector in m/s2. |
| `Orientation` | Orientation of the platform with respect to the local scenario frame, specified as a 3-by-3 rotation matrix. |
| `AngularVelocity` | Angular velocity of the platform relative to the local scenario frame, specified as a 3-element real-valued vector in degrees per second. |

You must pre-define each platform in the scenario before specifying its pose as
input. Use this input when you cannot pre-define the platform properties, such as its
position, in the scenario. For example, define the platform position in response to
positions of other platforms for collision avoidance during the scenario run.
Selecting this option disables all block output ports except the default
**Platforms** and **Simulation Time** output
ports.

#### Dependencies

To enable this port, in the **Scenario** tab, select the
**Source of platform pose** parameter as `Input
port`.
### Output

### **Platforms** — Information of platforms in the scenario Simulink bus containing MATLAB structure

Information of platforms in the scenario, returned as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumPlatforms` | Number of valid platforms, returned as a nonnegative integer. |
| `Platforms` | Platforms, returned as an array of platform pose structures. The first `NumPlatforms` of these structures are actual platform poses. |

The fields of each platform structure are:

| Field | Description |
| --- | --- |
| `PlatformID` | Unique platform identifier, returned as a positive integer. |
| `ClassID` | Platform classification identifier, returned as a nonnegative integer |
| `Position` | Position of the platform, returned as a 3-element real-valued vector.  - If the `IsEarthCentered` property of the   scenario is set to `false`, the position is   returned as a three element Cartesian state [`x`,   `y`, `z`] in meters. - If the `IsEarthCentered` property of the   scenario is set to `true`, the position is returned   as a three element geodetic state: `latitude` in   degrees, `longitude` in degrees, and   `altitude` in meters. |
| `Velocity` | Velocity of the platform, returned as a 3-element real-valued vector in m/s. |
| `Acceleration` | Acceleration of the platform, returned as a 3-element real-valued vector in m/s2. |
| `Orientation` | Orientation of the platform with respect to the local scenario frame, returned as a 3-by-3 rotation matrix. |
| `AngularVelocity` | Angular velocity of the platform relative to the local scenario frame, returned as a 3-element real-valued vector in degrees per second. |

The platform structure also contains these fields if you select the
**Include profiles information with platforms** parameter in the
**Output Setting** tab.

| Field | Description |
| --- | --- |
| `Dimensions` | Platform dimensions and origin offset, returned as a structure. The structure contains the `Length`, `Width`, `Height`, and `OriginOffset` of a cuboid that approximates the dimensions of the platform. The `OriginOffset` is the position vector from the center of the cuboid to the origin of the platform coordinate frame. For more details, see the `Dimensions` property of `Platform`. |
| `Mesh` | Mesh of the platform, returned as a structure. |

The mesh structure contains these fields:

| Field | Description |
| --- | --- |
| `NumVertices` | Number of valid vertices, returned as a positive integer. |
| `Vertices` | Vertices of the platform mesh, returned as an *N*-by-3 real-valued matrix, where *N* is the maximum number of vertices among all platform meshes in the scenario. The first, second, and third element of each row represents the x-, y-, and z-position of each vertex, respectively. |
| `NumFaces` | Number of valid faces, returned as a positive integer. |
| `Faces` | Faces of the platform mesh, returned as an *M*-by-3 matrix of positive integers, where *M* is the maximum number of faces among all platform meshes in the scenario. The three elements in each row are the vertex IDs of the three vertices forming the triangle face. The ID of the vertex is its corresponding row number specified in the `Vertices` field. |

### **Simulation Time** — Current simulation time nonnegative scalar

Current simulation time, returned as a nonnegative scalar in seconds.

### **Coverage Configurations** — Coverage configurations in the scenario Simulink bus containing MATLAB structure

Coverage configurations in the scenario, returned as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumConfigurations` | Number of valid coverage configurations, returned as a nonnegative integer. |
| `Configurations` | Coverage configurations, returned as an array of coverage configuration structures. The first `NumConfigurations` of these structures are actual coverage configurations. |

The fields of each coverage configuration structure are:

| Field | Description |
| --- | --- |
| `Index` | Unique sensor or emitter index, returned as a positive integer for sensors and returned as a negative integer for emitters. |
| `LookAngle` | The current boresight angles of the sensor or emitter, returned as two-element vector [`azimuth`; `elevation`] in degrees if the sensor or emitter scans both in the azimuth and elevation directions. If the sensor only scans only in the azimuth direction, the second element is returned as `NaN`. |
| `FieldOfView` | The field of view of the sensor or emitter, returned a 2-by-2 real-valued matrix in degrees. If the sensor is a lidar sensor, the first row returns the lower and upper azimuth limits and second row returns the lower and upper elevation limits. For other types of sensors or emitters, the first column contains the azimuth and elevation field of view and the second column is returned as `NaN`. |
| `ScanLimits` | The minimum and maximum angles the sensor or emitter can scan from its mounting orientation, returned as 2-by-2 matrix [`minAz`, `maxAz`; `minEl`, `maxEl`] in degrees if the sensor or emitter scans both in the azimuth and elevation directions. If the sensor only scans only in the azimuth direction, `minEl` and `maxEl` are returned as `NaN`. |
| `Range` | The range of the beam and coverage area of the sensor or emitter, returned as a scalar in meters. |
| `Position` | The origin position of the sensor or emitter, returned as a three-element vector [`x`, `y`, `z`] in meters. |
| `Orientation` | The rotation transformation from the scenario frame to the sensor or emitter mounting frame, returned as a rotation matrix. |

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Coverage** parameter.

### **Detections** — Detection list Simulink bus containing MATLAB structure

Detection list, returned as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumDetections` | Number of detections, returned as a nonnegative integer. |
| `Detections` | Object detections, returned as an array of object detection structures. The first `NumDetections` of these detections are actual detections. |

The fields of each object detection structure are:

| Field | Description |
| --- | --- |
| `Time` | Measurement time, returned as a positive scalar. |
| `Measurement` | Object measurements, returned as a real-valued vector. |
| `MeasurementNoise` | Measurement noise covariance matrix, returned as a positive define matrix. |
| `SensorIndex` | Unique ID of the sensor, returned as a positive integer. |
| `ObjectClassID` | Object classification ID, returned as a nonnegative integer. |
| `MeasurementParameters` | Measurement parameters, returned as a structure. |
| `ObjectAttributes` | Additional information passed to tracker, returned as a structure. |

See `objectDetection` for more detailed
explanations of these fields.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Detections** parameter.

### **Sensor Configuratons** — Sensor configurations in the scenario Simulink bus containing MATLAB structure

Sensor configurations in the scenario, returned as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumConfigurations` | Number of valid sensor configurations, returned as a nonnegative integer. |
| `Configurations` | Sensor configurations, returned as an array of coverage configuration structures. The first `NumConfigurations` of these structures are actual sensor configurations. |

The fields of each sensor configuration structure are:

| Field | Description |
| --- | --- |
| `SensorIndex` | Unique sensor identifier, returned as a positive integer. |
| `IsValidTime` | Indicate if the sensor should report at least a detection at the current time, returned as `false` or `true`. |
| `IsScanDone` | Indicate if the sensor has completed the current scan, returned as `false` or `true`. |
| `FieldOfView` | The field of view of the sensor or emitter, returned a 2-by-2 real-valued matrix in degrees. If the sensor is a lidar sensor, the first row returns the lower and upper azimuth limits and second row returns the lower and upper elevation limits. For other types of sensors or emitters, the first column contains the azimuth and elevation field of view and the second column is returned as `NaN`. |
| `MeasurementParameters` | Sensor measurement parameters, returned as an array of structures containing the coordinate frame transforms needed to transform positions and velocities in the scenario frame to the current sensor frame. See the `MeasurementParameters` property of the `objectDetection` object for more details. |

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Sensor** parameter.

### **Emissions** — Radar and sonar emissions in the scenario Simulink bus containing MATLAB structure

Radar and sonar emissions in the scenario, returned as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumEmissions` | Number of valid emissions, returned as a nonnegative integer. |
| `Emissions` | Emissions, returned as an array of emission structures. The first `NumEmissions` of these structures are actual emissions. |

The fields of each emission structure are:

| Field | Description |
| --- | --- |
| `PlatformID` | Platform identifier, returned as a positive integer. |
| `EmitterIndex` | Emitter identifier, returned as a positive integer. |
| `OriginPosition` | Location of emitter, returned as a 1-by-3 real-valued vector in meters. |
| `OriginVelocity` | Velocity of emitter, returned as a 1-by-3 real-valued vector in m/s. |
| `Orientation` | Orientation of emitter with respect to the local scenario frame, returned as a 3-by-3 rotation matrix. |
| `FieldOfView` | Field of view of the emitter, returned as a two-element vector [`azimuth` `elevation`] in degrees. |
| `EIRP` | Effective isotropic radiated power of the radar emission, returned as a scalar in dB for radar emission and returned as `NaN` for sonar emission. |
| `RCS` | Cumulative radar cross-section, returned as a scalar in dBsm for radar emission and returned as `NaN` for sonar emission. |
| `CenterFrequency` | Center frequency of the signal, returned as a positive scalar in Hz. |
| `BandWidth` | Half-power bandwidth of the signal, returned as a positive scalar in Hz. |
| `WaveformType` | Waveform type identifier, returned as a nonnegative integer. |
| `ProcessingGain` | Processing gain associated with the signal waveform, returned as a scalar in dB. |
| `PropagationRange` | Total distance over which the signal has propagated, returned as a nonnegative scalar in meters. For direct-path signals, the range is zero. |
| `PropagationRangeRate` | Total range rate for the path over which the signal has propagated, returned as a scalar in m/s. For direct-path signals, the range rate is zero. |
| `SourceLevel` | Cumulative source level of an emitted signal, returned as a scalar in dB per micro-pascal for sonar emission and returned as `NaN` for radar emission. The cumulative source level of the emitted signal in decibels is relative to the intensity of a sound wave having an rms pressure of 1 micro-pascal. |
| `TargetStrength` | Cumulative target strength of the source platform emitting the signal, returned as a scalar in dB for sonar emission and returned as `NaN` for radar emission. |

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Emissions** parameter.

### **Emitter Configurations** — Emitter configurations in the scenario Simulink bus containing MATLAB structure

Emitter configurations in the scenario, returned as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumConfigurations` | Number of valid emitter configurations, returned as a nonnegative integer. |
| `Configurations` | Emitter configurations, returned as an array of emitter configuration structures. The first `NumConfigurations` of these structures are actual emitter configurations. |

The fields of each emitter configuration are:

| Field | Description |
| --- | --- |
| `EmitterIndex` | Unique emitter identifier, returned as a positive integer. |
| `IsValidTime` | Indicate the emission status of the sensor, returned as `false` or `true`. |
| `IsScanDone` | Indicate if the emitter has completed its current scan, returned as `false` or `true`. |
| `FieldOfView` | The field of view of the emitter, specified as a two-element vector [`azimuth`; `elevation`] in degrees. |
| `MeasurementParameters` | Emitter measurement parameters, returned as an array of structures containing the coordinate frame transforms needed to transform positions and velocities in the scenario frame to the current emitter frame. See the `MeasurementParameters` property of the `objectDetection` object for more details. |

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Emitter** parameter.

### **Point Clouds** — Point clouds Simulink bus containing MATLAB structure

Point clouds, returned as a Simulink bus containing a MATLAB structure. The structure has the form:

| Field | Description |
| --- | --- |
| `NumPointClouds` | Number of valid point clouds, returned as a nonnegative integer. |
| `PointClouds` | Point clouds, returned as an array point cloud structures. The first `NumPointClouds` of these point cloud structures represent actual point clouds. |

The fields of each point cloud structure are:

| Field | Description |
| --- | --- |
| `NumPoints` | Number of valid points in the `Points` field, returned as a nonnegative integer. |
| `Points` | Unorganized points reported from the lidar, returned as an *N*-by-3 real-valued matrix, where *N* is the maximum number of points from all lidar sensors in the scenario. The first `NumPoints` rows represent actual points generated from the lidar. |
| `Clusters` | Cluster labels of points in the `Points` field, returned as an *N*-by-2 matrix of nonnegative integers, where *N* is the maximum number of points from all lidar sensors in the scenario. The first `NumPoint` rows represent actual cluster labels of the points. For each row of the matrix, the first element represents the `PlatformID` of the target generating the point whereas the second element represents the `ClassID` of the target. |

See `monostaticLidarSensor` for more information.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Point clouds** parameter.
## Parameters
```yaml
parameters:
- name: Source of scenario
  summary: Source of tracking scenario trackingScenario (default) | Tracking Scenario Designer session file
  group: Scenario
- name: Workspace variable name
  summary: Workspace variable name trackingScenario variable name
  group: Scenario
- name: Session file
  summary: Session file Tracking Scenario Designer session file name
  group: Scenario
- name: Source of platform pose
  summary: Source of platform pose Scenario (default) | Input port
  group: Scenario
- name: Sample time (s)
  summary: Sample time of simulation 0.1 (default) | positive real scalar
  group: Scenario
- name: Coordinate system to report platform poses
  summary: Coordinate system to report platform poses Cartesian (default) | Geodetic
  group: Scenario
- name: Include profiles information with platforms
  summary: Include profiles information with platforms off (default) | on
  group: Output Settings
- name: Detections
  summary: Enable detections output port off (default) | on
  group: Output Settings
- name: Point clouds
  summary: Enable port clouds output port off (default) | on
  group: Output Settings
- name: Emissions
  summary: Enable emission output port off (default) | on
  group: Output Settings
- name: Enable occlusion in emission propagation
  summary: Enable occlusion in emission propagation on (default) | off
  group: Output Settings
- name: Coverage
  summary: Enable coverage configurations output port off (default) | on
  group: Output Settings
- name: Sensor
  summary: Enable sensor configurations output port off (default) | on
  group: Output Settings
- name: Emitter
  summary: Enable emitter configurations output port off (default) | on
  group: Output Settings
- name: Random number generation
  summary: Method to generate random number seed Repeatable (default) | Not repeatable | Specify seed
  group: Output Settings
- name: Initial seed
  summary: Initial seed for randomization 0 (default) | nonnegative integer
  group: Output Settings
- name: Source of platform bus name
  summary: Source of name for platform poses bus Auto (default) | Property
  group: Bus Settings
- name: Specify platform bus name
  summary: Specify platform bus name BusPlatforms (default) | valid bus name
  group: Bus Settings
- name: Source of maximum number of platforms
  summary: Source of maximum number of platforms Auto (default) | Property
  group: Bus Settings
- name: Maximum number of platforms
  summary: Maximum number of platforms 50 (default) | positive integer
  group: Bus Settings
- name: Source of detection bus name
  summary: Source of name for detection bus Auto (default) | Property
  group: Bus Settings
- name: Specify detection bus name
  summary: Specify detection bus name BusDetection (default) | valid bus name
  group: Bus Settings
- name: Source of maximum number of detections
  summary: Source of maximum number of platforms Auto (default) | Property
  group: Bus Settings
- name: Maximum number of detections
  summary: Maximum number of detections 50 (default) | positive integer
  group: Bus Settings
- name: Source of point cloud bus name
  summary: Source of name for point cloud bus Auto (default) | Property
  group: Bus Settings
- name: Specify point cloud bus name
  summary: Specify point cloud bus name BusPointCloud (default) | valid bus name
  group: Bus Settings
- name: Maximum number of lidar sensors
  summary: Maximum number of lidar sensors 10 (default) | positive integer
  group: Bus Settings
- name: Source of maximum number of lidar sensors
  summary: Source of maximum number of lidar sensors Auto (default) | Property
  group: Bus Settings
- name: Source of emission bus name
  summary: Source of name for emission bus Auto (default) | Property
  group: Bus Settings
- name: Specify emission bus name
  summary: Specify emission bus name BusEmission (default) | valid bus name
  group: Bus Settings
- name: Source of maximum number of emissions
  summary: Source of maximum number of emissions Auto (default) | Property
  group: Bus Settings
- name: Maximum number of emissions
  summary: Maximum number of emissions 50 (default) | positive integer
  group: Bus Settings
- name: Source of coverage configuration bus name
  summary: Source of name for coverage configuration bus Auto (default) | Property
  group: Bus Settings
- name: Specify coverage configuration bus name
  summary: Specify coverage configuration bus name BusCovConf (default) | valid bus name
  group: Bus Settings
- name: Source of sensor configuration bus name
  summary: Source of name for sensor configuration bus Auto (default) | Property
  group: Bus Settings
- name: Specify sensor configuration bus name
  summary: Specify sensor configuration bus name BusSensorConf (default) | valid bus name
  group: Bus Settings
- name: Source of emitter configuration bus name
  summary: Source of name for emitter configuration bus Auto (default) | Property
  group: Bus Settings
- name: Specify emitter configuration bus name
  summary: Specify emitter configuration bus name BusEmitterConf (default) | valid bus name
  group: Bus Settings
- name: Source of maximum number of sensors
  summary: Source of maximum number of sensors Auto (default) | Property
  group: Bus Settings
- name: Maximum number of sensors
  summary: Maximum number of sensors 10 (default) | positive integer
  group: Bus Settings
- name: Source of maximum number of emitters
  summary: Source of maximum number of emitters Auto (default) | Property
  group: Bus Settings
- name: Maximum number of emitters
  summary: Maximum number of emitters 10 (default) | positive integer
  group: Bus Settings
```

### Scenario

### **Source of scenario** — Source of tracking scenario `trackingScenario` (default) | `Tracking Scenario Designer session file`

Specify the source of tracking scenario as one of these options:

- `trackingScenario` — In the **Workspace variable
  name** parameter, specify the name of a MATLAB workspace variable that represents a `trackingScenario` object.
- `Tracking Scenario Designer session file` — In the
  **Session file** parameter, specify the name of a session file
  that was saved from the Tracking Scenario
  Designer app.

### **Workspace variable name** — Workspace variable name `trackingScenario` variable name

Specify the workspace variable name as the name of a `trackingScenario` object in the MATLAB workspace.

If you change the definition of the tracking scenario, use the **Refresh
Scenario Data** button on the **Scenario** tab to update
the scenario.

#### Dependencies

To enable this parameter, set the **Source of scenario**
parameter to `trackingScenario`.

### **Session file** — Session file `Tracking Scenario Designer` session file name

Specify the session file as the name of a session file that was saved from the
Tracking Scenario
Designer app.

If you change the session file, use the **Refresh Scenario Data**
button on the **Scenario** tab to update the file.

#### Dependencies

To enable this parameter, set the **Source of scenario**
parameter to `Tracking Scenario Designer session file`.

### **Source of platform pose** — Source of platform pose `Scenario` (default) | `Input port`

Select the source of platform pose as

- `Scenario` — Use the platform poses defined in the
  scenario that is specified by the **Workspace variable name**
  or **Session file** parameter.
- `Input port` — Specify the platform poses by using
  the **Platform poses** input port. Select this option when you
  cannot pre-define the platform properties, such as its position, in the
  scenario. For example, define the platform position in response to positions of
  other platforms for collision avoidance during the scenario run. Also, selecting
  this option disables all block output ports except the default
  **Platforms** and **Simulation Time** output
  ports.

### **Sample time (s)** — Sample time of simulation `0.1` (default) | positive real scalar

Specify the sample time of simulation as a positive real scalar in seconds.
Inherited and continuous sample times are not supported.

This sample time overrides the sample time defined in the
`trackignScenario` object or the Tracking Scenario
Designer app session file. To obtain the same or similar outputs as the
scenario source, define this parameter according to the sample time defined in the
`trackignScenario` object or the Tracking Scenario
Designer app session file.

### **Coordinate system to report platform poses** — Coordinate system to report platform poses `Cartesian` (default) | `Geodetic`

Specify coordinate system to report platform poses as

- `Cartesian` — Report each platform position as a 3-element
  Cartesian position coordinates in meters with respect to the scenario
  frame.
- `Geodetic` — Report each platform position as a 3-element
  geodetic coordinates: latitude in degrees, longitude in degrees, and altitude in
  meters. To select this option, you must specify the **Source of
  scenario** parameter as `trackingScenario`
  and set the `IsEarthCentered` property of the scenario as
  `true`.

### Output Settings

#### Platforms

### **Include profiles information with platforms** — Include profiles information with platforms `off` (default) | `on`

Select this parameter include platform profile information, including platform
dimension and mesh, in the **Platforms** output.

#### Sensors and emitters

### **Detections** — Enable detections output port `off` (default) | `on`

Select this parameter to enable the **Detections** output
port.

#### Dependencies

To enable this parameter, select the **Source of platform
pose** parameter on the **Scenario** tab as
`Scenario`.

### **Point clouds** — Enable port clouds output port `off` (default) | `on`

Select this parameter to enable the **Point Clouds** output
port.

#### Dependencies

To enable this parameter, select the **Source of platform
pose** parameter on the **Scenario** tab as
`Scenario`.

### **Emissions** — Enable emission output port `off` (default) | `on`

Select this parameter to enable the **Emissions** output
port.

#### Dependencies

To enable this parameter, select the **Source of platform
pose** parameter on the **Scenario** tab as
`Scenario`.

### **Enable occlusion in emission propagation** — Enable occlusion in emission propagation `on` (default) | `off`

Select this parameter to enable occlusion of signal from platforms in emission
propagation.

#### Dependencies

To enable this parameter, select the **Emissions**
parameter.

#### Configurations

### **Coverage** — Enable coverage configurations output port `off` (default) | `on`

Select this parameter to enable the **Coverage Configurations**
output port.

#### Dependencies

To enable this parameter, select the **Source of platform
pose** parameter on the **Scenario** tab as
`Scenario`.

### **Sensor** — Enable sensor configurations output port `off` (default) | `on`

Select this parameter to enable the **Sensor Configurations**
output port.

#### Dependencies

To enable this parameter, select the **Source of platform
pose** parameter on the **Scenario** tab as
`Scenario`.

### **Emitter** — Enable emitter configurations output port `off` (default) | `on`

Select this parameter to enable the **Emitter Configurations**
output port.

#### Dependencies

To enable this parameter, select the **Source of platform
pose** parameter on the **Scenario** tab as
`Scenario`.

#### Random number generator settings

### **Random number generation** — Method to generate random number seed `Repeatable` (default) | `Not repeatable` | `Specify seed`

Select the method to generate random number seed as
`Repeatable`, `Not repeatable`, or
`Specify seed`. When selected as

- `Repeatable` — The blocks uses the same random seed
  every time.
- `Not repeatable` — The blocks uses a different
  random seed every time.
- `Specify seed` — Specify a random seed for the
  block using the **Initial Seed** parameter.

#### Dependencies

To enable this parameter, select the **Detections**,
**Point clouds**, or **Emissions**
parameter.

### **Initial seed** — Initial seed for randomization `0` (default) | nonnegative integer

Specify the initial seed for randomization in the block as a nonnegative
integer.

#### Dependencies

To enable this parameter, select the **Random number
generation** parameter as `Specify seed`.

### Bus Settings

#### Platforms

### **Source of platform bus name** — Source of name for platform poses bus `Auto` (default) | `Property`

Specify the source of the name for the platform poses bus returned in the
**Platforms** output port as one of these options:

- `Auto` — The block automatically creates a platform
  poses bus name.
- `Property` — Specify the platform poses bus name by
  using the **Specify platform bus name** parameter.

### **Specify platform bus name** — Specify platform bus name `BusPlatforms` (default) | valid bus name

Specify the name of the platform pose bus returned in the
**Platforms** output port as a valid bus name.

#### Dependencies

To enable this parameter, select the **Source of platform bus
name** parameter as `Property`.

### **Source of maximum number of platforms** — Source of maximum number of platforms `Auto` (default) | `Property`

Specify the source of the maximum number of platforms that you can have in the
tracking scenario as one of these options:

- `Auto` — The block sets the maximum number of
  platforms to the number of platforms in the tracking scenario.
- `Property` — Specify the maximum number of platforms
  by using the **Maximum number of platforms** parameter.

### **Maximum number of platforms** — Maximum number of platforms `50` (default) | positive integer

Specify the maximum number of platforms as a positive integer.

#### Dependencies

To enable this parameter, set the **Source of maximum number of
platforms** parameter to `Property`.

#### Detections

### **Source of detection bus name** — Source of name for detection bus `Auto` (default) | `Property`

Specify the source of the name for the detection bus returned in the
**Detections** output port as one of these options:

- `Auto` — The block automatically creates a detection
  bus name.
- `Property` — Specify the detection bus name by using
  the **Specify detection bus name** parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Detections** parameter.

### **Specify detection bus name** — Specify detection bus name `BusDetection` (default) | valid bus name

Specify the name of the detection bus returned in the
**Detections** output port as a valid bus name.

#### Dependencies

To enable this parameter, select the **Source of detection bus
name** parameter as `Property`.

### **Source of maximum number of detections** — Source of maximum number of platforms `Auto` (default) | `Property`

Specify the source of the maximum number of detections that you can generate from
the tracking scenario as one of these options:

- `Auto` — The block sets the maximum number of
  detections to the number of generated detections in the tracking scenario.
- `Property` — Specify the maximum number of detections
  by using the **Maximum number of detections** parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Detections** parameter.

### **Maximum number of detections** — Maximum number of detections `50` (default) | positive integer

Specify the maximum number of detections as a positive integer.

#### Dependencies

To enable this parameter, set the **Source of maximum number of
detections** parameter to `Property`.

#### Point clouds

### **Source of point cloud bus name** — Source of name for point cloud bus `Auto` (default) | `Property`

Specify the source of the name for the point bus returned in the **Point
Clouds** output port as one of these options:

- `Auto` — The block automatically creates a point
  cloud bus name.
- `Property` — Specify the point cloud bus name by
  using the **Specify point cloud bus name** parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Point clouds** parameter.

### **Specify point cloud bus name** — Specify point cloud bus name `BusPointCloud` (default) | valid bus name

Specify the name of the point cloud bus returned in the **Point
Clouds** output port as a valid bus name.

#### Dependencies

To enable this parameter, select the **Source of point cloud bus
name** parameter as `Property`.

### **Maximum number of lidar sensors** — Maximum number of lidar sensors `10` (default) | positive integer

Specify the maximum number of lidar sensors as a positive integer.

#### Dependencies

To enable this parameter, set the **Source of maximum number of lidar
sensors** parameter to `Property`.

### **Source of maximum number of lidar sensors** — Source of maximum number of lidar sensors `Auto` (default) | `Property`

Specify the source of the maximum number of lidar sensors that you can have in
the tracking scenario as one of these options:

- `Auto` — The block sets the maximum number of lidar
  sensors to the number of lidar sensors in the tracking scenario.
- `Property` — Specify the maximum number of detections
  by using the **Maximum number of lidar sensors** parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Point clouds** parameter.

#### Emissions

### **Source of emission bus name** — Source of name for emission bus `Auto` (default) | `Property`

Specify the source of the name for the emission bus returned in the
**Emissions** output port as one of these options:

- `Auto` — The block automatically creates an emission
  bus name.
- `Property` — Specify the emission bus name by using
  the **Specify emission bus name** parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Emissions** parameter.

### **Specify emission bus name** — Specify emission bus name `BusEmission` (default) | valid bus name

Specify the name of the emission bus returned in the
**Emissions** output port as a valid bus name.

#### Dependencies

To enable this parameter, select the **Source of emission bus
name** parameter as `Property`.

### **Source of maximum number of emissions** — Source of maximum number of emissions `Auto` (default) | `Property`

Specify the source of the maximum number of emissions that you can generate from
the tracking scenario as one of these options:

- `Auto` — The block sets the maximum number of
  emissions to the number of emissions generated in the tracking scenario.
- `Property` — Specify the maximum number of emissions
  by using the **Maximum number of emissions** parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Emissions** parameter.

### **Maximum number of emissions** — Maximum number of emissions `50` (default) | positive integer

Specify the maximum number of emissions as a positive integer.

#### Dependencies

To enable this parameter, set the **Source of maximum number of
emissions** parameter to `Property`.

#### Configurations

### **Source of coverage configuration bus name** — Source of name for coverage configuration bus `Auto` (default) | `Property`

Specify the source of the name for the coverage configuration bus returned in the
**Coverage Configurations** output port as one of these
options:

- `Auto` — The block automatically creates a coverage
  configuration bus name.
- `Property` — Specify the coverage configuration bus
  name by using the **Specify coverage configuration bus name**
  parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Coverage** parameter.

### **Specify coverage configuration bus name** — Specify coverage configuration bus name `BusCovConf` (default) | valid bus name

Specify the name of the coverage configuration bus returned in the
**Coverage Configurations** output port as a valid bus name.

#### Dependencies

To enable this parameter, select the **Source of coverage configuration
bus name** parameter as `Property`.

### **Source of sensor configuration bus name** — Source of name for sensor configuration bus `Auto` (default) | `Property`

Specify the source of the name for the sensor configuration bus returned in the
**Sensor Configurations** output port as one of these
options:

- `Auto` — The block automatically creates a sensor
  configuration bus name.
- `Property` — Specify the sensor configuration bus
  name by using the **Specify sensor configuration bus name**
  parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Sensor** parameter.

### **Specify sensor configuration bus name** — Specify sensor configuration bus name `BusSensorConf` (default) | valid bus name

Specify the name of the sensor configuration bus returned in the **Sensor
Configurations** output port as a valid bus name.

#### Dependencies

To enable this parameter, select the **Source of sensor configuration
bus name** parameter as `Property`.

### **Source of emitter configuration bus name** — Source of name for emitter configuration bus `Auto` (default) | `Property`

Specify the source of the name for the emitter configuration bus returned in the
**Emitter Configurations** output port as one of these
options:

- `Auto` — The block automatically creates an emitter
  configuration bus name.
- `Property` — Specify the emitter configuration bus
  name by using the **Specify emitter configuration bus name**
  parameter.

### **Specify emitter configuration bus name** — Specify emitter configuration bus name `BusEmitterConf` (default) | valid bus name

Specify the name of the emitter configuration bus returned in the
**Emitter Configurations** output port as a valid bus name.

#### Dependencies

To enable this parameter, select the **Source of emitter configuration
bus name** parameter as `Property`.

### **Source of maximum number of sensors** — Source of maximum number of sensors `Auto` (default) | `Property`

Specify the source of the maximum number of sensors that you can have in the
tracking scenario as one of these options:

- `Auto` — The block sets the maximum number of
  emissions to the number of sensors in the tracking scenario.
- `Property` — Specify the maximum number of sensors by
  using the **Maximum number of sensors** parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Coverage** or **Sensor** parameter.

### **Maximum number of sensors** — Maximum number of sensors `10` (default) | positive integer

Specify the maximum number of sensors as a positive integer.

#### Dependencies

To enable this parameter, set the **Source of maximum number of
sensors** parameter to `Property`.

### **Source of maximum number of emitters** — Source of maximum number of emitters `Auto` (default) | `Property`

Specify the source of the maximum number of emitters that you can have in the
tracking scenario as one of these options:

- `Auto` — The block sets the maximum number of
  emitters to the number of emitters in the tracking scenario.
- `Property` — Specify the maximum number of emitters
  by using the **Maximum number of emitters** parameter.

#### Dependencies

To enable this port, in the **Output Settings** tab, select the
**Emitter** or **Sensor** parameter.

### **Maximum number of emitters** — Maximum number of emitters `10` (default) | positive integer

Specify the maximum number of emitters as a positive integer.

#### Dependencies

To enable this parameter, set the **Source of maximum number of
emitters** parameter to `Property`.
## Libraries

Sensor Fusion and Tracking Toolbox / Tracking Scenario and Sensor Models

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

### R2023a: Simulink buses do not show in workspace

As of R2023a, the Simulink buses created by this block no longer show in MATLAB workspace.

## Description

Read tracking scenario and generate simulation data

The `Tracking Scenario Reader` block reads a `trackingScenario`
object or a Tracking Scenario Designer
session file and outputs platform poses and simulation time. You can configure the block to
optionally output detections, point clouds, emissions, sensor and emitter configurations, and
sensor coverages from the scenario.
