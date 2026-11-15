---
type: simulink-block
title: 'Direction Cosine Matrix Body to Wind to Alpha and Beta'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixbodytowindtoalphaandbeta'
documentation_source_path: 'directioncosinematrixbodytowindtoalphaandbeta.html'
language: zh-CN
chinese_source: worker-translation
---

# Direction Cosine Matrix Body to Wind to Alpha and Beta

## 端口

### 输入

### **DCMwb** — 方向余弦矩阵 3×3 方向余弦矩阵

用于将机体固定向量变换为风固定向量的方向余弦矩阵，指定为 3×3 方向余弦矩阵。

**数据类型：** `double`
### 输出

### **α β** — 攻角和侧滑角 2×1 向量

攻角和侧滑角，以向量形式返回，单位为 radians。

**数据类型：** `double`

## 参数

### **无效 DCM 的操作** — 模块行为 `None` (默认) | `Warning` | `Error`

当方向余弦矩阵无效（非正交）时的模块行为。

- `Warning` — 显示警告，指示方向余弦矩阵无效。
- `Error` — 显示错误，指示方向余弦矩阵无效。
- `None` — 不显示警告或错误（默认）。

#### 程序化使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'None'` |

**数据类型：** `char` | `string`

### **DCM 验证容差** — 容差 `eps(2)` (默认) | 标量

方向余弦矩阵有效性的容差，指定为标量。如果满足以下条件，模块认为方向余弦矩阵有效：

- 方向余弦矩阵的转置乘以自身在指定容差内等于 `1`（`transpose(n)*n == 1±tolerance`）。
- 方向余弦矩阵的行列式在指定容差内等于 `1`（`det(n) == 1±tolerance`）。

#### 程序化使用

|  |
| --- |
| **模块参数**：`tolerance` |
| **类型**：字符向量 |
| **值**：`'eps(2)'` | 标量 |
| **默认值**：`'eps(2)'` |

**数据类型：** `double`

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将方向余弦矩阵转换为攻角和侧滑角

Direction Cosine Matrix Body to Wind to Alpha and Beta 模块将 3×3 方向余弦矩阵（DCM）转换为攻角和侧滑角。DCM 执行机体轴（*ox*0, *oy*0, *oz*0）中的向量到风轴（*ox*2, *oy*2, *oz*2）中的向量的坐标变换。有关方向余弦矩阵的更多信息，请参阅算法。
