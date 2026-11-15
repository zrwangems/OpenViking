---
type: simulink-block
title: 'Digital Port Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / System Core'
documentation_page: 'digitalportread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/digitalportread.html'
language: en
---

# Digital Port Read

## Ports

### Input

### **Pin *`n`* msg** — SoC Blockset™ simulation message scalar

The simulation-only message input port, when connected to an Digital IO Interface (SoC Blockset)
block, acts as pass-through with the input to the Digital IO
Interface block emitted on the output of the Digital
Port Read block during simulation. When the **Access
port pins as array** parameter is not selected, a
simulation port is generated for each pin in the **Pin
number** parameter, otherwise the pin array must be treated
as a scalar.

#### Dependencies

To enable this port, check the **Enable simulation
port** parameter.

**Data Types:** `SoCData`
### Output

### **Pin(s)** — Output port containing the logical value `scalar` | `vector`

The port outputs the logical state of the digital pin on the board
that you specify in the **Pin number**
parameter.

#### Dependencies

To output multiple port values, select **Access port pins
as array** parameter.

**Data Types:** `Boolean`

## Parameters

### **Port name** — Port to read GPIO pin status `GPIOA` (default) | `GPIOB` | `GPIOC` | `GPIOD` | `GPIOE` | `GPIOF` | `GPIOG` | `GPIOH` | `GPIOI` | `GPIOJ` | `GPIOK`

Select one of `GPIOA` to `GPIOK` ports
to get a GPIO pin status of a specified GPIO port.

### **Pin number** — GPIO pin to read logical status `0` (default) | `scalar` | `vector`

Specify a GPIO pin to read the logical status.

When you specify a GPIO pin number and **Access port pins as
array** parameter is enabled, the output is always in the
incremental order of pin number.

### **Access port pins as array** — Output multiple pin values `on` (default) | `off`

Select this parameter to output multiple port pin values.

### **Sample time** — Frequency at which block reads input pin value `-1` (default) | `scalar` | `vector`

Specify in seconds how often this block reads the pin value.

When you specify this parameter as `-1`, Simulink determines the best sample time for the block based on the
block context within the model.

### **Enable simulation port** — Enable simulation ports to block `off` (default) | `on`

Select this parameter to add an SoC Blockset compatible simulation input port.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Read GPIO pin status

Read the logical status of a GPIO port pins for STM32 processors.

**Note**

You can run a Simulink® model containing Digital Port Read block in Connected
IO mode on STM32 Processor Based Boards. For more information, see Communicate with Hardware Using Connected IO.
