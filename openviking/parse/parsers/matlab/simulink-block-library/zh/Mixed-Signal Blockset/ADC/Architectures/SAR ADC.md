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

### **analog** — 模拟输入信号标量

模拟输入信号，指定为标量。

**数据类型：** `double`

### **start** — 用于启动转换的外部时钟标量

用于启动转换的外部时钟，指定为标量。模数转换过程在 **start** 端口信号的上升沿启动。

**数据类型：** `double`
### 输出

### **digital** — 转换后的数字输出信号标量

转换后的数字输出信号，以标量形式返回。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **ready** — 确定模数转换是否完成标量

确定模数转换是否完成，以标量形式返回。

**数据类型：** `double`

## 参数

### 配置

### **位数** — 物理输出位数 `8`（默认） | 范围 `[1, 26]` 内的正实整数

物理输出位数，指定为范围 `[1, 26]` 内的无量纲正实整数。**位数** 决定 ADC 的分辨率。

#### 程序化使用

- 使用 `get_param(gcb,'NBits')` 查看当前 **位数**。
- 使用 `set_param(gcb,'NBits',value)` 将 **位数** 设置为特定值。

**数据类型：** `double`

### **输入范围 (V)** — ADC 动态范围 `[-1 1]`（默认） | 2 元素行向量

ADC 动态范围，指定为以 V 为单位的 2 元素行向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputRange` |
| **类型：** character vector |
| **值：** 2 元素行向量 |
| **默认值：** `[-1 1]` |

**数据类型：** `double`

### **使用外部启动时钟** — 连接到外部启动转换时钟 on（默认） | off

选择以连接到外部启动转换时钟。默认情况下，此选项处于选中状态。如果取消选择此选项，则使用 SAR ADC 内部的 Sampling Clock Source 模块生成启动转换时钟。

### **转换启动频率 (Hz)** — 内部启动转换时钟的频率 `10e3`（默认） | 正实标量

内部启动转换时钟的频率，指定为以 Hz 为单位的正实标量。**转换启动频率** 决定 ADC 的速率。

#### 依赖关系

仅当未选择 **使用外部启动时钟** 时，此参数可用。

#### 程序化使用

- 使用 `get_param(gcb,'StartFreq')` 查看 **转换启动频率 (Hz)** 的当前值。
- 使用 `set_param(gcb,'StartFreq',value)` 将 **转换启动频率 (Hz)** 设置为特定值。

**数据类型：** `double`

### **RMS 孔径抖动 (s)** — 添加到启动转换时钟的 RMS 孔径抖动 `0`（默认） | 实非负标量

作为损伤添加到启动转换时钟的 RMS 孔径抖动，指定为以 s 为单位的实非负标量。如果需要干净的时钟信号，请将 **RMS 孔径抖动** 值设置为零。

#### 依赖关系

仅当未选择 **使用外部启动时钟** 时，此参数可用。

#### 程序化使用

- 使用 `get_param(gcb,'StartClkJitter')` 查看 **RMS 孔径抖动 (s)** 的当前值。
- 使用 `set_param(gcb,'StartClkJitter',value)` 将 **RMS 孔径抖动 (s)** 设置为特定值。

**数据类型：** `double`

### **SAR 频率 (Hz)** — SAR 时钟的频率 `2e7`（默认） | 实标量

SAR 时钟的频率，指定为以 Hz 为单位的实标量。**SAR 频率 (Hz)** 必须足够高，以允许 ADC 执行 *Nbits* 次比较，其中 *Nbits* 是 ADC 的 **位数**。该模块由于代数环移除而有一个周期的开销。因此，时钟必须在输出就绪之前多运行一个周期。因此，**SAR 频率 (Hz)**（*f*SAR）由方程 fSAR≥(Nbits+1)fstart 给出，其中 *f*start 是 **转换启动频率**。

#### 程序化使用

- 使用 `get_param(gcb,'SARFreq')` 查看 **SAR 频率 (Hz)** 的当前值。
- 使用 `set_param(gcb,'SARFreq',value)` 将 **SAR 频率 (Hz)** 设置为特定值。

### **匹配输入标度** — 从输入继承输出极性和数据类型 off（默认） | on

从 ADC 的模拟输入信号继承输出极性和数据类型。如果选择此选项，ADC 将忽略 **输出极性** 和 **输出数据类型** 参数。ADC 输出与输入具有相同极性，且数据类型为 double。

### **输出极性** — 定义 ADC 输出极性 `Auto`（默认） | `Bipolar` | `Unipolar`

定义 ADC 输出数据极性。

如果 **输出极性** 设置为 `Auto`，则输出的最小值和最大值由 **输入范围** 的极性决定。

如果 **输出极性** 设置为 `Bipolar`，则输出介于 `-2Nbits-1` 和 `2Nbits-1-1` 之间。

如果 **输出极性** 设置为 `Unipolar`，则输出介于 `0` 和 `2Nbits-1` 之间。

#### 依赖关系

要启用此参数，请取消选择 **匹配输入标度** 选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputPolarity` |
| **类型：** character vector |
| **值：** `Auto` | `Bipolar` | `Unipolar` |
| **默认值：** `Auto` |

