---
type: simulink-block
title: 'Digital Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / System Core'
documentation_page: 'digitalread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/digitalread.html'
language: en
---

# Digital Read

## Ports

### Output

### **Port\_1** — Output signal scalar

The port outputs the logical state of the digital pin on the board
that you specify in the **Pin** parameter.

## Parameters

### **Pin** — Pin number of the digital input

Specify the digital pin.

To open the pin mapping table, click **View pin
map**.

Make sure to assign different pin name to the different blocks of your
model.

### **Sample time** — Frequency at which the block reads the input pin value `-1` (default)

Specify in seconds how often this block reads the pin value.

When you specify this parameter as`-1`, Simulink®
determines the best sample time for the block based on the block context
within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Read logical state of digital input pin

The Digital Read block outputs the logical state of a specified digital
pin on the board.

During the external mode simulation, the block outputs the simulation results returned
from the executable running on the target hardware.

During simulation in all other modes, the block outputs zeroes.
