---
type: simulink-block
title: 'Quaternions to Rodrigues'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'quaternionstorodrigues'
documentation_source_path: 'quaternionstorodrigues.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternions to Rodrigues

## 端口

### 输入

### **Quaternion** — Quaternion 4-by-1 矩阵

Quaternion，用于从中确定 Euler-Rodrigues 向量。Quaternion 标量是第一个元素。

**数据类型：** `double`
### 输出

### **rod** — Euler-Rodrigues 向量三元素向量

由四元数确定的 Euler-Rodrigues 向量。

**数据类型：** `double`

## 参数

在 R2025b 中未记录。

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

将四元数转换为 Euler-Rodrigues 向量

Quaternions to Rodrigues 模块将 4-by-1 四元数转换为三元素 Euler-Rodrigues (Rodrigues) 向量。Aerospace Blockset™ 使用按标量在前约定定义的四元数。此模块会归一化所有四元数输入。四元数输入和所得的 Euler-Rodrigues 向量表示从坐标系 A 到坐标系 B 的右手被动变换。有关 Euler-Rodrigues 向量的详细信息，请参阅 Algorithms。
