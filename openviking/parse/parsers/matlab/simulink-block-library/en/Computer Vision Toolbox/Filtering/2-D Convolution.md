---
type: simulink-block
title: '2-D Convolution'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: '2dconvolution'
documentation_source_path: 'ref/2dconvolution.html'
language: en
---

# 2-D Convolution

## Ports

### Input

### **I1** — Input matrix matrix

Input matrix, specified as either a matrix of intensity values or a matrix that
represents one plane of an RGB video stream.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I2** — Input matrix matrix

Input matrix, specified as either a matrix of intensity values or a matrix that
represents one plane of an RGB video stream.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Output** — Convolution matrix

Convolution of the input matrices, returned as a matrix.

#### Dependencies

- The dimensions of the output are dictated by the **Output
  size** parameter.
- If the data type of the input is floating point, the output of the block is
  also floating point.
- If `all(size(I1)<size(I2))`, the block returns an
  error.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

**Main Tab**

### **Output size** — Output size matrix

Dimensions of the output.

The table describes the block output, given the following input dimensions:

- **I1** — (*Ma*,
  *Na*)
- **I2** — (*Mb*, *Nb*)

| **Output size** | Output | Output Dimension |
| --- | --- | --- |
| `Full` | Full two-dimensional convolution | (*Ma*+*Mb*-1, *Na*+*Nb*-1). |
| `Same as input port I1` | Central part of the convolution with the same dimensions as the input at port **I1** |  |
| `Valid` | Only the parts of the convolution that are computed without the zero-padded edges of any input. | (*Ma*-*Mb*+1, *Na*-*Nb*+1) |

### **Normalized output** — Normalized output matrix

Normalize output by dividing the output by
`sqrt(sum(dot(I1p,I1p))*sum(dot(I2,I2)))`, where
`I1p` is the portion of the **I1** matrix
that aligns with the **I2** matrix.

**Note**

When you select the **Normalized output** check box, the block
input cannot be fixed point.

**Data Types Tab**

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

## Libraries

Computer Vision Toolbox / Filtering

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

When you select the **Normalized output** check box, the block input
cannot be fixed point.

## Version History

**Introduced before R2006a**

## Description

Compute 2-D discrete convolution of two input matrices

The 2-D Convolution block computes the two-dimensional convolution of two input matrices.
Assume that matrix A has dimensions (*Ma*, *Na*) and matrix
B has dimensions (*Mb*, *Nb*). When the block calculates the
full output size, the equation for the 2-D discrete convolution is:

C(i,j)=∑m=0(Ma−1)∑n=0(Na−1)A(m,n)\*B(i−m,j−n)

where 0≤i<Ma+Mb−1 and 0≤j<Na+Nb−1.
