---
type: simulink-block
title: 'Plate Heat Exchanger (TL-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'plateheatexchangertltl'
documentation_source_path: 'ref/plateheatexchangertltl.html'
language: zh-CN
chinese_source: worker-translation
---

# Plate Heat Exchanger (TL-TL)

## 端口
```yaml
ports:
- name: A1
  summary: 热液体 1 入口或出口 thermal liquid
  direction: unspecified
- name: B1
  summary: 热液体 1 入口或出口 thermal liquid
  direction: unspecified
- name: A2
  summary: 热液体 2 入口或出口 thermal liquid
  direction: unspecified
- name: B2
  summary: 热液体 2 入口或出口 thermal liquid
  direction: unspecified
```

### 守恒

### **A1** — 热液体 1 入口或出口 thermal liquid

与热液体 1 相关的入口或出口端口。

### **B1** — 热液体 1 入口或出口 thermal liquid

与热液体 1 相关的入口或出口端口。

### **A2** — 热液体 2 入口或出口 thermal liquid

与热液体 2 相关的入口或出口端口。

### **B2** — 热液体 2 入口或出口 thermal liquid

与热液体 2 相关的入口或出口端口。
## 参数
```yaml
parameters:
- name: Flow arrangement
  summary: 流路排列 Counter flow（默认）| Parallel flow
  group: 配置
- name: Number of plates
  summary: 换热器中的板片数量 25（默认）| 正标量
  group: 配置
- name: Plate length
  summary: 板片长度 1 m（默认）| 正标量
  group: 配置
- name: Plate width
  summary: 板片宽度 0.5 m（默认）| 正标量
  group: 配置
- name: Spacing between plates
  summary: 板片间距 5e-3 m（默认）| 正标量
  group: 配置
- name: Corrugation pattern specification
  summary: 指定波纹图案的选项 Surface area enlargement factor（默认）| Chevron geometry
  group: 配置
- name: Surface area enlargement factor
  summary: 考虑板片面积增大的乘数 1.17（默认）| 正标量
  group: 配置
- name: Corrugation chevron angle
  summary: 板片上人字形的角度 60 deg（默认）| 正标量
  group: 配置
- name: Corrugation depth to pitch ratio
  summary: 人字形深度与节距之比 0.28（默认）| 正标量
  group: 配置
- name: Enable plate thermal resistance
  summary: 建模板片热阻的选项 off（默认）| on
  group: 配置
- name: Enable plate thermal mass
  summary: 建模板片热质量的选项 off（默认）| on
  group: 配置
- name: Plate thickness
  summary: 板片厚度 5e-4 m（默认）| 正标量
  group: 配置
- name: Plate density
  summary: 板片密度 7800 kg/m^3（默认）| 正标量
  group: 配置
- name: Plate specific heat
  summary: 板片比热 490 J/(K*kg)（默认）| 正标量
  group: 配置
- name: Plate thermal conductivity
  summary: 通过板片的热导率 15 W/(K*m)（默认）| 正标量
  group: 配置
- name: Cross-sectional area at port A1
  summary: 端口 A1 处的流通面积 0.01 m^2（默认）| 正标量
  group: 配置
- name: Cross-sectional area at port B1
  summary: 端口 B1 处的流通面积 0.01 m^2（默认）| 正标量
  group: 配置
- name: Cross-sectional area at port A2
  summary: 端口 A2 处的流通面积 0.01 m^2（默认）| 正标量
  group: 配置
- name: Cross-sectional area at port B2
  summary: 端口 B2 处的流通面积 0.01 m^2（默认）| 正标量
  group: 配置
- name: Pressure loss model
  summary: 由粘性摩擦引起的压力损失计算方法 Correlation for flow between corrugated plates（默认）| Friction factor
  group: Thermal Liquid 1
- name: Darcy friction factor for flow between corrugated plates
  summary: 恒定 Darcy 摩擦系数 1.7（默认）| 正标量
  group: Thermal Liquid 1
- name: Loss coefficient for inlet and outlet manifolds and ports
  summary: 入口和出口歧管及端口的压力损失系数 1.5（默认）| 正标量
  group: Thermal Liquid 1
- name: Heat transfer coefficient model
  summary: 传热系数计算方法 Correlation for flow between corrugated plates（默认）| Colburn equation
  group: Thermal Liquid 1
- name: Coefficients [a, b, c] for a\*Re^b\*Pr^c
  summary: Colburn 方程系数 [.141, .748, .333]（默认）| 三元素向量
  group: Thermal Liquid 1
- name: Coefficients for Martin correlation
  summary: Martin 关联式系数 [.122, .374, .333]（默认）| 三元素向量
  group: Thermal Liquid 1
- name: Fouling factor
  summary: 来自污垢沉积物的热阻 0.1 K*m^2/kW（默认）| 正标量
  group: Thermal Liquid 1
- name: Initial thermal liquid 1 pressure
  summary: 仿真开始时的热液体压力 0.101325 MPa（默认）| 正标量
  group: Thermal Liquid 1
- name: Initial thermal liquid 1 temperature
  summary: 仿真开始时的热液体温度 293.15 K（默认）| 正标量
  group: Thermal Liquid 1
- name: Pressure loss model
  summary: 由粘性摩擦引起的压力损失计算方法 Correlation for flow between corrugated plates（默认）| Friction factor
  group: Thermal Liquid 2
- name: Darcy friction factor for flow between corrugated plates
  summary: 恒定 Darcy 摩擦系数 1.7（默认）| 正标量
  group: Thermal Liquid 2
- name: Loss coefficient for inlet and outlet manifolds and ports
  summary: 入口和出口歧管及端口的压力损失系数 1.5（默认）| 正标量
  group: Thermal Liquid 2
- name: Heat transfer coefficient model
  summary: 传热系数计算方法 Correlation for flow between corrugated plates（默认）| Colburn equation
  group: Thermal Liquid 2
- name: Coefficients [a, b, c] for a\*Re^b\*Pr^c
  summary: Colburn 方程系数 [.141, .748, .333]（默认）| 三元素向量
  group: Thermal Liquid 2
- name: Coefficients for Martin correlation
  summary: Martin 关联式系数 [.122, .374, .333]（默认）| 三元素向量
  group: Thermal Liquid 2
- name: Fouling factor
  summary: 来自污垢沉积物的热阻 0.1 K*m^2/kW（默认）| 正标量
  group: Thermal Liquid 2
- name: Initial thermal liquid 2 pressure
  summary: 仿真开始时的热液体压力 0.101325 MPa（默认）| 正标量
  group: Thermal Liquid 2
- name: Initial thermal liquid 2 temperature
  summary: 仿真开始时的热液体温度 293.15 K（默认）| 正标量 | 二元素向量
  group: Thermal Liquid 2
```

