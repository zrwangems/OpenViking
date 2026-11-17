---
type: simulink-block
title: 'satlin'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'satlin'
documentation_source_path: 'ref/satlin.html'
language: en
---

# satlin

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

**Introduced before R2006a**

## Description

Saturating linear transfer function

`satlin` is a neural transfer function. Transfer functions calculate a
layer’s output from its net input.

`A = satlin(N,FP)` takes two inputs,

|  |  |
| --- | --- |
| `N` | `S`-by-`Q` matrix of net input (column) vectors |
| `FP` | Struct of function parameters (ignored) |

and returns `A`, the `S`-by-`Q` matrix
of `N`’s elements clipped to `[0, 1]`.

`info = satlin('code')` returns useful
information for each supported *`code`* character vector:

`satlin('name')` returns the name of this function.

`satlin('output',FP)` returns the `[min max]` output
range.

`satlin('active',FP)` returns the `[min max]` active
input range.

`satlin('fullderiv')` returns 1 or 0, depending on whether
`dA_dN` is
`S`-by-`S`-by-`Q` or
`S`-by-`Q`.

`satlin('fpnames')` returns the names of the function parameters.

`satlin('fpdefaults')` returns the default function parameters.
