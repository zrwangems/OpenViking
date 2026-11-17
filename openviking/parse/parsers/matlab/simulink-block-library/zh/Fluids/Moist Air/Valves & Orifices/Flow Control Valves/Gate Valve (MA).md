---
type: simulink-block
title: 'Gate Valve (MA)'
family: 'hydro'
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

与阀门闸门位移相关联的物理信号端口，单位为
m。正信号使闸门回缩并打开阀门。
### 守恒

### **A** — 阀门入口或出口湿空气

与流体进入或离开阀门的开口相关联的湿空气守恒端口。流动方向取决于阀门两端建立的
压差。该模块允许正向和反向两个方向。

### **B** — 阀门入口或出口湿空气

与流体进入或离开阀门的开口相关联的湿空气守恒端口。流动方向取决于阀门两端建立的
压差。该模块允许正向和反向两个方向。

## 参数

### **Valve orifice diameter** — 阀门孔径 `0.01 m`（默认）| 正标量

阀门孔径以及控制开口面积的闸门直径。假设节流孔从一个端口到另一个端口的整个长度上
横截面恒定。

### **Gate position when fully covering orifice** — 闸门偏移 `0` `m`（默认）| 正标量

阀门关闭时的闸门偏移。正的、非零值表示当端口 **S** 处信号为 0 时阀门部分打开。
负的、非零值表示重叠阀门，该阀门在端口 **S** 处物理信号设定的初始正位移期间保持关闭。

### **Valve parameterization** — 用于指定节流孔流动特性的参数化方法 `Orifice area based on geometry`（默认）| `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

计算质量流量的方法。

- `Cv flow coefficient` — 流量
  系数
  *C*v
  决定模块参数化。
- `Kv flow coefficient` — 流量
  系数
  *K*v，
  其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速
  导决定模块参数化。
- `Orifice area based on geometry` — 流动限制的
  尺寸决定模块参数化。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围 [0,1] 内的正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Orifice area based on
geometry`。

### **Maximum Cv flow coefficient** — 对应于组件最大开启状态的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积达到最大值时的 *Cv* 流量系数
值。此参数衡量湿空气在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Cv flow
coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

首次发生阻塞时的入口压力
*pin* 与出口压力
*pout* 之比，定义为 (pin−pout)/pin。如果您没有此值，
请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对
许多阀门来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Cv flow
coefficient` 或 `Kv flow
coefficient`。

