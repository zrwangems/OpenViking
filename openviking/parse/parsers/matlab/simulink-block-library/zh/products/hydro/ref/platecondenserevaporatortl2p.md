---
type: simulink-block
title: 'Plate Condenser Evaporator (TL-2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid - Thermal Liquid'
documentation_page: 'platecondenserevaporatortl2p'
documentation_source_path: 'ref/platecondenserevaporatortl2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Plate Condenser Evaporator (TL-2P)

## 端口

### 输出

### **Z** — 液体、混合物和蒸气区分数，unitless physical signal

物理信号输出端口，用于测量热交换器中的液体、混合物和蒸气区分数。
### 守恒

### **A1** — 热液体入口或出口热液体

与热液体关联的入口或出口端口。

### **B1** — 热液体入口或出口热液体

与热液体关联的入口或出口端口。

### **A2** — 两相流体入口或出口两相流体

与两相流体关联的入口或出口端口。

### **B2** — 两相流体入口或出口两相流体

与两相流体关联的入口或出口端口。

## 参数

### 配置

### **Flow arrangement** — 流路对齐 `Counter flow`（默认） | `Parallel flow`

热交换器中的流路对齐。可用的流动布置包括：

- `Parallel flow` — 流动沿相同方向运行。
- `Counter flow` — 流动彼此平行，方向相反。

### **Number of plates** — 热交换器中的板片数量 `25`（默认） | positive scalar

热交换器中的板片数量。流体流经每个板片的两侧，包括端板和起始板。

### **Plate length** — 板片长度 `1` `m`（默认） | positive scalar

每个板片的长度。此值是板片较长的一侧，也是流体的流动轴。

### **Plate width** — 板片宽度 `0.5` `m`（默认） | positive scalar

每个板片的宽度。

### **Spacing between plates** — 板片之间的间距 `5e-3` `m`（默认） | positive scalar

每个板片之间的间隙。此参数值通常等于波纹深度。

### **Corrugation pattern specification** — 用于指定波纹图案的选项 `Surface area enlargement factor`（默认） | `Chevron geometry`

是直接指定表面面积扩大系数，还是由模块根据指定的人字形几何结构计算扩大系数。

### **Surface area enlargement factor** — 考虑板片面积增加的乘数 `1.17`（默认） | positive scalar

考虑因波纹导致板片表面积增加的乘数。如果每个板片完全平坦，则此参数的值为 1。
否则，此值是实际总表面积与板片形状二维投影面积之比。

#### 依赖关系

要启用此参数，请将 **Corrugation pattern specification** 设置为 `Surface area enlargement factor`。

### **Corrugation chevron angle** — 板片上人字形的角度 `60` `deg`（默认） | positive scalar

每个板片上人字形波纹的角度。此值是此板片图中的 *β*：

#### 依赖关系

要启用此参数，请将 **Corrugation pattern specification** 设置为 `Chevron geometry`。

### **Corrugation depth to pitch ratio** — 人字形深度与节距之比 `0.28`（默认） | positive scalar

人字形波纹深度与波纹节距之比。波纹节距是波纹波长。此参数的值为此图中的 *b/λ*：

#### 依赖关系

要启用此参数，请将 **Corrugation pattern specification** 设置为 `Chevron geometry`。

### **Enable plate thermal resistance** — 对板片热阻建模的选项 `off`（默认） | on

对板片热阻建模的选项。如果选中此复选框，模块将使用 **Plate thickness** 和 **Plate thermal conductivity** 参数的值来计算穿过每个板片的热阻。如果清除此复选框，模块不会对穿过板片的热阻效应建模。

### **Enable plate thermal mass** — 对板片热质量建模的选项 `off`（默认） | `on`

是否对板片热质量建模。对板片热质量建模会在板片对温度或热流变化做出响应时引入瞬态响应延迟。如果清除 **Enable plate thermal mass**，则模块假定板片足够薄，以使瞬态响应在传热时间尺度上为瞬时响应。

