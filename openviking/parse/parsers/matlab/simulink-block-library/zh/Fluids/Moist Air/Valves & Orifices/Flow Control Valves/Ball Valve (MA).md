---
type: simulink-block
title: 'Ball Valve (MA)'
family: 'moist-air'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Valves & Orifices / Flow Control Valves'
documentation_page: 'ballvalvema'
documentation_source_path: 'ref/ballvalvema.html'
language: zh-CN
chinese_source: worker-translation
---

# Ball Valve (MA)

## 端口

### 输入

### **S** — 阀门位置，rad 物理信号

与阀门位置相关联的物理信号端口，单位为 rad。值 0 表示阀门完全关闭，值 π/2 表示阀门完全打开。
### 守恒

### **A** — 阀门入口或出口湿空气

与阀门入口或出口相关联的湿空气守恒端口。

### **B** — 阀门入口或出口湿空气

与阀门入口或出口相关联的湿空气守恒端口。

## 参数

### **Valve parameterization** — 用于指定阀门流动特性的参数化 `Orifice area based on geometry`（默认） | `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

计算质量流量的方法：

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。
- `Kv flow coefficient` — 流量系数
  *K*v，
  其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻力元件的声速流导决定模块参数化。
- `Orifice area` — 流动节流的尺寸决定模块参数化。

### **Opening characteristic** — 球阀参数化 `Area of overlapping circles`（默认） | `Tabulated`

用于通过重叠圆面积方法或表格化数据对模块进行参数化的选项。

### **Discharge coefficient** — 流量系数 `0.64`（默认） | 位于 [0,1] 范围内的正标量

用于考虑理论流动中排放损失的修正系数。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`。

### **Area vector** — 用于表格化参数化的流通面积 `[1e-10, 45, 90, 135, 180, 225, 270, 315, 360, 405, 450]` `mm^2`（默认） | 正数向量

给定球旋转角度下的流通面积。每个元素与 **Ball rotation vector** 参数中的元素一一对应。第一个元素对应阀门泄漏，且必须为非零值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应于最大开度组件的 *Cv* 系数 `4`（默认） | 正标量

当可用于流动的节流面积达到最大时，*Cv* 流量系数的值。此参数用于衡量湿空气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Area of overlapping circles`。

### **Cv flow coefficient vector** — 对应于球旋转向量中数值的 *Cv* 系数 `[1e-06, .0725, .1437, .2375, .35, .5375, .875, 1.3125, 2.125, 3.25, 4]` `1`（默认） | 正数向量

*Cv* 流量系数向量。每个系数对应于 **Ball rotation vector** 参数中的一个元素。此参数用于衡量湿空气在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **Ball rotation vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Ball rotation vector** — 用于指定表格化参数数据的值 `pi / 2 .* (0 : 0.1 : 1)` `rad`（默认） | 正数向量

给定流量系数或面积下的球旋转角度。此向量中的元素必须与 **Cv flow coefficient vector**、**Kv flow coefficient vector**、**Sonic conductance vector** 或 **Area vector** 参数中的元素一一对应。此向量中的元素必须从左到右单调递增。

#### 依赖关系

要启用此参数，请将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应于最大开度组件的 *Kv* 系数 `3.6`（默认） | 正标量

当可用于流动的节流面积达到最大时，*Kv* 流量系数的值。此参数用于衡量湿空气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Area of overlapping circles`。

### **Kv flow coefficient vector** — 对应于球旋转向量中数值的 *Kv* 系数 `[1e-06, .0653, .1293, .2137, .315, .4838, .7875, 1.1813, 1.8381, 2.8112, 3.6]`（默认） | 正数向量

*Kv* 流量系数向量。每个系数对应于 **Ball rotation vector** 参数中的一个元素。此参数用于衡量湿空气在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **Ball rotation vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认） | 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，在该处首次发生阻塞。如果您没有此值，请在 ISA-75.01.01 [3] 的表 2 中查找。否则，默认值 0.7 对许多阀门而言是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum sonic conductance** — 对应于最大开度组件的声速流导 `12` `l/(bar*s)`（默认） | 正标量

当可用于流动的横截面积达到最大时，声速流导的值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Area of overlapping circles`。

