---
type: simulink-block
title: 'Analog Input'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / System Core'
documentation_page: 'analoginput'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/analoginput.html'
language: en
---

# Analog Input

## Ports

### Output

### **Port\_1** — Voltage of analog input pin scalar

If the measured voltage equals the ground voltage, the block emits
`0`. If the measured voltage equals the analog
reference voltage, the block emits `1`.

## Parameters

### **Pin** — Pin name of the analog input

Specify the digital pin.

To open the pin mapping table, click **View pin
map**.

Make sure to assign different pin name to the different blocks of your
model.

Apart from the pins names mentioned in the pin mapping table, there are
other alternate pin names `(Px_y_ALTz)` that can be used to
access other hardware peripherals connected to the same pin.

The alternate pin names are only applicable for Simulink®
Coder™ Support Package for STMicroelectronics® Nucleo Boards and Discovery boards.

### **Sample time** — Frequency at which the block reads the input pin value -1 (default)

Specify how often this block measures the voltage of the analog input pin,
in seconds.

When you specify this parameter as`-1`, Simulink determines the best sample time for the block based on the
block context within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Measure voltage of analog input pin

The Analog Input block measures the voltage of an analog pin relative
to the analog input reference voltage on the hardware. The block outputs the measurement
as a float value in the range 0–1.

- If the measured voltage equals the ground voltage, the block emits
  `0`.
- If the measured voltage equals the analog reference voltage, the block emits
  `1`.

During the external mode simulation, the block outputs the simulation results returned
from the executable running on the target hardware.

During simulation in all other modes, the block outputs zeroes.
