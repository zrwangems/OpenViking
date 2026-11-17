---
type: simulink-block
title: 'Farrow Rate Converter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'farrowrateconverter'
documentation_source_path: 'ref/farrowrateconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Farrow Rate Converter

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
- name: Port_1
  summary: 速率转换后的信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

将输入信号指定为实数或复数值的标量、向量或矩阵信号。

该模块将输入信号的每一列视为一个独立通道。如果输入是二维信号，第一维表示通道长度（或帧大小），第二维表示通道数。如果输入是一维信号，则该模块将其解释为单通道信号。

当您输入可变大小信号（帧长度在仿真期间变化）时，信号的帧长度可以是任意的，即输入帧长度不必是抽取因子的整数倍。当您输入固定大小信号（帧长度在仿真期间不变）时，仅当您选中 **Allow arbitrary frame length for fixed-size input signals** 参数时，帧长度才可以是任意的。

要确定抽取因子，请点击模块对话框中的 **View Info** 按钮。

如果输入是定点数，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 速率转换后的信号 标量 | 向量 | 矩阵

Farrow Rate Converter 模块输出的信号具有与输入信号相同的数据类型和复数性。

输出信号维度取决于输入信号维度、Farrow Rate Converter 模块的总插值因子和抽取因子，以及您是否选中 **Allow arbitrary frame length for fixed-size input signals** 参数。您可以通过点击模块对话框中的 **View Info** 按钮来确定总插值因子 *L* 和抽取因子 *M*。

下表提供了当您输入固定大小输入信号时输出信号维度的更多详细信息。

**固定大小输入信号**

| 输入信号 | 输出信号维度 |
| --- | --- |
| *P*×1 列向量，其中 *P* 是抽取因子 *M* 的整数倍 | (*LP*/*M*)×1，其中 *L* 是插值因子 |
| *P*×1 列向量，其中 *P* 不是抽取因子 *M* 的整数倍 | 当您选中 **Allow arbitrary frame length for fixed-size input signals** 时，为 `ceil`(*LP*/*M*)×1。如果您未选中 **Allow arbitrary frame length for fixed-size input signals**，则该模块会报错。 |
| *P*×*Q* 矩阵，其中 *P* 是抽取因子 *M* 的整数倍 | (*LP*/*M*)×*Q* |
| *P*×*Q* 矩阵，其中 *P* 不是抽取因子 *M* 的整数倍 | 当您选中 **Allow arbitrary frame length for fixed-size input signals** 时，为 `ceil`(*LP*/*M*)×*Q*。如果您未选中 **Allow arbitrary frame length for fixed-size input signals**，则该模块会报错。 |

下表给出了当您输入可变大小输入信号时输出信号维度的更多详细信息。当您输入可变大小信号（帧长度在仿真期间变化）时，**Allow arbitrary frame length for fixed-size input signals** 会出现在模块对话框中，但对输入帧长度没有任何影响。即使您未选中 **Allow arbitrary frame length for fixed-size input signals** 参数，您也可以输入任意帧长度的可变大小信号。

**可变大小输入信号**

