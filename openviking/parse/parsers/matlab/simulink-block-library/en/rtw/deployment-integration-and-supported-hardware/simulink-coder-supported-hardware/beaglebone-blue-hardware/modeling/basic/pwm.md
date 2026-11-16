---
type: simulink-block
title: 'PWM'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'pwm'
documentation_source_path: 'beagleboneblue/ref/pwm.html'
language: en
---

# PWM

## Ports

### Input

### **Port\_1** — Duty cycle value scalar

The range of valid input is `0 - 100`. The input controls the
duty cycle of the square waveform. An input value of `0` sets the
duty cycle to 0% or no power, while an input value of `100` sets the
duty cycle to 100% or full power. An intermediate input value, such as
`0.333`, sets the duty cycle to 33.3%, or 1/3 power. An
out-of-range input value, such as `-0.2` or `1.2`,
outputs minimum or maximum power.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Pin** — Select the digital output pin GPS\_HEADER\_PIN\_3 (default) | GPS\_HEADER\_PIN\_4

Specify the digital output at which the block generates the PWM signal.

To view the pin mapping on the board, click **View pin
map**.

Each block must have a unique pin number within a model.

### **Frequency** — Frequency of the PWM signal 2000 (default)

Set the frequency of the PWM signal. If there are two PWM blocks, set both the
blocks to the same frequency.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Pulse width modulation of digital output pin

The PWM block varies the power output of a digital output pin. The input value sets the
percentage of time that the digital square-wave is on within a specific period. This time
percentage is called duty cycle.
