---
type: simulink-block
title: 'Plate Condenser Evaporator (TL-2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
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

### **Z** — 液体、混合物和蒸气区分数，无量纲物理信号

物理信号输出端口，用于测量热交换器中的液体、混合物和蒸气区分数。
### 守恒

### **A1** — 热液体入口或出口 热液体

与热液体相关的入口或出口端口。

### **B1** — 热液体入口或出口 热液体

与热液体相关的入口或出口端口。

### **A2** — 两相流体入口或出口 两相流体

与两相流体相关的入口或出口端口。

### **B2** — 两相流体入口或出口 两相流体

与两相流体相关的入口或出口端口。

## 参数

### 配置

### **Flow arrangement** — 流路对齐方式 `Counter flow`（默认）| `Parallel flow`

热交换器中的流路对齐方式。可用的流动布置为：

- `Parallel flow` — 流动方向相同。
- `Counter flow` — 流动彼此平行，方向相反。

### **Number of plates** — 热交换器中的板数 `25`（默认）| 正标量

热交换器中的板数。流体流过每块板的两侧，包括端板和起始板。

### **Plate length** — 板长度 `1` `m`（默认）| 正标量

每块板的长度。该值为板的长边，也是流体的流动轴方向。

### **Plate width** — 板宽度 `0.5` `m`（默认）| 正标量

每块板的宽度。

### **Spacing between plates** — 板间距 `5e-3` `m`（默认）| 正标量

每块板之间的间隙。该参数值通常等于波纹深度。

### **Corrugation pattern specification** — 指定波纹图案的选项 `Surface area enlargement factor`（默认）| `Chevron geometry`

您可以直接指定表面积增大系数，或由模块根据指定的人字形几何结构计算增大系数。

### **Surface area enlargement factor** — 考虑板面积增大的乘数 `1.17`（默认）| 正标量

考虑因波纹导致板表面积增大的乘数。如果每块板完全平坦，则该参数的值为 1。
否则，该值为实际总表面积与板形状二维投影面积之比。

#### 依赖关系

要启用此参数，请将 **Corrugation pattern specification** 设置为 `Surface area enlargement factor`。

### **Corrugation chevron angle** — 板上人字形的角度 `60` `deg`（默认）| 正标量

每块板上人字形波纹的角度。该值为下图中的 *β*：

#### 依赖关系

要启用此参数，请将 **Corrugation pattern specification** 设置为 `Chevron geometry`。

### **Corrugation depth to pitch ratio** — 人字形深度与节距之比 `0.28`（默认）| 正标量

人字形波纹深度与波纹节距之比。波纹节距即波纹波长。该参数的值为下图中的 *b/λ*：

#### 依赖关系

要启用此参数，请将 **Corrugation pattern specification** 设置为 `Chevron geometry`。

### **Enable plate thermal resistance** — 建模板热阻的选项 `off`（默认）| on

建模板热阻的选项。如果选中此复选框，模块将使用 **Plate thickness** 和 **Plate thermal conductivity** 参数的值来计算通过每块板的热阻。如果清除此复选框，模块不会建模通过板的热阻效应。

### **Enable plate thermal mass** — 建模板热质量的选项 `off`（默认）| `on`

是否建模板热质量。建模板热质量会在板对温度或热通量变化的瞬态响应中引入延迟。如果清除 **Enable plate thermal mass**，模块将假定板足够薄，使得在传热时间尺度上瞬态响应是瞬时的。

### **Plate thickness** — 板厚度 `5e-4` `m`（默认）| 正标量

热交换器中每块板的厚度。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal resistance** 或 **Enable plate thermal mass**。

### **Plate density** — 板密度 `7800 kg/m^3`（默认）| 正标量

板的密度。模块使用该值计算板热质量。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal mass**。

### **Plate specific heat** — 板比热 `490 J/(K*kg)`（默认）| 正标量

板的比热。模块使用该值计算板热质量。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal mass**。

