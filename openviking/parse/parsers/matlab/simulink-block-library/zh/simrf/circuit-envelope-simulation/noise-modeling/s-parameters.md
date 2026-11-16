---
type: simulink-block
title: 'S-Parameters'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / Basic Components'
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

### **数据源** — 数据源 `Data file` (默认) | `Network-parameters` | `Rational model`

用于 S 参数行为的数据源，指定为以下之一：

- `Data file` — 扩展名为 `.s2p` 的 Touchstone 文件名。模块会忽略导入文件中的噪声和非线性数据。
- `Network-parameters` — 提供 **网络参数** 数据，例如 `S-parameters`、`Y-parameters` 和 `Z-parameters`，以及用于 S 参数的对应 **频率** 和 **参考阻抗 (ohms)**。
- `Rational model` — 为 **留数**、**极点** 和 **直接馈通** 参数提供值，这些参数对应于有理模型的方程

  F(s)=(∑k=1nCks−Ak+D),s=j2πf

  。在此有理模型方程中，每个 *Ck* 是极点 *Ak* 的留数。如果 *Ck* 为复数，则还必须列出对应的复共轭极点和留数。此对象具有属性 `C`、`A` 和 `D`。您可以使用这些属性来指定 **留数**、**极点** 和 **直接馈通** 参数。

### **数据文件** — 网络参数数据文件的名称 `simrfV2_unitygain.s2p` (默认) | character vector

网络参数数据文件的名称，指定为 character vector。

#### 依赖关系

要启用此参数，请在 **数据源** 选项卡中选择 `Data file`。

### **网络参数对象** — 作为数据源的网络参数对象 `off` (默认) | `on`

选择此参数以使用网络参数对象作为数据源来对 S 参数建模。

选择此参数后，在打开的文本框中指定以下之一：

- 网络参数对象。
- MATLAB® 基础工作区变量或 Simulink® 模型工作区变量。模块会评估指定的变量是否为网络参数对象。

`sparameters('default.s2p')` 是选择此参数时的默认网络参数对象。

可以指定的网络参数对象包括：

- `sparameters`
- `yparameters`
- `zparameters`
- `gparameters`
- `hparameters`
- `abcdparameters`
- `tparameters`

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Network-parameters`。

### **网络参数类型** — 网络参数类型 `S-parameters` (默认) | `Y-parameters` | `Z-parameters`

网络参数类型，指定为 `S-parameters`、`Y-parameters` 或 `Z-parameters`。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Network-parameters`。

### **网络参数** — 网络参数值 `[0 0;1 0]` (默认) | multidimensional array | scalar

网络参数值，指定为 multidimensional array 或 scalar。当您将 **网络参数** 指定为 multi-dimensional array 时，S 参数数组的第三维必须与 **频率 (dB)** 参数中指定的 frequencies vector 长度相同。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Network-parameters`。

### **频率 (dB)** — 网络参数的频率 `1e9 Hz` (默认) | scalar | vector | `Hz` | `kHz` | `MHz` | `GHz`

网络参数的频率，指定为 scalar 或 vector，单位为 Hz。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Network-parameters`。

### **参考阻抗 (Ohm)** — 网络参数的参考阻抗 `50` (默认) | positive scalar | vector of positive scalars

网络参数的参考阻抗，指定为 positive scalar 或 vector of positive scalars，单位为 ohms。

**注意**

当将其指定为 vector of positive scalars 时，所有端口的参考阻抗必须相等。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Network-parameters`。

### **使用 rational 对象** — 作为数据源的 rational 对象 `off` (默认) | `on`

选择此参数以使用 `rational` 对象作为数据源来对 S 参数建模。

选择此参数后，在打开的文本框中指定以下之一：

- `rational` 对象。
- MATLAB 基础工作区变量或 Simulink 模型工作区变量。模块会评估指定的变量是否为 rational 对象。"

`rational('default.s2p')` 是选择此参数时的默认 `rational` 对象。

可以指定的 `rational` 对象包括：

- `rational`
- `rationalfit`
- `rfmodel.rational`

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Rational model`。

### **留数** — 有理模型顺序中的留数 `0` (默认) | vector

有理模型顺序中的留数，指定为 vector。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Rational model`。

### **极点** — 有理模型顺序中的留数 `0` (默认) | vector

有理模型顺序中的极点，指定为 vector。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Rational model`。

### **直接馈通** — 直接馈通 `{0 0:1 0}` (默认) | array of vectors

