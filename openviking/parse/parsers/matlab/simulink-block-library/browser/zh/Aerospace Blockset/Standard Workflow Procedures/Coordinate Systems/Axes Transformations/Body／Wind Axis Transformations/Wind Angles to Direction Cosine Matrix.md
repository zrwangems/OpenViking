---
type: simulink-block
title: 'Wind Angles to Direction Cosine Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'windanglestodirectioncosinematrix'
documentation_source_path: 'windanglestodirectioncosinematrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Wind Angles to Direction Cosine Matrix

## 端口

### 输入

### **μ γ χ** — 风旋转角 3×1 向量

风旋转角，指定为 3×1 向量，以 radians 为单位。

**数据类型：** `double`
### 输出

### **DCMwe** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，以 3×3 矩阵形式返回。

**数据类型：** `double`

## 参数

在 R2025b 中未记录。

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将风角转换为方向余弦矩阵

Wind Angles to Direction Cosine Matrix 模块将三个风旋转角转换为 3×3 方向余弦矩阵 (DCM)。DCM 矩阵将地轴系
(*ox*0,
*oy*0,
*oz*0) 中的向量进行坐标变换，转换为风轴系
(*ox*3,
*oy*3,
*oz*3) 中的向量。有关方向余弦矩阵的详细信息，请参阅算法。

此实现生成的航迹角位于 ±90 degrees 之间，滚转角和航向角位于 ±180 degrees 之间。
