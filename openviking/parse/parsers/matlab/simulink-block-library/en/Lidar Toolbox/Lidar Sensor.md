---
type: simulink-block
title: 'Lidar Sensor'
family: 'lidar'
product_id: 'lidar'
product_name: 'Lidar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'lidarsensor'
documentation_source_path: 'ref/lidarsensor.html'
language: en
---

# Lidar Sensor

## Ports
```yaml
ports:
- name: ActorPoses
  summary: Actor poses Simulink bus containing MATLAB® structure
  direction: input
- name: IsValid
  summary: Valid simulation time 0 | 1
  direction: output
  data_types: Boolean
- name: Location
  summary: Location values of points *M*-by-*N*-by-3 matrix
  direction: output
- name: Intensity
  summary: Intensity values of points *M*-by-*N* matrix
  direction: output
- name: Clusters
  summary: Classification data of actors *M*-by-*N*-by-3 array
  direction: output
```

### Input

### **ActorPoses** — Actor poses Simulink bus containing MATLAB® structure

Actor poses, specified as a Simulink bus containing MATLAB structure. The structure must contain these two fields.

1. Target poses of the actors in the scene, specified as an
   *L*- element array of structures. Each structure corresponds
   to an actor. *L* is the number of actors used.

   You can generate this structure programmatically using the `actorPoses` (Automated Driving Toolbox) function. You can
   also create these structures manually. Each structure must contain these
   fields.

   | Field | Description | Value |
   | --- | --- | --- |
   | `ActorID` | Unique identifier for the actor. | Positive scalar |
   | `Position` | Position of the actor with respect to the ego vehicle coordinate system, in meters. | Three-element vector of the form [`x y z`] |
   | `Velocity` | Velocity (*V*) of the actor, in meters per second, along the *x*-, *y*-, and *z*- directions. | Three-element vector of the form [`Vx Vy Vz`] |
   | `Roll` | Roll angle of the actor in degrees. | Numeric scalar |
   | `Pitch` | Pitch angle of the actor in degrees. | Numeric scalar |
   | `Yaw` | Yaw angle of the actor in degrees. | Numeric scalar |
   | `AngularVelocity` | Angular velocity (*ω*) of the actor, in degrees per second, along the *x*-, *y*-, and *z*- directions. | Three-element vector of the form [`ωx ωy ωz`] |
2. Simulation time for generating new point clouds, specified as a positive
   scalar.

You can output the scene actors poses from a Scenario
Reader (Automated Driving Toolbox) block.
### Output

### **IsValid** — Valid simulation time `0` | `1`

Valid simulation time, returned as a logical `0`
(`false`) or `1` (`true`). This
value is `0` for the updates requested at times between the update
interval specified by the **Required interval between sensor updates
(s)** parameter.

**Data Types:** `Boolean`

### **Location** — Location values of points *M*-by-*N*-by-3 matrix

Location values of points in the point cloud, returned as an
*M*-by-*N*-by-3 matrix. *M*,
*N* are the number of rows and columns in the organized point
cloud, respectively.

### **Intensity** — Intensity values of points *M*-by-*N* matrix

Intensity values of points in the point cloud, returned as an
*M*-by-*N* matrix. *M*,
*N* are the number of rows and columns in the organized point
cloud, respectively.

### **Clusters** — Classification data of actors *M*-by-*N*-by-3 array

