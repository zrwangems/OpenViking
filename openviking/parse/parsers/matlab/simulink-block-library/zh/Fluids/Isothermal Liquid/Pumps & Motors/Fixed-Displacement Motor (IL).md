---
type: simulink-block
title: 'Fixed-Displacement Motor (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'fixeddisplacementmotoril'
documentation_source_path: 'ref/fixeddisplacementmotoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Fixed-Displacement Motor (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

马达的入口或出口端口。

### **B** — 液体端口 isothermal liquid

马达的入口或出口端口。

### **R** — 机械端口 mechanical rotational

旋转轴的角速度和扭矩。

### **C** — 机械端口 mechanical rotational

马达壳体参考角速度和扭矩。
### 输入

### **EV** — 容积效率物理信号

用于流体排量的马达效率，指定为物理信号。该值必须介于 0 和 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率物理信号

用于机械能量提取的马达效率，指定为物理信号。该值必须介于 0 和 1 之间。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 泄漏流量，`m^3/s` 物理信号

与流体排量相关的马达损失，单位为 m^3/s，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 摩擦扭矩，`N*m` 物理信号

与机械能量提取相关的马达损失，单位为 N\*m，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical losses`。

## 参数

### 参数

### **Leakage and friction parameterization** — 计算泄漏流量和摩擦扭矩的方法 `Analytical`（默认）| `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Tabulated data - torque and speed` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

泵的泄漏和摩擦特性的参数化。

- 在 `Analytical` 参数化中，泄漏流量和摩擦扭矩通过解析方程计算。
- 在 `Tabulated data - volumetric and
  mechanical efficiencies` 参数化中，容积效率和机械效率根据用户提供的 **Pressure drop vector, dp** 和 **Shaft angular velocity vector, w** 参数计算，并从二维相关的 **Volumetric efficiency table, e\_v(dp,w)** 和 **Mechanical efficiency table, e\_m(dp,w)** 表插值得到。
- 在 `Tabulated data - volumetric and
  mechanical loss` 参数化中，泄漏流量和扭矩摩擦根据用户提供的 **Pressure drop vector, dp** 和 **Shaft angular velocity vector, w** 参数计算，并从二维相关的 **Volumetric loss table, q\_loss(dp,w)** 和 **Mechanical loss table, torque\_loss(dp,w)** 表插值得到。
- 在 `Tabulated data - torque and
  speed` 参数化中，您可以使用 **Torque table T(q,dp)** 和 **Shaft speed table w(q,dp)** 参数，将扭矩和轴转速输入为流量和压降的函数。
- 在 `Input signal - volumetric and
  mechanical efficiencies` 参数化中，容积效率和机械效率分别作为物理信号在端口 **EV** 和 **EM** 接收。
- 在 `Input signal - volumetric and
  mechanical loss` 参数化中，泄漏流量和扭矩摩擦分别作为物理信号在端口 **LV** 和 **LM** 接收。

### **Displacement** — 固定容积流体排量 `30 cm^3/rev`（默认）| scalar

固定容积的流体排量。

### **Nominal shaft angular velocity** — 轴角速度 `1800 rpm`（默认）| scalar

名义工况下的轴角速度。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Nominal pressure drop** — 流体入口和出口之间的压降 `10 MPa`（默认）| scalar

名义工况下马达流体入口和出口之间的压降。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Volumetric efficiency at nominal conditions** — 名义条件下实际流量与理想流量的比率 `0.92`（默认）| positive scalar

名义条件下实际流量与理想流量的比率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **No-load torque** — 基线扭矩 `0 N*m`（默认）| scalar

克服密封摩擦并引起轴运动所需的最小扭矩值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Mechanical efficiency at nominal conditions** — 名义条件下实际扭矩与理想生成扭矩的比率 `0.88`（默认）| positive scalar

名义条件下实际扭矩与理想生成扭矩的比率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Analytical`。

