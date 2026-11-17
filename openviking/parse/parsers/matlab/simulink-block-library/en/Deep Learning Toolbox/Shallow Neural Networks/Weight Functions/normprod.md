---
type: simulink-block
title: 'normprod'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Weight Functions'
documentation_page: 'normprod'
documentation_source_path: 'ref/normprod.html'
language: en
---

# normprod

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

Normalized dot product weight function

`normprod` is a weight function. Weight functions apply weights to an
input to get weighted inputs.

`Z = normprod(W,P,FP)` takes these inputs,

|  |  |
| --- | --- |
| `W` | `S`-by-`R` weight matrix |
| `P` | `R`-by-`Q` matrix of `Q` input (column) vectors |
| `FP` | Row cell array of function parameters (optional, ignored) |

and returns the `S`-by-`Q` matrix of normalized dot
products.

`dim = normprod('size',S,R,FP)` takes the layer dimension
`S`, input dimension `R`, and function parameters, and
returns the weight size [`S`-by-`R`].

`dw = normprod('dz_dw',W,P,Z,FP)` returns the derivative of
`Z` with respect to `W`.
