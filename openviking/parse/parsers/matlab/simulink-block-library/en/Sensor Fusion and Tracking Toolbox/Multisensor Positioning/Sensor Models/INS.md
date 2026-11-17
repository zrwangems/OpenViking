---
type: simulink-block
title: 'INS'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Sensor Models'
documentation_page: 'ins'
documentation_source_path: 'ref/ins.html'
language: en
---

# INS

## Ports
```yaml
ports:
- name: Position
  summary: Position of INS sensor *N*-by-3 real-valued matrix
  direction: input
  data_types: single | double
- name: Velocity
  summary: Velocity of INS sensor *N*-by-3 real-valued matrix of scalar
  direction: input
  data_types: single | double
- name: Orientation
  summary: Orientation of INS sensor 3-by-3-by-*N* real-valued array | *N*-by-4 real-valued matrix | *N*-by-3 matrix of Euler
    angles
  direction: input
  data_types: single | double
- name: Acceleration
  summary: Acceleration of INS sensor *N*-by-3 real-valued matrix
  direction: input
  data_types: single | double
- name: AngularVelocity
  summary: Angular velocity of INS sensor *N*-by-3 real-valued matrix
  direction: input
  data_types: single | double
- name: HasGNSSFix
  summary: Enable GNSS fix *N*-by-1 logical vector
  direction: input
  data_types: single | double
- name: Position
  summary: Position of INS sensor *N*-by-3 real-valued matrix
  direction: output
  data_types: single | double
- name: Velocity
  summary: Velocity of INS sensor *N*-by-3 real-valued matrix
  direction: output
  data_types: single | double
- name: Orientation
  summary: Orientation of INS sensor 3-by-3-by-*N* real-valued array | *N*-by-4 real-valued matrix
  direction: output
  data_types: single | double
- name: Acceleration
  summary: Acceleration of INS sensor *N*-by-3 real-valued matrix
  direction: output
  data_types: single | double
- name: AngularVelocity
  summary: Angular velocity of INS sensor *N*-by-3 real-valued matrix
  direction: output
  data_types: single | double
```

### Input

### **Position** — Position of INS sensor *N*-by-3 real-valued matrix

Position of the INS sensor relative to the navigation frame, in meters, specified
as an *N*-by-3 real-valued matrix. *N* is the number
of samples.

**Data Types:** `single` | `double`

### **Velocity** — Velocity of INS sensor *N*-by-3 real-valued matrix of scalar

Velocity of the INS sensor relative to the navigation frame, in meters per second,
specified as an *N*-by-3 real-valued matrix. *N* is
the number of samples.

**Data Types:** `single` | `double`

### **Orientation** — Orientation of INS sensor 3-by-3-by-*N* real-valued array | *N*-by-4 real-valued matrix | *N*-by-3 matrix of Euler angles

Orientation of the INS sensor relative to the navigation frame, specified as one
of these formats:

- A 3-by-3-by-*N* real-valued array, where each page of the
  array (3-by-3 matrix) is a rotation matrix.
- An *N*-by-4 real-valued matrix, where each row of the
  matrix is the four elements of a quaternion.
- An *N*-by-3 matrix of Euler angles, where each row of the
  matrix is the three Euler angles corresponding to the z-y-x rotation
  convention.

*N* is the number of samples.

**Data Types:** `single` | `double`

### **Acceleration** — Acceleration of INS sensor *N*-by-3 real-valued matrix

Acceleration of the INS sensor relative to the navigation frame, in meters per
second squared, specified as an *N*-by-3 real-valued matrix.
*N* is the number of samples.

#### Dependencies

To enable this input port, select **Use acceleration and angular
velocity**.

**Data Types:** `single` | `double`

### **AngularVelocity** — Angular velocity of INS sensor *N*-by-3 real-valued matrix

Angular velocity of the INS sensor relative to the navigation frame, in degrees
per second, specified as an *N*-by-3 real-valued matrix.
*N* is the number of samples.

#### Dependencies

To enable this input port, select **Use acceleration and angular
velocity**.

**Data Types:** `single` | `double`

### **HasGNSSFix** — Enable GNSS fix *N*-by-1 logical vector

Enable GNNS fix, specified as an *N*-by-1 logical vector.
*N* is the number of samples. Specify this input as
`false` to simulate the loss of a GNSS receiver fix. When a GNSS
receiver fix is lost, position measurements drift at a rate specified by the
**Position error factor** parameter.

#### Dependencies

To enable this input port, select **Enable HasGNSSFix
port**.

**Data Types:** `single` | `double`
### Output

### **Position** — Position of INS sensor *N*-by-3 real-valued matrix

Position of the INS sensor relative to the navigation frame, in meters, returned
as an *N*-by-3 real-valued matrix. *N* is the number
of samples in the input.

**Data Types:** `single` | `double`

### **Velocity** — Velocity of INS sensor *N*-by-3 real-valued matrix

