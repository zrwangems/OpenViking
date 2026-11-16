---
type: simulink-block
title: 'Gate Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Flow Control Valves'
documentation_page: 'gatevalvetl'
documentation_source_path: 'ref/gatevalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Gate Valve (TL)

## 端口

### 输入

### **S** — 闸门位移，m physical signal

与阀门闸门位移关联的 physical signal 端口，单位为 m。正信号使闸门回缩并打开阀门。

### 守恒

### **A** — 液体端口 thermal liquid

与阀门入口 A 关联的 thermal liquid 守恒端口。

### **B** — 液体端口 thermal liquid

与阀门入口 B 关联的 thermal liquid 守恒端口。

## 参数

### **Orifice diameter** — Orifice diameter `0.01` `m` (default) | positive scalar

阀门开口面积直径。

### **Gate position when fully covering orifice** — Gate offset `0` `m` (default) | nonnegative scalar

阀门关闭时的闸门偏移量。当端口 **S** 处的信号为 0 时，正值且非零值表示阀门部分打开。负值且非零值表示阀门重叠，并且在由端口 **S** 处的物理信号设置的初始正位移期间保持关闭。

### **Leakage area** — Gap area when in fully shut position `1e-10` `m^2` (default) | positive scalar

阀门处于完全关闭位置时所有间隙的总和。该模块会将更小的数值饱和到此值。此参数通过保持流动的连续性来帮助提高数值稳定性。

### **Smoothing factor** — Numerical smoothing factor `0.01` (default) | scalar in the range [0,1]

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。

### **Cross-sectional area at ports A and B** — Orifice area at conserving ports `0.01` `m^2` (default) | positive scalar

入口和出口端口 **A** 和 **B** 处的面积，用于确定通过孔口质量流量的压力-流量方程。

### **Discharge coefficient** — Discharge coefficient `0.64` (default) | positive scalar

修正因子，用于考虑理论流动中的排放损失。

### **Critical Reynolds number** — Upper Reynolds number limit for laminar flow `150` (default) | positive scalar

通过阀门的层流雷诺数上限。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

热液体系统中的闸门阀

Gate Valve (TL) 模块表示热液体网络中的闸门阀。该阀门包括一个圆形锐边孔口和一个直径相同的圆形闸门。闸门根据端口 **S** 处的位移信号打开或关闭。正信号抬起闸门以打开阀门。该图展示了开口面积与闸门净位移之间的关系。

展示开口面积与闸门净位移之间关系的图。

平滑函数允许阀门开口面积在完全关闭和完全打开位置之间平滑变化。该平滑函数可减少闸门位置为零和最大时开口面积的突变。

### 质量平衡

阀门中的质量守恒方程为

m˙A+m˙B=0,

其中：

- m˙A 是通过端口 **A** 进入阀门的质量流量。
- m˙B 是通过端口 **B** 进入阀门的质量流量。

### 动量平衡

阀门中的动量守恒方程为

pA−pB=m˙m˙2+m˙cr22ρAvgCd2S2[1−(SRS)2]PRLoss,

其中：

- *p*A 和 *p*B 是端口 **A** 和端口 **B** 处的压力。
- m˙ 是质量流量。
- m˙cr 是临界质量流量：

  m˙cr=RecrμAvgπ4SR.
- *ρ*Avg 是平均液体密度。
- *C*d 是流量系数。
- *S* 是阀门入口面积。
- *PR*Loss 是压力比：

  PRLoss=1−(SR/S)2(1−Cd2)−Cd(SR/S)1−(SR/S)2(1−Cd2)+Cd(SR/S).

### 能量平衡

阀门中的能量守恒方程为

ϕA+ϕB=0,

其中：

- *ϕ*A 是通过端口 **A** 进入阀门的能量流率。
- *ϕ*B 是通过端口 **B** 进入阀门的能量流率。

### 阀门开口面积

该模块使用以下表达式计算阀门开口面积

A=πd024−ACovered+Aleak,

其中：

- *A* 是阀门开口面积。
- *Aleak* 是 **Leakage area** 参数的值。
- *d*0 是阀门孔口直径。
- *A*Covered 是被闸门覆盖的阀门孔口面积部分：

  ACovered=d022acos(Δld0)−Δl2d02−(Δl)2.
- *Δl* 是闸门中心相对于孔口中心的净位移。

  Δl={0,(Sd−Smin)≤0d0,(Sd−Smin)≥d0(Sd−Smin),Else
- *S*min 是在模块对话框中指定的 **Gate position when fully covering orifice** 参数的值。
- *S*d 是通过物理信号输入端口 S 指定的闸门位移。

### 数值平滑位移

当阀门处于接近打开或接近关闭位置时，可以通过调整 **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，则该模块会在 `0` 和 **Valve orifice diameter** 参数之间平滑饱和闸门位移。有关详细信息，请参阅数值平滑。
