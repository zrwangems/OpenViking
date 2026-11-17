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
```yaml
ports:
- name: PRFIdx
  summary: PRF 索引 正整数
  direction: input
  data_types: double
- name: FreqOffset
  summary: 频率偏移 标量
  direction: input
  data_types: double
- name: Y
  summary: 脉冲波形 复值向量
  direction: output
  data_types: double
- name: PRF
  summary: 脉冲重复频率 正标量
  direction: output
  data_types: double
- name: Coeff
  summary: 匹配滤波器系数 向量 | 矩阵
  direction: output
  data_types: double
```

### 输入

### **PRFIdx** — PRF 索引 正整数

用于选择脉冲重复频率 (PRF) 的索引，指定为正整数。该索引从 **Pulse repetition frequency (Hz)** 参数指定的预定义值向量中选择 PRF。

**示例：**
`4`

#### 依赖关系

要启用此端口，请选择 **Enable PRF selection input**。

**数据类型：** `double`

### **FreqOffset** — 频率偏移 标量

频率偏移，以 Hz 为单位，指定为标量。

**示例：**
`2e3`

#### 依赖关系

要启用此端口，请将 **Source of Frequency Offset** 设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Y** — 脉冲波形 复值向量

脉冲波形采样，以复值向量形式返回。

**数据类型：** `double`

### **PRF** — 脉冲重复频率 正标量

当前脉冲的脉冲重复频率，以正标量形式返回。

#### 依赖关系

要启用此端口，请将 **Output signal format** 参数设置为 `Pulses`，然后选择 **Enable PRF output** 参数。

**数据类型：** `double`

### **Coeff** — 匹配滤波器系数 向量 | 矩阵

匹配滤波器系数，以向量或矩阵形式返回。

#### 依赖关系

要启用此端口，请选择 **Enable Matched Filter Coefficients Output**。

