---
type: simulink-block
title: 'Nonlinear FM Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveforms'
documentation_page: 'nonlinearfmwaveform'
documentation_source_path: 'ref/nonlinearfmwaveform.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear FM Waveform

## 端口

### 输入

### **PRFIdx** — PRF 索引 正整数

用于选择脉冲重复频率 (PRF) 的索引，指定为正整数。该索引从 **脉冲重复频率 (Hz)** 参数指定的预定义值向量中选择 PRF。

**示例:**
`4`

#### 依赖项

要启用此端口，请选择 **启用 PRF 选择输入**。

**数据类型:** `double`

### **FreqOffset** — 频率偏移 标量

频率偏移，单位为 Hz，指定为标量。

**示例:**
`2e3`

#### 依赖项

要启用此端口，请将 **频率偏移来源** 设置为 `Input port`。

**数据类型:** `double`

### 输出

### **Y** — 脉冲波形复值向量

脉冲波形采样，以复值向量形式返回。

**数据类型:** `double`

### **PRF** — 脉冲重复频率 正标量

当前脉冲的脉冲重复频率，以正标量形式返回。

#### 依赖项

要启用此端口，请将 **输出信号格式** 参数设置为 `Pulses`，然后选择 **启用 PRF 输出** 参数。

**数据类型:** `double`

### **Coeff** — 匹配滤波器系数 向量 | 矩阵

匹配滤波器系数，以向量或矩阵形式返回。

#### 依赖项

要启用此端口，请选择 **启用匹配滤波器系数输出**。

**数据类型:** `double`
**复数支持:** Yes

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡的 **Prepare** 库中，选择 **Property Inspector**。

### **采样率 (Hz)** — 输出波形的采样率 `1e6`（默认）| 正标量

输出波形的采样率，指定为正标量。**采样率 (Hz)** 与 **脉冲重复频率 (Hz)** 向量中每个元素的比值必须为整数。此限制等同于要求脉冲重复间隔是采样间隔的整数倍。

#### 程序化使用

|  |
| --- |
| **模块参数:**`SampleRate` |
| **类型:**double |
| **值:**正标量 |
| **默认:**`1e6` |

### **指定脉冲持续时间的方法** — 脉冲持续时间作为时间或占空比 `Pulse width`（默认）| `Duty cycle`

设置脉冲持续时间的方法，指定为 `Pulse width` 或 `Duty cycle`。将此参数设置为 `Pulse width` 时，脉冲持续时间使用 **脉冲宽度 (s)** 参数设置。将此参数设置为 `Duty cycle` 时，脉冲持续时间根据 **脉冲重复频率 (Hz)** 和 **占空比** 参数的值计算。

#### 程序化使用

|  |
| --- |
| **模块参数:**`DurationSpecification` |
| **类型:**string |
| **值:**string |
| **默认:**`'Pulse width'` |

### **脉冲宽度 (s)** — 脉冲的时间持续时间 `50e-6`（默认）| 正标量

每个脉冲的持续时间，指定为正标量。将 **脉冲宽度 (s)** 与 **脉冲重复频率** 的乘积设置为小于或等于一。此限制确保脉冲宽度小于脉冲重复间隔。单位为秒。

**示例:** `300e-6`

#### 依赖项

要启用此参数，请将 **指定脉冲持续时间的方法** 参数设置为 `Pulse width`。

#### 程序化使用

|  |
| --- |
| **模块参数:**`PulseWidth` |
| **类型:**double |
| **值:**string |
| **默认:**`50e-6` |

### **占空比** — 波形占空比 `0.5`（默认）| 范围 *[0,1]* 内的标量

波形占空比，指定为范围 *[0,1]* 内的标量。

**示例:** `0.7`

#### 依赖项

要启用此参数，请将 **指定脉冲持续时间的方法** 参数设置为 `Duty cycle`。

#### 程序化使用