### 配置

### **Flow arrangement** — 流路排列 `Counter flow`（默认）| `Parallel flow`

换热器内的流路排列。可用的流动布置为：

- `Parallel flow` — 流动方向相同。
- `Counter flow` — 流动彼此平行，方向相反。

  e-NTU 计算基于此参数的值，与仿真期间端口 **A1** 和 **B1** 之间以及端口 **A2** 和 **B2** 之间的实际流动方向无关。

### **Number of plates** — 换热器中的板片数量 `25`（默认）| 正标量

换热器中的板片数量。流体流经每个板片的两侧，包括端板和起始板。

### **Plate length** — 板片长度 `1` `m`（默认）| 正标量

每个板片的长度。该值为板片的长边，也是流体的流动轴。

### **Plate width** — 板片宽度 `0.5` `m`（默认）| 正标量

每个板片的宽度。

### **Spacing between plates** — 板片间距 `5e-3` `m`（默认）| 正标量

每个板片之间的间隙。该参数值通常等于波纹深度。

### **Corrugation pattern specification** — 指定波纹图案的选项 `Surface area enlargement factor`（默认）| `Chevron geometry`

是直接指定表面积增大系数，还是由模块根据指定的人字形几何计算增大系数。

### **Surface area enlargement factor** — 考虑板片面积增大的乘数 `1.17`（默认）| 正标量

