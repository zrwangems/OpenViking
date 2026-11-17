---
type: simulink-block
title: 'Interleaved ADC'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Architectures'
documentation_page: 'interleavedadc'
documentation_source_path: 'ref/interleavedadc.html'
language: zh-CN
chinese_source: worker-translation
---

# Interleaved ADC

## 端口

### 输入

### **analog** — 模拟输入信号 标量

模拟输入信号，指定为标量。

**数据类型：** `double`

### **start** — 启动转换的外部时钟 标量 | 向量

启动转换的外部时钟，指定为标量或向量。如果指定为向量，向量中的元素数量必须等于 ADC 核心的数量。

模数转换过程在 **start** 端口信号的上升沿开始。

**数据类型：** `double` | `Boolean`

### **Offset calibration** — 模拟输入端的失调误差校准 标量 | 向量

加到 ADC 输入以校准失调误差，指定为标量或向量。如果指定为标量，它会被解复用分配到 ADC 核心的模拟输入端。如果指定为向量，向量中的元素数量必须等于 ADC 核心的数量。向量元素按 ADC 核心分别应用。

您也可以使用该端口动态校准每个 ADC 核心的失调误差。

**数据类型：** `double`

### **Gain calibration** — 模拟输入端的增益误差校准 标量 | 向量

乘以模拟输入以校准增益误差，指定为标量或向量。如果指定为标量，它会被解复用分配到 ADC 核心的模拟输入端。如果指定为向量，向量中的元素数量必须等于 ADC 核心的数量。向量元素按 ADC 核心分别应用。

您也可以使用该端口动态校准每个 ADC 核心的增益误差。

**数据类型：** `double`

### 输出

### **digital** — 转换后的数字输出信号 标量 | 向量

转换后的数字输出信号，以标量形式返回。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ready** — 确定模数转换是否完成 标量 | 向量

确定模数转换是否完成，以标量形式返回。

通常，**ready** 信号的数据类型与 **start** 信号的数据类型相同。但如果 start 信号是定点类型或 64 位整数类型，**ready** 信号的数据类型默认为 Boolean。

**数据类型：** `double` | `Boolean`

## 参数

### 配置

### **Number of bits** — 所有 ADC 核心的物理输出位数 `8`（默认）| 标量 | 向量

所有 ADC 核心的物理输出位数，指定为无单位的正实数整数标量或长度为 **NADCs** 的向量。**Number of bits** 决定 ADC 的分辨率。

#### 编程使用

|  |
| --- |
| **模块参数：** `NBits` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认：** `8` |

**数据类型：** `double`

### **Input range** — ADC 动态范围 `[-1 1]`（默认）| 2 元素行向量 | [**NADCs** x 2] 矩阵

ADC 动态范围，指定为以伏特为单位的 2 元素行向量。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputRange` |
| **类型：** 字符向量 |
| **值：** 2 元素行向量 | [**NADCs** x 2] 矩阵 |
| **默认：** `[-1 1]` |

**数据类型：** `double`

### **Linearly interpolate analog input to find sampled value** — 使用正弦转换启动信号进行子采样插值 off（默认）| on

选择以启用使用正弦转换启动信号的子采样插值。这会在输入时钟的过零点处近似输入值。

对于方波转换启动信号，请禁用此参数。

### **Number of ADCs (N)** — 要交错的 ADC 核心数量 `4`（默认）| 正实数整数

要交错的 ADC 核心数量，指定为正实数整数。

#### 编程使用

|  |
| --- |
| **模块参数：** `NADCs` |
| **类型：** 字符向量 |
| **值：** 正实数整数 |
| **默认：** `4` |

**数据类型：** `double`

### **Match output to input scale** — 从输入继承输出极性和数据类型 off（默认）| on

从 ADC 的模拟输入信号继承输出极性和数据类型。
如果选择此选项，ADC 将忽略 **Output polarity**
和 **Output data type** 参数。ADC 输出具有与输入相同的
极性，数据类型为 double。

### **Output polarity** — 定义 ADC 输出极性 `Auto`（默认）| `Bipolar` | `Unipolar`

定义 ADC 输出数据极性。

如果 **Output polarity** 设置为 `Auto`，
输出的最小值和最大值由
**Input range** 的极性决定。

如果 **Output polarity** 设置为
`Bipolar`，输出介于
`-2NBits-1` 和
`2NBits-1-1` 之间。

如果 **Output polarity** 设置为
`Unipolar`，输出介于 `0`
和 `2NBits-1` 之间。

#### 依赖关系

要启用此参数，请取消选择 **Match output to input
scale** 选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputPolarity` |
| **类型：** 字符向量 |
| **值：** `Auto` | `Bipolar` | `Unipolar` |
| **默认值：** `Auto` |