Classification data of actors in the scene, returned as an
*M*-by-*N*-by-3 array. *M*,
*N* are the number of rows and columns in the organized point
cloud, respectively. The first dimension of the array contains the
`ActorID`s, the second dimension contains the
`ClassID`s of the target actors, and third dimension contains the
material IDs representing indices of **Material attribute
information in JSON format**.
## Parameters
```yaml
parameters:
- name: Unique identifier of sensor
  summary: Unique sensor identifier 1 (default) | positive integer
  group: Parameters
- name: Required interval between sensor updates (s)
  summary: Required time interval between sensor updates 0.1 (default) | positive scalar
  group: Parameters
- name: Sensor model to choose typical values
  summary: Name of sensor model Custom (default) | HDL64E | HDL32E | VLP16 | VLP32C | VLS128 | PuckLITE | PuckHiRes | OS0-32
    | OS0-64 | OS0-128 | OS1Gen1-32 | OS1Gen1-64 | OS1Gen1-128 | OS1Gen2-32 | OS1Gen2-64 | OS1Gen2-128 | OS2-32 | OS2-64 |
    OS2-128
  group: Parameters
- name: Position [X Y Height] (m)
  summary: Sensor center position [1.5 0 1.6] (default) | three-element vector of form [*X* *Y* *Height*]
  group: Parameters
- name: Orientation [Roll Pitch Yaw] (deg)
  summary: Sensor orientation [0 0 0] (default) | three-element vector
  group: Parameters
- name: MATLAB or Model workspace Actor profiles variable name
  summary: Variable name for actor profiles actor_profiles (default) | valid variable name
  group: Parameters
- name: ActorID of the host vehicle
  summary: Actor ID of ego vehicle 1 (default) | positive integer
  group: Parameters
- name: Coordinate system to report point cloud data
  summary: Coordinate system of reported detections World (default) | Sensor | Host
  group: Parameters
- name: Maximum detection range of sensor (m)
  summary: Maximum detection range 120 (default) | positive scalar
  group: Sensor FOV
- name: Azimuth limits (deg)
  summary: Azimuth limits of lidar sensor [-180 180] (default) | two-element vector
  group: Sensor FOV
- name: Azimuth resolution (deg)
  summary: Azimuthal resolution of lidar sensor 0.16 (default) | positive scalar
  group: Sensor FOV
- name: Use elevation angles
  summary: Use custom elevation angles off (default) | on
  group: Sensor FOV
- name: Elevation angles (deg)
  summary: Elevation angles of lidar sensor *N*-element real-valued vector
  group: Sensor FOV
- name: Elevation limits (deg)
  summary: Elevation limits of lidar sensor [-20 20] (default) | two element vector of form [*min*, *max*]
  group: Sensor FOV
- name: Elevation resolution (deg)
  summary: Elevation resolution of lidar sensor 1.25 (default) | positive scalar
  group: Sensor FOV
- name: Add noise to measurements
  summary: Add noise to measurements on (default) | off
  group: Advance Settings
- name: Range accuracy (m)
  summary: Accuracy of sensor range measurement 0.002 (default) | positive scalar
  group: Advance Settings
- name: Fog visibility in meters
  summary: Visible distance in fog 1000 (default) | positive scalar
  group: Advance Settings
- name: Rainrate in mm/hour
  summary: Rate of rainfall 0 (default) | positive scalar
  group: Advance Settings
- name: Simulate Motion Distortion
  summary: Simulate motion distortion off (default) | on
  group: Advance Settings
- name: Laser firing time (s)
  summary: Firing times of lasers in lidar sensor [] (default) | positive scalar | positive numeric vector
  group: Advance Settings
- name: Material attribute information in JSON format
  summary: Material attribute information in JSON format string scalar | character vector
  group: Scene Material Attributes
- name: Edit JSON text to add, remove, or modify material attributes
  summary: Edit JSON text to add, remove, or modify material attributes off (default) | on
  group: Scene Material Attributes
- name: Output intensity port
  summary: Output intensity values of points on (default) | off
  group: Output Port Settings
- name: Output clusters port
  summary: Output segmentation values of points on (default) | off
  group: Output Port Settings
```

### Parameters

#### Sensor Identification

### **Unique identifier of sensor** — Unique sensor identifier `1` (default) | positive integer

Unique identifier for the sensor, specified as a positive integer. In a
multisensor system, this index distinguishes different sensors from one
another.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Required interval between sensor updates (s)** — Required time interval between sensor updates `0.1` (default) | positive scalar

Time interval between two consecutive sensor updates, specified as a positive
scalar. The block generates new detections at the interval specified by this
parameter. The value must be an integer multiple of the simulation time. Updates
requested from the sensor in between the update intervals contain no detections. Units
are in seconds.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Sensor model to choose typical values** — Name of sensor model `Custom` (default) | `HDL64E` | `HDL32E` | `VLP16` | `VLP32C` | `VLS128` | `PuckLITE` | `PuckHiRes` | `OS0-32` | `OS0-64` | `OS0-128` | `OS1Gen1-32` | `OS1Gen1-64` | `OS1Gen1-128` | `OS1Gen2-32` | `OS1Gen2-64` | `OS1Gen2-128` | `OS2-32` | `OS2-64` | `OS2-128`

*Since R2024a*

Specify the name of a sensor model. For information on the supported sensor
models, see Supported Sensors. This parameter sets
the default elevation angle values based on the specified sensor. To apply custom
elevation angles, set this parameter to `Custom` and use the
**Elevation angles
(deg)** parameter.

#### Dependencies

When you do not set this
parameter to
`Custom`, the block disables these parameters:

