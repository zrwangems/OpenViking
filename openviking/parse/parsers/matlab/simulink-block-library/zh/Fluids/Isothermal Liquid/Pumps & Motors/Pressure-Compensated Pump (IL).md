---
type: simulink-block
title: 'Pressure-Compensated Pump (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pumps & Motors'
documentation_page: 'pressurecompensatedpumpil'
documentation_source_path: 'ref/pressurecompensatedpumpil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure-Compensated Pump (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

液体进入或离开泵的入口或出口端口。

### **B** — 液体端口 isothermal liquid

液体进入或离开泵的入口或出口端口。

### **X** — 压力参考 *P*x, MPa isothermal liquid

以 MPa 为单位的控制压力，记为 *P*x。控制压力 *P*x – *P*y 会与 **设定压差** 进行比较，以触发或调节可变泵排量。

### **Y** — 压力参考 *P*y, MPa isothermal liquid

以 MPa 为单位的控制压力，记为 *P*y。控制压力 *P*x – *P*y 会与 **设定压差** 进行比较，以触发或调节可变泵排量。

### **R** — 机械端口 mechanical rotational

旋转轴的角速度和扭矩。

### **C** — 机械端口 mechanical rotational

泵壳体参考角速度和扭矩。

### **EV** — 容积效率 物理信号

用于流体排量的泵效率，指定为物理信号。该值必须介于 0 和 1 之间。

#### 依赖关系

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **EM** — 机械效率 物理信号

用于机械能供应的泵效率，指定为物理信号。该值必须介于 0 和 1 之间。

#### 依赖关系

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **LV** — 泄漏流量, `m^3/s` 物理信号

与流体排量相关的泵损失，以 m3/s 为单位，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical losses`。

### **LM** — 摩擦扭矩, `N*m` 物理信号

与机械能供应相关的泵损失，以 N\*m 为单位，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical losses`。

## 参数

### 泵

### **泄漏和摩擦参数化** — 计算泄漏流量和摩擦扭矩的方法 `Analytical`（默认） | `Tabulated data - volumetric and mechanical efficiencies` | `Tabulated data - volumetric and mechanical losses` | `Input signal - volumetric and mechanical efficiencies` | `Input signal - volumetric and mechanical losses`

泵的泄漏和摩擦特性的参数化。

- 在 `Analytical` 参数化中，泄漏流量和摩擦扭矩通过解析方程计算。
- 在 `Tabulated data - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率根据用户提供的 **压力增益向量, dp**、**轴角速度向量, w** 和 **排量向量, D** 参数计算，并从三维 **容积效率表, e\_v(dp,w,D)** 和 **机械效率表, e\_m(dp,w,D)** 表中插值得到。
- 在 `Tabulated data - volumetric and mechanical losses` 参数化中，泄漏流量和摩擦扭矩根据用户提供的 **压力增益向量, dp**、**轴角速度向量, w** 和 **排量向量, D** 参数计算，并从三维 **容积损失表, q\_loss(dp,w,D)** 和 **机械损失表, torque\_loss(dp,w,D)** 参数中插值得到。
- 在 `Input signal - volumetric and mechanical efficiencies` 参数化中，容积效率和机械效率分别作为物理信号在端口 **EV** 和 **EM** 接收。
- 在 `Input signal - volumetric and mechanical loss` 参数化中，泄漏流量和摩擦扭矩分别作为物理信号在端口 **LV** 和 **LM** 接收。

### **额定排量** — 固定容积流体排量 `30 cm^3/rev`（默认） | 标量

在额定运行条件下轴旋转所排出的流体量。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **额定轴角速度** — 轴角速度 `1800 rpm`（默认） | 标量

额定运行条件下轴的角速度。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **额定压力增益** — 流体入口和出口之间的压力增益 `10 MPa`（默认） | 标量

额定运行条件下流体入口和出口之间的泵压力增益。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **额定工况下的容积效率** — 实际流量与理想流量的比率 `0.92`（默认） | 范围在 (0,1] 的正标量

额定工况下实际流量与理想流量的比率。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **空载扭矩** — 基线扭矩 `0 N*m`（默认） | 标量

克服密封摩擦并引起轴运动所需的最小扭矩值。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **额定工况下的机械效率** — 实际机械功率与理想机械功率的比率 `0.88`（默认） | 正标量

额定工况下实际机械功率与理想机械功率的比率。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Analytical`。

