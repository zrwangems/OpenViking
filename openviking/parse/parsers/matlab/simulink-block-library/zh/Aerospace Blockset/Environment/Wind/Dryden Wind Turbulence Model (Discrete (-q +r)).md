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
```yaml
ports:
- name: h
  summary: 高度 标量
  direction: input
  data_types: double
- name: V
  summary: 飞行器速度 标量
  direction: input
  data_types: double
- name: DCM
  summary: 方向余弦矩阵 3×3 矩阵
  direction: input
  data_types: double
- name: Vwind
  summary: 湍流速度 三元素向量
  direction: output
  data_types: double
- name: ωwind
  summary: 湍流角速率 三元素向量
  direction: output
  data_types: double
```

### 输入

### **h** — 高度 标量

高度，指定为标量，采用所选单位。

**数据类型：** `double`

### **V** — 飞行器速度 标量

飞行器速度，指定为标量，采用所选单位。

**数据类型：** `double`

### **DCM** — 方向余弦矩阵 3×3 矩阵

方向余弦矩阵，指定为 3×3 矩阵，表示平地坐标系到机体坐标系之间的转换。

**数据类型：** `double`
### 输出

### **Vwind** — 湍流速度 三元素向量

湍流速度，返回为三元素向量，采用与 **DCM** 输入相同的机体坐标参考，单位为所选单位。

**数据类型：** `double`

### **ωwind** — 湍流角速率 三元素向量

湍流角速率，指定为三元素向量，单位为弧度每秒。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 风速单位 Metric (MKS)（默认）| English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Specification
  summary: 军用参考标准 MIL-F-8785C（默认）| MIL-HDBK-1797 | MIL-HDBK-1797B
  group: ''
  block_parameter: spec
  type: 字符向量
  values: '''MIL-F-8785C'' | ''MIL-HDBK-1797'' | ''MIL-HDBK-1797B'''
  default: '''MIL-F-8785C'''
- name: Model type
  summary: 湍流模型 Discrete Dryden (+q +r)（默认）| Continuous Von Karman (+q +r) | Continuous Von Karman (-q +r) | Continuous Dryden
    (+q -r) | Continuous Dryden (+q +r) | Continuous Dryden (-q +r) | Discrete Dryden (+q -r) | Continuous Von Karman (+q
    -r) | Discrete Dryden (-q +r)
  group: ''
  block_parameter: model
  type: 字符向量
  values: '''Continuous Von Karman (+q +r)'' | ''Continuous Von Karman (-q +r)'' | ''Continuous Dryden (+q -r)'' | ''Continuous
    Dryden (+q +r)'' | ''Continuous Dryden (-q +r)'' | ''Discrete Dryden (+q -r)'' | ''Discrete Dryden (+q +r)'' | ''Discrete
    Dryden (-q +r)'''
  default: '''Discrete Dryden (+q +r)'''
- name: Wind speed at 6 m defines the low altitude intensity
  summary: 测量风速 15（默认）| 实标量
  group: ''
  block_parameter: W20
  type: 字符向量
  values: 实标量
  default: '''15'''
- name: Wind direction at 6 m (degrees clockwise from north)
  summary: 测量风向 0（默认）| 实标量
  group: ''
  block_parameter: Wdeg
  type: 字符向量
  values: 实标量
  default: '''0'''
- name: Probability of exceedance of high-altitude intensity
  summary: 湍流强度 10^-2 - Light（默认）| 10^-1 | 2x10^-1 | 10^-3 - Moderate | 10^-4 | 10^-5 - Severe | 10^-6
  group: ''
  block_parameter: TurbProb
  type: 字符向量
  values: '''2x10^-1'' | ''10^-1'' | ''10^-2 - Light'' | ''10^-3 - Moderate'' | ''10^-4'' | ''10^-5 - Severe'' | ''10^-6'''
  default: '''10^-2 - Light'''
