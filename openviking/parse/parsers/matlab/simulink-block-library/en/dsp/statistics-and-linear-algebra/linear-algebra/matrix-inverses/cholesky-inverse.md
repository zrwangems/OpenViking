---
type: simulink-block
title: 'Cholesky Inverse'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Linear Algebra / Matrix Inverses'
documentation_page: 'choleskyinverse'
documentation_source_path: 'ref/choleskyinverse.html'
language: en
---

# Cholesky Inverse

## Ports

### Input

### **Input** — Input matrix square matrix

Specify the input as a square matrix *S* that is Hermitian positive
definite. When the input is not positive definite, the block behaves as
specified by the **Non-positive definite input**
parameter. For more details, see the description of the
**Non-positive definite input** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Output** — Matrix inverse square matrix

Inverse of the Hermitian positive definite input matrix *S*, returned
as a square matrix. This is the equation for Cholesky
factorization.

S−1=(LL∗)−1

*L* is a lower triangular square matrix with positive diagonal elements
and *L*\* is the Hermitian
(complex conjugate) transpose of *L*. The block uses
only the diagonal and upper triangle of the input matrix and disregards
any imaginary component of the diagonal entries. Cholesky factorization
requires half the computation of Gaussian elimination (LU decomposition)
and is always stable.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Non-positive definite input** — Non-positive definite input `Warning` (default) | `Ignore` | `Error`

Specify the response to non-positive definite matrix input as
`Ignore`, `Warning`,
or `Error`.

The algorithm requires that the input be Hermitian positive definite. When the input is
not positive definite, the block behaves as specified by the
**Non-positive definite input** parameter. When you set
this parameter to:

- `Ignore` — The block proceeds with
  the computation and does not issue an alert. The output is not a
  valid inverse.
- `Warning` — The block displays a
  warning message in the MATLAB® command window and continues the simulation. The
  output is not a valid inverse.
- `Error` — The block displays an
  error dialog box and terminates the simulation.

**Note**

The **Non-positive definite input** parameter is a
diagnostic parameter. Like all diagnostic parameters in the
Configuration Parameters dialog box, it is set to
`Ignore` in the code generated for this
block by Simulink®
Coder™ code generation software.

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

Compute inverse of Hermitian positive definite matrix using Cholesky factorization

The Cholesky Inverse block computes the inverse of the Hermitian
positive definite input matrix *S* by performing Cholesky
factorization.

S−1=(LL∗)−1

*L* is a lower triangular square matrix with positive diagonal elements and
*L*\* is the Hermitian (complex
conjugate) transpose of *L*. The block uses only the diagonal and upper
triangle of the input matrix and disregards any imaginary component of the diagonal
entries. Cholesky factorization requires half the computation of Gaussian elimination
(LU decomposition) and is always stable.