### **压力增益向量, dp** — 用于表格数据参数化的压力数据向量 `[.1, 1, 2] MPa`（默认） | 1-by-*n* 向量

用于泄漏和扭矩摩擦表格参数化的压差值向量。该向量与 **轴角速度向量, w** 和 **排量向量, D** 参数一起，为三维因变量 **容积效率表, e\_v(dp,w,D)** 和 **机械效率表, e\_m(dp,w,D)** 参数形成独立轴。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为以下项之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **轴角速度向量, w** — 用于表格数据参数化的角速度数据向量 `[250, 500, 1000, 2000, 3000, 4000] rpm`（默认） | 1-by-*n* 向量

用于泄漏和扭矩摩擦表格参数化的角速度数据向量。该向量与 **压力增益向量, dp** 和 **排量向量, D** 参数一起，为三维因变量 **容积效率表, e\_v(dp,w,D)** 和 **机械效率表, e\_m(dp,w,D)** 参数形成独立轴。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为以下项之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **排量向量, D** — 用于表格数据参数化的排量体积向量 `[-30, -19, 19, 30] cm^3/s`（默认） | 1-by-*n* 向量

用于泄漏和扭矩摩擦表格参数化的流体容积排量数据向量。该向量与 **轴角速度向量, w** 和 **压力增益向量, dp** 参数一起，为三维因变量 **容积效率表, e\_v(dp,w,D)** 和 **机械效率表, e\_m(dp,w,D)** 参数形成独立轴。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为以下项之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Tabulated data - volumetric and mechanical losses`

### **容积效率表, e\_v(dp,w,D)** — 用于表格数据参数化的容积效率 `repmat([.816, .908, .954, .977, .981, .984; .325, .663, .831, .916, .925, .946; .137, .568, .78, .892, .893, .91], 1, 1, 4)`（默认） | *M*-by-*N*-by-*P* 矩阵

*M*-by-*N*-by-*P* 矩阵，包含在指定流体压力增益、轴角速度和容积排量下的容积效率。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **压力增益向量, dp** 参数中的向量元素数。
- *N* 是 **轴角速度向量, w** 参数中的向量元素数。
- *P* 是 **排量向量, D** 参数中的向量元素数。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **机械效率表, e\_m(dp,w,D)** — 用于表格数据参数化的机械效率 `repmat([.996, .996, .996, .996, .996, .996; .988, .989, .989, .989, .989, .99; .981, .981, .982, .982, .983, .984], 1, 1, 4)`（默认） | *M*-by-*N*-by-*P* 矩阵

*M*-by-*N*-by-*P* 矩阵，包含在指定流体压力增益、轴角速度和排量下的机械效率。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **压力增益向量, dp** 参数中的向量元素数。
- *N* 是 **轴角速度向量, w** 参数中的向量元素数。
- *P* 是 **排量向量, D** 参数中的向量元素数。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical efficiencies`。

### **容积损失表, q\_loss(dp,w,D)** — 用于表格数据参数化的容积损失 `repmat([.023, .023, .023, .023, .0285, .032; .0844, .0842, .0845, .084, .1125, .108; .1079, .108, .11, .108, .1605, .18] * 1e-3, 1, 1, 4)`m^3/s（默认） | 数值数组

