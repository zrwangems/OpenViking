---
type: simulink-block
title: 'IMU'
family: 'fusion'
product_id: 'fusion'
product_name: 'Sensor Fusion and Tracking Toolbox'
documentation_release: R2025b
official_category: 'Multisensor Positioning / Sensor Models'
documentation_page: 'imu'
documentation_source_path: 'ref/imu.html'
language: en
---

# IMU

## Ports

### Input

### **Linear Acceleration** — Acceleration of IMU in local navigation coordinate system (m/s2) *N*-by-3 matrix of real scalar

Acceleration of the IMU in the local navigation coordinate system, specified as an
*N*-by-3 matrix of real scalars in meters per second squared.
*N* is the number of samples in the current frame. Do not include
the gravitational acceleration in this input since the sensor models gravitational
acceleration by default.

To specify the orientation of the IMU sensor body frame with respect to the local
navigation frame, use the **Orientation** input port.

**Data Types:** `single` | `double`

### **Angular Velocity** — Angular velocity of IMU in local navigation coordinate system (rad/s) *N*-by-3 matrix of real scalar

Angular velocity of the IMU sensor body frame in the local navigation coordinate
system, specified as an *N*-by-3 matrix of scalars in radians per
second. *N* is the number of samples in the current frame. To specify
the orientation of the IMU sensor body frame with respect to the local navigation
frame, use the **Orientation** input port.

**Data Types:** `single` | `double`

### **Orientation** — Orientation of IMU in local navigation coordinate system *N*-by-4 array of real scalar | 3-by-3-by-*N*-element rotation matrix

Orientation of the IMU sensor body frame with respect to the local navigation
coordinate system, specified as an *N*-by-4 array of real scalars or
a 3-by-3-by-*N* rotation matrix. Each row the of the
*N*-by-4 array is assumed to be the four elements of a `quaternion`. *N* is the number of samples in the current
frame.

**Data Types:** `single` | `double`

### **Temperature** — Temperature of IMU (℃) *N*-by-1 vector of real scalar

Temperature of IMU, specified as an *N*-by-1 vector of real
scalars in degrees Celsius.

#### Dependencies

To enable this port, in the **Parameters** tab, select
**Specify temperature from input port**.

**Data Types:** `single` | `double`

### **Magnetic Field** — Magnetic field vector in local navigation coordinate system (μT) *N*-by-3 matrix of real scalar

Magnetic field vector in the local navigation coordinate system, specified as an
*N*-by-3 matrix of scalars in microteslas.

#### Dependencies

To enable this port, in the **Parameters** tab, select
**Specify magnetic field from input port**.

**Data Types:** `single` | `double`
### Output

### **Accel** — Accelerometer measurement of IMU in sensor body coordinate system (m/s2) *N*-by-3 matrix of real scalar

Accelerometer measurement of the IMU in the sensor body coordinate system,
returned as an *N*-by-3 matrix of real scalars in meters per second
squared. *N* is the number of samples in the current frame.

**Data Types:** `single` | `double`

### **Gyro** — Gyroscope measurement of IMU in sensor body coordinate system (rad/s) *N*-by-3 matrix of real scalar

Gyroscope measurement of the IMU in the sensor body coordinate system, returned as
an *N*-by-3 matrix of real scalars in radians per second.
*N* is the number of samples in the current frame.

**Data Types:** `single` | `double`

### **Mag** — Magnetometer measurement of IMU in sensor body coordinate system (μT) *N*-by-3 matrix of real scalar

Magnetometer measurement of the IMU in the sensor body coordinate system, returned
as an *N*-by-3 matrix of real scalars in microtesla.
*N* is the number of samples in the current frame.

**Data Types:** `single` | `double`

## Parameters

#### Parameters

### **Reference frame** — Navigation reference frame `NED` (default) | `ENU`

Navigation reference frame, specified as `NED` (North-East-Down) or
`ENU` (East-North-Up).

**Note**

- If you choose the NED reference frame, specify the sensor inputs in the NED
  reference frame. Additionally, the sensor models the gravitational acceleration
  as [0 0 9.81] m/s2.
- If you choose the ENU reference frame, specify the sensor inputs in the ENU
  reference frame. Additionally, the sensor models the gravitational acceleration
  as [0 0 −9.81] m/s2.

### **Specify temperature from input port** — Specify temperature from input port off (default) | on

Select this check box to enable the input of temperature by using the
**Temperature** input port.

### **Temperature (oC)** — Operating temperature of IMU (oC) `25` (default) | real scalar

