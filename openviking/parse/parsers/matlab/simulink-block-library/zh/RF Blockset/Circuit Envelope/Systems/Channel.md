---
type: simulink-block
title: 'Channel'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Systems'
documentation_page: 'channel'
documentation_source_path: 'ref/channel.html'
language: zh-CN
chinese_source: worker-translation
---

# Channel

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Source of channel model
  summary: 信道源 Isotropic free-space（默认）| Ray-tracing
  group: 主要参数
- name: Antenna gain
  summary: 发射天线增益 0 dBi（默认）| 实数标量或向量 | 正标量或向量
  group: 主要参数
- name: Impedance (Ohm)
  summary: 发射天线输入阻抗 50（默认）| 复数标量或向量
  group: 主要参数
- name: Antenna gain
  summary: 接收天线增益 0 dBi（默认）| 实数标量或向量 | 正标量或向量
  group: 主要参数
- name: Impedance (Ohm)
  summary: 接收天线输入阻抗 50（默认）| 复数标量或向量
  group: 主要参数
- name: Path loss
  summary: 自由空间路径损耗 10 dB（默认）| 实数标量或向量 | 正标量或向量
  group: 主要参数
- name: Path delay
  summary: 自由空间路径延迟 0 s（默认）| 非负标量
  group: 主要参数
- name: Map
  summary: 用于可视化或表面数据的地图 "none"（默认）| siteviewer 对象 | triangulation 对象 | 字符串标量 | 字符向量
  group: 主要参数
- name: Propagation model
  summary: 传播模型 'raytracing'（默认）| RayTracing 对象
  group: 主要参数
- name: Tx site
  summary: 发射端站点 txsite 对象 | txsite 对象数组
  group: 主要参数
- name: Rx site
  summary: 接收端站点 rxsite 对象
  group: 主要参数
- name: View Site
  summary: 显示射频传播场景按钮
  group: 主要参数
- name: Carrier frequencies
  summary: 信道载波频率 2.1 GHz（默认）| 非负标量或行向量
  group: 主要参数
- name: Simulate noise
  summary: 仿真热噪声 'on'（默认）| 'off'
  group: 主要参数
- name: Ground and hide negative terminals
  summary: 接地并隐藏射频电路端子 'on'（默认）| 'off'
  group: 主要参数
- name: Edit System
  summary: 编辑或展开信道模块按钮
  group: 主要参数
- name: Modeling options
  summary: 对频率相关信道参数建模的技术 Time domain（默认）| Frequency domain
  group: TX 建模
- name: Relative error desired (dB)
  summary: 有理拟合的相对误差 -40（默认）| 标量
  group: TX 建模
- name: Automatically estimate impulse response duration
  summary: 自动计算冲激响应持续时间 'on'（默认）| 'off'
  group: TX 建模
- name: Impulse response duration
  summary: 冲激响应持续时间 0s（默认）| 标量
  group: TX 建模
- name: Modeling options
  summary: 对频率相关信道参数进行建模的技术 Frequency domain（默认）| Time domain
  group: 介质建模
- name: Relative error desired (dB)
  summary: 有理拟合的相对误差 -40（默认）| 标量
  group: 介质建模
- name: Automatically estimate impulse response duration
  summary: 自动计算冲激响应持续时间 'off'（默认）| 'on'
  group: 介质建模
- name: Impulse response duration
  summary: 冲激响应持续时间 0s（默认）| 标量
  group: 介质建模
- name: Modeling options
  summary: 对频率相关信道参数进行建模的技术 Time domain（默认）| Frequency domain
  group: RX 建模
- name: Relative error desired (dB)
  summary: 有理拟合的相对误差 -40（默认）| 标量
  group: RX 建模
- name: Automatically estimate impulse response duration
  summary: 自动计算冲激响应持续时间 'on' | 'off'
  group: RX 建模
- name: Impulse response duration
  summary: 冲激响应持续时间 0s（默认）| 标量
  group: RX 建模
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要参数

### **Source of channel model** — 信道源 `Isotropic free-space`（默认）| `Ray-tracing`

信道源，指定为以下之一：

- `Isotropic free-space` — 该模块对从发射点出发的电磁辐射在自由空间中传播的行为进行建模。自由空间传播模型没有强制频率范围，假设视距（LOS）条件，并忽略地形、地球曲率和其他障碍物。有关详细信息，请参阅 `FreeSpace`（Antenna Toolbox）。
- `Ray-tracing` — 该模块使用 3-D 环境几何对传播路径进行建模。有关详细信息，请参阅 `RayTracing`（Antenna Toolbox）。

  **注意**

  要指定 `Ray-tracing` 选项，您必须拥有 Antenna Toolbox™ 许可证。

