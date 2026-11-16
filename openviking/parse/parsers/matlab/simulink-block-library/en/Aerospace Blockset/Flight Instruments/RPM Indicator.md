---
type: simulink-block
title: 'Revolutions Per Minute (RPM) Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2023b
official_category: 'Flight Instruments'
documentation_page: 'revolutionsperminuterpmindicator'
documentation_source_path: 'revolutionsperminuterpmindicator.html'
language: en
---

# Revolutions Per Minute (RPM) Indicator

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

### **Scale Colors** — Ranges of color bands 0 (default) | double | scalar

Ranges of color bands on the outside of the scale, specified as a finite double, or
scalar value. Specify the minimum and maximum color range to display on the
gauge.

To add a new color, click `+`. To remove a color, click
`-`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ScaleColors` |
| **Type**: *n*-by-1 struct array |
| **Values**: struct array with elements `Min`, `Max`, and `Color` |

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

Display measurements for engine revolutions per minute (RPM) in percentage of RPM

The RPM Indicator block displays measurements for engine revolutions per minute in percentage of RPM.

The range of values for RPM goes from 0 to 110 %. Minor ticks represent increments of 5 %
RPM and major ticks represent increments of 10 % RPM.

**Tip**

To facilitate understanding and debugging your model, you can modify instrument
block connections in your model during normal and accelerator mode
simulations.
