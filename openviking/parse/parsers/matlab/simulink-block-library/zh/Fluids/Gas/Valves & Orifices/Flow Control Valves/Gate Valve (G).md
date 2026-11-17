---
type: simulink-block
title: 'Gate Valve (G)'
family: 'hydro'
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

输入端口，用于将闸门的相对位移指定为其最大值的分数。该输入指定闸门位置，模块使用该位置计算通过阀门的质量流量。该位置的范围应为 `0`（阀门最大程度关闭）到 `1`（阀门完全打开）。
### 守恒

### **A** — 阀门入口气体

与开口关联的气体守恒端口，流体通过该开口进入或离开阀门。流动方向取决于阀门两端建立的压差。该模块允许正向和反向两个方向。

### **B** — 阀门入口气体

与开口关联的气体守恒端口，流体通过该开口进入或离开阀门。流动方向取决于阀门两端建立的压差。该模块允许正向和反向两个方向。

## 参数

### **Orifice diameter** — 阀门孔径的直径 `0.01 m`（默认）| 正标量

阀门孔径以及控制开口面积的闸门的直径。假设孔口从一个端口到另一个端口的整个长度上横截面恒定。

### **Valve parameterization** — 用于指定孔口流动特性的参数化方法 `Orifice area based on geometry`（默认）| `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。
- `Kv flow coefficient` — 流量系数
  *K*v，
  其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速导决定
  模块参数化。
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
值。该参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Cv flow
coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

首次发生阻塞时的入口压力 *pin* 与
出口压力 *pout* 之比，定义为 (pin−pout)/pin。如果您没有此值，
请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对
许多阀门来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Cv flow
coefficient` 或 `Kv flow
coefficient`。

### **Maximum Kv flow coefficient** — 对应于组件最大开启状态的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积达到最大值时的 *Kv* 流量
系数的最大值。该参数衡量气体在压差驱动下通过阻性
元件的难易程度。

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

### **Critical pressure ratio** — 流动首次发生阻塞时的下游与上游压力之比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到其最大值（由当地声速给出）时的
压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更精确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导值是在不同的参考值下获得时，才需要调整
ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导值是在不同的参考值下获得时，才需要调整
ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

孔口关闭时与打开时的流量之比。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入
一层渐变变化。将此参数设置为小于 1 的非零值，以提高在这些
工况下仿真的稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流流态之间过渡时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间过渡时的压力比。压力比为出口压力除以入口
压力。典型值范围为 `0.995` 到
`0.999`。

### **Cross-sectional area at ports A and B** — 气体端口处的流动面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。端口尺寸相等。
该参数的值应与阻性元件所连接的组件的入口面积相匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b: 使用改进的流量计算对气体系统建模

在之前的版本中，气体库中的模块使用转换因子来根据声速导纳实现不同的孔口参数化。您可以使用 **Valve parameterization** 参数来指定参数化。

新的参数化还包括新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数替换 **Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow** 和 **Restriction area at leakage flow** 参数。

为提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference density** 参数已分别重命名为 **ISO reference temperature** 和 **ISO reference density**。
- **Cv coefficient (USCS) at maximum flow** 和 **Kv coefficient (USCS) at maximum flow** 参数已分别重命名为 **Maximum Cv coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic conductance**。

### R2022b: 移除了 Offset 参数

该模块不再具有 **Gate displacement fraction offset** 参数，并且该模块不再对输入信号进行偏移。此更改不会影响兼容性。

## 描述

气体网络中的闸阀

Gate Valve (G) 模块表示一个带有平移闸板（或*闸门*）的孔口，作为流量控制机构。闸板是圆形的，并且由于其阀座凹槽的约束，必须垂直于流动方向滑动。阀座是环形的。流体通过孔径，孔径的大小与闸板匹配。闸板与孔径的重叠决定了阀门的开启面积。

此图显示了一个带有锥形阀座的闸阀。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度饱和。当背压比达到阀门特有的临界值时，就会发生阻塞。该模块不捕获超声速流动。

闸阀通常开启迅速。闸阀在接近关闭位置时对闸板位移最敏感，此时很小的位移会导致开启面积发生不成比例的巨大变化。因此，闸阀在该区域具有过高的增益，无法有效节流或调节流量。您可以将此模块用作打开和关闭气体回路的二元开关。

### 闸板力学

在实际阀门中，闸板通过齿轮机构连接到手柄。当手柄从完全关闭位置转动时，闸板从孔径上升，并逐渐打开阀门直至最大开度。硬限位可防止阀瓣越过其最小和最大位置。

该模块捕获阀瓣的运动，但不捕获其力学细节。您将运动指定为端口 **L** 处的归一化位移。输入物理信号携带瞬时位移在其完全打开阀门中的值中所占的比例。

如果您想要对 handle 和 hard stop 的作用进行建模，请使用 Simscape 机械模块来捕获位移信号。然而，在许多情况下，只需知道要施加给阀瓣的位移即可，不需要对阀门的力学进行建模。

### 闸板位置

该模块对闸板的位移建模，但不建模阀门开启或关闭动态。端口 **L** 处的信号提供归一化闸板位置 *L*。*L* 是介于 0 和 1 之间的归一化距离，分别表示完全关闭的阀门和完全打开的阀门。如果计算返回的数值超出此范围，该模块会将该数值设置为最接近的边界。

**数值平滑**

当 **Smoothing factor** 参数非零时，该模块会对归一化闸板位置 *L* 应用数值平滑。启用平滑有助于在仿真中保持数值稳健性。

有关详细信息，请参阅 Numerical Smoothing。

### 开启面积

阀门的开启面积是根据闸板瞬时重叠调整后的孔径面积

Sopen=pD24-SC，

其中：

- *Sopen* 是瞬时阀门开启面积。然后，该模块会对该面积进行平滑，以消除极限阀门位置处的导数不连续。
- *D* 是闸板及其孔径的共同直径，二者相同。这是 **Orifice diameter** 参数的值。
- *SC* 是闸板与孔径之间的重叠面积，该模块将其计算为闸板位置 *L* 的函数：

  SC=D22acos(L)−LD2D2−L2D2。

该图从左到右显示了阀门在最大关闭、部分打开和完全打开时的正视图。该图还显示了开启面积计算中的参数和变量。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声速导纳决定模块参数化。声速导纳衡量气体在*阻塞*状态下流动的难易程度，阻塞是指流动速度达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，就会发生阻塞。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

该模块按阀门开启比例缩放指定的流量能力。当阀门开启比例从 `0` 上升到 `1` 时，流量能力的度量从其指定的最小值缩放到指定的最大值。

### Momentum Balance

模块方程取决于 **Orifice parametrization** 参数。
当您将 **Orifice parametrization** 设置为 `Cv
flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin，