| 输入信号 | 输出信号维度 |
| --- | --- |
| *P*×*Q* | `ceil`(*LP*/*M*)×*Q* |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Sample rate of input signal (Hz)
  summary: 输入信号的采样率（Hz） 48e3（默认）| 正标量
  group: 主选项卡
- name: Sample rate of output signal (Hz)
  summary: 输出信号的采样率（Hz） 96e3（默认）| 以 Hz 为单位的正标量
  group: 主选项卡
- name: Tolerance for output sample rate
  summary: 输出采样率的最大容差 0（默认）| 正标量
  group: 主选项卡
- name: Filter Specification method
  summary: 指定滤波器系数的方法 Polynomial order（默认）| Coefficients
  group: 主选项卡
- name: Coefficients
  summary: 滤波器多项式系数 [-1 1; 1 0]（默认）| 实值方阵
  group: 主选项卡
- name: Polynomial order
  summary: Lagrange 插值滤波器多项式的阶数 3（默认）| 小于或等于 4 的正整数
  group: 主选项卡
- name: Allow arbitrary frame length for fixed-size input signals
  summary: 允许固定大小输入信号使用任意帧长度 开（默认）| 关
  group: 主选项卡
- name: View Filter Response
  summary: 查看滤波器响应 按钮
  group: 主选项卡
- name: View Info
  summary: 查看信息 按钮
  group: 主选项卡
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: 主选项卡
- name: Rounding mode
  summary: 舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 整数溢出时的处理方法 关（默认）| 开
  group: 数据类型选项卡
- name: Coefficients
  summary: 滤波器系数的数据类型 fixdt(1,16)（默认）| fixdt(1,16,0)
  group: 数据类型选项卡
- name: Fractional Delay
  summary: 分数延迟的数据类型 fixdt(0,8)（默认）| fixdt(0,16)
  group: 数据类型选项卡
- name: Multiplicand
  summary: 被乘数的数据类型 fixdt(1,16,13)（默认）| fixdt(1,16,0)
  group: 数据类型选项卡
- name: Output
  summary: '输出的数据类型 Inherit: Same word length as input（默认）| Inherit: Same as accumulator | fixdt(1,16) | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Output Minimum
  summary: 模块可以输出的最小值 []（默认）| 标量
  group: 数据类型选项卡
- name: Output Maximum
  summary: 模块可以输出的最大值 []（默认）| 标量
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 关（默认）| 开
  group: 数据类型选项卡
```

### 主选项卡

### **Sample rate of input signal (Hz)** — 输入信号的采样率（Hz） `48e3`（默认）| 正标量

将输入信号的采样率指定为以 Hz 为单位的正标量。输入采样率必须大于所关注的带宽。

### **Sample rate of output signal (Hz)** — 输出信号的采样率（Hz） `96e3`（默认）| 以 Hz 为单位的正标量

将输出信号的采样率指定为以 Hz 为单位的正标量。输出采样率必须高于或低于输入采样率。

### **Tolerance for output sample rate** — 输出采样率的最大容差 `0`（默认）| 正标量

将输出采样率的最大容差指定为范围 [`0``0.5`] 内的正标量。

实际输出采样率会有所变化，但处于指定范围内。例如，如果您将 **Tolerance for output sample rate** 设置为 0.01，则实际输出采样率处于输出信号采样率 ± 1% 的范围内。这种灵活性允许更简单的滤波器设计。

### **Filter Specification method** — 指定滤波器系数的方法 `Polynomial order`（默认）| `Coefficients`

将模块用于确定多项式插值器系数的方法指定为以下之一：

- `Polynomial order` — 通过 **Polynomial order** 参数指定 Lagrange 插值滤波器多项式的阶数。
- `Coefficients` — 通过 **Coefficients** 参数直接指定多项式系数。

### **Coefficients** — 滤波器多项式系数 `[-1 1; 1 0]`（默认）| 实值方阵

将滤波器多项式系数指定为实值方阵。

#### 依赖关系

要启用此参数，请将 **Filter specification method** 设置为 `Coefficients`。

### **Polynomial order** — Lagrange 插值滤波器多项式的阶数 `3`（默认）| 小于或等于 4 的正整数

将 Lagrange 插值滤波器多项式的阶数指定为 `1`、`2`、`3` 或 `4`。

#### 依赖关系

要启用此参数，请将 **Filter specification method** 设置为 `Polynomial order`。

### **Allow arbitrary frame length for fixed-size input signals** — 允许固定大小输入信号使用任意帧长度 开（默认）| 关

指定固定大小输入信号（其大小在仿真期间不变）是否可以具有任意帧长度，其中帧长度不必是抽取因子的整数倍。该模块仅对固定大小输入信号使用此参数设置，如果输入具有可变大小，则忽略此参数。

当输入信号是可变大小信号时，该信号可以具有任意帧长度，即帧长度不必是抽取因子的整数倍。

对于固定大小输入信号，如果您：

- 选中 **Allow arbitrary frame length for fixed-size input signals** 参数，则信号的帧长度不必是抽取因子的整数倍。如果输入不是抽取因子的整数倍，则输出通常是可变大小信号。因此，为了支持任意输入大小，该模块还必须支持可变大小操作，您可以通过选中 **Allow arbitrary frame length for fixed-size input signals** 参数来启用该操作。
- 清除 **Allow arbitrary frame length for fixed-size input signals** 参数，则输入帧长度必须是抽取因子的整数倍。

### **View Filter Response** — 查看滤波器响应 按钮

打开 FVTool 并显示 Farrow Rate Converter 的幅度/相位响应。该响应基于模块参数。当您更改参数时，FVTool 会更新。

要在 FVTool 运行时更新幅度响应，请修改对话框中的参数并点击 **Apply**。

### **View Info** — 查看信息 按钮

点击此按钮，模块将显示有关 Farrow 滤波器系统的以下信息：

- `Filter Structure`
- `Interpolation Factor`
- `Decimation Factor`
- `Filter Length`
- `Stable`
- `Linear Phase`

此按钮将 `info` 方法的功能引入 Simulink® 环境。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

### 数据类型选项卡

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 整数溢出时的处理方法 关（默认）| 开

当您选中此参数时，模块会对其定点运算的结果进行饱和处理。当您清除此参数时，模块会对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Coefficients** — 滤波器系数的数据类型 `fixdt(1,16)`（默认）| `fixdt(1,16,0)`

将滤波器系数的数据类型指定为有符号定点对象。默认值 `fixdt(1,16)` 对应于具有 16 位系数的有符号定点类型对象。为获得最大精度，模块会根据系数值确定小数长度。

### **Fractional Delay** — 分数延迟的数据类型 `fixdt(0,8)`（默认）| `fixdt(0,16)`

将分数延迟的数据类型指定为无符号定点对象。默认值 `fixdt(0,8)` 对应于具有 8 位字长的无符号定点数据类型对象。为获得最大精度，模块会根据分数延迟值计算小数长度。

### **Multiplicand** — 被乘数的数据类型 `fixdt(1,16,13)`（默认）| `fixdt(1,16,0)`

将被乘数数据类型指定为有符号定点对象。默认值 `fixdt(1,16,13)` 对应于具有 16 位字长和 13 位小数长度的有符号定点被乘数数据类型。

### **Output** — 输出的数据类型 `Inherit: Same word length as input`（默认）| `Inherit: Same as accumulator` | `fixdt(1,16)` | `fixdt(1,16,0)`

将输出数据类型的字长和小数长度指定为以下之一：

- `Inherit: Same word length as input`（默认）—— 输出字长和小数长度与输入相同。
- `Inherit: Same as accumulator` —— 输出字长和小数长度与累加器相同。
- `fixdt(1,16)` —— 具有 16 位字长的有符号定点数据类型。为获得最大精度，模块会根据输入范围计算小数长度，并保留输入的动态范围。
- `fixdt(1,16,0)` —— 具有 16 位字长和零小数长度的有符号定点数据类型。

### **Output Minimum** — 模块可以输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。Simulink 软件使用此最小值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **Output Maximum** — 模块可以输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。Simulink 软件使用此最大值来执行：

- 仿真范围检查。请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 关（默认）| 开

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。
## 所属库

DSP System Toolbox / Signal Operations DSP System Toolbox / Filtering / Multirate Filters

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

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

### R2022b：支持任意输入帧长度

从 R2022b 开始，当满足以下条件时，此模块支持具有任意帧长度的输入信号：

- 输入信号是固定大小信号（帧长度在仿真期间不变）且您选中 **Allow arbitrary frame length for fixed-size input signals** 参数
- 输入信号是可变大小信号（帧长度在仿真期间变化）

当此模块支持任意帧长度输入信号时，输入帧长度不必是抽取因子的整数倍。

## 描述

具有任意转换因子的多项式采样率转换器

Farrow Rate Converter 模块使用多项式拟合采样率转换来转换输入信号的采样率。基于多项式的滤波器在实现分数采样率转换方面非常高效。Farrow 结构是基于多项式的滤波器的一种实现。此模块使用 Farrow 结构来高效地实现任意速率变化因子。速率变化因子可以是无理数。
