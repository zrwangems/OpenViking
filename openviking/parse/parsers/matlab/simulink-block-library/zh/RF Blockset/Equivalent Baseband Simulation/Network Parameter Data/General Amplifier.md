---
type: simulink-block
title: 'General Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband Simulation / Cascaded Subsystems / Amplifiers'
documentation_page: 'generalamplifier'
documentation_source_path: 'ref/generalamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# General Amplifier

## 端口

R2025b 中未记录。

## 参数

### 主项

### **Data source** — 描述放大器行为的数据源 `Data file`（默认）| `RFDATA` object

描述放大器行为的数据源，指定为 `Data file` 或 `RFDATA` object。

### **Data file** — 包含放大器数据的文件名 `default.s2d`（默认）| string | character vector

包含放大器数据的文件名，指定为 string 或 character vector。文件名必须包含扩展名。如果文件不在您的 MATLAB® 路径中，请指定文件的完整路径，或点击 **Browse** 按钮查找该文件。

#### 依赖关系

要启用此参数，请在 **Data source** 中选择 `Data file`。

### **RFDATA object** — 包含放大器数据的 RF 数据对象 `read(rfdata.data, 'default.amp')`（默认）| `rfdata.data` object

包含放大器数据的 RF 数据对象，指定为 RF Toolbox 的 `rfdata.data` 对象、创建 `rfdata.data` 对象的 RF toolbox 命令，或生成此类对象的 MATLAB 表达式。

### **Interpolation method** — 插值网络参数的方法 `Linear`（默认）| `Spline` | `Cubic`

插值网络参数的方法，指定为以下之一：

| 方法 | 说明 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### 噪声数据

### **Noise type** — 噪声数据的类型 `Noise figure`（默认）| `Spot noise data` | `Noise factor` | `Noise temperature`

噪声数据的类型，指定为以下之一：

- `Noise figure`
- `Spot noise data`
- `Noise factor`
- `Noise temperature`

如果数据源包含噪声数据，则此参数被禁用。

### **Noise figure (dB)** — 输入端可用信噪比与输出端可用信噪比之比 `0`（默认）| scalar ratio | vector of ratios

输入端可用信噪比与输出端可用信噪比之比，指定为 scalar ratio 或 vector of ratios。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise figure`。

### **Minimum noise figure** — 输入端可用信噪比与输出端可用信噪比的最小比值 `0`（默认）| scalar ratio | vector of ratios

输入端可用信噪比与输出端可用信噪比的最小比值，指定为 scalar ratio 或 vector of ratios。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Optimal reflection coefficient** — 最佳源阻抗 `1+0i`（默认）| complex scalar | complex vector

最佳源阻抗，指定为 complex scalar 或 complex vector。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Equivalent normalized noise resistance** — 用于进行噪声测量的归一化电阻值 `1`（默认）| positive scalar | positive vector

用于进行噪声测量的归一化电阻值，指定为 positive scalar 或 positive vector。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Noise factor** — 输入端可用信噪功率与输出端可用信噪功率之比 `1`（默认）| scalar ratio | vector of ratios

输入端可用信噪功率与输出端可用信噪功率之比，指定为 scalar ratio 或 vector of ratios。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise factor`。

### **Noise temperature (K)** — 与放大器产生相同噪声量的等效温度 `0`（默认）| nonnegative scalar | nonnegative vector

