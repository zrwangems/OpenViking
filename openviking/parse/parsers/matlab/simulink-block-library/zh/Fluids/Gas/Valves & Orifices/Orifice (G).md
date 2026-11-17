---
type: simulink-block
title: 'Orifice (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices'
documentation_page: 'orificeg'
documentation_source_path: 'ref/orificeg.html'
language: zh-CN
chinese_source: worker-translation
---

# Orifice (G)

## 端口

### 输入

### **L** — 节流口开度，无量纲物理信号

用于指定节流口开度的控制信号。在某些阀中，该信号表示行程或升程百分比。节流口在值为 `0` 时完全关闭，在值为 `1` 时完全打开。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`。
### 守恒

### **A** — 流道气体

与流阻的入口或出口开口相关联的气体守恒端口，流体通过该开口进入或离开流阻。该模块没有固有的方向性。根据流动方向，该端口可以用作入口或出口。

### **B** — 流道气体

与流阻的入口或出口开口相关联的气体守恒端口，流体通过该开口进入或离开流阻。该模块没有固有的方向性。根据流动方向，该端口可以用作入口或出口。

## 参数

### **Orifice type** — 节流口类型 `Variable`（默认）| `Constant`

由节流口面积定义的节流口类型。当您将此参数设置为 `Variable` 时，节流口面积根据端口 **L** 接收到的输入信号而变化。

### **Orifice parameterization** — 用于指定节流口流动特性的参数化方法 `Cv flow coefficient`（默认）| `Kv flow coefficient` | `Sonic conductance` | `Orifice area`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。
- `Kv flow coefficient` — 流量系数
  *K*v，
  其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速导纳决定模块参数化。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **L** 指定的控制信号转换为所选流量能力度量的方法。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`。

### **Opening fraction vector** — 用于指定表格化参数数据的控制信号值 `0 : 0.2 : 1`（默认）| 正数向量

用于指定所选流量能力度量的控制信号值向量：**Sonic conductance vector**、**Cv coefficient vector**、**Kv coefficient vector** 或 **Orifice area vector**。控制信号介于 `0` 和 `1` 之间，每个值对应阻性元件的开度分数。值越大，开度越大，流动越容易。

开度分数必须在向量中从左到右单调递增。此向量的大小必须与 **Sonic conductance vector**、**Cv coefficient vector**、**Kv coefficient vector** 或 **Orifice area vector** 参数相同。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应最大开度组件的 Cv 系数 `4`（默认）| 正标量

当端口 **L** 指定的控制信号为 `1` 且可用于流动的限制面积最大时的 *Cv* 流量系数值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

首次发生阻塞时的入口压力 *pin* 与出口压力 *pout* 之比，定义为 (pin−pout)/pin。如果您没有此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，对于许多阀而言，默认值 0.7 是合理的。

#### 依赖

要启用此参数，请将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流口关闭时与打开时的流量之比。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，在节流口处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 对应开度分数向量中值的 Cv 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 正数向量

*Cv* 流量系数向量。每个系数对应 **Opening fraction vector** 参数中的一个值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。流量系数必须从左到右单调递增，较大的开度分数对应较大的流量系数。向量的大小必须与 **Opening fraction vector** 相同。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

常数 *Cv* 流量系数的值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Cv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应最大开度组件的 Kv 系数 `3.6`（默认）| 正标量

当端口 **L** 指定的控制信号为 `1` 且可用于流动的限制面积最大时的 *Kv* 流量系数值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 对应开度分数向量中值的 Kv 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 正数向量

*Kv* 流量系数向量。每个系数对应 **Opening fraction vector** 参数中的一个值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。流量系数必须从左到右单调递增，较大的开度分数对应较大的流量系数。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖

要启用此参数，请将 **Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

常数 *Kv* 流量系数的值。此参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Kv flow coefficient`。

### **Maximum sonic conductance** — 组件最大开启时对应的声速流导 `12 l/(bar*s)`（默认值）| 正标量

当端口 **L** 处指定的控制信号为 `1` 且可用于流动的横截面积最大时的声速流导值。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Linear`。

### **Critical pressure ratio** — 流量首次阻塞时的下游与上游压力比 `0.3`（默认值）| 正标量

流量首次开始阻塞且流速达到最大值（由当地声速决定）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Orifice type** 设置为 `Constant`，**Orifice parameterization** 设置为 `Sonic conductance`。
- **Orifice type** 设置为 `Variable`，**Orifice parameterization** 设置为 `Sonic conductance`，**Opening characteristic** 设置为 `Linear`。

