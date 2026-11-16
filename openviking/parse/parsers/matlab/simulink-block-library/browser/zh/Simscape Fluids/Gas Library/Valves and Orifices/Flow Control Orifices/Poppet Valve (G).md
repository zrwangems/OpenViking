---
type: simulink-block
title: 'Poppet Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Gas Library / Valves and Orifices / Flow Control Orifices'
documentation_page: 'poppetvalveg'
documentation_source_path: 'ref/poppetvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Poppet Valve (G)

## 端口

### 守恒端口

### **A** — Liquid port gas

与流进入或离开阀的开口相关联的气体守恒端口。

### **B** — Liquid port gas

与流进入或离开阀的开口相关联的气体守恒端口。

### 输入

### **L** — Normalized ball displacement, in the range of [0,1] physical signal

归一化球位移。球位置由最大开口距离归一化。值 0 表示完全关闭的阀，值 1 表示完全打开的阀。

## 参数

### **Valve seat specification** — 阀座几何的定义 `Sharp-edged` (默认) | `Conical`

球的阀座几何。此参数决定阀的开口面积。

### **Cone angle** — 阀的锥形阀座与其中心线之间的角度 `120 deg` (默认) | positive scalar

锥形阀座斜面与其中心线形成的角度。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Conical`。

### **Ball diameter** — 用于调节阀开口的球的直径 `0.01 m` (默认) | scalar

球控制元件的直径。

### **Orifice diameter** — 阀孔口的直径 `7e-3 m` (默认) | scalar

阀恒定孔口的直径。对于锥形几何，该直径是阀座根部的直径。

### **Valve parameterization** — 用于指定孔口流动特性的参数化 `Orifice area based on geometry` (默认) | `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

计算质量流率的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声导决定模块参数化。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

### **Discharge coefficient** — 排放系数 `0.64` (默认) | 范围 [0,1] 内的 positive scalar

用于考虑理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`。

### **Maximum Cv flow coefficient** — 对应于最大打开组件的 Cv 系数 `4` (默认) | positive scalar

当可用于流动的限制面积达到最大时 *Cv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7` (默认) | positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比，定义为 (pin−pout)/pin，其中首次发生阻塞。如果没有此值，请在 ISA-75.01.01 [3] 的表 2 中查找。否则，对于许多阀，默认值 0.7 是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应于最大打开组件的 Kv 系数 `3.6` (默认) | positive scalar

当可用于流动的限制面积达到最大时 *Kv* 流量系数的最大值。此参数衡量气体在压差驱动下穿过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **Maximum sonic conductance** — 对应于最大打开组件的声导 `12 l/(bar*s)` (默认) | positive scalar

当可用于流动的横截面积达到最大时声导的值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3` (默认) | positive scalar

压力比，在该压力比下流动首次开始阻塞，流速达到其最大值，即局部声速。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Subsonic index** — 用于表征亚声速流动状态下质量流量的指数 `0.5` (默认) | positive scalar

用于更准确计算亚声速流动状态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K` (默认) | scalar

标准参考大气中的温度，在 ISO 8778 中定义为 293.15 K。

