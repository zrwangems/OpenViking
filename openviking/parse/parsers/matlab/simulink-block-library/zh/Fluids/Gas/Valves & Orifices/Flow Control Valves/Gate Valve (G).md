---
type: simulink-block
title: 'Gate Valve (G)'
family: 'gas'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Flow Control Valves'
documentation_page: 'gatevalveg'
documentation_source_path: 'ref/gatevalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Gate Valve (G)

## 端口

### 输入

### **L** — 阀门控制信号，`unitless` 物理信号

输入端口，用于将闸门的相对位移指定为其最大值的分数。此输入指定闸门位置，模块使用该位置计算通过阀门的质量流量。此位置的范围应为 `0`（阀门最大程度关闭）到 `1`（阀门完全打开）。

### 守恒

### **A** — 阀门入口气体

与开口关联的气体守恒端口，流动通过该开口进入或离开阀门。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

### **B** — 阀门入口气体

与开口关联的气体守恒端口，流动通过该开口进入或离开阀门。流动方向取决于阀门两端建立的压差。该模块允许正向和反向流动。

## 参数

### **孔口直径** — 阀门孔径的直径 `0.01 m`（默认）| 正标量

阀门孔径以及控制开口面积的闸门的直径。假设孔口从一个端口到另一个端口的整个长度上横截面恒定。

### **阀门参数化** — 用于指定孔口流动特性的参数化 `Orifice area based on geometry`（默认）| `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

用于计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声导决定模块参数化。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

### **流出系数** — 流出系数 `0.64`（默认）| [0,1] 范围内的正标量

用于考虑理论流动中流出损失的修正因子。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Orifice area based on geometry`。

### **最大 Cv 流量系数** — 对应于最大打开组件的 Cv 系数 `4`（默认）| 正标量

当可供流动的限制面积最大时，*Cv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Cv flow coefficient`。

### **阻塞流下的 xT 压差比因子** — 压差比 `0.7`（默认）| 正标量

首次发生阻塞时的入口压力 *pin* 与出口压力 *pout* 之比，定义为 (pin−pout)/pin。如果您没有此值，请在 ISA-75.01.01 [3] 的表 2 中查找。否则，对于许多阀门，默认值 0.7 是合理的。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **最大 Kv 流量系数** — 对应于最大打开组件的 Kv 系数 `3.6`（默认）| 正标量

