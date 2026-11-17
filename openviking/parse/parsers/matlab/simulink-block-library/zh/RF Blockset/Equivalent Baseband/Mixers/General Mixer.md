---
type: simulink-block
title: 'General Mixer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Equivalent Baseband / Mixers'
documentation_page: 'generalmixer'
documentation_source_path: 'ref/generalmixer.html'
language: zh-CN
chinese_source: worker-translation
---

# General Mixer

## 端口

R2025b 中未记录。

## 参数

### 主

### **数据源** — 描述混频器行为的数据源 `Data file`（默认）| `RFDATA` 对象

描述混频器行为的数据源，指定为 `Data file` 或 `RFDATA` 对象。

**数据类型：** `char`

### **数据文件** — 包含混频器数据的文件名 `default.s2d`（默认）| 字符串 | 字符向量

包含混频器数据的文件名，指定为字符串或字符向量。文件名必须包含扩展名。如果文件不在您的 MATLAB® 路径中，请指定文件的完整路径，或点击 **浏览** 按钮查找文件。

**注意**

如果数据文件包含交调表，General Mixer 模块会忽略该表。在运行仿真之前，请使用 RF Toolbox 软件确保级联在感兴趣的频带内没有显著的杂散。

#### 依赖关系

要启用此参数，请在 **数据源** 中选择 `Data file`。

**数据类型：** `char` | `string`

### **RFDATA 对象** — 包含混频器数据的 RF 数据对象 `read(rfdata.data, 'default.s2p')`（默认）| `rfdata.data` 对象

包含混频器数据的 RF 数据对象，指定为 RF Toolbox `rfdata.data` 对象、创建 `rfdata.data` 对象的 RF Toolbox 命令，或生成此类对象的 MATLAB 表达式。

### **插值方法** — 插值网络参数的方法 `Linear`（默认）| `Spline` | `Cubic`

插值网络参数的方法，指定为以下之一：

| 方法 | 描述 |
| --- | --- |
| `Linear` | 线性插值 |
| `Spline` | 三次样条插值 |
| `Cubic` | 分段三次 Hermite 插值 |

### **混频器类型** — 混频器类型 `Downconverter`（默认）| `Upconverter`

混频器类型，指定为 `Downconverter` 或 `Upconverter`。

### **本振频率 (Hz)** — 本地振荡器频率 `0.9e9`（默认）| *M* 元素向量

本地振荡器频率，指定为 *M* 元素向量，每个元素单位为赫兹。

- 如果您将 **混频器类型** 选择为 `Downconverter`，则模块集根据混频器输入频率 *fin* 和本地振荡器频率 *flo* 计算混频器输出频率 *fout*，公式为 *fout* = *fin* – *flo*。
- 如果您将 **混频器类型** 选择为 `Upconverter`，则 *fout* = *fin* + *flo*。

**注意**

对于下变频混频器，本地振荡器频率必须满足条件 *fin* – *flo* ≥ 1/(2*ts*)，其中 *ts* 是在 Input Port 模块中指定的采样时间。否则会出现错误。

### 噪声数据

### **相位噪声频率偏移 (Hz)** — 相位噪声频率偏移 `[0.1 1 10 100]*1e3`（默认）| 数值向量

相位噪声频率偏移，指定为以赫兹为单位的数值向量。

**数据类型：** `double`

### **相位噪声电平 (dBc/Hz)** — 相位噪声电平 `[-70 -120 -140 -150]`（默认）| 数值向量

相位噪声电平，指定为以相对于载波每赫兹分贝为单位的数值向量。

**数据类型：** `double`

### **噪声类型** — 噪声数据类型 `Noise figure`（默认）| `Spot noise data` | `Noise factor` | `Noise temperature`

噪声数据类型，指定为以下之一：

- `Noise figure`
- `Spot noise data`
- `Noise factor`
- `Noise temperature`

如果数据源包含噪声数据，则此参数被禁用。

### **噪声系数 (dB)** — 输入端的可用信噪比与输出端的可用信噪比之比 `0`（默认）| 标量比值 | 比值向量

输入端的可用信噪比与输出端的可用信噪比之比，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **噪声类型** 中选择 `Noise figure`。

### **Minimum noise figure** — 输入端可用信噪比与输出端可用信噪比的最小比值 `0`（默认）| 标量比值 | 比值向量

输入端可用信噪比与输出端可用信噪比的最小比值，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Optimal reflection coefficient** — 最佳源阻抗 `1+0i`（默认）| 复标量 | 复向量