只有当您使用在不同参考值下获得的声导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3` (默认) | positive scalar

标准参考大气中的密度，在 ISO 8778 中定义为 1.185 kg/m3。

只有当您使用在不同参考值下获得的声导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Leakage flow fraction** — 流率比 `1e-6` (默认) | positive scalar

孔口关闭时与打开时的流率之比。

### **Smoothing factor** — 数值平滑因子 `0.01` (默认) | 范围 [0,1] 内的 positive scalar

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，以提高在这些状态下仿真的稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间过渡时的压力比 `0.999` (默认) | positive scalar

流动在层流和湍流状态之间过渡时的压力比。压力比是出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 气体端口处的流动面积 `0.01 m^2` (默认) | positive scalar

每个端口处垂直于流动路径的面积。端口尺寸相等。此参数的值应与阻性元件连接到的组件的入口面积匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Flow Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b：使用改进的流量计算对气体系统建模

在以前的版本中，气体库中的模块使用转换因子以声导形式实现不同的孔口参数化。您可以使用 **Valve parameterization** 参数来指定参数化。

新的参数化还包括新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数替换了 **Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow** 和 **Restriction area at leakage flow** 参数。

为了提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference density** 参数已分别重命名为 **ISO reference temperature** 和 **ISO reference density**。
- **Cv coefficient (USCS) at maximum flow** 和 **Kv coefficient (USCS) at maximum flow** 参数已分别重命名为 **Maximum Cv coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic conductance**。

### R2022b：更新的模块名

Ball Valve (G) 模块的标题已更改为 Poppet Valve (G)。要在气体系统中使用球阀，请使用 Ball Valve (G) 模块。

### R2022b：移除了 Offset 参数

该模块不再具有 **Valve lift control offset** 参数，并且该模块不再对输入信号进行偏移。此更改不影响兼容性。

## 描述

气体网络中的提升阀

Poppet Valve (G) 模块表示一个带有平移球的孔口，该球调节通过阀的流量。在完全关闭位置，球停靠在穿孔阀座上，并完全阻止流体在端口 **A** 和 **B** 之间通过。球与阀座之间的面积是阀的开口面积。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀的喉部，此处流动最窄且最快。当下游压力下降不再能提高速度时，流动发生阻塞，速度饱和。当背压比达到阀的特征临界值时，发生阻塞。该模块不捕获超声速流动。

### 球体力学

该模块对球的位移建模，但不建模阀的打开或关闭动态。端口 **L** 处的信号提供归一化球位置 *L*。注意，*L* 是 0 到 1 之间的归一化距离，分别表示完全关闭的阀和完全打开的阀。如果计算返回此范围之外的数字，则该数字会被设置为最接近的边界。

**数值平滑**

当 **Smoothing factor** 参数非零时，该模块对归一化球位置 *L* 应用数值平滑。启用平滑有助于在仿真中保持数值稳健性。

有关详细信息，请参阅 Numerical Smoothing。

### 开口面积

阀的开口面积取决于 **Valve seat geometry** 参数，该参数可以是 `Sharp-edged` 或 `Conical`。**Leakage flow fraction** 参数是阀关闭时与打开时的流率之比。**Leakage flow fraction** 允许在完全关闭位置球与阀座之间存在小的接触间隙。此参数还为求解器性能保持流动连续性。

此图显示了提升阀的阀座类型。

**锐边阀座几何**

该模块按如下方式计算阀的开口面积

Sopen,sharp−edged=πrO(Gsharp+h)2+rO2[1−rB2(Gsharp+h)2+rO2],

其中：

- *h* 是圆柱外边缘与阀座之间的距离。
- *rO* 是阀座孔口半径，该模块根据 **Orifice diameter** 参数计算。
- *rB* 是球的半径，该模块根据 **Ball diameter** 参数计算。
- *Gsharp* 是几何参数：Gsharp=rB2−rO2。

最大位移 *hmax* 限制开口面积：

hmax=2rB2−rO2+rOrO2+4rB22−Gsharp.

对于任何大于 *hmax* 的球位移，*Sopen* 是最大孔口面积的值：

Sopen=π4dO2.

当端口 **L** 处的信号小于 0 时，阀关闭，**Leakage flow fraction** 参数决定质量流量。

**锥形阀座几何**

该模块按如下方式计算阀的开口面积：

Sopen,conical=Gconicalh+π2sin(θ)sin(θ2)h2,

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离。
- *θ* 是 **Cone angle** 参数的值。
- *Gconical* 是几何参数，Gconical=πrBsin(θ)，其中 *rB* 是球半径。

最大位移 *hmax* 限制开口面积：

hmax=rB2+rO2cos(θ2)−rBsin(θ2).

对于任何大于 *hmax* 的球位移，*Sopen* 是最大孔口面积的值：

Sopen=π4dO2.

当端口 **L** 处的信号小于 0 时，阀关闭，**Leakage flow fraction** 参数决定质量流量。

### 阀参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在一定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在一定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻性元件的声导决定模块参数化。声导衡量气体在 *choked* 时流动的难易程度，*choked* 是流速处于局部声速的状态。当下游压力与上游压力之比达到称为 *critical pressure ratio* 的临界值时，发生阻塞。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

该模块按阀开口分数缩放指定的流动能力。当阀开口分数从 `0` 上升到 `1` 时，流动能力的度量从其指定的最小值缩放到指定的最大值。

### 质量流量

模块方程取决于 **Orifice parametrization** 参数。
当 **Orifice parametrization** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin,

其中：

- *Cv* 是 **Maximum Cv flow coefficient** 参数的值。
- *Sopen* 是阀门开口面积。
- *SMax* 是阀门完全打开时的最大阀门面积。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升高到超过 **Laminar flow pressure ratio** 参数的值 *Blam* 时，模块平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至低于 1−FγxT 时，节流孔变为阻塞流，模块切换为以下方程

m˙=23CvSopenSMaxN6FγxTpinρin.

当 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **Orifice parametrization** 参数为 `Kv flow coefficient parameterization` 或 `Cv flow coefficient parameterization` 时质量流量方程的更多信息，请参阅 [2][3]。

当 **Orifice parametrization** 设置为 `Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是 **Maximum sonic conductance** 参数的值。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升高到超过 **Laminar flow pressure ratio** 参数的值 *Blam* 时，模块平滑过渡到方程的线性化形式，

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至低于临界压力比 *Bcrit* 时，节流孔变为阻塞流，模块切换为以下方程

m˙=CSopenSMaxρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置用于气动应用。如果对空气以外的气体使用此设置，可能需要按气体相对密度的平方根对声速流导进行缩放。

有关当 **Orifice parametrization** 参数为 `Sonic conductance parameterization` 时质量流量方程的更多信息，请参阅 [1]。

当 **Orifice parametrization** 设置为 `Orifice area based on geometry` 时，质量流量 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ],

其中：

- *Sopen* 是阀门开口面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升高到超过 **Laminar flow pressure ratio** 参数的值 *Blam* 时，模块平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至低于 (2γ+1)γγ−1 时，节流孔变为阻塞流，模块切换为以下方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2.

有关当 **Orifice parametrization** 参数为 `Orifice area based on geometry` 时质量流量方程的更多信息，请参阅 [4]。

### 能量平衡

模块的阻力元件是绝热组件。流体与其周围壁面之间不会发生热交换。当流体从入口流到出口时，既不对流体做功，流体也不对外做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀门的能量流率。

### 质量平衡

模块假定阀门内流体的体积和质量非常小，并忽略这些值。因此，流体不能在阀门内积聚。根据质量守恒原理，通过一个端口进入阀门的质量流量等于通过另一个端口流出阀门的质量流量

m˙A+m˙B=0,

其中 m˙ 定义为通过由下标 **A** 或 **B** 指示的端口进入阀门的质量流量。

### 假设与限制

- 对于 `Orifice area based on geometry` 参数化，其方程对于远离理想状态的气体精度较低。
- 此模块不对超声速流动进行建模。
