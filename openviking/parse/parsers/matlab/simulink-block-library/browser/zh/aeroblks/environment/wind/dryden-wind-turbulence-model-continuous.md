---
type: simulink-block
title: 'Dryden Wind Turbulence Model (Continuous)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'drydenwindturbulencemodelcontinuous'
documentation_source_path: 'drydenwindturbulencemodelcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# Dryden Wind Turbulence Model (Continuous)

## 端口

### 输入

### **h** — 高度标量

高度，指定为标量，采用所选单位。

**数据类型：** `double`

### **V** — 飞行器速度标量

飞行器速度，指定为标量，采用所选单位。

**数据类型：** `double`

### **DCM** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，指定为 3×3 矩阵，表示平面地球坐标到机体固定轴坐标。

**数据类型：** `double`
### 输出

### **Vwind** — 湍流速度 三元素向量

湍流速度，返回为三元素向量，采用与 **DCM** 输入相同的机体坐标参考，并以指定单位表示。

**数据类型：** `double`

### **ωwind** — 湍流角速率 三元素向量

湍流角速率，指定为三元素向量，单位为 radians per second。

**数据类型：** `double`

## 参数

### **单位** — 风速单位 `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

由湍流引起的风速单位，指定为：

| 单位 | 风速 | 高度 | 空速 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters/second | Meters | Meters/second |
| `English (Velocity in ft/s)` | Feet/second | Feet | Feet/second |
| `English (Velocity in kts)` | Knots | Feet | Knots |

#### 编程使用

|  |
| --- |
| **模块参数**: `units` |
| **类型**: character vector |
| **值**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**: `'Metric (MKS)'` |

### **规范** — 军用参考 `MIL-F-8785C` (default) | `MIL-HDBK-1797` | `MIL-HDBK-1797B`

军用参考，影响湍流尺度长度在横向和垂直方向上的应用，指定为 `MIL-F-8785C`、`MIL-HDBK-1797` 或 `MIL-HDBK-1797B`。

#### 编程使用

|  |
| --- |
| **模块参数**: `spec` |
| **类型**: character vector |
| **值**: `'MIL-F-8785C'` | `'MIL-HDBK-1797'` | `'MIL-HDBK-1797B'` |
| **默认值**: `'MIL-F-8785C'` |

### **模型类型** — 湍流模型 `Continuous Dryden (+q -r)` (default) | `Continuous Von Karman (+q +r)` | `Continuous Von Karman (-q +r)` | `Continuous Von Karman (+q -r)` | `Continuous Dryden (+q +r)` | `Continuous Dryden (-q +r)` | `Discrete Dryden (+q -r)` | `Discrete Dryden (+q +r)` | `Discrete Dryden (-q +r)`

风湍流模型，指定为：

|  |  |
| --- | --- |
| `Continuous Von Karman (+q -r)` | 使用 Von Kármán 速度谱的连续表示，具有正垂直和负横向角速率谱。 |
| `Continuous Von Karman (+q +r)` | 使用 Von Kármán 速度谱的连续表示，具有正垂直和正横向角速率谱。 |
| `Continuous Von Karman (-q +r)` | 使用 Von Kármán 速度谱的连续表示，具有负垂直和正横向角速率谱。 |
| `Continuous Dryden (+q -r)` | 使用 Dryden 速度谱的连续表示，具有正垂直和负横向角速率谱。 |
| `Continuous Dryden (+q +r)` | 使用 Dryden 速度谱的连续表示，具有正垂直和正横向角速率谱。 |
| `Continuous Dryden (-q +r)` | 使用 Dryden 速度谱的连续表示，具有负垂直和正横向角速率谱。 |
| `Discrete Dryden (+q -r)` | 使用 Dryden 速度谱的离散表示，具有正垂直和负横向角速率谱。 |
| `Discrete Dryden (+q +r)` | 使用 Dryden 速度谱的离散表示，具有正垂直和正横向角速率谱。 |
| `Discrete Dryden (-q +r)` | 使用 Dryden 速度谱的离散表示，具有负垂直和正横向角速率谱。 |

Continuous Dryden 选项符合传递函数描述。

#### 编程使用

