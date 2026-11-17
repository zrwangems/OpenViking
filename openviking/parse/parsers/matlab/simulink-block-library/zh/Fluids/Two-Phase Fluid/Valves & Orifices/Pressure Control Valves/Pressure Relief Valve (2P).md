---
type: simulink-block
title: 'Pressure Relief Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalve2p'
documentation_source_path: 'ref/pressurereliefvalve2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Relief Valve (2P)

## 端口

### 守恒端口

### **A** — 流体入口或出口两相流体

与流体入口或出口端口关联的两相流体守恒端口。

### **B** — 流体入口或出口两相流体

与流体入口或出口端口关联的两相流体守恒端口。

### 输入

### **Ps** — 设定压力，Pa 物理信号

用于变化设定压力信号的输入端口。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。

## 参数

### **Modeling option** — 流体相的建模选项 `Liquid operating condition`（默认）| `Vapor operating condition`

阀门处流体相的建模选项。如果模块位置处的两相流体处于液态，请将此参数设置为 `Liquid operating condition`。如果模块位置处的两相流体处于气态，请将此参数设置为 `Vapor operating condition`。

### 参数

### **Valve parameterization** — 阀门参数化模型 `Linear - Area vs. pressure`（默认）| `Linear - Nominal mass flow rate vs. pressure` | `Tabulated data - Area vs. pressure` | `Cv flow coefficient` | `Kv flow coefficient` | `Orifice area`

模块用于根据阀门两端压差计算质量流量或根据质量流量计算压差的方法。

当 **Modeling option** 为 `Liquid operating condition` 时，此参数的选项为：

- `Linear - Area vs. pressure`
- `Linear - Nominal mass flow rate vs. pressure`
- `Tabulated data - Area vs. pressure`

当 **Modeling option** 为 `Vapor operating condition` 时，此参数的选项为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Opening pressure specification** — 控制压力 `Pressure differential`（默认）| `Gauge pressure at port A`

控制压力规格：

- 当此参数为 `Pressure differential` 时，当 *pA ̶ pB* 超过 **Set pressure differential** 时阀门打开。
- 当此参数为 `Gauge pressure at port A` 时，当 *pA ̶ patm* 超过 **Set pressure (gauge)** 时阀门打开。

### **Set pressure control** — 可变或恒定设定压力 `Constant`（默认）| `Controlled`

压力阈值是恒定的还是可变的。将此参数设置为 `Controlled` 会暴露物理信号端口 **Ps**。

### **Set pressure differential** — 设定压力 `0.01` MPa（默认）| 正标量

阀门压力阈值。当控制压力 *pA ̶ pB* 超过设定压力时，阀门开始打开。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure differential`，将 **Set pressure control** 设置为 `Constant`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition` 且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition` 且 **Opening characteristic** 设置为 `Linear`。

### **Set pressure (gauge)** — 设定压力 `0.1` MPa（默认）| 正标量

阀门压力阈值。当控制压力 *pA ̶ patm* 超过设定压力时，阀门开始打开。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`，将 **Set pressure control** 设置为 `Constant`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition` 且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition` 且 **Opening characteristic** 设置为 `Linear`。

### **Pressure regulation range** — 阀门工作范围 `0.1` MPa（默认）| 正标量

阀门工作范围。阀门在设定压力值处开始打开，在 *pmax* 处完全打开，*pmax* 为压力调节范围的终点，其中 *pmax = pset + prange*。

#### 依赖关系

要启用此参数，请设置以下任一选项：

- **建模选项**设为
  `Liquid operating
  condition`，并将**阀门参数化**设为
  `Linear -
  Area vs. pressure` 或
  `Linear - Nominal mass flow rate vs.
  pressure`。
- **建模选项**设为
  `Vapor operating condition`，
  并将**开度特性**设为
  `Linear`。

### **最大阀门开度下的额定质量流量** — 额定质量流量 `0.1` kg/s（默认）| 正标量

在典型、设计或额定工况下，通过全开阀门的质量流量。

