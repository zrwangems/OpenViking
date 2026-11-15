---
type: simulink-block
title: 'ICM20948 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'icm20948imusensor'
documentation_source_path: 'supportpkg/arduino_ref/icm20948imusensor.html'
language: en
---

# ICM20948 IMU Sensor

## Ports

### Output

### **Acceleration** — Linear acceleration measured by ICM20948 IMU sensor row vector

The **Acceleration** port outputs acceleration in
m/s2 along the x-, y-, and z- axes of the sensor as a
`n`-by-3 vector, where `n` is the
value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the **Acceleration
(m/s2)** parameter.

**Data Types:** `single (default)` | `double`

### **Angular Rate** — Angular velocity along each axis as measured by gyroscope row vector

The **Angular Rate** port outputs angular velocity in radians per
second (rad/s) along the x-, y-, and z- axes of the sensor as a
`n`-by-3 vector, where `n` is the
value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the **Angular Velocity
(rad/s)** parameter.

**Data Types:** `single (default)` | `double`

### **Magnetic Field** — Magnetic field strength measured by ICM20948 IMU sensor row vector

The **Magnetic Field** port outputs Magnetic field strength in µT
along the x-, y-, and z- axes of the sensor as a `n`-by-3
vector, where `n` is the value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the **Magnetic Field
(µT)** parameter.

**Data Types:** `single (default)` | `double`

### **Temperature** — Temperature measured by ICM20948 IMU sensor scalar

Temperature (in ℃) measured by ICM20948 IMU sensor connected to Arduino
board.

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `single` | `double`

### **Status** — Status of acceleration value, angular rate, magnetometer measurement, and temperature row vector

Status of acceleration value, angular rate, magnetometer measurement, and
temperature along the three axes, specified as a [1X2] vector of uint8 values. First
element represents status of acceleration, angular rate, and temperature measurements
and second element represents status of magnetometer measurements. Status indicates if
the data read is the new value or not. `0` indicates that the data
read is new and `1` indicates that the data read is not new.

#### Dependencies

This output port appears only if you select the **Status**
parameter.

**Note**

**Status** parameter will not be available if you select
**Generate data ready interrupt** parameter.

**Data Types:** `uint8`

### **Timestamp** — Timestamp at which data is read matrix | (`n`)-by-1

Timestamp (in seconds) at which data is read from the sensor, returned as
`n`-by-1 matrix, where `n` is the
value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the **Timestamp**
parameter.

The data type of Timestamp output depends on the value that you selected for the
**Output data type** parameter.

## Parameters

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino® hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **I2C address** — I2C address of ICM20948 IMU sensor `0x69` (default) | `0x68`

The I2C address of the ICM20948 IMU sensor from which the block reads the values.
The ICM20948 sensor can have two I2C addresses depending on the logic level on pin AD0
of the sensor.

| Pin Name | Pin State | I2C Address |
| --- | --- | --- |
| AD0 | Low | 0x68 |
| High | 0x69 |

### **Generate data ready interrupt** — Generate interrupt when data is ready `off` (default) | `on`

If this option is selected, an interrupt is generated on pin INT1 of the sensor when
data is ready. Using this option, you can trigger other subsystems to perform any
action. For more information, see Estimate Orientation Using AHRS Filter and IMU Data in Simulink

### **Interrupt type** — Generate interrupt when data is ready `Active high` (default) | `Active low`

Select the logic level for INT1 pin as `Active high` or
`Active low`.

#### Dependencies

This parameter appears only if you select the **Generate data ready
interrupt** parameter.

### **Acceleration (m/s2)** — Set output port for reading acceleration `on` (default) | `off`

Select this parameter to set **Acceleration** as one of the output
ports.

### **Angular rate (rad/s)** — Set output port for reading angular rate `on` (default) | `off`

Select this parameter to set **Angular Rate** as one of the output
ports.

### **Magnetic Field (µT)** — Set output port for reading magnetic field `on` (default) | `off`

Select this parameter to set **Magnetic Field** as one of the
output ports.

### **Temperature (℃)** — Set output port for reading temperature `on` (default) | `off`

Select this parameter to set **Temperature** as one of the output
ports.