|  |
| --- |
| **模块参数**: `model` |
| **类型**: character vector |
| **值**: `'Continuous Von Karman (+q +r)'` | `'Continuous Von Karman (-q +r)'` | `'Continuous Dryden (+q -r)'` | `'Continuous Dryden (+q +r)'` | `'Continuous Dryden (-q +r)'` | `'Discrete Dryden (+q -r)'` | `'Discrete Dryden (+q +r)'` | `'Discrete Dryden (-q +r)'` |
| **默认值**: `'Continuous Dryden (+q +r)'` |

### **6 m 处的风速定义低空强度** — 测得风速 `15` (default) | real scalar

在 20 feet（6 meters）高度处测得的风速，指定为 real scalar，为低空湍流模型提供强度。

#### 编程使用

|  |
| --- |
| **模块参数**: `W20` |
| **类型**: character vector |
| **值**: real scalar |
| **默认值**: `'15'` |

### **6 m 处的风向 (degrees clockwise from north)** — 测得风向 `0` (default) | real scalar

在 20 feet（6 meters）高度处测得的风向，指定为 real scalar，该角度用于帮助将低空湍流模型转换到机体坐标。

#### 编程使用

|  |
| --- |
| **模块参数**: `Wdeg` |
| **类型**: character vector |
| **值**: real scalar |
| **默认值**: `'0'` |

### **高空强度超越概率** — 湍流强度 `10^-2 - Light` (default) | `10^-1` | `2x10^-1` | `10^-3 - Moderate` | `10^-4` | `10^-5 - Severe` | `10^-6`

湍流强度被超越的概率，指定为 `10^-2 - Light`、`10^-1`、`2x10^-1`、`10^-3 - Moderate`、`10^-4`、`10^-5 - Severe` 或 `10^-6`。在 2000 feet 以上，湍流强度由查找表确定，该表给出湍流强度随高度和湍流强度被超越概率的函数关系。

#### 编程使用

|  |
| --- |
| **模块参数**: `TurbProb` |
| **类型**: character vector |
| **值**: `'2x10^-1'` | `'10^-1'` | `'10^-2 - Light'` | `'10^-3 - Moderate'` | `'10^-4'` | `'10^-5 - Severe'` | `'10^-6'` |
| **默认值**: `'10^-2 - Light'` |

### **中/高空尺度长度 (m)** — 湍流尺度长度 `533.4` (default) | real scalar

2000 feet 以上的湍流尺度长度，指定为 real scalar，并假定为常数。MIL-F-8785C 和 MIL-HDBK-1797/1797B 建议 Dryden 谱的纵向湍流尺度长度为 1750 feet。

**注意**

替代的尺度长度值会改变功率谱密度渐近线和阵风载荷。

#### 编程使用

|  |
| --- |
| **模块参数**: `L_high` |
| **类型**: character vector |
| **值**: real scalar |
| **默认值**: `'533.4'` |

### **翼展** — 翼展 `10` (default) | real scalar

翼展，指定为 real scalar，是计算角速率上的湍流所必需的。

#### 编程使用

|  |
| --- |
| **模块参数**: `Wingspan` |
| **类型**: character vector |
| **值**: real scalar |
| **默认值**: `'10'` |

### **带限噪声采样时间 (seconds)** — 噪声采样时间 `0.1` (default) | real scalar

噪声采样时间，指定为 real scalar，在该采样时间生成单位方差白噪声信号。

#### 编程使用

|  |
| --- |
| **模块参数**: `ts` |
| **类型**: character vector |
| **值**: real scalar |
| **默认值**: `'0.1'` |

### **随机噪声种子** — 噪声种子 [ug vg wg pg] `[23341 23342 23343 23344]` (default) | four-element vector

随机噪声种子，指定为 four-element vector，用于生成湍流信号，三个速度分量各一个，滚转角速率一个：

俯仰和偏航角速率上的湍流基于对垂直和横向速度成形滤波器输出的进一步成形。

#### 编程使用

|  |
| --- |
| **模块参数**: `Seed` |
| **类型**: character vector |
| **值**: four-element vector |
| **默认值**: `'[23341 23342 23343 23344]'` |

### **湍流开启** — 湍流信号 `on` (default) | `off`

要生成湍流信号，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**: `T_on` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认值**: `'on'` |

## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 Dryden 速度谱生成连续风湍流

Dryden Wind Turbulence Model (Continuous) 模块使用 Dryden 谱表示，通过将带限白噪声传递通过适当的成形滤波器，将湍流添加到航空航天模型。该模块实现军用规范 MIL-F-8785C、军用手册 MIL-HDBK-1797、军用手册 MIL-HDBK-1797B 中的数学表示。
