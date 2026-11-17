---
type: simulink-block
title: 'LU Inverse'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Inverses'
documentation_page: 'luinverse'
documentation_source_path: 'ref/luinverse.html'
language: en
---

# LU Inverse

## Ports
```yaml
ports:
- name: Input
  summary: Input square matrix square matrix
  direction: input
  data_types: single | double
- name: Output
  summary: Matrix inverse square matrix
  direction: output
  data_types: single | double
```

### Input

### **Input** — Input square matrix square matrix

Specify the input as an *M*-by-*M*
square matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Output** — Matrix inverse square matrix

Matrix inverse, returned as an
*M*-by-*M* square matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Inverses

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

Compute inverse of square matrix using LU factorization

The LU Inverse block computes the inverse of the square input matrix
*A* by factoring and inverting its row-pivoted variant
*A**p*.

Ap−1=(LU)−1

*L* is a lower triangular square matrix with unity diagonal elements,
and *U* is an upper triangular square matrix. The block outputs the
inverse matrix *A*-1.
