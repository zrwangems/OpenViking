---
type: simulink-block
title: 'Cross-Spectrum Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Power Spectrum Estimation'
documentation_page: 'crossspectrumestimator'
documentation_source_path: 'ref/crossspectrumestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Cross-Spectrum Estimator

## 端口
```yaml
ports:
- name: x
  summary: 第一个数据输入 向量 | 矩阵
  direction: input
  data_types: double | single
- name: y
  summary: 第二个数据输入 向量 | 矩阵
  direction: input
  data_types: double | single
- name: Output
  summary: 互功率谱密度 向量 | 矩阵
  direction: output
  data_types: double | single
```

### 输入

### **x** — 第一个数据输入 向量 | 矩阵

将第一个数据输入指定为向量或矩阵。该模块将输入信号的每一列视为单独的通道。如果输入是二维信号，则第一个维度表示通道长度（或帧大小），第二个维度表示通道数。如果输入是一维信号，则该模块将其解释为单通道信号。

输入 *x* 和 *y* 必须具有相同的大小和数据类型。

**数据类型：** `double` | `single`
**复数支持：** 是

### **y** — 第二个数据输入 向量 | 矩阵

将第二个数据输入指定为向量或矩阵。该模块将输入信号的每一列视为单独的通道。如果输入是二维信号，则第一个维度表示通道长度（或帧大小），第二个维度表示通道数。如果输入是一维信号，则该模块将其解释为单通道信号。

输入 *x* 和 *y* 必须具有相同的大小和数据类型。

**数据类型：** `double` | `single`
**复数支持：** 是
### 输出

### **Output** — 互功率谱密度 向量 | 矩阵

由该模块估计的互功率谱密度，以向量或矩阵形式返回。输出与输入信号具有相同的大小和数据类型。

**数据类型：** `double` | `single`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Window length source
  summary: 窗长度来源 Same as input frame length（默认）| Specify on dialog
  group: ''
- name: Window length
  summary: 窗长度（以采样为单位） 1024（默认）| 正整数
  group: ''
- name: Window overlap (%)
  summary: 窗之间的重叠百分比 0（默认）| [0,100) 范围内的标量
  group: ''
- name: Averaging method
  summary: 平均方法 Running（默认）| Exponential
  group: ''
- name: Specify forgetting factor from input port
  summary: 从输入端口指定遗忘因子 off（默认）| on
  group: ''
- name: Forgetting factor
  summary: 指数加权遗忘因子 0.9（默认）| (0,1] 范围内的标量
  group: ''
- name: Number of spectral averages
  summary: 频谱平均次数 1（默认）| 正整数
  group: ''
- name: FFT length source
  summary: FFT 长度值的来源 Auto（默认）| Property
  group: ''
- name: FFT length
  summary: FFT 长度 128（默认）| 正整数
  group: ''
- name: Window function
  summary: 窗函数 Hann（默认）| Chebyshev | Flat Top | Hamming | Kaiser | Rectangular
  group: ''
- name: Sidelobe attenuation of window (dB)
  summary: 窗的旁瓣衰减（dB） 60（默认）| 正标量
  group: ''
- name: Frequency range
  summary: 互频谱估计的频率范围 Centered（默认）| One-sided | Two-sided
  group: ''
- name: Inherit sample rate from input
  summary: 从输入继承采样率 on（默认）| off
  group: ''
- name: Sample rate (Hz)
  summary: 输入的采样率 44100（默认）| 正标量
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Window length source** — 窗长度来源 `Same as input frame length`（默认）| `Specify on dialog`

将窗长度值的来源指定为以下之一：

- `Same as input frame length`（默认）— 窗长度等于输入的帧大小。
- `Specify on dialog` — 窗长度为 **Window length** 中指定的值。

### **Window length** — 窗长度（以采样为单位） `1024`（默认）| 正整数

将模块用于计算频谱估计的窗长度（以采样为单位）指定为大于 `2` 的正整数。

#### 依赖关系

要启用此参数，请将 **Window length source** 设置为 `Specify on dialog`。

### **Window overlap (%)** — 窗之间的重叠百分比 `0`（默认）| [`0`,`100`) 范围内的标量

将连续数据窗之间的重叠百分比指定为 [`0`,`100`) 范围内的标量。

### **Averaging method** — 平均方法 `Running`（默认）| `Exponential`

将平均方法指定为：

- `Running` —— 在运行平均方法中，该模块计算由 **Number of spectral averages** 参数指定的频谱估计数量的等权平均值。
- `Exponential` —— 在指数方法中，该模块计算以指数衰减遗忘因子加权的样本平均值。

