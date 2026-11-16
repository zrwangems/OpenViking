---
type: simulink-block
title: 'Servo Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'servowrite'
documentation_source_path: 'freedomboard/ref/servowrite.html'
language: en
---

# Servo Write

## Ports

Not documented in R2025b.

## Parameters

**Servo**
:   Select Servo 0 or Servo 1 motor.

**Minimum angle (degrees)**
:   Specify the minimum angle achievable by the Servo motor.

**Maximum angle (degrees)**
:   Specify the maximum angle achievable by the Servo motor.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Drive the servo motor to the specified angle

The NXP TFC shield can have up to two servos connected to it.

The Servo Write block drives the servo using a PWM signal with a period
of 20ms. This block controls a servo motor between specified minimum and maximum angles.
The block clips any value outside the specified range.

During simulations without the hardware, this block does nothing.