### **Plate thickness** — 板片厚度 `5e-4` `m`（默认） | positive scalar

热交换器中每个板片的厚度。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal resistance** 或 **Enable plate thermal mass**。

### **Plate density** — 板片密度 `7800 kg/m^3`（默认） | positive scalar

板片的密度。模块使用此值计算板片热质量。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal mass**。

### **Plate specific heat** — 板片比热 `490 J/(K*kg)`（默认） | positive scalar

板片的比热。模块使用此值计算板片热质量。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal mass**。

### **Plate thermal conductivity** — 穿过板片的热导率 `15` `W/(K*m)`（默认） | positive scalar

每个板片的热导率。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal resistance**。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认） | positive scalar

热液体端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认） | positive scalar

热液体端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01` m^2（默认） | positive scalar

两相流体端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处的流通面积 `0.01` m^2（默认） | positive scalar

两相流体端口 **B2** 处的流通面积。

### 热液体 1

### **Pressure loss model** — 根据黏性摩擦计算压力损失的方法 `Correlation for flow between corrugated plates`（默认） | `Friction factor`

热液体因黏性摩擦产生压力损失的计算方法。设置包括：

- `Friction factor` — 模块基于板片通道之间流动的恒定 Darcy 摩擦系数计算压力损失，该系数由 **Darcy friction factor for flow between corrugated plates** 参数指定。
- `Correlation for flow between corrugated plates` — 模块使用适用于具有人字形或鱼骨形图案的板式热交换器的 Martin 关联式计算压力损失。

### **Darcy friction factor for flow between corrugated plates** — 恒定 Darcy 摩擦系数 `1.7`（默认） | positive scalar

用于计算压力损失的恒定 Darcy 摩擦系数。

如果您有热交换器两端压力损失 *Δpdata* 和通过热交换器的质量流量 *ṁdata* 的数据，则此参数的值为

fdarcy=DhS2Lp[2ρ(Δpdatam˙data2)−ξportsSport].

如果您没有 *ξports* 的数据，请在此表达式中使用 **Loss coefficient for inlet and outlet manifolds and ports** 参数的默认值。如果您有多个 *Δpdata* 和 *ṁdata* 数据点，请使用最小二乘拟合求 *fdarcy*。

如果您知道热交换器的损失系数值 *ξloss*，则 *fDarcy = ξloss Dh / LP*。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Friction factor`。

### **Loss coefficient for inlet and outlet manifolds and ports** — 入口和出口歧管及端口的压力损失系数 `1.5`（默认） | positive scalar

用于考虑热液体侧入口和出口歧管及端口处损失的压力损失系数。

### **Heat transfer coefficient model** — 计算传热系数的方法 `Correlation for flow between corrugated plates`（默认） | `Colburn equation`

计算热流体传热系数的方法。可用的设置包括：

- `Colburn equation` — 使用此设置可通过定义 Colburn 方程的变量 *a*、*b* 和 *c* 来计算传热系数。使用此选项可通过估计系数将传热结果拟合到实验数据。
- `Correlation for flow between corrugated plates` — 使用此设置可基于板片几何数据和 Martin 关联式计算传热系数。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c** — Colburn 方程系数 `[.141, .748, .333]`（默认） | three-element vector

包含 Colburn 方程经验系数的三元素向量。Colburn 方程是用于计算 Nusselt 数的公式。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients for Martin correlation** — Martin 关联式系数 `[.122, .374, .333]`（默认） | three-element vector

包含系数 *c1*、*c2* 和 *c3* 的三元素向量，模块使用这些系数通过 Martin 关联式计算 Nusselt 数：

