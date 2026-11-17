---
type: simulink-block
title: 'Magnetic Core'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'magneticcore'
documentation_source_path: 'ref/magneticcore.html'
language: zh-CN
chinese_source: worker-translation
---

# Magnetic Core

## 端口

### 守恒端口

### **N** — 北端磁端口

与北端关联的磁守恒端口。

### **S** — 南端磁端口

与南端关联的磁守恒端口。

### **H** — 热质量热端口

与热质量关联的热端口。

#### 依赖关系

要启用此端口，请选中 **Model thermal effects** 参数。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Effective length** — 有效磁芯长度 `0.032` `m`（默认）| 正有限标量

有效磁芯长度。此参数表示磁芯周围磁路的平均长度。

### **Effective cross-sectional area** — 有效磁芯横截面积 `1.6e-5` `m^2`（默认）| 正有限标量

有效磁芯横截面积。此参数表示磁芯周围磁路的平均面积。

### **Parameterization option** — 参数化方法 `Magnetic Characteristics`（默认）| `Jiles-Atherton Model` | `Saturated BH Curve`

用于描述 *B*-*H* 曲线的参数化方法。请选择以下选项之一：

- `Magnetic Characteristics` — 指定 *B* 和 *H* 截距的幅值 *B*r 和 *H*c，以及饱和点处 *B* 和 *H* 的幅值 *B*m 和 *H*m。
- `Jiles-Atherton Model` — 直接指定 Jiles-Atherton 参数。
- `Saturated BH Curve` — 将上升或下降的 *B*-*H* 曲线制成表格。

### **Magnetic remanence of saturation cycle** — 剩磁 `0.68` `T`（默认）| 正标量

磁芯磁化至饱和点且外部磁场减小至零后残留在磁芯中的剩磁 *Br*。此参数是 *B*-*H* 曲线与 *B* 轴相交处的磁通密度幅值。

#### 依赖关系

要启用此参数，请将 **Parameterization option** 设置为 `Magnetic Characteristics`。

### **Magnetic coercivity of saturation cycle** — 使磁芯退磁的磁场强度幅值 `151` `A/m`（默认）| 正标量

使磁芯退磁所需的磁场强度幅值 *Hc*。此参数是 *B*-*H* 曲线与 *H* 轴相交处的场强幅值。

要启用此参数，请将 **Parameterization option** 设置为 `Magnetic Characteristics`。

### **Magnetic flux density at saturation point** — 最大磁通密度幅值 `1.25` `T`（默认）| 正标量

磁芯可达到的最大磁通密度幅值 *Bm*。

要启用此参数，请将 **Parameterization option** 设置为 `Magnetic Characteristics` 或 `Saturated BH Curve`。

### **Magnetic field intensity at saturation point** — 饱和点处的场强 `3000` `A/m`（默认）| 正标量

饱和点处的场强 *Hm*。此参数是这样一个场强幅值：当 *H* 的幅值进一步增加时，*B* 的幅值不再显著增加。

要启用此参数，请将 **Parameterization option** 设置为 `Magnetic Characteristics`。

### **Saturation magnetization, Ms** — 饱和磁化强度，Ms `1e6` `A/m`（默认）| 正有限标量

Jiles-Atherton 方程中的饱和磁化强度 *M*s。

#### 依赖关系

要启用此参数，请将 **Parameterization option** 设置为 `Jiles-Atherton Model`。

### **Anhysteretic magnetization coefficient, a** — 无磁滞磁化系数，a `82` `A/m`（默认）| 有限正标量

Jiles-Atherton 方程中的无磁滞磁化系数 *a*。此参数决定饱和点，并近似描述两条磁滞曲线的平均值。

#### 依赖关系

要启用此参数，请将 **Parameterization option** 设置为 `Jiles-Atherton Model`。

### **Inter-domain coupling factor, alpha** — 域间耦合因子，alpha `0.0001`（默认）| 标量

Jiles-Atherton 方程中的域间耦合因子 *α*。此参数主要影响 *B*-*H* 曲线与零场强线相交的点。典型值在 `1e-4` 到 `1e-3` 范围内。