#### TX Antenna

### **Antenna gain** — 发射天线增益 `0 dBi`（默认）| 实数标量或向量 | 正标量或向量

发射天线增益，指定为实数标量或向量，或正标量或向量。

- 如果指定实数标量或向量，则将 **Antenna gain** 参数单位设置为 `dBi`。
- 如果指定正标量或向量，则将 **Antenna gain** 参数单位设置为 `None`。
- 如果指定向量，则该向量的长度必须与 **Carrier frequencies** 参数中的向量长度相同。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

### **Impedance (Ohm)** — 发射天线输入阻抗 `50`（默认）| 复数标量或向量

发射天线输入阻抗，以欧姆为单位指定为复数标量或向量。该向量的长度必须与您在 **Carrier frequencies** 参数中指定的向量长度相同。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

**Data Types:** `double`
**Complex Number Support:** Yes

#### RX Antenna

### **Antenna gain** — 接收天线增益 `0 dBi`（默认）| 实数标量或向量 | 正标量或向量

接收天线增益，指定为实数标量或向量，或正标量或向量。

- 如果指定实数标量或向量，则将 **Antenna gain** 参数单位设置为 `dBi`。
- 如果指定正标量或向量，则将 **Antenna gain** 参数单位设置为 `None`。
- 如果指定向量，则该向量的长度必须与 **Carrier frequencies** 参数中的向量长度相同。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

### **Impedance (Ohm)** — 接收天线输入阻抗 `50`（默认）| 复数标量或向量

接收天线输入阻抗，以欧姆为单位指定为复数标量或向量。该向量的长度必须与您在 **Carrier frequencies** 参数中指定的向量长度相同。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

**Data Types:** `double`
**Complex Number Support:** Yes

#### Medium

### **Path loss** — 自由空间路径损耗 `10 dB`（默认）| 实数标量或向量 | 正标量或向量

自由空间路径损耗，指定为实数标量或向量，或正标量或向量。

- 如果指定实数标量或向量，则将 **Antenna gain** 参数单位设置为 `dB`。
- 如果指定正标量或向量，则将 **Antenna gain** 参数单位设置为 `None`。
- 如果指定向量，则该向量的长度必须与 **Carrier frequencies** 参数中的向量长度相同。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

### **Path delay** — 自由空间路径延迟 `0 s`（默认）| 非负标量

