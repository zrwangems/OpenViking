---
type: simulink-block
title: 'LDL Solver'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'ldlsolver'
documentation_source_path: 'ref/ldlsolver.html'
language: en
---

# LDL Solver

## Ports

### Input

### **S** — System matrix square matrix

Specify the system matrix S as a square matrix of size
*M*-by-*M* that is Hermitian
positive definite. Only the diagonal and lower triangle of the matrix
are used, and any imaginary component of the diagonal entries is
disregarded. When the input is not positive definite, the block reacts
with the behavior specified by the **Non-positive definite
input** parameter. For more details, see the description of
the **Non-positive definite input** parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **B** — Right-side matrix of system equation vector | matrix

Specify the right-side matrix B of the system equation
S*X* = B as an
*M*-by-*N* matrix.

A length-*M* unoriented vector input for right side B
is treated as an *M*-by-1 matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **X** — Solution to system of equations vector | matrix

Unique solution to the system of equations S*X* = B,
returned as an *M*-by-*N* matrix,
*X*.

For more information on how the block determines this solution, see
Algorithms.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

## Parameters

### **Non-positive definite input** — Non-positive definite input `Ignore` (default) | `Warning` | `Error`

Specify the response to nonpositive definite matrix inputs as
`Ignore`, `Warning`,
or `Error`.

The algorithm requires that the input be Hermitian positive definite. When
the input is not positive definite, the block reacts with the behavior
specified by the **Non-positive definite input** parameter.
When you set this parameter to:

- `Ignore` — The block proceeds with
  the computation and do not issue an alert. The output is not a valid
  solution.
- `Warning` — The block proceeds
  with the computation and display a warning message in the
  MATLAB® command window. The output is not a valid
  solution.
- `Error` — The block displays an
  error dialog and terminate the simulation.

**Note**

The **Non-positive definite input** parameter is a
diagnostic parameter. Like all diagnostic parameters on the
Configuration Parameters dialog, it is set to
`Ignore` in the code generated for this
block by Simulink®
Coder™ code generation software.

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

Solve S X = B when S is square Hermitian positive definite matrix

The LDL Solver block solves the linear system of equations
S*X* = B by applying LDL factorization to the Hermitian positive
definite square matrix at the **S** port. For more details, see Algorithms.
