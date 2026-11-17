---
type: simulink-block
title: 'FIR Halfband Decimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'firhalfbanddecimator'
documentation_source_path: 'ref/firhalfbanddecimator.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Halfband Decimator

## 端口

### 输入

### **Input** — 输入信号 列向量 | 矩阵

将输入信号指定为列向量或大小为 *P*×*Q* 的矩阵。

该模块将输入信号的每一列视为一个独立通道。如果输入是二维信号，第一维表示通道长度（或帧大小），第二维表示通道数。如果输入是一维信号，则该模块将其解释为单通道信号。

该模块支持可变大小输入信号（帧长度在仿真期间发生变化）。

当您输入可变大小信号时，信号的帧长度可以是任意的，即输入帧长度不必是抽取因子 2 的倍数。当您输入固定大小信号（帧长度在仿真期间不变）时，仅当您选中 **Allow arbitrary frame length for fixed-size input signals** 参数时，帧长度才可以是任意的。*（自 R2023b 起）*

该模块支持可变大小输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是
### 输出

### **LP** — 抽取器输出的低通子带 列向量 | 矩阵

抽取器输出的低通子带，以列向量或矩阵形式返回。由于该滤波器是半带滤波器，下采样因子始终为 2。

输出信号的维度取决于输入信号的维度以及您是否选中 **Allow arbitrary frame length for fixed-size input signals** 参数。*（自 R2023b 起）*

下表提供了当您输入固定大小输入信号时低通子带输出信号维度的更多详细信息。

**固定大小输入信号**

| 输入信号 | 输出信号 |
| --- | --- |
| *P*×*Q*，其中 *P* 是抽取因子 2 的倍数 | 大小为 (*P*/2)×*Q* 的固定大小信号 |
| *P*×*Q*，其中 *P* 不是抽取因子 2 的倍数 *（自 R2023b 起）* | 当您选中 **Allow arbitrary frame length for fixed-size input signals** 时，上界为 `ceil`(*P*/2)×*Q* 的可变大小信号 *（自 R2023b 起）*  如果您未选中 **Allow arbitrary frame length for fixed-size input signals**，该模块将报错。*（自 R2023b 起）* |

下表给出了当您输入可变大小输入信号时低通子带输出信号维度的更多详细信息。当您输入可变大小信号（帧长度在仿真期间发生变化）时，**Allow arbitrary frame length for fixed-size input signals** 参数在模块对话框中可见，但对输入帧长度没有任何影响。即使您未选中 **Allow arbitrary frame length for fixed-size input signals** 参数，您也可以输入任意帧长度的可变大小信号。*（自 R2023b 起）*

**可变大小输入信号**

| 输入信号 | 输出信号 |
| --- | --- |
| *P*×*Q* | 上界为 `ceil`(*P*/2)×*Q* 的可变大小信号 *（自 R2023b 起）* |

当输出为定点数据类型时，它仅为有符号类型。

在您选中 **Output highpass subband** 参数之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** 是

### **HP** — 抽取器输出的高通子带 列向量 | 矩阵

抽取器输出的高通子带，以列向量或矩阵形式返回。由于该滤波器是半带滤波器，下采样因子始终为 2。

输出信号的维度取决于输入信号的维度以及您是否选中 **Allow arbitrary frame length for fixed-size input signals** 参数。*（自 R2023b 起）*

下表提供了当您输入固定大小输入信号时高通子带输出信号维度的更多详细信息。

**固定大小输入信号**

| 输入信号 | 输出信号 |
| --- | --- |
| *P*×*Q*，其中 *P* 是抽取因子 2 的倍数 | 大小为 (*P*/2)×*Q* 的固定大小信号 |
| *P*×*Q*，其中 *P* 不是抽取因子 2 的倍数 *（自 R2023b 起）* | 当您选中 **Allow arbitrary frame length for fixed-size input signals** 时，上界为 `ceil`(*P*/2)×*Q* 的可变大小信号 *（自 R2023b 起）*  如果您未选中 **Allow arbitrary frame length for fixed-size input signals**，该模块将报错。*（自 R2023b 起）* |

下表给出了当您输入可变大小输入信号时高通子带输出信号维度的更多详细信息。当您输入可变大小信号（帧长度在仿真期间发生变化）时，**Allow arbitrary frame length for fixed-size input signals** 参数在模块对话框中可见，但对输入帧长度没有任何影响。即使您未选中 **Allow arbitrary frame length for fixed-size input signals** 参数，您也可以输入任意帧长度的可变大小信号。*（自 R2023b 起）*

**可变大小输入信号**