### **Plate thermal conductivity** — 通过板的热导率 `15` `W/(K*m)`（默认）| 正标量

每块板的热导率。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal resistance**。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液体端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液体端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01` m^2（默认）| 正标量

两相流体端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处的流通面积 `0.01` m^2（默认）| 正标量

两相流体端口 **B2** 处的流通面积。

### Thermal Liquid 1

### **Pressure loss model** — 由粘性摩擦引起的压力损失计算方法 `Correlation for flow between corrugated plates`（默认）| `Friction factor`

热液体由粘性摩擦引起的压力损失计算方法。设置为：

- `Friction factor` — 模块基于板通道之间流动的恒定 Darcy 摩擦因子计算压力损失，该因子由 **Darcy friction factor for flow between corrugated plates** 参数指定。
- `Correlation for flow between corrugated plates` — 模块使用适用于具有人字形或鱼骨形图案的板式热交换器的 Martin 关联式计算压力损失。

### **Darcy friction factor for flow between corrugated plates** — 恒定 Darcy 摩擦因子 `1.7`（默认）| 正标量

用于计算压力损失的恒定 Darcy 摩擦因子。

如果您有热交换器压力损失数据 *Δpdata* 和通过热交换器的质量流量 *ṁdata*，则该参数的值为

fdarcy=DhS2Lp[2ρ(Δpdatam˙data2)−ξportsSport]。

如果您没有 *ξports* 的数据，请在此表达式中使用 **Loss coefficient for inlet and outlet manifolds and ports** 参数的默认值。如果您有多个 *Δpdata* 和 *ṁdata* 数据点，请使用最小二乘拟合来求 *fdarcy*。

如果您知道热交换器的损失系数值 *ξloss*，则 *fDarcy = ξloss Dh / LP*。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Friction factor`。

### **Loss coefficient for inlet and outlet manifolds and ports** — 入口和出口歧管及端口的压力损失系数 `1.5`（默认）| 正标量

考虑热液体侧入口和出口歧管及端口损失的压力损失系数。

### **Heat transfer coefficient model** — 传热系数计算方法 `Correlation for flow between corrugated plates`（默认）| `Colburn equation`

热流体的传热系数计算方法。可用设置为：

- `Colburn equation` — 使用此设置通过定义 Colburn 方程的变量 *a*、*b* 和 *c* 来计算传热系数。使用此选项可通过估计系数将传热结果拟合到实验数据。
- `Correlation for flow between corrugated plates` — 使用此设置基于板几何数据和 Martin 关联式计算传热系数。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c** — Colburn 方程系数 `[.141, .748, .333]`（默认）| 三元素向量

包含 Colburn 方程经验系数的三元素向量。Colburn 方程是计算 Nusselt 数的公式。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients for Martin correlation** — Martin 关联式系数 `[.122, .374, .333]`（默认）| 三元素向量

包含模块用于通过 Martin 关联式计算 Nusselt 数的系数 *c1*、*c2* 和 *c3* 的三元素向量：

