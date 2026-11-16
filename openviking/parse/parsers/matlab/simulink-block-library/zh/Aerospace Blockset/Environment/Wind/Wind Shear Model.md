---
type: simulink-block
title: 'Wind Shear Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'windshearmodel'
documentation_source_path: 'windshearmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Wind Shear Model

## 端口

### 输入

### **h** — 高度标量

高度，指定为以指定单位表示的标量。

**数据类型：** `double`

### **DCM** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，指定为表示平面地球坐标到机体固定轴坐标的 3×3 矩阵。

**数据类型：** `double`

### 输出

### **Vwind** — 平均风速三元素向量

平均风速，返回为与 **DCM** 输入相同的机体坐标参考下的三元素向量，并以指定单位表示。

**数据类型：** `double`

## 参数

### **Units** — 风切变单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

风切变单位，指定为：

| 单位 | 风速 | 高度 |
| --- | --- | --- |
| `Metric (MKS)` | Meters/second | Meters |
| `English (Velocity in ft/s)` | Feet/second | Feet |
| `English (Velocity in kts)` | Knots | Feet |

#### 编程用法

|  |
| --- |
| **模块参数**: `units` |
| **类型**: 字符向量 |
| **取值**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**: `'Metric (MKS)'` |

### **飞行阶段** — 飞行阶段 `Category C - Terminal Flight Phase`（默认）| `Other`

飞行阶段，指定为：

- `Category C - Terminal Flight Phase`，由军用规范 MIL-F-8785C 指定。
- `Other`

#### 编程用法

|  |
| --- |
| **模块参数**: `phase` |
| **类型**: 字符向量 |
| **取值**: `'Category C - Terminal Flight Phase'` | `'Other'` |
| **默认值**: `'Category C - Terminal Flight Phase'` |

### **20 ft 高度处的风速 (kts)** — 风速 `15`（默认）| 标量

在地面上方 6 m（20 ft）高度处测得的风速，指定为标量。

#### 编程用法

|  |
| --- |
| **模块参数**: `W_20` |
| **类型**: 字符向量 |
| **取值**: `scalar` |
| **默认值**: `'15'` |

### **20 ft 高度处的风向 (degrees clockwise from north)** — 风向 `0`（默认）| 标量

在地面上方 6 m（20 ft）高度处的风向，指定为标量，以从地球 *x* 轴方向（北）顺时针方向的度数表示。风向定义为风吹来的方向。

#### 编程用法

|  |
| --- |
| **模块参数**: `Wdeg` |
| **类型**: 字符向量 |
| **取值**: `scalar` |
| **默认值**: `'0'` |

## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算风切变条件

Wind Shear Model 模块将风切变添加到航空航天模型中。此实现基于军用规范 MIL-F-8785C [1] 中的数学表示。
