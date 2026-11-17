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
```yaml
ports:
- name: digital
  summary: 来自 ADC 的转换后数字信号 标量
  direction: input
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: ready
  summary: 指示模数转换是否完成 标量
  direction: input
  data_types: double
- name: start
  summary: 外部转换启动时钟 标量
  direction: input
  data_types: double
```

### 输入

### **digital** — 来自 ADC 的转换后数字信号 标量

来自 ADC 的转换后数字信号，指定为标量。

**数据类型：** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ready** — 指示模数转换是否完成 标量

指示模数转换是否完成，指定为标量。

**数据类型：** `double`

### **start** — 外部转换启动时钟 标量

外部转换启动时钟，指定为标量。模数转换过程在 **start** 端口信号的上升沿启动。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Distortion measurement type
  summary: 要测量的失真类型 Harmonic（默认）| Intermodulation
  group: ''
  block_parameter: DistortionMeasurement
  type: 字符向量
  values: Harmonic | Intermodulation
- name: Analog stimulus frequency (Hz)
  summary: ADC 模拟输入信号的频率 正实数标量 | 正实数值向量
  group: ''
  block_parameter: InputFrequency
  type: 字符向量
  values: 正实数标量 | 正实数值向量
- name: Spectrum estimation method
  summary: 频谱估计方法 Welch（默认）| Filter bank
  group: ''
  block_parameter: Method
  type: 字符向量
  values: Filter bank | Welch
- name: Resolution bandwidth (Hz)
  summary: 分辨率带宽 正实数标量
  group: ''
  block_parameter: RBW
  type: 字符向量
  values: 正实数标量
- name: Start conversion frequency (Hz)
  summary: ADC 启动转换时钟频率 1e6（默认）| 正实数标量
  group: ''
  block_parameter: Frequency
  type: character vector
  values: positive real scalar
  default: 1e6
- name: Hold off time (s)
  summary: 延迟测量分析以避免瞬态干扰 0（默认）| 非负实数标量
  group: ''
  block_parameter: HoldOffTime
  type: character vector
  values: nonnegative real scalar
  default: '0'
- name: Recommended min. simulation stop time (s)
  summary: 仿真获得有意义结果所需的最短运行时间 正实数标量
  group: ''
- name: Set as model stop time
  summary: 自动将推荐的最小仿真停止时间设置为模型停止时间 按钮
  group: ''
- name: Output result to base workspace
  summary: 将详细测试结果存储到基础工作区 off（默认）| on
  group: ''
- name: Workspace variable name
  summary: 存储详细测试结果的变量名称 adc_ac_out（默认）| 字符串
  group: ''
  block_parameter: VariableName
  type: character vector
  values: character string
  default: adc_ac_out
- name: Show spectrum analyzer during simulation
  summary: 在仿真期间显示频谱分析仪 off（默认）| on
  group: ''
```

### **Distortion measurement type** — 要测量的失真类型 `Harmonic`（默认）| `Intermodulation`

ADC AC Measurement 模块设置为测量的失真类型，指定为 `Harmonic` 或 `Intermodulation`。

#### 编程使用

|  |
| --- |
| **模块参数：** `DistortionMeasurement` |
| **类型：** 字符向量 |
| **值：** `Harmonic` | `Intermodulation` |
| **默认：** `Harmonic` |

### **Analog stimulus frequency (Hz)** — ADC 模拟输入信号的频率 正实数标量 | 正实数值向量

ADC 模块的模拟输入信号频率，指定为以赫兹为单位的正实数标量或正实数值向量。**Analog stimulus frequency** 必须与被测 ADC 设备的输入频率匹配。

- 当 ADC AC Measurement 设置为测量 `Harmonic` 失真时，**Analog stimulus frequency** 的默认值为 `10000`。
- 当 ADC AC Measurement 设置为测量 `Intermodulation` 失真时，**Analog stimulus frequency** 的默认值为 `[9000,11000]`。

**Analog stimulus frequency** 与 **Start conversion frequency** 之间除 1 外不得有任何公倍数。

为满足此条件，请使用公式 fanalog=JMfstart，

其中：

*f*analog 是模拟信号频率，

*f*start 是启动转换频率，

*J* 是每个 FFT 窗口内激励的周期数，

*M* 是 FFT 点数。

**注意**

*J* 选取为小于 FFT 点数十分之一的最大素数。*M* 的最小值允许为 16。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputFrequency` |
| **类型：** 字符向量 |
| **值：** 正实数标量 | 正实数值向量 |
| **默认：** `10000` |

