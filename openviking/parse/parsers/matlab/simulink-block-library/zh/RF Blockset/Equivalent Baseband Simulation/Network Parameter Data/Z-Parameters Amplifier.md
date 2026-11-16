---
type: simulink-block
title: 'Z-Parameters Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband Simulation / Cascaded Subsystems / Amplifiers'
documentation_page: 'zparametersamplifier'
documentation_source_path: 'ref/zparametersamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# Z-Parameters Amplifier

## 端口

R2025b 中未记录。

## 参数

### 主要

### **Z 参数** — 非线性放大器的 Z 参数 `[0.0200,0;-0.0400, 0.0200]`（默认） | 2-by-2-by-*M* 数组

非线性放大器的 Z 参数，指定为 2-by-2-by-*M* 数组，其中 *M* 是 Z 参数的数量。

### **频率 (Hz)** — Z 参数的频率 `2.0e9`（默认） | *M* 元素向量

Z 参数的频率，指定为 *M* 元素向量，每个元素的单位为 hertz。

### **插值方法** — 插值网络参数的方法 `Linear`（默认） | `Spline` | `Cubic`

用于插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### 噪声数据

### **噪声类型** — 噪声数据的类型 `Noise figure`（默认） | `Spot noise data` | `Noise factor` | `Noise temperature`

噪声数据的类型，指定为以下之一：

- `Noise figure`
- `Spot noise data`
- `Noise factor`
- `Noise temperature`

如果数据源包含噪声数据，则此参数被禁用。

### **噪声系数 (dB)** — 输入端的可用信噪比与输出端的可用信噪比之比 `0`（默认） | 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比之比，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Noise figure`。

### **最小噪声系数** — 输入端的可用信噪比与输出端的可用信噪比的最小比值 `0`（默认） | 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比的最小比值，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Spot noise data`。

### **最佳反射系数** — 最佳源阻抗 `1+0i`（默认） | 复标量 | 复向量

最佳源阻抗，指定为复标量或复向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Spot noise data`。

### **等效归一化噪声电阻** — 用于进行噪声测量的归一化电阻值 `1`（默认） | 正标量 | 正向量

用于进行噪声测量的归一化电阻值，指定为正标量或正向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Spot noise data`。

### **噪声因子** — 输入端的可用信噪功率与输出端的可用信噪功率之比 `1`（默认） | 标量比值 | 比值向量

输入端的可用信噪功率与输出端的可用信噪功率之比，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Noise factor`。

### **噪声温度 (K)** — 与放大器产生相同噪声量的等效温度 `0`（默认） | 非负标量 | 非负向量

与放大器产生相同噪声量的等效温度，指定为以 kelvins 为非负标量，或每个元素单位均为 kelvins 的非负向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Noise temperature`。

### **频率 (Hz)** — 用于表示噪声数据的频率域 `2.0e9`（默认） | 非负标量 | 非负向量

用于表示噪声数据的频率域，指定为以 hertz 为非负标量，或每个元素单位均为 hertz 的非负向量。如果为噪声数据提供标量值，则该模块忽略 **频率 (Hz)** 参数，并对所有频率使用相同的噪声数据。如果为噪声数据提供值向量，则其大小必须与频率向量相同。该模块使用 **主要** 选项卡中指定的 **插值方法** 来插值噪声数据。

### 非线性数据

### **IP3 类型** — 三阶截点类型 `OIP3`（默认） | `IIP3`

三阶截点类型，指定为 `OIP3`（输出截点）或 `IIP3`（输入截点）。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **IP3 (dBm)** — IP3 值 `inf`（默认） | 标量 | 向量

IP3 值，对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素单位均为 dBm 的向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **1dB 增益压缩功率 (dBm)** — 增益下降 1 dB 时的输出功率值 `inf`（默认） | 标量 | 向量

增益下降 1 dB 时的输出功率值 (P1dB,out)，对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素单位均为 dBm 的向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **输出饱和功率 (dBm)** — 放大器完全饱和时产生的输出功率值 `inf`（默认） | 标量 | 向量

放大器完全饱和时产生的输出功率值 (Psat,out)，对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素单位均为 dBm 的向量。如果数据源包含输出饱和功率数据，则此参数被禁用。

### **饱和时的增益压缩 (dB)** — 增益值的下降量 `3`（默认） | 标量 | 向量

功率完全饱和时增益值的下降量 (GCsat)，对于频率无关的非线性数据，指定为以 dB 为单位的标量；对于频率相关的非线性数据，指定为每个元素单位均为 dB 的向量。

### **频率 (Hz)** — 对应于三阶截点或功率数据的频率点 `2.0e9`（默认） | 正标量 | 正向量

对应于三阶截点或功率数据的频率点，指定为以 hertz 为单位的正标量或正向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

#### 依赖关系

- 如果将频率指定为标量，则 **IP3 (dBm)**、**1dB 增益压缩功率 (dBm)** 和 **输出饱和功率 (dBm)** 参数都必须为标量。
- 如果将频率指定为向量，则 **IP3 (dBm)**、**1dB 增益压缩功率 (dBm)** 和 **输出饱和功率 (dBm)** 参数中的一个或多个也必须为向量。

### 可视化

### **频率数据源** — 频率数据源 `Same as the Z-Parameters`（默认） | `User-specified`

频率数据源，指定为 `Same as the Z-Parameters` 或 `User-specified`。

### **频率数据 (Hz)** — 频率数据范围 `[1.9e9:1.0e8:2.2e9]`（默认） | 向量

频率数据范围，指定为每个元素单位均为 hertz 的向量。

#### 依赖关系

要启用此参数，请将 **频率数据源** 设置为 `User specified`。

### **参考阻抗 (ohms)** — 参考阻抗 `50`（默认） | 非负标量

参考阻抗，指定为以 ohms 为非负标量。

### **绘图类型** — 数据绘图类型 `X-Y plane`（默认） | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据进行可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性图、半对数图或双对数图，请相应设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y 参数1** — 要绘制的参数类型 `S11`（默认） | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当将 **绘图类型** 选择为 `Composite data` 时，**Y 参数1** 被禁用。

### **Y 参数2** — 要绘制的参数类型 `S11`（默认） | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当将 **绘图类型** 选择为 `Composite data` 时，**Y 参数2** 被禁用。

### **Y 格式1** — 绘图格式 `Magnitude (decibels)`（默认） | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y 参数1 | Y 格式1 |
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

要启用 **Y 格式1**，请将 **绘图类型** 设置为 `X-Y plane`。

### **Y 格式2** — 绘图格式 `Magnitude (decibels)`（默认） | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y 参数2 | Y 格式2 |
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

要启用 **Y 格式2**，请将 **绘图类型** 设置为 `X-Y plane`。

### **X 参数** — 频率绘图 `Freq`（默认）

频率绘图，指定为 `Freq`。

### **X 格式** — 频率绘图格式 `Hz`（默认） | `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率绘图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y 轴刻度** — Y 轴刻度 `Linear`（默认） | `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **绘图类型** 设置为 `X-Y plane`。

### **X 轴刻度** — X 轴刻度 `Linear`（默认） | `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **绘图类型** 设置为 `X-Y plane`。

### **绘图** — 绘制指定数据的按钮

使用绘图按钮绘制指定数据。

## 所属库

RF Blockset / Equivalent Baseband / Amplifiers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前推出**

## 描述

使用 Z 参数对非线性放大器建模

Z-Parameters Amplifier 模块根据模块对话框中描述的非线性放大器，使用其频率相关的 Z 参数、Z 参数的频率、噪声数据和非线性数据对该非线性放大器建模。
