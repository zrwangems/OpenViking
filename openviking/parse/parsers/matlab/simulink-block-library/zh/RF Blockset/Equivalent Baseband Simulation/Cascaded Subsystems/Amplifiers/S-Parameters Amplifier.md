---
type: simulink-block
title: 'S-Parameters Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband Simulation / Cascaded Subsystems / Amplifiers'
documentation_page: 'sparametersamplifier'
documentation_source_path: 'ref/sparametersamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# S-Parameters Amplifier

## 端口

R2025b 中未记录。

## 参数

### Main

### **S-Parameters** — 用于非线性放大器的 S-parameters `[0,0;1,0]`（默认）| 2-by-2-by-*M* array

用于非线性放大器的 S-parameters，指定为 2-by-2-by-*M* array，其中 *M* 是 S-parameters 的数量。

### **Frequency (Hz)** — S-parameters 的频率 `2.0e9`（默认）| *M*-element vector

S-parameters 的频率，指定为 *M*-element vector，每个元素的单位为 hertz。

### **Reference Impedance (ohms)** — 网络的参考阻抗 `50`（默认）| nonnegative scalar | vector of length *M*

网络的参考阻抗，指定为以 ohms 为单位的 nonnegative scalar，或长度为 *M* 的 vector，每个元素的单位为 ohms。此参数的值可以是实数或复数。如果提供 scalar 值，则该值应用于所有频率。

### **Interpolation method** — 插值网络参数的方法 `Linear`（默认）| `Spline` | `Cubic`

用于插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
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

### **Noise figure (dB)** — 输入端的可用信噪比与输出端的可用信噪比之比 `0`（默认）| scalar ratio | vector of ratios

输入端的可用信噪比与输出端的可用信噪比之比，指定为 scalar ratio 或 ratios 的 vector。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise figure`。

### **Minimum noise figure** — 输入端的可用信噪比与输出端的可用信噪比之比的最小值 `0`（默认）| scalar ratio | vector of ratios

输入端的可用信噪比与输出端的可用信噪比之比的最小值，指定为 scalar ratio 或 ratios 的 vector。

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

### **Noise factor** — 输入端的可用信噪功率与输出端的可用信噪功率之比 `1`（默认）| scalar ratio | vector of ratios

输入端的可用信噪功率与输出端的可用信噪功率之比，指定为 scalar ratio 或 ratios 的 vector。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise factor`。

### **Noise temperature (K)** — 与放大器产生相同噪声量的等效温度 `0`（默认）| nonnegative scalar | nonnegative vector

与放大器产生相同噪声量的等效温度，指定为以 kelvins 为单位的 nonnegative scalar，或每个元素单位为 kelvins 的 nonnegative vector。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise temperature`。

### **Frequency (Hz)** — 用于表示噪声数据的频率范围 `2.0e9`（默认）| nonnegative scalar | nonnegative vector

用于表示噪声数据的频率范围，指定为以 hertz 为单位的 nonnegative scalar，或每个元素单位为 hertz 的 nonnegative vector。如果为噪声数据提供 scalar 值，则该模块忽略 **Frequency (Hz)** 参数，并对所有频率使用相同的噪声数据。如果为噪声数据提供值的 vector，则其大小必须与频率的 vector 相同。该模块使用 **Main** 选项卡中指定的 **Interpolation method** 来插值噪声数据。

### 非线性数据

### **IP3 type** — 三阶截点的类型 `OIP3`（默认）| `IIP3`

三阶截点的类型，指定为 `OIP3`（输出截点）或 `IIP3`（输入截点）。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **IP3 (dBm)** — IP3 值 `inf`（默认）| scalar | vector

IP3 值，对于频率无关的非线性数据指定为以 dBm 为单位的 scalar，或对于频率相关的非线性数据指定为每个元素单位为 dBm 的 vector。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **1dB gain compression power (dBm)** — 增益下降 1 dB 时的输出功率值 `inf`（默认）| scalar | vector

增益下降 1 dB 时的输出功率值 (P1dB,out)，对于频率无关的非线性数据指定为以 dBm 为单位的 scalar，或对于频率相关的非线性数据指定为每个元素单位为 dBm 的 vector。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **Output saturation power (dBm)** — 放大器完全饱和时产生的输出功率值 `inf`（默认）| scalar | vector

放大器完全饱和时产生的输出功率值 (Psat,out)，对于频率无关的非线性数据指定为以 dBm 为单位的 scalar，或对于频率相关的非线性数据指定为每个元素单位为 dBm 的 vector。如果数据源包含输出饱和功率数据，则此参数被禁用。

### **Gain compression at saturation (dB)** — 增益值的下降量 `3`（默认）| scalar | vector

功率完全饱和时增益值的下降量 (GCsat)，对于频率无关的非线性数据指定为以 dB 为单位的 scalar，或对于频率相关的非线性数据指定为每个元素单位为 dB 的 vector。

### **Frequency (Hz)** — 对应于三阶截点或功率数据的频率点 `2.0e9`（默认）| positive scalar | positive vector

对应于三阶截点或功率数据的频率点，指定为以 hertz 为单位的 positive scalar 或 positive vector。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

#### 依赖关系

- 如果将频率指定为 scalar，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数必须全部为 scalar。
- 如果将频率指定为 vector，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数中的一个或多个也必须为 vector。

### 可视化

### **Source of frequency data** — 频率数据源 `Same as the S-Parameters`（默认）| `User-specified`

频率数据源，指定为 `Same as the S-Parameters` 或 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1.9e9:1.0e8:2.2e9]`（默认）| vector

