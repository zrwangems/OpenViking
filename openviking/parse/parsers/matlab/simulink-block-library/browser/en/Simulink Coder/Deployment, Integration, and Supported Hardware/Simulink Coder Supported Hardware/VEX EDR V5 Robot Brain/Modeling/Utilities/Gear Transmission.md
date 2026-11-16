---
type: simulink-block
title: 'Gear Transmission'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Utilities'
documentation_page: 'geartransmission'
documentation_source_path: 'vexv5/ref/geartransmission.html'
language: en
---

# Gear Transmission

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Set a scalar value (1 to 4) based on input values

Set a scalar value in the range 1 to 4, based on the signals to the input ports. The
input ports, Up and Down receive a logical value from a digital button. When the Up value is
HIGH (1) then the Gear Transmission block output is incremented by 1. If the Down value is
HIGH (1), the Gear Transmission block output is decremented by 1. If neither of the input
values change, the gear value does not change. The gear value does not change to go below 1
or above 4, even if the input values change.

For instance, use this block in a model to control the motor speed of robot by providing
the gear output value as the scaling factor to the Gamepad Joystick signal. This value can
scale up or down the speed value of the motors for the range of the joystick.
