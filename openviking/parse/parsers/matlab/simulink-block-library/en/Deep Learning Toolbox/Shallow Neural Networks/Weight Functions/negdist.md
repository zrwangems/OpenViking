---
type: simulink-block
title: 'negdist'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Weight Functions'
documentation_page: 'negdist'
documentation_source_path: 'ref/negdist.html'
language: en
---

# negdist

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

Negative distance weight function

`negdist` is a weight function. Weight functions apply weights to an input
to get weighted inputs.

`Z = negdist(W,P)` takes these inputs,

|  |  |
| --- | --- |
| `W` | `S`-by-`R` weight matrix |
| `P` | `R`-by-`Q` matrix of `Q` input (column) vectors |
| `FP` | Row cell array of function parameters (optional, ignored) |

and returns the `S`-by-`Q` matrix of negative vector
distances.

`dim = negdist('size',S,R,FP)` takes the layer dimension
`S`, input dimension `R`, and function parameters, and
returns the weight size [`S`-by-`R`].

`dw = negdist('dz_dw',W,P,Z,FP)` returns the derivative of
`Z` with respect to `W`.