Nu=c1(fDarcyRe2sin2β)c2Prc3。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow between corrugated plates`。

### **Fouling factor** — 污垢沉积引起的热阻 `0.1` `K*m^2/kW`（默认）| 正标量

壁面表面污垢层引起的附加热阻。在实际系统中，污垢沉积会随时间增长。然而，增长足够缓慢，因此模块假定仿真期间污垢是恒定的。

### **Initial thermal liquid pressure** — 仿真开始时的热液体压力 `0.101325` `MPa`（默认）| 正标量

仿真开始时热液体的压力。

### **Initial thermal liquid temperature** — 仿真开始时的热液体温度 `293.15` `K`（默认）| 正标量 | 二元素向量

仿真开始时热液体通道中的温度。该参数可以是标量或二元素向量。标量值表示流体流动中的平均初始温度。向量值表示入口和出口处的初始温度，形式为 [`inlet`，`outlet`]。模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

### Two-Phase Fluid 2

### **Pressure loss model** — 由粘性摩擦引起的压力损失计算方法 `Correlation for flow between corrugated plates`（默认）| `Friction factor`

两相流体由粘性摩擦引起的压力损失计算方法。设置为：

- `Friction factor` — 模块基于板通道之间流动的恒定 Darcy 摩擦因子计算压力损失，该因子由 **Darcy friction factor for flow between corrugated plates** 参数指定。
- `Correlation for flow between corrugated plates` — 模块使用适用于具有人字形或鱼骨形图案的板式热交换器的 Martin 关联式计算压力损失。

### **Darcy friction factor for flow between corrugated plates** — 恒定 Darcy 摩擦因子 `1.7`（默认）| 正标量

用于计算压力损失的恒定 Darcy 摩擦因子。

如果您有热交换器压力损失数据 *Δpdata* 和通过热交换器的质量流量 *ṁdata*，则该参数的值为

fdarcy=DhS2Lp[2ρ(Δpdatam˙data2)−ξportsSport]。

如果您没有 *ξports* 的数据，请在此表达式中使用 **Loss coefficient for inlet and outlet manifolds and ports** 参数的默认值。如果您有多个 *Δpdata* 和 *ṁdata* 数据点，请使用最小二乘拟合来求 *fdarcy*。

如果您知道热交换器的损失系数值 *ξloss*，则 *fDarcy = ξloss Dh / LP*。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Friction factor`。

### **Loss coefficient for inlet and outlet manifolds and ports** — 入口和出口歧管及端口的压力损失系数 `1.5`（默认）| 正标量

考虑热液体侧入口和出口歧管及端口损失的压力损失系数。

### **Heat transfer coefficient model** — 传热系数计算方法 `Correlation for flow between corrugated plates`（默认）| `Colburn equation`

两相流体的传热系数计算方法。可用设置为：

- `Colburn equation` — 使用此设置通过定义 Colburn 方程的变量 *a*、*b* 和 *c* 来计算传热系数。使用此选项可通过估计系数将传热结果拟合到实验数据。
- `Correlation for flow between corrugated plates` — 使用此设置基于板几何数据和 Martin 关联式计算传热系数。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in liquid zone** — 液体区 Colburn 方程系数 `[.141, .748, .333]`（默认）| 三元素向量

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，模块通过在每个区使用 Colburn 方程来计算。Colburn 方程的一般形式为：

Nu=aRebPrc。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone** — 混合物区 Longo 关联式方程系数 `[1.875, .445, .333]`（默认）| 三元素向量

包含 Longo 关联式系数的三元素向量。模块使用 Longo 关联式计算混合物区的 Nusselt 数。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in vapor zone** — 蒸气区 Colburn 方程系数 `[.141, .748, .333]`（默认）| 三元素向量

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，模块通过在每个区使用 Colburn 方程来计算。Colburn 方程的一般形式为：

Nu=aRebPrc。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients for Martin correlation in liquid zone** — 液体区 Martin 方程系数 `[.122, .374, .333]`（默认）| 三元素向量

包含模块用于在液体区通过 Martin 关联式计算 Nusselt 数的系数 *c1*、*c2* 和 *c3* 的三元素向量：

Nu=c1(fDarcyRe2sin2β)c2Prc3。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow between corrugated plates`。

### **Coefficients for Longo correlation in mixture zone** — 混合物区 Longo 关联式方程系数 `[1.875, .445, .333]`（默认）| 三元素向量

包含 Longo 关联式系数的三元素向量。模块使用 Longo 关联式计算混合物区的 Nusselt 数。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow between corrugated plates`。

### **Coefficients for Martin correlation in vapor zone** — 蒸气区 Martin 方程系数 `[.122, .374, .333]`（默认）| 三元素向量

包含模块用于在蒸气区通过 Martin 关联式计算 Nusselt 数的系数 *c1*、*c2* 和 *c3* 的三元素向量：

Nu=c1(fDarcyRe2sin2β)c2Prc3。

