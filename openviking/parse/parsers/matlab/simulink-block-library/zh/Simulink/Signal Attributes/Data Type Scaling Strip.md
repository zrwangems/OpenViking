---
type: simulink-block
title: 'Data Type Scaling Strip'
family: 'signal-attributes'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'datatypescalingstrip'
documentation_source_path: 'slref/datatypescalingstrip.html'
language: zh-CN
chinese_source: worker-translation
---

# Data Type Scaling Strip

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。该模块去除定点输入信号的缩放，并输出具有尽可能小的内置数据类型的存储整数值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 映射到内置数据类型的输入信号 标量 | 向量 | 矩阵

输入信号的存储整数值，具有尽可能小的内置数据类型，并且维度与输入相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

未在 R2025b 中记录。

## 所属库

Simulink / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

去除缩放并映射到内置整数

Data Type Scaling Strip 模块去除定点信号的缩放。它将输入数据类型映射到具有足够数据位来容纳输入的最小内置数据类型。输入的存储整数值即为输出的值。输出始终具有标称缩放（slope = 1.0 和 bias = 0.0），因此输出不区分真实世界值与存储整数值。