| 输入信号 | 输出信号 |
| --- | --- |
| *P*×*Q* | 上界为 `ceil`(*P*/2)×*Q* 的可变大小信号 *（自 R2023b 起）* |

当输出为定点数据类型时，它仅为有符号类型。

#### 依赖关系

要启用此端口，请选中 **Output highpass subband** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** 是

## 参数

### 主选项卡

### **Filter specification** — 滤波器设计参数 `Transition width and stopband attenuation`（默认）| `Filter order and transition width` | `Filter order and stopband attenuation` | `Coefficients`

选择该模块用于设计 FIR 半带滤波器的参数。

- `Transition width and stopband attenuation`（默认）—— 使用 **Transition width (Hz)** 和 **Stopband attenuation (dB)** 设计滤波器。此设计为最小阶数设计。
- `Filter order and transition width` —— 使用 **Filter order** 和 **Transition width (Hz)** 设计滤波器。
- `Filter order and stopband attenuation` —— 使用 **Filter order** 和 **Stopband attenuation (dB)** 设计滤波器。
- `Coefficients` —— 通过 **Numerator** 参数直接指定滤波器系数。

### **Filter order** — 滤波器阶数 `52`（默认）| 偶数正整数

将滤波器阶数指定为偶数正整数。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Filter order and transition width` 或 `Filter order and stopband attenuation`。

### **Transition width (Hz)** — 过渡带宽 `4.1e3`（默认）| 正标量

将过渡带宽指定为以 Hz 或归一化频率单位表示的正标量 *（自 R2023b 起）*。

如果您将 **Sample rate mode** 参数设置为：

- `Specify on dialog` 或 `Inherit from input port` —— 过渡带宽的值以 Hz 为单位，且必须小于输入采样率值的一半。
- `Use normalized frequency (0 to 1)` —— 过渡带宽的值以归一化频率单位表示。该值必须是小于 `1.0` 的正标量。

*（自 R2023b 起）*

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Filter order and transition width` 或 `Transition width and stopband attenuation`。

### **Stopband attenuation (dB)** — 阻带衰减 `80`（默认）| 正实标量

将阻带衰减指定为以 dB 表示的正实标量。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Filter order and stopband attenuation` 或 `Transition width and stopband attenuation`。

### **Numerator** — FIR 半带滤波器系数 `designHalfbandFIR('TransitionWidth',0.186, 'StopbandAttenuation',80, 'Structure','decim')`（默认）| 行向量

将 FIR 半带滤波器系数直接指定为行向量。系数必须符合 FIR 半带冲激响应格式。如果 (`length`(`Numerator`) − 1)/2 为偶数，其中 (`length`(`Numerator`) − 1) 是滤波器阶数，则从第一个系数开始的每隔一个系数必须为 0，但中心系数必须为 0.5。如果 (`length`(`Numerator`) − 1)/2 为奇数，则交替零序列（中心为 0.5）从第二个系数开始。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Coefficients`。

### **Design method** — 滤波器设计方法 `Auto`（默认）| `Equiripple` | `Kaiser`

将滤波器设计方法指定为以下之一：

- `Auto` —— 算法根据滤波器设计参数自动选择滤波器设计方法。算法使用等波纹法或 Kaiser 窗法来设计滤波器。

  如果设计约束非常严格，例如非常高的阻带衰减或非常窄的过渡带宽，则算法自动选择 Kaiser 方法，因为该方法对于设计具有非常严格规格的滤波器是最优的。但是，如果设计约束不严格，则算法选择等波纹法。

  当您将 **Design method** 参数设置为 `Auto` 时，您可以通过检查所设计滤波器的通带和阻带波纹特性来确定算法所使用的方法。如果该模块使用了等波纹法，则所设计滤波器的通带和阻带波纹在频率响应中具有恒定幅度。如果该模块在 `Auto` 模式下选择的滤波器设计方法不适合您的应用，请手动将 **Design method** 指定为 `Equiripple` 或 `Kaiser`。
- `Equiripple` —— 算法使用等波纹法。
- `Kaiser` —— 算法使用 Kaiser 窗法。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Filter order and stopband attenuation`、`Filter order and transition width` 或 `Transition width and stopband attenuation`。

### **Output highpass subband** — 输出高通子带 `off`（默认）| `on`

当您选中此复选框时，该模块充当分析滤波器组，将输入信号分析为高通和低通子带。当您清除此复选框时，该模块充当 FIR 半带抽取器。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认）| `Specify on dialog` | `Inherit from input port`

*自 R2023b 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)` —— 以归一化频率单位（0 到 1）指定过渡带宽。
- `Specify on dialog` —— 在模块对话框中使用 **Input sample rate (Hz)** 参数指定输入采样率。
- `Inherit from input port` —— 该模块从输入信号继承采样率。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为除 `Coefficients` 以外的任何值。

