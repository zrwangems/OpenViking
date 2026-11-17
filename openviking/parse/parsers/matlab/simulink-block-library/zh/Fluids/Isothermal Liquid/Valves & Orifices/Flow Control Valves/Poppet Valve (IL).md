---
type: simulink-block
title: 'Poppet Valve (IL)'
family: 'isothermal-liquid'
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

### 守恒

### **A** — 液体端口 isothermal liquid

阀的液体入口或出口端口。

### **B** — 液体端口 isothermal liquid

阀的液体入口或出口端口。

### 输入

### **S** — 阀杆位移，m physical signal

## 参数

### **Poppet geometry** — 阀芯类型 `Cylindrical stem` (default) | `Round ball`

阀芯类型。可以选择圆柱形或球形控制构件。

### **Valve seat specification** — 阀座几何 `Sharp-edged` (default) | `Conical`

阀座几何。该模块使用此参数计算阀芯与阀座之间的开口面积。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Ball diameter** — 球控制构件直径 `0.01 m` (default) | positive scalar

球控制构件的直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Seat orifice diameter** — 阀座孔口直径 `7e-3 m` (default) | positive scalar

阀座孔口直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Stem diameter** — 圆柱阀杆直径 `0.01 m` (default) | positive scalar

圆柱阀杆的直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Cylindrical stem`。

### **Seat cone angle** — 阀座开口角度 `120 deg` (default) | positive scalar

阀座开口的角度。

#### 依赖关系

要启用此参数，请设置以下任一项：

- 将 **Poppet geometry** 设置为
  `Cylindrical stem`
- 将 **Poppet geometry** 设置为 `Round
  ball`，并将 **Valve seat
  specification** 设置为
  `Conical`

### **Poppet position when in the seat** — 控制构件偏移 `0 m` (default) | positive scalar

阀关闭时的阀芯偏移。正非零值表示部分打开的阀。负非零值表示重叠阀，在由端口 **S** 处的 physical signal 设置的初始位移内保持关闭。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2` (default) | positive scalar

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。这通过保持流动连续性来帮助提高数值稳定性。

### **Cross-sectional area at ports A and B** — 守恒端口处的面积 `inf` `m^2` (default) | positive scalar

入口和出口端口 **A** 和 **B** 处的面积，用于确定通过阀的质量流量的压力-流量方程中。

### **Discharge coefficient** — 流量系数 `0.64` (default) | positive scalar

修正因子，用于考虑理论流动中的流量损失。

### **Critical Reynolds number** — 层流的上限雷诺数 `150` (default) | positive scalar

通过孔口的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01` (default) | positive scalar in the range [0,1]

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `off` (default) | `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力增加。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

isothermal liquid 网络中的 Poppet 阀

Poppet Valve (IL) 模块表示 isothermal liquid 系统中的流量控制阀。阀芯可以是圆柱体或球体。可以选择 sharp-edged 和 conical 阀座。阀芯根据端口 **S** 处的位移信号打开或关闭。正信号使阀芯回缩并打开阀。

**Poppet Valve 示意图**

侧视图示意图，说明阀座、阀芯和开口面积之间的关系。阀座为 V 形。阀芯为矩形。开口面积是橙色梯形，表示发生流动的区域。

**Poppet Valve 俯视图**

俯视图示意图，说明阀座、阀芯和开口面积之间的关系。阀座是外环。阀芯是填充的内圆。开口面积是阀芯与阀座之间的环。

### 圆柱阀杆阀芯开口面积

阀的开口面积计算如下：

Aopen=πhsin(θ2)[ds+h2sin(θ)]+Aleak,

其中：

- *h* 是圆柱体外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是 **Seat cone angle**。
- *d*s 是 **Stem diameter**。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=ds[1+cos(θ2)−1]sin(θ).

对于任何大于 *h*max 的阀杆位移，*A*open 为最大孔口面积与 **Leakage area** 之和：

Aopen=π4ds2+Aleak.

对于端口 **S** 处信号与小于 0 的圆柱偏移的任何组合，最小阀面积为 **Leakage area**。

### 圆球阀芯开口面积

**Sharp-edged 阀座几何**

阀的开口面积计算如下：

Aopen,sharp−edged=πrO(Gsharp+h)2+rO2[1−rB2(Gsharp+h)2+rO2]+Aleak,

其中：

- *h* 是圆柱体外边缘与阀座之间的垂直距离，如上图所示。
- *r*O 是根据 **Seat orifice diameter** 计算得到的阀座孔口半径。
- *r*B 是根据 **Ball diameter** 计算得到的球半径。
- *G*sharp 是几何参数：Gsharp=rB2−rO2。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=2rB2−rO2+rOrO2+4rB22−Gsharp.

对于任何大于 *h*max 的球位移，*A*open 为最大孔口面积与 **Leakage area** 之和：

Aopen=π4dO2+Aleak.

对于端口 **S** 处信号与小于 0 的球偏移的任何组合，最小阀面积为 **Leakage area**。

**Conical 阀座几何**

阀的开口面积计算如下：

Aopen,conical=Gconicalh+π2sin(θ)sin(θ2)h2+Aleak,

其中：

- *h* 是圆柱体外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是 **Seat cone angle**。
- *G*conical 是几何参数：Gconical=πrBsin(θ)，其中 *r*B 是球半径。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=rB2+rO2cos(θ2)−rBsin(θ2).

对于任何大于 *h*max 的球位移，*A*open 为最大孔口面积与 **Leakage area** 之和：

Aopen=π4dO2+Aleak.

对于端口 **S** 处信号与小于 0 的球偏移的任何组合，最小阀面积为 **Leakage area**。

### 数值平滑位移

该模块计算阀芯位移 *h*，使得

h={0,(S−Smin)≤0hMax,(S−Smin)≥hMax(S−Smin),Else

其中：

- *S* 是 physical signal 输入。
- *Smin* 是 **Poppet position when in the seat** 参数。
- *hMax* 是最大位移。

如果 **Smoothing factor** 参数非零，则该模块会在 `0` 和 *hMax* 之间平滑饱和阀芯位移。

有关详细信息，请参阅 Numerical Smoothing。

### 质量流量方程

通过阀的质量守恒：

m˙A+m˙B=0.

通过阀的质量流量计算如下：

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *C*d 是 **Discharge coefficient**。
- *A*valve 是当前阀开口面积。
- *A*port 是 **Cross-sectional area at ports A and B**。
- ρ¯ 是平均流体密度。
- *Δp* 是阀压差 *p*A – *p*B。

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit 相关的压差，即层流与湍流之间的流态转变点：

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*压力损失* 描述由于面积减小而导致的阀内压力降低。*PR*loss 计算如下：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*压力恢复* 描述由于面积增加而导致的阀内正压力变化。如果不希望捕捉此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。
