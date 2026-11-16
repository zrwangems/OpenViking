---
type: simulink-block
title: 'Pilot-Operated Check Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Gas Library / Valves and Orifices / Directional Control Valves'
documentation_page: 'pilotoperatedcheckvalveg'
documentation_source_path: 'ref/pilotoperatedcheckvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Pilot-Operated Check Valve (G)

## 端口

### 守恒

### **A** — 阀门入口气体

与在先导机构禁用时，正常运行期间流量必须通过其进入阀门的开口关联的气体守恒端口。只有当先导端口被加压到足够程度时，该端口才能用作出口。

### **B** — 阀门入口气体

与在先导机构禁用时，正常运行期间流量必须通过其离开阀门的开口关联的气体守恒端口。

### **X** — 先导端口气体

与这样一个开口关联的气体守恒端口：通过施加足够压力，可致动先导机构，从而打开阀门以实现反向流动。

## 参数

### **Pilot configuration** — 处理负先导压力作用力的方法 `Rigidly connected pilot spool and poppet` (default) | `Disconnected pilot spool and poppet`

当先导压力为负时模块使用的方法：

- `Rigidly connected pilot spool and poppet` — 先导滑阀传递正和负先导压力作用力，因此模块按原样使用 *ppilot*。
- `Disconnected pilot spool and poppet` — 先导滑阀仅传递正先导压力作用力，因此模块将 *ppilot* 限制为仅正值。模块将负值替换为零。

### **Pilot pressure specification** — 选择用作阀门控制信号的压力测量方式 `Pressure difference of port X relative to port A` (default) | `Gauge pressure at port X`

选择用作阀门控制信号的压力测量方式。模块使用此设置来确定阀门应何时开始打开。在默认设置 `Pressure difference of port X relative to port A` 下，阀门的开启压力表示为从先导端口 **X** 到入口 **A** 的压降。在替代设置 `Gauge pressure at port X` 下，它表示为相对于环境压力测量的入口表压。

### **Cracking pressure differential** — 阀门首次打开时的有效控制压力 `0.01 MPa` (default) | positive scalar

阀门开始打开时的有效压力差。此差值为从入口到出口的压降与先导压力和先导比乘积之和。所使用的先导压力取决于 **Pilot pressure specification** 参数的设置。

### **Maximum opening pressure differential** — 阀门完全打开时的有效控制压力 `0.02 MPa` (default) | positive scalar

阀门完全打开时的有效压力差。此差值为从入口到出口的压降与先导压力和先导比乘积之和。所使用的先导压力取决于 **Pilot pressure specification** 参数的设置。

### **Pilot ratio** — 先导端口面积与入口端口面积的比值 `1` (default) | positive scalar

先导端口面积与入口端口面积的比值。

### **Valve parameterization** — 用于指定节流孔流量特性的参数化 `Cv flow coefficient` (default) | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻力元件的声速流导决定模块参数化。
- `Orifice area` — 节流限制的尺寸决定模块参数化。

### **Maximum Cv flow coefficient** — 对应组件最大开启的 Cv 系数 `4` (default) | positive scalar

当可用于流动的限制面积最大时 *Cv* 流量系数的值。此参数衡量当由压差驱动时气体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 阻塞流下的压差比因子 `0.7` (default) | positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，此时首次发生阻塞。如果您没有此值，请在 ISA-75.01.01 [3] 的表 2 中查找。否则，对于许多阀门而言，默认值 0.7 是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应组件最大开启的 Kv 系数 `3.6` (default) | positive scalar

当可用于流动的限制面积最大时 *Kv* 流量系数的最大值。此参数衡量当由压差驱动时气体穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **Maximum sonic conductance** — 对应组件最大开启的声速流导 `12 l/(bar*s)` (default) | positive scalar

当可用于流动的横截面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3` (default) | positive scalar

流动首次开始阻塞且流速达到其最大值（由局部声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Subsonic index** — 用于表征亚声速流区质量流量的指数 `0.5` (default) | positive scalar

用于更准确计算亚声速流区质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K` (default) | scalar

