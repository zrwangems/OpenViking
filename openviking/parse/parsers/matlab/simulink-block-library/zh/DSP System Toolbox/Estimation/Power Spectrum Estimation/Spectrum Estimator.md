---
type: simulink-block
title: 'Spectrum Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Power Spectrum Estimation'
documentation_page: 'spectrumestimator'
documentation_source_path: 'ref/spectrumestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Spectrum Estimator

## 端口

### 输入

### **Input** — 输入信号 向量 | 矩阵

将输入信号指定为向量或矩阵。该模块将输入的每一列视为一个独立通道。如果输入是二维信号，第一维表示通道长度（或帧大小），第二维表示通道数。如果输入是一维信号，则将其解释为单通道。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **P** — 功率谱或功率密度谱 向量 | 矩阵

该模块估计的功率谱或功率密度谱，以向量或矩阵形式返回。

**数据类型：** `single` | `double`

### **P\_max** — 最大保持谱 向量 | 矩阵

最大保持谱，以向量或矩阵形式返回。该模块通过在每个频率 bin 处保留所有功率谱估计的最大值来计算最大保持谱。

**数据类型：** `single` | `double`

### **P\_min** — 最小保持谱 向量 | 矩阵

最小保持谱，以向量或矩阵形式返回。该模块通过在每个频率 bin 处保留所有功率谱估计的最小值来计算最小保持谱。

**数据类型：** `single` | `double`

### **F** — 输出频率 列向量

输出频率，以列向量形式返回。

**数据类型：** `single` | `double`

### **RBW** — 有效分辨率带宽 标量

有效分辨率带宽，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### 主选项卡

### **Method** — Welch 或滤波器组 `Filter bank`（默认）| `Welch`

将频谱估计方法指定为以下选项之一。

- `Filter bank` — 分析滤波器组将宽带输入信号拆分为多个窄子带。该模块计算每个窄频带内的功率，计算值即为相应频带上的频谱估计。
- `Welch` — 该模块使用 Welch 平均修正周期图法来计算窄子带上的功率谱。

### **Number of taps per band** — 每个频带的滤波器抽头数 `12`（默认）| 正整数

