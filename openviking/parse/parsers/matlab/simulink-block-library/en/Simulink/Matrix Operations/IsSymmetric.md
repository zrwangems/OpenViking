---
type: simulink-block
title: 'IsSymmetric'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'issymmetric'
documentation_source_path: 'slref/issymmetric.html'
language: en
---

# IsSymmetric

## Ports

### Input

### **Port\_1** — Input matrix matrix

Input, specified as a matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Symmetric or skew-symmetric matrix real scalar boolean

A symmetric or skew-symmetric matrix, returned as a real scalar boolean.

**Data Types:** `Boolean`

## Parameters

### **Mode** — Whether matrix is symmetric or skew-symmetric `Symmetric` (default) | `Skew-Symmetric`

Identify the matrix as `Symmetric` or
`Skew-Symmetric`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Mode` |
| **Type:** character vector |
| **Values:** `'Symmetric'` | `'Skew-Symmetric'` |
| **Default:** `'Symmetric'` |

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

**Introduced in R2021b**

## Description

Check if matrix is symmetric or skew-symmetric

The IsSymmetric block determines if the input is a symmetric or
skew-symmetric matrix.
