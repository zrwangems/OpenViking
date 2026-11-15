---
type: simulink-block
title: 'Poppet Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Moist Air Library / Valves and Orifices / Flow Control Orifices'
documentation_page: 'poppetvalvema'
documentation_source_path: 'ref/poppetvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# Poppet Valve (MA)

## 端口

### 守恒

### **A** — 阀的湿空气入口或出口

液体进入或退出阀的端口。

### **B** — 阀的湿空气入口或出口

液体进入或退出阀的端口。

### 输入

### **S** — 阀杆位移，m 物理信号

阀控制构件的位移，以 m 为单位，指定为物理信号。

## 参数

### **Poppet geometry** — 提升阀类型 `Cylindrical stem`（默认）| `Round ball`

提升阀类型。您可以选择圆柱形或球形控制构件。

### **Valve seat geometry** — 阀座几何形状 `Sharp-edged`（默认）| `Conical`

阀座几何形状。该模块使用此参数计算提升阀与阀座之间的开口面积。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Ball diameter** — 球控制构件直径 `0.01 m`（默认）| positive scalar

球控制构件的直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Orifice diameter** — 阀座节流孔直径 `7e-3 m`（默认）| positive scalar

阀座节流孔直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Stem diameter** — 圆柱阀杆直径 `0.01 m`（默认）| positive scalar

圆柱阀杆的直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Cylindrical stem`。

### **Seat cone angle** — 阀座开口角度 `120 deg`（默认）| positive scalar

阀座开口的角度。

#### 依赖关系

要启用此参数，请设置以下任一项：

- 将 **Poppet geometry** 设置为 `Cylindrical stem`
- 将 **Poppet geometry** 设置为 `Round ball`，并将 **Valve seat geometry** 设置为 `Conical`

### **Control member position at closed orifice** — 控制构件偏移 `0 m`（默认）| positive scalar

阀关闭时的提升阀偏移。正的非零值表示阀部分打开。负的非零值表示重叠阀，该阀在由端口 **S** 处的物理信号设置的初始位移期间保持关闭。

### **Valve parameterization** — 用于指定节流孔流量特性的参数化方法 `Orifice area based on geometry`（默认）| `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声导决定模块参数化。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| positive scalar，范围 [0,1]

