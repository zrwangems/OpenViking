---
type: simulink-block
title: 'S-Parameters'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'sparameters'
documentation_source_path: 'ref/sparameters.html'
language: zh-CN
chinese_source: worker-translation
---

# S-Parameters

## 端口

R2025b 中未记录。

## 参数

#### 主要

### **数据源** — 数据源 `Data file`（默认）| `Network-parameters` | `Rational model`

用于 S 参数行为的数据源，指定为以下之一：

- `Data file` — 扩展名为 `.s2p` 的 Touchstone 文件名。该模块忽略导入文件中的噪声和非线性数据。
- `Network-parameters` — 提供 **Network parameter** 数据，例如 `S-parameters`、`Y-parameters` 和 `Z-parameters`，并附带相应的 **Frequency** 和 **Reference impedance (ohms)** 用于 S 参数。
- `Rational model` — 为 **Residues**、**Poles** 和 **Direct feedthrough** 参数提供值，这些参数对应于有理模型的方程

  F(s)=(∑k=1nCks−Ak+D),s=j2πf

  。在此有理模型方程中，每个 *Ck* 是极点 *Ak* 的留数。如果 *Ck* 为复数，则还必须枚举相应的共轭复数极点和留数。此对象具有属性 `C`、`A` 和 `D`。您可以使用这些属性来指定 **Residues**、**Poles** 和 **Direct feedthrough** 参数。

### **数据文件** — 网络参数数据文件的名称 `simrfV2_unitygain.s2p`（默认）| 字符向量

网络参数数据文件的名称，指定为字符向量。

#### 依赖关系

要启用此参数，请在 **Data source** 选项卡中选择 `Data file`。

### **网络参数对象** — 作为数据源的网络参数对象 `off`（默认）| `on`

选择此参数以使用网络参数对象作为数据源来对 S 参数进行建模。

一旦选择此参数，在打开的文本框中，指定以下之一：

- 网络参数对象。
- MATLAB® 基础工作区变量或 Simulink® 模型工作区变量。该模块会评估指定的变量是否为网络参数对象。

当您选择此参数时，`sparameters('default.s2p')` 是默认的网络参数对象。

您可以指定的网络参数对象包括：

- `sparameters`
- `yparameters`
- `zparameters`
- `gparameters`
- `hparameters`
- `abcdparameters`
- `tparameters`

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Network-parameters`。

### **网络参数类型** — 网络参数类型 `S-parameters`（默认）| `Y-parameters` | `Z-parameters`

网络参数类型，指定为 `S-parameters`、`Y-parameters` 或 `Z-parameters`。

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Network-parameters`。

### **网络参数** — 网络参数值 `[0 0;1 0]`（默认）| 多维数组 | 标量

网络参数值，指定为多维数组或标量。当您将 **Network parameters** 指定为多维数组时，S 参数数组的第三维必须与 **Frequency (dB)** 参数中指定的频率向量长度相同。

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Network-parameters`。

### **频率 (dB)** — 网络参数的频率 `1e9 Hz`（默认）| 标量 | 向量 | `Hz` | `kHz` | `MHz` | `GHz`

网络参数的频率，以 Hz 为单位指定为标量或向量。

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Network-parameters`。

### **参考阻抗(Ohm)** — 网络参数的参考阻抗 `50`（默认）| 正标量 | 正标量向量

网络参数的参考阻抗，以欧姆为单位指定为正标量或正标量向量。

**注意**

当您将其指定为正标量向量时，所有端口的参考阻抗必须相等。

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Network-parameters`。

### **Use rational object** — 作为数据源的 rational 对象 `off`（默认）| `on`

选择此参数以使用 `rational` 对象作为数据源来对 S 参数进行建模。

选择此参数后，在打开的文本框中，指定以下之一：

- `rational` 对象。
- MATLAB 基础工作区变量或 Simulink 模型工作区变量。如果指定的变量是 rational 对象，该模块将对其进行求值。"

当您选择此参数时，`rational('default.s2p')` 是默认的 `rational` 对象。

您可以指定的 `rational` 对象包括：

- `rational`
- `rationalfit`
- `rfmodel.rational`

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Rational model`。

### **Residues** — 按有理模型顺序排列的留数 `0`（默认）| 向量

按有理模型顺序排列的留数，指定为向量。

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Rational model`。

### **Poles** — 按有理模型顺序排列的极点 `0`（默认）| 向量

按有理模型顺序排列的极点，指定为向量。

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Rational model`。

### **Direct feedthrough** — 直接馈通 `{0 0:1 0}`（默认）| 向量数组

