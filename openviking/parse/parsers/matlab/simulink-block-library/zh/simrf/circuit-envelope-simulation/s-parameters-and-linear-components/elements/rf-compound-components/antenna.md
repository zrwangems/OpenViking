---
type: simulink-block
title: 'Antenna'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / RF Compound Components'
documentation_page: 'antenna'
documentation_source_path: 'ref/antenna.html'
language: zh-CN
chinese_source: worker-translation
---

# Antenna

## 端口

### 输入

### **RX** — 接收信号 标量 | 向量 | 矩阵 | *m*-by-*n*-by-*k* 数组

接收信号，指定为标量、向量、矩阵或大小为 *m*-by-*n*-by-*k* 的数组。在数组中：

- *m* — 表示帧大小
- *n* — 表示干扰源数量
- *k* — 表示水平或垂直极化。*k* 的值必须为 2。

**数据类型：** `double`
### 输出

### **TX** — 发射信号 标量 | 向量 | 矩阵 | *m*-by-*n*-by-*k* 数组

发射信号，指定为标量、向量、矩阵或大小为 *m*-by-*n*-by-*k* 的数组。在数组中：

- *m* — 表示帧大小
- *n* — 表示干扰源数量
- *k* — 表示水平或垂直极化。*k* 的值必须为 2。

**数据类型：** `double`

## 参数

### 主要

### **Source of antenna model** — Antenna model `Isotropic radiator` (default) | `Antenna Designer` | `Antenna object`

天线模型，指定为以下之一：

- `Isotropic radiator`
- `Antenna Designer`
- `Antenna object`

**注意**

- 要使用 `Antenna Designer` 和 `Antenna object` 选项，您需要 Antenna Toolbox™。

- Antenna 模块支持模型保护和加速器模式。当 **Source of antenna model** 设置为：

  - `Isotropic radiator` — 支持加速器模式。
  - `Antenna Designer` 或 `Antenna object` — 支持加速器模式、快速加速器模式、模型引用加速器模式和模型保护。

  有关详细信息，请参阅在 RF Blockset 模型中启用模型保护和加速器模式。*(自 R2024b 起)*

### **Create Antenna** — 打开 Antenna Toolbox Antenna Designer 应用的按钮

从 Antenna Toolbox 打开 Antenna Designer 应用以创建天线。

#### 依赖项

要启用此参数，请将 **Source of antenna model** 设置为 `Antenna Designer`。

### **Antenna object** — 来自工作区的天线或阵列单元输入 天线目录对象 | 天线阵列目录对象 | `measuredAntenna` 对象 | `pcbstack` 对象

来自工作区的天线或阵列单元输入，指定为以下对象之一：

- Antenna catalog — 使用 Antenna Catalog (Antenna Toolbox) 中的任意一个天线对象。
- Array catalog — 使用 Array Catalog (Antenna Toolbox) 中的任意一个阵列对象。您可以指定一个最多具有 65 个端口的阵列。
- Measured antenna — 使用 `measuredAntenna` 对象对实测天线或阵列建模，该天线或阵列由其 S 参数和包含两个极化分量的频率相关远场辐射方向图表征。您可以对最多具有 65 个端口的阵列建模。*(自 R2023b 起)*
- PCB stack — 使用 `pcbStack` (Antenna Toolbox) 对象对单馈或多馈 PCB 天线建模。

**注意**

在模块中使用天线、阵列或 PCB stack 对象之前，请至少在一个频率上分析工作区中的这些对象。

#### 依赖项

要启用此参数，请将 **Source of antenna model** 设置为 `Antenna object`。

### **Antenna Gain** — 天线增益 `0` `dBi`（默认） | 实数标量或向量 | 正标量或向量

天线增益，如果您将单位设置为 `dBi`，则指定为实数标量或向量；如果您将单位设置为 `None`，则指定为正标量或向量。如果天线增益是向量，则该向量长度必须等于 **Incident carrier frequencies** 和 **Radiated carrier frequencies** 的向量长度。

#### 依赖项

要启用此参数，请将 **Source of antenna model** 设置为 `Isotropic radiator`，并选中 **Input incident wave** 或 **Output radiated wave**，或同时选中两者。

### **Impedance (Ohm)** — 输入阻抗 `50`（默认） | 复数值标量或向量

输入阻抗，指定为以欧姆为单位的复数值标量或向量。如果阻抗是向量，则该向量长度必须等于 **Incident carrier frequencies** 和 **Radiated carrier frequencies** 的长度。

