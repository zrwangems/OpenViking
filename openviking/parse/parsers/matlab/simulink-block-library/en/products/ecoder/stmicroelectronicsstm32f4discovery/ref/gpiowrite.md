---
type: simulink-block
title: 'GPIO Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'gpiowrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/gpiowrite.html'
language: en
---

# GPIO Write

## Ports

### Input

### **Port\_1** — Set the GPIO pin status scalar

The input port to set the GPIO pin status.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **GPIO port** — GPIO port to set the GPIO pin status GPIOA (default) | GPIOA | GPIOB | GPIOC | GPIOD | GPIOE | GPIOF | GPIOG | GPIOH | GPIOI

Select one of GPIOA to GPIOI ports to set a GPIO pin status.

### **Pin number** — GPIO port to set the GPIO pin status 1 (default)

Select a GPIO pin to write the logical status.

### **Initially set GPIO pin** — Option to set the GPIO pin status during model initialization off (default) | on

Select this option to set the GPIO pin status during model initialization.

### **Toggle pin when input is true** — Option to enable GPIO pin toggling when the input is true off (default) | on

Select this option to enable GPIO pin toggling when the input
is ‘true’.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4-Discovery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Set GPIO pin status

Set the logical value of a digital pin of the STM32F4 -Discovery™ board.