Velocity of the INS sensor relative to the navigation frame, in meters per second,
returned as an *N*-by-3 real-valued matrix. *N* is
the number of samples in the input.

**Data Types:** `single` | `double`

### **Orientation** — Orientation of INS sensor 3-by-3-by-*N* real-valued array | *N*-by-4 real-valued matrix

Orientation of the INS sensor relative to the navigation frame, returned as one of
the formats:

- A 3-by-3-by-*N* real-valued array, where each page of the
  array (3-by-3 matrix) is a rotation matrix.
- An *N*-by-4 real-valued matrix, where each row of the
  matrix is the four elements of a quaternion.
- An *N*-by-3 matrix of Euler angles, where each row of the
  matrix is the three Euler angles corresponding to the z-y-x rotation
  convention.

*N* is the number of samples in the input.

**Data Types:** `single` | `double`

### **Acceleration** — Acceleration of INS sensor *N*-by-3 real-valued matrix

Acceleration of the INS sensor relative to the navigation frame, in meters per
second squared, returned as an *N*-by-3 real-valued matrix.
*N* is the number of samples.

#### Dependencies

To enable this output port, select **Use acceleration and angular
velocity**.

**Data Types:** `single` | `double`

### **AngularVelocity** — Angular velocity of INS sensor *N*-by-3 real-valued matrix

Angular velocity of the INS sensor relative to the navigation frame, in degrees
per second, returned as an *N*-by-3 real-valued matrix.
*N* is the number of samples.

#### Dependencies

To enable this output port, select **Use acceleration and angular
velocity**.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Mounting location (m)
  summary: Location of sensor on platform (m) [0 0 0] (default) | three-element real-valued vector of form [*x* *y* *z*]
  group: ''
- name: Roll (X-axis) accuracy (deg)
  summary: Accuracy of roll measurement (deg) 0.2 (default) | nonnegative real scalar
  group: ''
- name: Pitch (Y-axis) accuracy (deg)
  summary: Accuracy of pitch measurement (deg) 0.2 (default) | nonnegative real scalar
  group: ''
- name: Yaw (Z-axis) accuracy (deg)
  summary: Accuracy of yaw measurement (deg) 1 (default) | nonnegative real scalar
  group: ''
- name: Position accuracy (m)
  summary: Accuracy of position measurement (m) 1 (default) | nonnegative real scalar | 1-by-3 vector of nonnegative values
  group: ''
- name: Velocity accuracy (m/s)
  summary: Accuracy of velocity measurement (m/s) 0.05 (default) | nonnegative real scalar
  group: ''
- name: Use acceleration and angular velocity
  summary: Use acceleration and angular velocity off (default) | on
  group: ''
- name: Acceleration accuracy (m/s2)
  summary: Accuracy of acceleration measurement (m/s2) 0 (default) | nonnegative real scalar
  group: ''
- name: Angular velocity accuracy (deg/s)
  summary: Accuracy of angular velocity measurement (deg/s) 0 (default) | nonnegative real scalar
  group: ''
- name: Enable HasGNSSFix port
  summary: Enable HasGNSSFix input port off (default) | on
  group: ''
- name: Position error factor
  summary: Position error factor (m) [0 0 0] (default) | nonnegative scalar | 1-by-3 real-valued vector
  group: ''
- name: Seed
  summary: Initial seed for randomization 67 (default) | nonnegative integer
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code Generation (default) | Interpreted Execution
  group: ''