最佳源阻抗，指定为复标量或复向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Equivalent normalized noise resistance** — 用于进行噪声测量的归一化电阻值 `1`（默认）| 正标量 | 正向量

用于进行噪声测量的归一化电阻值，指定为正标量或正向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Spot noise data`。

### **Noise factor** — 输入端可用信噪功率与输出端可用信噪功率的比值 `1`（默认）| 标量比值 | 比值向量

输入端可用信噪功率与输出端可用信噪功率的比值，指定为标量比值或比值向量。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise factor`。

### **Noise temperature (K)** — 与混频器产生相同噪声量的等效温度 `0`（默认）| 非负标量 | 非负向量

与混频器产生相同噪声量的等效温度，指定为非负标量或非负向量，单位为开尔文。

#### 依赖关系

要启用此参数，请在 **Noise type** 中选择 `Noise temperature`。

### **Frequency (Hz)** — 用于表示噪声数据的频率范围 `2.0e9`（默认）| 非负标量 | 非负向量

用于表示噪声数据的频率范围，指定为非负标量（单位为赫兹）或非负向量（每个元素的单位为赫兹）。如果为噪声数据提供标量值，该模块将忽略 **Frequency (Hz)** 参数，并对所有频率使用相同的噪声数据。如果为噪声数据提供向量值，其大小必须与频率向量相同。该模块使用 **Main** 选项卡中指定的 **Interpolation method** 对噪声数据进行插值。

### Nonlinearity Data

### **IP3 type** — 三阶截点的类型 `OIP3`（默认）| `IIP3`

三阶截点的类型，指定为 `OIP3`（输出截点）或 `IIP3`（输入截点）。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **IP3 (dBm)** — IP3 值 `inf`（默认）| 标量 | 向量

IP3 值，对于频率无关的非线性数据指定为以 dBm 为单位的标量，对于频率相关的非线性数据指定为每个元素以 dBm 为单位的向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **1dB gain compression power (dBm)** — 增益下降 1 dB 时的输出功率值 `inf`（默认）| 标量 | 向量

增益下降 1 dB 时的输出功率值（P1dB,out），对于频率无关的非线性数据指定为以 dBm 为单位的标量，对于频率相关的非线性数据指定为每个元素以 dBm 为单位的向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

### **输出饱和功率 (dBm)** — 混频器完全饱和时产生的输出功率值 `inf`（默认）| 标量 | 向量

混频器完全饱和时产生的输出功率值（Psat,out），对于频率无关的非线性数据，指定为以 dBm 为单位的标量；对于频率相关的非线性数据，指定为每个元素以 dBm 为单位的向量。如果数据源包含输出饱和功率数据，则此参数被禁用。

### **饱和时的增益压缩 (dB)** — 增益值的减少量 `3`（默认）| 标量 | 向量

功率完全饱和时增益值的减少量（GCsat），对于频率无关的非线性数据，指定为以 dB 为单位的标量；对于频率相关的非线性数据，指定为每个元素以 dB 为单位的向量。

### **频率 (Hz)** — 对应于三阶截点或功率数据的频率点 `2.0e9`（默认）| 正标量 | 正向量

对应于三阶截点或功率数据的频率点，指定为以赫兹为单位的正标量或正向量。如果数据源包含功率数据或 IP3 数据，则此参数被禁用。

#### 依赖关系

- 如果将频率指定为标量，则 **IP3 (dBm)**、**1 dB 增益压缩功率 (dBm)** 和 **输出饱和功率 (dBm)** 参数必须全部为标量。
- 如果将频率指定为向量，则 **IP3 (dBm)**、**1 dB 增益压缩功率 (dBm)** 和 **输出饱和功率 (dBm)** 参数中的一个或多个也必须为向量。

### 可视化

### **频率数据源** — 频率数据来源 `从数据源提取`（默认）| `用户指定`

频率数据来源，指定为 `从数据源提取` 或 `用户指定`。

### **频率数据 (Hz)** — 频率数据范围 `[1e9:1e8:2.9e9]`（默认）| 向量

频率数据范围，指定为每个元素以赫兹为单位的向量。

#### 依赖关系

要启用此参数，请将 **频率数据源** 设置为 `用户指定`。

### **输入功率数据源** — 输入功率数据来源 `从数据源提取`（默认）

输入功率数据来源，指定为 `从数据源提取`。

### **输入功率数据 (dBm)** — 输入功率数据 `[0:19]`（默认）| 向量

输入功率数据，指定为每个元素以 dBm 为单位的向量。

