---
type: simulink-block
title: 'Check Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Valves & Orifices / Directional Control Valves'
documentation_page: 'checkvalve2p'
documentation_source_path: 'ref/checkvalve2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Valve (2P)

## 端口

### 守恒端口

### **A** — 流体入口 two-phase fluid

与流体入口端口关联的 two-phase fluid 守恒端口。

### **B** — 流体出口 two-phase fluid

与流体出口端口关联的 two-phase fluid 守恒端口。

## 参数

### **Modeling option** — 流体相的建模选项 `Liquid operating condition`（默认） | `Vapor operating condition`

阀处流体相的建模选项。如果模块位置处的两相流体处于液态，请将此参数设置为 `Liquid operating condition`。如果模块位置处的两相流体处于气态，请将此参数设置为 `Vapor operating condition`。

### 参数

### **Valve parameterization** — 阀门参数化模型 `Linear - Area vs. pressure`（默认） | `Linear - Nominal mass flow rate vs. pressure` | `Tabulated data - Area vs. pressure` | `Cv flow coefficient` | `Kv flow coefficient` | `Orifice area`

模块用于根据阀门两端压差计算质量流量，或根据质量流量计算压差的方法。

当 **Modeling option** 为 `Liquid operating condition` 时，此参数的选项为：

- `Linear - Area vs. pressure`
- `Linear - Nominal mass flow rate vs. pressure`
- `Tabulated data - Area vs. pressure`

当 **Modeling option** 为 `Vapor operating condition` 时，此参数的选项为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Opening pressure specification** — 控制压力 `Pressure differential`（默认） | `Gauge pressure at port A`

控制压力设定：

- 当此参数为 `Pressure differential` 时，当 *pA ̶ pB* 超过 **Cracking pressure differential** 时，阀门打开。
- 当此参数为 `Gauge pressure at port A` 时，当 *pA ̶ patm* 超过 **Cracking pressure (gauge)** 时，阀门打开。

### **Cracking pressure (gauge)** — 开启压力 `0.1` MPa（默认） | positive scalar

阀门压力阈值。当控制压力 *pA ̶ patm* 超过开启压力时，阀门开始打开。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`，并将以下任一项设置为：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Linear`。

### **Maximum opening pressure (gauge)** — 使阀门完全打开的压力 `0.2` MPa（默认） | positive scalar

阀门工作压力，此时阀门完全打开。阀门在开启压力值处开始打开，并在 *pmax* 处完全打开。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`，并将以下任一项设置为：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Linear`。

### **Cracking pressure differential** — 开启压力 `0.01` MPa（默认） | positive scalar

阀门压力阈值。当控制压力 *pA ̶ pB* 超过开启压力时，阀门开始打开。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure differential`，并将以下任一项设置为：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Linear`。

### **Maximum opening pressure differential** — 最大阀门工作压力 `0.1` MPa（默认） | positive scalar

最大阀门工作压力。阀门在开启压力值处开始打开，并在 *pmax* 处完全打开。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure differential`，并将以下任一项设置为：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Linear`。

### **Nominal mass flow rate at maximum valve opening** — 额定质量流量 `0.1` kg/s（默认） | positive scalar

在典型、设计或额定条件下，通过完全打开阀门的质量流量。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **Nominal pressure drop at maximum valve opening** — 额定压降 `0.001` MPa（默认） | positive scalar

在典型、设计或额定条件下，完全打开阀门上的压降。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **Nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认） | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。模块根据 **Nominal inlet pressure** 参数的值和 **Nominal inlet condition specification** 参数的设置，从表格化流体属性数据中确定节流口标称入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **Nominal inlet pressure** — 入口流体压力 `0.101325` MPa（默认） | positive scalar

标称条件下的入口压力。模块根据 **Nominal inlet pressure** 参数的值和 **Nominal inlet condition specification** 参数的设置，从表格化流体属性数据中确定入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **Nominal inlet temperature** — 流体温度 `293.15` K（默认） | positive scalar

标称工况下的入口流体温度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Temperature`。

### **Nominal inlet vapor quality** — 入口蒸汽质量分数 `0`（默认） | positive scalar，取值范围 [0,1]

标称工况下入口混合物的蒸汽质量分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Vapor quality`。

### **Nominal inlet vapor void fraction** — 入口体积分数 `0`（默认） | positive scalar，取值范围 [0,1]

标称工况下入口混合物体积分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Vapor void fraction`。

### **Nominal inlet specific enthalpy** — 入口流体比焓 `400` kJ/kg（默认） | positive scalar

标称工况下的入口比焓。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet specific internal energy** — 入口比内能 `400` kJ/kg（默认） | positive scalar

标称工况下的入口比内能。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Specific internal energy`。

