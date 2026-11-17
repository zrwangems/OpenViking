---
type: simulink-block
title: 'S-Parameters Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Amplifiers'
documentation_page: 'sparametersamplifier'
documentation_source_path: 'ref/sparametersamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# S-Parameters Amplifier

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: S-Parameters
  summary: 非线性放大器的 S 参数 [0,0;1,0]（默认）| 2×2×*M* 数组
  group: 主要
- name: Frequency (Hz)
  summary: S 参数的频率 2.0e9（默认）| *M* 元向量
  group: 主要
- name: Reference Impedance (ohms)
  summary: 网络的参考阻抗 50（默认）| 非负标量 | 长度为 *M* 的向量
  group: 主要
- name: Interpolation method
  summary: 插值网络参数的方法 Linear（默认）| Spline | Cubic
  group: 主要
- name: Noise type
  summary: 噪声数据的类型 Noise figure（默认）| Spot noise data | Noise factor | Noise temperature
  group: 噪声数据
- name: Noise figure (dB)
  summary: 输入端的可用信噪比与输出端的可用信噪比之比 0（默认）| 标量比值 | 比值向量
  group: 噪声数据
- name: Minimum noise figure
  summary: 输入端的可用信噪比与输出端的可用信噪比之比的最小值 0（默认）| 标量比值 | 比值向量
  group: 噪声数据
- name: Optimal reflection coefficient
  summary: 最佳源阻抗 1+0i（默认）| 复标量 | 复向量
  group: 噪声数据
- name: Equivalent normalized noise resistance
  summary: 用于进行噪声测量的归一化电阻值 1（默认）| 正标量 | 正向量
  group: 噪声数据
- name: Noise factor
  summary: 输入端的可用信噪功率与输出端的可用信噪功率之比 1（默认）| 标量比值 | 比值向量
  group: 噪声数据
- name: Noise temperature (K)
  summary: 产生与放大器相同噪声量的等效温度 0（默认）| 非负标量 | 非负向量
  group: 噪声数据
- name: Frequency (Hz)
  summary: 用于表示噪声数据的频率范围 2.0e9（默认）| 非负标量 | 非负向量
  group: 噪声数据
- name: IP3 type
  summary: 三阶截点的类型 OIP3（默认）| IIP3
  group: 非线性数据
- name: IP3 (dBm)
  summary: IP3 值 inf（默认）| 标量 | 向量
  group: 非线性数据
- name: 1dB gain compression power (dBm)
  summary: 增益下降 1 dB 时的输出功率值 inf（默认）| 标量 | 向量
  group: 非线性数据
- name: Output saturation power (dBm)
  summary: 放大器完全饱和时产生的输出功率值 inf（默认）| 标量 | 向量
  group: 非线性数据
- name: Gain compression at saturation (dB)
  summary: 增益下降值 3（默认）| 标量 | 向量
  group: 非线性数据
- name: Frequency (Hz)
  summary: 对应于三阶截点或功率数据的频率点 2.0e9（默认）| 正标量 | 正向量
  group: 非线性数据
- name: Source of frequency data
  summary: 频率数据源 Same as the S-Parameters（默认）| User-specified
  group: 可视化
- name: Frequency data (Hz)
  summary: 频率数据范围 [1.9e9:1.0e8:2.2e9]（默认）| 向量
  group: 可视化
- name: Reference impedance (ohms)
  summary: 参考阻抗 50（默认）| 非负标量
  group: 可视化
- name: Plot type
  summary: 数据绘图类型 X-Y plane（默认）| Composite data | Polar plane | Z Smith chart | Y Smith chart | ZY Smith chart
  group: 可视化
- name: Y parameter1
  summary: 要绘制的参数类型 S11（默认）| S12 | S21 | S22 | GroupDelay | OIP3 | IIP3 | NF | ...
  group: 可视化
- name: Y parameter2
  summary: 要绘制的参数类型 S11（默认）| S12 | S21 | S22 | GroupDelay | OIP3 | IIP3 | NF | ...
  group: 可视化
- name: Y format1
  summary: 绘图格式 Magnitude (decibels)（默认）| Mag | Magnitude (linear) | Angle | Real | Imaginary | ...
  group: 可视化
- name: Y format2
  summary: 绘图格式 Magnitude (decibels)（默认）| Mag | Magnitude (linear) | Angle | Real | Imaginary | ...
  group: 可视化
