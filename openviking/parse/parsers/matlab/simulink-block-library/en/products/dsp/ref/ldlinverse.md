---
type: simulink-block
title: 'LDL Inverse'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Linear Algebra / Matrix Inverses'
documentation_page: 'ldlinverse'
documentation_source_path: 'ref/ldlinverse.html'
language: en
---

# LDL Inverse

## Ports

### Input

### **Input** — Input matrix square matrix

Specify the input as a square matrix *S* that is
Hermitian positive definite. When the input is not positive definite,
the block reacts with the behavior specified by the
**Non-positive definite input** parameter. For more
details, see the description of the **Non-positive definite
input** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Output** — Matrix inverse square matrix

Inverse of the Hermitian positive definite input matrix
*S*, returned as a square matrix. Here is the
equation for LDL factorization.

S−1=(LDL\*)−1

*L* is a lower triangular square matrix with unity
diagonal elements, *D* is a diagonal matrix, and
*L*\* is the Hermitian
(complex conjugate) transpose of *L*. Only the diagonal
and lower triangle of the input matrix are used, and any imaginary
component of the diagonal entries is disregarded.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Non-positive definite input** — Non-positive definite input `Warning` (default) | `Ignore` | `Error`

Specify the response to nonpositive definite matrix input as
`Ignore`, `Warning`,
or `Error`.

The algorithm requires that the input be Hermitian positive definite. When
the input is not positive definite, the block reacts with the behavior
specified by the **Non-positive definite input** parameter.
The following options are available:

- `Ignore` — Proceed with the
  computation and do not issue an alert. The output is not a valid
  inverse.
- `Warning` — Display a warning
  message in the MATLAB® command window, and continue the simulation. The
  output is not a valid inverse.
- `Error` — Display an error dialog
  and terminate the simulation.

**Note**

The **Non-positive definite input** parameter is a
diagnostic parameter. Like all diagnostic parameters on the
Configuration Parameters dialog, it is set to
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

Compute inverse of Hermitian positive definite matrix using LDL factorization

The LDL Inverse block computes the inverse of the Hermitian positive definite
input matrix *S* by performing an LDL factorization.

S−1=(LDL\*)−1

*L* is a lower triangular square matrix with unity diagonal elements,
*D* is a diagonal matrix, and
*L*\* is the Hermitian (complex
conjugate) transpose of *L*. Only the diagonal and lower triangle of
the input matrix are used, and any imaginary component of the diagonal entries is
disregarded.

LDL factorization requires half the computation of Gaussian elimination (LU decomposition), and is always stable. It is more efficient than Cholesky factorization because it avoids computing the square roots of the diagonal elements.
