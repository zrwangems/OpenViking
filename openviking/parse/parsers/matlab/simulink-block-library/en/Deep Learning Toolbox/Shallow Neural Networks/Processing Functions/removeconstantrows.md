---
type: simulink-block
title: 'removeconstantrows'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'removeconstantrows'
documentation_source_path: 'ref/removeconstantrows.html'
language: en
---

# removeconstantrows

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

**Introduced in R2006a**

## Description

Process matrices by removing rows with constant values

`removeconstantrows` processes matrices by removing rows with constant
values.

`[Y,PS] = removeconstantrows(X,max_range)` takes `X`
and an optional parameter,

|  |  |
| --- | --- |
| `X` | `N`-by-`Q` matrix |
| `max_range` | Maximum range of values for row to be removed (default is 0) |

and returns

|  |  |
| --- | --- |
| `Y` | `M`-by-`Q` matrix with `N` `-` `M` rows deleted |
| `PS` | Process settings that allow consistent processing of values |

`[Y,PS] = removeconstantrows(X,FP)` takes parameters as a struct:
`FP.max_range`.

`Y = removeconstantrows('apply',X,PS)` returns `Y`,
given `X` and settings `PS`.

`X = removeconstantrows('reverse',Y,PS)` returns `X`,
given `Y` and settings `PS`.

Any `NaN` values in the input matrix are treated as missing data, and are
not considered as unique values. So, for example, `removeconstantrows`
removes the first row from the matrix `[1 1 1 NaN; 1 1 1 2]`.
