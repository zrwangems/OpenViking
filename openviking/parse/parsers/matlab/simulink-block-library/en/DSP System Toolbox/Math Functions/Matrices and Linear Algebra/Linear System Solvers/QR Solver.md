---
type: simulink-block
title: 'QR Solver'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'qrsolver'
documentation_source_path: 'ref/qrsolver.html'
language: en
---

# QR Solver

## Ports
```yaml
ports:
- name: A
  summary: System matrix vector | matrix
  direction: input
  data_types: single | double
- name: B
  summary: Right-side matrix of system equation vector | matrix
  direction: input
  data_types: single | double
- name: X
  summary: Minimum-norm-residual solution vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **A** — System matrix vector | matrix

Specify the system matrix A as a vector or a matrix of size
*M*-by-*N* matrix. The block
treats length-*M* unoriented vector input as an
*M*-by-1 matrix.

The system is solved by applying QR factorization to the
*M*-by-*N* matrix A at the
`A` port.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **B** — Right-side matrix of system equation vector | matrix

Specify the right-side matrix B of the system equation
A*X*=B as an
*M*-by-*L* matrix.

When B is a vector, the solution *X* minimizes the
vector 2-norm of the residual (B−A*X* is the residual).
When B is a matrix, the solution *X* minimizes the
matrix Frobenius norm of the residual.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **X** — Minimum-norm-residual solution vector | matrix

Minimum-norm-residual solution to A*X*=B, returned as
an *N*-by-*L* matrix,
*X*. The block determines *X* so
as to minimize the sum of the squares of the elements of
B−A*X*. The minimum-norm-residual solution is
unique for overdetermined and exactly determined linear systems, but it
is not unique for underdetermined linear systems. Thus when the QR
Solver is applied to an underdetermined system, the output
*X* is chosen such that the number of nonzero
entries in *X* is minimized.

When B is a vector, this solution minimizes the vector 2-norm of the
residual (B−A*X* is the residual). When B is a matrix,
this solution minimizes the matrix Frobenius norm of the residual. In
this case, the columns of *X* are the solutions to the
*L* corresponding systems
A*X*k=Bk,
where Bk is the *k*th column of
B, and *X*k is the
*k*th column of *X*.

For more information on how the block computes *X*,
see Algorithms.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

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

Find minimum-norm-residual solution to A X =B

The QR Solver block solves the linear system A*X*=B,
which can be overdetermined, underdetermined, or exactly determined. The block applies
QR factorization to the matrix A to find the minimum-norm-residual solution to
A*X*=B. For more details, see Algorithms.
