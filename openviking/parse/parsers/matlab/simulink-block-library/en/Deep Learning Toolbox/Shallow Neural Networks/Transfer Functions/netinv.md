---
type: simulink-block
title: 'netinv'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'netinv'
documentation_source_path: 'ref/netinv.html'
language: en
---

# netinv

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

**Introduced in R2006a**

## Description

Inverse transfer function

`netinv` is a transfer function. Transfer functions calculate a layer’s
output from its net input.

`A = netinv(N,FP)` takes inputs

|  |  |
| --- | --- |
| `N` | `S`-by-`Q` matrix of net input (column) vectors |
| `FP` | Struct of function parameters (ignored) |

and returns `1/N`.

`info = netinv('code')` returns information
about this function. The following codes are supported:

`netinv('name')` returns the name of this function.

`netinv('output',FP)` returns the [`min`
`max`] output range.

`netinv('active',FP)` returns the [`min`
`max`] active input range.

`netinv('fullderiv')` returns 1 or 0, depending on whether
`dA_dN` is
`S`-by-`S`-by-`Q` or
`S`-by-`Q`.

`netinv('fpnames')` returns the names of the function parameters.

`netinv('fpdefaults')` returns the default function parameters.
