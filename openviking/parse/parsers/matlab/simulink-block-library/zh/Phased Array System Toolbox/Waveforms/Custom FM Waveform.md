---
type: simulink-block
title: 'Custom FM Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveforms'
documentation_page: 'customfmwaveform'
documentation_source_path: 'ref/customfmwaveform.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom FM Waveform

## 端口

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

脉冲重复频率 *PRF*，指定为标量或行向量。
单位为 Hz。脉冲重复间隔 *PRI* 是脉冲重复频率 *PRF* 的倒数。
**Pulse repetition frequency (Hz)** 的值必须满足以下约束：

- **Pulse width** 与 **Pulse repetition frequency (Hz)** 的乘积必须小于或等于一。该条件表示脉冲宽度小于一个脉冲重复间隔的要求。对于相位编码波形，脉冲宽度是码片宽度与码片数量的乘积。
- 采样率与 **Pulse repetition frequency** 的任一元素之比必须为整数。该条件表示一个脉冲重复间隔内的采样点数为整数。

你可以仅通过模块参数设置来选择 *PRF* 的值，也可以结合输入端口 `PRFIdx` 来选择。

- 当未选中 **Enable PRF selection input** 参数时，使用模块参数设置 *PRF*。

  - 要实现恒定 *PRF*，将 **Pulse repetition frequency (Hz)** 指定为正标量。
  - 要实现参差 *PRF*，将 **Pulse repetition frequency (Hz)** 指定为具有正值的行向量。当波形到达向量的最后一个元素后，过程从向量的第一个元素开始循环继续。当 *PRF* 为参差时，连续输出脉冲之间的时间会在 *PRF* 向量的连续值之间循环。
- 当选中 **Enable PRF selection input** 参数时，你可以通过将 **Pulse repetition frequency (Hz)** 指定为具有正实数值元素的行向量来实现可选择的 *PRF*。但此时，当你执行模块时，通过将 *PRF* 向量的索引传入 `PRFIdx` 端口来选择 *PRF*。

在所有情况下，当将 **Output signal format** 设置为 `Samples` 时，输出采样点数是固定的。当你使用变化的 *PRF* 并将 **Output signal format** 设置为 `Pulses` 时，输出采样点数可能会变化。

#### 编程使用

|  |
| --- |
| **模块参数**：`PRF` |
| **类型**：double |
| **值**：positive scalar |
| **默认值**：`1e6` |

### **Enable PRF selection input** — 选择预定义 PRF off（默认）| on

选择此参数以启用 `PRFIdx` 端口。

- 启用时，传入预定义 PRF 向量的索引。使用 **Pulse repetition frequency (Hz)** 参数设置预定义 PRF。
- 未启用时，模块会在由 **Pulse repetition frequency (Hz)** 参数指定的 PRF 向量中循环。如果 **Pulse repetition frequency (Hz)** 是标量，则 PRF 恒定。

#### 编程使用

|  |
| --- |
| **模块参数**：`PRFSelectionInputPort` |
| **类型**：logical |
| **值**：positive scalar |
| **默认值**：`off` |

### **Source of simulation sample time** — 仿真采样时间来源 `Derive from waveform parameters`（默认）| `Inherit from Simulink engine`

仿真采样时间来源，指定为 `Derive from waveform parameters` 或 `Inherit from Simulink engine`。
当设置为 `Derive from waveform parameters` 时，模块以由所选波形的 PRF 决定的可变速率运行。经过时间是可变的。当设置为 `Inherit from Simulink engine` 时，模块以固定速率运行，因此经过时间是常量。

#### 依赖关系