#### 依赖关系

要启用此参数，请将 **Parameterization option** 设置为 `Jiles-Atherton Model`。

### **Coefficient for reversible magnetization, c** — 可逆磁化系数 `0.1`（默认）| [0,1] 范围内的标量

Jiles-Atherton 方程中的可逆磁化系数 *c*。此参数表示可逆磁化的比例。

#### 依赖关系

要启用此参数，请将 **Parameterization option** 设置为 `Jiles-Atherton Model`。

### **Bulk coupling coefficient, k** — 体耦合系数 `200` `A/m`（默认）| 有限正标量

Jiles-Atherton 方程中的体耦合系数 *k*。此参数主要控制 *B*-*H* 曲线穿过零磁通密度线时的场强幅值。

#### 依赖关系

要启用此参数，请将 **Parameterization option** 设置为 `Jiles-Atherton Model`。

### **Magnetic flux density, B(H)** — 磁通密度向量 `[-1.25,-0.68,0,0.885,1.124,1.25]` `T`（默认）| 向量

磁通密度 *B*，指定为与磁场强度向量 *H* 具有相同元素数量的向量。提供沿上升曲线或下降曲线的数据点。您必须在第一象限和第三象限中至少指定一个数据点。对于上升曲线，您还必须在第四象限中至少指定一个点。对于下降曲线，您还必须在第二象限中至少指定一个点。

#### 依赖关系

要启用此参数，请将 **Parameterization option** 设置为 `Saturated BH Curve`。

### **Magnetic field intensity, H** — 磁场强度向量 `[-3000,0,151,500,1000,3000]` `A/m`（默认）| 向量

磁场强度 *H*，指定为与磁通密度向量 *B* 具有相同元素数量的向量。提供沿上升曲线或下降曲线的数据点。您必须在第一象限和第三象限中至少指定一个数据点。对于上升曲线，您还必须在第四象限中至少指定一个点。对于下降曲线，您还必须在第二象限中至少指定一个点。

要启用此参数，请将 **Parameterization option** 设置为 `Saturated BH Curve`。

### 损耗

### **Averaging period for hysteresis losses** — 磁滞损耗计算的平均周期 `1e-3` `s`（默认）| 正标量

磁滞损耗计算的平均周期。为获得准确结果，您必须指定大于 *B*-*H* 循环时间的值。如果指定较小的值，某些时刻的磁滞损耗将等于磁芯的磁能，这大于实际损耗。最佳选择是指定 *B*-*H* 循环时间的精确倍数。

### **Model eddy losses** — 对涡流损耗建模的选项 `Off`（默认）| `On`

对涡流损耗建模的选项。

### **Geometrical coefficient** — 几何系数 `6`（默认）| 正标量

几何系数 *β*，用于考虑磁芯形状对涡流损耗的影响。对于叠片磁芯，将此参数设置为默认值 `6`。对于圆柱形磁芯，将此参数设置为 `16`。对于球形磁芯，将此参数设置为 `20`。

#### 依赖关系

要启用此参数，请选中 **Model eddy losses** 参数。

### **Thickness of laminations** — 特征横截面尺寸 `1` `mm`（默认）| 正标量

特征横截面尺寸。对于叠片磁芯，此值对应于叠片的厚度。如果磁芯没有叠片，请指定对应于最宽横截面处的厚度值，例如圆柱形或球形磁芯的直径。

#### 依赖关系

要启用此参数，请选中 **Model eddy losses** 参数。

### **Electrical resistivity** — 磁芯电阻率 `1.03e-7` `Ohm*m`（默认）| 正标量

磁芯的电阻率。

#### 依赖关系

要启用此参数，请选中 **Model eddy losses** 参数。

### 热

### **Model thermal effects** — 对热效应建模的选项 `Off`（默认）| `On`

对热效应建模的选项。选中此参数以启用 **H** 端口。

### **Thermal mass** — 与 H 端口关联的热质量 `2` `J/K`（默认）| 正标量

与 **H** 端口关联的热质量。此参数表示将热端口温度升高 1 K 所需的能量。

#### 依赖关系

