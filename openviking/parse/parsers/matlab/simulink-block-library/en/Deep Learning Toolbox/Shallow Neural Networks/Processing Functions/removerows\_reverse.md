---
type: simulink-block
title: 'removerows'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'removerows'
documentation_source_path: 'ref/removerows.html'
language: en
---

# removerows

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

Process matrices by removing rows with specified indices

`removerows` processes matrices by removing rows with the specified
indices.

`[Y,PS] = removerows(X,'ind',ind)` takes `X` and an
optional parameter,

|  |  |
| --- | --- |
| `X` | `N`-by-`Q` matrix |
| `ind` | Vector of row indices to remove (default is `[]`) |

and returns

|  |  |
| --- | --- |
| `Y` | `M`-by-`Q` matrix, where `M == N-length(ind)` |
| `PS` | Process settings that allow consistent processing of values |

`[Y,PS] = removerows(X,FP)` takes parameters as a struct:
`FP.ind`.

`Y = removerows('apply',X,PS)` returns `Y`, given
`X` and settings `PS`.

`X = removerows('reverse',Y,PS)` returns `X`, given
`Y` and settings `PS`.

`dx_dy = removerows('dx',X,Y,PS)` returns the
`M`-by-`N`-by-`Q` derivative of
`Y` with respect to `X`.

`dx_dy = removerows('dx',X,[],PS)` returns the derivative, less
efficiently.

`name = removerows('name')` returns the name of this process
method.

`fp = removerows('pdefaults')` returns the default process parameter
structure.

`names = removerows('pdesc')` returns the process parameter
descriptions.

`removerows('pcheck',FP)` throws an error if any parameter is
illegal.
