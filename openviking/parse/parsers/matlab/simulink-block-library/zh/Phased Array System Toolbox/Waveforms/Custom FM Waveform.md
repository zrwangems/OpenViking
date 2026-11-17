---
type: simulink-block
title: 'Custom FM Waveform'
family: 'waveforms'
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

用于选择脉冲重复频率 (PRF) 的索引，指定为正整数。该索引从 **脉冲重复频率 (Hz)** 参数指定的预定义值向量中选择 PRF。

**示例：**
`4`

#### 依赖关系

要启用此端口，请选择 **启用 PRF 选择输入**。

**数据类型：** `double`

### **FreqOffset** — 频率偏移 标量

频率偏移，以 Hz 为单位，指定为标量。

**示例：**
`2e3`

#### 依赖关系

要启用此端口，请将 **频率偏移源** 设置为 `Input port`。

**数据类型：** `double`

### 输出

### **Y** — 脉冲波形 复值向量

脉冲波形采样，返回为复值向量。

**数据类型：** `double`

### **PRF** — 脉冲重复频率 正标量

当前脉冲的脉冲重复频率，返回为正标量。

#### 依赖关系

要启用此端口，请将 **输出信号格式** 参数设置为 `Pulses`，然后选择 **启用 PRF 输出** 参数。

**数据类型：** `double`

### **Coeff** — 匹配滤波器系数 向量 | 矩阵

匹配滤波器系数，返回为向量或矩阵。

#### 依赖关系

要启用此端口，请选择 **启用匹配滤波器系数输出**。

**数据类型：** `double`
**复数支持：** Yes

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **采样率 (Hz)** — 输出波形的采样率 `1e6`（默认值） | 正标量

输出波形的采样率，指定为正标量。**采样率 (Hz)** 与 **脉冲重复频率 (Hz)** 向量中每个元素的比值必须为整数。此限制等同于要求脉冲重复间隔是采样间隔的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数：**`SampleRate` |
| **类型：**double |
| **值：**正标量 |
| **默认值：**`1e6` |

### **指定脉冲持续时间的方法** — 脉冲持续时间（以时间或占空比表示） `Pulse width`（默认值） | `Duty cycle`

用于设置脉冲持续时间的方法，指定为 `Pulse width` 或 `Duty cycle`。当将此参数设置为 `Pulse width` 时，脉冲持续时间使用 **脉冲宽度 (s)** 参数设置。当将此参数设置为 `Duty cycle` 时，脉冲持续时间根据 **脉冲重复频率 (Hz)** 和 **占空比** 参数的值计算。

#### 编程用法

|  |
| --- |
| **模块参数：**`DurationSpecification` |
| **类型：**string |
| **值：**string |
| **默认值：**`'Pulse width'` |

### **脉冲宽度 (s)** — 脉冲的时间持续时间 `50e-6`（默认值） | 正标量

每个脉冲的持续时间，指定为正标量。将 **脉冲宽度 (s)** 与 **脉冲重复频率** 的乘积设置为小于或等于一。此限制确保脉冲宽度小于脉冲重复间隔。单位为秒。

**示例：** `300e-6`

#### 依赖关系

要启用此参数，请将 **指定脉冲持续时间的方法** 参数设置为 `Pulse width`。

#### 编程用法

|  |
| --- |
| **模块参数：**`PulseWidth` |
| **类型：**double |
| **值：**string |
| **默认值：**`50e-6` |

### **占空比** — 波形占空比 `0.5`（默认值） | 范围 *[0,1]* 中的标量

波形占空比，指定为范围 *[0,1]* 中的标量。

**示例：** `0.7`

#### 依赖关系

要启用此参数，请将 **指定脉冲持续时间的方法** 参数设置为 `Duty cycle`。

#### 编程用法

|  |
| --- |
| **模块参数：**`DutyCycle` |
| **类型：**double |
| **值：**正标量 |
| **默认值：**`1e6` |

### **脉冲重复频率 (Hz)** — 脉冲重复频率 `1e4`（默认值） | 正标量

脉冲重复频率，*PRF*，指定为标量或行向量。单位为 Hz。脉冲重复间隔，*PRI*，是脉冲重复频率 *PRF* 的倒数。**脉冲重复频率 (Hz)** 的值必须满足以下约束：

- **脉冲宽度** 与 **脉冲重复频率 (Hz)** 的乘积必须小于或等于一。此条件表示脉冲宽度小于一个脉冲重复间隔的要求。对于相位编码波形，脉冲宽度是码片宽度与码片数量的乘积。
- 采样率与 **脉冲重复频率** 的任何元素的比值必须为整数。此条件表示一个脉冲重复间隔中的采样数为整数的要求。