直接馈通，指定为向量数组。

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Rational model`。

### **Simulate noise** — 模拟热噪声波 `off`（默认）| `on`

选择此参数以模拟热噪声波 [1]。有关详细信息，请参阅 Generate Thermal Noise。

S-Parameter 模块模拟最多 65 个端口的 S 参数网络的热噪声。*（自 R2023b 起）*

### **Ground and hide negative terminals** — 接地 RF 电路端子 `on`（默认）| `off`

选择此参数以将负极端子接地并隐藏。清除此参数以暴露负极端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。

#### 建模

### **Modeling options** — 对 S 参数建模 `Time domain`（默认）| `Frequency domain`

对 S 参数建模，指定为：

- `Time domain` 技术创建一个解析有理模型，近似整个数据范围。使用 `Time domain` 建模时，`Visualization` 选项卡中的 **Plot** 绘制 `Data Source` 中定义的数据以及 `rational` 函数中的值。
- `Frequency domain` 独立计算每个载波频率的基带冲激响应。此技术基于卷积。有一个选项可以指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。
- 对于 Amplifier、Antenna 和 S-parameters 模块，默认值为 `Time domain`。对于 Transmission Line 模块，默认值为 `Frequency domain`。

#### 依赖关系

要启用此参数，请将 **Data source** 设置为 `Data file` 或 `Network-parameters`。

### **Fitting options** — 有理拟合选项 `Fit individually`（默认）| `Share poles by column` | `Share all poles`

有理拟合选项，指定为 `Fit individually`、`Share poles by column` 或 `Share all poles`。

**Rational fitting results** 显示 **Number of independent fits**、**Number of required poles** 和 **Relative error achieved (dB)** 的值。

#### 依赖关系

要设置此参数，请在 **Modeling options** 中选择 `Time domain`。

### **Relative error desired (dB)** — 有理拟合可接受的相对误差 `-40`（默认）| 标量

有理拟合可接受的相对误差，指定为标量。

#### 依赖关系

要设置此参数，请在 **Modeling options** 中选择 `Time domain`。

### **Maximum number of poles** — 最大极点数 `48`（默认）| 正标量

用于控制拟合过程的最大极点数，指定为正标量。您最多可以指定 `99` 个极点。

#### 依赖关系

要设置此参数，请在**建模选项**中选择 `Time domain`。

### **Automatically estimate impulse response duration** — 自动计算冲激响应 `on` | `off`

选择此参数可自动计算冲激响应。
清除此参数可使用**冲激响应持续时间**手动指定冲激响应持续时间。

#### 依赖关系

要设置此参数，请在**建模选项**中选择 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `1e-10`（默认）| 标量

冲激响应持续时间，指定为标量。

#### 依赖关系

要设置此参数，请先在**建模选项**中选择 `Frequency domain`。然后，清除 `Automatically estimate impulse response duration`。

### **Use only S-parameter magnitude with appropriate delay** — 仅使用带适当延迟的 S 参数幅值 `off`（默认）| `on`

选择此参数可忽略 S 参数相位，并将冲激响应延迟其长度的一半。您可以使用此参数通过仅指定幅值来利用滤波器效果塑造频谱内容。

此参数使用原始数据的幅值来获取模块的冲激响应。此冲激响应以时间序列为中心，并添加冲激响应持续时间一半的固有延迟。在频域中，这转化为在整个给定频谱中相位呈线性单调递减。

**注意**

- 此参数仅适用于在频域中建模的 S 参数数据，并会向系统引入人为延迟。
- 向系统添加时间延迟（或频率相位变化）可能导致意外行为。例如，在非匹配系统中，延迟信号会被反弹回来并叠加到原始信号上。

#### 依赖关系

要启用此参数，请将**建模选项**设置为 `Frequency domain`。

#### 可视化

### **Source of frequency data** — 频率数据源 `Extracted from data source`（默认）| `User-defined`

频率数据源，指定为：

当**频率数据源**为 `Extracted from data source` 时，**数据源**必须设置为 `Data file`。验证指定的**数据文件**包含频率数据。

当**频率数据源**为 `User-specified` 时，在**频率数据**参数中指定频率向量。同时，从相应的下拉列表中指定单位。

### **Frequency data** — 频率数据范围 `[1e9:1e6:3e9]` Hz（默认）| 向量 | 标量

频率数据范围，指定为以 Hz、kHz、MHZ 或 GHz 为单位的向量或标量。当您想要可视化单一频率的 S 参数数据时，将**频率数据**指定为标量。

#### 依赖关系

要启用此参数，请将**频率数据源**设置为 `User-specified`。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认）| `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用您的数据生成的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建线性、半对数或双对数图，请相应地设置 **Y 轴刻度**和 **X 轴刻度**。
- `Polar plane` — 生成数据的极坐标图。模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 圆图。模块仅绘制与指定频率对应的数据范围。

