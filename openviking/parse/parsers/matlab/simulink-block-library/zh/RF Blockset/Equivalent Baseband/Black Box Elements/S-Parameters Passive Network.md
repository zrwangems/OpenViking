---
type: simulink-block
title: 'S-Parameters Passive Network'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Black Box Elements'
documentation_page: 'sparameterspassivenetwork'
documentation_source_path: 'ref/sparameterspassivenetwork.html'
language: zh-CN
chinese_source: worker-translation
---

# S-Parameters Passive Network

## 端口

在 R2025b 中未记录。

## 参数

### 主要

### **S-Parameters** — 二端口无源网络的 S 参数 `[0,0;1,0]` (默认) | 2×2×*M* 数组

二端口无源网络的 S 参数，指定为 2×2×*M* 数组，其中 *M* 是 S 参数的数量。

### **Frequency (Hz)** — S 参数的频率 `2.0e9` (默认) | *M* 元素向量

S 参数的频率，指定为 *M* 元素向量，其中每个元素的单位均为 hertz。所有频率必须为正。

### **Reference Impedance (ohms)** — 网络的参考阻抗 `50` (默认) | 非负标量 | 长度为 *M* 的向量

网络的参考阻抗，指定为以 ohms 为单位的非负标量，或长度为 *M* 且每个元素单位均为 ohms 的向量。此参数的值可以是实数或复数。如果提供标量值，则该值应用于所有频率。

### **Interpolation method** — 插值网络参数的方法 `Linear` (默认) | `Spline` | `Cubic`

插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### 可视化

### **Source of frequency data** — 频率数据源 `Same as the S-Parameters` (默认) | `User-specified`

频率数据源，指定为 `Same as the S-Parameters` 或 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1.9e9:1.0e6:2.2e9]` (默认) | 向量

频率数据范围，指定为一个向量，其中每个元素的单位均为 hertz。

### **Reference impedance (ohms)** — 参考阻抗 `50` (默认) | 非负标量

参考阻抗，指定为以 ohms 为单位的非负标量。

### **Plot type** — 数据绘图类型 `X-Y plane` (默认) | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性图、半对数图或双对数图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅使用 Equivalent Baseband Library 模块创建绘图。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11` (默认) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当将 **Plot type** 选择为 `Composite data` 时，**Y parameter1** 被禁用。

### **Y parameter2** — 要绘制的参数类型 `S11` (默认) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当将 **Plot type** 选择为 `Composite data` 时，**Y parameter2** 被禁用。

### **Y format1** — 绘图格式 `Magnitude (decibels)` (默认) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter1 | Y format1 |
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

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)` (默认) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter2 | Y format2 |
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

要启用 **Y format2**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — 频率绘图 `Freq` (默认)

频率绘图，指定为 `Freq`。

### **X format** — 频率绘图格式 `Hz` (默认) | `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率绘图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y scale** — Y 轴刻度 `Linear` (默认) | `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **X scale** — X 轴刻度 `Linear` (默认) | `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Plot** — 绘制指定数据按钮

使用 plot 按钮绘制指定数据。

## 所属库

RF Blockset / Equivalent Baseband / Black Box Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 S 参数对无源网络建模

S-Parameters Passive Network 模块根据其 S 参数以及这些 S 参数的频率和参考阻抗，对模块对话框中描述的二端口无源网络进行建模。

在模块对话框的 **S-Parameters** 字段中，为 *M* 个频率中的每一个频率提供 S 参数，形式为 2×2×*M* 数组。在 **Frequency** 字段中，将 S 参数的频率指定为 *M* 元素向量。该向量的元素顺序必须与 S 参数相同。该图显示了 S 参数数组与频率向量之间的对应关系。

S 参数数组与频率向量对比

S-Parameters Passive Network 模块对给定的 S 参数进行插值，以确定它们在建模频率处的值。Output Port 模块确定建模频率。有关详细信息，请参阅将网络参数映射到建模频率。
