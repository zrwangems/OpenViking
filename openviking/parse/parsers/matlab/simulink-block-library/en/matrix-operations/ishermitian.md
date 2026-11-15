---
type: simulink-block
title: 'IsHermitian'
family: matrix-operations
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'ishermitian'
language: en
---

# IsHermitian

## Ports

### Input

### **Port\_1** — Input matrix matrix

Input matrix, specified as a matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Hermitian or skew-Hermitian matrix real scalar Boolean

A Hermitian or skew-Hermitian matrix, returned as a real scalar Boolean.

**Data Types:** `Boolean`

## Parameters

### **Mode** — Whether matrix is Hermitian or skew-Hermitian `Hermitian` (default) | `Skew-Hermitian`

Identify the matrix as `Hermitian` or
`Skew-Hermitian`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Mode` |
| **Type:** character vector |
| **Values:** `'Hermitian'` | `'Skew-Hermitian'` |
| **Default:** `'Hermitian'` |

## Libraries

Simulink / Matrix Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integera` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block only supports signed integer types for the skew-symmetric mode. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Check if matrix is Hermitian or skew-Hermitian

The IsHermitian block determines if the input is a Hermitian or a
skew-Hermitian matrix.