### **Pressure drop vector, dp** — 用于表格数据参数化的压力数据向量 `[.1, 1, 2] MPa`（默认）| 1-by-*n* vector

用于泄漏和扭矩摩擦表格参数化的压力差值向量。该向量与 **Shaft angular velocity vector, w** 参数或 **Flow rate vector, q** 参数一起构成独立轴，用于三维相关的 **Volumetric efficiency table, e\_v(dp,w)**、**Mechanical efficiency table, e\_m(dp,w)**、**Torque table, T(q,dp)** 和 **Shaft speed table, w(q,dp)** 参数。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Tabulated data - volumetric and
  mechanical losses`
- `Tabulated data - torque and
  speed`

### **Shaft angular velocity vector, w** — 用于表格数据参数化的角速度数据向量 `[250, 500, 1000, 2000, 3000, 4000] rpm`（默认）| 1-by-*n* vector

用于泄漏和扭矩摩擦表格参数化的角速度数据向量。该向量与 **Shaft angular velocity vector, w** 参数一起构成独立轴，用于三维相关的 **Volumetric efficiency table, e\_v(dp,w)** 和 **Mechanical efficiency table, e\_m(dp,w)** 参数。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Tabulated data - volumetric and
  mechanical losses`

### **Flow rate vector, q** — 流量数据向量 `[.125, .25, .5, 1, 1.5, 2] * 1e-3 m^3/s`（默认）| 1-by-*n* vector