要启用此参数，请选中 **Model thermal effects** 参数。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：提取 Jiles-Atherton 参数

如果您使用磁特性或饱和 B-H 曲线对 Magnetic Core 模块进行参数化，MATLAB 现在会在仿真开始时显示 Jiles-Atherton 参数的估计值。

Magnetic Core 模块基于磁芯为饱和铁的假设来估计 Jiles-Atherton 参数。对于其他类型的磁芯（例如矫顽力和剩磁值较小的铁氧体），此估计并不总是准确。您现在可以通过使用磁特性或饱和 *B*-*H* 曲线对 Magnetic Core 模块进行参数化来获得 Jiles-Atherton 参数的初始估计值。然后，检查预测的 *B*-*H* 曲线并调整 Jiles-Atherton 参数，以更好地拟合您的数据。有关详细信息，请参阅 Model Ferrite Core Using Magnetic Core Block 示例。

## 描述

非线性磁阻、磁滞和可选涡流损耗

Magnetic Core 模块对带磁滞的磁阻进行建模。使用此模块可对自定义电感进行建模并构建变压器模型。要将此模块连接到您的电气网络，请使用 Electromagnetic Converter 模块或 Winding 模块来表示电气域和磁域之间的接口。

该模块使用 Jiles-Atherton 模型来计算磁通密度 *B* 和磁场强度 *H*。您可以选择直接指定 Jiles-Atherton 参数、指定特征磁参数，或使用 **Parameterization option** 参数将 *B*-*H* 饱和曲线制成表格。

要定义您所建模的磁网络部分的几何形状，请使用 **Effective length** 和 **Effective cross-sectional area** 参数。该模块使用此几何信息将 *B* 和 *H* 映射为磁动势和磁通，它们是磁域中的 Through 和 Across 变量。

要对涡流损耗建模，请在 **Losses** 设置中选中 **Model eddy losses** 参数。要对热效应建模，请在 **Thermal** 设置中选中 **Model thermal effects** 参数。

### 方程

这些方程定义了磁通密度和磁动势，

B=φ/seff

mmf=leffH

其中：

- *B* 是铁芯中感应的磁通密度。
- *φ* 是磁通量。
- *seff* 是 **Effective cross-sectional area** 参数的值。
- *mmf* 是组件两端的磁动势（mmf）。
- *leff* 是 **Effective length** 参数的值。
- *H* 是总磁场强度。

此方程将 *B* 和 *H* 与铁芯的总磁化强度 *M* 关联起来，

B=μ0(H+M)，

其中 *μ*0 是真空的磁导率。

磁化作用会增加磁通密度，其值取决于磁场强度的当前值和历史值。该模块使用 Jiles-Atherton [1,2] 方程来确定任意给定时刻的 *M*。下图显示了 *B* 和 *H* 之间所得关系的典型曲线。

在此图中：

- *Bm* 是饱和点处的磁通密度。
- *Br* 是饱和循环的磁剩磁。
- *Hc* 是饱和循环的磁矫顽力。
- *Hm* 是饱和点处的磁场强度。

当磁场强度从 *H* = 0 开始增加时，曲线最初沿上升磁滞曲线变化。在饱和点处，磁场强度的进一步增加不再导致磁通量的显著增加。

当您从饱和点降低磁场强度时，曲线沿下降磁滞曲线变化。上升曲线和下降曲线之间的差异是由于 *M* 对轨迹历史的依赖性。从物理上讲，这种行为对应于铁芯中的磁偶极子随着磁场强度的增加而排列，但当磁场强度减小时并未完全恢复到其原始位置。

Jiles-Atherton 方程的起点是将磁化效应分为两部分，一部分纯粹是有效磁场强度 *Heff* 的函数，另一部分是不可逆的，取决于历史。此方程定义了无磁滞磁化 *Man* 和不可逆磁化 *Mirr* 对总磁化强度 *M* 的相对贡献，

M=cMan+(1−c)Mirr，

其中 *c* 是可逆磁化系数。

此方程将 *Man* 与等效磁化强度 *Heff* 关联起来：

Man=Ms(coth(Heffa)−aHeff)。