#### 依赖关系

要启用此参数，请将**传热系数模型**设置为`波纹板间流动关联式`。

### **污垢系数** — 污垢沉积产生的热阻 `0.1` `K*m^2/kW`（默认）| 正标量

由于壁面表面上的污垢层而产生的附加热阻。在实际系统中，污垢沉积会随时间增长。然而，其增长速度足够缓慢，因此该模块假设在仿真过程中污垢保持恒定。

### **初始流体能量规格** — 两相流体的初始状态 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

用于描述流体初始状态的量。

**初始流体能量规格**参数的值限制了两相流体可用的初始状态。当**初始流体能量规格**为：

- `Temperature` — 指定初始状态为过冷液体或过热蒸汽。不能指定液-汽混合物，因为在液-汽混合物区域温度是恒定的。
- `Vapor quality` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液相质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液相质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。该模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。该模块不限制初始状态。

### **初始两相流体压力** — 仿真开始时的流体压力 `0.101325` `MPa`（默认）| 正标量

仿真开始时流体的压力。

### **初始两相流体温度** — 仿真开始时的温度 `293.15` `K`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道中的温度。此参数可以是标量或二元素向量。标量值表示通道中的平均初始温度。向量值以 [`inlet`，`outlet`] 的形式表示入口和出口处的初始温度。该模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将**初始流体能量规格**设置为`Temperature`。

### **初始两相流体蒸汽干度** — 仿真开始时的蒸汽质量分数 `0.5`（默认）| [0,1] 范围内的正标量 | [0,1] 范围内的二元素向量

仿真开始时两相流体通道中的蒸汽质量分数。此参数可以是标量或二元素向量。标量值表示通道中的平均初始蒸汽干度。向量值以 [`inlet`，`outlet`] 的形式表示入口和出口处的初始蒸汽干度。该模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将**初始流体能量规格**设置为`Vapor quality`。

### **初始两相流体蒸汽空隙率** — 仿真开始时的蒸汽体积分数 `0.5`（默认）| [0,1] 范围内的正标量 | [0,1] 范围内的二元素向量

仿真开始时两相流体通道中的蒸汽体积分数。此参数可以是标量或二元素向量。标量值表示通道中的平均初始空隙率。向量值以 [`inlet`，`outlet`] 的形式表示入口和出口处的初始空隙率。该模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将**初始流体能量规格**设置为`Vapor void fraction`。

### **初始两相流体比焓** — 仿真开始时的单位质量焓 `1500` `kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道中的单位质量焓。此参数可以是标量或二元素向量。标量值表示通道中的平均初始比焓。向量值以 [`inlet`，`outlet`] 的形式表示入口和出口处的初始比焓。该模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将**初始流体能量规格**设置为`Specific enthalpy`。

### **初始两相流体比内能** — 仿真开始时的内能 `1500` `kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道中的单位质量内能。此参数可以是标量或二元素向量。标量值表示通道中的平均初始比内能。向量值以 [`inlet`，`outlet`] 的形式表示入口和出口处的初始比内能。该模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

#### 依赖关系

要启用此参数，请将**初始流体能量规格**设置为`Specific internal energy`。

## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a：对换热器板的热质量建模

选择**板热动力学**以对换热器板的热质量建模。

## 描述

两相流体与热液体网络之间的板式几何冷凝器蒸发器

Plate Condenser Evaporator (TL-2P) 模块对热液体和两相流体网络之间的板式换热器进行建模。该模块基于效能-NTU 方法对热液体和两相流体之间的传热进行建模。传热可以在两种流体之间沿任一方向发生。

该模块使用效能-NTU（E-NTU）方法对通过共享板壁的传热进行建模。您还可以通过选择**启用板热阻**参数来考虑通过板本身的传热。该模块对换热器壁面上的污垢进行建模，污垢会增加热阻并减少两种流体之间的热交换。

