---
type: simulink-block
title: 'Spool Orifice (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Orifices'
documentation_page: 'spoolorificeil'
documentation_source_path: 'ref/spoolorificeil.html'
language: zh-CN
chinese_source: worker-translation
---

# Spool Orifice (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

液体进入或离开孔口的入口或出口端口。

### **B** — 液体端口 isothermal liquid

液体进入或离开孔口的入口或出口端口。

### 输入

### **S** — 控制构件位移，m 物理信号

可变面积孔口的控制构件位移，单位为 m。

### 输出

### **F** — 液动力，N 物理信号

轴向液动力，单位为 N。

## 参数

### **Orifice parameterization** — 孔口类型 `Round holes` (default) | `Rectangular slot`

套筒中的孔几何形状。圆孔沿横截面圆周均匀分布。在 `Rectangular slot` 设置中只有一个孔。

### **Diameter of round holes** — 圆孔直径 `5e-3 m` (default) | positive scalar

套筒上所有孔的直径。

#### 依赖项

要启用此参数，请将 **Orifice parametrization** 设置为 `Round holes`。

### **Number of round holes** — 圆孔数量 `6` (default) | positive integer

沿套筒圆周的孔数量。

#### 依赖项

要启用此参数，请将 **Orifice parametrization** 设置为 `Round holes`。

### **Orifice width** — 矩形槽宽度 `0.01 m` (default) | positive scalar

矩形槽宽度。

#### 依赖项

要启用此参数，请将 **Orifice parametrization** 设置为 `Rectangular slot`。

### **Spool travel between closed and open orifice** — 控制构件最大行程 `5e-3 m` (default) | positive scalar

控制构件行程的最大距离。此值提供计算的上限，以使仿真不返回非物理值。

#### 依赖项

要启用此参数，请将 **Orifice parametrization** 设置为 `Rectangular slot`。

### **Flow force output** — 是否对阀芯上的轴向液压力建模 `off` (default) | `on`

是否对阀芯上的轴向液压力建模。选择此参数后，端口 **F** 启用，并输出轴向力作为物理信号，单位为 N。

### **Radial clearance** — 阀芯-套筒间隙 `1e-5 m` (default) | positive scalar

阀芯与套筒之间的径向距离。

#### 依赖项

要启用此参数，请选择 **Flow force output**。

### **Leakage area** — 当阀处于完全关闭位置时的间隙面积 `1e-10` m^2 (default) | positive scalar

当阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定泄漏面积。这通过保持流动连续性有助于数值稳定性。

### **Spool position at closed orifice** — 阀芯偏移 `0` (default) | scalar

当孔口完全打开时的阀芯偏移。正的、非零值表示部分关闭的孔口。负的、非零值表示重叠孔口，该孔口在由端口 **S** 处物理信号设置的初始位移下保持打开。

### **Cross-sectional area at ports A and B** — 守恒端口处的孔口面积 `inf m^2` (default) | positive scalar

入口和出口端口 **A** 和 **B** 处的横截面积。此面积用于确定通过孔口的质量流量的压力-流量方程中。

### **Opening orientation** — 孔口面积变化的方向 `Positive spool displacement opens the orifice` (default) | `Negative spool displacement opens the orifice`

可变孔口面积变化的方向。正的开度方向表示孔口开度增加。负的方向表示孔口开度减小。幅值始终为正。

### **Discharge coefficient** — 流量系数 `0.64` (default) | positive scalar in the range of [0,1]

修正因子，用于考虑理论流动中的排放损失。

### **Critical Reynolds number** — 层流的上限雷诺数 `150` (default) | positive scalar

通过孔口的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01` (default) | positive scalar

连续平滑因子，当孔口处于接近打开或接近关闭位置时，引入一层逐渐变化的流动响应。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Pressure recovery** — 是否考虑面积扩大中的压力增加 `off` (default) | `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Orifices

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中的可变面积滑阀孔口

Spool Orifice (IL) 模块对阀芯和带孔套筒之间的可变面积孔口建模。套筒孔可以是一系列圆孔或矩形孔。流量基于套筒、孔和阀芯之间的总开度面积，该面积根据端口 **S** 处接收的信号伸出或缩回。可以连接多个 Spool Orifice (IL) 模块，以用于沿阀芯-套筒对的多组孔。

如果系统中的阀芯位移由外部源或自定义模块提供，并且您希望将轴向液动力传递到系统，则可以使用 Spool Orifice Flow Force (IL) 模块，该模块应用与 Spool Orifice (IL) 模块相同的力方程。