#### 依赖项

要启用此参数，请将 **Source of antenna model** 设置为 `Isotropic radiator`。

**数据类型：** `double`
**复数支持：** 是

### **Input incident wave** — 用于仿真接收天线的输入入射波 `'off'`（默认） | `'on'`

如果要仿真接收天线，请选择此参数。

### **Output radiated wave** — 用于发射天线的输出辐射波 `'on'`（默认） | `'off'`

如果要仿真发射天线，请选择此参数。

### **Incident carrier frequencies** — 用于接收信号的载波频率 `2.1` `GHz`（默认） | 非负标量或行向量

用于接收信号的载波频率，指定为以赫兹为非负标量，或每个元素单位均为赫兹的行向量。如果 **Antenna gain** 或 **Impedance** 的值是向量，则 **Incident carrier frequencies** 和 **Radiated carrier frequencies** 的值必须相同。

#### 依赖项

要启用此参数，请选中 **Input incident wave**。

### **Radiated carrier frequencies** — 用于发射信号的载波频率 `2.1` `GHz`（默认） | 非负标量或行向量

用于发射信号的载波频率，指定为以赫兹为非负标量，或每个元素单位均为赫兹的行向量。如果 **Antenna gain** 或 **Impedance** 的值是向量，则 **Incident carrier frequencies** 和 **Radiated carrier frequencies** 的值必须相同。

#### 依赖项

要启用此参数，请选中 **Output radiated wave**。

### **Direction of departure** — 输出信号功率波辐射所朝向的方位角和仰角 `[0 0]` `deg`（默认） | 长度为 1-by-2 的有限实值行向量 | 长度为 *m*-by-2 的有限实值矩阵

输出信号功率波辐射所朝向的方位角和仰角，指定为长度为 1-by-2 的有限实值行向量或长度为 *m*-by-2 的有限实值矩阵 *(自 R2023a 起)*，其中每个元素的单位均为度或弧度。*m* 是范围为 [2, 100] 的整数。

#### 依赖项

要启用此参数，请将 **Source of antenna model** 设置为 `Antenna Designer` 或 `Antenna object`，并选中 **Output radiated wave**。

### **Direction of arrival** — 输入信号功率波从其到达的方位角和仰角 `[180 0]` `deg`（默认） | 长度为 1-by-2 的有限实值行向量 | 长度为 *m*-by-2 的有限实值矩阵

输入信号功率波从其到达的方位角和仰角，指定为长度为 1-by-2 的有限实值行向量或长度为 *m*-by-2 的有限实值矩阵 *(自 R2023a 起)*，其中每个元素的单位均为度或弧度。*m* 是范围为 [2, 100] 的整数。

#### 依赖项

要启用此参数，请将 **Source of antenna model** 设置为 `Antenna Designer` 或 `Antenna object`，并选中 **Input incident wave**。

### **Simulate noise** — 仿真热噪声 `'on'`（默认） | `'off'`

选择此参数可仿真天线中的热噪声，该噪声由天线端口处看到的阻抗实部导致。您还必须在 Configuration 模块中选择 **Simulate noise**。

### **Ground and hide negative terminals** — 将 RF 电路端子接地 `'on'`（默认） | `'off'`

选择此选项可将负极端子接地并隐藏它们。清除此参数可显示负极端子。通过显示这些端子，您可以将它们连接到模型的其他部分。

### 建模

### **Modeling options** — 对频率相关天线参数进行建模 `Time domain`（默认） | `Frequency domain`

对频率相关天线参数进行建模，指定为：

- `Time domain` — 此技术会创建一个解析有理模型，用于近似整个数据范围。
- `Frequency domain` — 此技术会针对每个载波频率独立计算基带冲激响应。此技术基于卷积。可以选择指定冲激响应的持续时间。有关详细信息，请参阅比较 S 参数的时域和频域仿真选项。

频率相关参数包括：

- Antenna impedance — 天线端口处的输入阻抗。它用于 RF 系统仿真。
- Normalized vector effective length — 一个属性，用于关联天线端口处流动的电流与给定方向上的辐射远场。由于互易性，有效长度还关联入射场与天线端口上感应的开路电压。

#### 依赖项

要将 **Source of antenna model** 设置为 `Antenna Designer` 或 `Antenna object`，以激活包含 **Modeling options** 参数的 **建模** 选项卡。

### **Relative error desired (dB)** — 有理拟合可接受的相对误差 `-40`（默认） | 标量

