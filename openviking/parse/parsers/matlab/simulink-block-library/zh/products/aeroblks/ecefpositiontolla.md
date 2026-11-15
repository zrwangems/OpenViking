---
type: simulink-block
title: 'ECEF Position to LLA'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'ecefpositiontolla'
documentation_source_path: 'ecefpositiontolla.html'
language: zh-CN
chinese_source: worker-translation
---

# ECEF Position to LLA

## 端口

### 输入

### **Xf** — 位置 3×1 向量

ECEF 坐标系中的位置，指定为 3×1 向量。

**数据类型：** `double`
### 输出

### **μ l** — 大地纬度和经度 2×1 向量

大地纬度和经度，以 2×1 向量形式返回，单位为 degrees。

**数据类型：** `double`

### **h** — 高度标量

行星椭球面上方高度，以标量形式返回，单位与 ECEF 位置相同。

**数据类型：** `double`

## 参数

### **Units** — 输出单位 `Metric (MKS)`（默认） | `English`

输出单位，指定为：

| 单位 | 位置 | 赤道半径 | 高度 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters | Meters | Meters |
| `English` | Feet | Feet | Feet |

#### 依赖关系

要启用此参数，请将 **Planet
model** 设置为 `Earth (WGS84)`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English'` |
| **默认值**: `'Metric (MKS)'` |

### **Planet model** — 行星模型 `Earth (WGS84)`（默认） | `Custom`

要使用的行星模型，`Custom` 或 `Earth (WGS84)`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ptype` |
| **类型**: character vector |
| **值**: `'Earth (WGS84)'` | `'Custom'` |
| **默认值**: `'Earth (WGS84)'` |

### **Flattening** — 行星扁率 `1/298.257223563`（默认） | scalar

行星的扁率，指定为 double scalar。

#### 依赖关系

要启用此参数，请将 **Planet model** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `F` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'1/298.257223563'` |

### **Equatorial radius of planet** — 赤道处的行星半径 `6378137`（默认） | scalar

行星赤道处的半径，指定为 double scalar，所用单位与 ECEF 位置的所需单位相同。

#### 依赖关系

要启用此参数，请将 **Planet model** 设置为
`Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `R` |
| **类型**: character vector |
| **值**: double scalar |
| **默认值**: `'6378137'` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

根据地心地固（ECEF）位置计算大地纬度、经度和行星椭球面上方高度

ECEF Position to LLA 模块将 3×1 的 ECEF 位置向量（p¯）转换为大地纬度（μ¯）、经度（ι¯）和行星椭球面上方高度（h¯）。有关 ECEF
位置的详细信息，请参阅 Algorithms。
