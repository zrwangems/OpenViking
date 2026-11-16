---
type: simulink-block
title: 'PWM'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'pwm'
documentation_source_path: 'beaglebone/ref/pwm.html'
language: en
---

# PWM

## Ports

### Input

### **Port\_1** — Input value that determines width of square pulses positive scalar in the range [`0`, `1`]

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

### **Pin** — PWM pin number `P9_21` (default) | `P9_34` | `P9_36` | `P9_45` | `P9_46` | `P9_13` | `P9_19` | `P9_42` | `P9_29` | `P9_31` | `P9_22` | `P9_28` | `P9_14` | `P9_16`

Select the BeagleBone® hardware board pin number to which the PWM input signal is connected. To
open the pin map of the BeagleBone board, click **View pin map**.

**Note**

Do not assign the same pin number to multiple blocks within a model.

### **Frequency (Hz)** — PWM output frequency 2000 (default) | nonnegative scalar

Set the frequency of the PWM signal. If there are two PWM blocks, set both the
blocks to the same frequency.

### **Polarity** — PWM signal polarity `Positive` (default) | `Negative`

Set the polarity of the PWM signal.

- `Positive` — Select this value to set the digital
  pulse high (ON) for the duty-cycle, and OFF for the remainder of the
  period.
- `Negative` — Select this value to set the digital
  pulse low (OFF) for the duty-cycle, and ON for the remainder of the period.

## Libraries

Embedded Coder Support Package for BeagleBone Black Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Pulse width modulation of digital output pin

Use the PWM block to vary the power output of a digital output pin. This
block enables a digital output to provide a range of different power levels, similar to that
of an analog output.

During simulations without the hardware, this block does nothing. See Block Produces Zeros or Does Nothing in Simulation.
