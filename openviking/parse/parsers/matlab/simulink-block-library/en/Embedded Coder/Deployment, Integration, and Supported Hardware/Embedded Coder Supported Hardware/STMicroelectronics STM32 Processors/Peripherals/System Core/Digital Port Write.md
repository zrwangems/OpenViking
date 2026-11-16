---
type: simulink-block
title: 'Digital Port Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / System Core'
documentation_page: 'digitalportwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/digitalportwrite.html'
language: en
---

# Digital Port Write

## Ports

### Input

### **Pin(s)** — Set GPIO pin status `scalar` | `vector`

The input port to set the GPIO pin status in incremental order.

- 0 - the respective pin is set to low value.
- Non zero - the pin is active low or active high.

#### Dependencies

To read multiple port values, select **Access port pins as
array** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **msg Pin *`n`*** — SoC Blockset™ simulation message scalar | vector

The simulation-only message output port, when connected to an Digital
IO Interface (SoC Blockset) block, acts as pass-through with the output
emitted on the output of the Digital IO Interface block
during simulation. When the **Access port pins as
array** parameter is not selected, a simulation port is
generated for each pin in the **Pin number** parameter,
otherwise the pin array must be treated as a scalar.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter.

**Data Types:** `SoCData`

## Parameters

### **Port name** — Port to write GPIO pin status `GPIOA` (default) | `GPIOB` | `GPIOC` | `GPIOD` | `GPIOE` | `GPIOF` | `GPIOG` | `GPIOH` | `GPIOI` | `GPIOJ` | `GPIOK`

Select one of `GPIOA` to `GPIOK` ports
to set a GPIO pin status of a specified GPIO port.

### **Pin number** — GPIO port to set GPIO pin status `0` (default) | `any range between 1 to 15`

Specify the GPIO digital pin to set the logical status.

### **Access port pins as array** — Input multiple pin values `on` (default) | `off`

Select this parameter to read multiple port pin values.

### **Enable simulation port** — Enable simulation ports to block `off` (default) | `on`

Select this parameter to add an SoC Blockset compatible simulation output port.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Set GPIO pin status

Write the logical status of a GPIO port pins for STM32 processors.

**Note**

You can run a Simulink® model containing Digital Port Write block in Connected
IO mode on STM32 Processor Based Boards. For more information, see Communicate with Hardware Using Connected IO.