### **Specify forgetting factor from input port** — 从输入端口指定遗忘因子 `off`（默认）| `on`

选中此复选框以从输入端口指定遗忘因子。如果不选中此复选框，则必须在模块对话框中通过 **Forgetting factor** 参数指定遗忘因子。

#### 依赖关系

要启用此参数，请将 **Averaging method** 设置为 `Exponential`。

### **Forgetting factor** — 指数加权遗忘因子 `0.9`（默认）| (`0`,`1`] 范围内的标量

将指数加权遗忘因子指定为 (`0`,`1`] 范围内的标量。

#### 依赖关系

要启用此参数，请将 **Averaging method** 设置为 `Exponential`，并清除 **Specify forgetting factor from input port** 参数。

### **Number of spectral averages** — 频谱平均次数 `1`（默认）| 正整数

将频谱平均次数指定为正整数。频谱估计器通过对最后 *N* 个功率谱估计求平均来计算当前功率谱估计，其中 *N* 是 **Number of spectral averages** 中定义的频谱平均次数。

#### 依赖关系

要启用此参数，请将 **Averaging method** 设置为 `Running`。

### **FFT length source** — FFT 长度值的来源 `Auto`（默认）| `Property`

将 FFT 长度值的来源指定为以下之一：

- `Auto` — FFT 长度等于输入的帧大小。
- `Property` — FFT 长度为在 **FFT length** 参数中指定的值。

### **FFT length** — FFT 长度 `128`（默认）| 正整数

将模块用于计算频谱估计的 FFT 长度指定为正整数。

#### 依赖关系

要启用此参数，请将 **FFT length source** 设置为 `Property`。

### **Window function** — 窗函数 `Hann`（默认）| `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular`

将互频谱估计器的窗函数指定为 `Chebyshev`、`Flat Top`、`Hamming`、`Hann`、`Kaiser` 或 `Rectangular`。默认值为 `Hann`。

### **Sidelobe attenuation of window (dB)** — 窗的旁瓣衰减（dB） `60`（默认）| 正标量

将窗的旁瓣衰减指定为以 dB 为单位的正标量。

#### 依赖关系

要启用此参数，请将 **Window function** 设置为 `Chebyshev` 或 `Kaiser`。

### **Frequency range** — 互频谱估计的频率范围 `Centered`（默认）| `One-sided` | `Two-sided`

将互频谱估计器的频率范围指定为以下之一：

- `Centered` — 互频谱估计器计算复数或实数输入信号 *x* 和 *y* 的中心双边频谱。互频谱估计的长度等于 FFT 长度。该模块在频率范围 [`-SampleRate/2 SampleRate/2`] 上计算频谱估计，其中 `SampleRate` 是输入信号的采样率。
- `One-sided` — 互频谱估计器计算实数输入信号 *x* 和 *y* 的单边频谱。当 FFT 长度 *NFFT* 为偶数时，互频谱估计的长度为 (*NFFT*/ `2`) + `1`，并在频率范围 [`0 SampleRate/2`] 上计算。当 FFT 长度 *NFFT* 为奇数时，互频谱估计的长度为 (*NFFT* + 1)/ `2`，并在频率范围 [`0 SampleRate/2`] 上计算。
- `Two-sided` — 互频谱估计器计算复数或实数输入信号 *x* 和 *y* 的双边频谱。互频谱估计的长度等于 FFT 长度。频谱估计在频率范围 [`0 SampleRate`] 上计算。

### **Inherit sample rate from input** — 从输入继承采样率 `on`（默认）| `off`

选中此复选框时，该模块将采样率计算为 *N*/*Ts*，其中 *N* 是输入信号的帧大小，*Ts* 是输入信号的采样时间。清除此复选框时，该模块使用在 **Sample rate (Hz)** 中指定的值。默认情况下，此复选框处于选中状态。

### **Sample rate (Hz)** — 输入的采样率 `44100`（默认）| 正标量

将输入信号的采样率指定为正标量。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 复选框。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

将要运行的仿真类型指定为以下之一：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，C 代码将复用于后续仿真。此选项需要额外的启动时间，但可提供更快的后续仿真。
## 所属库

DSP System Toolbox / Estimation / Power Spectrum Estimation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

估计互功率谱密度

Cross-Spectrum Estimator 模块使用 Welch 的平均修正周期图法估计两个输入信号 *x* 和 *y* 的互功率谱密度。该模块将输入数据缓冲为重叠段。您可以通过模块对话框中的参数设置数据段的长度以及段之间的数据重叠量。该模块使用 **Averaging method** 参数中指定的方法对先前的功率谱估计求平均，从而计算当前功率谱估计。
