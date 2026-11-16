---
type: simulink-block
title: 'Least Squares Polynomial Fit'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Polynomial Functions'
documentation_page: 'leastsquarespolynomialfit'
documentation_source_path: 'ref/leastsquarespolynomialfit.html'
language: en
---

# Least Squares Polynomial Fit

## Ports

### Input

### **Input** — Input data vector | matrix

Specify the input data as a vector or a matrix of size
*M*-by-*N*. The block treats a
length-*M* unoriented vector input as an
*M*-by-1 matrix.

**Data Types:** `single` | `double`
### Output

### **Output** — Polynomial coefficients column vector | matrix

Coefficients of the polynomial that best fits the input data in the
least-squares sense, returned as a column vector or a matrix of size
(*n*+1)-by-*N*, where
*n* is the value you specify in the
**Polynomial order** parameter.

Each column of the (*n*+1)-by-*N*
output matrix *c* represents a set of
*n*+1 coefficients describing the best-fit
polynomial for the corresponding column of the input. The coefficients
in each column are arranged in order of descending exponents,
*c*1,
*c*2, ...,
*c*n+1.

For more information on how this block computes the polynomial
coefficients, see Algorithms.

**Data Types:** `single` | `double`

## Parameters

### **Control points (X)** — Control points `(0:31)/31` (default) | vector

Specify the values of the independent variable to which the data in each
input column correspond. For an *M*-by-*N*
input, this parameter must be a length-*M* vector.

**Tunable:** Yes

### **Polynomial order (N)** — Polynomial order `3` (default) | positive integer

Specify the order *n* of the polynomial that the block uses to construct
the best fit. The number of coefficients is *n*+1.

## Libraries

DSP System Toolbox / Math Functions / Polynomial Functions

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

Compute polynomial coefficients that best fit input data in least-squares sense

The Least Squares Polynomial Fit block computes the coefficients of the
*n*th order polynomial that best fits the input data in the
least-squares sense, where *n* is the value you specify in the
**Polynomial order** parameter. The block computes a distinct set
of *n*+1 coefficients for each column of the
*M*-by-*N* input *u*.