您可以通过仅使用模块参数设置，或结合输入端口 `PRFIdx` 来选择 *PRF* 的值。

- 当未选择 **启用 PRF 选择输入** 参数时，使用模块参数设置 *PRF*。

  - 要实现恒定 *PRF*，请将 **脉冲重复频率 (Hz)** 指定为正标量。
  - 要实现参差 *PRF*，请将 **脉冲重复频率 (Hz)** 指定为具有正值的行向量。在波形到达向量的最后一个元素后，过程会循环继续使用向量的第一个元素。当 *PRF* 为参差时，连续输出脉冲之间的时间会循环经历 *PRF* 向量的连续值。
- 当选择 **启用 PRF 选择输入** 参数时，您可以通过将 **脉冲重复频率 (Hz)** 指定为具有正实数值的行向量来实现可选择的 *PRF*。但此时，在执行模块时，通过将 *PRF* 向量的索引传递到 `PRFIdx` 端口来选择 *PRF*。

在所有情况下，当您将 **输出信号格式** 设置为 `Samples` 时，输出采样数是固定的。当您使用变化的 *PRF* 并将 **输出信号格式** 设置为 `Pulses` 时，输出采样数可以变化。

#### 编程用法

|  |
| --- |
| **模块参数：**`PRF` |
| **类型：**double |
| **值：**正标量 |
| **默认值：**`1e6` |

### **启用 PRF 选择输入** — 选择预定义 PRF off（默认值） | on

选择此参数以启用 `PRFIdx` 端口。

- 启用时，传入预定义 PRF 向量的索引。使用 **脉冲重复频率 (Hz)** 参数设置预定义 PRF。
- 未启用时，模块会循环使用 **脉冲重复频率 (Hz)** 参数指定的 PRF 向量。如果 **脉冲重复频率 (Hz)** 是标量，则 PRF 恒定。

#### 编程用法

|  |
| --- |
| **模块参数：**`PRFSelectionInputPort` |
| **类型：**logical |
| **值：**正标量 |
| **默认值：**`off` |

### **仿真采样时间来源** — 仿真采样时间的来源 `Derive from waveform parameters`（默认值） | `Inherit from Simulink engine`

仿真采样时间来源，指定为 `Derive from waveform parameters` 或 `Inherit from Simulink engine`。当设置为 `Derive from waveform parameters` 时，模块以由所选波形的 PRF 决定的可变速率运行。经过的时间是可变的。当设置为 `Inherit from Simulink engine` 时，模块以固定速率运行，因此经过的时间是常量。

#### 依赖关系

要启用此参数，请选择 **启用 PRF 选择输入** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：**`SimulationTimeSource` |
| **类型：**enum |
| **值：**`Derive from waveform parameters`, `Inherit from Simulink engine` |
| **默认值：**`Derive from waveform parameters` |

### **频率调制** — 波形频率调制函数 长度为 *M* 的实值向量 | 函数句柄 | 元胞数组

波形频率调制函数，指定为长度为 *M* 的实值向量、函数句柄或元胞数组。

- 如果 `FrequencyModulation` 属性是向量，则它指定 *M* 个点处的瞬时频率采样，格式为 [*f*1, *f*2, …, *f*M]。对于第 *k* 个脉冲，起始时间为 *t*k，持续时间为 *T*k，波形扫过指定频率，使得时间

  tm=tk+(m−1)Tk/(M−1)

  处的瞬时频率等于 *f*m，其中 *t*k ≦ *t*m ≦ *t*k + *T*k 且 *m* = 1...*M*。时间 *t*m 和 *t*m+1 之间的瞬时频率通过对 *f*m 和 *f*m+1 进行线性插值得到。得到的自定义 FM 波形可视为由 *M*-1 个等持续时间 LFM 段组成的分段 LFM 波形。
- 如果 `FrequencyModulation` 属性是函数句柄，则该函数必须具有以下语法：`f = fmFcn(t)`，其中 *f* 是时间 *t* 处的瞬时频率。*t* 是计算瞬时频率的时间。*t* 中的值介于 0 和脉冲宽度之间。
- 如果 `FrequencyModulation` 属性是元胞数组，则第一个元胞必须是上面指定的函数句柄。元胞数组中的其余条目是函数的附加输入参数（如果有）。

#### 编程用法

