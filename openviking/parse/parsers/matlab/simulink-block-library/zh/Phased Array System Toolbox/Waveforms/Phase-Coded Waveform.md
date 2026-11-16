---
type: simulink-block
title: 'Phase Coded Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveforms'
documentation_page: 'phasecodedwaveform'
documentation_source_path: 'ref/phasecodedwaveform.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Coded Waveform

## 端口

### 输入

### **PRFIdx** — PRF 索引正整数

用于选择脉冲重复频率 (PRF) 的索引，指定为正整数。该索引从 **Pulse repetition frequency (Hz)** 参数指定的预定义值向量中选择 PRF。

**示例：**
`4`

#### 依赖关系

要启用此端口，请选择 **Enable PRF selection input**。

**数据类型：** `double`

### **FreqOffset** — 频率偏移标量

频率偏移，以 Hz 为单位，指定为标量。

**示例：**
`2e3`

#### 依赖关系

要启用此端口，请将 **Source of Frequency Offset** 设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Y** — 脉冲波形复值向量

脉冲波形样本，返回为复值向量。

**数据类型：** `double`

### **PRF** — 脉冲重复频率正标量

当前脉冲的脉冲重复频率，返回为正标量。

#### 依赖关系

要启用此端口，请将 **Output signal format** 参数设置为 `Pulses`，然后选择 **Enable PRF output** 参数。

**数据类型：** `double`

### **Coeff** — 匹配滤波器系数向量

匹配滤波器系数，返回为向量。

#### 依赖关系

要启用此端口，请选择 **Enable Matched Filter Coefficients Output**。

**数据类型：** `double`
**复数支持：** Yes

## 参数

### **Sample rate (Hz)** — 输出波形的采样率 `1e6`（默认）| 正标量

输出波形的采样率，指定为正标量。将 **Sample rate (Hz)** 参数与 **Pulse repetition frequency (Hz)** 参数的比值设置为整数。

- **Sample rate (Hz)** 与 **Pulse repetition frequency (Hz)** 向量中每个元素的比值必须为整数。此限制等同于要求脉冲重复间隔是采样间隔的整数倍。
- **Sample rate (Hz)** 与 **Chip width (s)** 的乘积必须为整数。此限制等同于要求码片宽度是采样间隔的整数倍。

单位是 Hz。

**示例：** `5e3`

### **Phase code** — 用于相位调制的码类型 `Frank`（默认）

用于相位调制的码类型，指定为以下之一

- `Barker`
- `Frank`
- `P1`
- `P2`
- `P3`
- `P4`
- `Px`
- `Zadoff-Chu`
- `Maximum Length Sequence`
- `Quadratic Residue Sequence`
- `Custom`

**示例：** `P2`

### **Custom phase code** — 自定义相位码 `[1,-1]`（默认）| *M* 长度复值向量

自定义相位码，指定为长度-*M* 的复值向量。指定向量中的每个元素对应单个码片。

**示例：** `[j,2/3,-j]`

#### 依赖关系

要启用此参数，请将 **Code** 参数设置为 `'Custom'`。

**数据类型：** `double`
**复数支持：** Yes

### **Chip width (s)** — 码片时间长度 `1e-5`（默认）| 正标量

相位编码波形中每个码片的持续时间，指定为正标量。此参数的值必须满足以下约束：

- **Chip width (s)**、**Number of chips** 和 **Pulse repetition frequency (Hz)** 的乘积必须小于或等于一。此限制等同于要求脉冲长度小于脉冲重复间隔。
- **Sample rate (Hz)** 与 **Chip width (s)** 的乘积必须为整数。此限制等同于要求码片宽度是采样间隔的整数倍。

单位是 seconds。

**示例：** `2e-4`

### **Number of chips** — 波形中的码片数 `4`（默认）| 正整数

相位编码波形中的码片数，指定为正整数。**Chip width (s)**、**Number of chips** 和 **Pulse repetition frequency (Hz)** 参数的乘积必须小于或等于一。此限制等同于要求码片宽度是采样间隔的整数倍。

下表显示了不同码类型对码片数的附加约束。

| 如果 **Phase code** 参数是... | 那么 **Number of chips** 参数必须为... |
| --- | --- |
| `Frank`、`P1` 或 `Px` | 完全平方数 |
| `P2` | 一个偶数的完全平方数 |
| `Barker` | `2, 3, 4, 5, 7, 11, or 13` |
| `'Maximum Length Sequence'` | `7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, and 8191` |
| `'Quadratic Residue Sequence'` | 形式为 `4`*n*`-1` 的质数，其中 *n* 是整数 |

**示例：** `9`

#### 依赖关系

要启用此参数，请将 **Code** 参数设置为 `'Custom'` 以外的任何值。

### **Zadoff-Chu sequence index** — Zadoff-Chu 码类型的序列索引 `1`（默认）| 正整数

Zadoff-Chu 码类型的序列索引，指定为正整数。**Zadoff-Chu sequence index** 和 **Number of chips** 参数的值必须互质。

**示例：** `2`

#### 依赖关系

要启用此参数，请将 **Phase Code** 设置为 `Zadoff-Chu`。

### **Pulse repetition frequency (Hz)** — 脉冲重复频率 `1e4`（默认）| 正标量

脉冲重复频率 *PRF*，指定为标量或行向量。单位是 Hz。脉冲重复间隔 *PRI* 是脉冲重复频率 *PRF* 的倒数。**Pulse repetition frequency (Hz)** 的值必须满足以下约束：

