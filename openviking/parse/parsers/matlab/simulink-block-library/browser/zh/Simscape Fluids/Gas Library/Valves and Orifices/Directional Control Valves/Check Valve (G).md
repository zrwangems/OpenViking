---
type: simulink-block
title: 'Check Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Gas Library / Valves and Orifices / Directional Control Valves'
documentation_page: 'checkvalveg'
documentation_source_path: 'ref/checkvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Valve (G)

## 端口

### 守恒

### **A** — 阀门入口气体

与流体必须进入阀门的开口关联的气体守恒端口。

### **B** — 阀门出口气体

与流体必须离开阀门的开口关联的气体守恒端口。

## 参数

### **开启压力设定** — 用作阀门控制信号的压力测量选择 `Pressure difference of port A relative to port B`（默认） | `Gauge pressure at port A`

用作阀门控制信号的压力测量选择。模块使用此设置来确定阀门应何时开始打开。在默认设置 `Pressure difference of port A relative to port B` 中，阀门的开启压力表示为从入口到出口的压降。在替代设置 `Gauge pressure at port A` 中，它表示为表压。

### **开启压差** — 打开阀门所需的压降 `0.01 MPa`（默认） | 正标量

从入口到出口打开阀门所需的最小压降。该值标记阀门压差范围的起点，在该范围内阀门逐渐开启以允许流量增加。

#### 依赖关系

要启用此参数，请将 **开启压力设定** 设置为 `Pressure difference of port A relative to port B`。

### **最大开启压差** — 阀门完全打开时的压降 `0.02 MPa`（默认） | 正标量

阀门完全打开时从入口到出口的压降。该值标记阀门压差范围的终点，在该范围内阀门逐渐开启以允许流量增加。

#### 依赖关系

要启用此参数，请将 **开启压力设定** 设置为 `Pressure difference of port A relative to port B`。

### **开启压力（表压）** — 打开阀门所需的入口最小压力 `0.01 MPa`（默认） | 正标量

打开阀门所需的入口（端口 **A**）最小表压。该值标记阀门压力范围的起点，在该范围内阀门逐渐开启以允许流量增加。

#### 依赖关系

要启用此参数，请将 **开启压力设定** 设置为 `Gauge pressure at port A`。

### **最大开启压力（表压）** — 入口最大压力 `0.02 MPa`（默认） | 正标量

入口端口 **A** 处的最大压力，在该压力下阀门完全打开。该值标记阀门压差范围的终点，在该范围内阀门逐渐开启以允许流量增加。如果模型中的阀门未按预期完全打开，可以尝试降低此参数的值。

#### 依赖关系

要启用此参数，请将 **开启压力设定** 设置为 `Gauge pressure at port A`。

### **阀门参数化** — 用于指定节流孔流量特性的参数化 `Cv flow coefficient`（默认） | `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v（其中 Kv=0.865Cv）决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速流导决定模块参数化。
- `Orifice area` — 流量限制的尺寸决定模块参数化。

### **最大 Cv 流量系数** — 组件最大开启时对应的 Cv 系数 `4`（默认） | 正标量

当可供流动的限制面积最大时 *Cv* 流量系数的值。该参数衡量气体在压差驱动下穿过阻性元件的容易程度。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Cv flow coefficient`。

### **阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认） | 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为首次发生阻塞处的 (pin−pout)/pin。如果不知道此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对许多阀门来说是合理的。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **最大 Kv 流量系数** — 组件最大开启时对应的 Kv 系数 `3.6`（默认） | 正标量

当可供流动的限制面积最大时 *Kv* 流量系数的最大值。该参数衡量气体在压差驱动下穿过阻性元件的容易程度。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Kv flow coefficient`。

### **最大声速流导** — 组件最大开启时对应的声速流导 `12 l/(bar*s)`（默认） | 正标量

当可供流动的横截面积最大时声速流导的值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **临界压力比** — 流量首次阻塞时的下游与上游压力之比 `0.3`（默认） | 正标量

流量首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认） | 正标量

用于更准确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认） | 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **最大节流孔面积** — 组件最大开启时对应的流通面积 `1e-4 m^2`（默认） | 正标量

