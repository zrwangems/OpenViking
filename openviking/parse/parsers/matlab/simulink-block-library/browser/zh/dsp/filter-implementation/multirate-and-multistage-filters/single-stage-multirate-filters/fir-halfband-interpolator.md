---
type: simulink-block
title: 'FIR Halfband Interpolator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Implementation / Multirate and Multistage Filters / Single Stage Multirate Filters'
documentation_page: 'firhalfbandinterpolator'
documentation_source_path: 'ref/firhalfbandinterpolator.html'
language: zh-CN
chinese_source: worker-translation
---

# FIR Halfband Interpolator

## 端口

### 输入

### **LP** — 数据输入 列向量 | 矩阵

将数据输入指定为向量或矩阵。如果输入信号是矩阵，模块将矩阵的每一列视为独立通道。

当选择 **Input highpass subband** 参数时，此模块充当半带合成滤波器组。此时，此端口的输入是半带分析滤波器组的低通子带输出。

在选择 **Input highpass subband** 参数之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes

### **HP** — 合成滤波器组的第二输入 列向量 | 矩阵

将合成滤波器组的第二输入指定为列向量或矩阵。此信号是半带分析滤波器组的高通子带输出。如果输入信号是矩阵，模块将矩阵的每一列视为独立通道。

两个输入的大小、数据类型和复/实性必须相同。

#### 依赖关系

要启用此端口，请选择 **Input highpass subband** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes

### 输出

### **Output** — FIR 半带内插器的输出 列向量 | 矩阵

FIR 半带内插器的输出，返回为列向量或矩阵。内插器输出的行数是输入信号行数的两倍。

当输出为定点时，它仅为有符号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **Filter specification** — 滤波器设计参数 `Transition width and stopband attenuation` (default) | `Filter order and transition width` | `Filter order and stopband attenuation` | `Coefficients`

选择模块用于设计 FIR 半带滤波器的参数。

- `Transition width and stopband attenuation` (default) — 使用 **Transition width (Hz)** 和 **Stopband attenuation (dB)** 设计滤波器。此设计为最小阶数设计。
- `Filter order and transition width` — 使用 **Filter order** 和 **Transition width (Hz)** 设计滤波器。
- `Filter order and stopband attenuation` — 使用 **Filter order** 和 **Stopband attenuation (dB)** 设计滤波器。
- `Coefficients` — 直接通过 **Numerator** 参数指定滤波器系数。

### **Transition width (Hz)** — 以 Hz 为单位的过渡带宽 `4.1e3` | 正实数标量

将过渡带宽指定为以 Hz 为单位的正实数标量，或以归一化频率单位表示的正实数标量 *(自 R2023b 起)*。

如果设置 **Sample rate mode** 参数为：

- `Specify on dialog` 或 `Inherit from input port` –– 过渡带宽的值以 Hz 为单位，且必须小于输出采样率（2 × 输入采样率）值的一半。
- `Use normalized frequency (0 to 1)` –– 过渡带宽的值以归一化频率单位表示。该值必须为小于 `1.0` 的正标量。

*(自 R2023b 起)*

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Filter order and transition width` 或 `Transition width and stopband attenuation`。

### **Filter order** — 滤波器阶数 `52` | 偶数正整数

将滤波器阶数指定为偶数正整数。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Filter order and transition width` 或 `Filter order and stopband attenuation`。

### **Stopband attenuation (dB)** — 阻带衰减 `80` (default) | 正实数标量

将阻带衰减指定为以 dB 为单位的正实数标量。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Filter order and stopband attenuation` 或 `Transition width and stopband attenuation`。

### **Numerator** — FIR 半带滤波器系数 `designHalfbandFIR('TransitionWidth',0.186, 'StopbandAttenuation',80, 'Structure','interp')` (default) | 行向量

将 FIR 半带滤波器系数直接指定为行向量。系数必须符合 FIR 半带冲激响应格式。如果 (`length`(`Numerator`) − 1)/2 为偶数，其中 (`length`(`Numerator`) − 1) 是滤波器阶数，则从第一个系数开始每隔一个系数必须为 0，但中心系数必须为 1.0。如果 (`length`(`Numerator`) − 1)/2 为奇数，则中心为 1.0 的交替零序列从第二个系数开始。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Coefficients`。

### **Design method** — 滤波器设计方法 `Auto` (default) | `Equiripple` | `Kaiser`

将滤波器设计方法指定为以下之一：

- `Auto` –– 算法根据滤波器设计参数自动选择滤波器设计方法。算法使用等波纹法或 Kaiser 窗法设计滤波器。

  如果设计约束非常严格，例如非常高的阻带衰减或非常窄的过渡带宽，则算法会自动选择 Kaiser 法，因为该方法非常适合设计具有非常严格指标的滤波器。但是，如果设计约束不严格，则算法会选择等波纹法。

  当将 **Design method** 参数设置为 `Auto` 时，可以通过检查所设计滤波器的通带和阻带波纹特性来确定算法所使用的方法。如果模块使用了等波纹法，则所设计滤波器的通带和阻带波纹在频率响应中具有恒定幅度。如果模块在 `Auto` 模式下选择的滤波器设计方法不适合您的应用，请将 **Design method** 手动指定为 `Equiripple` 或 `Kaiser`。
