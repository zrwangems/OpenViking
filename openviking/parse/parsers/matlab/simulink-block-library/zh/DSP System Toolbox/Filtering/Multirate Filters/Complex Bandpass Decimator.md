---
type: simulink-block
title: 'Complex Bandpass Decimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'complexbandpassdecimator'
documentation_source_path: 'ref/complexbandpassdecimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Complex Bandpass Decimator

## 端口
```yaml
ports:
- name: x
  summary: 输入数据向量 | 矩阵
  direction: input
  data_types: single | double
- name: Fc
  summary: 中心频率实数标量
  direction: input
  data_types: single | double
- name: Port_1
  summary: 滤波后的输出向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **x** — 输入数据向量 | 矩阵

将输入数据指定为向量或矩阵。

该模块将输入信号的每一列视为一个独立通道。如果输入是二维信号，第一维表示通道长度（或帧大小），第二维表示通道数。如果输入是一维信号，则该模块将其解释为单通道信号。

当输入可变大小信号（帧长度在仿真期间变化）时，信号的帧长度可以是任意的，即输入帧长度不必是抽取因子的整数倍。当输入固定大小信号（帧长度在仿真期间不变）时，仅当您选择 **Allow arbitrary frame length for fixed-size input signals** 参数时，帧长度才可以任意。

要确定抽取因子，请点击 **View Info** 按钮。

在您选择 **Specify center frequency from input port** 参数之前，此端口是未命名的。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Fc** — 中心频率实数标量

将所需频带的中心频率指定为范围 [–*Fs*/2, *Fs*/2] 内的实数有限数值标量，其中 *Fs* 是输入信号的采样率。如果您将 **Sample rate mode** 设置为 `Inherit from input port` 或 `Specify on dialog`，则该模块分别从输入信号继承 *Fs* 或使用 **Input sample rate (Hz)** 参数的值。如果您将 **Sample rate mode** 设置为 `Use normalized frequency (0 to 1)`，则该模块将 *Fs* 设置为 2 *（自 R2024b 起）*。

#### 依赖关系

要启用此端口，请选择 **Specify center frequency from input port** 参数。

**数据类型：** `single` | `double`
**复数支持：** 是
### 输出

### **Port\_1** — 滤波后的输出向量 | 矩阵

复数带通抽取器的输出，以向量或矩阵形式返回。输出包含由模块对话框中的参数指定的频率子带。

输出信号维度取决于输入信号维度、Complex Bandpass Decimator 模块的总抽取因子，以及您是否选择 **Allow arbitrary frame length for fixed-size input signals** 参数。您可以通过点击模块对话框中的 **View Info** 按钮来确定总抽取因子 *D*。

下表提供了当您输入固定大小输入信号时输出信号维度的更多详细信息。

**固定大小输入信号**

| 输入信号 | 输出信号维度 |
| --- | --- |
| *P*×1 列向量，其中 *P* 是抽取因子 *D* 的整数倍 | (*P*/*D*)×1 |
| *P*×1 列向量，其中 *P* 不是抽取因子 *D* 的整数倍 | 当您选择 **Allow arbitrary frame length for fixed-size input signals** 时，为 `ceil`(*P*/*D*)×1。如果您未选择 **Allow arbitrary frame length for fixed-size input signals**，则该模块会报错。 |
| *P*×*Q* 矩阵，其中 *P* 是抽取因子 *D* 的整数倍 | (*P*/*D*)×*Q* |
| *P*×*Q* 矩阵，其中 *P* 不是抽取因子 *D* 的整数倍 | 当您选择 **Allow arbitrary frame length for fixed-size input signals** 时，为 `ceil`(*P*/*D*)×*Q*。如果您未选择 **Allow arbitrary frame length for fixed-size input signals**，则该模块会报错。 |

下表给出了当您输入可变大小输入信号时输出信号维度的更多详细信息。当您输入可变大小信号（帧长度在仿真期间变化）时，**Allow arbitrary frame length for fixed-size input signals** 参数在模块对话框中可见，但对输入帧长度没有任何影响。即使您未选择 **Allow arbitrary frame length for fixed-size input signals** 参数，您也可以输入任意帧长度的可变大小信号。

**可变大小输入信号**

| 输入信号 | 输出信号维度 |
| --- | --- |
| *P*×*Q* | `ceil`(*P*/*D*)×*Q* |

输出的数据类型与输入的数据类型相同。输出信号始终为复数。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Filter specification
  summary: 滤波器设计参数 Decimation factor（默认）| Bandwidth | Decimation factor and bandwidth
  group: ''
- name: Decimation factor
  summary: 抽取因子 2（默认）| 正整数
  group: ''
- name: Bandwidth
  summary: 感兴趣频带的宽度 0.2268（默认）| 实数正标量
  group: ''
- name: Specify center frequency from input port
  summary: 指定中心频率的来源 off（默认）| on
  group: ''
- name: Center frequency
  summary: 所需频带的中心频率 0（默认）| 实数标量
  group: ''
- name: Stopband attenuation (dB)
  summary: 以 dB 表示的阻带衰减 80（默认）| 正标量
  group: ''
- name: Passband ripple (dB)
  summary: 以 dB 表示的通带纹波 1（默认）| 正标量
  group: ''
- name: Transition width
  summary: 过渡宽度 0.0045（默认）| 正标量
  group: ''
- name: Reduce number of complex coefficients
  summary: 最小化复数系数的数量 on（默认）| off
  group: ''
- name: Mix signal to baseband
  summary: 将信号混频到基带 on（默认）| off
  group: ''
- name: Sample rate mode
  summary: 指定输入采样率的模式 Use normalized frequency (0 to 1)（默认）| Specify on dialog | Inherit from input port
  group: ''
- name: Input sample rate (Hz)
  summary: 以 Hz 表示的输入采样率 44100（默认）| 实数正标量
  group: ''
- name: Allow arbitrary frame length for fixed-size input signals
  summary: 允许固定大小输入信号的任意帧长度 off（默认）| on
  group: ''
- name: View Filter Response
  summary: 可视化频率响应 按钮
  group: ''
- name: View Info
  summary: 查看滤波器信息 按钮
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

### **Filter specification** — 滤波器设计参数 `Decimation factor`（默认）| `Bandwidth` | `Decimation factor and bandwidth`

将滤波器设计参数指定为以下之一：

- `Decimation factor` —— 通过 **Decimation factor** 参数指定抽取因子。该模块使用以下公式计算感兴趣的带宽（*BW*）：

  BW=Fs/D

  其中

  - *Fs* —— 输入信号的采样率
  - *D* —— 抽取因子
- `Bandwidth` —— 通过 **Bandwidth** 参数指定带宽。该模块使用以下公式计算抽取因子（*D*）：

  D=floor(FsBW+TW)

  其中

  - *Fs* —— 输入信号的采样率
  - *BW* —— 感兴趣的带宽
  - *TW* —— 通过 **Transition width** 参数指定的过渡宽度
- `Decimation factor and bandwidth` —— 分别通过 **Decimation factor** 和 **Bandwidth** 参数指定抽取因子和感兴趣的带宽。

### **Decimation factor** — 抽取因子 `2`（默认）| 正整数

将输入信号带宽的缩减因子指定为正整数。输入信号的帧大小（行数）必须是抽取因子的整数倍。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Decimation factor` 或 `Decimation factor and bandwidth`。

