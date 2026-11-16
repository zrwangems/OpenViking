---
type: simulink-block
title: 'Transpose'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'transpose'
documentation_source_path: '../simulink/slref/transpose.html'
language: zh-CN
chinese_source: official
---

# Transpose

## 端口

### 输入

### **Port\_1** — 矩阵 *M*×*N* 矩阵

矩阵，指定为 *M*×*N* 矩阵。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 转置矩阵 *N*×*M* 矩阵

转置矩阵，以 *N*×*M* 矩阵形式返回。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2021b 中推出**

## 描述

计算矩阵转置

Transpose 模块计算 *M*×*N* 矩阵的转置。
