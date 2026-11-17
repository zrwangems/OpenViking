---
type: simulink-block
title: 'Operational Amplifier'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'operationalamplifier'
documentation_source_path: 'ref/operationalamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# Operational Amplifier

## 端口
```yaml
ports:
- name: InP
  summary: 正输入端 标量
  direction: input
  data_types: single | double
- name: InN
  summary: 负输入端 标量
  direction: input
  data_types: single | double
- name: OutP
  summary: 正输出端 标量
  direction: output
  data_types: single | double
- name: OutN
  summary: 负输出端 标量
  direction: output
  data_types: single | double
```

### 输入

### **InP** — 正输入端 标量

运算放大器的正输入端。

**数据类型：** `single` | `double`

### **InN** — 负输入端 标量

运算放大器的负输入端。

**数据类型：** `single` | `double`
### 输出

### **OutP** — 正输出端 标量

运算放大器的正输出端。

**数据类型：** `single` | `double`

### **OutN** — 负输出端 标量

运算放大器的负输出端。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Operational Amplifier Circuit
  summary: 运算放大器电路类型 Double-pole Circuit（默认）| Multipole Circuit
  group: ''
  block_parameter: OpampType
  type: character vector
  values: Double-pole Circuit| Multipole Circuit
  default: Double-pole Circuit
- name: Inherit sample interval from input
  summary: 从输入继承采样间隔 off（默认）| on
  group: ''
- name: Sample interval (s)
  summary: MATLAB 分析中使用的采样间隔值 1e-8（默认）| 标量
  group: ''
  block_parameter: SampleInterval
  type: character vector
  values: scalar
  default: 1e-8
- name: Simulate using
  summary: 选择仿真模式 Code generation（默认）| Interpreted execution
  group: ''
  block_parameter: SimulateUsing
  type: character vector
  values: Code generation| Interpreted execution
  default: Code generation
- name: Supply rail high (V)
  summary: 最大电源电压 5（默认）| 实数标量
  group: 信号参数
  block_parameter: VoltageSupplyPlus
  type: character vector
  values: real scalar
  default: '5'
- name: Supply rail low (V)
  summary: 最小电源电压 -5（默认）| 实数标量
  group: 信号参数
  block_parameter: VoltageSupplyMinus
  type: character vector
  values: real scalar
  default: '-5'
- name: Input offset voltage (V)
  summary: 输入端的偏移电压 0（默认）| 标量
  group: 信号参数
  block_parameter: InputOffsetVoltage
  type: character vector
  values: scalar
  default: '0'
- name: 开环增益 (V/V)
  summary: 无反馈时的运算放大器增益 3e3（默认）| 正实数标量
  group: 高级参数
  block_parameter: Gain
  type: 字符向量
  values: 正实数标量
  default: 3e3
- name: 单位增益带宽 (Hz)
  summary: 运算放大器增益等于 1 时的频率 10e6（默认）| 正实数标量
  group: 高级参数
  block_parameter: FrequencyUnityGain
  type: 字符向量
  values: 正实数标量
  default: 10e6
- name: 最大尾电流 (A)
  summary: 运算放大器电路中流过尾 MOSFET 的最大电流 100e-6（默认）| 正实数标量
  group: 高级参数
  block_parameter: InputCurrentMax
  type: 字符向量
  values: 正实数标量
  default: 100e-6
- name: 压摆率 (V/s)
  summary: 运算放大器输出电压的变化率 10e6（默认）| 正实数标量
  group: 高级参数
  block_parameter: SlewRate
  type: 字符向量
  values: 正实数标量
  default: 10e6
- name: 输出电阻 (Ohms)
  summary: 输出端子处的电阻 10e3（默认）| 正实数标量
  group: 高级参数
  block_parameter: OutputResistance
  type: 字符向量
  values: 正实数标量
  default: 10e3
