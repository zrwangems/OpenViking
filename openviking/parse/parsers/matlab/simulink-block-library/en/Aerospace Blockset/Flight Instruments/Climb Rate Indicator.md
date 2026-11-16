---
type: simulink-block
title: 'Climb Rate Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'climbrateindicator'
documentation_source_path: 'climbrateindicator.html'
language: en
---

# Climb Rate Indicator

## Ports

Not documented in R2025b.

## Parameters

### **Connection** — Connect to signal signal name

Connect to signal for display, selected from list of signal names.

To view the data from a signal, select a signal in the model. The signal
appears in the **Connection** table. Select the option
button next to the signal you want to display. Click
**Apply** to connect the signal.

The table has a row for the signal connected to the block. If there are no
signals selected in the model, or the block is not connected to any signals,
the table is empty.

### **Maximum** — Maximum tick mark value 4000 (default) | finite | double | scalar

Maximum tick mark value, specified as a finite double scalar value, in ft/min.

The minimum tick value is always `0`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MaximumRate` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'4000'` |

### **Label** — Block label location `Top` (default) | `Bottom` | `Hide`

Block label, displayed at the top or bottom of the block, or
hidden.

- `Top`

  Show label at the top of the block.
- `Bottom`

  Show label at the bottom of the block.
- `Hide`

  Do not show the label or instructional text when the block is not
  connected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LabelPosition` |
| **Type**: character vector |
| **Values**: `'Top'` | `'Bottom'` | `'Hide'` |
| **Default**: `'Top'` |

## Libraries

Aerospace Blockset / Flight Instruments

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block is ignored for code generation.

## Version History

**Introduced in R2016a**

## Description

Display measurements for aircraft climb rate

The Climb Rate Indicator block displays measurements for an aircraft climb rate in ft/min.

The needle covers the top semicircle, if the velocity is positive,
and the lower semicircle, if the climb rate is negative. The range
of the indicator is from –**Maximum** feet
per minute to **Maximum** feet per minute. Major
ticks indicate **Maximum**/4. Minor ticks indicate **Maximum**/8
and **Maximum**/80.

**Tip**

To facilitate understanding and debugging your model, you can modify instrument
block connections in your model during normal and accelerator mode
simulations.
