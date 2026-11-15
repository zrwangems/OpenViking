---
type: simulink-block
title: 'Geoid Height'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Gravity'
documentation_page: 'geoidheight'
documentation_source_path: 'geoidheight.html'
language: zh-CN
chinese_source: worker-translation
---

# Geoid Height

## 端口

### 输入

### **μ (deg)** — 大地纬度标量

大地纬度，指定为标量，单位为 degrees，其中北纬为正，南纬为负。输入纬度必须为 single 或 double 类型。如果纬度不在 –90 到 90 范围内，模块会将其回绕到该范围内。

**数据类型：** `double` | `single`

### **l (deg)** — 经度标量

经度，指定为标量，单位为 degrees，其中东经为正，范围为 0 到 360。输入经度必须为 single 或 double 类型。如果经度不在 0 到 360 范围内，当**超出范围输入的操作**设置为 `None` 或 `Warning` 时，模块会将其回绕到该范围内。当**超出范围输入的操作**设置为 `Error` 时，模块不会回绕。

**数据类型：** `double` | `single`
### 输出

### **N** — 大地水准面高度标量

大地水准面高度，以选定的长度单位返回为标量。数据类型与第一个输入中的纬度相同。

**数据类型：** `double` | `single`

## 参数

### **单位** — 参数和输出单位 `Metric (MKS)` (默认) | `English`

参数和输出单位，指定为：

| 单位 | 高度 |
| --- | --- |
| `Metric (MKS)` | Meters |
| `English` | Feet |

#### 编程使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **地球重力场模型** — 地球重力场模型 `EGM96` (默认) | `EGM2008` | `Custom`

地球重力场模型，指定为：

| 地球重力场模型 | 描述 |
| --- | --- |
| `EGM96 (Earth)` | 默认。EGM96 地球重力场模型的阶和次为 360。此模型在无潮系统中使用 15-minute 的点值网格。对于此模型，此模块计算大地水准面高度的精度为 0.01 m。 |
| `EGM2008 (Earth)` | EGM2008 地球重力场模型的阶和次为 2159。此模型在无潮系统中使用 2.5-minute 的点值网格。对于此模型，此模块计算大地水准面高度的精度为 0.001 m。  **注意**  此模块要求你使用附加功能资源管理器下载 EGM2008 地球重力场模型的大地水准面数据。点击 **获取数据** 按钮以启动附加功能资源管理器。有关详细信息，请参阅 `aeroDataPackage`。如果已安装数据，则不会显示 **获取数据** 按钮。 |
| `Custom` | 在 **地球重力场 MAT 文件** 中定义的自定义地球重力场模型。对于自定义模型，此模块计算大地水准面高度的精度为 0.01 m。选择 `Custom` 会启用 **地球重力场 MAT 文件** 参数。 |

#### 编程使用

|  |
| --- |
| **模块参数**: `gtype` |
| **类型**: character vector |
| **值**: `'EGM96'` | `'EGM2008'` | `'Custom'` |
| **默认值**: `'Earth'` |

### **地球重力场 MAT 文件** — 地球重力场 MAT 文件 `'geoidegm96grid'` (默认) | MAT 文件

定义自定义地球重力场模型的地球重力场 MAT 文件。

#### 依赖项

要启用此项，请将 **地球重力场模型** 设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**: `datafile` |
| **类型**: character vector |
| **值**: `'geoidegm96grid'` | MAT 文件 |
| **默认值**: `'geoidegm96grid'` |

### **数据类型** — 输入和输出信号的数据类型 `double` (默认) | `single`

输入和输出信号的数据类型，指定为 `double` 或 `single`。

#### 编程使用

|  |
| --- |
| **模块参数**: `dtype` |
| **类型**: character vector |
| **值**: `'double'` | `'single'` |
| **默认值**: `'double'` |

### **超出范围输入的操作** — 超出范围输入行为 `Warning` (默认) | `Error` | `None`

超出范围输入行为（纬度超出 –90 到 90 degrees，经度超出 0 到 360 degrees），指定如下。

| 操作 | 描述 |
| --- | --- |
| `None` | 无操作。 |
| `Warning` | 在诊断查看器中发出警告。 |
| `Error` (默认) | MATLAB® 返回异常，模型仿真停止。 |

#### 编程使用

|  |
| --- |
| **模块参数**: `action` |
| **类型**: character vector |
| **值**: `'None'` | `'Warning'` | `'Error'` |
| **默认值**: `'Warning'` |

## 所属库

Aerospace Blockset / Environment / Gravity

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010b 中引入**

## 描述

计算起伏/高度

Geoid Height 模块使用 **地球重力场模型** 参数计算大地水准面高度。该模块在无潮系统中从点值网格插值大地水准面高度。它使用指定的地球重力场模型，达到该模型的阶和次。大地水准面起伏相对于 WGS84 椭球。

插值方案在极点上进行回绕，以允许在这些位置及其附近进行大地水准面高度计算。
