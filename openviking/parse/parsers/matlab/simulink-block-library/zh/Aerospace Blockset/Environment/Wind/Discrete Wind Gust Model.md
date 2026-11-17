---
type: simulink-block
title: 'Discrete Wind Gust Model'
family: 'environment'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'discretewindgustmodel'
documentation_source_path: 'discretewindgustmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Wind Gust Model

## 端口

### 输入

### **V** — 空速标量

空速，指定为标量，采用所选单位。

**数据类型：** `double`
### 输出

### **Vwind** — 风速标量

风速，返回为标量，采用所选单位。

**数据类型：** `double`

## 参数

### **单位** — 单位 `Metric (MKS)` (默认) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

阵风单位，指定为：

| 单位 | 风速 | 高度 |
| --- | --- | --- |
| `Metric (MKS)` | Meters/second | Meters |
| `English (Velocity in ft/s)` | Feet/second | Feet |
| `English (Velocity in kts)` | Knots | Feet |

#### 编程使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**: `'Metric (MKS)'` |

### **u 轴上的阵风** — 施加到 *u* 轴的阵风 `on` (默认) | `off`

要将阵风施加到机体坐标系中的 *u* 轴，请选中此复选框。否则，请清除此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `Gx` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **v 轴上的阵风** — 施加到 *v* 轴的阵风 `on` (默认) | `off`

要将阵风施加到机体坐标系中的 *v* 轴，请选中此复选框。否则，请清除此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `Gy` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **w 轴上的阵风** — 施加到 *w* 轴的阵风 `on` (默认) | `off`

要将阵风施加到机体坐标系中的 *w* 轴，请选中此复选框。否则，请清除此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `Gz` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

### **阵风开始时间 (sec)** — 阵风开始时间 `5` (默认) | scalar

模型时间，指定为 scalar，阵风开始的时间，以 seconds 为单位。

#### 编程使用

|  |
| --- |
| **模块参数**: `t_0` |
| **类型**: character vector |
| **值**: scalar |
| **默认值**: `'5'` |

### **阵风长度 [dx dy dz] (m)** — 阵风长度 `[120 120 80]` (默认)

长度，以 meters 或 feet 为单位（取决于单位选择），阵风在每个轴上增强所经过的长度。这些值必须为正。

#### 编程使用

|  |
| --- |
| **模块参数**: `d_m` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'[120 120 80]'` |

### **阵风幅度 [ug vg wg] (m/s)** — 阵风幅度 `[3.5 3.5 3.0]` (默认)

由阵风在每个轴上引起的风速增量的幅值。这些值可以为正或负。

#### 编程使用

|  |
| --- |
| **模块参数**: `d_m` |
| **类型**: character vector |
| **值**: vector |
| **默认值**: `'[3.5 3.5 3.0]'` |

## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

生成离散阵风

Discrete Wind Gust Model 模块实现标准 “1-cosine” 形状的阵风。该模块实现军用规范 MIL-F-8785C [1] 中的数学表示。阵风可分别施加到每个轴，或同时施加到所有三个轴。您指定阵风幅度（由阵风产生的风速增量）、阵风长度（阵风增强所经过的长度，以 meters 为单位）和阵风开始时间。有关阵风形状的更多信息，请参阅算法。

Discrete Wind Gust Model 模块可以以 feet per second、meters per second 或 knots 为单位表示风速。
