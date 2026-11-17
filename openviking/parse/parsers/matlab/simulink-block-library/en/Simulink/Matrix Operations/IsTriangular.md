---
type: simulink-block
title: 'IsTriangular'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'istriangular'
documentation_source_path: 'slref/istriangular.html'
language: en
---

# IsTriangular

## Ports
```yaml
ports:
- name: Port_1
  summary: Input matrix matrix
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_2
  summary: Upper triangular or lower triangular matrix real scalar boolean
  direction: output
  data_types: Boolean
```

### Input

### **Port\_1** — Input matrix matrix

Input matrix, specified as a matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_2** — Upper triangular or lower triangular matrix real scalar boolean

Upper triangular or lower triangular matrix, specified scalar, returned as a real
scalar boolean.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Mode
  summary: Whether matrix is upper triangular or lower triangular Upper (default) | Lower
  group: ''
  block_parameter: Mode
  type: character vector
  values: '''Upper'' | ''Lower'''
  default: '''Upper'''
```

### **Mode** — Whether matrix is upper triangular or lower triangular `Upper` (default) | `Lower`

Identify the matrix as `Upper` or
`Lower`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Mode` |
| **Type:** character vector |
| **Values:** `'Upper'` | `'Lower'` |
| **Default:** `'Upper'` |
## Libraries

Simulink / Matrix Operations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Check if matrix is upper or lower triangular

The IsTriangular block determines if the input is an upper triangular or
lower triangular matrix.
