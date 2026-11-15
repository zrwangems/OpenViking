---
type: simulink-block
title: 'Stepped FM Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveform Design and Signal Synthesis / Pulsed Waveforms'
documentation_page: 'steppedfmwaveform'
documentation_source_path: 'ref/steppedfmwaveform.html'
language: zh-CN
chinese_source: worker-translation
---

# Stepped FM Waveform

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

要启用此端口，请将 **频率偏移来源** 设置为 `Input port`。

**数据类型：** `double`

### 输出

### **Y** — 脉冲波形 复值向量

脉冲波形样本，以复值向量形式返回。

**数据类型：** `double`

### **PRF** — 脉冲重复频率 正标量

当前脉冲的脉冲重复频率，以正标量形式返回。

#### 依赖关系

要启用此端口，请将 **输出信号格式** 参数设置为 `Pulses`，然后选择 **启用 PRF 输出** 参数。

**数据类型：** `double`

### **Coeff** — 匹配滤波器系数 向量 | 矩阵

匹配滤波器系数，以向量或矩阵形式返回。

#### 依赖关系

要启用此端口，请选择 **启用匹配滤波器系数输出**。

**数据类型：** `double`
**复数支持：** Yes

## 参数

### **采样率 (Hz)** — 输出波形的采样率 `1e6` (默认) | 正标量

输出波形的采样率，指定为正标量。**采样率 (Hz)** 与 **脉冲重复频率 (Hz)** 向量中每个元素的比值必须是整数。此限制等同于要求脉冲重复间隔是采样间隔的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数：**`SampleRate` |
| **类型：**double |
| **取值：**正标量 |
| **默认值：**`1e6` |

### **指定脉冲持续时间的方法** — 脉冲持续时间，以时间或占空比表示 `Pulse width` (默认) | `Duty cycle`

设置脉冲持续时间的方法，指定为 `Pulse width` 或 `Duty cycle`。当将此参数设置为 `Pulse width` 时，脉冲持续时间使用 **脉冲宽度 (s)** 参数设置。当将此参数设置为 `Duty cycle` 时，脉冲持续时间根据 **脉冲重复频率 (Hz)** 和 **占空比** 参数的值计算。

#### 编程用法

|  |
| --- |
| **模块参数：**`DurationSpecification` |
| **类型：**string |
| **取值：**string |
| **默认值：**`'Pulse width'` |

### **脉冲宽度 (s)** — 脉冲的时间持续时间 `50e-6` (默认) | 正标量

每个脉冲的持续时间，指定为正标量。将 **脉冲宽度 (s)** 与 **脉冲重复频率** 的乘积设置为小于或等于一。此限制确保脉冲宽度小于脉冲重复间隔。单位为 seconds。

**示例：** `300e-6`

#### 依赖关系

要启用此参数，请将 **指定脉冲持续时间的方法** 参数设置为 `Pulse width`。

#### 编程用法

|  |
| --- |
| **模块参数：**`PulseWidth` |
| **类型：**double |
| **取值：**string |
| **默认值：**`50e-6` |

### **占空比** — 波形占空比 `0.5` (默认) | *[0,1]* 范围内的标量

波形占空比，指定为 *[0,1]* 范围内的标量。

**示例：** `0.7`

#### 依赖关系

要启用此参数，请将 **指定脉冲持续时间的方法** 参数设置为 `Duty cycle`。

#### 编程用法

|  |
| --- |
| **模块参数：**`DutyCycle` |
| **类型：**double |
| **取值：**正标量 |
| **默认值：**`1e6` |

### **脉冲重复频率 (Hz)** — 脉冲重复频率 `1e4` (默认) | 正标量

脉冲重复频率 *PRF*，指定为标量或行向量。单位为 Hz。脉冲重复间隔 *PRI* 是脉冲重复频率 *PRF* 的倒数。**脉冲重复频率 (Hz)** 的值必须满足以下约束：

- **脉冲宽度** 与 **脉冲重复频率 (Hz)** 的乘积必须小于或等于一。此条件表示要求脉冲宽度小于一个脉冲重复间隔。对于相位编码波形，脉冲宽度是码片宽度与码片数量的乘积。
- 采样率与 **脉冲重复频率** 的任一元素的比值必须是整数。此条件表示要求一个脉冲重复间隔中的样本数必须是整数。

您可以仅使用模块参数设置，或结合输入端口 `PRFIdx` 来选择 *PRF* 的值。

- 当未选择 **启用 PRF 选择输入** 参数时，使用模块参数设置 *PRF*。
  - 要实现恒定 *PRF*，请将 **脉冲重复频率 (Hz)** 指定为正标量。
  - 要实现参差 *PRF*，请将 **脉冲重复频率 (Hz)** 指定为具有正值的行向量。当波形到达向量的最后一个元素后，过程会循环地从向量的第一个元素继续。当 *PRF* 参差时，连续输出脉冲之间的时间会循环使用 *PRF* 向量的连续值。
- 当选择 **启用 PRF 选择输入** 参数时，您可以通过将 **脉冲重复频率 (Hz)** 指定为具有正实数值元素的行向量来实现可选择的 *PRF*。但此时，在执行模块时，通过将 *PRF* 向量的索引传递到 `PRFIdx` 端口来选择 *PRF*。

在所有情况下，当您将 **输出信号格式** 设置为 `Samples` 时，输出样本数是固定的。当您使用变化的 *PRF* 并将 **输出信号格式** 设置为 `Pulses` 时，输出样本数可能会变化。

#### 编程用法