|  |
| --- |
| **模块参数:**`DutyCycle` |
| **类型:**double |
| **值:**正标量 |
| **默认:**`1e6` |

### **脉冲重复频率 (Hz)** — 脉冲重复频率 `1e4`（默认）| 正标量

脉冲重复频率 *PRF*，指定为标量或行向量。单位为 Hz。脉冲重复间隔 *PRI* 是脉冲重复频率 *PRF* 的倒数。**脉冲重复频率 (Hz)** 的值必须满足以下约束：

- **脉冲宽度** 与 **脉冲重复频率 (Hz)** 的乘积必须小于或等于一。此条件表示脉冲宽度小于一个脉冲重复间隔的要求。对于相位编码波形，脉冲宽度是码片宽度与码片数量的乘积。
- 采样率与 **脉冲重复频率** 的任一元素的比值必须为整数。此条件表示一个脉冲重复间隔内的采样点数量为整数的要求。

您可以仅使用模块参数设置，或结合输入端口 `PRFIdx` 来选择 *PRF* 的值。

- 当未选择 **启用 PRF 选择输入** 参数时，使用模块参数设置 *PRF*。

  - 要实现恒定 *PRF*，请将 **脉冲重复频率 (Hz)** 指定为正标量。
  - 要实现参差 *PRF*，请将 **脉冲重复频率 (Hz)** 指定为具有正值的行向量。当波形到达向量的最后一个元素后，过程从向量的第一个元素开始循环继续。当 *PRF* 为参差时，连续输出脉冲之间的时间在 *PRF* 向量的连续值之间循环。
- 当选择 **启用 PRF 选择输入** 参数时，您可以通过将 **脉冲重复频率 (Hz)** 指定为具有正实数值元素的行向量来实现可选择的 *PRF*。但此时，在执行模块时，通过将 *PRF* 向量的索引传入 `PRFIdx` 端口来选择 *PRF*。

在所有情况下，当将 **输出信号格式** 设置为 `Samples` 时，输出采样点数量是固定的。当使用变化的 *PRF* 并将 **输出信号格式** 设置为 `Pulses` 时，输出采样点数量可以变化。

#### 程序化使用

|  |
| --- |
| **模块参数:**`PRF` |
| **类型:**double |
| **值:**正标量 |
| **默认:**`1e6` |

### **启用 PRF 选择输入** — 选择预定义 PRF off（默认）| on

选择此参数以启用 `PRFIdx` 端口。

- 启用时，传入预定义 PRF 向量的索引。使用 **脉冲重复频率 (Hz)** 参数设置预定义 PRF。
- 未启用时，模块循环遍历 **脉冲重复频率 (Hz)** 参数指定的 PRF 向量。如果 **脉冲重复频率 (Hz)** 是标量，则 PRF 恒定。

#### 程序化使用

|  |
| --- |
| **模块参数:**`PRFSelectionInputPort` |
| **类型:**logical |
| **值:**正标量 |
| **默认:**`off` |

### **频率调制** — 频率调制 `Polynomial`（默认）| `Hyperbolic` | `Hybrid Linear-Tangent` | `Stepped Price`

非线性 FM 波形的频率调制，指定为 `Polynomial`、`Hyperbolic`、`Hybrid Linear-Tangent` 或 `Stepped Price`。

