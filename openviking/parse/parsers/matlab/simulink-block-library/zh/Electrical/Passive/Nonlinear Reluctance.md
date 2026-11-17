---
type: simulink-block
title: 'Nonlinear Reluctance'
family: 'passive'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'nonlinearreluctance'
documentation_source_path: 'ref/nonlinearreluctance.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear Reluctance

## 端口

### 守恒

### **N** — 北端磁性

与北端关联的磁守恒端口。

### **S** — 南端磁性

与南端关联的磁守恒端口。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条上的 **Simulation** 选项卡中，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **有效长度** — 有效核心长度 `0.032` `m`（默认）| positive finite scalar

有效核心长度。此参数表示铁心周围磁路的平均长度。

### **有效横截面积** — 有效铁心横截面积 `1.6e-5` `m^2`（默认）| positive finite scalar

有效铁心横截面积。此参数表示铁心周围磁路的平均面积。

### **功率记录平均周期** — 用于平均的激励周期 `0` `s`（默认）| scalar

用于磁滞损耗计算的平均周期。这些损耗与 *B*-*H* 轨迹围成的面积成正比。如果您以已知的固定频率激励该模块，可以将此值设置为相应的激励周期，以计算磁滞损耗。该模块每个 AC 周期一次将磁滞损耗记录到记录的仿真数据中的 `power_dissipated` 变量。如果使用固定步长求解器，此值必须是仿真步长的整数倍。

如果您不以已知的固定频率激励该模块，请将此参数设置为 `0`。该模块将记录的仿真数据中的 `power_dissipated` 变量设置为 `0`。您可以通过对记录的仿真数据中的 `power_instantaneous` 变量进行后处理来计算实际磁滞损耗。

#### 依赖关系

要启用此参数，请在 **B-H 曲线** 设置中，将 **参数化方式** 参数设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### B-H 曲线

### **参数化方式** — 参数化方法 `Reluctance (B-H curve)`（默认）| `Linear reluctance` | `Reluctance with single saturation point` | `Nonlinear reluctance with hysteresis (JA model)`

用于描述 *B*-*H* 曲线的参数化方法。请选择以下选项之一：

- `Reluctance (B-H curve)` — 通过将 *B*-*H* 曲线制成表格来建模无磁滞的磁阻。
- `Linear reluctance` — 通过指定相对磁导率来建模线性磁阻。
- `Reluctance with single saturation point` — 通过指定未饱和相对磁导率和饱和时的磁通量，建模无磁滞的开关线性磁阻。
- `Nonlinear reluctance with hysteresis (JA model)` — 通过指定 Jiles-Atherton 参数来建模带磁滞的非线性磁阻。

选择参数化方法会启用 **B-H 曲线** 设置中的相关参数。如果将此参数设置为 `Nonlinear reluctance with hysteresis (JA model)`，则会启用 **主要** 设置中的 **功率记录平均周期** 参数。

### **相对磁导率** — Relative magnetic permeability `5000`（默认）| positive finite scalar

相对磁导率。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Linear reluctance`。

### **未饱和相对磁导率** — Relative magnetic permeability `5000`（默认）| scalar

未饱和电感的相对磁导率。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Reluctance with single saturation point`。

### **饱和磁通密度** — Magnetic flux density at saturation `1.5` `T`（默认）| positive finite scalar

饱和电感的磁通密度。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Reluctance with single saturation point`。

### **磁场强度向量, H** — Magnetic field strength `[0, 200, 400, 600, 800, 1000]` `A/m`（默认）| vector

磁场强度 *H*，指定为与磁通密度 *B* 具有相同元素数量的向量。这些向量必须从零开始并单调递增。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Reluctance (B-H curve)`。

### **磁通密度向量, B** — Magnetic flux density `[0, 1.25, 1.35, 1.44, 1.48, 1.49]` `T`（默认）| vector

磁通密度 *B*，指定为与磁场强度向量 *H* 具有相同元素数量的向量。这些向量必须从零开始并单调递增。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Reluctance (B-H curve)`。

### **插值方法** — Interpolation method `Linear`（默认）| `Smooth`

该模块用于确定未指定的中间点处 *B* 和 *H* 的插值方法。请选择以下选项之一：

- `Linear` — 通过使用线性函数优先考虑性能。
- `Smooth` — 通过生成具有连续一阶导数的连续曲线优先考虑准确性。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Reluctance (B-H curve)`。

### **H 为零时的无磁滞 B-H 梯度** — Gradient of anhysteretic B-H curve around zero field strength `0.0063` `m*T/A`（默认）| scalar

零磁场强度附近无磁滞 *B*-*H* 曲线的梯度。将此参数设置为上升和下降磁滞曲线的平均梯度。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **无磁滞 B-H 曲线上的磁通密度点** — Flux density of the point for field strength measurement `1.49` `T`（默认）| scalar