#### 依赖关系

要启用此参数，请将**建模选项**设为
`Liquid operating condition`，并将
**阀门参数化**设为
`Linear - Nominal mass flow rate vs.
pressure`。

### **最大阀门开度下的额定压降** — 额定压降 `0.001` MPa（默认）| 正标量

在典型、设计或额定工况下，全开阀门两端的压降。

#### 依赖关系

要启用此参数，请将**建模选项**设为
`Liquid operating condition`，并将
**阀门参数化**设为
`Linear - Nominal mass flow rate vs.
pressure`。

### **额定入口条件规格** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。该模块根据**额定入口压力**参数的值以及**额定入口条件规格**参数的设置，从表格化的流体属性数据中确定孔口额定入口比容。

#### 依赖关系

要启用此参数，请将**建模选项**设为
`Liquid operating condition`，并将
**阀门参数化**设为
`Linear - Nominal mass flow rate vs.
pressure`。

### **额定入口压力** — 入口流体压力 `0.101325` MPa（默认）| 正标量

额定条件下的入口压力。该模块根据**额定入口压力**参数的值以及**额定入口条件规格**参数的设置，从表格化的流体属性数据中确定入口比容。

#### 依赖关系

要启用此参数，请将**建模选项**设为
`Liquid operating condition`，并将
**阀门参数化**设为
`Linear - Nominal mass flow rate vs.
pressure`。

### **额定入口温度** — 流体温度 `293.15` K（默认）| 正标量

额定运行条件下的入口流体温度。

#### 依赖关系

要启用此参数，请将**建模选项**设为
`Liquid operating condition`，
**阀门参数化**设为
`Linear - Nominal mass flow rate vs.
pressure`，并将**额定入口条件规格**设为
`Temperature`。

### **额定入口蒸汽干度** — 入口蒸汽干度质量分数 `0`（默认）| [0,1] 范围内的正标量

额定运行条件下入口混合物的蒸汽干度质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将**建模选项**设为
`Liquid operating condition`，
**阀门参数化**设为
`Linear - Nominal mass flow rate vs.
pressure`，并将**额定入口条件规格**设为 `Vapor
quality`。

### **额定入口蒸汽空隙率** — 入口体积分数 `0`（默认）| [0,1] 范围内的正标量

额定运行条件下入口混合物的体积分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将**建模选项**设为
`Liquid operating condition`，
**阀门参数化**设为
`Linear - Nominal mass flow rate vs.
pressure`，并将**额定入口条件规格**设为 `Vapor void
fraction`。

### **Nominal inlet specific enthalpy** — 入口流体比焓 `400` kJ/kg（默认）| 正标量

额定工况下的入口比焓。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet specific internal energy** — 入口比内能 `400` kJ/kg（默认）| 正标量

额定工况下的入口比内能。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Specific internal energy`。

### **Maximum valve area** — 最大阀门开度面积 `1e-4 m^2`（默认）| 正标量

阀门完全打开时的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear – Area vs. pressure`。

### **Opening pressure differential vector** — 压差向量 `[0.2 : 0.2 : 1.2] MPa`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的压差值向量。此向量中的值与 **Valve area vector**、**Orifice area vector**、**Cv flow coefficient vector** 或 **Kv flow coefficient vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure differential`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Opening pressure (gauge) vector** — 表压向量 `[0.2 : 0.2 : 1.2] MPa`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的表压值向量。此向量中的值与 **Valve area vector**、**Orifice area vector**、**Cv flow coefficient vector** 或 **Kv flow coefficient vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`
- **Modeling option** 设置为 `Vapor operating condition`，**Valve parameterization** 设置为 `Orifice area`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Valve area vector** — 阀门开度面积值向量 `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的节流孔面积值向量。此向量中的值与 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

实际流量与理想流量之比。此参数用于考虑节流孔方程中未涵盖的实际损失。

#### 依赖关系

要启用此参数，请满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Valve parameterization** 设置为 `Orifice area`。

### **压力恢复** — 是否考虑面积扩大时的压力升高 `off`（默认）| `on`

是否考虑从入口到孔口处压降之后压力的微小上升。当流体射流离开孔口时，它会耗散并膨胀以充满端口面积，从而导致这一微小压力上升。当您清除 **Pressure recovery** 复选框时，该模块不会对此压力升高进行建模。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **开启特性** — 用于参数化流量能力度量的方法 `Linear`（默认）| `Tabulated`

用于为所选流量能力度量参数化蒸汽阀的方法。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`。

