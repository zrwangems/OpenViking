---
type: simulink-block
title: 'satlins'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'satlins'
documentation_source_path: 'ref/satlins.html'
language: en
---

# satlins

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

Symmetric saturating linear transfer function

`satlins` is a neural transfer function. Transfer functions calculate a
layer’s output from its net input.

`A = satlins(N,FP)` takes `N` and an optional argument,

|  |  |
| --- | --- |
| `N` | `S`-by-`Q` matrix of net input (column) vectors |
| `FP` | Struct of function parameters (optional, ignored) |

and returns `A`, the `S`-by-`Q` matrix
of `N`’s elements clipped to `[-1, 1]`.

`info = satlins('code')` returns useful
information for each supported *`code`* character vector:

`satlins('name')` returns the name of this function.

`satlins('output',FP)` returns the `[min max]` output
range.

`satlins('active',FP)` returns the `[min max]` active
input range.

`satlins('fullderiv')` returns 1 or 0, depending on whether
`dA_dN` is
`S`-by-`S`-by-`Q` or
`S`-by-`Q`.

`satlins('fpnames')` returns the names of the function parameters.

`satlins('fpdefaults')` returns the default function parameters.
