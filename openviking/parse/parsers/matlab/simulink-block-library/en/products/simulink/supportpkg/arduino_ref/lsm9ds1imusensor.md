---
type: simulink-block
title: 'LSM9DS1 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'lsm9ds1imusensor'
documentation_source_path: 'supportpkg/arduino_ref/lsm9ds1imusensor.html'
language: en
---

# LSM9DS1 IMU Sensor

## Ports

### Output

You can select the active sensor(s) to measure angular velocity, acceleration, magnetic
field, or a combination of these measurements.

### **Acceleration (m/s^2)** — Acceleration along each axis as measured by accelerometer vector

The block outputs acceleration as a `n`-by-3 vector,
where `n` is the value specified as Samples per frame. Each value
represents the measurement of acceleration in `g(9.8 m/s^2)` along
the X, Y, and Z axes.

#### Dependencies

This output port appears only if you select the
**Acceleration** parameter.

**Data Types:** `double`

### **Angular rate (dps)** — Angular velocity along each axis as measured by gyroscope vector

The block outputs velocity as a `n`-by-3 vector, where
`n` is the value specified as Samples per frame. Each value
represents the measurement of angular velocity in degrees per second (dps) along the
X, Y, and Z axes.

#### Dependencies

This output port appears only if you select the **Angular
rate** parameter.

**Data Types:** `double`

### **Magnetic Field (µT)** — Strength of magnetic field along each axis as measured by magnetometer vector

The block outputs magnetic field as a `n`-by-3 vector,
where `n` is the value specified as Samples per frame. Each value
represents the measurement of magnetic field in micro Tesla (µT) along the X, Y, and Z
axes.

#### Dependencies

This output port appears only if you select the **Magnetic
field** parameter.

**Data Types:** `double`

### **Timestamp** — Timestamp at which data is read matrix | (`n`)-by-1

Timestamp (in seconds) at which data is read from the sensor, returned as
`n`-by-1 matrix, where `n` is the
value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the **Timestamp**
parameter.

**Data Types:** `double`

## Parameters

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **I2C addresses** — Peripheral addresses to communicate with sensors Accelerometer/Gyroscope: `0x6A` and Magnetometer: `0x1C` (default) | `0x6B` | `0x1E`

The peripheral addresses to communicate with the accelerometer, gyroscope, and
magnetometer peripherals on the LSM9DS1 sensor are decided by the state of the SDA\_M and
SDA\_AG pins on the hardware board. This table provides the peripheral addresses
corresponding to the pins and their state.

| Pin Name | Pin State | Peripheral Address |
| --- | --- | --- |
| SDA\_M (Magnetometer) | 0 | 0x1C |
| 1 | 0x1E |
| SDA\_AG (Accelerometer and Gyroscope) | 0 | 0x6A |
| 1 | 0x6B |

**Data Types:** `uint8`

#### Select sensor outputs

### **Acceleration (m/s2)** — Set output port for reading acceleration `on` (default) | `off`

Select this parameter to set **Acceleration** as one of the output
ports.

### **Angular rate (dps)** — Set output port for reading angular velocity `on` (default) | `off`

Select this parameter to set **Angular Rate** as one of the output
ports.

### **Magnetic field (uT)** — Set output port for obtaining magnetic field `on` (default) | `off`

Select this parameter to set **Magnetic Field** as one of the
output ports.

### **Timestamp (s)** — Set output port for obtaining timestamp `off` (default) | `on`

Select this parameter to set **Timestamp** as one of the output
ports.

#### Advanced sensor settings (optional)

### **Accelerometer Output Data Rate** — Rate of measurement of acceleration `119` Hz (default) | `10` Hz | `50` Hz | `238` Hz | `476` Hz | `952` Hz

Select the rate at which you want the accelerometer to measure the acceleration.

### **Accelerometer Full Scale Range** — Sensitivity of Accelerometer +/-`2` g (default) | +/-`4` g | +/-`8` g | +/-`16` g

Select the required sensitivity for measurement of acceleration. This parameter
specifies the upper and lower limits of what the sensor can measure. In general, for all
sensors, you get a more precise measurement with a low full-scale range.

### **Accelerometer Bandwidth** — Frequency range for sensor operation `50` Hz (default) | `105` Hz | `211` Hz | `408` Hz

Set the bandwidth for the low-pass filter associated with the measurement of
acceleration.

Refer to the LSM9DS1 Sensor data sheet for further information.

### **Gyroscope Output Data Rate** — Rate of measurement of angular velocity `119` Hz (default) | `14.9` Hz | `59.5` Hz | `238` Hz | `476` Hz | `952` Hz

Select the rate at which you want the gyroscope to measure the angular velocity.

### **Gyroscope Full Scale Range** — Sensitivity of gyroscope `245` dps (default) | `500` dps | `2000` dps

Select the required sensitivity for measurement of angular velocity. This parameter
specifies the upper and lower limits of what the sensor can measure. In general, for all
the sensors, you get a more precise measurement from a sensor with a low full-scale
range.

