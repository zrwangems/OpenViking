---
type: simulink-block
title: 'S-parameters'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband Simulation'
documentation_page: 'sparametersidealizedbaseband'
documentation_source_path: 'ref/sparametersidealizedbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# S-parameters

## 端口

### 输入

### **Port\_1** — 时变输入信号 实数标量 | 实数列 | 复数标量 | 复数列

时变输入信号，指定为实数标量、实数列、复数标量或复数列。列表示连续的时间点。

**数据类型：** `double` | `single`
### 输出

### **Port\_1** — 时变输出信号 复数标量 | 复数列

时变输出信号，返回为复数标量或复数列。输出时变信号的大小与输入时变信号相等。

**数据类型：** `double` | `single`

## 参数

### 主要

### **数据源** — 用于对 RF 复基带 S-parameters 建模的数据源 `file` (默认) | `sparameters` | `rational`

用于对 RF 复基带 S-parameters 建模的数据源，指定为以下项之一：

- `file` — 选择此选项可指定扩展名为 `.s2p` 的 Touchstone 文件。该模块会忽略导入文件中的噪声和非线性数据。
- `sparameters` — 选择此选项可指定 `sparameters` 对象。
- `rational` — 选择此选项可指定 `rational` 对象。

### **文件** — 二端口 Touchstone 数据文件 `unitygain.s2p` (默认) | 字符向量

二端口 Touchstone 文件的名称，指定为字符向量。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `file`。

### **Sparameter 对象** — 使用 `sparameters` 对象作为数据源 `sparameters('unitygain.s2p')` (默认)

选择此参数可使用 `sparameters` 对象作为数据源来对 S-parameters 建模。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `sparameters`。

### **Rational 对象** — 使用 `rational` 对象作为数据源 `rational('unitygain.s2p','TendsToZero',false)` (默认)

选择此参数可使用 `rational` 对象作为数据源来对 S-parameters 建模。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `rational`。

### **载波频率 (Hz)** — 对 S-parameters 建模时的载波频率 `1000000000` (默认) | 正实数标量

对 S-parameters 建模时的载波频率，指定为以 Hz 为单位的正实数标量。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

要运行的仿真类型，指定为以下项之一：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项时慢。使用此模式可调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时快。

### 建模

### **建模域** — 建模域 `Time (Fixed step)` (默认) | `Time (Continuous)` | `Frequency (Digital filter)`

建模域，指定为以下项之一：

- `Time(Fixed step)` — 使用固定步长求解器（`NDF2`、`Trapezoidal` 和 `Backward Euler`）建模
- `Time(Continuous)` — 使用连续或刚性求解器（`ode15s`、`ode23s`、`ode23t` 和 `ode23tb`）建模
- `Frequency (Digital filter)` — 使用一维数字滤波器建模。

### **求解器** — 时域求解器 `NDF2` (默认) | `Trapezoidal` | `Backward Euler` | `ode15s` | `ode23s` | `ode23t (trap)` | `ode23tb (trap+BE)`

固定步长和连续时域求解器，指定为以下项之一：

**固定步长求解器**

- `NDF2` — 平衡窄带和宽带精度。当系统中信号的频率内容相对于 Nyquist 率未知时，此求解器适用。
- `Trapezoidal` — 执行窄带仿真。频率畸变和缺少阻尼效应使此方法不适用于大多数宽带仿真。
- `Backward Euler` — 仿真最大类别的系统和信号。阻尼效应使此求解器适用于宽带仿真，但整体精度较低。

**连续求解器**

- `ode15s` — 使用变阶方法求解刚性微分方程和 DAE
- `ode23s` — 使用低阶方法求解刚性微分方程
- `ode23t (trap)` — 使用梯形规则求解中等刚性 ODE 和 DAE
- `ode23tb (trap+BE)` — 使用梯形规则和后向微分公式求解刚性微分方程

#### 依赖关系

要启用：

- 固定步长时域求解器，请将 **建模域** 设置为 `Time(Fixed step)`。
- 连续时域求解器，请将 **建模域** 设置为 `Time (Continuous)`。

### **极点拟合选项** — 有理拟合选项 `Share all poles` (默认) | `Fit individually` | `Share poles by columns`

用于控制复频率相关数据拟合过程的有理拟合选项，指定为 `Share all poles`、`Fit individually` 或 `Share poles by columns`。

#### 依赖关系

要设置此参数，请将 **数据源** 设置为 `file` 或 `sparameters`。

### **Rational 参数** — 用于控制拟合的有理拟合参数 `{ 'Tolerance',-40,'TendsToZero',false,'MaxPoles',48,'Qlimit',inf }` (默认) | 元胞数组

用于控制拟合的有理拟合参数，指定为元胞数组。

#### 依赖关系

要设置此参数，请将 **数据源** 设置为 `file` 或 `sparameters`。

### **FIR 滤波器长度** — 一维数字滤波器的滤波器长度 `128` (默认) | 正整数

一维数字滤波器的滤波器长度或冲激响应持续时间，指定为正整数。

#### 依赖关系

要设置此参数，请将 **建模域** 设置为 `Frequency (Digital filter)`。

### 可视化

### **第一个绘图类型** — 绘图类型 `S21` (默认) | `Phase delay` | `Group delay` | `Impulse response` | `Step response`

第一个绘图的绘图类型，指定为以下项之一：