自由空间路径延迟，指定为非负标量，单位为秒、毫秒、微秒或纳秒。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Isotropic free-space`。

#### 射线追踪

### **Map** — 用于可视化或表面数据的地图 `"none"`（默认）| `siteviewer` 对象 | `triangulation` 对象 | 字符串标量 | 字符向量

用于可视化或表面数据的地图，指定为 `siteviewer` 对象、`triangulation` 对象、字符串标量或字符向量。有效的地图值和默认地图值取决于坐标系，如传播模型中所述。

| 坐标系 | 有效的地图值 |
| --- | --- |
| `"geographic"` | - 一个 `siteviewer` (Antenna Toolbox) 对象a。 - 地形名称，如果函数在调用时带有输出参数。   有效的地形名称为 `"none"`、`"gmted2010"`，或使用 `addCustomTerrain` (Antenna Toolbox) 创建的自定义地形名称。 |
| `"cartesian"` | - `"none"`。 - 一个 `siteviewer` 对象。 - STL 文件的名称。 - 一个 `triangulation` 对象。 |
| a 边界和区域标签的对齐是数据供应商所提供功能的展示，并不意味着 MathWorks® 的认可。 | |

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

**数据类型：** `char` | `string`

### **Propagation model** — 传播模型 `'raytracing'`（默认）| `RayTracing` 对象

传播模型，指定为 `'raytracing'` 或 `RayTracing` (Antenna Toolbox) 对象。默认值为 `'raytracing'`，它使用 SBR 方法，查找最多包含两次反射和零次绕射的路径，并丢弃比最强路径弱超过 40 dB 的路径。

您可以使用 `propagationModel` (Antenna Toolbox) 函数创建 `RayTracing` (Antenna Toolbox) 对象。`RayTracing` 对象使您能够指定射线追踪方法、最大反射和绕射次数、路径损耗阈值以及建筑物和地形材料等属性。

有关射线追踪方法之间差异的信息，请参阅 Choose a Propagation Model (Antenna Toolbox)。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

**数据类型：** `char` | `string`

### **Tx site** — 发射端站点 `txsite` 对象 | `txsite` 对象数组

发射端站点，指定为 `txsite` (Antenna Toolbox) 对象或 `txsite` 对象数组。如果指定数组，则组成该数组的 `txsite` 对象除 `TransmitterFrequency` 属性外必须完全相同。

**注意**

- 在模块中使用 **Tx site** 中指定的天线、阵列或 PCB 堆叠对象之前，请至少对一个频率分析这些对象。
- 将 `txsite` 对象的 `Antenna` 属性指定为 Antenna Catalog (Antenna Toolbox) 中的天线元件或 Array Catalog (Antenna Toolbox) 中的阵列元件。有关更多信息，请参阅 `txsite` (Antenna Toolbox)。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

### **Rx site** — 接收端站点 `rxsite` 对象

接收端站点，指定为 `rxsite` (Antenna Toolbox) 对象。

**注意**

- 在模块中使用 **Rx site** 中指定的天线、阵列或 PCB 堆叠对象之前，请至少对一个频率分析这些对象。
- 将 `rxsite` 对象的 `Antenna` 属性指定为 Antenna Catalog (Antenna Toolbox) 中的天线元件或 Array Catalog (Antenna Toolbox) 中的阵列元件。有关更多信息，请参阅 `rxsite` (Antenna Toolbox)。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

### **View Site** — 显示射频传播场景按钮

点击此按钮可显示发射端站点、接收端站点和射频传播射线。有关详细信息，请参阅 `siteviewer` (Antenna Toolbox)。在点击此按钮之前，请在 **Map** 参数中指定 `siteviewer` (Antenna Toolbox) 对象。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

#### 信道配置

### **Carrier frequencies** — 信道载波频率 `2.1 GHz`（默认）| 非负标量或行向量

信道的载波频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的非负标量或行向量。

### **Simulate noise** — 仿真热噪声 `'on'`（默认）| `'off'`

选择此参数以仿真信道中的热噪声。您必须先在此模块中启用该参数之前，在 Configuration 模块中选择 **Simulate noise**。请注意，噪声仅添加到 TX 和 RX 天线中，而不会添加到其周围介质中。

### **Ground and hide negative terminals** — 接地并隐藏射频电路端子 `'on'`（默认）| `'off'`

选择此选项以接地并隐藏负端子。清除此参数以暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。

### **Edit System** — 编辑或展开信道模块按钮

点击此按钮可断开 Channel 模块与库的链接，并将变量替换为模块使用模块参数估计的值。点击此按钮时，Channel 模块要么变为简单的未屏蔽子系统，要么被展开。有关详细信息，请参阅 Edit Channel Block。

点击此按钮会弹出一个包含以下选项的对话框：

- **Edit System** — 在不展开子系统的情况下编辑内部变量。
- **Expand System** — 编辑子系统并在 Simulink 画布中展开子系统。
- **Cancel** — 取消操作。

**注意**

一旦您点击 **Edit System** 或 **Expand System** 按钮，该操作无法撤销。

### TX 建模

### **Modeling options** — 对频率相关信道参数建模的技术 `Time domain`（默认）| `Frequency domain`

对频率相关信道参数建模的技术，指定为以下值之一：

- `Time domain` — 此技术创建一个解析有理模型，近似该范围内的所有数据。
- `Frequency domain` — 此技术独立计算每个载波频率的基带冲激响应。此技术基于卷积。您还可以在选择此选项时指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。

这两种分析技术使用以下频率相关参数。

- 天线阻抗 — 此参数与发射天线端子处的输入阻抗有关，用于射频系统仿真。
- 归一化矢量有效长度 — 此参数建立发射天线端子处流动的电流与特定方向上辐射远场区域之间的关系。由于互易性，此参数还建立入射场与天线端子上感应开路电压之间的关系。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

### **Relative error desired (dB)** — 有理拟合的相对误差 `-40`（默认）| 标量

有理拟合的相对误差，指定为标量。模块在发射天线阻抗和归一化矢量有效长度的时域建模中应用此值，并在模块屏蔽中显示相应的有理拟合结果。

#### 依赖关系

要启用此属性，请将 **Modeling options** 设置为 `Time domain`。

### **Automatically estimate impulse response duration** — 自动计算冲激响应持续时间 `'on'`（默认）| `'off'`

选择此参数可自动计算冲激响应持续时间，或清除此参数以使用 **Impulse response duration** 参数手动指定冲激响应持续时间。该模块在发射机天线阻抗和归一化矢量有效长度的频域建模中应用该持续时间值。

#### 依赖关系

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `0``s`（默认）| 标量

冲激响应持续时间，指定为以秒为单位的标量。该模块在发射机天线阻抗和归一化矢量有效长度的频域建模中应用该持续时间值。

#### 依赖关系

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`，并清除 **Automatically estimate impulse response duration**。

### 介质建模

### **Modeling options** — 对频率相关信道参数进行建模的技术 `Frequency domain`（默认）| `Time domain`

