---
type: simulink-block
title: 'Voice Activity Detector'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Measurements'
documentation_page: 'voiceactivitydetector'
documentation_source_path: 'ref/voiceactivitydetector.html'
language: zh-CN
chinese_source: worker-translation
---

# Voice Activity Detector

## 端口

### 输入

### **x** — 输入信号矩阵 | 一维向量

- 矩阵输入 —— 输入的每一列被视为一个独立通道。
- 一维向量输入 —— 输入被视为单通道。

除非您指定额外的输入端口，否则此端口未命名。

**数据类型：** `single` | `double`

### **SilenceToSpeech** — 范围 [0, 1] 内的阈值（dB）标量

#### 依赖关系

要启用此端口，请为从静音帧到语音帧的转移概率参数选择**从输入端口指定静音到语音概率**。

**数据类型：** `single` | `double`

### **SpeechToSilence** — 范围 [0, 1] 内的阈值（dB）标量

#### 依赖关系

要启用此端口，请为从语音帧到静音帧的转移概率参数选择**从输入端口指定语音到静音概率**。

**数据类型：** `single` | `double`
### 输出

### **P** — 语音存在的概率 标量 | 行向量

该模块输出一个标量或行向量，其列数与输入信号的列数相同。

在选择**输出噪声方差**参数之前，此端口未命名。

**数据类型：** `single` | `double`

### **N** — 每个频率 bin 的噪声方差估计 列向量 | 矩阵

该模块输出一个列向量或矩阵，其列数与输入信号的列数相同。

#### 依赖关系

要启用此端口，请选择**输出噪声方差**参数。

**数据类型：** `single` | `double`

## 参数

如果参数被列为可调，则您可以在仿真期间更改其值。

### **Domain of the input** — 输入的域 `Time`（默认）| `Frequency`

### **Window** — 在 FFT 之前应用的窗函数 `Hann`（默认）| `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular`

窗函数使用以下函数的算法设计：

- `Hann` –– `hann`
- `Chebyshev` –– `chebwin`
- `Flat Top` –– `flattopwin`
- `Hamming` –– `hamming`
- `Kaiser` –– `kaiser`

**可调：** 否

#### 依赖关系

要启用此参数，请将 **Domain of the input** 设置为 `Time`。

### **Sidelobe attenuation of the window (dB)** — 窗的旁瓣衰减（dB） `60`（默认）| 正有限标量

#### 依赖关系

要启用此参数，请将 **Domain of the input** 设置为 `Time`，并将 **Window** 设置为 `Chebyshev` 或 `Kaiser`。

**数据类型：** `single` | `double`

### **Inherit FFT length from input dimensions** — 将 FFT 长度设置为输入样本数 开（默认）| 关

**可调：** 否

#### 依赖关系

要启用此参数，请将 **Domain of the input** 设置为 `Time`。

### **FFT length** — 频域中的 bin 数 `1024`（默认）| 正整数

**可调：** 否

#### 依赖关系

要启用此参数，请将 **Domain of the input** 设置为 `Time`，并清除 **Inherit FFT length from input dimensions** 参数。

**数据类型：** `single` | `double`

### **Probability of transition from a silence frame to a speech frame** — 语音帧跟在静音帧之后的概率 `0.2`（默认）| 范围 [0,1] 内的标量

要从输入端口指定 **Probability of transition from a silence frame to a speech frame**，请选择 **Specify silence-to-speech probability from input port**。

**可调：** 是

**数据类型：** `single` | `double`

### **Probability of transition from a speech frame to a silence frame** — 静音帧跟在语音帧之后的概率 `0.1`（默认）| 范围 [0,1] 内的标量

要从输入端口指定 **Probability of transition from a speech frame to a silence frame**，请选择 **Specify speech-to-silence probability from input port**。

**可调：** 是

**数据类型：** `single` | `double`

### **Output noise variance** — 每个频率 bin 的噪声方差输出估计 `off`（默认）| `on`

当您选择此参数时，一个额外的输出端口 **N** 会添加到该模块。

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可减少启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。

**可调：** 否

## 所属库

Audio Toolbox / Measurements

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

**在 R2018a 中引入**

## 描述

检测音频信号中是否存在语音

Voice Activity Detector 模块检测音频信号中是否存在语音。您还可以使用 Voice Activity Detector 模块输出每个频率 bin 的噪声方差估计。
