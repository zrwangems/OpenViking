---
type: simulink-block
title: 'FMCW Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveforms'
documentation_page: 'fmcwwaveform'
documentation_source_path: 'ref/fmcwwaveform.html'
language: zh-CN
chinese_source: worker-translation
---

# FMCW Waveform

## 端口
```yaml
ports:
- name: Port_1
  summary: FMCW 波形复值列向量
  direction: output
```

### 输出

### **Port\_1** — FMCW 波形复值列向量

FMCW 波形，以包含波形样本的复值列向量形式返回。

- 如果 **Output signal format** 参数设置为 `Samples`，则该端口的输出包含由 **Number of samples in output** 参数设置的样本数。
- 如果 **Output signal format** 参数设置为 `Sweeps`，则该端口的输出包含由 **Number of sweeps in output** 参数设置的扫频数。此外，如果 **Sweep direction** 参数设置为 `Triangle`，则每个扫频的持续时间为半个周期。
## 参数
```yaml
parameters:
- name: Sample rate (Hz)
  summary: 输出波形的采样率 1e6（默认）| 正标量
  group: ''
  block_parameter: SampleRate
  type: double
  values: positive scalar
  default: 1e6
- name: Sweep time (s)
  summary: 每个线性调频扫频的持续时间 1e-4（默认）
  group: ''
- name: Sweep bandwidth (Hz)
  summary: 调频扫频带宽 1e5（默认）
  group: ''
- name: Sweep direction
  summary: 调频扫频方向 Up（默认）| Down | Triangle
  group: ''
- name: Sweep interval
  summary: 调频扫频区间的位置 Positive（默认）| Symmetric
  group: ''
- name: Output signal format
  summary: 输出信号格式 Sweeps（默认）| Samples
  group: ''
- name: Number of samples in output
  summary: 输出中的采样数 100（默认）| 正整数
  group: ''
  block_parameter: NumSamples
  type: double
  values: positive scalar
- name: Number of sweeps in output
  summary: 输出中的扫频数 1（默认）
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution、Code Generation
```

### **Sample rate (Hz)** — 输出波形的采样率 `1e6`（默认）| 正标量

输出波形的采样率，指定为正标量。**Sample rate (Hz)** 与 **Pulse repetition frequency (Hz)** 向量中每个元素的比值必须为整数。此限制等同于要求脉冲重复间隔是采样间隔的整数倍。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleRate` |
| **类型**：double |
| **值**：positive scalar |
| **默认值**：`1e6` |

### **Sweep time (s)** — 每个线性调频扫频的持续时间 `1e-4`（默认）

将信号的上扫频或下扫频的持续时间（以秒为单位）指定为正实数的标量或行向量。**Sample rate** 值与每个 **Sweep time** 条目的乘积必须为整数。

要实现变化的扫频时间，请将 **Sweep time** 指定为行向量。波形将使用该向量的连续条目作为波形连续周期的扫频时间。如果到达该向量的最后一个元素，则过程将从该向量的第一个条目开始循环继续。

如果 **Sweep time** 和 **Sweep bandwidth** 均为行向量，则这些向量必须具有相同的长度。

如果 **Sweep direction** 为 `Up` 或 `Down`，则扫频周期等于扫频时间。如果 **Sweep direction** 为 `Triangle`，则扫频周期是扫频时间的两倍，因为每个周期由一个上扫频段和一个下扫频段组成。

### **Sweep bandwidth (Hz)** — 调频扫频带宽 `1e5`（默认）

将线性调频扫频的带宽（以赫兹为单位）指定为正实数的标量或行向量。

要实现变化的带宽，请将 **Sweep bandwidth** 指定为行向量。波形将使用该向量的连续条目作为波形连续周期的扫频带宽。如果波形到达 **Sweep bandwidth** 向量的最后一个元素，则过程将从该向量的第一个条目开始循环继续。

如果 **Sweep time** 和 **Sweep bandwidth** 均为行向量，则这些向量必须具有相同的长度。

### **Sweep direction** — 调频扫频方向 `Up`（默认）| `Down` | `Triangle`

将线性调频扫频的方向指定为 `Up`、`Down` 或 `Triangle` 之一。

### **Sweep interval** — 调频扫频区间的位置 `Positive`（默认）| `Symmetric`

如果将此参数值设置为 `Positive`，则波形在 0 和 *B* 之间的区间内扫频，其中 *B* 是 **Sweep bandwidth** 参数的值。如果将此参数设置为 `Symmetric`，则波形在 *–B/2* 和 *B/2* 之间的区间内扫频。

### **Output signal format** — 输出信号格式 `Sweeps`（默认）| `Samples`

将输出信号的格式指定为 `Sweeps` 或 `Samples`。

如果将此参数设置为 `Sweeps`，则模块的输出形式为多个扫频。扫频数是 **Number of sweeps in output** 参数的值。

如果将此参数设置为 `Samples`，则模块的输出形式为多个样本。样本数是 **Number of samples in output** 参数的值。

如果 **Sweep direction** 参数设置为 `Triangle`，则每个扫频为半个周期。

### **Number of samples in output** — 输出中的采样数 `100`（默认）| 正整数

模块输出中的采样数，指定为正整数。

**示例：** `1000`

#### 依赖关系

要启用此参数，请将 **Output signal format** 参数设置为 `Samples`。

#### 程序化使用

|  |
| --- |
| **模块参数：**`NumSamples` |
| **类型：**double |
| **值：**`positive scalar` |
| **默认：**`100` |

**数据类型：** `double`

### **Number of sweeps in output** — 输出中的扫频数 `1`（默认）

将模块输出中的扫频数指定为正整数。此参数仅在将 **Output signal format** 设置为 `Sweeps` 时显示。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |
## 所属库

Phased Array System Toolbox / Waveforms

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

调频连续波（FMCW）波形源

FMCW Waveform 模块生成具有指定扫频时间和扫频带宽的调频连续波（FMCW）波形。模块输出可以是整数个脉冲或采样。
