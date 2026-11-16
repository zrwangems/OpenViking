---
type: simulink-block
title: 'Variable-Displacement Pump (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Pumps and Motors'
documentation_page: 'variabledisplacementpumpil'
documentation_source_path: 'ref/variabledisplacementpumpil.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable-Displacement Pump (IL)

## 端口

### 守恒

### **A** — 液体端口 等温液体

泵的液体入口或出口端口。

### **B** — 液体端口 等温液体

泵的液体入口或出口端口。

### **R** — 机械端口 机械旋转

旋转轴的角速度和扭矩。

### **C** — 机械端口 机械旋转

泵壳参考角速度和扭矩。

### 输入

### **D** — 容积排量，cm^3/rad 物理信号

泵的容积排量，单位为 m^3/rad，指定为物理信号。

### **EV** — 容积效率 物理信号

用于流体排量的泵效率，指定为物理信号。该值必须在 0 和 1 之间。

#### 依赖项

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率 物理信号

用于机械功率传递的泵效率，指定为物理信号。该值必须在 0 和 1 之间。

#### 依赖项

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 泄漏流量，m^3/s 物理信号

泵的容积损失，单位为 m^3/s，指定为物理信号。

#### 依赖项

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 摩擦力矩，N\*m 物理信号

泵的机械损失，单位为 N\*m，指定为物理信号。

