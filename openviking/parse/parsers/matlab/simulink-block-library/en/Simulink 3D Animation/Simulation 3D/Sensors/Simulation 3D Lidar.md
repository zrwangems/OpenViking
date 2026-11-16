---
type: simulink-block
title: 'Simulation 3D Lidar'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Sensors'
documentation_page: 'simulation3dlidar'
documentation_source_path: 'simulation3dlidar.html'
language: en
---

# Simulation 3D Lidar

## Ports

### Output

### **Point cloud** — Point cloud data *m*-by-*n*-by-3 array of positive real-valued [*x*, *y*, *z*] points

Point cloud data, returned as an *m*-by-*n*-by 3
array of positive, real-valued [*x*, *y*,
*z*] points. *m* and *n* define
the number of points in the point cloud, as shown in this equation:

m×n=VFOVVRES×HFOVHRES

where:

- *V*FOV is the vertical field of view
  of the lidar, in degrees, as specified by the **Vertical field of view
  (deg)** parameter.
- *V*RES is the vertical angular
  resolution of the lidar, in degrees, as specified by the **Vertical
  resolution (deg)** parameter.
- *H*FOV is the horizontal field of view
  of the lidar, in degrees, as specified by the **Horizontal field of view
  (deg)** parameter.
- *H*RES is the horizontal angular
  resolution of the lidar, in degrees, as specified by the **Horizontal
  resolution (deg)** parameter.

Each *m*-by-*n* entry in the array specifies the
*x*, *y*, and *z* coordinates of
a detected point in the sensor coordinate system. If the lidar does not detect a point
at a given coordinate, then *x*, *y*, and
*z* are returned as `NaN`.

You can create a point cloud from these returned points by using point cloud
functions in a MATLAB Function block.

**Data Types:** `single`

### **Distance** — Distance to object points *m*-by-*n* positive real-valued matrix

Distance to object points measured by the lidar sensor, returned as an
*m*-by-*n* positive real-valued matrix. Each
*m*-by-*n* value in the matrix corresponds to an
[*x*, *y*, *z*] coordinate point
returned by the **Point cloud** output port.

#### Dependencies

To enable this port, on the **Parameters** tab, select
**Distance outport**.

**Data Types:** `single`

### **Reflectivity** — Reflectivity of surface materials *m*-by-*n* matrix of intensity values in range [0, 1]

Reflectivity of surface materials, returned as an *m*-by-*n* matrix of intensity values in the range [0, 1], where *m* is the number of rows in the point cloud and *n* is the number of columns. Each point in the **Reflectivity** output corresponds to a point in the **Point cloud** output. The block returns points that are not part of a surface material as `NaN`.

To calculate reflectivity, the lidar sensor uses the Phong reflection model. This model describes surface reflectivity as a combination of diffuse reflections (scattered reflections, such as from rough surfaces) and specular reflections (mirror-like reflections, such as from smooth surfaces). For more details on this model, see the Phong reflection model page on Wikipedia.

#### Dependencies

To enable this port, select the **Reflectivity outport** parameter.

**Data Types:** `single`

### **Labels** — Label identifiers *m*-by-*n* array of label identifiers

Label identifier for each point in the point cloud, output as an
*m*-by-*n* array. Each
*m*-by-*n* value in the matrix corresponds to an
[*x*, *y*, *z*] coordinate point
returned by the **Point cloud** output port.

The table shows the object IDs used in the default scenes that are selectable from
the Simulation 3D Scene
Configuration block. If you are using a custom scene, in the Unreal® Editor, you can assign new object types to unused IDs. If a
scene contains an object that does not have an assigned ID, that object is assigned an
ID of `0`. The detection of lane markings is not
supported.

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

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output semantic segmentation**.

**Data Types:** `uint8`

### **Translation** — Sensor location real-valued 1-by-3 vector

Sensor location along the *X*-axis, *Y*-axis,
and *Z*-axis of the scene.

#### Dependencies

To enable this port, on the **Ground Truth** tab, select
**Output
location and orientation**.

**Data Types:** `double`

### **Rotation** — Sensor orientation real-valued 1-by-3 vector