*M*-by-*N*-by-*P* 矩阵，包含在指定流体压力增益、轴角速度和排量下的容积泄漏。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **压力增益向量, dp** 参数中的向量元素数。
- *N* 是 **轴角速度向量, w** 参数中的向量元素数。
- *P* 是 **排量向量, D** 参数中的向量元素数。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical loss`。

### **机械损失表, torque\_loss(dp,w,D)** — 用于表格数据参数化的机械损失 `repmat([.002, .002, .002, .002, .002, .002; .0607, .0556, .0556, .0556, .0556, .0505; .1937, .1937, .1833, .1833, .1729, .1626], 1, 1, 4) N*m`（默认） | 数值数组

*M*-by-*N*-by-*P* 矩阵，包含在指定流体压力增益、轴角速度和排量下的摩擦扭矩。表元素之间采用线性插值。*M*、*N* 和 *P* 是相应向量的大小：

- *M* 是 **压力增益向量, dp** 参数中的向量元素数。
- *N* 是 **轴角速度向量, w** 参数中的向量元素数。
- *P* 是 **排量向量, D** 参数中的向量元素数。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Tabulated data - volumetric and mechanical loss`。

### **最小容积效率** — 容积效率的最小值 `1e-3`（默认） | 范围在 (0,1] 的正标量

容积效率的最小值。如果输入信号低于此值，则容积效率设置为最小容积效率。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **最大容积效率** — 容积效率的最大值 `1`（默认） | 范围在 (0,1] 的正标量

容积效率的最大值。如果输入信号高于此值，则容积效率设置为最大容积效率。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **最小机械效率** — 机械效率的最小值 `1e-3`（默认） | 范围在 (0,1] 的正标量

机械效率的最小值。如果输入信号低于此值，则机械效率设置为最小机械效率。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **最大机械效率** — 机械效率的最大值 `1`（默认） | 范围在 (0,1] 的正标量

机械效率的最大值。如果输入信号高于此值，则机械效率设置为最大机械效率。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为 `Input signal - volumetric and mechanical efficiencies`。

### **泵-马达转换的压力增益阈值** — 模式转换的压力阈值 `1e-3 MPa`（默认） | 正标量

