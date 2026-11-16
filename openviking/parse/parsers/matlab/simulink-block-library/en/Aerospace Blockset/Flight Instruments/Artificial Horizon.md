---
type: simulink-block
title: 'Artificial Horizon'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'artificialhorizon'
documentation_source_path: 'artificialhorizon.html'
language: en
---

# Artificial Horizon

## Ports

Not documented in R2025b.

## Parameters

### **Connection** — Connect to signal signal name | 2-element signal

Connect to 2-element signal for display, selected from list of signal names. The
2-element signal consists of roll and pitch combined together in a
Mux block, in degrees. You connect and display this
combined signal. This input cannot be a bus signal.

To view the data from a signal, select a signal in the model. The signal
appears in the **Connection** table. Select the option
button next to the signal you want to display. Click
**Apply** to connect the signal.

The table has a row for the signal connected to the block. If there are no
signals selected in the model, or the block is not connected to any signals,
the table is empty.

To view the data from a signal, select a signal in the model. The signal
appears in the **Connection** table. Select the option
button next to the signal you want to display. Click
**Apply** to connect the signal.

The table has a row for the signal connected to the block. If there are no
signals selected in the model, or the block is not connected to any signals,
the table is empty.

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

## Version History

**Introduced in R2016a**

## Description

Represent aircraft attitude relative to horizon

The Artificial Horizon block represents aircraft attitude relative to
horizon and displays roll and pitch in degrees:

- Values for roll cannot exceed +/– 90 degrees.
- Values for pitch cannot exceed +/– 30 degrees.

If the values exceed the maximum values, the gauge maximum and minimum values do not
change.

Changes in roll value affect the gauge semicircles and the ticks located on the black
arc turn accordingly. Changes in pitch value affect the scales and the distribution of
the semicircles.

Combine the roll and pitch signals in a Mux block in the order:

1. Roll
2. Pitch

**Tip**

To facilitate understanding and debugging your model, you can modify instrument
block connections in your model during normal and accelerator mode
simulations.
