---
type: simulink-block
title: 'Direction Cosine Matrix to Rotation Angles'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Body/Wind Axis Transformations'
documentation_page: 'directioncosinematrixtorotationangles'
documentation_source_path: 'directioncosinematrixtorotationangles.html'
language: zh-CN
chinese_source: worker-translation
---

# Direction Cosine Matrix to Rotation Angles

## 端口

### 输入

### **DCM** — 方向余弦矩阵，3×3 矩阵

用于确定旋转角的方向余弦矩阵，指定为 3×3 矩阵。

**数据类型：** `double`
### 输出

### **[R1,R2,R3]** — 旋转角，3×1 向量

旋转角，以 3×1 向量形式返回，单位为 radians。

**数据类型：** `double`

## 参数

### **旋转顺序** — 模块输出旋转顺序 `ZYX` (default) | `ZYZ` | `ZXY` | `ZXZ` | `YXZ` | `YXY` | `YZX` | `YZY` | `XYZ` | `XYX` | `XZY` | `XZX`

三个风旋转角的旋转顺序。

对于 `ZYX`、`ZXY`、`YXZ`、`YZX`、`XYZ` 和 `XZY` 旋转，模块生成的 R2 角介于 ±pi/2 radians 之间，R1 和 R3 角介于 ±pi radians 之间。

对于 `'ZYZ'`、`'ZXZ'`、`'YXY'`、`'YZY'`、`'XYX'` 和 `'XZX'` 旋转，模块生成的 R2 角介于 0 和 pi radians 之间，R1 和 R3 角介于 ±pi radians 之间。但是，在后一种情况下，R3 设置为 0 radians。

#### 程序化使用

|  |
| --- |
| **模块参数**：`rotationOrder` |
| **类型**：character vector |
| **值**：`'ZYX'` | `'ZYZ'` |`'ZXY'` | `'ZXZ'` | `'YXZ'` | `'YXY'` | `'YZX'` | `'YZY'` | `'XYZ'` | `'XYX'` | `'XZY'` | `'XZX'` |
| **默认值**：`'ZYX'` |

### **对无效 DCM 的操作** — 模块行为 `None` (default) | `Warning` | `Error`

当方向余弦矩阵无效（非正交）时的模块行为。

- `Warning` — 显示警告，指示方向余弦矩阵无效。
- `Error` — 显示错误，指示方向余弦矩阵无效。
- `None` — 不显示警告或错误（默认）。

#### 程序化使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'None'` |

**数据类型：** `char` | `string`

### **DCM 验证容差** — 容差 `eps(2)` (default) | scalar

方向余弦矩阵有效性的容差，指定为标量。如果以下条件成立，模块将方向余弦矩阵视为有效：

- 方向余弦矩阵的转置乘以自身在指定容差内等于 `1`（`transpose(n)*n == 1±tolerance`）。
- 方向余弦矩阵的行列式在指定容差内等于 `1`（`det(n) == 1±tolerance`）。

#### 程序化使用

|  |
| --- |
| **模块参数**：`tolerance` |
| **类型**：character vector |
| **值**：`'eps(2)'` | scalar |
| **默认值**：`'eps(2)'` |

**数据类型：** `double`

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

## 描述

将方向余弦矩阵转换为旋转角

Direction Cosine Matrix to Rotation Angles 模块将 3×3 方向余弦矩阵 (DCM) 转换为旋转角 R1、R2 和 R3。模块的 **旋转顺序** 参数指定模块输出旋转的顺序。例如，如果 **旋转顺序** 的值为 `ZYX`，则模块输出按旋转顺序 *`z-y-x`*（psi theta phi）排列。方向余弦矩阵表示从坐标系 A 到坐标系 B 的被动变换。得到的旋转角表示从坐标系 A 到坐标系 B 的一系列右手内旋被动旋转。