Operating temperature of the IMU in degrees Celsius, specified as a real
scalar.

When the block calculates temperature scale factors and environmental drift noises,
25 oC is used as the nominal temperature.

#### Dependencies

To enable this parameter, clear **Specify temperature from input
port**.

**Data Types:** `single` | `double`

### **Specify magnetic field from input port** — Specify magnetic field from input port off (default) | on

Select this check box to enable the input of magnetic field by using the
**Magnetic field** input port.

### **Magnetic field (NED)** — Magnetic field vector expressed in NED navigation frame (μT) `[27.5550, -2.4169, -16.0849]` (default) | 1-by-3 vector of scalar

Magnetic field vector expressed in the NED navigation frame, specified as a 1-by-3
vector of scalars.

The default magnetic field corresponds to the magnetic field at latitude zero,
longitude zero, and altitude zero.

#### Dependencies

To enable this parameter, set **Reference frame** to
`NED` and clear **Specify magnetic field from input
port**.

**Data Types:** `single` | `double`

### **MagneticField (ENU)** — Magnetic field vector expressed in ENU navigation frame (μT) `[-2.4169, 27.5550, 16.0849]` (default) | 1-by-3 vector of scalar

Magnetic field vector expressed in the ENU navigation frame, specified as a 1-by-3
vector of scalars.

The default magnetic field corresponds to the magnetic field at latitude zero,
longitude zero, and altitude zero.

#### Dependencies

To enable this parameter, set **Reference frame** to
`ENU` and clear **Specify magnetic field from input
port**.

**Data Types:** `single` | `double`

### **Seed** — Initial seed for randomization `67` (default) | nonnegative integer

Initial seed of a random number generator algorithm, specified as a nonnegative
integer.

**Data Types:** `single` | `double`

### **Simulate using** — Type of simulation to run `Interpreted Execution` (default) | `Code Generation`

- `Interpreted execution` — Simulate the model using the
  MATLAB® interpreter. This option shortens startup time. In
  `Interpreted execution` mode, you can debug the source
  code of the block.
- `Code generation` — Simulate the model using generated
  C code. The first time that you run a simulation, Simulink generates C code for the block. The C code is reused for subsequent
  simulations if the model does not change. This option requires additional startup
  time.

#### Accelerometer

### **Maximum readings (m/s2)** — Maximum sensor reading (m/s2) `inf` (default) | real positive scalar

Maximum sensor reading in m/s2, specified as a real
positive scalar.

**Data Types:** `single` | `double`

### **Resolution ((m/s2)/LSB)** — Resolution of sensor measurements ((m/s2)/LSB) `0` (default) | real nonnegative scalar

Resolution of sensor measurements in (m/s2)/LSB,
specified as a real nonnegative scalar.

**Data Types:** `single` | `double`

### **Constant offset bias (m/s2)** — Constant sensor offset bias (m/s2) `[0 0 0]` (default) | real scalar | real 3-element row vector

Constant sensor offset bias in m/s2, specified as a real
scalar or 3-element row vector. Any scalar input is converted into a real 3-element row
vector where each element has the input scalar value.

**Data Types:** `single` | `double`

### **Axis skew (%)** — Sensor axes skew (%) `diag([100 100 100])` (default) | scalar | 3-element row vector | 3-by-3 matrix

Sensor axes skew in percentage, specified as a scalar, a 3-element row vector, or a
3-by-3 matrix. The diagonal elements of the matrix account for the misalignment effects
for each axes. The off-diagonal elements account for the cross-axes misalignment
effects. The measured state
*v**measure* is obtained from
the true state *v**true* via
the misalignment matrix as:

vmeasure=1100M vtrue=1100[m11m12m13m21m22m23m31m32m33]vtrue

- If you specify the property as a scalar, then all the off-diagonal elements of
  the matrix take the value of the specified scalar and all the diagonal elements are
  100.
- If you specify the property as a vector [*a*
  *b*
  *c*], then *m*21 =
  *m*31 = *a*,
  *m*12 =
  *m*32 = *b*, and
  *m*13 =
  *m*23 = *c*. All the
  diagonal elements are 100.

**Data Types:** `single` | `double`

### **Velocity random walk (m/s2/√Hz)** — Velocity random walk (m/s2/√Hz) `[0 0 0]` (default) | real scalar | real 3-element row vector

Velocity random walk in (m/s2/√Hz), specified as a real
scalar or 3-element row vector. This property corresponds to the power spectral density
of sensor noise. Any scalar input is converted into a real 3-element row vector where
each element has the input scalar value.

