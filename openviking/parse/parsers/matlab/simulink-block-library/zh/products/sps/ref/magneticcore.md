---
type: simulink-block
title: 'Magnetic Core'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Basic'
documentation_page: 'magneticcore'
documentation_source_path: 'ref/magneticcore.html'
language: zh-CN
chinese_source: worker-translation
---

# Magnetic Core

## 端口

### 守恒

### **N** — 北端磁性

与北端关联的磁性守恒端口。

### **S** — 南端磁性

与南端关联的磁性守恒端口。

### **H** — 热质量热

与热质量关联的热端口。

#### 依赖关系

要启用此端口，请选择 **热效应建模** 参数。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条上，在 **Simulation** 选项卡中，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **有效长度** — 有效磁芯长度 `0.032` `m`（默认）| positive finite scalar

有效磁芯长度。此参数表示磁芯周围磁路的平均长度。

### **有效横截面积** — 有效磁芯横截面积 `1.6e-5` `m^2`（默认）| positive finite scalar

有效磁芯横截面积。此参数表示磁芯周围磁路的平均面积。

### **参数化选项** — 参数化方法 `Magnetic Characteristics`（默认）| `Jiles-Atherton Model` | `Saturated BH Curve`

用于描述 *B*-*H* 曲线的参数化方法。请选择以下选项之一：

- `Magnetic Characteristics` — 指定 *B* 和 *H* 截距的幅值，*B*r 和 *H*c，以及饱和点处 *B* 和 *H* 的幅值，*B*m 和 *H*m。
- `Jiles-Atherton Model` — 直接指定 Jiles-Atherton 参数。
- `Saturated BH Curve` — 将上升或下降 *B*-*H* 曲线制表。

### **饱和循环的剩磁** — 剩磁 `0.68` `T`（默认）| positive scalar

磁芯磁化到饱和点且外部磁场降至零后，留在磁芯中的剩磁，*Br*。此参数是 *B*-*H* 曲线与 *B* 轴相交处的磁通密度幅值。

#### 依赖关系

要启用此参数，请将 **参数化选项** 设置为 `Magnetic Characteristics`。

### **饱和循环的磁矫顽力** — 使磁芯退磁的场强幅值 `151` `A/m`（默认）| positive scalar

使磁芯退磁所需的磁场强度幅值，*Hc*。此参数是 *B*-*H* 曲线与 *H* 轴相交处的场强幅值。

要启用此参数，请将 **参数化选项** 设置为 `Magnetic Characteristics`。

### **饱和点处的磁通密度** — 最大磁通密度幅值 `1.25` `T`（默认）| positive scalar

磁芯可达到的最大磁通密度幅值，*Bm*。

要启用此参数，请将 **参数化选项** 设置为 `Magnetic Characteristics` 或 `Saturated BH Curve`。

### **饱和点处的磁场强度** — 饱和点处的场强 `3000` `A/m`（默认）| positive scalar

饱和点处的场强，*Hm*。此参数是场强幅值，在该幅值下，进一步增大 *H* 的幅值不再导致 *B* 的幅值显著增大。

要启用此参数，请将 **参数化选项** 设置为 `Magnetic Characteristics`。

### **饱和磁化强度, Ms** — 饱和磁化强度, Ms `1e6` `A/m`（默认）| positive finite scalar

Jiles-Atherton 方程中的饱和磁化强度，*M*s。

#### 依赖关系

要启用此参数，请将 **参数化选项** 设置为 `Jiles-Atherton Model`。

### **无磁滞磁化系数, a** — 无磁滞磁化系数, a `82` `A/m`（默认）| finite positive scalar

Jiles-Atherton 方程中的无磁滞磁化系数，*a*。此参数确定饱和点，并近似描述两条磁滞曲线的平均值。

#### 依赖关系

要启用此参数，请将 **参数化选项** 设置为 `Jiles-Atherton Model`。

### **域间耦合因子, alpha** — 域间耦合因子, alpha `0.0001`（默认）| scalar

