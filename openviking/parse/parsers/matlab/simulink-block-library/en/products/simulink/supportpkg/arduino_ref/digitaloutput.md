---
type: simulink-block
title: 'Digital Output'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'digitaloutput'
documentation_source_path: 'supportpkg/arduino_ref/digitaloutput.html'
language: en
---

# Digital Output

## Ports

### Input

### **Port\_1** — Input signal voltage on Arduino digital output pin scalar

The block sets this value to the digital output pin that you specify in the
**Pin number** parameter.

- Send `1` to the block to set logical value of the digital
  pin HIGH to 5 V or 3.3 V, depending on the board voltage.
- Send `0` to the block to set logical value of the digital
  pin LOW to 0 V.

**Data Types:** `double`

## Parameters

### **Pin number** — Arduino pin number `9` (default) | Arduino board pin number

Enter the Arduino board digital output pin number. To open the Arduino pin mapping
table, click **View pin map**. For more information on how to assign
pins for the Digital Output block, see Pin Mapping for Arduino Timer-Independent Blocks.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Set logical state of digital output pin on Arduino

Use the Digital Ouptut block to set the logical state of the specified
digital pin on the Arduino® board that you specify in the **Pin number** parameter.

During the external mode simulation, the block sets the value to the pin that you specify
in the **Pin number** parameter. During simulation in all other modes, the
block does nothing.
