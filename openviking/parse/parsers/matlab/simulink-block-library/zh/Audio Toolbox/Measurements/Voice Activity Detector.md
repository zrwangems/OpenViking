---
type: simulink-block
title: 'Voice Activity Detector'
family: 'measurements'
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
- 一维向量输入 —— 输入被视为单个通道。

除非您指定附加输入端口，否则该端口未命名。

**数据类型：** `single` | `double`

### **SilenceToSpeech** — 阈值 (dB) 标量，范围为 [0, 1]

#### 依赖关系

要启用此端口，请为 Probability of transition from a silence frame to a speech frame 参数选择 **Specify silence-to-speech probability from input port**。

**数据类型：** `single` | `double`

### **SpeechToSilence** — 阈值 (dB) 标量，范围为 [0, 1]

#### 依赖关系

要启用此端口，请为 Probability of transition from a speech frame to a silence frame 参数选择 **Specify speech-to-silence probability from input port**。

**数据类型：** `single` | `double`
### 输出

### **P** — 存在语音的概率 标量 | 行向量

该模块输出一个标量或行向量，其列数与输入信号相同。

该端口在您选择 **Output noise variance** 参数之前未命名。

**数据类型：** `single` | `double`

### **N** — 每个频率 bin 的噪声方差估计 列向量 | 矩阵

该模块输出一个列向量或矩阵，其列数与输入信号相同。

#### 依赖关系

要启用此端口，请选择 **Output noise variance** 参数。

**数据类型：** `single` | `double`

## 参数

如果某个参数被列为可调，则可以在仿真期间更改其值。

### **Domain of the input** — 输入的域 `Time` (default) | `Frequency`

### **Window** — 在 FFT 之前应用的窗函数 `Hann` (default) | `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular`

该窗函数使用以下函数的算法设计：

- `Hann` –– `hann`
- `Chebyshev` –– `chebwin`
- `Flat Top` –– `flattopwin`
- `Hamming` –– `hamming`
- `Kaiser` –– `kaiser`

**可调：** No

#### 依赖关系

要启用此参数，请将 **Domain of the input** 设置为 `Time`。

### **Sidelobe attenuation of the window (dB)** — 窗的旁瓣衰减 (dB) `60` (default) | 正有限标量

#### 依赖关系

要启用此参数，请将 **Domain of the input** 设置为 `Time`，并将 **Window** 设置为 `Chebyshev` 或 `Kaiser`。

**数据类型：** `single` | `double`

### **Inherit FFT length from input dimensions** — 将 FFT 长度设置为输入样本数 on (default) | off

**可调：** No

#### 依赖关系

要启用此参数，请将 **Domain of the input** 设置为 `Time`。

### **FFT length** — 频域中的 bin 数 `1024` (default) | 正整数

**可调：** No

#### 依赖关系

要启用此参数，请将 **Domain of the input** 设置为 `Time`，并清除 **Inherit FFT length from input dimensions** 参数。

**数据类型：** `single` | `double`

### **Probability of transition from a silence frame to a speech frame** — 语音帧跟随静音帧的概率 `0.2` (default) | [0,1] 范围内的标量

要从输入端口指定 **Probability of transition from a silence frame to a speech frame**，请选择 **Specify silence-to-speech probability from input port**。

**可调：** Yes

**数据类型：** `single` | `double`

### **Probability of transition from a speech frame to a silence frame** — 静音帧跟随语音帧的概率 `0.1` (default) | [0,1] 范围内的标量

要从输入端口指定 **Probability of transition from a speech frame to a silence frame**，请选择 **Specify speech-to-silence probability from input port**。

**可调：** Yes

**数据类型：** `single` | `double`

### **Output noise variance** — 每个频率 bin 的噪声方差的输出估计 `off` (default) | `on`

当您选择此参数时，模块会添加一个附加输出端口 **N**。

### **Simulate using** — 指定要运行的仿真类型 `Code generation` (default) | `Interpreted execution`

- `Code generation` – 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` – 使用 MATLAB® 解释器仿真模型。此选项可减少启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。

**可调：** No

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
