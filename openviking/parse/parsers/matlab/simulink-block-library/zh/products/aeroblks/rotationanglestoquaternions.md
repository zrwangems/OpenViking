---
type: simulink-block
title: 'Rotation Angles to Quaternions'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rotationanglestoquaternions'
documentation_source_path: 'rotationanglestoquaternions.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotation Angles to Quaternions

## 端口

### 输入

### **[R1,R2,R3]** — 旋转角 3×1 向量

旋转角，指定为 3×1 向量，以 radians 为单位。

**数据类型:** `double`
### 输出

### **q** — 四元数 4×1 向量

四元数，指定为 4×1 向量。

**数据类型:** `double`

## 参数

### **旋转顺序** — 旋转顺序 `ZYX`（默认）| `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

指定三个输入旋转角的旋转顺序。

#### 编程用法

|  |
| --- |
| **模块参数**: `rotationOrder` |
| **类型**: character vector |
| **值**: `'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **默认**: `'ZYX'` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

## 描述

从旋转角计算四元数

Rotation Angles to Quaternions 模块将由三个旋转角 (R1, R2, R3) 描述的旋转转换为四元素四元数向量 (*q*0, *q*1, *q*2, *q*3)，其中四元数使用 scalar-first 约定定义。Aerospace Blockset™ 使用通过 scalar-first 约定定义的四元数。旋转角表示从坐标系 A 到坐标系 B 的一系列右手本征被动变换。所得四元数表示从坐标系 A 到坐标系 B 的右手被动旋转。有关四元数的详细信息，请参阅 Algorithms。