**Data Types:** `single` | `double`

### **Bias Instability (m/s2)** — Instability of the bias offset (m/s2) `[0 0 0]` (default) | real scalar | real 3-element row vector

Instability of the bias offset in m/s2, specified as a
real scalar or 3-element row vector. Any scalar input is converted into a real 3-element
row vector where each element has the input scalar value.

**Data Types:** `single` | `double`

### **Bias instability filter numerator coefficients** — Bias instability filter numerator coefficients `fractalcoef.Numerator` (default) | real-valued row vector

Bias instability filter numerator coefficients, specified as a real-valued row
vector. To specify coefficients for fractal noise, use the `fractalcoef`
function.

**Data Types:** `single` | `double`

### **Bias instability filter denominator coefficients** — Bias instability filter denominator coefficients `fractalcoef.Denominator` (default) | real-valued row vector

Bias instability filter denominator coefficients, specified as a real-valued row
vector. To specify coefficients for fractal noise, use the `fractalcoef`
function.

**Data Types:** `single` | `double`

### **Acceleration random walk ((m/s2)(√Hz))** — Acceleration random walk ((m/s2)(√Hz)) `[0 0 0]` (default) | real scalar | real 3-element row vector

Acceleration random walk of sensor in (m/s2)(√Hz),
specified as a real scalar or 3-element row vector. Any scalar input is converted into a
real 3-element row vector where each element has the input scalar value.

**Data Types:** `single` | `double`

### **Noise Type** — Type of random noise `double-sided` (default) | `single-sided`

Select the type of random noise as:

- `double-sided` — Random noise coefficients have a
  scale factor of 2.
- `single-sided` — Random noise coefficients have a
  scale factor of 1.

**Data Types:** `single` | `double`

### **Bias from temperature ((m/s2)/℃)** — Sensor bias from temperature ((m/s2)/℃) `[0 0 0]` (default) | real scalar | real 3-element row vector

Sensor bias from temperature in (m/s2)/℃, specified as a
real scalar or 3-element row vector. Any scalar input is converted into a real 3-element
row vector where each element has the input scalar value.

**Data Types:** `single` | `double`

### **Temperature scale factor (%/℃)** — Scale factor error from temperature (%/℃) `[0 0 0]` (default) | real scalar in the range [0,100] | real 3-element row vector in the range [0,100]

Scale factor error from temperature in %/℃, specified as a real scalar or real
3-element row vector with values ranging from 0 to 100. Any scalar input is converted
into a real 3-element row vector where each element has the input scalar value.

**Data Types:** `single` | `double`

#### Gyroscope

### **Maximum readings (rad/s)** — Maximum sensor reading (rad/s) `inf` (default) | real positive scalar

Maximum sensor reading in rad/s, specified as a real positive scalar.

**Data Types:** `single` | `double`

### **Resolution ((rad/s)/LSB)** — Resolution of sensor measurements ((rad/s)/LSB) `0` (default) | real nonnegative scalar

Resolution of sensor measurements in (rad/s)/LSB, specified as a real nonnegative
scalar.

**Data Types:** `single` | `double`

### **Constant offset bias (rad/s)** — Constant sensor offset bias (rad/s) `[0 0 0]` (default) | real scalar | real 3-element row vector

Constant sensor offset bias in rad/s, specified as a real scalar or 3-element row
vector. Any scalar input is converted into a real 3-element row vector where each
element has the input scalar value.

**Data Types:** `single` | `double`

### **Axis skew (%)** — Sensor axes skew (%) `diag([100 100 100])` (default) | scalar | 3-element row vector | 3-by-3 matrix

Sensor axes skew in percentage, specified as a scalar, a 3-element row vector, or a
3-by-3 matrix. The diagonal elements of the matrix account for the misalignment effects
for each axes. The off-diagonal elements account for the cross-axes misalignment
effects. The measured state
*v**measure* is obtained from
the true state *v**true* via
the misalignment matrix as:

vmeasure=1100M vtrue=1100[m11m12m13m21m22m23m31m32m33]vtrue

- If you specify the property as a scalar, then all the off-diagonal elements of
  the matrix take the value of the specified scalar and all the diagonal elements are
  100.
- If you specify the property as a vector [*a*
  *b*
  *c*], then *m*21 =
  *m*31 = *a*,
  *m*12 =
  *m*32 = *b*, and
  *m*13 =
  *m*23 = *c*. All the
  diagonal elements are 100.

