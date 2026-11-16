---
type: simulink-block
title: 'Output Port'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Input/Output Ports'
documentation_page: 'outputport'
documentation_source_path: 'ref/outputport.html'
language: zh-CN
chinese_source: worker-translation
---

# Output Port

## 端口

在 R2025b 中未记录。

## 参数

### 主选项卡

### **Load impedance(ohms)** — 射频网络的负载阻抗 `50`（默认）| scalar

射频网络的负载阻抗，该网络在物理模型中描述并与其连接，指定为以 ohms 为单位的 scalar。

### 可视化选项卡

### **Source of frequency data** — 频率数据源 `Derived from Input Port parameter`（默认）| `User-specified`

频率数据源根据以下之一指定：

- 当 **Source of frequency data** 为 `Derived from Input Port parameter` 时，频率数据源将派生自 Input Port 上设置的参数。
- 当 **Source of frequency data** 为 `User-specified` 时，请在 **Frequency data** 参数中指定为频率 vector。

### **Frequency data (Hz)** — 频率数据范围 `1e9:1e8:3e9`（默认）| vector

频率数据范围，以 hertz 为单位指定为 vector。

#### 依赖关系

要启用此参数，请在 **Source of amplifier gain** 中设置 `User-specified`。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| scalar

同轴传输线的参考阻抗，以 ohms 为单位指定为 scalar。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用数据生成的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y scale** 和 **X scale**。
- `Composite data` — 复合数据图会在一图窗中自动生成四个单独的绘图，显示多个参数的频率依赖性。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z Smith chart`、`Y Smith chart` 和 `ZY Smith chart` — 生成数据的 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

基于您设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`, `S12`, `S21`, `S22`, `Gt`, `GroupDelay`, `GammaIn`, `GammaOut`, `VSWRIn`, `VSWROut`, `OIP3`, `NF`, `NFactor`, and `NTemp`. |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`, `S12`, `S21`, `S22`, `GammaIn`, and `GammaOut` |
| `Z Smith chart` | `S11`, `S22`, `GammaIn`, and `GammaOut`. |
| `Y Smith chart` | `S11`, `S22`, `GammaIn`, and `GammaOut`. |
| `ZY smith chart` | `S11`, `S22`, `GammaIn`, and `GammaOut`. |

### **Y parameter2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

基于您设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

| Plot type | Y parameter2 |
| --- | --- |
| `X-Y plane` | `S11`, `S12`, `S21`, `S22`, `Gt`, `GroupDelay`, `GammaIn`, `GammaOut`, `VSWRIn`, `VSWROut`, `OIP3`, `NF`, `NFactor`, and `NTemp`. |
| `Composite data` | 无需设置 **Y parameter2**。 |
| `Polar plane` | `S11`, `S12`, `S21`, `S22`, `GammaIn`, and `GammaOut` |
| `Z Smith chart` | `S11`, `S22`, `GammaIn`, and `GammaOut`. |
| `Y Smith chart` | `S11`, `S22`, `GammaIn`, and `GammaOut`. |
| `ZY smith chart` | `S11`, `S22`, `GammaIn`, and `GammaOut`. |

### **Y format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y prarameter1 | Y format1 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, and `GammaOut`. | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `VSWRIn`, `VSWROut`, and `Gt`. | `Magnitude (decibels)` and `None`. |
| `OIP3` | `dBm`, `dBW`, `W`, and `mW`. |
| `NF` | `Magnitude (decibels)`. |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

#### 依赖关系

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y prarameter2 | Y format2 |
| --- | --- |
| `S11`, `S12`, `S21`, `S22`, `GammaIn`, and `GammaOut`. | `dB`, `Magnitude (decibels)`, `Abs`, `Mag`, `Magnitude (linear)`, `Angle`, `Angle(degrees)`, `Angle(radians)`, `Real`, `Imag`, and `Imaginary`. |
| `GroupDelay` | `ns`, `us`, `ms`, `s`, and `ps`. |
| `VSWRIn`, `VSWROut`, and `Gt`. | `Magnitude (decibels)` and `None`. |
| `OIP3` | `dBm`, `dBW`, `W`, and `mW`. |
| `NF` | `Magnitude (decibels)`. |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

#### 依赖关系

要启用 **Y format2**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — X 参数 `Freq`（默认）

参数，指定为 `Freq`。此参数确定 X-Y plane 图上 x 轴的数据。

### **X format** — 绘图格式 `Hz`（默认）| `Auto` | `KHz` | `MHz` | `GHz` | `THz`

绘图格式，指定为以下之一：`Hz`、`Auto`、`KHz`、`MHz`、`GHz` 或 `THz`。

### **Y scale** — Y 轴刻度 `Linear`（默认）| `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

### **X scale** — X 轴刻度 `Linear`（默认）| `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

### **Plot** — 绘制指定数据按钮

使用 Plot 按钮绘制指定的数据。

**依赖关系**

如果您在执行以下一个或多个操作后显示 Output Port 掩码，则 **Visualization** 选项卡会显示用于创建绘图的参数：

- 运行一个模型，该模型在 Input Port 模块和 Output Port 模块之间有两个或更多模块。
- 单击 Update Diagram 按钮以初始化一个模型，该模型在 Input Port 模块和 Output Port 模块之间有两个或更多模块。

有关绘图的信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。

## 所属库

RF Blockset / Equivalent Baseband / Input / Output Ports

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

从 RF 物理模块到 Simulink 环境的连接模块

Output Port 模块产生输入信号经过一系列 RF 物理组件传输后的基带等效时域响应。Output Port 模块

1. 将 RF 物理组件划分为线性子系统和非线性子系统。
2. 提取线性子系统的复冲激响应，用于 RF 线性系统的基带等效建模。
3. 提取用于 RF 非线性的非线性 AMAM/AMPM 建模。

Output Port 模块还用作从模型的 RF 物理部分到模型的 Simulink®（或数学）部分的连接端口。有关 Output Port 模块如何将物理建模环境信号转换为数学 Simulink 信号的详细信息，请参阅 Convert to and from Simulink Signals。

**注意**

某些 RF 模块需要采样时间来执行基带建模计算。为确保这些计算的准确性，Input Port 模块以及数学 RF 模块会将输入采样时间与您在掩码中提供的采样时间进行比较。如果它们不匹配，或者由于模块未连接而导致输入采样时间缺失，则会出现错误消息。