标准参考大气中的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3` (default) | positive scalar

标准参考大气中的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Maximum orifice area** — 对应组件最大开启的流通面积 `1e-4 m^2` (default) | positive scalar

当可用于流动的横截面积最大时的节流孔开口横截面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Discharge coefficient** — 流量系数 `0.64` (default) | positive scalar in the range of [0,1]

用于计及理论流动中排出损失的修正系数。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Leakage flow fraction** — 流量比 `1e-6` (default) | positive scalar

节流孔关闭时与打开时的流量之比。

### **Smoothing factor** — 数值平滑因子 `0.01` (default) | positive scalar in the range [0,1]

当节流孔处于接近打开或接近关闭位置时，向流量响应引入渐变层的连续平滑因子。将此参数设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间转换的压力比 `0.999` (default) | positive scalar

流动在层流和湍流状态之间转换的压力比。压力比是出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 气体端口处的流通面积 `0.01 m^2` (default) | positive scalar

每个端口处垂直于流动路径的面积。端口尺寸相同。此参数的值应与阻力元件所连接组件的入口面积匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Directional Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b: 使用改进的流量计算对气体系统建模

在以前的版本中，气体库中的模块使用转换因子来按声速流导实现不同的节流孔参数化。您可以使用 **Valve parameterization** 参数来指定参数化。

新的参数化还包括新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数取代 **Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow** 和 **Restriction area at leakage flow** 参数。
- **Pilot configuration**

为提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference density** 参数已分别重命名为 **ISO reference temperature** 和 **ISO reference density**。
- **Cv coefficient (USCS) at maximum flow** 和 **Kv coefficient (USCS) at maximum flow** 参数已分别重命名为 **Maximum Cv coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic conductance**。
- **Pressure control specification** 参数已重命名为 **Pilot pressure specification**。此参数的选项已重命名为 `Pressure difference of port X relative to port A` 和 `Gauge pressure at port X`。

## 描述

气体网络中带控制端口的单向阀

Pilot-Operated Check Valve (G) 模块表示一种带超驰机构的单向阀，该机构在被激活时允许反向流动。单向阀是一种具有单向开启机构的节流孔，可防止反向流动。

模块的 **X** 端口表示用作超驰机构的先导端口。在正常运行期间，先导端口不活动，阀门表现为单向阀。在单向阀中，只有当阀门两端的压力梯度从入口到出口下降时，节流孔才会打开。节流孔开口可防止需要反向压力梯度的反向流动，并保护阀门上游组件免受下游压力浪涌、温度尖峰和化学污染的影响。

当 **X** 端口处有足够的值时，模块对先导端口加压，并迫使阀门的控制元件离开其阀座，从而允许反向流动。此时阀门在两个方向上均对流动打开，从出口到入口的反向压降驱动流量向上游流动。位于流动路径中的阀座决定阀门是否打开。当阀座被覆盖时，流动被切断，阀门关闭。

阀门在开启压力处开始打开，并持续打开直到压力调节范围末端。开启压力是阀门必须克服以开始打开的初始阻力，该阻力由摩擦力或弹簧力引起。低于此阈值时，阀门关闭，只有泄漏流量可以通过。超过压力调节范围末端后，阀门完全打开，最大流量值由瞬时压力条件决定。

流动可以是层流或湍流，并且可以达到声速。最大速度出现在阀门喉部，此处流动最窄且最快。当下游压力下降不再能提高速度时，流动阻塞，速度饱和。当背压比达到阀门的临界特征值时，发生阻塞。该模块不捕获超声速流动。

### 控制压力和其他压力

阀门的开启取决于先导压力和从入口到出口的压降。打开阀门的压力为

PCtrl=kpilotPpilot+PA-PB,

其中：

- *Ppilot* 是先导压力。
- *kpilot* 是先导比。
- *PA* 是端口 **A** 处的表压。
- *PB* 是端口 **B** 处的表压。

模块在仿真期间相对于绝对零压确定端口压力。

先导压力可以相对于入口端口 **A**，也可以相对于环境。您可以通过将 **Pilot pressure specification** 参数设置为 `Pressure difference of port X relative to port B` 或 `Gauge pressure at port X` 来选择先导压力。

如果选择 `Gauge pressure at port X`，则先导压力为

Ppilot=PX−Patm,

其中 *PAtm* 是模型 Gas Properties (G) 模块中指定的大气压力，*PX* 是先导端口处压力的绝对值。如果选择 `Pressure difference of port X relative to port A`，则先导压力为

Ppilot=PX−PA,

其中 *PA* 是阀门入口端口 **A** 处压力的绝对值。

当 **Pilot configuration** 参数为 `Rigidly connected pilot spool and poppet` 时，先导滑阀传递正和负先导力，模块在 *PCtrl* 方程中按原样使用 *Ppilot*。当 **Pilot configuration** 参数为 `Disconnected pilot spool and poppet` 时，先导滑阀仅传递正先导压力作用力，*Ppilot* 被限制为正值。模块在 *PCtrl* 方程中使用 `max(Ppilot,0)`。

### 阀门开启比例

控制压力超过开启压力的程度决定阀门打开的程度。阀门开启比例为

P^=PCtrl−PCrkPMax−PCrk,

其中：

- *PCtrl* 是控制压力。
- *PCrk* 是由 **Cracking pressure differential** 参数指定的开启压力。
- *PMax* 是由 **Maximum opening pressure differential** 参数指定的最大开启压力。

该比例经过归一化，使阀门完全关闭时为 `0`，阀门完全打开时为 `1`。如果计算返回的值超出这些边界，模块会将该值饱和到两个限值中最近的一个。

**数值平滑**

当 **Smoothing factor** 参数非零时，模块对归一化控制压力 p^ 应用数值平滑。启用平滑有助于在仿真中保持数值稳健性。

有关详细信息，请参阅数值平滑。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声导决定模块参数化。声导衡量气体在 *choked* 时流动的难易程度，*choked* 是一种流动速度达到当地声速的状态。当下游与上游压力之比达到称为 *critical pressure ratio* 的临界值时，发生阻塞。
- `Orifice area` — 节流口尺寸决定模块参数化。

模块按阀门开度分数缩放指定的流动能力。当阀门开度分数从 `0` 升至 `1` 时，流动能力的度量从其指定的最小值缩放至指定的最大值。

### 动量平衡

模块方程取决于 **Orifice parametrization** 参数。当将 **Orifice parametrization** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvN6Y(pin−pout)ρin,

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 之比。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口发生阻塞，模块切换到方程

m˙=23CvN6FγxTpinρin.

当将 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，模块使用这些相同的方程，但通过关系 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关 **Orifice parametrization** 参数为 `Kv flow coefficient parameterization` 或 `Cv flow coefficient parameterization` 时的质量流量方程的详细信息，请参阅 [2][3]。

当将 **Orifice parametrization** 设置为 `Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是声导。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口发生阻塞，模块切换到方程

