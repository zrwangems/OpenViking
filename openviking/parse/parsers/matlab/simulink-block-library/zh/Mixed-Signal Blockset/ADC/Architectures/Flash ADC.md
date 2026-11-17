---
type: simulink-block
title: 'Flash ADC'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Architectures'
documentation_page: 'flashadc'
documentation_source_path: 'ref/flashadc.html'
language: zh-CN
chinese_source: worker-translation
---

# Flash ADC

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

### **Number of bits** — 物理输出位数 `10`（默认）| `[1, 26]` 范围内的正实整数

物理输出位数，指定为 `[1, 26]` 范围内的无单位正实整数。**Number of bits** 决定 ADC 的分辨率。

#### 程序化使用

- 使用 `get_param(gcb,'NBits')` 查看当前的 **Number of bits**。
- 使用 `set_param(gcb,'NBits',value)` 将 **Number of bits** 设置为特定值。

**数据类型：** `double`

### **Input range (V)** — ADC 动态范围 `[-1 1]`（默认）| 2 元素行向量

ADC 动态范围，指定为以伏特为单位的 2 元素行向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputRange` |
| **类型：** 字符向量 |
| **值：** 2 元素行向量 |
| **默认：** `[-1 1]` |

**数据类型：** `double`

### **Use external start clock** — 连接到外部启动转换时钟 on（默认）| off

选择此项以连接到外部启动转换时钟。默认情况下，此选项处于选中状态。如果取消选择此选项，则使用 Flash ADC 内部的 Sampling Clock Source 模块来生成启动转换时钟。

### **Conversion start frequency (Hz)** — 内部启动转换时钟的频率 `1e6`（默认）| 正实标量

内部启动转换时钟的频率，指定为以赫兹为单位的正实标量。**Conversion start frequency (Hz)** 决定 ADC 的速率。

#### 依赖关系

此参数仅在未选择 **Use external start clock** 时可用。

#### 程序化使用

- 使用 `get_param(gcb,'StartFreq')` 查看 **Conversion start frequency (Hz)** 的当前值。
- 使用 `set_param(gcb,'StartFreq',value)` 将 **Conversion start frequency (Hz)** 设置为特定值。

**数据类型：** `double`

### **RMS aperture jitter (s)** — 添加到启动转换时钟的 RMS 孔径抖动 `1e-12`（默认）| 实非负标量

作为损伤添加到启动转换时钟的 RMS 孔径抖动，指定为以秒为单位的实非负标量。如果需要干净的时钟信号，请将 **RMS aperture jitter** 值设置为零。

#### 依赖关系

此参数仅在未选择 **Use external start clock** 时可用。

#### 程序化使用

- 使用 `get_param(gcb,'StartClkJitter')` 查看 **RMS aperture jitter (s)** 的当前值。
- 使用 `set_param(gcb,'StartClkJitter',value)` 将 **RMS aperture jitter (s)** 设置为特定值。

**数据类型：** `double`

### **Edge trigger type** — 触发输出更新的时钟边沿类型 `Rising edge`（默认）| `Falling edge` | `Either edge`

触发输出更新的时钟边沿类型：

- `Rising edge` — 输出在时钟信号的上升沿更新。
- `Falling edge` — 输出在时钟信号的下降沿更新。
- `Either edge` — 输出在时钟信号的上升沿和下降沿均更新。

#### 程序化使用

- 使用 `get_param(gcb,'Trigger')` 查看当前的 **边沿触发类型**。
- 使用 `set_param(gcb,'Trigger',value)` 将 **边沿触发类型** 设置为特定值。

### **匹配输入量程** — 从输入继承输出极性和数据类型 关（默认）| 开

从 ADC 的模拟输入信号继承输出极性和数据类型。如果选择此选项，ADC 将忽略 **输出极性** 和 **输出数据类型** 参数。ADC 输出具有与输入相同的极性，数据类型为 double。

### **输出极性** — 定义 ADC 输出极性 `Auto`（默认）| `Bipolar` | `Unipolar`

定义 ADC 输出数据极性。

如果 **输出极性** 设置为 `Auto`，输出的最小值和最大值由 **输入范围** 的极性决定。

如果 **输出极性** 设置为 `Bipolar`，输出介于 `-2Nbits-1` 和 `2Nbits-1-1` 之间。

如果 **输出极性** 设置为 `Unipolar`，输出介于 `0` 和 `2Nbits-1` 之间。

#### 依赖关系

要启用此参数，请取消选择 **匹配输入量程** 选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputPolarity` |
| **类型：** 字符向量 |
| **值：** `Auto` | `Bipolar` | `Unipolar` |
| **默认：** `Auto` |

### **输出数据类型** — 定义 ADC 输出数据类型 `fixdt(1,Nbits)`（默认）| `fixdt(0,Nbits)` | `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Inherit: Inherit via back propagation`

定义 ADC 输出数据类型。

