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
chinese_source: worker-translation
---

# Modulo by Constant

## 端口
```yaml
ports:
- name: X
  summary: 被除数 实数值标量 | 向量 | 矩阵 | 多维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | fixed point
- name: Y
  summary: 取模运算的结果 标量 | 向量 | 矩阵 | 多维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | fixed point
```

### 输入

### **X** — 被除数 实数值标量 | 向量 | 矩阵 | 多维数组

被除数，指定为实数值标量、向量、矩阵或多维数组。

如果 `X` 为定点数据类型，则必须使用二进制小数点定标。定点数据类型不支持斜率-偏置表示。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`
### 输出

### **Y** — 取模运算的结果 标量 | 向量 | 矩阵 | 多维数组

取模运算的结果，以标量、向量、矩阵或多维数组形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `fixed point`
## 参数
```yaml
parameters:
- name: Denominator for Modulo Problem
  summary: 除数 10 （默认） | 实数值标量 | 向量 | 矩阵 | 多维数组
  group: ''
  block_parameter: Denominator
  type: character vector
  values: MATLAB® expression that evaluates to a positive, real-valued, finite fixed point or numeric value
  default: '''10'''
```

### **Denominator for Modulo Problem** — 除数 10 （默认） | 实数值标量 | 向量 | 矩阵 | 多维数组

用于取模运算的除数，指定为正的实数值有限标量、向量、矩阵或多维数组。

#### 编程使用

|  |
| --- |
| **模块参数**：`Denominator` |
| **类型**：character vector |
| **值**：MATLAB® expression that evaluates to a positive, real-valued, finite fixed point or numeric value |
| **Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` |
| **默认值**：`'10'` |
## 所属库

Fixed-Point Designer

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

定点数据类型不支持斜率-偏置表示。

## 版本历史

**在 R2021a 中引入**

### R2023b：支持向量和矩阵输入

Modulo by Constant 模块现在支持向量和矩阵输入。

### R2023b：Modulo by Consant 模块支持在 For Each Subsystem 模块中使用

Modulo by Consant 模块支持在 For Each Subsystem 模块内部使用。

## 描述

使用常量除数执行取模运算

Modulo by Constant 模块使用常量除数执行取模运算（除法后的余数）。

Modulo by Constant 模块使用的算法在功能上类似于 Barrett Reduction。除法运算通过乘以逆元来计算，这通常能在嵌入式系统上获得更好的性能。