- 当设置为 `Polynomial` 时，模块生成瞬时频率遵循多项式函数的波形。多项式的系数由 **多项式 FM 的系数** 参数指定。所得频率函数经过归一化，使每个脉冲扫描 **扫描带宽 (Hz)** 中指定的带宽。当 **频率调制** 设置为 `Polynomial` 时，**扫描间隔** 参数不活动。
- 当设置为 `Hyperbolic` 时，模块生成双曲频率调制 (HFM) 波形。使用 **双曲 FM 的起始频率** 参数设置双曲扫描的起始频率。在这种情况下，**扫描间隔** 参数不活动。
- 当设置为 `Hybrid Linear-Tangent` 时，模块生成混合 NLFM 波形，将 LFM 与 tan-FM 组合，如 Collins 和 Atkins [1] 所述。LFM 与 tan-FM 之间的平衡由 **线性 FM 与 tan-FM 之间的平衡** 参数指定，用于 tan-FM 的 *tan(x)* 曲线部分由 **正切曲线部分** 参数指定。
- 当设置为 `Stepped Price` 时，模块生成 Price 的 NLFM 波形的阶梯版本，如 Levanon 和 Mozeson [2] 所述。当 **频率调制** 参数设置为 `Stepped Price` 时，**扫描间隔** 参数不活动。在这种情况下，扫描带宽由 **带宽因子** 参数中指定的带宽因子和 **频率步数** 参数中指定的频率步数确定。

**示例:** `Stepped Price`

#### 程序化使用

|  |
| --- |
| **模块参数:**`FrequencyModulation` |
| **类型:**char, string |
| **值:**char. string |
| **默认:**`Hyperbolic` |

**数据类型:** `char` | `string`

### **多项式 FM 的系数** — 多项式频率函数的系数 `[1 0 0]`（默认）| (*N*+1) 长度实值向量

多项式频率函数的系数，指定为长度 (*N*+1) 的实值向量。该向量表示 *N* 次多项式的系数。向量中的第一个元素是多项式最高次幂 *N* 的系数。最后一个元素是多项式零次幂项的系数。

**示例:** `[0.5,1,1,0.5]`

#### 依赖项

要启用此属性，请将 **频率调制** 参数设置为 `Polynomial`。

#### 程序化使用

|  |
| --- |
| **模块参数:**`PolynomialCoefficients` |
| **类型:**double |
| **值:**向量 |
| **默认:**`[1 0 0]` |

**数据类型:** `double`

### **扫描带宽 (Hz)** — 非线性 FM 扫描的带宽 `100e3`（默认）| 正标量

线性 FM 扫描的带宽，指定为正标量。单位为 Hz。

**示例:** `50e3`

#### 程序化使用

|  |
| --- |
| **模块参数:**`SweepBandwidth` |
| **类型:**double |
| **值:**正标量 |
| **默认:**`100e3` |

### **扫描方向** — 非线性 FM 扫描的方向 `Up`（默认）| `Down`

非线性 FM 扫描的方向，为 `Up`（频率增加）或 `Down`（频率减小）。

#### 程序化使用

|  |
| --- |
| **模块参数:**`SweepDirection` |
| **类型:**enum |
| **值:**Up, Down |
| **默认:**`Up` |

### **扫描间隔** — FM 频率扫描间隔 `Positive`（默认）| `Symmetric`

FM 频率扫描间隔，指定为 `Positive` 或 `Symmetric`。如果将此参数设置为 `Positive`，波形扫描 *0* 与 *B* 之间的频率间隔，其中 *B* 是 **扫描带宽** 参数的值。如果将此参数值设置为 `Symmetric`，波形扫描 *–B/2* 与 *B/2* 之间的间隔。

#### 程序化使用

|  |
| --- |
| **模块参数:**`SweepInterval` |
| **类型:**enum |
| **值:**Symmetric, Positive |
| **默认:**`Positive` |

### **包络函数** — FM 信号幅度包络 `Rectangular`（默认）| `Gaussian` | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

FM 信号幅度包络函数，指定为 `Rectangular`、`Gaussian`、`Hamming`、`Chebyshev`、`Hann`、`Kaiser` 或 `Taylor`。

#### 程序化使用

|  |
| --- |
| **模块参数:**`Envelope` |
| **类型:**enum |
| **值:**`Rectangular`, `Gaussian`, `Hamming`, `Chebyshev`, `Hann`, `Kaiser`, 或 `Taylor` |
| **默认:**`Rectangular` |

### **频率偏移来源** — 频率偏移来源 `Property`（默认）| `Input port`

频率偏移来源，指定为 `Property` 或 `Input port`。

