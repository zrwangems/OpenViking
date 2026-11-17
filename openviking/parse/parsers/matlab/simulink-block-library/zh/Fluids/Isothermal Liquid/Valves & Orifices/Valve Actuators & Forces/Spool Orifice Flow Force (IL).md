---
type: simulink-block
title: 'Spool Orifice Flow Force (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces'
documentation_page: 'spoolorificeflowforceil'
documentation_source_path: 'ref/spoolorificeflowforceil.html'
language: zh-CN
chinese_source: worker-translation
---

# Spool Orifice Flow Force (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

模块的液体进入或出口端口。

### **B** — 液体端口，等温液体

模块的液体进入或出口端口。
### 输入

### **S** — 控制构件位移，m，物理信号

阀芯位移，单位为 m，指定为物理信号。
### 输出

### **F** — 液动力，N，物理信号

轴向液动力，单位为 N，指定为物理信号。

## 参数

### **Orifice geometry** — 节流口几何形状 `Round holes`（默认）| `Rectangular slot`

所建模的阀芯在阀套中具有圆孔还是矩形槽。

### **Diameter of round holes** — 圆孔直径 `5e-3 m`（默认）| 正标量

阀套上所有孔的直径。

#### 依赖关系

要启用此参数，请将 **Orifice geometry** 设置为 `Round holes`。

### **Number of round holes** — 圆孔数量 `6`（默认）| 正整数

沿阀套圆周分布的孔的数量。

#### 依赖关系

要启用此参数，请将 **Orifice geometry** 设置为 `Round holes`。

### **Orifice width** — 矩形槽宽度 `0.01 m`（默认）| 正标量

矩形槽宽度。

#### 依赖关系

要启用此参数，请将 **Orifice geometry** 设置为 `Rectangular slot`。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `1 m`（默认）| 正标量

最大节流口开度，包括 **Spool position at maximum orifice area**。

#### 依赖关系

要启用此参数，请将 **Orifice geometry** 设置为 `Rectangular slot`。

### **Radial clearance** — 阀芯-阀套间隙 `1e-5 m`（默认）| 正标量

阀芯与阀套之间的径向距离。

### **Spool position at closed orifice** — 初始阀芯偏移 `0 m`（默认）| 标量

阀芯在中位伸出或缩回时的初始偏移。

### **Opening orientation** — 节流口面积变化方向 `Positive spool displacement opens orifice`（默认）| `Negative spool displacement closes orifice`

打开节流口的构件运动方向。正方向表示正的控制构件位移增大节流口开度。负方向表示负的控制构件位移增大节流口开度。幅值始终为正。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中阀芯节流口的轴向液动力

Spool Orifice Flow Force (IL) 模块对阀芯节流口上的液压轴向力进行建模。它通过端口 **S** 接收作为物理信号的阀芯位置。您还可以对通过带圆孔或矩形槽的阀芯节流口的流量进行建模。正方向的力用于关闭节流口。

如果您希望在一个模块中对阀芯和轴向力进行建模，请使用 Spool Orifice (IL) 模块。轴向力通过端口 **F** 作为物理信号输出。

### 液动力

作用在阀芯上的力按下式计算：

F=−m˙A2ρAcos(α)ε,

其中：

- m˙A 是端口 **A** 处的质量流量。
- *ρ* 是流体密度。
- *A* 是节流口开启面积，由阀芯位置和节流口参数化确定。
- *α* 是射流角，由 von Mises 公式的近似式计算得出：

  αjet=0.3663+0.8373(1−e−h1.848c),

  其中 *c* 是 **Radial clearance**，*h* 是节流口开度。
- *ε* 是开口方向，表示与 **S** 处正信号或负信号相关联的节流口开度。

### 开启面积

节流口开度基于位移阀芯所产生的开启面积：

ΔS=(S−Smin)ε,

其中：

- *S*min 是 **Spool position at closed orifice**。
- *S* 是端口 **S** 处的位移信号。

如果 *Δs* 降至 0 以下，则使用节流口泄漏面积。如果 *ΔS* 大于 **Spool travel between closed and open orifice**，则使用最大节流口面积。

**圆孔**

将 **Orifice geometry** 设置为 `Round holes` 时，会在阀套周边均匀分布用户定义数量的孔，这些孔具有相等的直径且中心对齐在同一平面内。

开启面积为

Aorifice=n0d028(θ−sin(θ2))+Aleak,

其中：

- *n*0 是孔的数量。
- *d*0 是孔的直径。
- *θ* 是节流口开启角：

  θ=2cos−1(1−2ΔSd0).

  如果 *θ* 大于 *2π*，则 *θ* 保持为 *2π*。
- *A*leak 是 **Leakage area**。

开启面积表达式基于几何推导，将每个孔的面积按平面圆计算。如果阀套为圆柱形，则孔并非平面，此表达式为近似计算。

最大开启面积为：

Amax=π4d02n0+Aleak.

**矩形槽**

将 **Orifice geometry** 设置为 `Rectangular slot` 时，对管状阀套中的一个矩形槽进行建模。

对于在矩形阀套中带有槽的节流口，开启面积为

Aorifice=wΔS+Aleak,

其中 *w* 是节流口宽度。

阀套与壳体之间的最大开启距离为：

Amax=wΔSmax+Aleak.

其中 *ΔS*max 是 **Spool travel between closed and open orifice**。

### 数值平滑位移

在节流口开度范围的极值处，您可以通过调整模块的 **Smoothing factor** 来保持仿真的数值鲁棒性。模块对每个计算出的位移应用平滑函数，但主要影响该范围极值处的仿真。

如果 **Smoothing factor** 参数非零，模块会在 `0` 与 *ΔSmax* 之间平滑地饱和节流口开度，其中 *ΔSmax* 为：

- 当 **Orifice parameterization** 设置为 `Round holes` 时，**Diameter of round holes** 参数的值。
- 当 **Orifice parameterization** 设置为 `Rectangular slot` 时，**Spool travel between closed and open orifice** 参数的值。

有关详细信息，请参阅 Numerical Smoothing。

### 假设与限制

- 瞬态效应可忽略不计。
- 射流角近似基于 Richard von Mises 方程。
- 射流角随节流口开度的变化对于矩形槽和圆孔节流口是相同的。
