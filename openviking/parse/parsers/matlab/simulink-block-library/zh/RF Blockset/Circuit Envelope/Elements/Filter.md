---
type: simulink-block
title: 'Filter'
family: 'simrf'
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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Design method
  summary: 仿真类型 Butterworth（默认）| Chebyshev | Inverse Chebyshev | Ideal
  group: 主要
- name: Filter type
  summary: 滤波器类型 Lowpass（默认）| Highpass | Bandpass | Bandstop
  group: 主要
- name: Implementation
  summary: 实现方式 LC Tee | LC Pi | Transfer function | Constant per carrier | Frequency Domain
  group: 主要
- name: Passband edge frequency
  summary: 通带边缘频率 1 GHz（默认）| 标量
  group: 主要
- name: Implement using filter order
  summary: 使用滤波器阶数实现 off（默认）| on
  group: 主要
- name: 滤波器阶数
  summary: 滤波器阶数 3（默认）| 标量
  group: 主要
- name: 通带频率
  summary: 低通和高通滤波器的通带频率 标量
  group: 主要
- name: 通带频率
  summary: 带通滤波器的通带频率 [2 3] GHz（默认）| 二元组向量
  group: 主要
- name: 通带衰减 (dB)
  summary: 通带衰减 10*log10(2)（默认）| 标量
  group: 主要
- name: 阻带频率
  summary: 带阻滤波器的阻带频率 [2.1 2.9] GHz（默认）| 二元组向量
  group: 主要
- name: 阻带衰减 (dB)
  summary: 阻带衰减 40（默认）| 标量
  group: 主要
- name: 源阻抗 (Ohm)
  summary: 输入源电阻 50（默认）| 标量
  group: 主要
- name: 负载阻抗 (Ohm)
  summary: 输出负载电阻 50（默认）| 标量
  group: 主要
- name: 接地并隐藏负端子
  summary: 将 RF 电路端子接地 on（默认）| off
  group: 主要
- name: 导出
  summary: 将滤波器设计保存到文件 按钮
  group: 主要
- name: Parameter 1
  summary: y 轴上的绘图类型 Voltage transfer（默认）| Phase delay | Group delay
  group: 可视化
- name: Parameter 2
  summary: 绘图类型 None（默认）| Voltage transfer | Phase delay | Group delay
  group: 可视化
- name: Format 1
  summary: y 轴缩放 Magnitude (decibels)（默认）| Magnitude (linear) | Angle (degrees) | Real | Imaginary
  group: 可视化
- name: Format 2
  summary: y 轴缩放 Magnitude (decibels)（默认）| Magnitude (linear) | Angle (degrees) | Real | Imaginary
  group: 可视化
- name: Frequency points
  summary: 要在 x 轴上绘制的频率点 logspace(0,10,101) Hz（默认）| 向量
  group: 可视化
- name: X-axis scale
  summary: x 轴刻度 Linear（默认）| Logarithmic
  group: 可视化
- name: Y-axis scale
  summary: y 轴刻度 Linear（默认）| Logarithmic
  group: 可视化
