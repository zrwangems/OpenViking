---
type: simulink-block
title: 'Lidar Point Cloud Generator'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Driving Scenario and Sensor Modeling'
documentation_page: 'lidarpointcloudgenerator'
documentation_source_path: 'ref/lidarpointcloudgenerator.html'
language: en
---

# Lidar Point Cloud Generator

## Ports
```yaml
ports:
- name: Actors
  summary: Scenario actor poses Simulink bus containing MATLAB® structure
  direction: input
- name: Ego Vehicle
  summary: Ego vehicle pose Simulink bus containing MATLAB structure
  direction: input
- name: Point Cloud
  summary: Point cloud data *m*-by-*n*-by-3 array of positive real-valued [*x*, *y*, *z*] points
  direction: output
```

### Input

### **Actors** — Scenario actor poses Simulink bus containing MATLAB® structure

Scenario actor poses in ego vehicle coordinates, specified as a Simulink bus containing a MATLAB structure.

The structure must contain these fields.

| Field | Description | Type |
| --- | --- | --- |
| `NumActors` | Number of actors | Nonnegative integer |
| `Time` | Current simulation time | Real-valued scalar |
| `Actors` | Actor poses | `NumActors`-length array of actor pose structures |

Each actor pose structure in `Actors` must have these
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

#### Dependencies

The block must be in a model that simulates a driving scenario using the Scenario
Reader block.

### **Ego Vehicle** — Ego vehicle pose Simulink bus containing MATLAB structure

Ego vehicle pose, specified as a Simulink bus containing a MATLAB structure.

The structure must have these fields.

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

You can output the ego vehicle pose from a Scenario
Reader block. In the Scenario Reader block used in your
model, select the **Output ego vehicle pose** parameter.

#### Dependencies

The block must be in a model that simulates a driving scenario using the Scenario
Reader block.
### Output

### **Point Cloud** — Point cloud data *m*-by-*n*-by-3 array of positive real-valued [*x*, *y*, *z*] points

Point cloud data, returned as an *m*-by-*n*-by 3
array of positive real-valued [*x*, *y*,
*z*] points. *m* is the number of elevation
(vertical) channels in the point cloud. *n* is the number of
azimuthal (horizontal) channels in the point cloud. *m* and
*n* define the number of points in the point cloud, as shown in
this equation:

m×n=VFOVVRES×HFOVHRES

- *V*FOV is the vertical field of view
  of the lidar, in degrees, as specified by the **Elevation limits of lidar
  (deg)** parameter.
- *V*RES is the vertical angular
  resolution of the lidar, in degrees, as specified by the **Elevation
  resolution of lidar (deg)** parameter.
- *H*FOV is the horizontal field of view
  of the lidar, in degrees, as specified by the **Azimuthal limits of lidar
  (deg)** parameter.
- *H*RES is the horizontal angular
  resolution of the lidar, in degrees, as specified by the **Azimuthal
  resolution of lidar (deg)** parameter.

Each *m*-by-*n* entry in the array specifies the
*x*-, *y*-, and *z*-coordinates
of a detected point in the ego vehicle coordinate system. If the lidar does not detect
a point at a given coordinate, then *x*, *y*, and
*z* are returned as `NaN`.