- **Use elevation angles**
- **Elevation angles (deg)**
- **Elevation limits (deg)**
- **Elevation resolution (deg)**

#### Sensor Mounting

### **Position [X Y Height] (m)** — Sensor center position `[1.5 0 1.6]` (default) | three-element vector of form [*X* *Y* *Height*]

Sensor center position, specified as a three-element vector of the form
[*X*
*Y*
*Height*]. The values of *X* and
*Y* represent the location of the sensor center with respect to the
*X*- and *Y*-axes of the ego vehicle coordinate
system. *Height* is the height of the sensor above the ground. The
default value defines a lidar sensor mounted on the front edge of the roof of a sedan.
Units are in meters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Orientation [Roll Pitch Yaw] (deg)** — Sensor orientation `[0 0 0]` (default) | three-element vector

Sensor orientation, specified as a three-element vector of the form,
[*Roll*
*Pitch*
*Yaw*]. These values are with respect to the ego vehicle coordinate
system. Units are in degrees.

- *Roll* — The roll angle is the angle of rotation around the
  front-to-back axis, which is the *x*-axis of the ego vehicle
  coordinate system. A positive roll angle corresponds to a clockwise rotation when
  looking in the positive direction of the *x*-axis.
- *Pitch* — The pitch angle is the angle of rotation around the
  side-to-side axis, which is the *y*-axis of the ego vehicle
  coordinate system. A positive roll angle corresponds to a clockwise rotation when
  looking in the positive direction of the *y*-axis.
- *Yaw* — The yaw angle is the angle of rotation around the
  vertical axis,which is the *z*-axis of the ego vehicle coordinate
  system. A positive roll angle corresponds to a clockwise rotation when looking in
  the positive direction of the *z*-axis. This
  rotation appears counter-clockwise when viewing the vehicle from above.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### Actor Profiles

### **MATLAB or Model workspace Actor profiles variable name** — Variable name for actor profiles `actor_profiles` (default) | valid variable name

Variable name for actor profiles, specified as the name of a MATLAB or model workspace variable containing actor profiles.

Actor profiles are the physical characteristics of the actors in the scene,
specified as a structure or as an *L*-element array of structures.
*L* is the number of actors in the scene.

If the actor profiles variable has a single structure, then all actors specified
at the **ActorPoses** input port use the same profile.

To generate an array of actor profile structures for your driving scenario `drivingScenario` (Automated Driving Toolbox), use the `actorProfiles` (Automated Driving Toolbox) function. You can also create these structures manually.
This table shows the valid structure fields.

| Field | Description | Value |
| --- | --- | --- |
| `ActorID` | Unique identifier for the actor. In a scene with multiple actors, this value distinguishes different actors from one another. | Positive integer |
| `ClassID` | User-defined classification ID for the actor.  | `ClassID` | Class Name | | --- | --- | | `1` | Car | | `2` | Truck | | `3` | Bicycle | | `4` | Pedestrian | | `5` | Jersey Barrier | | `6` | Guardrail | | Positive scalar |
| `Length` | Length of the actor in meters. | Positive scalar |
| `Width` | Width of the actor in meters. | Positive scalar |
| `Height` | Height of the actor in meters. | Positive scalar |
| `OriginOffset` | Offset of the rotational center of the actor from its geometric center. The rotational center, or origin, is located at the bottom center of the actor. For vehicles, the rotational center is the point on the ground beneath the center of the rear axle. | A three-element vector of the form `[x y z]`. Units are in meters. |
| `MeshVertices` | Vertices of the actor in mesh representation. | *N*-by-3 numeric matrix, where each row defines a vertex in 3-D space. |
| `MeshFaces` | Face of the actor in mesh representation. | *M*-by-3 integer matrix, where each row represents a triangle defined by vertex IDs, which are the row numbers of `MeshVertices`. |
| `MeshTargetReflectances` | Material reflectance for each triangular face of the actor. | *M*-by-1 numeric vector, where *M* is the number of triangle faces of the actor. Each value must be in the range `[0, 1]`. |

For more information about these structure fields, see the `actor` (Automated Driving Toolbox) and `vehicle` (Automated Driving Toolbox) functions.

### **ActorID of the host vehicle** — Actor ID of ego vehicle `1` (default) | positive integer

`ActorID` value of the ego vehicle, specified as a positive
integer. `ActorID` is the unique identifier for an actor. This
parameter must be a valid `ActorID` specified at the
**ActorPoses** input port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### Point Cloud Reporting