Nu=c1(fDarcyRe2sin2β)c2Prc3.

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow between corrugated plates`。

### **Fouling factor** — 污垢沉积产生的热阻 `0.1` `K*m^2/kW`（默认） | positive scalar

由于壁面表面上的污垢层而产生的附加热阻。在实际系统中，污垢沉积会随时间增长。然而，其增长足够缓慢，因此模块假定污垢在仿真期间恒定。

### **Initial thermal liquid pressure** — 仿真开始时的热液体压力 `0.101325` `MPa`（默认） | positive scalar

仿真开始时的热液体压力。

### **Initial thermal liquid temperature** — 仿真开始时的热液体温度 `293.15` `K`（默认） | positive scalar | two-element vector

仿真开始时热液体通道中的温度。此参数可以是标量或两元素向量。标量值表示流体流动中的平均初始温度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始温度。模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

### 两相流体 2

### **Pressure loss model** — 根据黏性摩擦计算压力损失的方法 `Correlation for flow between corrugated plates`（默认） | `Friction factor`

两相流体因黏性摩擦产生压力损失的计算方法。设置包括：

- `Friction factor` — 模块基于板片通道之间流动的恒定 Darcy 摩擦系数计算压力损失，该系数由 **Darcy friction factor for flow between corrugated plates** 参数指定。
- `Correlation for flow between corrugated plates` — 模块使用适用于具有人字形或鱼骨形图案的板式热交换器的 Martin 关联式计算压力损失。

### **Darcy friction factor for flow between corrugated plates** — 恒定 Darcy 摩擦系数 `1.7`（默认） | positive scalar

用于计算压力损失的恒定 Darcy 摩擦系数。

如果您有热交换器两端压力损失 *Δpdata* 和通过热交换器的质量流量 *ṁdata* 的数据，则此参数的值为

fdarcy=DhS2Lp[2ρ(Δpdatam˙data2)−ξportsSport].

如果您没有 *ξports* 的数据，请在此表达式中使用 **Loss coefficient for inlet and outlet manifolds and ports** 参数的默认值。如果您有多个 *Δpdata* 和 *ṁdata* 数据点，请使用最小二乘拟合求 *fdarcy*。

如果您知道热交换器的损失系数值 *ξloss*，则 *fDarcy = ξloss Dh / LP*。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Friction factor`。

### **Loss coefficient for inlet and outlet manifolds and ports** — 入口和出口歧管及端口的压力损失系数 `1.5`（默认） | positive scalar

用于考虑热液体侧入口和出口歧管及端口处损失的压力损失系数。

### **Heat transfer coefficient model** — 计算传热系数的方法 `Correlation for flow between corrugated plates`（默认） | `Colburn equation`

计算两相流体传热系数的方法。可用的设置包括：

- `Colburn equation` — 使用此设置可通过定义 Colburn 方程的变量 *a*、*b* 和 *c* 来计算传热系数。使用此选项可通过估计系数将传热结果拟合到实验数据。
- `Correlation for flow between corrugated plates` — 使用此设置可基于板片几何数据和 Martin 关联式计算传热系数。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in liquid zone** — 液相区中的 Colburn 方程系数 `[.141, .748, .333]`（默认） | three-element vector

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，模块通过在每个区中使用 Colburn 方程来计算该数。Colburn 方程的一般形式为：

Nu=aRebPrc.

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone** — 混合区中的 Longo 关联式方程系数 `[1.875, .445, .333]`（默认） | three-element vector

包含 Longo 关联式系数的三元素向量。模块使用 Longo 关联式计算混合区中的 Nusselt 数。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in vapor zone** — 气相区中的 Colburn 方程系数 `[.141, .748, .333]`（默认） | three-element vector

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，模块通过在每个区中使用 Colburn 方程来计算该数。Colburn 方程的一般形式为：

Nu=aRebPrc.

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients for Martin correlation in liquid zone** — 液相区中的 Martin 方程系数 `[.122, .374, .333]`（默认） | three-element vector

包含系数 *c1*、*c2* 和 *c3* 的三元素向量，模块使用这些系数在液相区中通过 Martin 关联式计算 Nusselt 数：

Nu=c1(fDarcyRe2sin2β)c2Prc3.

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow between corrugated plates`。

### **Coefficients for Longo correlation in mixture zone** — 混合区中的 Longo 关联式方程系数 `[1.875, .445, .333]`（默认） | three-element vector

包含 Longo 关联式系数的三元素向量。模块使用 Longo 关联式计算混合区中的 Nusselt 数。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow between corrugated plates`。

