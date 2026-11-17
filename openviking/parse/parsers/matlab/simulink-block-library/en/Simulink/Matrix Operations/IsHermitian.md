---
type: simulink-block
title: 'IsHermitian'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'ishermitian'
documentation_source_path: 'slref/ishermitian.html'
language: en
---

# IsHermitian

## Ports
```yaml
ports:
- name: Port_1
  summary: Input matrix matrix
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Hermitian or skew-Hermitian matrix real scalar Boolean
  direction: output
  data_types: Boolean
```

### Input

### **Port\_1** — Input matrix matrix

Input matrix, specified as a matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Hermitian or skew-Hermitian matrix real scalar Boolean

A Hermitian or skew-Hermitian matrix, returned as a real scalar Boolean.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Mode
  summary: Whether matrix is Hermitian or skew-Hermitian Hermitian (default) | Skew-Hermitian
  group: ''
  block_parameter: Mode
  type: character vector
  values: '''Hermitian'' | ''Skew-Hermitian'''
  default: '''Hermitian'''
```

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
