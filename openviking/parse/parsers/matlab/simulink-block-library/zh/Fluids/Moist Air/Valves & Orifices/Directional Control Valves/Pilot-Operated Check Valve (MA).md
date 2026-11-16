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

### 守恒

### **A** — 阀门入口或出口湿空气

与在正常操作且先导机构禁用时流动进入阀门的开口相关联的湿空气守恒端口。仅当先导端口被加压到足够程度时，此端口才可用作出口。

### **B** — 阀门入口或出口湿空气

与在正常操作且先导机构禁用时流动离开阀门的开口相关联的湿空气守恒端口。

### **X** — 先导端口湿空气

湿空气守恒端口，其通过施加足够压力来致动先导机构，从而打开阀门以允许反向流动。此端口没有质量流量。

## 参数

### **阀门参数化** — 用于指定节流孔流动特性的参数化 `Cv flow coefficient`（默认） | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻力元件的声速流导决定模块参数化。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### **先导配置** — 处理负先导压力作用力的方法 `Rigidly connected pilot spool and poppet`（默认） | `Disconnected pilot spool and poppet`

当先导压力为负时模块使用的方法：

- `Rigidly connected pilot spool and poppet` — 先导阀芯同时传递正先导压力作用力和负先导压力作用力，因此模块按原样使用 *ppilot*。
- `Disconnected pilot spool and poppet` — 先导阀芯仅传递正先导压力作用力，因此模块将 *ppilot* 限制为正值。模块将负值替换为零。

### **先导压力指定** — 用作阀门控制信号的压力测量选择 `Pressure difference of port X relative to port A`（默认） | `Gauge pressure at port X`

用作阀门控制信号的压力测量选择。模块使用此设置确定阀门应何时开始打开。在默认设置 `Pressure difference of port X relative to port A` 下，阀门的开启压力表示为从先导端口 **X** 到入口 **A** 的压降。在替代设置 `Gauge pressure at port X` 下，它表示为相对于环境压力测量的入口表压。

### **开启压力差** — 阀门首次打开时的有效控制压力 `0.01 MPa`（默认） | 正标量

阀门开始打开时的有效压力差。此差值是入口到出口的压降与先导压力和先导比的乘积之和。所使用的先导压力取决于 **先导压力指定** 参数的设置。

### **最大开度压力差** — 阀门完全打开时的有效控制压力 `0.02 MPa`（默认） | 正标量

阀门完全打开时的有效压力差。此差值是入口到出口的压降与先导压力和先导比的乘积之和。所使用的先导压力取决于 **先导压力指定** 参数的设置。

### **先导比** — 先导端口面积与入口端口面积之比 `1`（默认） | 正标量

先导端口面积与入口端口面积之比。

### **最大 Cv 流量系数** — 对应于组件最大开度的 Cv 系数 `4`（默认） | 正标量

可供流动的节流面积最大时的 *Cv* 流量系数值。当由压力差驱动时，此参数度量湿空气通过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Cv flow coefficient`。

### **阻塞流下的 xT 压差比因子** — 压差比 `0.7`（默认） | 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为首次发生阻塞时的 (pin−pout)/pin。如果没有此值，请在 ISA-75.01.01 [3] 的表 2 中查找。否则，默认值 0.7 对许多阀门都是合理的。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **最大 Kv 流量系数** — 对应于组件最大开度的 Kv 系数 `3.6`（默认） | 正标量

可供流动的节流面积最大时的 *Kv* 流量系数最大值。当由压力差驱动时，此参数度量湿空气通过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Kv flow coefficient`。

### **最大声速流导** — 对应于组件最大开度的声速流导 `12 l/(bar*s)`（默认） | 正标量

可供流动的横截面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **临界压力比** — 流动首次阻塞时的下游压力与上游压力之比 `0.3`（默认） | 正标量

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认） | 正标量

用于更准确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认） | 标量

标准参考大气下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用在不同于参考值下获得的声速流导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | 正标量

标准参考大气下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用在不同于参考值下获得的声速流导值时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **最大节流孔面积** — 对应于组件最大开度的流动面积 `1e-4 m^2`（默认） | 正标量

可供流动的横截面积最大时，节流孔开口的横截面积。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Orifice area`。

### **流出系数** — 流出系数 `0.64`（默认） | 范围 [0,1] 内的正标量

用于考虑理论流动中流出损失的修正因子。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Orifice area`。

### **泄漏流量分数** — 流量比 `1e-6`（默认） | 正标量

节流孔关闭时的流量与打开时的流量之比。

### **平滑因子** — 数值平滑因子 `0.01`（默认） | 范围 [0,1] 内的正标量

连续平滑因子，当节流孔处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

### **层流压力比** — 流动在层流和湍流流态之间转换时的压力比 `0.999`（默认） | 正标量

流动在层流和湍流流态之间转换时的压力比。压力比是出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **端口 A 和 B 处的横截面积** — 湿空气端口处的流动面积 `0.01 m^2`（默认） | 正标量

每个端口处垂直于流动路径的面积。这些端口尺寸相同。此参数值应与阻力元件所连接组件的入口面积匹配。

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

Pilot-Operated Check Valve (MA) 模块表示湿空气域中带超越机构的单向阀，该超越机构允许反向流动。单向阀是一种带有单向开启机构的节流孔，可防止反向流动。

模块的 **X** 端口表示先导端口，用作超越机构。正常操作期间，先导端口不活动，阀门表现为单向阀。在单向阀中，节流孔仅在阀门两端的压力梯度从入口到出口下降时打开。节流孔开启可防止反向流动，而反向流动需要反向压力梯度，并保护阀门上游组件免受下游压力浪涌、温度尖峰和化学污染的影响。

