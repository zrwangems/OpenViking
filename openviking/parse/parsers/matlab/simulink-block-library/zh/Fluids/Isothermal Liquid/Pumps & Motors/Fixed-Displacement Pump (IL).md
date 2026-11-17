---
type: simulink-block
title: 'Fixed-Displacement Pump (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'fixeddisplacementpumpil'
documentation_source_path: 'ref/fixeddisplacementpumpil.html'
language: zh-CN
chinese_source: worker-translation
---

# Fixed-Displacement Pump (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

泵的液体进入或出口端口。

### **B** — 液体端口，等温液体

泵的液体进入或出口端口。

### **R** — 机械端口，机械旋转

旋转轴的角速度和扭矩。

### **C** — 机械端口，机械旋转

泵壳体的角速度和扭矩。
### 输入

### **EV** — 容积效率，物理信号

用于流体排量的泵效率，指定为物理信号。该值必须在 0 到 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率，物理信号

用于机械能量供应的泵效率，指定为物理信号。该值必须在 0 到 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 泄漏流量，`m^3/s` 物理信号

泵的容积损失，单位为 m^3/s，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 摩擦力矩，`N*m` 物理信号

泵的机械损失，单位为 N\*m，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

## 参数

### 参数

### **Leakage and friction parameterization** — 泄漏流量和摩擦力矩的计算方法 `Analytical`（默认）| `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

泵的泄漏和摩擦特性的参数化方式。

- 在 `Analytical` 参数化中，泄漏流量和摩擦力矩通过解析方程计算。
- 在 `Tabulated data - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率根据用户提供的 **Pressure gain vector, dp** 和 **Shaft angular velocity vector, w** 参数计算，并从二维依赖的 **Volumetric efficiency table, e\_v(dp,w)** 和 **Mechanical efficiency table, e\_m(dp,w)** 表中插值得到。
- 在 `Tabulated data - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩根据用户提供的 **Pressure gain vector, dp** 和 **Shaft angular velocity vector, w** 参数计算，并从二维依赖的 **Volumetric loss table, q\_loss(dp,w)** 和 **Mechanical loss table, torque\_loss(dp,w)** 表中插值得到。
- 在 `Input signal - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率分别作为物理信号在端口 **EV** 和 **EM** 处接收。
- 在 `Input signal - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦力矩分别作为物理信号在端口 **LV** 和 **LM** 处接收。

### **Displacement** — 固定容积流体排量 `30 cm^3/rev`（默认）| 标量

在标称或典型工况下，轴旋转所排出的流体量。

### **Nominal shaft angular velocity** — 轴角速度 `1800 rpm`（默认）| 标量

在标称工况下的轴角速度。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal pressure gain** — 流体入口和出口之间的压力增益 `10 MPa`（默认）| 标量

在标称或典型工况下，泵在流体入口和出口之间的压力增益。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Volumetric efficiency at nominal conditions** — 实际流量与理想流量之比 `0.92`（默认）| 正标量

在标称条件下实际流量与理想流量之比。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **No-load torque** — 基线扭矩 `0 N*m`（默认）| 标量

克服密封摩擦并引起轴运动所需的最小扭矩值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Mechanical efficiency at nominal conditions** — 实际扭矩与产生的理想扭矩之比 `0.88`（默认）| 正标量

在标称条件下实际扭矩与产生的理想扭矩之比。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Pressure gain vector, dp** — 用于表格数据参数化的压力数据向量 `[.1, 1, 2] MPa`（默认）| 1×*n* 向量

用于泄漏和摩擦力矩表格参数化的压差值向量。该向量与 **Shaft angular velocity vector, w** 参数一起构成二维依赖的 **Volumetric efficiency table, e\_v(dp,w)** 和 **Mechanical efficiency table, e\_m(dp,w,D)** 参数的独立轴。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **Shaft angular velocity vector, w** — 用于表格数据参数化的角速度数据向量 `[250, 500, 1000, 2000, 3000, 4000] rpm`（默认）| 1×*n* 向量

