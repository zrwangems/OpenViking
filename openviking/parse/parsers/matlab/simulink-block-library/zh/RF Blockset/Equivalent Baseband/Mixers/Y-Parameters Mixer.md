---
type: simulink-block
title: 'Y-Parameters Mixer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Mixers'
documentation_page: 'yparametersmixer'
documentation_source_path: 'ref/yparametersmixer.html'
language: zh-CN
chinese_source: worker-translation
---

# Y-Parameters Mixer

## 端口

未在 R2025b 中记录。

## 参数

### Main

### **Y-Parameters** — Y-parameters for nonlinear mixer `[0.0200,0;-0.0400, 0.0200]` (默认) | 2-by-2-by-*M* 数组

非线性混频器的 Y-parameters，指定为 2-by-2-by-*M* 数组，其中 *M* 是 Y-parameters 的数量。

### **Frequency (Hz)** — Frequency of Y-parameters `2.0e9` (默认) | *M* 元素向量

Y-parameters 的频率，指定为 *M* 元素向量，每个元素的单位为 hertz。所有频率必须为正。

### **Interpolation method** — Method to interpolate network parameters `Linear` (默认) | `Spline` | `Cubic`

用于插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### **Mixer Type** — Type of mixer `Downconverter` (默认) | `Upconverter`

混频器类型，指定为 `Downconverter` 或 `Upconverter`。

### **LO frequency (Hz)** — Local oscillator frequency `0.9e9` (默认) | *M* 元素向量

本振频率，指定为 *M* 元素向量，每个元素的单位为 hertz。

- 如果选择 **Mixer Type** 为 `Downconverter`，则模块集根据混频器输入频率 *fin* 和本振频率 *flo* 按 *fout* = *fin* – *flo* 计算混频器输出频率 *fout*。
- 如果将 **Mixer Type** 设为 `Upconverter`，则 *fout* = *fin* + *flo*。

**注意**

对于下变频混频器，本振频率必须满足条件 *fin* – *flo* ≥ 1/(2*ts*)，其中 *ts* 是在 Input Port 模块中指定的采样时间。否则会出现错误。

### 噪声数据

### **Phase noise frequency offset (Hz)** — Phase noise frequency offset `[0.1 1 10 100]*1e3` (默认) | 数值向量

相位噪声频率偏移，指定为以 hertz 为单位的数值向量。

**数据类型：** `double`

### **Phase noise level (dBc/Hz)** — Phase noise level `[-70 -120 -140 -150]` (默认) | 数值向量

相位噪声电平，指定为以 decibels relative to the carrier per hertz 为单位的数值向量。

**数据类型：** `double`

### **Noise type** — Type of noise data `Noise figure` (默认) | `Spot noise data` | `Noise factor` | `Noise temperature`

噪声数据类型，指定为以下之一：

- `Noise figure`
- `Spot noise data`
- `Noise factor`
- `Noise temperature`

如果数据源包含噪声数据，则禁用此参数。

### **Noise figure (dB)** — Available signal-to-noise ratio at the input to available signal-to-noise ratio at the output `0` (默认) | 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比之比，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise figure`。

### **Minimum noise figure** — Minimum ratio of available signal-to-noise ratio at input to available signal-to-noise ratio at output `0` (默认) | 标量比值 | 比值向量

输入端可用信噪比与输出端可用信噪比的最小比值，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Optimal reflection coefficient** — Optimal source impedance `1+0i` (默认) | 复标量 | 复向量

最佳源阻抗，指定为复标量或复向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Equivalent normalized noise resistance** — Normalized resistance values used to take noise measurement `1` (默认) | 正标量 | 正向量

用于进行噪声测量的归一化电阻值，指定为正标量或正向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Noise factor** — Ratio of available signal-to-noise power at input to available signal-to-noise power at output `1` (默认) | 标量比值 | 比值向量

输入端可用信噪功率与输出端可用信噪功率之比，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise factor`。

### **Noise temperature (K)** — Equivalent temperature that produces same amount of noise as mixer `0` (默认) | 非负标量 | 非负向量

产生与混频器相同噪声量的等效温度，指定为非负标量或非负向量，单位为 kelvins。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise temperature`。

### **Frequency (Hz)** — Domain of frequencies to express noise data `2.0e9` (默认) | 非负标量 | 非负向量

用于表示噪声数据的频率范围，指定为以 hertz 为单位的非负标量，或每个元素均以 hertz 为单位的非负向量。如果为噪声数据提供标量值，则该模块忽略 **Frequency (Hz)** 参数，并对所有频率使用相同的噪声数据。如果为噪声数据提供值向量，则其大小必须与频率向量相同。该模块使用 **Main** 选项卡中指定的 **Interpolation method** 对噪声数据进行插值。