与放大器产生相同噪声量的等效温度，指定为以 kelvins 为单位的 nonnegative scalar，或每个元素单位均为 kelvins 的 nonnegative vector。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise temperature`。

### **Frequency (Hz)** — 用于表示噪声数据的频率范围 `2.0e9`（默认）| nonnegative scalar | nonnegative vector

用于表示噪声数据的频率范围，指定为以 hertz 为单位的 nonnegative scalar，或每个元素单位均为 hertz 的 nonnegative vector。如果为噪声数据提供 scalar 值，则该模块会忽略 **Frequency (Hz)** 参数，并对所有频率使用相同的噪声数据。如果为噪声数据提供值的 vector，则其大小必须与频率 vector 相同。该模块使用 **Main** 选项卡中指定的 **Interpolation method** 插值噪声数据。

### 非线性数据

### **IP3 type** — 三阶截点的类型 `OIP3`（默认）| `IIP3`

三阶截点的类型，指定为 `OIP3`（输出截点）或 `IIP3`（输入截点）。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **IP3 (dBm)** — IP3 值 `inf`（默认）| scalar | vector

IP3 值，对于与频率无关的非线性数据指定为以 dBm 为单位的 scalar，对于与频率相关的非线性数据指定为每个元素单位均为 dBm 的 vector。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **1dB gain compression power (dBm)** — 增益下降 1 dB 时的输出功率值 `inf`（默认）| scalar | vector

增益下降 1 dB 时的输出功率值（P1dB,out），对于与频率无关的非线性数据指定为以 dBm 为单位的 scalar，对于与频率相关的非线性数据指定为每个元素单位均为 dBm 的 vector。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **Output saturation power (dBm)** — 放大器完全饱和时产生的输出功率值 `inf`（默认）| scalar | vector

放大器完全饱和时产生的输出功率值（Psat,out），对于与频率无关的非线性数据指定为以 dBm 为单位的 scalar，对于与频率相关的非线性数据指定为每个元素单位均为 dBm 的 vector。如果数据源包含输出饱和功率数据，则此参数被禁用。

### **Gain compression at saturation (dB)** — 增益值的下降量 `3`（默认）| scalar | vector

功率完全饱和时增益值的下降量（GCsat），对于与频率无关的非线性数据指定为以 dB 为单位的 scalar，对于与频率相关的非线性数据指定为每个元素单位均为 dB 的 vector。

### **Frequency (Hz)** — 对应于三阶截点或功率数据的频率点 `2.0e9`（默认）| positive scalar | positive vector

对应于三阶截点或功率数据的频率点，指定为以 hertz 为单位的 positive scalar 或 positive vector。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

#### 依赖关系

- 如果将频率指定为 scalar，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数都必须为 scalars。
- 如果将频率指定为 vector，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数中有一个或多个也必须为 vector。

### 可视化

### **Source of frequency data** — 频率数据源 `Extracted from data source`（默认）| `User-specified`

频率数据源，指定为 `Extracted from data source` 或 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1e9:1e8:2.9e9]`（默认）| vector

频率数据范围，指定为每个元素单位均为 hertz 的 vector。

#### 依赖关系

要启用此参数，请将 **Source of frequency data** 设置为 `User specified`。

### **Source of input power** — 输入功率源 `User-specified`（默认）| `Extracted from data source`

输入功率源，指定为 `Extracted from data source` 或 `User-specified`。如果数据源包含功率数据，则此参数被禁用。

### **Input power data (dBm)** — 输入功率数据范围 `[0:19]`（默认）| vector

输入功率数据范围，指定为每个元素单位均为 dBm 的 vector。如果数据源包含功率数据，则此参数被禁用。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| nonnegative scalar

参考阻抗，指定为以 ohms 为单位的 nonnegative scalar。

### **Plot type** — 数据图的类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据可视化的数据图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建 linear、semilog 或 log-log 图，请相应设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型（基于您设置的 **Plot type**），指定为以下之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | 对于 `X-Y plane` 数据图，**Y parameter1** 会根据您选择的 **Data source** 而变化。有关详细信息，请参阅 Parameters to plot in X-Y pane。 |
| `Composite data` | 不需要设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y parameter2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型（基于您设置的 **Plot type**），指定为以下之一。

