---
type: simulink-block
title: 'Direction Cosine Matrix ECEF to NED to Latitude and Longitude'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'directioncosinematrixeceftonedtolatitudeandlongitude'
documentation_source_path: 'directioncosinematrixeceftonedtolatitudeandlongitude.html'
language: zh-CN
chinese_source: worker-translation
---

# Direction Cosine Matrix ECEF to NED to Latitude and Longitude

## 端口

### 输入

### **DCMef** — 方向余弦矩阵 3×3 矩阵

用于求取大地纬度和经度的方向余弦矩阵，指定为 3×3 矩阵。

**数据类型:** `double`
### 输出

### **μl** — 大地纬度和经度 2×1 向量

大地纬度和经度，以 degrees 为单位返回为 2×1 向量。

**数据类型:** `double`

## 参数

### **无效 DCM 的操作** — 模块行为 `None` (默认) | `Warning` | `Error`

当方向余弦矩阵无效（不正交）时的模块行为。

- `Warning` — 显示指示方向余弦矩阵无效的警告。
- `Error` — 显示指示方向余弦矩阵无效的错误。
- `None` — 不显示警告或错误（默认）。

#### 编程用法

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'None'` |

**数据类型:** `char` | `string`

### **DCM 验证容差** — 容差 `eps(2)` (默认) | scalar

方向余弦矩阵有效性的容差，指定为 scalar。如果以下条件成立，模块将方向余弦矩阵视为有效：

- 方向余弦矩阵的转置与其自身相乘在指定容差内等于 `1`（`transpose(n)*n == 1±tolerance`）。
- 方向余弦矩阵的行列式在指定容差内等于 `1`（`det(n) == 1±tolerance`）。

#### 编程用法

|  |
| --- |
| **模块参数**: `tolerance` |
| **类型**: character vector |
| **值**: `'eps(2)'` | scalar |
| **默认值**: `'eps(2)'` |

**数据类型:** `double`

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将方向余弦矩阵转换为大地纬度和经度

Direction Cosine Matrix ECEF to NED to Latitude and Longitude 模块将 3×3 方向余弦矩阵 (DCM) 转换为大地纬度和经度。该 DCM 矩阵执行坐标变换，将地心地固 (ECEF) 轴中的向量 (*ox*0, *oy*0, *oz*0) 转换为大地纬度和经度。有关方向余弦矩阵的更多信息，请参阅算法。
