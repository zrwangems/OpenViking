---
type: simulink-block
title: 'Antenna'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
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

### **Source of antenna model** — 天线模型 `Isotropic radiator`（默认）| `Antenna Designer` | `Antenna object`

天线模型，指定为以下之一：

- `Isotropic radiator`
- `Antenna Designer`
- `Antenna object`

**注意**

- 要使用 `Antenna Designer` 和 `Antenna object` 选项，您需要 Antenna Toolbox™。

- Antenna 模块支持模型保护和加速器模式。当 **Source of antenna model** 设置为：

  - `Isotropic radiator` — 支持加速器模式。
  - `Antenna Designer` 或 `Antenna object` — 支持加速器模式、快速加速器模式、模型引用加速器模式和模型保护。

  有关详细信息，请参阅 Enable Model Protection and Accelerator Modes in RF Blockset Models。*（自 R2024b 起）*

### **Create Antenna** — 打开 Antenna Toolbox Antenna Designer 应用 按钮

从 Antenna Toolbox 打开 Antenna Designer 应用以创建天线。

#### 依赖关系

要启用此参数，请将 **Source of antenna model** 设置为 `Antenna Designer`。

### **Antenna object** — 来自工作空间的天线或阵列元素输入 天线目录对象 | 天线阵列目录对象 | `measuredAntenna` 对象 | `pcbstack` 对象

来自工作空间的天线或阵列元素输入，指定为以下对象之一：

- 天线目录 — 使用天线目录（Antenna Toolbox）中的任一天线对象。
- 阵列目录 — 使用阵列目录（Antenna Toolbox）中的任一数组对象。您可以指定最多具有 65 个端口的阵列。
- 测量天线 — 使用 `measuredAntenna` 对象来对测量天线或阵列进行建模，该天线或阵列由其 S 参数和包含两个极化分量的频率相关远场辐射方向图来表征。您可以对最多具有 65 个端口的阵列进行建模。*（自 R2023b 起）*
- PCB 堆叠 — 使用 `pcbStack`（Antenna Toolbox）对象对单馈或多馈 PCB 天线进行建模。

**注意**

在模块中使用天线、阵列或 PCB 堆叠对象之前，请在工作空间中至少对一个频率分析这些对象。

#### 依赖关系

要启用此参数，请将 **Source of antenna model** 设置为 `Antenna object`。

### **Antenna Gain** — 天线增益 `0` `dBi`（默认）| 实数标量或向量 | 正标量或向量

天线增益，如果将单位设置为 `dBi`，则指定为实数标量或向量；如果将单位设置为 `None`，则指定为正标量或向量。如果天线增益是向量，则向量长度必须等于 **Incident carrier frequencies** 和 **Radiated carrier frequencies** 的向量长度。

#### 依赖关系

要启用此参数，请将 **Source of antenna model** 设置为 `Isotropic radiator`，并选中 **Input incident wave** 或 **Output radiated wave** 或两者。

### **Impedance (Ohm)** — 输入阻抗 `50`（默认）| 复数值标量或向量

输入阻抗，指定为以欧姆为单位的复数值标量或向量。如果阻抗是向量，则向量长度必须等于 **Incident carrier frequencies** 和 **Radiated carrier frequencies** 的长度。

#### 依赖关系

要启用此参数，请将 **天线模型来源** 设置为
`各向同性辐射器`。

**数据类型：** `double`
**复数支持：** 是

### **输入入射波** — 用于模拟接收天线的输入入射波 `'off'`（默认）| `'on'`

如果要模拟接收天线，请选择此参数。

### **输出辐射波** — 用于发射天线的输出辐射波 `'on'`（默认）| `'off'`

如果要模拟发射天线，请选择此参数。

### **入射载波频率** — 接收信号的载波频率 `2.1` `GHz`（默认）| 非负标量或行向量

接收信号的载波频率，指定为以赫兹为单位的非负标量或以赫兹为单位的行向量，其中每个元素的单位为赫兹。如果
**天线增益** 或 **阻抗** 的值是向量，
则 **入射载波频率** 和
**辐射载波频率** 的值必须相同。

