---
type: simulink-block
title: 'Rodrigues to Rotation Angles'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rodriguestorotationangles'
documentation_source_path: 'rodriguestorotationangles.html'
language: zh-CN
chinese_source: worker-translation
---

# Rodrigues to Rotation Angles

## 端口

### 输入

### **rod** — Euler-Rodrigues 向量三元素向量

由旋转角度确定的 Euler-Rodrigues 向量。

**数据类型：** `double`
### 输出

### **R1,R2,R3** — 旋转角度三元素向量

旋转角度，单位为 radians，用于从中确定 Euler-Rodrigues 向量。四元数标量是第一个元素。

**数据类型：** `double`

## 参数

### **旋转顺序** — 旋转顺序 `ZYX`（默认） | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

三个风旋转角度的旋转顺序。

对于 'ZYX'、'ZXY'、'YXZ'、'YZX'、'XYZ' 和 'XZY' 旋转，模块生成介于 ±pi/2 radians（±90 degrees）之间的 R2 角度，以及介于 ±pi radians（±180 degrees）之间的 R1 和 R3 角度。

对于 'ZYZ'、'ZXZ'、'YXY'、'YZY'、'XYX' 和 'XZX' 旋转，模块生成介于 0 和 pi radians（180 degrees）之间的 R2 角度，以及介于 ±pi（±180 degrees）之间的 R1 和 R3 角度。但是，在后一种情况下，当 R2 为 0 时，R3 设置为 0 radians。

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

将 Euler-Rodrigues 向量转换为旋转角度

Rodrigues to Rotation Angles 模块将三元素 Euler-Rodrigues 向量转换为旋转角度。Euler-Rodrigues 角度表示从坐标系 A 到坐标系 B 的右手被动变换。得到的旋转角度表示从坐标系 A 到坐标系 B 的一系列右手本征被动旋转。有关 Euler-Rodrigues 向量的更多信息，请参阅 Algorithms。
