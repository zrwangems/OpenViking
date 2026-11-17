---
type: simulink-block
title: 'Rotation Angles to Direction Cosine Matrix'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'TRN'
documentation_page: 'rotationanglestodirectioncosinematrix'
documentation_source_path: '../aeroblks/rotationanglestodirectioncosinematrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotation Angles to Direction Cosine Matrix

## 端口

### 输入

### **[R1,R2,R3]** — 旋转角度 3×1 向量

旋转角度，指定为 3×1 向量，单位为弧度。

**数据类型：** `double`
### 输出

### **DCM** — 方向余弦矩阵 3×3 矩阵

基于旋转角度执行坐标变换的方向余弦矩阵，返回为 3×3 矩阵。

**数据类型：** `double`

## 参数

### **Rotation Order** — 旋转顺序 `ZYX`（默认）| `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

三个旋转角度的输入旋转顺序。

#### 编程使用

|  |
| --- |
| **模块参数**：`rotationOrder` |
| **类型**：字符向量 |
| **值**：`'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **默认值**：`'ZYX'` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

## 描述

将旋转角度转换为方向余弦矩阵

Rotation Angles to Direction Cosine Matrix 模块根据给定的一组旋转角度 R1、R2 和 R3 确定方向余弦矩阵（DCM）。例如，默认旋转角度顺序 `ZYX` 表示一个序列，其中 R1 为 *z* 轴旋转（偏航），R2 为 *y* 轴旋转（俯仰），R3 为 *x* 轴旋转（滚转）。使用 **Rotation Order** 参数可更改该序列。旋转角度表示从坐标系 A 到坐标系 B 的一系列右手本征被动变换。得到的方向余弦矩阵表示从坐标系 A 到坐标系 B 的右手旋转。