#### 依赖关系

要启用此参数，请选择 **输入入射
波**。

### **辐射载波频率** — 发射信号的载波频率 `2.1` `GHz`（默认）| 非负标量或行向量

发射信号的载波频率，指定为以赫兹为单位的非负标量或以赫兹为单位的行向量，其中每个元素的单位为赫兹。如果
**天线增益** 或 **阻抗** 的值是向量，
则 **入射载波频率** 和
**辐射载波频率** 的值必须相同。

#### 依赖关系

要启用此参数，请选择 **输出辐射
波**。

### **离开方向** — 输出信号功率波辐射所朝向的方位角和仰角 `[0 0]` `deg`（默认）| 长度为 1×2 的有限实值行向量 | 长度为 *m*×2 的有限实值矩阵

输出信号功率波辐射所朝向的方位角和仰角，
指定为长度为 1×2 的有限实值行向量或长度为 *m*×2 的有限实值矩阵 *(自 R2023a 起)*，其中每个元素的
单位为度或弧度。*m* 是范围
[2, 100] 内的整数。

#### 依赖关系

要启用此参数，请将 **天线模型来源** 设置为
`Antenna Designer` 或 `Antenna
object`，并选择 **输出辐射
波**。

### **到达方向** — 输入信号功率波到达所来自的方位角和仰角 `[180 0]` `deg`（默认）| 长度为 1×2 的有限实值行向量 | 长度为 *m*×2 的有限实值矩阵

输入信号功率波到达所朝向的方位角和仰角，
指定为长度为 1×2 的有限实值行向量或长度为 *m*×2 的有限实值矩阵 *(自 R2023a 起)*，其中每个元素的
单位为度或弧度。*m* 是范围
[2, 100] 内的整数。

#### 依赖关系

要启用此参数，请将 **天线模型来源** 设置为
`Antenna Designer` 或 `Antenna
object`，并选择 **输入入射波**。

### **模拟噪声** — 模拟热噪声 `'on'`（默认）| `'off'`

选择此参数以模拟天线中由天线端子处所见阻抗的实部引起的热噪声。您还必须在 Configuration 模块中选择 **模拟
噪声**。

### **接地并隐藏负端子** — 将 RF 电路端子接地 `'on'`（默认）| `'off'`

选择此选项以将负端子接地并隐藏。清除此参数以暴露负端子。通过暴露这些端子，您可以将它们连接到模型的
其他部分。

### 建模

### **建模选项** — 对频率相关天线参数进行建模 `时域`（默认）| `频域`

对频率相关天线参数进行建模，指定为：

- `时域` — 此技术创建一个解析有理模型，用于近似整个数据范围。
- `频域` — 此技术针对每个载波频率独立计算基带冲激响应。此技术基于卷积。可以选择指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。

频率相关参数包括：

- 天线阻抗 — 天线端子处的输入阻抗。用于射频系统仿真。
- 归一化矢量有效长度 — 用于关联天线端子处流动的电流与给定方向上的辐射远场的属性。根据互易性，有效长度还关联入射场与天线端子上的感应开路电压。

#### 依赖关系

要将源 **Source of antenna model** 设置为 `Antenna Designer` 或 `Antenna object`，以激活包含 **Modeling options** 参数的 **Modeling** 选项卡。

### **期望相对误差 (dB)** — 有理拟合可接受的相对误差 `-40`（默认）| 标量

有理拟合可接受的相对误差，指定为标量。适用于天线阻抗和归一化矢量有效长度的时域建模。每个属性的相应有理拟合结果显示在模块掩膜上。

#### 依赖关系

要启用此属性，请将 **Modeling options** 设置为 `Time domain`。

### **自动估计冲激响应持续时间** — 自动计算冲激响应 `'on'` | `'off'`

选择此参数可自动计算冲激响应持续时间。清除此参数可使用 **Impulse response duration** 手动指定冲激响应持续时间。适用于天线阻抗和归一化矢量有效长度的频域建模。