### **Maximum Kv flow coefficient** — 对应于组件最大开启状态的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积达到最大值时的 *Kv* 流量
系数最大值。此参数衡量湿空气在压差驱动下通过
阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Kv flow
coefficient`。

### **Maximum sonic conductance** — 对应于组件最大开启状态的声速导 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积达到最大值时的声速导
值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比
为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **Subsonic index** — 用于表征亚声速流态质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态下质量流量的经验
值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO
8778 中定义为 293.15 K。

仅当您使用的声速导值是在不同参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO
8778 中定义为 1.185 kg/m3。

仅当您使用的声速导值是在不同参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时与打开时的流量之比。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当节流孔处于接近打开或接近关闭位置时，为流量响应引入一层渐变
变化。将此参数设置为小于 1 的非零值，以提高这些工况下仿真的
稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流流态之间转换时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间转换时的压力比。压力比为出口压力除以入口
压力。典型值范围为 `0.995` 到
`0.999`。

### **Cross-sectional area at ports A and B** — 湿空气端口处的流通面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。端口尺寸相等。此参数的值
应与阻性元件所连接的组件的入口面积相匹配。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的闸阀

Gate Valve (MA) 模块表示一个带有平移闸板（或称*闸门*）的节流孔，作为流量控制机构。闸板为圆形，由于阀座凹槽的约束，必须垂直于流向滑动。阀座为环形。流体通过孔径，孔径尺寸与闸板匹配。闸板与孔径的重叠决定了阀的开口面积。

流体可以是层流或湍流，并且可以达到声速。最大速度发生在阀的喉部，此处流道最窄、流速最快。当下游压力下降无法再提高流速时，流体发生阻塞，速度饱和。当背压比达到阀的临界值时发生阻塞。该模块不捕获超声速流动。

闸阀通常开启迅速。闸阀在接近关闭位置时对闸板位移最为敏感，此时微小的位移会导致开口面积发生不成比例的巨大变化。因此，闸阀在该区域的增益过高，无法有效节流或调节流量。您可以将此模块用作开闭湿空气流的二元开关。

### 闸板力学

在实际阀中，闸板通过齿轮机构与手柄连接。当手柄从全关位置转动时，闸板从孔径中升起，逐渐打开阀门直至最大开度。硬限位防止阀板超出其最小和最大位置。

该模块捕获阀板的运动，但不包含其力学细节。您将运动指定为端口 **S** 处的归一化位移。输入物理信号携带瞬时位移与全开阀位移的比值。

如果您想对 handle 和硬限位的动作进行建模，请使用 Simscape 机械模块来捕获位移信号。然而，在许多情况下，只需知道施加给阀板的位移即可，无需对阀的力学进行建模。

### 闸板位置

该模块对闸板的位移进行建模，但不包含阀的开启或关闭动态特性。端口 **S** 处的信号提供闸板位置。

**数值平滑**

当 **Smoothing factor** 参数非零时，模块对归一化闸板位置应用数值平滑。启用平滑有助于在仿真中保持数值鲁棒性。

有关详细信息，请参阅数值平滑。

### 开口面积

闸板缩回时流体通过的面积为：

Aopen=πd024−Ashielded，

其中 *d*0 是 **Valve orifice diameter**。部分开启阀中闸板遮挡的面积为：

Ashielded=d022cos−1(Δld0)−Δl2d02−(Δl)2，

其中 *Δl* 是闸板位移，即端口 **S** 处信号与 **Gate position when fully covering orifice** 之和。

该图从左到右显示了阀在最大关闭、部分开启和全开状态下的正视图。该图还显示了开口面积计算中的参数和变量。

### 阀参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量湿空气在一定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻性元件的声导决定模块参数化。声导衡量湿空气在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时发生阻塞。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

模块按阀开度比例缩放指定的流通能力。当阀开度比例从 `0` 升至 `1` 时，流通能力的度量从其指定的最小值缩放至指定的最大值。

### Momentum Balance

模块方程取决于 **Valve parameterization** 参数。
当您将 **Valve parameterization** 设置为 `Cv flow
coefficient` 时，质量流量 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin,

其中：

- *Cv* 是
  **Maximum Cv flow coefficient**
  参数的值。
- *Sopen* 是阀门
  开度面积。
- *SMax* 是阀门完全打开时的最大
  阀门面积。
- *N6* 是一个常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为
  kg/m3 时，其值等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口
  压力。
- *pout* 是出口
  压力。
- *ρin* 是入口
  密度。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是
  等熵指数与 1.4 的比值。
- *xT* 是
   **xT pressure differential ratio factor at choked
  flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数
*Blam* 的值以上时，模块会平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞状态，模块切换到
方程

m˙=23CvSopenSMaxN6FγxTpinρin.

当您将 **Valve parameterization** 设置为 `Kv flow
coefficient` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将
*Cv* 替换为
*Kv*。有关当
**Valve parameterization** 参数为 `Kv
flow coefficient` 或 `Cv flow
coefficient` 时的质量流量方程的更多信息，请参阅 [2][3]。

当您将 **Valve parameterization** 设置为 `Sonic
conductance` 时，质量流量 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是 **Maximum sonic
  conductance** 参数的值。
- *Bcrit* 是临界
  压力比。
- *m* 是 **Subsonic
  index** 参数的值。
- *Tref* 是
  **ISO reference temperature** 参数的值。
- *ρref* 是
  **ISO reference density** 参数的值。
- *Tin* 是入口
  温度。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数
*Blam* 的值以上时，模块会平滑过渡到方程的线性化形式，

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比
*Bcrit* 以下时，孔口变为
阻塞状态，模块切换到方程

m˙=CSopenSMaxρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动
应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者正在建模空气以外的流体，您可能需要按混合物比重的平方根来缩放声导。

有关当 **Valve
parameterization** 参数为 `Sonic
conductance` 时的质量流量方程的更多信息，请参阅 [1]。

当您将 **Valve parameterization** 设置为 `Orifice area
based on geometry` 时，质量流量 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ],

其中：

- *Sopen* 是阀门
  开度面积。
- *S* 是 **Cross-sectional
  area at ports A and B** 参数的值。
- *Cd* 是
  **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数
*Blam* 的值以上时，模块会平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至(2γ+1)γγ−1 以下时，孔口变为阻塞状态，模块切换到
方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2.

有关当 **Valve
parameterization** 参数为 `Orifice area based on
geometry` 时的质量流量方程的更多信息，请参阅 [4]。

### Mass Balance

模块通过阀门守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标
*g* 表示痕量气体，下标 *d*
表示水滴。

### Energy Balance

模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口流动时，没有对流体做功，也没有由流体做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是通过端口
**A** 或 **B** 进入阀门的能量流率。

### 假设和限制

- 该模块不建模超声速流动。
