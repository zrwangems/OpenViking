---
type: simulink-block
title: 'Interpolate Matrix(x,y)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Control'
documentation_page: 'interpolatematrixxy'
documentation_source_path: 'interpolatematrixxy.html'
language: en
---

# Interpolate Matrix(x,y)

## Ports

### Input

### **x\_k** — First interpolation index scalar

First interpolation index *i*, specified as a scalar
and vector.

**Data Types:** `double`

### **x\_f** — First interpolation fraction scalar

First interpolation fraction *λ*
x, specified as a scalar

**Data Types:** `double`

### **y\_k** — Second interpolation index scalar

Second interpolation index *j*, specified as a
scalar.

**Data Types:** `double`

### **y\_f** — Second interpolation fraction scalar

Second interpolation fraction *λ*
y, specified as a scalar.

**Data Types:** `double`
### Output

### **Matrix(x,y)** — Interpolated matrix matrix

Interpolated matrix, specified as a matrix.

**Data Types:** `double`

## Parameters

### **Matrix to interpolate** — Matrix `matrix` (default)

Matrix to be interpolated, with four indices and the third and fourth
indices labeling the interpolating values of *x* and
*y*.

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

Return interpolated matrix for given inputs

The Interpolate Matrix(x,y) block interpolates a
two-dimensional array of matrices. In two-dimensional cases, the interpolation is
carried out first on *x* and then *y*. For more
information, see Algorithms.

The matrix to be interpolated must be four-dimensional, the first two dimensions
corresponding to the matrix at each value of *x* and
*y*. For example, if you have four matrices *A*,
*B*, *C*, and *D* defined at
`(x = 0.0,y = 1.0)`,
`(x = 0.0,y = 3.0)`,
`(x = 1.0,y = 1.0)` and
`(x = 1.0,y = 3.0)`, then the input matrix is
given by

`matrix(:,:,1,1) = A;`

`matrix(:,:,1,2) = B;`

`matrix(:,:,2,1) = C;`

`matrix(:,:,2,2) = D;`
