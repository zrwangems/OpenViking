---
type: simulink-block
title: 'LSM6DSO IMU Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'lsm6dsoimusensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lsm6dsoimusensor.html'
language: en
---

# LSM6DSO IMU Sensor

## Ports

### Output

You can select the active sensor(s) to measure angular velocity, acceleration,
temperature, or a combination of these measurements.

### **Acceleration** — Acceleration along each axis as measured by accelerometer vector

The block outputs acceleration as a *n*-by-3 vector,
where *n* is the value for samples per frame. Each value
represents the measurement of acceleration in `m/s^2` along
the *X-*, *Y-*, and
*Z-* axes.

#### Dependencies

To enable this port, select the **Acceleration
(m/s2)** parameter.

**Data Types:** `double`

### **Angular Velocity** — Angular velocity along each axis as measured by gyroscope vector

The block outputs angular velocity as a *n*-by-3 vector,
where *n* is the value for samples per frame. Each value
represents the measurement of angular velocity in radians per second (rad/s)
along the *X-*, *Y-*, and
*Z-* axes.

#### Dependencies

To enable this port, select the **Angular Velocity
(rad/s)** parameter.

**Data Types:** `double`

### **Temperature** — Temperature measured by LSM6DSO sensor scalar

Temperature (in ℃) measured by LSM6DSO sensor connected to an STM32
processor.

#### Dependencies

To enable this port, select the **Temperature (℃)**
parameter.

**Data Types:** `double`

### **Status** — Status of acceleration, angular velocity, and temperature measurements `-1` | `0` | `1`

Status of acceleration, angular velocity, and temperature measurements,
returned as a 1-by-3 vector.

- `0` - Data read is new
- `1` - Data read is not new
- `-1` - Corresponding output is not selected

#### Dependencies

To enable this port, select the **Status**
parameter.

**Data Types:** `int8`

## Parameters

### Main

### **I2C module** — I2C communication module `I2C1` (default) | scalar

Specify the I2C module on the STM32 Processor to communicate with sensor
peripherals.

### **I2C address** — Peripheral addresses to communicate with sensors `0x6A` (default) | `0x6B`

The peripheral addresses to communicate with the accelerometer and gyroscope
peripherals on the LSM6DSO sensor are decided by the state of the SDO/SA0 pin
on the STM32 processor. This table provides the peripheral addresses
corresponding to the pin and its state.

| Pin Name | Pin State | Peripheral Address |
| --- | --- | --- |
| SDO/SA0 | 0 | 0x6A |
| 1 | 0x6B |

### **Acceleration (m/s2)** — Enable port to output acceleration `on` (default) | `off`

Select this parameter to enable **Acceleration** output
port.

### **Angular Velocity (rad/s)** — Enable port to output angular velocity `on` (default) | `off`

Select this parameter to enable **Angular Velocity** output
port.

### **Temperature (℃)** — Enable port to output temperature `on` (default) | `off`

Select this parameter to enable **Temperature** output
port.

### **Status** — Enable port to output status of selected outputs `on` (default) | `off`

Select this parameter to enable **Status** output
port.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often the block reads data from the LSM6DSO sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block
based on the block's context within the model. The output sample time is the
product of `Sample time` that you specify.

### Advanced

#### Accelerometer

### **Full scale range** — Range for measuring linear acceleration `±2g` (default) | `±4g` | `±8g` | `±16g`

Select the range for measuring linear acceleration.

### **Output data rate** — Rate at which sensor outputs accelerometer data `12.5 Hz` (default) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

Select the rate at which the sensor samples and outputs accelerometer data.
This rate also determines the bandwidth of the sensor.

### **Select composite filter** — Composite filter to use in the filtering chain `No filter` (default) | `High pass filter` | `Low pass filter`

Select the type of composite filter to use in the filtering chain for
reading accelerometer values.

### **High pass filter bandwidth** — Bandwidth of highpass filter `ODR/4` (default) | `ODR/10` | `ODR/20` | `ODR/45` | `ODR/100` | `ODR/200` | `ODR/400` | `ODR/800`

Select the bandwidth of the highpass filter in the composite filter used in
the filtering chain.

#### Dependencies

To enable this parameter, select `High pass
filter` in the **Select composite filter**
parameter.

### **Low pass filter bandwidth** — Bandwidth of lowpass filter `ODR/4` (default) | `ODR/10` | `ODR/20` | `ODR/45` | `ODR/100` | `ODR/200` | `ODR/400` | `ODR/800`

Select the required bandwidth of the lowpass filter in the composite filter
used in the filtering chain.

#### Dependencies

To enable this parameter, select `Low pass
filter` in the **Select composite filter**
parameter.

#### Gyroscope

### **Full scale range** — Range for for measuring angular velocity `125 dps` (default) | `250 dps` | `500 dps` | `1000 dps` | `2000 dps`

Select the range for measuring angular velocity (the range of angular
velocity that the sensor needs to measure).

### **Output data rate** — Rate at which sensor outputs gyroscope data `12.5 Hz` (default) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

Select the rate at which the sensor samples and outputs gyroscope data. This
rate also determines the bandwidth of the sensor.

### **Enable high pass filter** — Enable highpass filter for gyroscope data `off` (default) | `on`

Enable the highpass filter for reading gyroscope values.

### **High pass filter bandwidth** — Bandwidth of highpass filter `0.016 Hz` (default) | `0.065 Hz` | `0.260 Hz` | `1.04 Hz`

Select the required bandwidth of the highpass filter for reading gyroscope
values.

#### Dependencies

To enable this parameter, select the **Enable high pass
filter** parameter.

### **Enable low pass filter** — Enable lowpass filter for gyroscope data `off` (default) | `on`

Enable the lowpass filter for reading gyroscope values.

### **Low pass filter bandwidth mode** — Bandwidth mode of low pass filter `0` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7`

Select the required bandwidth mode of the low pass filter for reading
gyroscope values.

For Gyroscope ODR > 1666 Hz, only these values are applicable for Low
pass filter bandwidth mode: `0`, `1`,
`2`, `3`.

#### Dependencies

To enable this parameter, select the **Enable low pass
filter** parameter.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Measure linear acceleration, angular rate, and temperature from LSM6DSO sensor

The LSM6DSO IMU Sensor block measures linear acceleration and angular
rate along the *X-*, *Y-*, and
*Z-* axis using the LSM6DSO inertial measurement unit (IMU) sensor
interfaced with an STM32 processor. This six degree of freedom (DoF) and IMU sensor
comprises of an accelerometer and gyroscope that you can use to measure linear acceleration
and angular rate, respectively. The block also measures the temperature from the embedded
temperature sensor in the LSM6DSO ssensor.

You can also use the composite filter option in the block for the accelerometer values,
and use the highpass and lowpass filter options for the gyroscope values.