### **Coefficients for Martin correlation in vapor zone** — 气相区中的 Martin 方程系数 `[.122, .374, .333]`（默认） | three-element vector

包含系数 *c1*、*c2* 和 *c3* 的三元素向量，模块使用这些系数在气相区中通过 Martin 关联式计算 Nusselt 数：

Nu=c1(fDarcyRe2sin2β)c2Prc3.

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow between corrugated plates`。

### **Fouling factor** — 来自污垢沉积物的热阻 `0.1` `K*m^2/kW`（默认）| 正标量

由于壁面上的污垢层而产生的附加热阻。在实际系统中，污垢沉积物会随时间增长。然而，其增长足够缓慢，因此模块假设仿真期间污垢保持恒定。

### **Initial fluid energy specification** — 两相流体的初始状态 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

用于描述流体初始状态的量。

**Initial fluid energy specification** 参数的值限制了两相流体可用的初始状态。当 **Initial fluid energy specification** 为：

- `Temperature` — 指定为过冷液体或过热蒸气的初始状态。不能指定液-气混合物，因为在液-气混合物区域温度恒定。
- `Vapor quality` — 指定为液-气混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域内液相质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定为液-气混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域内液相质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。模块不限制初始状态。

### **Initial two-phase fluid pressure** — 仿真开始时的流体压力 `0.101325` `MPa`（默认）| 正标量

仿真开始时的流体压力。

### **Initial two-phase fluid temperature** — 仿真开始时的温度 `293.15` `K`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道内的温度。此参数可以是标量或二元素向量。标量值表示通道内的平均初始温度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始温度。模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Temperature`。

### **Initial two-phase fluid vapor quality** — 仿真开始时的蒸气质量分数 `0.5`（默认）| [0,1] 范围内的正标量 | [0,1] 范围内的二元素向量

仿真开始时两相流体通道内的蒸气质量分数。此参数可以是标量或二元素向量。标量值表示通道内的平均初始蒸气干度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始蒸气干度。模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Vapor quality`。

### **Initial two-phase fluid vapor void fraction** — 仿真开始时的蒸气体积分数 `0.5`（默认）| [0,1] 范围内的正标量 | [0,1] 范围内的二元素向量

仿真开始时两相流体通道内的蒸气体积分数。此参数可以是标量或二元素向量。标量值表示通道内的平均初始空隙率。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始空隙率。模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Vapor void fraction`。

### **Initial two-phase fluid specific enthalpy** — 仿真开始时的单位质量焓 `1500` `kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道内的单位质量焓。此参数可以是标量或二元素向量。标量值表示通道内的平均初始比焓。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始比焓。模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。

### **Initial two-phase fluid specific internal energy** — 仿真开始时的内能 `1500` `kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道内的单位质量内能。此参数可以是标量或二元素向量。标量值表示通道内的平均初始比内能。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始比内能。模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Specific internal energy`。

## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Thermal Liquid

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a: 对换热器板的热质量建模

选择 **Plate thermal dynamics** 以对换热器板的热质量建模。

## 描述

两相流体与热液体网络之间的板式几何冷凝器蒸发器

Plate Condenser Evaporator (TL-2P) 模块对热液体和两相流体网络之间的板式换热器进行建模。该模块基于 effectiveness-NTU 方法对热液体与两相流体之间的传热进行建模。传热可以在两种流体之间沿任一方向发生。

该模块使用 Effectiveness-NTU (E-NTU) 方法对通过共享板壁的传热进行建模。您还可以通过选择 **Enable plate thermal resistance** 参数来考虑通过板本身的传热。该模块对换热器壁上的污垢进行建模，这会增加热阻并减少两种流体之间的热交换。

两相流体流动使用边界跟随模型来跟踪三个区域中的过冷液体、液-气混合物和过热蒸气。区域在系统中所占的相对空间量称为 *区域分数*。