用于泄漏和摩擦力矩表格参数化的角速度数据向量。该向量与 **Shaft angular velocity vector, w** 参数一起构成二维依赖的 **Volumetric efficiency table, e\_v(dp,w)** 和 **Mechanical efficiency table, e\_m(dp,w)** 参数的独立轴。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **Volumetric efficiency table, e\_v(dp,w)** — 用于表格数据参数化的容积效率 `[.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91]`（默认）| *M*×*N*×*P* 矩阵

在指定的流体压力增益和轴角速度下的 *M*×*N* 容积效率矩阵。表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w)** — 用于表格数据参数化的机械效率 `[.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984]`（默认）| *M*×*N*×*P* 矩阵

在指定的流体压力增益和轴角速度下的 *M*×*N* 机械效率矩阵。表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Volumetric loss table, q\_loss(dp,w)** — 用于表格数据参数化的容积损失 `[.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3 m^3/s`（默认）| *M*×*N*×*P* 矩阵

在指定的流体压力增益和轴角速度下的 *M*×*N* 容积效率矩阵。表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical loss`。

### **Mechanical loss table, torque\_loss(dp,w)** — 用于表格数据参数化的机械损失 `[.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626] N*m`（默认）| *M*×*N*×*P* 矩阵

在指定的流体压力增益和轴角速度下的 *M*×*N* 机械损失矩阵。表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure gain vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical loss`。

### **Minimum volumetric efficiency** — 容积效率的最小值 `1e-3`（默认）| (0,1] 范围内的正标量

容积效率的最小值。如果输入信号低于此值，则容积效率设置为最小容积效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum volumetric efficiency** — 容积效率的最大值 `1`（默认）| 正标量

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

### **Pressure gain threshold for pump-motor transition** — 模式转换的压力阈值 `1e-3 MPa`（默认）| 正标量

泵和马达功能之间转换的阈值压力增益值。在压力增益阈值的正值和负值之间，围绕 0 MPa 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **Angular velocity threshold for pump-motor transition** — 模式转换的角速度阈值 `100 rpm`（默认）| 正标量

泵和马达功能之间转换的阈值角速度值。在角速度阈值的正值和负值之间，围绕 0 rpm 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦力矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **Check if operating beyond the range of supplied tabulated data** — 是否在超出所提供表格数据范围时发出通知 `None`（默认）| `Warning` | `Error`

是否在超出所提供数据范围时发出通知。选择 `Warning` 以在模块使用超出所提供数据范围的值时收到通知。选择 `Error` 以在模块使用超出所提供数据范围的值时停止仿真。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **Check if operating outside of pump mode** — 是否在模块运行于泵模式功能之外时发出通知 `None`（默认）| `Warning` | `Error`

是否在模块运行于泵模式功能之外时发出通知。此模块有四种运行模式：正向泵、反向泵、反向马达和正向马达。选择 `Warning` 以在模块运行于正向或反向马达模式时收到通知。选择 `Error` 以在模块运行于正向或反向马达模式时停止仿真。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### **Check if pressures are less than pump minimum pressure** — 是否在流体出口压力过低时发出通知 `None`（默认）| `Warning` | `Error`

是否在端口 **A** 或 **B** 处的流体经历低压时发出通知。选择 `Warning` 以在出口压力降至指定的最小值以下时收到通知。选择 `Error` 以在出口压力降至指定的最小值以下时停止仿真。

该参数有助于识别可能发生气蚀的条件，即流体压力降至流体蒸气压以下时。

### **Pump minimum pressure** — 泵出口可接受压力的下限阈值 `0.101325 MPa`（默认）| 正标量

泵入口和出口可接受压力的下限阈值。

#### 依赖关系

要启用此参数，请将 **Check if pressures are less than pump minimum pressure** 设置为：

- `Warning`
- `Error`

### 故障

### **Displacement fault** — 用于对排量故障建模的选项 `Add fault`

用于对模块中的排量故障建模的选项。发生故障时，排量按 **Faulted displacement factor** 参数的值进行缩放。要添加故障，请点击 **Add fault** 超链接。

