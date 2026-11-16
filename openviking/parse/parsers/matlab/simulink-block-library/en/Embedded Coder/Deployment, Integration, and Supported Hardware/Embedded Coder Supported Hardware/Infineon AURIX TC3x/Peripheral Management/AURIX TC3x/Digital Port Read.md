---
type: simulink-block
title: 'Digital Port Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'digitalportread'
documentation_source_path: 'infineonaurixtc3x/ref/digitalportread.html'
language: en
---

# Digital Port Read

## Ports

### Input

### **msg** — SoC Blockset simulation message `scalar`

This port receives the message from the interface blocks and the Digital
Port Read block converts the **msg** into data to be emitted
at the output port during simulation.

#### Dependencies

To view this port, select the **Enable simulation port**
parameter and set the port type as **SoC Data (Message
based)**.

### **sig** — Simulink based simulation signal `scalar` | `vector`

The simulation-only signal input port acts as pass-through with the output
of the Digital Port Read block during simulation.

#### Dependencies

To view this port, select the **Enable simulation port**
parameter and set the port type as **Signal**.
### Output

### **Pin(s)** — GPIO pin status `scalar` | `vector`

The port outputs the status of the digital pin you select in the
**Port number** and **Pin number**
parameter from Digital Port Read Peripheral Configuration.

The port outputs the status as a logical scalar if the pin number is
`1` or as a logical vector if it is greater than
`1`.

**Data Types:** `Boolean`

## Parameters

### **Number of pins** — Number of pins you want to configure `1` (default) | `2` | `3` | `...`

Select the number of pins (`1` to `15`) whose
output you want to configure in the block.

### **Sample time** — Frequency at which block reads input pin values `-1` (default) | `scalar` | `vector`

Specify in seconds how often the block should read the pin value.

When you specify this parameter as `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

### **Enable simulation port** — Enable peripheral simulation ports in the block `off` (default) | `on`

Select this parameter to enable peripheral simulation capability.

### **Port Type** — Specify the type of peripheral simulation port `SoC Data (Message based)` (default) | `Signal`

Select this parameter to configure either the SoC compatible or the Simulink signal based simulation ports to enable peripheral simulation
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

Read GPIO pin(s) status

Read the logical status of a GPIO port pin for the Infineon AURIX TC3x
Microcontrollers.
