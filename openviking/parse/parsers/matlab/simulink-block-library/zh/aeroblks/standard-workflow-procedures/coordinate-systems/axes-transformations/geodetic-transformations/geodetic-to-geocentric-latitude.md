---
type: simulink-block
title: 'Geodetic to Geocentric Latitude'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Standard Workflow Procedures / Coordinate Systems / Axes Transformations / Geodetic Transformations'
documentation_page: 'geodetictogeocentriclatitude'
documentation_source_path: 'geodetictogeocentriclatitude.html'
language: zh-CN
chinese_source: worker-translation
---

# Geodetic to Geocentric Latitude

## 端口

### 输入

### **μ** — 大地纬度标量

大地纬度，指定为标量，以度为单位。纬度值
可以为任意值。但是，由于极点处的奇异性，+90 和 -90 的值可能返回意外
值。

**数据类型：** `double`

### **h** — 椭球高度标量

椭球高度，指定为标量。

**数据类型：** `double`
### 输出

### **λ** — 地心纬度标量

包含地心纬度，指定为标量，以
度为单位。

**数据类型：** `double`

### **r** — 半径标量

从行星中心到重心的半径，返回为标量。

#### 依赖关系

要启用此端口，请选择 **Output
radius**。

**数据类型：** `double`

## 参数

### **Units** — 单位 `Metric (MKS)` (默认) | `English`

参数和输出单位：

| 单位 | 从 CG 到行星中心的半径 | 赤道半径 |
| --- | --- | --- |
| `Metric (MKS)` | Meters | Meters |
| `English` | Feet | Feet |

#### 编程用法

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **Planet model** — 行星模型 `Earth (WGS84)` (默认) | `Custom`

要使用的行星模型，`Custom` 或
`Earth (WGS84)`。

#### 依赖关系

选择 `Custom` 选项会启用以下参数：

- **Flattening**
- **Equatorial radius of planet**

#### 编程用法

|  |
| --- |
| **模块参数**：`ptype` |
| **类型**：character vector |
| **值**：`'Earth (WGS84)'` | `'Custom'` |
| **默认值**：`'Earth (WGS84)'` |

### **Flattening** — 扁率 `1/298.257223563` (默认) | 标量

行星的扁率，指定为 double scalar。

#### 依赖关系

当 **Planet
model** 设置为 `Custom` 时，此参数启用。

#### 编程用法

|  |
| --- |
| **模块参数**：`F` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`1/298.257223563` |

### **Equatorial radius of planet** — 半径 `6378137.0` (默认) | 标量

行星赤道处的半径，单位与 **Units**
参数相同。

#### 依赖关系

当 **Planet
model** 设置为 `Custom` 时，此参数启用。

#### 编程用法

|  |
| --- |
| **模块参数**：`R` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`6378137` |

### **Output radius** — 启用半径输出 `off` (默认) | on

选中此复选框可输出从赤道半径到
行星中心的标量距离半径。

#### 依赖关系

选中此复选框可启用 **r**
端口。

#### 编程用法

|  |
| --- |
| **模块参数**：`outputRadius` |
| **类型**：character vector |
| **值**：`off` | `on` |
| **默认值**：`'off'` |

## 所属库

Aerospace Blockset / Utilities / Axes Transformations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将大地纬度转换为地心纬度

Geodetic to Geocentric Latitude 模块使用大地纬度和椭球高度，将大地
纬度 (*μ*) 转换为地心纬度 (*λ*) 以及
可选的从行星中心到重心的
半径 (`r`)。有关地心纬度的更多
信息，请参阅算法。