| Plot type | Y parameter2 |
| --- | --- |
| `X-Y plane` | 对于 `X-Y plane` 数据图，**Y parameter2** 会根据您选择的 **Data source** 而变化。有关详细信息，请参阅 Parameters to plot in X-Y pane。 |
| `Composite data` | 不需要设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`、`S12`、`S21`、`S22`、`GammaIn`、`GammaOut`、`GammaOPT`、`TF1`、`TF2`、`TF3`、`GammaMS`、`GammaML` 和 `Delta`。 | `dB`、`Magnitude (decibels)`、`Abs`、`Mag`、`Magnitude (linear)`、`Angle`、`Angle(degrees)`、`Angle(radians)`、`Real`、`Imag` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `AM/AM`、`VSWRIn` 和 `VSWROut`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |
| `Pout`、`OIP3` 和 `IIP3`。 | `dBm`、`dBW`、`W` 和 `mW`。 |
| `NF` | `dB` 和 `Magnitude (decibels)`。 |
| `RN`、`NFactor`、`K`、`Mu` 和 `MuPrime`。 | `None` |
| `NTemp` | `Kelvin` |
| `Fmin`、`Gt`、`Ga`、`Gp`、`Gmag` 和 `Gmsg`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |
| `Phase` 和 `AM/PM` | `Angle`、`Angle(degrees)` 和 `Angle(radians)`。 |

#### 依赖关系

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter2 | Y format2 |
| --- | --- |
| `S11`、`S12`、`S21`、`S22`、`GammaIn`、`GammaOut`、`GammaOPT`、`TF1`、`TF2`、`TF3`、`GammaMS`、`GammaML` 和 `Delta`。 | `dB`、`Magnitude (decibels)`、`Abs`、`Mag`、`Magnitude (linear)`、`Angle`、`Angle(degrees)`、`Angle(radians)`、`Real`、`Imag` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `AM/AM`、`VSWRIn` 和 `VSWROut`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |
| `Pout`、`OIP3` 和 `IIP3`。 | `dBm`、`dBW`、`W` 和 `mW`。 |
| `NF` | `dB` 和 `Magnitude (decibels)`。 |
| `RN`、`NFactor`、`K`、`Mu` 和 `MuPrime`。 | `None` |
| `NTemp` | `Kelvin` |
| `Fmin`、`Gt`、`Ga`、`Gp`、`Gmag` 和 `Gmsg`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |
| `Phase` 和 `AM/PM` | `Angle`、`Angle(degrees)` 和 `Angle(radians)`。 |

#### 依赖关系

要启用 **Y format2**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — 频率图 `Freq`（默认）| `AM`

频率图，指定为 `Freq` 或 `AM`。

#### 依赖关系

要将 **X parameter** 设置为 `AM`，必须将 **Y parameter1** 设置为 `AM/AM` 或 `AM/PM`。

### **X format** — 频率图格式 `Hz`（默认）| `Auto` | `kHz` | `MHz` | `GHz` | `THz` | ...

频率图格式，指定为以下之一。

| X parameter | X format |
| --- | --- |
| `Freq` | `Auto`、`Hz`、`kHz`、`MHz`、`GHz` 和 `THz`。 |
| `AM` | `Magnitude (decibels)`、`Magnitude (linear)`、`dB`、`Mag` 和 `None`。 |

### **Y scale** — Y 轴刻度 `Linear`（默认）| `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **X scale** — X 轴刻度 `Linear`（默认）| `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Plot** — 绘制指定数据的按钮

使用 plot 按钮绘制指定数据。

### 工作条件

Agilent® P2D 和 S2D 文件为多个工作条件定义模块参数。工作条件是创建文件数据时使用的独立参数设置。默认情况下，RF Blockset™ Equivalent Baseband 软件使用与文件中出现的第一个工作条件对应的参数值来定义模块行为。要使用其他属性值，必须在 General Amplifier 模块对话框中选择不同的工作条件。

### **Bias** — 放大器偏置 `1.9`（默认）| scalar

放大器偏置，指定为以 volts 为单位的 scalar。当 **Data file** 为 `default.s2p` 时，此参数设置为 `1.9` volts。

## 所属库

RF Blockset / Equivalent Baseband / Amplifiers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

对由对象或文件数据描述的非线性放大器进行建模

General Amplifier 模块对由数据源描述的非线性放大器进行建模。数据源由 RF Toolbox™ 数据（`rfdata.data`）对象或来自文件的数据组成。