m˙=CρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果将此设置用于空气以外的气体，您可能需要用比重的平方根缩放声导。

有关 **Orifice parametrization** 参数为 `Sonic conductance parameterization` 时的质量流量方程的详细信息，请参阅 [1]。

当将 **Orifice parametrization** 设置为 `Orifice area parameterization` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ],

其中：

- *Sr* 是孔口或阀门面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至(2γ+1)γγ−1 以下时，孔口发生阻塞，模块切换到方程

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2.

有关 **Orifice parametrization** 参数为 `Orifice area parameterization` 时的质量流量方程的详细信息，请参阅 [4]。

### 质量平衡

模块假设阀门内流体的体积和质量非常小，并忽略这些值。因此，任何数量的流体都不能积聚在阀门中。根据质量守恒原理，通过一个端口进入阀门质量流量等于通过另一个端口流出阀门质量流量

m˙A+m˙B=0,

其中 m˙ 定义为通过由 **A** 或 **B** 下标指示的端口进入阀门质量流量。

### 能量平衡

模块的阻力元件是绝热组件。流体与其周围壁面之间不能发生热交换。流体从入口到出口的过程中，没有对流体做功或由流体做功。能量只能通过对流，经由端口 **A** 和 **B** 流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀门的能量流率。

### 假设与限制

- `Orifice area` 参数化的方程对于远离理想气体的气体精度较低。
- 此模块不建模超声速流动。