### **Critical pressure ratio** — 流动首次发生阻塞时的下游压力与上游压力之比 `0.3`（默认） | 正标量

流动首次开始阻塞且流速达到由当地声速给出的最大值时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Area of overlapping circles`。

### **Sonic conductance vector** — 对应于球旋转向量中数值的声速流导 `[1e-05, .2175, .4312, .7125, 1.05, 1.6125, 2.625, 3.9375, 6.375, 9.75, 12]` `l/(bar*s)`（默认） | 正数向量

阻力元件内部的声速流导向量。每个流导对应于 **Ball rotation vector** 参数中的一个元素。向量的大小必须与 **Ball rotation vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Critical pressure ratio vector** — 对应于球旋转向量中数值的临界压力比 `0.3 * ones(1, 11)`（默认） | 正数向量

流动首次发生阻塞时的临界压力比向量。每个临界压力比对应于 **Ball rotation vector** 参数中的一个元素。临界压力比是流动速度达到当地声速时的下游压力与上游压力之比。向量的大小必须与 **Ball rotation vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Subsonic index** — 用于计算亚声速流态下质量流量的指数 `0.5`（默认） | 正标量

用于计算亚声速流态下质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference temperature** — ISO 8778 参考温度 `293.15 K`（默认） | 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO reference density** — ISO 8778 参考密度 `1.185 kg/m^3`（默认） | 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **Cross-sectional area at ports A and B** — 湿空气端口处的流通面积 `pi * (0.025 ^ 2) / 4` `m^2`（默认） | 正标量

阀门端口的横截面积。阀门端口是阀体中流动与球孔相交的路径。

### **Ball bore area** — 球孔面积 `pi * (0.02 ^ 2) / 4` `m^2`（默认） | 正标量

阀球中孔的横截面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`，并将 **Opening characteristic** 设置为 `Area of overlapping circles`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认） | 正标量

