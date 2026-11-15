---
type: simulink-block
title: 'Direction Cosine Matrix to Wind Angles'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixtowindangles'
documentation_source_path: 'directioncosinematrixtowindangles.html'
language: zh-CN
chinese_source: worker-translation
---

# Direction Cosine Matrix to Wind Angles

## 端口

### 输入

### **DCMwe** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，指定为 3×3 矩阵，用于将地球固定矢量变换为风固定矢量。

**数据类型：** `double`
### 输出

### **μ γ x** — 风角 3×1 向量

风角（滚转角、航迹角、航向角），以 3×1 向量形式返回，单位为 radians。

**数据类型：** `double`

## 参数

### **DCM 无效时的操作** — 模块行为 `None`（默认）| `Warning` | `Error`

当方向余弦矩阵无效（非正交）时的模块行为。

- `Warning` — 显示警告，指示
  方向余弦矩阵无效。
- `Error` — 显示错误，指示
  方向余弦矩阵无效。
- `None` — 不显示警告或
  错误（默认）。

#### 程序化使用

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **取值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'None'` |

**数据类型：** `char` | `string`

### **DCM 验证容差** — 容差 `eps(2)`（默认）| scalar

方向余弦矩阵有效性的容差，指定为标量。如果以下条件成立，模块将方向余弦矩阵视为有效：

- 方向余弦矩阵的转置乘以自身在指定容差内等于
  `1`（`transpose(n)*n == 1±tolerance`）。
- 方向余弦矩阵的行列式在指定容差内等于
  `1`（`det(n) == 1±tolerance`）。

#### 程序化使用

|  |
| --- |
| **模块参数**: `tolerance` |
| **类型**: character vector |
| **取值**: `'eps(2)'` | scalar |
| **默认值**: `'eps(2)'` |

**数据类型：** `double`

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将方向余弦矩阵转换为风角

Direction Cosine Matrix to Wind Angles 模块将 3×3 方向余弦矩阵 (DCM) 转换为三个风旋转角。DCM 矩阵执行向量从地球轴 (*ox*0, *oy*0, *oz*0) 到风轴 (*ox*3, *oy*3, *oz*3) 的坐标变换。有关方向余弦矩阵的更多信息，请参阅算法。

此实现生成介于 ±90 degrees 之间的航迹角，以及介于 ±180 degrees 之间的滚转角和航向角。
