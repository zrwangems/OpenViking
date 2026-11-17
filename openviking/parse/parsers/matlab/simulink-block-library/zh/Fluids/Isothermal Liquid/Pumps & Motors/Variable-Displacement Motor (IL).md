---
type: simulink-block
title: 'Variable-Displacement Motor (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'variabledisplacementmotoril'
documentation_source_path: 'ref/variabledisplacementmotoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable-Displacement Motor (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

电机的液体入口或出口端口。

### **B** — 液体端口，等温液体

电机的液体入口或出口端口。

### **R** — 机械端口，机械旋转

旋转轴的角速度和扭矩。

### **C** — 机械端口，机械旋转

电机壳体的参考角速度和扭矩。
### 输入

### **D** — 容积排量，cm^3/rad，物理信号

电机的容积排量，单位为 m^3/rad，指定为物理信号。

### **EV** — 容积效率，物理信号

用于流体排量的电机效率，指定为物理信号。该值必须在 0 到 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率，物理信号

用于机械能量提取的电机效率，指定为物理信号。该值必须在 0 到 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 泄漏流量，m^3/s，物理信号

电机的容积损失，单位为 m^3/s，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 摩擦力矩，N\*m，物理信号

电机的机械损失，单位为 N\*m，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

## 参数

### **Leakage and friction parameterization** — 泄漏流量和摩擦力矩的计算方法 `Analytical`（默认）| `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

电机泄漏和摩擦特性的参数化方法。