### **Output data type** — 定义 ADC 输出数据类型 `double`（默认）| `single` | `(u)int8` | `(u)int16` | `(u)int32` | `fixdt(OutputPolarity,NBits)`

定义 ADC 输出数据类型。

#### 依赖关系

要启用此参数，请取消选择 **Match output to input
scale** 选项。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataType` |
| **类型：** 字符向量 |
| **值：** `double` | `single` | `(u)int8` | `(u)int16` | `(u)int32` | `fixdt(OutputPolarity,NBits)` |
| **默认值：** `double` |

### **Convert the output to scalar** — 将输出转换为标量 on（默认）| off

将 ADC 的输出转换为标量。该模块使用内部计数器选择最近的
转换结果以产生标量输出。

### **Sample time** — 固定步长采样率 `6.25e-12`（默认）| 正实数标量

固定步长采样率，指定为正实数标量。在 SerDes
系统中使用时，**Sample time** 表示 IBIS-AMI 采样
间隔。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `6.25e-12` |

### **Simulate using** — 定义如何仿真 ADC `Code generation`（默认）| `Interpreted execution`

定义 Interleaved ADC 模块在仿真中的使用方式。您
可以将该模块用作 Simulink® 模块，或使用 System object™ 实现（解释执行或代码生成）以获得更多
控制。

### 损伤

### **Enable linearity impairments** — 在 ADC 仿真中启用线性度损伤 off（默认）| on

选择以在 ADC 仿真中启用线性度损伤，例如偏移误差和增益误差。默认情况
下，此选项未选中。

### **Offset error** — 按特定值偏移量化步长 `0 LSB`（默认）| 实数标量

按特定值偏移量化步长，以 %FS、FS 或
LSB 为单位指定为标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿转换曲线上
最后一个码与第一个码之间的差值。在 +0.5 LSB
补偿转换曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5
LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = 转换器满量程范围2NBits。

#### 依赖关系

要启用此参数，请在 **Impairments** 选项卡中选择 **Enable linearity
impairments**。

#### 编程用法

|  |
| --- |
| **模块参数：** `OffsetError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认值：** `0 LSB` |

**数据类型：** `double`

### **增益误差** — ADC 转换曲线斜率的误差 `0 LSB`（默认）| 实数标量

用于插值 ADC 转换曲线的直线斜率的误差，指定为以 %FS、FS 或 LSB 为单位的实数标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿转换曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿转换曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5 LSB。输入值必须考虑在转换器的满量程范围内。

**注意**

LSB 由以下公式计算：LSB = 转换器满量程范围2NBits。

#### 依赖关系

要启用此参数，请在**损伤**选项卡中选择**启用线性损伤**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `GainError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0 LSB` |

**数据类型：** `double`

### **启用时序损伤** — 在 ADC 仿真中启用时序损伤 关（默认）| 开

选择以在 ADC 仿真中启用时序损伤，例如转换延迟。默认情况下，此选项未选中。

### **转换延迟（秒）** — ADC 的延迟 `0`（默认）| 非负实数标量

模数转换器的延迟，指定为非负实数标量。如果指定为分数，交错 ADC 模块会将其舍入为采样时间最接近的整数倍。

#### 依赖关系

此参数仅在选中**启用时序损伤**时可用。如果您在 System object 模式下使用 Flash ADC，此值会舍入到采样间隔最接近的倍数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ConversionDelay` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0` |

**数据类型：** `double`

### **启用偏移校准端口** — 启用偏移校准端口 关（默认）| 开

选择以启用**偏移校准**端口。此端口的值会加到模拟输入上，以在增益误差校准完成后校准偏移误差。

### **启用增益校准端口** — 启用增益校准端口 关（默认）| 开

选择以启用**增益校准**端口。此端口的值会乘以模拟输入，以校准增益误差。

## 所属库

Mixed-Signal Blockset / ADC / Architectures

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

时间交错 ADC 模型

使用 Interleaved ADC 来支持您设计中的时间交错 ADC 模型。此模块与 SerDes Toolbox™ IBIS-AMI 模型兼容。您可以使用该模块在无限输入范围和位数上进行建模。此模块使用 Flash ADC 作为其核心。

交错 ADC 由一组并联的 ADC 核心组成。

交错 ADC 模型

在 **start** 端口信号的上升沿，ADC 在当前核心上开始转换，并将输入开关索引到下一个核心。当转换完成时，输出开关切换到相关核心。转换结果可在 **digital** 端口获取。该模块还会在 **ready** 端口发送信号的上升沿。此结果会保持，直到下一次转换完成。

当一个 ADC 核心正在进行转换时，该模块可以在其他核心中开始新的转换，从而与单核 ADC 相比提高了吞吐量。
