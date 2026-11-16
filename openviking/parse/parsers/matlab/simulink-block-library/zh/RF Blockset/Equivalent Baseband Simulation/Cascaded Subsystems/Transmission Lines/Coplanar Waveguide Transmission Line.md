---
type: simulink-block
title: 'Coplanar Waveguide Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband Simulation / Cascaded Subsystems / Transmission Lines'
documentation_page: 'coplanarwaveguidetransmissionline'
documentation_source_path: 'ref/coplanarwaveguidetransmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# Coplanar Waveguide Transmission Line

## 端口

R2025b 中未记录。

## 参数

### 主

### **导体宽度 (m)** — 导体物理宽度 `0.6e-3` (默认) | scalar

共面波导导体的物理宽度，指定为以 meters 为单位的 scalar。

### **槽宽度 (m)** — 槽物理宽度 `0.2e-3` (默认) | scalar

共面波导槽的物理宽度，指定为以 meters 为单位的 scalar。

### **基板高度 (m)** — 导体所在介质的厚度 `0.635e-3` (默认) | scalar

共面波导中导体所在介质的厚度，指定为以 meters 为单位的 scalar。

### **导体条厚度 (m)** — 导体的物理厚度 `0.005e-3` (默认) | scalar

波在其中传播的导体的物理厚度。

### **相对介电常数** — 介质的相对介电常数 `9.8` (默认) | scalar

介质的相对介电常数，表示为介质的介电常数与自由空间中的介电常数 *ε*0 之比，指定为 scalar。

### **介质损耗角正切** — 介质损耗角正切 `0` (默认) | scalar

介质的损耗角正切，指定为 scalar。

### **导体电导率 (S/m)** — 导体电导率，以 siemens per meter 为单位 `inf` (默认) | scalar

导体电导率，指定为以 siemens per meter 为单位的 scalar。电导率衡量电流在导体中流动的容易程度。

### **传输线长度 (m)** — 传输线物理长度 `0.01` (默认) | scalar

传输线的物理长度，以 meters 为单位指定。

### **短截线模式** — 短截线类型 `Not a stub` (默认) | `Shunt` | `Series`

该模块使您能够将传输线建模为短截线或无短截线。

#### 无短截线传输线

- `Not a stub`—**Not a stub**

  如果将同轴传输线建模为无短截线，则 Coaxial Transmission Line 模块首先计算建模频率向量中包含的每个频率处的 ABCD 参数。然后使用 `abcd2s` 函数将 ABCD 参数转换为 S 参数。有关详细信息，请参阅 Stub Mode- Not a stub。

#### 并联传输线

- `Shunt`—此参数提供二端口网络，该网络由一条短截线传输线组成，您可以将其端接为短路或开路，如下列图所示。

  并联传输线

  *Zin* 是并联电路的输入阻抗。并联短截线的 ABCD 参数计算如下

  A=1B=0C=1/ZinD=1

#### 串联传输线

- `Series`—此模式参数提供二端口网络，该网络由一条串联传输线组成，您可以将其端接为短路或开路，如下列图所示。

  串联传输线

  *Zin* 是串联电路的输入阻抗。串联短截线的 ABCD 参数计算如下

  A=1B=ZinC=0D=1

### **短截线端接** — 短截线端接 `Open` (默认) | `Short`

用于短截线模式 `Shunt` 和 `Series` 的短截线端接。选项为 `Open` 或 `Short`

#### 依赖关系

要启用此参数，请在 **短截线模式** 中选择 `Shunt` 或 `Series`

### 可视化

### **频率数据来源** — 频率数据源 `User-specified` (默认)

频率数据源，指定为 `User-specified`。

### **频率数据 (Hz)** — 频率数据范围 `[1e9:1e6:3e9]` (默认) | vector

频率数据范围，指定为以 hertz 为单位的 vector。

### **参考阻抗 (ohms)** — 参考阻抗 `50` (默认) | nonnegative scalar

参考阻抗，指定为以 ohms 为单位的 nonnegative scalar。

### **绘图类型** — 数据绘图类型 `X-Y plane` (默认) | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据可视化的数据绘图类型，指定为以下选项之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅使用 Equivalent Baseband 库模块创建绘图。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y 参数1** — 要绘制的参数类型 `S11` (默认) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型，指定为以下选项之一。

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

**Y 参数1** 在将 **绘图类型** 设置为 `Composite data` 时被禁用。

### **Y 参数2** — 要绘制的参数类型 `S11` (默认) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型，指定为以下选项之一。

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

**Y 参数2** 在将 **绘图类型** 设置为 `Composite data` 时被禁用。

### **Y 格式1** — 绘图格式 `Magnitude (decibels)` (默认) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下选项之一。

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

### **Y 格式2** — 绘图格式 `Magnitude (decibels)` (默认) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下选项之一。

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

### **X 参数** — 频率绘图 `Freq` (默认)

频率绘图，指定为 `Freq`。

### **X 格式** — 频率绘图格式 `Hz` (默认) | `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率绘图格式，指定为以下选项之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y 刻度** — Y 轴刻度 `Linear` (默认) | `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **绘图类型** 设置为 `X-Y plane`。

### **X 刻度** — X 轴刻度 `Linear` (默认) | `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **绘图类型** 设置为 `X-Y plane`。

### **绘图** — 绘制指定数据的按钮

使用绘图按钮绘制指定数据。

## 所属库

RF Blockset / Equivalent Baseband / Transmission Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2009a 中引入**

## 描述

对共面波导传输线建模

Coplanar Waveguide Transmission Line 模块根据模块对话框中描述的共面波导传输线，以其频率相关的 S 参数进行建模。共面波导传输线的横截面如下图所示。其物理特性包括导体宽度 (*w*)、导体厚度 (*t*)、槽宽度 (*s*)、基板高度 (*d*) 和相对介电常数 (*ε*)。

共面波导传输线的横截面
