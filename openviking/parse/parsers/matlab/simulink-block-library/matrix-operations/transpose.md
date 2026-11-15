---
type: simulink-block
title: 'Transpose'
family: matrix-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'transpose'
---

# Transpose

Compute transpose of matrix

## 中文

计算矩阵转置

### 所属库

Simulink / Matrix Operations

### 描述

Transpose 模块计算 *M*×*N* 矩阵的转置。

### 端口

#### 输入

#### **Port\_1** — 矩阵 *M*×*N* 矩阵

矩阵，指定为 *M*×*N* 矩阵。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — 转置矩阵 *N*×*M* 矩阵

转置矩阵，以 *N*×*M* 矩阵形式返回。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 版本历史记录

**在 R2021b 中推出**

## Libraries

Simulink / Matrix Operations

## Description

The Transpose block computes the transpose of an
*M*-by-*N* matrix.

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
