---
type: simulink-block
title: 'C2000 Float to IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000floattoiqn'
documentation_source_path: 'ref/c2000floattoiqn.html'
language: en
---

# C2000 Float to IQN

## Ports

Not documented in R2025b.

## Parameters

**Q value**
:   Q value from 1 to 30 that specifies the precision of the output

**Q value**
:   Q value from 1 to 30 that specifies the precision of the output

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Convert floating-point number to IQ number

# C2000 Float to IQN

Convert floating-point number to IQ number

This block converts a floating-point number to an IQ number. The Q value of the
output is specified in the dialog.

**Note**

The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The TI function uses a global Q
setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the block
input. See Using the IQmath Library for more
information.

- C2000 Float to IQN block
