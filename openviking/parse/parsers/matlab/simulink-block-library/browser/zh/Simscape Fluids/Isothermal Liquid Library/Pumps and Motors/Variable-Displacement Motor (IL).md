---
type: simulink-block
title: 'Variable-Displacement Motor (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Pumps and Motors'
documentation_page: 'variabledisplacementmotoril'
documentation_source_path: 'ref/variabledisplacementmotoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable-Displacement Motor (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

电机的液体进入或离开端口。

### **B** — 液体端口 isothermal liquid

电机的液体进入或离开端口。

### **R** — 机械端口 mechanical rotational

旋转轴的角速度和扭矩。

### **C** — 机械端口 mechanical rotational

电机壳体的参考角速度和扭矩。
### 输入

### **D** — 体积排量, cm^3/rad physical signal

电机的体积排量，以 m^3/rad 为单位，指定为 physical signal。

### **EV** — 容积效率 physical signal

用于流体排量的电机效率，指定为 physical signal。该值必须在 0 和 1 之间。

#### 依赖项

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率 physical signal

用于机械能量提取的电机效率，指定为 physical signal。该值必须在 0 和 1 之间。

#### 依赖项

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 泄漏流量, m^3/s physical signal

电机的容积损失，以 m^3/s 为单位，指定为 physical signal。

#### 依赖项

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 摩擦力矩, N\*m physical signal

电机的机械损失，以 N\*m 为单位，指定为 physical signal。

#### 依赖项

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

## 参数

### **Leakage and friction parameterization** — 计算泄漏流量和摩擦扭矩的方法 `Analytical` (默认) | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

电机泄漏和摩擦特性的参数化。

