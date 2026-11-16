---
type: simulink-block
title: 'C2000 Trig Fcn IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x IQmath'
documentation_page: 'c2000trigfcniqn'
documentation_source_path: 'ref/c2000trigfcniqn.html'
language: en
---

# C2000 Trig Fcn IQN

## Ports

Not documented in R2025b.

## Parameters

**Function**
:   Type of trigonometric function to calculate:

    - `_IQsin` — Compute the sine
      `(sin(A))`, where A is in radians.
    - `_IQsinPU` — Compute the sine per unit
      `(sin(2*pi*A))`, where A is in per-unit radians.
    - `_IQcos` — Compute the cosine
      `(cos(A))`, where A is in radians.
    - `_IQcosPU` — Compute the cosine per unit
      `(cos(2*pi*A))`, where A is in per-unit radians.

**Function**
:   Type of trigonometric function to calculate:

    - `_IQsin` — Compute the sine
      `(sin(A))`, where A is in radians.
    - `_IQsinPU` — Compute the sine per unit
      `(sin(2*pi*A))`, where A is in per-unit radians.
    - `_IQcos` — Compute the cosine
      `(cos(A))`, where A is in radians.
    - `_IQcosPU` — Compute the cosine per unit
      `(cos(2*pi*A))`, where A is in per-unit radians.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Sine, cosine, or arc tangent of IQ number

# C2000 Trig Fcn IQN

Sine, cosine, or arc tangent of IQ number

This block calculates basic trigonometric functions and returns the result as an
IQ number. Valid Q values for `_IQsinPU` and `_IQcosPU`
are 1 to 30. For all others, valid Q values are from 1 to 29.

**Note**

The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The TI function uses a global Q
setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the block
input. See Using the IQmath Library for more
information.

- C2000 Trig Fcn IQN block
