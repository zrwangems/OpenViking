---
type: simulink-block
title: 'Digital Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Basic'
documentation_page: 'digitalwrite'
documentation_source_path: 'microbit/ref/digitalwrite.html'
language: en
---

# Digital Write

## Ports

### Input

### **Port\_1** — Input signal scalar

The block sets this value to the digital output pin that you specify
in the **Pin** parameter.

## Parameters

### **Pin** — Pin number of the digital output

Specify the digital pin.

To open the pin mapping table, click **View pin
map**.

Make sure not to assign the same pin name to multiple blocks within your
model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Set logical state of digital output pin

The Digital Write block sets the logical state of the specified digital
pin on the board.

During the external mode simulation, the block sets the value to the pin that you
specify in the **Pin** parameter.

During simulation in all other modes, the block does nothing.
