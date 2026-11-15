---
type: simulink-block
title: 'Rotation Angles to Rodrigues'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rotationanglestorodrigues'
documentation_source_path: 'rotationanglestorodrigues.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotation Angles to Rodrigues

## 端口

### 输入

### **R1,R2,R3** — 旋转角度三元素向量

旋转角度，以 radians 为单位，用于确定 Euler-Rodrigues 向量。值必须为 double。

### 输出

### **rod** — Euler-Rodrigues 向量三元素向量

根据旋转角度确定的 Euler-Rodrigues 向量。

**数据类型：** `double`

## 参数

### **旋转顺序** — 旋转顺序 `ZYX`（默认） | `ZYX` | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

三个风旋转角度的旋转顺序。

对于 `'ZYX'`、`'ZXY'`、`'YXZ'`、`'YZX'`、`'XYZ'` 和 `'XZY'` 序列，默认限制生成的 R2 角位于 ±pi/2 radians（± 90 degrees）之间，而 R1 和 R3 角位于 ±pi radians（±180 degrees）之间。

对于 `'ZYZ'`、`'ZXZ'`、`'YXY'`、`'YZY'`、`'XYX'` 和 `'XZX'` 序列，默认限制生成的 R2 角位于 0 与 pi radians（180 degrees）之间，而 R1 和 R3 角位于 ±pi（±180 degrees）之间。

当旋转角度等于 ±pi radians（±180 deg）时，Rodrigues 变换未定义。

#### 程序化使用

|  |
| --- |
| **模块参数**: `rotationOrder` |
| **类型**: character vector |
| **值**: `'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **默认值**: `'ZYX'` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

将旋转角度转换为 Euler-Rodrigues 向量

Rotation Angles to Rodrigues 模块将由三个旋转角度 `R1,R2,R3` 描述的旋转转换为三元素 Euler-Rodrigues 向量。此模块中使用的旋转是两个坐标系之间的被动变换。这些旋转角度表示从坐标系 A 到坐标系 B 的一系列右手内旋被动旋转。所得的 Euler-Rodrigues 向量表示从坐标系 A 到坐标系 B 的右手被动旋转。有关 Euler-Rodrigues 向量的更多信息，请参阅算法。
