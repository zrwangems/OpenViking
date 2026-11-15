---
type: simulink-block
title: 'Digital Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / ARM Cortex-R Processors / Modeling'
documentation_page: 'digitalread'
documentation_source_path: 'armcortexr/ref/digitalread.html'
language: en
---

# Digital Read

## Ports

### Output

### **Port\_1** — Logical value of specified GIO pin boolean scalar

Logical value of the specified GIO pin, returned as a boolean scalar.

**Data Types:** `uint32`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

### **Pin** — GIO Pin `GIOB_4 (User Switch A)` (default) | `GIOB_5 (User Switch B)`

Select the `GIO` pin on the Texas Instruments Hercules RM57Lx Launchpad hardware board from which you want read the
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

Read value from GIOB[4] or GIOB[5] pins on Texas Instruments Hercules RM57Lx microcontroller

Read logical value from the `GIOB[4]` or `GIOB[5]` pins
of the Texas Instruments® Hercules `RM57Lx` microcontroller based on the ARM®
Cortex®-R processor core.

The Digital Read block outputs a signal of type
`uint32`.

The `GIOB[4]` or `GIOB[5]` pins connect to `User
Switch A` and `User Switch B` on the Texas Instruments Hercules RM57Lx Launchpad hardware board, respectively.
