---
type: simulink-block
title: 'Series L'
family: 'equivalent-baseband'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Series/Shunt RLC'
documentation_page: 'seriesl'
documentation_source_path: 'ref/seriesl.html'
language: zh-CN
chinese_source: worker-translation
---

# Series L

## 端口

R2025b 中未记录。

## 参数

### 主要

### **Inductance (H)** — Inductance of the series element `1e-9` (default) | scalar

电感的标量值。该值必须为非负值。

### 可视化

### **Source of frequency data** — Frequency data source `User-specified` (default)

频率数据源，指定为 `User-specified`。

### **Frequency data (Hz)** — Frequency data range `[1:1.0e5:4e6]` (default) | vector

频率数据范围，指定为以 hertz 为单位的向量。

### **Reference impedance (ohms)** — Reference impedance `50` (default) | nonnegative scalar

参考阻抗，指定为以 ohms 为单位的非负标量。

### **Plot type** — Type of data plot `X-Y plane` (default) | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据可视化的数据绘图类型，指定为以下项之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性图、半对数图或双对数图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 圆图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — Type of parameters to plot `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

要根据所设置的 **Plot type** 绘制的参数类型，指定为以下项之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor` 和 `NTemp`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y parameter2** — Type of parameters to plot `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

要根据所设置的 **Plot type** 绘制的参数类型，指定为以下项之一。

| Plot type | Y parameter2 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor` 和 `NTemp`。 |
| `Composite data` | 无需设置 **Y parameter2**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y format1** — Plot format `Magnitude (decibels)` (default) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下项之一。

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`、`S12`、`S21` 和 `S22`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

#### Dependencies

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — Plot format `Magnitude (decibels)` (default) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下项之一。

| Y parameter2 | Y format2 |
| --- | --- |
| `S11`、`S12`、`S21` 和 `S22`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

#### Dependencies

要启用 **Y format2**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — Frequency plot `Freq` (default)

频率绘图，指定为 `Freq`。

### **X format** — Frequency plot format `Auto` (default) | `Hz` | `kHz` | `MHz` | `GHz` | `THz`

频率绘图格式，指定为以下项之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y scale** — Y-axis scale `Linear` (default) | `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### Dependencies

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **X scale** — X-axis scale `Linear` (default) | `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### Dependencies

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Plot** — Plot specified data button

使用 Plot 按钮绘制指定数据。

## 所属库

RF Blockset / Equivalent Baseband / Series / Shunt RLC

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

对串联电感建模

Series L 模块根据其频率相关 S 参数对模块对话框中所描述的串联电感建模

series L 对象是一个二端口网络，如下图所示电路图。

二端口 series L 网络