### **最大 Cv 流量系数** — 对应于组件最大开启状态的 *Cv* 系数 `4`（默认）| 正标量

当可用于流动的节流面积达到最大值时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv 流量系数向量** — 对应于构件位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应于 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **最大 Kv 流量系数** — 对应于组件最大开启状态的 *Kv* 系数 `3.6`（默认）| 正标量

当可用于流动的节流面积达到最大值时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv 流量系数向量** — 对应于构件位置向量中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **阻塞流下的 xT 压差比因子** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中首次发生阻塞。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，并将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum orifice area** — 最大阀门开度面积 `1e-4 m^2`（默认）| 正标量

阀门完全打开时的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Orifice area vector** — 阀门开度面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 1×*n* 向量

用于蒸汽阀门面积表格化参数化的孔口面积值向量。此向量中的值与 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

阀门关闭时的流量与打开时的流量之比。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure` 或 `Linear - Area vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值，以提高这些区域内仿真的稳定性。

#### 依赖关系

要启用此参数，请设置以下任一组合：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure` 或 `Linear - Area vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Linear`。

### **Inlet phase change time constant** — 液体比容滞后 `0.1` s（默认）| 正标量

计算流体比容时液-汽混合物的时间滞后。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`。

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

流体在层流和湍流状态之间过渡时的阀门出口压力与阀门入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **端口 A 和 B 处的横截面积** — 阀门端口面积 `0.01` m^2（默认）| 正标量

端口 **A** 和 **B** 的面积。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024a: 为蒸汽或液体阀门建模

您现在可以使用 **Modeling option** 参数来指定当两相流体处于蒸汽或液体状态时的阀门。两种建模选项也都包含新的阀门参数化方式。

当 **Modeling option** 为 `Liquid operating condition` 时，您现在可以将 **Valve parameterization** 设置为：

- `Linear - Area vs. pressure`
- `Tabulated data - Area vs. pressure`

当 **Modeling option** 为 `Vapor operating condition` 时，您现在可以将 **Valve parameterization** 设置为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

若要保留之前版本的模块行为，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

## 描述

两相流体网络中的泄压阀

Pressure Relief Valve (2P) 模块用于对两相流体网络中的压力控制泄压阀进行建模。当压力超过设定压力时，阀门打开。在 **Set pressure specification** 参数中指定使阀门打开的压力差，该压力差可以是端口 **A** 和 **B** 之间的压差，也可以是端口 **A** 处的表压。当您将 **Set pressure control** 设置为 `Controlled` 时，设定压力会根据端口 **Ps** 处的输入信号而变化。

**Modeling option** 参数控制用于蒸汽或液体建模的阀门参数化选项，但不影响流体属性。该模块根据入口条件计算阀门内部的流体属性。流体与环境之间没有热交换，因此孔口内部的相变仅由压降或模型中其他部分传播的相变引起。

### 压力控制

当阀门中的压力 *pcontrol* 超过设定压力 *pset* 时，阀门打开。当控制压力达到 *pset* + *prange* 时，阀门完全打开，其中 *prange* 是 **Pressure regulation range** 参数的值。

对于线性参数化，该模块计算阀门的开度分数 *λ*。当您将 **Set pressure control** 设置为 `Constant` 时，*λ* 为

λ=(1−fleak)(pcontrol−pset)prange+fleak，

其中：

