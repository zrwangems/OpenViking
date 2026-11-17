---
type: simulink-block
title: 'Wind Angular Rates'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'windangularrates'
documentation_source_path: 'windangularrates.html'
language: zh-CN
chinese_source: worker-translation
---

# Wind Angular Rates

## 端口

### 输入

### **ɑ β** — 迎角和侧滑角 2×1 向量

迎角和侧滑角，指定为 2×1 向量，单位为弧度。

**数据类型：** `double`

### **dɑ/dt dβ/dt** — 变化率 2×1 向量

迎角变化率和侧滑角变化率，指定为 2×1 向量，单位为弧度每秒。

**数据类型：** `double`

### **ω** — 机体角速率 三元素向量

机体角速率，指定为三元素向量，单位为弧度每秒。

**数据类型：** `double`
### 输出

### **ωw** — 风角速率 三元素向量

风角速率，返回为三元素向量，单位为弧度每秒。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Flight Parameters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

根据机体角速率、迎角、侧滑角、迎角变化率和侧滑角变化率计算风角速率

Wind Angular Rates 模块通过计算风固连角速率（*pw、qw、rw*）来支持风固连坐标系模型中的运动方程。有关计算所用方程的详细信息，请参阅算法。
