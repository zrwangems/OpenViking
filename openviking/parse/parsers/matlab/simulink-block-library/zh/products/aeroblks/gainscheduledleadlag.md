---
type: simulink-block
title: 'Gain Scheduled Lead-Lag'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Guidance, Navigation, and Control (GNC) / Control'
documentation_page: 'gainscheduledleadlag'
documentation_source_path: 'gainscheduledleadlag.html'
language: zh-CN
chinese_source: worker-translation
---

# Gain Scheduled Lead-Lag

## 端口

### 输入

### **e** — 滤波器输入标量

滤波器输入，指定为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **a** — 分子系数标量

分子系数，指定为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **b** — 分母系数正标量

分母系数，指定为正标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

### 输出

### **u** — 滤波器输出标量

滤波器输出，指定为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Initial state, x\_initial** — 初始内部状态 `0`（默认） | vector

初始内部状态，指定为向量，用于滤波器 `x_initial`。给定该初始状态，初始输出由下式给出

u|t=0=x\_initial+aeb

#### 编程使用

|  |
| --- |
| **模块参数**：`initial state, x_initial` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'0'` |

## 所属库

Aerospace Blockset / GNC / Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现具有增益调度系数的一阶超前-滞后

Gain Scheduled Lead-Lag 模块实现以下形式的一阶滞后

u=1+as1+bse

其中 *e* 是滤波器输入，*u* 是滤波器输出。

系数 *a* 和 *b* 是模块的输入。这些值可以取决于飞行条件或工作点。例如，您可以从 Lookup Table (n-D) Simulink® 模块生成它们。