- name: 输出电容 (F)
  summary: 输出端子处的电容 50e-12（默认）| 正实数标量
  group: 高级参数
  block_parameter: OutputCapacitance
  type: 字符向量
  values: 正实数标量
  default: 50e-12
- name: 传递函数极点
  summary: 拉普拉斯域中传递函数的极点 [-2.09e+04 -8.62e+07]（默认）| 列向量
  group: 高级参数
  block_parameter: Poles
  type: 字符向量
  values: 列向量
  default: '[-2.09e+04 -8.62e+07]'
- name: Transfer function zeroes
  summary: 拉普拉斯域中传递函数的零点 [-9.14e+07]（默认）| 列向量
  group: 高级参数
  block_parameter: Zeros
  type: character vector
  values: column vector
  default: '[-9.14e+07]'
- name: Include Z-domain approximation
  summary: 在绘制开环响应时包含 *z* 域近似 off（默认）| on
  group: Analysis
- name: Plot open loop response
  summary: 绘制运放开环响应 button
  group: Analysis
```

### **Operational Amplifier Circuit** — 运算放大器电路类型 `Double-pole Circuit`（默认）| `Multipole Circuit`

运算放大器电路的类型。

- `Double-pole Circuit` — 使用开环增益、单位增益带宽、最大尾电流和压摆率等电路参数来定义简单的双极点电路。
- `Multipole Circuit` — 使用传递函数极点和零点来定义多极点电路。

#### 编程使用

|  |
| --- |
| **模块参数：** `OpampType` |
| **类型**：character vector |
| **值**：`Double-pole Circuit`| `Multipole Circuit` |
| **默认值**：`Double-pole Circuit` |

### **Inherit sample interval from input** — 从输入继承采样间隔 off（默认）| on

从输入继承采样间隔值。默认情况下，此选项未选中。

### **Sample interval (s)** — MATLAB 分析中使用的采样间隔值 `1e-8`（默认）| 标量

模块在 MATLAB® 分析中使用的采样间隔值，指定为以秒为单位的标量。

#### 依赖关系

要启用此参数，请取消选择 **Inherit sample interval from input** 选项。

#### 编程使用

|  |
| --- |
| **模块参数：** `SampleInterval` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`1e-8` |

### **Simulate using** — 选择仿真模式 `Code generation`（默认）| `Interpreted execution`

选择仿真模式。您选择的此选项会影响仿真性能。

使用 `Code generation` 方法仿真模型需要额外的启动时间，但后续仿真运行更快。使用 `Interpreted execution` 方法仿真模型可能会减少启动时间，但后续仿真运行较慢。有关详细信息，请参阅 Interpreted Execution vs. Code Generation。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型**：character vector |
| **值**：`Code generation`| `Interpreted execution` |
| **默认值**：`Code generation` |

### 信号参数

### **Supply rail high (V)** — 最大电源电压 `5`（默认）| 实数标量

提供给 Operational Amplifier 模块的最大电源电压，指定为以伏特为单位的实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `VoltageSupplyPlus` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`5` |

### **Supply rail low (V)** — 最小电源电压 `-5`（默认）| 实数标量

提供给 Operational Amplifier 模块的最小电源电压，指定为以伏特为单位的实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `VoltageSupplyMinus` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`-5` |

### **Input offset voltage (V)** — 输入端的偏移电压 `0`（默认）| 标量

运算放大器输入端的偏移电压，指定为以伏特为单位的标量。模块使用此值在运算放大器的输出端获得零电压。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputOffsetVoltage` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`0` |

### 高级参数

### **开环增益 (V/V)** — 无反馈时的运算放大器增益 `3e3`（默认）| 正实数标量

运算放大器在没有任何正反馈或负反馈时的增益，指定为无单位的正实数标量。

#### 依赖关系

