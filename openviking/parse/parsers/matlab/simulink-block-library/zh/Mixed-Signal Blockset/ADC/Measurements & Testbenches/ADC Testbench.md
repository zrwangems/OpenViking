---
type: simulink-block
title: 'ADC Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Measurements & Testbenches'
documentation_page: 'adctestbench'
documentation_source_path: 'ref/adctestbench.html'
language: zh-CN
chinese_source: worker-translation
---

# ADC Testbench

## 端口

### 输入

### **from adc digital** — 来自 ADC 输出的数字信号 标量

来自 ADC 输出的数字输入信号，指定为标量。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **from adc ready** — 来自 ADC 输出的转换就绪信号 标量

来自 ADC 输出的转换就绪信号，指定为标量。此信号指示 ADC 转换过程何时完成。

**数据类型：** `double`
### 输出

### **to adc analog** — 用于 ADC 输入的模拟激励信号 标量

用于 ADC 输入的模拟输出激励信号，以标量形式返回。

**数据类型：** `double`

### **to adc start** — 用于 ADC 的外部启动转换时钟 标量

用于 ADC 的外部启动转换时钟，以标量形式返回。此信号的上升沿启动 ADC 模块中的转换过程。

**数据类型：** `double`

## 参数

### **Measurement** — 选择测量直流还是交流性能指标 `DC`（默认）| `AC`

选择测量静态（直流）还是动态（交流）性能指标。

- 选择 `DC` 以测量失调误差和增益误差。
- 选择 `AC` 以测量 SNR、SINAD、SFDR、ENOB、噪声底和转换延迟。

### **Recommended min. simulation stop time (s)** — 仿真必须运行以获得有意义结果的最短时间 `2.048e-02`（默认）| 正实数标量

仿真必须运行以获得有意义结果的最短时间，以秒为单位指定为正实数标量。

- 要测量直流性能，仿真必须运行到 ADC 能够对每个数字码进行采样，直到满足误差容限为止。在计算停止时间时，该模块假定每个码至少采样 10 次。您可以根据误差容限（*ErrorTolerance*）计算预期的采样次数（*Samples*）：

  Samples=max(ceil(log2(1ErrorTolerance)),10)

  在这种情况下，推荐的停止时间为：

  StopTime=(Samples·SampleInterval·2Nbits)+HoldOffTime

  其中 *SampleInterval* 是 ADC Testbench 的采样间隔，*Nbits* 是 ADC 的分辨率，*Hold off time* 由 **Hold off time** 参数定义。

  如果信号中存在抖动，推荐的停止时间会增加，以考虑对抖动信号进行采样所需的额外步骤。

  **注意**

  如果您使用 **Sweep range** 参数手动设置扫描范围，则可能需要运行仿真长于推荐的停止时间。

  因此，**Recommended min. simulation stop time (s)** *T* 通过以下公式计算：T=1fanalog+HoldOffTime。
- 要测量交流性能，仿真必须运行到 ADC 能够生成 ADC 输出的 6 次频谱更新。基于 Welch 方法生成一次频谱输出所需的时间由下式给出：

  t=1.5·SamplingFrequencyRBW

  其中 *SamplingFrequency* 和 *RBW* 分别是 ADC Testbench 模块内部频谱估计器的采样频率和分辨率带宽。

此参数仅由测试平台报告，不可编辑。

**数据类型：** `double`

### **Set as model stop time** — 自动将推荐的仿真最短停止时间设置为模型停止时间 按钮

点击以自动将 **Recommended min. simulation stop time (s)** 设置为 Simulink® 模型的停止时间。

### **Endpoint** — 使用端点法测量 DNL、INL 开（默认）| 关

使用端点法测量微分非线性（DNL）误差和积分非线性（INL）误差。此方法使用实际传递函数的端点来测量 DNL 和 INL 误差。

### **Best fit** — 使用最佳拟合方法测量 DNL、INL 开（默认）| 关

使用最佳拟合方法测量微分非线性（DNL）误差和积分非线性（INL）误差。此方法使用标准曲线拟合技术来找到最佳拟合以测量 DNL 和 INL 误差。

### **Plot DC analysis result** — 绘制 DC 分析结果按钮

点击以绘制 DC 分析结果，以便进一步分析。要执行完整的 DC 分析（包括积分非线性 (INL) 和微分非线性 (DNL)），请使用 ADC DC Measurement 模块。

#### 依赖关系

仅当 **Measurement** 选项设置为 `DC` 时，此参数才可用。

### **Export measurement result** — 将详细测试结果存储到基础工作区按钮

