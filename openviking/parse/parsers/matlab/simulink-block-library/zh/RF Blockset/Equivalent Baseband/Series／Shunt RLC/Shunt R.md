---
type: simulink-block
title: 'Shunt R'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Series/Shunt RLC'
documentation_page: 'shuntr'
documentation_source_path: 'ref/shuntr.html'
language: zh-CN
chinese_source: worker-translation
---

# Shunt R

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Resistance (Ohms)
  summary: 分流元件的电阻 1（默认）| 标量
  group: 主
- name: Source of frequency data
  summary: 频率数据源 User-specified（默认）
  group: 可视化
- name: Frequency data (Hz)
  summary: 频率数据范围 [1:1.0e5:4e6]（默认）| 向量
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
  summary: 频率图 Freq（默认）
  group: 可视化
- name: X format
  summary: 频率图格式 Auto（默认）| Hz | kHz | MHz | GHz | THz
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

### **Resistance (Ohms)** — 分流元件的电阻 `1`（默认）| 标量

电阻的标量值。该值必须为非负。

### 可视化

### **Source of frequency data** — 频率数据源 `User-specified`（默认）

频率数据源，指定为 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1:1.0e5:4e6]`（默认）| 向量

频率数据范围，指定为以赫兹为单位的向量。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| 非负标量

参考阻抗，指定为以欧姆为单位的非负标量。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据进行可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 圆图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

根据您设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

| 绘图类型 | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor` 和 `NTemp`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y parameter2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

根据您设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

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

### **X parameter** — 频率图 `Freq`（默认）

频率图，指定为 `Freq`。

### **X format** — 频率图格式 `Auto`（默认）| `Hz` | `kHz` | `MHz` | `GHz` | `THz`

频率图格式，指定为以下之一。

|  |  |  |  |
| --- | --- | --- | --- |
| `Auto` | `Hz` | `kHz` | `MHz` |
| `GHz` | `THz` |  |  |

### **Y scale** — Y 轴刻度 `Linear`（默认）| `Log`

Y 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y
plane`。

### **X scale** — X 轴刻度 `Linear`（默认）| `Log`

X 轴刻度，指定为 `Linear` 或 `Log`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y
plane`。

### **Plot** — 绘制指定数据按钮

使用绘制按钮绘制指定的数据。
## 所属库

RF Blockset / Equivalent Baseband / Series / Shunt RLC

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

对并联电阻进行建模

Shunt R 模块根据其频率相关 S 参数，对模块对话框中描述的并联电阻进行建模。

并联 R 对象是一个二端口网络，如下图所示电路所示。

二端口并联 L 网络
