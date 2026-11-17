---
type: simulink-block
title: 'Parallel-Plate Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Transmission Lines'
documentation_page: 'parallelplatetransmissionline'
documentation_source_path: 'ref/parallelplatetransmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# Parallel-Plate Transmission Line

## 端口

R2025b 中未记录。

## 参数

#### 主

### **Plate width (m)** — 平行板传输线的宽度 `5e-3`（默认）| 标量

平行板传输线的物理宽度，指定为以米为单位的标量。

### **Plate separation (m)** — 平行板传输线中的电介质间距 `1e-3`（默认）| 标量

分隔板的电介质厚度，指定为以米为单位的标量。

### **Relative permeability constant** — 平行板传输线中电介质材料的相对磁导率 `1`（默认）| 标量

电介质的相对磁导率，表示为电介质的磁导率与自由空间磁导率 *μ*0 之比，指定为标量。

### **Relative permittivity constant** — 平行板传输线中电介质材料的相对介电常数 `2.3`（默认）| 标量

电介质的相对介电常数，表示为电介质的介电常数与自由空间介电常数 *ε*0 之比，指定为标量。

### **Loss tangent of dielectric** — 平行板传输线中电介质的损耗角正切 `0`（默认）| 标量

电介质的损耗角正切，指定为标量。

### **Conductivity of the conductor (S/m)** — 导体的电导率 `inf`（默认）| 标量

导体的电导率，指定为以西门子每米为单位的标量。电导率是衡量导体中电流流动的指标。

### **Transmission line length(m)** — 传输线的物理长度 `0.01`（默认）| 正标量

传输线的物理长度，以米为单位，指定为以米为单位的正标量。

### **Stub mode** — 短截线类型 `Not a stub`（默认）| `Shunt` | `Series`

该模块使您能够将传输线建模为短截线或无短截线线路。

#### 无短截线传输线

- `Not a stub`—**Not a stub**

  如果将平行板传输线建模为无短截线线路，Parallel-Plate Transmission Line 模块首先计算建模频率向量中包含的每个频率处的 ABCD 参数。然后使用 `abcd2s` 函数将 ABCD 参数转换为 S 参数。有关详细信息，请参阅 Stub Mode- Not a stub。

#### 并联和串联短截线

- 平行板传输线的短截线模式分类如下：

  `Shunt`—**Shunt** 参数为用户提供由短截线传输线组成的二端口网络，您可以将其终端接短路或开路，如下所示。

  并联传输线

  *Zin* 是并联电路的输入阻抗。并联短截线的 ABCD 参数计算为

  A=1B=0C=1/ZinD=1

- `Series`—**Series** 参数为用户提供由串联传输线组成的二端口网络，您可以将其终端接短路或开路，如下所示。

  串联传输线

  *Zin* 是串联电路的输入阻抗。串联短截线的 ABCD 参数计算为

  A=1B=ZinC=0D=1

### **Termination of stub** — 短截线终端 `Open`（默认）

短截线模式 `Shunt` 和 `Series` 的短截线终端。选项为 `Open` 或 `Short`

#### 依赖关系

要启用此参数，请在 **Stub mode** 中选择 `Shunt` 或 `Series`

#### 可视化

### **Source of frequency data** — 频率数据源 `User-specified`（默认）

频率数据源，指定为 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1e9:1e6:3e9]`（默认）| 向量

频率数据范围，指定为以 Hz 为单位的向量。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| 非负标量

参考阻抗，指定为以欧姆为单位的非负标量。

### **绘图类型** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据进行可视化的数据绘图类型，指定为以下选项之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成史密斯®圆图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y parameter1** 将被禁用。

### **Y parameter2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y parameter2** 将被禁用。

### **Y format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下选项之一。

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

要启用 **Y format1**，请将 **绘图类型** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下选项之一。

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

要启用 **Y format2**，请将 **绘图类型** 设置为 `X-Y plane`。

### **X parameter** — 频率图 `Freq`（默认值）

频率图，指定为 `Freq`。

### **X format** — 频率图格式 `Hz`（默认值） | `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y scale** — Y 轴刻度 `Linear`（默认值） | `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y
plane`。

### **X scale** — X 轴刻度 `Linear`（默认值） | `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y
plane`。

### **Plot** — 绘制指定数据按钮

使用绘制按钮绘制指定数据。

## 所属库

RF Blockset / Equivalent Baseband / Transmission Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2009a 中引入**

## 描述

对平行板传输线进行建模

Parallel-Plate Transmission Line 模块根据其频率相关 S 参数对模块对话框中描述的平行板传输线进行建模。平行板传输线的横截面如下图所示。其物理特性包括板宽 *w* 和板间距 *d*。

平行板传输线的横截面
