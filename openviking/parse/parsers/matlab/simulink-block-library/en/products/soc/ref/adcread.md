---
type: simulink-block
title: 'ADC Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Other'
documentation_page: 'adcread'
documentation_source_path: 'ref/adcread.html'
language: en
---

# ADC Read

## Ports

### Input

### **msg** — Data message from register scalar

This message port receives ADC value messages from a connected ADC Interface
block. The messages process when the Task Manager block triggers a task containing the
ADC Read block. For more information on messages, see Messages.

**Data Types:** `SoCData`
### Output

### **data** — Output signal scalar

This port emits a measurement from the ADC Interface block.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Data type** — Data type of ADC measurements received `double` (default) | `single` | `uint8` | `int8` | `int16` | `int32` | `uint16` | `uint32`

Select the data type of the input data. Match this data type with data type of the
ADC hardware.

### **Sample time** — Sample time `-1` (default) | nonnegative scalar

Specify how often the scheduler runs this block. If this value is
`-1` (default), the scheduler assigns the sample time for the
block.

## Libraries

SoC Blockset / Processor I/O

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

When deployed to a supported hardware board, this generated code for this block reads
the ADC registers in the MCU for the specified ADC module. For more information on
configuring the register settings, see Hardware Mapping.

## Version History

**Introduced in R2020b**

## Description

Read ADC data values from ADC Interface block

The ADC Read block converts the message received from the ADC Interface
block to a signal that can be used by an algorithm. The data type of the output signal is the
same as the data type in the contained data message.
