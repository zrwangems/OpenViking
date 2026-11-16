---
type: simulink-block
title: 'Filter'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband Simulation'
documentation_page: 'filteridealizedbaseband'
documentation_source_path: 'ref/filteridealizedbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# Filter

## 端口

### 输入

### **Port\_1** — 时变输入信号 实标量 | 实列 | 复标量 | 复列

时变输入信号，指定为实标量、实列、复标量或复列。列表示连续的时间点。

**数据类型：** `double` | `single`
### 输出

### **Port\_1** — 时变输出信号 复标量 | 复列

时变输出信号，返回为复标量或复列。输出时变信号的大小等于输入时变信号。

**数据类型：** `double` | `single`

## 参数

### 主要

### **设计方法** — 滤波器设计方法 `Butterworth`（默认）| `Chebyshev` | `Inverse Chebyshev`

滤波器设计方法，指定为以下项之一：

- `Butterworth`
- `Chebyshev`
- `Inverse Chebyshev`

### **滤波器类型** — 滤波器响应类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器响应类型，指定为以下项之一：

- `Lowpass` — 使用 **设计方法** 中指定的设计模拟低通滤波器类型。
- `Highpass` — 使用 **设计方法** 中指定的设计模拟高通滤波器类型。
- `Bandpass` — 使用 **设计方法** 中指定的设计模拟带通滤波器类型。
- `Bandstop` — 使用 **设计方法** 中指定的设计模拟带阻滤波器类型。

### **使用滤波器阶数实现** — 使用滤波器阶数实现 `off`（默认）| `on`

选择此参数以手动实现滤波器阶数。

### **滤波器阶数** — 滤波器阶数 `3`（默认）| 大于 `2` 的整数

滤波器阶数，指定为大于 `2` 的整数。如果将 **滤波器设计** 设置为 `Lowpass` 或 `Highpass`，请指定集总储能元件的数量。如果将 **滤波器设计** 设置为 `Bandpass` 或 `Bandstop`，请指定集总储能元件数量的两倍。

#### 依赖关系

要启用此参数，请选择 **使用滤波器阶数实现**。

### **通带频率 (Hz)** — 通带频率 `1e9`（默认）| 正实标量 | 正升序二元组向量

低通、高通和带通滤波器类型的通带频率，指定为正实标量或以 Hz 为正的升序二元组向量。根据 **滤波器类型**，可接受的值类型和默认值如下不同。

| 滤波器类型 | 值类型 | 默认值 (Hz) |
| --- | --- | --- |
| Lowpass | 正实标量 | `1e9` |
| Highpass | 正实标量 | `2000000000` |
| Bandpass | 正升序二元组向量 | `[2000000000 3000000000]` |

#### 依赖关系

要启用此参数，请将 **滤波器类型** 设置为 `Lowpass`、`Highpass` 或 `Bandpass`。

### **通带衰减 (dB)** — 通带衰减 `10*log10(2)`（默认）| 正实标量

滤波器的通带衰减，指定为以 dB 为单位的正实标量。对于带通滤波器，此值同等应用于通带的两侧边缘。

#### 依赖关系

要启用此参数，请将 **滤波器类型** 设置为 `Lowpass`、`Highpass` 或 `Bandpass`。

### **阻带频率 (Hz)** — 带阻滤波器的阻带频率 `2000000000`（默认）| 正实标量 | 正升序二元组向量

带阻滤波器的阻带频率，指定为以 Hz 为单位的正实标量或正升序二元组向量。根据 **滤波器类型** 和 **使用滤波器阶数实现** 参数，可接受的值类型和默认值如下不同。

| 滤波器类型 | 值类型 | 默认值 (Hz) | 启用此参数的方法 |
| --- | --- | --- | --- |
| Lowpass | 正实标量 | `2000000000` | 将 **滤波器类型** 设置为 `Lowpass` 并清除 **使用滤波器阶数实现**。 |
| Highpass | 正实标量 | `1000000000` | 将 **滤波器类型** 设置为 `Highpass` 并清除 **使用滤波器阶数实现**。 |
| Bandpass | 正升序二元组向量 | `[1500000000 3500000000]` | 将 **滤波器类型** 设置为 `Bandpass` 并清除 **使用滤波器阶数实现**。 |
| Bandstop | 正升序二元组向量 | `[2100000000 2900000000]` | 将 **滤波器类型** 设置为 `Bandstop` 并清除或选择 **使用滤波器阶数实现**。 |