### **Faulted displacement factor** — 用于缩放故障排量的因子 `0.5`（默认）| 正标量

模块在发生故障时用于缩放排量的因子。

#### 依赖关系

要启用此参数，请为 **Displacement fault** 参数点击 **Add fault** 超链接。

### **Leakage fault** — 用于对泄漏故障建模的选项 `Add fault`

用于对模块中的泄漏故障建模的选项。发生故障时，容积效率或损失将按 **Faulted leakage factor** 参数的值进行缩放。要添加故障，请点击 **Add fault** 超链接。

### **Faulted leakage factor** — 用于缩放泄漏故障的因子 `2.0`（默认）| 正标量

发生故障时，模块用于缩放容积效率或损失的因子。

#### 依赖关系

要启用此参数，请为 **Leakage fault** 参数点击 **Add fault** 超链接。

### **Shaft friction torque fault** — 用于对轴摩擦力矩故障建模的选项 `Add fault`

用于对模块中的轴摩擦力矩故障建模的选项。发生故障时，机械效率或损失将按 **Faulted shaft friction torque factor** 参数的值进行缩放。要添加故障，请点击 **Add fault** 超链接。

### **Faulted shaft friction torque factor** — 用于缩放轴摩擦力矩故障的因子 `2.0`（默认）| 正标量

发生故障时，模块用于缩放机械效率或损失的因子。

#### 依赖关系

要启用此参数，请为 **Shaft friction torque fault** 参数点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024b：使用 Simscape faults 接口对故障建模

Fixed-Displacement Pump (IL) 模块现在支持 Simscape™ faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2024a：检查模块是否在计算数据范围之外运行

**Check if operating beyond the quadrants of supplied tabulated data** 参数已重命名为 **Check if operating beyond the range of supplied tabulated data**。您可以启用 **Check if operating beyond the range of supplied tabulated data** 参数，以检查模块是否在模块参数指定的数据之外运行，即模块已扩展数据的区域内运行。

## 描述

等温液体系统中的固定排量泵

Fixed-Displacement Pump (IL) 模块对具有恒定容积排量的泵进行建模。流体可以从端口 **A** 流向端口 **B**，称为*正向模式*，也可以从端口 **B** 流向端口 **A**，称为*反向模式*。当沿流动方向存在压力增益时，为泵模式运行。当沿流动方向存在压力下降时，为马达模式运行。

轴旋转对应于流体容积的符号。正流体排量对应于正向模式下的正轴旋转。负流体排量对应于正向模式下的负轴角速度。

**运行模式**

该模块有四种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压力增益 *Δp = p*B – *p*A 以及角速度 *ω = ω*R – *ω*C：

- 模式 1，*正向泵*：正轴角速度导致从端口 **A** 到端口 **B** 的压力升高，以及从端口 **A** 到端口 **B** 的流动。
- 模式 2，*反向马达*：从端口 **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力下降以及负轴角速度。
- 模式 3，*反向泵*：负轴角速度导致从端口 **B** 到端口 **A** 的压力升高，以及从 **B** 到 **A** 的流动。
- 模式 4，*正向马达*：从端口 **A** 到 **B** 的流动导致从 **A** 到 **B** 的压力下降以及正轴角速度。

泵模块具有解析、查找表和物理信号参数化。使用表格数据或输入信号进行参数化时，您可以选择基于效率或损失来表征泵运行。

阈值参数 **Pressure gain threshold for pump-motor transition** 和 **Angular velocity threshold for pump-motor transition** 用于标识泵运行模式之间可发生数值平滑流动过渡的区域。对于压力阈值和角速度阈值，请选择为过渡项提供一定裕量的过渡区域，但该区域相对于典型泵压力增益和角速度应足够小，以免影响计算结果。

### 解析泄漏与摩擦参数化

如果将 **Leakage and friction parameterization** 设置为 `Analytical`，模块将根据轴速度、压力增益和摩擦力矩的恒定值计算泄漏和摩擦。与泵两端压差相关的泄漏流量计算如下：