用于扭矩和转速表格参数化的流量数据向量。该向量与 **Pressure drop vector, dp** 参数一起构成独立轴，用于三维相关的 **Torque table, T(q,dp)** 和 **Shaft speed table, w(q,dp)** 参数。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed`。

### **Volumetric efficiency table, e\_v(dp,w)** — 用于表格数据参数化的容积效率 `[.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91]`（默认）| *M*-by-*N* matrix

在指定流体压降和轴角速度下的容积效率的 *M*-by-*N* matrix。模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Mechanical efficiency table, e\_m(dp,w)** — 用于表格数据参数化的机械效率 `[.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984]`（默认）| *M*-by-*N* matrix

在指定流体压降和轴角速度下的机械效率的 *M*-by-*N* matrix。模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **Volumetric loss table, q\_loss(dp,w)** — 用于表格数据参数化的容积损失 `[.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3 m^3/s`（默认）| *M*-by-*N* matrix

在指定流体压降和轴角速度下的容积效率的 *M*-by-*N* matrix。模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Mechanical loss table, torque\_loss(dp,w)** — 用于表格数据参数化的机械损失 `[.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626] N*m`（默认）| *M*-by-*N* matrix

在指定流体压降和轴角速度下的机械损失的 *M*-by-*N* matrix。模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **Shaft angular velocity vector, w** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - volumetric and mechanical losses`。

### **Torque table, T(q,dp)** — 用于表格数据参数化的扭矩值 `[.47, 4.72, 9.35; .47, 4.7, 9.36; .47, 4.7, 9.4; .47, 4.7, 9.41; .47, 4.7, 9.46; .47, 4.68, 9.5] N*m`（默认）| *M*-by-*N* matrix

在指定流体压降和流量下的扭矩值的 *M*-by-*N* matrix。模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Flow rate vector, q** 参数中元素的数量。
- *N* 是 **Pressure drop vector, dp** 参数中向量元素的数量。

如果您的表在四个角中的任意一个角有未知数据点，请使用 `NaN` 代替这些值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed`。

### **Shaft speed table, w(q,dp)** — 用于表格数据参数化的轴转速 `[205, 80, 35; 455, 330, 285; 955, 831, 780; 1950, 1830, 1780; 2940, 2775, 2680; 3940, 3780, 3640] rpm`（默认）| *M*-by-*N* matrix

在指定流体压降和流量下的轴转速值的 *M*-by-*N* matrix。模块在表元素之间采用线性插值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Flow rate vector, q** 参数中元素的数量。
- *N* 是 **Pressure drop vector, dp** 参数中向量元素的数量。

如果您的表在四个角中的任意一个角有未知数据点，请使用 `NaN` 代替这些值。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Tabulated data - torque and speed`。

### **Minimum volumetric efficiency** — 容积效率的最小值 `1e-3`（默认）| positive scalar in the range of (0,1]

容积效率的最小值。如果输入信号低于此值，则容积效率设置为最小容积效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum volumetric efficiency** — 容积效率的最大值 `1`（默认）| positive scalar

容积效率的最大值。如果输入信号高于此值，则容积效率设置为最大容积效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Minimum mechanical efficiency** — 机械效率的最小值 `1e-3`（默认）| positive scalar in the range of (0,1]

机械效率的最小值。如果输入信号低于此值，则机械效率设置为最小机械效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Maximum mechanical efficiency** — 机械效率的最大值 `1`（默认）| positive scalar in the range of (0,1]

机械效率的最大值。如果输入信号高于此值，则机械效率设置为最大机械效率。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **Pressure drop threshold for motor-pump transition** — 模式转换的压力阈值 `1e-3 MPa`（默认）| positive scalar

用于泵和马达功能之间转换的压降阈值。在压降阈值的正值和负值之间，围绕 0 MPa 定义了一个过渡区域。在此过渡区域内，计算出的泄漏流量和摩擦扭矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Input signal - volumetric and mechanical
  efficiencies`
- `Input signal - volumetric and mechanical
  losses`

### **Angular velocity threshold for motor-pump transition** — 模式转换的角速度阈值 `100 rpm`（默认）| positive scalar

用于泵和马达功能之间转换的角速度阈值。在角速度阈值的正值和负值之间，围绕 0 rpm 定义了一个过渡区域。在此过渡区域内，计算出的泄漏流量和摩擦扭矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **Leakage and friction parameterization** 设置为以下之一：

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Input signal - volumetric and mechanical
  efficiencies`
- `Input signal - volumetric and mechanical
  losses`

### **Check if operating beyond the range of supplied tabulated data** — 是否在所提供数据的范围被超过时发出通知 `None`（默认） | `Warning` | `Error`

是否在所提供数据的范围被超过时发出通知。
选择 `Warning`，以便在模块使用超出所提供数据范围的值时收到通知。选择
`Error`，以便在模块使用超出所提供数据范围的值时停止仿真。

当 **Leakage and friction parameterization** 为
`Tabulated data - torque and speed` 时，此参数还会检查模块是否在提供的
`NaN` 值区域内运行。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`
- `Tabulated data - torque and speed`

### **Check if operating outside of motor mode** — 是否在模块运行于电机模式功能之外时发出通知 `None`（默认） | `Warning` | `Error`

是否在模块运行于电机模式功能之外时发出通知。此模块有四种运行模式：正向电机、
反向电机、反向泵和正向泵。选择
`Warning`，以便在模块运行于正向或反向马达泵模式时收到通知。选择
`Error`，以便在模块运行于正向或反向泵模式时停止仿真。

#### 依赖关系

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical losses`。

### **Check if pressures are less than motor minimum pressure** — 是否在流体出口压力过低时发出通知 `None`（默认） | `Warning` | `Error`

是否在端口 **A** 或 **B** 处的流体经历低压时发出通知。选择
`Warning`，以便在出口压力低于指定的最小值时收到通知。选择
`Error`，以便在出口压力低于指定的最小值时停止仿真。

此参数有助于识别潜在的汽蚀条件，即流体压力低于流体蒸气压时。

### **Motor minimum pressure** — 马达出口处可接受压力的下限阈值 `0.101325 MPa`（默认） | 正标量

马达入口或出口处可接受压力的下限阈值。

#### 依赖关系

要启用此参数，请将 **Check if pressures are
less than motor minimum pressure** 设置为以下之一：

- `Warning`
- `Error`

### 故障

### **Displacement fault** — 对位移故障建模的选项 `Add fault`

对模块中的位移故障建模的选项。当发生故障时，位移按 **Faulted displacement
factor** 参数的值进行缩放。要添加故障，请单击 **Add
fault** 超链接。

### **Faulted displacement factor** — 用于缩放故障位移的因子 `0.5`（默认） | 正标量

当发生故障时，模块用于缩放位移的因子。

#### 依赖关系

要启用此参数，请单击 **Displacement fault** 参数的 **Add fault** 超链接。

### **Leakage fault** — 对泄漏故障建模的选项 `Add fault`

对模块中的泄漏故障建模的选项。当发生故障时，容积效率或损失按 **Faulted
leakage factor** 参数的值进行缩放。要添加故障，请单击 **Add
fault** 超链接。

### **Faulted leakage factor** — 用于缩放泄漏故障的因子 `2.0`（默认） | 正标量

当发生故障时，模块用于缩放容积效率或损失的因子。

#### 依赖关系

要启用此参数，请单击 **Leakage fault** 参数的 **Add fault** 超链接。

### **Shaft friction torque fault** — 对轴摩擦扭矩故障建模的选项 `Add fault`

对模块中的轴摩擦扭矩故障建模的选项。当发生故障时，机械效率或损失按
**Faulted shaft friction torque factor** 参数的值进行缩放。要添加
故障，请单击 **Add fault** 超链接。

### **Faulted shaft friction torque factor** — 用于缩放轴摩擦扭矩故障的因子 `2.0`（默认） | 正标量

当发生故障时，模块用于缩放机械效率或损失的因子。

#### 依赖关系

要启用此参数，请单击 **Shaft friction torque fault**
参数的 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024b：使用 Simscape faults 接口对故障建模

Fixed-Displacement Motor (IL) 模块现在支持 Simscape™ faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2024a：使用扭矩和轴转速对模块进行参数化

现在，您可以通过将 **Leakage and friction parameterization** 参数设置为
`Tabulated data - torque and speed` 来指定扭矩和轴转速，从而对模块进行参数化。制造商
通常以这种格式提供电机数据表。

### R2024a：检查模块是否在计算数据范围之外运行

**Check if operating beyond the quadrants of supplied tabulated
data** 参数已重命名为 **Check if operating
beyond the range of supplied tabulated data**。您可以启用
**Check if operating beyond the range of supplied tabulated
data** 参数，以检查模块是否在模块参数中指定的数据之外运行，即，在模块已扩展数据的区域中运行。

## 描述

等温液体系统中的固定排量马达

Fixed-Displacement Motor (IL) 模块对具有恒定容积排量的马达进行建模。流体可以从端口 **A** 流向端口
**B**，称为*正向模式*，或从端口
**B** 流向端口 **A**，称为*反向模式*。当沿流动方向存在压降时，发生电机模式运行。当沿流动方向存在压力升高时，发生泵模式运行。

轴旋转对应于流经马达的流体体积的符号。正流体排量对应于正向模式下的正轴旋转。
负流体排量对应于正向模式下的负轴角速度。

该模块有八种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压降，
*Δp = p*A – *p*B 以及角速度 *ω =
ω*R – *ω*C：

- 模式 1，*正向电机*：从端口 **A** 流向端口
  **B** 的流动导致从 **A** 到 **B** 的压力降低以及正轴角速度。
- 模式 2，*反向泵*：负轴角速度导致从端口 **B** 到端口
  **A** 的压力升高以及从 **B** 到端口 **A** 的流动。
- 模式 3，*反向电机*：从端口 **B** 流向端口
  **A** 的流动导致从 **B** 到 **A** 的压力降低以及负轴角速度。
- 模式 4，*正向泵*：正轴角速度导致从端口 **A** 到端口
  **B** 的压力升高以及从 **A** 到 **B** 的流动。

马达模块具有解析、查找表和物理信号参数化。当使用表格数据或输入信号进行参数化时，您可以选择
基于效率或损失来表征马达运行。

在表格数据和输入信号参数化选项中，阈值参数 **Pressure drop threshold for motor-pump transition** 和
**Angular velocity threshold for motor-pump transition** 标识了可在马达运行模式之间进行数值平滑流动过渡的区域。选择过渡区域时，
应为过渡项提供一定裕量，但相对于压力和角速度又要足够小，以免影响计算结果。

### 解析泄漏和摩擦参数化

如果将 **Leakage and friction parameterization** 设置为
`Analytical`，则该模块根据轴速度、压降和摩擦扭矩的常数值计算泄漏和摩擦。泄漏流量与马达上的压差相关，
其计算公式为：

m˙leak=KρavgΔp,

其中：

- *Δp* 是 *p*A – *p*B。
- *ρ*avg 是平均流体密度。
- *K* 是解析损失的 Hagen-Poiseuille 系数，

  K=Dωnom(1ηv,nom−1)Δpnom,

  其中：

  - *D* 是 **Displacement** 参数的值。
  - *ωnom* 是 **Nominal shaft angular velocity** 参数的值。
  - *ηv, nom* 是 **Volumetric efficiency at nominal conditions** 参数的值。
- *Δpnom* 是 **Nominal pressure drop** 参数的值。

摩擦扭矩与轴角速度相关，其计算公式为：

τfr=(τ0+k|Δp|)tanh(4ω5×10−5ωnom),

其中：

- *τ*0 是 **No-load torque** 参数的值。
- *k* 是标称排量下的摩擦扭矩与压力增益系数，由 **Mechanical efficiency at nominal conditions** 参数的值
  *ηm* 确定：

  k=τfr,nom−τ0Δpnom.

  *τfric* 是标称条件下的摩擦扭矩：

  τfr,nom=(1−ηm,nom)DΔpnom.
- *Δp* 是端口 **A** 和 **B** 之间的压降。
- *ω* 是相对轴角速度，即 ωR−ωC。

### 表格数据参数化

当使用表格数据表示马达效率或损失时，您可以提供一个或多个马达运行模式的数据。表格数据的符号决定了模块的运行区域。
当提供的数据少于四种运行模式时，模块会通过将给定数据扩展到其余象限来计算其他模式的补充数据。

**表格数据 - 容积效率和机械效率参数化**

泄漏流量为

m˙leak=m˙leak,motor(1+α2)+m˙leak,pump(1−α2),

其中：

- m˙leak,pump=(ηυ−1)m˙ideal
- m˙leak,motor=(1−ηv)m˙

并且 *ηv* 是容积效率，它由用户提供的表格数据插值得到。过渡项 *α* 为

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold),