当 **输出极性** 设置为 `Bipolar` 或 `Auto` 时，无符号整数和定点类型（`fixdt(0,Nbits)`）不可用。

当 **输出极性** 设置为 `Unipolar` 时，有符号整数和定点类型（`fixdt(1,Nbits)`）不可用。

#### 依赖关系

要启用此参数，请取消选择 **匹配输入量程** 选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutDataType` |
| **类型：** 字符向量 |
| **值：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixdt(0,Nbits)` | `fixdt(1,Nbits)` | `Inherit: Inherit via back propagation` |
| **默认：** `fixdt(1,Nbits)` |

### **仿真方式** — 定义如何仿真 ADC `Simulink blocks`（默认）| `System object (interpreted)` | `System object (code generation)`

定义 Flash ADC 模块在仿真中的使用方式。您可以将该模块用作 Simulink® 模块，或使用 System object™ 实现（解释执行或代码生成）以获得更多控制。

### 损伤

### **启用线性度损伤** — 在 ADC 仿真中启用线性度损伤 关（默认）| 开

选择以在 ADC 仿真中启用线性度损伤，例如偏移误差和增益误差。默认情况下，此选项未选中。

### **偏移误差** — 按特定值偏移量化步长 `3 LSB`（默认）| 实数标量

按特定值偏移量化步长，以 %FS、FS 或 LSB 为单位的标量指定。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿传输曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5 LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = 转换器满量程范围2NBits。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用线性度损伤**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OffsetError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `3 LSB` |

**数据类型：** `double`

### **增益误差** — ADC 转换曲线斜率的误差 `2 LSB`（默认）| 实数标量

用于插值 ADC 转换曲线的直线的斜率误差，指定为以 %FS、FS 或 LSB 为单位的实数标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿转换曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿转换曲线中，第一个码的宽度为 0.5 LSB，而最后一个码的宽度为 1.5 LSB。输入值必须考虑在转换器的满量程范围内。

**注意**

LSB 由以下公式计算：LSB = 转换器的满量程范围2NBits。

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

### **缺失码** — 失效比较器的位置 `[]`（默认）| 具有正实数值的行向量

失效比较器的位置，指定为具有正实数值的行向量。

#### 依赖关系

此参数仅在选中**启用线性损伤**时可用。

#### 程序化使用

- 使用 `get_param(gcb,'Bubbles')` 查看当前的**缺失码**。
- 使用 `set_param(gcb,'Bubbles',value)` 将**缺失码**设置为特定值。

**数据类型：** `double`

### **启用时序损伤** — 在 ADC 仿真中启用时序损伤 off（默认）| on

选择以在 ADC 仿真中启用时序损伤，例如转换延迟。默认情况下，此选项未选中。

### **转换延迟 (s)** — ADC 的延迟 `0`（默认）| 非负实数标量

模数转换器的延迟，指定为非负实数标量。

#### 依赖关系

此参数仅在选中**启用时序损伤**时可用。如果您在 System object 模式下使用 Flash ADC，此值将舍入到采样间隔的最近倍数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ConversionDelay` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0` |

**数据类型：** `double`

### **启用增加的缓冲区大小** — 启用增加的缓冲区大小 off（默认）| on

选择以在仿真期间启用增加的缓冲区大小。默认情况下，此选项未选中。

#### 依赖关系

要启用此参数，请在配置选项卡中将**仿真使用**设置为 `Simulink blocks`，并在损伤选项卡中选择**启用时序损伤**。

### **缓冲区大小** — 额外缓冲区滤波器的数量 `100`（默认）| 正实数标量

仿真期间可用的额外缓冲区滤波器的数量，指定为正实数标量。

选择不同的仿真求解器或采样策略可能会改变生成准确输出样本所需的输入样本数量。将**缓冲区大小**设置为足够大的值，以便输入缓冲区包含所需的所有输入样本。

#### 依赖关系

要启用此参数，请在配置选项卡中将**仿真使用**设置为 `Simulink blocks`。然后在损伤选项卡中选择**启用时序损伤**和**启用增加的缓冲区大小**。

## 所属库

Mixed-Signal Blockset / ADC / Architectures

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

采用闪存架构的 N 位 ADC

一个 *N* 位闪存 ADC 由包含
2*N* 个电阻的电阻梯和
2*N*-1 个比较器组成。

每个比较器的参考电压比其在电阻梯中下方的比较器高 1 个最低有效位（LSB）。因此，低于某一特定点的所有比较器其输入电压将大于参考电压，并输出逻辑 `1`。高于该点的所有比较器其输入电压将小于参考电压，并输出逻辑 `0`。
2*N*-1 个比较器的输出通过优先编码器以产生数字输出。这种编码方案称为温度计编码。

由于模拟输入一次性施加到所有比较器，闪存 ADC 架构速度非常快。但由于实现该架构需要大量电阻，该 ADC 的分辨率较低且功耗要求较高。