### **阻带衰减 (dB)** — 阻带衰减 `40`（默认）| 正实标量

阻带衰减，指定为大于 **通带衰减 (dB)** 值的正实标量，以 dB 为单位。

#### 依赖关系

要启用此参数，您可以执行以下任一操作：

- 将 **滤波器类型** 设置为 `Lowpass`、`Highpass` 或 `Bandpass`，并清除 **使用滤波器阶数实现**。
- 将 **滤波器类型** 设置为 `Bandstop`，选择 **使用滤波器阶数实现**。

### **RF 频率 (Hz)** — 信号带宽中心 `1000000000`（默认）| 正实标量

相对于滤波器传递函数的信号带宽中心，指定为以 Hz 为单位的正实标量。信号带宽为 1Simulink Step Size。

### **模拟使用** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为以下项之一：

- `Interpreted execution` — 使用 MATLAB® 解释器模拟模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项时慢。使用此模式可调试模块的源代码。
- `Code generation` — 使用生成的 C 代码模拟模型。首次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不变，C 代码会重用于后续仿真。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时快。

### 建模

### **建模域** — 建模域 `Time (Fixed step)`（默认）| `Time (Continuous)` | `Frequency (Digital filter)`

建模域，指定为以下项之一：

- `Time (Fixed step)` — 使用固定步长求解器（`NDF2`、`Trapezoidal` 和 `Backward Euler`）建模
- `Time(Continuous)` — 使用连续或刚性求解器（`ode15s`、`ode23s`、`ode23t` 和 `ode23tb`）建模
- `Frequency (Digital filter)` — 使用一维数字滤波器建模。

### **求解器** — 时域求解器 `NDF2`（默认）| `Trapezoidal` | `Backward Euler` | `ode15s` | `ode23s` | `ode23t (trap)` | `ode23tb (trap+BE)`

固定步长和连续时域求解器，指定为以下项之一：

**固定步长求解器**

- `NDF2` — 平衡窄带和宽带精度。当系统中信号的频率内容相对于 Nyquist 速率未知时，此求解器适用。
- `Trapezoidal` — 执行窄带仿真。频率扭曲和缺少阻尼效应使此方法不适用于大多数宽带仿真。
- `Backward Euler` — 模拟最大类别的系统和信号。阻尼效应使此求解器适用于宽带仿真，但整体精度较低。

**连续求解器**

- `ode15s` — 使用可变阶方法求解刚性微分方程和 DAE
- `ode23s` — 使用低阶方法求解刚性微分方程
- `ode23t (trap)` — 使用梯形法则求解中等刚性 ODE 和 DAE
- `ode23tb (trap+BE)` — 使用梯形法则和后向差分公式求解刚性微分方程

#### 依赖关系

要启用：

- 固定步长时域求解器，请将 **建模域** 设置为 `Time (Fixed step)`。
- 连续时域求解器，请将 **建模域** 设置为 `Time (Continuous)`。

### **FIR 滤波器长度** — 一维数字滤波器的滤波器长度 `128`（默认）| 正实数整数

一维数字滤波器的滤波器长度或冲激响应持续时间，指定为正实数整数。

#### 依赖关系

要设置此参数，请将 **建模域** 设置为 `Frequency (Digital filter)`。

### 可视化

### **第一个绘图类型** — 绘图类型 `S21`（默认）| `Phase delay` | `Group delay` | `Impulse response` | `Step response`

第一个绘图的绘图类型，指定为以下项之一：

- `S21`
- `Phase delay`
- `Group delay`
- `Impulse response`
- `Step response`

### **冲激响应参数** — 用于绘制冲激响应的输入参数 `[ 1e-11, 1e4]`（默认）| 二元素向量

用于绘制冲激响应的输入参数，指定为二元素向量。通过在此参数中指定输入信号的采样时间和样本数来绘制冲激响应。有关详细信息，请参阅 `impulse`。

#### 依赖关系

要设置此参数，请将 **第一个绘图类型** 或 **第二个绘图类型** 设置为 `Impulse response`。

### **阶跃响应参数** — 用于绘制阶跃响应的输入参数 `[ 1e-11, 1e4, 1e-10 ]`（默认）| 三元素向量

用于绘制阶跃响应的输入参数，指定为三元素向量。通过在此参数中指定输入信号的采样时间、样本数以及阶跃信号达到最大值所需的时间来绘制阶跃响应。有关详细信息，请参阅 `stepresp`。

