---
type: simulink-block
title: 'LC Bandpass Pi'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Ladder Filters'
documentation_page: 'lcbandpasspi'
documentation_source_path: 'ref/lcbandpasspi.html'
language: zh-CN
chinese_source: worker-translation
---

# LC Bandpass Pi

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Inductance (H)
  summary: LC Bandpass Pi 的电感 [1.4446e-9 4.3949e-8 1.4446e-9]（默认）| 向量
  group: 主
- name: Capacitance (F)
  summary: LC Bandpass Pi 的电容 [3.5785e-11 1.1762e-12 3.5785e-11]（默认）| 向量
  group: 主
- name: Source of frequency data
  summary: 频率数据源 User-specified（默认）
  group: 可视化
- name: Frequency data (Hz)
  summary: 频率数据范围 [500e6:4e6:900e6]（默认）| 向量
  group: 可视化
- name: Reference impedance (ohms)
  summary: 参考阻抗 50（默认）| 非负标量
  group: 可视化
- name: Plot type
  summary: 数据绘图类型 X-Y plane（默认）| Composite data | Polar plane | Z Smith chart | Y Smith chart | ZY Smith chart
  group: 可视化
- name: Y parameter1
  summary: 要绘制的参数类型 S11（默认）| S12 | S21 | S22 | GroupDelay | OIP3 | NF | ...
  group: 可视化
- name: Y parameter2
  summary: 要绘制的参数类型 S11（默认）| S12 | S21 | S22 | GroupDelay | OIP3 | NF | ...
  group: 可视化
- name: Y format1
  summary: 绘图格式 Magnitude (decibels)（默认）| Mag | Magnitude (linear) | Angle | Real | Imaginary | ...
  group: 可视化
- name: Y format2
  summary: 绘图格式 Magnitude (decibels)（默认）| Mag | Magnitude (linear) | Angle | Real | Imaginary | ...
  group: 可视化
- name: X parameter
  summary: 频率绘图 Freq（默认）
  group: 可视化
- name: X format
  summary: 频率绘图格式 Hz（默认）| Auto | kHz | MHz | GHz | THz
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

### 主

### **Inductance (H)** — LC Bandpass Pi 的电感 `[1.4446e-9 4.3949e-8 1.4446e-9]`（默认）| 向量

包含网络中所有电感器电感值的向量，按从源到负载的顺序排列。电感向量必须至少包含三个元素。所有值必须严格为正。

### **Capacitance (F)** — LC Bandpass Pi 的电容 `[3.5785e-11 1.1762e-12 3.5785e-11]`（默认）| 向量

包含网络中所有电容器电容值的向量，按从源到负载的顺序排列。其长度必须等于您在 **Inductance** 参数中提供的向量长度。所有值必须严格为正。

### 可视化

### **Source of frequency data** — 频率数据源 `User-specified`（默认）

频率数据源，指定为 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[500e6:4e6:900e6]`（默认）| 向量

频率数据范围，指定为以赫兹为单位的向量。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| 非负标量

参考阻抗，指定为以欧姆为单位的非负标量。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成史密斯®图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

基于您设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

| 绘图类型 | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor` 和 `NTemp`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y parameter2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

基于您设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

| 绘图类型 | Y parameter2 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor` 和 `NTemp`。 |
| `Composite data` | 无需设置 **Y parameter2**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

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

### **Y format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下选项之一。

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

### **X parameter** — 频率绘图 `Freq`（默认）

频率绘图，指定为 `Freq`。

### **X format** — 频率绘图格式 `Hz`（默认）| `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率绘图格式，指定为以下选项之一。

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

使用绘图按钮绘制指定的数据。
## 所属库

RF Blockset / Equivalent Baseband / Ladder Filters

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

对 LC 带通 pi 网络进行建模

LC Bandpass Pi 模块根据其频率相关 S 参数，对模块对话框中描述的 LC 带通 pi 网络进行建模。

对于网络中的每一对电感器和电容器，该模块首先在建模频率向量中包含的每个频率处计算 ABCD 参数。对于每个串联对，A = 1，B = *Z*，C = 0，D = 1，其中 *Z* 是串联对的阻抗。对于每个并联对，A = 1，B = 0，C = *Y*，D = 1，其中 *Y* 是并联对的导纳。

然后，LC Bandpass Pi 模块在每个建模频率处级联每个串联对和并联对的 ABCD 参数，并使用 RF Toolbox™ 的 `abcd2s` 函数将级联后的参数转换为 S 参数。

有关确定建模频率的信息，请参阅 Output Port 模块。

LC 带通 pi 网络对象是一个二端口网络，如下图所示。

二端口 LC 带通 pi 网络

[L1, L2, L3, L4, ...] 是 `'L'` 属性的值，[C1, C2, C3, C4, ...] 是 `'C'` 属性的值。
