---
type: simulink-block
title: 'PS State-Space'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Linear Operators'
documentation_page: 'psstatespace'
documentation_source_path: 'ref/psstatespace.html'
language: en
---

# PS State-Space

## Ports

### Input

### **U** — Input physical signal vector, *u*, untyped physical signal

Input physical signal.
### Output

### **Y** — Output physical signal vector, *y*, untyped physical signal

Output physical signal.

## Parameters

### **A** — State matrix `[0, 1; -1, -2]` (default) | scalar | matrix

State matrix, specified as an *n*-by-*n* matrix,
where *n* is the number of states.

### **B** — Input matrix `[0, 1]` (default) | scalar | vector | matrix

Input matrix, specified as an *n*-by-*m* matrix,
where *n* is the number of states and *m* is the
number of elements in the input vector.

### **C** — Output matrix `[1, 0]` (default) | scalar | vector | matrix

Output matrix, specified as an *r*-by-*n* matrix,
where *r* is the number of elements in the output vector and
*n* is the number of states.

### **D** — Feedthrough, or direct transmission matrix `0` (default) | scalar | vector | matrix

Feedthrough, or direct transmission matrix, specified as an
*r*-by-*m* matrix, where *r* is the
number of elements in the output vector and *m* is the number of
elements in the input vector.

### **E** — Descriptor matrix `[1, 0; 0, 1]` (default) | scalar | matrix

Mass matrix of the system. The mass matrix can be singular or nonsingular and must
have the same dimensions as the state matrix **A**.

### **Initial state vector** — Initial condition of state vector `[0; 0]` (default) | scalar | vector | matrix

Dimensionless vector that represents the initial conditions of the state vector at
time *t*=0.

## Libraries

Simscape / Foundation Library / Physical Signals / Linear Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Implement linear state-space system

The PS State-Space block implements a state-space
representation of the linear time-invariant system, defined by equations:

Ex˙=Ax+Bu,y=Cx+Du,

where:

- *x* is the dimensionless state vector.
- *u* is the input vector.
- *y* is the output vector.
- *E* is the descriptor matrix.
- *A* is the state matrix.
- *B* is the input matrix.
- *C* is the output matrix.
- *D* is the feedthrough, or direct transmission matrix.

The state-space model provides a compact and efficient way to represent and analyze
systems with multiple inputs and outputs. This model is particularly useful for control design
and simulation of dynamic systems.

You can define matrices in your workspace and then use these workspace variables as block
parameters.
