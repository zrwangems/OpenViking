---
type: simulink-block
title: 'Binary Weighted DAC'
family: 'dac'
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

### **digital** — 至 DAC 的数字输入信号 integer

至 DAC 的数字输入信号，指定为整数。

如果 **输入极性** 参数设置为 `Bipolar`，信号允许范围是
[−2(*NBits*-1),
2(*NBits*-1)-1]。

如果 **输入极性** 参数设置为 `Unipolar`，信号允许范围是 [0,
2*NBits*-1]。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **start** — 用于开始转换的外部时钟 scalar

用于开始转换的外部时钟，指定为标量。数模转换过程在 **start** 端口处信号的上升沿开始。

#### 依赖关系

要启用此端口，请在 **常规** 选项卡中选择 **使用外部启动时钟**。

**数据类型：** `double`

### 输出

### **analog** — 转换后的模拟输出信号 scalar

转换后的模拟输出信号，以标量形式返回。

**数据类型：** `double`

### **ready** — 指示数模转换是否完成 scalar

指示数模转换是否完成，以标量形式返回。

#### 依赖关系

要启用此端口，请在 **常规** 选项卡中选择 **显示 ready 端口**。

**数据类型：** `double`

## 参数

### 常规

### **位数** — 输入字中的位数 `5` (默认) | positive real integer

输入字中的位数，指定为无单位正整数。**位数** 决定 DAC 的分辨率。

#### 编程用法

|  |
| --- |
| **模块参数：** `NBits` |
| **类型：** character vector |
| **值：** 正整数 |
| **默认：** `5` |

**数据类型：** `double`

### **输入极性** — 至 DAC 的输入信号极性 `Bipolar` (默认) | `Unipolar`

至 DAC 的输入信号极性。

#### 编程用法

|  |
| --- |
| **模块参数：** `Polarity` |
| **类型：** character vector |
| **值：** `Bipolar`|`Unipolar` |
| **默认：** `Bipolar` |

### **使用外部启动时钟** — 连接到外部启动转换时钟 on (默认) | off

选择以连接到外部启动转换时钟。默认情况下，此选项已选中。如果清除此选项，则使用 Segmented DAC 内部的 Sampling Clock Source 模块生成启动转换时钟。

### **转换启动频率 (Hz)** — 内部启动转换时钟频率 `1e6` (默认) | positive real scalar

内部启动转换时钟的频率，指定为以 Hz 为单位的实数标量。**转换启动频率** 参数确定转换开始时的转换速率。

#### 依赖关系

要启用此参数，请清除 **使用外部启动时钟**。

#### 编程用法

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认：** `1e6` |

**数据类型：** `double`

### **参考电压 (V)** — 参考电压 `2` (默认) | real scalar

DAC 的参考电压，指定为以 V 为单位的实数标量。**参考电压 (V)** 使用以下方程帮助根据输入数字码、**位数** 和 **偏置 (V)** 确定输出：

DAC output = ((Digital input code2Number of bits)Reference)+Bias.

#### 编程用法

|  |
| --- |
| **模块参数：** `Ref` |
| **类型：** character vector |
| **值：** 实数标量 |
| **默认：** `2` |

**数据类型：** `double`

### **偏置 (V)** — 添加到输出的偏置电压 `0` (默认) | real scalar

添加到 DAC 输出的偏置电压，指定为以 V 为单位的实数标量。**偏置 (V)** 使用以下方程帮助根据输入数字码、**位数** 和 **参考电压 (V)** 确定输出：

DAC output = ((Digital input code2Number of bits)Reference)+Bias.

#### 编程用法

|  |
| --- |
| **模块参数：** `Bias` |
| **类型：** character vector |
| **值：** 实数标量 |
| **默认：** `0` |

**数据类型：** `double`

### **显示 ready 端口** — 在模块上启用 ready 端口 off (默认) | on

选择以启用模块上的 **ready** 端口。默认情况下，此选项已清除。

### 损伤

### **启用线性损伤** — 在 DAC 仿真中启用失调误差和增益误差 on (默认) | off

选择以在 DAC 仿真中启用失调误差和增益误差等损伤。默认情况下，此参数已选中。

### **失调误差** — 按特定值移动量化步长 `0 LSB` (默认) | real scalar

按特定值移动量化步长，指定为以 %FS（满量程百分比）、FS（满量程）或 LSB（最低有效位）为单位的标量。

**失调误差** 在 **参考电压 (V)** 和 **偏置 (V)** 之前应用。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之差。在 +0.5 LSB 补偿传输曲线中，第一个码宽为 0.5 LSB，而最后一个码宽为 1.5 LSB。输入值必须考虑在转换器的满量程范围内。