- `Equiripple` –– 算法使用等波纹法。
- `Kaiser` –– 算法使用 Kaiser 窗法。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Filter order and stopband attenuation`、`Filter order and transition width` 或 `Transition width and stopband attenuation`。

### **Input highpass subband** — 输入高通子带 off (default) | on

当选中此复选框时，模块充当合成滤波器组。模块接受两个输入进行合成：低通和高通子带。当清除此复选框时，模块充当 IIR 半带内插器，并接受单个向量或矩阵作为输入。默认情况下，此复选框处于清除状态。

### **Sample rate mode** — 用于指定输入采样率的模式 `Use normalized frequency (0 to 1)` (default) | `Specify on dialog` | `Inherit from input port`

*自 R2023b 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)` –– 以归一化频率单位（0 到 1）指定过渡带宽。
- `Specify on dialog` –– 使用 **Input sample rate (Hz)** 参数在模块对话框中指定输入采样率。
- `Inherit from input port` –– 模块从输入信号继承采样率。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为除 `Coefficients` 之外的任何值。

### **Input sample rate (Hz)** — 输入信号的采样率 `44100` (default) | 正实数标量

将输入信号的采样率指定为以 Hz 为单位的标量。

#### 依赖关系

要启用此参数，请设置：

- **Filter specification** 为除 `Coefficients` 之外的任何值。
- **Sample rate mode** 为 `Specify on dialog`。

*(自 R2023b 起)*

### **View Filter Response** — 查看滤波器响应按钮

单击此按钮可打开 Filter Visualization Tool (FVTool)，并显示 FIR Halfband Interpolator 的幅值和相位响应。响应基于您在模块参数对话框中指定的值。对这些参数所做的更改会更新 FVTool。

要在 FVTool 运行时更新幅值响应，请修改对话框参数并单击 **Apply**。

要同时查看幅值响应和相位响应，请单击工具栏上的 **Magnitude and Phase responses** 按钮。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

指定要运行的仿真类型。可将此参数设置为：

- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` –– 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。

### 数据类型选项卡

### **Rounding mode** — 输出定点运算的舍入模式 `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定输出定点运算的舍入方法。舍入方法有 `Ceiling`、`Convergent`、`Floor`、`Nearest`、`Round`、`Simplest` 和 `Zero`。默认值为 `Floor`。

### **Coefficients** — 系数的字长和小数长度 `fixdt(1,16)` (default) | `fixdt(1,16,0)`

将系数的定点数据类型指定为以下之一：

- `fixdt(1,16)` (default) — 字长为 `16` 且采用二进制小数点定标的带符号定点数据类型。模块根据系数值自动确定小数长度，以使系数在不溢出的情况下占用最大可表示范围。
- `fixdt(1,16,0)` — 字长为 `16` 且小数长度为 `0` 的带符号定点数据类型。可将小数长度更改为任何其他整数值。
- `<data type expression>` — 使用可求值为数据类型对象的表达式指定系数数据类型。例如，`numerictype`(`fixdt`(`[ ]`,`18`, `15`))。将此数据类型的符号模式指定为 `[ ]` 或 true。
- `Refresh Data Type` — 刷新为默认数据类型。

单击 **Show data type assistant** 按钮  以显示数据类型助手，它可帮助您设置系数数据类型。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当输入信号的数据类型为 `single` 或 `double` 时，FIR Halfband Interpolator 模块支持使用 Intel AVX2 code replacement library 的 SIMD 代码生成。

SIMD 技术显著提高生成代码的性能。有关详细信息，请参阅 SIMD Code Generation。要从此模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks。

## 版本历史

**在 R2015b 中引入**

### R2024a：**Simulate using** 参数默认值的变化

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，模块默认使用 MATLAB 解释器进行仿真。

### R2023b：支持归一化频率

当将 **Sample rate mode** 参数设置为 `Use normalized frequency (0 to 1)` 时，可以以归一化频率单位（0 到 1）指定过渡带宽。

## 描述

使用多相 FIR 半带滤波器对信号进行内插

FIR Halfband Interpolator 模块将输入信号内插两倍。该模块使用 FIR 等波纹设计或 Kaiser 窗设计来构造半带滤波器。模块使用高效的多相实现来对输入进行滤波。该实现利用 FIR 半带滤波器的零值系数，使其中一个多相分支成为延迟。有关详细信息，请参阅 Algorithms。您还可以使用此模块实现双频带滤波器组的合成部分，以从低通和高通子带合成信号。

输入信号可以是实值或复值列向量或矩阵。如果输入信号是矩阵，模块将矩阵的每一列视为独立通道。该模块支持定点运算和 ARM® Cortex® 代码生成。有关 ARM Cortex 代码生成的详细信息，请参阅 Code Generation for ARM Cortex-M and ARM Cortex-A Processors。

该模块还支持 SIMD 代码生成。有关详细信息，请参阅 Code Generation。