用于磁场强度测量的点的磁通密度。您必须通过提供其磁通密度值来指定无磁滞曲线上的一个点。为获得准确结果，请选择高磁场强度处上升和下降磁滞曲线重合的点。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **对应磁场强度** — Field strength at measurement point `1000` `A/m`（默认）| scalar

与您使用 **无磁滞 B-H 曲线上的磁通密度点** 参数定义的点相对应的磁场强度。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **可逆磁化系数, c** — Coefficient for reversible magnetization `0.1`（默认）| scalar in the range [0,1]

Jiles-Atherton 方程中可逆磁化的系数 *c*。此参数表示可以反转的磁化比例。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **体耦合系数, K** — Jiles-Atherton equations parameter `200` `A/m`（默认）| finite positive scalar

Jiles-Atherton 方程中的体耦合系数 *K*。此参数主要控制 *B*-*H* 曲线穿过零磁通密度线时的磁场强度大小。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **域间耦合因子, alpha** — Jiles-Atherton equations parameter `0.0001`（默认）| scalar

Jiles-Atherton 方程中的域间耦合因子 *α*。此参数主要影响 *B*-*H* 曲线与零磁场强度线相交的点。典型值在 `1e-4` 到 `1e-3` 范围内。

#### 依赖关系

要启用此参数，请将 **参数化方式** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

## 所属库

Simscape / Electrical / Passive

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

带可选磁滞的线性或非线性磁阻

Nonlinear Reluctance 模块对带可选磁滞的线性或非线性磁阻进行建模。使用此模块可对自定义电感进行建模并构建变压器模型。要将此模块连接到您的电气网络，请使用 Electromagnetic Converter 模块或 Winding 模块来表示电气域和磁域之间的接口。

要为正在建模的磁网络部分定义几何结构，请使用 **有效长度** 和 **有效横截面积** 参数。该模块使用此几何信息将 *B* 和 *H* 映射到磁动势和磁通量，这些是磁域中的 Through 和 Across 变量。使用 **参数化方式** 参数选择如何参数化 *B*-*H* 曲线。

### 线性磁阻参数化的方程

线性磁阻参数化的方程为

B= μ0μrH

mmf=leffH

φ=seffB

其中：

- *B* 是磁通密度。
- μ0 是真空磁导率。
- μr 是相对磁导率。
- *H* 是磁场强度。
- *mmf* 是组件两端的磁动势（mmf）。
- *leff* 是正在建模的区段的有效长度。
- φ 是磁通量。
- *seff* 是正在建模的区段的有效横截面积。

### 单饱和点磁阻参数化的方程

此参数化方法对开关线性磁阻进行建模。在未饱和状态下，材料具有指定的相对磁导率。在饱和状态下，相对磁导率为 𝜇0。

单饱和点磁阻的方程为

mmf=leffH

φ=seffB

mmf=Rφ

如果 B<Bsat，

B= μ0μr\_unsatH.

否则，

B=Bsat+ μ0(H−Bsatμ0μr\_unsat)

其中：

- *mmf* 是组件两端的磁动势（mmf）。
- *leff* 是正在建模的区段的有效长度。
- *H* 是磁场强度。
- φ 是磁通量。
- *seff* 是正在建模的区段的有效横截面积。
- *B* 是磁通密度。
- *Bsat* 是饱和时的磁通密度。
- *Rsat* 是饱和时的磁阻。
- μ0 是真空磁导率。
- μr 是相对磁导率。
- μr\_unsat 是未饱和相对磁导率。

### 磁阻（B-H 曲线）

要通过将 *B*-*H* 曲线制成表格来建模无磁滞的磁阻，请将 **参数化方式** 参数设置为 `Reluctance (B-H curve)`。

### 磁滞参数化磁阻方程

这些方程定义磁通密度和磁动势，

B=φ/seff

mmf=leffH

其中：

- *B* 是磁芯中感应出的磁通密度。
- *φ* 是磁通量。
- *seff* 是 **有效横截面积** 参数的值。
- *mmf* 是组件两端的磁动势 (mmf)。
- *leff* 是 **有效长度** 参数的值。
- *H* 是总场强。

此方程将 *B* 和 *H* 与磁芯的总磁化强度 *M* 关联起来，

B=μ0(H+M),

其中 *μ*0 是真空磁导率。

磁化作用会增大磁通密度，其值取决于场强的当前值和历史值。该模块使用 Jiles-Atherton [1, 2] 方程来确定任意给定时刻的 *M*。下图显示了由此得到的 *B* 与 *H* 之间关系的典型曲线。

当场强从 *H* = 0 开始增大时，曲线最初沿上升磁滞曲线变化。在饱和点处，场强的进一步增大不再引起磁通量的显著增大。