### **Subsonic index** — 用于表征亚声速流态下质量流量的指数 `0.5`（默认值）| 正标量

用于更精确计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认值）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认值）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **Sonic conductance vector** — 开度分数向量中各值对应的声速流导 `[1e-05, 2.4, 4.8, 7.2, 9.6, 12] l/(bar*s)`（默认值）| 正值向量

阻性元件内部的声速流导向量。每个流导对应 **Opening fraction vector** 参数中的一个值。声速流导必须从左到右单调递增，较大的开度分数对应较大的声速流导。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 开度分数向量中各值对应的临界压力比 `0.3 * ones(1,6)`（默认值）| 正数向量

流量首次阻塞时的临界压力比向量，每个临界压力比对应 **Opening fraction vector** 参数中的一个值。临界压力比是流速达到当地声速时的下游与上游压力之比。向量的大小必须与 **Opening fraction vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Sonic conductance** — 阻塞流态下流率能力的度量 `12 l/(bar*s)`（默认值）| 正标量

在阻塞开始时测得的、通过阻性元件的质量流量与上游压力和 ISO 8778 中定义的标准条件下质量密度之积的比值。此参数决定了给定上游压力下允许的最大流率。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Sonic conductance`。

### **Maximum orifice area** — 组件最大开启时对应的流通面积 `1e-4 m^2`（默认值）| 正标量

当端口 **L** 处指定的控制信号为 `1` 且可用于流动的横截面积最大时，节流孔开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Discharge coefficient** — 流量系数 `0.64`（默认值）| [0,1] 范围内的正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Orifice area`。

### **Orifice area vector** — 节流孔开口面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认值）| 向量

节流孔开口的横截面积向量。此向量中的值与 **Opening fraction vector** 参数中的元素一一对应。此向量的第一个元素是节流孔泄漏面积，最后一个元素是最大节流孔面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Variable`，将 **Orifice parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Orifice area** — 节流孔开口面积 `1e-4 m^2`（默认值）| 正标量

节流孔开口的横截面积。

#### 依赖关系

要启用此参数，请将 **Orifice type** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Orifice area`。

### **Laminar flow pressure ratio** — 层流与湍流流态之间转换时的压力比 `0.999`（默认值）| 正标量

流动在层流与湍流流态之间转换时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **Cross-sectional area at ports A and B** — 气体端口处的流通面积 `0.01 m^2`（默认值）| 正标量

每个端口处垂直于流动路径的面积。各端口尺寸相同。此参数的值应与阻性元件所连接组件的入口面积相匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2022b: 使用改进的流量计算对气体系统建模

在之前的版本中，气体库中的模块使用转换因子来以声速流导的形式实现不同的孔口参数化。您可以使用 **Orifice parameterization** 参数来指定参数化方式。

新的参数化方式还包含新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数取代了 **Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow** 和 **Restriction area at leakage flow** 参数。

为提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference density** 参数已分别重命名为 **ISO reference temperature** 和 **ISO reference density**。
- **Cv coefficient (USCS) at maximum flow** 和 **Kv coefficient (USCS) at maximum flow** 参数已分别重命名为 **Maximum Cv coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic conductance**。

### R2022b: 分离的孔口模块合并为一个

Orifice (G) 模块取代了 Orifice ISO 6358 (G) 和 Variable Orifice ISO 6358 (G)。使用新的 **Orifice Type** 参数在 `Constant` 和 `Variable` 之间进行选择。

## 描述

气体网络中的流动限制

Orifice (G) 模块表示气体网络中由于固定或可变尺寸的纯阻性元件（如流动限制、孔口或阀门）而产生的压力损失。您可以使用孔口来测量和报告气体流动特性。

### 孔口参数化

模块行为取决于 **Orifice parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 阻性元件在稳态下的声速流导决定模块参数化。声速流导衡量气体在*阻塞*状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，就会发生阻塞。
- `Orifice area` — 流动限制的尺寸决定模块参数化。

### 开度特性

当您将 **Orifice type** 设置为 `Variable` 时，模块使用端口 **L** 处的输入来控制特定参数。此输入为控制信号，与行程或升程百分比相关联。控制信号的取值范围为 `0` 到 `1`。如果您指定的值小于或大于此范围，模块会将值饱和到两个限值中最近的一个。