**数据类型：** `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Sample rate (Hz)
  summary: 输出波形的采样率 1e6（默认）| 正标量
  group: ''
  block_parameter: SampleRate
  type: double
  values: 正标量
  default: 1e6
- name: Method to specify pulse duration
  summary: 以时间或占空比表示脉冲持续时间 Pulse width（默认）| Duty cycle
  group: ''
  block_parameter: DurationSpecification
  type: string
  values: string
  default: '''Pulse width'''
- name: Pulse width (s)
  summary: 脉冲的时间持续时间 50e-6（默认）| 正标量
  group: ''
  block_parameter: PulseWidth
  type: double
  values: string
  default: 50e-6
- name: Duty cycle
  summary: 波形占空比 0.5（默认）| *[0,1]* 范围内的标量
  group: ''
  block_parameter: DutyCycle
  type: double
  values: 正标量
  default: 1e6
- name: Pulse repetition frequency (Hz)
  summary: 脉冲重复频率 1e4（默认）| 正标量
  group: ''
  block_parameter: PRF
  type: double
  values: positive scalar
  default: 1e6
- name: Enable PRF selection input
  summary: 选择预定义 PRF off（默认）| on
  group: ''
  block_parameter: PRFSelectionInputPort
  type: logical
  values: positive scalar
  default: 'off'
- name: Frequency modulation
  summary: 频率调制 Polynomial（默认）| Hyperbolic | Hybrid Linear-Tangent | Stepped Price
  group: ''
  block_parameter: FrequencyModulation
  type: char, string
  values: char. string
  default: Hyperbolic
- name: Coefficients of a polynomial FM
  summary: 多项式频率函数的系数 [1 0 0]（默认）| (*N*+1) 长度实值向量
  group: ''
  block_parameter: PolynomialCoefficients
  type: double
  values: vector
  default: '[1 0 0]'
- name: Sweep bandwidth (Hz)
  summary: 非线性调频扫频的带宽 100e3（默认）| 正标量
  group: ''
  block_parameter: SweepBandwidth
  type: double
  values: positive scalar
  default: 100e3
- name: Sweep direction
  summary: 非线性调频扫频的方向 Up（默认）| Down
  group: ''
  block_parameter: SweepDirection
  type: enum
  values: Up, Down
  default: Up
- name: Sweep interval
  summary: FM 频率扫描间隔 Positive（默认）| Symmetric
  group: ''
  block_parameter: SweepInterval
  type: enum
  values: Symmetric, Positive
  default: Positive
- name: Envelope function
  summary: FM 信号幅度包络 Rectangular（默认）| Gaussian | Hamming | Chebyshev | Hann | Kaiser | Taylor
  group: ''
  block_parameter: Envelope
  type: enum
  values: Rectangular、Gaussian、Hamming、Chebyshev、Hann、Kaiser 或 Taylor
  default: Rectangular
- name: Source of Frequency Offset
  summary: 频率偏移源 Property（默认）| Input port
  group: ''
  block_parameter: FrequencyOffsetSource
  type: enum
  values: Property、Input Port
  default: Property
- name: Frequency Offset (Hz)
  summary: 频率偏移 0（默认）| 标量
  group: ''
  block_parameter: FrequencyOffset
  type: double
  values: scalar
  default: '0'
- name: Output signal format
  summary: 输出信号的格式 Pulses（默认）| Samples
  group: ''
  block_parameter: OutputFormat
  type: enum
  values: Pulses Samples
  default: Pulses
- name: Number of samples in output
  summary: 输出中的样本数 100（默认）| 正整数
  group: ''
  block_parameter: NumSamples
  type: double
  values: positive scalar
  default: '100'
- name: Number of pulses in output
  summary: 输出中的脉冲数 1（默认）| 正整数
  group: ''
  block_parameter: NumPulses
  type: double
  values: positive scalar
  default: '1'
- name: Enable PRF Output
  summary: 启用 PRF 输出 off（默认）| on
  group: ''
  block_parameter: PRFOutputPort
  type: enum
  values: off on
  default: 'off'
- name: Enable Matched Filter Coefficients Output
  summary: 启用匹配滤波器系数输出 off（默认）| on
  group: ''
  block_parameter: CoefficientOutputPort
  type: enum
  values: off on
  default: 'off'
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution、Code Generation
  default: Interpreted Execution
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Sample rate (Hz)** — 输出波形的采样率 `1e6`（默认）| 正标量

输出波形的采样率，指定为正标量。**Sample rate (Hz)** 与 **Pulse repetition frequency (Hz)** 向量中每个元素的比值必须为整数。此限制等同于要求脉冲重复间隔是采样间隔的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数：**`SampleRate` |
| **类型：**double |
| **值：**正标量 |
| **默认值：**`1e6` |

### **Method to specify pulse duration** — 以时间或占空比表示脉冲持续时间 `Pulse width`（默认）| `Duty cycle`

设置脉冲持续时间的方法，指定为 `Pulse width` 或 `Duty cycle`。当将此参数设置为 `Pulse width` 时，脉冲持续时间使用 **Pulse width (s)** 参数设置。当将此参数设置为 `Duty cycle` 时，脉冲持续时间根据 **Pulse repetition frequency (Hz)** 和 **Duty Cycle** 参数的值计算得出。

#### 编程使用

|  |
| --- |
| **模块参数：**`DurationSpecification` |
| **类型：**string |
| **值：**string |
| **默认值：**`'Pulse width'` |

### **Pulse width (s)** — 脉冲的时间持续时间 `50e-6`（默认）| 正标量

每个脉冲的持续时间，指定为正标量。将 **Pulse width (s)** 与 **Pulse repetition frequency** 的乘积设置为小于或等于一。此限制确保脉冲宽度小于脉冲重复间隔。单位为秒。

**示例：** `300e-6`

#### 依赖关系

要启用此参数，请将 **Method to specify pulse duration** 参数设置为 `Pulse width`。

#### 编程使用

|  |
| --- |
| **模块参数：**`PulseWidth` |
| **类型：**double |
| **值：**string |
| **默认值：**`50e-6` |

### **Duty cycle** — 波形占空比 `0.5`（默认）| *[0,1]* 范围内的标量

波形占空比，指定为 *[0,1]* 范围内的标量。

**示例：** `0.7`

#### 依赖关系

要启用此参数，请将 **Method to specify pulse duration** 参数设置为 `Duty cycle`。

#### 编程使用

|  |
| --- |
| **模块参数：**`DutyCycle` |
| **类型：**double |
| **值：**正标量 |
| **默认值：**`1e6` |

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1e4`（默认）| 正标量

