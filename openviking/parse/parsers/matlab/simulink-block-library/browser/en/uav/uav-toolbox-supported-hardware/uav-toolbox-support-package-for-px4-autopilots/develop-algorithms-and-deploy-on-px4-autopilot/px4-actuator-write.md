---
type: simulink-block
title: 'PX4 Actuator Write'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4actuatorwrite'
documentation_source_path: 'px4/ref/px4actuatorwrite.html'
language: en
---

# PX4 Actuator Write

## Ports

### Input

### **Arm** — Arm PX4® flight controller `0` | `1`

Enable signal for arming the flight actuators.

A value of `0` indicates that the flight actuator is not
armed, whereas a value of `1` indicates that the flight
actuator is armed.

**Data Types:** `Boolean`

### **Motor *`x`*** — Inputs that accept motor values `[-1,1]`

Connect the Motor `x` inputs to signals that represent
single scalar values.

If you provide an input greater than `1` or less than
`-1`, the block internally clips it to `1`
and `-1`, respectively.

#### Dependencies

To enable these ports, select the required number of motors
`(1-12)` from the **Motors**
parameter.

**Data Types:** `single`

### **Servo *`x`*** — Input that accept servo values `[-1,1]`

Connect the Servo `x` inputs to signals that represent
single scalar values.

If you provide an input greater than `1` or less than
`-1`, the block internally clips it to `1`
and `-1`, respectively.

#### Dependencies

To enable these ports, select the required number of servos
`(1-8)` from the **Servos**
parameter.

**Data Types:** `single`

### **Motor Values** — Input that accept motor values as an array `-1` | `1`

Connect the `Motor Values` inputs to signals that represent
values as an array.

An input value of `1` indicates maximum output, a value of
`0` sets the motors to their lowest possible thrust, and an
input of `-1` stops the motor.

#### Dependencies

To enable this port, select **Input Motor Values as an
array** parameter.

**Data Types:** `single`

### **Servo Values** — Input that accept servo values as an array `-1` | `1`

Connect the `Servo Values` inputs to signals that represent
values as an array.

An input value of `1` indicates maximum output, a value of
`0` centers the servos, and an input of
`-1` indicates the maximum output in the reverse direction.

#### Dependencies

To enable this port, select **Input Servo Values as an
array** parameter.

**Data Types:** `single`

## Parameters

#### Motors tab

### **Motors** — Motors to write values to Motor numbers

Select the motor numbers to which you want to send the single scalar values.
The number of **Motor** input ports on the block depends on the number of
motors you select in this parameter.

### **Input Motor Values as an array** — Option to specify motor values as an array `off` (default) | `on`

Select this parameter to enable the **Motor Values** input
port.

You can input the motor values as an array of size
`1-by-12`.

#### Servos tab

### **Servos** — Servos to write values to Servo numbers

Select the servo numbers to which you want to send the single scalar values.
The number of **Servo** input ports on the block depends on the number of
servos you select in this parameter.

### **Input Servo Values as an array** — Option to specify servo values as an array `off` (default) | `on`

Select this parameter to enable the **Servo Values** input
port.

You can input the servo values as an array of size
`1-by-8`.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Peripheral Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Set actuator values for motors and servos

The PX4 Actuator Write block writes motor and servo actuator values over
the PWM and UAVCAN interfaces. The PX4 Actuator Write block accepts single
scalar values between `-1` to `1` as input and writes
those values to the selected motors or servos using `ActuatorTest` uORB
topic.

An input value of `1` indicates maximum output, a value of
`0` centers the servos or sets the motors to their lowest possible
thrust, and an input of `-1` indicates the maximum output but in the
reverse direction. However, for motors that do not support reverse operation, any value
less than zero stops the motor.

Setting the **Arm** input to `true` value arms the actuators,
while false serves as a kill switch and disarms the actuators.

**Configure Actuators**

For firmware version 1.14, you must configure the PWM & AUX pins in QGroundControl
before using the PX4 Actuator Write block in Simulink. To configure the
pins, you must use QGroundControl version 4.3.0, which can be downloaded from this
location. For information on configuring the actuators, see Configure and Assign Actuators in QGC.