### **Input sample rate (Hz)** — 输入信号的采样率 `44100`（默认）| 正实标量

将输入信号的采样率指定为以 Hz 表示的正标量。

#### 依赖关系

要启用此参数，请设置：

- **Filter specification** 为除 `Coefficients` 以外的任何值。
- **Sample rate mode** 为 `Specify on dialog`。

*（自 R2023b 起）*

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号的任意帧长度 `off`（默认）| `on`

*自 R2023b 起*

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是抽取因子 2 的倍数。该模块仅对固定大小输入信号使用此参数，如果输入数据在仿真期间大小发生变化，则忽略此参数。

当输入信号为可变大小信号时，该信号可以具有任意帧长度，即帧长度不必是抽取因子 2 的倍数。

对于固定大小输入信号，如果您：

- 选中 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是抽取因子 2 的倍数。如果输入不是抽取因子的倍数，则输出通常是可变大小信号。因此，为了支持任意输入大小，该模块还必须支持可变大小操作，您可以通过选中 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该操作。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是抽取因子 2 的倍数。

### **View Filter Response** — 查看滤波器响应 按钮

点击此按钮可打开滤波器可视化工具（FVTool），并显示 FIR Halfband Decimator 的幅频和相频响应。该响应基于您在模块参数对话框中指定的值。对这些参数所做的更改会更新 FVTool。

要在 FVTool 运行时更新幅频响应，请修改对话框参数并点击 **Apply**。

以 dB 为单位的幅频响应

要同时查看幅频响应和相频响应，请点击工具栏上的 **Magnitude and Phase responses** 按钮。

#### 依赖关系

要可视化滤波器响应，请将 **Sample rate mode** 设置为 `Specify on dialog` 或 `Use normalized frequency (0 to 1)`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。

### 数据类型选项卡

### **Rounding mode** — 输出定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Nearest` | `Round` | `Simplest` | `Zero`

选择输出定点运算的舍入模式。默认为 `Floor`。

### **Coefficients** — 系数的字长和小数长度 `fixdt(1,16)`（默认）| `fixdt(1,16,0)`

将系数的定点数据类型指定为以下之一：

- `fixdt(1,16)`（默认）—— 字长为 `16` 且采用二进制小数点定标的有符号定点数据类型。该模块根据系数值自动确定小数长度，使得系数在不溢出的情况下占据最大可表示范围。
- `fixdt(1,16,0)` —— 字长为 `16`、小数长度为 `0` 的有符号定点数据类型。您可以将小数长度更改为任何其他整数值。
- `<data type expression>` —— 使用求值为数据类型对象的表达式指定系数数据类型。例如，`numerictype`(`fixdt`(`[ ]`,`18`, `15`))。将此数据类型的符号模式指定为 `[ ]` 或 true。
- `Refresh Data Type` —— 刷新为默认数据类型。

点击 **Show data type assistant** 按钮以显示数据类型助手，它可帮助您设置系数数据类型。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2024a：**Simulate using** 参数默认值的更改

**Simulate using** 参数的默认值现在为
`Interpreted execution`。通过此更改，该模块默认使用
MATLAB 解释器进行仿真。

### R2023b：支持归一化频率

当您将 **Sample rate mode** 参数设置为
`Use normalized frequency (0 to 1)` 时，您可以以归一化频率单位（0 到 1）指定
过渡宽度。

### R2023b：支持任意输入帧长度

当满足以下条件时，此模块支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（帧长度在仿真期间不变），并且您选择 **Allow arbitrary frame
  length for fixed-size input signals** 参数。
- 输入信号是可变大小信号（帧长度在仿真期间变化）。

当此模块支持具有任意帧长度的输入信号时，输入帧
长度不必是抽取因子 2 的倍数，并且输出
信号是可变大小信号。

## 描述

使用多相 FIR 半带滤波器对信号进行抽取

FIR Halfband Decimator 模块对
输入信号执行因子为 2 的多相抽取。该模块使用 FIR 等波纹设计或 Kaiser
窗设计来构造半带滤波器。该实现利用了
FIR 半带滤波器的零值系数，使其中一个多相
支路成为延迟。您可以使用该模块实现双频带
滤波器组的分析部分，以将信号分离为低通和高通子带。有关更多
信息，请参阅算法。

该模块支持定点运算和 ARM®
Cortex® 代码生成。有关 ARM
Cortex 代码生成的更多信息，请参阅 Code Generation for ARM Cortex-M and ARM Cortex-A Processors。
