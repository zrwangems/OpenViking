---
type: simulink-block
title: 'Filter'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'filteridealizedbaseband'
documentation_source_path: 'ref/filteridealizedbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# Filter

## 端口

### 输入

### **Port\_1** — 时变输入信号 实数标量 | 实数列向量 | 复数标量 | 复数列向量

时变输入信号，指定为实数标量、实数列向量、复数标量或复数列向量。列向量表示连续的时间点。

**数据类型：** `double` | `single`
### 输出

### **Port\_1** — 时变输出信号 复数标量 | 复数列向量

时变输出信号，返回为复数标量或复数列向量。输出时变信号的大小与输入时变信号相等。

**数据类型：** `double` | `single`

## 参数

### 主要

### **Design method** — 滤波器设计方法 `Butterworth`（默认）| `Chebyshev` | `Inverse Chebyshev`

滤波器设计方法，指定为以下之一：

- `Butterworth`
- `Chebyshev`
- `Inverse Chebyshev`

### **Filter type** — 滤波器响应类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器响应类型，指定为以下之一：

- `Lowpass` — 使用 **Design method** 中指定的设计模拟低通滤波器类型。
- `Highpass` — 使用 **Design method** 中指定的设计模拟高通滤波器类型。
- `Bandpass` — 使用 **Design method** 中指定的设计模拟带通滤波器类型。
- `Bandstop` — 使用 **Design method** 中指定的设计模拟带阻滤波器类型。

### **Implement using filter order** — 使用滤波器阶数实现 `off`（默认）| `on`

选择此参数以手动实现滤波器阶数。

### **Filter order** — 滤波器阶数 `3`（默认）| 大于 `2` 的整数

滤波器阶数，指定为大于 `2` 的整数。如果将 **Filter design** 设置为 `Lowpass` 或 `Highpass`，请指定集总储能元件的数量。如果将 **Filter design** 设置为 `Bandpass` 或 `Bandstop`，请指定集总储能元件数量的两倍。

#### 依赖关系

要启用此参数，请选择 **Implement using filter order**。

### **Passband frequency (Hz)** — 通带频率 `1e9`（默认）| 正实数标量 | 正递增二元向量

低通、高通和带通滤波器类型的通带频率，以 Hz 为单位指定为正实数标量或正递增二元向量。根据 **Filter Type** 的不同，可接受的值类型和默认值如下所示。