```

### 主要

### **Design method** — 仿真类型 `Butterworth`（默认）| `Chebyshev` | `Inverse Chebyshev` | `Ideal`

仿真类型，指定为以下之一：

- `Ideal` — 仿真 **Filter type** 中指定类型且 **Implementation** 中指定模型的理想滤波器。
- `Butterworth` — 仿真 **Filter type** 中指定类型且 **Implementation** 中指定模型的巴特沃斯滤波器。
- `Chebyshev` — 仿真 **Filter type** 中指定类型且 **Implementation** 中指定模型的切比雪夫滤波器。
- `Inverse Chebyshev` — 仿真 **Filter type** 中指定类型且 **Implementation** 中指定 `Transfer function` 模型的逆切比雪夫滤波器。

### **Filter type** — 滤波器类型 `Lowpass`（默认）| `Highpass` | `Bandpass` | `Bandstop`

滤波器类型，指定为以下之一：

- `Lowpass` — 仿真 **Design method** 中指定设计的低通滤波器类型。
- `Highpass` — 仿真 **Design method** 中指定设计的高通滤波器类型。
- `Bandpass` — 仿真 **Design method** 中指定设计的带通滤波器类型。
- `Bandstop` — 仿真 **Design method** 中指定设计的带阻滤波器类型。

### **Implementation** — 实现方式 `LC Tee` | `LC Pi` | `Transfer function` | `Constant per carrier` | `Frequency Domain`

实现方式，指定为以下之一：

- `LC Tee` — 当 **Design method** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Tee 结构对模拟滤波器建模。
- `LC Pi` — 当 **Design method** 为 Butterworth 或 Chebyshev 时，使用 LC 集总 Pi 结构对模拟滤波器建模。
- `Transfer Function` — 当 **Design method** 为 Butterworth 或 Chebyshev 时，使用二端口 S 参数对模拟滤波器建模。
- `Constant per carrier` — 对滤波器建模，在每个载波周围的整个包络频带内将全传输或全反射设为常数。**Design method** 指定为 ideal。
- `Frequency Domain` — 使用与冲激响应的卷积对滤波器建模。**Design method** 指定为 ideal。冲激响应针对每个载波频率独立计算，以捕获理想滤波响应。当理想滤波器的全传输与全反射之间的过渡发生在载波周围的包络频带内时，频域实现可正确捕获此过渡，精度达到 **Impulse response duration** 中指定的频率分辨率。

默认情况下，对于理想滤波器，**Implementation** 为 `Constant per carrier`；对于 Butterworth 或 Chebyshev，为 `LC Tee`。

**注意**

由于因果性，反射信号和传输信号都包含冲激响应持续时间一半的延迟。当源电阻和负载电阻与滤波器参数中指定的值不同时，此延迟将损害滤波器性能。

### **Passband edge frequency** — 通带边缘频率 `1 GHz`（默认）| 标量

通带边缘频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的标量。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Ideal`。

### **Implement using filter order** — 使用滤波器阶数实现 `off`（默认）| `on`

选择此参数以手动实现滤波器阶数。

#### 依赖关系

要启用此参数，请将 **Design method** 设置为 `Butterworth` 或 `Chebyshev`。

### **滤波器阶数** — 滤波器阶数 `3`（默认）| 标量

滤波器阶数，指定为范围在 [2, 60] 之间的标量。
该阶数是 `lowpass` 或 `highpass` 中集总储能元件的数量。在
`bandpass` 或 `bandstop` 中，集总储能（L 和 C）元件的数量是该值的两倍。

**注意**

对于偶数阶 Chebyshev 滤波器，Tee 网络实现中的电阻比 RloadRsource>Rratio，而 Pi 网络实现中的 RloadRsource<1Rratio。

Rratio = 1+ε2+ε1+ε2−ε

其中：

- ε = 10(0.1Rp)−1

- *R*p 是以 dB 为单位的通带纹波。

#### 依赖关系

要启用此参数，请选择 **Implement using filter
order**。

### **通带频率** — 低通和高通滤波器的通带频率 标量

低通和高通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的标量。根据您选择的 **Filter
type**，此参数的默认值会有所不同。默认值列于此表中。

| 滤波器类型 | 通带频率的默认值 |
| --- | --- |
| `Lowpass` | `1 GHz` |
| `Highpass` | `2 GHz` |

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`，并将 **Filter
type** 设置为 `Lowpass` 或
`Highpass`。

### **通带频率** — 带通滤波器的通带频率 `[2 3] GHz`（默认）| 二元组向量

带通滤波器的通带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的二元组向量。此选项不适用于带阻滤波器。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`，并将 **Filter
type** 设置为 `Bandpass`。

### **通带衰减 (dB)** — 通带衰减 `10*log10(2)`（默认）| 标量

通带衰减，指定为以 dB 为单位的标量。对于带通滤波器，该值同等应用于通带的两侧边缘。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`。

### **阻带频率** — 带阻滤波器的阻带频率 `[2.1 2.9] GHz`（默认）| 二元组向量

带阻滤波器的阻带频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的二元组向量。此选项不适用于带通滤波器。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`，并将 **Filter
type** 设置为 `Bandstop`。