从控制信号到所选流量能力度量的转换取决于 **Opening characteristic** 参数化。当控制信号为 `0` 时，流量限制最大；当控制信号为 `1` 时，流量限制最小。在这些值之间，阻性元件内实现的流量取决于开度参数化是线性的还是基于表格数据：

- `Linear` — 流量能力的度量与端口 **L** 处的控制信号成正比。这两个值同步变化，直到控制信号降至 `0` 以下或升至 `1` 以上。当控制信号从 `0` 升至 `1` 时，流量能力的度量从指定的最小值缩放到指定的最大值。

  当您将 **Orifice parameterization** 设置为 `Sonic conductance` 时，模块将临界压力比和亚声速指数视为独立于控制信号的常数。当您将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient` 时，模块将参数 **xT pressure differential ratio factor at choked flow** 视为独立于控制信号的常数。
- `Tabulated` — 模块将流量能力的度量计算为端口 **L** 处控制信号的函数。此函数基于单向查找表。必须指定表格数据，使流量能力的度量随控制信号单调递增。

  当您将 **Orifice parameterization** 设置为 `Sonic conductance` 时，模块将临界压力比视为控制信号的函数，并将亚声速指数视为常数。当您将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient` 时，模块将参数 **xT pressure differential ratio factor at choked flow** 视为控制信号的函数。

### 数值平滑

当 **Orifice type** 参数为 `Variable`、**Opening characteristic** 参数为 `Linear` 且 **Smoothing factor** 参数非零时，模块对来自端口 **L** 的控制信号应用数值平滑。启用平滑有助于在仿真中保持数值鲁棒性。

有关详细信息，请参阅数值平滑。

### Momentum Balance

该模块方程取决于 **Orifice parametrization** 参数。当您将 **Orifice parametrization** 设置为 `Cv flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvN6Y(pin−pout)ρin，

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，该模块会平滑过渡到方程的线性化形式，

m˙=CvN6Ylamρavgpavg(1−Blam)(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞，模块切换到方程

m˙=23CvN6FγxTpinρin。

当您将 **Orifice parametrization** 设置为 `Kv flow coefficient parameterization` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 用 *Kv* 替换 *Cv*。有关当 **Orifice parametrization** 参数为 `Kv flow coefficient parameterization` 或 `Cv flow coefficient parameterization` 时的质量流量方程的更多信息，请参阅 [2][3]。

当您将 **Orifice parametrization** 设置为 `Sonic conductance parameterization` 时，质量流量 m˙ 为

m˙=CρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

其中：

- *C* 是声导。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，该模块会平滑过渡到方程的线性化形式，

m˙=CρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降至临界压力比 *Bcrit* 以下时，孔口变为阻塞，模块切换到方程

m˙=CρrefpinTrefTin。

**Orifice parameterization** 参数的 `Sonic conductance` 设置适用于气动应用。如果您将此设置用于空气以外的气体，则可能需要按比重的平方根对声导进行缩放。

有关当 **Orifice parametrization** 参数为 `Sonic conductance parameterization` 时的质量流量方程的更多信息，请参阅 [1]。

当您将 **Orifice parametrization** 设置为 `Orifice area parameterization` 时，质量流量 m˙ 为

m˙=CdSr2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SRS)2(poutpin)2γ]，

其中：

- *Sr* 是孔口或阀门面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，该模块会平滑过渡到方程的线性化形式，

m˙=CdSr2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SRS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口变为阻塞，模块切换到方程

m˙=CdSR2γγ+1pinρin1(γ+12)2γ−1−(SRS)2。

有关当 **Orifice parametrization** 参数为 `Orifice area parameterization` 时的质量流量方程的更多信息，请参阅 [4]。

### Mass Balance

该模块假设阻性元件内部流体的体积和质量非常小，并忽略这些值。因此，流体不能在阻性元件中积聚。根据质量守恒原理，通过一个端口流入阀门并流出的质量流量等于通过另一个端口流出阀门的质量流量

m˙A+m˙B=0，

其中 m˙ 定义为通过由 **A** 或 **B** 下标指示的端口流入阀门的质量流量。

### Energy Balance

该模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口流动时，没有对流体做功，也没有由流体做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口 **A** 或 **B** 流入阀门的能量流率。

### 假设和限制

- `Orifice area` 参数化的方程对于远离理想气体的气体不太准确。
- 该模块不建模超声速流动。