By default, the Lidar Point Cloud Generator block includes road
data in the generated point cloud. The block obtains the road data in world
coordinates from a Scenario
Reader block that is in the same model as the Lidar Point Cloud
Generator block. The Lidar Point Cloud Generator block
computes the road mesh in ego vehicle coordinates based on the road data and the ego
vehicle pose at the **Ego Vehicle** input port. The **Maximum
detection range (m)** parameter of the Lidar Point Cloud
Generator block determines the extent of the road mesh. To exclude road data
from the point cloud, clear the **Include roads in generated point
cloud** parameter.
## Parameters
```yaml
parameters:
- name: Unique identifier of sensor
  summary: Unique sensor identifier 1 (default) | positive integer
  group: Parameters
- name: Required interval between sensor updates (s)
  summary: Required time interval between sensor updates 0.1 (default) | positive scalar
  group: Parameters
- name: Sensor's (x,y) position (m)
  summary: Location of center of lidar sensor [1.5 0] (default) | real-valued 1-by-2 vector
  group: Parameters
- name: Sensor's height (m)
  summary: Height of lidar sensor 1.6 (default) | positive scalar
  group: Parameters
- name: Yaw angle of sensor mounted on ego vehicle (deg)
  summary: Yaw angle of lidar sensor 0 (default) | real-valued scalar
  group: Parameters
- name: Pitch angle of sensor mounted on ego vehicle (deg)
  summary: Pitch angle of lidar sensor 0 (default) | real-valued scalar
  group: Parameters
- name: Roll angle of sensor mounted on ego vehicle (deg)
  summary: Roll angle of lidar sensor 0 (default) | real-valued scalar
  group: Parameters
- name: Coordinate system used to report point cloud
  summary: Coordinate system of reported detections Ego Cartesian (default) | Sensor Cartesian
  group: Parameters
- name: Include ego vehicle in generated point cloud
  summary: Include ego vehicle in point cloud on (default) | off
  group: Parameters
- name: ActorID of ego vehicle
  summary: ActorID value of ego vehicle 1 (default) | positive integer
  group: Parameters
- name: Include roads in generated point cloud
  summary: Include roads in point cloud on (default) | off
  group: Parameters
- name: Source of actor profiles
  summary: Source of actor profiles From Scenario Reader block (default) | From workspace
  group: Parameters
- name: MATLAB or model workspace variable name
  summary: Variable name of actor profiles actor_profiles (default) | valid variable name
  group: Parameters
- name: Maximum detection range (m)
  summary: Maximum detection range 120 (default) | positive scalar
  group: Measurements
- name: Range accuracy (m)
  summary: Accuracy of range measurements 0.002 (default) | positive scalar
  group: Measurements
- name: Azimuthal resolution of lidar (deg)
  summary: Azimuthal resolution of lidar sensor 0.16 (default) | positive scalar
  group: Measurements
- name: Elevation resolution of lidar (deg)
  summary: Elevation resolution of lidar sensor 1.25 (default) | positive scalar
  group: Measurements
- name: Azimuthal limits of lidar (deg)
  summary: Azimuthal limits of lidar sensor [-180 180] (default) | 1-by-2 real-valued vector of form [*min*, *max*]
  group: Measurements
- name: Elevation limits of lidar (deg)
  summary: Elevation limits of lidar sensor [-20 20] (default) | 1-by-2 real-valued vector of form [*min*, *max*]
  group: Measurements
- name: Add noise to measurements
  summary: Add noise to measurements on (default) | off
  group: Measurements
```

### Parameters

#### Sensor Identification

### **Unique identifier of sensor** — Unique sensor identifier `1` (default) | positive integer

Unique sensor identifier, specified as a positive integer. The sensor identifier
distinguishes detections that come from different sensors in a multisensor system. If
a model contains multiple sensor blocks that have the same sensor identifier, the Bird's-Eye
Scope displays an error.

### **Required interval between sensor updates (s)** — Required time interval between sensor updates `0.1` (default) | positive scalar

Required time interval between sensor updates, specified as a positive scalar. The
value of this parameter must be an integer multiple of the **Actors**
input port data interval. Updates requested from the sensor between update intervals
contain no detections. Units are in seconds.

#### Sensor Extrinsics

### **Sensor's (x,y) position (m)** — Location of center of lidar sensor `[1.5 0]` (default) | real-valued 1-by-2 vector

Location of the center of the lidar sensor, specified as a real-valued 1-by-2
vector. The **Sensor's (x,y) position (m)** and **Sensor's
height (m)** parameters define the coordinates of the lidar sensor with
respect to the ego vehicle coordinate system. The default value corresponds to a lidar
sensor mounted on a sedan, at the center of the roof's front edge. Units are in
meters.

### **Sensor's height (m)** — Height of lidar sensor `1.6` (default) | positive scalar

Height of the lidar sensor above the ground plane, specified as a positive scalar.
The **Sensor's (x,y) position (m)** and **Sensor's height
(m)** parameters define the coordinates of the lidar sensor with respect to
the ego vehicle coordinate system. The default value corresponds to a lidar sensor
mounted on a sedan, at the center of the roof front edge. Units are in meters.

### **Yaw angle of sensor mounted on ego vehicle (deg)** — Yaw angle of lidar sensor `0` (default) | real-valued scalar

Yaw angle of the lidar sensor, specified as a real-valued scalar. The
*yaw angle* is the angle between the center line of the ego
vehicle and the downrange axis of the lidar sensor. A positive yaw angle corresponds
to a clockwise rotation when you look in the positive direction of the
*z*-axis of the ego vehicle coordinate system. Units are in
degrees.

### **Pitch angle of sensor mounted on ego vehicle (deg)** — Pitch angle of lidar sensor `0` (default) | real-valued scalar

Pitch angle of the lidar sensor, specified as a real-valued scalar. The
*pitch angle* is the angle between the downrange axis of the
lidar sensor and the *xy*-plane of the ego vehicle coordinate system.
A positive pitch angle corresponds to a clockwise rotation when you look in the
positive direction of the *y*-axis of the ego vehicle coordinate
system. Units are in degrees.

