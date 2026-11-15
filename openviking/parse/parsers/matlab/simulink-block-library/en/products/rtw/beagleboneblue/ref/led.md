---
type: simulink-block
title: 'LED'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'led'
documentation_source_path: 'beagleboneblue/ref/led.html'
language: en
---

# LED

## Ports

### Input

### **Port\_1** — Input signal scalar

If the input to the block is a nonzero value, the LED specified in the
**LED** parameter turns on. If the input to the
block is zero, the LED specified in the **LED**
parameter turns off.

For example, if the **LED** parameter is set to
`GREEN` and the input to the block is
`5`, the green LED on the hardware starts
glowing.

**Data Types:** `uint8`

## Parameters

### **LED** — User-controllable LED `RED` (default) | `GREEN`

Select the LED to be turned on or off.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

## Description

Illuminate built-in LED

The LED block illuminates a user-controllable LED on the
hardware.

The block accepts a `uint8` value as input. If the input to the block
is a nonzero value, the LED specified in the **LED** parameter turns
on. If the input to the block is zero, the LED specified in the
**LED** parameter turns off.

During simulations without hardware, this block does nothing. See Block Produces Zeros or Does Nothing in Simulation.

**Note**

Do not specify the same LED in multiple blocks within a model.
