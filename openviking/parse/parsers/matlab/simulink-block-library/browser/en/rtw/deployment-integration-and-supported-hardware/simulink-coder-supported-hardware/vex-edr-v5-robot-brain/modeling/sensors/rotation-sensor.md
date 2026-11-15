---
type: simulink-block
title: 'Rotation Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'rotationsensor'
documentation_source_path: 'vexv5/ref/rotationsensor.html'
language: en
---

# Rotation Sensor

## Ports

### Output

### **Position** — Shaft rotational position vector

This port represents the rotational position of the shaft in degrees.
The rotational position value ranges from `-inf` to
`inf`.

**Data Types:** `double`

### **Velocity** — Shaft velocity vector

The **Velocity** port outputs shaft velocity in
degrees per second.

**Data Types:** `double`

## Parameters

### **Smart Port** — Smart Port to which VEX V5 Rotation Sensor is connected 1 (default) | `1` to `21`

Select the smart port on the V5 robot to which the VEX V5 Rotation sensor
is connected. There are 21 smart ports on the V5 robot.

### **Reset mode** — Option to reset the Rotation Sensor reading `No reset` (default) | `Reset by each sample time` | `Reset by external signal`

Specify the option to reset the rotation sensor reading.

- `No reset` – The block does not reset the
  Rotation sensor reading and outputs the total angle of
  rotation.

  For example, at T = 1 in the table the Rotation sensor rotates 20
  degrees in a counterclockwise direction,so, the output is 20.
- `Reset at each sample time`  – For each
  sample period, the block outputs the rotation sensor reading, and
  then resets it to 0.

  For example, in the table, at T = 1, the rotation sensor rotates
  20 degrees in a counterclockwise direction, and therefore, the
  output is 20.

  Between T = 1 and T = 2, the rotation sensor rotates 10 degrees in
  a counterclockwise direction, and therefore, the output is
  10.

  If you reset the rotation sensor in this way, it retains the
  offset for the current program execution. It might require a reset
  after restarting the program. If you want to preserve the zero
  offset, select **Set Zero** on VEX V5 Brain’s User
  Interface. For more information, see Using VEX V5 Rotation Sensor.
- `Reset by external signal`  – The
  Rotation sensor reading is reset to 0 based on the input value to
  `Rst` port. When you send a value other than 0
  to the block input, the Rotation sensor reading is reset to 0. For
  each sample period, the block outputs the Rotation sensor reading
  since the last reset.

  Reset mode

### **Sample time** — Interval to read values from sensor `0.2` (default) | positive scalar | `-1`

Specify the sample time in seconds to determine how often the block reads
values from the sensor. When you specify this parameter as
`-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Read shaft position and velocity

The Rotation Sensor block reads shaft's position and velocity from the
Rotation sensor that is connected to the VEX® V5 Brain. The VEX V5 Rotation sensor is an absolute encoder and it retains
the shaft orientation across power cycle.