### 非线性数据

### **IP3 type** — Type of third order intercept `OIP3` (默认) | `IIP3`

三阶截点的类型，指定为 `OIP3`（输出截点）或 `IIP3`（输入截点）。如果数据源包含功率数据或 IP3 数据，则禁用此参数。

### **IP3 (dBm)** — IP3 value `inf` (默认) | 标量 | 向量

IP3 值，对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素均以 dBm 为单位的向量。如果数据源包含功率数据或 IP3 数据，则禁用此参数。

### **1dB gain compression power (dBm)** — Output power value at which gain has decreased by 1 dB `inf` (默认) | 标量 | 向量

增益下降 1 dB 时的输出功率值（P1dB,out），对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素均以 dBm 为单位的向量。如果数据源包含功率数据或 IP3 数据，则禁用此参数。

### **Output saturation power (dBm)** — Output power value that mixer produces when fully saturated `inf` (默认) | 标量 | 向量

混频器完全饱和时产生的输出功率值（Psat,out），对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素均以 dBm 为单位的向量。如果数据源包含输出饱和功率数据，则禁用此参数。

### **Gain compression at saturation (dB)** — Decrease in gain value `3` (默认) | 标量 | 向量

功率完全饱和时的增益下降值（GCsat），对于频率无关的非线性数据，指定为以 dB 为单位的标量；对于频率相关的非线性数据，指定为每个元素均以 dB 为单位的向量。

### **Frequency (Hz)** — Frequency points corresponding to third-order intercept or power data `2.0e9` (默认) | 正标量 | 正向量

与三阶截点或功率数据对应的频率点，指定为以 hertz 为单位的正标量或正向量。如果数据源包含功率数据或 IP3 数据，则禁用此参数。

#### 依赖关系

- 如果将频率指定为标量，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数必须全部为标量。
- 如果将频率指定为向量，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数中的一个或多个也必须为向量。

### 可视化

### **Source of frequency data** — Frequency data source `Same as the Y-Parameters` (默认) | `User-specified`

频率数据源，指定为 `Same as the Y-Parameters` 或 `User-specified`。

### **Frequency data (Hz)** — Frequency data range `[1e9:1e8:2.9e9]` (默认) | 向量

频率数据范围，指定为向量，每个元素的单位为 hertz。

#### 依赖关系

要启用此参数，请将 **Source of frequency data** 设置为 `User specified`。

### **Reference impedance (ohms)** — Reference impedance `50` (默认) | 非负标量

参考阻抗，指定为以 ohms 为单位的非负标量。

### **Plot type** — Type of data plot `X-Y plane` (默认) | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据进行可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性图、半对数图或双对数图，请相应设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — Type of parameters to plot `S11` (默认) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | `NFactor` | `NTemp` | `PhaseNoise` | ...

基于所设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor`、`NTemp` 和 `PhaseNoise`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y parameter2** — Type of parameters to plot `S11` | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | `NFactor` | `NTemp` | ...

基于所设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor`、`NTemp` 和 `PhaseNoise`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y format1** — Plot format `Magnitude (decibels)` (默认) | `Magnitude (linear)` | `Angle(degrees)` | `Angle(radians)` | `Real` | `Imaginary`

绘图格式，指定为以下之一。

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`、`S12`、`S21` 和 `S22`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |
| `PhaseNoise` | `dBc/Hz` |

#### 依赖关系

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — Plot format `Magnitude (decibels)` (默认) | `Magnitude (linear)` | `Angle(degrees)` | `Angle(radians)` | `Real` | `Imaginary`

绘图格式，指定为以下之一。

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`、`S12`、`S21` 和 `S22`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |
| `PhaseNoise` | `dBc/Hz` |

#### 依赖关系

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — Frequency plot `Freq` (默认)

频率图，指定为 `Freq`。

### **X format** — Frequency plot format `Hz` (默认) | `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y scale** — Y-axis scale `Linear` (默认) | `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **X scale** — X-axis scale `Linear` (默认) | `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Plot** — Plot specified data button

绘制指定数据的按钮。

## 所属库

RF Blockset / Equivalent Baseband / Mixers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 Y-parameters 对混频器和本振建模

Y-Parameters Mixer 模块根据其频率相关的 Y-parameters、Y-parameters 的频率、噪声数据（包括相位噪声数据）和非线性数据，对模块对话框中所描述的非线性混频器建模。