- `S21`
- `Phase delay`
- `Group delay`
- `Impulse response`
- `Step response`

### **冲激响应参数** — 用于绘制冲激响应的输入参数 `[ 1e-11, 1e4]` (默认) | 二元素向量

用于绘制冲激响应的输入参数，指定为二元素向量。通过在此参数中指定输入信号的采样时间和采样点数来绘制冲激响应。有关详细信息，请参阅 `impulse`。

#### 依赖关系

要设置此参数，请将 **第一个绘图类型** 或 **第二个绘图类型** 设置为 `Impulse response`。

### **阶跃响应参数** — 用于绘制阶跃响应的输入参数 `[ 1e-11, 1e4, 1e-10 ]` (默认) | 三元素向量

用于绘制阶跃响应的输入参数，指定为三元素向量。通过在此参数中指定输入信号的采样时间、采样点数以及阶跃信号达到最大值所需的时间来绘制阶跃响应。有关详细信息，请参阅 `stepresp`。

#### 依赖关系

要设置此参数，请将 **第一个绘图类型** 或 **第二个绘图类型** 设置为 `Step response`。

### **第一个绘图 y 轴单位** — 第一个绘图的 y 轴单位 `Magnitude (dB)` (默认) | `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

第一个绘图的 y 轴单位，指定为以下项之一：

- `Magnitude (dB)`
- `Magnitude (linear)`
- `Angle (degrees)`
- `Real`
- `Imaginary`

#### 依赖关系

要设置此参数，请将 **第一个绘图类型** 设置为 `S21`。

### **第二个绘图类型** — 第二个绘图的绘图类型 `None` (默认) | `S21` | `Phase delay` | `Group delay` | `Impulse response` | `Step response`

第二个绘图的绘图类型，指定为以下项之一：

- `None`
- `S21`
- `Phase delay`
- `Group delay`
- `Impulse response`
- `Step response`

### **第二个绘图 y 轴单位** — 第二个绘图的 y 轴单位 `Magnitude (dB)` (默认) | `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

第二个绘图的 y 轴单位，指定为以下项之一：

- `Magnitude (dB)`
- `Magnitude (linear)`
- `Angle (degrees)`
- `Real`
- `Imaginary`

#### 依赖关系

要设置此参数，请将 **第二个绘图类型** 设置为 `S21`。

### **X 轴频率点 (Hz)** — 用于绘制 S-parameter 数据的频率点 `logspace(8,10,2001)` (默认) | 正实数向量

用于绘制 S-parameter 数据的频率点，指定为以 Hz 为单位的正实数向量。

### **X 轴刻度** — 线性或对数 X 轴刻度 `Linear` (默认) | `Logarithmic`

选择此参数可将数据绘制在线性或对数 X 轴刻度上。指定 `Linear` 或 `Logarithmic`。

### **Y 轴刻度** — 线性或对数 Y 轴刻度 `Linear` (默认) | `Logarithmic`

选择此参数可将数据绘制在线性或对数 Y 轴刻度上。指定 `Linear` 或 `Logarithmic`。

### **绘制 Sparameter 特性** — 绘制 S-parameters 数据按钮

选择此按钮可绘制 S-parameters 数据的特性。

## 所属库

RF Blockset / Idealized Baseband

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2025a: Idealized Baseband 库中 S-Parameter 模块的参数已重命名

Idealized Baseband 库中 S-parameters 模块的 **RF 频率 (Hz)** 参数已重命名为 **载波频率 (Hz)**。

打开包含 S-parameter 模块且在 R2024b 中创建的模型时，软件会将 **RF 频率 (Hz)** 参数替换为 **载波频率 (Hz)** 参数。

### R2024b: idealized baseband 库中 S-parameters 模块的参数已重命名

idealized baseband 库中 S-parameters 模块的以下参数已重命名。

| R2024b 之前的参数名称 | 自 R2024b 起的参数名称 |
| --- | --- |
| **数据文件** | **文件** |
| **载波频率 (Hz)** | **RF 频率 (Hz)** |

以下参数值在 idealized baseband 库中的 S-parameters 模块中已更改。

| 参数 | R2024b 之前的值 | 自 R2024b 起的值 |
| --- | --- | --- |
| **数据源** | `Data file` | `file` |
| `S-parameters object` | `sparameters` |
| `Rational object` | `rational` |
| **建模域** | `Time domain (Fixed step)` | `Time (Fixed step)` |
| `Time domain (Continuous)` | `Time (Continuous)` |
| `Frequency domain (Digital filter)` | `Frequency (Digital filter)` |

打开包含 S-parameters 模块且在 R2024b 之前创建的模型时，软件会按照表中所示替换参数名称和值。

## 描述

在 Simulink 中对 RF 复基带 S-parameters 建模

使用 Idealized Baseband S-parameter block 在 Simulink® 中对 RF 复基带 S-parameters 建模。您可以将 S-parameters 作为 Touchstone 文件、`sparameters` 对象或 `rational` 对象输入。如果使用 Touchstone 文件或 `sparameters` 对象描述 S-parameters，软件会使用有理拟合来推导 `rational` 对象。您还可以在时域或频域中对 S-parameters 数据建模，并绘制 S-parameters 特性。

如果要设计具有阻抗失配的 S-parameters，请使用 Circuit Envelope S-Parameters block。
