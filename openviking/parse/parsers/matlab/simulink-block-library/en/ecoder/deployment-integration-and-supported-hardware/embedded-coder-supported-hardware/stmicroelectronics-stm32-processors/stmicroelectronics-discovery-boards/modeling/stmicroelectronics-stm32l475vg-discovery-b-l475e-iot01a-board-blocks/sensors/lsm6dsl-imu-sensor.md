---
type: simulink-block
title: 'LSM6DSL IMU Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32L475VG-Discovery (B-L475E-IOT01A) Board Blocks / Sensors'
documentation_page: 'lsm6dslimusensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lsm6dslimusensor.html'
language: en
---

# LSM6DSL IMU Sensor

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

### **Temperature** — Temperature measured by LSM6DSL sensor scalar

Temperature (in ℃) measured by LSM6DSL sensor connected to
Nucleo/STM32L475-Discovery board.

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

### **Use onboard sensors** — Enable to use onboard sensors `on` (default) | `off`

Select this parameter to use onboard sensors.

**Note**

This parameters is available only for STM32L475VG-Discovery (B-L475E-IOT01A)
board.

### **I2C module** — Specify I2C module `2` (default) | `positive integer`

Specify the I2C module on the board. The I2C bus frequency, serial clock (SCL) pin
and serial data (SDA) pin are taken according to the corresponding I2C module entry in
the configuration parameters.

#### Dependencies

To enable this parameter, deselect the **Use onboard sensors**
parameter.

### **I2C address** — Peripheral addresses to communicate with sensor peripherals `0x6A` (default) | `0x6B`

The Peripheral addresses to communicate with the accelerometer and gyroscope
peripherals on the LSM6DSL sensor are decided by the state of the SDO/SA0 pin on the
hardware board. This table provides the Peripheral addresses corresponding to the pin
and their state.

| Pin Name | Pin State | Peripheral Address |
| --- | --- | --- |
| SDO/SA0 | 0 | 0x6A |
| 1 | 0x6B |

#### Dependencies

To enable this parameter, deselect the **Use onboard sensors**
parameter.

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

Specify how often this block reads the data from the LSM6DSL sensor. When you set
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

### **Digital low pass filter bandwidth** — Bandwidth of low-pass digital filter `ODR/2` (default) | `ODR/4`

Select the required bandwidth of the low-pass digital filter.

### **Select composite filter** — Composite filter used in the filtering chain `No filter` (default) | `High pass filter` | `Low pass filter`

Select the type of composite filter used in the filtering chain for reading
accelerometer values.

### **High pass filter bandwidth** — Bandwidth of high pass filter `ODR/100` (default) | `ODR/9` | `ODR/400`

Select the required bandwidth of the high pass filter in the composite filter used
in the filtering chain.

#### Dependencies

This parameter appears only if you select `High pass
filter` in the **Select composite filter**
parameter.

### **Low pass filter bandwidth** — Bandwidth of low pass filter `ODR/50` (default) | `ODR/100` | `ODR/9` | `ODR/400`

Select the required bandwidth of the low pass filter in the composite filter used
in the filtering chain.

#### Dependencies

This parameter appears only if you select `Low pass
filter` in the **Select composite filter**
parameter.

#### Gyroscope

### **Full scale range** — Full scale for measuring angular velocity `250 dps` (default) | `125 dps` | `500 dps` | `1000 dps` | `2000 dps`

Select the full scale for measuring angular velocity (the range of angular
velocity that the sensor needs to measure).

### **Output data rate** — Rate at which gyroscope data is sampled `12.5 Hz` (default) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

Select the output data rate at which gyroscope data is sampled, which also
determines the bandwidth.

### **Enable high pass filter** — Enable high pass filter for gyroscope data `off` (default) | `on` |

Enable the high pass filter for reading gyroscope values.

### **High pass filter bandwidth** — Bandwidth of high pass filter `0.016 Hz` (default) | `0.065 Hz` | `0.260 Hz` | `1.04 Hz`

Select the required bandwidth of the high pass filter for reading gyroscope
values.

#### Dependencies

This parameter appears only if you select the **Enable high pass
filter** parameter.

### **Enable low pass filter** — Enable low pass filter for gyroscope data `off` (default) | `on` |

Enable the low pass filter for reading gyroscope values.

### **Low pass filter bandwidth mode** — Bandwidth mode of low pass filter `0` (default) | `1` | `2` | `3`

Select the required bandwidth mode of the low pass filter for reading gyroscope
values.

#### Dependencies

This parameter appears only if you select the **Enable low pass
filter** parameter.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Measure linear acceleration, angular rate, and temperature from LSM6DSL sensor

The LSM6DSL IMU Sensor block measures linear acceleration and angular rate
along the X, Y, and Z axis using the LSM6DSL Inertial Measurement Unit (IMU) sensor interfaced
with the Nucleo/STM32L475-Discovery board. This 6-Degree of Freedom (DoF) IMU sensor comprises
of an accelerometer and gyroscope used to measure linear acceleration and angular rate,
respectively. The block also measures the temperature from the embedded temperature sensor in
LSM6DSL Sensor.

You can also use the composite filter option in the block for the accelerometer values,
and use the high pass and low pass filter options for gyroscope values.
