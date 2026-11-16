---
type: simulink-block
title: 'C2000 Arctangent IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x IQmath'
documentation_page: 'c2000arctangentiqn'
documentation_source_path: 'ref/c2000arctangentiqn.html'
language: en
---

# C2000 Arctangent IQN

## Ports

Not documented in R2025b.

## Parameters

**Function**
:   Type of arc tangent to calculate:

    - `atan2` — Compute the four-quadrant arc
      tangent with output in radians with values from -pi to +pi.
    - `atan2PU` — Compute the four-quadrant arc
      tangent per unit. If `atan2(B,A)` is greater than or equal to 0,
      `atan2PU(B,A) = atan2(B,A)/2*pi`. Otherwise,
      `atan2PU(B,A) = atan2(B,A)/2*pi+1`. The output is in per-unit
      radians with values from 0 to 2\*pi radians.

**Note**

The order of the inputs to the Arctangent IQN block correspond to the Texas Instruments convention, with argument 'A' at the top and 'B' at bottom.

**Function**
:   Type of arc tangent to calculate:

    - `atan2` — Compute the four-quadrant arc
      tangent with output in radians with values from -pi to +pi.
    - `atan2PU` — Compute the four-quadrant arc
      tangent per unit. If `atan2(B,A)` is greater than or equal to 0,
      `atan2PU(B,A) = atan2(B,A)/2*pi`. Otherwise,
      `atan2PU(B,A) = atan2(B,A)/2*pi+1`. The output is in per-unit
      radians with values from 0 to 2\*pi radians.

**Note**

The order of the inputs to the Arctangent IQN block correspond to the Texas Instruments convention, with argument 'A' at the top and 'B' at bottom.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Four-quadrant arc tangent

# C2000 Arctangent IQN

Four-quadrant arc tangent

The Arctangent IQN block computes the four-quadrant arc tangent of the IQ number
inputs and produces IQ number output.

**Note**

The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The Texas Instruments function uses a global Q setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the block
input. See Using the IQmath Library for more
information.

- C2000 Arctangent IQN block
