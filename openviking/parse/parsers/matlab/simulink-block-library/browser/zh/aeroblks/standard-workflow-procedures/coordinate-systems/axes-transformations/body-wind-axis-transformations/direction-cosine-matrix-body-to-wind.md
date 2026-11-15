---
type: simulink-block
title: 'Direction Cosine Matrix Body to Wind'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixbodytowind'
documentation_source_path: 'directioncosinematrixbodytowind.html'
language: zh-CN
chinese_source: worker-translation
---

# Direction Cosine Matrix Body to Wind

## 端口

### 输入

### **ɑ β** — 攻角和侧滑角 2-by-1 向量

攻角和侧滑角，指定为 2-by-1 向量，单位为 radians。

**数据类型：** `double`
### 输出

### **DCMwb** — 方向余弦矩阵 3-by-3 方向余弦矩阵

方向余弦矩阵，返回为 3-by-3 方向余弦矩阵。

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

将攻角和侧滑角转换为方向余弦矩阵

Direction Cosine Matrix Body to Wind 模块将攻角和侧滑角转换为 3-by-3 方向余弦矩阵 (DCM)。该方向余弦矩阵有助于进行从机体轴到风轴的矢量坐标变换。要将机体轴
(*ox*0,
*oy*0,
*oz*0) 中矢量的坐标变换为风轴
(*ox*2,
*oy*2,
*oz*2) 中的矢量，请将模块输出的方向余弦矩阵与机体轴中的矢量相乘。有关此变换的轴旋转信息，请参阅算法。
