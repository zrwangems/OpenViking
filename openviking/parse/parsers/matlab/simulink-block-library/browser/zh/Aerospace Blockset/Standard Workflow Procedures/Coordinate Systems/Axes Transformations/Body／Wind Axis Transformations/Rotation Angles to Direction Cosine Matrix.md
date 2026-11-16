---
type: simulink-block
title: 'Rotation Angles to Direction Cosine Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'rotationanglestodirectioncosinematrix'
documentation_source_path: 'rotationanglestodirectioncosinematrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotation Angles to Direction Cosine Matrix

## 端口

### 输入

### **[R1,R2,R3]** — 旋转角 3×1 向量

旋转角，指定为 3×1 向量，单位为 radians。

**数据类型：** `double`
### 输出

### **DCM** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，基于旋转角执行坐标变换，返回为 3×3 矩阵。

**数据类型：** `double`

## 参数

### **旋转顺序** — 旋转顺序 `ZYX` (默认) | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

三个旋转角的输入旋转顺序。

#### 编程用法

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

**在 R2007b 中引入**

## 描述

将旋转角转换为方向余弦矩阵

Rotation Angles to Direction Cosine Matrix 模块根据给定的一组旋转角 R1、R2 和 R3 确定方向余弦矩阵 (DCM)。例如，默认旋转角顺序 `ZYX` 表示如下序列：R1 为 *z* 轴旋转（偏航），R2 为 *y* 轴旋转（俯仰），R3 为 *x* 轴旋转（滚转）。使用 **旋转顺序** 参数更改该序列。这些旋转角表示从坐标系 A 到坐标系 B 的一系列右手内旋被动变换。得到的方向余弦矩阵表示从坐标系 A 到坐标系 B 的右手旋转。
