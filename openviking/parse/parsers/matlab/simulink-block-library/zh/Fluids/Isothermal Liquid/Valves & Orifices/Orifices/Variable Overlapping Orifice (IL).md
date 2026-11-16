---
type: simulink-block
title: 'Variable Overlapping Orifice (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Orifices'
documentation_page: 'variableoverlappingorificeil'
documentation_source_path: 'ref/variableoverlappingorificeil.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Overlapping Orifice (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

节流孔的入口或出口点。

### **B** — 液体端口 isothermal liquid

节流孔的入口或出口点。
### 输入

### **S** — 套筒位移，m physical signal

相对于壳体的套筒位置，单位为 m。

## 参数

### **套筒孔直径** — 套筒孔直径 `5e-3 m` (默认) | 正标量

运动元件中孔的直径。

### **壳体孔直径** — 壳体孔直径 `5.5e-3 m` (默认) | 正标量

固定元件中孔的直径。

### **孔同心时的套筒位置** — 当孔中心对齐时的运动元件位置 `0 m` (默认) | 标量

当孔中心对齐时的运动元件位置。此参数用于在仿真期间通过与端口 **S** 接收到的信号进行比较，确定运动孔与固定孔的瞬时重叠。

### **相互作用对数** — 重叠节流孔的数目，按对计 `1` (默认) | 正标量

重叠节流孔的数目，按对计。在被建模的物理硬件中，套筒-壳体对不需要对齐。

### **泄漏面积** — 完全关闭位置时的间隙面积 `1e-10 m^2` (默认) | 正标量

阀处于完全关闭位置时所有间隙之和。任何小于此值的面积都保持为指定的泄漏面积。这通过保持流动的连续性来提高数值稳定性。

### **端口 A 和 B 处的横截面积** — 守恒端口处的节流孔面积 `inf m^2` (默认) | 正标量

入口和出口端口 **A** 和 **B** 处的面积，用于确定通过节流孔的质量流量的压力-流量方程中。

### **流量系数** — 流量系数 `0.64` (默认) | 正标量

考虑理论流动中流量损失的修正因子。

### **临界雷诺数** — 层流的上限雷诺数 `150` (默认) | 正标量

通过节流孔的层流的上限雷诺数。

### **平滑系数** — 数值平滑系数 `0.01` (默认) | [0,1] 范围内的正标量

连续平滑系数，在阀接近打开或接近关闭位置时，为流量响应引入逐渐变化层。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **压力恢复** — 是否考虑面积扩大中的压力增加 `Off` (默认) | `On`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力增加。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

在等温液体系统中由具有可变重叠的开口段创建的节流孔

Variable Overlapping Orifice (IL) 模块对通过具有变化重叠面积的圆孔的流动进行建模，例如固定壳体内的移动套筒。重叠的孔可以具有不同直径，但沿阀芯或套筒的其他孔具有相同直径。

### 重叠面积

流量取决于由套筒和壳体中的孔重叠产生的可变开口面积。该瞬时开口面积计算如下：

Aoverlap=r2[cos−1(C2+r2−R22Cr)−(C2+r2−R22Cr)1−(C2+r2−R22Cr)2]+R2[cos−1(C2−r2+R22CR)−(C2−r2+R22CR)1−(C2−r2+R22CR)2],

其中：

- *r* 是较小孔的直径。
- *R* 是较大孔的直径。
- *C* 是孔中心之间的绝对距离，根据端口 **S** 处的物理信号、瞬时套筒位置以及 **孔同心时的套筒位置** *S*0 计算：C=|S−S0|。

如果套筒和壳体上的孔具有相同直径，则重叠面积变为：

Aoverlap=2r2[cos−1(C2r)−(C2r)1−(C2r)2].

可以通过在孔中心之间的最近点和最远点处调整模块的 **平滑系数** 来保持仿真中的数值稳健性。模块对归一化孔中心距离应用平滑函数，

C^=(C−R+r)(2r).

该函数在 `0` 和 `1` 之间平滑地饱和归一化孔中心距离。

有关更多信息，请参阅数值平滑

### 质量流量方程

通过一对节流孔的流量根据压力-面积关系计算：

m˙=CdAorifice2ρ¯PRloss(1−(AorificeAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *C*d 是 **流量系数**。
- *A*orifice 是开放流动的面积，Aorifice=Aoverlap+Aleak。
- *A* 是 **端口 A 和 B 处的横截面积**。
- ρ¯ 是平均流体密度。

*压力损失* 描述由于面积减小而在阀中产生的压力降低。压力损失项 *PR*loss 计算如下：

PRloss=1−(AoverlappingAport)2(1−Cd2)−CdAoverlappingAport1−(AoverlappingAport)2(1−Cd2)+CdAoverlappingAport.

*压力恢复* 描述由于面积增加而在阀中产生的正压力变化。如果不希望捕获此压力增加，请将 **压力恢复** 设置为 `Off`。在这种情况下，*PR*loss 为 1。

临界压差 *Δp*crit 是与 **临界雷诺数** *Re*crit 相关的压差，即层流与湍流之间的流态转变点：

Δpcrit=πρ¯8Aoverlapping(νRecritCd)2.
