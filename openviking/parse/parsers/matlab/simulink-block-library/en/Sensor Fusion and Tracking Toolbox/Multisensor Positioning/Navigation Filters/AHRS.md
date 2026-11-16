---
type: simulink-block
title: 'AHRS'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Navigation Filters'
documentation_page: 'ahrs'
documentation_source_path: 'ref/ahrs.html'
language: en
---

# AHRS

## Ports

### Input

### **Accel** — Accelerometer readings in sensor body coordinate system (m/s2) *N*-by-3 matrix of real scalar

Accelerometer readings in the sensor body coordinate system in
m/s2, specified as an *N*-by-3 matrix of
real scalars. *N* is the number of samples, and the three columns of
`Accel` represent the [*x*
*y*
*z*] measurements, respectively.

**Data Types:** `single` | `double`

### **Gyro** — Gyroscope readings in sensor body coordinate system (rad/s) *N*-by-3 matrix of real scalar

Gyroscope readings in the sensor body coordinate system in rad/s, specified as an
*N*-by-3 matrix of real scalars. *N* is the number
of samples, and the three columns of `Gyro` represent the
[*x*
*y*
*z*] measurements, respectively.

**Data Types:** `single` | `double`

### **Mag** — Magnetometer readings in sensor body coordinate system (µT) *N*-by-3 matrix of real scalar

Magnetometer readings in the sensor body coordinate system in µT, specified as an
*N*-by-3 matrix of real scalars. *N* is the number
of samples, and the three columns of `magReadings` represent the
[*x*
*y*
*z*] measurements, respectively.

**Data Types:** `single` | `double`
### Output

### **Orientation** — Orientation of sensor body frame relative to navigation frame *M*-by-4 array of scalar | 3-by-3-by-*M*-element rotation matrix

Orientation of the sensor body frame relative to the navigation frame, return as
an *M*-by-4 array of scalars or a 3-by-3-by-*M*
array of rotation matrices. Each row the of the *N*-by-4 array is
assumed to be the four elements of a `quaternion`. The number of input samples, *N*, and the
**Decimation Factor** parameter determine the output size
*M*.

**Data Types:** `single` | `double`

### **Angular Velocity** — Angular velocity in sensor body coordinate system (rad/s) *M*-by-3 array of real scalar (default)

Angular velocity with gyroscope bias removed in the sensor body coordinate system
in rad/s, returned as an *M*-by-3 array of real scalars. The number
of input samples, *N*, and the **Decimation Factor**
parameter determine the output size *M*.

**Data Types:** `single` | `double`

## Parameters

#### Main

### **Reference frame** — Navigation reference frame `NED` (default) | `ENU`

Navigation reference frame, specified as `NED` (North-East-Down) or
`ENU` (East-North-Up).

### **Decimation factor** — Decimation factor `1` (default) | positive integer

Decimation factor by which to reduce the input sensor data rate, specified as a
positive integer.

The number of rows of the inputs –– **Accel**,
**Gyro** , and **Mag** –– must be a multiple of the
decimation factor.

**Data Types:** `single` | `double`

### **Initial process noise** — Initial process noise `ahrsfilter.defaultProcessNoise` (default) | 12-by-12 matrix of real scalar

Initial process noise, specified as a 12-by-12 matrix of real scalars. The default
value, `ahrsfilter.defaultProcessNoise`, is a 12-by-12 diagonal matrix
as:

```
  Columns 1 through 6

   0.000006092348396                   0                   0                   0                   0                   0
                   0   0.000006092348396                   0                   0                   0                   0
                   0                   0   0.000006092348396                   0                   0                   0
                   0                   0                   0   0.000076154354947                   0                   0
                   0                   0                   0                   0   0.000076154354947                   0
                   0                   0                   0                   0                   0   0.000076154354947
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0

  Columns 7 through 12

                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
                   0                   0                   0                   0                   0                   0
   0.009623610000000                   0                   0                   0                   0                   0
                   0   0.009623610000000                   0                   0                   0                   0
                   0                   0   0.009623610000000                   0                   0                   0
                   0                   0                   0   0.600000000000000                   0                   0
                   0                   0                   0                   0   0.600000000000000                   0
                   0                   0                   0                   0                   0   0.600000000000000
```

