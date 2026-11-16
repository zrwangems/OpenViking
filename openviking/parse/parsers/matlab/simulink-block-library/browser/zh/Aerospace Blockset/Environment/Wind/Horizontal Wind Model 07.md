---
type: simulink-block
title: 'Horizontal Wind Model 07'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'horizontalwindmodel07'
documentation_source_path: 'horizontalwindmodel07.html'
language: zh-CN
chinese_source: worker-translation
---

# Horizontal Wind Model 07

## 端口

### 输入

### **μ l h** — 大地纬度、经度和位势高度三元素向量 | 高度为 0 到 500 km 之间的值

大地纬度 (μ)、经度 (l) 和位势高度 (h)，指定为三元素向量。

纬度和经度值以度为单位。

高度值保持在 0 到 500 km 的范围之外。高度值使用在 **Units** 中选择的单位。

**数据类型：** `double`

### **day** — 日标量 | 值介于 1 和 366 之间

协调世界时 (UTC) 的一年中的第几天，指定为 1 到 366 之间的值（用于闰年）。值会环绕在 1 到 366 天的范围内。

**数据类型：** `double`

### **sec** — 经过秒数标量

指定日期自午夜以来经过的秒数（UTC）。

**数据类型：** `double`

### **Ap** — Ap 指数标量 | 范围从 0 到 400

用于世界时 (UT) 的 Ap 指数，指定为标量，范围为 0 到 400。从 NOAA National Geophysical Data Center 选择该指数，其中包含 3 小时间隔的地磁扰动指数值。如果 Ap 指数值大于零，软件在模型评估期间会考虑磁效应。

#### 依赖项

要启用此端口，请将 **Model** 设置为 `Total` 或 `Disturbance`。

**数据类型：** `double`

### 输出

### **Vwind** — 风速向量 1×2 向量

风速向量，返回为 1×2 向量，按顺序包含经向和纬向风分量。

**数据类型：** `double`

## 参数

### **Units** — 输入和输出单位 `Metric (MKS)`（默认） | `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 风速 | 风速度 |
| --- | --- | --- |
| `Metric (MKS)` | Meters per second | Meters per second |
| `English (Velocity in ft/s)` | Feet per second | Feet per second |
| `English (Velocity in kts)` | Knots | Knots |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Model** — 水平风模型类型 `Quiet`（默认） | `Total` | `Disturbance`

要计算风分量的水平风模型类型，指定为：

- `Disturbance`

  仅计算风中的磁扰动效应。
- `Quiet`

  计算不含磁扰动的水平风模型。
- `Total`

  计算平静状态和磁扰动的综合效应。

#### 程序化使用

|  |
| --- |
| **模块参数**：`model` |
| **类型**：character vector |
| **值**：`'Quiet'` | `'Total'` | `'Disturbance'` |
| **默认值**：`'Quiet'` |

### **Action for out-of-range input** — 超出范围的模块行为 `Error`（默认） | `Warning` | `None`

超出范围的模块行为，指定如下。

| 值 | 说明 |
| --- | --- |
| `None` | 无操作。模块对输入信号施加上限和下限。 |
| `Warning` | Diagnostic Viewer 中显示警告，模型仿真继续。对于 Accelerator 和 Rapid Accelerator 模式，将操作设置为 `Warning` 无效，模型的行为如同操作设置为 `None`。 |
| `Error` | MATLAB® 返回异常，模型仿真停止。对于 Accelerator 和 Rapid Accelerator 模式，将操作设置为 `Error` 无效，模型的行为如同操作设置为 `None`。 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |

## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2021b：Horizontal Wind Model 07 模块返回的值可能已更改

Horizontal Wind Model 07 模块现在接受：

- **day** 端口值可以是小数、负数、`0` 或大于 `366`。
- **sec** 端口值为 `0` 或大于 `86400`。

因此，此模块的输出值可能不同于先前版本。

## 描述

实现 Horizontal Wind Model 07

Horizontal Wind Model 07 模块实现 U.S. Naval Research Laboratory HWM™ 例程，以计算一组地理坐标（纬度、经度和高度）下的经向和纬向风分量。
