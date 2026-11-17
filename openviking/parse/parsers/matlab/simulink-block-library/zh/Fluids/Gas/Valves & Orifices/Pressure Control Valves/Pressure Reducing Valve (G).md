---
type: simulink-block
title: 'Pressure Reducing Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereducingvalveg'
documentation_source_path: 'ref/pressurereducingvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Reducing Valve (G)

## 端口

### 守恒端口

### **A** — 阀入口气体

与气流必须进入阀门的开口关联的气体守恒端口。

### **B** — 阀入口气体

与气流必须离开阀门的开口关联的气体守恒端口。

## 参数

### **Valve parameterization** — 用于指定节流孔流量特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化方法。
- `Kv flow coefficient` — 流量系数
  *K*v，
  其中 Kv=0.865Cv，决定模块参数化方法。
- `Sonic conductance` — 稳态下阻性元件的声速导纳决定模块参数化方法。
- `Orifice area` — 流动限制的尺寸决定模块参数化方法。

### **Opening characteristic** — 计算阀门开度特性的方法 `Linear`（默认）| `Tabulated`

模块用于计算阀门开口面积的方法。线性设置将开口面积视为节流孔开度分数的线性函数。表格设置允许以表格形式指定一般的非线性关系。

### **Set pressure (gauge)** — 关闭阀门所需的出口表压 `0.1 MPa`（默认）| 标量

关闭阀门所需的出口表压。此参数标记压力调节范围的起点，在该范围内阀门逐渐关闭以抑制压力上升。阀门的开口面积取决于实际出口压力与此处指定值之间的差值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear`。

### **Pressure regulation range** — 开口面积可变的压力范围宽度 `0.1 MPa`（默认）| 标量

阀门开口面积可变的压力范围宽度。该压力范围从 **Set pressure (gauge)** 参数的值开始，到该参数值与 **Set pressure (gauge)** 参数值之和结束。压力调节范围越小，单位压力上升对阀门开口面积的影响越大。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear`。

### **Pressure at port B (gauge) vector** — 用于指定阀门开度数据的控制压力向量 `0.2 : 0.2 : 1.2 MPa`（默认）| 以压力单位表示的向量

用于指定所选阀门开度度量（声速导纳、流量系数或开口面积）的控制压力向量。此向量的大小必须与包含阀门开度数据的向量相同。向量元素必须为正值，且从左到右单调递增。

第一个向量元素给出阀门开始关闭时的压力设定值。该元素等效于 `Linear` 开度参数化方法的 **Set pressure (gauge)** 参数。最后一个元素给出最大压力，此时阀门最大程度关闭，仅剩泄漏流量。两者之差给出阀门的压力调节范围。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应最大开启组件的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积达到最大时的 *Cv* 流量系数值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

首次发生阻塞时入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。如果您没有此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对许多阀门来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时与开启时的流量之比。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当节流孔处于接近开启或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 对应开度分数向量中各值的 Cv 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 正数向量

*Cv* 流量系数向量。每个系数对应 **Opening fraction vector** 参数中的一个值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。流量系数必须从左到右单调递增，较大的开度分数对应较大的流量系数。向量的大小必须与 **Opening fraction vector** 相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应最大开启组件的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积达到最大时的 *Kv* 流量系数值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 对应开度分数向量中各值的 Kv 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 正数向量

*Kv* 流量系数向量。每个系数对应 **Opening fraction vector** 参数中的一个值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。流量系数必须从左到右单调递增，较大的开度分数对应较大的流量系数。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum sonic conductance** — 对应最大开启组件的声速导纳 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积达到最大时的声速导纳值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Critical pressure ratio** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速导纳值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 对应开度分数向量中各值的声速导纳 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正值向量