### **Status** — Set output port for obtaining acceleration, angular rate, magnetometer measurement, and temperature status `off` (default) | `on`

Select this parameter to set **Status** as one of the output ports.
This parameter will not be available if **Generate data ready
interrupt** parameter is selected.

### **Timestamp** — Set output port for obtaining timestamp `off` (default) | `on`

Select this parameter to set **Timestamp** as one of the output
ports.

### **Output data type** — Type of output data `double` (default) | `single`

Specify the datatype for acceleration, angular rate, magnetic field, and temperature
outputs.

### **Samples per frame** — Number of samples that the block outputs `1` (default) | positive integer

Specify the number of samples that the block outputs. The value that you specify
here is also used to compute the output sample time:

Output sample time = `Samples per frame` \*
`Sample time`

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the ICM20948 IMU sensor. When you
set this parameter to -1, Simulink determines the best sample time for the block based
on the block context within the model. The output sample time is the product of
`Samples per frame` and `Sample
time` that you specify.

#### Accelerometer Settings

### **Full scale range** — Range of acceleration that can be measured by accelerometer `±2g` (default) | `±4g` | `±8g` | `±16g`

Select the range of acceleration that the accelerometer can measure.

### **Output data rate** — Rate at which accelerometer data is sampled `1125Hz` (default)

Enter the output data rate between `0.3` Hz to
`1125` Hz, at which accelerometer data is sampled.

Accelerometer data output rate in Hz is determined by the following
calculation.

`1125/(1+ACCEL_SMPLRT_DIV)Hz`, where
`ACCEL_SMPLRT_DIV` is `0,1,2,...4095`.

Depending on the output data rate specified on the block mask,
`ACCEL_SMPLRT_DIV` will be set on the sensor.

### **Bandwidth** — Bandwidth of accelerometer `23.9 Hz` (default) | `5.7 Hz` | `11.5 Hz` | `50.4 Hz` | `111.4 Hz` | `246 Hz` | `473 Hz`

Specify the 3 dB bandwidth of accelerometer low pass filter.

#### Gyroscope Settings

### **Full scale range** — Maximum angular velocity that can be measured by gyroscope `±250 dps` (default) | `±500 dps` | `±1000 dps` | `±2000 dps`

Specify the maximum angular velocity that the gyroscope can measure per
second.

### **Output data rate** — Rate at which gyroscope data is sampled `1125Hz` (default)

Enter the output data rate between `4.4` Hz to
`1125` Hz, at which gyroscope data is sampled.

Gyroscope data output rate in Hz is determined by the following calculation.

`1125/(1+GYRO_SMPLRT_DIV)Hz`, where
`GYRO_SMPLRT_DIV` is `0,1,2,...255`.

Depending on the output data rate specified on the block mask,
`GYRO_SMPLRT_DIV` will be set on the sensor.

### **Bandwidth** — Bandwidth of gyroscope `23.9 Hz` (default) | `5.7 Hz` | `11.6 Hz` | `51.2 Hz` | `119.5 Hz` | `151.8 Hz` | `196.6 Hz` | `361.4 Hz`

Specify the 3 dB bandwidth of gyroscope low pass filter.

#### Magnetometer Settings

### **Output data rate** — Rate at which magnetometer data is sampled `100 Hz` (default) | `10 Hz` | `20 Hz` | `50 Hz`

Select the output data rate at which magnetometer data is sampled.

#### Temperature sensor Settings

### **Bandwidth** — Noise bandwidth of temperature `34.1 Hz` (default) | `8.8 Hz` | `17.3 Hz` | `65.9 Hz` | `123.5 Hz` | `217.9 Hz` | `7932.0 Hz`

Specify the noise bandwidth (NBW) of temperature low pass filter in Hz.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Measure linear acceleration, angular velocity, magnetic field, and temperature from ICM20948 IMU sensor

The ICM20948 IMU Sensor block outputs the values of linear acceleration,
angular velocity, and magnetic field strength along x-, y- and z- axes as measured by the
ICM20948 IMU sensor connected to Arduino board. The block also outputs the temperature as read
by the ICM20948 IMU sensor.
