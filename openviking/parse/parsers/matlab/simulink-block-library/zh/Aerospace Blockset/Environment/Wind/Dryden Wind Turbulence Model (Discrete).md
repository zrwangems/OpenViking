---
type: simulink-block
title: 'Dryden Wind Turbulence Model (Discrete)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'drydenwindturbulencemodeldiscrete'
documentation_source_path: 'drydenwindturbulencemodeldiscrete.html'
language: zh-CN
chinese_source: worker-translation
---

# Dryden Wind Turbulence Model (Discrete)

## 端口

### 输入

### **h** — 高度标量

高度，指定为标量，使用选定的单位。

**数据类型：** `double`

### **V** — 飞机速度标量

飞机速度，指定为标量，使用选定的单位。

**数据类型：** `double`

### **DCM** — 方向余弦矩阵 3-by-3 矩阵

方向余弦矩阵，指定为 3-by-3 矩阵，表示从平面地球坐标到机体固连轴坐标的转换。

**数据类型：** `double`
### 输出

### **Vwind** — 湍流速度三元素向量

湍流速度，返回为三元素向量，位于与 **DCM** 输入相同的机体坐标参考中，使用指定的单位。

**数据类型：** `double`

### **ωwind** — 湍流角速率三元素向量

湍流角速率，指定为三元素向量，单位为 radians per second。

**数据类型：** `double`

## 参数

### **Units** — 风速单位 `Metric (MKS)`（默认值）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

湍流引起的风速单位，指定为：

| 单位 | 风速 | 高度 | 空速 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters/second | Meters | Meters/second |
| `English (Velocity in ft/s)` | Feet/second | Feet | Feet/second |
| `English (Velocity in kts)` | Knots | Feet | Knots |

#### 编程用法

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Specification** — 军事参考 `MIL-F-8785C`（默认值）| `MIL-HDBK-1797` | `MIL-HDBK-1797B`

军事参考，影响湍流尺度长度在横向和垂直方向上的应用，指定为 `MIL-F-8785C`、`MIL-HDBK-1797` 或 `MIL-HDBK-1797B`。

#### 编程用法

|  |
| --- |
| **模块参数**：`spec` |
| **类型**：character vector |
| **值**：`'MIL-F-8785C'` | `'MIL-HDBK-1797'` | `'MIL-HDBK-1797B'` |
| **默认值**：`'MIL-F-8785C'` |

### **Model type** — 湍流模型 `Discrete Dryden (+q +r)`（默认值）| `Continuous Von Karman (+q +r)` | `Continuous Von Karman (-q +r)` | `Continuous Dryden (+q -r)` | `Continuous Dryden (+q +r)` | `Continuous Dryden (-q +r)` | `Discrete Dryden (+q -r)` | `Continuous Von Karman (+q -r)` | `Discrete Dryden (-q +r)`

选择要使用的风湍流模型：

|  |  |
| --- | --- |
| `Continuous Von Karman (+q -r)` | 使用 Von Kármán 速度谱的连续表示，具有正的垂直角速率谱和负的横向角速率谱。 |
| `Continuous Von Karman (+q +r)` | 使用 Von Kármán 速度谱的连续表示，具有正的垂直角速率谱和正的横向角速率谱。 |
| `Continuous Von Karman (-q +r)` | 使用 Von Kármán 速度谱的连续表示，具有负的垂直角速率谱和正的横向角速率谱。 |
| `Continuous Dryden (+q -r)` | 使用 Dryden 速度谱的连续表示，具有正的垂直角速率谱和负的横向角速率谱。 |
| `Continuous Dryden (+q +r)` | 使用 Dryden 速度谱的连续表示，具有正的垂直角速率谱和正的横向角速率谱。 |
| `Continuous Dryden (-q +r)` | 使用 Dryden 速度谱的连续表示，具有负的垂直角速率谱和正的横向角速率谱。 |
| `Discrete Dryden (+q -r)` | 使用 Dryden 速度谱的离散表示，具有正的垂直角速率谱和负的横向角速率谱。 |
| `Discrete Dryden (+q +r)` | 使用 Dryden 速度谱的离散表示，具有正的垂直角速率谱和正的横向角速率谱。 |
| `Discrete Dryden (-q +r)` | 使用 Dryden 速度谱的离散表示，具有负的垂直角速率谱和正的横向角速率谱。 |

Discrete Dryden 选项符合传递函数描述。