### **Maximum valve area** — 最大阀门开口面积 `1e-4 m^2`（默认） | positive scalar

阀门完全打开时的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear – Area vs. pressure`。

### **Opening pressure differential vector** — 压差向量 `[0.2 : 0.2 : 1.2] MPa`（默认） | 1-by-*n* vector

用于阀门面积表格化参数化的压差值向量。此向量中的值与 **Valve area vector**、**Orifice area vector**、**Cv flow coefficient vector** 或 **Kv flow coefficient vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure differential`，并将以下任一项设置为：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Opening pressure (gauge) vector** — 表压向量 `[0.2 : 0.2 : 1.2] MPa`（默认） | 1-by-*n* vector

用于阀门面积表格化参数化的表压力值向量。此向量中的值与 **Valve area vector**、**Orifice area vector**、**Cv flow coefficient vector** 或 **Kv flow coefficient vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Gauge pressure at port A`，并将以下任一项设置为：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Valve area vector** — 阀门开口面积值向量 `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05] m^2`（默认） | 1-by-*n* vector

用于阀门面积表格化参数化的节流口面积值向量。此向量中的值与 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Discharge coefficient** — 流量系数 `0.64`（默认） | positive scalar

实际流量与理想流量的比值。此参数考虑了节流口方程未涵盖的实际损失。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Valve parameterization** 设置为 `Orifice area`。

### **Pressure recovery** — 是否考虑面积扩张中的压力升高 `off`（默认） | `on`

是否考虑从入口到节流孔压降之后的小幅压力升高。当流体射流离开节流孔时，其耗散并膨胀以充满端口面积，从而导致这一小幅压力升高。当清除 **Pressure recovery** 复选框时，模块不建模此压力升高。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Opening characteristic** — 参数化流通能力度量的方法 `Linear`（默认） | `Tabulated`

根据所选流通能力度量对蒸汽阀门进行参数化的方法。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`。

### **Maximum Cv flow coefficient** — 对应组件最大开度的 *Cv* 系数 `4`（默认） | positive scalar

当可供流动的限制面积最大时 *Cv* 流量系数的值。此参数衡量在压差驱动下蒸汽穿过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 对应成员位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽穿过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应组件最大开度的 *Kv* 系数 `3.6`（默认） | positive scalar

当可供流动的限制面积最大时 *Kv* 流量系数的值。此参数衡量在压差驱动下蒸汽穿过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 对应成员位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的一个值。此参数衡量在压差驱动下蒸汽穿过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 阻塞流时的压差比系数 `0.7`（默认） | positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中首次发生阻塞。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，并将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum orifice area** — 最大阀门开口面积 `1e-4 m^2`（默认） | positive scalar

阀门完全打开时的最大阀门面积。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，将 **阀门参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Linear`。

### **孔口面积向量** — 阀门开启面积值的向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于蒸汽阀门面积的表格化参数化的孔口面积值向量。此向量中的值与 **开启压差向量** 或 **开启压力（表压）向量** 参数中的元素一一对应。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，将 **阀门参数化** 设置为 `Orifice area`，并将 **开启特性** 设置为 `Tabulated`。

### **泄漏流量分数** — 流量比 `1e-6`（默认）| positive scalar

阀门关闭时与开启时的流量之比。

#### 依赖项

要启用此参数，请设置以下任一情况：

- **建模选项** 为 `Liquid operating condition`，且 **阀门参数化** 为 `Linear - Nominal mass flow rate vs. pressure` 或 `Linear - Area vs. pressure`。
- **建模选项** 为 `Vapor operating condition`，且 **开启特性** 为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的 positive scalar

连续平滑因子，当阀门处于接近开启或接近关闭位置时，为流量响应引入一层渐变。将此参数设置为小于 1 的非零值，以提高这些区域中仿真的稳定性。

#### 依赖项

要启用此参数，请设置以下任一情况：

- **建模选项** 为 `Liquid operating condition`，且 **阀门参数化** 为 `Linear - Nominal mass flow rate vs. pressure` 或 `Linear - Area vs. pressure`。
- **建模选项** 为 `Vapor operating condition`，且 **开启特性** 为 `Linear`。

### **入口相变时间常数** — 液体比体积的滞后 `0.1` s（默认）| positive scalar

计算流体比体积时液-汽混合物的时间滞后。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`。

