---
type: simulink-block
title: 'Differential Drive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Drivetrain'
documentation_page: 'differentialtankdrive'
documentation_source_path: 'vexv5/ref/differentialtankdrive.html'
language: en
---

# Differential Drive

## Ports

### Input

### **Ref** — Reference pose three-element vector

Final pose or waypoint specified as a three-element vector of
`[x y θ]`, where x and y corresponds to position
and *θ* corresponds to the orientation angle. Positive
angles are measured counterclockwise from the positive
*x*-axis relative to starting pose.

Since the differential drive robot cannot move sideways, position (x,
y) and angle *θ* references are controlled one after
the other. First the robot moves to the specified position and then
turns towards the specified angle.
### Output

### **Status** — Activity status of the drive 0 | `1`

This port outputs if the drive block is active or not. Use this output
to determine if the current waypoint is reached. The status is active
when:

- The drive is moving or turning.
- The sensors (inertial sensor or gyroscope) are being
  calibrated.

The port returns `1` when the drive is
active and `0` otherwise.

**Data Types:** `Boolean`

### **WWheel** — Target wheel speeds two-element vector

This port outputs the target wheel speed from right to left order
measured in radians per second. This block contains controller logic
that provides wheel speed commands, which corresponds to motor commands
sent to Smart Motor write blocks.

You can use this output to monitor the wheel speed commands or to add
additional Smart Motors.

#### Dependencies

To enable this port select **Target wheel speeds in right,
left order (rad/s)** parameter.

**Data Types:** `double`

### **Pose** — Current robot pose three-element vector

Current vehicle pose, specified as a three-element vector of
`[x y θ]`, where x and y corresponds to position
and *θ* corresponds to orientation angle. Positive
angles are measured counterclockwise from the positive
*x*-axis.

Use this block to monitor the robot’s current position and
heading.

#### Dependencies

To enable this port select **Current Pose**
parameter.
### Optional outputs

### **Target wheel speeds in right, left order (rad/s)** — Target wheel speeds `off` (default) | `on`

Select the **Target wheel speeds in right, left order
(rad/s)** parameter to enable the
**WWheel** port. For
more information on the **Wheel** port, see Wheel.

### **Current pose (x,y, θ)** — Current position and orientation `off` (default) | `on`

Select the **Current pose (x,y, θ)** parameter to
enable the **Pose** port. For more information on the
**Pose** port, see Pose.

## Parameters

### Drive

### **Configuration** — Drivetrain configuration `2-Motor Differential (Tank) Drive` (default) | `4-Motor Differential (Tank) Drive`

Select the drivetrain configuration based on the number of smart
motors present. If the robot drivetrain is driven by two motors, select
`2-Motor Differential (Tank) Drive`. If it
is driven by four motors, select `4-Motor Differential
(Tank) Drive`.

### **Flip drive direction** — Changes drive direction `off` (default) | `on`

This parameter flips or reverses the direction of all smart motors
(left and right) used in the drivetrain. The default value works for
configurations where there is no direction reversal between motors and
wheels (for example, a V5 speed bot).

When there are gears between motor and wheel, the motor and wheel might
move in opposite directions. In such cases, select this option.
Selecting this parameter incorrectly will destabilize the heading
control.

### **Left smart motor ports** — Select the left smart port 1 (default) | `1` to `21`

Select the smart port to which the left motor is connected. There are
21 smart ports on V5 Robot Brain. Assign a unique port number to each
motor.

### **Left smart motor ports** — Select the left smart port 3 (default) | `1` to `21`

Select the smart port to which the left motor is connected. There are
21 smart ports on V5 Robot Brain. Assign a unique port number to each
motor.

#### Dependencies

To enable this port set the **Configuration**
parameter to `4-Motor Differential (Tank)
Drive`.

### **Right smart motor ports** — Select the right smart port 2 (default) | `1` to `21`

Select the smart port to which the right motor is connected. There are
21 smart ports on V5 Robot Brain. Assign a unique port number to each
motor.

### **Right smart motor ports** — Select the right smart port 4 (default) | `1` to `21`

Select the smart port to which the right motor is connected. There are
21 smart ports on V5 Robot Brain. Assign a unique port number to each
motor.

#### Dependencies

The port is available only when you select the
`4-Motor Differential (Tank) Drive`
parameter.

### **Motor gear catridge** — Motor gear catridge ratio 18:1 (default) | `36:1` | `6:1`

Select the internal gear ratio for smart motors used in the
drivetrain.

### **Gear ratio (motor to wheel)** — value for gear ratio (motor to wheel) 1 (default) | positive value

Enter the value for motor to wheel gear ratio for VEX V5 Differential
(Tank) Drive.

