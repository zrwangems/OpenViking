---
type: simulink-block
title: 'PWM Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Other'
documentation_page: 'pwmwrite'
documentation_source_path: 'ref/pwmwrite.html'
language: en
---

# PWM Write

## Ports

### Input

### **Compare** — Comparator trigger value positive scalar | *N*-length positive vector

Specify the comparator values that trigger the change in pulse-width modulation
waveform. When a *N* is `1`, the comparator value
defines the duty cycle of the PWM waveform. Using `2` comparators and
the settings provided in the PWM Interface block, more fine grained control of the
output waveform can be achieved.

**Data Types:** `single` | `double`

### **Period** — Period of PWM waveform positive scalar

Specify the total period of the PWM waveform.

#### Dependencies

This parameter is only available when the **Show period as
input** parameter is enabled.

**Data Types:** `single` | `double`

### **Phase** — Phase offset of the waveform scalar from `0` to PWM period

Specify the phase of the PWM waveform relative period of waveform. The phase is
represented as a scalar between `0` and PWM period.

#### Dependencies

This parameter is only available when the **Show phase as
input** parameter is enabled.

**Data Types:** `single` | `double`
### Output

### **msg** — PWM duty cycle values scalar

This message port sends duty cycle values as messages to a connected PWM Interface
block. For more information on messages, see Messages.

**Note**

This output is used only during simulation and is ignored in code generation and
external mode simulation.

**Data Types:** `SoCData`

## Parameters

### **Show period as input** — Show period input port `off` (default) | `on`

Show a **Period** input port on the block. This port accepts
a dynamic period value for the PWM waveform, allowing the period of waveform to be
modified during execution.

### **Show phase as input** — Show phase input port `off` (default) | `on`

Show a **Phase** input port on the block. This port accepts a
dynamic phase value for the PWM waveform, allowing the phase offset of the waveform to
be modified during execution.

## Libraries

SoC Blockset / Processor I/O

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

When deployed to a supported hardware board, this generated code for this block writes
to the PWM registers in the MCU for the specified PWM module. For more information on
configuring the register settings, see Hardware Mapping.

## Version History

**Introduced in R2020b**

## Description

Send pulse width modulation (PWM) signal configuration to PWM Interface block

The PWM Write block sets the duty cycle for a PWM peripheral. In
simulation, the block passes through the duty cycle input to drive the PWM Interface block
that simulates the PWM switching signals produced by the hardware. When deployed to hardware,
the PWM Write block writes to the appropriate PWM drivers on the
hardware.