用于考虑理论流动中流出损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`。

### **Maximum Cv flow coefficient** — 对应最大开度组件的 Cv 系数 `4`（默认）| positive scalar

当可用于流动的限制面积最大时 *Cv* 流量系数的值。此参数衡量湿空气在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，在该值处首次发生阻塞流。如果您没有此值，请在 ISA-75.01.01 [3] 的表 2 中查找。否则，对于许多阀而言，默认值 0.7 是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应最大开度组件的 Kv 系数 `3.6`（默认）| positive scalar

当可用于流动的限制面积最大时 *Kv* 流量系数的最大值。此参数衡量湿空气在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **Maximum sonic conductance** — 对应最大开度组件的声导 `12 l/(bar*s)`（默认）| positive scalar

当可用于流动的横截面积最大时的声导值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| positive scalar

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Subsonic index** — 用于表征亚音速流态下质量流量的指数 `0.5`（默认）| positive scalar

用于更准确计算亚音速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| scalar

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| positive scalar

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| positive scalar

节流孔关闭时流量与打开时流量的比值。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| positive scalar，范围 [0,1]

连续平滑因子，当节流孔处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Laminar flow pressure ratio** — 流动在层流与湍流流态之间转换时的压力比 `0.999`（默认）| positive scalar

流动在层流与湍流流态之间转换时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 湿空气端口处的流通面积 `0.01 m^2`（默认）| positive scalar

每个端口处垂直于流动路径的面积。各端口尺寸相等。此参数的值应与阻性元件所连接的组件的入口面积匹配。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的提升阀

Poppet Valve (MA) 模块表示一个带有平移球的节流孔，用于调节通过阀的流量。在完全关闭位置，球停在带孔的阀座上，并完全阻止流体在端口 **A** 和 **B** 之间通过。球与阀座之间的面积是阀的开口面积。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀的喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度达到饱和。当背压比达到该阀特有的临界值时，就会发生阻塞。该模块不捕捉超音速流动。

侧视图示意图，说明阀座、提升阀与开口面积之间的关系。阀座为 V 形。提升阀为矩形。开口面积为橙色梯形，表示发生流动的位置。

俯视图示意图，说明阀座、提升阀与开口面积之间的关系。阀座为外环。提升阀为填充的内圆。开口面积为提升阀与阀座之间的环带。

### 圆柱阀杆提升阀开口面积

阀的开口面积计算如下：

Aopen=πhsin(θ2)[ds+h2sin(θ)]+Aleak,

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是 **Seat cone angle**。
- *d*s 是 **Stem diameter**。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=ds[1+cos(θ2)−1]sin(θ).

对于任何大于 *h*max 的阀杆位移，*A*open 为最大节流孔面积与 **Leakage area** 之和：

Aopen=π4ds2+Aleak.

对于端口 **S** 处的信号与小于 0 的圆柱偏移的任何组合，最小阀面积为 **Leakage area**。

### 圆球提升阀开口面积

**Sharp-edged 阀座几何形状**

阀的开口面积计算如下：

Aopen,sharp−edged=πrO(Gsharp+h)2+rO2[1−rB2(Gsharp+h)2+rO2]+Aleak,

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离，如上图所示。
- *r*O 是阀座节流孔半径，由 **Orifice diameter** 计算得出。
- *r*B 是球半径，由 **Ball diameter** 计算得出。
- *G*sharp 是几何参数：Gsharp=rB2−rO2。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=2rB2−rO2+rOrO2+4rB22−Gsharp.

对于任何大于 *h*max 的球位移，*A*open 为最大节流孔面积与 **Leakage area** 之和：

Aopen=π4dO2+Aleak.

对于端口 **S** 处的信号与小于 0 的球偏移的任何组合，最小阀面积为 **Leakage area**。

**Conical 阀座几何形状**

阀的开口面积计算如下：

Aopen,conical=Gconicalh+π2sin(θ)sin(θ2)h2+Aleak,

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是 **Seat cone angle**。
- *G*conical 是几何参数：Gconical=πrBsin(θ)，其中 *r*B 是球半径。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=rB2+rO2cos(θ2)−rBsin(θ2).

对于任何大于 *h*max 的球位移，*A*open 为最大节流孔面积与 **Leakage area** 之和：

Aopen=π4dO2+Aleak.

对于端口 **S** 处的信号与小于 0 的球偏移的任何组合，最小阀面积为 **Leakage area**。

### 阀参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻性元件的声导决定模块参数化。声导衡量湿空气在 *choked* 时流动的难易程度，阻塞是指流速达到当地声速的工况。当下游与上游压力之比达到称为 *critical pressure ratio* 的临界值时，就会发生阻塞。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

该模块按阀开口比例缩放指定的流通能力。当阀开口比例从 `0` 升至 `1` 时，流通能力的度量从指定的最小值缩放至指定的最大值。

### 动量平衡

该模块方程取决于 **Valve parameterization** 参数。
当将 **Valve parameterization** 设置为 `Cv flow coefficient` 时，质量流率 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin,

其中：

- *Cv* 是 **Maximum Cv flow coefficient** 参数的值。
- *Sopen* 是阀门开度面积。
- *SMax* 是阀门完全打开时的最大阀门面积。
- *N6* 是等于 27.3 的常数，当质量流量以 kg/hr、压力以 bar、密度以 kg/m3 为单位时。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至高于 **Laminar flow pressure ratio** 参数 *Blam* 的值时，该模块平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至低于 1−FγxT 时，孔口变为阻塞，该模块切换到方程

m˙=23CvSopenSMaxN6FγxTpinρin.

当将 **Valve parameterization** 设置为 `Kv flow coefficient` 时，该模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **Valve parameterization** 参数为 `Kv flow coefficient` 或 `Cv flow coefficient` 时的质量流量方程的更多信息，请参阅 [2][3]。

当将 **Valve parameterization** 设置为 `Sonic conductance` 时，质量流率 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是 **Maximum sonic conductance** 参数的值。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至高于 **Laminar flow pressure ratio** 参数 *Blam* 的值时，该模块平滑过渡到方程的线性化形式，

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至低于临界压力比 *Bcrit* 时，孔口变为阻塞，该模块切换到方程

m˙=CSopenSMaxρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果将此设置用于具有高浓度痕量气体的湿空气，或对空气以外的流体建模，则可能需要按混合物比重的平方根来缩放声速传导。

有关当 **Valve parameterization** 参数为 `Sonic conductance` 时的质量流量方程的更多信息，请参阅 [1]。

当将 **Valve parameterization** 设置为 `Orifice area based on geometry` 时，质量流率 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ],

其中：

- *Sopen* 是阀门开度面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至高于 **Laminar flow pressure ratio** 参数 *Blam* 的值时，该模块平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至低于 (2γ+1)γγ−1 时，孔口变为阻塞，该模块切换到方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2.

有关当 **Valve parameterization** 参数为 `Orifice area based on geometry` 时的质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

该模块通过阀门保持质量守恒

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流率，下标 *w* 表示水蒸气，下标 *g* 表示痕量气体，下标 *d* 表示水滴。

### 能量平衡

该模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口流动过程中，不对流体做功，流体也不做功。能量仅能通过对流通过端口 **A** 和 **B** 流动。根据能量守恒原理，各端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是经由端口 **A** 或 **B** 进入阀门的能量流率。

### 假设和限制

- 此模块不模拟超声速流动。
