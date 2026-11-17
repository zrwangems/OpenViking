---
type: simulink-block
title: 'Poppet Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Flow Control Valves'
documentation_page: 'poppetvalvema'
documentation_source_path: 'ref/poppetvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# Poppet Valve (MA)

## 端口
```yaml
ports:
- name: A
  summary: 阀入口或出口湿空气
  direction: conserving
- name: B
  summary: 阀入口或出口湿空气
  direction: conserving
- name: S
  summary: 阀杆位移，m 物理信号
  direction: input
```

### 守恒端口

### **A** — 阀入口或出口湿空气

阀的液体入口或出口端口。

### **B** — 阀入口或出口湿空气

阀的液体入口或出口端口。

### 输入

### **S** — 阀杆位移，m 物理信号

阀控制部件的位移，单位为 m，指定为物理信号。
## 参数
```yaml
parameters:
- name: Poppet geometry
  summary: 阀芯类型 Cylindrical stem（默认）| Round ball
  group: ''
- name: Valve seat geometry
  summary: 阀座几何形状 Sharp-edged（默认）| Conical
  group: ''
- name: Ball diameter
  summary: 球形控制部件直径 0.01 m（默认）| 正标量
  group: ''
- name: Orifice diameter
  summary: 阀座孔口直径 7e-3 m（默认）| 正标量
  group: ''
- name: Stem diameter
  summary: 圆柱形阀杆直径 0.01 m（默认）| 正标量
  group: ''
- name: Seat cone angle
  summary: 阀座开口角度 120 deg（默认）| 正标量
  group: ''
- name: Control member position at closed orifice
  summary: 控制部件偏移量 0 m（默认）| 正标量
  group: ''
- name: Valve parameterization
  summary: 用于指定孔口流量特性的参数化方法 Orifice area based on geometry（默认）| Cv flow coefficient | Kv flow coefficient | Sonic conductance
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 范围 [0,1] 内的正标量
  group: ''
- name: Maximum Cv flow coefficient
  summary: 对应组件最大开启状态的 Cv 系数 4（默认）| 正标量
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: 压差比系数 0.7（默认）| 正标量
  group: ''
- name: Maximum Kv flow coefficient
  summary: 对应最大开度组件的 Kv 系数 3.6（默认）| 正标量
  group: ''
- name: Maximum sonic conductance
  summary: 对应最大开度组件的声速导 12 l/(bar*s)（默认）| 正标量
  group: ''
- name: Critical pressure ratio
  summary: 流动首次阻塞时的下游与上游压力比 0.3（默认）| 正标量
  group: ''
- name: Subsonic index
  summary: 用于表征亚声速流态中质量流量的指数 0.5（默认）| 正标量
  group: ''
- name: ISO reference temperature
  summary: ISO 8778 参考温度 293.15 K（默认）| 标量
  group: ''
- name: ISO reference density
  summary: ISO 8778 参考密度 1.185 kg/m^3（默认）| 正标量
  group: ''
- name: Leakage flow fraction
  summary: 流量比 1e-6（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: ''
- name: Laminar flow pressure ratio
  summary: 流动在层流和湍流流态之间过渡时的压力比 0.999（默认）| 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 湿空气端口处的流通面积 0.01 m^2（默认）| 正标量
  group: ''
```

### **Poppet geometry** — 阀芯类型 `Cylindrical stem`（默认）| `Round ball`

阀芯类型。您可以选择圆柱形或球形控制部件。

### **Valve seat geometry** — 阀座几何形状 `Sharp-edged`（默认）| `Conical`

阀座几何形状。该模块使用此参数计算阀芯与阀座之间的开口面积。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Ball diameter** — 球形控制部件直径 `0.01 m`（默认）| 正标量

球形控制部件的直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Orifice diameter** — 阀座孔口直径 `7e-3 m`（默认）| 正标量

