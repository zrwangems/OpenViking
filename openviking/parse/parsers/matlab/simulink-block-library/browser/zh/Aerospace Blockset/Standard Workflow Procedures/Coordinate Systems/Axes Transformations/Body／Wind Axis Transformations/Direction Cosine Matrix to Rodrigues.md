---
type: simulink-block
title: 'Direction Cosine Matrix to Rodrigues'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixtorodrigues'
documentation_source_path: 'directioncosinematrixtorodrigues.html'
language: zh-CN
chinese_source: worker-translation
---

# Direction Cosine Matrix to Rodrigues

## 端口

### 输入

### **DCM** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，指定为 3×3 矩阵，用于确定 Euler-Rodrigues 向量。

**数据类型：** `double`
### 输出

### **rod** — Euler-Rodrigues 向量 三元素向量

Euler-Rodrigues 向量，返回为三元素向量。

**数据类型：** `double`

## 参数

### **对无效 DCM 的操作** — 模块行为 `None`（默认） | `Warning` | `Error`

当方向余弦矩阵无效（非正交）时的模块行为。

- `Warning` — 显示警告，并指示方向余弦矩阵无效。
- `Error` — 显示错误，并指示方向余弦矩阵无效。
- `None` — 不显示警告或错误（默认）。

#### 编程用法

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'None'` |

**数据类型：** `char` | `string`

### **DCM 验证容差** — 容差 `eps(2)`（默认） | 标量

方向余弦矩阵有效性的容差，指定为标量。当以下条件为真时，模块认为方向余弦矩阵有效：

- 方向余弦矩阵的转置与其自身相乘在指定容差内等于 `1`
  （`transpose(n)*n == 1±tolerance`）
- 方向余弦矩阵的行列式在指定容差内等于 `1`
  （`det(n) == 1±tolerance`）。

#### 编程用法

|  |
| --- |
| **模块参数**: `tolerance` |
| **类型**: character vector |
| **值**: `'eps(2)'` | 标量 |
| **默认值**: `'eps(2)'` |

**数据类型：** `double`

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

将方向余弦矩阵转换为 Euler-Rodrigues 向量

Direction Cosine Matrix to Rodrigues 模块根据三元素 Euler-Rodrigues 向量确定 3×3 方向余弦矩阵。输入方向余弦矩阵和所得 Euler-Rodrigues 向量表示从坐标系 A 到坐标系 B 的右手被动变换。有关方向余弦矩阵的更多信息，请参阅算法。