两相流体流动使用边界跟随模型来跟踪三个区域中的过冷液体、汽-液混合物和过热蒸汽。一个区域在系统中所占的相对空间量称为*区域分数*。

### 板式换热器几何结构

板式换热器由一系列夹紧在一起的板组成。每块板都有用于流体流过的端口孔，以及围绕端口孔和板侧的垫圈以容纳液体。垫圈图案在板之间交替，使得在板的每一侧，一种流体流过板面，而另一种流体穿过板。这种设计导致热流体和冷流体交替分层。下图显示了板式换热器中逆流的一部分。

下图显示了单块板以及两块相邻板的横截面。在单块板图像中，粗线代表垫圈，虚线代表板波纹。该模块假设板之间的流动通道间隙等于波纹深度 *b*。

在此板上，一种流体从右上端口孔流过板面到右下端口孔。另一种流体流过左侧两个端口孔上的垫圈，不接触此侧的板。板波纹图案增加了结构刚度、表面积和湍流。

由于流体沿每块板的两侧流动，总流体体积为

Vtotal=(Np+1)bLpWp，

其中：

- *Np* 是**板数**参数的值。
- *Lp* 是**板长度**参数的值。
- *Wp* 是**板宽度**参数的值。
- *b* 是**板间距**参数的值。

每种流体的体积是总体积的一半。每种流体的流动横截面积 *S* 为

S=(Np+1)2bWp。

假设无波纹时，板的总投影表面积为

Atotal,proj=2NpLpWp。

每种流体拥有总传热表面积的一半

ATL=A2P=Atotal,actual2=ϕNpLpWp，

其中面积增大系数 *ϕ* 考虑了波纹导致的表面积增加

ϕ=Atotal,actualAtotal,proj=1+1+(πbλ)2+41+(πb2λ)26。

每种流体的水力直径为

Dh=2bϕ(Np+1Np)。

### 效能-NTU 传热

该模块分三部分计算传热速率，以对应于换热器两相流体侧出现的三个流体区域。

区域内的对流传热为

Qzone=ϵCMin(TIn,2P−TIn,TL)，

其中：

- *CMin* 是该区域内两种流体热容率中的较小者。热容率是流体比热 *cp* 与流体质量流率的乘积。*CMin* 始终为正。
- *TIn,2P* 是两相流体的区域入口温度。
- *TIn,TL* 是热液体的区域入口温度。
- *ε* 是换热器效能。

效能是热容率和传热单元数 *NTU* 的函数，并根据换热器流动布置而变化。*NTU* 为

NTU=zCMinR，

其中：

- *z* 是单个区域分数。
- *R* 是由于对流、传导以及板上任何污垢引起的两种流动之间的总热阻：

  R=1U2PA2P+F2PA2P+RW+FTLATL+1UTLATL，

  其中：

  - *U* 是相应流体的对流传热系数。
  - *F* 是两相流体侧或热液体侧的**污垢系数**参数的值。
  - *RW* 是通过板的热阻。如果您选择**启用板热阻**，则 RW=tNpLpWpkp，其中 *t* 是**板厚度**参数的值，*kp* 是**板导热系数**参数的值。

    如果您清除**启用板热阻**复选框，则 *RW = 0*。

流体之间的总对流传热速率是三个区域中传递的热量之和，即过冷液体 *QL*、液-汽混合物 *QM* 和过热蒸汽 *QV*，

Q=∑QZ=QL+QM+QV。

该模块在传热计算中使用的流体属性是入口值与流体体积内值的平均值。

**按流动布置的效能**

换热器效能根据流动配置和流体阶段而变化。在液-汽混合物区域，所有流动布置的效能均为 ε=1−exp(−NTU)。

对于过冷液体和过热蒸汽区域，当**流动布置**为 `Parallel flow` 时

ϵ=1−exp[−NTU(1+CR)]1+CR。

对于过冷液体和过热蒸汽区域，当**流动布置**为 `Counter flow` 时

ϵ=1−exp[−NTU(1−CR)]1−CRexp[−NTU(1−CR)]。

