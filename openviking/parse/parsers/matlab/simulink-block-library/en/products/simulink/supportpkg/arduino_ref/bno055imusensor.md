---
type: simulink-block
title: 'BNO055 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Acceleration Sensors'
documentation_page: 'bno055imusensor'
documentation_source_path: 'supportpkg/arduino_ref/bno055imusensor.html'
language: en
---

# BNO055 IMU Sensor

## Ports

### Output

### **Accel** — Acceleration including force of gravity along axes of sensor matrix

The **Accel** port outputs acceleration along the
*x*, *y*, and *z*
axes of the sensor as a 3-by-`n` vector, where
`n` is the value specified as Samples per frame.
In Fusion mode, the elements of the vector represent calibrated values,
whereas in Non-Fusion mode, the elements represent raw values. The
acceleration is measured in m/s2 and also
includes acceleration due to gravity.

#### Dependencies

The **Accel** port is available only when you
select the **Acceleration (m/s^2)** parameter.

**Data Types:** `double`

### **Ang rate** — Angle of rotation per second about axes of sensor matrix

The **Ang rate** port outputs the angle of rotation
per second about the *x-*, *y-*, and
*z-* axes of the sensor as a
3-by-`n` vector, where
`n` is the value specified as Samples per frame.
In Fusion mode, the elements of the vector represent calibrated values,
whereas in Non-Fusion mode, the elements represent raw values. The
angular rate is measured in dps.

#### Dependencies

The **Ang rate** port is available only when you
select the **Angular rate (dps)** parameter.

**Data Types:** `double`

### **Mag field** — Strength of magnetic field along axes of sensor matrix

The **Mag field** port outputs the strength of the
magnetic field along the *x-*, *y-*,
and *z-* axes of the sensor as a
3-by-`n` vector, where
`n` is the value specified as Samples per frame.
In Fusion mode, the elements of the vector represent calibrated values,
whereas in Non-Fusion mode, the elements represent raw values. The
magnetic strength is measured in μT.

#### Dependencies

The **Mag field** port is available only when you
select the **Magnetic field (μT)**
parameter.

**Data Types:** `double`

### **Euler** — Sensor orientation given as Euler angles matrix

The **Euler** port outputs the orientation along the
axes of the sensor as a 3-by-n vector in the Azimuth-Pitch-Roll notation
(*z*-*y*-*x*
sequence). Here `n` is the value specified as
Samples per frame

| Angular Quantity | Range in Degrees |
| --- | --- |
| Azimuth | [0, 360] |
| Pitch | [−180, 180] |
| Roll | [−90, 90] |

#### Dependencies

The **Euler** port is available only when you set
the **Operation mode** to
`Fusion` and select the **Euler
angles (degrees)** parameter.

**Data Types:** `double`

### **Quat** — Sensor orientation given as a quaternion quaternion array

The **Quat** port outputs the orientation along the
*w-*, *x-*, *y-*,
and *z-* axes of the sensor as a
4-by-`n` vector, where
`n` is the value specified as Samples per frame.
The orientation is measured in quaternion.

#### Dependencies

The **Quat** port is available only when you set
the **Operation mode** to
`Fusion` and select the
**Quaternion (quaternion)** parameter.

**Data Types:** `double`

### **Lin accel** — Acceleration excluding force of gravity along axes of sensor matrix

The **Lin accel** port outputs linear acceleration
along the *x-*, *y-*, and
*z-* axes of the sensor as a
3-by-`n` vector, where
`n` is the value specified as Samples per frame.
The acceleration is measured in m/s2 and does
not include acceleration due to gravity.

#### Dependencies

The **Lin accel** port is available only when you
set the **Operation mode** to
`Fusion` and select the
**Linear acceleration (m/s^2)**
parameter.

**Data Types:** `double`

### **Gravity** — Acceleration due to gravity along axes of sensor matrix

The **Gravity** port outputs acceleration due to
gravity along the *x-*, *y-*, and
*z-* axes of the sensor as a
3-by-`n` vector, where
`n` is the value specified as Samples per frame.
The acceleration due to gravity is measured in
m/s2.

#### Dependencies

The **Gravity** port is available only when you
set the **Operation mode** to
`Fusion` and select the
**Gravity vector (m/s^2)** parameter.

**Data Types:** `double`

### **Status** — Calibration status of overall system and gyroscope, accelerometer, and magnetometer matrix

The **Status** port outputs the calibration status of
the overall system and the sensors (gyroscope, accelerometer, and
magnetometer) located inside the BNO055 sensor as a
4-by-`n` vector, where
`n` is the value specified as Samples per frame.

This table shows what each element values in the vector indicate about
the sensor calibration status.

