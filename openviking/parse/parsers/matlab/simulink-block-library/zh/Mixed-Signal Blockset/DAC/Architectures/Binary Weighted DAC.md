---
type: simulink-block
title: 'Binary Weighted DAC'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'DAC / Architectures'
documentation_page: 'binaryweighteddac'
documentation_source_path: 'ref/binaryweighteddac.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary Weighted DAC

## 端口

### 输入

### **digital** — 输入到 DAC 的数字输入信号 整数

输入到 DAC 的数字输入信号，指定为整数。

如果 **Input polarity** 参数设置为
`Bipolar`，则信号的允许范围为
[−2(*NBits*-1),
2(*NBits*-1)-1]。

如果 **Input polarity** 参数设置为
`Unipolar`，则信号的允许范围为 [0,
2*NBits*-1]。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **start** — 用于启动转换的外部时钟 标量

用于启动转换的外部时钟，指定为标量。数模转换过程在
**start** 端口信号的上升沿开始。

#### 依赖关系

要启用此端口，请在
**General** 选项卡中选择 **Use external start clock**。

**数据类型：** `double`
### 输出

### **analog** — 转换后的模拟输出信号 标量

转换后的模拟输出信号，以标量形式返回。

**数据类型：** `double`

### **ready** — 指示数模转换是否完成 标量

指示数模转换是否完成，以标量形式返回。

#### 依赖关系

要启用此端口，请在
**General** 选项卡中选择 **Show ready port**。

**数据类型：** `double`

## 参数

### 常规

### **Number of bits** — 输入字中的位数 `5`（默认）| 正实数整数

输入字中的位数，指定为无单位的正实数整数。
**Number of bits** 决定 DAC 的分辨率。

#### 编程使用

|  |
| --- |
| **模块参数：** `NBits` |
| **类型**：character vector |
| **值**：positive real integer |
| **默认值**：`5` |

**数据类型：** `double`

### **Input polarity** — 输入到 DAC 的信号的极性 `Bipolar`（默认）| `Unipolar`

输入到 DAC 的信号的极性。

#### 编程使用

|  |
| --- |
| **模块参数：** `Polarity` |
| **类型**：character vector |
| **值**：`Bipolar`|`Unipolar` |
| **默认值**：`Bipolar` |

### **Use external start clock** — 连接到外部启动转换时钟 on（默认）| off

选择以连接到外部启动转换时钟。默认情况下，此选项为选中状态。如果取消选择此选项，则使用 Segmented DAC 内部的 Sampling Clock
Source 模块来生成启动转换时钟

### **Conversion start frequency (Hz)** — 内部启动转换时钟的频率 `1e6`（默认）| 正实数标量

内部启动转换时钟的频率，指定为以 Hz 为单位的实数标量。
**Conversion start frequency** 参数决定转换开始时的转换速率。

#### 依赖关系

要启用此参数，请取消选择 **Use external start
clock**。

#### 编程使用

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型**：character vector |
| **值**：positive real scalar |
| **默认值**：`1e6` |

**数据类型：** `double`

### **Reference (V)** — 参考电压 `2`（默认）| 实数标量

DAC 的参考电压，指定为以伏特为单位的实数标量。**Reference
(V)** 有助于根据输入数字代码、
**Number of bits** 和 **Bias (V)** 使用以下方程确定输出：

DAC 输出 = ((数字输入码2位数)参考)+偏置。

#### 编程使用

|  |
| --- |
| **模块参数：** `Ref` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`2` |

**数据类型：** `double`

### **Bias (V)** — 添加到输出的偏置电压 `0`（默认）| 实数标量

添加到 DAC 输出的偏置电压，指定为以伏特为单位的实数标量。
**Bias (V)** 有助于根据输入数字
代码、**Number of bits** 和 **Reference (V)** 使用
以下方程确定输出：

DAC 输出 = ((数字输入码2位数)参考)+偏置。

#### 编程使用

|  |
| --- |
| **模块参数：** `Bias` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`0` |

**数据类型：** `double`

### **Show ready port** — 在模块上启用 ready 端口 off（默认）| on

选择以在模块上启用 **ready** 端口。默认情况下此选项未选中。

###  impairments

### **Enable linearity impairments** — 在 DAC 仿真中启用偏移和增益误差 on（默认）| off