### **层流压力比** — 层流-湍流过渡压力比 `0.999`（默认）| positive scalar

流体在层流和湍流状态之间转换时的阀门出口压力与阀门入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **端口 A 和 B 的横截面积** — 阀门端口面积 `0.01` m^2（默认）| positive scalar

端口 **A** 和 **B** 的面积。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Directional Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024a: 对蒸汽或液体阀门建模

现在，您可以使用 **建模选项** 参数来指定两相流体处于蒸汽或液体状态时的阀门。两个建模选项还包括新的阀门参数化。

当 **建模选项** 为 `Liquid operating condition` 时，您现在可以将 **阀门参数化** 设置为：

- `Linear - Area vs. pressure`
- `Tabulated data - Area vs. pressure`

当 **建模选项** 为 `Vapor operating condition` 时，您现在可以将 **阀门参数化** 设置为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

要保留先前版本的模块行为，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **阀门参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

## 描述

两相流体网络中的止回阀

Check Valve (2P) 模块对两相流体网络中的方向控制止回阀建模。该阀门通过在高于指定压力时打开，并允许流体从端口 **A** 流向端口 **B**，但不允许反向流动，来维持流体压力。开启阀门的压差在 **开启压力设定** 参数中指定。该值可以是端口 **A** 和 **B** 之间的压差，或端口 **A** 处的表压。

**建模选项** 参数控制为蒸汽或液体建模而设计的阀门的参数化选项，但不影响流体属性。该模块根据入口条件计算阀门内部的流体属性。流体与环境之间没有热交换，因此孔口内部的相变仅由于压降或模型中另一部分传播的相变而发生。

### 方向控制

当阀门中的压力 *pcontrol* 超过开启压力 *pcrack* 时，阀门打开。当控制压力达到阀门最大压力 *pmax* 时，阀门完全打开。对于线性参数化，模块计算阀门的开启分数 *λ*，如下：

λ=(1−fleak)(pcontrol−pcrack)(pmax−pcrack)+fleak,

其中：

- *fleak* 是 **泄漏流量分数** 参数的值。
- *pcontrol* 是控制压力，取决于 **开启压力设定** 参数的值。

  当您将 **开启压力设定** 设置为 `Pressure differential` 时，控制压力为 *pA ̶ pB*。

  当您将 **开启压力设定** 设置为 `Gauge pressure at port A` 时，控制压力为端口 **A** 处的压力与大气压力之差。

开启压力和最大压力根据 **开启压力设定** 的设置指定为差值或表压值。如果控制压力超过最大压力，则阀门开启分数为 1。

### 液体阀门

当 **建模选项** 为 `Liquid operating condition` 时，模块参数化取决于 **阀门参数化** 参数的值。对于所有液体参数化选项，模块以相同方式计算压力损失和压力恢复。

临界压差 *Δpcrit* 是流动在层流和湍流之间转换时的压差。对于所有液体参数化，*Δpcrit* 为

Δpcrit=(pA+pB)2(1−Blam),

其中：

- *pA* 和 *pB* 分别是端口 **A** 和 **B** 处的压力。
- *Blam* 是 **层流压力比** 参数的值。

该模块通过使用整个阀门的压力损失与紧邻阀门节流区域两侧的压降之比来考虑压力损失。该比值 *PRloss* 为

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport,

其中：

- *Aport* 是 **端口 A 和 B 的横截面积** 参数的值。
- *Cd* 是 **流量系数** 参数的值。
- *Avalve* 是阀门面积。

压力恢复是由于孔口孔之后面积增加而在阀门中产生的正压力变化。如果您不想捕获此压力增加，请清除 **压力恢复** 复选框。在这种情况下，*PRloss* 为 1，这降低了模型复杂度。如果孔口孔相对于端口面积非常小，或者下一个下游组件靠近该模块且任何射流都没有空间消散，请清除此设置。

**线性 - 标称质量流量与压力参数化**

当您将 **阀门参数化** 设置为 `Nominal Mass Flow Rate vs. pressure` 时，通过阀门的质量流量为

m˙=λm˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25,

其中：

- *Δp* 是阀门上的压降，*pA ̶ pB*。
- m˙nom 是 **最大阀门开度下的标称质量流量** 参数的值。
- *Δpnom* 是 **最大阀门开度下的标称压力降率** 参数的值。
- *vnom* 是标称入口比体积。该模块根据 **标称入口比焓** 和 **标称入口压力** 参数，从表格化流体属性数据中确定此值。
- *vin* 是入口比体积。

**线性 - 面积与压力参数化**

