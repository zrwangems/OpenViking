---
type: simulink-block
title: 'ICM20948 IMU Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'icm20948imusensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/icm20948imusensor.html'
language: en
---

# ICM20948 IMU Sensor

## Ports

### Output

### **Acceleration** — Linear acceleration measured by sensor row vector

The **Acceleration** port outputs acceleration in
m/s2 along the *x-*,
*y-*, and *z-* axes of the sensor as a
*n*-by-3 vector.

#### Dependencies

To enable this port, select the **Acceleration
(m/s2)** parameter.

**Data Types:** `single (default)` | `double`

### **Angular Rate** — Angular velocity measured by sensor row vector

The **Angular Rate** port outputs angular velocity in
radians per second (rad/s) along the *x-*,
*y-*, and *z-* axes of the sensor as a
*n*-by-3 vector.

#### Dependencies

To enable this port, select the **Angular Velocity
(rad/s)** parameter.

**Data Types:** `single (default)` | `double`

### **Magnetic Field** — Magnetic field strength measured by ICM20948 IMU sensor row vector

The **Magnetic Field** port outputs magnetic field strength
in µT along the *x-*, *y-*, and
*z-* axes of the sensor as a *n*-by-3
vector..

#### Dependencies

To enable this port, select the **Magnetic Field (µT)**
parameter.

**Data Types:** `single (default)` | `double`

### **Temperature** — Temperature measured by sensor scalar

Temperature (in ℃) measured by the ICM20948 IMU sensor connected to an STM32
processor.

#### Dependencies

To enable this port, select the **Temperature (℃)**
parameter.

**Data Types:** `single` | `double`

### **Status** — Status of acceleration, angular rate, magnetometer, and temperature measurements row vector

Status of acceleration, angular rate, magnetometer, and temperature
measurements along the three axes, returned as a 1-by-2 vector of
`uint8` values. First element in the vector represents the
status of acceleration, angular rate, and temperature measurements and the
second element represents the status of magnetometer measurements. The block
outputs status as `0`s or `1`s.
`0` indicates that the data read is new and
`1` indicates that the data read is not new.

#### Dependencies

To enable this port, select the **Status**
parameter.

**Note**

The **Status** parameter is disabled if you select
the **Generate data ready interrupt** parameter.

**Data Types:** `uint8`

## Parameters

### **I2C module** — I2C communication module `I2C1` (default) | scalar

Specify the I2C module on the STM32 processor to communicate with sensor
peripherals.

### **I2C address** — I2C address of sensor `0x69` (default) | `0x68`

The I2C address of the ICM20948 IMU sensor from which the block reads the data.
The ICM20948 sensor can have two I2C addresses depending on the logic level on pin
AD0 of the sensor.

| Pin Name | Pin State | I2C Address |
| --- | --- | --- |
| AD0 | Low | 0x68 |
| High | 0x69 |

### **Generate data ready interrupt** — Generate interrupt when data is ready `off` (default) | `on`

Select this parameter to generate an interrupt on pin INT1 of the sensor when
data is ready. Using this option, you can trigger other subsystems to perform any
action.

### **Interrupt type** — Type of interrupt `Active high` (default) | `Active low`

Select the logic level for the INT1 pin as `Active
high` or `Active low`.

#### Dependencies

To enable this parameter, select the **Generate data ready
interrupt** parameter.

### **Acceleration (m/s2)** — Enable port to output acceleration `on` (default) | `off`

Select this parameter to enable **Acceleration** output
port.

### **Angular rate (rad/s)** — Enable port to output angular rate `on` (default) | `off`

Select this parameter to enable **Angular Rate** output
port.

### **Magnetic Field (µT)** — Enable port to output magnetic field `on` (default) | `off`

Select this parameter to enable **Magnetic Field** output
port.

### **Temperature (℃)** — Enable port to output temperature `on` (default) | `off`

Select this parameter to enable **Temperature** output
port.

### **Status** — Enable port to output acceleration, angular rate, magnetometer measurement, and temperature status `off` (default) | `on`

Select this parameter to set **Status** as one of the output
ports. This parameter is disabled if you select the **Generate data ready
interrupt** parameter.

### **Output data type** — Data type of output `double` (default) | `single`

Specify the data type for the acceleration, angular rate, magnetic field, and
temperature outputs.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often the block reads the data from the ICM20948 IMU sensor. When
you set this parameter to -1, Simulink determines the best sample time for the
block based on the block's context within the model. The output sample time is the
product of the values you specify in `Sample time`
parameter.

#### Accelerometer Settings

### **Full scale range** — Range for measuring acceleration `±2g` (default) | `±4g` | `±8g` | `±16g`

Select the range of for measuring acceleration.

### **Output data rate** — Rate at which sensor outputs accelerometer data `1125Hz` (default)

Specify the output data rate as a scalar in the range `0.3` to
`1125` Hz. Accelerometer data output rate in Hz is determined
by the following calculation.

`1125/(1+ACCEL_SMPLRT_DIV)Hz`, where
`ACCEL_SMPLRT_DIV` is `0,1,2,...4095`.

Depending on the output data rate specified on the block mask,
`ACCEL_SMPLRT_DIV` is set on the sensor.

### **Bandwidth** — Bandwidth of accelerometer `23.9 Hz` (default) | `5.7 Hz` | `11.5 Hz` | `50.4 Hz` | `111.4 Hz` | `246 Hz` | `473 Hz`

Specify the 3 dB bandwidth of the accelerometer lowpass filter.

#### Gyroscope Settings

### **Full scale range** — Maximum angular velocity measured by gyroscope `±250 dps` (default) | `±500 dps` | `±1000 dps` | `±2000 dps`

Specify the maximum angular velocity that the gyroscope can measure per
second.

### **Output data rate** — Rate at which sensor outputs gyroscope data `1125Hz` (default)

Specify the output data rate as a scalar in the range `4.4` Hz
to `1125` Hz.

Gyroscope data output rate in Hz is determined by the following
calculation.

`1125/(1+GYRO_SMPLRT_DIV)Hz`, where
`GYRO_SMPLRT_DIV` is `0,1,2,...255`.

Depending on the output data rate specified on the block mask,
`GYRO_SMPLRT_DIV` will be set on the sensor.

### **Bandwidth** — Bandwidth of gyroscope `23.9 Hz` (default) | `5.7 Hz` | `11.6 Hz` | `51.2 Hz` | `119.5 Hz` | `151.8 Hz` | `196.6 Hz` | `361.4 Hz`

Specify the 3 dB bandwidth of the gyroscope lowpass filter.

#### Magnetometer Settings

### **Output data rate** — Rate at which sensor outputs magnetometer data `100 Hz` (default) | `10 Hz` | `20 Hz` | `50 Hz`

Select the output data rate at which magnetometer data is sampled.

#### Temperature sensor Settings

### **Bandwidth** — Noise bandwidth of temperature `34.1 Hz` (default) | `8.8 Hz` | `17.3 Hz` | `65.9 Hz` | `123.5 Hz` | `217.9 Hz` | `7932.0 Hz`

Specify the noise bandwidth (NBW) of the temperature lowpass filter in
Hz.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Measure linear acceleration, angular velocity, magnetic field, and temperature from ICM20948 IMU sensor

The ICM20948 IMU Sensor block outputs the values of linear acceleration,
angular velocity, and magnetic field strength along *x-*,
*y-* and *z-* axes as measured by the ICM20948 IMU
sensor connected to an STM32 processor. The block also outputs the temperature read by the
ICM20948 IMU sensor.
