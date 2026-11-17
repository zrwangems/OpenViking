---
type: simulink-block
title: 'Gate Valve (MA)'
family: 'moist-air'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Flow Control Valves'
documentation_page: 'gatevalvema'
documentation_source_path: 'ref/gatevalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# Gate Valve (MA)

## 端口

### 输入

### **S** — 闸门位移，m 物理信号

与阀门闸门位移关联的物理信号端口，单位为 m。正信号使闸门缩回并打开阀门。

### 守恒

### **A** — 阀门入口或出口湿空气

与流体进入或离开阀门的开口关联的湿空气守恒端口。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

### **B** — 阀门入口或出口湿空气

与流体进入或离开阀门的开口关联的湿空气守恒端口。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

## 参数

### **Valve orifice diameter** — 阀的孔径 `0.01 m`（默认）| 正标量

阀门孔口的直径以及控制开口面积的闸门直径。假设孔口从一个端口到另一个端口的整个长度上横截面恒定。

### **Gate position when fully covering orifice** — 闸门偏移 `0` `m`（默认）| 正标量

阀门关闭时的闸门偏移。正值（非零）表示当端口 **S** 的信号为 0 时阀门部分打开。负值（非零）表示重叠阀门，在由端口 **S** 处物理信号设定的初始正位移期间保持关闭。

### **Valve parameterization** — 用于指定孔口流动特性的参数化 `Orifice area based on geometry`（默认）| `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻力元件的声导决定模块参数化。
- `Orifice area based on geometry` — 流动限流的大小决定模块参数化。

### **Discharge coefficient** — 排放系数 `0.64`（默认）| [0,1] 范围内的正标量