该函数定义了一条饱和曲线，其极限值为 ±*Ms*，其中：

- *M*s 是*饱和磁化强度*。
- *a* 是*无磁滞磁化系数*，它决定了饱和点。它近似描述了两条磁滞曲线的平均值。

Jiles-Atherton 模型通过关于磁场强度的偏导数来定义不可逆项，

dMirrdH=Man−Mirrkδ−α(Man−Mirr)δ={1if dHdt≥0−1if dHdt<0

其中：

- *k* 是*体耦合系数*，它决定了不可逆特性的形状。
- *α* 是*域间耦合因子*。

将该方程与标准一阶微分方程进行比较可以看出，当您改变总磁场强度 *H* 时，不可逆项 *Mirr* 试图跟踪可逆项 *Man*，但具有可变跟踪增益 1/(kδ−α(Man−Mirr))。跟踪误差在 *δ* 改变符号的点处产生磁滞。

此方程定义了无涡流损耗时无磁滞曲线的有效磁场强度，

Heff=H+αM。

*α* 的值影响磁滞曲线的形状。较大的值会增加 *B* 轴截距。然而，稳定性项 kδ−α(Man−Mirr) 对于 *δ* > 0 必须为正，对于 *δ* < 0 必须为负。因此，您可以提供的 *α* 值存在限制。典型的最大值约为 1e-3。

您可以选择如何参数化 *B*-*H* 曲线。将 **Parameterization option** 参数设置为以下选项之一：

- `Jiles-Atherton Model` — 直接指定 Jiles-Atherton 参数：

  - 饱和磁化强度 *M*s
  - 无磁滞磁化常数 *a*
  - 域间耦合因子 *α*
  - 可逆磁化系数 *c*
  - 体耦合系数 *k*
- `Saturated BH Curve` — 将上升或下降 *B*-*H* 曲线制成表格。您必须在第一象限和第三象限中至少指定一个数据点。对于上升曲线，您还必须在第四象限中至少指定一个点。对于下降曲线，您还必须在第二象限中至少指定一个点。
- `Magnetic Characteristics` — 指定 *B* 和 *H* 截距的大小，*B*r 和 *H*c，以及饱和点处 *B* 和 *H* 的大小，*B*m 和 *H*m。

如果您将 **Parameterization option** 参数设置为 `Magnetic characteristics` 或 `Saturated BH Curve`，MATLAB® 会在仿真开始时显示 Jiles-Atherton 参数的估计值 *(自 R2025a 起)*。

### 模型损耗

该模块计算磁滞损耗和涡流损耗。

该模块使用平均时间来计算磁滞损耗。*B*-*H* 曲线内部面积的瞬时值与铁芯的磁能和热功率耗散之和成正比。为获得准确结果，您必须指定一个大于 *B*-*H* 循环时间的 **Averaging period for hysteresis losses** 参数值。如果您指定较小的值，某些时刻的磁滞损耗将等于铁芯的磁能，这大于实际损耗。最佳选择是指定一个恰好为 *B*-*H* 循环时间整数倍的值。

这些方程定义了在时间间隔 *Δt* 内由涡流耗散的能量密度 *W*eddy [3-5]，

Weddy=σd212β∫Δt(dBdt)2dt

dWeddydt=σd22β(dBdt)2

其中：

- *σ* 是电导率。
- *d* 是 **Thickness of laminations** 参数的值。如果铁芯没有叠片，此值对应于最宽横截面处的厚度；例如，圆柱形或球形铁芯的直径。
- *β* 是 **Geometrical coefficient** 参数的值。对于叠片铁芯，*β* = `6`。对于圆柱形铁芯，*β* = `16`。对于球形铁芯，*β* = `20` [5]。

涡流感应出磁场 *HEddy*：

HEddy=σd212βdBdt。

该磁场还会修改有效磁场强度：

Heff=H+αM−HEddy。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

**注意**

在 **Initial Targets** 部分中，您可以为 **Field strength** 和 **Flux density** 参数指定值。您提供的值必须大致对应于 *B*-*H* 曲线上的一个点。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
