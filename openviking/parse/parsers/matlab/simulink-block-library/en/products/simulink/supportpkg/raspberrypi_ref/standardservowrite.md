---
type: simulink-block
title: 'Standard Servo Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'standardservowrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/standardservowrite.html'
language: en
---

# Standard Servo Write

## Ports

### Input

### **Data** — Input value that determines speed and direction of standard rotation servo motor positive integer in the range [`0`, `255`]

The value sent to the block at the input port determines the speed and direction
of rotation of the standard rotation servo motor interfaced with the Raspberry Pi hardware board. For example:

- An input value of `0` positions the shaft at
  `0` degrees.
- An input value of `180` positions the shaft at
  `180` degrees.
- Any input value between the [`0`, `180`]
  range, for example `50`, positions the shaft at
  `50` degrees.
- Any input value out of the [`0`, `180`]
  range, for example `-2` or `188`, positions
  the shaft at `0` and `180`,
  respectively.

**Data Types:** `double`

## Parameters

### **Board** — Raspberry Pi hardware board `Pi 4 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

Select your Raspberry Pi hardware board. You can find this information on the target hardware,
product packaging, or product documentation.

### **Pin** — Standard servo write pin number `18` (default) | `4` | `17` | `27` | `22` | `10` | `9` | `11` | `14` | `15` | `21` | `23` | `24` | `25` | `8` | `7` | `5` | `6` | `12` | `13` | `19` | `16` | `26` | `20` | `21`

Select the Raspberry Pi hardware board pin number to which the standard rotation servo write motor
input signal is connected. To open the pin map of the Raspberry Pi board, click **View pin map**.

**Note**

Do not assign the same pin number to multiple blocks within a model.

### **Minimum pulse duration** — Minimum pulse duration of servo signal `1000e-6` (default) | positive scalar

Set the minimum pulse duration of the servo signal in seconds.

### **Maximum pulse duration** — Maximum pulse duration of servo signal `2000e-6` (default) | positive scalar

Set the maximum pulse duration of the servo signal in seconds.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Set shaft position of standard servo motor to angle specified in degrees

Use the Standard Servo Write block to control the shaft angle of a servo
motor attached to a pulse width modulation (PWM) output pin on the Raspberry Pi® hardware board.

During simulations without the hardware, this block does nothing. See Block Produces Zeros or Does Nothing in Simulation.
