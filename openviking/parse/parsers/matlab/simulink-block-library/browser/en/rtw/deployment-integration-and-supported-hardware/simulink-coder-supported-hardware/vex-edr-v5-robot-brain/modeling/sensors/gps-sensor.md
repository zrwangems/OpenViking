---
type: simulink-block
title: 'GPS Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'v5gpssensor'
documentation_source_path: 'vexv5/ref/v5gpssensor.html'
language: en
---

# GPS Sensor

## Ports

### Output

### **[X, Y, θ]** — Pose three-element vector

Pose specified as a three-element vector of `[x y
θ]`, where x and y corresponds to position and
*θ* corresponds to the orientation angle.
*θ* is positive clockwise and its range is
`0-360` degrees.

**Data Types:** `double`

### **Error** — Estimate of position error scalar

This port outputs the estimation of position error in meters.

#### Dependencies

**Data Types:** `double`

### **Euler** — Yaw, pitch, and roll angles vector

The **Euler** port outputs yaw, pitch,
and roll angles as a 3-by-1 vector in the *z*-*y*-*x* sequence.

#### Dependencies

To enable this port select the **Euler angles
(deg)** parameter.

**Data Types:** `double`

### **Accel** — Acceleration vector

The **Accel** port outputs acceleration (or specific
force) in *x*, *y*, and
*z* order as a 3-by-1 vector. The Acceleration is
measured in m/s2.

#### Dependencies

To enable this port select the **Acceleration
(m/s^2)** parameter.

**Data Types:** `double`

### **Ang rate** — Angle of rotation per second about the axes of sensor vector

The **Ang rate** port outputs the angle of rotation
per second about the *x-*, *y-*, and
*z-* axes of the sensor as a 3-by-1 vector. The
angular rate is measured in deg/s.

#### Dependencies

To enable this port select the **Angular rate
(deg/s)** parameter.

**Data Types:** `double`

## Parameters

### **Smart Port** — Smart Port to which VEX V5 GPS Sensor is connected 1 (default) | `1` to `21`

Select the smart port on the V5 robot to which the VEX V5 GPS sensor is
connected. There are 21 smart ports on the V5 robot.

Assign a unique smart port for each block in the model. If you use
multiple GPS Sensor blocks with the same port, then the last executed GPS
Sensor block sets the sensor parameters.

### **Visualize** — Sensor and robot configuration GPS mounting position and initial pose

Click **Visualize** to view the GPS mounting position
and initial pose of the robot in a graph. A sample screen is shown
below.

### GPS Mounting Location (on robot)

### **X (m)** — Position coordinate 0 (default) | scalar

Set the *x*-axis position coordinate of GPS sensor
relative to the robot's center

### **Y (m)** — Position coordinate 0 (default) | scalar

Set the *y*-axis position coordinate of GPS sensor
relative to the robot's center.

### **θ (deg)** — Orientation angle 0 (default) | scalar

Set the heading of GPS sensor relative to the robot's forward axis.
Heading is measured clockwise. If the GPS sensor is in forward direction
of robot, this parameter will be `0`.

### Initial Robot pose

These parameters help the GPS sensor initialize the outputs when field strips are
not clearly visible. There is no need to set these parameters if field strips are
visible and the sensor is not too close to the strips.

### **X (m)** — Position coordinate 0 (default) | positive scalar

Set the *x*-axis position coordinate of initial robot
location on V5 Field. `0` corresponds to the center of
the field.

### **Y (m)** — Position coordinate 0 (default) | positive scalar

Set the *y*-axis position coordinate of initial robot
location on V5 Field. `0` corresponds to the center of
the field.

### **θ (deg)** — Orientation angle 0 (default) | positive scalar

Set the initial heading of robot relative to the field. Heading is
measured clockwise. If the robot is perfectly aligned against the field
code strip number `4`, heading will be
`0`.

### Additional Outputs

### **Euler Angles (deg)** — Yaw, pitch, and roll angles `off` (default) | `on`

Select the **Euler angles (deg)** parameter to enable
**Euler**port. For more information, see Euler.

### **Acceleration (m/s^2)** — Acceleration `off` (default) | `on`

Select the **Acceleration (m/s^2)** parameter to
enable **Accel** port. For more information on the
**Accel** port, see Accel.

### **Angular rate (deg/s)** — Angle of rotation per second sensor axes `off` (default) | `on`

Select the **Angular rate (deg/s)** parameter to
enable **Ang rate** port. For more information on the
**Ang rate** port, see Ang rate.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Read position and orientation

The GPS Sensor block reads position and orientation from the VEX V5 GPS
Sensor connected to the robot.

The block outputs pose as a 3-by-1 vector representing *X*,
*Y* coordinates and *θ* heading. Additionally, it
outputs an estimate of position error.

This block also allows you to visualize the sensor and robot configuration.
