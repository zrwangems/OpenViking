---
type: simulink-block
title: 'Digital Input'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'digitalinput'
documentation_source_path: '../rtw/freedomboard/ref/digitalinput.html'
language: en
---

# Digital Input

## Ports

Not documented in R2025b.

## Parameters

**Pin**
:   Select a digital pin.

    Make sure not to assign the same pin number to multiple blocks within your
    model.

**Sample time**
:   Specify how often this block reads a digital pin value, in seconds. This
    parameter value defaults to 1/10 second.

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

Read the logical value of a digital input pin

Read the logical value of the selected digital input pin. There are 14 pins on the
FRDM-KL25Z board that you can use as inputs for digital signals, D0-D13. The digital pin
layout for this board is compatible with the standard Arduino Digital Pins.

During simulations without the hardware, this block emits zeroes.
