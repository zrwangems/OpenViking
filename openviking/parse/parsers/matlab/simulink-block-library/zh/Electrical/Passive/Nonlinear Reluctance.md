---
type: simulink-block
title: 'Nonlinear Reluctance'
family: 'sps'
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
```yaml
ports:
- name: N
  summary: 北端磁端口
  direction: conserving
- name: S
  summary: 南端磁端口
  direction: conserving
```

### 守恒端口

### **N** — 北端磁端口

与北端关联的磁守恒端口。

### **S** — 南端磁端口

与南端关联的磁守恒端口。
## 参数
```yaml
parameters:
- name: Effective length
  summary: 有效磁芯长度 0.032 m（默认值）| 正有限标量
  group: 主要
- name: Effective cross-sectional area
  summary: 有效磁芯横截面积 1.6e-5 m^2（默认值）| 正有限标量
  group: 主要
- name: Averaging period for power logging
  summary: 用于平均的激励周期 0 s（默认值）| 标量
  group: 主要
- name: Parameterized by
  summary: 参数化方法 Reluctance (B-H curve)（默认值）| Linear reluctance | Reluctance with single saturation point | Nonlinear reluctance
    with hysteresis (JA model)
  group: B-H 曲线
- name: Relative magnetic permeability
  summary: 相对磁导率 5000（默认值）| 正有限标量
  group: B-H 曲线
- name: Unsaturated relative magnetic permeability
  summary: 相对磁导率 5000（默认值）| 标量
  group: B-H 曲线
- name: Magnetic flux density at saturation
  summary: 饱和时的磁通密度 1.5 T（默认值）| 正有限标量
  group: B-H 曲线
- name: Magnetic field strength vector, H
  summary: 磁场强度 [0, 200, 400, 600, 800, 1000] A/m（默认值）| 向量
  group: B-H 曲线
- name: Magnetic flux density vector, B
  summary: 磁通密度 [0, 1.25, 1.35, 1.44, 1.48, 1.49] T（默认值）| 向量
  group: B-H 曲线
- name: Interpolation method
  summary: 插值方法 Linear（默认值）| Smooth
  group: B-H 曲线
- name: Anhysteretic B-H gradient when H is zero
  summary: 零场强附近无磁滞 B-H 曲线的梯度 0.0063 m*T/A（默认值）| 标量
  group: B-H 曲线
- name: Flux density point on anhysteretic B-H curve
  summary: 用于场强测量的点的磁通密度 1.49 T（默认值）| 标量
  group: B-H 曲线
- name: Corresponding field strength
  summary: 测量点处的场强 1000 A/m（默认值）| 标量
  group: B-H 曲线
- name: Coefficient for reversible magnetization, c
  summary: 可逆磁化系数 0.1（默认值）| 范围 [0,1] 内的标量
  group: B-H 曲线
- name: Bulk coupling coefficient, K
  summary: Jiles-Atherton 方程参数 200 A/m（默认值）| 有限正标量
  group: B-H 曲线
- name: Inter-domain coupling factor, alpha
  summary: Jiles-Atherton 方程参数 0.0001（默认值）| 标量
  group: B-H 曲线
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### 主要

### **Effective length** — 有效磁芯长度 `0.032` `m`（默认值）| 正有限标量

有效磁芯长度。此参数表示磁芯周围磁路的平均长度。

### **Effective cross-sectional area** — 有效磁芯横截面积 `1.6e-5` `m^2`（默认值）| 正有限标量

有效磁芯横截面积。此参数表示磁芯周围磁路的平均面积。

### **Averaging period for power logging** — 用于平均的激励周期 `0` `s`（默认值）| 标量

用于磁滞损耗计算的平均周期。这些损耗与 *B*-*H* 轨迹所包围的面积成正比。如果您以已知的固定频率激励该模块，可以将此值设置为相应的激励周期以计算磁滞损耗。该模块在每个交流周期将磁滞损耗记录到记录的仿真数据中的 `power_dissipated` 变量中。如果您使用的是定步长求解器，此值必须是仿真步长的整数倍。

如果您不以已知的固定频率激励该模块，请将此参数设置为 `0`。该模块将记录的仿真数据中的 `power_dissipated` 变量设置为 `0`。您可以通过后处理记录的仿真数据中的 `power_instantaneous` 变量来计算实际的磁滞损耗。

#### 依赖关系

要启用此参数，请在 **B-H Curve** 设置中将 **Parameterized by** 参数设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### B-H 曲线

### **Parameterized by** — 参数化方法 `Reluctance (B-H curve)`（默认值）| `Linear reluctance` | `Reluctance with single saturation point` | `Nonlinear reluctance with hysteresis (JA model)`

用于描述 *B*-*H* 曲线的参数化方法。请选择以下选项之一：

- `Reluctance (B-H curve)` — 通过将 *B*-*H* 曲线制表来建模无磁滞的磁阻。
- `Linear reluctance` — 通过指定相对磁导率来建模线性磁阻。
- `Reluctance with single saturation point` — 通过指定未饱和相对磁导率和饱和时的磁通密度来建模无磁滞的开关线性磁阻。
- `Nonlinear reluctance with hysteresis (JA model)` — 通过指定 Jiles-Atherton 参数来建模带磁滞的非线性磁阻。

选择参数化方法会启用 **B-H Curve** 设置中的相关参数。如果您将此参数设置为 `Nonlinear reluctance with hysteresis (JA model)`，则会启用 **Main** 设置中的 **Averaging period for power logging** 参数。

### **Relative magnetic permeability** — 相对磁导率 `5000`（默认值）| 正有限标量

相对磁导率。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Linear reluctance`。

