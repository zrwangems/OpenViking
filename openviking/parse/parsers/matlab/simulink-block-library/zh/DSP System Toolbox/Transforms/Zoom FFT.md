---
type: simulink-block
title: 'Zoom FFT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'zoomfft'
documentation_source_path: 'ref/zoomfft.html'
language: zh-CN
chinese_source: worker-translation
---

# Zoom FFT

## 端口

### 输入

### **x** — 输入数据向量 | 矩阵

用于计算 zoom FFT 的输入数据，指定为向量或矩阵。

该模块将输入信号的每一列视为一个独立通道。如果输入是二维信号，第一维表示通道长度（或帧大小），第二维表示通道数。如果输入是一维信号，则该模块将其解释为单通道信号。

当您输入可变大小信号（帧长度在仿真期间变化）时，信号的帧长度可以是任意的，即输入帧长度不必是抽取因子的整数倍。当您输入固定大小信号（帧长度在仿真期间不变）时，仅当您选中 **Allow arbitrary frame length for fixed-size input signals** 参数时，帧长度才可以任意。

在您选中 **Specify center frequency from input port** 参数并点击 **Apply** 之前，此端口未命名。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Fc** — 中心频率输入实数标量

所需频带的中心频率，指定为范围在 (– *Fs*/2, *Fs*/2) 内的实数标量，其中 *Fs* 是输入信号的采样率。如果您将 **Sample rate mode** 设置为 `Inherit from input port` 或 `Specify on dialog`，则该模块分别从输入信号继承 *Fs* 或使用 **Input sample rate (Hz)** 参数的值。如果您将 **Sample rate mode** 设置为 `Use normalized frequency (0 to 1)`，则该模块将 *Fs* 设置为 2 *(自 R2024b 起)*。

#### 依赖

要启用此端口，请选中 **Specify center frequency from input port** 复选框并点击 **Apply**。

**数据类型：** `single` | `double`
### 输出参数

### **Port\_1** — Zoom FFT 输出向量 | 矩阵

Zoom FFT 输出，以向量或矩阵形式返回。

如果您选中 **Inherit FFT Length from input dimensions** 复选框，则输出信号的维度取决于输入信号的维度、Zoom FFT 模块的抽取因子，以及您是否选中 **Allow arbitrary frame length for fixed-size input signals** 参数。

下表提供了当您输入固定大小输入信号时输出信号维度的更多详细信息。

**固定大小输入信号**

| 输入信号 | 输出信号维度 |
| --- | --- |
| *P*×1 列向量，其中 *P* 是抽取因子 *D* 的整数倍 | (*P*/*D*)×1 |
| *P*×1 列向量，其中 *P* 不是抽取因子 *D* 的整数倍 | 当您选中 **Allow arbitrary frame length for fixed-size input signals** 时，为 `ceil`(*P*/*D*)×1。如果您未选中 **Allow arbitrary frame length for fixed-size input signals**，则该模块报错。 |
| *P*×*Q* 矩阵，其中 *P* 是抽取因子 *D* 的整数倍 | (*P*/*D*)×*Q* |
| *P*×*Q* 矩阵，其中 *P* 不是抽取因子 *D* 的整数倍 | 当您选中 **Allow arbitrary frame length for fixed-size input signals** 时，为 `ceil`(*P*/*D*)×*Q*。如果您未选中 **Allow arbitrary frame length for fixed-size input signals**，则该模块报错。 |

下表给出了当您输入可变大小输入信号时输出信号维度的更多详细信息。当您输入可变大小信号（帧长度在仿真期间变化）时，**Allow arbitrary frame length for fixed-size input signals** 在模块对话框中可见，但对输入帧长度没有任何影响。即使您未选中 **Allow arbitrary frame length for fixed-size input signals** 参数，您也可以输入任意帧长度的可变大小信号。

**可变大小输入信号**

| 输入信号 | 输出信号维度 |
| --- | --- |
| *P*×*Q* | `ceil`(*P*/*D*)×*Q* |

如果您清除 **Inherit FFT Length from input dimensions** 复选框，则输出帧大小等于您在 **FFT length**(*L*) 参数中指定的值。

| 输入信号 | 输出信号维度 |
| --- | --- |
| *P*×*Q* | *L*×*Q* |

输出的数据类型与输入的数据类型相同。

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

### **Decimation factor** — 抽取因子 `2`（默认）| 正整数

将抽取因子指定为正整数。此值指定该模块对输入信号带宽进行缩减的因子。输入信号的行数必须是抽取因子的整数倍。

**示例：**
`4`

**示例：**
`8`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Specify center frequency from input port** — 从输入端口指定中心频率的标志 `'off'`（默认）| `'on'`

当您选中此选项并点击 **Apply** 时，输入端口 **Fc** 将出现在模块图标上。您可以通过此输入端口以标量形式传递中心频率。

### **Center frequency** — 中心频率 `0`（默认）| 实数标量

将所需频带的中心频率指定为以 Hz 为单位的实数标量或以归一化频率单位表示的实数标量 *(自 R2024b 起)*。中心频率必须在 (– *Fs*/2, *Fs*/2) 范围内，其中 *Fs* 是输入信号的采样率。如果您将 **Sample rate mode** 设置为 `Inherit from input port` 或 `Specify on dialog`，则该模块分别从输入信号继承 *Fs* 或使用 **Input sample rate (Hz)** 参数的值。如果您将 **Sample rate mode** 设置为 `Use normalized frequency (0 to 1)`，则该模块将 *Fs* 设置为 2 *(自 R2024b 起)*。

