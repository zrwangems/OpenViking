---
type: simulink-block
title: 'SAR ADC'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Architectures'
documentation_page: 'saradc'
documentation_source_path: 'ref/saradc.html'
language: zh-CN
chinese_source: worker-translation
---

# SAR ADC

## 端口

### 输入

### **analog** — 模拟输入信号 标量

模拟输入信号，指定为标量。

**数据类型：** `double`

### **start** — 用于启动转换的外部时钟 标量

用于启动转换的外部时钟，指定为标量。模数转换过程在 **start** 端口信号的上升沿开始。

**数据类型：** `double`
### 输出

### **digital** — 转换后的数字输出信号 标量

转换后的数字输出信号，以标量形式返回。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **ready** — 确定模数转换是否完成 标量

确定模数转换是否完成，以标量形式返回。

**数据类型：** `double`

## 参数

### 配置

### **Number of bits** — 物理输出位数 `8`（默认）| `[1, 26]` 范围内的正实数整数

物理输出位数，指定为 `[1, 26]` 范围内的无单位正实数整数。**Number of bits** 决定 ADC 的分辨率。

#### 编程用法

- 使用 `get_param(gcb,'NBits')` 查看当前的 **Number of bits**。
- 使用 `set_param(gcb,'NBits',value)` 将 **Number of bits** 设置为特定值。

**数据类型：** `double`

### **Input range (V)** — ADC 动态范围 `[-1 1]`（默认）| 2 元素行向量

ADC 动态范围，指定为以伏特为单位的 2 元素行向量。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputRange` |
| **类型：** 字符向量 |
| **值：** 2 元素行向量 |
| **默认：** `[-1 1]` |

**数据类型：** `double`

### **Use external start clock** — 连接到外部启动转换时钟 on（默认）| off

选择此项以连接到外部启动转换时钟。默认情况下，此选项处于选中状态。如果取消选择此选项，则使用 SAR ADC 内部的 Sampling Clock Source 模块来生成启动转换时钟。

### **Conversion start frequency (Hz)** — 内部启动转换时钟的频率 `10e3`（默认）| 正实数标量

内部启动转换时钟的频率，指定为以 Hz 为单位的正实数标量。**Conversion start frequency** 决定 ADC 的速率。

#### 依赖关系

此参数仅在未选择 **Use external start clock** 时可用。

#### 编程用法

- 使用 `get_param(gcb,'StartFreq')` 查看 **Conversion start frequency (Hz)** 的当前值。
- 使用 `set_param(gcb,'StartFreq',value)` 将 **Conversion start frequency (Hz)** 设置为特定值。

**数据类型：** `double`

### **RMS aperture jitter (s)** — 添加到启动转换时钟的 RMS 孔径抖动 `0`（默认）| 实数非负标量

作为损伤添加到启动转换时钟的 RMS 孔径抖动，指定为以 s 为单位的实数非负标量。如果需要干净的时钟信号，请将 **RMS aperture jitter** 值设置为零。

#### 依赖关系

此参数仅在未选择 **Use external start clock** 时可用。

#### 编程用法

- 使用 `get_param(gcb,'StartClkJitter')` 查看 **RMS aperture jitter (s)** 的当前值。
- 使用 `set_param(gcb,'StartClkJitter',value)` 将 **RMS aperture jitter (s)** 设置为特定值。

**数据类型：** `double`

### **SAR Frequency (Hz)** — SAR 时钟的频率 `2e7`（默认）| 实数标量

SAR 时钟的频率，指定为以 Hz 为单位的实数标量。**SAR Frequency (Hz)** 必须足够高，以允许 ADC 执行 *Nbits* 次比较，其中 *Nbits* 是 ADC 的 **Number of bits**。由于代数环移除，该模块有一个周期开销。因此，时钟必须再运行一个周期，输出才会就绪。因此，**SAR Frequency (Hz)**（*f*SAR）由以下方程给出：fSAR≥(Nbits+1)fstart，其中 *f*start 是 **Conversion start frequency**。

#### 编程用法

- 使用 `get_param(gcb,'SARFreq')` 查看 **SAR Frequency (Hz)** 的当前值。
- 使用 `set_param(gcb,'SARFreq',value)` 将 **SAR Frequency (Hz)** 设置为特定值。

### **Match input scale** — 从输入继承输出极性和数据类型 off（默认）| on

从 ADC 的模拟输入信号继承输出极性和数据类型。如果选择此选项，ADC 将忽略 **Output polarity** 和 **Output data type** 参数。ADC 输出具有与输入相同的极性，数据类型为 double。

### **Output polarity** — 定义 ADC 输出极性 `Auto`（默认）| `Bipolar` | `Unipolar`

定义 ADC 输出数据极性。

如果 **Output polarity** 设置为 `Auto`，输出的最小值和最大值由 **Input range** 的极性决定。

如果 **Output polarity** 设置为 `Bipolar`，输出介于 `-2Nbits-1` 和 `2Nbits-1-1` 之间。

如果 **Output polarity** 设置为 `Unipolar`，输出介于 `0` 和 `2Nbits-1` 之间。

#### 依赖关系

要启用此参数，请取消选择 **Match input scale** 选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputPolarity` |
| **类型：** 字符向量 |
| **值：** `Auto` | `Bipolar` | `Unipolar` |
| **默认：** `Auto` |

