---
type: simulink-block
title: 'ADC AC Measurement'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'ADC / Measurements & Testbenches'
documentation_page: 'adcacmeasurement'
documentation_source_path: 'ref/adcacmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# ADC AC Measurement

## 端口

### 输入

### **digital** — 来自 ADC 的转换后数字信号（标量）

来自 ADC 的转换后数字信号，指定为标量。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ready** — 指示模数转换是否完成（标量）

指示模数转换是否完成，指定为标量。

**数据类型：** `double`

### **start** — 外部转换启动时钟（标量）

外部转换启动时钟，指定为标量。模数转换过程在 **start** 端口处信号的上升沿开始。

**数据类型：** `double`

## 参数

### **失真测量类型** — 要测量的失真类型 `Harmonic`（默认）| `Intermodulation`

ADC AC Measurement 模块设置为测量的失真类型，指定为 `Harmonic` 或 `Intermodulation`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DistortionMeasurement` |
| **类型：** character vector |
| **值：** `Harmonic` | `Intermodulation` |
| **默认值：** `Harmonic` |

### **模拟激励频率 (Hz)** — ADC 模拟输入信号的频率 正实数标量 | 正实数向量

ADC 模块的模拟输入信号频率，指定为以赫兹为单位的正实数标量或正实数向量。**模拟激励频率** 必须与被测 ADC 器件的输入频率匹配。

- 当 ADC AC Measurement 设置为测量 `Harmonic` 失真时，**模拟激励频率** 的默认值为 `10000`。
- 当 ADC AC Measurement 设置为测量 `Intermodulation` 失真时，**模拟激励频率** 的默认值为 `[9000,11000]`。

**模拟激励频率** 除 1 外不得与 **启动转换频率** 有任何其他公共倍数。

为满足此条件，请使用方程 fanalog=JMfstart，

其中：

*f*analog 是模拟信号频率，

*f*start 是启动转换频率，

*J* 是每个 FFT 窗口的激励周期数，

并且 *M* 是 FFT 点数。

**注意**

*J* 选为小于 FFT 点数的十分之一的最大质数。*M* 的最小值允许为 16。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputFrequency` |
| **类型：** character vector |
| **值：** 正实数标量 | 正实数向量 |
| **默认值：** `10000` |

### **频谱估计方法** — 频谱估计方法 **Welch**（默认）| **Filter bank**

选择频谱估计方法为以下之一：

- **Filter bank** — 使用分析滤波器组估计功率谱。与 Welch 方法相比，此方法具有更低的本底噪声、更好的频率分辨率、更低的频谱泄漏，并且每次更新所需的样本更少。有关详细信息，请参阅频谱估计 — 滤波器组
- **Welch** — 使用 Welch 的平均修正周期图方法。有关详细信息，请参阅频谱估计 — Welch 方法

#### 编程用法

|  |
| --- |
| **模块参数：** `Method` |
| **类型：** character vector |
| **值：** **Filter bank** | **Welch** |
| **默认值：** **Filter bank** |

### **分辨率带宽 (Hz)** — 分辨率带宽 正实数标量

分辨率带宽，指定为以赫兹为单位的正实数标量。此参数定义可分辨的最小正频率。默认情况下，此参数会自动计算。您可以取消选择 **自动设置** 来自定义该值。

#### 编程用法

|  |
| --- |
| **模块参数：** `RBW` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `976.5625` |

### **启动转换频率 (Hz)** — ADC 启动转换时钟的频率 `1e6`（默认）| 正实数标量

ADC 启动转换时钟的频率，指定为以赫兹为单位的正实数标量。**启动转换频率** 必须与 ADC 模块的启动转换时钟频率匹配。

#### 编程用法

|  |
| --- |
| **模块参数：** `Frequency` |
| **类型：** character vector |
| **值：** 正实数标量 |
| **默认值：** `1e6` |

### **保持关断时间 (s)** — 延迟测量分析以避免瞬态造成的数据损坏 `0`（默认）| 非负实数标量

延迟测量分析以避免瞬态造成的数据损坏，指定为以秒为单位的非负实数标量。

#### 编程用法

|  |
| --- |
| **模块参数：** `HoldOffTime` |
| **类型：** character vector |
| **值：** 非负实数标量 |
| **默认值：** `0` |

### **建议的最小仿真停止时间 (s)** — 仿真必须运行以获得有意义结果的最短时间 正实数标量

仿真必须运行以获得有意义结果的最短时间，指定为以秒为单位的正实数标量。

对于 AC 测量，仿真必须运行到 ADC 可以生成 6 次 ADC 输出的频谱更新。基于 Welch 方法生成一次频谱输出所需的时间由下式给出：

t=1.5·SamplingFrequencyRBW

其中 *SamplingFrequency* 和 *RBW* 分别是 ADC Testbench 模块内频谱估计器的采样频率和分辨率带宽。

此参数仅由测试台报告，且不可编辑。

**数据类型：** `double`

### **设为模型停止时间** — 自动将建议的最小仿真停止时间设置为模型停止时间 按钮

单击以自动将 **建议的最小仿真停止时间 (s)** 设置为 Simulink® 模型的停止时间。

### **将结果输出到基础工作区** — 将详细测试结果存储到基础工作区 off（默认）| on

在仿真结束时将详细测试结果存储到基础工作区以供进一步处理。默认情况下，不选择此选项。

### **工作区变量名称** — 存储详细测试结果的变量名称 `adc_ac_out`（默认）| character string

存储详细测试结果的变量名称，指定为 character string。

#### 依赖关系

仅当选择 **将结果输出到基础工作区** 时，此参数才可用。

#### 编程用法

|  |
| --- |
| **模块参数：** `VariableName` |
| **类型：** character vector |
| **值：** character string |
| **默认值：** `adc_ac_out` |

### **在仿真期间显示频谱分析仪** — 在仿真期间显示频谱分析仪 off（默认）| on

在仿真期间显示频谱分析仪。默认情况下，不选择此选项。

## 所属库

Mixed-Signal Blockset / ADC / Measurements & Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

测量 ADC 输出的 AC 性能指标

ADC AC Measurement 模块测量 ADC AC 性能指标，例如信噪比 (SNR)、信噪失真比 (SINAD)、无杂散动态范围 (SFDR)、有效位数 (ENOB)、本底噪声和转换延迟。您可以使用 ADC AC Measurement 模块验证 Mixed-Signal Blockset™ 中提供的 ADC 架构模型，也可以使用自己实现的 ADC。
