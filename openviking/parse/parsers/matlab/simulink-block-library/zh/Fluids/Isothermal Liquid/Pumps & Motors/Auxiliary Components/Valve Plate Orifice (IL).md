---
type: simulink-block
title: 'Valve Plate Orifice (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors / Auxiliary Components'
documentation_page: 'valveplateorificeil'
documentation_source_path: 'ref/valveplateorificeil.html'
language: zh-CN
chinese_source: worker-translation
---

# Valve Plate Orifice (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

节流口的入口点。

### **B** — 液体端口，等温液体

节流口的出口点。
### 输入

### **G** — 缸体旋转角度，rad，物理信号

缸体旋转角度，以弧度为单位，指定为物理信号。

## 参数

### **Cylinder block pitch radius** — 缸体节圆半径 `0.05 m`（默认）| 正标量

旋转缸体的节圆半径。

### **Cylinder orifice diameter** — 缸体槽直径 `2.5e-3 m`（默认）| 正标量

缸体槽的直径。

### **Pressure carryover angle** — 压力过渡距离 `0.06 rad`（默认）| 标量

活塞在从关闭槽到打开槽的压力过渡期间所经过的平均角距离。

### **Phase angle** — 初始配流盘偏移角 `0 rad`（默认）| 标量

初始配流盘偏移角。配流盘与槽之间的总角度是 **Phase angle** 与 **Pressure carryover angle** 之和，*Ψ*。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持为指定的泄漏面积。这通过保持流动的连续性来帮助数值稳定性。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过节流口的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors / Auxiliary Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温轴向柱塞机中的可变节流口

Valve Plate Orifice (IL) 模块对轴向柱塞机中运动活塞与泵之间的月牙形开口进行建模。旋转活塞通过配流盘周期性地连接到泵的吸入口或排出口。您可以将两个配流盘模块连接到轴向柱塞泵的每个缸体，以表示泵的入口槽和出口槽。

一个带有一个月牙槽的旋转缸体，在端口 **A** 处连接到泵吸入口，在端口 **B** 处连接到泵排出口。这些点连接到配流盘，彼此之间相隔 **Pressure carryover angle** 与 π 弧度（180 度）之间。配流盘旋转角度由端口 **G** 处的信号设定。缸体位置角 *γ* 是位置信号 *G* 与初始角度偏移（即 **Phase angle**，*γ*0）之和：

γ=γ0+G。

*γ* 始终介于 0 和 2π 之间。对于任何大于 2π rad 的组合信号与偏移，*γ* 保持在 2π；对于任何小于 0 rad 的组合信号与偏移，*γ* 保持在 0。要改变节流口相对于槽的初始位置，您可以调整 **Phase angle** 参数。

**带五个活塞的轴向柱塞机**

图中的数字表示轴向柱塞机的组件：

1. 配流盘节流口
2. 转子
3. 活塞
4. 驱动轴
5. 斜盘

### 缸体角度

缸体与槽的旋转对齐由以下角度描述：

- 旋转到槽上时的缸体角度，*γ*1：

  γ1=Ψ−rR
- 完全旋转到槽上时的缸体角度，*γ*2：

  γ2=Ψ+rR
- 旋转超过槽时的缸体角度，*γ*3：

  γ3=π−2rR
- 完全旋转超过槽时的缸体角度，*γ*4：

  γ4=π

其中：

- *Ψ* 是 **Pressure carryover angle**。该角度表示活塞在从关闭槽到打开槽的压力过渡期间所经过的平均角距离。
- *r* 是 **Cylinder orifice diameter** 的一半。
- *R* 是 **Cylinder block pitch radius**。

### 节流口开口面积

**缸体运动期间的节流口面积计算**

过渡打开面积，即缸体旋转角度 *γ*1 与 *γ*2 之间的开口，计算如下：

Aγ1γ2=Sopening+SLeak=r2(2βopening−sin(2βopening))+SLeak。

过渡关闭面积，即缸体旋转角度 *γ*3 与 *γ*4 之间的开口，计算如下：

Aγ3γ4=Sclosing+SLeak=r2(2βclosing−sin(2βclosing))+SLeak，

其中打开和关闭参数为：

βopening=cos−1(Rrsin((ψ+rR)−γ2))，

以及

βclosing=cos−1(Rrsin(γ−(π−2rR)2))。

*γ*2 与 *γ*3 之间的面积为 Aγ2γ3=SMax+SLeak，*γ*4 与 *γ*1 之间的面积为 Aγ4γ1=SLeak。节流口的最大开口为 SMax=πr2。

非零的 **Smoothing factor** 可以在节流口处于接近关闭或接近打开位置时提供额外的数值稳定性。

### 数值平滑的节流口角度

在节流口槽的入口和出口角度处，您可以通过调整模块的 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会平滑地饱和 *γ*1 与 *γ*2 之间的过渡打开角度以及 *γ*3 与 *γ*4 之间的过渡关闭角度。有关更多信息，请参阅数值平滑。

### 质量流量方程

通过配流盘节流口的流量由压力-面积关系计算：

m˙=CdAorifice2ρ¯Δp[Δp2+Δpcrit2]1/4，

其中：

- *C*d 是 **Discharge coefficient**。
- *A*orifice 是向流动开放的面积。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门上的压降，*P*A – *P*B。

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit 相关的压差，后者是流体中层流与湍流之间的转变点：

Δpcrit=πρ¯8Aorifice(νRecritCd)2。