- name: Scale length at medium/high altitudes (m)
  summary: 湍流尺度长度 533.4（默认）| 实标量
  group: ''
  block_parameter: L_high
  type: 字符向量
  values: 实标量
  default: '''533.4'''
- name: Wingspan
  summary: 翼展 10（默认）| 实标量
  group: ''
  block_parameter: Wingspan
  type: 字符向量
  values: 实标量
  default: '''10'''
- name: Band limited noise sample time (seconds)
  summary: 噪声采样时间 0.1（默认）| 实标量
  group: ''
  block_parameter: ts
  type: 字符向量
  values: 实标量
  default: '''0.1'''
- name: Random noise seeds
  summary: 噪声种子 [ug vg wg pg] [23341 23342 23343 23344]（默认）| 四元素向量
  group: ''
  block_parameter: Seed
  type: 字符向量
  values: 四元素向量
  default: '''[23341 23342 23343 23344]'''
- name: Turbulence on
  summary: 湍流信号 on（默认）| off
  group: ''
  block_parameter: T_on
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
```

### **Units** — 风速单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

由湍流引起的风速单位，指定为：

| 单位 | 风速 | 高度 | 空速 |
| --- | --- | --- | --- |
| `Metric (MKS)` | 米/秒 | 米 | 米/秒 |
| `English (Velocity in ft/s)` | 英尺/秒 | 英尺 | 英尺/秒 |
| `English (Velocity in kts)` | 节 | 英尺 | 节 |

#### 程序化使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Specification** — 军用参考标准 `MIL-F-8785C`（默认）| `MIL-HDBK-1797` | `MIL-HDBK-1797B`

军用参考标准，影响湍流尺度在横向和垂直方向上的应用，指定为 `MIL-F-8785C`、`MIL-HDBK-1797` 或 `MIL-HDBK-1797B`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`spec` |
| **类型**：字符向量 |
| **值**：`'MIL-F-8785C'` | `'MIL-HDBK-1797'` | `'MIL-HDBK-1797B'` |
| **默认值**：`'MIL-F-8785C'` |

### **Model type** — 湍流模型 `Discrete Dryden (+q +r)`（默认）| `Continuous Von Karman (+q +r)` | `Continuous Von Karman (-q +r)` | `Continuous Dryden (+q -r)` | `Continuous Dryden (+q +r)` | `Continuous Dryden (-q +r)` | `Discrete Dryden (+q -r)` | `Continuous Von Karman (+q -r)` | `Discrete Dryden (-q +r)`

选择要使用的风湍流模型：

|  |  |
| --- | --- |
| `Continuous Von Karman (+q -r)` | 使用 Von Kármán 速度谱的连续表示，具有正垂直和负横向角速率谱。 |
| `Continuous Von Karman (+q +r)` | 使用 Von Kármán 速度谱的连续表示，具有正垂直和横向角速率谱。 |
| `Continuous Von Karman (-q +r)` | 使用 Von Kármán 速度谱的连续表示，具有负垂直和正横向角速率谱。 |
| `Continuous Dryden (+q -r)` | 使用 Dryden 速度谱的连续表示，具有正垂直和负横向角速率谱。 |
| `Continuous Dryden (+q +r)` | 使用 Dryden 速度谱的连续表示，具有正垂直和横向角速率谱。 |
| `Continuous Dryden (-q +r)` | 使用 Dryden 速度谱的连续表示，具有负垂直和正横向角速率谱。 |
| `Discrete Dryden (+q -r)` | 使用 Dryden 速度谱的离散表示，具有正垂直和负横向角速率谱。 |
| `Discrete Dryden (+q +r)` | 使用 Dryden 速度谱的离散表示，具有正垂直和横向角速率谱。 |
| `Discrete Dryden (-q +r)` | 使用 Dryden 速度谱的离散表示，具有负垂直和正横向角速率谱。 |

Discrete Dryden 选项符合传递函数描述。

#### 程序化使用

|  |
| --- |
| **模块参数**：`model` |
| **类型**：字符向量 |
| **值**：`'Continuous Von Karman (+q +r)'` | `'Continuous Von Karman (-q +r)'` | `'Continuous Dryden (+q -r)'` | `'Continuous Dryden (+q +r)'` | `'Continuous Dryden (-q +r)'` | `'Discrete Dryden (+q -r)'` | `'Discrete Dryden (+q +r)'` | `'Discrete Dryden (-q +r)'` |
| **默认值**：`'Discrete Dryden (+q +r)'` |

### **Wind speed at 6 m defines the low altitude intensity** — 测量风速 `15`（默认）| 实标量

在 20 英尺（6 米）高度处测量的风速，指定为实标量，为低空湍流模型提供强度。

#### 程序化使用

|  |
| --- |
| **模块参数**：`W20` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'15'` |