Roll, pitch, and yaw sensor orientation about the *X*-axis,
*Y*-axis, and *Z*-axis of the
scene.

#### Dependencies

To enable this port, on the **Ground Truth** tab,
select **Output location and
orientation**.

**Data Types:** `double`

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

### **Coordinate system** — Coordinate system for actor transformation `Default` (default) | `MATLAB` | `ISO8855` | `AERO` | `VRML` | `SAE`

*Since R2025a*

Specify the coordinate system that the actor uses for
translation and rotation in the 3D environment.

- `Default` – World coordinate system
- `MATLAB` – MATLAB® coordinate system
- `ISO8855` – ISO 8855 standard coordinate system
- `AERO` – SAE coordinate system
- `VRML` – X3D ISO standard coordinate system
- `SAE` – SAE coordinate system

For more details on the different coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `MATLAB`

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
  the table. During simulation, the sensor travels with the vehicle. For example, the table provides the mounting
  locations in the ISO 8855 standard coordinate system.

| Mounting Location | Description | Orientation Relative to Vehicle Origin [Roll, Pitch, Yaw] (deg) |
| --- | --- | --- |
| `Origin` | Forward-facing sensor mounted to the vehicle origin, which is on the ground and at the geometric center of the vehicle (see Coordinate Systems in Simulink 3D Animation)  Vehicle with sensor mounted at origin | [0, 0, 0] |
| `Front bumper`  `Front center` | Forward-facing sensor mounted to the front bumper  Vehicle with sensor mounted at front bumper | [0, 0, 0] |
| `Rear bumper`  `Rear center` | Backward-facing sensor mounted to the rear bumper  Vehicle with sensor mounted at rear bumper | [0, 0, 180] |
| `Right mirror` | Downward-facing sensor mounted to the right side-view mirror  Vehicle with sensor mounted at right side-view mirror | [0, –90, 0] |
| `Left mirror` | Downward-facing sensor mounted to the left side-view mirror  Vehicle with sensor mounted at left side-view mirror | [0, –90, 0] |
| `Rearview mirror` | Forward-facing sensor mounted to the rearview mirror, inside the vehicle  Vehicle with sensor mounted at rearview mirror | [0, 0, 0] |
| `Hood center` | Forward-facing sensor mounted to the center of the hood  Vehicle with sensor mounted at hood center | [0, 0, 0] |
| `Roof center` | Forward-facing sensor mounted to the center of the roof  Vehicle with sensor mounted at roof center | [0, 0, 0] |

The
*X*-*Y*-*Z* mounting
location of the sensor relative to the vehicle depends on the vehicle type. To specify
the vehicle type, use the **Type** parameter of the Simulation 3D Vehicle with
Ground Following to which you mount the sensor. To obtain the
*X*-*Y*-*Z* mounting
locations for a vehicle type, see the reference page for that vehicle.

To determine the location of the sensor, open the sensor block. Then,
on the **Ground Truth** tab, select the **Output location and
orientation** parameter and inspect the data from the
**Translation** output port.

### **Specify offset** — Specify offset from mounting location `off` (default) | `on`

Select this parameter to specify an offset from the mounting location by using the **Relative translation [X, Y, Z]** and **Relative rotation [Roll, Pitch, Yaw]**
parameters.

### **Relative translation [X, Y, Z]** — Translation offset relative to mounting location `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Translation offset relative to the mounting location of the sensor, specified as a
real-valued 1-by-3 vector of the form [*X*, *Y*,
*Z*].

You can mount the sensor to a vehicle by setting **Parent
name** to the name of that vehicle. The origin is the mounting location
specified in the **Mounting location** parameter. This origin is
different from the vehicle origin, which is the geometric center of the vehicle. You can
also mount the sensor to the scene origin by setting **Parent name** to
`Scene Origin`.

