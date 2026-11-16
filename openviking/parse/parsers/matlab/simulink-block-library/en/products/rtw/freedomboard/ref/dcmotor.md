---
type: simulink-block
title: 'DC Motor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'dcmotor'
documentation_source_path: 'freedomboard/ref/dcmotor.html'
language: en
---

# DC Motor

## Ports

Not documented in R2025b.

## Parameters

**DC motor**
:   Select the DC Motor A or DC Motor B.

    When you select DC Motor B, make sure that you do not use the RGB LED block in the same model.

    The PTC2 pin, used in DC Motor B, and the LED\_BLUE (PTD1) pin, used in the RGB
    LED block for the blue LED, belong to Timer 0 Channel 1. In a Simulink® model, using pins that belong to the same timer channel combination
    results in a pin conflict error. Hence, when you build a model using DC Motor B and
    the RGB LED block, you receive the pin conflict error message. As a result, you are
    restricted even from using the LED\_RED pin and the LED\_GREEN pin from the RGB LED
    block. As an alternative to the RGB LED block, you can use two PWM Output blocks and set their output pins to LED\_RED and LED\_GREEN
    respectively.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Drive a DC motor in either direction

The NXP TFC shield can have up to two DC motors connected to it. The DC Motor Block
drives a DC motor with torque between full reverse (-1.0) and full forward (1.0). The
resulting speed and torque depends on the current state of the battery connected to the
TFC shield.

During simulations without the hardware, this block does nothing.