### **Gyroscope Bandwidth Mode** — Frequency range for sensor operation `0` (default) | `1` | `2` | `3`

Select the desired bandwidth mode to set the cutoff frequency for the low-pass
filter associated with the gyroscope. Refer to this table for information regarding the
cutoff frequencies.

**Output Data Rate (ODR) and Bandwidth Configuration Setting After Low-Pass Filter
2 (LPF2)**

| Bandwidth Mode | ODR (Hz) | Cutoff (Hz) |
| --- | --- | --- |
| 0 | 14.9 | NA |
| 1 | 14.9 | NA |
| 2 | 14.9 | NA |
| 3 | 14.9 | NA |
| 0 | 59.5 | 16 |
| 1 | 59.5 | 16 |
| 2 | 59.5 | 16 |
| 3 | 59.5 | 16 |
| 0 | 119 | 14 |
| 1 | 119 | 31 |
| 2 | 119 | 31 |
| 3 | 119 | 31 |
| 0 | 238 | 14 |
| 1 | 238 | 29 |
| 2 | 238 | 63 |
| 3 | 238 | 78 |
| 0 | 476 | 21 |
| 1 | 476 | 28 |
| 2 | 476 | 57 |
| 3 | 476 | 100 |
| 0 | 952 | 33 |
| 1 | 952 | 40 |
| 2 | 952 | 58 |
| 3 | 952 | 100 |

### **Enable High Pass Filter** — Option to enable high-pass filter for gyroscope on (default) | off

Select this option to enable the high-pass filter for the gyroscope.

### **Gyroscope High Pass Filter Mode** — Mode of operation for gyroscope high-pass filter `0` (default) | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9`

Select the high-pass filter mode to set the desired cutoff frequencies for the
high-pass filter. Refer to this table given to select the desired cutoff
frequency.

**Gyroscope High Pass Filter Cutoff Frequency Configuration (Hz)**

| HPF Mode | ODR=14.9 Hz | ODR=59.5 Hz | ODR=119 Hz | ODR=238 Hz | ODR=476 Hz | ODR=952 Hz |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 1 | 4 | 8 | 15 | 30 | 57 |
| 1 | 0.5 | 2 | 4 | 8 | 15 | 30 |
| 2 | 0.2 | 1 | 2 | 4 | 8 | 15 |
| 3 | 0.1 | 0.5 | 1 | 2 | 4 | 8 |
| 4 | 0.05 | 0.2 | 0.5 | 1 | 2 | 4 |
| 5 | 0.02 | 0.1 | 0.2 | 0.5 | 1 | 2 |
| 6 | 0.01 | 0.05 | 0.1 | 0.2 | 0.5 | 1 |
| 7 | 0.005 | 0.02 | 0.05 | 0.1 | 0.2 | 0.5 |
| 8 | 0.002 | 0.01 | 0.02 | 0.005 | 0.1 | 0.2 |
| 9 | 0.001 | 0.005 | 0.01 | 0.002 | 0.005 | 0.1 |

Refer to the LSM9DS1 Sensor data sheet for further information.

### **Magnetometer Output Data Rate** — Rate of measurement of magnetic field `40` Hz (default) | `0.625` Hz | `1.25` Hz | `25` Hz | `5` Hz | `10` Hz | `20` Hz | `80` Hz

Select the required rate at which you want the Magnetometer to measure the magnetic
field.

### **Magnetometer Full Scale Range** — Sensitivity of Magnetometer +/-`4` gauss (default) | +/-`8` gauss | +/-`12` gauss | +/-`16` gauss

Select the required sensitivity for measurement of magnetic field. This parameter
specifies the upper and lower limits of what the sensor can measure. In general, for all
the sensors, you get a more precise measurement with a low full-scale range.

### **Timestamp** — Set output port for obtaining timestamp `off` (default) | `on`

Select this parameter to set **Timestamp** as one of the output
ports.

### **Samples per frame** — Number of samples that the block outputs `1` (default) | positive integer

Specify the number of samples that the block outputs.

The value that you specify here is also used to compute the output sample
time:

Output sample time = `Samples per frame * Sample time` \*
`Sample time`.

### **Sample time** — Time at which data is read from active sensors `0.1` (default) | scalar

Enter the time interval in seconds at which the block reads values from the active
sensors. The output sample time is the product of `Samples per
frame` and `Sample time` that you
specify.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Measure linear acceleration, angular rate, and magnetic field along X, Y, and Z axis

The LSM9DS1 IMU Sensor block measures linear acceleration, angular rate,
and magnetic field along the X, Y, and Z axis using the LSM9DS1 Inertial Measurement Unit
(IMU) sensor interfaced with the Arduino® hardware. This 9-Degree of Freedom (DoF) IMU sensor comprises of an
accelerometer, gyroscope, and magnetometer used to measure linear acceleration, angular rate,
and magnetic field, respectively.

**Note**

If you are using Arduino Nano 33 BLE Sense hardware, which always includes an embedded
sensor, reading data from a breakout board containing LSM9DS1 sensor is not supported.
