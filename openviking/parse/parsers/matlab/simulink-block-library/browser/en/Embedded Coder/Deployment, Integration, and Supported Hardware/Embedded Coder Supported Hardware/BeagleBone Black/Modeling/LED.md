---
type: simulink-block
title: 'LED'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'led'
documentation_source_path: 'beaglebone/ref/led.html'
language: en
---

# LED

## Ports

### Input

### **Port\_1** — Input signal scalar

If the input to the block is a nonzero value, the LED specified in the
**LED** parameter turns ON. If the input to the block is zero, the
LED specified in the **LED** parameter turns OFF.

For example, if the **LED** parameter is set to
`GREEN` and the input to the block is `5`,
the green LED on the hardware starts glowing.

**Data Types:** `Boolean`

## Parameters

### **LED** — User-controllable LED `USR0` (default) | `USR1``USR2``USR3`

Select the LED to be turned on or off on your BeagleBone hardware board. To view the locations of the LED on the BeagleBone board, click **View LED location**.

## Libraries

Embedded Coder Support Package for BeagleBone Black Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Illuminate built-in LED on BeagleBone board

Use the LED block to illuminate a user-controllable LED on the BeagleBone® board. During simulations without the hardware, this block does nothing. See
Block Produces Zeros or Does Nothing in Simulation.

**Note**

Do not specify the same LED in multiple blocks within a model.