用于在泵和马达功能之间转换的阈值压力增益值。在压力增益阈值的正值和负值之间围绕 0 MPa 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦扭矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为以下项之一：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical losses`

### **泵-马达转换的角速度阈值** — 模式转换的角速度阈值 `100 rpm`（默认） | 正标量

用于在马达和泵功能之间转换的阈值角速度值。在角速度阈值的正值和负值之间围绕 0 rpm 定义了一个过渡区域。在该过渡区域内，计算得到的泄漏流量和摩擦扭矩根据过渡项 *α* 进行调整，以确保从一种模式平滑过渡到另一种模式。

#### 依赖关系

要启用此参数，请将 **泄漏和摩擦参数化** 设置为：

- `Tabulated data - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical efficiencies`
- `Input signal - volumetric and mechanical loss`

### **检查是否超出提供的表格数据范围运行** — 是否在超出提供的数据范围时发出通知 `None`（默认） | `Warning` | `Error`

是否在超出所提供数据的范围时发出通知。选择 `Warning` 可在模块使用超出所提供数据范围的值时收到通知。选择 `Error` 可在模块使用超出所提供数据范围的值时停止仿真。

#### 依赖项

要启用此参数，请将 **Leakage and friction
parameterization** 设置为：

- `Tabulated data - volumetric and
  mechanical efficiencies`
- `Tabulated data - volumetric and
  mechanical losses`

### **Check if operating beyond pump mode** — 是否在模块运行于泵模式功能之外时发出通知 `None`（默认） | `Warning` | `Error`

是否在模块运行于泵模式功能之外时发出通知。选择 `Warning` 以在模块运行于正向或反向马达模式时收到通知。选择 `Error` 以在模块运行于正向或反向马达模式时停止仿真。

#### 依赖项

要启用此参数，请将 **Leakage and friction
parameterization** 设置为 `Input signal -
volumetric and mechanical losses`。

### **Check if pressures are less than pump minimum pressure** — 是否在流体出口压力过低时发出通知 `None`（默认） | `Warning` | `Error`

是否在端口 **A** 或 **B** 处的流体经历低压时发出通知。选择 `Warning` 以在出口压力降至指定的最小值以下时收到通知。选择 `Error` 以在出口压力降至指定的最小值以下时停止仿真。

当流体压力降至流体蒸气压以下时，该参数有助于识别可能发生气蚀的条件。

### **Pump minimum pressure** — 泵出口可接受压力的下限 `0.101325 MPa`（默认） | 正标量

泵入口或出口可接受压力的下限。

#### 依赖项

要启用此参数，请将 **Check if pressures are less than pump minimum pressure** 设置为：

- `Warning`
- `Error`

### 压力补偿

### **Maximum displacement** — 泵排量上限 `30 cm^3/rev`（默认） | 标量

泵排量上限。

### **Minimum displacement** — 泵排量下限 `0.1 cm^3/rev`（默认） | 标量

泵排量下限。

### **Set pressure differential** — 变排量功能的阈值 `10 MPa`（默认） | 正标量

超过该阈值后，泵排量会被调整。

### **Pressure regulation range** — 变排量运行范围 `0.6 MPa`（默认） | 正标量

变排量运行范围。泵在 **Set pressure differential** 与泵最大压力之间运行，泵最大压力为 *pset +
pregulation*。

### **Displacement dynamics** — 是否考虑流量对排量变化的响应 `off`（默认） | `on`

是否考虑由于泵流体排量变化而对流体系统产生的瞬态效应。选择 **Displacement dynamics** 会通过在流量响应中引入一阶滞后近似该条件变化。**Time constant** 的大小也会影响所建模的排量动态。

### **Time constant** — 流量响应时间常数 `0.1 s`（默认） | 正标量

该常数表示改变流体排量时流体达到稳态所需的时间。此参数影响所建模的排量动态。

#### 依赖项

要启用此参数，请选择 **Displacement dynamics**。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pumps & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a: 检查模块是否在计算数据范围之外运行

参数 **Check if operating beyond the octants of supplied tabulated data** 已重命名为 **Check if operating beyond the range of supplied tabulated data**。您可以启用 **Check if operating beyond the range of supplied tabulated data** 参数来检查模块是否在模块参数指定的数据范围之外运行，即运行在模块已扩展数据的区域中。

## 描述

等温液体网络中的恒压变排量泵

Pressure-Compensated Pump (IL) 模块对等温液体网络中的恒压变排量泵进行建模。泵排量由端口 **X** 和 **Y** 之间测得的压差 *pcontrol* 控制。当该压力超过 **Set pressure differential** 时，流体排量根据泵的 **Leakage and friction parameterization** 进行调整。变排量功能在 **Pressure regulation range** 内发生，该范围位于 *pset* 处的 **Maximum displacement** 与 *pmax* 处的 **Minimum displacement** 之间。

流体可以从端口 **A** 流向端口 **B**，称为*正向模式*，或者从端口 **B** 流向端口 **A**，称为*反向模式*。当沿流动方向存在压力增益时，发生泵模式运行。当沿流动方向存在压力降时，发生马达模式运行。

轴旋转对应于流经泵的流体体积的符号。正流体排量对应于正向模式下的正轴旋转。负流体排量对应于正向模式下的负轴角速度。

**运行模式**

该模块有八种运行模式。工作模式取决于从端口 **A** 到端口 **B** 的压力增益 *Δp =
p*B – *p*A；角速度 *ω = ω*R – *ω*C；以及由压差设定的流体体积排量。上图将这些模式映射到 *Δp*-*ω*-*D* 图的八分区：

- 模式 1，*正向泵*：正轴角速度导致从端口 **A** 到端口 **B** 的压力增加，以及从端口 **A** 到端口 **B** 的流动。
- 模式 2，*反向马达*：从端口 **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力降低和负轴角速度。
- 模式 3，*反向泵*：负轴角速度导致从端口 **B** 到端口 **A** 的压力增加，以及从 **B** 到 **A** 的流动。
- 模式 4，*正向马达*：从端口 **A** 到 **B** 的流动导致从 **A** 到 **B** 的压力降低和正轴角速度。
- 模式 5，*反向马达*：从端口 **B** 到端口 **A** 的流动导致从 **B** 到 **A** 的压力降低和正轴角速度。
- 模式 6，*正向泵*：负轴角速度导致从 **A** 到 **B** 的压力增加，以及从 **A** 到 **B** 的流动。
- 模式 7，*正向马达*：从端口 **A** 到 **B** 的流动导致从 **A** 到 **B** 的压力降低和负轴角速度。
- 模式 8，*反向泵*：正轴角速度导致从端口 **B** 到端口 **A** 的压力增加，以及从 **B** 到 **A** 的流动。

该模块具有解析、查找表和物理信号参数化。使用表格数据或输入信号进行参数化时，您可以选择基于效率或损失来表征泵运行。

阈值参数 **Pressure gain threshold for pump-motor transition**、**Angular velocity threshold for pump-motor transition** 和 **Displacement threshold for pump-motor transition** 标识了泵运行模式之间可发生数值平滑流量过渡的区域。对于压力阈值和角速度阈值，请选择为过渡项提供一定裕量、但相对于典型泵压力增益和角速度足够小以致不会影响计算结果的过渡区域。对于排量阈值，请选择小于正常运行期间典型排量体积的阈值。

### 解析泄漏和摩擦参数化

如果您将 **Leakage and friction parameterization** 设置为 `Analytical`，则该模块根据轴速度、压力增益和转矩的常数值计算泄漏和摩擦。与泵两端压差相关的泄漏流量按下式计算：

m˙leak=KρavgΔp,

其中：

- *Δp*nom 是
  *p*B –
  *p*A。
- *ρ*avg 是平均流体
  密度。
- *K* 是用于解析损失的 Hagen-Poiseuille 系数，

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

与泵压差相关的摩擦转矩按下式计算：

τfr=(τ0+k|ΔpDDnom|)tanh(4ω5×10−5ωnom),

其中：

- *τ*0 是 **No-load
  torque**。
- *k* 是标称排量下的摩擦转矩与压力增益系数，由 **Mechanical
  efficiency at nominal conditions** *ηm,nom* 确定：

  k=τfr,nom−τ0Δpnom.

  *τfr,nom* 是
  标称条件下的摩擦转矩：

  τfr,nom=(1−ηm,nomηm,nom)DnomΔpnom.
- *ω* 是相对轴角速度，或 ωR−ωC。

### 表格数据参数化

使用表格数据表示泵效率或损失时，您可以为一个或多个泵运行模式提供数据。表格数据的符号决定模块的运行区域。当提供的数据少于八个运行模式时，模块通过将给定数据扩展到其余八分区来计算其他模式的补充数据。

**`Tabulated data - volumetric and mechanical
efficiencies` 参数化**

泄漏流量按下式计算：

m˙leak=m˙leak,pump(1+α2)+m˙leak,motor(1−α2),

其中：

- m˙leak,pump=(1−ηυ)m˙ideal
- m˙leak,motor=(ηv−1)m˙

并且 *η*v 是体积效率，它从用户提供的表格数据中插值得到。过渡项 *α* 为

α=tanh(4ΔpΔpthreshold)tanh(4ωωthreshold)tanh(4DDthreshold),

其中：

- *Δp* 是
  *p*B –
  *p*A。
- *p*threshold 是
  **Pressure gain threshold for pump-motor
  transition**。
- *ω* 是
  *ω*R –
  *ω*C。
- *ω*threshold 是
  **Angular velocity threshold for pump-motor
  transition**。

摩擦转矩按下式计算：

τfr=τfr,pump(1+α2)+τfr,motor(1−α2),

其中：

- τfr,pump=(1−ηm)τ
- τfr,motor=(ηm−1)τideal

并且 *η*m 是机械效率，它从用户提供的表格数据中插值得到。

**`Tabulated data - volumetric and mechanical
losses` 参数化**

泄漏流量按下式计算：

m˙leak=ρavgqloss(Δp,ω,D),

其中 *q*loss 从 **Volumetric loss table, q\_loss(dp,w,D)** 参数插值得到，该参数基于用户提供的压力增益、轴角速度和流体体积排量数据。

轴摩擦转矩按下式计算：

τfr=τloss(Δp,ω,D),

其中 *τ*loss 从 **Mechanical loss table, torque\_loss(dp,w,D)** 参数插值得到，该参数基于用户提供的压力增益、轴角速度和流体体积排量数据。

### 输入信号参数化

当您选择 `Input signal - volumetric and mechanical
efficiencies` 时，端口 **EV** 和 **EM** 会启用。内部泄漏和轴摩擦的计算方式与 `Tabulated data - volumetric and
mechanical efficiencies` 参数化相同，不同之处在于 *η*v 和 *η*m 分别直接在端口 **EV** 和 **EM** 处接收。

当您选择 `Input signal - volumetric and mechanical
losses` 时，端口 **LV** 和 **LM** 会启用。这些端口接收作为正物理信号的泄漏流量和摩擦转矩。泄漏流量按下式计算：

m˙leak=ρavgqLVtanh(4Δppthresh),

其中：

- *q*LV 是在端口 **LV** 处
  接收的泄漏流量。
- *p*thresh 是
  **Pressure gain threshold for pump-motor
  transition** 参数。

摩擦转矩按下式计算：

τfr=τLMtanh(4ωωthresh),

其中

- *τ*LM 是在端口 **LM** 处
  接收的摩擦转矩。
- *ω*thresh 是
  **Angular velocity threshold for pump-motor
  transition** 参数。

体积效率和机械效率介于用户定义的指定最小值和最大值之间。低于或高于此范围的值将分别取指定的最小值和最大值。

### 泵运行

泵流量为：

m˙=m˙ideal−m˙leak,

其中 m˙ideal=ρavgD⋅ω。

泵转矩为：

τ=τideal+τfr,

其中 τideal=D⋅Δp。

泵轴传递的机械功率为：

φmech=τω,

泵液压功率为：

φhyd=Δpm˙ρavg.

若要在模块运行超出提供的表格数据时收到通知，请将 **Check if operating beyond the range of supplied tabulated data** 设置为 `Warning`，以便在发生此情况时收到警告；或设置为 `Error`，以便在发生此情况时停止仿真。对于通过输入信号对体积损失或机械损失进行参数化，您可以使用 **Check if operating beyond pump mode** 参数在仿真超过运行模式时收到通知。

您还可以监测泵功能。将 **Check if pressures are less than pump minimum pressure** 设置为 `Warning`，以便在发生此情况时收到警告；或设置为 `Error`，以便在发生此情况时停止仿真。

### 排量参数化

泵排量的线性参数化为：

D=p^(Dmin−Dmax)+Dmax,

其中归一化压力 p^ 为

p^=pcontrol−psetpmax−pset.

其中 *pmax* 是 **Set pressure differential** 与 **Pressure regulation range** 之和。

### 排量动态

如果对排量动态进行建模，则会在针对所建模控制压力的流量响应中引入滞后。*p*control 变为动态控制压力 *p*dyn；否则 *p*control 为稳态压力。动态控制压力的瞬时变化基于 **Time constant** *τ* 计算：

p˙dyn=pcontrol−pdynτ.

默认情况下，**Displacement dynamics** 复选框未选中。

### 数值平滑压力

您可以通过调整 **Smoothing factor** 参数来在仿真中保持数值稳健性。如果 **Smoothing factor** 参数非零，则模块会在 *pset* 和 *pmax* 之间平滑饱和归一化控制压力。有关详细信息，请参阅 Numerical Smoothing。
