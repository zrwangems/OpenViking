---
type: simulink-block
title: 'General Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Amplifiers'
documentation_page: 'generalamplifier'
documentation_source_path: 'ref/generalamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# General Amplifier

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: 数据源
  summary: 描述放大器行为的数据源 Data file（默认）| RFDATA 对象
  group: 主
- name: 数据文件
  summary: 包含放大器数据的文件名 default.s2d（默认）| 字符串 | 字符向量
  group: 主
- name: RFDATA 对象
  summary: 包含放大器数据的 RF 数据对象 read(rfdata.data, 'default.amp')（默认）| rfdata.data 对象
  group: 主
- name: 插值方法
  summary: 插值网络参数的方法 Linear（默认）| Spline | Cubic
  group: 主
- name: 噪声类型
  summary: 噪声数据的类型 Noise figure（默认）| Spot noise data | Noise factor | Noise temperature
  group: 噪声数据
- name: 噪声系数 (dB)
  summary: 输入端的可用信噪比与输出端的可用信噪比之比 0（默认）| 标量比值 | 比值向量
  group: 噪声数据
- name: 最小噪声系数
  summary: 输入端的可用信噪比与输出端的可用信噪比之比的最小值 0（默认）| 标量比值 | 比值向量
  group: 噪声数据
- name: 最佳反射系数
  summary: 最佳源阻抗 1+0i（默认）| 复标量 | 复向量
  group: 噪声数据
- name: 等效归一化噪声电阻
  summary: 用于进行噪声测量的归一化电阻值 1（默认）| 正标量 | 正向量
  group: 噪声数据
- name: 噪声因子
  summary: 输入端的可用信噪功率与输出端的可用信噪功率之比 1（默认）| 标量比值 | 比值向量
  group: 噪声数据
- name: Noise temperature (K)
  summary: 产生与放大器相同噪声量的等效温度 0（默认）| 非负标量 | 非负向量
  group: 噪声数据
- name: Frequency (Hz)
  summary: 用于表示噪声数据的频率范围 2.0e9（默认）| 非负标量 | 非负向量
  group: 噪声数据
- name: IP3 type
  summary: 三阶截点的类型 OIP3（默认）| IIP3
  group: 非线性数据
- name: IP3 (dBm)
  summary: IP3 值 inf（默认）| 标量 | 向量
  group: 非线性数据
- name: 1dB gain compression power (dBm)
  summary: 增益下降 1 dB 时的输出功率值 inf（默认）| 标量 | 向量
  group: 非线性数据
- name: Output saturation power (dBm)
  summary: 放大器完全饱和时产生的输出功率值 inf（默认）| 标量 | 向量
  group: 非线性数据
- name: Gain compression at saturation (dB)
  summary: 增益值的下降量 3（默认）| 标量 | 向量
  group: 非线性数据
- name: Frequency (Hz)
  summary: 对应于三阶截点或功率数据的频率点 2.0e9（默认）| 正标量 | 正向量
  group: 非线性数据
- name: Source of frequency data
  summary: 频率数据源 Extracted from data source（默认）| User-specified
  group: 可视化
- name: Frequency data (Hz)
  summary: 频率数据范围 [1e9:1e8:2.9e9]（默认）| 向量
  group: 可视化
- name: Source of input power
  summary: 输入功率源 User-specified（默认）| Extracted from data source
  group: 可视化
- name: Input power data (dBm)
  summary: 输入功率数据范围 [0:19]（默认）| 向量
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
  summary: 频率绘图 Freq（默认）| AM
  group: 可视化
- name: X format
  summary: 频率绘图格式 Hz（默认）| Auto | kHz | MHz | GHz | THz | ...
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
- name: Bias
  summary: 放大器偏置 1.9（默认）| 标量
  group: 工作条件
```

### 主

### **数据源** — 描述放大器行为的数据源 `Data file`（默认）| `RFDATA` 对象

描述放大器行为的数据源，指定为 `Data file` 或 `RFDATA` 对象。

### **数据文件** — 包含放大器数据的文件名 `default.s2d`（默认）| 字符串 | 字符向量

包含放大器数据的文件名，指定为字符串或字符向量。文件名必须包含扩展名。如果文件不在您的 MATLAB® 路径中，请指定文件的完整路径，或点击 **浏览** 按钮查找文件。

#### 依赖关系

要启用此参数，请在 **数据源** 中选择 `Data file`。

### **RFDATA 对象** — 包含放大器数据的 RF 数据对象 `read(rfdata.data, 'default.amp')`（默认）| `rfdata.data` 对象

包含放大器数据的 RF 数据对象，指定为 RF Toolbox `rfdata.data` 对象、创建 `rfdata.data` 对象的 RF 工具箱命令，或生成此类对象的 MATLAB 表达式。

### **插值方法** — 插值网络参数的方法 `Linear`（默认）| `Spline` | `Cubic`

插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### 噪声数据

### **噪声类型** — 噪声数据的类型 `Noise figure`（默认）| `Spot noise data` | `Noise factor` | `Noise temperature`

噪声数据的类型，指定为以下之一：

- `Noise figure`
- `Spot noise data`
- `Noise factor`
- `Noise temperature`

如果数据源包含噪声数据，则此参数被禁用。

### **噪声系数 (dB)** — 输入端的可用信噪比与输出端的可用信噪比之比 `0`（默认）| 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比之比，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Noise figure`。