*自 R2024a 起*

对频率相关信道参数进行建模的技术，指定为以下值之一：

- `Frequency domain` — 此技术独立计算每个载波频率的基带冲激响应。此技术基于卷积。选择此选项时，您还可以指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。
- `Time domain` — 此技术创建一个解析有理模型，以近似该范围内的所有数据。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

### **Relative error desired (dB)** — 有理拟合的相对误差 `-40`（默认）| 标量

*自 R2024a 起*

有理拟合的相对误差，指定为以 dB 为单位的标量。该模块在介质的时域建模中应用此值，并在模块掩码中显示相应的有理拟合结果。

#### 依赖关系

要启用此属性，请将 **Modeling options** 设置为 `Time domain`。

### **Automatically estimate impulse response duration** — 自动计算冲激响应持续时间 `'off'`（默认）| `'on'`

*自 R2024a 起*

选择此参数可自动计算冲激响应持续时间，或清除此参数以使用 **Impulse response duration** 参数手动指定冲激响应持续时间。该模块在介质的频域建模中应用该持续时间值。

#### 依赖关系

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `0``s`（默认）| 标量

*自 R2024a 起*

冲激响应持续时间，指定为以秒为单位的标量。该模块在介质的频域建模中应用该持续时间值。

#### 依赖关系

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`，并清除 **Automatically estimate impulse response duration**。

### RX 建模

### **Modeling options** — 对频率相关信道参数进行建模的技术 `Time domain`（默认）| `Frequency domain`

用于对频率相关信道参数进行建模的技术，指定为以下值之一：

- `Time domain` — 此技术创建一个解析有理模型，用于近似范围内的所有数据。
- `Frequency domain` — 此技术独立计算每个载波频率的基带冲激响应。此技术基于卷积。选择此选项时，您还可以指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。

这两种分析技术使用以下频率相关参数。

- 天线阻抗 — 此参数与接收天线端子处的输入阻抗相关，并用于 RF 系统仿真。
- 归一化矢量有效长度 — 此参数建立发射天线端子处流动的电流与特定方向上辐射远场区域之间的关系。由于互易性，此参数还建立入射场与天线端子上感应的开路电压之间的关系。

#### 依赖关系

要启用此参数，请将 **Source of channel model** 设置为 `Ray-tracing`。

### **Relative error desired (dB)** — 有理拟合的相对误差 `-40`（默认）| 标量

有理拟合的相对误差，指定为标量。该模块在接收天线阻抗和归一化矢量有效长度的时域建模中应用此值，并在模块掩码中显示相应的有理拟合结果。

#### 依赖关系

要启用此属性，请将 **Modeling options** 设置为 `Time domain`。

### **Automatically estimate impulse response duration** — 自动计算冲激响应持续时间 `'on'` | `'off'`

选择此参数可自动计算冲激响应持续时间，或清除此参数以使用 **Impulse response duration** 参数手动指定冲激响应持续时间。该模块在接收天线阻抗和归一化矢量有效长度的频域建模中应用该持续时间值。

#### 依赖关系

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `0``s`（默认）| 标量

冲激响应持续时间，指定为标量。该模块在接收天线阻抗和归一化矢量有效长度的频域建模中应用该持续时间值。

#### 依赖关系

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`，并清除 **Automatically estimate impulse response duration**。
## 所属库

RF Blockset / Circuit Envelope / Systems

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

### R2024b：`Time domain (rationalfit)` 参数已重命名

Channel 模块中 **Modeling options** 参数的 `Time domain (rationalfit)` 参数值已重命名为 `Time domain`。

当您打开在 R2024b 之前创建的包含 Channel 模块的模型时，该参数名称显示为 `Time domain`。

### R2024a：使用 Channel 模块对频率相关传播场景进行建模

您现在可以使用 Channel 模块，通过 **Medium Modeling** 选项卡中的选项，对两个 RF 系统之间的频率相关 Ray-trace 传播场景进行建模。

### R2024a：Modeling TX 和 Modeling RX 选项卡已重命名

Channel 模块中的 **Modeling TX** 和 **Modeling RX** 选项卡已分别重命名为 **TX Modeling** 和 **RX Modeling**。

当您打开在 R2024a 之前创建的包含 Channel 模块的模型时，软件会将 **Modeling TX** 和 **Modeling RX** 选项卡的名称分别显示为 **TX Modeling** 和 **RX Modeling** 选项卡。

## 描述

对基于各向同性自由空间或射线追踪的信道进行建模

使用电路包络库中的 Channel 模块对基于各向同性自由空间或射线追踪的信道进行建模，以考虑介质中天线和射频传播的影响。
