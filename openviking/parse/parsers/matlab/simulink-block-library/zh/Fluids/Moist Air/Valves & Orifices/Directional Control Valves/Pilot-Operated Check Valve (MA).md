---
type: simulink-block
title: 'Pilot-Operated Check Valve (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Directional Control Valves'
documentation_page: 'pilotoperatedcheckvalvema'
documentation_source_path: 'ref/pilotoperatedcheckvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# Pilot-Operated Check Valve (MA)

## 端口
```yaml
ports:
- name: A
  summary: 阀入口或出口湿空气
  direction: conserving
- name: B
  summary: 阀入口或出口湿空气
  direction: conserving
- name: X
  summary: 先导端口湿空气
  direction: conserving
```

### 守恒端口

### **A** — 阀入口或出口湿空气

与常开开口关联的湿空气守恒端口，当先导机构禁用时，在正常运行期间流量通过该开口进入阀。仅当先导端口加压到足够程度时，该端口才可用作出口。

### **B** — 阀入口或出口湿空气

与常开开口关联的湿空气守恒端口，当先导机构禁用时，在正常运行期间流量通过该开口离开阀。

### **X** — 先导端口湿空气

与先导机构关联的湿空气守恒端口，通过施加足够的压力来致动先导机构，从而打开阀以实现反向流动。该端口没有质量流量。
## 参数
```yaml
parameters:
- name: Valve parameterization
  summary: 用于指定节流孔流动特性的参数化方法 Cv flow coefficient（默认）| Kv flow coefficient | Sonic conductance | Orifice area
  group: ''
- name: Pilot configuration
  summary: 处理负先导压力作用力的方法 Rigidly connected pilot spool and poppet（默认）| Disconnected pilot spool and poppet
  group: ''
- name: Pilot pressure specification
  summary: 选择用作阀控制信号的压力测量 Pressure difference of port X relative to port A（默认）| Gauge pressure at port X
  group: ''
- name: Cracking pressure differential
  summary: 阀首次打开时的有效控制压力 0.01 MPa（默认）| 正标量
  group: ''
- name: Maximum opening pressure differential
  summary: 阀完全打开时的有效控制压力 0.02 MPa（默认）| 正标量
  group: ''
- name: Pilot ratio
  summary: 先导端口面积与入口端口面积之比 1（默认）| 正标量
  group: ''
- name: Maximum Cv flow coefficient
  summary: 对应于组件最大开启状态的 Cv 系数 4（默认）| 正标量
  group: ''
- name: xT pressure differential ratio factor at choked flow
  summary: 压差比 0.7（默认）| 正标量
  group: ''
- name: Maximum Kv flow coefficient
  summary: 对应于组件最大开启状态的 Kv 系数 3.6（默认）| 正标量
  group: ''
- name: Maximum sonic conductance
  summary: 对应于组件最大开启状态的声速导 12 l/(bar*s)（默认）| 正标量
  group: ''
- name: Critical pressure ratio
  summary: 流动首次阻塞时的下游与上游压力之比 0.3（默认）| 正标量
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
- name: Maximum orifice area
  summary: 对应于组件最大开启状态的流动面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 范围在 [0,1] 内的正标量
  group: ''
- name: Leakage flow fraction
  summary: orifice 关闭时与打开时的流量比 1e-6（默认）| 正标量
  group: ''
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: ''
- name: Laminar flow pressure ratio
  summary: 流动在层流与湍流状态之间转换时的压力比 0.999（默认）| 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 湿空气端口处的流通面积 0.01 m^2（默认）| 正标量
  group: ''
```

### **Valve parameterization** — 用于指定节流孔流动特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。
- `Kv flow coefficient` — 流量系数
  *K*v，
  其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速导决定
  模块参数化。
- `Orifice area` — 流动限制的尺寸决定
  模块参数化。

### **Pilot configuration** — 处理负先导压力作用力的方法 `Rigidly connected pilot spool and poppet`（默认）| `Disconnected pilot spool and poppet`

当先导压力为负时模块使用的方法：

- `Rigidly connected pilot spool and
  poppet` — 先导滑阀传递正负先导压力作用力，
  因此模块按原样使用
  *ppilot*。
- `Disconnected pilot spool and poppet` —
  先导滑阀仅传递正先导压力作用力，因此
  模块将 *ppilot* 限制为
  仅正值。模块将负值替换为
  零。

### **Pilot pressure specification** — 选择用作阀控制信号的压力测量 `Pressure difference of port X relative to port A`（默认）| `Gauge pressure at port X`

