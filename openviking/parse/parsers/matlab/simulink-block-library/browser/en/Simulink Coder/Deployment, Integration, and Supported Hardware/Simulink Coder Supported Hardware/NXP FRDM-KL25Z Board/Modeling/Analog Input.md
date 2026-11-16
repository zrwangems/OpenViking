---
type: simulink-block
title: 'Analog Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'analoginput'
documentation_source_path: 'freedomboard/ref/analoginput.html'
language: en
---

# Analog Input

## Ports

Not documented in R2025b.

## Parameters

**Analog pin**
:   Select the analog pin from A0-A5 to measure the voltage. Make sure not to select
    the same pin number for multiple blocks in your model.

**Sample time**
:   Specify how often this block reads the pin value, in seconds.

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

Measure the voltage of an analog input pin

Measure the voltage of the selected analog input pin A0-A5. The block output emits a
value in the range 0.0 to 1.0 with 16 bit resolution. The maximum voltage is determined by
the input reference voltage, VREFH, which defaults to a 3.3 Volt source.

During simulations without the hardware, this block emits zeroes.
