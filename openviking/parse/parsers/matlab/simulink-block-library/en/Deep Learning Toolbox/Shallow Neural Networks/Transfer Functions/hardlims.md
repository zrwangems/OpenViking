---
type: simulink-block
title: 'hardlims'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'hardlims'
documentation_source_path: 'ref/hardlims.html'
language: en
---

# hardlims

## Ports

Not documented in R2025b.

## Parameters

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

Symmetric hard-limit transfer function

`hardlims` is a neural transfer function. Transfer functions calculate a
layer’s output from its net input.

`A = hardlims(N,FP)` takes `N` and optional function
parameters,

|  |  |
| --- | --- |
| `N` | `S`-by-`Q` matrix of net input (column) vectors |
| `FP` | Struct of function parameters (ignored) |

and returns `A`, the `S`-by-`Q` +1/–1
matrix with +1s where `N` ≥ 0.

`info = hardlims('code')` returns information
according to the code string specified:

`hardlims('name')` returns the name of this function.

`hardlims('output',FP)` returns the `[min max]` output
range.

`hardlims('active',FP)` returns the `[min max]` active
input range.

`hardlims('fullderiv')` returns 1 or 0, depending on whether
`dA_dN` is
`S`-by-`S`-by-`Q` or
`S`-by-`Q`.

`hardlims('fpnames')` returns the names of the function parameters.

`hardlims('fpdefaults')` returns the default function parameters.
