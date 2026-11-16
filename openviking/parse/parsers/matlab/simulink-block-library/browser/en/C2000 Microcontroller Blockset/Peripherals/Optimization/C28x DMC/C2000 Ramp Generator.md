---
type: simulink-block
title: 'C2000 Ramp Generator'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000rampgenerator'
documentation_source_path: 'ref/c2000rampgenerator.html'
language: en
---

# C2000 Ramp Generator

## Ports

Not documented in R2025b.

## Parameters

**Maximum step angle**
:   The maximum step size, which determines the rate of change of the output (i.e.,
    the minimum period of the ramp signal).

    When you enter double-precision floating-point values for parameters in the IQ
    Math blocks, the software converts them to single-precision values that are compatible
    with the behavior on c28x processor.

**Maximum step angle**
:   The maximum step size, which determines the rate of change of the output (i.e.,
    the minimum period of the ramp signal).

    When you enter double-precision floating-point values for parameters in the IQ
    Math blocks, the software converts them to single-precision values that are compatible
    with the behavior on c28x processor.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Generate ramp output

# C2000 Ramp Generator

Generate ramp output

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

This block generates ramp output (`out`) from the slope of the
ramp signal (`gain`), DC offset in the ramp signal
(`offset`), and frequency of the ramp signal (`freq`)
inputs. All of the inputs and output are 32-bit fixed-point
numbers with Q values between 1 and 29.
