---
type: simulink-block
title: 'C2000 Ramp Control'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000rampcontrol'
documentation_source_path: 'ref/c2000rampcontrol.html'
language: en
---

# C2000 Ramp Control

## Ports

Not documented in R2025b.

## Parameters

**Maximum delay rate**
:   Value that is multiplied by the sampling loop time period to determine the time
    delay for each ramp step. Valid values are integers greater than 0.

**Minimum limit**
:   Minimum allowable ramp value. If the input falls below this value, it will be
    saturated to this minimum. The smallest value you can enter is the minimum value that
    can be represented in fixed-point data format by the input and output blocks to which
    this Ramp Control block is connected in your model. If you enter a value below this
    minimum, an error occurs at the start of code generation or simulation. For example,
    if your input is in Q29 format, its minimum value is -4.

**Maximum limit**
:   Maximum allowable ramp value. If the input goes above this value, it will be
    reduced to this maximum. The largest value you can enter is the maximum value that can
    be represented in fixed-point data format by the input and output blocks to which this
    Ramp Control block is connected in your model. If you enter a value above this
    maximum, an error occurs at the start of code generation or simulation. For example,
    if your input is in Q29 format, its maximum value is 3.9999....

**Maximum delay rate**
:   Value that is multiplied by the sampling loop time period to determine the time
    delay for each ramp step. Valid values are integers greater than 0.

**Minimum limit**
:   Minimum allowable ramp value. If the input falls below this value, it will be
    saturated to this minimum. The smallest value you can enter is the minimum value that
    can be represented in fixed-point data format by the input and output blocks to which
    this Ramp Control block is connected in your model. If you enter a value below this
    minimum, an error occurs at the start of code generation or simulation. For example,
    if your input is in Q29 format, its minimum value is -4.

**Maximum limit**
:   Maximum allowable ramp value. If the input goes above this value, it will be
    reduced to this maximum. The largest value you can enter is the maximum value that can
    be represented in fixed-point data format by the input and output blocks to which this
    Ramp Control block is connected in your model. If you enter a value above this
    maximum, an error occurs at the start of code generation or simulation. For example,
    if your input is in Q29 format, its maximum value is 3.9999....

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Create ramp-up and ramp-down function

# C2000 Ramp Control

Create ramp-up and ramp-down function

Replace the existing DMC blocks with MCB blocks for improved usability and future
compatibility. It is recommended that you use blocks from Control Algorithm Design (Motor Control Blockset). While these blocks
are not one-to-one replacements, they enable you to achieve the same functionality.

| C28x DMC lib | C28x DMC lib equivalent in MCB |
| --- | --- |
| C2000 Clarke Transformation | Clarke Transform (Motor Control Blockset) |
| C2000 Inverse Park Transformation | Inverse Park Transform (Motor Control Blockset) |
| C2000 Park Transformation | Park Transform (Motor Control Blockset) |
| C2000 PID Controller | PI Controller (Motor Control Blockset) |
| C2000 Ramp Control | Position Generator (Motor Control Blockset) |
| C2000 Ramp Generator | Position Generator (Motor Control Blockset) |
| C2000 Space Vector Generator | PWM Reference Generator (Motor Control Blockset) |
| C2000 Speed Measurement | Speed Measurement (Motor Control Blockset) |

This block implements a ramp-up and ramp-down function. The input is a
`target` value and the outputs are the set point value
(`setpt`) and a `flag`. The `flag`
output is set to `7FFFFFFFh` when the output `setpt` value
reaches the input `target` value. The `target` and
`setpt` values are signed 32-bit fixed-point numbers with Q values
between 16 and 29. The flag is a long number.

The `target` value is compared with the `setpt` value.
If they are not equal, the output `setpt` is adjusted up or down by a fixed
step size (0.0000305).

If the fixed step size is relatively large compared to the `target`
value, the output may oscillate around the `target` value.

- C2000 Ramp Control block
