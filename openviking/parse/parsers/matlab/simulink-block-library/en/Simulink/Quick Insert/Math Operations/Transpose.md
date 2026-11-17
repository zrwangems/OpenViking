---
type: simulink-block
title: 'Transpose'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'transpose'
documentation_source_path: 'slref/transpose.html'
language: en
---

# Transpose

## Ports

### Input

### **Port\_1** — Matrix *M*-by-*N* matrix

Matrix, specified as an *M*-by-*N*
matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Transposed matrix *N*-by-*M* matrix

Transposed matrix, returned as an *N*-by-*M*
matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

Not documented in R2025b.

## Libraries

Simulink / Matrix Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Compute transpose of matrix

The Transpose block computes the transpose of an
*M*-by-*N* matrix.