|  |
| --- |
| **模块参数：**`FrequencyModulation` |
| **类型：**char, string, function |
| **值：**char. string |
| **默认值：**`Hyperbolic` |

**数据类型：** `char` | `string`

### **包络函数** — FM 信号幅度包络 `Rectangular`（默认值） | `Gaussian` | `Hamming` | `Chebyshev` | `Hann` | `Kaiser` | `Taylor`

FM 信号幅度包络函数，指定为 `Rectangular`、`Gaussian`、`Hamming`、`Chebyshev`、`Hann`、`Kaiser` 或 `Taylor`。

#### 编程用法

|  |
| --- |
| **模块参数：**`Envelope` |
| **类型：**enum |
| **值：**`Rectangular`, `Gaussian`, `Hamming`, `Chebyshev`, `Hann`, `Kaiser`, 或 `Taylor` |
| **默认值：**`Rectangular` |

### **频率偏移源** — 频率偏移的来源 `Property`（默认值） | `Input port`

频率偏移源，指定为 `Property` 或 `Input port`。

- 当设置为 `Property` 时，偏移由 **频率偏移 (Hz)** 参数的值确定。
- 当设置为 `Input port` 时，偏移由 **FreqOffset** 端口的值确定。

#### 编程用法

|  |
| --- |
| **模块参数：**`FrequencyOffsetSource` |
| **类型：**enum |
| **值：**`Property`, `Input Port` |
| **默认值：**`Property` |

### **频率偏移 (Hz)** — 频率偏移 `0`（默认值） | 标量

频率偏移，指定为标量。单位为 Hz。

**示例：** `2e3`

#### 依赖关系

要启用此参数，请将 **频率偏移源** 参数设置为 `Input port`。

#### 编程用法

|  |
| --- |
| **模块参数：**`FrequencyOffset` |
| **类型：**double |
| **值：**`scalar` |
| **默认值：**`0` |

### **输出信号格式** — 输出信号的格式 `Pulses`（默认值） | `Samples`

输出信号的格式，指定为 `Pulses` 或 `Samples`。

如果将参数设置为 `Samples`，则模块输出包含多个采样。采样数是 **输出中的采样数** 参数的值。

如果将参数设置为 `Pulses`，则模块输出包含多个脉冲。脉冲数是 **输出中的脉冲数** 参数的值。

#### 编程用法

|  |
| --- |
| **模块参数：**`OutputFormat` |
| **类型：**enum |
| **值：**`Pulses` `Samples` |
| **默认值：**`Pulses` |

### **输出中的采样数** — 输出中的采样数 `100`（默认值） | 正整数

模块输出中的采样数，指定为正整数。

**示例：** `1000`

#### 依赖关系

要启用此参数，请将 **输出信号格式** 参数设置为 `Samples`。

#### 编程用法

|  |
| --- |
| **模块参数：**`NumSamples` |
| **类型：**double |
| **值：**`positive scalar` |
| **默认值：**`100` |

**数据类型：** `double`

### **输出中的脉冲数** — 输出中的脉冲数 `1`（默认值） | 正整数

模块输出中的脉冲数，指定为正整数。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **输出信号格式** 参数设置为 `Pulses`。

#### 编程用法

|  |
| --- |
| **模块参数：**`NumPulses` |
| **类型：**double |
| **值：**`positive scalar` |
| **默认值：**`1` |

**数据类型：** `double`

### **启用 PRF 输出** — 启用 PRF 输出 `off`（默认值） | `on`

选择此参数以启用 `PRF` 输出端口。

#### 依赖关系

要启用此参数，请将 **输出信号格式** 设置为 `Pulses`。

#### 编程用法

|  |
| --- |
| **模块参数：**`PRFOutputPort` |
| **类型：**enum |
| **值：**`off` `on` |
| **默认值：**`off` |

### **启用匹配滤波器系数输出** — 启用匹配滤波器系数输出 `off`（默认值） | `on`

选择此参数以启用 `Coeff` 输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`CoefficientOutputPort` |
| **类型：**enum |
| **值：**`off` `on` |
| **默认值：**`off` |

### **仿真方式** — 模块仿真方法 `Interpreted Execution`（默认值） | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则模块会在执行前自动重新编译。

下表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |  |

有关更多信息，请参阅选择仿真模式 (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Waveforms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

自定义 FM 脉冲波形

Custom FM Waveform 模块生成具有指定脉冲宽度、脉冲重复频率 (PRF) 和扫频带宽的自定义 FM 脉冲波形。该模块输出整数个脉冲或整数个采样。
