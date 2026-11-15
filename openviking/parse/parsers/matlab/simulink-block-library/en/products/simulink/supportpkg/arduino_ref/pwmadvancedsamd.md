---
type: simulink-block
title: 'PWM SAMD'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'pwmadvancedsamd'
documentation_source_path: 'supportpkg/arduino_ref/pwmadvancedsamd.html'
language: en
---

# PWM SAMD

## Ports

### Input

### **Data** — Input value that determines width of square pulses positive integer in the range [0, 255]

The value at the block input port determines the width of the square wave, called
*duty-cycle*, that the Arduino hardware outputs on the specified PWM pin.

For example:

- Sending the maximum value, `255`, to the block input port
  produces a duty cycle of 100%, which results in full power at the PWM
  pin.
- Sending the minimum value, `0`, to the block input port
  produces a duty cycle of 0%, which results in no power at the PWM pin.
- Sending an intermediate value to the block input port produces a
  proportional duty cycle and power output at the PWM pin. For example, sending a
  value of `204` to the block input port produces a duty cycle of
  80%, and power (204/255 = 0.8).
- Sending out-of-range values, such as `500` or
  `-500`, to the block input port has the same effect as
  sending the maximum or minimum input values, respectively.

The block input port inherits the data type of the upstream block, and internally
converts the data to the `uint8` data type.

**Data Types:** `uint8`

## Parameters

### **Pin number** — PWM pin number `5` (default) | scalar

Specify the Arduino hardware board pin number to which the PWM input signal is connected.
Click **View pin map** to open the Arduino pin mapping table. For more information on how to assign pins or view the
pins for the PWM block, see Pin Mapping for Arduino Timer-Dependent Blocks.

**Note**

Do not assign the same pin number to multiple blocks within a model.

### **Frequency** — PWM output frequency `Specify` (default)

This read-only parameter displays the output frequency of the PWM signal.

### **Desired (Hz)** — Desired PWM output frequency `490.2` (default) | scalar

Specify the desired output frequency of the PWM signal.

### **Achievable (Hz)** — Achievable PWM output frequency by Arduino board scalar

The block generates the PWM signals with the frequency that is closest to the
frequency specified in the **Desired(Hz)** parameter.

### **Wave generation mode** — Timer/Counter wave generation mode `Dual-slope, interrupt/event at TOP (DSTOP)` (default) | `Dual-slope, interrupt/event at ZERO (DSBOTTOM)` | `Dual-slope, interrupt/event at TOP and ZERO (DSBOTH)`

Select one of these options to determine when the block generates a dual-slope timer waveform.

- `Dual-slope, interrupt/event at TOP (DSTOP)` — The
  block generates the PWM interrupt/event when the timer/counter value reaches the
  maximum value.
- `Dual-slope, interrupt/event at ZERO (DSBOTTOM)` —
  The block generates the PWM interrupt/event when the timer/counter value reaches
  the minimum value.
- `Dual-slope, interrupt/event at TOP and ZERO
  (DSBOTH)` — The block generates the PWM interrupt/event when the
  timer/counter value reaches both, the maximum and the minimum value.

### **Enable compare match (MCx) interrupt** — Enable timer/counter match or compare interrupt `off` (default) | `on`

Select this option to generate an interrupt at each compare match of the Arduino timer.

### **Enable overflow/underflow (OVF) interrupt** — Enable timer/counter overflow/underflow interrupt `on` (default) | `off`

Select this option to generate an interrupt when the timer/counter reaches the
maximum value (TOP) during up counting and when the timer/counter reaches the minimum
value (ZERO) during down counting. For dual-slope mode of timer/counter operation, TOP
value is defined by the Period (PER) register value.

### **Invert output polarity** — Invert polarity of PWM output waveform `off` (default) | `on`

Select this option to invert the polarity of the PWM block output
waveform.

## Libraries

Simulink Support Package for Arduino Hardware / Advanced / SAMD

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Generate pulse width modulated signal on analog output pin of Arduino SAMD21 core

Use the PWM block to generate square pulses of varying duty cycle on the
Arduino® SAMD 21 hardware pin.

**Note**

The PWM block supports C/C++ code generation. This feature allows you
to generate C and C++ code using Embedded Coder®.

### Supported Arduino Boards

- Arduino MKR 1000
- Arduino MKR ZERO
- Arduino MKR Wi-Fi® 1010
- Arduino Nano 33 IoT
