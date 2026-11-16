---
type: simulink-block
title: 'PWM Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'pwmoutput'
documentation_source_path: 'nucleo/ref/pwmoutput.html'
language: en
---

# PWM Output

## Ports

### Input

### **Port\_1** — Duty cycle value scalar

The range of valid input values is
`0``–100`. The input controls the
duty cycle (width of the square wave) of the square waveform.

An input value of `0` produces a 0% duty cycle and an
input value of `100` produces a 100% duty cycle. Any
out-of-range values, such as `500` or
`-500`, at the block input port has the same effect
as the maximum or minimum input values.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Pin** — Pin at which the block generates the PWM signal

To view the pin mapping on the board, click **View pin
map**.

Make sure to assign different pin name to the different blocks of your
model.

Apart from the pins names mentioned in the pin mapping table, there are
other alternate pin names `(Px_y_ALTz)` that can be used to
access other hardware peripheral devices connected to the same pin. To know
more, refer to Usage of Alternate Pin Names.

The alternate pin names are only applicable for Simulink®
Coder™ Support Package for STMicroelectronics® Nucleo Boards and Discovery boards.

### **Initial frequency (Hz)** — Initial frequency of the PWM waveform `2000` (default)

Specify the initial frequency of the PWM waveform.

### **Initial duty cycle (0 - 100)** — Initial width of the square wave on PWM pin `50` (default) | `integer between 0 and 100`

Specify the initial duty cycle between
`0`–`100`.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Generate square wave on the specified output pin

The PWM Output block generates square waveform on the specified output pin. The block
input controls the duty cycle of the square waveform. You can provide a value between
`0`–`100` as the block input. An input value of 0
produces a 0 percent duty cycle and an input value of 100 produces a 100 percent duty
cycle
