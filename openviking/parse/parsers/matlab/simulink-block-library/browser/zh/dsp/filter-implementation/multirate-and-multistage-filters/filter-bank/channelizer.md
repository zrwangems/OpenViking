---
type: simulink-block
title: 'Channelizer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Multirate and Multistage Filters / Filter Bank'
documentation_page: 'channelizer'
documentation_source_path: 'ref/channelizer.html'
language: zh-CN
chinese_source: worker-translation
---

# Channelizer

## 端口

### 输入

### **x** — 宽带信号 *L*×1 列向量 | *L*×*N* 矩阵

指定 Channelizer 模块将其拆分为多个窄带的输入宽带信号。

- 当输入可变大小信号（仿真期间帧长度发生变化）时，信号的帧长度可以是任意的，也就是说，输入帧长度不必是抽取因子的整数倍。
- 当输入固定大小信号（仿真期间帧长度不发生变化）时，只有当你选择 **Allow arbitrary frame length for fixed-size input signals** 参数时，帧长度才可以是任意的。

在将 **Polyphase filter specification** 设置为 `Coefficients` 并选择 **Specify coefficients from input port** 参数之前，此端口没有名称。

**数据类型：** `single` | `double`
**复数支持：** 是

### **coeffs** — 原型低通滤波器系数行向量

原型低通滤波器的系数。每个频带至少必须有一个系数。如果低通滤波器的长度小于频带数量，该模块会对系数进行零填充。

如果指定复数系数，该模块会设计一个中心位于非零频率的原型滤波器，也称为带通滤波器。原型带通滤波器的调制版本相对于原型滤波器出现，并环绕在频率范围 [−*F*s
*F*s] 内。

#### 依赖项

当你将 **Polyphase filter specification** 设置为 `Coefficients` 并选择 **Specify coefficients from input port** 参数时，此端口会出现。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Output(s)** — 多个窄带信号 向量 | 矩阵 | 三维数组

输入宽带信号的多个窄子带，以向量、矩阵或三维数组形式返回。输出端口数量以及每个端口的维度取决于输入信号的维度以及是否选择 **Bands as separate output ports (Max. of 16 bands)** 参数。*(自 R2024a 起)*

当你选择 **Bands as separate output ports (Max. of 16 bands)** 参数时，该模块在单独端口输出每个窄带信号。输出端口数量在 [1 `min`(**Number of frequency bands**, 16)] 范围内。当你清除 **Bands as separate output ports (Max. of 16 bands)** 参数时，该模块将每个窄带信号作为输出数组中的单独列输出，并在单个输出端口输出该数组。*(自 R2024a 起)*

下表提供了当你输入固定大小输入信号（仿真期间帧大小不发生变化）时有关输出信号维度的更多信息。

| 输入信号 | 条件 | 输出信号 |
| --- | --- | --- |
| *L*×1 列向量，其中 *L* 是 *M* 的倍数，*M* 是频带数量。  你可以使用 **Number of frequency bands** 参数指定 *M*。 | 清除 **Bands as separate output ports (Max. of 16 bands)** 参数 | (*L*/*M*)×*M* |
| 选择 **Bands as separate output ports (Max. of 16 bands)** 参数 | 该模块在 *M* 个输出端口的每个端口输出 *M* 个大小为 (*L*/*M*)×1 的窄带信号。  如果 *M* > 16，则最后一个输出端口处的窄带信号大小为 (*L*/*M*)×(*M*−15)。 |
| *L*×1 列向量，其中 *L* 不是 *M* 的倍数。  选择 **Allow arbitrary frame length for fixed-size input signals** 参数。如果未选择 **Allow arbitrary frame length for fixed-size input signals**，该模块将报错。 | 清除 **Bands as separate output ports (Max. of 16 bands)** 参数 | `ceil`(*L*/*M*)×*M* |
| 选择 **Bands as separate output ports (Max. of 16 bands)** 参数 | 该模块在 *M* 个输出端口的每个端口输出 *M* 个大小为 `ceil`(*L*/*M*)×1 的窄带信号。  如果 *M* > 16，则最后一个输出端口处的窄带信号大小为 `ceil`(*L*/*M*)×(*M*−15)。 |
| *L*×*N* 矩阵，其中 *L* 是 *M* 的倍数 | 清除 **Bands as separate output ports (Max. of 16 bands)** 参数 | (*L*/*M*)×*M*×*N* |
| 选择 **Bands as separate output ports (Max. of 16 bands)** 参数 | 该模块在 *M* 个输出端口的每个端口输出 *M* 个大小为 (*L*/*M*)×*N* 的窄带信号。  如果 *M* > 16，则最后一个输出端口处的窄带信号大小为 (*L*/*M*)×(*M*−15)×*N*。 |
| *L*×*N* 矩阵，其中 *L* 不是 *M* 的倍数。  选择 **Allow arbitrary frame length for fixed-size input signals** 参数。如果未选择 **Allow arbitrary frame length for fixed-size input signals**，该模块将报错。 | 清除 **Bands as separate output ports (Max. of 16 bands)** 参数 | `ceil`(*L*/*M*)×*M*×*N* |
| 选择 **Bands as separate output ports (Max. of 16 bands)** 参数 | 该模块在 *M* 个输出端口的每个端口输出 *M* 个大小为 `ceil`(*L*/*M*)×*N* 的窄带信号。  如果 *M* > 16，则最后一个输出端口处的窄带信号大小为 `ceil`(*L*/*M*)×(*M*−15)×*N*。 |

