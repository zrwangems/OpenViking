---
type: simulink-block
title: 'Horizontal Wind Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'horizontalwindmodel'
documentation_source_path: 'horizontalwindmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Horizontal Wind Model

## 端口

### 输入

### **DCM** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，指定为表示从平面地球坐标系到体轴坐标系的 3×3 矩阵。

**数据类型：** `double`

### **Vwind** — 风速 1×3 向量

风速，指定为 1×3 向量，采用所选单位。

#### 依赖关系

要启用此参数，请将 **风速源** 设置为 `External`。

**数据类型：** `double`

### **θwind** — 风向标量

风向，指定为标量，单位为 degrees。风向从地球 *x* 轴方向（北）顺时针测量，单位为 degrees。风向定义为风吹来的方向。

#### 依赖关系

要启用此参数，请将 **风向源** 设置为 `External`。

**数据类型：** `double`
### 输出

### **Vwind** — 风速矢量 3×3 矩阵

风速矢量，以三元素信号形式返回，采用与 **DCM** 输入相同的体坐标系参考，并使用指定单位。

**数据类型：** `double`

## 参数

### **单位** — 输入和输出单位 `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 风速 | 风速矢量 |
| --- | --- | --- |
| `Metric (MKS)` | Meters per second | Meters per second |
| `English (Velocity in ft/s)` | Feet per second | Feet per second |
| `English (Velocity in kts)` | Knots | Knots |

#### 编程用法

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English (Velocity in kts)'` | `'English (Velocity in ft/s)'` |
| **默认值**: `'Metric (MKS)'` |

### **风速源** — 风速源 `Internal` (default) | `External`

风速源，指定为：

|  |  |
| --- | --- |
| `External` | 可变风速输入到模块 |
| `Internal` | 在掩码中指定的恒定风速 |

#### 依赖关系

- 将此参数设置为 `Internal`
  会启用 **高度处的风速**。
- 将此参数设置为 `External`
  会启用 **Vwind**
  输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**: `Vw_source` |
| **类型**: character vector |
| **值**: `'Internal'` | `'External'` |
| **默认值**: `'Internal'` |

### **高度处的风速 (m/s)** — 风速 `15` (default) | scalar

恒定风速，指定为 double 标量，采用指定单位。

#### 依赖关系

要启用此参数，请将 **风速源** 设置为 `Internal`。

#### 编程用法

|  |
| --- |
| **模块参数**: `Vwind` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'15'` |

### **风向源** — 风向源 `Internal` (default) | `External`

风向源，指定为：

|  |  |
| --- | --- |
| `External` | 可变风向输入到模块 |
| `Internal` | 在掩码中指定的恒定风向 |

#### 依赖关系

- 将此参数设置为 `Internal`
  会启用 **高度处的风向（从北顺时针的 degrees）**。
- 将此参数设置为 `External`
  会启用 **θwind**
  输入端口。

#### 编程用法

|  |
| --- |
| **模块参数**: `W_source` |
| **类型**: character vector |
| **值**: `'Internal'` | `'External'` |
| **默认值**: `'Internal'` |

### **高度处的风向（从北顺时针的 degrees）** — 风向 `0` (default)

恒定风向，指定为标量，以从地球 *x* 轴方向（北）顺时针的 degrees 为单位。风向为风吹来的方向。

#### 依赖关系

要启用此参数，请将 **风向源** 设置为 `Internal`。

#### 编程用法

|  |
| --- |
| **模块参数**: `Wdeg` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'0'` |

## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将水平风转换到体轴坐标

Horizontal Wind Model 模块计算体轴坐标下的风速矢量。

风由地球坐标系中的风速和风向指定。风速和风向可以是恒定的，也可以是随时间变化的。风向从地球 *x* 轴方向（北）顺时针测量，单位为 degrees。风向定义为风吹来的方向。使用方向余弦矩阵 (DCM)，风速矢量被转换到体轴坐标。