其中：

- *Δp* 是 *p*A – *p*B。
- *p*threshold 是 **Pressure drop threshold for motor-pump transition** 参数的值。
- *ω* 是 *ω*R – *ω*C。
- *ω*threshold 是 **Angular velocity threshold for motor-pump transition** 参数的值。

摩擦扭矩为

τfr=τfr,motor(1+α2)+τfr,pump(1−α2),

其中：

- τfr,pump=(ηm−1)τ
- τfr,motor=(1−ηm)τideal

并且 *η*m 是机械效率，它由用户提供的表格数据插值得到。

**表格数据 - 容积损失和机械损失参数化**

泄漏流量为

m˙leak=ρavgqloss(Δp,ω),

其中 *qloss* 由 **Volumetric loss table, q\_loss(dp,w)** 参数插值得到，该参数基于用户提供的压降、轴角速度和流体
容积排量数据。

轴摩擦扭矩为

τfr=τloss(Δp,ω)tanh(4ωωthreshold),

其中 *τloss* 由 **Mechanical loss table, torque\_loss(dp,w)** 参数插值得到，该参数基于用户提供的压降和轴角速度
数据。

**表格数据 - 扭矩和速度参数化**

该模块计算容积损失表 *qloss,TLU* 和机械损失表
*τloss,TLU*，如下：