当可供流动的横截面积最大时，节流孔开口的横截面积。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Orifice area`。

### **流出系数** — 流出系数 `0.64`（默认） | [0,1] 范围内的正标量

用于说明理论流动中流出损失的修正系数。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Orifice area`。

### **泄漏流量分数** — 流量比 `1e-6`（默认） | 正标量

节流孔关闭时的流量与打开时的流量之比。

### **平滑因子** — 数值平滑因子 `0.01`（默认） | [0,1] 范围内的正标量

连续平滑因子，当节流孔处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

### **层流压力比** — 流动在层流和湍流流态之间转换时的压力比 `0.999`（默认） | 正标量

流动在层流和湍流流态之间转换时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **端口 A 和 B 处的横截面积** — 气体端口处的流通面积 `0.01 m^2`（默认） | 正标量

每个端口处垂直于流路的面积。各端口尺寸相同。此参数的值应与阻性元件所连接组件的入口面积匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b：使用改进的流量计算对气体系统建模

在以前的版本中，气体库中的模块使用转换因子以声速流导的形式实现不同的节流孔参数化。可以使用 **阀门参数化** 参数来指定参数化。

新的参数化还包括新参数：

- **阻塞流时的 xT 压差比系数**
- **流出系数**
- **泄漏流量分数**。此参数取代 **泄漏流量下的 Cv 系数 (USCS)**、**泄漏流量下的 Kv 系数 (SI)**、**泄漏流量下的声速流导** 和 **泄漏流量下的限制面积** 参数。

为提高清晰度：

- **开启参数化** 参数已重命名为 **开启特性**。
- **参考温度** 和 **参考密度** 参数已分别重命名为 **ISO 参考温度** 和 **ISO 参考密度**。
- **最大流量下的 Cv 系数 (USCS)** 和 **最大流量下的 Kv 系数 (USCS)** 参数已分别重命名为 **最大 Cv 系数** 和 **最大 Kv 系数**。
- **最大流量下的声速流导** 参数已重命名为 **最大声速流导**。
- **压力控制设定** 参数已重命名为 **开启压力设定**。此参数的选项已重命名为 `Pressure difference of port A relative to port B` 和 `Gauge pressure at port A`。

## 描述

气体网络中的单向阀

Check Valve (G) 模块表示一个具有单向开启机构的节流孔，可防止不希望的逆流。开启机构对压力作出响应，当压力梯度从端口 **A** 的入口向端口 **B** 的出口下降时打开节流孔。单向阀保护上游组件免受来自下游点的压力浪涌、温度尖峰和化学污染。

阀门在开启压力处开始打开，并持续打开直到压力调节范围的终点。开启压力是阀门为开启而必须克服的初始阻力，由摩擦力或弹簧力引起。低于此阈值时，阀门关闭，只有泄漏流量可以通过。超过压力调节范围的终点后，阀门完全打开，最大流量值由瞬时压力条件决定。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度饱和。当背压比达到阀门特有的临界值时发生阻塞。该模块不捕获超声速流动。

### 控制压力和其他压力

阀门响应的压力是控制压力。默认情况下，控制压力是从入口到出口的压降。此设置确保如果流动方向反转，阀门关闭。

也可以将控制压力指定为入口处的表压。如果已知入口压力始终高于出口压力，请使用此设置。例如，当入口连接到压力源（如泵）时。

可以通过将 **开启压力设定** 参数设置为 `Pressure difference of port A relative to port B` 或 `Gauge pressure at port A` 来选择控制压力。

**Pressure difference of port A relative to port B**

当 **开启压力设定** 参数为 `Pressure difference of port A relative to port B` 时：

- 控制压力为：

  PCtl=PA-PB，

  其中 *PA* 是端口 **A** 处的绝对压力，*PB* 是端口 **B** 处的绝对压力。
- 开启压力 *PCrk* 是 **开启压差** 参数的值。
- 阀门完全打开时的最大压力 *PMax* 是 **最大开启压差** 参数的值。

**Gauge pressure at port A**

当 **开启压力设定** 参数为 `Gauge pressure at port A` 时：

