---
type: simulink-block
title: 'LU Solver'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'lusolver'
documentation_source_path: 'ref/lusolver.html'
language: en
---

# LU Solver

## Ports

### Input

### **A** — Input *A* matrix *M*-by-*M* matrix

Specify the input *M*-by-*M* square matrix
*A* through this port. Inputs *A*
and *B* must have the same number of rows.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **B** — *B* matrix *M*-by-*N* matrix | *M*-by-1 vector

Specify the *B* matrix in the *AX* =
*B* equation as an
*M*-by-*N* matrix or an
*M*-by-1 vector.

When you specify an *M*-by-1 vector, the block treats
the length-*M* unoriented vector input at port
**B** as an *M*-by-1 matrix.
Inputs *A* and *B* must have the same
number of rows.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **X** — Solution to system of equations *M*-by-*N* matrix | *M*-by-1 matrix

The block returns the output as an
*M*-by-*N* matrix or a
*M*-by-1 matrix. The size of *X*
matrix is same as the size of the *B* matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

Not documented in R2025b.

## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Linear System Solvers

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

Solve AX = B when A is a square matrix

The LU Solver block solves the linear system
*A**X* = *B* by applying LU
factorization, where:

- *A* is an *M*-by-*M*
  square matrix input through the **A** port.
- *B* is an *M*-by-*N*
  matrix input through the **B** port.
- *X* is the *M*-by-*N*
  output matrix and is the unique solution to the equations.