节流口关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`，并将 **Opening characteristic** 设置为 `Area of overlapping circles`。

### **Laminar flow pressure ratio** — 流动在层流与湍流流态之间转换时的压力比 `0.999`（默认） | 正标量

流动在层流与湍流流态之间转换时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

## 所属库

Simscape / Fluids / Moist Air / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

湿空气网络中的球阀

Ball Valve (MA) 模块对湿空气网络中通过球阀的流动进行建模。带有中心孔（或孔）的旋转球控制阀门的流动。当孔与阀门入口和出口对齐时，阀门打开。端口 **S** 处的物理信号控制球的旋转。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数
  *C*v
  决定模块参数化。流量系数衡量湿空气在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数
  *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量湿空气在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声速流导决定模块参数化。声速流导衡量湿空气在*阻塞*状态下流动的难易程度，该状态指流速达到当地声速。当下游压力与上游压力之比达到称为*临界压力比*的临界值时，发生阻塞。
- `Orifice area` — 流动节流的尺寸决定模块参数化。

### 开口面积

模块在仿真期间根据端口 **S** 处的输入计算球阀开度。开口面积计算取决于 **Opening Characteristic** 参数。

**重叠圆面积**

如果将 **Opening Characteristic** 设置为 `Area of overlapping circles`，则模块通过假设阀门端口与球孔为重叠圆来计算阀门的开口面积。当来自端口 **S** 的输入信号超出 0 rad 到 π/2 rad 的范围时，开口面积饱和。

模块按如下公式计算开口面积

Aopen=sin(φ)Rbore2[cos−1(λbore)−λbore1−λ2bore]+Rport2[cos−1(λport)−λport1−λ2port]λbore=Rbore2−Rport2+l22Rborelλport=Rport2−Rbore2+l22Rportl

其中：

- *Rport* 和
  *Rbore* 分别是阀门端口和球孔的半径。
- *l* 是孔中心与阀门端口中心的位移。
- *φ* 是由物理信号 **S** 给出的球阀旋转角度。阀门在 0 rad 时完全关闭，在 π/2 rad 时完全打开。

**表格化面积**

如果将 **Opening Characteristic** 设置为 `Tabulated`，则模块根据 **Area vector**、**Cv flow coefficient vector**、**Kv flow coefficient vector** 或 **Sonic conductance vector** 参数对阀门开度进行插值。这些向量中的元素与 **Ball rotation vector** 参数中的元素一一对应。模块使用线性插值在数据点之间插值，并对超出表格边界的点使用最近邻外插。

### 动量平衡

模块方程取决于 **Valve parametrization** 参数。当将 **Valve parametrization** 设置为 `Cv flow coefficient` 时，质量流量 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin，

其中：

- *Cv* 是 **Maximum Cv flow coefficient** 参数的值。
- *Sopen* 是阀门开口面积。
- *SMax* 是阀门完全打开时的最大阀门面积。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *ρin* 是入口密度。

膨胀系数为

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是等熵指数与 1.4 之比。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升高到超过 **Laminar flow pressure ratio** 参数 *Blam* 的值时，模块平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降到低于 1−FγxT 时，节流孔发生阻塞，模块切换到以下方程

m˙=23CvSopenSMaxN6FγxTpinρin。

当将 **Valve parametrization** 设置为 `Kv flow coefficient` 时，模块使用这些相同的方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。有关当 **Valve parametrization** 参数为 `Kv flow coefficient` 或 `Cv flow coefficient` 时质量流量方程的更多信息，请参见 [2][3]。

当将 **Valve parametrization** 设置为 `Sonic conductance` 时，质量流量 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

其中：

- *C* 是 **Maximum sonic conductance** 参数的值。
- *Bcrit* 是临界压力比。
- *m* 是 **Subsonic index** 参数的值。
- *Tref* 是 **ISO reference temperature** 参数的值。
- *ρref* 是 **ISO reference density** 参数的值。
- *Tin* 是入口温度。

当压力比 pout/pin 升高到超过 **Laminar flow pressure ratio** 参数 *Blam* 的值时，模块平滑过渡到方程的线性化形式，

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降到低于临界压力比 *Bcrit* 时，节流孔发生阻塞，模块切换到以下方程

m˙=CSopenSMaxρrefpinTrefTin。

**Valve parameterization** 参数的 `Sonic conductance` 设置用于气动应用。如果将此设置用于含有高水平微量气体的湿空气，或者对空气以外的流体建模，则可能需要按混合气体比重的平方根缩放声速流导。

有关当 **Valve parametrization** 参数为 `Sonic conductance` 时质量流量方程的更多信息，请参见 [1]。

当将 **Valve parametrization** 设置为 `Orifice area based on geometry` 时，质量流量 m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ]，

其中：

- *Sopen* 是阀门开口面积。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升高到超过 **Laminar flow pressure ratio** 参数 *Blam* 的值时，模块平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降到低于 (2γ+1)γγ−1 时，节流孔发生阻塞，模块切换到以下方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2。

有关当 **Valve parametrization** 参数为 `Orifice area based on geometry` 时质量流量方程的更多信息，请参见 [4]。

### 质量平衡

模块保持通过阀门的质量守恒

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中 *ṁ* 是质量流量，下标 *w* 表示水蒸气，下标 *g* 表示微量气体，下标 *d* 表示水滴。

### 能量平衡

模块的阻性元件是绝热组件。流体与其周围壁面之间不会发生热交换。流体从入口到出口流动过程中，没有对流体做功，也没有由流体做功。能量只能通过平流，经由端口 **A** 和 **B** 流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口 **A** 或 **B** 进入阀门的能量流率。

### 假设与限制

- 该模块不对超声速流动建模。
