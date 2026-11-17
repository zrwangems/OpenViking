---
type: simulink-block
title: 'S-Parameters Mixer'
family: 'equivalent-baseband'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Mixers'
documentation_page: 'sparametersmixer'
documentation_source_path: 'ref/sparametersmixer.html'
language: zh-CN
chinese_source: worker-translation
---

# S-Parameters Mixer

## 端口

在 R2025b 中未记录。

## 参数

### 主要

### **S-Parameters** — 用于非线性混频器的 S 参数 `[0,0;1,0]`（默认） | 2×2×*M* 数组

用于非线性混频器的 S 参数，指定为 2×2×*M* 数组，其中 *M* 是 S 参数的数量。

### **Frequency (Hz)** — S 参数的频率 `2.0e9`（默认） | *M* 元素向量

S 参数的频率，指定为 *M* 元素向量，每个元素的单位为 hertz。所有频率必须为正。

### **Reference Impedance (ohms)** — S 参数的参考阻抗 `50`（默认） | 数值标量 | 长度为 *M* 的数值向量

S 参数的参考阻抗，指定为数值标量或长度为 *M* 的数值向量。如果提供标量值，则该值应用于所有频率。

**复数支持：** Yes

### **Interpolation method** — 用于对网络参数进行插值的方法 `Linear`（默认） | `Spline` | `Cubic`

用于对网络参数进行插值的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### **Mixer Type** — 混频器类型 `Downconverter`（默认） | `Upconverter`

混频器类型，指定为 `Downconverter` 或 `Upconverter`。

### **LO frequency (Hz)** — 本振频率 `0.9e9`（默认） | *M* 元素向量

本振频率，指定为 *M* 元素向量，每个元素的单位为 hertz。

- 如果将 **Mixer Type** 选择为 `Downconverter`，则模块集根据混频器输入频率 *fin* 和本振频率 *flo* 计算混频器输出频率 *fout*，即 *fout* = *fin* – *flo*。
- 如果将 **Mixer Type** 选择为 `Upconverter`，则 *fout* = *fin* + *flo*。

**注意**

对于下变频混频器，本振频率必须满足条件 *fin* – *flo* ≥ 1/(2*ts*)，其中 *ts* 是在 Input Port 模块中指定的采样时间。否则，会出现错误。

### 噪声数据

### **Phase noise frequency offset (Hz)** — 相位噪声频率偏移 `[0.1 1 10 100]*1e3`（默认） | 数值向量

相位噪声频率偏移，指定为以 hertz 为单位的数值向量。

**数据类型：** `double`

### **Phase noise level (dBc/Hz)** — 相位噪声电平 `[-70 -120 -140 -150]`（默认） | 数值向量

相位噪声电平，指定为以相对于载波的每 hertz 分贝为单位的数值向量。

**数据类型：** `double`

### **Noise type** — 噪声数据类型 `Noise figure`（默认） | `Spot noise data` | `Noise factor` | `Noise temperature`

噪声数据类型，指定为以下之一：

- `Noise figure`
- `Spot noise data`
- `Noise factor`
- `Noise temperature`

如果数据源包含噪声数据，则此参数被禁用。

### **Noise figure (dB)** — 输入端的可用信噪比与输出端的可用信噪比之比 `0`（默认） | 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比之比，指定为标量比值或比值向量。

#### 依赖项

要启用此参数，请在 **Noise type** 中选择 `Noise figure`。

### **Minimum noise figure** — 输入端的可用信噪比与输出端的可用信噪比的最小比值 `0`（默认） | 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比的最小比值，指定为标量比值或比值向量。

#### 依赖项

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Optimal reflection coefficient** — 最佳源阻抗 `1+0i`（默认） | 复标量 | 复向量

最佳源阻抗，指定为复标量或复向量。

#### 依赖项

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Equivalent normalized noise resistance** — 用于进行噪声测量的归一化电阻值 `1`（默认） | 正标量 | 正向量

用于进行噪声测量的归一化电阻值，指定为正标量或正向量。

#### 依赖项

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Noise factor** — 输入端的可用信噪功率与输出端的可用信噪功率之比 `1`（默认） | 标量比值 | 比值向量

输入端的可用信噪功率与输出端的可用信噪功率之比，指定为标量比值或比值向量。

#### 依赖项

要启用此参数，请在 **Noise type** 中选择 `Noise factor`。

### **Noise temperature (K)** — 产生与混频器相同噪声量的等效温度 `0`（默认） | 非负标量 | 非负向量

