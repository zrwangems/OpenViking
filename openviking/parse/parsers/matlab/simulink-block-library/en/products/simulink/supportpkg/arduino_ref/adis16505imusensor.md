---
type: simulink-block
title: 'ADIS16505 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'adis16505imusensor'
documentation_source_path: 'supportpkg/arduino_ref/adis16505imusensor.html'
language: en
---

# ADIS16505 IMU Sensor

## Ports

### Output

### **Acceleration** — Linear acceleration along axes of sensor row vector

The **Acceleration** port outputs acceleration in
m/s2 along the x-, y-, and z- axes of the sensor
as a `n`-by-3 vector, where
`n` is the value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the **Acceleration
(m/s2)** parameter.

**Data Types:** `double` | `single` | `int32`

### **Angular Rate** — Angle of rotation per second along axes of sensor row vector

The **Angular Rate** port outputs angular velocity in
radians per second (rad/s) along the x-, y-, and z- axes of the sensor as a
`n`-by-3 vector, where `n`
is the value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the **Angular
Velocity (rad/s)** parameter.

**Data Types:** `double` | `single` | `int32`

### **Temperature** — Temperature along axes of sensor scalar

Temperature (in ℃) measured by ADIS16505 IMU sensor connected to Arduino
board.

#### Dependencies

This output port appears only if you select the **Temperature
(℃)** parameter.

**Data Types:** `double` | `single` | `int32`

### **Status** — Status of acceleration, angular velocity and temperature measurements `0` | `1`

Status of acceleration, angular velocity and temperature measurements,
specified as a scalar. `0` indicates that the data read is
new, `1` indicates that the data read is not new.

**Note**

To observe the status changes, set the block sample time to less than
`0.5` milliseconds. This is because the ADIS16505 sensor
operates at a clock frequency of `2000` Hz.

#### Dependencies

The **Status** port is available only when you select
the **Status** parameter.

**Data Types:** `uint8`

### **Timestamp** — Timestamp at which data is read matrix | (`n`)-by-1

Timestamp (in seconds) at which data is read from the sensor, returned as
`n`-by-1 matrix, where `n`
is the value specified as Samples per frame.

#### Dependencies

This output port appears only if you select the **Timestamp
(s)** parameter.

**Data Types:** `double`

## Parameters

### **SPI chip select pin** — Chip select pin to which SPI peripheral device is connected `10` (default) | target hardware pin

Enter the pin number on the Arduino® board to which the sensor chip select pin is connected. See Pin Mapping for Arduino Timer-Independent Blocks to know the
SS pin restriction with different Arduino boards.

### **Interrupt type** — Generate interrupt when data is ready `Active high` (default) | `Active low`

Select the logic level for INT1 pin as `Active high`
or `Active low`.

### **Desired output data rate (1 Hz - 2000 Hz)** — Rate at which accelerometer data is sampled `1` (default)

Enter the desired output data rate between `1` Hz to
`2000` Hz, at which accelerometer data has to be
sampled.

Accelerometer data output rate in Hz is determined by the following
calculation.

`Achieved output data rate = 2000/(1+DEC_RATE)`, where
`DEC_RATE` is `0,1,2,...1999`.

Depending on the desired output data rate specified on the block mask,
`Achieved output data rate (Hz)` will be set on the sensor.

### **No of taps for Bartlett window filter** — Number of taps `1` (default) | `2` | `4` | `8` | `16` | `32` | `64`

Select the number of taps for Bartlett window filter.

Click **Frequency response based on number of taps** to view
the frequency response of Bartlett filter. A sample screen is shown below.

Bartlett Window Filter

### **Data type** — Type of output data `double` (default) | `single` | `int32`

Specify the datatype for acceleration, angular rate, and temperature
outputs.

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

When you select the **Acceleration (m/s^2)** parameter, the
**Acceleration** port becomes available. For more
information on the **Acceleration** port, see Acceleration.

### **Angular velociy (rad/s)** — Angle of rotation per second along axes of sensor `on` (default) | `off`

When you select the **Angular velocity (rad/s)** parameter,
the **Angular Rate** port becomes available. For more
information on the **Angular Rate** port, see Angular Rate.

### **Temperature (deg C)** — Temperature along axes of sensor `on` (default) | `off`

When you select the **Temperature (deg C)** parameter, the
**Temperature** port becomes available. For more
information on the **Temperature (deg C)** port, see Temperature.

### **Status** — Status of read operation `on` (default) | `off`

Select this parameter to display the status of read operation.

When you select the **Status** parameter, the
**Status** port becomes available. For more information on
the **Status** port, see Status.

### **Timestamp (s)** — Set output port for obtaining timestamp `on` (default) | `off`

Select this parameter to set **Timestamp** as one of the
output ports. For more information on the **Timestamp** port,
see Timestamp.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Measure acceleration, angular rate, and temperature along axes of ADIS16505 sensor

The ADIS16505 IMU Sensor block outputs the values of acceleration,
angular rate, and temperature along x-, y- and z- axes as measured by the ADIS16505 IMU
Sensor connected to Arduino board.

**Note**

The output from the ADIS16505 sensor may have a finite non-negligible offset value
except for the `Temperature` output. You may consider correcting this offset value for
such cases.

If you simulate a model that contains the ADIS16505 IMU Sensor block
without connecting it to the hardware, the block outputs zeros. For more information, see
Block Produces Zeros or Does Nothing in Simulation.
