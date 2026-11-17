---
type: simulink-block
title: 'Spool Orifice (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Orifices'
documentation_page: 'spoolorificeil'
documentation_source_path: 'ref/spoolorificeil.html'
language: zh-CN
chinese_source: worker-translation
---

# Spool Orifice (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

液体进入或离开节流口的端口。

### **B** — 液体端口，等温液体

液体进入或离开节流口的端口。
### 输入

### **S** — 控制构件位移，m，物理信号

可变面积节流口的控制构件位移，单位为 m。
### 输出

### **F** — 液动力，N，物理信号

轴向液动力，单位为 N。

## 参数

### **Orifice parameterization** — 节流口类型 `Round holes`（默认）| `Rectangular slot`

套筒中的孔几何形状。圆孔沿横截面圆周均匀分布。在 `Rectangular
slot` 设置中只有一个槽。

### **Diameter of round holes** — 圆孔直径 `5e-3 m`（默认）| 正标量

套筒上所有孔的直径。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Round
holes`。

### **Number of round holes** — 圆孔数量 `6`（默认）| 正整数

沿套筒圆周的孔数量。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Round
holes`。

### **Orifice width** — 矩形槽宽度 `0.01 m`（默认）| 正标量

矩形槽宽度。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Rectangular
slot`。

### **Spool travel between closed and open orifice** — 控制构件最大行程 `5e-3 m`（默认）| 正标量

控制构件行程的最大距离。该值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **Orifice
parametrization** 设置为 `Rectangular
slot`。

### **Flow force output** — 是否对阀芯上的轴向液压力建模 `off`（默认）| `on`

是否对阀芯上的轴向液压力建模。选择此参数后，端口 **F** 启用，并输出轴向力作为物理信号，单位为 N。

### **Radial clearance** — 阀芯-套筒间隙 `1e-5 m`（默认）| 正标量

阀芯与套筒之间的径向距离。

#### 依赖关系

要启用此参数，请选择 **Flow force output**。

### **Leakage area** — 阀处于全关闭位置时的间隙面积 `1e-10` m^2（默认）| 正标量

阀处于全关闭位置时所有间隙的总和。任何小于此值的面积都会被饱和到指定的泄漏面积。这通过保持流动的连续性来帮助数值稳定性。

### **Spool position at closed orifice** — 阀芯偏移 `0`（默认）| 标量

节流口全开时的阀芯偏移。正的、非零值表示部分关闭的节流口。负的、非零值表示重叠的节流口，该节流口在端口 **S** 处物理信号设定的初始位移下保持打开。

### **Cross-sectional area at ports A and B** — 守恒端口处的节流口面积 `inf m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。该面积用于确定通过节流口质量流量的压力-流量方程中。

### **Opening orientation** — 节流口面积变化方向 `Positive spool displacement opens the orifice`（默认）| `Negative spool displacement opens the orifice`

可变节流口面积变化的方向。正开口方向表示节流口开度增加。负方向表示节流口开度减小。幅值始终为正。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| [0,1] 范围内的正标量

考虑理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过节流口的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当节流口处于接近打开或接近关闭位置时，引入一层逐渐变化的流动响应。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中的可变面积阀芯节流口

Spool Orifice (IL) 模块对阀芯和带孔套筒之间的可变面积节流口进行建模。套筒孔可以是一系列圆孔或矩形孔。流量基于套筒、孔和阀芯之间的总开口面积，该面积根据端口 **S** 处接收的信号而伸出或缩回。可以沿阀芯-套筒对连接多个 Spool Orifice (IL) 模块以对应多组孔。

如果系统中的阀芯位移由外部源或自定义模块提供，并且您希望将轴向液动力传递到系统，则可以使用 Spool Orifice Flow Force (IL) 模块，该模块应用与 Spool Orifice (IL) 模块相同的力方程。

### 液动力

作用在阀芯上的力计算如下：

F=−m˙A2ρAcos(α)ε,

其中：

