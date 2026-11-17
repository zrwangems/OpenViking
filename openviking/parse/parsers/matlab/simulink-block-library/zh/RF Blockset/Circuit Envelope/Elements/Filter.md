---
type: simulink-block
title: 'Filter'
family: 'circuit-envelope'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'filter'
documentation_source_path: 'ref/filter.html'
language: zh-CN
chinese_source: worker-translation
---

# Filter

## 端口

在 R2025b 中未记录。

## 参数

### 主要

### **设计方法** — 仿真类型 `Butterworth`（默认）| `Chebyshev` | `Inverse Chebyshev` | `Ideal`

仿真类型，指定为以下之一：

- `Ideal` — 模拟由 **滤波器类型** 指定的类型和 **实现** 指定的模型的理想滤波器。
- `Butterworth` — 模拟由 **滤波器类型** 指定的类型和 **实现** 指定的模型的 Butterworth 滤波器。
- `Chebyshev` — 模拟由 **滤波器类型** 指定的类型和 **实现** 指定的模型的 Chebyshev 滤波器。
- `Inverse Chebyshev` — 模拟由 **滤波器类型** 指定的类型和 **实现** 中指定的 `Transfer function` 模型的 inverse Chebyshev 滤波器。

### **滤波器类型** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器类型，指定为以下之一：

- `Lowpass` — 模拟由 **设计方法** 指定的设计的低通滤波器类型。
- `Highpass` — 模拟由 **设计方法** 指定的设计的高通滤波器类型。
- `Bandpass` — 模拟由 **设计方法** 指定的设计的带通滤波器类型。
- `Bandstop` — 模拟由 **设计方法** 指定的设计的带阻滤波器类型。

### **实现** — 实现 `LC Tee` | `LC Pi` | `Transfer function` | `Constant per carrier` | `Frequency Domain`

实现，指定为以下之一：

- `LC Tee` — 当 **设计方法** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Tee 结构对模拟滤波器建模。
- `LC Pi` — 当 **设计方法** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Pi 结构对模拟滤波器建模。
- `Transfer Function` — 当 **设计方法** 为 Butterworth 或 Chebyshev 时，使用二端口 S 参数对模拟滤波器建模。
- `Constant per carrier` — 在每个载波周围的整个包络频带内，将全传输或全反射设置为常数来对滤波器建模。**设计方法** 指定为 ideal。
- `Frequency Domain` — 使用与冲激响应的卷积对滤波器建模。**设计方法** 指定为 ideal。冲激响应针对每个载波频率独立计算，以捕获理想滤波响应。当理想滤波器的全传输和全反射之间的过渡发生在载波周围的包络频带内时，频域实现会正确捕获此过渡，直到 **冲激响应持续时间** 中指定的频率分辨率。

默认情况下，对于理想滤波器，**实现** 为 `Constant per carrier`；对于 Butterworth 或 Chebyshev，**实现** 为 `LC Tee`。

**注意**

由于因果性，反射信号和传输信号都会包含冲激响应持续时间一半的延迟。当源电阻和负载电阻不同于滤波器参数中指定的值时，此延迟会损害滤波器性能。

### **通带边缘频率** — 通带边缘频率 `1 GHz`（默认）| scalar

通带边缘频率，指定为 scalar，单位为 Hz、kHz、MHz 或 GHz。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Ideal`。

### **使用滤波器阶数实现** — 使用滤波器阶数实现 `off`（默认）| `on`

选择此参数以手动实现滤波器阶数。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **滤波器阶数** — 滤波器阶数 `3`（默认）| scalar

滤波器阶数，指定为范围 [2, 60] 内的 scalar。此阶数是 `lowpass` 或 `highpass` 中集总储能元件的数量。在 `bandpass` 或 `bandstop` 中，集总储能（L 和 C）元件的数量是该值的两倍。

**注意**

对于偶数阶 Chebyshev 滤波器，电阻比 RloadRsource>Rratio 用于 Tee 网络实现，而 RloadRsource<1Rratio 用于 Pi 网络实现。

Rratio = 1+ε2+ε1+ε2−ε

其中：

- ε = 10(0.1Rp)−1

- *R*p 是以 dB 为单位的通带波纹。

#### 依赖关系

要启用此参数，请选择 **使用滤波器阶数实现**。

### **通带频率** — 低通和高通滤波器的通带频率 scalar

低通和高通滤波器的通带频率，指定为 scalar，单位为 Hz、kHz、MHz 或 GHz。根据所选的 **滤波器类型**，此参数的默认值会有所不同。默认值列于下表中。

| 滤波器类型 | 通带频率的默认值 |
| --- | --- |
| `Lowpass` | `1 GHz` |
| `Highpass` | `2 GHz` |

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Lowpass` 或 `Highpass`。

