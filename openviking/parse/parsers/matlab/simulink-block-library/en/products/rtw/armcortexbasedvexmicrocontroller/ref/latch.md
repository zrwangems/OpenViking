---
type: simulink-block
title: 'Latch'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Utilities'
documentation_page: 'latch'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/latch.html'
language: en
---

# Latch

## Ports

Not documented in R2025b.

## Parameters

**Check if Initial Output is 1. Uncheck if 0**
:   This parameter is applicable to simulation behavior only. If the initial output
    value must be 1, select this check box. Otherwise, the initial output value is
    0.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Latch the logical value based on the change in the input signal

Latch the logical value based on the change in the input signal between a zero and
nonzero value. The Latch switches between 1 and 0 for every rising edge transition of the
input signal. When you use this block to latch the output of a Gamepad Button block, the
output switches between 1 and 0 when the specified button is pressed. When the button is
released, the output does not switch. For instance, use this block in a model to press a
button to latch the angular position of the robot arm or claw to a specific value. Switch to
the original position by pressing the button again.
