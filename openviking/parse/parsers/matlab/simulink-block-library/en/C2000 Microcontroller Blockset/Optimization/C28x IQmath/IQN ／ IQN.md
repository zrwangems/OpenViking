---
type: simulink-block
title: 'C2000 Division IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000divisioniqn'
documentation_source_path: 'ref/c2000divisioniqn.html'
language: en
---

# C2000 Division IQN

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Divide IQ numbers

This block divides two numbers that use the same Q format, using the
Newton-Raphson technique. The resulting quotient uses the same Q format at the inputs.

**Note**

The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The TI function uses a global Q
setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the block
input. See Using the IQmath Library for more
information.
