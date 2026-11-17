---
type: simulink-block
title: 'C2000 IQN x IQN'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000iqnxiqn'
documentation_source_path: 'ref/c2000iqnxiqn.html'
language: en
---

# C2000 IQN x IQN

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Multiply option**
:   Type of multiplication to perform:

    - `Multiply` — Multiply the numbers.
    - `Multiply with Rounding` — Multiply the
      numbers and round the result.
    - `Multiply with Rounding and Saturation` —
      Multiply the numbers and round and saturate the result to the maximum
      value.

**Multiply option**
:   Type of multiplication to perform:

    - `Multiply` — Multiply the numbers.
    - `Multiply with Rounding` — Multiply the
      numbers and round the result.
    - `Multiply with Rounding and Saturation` —
      Multiply the numbers and round and saturate the result to the maximum
      value.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Multiply IQ numbers with same Q format

# C2000 IQN x IQN

Multiply IQ numbers with same Q format

This block multiplies two IQ numbers. Optionally, it can also round and saturate
the result.

**Note**

The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The TI function uses a global Q
setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the block
input. See Using the IQmath Library for more
information.

- C2000 IQN x IQN block
