---
type: simulink-block
title: 'Modulo by Constant'
family: 'fixedpoint'
product_id: 'fixedpoint'
product_name: 'Fixed-Point Designer'
documentation_release: R2025b
official_category: ''
documentation_page: 'modulobyconstant'
documentation_source_path: 'ref/modulobyconstant.html'
language: zh-CN
chinese_source: official
---

# Modulo by Constant

## 端口

### 输入

### **X** — 被除数 实数值标量 | 向量 | 矩阵 | 多维数组

被除数，指定为实数值标量、向量、矩阵或多维数组。

如果 `X` 是定点数据类型，它必须使用二进制小数点定标。定点数据类型不支持斜率偏置表示。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Y** — 模数运算的结果 标量 | 向量 | 矩阵 | 多维数组

模数运算的结果，以标量、向量、矩阵或多维数组形式返回。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

### **模数问题的分母** — 除数 10 (默认) | 实数值标量 | 向量 | 矩阵 | 多维数组

用于模数运算的除数，指定为正实数值、有限标量、向量、矩阵或多维数组。

#### 编程用法

|  |
| --- |
| **模块参数**：`Denominator` |
| **类型：**字符向量 |
| **值：**计算结果为正实数值有限定点或数值的 MATLAB® 表达式 |
| **数据类型：**`single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **默认值：**`'10'` |

## 所属库

Fixed-Point Designer

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

定点数据类型不支持斜率偏置表示。

## 版本历史

**在 R2021a 中推出**

### R2023b: 支持向量和矩阵输入

Modulo by Constant 模块现在支持向量和矩阵输入。

### R2023b: 支持在 For Each Subsystem 模块中使用 Modulo by Consant 模块

支持在 For Each Subsystem 模块中使用 Modulo by Consant 模块。

## 描述

用常量分母执行取模运算

Modulo by Constant 模块使用常量分母执行取模运算（除后余数）。

Modulo by Constant 模块使用的算法在功能上类似于巴雷特归约。除法运算是通过与倒数相乘计算的，这通常有助于在嵌入式系统上实现更好的性能。
