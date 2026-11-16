---
type: simulink-block
title: 'Interpolate Matrix(x)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Control'
documentation_page: 'interpolatematrixx'
documentation_source_path: 'interpolatematrixx.html'
language: zh-CN
chinese_source: worker-translation
---

# Interpolate Matrix(x)

## 端口

### 输入

### **x\_k** — 插值索引 *i* 标量

插值索引 *i*，指定为标量。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **x\_f** — 插值分数标量

插值分数 *λ*，指定为标量。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Matrix(x)** — 插值矩阵 matrix

插值矩阵，指定为矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **要插值的矩阵** — 矩阵 `matrix`（默认）

要插值的矩阵，具有三个索引，第三个索引标记 *x* 的插值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `matrix` |
| **类型**: character vector |
| **值**: matrix |
| **默认**: `'matrix'` |

## 所属库

Aerospace Blockset / GNC / Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

返回给定输入的插值矩阵

Interpolate Matrix(x) 模块对一维矩阵数组进行插值。该模块假定一维数组如算法中所定义。

要插值的矩阵必须为三维，前两维对应于每个 *x* 值处的矩阵。例如，如果有三个矩阵 *A*、*B* 和 *C* 分别在 `x = 0`、`x = 0.5` 和 `x = 1.0` 处定义，则输入矩阵由下式给出

`matrix(:,:,1) = A;`

`matrix(:,:,2) = B;`

`matrix(:,:,3) = C;`
