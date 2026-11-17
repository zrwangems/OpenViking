---
type: simulink-block
title: 'netprod'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Net Input Functions'
documentation_page: 'netprod'
documentation_source_path: 'ref/netprod.html'
language: en
---

# netprod

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

Product net input function

`netprod` is a net input function. Net input functions calculate a layer’s
net input by combining its weighted inputs and biases.

`N = netprod({Z1,Z2,...,Zn})` takes

|  |  |
| --- | --- |
| `Zi` | `S`-by-`Q` matrices in a row cell array |

and returns an element-wise product of `Z1` to
`Zn`.

`info = netprod('code')` returns information
about this function. The following codes are supported:

|  |  |
| --- | --- |
| `'deriv'` | Name of derivative function |
| `'fullderiv'` | Full `N`-by-`S`-by-`Q` derivative = 1, element-wise `S`-by-`Q` derivative = 0 |
| `'name'` | Full name |
| `'fpnames'` | Returns names of function parameters |
| `'fpdefaults'` | Returns default function parameters |