- 控制压力为

  PCtrl=PA−PAtm，

  其中 *PAtm* 是模型中 Gas Properties (G) 模块指定的大气压力。
- 开启压力 *PCrk* 是 **开启压力（表压）** 参数的值。
- 阀门完全打开时的最大压力 *PMax* 是 **最大开启压力（表压）** 参数的值。

### 阀门开启比例

控制压力超过开启压力的程度决定阀门打开多少。归一化控制压力为

P^=PCtrl−PCrkPMax−PCrk，

其中：

- *PCtrl* 是控制压力。
- *PCrk* 是开启压力。
- *PMax* 是最大开启压力。

该分数经过归一化，使得在阀门完全关闭时为 `0`，在阀门完全打开时为 `1`。如果计算结果超出这些边界，模块会将该值饱和到两个极限中最近的一个。

阀门开启比例 *L* 为

L=(1-Lleak)P^+Lleak，

其中 *Lleak* 是 **泄漏流量分数** 参数的值。

**数值平滑**

当 **平滑因子** 参数非零时，模块会对归一化控制压力 p^ 应用数值平滑。启用平滑有助于保持仿真的数值稳健性。

有关详细信息，请参阅数值平滑。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的容易程度。
- `Kv flow coefficient` — 流量系数 *K*v（其中 Kv=0.865Cv）决定模块参数化。流量系数衡量气体在特定压差驱动下流动的容易程度。
- `Sonic conductance` — 阻力元件在稳态下的声速流导决定模块参数化。声速流导衡量气体在 *阻塞* 时流动的容易程度，*阻塞* 是一种流速达到当地声速的状态。当下游压力与上游压力之比达到称为 *临界压力比* 的临界值时，就会发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

模块按阀门开度分数缩放指定的流量能力。当阀门开度分数从 `0` 上升到 `1` 时，流量能力的度量从指定的最小值缩放到指定的最大值。

### 动量平衡

模块方程取决于 **Orifice parametrization** 参数。当将 **Orifice parametrization** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvN6Y(pin−pout)ρin,

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量以 kg/hr 为单位、压力以 bar 为单位、密度以 kg/m3 为单位时，其值为 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式：

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，孔口发生阻塞，模块切换到以下方程：

m˙=23CvN6FγxTpinρin.

当将 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关 **Orifice parametrization** 参数为 `Kv flow coefficient parameterization` 或 `Cv flow coefficient parameterization` 时的质量流量方程的更多信息，请参阅 [2][3]。

当将 **Orifice parametrization** 设置为 `Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是声速流导。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式：

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口发生阻塞，模块切换到以下方程：

m˙=CρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置用于气动应用。如果对空气以外的气体使用此设置，可能需要按比重的平方根缩放声速流导。

有关 **Orifice parametrization** 参数为 `Sonic conductance parameterization` 时的质量流量方程的更多信息，请参阅 [1]。

当将 **Orifice parametrization** 设置为 `Orifice area parameterization` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ],

其中：

- *Sr* 是孔口或阀门面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式：

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口发生阻塞，模块切换到以下方程：

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2.

有关 **Orifice parametrization** 参数为 `Orifice area parameterization` 时的质量流量方程的更多信息，请参阅 [4]。

### 质量平衡

模块假定阀门内流体的体积和质量非常小，并忽略这些值。因此，流体无法在阀门中积聚。根据质量守恒原理，通过一个端口流入阀门的质量流量等于通过另一个端口流出阀门的质量流量

m˙A+m˙B=0,

其中 m˙ 定义为通过 **A** 或 **B** 下标所指示的端口流入阀门的质量流量。

### 能量平衡

模块的阻力元件是绝热元件。流体与其周围壁面之间不会发生热交换。流体从入口到出口的过程中，不对流体做功，流体也不做功。能量只能通过对流，经由端口 **A** 和 **B** 流动。根据能量守恒原理，各端口能量流之和始终为零

ϕA+ϕB=0,

其中 *ϕ* 是通过端口 **A** 或 **B** 流入阀门的能量流率。

### 假设和限制

- 对于远离理想气体的气体，`Orifice area` 参数化的方程准确性较低。
- 此模块不对超声速流动建模。
