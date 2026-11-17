---
type: simulink-block
title: 'DAC Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'DAC / Measurements & Testbenches'
documentation_page: 'dactestbench'
documentation_source_path: 'ref/dactestbench.html'
language: zh-CN
chinese_source: worker-translation
---

# DAC Testbench

## 端口

### 输入

### **from dac analog** — 来自 DAC 输出的模拟信号 标量

来自 DAC 输出的模拟输入信号，指定为标量。

**数据类型：** `double`
### 输出

### **to dac digital** — 用于 DAC 输入的数字激励信号 标量

用于 DAC 输入的数字输出激励信号，以标量形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **to dac start** — 用于 DAC 的外部启动转换时钟 标量

用于 DAC 的外部启动转换时钟，以标量形式返回。该信号的上升沿启动 DAC 模块中的转换过程。

**数据类型：** `double`

## 参数

### **Measurement** — 选择测量直流还是交流性能指标 `DC`（默认）| `AC`

选择测量静态（DC）还是动态（AC）性能指标：

- 选择 `DC` 以测量失调误差和增益误差。
- 选择 `AC` 以测量 SNR、SINAD、SFDR、ENOB 和噪声底。

### **Recommended min. simulation stop time (s)** — 仿真必须运行以获得有意义结果的最短时间 `2.048e-02`（默认）| 正实数标量

仿真必须运行以获得有意义结果的最短时间，以秒为单位指定为正实数标量。

- 要测量 DC 性能，仿真必须运行到 DAC 能够对每个数字码采样 20 次。基于此假设，**Recommended min.
  simulation stop time (s)**
  *T* 由下式给出：

  T=Samples per bit(StartFreq/2Nbits+1)+Hold off time，

  其中 *StartFreq* 是转换启动时钟的频率，*Nbits* 是 DAC 的分辨率。

  每比特采样数使用以下公式计算：

  Samples per bit = max(1Error tolerance,10)。
- 要测量 AC 性能，仿真必须运行到 DAC 能够生成 DAC 输出的六次频谱更新。因此，**Recommended min.
  simulation stop time (s)**
  *T* 由下式给出 [1]：

  T=6(1.5RBW+Hold off time)，

  其中 *RBW* 是 DAC Testbench 模块内部频谱估计器的分辨率带宽，由以下公式给出：RBW=[min(Input frequency)0.1]。

该参数仅由测试平台报告，不可编辑。

**数据类型：** `double`

### **Set as model stop time** — 自动将推荐的仿真最短停止时间设置为模型停止时间 按钮

点击以自动将 **Recommended min. simulation stop time
(s)** 设置为 Simulink® 模型的停止时间。

### **Endpoint** — 使用端点法测量 DNL、INL on（默认）| off

使用端点法测量微分非线性（DNL）误差和积分非线性（INL）误差。该方法使用实际传递函数的端点来测量 DNL 和 INL 误差。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为
`DC`。

### **Best fit** — 使用最佳拟合法测量 DNL、INL on（默认）| off

使用最佳拟合法测量微分非线性（DNL）误差和积分非线性（INL）误差。该方法使用标准曲线拟合技术来找到最佳拟合以测量 DNL 和 INL 误差。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为
`DC`。

### **Plot DC analysis result** — 绘制 DC 分析结果 按钮

点击以绘制 DC 分析结果以供进一步分析。要执行包括积分非线性（INL）和微分非线性（DNL）在内的完整 DC 分析，请使用 DAC DC
Measurement 模块。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为
`DC`。

### **Export measurement result** — 将详细测试结果存储到基础工作区 按钮

点击以将详细测试结果存储到电子表格（XLS 文件）或逗号分隔值（CSV 文件）中以供进一步处理。

### Stimulus

### **Digital input frequency (Hz)** — 数字输入信号频率 `1e4`（默认）| 正实数标量

DAC 模块数字输入信号的频率，指定为以赫兹为单位的正实数标量。**Digital input frequency (Hz)** 必须与待测 DAC 设备的输入频率匹配。

**Digital input frequency (Hz)** 需要满足两个要求：

- DAC 的所有输出码必须被激活。
- **Digital input frequency (Hz)** 与 **Start conversion frequency (Hz)** 之间除 1 外不得有任何公倍数。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `AC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputFrequency` |
| **类型**：character vector |
| **值**：positive real scalar |
| **默认值**：`1e3` |

**Data Types:** `double`

### **Start conversion frequency (Hz)** — 内部启动转换时钟频率 `1e6`（默认）| 正实数标量

内部启动转换时钟的频率，指定为以 Hz 为单位的正实数标量。**Start conversion frequency (Hz)** 决定 DAC 的速率。

#### 编程使用

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型**：character vector |
| **值**：positive real scalar |
| **默认值**：`1e6` |

**Data Types:** `double`

### **Error tolerance (LSB)** — 数字信号连续采样之间的最大差值 `0.1`（默认）| 范围 (`0, 1`] 内的正标量

数字输入信号连续采样之间允许的最大幅度差，指定为以最低有效位（LSB）为单位的正实数标量。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `ErrorTolerance` |
| **类型**：character vector |
| **值**：positive scalar in the range (`0, 1`] |
| **默认值**：`0.1` |

**Data Types:** `double`

### Setup

### **Autofill setup parameters** — 自动传播 DAC 的设置参数 button

点击以自动传播 DAC 的设置参数。

#### 依赖关系

DAC 必须是 Mixed-Signal Blockset 中的 Binary Weighted DAC。

### **Number of bits** — 输入字中的位数 `10`（默认）| 正实数整数

