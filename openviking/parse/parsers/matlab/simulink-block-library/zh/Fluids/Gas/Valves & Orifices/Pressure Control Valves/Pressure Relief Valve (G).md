---
type: simulink-block
title: 'Pressure Relief Valve (G)'
family: 'gas'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalveg'
documentation_source_path: 'ref/pressurereliefvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Relief Valve (G)

## 端口

### 守恒

### **A** — 阀门入口气体

与流体必须进入阀门的开口相关联的气体守恒端口。

### **B** — 阀门入口气体

与流体必须离开阀门的开口相关联的气体守恒端口。

## 参数

### **开启压力规格** — 用作阀门控制信号的压力测量选择 `Pressure difference of port A relative to port B`（默认）| `Gauge pressure at port A`

用作阀门控制信号的压力测量选择。该模块使用此设置来确定阀门应何时开始开启。在默认设置 `Pressure difference of port A relative to port B` 下，阀门的开启压力表示为从入口到出口的压降。在替代设置 `Gauge pressure at port A` 下，它表示为入口表压。

### **阀门参数化** — 用于指定阀门流量特性的参数化 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速流导决定模块参数化。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### **开启特性** — 计算阀门开启特性的方法 `Linear`（默认）| `Tabulated`

该模块用于计算阀门开启面积的方法。`Linear` 设置将开启面积视为孔口开启分数的线性函数。`Tabulated` 设置允许使用以表格形式指定的通用非线性关系。

### **设定压差** — 阀门操作的阈值压差 `0 MPa`（默认）| 正标量

开启阀门所需的从入口到出口的压降。此值标记压力调节范围的起点，在该范围内阀门逐渐开启以抑制压力上升。阀门的开启面积取决于实际压降与此处指定值之间的差值。

#### 依赖关系

要启用此参数，请将 **开启压力规格** 设置为 `Pressure difference at port A relative to port B`，并将 **开启特性** 设置为 `Linear`。

### **压力调节范围** — 开启面积可变的压力范围宽度 `0.1 MPa`（默认）| 正标量

阀门工作范围。阀门在设定压力值处开始开启，并在 *pmax* 处完全开启，即压力调节范围的终点，其中 *pmax = pset + prange*。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **设定压力（表压）** — 开启阀门所需的入口表压 `0.1 MPa`（默认）| 以压力单位表示的正标量

开启阀门所需的入口表压。此参数标记压力调节范围的起点，在该范围内阀门逐渐开启以抑制压力上升。阀门的开启面积取决于实际入口压力与此处指定值之间的差值。

#### 依赖关系

要启用此参数，请将 **开启压力规格** 设置为 `Gauge pressure at port A`，并将 **开启特性** 设置为 `Linear`。

### **开启压差向量** — 用于指定阀门开启数据的控制压力向量 `0.2 : 0.2 : 1.2 MPa`（默认）| 向量

用于指定所选阀门开启度量——声速流导、流量系数或开启面积——的控制压力向量。此向量的大小必须与包含阀门开启数据的向量相同。向量元素必须为正，并从左到右单调递增。这些压力值是从入口到出口的压降。

此参数的第一个元素是阀门的压力设定值，阀门在该压力下开始开启。最后一个元素是最大压力，阀门在该压力下完全开启。两者之差是阀门的压力调节范围。

#### 依赖关系

要启用此参数，请将 **开启压力规格** 设置为 `Pressure difference at port A relative to port B`，并将 **开启特性** 设置为 `Tabulated`。

### **开启压力（表压）向量** — 用于指定阀门开启数据的控制压力向量 `0.2 : 0.2 : 1.2 MPa`（默认）| 向量

用于指定所选阀门开启度量——声速流导、流量系数或开启面积——的控制压力向量。此向量的大小必须与包含阀门开启数据的向量相同。向量元素必须为正，并从左到右单调递增。这些压力是入口处的表压。

此参数的第一个元素是阀门的压力设定值，阀门在该压力下开始开启。最后一个元素是最大压力，阀门在该压力下完全开启。两者之差是阀门的压力调节范围。

#### 依赖关系

要启用此参数，请将 **开启压力规格** 设置为 `Gauge pressure at port A`，并将 **开启特性** 设置为 `Tabulated`。

### **最大 Cv 流量系数** — 对应组件最大开启状态的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积最大时，*Cv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻性元件的容易程度。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，在该比值下首次发生阻塞。如果您没有此值，请在 ISA-75.01.01 [3] 的表 2 中查找。否则，对于许多阀门，默认值 0.7 是合理的。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **泄漏流量分数** — 流量比 `1e-6`（默认）| 正标量

孔口关闭时的流量与开启时的流量之比。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当孔口处于接近开启或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **开启特性** 设置为 `Linear`。

### **Cv 流量系数向量** — 对应于开启比例向量中各值的 Cv 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 正数向量