将每个频带的滤波器系数（或抽头）数指定为正整数。该值对应于每个多相分支的滤波器系数数量。滤波器系数总数为 **Number of taps per band** 乘以 FFT 长度。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Filter bank`。

### **Spectrum type** — 频谱类型 `Power`（默认）| `Power density`

将要计算的频谱类型指定为以下之一：

- `Power` — 计算功率谱。
- `Power density` — 计算功率谱密度。

### **Frequency resolution method** — 频率分辨率方法 `Auto`（默认）| `RBW` | `Number of frequency bands`

将频率分辨率方法指定为以下选项之一。

- `Auto` — Spectrum Estimator 模块计算分辨率带宽（RBW），使频率跨度容纳 1024 个 RBW 间隔。

  - Welch 方法 — 窗长度 *winLen* 使用 winLen=NENBW×Fs/RBW 计算。*NENBW* 是窗的等效噪声带宽，*Fs* 是采样率。
  - 滤波器组方法 — FFT 长度是 **Sample rate (Hz)** 与计算得到的分辨率带宽之比的上取整。
- `RBW` — 指定分辨率带宽，用于确定窗长度（Welch 方法）或 FFT 长度（滤波器组方法）。当该模块使用 Welch 方法时，其行为等同于 Spectrum Analyzer 模块。窗长度使用 winLen=NENBW×Fs/RBW 计算。*NENBW* 是窗的等效噪声带宽，*Fs* 是采样率。FFT 长度等于 **Sample rate (Hz)** 与 **RBW (Hz)** 之比的上取整。
- `Window length` — 指定 Welch 算法中使用的窗或段长度。当您将 **Method** 设置为 `Welch` 时，此选项可用。
- `Number of frequency bands` — 指定分析滤波器组的多相分支数。该值对应于滤波器组使用的 FFT 长度。要启用此选项，请将 **Method** 设置为 `Filter bank`。

### **RBW (Hz)** — 分辨率带宽 `5`（默认）| 正标量

将分辨率带宽指定为以 Hz 为单位的正标量。频率跨度与 RBW 之比的上取整必须大于 `2`。

#### 依赖关系

要启用此参数，请将 **Frequency resolution method** 设置为 `RBW`。

### **Window length source** — 窗长度来源 `Same as input frame length`（默认）| `Specify on dialog`

将窗长度值的来源指定为以下之一：

- `Same as input frame length` — 窗长度等于输入的帧大小。指定此选项可获得等同于 Periodogram 模块的行为。
- `Specify on dialog` — 窗长度为您在 **Window length** 参数中指定的值。

#### 依赖关系

要启用此参数，请设置

- **Method** 为 `Welch`。
- **Frequency resolution method** 为 `Window length`。

### **Window length** — 窗长度 `1024`（默认）| 正整数

将用于计算频谱估计的窗长度指定为大于 `2` 的正整数标量。

#### 依赖关系

要启用此参数，请设置

- **Method** 为 `Welch`。
- **Frequency resolution method** 为 `Window length`。
- **Window length source** 为 `Specify on dialog`。

### **Number of bands source** — 频带数来源 `Same as input frame size`（默认）| `Specify on dialog`

将频带数的来源指定为以下之一：

- `Same as input frame length` — FFT 长度等于输入的帧大小。
- `Specify on dialog` — FFT 长度为您在 **Number of bands** 中指定的值。

#### 依赖关系

要启用此参数，请设置

- **Method** 为 `Filter bank`。
- **Frequency resolution method** 为 `Number of frequency bands`。

### **Number of bands** — 频带数 `1024`（默认）| 正标量

将滤波器组用于计算功率谱估计的频带数或 FFT 长度指定为正标量。

#### 依赖关系

要启用此参数，请设置

- **Method** 为 `Filter bank`。
- **Frequency resolution method** 为 `Number of frequency bands`。
- **Number of bands source** 为 `Specify on dialog`。

### **FFT length source** — FFT 长度值来源 `Auto`（默认）| `Property`

将 FFT 长度值的来源指定为以下之一：

- `Auto` — 该模块将 FFT 长度设置为输入的帧大小。
- `Property` — 该模块将 FFT 长度设置为您在 **FFT length** 中指定的值。

#### 依赖关系

要启用此参数，请设置

- **Method** 为 `Welch`。
- **Frequency resolution method** 为 `Window length`。

### **FFT length** — FFT 长度 `1024`（默认）| 正整数

将 FFT 长度指定为正整数。该模块使用此值来计算频谱估计。

#### 依赖关系

要启用此参数，请设置

- **Method** 为 `Welch`。
- **Frequency resolution method** 为 `Window length`。
- **FFT length source** 为 `Property`。

### **Inherit sample rate from input** — 从输入继承采样率 `on`（默认）| `off`

当您选中此复选框时，模块算法将模块采样率计算为 *N*/*Ts*，其中 *N* 是输入信号的帧大小，*Ts* 是输入信号的采样时间。默认情况下，该模块从其输入信号继承采样率。当您清除此复选框时，模块采样率为您在 **Sample rate (Hz)** 中指定的值。

#### 依赖关系

要启用此参数，请执行以下操作之一：

- 将 **Method** 设置为 `Welch`，并将 **Frequency resolution method** 设置为 `Window length`。
- 将 **Method** 设置为 `Filter bank`，并将 **Frequency resolution method** 设置为 `Number of frequency bands`。

### **Sample rate (Hz)** — 输入采样率 `44100`（默认）| 标量

将输入信号的采样率指定为正标量。

#### 依赖关系

要启用此参数，请执行以下操作之一：

- 将 **Frequency resolution method** 设置为 `Auto` 或 `RBW`。
- 将 **Method** 设置为 `Welch`，将 **Frequency resolution method** 设置为 `Window length`，并清除 **Inherit sample rate from input** 复选框。
- 将 **Method** 设置为 `Filter bank`，将 **Frequency resolution method** 设置为 `Number of frequency bands`，并清除 **Inherit sample rate from input** 复选框。

### **Window function** — 窗函数 `Hann`（默认）| `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular`

将 Welch 算法使用的窗函数指定为 `Chebyshev`、`Flat Top`、`Hamming`、`Hann`、`Kaiser` 或 `Rectangular`。默认值为 `Hann`。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Welch`。

### **Sidelobe attenuation of window (dB)** — 窗的旁瓣衰减 `60`（默认）| 正标量

