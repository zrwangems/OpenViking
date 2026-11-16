---
type: simulink-block
title: 'GPIO Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'gpioread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/gpioread.html'
language: en
---

# GPIO Read

## Ports

### Output

### **Port\_1** — Output port containing the logical value scalar

Output port containing the logical value of a digital pin.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **GPIO port** — GPIO port to read the GPIO pin status GPIOA (default) | GPIOA | GPIOB | GPIOC | GPIOD | GPIOE | GPIOF | GPIOG | GPIOH | GPIOI

Select one of GPIOA to GPIOI ports to get a GPIO pin status.

### **Pin number** — GPIO pin to read the logical status 0 (default) | scalar

Select a GPIO pin to read the logical status.

### **Sample time** — Time frequency at which the read the pin value -1 (default) | scalar

Specify how often this block reads the pin value, in seconds.
Enter a value greater than zero.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4-Discovery

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

## Description

Read GPIO pin status

Read the logical value of a digital pin of the STM32F4 –Discovery™ board.
