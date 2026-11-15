---
type: simulink-block
title: 'MPU6050 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'mpu6050imusensor'
documentation_source_path: 'supportpkg/arduino_ref/mpu6050imusensor.html'
language: en
---

# MPU6050 IMU Sensor

## Ports

### Output

### **Accel** — Acceleration including force of gravity along axes of sensor vector

The **Accel** port outputs acceleration along the
*x-*, *y-*, and
*z-*axes of the sensor as a
3-by-`n` vector, where
`n` is the value specified as Samples per frame.
The acceleration is measured in m/s2 and also
includes acceleration due to gravity.

#### Dependencies

The **Accel** port is available only when you
select the **Acceleration (m/s^2)** parameter.

**Data Types:** `double`

### **Ang rate** — Angle of rotation per second along axes of sensor vector

The **Ang rate** port outputs the angle of rotation
per second along the *x-*, *y-*, and
*z-*axes of the sensor as a
3-by-`n` vector, where
`n` is the value specified as Samples per frame.
The angular rate is measured in dps.

#### Dependencies

The **Ang rate** port is available only when you
select the **Angular rate (dps)** parameter.

**Data Types:** `double`

### **Temperature** — Temperature along axes of sensor vector

The **Temperature** port outputs the temperature
along the *x-*, *y-*, and
*z-*axes of the sensor. The temperature is measured
in degree Celsius.

#### Dependencies

The **Temperature** port is available only when
you select the **Temperature (deg C)**
parameter.

**Data Types:** `double`

### **Status** — Status of read operation scalar

The **Status** port outputs the status of the read
operation. The port outputs the status as a `uint8`
value. Each value corresponds to the data transfer status.

| Status Value | Status Description |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `BUS_ERROR` |
| `16` | `BUS_NOT_IN_USE` |
| `32` | `SENSOR_INIT_ERROR` |

#### Dependencies

The **Status** port is available only when you
select the **Status** parameter.

**Data Types:** `uint8`

### **Timestamp** — Timestamp at which data is read matrix | (`n`)-by-1

Timestamp (in seconds) at which data is read from the sensor, returned
as `n`-by-1 matrix, where
`n` is the value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the
**Timestamp** parameter.

**Data Types:** `double`

## Parameters

### **I2C module** — I2C communication module `0` (default) | scalar

Specify the I2C module on the Arduino® hardware to communicate with sensor peripherals. For more
information on the Arduino pin mapping and modules that hardware boards support, see
Pin Mapping for Arduino Timer-Independent Blocks.

### **I2C address** — I2C peripheral address of sensor `0x68` (default) | `0x69`

Select the I2C address of the sensor from which the block reads the
values.

### **Samples per frame** — Number of samples that the block outputs `1` (default) | positive integer

Specify the number of samples that the block outputs.

The value that you specify here is also used to compute the output sample
time:

Output sample time = `Samples per frame` \*
`Sample time`.

### **Sample time** — Interval to read values from sensor `–1` (default) | any nonnegative value

Specify how often the block read values from the sensor, in seconds. When
you specify this parameter as `-1`, Simulink® determines the best sample time for the block based on the
block context within the model. The output sample time is the product of
`Samples per frame` and `Sample
time` that you specify.

### Select outputs

### **Acceleration (m/s^2)** — Acceleration including force of gravity along axes of sensor `on` (default) | `off`

When you select the **Acceleration (m/s^2)**
parameter, the **Accel** port becomes available. For
more information on the **Accel** port, see Accel.

### **Angular rate (dps)** — Angle of rotation per second along axes of sensor `on` (default) | `off`

When you select the **Angular rate (dps)** parameter,
the **Ang rate** port becomes available. For more
information on the **Ang rate** port, see Ang rate.

### **Temperature (deg C)** — Temperature along axes of sensor `on` (default) | `off`

When you select the **Temperature (deg C)**
parameter, the **Temperature** port becomes available.
For more information on the **Temperature (deg C)**
port, see Temperature.

### **Status** — Status of read operation `on` (default) | `off`

Select this parameter to display the status of read operation.

When you select the **Status** parameter, the
**Status** port becomes available. For more
information on the **Status** port, see Status.

### **Timestamp (s)** — Set output port for obtaining timestamp `off` (default) | `on`

Select this parameter to set **Timestamp** as one of
the output ports.

### Advanced sensor settings (optional)

### **Accelerometer range** — Range of acceleration deviation measured by accelerometer `2G` (default) | `4G` | `8G` | `16G`

Select a deviation in the acceleration that the accelerometer can
measure. The smaller the accelerometer range, the more sensitive the
readings from the accelerometer. A small range provides more detailed
data, resulting in a more precise reading from the accelerometer.

#### Dependencies

The **Accelerometer range** parameter is
available only when you select the **Acceleration
(m/s^2)** parameter.

### **Gyroscope range** — Maximum angular velocity measured by gyroscope `250 dps` (default) | `500 dps` | `1000 dps` | `2000 dps`

Specify the maximum angular velocity that the gyroscope can measure
per second.

#### Dependencies

The **Gyroscope range** parameter is available
only when you select the **Angular rate (dps)**
parameter.

### **Accelerometer and Gyroscope bandwidth** — Frequency response of accelerometer and gyroscope `Accelerometer: 184Hz, Gyroscope: 188Hz` (default) | `Accelerometer: 260Hz, Gyroscope: 256Hz` | `Accelerometer: 94Hz, Gyroscope: 98Hz` | `Accelerometer: 44Hz, Gyroscope: 42Hz` | `Accelerometer: 21Hz, Gyroscope: 20Hz` | `Accelerometer: 10Hz, Gyroscope: 10Hz` | `Accelerometer: 5Hz, Gyroscope: 5Hz`

Specify the highest frequency at which the accelerometer and gyroscope
samples the signal without aliasing.

#### Dependencies

The **Accelerometer and Gyroscope bandwidth**
parameter is available only when you select the
**Acceleration (m/s^2)** or **Angular
rate (dps)** parameter.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020a**

## Description

Measure acceleration, angular rate, and temperature along axes of MPU-6050 sensor

The MPU6050 IMU Sensor block reads data from the MPU-6050 sensor that
is connected to the hardware.

The block outputs acceleration, angular rate, and temperature along the axes of the
sensor. The block outputs acceleration and angular rate as a
3-by-`n` double-precision array, where
`n` is the value specified as Samples per frame. The temperature
data is output as a scalar double.

**Note**

The output from the MPU-6050 sensor may have a finite non-negligible offset value
except for the `Temperature` output. You
may consider correcting this offset value for such cases.

This diagram shows the default orientation of the *x-*,
*y-*, and *z-*axes of the MPU-6050 sensor.

If you simulate a model that contains the MPU6050 IMU Sensor block
without connecting it to the hardware, the block outputs zeros. For more information,
see Block Produces Zeros or Does Nothing in Simulation.