### **参考阻抗 (欧姆)** — 参考阻抗 `50`（默认）| 非负标量

参考阻抗，指定为以欧姆为单位的非负标量。

### **绘图类型** — 数据绘图类型 `X-Y 平面`（默认）| `复合数据` | `极坐标平面` | `Z 史密斯圆图` | `Y 史密斯圆图` | `ZY 史密斯圆图`

使用给定数据进行可视化的数据绘图类型，指定为以下之一：

- `X-Y 平面` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y 轴刻度** 和 **X 轴刻度**。
- `复合数据` — 绘制复合数据。有关详细信息，请参阅 Create Plots Using Equivalent Baseband Library Blocks。
- `极坐标平面` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据范围。
- `Z 史密斯圆图`、`Y 史密斯圆图` 和 `ZY 史密斯圆图` — 生成史密斯圆图。该模块仅绘制与指定频率对应的数据范围。

### **Y parameter1** — 要绘制的参数类型 `S11`（默认）| `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

要绘制的参数类型，基于您设置的 **Plot type**，指定为以下之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor`、`NTemp`、`Fmin`、`GaammaOPT`、`RN` 和 `PhaseNoise`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y parameter2** — 要绘制的参数类型 `S11` | `S12` | `S21` | `S22` | `GroupDelay` | `OIP3` | `NF` | ...

要绘制的参数类型，基于您设置的 **Plot type**，指定为以下之一。

| Plot type | Y parameter1 |
| --- | --- |
| `X-Y plane` | `S11`、`S12`、`S21`、`S22`、`GroupDelay`、`OIP3`、`NF`、`NFactor`、`NTemp`、`Fmin`、`GaammaOPT`、`RN` 和 `PhaseNoise`。 |
| `Composite data` | 无需设置 **Y parameter1**。 |
| `Polar plane` | `S11`、`S12`、`S21` 和 `S22` |
| `Z Smith chart` | `S11` 和 `S22`。 |
| `Y Smith chart` | `S11` 和 `S22`。 |
| `ZY smith chart` | `S11` 和 `S22`。 |

### **Y format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Magnitude (linear)` | `Angle(degrees)` | `Angle(radians)` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter1 | Y format1 |
| --- | --- |
| `S11`、`S12`、`S21`、`S22` 和 `GaammaOPT`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` 和 `RN`。 | `None` |
| `NTemp` | `Kelvin` |
| `Fmin` | `None` 和 `Magnitude (decibels)` |
| `PhaseNoise` | `dBc/Hz` |

#### 依赖关系

要启用 **Y format1**，请将 **Plot type** 设置为 `X-Y plane`。

### **Y format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Magnitude (linear)` | `Angle(degrees)` | `Angle(radians)` | `Real` | `Imaginary` | ...

绘图格式，指定为以下之一。

| Y parameter2 | Y format2 |
| --- | --- |
| `S11`、`S12`、`S21`、`S22` 和 `GaammaOPT`。 | `Magnitude (decibels)`、`Magnitude (linear)`、`Angle(degrees)`、`Angle(radians)`、`Real` 和 `Imaginary`。 |
| `GroupDelay` | `ns`、`us`、`ms`、`s` 和 `ps`。 |
| `OIP3` | `dB`、`dBm`、`W` 和 `mW`。 |
| `NF` | `Magnitude (decibels)` |
| `NFactor` 和 `RN`。 | `None` |
| `NTemp` | `Kelvin` |
| `Fmin` | `None` 和 `Magnitude (decibels)` |
| `PhaseNoise` | `dBc/Hz` |

#### 依赖关系

要启用 **Y format2**，请将 **Plot type** 设置为 `X-Y plane`。

### **X parameter** — 频率图 `Freq`（默认）

频率图，指定为 `Freq`。

### **X format** — 频率图格式 `Hz`（默认）| `Auto` | `kHz` | `MHz` | `GHz` | `THz`

频率图格式，指定为以下之一。

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

使用绘制按钮绘制指定数据。

### 工作条件

Agilent® P2D 和 S2D 文件为若干工作条件定义了模块参数。工作条件是创建文件数据时使用的独立参数设置。默认情况下，模块集使用与文件中首先出现的工作条件相对应的参数值来定义模块行为。要使用其他属性值，必须在 General Mixer 模块对话框中选取不同的工作条件。

## 所属库

RF Blockset / Equivalent Baseband / Mixers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

对由 rfdata 对象描述的混频器和本振进行建模

General Mixer 模块对由 RF Toolbox™ 数据（`rfdata.data`）对象描述的混频器进行建模。