脉冲重复频率，*PRF*，指定为标量或行向量。
单位为 Hz。脉冲重复间隔，*PRI*，是脉冲重复频率 *PRF* 的倒数。**Pulse repetition frequency (Hz)** 的值必须满足以下约束：

- **Pulse width** 与 **Pulse repetition frequency (Hz)** 的乘积必须小于或等于一。此条件表示脉冲宽度小于一个脉冲重复间隔的要求。对于相位编码波形，脉冲宽度是码片宽度与码片数量的乘积。
- 采样率与 **Pulse repetition frequency** 的任一元素之比必须为整数。此条件表示一个脉冲重复间隔内的采样点数为整数。

您可以仅通过模块参数设置来选择 *PRF* 的值，也可以结合输入端口 `PRFIdx` 来选择。

- 当未选中 **Enable PRF selection input** 参数时，使用模块参数设置 *PRF*。

  - 要实现恒定 *PRF*，请将 **Pulse repetition frequency (Hz)** 指定为正标量。
  - 要实现参差 *PRF*，请将 **Pulse repetition frequency (Hz)** 指定为具有正值的行向量。当波形到达向量的最后一个元素后，该过程从向量的第一个元素开始循环继续。当 *PRF* 为参差时，连续输出脉冲之间的时间会在 *PRF* 向量的各个值之间循环。
- 当选中 **Enable PRF selection input** 参数时，您可以通过将 **Pulse repetition frequency (Hz)** 指定为具有正实数值元素的行向量来实现可选择的 *PRF*。但此时，在执行模块时，通过将 *PRF* 向量的索引传入 `PRFIdx` 端口来选择 *PRF*。

在所有情况下，当您将 **Output signal format** 设置为 `Samples` 时，输出采样点数是固定的。当您使用变化的 *PRF* 并将 **Output signal format** 设置为 `Pulses` 时，输出采样点数可能会变化。

#### 编程使用

|  |
| --- |
| **模块参数**：`PRF` |
| **类型**：double |
| **值**：positive scalar |
| **默认值**：`1e6` |

### **Enable PRF selection input** — 选择预定义 PRF off（默认）| on

选中此参数以启用 `PRFIdx` 端口。

- 启用时，传入预定义 PRF 向量的索引。使用 **Pulse repetition frequency (Hz)** 参数设置预定义 PRF。
- 未启用时，模块在 **Pulse repetition frequency (Hz)** 参数指定的 PRF 向量中循环。如果 **Pulse repetition frequency (Hz)** 是标量，则 PRF 是恒定的。

#### 编程使用

|  |
| --- |
| **模块参数**：`PRFSelectionInputPort` |
| **类型**：logical |
| **值**：positive scalar |
| **默认值**：`off` |

### **Frequency modulation** — 频率调制 `Polynomial`（默认）| `Hyperbolic` | `Hybrid Linear-Tangent` | `Stepped Price`

非线性调频波形的频率调制，指定为 `Polynomial`、`Hyperbolic`、`Hybrid Linear-Tangent` 或 `Stepped Price`。