*C*R 是两种流体热容率之比

CR=CMinCMax。

### 传导传热

区域内的传导传热为

Qcond=Tout,TL−Tout,2PRcond，

其中：

- *Tout,2P* 是两相流体的区域出口温度。
- *Tout,TL* 是热液体的区域出口温度。
- *Rcond* 是两种流动之间的总传导热阻，

  Rcond=Dhk2PAW,2P+F2PAW,2P+RW+FTLAW,TL+DhkTLAW,TL，

  其中：

  - *AW* 是壁面表面积。
  - *k* 是每种流体的导热系数。
  - *DH* 是水力直径。

总传热是对流传热与传导传热之和。与对流传热相比，传导传热可以忽略不计。当流率为零时，对流传热也为零。然而，由于对流传热和传导传热彼此独立运行，即使对流传热为零，仍然存在传导传热。

### 压力损失

对于两种流体和压力损失参数化，每个端口与内部节点之间的压力损失为

pA−pI=ξportsm˙A|m˙A|4ρSport,A2+fDarcyLpm˙A|m˙A|4ρDhS2pB−pI=ξportsm˙B|m˙B|4ρSport,B2+fDarcyLpm˙B|m˙B|4ρDhS2

其中：

- *ṁA* 是当该模块计算热液体和两相网络的值时，通过端口 **A1** 或 **A2** 的质量流率。
- *ṁB* 是当该模块计算热液体和两相网络的值时，通过端口 **A1** 或 **A2** 的质量流率。
- *ρ* 是流体密度。
- *ξports* 是**进出口歧管和端口损失系数**参数的值。
- *Sport,A* 是当该模块计算热液体和两相网络的值时，**端口 A1 处横截面积**或**端口 A2 处横截面积**参数的值。
- *Sport,B* 是当该模块计算热液体和两相网络的值时，**端口 B1 处横截面积**或**端口 B2 处横截面积**参数的值。

当**压力损失模型**参数为 `Friction factor` 时，您使用**波纹板间流动的 Darcy 摩擦系数**参数为流体指定单个恒定摩擦系数。*fDarcy* 是**波纹板间流动的 Darcy 摩擦系数**参数的值。

当**压力损失模型**参数为 `Correlation for flow between corrugated plates` 时，该模块根据板几何数据和雷诺数计算 Darcy 摩擦系数，参考文献 [3]。

雷诺数为 Re=m˙DhμS，其中 *μ* 是动力粘度。当雷诺数在 200 到 1000 之间时，

fDarcy=[cosβ0.18tanβ+0.36sinβ+64Recosβ+1−cosβ3.8(597Re+3.85)]−2。

当雷诺数大于 2000 时，

fDarcy=[cosβ0.18tanβ+0.36sinβ+1(1.8lnRe−1.5)2cosβ+1−cosβ3.8∗39Re0.289]−2。

该模块在这些区域之间以及雷诺数在 1000 到 2000 之间时使用平滑三次过渡。对于低于 200 的雷诺数，该模块根据层流摩擦常数计算 *fDarcy*，以确保流动趋近于 0 时的数值鲁棒性。

### Heat Transfer Coefficient

传热系数 *U* 为

U=NukDh。

传热计算取决于 **Heat transfer coefficient model** 参数的值以及两相流体区域。当热液体和两相流体处于过冷液体或过热蒸汽区域时，*k* 为流体导热系数。当两相流体处于饱和液-汽混合物区域时，*k* 为饱和液体导热系数。

**Colburn Equation**

当 **Heat transfer coefficient model** 为 `Colburn equation` 时，模块使用 Colburn 关联式系数根据数据计算传热系数。

当热液体和两相流体处于过冷液体或过热蒸汽区域时，Nusselt 数为

Nu=aRebPrc，

其中 *a*、*b* 和 *c* 分别是 **Coefficients [a, b, c] for a\*Re^b\*Pr^c** 参数中的第一个、第二个和第三个元素，*Pr* 为 Prandtl 数。