点击以将详细测试结果存储为电子表格（XLS 文件）或逗号分隔值（CSV 文件），以便进一步处理。

### Stimulus

### **Sample interval (s)** — ADC Testbench 轮询输入的速率 `1e-6`（默认）| 正实数标量

ADC Testbench 模块轮询其输入的速率，指定为正实数标量，单位为秒。测试台读取输入信号并更新其输出值以控制被测设备。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `DC`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleInterval` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `1e-6` |

### **Distortion measurement type** — 要测量的失真类型 `Harmonic`（默认）| `Intermodulation`

ADC Testbench 模块设置为测量的失真类型，指定为 `Harmonic` 或 `Intermodulation`。

如果模块正在自动计算 **Analog stimulus frequency**，

- 当测量谐波失真时，直接使用计算出的激励频率。
- 当测量互调失真时，谐波选择为计算出的激励频率上下各十分之一。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `AC`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DistortionMeasurement` |
| **类型：** 字符向量 |
| **值：** `Harmonic` | `Intermodulation` |
| **默认值：** `Harmonic` |

### **Analog stimulus frequency (Hz)** — ADC 模拟输入信号的频率 正实数标量 | 正实数值向量

ADC 模块的模拟输入信号频率，指定为正实数标量，单位为赫兹。**Analog stimulus frequency** 必须与被测 ADC 设备的输入频率匹配。默认情况下，此参数自动计算。您可以取消选择 **Set automatically** 来自定义该值。

如果模块正在自动计算 **Analog stimulus frequency**，

- 当测量谐波失真时，直接使用计算出的激励频率。
- 当测量互调失真时，谐波选择为计算出的激励频率上下各十分之一。

**Analog stimulus frequency** 与 **Start conversion frequency** 之间除 1 外不得有任何公倍数。

要满足此条件，请使用公式 fanalog=JMfstart，

其中：

*f*analog 是模拟信号频率，

*f*start 是启动转换频率，

*J* 是每个 FFT 窗口的激励周期数，

*M* 是 FFT 点数。

**注意**

*J* 选择为小于 FFT 点数十分之一的最大质数。*M* 的最小值允许为 16。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `AC`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputFrequency` |
| **类型：** 字符向量 |
| **值：** 正实数标量 | 正实数值向量 |
| **默认值：** `98632.8125` |

### **Resolution bandwidth (Hz)** — 分辨率带宽 正实数标量

分辨率带宽，指定为正实数标量，单位为赫兹。此参数定义了可分辨的最小正频率。默认情况下，此参数自动计算。您可以取消选择 **Set automatically** 来自定义该值。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `AC`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RBW` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `976.5625` |

### **起始转换频率 (Hz)** — ADC 起始转换时钟的频率 `1e6`（默认）| 正实数标量

ADC 起始转换时钟的频率，指定为正实数标量，单位为 Hz。**起始转换频率 (Hz)** 必须与 ADC 模块的起始转换时钟频率匹配。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `1e6` |

**数据类型：** `double`

### **RMS 孔径抖动 (s)** — 由起始转换时钟添加的 RMS 孔径抖动 `40e-12`（默认）| 正实数标量

由起始转换时钟添加的 RMS 孔径抖动，指定为正实数标量，单位为秒。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RMSJitt` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `40e-12` |

**数据类型：** `double`

### **误差容限 (LSB)** — 模拟信号相邻采样之间的最大差值 `0.1`（默认）| 范围 (`0, 1`] 内的正标量

模拟输入信号相邻采样之间允许的最大幅度差，指定为以最低有效位 (LSB) 为单位的正实数标量。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `DC`。

**数据类型：** `double`

### **自动确定扫描范围** — 自动确定扫描范围 开（默认）| 关

选择此项可根据 ADC 动态输入范围和目标指标自动确定扫描范围。您可以取消选择此选项以指定自定义扫描范围。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `DC`。

### **扫描范围** — 自定义扫描范围 `[-1 1]`（默认）| 2 元素向量

定义自定义扫描范围，指定为 2 元素向量。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `DC`，并取消选择 **自动确定扫描范围** 参数。

**数据类型：** `double`

### **完成时停止仿真** — 完成时停止仿真 开（默认）| 关

选择此项可在完成时停止仿真。您可以取消选择此选项以提前终止仿真。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `DC`。

### 设置

### **自动填充设置参数** — 自动从 ADC 传播设置参数 按钮

点击以自动从 ADC 传播设置参数。

#### 依赖关系

此参数仅在 ADC 为 Mixed-Signal Blockset 中的 Flash ADC 或 SAR ADC 时有效。

### **位数** — 物理输出位数 `10`（默认）| 范围 `[1, 26]` 内的正实数整数

物理输出位数，指定为范围 `[1, 26]` 内的无单位正实数整数。**位数** 决定了 ADC 的分辨率。

#### 程序化使用

- 使用 `get_param(gcb,'NBits')` 查看当前 **位数**。
- 使用 `set_param(gcb,'NBits',value)` 将 **位数** 设置为特定值。

**数据类型：** `double`

### **输入范围 (V)** — ADC 动态范围 `[-1 1]`（默认）| 2 元素行向量

ADC 动态范围，指定为 2 元素行向量，单位为伏特。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputRange` |
| **类型：** 字符向量 |
| **值：** 2 元素行向量 |
| **默认值：** `[-1 1]` |