Jiles-Atherton 方程中的域间耦合因子，*α*。此参数主要影响 *B*-*H* 曲线与零场强线相交的点。典型值在 `1e-4` 到 `1e-3` 范围内。

#### 依赖关系

要启用此参数，请将 **参数化选项** 设置为 `Jiles-Atherton Model`。

### **可逆磁化系数, c** — 可逆磁化系数 `0.1`（默认）| scalar in the range [0,1]

Jiles-Atherton 方程中的可逆磁化系数，*c*。此参数表示可反转的磁化比例。

#### 依赖关系

要启用此参数，请将 **参数化选项** 设置为 `Jiles-Atherton Model`。

### **体耦合系数, k** — 体耦合系数 `200` `A/m`（默认）| finite positive scalar

Jiles-Atherton 方程中的体耦合系数，*k*。此参数主要控制 *B*-*H* 曲线穿过零磁通密度线时的场强幅值。

#### 依赖关系

要启用此参数，请将 **参数化选项** 设置为 `Jiles-Atherton Model`。

### **磁通密度, B(H)** — 磁通密度向量 `[-1.25,-0.68,0,0.885,1.124,1.25]` `T`（默认）| vector

磁通密度 *B*，指定为与磁场强度向量 *H* 具有相同元素数的向量。提供沿上升曲线或下降曲线的数据点。必须至少在第一象限和第三象限中指定一个数据点。对于上升曲线，还必须在第四象限中指定至少一个点。对于下降曲线，还必须在第二象限中指定至少一个点。

#### 依赖关系

要启用此参数，请将 **参数化选项** 设置为 `Saturated BH Curve`。

### **磁场强度, H** — 磁场强度向量 `[-3000,0,151,500,1000,3000]` `A/m`（默认）| vector

磁场强度 *H*，指定为与磁通密度向量 *B* 具有相同元素数的向量。提供沿上升曲线或下降曲线的数据点。必须至少在第一象限和第三象限中指定一个数据点。对于上升曲线，还必须在第四象限中指定至少一个点。对于下降曲线，还必须在第二象限中指定至少一个点。

要启用此参数，请将 **参数化选项** 设置为 `Saturated BH Curve`。

### 损耗

### **磁滞损耗平均周期** — 磁滞损耗计算的平均周期 `1e-3` `s`（默认）| positive scalar

磁滞损耗计算的平均周期。要获得准确结果，必须指定大于 *B*-*H* 周期时间的值。如果指定较小的值，某些时刻的磁滞损耗将等于磁芯的磁能，这大于实际损耗。最佳选项是指定 *B*-*H* 周期时间的精确倍数。

### **涡流损耗建模** — 涡流损耗建模选项 `Off`（默认）| `On`

涡流损耗建模选项。

### **几何系数** — 几何系数 `6`（默认）| positive scalar

几何系数 *β*，用于考虑磁芯形状对涡流损耗的影响。对于叠片磁芯，将此参数设置为默认值 `6`。对于圆柱形磁芯，将此参数设置为 `16`。对于球形磁芯，将此参数设置为 `20`。

#### 依赖关系

要启用此参数，请选择 **涡流损耗建模** 参数。

### **叠片厚度** — 特征横截面尺寸 `1` `mm`（默认）| positive scalar

特征横截面尺寸。对于叠片磁芯，此值对应于叠片厚度。如果磁芯没有叠片，请指定对应于最宽横截面处厚度的值，例如圆柱形或球形磁芯的直径。

#### 依赖关系

要启用此参数，请选择 **涡流损耗建模** 参数。

### **电阻率** — 磁芯的电阻率 `1.03e-7` `Ohm*m`（默认）| positive scalar

磁芯的电阻率。

#### 依赖关系

要启用此参数，请选择 **涡流损耗建模** 参数。

### 热

### **热效应建模** — 热效应建模选项 `Off`（默认）| `On`

热效应建模选项。选择此参数以启用 **H** 端口。

### **热质量** — 与 H 端口关联的热质量 `2` `J/K`（默认）| positive scalar

与 **H** 端口关联的热质量。此参数表示将热端口温度升高 1 K 所需的能量。

#### 依赖关系