考虑理论流动中排放损失的修正系数。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`。

### **Maximum Cv flow coefficient** — 对应组件最大开度的 Cv 系数 `4`（默认）| 正标量

当可供流动的限流面积最大时 *Cv* 流量系数的值。该参数衡量湿空气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为发生阻塞流时的 (pin−pout)/pin。如果没有此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对许多阀门是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应组件最大开度的 Kv 系数 `3.6`（默认）| 正标量

当可供流动的限流面积最大时 *Kv* 流量系数的最大值。该参数衡量湿空气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **Maximum sonic conductance** — 对应组件最大开度的声导 `12 l/(bar*s)`（默认）| 正标量

当可供流动的横截面积最大时声导的值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Critical pressure ratio** — 流动首次发生阻塞时的下游与上游压力之比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

孔口关闭时的流量与打开时的流量之比。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入渐进变化层。将此参数设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流流态之间转换时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间转换时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 湿空气端口处的流通面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流路的面积。各端口尺寸相同。此参数的值应与阻力元件所连接组件的入口面积匹配。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Flow Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的闸阀

Gate Valve (MA) 模块表示一个具有平移闸门（或称 *闸板*）的孔口，作为流量控制机构。闸门为圆形，受其阀座凹槽约束，必须垂直于流动方向滑动。阀门的阀座为环形。流体通过孔，孔径与闸门尺寸匹配。闸门与孔的重叠量决定阀门的开口面积。

流动可以是层流或湍流，并且可达到声速。最大速度出现在阀门喉部，此处流动最窄且最快。当下游压力下降无法再提高速度时，流动发生阻塞且速度饱和。当背压比达到该阀门特有的临界值时发生阻塞。该模块不捕获超声速流动。

闸阀通常开启迅速。闸阀在关闭位置附近对闸门位移最敏感，此时很小的位移会导致开口面积发生不成比例的大变化。因此，闸阀在该区域增益过高，无法有效地节流或调节流量。你可以使用此模块作为二元开关来打开和关闭湿空气流。

### 闸门力学

在真实阀门中，闸门通过齿轮机构连接到手柄。当手柄从完全关闭位置转动时，闸门从孔中升起，并逐渐将阀门打开至最大开度。硬限位可防止阀盘超出其最小和最大位置。

该模块捕获阀盘的运动，但不捕获其力学细节。你将运动指定为端口 **S** 处的归一化位移。输入物理信号携带瞬时位移与阀门完全打开时位移值之比。

如果要建模手柄和硬限位的动作，请使用 Simscape 机械模块来捕获位移信号。然而，在许多情况下，只需知道要对阀盘施加什么位移即可，不需要建模阀门的力学。

### 闸门位置

该模块对闸门位移建模，但不对阀门打开或关闭动态建模。端口 **S** 处的信号提供闸门位置。

**数值平滑**

当 **Smoothing factor** 参数非零时，该模块对归一化闸门位置应用数值平滑。启用平滑有助于保持仿真的数值鲁棒性。

有关更多信息，请参阅数值平滑。

### 开口面积

闸门缩回时可供流动的面积为：

Aopen=πd024−Ashielded,

其中 *d*0 是 **Valve orifice diameter**。部分打开阀门中由闸门遮挡的面积为：

Ashielded=d022cos−1(Δld0)−Δl2d02−(Δl)2,

其中 *Δl* 是闸门位移，它等于端口 **S** 处信号与 **Gate position when fully covering orifice** 之和。

该图从左到右显示了阀门在最大关闭、部分打开和完全打开时的正视图。该图还显示了开口面积计算中使用的参数和变量。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量湿空气在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量湿空气在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声导决定模块参数化。声导衡量湿空气在 *阻塞* 时流动的难易程度；阻塞是指流速达到当地声速的状态。当下游与上游压力之比达到称为 *临界压力比* 的临界值时，发生阻塞。
- `Orifice area based on geometry` — 流动限流的大小决定模块参数化。

该模块按阀门开度分数缩放指定的流动能力。当阀门开度分数从 `0` 上升到 `1` 时，流动能力度量从指定的最小值缩放到指定的最大值。

### 动量平衡

模块方程取决于 **Valve parameterization** 参数。当将 **Valve parameterization** 设置为 `Cv flow coefficient` 时，质量流量 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin,

其中：
- *Cv* 是 **Maximum Cv flow coefficient** 参数的值。
- *Sopen* 是阀门开口面积。
- *SMax* 是阀门完全打开时的最大阀门面积。
- *N6* 是常量，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：
- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 上升到高于 **Laminar flow pressure ratio** 参数 *Blam* 的值时，模块平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 低于 1−FγxT 时，孔口发生阻塞，模块切换到方程

m˙=23CvSopenSMaxN6FγxTpinρin.

当将 **Valve parameterization** 设置为 `Kv flow coefficient` 时，模块使用相同的方程，但通过关系式 Kv=0.865Cv 用 *Kv* 替换 *Cv*。有关 **Valve parameterization** 参数为 `Kv flow coefficient` 或 `Cv flow coefficient` 时质量流量方程的更多信息，请参阅 [2][3]。

当将 **Valve parameterization** 设置为 `Sonic conductance` 时，质量流量 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：
- *C* 是 **Maximum sonic conductance** 参数的值。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 上升到高于 **Laminar flow pressure ratio** 参数 *Blam* 的值时，模块平滑过渡到方程的线性化形式，

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 低于临界压力比 *Bcrit* 时，孔口发生阻塞，模块切换到方程

m˙=CSopenSMaxρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果将此项设置用于含有高水平痕量气体的湿空气，或建模空气以外的流体，则可能需要用混合气相对密度的平方根来缩放声导。

有关 **Valve parameterization** 参数为 `Sonic conductance` 时质量流量方程的更多信息，请参阅 [1]。

当将 **Valve parameterization** 设置为 `Orifice area based on geometry` 时，质量流量 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ],

其中：
- *Sopen* 是阀门开口面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 上升到高于 **Laminar flow pressure ratio** 参数 *Blam* 的值时，模块平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 低于(2γ+1)γγ−1 时，孔口发生阻塞，模块切换到方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2.

有关 **Valve parameterization** 参数为 `Orifice area based on geometry` 时质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

该模块通过阀门保持质量守恒

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标 *g* 表示痕量气体，下标 *d* 表示水滴。

### 能量平衡

该模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口流动时，不对流体做功，流体也不对外做功。能量只能通过平流，经由端口 **A** 和 **B** 流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀门的能量流率。

### 假设与限制

- 该模块不对超音速流动建模。
