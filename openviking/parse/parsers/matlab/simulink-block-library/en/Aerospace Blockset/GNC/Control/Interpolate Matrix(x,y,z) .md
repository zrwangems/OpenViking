---
type: simulink-block
title: 'Interpolate Matrix(x,y,z)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Control'
documentation_page: 'interpolatematrixxyz'
documentation_source_path: 'interpolatematrixxyz.html'
language: en
---

# Interpolate Matrix(x,y,z)

## Ports

### Input

### **x\_k** — First interpolation index scalar

First interpolation index *i*, specified as a scalar.

**Data Types:** `double`

### **x\_f** — First interpolation fraction scalar

First interpolation fraction *λ x*, specified as
a scalar.

**Data Types:** `double`

### **y\_k** — Second interpolation index scalar

Second interpolation index *j*, specified as a scalar.

**Data Types:** `double`

### **y\_f** — Second interpolation fraction scalar

Second interpolation fraction *λ y*, specified
as a scalar.

**Data Types:** `double`

### **z\_k** — Third interpolation index scalar

Third interpolation index *k*, specified as a scalar.

**Data Types:** `double`

### **z\_f** — Third interpolation fraction scalar

Third interpolation fraction *λ z*, specified as
a scalar.

**Data Types:** `double`
### Output

### **Matrix(x,y,z)** — Interpolated matrix matrix

Interpolated matrix, specified as a matrix.

**Data Types:** `double`

## Parameters

### **Matrix to interpolate** — Matrix to interpolate `matrix` (default)

Matrix to be interpolated, with five indices and the third, fourth, and
fifth indices labeling the interpolating values of *x*,
*y*, and *z*.

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

The Interpolate Matrix(x,y,z) block interpolates a
three-dimensional array of matrices.

This three-dimensional case assumes the matrix is defined as a function of three independent variables:

*x*
= [ *x*
1
*x*
2
*x*
3
... *x*
i
*x*
i+1
... *x*
n
]

*y*
= [ *y*
1
*y*
2
*y*
3
... *y*
j
*y*
j+1
... *y*
m
]

*z*
= [ *z*
1
*z*
2
*z*
3
... *z*
k
*z*
k+1
... *z*
p
]

For given values of *x*, *y*,
and *z*, eight matrices are interpolated. Then for

*x*
i
 *< x < x*
i+1

*y*
j
 *< y < y*
j+1

*z*
k
 *< z < z*
k+1

the output matrix is given by

(1−λz){(1−λy)[(1−λx)M(xi,yj,zk)+λxM(xi+1,yj,zk)]             +λy[(1−λx)M(xi,yj+1,zk)+λxM(xi+1,yj+1,zk)]}   +λz{(1−λy)[(1−λx)M(xi,yj,zk+1)+λxM(xi+1,yj,zk+1)]            +λy[(1−λx)M(xi,yj+1,zk+1)+λxM(xi+1,yj+1,zk+1)]}

where the three interpolation fractions are denoted by

λx=(x−xi)/(xi+1−xi)λy=(y−yj)/(yj+1−yj)λz=(z−zk)/(zk+1−zk)

In the three-dimensional case, the interpolation is carried out first on
*x*, then *y*, and finally *z*.

The matrix to be interpolated should be five-dimensional, the first two dimensions
corresponding to the matrix at each value of *x*, *y*,
and *z*. For example, if you have eight matrices *A*,
*B*, *C*, *D*,
*E*, *F*, *G*, and
*H* defined at the following values of *x*,
*y*, and *z*, then the corresponding input matrix
is given by

|  |  |
| --- | --- |
| `(x = 0.0,y = 1.0,z = 0.1)` | `matrix(:,:,1,1,1) = A;` |
| `(x = 0.0,y = 1.0,z = 0.5)` | `matrix(:,:,1,1,2) = B;` |
| `(x = 0.0,y = 3.0,z = 0.1)` | `matrix(:,:,1,2,1) = C;` |
| `(x = 0.0,y = 3.0,z = 0.5)` | `matrix(:,:,1,2,2) = D;` |
| `(x = 1.0,y = 1.0,z = 0.1)` | `matrix(:,:,2,1,1) = E;` |
| `(x = 1.0,y = 1.0,z = 0.5)` | `matrix(:,:,2,1,2) = F;` |
| `(x = 1.0,y = 3.0,z = 0.1)` | `matrix(:,:,2,2,1) = G;` |
| `(x = 1.0,y = 3.0,z = 0.5)` | `matrix(:,:,2,2,2) = H;` |
