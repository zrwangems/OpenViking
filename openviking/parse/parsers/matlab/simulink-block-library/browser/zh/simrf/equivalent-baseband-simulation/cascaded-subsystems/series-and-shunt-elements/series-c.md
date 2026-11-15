---
type: simulink-block
title: 'Series C'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband Simulation / Cascaded Subsystems / Series and Shunt Elements'
documentation_page: 'seriesc'
documentation_source_path: 'ref/seriesc.html'
language: zh-CN
chinese_source: worker-translation
---

# Series C

## 端口

未在 R2025b 中记录。

## 参数

### 主要

### **Capacitance (F)** — 串联元件的电容 `1e-12` (default) | scalar

电容的 scalar 值。该值必须为非负。

### 可视化

### **Source of frequency data** — 频率数据源 `User-specified` (default)

频率数据源，指定为 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1:1.0e5:4e6]` (default) | vector

频率数据范围，指定为以 hertz 为单位的 vector。

### **Reference impedance (ohms)** — 参考阻抗 `50` (default) | nonnegative scalar

参考阻抗，指定为以 ohms 为单位的非负 scalar。

### **Plot type** — 数据绘图类型 `X-Y plane` (default) | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据进行可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据相对于频率的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置
  **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。
  有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定
  频率相对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块
  仅绘制与指定频率相对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

要绘制的参数类型，基于所设置的 **Plot type**，指定为以下之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor` 和 `NTemp`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y parameter2** — 要绘制的参数类型 `S11` (default) | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

要绘制的参数类型，基于所设置的 **Plot type**，指定为以下之一。

| Plot type | Y parameter2 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor` 和 `NTemp`。 |
| `Composite data` | 无需设置 **Y parameter2**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y format1** — 绘图格式 `Magnitude (decibels)` (default) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`、`S12`、`S21` 和 `S22`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

#### 依赖关系

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)` (default) | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter2 | Y format2 |
| --- | --- |
| `S11`、`S12`、`S21` 和 `S22`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

#### 依赖关系

要启用 **Y format2**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — 频率绘图 `Freq` (default)

频率绘图，指定为 `Freq`。

### **X format** — 频率绘图格式 `Auto` (default) | `Hz` | `kHz` | `MHz` | `GHz` | `THz`

频率绘图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y scale** — Y 轴刻度 `Linear` (default) | `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **X scale** — X 轴刻度 `Linear` (default) | `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Plot** — 绘制指定数据按钮

使用绘图按钮绘制指定的数据。

## 所属库

RF Blockset / Equivalent Baseband / Series / Shunt RLC

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

对串联电容器建模

Series C 模块根据其频率相关 S 参数，对模块对话框中描述的串联电容器建模。

series C 对象是一个二端口网络，如下面的电路图所示。

二端口 series C 网络
