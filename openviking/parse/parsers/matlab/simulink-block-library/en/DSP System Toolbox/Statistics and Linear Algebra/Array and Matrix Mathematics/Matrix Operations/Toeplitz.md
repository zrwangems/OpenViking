---
type: simulink-block
title: 'Toeplitz'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Matrix Operations'
documentation_page: 'toeplitz'
documentation_source_path: 'ref/toeplitz.html'
language: en
---

# Toeplitz

## Ports

### Input

### **Input** — Input vector

Input `u` from which the block generates a symmetric
(or Hermitian) Toeplitz matrix when you select the
**Symmetric** check box. The single input defines
both the first row and first column of the Toeplitz matrix.

Here is the equivalent MATLAB® code.

```
y = toeplitz(u)
```

The output *y* has the dimension
[`length`(`u`)
`length`(`u`)]. For example, the
Toeplitz matrix generated from the input vector `[1 2 3
4]` is

[1234212332124321]

#### Dependencies

To enable this port, select the **Symmetric**
check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **Toep Col** — First column of asymmetric Toeplitz matrix vector

First column of the asymmetric Toeplitz matrix, specified as a
vector.

#### Dependencies

To enable this port, clear the **Symmetric**
check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

### **Toep Row** — First row of asymmetric Toeplitz matrix vector

First row of the asymmetric Toeplitz matrix, specified as a
vector.

#### Dependencies

To enable this port, clear the **Symmetric**
check box.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Toeplitz matrix matrix

Toeplitz matrix, returned as a matrix. The block generates this matrix
depending on the setting of the **Symmetric** check
box.

When you select the **Symmetric** check box, the
block generates a symmetric (or Hermitian) Toeplitz matrix from a single
input `u` defining both the first row and first column
of the matrix.

Here is the equivalent MATLAB code.

```
y = toeplitz(u)
```

The output has dimension
[`length`(`u`)
`length`(`u`)]. For example, the
Toeplitz matrix generated from the input vector `[1 2 3
4]` is

[1234212332124321]

When you do not select the **Symmetric** check box,
the Toeplitz block generates a Toeplitz matrix from
inputs defining the first column and first row. The top input
(`Toep Col`) is a vector containing the values to
be placed in the first column of the matrix, and the bottom input
(`Toep Row`) is a vector containing the values to
be placed in the first row of the matrix.

Here is the equivalent MATLAB code.

```
y = toeplitz(Toep Col,Toep Row)
```

The other elements of the matrix obey the relationship:

```
y(i,j) = y(i-1,j-1)
```

and the output has dimension
[`length`(`Toep Col`)
`length`(`Toep Row`)]. The
*y*(1,1) element is inherited from the
`Toep Col` input. For example, the following
inputs

```
Toep Col = [1 2 3 4 5]
```

```
Toep Row = [7 7 3 3 2 1 3]
```

produce the Toeplitz matrix

[17332132173321321733243217335432173]

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### **Symmetric** — Symmetric Toeplitz matrix output `on` (default) | `off`

When you select the **Symmetric** check box, the block
generates a symmetric (Hermitian) Toeplitz matrix from a single input,
`u`, defining both the first row and first column of
the matrix.

Here is the equivalent MATLAB code.

```
y = toeplitz(u)
```

When you do not select the **Symmetric** check box, the
Toeplitz block generates a Toeplitz matrix from inputs
defining the first column `Toep Col` and first row
`Toep Row`.

Here is the equivalent MATLAB code.

```
y = toeplitz(Toep Col,Toep Row)
```

The other elements of the matrix obey the relationship:

```
y(i,j) = y(i-1,j-1)
```

For more information, see the **Output** port
description.

### **Saturate on integer overflow** — Saturate on integer overflow `on` (default) | `off`

When you generate a symmetric Toeplitz matrix with this block, if the input vector is
complex, the output is a symmetric Hermitian matrix whose elements satisfy
the relationship:

y(i,j)=conj(y(j,i))

For fixed-point signals, the conjugate operation could result in an overflow. When you
select this parameter, overflows saturate. This parameter is ignored for
floating-point signals.

#### Dependencies

To enable this parameter, select the **Symmetric**
check box.

## Libraries

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Generate matrix with Toeplitz symmetry

Generate a symmetric or asymmetric Toeplitz matrix from inputs. If you select the
**Symmetric** check box, the block generates a symmetric (or
Hermitian) Toeplitz matrix. If you do not select the **Symmetric**
check box, the block generates an asymmetric Toeplitz matrix. The columns and rows are
specified by the first and second inputs, respectively. The first matrix element is
inherited from the column.