### **Parameter 1** — 要绘制的 S 参数类型 `S11`（默认）| `SNN`

要绘制的 S 参数类型，指定为 `SNN`，其中 *N* 是 s 参数模块中的端口数。

### **Parameter 2** — 要绘制的 S 参数类型 `None`（默认）| `SNN`

要绘制的 S 参数类型，指定为 `SNN`，其中 *N* 是 s 参数模块中的端口数。

### **Format1** — 绘图格式 `Magnitude (decibels)`（默认）| `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (decibels)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

### **Format2** — 绘图格式 `Magnitude (decibels)`（默认）| `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (decibels)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

### **Y-axis scale** — Y 轴刻度 `Linear`（默认）| `Logarithmic`

Y 轴刻度，指定为 `Linear` 或 `Logarithmic`。

### **X-axis scale** — X 轴刻度 `Linear`（默认）| `Logarithmic`

X 轴刻度，指定为 `Linear` 或 `Logarithmic`。

### **Plot** — 绘制指定数据按钮

使用绘图按钮绘制指定数据。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2024b：`Time domain (rationalfit)` 参数已重命名

S-parameters 模块中 **Modeling options** 参数的 `Time domain (rationalfit)` 参数值已重命名为 `Time domain`。

当您打开在 R2024b 之前创建的包含 S-parameters 模块的模型时，参数名称显示为 `Time domain`。

### R2023b：在 S-parameters 模块中仿真噪声

从此版本开始，您可以使用 S-Parameters 模块中的 **Simulate noise** 参数来仿真具有八个以上端口的 S 参数网络的噪声。在更早的版本中，您可以使用该模块仿真最多八个端口的网络的噪声。

### R2022b：使用 Network parameter 和 rational 对象对 S 参数进行建模

通过将 **Data Source** 设置为 `Network parameters` 和 `Rational model`，可以使用在 MATLAB 命令行中创建的 network parameter 和 `rational` 对象作为数据源来对 S 参数进行建模。有关详细信息，请参阅 **Network-parameter object** 和 **Use rational object**。

### R2022b：可视化单频 S 参数数据

通过在 **Frequency data** 参数中指定单频 S 参数数据来可视化单频 S 参数数据。

### R2022b：模块参数已重命名

S-parameter 模块中的 **Frequency data** 参数已重命名为 **Source of frequency data**。

当您打开在 R2022b 之前创建的包含 S-parameter 模块的模型时，软件会将 **Frequency data** 参数替换为 **Source of frequency data** 参数。

### R2021b：在 S-parameter 模块中构建 S 参数网络数据

从 R2021b 开始，Circuit Envelope 库的 S-Parameters 模块使用 `rational` 函数对复数频率相关数据执行有理拟合。`rational` 对象提供了改进的拟合速度。该模块还有一个新参数 **Maximum number of poles**，用于对拟合过程提供额外控制。您最多可以指定 99 个极点。

当您打开在 R2021b 之前创建的包含 Circuit Envelope 库 S-parameter 模块的模型时，软件会更新提取方法，使用新的 **Maximum number of poles** 参数执行有理拟合。模型的输出会被重新拟合，重新拟合后的输出可能与之前版本的输出不同。

### R2021b：S-parameter 模块图标已更新

从 R2021b 开始，S-parametrs 模块图标已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 S-parametrs 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

对 S 参数网络进行建模

S-parameters 模块在 RF Blockset™ 电路包络仿真环境中对由 S 参数定义的网络进行建模。该器件最多可具有 65 个端口。有关 RF 仿真的介绍，请参阅示例 Simulate High Frequency Components。

该模块通过对指定数据拟合有理函数，在 RF Blockset 环境中对 S 参数数据进行建模。有关 S 参数有理拟合的更多信息，请参阅 RF Toolbox™ 的 `rational` 函数。

**注意**

在拟合过程中，该模块将 `rational` 对象的 `TendsToZero` 和 `Qlimit` 属性分别设置为 `false` 和 `inf`。

S-parameters 模块的掩码图标是动态的，用于指示所应用噪声参数的当前状态。下表展示了该模块上的图标如何根据模块上 **Simulate noise** 参数的状态而变化。

| Simulate noise: `on` | Simulate noise: `off` |
| --- | --- |
| Simulate noise 设置为 on 时的 S-parameters 模块图标。 | Simulate noise 设置为 off 时的 S-parameters 模块图标。 |

要在 Simulink 中对 RF 复基带 S 参数进行建模，请使用 Idealized Baseband S-parameters 模块。