*Cv* 流量系数的向量。每个系数对应于 **Opening fraction vector** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻性元件的容易程度。流量系数必须从左到右单调递增，较大的开启分数表示较大的流量系数。向量的大小必须与 **Opening fraction vector** 相同。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **最大 Kv 流量系数** — 对应组件最大开启状态的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积最大时，*Kv* 流量系数的值。此参数衡量气体在压差驱动下穿过阻性元件的容易程度。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Kv 流量系数向量** — 对应于开启比例向量中各值的 Kv 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 正数向量

*Kv* 流量系数的向量。每个系数对应于 **Opening fraction vector** 参数中的一个值。此参数衡量气体在压差驱动下穿过阻性元件的容易程度。流量系数必须从左到右单调递增，较大的开启分数表示较大的流量系数。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **最大声速流导** — 对应组件最大开启状态的声速流导 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积最大时，声速流导的值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Linear`。

### **临界压力比** — 流动首次阻塞时的下游与上游压力比 `0.3`（默认）| 正标量

流动首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比是出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Linear`。

### **亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更准确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`。

### **声速流导向量** — 对应于开启比例向量中各值的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认）| 正数值向量

阻性元件内部的声速流导向量。每个流导对应于 **Opening fraction vector** 参数中的一个值。声速流导必须从左到右单调递增，较大的开启分数表示较大的声速流导。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **临界压力比向量** — 对应于开启比例向量中各值的临界压力比 `0.3 * ones(1,6)`（默认）| 正数向量

流动首次阻塞时的临界压力比向量，每个临界压力比对应于 **Opening fraction vector** 参数中的一个值。临界压力比是下游与上游压力之比，在该比值下流速达到当地声速。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Sonic conductance`，并将 **开启特性** 设置为 `Tabulated`。

### **最大孔口面积** — 对应组件最大开启状态的流动面积 `1e-4 m^2`（默认）| 正标量

当可用于流动的横截面积最大时，孔口开口的横截面积。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Linear`。

### **排放系数** — 排放系数 `0.64`（默认）| 范围 [0,1] 内的正标量

考虑理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Orifice area`。

### **孔口面积向量** — 孔口开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 向量

孔口开口的横截面积向量。此向量中的值与 **Opening fraction vector** 参数中的元素一一对应。此向量的第一个元素是孔口泄漏面积，最后一个元素是最大孔口面积。

#### 依赖关系

要启用此参数，请将 **阀门参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Tabulated`。

### **层流压力比** — 流动在层流与湍流态之间转换的压力比 `0.999`（默认）| 正标量

流动在层流与湍流态之间转换的压力比。压力比是出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **端口 A 和 B 的横截面积** — 气体端口处的流动面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。端口尺寸相等。此参数的值应与阻性元件连接到的组件的入口面积匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b: 使用改进的流量计算对气体系统建模

在之前的版本中，Gas 库中的模块使用转换因子来以 sonic conductance 实现不同的孔口参数化。您可以使用 **Valve parameterization** 参数来指定参数化。

新的参数化还包括新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数替代 **Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow** 和 **Restriction area at leakage flow** 参数。

为提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference density** 参数已分别重命名为 **ISO reference temperature** 和 **ISO reference density**。
- **Cv coefficient (USCS) at maximum flow** 和 **Kv coefficient (USCS) at maximum flow** 参数已分别重命名为 **Maximum Cv coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic conductance**。
- **Pressure control specification** 参数已重命名为 **Opening pressure specification**。此参数的选项已重命名为 `Pressure difference of port A relative to port B` 和 `Gauge pressure at port A`。
- **Control pressure vector** 参数已重命名为 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector**，具体取决于 **Opening pressure specification** 的选择。

## 描述

气体网络中的泄压阀

Pressure Relief Valve (G) 模块表示一个孔口，该孔口随入口压力打开，以防止压力达到极端水平。在正常压力下，阀门关闭并仅释放泄漏流量。高于指定压力设定值时，阀门开始打开，从而允许气体从高压区域排出。开启面积随入口压力增加而增大，直至达到最大值；此时阀门完全打开，压力不受阻碍地上升。

阀门响应相对于出口的入口压力，或相对于环境的入口压力。所选择的压力测量值是阀门的*控制压力*。**Control pressure specification** 参数决定模块在仿真期间使用哪个测量值。

开启面积与压降之间的关系取决于阀门的参数化。该关系可以采用线性解析表达式或表格函数的形式。

流动可以是层流或湍流，并且可达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能提高速度时，流动发生阻塞，速度饱和。当背压比达到该阀门特有的临界值时，发生阻塞。该模块不捕获超声速流动。

### 阀门开启比例

入口压力是阀门控制信号。入口压力超过阀门压力设定值越多，开启面积越大。控制压力超过压力设定值的量决定阀门开启程度。当 **Opening characteristic** 参数为 `Linear` 时，模块计算阀门开启比例以缩放流量特性参数。归一化控制压力为