频率数据范围，指定为每个元素单位为 hertz 的 vector。

#### 依赖关系

要启用此参数，请将 **Source of frequency data** 设置为 `User specified`。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| nonnegative scalar

参考阻抗，指定为以 ohms 为单位的 nonnegative scalar。

### **Plot type** — 数据图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据可视化的数据图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性图、半对数图或双对数图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® chart。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型，指定为以下之一：

|  |  |  |  |
| --- | --- | --- | --- |
| `S11` | `S12` | `S21` | `S22` |
| `GroupDelay` | `GammaIn` | `GammaOut` | `VSWRIn` |
| `VSWROut` | `OIP3` | `IIP3` | `NF` |
| `NFactor` | `NTemp` | `TF1` | `TF2` |
| `TF3` | `Gt` | `Ga` | `Gp` |
| `Gmag` | `Gmsg` | `GammaMS` | `GammaML` |
| `K` | `Delta` | `Mu` | `MuPrime` |

**注意**

当将 **Plot type** 选择为 `Composite data` 时，**Y parameter1** 被禁用。

### **Y parameter2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型，指定为以下之一：

|  |  |  |  |
| --- | --- | --- | --- |
| `S11` | `S12` | `S21` | `S22` |
| `GroupDelay` | `GammaIn` | `GammaOut` | `VSWRIn` |
| `VSWROut` | `OIP3` | `IIP3` | `NF` |
| `NFactor` | `NTemp` | `TF1` | `TF2` |
| `TF3` | `Gt` | `Ga` | `Gp` |
| `Gmag` | `Gmsg` | `GammaMS` | `GammaML` |
| `K` | `Delta` | `Mu` | `MuPrime` |

**注意**

当将 **Plot type** 选择为 `Composite data` 时，**Y parameter2** 被禁用。

### **Y format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, `GammaOut`, `TF1`, `TF2`, `TF3`, `GammaMS`, `GammaML`, and `Delta`. | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `VSWRIn` and `VSWROut`. | `Magnitude (decibels)` and `None`. |
| `OIP3` and `IIP3`. | `dBm`, `W`, and `mW`. |
| `NF` | `dB` and `Magnitude (decibels)`. |
| `NFactor`, `K`, `Mu`, and `MuPrime`. | `None` |
| `NTemp` | `Kelvin` |
| `Gt`, `Ga`, `Gp`, `Gmag`, and `Gmsg`. | `dB`, `Magnitude (decibels)`, and `None`. |

#### 依赖关系

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter2 | Y format2 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, `GammaOut`, `TF1`, `TF2`, `TF3`, `GammaMS`, `GammaML`, and `Delta`. | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `VSWRIn` and `VSWROut`. | `Magnitude (decibels)` and `None`. |
| `OIP3` and `IIP3`. | `dBm`, `W`, and `mW`. |
| `NF` | `dB` and `Magnitude (decibels)`. |
| `NFactor`, `K`, `Mu`, and `MuPrime`. | `None` |
| `NTemp` | `Kelvin` |
| `Gt`, `Ga`, `Gp`, `Gmag`, and `Gmsg`. | `dB`, `Magnitude (decibels)`, and `None`. |

#### 依赖关系

要启用 **Y format2**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — 频率图 `Freq`（默认）

频率图，指定为 `Freq`。

### **X format** — 频率图格式 `Hz`（默认）| `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

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

## 所属库

RF Blockset / Equivalent Baseband / Amplifiers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 S-parameters 对非线性放大器建模

S-Parameters Amplifier 模块根据模块对话框中的描述，使用其频率相关的 S-parameters、S-parameters 的频率和参考阻抗、噪声数据以及非线性数据来对非线性放大器建模。
