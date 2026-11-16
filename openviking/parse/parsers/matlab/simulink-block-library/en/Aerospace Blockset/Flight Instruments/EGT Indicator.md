---
type: simulink-block
title: 'Exhaust Gas Temperature (EGT) Indicator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2023b
official_category: 'Flight Instruments'
documentation_page: 'exhaustgastemperatureegtindicator'
documentation_source_path: 'exhaustgastemperatureegtindicator.html'
language: en
---

# Exhaust Gas Temperature (EGT) Indicator

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

### **Minimum** — Minimum tick mark value 0 (default) | finite | double | scalar

Minimum tick mark value, specified as a finite double, or scalar value, in ft/min.

#### Dependencies

The **Minimum** tick value must be less than the **Minimum** tick value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Limits` |
| **Type**: double |
| **Values**: double scalar |
| **Default**: `[0 1000]`, where `0` is the minimum value |

### **Maximum** — Maximum tick mark value 1000 (default) | finite | double | scalar

Specify the maximum tick mark value, specified as a finite double, or scalar value, in
ft/min..

#### Dependencies

The **Maximum** tick value must be
greater than the **Maximum** tick
value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Limits` |
| **Type**: double |
| **Values**: double scalar |
| **Default**: `[0 1000]`, where `1000` is the maximum value |

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

Display measurements for engine exhaust gas temperature (EGT)

The EGT Indicator block displays temperature measurements for engine exhaust gas temperature (EGT) in Celsius.

This block displays values using both:

- A needle on a gauge. A major tick is (**Maximum**-**Minimum**)/1,000
  degrees, a minor tick is (**Maximum**-**Minimum**)/200 degrees Celsius.
- A numeric indicator. The operating range for the indicator
  goes from **Minimum** to **Maximum** degrees Celsius.

If the value of the signal is under **Minimum**,
the needle displays 5 degrees under the **Minimum** value,
the numeric display shows the **Minimum** value.
If the value exceeds the **Maximum** value, the needle
displays 5 degrees over the maximum tick, and the numeric displays
the **Maximum** value.

**Tip**

To facilitate understanding and debugging your model, you can modify instrument
block connections in your model during normal and accelerator mode
simulations.