- **Pulse width** 与 **Pulse repetition frequency (Hz)** 的乘积必须小于或等于一。此条件表示脉冲宽度小于一个脉冲重复间隔的要求。对于相位编码波形，脉冲宽度是码片宽度与码片数的乘积。
- 采样率与 **Pulse repetition frequency** 的任一元素的比值必须为整数。此条件表示一个脉冲重复间隔中的样本数是整数的要求。

您可以通过仅使用模块参数设置，或结合输入端口 `PRFIdx` 来选择 *PRF* 的值。

- 当未选择 **Enable PRF selection input** 参数时，使用模块参数设置 *PRF*。

  - 要实现恒定 *PRF*，请将 **Pulse repetition frequency (Hz)** 指定为正标量。
  - 要实现参差 *PRF*，请将 **Pulse repetition frequency (Hz)** 指定为正值的行向量。在波形到达向量的最后一个元素后，该过程从向量的第一个元素开始循环继续。当 *PRF* 参差时，连续输出脉冲之间的时间会在 *PRF* 向量的连续值之间循环。
- 当选择 **Enable PRF selection input** 参数时，可以通过将 **Pulse repetition frequency (Hz)** 指定为具有正实数值条目的行向量来实现可选择的 *PRF*。但此时，在执行模块时，通过将 *PRF* 向量的索引传递到 `PRFIdx` 端口来选择 *PRF*。

在所有情况下，当将 **Output signal format** 设置为 `Samples` 时，输出样本数是固定的。当使用变化的 *PRF* 并将 **Output signal format** 设置为 `Pulses` 时，输出样本数可以变化。

#### 编程使用

|  |
| --- |
| **模块参数：**`PRF` |
| **类型：**double |
| **值：**正标量 |
| **默认值：**`1e6` |

### **Enable PRF selection input** — 选择预定义 PRF off（默认）| on

选择此参数以启用 `PRFIdx` 端口。

- 启用时，传入预定义 PRF 向量的索引。使用 **Pulse repetition frequency (Hz)** 参数设置预定义 PRF。
- 未启用时，模块循环遍历由 **Pulse repetition frequency (Hz)** 参数指定的 PRF 向量。如果 **Pulse repetition frequency (Hz)** 是标量，则 PRF 恒定。

#### 编程使用

|  |
| --- |
| **模块参数：**`PRFSelectionInputPort` |
| **类型：**logical |
| **值：**正标量 |
| **默认值：**`off` |

### **Source of Frequency Offset** — 频率偏移源 `Property`（默认）| `Input port`

频率偏移源，指定为 `Property` 或 `Input port`。

- 设置为 `Property` 时，偏移由 **Frequency Offset** 参数的值确定。
- 设置为 `Input port` 时，偏移由 **FreqOffset** 端口的值确定。

#### 编程使用

|  |
| --- |
| **模块参数：**`FrequencyOffsetSource` |
| **类型：**enum |
| **值：**`Property`, `Input Port` |
| **默认值：**`Property` |

### **Frequency Offset (Hz)** — 频率偏移 `0`（默认）| 标量

频率偏移，指定为标量。单位是 Hz。

**示例：** `2e3`

#### 依赖关系

要启用此参数，请将 **Source of Frequency Offset** 参数设置为 `Input port`。

#### 编程使用

|  |
| --- |
| **模块参数：**`FrequencyOffset` |
| **类型：**double |
| **值：**`scalar` |
| **默认值：**`0` |

### **Source of simulation sample time** — 仿真采样时间源 `Derive from waveform parameters`（默认）| `Inherit from Simulink engine`

仿真采样时间源，指定为 `Derive from waveform parameters` 或 `Inherit from Simulink engine`。设置为 `Derive from waveform parameters` 时，模块以由所选波形的 PRF 确定的可变速率运行。经过时间是变化的。设置为 `Inherit from Simulink engine` 时，模块以固定速率运行，因此经过时间是常量。

#### 依赖关系

要启用此参数，请选择 **Enable PRF selection input** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：**`SimulationTimeSource` |
| **类型：**enum |
| **值：**`Derive from waveform parameters`, `Inherit from Simulink engine` |
| **默认值：**`Derive from waveform parameters` |

### **Output signal format** — 输出信号的格式 `Pulses`（默认）| `Samples`

输出信号的格式，指定为 `Pulses` 或 `Samples`。

如果将此参数设置为 `Samples`，则模块的输出由多个样本组成。样本数是 **Number of samples in output** 参数的值。

如果将此参数设置为 `Pulses`，则模块的输出由多个脉冲组成。脉冲数是 **Number of pulses in output** 参数的值。

#### 编程使用

|  |
| --- |
| **模块参数：**`OutputFormat` |
| **类型：**enum |
| **值：**`Pulses` `Samples` |
| **默认值：**`Pulses` |

### **Number of samples in output** — 输出中的样本数 `100`（默认）| 正整数

模块输出中的样本数，指定为正整数。

**示例：** `1000`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Samples`。

#### 编程使用

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

#### 编程使用

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

#### 编程使用

|  |
| --- |
| **模块参数：**`PRFOutputPort` |
| **类型：**enum |
| **值：**`off` `on` |
| **默认值：**`off` |

### **Enable Matched Filter Coefficients Output** — 启用匹配滤波器系数输出 `off`（默认）| `on`

选择此参数以启用 `Coeff` 输出端口。

#### 编程使用

|  |
| --- |
| **模块参数：**`CoefficientOutputPort` |
| **类型：**enum |
| **值：**`off` `on` |
| **默认值：**`off` |

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

下表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块均被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
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

相位编码脉冲波形

Phase-Coded Waveform 模块生成具有指定码片宽度、脉冲重复频率 (PRF) 和相位码的相位编码脉冲波形的样本。该模块输出整数个脉冲或样本。