要启用此参数，请选中 **Enable PRF selection input** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulationTimeSource` |
| **类型**：enum |
| **值**：`Derive from waveform parameters`, `Inherit from Simulink engine` |
| **默认值**：`Derive from waveform parameters` |

### **频率调制** — Wavefform 频率调制函数，长度为 *M* 的实值向量 | 函数句柄 | 元胞数组

波形频率调制函数，指定为长度为 *M* 的实值向量、函数句柄或元胞数组。

- 如果 `FrequencyModulation` 属性是向量，则它指定 *M* 个点处的瞬时频率采样值，表示为
  [*f*1,
  *f*2, …,
  *f*M]。波形按照指定的频率进行扫频，对于第 *k* 个脉冲，
  其起始时间为 *t*k，持续时间为
  *T*k，则在时刻

  tm=tk+(m−1)Tk/(M−1)

  的瞬时频率等于 *f*m，其中
  *t*k ≦
  *t*m ≦
  *t*k +
  *T*k，且 *m* =
  1...*M*。时刻
  *t*m 与
  *t*m+1 之间的瞬时频率通过对 *f*m 和
  *f*m+1 进行线性插值得到。由此生成的自定义 FM 波形
  可视为由 *M*-1 个等时长的 LFM 段组成的分段 LFM 波形。
- 如果 `FrequencyModulation` 属性是函数句柄，
  则该函数必须具有以下语法：`f = fmFcn(t)`，其中
  *f* 是时刻
  *t* 处的瞬时频率。*t* 是用于计算
  瞬时频率的时刻。*t* 中的值介于 0 和脉冲宽度之间。
- 如果 `FrequencyModulation` 属性是元胞数组，则
  第一个元胞必须是如上所述的函数句柄。元胞数组中的
  其余元素是函数的附加输入参数（如果有）。

#### 程序化使用

|  |
| --- |
| **模块参数：**`FrequencyModulation` |
| **类型：**char, string, function |
| **值：**char. string |
| **默认值：**`Hyperbolic` |

**数据类型：** `char` | `string`

### **包络函数** — FM 信号幅度包络 `Rectangular`（默认）| `Gaussian` | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

FM 信号幅度包络函数，指定为
`Rectangular`、`Gaussian`、
`Hamming`、`Chebyshev`、
`Hann`、`Kaiser` 或
`Taylor`。

#### 程序化使用

|  |
| --- |
| **模块参数：**`Envelope` |
| **类型：**enum |
| **值：**`Rectangular`、`Gaussian`、`Hamming`、`Chebyshev`、`Hann`、`Kaiser` 或 `Taylor` |
| **默认值：**`Rectangular` |

### **频率偏移源** — 频率偏移的来源 `Property`（默认）| `Input port`

频率偏移的来源，指定为 `Property` 或
`Input port`。

- 当设置为
  `Property` 时，偏移量由 **Frequency
  Offset** 参数的值决定。
- 当设置为 `Input
  port` 时，偏移量由
  **FreqOffset**
  端口的值决定。

#### 程序化使用

|  |
| --- |
| **模块参数：**`FrequencyOffsetSource` |
| **类型：**enum |
| **值：**`Property`、`Input Port` |
| **默认值：**`Property` |

### **频率偏移 (Hz)** — 频率偏移 `0`（默认）| 标量

频率偏移，指定为标量。单位为 Hz。

**示例：** `2e3`

#### 依赖关系

要启用此参数，请将 **Source of Frequency Offset**
参数设置为 `Input port`。

#### 程序化使用

|  |
| --- |
| **模块参数：**`FrequencyOffset` |
| **类型：**double |
| **值：**`scalar` |
| **默认值：**`0` |

### **输出信号格式** — 输出信号的格式 `Pulses`（默认）| `Samples`

输出信号的格式，指定为 `Pulses` 或 `Samples`。

如果将此参数设置为 `Samples`，则模块的输出由多个采样组成。采样数量为 **Number of samples in output** 参数的值。

如果将此参数设置为 `Pulses`，则模块的输出由多个脉冲组成。脉冲数量为 **Number of pulses in output** 参数的值。

#### 程序化使用

|  |
| --- |
| **模块参数：**`OutputFormat` |
| **类型：**enum |
| **值：**`Pulses` `Samples` |
| **默认值：**`Pulses` |

### **输出中的采样数** — 输出中的采样数 `100`（默认）| 正整数

模块输出中的采样数，指定为正整数。

**示例：** `1000`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Samples`。

#### 编程用法

|  |
| --- |
| **模块参数：**`NumSamples` |
| **类型：**double |
| **值：**`positive scalar` |
| **默认值：**`100` |

**数据类型：** `double`

### **Number of pulses in output** — 输出中的脉冲数 `1`（默认）| 正整数

模块输出中的脉冲数，指定为正整数。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Pulses`。

#### 编程用法

|  |
| --- |
| **模块参数：**`NumPulses` |
| **类型：**double |
| **值：**`positive scalar` |
| **默认值：**`1` |

**数据类型：** `double`

### **Enable PRF Output** — 启用 PRF 输出 `off`（默认）| `on`

选择此参数以启用 `PRF` 输出端口。

#### 依赖关系

要启用此参数，请将 **Output signal format** 设置为 `Pulses`。

#### 编程用法

|  |
| --- |
| **模块参数：**`PRFOutputPort` |
| **类型：**enum |
| **值：**`off` `on` |
| **默认值：**`off` |

### **Enable Matched Filter Coefficients Output** — 启用匹配滤波器系数输出 `off`（默认）| `on`

选择此参数以启用 `Coeff` 输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`CoefficientOutputPort` |
| **类型：**enum |
| **值：**`off` `on` |
| **默认值：**`off` |

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

此表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程用法

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

自定义 FM 脉冲波形

Custom FM Waveform 模块生成具有指定脉冲宽度、脉冲重复频率 (PRF) 和扫频带宽的自定义 FM 脉冲波形。该模块输出整数个脉冲或整数个采样。
