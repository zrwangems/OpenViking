---
type: simulink-block
title: 'LED'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'led'
documentation_source_path: 'supportpkg/raspberrypi_ref/led.html'
language: en
---

# LED

## Ports

### Input

### **Port\_1** — Input signal scalar

If the input to the block is a nonzero value, the LED specified in the **LED** parameter turns on. If the input to the block is zero,
the LED specified in the **LED** parameter turns
off.

For example, if the **LED** parameter is set to
`led0(Green)` and the input to the block is
`5`, the green LED on the hardware starts glowing.

**Data Types:** `uint8`

## Parameters

### **Board** — Raspberry Pi hardware board `Pi 2 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

Select your Raspberry Pi hardware board. You can find this information on the target hardware,
product packaging, or product documentation.

### **LED** — User-controllable LED `led0(Green)` (default) | LED on Raspberry Pi board

Select the LED to be turned on or off on your Raspberry Pi hardware board. To view the locations of the LED on the Raspberry Pi board, click **View LED location**.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013a**

## Description

Illuminate built-in LED on Raspberry Pi board

Use the LED block to illuminate a user-controllable LED on the Raspberry Pi® board. During simulations without the hardware, this block does nothing. See
Block Produces Zeros or Does Nothing in Simulation.

**Note**

Do not specify the same LED in multiple blocks within a model.