### **阻带衰减 (dB)** — 阻带衰减 `40`（默认）| 标量

阻带衰减，指定为以 dB 为单位的标量。对于带阻滤波器，该值同等应用于阻带的两侧边缘。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`，并将 **Filter
type** 设置为 `Bandstop`。

### **源阻抗 (Ohm)** — 输入源电阻 `50`（默认）| 标量

输入源电阻，指定为以欧姆为单位的标量。

**注意**

当 **Implementation** 设置为
`Transfer function` 时，源阻抗和负载阻抗必须相等。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`。

### **负载阻抗 (Ohm)** — 输出负载电阻 `50`（默认）| 标量

输出负载电阻，指定为以欧姆为单位的标量。

**注意**

当 **Implementation** 设置为
`Transfer function` 时，源阻抗和负载阻抗必须相等。

#### 依赖关系

要启用此参数，请将 **Design method**
设置为 `Butterworth` 或
`Chebyshev`。

### **接地并隐藏负端子** — 将 RF 电路端子接地 `on`（默认）| `off`

选择以在内部接地并隐藏负端子。清除以暴露负端子。当端子暴露时，您可以将它们连接到模型的其它部分。

### **导出** — 将滤波器设计保存到文件 按钮

使用此按钮将滤波器设计保存到 MAT 或 TXT 文件。有关详细信息，请参阅 Export Your Filter Design。

### 可视化

### **Parameter 1** — y 轴上的绘图类型 `Voltage transfer`（默认）| `Phase delay` | `Group delay`

绘图类型，指定为 `Voltage
transfer`、`Phase delay` 或
`Group delay`。

### **Parameter 2** — 绘图类型 `None`（默认）| `Voltage transfer` | `Phase delay` | `Group delay`

绘图类型，指定为 `None`、
`Voltage transfer`、`Phase
delay` 或 `Group
delay`。

### **Format 1** — y 轴缩放 `Magnitude (decibels)`（默认）| `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

y 轴缩放，指定为，

- 对于 `Voltage
  transfer` 参数，为 `Magnitude(decibels)`、
  `Magnitude(linear)` 或
  `Angle(degrees)`、`Real`
  或 `Imaginary`。
- 对于 `Phase
  delay` 或 `Group delay`
  参数，为 `Magnitude(decibels)` 或
  `Magnitude(linear)`。

### **Format 2** — y 轴缩放 `Magnitude (decibels)`（默认）| `Magnitude (linear)` | `Angle (degrees)` | `Real` | `Imaginary`

y 轴缩放，指定为，

- 对于 `Voltage
  transfer` 参数，为 `Magnitude(decibels)`、
  `Magnitude(linear)` 或
  `Angle(degrees)`、`Real`
  或 `Imaginary`。
- 对于 `Phase
  delay` 或 `Group delay`
  参数，为 `Magnitude(decibels)` 或
  `Magnitude(linear)`。

### **Frequency points** — 要在 x 轴上绘制的频率点 `logspace(0,10,101) Hz`（默认）| 向量

要在 x 轴上绘制的频率点，指定为一个向量，其中每个元素的单位为 Hz、kHz、MHz 或 GHz。

### **X-axis scale** — x 轴刻度 `Linear`（默认）| `Logarithmic`

x 轴刻度，指定为 `Linear` 或
`Logarithmic`。

### **Y-axis scale** — y 轴刻度 `Linear`（默认）| `Logarithmic`

y 轴刻度，指定为 `Linear` 或
`Logarithmic`。
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

Model RF Filter

Filter 模块对四种设计的 RF 滤波器进行建模：

- Butterworth — Butterworth 滤波器具有在通带内最大平坦且整体单调的幅值响应。这种平滑性以滚降陡度降低为代价。
- Chebyshev — Chebyshev I 型滤波器在通带内具有等幅纹波，在阻带内单调。
- Inverse Chebyshev — Chebyshev II 型滤波器在阻带内具有等幅纹波，在通带内单调。
- Ideal — 理想滤波器完全允许通带内的频率，并完全抑制阻带内的频率。

要在 Simulink 中过滤 RF 复基带信号，请使用 Idealized Baseband Filter 模块。