**示例：**
`0.5`

**示例：**
`10`

#### 依赖

此参数在您清除 **Specify center frequency from input port** 复选框时适用。

**数据类型：** `single` | `double`

### **Inherit FFT Length from input dimensions** — 从输入维度继承 FFT 长度的标志 `'on'`（默认）| `'off'`

当您选中此选项时，FFT 长度是输入帧大小（输入中的行数）与 **Decimation factor** 的比值。

### **FFT length** — FFT 长度 `64`（默认）| 正标量

将 FFT 长度指定为正整数。FFT 长度必须大于或等于帧大小（输入行数）与 **Decimation factor** 的比值。

**示例：** `24`

**示例：** `52`

#### 依赖

要启用此参数，请清除 **Inherit FFT Length from input dimensions** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认）| `Specify on dialog` | `Inherit from input port`

*自 R2024b 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)` —— 以归一化频率单位（0 到 1）指定所需频带的中心频率。
- `Specify on dialog` —— 在模块对话框中使用 **Input sample rate (Hz)** 参数指定输入采样率。
- `Inherit from input port` —— 该模块从输入信号继承采样率。

### **Input sample rate (Hz)** — 输入采样率 `44100`（默认）| 正实数标量

将输入采样率 *Fs* 指定为以 Hz 为单位的正实数标量。

**示例：** `44100`

**示例：** `48000`

#### 依赖

要启用此参数，请将 **Sample rate mode** 参数设置为 `Specify on dialog`。*(自 R2024b 起)*

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号的任意帧长度 `off`（默认）| `on`

*自 R2023a 起*

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是抽取因子的整数倍。该模块仅对固定大小输入信号使用此参数，如果输入具有可变大小，则忽略此参数。

当输入信号是可变大小信号时，该信号可以具有任意帧长度，即帧长度不必是抽取因子的整数倍。

对于固定大小输入信号，如果您：

- 选中 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是抽取因子的整数倍。如果输入不是抽取因子的整数倍，则输出通常是可变大小信号。因此，为了支持任意输入大小，该模块还必须支持可变大小操作，您可以通过选中 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该操作。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是抽取因子的整数倍。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `Yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2024b：支持归一化频率

当您将 **Sample rate mode** 参数设置为 `Use normalized frequency (0 to 1)` 时，您可以以归一化频率单位（0 到 1）指定所需频带的中心频率。

### R2023a：支持任意输入帧长度

当满足以下条件时，该模块支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（帧长度在仿真期间不变）且您选中 **Allow arbitrary frame length for fixed-size input signals** 参数。
- 输入信号是可变大小信号（帧长度在仿真期间变化）。

当该模块支持具有任意帧长度的输入信号时，输入帧长度不必是抽取因子的整数倍，且输出为可变大小信号。

## 描述

频谱一部分的高分辨率 FFT

Zoom FFT 模块计算信号在奈奎斯特区间内一部分频率上的快速傅里叶变换（FFT）。通过设置适当的抽取因子 *D* 和采样率 *Fs*，您可以选择要分析的频率带宽 *BW*，其中 *BW* = *Fs*/*D*。您还可以通过选择所需频带的中心频率，在奈奎斯特区间内选择要分析的特定频率范围。如果您将 **Sample rate mode** 设置为 `Use normalized frequency (0 to 1)`，则该模块将 *BW* 设置为 2/*D*。*(自 R2024b 起)*

信号的分辨率是 *Fs* 与 FFT 长度 (*L*) 的比值。使用 zoom FFT，您可以通过对较短信号计算小型 FFT，来保持对原始信号进行全尺寸 FFT 所能达到的相同分辨率。较短信号来自对原始信号的抽取。其优势在于能够计算短得多的 FFT，同时达到相同的分辨率。对于抽取因子 *D*，新的采样率 *Fsd* 为 *Fs*/*D*，新的帧大小（和 FFT 长度）为 *Ld* = *L*/*D*。抽取信号的分辨率为 *Fsd*/*Ld* = *Fs*/*L*。为了在较短的频带上获得更高的分辨率，请使用原始 FFT 长度 *L*，而不是抽取后的 FFT 长度 *Ld*。
