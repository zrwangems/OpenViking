---
type: simulink-block
title: 'Check Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Directional Control Valves'
documentation_page: 'checkvalveg'
documentation_source_path: 'ref/checkvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Valve (G)

## 端口

### 守恒端口

### **A** — 阀门入口气体

与流体必须进入阀门的开口相关联的气体守恒端口。

### **B** — 阀门入口气体

与流体必须离开阀门的开口相关联的气体守恒端口。

## 参数

### **Opening pressure specification** — 用作阀门控制信号的压力测量选择 `Pressure difference of port A relative to port B`（默认）| `Gauge pressure at port A`

用作阀门控制信号的压力测量选择。该模块使用此设置来确定阀门应何时开始打开。在默认设置 `Pressure difference of port A relative to port B` 下，阀门的开启压力表示为从入口到出口的压降。在替代设置 `Gauge pressure at port A` 下，它表示为表压。

### **Cracking pressure differential** — 打开阀门所需的压降 `0.01 MPa`（默认）| 正标量

从入口到出口打开阀门所需的最小压降。该值标志着阀门压差范围的起点，在此范围内阀门逐渐打开以允许流量增加。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure difference of port A relative to port B`。

### **Maximum opening pressure differential** — 阀门完全打开时的压降 `0.02 MPa`（默认）| 正标量

从入口到出口阀门完全打开时的压降。该值标志着阀门压差范围的终点，在此范围内阀门逐渐打开以允许流量增加。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure difference of port A relative to port B`。

### **Cracking pressure (gauge)** — 打开阀门所需的入口最小压力 `0.01 MPa`（默认）| 正标量

打开阀门所需的入口（端口 **A**）最小表压。该值标志着阀门压力范围的起点，在此范围内阀门逐渐打开以允许流量增加。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`。

### **Maximum opening pressure (gauge)** — 入口最大压力 `0.02 MPa`（默认）| 正标量

入口端口 **A** 处阀门完全打开时的最大压力。该值标志着阀门压差范围的终点，在此范围内阀门逐渐打开以允许流量增加。如果阀门在您的模型中未按预期完全打开，您可以尝试降低此参数的值。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`。

### **Valve parameterization** — 用于指定孔口流量特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速导决定模块参数化。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### **Maximum Cv flow coefficient** — 对应于最大打开状态的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积最大时 *Cv* 流量系数的值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，此时首次发生阻塞。如果您没有此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对许多阀门来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应于最大打开状态的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积最大时 *Kv* 流量系数的最大值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **Maximum sonic conductance** — 对应于最大打开状态的声速导 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积最大时声速导的值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确地计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导值是在不同参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导值是在不同参考值下获得的时候，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Maximum orifice area** — 对应于最大打开状态的流动面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积最大时孔口开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| [0,1] 范围内的正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

孔口关闭时与打开时的流量之比。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当孔口处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

### **Laminar flow pressure ratio** — 流动在层流和湍流流态之间过渡时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间过渡时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 气体端口处的流动面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。端口尺寸相等。此参数的值应与阻性元件所连接组件的入口面积相匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b: 使用改进的流量计算对气体系统建模

在以前的版本中，气体库中的模块使用转换因子来以声速导的形式实现不同的孔口参数化。您可以使用 **Valve parameterization** 参数来指定参数化。

新的参数化还包括新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数替换了 **Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow** 和 **Restriction area at leakage flow** 参数。

为提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference density** 参数已分别重命名为 **ISO reference temperature** 和 **ISO reference density**。
- **Cv coefficient (USCS) at maximum flow** 和 **Kv coefficient (USCS) at maximum flow** 参数已分别重命名为 **Maximum Cv coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic conductance**。
- **Pressure control specification** 参数已重命名为 **Opening pressure specification**。此参数的选项已重命名为 `Pressure difference of port A relative to port B` 和 `Gauge pressure at port A`。

## 描述

气体网络中的单向阀

Check Valve (G) 模块表示一个具有单向开启机构的孔口，可防止不希望的逆流。开启机构响应压力，当压力梯度从入口端口 **A** 到出口端口 **B** 下降时打开孔口。单向阀保护上游组件免受来自下游点的压力浪涌、温度尖峰和化学污染的影响。

阀门在开启压力处开始打开，并持续打开直到压力调节范围的终点。开启压力是阀门必须克服的初始阻力，由摩擦力或弹簧力引起，以开启阀门。低于此阈值时，阀门关闭，只有泄漏流量可以通过。超过压力调节范围的终点后，阀门完全打开，最大流量值由瞬时压力条件决定。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动阻塞且速度饱和。当背压比达到阀门特有的临界值时发生阻塞。该模块不捕获超声速流动。

