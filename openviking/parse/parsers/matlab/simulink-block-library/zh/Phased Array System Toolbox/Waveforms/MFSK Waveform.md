---
type: simulink-block
title: 'MFSK Waveform'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveforms'
documentation_page: 'mfskwaveform'
documentation_source_path: 'ref/mfskwaveform.html'
language: zh-CN
chinese_source: worker-translation
---

# MFSK Waveform

## 端口

### 输出

### **Port\_1** — MFSK 波形 复值列向量

MFSK 波形，以包含波形样本的复值列向量形式返回。

- 如果 **Output signal format** 参数设置为 `Steps`，则该端口的输出包含由 **Number of frequency steps in output** 参数设置的步数。
- 如果 **Output signal format** 参数设置为 `Samples`，则该端口的输出包含由 **Number of samples in output** 参数设置的样本数。
- 如果 **Output signal format** 参数设置为 `Sweeps`，则该端口的输出包含由 **Number of sweeps in output** 参数设置的扫描数。

## 参数

### **Sample rate (Hz)** — 采样率 `151e6`（默认）| 正标量

信号的采样率，指定为正标量。单位为赫兹。

### **Sweep bandwidth (Hz)** — MFSK 扫描带宽 `150e6`（默认）| 正标量

MFSK 扫描的带宽，指定为正标量。单位为赫兹。

### **Frequency step burst time (s)** — 频率步进突发时间 `5e-6`（默认）| 正标量

每个频率步进的持续时间，指定为正标量。单位为秒。

### **Number of steps per sweep** — 每次扫描的总频率步数 `512`（默认）| 偶正标量

每次扫描中的总步数，指定为偶正整数。

### **Chirp offset frequency (Hz)** — 线性调频偏移频率 `-294e3`（默认）| 实标量

线性调频偏移频率，指定为实标量。单位为赫兹。该偏移量决定两个序列之间的频率平移。

### **Output signal format** — 输出信号格式 `Steps`（默认）| `Samples` | `Sweeps`

输出信号的格式，指定为以下之一：

- `Steps` — 模块输出由 **Number of frequency steps in output** 参数指定的整数个频率步进所包含的样本数。
- `Samples` — 模块输出由 **Number of samples in output** 参数指定的样本数。
- `Sweeps` — 模块输出由 **Number of sweeps in output** 参数指定的整数次扫描所包含的样本数。

### **Number of sweeps in output** — 输出中的扫描次数 `1`（默认）| 正整数

模块输出中的扫描次数，指定为正整数。

#### 依赖关系

此参数仅在将 **Output signal format** 设置为 `Sweeps` 时显示。

### **Number of frequency steps in output** — 输出中的频率步数 `1`（默认）| 正整数

模块输出中的步数，指定为正整数。

#### 依赖关系

此参数仅在将 **Output signal format** 设置为 `Steps` 时显示。

### **Number of samples in output** — 输出中的样本数 `100`（默认）| 正整数

模块输出中的样本数，指定为正整数。

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

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或
`Code Generation`。如果希望模块使用
MATLAB® 解释器，请选择 `Interpreted Execution`。如果
希望模块作为编译代码运行，请选择 `Code
Generation`。编译代码需要时间编译，但通常运行
更快。

当您开发和调整模型时，解释执行很有用。模块
在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对
结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成代码比
解释执行运行得更快。您可以重复执行而无需重新编译，但如果您
更改任何模块参数，模块会在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响
整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式
会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

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

**在 R2015a 中引入**

## 描述

多频移键控 (MFSK) 连续波形

MFSK Waveform 模块生成具有指定步进时间、扫频带宽、频率偏移和
步进数的多频移键控 (MFSK)
连续波形。模块输出整数个采样、步进或扫频。有关
MFSK 波形结构的详细信息，请参阅 `phased.MFSKWaveform`。