考虑因波纹导致板片表面积增大的乘数。如果每个板片完全平坦，则该参数的值为 1。否则，该值为实际总表面积与板片形状二维投影面积之比。

#### 依赖关系

要启用此参数，请将 **Corrugation pattern specification** 设置为 `Surface area enlargement factor`。

### **Corrugation chevron angle** — 板片上人字形的角度 `60` `deg`（默认）| 正标量

每个板片上人字形波纹的角度。该值为下图中的 *β*：

#### 依赖关系

要启用此参数，请将 **Corrugation pattern specification** 设置为 `Chevron geometry`。

### **Corrugation depth to pitch ratio** — 人字形深度与节距之比 `0.28`（默认）| 正标量

人字形波纹深度与波纹节距之比。波纹节距即波纹波长。该参数的值为下图中的 *b/λ*：

#### 依赖关系

要启用此参数，请将 **Corrugation pattern specification** 设置为 `Chevron geometry`。

### **Enable plate thermal resistance** — 建模板片热阻的选项 `off`（默认）| on

建模板片热阻的选项。如果选中此复选框，模块将使用 **Plate thickness** 和 **Plate thermal conductivity** 参数的值来计算通过每个板片的热阻。如果清除此复选框，模块不会建模通过板片的热阻效应。

### **Enable plate thermal mass** — 建模板片热质量的选项 `off`（默认）| `on`

是否建模板片热质量。建模板片热质量会在板片对温度或热流变化的瞬态响应中引入延迟。如果清除 **Enable plate thermal mass**，模块假定板片足够薄，以至于在传热的时间尺度上瞬态响应是瞬时的。

### **Plate thickness** — 板片厚度 `5e-4` `m`（默认）| 正标量

换热器中每个板片的厚度。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal resistance** 或 **Enable plate thermal mass**。

### **Plate density** — 板片密度 `7800 kg/m^3`（默认）| 正标量

板片的密度。模块使用此值来计算板片热质量。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal mass**。

### **Plate specific heat** — 板片比热 `490 J/(K*kg)`（默认）| 正标量

板片的比热。模块使用此值来计算板片热质量。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal mass**。

### **Plate thermal conductivity** — 通过板片的热导率 `15` `W/(K*m)`（默认）| 正标量

每个板片的热导率。

#### 依赖关系

要启用此参数，请选中 **Enable plate thermal resistance**。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液体 1 端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液体 1 端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01` m^2（默认）| 正标量

热液体 2 端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处的流通面积 `0.01` m^2（默认）| 正标量

热液体 2 端口 **B2** 处的流通面积。

### Thermal Liquid 1

### **Pressure loss model** — 由粘性摩擦引起的压力损失计算方法 `Correlation for flow between corrugated plates`（默认）| `Friction factor`

热液体 1 由粘性摩擦引起的压力损失计算方法。设置为：

- `Friction factor` — 模块基于由 **Darcy friction factor for flow between corrugated plates** 参数指定的板片通道间流动的恒定 Darcy 摩擦系数来计算压力损失。
- `Correlation for flow between corrugated plates` — 模块使用适用于带人字形或鱼骨形图案的板式换热器的 Martin 关联式来计算压力损失。

### **Darcy friction factor for flow between corrugated plates** — 恒定 Darcy 摩擦系数 `1.7`（默认）| 正标量

用于计算压力损失的恒定 Darcy 摩擦系数。

如果您有换热器压力损失数据 *Δpdata* 和通过换热器的质量流量 *ṁdata*，则该参数的值为

fdarcy=DhS2Lp[2ρ(Δpdatam˙data2)−ξportsSport]。

如果您没有 *ξports* 的数据，请在此表达式中使用 **Loss coefficient for inlet and outlet manifolds and ports** 参数的默认值。如果您有多个 *Δpdata* 和 *ṁdata* 数据点，请使用最小二乘拟合来求 *fdarcy*。

如果您知道换热器的损失系数值 *ξloss*，则 *fDarcy = ξloss Dh / LP*。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Friction factor`。

### **Loss coefficient for inlet and outlet manifolds and ports** — 入口和出口歧管及端口的压力损失系数 `1.5`（默认）| 正标量

