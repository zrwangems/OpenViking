---
type: simulink-block
title: 'Mel Spectrogram'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Features'
documentation_page: 'melspectrogramblock'
documentation_source_path: 'ref/melspectrogramblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Mel Spectrogram

## 端口
```yaml
ports:
- name: Port_1
  summary: 音频输入列向量 | 矩阵
  direction: input
  data_types: single | double
- name: spec
  summary: 梅尔频谱图矩阵 | 三维数组
  direction: output
  data_types: single | double
- name: fvec
  summary: 中心频率行向量
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 音频输入列向量 | 矩阵

音频输入信号，指定为列向量或矩阵。当指定矩阵时，该模块将各列视为独立的音频通道。

**数据类型：** `single` | `double`
### 输出

### **spec** — 梅尔频谱图矩阵 | 三维数组

梅尔频谱图，以矩阵或三维数组形式返回。**spec** 的维度为
*L*×*M*×*N*，其中：

- *L* 是频谱数量，由 **Number of spectra**
  参数决定。
- *M* 是频带数量，由 **Number of bands**
  参数决定。
- *N* 是输入音频信号中的通道数。

输出中会移除末尾的单一维度。

在您选择 **Output center
frequencies** 参数之前，此端口没有名称。

**数据类型：** `single` | `double`

### **fvec** — 中心频率行向量

带通滤波器的中心频率，以 Hz 为单位，以行向量形式返回，其元素数量等于频带数量。

#### 依赖关系

要启用此端口，请选择 **Output frequency vector**
参数。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Number of bands
  summary: 带通滤波器数量 32（默认）| 正整数
  group: ''
- name: Auto-determine frequency range
  summary: 自动确定频率范围 on（默认）| off
  group: ''
- name: Frequency range (Hz)
  summary: 设计听觉滤波器组的频率范围 [0,22050]（默认）| 二元素行向量
  group: ''
- name: Filter bank design domain
  summary: 设计滤波器组的域 linear（默认）| warped
  group: ''
- name: Filter bank normalization
  summary: 滤波器组的归一化技术 bandwidth（默认）| area | none
  group: ''
- name: Mel style
  summary: 梅尔刻度风格 oshaughnessy（默认）| slaney
  group: ''
- name: Visualize filter bank
  summary: 打开绘图以可视化滤波器组 按钮
  group: ''
- name: Output frequency vector
  summary: 为中心频率指定附加输出端口 off（默认）| on
  group: ''
- name: Window
  summary: 分析窗 hamming(1024,'periodic')（默认）| 实数向量
  group: ''
- name: Normalize window
  summary: 归一化分析窗 on（默认）| off
  group: ''
- name: Overlap length
  summary: 相邻分析窗的重叠长度 512（默认）| 范围 [0, windowLength) 内的整数
  group: ''
- name: Auto-determine FFT length
  summary: 自动确定 FFT 长度 on（默认）| off
  group: ''
- name: FFT length
  summary: DFT 点数 1024（默认）| 正整数
  group: ''
- name: Spectrum type
  summary: 频谱类型 magnitude（默认）| power
  group: ''
- name: Number of spectra
  summary: 频谱数量 1（默认）| 正整数
  group: ''
- name: Number of spectra overlap
  summary: 重叠频谱数量 0（默认）| 范围 [0, Number of spectra) 内的整数。
  group: ''
- name: Apply logarithm
  summary: 应用对数 off（默认）| on
  group: ''
- name: Inherit sample rate from input
  summary: 指定输入采样率的来源 off（默认）| on
  group: ''
- name: Input sample rate (Hz)
  summary: 输入的采样率 44.1e3（默认）| 正标量
  group: ''
```

#### 滤波器组参数

### **Number of bands** — 带通滤波器数量 `32`（默认）| 正整数

带通滤波器数量，指定为正整数。

### **Auto-determine frequency range** — 自动确定频率范围 `on`（默认）| `off`

当您选择此参数时，该模块将 **Frequency range**
设置为 `[0,fs/2]`，其中 `fs` 是采样率。采样率由 **Inherit sample rate
from input** 和 **Input sample rate (Hz)**
参数决定。

### **Frequency range (Hz)** — 设计听觉滤波器组的频率范围 `[0,22050]`（默认）| 二元素行向量

设计听觉滤波器组的频率范围，以 Hz 为单位，指定为二元素行向量。

#### 依赖关系

要启用此参数，请清除 **Auto-determine frequency
range** 参数。

### **Filter bank design domain** — 设计滤波器组的域 `linear`（默认）| `warped`

