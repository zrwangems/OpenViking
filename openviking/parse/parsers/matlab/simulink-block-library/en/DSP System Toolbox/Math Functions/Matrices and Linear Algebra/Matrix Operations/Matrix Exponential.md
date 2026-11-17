---
type: simulink-block
title: 'Matrix Exponential'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'matrixexponential'
documentation_source_path: 'ref/matrixexponential.html'
language: en
---

# Matrix Exponential

## Ports
```yaml
ports:
- name: Input 1
  summary: Data input matrix
  direction: input
  data_types: single | double
- name: Output 1
  summary: Matrix exponential output matrix
  direction: output
  data_types: single | double
```

### Input

### **Input 1** — Data input matrix

Specify the input data as a square matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Output 1** — Matrix exponential output matrix

Matrix exponential output of the input square matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
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

Compute matrix exponential

The Matrix Exponential block computes the matrix exponential of a
square matrix using a scaling and squaring algorithm with a Pade approximation.