| 滤波器类型 | 值类型 | 默认值 (Hz) |
| --- | --- | --- |
| Lowpass | 正实数标量 | `1e9` |
| Highpass | 正实数标量 | `2000000000` |
| Bandpass | 正递增二元向量 | `[2000000000 3000000000]` |

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Lowpass`、`Highpass` 或 `Bandpass`。

### **Passband attenuation (dB)** — 通带衰减 `10*log10(2)`（默认）| 正实数标量

滤波器的通带衰减，以 dB 为单位指定为正实数标量。对于带通滤波器，此值同等应用于通带的两侧边缘。

#### 依赖关系

要启用此参数，请将 **Filter type** 设置为 `Lowpass`、`Highpass` 或 `Bandpass`。

### **阻带频率 (Hz)** — 带阻滤波器的阻带频率 `2000000000`（默认）| 正实数标量 | 正递增二元组向量

带阻滤波器的阻带频率，指定为正实数标量或正递增二元组向量，单位为 Hz。根据 **Filter Type** 和 **Implement using filter order** 参数，可接受的值类型和默认值有所不同，如下所示。

| 滤波器类型 | 值类型 | 默认值 (Hz) | 启用此参数的条件 |
| --- | --- | --- | --- |
| 低通 | 正实数标量 | `2000000000` | 将 **Filter type** 设置为 `Lowpass` 并清除 **Implement using filter order**。 |
| 高通 | 正实数标量 | `1000000000` | 将 **Filter type** 设置为 `Highpass` 并清除 **Implement using filter order**。 |
| 带通 | 正递增二元组向量 | `[1500000000 3500000000]` | 将 **Filter type** 设置为 `Bandpass` 并清除 **Implement using filter order**。 |
| 带阻 | 正递增二元组向量 | `[2100000000 2900000000]` | 将 **Filter type** 设置为 `Bandstop` 并清除或选中 **Implement using filter order**。 |

### **阻带衰减 (dB)** — 阻带衰减 `40`（默认）| 正实数标量

阻带衰减，指定为大于 **Passband attenuation (dB)** 值的正实数标量，单位为 dB。

#### 依赖关系

要启用此参数，您可以执行以下任一操作：

- 将 **Filter type** 设置为 `Lowpass`、`Highpass` 或 `Bandpass`，并清除 **Implement using filter order**。
- 将 **Filter type** 设置为 `Bandstop`，选中 **Implement using filter order**。

### **RF 频率 (Hz)** — 信号带宽中心 `1000000000`（默认）| 正实数标量

相对于滤波器传递函数的信号带宽中心，指定为正实数标量，单位为 Hz。信号带宽为 1Simulink Step Size。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为以下之一：

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项时慢。使用此模式可调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时更快。

### 建模

### **建模域** — 建模域 `Time (Fixed step)`（默认）| `Time (Continuous)` | `Frequency (Digital filter)`

建模域，指定为以下之一：

- `Time (Fixed step)` — 使用固定步长求解器（`NDF2`、`Trapezoidal` 和 `Backward Euler`）建模
- `Time(Continuous)` — 使用连续或刚性求解器（`ode15s`、`ode23s`、`ode23t` 和 `ode23tb`）建模
- `Frequency (Digital filter)` — 使用一维数字滤波器建模。

### **Solver** — 时域求解器 `NDF2`（默认）| `Trapezoidal` | `Backward Euler` | `ode15s` | `ode23s` | `ode23t (trap)` | `ode23tb (trap+BE)`

固定步长和连续时域求解器，指定为以下之一：

**固定步长求解器**

- `NDF2` — 平衡窄带和宽带精度。
  该求解器适用于系统中信号的频率内容相对于奈奎斯特速率未知的情况。
- `Trapezoidal` — 执行窄带仿真。
  频率畸变和缺乏阻尼效应使得该方法不适用于大多数宽带仿真。
- `Backward Euler` — 仿真最大类别的系统和信号。阻尼效应使得该求解器适用于宽带仿真，但整体精度较低。

**连续求解器**

- `ode15s` — 使用变阶方法求解刚性微分方程和 DAE
- `ode23s` — 使用低阶方法求解刚性微分方程
- `ode23t (trap)` — 使用梯形规则求解中等刚性 ODE 和 DAE
- `ode23tb (trap+BE)` — 使用梯形规则和后向差分公式求解刚性微分方程

#### 依赖关系

要启用：

- 固定步长时域求解器，将 **Modeling domain** 设置为 `Time (Fixed step)`。
- 连续时域求解器，将 **Modeling domain** 设置为 `Time (Continuous)`。

### **FIR filter length** — 一维数字滤波器的滤波器长度 `128`（默认）| 实正整数

一维数字滤波器的滤波器长度或冲激响应持续时间，指定为实正整数。

#### 依赖关系

要设置此参数，将 **Modeling domain** 设置为 `Frequency (Digital filter)`。

### 可视化

### **First plot type** — 绘图类型 `S21`（默认）| `Phase delay` | `Group delay` | `Impulse response` | `Step response`

第一个绘图的绘图类型，指定为以下之一：

- `S21`
- `Phase delay`
- `Group delay`
- `Impulse response`
- `Step response`

### **Impulse response arguments** — 绘制冲激响应的输入参数 `[ 1e-11, 1e4]`（默认）| 二元素向量

绘制冲激响应的输入参数，指定为二元素向量。通过在此参数中指定输入信号的采样时间和采样点数来绘制冲激响应。有关详细信息，请参阅 `impulse`。

#### 依赖关系

要设置此参数，将 **First plot type** 或 **Second plot type** 设置为 `Impulse response`。

### **Step response arguments** — 绘制阶跃响应的输入参数 `[ 1e-11, 1e4, 1e-10 ]`（默认）| 三元素向量

绘制阶跃响应的输入参数，指定为三元素向量。通过在此参数中指定输入信号的采样时间、采样点数以及阶跃信号达到最大值所需的时间来绘制阶跃响应。有关详细信息，请参阅 `stepresp`。

#### 依赖关系

要设置此参数，将 **First plot type** 或 **Second plot type** 设置为 `Step response`。

### **First plot y-axis units** — 第一个绘图的 y 轴单位 `Magnitude (dB)`（默认）| `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