#### 编程用法

|  |
| --- |
| **模块参数**：`model` |
| **类型**：character vector |
| **值**：`'Continuous Von Karman (+q +r)'` | `'Continuous Von Karman (-q +r)'` | `'Continuous Dryden (+q -r)'` | `'Continuous Dryden (+q +r)'` | `'Continuous Dryden (-q +r)'` | `'Discrete Dryden (+q -r)'` | `'Discrete Dryden (+q +r)'` | `'Discrete Dryden (-q +r)'` |
| **默认值**：`'Discrete Dryden (+q +r)'` |

### **Wind speed at 6 m defines the low altitude intensity** — 测量的风速 `15`（默认值）| real scalar

在 20 feet（6 meters）高度处测量的风速，指定为 real scalar，为低空湍流模型提供强度。

#### 编程用法

|  |
| --- |
| **模块参数**：`W20` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'15'` |

### **Wind direction at 6 m (degrees clockwise from north)** — 测量的风向 `0`（默认值）| real scalar

在 20 feet（6 meters）高度处测量的风向，指定为 real scalar，这是一个角度，用于帮助将低空湍流模型转换到机体坐标。

#### 编程用法

|  |
| --- |
| **模块参数**：`Wdeg` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'0'` |

### **Probability of exceedance of high-altitude intensity** — 湍流强度 `10^-2 - Light`（默认值）| `10^-1` | `2x10^-1` | `10^-3 - Moderate` | `10^-4` | `10^-5 - Severe` | `10^-6`

湍流强度被超过的概率，指定为 `10^-2 - Light`、`10^-1`、`2x10^-1`、`10^-3 - Moderate`、`10^-4`、`10^-5 - Severe` 或 `10^-6`。高于 2000 feet 时，湍流强度由查找表确定，该表给出湍流强度作为高度和湍流强度被超过概率的函数。

#### 编程用法

|  |
| --- |
| **模块参数**：`TurbProb` |
| **类型**：character vector |
| **值**：`'2x10^-1'` | `'10^-1'` | `'10^-2 - Light'` | `'10^-3 - Moderate'` | `'10^-4'` | `'10^-5 - Severe'` | `'10^-6'` |
| **默认值**：`'10^-2 - Light'` |

### **Scale length at medium/high altitudes (m)** — 湍流尺度长度 `533.4`（默认值）| real scalar

高于 2000 feet 的湍流尺度长度，指定为 real scalar，假定为常数。根据军事参考，对于 Dryden 谱的纵向湍流尺度长度，推荐数值为 1750 feet。

**注意**

替代尺度长度值会改变功率谱密度渐近线和阵风载荷。

#### 编程用法

|  |
| --- |
| **模块参数**：`L_high` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'533.4'` |

### **Wingspan** — 翼展 `10`（默认值）| real scalar

翼展，指定为 real scalar，是计算角速率上的湍流时所需的。

#### 编程用法

|  |
| --- |
| **模块参数**：`Wingspan` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'10'` |

### **Band limited noise sample time (seconds)** — 噪声采样时间 `0.1`（默认值）| real scalar

噪声采样时间，指定为 real scalar，在该时间生成单位方差白噪声信号。

#### 编程用法

|  |
| --- |
| **模块参数**：`ts` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`'0.1'` |

### **Random noise seeds** — 噪声种子 [ug vg wg pg] `[23341 23342 23343 23344]`（默认值）| four-element vector

随机噪声种子，指定为 four-element vector，用于生成湍流信号，三个速度分量各一个，滚转角速率一个：

俯仰和偏航角速率上的湍流基于对垂直和横向速度的整形滤波器输出的进一步整形。

#### 编程用法

|  |
| --- |
| **模块参数**：`Seed` |
| **类型**：character vector |
| **值**：four-element vector |
| **默认值**：`'[23341 23342 23343 23344]'` |

### **Turbulence on** — 湍流信号 `on`（默认值）| `off`

要生成湍流信号，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**：`T_on` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 Dryden 速度谱生成离散风湍流

Dryden Wind Turbulence Model (Discrete) 模块使用 Dryden 谱表示，通过使用限带白噪声和适当的数字滤波器有限差分方程，将湍流添加到航空航天模型中。该模块实现 Military Specification MIL-F-8785C、Military Handbook MIL-HDBK-1797 和 Military Handbook MIL-HDBK-1797B 中的数学表示。有关详细信息，请参阅算法。