**Data Types:** `single` | `double`

### **Bias from acceleration ((rad/s)/(m/s2)** — Sensor bias from linear acceleration (rad/s)/(m/s2) `[0 0 0]` (default) | real scalar | real 3-element row vector

Sensor bias from linear acceleration in (rad/s)/(m/s2),
specified as a real scalar or 3-element row vector. Any scalar input is converted into a
real 3-element row vector where each element has the input scalar value.

**Data Types:** `single` | `double`

### **Angle random walk ((rad/s)/(√Hz))** — Angle random walk ((rad/s)/(√Hz)) `[0 0 0]` (default) | real scalar | real 3-element row vector

Angle random walk of sensor in (rad/s)/(√Hz), specified as a real scalar or
3-element row vector. Any scalar input is converted into a real 3-element row vector
where each element has the input scalar value.

**Data Types:** `single` | `double`

### **Bias Instability (rad/s)** — Instability of the bias offset (rad/s) `[0 0 0]` (default) | real scalar | real 3-element row vector

Instability of the bias offset in rad/s, specified as a real scalar or 3-element row
vector. Any scalar input is converted into a real 3-element row vector where each
element has the input scalar value.

**Data Types:** `single` | `double`

### **Bias instability filter numerator coefficients** — Bias instability filter numerator coefficients `fractalcoef.Numerator` (default) | real-valued row vector

Bias instability filter numerator coefficients, specified as a real-valued row
vector. To specify coefficients for fractal noise, use the `fractalcoef`
function.

**Data Types:** `single` | `double`

### **Bias instability filter denominator coefficients** — Bias instability filter denominator coefficients `fractalcoef.Denominator` (default) | real-valued row vector

Bias instability filter denominator coefficients, specified as a real-valued row
vector. To specify coefficients for fractal noise, use the `fractalcoef`
function.

**Data Types:** `single` | `double`

### **Noise Type** — Type of random noise `double-sided` (default) | `single-sided`

Select the type of random noise as:

- `double-sided` — Random noise coefficients have a
  scale factor of 2.
- `single-sided` — Random noise coefficients have a
  scale factor of 1.

**Data Types:** `single` | `double`

### **Rate random walk ((rad/s)(√Hz))** — Integrated white noise of sensor ((rad/s)(√Hz)) `[0 0 0]` (default) | real scalar | real 3-element row vector

Integrated white noise of sensor in (rad/s)(√Hz), specified as a real scalar or
3-element row vector. Any scalar input is converted into a real 3-element row vector
where each element has the input scalar value.

**Data Types:** `single` | `double`

### **Bias from temperature ((rad/s)/℃)** — Sensor bias from temperature ((rad/s)/℃) `[0 0 0]` (default) | real scalar | real 3-element row vector

Sensor bias from temperature in (rad/s)/℃, specified as a real scalar or 3-element
row vector. Any scalar input is converted into a real 3-element row vector where each
element has the input scalar value.

**Data Types:** `single` | `double`

### **Temperature scale factor (%/℃)** — Scale factor error from temperature (%/℃) `[0 0 0]` (default) | real scalar in the range [0,100] | real 3-element row vector in the range [0,100]

Scale factor error from temperature in %/℃, specified as a real scalar or real
3-element row vector with values ranging from 0 to 100. Any scalar input is converted
into a real 3-element row vector where each element has the input scalar value.

**Data Types:** `single` | `double`

#### Magnetometer

### **Maximum readings (μT)** — Maximum sensor reading (μT) `inf` (default) | real positive scalar

Maximum sensor reading in μT, specified as a real positive scalar.

**Data Types:** `single` | `double`

### **Resolution ((μT)/LSB)** — Resolution of sensor measurements ((μT)/LSB) `0` (default) | real nonnegative scalar

Resolution of sensor measurements in (μT)/LSB, specified as a real nonnegative
scalar.

**Data Types:** `single` | `double`

### **Constant offset bias (μT)** — Constant sensor offset bias (μT) `[0 0 0]` (default) | real scalar | real 3-element row vector

Constant sensor offset bias in μT, specified as a real scalar or 3-element row
vector. Any scalar input is converted into a real 3-element row vector where each
element has the input scalar value.

**Data Types:** `single` | `double`

### **Axis skew (%)** — Sensor axes skew (%) `diag([100 100 100])` (default) | scalar | 3-element row vector | 3-by-3 matrix