将窗的旁瓣衰减指定为以 dB 为单位、大于或等于 `45` 的正标量。

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Welch`，并将 **Window function** 设置为 `Chebyshev` 或 `Kaiser`。

### **Averaging method** — 平均方法 `Exponential`（默认）| `Running`

将平均方法指定为 `Exponential`（默认）或 `Running`。在指数方法中，该模块对样本进行加权平均，权重由指数衰减遗忘因子决定。在运行平均方法中，该模块对由 **Number of spectral averages** 参数指定数量的频谱估计计算等权平均。

### **Number of spectral averages** — 频谱平均次数 `1`（默认）| 正整数

将频谱平均次数指定为正整数。频谱估计器通过对最近 *N* 个功率谱估计求平均来计算当前功率谱估计，其中 *N* 是 **Number of spectral averages** 中定义的频谱平均次数。

#### 依赖关系

要启用此参数，请将 **Averaging method** 设置为 `Running`。

### **Specify forgetting factor from input port** — 从输入端口指定遗忘因子 `off`（默认）| `on`

选中此复选框以从输入端口指定遗忘因子。当您不选中此复选框时，必须通过 **Forgetting factor** 参数指定遗忘因子。

#### 依赖关系

要启用此参数，请将 **Averaging method** 设置为 `Exponential`。

### **Forgetting factor** — 遗忘因子 `0.9`（默认）| 范围 (`0,1`] 内的标量

将指数加权遗忘因子指定为大于 0 且小于或等于 1 的标量值。

#### 依赖关系

要启用此参数，请将 **Averaging method** 设置为 `Exponential`，并清除 **Specify forgetting factor from input port** 参数。

### 高级选项卡

### **Window overlap (%)** — 窗之间的重叠百分比 `0`（默认）

将连续数据窗之间的重叠百分比指定为 `0` 到 `100` 之间的标量。

#### 依赖关系

要启用此参数，请在 **Main Tab** 上将 **Method** 设置为 `Welch`。

### **Reference load (ohms)** — 参考负载 `1`（默认）| 正标量

将用于计算功率值的参考负载指定为以欧姆表示的实正标量。

### **Frequency range** — 频谱估计器的频率范围 `Centered`（默认）| `One-sided` | `Two-sided`

将频谱估计器的频率范围指定为以下之一：

- `Centered` — 频谱估计器计算复输入或实输入信号的中心双边谱。频谱估计的长度等于 FFT 长度。当 FFT 长度为偶数时，频谱估计在频率范围 (`-SampleRate/2 SampleRate/2`] 上计算；当 FFT 长度为奇数时，在 `(-SampleRate/2 SampleRate/2)` 上计算。
- `One-sided` — 频谱估计器计算实输入信号的单边谱。当 FFT 长度 `NFFT` 为偶数时，频谱估计的长度为 (`NFFT`/`2`) + `1`，并在频率范围 `[0 SampleRate/2]` 上计算。`SampleRate` 是输入信号的采样率。当 `NFFT` 为奇数时，频谱估计的长度为 (`NFFT` + 1)/`2`，并在频率范围 [`0 SampleRate/2`) 上计算。
- `Two-sided` — 频谱估计器计算复输入或实输入信号的双边谱。频谱估计的长度等于 FFT 长度。频谱估计在频率范围 [`0 SampleRate`) 上计算，其中 `SampleRate` 是输入信号的采样率。

### **Power units** — 功率单位 `dBm`（默认）| `Watts` | `dBW`

将用于测量功率的单位指定为以下之一：

- `dBm` — 频谱估计器以分贝毫瓦为单位测量功率。
- `Watts` — 频谱估计器以瓦特为单位测量功率。
- `dBW` — 频谱估计器以分贝瓦为单位测量功率。

### **Output max-hold spectrum** — 输出最大保持谱 `off`（默认）| `on`

当您选中此复选框时，该模块通过 **P\_max** 端口输出输入信号的最大保持谱。该模块通过在每个频率 bin 处保留所有功率谱估计的最大值来计算最大保持谱。默认情况下，此复选框未选中。

### **Output min-hold spectrum** — 输出最小保持谱 `off`（默认）| `on`

当您选中此复选框时，该模块通过 **P\_min** 端口输出输入信号的最小保持谱。该模块通过在每个频率 bin 处保留所有功率谱估计的最小值来计算最小保持谱。默认情况下，此复选框未选中。

### **Output frequency vector** — 输出频率向量 `off`（默认）| `on`

当您选中此复选框时，该模块通过 **F** 端口输出频率向量。默认情况下，此复选框未选中。

### **Output effective RBW** — 输出有效 RBW `off`（默认）| `on`

当您选中此复选框时，该模块计算并通过 **RBW** 端口输出有效分辨率带宽。默认情况下，此复选框未选中。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

将要运行的仿真类型指定为以下之一：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

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

**在 R2015b 中引入**

## 描述

估计功率谱或功率密度谱

Spectrum Estimator 模块使用平均修正周期图的 Welch 方法和滤波器组方法，输出实数或复数输入信号的功率谱或功率密度谱。

当您选择滤波器组方法时，该模块使用分析滤波器组来估计功率谱。与 Welch 方法相比，滤波器组方法产生的频谱估计具有更高的分辨率、更准确的噪声底和更精确的峰值，且频谱泄漏低或无频谱泄漏。其代价是计算量增加且跟踪速度变慢。

当您选择 Welch 方法时，该模块计算平均修正周期图以计算频谱估计。该模块将输入数据缓冲为重叠段。使用模块参数可设置数据段的长度、连续段之间的数据重叠量以及功率谱的其他特性。

有关 Welch 方法和滤波器组方法的更多信息，请参阅算法。
