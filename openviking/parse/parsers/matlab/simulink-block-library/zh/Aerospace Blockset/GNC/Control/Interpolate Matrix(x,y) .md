---
type: simulink-block
title: 'Interpolate Matrix(x,y)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Control'
documentation_page: 'interpolatematrixxy'
documentation_source_path: 'interpolatematrixxy.html'
language: zh-CN
chinese_source: worker-translation
---

# Interpolate Matrix(x,y)

## 端口

### 输入

### **x\_k** — 第一插值索引标量

第一插值索引 *i*，指定为标量和向量。

**数据类型：** `double`

### **x\_f** — 第一插值分数标量

第一插值分数 *λ* x，指定为标量

**数据类型：** `double`

### **y\_k** — 第二插值索引标量

第二插值索引 *j*，指定为标量。

**数据类型：** `double`

### **y\_f** — 第二插值分数标量

第二插值分数 *λ* y，指定为标量。

**数据类型：** `double`
### 输出

### **Matrix(x,y)** — 插值矩阵 matrix

插值矩阵，指定为矩阵。

**数据类型：** `double`

## 参数

### **要插值的矩阵** — 矩阵 `matrix`（默认）

要插值的矩阵，具有四个索引，第三和第四个索引标记 *x* 和 *y* 的插值值。

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

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

返回给定输入的插值矩阵

Interpolate Matrix(x,y) 模块对二维矩阵数组进行插值。在二维情况下，插值先对 *x* 执行，然后对 *y* 执行。有关详细信息，请参阅算法。

要插值的矩阵必须是四维的，前两个维度对应于每个 *x* 和 *y* 值处的矩阵。例如，如果有四个矩阵 *A*、*B*、*C* 和 *D*，定义在 `(x = 0.0,y = 1.0)`、`(x = 0.0,y = 3.0)`、`(x = 1.0,y = 1.0)` 和 `(x = 1.0,y = 3.0)`，则输入矩阵由下式给出

`matrix(:,:,1,1) = A;`

`matrix(:,:,1,2) = B;`

`matrix(:,:,2,1) = C;`

`matrix(:,:,2,2) = D;`
