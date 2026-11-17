---
type: simulink-block
title: 'elliot2sig'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'elliot2sig'
documentation_source_path: 'ref/elliot2sig.html'
language: en
---

# elliot2sig

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

**Introduced in R2012b**

## Description

Elliot 2 symmetric sigmoid transfer function

Transfer functions convert a neural network layer’s net input into its net output. This
function is a variation on the original Elliot sigmoid function. It has a steeper slope, closer
to `tansig`, but is not as smooth at the center.

`A = elliot2sig(N)` takes an
`S`-by-`Q` matrix of `S`
`N`-element net input column vectors and returns an
`S`-by-`Q` matrix `A` of output vectors,
where each element of `N` is squashed from the interval `[-inf
inf]` to the interval `[-1 1]` with an “S-shaped”
function.

The advantage of this transfer function over other sigmoids is that it is fast to calculate
on simple computing hardware as it does not require any exponential or trigonometric functions.
Its disadvantage is that it departs from the classic sigmoid shape around zero.
