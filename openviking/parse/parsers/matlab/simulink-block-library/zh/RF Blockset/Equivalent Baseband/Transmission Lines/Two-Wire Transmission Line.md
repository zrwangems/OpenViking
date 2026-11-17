---
type: simulink-block
title: 'Two-Wire Transmission Line'
family: 'equivalent-baseband'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Transmission Lines'
documentation_page: 'twowiretransmissionline'
documentation_source_path: 'ref/twowiretransmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Wire Transmission Line

## 端口

未在 R2025b 中记录。

## 参数

### 主要

### **导线半径 (m)** — 导线的半径 `0.67e-3`（默认）| scalar

双线传输线的导线的半径，指定为以 meters 为单位的 scalar。

### **导线间距 (m)** — 双线传输线中的间距 `1.62e-3`（默认）| scalar

导线之间的物理距离，指定为以 meters 为单位的 scalar。

### **相对磁导率常数** — 介质的相对磁导率 `1`（默认）| scalar

介质的相对磁导率，表示为介质的磁导率与自由空间中的磁导率 *μ*0 之比，指定为 scalar。

### **相对介电常数** — 介质的相对介电常数 `2.3`（默认）| scalar

介质的相对介电常数，表示为介质的介电常数与自由空间中的介电常数 *ε*0 之比，指定为 scalar。

### **介电损耗角正切** — 介电损耗角正切 `0`（默认）| scalar

介质的损耗角正切，指定为 scalar。

### **导体电导率 (S/m)** — 导体电导率 `inf`（默认）| scalar

导体的电导率，指定为以 siemens per meter 为单位的 scalar。电导率衡量电流在导体中流动的容易程度。

### **传输线长度 (m)** — 传输线的物理长度 `0.01`（默认）| scalar

传输线的物理长度，指定为以 meters 为单位的 scalar。

### **短截线模式** — 短截线类型 `Not a stub`（默认）| `Shunt` | `Series`

该模块允许您将传输线建模为短截线或无短截线。

#### 无短截线传输线

- `Not a stub`—**Not
  a stub**

  如果将同轴传输线建模为无短截线，则 Coaxial Transmission Line 模块首先计算建模频率向量中包含的每个频率处的 ABCD 参数。然后，它使用 `abcd2s` 函数将 ABCD 参数转换为 S 参数。有关详细信息，请参阅 Stub Mode- Not a stub。

#### 并联传输线

- `Shunt`—此参数提供一个二端口网络，该网络由短截线传输线组成，您可以用短路或开路对其进行端接，如下图所示。

  短路和开路并联短截线

  *Zin* 是并联电路的输入阻抗。并联短截线的 ABCD 参数计算如下

  A=1B=0C=1/ZinD=1

#### 串联传输线

- `Series`—此模式参数提供一个二端口网络，该网络由串联传输线组成，您可以用短路或开路对其进行端接，如下图所示。

  短路和开路串联短截线

  *Zin* 是串联电路的输入阻抗。串联短截线的 ABCD 参数计算如下

  A=1B=ZinC=0D=1

### **短截线端接** — 短截线端接 `Open`（默认）| `Short`

用于短截线模式 `Shunt` 和 `Series` 的短截线端接。可选项为 `Open` 或 `Short`

#### 依赖关系

要启用此参数，请在 **短截线模式** 中选择 `Shunt` 或 `Series`

### 可视化

### **频率数据源** — 频率数据源 `User-specified`（默认）

频率数据源，指定为 `User-specified`。

### **频率数据 (Hz)** — 频率数据范围 `[1e9:1e6:3e9]`（默认）| vector

频率数据范围，指定为以 hertz 为单位的 vector。

### **参考阻抗 (ohms)** — 参考阻抗 `50`（默认）| nonnegative scalar

参考阻抗，指定为以 ohms 为单位的 nonnegative scalar。

### **绘图类型** — 数据图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据可视化的数据图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性图、半对数图或双对数图，请相应地设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅使用 Equivalent Baseband 库模块创建绘图。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`, `Y smith chart`, 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y 参数1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y 参数1** 将禁用。

### **Y 参数2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y 参数2** 将禁用。

### **Y 格式1** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y 参数1 | Y 格式1 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, `GammaOut`, `TF1`, `TF2`, `TF3`, `GammaMS`, `GammaML`, 和 `Delta`. | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, 和 `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, 和 `ps`. |
| `VSWRIn` 和 `VSWROut`. | `Magnitude (decibels)` 和 `None`. |
| `OIP3` 和 `IIP3`. | `dBm`, `W`, 和 `mW`. |
| `NF` | `dB` 和 `Magnitude (decibels)`. |
| `NFactor`, `K`, `Mu`, 和 `MuPrime`. | `None` |
| `NTemp` | `Kelvin` |
| `Gt`, `Ga`, `Gp`, `Gmag`, 和 `Gmsg`. | `dB`, `Magnitude (decibels)`, 和 `None`. |

#### 依赖关系

要启用 **Y 格式1**，请将 **绘图类型** 设置为 `X-Y plane`。

### **Y 格式2** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y 参数2 | Y 格式2 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, `GammaOut`, `TF1`, `TF2`, `TF3`, `GammaMS`, `GammaML`, 和 `Delta`. | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, 和 `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, 和 `ps`. |
| `VSWRIn` 和 `VSWROut`. | `Magnitude (decibels)` 和 `None`. |
| `OIP3` 和 `IIP3`. | `dBm`, `W`, 和 `mW`. |
| `NF` | `dB` 和 `Magnitude (decibels)`. |
| `NFactor`, `K`, `Mu`, 和 `MuPrime`. | `None` |
| `NTemp` | `Kelvin` |
| `Gt`, `Ga`, `Gp`, `Gmag`, 和 `Gmsg`. | `dB`, `Magnitude (decibels)`, 和 `None`. |

#### 依赖关系

要启用 **Y 格式2**，请将 **绘图类型** 设置为 `X-Y plane`。

### **X 参数** — 频率图 `Freq`（默认）

频率图，指定为 `Freq`。

### **X 格式** — 频率图格式 `Hz`（默认）| `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y 轴刻度** — Y 轴刻度 `Linear`（默认）| `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **绘图类型** 设置为 `X-Y plane`。

### **X 轴刻度** — X 轴刻度 `Linear`（默认）| `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **绘图类型** 设置为 `X-Y plane`。

### **绘图** — 绘制指定数据按钮

使用绘图按钮绘制指定数据。

## 所属库

RF Blockset / Equivalent Baseband / Transmission Lines

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2009a 中引入**

## 描述

对双线传输线建模

Two-Wire Transmission Line 模块根据随频率变化的 S 参数，对模块对话框中描述的双线传输线进行建模。下图以横截面形式显示了双线传输线。其物理特性包括导线半径 *a*、导线中心之间的间距或物理距离 *S*，以及导线的相对介电常数和相对磁导率。RF Blockset™ Equivalent Baseband 软件假定相对介电常数和相对磁导率是均匀的。

双线传输线
