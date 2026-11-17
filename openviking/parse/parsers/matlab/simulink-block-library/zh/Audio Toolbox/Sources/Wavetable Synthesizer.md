---
type: simulink-block
title: 'Wavetable Synthesizer'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'wavetablesynthesizer'
documentation_source_path: 'ref/wavetablesynthesizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Wavetable Synthesizer

## 端口

### 输入

### **WT** — 实数值的单周期波形向量

#### 依赖

要启用此端口，请为 Single-cycle waveform 参数选择 **Specify wavetable from input port**。

**数据类型：** `single` | `double`

### **F** — 输出波频率 (Hz) 非负标量 | 非负值向量

#### 依赖

要启用此端口，请为 Output wave frequency (Hz) 参数选择 **Specify frequency from input port**。

**数据类型：** `single` | `double`

### **A** — 输出波幅度 非负标量

#### 依赖

要启用此端口，请为 Output wave amplitude 参数选择 **Specify amplitude from input port**。

**数据类型：** `single` | `double`

### **DC** — 输出波直流偏移 标量

#### 依赖

要启用此端口，请为 Output wave DC offset 参数选择 **Specify DC offset from input port**。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号 向量 | 矩阵

Wavetable Synthesizer 模块输出由模块参数定义的周期信号。

**数据类型：** `single` | `double`

## 参数

如果某个参数被列为可调，则可以在仿真期间更改其值。

### **Single-cycle waveform** — 波表 `sin(2*pi*(0:511)/512)`（默认）| 实数值向量

Wavetable Synthesizer 模块对单周期波形进行索引，以合成周期波。

要从输入端口指定 **Single-cycle waveform**，请为该参数选择 **Specify wavetable from input port**。

**可调：** 是

### **Output wave frequency (Hz)** — 生成信号的频率 `100`（默认）| 非负标量

单周期波形在一秒内重复的次数。

要从输入端口指定 **Output wave frequency (Hz)**，请为该参数选择 **Specify frequency from input port**。

**可调：** 是

### **Output wave amplitude** — 生成信号的幅度 `1`（默认）| 非负标量

幅度缩放应用于直流偏移之前。

要从输入端口指定 **Output wave amplitude**，请为该参数选择 **Specify amplitude from input port**。

**可调：** 是

### **Output wave phase offset** — 生成信号的归一化相位偏移 `0`（默认）| `[0,1]` 范围内的标量

相位偏移范围 `[0,1]` 对应于归一化的 2π 弧度区间。

### **Output wave DC offset** — 添加到生成信号每个元素的值 `0`（默认）| 标量

要从输入端口指定 **Output wave DC offset**，请为该参数选择 **Specify DC offset from input port**。

**可调：** 是

### **Samples per frame** — 模块输出的每帧采样数 `512`（默认）| 正整数标量

模块输出的每帧采样数，指定为正整数标量。

**可调：** 否

### **Sample rate (Hz)** — 生成信号的采样率 `44100`（默认）| 正标量

生成信号的采样率，指定为正标量。

**可调：** 否

### **Output data type** — 生成信号的数据类型 `double`（默认）| `single`

生成信号的数据类型，指定为 `double` 或 `single`。

**可调：** 否

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` – 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` – 使用 MATLAB® 解释器仿真模型。此选项可减少启动时间，仿真速度与 `Code generation` 相当。在此模式下，您可以调试模块的源代码。

## 所属库

Audio Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

从单周期波形生成周期信号

Wavetable Synthesizer 模块生成具有可调参数的周期信号。该周期信号由缓存的单周期波形定义，该波形作为 Wavetable Synthesizer 模块的 **Single-cycle waveform** 参数。

Wavetable Synthesizer 模块使您能够输出重复的单周期波形，同时调整单周期波形的各个方面，例如频率、幅度和偏移。
