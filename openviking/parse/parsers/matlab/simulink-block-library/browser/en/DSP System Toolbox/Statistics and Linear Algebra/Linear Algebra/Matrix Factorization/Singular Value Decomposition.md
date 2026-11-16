---
type: simulink-block
title: 'Singular Value Decomposition'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Linear Algebra / Matrix Factorization'
documentation_page: 'singularvaluedecomposition'
documentation_source_path: 'ref/singularvaluedecomposition.html'
language: en
---

# Singular Value Decomposition

## Ports

### Input

### **A** — Input matrix matrix

Specify the input as an *M*-by-*N*
matrix. The dimensions of outputs *U* and
*V* depends on whether *M* =
*N*, *M* >
*N*, or *M* < *N*.
For more information, see the description of the output ports
**U** and **V**.

Length-*N* row inputs are treated as
length-*N* columns.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **U** — *U* component matrix

*U* component of the singular value decomposition,
returned as one of these:

- When *M* = *N*,
  *U* is an
  *M*-by-*M* unitary
  matrix.
- When *M* > *N*,
  *U* is an
  *M*-by-*N* matrix whose
  columns are the first *N* columns of a unitary
  matrix.
- When *N* > *M*,
  *U* is an
  *M*-by-*M* unitary
  matrix.

If the singular value decomposition calculation fails to converge, the
output on port **U** is an undefined matrix of the
correct size.

#### Dependencies

To enable this port, select the **Show ports with U and V
matrices** check box.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **S** — *S* component column vector

*S* component of the singular value decomposition, returned as a column
vector of length *P* with positive singular
values.

Note that the first (maximum) element of output *S*
is equal to the 2-norm of the matrix *A*.

If the singular value decomposition calculation fails to converge, the
output on port **S** is an undefined vector of the
correct size.

**Data Types:** `single` | `double`

### **V** — *V* component matrix

*V* component of the singular value decomposition,
returned as one of these:

- When *M* = *N*,
  *V* is an
  *M*-by-*M* unitary
  matrix.
- When *M* > *N*,
  *V* is an
  *N*-by-*N* unitary
  matrix.
- When *N* > *M*,
  *V* is an
  *N*-by-*M* matrix whose
  columns are the first *M* columns of a unitary
  matrix.

If the singular value decomposition calculation fails to converge, the
output on port **V** is an undefined matrix of the
correct size.

#### Dependencies

To enable this port, select the **Show ports with U and V
matrices** check box.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **E** — Error port scalar

Failure to converge, returned as one of these:

- `0` — The singular value decomposition
  calculation converges.
- `1` — The singular value decomposition
  calculation does not converge.

If the singular value decomposition calculation fails to converge, the
output on ports **U**, **S**, and
**V** are undefined matrices of the correct
size.

#### Dependencies

To enable this port, select the **Show error status port
(E)** check box.

**Data Types:** `Boolean`

## Parameters

### **Show ports with U and V matrices** — Show ports with *U* and *V* matrices on (default) | off

Select this check box to enable the **U** and
**V** output ports.

### **Show error status port (E)** — Show error status port off (default) | on

Select this check box to enable the output port **E**, which reports a
failure to converge. For more information, see the description for output
port **E**.

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

## Version History

**Introduced before R2006a**

## Description

Factor matrix using singular value decomposition

The Singular Value Decomposition block factors the
*M*-by-*N* input matrix *A* such
that

A=U⋅diag(S)⋅V\*

where

- *U* is an *M*-by-*P* matrix
- *V* is an *N*-by-*P* matrix
- *S* is a length-*P* vector
- *P* is defined as
  min(*M*,*N*)
