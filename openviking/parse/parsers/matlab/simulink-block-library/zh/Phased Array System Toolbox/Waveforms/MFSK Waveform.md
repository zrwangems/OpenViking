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

### **Port\_1** — MFSK Waveform 复值列向量

MFSK 波形，作为包含波形样本的复值列向量返回。

- 如果 **输出信号格式** 参数设置为 `Steps`，则端口的输出包含由 **输出中的频率步进数** 参数设置的步进数。
- 如果 **输出信号格式** 参数设置为 `Samples`，则端口的输出包含由 **输出中的样本数** 参数设置的样本数。
- 如果 **输出信号格式** 参数设置为 `Sweeps`，则端口的输出包含由 **输出中的扫频数** 参数设置的扫频数。

## 参数

### **采样率 (Hz)** — 采样率 `151e6`（默认） | positive scalar

信号的采样率，指定为 positive scalar。单位为 hertz。

### **扫频带宽 (Hz)** — MFSK 扫频带宽 `150e6`（默认） | positive scalar

MFSK 扫频的带宽，指定为 positive scalar。单位为 hertz。

### **频率步进突发时间 (s)** — 频率步进突发时间 `5e-6`（默认） | positive scalar

每个频率步进的持续时间，指定为 positive scalar。单位为 seconds。

### **每次扫频的步进数** — 频率步进总数 `512`（默认） | even positive scalar

每次扫频中的总步进数，指定为 even positive integer。

### **线性调频偏移频率 (Hz)** — 线性调频偏移频率 `-294e3`（默认） | real scalar

线性调频偏移频率，指定为 real scalar。单位为 hertz。该偏移确定两个序列之间的频率平移。

### **输出信号格式** — 输出信号格式 `Steps`（默认） | `Samples` | `Sweeps`

输出信号的格式，指定为以下之一：

- `Steps` — 模块输出由 **输出中的频率步进数** 参数指定的整数个频率步进所包含的样本数。
- `Samples` — 模块输出 **输出中的样本数** 参数中指定的样本数。
- `Sweeps` — 模块输出由 **输出中的扫频数** 参数指定的整数个扫频所包含的样本数。

### **输出中的扫频数** — 输出中的扫频数 `1`（默认） | positive integer

模块输出中的扫频数，指定为 positive integer。

#### 依赖关系

仅当将 **输出信号格式** 设置为 `Sweeps` 时，此参数才会出现。

### **输出中的频率步进数** — 输出中的频率步进数 `1`（默认） | positive integer

模块输出中的步进数，指定为 positive integer。

#### 依赖关系

仅当将 **输出信号格式** 设置为 `Steps` 时，此参数才会出现。

### **输出中的样本数** — 输出中的样本数 `100`（默认） | positive integer

模块输出中的样本数，指定为 positive integer。

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

### **仿真方式** — 模块仿真方法 `Interpreted Execution`（默认） | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间来编译，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

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

**在 R2015a 中引入**

## 描述

多频移键控 (MFSK) 连续波形

MFSK Waveform 模块生成具有指定步进时间、扫频带宽、频率偏移和步进数的多频移键控 (MFSK) 连续波形。该模块输出整数个样本、步进或扫频。有关 MFSK 波形结构的详细信息，请参阅 `phased.MFSKWaveform`。