For more details about the coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `[0,0,0.01]`

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Relative rotation [Roll, Pitch, Yaw]** — Rotational offset relative to mounting location `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Rotational offset relative to the mounting location of the sensor, specified as a
real-valued 1-by-3 vector of the form [*Roll*,
*Pitch*, *Yaw*]. Roll, pitch, and yaw are the
angles of rotation about the *X*-, *Y*-, and
*Z*-axes, respectively.

You can mount the sensor to a vehicle by setting **Parent
name** to the name of that vehicle. The origin is the mounting location
specified in the **Mounting location** parameter. This origin is
different from the vehicle origin, which is the geometric center of the vehicle. You can
also mount the sensor to the scene origin by setting **Parent name** to
`Scene Origin`.

For more details about the vehicle and world coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `[0,0,10]`

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time of the block, in seconds, specified as a positive scalar. The 3D simulation
environment frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block inherits its sample time from
the Simulation 3D Scene Configuration block.

### Parameters

### **Detection range (m)** — Maximum distance measured by lidar sensor `120` (default) | positive scalar

Maximum distance measured by the lidar sensor, specified as a positive scalar less
than or equal to `500`. Points outside this range are ignored. Units
are in meters.

### **Range resolution (m)** — Resolution of lidar sensor range `0.002` (default) | positive real scalar

Resolution of the lidar sensor range, in meters, specified as a positive real
scalar. The range resolution is also known as the *quantization
factor*. The minimal value of this factor is
*D*range / 224,
where *D*range is the maximum distance
measured by the lidar sensor, as specified in the **Detection range
(m)** parameter.

### **Vertical field of view (deg)** — Vertical field of view `40` (default) | positive scalar

Vertical field of view of the lidar sensor, specified as a positive scalar less
than or equal to `90`. Units are in degrees.

### **Vertical resolution (deg)** — Vertical angular resolution `1.25` (default) | positive scalar

Vertical angular resolution of the lidar sensor, specified as a positive scalar.
Units are in degrees.

### **Horizontal field of view (deg)** — Horizontal field of view `360` (default) | positive scalar

Horizontal field of view of the lidar sensor, specified as a positive scalar.
Units are in degrees.

### **Horizontal resolution (deg)** — Horizontal angular (azimuth) resolution `0.16` (default) | positive scalar

Horizontal angular (azimuth) resolution of the lidar sensor, specified as a
positive scalar. Units are in degrees.

### **Distance outport** — Output distance to measured object points `off` (default) | `on`

Select this parameter to output the distance to measured object points at the
**Distance** port.

### **Reflectivity outport** — Output reflectivity of surface materials `off` (default) | `on`

Select this parameter to output the reflectivity of surface materials at the
**Reflectivity** port.

### Ground Truth

### **Output semantic segmentation** — Output semantic segmentation map of label IDs `off` (default) | `on`

Select this parameter to output a semantic segmentation map of label IDs at the **Labels** port.

### **Output location and orientation** — Output location and orientation of sensor `off` (default) | `on`

Select this parameter to output the translation and rotation of the
sensor at the **Translation** and
**Rotation** ports,
respectively.

## Libraries

Offroad Autonomy Library / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors UAV Toolbox / Simulation 3D

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2025a: Set coordinate system parameter

Set the **Coordinate system** parameter in
the Simulation 3D Lidar block to represent the coordinate system for actor transformation
in the 3D environment.

### R2025a: Performance optimization

The sensor models in the Unreal Engine executable now run at the same sample rate set in the Simulation 3D blocks. This software update improves the frame rate and model execution time.

## Description

Lidar sensor model in 3D simulation environment

The Simulation 3D Lidar block provides an interface to the lidar sensor in
a 3D simulation environment. This environment is rendered using the Unreal Engine® from Epic Games®. The block returns a point cloud with the specified field of view and angular
resolution. You can also output the distances from the sensor to object points and the
reflectivity of surface materials. In addition, you can output the location and orientation of
the sensor in the world coordinate system of the scene.

If you set **Sample time** to `-1`, the block uses the
sample time specified in the Simulation 3D Scene Configuration block. To use
this sensor, ensure that the Simulation 3D Scene Configuration block is in your
model.

**Tip**

The Simulation 3D Scene Configuration
block must execute before the Simulation 3D Lidar block. That way, the
Unreal Engine 3D visualization environment prepares the data before the Simulation 3D
Lidar block receives it. To check the block execution order, right-click the
blocks and select **Properties**. On the **General** tab,
confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Lidar — `1`

For more information about execution order, see Control and Display Execution Order (Simulink).

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.