m˙leak=KρavgΔp，

其中：

- *Δp* 为 *p*B – *p*A。
- *ρavg* 为平均流体密度。
- *K* 为用于解析损失的 Hagen-Poiseuille 系数，

  K=Dωnom(1−ηv,nom)Δpnom，

  其中：

  - *D* 为 **Displacement**。
  - *ωnom* 为 **Nominal shaft angular velocity**。
  - *ηv, nom* 为 **Volumetric efficiency at nominal conditions**。
  - *Δpnom* 为 **Nominal pressure gain**。

与泵压差相关的摩擦力矩计算如下：

τfr=(τ0+k|Δp|)tanh(4ω5×10−5ωnom)，

其中：

- *τ0* 为 **No-load torque**。
- *k* 为名义排量下的摩擦力矩与压力增益系数，由 **Mechanical efficiency at nominal conditions** *ηm, nom* 确定：

  k=τfr,nom−τ0Δpnom。

  *τfr,nom* 为名义条件下的摩擦力矩：

  τfr,nom=(1−ηm,nomηm,nom)DΔpnom。
- *ω* 为相对轴角速度，即 ωR−ωC。

### 表格数据参数化

使用表格数据表示泵效率或损失时，您可以为一种或多种泵运行模式提供数据。表格数据的符号决定模块的运行区域。当提供的数据少于四种运行模式时，模块通过将给定数据扩展到其余象限来计算其他模式的补充数据。

**`Tabulated data - volumetric and mechanical efficiencies` 参数化**

泄漏流量为

m˙leak=m˙leak,pump(1+α2)+m˙leak,motor(1−α2)，

其中：

- m˙leak,pump=(1−ηυ)m˙ideal
- m˙leak,motor=(ηv−1)m˙

并且 *η*v 为容积效率，由用户提供的表格数据插值得到。过渡项 *α* 为

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold)，

其中：

- *Δp* 为 *p*B – *p*A。
- *p*threshold 为 **Pressure gain threshold for pump-motor transition**。
- *ω* 为 *ω*R – *ω*C。
- *ω*threshold 为 **Angular velocity threshold for pump-motor transition**。

摩擦力矩计算如下：

τfr=τfr,pump(1+α2)+τfr,motor(1−α2)，

其中：

- τfr,pump=(1−ηm)τ
- τfr,motor=(ηm−1)τideal

并且 *η*m 为机械效率，由用户提供的表格数据插值得到。

**`Tabulated data - volumetric and mechanical losses` 参数化**

泄漏流量计算如下：

m˙leak=ρavgqloss(Δp,ω)，

其中 *q*loss 由 **Volumetric loss table, q\_loss(dp,w)** 参数插值得到，该参数基于用户提供的压降、轴角速度和流体容积排量数据。

轴摩擦力矩为

τfr=τloss(Δp,ω)tanh(4ωωthreshold)，

其中 *τ*loss 由 **Mechanical loss table, torque\_loss(dp,w)** 参数插值得到，该参数基于用户提供的压降和轴角速度数据。

### 输入信号参数化

当选择 `Input signal - volumetric and mechanical efficiencies` 时，端口 **EV** 和 **EM** 启用。内部泄漏和轴摩擦的计算方式与 `Tabulated data - volumetric and mechanical efficiencies` 参数化相同，不同之处在于 *η*v 和 *η*m 分别直接在端口 **EV** 和 **EM** 接收。

当选择 `Input signal - volumetric and mechanical losses` 时，端口 **LV** 和 **LM** 启用。这些端口以正物理信号形式接收泄漏流量和摩擦力矩。泄漏流量计算如下：

m˙leak=ρavgqLVtanh(4Δppthresh)，

其中：

- *q*LV 为在端口 **LV** 接收的泄漏流量。
- *p*thresh 为 **Pressure gain threshold for pump-motor transition** 参数。

摩擦力矩计算如下：

τfr=τLMtanh(4ωωthresh)，

其中