当两相流体处于饱和液-汽混合物区域时，来自 [2] 的 Nusselt 数为

Nu=aϕReSLbPrSLc{[(vSVvSL-1)xout+1]1+b-[(vSVvSL-1)xin+1]1+b}(1+b)(vSVvSL-1)(xout-xin)，

其中：

- *ReSL* 和 *PrSL* 分别是饱和液体的 Reynolds 数和 Prandtl 数。
- *vSL* 和 *vSV* 分别是饱和液体和蒸汽的比体积。
- *xin* 是饱和液-汽混合物区域开始处的蒸汽干度。
- *xout* 是饱和液-汽混合物区域结束处的蒸汽干度。

**Correlation for Flow Between Corrugated Plates**

当 **Heat transfer coefficient model** 为 `Correlation for flow between corrugated plates` 时，模块基于板几何数据计算传热系数。

当热液体和两相流体处于过冷液体或过热蒸汽区域时，来自 [3] 的 Nusselt 数为

Nu=c1(fDarcyRe2sin2β)c2Prc3，

其中：

- *c1*、*c2* 和 *c3* 分别是 **Coefficients for Martin correlation** 参数中的第一个、第二个和第三个元素。
- *Pr* 为 Prandtl 数。

当两相流体处于饱和液-汽混合物区域时，来自 [2] 的 Nusselt 数为

Nu=c1ϕReSLc2PrSLc3{[(vSVvSL-1)xout+1]1+c2-[(vSVvSL-1)xin+1]1+c2}(1+c2)(vSVvSL-1)(xout-xin)。

### Plate Thermal Mass

如果选择 **Enable plate thermal mass**，模块会对换热器板热质量建模，这会引入板对温度或热通量变化的瞬态响应延迟。如果对热质量建模，板会在其边界内储存热量。这种热量储存会减缓稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率平衡为止。

如果选择 **Enable plate thermal mass**，壁面能量守恒为

(Mplatecp,plate2)dTplateTLdt=−QTL−Q(Mplatecp,plate2)dTplate2Pdt=−Q2P+Q

其中：

- *Mplate* 是板的质量，模块根据板几何参数和 **Plate density** 参数计算该值。
- *cp,plate* 是 **Plate specific heat** 参数的值。
- *Tplate* 是有效板温度。模块使用该值对瞬态响应建模。该值无法测量。

传递到每种流体的热量为

QTL=CTL(TplateTL−TinTL)(1−e−NTUTL)Q2P=C2P(Tplate2P−Tin2P)(1−e−NTU2P)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容率。

每一侧流体与板之间的传热单元数为

NTUTL=UTLATLCTLNTU2P=U2PA2PC2P

其中 *A* 是板的总表面积，*U* 是传热系数。

### Conservation Equations

**Two-Phase Fluid**

两相流体中的总质量累积率为

dM2Pdt=m˙A2+m˙B2，

其中：

- *M2P* 是两相流体的总质量。
- m˙A2 是端口 **A2** 处流体的质量流量。
- m˙B2 是端口 **B2** 处流体的质量流量。

模块使用以下方程将比内能变化与流体传热关联起来

M2Pdu2Pdt+u2P(m˙A2+m˙B2)=ϕA2+ϕB2+Q，

其中：

- *u2P* 是两相流体比内能。
- *φA1* 是端口 **A1** 处的能量流率。
- *φB1* 是端口 **B1** 处的能量流率。
- *Q* 是传热率。

**Thermal Liquid**

热液体中的总质量累积率为

dMTLdt=m˙A1+m˙B1。

能量守恒方程为

MTLduTLdt+uTL(m˙A1+m˙B1)=ϕA1+ϕB1−Q，

其中：

- *ϕA1* 是端口 **A1** 处的能量流率。
- *ϕB1* 是端口 **B1** 处的能量流率。

传入或传出热液体的热量 *Q* 等于传出或传入两相流体的热量。
