---
type: simulink-block
title: 'processpca'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'processpca'
documentation_source_path: 'ref/processpca.html'
language: en
---

# processpca

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

Process columns of matrix with principal component analysis

`processpca` processes matrices using principal component analysis so that
each row is uncorrelated, the rows are in the order of the amount they contribute to total
variation, and rows whose contribution to total variation are less than
`maxfrac` are removed.

`[Y,PS] = processpca(X,maxfrac)` takes `X` and an
optional parameter,

|  |  |
| --- | --- |
| `X` | `N`-by-`Q` matrix |
| `maxfrac` | Maximum fraction of variance for removed rows (default is 0) |

and returns

|  |  |
| --- | --- |
| `Y` | `M`-by-`Q` matrix with `N` `-` `M` rows deleted |
| `PS` | Process settings that allow consistent processing of values |

`[Y,PS] = processpca(X,FP)` takes parameters as a struct:
`FP.maxfrac`.

`Y = processpca('apply',X,PS)` returns `Y`, given
`X` and settings `PS`.

`X = processpca('reverse',Y,PS)` returns `X`, given
`Y` and settings `PS`.

`name = processpca('name')` returns the name of this process
method.

`fp = processpca('pdefaults')` returns default process parameter
structure.

`names = processpca('pdesc')` returns the process parameter
descriptions.

`processpca('pcheck',fp);` throws an error if any parameter is
illegal.