### **Wind direction at 6 m (degrees clockwise from north)** — 测量风向 `0`（默认）| 实标量

在 20 英尺（6 米）高度处测量的风向，指定为实标量，该角度用于辅助将低空湍流模型转换到机体坐标系。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Wdeg` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'0'` |

### **Probability of exceedance of high-altitude intensity** — 湍流强度 `10^-2 - Light`（默认）| `10^-1` | `2x10^-1` | `10^-3 - Moderate` | `10^-4` | `10^-5 - Severe` | `10^-6`

湍流强度被超过的概率，指定为 `10^-2 - Light`、`10^-1`、`2x10^-1`、`10^-3 - Moderate`、`10^-4`、`10^-5 - Severe` 或 `10^-6`。在 2000 英尺以上，湍流强度由查找表确定，该表给出湍流强度作为高度和湍流强度被超过概率的函数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`TurbProb` |
| **类型**：字符向量 |
| **值**：`'2x10^-1'` | `'10^-1'` | `'10^-2 - Light'` | `'10^-3 - Moderate'` | `'10^-4'` | `'10^-5 - Severe'` | `'10^-6'` |
| **默认值**：`'10^-2 - Light'` |

### **Scale length at medium/high altitudes (m)** — 湍流尺度长度 `533.4`（默认）| 实标量

2000 英尺以上的湍流尺度长度，指定为实标量，假定为常数。根据军用参考标准，Dryden 谱的纵向湍流尺度长度推荐值为 1750 英尺。

**注意**

替代的尺度长度值会改变功率谱密度渐近线和阵风载荷。

#### 程序化使用

|  |
| --- |
| **模块参数**：`L_high` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'533.4'` |

### **Wingspan** — 翼展 `10`（默认）| 实标量

翼展，指定为实标量，在计算角速率上的湍流时需要用到。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Wingspan` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'10'` |

### **Band limited noise sample time (seconds)** — 噪声采样时间 `0.1`（默认）| 实标量

噪声采样时间，指定为实标量，即生成单位方差白噪声信号的采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数**：`ts` |
| **类型**：字符向量 |
| **值**：实标量 |
| **默认值**：`'0.1'` |

### **Random noise seeds** — 噪声种子 [ug vg wg pg] `[23341 23342 23343 23344]`（默认）| 四元素向量

随机噪声种子，指定为四元素向量，用于生成湍流信号，三个速度分量各一个，滚转角速率一个：

俯仰和偏航角速率上的湍流基于对垂直和横向速度整形滤波器输出的进一步整形。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Seed` |
| **类型**：字符向量 |
| **值**：四元素向量 |
| **默认值**：`'[23341 23342 23343 23344]'` |

### **Turbulence on** — 湍流信号 `on`（默认）| `off`

要生成湍流信号，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**：`T_on` |
| **类型**：字符向量 |
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

Dryden Wind Turbulence Model (Discrete) 模块使用 Dryden 谱表示，通过使用带限白噪声和适当的数字滤波器有限差分方程，将湍流添加到航空航天模型中。该模块实现了军用规范 MIL-F-8785C、军用手册 MIL-HDBK-1797 和军用手册 MIL-HDBK-1797B 中的数学表示。有关更多信息，请参阅算法。