- 在 `Analytical` 参数化中，泄漏流量和摩擦扭矩通过解析方程计算。
- 在 `Tabulated data - volumetric and mechanical efficiencies` 参数化中，泄漏流量和摩擦力矩根据用户提供的 **Pressure drop vector, dp**、**Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数计算，并从三维相关 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 表中插值得到。
- 在 `Tabulated data - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩根据用户提供的 **Pressure drop vector, dp**；**Shaft angular velocity vector, w**；和 **Displacement vector, D** 参数计算，并从三维相关 **Volumetric loss table, q\_loss(dp,w,D)** 和 **Mechanical loss table, torque\_loss(dp,w,D)** 表中插值得到。
- 在 `Input signal - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率分别作为 physical signal 在端口 **EV** 和 **EM** 接收。
- 在 `Input signal - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩分别作为 physical signal 在端口 **LV** 和 **LM** 接收。

### **Nominal displacement** — 固定体积流体排量 `30 cm^3/rev` (默认) | scalar

在额定运行条件下，轴旋转所排出的流体量。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal shaft angular velocity** — 轴角速度 `1800 rpm` (默认) | scalar

在额定运行条件下轴的角速度。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal pressure drop** — 流体入口和出口之间的压降 `10 MPa` (默认) | scalar

在额定运行条件下，电机流体入口和出口之间的压降。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Volumetric efficiency at nominal conditions** — 额定条件下实际流量与理想流量之比 `0.92` (默认) | positive scalar in the range of (0,1]

额定条件下实际流量与理想流量之比。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **No-load torque** — 基线扭矩 `0 N*m` (默认) | scalar

克服密封摩擦并引起轴运动所需的最小扭矩值。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Mechanical efficiency at nominal conditions** — 额定条件下实际机械功率与理想机械功率之比 `0.88` (默认) | positive scalar

额定条件下实际机械功率与理想机械功率之比。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Pressure drop vector, dp** — 用于表格数据参数化的压力数据向量 `[.1, 1, 2] MPa` (默认) | 1-by-*n* vector

用于泄漏和摩擦力矩表格参数化的压差值向量。该向量与 **Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数一起，形成三维相关 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数的独立轴。向量元素必须按升序排列。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下任一项：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **Shaft angular velocity vector, w** — 用于表格数据参数化的角速度数据向量 `[250, 500, 1000, 2000, 3000, 4000] rpm` (默认) | 1-by-*n* vector

用于泄漏和摩擦力矩表格参数化的角速度数据向量。该向量与 **Shaft angular velocity vector, w** 和 **Displacement vector, D** 参数一起，形成三维相关 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数的独立轴。向量元素必须按升序排列。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下任一项：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **Displacement vector, D** — 用于表格数据参数化的排量体积向量 `[-30, -19, 19, 30] cm^3/s` (默认) | 1-by-*n* vector

用于泄漏和摩擦力矩表格参数化的体积排量数据向量。该向量与 **Shaft angular velocity vector, w** 和 **Pressure drop vector, dp** 参数一起，形成三维相关 **Volumetric efficiency table, e\_v(dp,w,D)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数的独立轴。向量元素必须按升序排列。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下任一项：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **Volumetric efficiency table, e\_v(dp,w,D)** — 用于表格数据参数化的容积效率 `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)` (默认) | *M*-by-*N*-by-*P* matrix

*M*-by-*N*-by-*P* 矩阵，包含在指定流体压降、轴角速度和体积排量下的容积效率。表元素之间采用线性插值。*M*、*N* 和 *P* 是对应向量的长度：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。
- *P* 是 **Displacement vector, D** 参数中向量元素的个数。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w,D)** — 用于表格数据参数化的机械效率 `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)` (默认) | *M*-by-*N*-by-*P* matrix

*M*-by-*N*-by-*P* 矩阵，包含在指定流体压降、轴角速度和排量下的机械效率。表元素之间采用线性插值。*M*、*N* 和 *P* 是对应向量的长度：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。
- *P* 是 **Displacement vector, D** 参数中向量元素的个数。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Volumetric loss table, q\_loss(dp,w,D)** — 用于表格数据参数化的容积损失 `repmat([.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3, 1, 1, 4)` (默认) | *M*-by-*N*-by-*P* matrix

*M*-by-*N*-by-*P* 矩阵，包含在指定流体压降、轴角速度和排量下的容积泄漏。表元素之间采用线性插值。*M*、*N* 和 *P* 是对应向量的长度：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。
- *P* 是 **Displacement vector, D** 参数中向量元素的个数。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Mechanical loss table, torque\_loss(dp,w,D)** — 用于表格数据参数化的机械损失 `repmat([.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626], 1, 1, 4) N*m` (默认) | *M*-by-*N*-by-*P* matrix

*M*-by-*N*-by-*P* 矩阵，包含在指定流体压降和轴角速度下的机械损失。表元素之间采用线性插值。*M*、*N* 和 *P* 是相关向量的长度：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的个数。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的个数。
- *P* 是 **Displacement vector, D** 参数中向量元素的个数。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Minimum volumetric efficiency** — 容积效率的最小值 `1e-3` (默认) | positive scalar in the range of (0,1]

容积效率的最小值。如果输入信号低于此值，则将容积效率设置为最小容积效率。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum volumetric efficiency** — 容积效率的最大值 `1` (默认) | positive scalar in the range of (0,1]

容积效率的最大值。如果输入信号高于此值，则将容积效率设置为最大容积效率。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Minimum mechanical efficiency** — 机械效率的最小值 `1e-3` (默认) | positive scalar in the range of (0,1]

机械效率的最小值。如果输入信号低于此值，则将机械效率设置为最小机械效率。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum mechanical efficiency** — 机械效率的最大值 `1` (默认) | positive scalar in the range of (0,1]

机械效率的最大值。如果输入信号高于此值，则将机械效率设置为最大机械效率。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Pressure drop threshold for motor-pump transition** — 模式转换的压力阈值 `1e-3 MPa` (默认) | positive scalar

指示电机和泵功能之间转换阈值的电机压降。在压降阈值的正值和负值之间，围绕 0 MPa 定义了一个过渡区域。在该过渡区域内，计算出的泄漏流量和摩擦扭矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下任一项：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **Angular velocity threshold for motor-pump transition** — 模式转换的角速度阈值 `100 rpm` (默认) | positive scalar

指示电机和泵功能之间转换阈值的轴角速度。在角速度阈值的正值和负值之间，围绕 0 rpm 定义了一个过渡区域。在该过渡区域内，计算出的泄漏流量和摩擦扭矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖项

要启用此参数，请将 **Leakage and friction parameterization** 设置为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **Displacement threshold for motor-pump transition** — 模式转换的排量阈值 `0.1 cm^3/s` (默认) | positive scalar

指示电机和泵功能之间转换阈值的体积排量。在排量阈值的正值和负值之间，围绕 0 cm^3/s 定义了一个过渡区域。在该过渡区域内，计算出的泄漏流量和摩擦扭矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。当 **D** 的符号变化时，它还用于过渡理想质量流量。

### **检查是否超出所提供表格数据的范围** — 是否在所提供数据的范围被超过时发出通知 `None`（默认）| `Warning` | `Error`

是否在所提供数据的范围被超过时发出通知。
选择 `Warning` 以在模块使用超出所提供数据范围的值时收到通知。选择
`Error` 以在模块使用超出所提供数据范围的值时停止仿真。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦
参数化** 设置为：

- `Tabulated data - volumetric and mechanical
  efficiencies`
- `Tabulated data - volumetric and mechanical
  losses`

### **检查是否超出马达模式** — 是否在模块运行超出马达模式功能时发出通知 `None`（默认）| `Warning` | `Error`

是否在模块运行超出马达模式功能时发出通知。选择 `Warning` 以在模块以正向或反向泵模式运行时收到通知。选择
`Error` 以在模块以正向或反向泵模式运行时停止仿真。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦
参数化** 设置为 `Input signal -
volumetric and mechanical losses`。

### **检查压力是否低于马达最小压力** — 是否在流体出口压力低时发出通知 `None`（默认）| `Warning` | `Error`

是否在端口 **A** 或 **B** 处的流体经历低压时发出通知。选择
`Warning` 以在压力低于指定的最小值时收到通知。选择
`Error` 以在压力低于指定的最小值时停止仿真。

该参数有助于识别可能发生气蚀的条件，即当流体压力低于流体蒸气压时。

### **马达最小压力** — 马达出口处可接受压力的下限 `0.101325 MPa`（默认）| 正标量

马达入口或出口处可接受压力的下限。

#### 依赖关系

要启用此参数，请将 **检查压力是否低于马达最小压力** 设置为以下任一值：

- `Warning`
- `Error`

## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：检查模块是否在计算数据范围之外运行

**检查是否超出所提供表格数据的卦限** 参数已重命名为 **检查是否超出所提供表格数据的范围**。您可以启用
**检查是否超出所提供表格数据的范围** 参数，以检查模块是否在模块参数中指定的数据范围之外运行，即模块已扩展数据的区域中运行。

## 描述

等温液体系统中的可变排量马达

Variable-Displacement Motor (IL) 模块对具有可变容积排量的马达进行建模。流体可以从端口 **A** 流向端口 **B**，称为*正向模式*，或者从端口 **B** 流向端口 **A**，称为*反向模式*。当沿流动方向存在压降时，发生马达模式运行。当沿流动方向存在压力增益时，发生泵模式运行。

轴旋转对应于流经马达的流体容积的符号，该容积在端口 **D** 处作为物理信号接收。在 **D** 处的正流体排量对应于正向模式下的正轴旋转。在 **D** 处的负流体排量对应于正向模式下的负轴角速度。

**运行模式**

该模块有八种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压降，*Δp =
p*A – *p*B；
角速度，*ω = ω*R –
*ω*C；以及端口 **D** 处的流体容积排量。上图将这些模式映射到
*Δp*-*ω*-*D* 图的卦限：

- 模式 1，*Forward Motor*：从端口
  **A** 到端口 **B** 的流动导致从 **A** 到 **B** 的压力降低以及正轴角速度。
- 模式 2，*Reverse Pump*：负轴角速度
  导致从端口 **B** 到端口 **A** 的压力升高以及从 **B** 到端口 **A** 的流动。
- 模式 3，*Reverse Motor*：从端口
  **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力降低以及负轴角速度。
- 模式 4，*Forward Pump*：正轴角速度
  导致从端口 **A** 到端口 **B** 的压力升高以及从 **A** 到 **B** 的流动。
- 模式 5，*Reverse Pump*：正轴角速度
  导致从端口 **B** 到端口 **A** 的压力升高以及从 **B** 到 **A** 的流动。
- 模式 6，*Forward Motor*：从端口
  **A** 到端口 **B** 的流动导致从 **A** 到 **B** 的压力降低以及正轴角速度。
- 模式 7，*Forward Pump*：负轴角速度
  导致从端口 **A** 到端口 **B** 的压力升高以及从 **A** 到 **B** 的流动。
- 模式 8，*Reverse Motor*：从
  **B** 到 **A** 的流动导致从 **B** 到 **A** 的压力降低以及正轴角速度。

马达模块具有解析、查找表和物理信号参数化。使用表格数据或输入信号进行参数化时，您可以选择基于效率或损失来表征马达运行。

阈值参数 **Pressure drop threshold for motor-pump transition**、**Angular velocity threshold for motor-pump transition** 和 **Displacement threshold for motor-pump transition** 标识可能出现马达运行模式之间数值平滑流动过渡的区域。对于压力和角速度阈值，请选择为过渡项提供一定裕量的过渡区域，但该区域相对于典型马达压降和角速度要足够小，以免影响计算结果。对于排量阈值，请选择小于正常运行期间典型排量的阈值。

### 解析泄漏和摩擦参数化

如果您将 **泄漏和摩擦参数化** 设置为 `Analytical`，则该模块根据轴速度、压降、容积排量和扭矩的恒定标称值计算内部泄漏和轴摩擦。泄漏流量与马达上的压差相关，计算如下：

m˙leak=KρavgΔp,

其中：

- *Δp* 是 *p*A – *p*B。
- *ρ*avg 是平均流体密度。
- *K* 是解析损失的 Hagen-Poiseuille 系数，

  K=Dnomωnom(1ηv,nom−1)Δpnom,

  其中：

  - *D*nom 是 **标称排量**。
  - *ω*nom 是 **标称轴角速度**。
  - *η*nom 是 **标称条件下的容积效率**。
  - *Δp*nom 是 **标称压降**。

扭矩与马达压差相关，计算如下：

τfr=(τ0+k|ΔpDDnom|)tanh(4ω5×10−5ωnom),

其中：

- *τ*0 是 **空载扭矩**。
- *k* 是标称排量下的摩擦扭矩与压力增益系数，由 **标称条件下的机械效率** *ηm,nom* 确定：

  k=τfr,nom−τ0Δpnom.

  *τfr,nom* 是标称条件下的摩擦扭矩：

  τfr,nom=(1−ηm,nom)DnomΔpnom.
- *Δp* 是端口 **A** 和 **B** 之间的压降。
- *ω* 是相对轴角速度，即 ωR−ωC。

### 表格数据参数化

使用表格数据表示马达效率或损失时，您可以为一个或多个马达运行模式提供数据。表格数据的符号决定模块的运行状态。当提供的数据少于八种运行模式时，该模块通过将给定数据扩展到其余卦限来计算其他模式的补充数据。

**`Tabulated data - volumetric and mechanical efficiencies` 参数化**

泄漏流量计算如下：

m˙leak=m˙leak,motor(1+α2)+m˙leak,pump(1−α2),

其中：

- m˙leak,pump=(ηυ−1)m˙ideal
- m˙leak,motor=(1−ηv)m˙

并且 *η*v 是容积效率，它从用户提供的表格数据中插值得到。过渡项 *α* 为

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold)tanh(4DDthreshold),

其中：

- *Δp* 是 *p*A – *p*B。
- *Δp*threshold 是 **Pressure drop threshold for motor-pump transition**。
- *ω* 是 *ω*R – *ω*C。
- *ω*threshold 是 **Angular velocity threshold for motor-pump transition**。

扭矩计算如下：

τfr=τfr,pump(1+α2)+τfr,motor(1−α2),

其中：

- τfr,pump=(ηm−1)τ
- τfr,motor=(1−ηm)τideal

并且 *η*m 是机械效率，它从用户提供的表格数据中插值得到。

**`Tabulated data - volumetric and mechanical losses` 参数化**

泄漏流量计算如下：

m˙leak=ρavgqloss(Δp,ω,D),

其中 *q*loss 从 **Volumetric loss table, q\_loss(dp,w,D)** 参数插值得到，该参数基于用户提供的压降、轴角速度和流体容积排量数据。

轴摩擦扭矩计算如下：

τfr=τloss(Δp,ω,D),

其中 *τ*loss 从 **Mechanical loss table, torque\_loss(dp,w,D)** 参数插值得到，该参数基于用户提供的压降、轴角速度和流体容积排量数据。

### 输入信号参数化

当 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies` 时，端口 **EV** 和 **EM** 启用。内部泄漏和轴摩擦的计算方式与 `Tabulated data - volumetric and mechanical efficiencies` 参数化相同，不同之处在于 *η*v 和 *η*m 分别直接在端口 **EV** 和 **EM** 处接收。

当 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical losses` 时，端口 **LV** 和 **LM** 启用。这些端口以正物理信号形式接收泄漏流量和摩擦扭矩。泄漏流量计算如下：

m˙leak=ρavgqLVtanh(4Δppthresh),

其中：

- *q*LV 是在端口 **LV** 处接收的泄漏流量。
- *p*thresh 是 **Pressure drop threshold for motor-pump transition** 参数。

摩擦扭矩计算如下：

τfr=τLMtanh(4ωωthresh),

其中

- *τ*LM 是在端口 **LM** 处接收的摩擦扭矩。
- *ω*thresh 是 **Angular velocity threshold for motor-pump transition** 参数。

容积效率和机械效率在用户指定的最小值和最大值之间。任何低于或高于此范围的值将分别取指定的最小值和最大值。

### 马达运行

马达流量为：

m˙=m˙ideal+m˙leak,

其中 m˙ideal=ρavgD⋅ω。

马达扭矩为：

τ=τideal−τfr,

其中 τideal=D⋅Δp。

马达轴提取的机械功率为：

φmech=τω,

马达液压功率为：

φhyd=Δpm˙ρavg.

若要在模块运行超出提供的表格数据时收到通知，您可以将 **检查是否超出所提供表格数据的范围** 设置为 `Warning`，以便在发生此情况时收到警告，或设置为 `Error`，以便在发生此情况时停止仿真。使用输入信号表示容积损失或机械损失时，您可以通过 **检查是否超出马达模式** 参数在仿真超过运行模式时收到通知。

您还可以监测马达功能。将 **检查压力是否低于马达最小压力** 设置为 `Warning`，以便在发生此情况时收到警告，或设置为 `Error`，以便在发生此情况时停止仿真。
