---
type: simulink-block
title: 'IsHermitian'
family: 'matrix-operations'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'ishermitian'
documentation_source_path: 'slref/ishermitian.html'
language: zh-CN
chinese_source: worker-translation
---

# IsHermitian

## 端口

### 输入

### **Port\_1** — 输入矩阵 matrix

输入矩阵，指定为矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — Hermitian 或 skew-Hermitian 矩阵 real scalar Boolean

一个 Hermitian 或 skew-Hermitian 矩阵，以 real scalar Boolean 形式返回。

**数据类型：** `Boolean`

## 参数

### **Mode** — 矩阵是 Hermitian 还是 skew-Hermitian `Hermitian`（默认） | `Skew-Hermitian`

将矩阵标识为 `Hermitian` 或 `Skew-Hermitian`。

#### 编程用法

|  |
| --- |
| **模块参数：** `Mode` |
| **类型：** character vector |
| **取值：** `'Hermitian'` | `'Skew-Hermitian'` |
| **默认值：** `'Hermitian'` |

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integera` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 此模块仅对 skew-symmetric 模式支持有符号整数类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

检查矩阵是否为 Hermitian 或 skew-Hermitian

IsHermitian 模块确定输入是否为 Hermitian 或 skew-Hermitian 矩阵。