直接馈通，指定为 array vector。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Rational model`。

### **仿真噪声** — 仿真热噪声波 `off` (默认) | `on`

选择此参数以仿真热噪声波 [1]。有关详细信息，请参阅 Generate Thermal Noise。

S-Parameters 模块可仿真最多 65 个端口的 S 参数网络的热噪声。*(自 R2023b 起)*

### **接地并隐藏负极端子** — 接地 RF 电路端子 `on` (默认) | `off`

选择此参数以接地并隐藏负极端子。清除此参数以显示负极端子。通过显示这些端子，您可以将它们连接到模型的其他部分。

#### 建模

### **建模选项** — 对 S 参数建模 `Time domain` (默认) | `Frequency domain`

对 S 参数建模，指定为：

- `Time domain` 技术会创建一个解析有理模型，以近似整个数据范围。使用 `Time domain` 建模时，`Visualization` 选项卡中的 **绘图** 会绘制 `Data Source` 中定义的数据以及 `rational` 函数中的值。
- `Frequency domain` 会针对每个载波频率独立计算基带冲激响应。此技术基于卷积。可以选择指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。
- 对于 Amplifier、Antenna 和 S-parameters 模块，默认值为 `Time domain`。对于 Transmission Line 模块，默认值为 `Frequency domain`。

#### 依赖关系

要启用此参数，请将 **数据源** 设置为 `Data file` 或 `Network-parameters`。

### **拟合选项** — 有理拟合选项 `Fit individually` (默认) | `Share poles by column` | `Share all poles`

有理拟合选项，指定为 `Fit individually`、`Share poles by column` 或 `Share all poles`。

**有理拟合结果** 会显示 **独立拟合数**、**所需极点数** 和 **达到的相对误差 (dB)** 的值。

#### 依赖关系

要设置此参数，请在 **建模选项** 中选择 `Time domain`。

### **期望相对误差 (dB)** — 有理拟合可接受的相对误差 `-40` (默认) | scalar

有理拟合可接受的相对误差，指定为 scalar。

#### 依赖关系

要设置此参数，请在 **建模选项** 中选择 `Time domain`。

### **最大极点数** — 最大极点数 `48` (默认) | positive scalar

用于控制拟合过程的最大极点数，指定为 positive scalar。您最多可以指定 `99` 个极点。

#### 依赖关系

要设置此参数，请在 **建模选项** 中选择 `Time domain`。

### **自动估计冲激响应持续时间** — 自动计算冲激响应 `on` | `off`

选择此参数以自动计算冲激响应。清除此参数以使用 **冲激响应持续时间** 手动指定冲激响应持续时间。

#### 依赖关系

要设置此参数，请在 **建模选项** 中选择 `Frequency domain`。

### **冲激响应持续时间** — 冲激响应持续时间 `1e-10` (默认) | scalar

冲激响应持续时间，指定为 scalar。

#### 依赖关系

要设置此参数，请先在 **建模选项** 中选择 `Frequency domain`。然后，清除 `Automatically estimate impulse response duration`。

### **仅使用具有适当延迟的 S 参数幅值** — 仅使用具有适当延迟的 S 参数幅值 `off` (默认) | `on`

选择此参数以忽略 S 参数相位，并将冲激响应延迟其长度的一半。您可以通过仅指定幅值，使用此参数来塑造具有滤波器效果的频谱内容。

此参数使用原始数据的幅值来获取模块的冲激响应。此冲激响应以时间序列为中心，并增加冲激响应持续时间一半的固有延迟。在频域中，这转换为在给定频谱范围内相位呈线性单调减小。

**注意**

- 此参数仅适用于在频域中建模的 S 参数数据，并会向系统引入人工延迟。
- 向系统添加时间延迟（或频率相位变化）可能会导致意外行为。例如，在未匹配系统中，延迟信号会被反弹并添加到原始信号中。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Frequency domain`。

#### 可视化

### **频率数据源** — 频率数据源 `Extracted from data source` (默认) | `User-defined`

频率数据源，指定为：

当 **频率数据源** 为 `Extracted from data source` 时，**数据源** 必须设置为 `Data file`。验证指定的 **数据文件** 包含频率数据。

当 **频率数据源** 为 `User-specified` 时，在 **频率数据** 参数中指定频率 vector。此外，从对应的下拉列表中指定单位。

### **频率数据** — 频率数据范围 `[1e9:1e6:3e9]` Hz (默认) | vector | scalar

频率数据范围，指定为 vector 或 scalar，单位为 Hz、kHz、MHZ 或 GHz。当您想要可视化单频 S 参数数据时，请将 **频率数据** 指定为 scalar。

#### 依赖关系

要启用此参数，请将 **频率数据源** 设置为 `User-specified`。

### **绘图类型** — 数据绘图类型 `X-Y plane` (默认) | `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