要启用此参数，请选择 **热效应建模** 参数。

## 所属库

Simscape / Electrical / Passive

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：提取 Jiles-Atherton 参数

如果使用磁特性或饱和 B-H 曲线参数化 Magnetic Core 模块，MATLAB 现在会在仿真开始时显示 Jiles-Atherton 参数的估计值。

Magnetic Core 模块基于磁芯为饱和铁的假设来估计 Jiles-Atherton 参数。对于其他类型的磁芯，例如具有较小矫顽力和剩磁值的铁氧体，此估计并不总是准确。现在，您可以通过使用磁特性或饱和 *B*-*H* 曲线参数化 Magnetic Core 模块来获得 Jiles-Atherton 参数的初始估计值。然后，检查预测的 *B*-*H* 曲线并调整 Jiles-Atherton 参数，以更好地拟合您的数据。有关详细信息，请参阅 Model Ferrite Core Using Magnetic Core Block 示例。

## 描述

非线性磁阻、磁滞和可选涡流损耗

Magnetic Core 模块对带磁滞的磁阻进行建模。使用此模块可对自定义电感建模并构建变压器模型。要将此模块连接到您的电气网络，请使用 Electromagnetic Converter 模块或 Winding 模块来表示电气域与磁域之间的接口。

此模块使用 Jiles-Atherton 模型计算磁通密度 *B* 和磁场强度 *H*。您可以选择直接指定 Jiles-Atherton 参数、指定特征磁参数，或使用 **参数化选项** 参数将 *B*-*H* 饱和曲线制表。

要为您所建模的磁网络部分定义几何结构，请使用 **有效长度** 和 **有效横截面积** 参数。此模块使用此几何信息将 *B* 和 *H* 映射到磁动势和磁通量，它们分别是磁域中的 Through 和 Across 变量。

要对涡流损耗建模，请在 **损耗** 设置中选择 **涡流损耗建模** 参数。要对热效应建模，请在 **热** 设置中选择 **热效应建模** 参数。

### 方程

这些方程定义磁通密度和磁动势，

B=φ/seff

mmf=leffH

其中：

- *B* 是磁芯中感应的磁通密度。
- *φ* 是磁通量。
- *seff* 是
  **Effective cross-sectional area** 参数的值。
- *mmf* 是组件两端的
  磁动势 (mmf)。
- *leff* 是
  **Effective length** 参数的值。
- *H* 是总场强。

此方程将 *B* 和 *H* 与磁芯的总磁化 *M* 相关联，

B=μ0(H+M),

其中 *μ*0 是真空磁导率。

磁化作用会增加磁通密度，其值同时取决于当前值和场强的历史。该模块使用 Jiles-Atherton [1,2] 方程确定任意给定时刻的 *M*。此图显示所得到的 *B* 和 *H* 之间关系的典型图。

此图中：

- *Bm* 是饱和点处的磁通密度。
- *Br* 是饱和循环的磁剩磁。
- *Hc* 是饱和循环的磁矫顽力。
- *Hm* 是饱和点处的磁场强度。

当场强从 *H* = 0 增加时，曲线最初沿上升磁滞曲线变化。在饱和点处，场强进一步增加不再导致磁通量显著增加。

当从饱和点降低磁场强度时，曲线沿下降磁滞曲线变化。上升曲线和下降曲线之间的差异是由于 *M* 对轨迹历史的依赖性。从物理上看，该行为对应于：随着场强增加，磁芯中的磁偶极子排列，但随后当场强减小时不会完全恢复到其原始位置。

Jiles-Atherton 方程的起点是将磁化效应分成两部分：一部分纯粹是有效场强 *Heff* 的函数，另一部分是不可逆部分，取决于历史。此方程定义无磁滞磁化 *Man* 和不可逆磁化 *Mirr* 对总磁化 *M* 的相对贡献，

M=cMan+(1−c)Mirr,

其中 *c* 是可逆磁化系数。

此方程将 *Man* 与等效磁化 *Heff* 相关联：

Man=Ms(coth(Heffa)−aHeff).

