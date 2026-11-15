---
type: simulink-block
title: 'LSM6DSO IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'lsm6dsoimusensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/lsm6dsoimusensor.html'
language: en
---

# LSM6DSO IMU Sensor

## Ports

### Output

You can select the active sensor(s) to measure angular velocity, acceleration,
temperature, or a combination of these measurements.

### **Acceleration** — Acceleration along each axis as measured by accelerometer vector

The block outputs acceleration as a `1`-by-`3`
vector. Each value represents the measurement of acceleration in
`m/s^2` along the X, Y, and Z axes.

#### Dependencies

This output port appears only if you select the **Acceleration
(m/s2)** parameter.

**Data Types:** `double`

### **Angular Velocity** — Angular velocity along each axis as measured by gyroscope vector

The block outputs angular velocity as a
`1`-by-`3` vector. Each value represents the
measurement of angular velocity in radians per second (rad/s) along the X, Y, and Z
axes.

#### Dependencies

This output port appears only if you select the **Angular Velocity
(rad/s)** parameter.

**Data Types:** `double`

### **Temperature** — Temperature measured by LSM6DSO sensor scalar

Temperature (in ℃) measured by LSM6DSO sensor connected to Raspberry Pi board.

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `double`

### **Status** — Status of acceleration, angular velocity and temperature measurements `-1` | `0` | `1`

Status of acceleration, angular velocity and temperature measurements, specified
as a 1-by-3 vector. `0` indicates that the data read is new,
`1` indicates that the data read is not new, and
`-1` indicates that the corresponding output is not
selected.

#### Dependencies

This output port appears only if you select the **Status**
parameter.

**Data Types:** `int8`

## Parameters

### Main

### **I2C module** — Module for communication `1` (default)

Specify the module on the board that you are using for I2C communication.

### **I2C address** — Peripheral addresses to communicate with sensors `0x6A` (default) | `0x6B`

The peripheral addresses to communicate with the accelerometer and gyroscope
peripherals on the LSM6DSO sensor are decided by the state of the SDO/SA0 pin on the
hardware board. This table provides the peripheral addresses corresponding to the pin
and their state.

| Pin Name | Pin State | Peripheral Address |
| --- | --- | --- |
| SDO/SA0 | 0 | 0x6A |
| 1 | 0x6B |

### **Acceleration (m/s2)** — Set output port for reading acceleration `on` (default) | `off`

Select this parameter to set **Acceleration** as one of the
output ports.

### **Angular Velocity (rad/s)** — Set output port for reading angular velocity `on` (default) | `off`

Select this parameter to set **Angular Velocity** as one of the
output ports.

### **Temperature (℃)** — Set output port for reading temperature `on` (default) | `off`

Select this parameter to set **Temperature** as one of the output
ports.

### **Status** — Set output port for obtaining status of selected outputs `off` (default) | `on`

Select this parameter to set **Status** as one of the output
ports.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the LSM6DSO sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block based on
the block context within the model.

### Advanced

#### Accelerometer

### **Full scale range** — Full scale for measuring linear acceleration `±2g` (default) | `±4g` | `±8g` | `±16g`

Select the full scale for measuring linear acceleration (the range of acceleration
that the sensor needs to measure).

### **Output data rate** — Rate at which accelerometer data is sampled `12.5 Hz` (default) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

Select the output data rate at which accelerometer data is sampled, which also
determines the bandwidth.

### **Select composite filter** — Composite filter used in the filtering chain `No filter` (default) | `High pass filter` | `Low pass filter`

Select the type of composite filter used in the filtering chain for reading
accelerometer values.

### **High pass filter bandwidth** — Bandwidth of high pass filter `ODR/4` (default) | `ODR/10` | `ODR/20` | `ODR/45` | `ODR/100` | `ODR/200` | `ODR/400` | `ODR/800`

Select the required bandwidth of the high pass filter in the composite filter used
in the filtering chain.

#### Dependencies

This parameter appears only if you select `High pass
filter` in the **Select composite filter**
parameter.

### **Low pass filter bandwidth** — Bandwidth of low pass filter `ODR/4` (default) | `ODR/10` | `ODR/20` | `ODR/45` | `ODR/100` | `ODR/200` | `ODR/400` | `ODR/800`

Select the required bandwidth of the low pass filter in the composite filter used
in the filtering chain.

#### Dependencies

This parameter appears only if you select `Low pass
filter` in the **Select composite filter**
parameter.

#### Gyroscope

### **Full scale range** — Full scale for measuring angular velocity `125 dps` (default) | `250 dps` | `500 dps` | `1000 dps` | `2000 dps`

Select the full scale for measuring angular velocity (the range of angular
velocity that the sensor needs to measure).

### **Output data rate** — Rate at which gyroscope data is sampled `12.5 Hz` (default) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

Select the output data rate at which gyroscope data is sampled, which also
determines the bandwidth.

### **Enable high pass filter** — Enable high pass filter for gyroscope data `off` (default) | `on`

Enable the high pass filter for reading gyroscope values.

### **High pass filter bandwidth** — Bandwidth of high pass filter `0.016 Hz` (default) | `0.065 Hz` | `0.260 Hz` | `1.04 Hz`

Select the required bandwidth of the high pass filter for reading gyroscope
values.

#### Dependencies

This parameter appears only if you select the **Enable high pass
filter** parameter.

### **Enable low pass filter** — Enable low pass filter for gyroscope data `off` (default) | `on`

Enable the low pass filter for reading gyroscope values.

### **Low pass filter bandwidth mode** — Bandwidth mode of low pass filter `0` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7`

Select the required bandwidth mode of the low pass filter for reading gyroscope
values.

For Gyroscope ODR > 1666 Hz, only these values are applicable for Low pass filter
bandwidth mode: `0`, `1`, `2`,
`3`.

#### Dependencies

This parameter appears only if you select the **Enable low pass
filter** parameter.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sensors / IMU Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Measure linear acceleration, angular rate, and temperature from LSM6DSO sensor

The LSM6DSO IMU Sensor block measures linear acceleration and angular rate
along the X, Y, and Z axis using the LSM6DSO Inertial Measurement Unit (IMU) sensor interfaced
with the Raspberry Pi® hardware. This 6-Degree of Freedom (DoF) IMU sensor comprises of an
accelerometer and gyroscope used to measure linear acceleration and angular rate,
respectively. The block also measures the temperature from the embedded temperature sensor in
LSM6DSO Sensor.

You can also use the composite filter option in the block for the accelerometer values,
and use the high pass and low pass filter options for gyroscope values.