- 当设置为 `Polynomial` 时，该模块生成瞬时频率遵循多项式函数的波形。多项式的系数由 **Coefficients of a Polynomial FM** 参数指定。生成的频率函数经过归一化，使得每个脉冲扫过 **Sweep bandwidth (Hz)** 中指定的带宽。当 **Frequency modulation** 设置为 `Polynomial` 时，**Sweep interval** 参数无效。
- 当设置为 `Hyperbolic` 时，该模块生成双曲调频（HFM）波形。使用 **Start frequency of a hyperbolic FM** 参数设置双曲扫频的起始频率。在这种情况下，**Sweep interval** 参数无效。
- 当设置为 `Hybrid Linear-Tangent` 时，该模块生成一种混合非线性调频波形，将 LFM 与 tan-FM 相结合，如 Collins 和 Atkins [1] 所述。LFM 与 tan-FM 之间的平衡由 **Balance between linear FM and tan-FM** 参数指定，用于 tan-FM 的 *tan(x)* 曲线部分由 **Tangent curve portion** 参数指定。
- 当设置为 `Stepped Price` 时，该模块生成 Price 非线性调频波形的步进版本，如 Levanon 和 Mozeson [2] 所述。当 **Frequency modulation** 参数设置为 `Stepped Price` 时，**Sweep interval** 参数无效。在这种情况下，扫频带宽由 **Bandwidth factors** 参数中指定的带宽因子和 **Number of frequency steps** 参数中指定的频率步数决定。

**示例：** `Stepped Price`

#### 编程使用

|  |
| --- |
| **模块参数**：`FrequencyModulation` |
| **类型**：char, string |
| **值**：char. string |
| **默认值**：`Hyperbolic` |

**Data Types:** `char` | `string`

### **Coefficients of a polynomial FM** — 多项式频率函数的系数 `[1 0 0]`（默认）| (*N*+1) 长度实值向量

多项式频率函数的系数，指定为长度 (*N*+1) 的实值向量。该向量表示 *N* 次多项式的系数。向量中的第一个元素是多项式最高次幂 *N* 的系数。最后一个元素是多项式零次幂项的系数。

**示例：** `[0.5,1,1,0.5]`

#### 依赖关系

要启用此属性，请将 **Frequency modulation** 参数设置为 `Polynomial`。

#### 编程使用

|  |
| --- |
| **模块参数**：`PolynomialCoefficients` |
| **类型**：double |
| **值**：vector |
| **默认值**：`[1 0 0]` |

**Data Types:** `double`

### **Sweep bandwidth (Hz)** — 非线性调频扫频的带宽 `100e3`（默认）| 正标量

线性调频扫频的带宽，指定为正标量。单位为 Hz。

**示例：** `50e3`

#### 编程使用

|  |
| --- |
| **模块参数**：`SweepBandwidth` |
| **类型**：double |
| **值**：positive scalar |
| **默认值**：`100e3` |

### **Sweep direction** — 非线性调频扫频的方向 `Up`（默认）| `Down`

非线性调频扫频的方向，为 `Up`（频率增加）或 `Down`（频率减小）。

#### 编程使用

|  |
| --- |
| **模块参数**：`SweepDirection` |
| **类型**：enum |
| **值**：Up, Down |
| **默认值**：`Up` |

### **Sweep interval** — FM 频率扫描间隔 `Positive`（默认）| `Symmetric`

FM 频率扫描间隔，指定为 `Positive` 或 `Symmetric`。如果将此参数设置为 `Positive`，波形在 *0* 和 *B* 之间的频率间隔内扫描，其中 *B* 是 **Sweep bandwidth** 参数的值。如果将此参数值设置为 `Symmetric`，波形在 *–B/2* 和 *B/2* 之间的间隔内扫描。

#### 编程使用

|  |
| --- |
| **模块参数**：`SweepInterval` |
| **类型**：enum |
| **值**：Symmetric, Positive |
| **默认值**：`Positive` |

