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
language: zh-CN
chinese_source: worker-translation
---

# IsTriangular

## 端口

### 输入

### **Port\_1** — 输入矩阵 matrix

输入矩阵，指定为矩阵。

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_2** — 上三角矩阵或下三角矩阵 real scalar boolean

上三角矩阵或下三角矩阵，指定为标量，返回为实数标量布尔值。

**Data Types:** `Boolean`

## 参数

### **Mode** — 矩阵是上三角矩阵还是下三角矩阵 `Upper`（默认）| `Lower`

将矩阵标识为 `Upper` 或 `Lower`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Mode` |
| **类型：** character vector |
| **值：** `'Upper'` | `'Lower'` |
| **默认值：** `'Upper'` |

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

检查矩阵是上三角还是下三角

IsTriangular 模块确定输入是上三角矩阵还是下三角矩阵。
