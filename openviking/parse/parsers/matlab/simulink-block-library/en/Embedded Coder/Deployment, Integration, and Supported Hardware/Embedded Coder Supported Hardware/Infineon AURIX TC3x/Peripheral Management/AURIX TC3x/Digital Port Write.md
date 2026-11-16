---
type: simulink-block
title: 'Digital Port Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'digitalportwrite'
documentation_source_path: 'infineonaurixtc3x/ref/digitalportwrite.html'
language: en
---

# Digital Port Write

## Ports

### Input

### **Pin(s)** — Status of GPIO pin(s) `scalar` | `vector`

Specify a value at this port to set the status of GPIO pin(s). You can
specify a non-negative scalar or a vector of non-negative elements.

- Specify `0` to set the pin(s) to a low
  value.
- Specify a `nonzero` value to set the pin(s) to a
  high value.

The size of input ports available depends on the **Number of
pins** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **msg** — SoC simulation message `scalar`

The Digital Port Write block converts the data received at input port into
SoC Blockset™ message form and the **msg** port outputs that
message during simulation.

#### Dependencies

To view this port, select the **Enable simulation port**
parameter and set the port type as **SoC Data (Message
based)**.

### **sig** — Simulink based simulation signal `scalar` | `vector`

This port outputs the data received at the input port during simulation.

#### Dependencies

To view this port, select the **Enable simulation port**
parameter and set the port type as **Signal**.

## Parameters

### **Number of pins** — Number of pins you want to configure `1` (default) | `2` | `3` | `...`

Select the number of pins (`1` to `15`) whose
output you want to configure in the block.

### **Enable simulation port** — Enable peripheral simulation ports in the block `off` (default) | `on`

Select this parameter to enable peripheral simulation capability.

### **Port Type** — Specify the type of peripheral simulation port `SoC Data (Message based)` (default) | `Signal`

Select this parameter to configure either the SoC compatible or the Simulink® signal based simulation ports to enable peripheral simulation
capability.

#### Dependencies

To view this parameter, select the **Enable simulation
port** parameter.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Set GPIO pin(s) status

Write logical status of pins of a GPIO port for the Infineon AURIX TC3x
Microcontrollers.