### 控制压力和其他压力

阀门响应的压力是控制压力。默认情况下，控制压力是从入口到出口的压降。此设置确保如果流动方向反转，阀门关闭。

您也可以将控制压力指定为入口处的表压。如果您知道入口压力始终高于出口压力，请使用此设置。例如，当入口连接到压力源（如泵）时。

您可以通过将 **Opening pressure specification** 参数设置为 `Pressure difference of port A relative to port B` 或 `Gauge pressure at port A` 来选择控制压力。

**Pressure difference of port A relative to port B**

当 **Opening pressure specification** 参数为 `Pressure difference of port A relative to port B` 时：

- 控制压力为：

  PCtl=PA-PB，

  其中 *PA* 是端口 **A** 处的绝对压力，*PB* 是端口 **B** 处的绝对压力。
- 开启压力 *PCrk* 是 **Cracking pressure differential** 参数的值。
- 阀门完全打开时的最大压力 *PMax* 是 **Maximum opening pressure differential** 参数的值。

**Gauge pressure at port A**

当 **Opening pressure specification** 参数为 `Gauge pressure at port A` 时：

- 控制压力为

  PCtrl=PA−PAtm，

  其中 *PAtm* 是模型 Gas Properties (G) 模块中指定的大气压力。
- 开启压力 *PCrk* 是 **Cracking pressure (gauge)** 参数的值。
- 阀门完全打开时的最大压力 *PMax* 是 **Maximum opening pressure (gauge)** 参数的值。

### 阀门开度分数

控制压力超过开启压力的程度决定阀门打开多少。归一化控制压力为

P^=PCtrl−PCrkPMax−PCrk，

其中：

- *PCtrl* 是控制压力。
- *PCrk* 是开启压力。
- *PMax* 是最大开启压力。

该分数经过归一化，使得阀门完全关闭时为 `0`，阀门完全打开时为 `1`。如果计算返回超出这些边界值，模块会将值饱和到两个限制中最近的一个。

阀门开度分数 *L* 为

L=(1-Lleak)P^+Lleak，

其中 *Lleak* 是 **Leakage flow fraction** 参数的值。

**数值平滑**

当 **Smoothing factor** 参数非零时，模块对归一化控制压力 p^ 应用数值平滑。启用平滑有助于保持仿真的数值鲁棒性。

有关详细信息，请参阅 Numerical Smoothing。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻性元件的声速导决定模块参数化。声速导衡量气体在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

模块按阀门开度比例缩放指定的流通能力。当阀门开度比例从 `0` 上升到 `1` 时，流通能力的度量从其指定的最小值缩放到指定的最大值。

### 动量平衡

模块方程取决于 **Orifice parametrization** 参数。当您将 **Orifice parametrization** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvN6Y(pin−pout)ρin，

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 上升到 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降到 1−FγxT 以下时，孔口变为阻塞，模块切换到方程

m˙=23CvN6FγxTpinρin。

当您将 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，模块使用相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **Orifice parametrization** 参数为 `Kv flow coefficient parameterization` 或 `Cv flow coefficient parameterization` 时的质量流量方程的更多信息，请参阅 [2][3]。

当您将 **Orifice parametrization** 设置为 `Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

其中：

- *C* 是声速导。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 上升到 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降到临界压力比 *Bcrit* 以下时，孔口变为阻塞，模块切换到方程

m˙=CρrefpinTrefTin。

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您将此设置用于空气以外的气体，可能需要按比重的平方根缩放声速导。

有关当 **Orifice parametrization** 参数为 `Sonic conductance parameterization` 时的质量流量方程的更多信息，请参阅 [1]。

当您将 **Orifice parametrization** 设置为 `Orifice area parameterization` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ]，

其中：

- *Sr* 是孔口或阀门面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 上升到 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降到 (2γ+1)γγ−1 以下时，孔口变为阻塞，模块切换到方程

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2。

有关当 **Orifice parametrization** 参数为 `Orifice area parameterization` 时的质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

模块假设阀门内部流体的体积和质量非常小，并忽略这些值。因此，不会有流体在阀门中积聚。根据质量守恒原理，通过一个端口进入阀门质量流量等于通过另一个端口流出阀门质量流量

m˙A+m˙B=0，

其中 m˙ 定义为通过由 **A** 或 **B** 下标指示的端口进入阀门质量流量。

### 能量平衡

模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口流动时，不对流体做功，也不由流体做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀门的能量流率。

### 假设和限制

- `Orifice area` 参数化的方程对于远离理想气体的气体不太准确。
- 此模块不建模超声速流动。
