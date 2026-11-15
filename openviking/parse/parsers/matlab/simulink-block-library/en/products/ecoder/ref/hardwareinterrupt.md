---
type: simulink-block
title: 'Hardware Interrupt'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'hardwareinterrupt'
documentation_source_path: 'ref/hardwareinterrupt.html'
language: en
---

# Hardware Interrupt

## Ports

### Input

### **Default event task** — Function-call event input simulation `scalar`

The simulation-only message input acts as pass-through with the output
emitted on the block in simulation.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter.
### Output

### **Default event** — Generate interrupt request `scalar`

The output of this block is a function-call.

## Parameters

### **Simulink task priority** — Set priority of selected ISR `50` (default) | `0-255`

The value you specify in this parameter sets the priority of the
downstream function-call subsystem. The simulink task priority of the
selected (ISR) is relative to the model base rate priority.

### **Run interrupt service routine as atomic unit** — Select to disable interrupt preemption `off` (default) | `on`

Select this parameter to block all other interrupts while executing the
selected interrupt service routine.

### **Enable simulation port** — Enable peripheral simulation ports in the block `off` (default) | `on`

Select this parameter to enable peripheral simulation capability.

### **Port Type** — Specify the type of peripheral simulation port `SoC Data (Message based)` (default) | `Signal`

Select this parameter to configure either the SoC compatible or the
Simulink® signal based simulation ports to enable peripheral simulation
capability.

#### Dependencies

To view this parameter, select the **Enable simulation
port** parameter.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

## Description

Trigger downstream function-call subsystem from an interrupt service routine

Trigger the downstream function-call subsystem from an interrupt service routine
(ISR).