### **Roll angle of sensor mounted on ego vehicle (deg)** — Roll angle of lidar sensor `0` (default) | real-valued scalar

Roll angle of the lidar sensor, specified as a real-valued scalar. The
*roll angle* is the angle of rotation of the downrange axis of
the lidar sensor around the *x*-axis of the ego vehicle coordinate
system. A positive roll angle corresponds to a clockwise rotation when you look in the
positive direction of the *x*-axis of the ego vehicle coordinate
system. Units are in degrees.

#### Point Cloud Reporting

### **Coordinate system used to report point cloud** — Coordinate system of reported detections `Ego Cartesian` (default) | `Sensor Cartesian`

Coordinate system of reported detections, specified as one of these values:

- `Ego Cartesian` — Detections are reported in the
  ego vehicle Cartesian coordinate system.
- `Sensor Cartesian` — Detections are reported in the
  sensor Cartesian coordinate system.

### **Include ego vehicle in generated point cloud** — Include ego vehicle in point cloud `on` (default) | `off`

Select this parameter to include the ego vehicle in the generated point
cloud.

### **ActorID of ego vehicle** — `ActorID` value of ego vehicle `1` (default) | positive integer

`ActorID` value of the ego vehicle, specified as a positive
integer. `ActorID` is the unique identifier for an actor. This
parameter must be a valid `ActorID` from the input **Actor** bus.

#### Dependencies

To enable this parameter, select the **Include ego vehicle in generated
point cloud** parameter.

### **Include roads in generated point cloud** — Include roads in point cloud `on` (default) | `off`

Select this parameter to include the roads in the generated point cloud.

### **Source of actor profiles** — Source of actor profiles `From Scenario Reader block` (default) | `From workspace`

Source of actor profiles, which are the physical and radar characteristics of all
actors in the driving scenario, specified as one of these options:

- `From Scenario Reader block` — The block obtains
  the actor profiles from the scenario specified by the Scenario
  Reader block or RoadRunner
  Scenario Reader block.
- `From workspace` — The block obtains the actor
  profiles from the MATLAB or model workspace variable specified by the **MATLAB or
  model workspace variable name** parameter.

### **MATLAB or model workspace variable name** — Variable name of actor profiles `actor_profiles` (default) | valid variable name

Variable name of actor profiles, specified as the name of a MATLAB or model workspace variable containing actor profiles.

Actor profiles are the physical and radar characteristics of all actors in a
driving scenario and are specified as a structure or structure array.

- If the actor profiles variable contains a single structure, then all actors
  specified in the input **Actors** bus use this profile.
- If the actor profiles variable is a structure array, then each actor
  specified in the input **Actors** bus must have a unique actor
  profile.

To generate an array of structures for your driving scenario, use the `actorProfiles` function. The table shows the valid structure fields. If
you do not specify a field, the fields are set to their default values.

| Field | Description |
| --- | --- |
| `ActorID` | Scenario-defined actor identifier, specified as a positive integer. |
| `ClassID` | Classification identifier, specified as a nonnegative integer. `0` represents an object of an unknown or unassigned class. |
| `Length` | Length of actor, specified as a positive real-valued scalar. Units are in meters. |
| `Width` | Width of actor, specified as a positive real-valued scalar. Units are in meters. |
| `Height` | Height of actor, specified as a positive real-valued scalar. Units are in meters. |
| `OriginOffset` | Offset of actor's rotational center from its geometric center, specified as a real-valued vector of the form [*x*, *y*, *z*]. The rotational center, or origin, is located at the bottom center of the actor. For vehicles, the rotational center is the point on the ground beneath the center of the rear axle. Units are in meters. |
| `MeshVertices` | Mesh vertices of actor, specified as an *n*-by-*3* real-valued matrix of vertices. Each row in the matrix defines a point in 3-D space. |
| `MeshFaces` | Mesh faces of actor, specified as an *m*-by-*3* matrix of integers. Each row of `MeshFaces` represents a triangle defined by the vertex IDs, which are the row numbers of vertices. |
| `RCSPattern` | Radar cross-section (RCS) pattern of actor, specified as a `numel(RCSElevationAngles)`-by-`numel(RCSAzimuthAngles)` real-valued matrix. Units are in decibels per square meter. |
| `RCSAzimuthAngles` | Azimuth angles corresponding to rows of `RCSPattern`, specified as a vector of values in the range [–180, 180]. Units are in degrees. |
| `RCSElevationAngles` | Elevation angles corresponding to rows of `RCSPattern`, specified as a vector of values in the range [–90, 90]. Units are in degrees. |

For complete definitions of the structure fields, see the `actor` and `vehicle` functions.