阀座孔口直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Round ball`。

### **Stem diameter** — 圆柱形阀杆直径 `0.01 m`（默认）| 正标量

圆柱形阀杆的直径。

#### 依赖关系

要启用此参数，请将 **Poppet geometry** 设置为 `Cylindrical stem`。

### **Seat cone angle** — 阀座开口角度 `120 deg`（默认）| 正标量

阀座开口的角度。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Poppet geometry** 为 `Cylindrical stem`
- **Poppet geometry** 为 `Round ball` 且 **Valve seat geometry** 为 `Conical`

### **Control member position at closed orifice** — 控制部件偏移量 `0 m`（默认）| 正标量

阀关闭时的阀芯偏移量。正的、非零值表示阀部分打开。负的、非零值表示重叠阀，该阀在由端口 **S** 处的物理信号设定的初始位移期间保持关闭。

### **Valve parameterization** — 用于指定孔口流量特性的参数化方法 `Orifice area based on geometry`（默认）| `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速导纳决定模块参数化。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围 [0,1] 内的正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`。

### **Maximum Cv flow coefficient** — 对应组件最大开启状态的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积达到最大值时的 *Cv* 流量系数值。此参数衡量湿空气在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

首次发生阻塞时入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。如果您没有此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对许多阀来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应最大开度组件的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的节流面积达到最大值时的 *Kv* 流量系数最大值。此参数衡量湿空气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **Maximum sonic conductance** — 对应最大开度组件的声速导 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积达到最大值时的声速导值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时与打开时的流量之比。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，在节流孔处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流流态之间过渡时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间过渡时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 湿空气端口处的流通面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。各端口尺寸相同。此参数的值应与阻力元件所连接组件的入口面积相匹配。
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

Poppet Valve (MA) 模块表示一个带有平移球的节流孔，用于调节通过阀门的流量。在完全关闭位置，球停在多孔阀座上，完全阻止流体在端口 **A** 和 **B** 之间通过。球与阀座之间的区域即为阀门的开口面积。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降无法再增加速度时，流动发生阻塞，速度饱和。当背压比达到阀门特有的临界值时，发生阻塞。该模块不捕获超音速流动。

侧视图示意图，说明阀座、提升阀和开口面积之间的关系。阀座为 V 形。提升阀为矩形。开口面积为橙色梯形，表示流动发生的区域。

俯视图示意图，说明阀座、提升阀和开口面积之间的关系。阀座为外环。提升阀为填充的内圆。开口面积为提升阀与阀座之间的环。

### 圆柱杆提升阀开口面积

阀门的开口面积计算如下：

Aopen=πhsin(θ2)[ds+h2sin(θ)]+Aleak，

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是 **Seat cone angle**。
- *d*s 是 **Stem diameter**。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=ds[1+cos(θ2)−1]sin(θ)。

对于任何大于 *h*max 的杆位移，*A*open 为最大节流孔面积与 **Leakage area** 之和：

Aopen=π4ds2+Aleak。

对于端口 **S** 处的信号与小于 0 的圆柱偏移的任何组合，最小阀门面积为 **Leakage area**。

### 圆球提升阀开口面积

**锐边阀座几何形状**

阀门的开口面积计算如下：

Aopen,sharp−edged=πrO(Gsharp+h)2+rO2[1−rB2(Gsharp+h)2+rO2]+Aleak，

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离，如上图所示。
- *r*O 是阀座节流孔半径，由 **Orifice diameter** 计算得出。
- *r*B 是球的半径，由 **Ball diameter** 计算得出。
- *G*sharp 是几何参数：Gsharp=rB2−rO2。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=2rB2−rO2+rOrO2+4rB22−Gsharp。

对于任何大于 *h*max 的球位移，*A*open 为最大节流孔面积与 **Leakage area** 之和：

Aopen=π4dO2+Aleak。

对于端口 **S** 处的信号与小于 0 的球偏移的任何组合，最小阀门面积为 **Leakage area**。

**锥形阀座几何形状**

阀门的开口面积计算如下：

Aopen,conical=Gconicalh+π2sin(θ)sin(θ2)h2+Aleak，

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离，如上图所示。
- *θ* 是 **Seat cone angle**。
- *G*conical 是几何参数：Gconical=πrBsin(θ)，其中 *r*B 是球半径。
- *A*leak 是 **Leakage area**。

开口面积受最大位移 *h*max 限制：

hmax=rB2+rO2cos(θ2)−rBsin(θ2)。

对于任何大于 *h*max 的球位移，*A*open 为最大节流孔面积与 **Leakage area** 之和：

Aopen=π4dO2+Aleak。

对于端口 **S** 处的信号与小于 0 的球偏移的任何组合，最小阀门面积为 **Leakage area**。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。流量系数衡量在特定压差驱动下湿空气流动的难易程度。
- `Kv flow coefficient` — 流量系数
  *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量在特定压差驱动下湿空气流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声速导决定模块参数化。声速导衡量湿空气在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游与上游压力之比达到称为*临界压力比*的临界值时，发生阻塞。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

模块按阀门开度分数缩放指定的流通能力。当阀门开度分数从 `0` 上升到 `1` 时，流通能力的度量从其指定的最小值缩放到指定的最大值。

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
- *SMax* 是阀门完全
  打开时的最大
  阀门面积。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为
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
coefficient` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 用
*Kv* 替换
*Cv*。有关当
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

**Valve parameterization** 参数的 `Sonic conductance` 设置
适用于气动
应用。如果您将此设置用于带有高水平痕量气体的湿空气，或者正在建模空气以外的流体，您可能需要按混合物比重的平方根来缩放声速
导纳。

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

### 质量平衡

该模块通过阀门守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标 *g* 表示微量气体，下标 *d* 表示水滴。

### 能量平衡

该模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口流动时，不对流体做功，也不由流体做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀门的能量流率。

### 假设和限制

- 该模块不建模超声速流动。