### 液动力

阀芯上的力计算为：

F=−m˙A2ρAcos(α)ε,

其中：

- m˙A 是端口 **A** 处的质量流量。
- *ρ* 是流体密度。
- *A* 是孔口开度面积，由阀芯位置和孔口参数化确定。
- *α* 是射流角，由 von Mises 公式的近似计算：

  αjet=0.3663+0.8373(1−e−h1.848c),

  其中 *c* 是 **Radial clearance**，*h* 是孔口开度。
- *ε* 是 **Orifice orientation**，表示与 **S** 处正信号或负信号相关联的孔口开度。

### 孔口开度面积

对于可变孔口，将 **Orifice orientation** 设置为 `Positive spool displacement opens the orifice` 表示当控制构件伸出时孔口打开，而 `Negative spool displacement opens the orifice` 表示当控制构件缩回时孔口打开。

**Leakage area**，*A*leak，被视为孔口关闭时对流动开放的小面积，这保持数值连续性。此外，非零 **Smoothing factor** 可以在孔口处于接近关闭或接近打开位置时提供更高的数值稳定性。

**圆孔**

将 **Orifice parameterization** 设置为 `Round holes` 会沿套筒周边均匀分布用户定义数量的孔，这些孔具有相同直径且中心对齐在同一平面内。

开度面积表达式基于几何推导，并将每个孔的面积计算为平面圆。如果套筒是圆柱形，则孔不是平面的，此表达式是近似。开度面积为

Aorifice=n0d028(θ−sin(θ))+Aleak,

其中：

- *n*0 是孔的数量。
- *d*0 是孔的直径。
- *A*leak 是 Aleak=cd0n0。
- *θ* 是孔口开度面积。

*θ* 由 **S** 处的控制信号设置

θ=2cos−1(1−2ΔSd0),

其中 *ΔS* 是控制构件行程距离，*ε(S - Smin)*，其中 *Smin* 是 **Control member position at closed orifice**。

最大开度面积为：

Amax=π4d02n0+Aleak.

**矩形槽**

将 **Orifice parameterization** 设置为 `Rectangular slot` 会对管套筒中的一个矩形槽建模。

对于在矩形套筒中具有槽的孔口，开度面积为

Aorifice=wΔS+Aleak,

其中 *w* 是孔口宽度。

套筒和壳体之间的最大开度距离为：

Amax=wΔSmax+Aleak.

其中 *ΔS*max 是槽孔 **Spool travel between closed and open orifice** 距离。

在最小孔口开度面积处，泄漏面积为：

Aleak=cw.

### 数值平滑位移

在孔口开度范围的极值处，您可以通过调整模块 **Smoothing factor** 来保持仿真中的数值稳健性。该模块对每个计算出的位移应用平滑函数，但主要影响此范围极值处的仿真。

如果 **Smoothing factor** 参数非零，则该模块在 `0` 和 *ΔSmax* 之间平滑饱和孔口开度，其中 *ΔSmax* 是：

- 当 **Orifice parameterization** 设置为 `Round holes` 时，**Diameter of round holes** 参数的值。
- 当 **Orifice parameterization** 设置为 `Rectangular slot` 时，**Spool travel between closed and open orifice** 参数的值。

有关详细信息，请参阅 Numerical Smoothing。

### 质量流量方程

通过滑阀孔口的流量由压力-流量方程计算：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeA)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *C*d 是 **Discharge coefficient**。
- *A* 是 **Cross-sectional area at ports A and B**。
- ρ¯ 是平均流体密度。
- *A*orifice 是孔口开度面积，除非：

  - 开度大于或等于 **Spool travel between closed and open orifice** 距离处的面积。此时孔口面积为 *A*max。
  - 孔口开度小于或等于最小开度距离。此时孔口面积为 *A*leak。

临界压力差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit 相关的压力差，*Re*crit 是流体中层流和湍流之间的转捩点：

Δpcrit=πρ¯8Aorifice(νRecritCd)2.

*压力损失* 描述由于面积减小而导致的孔口中压力降低。*PR*loss 计算为：

PRloss=1−(AorificeAport)2(1−Cd2)−CdAorificeAport1−(AorificeAport)2(1−Cd2)+CdAorificeAport.

*压力恢复* 描述由于面积增加而导致的孔口中正压力变化。如果您不希望捕获此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。

### 假设与限制

- 瞬态效应可忽略。
- 射流角近似基于 Richard von Mises 方程。
- 对于矩形槽和圆孔孔口，射流角随孔口开度的变化相同。