### **输出数据类型** — 定义 ADC 输出数据类型 `fixdt(1,Nbits)`（默认） | `fixdt(0,Nbits)` | `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Inherit: Inherit via back propagation`

定义 ADC 输出数据类型。

当 **输出极性** 设置为 `Bipolar` 或 `Auto` 时，无符号整数和定点类型（`fixdt(0,Nbits)`）不可用。

当 **输出极性** 设置为 `Unipolar` 时，有符号整数和定点类型（`fixdt(1,Nbits)`）不可用。

#### 依赖关系

要启用此参数，请取消选择 **匹配输入标度** 选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutDataType` |
| **类型：** character vector |
| **值：** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixdt(0,Nbits)` | `fixdt(1,Nbits)` | `Inherit: Inherit via back propagation` |
| **默认值：** `fixdt(1,Nbits)` |

### 损伤

### **启用线性度损伤** — 在 ADC 仿真中启用线性度损伤 off（默认） | on

选择以在 ADC 仿真中启用线性度损伤，例如偏移误差和增益误差。默认情况下，此选项未选中。

### **偏移误差** — 以特定值移动量化步长 `1 LSB`（默认） | 实标量

以特定值移动量化步长，指定为以最低有效位 (LSB) 或 % 为单位的标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传递曲线上最后一个码与第一个码之间的差。在 +0.5 LSB 补偿传递曲线中，第一个码宽为 0.5 LSB，而最后一个码宽为 1.5 LSB。输入值必须考虑在转换器的满量程范围内。

**注意**

LSB 由公式 LSB = Full scale range of converter2NBits 计算。

#### 依赖关系

仅当选择 **启用线性度损伤** 时，此参数可用。

#### 程序化使用

- 使用 `get_param(gcb,'OffsetError')` 查看 **偏移误差 (LSB)** 的当前值。
- 使用 `set_param(gcb,'OffsetError',value)` 将 **偏移误差 (LSB)** 设置为特定值。

**数据类型：** `double`

### **增益误差** — ADC 传递曲线斜率上的误差 `2 LSB`（默认） | 实标量

对 ADC 传递曲线进行插值的直线斜率的误差，指定为以 %FS、FS 或 LSB 为单位的实标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传递曲线上最后一个码与第一个码之间的差。在 +0.5 LSB 补偿传递曲线中，第一个码宽为 0.5 LSB，而最后一个码宽为 1.5 LSB。输入值必须考虑在转换器的满量程范围内。

**注意**

LSB 由公式 LSB = Full scale range of converter2NBits 计算。

#### 依赖关系

要启用此参数，请在 **损伤** 选项卡中选择 **启用线性度损伤**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `GainError` |
| **类型：** character vector |
| **值：** 实标量 |
| **默认值：** `2 LSB` |

**数据类型：** `double`

## 所属库

Mixed-Signal Blockset / ADC / Architectures

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2019a 中引入**

## 描述

基于 N 位逐次逼近寄存器 (SAR) 的 ADC

基于逐次逼近寄存器 (SAR) 的 ADC 由采样保持电路 (SHA)、比较器、内部数模转换器 (DAC) 和逐次逼近寄存器组成。

当 ADC 收到 **start** 命令时，SHA 被置于保持模式。SAR 的最高有效位 (MSB) 设置为逻辑 `1`，所有其他位设置为逻辑 `0`。

SAR 的输出反馈到 DAC，其输出与传入的输入信号进行比较。如果 DAC 输出大于模拟输入，则 MSB 被复位，否则保持置位。接下来将下一个 MSB 设置为 1，并重复该过程，直到 SAR 的每一位都比较完毕。该过程结束时 SAR 的最终值对应于模拟输入值。转换过程的结束由 **ready** 信号指示。