选择以在 DAC 仿真中启用偏移误差和增益误差等损伤。默认情况下此参数已选中。

### **Offset error** — 将量化步长偏移特定值 `0 LSB`（默认）| 实数标量

将量化步长偏移特定值，以 %FS（满量程百分比）、FS（满量程）或 LSB（最低有效位）为单位指定为标量。

**Offset error** 在 **Reference (V)** 和 **Bias (V)** 之前应用。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿传输曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5 LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = Full scale range of converter2NBits。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Enable linearity impairments**。

#### 编程使用

|  |
| --- |
| **模块参数：** `OffsetError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0 LSB` |

**数据类型：** `double`

### **Gain error** — DAC 传输曲线斜率误差 `0 LSB`（默认）| 实数标量

插值 DAC 传输曲线的直线斜率误差，以 %FS（满量程百分比）、FS（满量程）或 LSB（最低有效位）为单位指定为实数标量。

**Gain error** 在 **Reference (V)** 和 **Bias (V)** 之前应用。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿传输曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5 LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = Full scale range of converter2NBits。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Enable linearity impairments**。

#### 编程使用

|  |
| --- |
| **模块参数：** `GainError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0 LSB` |

**数据类型：** `double`

### **Enable timing impairments** — 在 DAC 仿真中启用时序损伤 on（默认）| off

选择以在 DAC 仿真中启用建立时间或压摆率等时序损伤。默认情况下此参数已选中。

### **Specify switch timing using** — 指定 DAC 如何计算开关时序 `Settling time`（默认）| `Slew rate`

指定 Binary Weighted DAC 是使用建立时间参数还是压摆率参数来计算开关时序。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Enable timing impairments**。

### **Settling time (s)** — 输出建立所需时间 `2e-7`（默认）| 非负实数标量

DAC 输出建立到其最终值某一比例范围内所需的时间，以秒为单位指定为非负实数标量。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Enable timing impairments** 并将 **Specify switch timing using** 设置为 `Settling time`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SettlingTime` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `2e-7` |

**数据类型：** `double`

### **Settling time tolerance (LSB)** — 用于计算建立时间的容差 `0.5`（默认）| 正实数标量

用于计算建立时间的容差，指定为以 LSB 为单位的正实数标量。DAC 的输出必须在 **Settling time (s)** 之前稳定在 **Settling time tolerance (LSB)** 范围内。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Enable timing impairments**，并将 **Specify switch timing using** 设置为 `Settling time`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTimeTolerance` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `0.5` |

**数据类型：** `double`

### **Rising slew rate** — DAC 的开关上升压摆率 `5015625`（默认）| 正实数标量 | 正实数向量

DAC 的开关上升压摆率，指定为正实数标量或向量。如果 **Rising slew rate** 是标量，则为所有开关指定相同的压摆率。如果 **Rising slew rate** 是长度为 *Nbits* 的向量，则为每个单独的开关指定压摆率。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Enable timing impairments**，并将 **Specify switch timing using** 设置为 `Slew rate`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RisingSlewRate` |
| **类型：** 字符向量 |
| **值：** 正实数标量 | 正实数向量 |
| **默认：** `5015625` |

### **Falling slew rate** — DAC 的开关下降压摆率 `-5015625`（默认）| 负实数标量 | 负实数向量

DAC 的开关下降压摆率，指定为正实数标量或向量。如果 **Falling slew rate** 是标量，则为所有开关指定相同的压摆率。如果 **Falling slew rate** 是长度为 *Nbits* 的向量，则为每个单独的开关指定压摆率。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Enable timing impairments**，并将 **Specify switch timing using** 设置为 `Slew rate`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FallingSlewRate` |
| **类型：** 字符向量 |
| **值：** 负实数标量 | 负实数向量 |
| **默认：** `-5015625` |

## 所属库

Mixed-Signal Blockset / DAC / Architectures

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

基于 R-2R 加权电阻架构的 N 位 DAC

R-2R DAC 是最常见的二进制加权 DAC 类型之一。它由并联的二进制加权电阻组构成。每个数字电平通过电阻组转换为等效的模拟信号。

二进制加权 DAC 的输入/输出传递曲线可能是非单调的，这意味着传递曲线可能反转其方向。

R-2R DAC 架构分辨率较低，并且由于实现该架构需要大量电阻，因此功耗较高。
