---
type: simulink-block
title: 'poslin'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'poslin'
documentation_source_path: 'ref/poslin.html'
language: en
---

# poslin

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

Positive linear transfer function

`poslin` is a neural transfer function. Transfer functions calculate a
layer’s output from its net input.

`A = poslin(N,FP)` takes `N` and optional function
parameters,

|  |  |
| --- | --- |
| `N` | `S`-by-`Q` matrix of net input (column) vectors |
| `FP` | Struct of function parameters (ignored) |

and returns `A`, the `S`-by-`Q` matrix
of `N`’s elements clipped to `[0, inf]`.

`info = poslin('code')` returns information
about this function. The following codes are supported:

`poslin('name')` returns the name of this function.

`poslin('output',FP)` returns the `[min max]` output
range.

`poslin('active',FP)` returns the `[min max]` active
range.

`poslin('fullderiv')` returns 1 or 0, depending on whether
`dA_dN` is
`S`-by-`S`-by-`Q` or
`S`-by-`Q`.

`poslin('fpnames')` returns the names of the function parameters.

`poslin('fpdefaults')` returns the default function parameters.