### **通带频率** — 带通滤波器的通带频率 `[2 3] GHz`（默认）| 2-tuple vector

带通滤波器的通带频率，指定为 2-tuple vector，单位为 Hz、kHz、MHz 或 GHz。此选项不适用于带阻滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Bandpass`。

### **通带衰减 (dB)** — 通带衰减 `10*log10(2)`（默认）| scalar

通带衰减，指定为 scalar，单位为 dB。对于带通滤波器，此值同等应用于通带的两条边缘。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **阻带频率** — 带阻滤波器的阻带频率 `[2.1 2.9] GHz`（默认）| 2-tuple vector

带阻滤波器的阻带频率，指定为 2-tuple vector，单位为 Hz、kHz、MHz 或 GHz。此选项不适用于带通滤波器。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Bandstop`。

### **阻带衰减 (dB)** — 阻带衰减 `40`（默认）| scalar

阻带衰减，指定为 scalar，单位为 dB。对于带阻滤波器，此值同等应用于阻带的两条边缘。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`，并将 **滤波器类型** 设置为 `Bandstop`。

### **源阻抗 (Ohm)** — 输入源电阻 `50`（默认）| scalar

输入源电阻，指定为 scalar，单位为 ohms。

**注意**

当 **实现** 设置为 `Transfer function` 时，源阻抗和负载阻抗必须相等。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **负载阻抗 (Ohm)** — 输出负载电阻 `50`（默认）| scalar

输出负载电阻，指定为 scalar，单位为 ohms。

**注意**

当 **实现** 设置为 `Transfer function` 时，源阻抗和负载阻抗必须相等。

#### 依赖关系

要启用此参数，请将 **设计方法** 设置为 `Butterworth` 或 `Chebyshev`。

### **接地并隐藏负端子** — 将 RF 电路端子接地 `on`（默认）| `off`

选择此项可将负端子在内部接地并隐藏。清除此项可暴露负端子。当端子暴露时，您可以将它们连接到模型的其他部分。

### **导出** — 将滤波器设计保存到文件 按钮

使用此按钮可将滤波器设计保存到 MAT 或 TXT 文件。有关详细信息，请参阅导出滤波器设计。

### 可视化

### **参数 1** — y 轴上的绘图类型 `Voltage transfer`（默认）| `Phase delay` | `Group delay`

绘图类型，指定为 `Voltage transfer`、`Phase delay` 或 `Group delay`。

### **参数 2** — 绘图类型 `None`（默认）| `Voltage transfer` | `Phase delay` | `Group delay`

绘图类型，指定为 `None`、`Voltage transfer`、`Phase delay` 或 `Group delay`。

### **格式 1** — y 轴的缩放 `Magnitude (decibels)`（默认）| `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

y 轴的缩放，指定为，

- 对于 `Voltage transfer` 参数，为 `Magnitude(decibels)`、`Magnitude(linear)` 或 `Angle(degrees)`、`Real` 或 `Imaginary`。
- 对于 `Phase delay` 或 `Group delay` 参数，为 `Magnitude(decibels)` 或 `Magnitude(linear)`。

### **格式 2** — y 轴的缩放 `Magnitude (decibels)`（默认）| `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

y 轴的缩放，指定为，

- 对于 `Voltage transfer` 参数，为 `Magnitude(decibels)`、`Magnitude(linear)` 或 `Angle(degrees)`、`Real` 或 `Imaginary`。
- 对于 `Phase delay` 或 `Group delay` 参数，为 `Magnitude(decibels)` 或 `Magnitude(linear)`。

### **频率点** — 要在 x 轴上绘制的频率点 `logspace(0,10,101) Hz`（默认）| vector

要在 x 轴上绘制的频率点，指定为 vector，其中每个元素的单位为 Hz、kHz、MHz 或 GHz。

### **X 轴刻度** — X 轴刻度 `Linear`（默认）| `Logarithmic`

X 轴刻度，指定为 `Linear` 或 `Logarithmic`。

### **Y 轴刻度** — Y 轴刻度 `Linear`（默认）| `Logarithmic`

Y 轴刻度，指定为 `Linear` 或 `Logarithmic`。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

对 RF 滤波器建模

Filter 模块对四种设计的 RF 滤波器进行建模：

- Butterworth — Butterworth 滤波器具有在通带内最大平坦且整体单调的幅值响应。这种平滑性以滚降陡度降低为代价。
- Chebyshev — Chebyshev Type I 滤波器在通带中具有等幅波纹，在阻带中单调。
- Inverse Chebyshev — Chebyshev Type II 滤波器在阻带中具有等幅波纹，在通带中单调。
- Ideal — 理想滤波器完美地允许通带中的频率，并完全抑制阻带中的频率。

要在 Simulink 中对 RF 复基带信号进行滤波，请使用 Idealized Baseband Filter 模块。