有理拟合可接受的相对误差，指定为标量。适用于天线阻抗和归一化向量有效长度的时域建模。每个属性对应的有理拟合结果会显示在模块封装上。

#### 依赖项

要启用此属性，请将 **Modeling options** 设置为 `Time domain`。

### **Automatically estimate impulse response duration** — 自动计算冲激响应 `'on'` | `'off'`

选择此参数可自动计算冲激响应持续时间。清除此参数可使用 **Impulse response duration** 手动指定冲激响应持续时间。适用于天线阻抗和归一化向量有效长度的频域建模。

#### 依赖项

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `1e-10``s`（默认） | 标量

冲激响应持续时间，指定为标量。适用于天线阻抗和归一化向量有效长度的频域建模。

#### 依赖项

要设置此参数，请先在 **Modeling options** 中选择 `Frequency domain`。然后，清除 **Automatically estimate impulse response duration**。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2024b: `Time domain (rationalfit)` 参数已重命名

Antenna 模块中 **Modeling options** 参数内的 `Time domain (rationalfit)` 参数值已重命名为 `Time domain`。

当您打开在 R2024b 之前创建且包含 Antenna 模块的模型时，参数名显示为 `Time domain`。

### R2024b: 在 Antenna 模块中启用模型保护和加速器模式

Antenna 模块现在支持以下功能：

- 模型保护：通过以 SLXP 文件格式创建受保护模型来隐藏模型内容。
- 快速加速器和模型引用加速器仿真模式：这些加速器模式通过为模型生成可执行文件来提高仿真速度。加速程度因模型而异。

**注意**

仅当 **Source of antenna model** 参数设置为 `Antenna Designer` 或 `Antenna object` 时，Antenna 模块才支持模型保护和加速器模式。

### R2023b: 使用 `measuredAntenna` 对象对天线建模

Circuit Envelope 库中的 Antenna 模块现在支持 `measuredAntenna` 对象。指定此对象可对实测天线或阵列建模，该天线或阵列由其 S 参数和包含两个极化分量的频率相关远场辐射方向图表征。

### R2023a: Antenna 模块中支持多个到达和离开方向

现在，您可以使用 Antenna 模块，通过 **Direction of arrival** 和 **Direction of departure** 属性在多个方向上发送和接收信号。

### R2022a: 对发射和接收天线阵列建模

要对发射和接收天线建模，请在 **Antenna object** 参数中指定来自 Array Catalog (Antenna Toolbox) 的天线阵列。

### R2021b: Antenna 模块图标已更新

Antenna 模块图标在 R2021b 中已更新。该模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建且包含 Antenna 模块的模型时，软件会将该模块图标替换为 R2021b 版本。

## 描述

对天线或天线阵列建模，并考虑入射功率波 (RX) 和辐射功率波 (TX)

使用 Antenna 模块对天线或天线阵列建模。使用此模块可以：

- 将入射功率波向量的 Simulink® 输入转换为天线或天线阵列端口处的 RF Blockset™ 电压信号。
- 将 RF Blockset 天线或天线阵列端口处的电流转换为辐射功率波向量的 Simulink 输出。
- 将天线阻抗引入 RF 系统。

默认情况下，Antenna 模块是各向同性辐射器，会生成 Simulink 输出信号。对于各向同性辐射器，请在模块参数中指定天线的增益和阻抗。**Radiated carrier frequencies** 参数是一组载波频率，Antenna 模块在这些频率上生成辐射功率波。有关详细信息，请参阅辐射波和入射波。

Antenna 模块封装图标是动态的：这些图标显示噪声参数的当前状态，指示您是否在 **Antenna object** 参数中指定了 `antennaarray` 对象，并根据 `antennaarray` 对象中的元素数量更新端口数。下表显示了模块图标如何根据 **Simulate noise** 和 **Antenna object** 参数的状态而变化。

| Antenna object | Simulate noise: `on` | Simulate noise: `off` |
| --- | --- | --- |
| Antenna Catalog 对象 | Antenna 模块图标，其中 Simulate noise 设置为 `on`。 | Antenna 模块图标，其中 Simulate noise 设置为 `off`。 |
| Antenna Array Catalog 对象 | Antenna 模块图标，其中输入为四元天线阵列，并且 Simulate noise 设置为 `on`。 | Antenna 模块图标，其中输入为四元天线阵列，并且 Simulate noise 设置为 `off`。 |