要使用数据生成的数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建 linear、semilog 或 log-log 图，请相应地设置 **Y 轴刻度** 和 **X 轴刻度**。
- `Polar plane` — 生成数据的极坐标图。模块仅绘制与指定频率对应的数据范围。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。模块仅绘制与指定频率对应的数据范围。

### **Parameter 1** — 要绘制的 S 参数类型 `S11` (默认) | `SNN`

要绘制的 S 参数类型，指定为 `SNN`，其中 *N* 是 S-Parameters 模块中的端口数。

### **Parameter 2** — 要绘制的 S 参数类型 `None` (默认) | `SNN`

要绘制的 S 参数类型，指定为 `SNN`，其中 *N* 是 S-Parameters 模块中的端口数。

### **Format1** — 绘图格式 `Magnitude (decibels)` (默认) | `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (decibels)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

### **Format2** — 绘图格式 `Magnitude (decibels)` (默认) | `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (decibels)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

### **Y 轴刻度** — Y 轴刻度 `Linear` (默认) | `Logarithmic`

Y 轴刻度，指定为 `Linear` 或 `Logarithmic`。

### **X 轴刻度** — X 轴刻度 `Linear` (默认) | `Logarithmic`

X 轴刻度，指定为 `Linear` 或 `Logarithmic`。

### **绘图** — 绘制指定数据按钮

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

**建模选项** 参数中的 `Time domain (rationalfit)` 参数值在 S-parameters 模块中已重命名为 `Time domain`。

当您打开在 R2024b 之前创建且包含 S-parameters 模块的模型时，参数名称显示为 `Time domain`。

### R2023b：在 S-parameters 模块中仿真噪声

从此版本开始，您可以使用 S-Parameters 模块中的 **仿真噪声** 参数来仿真具有八个以上端口的 S 参数网络的噪声。在早期版本中，您可以使用该模块仿真最多八个端口的网络噪声。

### R2022b：使用 Network parameter 和 rational 对象对 S 参数建模

通过将 **数据源** 设置为 `Network parameters` 和 `Rational model`，使用在 MATLAB 命令行中创建的网络参数对象和 `rational` 对象作为数据源来对 S 参数建模。有关详细信息，请参阅 **网络参数对象** 和 **使用 rational 对象**。

### R2022b：可视化单频 S 参数数据

通过在 **频率数据** 参数中指定单频 S 参数数据，可视化单频 S 参数数据。

### R2022b：模块参数已重命名

S-parameter 模块中的 **频率数据** 参数已重命名为 **频率数据源**。

当您打开在 R2022b 之前创建且包含 S-parameter 模块的模型时，软件会将 **频率数据** 参数替换为 **频率数据源** 参数。

### R2021b：在 S-parameter 模块中构造 S 参数网络数据

从 R2021b 开始，Circuit Envelope 库的 S-Parameters 模块使用 `rational` 函数对复数频率相关数据执行有理拟合。`rational` 对象提供改进的拟合速度。该模块还有一个新参数 **最大极点数**，用于提供对拟合过程的额外控制。您最多可以指定 99 个极点。

当您打开在 R2021b 之前创建且包含 Circuit Envelope 库 S-parameter 模块的模型时，软件会更新提取方法，以使用新的 **最大极点数** 参数执行有理拟合。模型的输出会被重新拟合，并且重新拟合后的输出可能不同于先前版本中的输出。

### R2021b：S-parameter 模块图标已更新

从 R2021b 开始，S-parametrs 模块图标已更新。模块图标现在为动态图标，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建且包含 S-parametrs 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

对 S 参数网络建模

S-parameters 模块对 RF Blockset™ 电路包络仿真环境中由 S 参数定义的网络进行建模。该器件最多可具有 65 个端口。有关 RF 仿真的介绍，请参阅示例 Simulate High Frequency Components。

该模块通过将有理函数拟合到指定数据，对 RF Blockset 环境中的 S 参数数据进行建模。有关 S 参数有理拟合的详细信息，请参阅 RF Toolbox™ `rational` 函数。

**注意**

在拟合过程中，该模块将 `rational` 对象的 `TendsToZero` 和 `Qlimit` 属性分别设置为 `false` 和 `inf`。

S-parameters 模块掩码图标是动态的，并指示所应用噪声参数的当前状态。此表显示了此模块上的图标如何基于模块上 **Simulate noise** 参数的状态而变化。

| Simulate noise: `on` | Simulate noise: `off` |
| --- | --- |
| S-parameters 模块图标，Simulate noise 设置为 on。 | S-parameters 模块图标，Simulate noise 设置为 off。 |

要在 Simulink 中对 RF 复基带 S 参数建模，请使用 Idealized Baseband S-parameters 模块。