```

### **Mounting location (m)** — Location of sensor on platform (m) `[0 0 0]` (default) | three-element real-valued vector of form [*x* *y* *z*]

Location of the sensor on the platform, in meters, specified as a three-element
real-valued vector of the form [*x*
*y*
*z*]. The vector defines the offset of the sensor origin from the
origin of the platform.

**Data Types:** `single` | `double`

### **Roll (X-axis) accuracy (deg)** — Accuracy of roll measurement (deg) `0.2` (default) | nonnegative real scalar

Accuracy of the roll measurement of the sensor body in degrees, specified as a
nonnegative real scalar.

Roll is defined as rotation around the *x*-axis of the sensor body.
Roll noise is modeled as white process noise with standard deviation equal to the
specified **Roll accuracy** in degrees.

**Data Types:** `single` | `double`

### **Pitch (Y-axis) accuracy (deg)** — Accuracy of pitch measurement (deg) `0.2` (default) | nonnegative real scalar

Accuracy of the pitch measurement of the sensor body in degrees, specified as a
nonnegative real scalar.

Pitch is defined as rotation around the *y*-axis of the sensor
body. Pitch noise is modeled as white process noise with standard deviation equal to the
specified **Pitch accuracy** in degrees.

**Data Types:** `single` | `double`

### **Yaw (Z-axis) accuracy (deg)** — Accuracy of yaw measurement (deg) `1` (default) | nonnegative real scalar

Accuracy of the yaw measurement of the sensor body in degrees, specified as a
nonnegative real scalar.

Yaw is defined as rotation around the *z*-axis of the sensor body.
Yaw noise is modeled as white process noise with standard deviation equal to the
specified **Yaw accuracy** in degrees.

**Data Types:** `single` | `double`

### **Position accuracy (m)** — Accuracy of position measurement (m) `1` (default) | nonnegative real scalar | 1-by-3 vector of nonnegative values

Accuracy of the position measurement of the sensor body in meters, specified as a
nonnegative real scalar or a 1-by-3 vector of nonnegative values. If you specify the
parameter as a scalar value, then the block sets the accuracy of all three position
components to this value.

Position noise is modeled as white process noise with a standard deviation equal to
the specified **Position accuracy** in meters.

**Data Types:** `single` | `double`

### **Velocity accuracy (m/s)** — Accuracy of velocity measurement (m/s) `0.05` (default) | nonnegative real scalar

Accuracy of the velocity measurement of the sensor body in meters per second,
specified as a nonnegative real scalar.

Velocity noise is modeled as white process noise with a standard deviation equal to
the specified **Velocity accuracy** in meters per second.

**Data Types:** `single` | `double`

### **Use acceleration and angular velocity** — Use acceleration and angular velocity off (default) | on

Select this check box to enable the block inputs of acceleration and angular
velocity through the **Acceleration** and
**AngularVelocity** input ports, respectively. Meanwhile, the block
outputs the acceleration and angular velocity measurements through the
**Acceleration** and **AngularVelocity** output
ports, respectively. Additionally, selecting this parameter enables you to specify the
**Acceleration accuracy** and **Angular velocity
accuracy** parameters.

### **Acceleration accuracy (m/s2)** — Accuracy of acceleration measurement (m/s2) `0` (default) | nonnegative real scalar

Accuracy of the acceleration measurement of the sensor body in meters, specified as
a nonnegative real scalar.

Acceleration noise is modeled as white process noise with a standard deviation equal
to the specified **Acceleration accuracy** in meters per second
squared.

#### Dependencies

To enable this parameter, select **Use acceleration and angular
velocity**.

**Data Types:** `single` | `double`

### **Angular velocity accuracy (deg/s)** — Accuracy of angular velocity measurement (deg/s) `0` (default) | nonnegative real scalar

Accuracy of the angular velocity measurement of the sensor body in meters, specified
as a nonnegative real scalar.

Angular velocity noise is modeled as white process noise with a standard deviation
equal to the specified **Angular velocity accuracy** in degrees per
second.

#### Dependencies

To enable this parameter, select **Use acceleration and angular
velocity**.

**Data Types:** `single` | `double`

### **Enable HasGNSSFix port** — Enable `HasGNSSFix` input port off (default) | on

Select this check box to enable the **HasGNSSFix** input port. When
the **HasGNSSFix** input is specified as `false`,
position measurements drift at a rate specified by the **Position error
factor** parameter.

### **Position error factor** — Position error factor (m) `[0 0 0]` (default) | nonnegative scalar | 1-by-3 real-valued vector

Position error factor without GNSS fix, specified as a scalar or a 1-by-3
real-valued vector. If you specify the parameter as a scalar value, then the block sets
the position error factors of all three position components to this value.

When the **HasGNSSFix** input is specified as
`false`, the position error grows at a quadratic rate due to constant
bias in the accelerometer. The position error for a position component
*E*(*t*) can be expressed as
*E*(*t*) =
1/2*α**t*2, where
*α* is the position error factor for the corresponding component and
*t* is the time since the GNSS fix is lost. The computed
*E*(*t*) values for the *x*,
*y*, and *z* components are added to the
corresponding position components of the **Position** output.

#### Dependencies

To enable this parameter, select **Enable HasGNSSFix
port**.

**Data Types:** `double`

### **Seed** — Initial seed for randomization `67` (default) | nonnegative integer

Initial seed of a random number generator algorithm, specified as a nonnegative
integer.

**Data Types:** `single` | `double`

### **Simulate using** — Type of simulation to run `Code Generation` (default) | `Interpreted Execution`

- `Interpreted execution` — Simulate the model using the
  MATLAB® interpreter. This option shortens startup time. In
  `Interpreted execution` mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time that you run a simulation, Simulink® generates C code for the block. The C code is reused for subsequent
  simulations if the model does not change. This option requires additional startup
  time.
## Libraries

Navigation Toolbox / Multisensor Positioning / Sensor Models Automated Driving Toolbox / Driving Scenario and Sensor Modeling Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Sensor Models UAV Toolbox / UAV Scenario and Sensor Modeling

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020b**

## Description

Simulate INS sensor

The block simulates an INS sensor, which outputs noise-corrupted position, velocity, and
orientation based on the corresponding inputs. The block can also optionally output
acceleration and angular velocity based on the corresponding inputs. To change the level of
noise present in the output, you can vary the roll, pitch, yaw, position, velocity,
acceleration, and angular velocity accuracies. The accuracy is defined as the standard
deviation of the noise.
