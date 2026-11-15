---
type: simulink-block
title: 'Inertial Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'inertialsensor'
documentation_source_path: 'vexv5/ref/inertialsensor.html'
language: en
---

# Inertial Sensor

## Ports

### Output

### **Yaw** — Rotation around vertical z-axis vector

This port represents rotation around the vertical
*z*-axis.

#### Dependencies

To enable this port select the **Euler angles
(deg)** parameter.

**Data Types:** `double`

### **Pitch** — Angle between x-axis and horizontal plane vector

This port represents the angle between *x*-axis and
the horizontal plane.

#### Dependencies

To enable this port select the **Euler angles
(deg)** parameter.

**Data Types:** `double`

### **Roll** — Rotation around longitudinal axis vector

This port represents rotation around the longitudinal axis
(*x*-axis) of the sensor.

#### Dependencies

To enable this port select the **Euler angles
(deg)** parameter.

**Data Types:** `double`

### **Quat** — Sensor orientation given as quaternion quaternion array

The **Quat** port outputs the orientation along the
*w-*, *x-*, *y-*,
and *z-* axes of the sensor as a 4-by-1 vector. The
orientation is measured in quaternion. For more information on a
quaternion, see Quaternion

#### Dependencies

The **Quat** port is available only when you
select the **Quaternion** parameter.

### **Ang rate** — Angle of rotation per second about the axes of sensor vector

The **Ang rate** port outputs the angle of rotation
per second about the *x-*, *y-*, and
*z-* axes of the sensor as a 3-by-1 vector. The
angular rate is measured in deg/s.

#### Dependencies

To enable this port select the **Angular rate
(deg/s)** parameter.

**Data Types:** `double`

### **Accel** — Acceleration including force of gravity along sensor axes vector

The **Accel** port outputs acceleration along the
*x*, *y*, and *z*
axes of the sensor as a 3-by-1 vector. The Acceleration is measured in
m/s2 and also includes acceleration due
to gravity.

#### Dependencies

To enable this port select the **Acceleration
(m/s^2)** parameter.

**Data Types:** `double`

### **Status** — Calibration status boolean

The **Status** port outputs the calibration status.
The port outputs the status as a `boolean` value. The
status remains 0 until the calibration is complete. The sensor takes 2
seconds to complete calibration.

This table shows what each element values in the vector indicate about
the sensor calibration status.

| Value | Calibration Status |
| --- | --- |
| `0` | Uncalibrated |
| `1` | Calibrated |

#### Dependencies

To enable this port select the **Calibration
Status** parameter.

**Data Types:** `Boolean`

## Parameters

### **Smart Port** — Smart Port to which VEX V5 Inertial Sensor is connected 1 (default) | `1` to `21`

Select the smart port on the V5 robot to which the VEX V5 inertial sensor
is connected. There are 21 smart ports on the V5 robot.

Assign a unique smart port for each block in the model. If you use
multiple Inertial Sensor blocks with the same port, the last Inertial Sensor
block executed might be the only block that is active.

### **Sample time** — Interval to read values from sensor `0.2` (default) | `-1` | positive scalar

Specify the sample time in seconds to determine how often the block reads
values from the sensor. When you specify this parameter as
`-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

### Select Outputs

### **Euler angles (deg)** — Orientation of sensor `on` (default) | `off`

Select the **Euler angles (deg)** parameter to enable
**Yaw**, **Pitch**, and
**Roll** ports. For more information, see Yaw,
Pitch,
and Roll.

### **Quaternion** — Orientation of sensor `off` (default) | `on`

Select the **Quaternion** parameter to enable
**Quat** port. For more information on the
**Quat** port, see Quat.

**Data Types:** `double`

### **Angular rate (deg/s)** — Angle of rotation per second sensor axes `off` (default) | `on`

Select the **Angular rate (deg/s)** parameter to
enable **Ang rate** port. For more information on the
**Ang rate** port, see Ang rate.

### **Acceleration (m/s^2)** — Acceleration including force of gravity along sensor axes `off` (default) | `on`

Select the **Acceleration (m/s^2)** parameter to
enable **Accel** port. For more information on the
**Accel** port, see Accel.

### **Calibration Status** — Status of calibration `off` (default) | `on`

Select the **Calibration Status** parameter to enable
**Status** port. For more information on the
**Status** port, see Status.

### Additional Options

### **Yaw reset mode** — Option to reset the Inertial Sensor reading `No reset` (default) | `Reset by external signal`

Specify if the yaw mode has to be reset by external signal or
not.

- `No reset` – The block does not reset
  the inertial sensor reading and outputs the total angle of
  rotation.

  For example, at T = 1 in the table the inertial sensor rotates
  20 degrees in a counterclockwise direction,so, the output is 20.

  Between T = 1 and T = 2, the inertial sensor rotates 10
  degrees in a counterclockwise direction. Therefore, the yaw
  rotation is 30 at T = 2 (20 from T = 1 and 10 from T = 2).

  In this reset mode, the output at any time instant is a
  cumulative sum of the previous yaw rotation and the current yaw
  rotation.
- `Reset by external signal`  – The
  inertial sensor reading is reset to 0 based on the input value
  to `Rst` port. When you send a value other than
  0 to the block input, the inertial sensor reading is reset to 0.
  For each sample period, the block outputs the inertial sensor
  reading since the last reset.

  Reset mode

#### Dependencies

To enable this parameter select **Euler Angles**
parameter.

### **Yaw wrap around** — Specify the angle for yaw wrap around `No wrap around` (default) | `0 to 360` | `-180 to 180`

Specify the yaw angle limit for the inertial sensor.

Set the parameter to one of these values:

`0 to 360` -- The yaw angle rolls over to 0
after reaching 360 degrees.

`-180 to 180` -- The yaw angle rolls over to
-180 degrees after reaching 180 degrees.

`No wrap around`-- The yaw angle can go over
360 degrees.

#### Dependencies

To enable this parameter select the **Euler
Angles** parameter.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Measure orientation, acceleration, and angular rate

The Inertial Sensor block reads data from the Inertial sensor that is
connected to the VEX® V5 Brain.

By default, the block outputs yaw, pitch, and roll (as Euler angles following the
3-2-1 convention). The block also outputs the quaternion, angular rate, and
acceleration. The block returns the angular rate and acceleration as 3-by-1 double
vector in `x-y-z` order and quaternion is returned as 4-by-1
double.

The VEX V5 inertial sensor auto-detects and adjusts for the mounting position. This
allows the sensor to output the same orientation (Euler angles) even when the sensor is
mounted upside down. For more information, see Using the V5 Inertial Sensor.

The sensor takes about 2 seconds for calibration when you start a program. Ensure that
the inertial sensor is kept steady on a level surface while starting the program.

**Note**

When the sensor is placed on a level surface and if the pitch or roll angles
show errors (of more than 1 degree), then you might need to calibrate the
accelerometer.
