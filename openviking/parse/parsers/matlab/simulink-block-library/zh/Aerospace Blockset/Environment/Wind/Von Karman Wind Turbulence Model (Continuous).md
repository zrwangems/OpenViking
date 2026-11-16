---
type: simulink-block
title: 'Von Karman Wind Turbulence Model (Continuous)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'vonkarmanwindturbulencemodelcontinuous'
documentation_source_path: 'vonkarmanwindturbulencemodelcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# Von Karman Wind Turbulence Model (Continuous)

## 端口

### 输入

### **h** — 高度标量

高度，指定为标量，采用所选单位。

**数据类型：** `double`

### **V** — 飞行器速度标量

飞行器速度，指定为标量，采用所选单位。

**数据类型：** `double`

### **DCM** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，指定为表示平面地球坐标到机体固定轴坐标的 3×3 矩阵。

**数据类型：** `double`
### 输出

### **Vwind** — 湍流速度 三元素向量

湍流速度，返回为三元素向量，与 **DCM** 输入处于同一机体坐标参考系中，采用指定单位。

**数据类型：** `double`

### **ωwind** — 湍流角速率 三元素向量

湍流角速率，指定为三元素向量，单位为 radians per second。

**数据类型：** `double`

## 参数

### **Units** — 风速单位 `Metric (MKS)`（默认） | `English (Velocity in ft/s)` | `English (Velocity in kts)`

由湍流引起的风速单位，指定为：

| 单位 | 风速 | 高度 | 空速 |
| --- | --- | --- | --- |
| `Metric (MKS)` | Meters/second | Meters | Meters/second |
| `English (Velocity in ft/s)` | Feet/second | Feet | Feet/second |
| `English (Velocity in kts)` | Knots | Feet | Knots |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认**：`'Metric (MKS)'` |

### **Specification** — 军用参考 `MIL-F-8785C`（默认） | `MIL-HDBK-1797` | `MIL-HDBK-1797B`

军用参考，影响湍流尺度长度在横向和垂直方向上的应用，指定为 `MIL-F-8785C`、`MIL-HDBK-1797` 或 `MIL-HDBK-1797B`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`spec` |
| **类型**：character vector |
| **值**：`'MIL-F-8785C'` | `'MIL-HDBK-1797'` | `'MIL-HDBK-1797B'` |
| **默认**：`'MIL-F-8785C'` |

### **Model type** — 湍流模型 `Continuous Von Karman (+q -r)`（默认） | `Continuous Von Karman (+q +r)` | `Continuous Von Karman (-q +r)` | `Continuous Dryden (+q -r)` | `Continuous Dryden (+q +r)` | `Continuous Dryden (-q +r)` | `Discrete Dryden (+q -r)` | `Discrete Dryden (+q +r)` | `Discrete Dryden (-q +r)`

风湍流模型，指定为：

|  |  |
| --- | --- |
| `Continuous Von Karman (+q -r)` | 使用 Von Kármán 速度谱的连续表示，具有正垂直角速率谱和负横向角速率谱。 |
| `Continuous Von Karman (+q +r)` | 使用 Von Kármán 速度谱的连续表示，具有正垂直角速率谱和正横向角速率谱。 |
| `Continuous Von Karman (-q +r)` | 使用 Von Kármán 速度谱的连续表示，具有负垂直角速率谱和正横向角速率谱。 |
| `Continuous Dryden (+q -r)` | 使用 Dryden 速度谱的连续表示，具有正垂直角速率谱和负横向角速率谱。 |
| `Continuous Dryden (+q +r)` | 使用 Dryden 速度谱的连续表示，具有正垂直角速率谱和正横向角速率谱。 |
| `Continuous Dryden (-q +r)` | 使用 Dryden 速度谱的连续表示，具有负垂直角速率谱和正横向角速率谱。 |
| `Discrete Dryden (+q -r)` | 使用 Dryden 速度谱的离散表示，具有正垂直角速率谱和负横向角速率谱。 |
| `Discrete Dryden (+q +r)` | 使用 Dryden 速度谱的离散表示，具有正垂直角速率谱和正横向角速率谱。 |
| `Discrete Dryden (-q +r)` | 使用 Dryden 速度谱的离散表示，具有负垂直角速率谱和正横向角速率谱。 |

Continuous Von Kármán 选项符合传递函数描述。

#### 程序化使用

