---
type: simulink-block
title: 'Simulation 3D Ray Tracer'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Sensors'
documentation_page: 'simulation3draytracer'
documentation_source_path: 'simulation3draytracer.html'
language: en
---

# Simulation 3D Ray Tracer

## Ports

### Output

### **HitLocations** — Hit locations real-valued *N(B+1)*-by-3 array

Hit locations, returned as a real-valued *N(B+1)*-by-3 array of
the form [*X*, *Y*, *Z*], in
meters. *N* is the number of rays and *B* is the
number of bounces per ray.

**Data Types:** `double`

### **HitNormals** — Ray normal to hit location real-valued *N(B+1)*-by-3 array

Ray normal to the hit location, returned as a real-valued
*N(B+1)*-by-3 array of the form [*X*,
*Y*, *Z*], in meters. *N* is
the number of rays and *B* is the number of bounces per ray.

**Data Types:** `double`

### **HitDistances** — Ray distance to hit location real-valued *N(B+1)*-by-1 array

Ray distance to hit location, returned as a real-valued
*N(B+1)*-by-1 vector *N*, in meters.
*N* is the number of rays and *B* is the number of
bounces per ray.

**Data Types:** `double`

### **SurfaceIds** — Object IDs of hit surfaces integer-valued *N(B+1)*-by-1 vector | `0`

Object identifier of the surfaces hit by the ray, returned as an integer-valued
*N(B+1)*-by-1 vector *N*. *N* is
the number of rays and *B* is the number of bounces per ray.

The returned surface identifiers are the object values specified when creating
custom surfaces in the Unreal® Editor. If a surface identifier is unknown, the block assigns it an ID
of `0`. For information about adding surfaces, see Add a Surface Type in the Unreal Engine documentation.

**Data Types:** `uint8`

### **IsValidHit** — Hit flag *N*-by-1 vector

Hit flag, returned as a *N*-by-1 Boolean vector.
*N* is the number of rays. A value of 1 indicates the ray hit a
surface.

**Data Types:** `Boolean`

## Parameters

#### Mounting

### **Sensor identifier** — Unique sensor identifier `1` (default) | positive integer

Specify the unique identifier of the sensor. In a multisensor system, the sensor identifier
enables you to distinguish between sensors. When you add a new sensor block to your
model, the **Sensor identifier** of that block is *N*
+ 1, where *N* is the highest **Sensor identifier**
value among the existing sensor blocks in the model.

**Example:** `2`

### **Parent name** — Name of parent `Scene Origin` (default)

Name of parent to which the sensor is mounted, specified as the name of a vehicle in
your model, or `Scene Origin`. The vehicle names that you can
select correspond to the **Name** parameters of the
simulation 3D vehicle blocks in your model.

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
*Z*], in meters.

You can mount the sensor to a vehicle by setting
**Parent name** to the name of that vehicle. The origin is the
mounting location specified in the **Mounting location** parameter.
This origin is different from the vehicle origin, which is the geometric center of the
vehicle. You can also mount the sensor to the scene origin by setting **Parent
name** to `Scene Origin`.

For more details about the coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `[0,0,0.01]`

#### Dependencies

To enable this parameter, select **Specify offset**.

### **Relative rotation [Roll, Pitch, Yaw]** — Rotational offset relative to mounting location `[0, 0, 0]` (default) | real-valued 1-by-3 vector

Rotational offset relative to the mounting location of the sensor, specified as a
real-valued 1-by-3 vector of the form [*Roll*,
*Pitch*, *Yaw*]. Roll, pitch, and yaw are the angles of rotation about the
*X*-, *Y*-, and *Z*-axes,
respectively.

You can mount the sensor to a vehicle by setting
**Parent name** to the name of that vehicle. The origin is the
mounting location specified in the **Mounting location** parameter.
This origin is different from the vehicle origin, which is the geometric center of the
vehicle. You can also mount the sensor to the scene origin by setting **Parent
name** to `Scene Origin`.

For more details about the coordinate systems, see Coordinate Systems in Simulink 3D Animation.

**Example:** `[0,0,10]`

#### Dependencies

To enable this parameter, select **Specify offset**.

#### Parameters

### **Ray origins** — Ray origin `zeros(10,3)` (default) | real-valued *N*-by-3 array

Ray origin relative to sensor mounting location, specified as a real-valued
*N*-by-3 array of the form [*X*,
*Y*, *Z*], in meters. *N* is
the number of rays.

**Example:** `zeros(10,3)`

### **Ray directions** — Normalized ray direction `ones(10,3)` (default) | real-valued *N*-by-3 array

Normalized ray direction relative to sensor mounting location, specified as a
real-valued *N*-by-3 array of the form [*X*,
*Y*, *Z*]. *N* is the number of
rays. The units are dimensionless.

**Example:** `ones(10,3)`

### **Max ray lengths** — Maximum total ray length `ones(10,1)*10` (default) | real-valued *N*-by-1 vector

Maximum total ray length of a multi-bounce trace path, specified as a real-valued
*N*-by-1 vector, in meters. *N* is the number of
rays.

**Example:** `ones(10,1)*10`

### **Number of bounces** — Number of bounces per ray `2` (default) | positive integer

Number of bounces that a trace may have before terminating, *B*,
specified as an integer.

**Example:** `0`

### **Visualize trace line** — Visualize ray traces on (default) | off

Whether to enable Unreal Engine trace line visualization for the ray tracer.

### **Enable optimization** — Enable optimization on (default) | off

Whether to enable optimization of the ray tracer. Enabling this
parameter allows the block to perform concurrent traces. Enable this parameter when the
number of traces is large and your machine has multiple cores.

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time of the block, in seconds, specified as a positive scalar. The 3D simulation
environment frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block inherits its sample time from
the Simulation 3D Scene Configuration block.

## Libraries

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Vehicle / Components Simulink 3D Animation / Simulation 3D / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2025a: Set coordinate system parameter

Set the **Coordinate system** parameter in
the Simulation 3D Ray Tracer block to represent the coordinate system for actor transformation
in the 3D environment.

## Description

Implement ray tracing in 3D environment

The Simulation 3D Ray Tracer block implements ray tracing to get the positions, surface normals,
surface identifiers, and distances for objects in the scene. You can specify block parameters
that configure the ray origins, directions, and lengths to adjust the ray trace sensor pattern
for your scene and test scenario.

**Tip**

Verify that the Simulation 3D Scene
Configuration block executes before the Simulation 3D Ray Tracer block. That way, the
Unreal Engine® 3D visualization environment prepares the data before the Simulation 3D Ray Tracer block
receives it. To check the block execution order, right-click the blocks and select
**Properties**. On the **General** tab, confirm these
**Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Terrain Sensor — `1`

For more information about execution order, see Control and Display Execution Order (Simulink).

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.