### **Coordinate system to report point cloud data** — Coordinate system of reported detections `World` (default) | `Sensor` | `Host`

*Since R2024b*

Coordinate system of reported detections, specified as one of these values:

- `Sensor` — The block reports the detections in the
  sensor coordinate system.
- `Host` — The block reports the detections in the
  coordinate system of a host actor.
- `World` — The block reports the detections in the
  world coordinate system.

### Sensor FOV

#### Settings

### **Maximum detection range of sensor (m)** — Maximum detection range `120` (default) | positive scalar

Maximum detection range of the sensor specified as a positive scalar. The sensor
cannot scan for the points beyond this range. Units are in meters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Azimuth limits (deg)** — Azimuth limits of lidar sensor `[-180 180]` (default) | two-element vector

Azimuth limits of the lidar sensor, specified as a two-element vector of the form
[*min*
*max*]. The values must be in the range `[-180,
180]`, *max* must be greater than *min*.
Units are in degrees.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Azimuth resolution (deg)** — Azimuthal resolution of lidar sensor `0.16` (default) | positive scalar

Azimuthal resolution of the lidar sensor, specified as a positive scalar. Units
are in degrees.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Use elevation angles** — Use custom elevation angles `off` (default) | `on`

Select this parameter to use custom elevation angles.

#### Dependencies

- To enable this parameter, set the **Set model to choose typical
  values** parameter to `Custom`.
- When you select this parameter, the block disables the **Elevation
  limits (deg)** and **Elevation resolution (deg)**
  parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Elevation angles (deg)** — Elevation angles of lidar sensor *N*-element real-valued vector

Custom elevation angles of the lidar sensor, specified as an
*N*-element real-valued vector. *N* is the number of
elevation channels. The elements of the vector must be in the increasing order. Units
are in degrees.

#### Dependencies

To enable this parameter:

- Set the **Set model to choose typical values** parameter
  to `Custom`.
- Select the **Use elevation angles** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Elevation limits (deg)** — Elevation limits of lidar sensor `[-20 20]` (default) | two element vector of form [*min*, *max*]

Elevation limits of the lidar sensor, specified as a two-element vector of the
form [*min*
*max*]. The values must be in the range `[-180,
180]`, *max* must be greater than *min*.
Units are in degrees.

#### Dependencies

To enable this parameter:

- Set the **Set model to choose typical values** parameter
  to `Custom`.
- Clear the **Use elevation angles** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Elevation resolution (deg)** — Elevation resolution of lidar sensor `1.25` (default) | positive scalar

Elevation resolution of the lidar sensor, specified as a positive scalar in
degrees.

#### Dependencies

To enable this parameter:

- Set the **Set model to choose typical values** parameter
  to `Custom`.
- Clear the **Use elevation angles** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### Advance Settings

#### Noise Simulation

### **Add noise to measurements** — Add noise to measurements `on` (default) | `off`

When you select this parameter, the block adds random Gaussian noise to each point
in the point cloud using the **Range accuracy (m)** parameter as one
standard deviation. Otherwise, the data has no noise.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Range accuracy (m)** — Accuracy of sensor range measurement `0.002` (default) | positive scalar

Accuracy of the sensor range measurement, specified as a positive scalar. Units
are in meters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### Weather Simulation

### **Fog visibility in meters** — Visible distance in fog `1000` (default) | positive scalar

Visible distance in fog, specified as a positive scalar, in meters. The value of
this parameter must not be greater than 1000. A higher value indicates a better
visibility and a lower fog impact. The default value of `1000`
indicates clear visibility, or no fog.

**Note**

When you specify both **Fog visibility in meters** and
**Rainrate in mm/hour** parameters, the block simulates only the
foggy weather.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Rainrate in mm/hour** — Rate of rainfall `0` (default) | positive scalar

Rate of rainfall, specified as a positive scalar in millimeter per hour. The value
of this parameter must not be greater than 200. Increasing this value increases the
impact of rain on the generated point cloud. The default value is
`0`, indicating no rainfall.

**Note**

When you specify both **Fog visibility in meters** and
**Rainrate in mm/hour** parameters, the block simulates only the
foggy weather.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### Motion Distortion

### **Simulate Motion Distortion** — Simulate motion distortion `off` (default) | `on`

*Since R2024a*

Select this parameter to simulate distortion in point cloud data due to ego
vehicle motion.

### **Laser firing time (s)** — Firing times of lasers in lidar sensor `[]` (default) | positive scalar | positive numeric vector

*Since R2024a*