qloss,TLU=qTLU−DωTLUτloss,TLU=DΔpTLU−TTLU

其中：

- *qTLU* 是 **Flow rate vector, q** 参数的值。
- *ωTLU* 是 **Shaft speed table, w(q,dp)** 参数的值。
- *ΔpTLU* 是 **Pressure drop vector, dp** 参数的值。
- *TTLU* 是 **Torque table, T(q,dp)** 参数的值。

如果 **Shaft speed table, w(q,dp)** 和 **Torque table, T(q,dp)** 参数的提供值未覆盖所有四个象限，则该模块通过以下方式扩展数据：

- 对称镜像 **Pressure drop vector, dp** 和 **Flow rate vector, q** 参数的值，使其包含负值。
- 将容积损失表 *qloss,TLU* 的值对称扩展到其他象限。这些扩展值的符号与每个象限中的符号
  *ΔpTLU* 匹配。
- 根据扩展后的流量向量和容积损失表的值计算轴速度向量 *ωTLU* 的扩展值，ωTLU=qTLU−qloss,TLUD。
- 将机械损失表 *τloss,TLU* 的值对称扩展到其他象限。这些扩展值的符号与每个象限中的符号
  *ωTLU* 匹配。

如果您的数据表在四个角中的任意一个角或 **Shaft speed table, w(q,dp)** 或 **Torque table,
T(q,dp)** 参数中有未知数据点，请使用 `NaN` 代替这些值。该模块使用关于压降的最近外插来填充所得容积损失表和机械损失表中的
`NaN` 元素。该模块会调整外插后的机械损失表中的符号，以匹配轴速度向量 *ωTLU* 中对应元素的符号，其中
ωTLU=qTLU−qloss,TLUD。