输入字中的位数，指定为无单位的正实数整数。**Number of bits** 决定 DAC 的分辨率。

#### 编程使用

|  |
| --- |
| **模块参数：** `NBits` |
| **类型**：character vector |
| **值**：positive real integer |
| **默认值**：`10` |

**Data Types:** `double`

### **Input polarity** — DAC 输入信号的极性 `Bipolar`（默认）| `Unipolar`

DAC 输入信号的极性。

#### 编程使用

|  |
| --- |
| **模块参数：** `Polarity` |
| **类型**：character vector |
| **值**：`Bipolar`|`Unipolar` |
| **默认值**：`Bipolar` |

### **Reference (V)** — 参考电压 `1`（默认）| 实数标量

DAC 的参考电压，指定为以伏特为单位的实数标量。**Reference (V)** 有助于根据输入数字码、**Number of bits** 和 **Bias (V)** 使用以下方程确定输出：

DAC 输出 = ((数字输入码2位数)参考)+偏置。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Ref` |
| **类型**：character vector |
| **值**：real scalar |
| **默认值**：`1` |

**Data Types:** `double`

### **Bias (V)** — 添加到输出的偏置电压 `0`（默认）| 实数标量

添加到 DAC 输出的偏置电压，指定为以伏特为单位的实数标量。**Bias (V)** 有助于根据输入数字码、**Number of bits** 和 **Reference (V)** 使用以下方程确定输出：

DAC 输出 = ((数字输入码2位数)参考)+偏置

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Bias` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认值：** `0` |

**数据类型：** `double`

### **建立时间 (s)** — 输出建立所需的时间 `0.25/1e-6`（默认）| 非负实数标量

DAC 输出建立到其最终值的某一比例范围内所需的时间，指定为非负实数标量，单位为秒。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为
`DC`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTime` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认值：** `0.25/1e-6` |

**数据类型：** `double`

### **建立时间容差 (LSB)** — 计算建立时间的容差 `0.5`（默认）| 正实数标量

计算建立时间时允许的容差，指定为正实数标量，单位为 LSB。DAC 的输出必须在 **建立时间 (s)** 内建立到 **建立时间容差 (LSB)** 范围内。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为
`AC`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SettlingTimeTolerance` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认值：** `0.5` |

**数据类型：** `double`

### **保持关断时间 (s)** — 测量分析前的延迟 `0`（默认）| 非负实数标量

测量分析前的延迟，以避免瞬态过程的干扰，指定为非负实数标量，单位为秒。

#### 程序化使用

- 使用 `get_param(gcb,'HoldOffTime')` 查看 **保持关断时间 (s)** 的当前值。
- 使用 `set_param(gcb,'HoldOffTime',value)` 将 **保持关断时间 (s)** 设置为特定值。

**数据类型：** `double`

### **在仿真期间显示频谱分析仪** — 在仿真期间显示频谱分析仪 关（默认）| 开

选择此参数可在仿真期间显示频谱分析仪窗口。默认情况下，此参数未选中。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为
`AC`。

### 目标指标

### **自动填充目标指标** — 从 DAC 自动传播目标指标 按钮

点击以从 DAC 自动传播目标指标。

#### 依赖关系

- 要启用此参数，请将 **Measurement** 设置为
  `DC`。
- DAC 必须是来自 Mixed-Signal Blockset 的 Binary
  Weighted DAC。

### **失调误差** — 将量化步长偏移特定值 `0 LSB`（默认）| 实数标量

将量化步长偏移特定值，指定为实数标量，单位为 %FS（满量程百分比）、FS（满量程）或 LSB（最低有效位）。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传输曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿传输曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5 LSB。输入值必须在转换器的满量程范围内考虑。

**注意**

LSB 由以下公式计算：LSB = 转换器满量程范围2NBits。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为
`DC`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TargetOffsetError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认值：** `0 LSB` |

**数据类型：** `double`

### **增益误差** — DAC 转换曲线斜率误差 `0 LSB`（默认）| 实数标量

对 DAC 转换曲线进行直线插值时的斜率误差，指定为以 %FS（满量程百分比）、FS（满量程）或 LSB（最低有效位）表示的实数标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿转换曲线上最后一个码与第一个码之间的差值。在 +0.5 LSB 补偿转换曲线中，第一个码宽度为 0.5 LSB，而最后一个码宽度为 1.5 LSB。输入值必须考虑在转换器的满量程范围内。

**注意**

LSB 由以下公式计算：LSB = 转换器满量程范围2NBits。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 编程用法

#### 编程用法

|  |
| --- |
| **模块参数：** `TargetGainError` |
| **类型：** 字符向量 |
| **值：** 实数标量 |
| **默认：** `0 LSB` |

**数据类型：** `double`

## 所属库

Mixed-Signal Blockset / DAC / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

测量 DAC 输出的直流和交流性能指标

DAC Testbench 模块测量 DAC（数字到模拟转换器）的直流和交流性能指标。直流性能指标包括失调误差和增益误差。交流性能指标包括信噪比 (SNR)、信纳比 (SINAD)、无杂散动态范围 (SFDR)、有效位数 (ENOB) 和噪声底。

DAC Testbench 模块从 **Stimulus** 选项卡生成用于驱动被测设备 (DUT) 的激励。用于验证 DUT 的设置参数在 **Setup** 选项卡中定义。目标验证指标在 **Target Metric** 选项卡中定义。

您可以使用 DAC Testbench 模块验证 Mixed-Signal Blockset™ 中提供的 DAC 架构模型，也可以验证您自己实现的 DAC。
