---
type: simulink-block
title: 'Gyroscope'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'gyroscope'
documentation_source_path: 'vexv5/ref/gyroscope.html'
language: en
---

# Gyroscope

## Ports

### Output

### **Port\_1** — Yaw rotation since last start or reset degrees

The yaw rotation along the axis of the gyroscope sensor, in degrees. When you
rotate the gyroscope sensor in a clockwise direction, the value increases. When you
rotate the gyroscope in a counterclockwise direction, the value decreases.

**Data Types:** `double`

## Parameters

### **3-Wire Expander (smart port)** — Select the smart port that is used by 3-Wire Expander `None` (default) | `1` to `21`

If you are using a 3-Wire Expander, specify the smart port on VEX® EDR V5 Robot Brain to which the expander is connected.

### **Port** — 3-wire port to which the gyroscope is connected A (default) | `B` | `C` | `D` | `E` | `F` | `G` | `H`

Select the 3-wire port of VEX V5 Robot Brain to which the gyroscope is
connected.

### **Reset mode** — Reset mode for resetting the gyroscope sensor reading `No reset` (default) | `Reset at each sample time` | `Reset by external signal`

- In the example table, assume that the block sample time is 1 second. The
  rotation angle at time instant T = 0 is 0 degrees.

  The different reset modes that this block supports are:

  - `No reset` – The gyroscope reading is not reset and
    the block outputs the total angle of rotation.

    For example, in the table, at T = 1, the gyroscope sensor rotates 20 degrees
    in a counterclockwise direction, and therefore, the output is 20.

    Between T = 1 and T = 2, the gyroscope sensor rotates 10 degrees in a
    counterclockwise direction. Therefore, the yaw rotation is 30 at T = 2 (20 from
    T = 1 and 10 from T = 2).

    In this reset mode, the output at any time instant is a cumulative sum of
    the previous yaw rotation and the current yaw rotation.
  - `Reset at each sample time`  – For each sample
    period, the block outputs the gyroscope reading, and then resets it to 0.

    For example, in the table, at T = 1, the gyroscope sensor rotates 20 degrees
    in a counterclockwise direction, and therefore, the output is 20.

    Between T = 1 and T = 2, the gyroscope sensor rotates 10 degrees in a
    counterclockwise direction, and therefore, the output is 10.

    In this reset mode, the output is the yaw rotation at a particular time
    instant.
  - `Reset by external signal`  – The gyroscope reading
    is reset to 0 based on the input value to `Rst` port. When you
    send a value other than 0 to the block input, the gyroscope reading is reset to
    0. For each sample period, the block outputs the gyroscope reading since the
    last reset.

    For example, in the table, when the external signal is 0, the output is
    calculated the same as in the `No reset` mode. When the
    external signal is nonzero, the output is calculated the same as in the
    `Reset at each sample time` mode.

### **Sample time** — Interval at which the block reads values `0.2` (default) | positive scalar | -1

Enter the time interval at which the block reads values from the gyroscope.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model. If you select `Reset by external signal`
option in **Reset mode** parameter, the **Sample
time** parameter is hidden and the value is inherited (Sample time =
-1).

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Represent connected gyroscope and measure yaw angle

The Gyroscope block represents a gyroscope connected to the 3-wire port of
VEX V5 Robot brain, and measures the angle (in degrees) along the yaw axis of the gyroscope
sensor.

The block outputs angle in degrees as a double-precision scalar value. When you rotate the
gyroscope sensor in a clockwise direction, the angular increases. When you rotate the sensor
in a counterclockwise direction, the value decreases.

While starting the program, do not move the robot for a couple of seconds for proper
initialization of Gyroscope.
