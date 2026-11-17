---
type: simulink-block
title: 'Reciprocal Condition'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'reciprocalcondition'
documentation_source_path: 'ref/reciprocalcondition.html'
language: en
---

# Reciprocal Condition

## Ports
```yaml
ports:
- name: Input
  summary: Input matrix square matrix
  direction: input
  data_types: single | double
- name: Output
  summary: Reciprocal condition output scalar
  direction: output
  data_types: single | double
```

### Input

### **Input** — Input matrix square matrix

Specify the input matrix as a square matrix.

**Data Types:** `single` | `double`
### Output

### **Output** — Reciprocal condition output scalar

Reciprocal of the condition number for a square input matrix
*A*, returned as a scalar.

If input is well conditioned, the output is near 1.0. If input is
badly conditioned, the output is near 0.0.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Compute reciprocal condition of square matrix in 1-norm

The Reciprocal Condition block computes the reciprocal of the condition
number for a square input matrix *A*.

Here is the equivalent MATLAB® code.

```
y = rcond(A)
```

or

y=1κ=1‖A−1‖1‖A‖1,

where κ is the condition number (κ ≥ 1), and *y* is the scalar
output (0 ≤ *y* < 1).

The matrix 1-norm, ‖A‖1, is the maximum column-sum in the
*M*-by-*M* matrix *A*.

‖A‖1=1≤j≤Mmax∑i=1M|aij|

For a 3-by-3 matrix:
