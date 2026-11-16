---
type: simulink-block
title: 'LLA to ECEF Position'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'llatoecefposition'
documentation_source_path: 'llatoecefposition.html'
language: zh-CN
chinese_source: worker-translation
---

# LLA to ECEF Position

## 端口

### 输入

### **μ l** — 大地纬度和经度 2×1 向量

大地纬度和经度，指定为 2×1 向量，单位为 degrees。

**数据类型：** `double`

### **h** — 高度标量

行星椭球上方的高度，指定为标量。

**数据类型：** `double`
### 输出

### **Xf** — 位置 3×1 向量

ECEF 坐标系中的位置，以 3×1 向量返回，单位与 **h** 端口处的输入相同。

**数据类型：** `double`

## 参数

### **单位** — 单位 `Metric (MKS)` (默认) | `English`

参数和输出单位：

| 单位 | 从 CG 到行星中心的半径 | 赤道半径 |
| --- | --- | --- |
| `Metric (MKS)` | Meters | Meters |
| `English` | Feet | Feet |

#### 依赖项

要启用此参数，请将 **行星模型** 设置为 `Earth (WGS84)`。

#### 编程用法

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **行星模型** — 行星模型 `Earth (WGS84)` (默认) | `Custom`

要使用的行星模型，`Custom` 或 `Earth (WGS84)`。

#### 编程用法

|  |
| --- |
| **模块参数**: `ptype` |
| **类型**: character vector |
| **值**: `'Earth (WGS84)'` | `'Custom'` |
| **默认值**: `'Earth (WGS84)'` |

### **扁率** — 行星扁率 `1/298.257223563` (默认) | 标量

行星的扁率，指定为 double 标量。

#### 依赖项

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**: `F` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `1/298.257223563` |

### **行星赤道半径** — 行星赤道处的半径 `6378137` (默认) | 标量

行星在其赤道处的半径，单位与 ECEF 位置所需单位相同。

#### 依赖项

要启用此参数，请将 **行星模型** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**: `R` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `6378137` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

根据大地纬度、经度和行星椭球上方的高度计算地心地固 (ECEF) 位置

LLA to ECEF Position 模块将大地纬度 (μ¯)、经度 (ι¯) 和行星椭球上方的高度 (h¯) 转换为 ECEF 位置的 3×1 向量 (p¯)。纬度和经度值可以为任意值。但是，由于两极处的奇异性，纬度值 +90 和 -90 可能返回意外值。有关 ECEF 位置计算的详细信息，请参阅算法。