下表提供了当你输入可变大小输入信号（仿真期间信号帧大小发生变化）时有关输出信号维度的更多信息。

| 输入信号 | 条件 | 输出信号 |
| --- | --- | --- |
| *L*×1 列向量，其中 *L* 是 *M* 的倍数 | 清除 **Bands as separate output ports (Max. of 16 bands)** 参数 | (*L*/*M*)×*M* |
| 选择 **Bands as separate output ports (Max. of 16 bands)** 参数 | 该模块在 *M* 个输出端口的每个端口输出 *M* 个大小为 (*L*/*M*)×1 的窄带信号。  如果 *M* > 16，则最后一个输出端口处的窄带信号大小为 (*L*/*M*)×(*M*−15)。 |
| *L*×1 列向量，其中 *L* 不是 *M* 的倍数。  该模块忽略 **Allow arbitrary frame length for fixed-size input signals** 参数。 | 清除 **Bands as separate output ports (Max. of 16 bands)** 参数 | `ceil`(*L*/*M*)×*M* |
| 选择 **Bands as separate output ports (Max. of 16 bands)** 参数 | 该模块在 *M* 个输出端口的每个端口输出 *M* 个大小为 `ceil`(*L*/*M*)×1 的窄带信号。  如果 *M* > 16，则最后一个输出端口处的窄带信号大小为 `ceil`(*L*/*M*)×(*M*−15)。 |
| *L*×*N* 矩阵，其中 *L* 是 *M* 的倍数 | 清除 **Bands as separate output ports (Max. of 16 bands)** 参数 | (*L*/*M*)×*M*×*N* |
| 选择 **Bands as separate output ports (Max. of 16 bands)** 参数 | 该模块在 *M* 个端口的每个端口输出 *M* 个大小为 (*L*/*M*)×*N* 的窄带信号。  如果 *M* > 16，则最后一个输出端口处的窄带信号大小为 (*L*/*M*)×(*M*−15)×*N*。 |
| *L*×*N* 矩阵，其中 *L* 不是 *M* 的倍数。  该模块忽略 **Allow arbitrary frame length for fixed-size input signals** 参数。 | 清除 **Bands as separate output ports (Max. of 16 bands)** 参数 | `ceil`(*L*/*M*)×*M*×*N* |
| 选择 **Bands as separate output ports (Max. of 16 bands)** 参数 | 该模块在 *M* 个输出端口的每个端口输出 *M* 个大小为 `ceil`(*L*/*M*)×*N* 的窄带信号。  如果 *M* > 16，则最后一个输出端口处的窄带信号大小为 `ceil`(*L*/*M*)×(*M*−15)×*N*。 |

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

如果参数被列为可调，则可以在仿真期间更改其值。

### **Number of frequency bands** — 频带数量 `8`（默认） | 大于 1 的正整数

指定该模块将输入宽带信号分离成的频带数量 *M*。此参数指示算法使用的 FFT 长度和抽取因子。

### **DecimationFactor** — 抽取因子 `Number of frequency bands`（默认） | 正整数

指定抽取因子 *D* 为以下之一：

- `Number of frequency bands` –– 当你更改 **Number of frequency bands** 参数的值时，抽取因子会自动更改。*(自 R2024a 起)*
- 小于或等于频带数量 *M* 的正整数。

如果抽取因子 *D* 等于频带数量 *M*，则 *M*/*D* 比率等于 1，该信道化器称为最大抽取信道化器。

如果 *M*/*D* 比率大于 `1`，则输出采样率与信道间隔不同，该信道化器称为非最大抽取信道化器。如果比率为整数，则该信道化器称为整数过采样信道化器。如果比率不是整数，例如 4/3，则该信道化器称为有理过采样信道化器。有关更多详细信息，请参阅算法。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Polyphase filter specification** — 滤波器设计参数或系数 `Number of taps per band and stopband attenuation`（默认） | `Coefficients`

- `Number of taps per band and stopband attenuation` — 通过 **Number of filter taps per frequency band** 和 **Stopband attenuation (dB)** 参数指定滤波器设计参数。当你指定设计参数时，滤波器使用 `designMultirateFIR` 函数设计。
- `Coefficients` — 使用 **Prototype lowpass filter coefficients** 参数直接指定滤波器系数，或通过 **coeffs** 端口输入这些系数。

### **Number of filter taps per frequency band** — 每个频带的滤波器系数数量 `12`（默认） | 正整数