### 板式换热器几何结构

板式换热器由一系列夹紧在一起的板组成。每块板都有用于流体流过的端口孔，以及围绕端口孔和板侧的垫圈以容纳液体。垫圈图案在板之间交替，使得在板的每一侧，一种流体横穿板流动，而另一种流体穿过端口孔流动。这种设计导致冷热流体交替分层。此图显示了板式换热器中的一段逆流。

此图显示了单块板以及两块相邻板的横截面。在单块板图像中，粗线表示垫圈，虚线表示板波纹。该模块假设板之间的流动通道间隙等于波纹深度 *b*。

在此板上，一种流体从右上端口孔横穿板流到右下端口孔。另一种流体流过左侧两个端口孔上的垫圈，并且不接触此侧的板。板波纹图案增加了结构刚度、表面积和湍流。

因为流体沿每块板的两侧流动，所以总流体体积为

Vtotal=(Np+1)bLpWp,

其中：

- *Np* 是 **Number of plates** 参数的值。
- *Lp* 是 **Plate length** 参数的值。
- *Wp* 是 **Plate width** 参数的值。
- *b* 是 **Spacing between plates** 参数的值。

每种流体的体积是总体积的一半。每种流体的流动横截面积 *S* 为

S=(Np+1)2bWp.

假设无波纹，板的总投影表面积为

Atotal,proj=2NpLpWp.

每种流体具有总传热表面积的一半

ATL=A2P=Atotal,actual2=ϕNpLpWp,

其中面积增大因子 *ϕ* 考虑了由于波纹而增加的表面积

ϕ=Atotal,actualAtotal,proj=1+1+(πbλ)2+41+(πb2λ)26.

每种流体的水力直径为

Dh=2bϕ(Np+1Np).

### Effectiveness-NTU 传热

该模块分三部分计算传热速率，以对应换热器两相流体侧出现的三个流体区域。

区域内的对流传热为

Qzone=ϵCMin(TIn,2P−TIn,TL),

其中：

- *CMin* 是该区域内两种流体热容率中的较小者。热容率是流体比热 *cp* 与流体质量流量的乘积。*CMin* 始终为正。
- *TIn,2P* 是两相流体的区域入口温度。
- *TIn,TL* 是热液体的区域入口温度。
- *ε* 是换热器效能。

效能是热容率和传热单元数 *NTU* 的函数，并且根据换热器流动布置而变化。*NTU* 为

NTU=zCMinR,

其中：

- *z* 是单个区域分数。
- *R* 是由于对流、传导以及板上的任何污垢而在两股流之间的总热阻：

  R=1U2PA2P+F2PA2P+RW+FTLATL+1UTLATL,

  其中：

  - *U* 是相应流体的对流传热系数。
  - *F* 是两相流体侧或热液体侧的 **Fouling factor** 参数的值。
  - *RW* 是通过板的热阻。如果选择 **Enable plate thermal resistance**，则 RW=tNpLpWpkp，其中 *t* 是 **Plate thickness** 参数的值，*kp* 是 **Plate thermal conductivity** 参数的值。

    如果清除 **Enable plate thermal resistance** 复选框，则 *RW = 0*。

流体之间的总对流传热速率是三个区域中传递的热量之和：过冷液体 *QL*、液-气混合物 *QM* 和过热蒸气 *QV*，

Q=∑QZ=QL+QM+QV.

该模块在传热计算中使用的流体属性是入口处值与流体体积内值的平均值。

**按流动布置的效能**

换热器效能根据流动配置和流体阶段而变化。对于液-气混合物区域中的所有流动布置，效能为 ε=1−exp(−NTU)。

对于过冷液体和过热蒸气区域，当 **Flow arrangement** 为 `Parallel flow` 时

ϵ=1−exp[−NTU(1+CR)]1+CR.

对于过冷液体和过热蒸气区域，当 **Flow arrangement** 为 `Counter flow` 时

