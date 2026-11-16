---
type: simulink-block
title: 'Shunt L'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Series/Shunt RLC'
documentation_page: 'shuntl'
documentation_source_path: 'ref/shuntl.html'
language: zh-CN
chinese_source: worker-translation
---

# Shunt L

## 端口

R2025b 中未记录。

## 参数

### 主要

### **电感 (H)** — 分流元件的电感 `1e-9`（默认） | scalar

电感的标量值。该值必须为非负。

### 可视化

### **频率数据源** — 频率数据源 `User-specified`（默认）

频率数据源，指定为 `User-specified`。

### **频率数据 (Hz)** — 频率数据范围 `[1:1.0e5:4e6]`（默认） | vector

频率数据范围，指定为以 Hz 为单位的向量。

### **参考阻抗 (ohms)** — 参考阻抗 `50`（默认） | nonnegative scalar

参考阻抗，指定为以 ohms 为单位的非负标量。

### **绘图类型** — 数据绘图类型 `X-Y plane`（默认） | `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据进行可视化的数据绘图类型，指定为下列之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅使用 Equivalent Baseband Library 模块创建绘图。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据范围。

### **Y 参数1** — 要绘制的参数类型 `S11`（默认） | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

要绘制的参数类型取决于你设置的 **绘图类型**，指定为下列之一。

| 绘图类型 | Y 参数1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor` 和 `NTemp`。 |
| `Composite data` | 没有要设置的 **Y 参数1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y 参数2** — 要绘制的参数类型 `S11`（默认） | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

要绘制的参数类型取决于你设置的 **绘图类型**，指定为下列之一。

| 绘图类型 | Y 参数2 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor` 和 `NTemp`。 |
| `Composite data` | 没有要设置的 **Y 参数2**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y 格式1** — 绘图格式 `Magnitude (decibels)`（默认） | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为下列之一。

| Y 参数1 | Y 格式1 |
| --- | --- |
| `S11`、`S12`、`S21` 和 `S22`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

#### 依赖关系

要启用 **Y 格式1**，请将 **绘图类型** 设置为 `X-Y plane`。

### **Y 格式2** — 绘图格式 `Magnitude (decibels)`（默认） | `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为下列之一。

| Y 参数2 | Y 格式2 |
| --- | --- |
| `S11`、`S12`、`S21` 和 `S22`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` | `None` |
| `NTemp` | `Kelvin` |

#### 依赖关系

要启用 **Y 格式2**，请将 **绘图类型** 设置为 `X-Y plane`。

### **X 参数** — 频率绘图 `Freq`（默认）

频率绘图，指定为 `Freq`。

### **X 格式** — 频率绘图格式 `Auto`（默认） | `Hz` | `kHz` | `MHz` | `GHz` | `THz`

频率绘图格式，指定为下列之一。

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

RF Blockset / Equivalent Baseband / Series / Shunt RLC

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2006a 之前引入**

## 描述

建立分流电感模型

Shunt L 模块根据其频率相关 S 参数，对模块对话框中描述的分流电感进行建模

shunt L 对象是一个二端口网络，如下图所示。

二端口 shunt L 网络