第一个绘图的 y 轴单位，指定为以下之一：

- `Magnitude (dB)`
- `Magnitude (linear)`
- `Angle (degrees)`
- `Real`
- `Imaginary`

#### 依赖关系

要设置此参数，将 **First plot type** 设置为 `S21`。

### **Second Plot type** — 第二个绘图的绘图类型 `None`（默认）| `S21` | `Phase delay` | `Group delay` | `Impulse response` | `Step response`

第二个绘图的绘图类型，指定为以下之一：

- `None`
- `S21`
- `Phase delay`
- `Group delay`
- `Impulse response`
- `Step response`

### **Second plot y-axis units** — 第二个图的 Y 轴单位 `Magnitude (dB)`（默认）| `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

第二个图的 Y 轴单位，指定为以下之一：

- `Magnitude (dB)`
- `Magnitude (linear)`
- `Angle (degrees)`
- `Real`
- `Imaginary`

#### 依赖关系

要设置此参数，请将 **Second plot type** 设置为
`S21`。

### **X-axis frequency points (Hz)** — 用于绘制 S 参数数据的频率点 `logspace(8,10,2001)`（默认）| 正实数向量

用于绘制 S 参数数据的频率点，指定为以 Hz 为单位的正实数向量。

### **X-axis scale** — 线性或对数 X 轴刻度 `Linear`（默认）| `Logarithmic`

选择此参数可将数据绘制在线性或对数 X 轴刻度上。
指定 `Linear` 或
`Logarithmic`。

### **Y-axis scale** — 线性或对数 Y 轴刻度 `Linear`（默认）| `Logarithmic`

选择此参数可将数据绘制在线性或对数 Y 轴刻度上。
指定 `Linear` 或
`Logarithmic`。

### **Plot Sparameter characteristics** — 绘制 S 参数数据按钮

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

理想化基带库中 Filter 模块的以下内容
已重命名：

| R2024b 之前的参数名称 | R2024b 起的参数名称 |
| --- | --- |
| **Carrier frequency (Hz)** | **RF frequency (Hz)** |

理想化基带库中 Filter 模块的以下参数值
已更改。

| 参数 | R2024b 之前的值 | R2024b 起的值 |
| --- | --- | --- |
| **Modeling domain** | `Time domain (Fixed step)` | `Time (Fixed step)` |
| `Time domain (Continuous)` | `Time (Continuous)` |
| `Frequency domain (Digital filter)` | `Frequency (Digital filter)` |

当您打开在 R2024b 之前创建的包含 S-parameters 模块的模型时，
软件会按表中所示替换参数名称和值。

### R2023a：Lowpass RF、Highpass RF、Bandpass RF 和 Bandstop RF Filter 模块已被替换

从 R2023a 开始，理想化基带 Filter 模块
替换了 Lowpass RF Filter、Highpass RF Filter、
Bandpass RF Filter 和 Bandstop RF Filter 模块。

当您打开在 R2023a 之前创建的包含 Lowpass RF
Filter、Highpass RF Filter、Bandpass RF Filter 和
Bandstop RF Filter Filter 模块的模型时，软件会将旧模块替换为
新的理想化基带 Filter
模块。

## 描述

在 Simulink 中滤波 RF 复基带信号

使用 Idealized Baseband Filter 模块在 Simulink 中滤波 RF 复基带
信号。您可以使用 Butterworth、Chebyshev 或 inverse Chebyshev 设计
方法来设计滤波器。您还可以在时域或
频域中对滤波器建模，并绘制滤波器特性。

要设计具有阻抗失配的 RF 滤波器，请使用 Circuit Envelope Filter 模块。

**注意**

Idealized Baseband Filter 模块替换了 Lowpass RF Filter、
Highpass RF Filter、Bandpass RF Filter 和 Bandstop RF Filter 模块。
