---
type: simulink-block
title: 'C2000 IQN1 x IQN2'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Optimization / C28x IQmath'
documentation_page: 'c2000iqn1xiqn2'
documentation_source_path: 'ref/c2000iqn1xiqn2.html'
language: en
---

# C2000 IQN1 x IQN2

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

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

Multiply IQ numbers with different Q formats

# C2000 IQN1 x IQN2

Multiply IQ numbers with different Q formats

This block multiples two IQ numbers when the numbers are represented in
different Q formats. The format of the result is specified in the dialog box.

**Note**

The implementation of this block does not call the corresponding Texas Instruments® library function during code generation. The TI function uses a global Q
setting and the MathWorks® code used by this block dynamically adjusts the Q format based on the block
input. See Using the IQmath Library for more
information.

- C2000 IQN1 x IQN2 block
