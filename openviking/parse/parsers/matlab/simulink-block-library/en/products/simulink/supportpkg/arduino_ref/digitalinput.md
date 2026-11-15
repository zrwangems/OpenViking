---
type: simulink-block
title: 'Digital Input'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'digitalinput'
documentation_source_path: 'supportpkg/arduino_ref/digitalinput.html'
language: en
---

# Digital Input

## Ports

### Output

### **Port\_1** — Output signal voltage on Arduino digital input pin scalar

The block outputs the logical state of the digital pin on the Arduino board that you specify in the **Pin
number** parameter.

- If the logical value of the digital pin is LOW (0 `V`), the
  block output emits `0`.
- If the logical value of the digital pin is HIGH (5 `V` or
  3.3 `V`, depending on the board voltage), the block output
  emits `1`.

**Data Types:** `Boolean`

## Parameters

### **Pin number** — Arduino pin number `8` (default) | Arduino board pin number

Enter the Arduino board digital input pin number. To open the Arduino pin mapping
table, click **View pin map**. For more information on how to assign
pins for the Digital Input block, see Pin Mapping for Arduino Timer-Independent Blocks.

### **Pin mode** — Mode of Arduino board digital pin `Default` (default) | `Input Pullup`

Set the mode of the Arduino board digital pin.

- `Default` — Select this mode to set the Arduino board digital pin to the default mode. This mode sets the pin in an
  high-impedance state. In this mode, the pin can detect the voltage applied to it,
  either HIGH or LOW.
- `Input Pullup` — Select this mode to set the
  Arduino board digital pin to the input pullup mode and activate the internal
  pull-up resistor. The pull-up resistor ensures that the pin reads a HIGH state by
  default when an external signal is not applied.

### **Sample time** — Time interval at which the blocks read input pin value `0.1` (default) | scalar

Specify how often this block reads the pin value, in seconds. Enter a value greater
than zero.

Smaller values require the processor to complete the same number of instructions in
less time, which can cause task overruns. When you specify this parameter as
`–1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Get logical state of digital input pin on Arduino

Use the Digital Input block to read and output the logical state of the
digital pins on your Arduino® board.

During the external mode simulation, the block outputs the simulation results returned
from the executable running on the target hardware. During simulation in all other modes, the
block outputs zeroes.
