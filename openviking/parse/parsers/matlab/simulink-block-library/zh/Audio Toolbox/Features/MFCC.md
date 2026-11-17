---
type: simulink-block
title: 'MFCC'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Features'
documentation_page: 'mfccblock'
documentation_source_path: 'ref/mfccblock.html'
language: zh-CN
chinese_source: worker-translation
---

# MFCC

## 端口

### 输入

### **Port\_1** — 音频输入列向量 | 矩阵

音频输入信号，指定为列向量或矩阵。当指定矩阵时，模块将各列视为独立的音频通道。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — MFCC 特征矩阵 | 三维数组

返回的 MFCC 特征，以矩阵或三维数组形式表示。特征包括 MFCC 本身，并可选择包含 MFCC 的 delta 和 delta-delta 特征。输出的维度为
*L*-by-*M*-by-*N*，其中：

- *L* 是特征向量的数量，由 **Number of
  feature vectors** 参数指定。
- *M* 是每个特征向量中的特征数量，由 **Number of
  cepstral coefficients**、**Append
  delta** 和 **Append
  delta-delta** 参数决定。
- *N* 是输入音频信号中的通道数。

输出中大小为 1 的尾部维度将被移除。

**数据类型：** `single` | `double`

## 参数

#### Mel-Frequency Cepstral Coefficients

### **Window** — 分析窗 `hamming(1024,'periodic')`（默认）| 实向量

在时域中应用于输入信号的分析窗，指定为实向量。

### **Overlap length** — 相邻窗之间重叠样本的数量 `512`（默认）| 范围 [0, `windowLength`) 内的整数

相邻窗之间重叠样本的数量，指定为范围 [0, `windowLength`) 内的整数，其中 `windowLength` 是分析窗的长度，由 **Window**
参数指定。

### **Number of cepstral coefficients** — 每个特征向量中倒谱系数的数量 `13`（默认）| 大于 1 的正整数

每个特征向量中倒谱系数的数量，指定为大于 1 的正整数。

### **Rectification** — 非线性整流的类型 `Logarithm`（默认）| `Cubic root`

在离散余弦变换之前应用于频谱的非线性整流的类型，指定为 `Logarithm` 或 `Cubic
root`。

### **Append delta** — 将 MFCC 的 delta 附加到特征向量 `on`（默认）| `off`

选中此参数时，模块将 MFCC 的 delta 附加到每个特征向量中的系数上。delta 是 MFCC 关于时间的一阶导数的近似值。delta 特征的数量等于 MFCC 的数量，由 **Number of cepstral
coefficients** 指定。

### **Append delta-delta** — 将 MFCC 的 delta-delta 附加到特征向量 `on`（默认）| `off`

选中此参数时，模块将 MFCC 的 delta-delta 附加到每个输出特征向量上。delta-delta 是 MFCC 关于时间的二阶导数的近似值。delta-delta 特征的数量等于 MFCC 的数量，由 **Number of cepstral
coefficients** 指定。

如果同时选中 **Append delta** 参数，模块会在特征向量中将 delta-delta 附加在 delta 之后。

### **Delta window length** — 用于计算 delta 和 delta-delta 的系数数量 `9`（默认）| 大于 2 的奇数

用于计算 delta 和 delta-delta 的系数数量，指定为大于 2 的奇数。

#### Output Buffering

### **Number of feature vectors** — 输出中 MFCC 特征向量的数量 `1`（默认）| 正整数

输出中 MFCC 特征向量的数量，指定为正整数。模块对输出进行缓冲以返回指定数量的特征向量。

### **Number of overlapped feature vectors** — 输出中重叠的特征向量数量 `0`（默认）| 非负整数

模块在输出中重叠的特征向量数量，指定为小于 **Number of feature vectors** 的非负整数。

#### Simulation Parameters

### **Inherit sample rate from input** — 指定输入采样率的来源 `off`（默认）| `on`

选中此参数时，模块从输入信号继承其采样率。清除此参数时，在 **Input sample rate (Hz)** 参数中指定采样率。

### **Input sample rate (Hz)** — 输入的采样率 `44.1e3`（默认）| 正标量

输入的采样率，以 Hz 为单位，指定为正标量。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from
input** 参数。

#### Mel Filter Bank Design

### **Number of bands** — mel 滤波器组中的频带数量 `32`（默认）| 正整数

mel 滤波器组中的频带数量，指定为正整数。

### **Auto-determine frequency range** — 自动确定频率范围 `on`（默认）| `off`

选中此参数时，模块将 **Frequency
range** 设置为 `[0,fs/2]`，其中 `fs` 是采样率。模块使用 **Inherit sample
rate from input** 和 **Input sample rate (Hz)**
参数确定采样率。

### **Frequency range (Hz)** — mel 滤波器组的频率范围 `[0,22050]`（默认）| 二元素行向量

mel 滤波器组的频率范围，以 Hz 为单位，指定为二元素行向量。

#### 依赖关系

要启用此参数，请清除 **Auto-determine frequency
range** 参数。

### **Filter bank design domain** — mel 滤波器组的设计域 `linear`（默认）| `warped`

mel 滤波器组的设计域，指定为 `linear` 或
`warped`。

### **Filter bank normalization** — 滤波器组的归一化技术 `bandwidth`（默认）| `area` | `none`

模块用于滤波器组权重的归一化技术，指定为 `bandwidth`、`area` 或
`none`。

- `bandwidth` –– 按滤波器的相应带宽对每个带通滤波器的权重进行归一化。
- `area` –– 按带通滤波器的相应面积对每个带通滤波器的权重进行归一化。
- `none` –– 模块不对滤波器的权重进行归一化。

### **Mel style** — Mel 风格 `oshaughnessy`（默认）| `slaney`

mel 刻度的风格，指定为 `oshaughnessy` 或
`slaney`。

#### Spectrogram

### **Normalize window** — 归一化分析窗 `on`（默认）| `off`

选中此参数时，模块应用窗归一化。

### **Spectrum type** — 频谱类型 `power`（默认）| `magnitude`

频谱类型，指定为 `power` 或
`magnitude`。

### **Auto-determine FFT length** — 自动确定 FFT 长度 `on`（默认）| `off`

选中此参数时，模块自动将 FFT 长度设置为窗长度。窗长度由 **Window**
参数确定。

### **FFT length** — DFT 点数 `1024`（默认）| 正整数

用于计算 DFT 的点数，指定为正整数。

#### 依赖关系

要启用此参数，请清除 **Auto-determine FFT length**
参数。

## 所属库

Audio Toolbox / Features

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

MFCC 模块支持使用单指令多数据（SIMD）指令进行优化代码生成。有关 SIMD 代码生成的详细信息，请参阅 Generate SIMD Code from Simulink Blocks for Intel Platforms (Simulink Coder)。

## 版本历史

**在 R2022b 中引入**

### R2023b：支持 Slaney 风格 mel 刻度

将 **Mel style** 参数设置为 `slaney` 以使用 Slaney 风格 mel 刻度。

### R2023a：生成用于计算 MFCC 的优化 C/C++ 代码

MFCC 模块支持使用单指令多数据（SIMD）指令进行优化 C/C++ 代码生成。

## 描述

从音频中提取梅尔频率倒谱系数

MFCC 模块从音频输入信号中提取包含梅尔频率倒谱系数（MFCC）及其 delta 和 delta-delta 特征的特征向量。MFCC 是从语音信号中提取的常用特征，用于分类任务。
