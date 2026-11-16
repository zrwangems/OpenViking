---
type: simulink-block
title: 'Direction Cosine Matrix to Quaternions'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixtoquaternions'
documentation_source_path: 'directioncosinematrixtoquaternions.html'
language: zh-CN
chinese_source: worker-translation
---

# Direction Cosine Matrix to Quaternions

## 端口

### 输入

### **DCMbe** — 方向余弦矩阵 3-by-3 矩阵

用于将方向余弦矩阵转换为四元数的方向余弦矩阵，指定为 3-by-3。

**数据类型:** `double`

### 输出

### **q** — 四元数 4-by-1 向量

由变换返回的四元数，为 4-by-1 向量。

**数据类型:** `double`

## 参数

### **无效 DCM 的操作** — 模块行为 `None`（默认）| `Warning` | `Error`

当方向余弦矩阵无效（非正交）时的模块行为。

- `Warning` — 显示指示方向余弦矩阵无效的警告。
- `Error` — 显示指示方向余弦矩阵无效的错误。
- `None` — 不显示警告或错误（默认）。

#### 程序化使用

|  |
| --- |
| **模块参数**: `action` |
| **类型**: 字符向量 |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'None'` |

**数据类型:** `char` | `string`

### **DCM 验证容差** — 容差 `eps(2)`（默认）| 标量

方向余弦矩阵有效性的容差，指定为标量。如果以下条件为真，模块认为方向余弦矩阵有效：

- 方向余弦矩阵的转置乘以自身在指定容差内等于 `1`（`transpose(n)*n == 1±tolerance`）。
- 方向余弦矩阵的行列式在指定容差内等于 `1`（`det(n) == 1±tolerance`）。

#### 程序化使用

|  |
| --- |
| **模块参数**: `tolerance` |
| **类型**: 字符向量 |
| **值**: `'eps(2)'` | 标量 |
| **默认值**: `'eps(2)'` |

**数据类型:** `double`

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将方向余弦矩阵转换为四元数向量

Direction Cosine Matrix to Quaternions 模块将 3-by-3 方向余弦矩阵 (DCM) 转换为四元素单位四元数向量 (*q*0, *q*1, *q*2, *q*3)。Aerospace Blockset™ 使用按标量优先约定定义的四元数。方向余弦矩阵表示从坐标系 A 到坐标系 B 的被动变换。所得四元数表示从坐标系 A 到坐标系 B 的一系列内禀右手被动变换。有关方向余弦矩阵的更多信息，请参阅 Algorithms。
