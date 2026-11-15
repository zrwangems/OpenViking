---
type: simulink-block
title: 'LSM6DS3 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'lsm6ds3imusensor'
documentation_source_path: 'supportpkg/arduino_ref/lsm6ds3imusensor.html'
language: en
---

# LSM6DS3 IMU Sensor

## Ports

### Output

### **Acceleration** — Acceleration along each axis as measured by accelerometer vector

The block outputs acceleration as a `n`-by-3 vector,
where `n` is the value specified as Samples per frame. Each value
represents the measurement of acceleration in `m/s^2` along the X, Y,
and Z axes.

#### Dependencies

This output port appears only if you select the **Acceleration
(m/s2)** parameter.

**Data Types:** `double`

### **Angular Velocity** — Angular velocity along each axis as measured by gyroscope vector

The block outputs angular velocity as a `n`-by-3 vector,
where `n` is the value specified as Samples per frame. Each value
represents the measurement of angular velocity in radians per second (rad/s) along the
X, Y, and Z axes.

#### Dependencies

This output port appears only if you select the **Angular Velocity
(rad/s)** parameter.

**Data Types:** `double`

### **Temperature** — Temperature measured by LSM6DS3 sensor scalar

Temperature (in ℃) measured by LSM6DS3 sensor connected to Arduino board.

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

### **Timestamp** — Timestamp at which data is read matrix | (`n`)-by-1

Timestamp (in seconds) at which data is read from the sensor, returned as
`n`-by-1 matrix, where `n` is the
value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the **Timestamp**
parameter.

**Data Types:** `double`

## Parameters

### Main

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino hardware to communicate with sensor peripherals. For more information on
the Arduino pin mapping and modules that hardware boards support, see Pin Mapping for Arduino Timer-Independent Blocks.

### **I2C address** — Peripheral addresses to communicate with sensors `0x6A` (default) | `0x6B`

The peripheral addresses to communicate with the accelerometer and gyroscope
peripherals on the LSM6DS3 sensor are decided by the state of the SDO/SA0 pin on the
sensor board. This table provides the peripheral addresses corresponding to the pin
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

### **Timestamp** — Set output port for obtaining timestamp `off` (default) | `on`

Select this parameter to set **Timestamp** as one of the output
ports.

### **Samples per frame** — Number of samples that the block outputs `1` (default) | positive integer

Specify the number of samples that the block outputs.

The value that you specify here is also used to compute the output sample
time:

Output sample time = `Samples per frame` \*
`Sample time`.

### **Sample time** — Time interval to read data `-1` (default) | positive integer

Specify how often this block reads the data from the LSM6DS3 sensor. When you set
this parameter to -1, Simulink determines the best sample time for the block based on
the block context within the model. The output sample time is the product of
`Samples per frame` and `Sample
time` that you specify.

### Advanced

#### Accelerometer

### **Full scale range** — Full scale for measuring linear acceleration `±2g` (default) | `±4g` | `±8g` | `±16g`

Select the full scale for measuring linear acceleration (the range of acceleration
that the sensor needs to measure).

### **Output data rate** — Rate at which accelerometer data is sampled `12.5 Hz` (default) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz` | `3332 Hz` | `6664 Hz`

Select the output data rate at which accelerometer data is sampled, which also
determines the bandwidth.

### **Configure analog filter bandwidth** — Set option to configure analog filter bandwidth `off` (default) | `on`

Select this parameter to configure the bandwidth of analog low-pass filter used in
the filtering chain of the accelerometer values.

### **Analog filter bandwidth** — Bandwidth of low-pass analog filter `400 Hz` (default) | `50 Hz` | `100 Hz` | `200 Hz`

Select the required bandwidth of the low-pass analog filter.

#### Dependencies

This parameter appears only if you select the **Configure analog filter
bandwidth** parameter.

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

### **Output data rate** — Rate at which gyroscope data is sampled `12.5 Hz` (default) | `26 Hz` | `52 Hz` | `104 Hz` | `208 Hz` | `416 Hz` | `833 Hz` | `1666 Hz`

Select the output data rate at which gyroscope data is sampled, which also
determines the bandwidth.

### **Enable high pass filter** — Enable high pass filter for gyroscope data `off` (default) | `on`

Enable the high pass filter for reading gyroscope values.

### **High pass filter bandwidth** — Bandwidth of high pass filter `0.0081 Hz` (default) | `0.0324 Hz` | `2.07 Hz` | `16.32 Hz`

Select the required bandwidth of the high pass filter for reading gyroscope
values.

#### Dependencies

This parameter appears only if you select the **Enable high pass
filter** parameter.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Measure linear acceleration, angular rate, and temperature from LSM6DS3 sensor

The LSM6DS3 IMU Sensor block measures linear acceleration and angular rate
along the X, Y, and Z axis using the LSM6DS3 Inertial Measurement Unit (IMU) sensor interfaced
with the Arduino® hardware. This 6-Degree of Freedom (DoF) IMU sensor comprises of an
accelerometer and gyroscope used to measure linear acceleration and angular rate,
respectively. The block also measures the temperature from the embedded temperature sensor in
LSM6DS3 Sensor.

You can also use the analog filter and composite filter options in the block for the
accelerometer values, and use the high pass filter option for gyroscope values.
