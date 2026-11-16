---
type: simulink-block
title: 'Periodogram'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Power Spectrum Estimation'
documentation_page: 'periodogram'
documentation_source_path: 'ref/periodogram.html'
language: zh-CN
chinese_source: worker-translation
---

# Periodogram

## 端口

### 输入

### **Port\_1** — 输入信号 向量 | 矩阵

输入信号，指定为向量或矩阵。

该模块将 *M*-by-*N* 矩阵输入视为来自 *N* 个独立通道的 *M* 个顺序时间采样。

**数据类型：** `single` | `double`
**复数支持：** Yes

### 输出

### **Port\_1** — 输出信号 向量 | 矩阵

输出信号，以向量或矩阵形式返回。

输出矩阵的每一列包含对应输入列在 *Nfft* 个等间隔频率点处的功率谱密度估计。频率点位于范围 [0,Fs) 内，其中 Fs 是信号的采样频率。

该模块为 *N* 个独立通道中的每一个计算单独的估计，并生成 *Nfft*-by-*N* 矩阵输出。

**数据类型：** `single` | `double`

## 参数

### **Measurement** — 测量类型 `Power spectral density`（默认）| `Mean-square spectrum`

指定该模块要执行的测量类型：`Power spectral density` 或 `Mean-square spectrum`。

**可调：** No

### **Window** — 窗类型 `Hamming`（默认）| `Bartlett` | `Blackman` | `Boxcar` | `Chebyshev` | `Hann` | `Hanning` | `Kaiser` | `Triang`

选择要应用的窗类型。

有关详细信息，请参阅 Window Function block 参考页。

**可调：** Yes

### **Beta** — Beta `5`（默认）| 标量

输入 Kaiser 窗的 β 参数。增大 **Beta** 会加宽显示频率幅度响应中的主瓣，并降低旁瓣的幅度。

有关更多详细信息，请参阅 Window Function block 参考页。

**可调：** Yes

#### 依赖关系

如果对于 `Window` 参数选择了 `Kaiser`，则此参数可见。

### **Window sampling** — 窗采样 `Symmetric`（默认）| `Periodic`

从列表中选择 `Symmetric` 或 `Periodic`。

有关更多详细信息，请参阅 Window Function block 参考页。

**可调：** Yes

#### 依赖关系

仅当将 `Window` 参数设置为 `Blackman`、`Hamming`、`Hann` 或 `Hanning` 之一时，此参数才可见。

### **FFT implementation** — FFT 实现 `Auto`（默认）| `Radix-2` | `FFTW`

将此参数设置为 `FFTW` 以支持任意长度的输入信号。该模块将使用 FFTW 实现生成的代码限制为 MATLAB® 主机计算机。

将此参数设置为 `Radix-2`，用于位反转处理、定点或浮点数据，或通过 Simulink® Coder™ 进行可移植 C 代码生成。输入矩阵的第一维 *M* 必须是 2 的幂。要处理其他输入大小，请使用 Pad block 将这些维度填充或截断为 2 的幂，或者如果可能，选择 FFTW 实现。

将此参数设置为 `Auto`，以使该模块选择 FFT 实现。对于非 2 的幂的变换长度，该模块将生成的代码限制为 MATLAB 主机计算机。

**可调：** No

### **Stopband attenuation in dB** — 阻带衰减（以 dB 为单位） `50`（默认）| 标量

输入 Chebyshev 窗的阻带衰减电平 Rs（以分贝 (dB) 为单位）。

**可调：** Yes

#### 依赖关系

如果对于 `Window` 参数选择了 `Chebyshev`，则此参数可见。

### **Inherit FFT length from input dimensions** — 继承 FFT 长度 `off`（默认）| `on`

选中此复选框时，该模块将输入帧大小用作执行 FFT 的数据点数 *Nfft*。要指定执行 FFT 的点数，请清除 **Inherit FFT length from input dimensions** 复选框。然后，可以使用 FFT length 参数指定 2 的幂的 FFT 长度。

**可调：** No

### **FFT length** — 数据点数 `256`（默认）| 标量

输入执行 FFT 的数据点数 *Nfft*。当 *Nfft* 大于输入帧大小时，该模块根据需要为每个帧补零。当 *Nfft* 小于输入帧大小时，该模块根据需要环绕每个帧。

当将 `FFT implementation` 参数设置为 `Radix-2` 时，此值必须是 2 的幂。

**可调：** No

#### 依赖关系

仅当清除 Inherit FFT length from input dimensions 复选框时，此参数才可见。

### **Number of spectral averages** — 频谱平均次数 `4`（默认）| 标量

指定要平均的频谱数量。当将此值设置为 `1` 时，该模块计算输入的周期图。当将此值设置为大于 `1` 时，该模块实现 Welch 方法以计算输入的修正周期图。

**可调：** No

### **Inherit sample time from input** — 继承采样时间 `on`（默认）| `off`

如果选中 **Inherit sample time from input** 复选框，则该模块根据输入信号的采样周期计算频率数据。为使该模块产生有效输出，必须满足以下条件：

- 该模块的输入是原始信号，未添加或删除任何采样（例如，通过插入零）。
- 仿真中时域信号的采样周期等于原始时间序列的采样周期。

如果这些条件不成立，请清除 **Inherit sample time from input** 复选框。然后，可以使用 `Sample time of original time series` 参数指定采样时间。

#### 依赖关系

仅当将 `Measurement` 参数设置为 `Power spectral density` 时，此参数才可见。

### **Sample time of original time series** — 原始时间序列的采样时间 `1`（默认）| 标量

指定原始时域信号的采样时间。

**可调：** No

#### 依赖关系

仅当清除 `Inherit sample time from input` 复选框时，此参数才可见。

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

使用说明和限制：

- 生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。
- 当以下条件适用时，由该模块生成的可执行文件依赖 MATLAB 附带的预构建动态库文件（`.dll` 文件）：

  - **FFT implementation** 设置为 `FFTW`。
  - 清除 **Inherit FFT length from input dimensions**，并且 **FFT length** 设置为不是 2 的幂的值。

  使用 `packNGo` 函数将由此模块生成的代码以及所有相关文件打包到一个压缩 zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的另一开发环境中重定位、解包并重新构建您的项目。有关更多详细信息，请参阅如何在 MATLAB 外部运行生成的可执行文件。

- 当 FFT 长度为 2 的幂时，可以从此模块生成独立的 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用周期图法估计功率谱密度或均方谱

Periodogram 模块估计输入的功率谱密度 (PSD) 或均方谱 (MSS)。该模块使用周期图法和 Welch 平均修正周期图法。该模块对在输入的加窗片段上计算的 FFT 函数的平方幅度进行平均。然后，它用窗样本之和的平方对频谱平均值进行归一化。有关更多信息，请参阅 Periodogram 和 Welch 方法。