ϵ=1−exp[−NTU(1−CR)]1−CRexp[−NTU(1−CR)].

*C*R 是两种流体的热容率之比

CR=CMinCMax.

### 传导传热

区域内的传导传热为

Qcond=Tout,TL−Tout,2PRcond,

其中：

- *Tout,2P* 是两相流体的区域出口温度。
- *Tout,TL* 是热液体的区域出口温度。
- *Rcond* 是两股流之间的总传导热阻，

  Rcond=Dhk2PAW,2P+F2PAW,2P+RW+FTLAW,TL+DhkTLAW,TL,

  其中：

  - *AW* 是壁表面积。
  - *k* 是每种流体的热导率。
  - *DH* 是水力直径。

总传热是对流传热与传导传热之和。与对流传热相比，传导传热可以忽略不计。当流量为零时，对流传热也为零。然而，由于来自对流和传导的传热彼此独立运行，即使对流传热为零，仍然存在传导传热。

### 压力损失

对于两种流体和压力损失参数化，每个端口与内部节点之间的压力损失为

pA−pI=ξportsm˙A|m˙A|4ρSport,A2+fDarcyLpm˙A|m˙A|4ρDhS2pB−pI=ξportsm˙B|m˙B|4ρSport,B2+fDarcyLpm˙B|m˙B|4ρDhS2

其中：

- *ṁA* 是当模块分别为热液体网络和两相网络计算值时，通过端口 **A1** 或 **A2** 的质量流量。
- *ṁB* 是当模块分别为热液体网络和两相网络计算值时，通过端口 **A1** 或 **A2** 的质量流量。
- *ρ* 是流体密度。
- *ξports* 是 **Loss coefficient for inlet and outlet manifolds and ports** 参数的值。
- *Sport,A* 是当模块分别为热液体网络和两相网络计算值时，**Cross-sectional area at port A1** 或 **Cross-sectional area at port A2** 参数的值。
- *Sport,B* 是当模块分别为热液体网络和两相网络计算值时，**Cross-sectional area at port B1** 或 **Cross-sectional area at port B2** 参数的值。

当 **Pressure loss model** 参数为 `Friction factor` 时，您使用 **Darcy friction factor for flow between corrugated plates** 参数为流体指定单个恒定摩擦因子。*fDarcy* 是 **Darcy friction factor for flow between corrugated plates** 参数的值。

当 **Pressure loss model** 参数为 `Correlation for flow between corrugated plates` 时，该模块根据板几何数据和参考文献 [3] 中的 Reynolds 数计算 Darcy 摩擦因子。

Reynolds 数为 Re=m˙DhμS，其中 *μ* 是动力粘度。当 Reynolds 数在 200 与 1000 之间时，

fDarcy=[cosβ0.18tanβ+0.36sinβ+64Recosβ+1−cosβ3.8(597Re+3.85)]−2.

当 Reynolds 数大于 2000 时，

fDarcy=[cosβ0.18tanβ+0.36sinβ+1(1.8lnRe−1.5)2cosβ+1−cosβ3.8∗39Re0.289]−2.

该模块在这些区域之间以及 Reynolds 数在 1000 与 2000 之间时使用平滑三次过渡。对于低于 200 的 Reynolds 数，该模块根据层流摩擦常数计算 *fDarcy*，以确保流量趋近于 0 时的数值稳健性。

### 传热系数

传热系数 *U* 为

U=NukDh.

传热计算取决于 **Heat transfer coefficient model** 参数的值以及两相流体区。当热液体和两相流体处于过冷液体或过热蒸汽区时，*k* 为流体导热系数。当两相流体处于饱和液-汽混合物区时，*k* 为饱和液体导热系数。

**Colburn 方程**

当 **Heat transfer coefficient model** 为 `Colburn equation` 时，该模块使用 Colburn 关联式系数根据数据计算传热系数。

当热液体和两相流体处于过冷液体或过热蒸汽区时，努塞尔数为

Nu=aRebPrc,

