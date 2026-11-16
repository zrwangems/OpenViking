---
type: simulink-block
title: 'QR Factorization'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Factorizations'
documentation_page: 'qrfactorization'
documentation_source_path: 'ref/qrfactorization.html'
language: en
---

# QR Factorization

## Ports

### Input

### **A** — Input vector | matrix

Specify the input as a vector or a matrix of size
*M*-by-*N*.

The block treats length-*M* unoriented vector input
as an *M*-by-1 matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Q** — Orthonormal component *Q* of QR factorization vector | matrix

Orthonormal component *Q* of QR factorization,
returned as a vector or a matrix. The size of *Q*
depends on the setting of the **Output size**
parameter:

The size of *Q* depends on the setting of the
**Output size** parameter:

- When you select `Economy` for the output
  size, *Q* is an
  *M*-by-`min`(*M*,*N*)
  unitary matrix.

  ```
  [Q R E] = qr(A,0)   % Equivalent MATLAB code
  ```
- When you select `Full` for the output size,
  *Q* is an
  *M*-by-*M* unitary
  matrix.

  ```
  [Q R E] = qr(A)      % Equivalent MATLAB code
  ```

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **R** — Upper triangular component *R* of QR factorization vector | matrix

Upper triangular component *R* of QR factorization,
returned as a vector or a matrix.

The size of *R* depends on the setting of the
**Output size** parameter:

- When you select `Economy` for the output
  size, *R* is a
  `min`(*M*,*N*)-by-*N*
  upper-triangular matrix.

  ```
  [Q R E] = qr(A,0)   % Equivalent MATLAB code
  ```
- When you select `Full` for the output size,
  *R* is a
  *M*-by-*N*
  upper-triangular matrix.

  ```
  [Q R E] = qr(A)      % Equivalent MATLAB code
  ```

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **E** — Column permutation vector vector

Column permutation vector *E* of length
*N*, where *N* is the number of
columns in the input matrix.

The block selects a column permutation vector which ensures that the
diagonal elements of matrix *R* are arranged in order
of decreasing magnitude.

|ri+1,j+1|<|ri,j|        i=j

For more details on how the block uses this vector, see Algorithms.

**Data Types:** `single` | `double`

## Parameters

### **Output size** — Output size `Economy` (default) | `Full`

Specify the size of output matrices *Q* and
*R*:

- `Economy` — When you select this
  output size, the block outputs an
  *M*-by-min(*M*,*N*)
  unitary matrix *Q* and a
  min(*M*,*N*)-by-*N*
  upper-triangular matrix *R*.
- `Full` — When you select this
  output size, the block outputs an
  *M*-by-*M* unitary matrix
  *Q* and a
  *M*-by-*N* upper-triangular
  matrix *R*.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

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

Factor arbitrary matrix into unitary and upper triangular components

The QR Factorization block uses a sequence of Householder
transformations to triangularize the input matrix *A*.

QR factorization is an important tool for solving linear systems of equations because
of good error propagation properties and the invertibility of unitary matrices:

*Q*
 –1 = *Q*
`'`

where *Q*`'` is the complex conjugate transpose of
*Q*.

Unlike LU and Cholesky factorizations, the matrix *A* does not need
to be square for QR factorization. However, QR factorization requires twice as many
operations as LU Factorization (Gaussian elimination).

For more details on how the block performs the QR factorization, see Algorithms.