#### 依赖项

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical losses`。

## 参数

### **泄漏和摩擦参数化** — 计算泄漏流量和摩擦力矩的方法 `Analytical`（默认） | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

泵的泄漏和摩擦特性的参数化。

- 在 `Analytical` 参数化中，泄漏流量和摩擦力矩通过解析方程计算。
- 在 `Tabulated data - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率根据用户提供的 **压力增益向量，dp**、**轴角速度向量，w** 和 **排量向量，D** 参数计算，并根据三维相关 **容积效率表，e\_v(dp,w,D)** 和 **机械效率表，e\_m(dp,w,D)** 表进行插值。
- 在 `Tabulated data - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩根据用户提供的 **压力增益向量，dp**；**轴角速度向量，w**；和 **排量向量，D** 参数计算，并根据三维相关 **容积损失表，q\_loss(dp,w,D)** 和 **机械损失表，torque\_loss(dp,w,D)** 表进行插值。
- 在 `Input signal - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率分别作为物理信号在端口 **EV** 和 **EM** 接收。
- 在 `Input signal - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩分别作为物理信号在端口 **LV** 和 **LM** 接收。

### **名义排量** — 名义流体排量 `30 cm^3/rev`（默认） | 标量

在名义工况下轴旋转所排出的流体量。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **名义轴角速度** — 轴角速度 `1800 rpm`（默认） | 标量

在名义工况下轴的角速度。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **名义压力增益** — 流体入口和出口之间的压降 `10 MPa`（默认） | 标量

在名义工况下泵在流体入口和出口之间的压力增益。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **名义工况下的容积效率** — 名义工况下实际流量与理想流量之比 `0.92`（默认） | 范围 (0,1] 内的正标量

名义工况下实际流量与理想流量之比。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **空载扭矩** — 基础扭矩 `0 N*m`（默认） | 标量

克服密封摩擦并引起轴运动所需的最小扭矩值。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **名义工况下的机械效率** — 实际机械功率与理想机械功率之比 `0.88`（默认） | 正标量

名义工况下实际机械功率与理想机械功率之比。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **压力增益向量，dp** — 表格数据参数化的压力数据向量 `[.1, 1, 2] MPa`（默认） | 1×*n* 向量

用于泄漏和扭矩摩擦的表格参数化的压力差值向量。此向量与 **轴角速度向量，w** 和 **排量向量，D** 参数构成独立轴，用于三维相关 **容积效率表，e\_v(dp,w,D)** 和 **机械效率表，e\_m(dp,w,D)** 参数。向量元素必须按升序列出。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **轴角速度向量，w** — 表格数据参数化的角速度数据向量 `[250, 500, 1000, 2000, 3000, 4000] rpm`（默认） | 1×*n* 向量

用于泄漏和扭矩摩擦的表格参数化的角速度数据向量。此向量与 **压力增益向量，dp** 和 **排量向量，D** 参数构成独立轴，用于三维相关 **容积效率表，e\_v(dp,w,D)** 和 **机械效率表，e\_m(dp,w,D)** 参数。向量元素必须按升序列出。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **排量向量，D** — 表格数据参数化的排量体积向量 `[-30, -19, 19, 30] cm^3/s`（默认） | 1×*n* 向量

用于泄漏和扭矩摩擦的表格参数化的流体容积排量数据向量。此向量与 **轴角速度向量，w** 和 **压力增益向量，dp** 参数构成独立轴，用于三维相关 **容积效率表，e\_v(dp,w,D)** 和 **机械效率表，e\_m(dp,w,D)** 参数。向量元素必须按升序列出。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **容积效率表，e\_v(dp,w,D)** — 表格数据参数化的容积效率 `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)`（默认） | *M*×*N*×*P* 矩阵

*M*×*N*×*P* 矩阵，表示在指定流体压力增益、轴角速度和容积排量下的容积效率。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **压力增益向量，dp** 参数中的向量元素数。
- *N* 是 **轴角速度向量，w** 参数中的向量元素数。
- *P* 是 **排量向量，D** 参数中的向量元素数。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **机械效率表，e\_m(dp,w,D)** — 表格数据参数化的机械效率 `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)`（默认） | *M*×*N*×*P* 矩阵

*M*×*N*×*P* 矩阵，表示在指定流体压力增益、轴角速度和排量下的机械效率。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **压力增益向量，dp** 参数中的向量元素数。
- *N* 是 **轴角速度向量，w** 参数中的向量元素数。
- *P* 是 **排量向量，D** 参数中的向量元素数。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **容积损失表，q\_loss(dp,w,D)** — 表格数据参数化的容积损失 `repmat([.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3, 1, 1, 4)`m^3/s（默认） | 数值数组

*M*×*N*×*P* 矩阵，表示在指定流体压力增益、轴角速度和排量下的容积泄漏。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **压力增益向量，dp** 参数中的向量元素数。
- *N* 是 **轴角速度向量，w** 参数中的向量元素数。
- *P* 是 **排量向量，D** 参数中的向量元素数。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **机械损失表，torque\_loss(dp,w,D)** — 表格数据参数化的机械损失 `repmat([.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626], 1, 1, 4) N*m`（默认） | 数值数组

*M*×*N*×*P* 矩阵，表示在指定流体压力增益、轴角速度和排量下的摩擦力矩。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **压力增益向量，dp** 参数中的向量元素数。
- *N* 是 **轴角速度向量，w** 参数中的向量元素数。
- *P* 是 **排量向量，D** 参数中的向量元素数。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical loss`。

### **最小容积效率** — 容积效率的最小值 `1e-3`（默认） | 范围 (0,1] 内的正标量

容积效率的最小值。如果输入信号低于此值，则将容积效率设置为最小容积效率。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **最大容积效率** — 容积效率的最大值 `1`（默认） | 范围 (0,1] 内的正标量

容积效率的最大值。如果输入信号高于此值，则将容积效率设置为最大容积效率。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **最小机械效率** — 机械效率的最小值 `1e-3`（默认） | 范围 (0,1] 内的正标量

机械效率的最小值。如果输入信号低于此值，则将机械效率设置为最小机械效率。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **最大机械效率** — 机械效率的最大值 `1`（默认） | 范围 (0,1] 内的正标量

机械效率的最大值。如果输入信号高于此值，则将机械效率设置为最大机械效率。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **泵-马达转换的压力增益阈值** — 模式转换的压力阈值 `1e-3 MPa`（默认） | 正标量

指示泵和马达功能之间转换阈值的泵压力增益。转换区域定义在 0 MPa 附近，位于压力增益阈值的正值和负值之间。在此转换区域内，计算出的泄漏流量和摩擦力矩根据转换项 *α* 进行调整，以确保从一种模式平滑转换到另一种模式。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **泵-马达转换的角速度阈值** — 模式转换的角速度阈值 `100 rpm`（默认） | 正标量

指示马达和泵功能之间转换阈值的轴角速度。转换区域定义在 0 rpm 附近，位于角速度阈值的正值和负值之间。在此转换区域内，计算出的泄漏流量和摩擦力矩根据转换项 *α* 进行调整，以确保从一种模式平滑转换到另一种模式。

#### 依赖项

要启用此参数，请将 **泄漏和摩擦参数化** 设置为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical loss`

### **泵-马达转换的排量阈值** — 模式转换的排量阈值 `0.1 cm^3/s`（默认） | 正标量

指示泵和马达功能之间转换阈值的容积排量。转换区域定义在 0 cm^3/s 附近，位于排量阈值的正值和负值之间。在此转换区域内，计算出的泄漏流量和摩擦力矩根据转换项 *α* 进行调整，以确保从一种模式平滑转换到另一种模式。当 **D** 的符号变化时，它也用于转换理想质量流量。

### **Check if operating beyond the range of supplied tabulated data** — 是否通知已超出所提供数据的范围 `None`（默认） | `Warning` | `Error`

是否通知已超出所提供数据的范围。
选择 `Warning` 以在模块使用超出所提供数据范围的值时收到通知。选择
`Error` 以在模块使用超出所提供数据范围的值时停止仿真。

#### 依赖项

要启用此参数，请将 **Leakage and friction
parameterization** 设置为：

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`

### **Check if operating beyond pump mode** — 是否通知该模块在泵模式功能之外运行 `None`（默认） | `Warning` | `Error`

是否通知该模块在泵模式功能之外运行。选择 `Warning` 以在该模块运行于正向或反向电机模式时收到通知。选择
`Error` 以在该模块运行于正向或反向电机模式时停止仿真。

#### 依赖项

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical losses`。

### **Check if pressures are less than pump minimum pressure** — 是否通知流体出口压力过低 `None`（默认） | `Warning` | `Error`

是否通知端口 **A** 和
**B** 处的流体经历低压。选择
`Warning` 以在压力降至指定最小值以下时收到通知。选择
`Error` 以在压力降至指定最小值以下时停止仿真。

此参数有助于识别空化的潜在条件，即流体压力降至流体蒸气压以下时。

### **Pump minimum pressure** — 泵出口可接受压力的下限 `0.101325 MPa`（默认） | positive scalar

泵入口或出口可接受压力的下限。

#### 依赖项

要启用此参数，请将 **Check if pressures are less
than pump minimum pressure** 设置为以下任一项：

- `Warning`
- `Error`

## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2020a 中引入**

### R2024a：检查模块是否在计算数据范围之外运行

**Check if operating beyond the octants of supplied tabulated
data** 参数已重命名为 **Check if operating
beyond the range of supplied tabulated data**。您可以启用
**Check if operating beyond the range of supplied tabulated
data** 参数，以检查模块是否在模块参数指定的数据之外运行，即，在模块已扩展数据的区域中运行。

## 描述

等温液体网络中的可变排量泵

Variable-Displacement Pump (IL) 模块对具有可变容积排量的泵进行建模。流体可以从端口 **A** 流向端口
**B**，称为 *正向模式*，或者从端口
**B** 流向端口 **A**，称为 *反向模式*。当沿流动方向存在压力增益时，发生泵模式运行。当沿流动方向存在压力降时，发生电机模式运行。

轴旋转对应于流过泵的流体容积的符号，该容积在端口 **D** 处作为物理信号接收。**D** 处的正流体排量对应于正向模式下的正轴旋转。**D** 处的负流体排量对应于正向模式下的负轴角速度。

**运行模式**

该模块有八种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压力增益，*Δp =
p*B – *p*A；
角速度，*ω = ω*R –
*ω*C；以及端口 **D** 处的流体容积排量。上图将这些模式映射到
*Δp*-*ω*-*D* 图表的卦限：

- 模式 1，*正向泵*：正轴角速度
  导致从端口 **A** 到端口
  **B** 的压力增加，以及从端口 **A** 到端口
  **B** 的流动。
- 模式 2，*反向电机*：从端口
  **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力
  降低以及负轴角速度。
- 模式 3，*反向泵*：负轴角速度
  导致从端口 **B** 到端口
  **A** 的压力增加，以及从 **B** 到
  **A** 的流动。
- 模式 4，*正向电机*：从端口
  **A** 到 **B** 的流动导致从 **A** 到 **B** 的压力
  降低以及正轴角速度。
- 模式 5，*反向电机*：从端口
  **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力
  降低以及正轴角速度。
- 模式 6，*正向泵*：负轴角速度
  导致从 **A** 到
  **B** 的压力增加，以及从 **A** 到
  **B** 的流动。
- 模式 7，*正向电机*：从端口
  **A** 到 **B** 的流动导致从 **A** 到 **B** 的压力
  降低以及负轴角速度。
- 模式 8，*反向泵*：正轴角速度
  导致从端口 **B** 到端口
  **A** 的压力增加，以及从 **B** 到
  **A** 的流动。

该泵模块具有解析、查找表和物理信号参数化。
使用表格数据或输入信号进行参数化时，您可以选择基于效率或损失来表征泵运行。

阈值参数 **Pressure gain threshold for pump-motor
transition**、**Angular velocity threshold for pump-motor
transition** 和 **Displacement threshold for pump-motor
transition** 确定泵运行模式之间可发生数值平滑流动过渡的区域。对于压力和角速度
阈值，选择一个为过渡项提供一定裕量的过渡区域，但相对于典型泵压力增益和角速度
足够小，以免影响计算结果。对于排量阈值，
选择一个小于正常运行期间典型排量容积的阈值。

### 解析泄漏和摩擦力参数化

如果将 **Leakage and friction parameterization** 设置为
`Analytical`，则该模块根据轴速度、压力增益、
容积排量和容积效率的恒定标称值计算内部泄漏和轴摩擦。泄漏流量与
泵上的压差相关，按下式计算：

m˙leak=KρavgΔp,

其中：

- *Δp* 是 *p*B
  – *p*A。
- *ρ*avg 是平均流体
  密度。
- *K* 是用于
  解析损失的 Hagen-Poiseuille 系数，

  K=Dnomωnom(1−ηv,nom)Δpnom,

  其中：

  - *D*nom 是
    **Nominal displacement**。
  - *ω*nom 是
    **Nominal shaft angular
    velocity**。
  - *η*nom 是
    **Volumetric efficiency at nominal
    conditions**。
  - *Δp*nom 是
    **Nominal pressure gain**。

摩擦扭矩与泵压差相关，按下式计算：

τfr=(τ0+k|ΔpDDnom|)tanh(4ω5×10−5ωnom),

其中：

- *τ*0 是 **No-load
  torque**。
- *k* 是标称排量下的摩擦扭矩与压力增益系数，由 **Mechanical
  efficiency at nominal conditions**，
  *ηm,nom* 确定：

  k=τfr,nom−τ0Δpnom.

  *τfr,nom* 是
  标称条件下的摩擦扭矩：

  τfr,nom=(1−ηm,nomηm,nom)DnomΔpnom.
- *ω* 是相对轴角速度，即 ωR−ωC。

### 表格数据参数化

当使用表格数据表示泵效率或损失时，您可以为一种或
多种泵运行模式提供数据。表格数据的符号决定该模块的
运行状态。当提供的数据少于八种
运行模式时，该模块通过将给定数据扩展到其余卦限，来计算其他模式的补充数据。

**`Tabulated data - volumetric and mechanical
efficiencies` 参数化**

泄漏流量按下式计算：

m˙leak=m˙leak,pump(1+α2)+m˙leak,motor(1−α2),

其中：

- m˙leak,pump=(1−ηυ)m˙ideal
- m˙leak,motor=(ηv−1)m˙

并且 *η*v 是容积效率，
它从用户提供的表格数据中插值得到。过渡
项 *α* 为

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold)tanh(4DDthreshold),

其中：

- *Δp* 是
  *p*B –
  *p*A。
- *Δp*threshold 是
  **Pressure gain threshold for pump-motor
  transition**。
- *ω* 是
  *ω*R –
  *ω*C。
- *ω*threshold 是
  **Angular velocity threshold for pump-motor
  transition**。

摩擦扭矩按下式计算：

τfr=τfr,pump(1+α2)+τfr,motor(1−α2),

其中：

- τfr,pump=(1−ηm)τ
- τfr,motor=(ηm−1)τideal

并且 *η*m 是
机械效率，它从用户提供的表格数据中插值得到。

**`Tabulated data - volumetric and mechanical
losses` 参数化**

泄漏流量按下式计算：

m˙leak=ρavgqloss(Δp,ω,D),

其中 *q*loss 从
**Volumetric loss table, q\_loss(dp,w,D)** 参数插值得到，该参数
基于用户提供的压力增益、轴角速度和
流体容积排量数据。

轴摩擦扭矩按下式计算：

τfr=τloss(Δp,ω,D),

其中 *τ*loss 从
**Mechanical loss table, torque\_loss(dp,w,D)** 参数插值得到，
该参数基于用户提供的压力增益、轴角速度
和流体容积排量数据。

### 输入信号参数化

当您选择 `Input signal - volumetric and mechanical
efficiencies` 时，端口 **EV** 和
**EM** 启用。内部泄漏和轴摩擦的计算方式与
`Tabulated data - volumetric and
mechanical efficiencies` 参数化相同，不同之处在于
*η*v 和
*η*m 分别在端口
**EV** 和 **EM** 处直接接收。

当您选择 `Input signal - volumetric and mechanical
losses` 时，端口 **LV** 和 **LM**
启用。这些端口以正物理信号形式接收泄漏流量和摩擦扭矩。
泄漏流量按下式计算：

m˙leak=ρavgqLVtanh(4Δppthresh),

其中：

- *q*LV 是在端口 **LV** 处
  接收的泄漏流量。
- *p*thresh 是
  **Pressure gain threshold for pump-motor
  transition** 参数。

摩擦扭矩按下式计算：

τfr=τLMtanh(4ωωthresh),

其中

- *τ*LM 是在端口 **LM** 处
  接收的摩擦扭矩。
- *ω*thresh 是
  **Angular velocity threshold for pump-motor
  transition** 参数。

容积效率和机械效率在用户指定的
最小值和最大值之间。任何低于或高于此范围的值
将分别取指定的最小值和最大值。

### 泵运行

泵流量为：

m˙=m˙ideal−m˙leak,

其中 m˙ideal=ρavgD⋅ω。

泵扭矩为：

τ=τideal+τfr,

其中 τideal=D⋅Δp。

泵轴传递的机械功率为：

φmech=τω,

泵液压功率为：

φhyd=Δpm˙ρavg。

若要在模块运行超出所提供的
表格数据时收到通知，您可以将 **Check if operating beyond the range of
supplied tabulated data** 设置为 `Warning`，以
在发生这种情况时收到警告，或设置为 `Error`，以在发生这种情况时停止
仿真。当使用输入信号表示容积损失或机械
损失时，您可以通过
**Check if operating beyond pump mode** 参数，在仿真超出运行模式时收到通知。

您还可以监控泵功能。将 **Check if pressures are less
than pump minimum pressure** 设置为 `Warning`，以
在发生这种情况时收到警告，或设置为 `Error`，以在发生这种情况时停止
仿真。