### **Unsaturated relative magnetic permeability** — 相对磁导率 `5000`（默认值）| 标量

未饱和电感器的相对磁导率。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Reluctance with single saturation point`。

### **Magnetic flux density at saturation** — 饱和时的磁通密度 `1.5` `T`（默认值）| 正有限标量

饱和电感器的磁通密度。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Reluctance with single saturation point`。

### **Magnetic field strength vector, H** — 磁场强度 `[0, 200, 400, 600, 800, 1000]` `A/m`（默认值）| 向量

磁场强度 *H*，指定为与磁通密度 *B* 具有相同元素数量的向量。这些向量必须以零开头并单调递增。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Reluctance (B-H curve)`。

### **Magnetic flux density vector, B** — 磁通密度 `[0, 1.25, 1.35, 1.44, 1.48, 1.49]` `T`（默认值）| 向量

磁通密度 *B*，指定为与磁场强度向量 *H* 具有相同元素数量的向量。这些向量必须以零开头并单调递增。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Reluctance (B-H curve)`。

### **Interpolation method** — 插值方法 `Linear`（默认值）| `Smooth`

该模块用于确定未指定的中间点处的 *B* 和 *H* 的插值方法。请选择以下选项之一：

- `Linear` — 通过使用线性函数优先考虑性能。
- `Smooth` — 通过生成具有连续一阶导数的连续曲线优先考虑精度。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Reluctance (B-H curve)`。

### **Anhysteretic B-H gradient when H is zero** — 零场强附近无磁滞 B-H 曲线的梯度 `0.0063` `m*T/A`（默认值）| 标量

零场强附近无磁滞 *B*-*H* 曲线的梯度。将此参数设置为上升和下降磁滞曲线的平均梯度。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **Flux density point on anhysteretic B-H curve** — 用于场强测量的点的磁通密度 `1.49` `T`（默认值）| 标量

用于场强测量的点的磁通密度。您必须通过提供磁通密度值来指定无磁滞曲线上的一个点。为获得准确结果，请选择高场强处上升和下降磁滞曲线重合的点。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **Corresponding field strength** — 测量点处的场强 `1000` `A/m`（默认值）| 标量

与您使用 **Flux density point on anhysteretic B-H curve** 参数定义的点相对应的场强。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **Coefficient for reversible magnetization, c** — 可逆磁化系数 `0.1`（默认值）| 范围 [0,1] 内的标量

Jiles-Atherton 方程中的可逆磁化系数 *c*。此参数表示可以可逆的磁化比例。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **Bulk coupling coefficient, K** — Jiles-Atherton 方程参数 `200` `A/m`（默认值）| 有限正标量

Jiles-Atherton 方程中的体耦合系数 *K*。此参数主要控制 *B*-*H* 曲线穿过零磁通密度线时的场强幅值。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。

### **Inter-domain coupling factor, alpha** — Jiles-Atherton 方程参数 `0.0001`（默认值）| 标量

Jiles-Atherton 方程中的域间耦合因子 *α*。此参数主要影响 *B*-*H* 曲线与零场强线相交的点。典型值在 `1e-4` 到 `1e-3` 范围内。

#### 依赖关系

要启用此参数，请将 **Parameterized by** 设置为 `Nonlinear reluctance with hysteresis (JA model)`。
## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

带可选磁滞的线性或非线性磁阻

Nonlinear Reluctance 模块对带可选磁滞的线性或非线性磁阻进行建模。使用此模块可以建模自定义电感并构建变压器模型。要将此模块连接到您的电气网络，请使用 Electromagnetic Converter 模块或 Winding 模块来表示电气域和磁域之间的接口。

要为您正在建模的磁网络部分定义几何形状，请使用 **Effective length** 和 **Effective cross-sectional area** 参数。该模块使用此几何信息将 *B* 和 *H* 映射为磁动势和磁通量，它们是磁域中的 Through 和 Across 变量。使用 **Parameterized by** 参数选择如何参数化 *B*-*H* 曲线。

### 线性磁阻参数化的方程

线性磁阻参数化的方程为

B= μ0μrH

mmf=leffH

φ=seffB

其中：

- *B* 是磁通密度。
- μ0 是真空中的磁导率。
- μr 是相对磁导率。
- *H* 是场强。
- *mmf* 是组件两端的磁动势（mmf）。
- *leff* 是正在建模的区段的有效长度。
- φ 是磁通量。
- *seff* 是正在建模的区段的有效横截面积。

### 单饱和点磁阻参数化的方程

此参数化对开关线性磁阻进行建模。在未饱和状态下，材料具有指定的相对磁导率。在饱和状态下，相对磁导率为 𝜇0。

单饱和点磁阻的方程为

mmf=leffH

φ=seffB

mmf=Rφ

如果 B<Bsat，

B= μ0μr\_unsatH。

否则，

B=Bsat+ μ0(H−Bsatμ0μr\_unsat)

其中：

- *mmf* 是组件两端的磁动势（mmf）。
- *leff* 是正在建模的区段的有效长度。
- *H* 是场强。
- φ 是磁通量。
- *seff* 是正在建模的区段的有效横截面积。
- *B* 是磁通密度。
- *Bsat* 是饱和时的磁通密度。
- *Rsat* 是饱和时的磁阻。
- μ0 是真空中的磁导率。
- μr 是相对磁导率。
- μr\_unsat 是未饱和相对磁导率。

### 磁阻（B-H 曲线）

要通过将 *B*-*H* 曲线制表来建模无磁滞的磁阻，请将 **Parameterized by** 参数设置为 `Reluctance (B-H curve)`。

### 磁滞参数化磁阻方程

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

其中 *μ*0 是真空磁导率。

磁化作用会增加磁通密度，其值取决于磁场强度的当前值和历史值。该模块使用 Jiles-Atherton [1, 2] 方程来确定任意给定时刻的 *M*。下图显示了由此得到的 *B* 与 *H* 之间关系的典型曲线图。

当磁场强度从 *H* = 0 开始增加时，曲线最初沿上升磁滞曲线变化。在饱和点，磁场强度的进一步增加不再导致磁通量的显著增加。

当您从饱和点降低磁场强度时，曲线沿下降磁滞曲线变化。上升曲线和下降曲线之间的差异是由于 *M* 对轨迹历史的依赖性。从物理上讲，这种行为对应于铁芯中的磁偶极子随着磁场强度的增加而排列，但当磁场强度减小时，它们不会完全恢复到原始位置。

Jiles-Atherton 方程的起点是将磁化效应分为两部分，一部分是有效磁场强度 *Heff* 的纯函数，另一部分是不可逆部分，取决于历史。此方程定义了非磁滞磁化 *Man* 和不可逆磁化 *Mirr* 对总磁化强度 *M* 的相对贡献，

M=cMan+(1−c)Mirr，

其中 *c* 是可逆磁化系数。

此方程将 *Man* 与等效磁化强度 *Heff* 关联起来：

Man=Ms(coth(Heffa)−aHeff)。

该函数定义了一条饱和曲线，其极限值为 ±*Ms*，其中：

- *M*s 是 *饱和磁化强度*。
- *a* 是 *非磁滞磁化系数*，它决定了饱和点。它近似描述了两条磁滞曲线的平均值。

在 Nonlinear Reluctance 模块掩膜中，您需要提供当 *Heff* = 0 时的 dMan/dHeff 值，以及非磁滞 *B*-*H* 曲线上的一个点 [*H1*, *B1*]。该模块使用这些值来确定 *α* 和 *Ms* 的值。

Jiles-Atherton 模型通过关于磁场强度的偏导数来定义不可逆项，

dMirrdH=Man−MirrKδ−α(Man−Mirr)δ={1if dHdt≥0−1if dHdt<0

其中：

- *K* 是 *体耦合系数*，它决定了不可逆特性的形状。
- *α* 是 *域间耦合因子*。

将该方程与标准一阶微分方程进行比较可以发现，当您改变总磁场强度 *H* 时，不可逆项 *Mirr* 试图跟踪可逆项 *Man*，但具有可变跟踪增益 1/(Kδ−α(Man−Mirr))。跟踪误差在 *δ* 改变符号的点处产生磁滞。

此方程定义了非磁滞曲线的有效磁场强度，

Heff=H+αM。

*α* 的值影响磁滞曲线的形状。较大的值会增加 *B* 轴截距。然而，稳定性项 Kδ−α(Man−Mirr) 对于 *δ* > 0 必须为正，对于 *δ* < 0 必须为负。因此，您可以提供的 *α* 值存在限制。典型的最大值约为 1e-3。

**注意**

您也可以使用 Magnetic Core 模块来对表现出非线性磁阻和磁滞的磁芯进行建模。这两个模块都使用 Jiles-Atherton 模型来确定 *B*、*H* 和 *M* 之间的关系。但是，Magnetic Core 模块为您提供了额外的选项：

- 除了直接指定 Jiles-Atherton 参数外，您还可以使用以下选项来参数化 *B*-*H* 曲线：

  - 指定 *B* 和 *H* 截距的大小以及饱和点处 *B* 和 *H* 的大小。
  - 将上升或下降 *B*-*H* 曲线制成表格。
- 您可以对涡流损耗和热效应进行建模。

**寻找 Jiles-Atherton (JA) 方程系数近似值的步骤**

您可以使用以下步骤来确定方程系数的代表性值：

1. 为 **Anhysteretic B-H gradient when H is zero** 参数（当 *Heff* = 0 时的 dMan/dHeff）提供一个值，以及非磁滞 *B*-*H* 曲线上的一个数据点 [*H*1, *B1*]。根据这些值，模块初始化会确定 *α* 和 *M*s 的值。
2. 设置 **Coefficient for reversible magnetization, c** 参数，以在从 [*H* *B*] = [0 0] 开始仿真时获得正确的初始 *B*-*H* 梯度。*c* 的值大约是该初始梯度与 **Anhysteretic B-H gradient when H is zero** 的比值。*c* 的值必须大于 0 且小于 1。
3. 将 **Bulk coupling coefficient, K** 参数设置为上升磁滞曲线上 *B* = 0 时 *H* 的近似大小。
4. 从 **Inter-domain coupling factor, alpha** 参数的一个非常小的值开始，然后逐渐增大它以调整穿过 *H* = 0 线时的 *B* 值。典型值在 1e-4 到 1e-3 的范围内。过大的值会导致 *B*-*H* 曲线的梯度趋于无穷大，这是非物理的，并会产生运行时断言错误。

要获得与预定义 *B*-*H* 曲线的良好匹配，请对这四个步骤进行迭代。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期大小。使用基于标称值的系统缩放可以提高仿真的鲁棒性。标称值可以来自不同的来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