当您将 **阀门参数化** 设置为 `Linear - Area vs. Pressure Parameterization` 时，阀门面积为

Avalve=λAmax,

其中 *Amax* 是 **最大阀门面积** 参数的值。

质量流量为

m˙=CdAvalve2vinPRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4.

当阀门处于接近开启或接近关闭位置时，您可以通过调整 **平滑因子** 参数来保持仿真的数值稳健性。如果 **平滑因子** 参数非零，则模块在 *Aleak* 和 *Amax* 之间平滑地饱和开启面积，其中 *Aleak = fleakAmax*。有关更多信息，请参阅 Numerical Smoothing。

**表格数据 - 面积与压力参数化**

当您将 **阀门参数化** 设置为 `Tabulated data - Area vs. pressure` 时，模块根据 **阀门面积向量** 和 **开启压差向量** 或 **开启压力（表压）向量** 参数对阀门面积进行插值。

该模块使用与 `Linear - Area vs. pressure` 设置相同的方程来计算体积流量。

**流体比体积动态**

对于所有参数化，模块在仿真期间基于液体状态计算流体比体积。

如果阀门入口处的流体是液-汽混合物，则模块计算比体积为

vin=(1−xdyn)vliq+xdynvvap,

其中：

- *xdyn* 是入口蒸汽干度。模块对混合物的入口蒸汽干度应用一阶滞后。
- *vliq* 是流体的液体比体积。
- *vvap* 是流体的蒸汽比体积。

如果入口流体是液体或蒸汽，*vin* 是相应的液体或蒸汽比体积。

如果入口流体是液-汽混合物，模块应用一阶时间滞后，

dxdyndt=xin−xdynτ,

其中：

- *xdyn* 是动态蒸汽干度。
- *xin* 是当前入口蒸汽干度。
- *τ* 是 **入口相变时间常数** 参数的值。

如果入口流体是过冷液体，则 *xin = 0*。如果入口流体是过热蒸汽，则 *xin = 1*。

### 蒸汽阀门

当 **建模选项** 为 `Vapor operating condition` 时，模块行为取决于 **阀门参数化** 和 **开启特性** 参数。

阀门中的流量取决于 **开启特性** 参数：

- `Linear` — 模块将流量容量的度量按 *λ* 缩放，以考虑阀门开启面积。
- `Tabulated` — 模块从 **Cv 流量系数向量**、**Kv 流量系数向量** 或 **孔口面积向量** 参数中对流量容量的度量进行插值。此函数使用一维查找表。

**Cv 流量系数参数化**

当您将 **阀门参数化** 设置为 `Cv flow coefficient` 时，质量流量为

m˙=CvN6Y(pin−pout)vin,

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其值等于 27.3。
- *Y* 是膨胀因子。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *vin* 是入口比体积。

膨胀因子为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 之比。
- *xT* 是 **阻塞流下的 xT 压差比因子** 参数的值。

当压力比 pout/pin 升至 **层流压力比** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

其中

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，阀门变为阻塞流，模块使用以下方程

m˙=23CvN6FγxTpinvin.

**Kv 流量系数参数化**

当您将 **阀门参数化** 设置为 `Kv flow coefficient` 时，模块使用与 `Cv flow coefficient` 参数化相同的方程，但使用关系 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。

**阀门面积参数化**

当您将 **阀门参数化** 设置为 `Orifice area` 时，质量流量为

m˙=CdAvalve2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AvalveAport)2(poutpin)2γ],

其中：

- *γ* 是等熵指数。

当压力比 pout/pin 升至 **层流压力比** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CdAvalve2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AvalveAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，阀门变为阻塞流，模块使用以下方程

m˙=CdAvalve2γγ+1pin1vin1(γ+12)2γ−1−(AvalveAport)2.

### 质量平衡

阀门中的质量守恒，

m˙A+m˙B=0,

其中：

- m˙A 是端口 **A** 处的质量流量。
- m˙B 是端口 **B** 处的质量流量。

### 能量平衡

阀门中的能量守恒，

ΦA+ΦB=0,

其中：

- *ΦA* 是端口 **A** 处的能量流。
- *ΦB* 是端口 **B** 处的能量流。

### 假设和限制

- 阀门与环境之间没有热交换。
- 当 **建模选项** 为 `Liquid operating condition` 时，结果在过冷液体区域之外可能不准确。当 **建模选项** 为 `Vapor operating condition` 时，结果在过热蒸汽区域之外可能不准确。要对液-汽混合物中的阀门建模，请将 **建模选项** 设置为 `Liquid operating condition`。
