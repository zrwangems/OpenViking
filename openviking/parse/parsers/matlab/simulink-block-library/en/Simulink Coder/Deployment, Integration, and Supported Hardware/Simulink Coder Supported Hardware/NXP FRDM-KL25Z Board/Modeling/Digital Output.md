---
type: simulink-block
title: 'Digital Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'digitaloutput'
documentation_source_path: 'freedomboard/ref/digitaloutput.html'
language: en
---

# Digital Output

## Ports

Not documented in R2025b.

## Parameters

**Pin**
:   Select the digital pin.

    Make sure not to assign the same pin number to multiple blocks within your
    model.

**View pin map**
:   Click on this button to open a snapshot of the board with a reference to the
    GPIO pins.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Set the logical value of a digital output pin

Set the logical value of the selected digital output pin. There are 14 pins on the
FRDM-KL25Z board that you can use as output for digital signals, D0-D13. The digital pin
layout for this board is compatible with the standard Arduino Digital Pins.

During simulations without the hardware, this block does nothing.
