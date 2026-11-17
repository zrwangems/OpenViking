---
type: simulink-block
title: 'mapstd'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'mapstd'
documentation_source_path: 'ref/mapstd.html'
language: en
---

# mapstd

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

Process matrices by mapping each row’s means to 0 and deviations to 1

`mapstd` processes matrices by transforming the mean and standard
deviation of each row to `ymean` and `ystd`.

`[Y,PS] = mapstd(X,ymean,ystd)` takes `X` and optional
parameters,

|  |  |
| --- | --- |
| `X` | `N`-by-`Q` matrix |
| `ymean` | Mean value for each row of `Y` (default is 0) |
| `ystd` | Standard deviation for each row of `Y` (default is 1) |

and returns

|  |  |
| --- | --- |
| `Y` | `N`-by-`Q` matrix |
| `PS` | Process settings that allow consistent processing of values |

`[Y,PS] = mapstd(X,FP)` takes parameters as a struct:
`FP.ymean`, `FP.ystd`.

`Y = mapstd('apply',X,PS)` returns `Y`, given
`X` and settings `PS`.

`X = mapstd('reverse',Y,PS)` returns `X`, given
`Y` and settings `PS`.

`dx_dy = mapstd('dx_dy',X,Y,PS)` returns the reverse derivative.