#### 依赖关系

要设置此参数，请将 **第一个绘图类型** 或 **第二个绘图类型** 设置为 `Step response`。

### **第一个绘图的 y 轴单位** — 第一个绘图的 Y 轴单位 `Magnitude (dB)`（默认）| `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

第一个绘图的 Y 轴单位，指定为以下项之一：

- `Magnitude (dB)`
- `Magnitude (linear)`
- `Angle (degrees)`
- `Real`
- `Imaginary`

#### 依赖关系

要设置此参数，请将 **第一个绘图类型** 设置为 `S21`。

### **第二个绘图类型** — 第二个绘图的绘图类型 `None`（默认）| `S21` | `Phase delay` | `Group delay` | `Impulse response` | `Step response`

第二个绘图的绘图类型，指定为以下项之一：

- `None`
- `S21`
- `Phase delay`
- `Group delay`
- `Impulse response`
- `Step response`

### **第二个绘图的 y 轴单位** — 第二个绘图的 Y 轴单位 `Magnitude (dB)`（默认）| `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

第二个绘图的 Y 轴单位，指定为以下项之一：

- `Magnitude (dB)`
- `Magnitude (linear)`
- `Angle (degrees)`
- `Real`
- `Imaginary`

#### 依赖关系

要设置此参数，请将 **第二个绘图类型** 设置为 `S21`。

### **X 轴频率点 (Hz)** — 用于绘制 S 参数数据的频率点 `logspace(8,10,2001)`（默认）| 正实向量

用于绘制 S 参数数据的频率点，指定为以 Hz 为单位的正实向量。

### **X 轴刻度** — 线性或对数 X 轴刻度 `Linear`（默认）| `Logarithmic`

选择此参数可将数据绘制在线性或对数 X 轴刻度上。指定 `Linear` 或 `Logarithmic`。

### **Y 轴刻度** — 线性或对数 Y 轴刻度 `Linear`（默认）| `Logarithmic`

选择此参数可将数据绘制在线性或对数 Y 轴刻度上。指定 `Linear` 或 `Logarithmic`。

### **绘制 S 参数特性** — 绘制 S 参数数据按钮

选择此按钮可绘制 S 参数数据的特性。

## 所属库

RF Blockset / Idealized Baseband

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2024b：理想化基带库中 Filter 模块的参数已重命名

理想化基带库中 Filter 模块中的以下内容已重命名：

| R2024b 之前的参数名称 | R2024b 之后的参数名称 |
| --- | --- |
| **载波频率 (Hz)** | **RF 频率 (Hz)** |

理想化基带库中 Filter 模块中的以下参数值已更改。

| 参数 | R2024b 之前的值 | R2024b 之后的值 |
| --- | --- | --- |
| **建模域** | `Time domain (Fixed step)` | `Time (Fixed step)` |
| `Time domain (Continuous)` | `Time (Continuous)` |
| `Frequency domain (Digital filter)` | `Frequency (Digital filter)` |

当您打开包含 S-parameters 模块且在 R2024b 之前创建的模型时，软件会按表中所示替换参数名称和值。

### R2023a：Lowpass RF、Highpass RF、Bandpass RF 和 Bandstop RF Filter 模块已被替换

从 R2023a 开始，理想化基带 Filter 模块替换 Lowpass RF Filter、Highpass RF Filter、Bandpass RF Filter 和 Bandstop RF Filter 模块。

当您打开包含 Lowpass RF Filter、Highpass RF Filter、Bandpass RF Filter 和 Bandstop RF Filter Filter 模块且在 R2023a 之前创建的模型时，软件会用新的理想化基带 Filter 模块替换旧模块。

## 描述

在 Simulink 中滤波 RF 复基带信号

使用 Idealized Baseband Filter 模块在 Simulink 中滤波 RF 复基带信号。您可以使用 Butterworth、Chebyshev 或 inverse Chebyshev 设计方法来设计滤波器。您还可以在时域或频域中对滤波器建模，并绘制滤波器特性。

要设计具有阻抗失配的 RF 滤波器，请使用 Circuit Envelope Filter 模块。

**注意**

Idealized Baseband Filter 模块替换 Lowpass RF Filter、Highpass RF Filter、Bandpass RF Filter 和 Bandstop RF Filter 模块。
