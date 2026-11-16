---
type: simulink-block
title: 'Estimate Inertia Tensor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Mass Properties'
documentation_page: 'estimateinertiatensor'
documentation_source_path: 'estimateinertiatensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Estimate Inertia Tensor

## 端口

### 输入

### **mass** — 质量标量

质量，指定为标量。

**数据类型：** `double`

### **dm/dt** — 变化率标量

质量变化率，指定为标量。

**数据类型：** `double`
### 输出

### **I** — 惯性张量 3×3 矩阵

惯性张量，以 3×3 矩阵形式返回。

**数据类型：** `double`

### **dI/dt** — 变化率 3×3 矩阵

惯性张量的变化率，以 3×3 矩阵形式返回。

**数据类型：** `double`

## 参数

### **满载质量** — 质量 `2`（默认）| 标量

车辆的总质量，指定为 double 标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`fmass` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'2'` |

### **空载质量** — 空载质量 `1`（默认）| 标量

车辆的空载质量，指定为 double 标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`emass` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'1'` |

### **满载惯性矩阵** — 满载惯性矩阵 `eye(3)`（默认）| 3 元素矩阵

车辆总质量下的惯性张量，指定为三元素矩阵。

#### 编程使用

|  |
| --- |
| **模块参数**：`fI` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`'eye(3)'` |

### **空载惯性矩阵** — 空载惯性矩阵 `eye(3)/2`（默认）| 标量

车辆空载质量下的惯性张量，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`eI` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'eye(3)/2'` |

## 所属库

Aerospace Blockset / Mass Properties

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算惯性张量

Estimate Inertia Tensor 模块计算惯性张量以及惯性张量的变化率。

使用线性插值将惯性张量估计为质量的函数。惯性张量的变化率是质量变化率的线性函数。
