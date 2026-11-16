---
type: simulink-block
title: 'Simulation 3D Ultrasonic Array'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'simulation3dultrasonicarray'
documentation_source_path: 'simulation3dultrasonicarray.html'
language: en
---

# Simulation 3D Ultrasonic Array

## Ports

### Output

### **Has object** — Flag indicating whether any detectable object is present in the sensor field-of-view `true` | `false`

Flag indicating whether any detectable object is present in the sensor
field-of-view, returned as a logical scalar. An object is considered detectable if its
closest distance to the sensor is greater than the minimum detection-only range
specified in the **Detection ranges (m)** parameter.

### **Has range** — Flag indicating whether range measurement is possible for any object present in the sensor field-of-view `true` | `false`

Flag indicating whether range measurement is possible for any object present in
the sensor field-of-view, returned as a logical scalar. For any object in the
field-of-view, range measurement is possible if its closest distance to the sensor is
greater than the minimum-distance range specified in the
`Detection ranges (m)` parameter.

### **Range** — Distance measurement to the closest object nonnegative scalar

Distance measurement to the closest object, returned as a nonnegative
scalar.

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

Select this parameter to specify an offset from the mounting location by using the
**Relative translation [X, Y,
Z]** and **Relative rotation [Roll, Pitch, Yaw]** parameters.

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

### **Sample time** — Sample time `-1` (default) | positive scalar

Sample time of the block, in seconds, specified as a positive scalar. The 3D simulation
environment frame rate is the inverse of the sample time.

If you set the sample time to `-1`, the block inherits its sample time from
the Simulation 3D Scene Configuration block.

### Sensor Parameters

#### Intrinsic parameters

### **Relative mounting locations** — Relative mounting locations of individual sensors in the ultrasonic array `[[0, -0.67, 0]; [0, -0.22, 0]; [0, 0.22, 0]; [0, 0.67, 0]]` (default) | real-valued *N*-by-`3` array

Relative mounting locations of individual sensors in the ultrasonic array,
specified as a real-valued *N*-by-`3` array.
*N* is the number of sensors in the ultrasonic array and the
locations are relative to the sensor mounting position specified by the
`Mounting Location` parameter. Each row of the array must be a
1-by-3 vector of the form [*X*, *Y*,
*Z*]. Units are in meters.

### **Relative mounting rotations** — Relative mounting rotations of individual sensors in the ultrasonic array `zeros(4,3)` (default) | real-valued *N*-by-`3` array

Relative mounting rotations of individual sensors in the ultrasonic array,
specified as a real-valued *N*-by-`3` array.
*N* is the number of sensors in the ultrasonic array and the
rotations are relative to the sensor mounting orientation specified by the
`Mounting Location` parameter. Each row of the array must be a
1-by-3 vector of the form [*roll*, *pitch*,
*yaw*].

### **Horizontal Field of view (deg)** — Horizontal field of view of ultrasonic array `70` (default) | positive real scalar

Horizontal field of view of ultrasonic array, specified as a positive real scalar.
This field of view defines the total angular extent spanned by all sensors of the
ultrasonic array in the horizontal direction relative to their orientations. You must
specify the horizontal field of view `horizontalFOV` in the range (0,
360]. Units are in degrees.

### **Vertical field of view (deg)** — Vertical field of view of ultrasonic array `35` (default) | positive real scalar

Vertical field of view of ultrasonic array, specified as a positive real scalar.
This field of view defines the total angular extent spanned by all sensors of the
ultrasonic array in the vertical direction relative to their orientations. You must
specify the vertical field of view in the range (0, 180]. Units are in degrees.

### **Detection ranges (m)** — Detection range vector of ultrasonic array (m) `[0.03 0.15 5.5]` (default) | 1-by-3 nonnegative real-valued vector of form `[minDetOnlyRange minDistRange maxDistRange]`

