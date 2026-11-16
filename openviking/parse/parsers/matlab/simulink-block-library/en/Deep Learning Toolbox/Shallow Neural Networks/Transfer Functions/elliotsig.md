---
type: simulink-block
title: 'elliotsig'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Transfer Functions'
documentation_page: 'elliotsig'
documentation_source_path: 'ref/elliotsig.html'
language: en
---

# elliotsig

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

**Introduced in R2012b**

## Description

Elliot symmetric sigmoid transfer function

Transfer functions convert a neural network layer’s net input into its net output.

`A = elliotsig(N)` takes an `S`-by-`Q`
matrix of net input (column) vectors, `N`, and returns an
`S`-by-`Q` matrix, `A`, of output vectors,
where each element of `N` is squashed from the interval `[-inf
inf]` to the interval `[-1 1]` with an “S-shaped”
function.

The advantage of this transfer function over other sigmoids is that it is fast to calculate
on simple computing hardware as it does not require any exponential or trigonometric functions.
Its disadvantage is that it only flattens out for large inputs, so its effect is not as local as
other sigmoid functions. This might result in more training iterations, or require more neurons
to achieve the same accuracy.
