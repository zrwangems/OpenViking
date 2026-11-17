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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: S-Parameters
  summary: 双端口无源网络的 S 参数 [0,0;1,0]（默认）| 2×2×*M* 数组
  group: 主
- name: Frequency (Hz)
  summary: S 参数的频率 2.0e9（默认）| *M* 元素向量
  group: 主
- name: Reference Impedance (ohms)
  summary: 网络的参考阻抗 50（默认）| 非负标量 | 长度为 *M* 的向量
  group: 主
- name: Interpolation method
  summary: 插值网络参数的方法 Linear（默认）| Spline | Cubic
  group: 主
- name: Source of frequency data
  summary: 频率数据源 Same as the S-Parameters（默认）| User-specified
  group: 可视化
- name: Frequency data (Hz)
  summary: 频率数据范围 [1.9e9:1.0e6:2.2e9]（默认）| 向量
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

### **S-Parameters** — 双端口无源网络的 S 参数 `[0,0;1,0]`（默认）| 2×2×*M* 数组

双端口无源网络的 S 参数，指定为 2×2×*M* 数组，其中 *M* 是 S 参数的数量。

### **Frequency (Hz)** — S 参数的频率 `2.0e9`（默认）| *M* 元素向量

S 参数的频率，指定为 *M* 元素向量，每个元素单位为赫兹。所有频率必须为正。

### **Reference Impedance (ohms)** — 网络的参考阻抗 `50`（默认）| 非负标量 | 长度为 *M* 的向量

网络的参考阻抗，指定为以欧姆为单位的非负标量或长度为 *M* 的向量，每个元素单位为欧姆。此参数的值可以是实数或复数。如果提供标量值，则该值应用于所有频率。

### **Interpolation method** — 插值网络参数的方法 `Linear`（默认）| `Spline` | `Cubic`

用于插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### 可视化

### **Source of frequency data** — 频率数据源 `Same as the S-Parameters`（默认）| `User-specified`

频率数据源，指定为 `Same as the S-Parameters` 或 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1.9e9:1.0e6:2.2e9]`（默认）| 向量

频率数据范围，指定为向量，每个元素单位为赫兹。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| 非负标量

参考阻抗，指定为以欧姆为单位的非负标量。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

使用给定数据可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 圆图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

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

当 **Plot type** 选择为 `Composite data` 时，**Y parameter1** 被禁用。

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

当 **Plot type** 选择为 `Composite data` 时，**Y parameter2** 被禁用。

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

要启用 **Y format1**，请将 **Plot type** 设置为
`X-Y plane`。

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

要启用 **Y format2**，请将 **Plot type** 设置为
`X-Y plane`。

### **X parameter** — 频率绘图 `Freq`（默认）

频率绘图，指定为 `Freq`。

### **X format** — 频率绘图格式 `Hz`（默认）| `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率绘图格式，指定为以下之一。

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

使用 S 参数对无源网络建模

S-Parameters Passive Network 模块根据 S 参数以及 S 参数的频率和参考阻抗，对模块对话框中描述的双端口无源网络进行建模。

在模块对话框的 **S-Parameters** 字段中，将 *M* 个频率中每个频率的 S 参数提供为
2×2×*M* 数组。在 **Frequency** 字段中，
将 S 参数的频率指定为 *M* 元素向量。
向量元素必须与 S 参数的顺序相同。该图
显示了 S 参数数组与频率向量之间的对应关系。

S 参数数组与频率向量

S-Parameters Passive Network 模块对给定的
S 参数进行插值，以确定其在建模频率处的值。Output
Port 模块确定建模频率。有关更多详细信息，请参阅 Map Network Parameters to Modeling Frequencies。