产生与混频器相同噪声量的等效温度，指定为以 kelvins 为单位的非负标量或非负向量。

#### 依赖项

要启用此参数，请在 **Noise type** 中选择 `Noise temperature`。

### **Frequency (Hz)** — 用于表示噪声数据的频率域 `2.0e9`（默认） | 非负标量 | 非负向量

用于表示噪声数据的频率域，指定为以 hertz 为单位的非负标量，或每个元素的单位为 hertz 的非负向量。如果为噪声数据提供标量值，则该模块忽略 **Frequency (Hz)** 参数，并对所有频率使用相同的噪声数据。如果为噪声数据提供向量值，则该向量的大小必须与频率向量相同。该模块使用 **主要** 选项卡中指定的 **Interpolation method** 对噪声数据进行插值。

### 非线性数据

### **IP3 type** — 三阶截点类型 `OIP3`（默认） | `IIP3`

三阶截点类型，指定为 `OIP3`（输出截点）或 `IIP3`（输入截点）。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **IP3 (dBm)** — IP3 值 `inf`（默认） | 标量 | 向量

IP3 值，对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素的单位为 dBm 的向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **1dB gain compression power (dBm)** — 增益下降 1 dB 时的输出功率值 `inf`（默认） | 标量 | 向量

增益下降 1 dB 时的输出功率值 (P1dB,out)，对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素的单位为 dBm 的向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **Output saturation power (dBm)** — 混频器完全饱和时产生的输出功率值 `inf`（默认） | 标量 | 向量

混频器完全饱和时产生的输出功率值 (Psat,out)，对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素的单位为 dBm 的向量。如果数据源包含输出饱和功率数据，则此参数被禁用。

### **Gain compression at saturation (dB)** — 增益值的下降量 `3`（默认） | 标量 | 向量

功率完全饱和时增益值的下降量 (GCsat)，对于频率无关的非线性数据，指定为以 dB 为单位的标量；对于频率相关的非线性数据，指定为每个元素的单位为 dB 的向量。

### **Frequency (Hz)** — 对应于三阶截点或功率数据的频率点 `2.0e9`（默认） | 正标量 | 正向量

对应于三阶截点或功率数据的频率点，指定为以 hertz 为单位的正标量或正向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

#### 依赖项

- 如果将频率指定为标量，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数必须全部为标量。
- 如果将频率指定为向量，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数中的一个或多个也必须为向量。

### 可视化

### **Source of frequency data** — 频率数据源 `Same as the S-Parameters`（默认） | `User-specified`

频率数据源，指定为 `Same as the S-Parameters` 或 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1e9:1e8:2.9e9]`（默认） | 向量

频率数据范围，指定为每个元素的单位为 hertz 的向量。

#### 依赖项

要启用此参数，请将 **Source of frequency data** 设置为 `User specified`。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认） | 非负标量

参考阻抗，指定为以 ohms 为单位的非负标量。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认） | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

用于使用给定数据可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性图、半对数图或双对数图，请相应设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认） | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | `NFactor` | `NTemp` | `PhaseNoise` | ...

要根据设置的 **Plot type** 绘制的参数类型，指定为以下之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor`、`NTemp` 和 `PhaseNoise`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y parameter2** — 要绘制的参数类型 `S11` | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | `NFactor` | `NTemp` | ...

要根据设置的 **Plot type** 绘制的参数类型，指定为以下之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor`、`NTemp` 和 `PhaseNoise`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y format1** — 绘图格式 `Magnitude (decibels)`（默认） | `Magnitude (linear)` | `Angle(degrees)` | `Angle(radians)` | `Real` | `Imaginary`

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

#### 依赖项

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)`（默认） | `Magnitude (linear)` | `Angle(degrees)` | `Angle(radians)` | `Real` | `Imaginary`

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

#### 依赖项

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — 频率图 `Freq`（默认）

频率图，指定为 `Freq`。

### **X format** — 频率图格式 `Hz`（默认） | `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y scale** — Y 轴刻度 `Linear`（默认） | `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖项

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **X scale** — X 轴刻度 `Linear`（默认） | `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖项

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Plot** — 绘制指定数据按钮

使用绘图按钮绘制指定数据。

## 所属库

RF Blockset / Equivalent Baseband / Mixers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 S 参数对混频器和本振进行建模

S-Parameters Mixer 模块根据其频率相关 S 参数、S 参数的频率和参考阻抗、噪声数据（包括相位噪声数据）以及非线性数据，对模块对话框中描述的非线性混频器进行建模。
