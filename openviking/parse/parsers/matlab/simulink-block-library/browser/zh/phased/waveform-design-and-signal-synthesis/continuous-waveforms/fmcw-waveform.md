---
type: simulink-block
title: 'FMCW Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveform Design and Signal Synthesis / Continuous Waveforms'
documentation_page: 'fmcwwaveform'
documentation_source_path: 'ref/fmcwwaveform.html'
language: zh-CN
chinese_source: worker-translation
---

# FMCW Waveform

## 端口

### 输出

### **Port\_1** — FMCW Waveform 复值列向量

FMCW 波形，以包含波形样本的复值列向量形式返回。

- 如果 **输出信号格式** 参数设置为 `Samples`，则该端口的输出由 **输出中的样本数** 参数设置的样本数组成。
- 如果 **输出信号格式** 参数设置为 `Sweeps`，则该端口的输出由 **输出中的扫频数** 参数设置的扫频数组成。此外，如果 **扫频方向** 参数设置为 `Triangle`，则每个扫频的持续时间为半个周期。

## 参数

### **采样率 (Hz)** — 输出波形的采样率 `1e6` (默认值) | 正标量

输出波形的采样率，指定为正标量。**采样率 (Hz)** 与 **脉冲重复频率 (Hz)** 向量中每个元素的比值必须为整数。此限制等效于要求脉冲重复间隔是采样间隔的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数：**`SampleRate` |
| **类型：**double |
| **值：**正标量 |
| **默认值：**`1e6` |

### **扫频时间 (s)** — 每个线性 FM 扫频的持续时间 `1e-4` (默认值)

将信号上扫频或下扫频的持续时间（以 s 为单位）指定为正实数的标量或行向量。**采样率** 值与每个 **扫频时间** 元素的乘积必须为整数。

要实现变化的扫频时间，请将 **扫频时间** 指定为行向量。波形将向量的连续元素用作波形连续周期的扫频时间。如果到达向量的最后一个元素，则该过程会从向量的第一个元素开始循环继续。

如果 **扫频时间** 和 **扫频带宽** 都是行向量，则这些向量必须具有相同长度。

如果 **扫频方向** 为 `Up` 或 `Down`，则扫频周期等于扫频时间。如果 **扫频方向** 为 `Triangle`，则扫频周期是扫频时间的两倍，因为每个周期由一个上扫频段和一个下扫频段组成。

### **扫频带宽 (Hz)** — FM 扫频带宽 `1e5` (默认值)

将线性 FM 扫频的带宽（以 Hz 为单位）指定为正实数的标量或行向量。

要实现变化的带宽，请将 **扫频带宽** 指定为行向量。波形将向量的连续元素用作波形连续周期的扫频带宽。如果波形到达 **扫频带宽** 向量的最后一个元素，则该过程会从向量的第一个元素开始循环继续。

如果 **扫频时间** 和 **扫频带宽** 都是行向量，则这些向量必须具有相同长度。

### **扫频方向** — FM 扫频方向 `Up` (默认值) | `Down` | `Triangle`

将线性 FM 扫频的方向指定为 `Up`、`Down` 或 `Triangle` 之一。

### **扫频间隔** — FM 扫频间隔的位置 `Positive` (默认值) | `Symmetric`

如果将此参数值设置为 `Positive`，则波形在 0 与 *B* 之间的区间内扫频，其中 *B* 是 **扫频带宽** 参数的值。如果将此参数设置为 `Symmetric`，则波形在 *–B/2* 与 *B/2* 之间的区间内扫频。

### **输出信号格式** — 输出信号格式 `Sweeps` (默认值) | `Samples`

将输出信号的格式指定为 `Sweeps` 或 `Samples`。

如果将此参数设置为 `Sweeps`，则模块输出采用多个扫频的形式。扫频数是 **输出中的扫频数** 参数的值。

如果将此参数设置为 `Samples`，则模块输出采用多个样本的形式。样本数是 **输出中的样本数** 参数的值。

如果 **扫频方向** 参数设置为 `Triangle`，则每个扫频是周期的一半。

### **输出中的样本数** — 输出中的样本数 `100` (默认值) | 正整数

模块输出中的样本数，指定为正整数。

**示例：** `1000`

#### 依赖关系

要启用此参数，请将 **输出信号格式** 参数设置为 `Samples`。

#### 编程使用

|  |
| --- |
| **模块参数：**`NumSamples` |
| **类型：**double |
| **值：**`positive scalar` |
| **默认值：**`100` |

**数据类型：** `double`

### **输出中的扫频数** — 输出中的扫频数 `1` (默认值)

将模块输出中的扫频数指定为正整数。仅当将 **输出信号格式** 设置为 `Sweeps` 时，此参数才会出现。

### **仿真使用** — 模块仿真方法 `Interpreted Execution` (默认值) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行得更快。您可以重复运行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真使用** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真使用** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块会被编译。 | 模型中的所有模块都会被编译。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

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

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

调频连续波 (FMCW) 波形源

FMCW Waveform 模块生成具有指定扫频时间和扫频带宽的调频连续波 (FMCW) 波形。模块输出可以是整数个脉冲或样本。