选择用作阀控制信号的压力测量。模块使用此设置来确定阀应何时开始打开。在默认设置 `Pressure difference of port X relative to port
A` 下，阀的开启压力表示为从先导端口 **X** 到入口
**A** 的压降。在替代设置 `Gauge
pressure at port X` 下，它表示为相对于环境压力测量的入口表压。

### **Cracking pressure differential** — 阀首次打开时的有效控制压力 `0.01 MPa`（默认）| 正标量

阀开始打开时的有效压差。该压差是从入口到出口的压降与先导压力和先导比的乘积之和。所使用的先导压力取决于 **Pilot pressure
specification** 参数的设置。

### **Maximum opening pressure differential** — 阀完全打开时的有效控制压力 `0.02 MPa`（默认）| 正标量

阀完全打开时的有效压差。该压差是从入口到出口的压降与先导压力和先导比的乘积之和。所使用的先导压力取决于 **Pilot pressure
specification** 参数的设置。

### **Pilot ratio** — 先导端口面积与入口端口面积之比 `1`（默认）| 正标量

先导端口面积与入口端口面积之比。

### **Maximum Cv flow coefficient** — 对应于组件最大开启状态的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积达到最大时 *Cv* 流量系数的值。该参数衡量湿空气在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Cv flow
coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力
*pout* 之间的比值，定义为 (pin−pout)/pin，此时首次发生阻塞。如果您没有此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对许多阀来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Cv flow
coefficient` 或 `Kv flow
coefficient`。

### **Maximum Kv flow coefficient** — 对应于组件最大开启状态的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积达到最大时 *Kv* 流量系数的最大值。该参数衡量湿空气在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Kv flow
coefficient`。

### **Maximum sonic conductance** — 对应于组件最大开启状态的声速导 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积达到最大时的声速导值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力之比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导值是在不同参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导值是在不同参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Sonic
conductance`。

### **Maximum orifice area** — 对应于组件最大开启状态的流动面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积达到最大时节流孔开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Orifice
area`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围在 [0,1] 内的正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve
parameterization** 设置为 `Orifice
area`。

### **Leakage flow fraction** —  orifice 关闭时与打开时的流量比 `1e-6`（默认）| 正标量

orifice 关闭时与打开时的流量比。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，用于在 orifice 接近打开或接近关闭位置时为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，可提高仿真在这些工况下的稳定性。

### **Laminar flow pressure ratio** — 流动在层流与湍流状态之间转换时的压力比 `0.999`（默认）| 正标量

流动在层流与湍流状态之间转换时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 湿空气端口处的流通面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。各端口尺寸相同。此参数的值应与阻力元件所连接组件的入口面积相匹配。
## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的先导式单向阀

Pilot-Operated Check Valve (MA) 模块表示一种带有超控机构的单向阀，允许湿空气域中的反向流动。单向阀是一种带有单向开启机构的 orifice，可防止反向流动。

模块的 **X** 端口表示一个先导端口，用作超控机构。在正常运行期间，先导端口不活动，阀门表现为单向阀。在单向阀中，只有当阀门两端的压力梯度从入口到出口下降时，orifice 才会打开。orifice 的开启可防止反向流动，而反向流动需要反向压力梯度，并保护阀门上游组件免受下游压力冲击、温度尖峰和化学污染的影响。

当端口 **X** 处的值足够大时，模块对先导端口加压，并将阀门的控制元件推离阀座，从而允许反向流动。此时阀门在两个方向上均对流动开放，从出口到入口的反向压降驱动流动向上游流动。位于流动路径中的阀座决定阀门是否打开。当阀座被覆盖时，流动被切断，阀门关闭。

阀门在开启压力下开始打开，并持续打开直至压力调节范围结束。开启压力是阀门必须克服的初始阻力，由摩擦力或弹簧力引起，以开始打开。低于此阈值时，阀门关闭，只有泄漏流量可以通过。超过压力调节范围终点后，阀门完全打开，最大流量由瞬时压力条件决定。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度饱和。当背压比达到阀门特有的临界值时，发生阻塞。该模块不捕捉超声速流动。

### 控制压力及其他压力

阀门的开度取决于先导压力和从入口到出口的压降。打开阀门的压力为

PCtrl=kpilotPpilot+PA-PB，

其中：

- *Ppilot* 是先导压力。
- *kpilot* 是先导比。
- *PA* 是端口 **A** 处的表压。
- *PB* 是端口 **B** 处的表压。

模块在仿真期间基于绝对零位确定端口压力。

