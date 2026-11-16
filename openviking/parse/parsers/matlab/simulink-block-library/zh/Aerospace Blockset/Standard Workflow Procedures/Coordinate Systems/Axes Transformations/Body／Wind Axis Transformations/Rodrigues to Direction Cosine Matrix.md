---
type: simulink-block
title: 'Rodrigues to Direction Cosine Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rodriguestodirectioncosinematrix'
documentation_source_path: 'rodriguestodirectioncosinematrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Rodrigues to Direction Cosine Matrix

## 端口

### 输入

### **rod** — Euler-Rodrigues 向量三元素向量

用于确定方向余弦矩阵的 Euler-Rodrigues 向量。

**数据类型：** `double`
### 输出

### **DCM** — 方向余弦矩阵 3×3 矩阵

根据 Euler-Rodrigues 向量确定的方向余弦矩阵。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

将 Euler-Rodrigues 向量转换为方向余弦矩阵

Rodrigues to Direction Cosine Matrix 模块根据三元素 Euler-Rodrigues 向量确定 3×3 方向余弦矩阵。Euler-Rodrigues 向量输入和得到的方向余弦矩阵表示从坐标系 A 到坐标系 B 的右手被动变换。得到的方向余弦矩阵表示从坐标系 A 到坐标系 B 的一系列右手内旋被动旋转。有关 Euler-Rodrigues 向量的详细信息，请参阅算法。
