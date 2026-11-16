---
type: simulink-block
title: 'Gate Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Valves and Orifices / Flow Control Valves'
documentation_page: 'gatevalveil'
documentation_source_path: 'ref/gatevalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Gate Valve (IL)

## 端口

### 输入

### **S** — 闸门位移，m 物理信号

与阀门闸门位移关联的物理信号端口，单位为 m。正信号使闸门缩回并打开阀门。

### 守恒

### **A** — 液体端口 isothermal liquid

与阀入口 A 关联的 Isothermal liquid 守恒端口。

### **B** — 液体端口 isothermal liquid

与阀入口 B 关联的 Isothermal liquid 守恒端口。

## 参数

### **阀门孔口直径** — 孔口直径 `5e-3` `m^2`（默认） | 正标量

阀门开启面积直径。

### **完全覆盖孔口时的闸门位置** — 闸门偏移 `0` `m`（默认） | 正标量

阀门关闭时的闸门偏移。正值且非零表示当端口 **S** 处信号为 0 时阀门部分开启。负值且非零表示重叠阀，该阀在由端口 **S** 处物理信号设定的初始正位移范围内保持关闭。

### **泄漏面积** — 完全关闭位置时的间隙面积 `1e-10` `m^2`（默认） | 正标量

阀门处于完全关闭位置时所有间隙之和。任何小于此值的面积都会被饱和到指定的泄漏面积。这通过保持流动连续性来有助于数值稳定性。

### **端口 A 和 B 的横截面积** — 守恒端口处的孔口面积 `inf` `m^2`（默认） | 正标量

入口和出口端口 **A** 和 **B** 处的面积，用于确定通过孔口的质量流量的压力-流量率方程。

### **流量系数** — 流量系数 `0.64`（默认） | 正标量

考虑理论流动中排放损失的修正因子。

### **临界雷诺数** — 层流的上限雷诺数 `150`（默认） | 正标量

通过阀门的层流的上限雷诺数。

### **平滑因子** — 数值平滑因子 `0.01`（默认） | 范围 [0,1] 内的正标量

连续平滑因子，当阀门处于接近开启或接近关闭位置时，为流量响应引入一层渐变变化。

### **压力恢复** — 是否考虑面积扩张中的压力增加 `off`（默认） | `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力增加。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Flow Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中的闸阀

Gate Valve (IL) 模块表示等温液体网络中的闸阀流量控制。该阀包括一个圆形、锐边孔口和一个相同直径的圆形闸门。闸门根据端口 **S** 处的位移信号开启或关闭。正信号使闸门缩回并打开阀门。

### 开启面积

**闸阀开启示意图**

当闸门缩回时，流通面积为：

Aopen=πd024−Ashielded,

其中 *d*0 是 **阀门孔口直径**。部分开启阀门中由闸门遮挡的面积为：

Ashielded=d022cos−1(Δld0)−Δl2d02−(Δl)2,

其中 *Δl* 是闸门位移，它是端口 **S** 处信号与 **完全覆盖孔口时的闸门位置** 之和。

如果位移超过 **孔口直径**，阀门面积 *A*open 为最大孔口面积与 **泄漏面积** 之和：

Aopen=π4d02+Aleak.

对于端口 **S** 处信号与闸门偏移的任意小于 0 的组合，最小阀门面积为 **泄漏面积**。

### 数值平滑位移

当阀门处于接近开启或接近关闭位置时，可以通过调整 **平滑因子** 参数来保持仿真中的数值鲁棒性。如果 **平滑因子** 参数非零，模块会在 `0` 与 **阀门孔口直径** 参数之间平滑饱和闸门位移。有关详细信息，请参阅数值平滑。

### 质量流量方程

通过阀门的质量守恒：

m˙A+m˙B=0.

通过阀门的质量流量计算如下：

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *C*d 是 **流量系数**。
- *A*valve 是阀门开启面积。
- *A*port 是 **端口 A 和 B 的横截面积**。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差 *p*A – *p*B。

临界压差 *Δp*crit 是与 **临界雷诺数** *Re*crit 相关的压差，*Re*crit 是层流与湍流之间的流态转变点：

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*压力损失* 描述由于面积减小而导致的阀门压力降低。*PR*loss 计算如下：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*压力恢复* 描述由于面积增加而在阀门中产生的正压力变化。如果不希望捕获此压力增加，请清除 **压力恢复** 复选框。在这种情况下，*PR*loss 为 1。
