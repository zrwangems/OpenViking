---
type: simulink-block
title: 'Complementary Filter'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Navigation Filters'
documentation_page: 'complementaryfilter'
documentation_source_path: 'ref/complementaryfilter.html'
language: en
---

# Complementary Filter

## Ports
```yaml
ports:
- name: Accel
  summary: Accelerometer readings in sensor body coordinate system (m/s2) matrix
  direction: input
  data_types: single | double
- name: Gyro
  summary: Gyroscope readings in sensor body coordinate system (rad/s) matrix
  direction: input
  data_types: single | double
- name: Mag
  summary: Magnetometer readings in sensor body coordinate system (µT) matrix
  direction: input
  data_types: single | double
- name: Orientation
  summary: Orientation of sensor body frame relative to navigation frame matrix | array
  direction: output
  data_types: single | double
- name: Angular Velocity
  summary: Angular velocity in sensor body coordinate system (rad/s) matrix
  direction: output
  data_types: single | double
```

### Input

### **Accel** — Accelerometer readings in sensor body coordinate system (m/s2) matrix

Accelerometer readings in the sensor body coordinate system in
m/s2, specified as an *N*-by-3 matrix of
real numbers. *N* is the number of samples, and the each row is of
the form [*x*
*y*
*z*].

**Data Types:** `single` | `double`

### **Gyro** — Gyroscope readings in sensor body coordinate system (rad/s) matrix

Gyroscope readings in the sensor body coordinate system in rad/s, specified as an
*N*-by-3 matrix of real numbers. *N* is the number
of samples, and the each row is of the form [*x*
*y*
*z*].

**Data Types:** `single` | `double`

### **Mag** — Magnetometer readings in sensor body coordinate system (µT) matrix

Magnetometer readings in the sensor body coordinate system in µT, specified as an
*N*-by-3 matrix of real numbers. *N* is the number
of samples, and the each row is of the form [*x*
*y*
*z*].

#### Dependencies

To enable this input port, select the `Enable Magnetometer
input` parameter.

**Data Types:** `single` | `double`
### Output

### **Orientation** — Orientation of sensor body frame relative to navigation frame matrix | array

Orientation of the sensor body frame relative to the navigation frame, returned as
an *M*-by-4 matrix of real numbers or a
3-by-3-by-*M* array. Each row of the *M*-by-4
matrix represents the four components of a `quaternion`. Each
page of the 3-by-3-by-*M* array represents a 3-by-3 rotation
matrix.

The number of input samples, *N*, determines the output size,
*M*.

The output format depends on the value of the `Orientation format`
parameter.

**Data Types:** `single` | `double`

### **Angular Velocity** — Angular velocity in sensor body coordinate system (rad/s) matrix

Angular velocity, with gyroscope bias removed, in the sensor body coordinate
system in rad/s, returned as an *M*-by-3 matrix of real
numbers.

The number of input samples, *N*, determines the output size,
*M*.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Reference frame
  summary: Navigation reference frame NED (default) | ENU
  group: ''
- name: Orientation format
  summary: Orientation output format quaternion (default) | Rotation matrix
  group: ''
- name: Accelerometer gain
  summary: Accelerometer gain 0.01 (default) | real scalar in range [0, 1]
  group: ''
- name: Enable Magnetometer input
  summary: Accept magnetometer readings input on (default) | off
  group: ''
- name: Magnetometer gain
  summary: Magnetometer gain 0.01 (default) | real scalar in range [0, 1]
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted Execution (default) | Code Generation
  group: ''
```

### **Reference frame** — Navigation reference frame `NED` (default) | `ENU`

Specify the navigation reference frame as `NED` (North-East-Down)
or `ENU` (East-North-Up).

### **Orientation format** — Orientation output format `quaternion` (default) | `Rotation matrix`

Specify the format in which to output `Orientation` as
`quaternion` or `Rotation
matrix`:

- `quaternion` — `Orientation` outputs
  an *M*-by-4 matrix of real numbers. Each row of the matrix
  represents the four components of a `quaternion`.
- `Rotation matrix` — `Orientation`
  outputs a 3-by-3-by-*M* array, in which each page of the array is a
  3-by-3 rotation matrix.

The number of input samples, *N*, determines the output size,
*M*.

### **Accelerometer gain** — Accelerometer gain `0.01` (default) | real scalar in range [0, 1]

Specify the accelerometer gain as a real scalar in the range [0, 1]. The gain
determines how much the block trust the accelerometer measurement over the gyroscope
measurement for orientation estimation.

**Example:** `0.02`

**Data Types:** `single` | `double`

### **Enable Magnetometer input** — Accept magnetometer readings input `on` (default) | `off`

Select this parameter to enable input of magnetometer readings at the `Mag` port.

### **Magnetometer gain** — Magnetometer gain `0.01` (default) | real scalar in range [0, 1]

Specify the magnetometer gain as a real scalar in the range [0, 1]. The gain
determines how much the block trust the magnetometer measurement over the gyroscope
measurement for orientation estimation.

**Example:** `0.02`

**Data Types:** `single` | `double`

### **Simulate using** — Type of simulation to run `Interpreted Execution` (default) | `Code Generation`

Select the type of simulation to run from these options:

- `Interpreted execution` — Simulate the model using the
  MATLAB® interpreter. This option shortens startup time, but has a slower
  simulation speed than `Code generation`. In this mode, you
  can debug the source code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time you run a simulation in this mode, Simulink generates C code for the block. Simulink reuses the C code for subsequent simulations, as long as the model
  does not change. This option requires additional startup time, but the speed of
  subsequent simulations is comparable to `Interpreted
  execution`.
## Libraries

Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Navigation Filters Navigation Toolbox / Multisensor Positioning / Navigation Filters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Estimate orientation using complementary filter

The Complementary Filter
Simulink® block fuses accelerometer, magnetometer, and gyroscope sensor data to estimate
device orientation.
