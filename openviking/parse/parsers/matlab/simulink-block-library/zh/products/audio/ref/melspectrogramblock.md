---
type: simulink-block
title: 'Mel Spectrogram'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'AI for Audio / Feature Extraction'
documentation_page: 'melspectrogramblock'
documentation_source_path: 'ref/melspectrogramblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Mel Spectrogram

## 端口

### 输入

### **Port\_1** — 音频输入列向量 | 矩阵

音频输入信号，指定为列向量或矩阵。当指定矩阵时，模块将各列视为独立的音频通道。

**Data Types:** `single` | `double`
### 输出

### **spec** — Mel 频谱图矩阵 | 三维数组

Mel 频谱图，返回为矩阵或三维数组。**spec** 的维度为
*L*×*M*×*N*，其中：

- *L* 是频谱的数量，由 **Number of spectra**
  参数确定。
- *M* 是频带的数量，由 **Number of bands**
  参数确定。
- *N* 是输入音频信号中的通道数。

输出中会删除末尾的单一维度。

在选择 **Output center frequencies** 参数之前，此端口未命名。

**Data Types:** `single` | `double`

### **fvec** — 中心频率行向量

带通滤波器的中心频率，以 Hz 为单位，返回为行向量，其元素数量等于频带数量。

#### 依赖项

要启用此端口，请选择 **Output frequency vector**
参数。

**Data Types:** `single` | `double`

## 参数

#### 滤波器组参数

### **Number of bands** — 带通滤波器的数量 `32`（默认）| 正整数

带通滤波器的数量，指定为正整数。

### **Auto-determine frequency range** — 自动确定频率范围 `on`（默认）| `off`

选择此参数时，模块将 **Frequency range**
设置为 `[0,fs/2]`，其中 `fs` 是采样率。采样率由 **Inherit sample rate
from input** 和 **Input sample rate (Hz)**
参数确定。

### **Frequency range (Hz)** — 用于设计听觉滤波器组的频率范围 `[0,22050]`（默认）| 二元素行向量

用于设计听觉滤波器组的频率范围，以 Hz 为单位，指定为二元素行向量。

#### 依赖项

要启用此参数，请清除 **Auto-determine frequency
range** 参数。

### **Filter bank design domain** — 设计滤波器组的域 `linear`（默认）| `warped`

模块设计滤波器组所在的域，指定为
`linear` 或 `warped`。
将滤波器组设计域设置为 `linear` 以
在 linear (Hz) 域中设计带通滤波器。将滤波器组
设计域设置为 `warped` 以在 warped
(mel) 域中设计带通滤波器。

### **Filter bank normalization** — 滤波器组的归一化方法 `bandwidth`（默认）| `area` | `none`

用于滤波器组权重的归一化方法，指定为
`bandwidth`、`area`
或 `none`。

- `bandwidth` –– 按滤波器对应的带宽对
  每个带通滤波器的权重进行归一化。
- `area` –– 按带通滤波器对应的面积对
  每个带通滤波器的权重进行归一化。
- `none` –– 模块不
  对滤波器的权重进行归一化。

### **Mel style** — Mel 样式 `oshaughnessy`（默认）| `slaney`

mel 尺度的样式，指定为 `oshaughnessy` 或
`slaney`。

### **Visualize filter bank** — 打开绘图以可视化滤波器组 按钮

打开绘图以在频域中可视化滤波器。

### **Output frequency vector** — 为中心频率指定额外输出端口 `off`（默认）| `on`

选择此参数时，模块会显示一个额外的输出
端口，**fvec**。此端口输出
带通滤波器的中心频率。

#### 频谱图参数

### **Window** — 分析窗 `hamming(1024,'periodic')`（默认）| 实数向量

在时域中应用的分析窗，指定为实数
向量。

### **Normalize window** — 归一化分析窗 `on`（默认）| `off`

选择此参数时，模块会应用窗
归一化。

### **Overlap length** — 相邻分析窗的重叠长度 `512`（默认）| [0, `windowLength`) 范围内的整数

相邻分析窗的重叠长度，指定为
范围 [0, `windowLength`) 内的整数，其中
`windowLength` 是分析窗的长度，
由 **Window** 指定。

### **Auto-determine FFT length** — 自动确定 FFT 长度 `on`（默认）| `off`

选择此参数时，模块会自动将 FFT
长度设置为窗长度，`numel(Window)`。

### **FFT length** — DFT 点数 `1024`（默认）| 正整数

用于计算 DFT 的点数，指定为正整数。

#### 依赖项

要启用此参数，请清除 **Auto-determine FFT
length** 参数。

### **Spectrum type** — 频谱类型 `magnitude`（默认）| `power`

频谱类型，指定为 `magnitude` 或
`power`。

### **Number of spectra** — 频谱数量 `1`（默认）| 正整数

频谱图中的频谱数量，指定为正整数。

### **Number of spectra overlap** — 重叠频谱数量 `0`（默认）| [0, **Number of spectra**) 范围内的整数。

连续频谱图之间重叠的频谱数量，指定为
范围 [0, **Number of spectra**) 内的整数

### **Apply logarithm** — 应用对数 `off`（默认）| `on`

选择此参数时，模块会对频谱图应用以 10 为底的对数。

#### 仿真参数

### **Inherit sample rate from input** — 指定输入采样率的来源 `off`（默认）| `on`

选择此参数时，模块从输入信号继承采样率。清除此参数时，您需要在 **Input sample rate (Hz)** 参数中指定采样率。

### **Input sample rate (Hz)** — 输入采样率 `44.1e3`（默认）| 正标量

输入采样率，以 Hz 为单位，指定为实数正标量。

#### 依赖项

要启用此参数，请清除 **Inherit sample rate from
input** 参数。

## 所属库

Audio Toolbox / Features

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Mel Spectrogram 模块支持使用单指令多数据 (SIMD) 指令进行优化的代码生成。有关 SIMD 代码生成的详细信息，请参阅 Generate SIMD Code from Simulink Blocks for Intel Platforms (Simulink Coder)。

## 版本历史

**在 R2022a 中引入**

### R2024a: 对频谱图应用对数

选择 **Apply logarithm** 参数以对频谱图应用以 10 为底的对数。

### R2023b: 支持 Slaney 样式 mel 尺度

将 **Mel style** 参数设置为
`slaney` 以使用 Slaney 样式的 mel 尺度。

### R2023a: 为计算 mel 频谱图生成优化的 C/C++ 代码

Mel Spectrogram 模块支持使用单指令多数据 (SIMD) 指令进行优化的 C/C++ 代码生成。

## 描述

从音频中提取 mel 频谱图

Mel Spectrogram 模块从音频输入信号中提取 mel 频谱图。mel
频谱图包含输入信号在 mel 频率尺度上的短期、时间局部化频率内容的估计。