Detection range vector of the ultrasonic array, specified as a 1-by-3 nonnegative
real-valued vector of the form `[minDetOnlyRange minDistRange
maxDistRange]`, where `minDetOnlyRange < minDistRange <
maxDistRange`. Units are in meters. These values determine the detections
and distance values returned by the ultrasonic array.

- When the detected object is at a distance between
  `minDistRange` and `maxDistRange`, the
  sensor returns a positive distance value.
- When the detected object is at a distance between
  `minDetOnlyRange` and `minDistRange`, the
  sensor detects the object, but cannot determine the distance and returns a value
  of `0`.
- When the object is at a distance below `minDetOnlyRange` or
  above `maxDistRange`, the sensor returns an empty cell
  array.

#### Signal parameters

### **Acoustic frequency (kHz)** — Frequency of sound waves used by all sensor emitters in ultrasonic array `50` (default) | positive real scalar

Frequency of sound waves used by all sensor emitters in the ultrasonic array,
specified as a positive real scalar. Units are in kHz.

### **Sampling frequency (kHz)** — Sampling frequency of all sensor receivers in ultrasonic array `500` (default) | positive real scalar

Sampling frequency of all sensor receivers in the ultrasonic array, specified as a
positive real scalar. To sample a signal of a given frequency, the sampling frequency
of the receiver must be at least two times that frequency. Units are in kHz.

### **Pulse width (s)** — Pulse width of ultrasonic waves used by all sensors in ultrasonic array `1e-6` (default) | positive real scalar

Pulse width of the ultrasonic waves used by all sensors in the ultrasonic array,
specified as a positive real scalar.

### **Gain** — Vector gain for sound signal used by sensors in ultrasonic array `[1, 0]` (default) | real-valued scalar | real-valued `1`-by-`2` vector

Vector gain for the sound signal used by the sensors in ultrasonic array,
real-valued scalar or a `1`-by-`2` vector of the
form `[a, b]`. The blocks multiplies the scalar gain as a constant,
and the vector gain as a time signal of the form `a + b*t` with the
ultrasonic signal.

### **Sound speed (m/s)** — Speed of sound in environment `330` (default) | positive real scalar

Speed of sound in the environment, specified as a positive real scalar. Units are
in m/s.

### Ground Truth

### **Output location and orientation** — Output location and orientation of sensor `off` (default) | `on`

Select this parameter to output the translation and rotation of the
sensor at the **Translation** and
**Rotation** ports,
respectively.

## Libraries

Automated Driving Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

### R2025a: Set coordinate system parameter

Set the **Coordinate system** parameter in
the Simulation 3D Ultrasonic Array block to represent the coordinate system for actor transformation
in the 3D environment.

## Description

Ultrasonic sensor model with tunable acoustic parameters in 3D simulation environment

The Simulation 3D Ultrasonic Array block generates detections from range
measurements taken by an array of ultrasonic sensors with tunable acoustic parameters, mounted
on an ego vehicle in a 3D simulation environment. This environment is rendered using the
Unreal Engine® from Epic Games®. The block calculates range measurements based on the distance between the
sensor and the closest point on the detected object. The block also provides parameters to
control the waveform of the ultrasonic signal used by the sensor to calculate range
measurements.

If you set **Sample time** to `-1`, the block uses the
sample time specified in the Simulation 3D Scene Configuration block. To use
this sensor, you must include a Simulation 3D Scene Configuration block in your
model.

**Tip**

The Simulation 3D Scene Configuration
block must execute before the Simulation 3D Ultrasonic Array block. That way,
the Unreal Engine 3D visualization environment prepares the data before the Simulation 3D
Ultrasonic Array block receives it. To check the block execution order,
right-click the blocks and select **Properties**. On the
**General** tab, confirm these **Priority** settings:

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Ultrasonic Array — `1`

For more information about execution order, see Control and Display Execution Order (Simulink).

The **Coordinate system** parameter of the block specifies how the actor transformations are applied in the 3D environment. The output of the block also follows the specified coordinate system.