### **Bandwidth** — 感兴趣频带的宽度 `0.2268`（默认）| 实数正标量

将感兴趣频带的宽度指定为以 Hz 或归一化频率单位表示的实数正标量 *（自 R2024b 起）*。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Bandwidth` 或 `Decimation factor and bandwidth`。

**数据类型：** `single` | `double`

### **Specify center frequency from input port** — 指定中心频率的来源 `off`（默认）| `on`

当您选中此复选框时，中心频率通过 **Fc** 端口输入。当您清除此复选框时，您可以通过 **Center frequency** 参数在模块对话框中指定中心频率。

当您选中此复选框时，该模块不计算滤波器响应。要查看滤波器响应，请清除此复选框，在模块对话框中指定中心频率，然后点击 **View Filter Response** 按钮。

### **Center frequency** — 所需频带的中心频率 `0`（默认）| 实数标量

将所需频带的中心频率指定为以 Hz 或归一化频率单位表示的实数标量 *（自 R2024b 起）*。中心频率必须在范围 [–*Fs*/2, *Fs*/2] 内，其中 *Fs* 是输入信号的采样率。如果您将 **Sample rate mode** 设置为 `Inherit from input port` 或 `Specify on dialog`，则该模块分别从输入信号继承 *Fs* 或使用 **Input sample rate (Hz)** 参数的值。如果您将 **Sample rate mode** 设置为 `Use normalized frequency (0 to 1)`，则该模块将 *Fs* 设置为 2 *（自 R2024b 起）*。

**可调：** 是

**数据类型：** `single` | `double`

### **Stopband attenuation (dB)** — 以 dB 表示的阻带衰减 `80`（默认）| 正标量

将滤波器的阻带衰减指定为以 dB 表示的有限正标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Passband ripple (dB)** — 以 dB 表示的通带纹波 `1`（默认）| 正标量

将滤波器的通带纹波指定为以 dB 表示的正标量。

#### 依赖关系

要启用此参数，请将 **Filter specification** 设置为 `Bandwidth` 或 `Decimation factor and bandwidth`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Transition width** — 过渡宽度 `0.0045`（默认）| 正标量

将滤波器的过渡宽度指定为以 Hz 或归一化频率单位表示的正标量 *（自 R2024b 起）*。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Reduce number of complex coefficients** — 最小化复数系数的数量 `on`（默认）| `off`

选择此参数以最小化复数系数的数量。当您选择此参数时，多级滤波器的第一级是以指定中心频率为中心的带通滤波器（具有复数系数）。第一级之后是一个混频级，将信号外差到 DC。其余滤波器级均具有实数系数。

当您清除此参数时，输入信号首先通过多级滤波器的各个级。所有级均为带通（复数系数）。然后，如果选择了 **Mix signal to baseband** 参数且由抽取产生的频率偏移非零，则将信号外差到 DC。

### **Mix signal to baseband** — 将信号混频到基带 `on`（默认）| `off`

选择此参数以将信号混频到基带。当您选择此参数时，该模块将滤波、抽取后的信号外差到 DC。此混频级以滤波器的输出采样率运行。当您清除此参数时，该模块跳过混频级。

#### 依赖关系

此参数在您清除 **Reduce number of complex coefficients** 参数时适用。

### **Sample rate mode** — 指定输入采样率的模式 `Use normalized frequency (0 to 1)`（默认）| `Specify on dialog` | `Inherit from input port`

*自 R2024b 起*

使用以下选项之一指定输入采样率：

- `Use normalized frequency (0 to 1)` —— 以归一化频率单位（0 到 1）指定中心频率、过渡宽度和带宽。
- `Specify on dialog` —— 使用 **Input sample rate (Hz)** 参数在模块对话框中指定输入采样率。
- `Inherit from input port` —— 该模块从输入信号继承采样率。该模块根据输入端口的采样时间计算采样率。

### **Input sample rate (Hz)** — 以 Hz 表示的输入采样率 `44100`（默认）| 实数正标量

将输入信号 *Fs* 的采样率指定为以 Hz 表示的实数正标量。

#### 依赖关系

要启用此参数，请将 **Sample rate mode** 参数设置为 `Specify on dialog`。*（自 R2024b 起）*

**数据类型：** `single` | `double`

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号的任意帧长度 `off`（默认）| `on`

*自 R2023a 起*

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是抽取因子的整数倍。该模块仅对固定大小输入信号使用此参数，如果输入数据在仿真期间大小变化，则忽略此参数。

当输入信号是可变大小信号时，该信号可以具有任意帧长度，即帧长度不必是抽取因子的整数倍。

对于固定大小输入信号，如果您：

- 选择 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是抽取因子的整数倍。如果输入不是抽取因子的整数倍，则输出通常是可变大小信号。因此，为了支持任意输入大小，该模块还必须支持可变大小操作，您可以通过选择 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该操作。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是抽取因子的整数倍。

### **View Filter Response** — 可视化频率响应 按钮

点击此按钮以打开滤波器可视化器并显示复数带通抽取器的幅值响应。响应基于您在模块对话框中选择的参数。要在可视化器运行时更新响应，请修改对话框中的参数并点击 **Apply**。

您可以从可视化器的界面配置绘图设置和频率响应测量。

在 **Scope** 选项卡上，您可以启用图例，指定同时绘制滤波器的幅值和相位响应，修改绘图设置，生成用于重新创建绘图的脚本，甚至保存或共享设置。在 **Measurements** 选项卡上，您可以启用数据光标，并显示滤波器响应的峰值。

有关滤波器可视化器界面及其工具的更多详细信息，请参阅 Configure Filter Visualizer。

#### 依赖关系

要启用此按钮，请勿从输入端口指定任何滤波器规格。

### **View Info** — 查看滤波器信息 按钮

显示 Complex Bandpass Decimator 模块的滤波器信息。

此按钮将 `info` 分析方法的功能引入 Simulink® 环境。

#### 依赖关系

要启用此按钮，请勿从输入端口指定任何滤波器规格。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重复使用。此选项需要额外的启动时间，但可提供更快的后续仿真。
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

Complex Bandpass Decimator 模块在以下条件下支持使用 Intel AVX2 代码替换库进行 SIMD 代码生成：

- 输入信号为复数值。
- 输入信号的数据类型为 `single` 或 `double`。

SIMD 技术显著提高了生成代码的性能。有关更多信息，请参阅 SIMD Code Generation。要从该模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks。

## 版本历史

**在 R2018a 中引入**

### R2024b：支持归一化频率

当您将 **Sample rate mode** 参数设置为 `Use normalized frequency (0 to 1)` 时，您可以以归一化频率单位（0 到 1）指定中心频率、过渡宽度和带宽。

### R2024a：**Simulate using** 参数默认值的变化

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

### R2023a：支持任意输入帧长度

当满足以下条件时，此模块支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（帧长度在仿真期间不变），并且您选择 **Allow arbitrary frame length for fixed-size input signals** 参数。
- 输入信号是可变大小信号（帧长度在仿真期间变化）。

当此模块支持具有任意帧长度的输入信号时，输入帧长度不必是抽取因子的整数倍，并且输出信号是可变大小信号。

## 描述

使用单边（复数）带通抽取器提取频率子带

Complex Bandpass Decimator 模块使用单边、多级、复数带通抽取器提取特定的频率子带。该模块使用指定的中心频率、抽取因子和带宽值来确定感兴趣的带宽。

此模块支持 C/C++ 代码生成和 SIMD 代码生成。有关详细信息，请参阅代码生成。