考虑热液体 1 侧入口和出口歧管及端口损失的压力损失系数。

### **Heat transfer coefficient model** — 传热系数计算方法 `Correlation for flow between corrugated plates`（默认）| `Colburn equation`

热液体 1 传热系数的计算方法。可用的设置为：

- `Colburn equation` — 使用此设置通过定义 Colburn 方程的变量 *a*、*b* 和 *c* 来计算传热系数。使用此选项通过估计系数将传热结果拟合到实验数据。
- `Correlation for flow between corrugated plates` — 使用此设置基于板片几何数据和 Martin 关联式计算传热系数。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c** — Colburn 方程系数 `[.141, .748, .333]`（默认）| 三元素向量

包含热液体 1 的 Colburn 方程经验系数的三元素向量。Colburn 方程是用于计算 Nusselt 数的公式。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients for Martin correlation** — Martin 关联式系数 `[.122, .374, .333]`（默认）| 三元素向量

包含模块用于通过 Martin 关联式计算热液体 1 的 Nusselt 数的系数 *c1*、*c2* 和 *c3* 的三元素向量：

Nu=c1(fDarcyRe2sin2β)c2Prc3。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow between corrugated plates`。

### **Fouling factor** — 来自污垢沉积物的热阻 `0.1` `K*m^2/kW`（默认）| 正标量

热液体 1 由于壁面表面上的污垢层而产生的附加热阻。在实际系统中，污垢沉积物会随时间增长。然而，增长足够缓慢，以至于模块假定污垢在仿真期间是恒定的。

### **Initial thermal liquid 1 pressure** — 仿真开始时的热液体压力 `0.101325` `MPa`（默认）| 正标量

仿真开始时热液体 1 的压力。

### **Initial thermal liquid 1 temperature** — 仿真开始时的热液体温度 `293.15` `K`（默认）| 正标量

仿真开始时热液体 1 中的温度。此参数可以是标量或二元素向量。标量值表示流体流动中的平均初始温度。向量值以 [`inlet`，`outlet`] 的形式表示入口和出口处的初始温度。模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。

### Thermal Liquid 2

### **Pressure loss model** — 由粘性摩擦引起的压力损失计算方法 `Correlation for flow between corrugated plates`（默认）| `Friction factor`

热液体 2 由粘性摩擦引起的压力损失计算方法。设置为：

- `Friction factor` — 模块基于由 **Darcy friction factor for flow between corrugated plates** 参数指定的板片通道间流动的恒定 Darcy 摩擦系数来计算压力损失。
- `Correlation for flow between corrugated plates` — 模块使用适用于带人字形或鱼骨形图案的板式换热器的 Martin 关联式来计算压力损失。

### **Darcy friction factor for flow between corrugated plates** — 恒定 Darcy 摩擦系数 `1.7`（默认）| 正标量

用于计算压力损失的恒定 Darcy 摩擦系数。

如果您有换热器压力损失数据 *Δpdata* 和通过换热器的质量流量 *ṁdata*，则该参数的值为

fdarcy=DhS2Lp[2ρ(Δpdatam˙data2)−ξportsSport]。

如果您没有 *ξports* 的数据，请在此表达式中使用 **Loss coefficient for inlet and outlet manifolds and ports** 参数的默认值。如果您有多个 *Δpdata* 和 *ṁdata* 数据点，请使用最小二乘拟合来求 *fdarcy*。

如果您知道换热器的损失系数值 *ξloss*，则 *fDarcy = ξloss Dh / LP*。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Friction factor`。

### **Loss coefficient for inlet and outlet manifolds and ports** — 入口和出口歧管及端口的压力损失系数 `1.5`（默认）| 正标量

考虑热液体 2 侧入口和出口歧管及端口损失的压力损失系数。

### **Heat transfer coefficient model** — 传热系数计算方法 `Correlation for flow between corrugated plates`（默认）| `Colburn equation`

热液体 2 传热系数的计算方法。可用的设置为：