每个多相分支使用的滤波器系数数量。多相分支的数量与频带数量匹配。原型低通滤波器的滤波器系数总数为 **Number of frequency bands** × **Number of filter taps per frequency band**。对于给定的阻带衰减，增加每个频带的抽头数会收窄滤波器的过渡宽度。因此，每个频带会有更多可用带宽，但代价是计算量增加。

#### 依赖项

要启用此参数，请将 **Polyphase filter specification** 设置为 `Number of taps per band and stopband attenuation`。

### **Stopband attenuation (dB)** — 阻带衰减 `80`（默认） | 正实数标量

低通滤波器的阻带衰减，以 dB 为单位。此值控制从一个频带到下一个频带的最大混叠量。随着阻带衰减增加，通带波纹减小。

#### 依赖项

要启用此参数，请将 **Polyphase filter specification** 设置为 `Number of taps per band and stopband attenuation`。

### **Specify coefficients from input port** — 用于指定低通滤波器系数的标志 off（默认） | on

当你选择此参数时，低通滤波器系数通过 **coeffs** 端口输入。当你清除此参数时，系数通过 **Prototype lowpass filter coefficients** 参数在模块对话框中指定。

#### 依赖项

要启用此参数，请将 **Polyphase filter specification** 设置为 `Coefficients`。

### **Prototype lowpass filter coefficients** — 原型低通滤波器系数 `rcosdesign(0.25,6,8,'sqrt')`（默认） | 行向量

原型低通滤波器的系数。默认值是 `rcosdesign(0.25,6,8,'sqrt')` 返回的系数向量。每个频带至少必须有一个系数。如果低通滤波器的长度小于频带数量，该模块会对系数进行零填充。

如果指定复数系数，该模块会设计一个中心位于非零频率的原型滤波器，也称为带通滤波器。原型带通滤波器的调制版本相对于原型滤波器出现，并环绕在频率范围 [−*F*s
*F*s] 内。

**可调：** 是

#### 依赖项

要启用此参数，请将 **Polyphase filter specification** 设置为 `Coefficients`，并清除 **Specify coefficients from input port** 参数。

**复数支持：** 是

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号使用任意帧长度 off（默认） | on

指定固定大小输入信号（其大小在仿真期间不发生变化）是否可以具有任意帧长度，其中帧长度不必是抽取因子的整数倍。该模块仅对固定大小输入信号使用此参数设置，如果输入具有可变大小，则忽略此参数。

当输入信号是可变大小信号时，该信号可以具有任意帧长度，也就是说，帧长度不必是抽取因子的整数倍。

对于固定大小输入信号，如果你：

- 选择 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是抽取因子的整数倍。如果输入不是抽取因子的整数倍，则输出通常是可变大小信号。因此，为了支持任意输入大小，该模块还必须支持可变大小操作，你可以通过选择 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该支持。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是抽取因子的整数倍。

### **Bands as separate output ports (Max. of 16 bands)** — 在单独输出端口上输出频带 off（默认） | on

*自 R2024a 起*

当你选择此参数时，该模块为每个频带提供一个单独的输出端口。输出端口数量等于 `min`(**Number of frequency bands**, 16)。该模块将每个输出端口标记为 **Band*`x`***，其中 *x* 可以是范围 [1 `min`(**Number of frequency bands**, 16)] 中的值。

有关每个输出端口上信号大小的更多信息，请参阅 **Output(s)** 端口描述。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。你可以将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不发生变化，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `No` |
| **可变大小信号** | `Yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2024a：在单独输出端口输出每个窄带信号

当你选择 **Bands as separate output ports (Max. of 16 bands)** 参数时，该模块在单独端口输出每个窄带信号。该模块最多可以单独输出 16 个窄带信号。当你清除此参数时，该模块将所有窄带信号串联起来，形成单个输出数组。

### R2024a：指定抽取因子等于频带数量

你现在可以将 **Decimation factor** 参数设置为 `Number of frequency bands`。当你更改 **Number of frequency bands** 参数的值时，抽取因子会自动更改。

使用 Channelizer 模块的现有 Simulink 模型在 R2024a 中继续运行。

### R2022b：支持任意输入帧长度

当满足以下条件时，Channelizer 模块支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（仿真期间帧长度不发生变化），并且你选择 **Allow arbitrary frame length for fixed-size input signals** 参数
- 输入信号是可变大小信号（仿真期间帧长度发生变化）

当帧长度不是抽取因子的倍数时，帧长度是任意的。

## 描述

多相 FFT 分析滤波器组

Channelizer 模块使用基于 FFT 的分析滤波器组将宽带输入信号分离成多个窄子带。该滤波器组使用原型低通滤波器，并采用多相结构实现。你可以直接指定滤波器系数，或通过设计参数指定。当你指定设计参数时，滤波器使用 `designMultirateFIR` 函数设计。

此模块接受可变大小输入，因此你可以在仿真期间更改每个输入通道的大小。但是，通道数量不能更改。
