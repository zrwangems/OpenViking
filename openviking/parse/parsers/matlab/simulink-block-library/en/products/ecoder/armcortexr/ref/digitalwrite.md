---
type: simulink-block
title: 'Digital Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-R Processors / Modeling'
documentation_page: 'digitalwrite'
documentation_source_path: 'armcortexr/ref/digitalwrite.html'
language: en
---

# Digital Write

## Ports

### Input

### **Port\_1** — Logical value of selected GIO pin nonnegative scalar

Logical value of the selected GIO pin, specified as a Simulink® signal. This port accepts a signal of any data type and internally
converts it to `boolean`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

### **Pin** — GIO Pin `GIOB_6 (LED 2)` (default) | `GIOB_7 (LED 3)`

Select the `GIO` pin on the Texas Instruments Hercules RM57Lx Launchpad hardware board to which you want to write the
logical status.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Whichpin` |

## Libraries

Embedded Coder Support Package for ARM Cortex-R Processors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Write value to GIOB[6] or GIOB[7] pins on Texas Instruments Hercules RM57Lx microcontroller

Write a logical value to the `GIOB[6]` or `GIOB[7]` pins
of the Texas Instruments® Hercules `RM57Lx` microcontroller based on the ARM®
Cortex®-R processor core.

The `GIOB[6]` or `GIOB[7]` pins connect to `LED
2` and `LED 3` on Texas Instruments Hercules RM57Lx Launchpad hardware board, respectively.