- *fleak* 是 **Leakage flow fraction** 参数的值。
- *pcontrol* 是控制压力，取决于 **Set pressure specification** 参数的值。

  当您将 **Set pressure specification** 设置为 `Pressure differential` 时，控制压力为 *pA ̶ pB*。

  当您将 **Set pressure specification** 设置为 `Gauge pressure at port A` 时，控制压力是端口 **A** 处压力与大气压力之间的差值。
- *pset* 是设定压力，取决于 **Set pressure specification** 参数的值。

  当您将 **Set pressure specification** 设置为 `Pressure differential` 时，*pset* 是 **Set pressure differential** 参数的值。

  当您将 **Set pressure specification** 设置为 `Gauge pressure at port A` 时，*pset* 是 **Set pressure (gauge)** 参数的值。

当您将 **Set pressure control** 设置为 `Controlled` 时，阀门开度分数为

λ=(1−fleak)(pcontrol−ps)prange+fleak，

其中 *ps* 是端口 **Ps** 处信号的值。如果控制压力超过阀门压力调节范围，则阀门开度分数为 1。

### Liquid Valve

当 **Modeling option** 为 `Liquid operating
condition` 时，模块参数化取决于
**Valve parameterization** 参数的值。对于所有液体参数化选项，模块以相同方式计算
压力损失和压力恢复。

临界压差，
*Δpcrit*，是流动在层流和湍流之间过渡时的压差。对于所有液体
参数化，*Δpcrit* 为

Δpcrit=(pA+pB)2(1−Blam),

其中：

- *pA* 和
  *pB* 分别是端口 **A** 和 **B** 处的压力。
- *Blam* 是
  **Laminar flow pressure ratio** 参数的值。

模块通过使用整个阀门上的压力损失与紧邻阀门节流面积处的压降之比来考虑压力损失。这个
比值 *PRloss* 为

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport,

其中：

- *Aport* 是
  **端口 A 和 B 处的横截面积**
  参数的值。
- *Cd* 是
  **Discharge coefficient** 参数的值。
- *Avalve* 是阀门
  面积。

压力恢复是由于孔口后面积增加而在阀门中产生的正压力变化。如果你不想捕捉这种压力
增加，请清除 **Pressure recovery** 复选框。在这种
情况下，*PRloss* 为 1，这会降低模型
复杂度。如果孔口相对于
端口面积相当小，或者如果紧邻的下游组件靠近该模块并且任何射流
没有空间耗散，请清除此设置。

**Linear - Nominal Mass Flow Rate vs. Pressure Parameterization**

当你将 **Valve Parameterization** 设置为
`Nominal mass flow rate vs. pressure` 时，通过
阀门的质量流量为

m˙=λm˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25,

其中：

- *Δp* 是阀门上的压降，
  *pA ̶
  pB*。
- m˙nom 是 **Nominal mass flow
  rate at maximum valve opening** 参数的值。
- *Δpnom* 是
  **Nominal pressure drop rate at maximum valve
  opening** 参数的值。
- *vnom* 是标称
  入口比体积。模块根据 **Nominal inlet
  specific enthalpy** 和 **Nominal inlet
  pressure** 参数，从表格化流体属性数据中确定此值。
- *vin* 是入口
  比体积。

**Linear - Area vs. Pressure Parameterization**

当你将 **Valve parameterization** 设置为
`Linear - area vs. pressure` 时，阀门面积为

Avalve=λAmax,

其中 *Amax* 是
**Maximum valve area** 参数的值。

质量流量为

m˙=CdAvalve2vinPRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4.

当阀门处于接近打开或接近关闭位置时，
你可以通过调整
**Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果
**Smoothing factor** 参数非零，模块
会在
*Aleak* 和
*Amax* 之间平滑地饱和开口面积，其中
*Aleak =
fleakAmax*。有关
更多信息，请参阅 Numerical Smoothing。

**Tabulated Data - Area vs. Pressure Parameterization**

当你将 **Valve Parameterization** 设置为
`Tabulated data - area vs. pressure` 时，模块
从 **Valve area vector** 和
**Opening pressure differential vector** 或
**Opening pressure (gauge) vector** 参数中插值得到阀门面积。