If the motors are connected directly to wheels without any gear
reduction (direct drive), **Gear ratio (motor to
wheel)** is 1, else set the gear ratio. For example, if
wheels turn once for every two rotations of motor, then the ratio is 2/1
or 2.

### **VEX wheel diameter** — wheel diameter 4" (default) | `2.75"` | `3.25"` | `5"` | `6"` | `other`

Select the wheel diameter in inches. If your wheel diameter is not
listed, select `other` and then enter the wheel
diameter.

### **Wheel diameter (m)** — wheel diameter 0.1016 (default) | positive value

Enter the wheel diameter in meters.

#### Dependencies

To enable this parameter, select `other`
in **VEX wheel diameter** parameter.

### **Track width (m)** — value for track width 0.2950 (default) | positive value

Enter the track width in meters.

### Sensors

### **Heading sensor** — Select the heading sensor `Inertial sensor` (default) | `Gyroscope` | `smart motor encoders`

Select the sensor to provide heading feedback.

For best results, select `Inertial sensor`.
Gyroscopes tend to drift over time and `smart motor
encoders` are susceptible to wheel slippage and might
lead to inaccurate heading.

### **Port** — Set the port for Inertial Sensor 5 (default) | `1` to `21`

Select the smart port to which the motor is connected. There are 21
smart ports on V5 Robot Brain. Assign a unique port number to each
motor.

#### Dependencies

To enable this parameter, select `Inertial
sensor` in **Heading sensor**
parameter.

### **3-Wire Expander (smart port)** — Select the smart port that is used by 3-Wire Expander `None` (default) | `1` to `21`

If you are using a 3-Wire Expander, specify the smart port on
VEX EDR V5 Robot Brain to which the expander is
connected.

#### Dependencies

To enable this parameter, select
`Gyroscope` in **Heading
sensor** parameter.

### **Port** — Set the port for gyroscope A (default) | `A` to `H`

Select the port on the robot to which the block is connected.

#### Dependencies

To enable this parameter, select
`Gyroscope` in **Heading
sensor** parameter.

### **Gyroscope scale factor** — Scale factor for gyroscope 1.34 (default) | any positive value

Set the scale factor value for the gyroscope. For more information
see, Monitoring Signals for Gyroscope Calibration Using the VEX V5 Touch Screen

**Data Types:** `double`

### **Mounted direction** — Gyroscope orientation Z-axis downwards (default) | Z-axis upwards

Specify how the gyroscope is mounted. This parameter indicates the
orientation of the gyroscope.

### Controller parameters

**Distance**

### **Drive speed (m/s)** — Set the drive speed 0.3 (default) | positive scalar

Set the linear speed of the robot in meters per second.

### **Deadband (m)** — set the deadband distance 0,04 (default) | any positive scalar

Set the deadband in meters. This parameter sets the accuracy of
position control. The robot stops once the distance error (between
current and reference position) falls below deadband value.

Setting a very low value might destabilize the robot motion.

### **Hysteresis (m)** — set the hysteresis distance 0.01 (default) | positive scalar

Set the hysteresis distance in meters. As the robot uses an on-off
type controller, the motor speeds may switch many times when the robot
is near target. Hysteresis prevents the controller from switching too
much.

**Angle**

### **Turn rate (dps)** — set the angular speed 50 (default) | positive scalar

Set the angular speed or turn rate of the robot.

### **Deadband (deg)** — set the deadband angle 4 (default) | positive scalar

Set the accuracy of angle control.

Since, heading angle is controlled even when the robot moves towards
reference position, setting a low deadband can lead to oscillatory
movement. Setting a high Deadband can compromise angle accuracy.

### **Hysteresis (deg)** — set the hysteresis angle 5 (default) | positive scalar

Set the hysteresis angle in degrees. Since the robot uses an on-off
type heading controller, motor may switch on and off many times.
Hysteresis prevents the controller from switching on-off too
much.

### Sample time

### **Sample time** — Discrete interval between samples `0.02` (default) | -1 | positive scalar

Specify a sample time by entering a positive scalar value, such as
0.1. The discrete sample time of -1 means that the block inherits its
sample time from upstream blocks.

If you set the sample time to a high value, robot motion might not be
stable.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Drivetrain

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Set up differential drive and control robot pose

Use the Differential (Tank) Drive block to control pose (position and
heading) of VEX® V5 robot drivetrain.

Provide the position and final heading waypoints as input to move the robot to the
specified position and turn it toward the final heading.

This block also allows you configure drive parameters such as track width or wheel
size and change controller parameters such as drive speed and accuracy.

This block requires Stateflow® license.

**Note**

To study or modify the block algorithm, click anywhere in the block. On the
**Block** tab that appears on the Simulink toolstrip, click
**Disable Link**, and then click **Look inside
mask**.