### **Spectrum estimation method** — 频谱估计方法 **Welch**（默认）| **Filter bank**

选择频谱估计方法为以下之一：

- **Filter bank** — 使用分析滤波器组估计功率谱。与 Welch 方法相比，此方法具有更低的噪声底、更好的频率分辨率、更低的频谱泄漏，并且每次更新所需的样本更少。有关详细信息，请参阅 Spectrum Estimation — Filter Bank
- **Welch** — 使用 Welch 的平均修正周期图方法。有关详细信息，请参阅 Spectrum Estimation — Welch's Method

#### 编程使用

|  |
| --- |
| **模块参数：** `Method` |
| **类型：** 字符向量 |
| **值：** **Filter bank** | **Welch** |
| **默认：** **Filter bank** |

### **Resolution bandwidth (Hz)** — 分辨率带宽 正实数标量

分辨率带宽，指定为以赫兹为单位的正实数标量。此参数定义可分辨的最小正频率。默认情况下，此参数自动计算。您可以取消选择 **Set automatically** 来自定义该值。

#### 编程使用

|  |
| --- |
| **模块参数：** `RBW` |
| **类型：** 字符向量 |
| **值：** 正实数标量 |
| **默认：** `976.5625` |

### **Start conversion frequency (Hz)** — ADC 启动转换时钟频率 `1e6`（默认）| 正实数标量

ADC 启动转换时钟的频率，指定为以赫兹为单位的正实数标量。**Start conversion frequency** 必须与 ADC 模块的启动转换时钟频率匹配。

#### 编程使用

|  |
| --- |
| **模块参数：** `Frequency` |
| **类型**：character vector |
| **值**：positive real scalar |
| **默认值**：`1e6` |

### **Hold off time (s)** — 延迟测量分析以避免瞬态干扰 `0`（默认）| 非负实数标量

延迟测量分析以避免瞬态干扰，指定为以秒为单位的非负实数标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `HoldOffTime` |
| **类型**：character vector |
| **值**：nonnegative real scalar |
| **默认值**：`0` |

### **Recommended min. simulation stop time (s)** — 仿真获得有意义结果所需的最短运行时间 正实数标量

仿真必须运行以获得有意义结果的最短时间，指定为以秒为单位的正实数标量。

对于 AC 测量，仿真必须运行到 ADC 能够生成 6 次 ADC 输出的频谱更新。基于 Welch 方法生成一次频谱输出所需的时间由下式给出：

t=1.5·SamplingFrequencyRBW

其中 *SamplingFrequency* 和 *RBW* 分别是 ADC Testbench 模块内部频谱估计器的采样频率和分辨率带宽。

此参数仅由测试平台报告，不可编辑。

**Data Types:** `double`

### **Set as model stop time** — 自动将推荐的最小仿真停止时间设置为模型停止时间 按钮

点击以自动将 **Recommended min. simulation stop time (s)** 设置为 Simulink® 模型的停止时间。

### **Output result to base workspace** — 将详细测试结果存储到基础工作区 off（默认）| on

在仿真结束时将详细测试结果存储到基础工作区以供进一步处理。默认情况下，此选项未选中。

### **Workspace variable name** — 存储详细测试结果的变量名称 `adc_ac_out`（默认）| 字符串

存储详细测试结果的变量名称，指定为字符串。

#### 依赖关系

此参数仅在选中 **Output result to base workspace** 时可用。

#### 编程使用

|  |
| --- |
| **模块参数：** `VariableName` |
| **类型**：character vector |
| **值**：character string |
| **默认值**：`adc_ac_out` |

### **Show spectrum analyzer during simulation** — 在仿真期间显示频谱分析仪 off（默认）| on

在仿真期间显示频谱分析仪。默认情况下，此选项未选中。
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

ADC AC Measurement 模块测量 ADC 的 AC 性能指标，例如信噪比（SNR）、信噪失真比（SINAD）、无杂散动态范围（SFDR）、有效位数（ENOB）、噪声底和转换延迟。您可以使用 ADC AC Measurement 模块验证 Mixed-Signal Blockset™ 中提供的 ADC 架构模型，也可以使用您自己实现的 ADC。
