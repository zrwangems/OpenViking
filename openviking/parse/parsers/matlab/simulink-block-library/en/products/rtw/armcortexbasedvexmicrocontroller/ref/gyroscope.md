---
type: simulink-block
title: 'Gyroscope'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'gyroscope'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/gyroscope.html'
language: en
---

# Gyroscope

## Ports

### Input

### **Rst** — Reset mode scalar

When you set the **Reset mode** parameter to `Reset
by external signal`, the `Rst` port becomes
available.

The block output is reset to 0 based on the input value at this
port. When you send a value other than 0 to the block input, the block
output is reset to 0. For each sample period, the block outputs the
gyroscope reading since the last reset.

When the external signal is 0, the output is calculated the
same as in the `No reset` mode. When the
external signal is nonzero, the output is calculated the same as in
the `Reset at each sample time` mode. For
more information on the reset modes, see the **Reset mode** parameter
description.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Sim** — Gyroscope reading for simulation purpose scalar

When you select the **Add input port for simulation** parameter,
the `Sim` port becomes available.

For the simulation behavior, provide the gyroscope reading from
this port via a source block

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Port\_1** — Yaw rotation since last start or reset scalar

The yaw rotation along the axis of the gyroscope sensor, in
degrees. When you rotate the gyroscope sensor in a clockwise direction,
the tick count decreases. When you rotate the encoder in a counterclockwise
direction, the tick count increases.

**Data Types:** `double`

## Parameters

### **Analog port** — Analog port number `1` (default) | `2` | `3` | `4` | `5` | `6` | `7` | `8`

Select the analog port number on the microcontroller to which
the gyroscope sensor is connected.

### **Calibration multiplier** — Constant to adjust the block readings `196` (default) | `Any value between 0 and 65535`

Specify a value to remove positive or negative bias in the output
of the block readings. To calibrate the sensor, try different ranges
until an acceptable range of accuracy is achieved.

When the gyroscope reading is greater than the actual rotation,
decrease the **Calibration multiplier** value. When
the gyroscope reading is less than the actual rotation, increase the **Calibration
multiplier** value.

### **Reset mode** — Reset mode for resetting the gyroscope sensor reading `No reset` (default) | `Reset at each sample time` | `Reset by external signal`

- In the example table, assume that the block sample
  time is 1 second. The rotation angle at time instant T = 0 is 0 degrees.

  The different reset modes that this block supports are:

  - `No reset` – The gyroscope
    reading is not reset and the block outputs the total angle of rotation.

    For example, in the table, at T = 1, the gyroscope sensor rotates
    20 degrees in a counterclockwise direction, and therefore, the output
    is 20.

    Between T = 1 and T = 2, the gyroscope sensor rotates 10 degrees
    in a counterclockwise direction. Therefore, the yaw rotation is 30
    at T = 2 (20 from T = 1 and 10 from T = 2).

    In this reset mode, the output at any time instant is a cumulative
    sum of the previous yaw rotation and the current yaw rotation.
  - `Reset at each sample time`  –
    For each sample period, the block outputs the gyroscope reading, and
    then resets it to 0.

    For example, in the table, at T = 1, the gyroscope sensor rotates
    20 degrees in a counterclockwise direction, and therefore, the output
    is 20.

    Between T = 1 and T = 2, the gyroscope sensor rotates 10 degrees
    in a counterclockwise direction, and therefore, the output is 10.

    In this reset mode, the output is the yaw rotation at a particular
    time instant.
  - `Reset by external signal`  –
    The gyroscope reading is reset to 0 based on the input value to `Rst` port.
    When you send a value other than 0 to the block input, the gyroscope
    reading is reset to 0. For each sample period, the block outputs the
    gyroscope reading since the last reset.

    For example, in the table, when the external signal is 0, the
    output is calculated the same as in the `No reset` mode.
    When the external signal is nonzero, the output is calculated the
    same as in the `Reset at each sample time` mode.

### **Add input port for simulation** — Specify if you want to run a normal mode simulation off (default) | on

If you want the normal mode simulation with a source block providing
the input value, select this parameter.

### **Sample time** — Specify how often the block reads the rotation `0.2` (default)

Specify how often the block reads the rotation, in seconds.

#### Dependencies

If you set the **Reset mode** parameter to `Reset
by external signal` or select the **Add input
port for simulation** parameter, the **Sample time** parameter
is hidden and the value is inherited (Sample time = -1).

## Libraries

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller/Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Measure yaw rotation in degrees

The Gyroscope block measures the angle of rotation
(yaw) along the single axis of the gyroscope sensor. In the graphic,
the arrow above the vertical axis indicates yaw. The direction of
the arrow shows the positive direction of the reading for the gyroscope
sensor.

The block outputs angle (in degrees) as a double-precision scalar
value. When you rotate the gyroscope sensor in a clockwise direction,
the tick count decreases. When you rotate the encoder in a counterclockwise
direction, the tick count increases.

Using the **Calibration multiplier** parameter, calibrate the
gyroscope and reduce drifts in the gyroscope sensor readings. Drifts are positive or
negative bias introduced in the readings due to the external factors such as
temperature, mechanical vibration, and motor magnetic field influence. A calibrated
sensor helps you reduce drifts and obtain an acceptable range of accuracy in the
readings from the sensor. To learn how to calibrate the gyroscope sensor, see Turn Robot Using LCD Button Press and Display Gyroscope Reading on LCD Screen.

During simulations, without the hardware, this block emits zeros if there is no source block
connected to the simulation input port. See Block Produces Zeros or Does Nothing in Simulation. To achieve simulation
behavior, connect a source block from the Utilities library in VEX microcontroller
library.

During code generation, any simulation block that is connected
to the input port of the Gyroscope block is ignored
and has no effect on the generated code.

For the code generated from this block to work properly with
the gyroscope sensor, connect a VEX 7.2 volt battery to the microcontroller.
Before you download the program to the VEX microcontroller, turn on
the battery. After turning on the battery, do not move the robot on
which the gyroscope sensor is mounted for proper initialization of
the gyroscope.