该函数定义了一条饱和曲线，其极限值为
±*Ms*，其中：

- *M*s 是 *饱和磁化*。
- *a* 是 *无磁滞磁化系数*，它决定饱和点。它近似描述两条磁滞曲线的平均值。

Jiles-Atherton 模型通过关于场强的偏导数定义不可逆项，

dMirrdH=Man−Mirrkδ−α(Man−Mirr)δ={1if dHdt≥0−1if dHdt<0

其中：

- *k* 是 *体耦合系数*，
  它塑造不可逆特性。
- *α* 是 *域间耦合因子*。

将该方程与标准一阶微分方程进行比较可知，当改变总场强 *H* 时，不可逆项
*Mirr* 试图跟踪可逆项
*Man*，但具有可变跟踪增益 1/(kδ−α(Man−Mirr))。跟踪误差在
*δ* 改变符号的点处产生磁滞。

此方程定义了无涡流损耗时无磁滞曲线的有效场强，

Heff=H+αM.

*α* 的值会影响磁滞曲线的形状。较大的值会增加 *B* 轴截距。然而，稳定性项 kδ−α(Man−Mirr) 在 *δ* > 0 时必须为正，在 *δ* < 0 时必须为负。因此，对可提供的 *α* 值存在限制。典型最大值约为 1e-3 量级。

您可以选择如何对 *B*-*H* 曲线进行参数化。
将 **Parameterization option** 参数设置为以下选项之一：

- `Jiles-Atherton Model` — 直接指定 Jiles-Atherton 参数：

  - 饱和磁化 *M*s
  - 无磁滞磁化常数 *a*
  - 域间耦合因子 *α*
  - 可逆磁化系数 *c*
  - 体耦合系数 *k*
- `Saturated BH Curve` — 以表格形式提供上升或下降 *B*-*H* 曲线。必须至少在第一和第三象限中各指定一个数据点。对于上升曲线，还必须至少在第四象限中指定一个点。对于下降曲线，还必须至少在第二象限中指定一个点。
- `Magnetic Characteristics` — 指定 *B* 和 *H* 截距的大小，即 *B*r 和 *H*c，以及饱和点处 *B* 和 *H* 的大小，即 *B*m 和 *H*m。

如果将 **Parameterization option**
参数设置为 `Magnetic characteristics` 或 `Saturated BH Curve`，MATLAB® 会在仿真开始时显示 Jiles-Atherton 参数的估计值 *（自 R2025a 起）*。

### 模型损耗

该模块计算磁滞损耗和涡流损耗。

该模块使用平均时间计算磁滞损耗。*B*-*H* 曲线内部面积的瞬时值与磁芯磁能和热功率耗散之和成正比。为获得准确结果，必须指定一个大于 *B*-*H* 周期时间的 **Averaging period for hysteresis losses** 参数值。如果指定较小的值，某些时刻的磁滞损耗将等于磁芯磁能，而这大于实际损耗。最佳选择是指定一个恰好为 *B*-*H* 周期时间精确倍数的值。

这些方程定义了在时间间隔 *Δt* [3-5] 内由涡流耗散的能量密度 *W*eddy，

Weddy=σd212β∫Δt(dBdt)2dt

dWeddydt=σd22β(dBdt)2

其中：

- *σ* 是电导率。
- *d* 是 **Thickness of laminations** 参数的值。如果磁芯没有叠片，该值对应于最宽横截面处的厚度；例如，圆柱形或球形磁芯的直径。
- *β* 是 **Geometrical coefficient** 参数的值。对于叠片磁芯，*β* = `6`。对于圆柱形磁芯，*β* = `16`。对于球形磁芯，*β* = `20` [5]。

涡流感应出磁场 *HEddy*：

HEddy=σd212βdBdt.

该磁场还会修正有效场强：

Heff=H+αM−HEddy.

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

**注意**

在 **Initial Targets** 部分中，可以为 **Field strength** 和 **Flux density** 参数指定值。提供的值必须近似对应于 *B*-*H* 曲线上的一个点。

使用标称值指定模型中变量的预期幅值。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