当从饱和点开始减小磁场强度时，曲线沿下降磁滞曲线变化。上升曲线与下降曲线之间的差异是由于 *M* 对轨迹历史的依赖性。从物理上讲，这种行为对应于磁芯中的磁偶极子在场强增大时发生取向排列，但在场强减小时不会完全恢复到其原始位置。

Jiles-Atherton 方程的出发点是：将磁化效应分为两部分，一部分纯粹是有效场强 *Heff* 的函数，另一部分则是取决于历史的不可逆部分。此方程定义了无磁滞磁化 *Man* 和不可逆磁化 *Mirr* 对总磁化强度 *M* 的相对贡献，

M=cMan+(1−c)Mirr,

其中 *c* 是可逆磁化系数。

此方程将 *Man* 与等效磁化 *Heff* 关联起来：

Man=Ms(coth(Heffa)−aHeff).

该函数定义了一条饱和曲线，其极限值为 ±*Ms*，其中：

- *M*s 是 *饱和磁化强度*。
- *a* 是 *无磁滞磁化系数*，它决定了饱和点。它近似描述两条磁滞曲线的平均值。

在 Nonlinear Reluctance 模块封装中，您需要提供 *Heff* = 0 时 dMan/dHeff 的值，以及无磁滞 *B*-*H* 曲线上的一个点 [*H1*, *B1*]。该模块使用这些值来确定 *α* 和 *Ms* 的值。

Jiles-Atherton 模型通过关于场强的偏导数来定义不可逆项，

dMirrdH=Man−MirrKδ−α(Man−Mirr)δ={1if dHdt≥0−1if dHdt<0

其中：

- *K* 是 *体耦合系数*，它决定不可逆特性的形状。
- *α* 是 *域间耦合因子*。

将该方程与标准一阶微分方程进行比较可以看出，当改变总场强 *H* 时，不可逆项 *Mirr* 会尝试跟踪可逆项 *Man*，但带有可变跟踪增益 1/(Kδ−α(Man−Mirr))。跟踪误差会在 *δ* 改变符号的点处产生磁滞。

此方程定义无磁滞曲线的有效场强，

Heff=H+αM.

*α* 的值会影响磁滞曲线的形状。较大的值会增大 *B* 轴截距。但是，对于 *δ* > 0，稳定项 Kδ−α(Man−Mirr) 必须为正；对于 *δ* < 0，稳定项必须为负。因此，您可以提供的 *α* 值存在限制。典型最大值在 1e-3 量级。

**注意**

您还可以使用 Magnetic Core 模块对表现出非线性磁阻和磁滞的磁芯进行建模。这两个模块都使用 Jiles-Atherton 模型来确定 *B*、*H* 和 *M* 之间的关系。但是，Magnetic Core 模块提供了附加选项：

- 除了直接指定 Jiles-Atherton 参数外，您还可以使用以下选项来参数化 *B*-*H* 曲线：

  - 指定 *B* 和 *H* 截距的幅值，以及饱和点处 *B* 和 *H* 的幅值。
  - 将上升或下降 *B*-*H* 曲线制成表格。
- 您可以对涡流损耗和热效应进行建模。

**查找 Jiles-Atherton (JA) 方程系数近似值的过程**

您可以使用以下过程确定方程系数的代表值：

1. 为 **H 为零时的无磁滞 B-H 梯度** 参数提供值（当 *Heff* = 0 时的 dMan/dHeff），以及无磁滞 *B*-*H* 曲线上的数据点 [*H*1, *B1*]。根据这些值，模块初始化会确定 *α* 和 *M*s 的值。
2. 设置 **可逆磁化系数，c** 参数，以在从 [*H* *B*] = [0 0] 开始仿真时获得正确的初始 *B*-*H* 梯度。*c* 的值大约是该初始梯度与 **H 为零时的无磁滞 B-H 梯度** 的比值。*c* 的值必须大于 0 且小于 1。
3. 将 **体耦合系数，K** 参数设置为上升磁滞曲线上 *B* = 0 时 *H* 的近似幅值。
4. 为 **域间耦合因子，alpha** 参数设置一个非常小的值，然后逐渐增大它，以调整穿过 *H* = 0 线时的 *B* 值。典型值在 1e-4 到 1e-3 范围内。值过大会导致 *B*-*H* 曲线的梯度趋于无穷大，这是非物理的，并会产生运行时断言错误。

要获得与预定义 *B*-*H* 曲线的良好匹配，请迭代这四个步骤。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关更多信息，请参阅为模块变量设置优先级和初始目标。

使用标称值来指定模型中变量的预期幅值。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **标称值** 部分。有关更多信息，请参阅按标称值进行系统缩放。
