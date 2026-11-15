---
type: simulink-block
title: 'Comparator'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Analog Peripherals'
documentation_page: 'comparator'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/comparator.html'
language: en
---

# Comparator

## Ports

### Input

### **Enable** — Enable run time scalar

The port `Enable` allows user to enable the comparator
module during run time.

#### Dependencies

To enable this port, select the **Run time module
enable** parameter.

**Data Types:** `uint8` | `uint16`
### Output

### **result** — Result of comparator scalar

The block outputs the result of the comparator.

- `0` - +ve pin input is greater than -ve pin
  input
- `1` - +ve pin input is less than -ve pin input

**Data Types:** `Boolean`

### **Status** — Status of comparator scalar

The block outputs comparator execution status.

- `0` - Valid result
- `1` - Invalid result

#### Dependencies

To enable this port, select the **Run time module
enable** and **Output status**
parameters.

**Data Types:** `Boolean`

## Parameters

### **Comparator module** — Select comparator module `COMP1` (default) | `COMP2` | `COMP3` | `COMP4` | `COMP5` | `COMP6` | `COMP7`

Select a comparator module for comparison of analog inputs.

### **Run time module enable** — Select to enable comparator `off` (default) | `on`

Select to Run time module enable to enable the comparator during run time.
Selecting this parameter, configures the enable input port.

### **Output status** — Comparator output `off` (default) | `on`

When you select this parameter, the block configures
**Status** output port. The Status port outputs the status of
the comparator.

#### Dependencies

To enable this parameter, select the **Run time module
enable** parameter.

### **Sample time** — Frequency at which block reads pin value `-1` (default) | `non-negative real value`

Specify how often (in seconds) the block reads the pin value. Enter a value
greater than zero. When you specify this parameter as -1, Simulink determines the
best sample time for the block based on the block context within the model.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Compare two analog inputs on peripheral and provide results

The Comparator block compares two analog inputs on the peripheral and
provides the logical value of the result.