- 当设置为 `Property` 时，偏移由 **频率偏移** 参数的值确定。
- 当设置为 `Input port` 时，偏移由 **FreqOffset** 端口的值确定。

#### 程序化使用

|  |
| --- |
| **模块参数:**`FrequencyOffsetSource` |
| **类型:**enum |
| **值:**`Property`, `Input Port` |
| **默认:**`Property` |

### **频率偏移 (Hz)** — 频率偏移 `0`（默认）| 标量

频率偏移，指定为标量。单位为 Hz。

**示例:** `2e3`

#### 依赖项

要启用此参数，请将 **频率偏移来源** 参数设置为 `Input port`。

#### 程序化使用

|  |
| --- |
| **模块参数:**`FrequencyOffset` |
| **类型:**double |
| **值:**`scalar` |
| **默认:**`0` |

### **输出信号格式** — 输出信号的格式 `Pulses`（默认）| `Samples`

输出信号的格式，指定为 `Pulses` 或 `Samples`。

如果将此参数设置为 `Samples`，模块的输出由多个采样点组成。采样点数量是 **输出中的采样点数** 参数的值。

如果将此参数设置为 `Pulses`，模块的输出由多个脉冲组成。脉冲数量是 **输出中的脉冲数** 参数的值。

#### 程序化使用

|  |
| --- |
| **模块参数:**`OutputFormat` |
| **类型:**enum |
| **值:**`Pulses` `Samples` |
| **默认:**`Pulses` |

### **输出中的采样点数** — 输出中的采样点数 `100`（默认）| 正整数

模块输出中的采样点数，指定为正整数。

**示例:** `1000`

#### 依赖项

要启用此参数，请将 **输出信号格式** 参数设置为 `Samples`。

#### 程序化使用

|  |
| --- |
| **模块参数:**`NumSamples` |
| **类型:**double |
| **值:**`positive scalar` |
| **默认:**`100` |

**数据类型:** `double`

### **输出中的脉冲数** — 输出中的脉冲数 `1`（默认）| 正整数

模块输出中的脉冲数，指定为正整数。

**示例:** `2`

#### 依赖项

要启用此参数，请将 **输出信号格式** 参数设置为 `Pulses`。

#### 程序化使用

|  |
| --- |
| **模块参数:**`NumPulses` |
| **类型:**double |
| **值:**`positive scalar` |
| **默认:**`1` |

**数据类型:** `double`

### **启用 PRF 输出** — 启用 PRF 输出 `off`（默认）| `on`

选择此参数以启用 `PRF` 输出端口。

#### 依赖项

要启用此参数，请将 **输出信号格式** 设置为 `Pulses`。

#### 程序化使用

|  |
| --- |
| **模块参数:**`PRFOutputPort` |
| **类型:**enum |
| **值:**`off` `on` |
| **默认:**`off` |

### **启用匹配滤波器系数输出** — 启用匹配滤波器系数输出 `off`（默认）| `on`

选择此参数以启用 `Coeff` 输出端口。

#### 程序化使用

|  |
| --- |
| **模块参数:**`CoefficientOutputPort` |
| **类型:**enum |
| **值:**`off` `on` |
| **默认:**`off` |

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认） | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果您希望您的模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果您
希望您的模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间进行编译，但通常运行
更快。

解释执行在您开发和调整模型时很有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改并执行您的模型。当您
对结果满意时，然后可以使用 `Code
Generation` 运行模块。长时间仿真使用生成的代码比在
解释执行中运行更快。您可以重复执行而无需重新编译，但如果您
更改任何模块参数，则模块会在执行前自动重新编译。

下表显示 **Simulate using** 参数如何影响
整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用
**Simulate using** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Waveforms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

非线性 FM 脉冲波形

Nonlinear FM Waveform 模块生成具有指定脉冲宽度、脉冲重复频率 (PRF) 和扫频带宽的非线性 FM 脉冲波形。该模块
输出整数个脉冲或整数个样本。
