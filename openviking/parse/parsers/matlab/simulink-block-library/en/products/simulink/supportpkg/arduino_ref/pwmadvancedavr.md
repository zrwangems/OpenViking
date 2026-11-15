---
type: simulink-block
title: 'PWM AVR'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'pwmadvancedavr'
documentation_source_path: 'supportpkg/arduino_ref/pwmadvancedavr.html'
language: en
---

# PWM AVR

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
  80% and power of 0.8 (204/255).
- Sending out-of-range values, such as `500` or
  `-500`, to the block input port has the same effect as
  sending the maximum or minimum input values, respectively.

The block input port inherits the data type of the upstream block, and internally
converts the data to the `uint8` data type.

**Data Types:** `uint8`

## Parameters

### **Pin number** — PWM pin number `9` (default) | scalar

Specify the Arduino hardware board pin number to which the PWM input signal is connected.
Click **View pin map** to open the Arduino pin mapping table. For more information on how to assign pins or view the
pins for the PWM block, see Pin Mapping for Arduino Timer-Dependent Blocks.

**Note**

Do not assign the same pin number to multiple blocks within a model.

### **Frequency** — Specify PWM frequency Read-only: `Specify` (default)

This parameter is read-only.

This read-only parameter is set to `Specify`. You can
specify the frequency of the PWM signal in the **Desired(Hz)**
parameter.

### **Desired (Hz)** — Desired PWM output frequency `490.2` (default) | scalar

Specify the desired output frequency of the PWM signal.

### **Achievable (Hz)** — Achievable PWM output frequency by Arduino board Read-only: scalar

This parameter is read-only.

The block generates the PWM signals with the frequency that is closest to the
frequency specified in the **Desired(Hz)** parameter. This is a
read-only parameter.

### **Enable compare match (MCx) interrupt** — Option to generate interrupt at compare match `off` (default) | `on`

Select this option to generate an interrupt at each compare match of the Arduino timer.

**Note**

Select an appropriate interrupt handler in the Interrupt name parameter of
the Hardware
Interrupt block to generate an interrupt at each timer compare
match.

### **Enable overflow/underflow (OVF) interrupt** — Option to generate interrupt at timer/counter overflow/underflow `off` (default) | `on`

Select this option to generate an interrupt when the timer/counter reaches the
maximum value (TOP) during up counting and when the timer/counter reaches the minimum
value (ZERO) during down counting. For dual-slope mode of the timer/counter operation,
TOP value is defined by the period (PER) register value.

**Note**

Configure the same interrupt handler in this parameter as in the Interrupt name parameter of
the Hardware
Interrupt block as in the PWM block.

## Libraries

Simulink Support Package for Arduino Hardware / Advanced / AVR

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Generate pulse width modulated signal on analog output pin of Arduino AVR core

Use the PWM block to generate square pulses of varying duty cycle on the
Arduino® AVR hardware pin.

**Note**

The PWM block supports C/C++ code generation. This feature allows you
to generate C and C++ code using Embedded Coder®.

### Supported Arduino Boards

- Arduino Uno
- Arduino Mega 2560
- Arduino Mega ADK
- Arduino Leonardo
- Arduino Micro