先导压力可以相对于入口（端口 **A**）或相对于环境。您可以通过将 **Pilot pressure specification** 参数设置为 `Pressure difference of port X relative to port B` 或 `Gauge pressure at port X` 来选择先导压力。

如果选择 `Gauge pressure at port X`，则先导压力为

Ppilot=PX−Patm，

其中 *PAtm* 是大气压力，*PX* 是先导端口压力的绝对值。如果选择 `Pressure difference of port X relative to port A`，则先导压力为

Ppilot=PX−PA，

其中 *PA* 是阀门入口（端口 **A**）处压力的绝对值。

当 **Pilot configuration** 参数为 `Rigidly connected pilot spool and poppet` 时，先导滑阀传递正先导力和负先导力，模块在 *PCtrl* 的方程中按原样使用 *Ppilot*。当 **Pilot configuration** 参数为 `Disconnected pilot spool and poppet` 时，先导滑阀仅传递正先导压力，*Ppilot* 被限制为正值。模块在 *PCtrl* 的方程中使用 `max(Ppilot,0)`。

### 阀门开度比例

控制压力超过开启压力的程度决定阀门打开多少。阀门开度比例为

P^=PCtrl−PCrkPMax−PCrk，

其中：

- *PCtrl* 是控制压力。
- *PCrk* 是由 **Cracking pressure differential** 参数指定的开启压力。
- *PMax* 是由 **Maximum opening pressure differential** 参数指定的最大开启压力。

该比例经过归一化，使阀门完全关闭时为 `0`，阀门完全打开时为 `1`。如果计算返回超出这些边界范围的值，模块会将该值饱和到两个限值中最近的一个。

**数值平滑**

当 **Smoothing factor** 参数非零时，模块对归一化控制压力 p^ 应用数值平滑。启用平滑有助于在仿真中保持数值稳健性。

有关详细信息，请参阅 Numerical Smoothing。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量湿空气在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量湿空气在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 阻力元件在稳态下的声速流导决定模块参数化。声速流导衡量湿空气在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

模块按阀门开度比例缩放指定的流通能力。当阀门开度比例从 `0` 上升到 `1` 时，流通能力的度量从其指定的最小值缩放到指定的最大值。

### Momentum Balance

模块方程取决于 **Valve parameterization** 参数。
当您将 **Valve parameterization** 设置为 `Cv flow
coefficient` 时，质量流量 m˙ 为

m˙=CvN6Y(pin−pout)ρin，

其中：

- *Cv* 是流量
  系数。
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

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞状态，模块切换到
方程

m˙=23CvN6FγxTpinρin。

当您将 **Valve parameterization** 设置为 `Kv flow
coefficient` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将
*Cv* 替换为
*Kv*。有关当
**Valve parameterization** 参数为 `Kv
flow coefficient` 或 `Cv flow
coefficient` 时的质量流量方程的更多信息，请参阅 [2][3]。

当您将 **Valve parameterization** 设置为 `Sonic
conductance` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

其中：

- *C* 是声速导。
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

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降至临界压力比
*Bcrit* 以下时，孔口变为
阻塞状态，模块切换到方程

m˙=CρrefpinTrefTin。

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动
应用。如果您将此设置用于含有高水平痕量气体的湿空气，或者正在建模空气以外的流体，您可能需要按混合物比重的平方根来缩放声速导。

有关当 **Valve
parameterization** 参数为 `Sonic
conductance` 时的质量流量方程的更多信息，请参阅 [1]。

当您将 **Valve parameterization** 设置为 `Orifice
area` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ]，

其中：

- *Sr* 是孔口或
  阀门面积。
- *S* 是 **Cross-sectional
  area at ports A and B** 参数的值。
- *Cd* 是
  **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数
*Blam* 的值以上时，模块会平滑过渡到方程的线性化形式，

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至(2γ+1)γγ−1 以下时，孔口变为阻塞状态，模块切换到
方程

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2。

有关当 **Valve
parameterization** 参数为 `Orifice
area` 时的质量流量方程的更多信息，请参阅 [4]。

### Mass Balance

模块假设阀门内部流体的体积和质量非常小，并忽略
这些值。因此，不会有任何数量的流体在阀门中积聚。模块
通过阀门守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标
*w* 表示水蒸气，下标
*g* 表示痕量气体，下标 *d*
表示水滴。

### Energy Balance

模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口流动时，不对流体做功，也不由流体做功。能量只能通过
**A** 和 **B** 端口以平流方式流动。根据能量守恒原理，端口
能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口
**A** 或 **B** 进入阀门的能量流率。

### 假设和限制

- 该模块不建模超声速流动。
