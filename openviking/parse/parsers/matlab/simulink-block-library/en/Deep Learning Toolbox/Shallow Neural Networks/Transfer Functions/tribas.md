---
type: simulink-block
title: 'tribas'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'tribas'
documentation_source_path: 'ref/tribas.html'
language: en
---

# tribas

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

Triangular basis transfer function

`tribas` is a neural transfer function. Transfer functions calculate a
layer’s output from its net input.

`A = tribas(N,FP)` takes `N` and optional function
parameters,

|  |  |
| --- | --- |
| `N` | `S`-by-`Q` matrix of net input (column) vectors |
| `FP` | Struct of function parameters (ignored) |

and returns `A`, an `S`-by-`Q` matrix of
the triangular basis function applied to each element of `N`.

`info = tribas('code')` can take the following
forms to return specific information:

`tribas('name')` returns the name of this function.

`tribas('output',FP)` returns the `[min max]` output
range.

`tribas('active',FP)` returns the `[min max]` active
input range.

`tribas('fullderiv')` returns 1 or 0, depending on whether
`dA_dN` is
`S`-by-`S`-by-`Q` or
`S`-by-`Q`.

`tribas('fpnames')` returns the names of the function parameters.

`tribas('fpdefaults')` returns the default function parameters.
