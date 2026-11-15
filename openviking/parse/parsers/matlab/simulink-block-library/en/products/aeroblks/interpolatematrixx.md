---
type: simulink-block
title: 'Interpolate Matrix(x)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control (GNC) / Control'
documentation_page: 'interpolatematrixx'
documentation_source_path: 'interpolatematrixx.html'
language: en
---

# Interpolate Matrix(x)

## Ports

### Input

### **x\_k** — Interpolation index *i* scalar

Interpolation index *i*, specified as a
scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **x\_f** — Interpolation fraction scalar

Interpolation fraction *λ*, specified as a scalar.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### Output

### **Matrix(x)** — Interpolated matrix matrix

Interpolated matrix, specified as a matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Matrix to interpolate** — Matrix `matrix` (default)

Matrix to be interpolated, with three indices and the third index labeling
the interpolating values of *x*.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `matrix` |
| **Type**: character vector |
| **Values**: matrix |
| **Default**: `'matrix'` |

## Libraries

Aerospace Blockset / GNC / Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Return interpolated matrix for given input

The Interpolate Matrix(x) block interpolates a
one-dimensional array of matrices. The block assumes a one-dimensional array as defined
in Algorithms.

The matrix to be interpolated must be three dimensional, the first two dimensions
corresponding to the matrix at each value of *x*. For example, if you
have three matrices *A*, *B*, and *C*
defined at `x = 0`, `x = 0.5`, and
`x = 1.0`, then the input matrix is given by

`matrix(:,:,1) = A;`

`matrix(:,:,2) = B;`

`matrix(:,:,3) = C;`
