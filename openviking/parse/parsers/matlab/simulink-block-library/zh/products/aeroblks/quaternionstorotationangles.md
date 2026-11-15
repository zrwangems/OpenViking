---
type: simulink-block
title: 'Quaternions to Rotation Angles'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'quaternionstorotationangles'
documentation_source_path: 'quaternionstorotationangles.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternions to Rotation Angles

## 端口

### 输入

### **q** — 四元数 4×1 向量

四元数，指定为 4×1 向量。

**数据类型：** `double`

### 输出

### **[R1,R2,R3]** — 旋转角度 3×1 向量

旋转角度，返回的 3×1 向量，以 radians 为单位。

**数据类型：** `double`

## 参数

### **旋转顺序** — 旋转顺序 `ZYX`（默认）| `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

三个旋转角度的输出旋转顺序。

#### 编程用法

|  |
| --- |
| **模块参数**: `rotationOrder` |
| **类型**: character vector |
| **值**: `ZYX` | `ZYZ` |`ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX` |
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

从四元数确定旋转向量

Quaternions to Rotation Angles 模块将四元素
四元数向量（*q*0,
*q*1,
*q*2,
*q*3）转换为由
三个旋转角度（R1, R2, R3）描述的旋转。该模块通过计算
方向余弦矩阵（DCM）中作为旋转角度函数的元素来生成转换。DCM
中的元素是单位四元数向量的函数。Aerospace Blockset™ 使用按
标量在前约定定义的四元数。此
模块会归一化所有四元数输入。生成的旋转角度表示从坐标系 A 到坐标系 B 的一系列
右手内旋被动旋转。四元数
表示从坐标系 A 到坐标系 B 的右手被动变换。有关
方向余弦矩阵的更多信息，请参阅算法。