在扩展或填充未知数据后，该模块在仿真期间使用线性插值和最近外插来计算容积损失表和机械损失表

qloss=tablelookup(qTLU,ΔpTLU,qloss,TLU,Q,Δp,interpolation=linear,extrapolation=nearest)τloss=tablelookup(qTLU,ΔpTLU,τloss,TLU,Q,Δp,interpolation=linear,extrapolation=nearest)

其中 Q=m˙Aρavg。

### 输入信号参数化

当 **Leakage and friction parameterization** 为
`Input signal - volumetric and mechanical efficiencies` 时，端口 **EV** 和
**EM** 启用。内部泄漏和轴摩擦的计算方式与 `Tabulated data - volumetric and
mechanical efficiencies` 参数化相同，不同之处在于
*η*v 和 *η*m 分别直接在端口
**EV** 和 **EM** 处接收。

当 **Leakage and friction parameterization** 为
`Input signal - volumetric and mechanical losses` 时，端口 **LV** 和 **LM** 启用。这些端口
以正物理信号形式接收泄漏流量和摩擦扭矩。泄漏流量计算如下：

m˙leak=ρavgqLVtanh(4Δppthresh),

其中：

- *q*LV 是在端口 **LV** 处接收的泄漏流量。
- *p*thresh 是 **Pressure drop threshold for motor-pump transition** 参数的值。

摩擦扭矩计算如下：

τfr=τLMtanh(4ωωthresh),

其中

- *τ*LM 是在端口 **LM** 处接收的摩擦扭矩。
- *ω*thresh 是 **Angular velocity threshold for motor-pump transition** 参数的值。

容积效率和机械效率在用户定义的最小值和最大值之间。任何低于或高于此范围的值将分别取指定的最小值和最大值。

### 泵运行

马达流量为：

m˙=m˙ideal+m˙leak,

其中 m˙ideal=ρavgD⋅ω。

马达扭矩为：

τ=τideal−τfr,

