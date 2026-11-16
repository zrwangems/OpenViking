---
type: simulink-block
title: 'Rodrigues to Quaternions'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rodriguestoquaternions'
documentation_source_path: 'rodriguestoquaternions.html'
language: zh-CN
chinese_source: worker-translation
---

# Rodrigues to Quaternions

## 端口

### 输入

### **rod** — Euler-Rodrigues 向量，三元素向量

用于确定四元数的 Euler-Rodrigues 向量。

**数据类型：** `double`

### 输出

### **q** — 四元数 4-by-1 矩阵

根据 Euler-Rodrigues 向量确定的四元数。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

将 Euler-Rodrigues 向量转换为四元数

Rodrigues to Quaternions 模块根据三元素 Euler-Rodrigues 向量确定 4-by-1 四元数。Aerospace Blockset™ 使用按 scalar-first 约定定义的四元数。Euler-Rodrigues 向量输入和所得四元数表示从 frame A 到 frame B 的右手被动变换。所得四元数表示从 frame A 到 frame B 的一系列右手内禀被动旋转。有关 Euler-Rodrigues 向量的更多信息，请参阅 Algorithms。