|  |
| --- |
| **模块参数：**`PRF` |
| **类型：**double |
| **取值：**正标量 |
| **默认值：**`1e6` |

### **启用 PRF 选择输入** — 选择预定义 PRF off (默认) | on

选择此参数以启用 `PRFIdx` 端口。

- 启用时，传入预定义 PRF 向量的索引。使用 **脉冲重复频率 (Hz)** 参数设置预定义 PRF。
- 未启用时，模块循环遍历 **脉冲重复频率 (Hz)** 参数指定的 PRF 向量。如果 **脉冲重复频率 (Hz)** 是标量，则 PRF 恒定。

#### 编程用法

|  |
| --- |
| **模块参数：**`PRFSelectionInputPort` |
| **类型：**logical |
| **取值：**正标量 |
| **默认值：**`off` |

### **频率步长 (Hz)** — 线性频率步长 `2e4` (默认) | 正标量

将线性频率步长指定为正标量。单位为 Hertz。

**示例：** `1e3`

### **频率步数** — 脉冲中的频率步数 `5` (默认) | 正整数

将频率步数指定为正整数。当 **频率步数** 为 1 时，步进 FM 波形退化为矩形波形。

**示例：** `8`

### **仿真采样时间来源** — 仿真采样时间的来源 `Derive from waveform parameters` (默认) | `Inherit from Simulink engine`

仿真采样时间的来源，指定为 `Derive from waveform parameters` 或 `Inherit from Simulink engine`。当设置为 `Derive from waveform parameters` 时，模块以由所选波形的 PRF 确定的可变速率运行。经过时间是可变的。当设置为 `Inherit from Simulink engine` 时，模块以固定速率运行，因此经过时间是常量。

#### 依赖关系

要启用此参数，请选择 **启用 PRF 选择输入** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：**`SimulationTimeSource` |
| **类型：**enum |
| **取值：**`Derive from waveform parameters`, `Inherit from Simulink engine` |
| **默认值：**`Derive from waveform parameters` |

### **频率偏移来源** — 频率偏移的来源 `Property` (默认) | `Input port`

频率偏移的来源，指定为 `Property` 或 `Input port`。

- 当设置为 `Property` 时，偏移由 **频率偏移** 参数的值确定。
- 当设置为 `Input port` 时，偏移由 **FreqOffset** 端口的值确定。

#### 编程用法

|  |
| --- |
| **模块参数：**`FrequencyOffsetSource` |
| **类型：**enum |
| **取值：**`Property`, `Input Port` |
| **默认值：**`Property` |

### **频率偏移 (Hz)** — 频率偏移 `0` (默认) | 标量

频率偏移，指定为标量。单位为 Hz。

**示例：** `2e3`

#### 依赖关系

要启用此参数，请将 **频率偏移来源** 参数设置为 `Input port`。

#### 编程用法

|  |
| --- |
| **模块参数：**`FrequencyOffset` |
| **类型：**double |
| **取值：**`scalar` |
| **默认值：**`0` |

### **输出信号格式** — 输出信号的格式 `Pulses` (默认) | `Samples`

输出信号的格式，指定为 `Pulses` 或 `Samples`。

如果将此参数设置为 `Samples`，模块的输出由多个样本组成。样本数是 **输出中的样本数** 参数的值。

如果将此参数设置为 `Pulses`，模块的输出由多个脉冲组成。脉冲数是 **输出中的脉冲数** 参数的值。

#### 编程用法

|  |
| --- |
| **模块参数：**`OutputFormat` |
| **类型：**enum |
| **取值：**`Pulses` `Samples` |
| **默认值：**`Pulses` |

### **输出中的样本数** — 输出中的样本数 `100` (默认) | 正整数

模块输出中的样本数，指定为正整数。

**示例：** `1000`

#### 依赖关系

要启用此参数，请将 **输出信号格式** 参数设置为 `Samples`。

#### 编程用法

|  |
| --- |
| **模块参数：**`NumSamples` |
| **类型：**double |
| **取值：**`positive scalar` |
| **默认值：**`100` |

**数据类型：** `double`

### **输出中的脉冲数** — 输出中的脉冲数 `1` (默认) | 正整数

模块输出中的脉冲数，指定为正整数。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **输出信号格式** 参数设置为 `Pulses`。

#### 编程用法

|  |
| --- |
| **模块参数：**`NumPulses` |
| **类型：**double |
| **取值：**`positive scalar` |
| **默认值：**`1` |

**数据类型：** `double`

### **启用 PRF 输出** — 启用 PRF 输出 `off` (默认) | `on`

选择此参数以启用 `PRF` 输出端口。

#### 依赖关系

要启用此参数，请将 **输出信号格式** 设置为 `Pulses`。

#### 编程用法

|  |
| --- |
| **模块参数：**`PRFOutputPort` |
| **类型：**enum |
| **取值：**`off` `on` |
| **默认值：**`off` |

### **启用匹配滤波器系数输出** — 启用匹配滤波器系数输出 `off` (默认) | `on`

选择此参数以启用 `Coeff` 输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：**`CoefficientOutputPort` |
| **类型：**enum |
| **取值：**`off` `on` |
| **默认值：**`off` |

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为已编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **取值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Waveforms

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

步进 FM 脉冲波形

Stepped FM Waveform 模块生成具有指定脉冲宽度、脉冲重复频率 (PRF) 和频率步数的步进 FM 脉冲波形。发射频率在脉冲持续时间内以恒定步长递增。该模块输出整数个脉冲或样本。