- name: X parameter
  summary: 频率图 Freq（默认值）
  group: 可视化
- name: X format
  summary: 频率图格式 Hz（默认值）| Auto | kHz | MHz | GHz | THz
  group: 可视化
- name: Y scale
  summary: Y 轴刻度 Linear（默认值）| Log
  group: 可视化
- name: X scale
  summary: X 轴刻度 Linear（默认值）| Log
  group: 可视化
- name: Plot
  summary: 绘制指定数据按钮
  group: 可视化
```

### 主要

### **S-Parameters** — 非线性放大器的 S 参数 `[0,0;1,0]`（默认）| 2×2×*M* 数组

非线性放大器的 S 参数，指定为 2×2×*M* 数组，其中 *M* 是 S 参数的数量。

### **Frequency (Hz)** — S 参数的频率 `2.0e9`（默认）| *M* 元向量

S 参数的频率，指定为 *M* 元向量，每个元素的单位为赫兹。

### **Reference Impedance (ohms)** — 网络的参考阻抗 `50`（默认）| 非负标量 | 长度为 *M* 的向量

网络的参考阻抗，指定为以欧姆为单位的非负标量或以欧姆为单位的长度为 *M* 的向量，每个元素的单位为欧姆。此参数的值可以是实数或复数。如果提供标量值，则该值应用于所有频率。

### **Interpolation method** — 插值网络参数的方法 `Linear`（默认）| `Spline` | `Cubic`

插值网络参数的方法，指定为以下之一：

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

### **Noise figure (dB)** — 输入端的可用信噪比与输出端的可用信噪比之比 `0`（默认）| 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比之比，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise figure`。

### **Minimum noise figure** — 输入端的可用信噪比与输出端的可用信噪比之比的最小值 `0`（默认）| 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比之比的最小值，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Optimal reflection coefficient** — 最佳源阻抗 `1+0i`（默认）| 复标量 | 复向量

最佳源阻抗，指定为复标量或复向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Equivalent normalized noise resistance** — 用于进行噪声测量的归一化电阻值 `1`（默认）| 正标量 | 正向量

用于进行噪声测量的归一化电阻值，指定为正标量或正向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Noise factor** — 输入端的可用信噪功率与输出端的可用信噪功率之比 `1`（默认）| 标量比值 | 比值向量

输入端的可用信噪功率与输出端的可用信噪功率之比，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise factor`。

### **Noise temperature (K)** — 产生与放大器相同噪声量的等效温度 `0`（默认）| 非负标量 | 非负向量

产生与放大器相同噪声量的等效温度，指定为以开尔文为单位的非负标量或以开尔文为单位的非负向量，每个元素的单位为开尔文。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise temperature`。

### **Frequency (Hz)** — 用于表示噪声数据的频率范围 `2.0e9`（默认）| 非负标量 | 非负向量

用于表示噪声数据的频率范围，指定为以赫兹为单位的非负标量或以赫兹为单位的非负向量，其中每个元素的单位为赫兹。如果为噪声数据提供标量值，该模块将忽略 **Frequency (Hz)** 参数，并对所有频率使用相同的噪声数据。如果为噪声数据提供向量值，则其大小必须与频率向量相同。该模块使用 **Main** 选项卡中指定的 **Interpolation method** 对噪声数据进行插值。

### 非线性数据

### **IP3 type** — 三阶截点的类型 `OIP3`（默认）| `IIP3`

三阶截点的类型，指定为 `OIP3`（输出截点）或 `IIP3`（输入截点）。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **IP3 (dBm)** — IP3 值 `inf`（默认）| 标量 | 向量

IP3 值，对于与频率无关的非线性数据，指定为以 dBm 为单位的标量；对于与频率相关的非线性数据，指定为以 dBm 为单位的向量，其中每个元素的单位为 dBm。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **1dB gain compression power (dBm)** — 增益下降 1 dB 时的输出功率值 `inf`（默认）| 标量 | 向量

增益下降 1 dB 时的输出功率值（P1dB,out），对于与频率无关的非线性数据，指定为以 dBm 为单位的标量；对于与频率相关的非线性数据，指定为以 dBm 为单位的向量，其中每个元素的单位为 dBm。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **Output saturation power (dBm)** — 放大器完全饱和时产生的输出功率值 `inf`（默认）| 标量 | 向量

