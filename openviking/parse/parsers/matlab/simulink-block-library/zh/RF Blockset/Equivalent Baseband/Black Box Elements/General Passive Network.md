---
type: simulink-block
title: 'General Passive Network'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Black Box Elements'
documentation_page: 'generalpassivenetwork'
documentation_source_path: 'ref/generalpassivenetwork.html'
language: zh-CN
chinese_source: worker-translation
---

# General Passive Network

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: 数据源
  summary: 描述无源器件行为的数据源 Data file（默认）| RFDATA 对象
  group: 主要
- name: 数据文件
  summary: 包含无源器件数据的文件名 passive.s2p（默认）| 字符串 | 字符向量
  group: 主要
- name: RFDATA 对象
  summary: 包含无源器件数据的 RF 数据对象 read(rfdata.data, 'passive.s2p')（默认）| rfdata.data 对象
  group: 主要
- name: 插值方法
  summary: 插值网络参数的方法 Linear（默认）| Spline | Cubic
  group: 主要
- name: 频率数据源
  summary: 频率数据源 Extracted from data source（默认）| User-specified
  group: 可视化
- name: 频率数据
  summary: 频率数据范围 [0.3e6:1e:6e9]（默认）| 向量
  group: 可视化
- name: 参考阻抗（欧姆）
  summary: 参考阻抗 50（默认）| 非负标量
  group: 可视化
- name: 绘图类型
  summary: 数据绘图类型 X-Y plane（默认）| Composite data | Polar plane | Z Smith chart | Y Smith chart | ZY Smith chart
  group: 可视化
- name: Y 参数1
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
  summary: 频率图 Freq（默认）
  group: 可视化
- name: X format
  summary: 频率图格式 Hz（默认）| Auto | kHz | MHz | GHz | THz
  group: 可视化
- name: Y scale
  summary: Y 轴刻度 Linear（默认）| Log
  group: 可视化
- name: X scale
  summary: X 轴刻度 Linear（默认）| Log
  group: 可视化
- name: Plot
  summary: 绘制指定数据按钮
  group: 可视化
```

### 主要

### **数据源** — 描述无源器件行为的数据源 `Data file`（默认）| `RFDATA` 对象

描述无源器件行为的数据源，指定为 `Data file` 或 `RFDATA` 对象。数据源必须包含网络参数，还可以包含噪声数据、非线性数据或两者。

### **数据文件** — 包含无源器件数据的文件名 `passive.s2p`（默认）| 字符串 | 字符向量

包含无源器件数据的文件名，指定为字符串或字符向量。文件名必须包含扩展名。如果文件不在您的 MATLAB® 路径中，请指定文件的完整路径，或点击 **Browse** 按钮查找文件。

#### 依赖

要启用此参数，请在 **数据源** 中选择 `Data file`。

### **RFDATA 对象** — 包含无源器件数据的 RF 数据对象 `read(rfdata.data, 'passive.s2p')`（默认）| `rfdata.data` 对象

包含无源器件数据的 RF 数据对象，指定为 RF Toolbox `rfdata.data` 对象。您也可以使用诸如默认值之类的表达式从 `.s2p` 文件创建 `rfdata.data` 对象。

### **插值方法** — 插值网络参数的方法 `Linear`（默认）| `Spline` | `Cubic`

插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### 可视化

### **频率数据源** — 频率数据源 `Extracted from data source`（默认）| `User-specified`

频率数据源，指定为 `Extracted from data source` 或 `User-specified`。

### **频率数据** — 频率数据范围 `[0.3e6:1e:6e9]`（默认）| 向量

频率数据范围，指定为向量，每个元素单位为赫兹。

### **参考阻抗（欧姆）** — 参考阻抗 `50`（默认）| 非负标量

参考阻抗，指定为非负标量，单位为欧姆。

### **绘图类型** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成史密斯®图。该模块仅绘制与指定频率对应的数据范围。

### **Y 参数1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y 参数1** 被禁用。

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

当您将 **Plot type** 选择为 `Composite data` 时，**Y parameter2** 被禁用。

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

### **Plot** — 绘制指定数据按钮

使用绘图按钮绘制指定数据。
## 所属库

RF Blockset / Equivalent Baseband / Black Box Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

对由 rfdata 对象描述的双端口无源网络进行建模

通用无源网络模块对由 RF Toolbox™ 数据（`rfdata.data`）对象描述的双端口无源网络进行建模。

如果网络参数数据及其对应频率在 `rfdata.data` 对象中以 S 参数形式存在，则通用无源网络模块会对 S 参数进行插值，以确定它们在建模频率处的值。如果该模块包含网络 Y 参数或 Z 参数，则该模块首先将它们转换为 S 参数。有关更多详细信息，请参阅将网络参数映射到建模频率。

要了解如何使用通用无源网络模块对双端口带通滤波器进行建模，请参阅指定或导入元件数据示例中的*将数据文件导入 RF 模块*部分。