阻性元件内部的声速导纳向量。每个导纳对应 **Opening fraction vector** 参数中的一个值。声速导纳必须从左到右单调递增，较大的开度分数对应较大的声速导纳。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 对应开度分数向量中各值的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次阻塞时的临界压力比向量，每个临界压力比对应 **Opening fraction vector** 参数中的一个值。临界压力比是流速达到当地声速时的下游与上游压力之比。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum orifice area** — 对应最大开启组件的流通面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积达到最大时节流孔开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围 [0,1] 内的正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`。

### **Orifice area vector** — 节流孔开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 向量

节流孔开口的横截面积向量。此向量中的值与 **Opening fraction vector** 参数中的元素一一对应。此向量的第一个元素是节流孔泄漏面积，最后一个元素是最大节流孔面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Laminar flow pressure ratio** — 流动在层流和湍流流态之间过渡时的压力比 `0.999`（默认）| 正标量

流动在层流和湍流流态之间过渡时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 气体端口处的流通面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。端口尺寸相同。此参数的值应与阻性元件所连接组件的入口面积相匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b: 使用改进的流量计算对气体系统建模

在以前的版本中，气体库中的模块使用转换因子来以声速导纳实现不同的节流孔参数化方法。您可以使用 **Valve parameterization** 参数来指定参数化方法。

新的参数化方法还包括新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数替代了 **Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow** 和 **Restriction area at leakage flow** 参数。

为提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference density** 参数已分别重命名为 **ISO reference temperature** 和 **ISO reference density**。
- **Cv coefficient (USCS) at maximum flow** 和 **Kv coefficient (USCS) at maximum flow** 参数已分别重命名为 **Maximum Cv coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic conductance**。
- **Control pressure vector** 参数已重命名为 **Pressure at port B (gauge) vector**。

## 描述

气体网络中的减压阀

Pressure Reducing Valve (G) 模块表示一个节流以在其出口端口 **B** 处维持预设表压的阀门。常开阀门在出口压力（相对于大气压测量）升至阀门压力设定值以上时开始关闭。开口面积随压降下降至最小值，此时阀门完全关闭，仅剩泄漏流量。

开口面积与压降之间的关系取决于阀门的参数化方法。该关系可以采用线性解析表达式或表格函数的形式。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度饱和。当背压比达到阀门的临界值时发生阻塞。该模块不捕获超声速流动。

### Control and Other Pressures

出口处的压力是阀的控制信号。出口压力超过阀的压力设定值越多，开启面积就越小。
控制压力 *PCtl* 为

PCtl=PB-PAtm

其中 *PB* 是端口 **B** 处的瞬时压力，*PAtm* 是模型中 Gas Properties (G) 模块指定的大气压。两个压力均在仿真期间以绝对压力确定。

阀的压力设定值 *PSet* 是当 **Opening characteristic** 参数为 `Linear` 时 **Set pressure (gauge)** 参数的值。当 **Opening characteristic** 参数为 `Tabulated` 时，*PSet* 是 **Pressure at port B (gauge) vector** 参数的第一个元素。

最大压力 *PMax* 为 PMax=PSet+ΔP，其中 *ΔP* 是当 **Opening characteristic** 参数为 `Linear` 时阀的压力调节范围。当 **Opening characteristic** 参数为 `Tabulated` 时，*PSet* 是 **Pressure at port B (gauge) vector** 参数的最后一个元素。

### Fraction of Valve Opening

控制压力超过压力设定值的程度决定了阀开启的大小。当 **Opening characteristic** 参数为 `Linear` 时，该模块计算阀开启分数以缩放流量特性参数。归一化控制压力为

P^=1−PCtl−PSetΔP,

其中：

- *PCtl* 是控制压力。
- *PSet* 是由 **Set pressure (gauge)** 参数指定的压力设定值。
- *ΔP* 是由 **Pressure regulation range** 参数指定的压力调节范围。

该分数经过归一化，使得阀完全关闭时为 `0`，阀完全打开时为 `1`。如果计算结果超出这些边界，该模块会将值饱和到两个限值中最近的一个。

阀开启分数 *L* 为

L=(1-Lleak)P^+Lleak,

其中 *Lleak* 是 **Leakage flow fraction** 参数的值。

**Numerical Smoothing**

当 **Opening characteristic** 参数为 `Linear` 且 **Smoothing factor** 参数非零时，该模块对归一化控制压力 p^ 应用数值平滑。启用平滑有助于在仿真中保持数值鲁棒性。

有关详细信息，请参阅 Numerical Smoothing。

### Valve Parameterizations

该模块的行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v（其中 Kv=0.865Cv）决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻性元件的声速导纳决定模块参数化。声速导纳衡量气体在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，就会发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### Opening Characteristics

流量特性将阀的开启程度与产生该开启程度的输入联系起来。开启程度表示为声速导纳、流量系数或限制面积，由 **Valve parameterization** 参数决定。

流量特性通常在稳态下给出，入口处于恒定且精心控制的压力下。这种固有流量特性仅取决于阀，它可以是线性的或非线性的，后者最常见的例子是快开型和等百分比型。为了捕获此类流量特性，该模块为 **Opening characteristic** 参数提供了选择：

- `Linear` — 流量容量的度量是孔口开启分数的线性函数。当开启分数从 `0` 上升到 `1` 时，流量容量的度量从其指定的最小值缩放到指定的最大值。
- `Tabulated` — 流量容量的度量是孔口开启分数的一般函数，可以是线性的或非线性的。该函数以表格形式指定，自变量由 **Pressure at port B (gauge) vector** 指定。

### Momentum Balance

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

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，该模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，孔口发生阻塞，该模块切换到方程

m˙=23CvN6FγxTpinρin.

当将 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，该模块使用相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **Orifice parametrization** 参数为 `Kv flow coefficient parameterization` 或 `Cv flow coefficient parameterization` 时质量流量方程的更多信息，请参阅 [2][3]。

当将 **Orifice parametrization** 设置为 `Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是声速导纳。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，该模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口发生阻塞，该模块切换到方程

m˙=CρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果将此设置用于空气以外的气体，可能需要将声速导纳乘以比重的平方根进行缩放。

有关当 **Orifice parametrization** 参数为 `Sonic conductance parameterization` 时质量流量方程的更多信息，请参阅 [1]。

当将 **Orifice parametrization** 设置为 `Orifice area parameterization` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ],

其中：

- *Sr* 是孔口或阀面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，该模块平滑过渡到方程的线性化形式，

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口发生阻塞，该模块切换到方程

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2.

有关当 **Orifice parametrization** 参数为 `Orifice area parameterization` 时质量流量方程的更多信息，请参阅 [4]。

### Mass Balance

该模块假设阀内流体的体积和质量非常小，并忽略这些值。因此，不会有流体在阀中积聚。根据质量守恒原理，通过一个端口进入阀的质量流量等于通过另一个端口流出阀的质量流量

m˙A+m˙B=0,

其中 m˙ 定义为通过 **A** 或 **B** 下标所指示的端口进入阀的质量流量。

### Energy Balance

该模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口的过程中，没有对流体做功，也没有流体做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀的能量流率。

### 假设和限制

- `Orifice area` 参数化的方程对于远离理想气体的气体不太准确。
- 该模块不建模超声速流动。
