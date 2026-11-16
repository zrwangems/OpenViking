---
type: simulink-block
title: 'C2000 Square Root IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000squarerootiqn'
documentation_source_path: 'ref/c2000squarerootiqn.html'
language: en
---

# C2000 Square Root IQN

## Ports

Not documented in R2025b.

## Parameters

**Function**
:   Whether to calculate the square root or inverse square root

    - `Square root (_sqrt)` — Compute the square
      root.
    - `Inverse square root (_isqrt)` — Compute the
      inverse square root.

**Function**
:   Whether to calculate the square root or inverse square root

    - `Square root (_sqrt)` — Compute the square
      root.
    - `Inverse square root (_isqrt)` — Compute the
      inverse square root.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Square root or inverse square root of IQ number

# C2000 Square Root IQN

Square root or inverse square root of IQ number

This block calculates the square root or inverse square root of an IQ number and
returns an IQ number of the same Q format. The block uses table lookup and a Newton-Raphson
approximation.

Negative inputs to this block return a value of zero.

**Note**

The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The TI function uses a global Q
setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the block
input. See Using the IQmath Library for more
information.
