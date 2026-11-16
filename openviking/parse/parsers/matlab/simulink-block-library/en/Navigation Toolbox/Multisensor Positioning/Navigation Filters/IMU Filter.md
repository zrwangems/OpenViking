---
type: simulink-block
title: 'IMU Filter'
family: 'nav'
product_id: 'nav'
product_name: 'Navigation Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Navigation Filters'
documentation_page: 'imufilter'
documentation_source_path: 'ref/imufilter.html'
language: en
---

# IMU Filter

## Ports

### Input

### **Accel** — Accelerometer readings in sensor body coordinate system (m/s2) matrix

Accelerometer readings in the sensor body coordinate system in
m/s2, specified as an *N*-by-3 matrix of
real numbers. *N* is the number of samples, and each row is of the
form [*x*
*y*
*z*].

**Data Types:** `single` | `double`

### **Gyro** — Gyroscope readings in sensor body coordinate system (rad/s) matrix

Gyroscope readings in the sensor body coordinate system in rad/s, specified as an
*N*-by-3 matrix of real numbers. *N* is the number
of samples, and each row is of the form [*x*
*y*
*z*].

**Data Types:** `single` | `double`
### Output

### **Orientation** — Orientation of sensor body frame relative to navigation frame matrix | array

Orientation of the sensor body frame relative to the navigation frame, returned as
an *M*-by-4 matrix of real numbers or a
3-by-3-by-*M* array. Each row of the *M*-by-4
matrix represents the four components of a `quaternion`. Each
page of the 3-by-3-by-*M* array represents a 3-by-3 rotation
matrix.

The number of input samples *N* and the **Decimation
factor** parameter determine the output size *M*.

The output format depends on the value of the **Orientation
format** parameter.

**Data Types:** `single` | `double`

### **Angular Velocity** — Angular velocity in sensor body coordinate system (rad/s) matrix

Angular velocity, with gyroscope bias removed, in the sensor body coordinate
system in rad/s, returned as an *M*-by-3 matrix of real
numbers.

The number of input samples *N* and the **Decimation
factor** parameter determine the output size *M*.

**Data Types:** `single` | `double`

## Parameters

### **Reference frame** — Navigation reference frame `NED` (default) | `ENU`

Specify the navigation reference frame as `NED` (North-East-Down)
or `ENU` (East-North-Up).

### **Orientation format** — Orientation output format `quaternion` (default) | `Rotation Matrix`

Specify the format in which to output **Orientation** as
`quaternion` or `Rotation
matrix`.

- `quaternion` — **Orientation** outputs an
  *M*-by-4 matrix of real numbers. Each row of the matrix
  represents the four components of a `quaternion`.
- `Rotation matrix` — **Orientation** outputs a
  3-by-3-by-*M* array, in which each page of the array is a 3-by-3
  rotation matrix.

The number of input samples *N* and the **Decimation
factor** parameter determine the output size *M*.

### **Decimation factor** — Decimation factor `1` (default) | positive integer

Specify the decimation factor by which to reduce the input sensor data rate as a
positive integer.

The number of rows of the **Accel** and **Gyro** inputs must
be a multiple of the decimation factor.

### **Initial process noise** — Initial process noise `imufilter.defaultProcessNoise` (default) | 9-by-9 matrix of real numbers

Specify the initial process noise as a 9-by-9 matrix of real numbers. The
`imufilter.defaultProcessNoise` variable contains the default
value.

### **Accelerometer noise ((m/s2)2)** — Variance of accelerometer signal noise (m/s2)2 `0.0001924722` (default) | positive real scalar

Specify the variance of the accelerometer signal noise in
(m/s2)2 as a positive real
scalar.

### **Gyroscope noise ((rad/s)2)** — Variance of gyroscope signal noise (rad/s)2 `9.1385e-5` (default) | positive real scalar

Specify the variance of the gyroscope signal noise in
(rad/s)2 as a positive real scalar.

### **Gyroscope drift noise ((rad/s)2)** — Variance of gyroscope offset drift (rad/s)2 `3.0462e-13` (default) | positive real scalar

Specify the variance of the gyroscope offset drift in
(rad/s)2 as a positive real scalar.

### **Linear acceleration noise ((m/s2)2)** — Variance of linear acceleration noise (m/s2)2 `0.0096236100000000012` (default) | positive real scalar

Specify the variance of linear acceleration noise in
(m/s2)2 as a positive real
scalar. The block models linear acceleration as a lowpass-filtered white noise
process.

### **Linear acceleration decay factor** — Decay factor for linear acceleration drift `0.5` (default) | scalar in the range [0 1)

Specify the decay factor for linear acceleration drift as a scalar in the range [0
1). If linear acceleration changes quickly, set this parameter to a lower value. If
linear acceleration changes slowly, set this parameter to a higher value. The block
models linear acceleration drift as a lowpass-filtered white noise process.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Select the type of simulation to run from these options:

- `Interpreted execution` — Simulate the model using the
  MATLAB® interpreter. This option reduces startup time, but has a slower
  simulation speed than `Code generation`. In this mode, you
  can debug the source code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time you run a simulation in this mode, Simulink generates C code for the block. Simulink reuses the C code for subsequent simulations, as long as the model
  does not change. This option requires additional startup time for the initial run,
  but increases the speed of subsequent simulations relative to
  `Interpreted execution`.

## Libraries

Navigation Toolbox / Multisensor Positioning / Navigation Filters Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Navigation Filters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- This block also supports strict single-precision code generation.

## Version History

**Introduced in R2023b**

## Description

Estimate orientation using IMU Filter

The IMU Filter
Simulink® block fuses accelerometer and gyroscope sensor data to estimate device
orientation.
