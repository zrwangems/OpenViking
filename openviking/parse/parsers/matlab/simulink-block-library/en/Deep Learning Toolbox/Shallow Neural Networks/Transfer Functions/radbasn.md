---
type: simulink-block
title: 'radbasn'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'radbasn'
documentation_source_path: 'ref/radbasn.html'
language: en
---

# radbasn

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

**Introduced in R2010b**

## Description

Normalized radial basis transfer function

`radbasn` is a neural transfer function. Transfer functions calculate a
layer’s output from its net input. This function is equivalent to radbas, except that output
vectors are normalized by dividing by the sum of the pre-normalized values.

`A = radbasn(N,FP)` takes one or two inputs,

|  |  |
| --- | --- |
| `N` | `S`-by-`Q` matrix of net input (column) vectors |
| `FP` | Struct of function parameters (ignored) |

and returns `A`, an `S`-by-`Q` matrix of
the radial basis function applied to each element of `N`.
