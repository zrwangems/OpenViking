---
type: simulink-block
title: 'Altimeter'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Instruments'
documentation_page: 'altimeter'
documentation_source_path: 'altimeter.html'
language: en
---

# Altimeter

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Connection
  summary: Connect to signal signal name
  group: ''
- name: Label
  summary: Block label location Top (default) | Bottom | Hide
  group: ''
  block_parameter: LabelPosition
  type: character vector
  values: '''Top'' | ''Bottom'' | ''Hide'''
  default: '''Top'''
```

### **Connection** — Connect to signal signal name

Connect to signal for display, selected from list of signal names.

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

This block is ignored for code generation.

## Version History

**Introduced in R2016a**

## Description

Display measurements for aircraft altitude

The Altimeter Indicator block displays the altitude above sea level in feet, also known as the pressure altitude. The block displays the altitude value with needles on a gauge and a numeric indicator.

- The gauge has 10 major ticks. Within each major tick are five minor ticks.
  This gauge has three needles. Using the needles, the altimeter can display
  accurately only altitudes between 0 and 100,000 feet.

  - For the longest needle, an increment of a small tick represents 20
    feet and a major tick represents 100 feet.
  - For the second longest needle, a minor tick represents 200 feet and a
    major tick represents 1,000 feet.
  - For the shortest needle a minor tick represents 2,000 feet and a major
    tick represents 10,000 feet.
- For the numeric display, the block shows values as numeric characters between
  0 and 9,999 feet. When the numeric display value reaches 10,000 feet, the gauge
  displays the value as the remaining values below 10,000 feet. For example,
  12,345 feet displays as 2,345 feet. When a value is less than 0 (below sea
  level), the block displays `0`. The needles show the
  appropriate value except for when the value is below sea level or over 100,000
  feet. Below sea level, the needles are set to `0`, over
  100,000, the needles stay set at 100,000.

**Tip**

To facilitate understanding and debugging your model, you can modify instrument
block connections in your model during normal and accelerator mode
simulations.
