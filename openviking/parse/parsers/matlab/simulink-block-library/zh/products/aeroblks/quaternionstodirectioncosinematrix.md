---
type: simulink-block
title: 'Quaternions to Direction Cosine Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'quaternionstodirectioncosinematrix'
documentation_source_path: 'quaternionstodirectioncosinematrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternions to Direction Cosine Matrix

## 端口

### 输入

### **q** — 四元数 4×1 向量

四元数，指定为 4×1 向量。

**数据类型：** `double`
### 输出

### **DCMbe** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，返回为 3×3 矩阵。

**数据类型：** `double`

## 参数

未在 R2025b 中记录。

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将四元数向量转换为方向余弦矩阵

Quaternions to Direction Cosine Matrix 模块将四元素单位四元数向量 (*q*0, *q*1, *q*2, *q*3) 转换为 3×3 方向余弦矩阵 (DCM)。输出的 DCM 执行从惯性轴中的向量到体轴中的向量的坐标变换。Aerospace Blockset™ 使用按标量优先约定定义的四元数。此模块对所有四元数输入进行归一化。四元数输入和得到的方向余弦矩阵表示从坐标系 A 到坐标系 B 的右手被动变换。有关详细信息，请参阅算法。
