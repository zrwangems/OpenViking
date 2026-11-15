---
type: simulink-block
title: 'Turn Coordinator'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Visualization / Flight Instruments'
documentation_page: 'turncoordinator'
documentation_source_path: 'turncoordinator.html'
language: en
---

# Turn Coordinator

## Ports

Not documented in R2025b.

## Parameters

### **Connection** — Connect to signal signal name | 2-element signal

Connect to 2-element signal for display, selected from a list of signal names. The
2-element signal consists of turn indicator and inclinometer signals
combined in a Mux block, in degrees. You connect and display
this combined signal. This input cannot be a bus signal.

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

Display measurements on turn coordinator and inclinometer

The Turn Coordinator block displays measurements on a gyroscopic turn
rate instrument and on an inclinometer.

- The gyroscopic turn rate instrument shows the rate of heading change of the
  aircraft as a tilting of the aircraft symbol in the gauge.
- The inclinometer shows whether the turn is coordinated, slipping, or skidding
  by the position of the ball.

When the ball is centered, the turn is coordinated. When the ball is off center, the turn is
slipping or skidding. The turn rate instrument has marks for wings level and for a
standard rate turn. A standard rate turn is a heading change of 3 degrees per second,
also known as a two minute turn.

The input for gyroscopic turn rate instruments and inclinometers is in degrees. The turn
rate value is input as the degrees of tilt of the aircraft symbol in the gauge. The
standard rate turn marks are at angles of ±15 degrees. Tilt angle values are limited to
±20 degrees, whereas inclinometer angles are limited to ±15 degrees.

Combine the turn indicator and inclinometer signals in a Mux block in
order:

1. Turn indicator
2. Inclinometer

For example, turn indicator and inclinometer values of `[15 0]`
indicate a coordinated, standard rate turn.

**Tip**

To facilitate understanding and debugging your model, you can modify instrument
block connections in your model during normal and accelerator mode
simulations.
