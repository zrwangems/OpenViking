---
type: simulink-block
title: 'IsSymmetric'
family: matrix-operations
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'issymmetric'
language: zh-CN
chinese_source: official
---

# IsSymmetric

检查矩阵是否对称或斜对称

## 所属库

Simulink / Matrix Operations

## 描述

IsSymmetric 模块确定输入是对称矩阵还是斜对称矩阵。

## 端口

### 输入

### **Port\_1** — 输入矩阵 矩阵

输入，指定为矩阵。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 对称或斜对称矩阵 实数标量布尔值

对称或斜对称矩阵，以实数标量布尔值返回。

**数据类型:** `Boolean`

## 参数

### **模式** — 矩阵是对称矩阵还是斜对称矩阵 **对称** (默认) | **斜对称**

将矩阵标识为**对称**或**斜对称**。

#### 编程用法

|  |
| --- |
| **模块参数**：`Mode` |
| **类型：**字符向量 |
| **值：**`'Symmetric'` | `'Skew-Symmetric'` |
| **默认值**：`'Symmetric'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integera` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 此模块仅支持斜对称模式的有符号整数类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史记录

**在 R2021b 中推出**