- `Colburn equation` — 使用此设置通过定义 Colburn 方程的变量 *a*、*b* 和 *c* 来计算传热系数。使用此选项通过估计系数将传热结果拟合到实验数据。
- `Correlation for flow between corrugated plates` — 使用此设置基于板片几何数据和 Martin 关联式计算传热系数。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c** — Colburn 方程系数 `[.141, .748, .333]`（默认）| 三元素向量

包含热液体 2 的 Colburn 方程经验系数的三元素向量。Colburn 方程是用于计算 Nusselt 数的公式。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients for Martin correlation** — Martin 关联式系数 `[.122, .374, .333]`（默认）| 三元素向量

包含模块用于通过 Martin 关联式计算热液体 2 的 Nusselt 数的系数 *c1*、*c2* 和 *c3* 的三元素向量：

Nu=c1(fDarcyRe2sin2β)c2Prc3。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow between corrugated plates`。

### **Fouling factor** — 来自污垢沉积物的热阻 `0.1` `K*m^2/kW`（默认）| 正标量

热液体 2 由于壁面表面上的污垢层而产生的附加热阻。在实际系统中，污垢沉积物会随时间增长。然而，增长足够缓慢，以至于模块假定污垢在仿真期间是恒定的。

### **Initial thermal liquid 2 pressure** — 仿真开始时的热液体压力 `0.101325` `MPa`（默认）| 正标量

仿真开始时热液体 2 的压力。

### **Initial thermal liquid 2 temperature** — 仿真开始时的热液体温度 `293.15` `K`（默认）| 正标量 | 二元素向量

仿真开始时热液体 1 中的温度。此参数可以是标量或二元素向量。标量值表示流体流动中的平均初始温度。向量值以 [`inlet`，`outlet`] 的形式表示入口和出口处的初始温度。模块计算两个端口之间的线性梯度。初始流动方向决定入口和出口端口。
## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2025a: 建模换热器板片的热质量

选择 **Plate thermal dynamics** 以建模换热器板片的热质量。

## 描述

两个热液体网络之间的板式换热器几何结构

板式换热器（TL-TL）模块对两个热液体网络之间的板式换热器进行建模。该模块基于效能-NTU 方法对两种热液体之间的传热进行建模。热量可以在两种流体之间沿任一方向传递。

该模块使用效能-NTU（E-NTU）方法对通过共享板壁的传热进行建模。您还可以通过选择 **Enable plate thermal resistance** 参数来考虑通过板本身的传热。该模块对换热器壁面上的污垢进行建模，污垢会增加热阻并减少两种流体之间的热交换。

### 板式换热器几何结构

板式换热器由一系列夹紧在一起的板片组成。每块板片都有用于流体流过的端口孔，以及围绕端口孔和板片侧边的垫圈，用于容纳液体。垫圈图案在板片之间交替，使得在板片的每一侧，一种流体沿板片表面流动，而另一种流体穿过板片流动。这导致热流体和冷流体交替分层。下图显示了板式换热器中逆流的一个截面。

下图显示了单块板片以及两块相邻板片的横截面。在单块板片图像中，粗线代表垫圈，虚线代表板片波纹。该模块假设板片之间的流道间隙等于波纹深度 *b*。

在这块板片上，一种流体从右上端口孔沿板片流向右下端口孔。另一种流体流过左侧两个端口孔上的垫圈，不接触这一侧的板片。板片波纹图案增加了结构刚度、表面积和湍流。

由于流体沿每块板片的两侧流动，总流体体积为

Vtotal=(Np+1)bLpWp，

其中：

- *Np* 是 **Number of plates** 参数的值。
- *Lp* 是 **Plate length** 参数的值。
- *Wp* 是 **Plate width** 参数的值。
- *b* 是 **Spacing between plates** 参数的值。

每种流体的体积为总体积的一半。每种流体的流动横截面积 *S* 为

S=(Np+1)2bWp。

假设没有波纹，板片的总投影表面积为

Atotal,proj=2NpLpWp。

每种流体拥有总传热表面积的一半

ATL1=ATL2=Atotal,actual2=ϕNpLpWp，

其中面积增大系数 *ϕ* 考虑了波纹导致的表面积增加

ϕ=Atotal,actualAtotal,proj=1+1+(πbλ)2+41+(πb2λ)26。

每种流体的水力直径为

Dh=2bϕ(Np+1Np)。

### 效能-NTU 传热

流体之间的对流传热为

Q=ϵCMin(TIn,TL1−TIn,TL2)，

其中：

- *CMin* 是两种流体热容率中的较小者。热容率是流体比热 *cp* 与流体质量流率的乘积。*CMin* 始终为正。
- *TIn,TL1* 是热液体 1 的区域入口温度。
- *TIn,TL2* 是热液体 2 的区域入口温度。
- *ε* 是换热器效能。

效能是热容率和传热单元数 *NTU* 的函数，并根据换热器流动布置而变化。*NTU* 为

NTU=1CMinR，

其中：

- *R* 是两种流体之间由于对流、传导以及板片上任何污垢导致的总热阻：

  R=1UTL1ATL1+FTL1ATL1+RW+FTL2ATL2+1UTL2ATL2，

  其中：

  - *U* 是相应热液体的对流传热系数。
  - *F* 是热液体 1 或 2 侧的 **Fouling factor** 参数值。
  - *RW* 是通过板片的热阻。如果您选择 **Enable plate thermal resistance**，则 RW=tNpLpWpkp，其中 *t* 是 **Plate thickness** 参数的值，*kp* 是 **Plate thermal conductivity** 参数的值。

    如果您清除 **Enable plate thermal resistance** 复选框，则 *RW = 0*。

该模块在传热计算中使用的流体属性是入口值与流体体积内值的平均值。

**按流动布置的效能**

换热器效能根据流动配置而变化。对于所有流动布置，效能为 ε=1−exp(−NTU)。

当 **Flow arrangement** 为 `Parallel flow` 时

ϵ=1−exp[−NTU(1+CR)]1+CR。

当 **Flow arrangement** 为 `Counter flow` 时

ϵ=1−exp[−NTU(1−CR)]1−CRexp[−NTU(1−CR)]。

*C*R 是两种流体热容率之比：

CR=CMinCMax。

### 传导传热

区域内的传导传热为

Qcond=Tout,TL1−Tout,TL2Rcond，

其中：

- *Tout,TL1* 是热液体 1 的区域出口温度。
- *Tout,TL2* 是热液体 2 的区域出口温度。
- *Rcond* 是两种流体之间的总传导热阻，

  Rcond=DhkTL1AW,TL1+FTL1AW,TL1+RW+FTL2AW,TL2+DhkTL2AW,TL2，

  其中：

  - *AW* 是壁面表面积。
  - *k* 是每种流体的热导率。
  - *DH* 是水力直径。

总传热是对流传热与传导传热之和。与对流传热相比，传导传热可以忽略不计。当流率为零时，对流传热也为零。然而，由于对流传热和传导传热彼此独立运行，即使对流传热为零，仍然存在传导传热。

### 压力损失

对于两种流体和压力损失参数化，每个端口与内部节点之间的压力损失为

pA−pI=ξportsm˙A|m˙A|4ρSport,A2+fDarcyLpm˙A|m˙A|4ρDhS2pB−pI=ξportsm˙B|m˙B|4ρSport,B2+fDarcyLpm˙B|m˙B|4ρDhS2

其中：

- *ṁA* 是当模块计算热液体 1 和热液体 2 网络的值时，通过端口 **A1** 或 **A2** 的质量流率。
- *ṁB* 是当模块计算热液体 1 和热液体 2 网络的值时，通过端口 **B1** 或 **B2** 的质量流率。
- *ρ* 是流体密度。
- *ξports* 是 **Loss coefficient for inlet and outlet manifolds and ports** 参数的值。
- *Sport,A* 是当模块计算热液体 1 和热液体 2 网络的值时，**Cross-sectional area at port A1** 或 **Cross-sectional area at port A2** 参数的值。
- *Sport,B* 是当模块计算热液体 1 和热液体 2 网络的值时，**Cross-sectional area at port B1** 或 **Cross-sectional area at port B2** 参数的值。

当 **Pressure loss model** 参数为 `Friction factor` 时，您使用 **Darcy friction factor for flow between corrugated plates** 参数为流体指定单个恒定摩擦因子。*fDarcy* 是 **Darcy friction factor for flow between corrugated plates** 参数的值。

当 **Pressure loss model** 参数为 `Correlation for flow between corrugated plates` 时，该模块根据板片几何数据和雷诺数计算 Darcy 摩擦因子，依据 [3]。

雷诺数为 Re=m˙DhμS，其中 *μ* 是动力黏度。当雷诺数在 200 到 1000 之间时，

fDarcy=[cosβ0.18tanβ+0.36sinβ+64Recosβ+1−cosβ3.8(597Re+3.85)]−2。

当雷诺数大于 2000 时，

fDarcy=[cosβ0.18tanβ+0.36sinβ+1(1.8lnRe−1.5)2cosβ+1−cosβ3.8∗39Re0.289]−2。

该模块在这些区域之间以及雷诺数在 1000 到 2000 之间时使用平滑三次过渡。对于低于 200 的雷诺数，该模块根据层流摩擦常数计算 *fDarcy*，以确保流动趋近于 0 时的数值鲁棒性。

### 传热系数

传热系数 *U* 为

U=NukDh，

其中 *k* 是流体热导率。传热计算取决于 **Heat transfer coefficient model** 参数的值。

**Colburn 方程**

当 **Heat transfer coefficient model** 为 `Colburn equation` 时，该模块使用 Colburn 关联式系数根据数据计算传热系数。

Nusselt 数为

Nu=aRebPrc，

其中 *a*、*b* 和 *c* 是 **Coefficients [a, b, c] for a\*Re^b\*Pr^c** 参数中的第一、第二和第三个元素，*Pr* 是 Prandtl 数。

**波纹板间流动关联式**

当 **Heat transfer coefficient model** 为 `Correlation for flow between corrugated plates` 时，该模块根据板片几何数据计算传热系数。来自 [3] 的 Nusselt 数为

Nu=c1(fDarcyRe2sin2β)c2Prc3，

其中：

- *c1*、*c2* 和 *c3* 是 **Coefficients for Martin correlation** 参数中的第一、第二和第三个元素。
- *Pr* 是 Prandtl 数。

### 板片热质量

如果您选择 **Enable plate thermal mass**，该模块会对换热器板片热质量进行建模，这会引入板片对温度或热通量变化的瞬态响应延迟。如果您对热质量进行建模，板片会在其边界内储存热量。这种热量储存会减缓稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率平衡为止。

如果您选择 **Enable plate thermal mass**，壁面能量守恒为

(Mplatecp,plate2)dTplateTL,1dt=−QTL,1−Q(Mplatecp,plate2)dTplateTL,2dt=−QTL,2+Q

其中：

- *Mplate* 是板片的质量，该模块根据板片几何参数和 **Plate density** 参数计算得到。
- *cp,plate* 是 **Plate specific heat** 参数的值。
- *Tplate* 是有效板片温度。该模块使用此值对瞬态响应进行建模。您无法测量此值。

传递到每种流体的热量为

QTL,1=CTL,1(TplateTL,1−TinTL,1)(1−e−NTUTL,1)QTL,2=CTL,2(TplateTL,2−TinTL,2)(1−e−NTUTL,2)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容率。

每一侧流体与板片之间的传热单元数为

NTUTL,1=UTL,1ATL,1CTL,1NTUTL,2=UTL,2ATL,2CTL,2

其中 *A* 是总板片表面积，*U* 是传热系数。

### 守恒方程

两种热液体的总质量累积率为

dMTL1dt=m˙A1+m˙B1dMTL2dt=m˙A2+m˙B2

其中 m˙i 是通过端口 **i** 的流体质量流率。

能量守恒方程为

MTL1duTL1dt+uTL1(m˙A1+m˙B1)=ϕA1+ϕB1−QMTL2duTL2dt+uTL2(m˙A2+m˙B2)=ϕA2+ϕB2+Q

其中 *ϕi* 是端口 **i** 处的能量流率。

传入或传出一种热液体的热量 *Q* 等于传出或传入另一种热液体的热量。