其中：

- *Cv* 是
  **Maximum Cv flow coefficient**
  参数的值。
- *Sopen* 是阀门
  开口面积。
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

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是
  等熵指数与 1.4 的比值。
- *xT* 是
  **xT pressure differential ratio factor at choked
  flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数
*Blam* 的值以上时，模块会平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞状态，模块切换到
方程

m˙=23CvSopenSMaxN6FγxTpinρin。

当您将 **Orifice parametrization** 设置为 `Kv flow
coefficient parameterization` 时，模块使用这些相同的
方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为
*Kv*。有关当
**Orifice parametrization** 参数为 `Kv
flow coefficient parameterization` 或 `Cv flow
coefficient parameterization` 时的质量流量方程的更多信息，请参阅 [2][3]。

当您将 **Orifice parametrization** 设置为 `Sonic
conductance parameterization` 时，质量流量 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

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

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降至临界压力比
*Bcrit* 以下时，孔口变为
阻塞状态，模块切换到方程

m˙=CSopenSMaxρrefpinTrefTin。

**Valve parameterization** 参数的 `Sonic conductance` 设置
用于气动应用。如果您将此设置用于空气以外的气体，则可能需要
按比重的平方根对声导进行缩放。

有关当 **Orifice
parametrization** 参数为 `Sonic conductance
parameterization` 时的质量流量方程的更多信息，请参阅 [1]。

当您将 **Orifice parametrization** 设置为
`Orifice area based on geometry` 时，质量流量
m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ]，

其中：

- *Sopen* 是阀门
  开口面积。
- *S* 是 **Cross-sectional
  area at ports A and B** 参数的值。
- *Cd* 是
  **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数
*Blam* 的值以上时，模块会平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口变为阻塞状态，模块切换到
方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2。

有关当 **Orifice
parametrization** 参数为 `Orifice area based on
geometry` 时的质量流量方程的更多信息，请参阅 [4]。

### Mass Balance

模块假定阀门内部流体的体积和质量非常小，并
忽略这些值。因此，不会有任何数量的流体在阀门中积聚。
根据质量守恒原理，通过
一个端口进入阀门的质量流量等于通过另一个端口流出阀门的质量流量

m˙A+m˙B=0，

其中 m˙ 定义为通过由 **A** 或 **B** 下标指示的端口进入阀门的质量流量。

### Energy Balance

模块的阻性元件是绝热组件。流体与其周围
壁面之间不会发生热交换。流体从入口到出口流动时，不会对流体做功，也不会由流体做功。能量只能通过
端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口
能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口
**A** 或 **B** 进入阀门的能量流率。

### 假设和限制

- `Orifice area based on
  geometry` 参数化的方程对于远离理想气体的气体
  精度较低。
- 此模块不建模超声速流动。
