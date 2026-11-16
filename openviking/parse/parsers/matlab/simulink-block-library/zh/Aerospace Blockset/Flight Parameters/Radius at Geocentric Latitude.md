---
type: simulink-block
title: 'Radius at Geocentric Latitude'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Flight Parameters'
documentation_page: 'radiusatgeocentriclatitude'
documentation_source_path: 'radiusatgeocentriclatitude.html'
language: zh-CN
chinese_source: worker-translation
---

# Radius at Geocentric Latitude

## 端口

### 输入

### **λs** — 地心纬度 标量 | 向量

地心纬度，指定为标量或向量，以 degrees 为单位。

**数据类型：** `double`
### 输出

### **rs** — 半径 标量 | 向量

地心纬度处的行星半径，以标量或向量形式返回，单位与扁率相同。

**数据类型：** `double`

## 参数

### **Units** — 输出单位 `Metric (MKS)` (默认) | `English`

输出单位，指定为：

| 单位 | 赤道半径 | Radius at Geocentric Latitude |
| --- | --- | --- |
| `Metric (MKS)` | Meters | Meters |
| `English` | Feet | Feet |

#### 依赖关系

要启用此参数，请将 **Planet model** 设置为
`Earth (WGS84)`。

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English'` |
| **默认值**：`'Metric (MKS)'` |

### **Planet model** — 行星模型 `Earth (WGS84)` (默认) | `Custom`

要使用的行星模型，`Custom` 或
`Earth (WGS84)`。

#### 编程使用

|  |
| --- |
| **模块参数**：`ptype` |
| **类型**：character vector |
| **值**：`'Earth (WGS84)'` | `'Custom'` |
| **默认值**：`'Earth (WGS84)'` |

### **Flattening** — 行星的扁率 `1/298.257223563` (默认) | 标量

行星的扁率，指定为 double 标量。

#### 依赖关系

要启用此参数，请将 **Planet model** 设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**：`F` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`1/298.257223563` |

### **Equatorial radius of planet** — 行星赤道处的半径 `6378137` (默认) | 标量

行星在其赤道处的半径，采用与 ECEF 位置所需单位相同的单位。

#### 依赖关系

要启用此参数，请将 **Planet model** 设置为 `Custom`。

#### 编程使用

|  |
| --- |
| **模块参数**：`R` |
| **类型**：character vector |
| **值**：double scalar |
| **默认值**：`6378137` |

## 所属库

Aerospace Blockset / Flight Parameters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

估计椭球行星在地心纬度处的半径

Radius at Geocentric Latitude 模块估计椭球行星在特定地心纬度 (λs) 处的半径 (rs)。

特定地心纬度处的椭球行星，显示椭球半径、扁率、地心纬度和赤道半径。

以下方程使用扁率 (f¯)、地心纬度 (λ¯s) 和赤道半径 (R¯) 估计椭球半径 (rs)：

rs=R21+[1/(1−f)2−1]sin2λs.