要启用此参数，请将 **Operational Amplifier Circuit** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Gain` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `3e3` |

### **单位增益带宽 (Hz)** — 运算放大器增益等于 1 时的频率 `10e6`（默认）| 正实数标量

运算放大器的开环增益变为 1 时的频率，指定为以赫兹为单位的正实数标量。

#### 依赖关系

要启用此参数，请将 **Operational Amplifier Circuit** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencyUnityGain` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `10e6` |

### **最大尾电流 (A)** — 运算放大器电路中流过尾 MOSFET 的最大电流 `100e-6`（默认）| 正实数标量

运算放大器电路中流过尾 MOSFET（金属氧化物半导体场效应晶体管）的电流最大值，指定为以安培为单位的正实数标量。

#### 依赖关系

要启用此参数，请将 **Operational Amplifier Circuit** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputCurrentMax` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `100e-6` |

### **压摆率 (V/s)** — 运算放大器输出电压的变化率 `10e6`（默认）| 正实数标量

运算放大器输出电压相对于时间的变化率，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Operational Amplifier Circuit** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SlewRate` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `10e6` |

### **输出电阻 (Ohms)** — 输出端子处的电阻 `10e3`（默认）| 正实数标量

运算放大器输出端子处的电阻，指定为以欧姆为单位的正实数标量。

#### 依赖关系

要启用此参数，请将 **Operational Amplifier Circuit** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputResistance` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `10e3` |

### **输出电容 (F)** — 输出端子处的电容 `50e-12`（默认）| 正实数标量

运算放大器输出端子处的电容，指定为以法拉为单位的正实数标量。

#### 依赖关系

要启用此参数，请将 **Operational Amplifier Circuit** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputCapacitance` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `50e-12` |

### **传递函数极点** — 拉普拉斯域中传递函数的极点 `[-2.09e+04 -8.62e+07]`（默认）| 列向量

运算放大器在拉普拉斯域中传递函数的极点，指定为以 rad/s 为单位的列向量。

如果将 **Operational Amplifier Circuit** 设置为 `Double-pole Circuit`，模块会根据电路参数自动计算极点。如果将 **Operational Amplifier Circuit** 设置为 `Multipole Circuit`，则可以指定极点。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Poles` |
| **类型：** 字符向量 |
| **值：** 列向量 |
| **默认值：** `[-2.09e+04 -8.62e+07]` |

### **Transfer function zeroes** — 拉普拉斯域中传递函数的零点 `[-9.14e+07]`（默认）| 列向量

运算放大器在拉普拉斯域中传递函数的零点，指定为以 rad/s 为单位的列向量。

如果将 **Operational Amplifier Circuit** 设置为 `Double-pole Circuit`，该模块会根据电路参数自动计算零点。如果将 **Operational Amplifier Circuit** 设置为 `Multipole Circuit`，则可以指定零点。

#### 编程使用

|  |
| --- |
| **模块参数：** `Zeros` |
| **类型**：character vector |
| **值**：column vector |
| **默认值**：`[-9.14e+07]` |

### Analysis

### **Include Z-domain approximation** — 在绘制开环响应时包含 *z* 域近似 off（默认）| on

在绘制运算放大器的开环响应时，除 *s* 域传递函数外，还包括 *z* 域（离散时间）近似。

### **Plot open loop response** — 绘制运放开环响应 button

绘制运算放大器开环响应的 *s* 域传递函数。该图还报告单位增益带宽和相位裕度。您可以选择包含 *z* 域近似。
## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

Not documented in R2025b.

## 扩展功能

Not documented in R2025b.

## 版本历史

**在 R2021b 中引入**

### R2024a: Plot Open Loop Response

您现在可以绘制运算放大器的开环响应，以及 *z* 域近似。

## 描述

使用两个或多个极点对运算放大器进行建模

使用 Operational Amplifier 模块对具有两个或更多极点的运算放大器进行建模。您可以根据重要电路参数创建双极点放大器，或根据传递函数创建多极点放大器。使用该模块可将运算放大器的性能表征为更大电路系统的一部分。