该模块设计滤波器组所在的域，指定为
`linear` 或 `warped`。
将滤波器组设计域设置为 `linear` 以在
线性（Hz）域中设计带通滤波器。将滤波器组设计域设置为 `warped`
以在扭曲（梅尔）域中设计带通滤波器。

### **Filter bank normalization** — 滤波器组的归一化技术 `bandwidth`（默认）| `area` | `none`

用于滤波器组权重的归一化技术，指定为
`bandwidth`、`area`
或 `none`。

- `bandwidth` —— 按滤波器的相应带宽对
  每个带通滤波器的权重进行归一化。
- `area` —— 按带通滤波器的相应面积对
  每个带通滤波器的权重进行归一化。
- `none` —— 该模块不对滤波器权重
  进行归一化。

### **Mel style** — 梅尔刻度风格 `oshaughnessy`（默认）| `slaney`

梅尔刻度的风格，指定为 `oshaughnessy` 或
`slaney`。

### **Visualize filter bank** — 打开绘图以可视化滤波器组 按钮

打开绘图以在频域中可视化滤波器。

### **Output frequency vector** — 为中心频率指定附加输出端口 `off`（默认）| `on`

当您选择此参数时，该模块会显示一个附加输出
端口 **fvec**。此端口输出带通滤波器的中心频率。

#### 频谱图参数

### **Window** — 分析窗 `hamming(1024,'periodic')`（默认）| 实数向量

在时域中应用的分析窗，指定为实数
向量。

### **Normalize window** — 归一化分析窗 `on`（默认）| `off`

当您选择此参数时，该模块会应用窗
归一化。

### **Overlap length** — 相邻分析窗的重叠长度 `512`（默认）| 范围 [0, `windowLength`) 内的整数

相邻分析窗的重叠长度，指定为
范围 [0, `windowLength`) 内的整数，其中
`windowLength` 是分析窗的长度，
由 **Window** 指定。

### **Auto-determine FFT length** — 自动确定 FFT 长度 `on`（默认）| `off`

当您选择此参数时，该模块会自动将 FFT
长度设置为窗长度 `numel(Window)`。

### **FFT length** — DFT 点数 `1024`（默认）| 正整数

用于计算 DFT 的点数，指定为正
整数。

#### 依赖关系

要启用此参数，请清除 **Auto-determine FFT
length** 参数。

### **Spectrum type** — 频谱类型 `magnitude`（默认）| `power`

频谱类型，指定为 `magnitude` 或
`power`。

### **Number of spectra** — 频谱数量 `1`（默认）| 正整数

频谱图中的频谱数量，指定为正
整数。

### **Number of spectra overlap** — 重叠频谱数量 `0`（默认）| 范围 [0, **Number of spectra**) 内的整数。

连续频谱图之间重叠的频谱数量，指定为
范围 [0, **Number of spectra**) 内的整数

### **Apply logarithm** — 应用对数 `off`（默认）| `on`

当您选择此参数时，该模块会对
频谱图应用以 10 为底的对数。

#### 仿真参数

### **Inherit sample rate from input** — 指定输入采样率的来源 `off`（默认）| `on`

当您选择此参数时，该模块会从
输入信号继承其采样率。当您清除此参数时，您需要在
**Input sample rate (Hz)** 参数中指定采样率。

### **Input sample rate (Hz)** — 输入的采样率 `44.1e3`（默认）| 正标量

输入采样率，以 Hz 为单位，指定为实正标量。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from
input** 参数。
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

Mel Spectrogram 模块支持使用单指令多数据（SIMD）指令进行优化代码生成。有关 SIMD 代码生成的详细信息，请参阅 Generate SIMD Code from Simulink Blocks for Intel Platforms (Simulink Coder)。

## 版本历史

**在 R2022a 中引入**

### R2024a: 对频谱图应用对数

选择 **Apply logarithm** 参数以对频谱图应用以 10 为底
的对数。

### R2023b: 支持 Slaney 风格梅尔刻度

将 **Mel style** 参数设置为
`slaney` 以使用 Slaney 风格梅尔刻度。

### R2023a: 生成用于计算梅尔频谱图的优化 C/C++ 代码

Mel Spectrogram 模块支持使用单指令多数据（SIMD）指令进行优化 C/C++ 代码生成。

## 描述

从音频中提取梅尔频谱图

Mel Spectrogram 模块从音频输入信号中提取梅尔频谱图。梅尔
频谱图包含输入信号在梅尔频率刻度上的短期、时间局部化频率内容的估计。