### **Output data type** — 定义 ADC 输出数据类型 `fixdt(1,Nbits)`（默认）| `fixdt(0,Nbits)` | `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Inherit: Inherit via back propagation`

定义 ADC 输出数据类型。

当 **Output polarity** 设置为 `Bipolar` 或 `Auto` 时，无符号整数和定点类型（`fixdt(0,Nbits)`）不可用。

当 **Output polarity** 设置为 `Unipolar` 时，有符号整数和定点类型（`fixdt(1,Nbits)`）不可用。

#### 依赖关系

要启用此参数，请取消选择 **Match input scale** 选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataType` |
| **类型：** 字符向量 |
| **值：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixdt(0,Nbits)` | `fixdt(1,Nbits)` | `Inherit: Inherit via back propagation` |
| **默认：** `fixdt(1,Nbits)` |

### 非理想特性

### **Enable Linearity Impairments** — 在 ADC 仿真中启用线性度非理想特性 off（默认）| on

选择以在 ADC 仿真中启用线性度非理想特性，例如偏移误差和增益误差。默认情况下，此选项未选中。

### **Offset error** — 将量化步长偏移特定值 `1 LSB`（默认）| 实数标量

将量化步长偏移特定值，以最低有效位（LSB）或 % 为单位指定为标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿转换曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿转换曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5 LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = 转换器满量程范围2NBits。

#### 依赖关系

此参数仅在选中 **Enable Linearity Impairments** 时可用。

#### 编程用法

- 使用 `get_param(gcb,'OffsetError')` 查看 **Offset error (LSB)** 的当前值。
- 使用 `set_param(gcb,'OffsetError',value)` 将 **Offset error (LSB)** 设置为特定值。

**数据类型：** `double`

### **Gain error** — ADC 转换曲线斜率的误差 `2 LSB`（默认）| 实数标量

用于插值 ADC 转换曲线的直线斜率的误差，指定为以 %FS、FS 或 LSB 表示的实数标量。

**注意**

转换器的满量程范围定义为在 +0.5 LSB 补偿转换曲线上的最后一个码与第一个码之间的差。在 +0.5 LSB 补偿转换曲线中，第一个码宽为 0.5 LSB，而最后一个码宽为 1.5 LSB。输入值必须考虑在转换器的满量程范围内。

**注意**

LSB 由方程 LSB = 转换器满量程范围2NBits 计算。

#### 依赖关系

要启用此参数，请在**损伤**选项卡中选择**启用线性损伤**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `GainError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `2 LSB` |

**数据类型：** `double`

## 所属库

Mixed-Signal Blockset / ADC / Architectures

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

基于 N 位逐次逼近寄存器（SAR）的 ADC

基于逐次逼近寄存器（SAR）的 ADC 由采样保持电路（SHA）、比较器、内部数模转换器（DAC）和逐次逼近寄存器组成。

当 ADC 接收到 **start** 命令时，SHA 被置于保持模式。
SAR 的最高有效位（MSB）被设置为逻辑 `1`，所有其他位被设置为逻辑 `0`。

SAR 的输出被反馈到 DAC，其输出与输入信号进行比较。如果 DAC 输出大于模拟输入，则 MSB 被复位，否则保持置位。下一个 MSB 现在被设置为 1，并且重复该过程，直到 SAR 的每一位都被比较。该过程结束时 SAR 的最终值对应于模拟输入值。转换过程的结束由 **ready** 信号指示。