Sensor axes skew in percentage, specified as a scalar, a 3-element row vector, or a
3-by-3 matrix. The diagonal elements of the matrix account for the misalignment effects
for each axes. The off-diagonal elements account for the cross-axes misalignment
effects. The measured state
*v**measure* is obtained from
the true state *v**true* via
the misalignment matrix as:

vmeasure=1100M vtrue=1100[m11m12m13m21m22m23m31m32m33]vtrue

- If you specify the property as a scalar, then all the off-diagonal elements of
  the matrix take the value of the specified scalar and all the diagonal elements are
  100.
- If you specify the property as a vector [*a*
  *b*
  *c*], then *m*21 =
  *m*31 = *a*,
  *m*12 =
  *m*32 = *b*, and
  *m*13 =
  *m*23 = *c*. All the
  diagonal elements are 100.

### **White noise PSD (μT/√Hz)** — Power spectral density of sensor noise (μT/√Hz) `[0 0 0]` (default) | real scalar | real 3-element row vector

Power spectral density of sensor noise in μT/√Hz, specified as a real scalar or
3-element row vector. Any scalar input is converted into a real 3-element row vector
where each element has the input scalar value.

**Data Types:** `single` | `double`

### **Bias Instability (μT)** — Instability of the bias offset (μT) `[0 0 0]` (default) | real scalar | real 3-element row vector

Instability of the bias offset in μT, specified as a real scalar or 3-element row
vector. Any scalar input is converted into a real 3-element row vector where each
element has the input scalar value.

**Data Types:** `single` | `double`

### **Bias instability filter numerator coefficients** — Bias instability filter numerator coefficients `fractalcoef.Numerator` (default) | real-valued row vector

Bias instability filter numerator coefficients, specified as a real-valued row
vector. To specify coefficients for fractal noise, use the `fractalcoef`
function.

**Data Types:** `single` | `double`

### **Bias instability filter denominator coefficients** — Bias instability filter denominator coefficients `fractalcoef.Denominator` (default) | real-valued row vector

Bias instability filter denominator coefficients, specified as a real-valued row
vector. To specify coefficients for fractal noise, use the `fractalcoef`
function.

**Data Types:** `single` | `double`

### **Noise Type** — Type of random noise `double-sided` (default) | `single-sided`

Select the type of random noise as:

- `double-sided` — Random noise coefficients have a
  scale factor of 2.
- `single-sided` — Random noise coefficients have a
  scale factor of 1.

**Data Types:** `single` | `double`

### **Random walk ((μT)\*√Hz)** — Integrated white noise of sensor ((μT)\*√Hz) `[0 0 0]` (default) | real scalar | real 3-element row vector

Integrated white noise of sensor in (μT)\*√Hz, specified as a real scalar or
3-element row vector. Any scalar input is converted into a real 3-element row vector
where each element has the input scalar value.

**Data Types:** `single` | `double`

### **Bias from temperature (μT/℃)** — Sensor bias from temperature (μT/℃) `[0 0 0]` (default) | real scalar | real 3-element row vector

Sensor bias from temperature in μT/℃, specified as a real scalar or 3-element row
vector. Any scalar input is converted into a real 3-element row vector where each
element has the input scalar value.

**Data Types:** `single` | `double`

### **Temperature scale factor (%/℃)** — Scale factor error from temperature (%/℃) `[0 0 0]` (default) | real scalar in the range [0,100] | real 3-element row vector in the range [0,100]

Scale factor error from temperature in %/℃, specified as a real scalar or real
3-element row vector with values ranging from 0 to 100. Any scalar input is converted
into a real 3-element row vector where each element has the input scalar value.

**Data Types:** `single` | `double`

## Libraries

Sensor Fusion and Tracking Toolbox / Multisensor Positioning / Sensor Models Navigation Toolbox / Multisensor Positioning / Sensor Models

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2023b: Specify bias instability noise coefficients and noise type for accelerometer, gyroscope, and magnetometer

You can use these new parameters in the **Accelerometer, Gyroscope, or
Magnetometer** tab to specify the coefficients of the transfer function used to
generate the bias instability noise and specify the scale factor of the noise
coefficients.

- **Bias instability filter numerator coefficients**
- **Bias instability filter denominator
  coefficients**
- **Noise type**

## Description

IMU simulation model

The IMU
Simulink® block models receiving data from an inertial measurement unit (IMU) composed of
accelerometer, gyroscope, and magnetometer sensors. You can specify the reference frame of the
block inputs as the `NED` (North-East-Down) or `ENU`
(East-North-Up) frame by using the **Reference Frame** parameter.
