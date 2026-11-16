---
type: simulink-block
title: 'DAC Testbench'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Measurements and Testbenches / DAC'
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

用于 DAC 输入的数字输出激励信号，返回为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **to dac start** — DAC 的外部启动转换时钟 标量

DAC 的外部启动转换时钟，返回为标量。此信号的上升沿启动 DAC 模块中的转换过程。

**数据类型：** `double`

## 参数

### **Measurement** — 选择测量 DC 还是 AC 性能指标 `DC`（默认）| `AC`

选择测量静态（DC）还是动态（AC）性能指标：

- 选择 `DC` 以测量失调误差和增益误差。
- 选择 `AC` 以测量 SNR、SINAD、SFDR、ENOB 和噪声底。

### **Recommended min. simulation stop time (s)** — 仿真必须运行以获得有意义结果的最短时间 `2.048e-02`（默认）| 正实数标量

仿真必须运行以获得有意义结果的最短时间，指定为以秒为单位的正实数标量。

- 要测量 DC 性能，仿真必须运行到 DAC 能对每个数字码采样 20 次。基于此假设，**Recommended min. simulation stop time (s)** *T* 由下式给出：

  T = Samples per bit (StartFreq / 2^Nbits + 1) + Hold off time,

  其中 *StartFreq* 是转换启动时钟的频率，*Nbits* 是 DAC 的分辨率。

  每比特采样数由以下方程计算：

  Samples per bit = max(1 / Error tolerance, 10).
- 要测量 AC 性能，仿真必须运行到 DAC 能生成 DAC 输出的六次频谱更新。因此，**Recommended min. simulation stop time (s)** *T* 由下式给出 [1]：

  T = 6 (1.5 RBW + Hold off time),

  其中 *RBW* 是 DAC Testbench 模块内部频谱估计器的分辨率带宽，由以下方程给出：RBW = [min(Input frequency) / 0.1]。

此参数仅由测试平台报告，不可编辑。

**数据类型：** `double`

### **Set as model stop time** — 自动将推荐的最小仿真停止时间设置为模型停止时间 按钮

点击以自动将 **Recommended min. simulation stop time (s)** 设置为 Simulink® 模型的停止时间。

### **Endpoint** — 使用端点方法测量 DNL、INL on（默认）| off

使用端点方法测量微分非线性（DNL）误差和积分非线性（INL）误差。此方法使用实际传递函数的端点来测量 DNL 和 INL 误差。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

### **Best fit** — 使用最佳拟合方法测量 DNL、INL on（默认）| off

使用最佳拟合方法测量微分非线性（DNL）误差和积分非线性（INL）误差。此方法使用标准曲线拟合技术来找到最佳拟合，以测量 DNL 和 INL 误差。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

### **Plot DC analysis result** — 绘制 DC 分析结果 按钮

点击以绘制 DC 分析结果以供进一步分析。要执行包括积分非线性（INL）和微分非线性（DNL）在内的完整 DC 分析，请使用 DAC DC Measurement 模块。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

### **Export measurement result** — 将详细测试结果存储到基础工作区 按钮

点击以将详细测试结果存储到电子表格（XLS 文件）或逗号分隔值（CSV 文件）中，以供进一步处理。

### 激励

### **Digital input frequency (Hz)** — DAC 数字输入信号的频率 `1e4`（默认）| 正实数标量

DAC 模块的数字输入信号的频率，指定为以赫兹为单位的正实数标量。**Digital input frequency (Hz)** 必须与 DAC 被测设备的输入频率匹配。

**Digital input frequency (Hz)** 需要满足两个要求：

- 必须激活 DAC 的所有输出码。
- **Digital input frequency (Hz)** 不得与 **Start conversion frequency (Hz)** 共享除 1 以外的任何公倍数。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `AC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputFrequency` |
| **类型：** character vector |
| **取值：** positive real scalar |
| **默认：** `1e3` |

**数据类型：** `double`

### **Start conversion frequency (Hz)** — 内部启动转换时钟的频率 `1e6`（默认）| 正实数标量

内部启动转换时钟的频率，指定为以 Hz 为单位的正实数标量。**Start conversion frequency (Hz)** 决定 DAC 的速率。

#### 编程使用

|  |
| --- |
| **模块参数：** `StartFreq` |
| **类型：** character vector |
| **取值：** positive real scalar |
| **默认：** `1e6` |

**数据类型：** `double`

### **Error tolerance (LSB)** — 数字信号连续样本之间的最大差值 `0.1`（默认）| 范围 (`0, 1`] 内的正标量

数字输入信号连续样本的幅度允许的最大差值，指定为以最低有效位（LSB）为单位的正实数标量。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `ErrorTolerance` |
| **类型：** character vector |
| **取值：** 范围 (`0, 1`] 内的正标量 |
| **默认：** `0.1` |

**数据类型：** `double`

### 设置

### **Autofill setup parameters** — 自动传播来自 DAC 的设置参数 按钮

点击以自动传播来自 DAC 的设置参数。

#### 依赖关系

DAC 必须是 Mixed-Signal Blockset 中的 Binary Weighted DAC。

### **Number of bits** — 输入字中的位数 `10`（默认）| 正实数整数

输入字中的位数，指定为无单位的正实数整数。**Number of bits** 决定 DAC 的分辨率。

#### 编程使用

|  |
| --- |
| **模块参数：** `NBits` |
| **类型：** character vector |
| **取值：** positive real integer |
| **默认：** `10` |

**数据类型：** `double`

### **Input polarity** — DAC 输入信号的极性 `Bipolar`（默认）| `Unipolar`

DAC 输入信号的极性。