**Data Types:** `single` | `double`

### **Orientation format** — Orientation output format `'quaternion'` (default) | `'Rotation matrix'`

Output orientation format, specified as `'quaternion'` or
`'Rotation matrix'`:

- `'quaternion'` –– Output is an *M*-by-4
  array of real scalars. Each row of the array represents the four components of a
  `quaternion`.
- `'Rotation matrix'` –– Output is a
  3-by-3-by-*M* rotation matrix.

The output size *M* depends on the input dimension
*N* and the **Decimation Factor** parameter.

**Data Types:** `char` | `string`

### **Simulate using** — Type of simulation to run `Interpreted Execution` (default) | `Code Generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB® interpreter. This option shortens startup time. In
  `Interpreted execution` mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations as long as the model does not change. This option requires additional
  startup time.

#### Measurement Noise

### **Accelerometer noise ((m/s2)2)** — Variance of accelerometer signal noise ((m/s2)2) `0.0001924722` (default) | positive real scalar

Variance of accelerometer signal noise in
(m/s2)2, specified as a positive
real scalar.

**Data Types:** `single` | `double`

### **Gyroscope noise ((rad/s)2)** — Variance of gyroscope signal noise ((rad/s)2) `9.1385e-5` (default) | positive real scalar

Variance of gyroscope signal noise in (rad/s)2, specified
as a positive real scalar.

**Data Types:** `single` | `double`

### **Magnetometer noise (μT2)** — Variance of magnetometer signal noise (μT2) `0.1` (default) | positive real scalar

Variance of magnetometer signal noise in μT2, specified
as a positive real scalar.

**Data Types:** `single` | `double`

### **Gyroscope drift noise (rad/s)** — Variance of gyroscope offset drift ((rad/s)2) `3.0462e-13` (default) | positive real scalar

Variance of gyroscope offset drift in (rad/s)2, specified
as a positive real scalar.

**Data Types:** `single` | `double`

#### Environmental Noise

### **Linear acceleration noise ((m/s2)2)** — Variance of linear acceleration noise (m/s2)2 `0.0096236100000000012` (default) | positive real scalar

Variance of linear acceleration noise in
(m/s2)2, specified as a positive
real scalar. Linear acceleration is modeled as a lowpass-filtered white noise
process.

**Data Types:** `single` | `double`

### **Magnetic disturbance noise (μT2)** — Variance of magnetic disturbance noise ((μT)2) `0.5` (default) | real finite positive scalar

Variance of magnetic disturbance noise in μT2, specified
as a real finite positive scalar.

**Data Types:** `single` | `double`

### **Linear acceleration decay factor** — Decay factor for linear acceleration drift `0.5` (default) | scalar in the range [0,1)

Decay factor for linear acceleration drift, specified as a scalar in the range
[0,1). If linear acceleration changes quickly, set this parameter to a lower value. If
linear acceleration changes slowly, set this parameter to a higher value. Linear
acceleration drift is modeled as a lowpass-filtered white noise process.

**Data Types:** `single` | `double`

### **Magnetic disturbance decay factor** — Decay factor for magnetic disturbance `0.5` (default) | positive scalar in the range [0,1]

Decay factor for magnetic disturbance, specified as a positive scalar in the range
[0,1]. Magnetic disturbance is modeled as a first order Markov process.

**Data Types:** `single` | `double`

### **Magnetic field strength (μT)** — Magnetic field strength (μT) `50` (default) | real positive scalar

Magnetic field strength in μT, specified as a real positive scalar. The magnetic
field strength is an estimate of the magnetic field strength of the Earth at the current
location.

**Data Types:** `single` | `double`

## Libraries

Navigation Toolbox / Multisensor Positioning / Navigation Filters Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Navigation Filters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- This block also supports strict single-precision code generation.

## Version History

**Introduced in R2020a**

## Description

Orientation from accelerometer, gyroscope, and magnetometer readings

The `AHRS`
Simulink® block fuses accelerometer, magnetometer, and gyroscope sensor data to estimate
device orientation.
