---
type: simulink-block
title: 'radbas'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'radbas'
documentation_source_path: 'ref/radbas.html'
language: en
---

# radbas

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

Radial basis transfer function

`radbas` is a neural transfer function. Transfer functions calculate a
layer’s output from its net input.

`A = radbas(N,FP)` takes one or two inputs,

|  |  |
| --- | --- |
| `N` | `S`-by-`Q` matrix of net input (column) vectors |
| `FP` | Struct of function parameters (ignored) |

and returns `A`, an `S`-by-`Q` matrix of
the radial basis function applied to each element of `N`.
