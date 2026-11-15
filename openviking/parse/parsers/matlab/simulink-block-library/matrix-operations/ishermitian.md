---
type: simulink-block
title: 'IsHermitian'
family: matrix-operations
languages: [en, zh-CN]
chinese_source: worker-translation
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'ishermitian'
---

# IsHermitian

Check if matrix is Hermitian or skew-Hermitian

## 中文

检查矩阵是 Hermitian 还是 skew-Hermitian

### 库

Simulink / Matrix Operations

### 说明

IsHermitian 模块确定输入是 Hermitian 矩阵还是 skew-Hermitian 矩阵。

### 端口

#### 输入

#### **Port\_1** — 输入矩阵 matrix

输入矩阵，指定为矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — Hermitian 或 skew-Hermitian 矩阵，实数标量 Boolean

一个 Hermitian 或 skew-Hermitian 矩阵，以实数标量 Boolean 返回。

**数据类型：** `Boolean`

### 参数

#### **Mode** — 矩阵是 Hermitian 还是 skew-Hermitian `Hermitian` (默认) | `Skew-Hermitian`

将矩阵标识为 `Hermitian` 或
`Skew-Hermitian`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Mode` |
| **类型：** character vector |
| **值：** `'Hermitian'` | `'Skew-Hermitian'` |
| **默认值：** `'Hermitian'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integera` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块仅支持 skew-symmetric 模式的有符号整数类型。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 版本历史

**在 R2022a 中引入**

## Libraries

Simulink / Matrix Operations

## Description

The IsHermitian block determines if the input is a Hermitian or a
skew-Hermitian matrix.

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