### **最小噪声系数** — 输入端的可用信噪比与输出端的可用信噪比之比的最小值 `0`（默认）| 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比之比的最小值，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Spot noise data`。

### **最佳反射系数** — 最佳源阻抗 `1+0i`（默认）| 复标量 | 复向量

最佳源阻抗，指定为复标量或复向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Spot noise data`。

### **等效归一化噪声电阻** — 用于进行噪声测量的归一化电阻值 `1`（默认）| 正标量 | 正向量

用于进行噪声测量的归一化电阻值，指定为正标量或正向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Spot noise data`。

### **噪声因子** — 输入端的可用信噪功率与输出端的可用信噪功率之比 `1`（默认）| 标量比值 | 比值向量

输入端的可用信噪功率与输出端的可用信噪功率之比，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Noise factor`。

### **Noise temperature (K)** — 产生与放大器相同噪声量的等效温度 `0`（默认）| 非负标量 | 非负向量

产生与放大器相同噪声量的等效温度，指定为以开尔文为单位的非负标量，或每个元素以开尔文为单位的非负向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise temperature`。

### **Frequency (Hz)** — 用于表示噪声数据的频率范围 `2.0e9`（默认）| 非负标量 | 非负向量

用于表示噪声数据的频率范围，指定为以赫兹为单位的非负标量，或每个元素以赫兹为单位的非负向量。如果为噪声数据提供标量值，模块将忽略 **Frequency (Hz)** 参数，并对所有频率使用相同的噪声数据。如果为噪声数据提供向量值，其大小必须与频率向量相同。模块使用 **Main** 选项卡中指定的 **Interpolation method** 对噪声数据进行插值。

### 非线性数据

### **IP3 type** — 三阶截点的类型 `OIP3`（默认）| `IIP3`

三阶截点的类型，指定为 `OIP3`（输出截点）或 `IIP3`（输入截点）。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **IP3 (dBm)** — IP3 值 `inf`（默认）| 标量 | 向量

IP3 值，对于频率无关的非线性数据指定为以 dBm 为单位的标量，对于频率相关的非线性数据指定为每个元素以 dBm 为单位的向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **1dB gain compression power (dBm)** — 增益下降 1 dB 时的输出功率值 `inf`（默认）| 标量 | 向量

增益下降 1 dB 时的输出功率值（P1dB,out），对于频率无关的非线性数据指定为以 dBm 为单位的标量，对于频率相关的非线性数据指定为每个元素以 dBm 为单位的向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **Output saturation power (dBm)** — 放大器完全饱和时产生的输出功率值 `inf`（默认）| 标量 | 向量

放大器完全饱和时产生的输出功率值（Psat,out），对于频率无关的非线性数据指定为以 dBm 为单位的标量，对于频率相关的非线性数据指定为每个元素以 dBm 为单位的向量。如果数据源包含输出饱和功率数据，则此参数被禁用。

### **Gain compression at saturation (dB)** — 增益值的下降量 `3`（默认）| 标量 | 向量

功率完全饱和时增益值的下降量（GCsat），对于频率无关的非线性数据指定为以 dB 为单位的标量，对于频率相关的非线性数据指定为每个元素以 dB 为单位的向量。

### **Frequency (Hz)** — 对应于三阶截点或功率数据的频率点 `2.0e9`（默认）| 正标量 | 正向量

对应于三阶截点或功率数据的频率点，指定为以赫兹为单位的正标量或正向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

#### 依赖关系

- 如果将频率指定为标量，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数必须全部为标量。
- 如果将频率指定为向量，则 **IP3 (dBm)**、**1 dB gain compression power (dBm)** 和 **Output saturation power (dBm)** 参数中的一个或多个也必须为向量。

### 可视化

### **Source of frequency data** — 频率数据源 `Extracted from data source`（默认）| `User-specified`

频率数据源，指定为 `Extracted from data source` 或 `User-specified`。

### **Frequency data (Hz)** — 频率数据范围 `[1e9:1e8:2.9e9]`（默认）| 向量

频率数据范围，指定为向量，每个元素的单位为赫兹。

#### 依赖

要启用此参数，请将 **Source of frequency data** 设置为
`User specified`。

### **Source of input power** — 输入功率源 `User-specified`（默认）| `Extracted from data source`

输入功率源，指定为 `Extracted from data
source` 或 `User-specified`。
如果数据源包含功率数据，则此参数被禁用。

### **Input power data (dBm)** — 输入功率数据范围 `[0:19]`（默认）| 向量

输入功率数据范围，指定为向量，每个元素的单位为 dBm。如果数据源包含功率数据，则此参数被禁用。

### **Reference impedance (ohms)** — 参考阻抗 `50`（默认）| 非负标量

