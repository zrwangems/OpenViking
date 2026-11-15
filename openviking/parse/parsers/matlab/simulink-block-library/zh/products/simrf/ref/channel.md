---
type: simulink-block
title: 'Channel'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Systems'
documentation_page: 'channel'
documentation_source_path: 'ref/channel.html'
language: zh-CN
chinese_source: worker-translation
---

# Channel

## 端口

在 R2025b 中未记录。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Source of channel model** — 信道源 `Isotropic free-space`（默认）| `Ray-tracing`

信道源，指定为以下选项之一：

- `Isotropic free-space` — 该模块对电磁辐射从发射点穿过自由空间传播时的行为进行建模。自由空间传播模型没有强制频率范围，假设视距（LOS）条件，并忽略地形、地球曲率和其他障碍物。更多信息，请参阅 `FreeSpace`（Antenna Toolbox）。
- `Ray-tracing` — 该模块使用三维环境几何对传播路径建模。更多信息，请参阅 `RayTracing`（Antenna Toolbox）。

  **注意**

  要指定 `Ray-tracing` 选项，您必须具有 Antenna Toolbox™ 许可证。

#### TX 天线

### **Antenna gain** — 发射天线增益 `0 dBi`（默认）| 实数标量或向量 | 正标量或向量

发射天线的增益，指定为实数标量或向量，或正标量或向量。

- 如果指定实数标量或向量，则将 **Antenna gain** 参数单位设置为 `dBi`。
- 如果指定正标量或向量，则将 **Antenna gain** 参数单位设置为 `None`。
- 如果指定向量，则该向量必须与 **Carrier frequencies** 参数中的向量长度相同。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

### **Impedance (Ohm)** — 发射天线的输入阻抗 `50`（默认）| 复标量或向量

发射天线的输入阻抗，指定为复标量或向量，单位为 ohms。该向量必须与您在 **Carrier frequencies** 参数中指定的向量长度相同。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

**数据类型：** `double`
**复数支持：** Yes

#### RX 天线

### **Antenna gain** — 接收天线增益 `0 dBi`（默认）| 实数标量或向量 | 正标量或向量

接收天线的增益，指定为实数标量或向量，或正标量或向量。

- 如果指定实数标量或向量，则将 **Antenna gain** 参数单位设置为 `dBi`。
- 如果指定正标量或向量，则将 **Antenna gain** 参数单位设置为 `None`。
- 如果指定向量，则该向量必须与 **Carrier frequencies** 参数中的向量长度相同。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

### **Impedance (Ohm)** — 接收天线的输入阻抗 `50`（默认）| 复标量或向量

接收天线的输入阻抗，指定为复标量或向量，单位为 ohms。该向量必须与您在 **Carrier frequencies** 参数中指定的向量长度相同。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

**数据类型：** `double`
**复数支持：** Yes

#### 介质

### **Path loss** — 自由空间路径损耗 `10 dB`（默认）| 实数标量或向量 | 正标量或向量

自由空间路径损耗，指定为实数标量或向量，或正标量或向量。

- 如果指定实数标量或向量，则将 **Antenna gain** 参数单位设置为 `dB`。
- 如果指定正标量或向量，则将 **Antenna gain** 参数单位设置为 `None`。
- 如果指定向量，则该向量必须与 **Carrier frequencies** 参数中的向量长度相同。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

### **Path delay** — 自由空间路径延迟 `0 s`（默认）| 非负标量

自由空间路径延迟，指定为非负标量，单位为 seconds、milliseconds、microseconds 或 nanoseconds。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

#### 射线追踪

### **Map** — 用于可视化或表面数据的 Map `"none"`（默认）| `siteviewer` 对象 | `triangulation` 对象 | 字符串标量 | 字符向量

用于可视化或表面数据的 Map，指定为 `siteviewer` 对象、`triangulation` 对象、字符串标量或字符向量。有效的和默认的 Map 值取决于坐标系，如传播模型中所指定。

| 坐标系 | 有效的 Map 值 |
| --- | --- |
| `"geographic"` | - 一个 `siteviewer`（Antenna Toolbox）对象a。 - 地形名称，如果函数在调用时带有输出参数。   有效的地形名称为 `"none"`、   `"gmted2010"`，或您使用 `addCustomTerrain`（Antenna Toolbox）创建的自定义地形名称。 |
| `"cartesian"` | - `"none"`。 - 一个 `siteviewer` 对象。 - 一个 STL 文件的名称。 - 一个 `triangulation` 对象。 |
| a 边界和区域标签的对齐是数据供应商提供的功能的一种呈现，并不表示 MathWorks® 的认可。 | |

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

**数据类型：** `char` | `string`

### **Propagation model** — 传播模型 `'raytracing'`（默认）| `RayTracing` 对象

传播模型，指定为 `'raytracing'` 或 `RayTracing`（Antenna Toolbox）对象。默认值为 `'raytracing'`，它使用 SBR 方法，查找最多具有两次反射和零次绕射的路径，并丢弃比最强路径弱 40 dB 以上的路径。