| Value | Calibration Status |
| --- | --- |
| `0` | Uncalibrated |
| `1` and `2` | Partially calibrated |
| `3` | Fully calibrated |

A partially calibrated sensor with a calibration status of
`2` provides more accurate readings than the sensor
with a calibration status of `1`. To fully calibrate
any of these sensors, see Calibrate Gyroscope, Calibrate Accelerometer, and Calibrate Magnetometer.

**Note**

If the **Status** port outputs an array with all
the elements having a value of `-1`, ensure that
the sensor is properly connected to the hardware and the value of
the **I2C address** parameter is correct.

#### Dependencies

The **Status** port is available only when you
set the **Operation mode** to
`Fusion`.

**Data Types:** `int8`

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

### **I2C address** — I2C peripheral address of sensor `0x28` (default) | `0x29`

Select the I2C address of the sensor from which the block read
values.

### **Operation mode** — Option to output calibrated or raw values `Fusion` (default) | `Non-Fusion`

- `Fusion` — When you set
  **Operation mode** to
  `Fusion`, the sensor operates in 9
  degrees of freedom (NDOF) mode. The block outputs calibrated
  values from the sensor.

  This table lists the block output, measurement unit,
  dimension, and the axes of the sensor along which each of these
  outputs are measured.

  | Output | Unit | Dimensiona | Axes |
  | --- | --- | --- | --- |
  | Acceleration | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | Angular rate | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | Magnetic field | microtesla (μT) | 3-by-n | *x*, *y*, and *z* |
  | Euler angles | degrees per second (dps) | 3-by-n | *x*, *y*, and *z* |
  | Quaternions | Quaternion units | 4-by-n | *w*, *x*, *y*, and *z* |
  | Linear acceleration | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | Gravity vector | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | a `n` is the value specified as Samples per frame | | | |

  **Note**

  In Fusion mode, an internal fusion algorithm configures
  the range and bandwidth of the sensor with some values.
  These values cannot be modified.
- `Non-Fusion` — When you set
  **Operation mode** to
  `Non-Fusion`, the sensor operates
  in Accelerometer Magnetometer Gyroscope (AMG) mode. The block
  outputs raw values from the sensor.

  This table lists the block output, measurement unit,
  dimension, and the axes of the sensor along which each of these
  outputs are measured in Non-Fusion mode.

  | Output | Unit | Dimensiona | Axes |
  | --- | --- | --- | --- |
  | Acceleration | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | Angular rate | Meter per second squared (m/s2) | 3-by-n | *x*, *y*, and *z* |
  | Magnetic field | microtesla (μT) | 3-by-n | *x*, *y*, and *z* |
  | a `n` is the value specified as Samples per frame | | | |

### **Samples per frame** — Number of samples that the block outputs `1` (default) | positive integer

Specify the number of samples that the block outputs.

The value that you specify here is also used to compute the output sample
time:

Output sample time = `Samples per frame` \*
`Sample time`.

### **Sample time** — Interval to read values from sensor `–1` (default) | `-1` | any nonnegative value

Specify how often the block read values from the sensor, in seconds. When
you specify this parameter as `-1`, Simulink® determines the best sample time for the block based on the
block context within the model. The output sample time is the product of
`Samples per frame` and `Sample
time` that you specify.

### Select Outputs

### **Acceleration (m/s^2)** — Acceleration including force of gravity along axes of sensor `on` (default) | `off`

When you select the **Acceleration (m/s^2)**
parameter, the **Accel** port becomes available. For
more information on the **Accel** port, see Accel.

### **Angular rate (dps)** — Angle of rotation per second about axes of sensor `on` (default) | `off`

When you select the **Angular rate (dps)** parameter,
the **Ang rate** port becomes available. For more
information on the **Ang rate** port, see Ang rate.

### **Magnetic field (μT)** — Strength of magnetic field along axes of sensor `on` (default) | `off`

When you select the **Magnetic field (μT)**
parameter, the **Mag field** port becomes available.
For more information on the **Mag field** port, see
Mag field.

**Data Types:** `double`

### **Euler angles (degrees)** — Orientation along axes of sensor `off` (default) | `on`

When you select the **Euler angles (degrees)**
parameter, the **Euler** port becomes available. For
more information on the **Euler** port, see Euler.

#### Dependencies

The **Euler angles (degrees)** parameter is
available only when you set the **Operation mode**
to `Fusion`.

### **Quaternion (quaternion)** — Orientation along axes of sensor `off` (default) | `on`

When you select the **Quaternion (quaternion)**
parameter, the **Quat** port becomes available. For
more information on the **Quat** port, see Quat.

#### Dependencies