其中 τideal=D⋅Δp。

由马达轴提取的机械功率为：

φmech=τω,

马达液压功率为：

φhyd=Δpm˙ρavg.

如果您想知道模块是否在所提供的表格数据范围之外运行，可以将 **Check if operating beyond the range
of supplied tabulated data** 设置为 `Warning`，以便在发生这种情况时收到警告，或设置为 `Error`，以便在发生这种情况时停止
仿真。对于通过容积损失或机械损失的输入信号进行参数化的情况，您可以使用 **Check if operating outside of motor mode**
参数在仿真超过运行模式时收到通知。

您还可以监控马达功能。将 **Check if pressures are
less than motor minimum pressure** 设置为
`Warning`，以便在发生这种情况时收到警告，或设置为
`Error`，以便在发生这种情况时停止仿真。

### 预定义参数化

此模块可使用预参数化制造商数据。该数据允许您对特定的供应商组件建模。

要加载预定义参数化，

1. 在模块对话框描述中，单击“选择预定义参数化”超链接。
2. 从下拉菜单中选择一个部件，然后单击 **使用所选部件更新模块**。
3. 如果在加载参数化后更改了任何参数设置，可以通过单击 **将模块设置与所选部件比较** 来检查更改。模块与预定义参数化之间的任何设置差异都将显示在 MATLAB® 命令行窗口中。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。模块用工程判断和简化假设替代缺失数据。因此，预计仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

要了解更多信息，请参阅预参数化组件列表。

### 故障

要对故障建模，请在 **故障** 部分中，单击要建模的故障旁边的 **添加故障** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Simscape 故障简介。

您可以对位移故障、泄漏或轴摩擦力矩故障建模。

当您启用 **位移故障** 参数时，故障触发时，模块按 **故障位移因子** 参数的值缩放位移，

DFault=fDD，

其中 *fD* 是 **故障位移因子** 参数的值。当 **泄漏和摩擦参数化** 参数为 `Analytical` 时，模块不使用故障位移值来计算 Hagen-Poiseuille 系数或摩擦力矩。

当您启用 **泄漏故障** 参数且 **泄漏和摩擦参数化** 为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical efficiencies` 时，故障容积效率为

ηv,Fault=ηvfLeak，

其中 *fLeak* 是 **故障泄漏因子** 参数的值，*ηv* 是容积效率。当 **泄漏和摩擦参数化** 为 `Analytical` 时，模块使用故障容积效率计算 Hagen-Poiseuille 系数。

当 **泄漏和摩擦参数化** 为 `Tabulated data - volumetric and mechanical losses`、`Input signal - volumetric and mechanical losses` 或 `Tabulated data - torque and speed` 时，故障泄漏体积流量为

qLeak,Fault=fLeakqLeak.

当 **泄漏和摩擦参数化** 为 `Tabulated data - torque and speed` 时，模块根据轴转速和扭矩参数计算 *qLeak*。

当您启用 **轴摩擦力矩故障** 参数且 **泄漏和摩擦参数化** 为 `Analytical`、`Tabulated data - volumetric and mechanical efficiencies` 或 `Input signal - volumetric and mechanical efficiencies` 时，故障机械效率为

ηm,Fault=ηmfFriction，

其中 *fFriction* 是 **轴摩擦力矩故障** 参数的值，*ηm* 是机械效率。当 **泄漏和摩擦参数化** 为 `Analytical` 时，模块使用故障机械效率计算摩擦力矩。

当 **泄漏和摩擦参数化** 为 `Tabulated data - volumetric and mechanical losses`、`Input signal - volumetric and mechanical losses` 或 `Tabulated data - torque and speed` 时，故障摩擦力矩为

τFriction,Fault=fFrictionτFriction.

当 **泄漏和摩擦参数化** 为 `Tabulated data - torque and speed` 时，模块根据轴转速和扭矩参数计算 *τLeak*。
