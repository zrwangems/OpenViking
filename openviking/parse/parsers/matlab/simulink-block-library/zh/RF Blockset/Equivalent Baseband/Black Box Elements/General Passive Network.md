---
type: simulink-block
title: 'General Passive Network'
family: 'equivalent-baseband'
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

R2025b 中未记录。

## 参数

### 主

### **数据源** — 描述无源器件行为的数据源 `Data file`（默认） | `RFDATA` object

描述无源器件行为的数据源，指定为 `Data file` 或 `RFDATA` object。
数据源必须包含网络参数，并且还可以包含噪声数据、非线性数据，或两者。

### **数据文件** — 包含无源器件数据的文件名 `passive.s2p`（默认） | string | character vector

包含无源器件数据的文件名，指定为 string 或 character vector。文件名必须包含扩展名。
如果文件不在您的 MATLAB® 路径中，请指定该文件的完整路径，或点击 **浏览** 按钮查找该文件。

#### 依赖关系

要启用此参数，请在 **数据源** 中选择 `Data file`。

### **RFDATA 对象** — 包含无源器件数据的 RF 数据对象 `read(rfdata.data, 'passive.s2p')`（默认） | `rfdata.data` 对象

包含无源器件数据的 RF 数据对象，指定为 RF Toolbox `rfdata.data` 对象。您还可以使用诸如默认值之类的表达式，从 `.s2p` 文件创建 `rfdata.data` 对象。

### **插值方法** — 插值网络参数的方法 `Linear`（默认） | `Spline` | `Cubic`

插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### 可视化

### **频率数据源** — 频率数据源 `Extracted from data source`（默认） | `User-specified`

频率数据源，指定为 `Extracted from data source` 或 `User-specified`。

### **频率数据** — 频率数据范围 `[0.3e6:1e:6e9]`（默认） | 向量

频率数据范围，指定为向量，其中每个元素的单位为 hertz。

### **参考阻抗 (ohms)** — 参考阻抗 `50`（默认） | 非负标量

参考阻抗，指定为以 ohms 表示的非负标量。

### **绘图类型** — 数据绘图类型 `X-Y plane`（默认） | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性图、半对数图或双对数图，请相应地设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅使用等效基带库模块创建绘图。
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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y 参数1** 将被禁用。

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

当您将 **绘图类型** 选择为 `Composite data` 时，**Y 参数2** 将被禁用。

### **Y 格式1** — 绘图格式 `Magnitude (decibels)`（默认） | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y 参数1 | Y 格式1 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, `GammaOut`, `TF1`, `TF2`, `TF3`, `GammaMS`, `GammaML`, 和 `Delta`。 | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, 和 `Imaginary`。 |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, 和 `ps`。 |
| `VSWRIn` 和 `VSWROut`。 | `Magnitude (decibels)` 和 `None`。 |
| `OIP3` 和 `IIP3`。 | `dBm`, `W`, 和 `mW`。 |
| `NF` | `dB` 和 `Magnitude (decibels)`。 |
| `NFactor`, `K`, `Mu`, 和 `MuPrime`。 | `None` |
| `NTemp` | `Kelvin` |
| `Gt`, `Ga`, `Gp`, `Gmag`, 和 `Gmsg`。 | `dB`, `Magnitude (decibels)`, 和 `None`。 |

#### 依赖关系

要启用 **Y 格式1**，请将 **绘图类型** 设置为 `X-Y plane`。

### **Y 格式2** — 绘图格式 `Magnitude (decibels)`（默认） | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y 参数2 | Y 格式2 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, `GammaOut`, `TF1`, `TF2`, `TF3`, `GammaMS`, `GammaML`, 和 `Delta`。 | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, 和 `Imaginary`。 |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, 和 `ps`。 |
| `VSWRIn` 和 `VSWROut`。 | `Magnitude (decibels)` 和 `None`。 |
| `OIP3` 和 `IIP3`。 | `dBm`, `W`, 和 `mW`。 |
| `NF` | `dB` 和 `Magnitude (decibels)`。 |
| `NFactor`, `K`, `Mu`, 和 `MuPrime`。 | `None` |
| `NTemp` | `Kelvin` |
| `Gt`, `Ga`, `Gp`, `Gmag`, 和 `Gmsg`。 | `dB`, `Magnitude (decibels)`, 和 `None`。 |

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

RF Blockset / Equivalent Baseband / Black Box Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

对由 rfdata 对象描述的两端口无源网络进行建模

General Passive Network 模块对由 RF Toolbox™ 数据 (`rfdata.data`) 对象描述的两端口无源网络进行建模。

如果网络参数数据及其对应频率在 `rfdata.data` 对象中作为 S 参数存在，则 General Passive Network 模块会对 S 参数进行插值，以确定它们在建模频率处的值。如果该模块包含网络 Y 参数或 Z 参数，则该模块会先将它们转换为 S 参数。有关详细信息，请参阅将网络参数映射到建模频率。

要了解如何使用 General Passive Network 模块对两端口带通滤波器进行建模，请参阅指定或导入元器件数据示例的 *将数据文件导入 RF Blocks* 部分。