- m˙A 是端口 **A** 处的质量流量。
- *ρ* 是流体密度。
- *A* 是节流口开口面积，由阀芯位置和节流口参数化确定。
- *α* 是射流角，由 von Mises 公式的近似计算得出：

  αjet=0.3663+0.8373(1−e−h1.848c),

  其中 *c* 是 **Radial
  clearance**，*h* 是节流口开度。
- *ε* 是 **Orifice orientation**，表示与 **S** 处正信号或负信号相关的节流口开口。

### 节流口开口面积

对于可变节流口，将 **Orifice orientation** 设置为 `Positive spool displacement opens the orifice` 表示当控制构件伸出时节流口打开，而 `Negative spool displacement opens the orifice` 表示当控制构件缩回时节流口打开。

**Leakage area**，*A*leak，被视为节流口关闭时对流动开放的小面积，用于保持数值连续性。此外，非零的 **Smoothing factor** 可以在节流口处于接近关闭或接近打开位置时提供更高的数值稳定性。

**圆孔**

将 **Orifice parameterization** 设置为 `Round
holes` 会将用户定义数量的孔均匀分布在套筒周边，直径相等且中心对齐在同一平面内。

开口面积表达式基于几何推导，将每个孔的面积计算为平面圆。如果套筒是圆柱形的，则孔不是平面的，此表达式为近似值。开口面积为

Aorifice=n0d028(θ−sin(θ))+Aleak,

其中：

- *n*0 是孔的数量。
- *d*0 是孔的直径。
- *A*leak 是 Aleak=cd0n0。
- *θ* 是节流口开口面积。

*θ* 由 **S** 处的控制信号设定

θ=2cos−1(1−2ΔSd0),

其中 *ΔS* 是控制构件行程距离，*ε(S - Smin)*，其中 *Smin* 是 **Control
member position at closed orifice**。

最大开口面积为：

Amax=π4d02n0+Aleak.

**矩形槽**

将 **Orifice parameterization** 设置为 `Rectangular
slot` 会对管套筒中的一个矩形槽进行建模。

对于在矩形套筒中带有槽的节流口，开口面积为

Aorifice=wΔS+Aleak,

其中 *w* 是节流口宽度。

套筒与壳体之间的最大开口距离为：

Amax=wΔSmax+Aleak.

其中 *ΔS*max 是槽式节流口的 **Spool travel between closed and open orifice** 距离。

在最小节流口开口面积处，泄漏面积为：

Aleak=cw.

### 数值平滑位移

在节流口开度范围的极值处，您可以通过调整模块的 **Smoothing
factor** 来保持仿真中的数值鲁棒性。模块对每个计算的位移应用平滑函数，但主要影响该范围极值处的仿真。

如果 **Smoothing factor** 参数非零，模块会在 `0` 和 *ΔSmax* 之间平滑地饱和节流口开度，其中 *ΔSmax* 是：

- 当 **Orifice parameterization** 设置为 `Round holes` 时，**Diameter of round holes** 参数的值。
- 当 **Orifice parameterization** 设置为 `Rectangular slot` 时，**Spool travel between closed and open orifice** 参数的值。

有关更多信息，请参阅数值平滑。

### 质量流量方程

通过阀芯节流口的流量由压力-流量方程计算：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *C*d 是 **Discharge coefficient**。
- *A* 是 **Cross-sectional area at ports A and B**。
- ρ¯ 是平均流体密度。
- *A*orifice 是节流口开口面积，除非：

  - 开口大于或等于 **Spool travel between closed and open orifice** 距离处的面积。此时节流口面积为 *A*max。
  - 节流口开度小于或等于最小开口距离。此时节流口面积为 *A*leak。

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit 相关的压差，即流体中层流与湍流之间的过渡点：

Δpcrit=πρ¯8Aorifice(νRecritCd)2.

*Pressure loss* 描述了由于面积减小导致的节流口压力降低。*PR*loss 计算如下：

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport.

*Pressure recovery* 描述了由于面积增加导致的节流口正压力变化。如果您不希望捕获此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。

### 假设与限制

- 瞬态效应可忽略不计。
- 射流角近似基于 Richard von Mises 方程。
- 射流角随节流口开度的变化对于矩形槽和圆孔节流口是相同的。
