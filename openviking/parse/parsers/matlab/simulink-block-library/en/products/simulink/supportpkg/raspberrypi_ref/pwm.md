---
type: simulink-block
title: 'PWM'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'pwm'
documentation_source_path: 'supportpkg/raspberrypi_ref/pwm.html'
language: en
---

# PWM

## Ports

### Input

### **In** — Input value that determines width of square pulses positive scalar in the range [`0`, `1`]

The block input inherits the data type of the upstream block, and internally
converts it to double. The value sent to the block input determines the width of the
square wave, called *duty-cycle*, that the
Raspberry Pi® hardware outputs on the specified PWM pin. The block input accepts a
range of values from `0` to `1` (from 0% to 100% of
the duty cycle).

For example:

- The maximum input value, `1`, sets the duty cycle to 100%, or
  full power.
- The minimum input value, `0`, sets the duty cycle to 0%, or
  no power.
- An intermediate input value, such as `0.333`, sets the duty
  cycle to 33.3%, or 1/3 power.
- Out of range input values, such as `-0.2` or
  `1.2`, output minimum or maximum power.

**Data Types:** `double`

## Parameters

### **Board** — Raspberry Pi hardware board `Pi 4 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

Select your Raspberry Pi hardware board. You can find this information on the target hardware,
product packaging, or product documentation.

### **Pin** — PWM pin number `21` (default) | `4` | `17` | `27` | `22` | `10` | `9` | `11` | `14` | `15` | `18` | `23` | `24` | `25` | `8` | `7` | `5` | `6` | `12` | `13` | `19` | `16` | `26` | `20` | `21`

Select the Raspberry Pi hardware board pin number to which the PWM input signal is connected. To
open the pin map of the Raspberry Pi board, click **View pin map**.

**Note**

Do not assign the same pin number to multiple blocks within a model.

### **Frequency** — PWM output frequency `500` (default) | `8000` | `4000` | `2000` | `1600` | `1000` | `800` | `400` | `320` | `250` | `200` | `160` | `100` | `80` | `50` | `40` | `20` | `10`

Select the output frequency of the PWM signal.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Generate pulse width modulated signal of digital output pin

Use the PWM block to vary the power output of a digital output pin. This
block enables a digital output to provide a range of different power levels, similar to that
of an analog output.

During simulations without the hardware, this block does nothing. See Block Produces Zeros or Does Nothing in Simulation.