|  |
| --- |
| **模块参数**：`model` |
| **类型**：character vector |
| **值**：`'Continuous Von Karman (+q +r)'` | `'Continuous Von Karman (-q +r)'` | `'Continuous Dryden (+q -r)'` | `'Continuous Dryden (+q +r)'` | `'Continuous Dryden (-q +r)'` | `'Discrete Dryden (+q -r)'` | `'Discrete Dryden (+q +r)'` | `'Discrete Dryden (-q +r)'` |
| **默认**：`'Continuous Von Karman (+q +r)'` |

### **Wind speed at 6 m defines the low altitude intensity** — 测得风速 `15`（默认） | real scalar

在高度 20 feet (6 meters) 处测得的风速，指定为 real scalar，它为低空湍流模型提供强度。

#### 程序化使用

|  |
| --- |
| **模块参数**：`W20` |
| **类型**：character vector |
| **值**：real scalar |
| **默认**：`'15'` |

### **Wind direction at 6 m (degrees clockwise from north)** — 测得风向 `0`（默认） | real scalar

在高度 20 feet (6 meters) 处测得的风向，指定为 real scalar，该角度用于帮助将低空湍流模型转换到机体坐标。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Wdeg` |
| **类型**：character vector |
| **值**：real scalar |
| **默认**：`'0'` |

### **Probability of exceedance of high-altitude intensity** — 湍流强度 `10^-2 - Light`（默认） | `10^-1` | `2x10^-1` | `10^-3 - Moderate` | `10^-4` | `10^-5 - Severe` | `10^-6`

湍流强度被超过的概率，指定为 `10^-2 - Light`、`10^-1`、`2x10^-1`、`10^-3 - Moderate`、`10^-4`、`10^-5 - Severe` 或 `10^-6`。在 2000 feet 以上，湍流强度由查找表确定，该表给出湍流强度作为高度和湍流强度被超过概率的函数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`TurbProb` |
| **类型**：character vector |
| **值**：`'2x10^-1'` | `'10^-1'` | `'10^-2 - Light'` | `'10^-3 - Moderate'` | `'10^-4'` | `'10^-5 - Severe'` | `'10^-6'` |
| **默认**：`'10^-2 - Light'` |

### **Scale length at medium/high altitudes** — 湍流尺度长度 `762`（默认） | real scalar

在 2000 feet 以上的湍流尺度长度，指定为 real scalar。假定该长度为常数。

根据军用规范，对于 Dryden 谱的纵向湍流尺度长度，推荐使用 1750 feet。

**注意**

备用尺度长度值会改变功率谱密度渐近线和阵风载荷。

#### 程序化使用

|  |
| --- |
| **模块参数**：`L_high` |
| **类型**：character vector |
| **值**：real scalar |
| **默认**：`'762'` |

### **Wingspan** — 翼展 `10`（默认） | real scalar

翼展，指定为 real scalar，在计算角速率上的湍流时需要。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Wingspan` |
| **类型**：character vector |
| **值**：real scalar |
| **默认**：`'10'` |

### **Band limited noise sample time (seconds)** — 噪声采样时间 `0.1`（默认） | real scalar

噪声采样时间，指定为 real scalar，在该时间生成单位方差白噪声信号。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ts` |
| **类型**：character vector |
| **值**：real scalar |
| **默认**：`'0.1'` |

### **Random noise seeds** — 噪声种子 [ug vg wg pg] `[23341 23342 23343 23344]`（默认） | four-element vector

随机噪声种子，指定为 four-element vector，用于生成湍流信号，三个速度分量各一个，以及滚转角速率一个：

俯仰和偏航角速率上的湍流基于对垂直和横向速度成形滤波器输出的进一步成形。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Seed` |
| **类型**：character vector |
| **值**：four-element vector |
| **默认**：`'[23341 23342 23343 23344]'` |

### **Turbulence on** — 湍流信号 `on`（默认） | `off`

要生成湍流信号，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**：`T_on` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认**：`'on'` |

## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006b 中引入**

## 描述

生成具有 Von Kármán 速度谱的连续风湍流

Von Kármán Wind Turbulence Model (Continuous) 模块使用 Von Kármán 谱表示，通过将带限白噪声通过适当的成形滤波器来向航空航天模型添加湍流。此模块实现 Military Specification MIL-F-8785C、Military Handbook MIL-HDBK-1797 和 Military Handbook MIL-HDBK-1797B 中的数学表示。有关详细信息，请参阅 Algorithms。
