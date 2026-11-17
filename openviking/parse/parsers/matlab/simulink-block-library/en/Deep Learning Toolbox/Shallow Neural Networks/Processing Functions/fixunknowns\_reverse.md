---
type: simulink-block
title: 'fixunknowns'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Processing Functions'
documentation_page: 'fixunknowns'
documentation_source_path: 'ref/fixunknowns.html'
language: en
---

# fixunknowns

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

Process data by marking rows with unknown values

`fixunknowns` processes matrices by replacing each row containing unknown
values (represented by `NaN`) with two rows of information.

The first row contains the original row, with `NaN` values replaced by the
row’s mean. The second row contains 1 and 0 values, indicating which values in the first row
were known or unknown, respectively.

`[y,ps] = fixunknowns(X)` takes these inputs,

|  |  |
| --- | --- |
| `X` | `N`-by-`Q` matrix |

and returns

|  |  |
| --- | --- |
| `Y` | `M`-by-`Q` matrix with `M - N` rows added |
| `PS` | Process settings that allow consistent processing of values |

`[y,ps] = fixunknowns(X,FP)` takes an empty struct `FP`
of parameters.

`Y = fixunknowns('apply',X,PS)` returns `Y`, given
`X` and settings `PS`.

`X = fixunknowns('reverse',Y,PS)` returns `X`, given
`Y` and settings `PS`.

`name = fixunknowns('name')` returns the name of this process
method.

`fp = fixunknowns('pdefaults')` returns the default process parameter
structure.

`pd = fixunknowns('pdesc')` returns the process parameter
descriptions.

`fixunknowns('pcheck',fp)` throws an error if any parameter is
illegal.
