---
type: simulink-block
title: 'Poppet Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'poppetvalveil'
documentation_source_path: 'ref/poppetvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Poppet Valve (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

阀的液体入口或出口端口。

### **B** — 液体端口，等温液体

阀的液体入口或出口端口。

### 输入

### **S** — 阀杆位移，m，物理信号

阀控制部件的位移，以 m 为单位，指定为物理信号。

## 参数

### **Poppet geometry** — 阀芯类型 `Cylindrical stem`（默认）| `Round ball`

阀芯类型。您可以选择圆柱形或球形控制部件。

### **Valve seat specification** — 阀座几何形状 `Sharp-edged`（默认）| `Conical`

阀座几何形状。该模块使用此参数计算阀芯与阀座之间的开口面积。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Ball diameter** — 球形控制部件直径 `0.01 m`（默认）| 正标量

球形控制部件的直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Seat orifice diameter** — 阀座孔口直径 `7e-3 m`（默认）| 正标量

阀座孔口直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Stem diameter** — 圆柱形阀杆直径 `0.01 m`（默认）| 正标量

圆柱形阀杆的直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Cylindrical stem`。

### **Seat cone angle** — 阀座开口角度 `120 deg`（默认）| 正标量

阀座开口的角度。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Poppet geometry** 为 `Cylindrical stem`
- **Poppet geometry** 为 `Round ball` 且 **Valve seat specification** 为 `Conical`

### **Poppet position when in the seat** — 控制部件偏移量 `0 m`（默认）| 正标量

阀关闭时的阀芯偏移量。正的、非零值表示阀部分打开。负的、非零值表示重叠阀，该阀在由端口 **S** 处的物理信号设定的初始位移范围内保持关闭。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都被饱和到指定的泄漏面积。这通过保持流量连续性来有助于数值稳定性。

### **Cross-sectional area at ports A and B** — 守恒端口处的面积 `inf` `m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的面积，用于确定通过阀的质量流率的压力-流率方程中。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `off`（默认）| `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力增加。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络中的提升阀

Poppet Valve (IL) 模块表示等温液体系统中的流量控制阀。提升阀可以是圆柱形或球形。您可以选择锐边阀座或锥形阀座。提升阀根据端口 **S** 处的位移信号打开或关闭。正信号使提升阀回缩并打开阀门。

**提升阀示意图**

侧视图示意图，说明阀座、提升阀和开口面积之间的关系。阀座为 V 形。提升阀为矩形。开口面积为橙色梯形，表示流动发生的位置。

**提升阀俯视图**

俯视图示意图，说明阀座、提升阀和开口面积之间的关系。阀座为外环。提升阀为填充的内圆。开口面积为提升阀与阀座之间的环。

### 圆柱形阀杆提升阀开口面积

阀门的开口面积计算如下：

Aopen=πhsin(θ2)[ds+h2sin(θ)]+Aleak，

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是 **Seat cone angle**。
- *d*s 是 **Stem diameter**。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=ds[1+cos(θ2)−1]sin(θ)。

对于任何大于 *h*max 的阀杆位移，*A*open 为最大孔口面积与 **Leakage area** 之和：

Aopen=π4ds2+Aleak。

对于端口 **S** 处信号与圆柱偏移量小于 0 的任何组合，最小阀门面积为 **Leakage area**。

### 圆球提升阀开口面积

**锐边阀座几何形状**

阀门的开口面积计算如下：

Aopen,sharp−edged=πrO(Gsharp+h)2+rO2[1−rB2(Gsharp+h)2+rO2]+Aleak，

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离，如上图所示。
- *r*O 是阀座孔口半径，由 **Seat orifice diameter** 计算得出。
- *r*B 是球的半径，由 **Ball diameter** 计算得出。
- *G*sharp 是几何参数：Gsharp=rB2−rO2。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=2rB2−rO2+rOrO2+4rB22−Gsharp。

对于任何大于 *h*max 的球位移，*A*open 为最大孔口面积与 **Leakage area** 之和：

Aopen=π4dO2+Aleak。

对于端口 **S** 处信号与球偏移量小于 0 的任何组合，最小阀门面积为 **Leakage area**。

**锥形阀座几何形状**

阀门的开口面积计算如下：

Aopen,conical=Gconicalh+π2sin(θ)sin(θ2)h2+Aleak，

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是 **Seat cone angle**。
- *G*conical 是几何参数：Gconical=πrBsin(θ)，其中 *r*B 是球半径。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=rB2+rO2cos(θ2)−rBsin(θ2)。

对于任何大于 *h*max 的球位移，*A*open 为最大孔口面积与 **Leakage area** 之和：

Aopen=π4dO2+Aleak。

对于端口 **S** 处信号与球偏移量小于 0 的任何组合，最小阀门面积为 **Leakage area**。

### 数值平滑位移

该模块计算提升阀位移 *h*，使得

h={0,(S−Smin)≤0hMax,(S−Smin)≥hMax(S−Smin),Else

其中：

- *S* 是物理信号输入。
- *Smin* 是 **Poppet position when in the seat** 参数。
- *hMax* 是最大位移。

如果 **Smoothing factor** 参数非零，则该模块在 `0` 和 *hMax* 之间平滑地饱和提升阀位移。

有关详细信息，请参阅数值平滑。

### 质量流量方程

通过阀门的质量守恒：

m˙A+m˙B=0。

通过阀门的质量流量计算如下：

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4，

其中：

- *C*d 是
  **Discharge coefficient**。
- *A*valve 是当前阀门
  开口面积。
- *A*port 是
  **端口 A 和 B 处的横截面积**。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差
  *p*A –
  *p*B。

临界压差，
*Δp*crit，是与 **Critical Reynolds number**，
*Re*crit，即层流与湍流之间的流态转变点
相关的压差：

Δpcrit=πρ¯8Avalve(νRecritCd)2。

*Pressure loss* 描述由于面积减小而导致阀门中的压力降低。*PR*loss 计算如下：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport。

*Pressure recovery* 描述由于面积增加而导致阀门中的正压力变化。如果你不想捕捉这种压力增加，
请清除 **Pressure recovery** 复选框。在这种情况下，
*PR*loss 为 1。