#### Dependencies

To enable this parameter, set the **Source of actor profiles**
parameter to `From workspace`.

### Measurements

#### Settings

### **Maximum detection range (m)** — Maximum detection range `120` (default) | positive scalar

Maximum detection range of the lidar sensor, specified as a positive scalar. The
sensor cannot detect actors beyond this range. This parameter also determines the
extent of the road mesh. Units are in meters.

### **Range accuracy (m)** — Accuracy of range measurements `0.002` (default) | positive scalar

Accuracy of range measurements, specified as a positive scalar. Units are in
meters.

### **Azimuthal resolution of lidar (deg)** — Azimuthal resolution of lidar sensor `0.16` (default) | positive scalar

Azimuthal resolution of the lidar sensor, specified as a positive scalar. The
azimuthal resolution defines the minimum separation in azimuth angle at which the
lidar can distinguish between two targets. Units are in degrees.

### **Elevation resolution of lidar (deg)** — Elevation resolution of lidar sensor `1.25` (default) | positive scalar

Elevation resolution of the lidar sensor, specified as a positive scalar. The
elevation resolution defines the minimum separation in elevation angle at which the
lidar can distinguish between two targets. Units are in degrees.

### **Azimuthal limits of lidar (deg)** — Azimuthal limits of lidar sensor `[-180 180]` (default) | 1-by-2 real-valued vector of form [*min*, *max*]

Azimuthal limits of the lidar sensor, specified as a 1-by-2 real-valued vector of
the form [*min*, *max*]. Units are in
degrees.

### **Elevation limits of lidar (deg)** — Elevation limits of lidar sensor `[-20 20]` (default) | 1-by-2 real-valued vector of form [*min*, *max*]

Elevation limits of the lidar sensor, specified as a 1-by-2 real-valued vector of
the form [*min*, *max*]. Units are in
degrees.

### **Add noise to measurements** — Add noise to measurements `on` (default) | `off`

Select this parameter to add noise to lidar sensor measurements. When you clear
this parameter, the measurements have no noise.
## Libraries

Automated Driving Toolbox / Driving Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

### R2024a: Usage with RoadRunner Scenario simulation does not require registering the sensor model using `addSensors` function

Starting in R2024a, Simulink automatically instantiates a `SensorSimulation` object and adds sensors defined in the model to the RoadRunner scenario. Hence, registering Lidar Point Cloud Generator block manually using the `addSensors` function is not required. For more information on the new workflow, see the Add Sensors to RoadRunner Scenario Using Simulink example.

In releases prior to R2024a, you must manually register the block as a sensor model using the `addSensors` function. For more information, see Adding sensors manually using `addSensors` function is not required for Simulink models.

## Description

Generate lidar point cloud data for driving scenario or RoadRunner Scenario

The Lidar Point Cloud Generator block generates a point cloud from lidar
measurements taken by a lidar sensor mounted on an ego vehicle.

The block derives the point cloud from simulated roads and actor poses in a driving
scenario and generates the point cloud at intervals equal to the sensor update interval. By
default, detections are referenced to the coordinate system of the ego vehicle. The block can
simulate added noise at a specified range accuracy by using a statistical model. The block
also provides parameters to exclude the ego vehicle and roads from the generated point
cloud.

You can use the block with vehicle actors in Driving Scenario and RoadRunner Scenario simulations. The block does not require any inputs when used with actors in a
RoadRunner Scenario simulation. For more information, see Add Sensors to RoadRunner Scenario Using Simulink example.

The lidar generates point cloud data based on the mesh representations of the roads and
actors in the scenario. A *mesh* is a 3-D geometry of an object that is
composed of faces and vertices.

The lidar sensor model created with Lidar Point Cloud Generator uses hardware accelerated ray tracing to
produce a highly realistic and accurate representation of objects in the point cloud. Ray
tracing allows for precise modeling of the interactions between light rays emitted by the
lidar sensor and the surfaces of objects in the scene. Additionally, ray tracing considers
factors such as surface texture and angles, which enhances the realism and accuracy of the
output point cloud data. The sensor model can also add random noise to the detections.

When building scenarios and sensor models using the Driving Scenario
Designer app, the lidar sensors exported to Simulink® are output as Lidar Point Cloud Generator blocks.

**Tip**

In a model configured for driving scenario simulation,
the Scenario Reader block must execute before the Lidar Point Cloud Generator block. That
way, the driving scenario data is correctly processed by the Lidar Point Cloud Generator block. To check the
block execution order, right-click the blocks and select **Properties**. On
the **General** tab, confirm these **Priority** settings:

- Scenario Reader — `0`
- Lidar Point Cloud Generator — `1`

.
