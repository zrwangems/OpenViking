---
type: simulink-block
title: '2-D Correlation'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Analysis and Statistics'
documentation_page: '2dcorrelation'
documentation_source_path: 'ref/2dcorrelation.html'
language: en
---

# 2-D Correlation

## Ports

### Input

### **I1** — First input matrix matrix

First input matrix, specified as an *M*-by-*N*
matrix. The two input matrices must have data types in the same category such as
`double`, `single`, unsigned integer
(`uint8`,`uint16`,`uint32`,`uint64`),
or integer
(`int8`,`int16`,`int32`,`int64`).

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **I2** — Second input matrix matrix

Second input matrix, specified as a *P*-by-*Q*
matrix. The two input matrices must have data types in the same category such as
`double`, `single`, unsigned integer
(`uint8`,`uint16`,`uint32`,`uint64`),
or integer
(`int8`,`int16`,`int32`,`int64`).

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Calculated cross-correlation scalar | vector | matrix

Calculated cross-correlation, returned as a scalar, vector, or matrix. The size of
the cross-correlation output depends on the **Output
size** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

## Parameters

### Main

### **Output size** — Size of cross-correlation output `Full` (default) | `Same as input port I1` | `Valid`

Size of the cross-correlation output.

- If you choose `Full`, the output has the
  dimensions
  (*M*+*P*-1)-by-(*N*+*Q*-1).
- If you choose `Same as input port I1`, the output
  has the same dimensions as the input at port **I1**. The block
  returns the central part of cross-correlation matrix, which is the same size as
  the input at port **I1**.
- If you choose `Valid`, the output has the
  dimensions
  (*M*-*P*+1)-by-(*N*-*Q*+1).
  The block returns only parts of the cross-correlation matrix that are computed
  without zero-padded edges.

### **Normalized output** — Normalize cross-correlation output `off` (default) | `on`

Select this parameter, if the data types of the inputs are floating-point. The
values of the cross-correlation output are normalized to [0, 1].

### Data Types

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

## Libraries

Computer Vision Toolbox / Statistics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Compute 2-D correlation of two input matrices

The 2-D Correlation block computes the two-dimensional cross-correlation
between two input matrices.