#### 编程使用

|  |
| --- |
| **模块参数：** `Polarity` |
| **类型：** character vector |
| **取值：** `Bipolar`|`Unipolar` |
| **默认：** `Bipolar` |

### **Reference (V)** — 参考电压 `1`（默认）| 实数标量

DAC 的参考电压，指定为以伏特为单位的实数标量。**Reference (V)** 帮助根据输入数字码、**Number of bits** 和 **Bias (V)** 使用以下方程确定输出：

DAC output = ((Digital input code / 2^Number of bits) * Reference) + Bias.

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Ref` |
| **类型：** character vector |
| **取值：** real scalar |
| **默认：** `1` |

**数据类型：** `double`

### **Bias (V)** — 添加到输出的偏置电压 `0`（默认）| 实数标量

添加到 DAC 输出的偏置电压，指定为以伏特为单位的实数标量。**Bias (V)** 帮助根据输入数字码、**Number of bits** 和 **Reference (V)** 使用以下方程确定输出：

DAC output = ((Digital input code / 2^Number of bits) * Reference) + Bias

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Bias` |
| **类型：** character vector |
| **取值：** real scalar |
| **默认：** `0` |

**数据类型：** `double`

### **Settling time (s)** — 输出稳定所需的时间 `0.25/1e-6`（默认）| 非负实数标量

DAC 输出稳定到其最终值的某一分数所需的时间，指定为以秒为单位的非负实数标量。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SettlingTime` |
| **类型：** character vector |
| **取值：** real scalar |
| **默认：** `0.25/1e-6` |

**数据类型：** `double`

### **Settling time tolerance (LSB)** — 计算稳定时间的容差 `0.5`（默认）| 正实数标量

计算稳定时间时允许的容差，指定为以 LSB 为单位的正实数标量。DAC 的输出必须在 **Settling time (s)** 之前稳定到 **Settling time tolerance (LSB)** 以内。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `AC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `SettlingTimeTolerance` |
| **类型：** character vector |
| **取值：** positive real scalar |
| **默认：** `0.5` |

**数据类型：** `double`

### **Hold off time (s)** — 测量分析前的延迟 `0`（默认）| 非负实数标量

测量分析前的延迟，以避免瞬态损坏，指定为以秒为单位的非负实数标量。

#### 编程使用

- 使用 `get_param(gcb,'HoldOffTime')` 查看 **Hold off time (s)** 的当前值。
- 使用 `set_param(gcb,'HoldOffTime',value)` 将 **Hold off time (s)** 设置为特定值。

**数据类型：** `double`

### **Show spectrum analyzer during simulation** — 在仿真期间显示频谱分析仪 off（默认）| on

选择此参数以在仿真期间显示 Spectrum Analyzer 窗口。默认情况下，此参数未选中。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `AC`。

### 目标指标

### **Autofill target metric** — 自动传播来自 DAC 的目标指标 按钮

点击以自动传播来自 DAC 的目标指标。

#### 依赖关系

- 要启用此参数，请将 **Measurement** 设置为 `DC`。
- DAC 必须是 Mixed-Signal Blockset 中的 Binary Weighted DAC。

### **Offset error** — 将量化步长偏移特定值 `0 LSB`（默认）| 实数标量

将量化步长偏移特定值，指定为以 %FS（满量程百分比）、FS（满量程）或 LSB（最低有效位）为单位的实数标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传递曲线上最后一个码与第一个码之间的差。在 +0.5 LSB 补偿传递曲线中，第一个码宽为 0.5 LSB，而最后一个码宽为 1.5 LSB。输入值必须被视为在转换器的满量程范围内。

**注意**

LSB 由以下方程计算：LSB = Full scale range of converter / 2^NBits。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 编程使用

|  |
| --- |
| **模块参数：** `TargetOffsetError` |
| **类型：** character vector |
| **取值：** real scalar |
| **默认：** `0 LSB` |

**数据类型：** `double`

### **Gain error** — DAC 传递曲线斜率的误差 `0 LSB`（默认）| 实数标量

插值 DAC 传递曲线的直线斜率的误差，指定为以 %FS（满量程百分比）、FS（满量程）或 LSB（最低有效位）为单位的实数标量。

**注意**

转换器的满量程范围定义为 +0.5 LSB 补偿传递曲线上最后一个码与第一个码之间的差。在 +0.5 LSB 补偿传递曲线中，第一个码宽为 0.5 LSB，而最后一个码宽为 1.5 LSB。输入值必须被视为在转换器的满量程范围内。

**注意**

LSB 由以下方程计算：LSB = Full scale range of converter / 2^NBits。

#### 依赖关系

要启用此参数，请将 **Measurement** 设置为 `DC`。

#### 编程使用

#### 编程使用

|  |
| --- |
| **模块参数：** `TargetGainError` |
| **类型：** character vector |
| **取值：** real scalar |
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

测量 DAC 输出的 DC 和 AC 性能指标

DAC Testbench 模块测量 DAC（数字到模拟转换器）的 DC 和 AC 性能指标。DC 性能指标包括失调误差和增益误差。AC 性能指标包括信噪比（SNR）、信噪失真比（SINAD）、无杂散动态范围（SFDR）、有效位数（ENOB）和噪声底。

DAC Testbench 模块从 **激励** 选项卡生成激励以驱动被测设备（DUT）。用于验证 DUT 的设置参数在 **设置** 选项卡上定义。目标验证指标在 **目标指标** 选项卡上定义。

您可以使用 DAC Testbench 模块验证 Mixed-Signal Blockset™ 中提供的 DAC 架构模型，也可以验证您自己实现的 DAC。