模块使用与 `Linear - Area vs.
pressure` 设置相同的方程来计算体积流量。

**Fluid Specific Volume Dynamics**

对于所有参数化，模块在仿真期间基于液体状态计算流体比体积。

如果阀门入口处的流体是液-汽混合物，模块
将比体积计算为

vin=(1−xdyn)vliq+xdynvvap,

其中：

- *xdyn* 是入口蒸汽
  质量分数。模块对混合物的入口蒸汽
  质量分数应用一阶滞后。
- *vliq* 是流体的液体
  比体积。
- *vvap* 是流体的蒸汽
  比体积。

如果入口流体为液体或蒸汽，*vin* 为相应的液体或蒸汽比容。

如果入口蒸汽干度为液-汽混合物，该模块应用一阶时间滞后，

dxdyndt=xin−xdynτ,

其中：

- *xdyn* 为动态蒸汽干度。
- *xin* 为当前入口蒸汽干度。
- *τ* 为 **Inlet phase change time constant** 参数的值。

如果入口流体为过冷液体，*xin = 0*。如果入口流体为过热蒸汽，*xin = 1*。

### Vapor Valve

当 **Modeling option** 为 `Vapor operating condition` 时，模块行为取决于 **Valve parameterization** 和 **Opening characteristic** 参数。

阀门中的流量取决于 **Opening characteristic** 参数：

- `Linear` — 模块将流量容量的度量按 *λ* 缩放，以考虑阀门开口面积。
- `Tabulated` — 模块从 **Cv flow coefficient vector**、**Kv flow coefficient vector** 或 **Orifice area vector** 参数中插值得到流量容量的度量。此函数使用一维查找表。

**Cv Flow Coefficient Parameterization**

当您将 **Valve parametrization** 设置为 `Cv flow coefficient` 时，质量流量为

m˙=CvN6Y(pin−pout)vin,

其中：

- *Cv* 为流量系数。
- *N6* 为常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值等于 27.3。
- *Y* 为膨胀系数。
- *pin* 为入口压力。
- *pout* 为出口压力。
- *vin* 为入口比容。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 为等熵指数与 1.4 的比值。
- *xT* 为 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，阀门变为阻塞状态，模块使用以下方程

m˙=23CvN6FγxTpinvin.

**Kv Flow Coefficient Parameterization**

当您将 **Valve parametrization** 设置为 `Kv flow coefficient` 时，模块使用与 `Cv flow coefficient` 参数化相同的方程，但使用关系式 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。

**Valve Area Parameterization**

当您将 **Valve parametrization** 设置为 `Orifice area` 时，质量流量为

m˙=CdAvalve2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AvalveAport)2(poutpin)2γ],

其中：

- *Cd* 为 **Discharge coefficient** 参数的值。
- *γ* 为等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数的值 *Blam* 以上时，模块平滑过渡到方程的线性化形式，

m˙=CdAvalve2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AvalveAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，阀门变为阻塞状态，模块使用以下方程

m˙=CdAvalve2γγ+1pin1vin1(γ+12)2γ−1−(AvalveAport)2.

### Mass Balance

阀门中质量守恒，

m˙A+m˙B=0,

其中：

- m˙A 为端口 **A** 处的质量流量。
- m˙B 为端口 **B** 处的质量流量。

### Energy Balance

阀门中能量守恒，

ΦA+ΦB=0,

其中：

- *ΦA* 为端口 **A** 处的能量流。
- *ΦB* 为端口 **B** 处的能量流。

### 假设和限制

- 阀门与环境之间无热交换。
- 当 **Modeling option** 为 `Liquid operating condition` 时，结果在过冷液体区域之外可能不准确。当 **Modeling option** 为 `Vapor operating condition` 时，结果在过热蒸汽区域之外可能不准确。要对液-汽混合物中的阀门进行建模，请将 **Modeling option** 设置为 `Liquid operating condition`。
