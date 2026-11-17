---
type: simulink-block
title: 'C2000 Saturate IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000saturateiqn'
documentation_source_path: 'ref/c2000saturateiqn.html'
language: en
---

# C2000 Saturate IQN

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Upper Limit**
:   Maximum real-world value to which to saturate

**Lower Limit**
:   Minimum real-world value to which to saturate

**Upper Limit**
:   Maximum real-world value to which to saturate

**Lower Limit**
:   Minimum real-world value to which to saturate
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Saturate IQ number

# C2000 Saturate IQN

Saturate IQ number

This block saturates an input IQ number to the specified upper and lower limits.
The returned value is an IQ number of the same Q value as the input.

**Note**

The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The TI function uses a global Q
setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the block
input. See Using the IQmath Library for more
information.

- C2000 Saturate IQN block