放大器完全饱和时产生的输出功率值（Psat,out），对于与频率无关的非线性数据，指定为以 dBm 为单位的标量；对于与频率相关的非线性数据，指定为以 dBm 为单位的向量，其中每个元素的单位为 dBm。如果数据源包含输出饱和功率数据，则此参数被禁用。

### **Gain compression at saturation (dB)** — 增益下降值 `3`（默认）| 标量 | 向量

功率完全饱和时的增益下降值（GCsat），对于与频率无关的非线性数据，指定为以 dB 为单位的标量；对于与频率相关的非线性数据，指定为以 dB 为单位的向量，其中每个元素的单位为 dB。

### **Frequency (Hz)** — 对应于三阶截点或功率数据的频率点 `2.0e9`（默认）| 正标量 | 正向量

对应于三阶截点或功率数据的频率点，指定为以赫兹为单位的正标量或正向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

#### 依赖关系

- 如果将频率指定为标量，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数必须全部为标量。
- 如果将频率指定为向量，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数中的一个或多个也必须为向量。

### 可视化

### **Source of frequency data** — 频率数据源 `Same as the S-Parameters`（默认）| `User-specified`

频率数据源，指定为 `Same as the S-Parameters` 或 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1.9e9:1.0e8:2.2e9]`（默认）| 向量

频率数据范围，指定为向量，其中每个元素的单位为赫兹。

#### 依赖关系

要启用此参数，请将 **Source of frequency data** 设置为 `User specified`。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| 非负标量

参考阻抗，指定为以欧姆为单位的非负标量。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据进行可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 圆图。该模块仅绘制与指定频率对应的数据范围。

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

当 **Plot type** 选择为 `Composite data` 时，**Y parameter1** 被禁用。

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

当 **Plot type** 选择为 `Composite data` 时，**Y parameter2** 被禁用。

### **Y format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`、`S12`、`S21`、`S22`、`GammaIn`、`GammaOut`、`TF1`、`TF2`、`TF3`、`GammaMS`、`GammaML` 和 `Delta`。 | `dB`、`Magnitude (decibels)`、`Abs`、`Mag`、`Magnitude (linear)`、`Angle`、`Angle(degrees)`、`Angle(radians)`、`Real`、`Imag` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `VSWRIn` 和 `VSWROut`。 | `Magnitude (decibels)` 和 `None`。 |
| `OIP3` 和 `IIP3`。 | `dBm`、`W` 和 `mW`。 |
| `NF` | `dB` 和 `Magnitude (decibels)`。 |
| `NFactor`、`K`、`Mu` 和 `MuPrime`。 | `None` |
| `NTemp` | `Kelvin` |
| `Gt`、`Ga`、`Gp`、`Gmag` 和 `Gmsg`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |

#### 依赖关系

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter2 | Y format2 |
| --- | --- |
| `S11`、`S12`、`S21`、`S22`、`GammaIn`、`GammaOut`、`TF1`、`TF2`、`TF3`、`GammaMS`、`GammaML` 和 `Delta`。 | `dB`、`Magnitude (decibels)`、`Abs`、`Mag`、`Magnitude (linear)`、`Angle`、`Angle(degrees)`、`Angle(radians)`、`Real`、`Imag` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `VSWRIn` 和 `VSWROut`。 | `Magnitude (decibels)` 和 `None`。 |
| `OIP3` 和 `IIP3`。 | `dBm`、`W` 和 `mW`。 |
| `NF` | `dB` 和 `Magnitude (decibels)`。 |
| `NFactor`、`K`、`Mu` 和 `MuPrime`。 | `None` |
| `NTemp` | `Kelvin` |
| `Gt`、`Ga`、`Gp`、`Gmag` 和 `Gmsg`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |

#### 依赖关系

要启用 **Y format2**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — 频率图 `Freq`（默认值）

频率图，指定为 `Freq`。

### **X format** — 频率图格式 `Hz`（默认值）| `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y scale** — Y 轴刻度 `Linear`（默认值）| `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y
plane`。

### **X scale** — X 轴刻度 `Linear`（默认值）| `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y
plane`。

### **Plot** — 绘制指定数据按钮

使用绘制按钮绘制指定数据。
## 所属库

RF Blockset / Equivalent Baseband / Amplifiers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 S 参数对非线性放大器建模

S-Parameters Amplifier 模块根据其频率相关的 S 参数、S 参数的频率和参考阻抗、噪声数据以及非线性数据，对模块对话框中描述的非线性放大器进行建模。
