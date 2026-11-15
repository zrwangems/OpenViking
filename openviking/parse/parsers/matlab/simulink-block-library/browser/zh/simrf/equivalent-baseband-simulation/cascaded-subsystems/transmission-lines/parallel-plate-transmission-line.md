---
type: simulink-block
title: 'Parallel-Plate Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband Simulation / Cascaded Subsystems / Transmission Lines'
documentation_page: 'parallelplatetransmissionline'
documentation_source_path: 'ref/parallelplatetransmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# Parallel-Plate Transmission Line

## 端口

R2025b 中未记录。

## 参数

#### 主要

### **极板宽度 (m)** — 平行板传输线的宽度 `5e-3`（默认）| scalar

平行板传输线的物理宽度，以 meters 为单位指定为 scalar。

### **极板间距 (m)** — 平行板传输线中的电介质间距 `1e-3`（默认）| scalar

分隔极板的电介质厚度，以 meters 为单位指定为 scalar。

### **相对磁导率常数** — 平行板传输线中电介质材料的相对磁导率 `1`（默认）| scalar

电介质的相对磁导率，表示为电介质的磁导率与自由空间中的磁导率 *μ*0 之比，指定为 scalar。

### **相对介电常数** — 平行板传输线中电介质材料的相对介电常数 `2.3`（默认）| scalar

电介质的相对介电常数，表示为电介质的介电常数与自由空间中的介电常数 *ε*0 之比，指定为 scalar。

### **电介质损耗角正切** — 平行板传输线中电介质的损耗角正切 `0`（默认）| scalar

电介质的损耗角正切，指定为 scalar。

### **导体电导率 (S/m)** — 导体的电导率 `inf`（默认）| scalar

导体的电导率，以 siemens per meter 为单位指定为 scalar。电导率是衡量导体中电流流动的指标。

### **传输线长度(m)** — 传输线的物理长度 `0.01`（默认）| positive scalar

传输线的物理长度，单位为 meters，指定为以 meters 为单位的 positive scalar。

### **短截线模式** — 短截线类型 `Not a stub`（默认）| `Shunt` | `Series`

该模块使您能够将传输线建模为短截线或非短截线。

#### 无短截线传输线

- `Not a stub`—**Not a
  stub**

  如果将平行板传输线建模为无短截线线路，则 Parallel-Plate Transmission Line 模块首先计算建模频率向量中包含的每个频率处的 ABCD 参数。然后，它使用 `abcd2s` 函数将 ABCD 参数转换为 S 参数。有关详细信息，请参阅短截线模式 - Not a stub。

#### Shunt 和 Series 短截线

- 平行板传输线的短截线模式分类如下：

  `Shunt`—**Shunt**
  参数为用户提供由短截线传输线组成的二端口网络，您可以用短路或开路端接，如下所示。

  Shunt 传输线

  *Zin* 是并联电路的输入阻抗。并联短截线的 ABCD 参数计算如下：

  A=1B=0C=1/ZinD=1

- `Series`—**Series**
  参数为用户提供由串联传输线组成的二端口网络，您可以用短路或开路端接，如下所示。

  Series 传输线

  *Zin* 是串联电路的输入阻抗。串联短截线的 ABCD 参数计算如下：

  A=1B=ZinC=0D=1

### **短截线终端** — 短截线终端 `Open`（默认）

用于 `Shunt` 和 `Series` 短截线模式的短截线终端。选项为 `Open` 或 `Short`

#### 依赖关系

要启用此参数，请在 **短截线模式** 中选择 `Shunt` 或 `Series`

#### 可视化

### **频率数据源** — 频率数据源 `User-specified`（默认）

频率数据源，指定为 `User-specified`。

### **频率数据 (Hz)** — 频率数据范围 `[1e9:1e6:3e9]`（默认）| vector

频率数据范围，以 Hz 为单位指定为 vector。

### **参考阻抗 (ohms)** — 参考阻抗 `50`（默认）| nonnegative scalar

参考阻抗，以 ohms 为单位指定为 nonnegative scalar。

### **绘图类型** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据可视化的数据绘图类型，指定为下列之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅使用等效基带库模块创建绘图。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y 参数1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型，指定为下列之一。

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y 参数1** 将被禁用。

### **Y 参数2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

要绘制的参数类型，指定为下列之一。

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y 参数2** 将被禁用。

### **Y 格式1** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为下列之一。

| Y 参数1 | Y 格式1 |
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

要启用 **Y 格式1**，请将 **绘图类型** 设置为 `X-Y plane`。

### **Y 格式2** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为下列之一。

| Y 参数2 | Y 格式2 |
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

要启用 **Y 格式2**，请将 **绘图类型** 设置为 `X-Y plane`。

### **X 参数** — 频率绘图 `Freq`（默认）

频率绘图，指定为 `Freq`。

### **X 格式** — 频率绘图格式 `Hz`（默认）| `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率绘图格式，指定为下列之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y 刻度** — Y 轴刻度 `Linear`（默认）| `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **绘图类型** 设置为 `X-Y plane`。

### **X 刻度** — X 轴刻度 `Linear`（默认）| `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **绘图类型** 设置为 `X-Y plane`。

### **绘图** — 绘制指定数据按钮

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

对平行板传输线建模

Parallel-Plate Transmission Line 模块根据块对话框中的描述，以频率相关 S 参数对平行板传输线进行建模。平行板传输线的横截面如下图所示。其物理特性包括极板宽度 *w* 和极板间距 *d*。

平行板传输线的横截面