您可以使用 `propagationModel`（Antenna Toolbox）函数创建 `RayTracing`（Antenna Toolbox）对象。`RayTracing` 对象使您能够指定属性，例如射线追踪方法、最大反射和绕射次数、路径损耗阈值以及建筑和地形材料。

有关射线追踪方法之间差异的信息，请参阅 Choose a Propagation Model（Antenna Toolbox）。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

**数据类型：** `char` | `string`

### **Tx site** — 发射站点 `txsite` 对象 | `txsite` 对象数组

发射站点，指定为 `txsite`（Antenna Toolbox）对象或 `txsite` 对象数组。如果指定数组，则组成该数组的 `txsite` 对象除 `TransmitterFrequency` 属性外必须相同。

**注意**

- 在模块中使用您要在 **Tx site** 中指定的天线、阵列或 PCB 叠层对象之前，请至少针对一个频率对其进行分析。
- 将 `txsite` 对象的 `Antenna` 属性指定为 Antenna Catalog（Antenna Toolbox）中的天线单元，或 Array Catalog（Antenna Toolbox）中的阵列单元。更多信息，请参阅 `txsite`（Antenna Toolbox）。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

### **Rx site** — 接收站点 `rxsite` 对象

接收站点，指定为 `rxsite`（Antenna Toolbox）对象。

**注意**

- 在模块中使用您要在 **Rx site** 中指定的天线、阵列或 PCB 叠层对象之前，请至少针对一个频率对其进行分析。
- 将 `rxsite` 对象的 `Antenna` 属性指定为 Antenna Catalog（Antenna Toolbox）中的天线单元，或 Array Catalog（Antenna Toolbox）中的阵列单元。更多信息，请参阅 `rxsite`（Antenna Toolbox）。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

### **View Site** — 显示 RF 传播场景按钮

单击此按钮可显示发射站点、接收站点和 RF 传播射线。更多信息，请参阅 `siteviewer`（Antenna Toolbox）。在单击此按钮之前，请在 **Map** 参数中指定 `siteviewer`（Antenna Toolbox）对象。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

#### 信道配置

### **Carrier frequencies** — 信道的载波频率 `2.1 GHz`（默认）| 非负标量或行向量

信道的载波频率，指定为以 Hz、kHz、MHz 或 GHz 表示的非负标量或行向量。

### **Simulate noise** — 仿真热噪声 `'on'`（默认）| `'off'`

选择此参数以仿真信道中的热噪声。在启用此模块中的该参数之前，您必须在 Configuration 模块中选择 **Simulate noise**。请注意，噪声仅添加到 TX 和 RX 天线中，而不添加到它们周围的介质中。

### **Ground and hide negative terminals** — 将 RF 电路端子接地 `'on'`（默认）| `'off'`

选择此选项可将负极端子接地并隐藏。清除此参数可暴露负极端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。

### **Edit System** — 编辑或展开 Channel 模块按钮

单击此按钮可断开 Channel 模块与库的链接，并将变量替换为模块使用模块参数估计的值。单击此按钮时，Channel 模块要么成为简单的未封装子系统，要么被展开。更多信息，请参阅 Edit Channel Block。

单击此按钮会弹出一个对话框，其中包含以下选项：

- **Edit System** — 编辑内部变量而不展开子系统。
- **Expand System** — 编辑子系统并在 Simulink 画布中展开该子系统。
- **Cancel** — 取消操作。

**注意**

一旦单击 **Edit System** 或 **Expand System** 按钮，该操作将无法撤销。

### TX 建模

### **Modeling options** — 对频率相关信道参数建模的技术 `Time domain`（默认）| `Frequency domain`

用于对频率相关信道参数建模的技术，指定为以下值之一：

- `Time domain` — 此技术创建解析有理模型，以近似范围内的所有数据。
- `Frequency domain` — 此技术为每个载波频率独立计算基带冲激响应。此技术基于卷积。选择此选项时，您还可以指定冲激响应的持续时间。更多信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。

这两种分析技术使用以下频率相关参数。

- 天线阻抗 — 此参数与发射天线端子处的输入阻抗有关，用于 RF 系统仿真。
- 归一化向量有效长度 — 此参数建立发射天线端子处流动的电流与特定方向上的辐射远场区域之间的关系。根据互易性，此参数还建立入射场与天线端子上感应开路电压之间的关系。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

### **Relative error desired (dB)** — 有理拟合的相对误差 `-40`（默认）| 标量

有理拟合的相对误差，指定为标量。该模块将此值应用于发射天线阻抗和归一化向量有效长度的时域建模，并在模块封装中显示相应的有理拟合结果。

#### 依赖项

要启用此属性，请将 **Modeling options** 设置为 `Time domain`。

### **Automatically estimate impulse response duration** — 自动计算冲激响应持续时间 `'on'`（默认）| `'off'`

选择此参数以自动计算冲激响应持续时间，或清除此参数以使用 **Impulse response duration** 参数手动指定冲激响应持续时间。该模块将此持续时间值应用于发射天线阻抗和归一化向量有效长度的频域建模。

#### 依赖项

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `0``s`（默认）| 标量

