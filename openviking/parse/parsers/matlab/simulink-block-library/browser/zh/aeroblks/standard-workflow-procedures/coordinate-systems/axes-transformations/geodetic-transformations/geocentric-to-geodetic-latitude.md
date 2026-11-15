---
type: simulink-block
title: 'Geocentric to Geodetic Latitude'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'geocentrictogeodeticlatitude'
documentation_source_path: 'geocentrictogeodeticlatitude.html'
language: zh-CN
chinese_source: worker-translation
---

# Geocentric to Geodetic Latitude

## 端口

### 输入

### **λ** — 地心纬度标量

地心纬度，指定为标量，单位为 degrees。纬度值可为任意值。但是，由于极点处存在奇异点，+90 和 -90 的值可能返回意外值。

**数据类型：** `double`

### **r** — 半径标量

从行星中心到重心的半径，指定为标量。

**数据类型：** `double`
### 输出

### **μ** — 大地纬度标量

大地纬度，指定为标量，单位为 degrees。

**数据类型：** `double`

### **h** — 椭球高度标量

椭球高度，以标量形式返回。

#### 依赖关系

要启用此端口，请选择 **输出高度**。

**数据类型：** `double`

## 参数

### **单位** — 单位 `Metric (MKS)` (default) | `English`

参数和输出单位：

| 单位 | 从 CG 到行星中心的半径 | 赤道半径 |
| --- | --- | --- |
| `Metric (MKS)` | Meters | Meters |
| `English` | Feet | Feet |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **行星模型** — 行星模型 `Earth (WGS84)` (default) | `Custom`

要使用的行星模型，`Custom` 或 `Earth (WGS84)`。

#### 编程使用

|  |
| --- |
| **模块参数**：`ptype` |
| **类型**：character vector |
| **值**：`'Earth (WGS84)'` | `'Custom'` |
| **默认值**：`'Earth (WGS84)'` |

### **扁率** — 扁率 `1/298.257223563` (default) | 标量

行星的扁率，指定为 double scalar。

#### 依赖关系

当 **行星模型** 设置为 `Custom` 时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`F` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`1/298.257223563` |

### **行星赤道半径** — 半径 `6378137.0` (default) | 标量

行星在其赤道处的半径，单位与 **单位** 参数相同。

#### 依赖关系

当 **行星模型** 设置为 `Custom` 时，此参数启用。

#### 编程使用

|  |
| --- |
| **模块参数**：`R` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`6378137` |

### **输出高度** — 启用椭球高度 `off` (default) | on

选中此复选框以输出椭球高度。

#### 依赖关系

选中此复选框以启用 **h** 端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`outputAltitude` |
| **类型**：character vector |
| **值**：`off` | `on` |
| **默认值**：`'off'` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将地心纬度转换为大地纬度

Geocentric to Geodetic Latitude 模块使用地心纬度和从行星中心到重心的半径，将地心纬度（`λ`）转换为大地纬度（`μ`）以及可选的椭球高度（`h`）。该函数使用 Bowring 公式的迭代法计算大地纬度。有关详细信息，请参阅算法。