**数据类型：** `double`

### **保持时间 (s)** — 测量分析前的延迟 `0`（默认）| 非负实数标量

延迟测量分析以避免瞬态干扰，指定为非负实数标量，单位为秒。

#### 编程用法

|  |
| --- |
| **模块参数：** `HoldOffTime` |
| **类型：** 字符向量 |
| **值：** 非负实数标量 |
| **默认值：** `0` |

**数据类型：** `double`

### **在仿真期间显示频谱分析仪** — 在仿真期间显示频谱分析仪 off（默认）| on

在仿真期间显示频谱分析仪。默认情况下，此选项未选中。

#### 依赖关系

此参数仅在 **Measurement** 选项设置为 `AC` 时可用。

### **启用增大的缓冲区大小** — 启用增大的缓冲区大小 off（默认）| on

选择此项可在仿真期间启用增大的缓冲区大小。默认情况下，此选项未选中。

### **缓冲区大小** — 仿真期间可用的输入缓冲采样数 `5`（默认）| 正整数标量

仿真期间可用的输入缓冲采样数，指定为正整数标量。

选择不同的仿真求解器或采样策略可能会改变生成准确输出采样所需的输入采样数。将 **Buffer size** 设置为足够大的值，使输入缓冲区包含所有所需的输入采样。

#### 依赖关系

此参数仅在 **Configuration** 选项卡中选中 **Enable increased buffer size** 选项时可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `NBuffer` |
| **类型：** 字符向量 |
| **值：** 正整数标量 |
| **默认值：** `5` |

**数据类型：** `double`

### 目标指标

### **自动填充目标指标** — 从 ADC 自动传播目标指标 button

点击以从 ADC 自动传播目标指标。

#### 依赖关系

- 要启用此参数，请将 **Measurement** 选项设置为 `DC`。
- 此参数仅在 ADC 为 Mixed-Signal Blockset 中的 Flash ADC 或 SAR ADC 时有效。

### **失调误差** — 将量化步长偏移特定值 `1.5 LSB`（默认）| 实数标量

将量化步长偏移特定值，以 %FS、FS 或 LSB 为单位指定为正实数标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿传输曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5 LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = Full scale range of converter2NBits。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `DC`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TargetOffsetError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认值：** `1.5 LSB` |

**数据类型：** `double`

### **增益误差** — ADC 传输曲线斜率上的误差 `1 LSB`（默认）| 实数标量

对 ADC 传输曲线进行直线插值时的斜率误差，以最低有效位 %FS、FS 或 LSB 为单位指定为正实数标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿传输曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5 LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = Full scale range of converter2NBits。

#### 依赖关系

要启用此参数，请将 **Measurement** 选项设置为 `DC`。

#### 编程用法

|  |
| --- |
| **模块参数：** `TargetGainError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认值：** `1 LSB` |

**数据类型：** `double`

## 所属库

Mixed-Signal Blockset / ADC / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

测量 ADC 输出的直流和交流性能指标

ADC Testbench 模块可测量直流和交流性能指标。直流性能指标包括失调误差和增益误差。交流性能指标包括信噪比（SNR）、信纳比（SINAD）、无杂散动态范围（SFDR）、有效位数（ENOB）、噪声底和转换延迟。

ADC Testbench 模块从 **Stimulus** 选项卡生成激励以驱动被测设备（DUT）。用于验证 DUT 的设置参数在 **Setup** 选项卡中定义，目标验证指标在 **Target Metric** 选项卡中定义。

您可以使用 ADC Testbench 模块验证 Mixed-Signal Blockset™ 中提供的 ADC 架构模型，也可以验证您自己实现的 ADC。