- *τ*LM 为在端口 **LM** 接收的摩擦力矩。
- *ω*thresh 为 **Angular velocity threshold for pump-motor transition** 参数。

容积效率和机械效率在用户指定的最小值和最大值之间取值。任何低于或高于此范围的值将分别取指定的最小值和最大值。

### 泵运行

泵流量为：

m˙=m˙ideal−m˙leak，

其中 m˙ideal=ρavgD⋅ω。

泵扭矩为：

τ=τideal+τfr，

其中 τideal=D⋅Δp。

泵轴传递的机械功率为：

φmech=τω，

泵液压功率为：

φhyd=Δpm˙ρavg。

如果您想知道模块是否在所提供的表格数据之外运行，可以将 **Check if operating beyond the range of supplied tabulated data** 设置为 `Warning`，以便在发生这种情况时收到警告，或设置为 `Error`，以便在发生这种情况时停止仿真。对于通过输入信号对容积损失或机械损失进行参数化的情况，可以使用 **Check if operating beyond pump mode** 参数在仿真超出运行模式时收到通知。

您还可以监测泵功能。将 **Check if pressures are less than pump minimum pressure** 设置为 `Warning`，以便在发生这种情况时收到警告，或设置为 `Error`，以便在发生这种情况时停止仿真。

### 预定义参数化

Fixed-Displacement Pump (IL) 模块可使用制造商数据进行预参数化。此数据允许您对特定供应商组件进行建模。

要加载预定义参数化：

1. 在 Fixed-Displacement Pump (IL) 模块对话框描述中点击 "Select a predefined parameterization" 超链接。
2. 从下拉菜单中选择一个部件，然后点击 **Update block with selected part**。
3. 如果在加载参数化后更改了任何参数设置，可以通过点击 **Compare block settings with selected part** 来检查更改。模块与预定义参数化之间的任何设置差异都将显示在 MATLAB 命令窗口中。

**注意**

Simscape 组件的预定义参数化使用可用的数据源来提供参数值。工程判断和简化假设用于填补缺失数据。因此，仿真行为与实际物理行为之间应预期存在偏差。为确保所需精度，您应根据实验数据验证仿真行为，并根据需要细化组件模型。

### 故障

要对故障建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Introduction to Simscape Faults。

您可以对排量故障、泄漏或轴摩擦力矩故障建模。

当启用 **Displacement fault** 参数时，模块在故障触发时按 **Faulted displacement factor** 参数的值缩放排量，

DFault=fDD，

其中 *fD* 为 **Faulted displacement factor** 参数的值。当 **Leakage and friction parameterization** 参数为 `Analytical` 时，模块不使用故障排量值来计算 Hagen-Poiseuille 系数或名义条件下的摩擦力矩。

当启用 **Leakage fault** 参数且 **Leakage and friction parameterization** 为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical efficiencies` 时，故障容积效率为

ηv,Fault=ηvfLeak，

其中 *fLeak* 为 **Faulted leakage factor** 参数的值，*ηv* 为容积效率。当 **Leakage and friction parameterization** 为 `Analytical` 时，模块使用故障容积效率来计算 Hagen-Poiseuille 系数。

当 **Leakage and friction parameterization** 为 `Tabulated data - volumetric and mechanical losses` 或 `Input signal - volumetric and mechanical losses` 时，故障泄漏体积流量为

qLeak,Fault=fLeakqLeak。

当启用 **Shaft friction torque fault** 参数且 **Leakage and friction parameterization** 为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical efficiencies` 时，故障机械效率为

ηm,Fault=ηmfFriction，

其中 *fFriction* 为 **Faulted shaft friction torque factor** 参数的值，*ηm* 为机械效率。当 **Leakage and friction parameterization** 为 `Analytical` 时，模块使用故障机械效率来计算名义条件下的摩擦力矩。

当 **Leakage and friction parameterization** 为 `Tabulated data - volumetric and mechanical losses` 或 `Input signal - volumetric and mechanical losses` 时，故障摩擦力矩为

τFriction,Fault=fFrictionτFriction。