#### 依赖关系

要设置此参数，请将 **Modeling options** 设置为 `Frequency domain`。

### **冲激响应持续时间** — 冲激响应持续时间 `1e-10` `s`（默认）| 标量

冲激响应持续时间，指定为标量。适用于天线阻抗和归一化矢量有效长度的频域建模。

#### 依赖关系

要设置此参数，请先在 **Modeling options** 中选择 `Frequency domain`。然后，清除 **Automatically estimate impulse response duration**。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2024b：`Time domain (rationalfit)` 参数已重命名

Antenna 模块中 **Modeling options** 参数的 `Time domain (rationalfit)` 参数值已重命名为 `Time domain`。

当您打开在 R2024b 之前创建的包含 Antenna 模块的模型时，参数名称显示为 `Time domain`。

### R2024b：在 Antenna 模块中启用模型保护和加速器模式

Antenna 模块现在支持以下功能：

- 模型保护：通过创建 SLXP 文件格式的受保护模型来隐藏模型内容。
- 快速加速和模型引用加速仿真模式：这些加速器模式通过为模型生成可执行文件来提高仿真速度。加速程度因模型而异。

**注意**

仅当 **Source of antenna model** 参数设置为 `Antenna Designer` 或 `Antenna object` 时，Antenna 模块才支持模型保护和加速器模式。

### R2023b：使用 `measuredAntenna` 对象对天线建模

Circuit Envelope 库中的 Antenna 模块现在支持
`measuredAntenna` 对象。指定此对象可对测量天线
或阵列进行建模，其特性由 S 参数和随频率变化的远场辐射
方向图描述，且包含两个极化分量。

### R2023a：Antenna 模块中的多个到达方向和离开方向

现在可以使用 Antenna 模块通过 **Direction of arrival** 和
**Direction of departure** 属性在多个方向上发射和接收信号。

### R2022a：对发射和接收天线阵列建模

要对发射和接收天线建模，请在
**Antenna
object** 参数中指定 Array Catalog (Antenna Toolbox) 中的天线阵列。

### R2021b：Antenna 模块图标已更新

Antenna 模块图标在 R2021b 中已更新。该模块图标现在是
动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 Antenna 模块的模型时，
软件会将该模块图标替换为 R2021b 版本。

## 描述

对天线或天线阵列建模，考虑入射功率波 (RX) 和辐射功率波 (TX)

使用 Antenna 模块对天线或天线阵列建模。使用此模块可以：

- 将入射功率波向量的 Simulink® 输入转换为天线或天线阵列端口处的 RF Blockset™ 电压信号。
- 将 RF Blockset 天线或天线阵列端口处的电流转换为辐射功率波向量的 Simulink 输出。
- 将天线阻抗引入 RF 系统。

默认情况下，Antenna 模块是各向同性辐射器，产生 Simulink 输出信号。对于各向同性辐射器，请在模块参数中指定
天线的增益和阻抗。**Radiated carrier frequencies**
参数是一组载波频率，Antenna 模块在这些频率上创建
辐射功率波。有关详细信息，请参阅 Radiated Wave and Incident Wave。

Antenna 模块掩码图标是动态的：这些图标显示噪声参数的当前状态，
指示您是否在 **Antenna object**
参数中指定了 `antennaarray` 对象，并根据
`antennaarray` 对象中的元素数量更新端口数量。此表显示了模块图标如何根据
**Simulate noise**
和 **Antenna object**
参数的状态而变化。

| Antenna object | Simulate noise: `on` | Simulate noise: `off` |
| --- | --- | --- |
| Antenna Catalog Objects | Antenna 模块图标，Simulate noise 设置为 on。 | Antenna 模块图标，Simulate noise 设置为 off。 |
| Antenna Array Catalog Objects | Antenna 模块图标，以四元素天线阵列作为输入，且 Simulate noise 设置为 on。 | Antenna 模块图标，以四元素天线阵列作为输入，且 Simulate noise 设置为 off。 |