参考阻抗，指定为非负标量，单位为欧姆。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认）| `Composite data` | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用给定数据进行可视化的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Composite data` — 绘制复合数据。
  有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith
  chart` 和 `ZY smith chart` —
  生成史密斯®圆图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

基于所设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

| 绘图类型 | Y parameter1 |
| --- | --- |
| `X-Y plane` | 对于 `X-Y plane` 数据绘图，**Y parameter1** 根据所选的 **Data source** 而变化。有关详细信息，请参阅 Parameters to plot in X-Y pane。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y parameter2** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `IIP3` | `NF` | ...

基于所设置的 **Plot type** 要绘制的参数类型，指定为以下之一。

| 绘图类型 | Y parameter2 |
| --- | --- |
| `X-Y plane` | 对于 `X-Y plane` 数据绘图，**Y parameter2** 根据所选的 **Data source** 而变化。有关详细信息，请参阅 Parameters to plot in X-Y pane。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`、`S12`、`S21`、`S22`、`GammaIn`、`GammaOut`、`GammaOPT`、`TF1`、`TF2`、`TF3`、`GammaMS`、`GammaML` 和 `Delta`。 | `dB`、`Magnitude (decibels)`、`Abs`、`Mag`、`Magnitude (linear)`、`Angle`、`Angle(degrees)`、`Angle(radians)`、`Real`、`Imag` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `AM/AM`、`VSWRIn` 和 `VSWROut`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |
| `Pout`、`OIP3` 和 `IIP3`。 | `dBm`、`dBW`、`W` 和 `mW`。 |
| `NF` | `dB` 和 `Magnitude (decibels)`。 |
| `RN`、`NFactor`、`K`、`Mu` 和 `MuPrime`。 | `None` |
| `NTemp` | `Kelvin` |
| `Fmin`、`Gt`、`Ga`、`Gp`、`Gmag` 和 `Gmsg`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |
| `Phase` 和 `AM/PM` | `Angle`、`Angle(degrees)` 和 `Angle(radians)`。 |

#### 依赖关系

要启用 **Y format1**，请将 **Plot
type** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Mag` | `Magnitude (linear)` | `Angle` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter2 | Y format2 |
| --- | --- |
| `S11`、`S12`、`S21`、`S22`、`GammaIn`、`GammaOut`、`GammaOPT`、`TF1`、`TF2`、`TF3`、`GammaMS`、`GammaML` 和 `Delta`。 | `dB`、`Magnitude (decibels)`、`Abs`、`Mag`、`Magnitude (linear)`、`Angle`、`Angle(degrees)`、`Angle(radians)`、`Real`、`Imag` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `AM/AM`、`VSWRIn` 和 `VSWROut`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |
| `Pout`、`OIP3` 和 `IIP3`。 | `dBm`、`dBW`、`W` 和 `mW`。 |
| `NF` | `dB` 和 `Magnitude (decibels)`。 |
| `RN`、`NFactor`、`K`、`Mu` 和 `MuPrime`。 | `None` |
| `NTemp` | `Kelvin` |
| `Fmin`、`Gt`、`Ga`、`Gp`、`Gmag` 和 `Gmsg`。 | `dB`、`Magnitude (decibels)` 和 `None`。 |
| `Phase` 和 `AM/PM` | `Angle`、`Angle(degrees)` 和 `Angle(radians)`。 |

#### 依赖关系

要启用 **Y format2**，请将 **Plot
type** 设置为 `X-Y plane`。

### **X parameter** — 频率绘图 `Freq`（默认）| `AM`

频率绘图，指定为 `Freq` 或
`AM`。

#### 依赖关系

要将 **X parameter** 设置为
`AM`，必须将 **Y
parameter1** 设置为 `AM/AM` 或
`AM/PM`。

### **X format** — 频率绘图格式 `Hz`（默认）| `Auto` | `kHz` | `MHz` | `GHz` | `THz` | ...

频率绘图格式，指定为以下之一。

| X parameter | X format |
| --- | --- |
| `Freq` | `Auto`、`Hz`、`kHz`、`MHz`、`GHz` 和 `THz`。 |
| `AM` | `Magnitude (decibels)`、`Magnitude (linear)`、`dB`、`Mag` 和 `None`。 |

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

### 工作条件

Agilent® P2D 和 S2D 文件为若干工作条件定义模块参数。工作条件是创建文件数据时使用的独立参数设置。默认情况下，RF Blockset™ Equivalent Baseband 软件使用与文件中首次出现的工作条件相对应的参数值来定义模块行为。要使用其他属性值，必须在 General Amplifier 模块对话框中选取不同的工作条件。

### **Bias** — 放大器偏置 `1.9`（默认）| 标量

放大器偏置，指定为以伏特为单位的标量。当 **Data file**
为 `default.s2p` 时，此参数设置为 `1.9` 伏特。
## 所属库

RF Blockset / Equivalent Baseband / Amplifiers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用对象或文件数据对非线性放大器进行建模

General Amplifier 模块对由数据源描述的非线性放大器进行建模。
数据源由 RF Toolbox™ 数据（`rfdata.data`）对象或来自文件的数据组成。
