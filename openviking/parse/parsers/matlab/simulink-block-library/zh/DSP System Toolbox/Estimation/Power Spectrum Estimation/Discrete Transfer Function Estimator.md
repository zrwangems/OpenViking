---
type: simulink-block
title: 'Discrete Transfer Function Estimator'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Power Spectrum Estimation'
documentation_page: 'discretetransferfunctionestimator'
documentation_source_path: 'ref/discretetransferfunctionestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Transfer Function Estimator

## 端口

### 输入

### **x** — 系统输入信号 向量 | 矩阵

将系统输入信号指定为向量或矩阵。

输入 *x* 和 *y* 必须具有相同的大小和数据类型。

**数据类型：** `double` | `single`

### **y** — 系统输出信号 向量 | 矩阵

将系统输出信号指定为向量或矩阵。

输入 *x* 和 *y* 必须具有相同的大小和数据类型。

**数据类型：** `double` | `single`
### 输出

### **Output** — 传递函数估计 向量 | 矩阵

传递函数估计，以向量或矩阵形式返回。有关该模块如何计算传递函数估计的更多详细信息，请参阅算法。

**数据类型：** `double` | `single`

## 参数

### **Window length source** — 窗长来源 `Same as input frame length`（默认）| `Specify on dialog`

指定窗长值的来源。您可以将此参数设置为：

- `Same as input frame length` —— 窗长设置为输入的帧大小。
- `Specify on dialog` —— 窗长为在 **Window length** 中指定的值。

### **Window length** — 窗长 `1024`（默认）| 正整数 ≥ 2

指定用于计算频谱估计的窗长（以采样点为单位），为大于或等于 `2` 的正整数。

#### 依赖关系

要启用此参数，请将 **Window length source** 设置为 `Specify on dialog`。

### **Window overlap (%)** — 窗之间的重叠百分比 `0`（默认）| 非负标量

指定连续数据窗之间的重叠百分比，为范围 [`0`,`100`) 内的非负标量。

### **Averaging method** — 平均方法 `Running`（默认）| `Exponential`

将平均方法指定为 `Running` 或 `Exponential`。在运行平均方法中，该模块计算由 **Number of spectral averages** 参数定义的指定数量的频谱估计的等权平均值。在指数方法中，该模块计算按指数衰减遗忘因子加权的样本平均值。

### **Specify forgetting factor from input port** — 从输入端口指定遗忘因子 `off`（默认）| `on`

选中此复选框以从输入端口指定遗忘因子。当您不选中此复选框时，遗忘因子通过 **Forgetting factor** 参数指定。

#### 依赖关系

要启用此参数，请将 **Averaging method** 设置为 `Exponential`。

### **Forgetting factor** — 遗忘因子 `0.9`（默认）| 正标量 ≤ `1`

将指数加权遗忘因子指定为 ≤ `1` 的正标量。

#### 依赖关系

要启用此参数，请将 **Averaging method** 设置为 `Exponential`，并清除 **Specify forgetting factor from input port** 参数。

### **Number of spectral averages** — 频谱平均次数 `1`（默认）| 正整数

将频谱平均次数指定为正整数。Transfer Function Estimator 模块通过对最近 *N* 个估计求平均来计算当前估计。*N* 为频谱平均次数。

#### 依赖关系

要启用此参数，请将 **Averaging method** 设置为 `Running`。

### **FFT length source** — FFT 长度值的来源 `Auto`（默认）| `Property`

将 FFT 长度值的来源指定为 `Auto` 或 `Property`。

当 FFT 长度的来源设置为 `Auto` 时，该模块将 FFT 长度设置为输入帧大小。当 FFT 长度的来源设置为 `Property` 时，您在 **FFT length** 参数中指定 FFT 长度。

### **FFT length** — FFT 长度 `128`（默认）| 正整数

将 Discrete Transfer Function Estimator 模块用于计算频谱估计的 FFT 长度指定为正整数。

### **Window function** — 窗函数 `Hann`（默认）| `Chebyshev` | `Flat Top` | `Hamming` | `Kaiser` | `Rectangular`

为 Discrete Transfer Function Estimator 模块指定窗函数。可能的值为：

- `Hann`
- `Chebyshev`
- `Flat Top`
- `Hamming`
- `Kaiser`
- `Rectangular`

### **Sidelobe attenuation of window (dB)** — 窗的旁瓣衰减 `60`（默认）| 正标量

将窗的旁瓣衰减指定为以 dB 为单位的正标量。

#### 依赖关系

要启用此参数，请将 **Window function** 设置为 `Kaiser` 或 `Chebyshev`。

### **Frequency range** — 传递函数估计的频率范围 `Centered`（默认）| `One-sided` | `Two-sided`

指定传递函数估计的频率范围。

- `Centered` —— 该模块计算实数或复数输入信号 *x* 和 *y* 的中心双边传递函数。
- `onesided` —— 该模块计算实数输入信号 *x* 和 *y* 的单边传递函数。
- `twosided` —— 该模块计算实数或复数输入信号 *x* 和 *y* 的双边传递函数。

### **Output magnitude squared coherence estimate** — 幅度平方相干估计 `off`（默认）| `on`

选中此复选框以使用 Welch 平均修正周期图方法计算并输出幅度平方相干估计。幅度平方相干估计指示两个输入在每个频率上彼此的对应程度。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，C 代码将复用于后续仿真。此选项需要额外的启动时间，但可提供更快的后续仿真。

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

**在 R2014a 中引入**

### R2024a：**Simulate using** 参数默认值的变化

**Simulate using** 参数的默认值现在为 `Interpreted execution`。通过此更改，该模块默认使用 MATLAB 解释器进行仿真。

## 描述

计算系统频域传递函数的估计

Discrete Transfer Function Estimator 模块使用 Welch 平均修正周期图方法估计系统的频域传递函数。

该模块将输入数据缓冲为重叠段。您可以通过在模块对话框中设置的参数来设置数据段的长度和数据重叠量。该模块的采样率等于 1/*T*。*T* 是模块输入的采样时间。

该模块首先对两个输入 *x* 和 *y* 应用窗函数，然后按窗功率对其进行缩放。它对每个信号进行 FFT，分别称为 *X* 和 *Y*。该模块计算 *Pxx*，即 FFT *X* 的幅度平方。然后该模块计算 *Pyx*，即 *X* 乘以 *Y* 的共轭。输出传递函数估计 *H* 通过将 *Pyx* 除以 *Pxx* 计算得出。
