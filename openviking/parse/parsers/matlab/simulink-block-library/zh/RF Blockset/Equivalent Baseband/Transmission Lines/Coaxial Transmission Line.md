---
type: simulink-block
title: 'Coaxial Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Transmission Lines'
documentation_page: 'coaxialtransmissionline'
documentation_source_path: 'ref/coaxialtransmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# Coaxial Transmission Line

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Outer radius (m)
  summary: 外导体半径 2.57e-3（默认）| 标量
  group: 主
- name: Inner radius(m)
  summary: 内导体半径 0.725e-3（默认）| 标量
  group: 主
- name: Relative permeability constant
  summary: 电介质的相对磁导率 1（默认）| 实标量
  group: 主
- name: Relative permittivity constant
  summary: 电介质的相对介电常数 2.3（默认）| 实标量
  group: 主
- name: Loss tangent of dielectric
  summary: 电介质损耗角正切 0（默认）| 非负标量
  group: 主
- name: Conductivity of the conductor (S/m)
  summary: 导体电导率 inf（默认）| 正标量
  group: 主
- name: Transmission line length (m)
  summary: 传输线物理长度 0.01（默认）| 正标量
  group: 主
- name: Stub mode
  summary: 短截线类型 Not a stub（默认）| Shunt | Series
  group: 主
- name: Termination of stub
  summary: 短截线终端 Open（默认）| Short
  group: 主
- name: Source of frequency data
  summary: 频率数据源 User-specified（默认）
  group: 可视化
- name: Frequency data (Hz)
  summary: 频率数据范围 [1e9:1e6:3e9]（默认）| 向量
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

### 主

### **Outer radius (m)** — 外导体半径 `2.57e-3`（默认）| 标量

同轴传输线外导体半径，指定为以米为单位的标量。

### **Inner radius(m)** — 内导体半径 `0.725e-3`（默认）| 标量

同轴传输线内导体半径，指定为以米为单位的标量。

### **Relative permeability constant** — 电介质的相对磁导率 `1`（默认）| 实标量

电介质的相对磁导率，表示为电介质磁导率与自由空间磁导率 *μ*0 之比，指定为实标量。

### **Relative permittivity constant** — 电介质的相对介电常数 `2.3`（默认）| 实标量

电介质的相对介电常数，表示为电介质介电常数与自由空间介电常数 *ε*0 之比，指定为实标量。

### **Loss tangent of dielectric** — 电介质损耗角正切 `0`（默认）| 非负标量

电介质的损耗角正切，指定为非负标量。

### **Conductivity of the conductor (S/m)** — 导体电导率 `inf`（默认）| 正标量

导体的电导率，指定为以西门子/米为单位的正标量。

### **Transmission line length (m)** — 传输线物理长度 `0.01`（默认）| 正标量

传输线的物理长度，指定为以米为单位的正标量。

### **Stub mode** — 短截线类型 `Not a stub`（默认）| `Shunt` | `Series`

该模块使您能够将传输线建模为短截线或无短截线线路。

#### 无短截线传输线

- `Not a stub`—**不是短截线**

  如果将同轴传输线建模为无短截线线路，Coaxial Transmission Line 模块首先计算建模频率向量中包含的每个频率处的 ABCD 参数。然后使用 `abcd2s` 函数将 ABCD 参数转换为 S 参数。有关详细信息，请参阅短截线模式 - 不是短截线。

#### 并联传输线

- `Shunt`—此参数提供一个双端口网络，该网络由短截线传输线组成，您可以将其终端接为短路或开路，如下图所示。

  并联传输线

  *Zin* 是并联电路的输入阻抗，其计算方法如下：

  对于短路传输线

  Zin=jZ0tanγl

  对于开路传输线

  Zin=−jZ0cotγl

  其中

  - *Z0* 是特性阻抗，以及
  - γ 是传播常数

  并联短截线的 ABCD 参数计算为

  A=1B=0C=1/ZinD=1

#### 串联传输线

- `Series`—此模式参数提供一个双端口网络，该网络由串联传输线组成，您可以将其终端接为短路或开路，如下图所示。

  串联传输线

  *Zin* 是串联电路的输入阻抗。串联短截线的 ABCD 参数计算为

  A=1B=ZinC=0D=1

### **Termination of stub** — 短截线终端 `Open`（默认）| `Short`

短截线模式 `Shunt` 和 `Series` 的短截线终端。选项为 `Open` 或 `Short`

#### 依赖关系

要启用此参数，请在 **Stub mode** 中选择 `Shunt` 或 `Series`

### 可视化

### **Source of frequency data** — 频率数据源 `User-specified`（默认）

频率数据源，指定为 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1e9:1e6:3e9]`（默认）| 向量

频率数据范围，指定为以赫兹为单位的向量。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| 非负标量

参考阻抗，指定为以欧姆为单位的非负标量。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据进行可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 圆图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当您将 **Plot type** 选择为 `Composite data` 时，**Y parameter1** 将被禁用。

### **Y parameter2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当您将 **Plot type** 选择为 `Composite data` 时，**Y parameter2** 将被禁用。

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

RF Blockset / Equivalent Baseband / Transmission Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2009a 中引入**

## 描述

对同轴传输线建模

Coaxial Transmission Line 模块使用 S 参数对其频率行为进行建模。同轴传输线的横截面如下图所示。其物理特性包括内导体半径 *a* 和外导体半径 *b*。

同轴传输线的横截面