当端口 **X** 处有足够的值时，模块对先导端口加压，并迫使阀门的控制元件离开阀座，从而允许反向流动。此时阀门双向对流动打开，由出口到入口的反向压降驱动流动向上游流动。位于流动路径中的阀座决定阀门是否打开。当阀座被覆盖时，流动被切断，阀门关闭。

阀门在开启压力下开始打开，并持续打开直到压力调节范围结束。开启压力是阀门必须克服才能开启的初始阻力，由摩擦或弹簧力引起。低于此阈值时，阀门关闭，只有泄漏流量可以通过。超过压力调节范围末端后，阀门完全打开，最大值的流量由瞬时压力条件决定。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能提高速度时，流动阻塞且速度饱和。当背压比达到阀门特有的临界值时发生阻塞。模块不捕获超声速流动。

### 控制压力和其他压力

阀门的打开取决于先导压力和从入口到出口的压降。打开阀门的压力为

PCtrl=kpilotPpilot+PA-PB，

其中：

- *Ppilot* 是先导压力。
- *kpilot* 是先导比。
- *PA* 是端口 **A** 处的表压。
- *PB* 是端口 **B** 处的表压。

仿真期间，模块相对于绝对零压确定端口压力。

先导压力可以相对于入口端口 **A**，也可以相对于环境。您可以通过将 **先导压力指定** 参数设置为 `Pressure difference of port X relative to port B` 或 `Gauge pressure at port X` 来选择先导压力。

如果选择 `Gauge pressure at port X`，则先导压力为

Ppilot=PX−Patm，

其中 *PAtm* 是大气压力，*PX* 是先导端口处压力的绝对值。如果选择 `Pressure difference of port X relative to port A`，则先导压力为

Ppilot=PX−PA，

其中 *PA* 是阀门入口端口 **A** 处压力的绝对值。

当 **先导配置** 参数为 `Rigidly connected pilot spool and poppet` 时，先导阀芯同时传递正先导作用力和负先导作用力，模块在 *PCtrl* 的方程中按原样使用 *Ppilot*。当 **先导配置** 参数为 `Disconnected pilot spool and poppet` 时，先导阀芯仅传递正先导压力作用力，*Ppilot* 被限制为正值。模块在 *PCtrl* 的方程中使用 `max(Ppilot,0)`。

### 阀门开度比例

控制压力超过开启压力的程度决定阀门打开多少。阀门开度比例为

P^=PCtrl−PCrkPMax−PCrk，

其中：

- *PCtrl* 是控制压力。
- *PCrk* 是由 **开启压力差** 参数指定的开启压力。
- *PMax* 是由 **最大开度压力差** 参数指定的最大打开压力。

该比例经过归一化，使阀门完全关闭时为 `0`，阀门完全打开时为 `1`。如果计算返回超出这些界限的值，模块会将值限幅到两个限值中最近的一个。

**数值平滑**

当 **平滑因子** 参数非零时，模块对归一化控制压力 p^ 应用数值平滑。启用平滑有助于在仿真中保持数值稳健性。

有关详细信息，请参阅数值平滑。

### 阀门参数化

模块行为取决于 **阀门参数化** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数度量当由某一压力差驱动时湿空气流动的容易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数度量当由某一压力差驱动时湿空气流动的容易程度。
- `Sonic conductance` — 稳态下阻力元件的声速流导决定模块参数化。声速流导度量当流动 *阻塞*（即流速处于当地声速的状态）时湿空气流动的容易程度。当下游压力与上游压力之比达到称为 *临界压力比* 的临界值时，发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

模块按阀门开度比例缩放指定的流动能力。当阀门开度比例从 `0` 升至 `1` 时，流动能力的度量从其指定的最小值缩放到指定的最大值。

### 动量平衡

模块方程取决于 **Valve parameterization** 参数。

当您将 **Valve parameterization** 设置为 `Cv flow coefficient` 时，质量流量 m˙ 为

m˙=CvN6Y(pin−pout)ρin,

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，孔口发生阻塞流，模块切换到以下方程

m˙=23CvN6FγxTpinρin.

当您将 **Valve parameterization** 设置为 `Kv flow coefficient` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **Valve parameterization** 参数为 `Kv flow coefficient` 或 `Cv flow coefficient` 时的质量流量方程的更多信息，请参见 [2][3]。

当您将 **Valve parameterization** 设置为 `Sonic conductance` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是声速流导。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口发生阻塞流，模块切换到以下方程

m˙=CρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置用于气动应用。如果将此设置用于含有高水平痕量气体的湿空气，或正在建模除空气以外的流体，则可能需要按混合气体比重的平方根缩放声速流导。

有关当 **Valve parameterization** 参数为 `Sonic conductance` 时的质量流量方程的更多信息，请参见 [1]。

当您将 **Valve parameterization** 设置为 `Orifice area` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ],

其中：

- *Sr* 是孔口或阀门面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口发生阻塞流，模块切换到以下方程

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2.

有关当 **Valve parameterization** 参数为 `Orifice area` 时的质量流量方程的更多信息，请参见 [4]。

### 质量平衡

模块假定阀门内部流体的体积和质量非常小，并忽略这些值。因此，流体不能在阀门中积聚。模块保持通过阀门的质量守恒

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标 *g* 表示痕量气体，下标 *d* 表示水滴。

### 能量平衡

模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口流到出口时，既没有对流体做功，也没有由流体做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，各端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀门的能量流率。

### 假设与限制

- 此模块不对超声速流动进行建模。