当可供流动的限制面积最大时，*Kv* 流量系数的最大值。此参数衡量气体在压差驱动下穿过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Kv flow coefficient`。

### **最大声导** — 对应于最大打开组件的声导 `12 l/(bar*s)`（默认）| 正标量

当可供流动的横截面积最大时，声导的值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **临界压力比** — 流动首次阻塞时的下游与上游压力之比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到其最大值（由当地声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于在亚声速流态中更准确地计算质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声导值是在不同的参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **泄漏流量分数** — 流量比 `1e-6`（默认）| 正标量

孔口关闭时的流量与打开时的流量之比。

### **平滑因子** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值，可提高这些状态下仿真的稳定性。

### **层流压力比** — 流动在层流和湍流流态之间转换时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间转换时的压力比。压力比是出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **端口 A 和 B 的横截面积** — 气体端口处的流动面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。端口尺寸相等。此参数的值应与阻性元件连接到的组件的入口面积匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2018b 中引入**

### R2022b：使用改进的流量计算对气体系统建模

在以前的版本中，气体库中的模块使用转换因子来以声导形式实现不同的孔口参数化。您可以使用 **阀门参数化** 参数指定参数化。

新的参数化还包括新参数：

- **阻塞流下的 xT 压差比因子**
- **流出系数**
- **泄漏流量分数**。此参数替换 **泄漏流量下的 Cv 系数 (USCS)**、**泄漏流量下的 Kv 系数 (SI)**、**泄漏流量下的声导** 和 **泄漏流量下的限制面积** 参数。

为提高清晰度：

- **开启参数化** 参数已重命名为 **开启特性**。
- **参考温度** 和 **参考密度** 参数已分别重命名为 **ISO 参考温度** 和 **ISO 参考密度**。
- **最大流量下的 Cv 系数 (USCS)** 和 **最大流量下的 Kv 系数 (USCS)** 参数已分别重命名为 **最大 Cv 系数** 和 **最大 Kv 系数**。
- **最大流量下的声导** 参数已重命名为 **最大声导**。

### R2022b：偏移参数已移除

该模块不再具有 **闸门位移分数偏移** 参数，并且该模块不再对输入信号进行偏移。此更改不影响兼容性。

## 描述

气体网络中的闸阀

Gate Valve (G) 模块表示一个带有平移闸门（或*闸板*）的孔口，作为流量控制机构。闸门为圆形，由于阀座凹槽的限制，必须垂直于流动方向滑动。阀门阀座为环形。流体通过孔口，孔口尺寸与闸门匹配。闸门与孔口的重叠决定阀门的开口面积。

此图显示了一个带锥形阀座的闸阀。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能提高速度时，流动发生阻塞且速度饱和。当背压比达到阀门特有的临界值时，发生阻塞。该模块不捕获超声速流动。

闸阀通常开启迅速。闸阀在关闭位置附近对闸门位移最敏感，在此处小的位移会转化为开口面积不成比例的大变化。因此，闸阀在该区域增益过高，无法有效地节流或调节流量。您可以将此模块用作二进制开关来打开和关闭气体回路。

### 闸门力学

在实际阀门中，闸门通过齿轮机构连接到手柄。当手柄从完全关闭位置转动时，闸门从孔口升起，并使阀门逐渐打开至最大。硬限位可防止阀盘超出其最小和最大位置。

该模块捕获阀盘的运动，但不捕获其力学的细节。您将运动指定为端口 **L** 处的归一化位移。输入物理信号携带瞬时位移与阀门完全打开时的位移值之比。

如果您想对硬限位和手柄的动作建模，请使用 Simscape 机械模块来捕获位移信号。然而，在许多情况下，只需知道要向阀盘施加什么位移，而不需要对阀门的力学进行建模。

### 闸门位置

该模块对闸门位移建模，但不建阀门开启或关闭动态。端口 **L** 处的信号提供归一化闸门位置 *L*。*L* 是介于 0 和 1 之间的归一化距离，分别表示完全关闭的阀门和完全打开的阀门。如果计算返回此范围之外的数值，该模块会将该数值设置为最接近的边界。

**数值平滑**

当 **平滑因子** 参数非零时，该模块对归一化闸门位置 *L* 应用数值平滑。启用平滑有助于保持仿真的数值稳健性。

有关详细信息，请参阅数值平滑。

### 开口面积

阀门的开口面积是根据闸门的瞬时重叠调整后的孔口面积

Sopen=pD24-SC,

其中：

- *Sopen* 是瞬时阀门开口面积。然后该模块对此面积进行平滑，以消除在极限阀门位置处的导数不连续性。
- *D* 是闸门及其孔口的共同直径，二者相同。这是 **孔口直径** 参数的值。
- *SC* 是闸门与孔口之间的重叠面积，该模块将其计算为闸门位置 *L* 的函数：

SC=D22acos(L)−LD2D2−L2D2.

该图从左到右显示了阀门在最大关闭、部分打开和完全打开时的正视图。该图还显示了开口面积计算中的参数和变量。

### 阀门参数化

模块行为取决于 **阀门参数化** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻性元件的声导决定模块参数化。声导衡量气体在*阻塞*时流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，发生阻塞。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

该模块按阀门开度分数缩放指定的流动容量。当阀门开度分数从 `0` 上升到 `1` 时，流动容量度量从指定的最小值缩放到指定的最大值。

### 动量平衡

模块方程取决于 **Orifice parametrization** 参数。
当你将 **Orifice parametrization** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin,

其中：

- *Cv* 是 **Maximum Cv flow coefficient** 参数的值。
- *Sopen* 是阀门开口面积。
- *SMax* 是阀门完全打开时的最大阀门面积。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，等于 27.3。
- *Y* 是膨胀因子。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀因子为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞，模块切换到方程

m˙=23CvSopenSMaxN6FγxTpinρin.

当你将 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **Orifice parametrization** 参数为 `Kv flow coefficient parameterization` 或 `Cv flow coefficient parameterization` 时的质量流量方程的更多信息，请参阅 [2][3]。

当你将 **Orifice parametrization** 设置为 `Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是 **Maximum sonic conductance** 参数的值。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口变为阻塞，模块切换到方程

m˙=CSopenSMaxρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置用于气动应用。如果你将此设置用于空气以外的气体，则可能需要用比重的平方根来缩放声导。

有关当 **Orifice parametrization** 参数为 `Sonic conductance parameterization` 时的质量流量方程的更多信息，请参阅 [1]。

当你将 **Orifice parametrization** 设置为 `Orifice area based on geometry` 时，质量流量 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ],

其中：

- *Sopen* 是阀门开口面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口变为阻塞，模块切换到方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2.

有关当 **Orifice parametrization** 参数为 `Orifice area based on geometry` 时的质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

模块假设阀门内部流体的体积和质量非常小，并忽略这些值。因此，任何数量的流体都不能在阀门中积聚。根据质量守恒原理，通过一个端口流入阀门的质量流量等于通过另一个端口流出阀门的质量流量

m˙A+m˙B=0,

其中 m˙ 定义为通过下标 **A** 或 **B** 所指示端口流入阀门时的质量流量。

### 能量平衡

模块的阻性元件是绝热组件。流体与其周围壁面之间不能发生热交换。流体从入口到出口流动时，没有对流体做功或由流体做功。能量只能通过对流通过端口 **A** 和 **B** 流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是通过端口 **A** 或 **B** 流入阀门的能量流率。

### 假设和限制

- 对于远离理想气体的气体，`Orifice area based on geometry` 参数化的方程准确度较低。
- 此模块不对超声速流动建模。
