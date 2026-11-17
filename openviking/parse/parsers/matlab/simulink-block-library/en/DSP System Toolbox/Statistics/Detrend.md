---
type: simulink-block
title: 'Detrend'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'detrend'
documentation_source_path: 'ref/detrend.html'
language: en
---

# Detrend

## Ports
```yaml
ports:
- name: Input
  summary: Input data vector
  direction: input
  data_types: single | double
- name: Output
  summary: Output data column vector
  direction: output
  data_types: single | double
```

### Input

### **Input** — Input data vector

Input data, specified as a vector. The block removes the straight line
that best fits the data in the least squares sense.

**Data Types:** `single` | `double`
### Output

### **Output** — Output data column vector

Output data, returned as a column vector. The block returns the
remaining data after removing the straight line that best fits the data
in the least squares sense.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

DSP System Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Remove linear trend from vectors

The Detrend block removes a linear trend from the length-*M* input
vector, *u*, by subtracting the straight line that best fits the data in the least squares sense.

The least squares line, *û* = *ax* +
*b*, is the line with parameters *a* and
*b* that minimizes the quantity

∑i=1M(ui−u^i)2

for *M* evenly-spaced values of *x*, where
*ui* is the *i*th
element in the input vector. The output, *y* =
*u*-*û*, is always an *M*-by-1 column vector.