其中 *a*、*b* 和 *c* 是 **Coefficients [a, b, c] for a\*Re^b\*Pr^c** 参数中的第一、第二和第三个元素，*Pr* 是普朗特数。

当两相流体处于饱和液-汽混合物区时，来自 [2] 的努塞尔数为

Nu=aϕReSLbPrSLc{[(vSVvSL-1)xout+1]1+b-[(vSVvSL-1)xin+1]1+b}(1+b)(vSVvSL-1)(xout-xin),

其中：

- *ReSL* 和 *PrSL* 分别是饱和液体的雷诺数和普朗特数。
- *vSL* 和 *vSV* 分别是饱和液体和蒸汽的比容。
- *xin* 是饱和液-汽混合物区起点处的蒸汽干度。
- *xout* 是饱和液-汽混合物区终点处的蒸汽干度。

**波纹板间流动关联式**

当 **Heat transfer coefficient model** 为 `Correlation for flow between corrugated plates` 时，该模块基于板几何数据计算传热系数。

当热液体和两相流体处于过冷液体或过热蒸汽区时，来自 [3] 的努塞尔数为

Nu=c1(fDarcyRe2sin2β)c2Prc3,

其中：

- *c1*、*c2* 和 *c3* 是 **Coefficients for Martin correlation** 参数中的第一、第二和第三个元素。
- *Pr* 是普朗特数。

当两相流体处于饱和液-汽混合物区时，来自 [2] 的努塞尔数为

Nu=c1ϕReSLc2PrSLc3{[(vSVvSL-1)xout+1]1+c2-[(vSVvSL-1)xin+1]1+c2}(1+c2)(vSVvSL-1)(xout-xin).

### 板热质量

如果选择 **Enable plate thermal mass**，该模块会建模换热器板热质量，这会在板对温度或热通量变化的瞬态响应中引入延迟。如果建模热质量，板会在其边界内存储热量。这种热量存储会减缓稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。滞后会持续到来自两侧的热流率达到平衡为止。

如果选择 **Enable plate thermal mass**，壁面能量守恒为

(Mplatecp,plate2)dTplateTLdt=−QTL−Q(Mplatecp,plate2)dTplate2Pdt=−Q2P+Q

其中：

- *Mplate* 是板的质量，该模块根据板几何参数和 **Plate density** 参数计算该值。
- *cp,plate* 是 **Plate specific heat** 参数的值。
- *Tplate* 是有效板温。该模块使用此值来建模瞬态响应。你无法测量该值。

对每种流体的传热为

QTL=CTL(TplateTL−TinTL)(1−e−NTUTL)Q2P=C2P(Tplate2P−Tin2P)(1−e−NTU2P)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容量流率。

每一侧流体与板之间的传热单元数为

NTUTL=UTLATLCTLNTU2P=U2PA2PC2P

其中 *A* 是板总表面积，*U* 是传热系数。

### 守恒方程

**两相流体**

两相流体中的总质量累积速率为

dM2Pdt=m˙A2+m˙B2,

其中：

- *M2P* 是两相流体的总质量。
- m˙A2 是端口 **A2** 处流体的质量流量。
- m˙B2 是端口 **B2** 处流体的质量流量。

该模块使用以下方程将比内能变化与流体传热相关联

M2Pdu2Pdt+u2P(m˙A2+m˙B2)=ϕA2+ϕB2+Q,

其中：

- *u2P* 是两相流体比内能。
- *φA1* 是端口 **A1** 处的能量流率。
- *φB1* 是端口 **B1** 处的能量流率。
- *Q* 是传热速率。

**热液体**

热液体中的总质量累积速率为

dMTLdt=m˙A1+m˙B1.

能量守恒方程为

MTLduTLdt+uTL(m˙A1+m˙B1)=ϕA1+ϕB1−Q,

其中：

- *ϕA1* 是端口 **A1** 处的能量流率。
- *ϕB1* 是端口 **B1** 处的能量流率。

传入或传出热液体的热量 *Q* 等于传出或传入两相流体的热量。
