---
type: simulink-block
title: 'Cholesky Factorization'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'choleskyfactorization'
documentation_source_path: 'ref/choleskyfactorization.html'
language: en
---

# Cholesky Factorization

## Ports

### Input

### **S** — Input matrix square matrix

Specify the input matrix as a square matrix. The block output is valid
only when its input has the following characteristics:

- Hermitian — The block does not check whether the input
  is Hermitian. The block uses only the diagonal and upper
  triangle of the input to compute the output.
- Real-valued diagonal entries — The block disregards any
  imaginary component of the input diagonal entries.
- Positive definite — The block notifies you when the
  input is not positive definite as described in the
  **Non-positive definite input** parameter
  description.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **LL'** — Lower and upper triangular factors square matrix

The block outputs a square matrix with lower triangle elements from *L*
and upper triangle elements from
*L*'. The output is not
in the same form as the output of the MATLAB®
`chol` function. In order to convert the output of
the Cholesky Factorization block to the MATLAB form, use the following equation:

```
R = triu(LL');
```

In order to extract the *L* matrix exclusively, pass
the output of the Cholesky Factorization block,
*LL'*, to the Extract Triangular Matrix
block. Setting the **Extract** parameter of the
Extract Triangular Matrix to
`Lower` extracts the *L*
matrix. Setting the **Extract** parameter to
`Upper` extracts the
*L*' matrix.

In this diagram, `LL'` is the output of the
Cholesky Factorization block. Due to round off error,
these equations do not produce a result that is exactly the same as the
MATLAB result.

**Block Output Composed of L and L \***

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Non-positive definite input** — Non-positive definite input `Warning` (default) | `Ignore` | `Error`

Specify the response to nonpositive definite matrix inputs as one of these:

- `Ignore` — Proceed with the
  computation and *do not* issue an alert. The
  output is *not* a valid factorization. A
  partial factorization will be present in the upper left corner
  of the output.
- `Warning` — Display a warning
  message in the MATLAB Command Window, and continue the simulation. The
  output is *not* a valid factorization. A
  partial factorization will be present in the upper left corner
  of the output.
- `Error` — Display an error
  dialog and terminate the simulation.

To generate a valid output, the block algorithm requires a positive
definite input. See the **S** port description for more
information.

**Note**

The **Non-positive definite input** parameter is a
diagnostic parameter. Like all diagnostic parameters on the
Configuration Parameters dialog box, it is set to
`Ignore` in the code generated for this
block by Simulink®
Coder™ code generation software.

## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Factorizations

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

Factor square Hermitian positive definite matrix into triangular components

The Cholesky Factorization block uniquely factors the square Hermitian
positive definite input matrix *S* as

S=LL'

where *L* is a lower triangular square matrix with positive diagonal
elements and *L*' is the Hermitian (complex
conjugate) transpose of *L*.

Note that *L* and *L*' share
the same diagonal in the output matrix. Cholesky factorization requires half the
computation of Gaussian elimination (LU decomposition), and is always stable.
