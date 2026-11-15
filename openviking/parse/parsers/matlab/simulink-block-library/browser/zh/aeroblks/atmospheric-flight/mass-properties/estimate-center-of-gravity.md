---
type: simulink-block
title: 'Estimate Center of Gravity'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Mass Properties'
documentation_page: 'estimatecenterofgravity'
documentation_source_path: 'estimatecenterofgravity.html'
language: zh-CN
chinese_source: worker-translation
---

# Estimate Center of Gravity

## 端口

### 输入

### **mass** — 质量标量

质量，指定为标量。

**数据类型：** `double`

### **dm/dt** — 变化率标量 | 三元素向量

质量变化率，指定为标量或三元素向量。

**数据类型：**  | `double`

### 输出

### **CG** — 重心位置 三元素向量

重心位置，返回为三元素向量。

**数据类型：** `double`

### **dCG/dt** — 变化率 三元素向量

重心位置的变化率，返回为三元素向量。

**数据类型：** `double`

## 参数

### **满载质量** — 质量 `2`（默认）| 标量

车辆的总质量，指定为 double 标量。

#### 编程用法

|  |
| --- |
| **模块参数**: `fmass` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'2'` |

### **空载质量** — 空载质量 `1`（默认）| 标量

车辆的空载质量，指定为 double 标量。

#### 编程用法

|  |
| --- |
| **模块参数**: `emass` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'1'` |

### **满载重心** — 满载重心 `[1 1 1]'`（默认）| 三元素向量

车辆总质量时的重心，指定为三元素向量。

#### 编程用法

|  |
| --- |
| **模块参数**: `fcg` |
| **类型**: character vector |
| **值**: 3-element vector |
| **默认值**: `[1 1 1]'` |

### **空载重心** — 空载重心 `[0.5 0.5 0.5]'`（默认）| 三元素向量

车辆空载质量时的重心，指定为三元素向量。

#### 编程用法

|  |
| --- |
| **模块参数**: `ecg` |
| **类型**: character vector |
| **值**: 3-element vector |
| **默认值**: `[0.5 0.5 0.5]'` |

## 所属库

Aerospace Blockset / Mass Properties

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算重心位置

Estimate Center of Gravity 模块计算重心位置以及重心的变化率。

使用线性插值根据质量估算重心位置。重心的变化率是质量变化率的线性函数。