冲激响应持续时间，指定为标量，单位为 seconds。该模块将此持续时间值应用于发射天线阻抗和归一化向量有效长度的频域建模。

#### 依赖项

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`，并清除 **Automatically estimate impulse response duration**。

### 介质建模

### **Modeling options** — 对频率相关信道参数建模的技术 `Frequency domain`（默认）| `Time domain`

*自 R2024a 起*

用于对频率相关信道参数建模的技术，指定为以下值之一：

- `Frequency domain` — 此技术为每个载波频率独立计算基带冲激响应。此技术基于卷积。选择此选项时，您还可以指定冲激响应的持续时间。更多信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。
- `Time domain` — 此技术创建解析有理模型，以近似范围内的所有数据。

#### 依赖项

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

### **Relative error desired (dB)** — 有理拟合的相对误差 `-40`（默认）| 标量

*自 R2024a 起*

有理拟合的相对误差，指定为标量，单位为 dB。该模块将此值应用于介质的时域建模，并在模块封装中显示相应的有理拟合结果。

#### 依赖项

要启用此属性，请将 **Modeling options** 设置为 `Time domain`。

### **Automatically estimate impulse response duration** — 自动计算冲激响应持续时间 `'off'`（默认）| `'on'`

*自 R2024a 起*

选择此参数以自动计算冲激响应持续时间，或清除此参数以使用 **Impulse response duration** 参数手动指定冲激响应持续时间。该模块将此持续时间值应用于介质的频域建模。

#### 依赖项

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `0``s`（默认）| 标量

*自 R2024a 起*

冲激响应持续时间，指定为标量，单位为 seconds。该模块将此持续时间值应用于介质的频域建模。

#### 依赖项

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`，并清除 **Automatically estimate impulse response duration**。

### RX 建模

### **建模选项** — 用于对频率相关信道参数建模的技术 `Time domain` (默认) | `Frequency domain`

用于对频率相关信道参数建模的技术，指定为以下值之一：

- `Time domain` — 此技术创建一个解析有理模型，以近似范围内的所有数据。
- `Frequency domain` — 此技术独立计算每个载波频率的基带冲激响应。此技术基于卷积。选择此选项时，您还可以指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。

这两种分析技术使用以下频率相关参数。

- 天线阻抗 — 此参数与接收天线端子处的输入阻抗相关，用于 RF 系统仿真。
- 归一化矢量有效长度 — 此参数建立发射天线端子处流动的电流与特定方向上辐射远场区域之间的关系。由于互易性，此参数还建立入射场与天线端子上感应开路电压之间的关系。

#### 依赖关系

要启用此参数，请将 **信道模型源** 设置为 `Ray-tracing`。

### **期望的相对误差 (dB)** — 有理拟合的相对误差 `-40` (默认) | 标量

有理拟合的相对误差，指定为标量。该模块在接收天线阻抗和归一化矢量有效长度的时域建模中应用此值，并在模块掩码中显示相应的有理拟合结果。

#### 依赖关系

要启用此属性，请将 **建模选项** 设置为 `Time domain`。

### **自动估计冲激响应持续时间** — 自动计算冲激响应持续时间 `'on'` | `'off'`

选择此参数可自动计算冲激响应持续时间，或清除此参数以使用 **冲激响应持续时间** 参数手动指定冲激响应持续时间。该模块在接收天线阻抗和归一化矢量有效长度的频域建模中应用该持续时间值。

#### 依赖关系

要设置此参数，请将 **建模选项** 设置为 `Frequency domain`。

### **冲激响应持续时间** — 冲激响应持续时间 `0``s` (默认) | 标量

冲激响应持续时间，指定为标量。该模块在接收天线阻抗和归一化矢量有效长度的频域建模中应用该持续时间值。

#### 依赖关系

要设置此参数，请将 **建模选项** 设置为 `Frequency domain`，并清除 **自动估计冲激响应持续时间**。

## 所属库

RF Blockset / Circuit Envelope / Systems

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

### R2024b：`Time domain (rationalfit)` 参数已重命名

在 Channel block 中，**建模选项** 参数中的 `Time domain (rationalfit)` 参数值已重命名为 `Time domain`。

当您打开在 R2024b 之前创建的包含 Channel block 的模型时，参数名显示为 `Time domain`。

### R2024a：使用 Channel block 对频率相关传播场景建模

现在，您可以使用 Channel block，通过 **介质建模** 选项卡中的选项，对两个 RF 系统之间的频率相关射线追踪传播场景建模。

### R2024a：建模 TX 和建模 RX 选项卡已重命名

Channel block 中的 **建模 TX** 和 **建模 RX** 选项卡已分别重命名为 **TX 建模** 和 **RX 建模**。

当您打开在 R2024a 之前创建的包含 Channel block 的模型时，软件会将 **建模 TX** 和 **建模 RX** 选项卡的名称分别显示为 **TX 建模** 和 **RX 建模** 选项卡。

## 描述

为各向同性自由空间或基于射线追踪的信道建模

使用 Circuit Envelope 库中的 Channel block 为各向同性自由空间或基于射线追踪的信道建模，以考虑天线以及介质中 RF 传播的影响。
