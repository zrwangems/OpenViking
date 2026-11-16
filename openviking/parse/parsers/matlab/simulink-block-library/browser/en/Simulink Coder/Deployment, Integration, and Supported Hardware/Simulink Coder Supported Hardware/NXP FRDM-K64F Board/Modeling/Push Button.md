---
type: simulink-block
title: 'Push Button'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'pushbutton'
documentation_source_path: 'freescalefrdmk64fboard/ref/pushbutton.html'
language: en
---

# Push Button

## Ports

### Output

### **Port\_1** — Logical state of the button scalar

When the switch is pressed, the block outputs `1`.
Otherwise it outputs `0`

**Data Types:** `uint8`

## Parameters

### **Switch** — The switch to read the logical state `SW2` (default) | `SW3`

Select the switch that you want to read the logical state.

### **Sample time** — The frequency to read the state of the button `-1` (default)

Specify how often the Push Button block reads
the state of the button that you select in the **Switch** parameter.
By default, the block inherits its sample time based on the context
of the block within the model.

## Libraries

Simulink Coder Support Package for NXP FRDM-K64F Board

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Read logical state of Push button

The Push Button block reads the logical state
(pressed or released) of the push buttons, SW2 or SW3, that are available
on the FRDM-K64F board. The SW2 button is connected to the PTC6 pin
on the board. The SW3 button is connected to the PTA4 pin on the board.
When the switch is pressed, the block outputs `1`.
Otherwise it outputs `0`.