The **Quaternion (quaternion)** parameter is
available only when you set the **Operation mode**
to `Fusion`

**Data Types:** `double`

### **Linear acceleration (m/s^2)** — Acceleration excluding force of gravity along axes of sensor `off` (default) | `on`

When you select the **Linear acceleration (m/s^2)**
parameter, the **Lin accel** port becomes available.
For more information on the **Lin accel** port, see
Lin accel.

#### Dependencies

The **Linear acceleration (m/s^2)** parameter is
available only when you set the **Operation mode**
to `Fusion`.

### **Gravity vector (m/s^2)** — Acceleration due to gravity along axes of sensor `off` (default) | `on`

When you select the **Gravity vector (m/s^2)**
parameter, the **Gravity** port becomes available. For
more information on the **Gravity** port, see Gravity.

#### Dependencies

The **Gravity vector (m/s^2)** parameter is
available only when you set the **Operation mode**
to `Fusion`.

### **Status** — Status of read operation `on` (default) | `off`

Select this parameter to display the status of read operation.

When you select the **Status** parameter, the
**Status** port becomes available. For more
information on the **Status** port, see Status.

### **Timestamp (s)** — Set output port for obtaining timestamp `off` (default) | `on`

Select this parameter to set **Timestamp** as one of
the output ports.

### Advanced Sensor Settings

### **Accelerometer range** — Range of acceleration deviation measured by accelerometer `4G` (default) | `2G` | `8G` | `16G`

Specify the deviation in the acceleration that the accelerometer can
measure. The smaller the accelerometer range is, the more sensitive the
readings from the accelerometer are. A small range provides more
detailed data, resulting in a more precise reading from the
accelerometer.

#### Dependencies

The **Accelerometer range** parameter is
available only when you set the **Operation mode**
to `Non-Fusion`.

### **Accelerometer bandwidth** — Frequency response of accelerometer `62.5 Hz` (default) | `7.81 Hz` | `15.63 Hz` | `31.25 Hz` | `125 Hz` | `250 Hz` | `500 Hz` | `1000 Hz`

Specify the frequency at which the accelerometer measures
acceleration.

#### Dependencies

The **Accelerometer bandwidth** parameter is
available only when you set the **Operation mode**
to `Non-Fusion`.

### **Gyroscope range** — Maximum angular velocity measured by gyroscope `2000 dps` (default) | `125 dps` | `250 dps` | `500 dps` | `1000 dps`

Specify the maximum angular velocity that the gyroscope can measure
per second.

#### Dependencies

The **Gyroscope range** parameter is available
only when you set the **Operation mode** to
`Non-Fusion`.

### **Gyroscope bandwidth** — Frequency response of gyroscope `32 Hz` (default) | `12 Hz` | `23 Hz` | `47 Hz` | `64 Hz` | `116 Hz` | `230 Hz` | `523 Hz`

Specify the frequency at which the gyroscope measures angular
velocity.

#### Dependencies

The **Gyroscope bandwidth** parameter is
available only when you set the **Operation mode**
to `Non-Fusion`.

### **Magnetometer output data range** — Rate at which data is sampled `15 Hz` (default) | `2 Hz` | `6 Hz` | `8 Hz` | `10 Hz` | `20 Hz` | `25 Hz` | `30 Hz`

Specify the range of the magnetic field that the magnetometer can
read.

#### Dependencies

The **Magnetometer output data range** parameter
is available only when you set the **Operation
mode** to `Fusion`

**Data Types:** `double`

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Measure acceleration, angular rate, and magnetic field, and calculate fusion values such as Euler angles, quaternion, linear acceleration, and gravity vector along the axes of BNO055 sensor

The BNO055 IMU Sensor block reads data from the BNO055 IMU sensor that
is connected to the hardware. The block has two operation modes: Non-Fusion and
Fusion.

The block outputs acceleration, angular rate, and strength of the magnetic field along
the axes of the sensor in Non-Fusion and Fusion mode. In Fusion mode, the block also
outputs the orientation of the sensor as an Euler angle or quaternion, as well as the
linear acceleration, gravity vectors, and calibration status of the sensor. The values
emitted in the Non-Fusion mode are raw values, whereas the values emitted in the Fusion
mode are calibrated values. The block outputs all the values except for quaternion and
calibration status as a 3-by-n array of `double` data type. The
quaternion is a 4-by-n array of `double` data type, and the calibration
status is a 4-by-n array of `int8` data type. Here,
`n` is the value specified as Samples per frame

If you simulate a model that contains the BNO055 IMU Sensor block
without connecting the hardware, the block outputs zeros. For more information, see
Block Produces Zeros or Does Nothing in Simulation.
