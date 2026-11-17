---
type: simulink-block
title: 'Horizontal Wind Model 14'
family: 'environment'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'horizontalwindmodel14'
documentation_source_path: 'horizontalwindmodel14.html'
language: zh-CN
chinese_source: worker-translation
---

# Horizontal Wind Model 14

## 端口

### 输入

### **First** — 大地纬度 (μ)、经度 (`l`) 和位势高度 (`h`) 三元素 double 向量

该输入指定模块实现模型时所用的大地纬度 (μ)、经度
(`l`) 和位势高度 (`h`)。

纬度和经度值以度为单位。

高度值使用你在 **Units** 参数中选择的单位。
将高度元素指定为 0 到 500 km 之间的值。超出 0 到 500 km 范围的值将保持在边界。

### **Second** — 一年中的第几天标量 double

该输入指定协调世界时 (UTC) 下的一年中的第几天。该输入将一年中的第几天指定为 1 到 366（闰年）之间的值。值会在 1 到 366 天范围内回绕。

### **Third** — 经过的秒数标量 double

包含所选日期在 UTC 中自午夜以来经过的秒数。

### **Fourth (Optional)** — Ap 指数标量 double

包含模块评估模型时的世界时 (UT) 对应的 Ap 指数。从 NOAA
National Geophysical Data Center 选择该指数，其中包含 3 小时间隔的地磁扰动指数值。如果 Ap 指数值大于零，软件在模型评估期间会考虑磁效应。

### 输出

### **First** — 风速度矢量 1-by-2 double 向量

风速度矢量按该顺序包含经向和纬向风分量。

## 参数

### **Units** — 输入和输出单位 `Metric (MKS)` (默认) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

风速和风速度的输入和输出单位，指定为：

| 单位 | 风速 | 风速度 |
| --- | --- | --- |
| `Metric (MKS)` | Meters per second | Meters per second |
| `English (Velocity in ft/s)` | Feet per second | Feet per second |
| `English (Velocity in kts)` | Knots | Knots |

#### 程序化使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**: `'Metric (MKS)'` |

### **Model** — 水平风模型 `Quiet` (默认) | `Total` | `Disturbance`

选择要计算风分量的水平风模型类型。

- `Quiet`

  计算不含磁扰动的水平风模型。对于此模型类型，不要输入 Ap 指数值。
- `Total`

  计算平静条件和磁扰动的组合效应。对于此模型类型，输入大于或等于零的 Ap 指数值。
- `Disturbance`

  计算风中磁扰动的效应。对于此模型类型，输入大于或等于零的 Ap 指数值。

#### 程序化使用

|  |
| --- |
| **模块参数**: `model` |
| **类型**: character vector |
| **值**: `'Quiet'` | `'Total'` | `'Disturbance'` |
| **默认值**: `'Quiet'` |

### **Action for out-of-range input** — 模块行为 `Error` (默认) | `Warning` | `None`

指定当模块输入超出范围时的模块行为。

| 值 | 描述 |
| --- | --- |
| `Error` (默认) | MATLAB® 返回异常，模型仿真停止。对于 Accelerator 和 Rapid Accelerator 模式，将操作设置为 `Error` 无效，模型的行为如同操作设置为 `None`。 |
| `Warning` | 在诊断查看器中显示警告，模型仿真继续。对于 Accelerator 和 Rapid Accelerator 模式，将操作设置为 `Warning` 无效，模型的行为如同操作设置为 `None`。 |
| `None` | 不执行操作。模块对输入信号施加上限和下限。 |

#### 程序化使用

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'Error'` |

## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2021b：Horizontal Wind Model 14 模块可能更改了返回值

Horizontal Wind Model 14 模块现在接受：

- **day** 端口值，其为小数、负数、
  `0` 或大于 `366` 的值。
- **sec** 端口值，其为 `0` 或
  大于 `86400` 的值。

因此，此模块的输出值可能与之前的版本不同。

## 描述

实现 Horizontal Wind Model 14

Horizontal Wind Model 14 模块实现 U.S. Naval Research Laboratory (HWM™) 例程，以针对一组地理坐标：纬度、经度和高度，计算风的经向和纬向分量。
