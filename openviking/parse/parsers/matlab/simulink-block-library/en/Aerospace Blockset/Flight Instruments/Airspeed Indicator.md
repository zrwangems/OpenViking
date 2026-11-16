---
type: simulink-block
title: 'Airspeed Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'airspeedindicator'
documentation_source_path: 'airspeedindicator.html'
language: en
---

# Airspeed Indicator

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

### **Minimum** — Minimum tick mark value 40 (default) | finite | double | scalar

Minimum tick mark value, specified as a finite double scalar value, in knots.

#### Dependencies

The **Minimum** tick value must be less
than the **Maximum** tick value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Limits` |
| **Type**: double |
| **Values**: vector |
| **Default**: `[40 400]`, where `40` is the minimum value |

### **Maximum** — Maximum tick mark value 400 (default) | finite | double | scalar

Specify the maximum tick mark value, specified as a finite double scalar value, in
knots.

#### Dependencies

The **Maximum** tick value must be greater than the
**Minimum** tick value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Limits` |
| **Type**: double |
| **Values**: vector |
| **Default**: `[40 400]`, where `400` is the maximum value |

### **Scale Colors** — Ranges of color bands 0 (default) | double | scalar

Ranges of color bands outside the scale, specified as a finite double scalar value.
Specify the minimum and maximum color range to display on the gauge.

To add a new color, click `+`. To remove a color, click
`-`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ScaleColors` |
| **Type**: *n*-by-1 struct array |
| **Values**: struct array with elements `Min`, `Max`, and `Color` |

### **Label** — Name of connected signal `Top` (default) | `Bottom` | `Hide`

Name of connected signal.

- `Top`

  Show label at the top of the block.
- `Bottom`

  Show label at the bottom of the block.
- `Hide`

  Do not show the label or instructional text when the block is not connected.

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

Display measurements for aircraft airspeed

The Airspeed Indicator block displays measurements for aircraft airspeed in knots.

By default, minor ticks represent 10-knot increments and major ticks represent 40-knot
increments. The parameters **Minimum** and **Maximum**
determine the minimum and maximum values on the gauge. The number and distribution of
ticks is fixed, which means that the first and last tick display the minimum and maximum
values. The ticks in between distribute evenly between the minimum and maximum values.
For major ticks, the distribution of ticks is
(**Maximum**-**Minimum**)/9. For minor ticks, the
distribution of ticks is
(**Maximum**-**Minimum**)/36.

The airspeed indicator has scale color bars that allow for overlapping for the first bar,
displayed at a different radius. This different radius lets the block represent maximum
speed with flap extended (VFE) and stall speed with flap extended
(VSO) accurately for aircraft airspeed and stall speed.

**Tip**

To facilitate understanding and debugging your model, you can modify instrument
block connections in your model during normal and accelerator mode
simulations.
