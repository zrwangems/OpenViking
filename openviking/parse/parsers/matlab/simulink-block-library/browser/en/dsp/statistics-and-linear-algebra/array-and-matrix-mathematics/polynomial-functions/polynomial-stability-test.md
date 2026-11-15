---
type: simulink-block
title: 'Polynomial Stability Test'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Polynomial Functions'
documentation_page: 'polynomialstabilitytest'
documentation_source_path: 'ref/polynomialstabilitytest.html'
language: en
---

# Polynomial Stability Test

## Ports

### Input

### **Input** — Input polynomial vector | matrix

Specify the input polynomial as a vector or a matrix of size
*M*-by-*N*.

Each column of the input matrix *u* contains *M*
coefficients from a distinct polynomial

f(x)=u1xM−1+u2xM−2+…+uM

arranged in order of descending exponents *u*1,
*u*2, ...,
*u*M. The polynomial has an
order of *M* − 1 and contains positive integer
exponents.

The block always treats a length-*M* unoriented vector input as an
*M*-by-1 matrix.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Output** — Polynomial stability test output scalar | 1-by-*N* matrix

Polynomial stability test output, returned as a scalar or a
1-by-*N* matrix with each column containing the
value `1` or `0`.

The value of `1` indicates that the polynomial in the
corresponding column of the input is stable, that is, the magnitudes of
all solutions to *f(x)* = 0 are less than 1. The
value of `0` indicates that the polynomial in the
corresponding column of the input might be unstable, that is, the
magnitude of at least one solution to
*f*(*x*) = 0 is greater than
or equal to 1.

**Data Types:** `Boolean`

## Parameters

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Math Functions / Polynomial Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `No` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generated code relies on the `memcpy` or
`memset` function (`string.h`) under certain
conditions.

## Version History

**Introduced before R2006a**

## Description

Use Schur-Cohn algorithm to determine whether all roots of input polynomial are inside unit circle

The Polynomial Stability Test block uses the Schur-Cohn algorithm to
determine whether all roots of a polynomial are within the unit circle.

This is the equivalent MATLAB® code for the block.

```
y = all(abs(roots(u)) < 1)
```

This block is most commonly used to check the pole locations of the denominator polynomial
*A*(*z*) of a transfer function
*H*(*z*).

H(z)=B(z)A(z)=b1+b2z−1+…+bmz−(m−1)a1+a2z−1+…+anz−(n−1)

The poles are the *n* − 1 roots of the denominator polynomial
*A*(*z*). When any poles are located outside the
unit circle, the transfer function *H*(*z*) is
unstable. As is typical in DSP applications, the transfer function
*H*(*z*) is specified in descending powers of
*z*−1 rather than
*z*.