**注意**

LSB 由方程 LSB = Full scale range of converter2NBits 计算。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用线性损伤**。

#### 编程用法

|  |
| --- |
| **模块参数：** `OffsetError` |
| **类型：** character vector |
| **值：** 实数标量 |
| **默认：** `0 LSB` |

**数据类型：** `double`

### **增益误差** — DAC 传输曲线斜率误差 `0 LSB` (默认) | real scalar

插值 DAC 传输曲线的直线斜率误差，指定为以 %FS（满量程百分比）、FS（满量程）或 LSB（最低有效位）为单位的实数标量。

**增益误差** 在 **参考电压 (V)** 和 **偏置 (V)** 之前应用。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之差。在 +0.5 LSB 补偿传输曲线中，第一个码宽为 0.5 LSB，而最后一个码宽为 1.5 LSB。输入值必须考虑在转换器的满量程范围内。

**注意**

LSB 由方程 LSB = Full scale range of converter2NBits 计算。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用线性损伤**。

#### 编程用法

|  |
| --- |
| **模块参数：** `GainError` |
| **类型：** character vector |
| **值：** 实数标量 |
| **默认：** `0 LSB` |

**数据类型：** `double`

### **启用时序损伤** — 在 DAC 仿真中启用时序损伤 on (默认) | off

选择以在 DAC 仿真中启用建立时间或压摆率等时序损伤。默认情况下，此参数已选中。

### **指定开关时序使用** — 指定 DAC 计算开关时序的方式 `Settling time` (默认) | `Slew rate`

指定 Binary Weighted DAC 是使用建立时间参数还是压摆率参数来计算开关时序。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用时序损伤**。

### **建立时间 (s)** — 输出建立所需时间 `2e-7` (默认) | nonnegative real scalar

DAC 输出建立到其最终值的某个分数范围内所需的时间，指定为以 s 为单位的非负实数标量。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用时序损伤**，并将 **指定开关时序使用** 设置为 `Settling time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SettlingTime` |
| **类型：** character vector |
| **值：** 实数标量 |
| **默认：** `2e-7` |

**数据类型：** `double`

### **建立时间容差 (LSB)** — 计算建立时间的容差 `0.5` (默认) | positive real scalar

计算建立时间所允许的容差，指定为以 LSB 为单位的正实数标量。DAC 的输出必须在 **建立时间 (s)** 之前建立到 **建立时间容差 (LSB)** 范围内。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用时序损伤**，并将 **指定开关时序使用** 设置为 `Settling time`。

#### 编程用法

|  |
| --- |
| **模块参数：** `SettlingTimeTolerance` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认：** `0.5` |

**数据类型：** `double`

### **上升压摆率** — DAC 的开关上升压摆率 `5015625` (默认) | positive real scalar | positive real vector

DAC 的开关上升压摆率，指定为正实数标量或向量。如果 **上升压摆率** 是标量，则为所有开关指定相同的压摆率。如果 **上升压摆率** 是长度为 *Nbits* 的向量，则为每个单独开关指定压摆率。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用时序损伤**，并将 **指定开关时序使用** 设置为 `Slew rate`。

#### 编程用法

|  |
| --- |
| **模块参数：** `RisingSlewRate` |
| **类型：** character vector |
| **值：** 正实数标量 | 正实数向量 |
| **默认：** `5015625` |

### **下降压摆率** — DAC 的开关下降压摆率 `-5015625` (默认) | negative real scalar | negative real vector

DAC 的开关下降压摆率，指定为正实数标量或向量。如果 **下降压摆率** 是标量，则为所有开关指定相同的压摆率。如果 **下降压摆率** 是长度为 *Nbits* 的向量，则为每个单独开关指定压摆率。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用时序损伤**，并将 **指定开关时序使用** 设置为 `Slew rate`。

#### 编程用法

|  |
| --- |
| **模块参数：** `FallingSlewRate` |
| **类型：** character vector |
| **值：** 负实数标量 | 负实数向量 |
| **默认：** `-5015625` |

## 所属库

Mixed-Signal Blockset / DAC / Architectures

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

基于 R-2R 加权电阻架构的 N 位 DAC

R-2R DAC 是最常见的 Binary-Weighted DAC 类型之一。它由一个并联二进制加权电阻组构成。每个数字电平由电阻组转换为等效模拟信号。

二进制加权 DAC 的输入/输出传输曲线可能是非单调的，这意味着传输曲线可以反转其方向。

R-2R DAC 架构分辨率低，并且由于实现该架构需要大量电阻器，因此消耗更多功率。