Specify the firing times of the lasers in the lidar sensor. To specify the same
firing time for all the lasers in the sensor, use a positive scalar. Otherwise use a
positive numeric vector. The length of the vector must match the length of the
**Elevation angles (deg)** parameter.

If you do not select the **Use elevation angles** parameter, then
the length of the vector must be consistent with the **Elevation limits
(deg)** and **Elevation resolution (deg)** parameters. For
example, if you set the **Elevation limits (deg)** parameter to
`[-20 20]`, and the **Elevation resolution (deg)**
parameter to `1.25`, then the length of the **Laser firing
time (s)** vector must match the length of the vector
`[-20:1.25:20]`.

#### Dependencies

To enable this parameter, select the **Simulate Motion
Distortion** parameter.

**Data Types:** `single` | `double`

### Scene Material Attributes

### **Material attribute information in JSON format** — Material attribute information in JSON format string scalar | character vector

*Since R2024b*

Select this parameter to view or edit information of target material attributes in
JSON format. For more information of material attributes, see `MaterialAttributes` property.

#### Dependencies

- To enable this parameter, select **Edit JSON text to add, remove, or
  modify material attributes**.

### **Edit JSON text to add, remove, or modify material attributes** — Edit JSON text to add, remove, or modify material attributes `off` (default) | `on`

*Since R2024b*

Select this parameter to enable editing material attribute information stored in
JSON format.

### Output Port Settings

### **Output intensity port** — Output intensity values of points `on` (default) | `off`

Select this parameter to enable the **Intensity** output port.

### **Output clusters port** — Output segmentation values of points `on` (default) | `off`

Select this parameter to enable the **Clusters** output port.
## Libraries

Lidar Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

### R2024b: Use target material information from RoadRunner Scenario

You can now use material information of target actors in RoadRunner Scenario to generate point cloud data by using the parameters in the **Scene
Material Attributes** tab. The **Clusters** output port
also contains material ID information.

### R2024b: Specify coordinate system to report point cloud data

Specify `World`, `Host`, or `Sensor`
type of coordinate system for the output point cloud by using the **Coordinate
system to report point cloud data** parameter.

### R2024a: Specify sensor model

You can now specify the type of sensor model by using the **Sensor model to
choose typical values** parameter. This parameter sets the default elevation
angle values based on the specified sensor.

### R2024a: Simulate motion distortion

You can now simulate motion distortion by using the **Simulate Motion
Distortion** and **Laser firing time (s)** parameters.

### R2024a: Add lidar sensor to vehicle actors in RoadRunner Scenario

You can now generate point cloud data in a RoadRunner scenario using a lidar sensor model defined in Simulink. The block does not require any inputs when used with actors in a RoadRunner Scenario simulation.

## Description

Generate lidar point cloud data for a scene

The Lidar Sensor block generates point cloud data from the measurements
recorded by a lidar sensor mounted on an ego vehicle. The generated data is in the ego vehicle
coordinate system.

To generate point cloud data for a scene, you can configure the sensor and actor poses by
using this block. The block also outputs the intensity and segmentation values for the
generated points.

Additionally, you can use this block to

- configure the lidar sensor parameters such as range, azimuth angles, and elevation
  angles.
- add random Gaussian noise to the points in the point cloud.
- simulate weather conditions such as fog and rain.

You can use the `drivingScenario` (Automated Driving Toolbox) object to create a scenario
containing actors and trajectories, import this data into Simulink® by using the Scenario Reader (Automated Driving Toolbox)
block and then generate the point cloud data for the scenario by using the Lidar Sensor
block.

You can also use the block with vehicle actors in
RoadRunner Scenario simulations. The block does not require any inputs when used with actors in a
RoadRunner Scenario simulation. For more information, see Integrate Lidar Sensor Model into RoadRunner Scenario and Cosimulate with Unreal Engine. *(since R2024a)*

The lidar sensor model created with Lidar Sensor block uses hardware accelerated ray
tracing to produce a highly realistic and accurate representation of objects in the point
cloud. Ray tracing allows for precise modeling of the interactions between light rays emitted
by the lidar sensor and the surfaces of objects in the scene. Additionally, ray tracing
considers factors such as surface texture and angles, which enhances the realism and accuracy
of the output point cloud data.

**Tip**

In a model configured for driving scenario simulation,
the Scenario Reader block must execute before the Lidar Sensor block. That
way, the Lidar Sensor block processes the driving scenario data correctly. To check the block
execution order, right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Scenario Reader — `0`
- Lidar Sensor — `1`

.
