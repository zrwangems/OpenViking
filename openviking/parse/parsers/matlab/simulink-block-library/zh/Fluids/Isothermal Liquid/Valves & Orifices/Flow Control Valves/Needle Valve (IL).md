---
type: simulink-block
title: 'Needle Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'needlevalveil'
documentation_source_path: 'ref/needlevalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Needle Valve (IL)

## 端口

### 守恒

### **A** — 液体端口，isothermal liquid

液体进入或离开阀的端口。

### **B** — 液体端口，isothermal liquid

液体进入或离开阀的端口。

### 输入

### **S** — 针位移，m 物理信号

控制构件位移，单位为 m，指定为物理信号。正信号使针回缩并打开阀。

## 参数

### **Seat orifice diameter** — 阀座孔直径 `5e-3 m`（默认）| 正标量

阀座孔的直径。

### **Needle cone angle** — 控制构件几何角度 `90 deg`（默认）| 正标量

控制构件几何角度。参见阀描述中的针阀示意图。

### **Needle position when in the seat** — 针偏移 `0 m`（默认）| 标量

阀关闭时的针偏移。正值且非零表示阀部分打开。负值且非零表示重叠阀，该阀在由端口 **S** 处物理信号设定的初始位移内保持关闭。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于该值的面积都会饱和到指定的泄漏面积。这通过保持流动连续性来增强数值稳定性。

### **Cross-sectional area at ports A and B** — 守恒端口处的面积 `inf m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 的面积，用于确定通过阀的质量流量的压力-流量方程。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于计入理论流动中流量损失的修正系数。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将该值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Pressure recovery** — 是否在面积扩张中计入压力升高 `off`（默认）| `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力升高。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2020a 中引入**

## 描述

等温液体系统中的针阀

Needle Valve (IL) 模块对针阀造成的流量减少进行建模。该阀包括一个锥形针和一个圆形锐边阀座。针根据端口 **S** 处的位移信号打开或关闭。正信号使针回缩并打开阀。

### 开口面积

**针阀示意图**

**针阀俯视图**

阀的开口面积计算如下：

Aopen=πhsin(θ2)[d0−h2sin(θ)]+Aleak,

其中：

- *h* 是针的外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是阀座锥角，始终与 **Needle cone angle** 匹配。
- *d*0 是 **Seat orifice diameter**。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=d0[1−1−cos(θ2)]sin(θ).

对于任何大于 *hmax* 的针位移，*A*open 为最大孔口面积与 **Leakage area** 之和：

Aopen=π4d02+Aleak.

对于端口 **S** 处信号与小于 0 的针偏移的任何组合，最小阀面积为 **Leakage area**。

如果 **Smoothing factor** 参数非零，则模块在 `0` 与 *h*max 之间平滑地饱和位移。有关详细信息，请参阅数值平滑。

### 质量流量方程

通过阀的质量守恒：

m˙A+m˙B=0.

通过阀的质量流量计算如下：

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *C*d 是 **Discharge coefficient**。
- *A*valve 是阀的瞬时开口面积。
- *A*port 是 **Cross-sectional area at ports A and B**。
- ρ¯ 是平均流体密度。
- *Δp* 是阀压差 *p*A – *p*B。

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit（层流与湍流之间的流态转捩点）相关的压差：

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*压力损失*描述由于面积减小而导致阀中压力降低。*PR*loss 计算如下：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*压力恢复*描述由于面积增大而导致阀中压力升高。如果不想捕获该压力升高，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。