### **Envelope function** — FM 信号幅度包络 `Rectangular`（默认）| `Gaussian` | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

FM 信号幅度包络函数，指定为 `Rectangular`、`Gaussian`、`Hamming`、`Chebyshev`、`Hann`、`Kaiser` 或 `Taylor`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Envelope` |
| **类型**：enum |
| **值**：`Rectangular`、`Gaussian`、`Hamming`、`Chebyshev`、`Hann`、`Kaiser` 或 `Taylor` |
| **默认值**：`Rectangular` |

### **Source of Frequency Offset** — 频率偏移源 `Property`（默认）| `Input port`

频率偏移源，指定为 `Property` 或 `Input port`。

- 当设置为 `Property` 时，偏移由 **Frequency Offset** 参数的值确定。
- 当设置为 `Input port` 时，偏移由 **FreqOffset** 端口的值确定。

#### 编程使用

|  |
| --- |
| **模块参数**：`FrequencyOffsetSource` |
| **类型**：enum |
| **值**：`Property`、`Input Port` |
| **默认值**：`Property` |

### **Frequency Offset (Hz)** — 频率偏移 `0`（默认）| 标量

频率偏移，指定为标量。单位为 Hz。

**Example:** `2e3`

#### 依赖关系

要启用此参数，请将 **Source of Frequency Offset** 参数设置为 `Input port`。

#### 编程使用

|  |
| --- |
| **模块参数**：`FrequencyOffset` |
| **类型**：double |
| **值**：`scalar` |
| **默认值**：`0` |

### **Output signal format** — 输出信号的格式 `Pulses`（默认）| `Samples`

输出信号的格式，指定为 `Pulses` 或 `Samples`。

如果将此参数设置为 `Samples`，模块的输出由多个样本组成。样本数是 **Number of samples in output** 参数的值。

如果将此参数设置为 `Pulses`，模块的输出由多个脉冲组成。脉冲数是 **Number of pulses in output** 参数的值。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputFormat` |
| **类型**：enum |
| **值**：`Pulses` `Samples` |
| **默认值**：`Pulses` |

### **Number of samples in output** — 输出中的样本数 `100`（默认）| 正整数

模块输出中的样本数，指定为正整数。

**Example:** `1000`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Samples`。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumSamples` |
| **类型**：double |
| **值**：`positive scalar` |
| **默认值**：`100` |

**Data Types:** `double`

### **Number of pulses in output** — 输出中的脉冲数 `1`（默认）| 正整数

模块输出中的脉冲数，指定为正整数。

**Example:** `2`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Pulses`。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumPulses` |
| **类型**：double |
| **值**：`positive scalar` |
| **默认值**：`1` |

**Data Types:** `double`

### **Enable PRF Output** — 启用 PRF 输出 `off`（默认）| `on`

选择此参数以启用 `PRF` 输出端口。

#### 依赖关系

要启用此参数，请将 **Output signal format** 设置为 `Pulses`。

#### 程序化使用

|  |
| --- |
| **模块参数：**`PRFOutputPort` |
| **类型：**enum |
| **值：**`off` `on` |
| **默认值：**`off` |

### **Enable Matched Filter Coefficients Output** — 启用匹配滤波器系数输出 `off`（默认）| `on`

选择此参数以启用 `Coeff` 输出端口。

#### 程序化使用

|  |
| --- |
| **模块参数：**`CoefficientOutputPort` |
| **类型：**enum |
| **值：**`off` `on` |
| **默认值：**`off` |

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果您希望模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认值：** `Interpreted Execution` |
## 所属库

Phased Array System Toolbox / Waveforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

非线性 FM 脉冲波形

Nonlinear FM Waveform 模块生成具有指定脉冲宽度、脉冲重复频率（PRF）和扫频带宽的非线性 FM 脉冲波形。该模块输出整数个脉冲或整数个采样。