p^=PCtl-PSetΔP,

其中：

- *PCtl* 是控制压力。

  当 **Opening pressure specification** 为
  `Pressure difference of port A relative to port
  B` 时，

  PCtl=PA−PB,

  其中 *PA* 是端口 **A** 的绝对压力，*PB* 是端口 **B** 的绝对压力。

  当 **Opening pressure specification** 为
  `Gauge pressure at port A` 时，

  PCtl=PA−PAtm,

  其中 *PAtm* 是模型中 Gas Properties
  (G) 模块指定的大气压力。
- *PSet* 是设定压力。

  当 **Opening pressure specification** 为
  `Pressure difference of port A relative to port
  B` 时，*PSet* 是 **Set pressure differential**
  参数的值

  当 **Opening pressure specification** 为
  `Gauge pressure at port A` 时，
  *PSet* 是 **Set pressure (gauge)** 参数的值
- *ΔP* 是 **Pressure
  regulation range** 参数的值。

阀门开启比例 *L* 为

L=(1-Lleak)P^+Lleak,

其中 *Lleak* 是 **Leakage flow fraction** 参数的值。

**数值平滑**

当 **Opening characteristic** 参数为 `Linear` 且 **Smoothing factor** 参数非零时，模块对归一化控制压力 p^ 应用数值平滑。启用平滑有助于在仿真中保持数值稳健性。

有关详细信息，请参阅数值平滑。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的容易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的容易程度。
- `Sonic conductance` — 稳态下阻力元件的 sonic conductance 决定模块参数化。sonic conductance 衡量气体在 *阻塞* 时流动的容易程度，*阻塞* 是流速达到当地声速的状态。当下游压力与上游压力之比达到称为 *临界压力比* 的临界值时，发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### 开启特性

流量特性将阀门开启程度与产生该开启程度的输入相关联。开启程度表示为 sonic conductance、流量系数或限制面积，具体由 **Valve parameterization** 参数决定。

流量特性通常在稳态下给出，此时入口处于恒定且经过仔细控制的压力下。流量特性仅取决于阀门，可以是线性或非线性的。为捕获流量特性，请使用 **Opening characteristic** 参数：

- `Linear` — 流量容量的度量是阀门开启比例的线性函数。当开启比例从 `0` 升至 `1` 时，流量容量的度量从指定的最小值缩放至指定的最大值。
- `Tabulated` — 流量容量的度量是孔口开启比例的一般函数，可以是线性或非线性的。该函数以表格形式指定，其自变量由 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 指定。

### 动量平衡

模块方程取决于 **Orifice parametrization** 参数。当您将 **Orifice parametrization** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

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

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 低于 1−FγxT 时，孔口发生阻塞，模块切换为方程

m˙=23CvN6FγxTpinρin.

当您将 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，模块使用相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关 **Orifice parametrization** 参数为 `Kv flow coefficient parameterization` 或 `Cv flow coefficient parameterization` 时质量流量方程的详细信息，请参阅 [2][3]。

当您将 **Orifice parametrization** 设置为 `Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m,

其中：

- *C* 是 sonic conductance。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam).

当压力比 pout/pin 低于临界压力比 *Bcrit* 时，孔口发生阻塞，模块切换为方程

m˙=CρrefpinTrefTin.

**Valve parameterization** 参数的 `Sonic conductance` 设置用于气动应用。如果将此设置用于空气以外的气体，您可能需要按比重的平方根缩放 sonic conductance。

有关 **Orifice parametrization** 参数为 `Sonic conductance parameterization` 时质量流量方程的详细信息，请参阅 [1]。

当您将 **Orifice parametrization** 设置为 `Orifice area parameterization` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ],

其中：

- *Sr* 是孔口或阀门面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 低于 (2γ+1)γγ−1 时，孔口发生阻塞，模块切换为方程

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2.

有关 **Orifice parametrization** 参数为 `Orifice area parameterization` 时质量流量方程的详细信息，请参阅 [4]。

### 质量平衡

模块假设阀门内部流体的体积和质量非常小，并忽略这些值。因此，流体不能在阀门中积聚。根据质量守恒原理，通过一个端口流入阀门的质量流量等于通过另一个端口流出阀门的质量流量

m˙A+m˙B=0,

其中 m˙ 定义为通过 **A** 或 **B** 下标所指示的端口流入阀门的质量流量。

### 能量平衡

模块的阻力元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口过程中，不对流体做功，也不由流体做功。能量只能通过对流、通过端口 **A** 和 **B** 流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0,

其中 *ϕ* 是通过端口 **A** 或 **B** 流入阀门的能量流量。

### 假设与限制

- `Orifice area` 参数化的方程对于远离理想状态的气体精度较低。
- 该模块不对超声速流动建模。