- 在 `Analytical` 参数化中，泄漏流量和摩擦力矩通过解析方程计算。
- 在 `Tabulated data - volumetric and mechanical efficiencies` 参数化中，泄漏流量和摩擦力矩根据用户提供的 **Pressure drop vector, dp**、**Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数计算，并从三维因变量 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 表中插值得到。
- 在 `Tabulated data - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩根据用户提供的 **Pressure drop vector, dp**、**Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数计算，并从三维因变量 **Volumetric loss table, q\_loss(dp,w,D)** 和 **Mechanical loss table, torque\_loss(dp,w,D)** 表中插值得到。
- 在 `Input signal - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率分别作为物理信号在端口 **EV** 和 **EM** 处接收。
- 在 `Input signal - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩分别作为物理信号在端口 **LV** 和 **LM** 处接收。

### **Nominal displacement** — 固定容积流体排量 `30 cm^3/rev`（默认）| 标量

在额定工况下轴旋转所排出的流体量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal shaft angular velocity** — 轴角速度 `1800 rpm`（默认）| 标量

在额定工况下轴的角速度。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal pressure drop** — 流体入口和出口之间的压降 `10 MPa`（默认）| 标量

在额定工况下电机流体入口和出口之间的压降。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Volumetric efficiency at nominal conditions** — 额定工况下实际流量与理想流量之比 `0.92`（默认）| (0,1] 范围内的正标量

额定工况下实际流量与理想流量之比。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **No-load torque** — 基线扭矩 `0 N*m`（默认）| 标量

克服密封摩擦并引起轴运动所需的最小扭矩值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Mechanical efficiency at nominal conditions** — 实际机械功率与理想机械功率之比 `0.88`（默认）| 正标量

额定工况下实际机械功率与理想机械功率之比。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Pressure drop vector, dp** — 表格数据参数化的压力数据向量 `[.1, 1, 2] MPa`（默认）| 1×*n* 向量

用于泄漏和摩擦力矩表格参数化的压差值向量。该向量与 **Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数一起构成独立轴，用于三维因变量 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **Shaft angular velocity vector, w** — 表格数据参数化的角速度数据向量 `[250, 500, 1000, 2000, 3000, 4000] rpm`（默认）| 1×*n* 向量

用于泄漏和摩擦力矩表格参数化的角速度数据向量。该向量与 **Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数一起构成独立轴，用于三维因变量 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **Displacement vector, D** — 表格数据参数化的排量体积向量 `[-30, -19, 19, 30] cm^3/s`（默认）| 1×*n* 向量

用于泄漏和摩擦力矩表格参数化的容积排量数据向量。该向量与 **Shaft angular velocity vector, w** 和 **Pressure drop vector, dp** 参数一起构成独立轴，用于三维因变量 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **Volumetric efficiency table, e\_v(dp,w,D)** — 表格数据参数化的容积效率 `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)`（默认）| *M*×*N*×*P* 矩阵

在指定流体压降、轴角速度和容积排量下的容积效率 *M*×*N*×*P* 矩阵。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。
- *P* 是 **Displacement vector, D** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w,D)** — 表格数据参数化的机械效率 `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)`（默认）| *M*×*N*×*P* 矩阵

在指定流体压降、轴角速度和排量下的机械效率 *M*×*N*×*P* 矩阵。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。
- *P* 是 **Displacement vector, D** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Volumetric loss table, q\_loss(dp,w,D)** — 表格数据参数化的容积损失 `repmat([.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3, 1, 1, 4)`（默认）| *M*×*N*×*P* 矩阵

在指定流体压降、轴角速度和排量下的容积泄漏 *M*×*N*×*P* 矩阵。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。
- *P* 是 **Displacement vector, D** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Mechanical loss table, torque\_loss(dp,w,D)** — 表格数据参数化的机械损失 `repmat([.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626], 1, 1, 4) N*m`（默认）| *M*×*N*×*P* 矩阵

在指定流体压降和轴角速度下的机械损失 *M*×*N*×*P* 矩阵。表元素之间采用线性插值。*M*、*N* 和 *P* 是相关向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。
- *P* 是 **Displacement vector, D** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Minimum volumetric efficiency** — 容积效率的最小值 `1e-3`（默认）| (0,1] 范围内的正标量

容积效率的最小值。如果输入信号低于此值，则容积效率设置为最小容积效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum volumetric efficiency** — 容积效率的最大值 `1`（默认）| (0,1] 范围内的正标量

容积效率的最大值。如果输入信号高于此值，则容积效率设置为最大容积效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Minimum mechanical efficiency** — 机械效率的最小值 `1e-3`（默认）| (0,1] 范围内的正标量

机械效率的最小值。如果输入信号低于此值，则机械效率设置为最小机械效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum mechanical efficiency** — 机械效率的最大值 `1`（默认）| (0,1] 范围内的正标量

机械效率的最大值。如果输入信号高于此值，则机械效率设置为最大机械效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Pressure drop threshold for motor-pump transition** — 模式转换的压力阈值 `1e-3 MPa`（默认）| 正标量

指示电机和泵功能之间转换阈值的电机压降。在压降阈值的正值和负值之间围绕 0 MPa 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **Angular velocity threshold for motor-pump transition** — 模式转换的角速度阈值 `100 rpm`（默认）| 正标量

指示电机和泵功能之间转换阈值的轴角速度。在角速度阈值的正值和负值之间围绕 0 rpm 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **Displacement threshold for motor-pump transition** — 模式转换的排量阈值 `0.1 cm^3/s`（默认）| 正标量

指示电机和泵功能之间转换阈值的容积排量。在排量阈值的正值和负值之间围绕 0 cm^3/s 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。当 **D** 的符号变化时，该阈值也用于过渡理想质量流量。

### **检查是否超出所提供的表格数据范围** — 是否在超出所提供数据范围时发出通知 `None`（默认）| `Warning` | `Error`

是否在超出所提供数据范围时发出通知。
选择 `Warning`，当模块使用的值超出所提供的数据范围时发出通知。选择
`Error`，当模块使用的值超出所提供的数据范围时停止仿真。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为：

- `表格数据 - 容积效率和机械效率`
- `表格数据 - 容积损失和机械损失`

### **检查是否超出电机模式运行** — 是否在模块超出电机模式功能运行时发出通知 `None`（默认）| `Warning` | `Error`

是否在模块超出电机模式功能运行时发出通知。选择 `Warning`，当模块在正向或反向泵模式下运行时发出通知。选择
`Error`，当模块在正向或反向泵模式下运行时停止仿真。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `输入信号 - 容积损失和机械损失`。

### **检查压力是否低于电机最低压力** — 是否在流体出口压力过低时发出通知 `None`（默认）| `Warning` | `Error`

是否在端口 **A** 或 **B** 处的流体经历低压时发出通知。选择
`Warning`，当压力降至指定的最低值以下时发出通知。选择
`Error`，当压力降至指定的最低值以下时停止仿真。

当流体压力降至流体蒸气压以下时，该参数有助于识别可能发生气蚀的条件。

### **电机最低压力** — 电机出口可接受压力的下限阈值 `0.101325 MPa`（默认）| 正标量

电机入口或出口可接受压力的下限阈值。

#### 依赖关系

要启用此参数，请将 **检查压力是否低于电机最低压力** 设置为以下任一值：

- `Warning`
- `Error`

## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：检查模块是否在计算数据范围之外运行

**检查是否超出所提供的表格数据的八分仪范围** 参数已重命名为 **检查是否超出所提供的表格数据范围**。您可以启用
**检查是否超出所提供的表格数据范围** 参数来检查模块是否在模块参数所指定的数据之外运行，即在模块已扩展数据的区域内运行。

## 描述

等温液体系统中的可变排量电机

Variable-Displacement Motor (IL) 模块对具有可变容积排量的电机进行建模。流体可以从端口 **A** 流向端口 **B**，称为*正向模式*，或从端口 **B** 流向端口 **A**，称为*反向模式*。当沿流动方向存在压降时，发生电机模式运行。当沿流动方向存在压力增益时，发生泵模式运行。

轴旋转对应于通过电机移动的流体体积的符号，该符号在端口 **D** 处作为物理信号接收。在 **D** 处的正流体排量对应于正向模式下的正轴旋转。在 **D** 处的负流体排量对应于正向模式下的负轴角速度。

**运行模式**

该模块有八种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压降，*Δp = p*A – *p*B；角速度，*ω = ω*R – *ω*C；以及端口 **D** 处的流体容积排量。上图将这些模式映射到 *Δp*-*ω*-*D* 图的八分仪：

- 模式 1，*正向电机*：流体从端口 **A** 流向端口 **B**，导致从 **A** 到 **B** 的压力降低以及正轴角速度。
- 模式 2，*反向泵*：负轴角速度导致从端口 **B** 到端口 **A** 的压力升高以及从 **B** 流向端口 **A** 的流动。
- 模式 3，*反向电机*：流体从端口 **B** 流向端口 **A**，导致从 **B** 到 **A** 的压力降低以及负轴角速度。
- 模式 4，*正向泵*：正轴角速度导致从端口 **A** 到端口 **B** 的压力升高以及从 **A** 流向 **B** 的流动。
- 模式 5，*反向泵*：正轴角速度导致从端口 **B** 到端口 **A** 的压力升高以及从 **B** 流向 **A** 的流动。
- 模式 6，*正向电机*：流体从端口 **A** 流向端口 **B**，导致从 **A** 到 **B** 的压力降低以及正轴角速度。
- 模式 7，*正向泵*：负轴角速度导致从端口 **A** 到端口 **B** 的压力升高以及从 **A** 流向 **B** 的流动。
- 模式 8，*反向电机*：流体从 **B** 流向 **A**，导致从 **B** 到 **A** 的压力降低以及正轴角速度。

电机模块具有解析、查找表和物理信号参数化。当使用表格数据或输入信号进行参数化时，您可以选择基于效率或损失来表征电机运行。

阈值参数 **电机-泵转换的压降阈值**、**电机-泵转换的角速度阈值** 和 **电机-泵转换的排量阈值** 用于识别可在电机运行模式之间进行数值平滑流动过渡的区域。对于压力和角速度阈值，请选择一个为过渡项提供一定裕量的过渡区域，但该区域相对于典型电机压降和角速度足够小，以免影响计算结果。对于排量阈值，请选择一个小于正常运行期间典型排量体积的阈值。

### 解析泄漏和摩擦参数化

如果将 **泄漏和摩擦参数化** 设置为 `Analytical`，模块将根据轴速度、压降、容积排量和扭矩的恒定标称值计算内部泄漏和轴摩擦。泄漏流量与电机上的压差相关，计算如下：

m˙leak=KρavgΔp，

其中：

- *Δp* 为 *p*A – *p*B。
- *ρ*avg 为平均流体密度。
- *K* 为解析损失的 Hagen-Poiseuille 系数，

  K=Dnomωnom(1ηv,nom−1)Δpnom，

  其中：

  - *D*nom 为 **标称排量**。
  - *ω*nom 为 **标称轴角速度**。
  - *η*nom 为 **标称条件下的容积效率**。
  - *Δp*nom 为 **标称压降**。

扭矩与电机压差相关，计算如下：

τfr=(τ0+k|ΔpDDnom|)tanh(4ω5×10−5ωnom)，

其中：

- *τ*0 为 **空载扭矩**。
- *k* 为标称排量下的摩擦扭矩与压力增益系数，由 **标称条件下的机械效率** *ηm,nom* 确定：

  k=τfr,nom−τ0Δpnom。

  *τfr,nom* 为标称条件下的摩擦扭矩：

  τfr,nom=(1−ηm,nom)DnomΔpnom。
- *Δp* 为端口 **A** 和 **B** 之间的压降。
- *ω* 为相对轴角速度，即 ωR−ωC。

### 表格数据参数化

当使用表格数据表示电机效率或损失时，您可以为一种或多种电机运行模式提供数据。表格数据的符号决定模块的运行状态。当提供的运行模式数据少于八种时，模块通过将给定数据扩展到其余八分仪来计算其他模式的补充数据。

**`表格数据 - 容积效率和机械效率` 参数化**

泄漏流量计算如下：

m˙leak=m˙leak,motor(1+α2)+m˙leak,pump(1−α2)，

其中：

- m˙leak,pump=(ηυ−1)m˙ideal
- m˙leak,motor=(1−ηv)m˙

且 *η*v 为容积效率，从用户提供的表格数据中插值得到。过渡项 *α* 为

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold)tanh(4DDthreshold)，

其中：

- *Δp* 为 *p*A – *p*B。
- *Δp*threshold 为 **电机-泵转换的压降阈值**。
- *ω* 为 *ω*R – *ω*C。
- *ω*threshold 为 **电机-泵转换的角速度阈值**。

扭矩计算如下：

τfr=τfr,pump(1+α2)+τfr,motor(1−α2)，

其中：

- τfr,pump=(ηm−1)τ
- τfr,motor=(1−ηm)τideal

且 *η*m 为机械效率，从用户提供的表格数据中插值得到。

**`表格数据 - 容积损失和机械损失` 参数化**

泄漏流量计算如下：

m˙leak=ρavgqloss(Δp,ω,D)，

其中 *q*loss 从 **容积损失表，q\_loss(dp,w,D)** 参数中插值得到，该参数基于用户提供的压降、轴角速度和流体容积排量数据。

轴摩擦扭矩计算如下：

τfr=τloss(Δp,ω,D)，

其中 *τ*loss 从 **机械损失表，torque\_loss(dp,w,D)** 参数中插值得到，该参数基于用户提供的压降、轴角速度和流体容积排量数据。

### 输入信号参数化

当 **泄漏和摩擦参数化** 设置为 `输入信号 - 容积效率和机械效率` 时，端口 **EV** 和 **EM** 启用。内部泄漏和轴摩擦的计算方式与 `表格数据 - 容积效率和机械效率` 参数化相同，不同之处在于 *η*v 和 *η*m 分别直接在端口 **EV** 和 **EM** 处接收。

当 **泄漏和摩擦参数化** 设置为 `输入信号 - 容积损失和机械损失` 时，端口 **LV** 和 **LM** 启用。这些端口接收泄漏流量和摩擦扭矩作为正物理信号。泄漏流量计算如下：

m˙leak=ρavgqLVtanh(4Δppthresh)，

其中：

- *q*LV 为在端口 **LV** 处接收的泄漏流量。
- *p*thresh 为 **电机-泵转换的压降阈值** 参数。

摩擦扭矩计算如下：

τfr=τLMtanh(4ωωthresh)，

其中

- *τ*LM 为在端口 **LM** 处接收的摩擦扭矩。
- *ω*thresh 为 **电机-泵转换的角速度阈值** 参数。

容积效率和机械效率在用户指定的最小值和最大值之间变化。任何低于或高于此范围的值将分别取指定的最小值和最大值。

### 电机运行

电机流量为：

m˙=m˙ideal+m˙leak，

其中 m˙ideal=ρavgD⋅ω。

电机扭矩为：

τ=τideal−τfr，

其中 τideal=D⋅Δp。

电机轴提取的机械功率为：

φmech=τω，

电机液压功率为：

φhyd=Δpm˙ρavg。

若要在模块运行超出所提供的表格数据时收到通知，您可以将 **检查是否超出所提供的表格数据范围** 设置为 `Warning`，在发生此情况时收到警告，或设置为 `Error`，在发生此情况时停止仿真。当使用输入信号表示容积损失或机械损失时，您可以通过 **检查是否超出电机模式运行** 参数在仿真超出运行模式时收到通知。

您还可以监控电机功能。将 **检查压力是否低于电机最低压力** 设置为 `Warning`，在发生此情况时收到警告，或设置为 `Error`，在发生此情况时停止仿真。
