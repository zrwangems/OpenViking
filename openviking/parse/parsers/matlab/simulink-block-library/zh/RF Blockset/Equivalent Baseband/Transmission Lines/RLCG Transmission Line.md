---
type: simulink-block
title: 'RLCG Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Transmission Lines'
documentation_page: 'rlcgtransmissionline'
documentation_source_path: 'ref/rlcgtransmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# RLCG Transmission Line

## 端口

R2025b 中未记载。

## 参数

### 主要

### **每单位长度电阻 (ohms/m)** — RLGC 传输线的电阻 `0`（默认） | scalar

RLGC 传输线的电阻，指定为以 ohms/meters 为单位的 scalar。

### **每单位长度电感 (H/m)** — RLGC 传输线的电感 `0`（默认） | scalar

RLGC 传输线的电感，指定为以 henries/meters 为单位的 scalar。

### **每单位长度电容 (F/m)** — RLGC 传输线的电容 `0`（默认）

RLGC 传输线的电容，指定为以 farad/meters 为单位的 scalar

### **每单位长度电导(S/m)** — RLGC 传输线的电导 `0`（默认） | scalar

RLGC 传输线的电导，指定为以 siemens per meter 为单位的 scalar。

### **频率 (Hz)** — RLGC 传输线工作的频率 `1e-9`（默认）

频率值的 vector，在这些频率下已知 resistance、inductance、capacitance 和 conductance 值。

### **插值方法** — 插值网络参数的方法 `Linear`（默认） | `Spline` | `Cubic`

插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### **传输线长度 (m)** — 传输线的物理长度 `0.01`（默认） | scalar

传输线的物理长度，指定为以 meters 为单位的 scalar。

### **短截线模式** — 短截线类型 `Not a stub`（默认） | `Shunt` | `Series`

该模块允许您将传输线建模为短截线或无短截线线路。

#### 无短截线传输线

- `Not a stub`—**Not a stub**

  如果将以无短截线线路对同轴传输线进行建模，则 Coaxial Transmission Line 模块首先计算建模频率 vector 中包含的每个频率处的 ABCD 参数。然后使用 `abcd2s` 函数将 ABCD 参数转换为 S 参数。有关详细信息，请参阅 Stub Mode - Not a Stub。

#### 并联传输线

- `Shunt`—此参数提供一个二端口网络，该网络由一段短截线传输线组成，您可以用短路或开路端接，如下图所示。

  并联传输线

  *Zin* 是并联电路的输入阻抗。并联短截线的 ABCD 参数计算如下

  A=1B=0C=1/ZinD=1

#### 串联传输线

- `Series`—此模式参数提供一个二端口网络，该网络由一段串联传输线组成，您可以用短路或开路端接，如下图所示。

  串联传输线

  *Zin* 是串联电路的输入阻抗。串联短截线的 ABCD 参数计算如下

  A=1B=ZinC=0D=1

### **短截线端接** — 短截线端接 `Open`（默认） | `Short`

用于短截线模式 `Shunt` 和 `Series` 的短截线端接。可选值为 `Open` 或 `Short`

#### 依赖关系

要启用此参数，请在 **短截线模式** 中选择 `Shunt` 或 `Series`

### 可视化

### **频率数据源** — 频率数据源 `User-specified`（默认）

频率数据源，指定为 `User-specified`。

### **频率数据 (Hz)** — 频率数据范围 `[1e9:1e6:3e9]`（默认） | vector

频率数据范围，指定为以 hertz 为单位的 vector。

### **参考阻抗 (ohms)** — 参考阻抗 `50`（默认） | nonnegative scalar

参考阻抗，指定为以 ohms 为单位的 nonnegative scalar。

### **绘图类型** — 数据绘图类型 `X-Y plane`（默认） | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据相对于频率的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y 参数1** — 要绘制的参数类型 `S11`（默认） | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型，指定为以下之一。

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y 参数1** 会被禁用。

### **Y 参数2** — 要绘制的参数类型 `S11`（默认） | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型，指定为以下之一。

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y 参数2** 会被禁用。

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

### **绘图** — 绘制指定数据按钮

使用绘图按钮绘制指定数据。

## 所属库

RF Blockset / Equivalent Baseband / Transmission Lines

## 模块特性

R2025b 中未记载。

## 扩展功能

R2025b 中未记载。

## 版本历史

**在 R2009a 中引入**

## 描述

对 RLCG 传输线建模

RLCG Transmission Line 模块根据随频率变化的电阻、电感、电容和电导，对模块对话框中描述的 RLCG 传输线进行建模。该传输线可以是有损或无损耗的，被视为二端口线性网络。

RLGC 传输线横截面

其中 *z*′ = *z* + Δ*z*。

要了解如何使用 RLCG Transmission Line 模块创建基带等效模型，请参阅 Create Complex Baseband-Equivalent Model。
