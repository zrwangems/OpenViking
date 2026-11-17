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

高度，指定为指定单位下的标量。

**数据类型：** `double`

### **DCM** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，指定为表示平面地球坐标到机体固定轴坐标的 3×3 矩阵。

**数据类型：** `double`
### 输出

### **Vwind** — 平均风速 三元素向量

平均风速，返回为与 **DCM** 输入相同的机体坐标参考下的三元素向量，单位为指定单位。

**数据类型：** `double`

## 参数

### **Units** — 风切变单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

风切变单位，指定为：

| 单位 | 风 | 高度 |
| --- | --- | --- |
| `Metric (MKS)` | 米/秒 | 米 |
| `English (Velocity in ft/s)` | 英尺/秒 | 英尺 |
| `English (Velocity in kts)` | 节 | 英尺 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Flight phase** — 飞行阶段 `Category C - Terminal Flight Phase`（默认）| `Other`

飞行阶段，指定为：

- `Category C - Terminal Flight Phase`，按照军用规范 MIL-F-8785C 指定。
- `Other`

#### 编程使用

|  |
| --- |
| **模块参数**：`phase` |
| **类型**：字符向量 |
| **值**：`'Category C - Terminal Flight Phase'` | `'Other'` |
| **默认值**：`'Category C - Terminal Flight Phase'` |

### **Wind speed at 20 ft altitude (kts)** — 风速 `15`（默认）| 标量

在地面上方 6 米（20 英尺）高度处测得的风速，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`W_20` |
| **类型**：字符向量 |
| **值**：`scalar` |
| **默认值**：`'15'` |

### **Wind direction at 20 ft altitude (degrees clockwise from north)** — 风向 `0`（默认）| 标量

在地面上方 6 米（20 英尺）高度处的风向，指定为标量，以从地球 *x* 轴方向（北）顺时针方向的度数表示。风向定义为风吹来的方向。

#### 编程使用

|  |
| --- |
| **模块参数**：`Wdeg` |
| **类型**：字符向量 |
| **值**：`scalar` |
| **默认值**：`'0'` |

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
