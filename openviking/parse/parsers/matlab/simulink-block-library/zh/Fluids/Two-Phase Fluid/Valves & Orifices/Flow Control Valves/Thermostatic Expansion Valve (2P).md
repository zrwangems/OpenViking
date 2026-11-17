---
type: simulink-block
title: 'Thermostatic Expansion Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Valves & Orifices / Flow Control Valves'
documentation_page: 'thermostaticexpansionvalve2p'
documentation_source_path: 'ref/thermostaticexpansionvalve2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermostatic Expansion Valve (2P)

## 端口

### 守恒端口

### **A** — 流体入口 两相流体

阀入口端口。将此端口连接到制冷循环模型中冷凝器或储液器的出口。

### **B** — 流体出口 两相流体

阀出口端口。将此端口连接到制冷循环模型中蒸发器的入口。

### **S** — 感温包温度测量 两相流体

与感温包温度关联的两相流体守恒端口。将此端口连接到蒸发器的出口端口。阀的操作取决于 **S** 处感测温度与流体饱和温度的比较。

通过端口 **S** 没有质量或能量流量。

### **E** — 均压管压力测量 两相流体

与均压管压力关联的两相流体端口。将此端口连接到蒸发器的出口端口。

通过端口 **E** 没有质量或能量流量。

#### 依赖关系

要启用此端口，请将 **Pressure equalization** 设置为 `External pressure equalization`。

## 参数

### **Valve parameterization** — 参数化方法 `Nominal capacity, superheat, and operating conditions`（默认）| `Tabulated data - quadrant diagram`

确定阀特性的方法。当您选择 `Nominal capacity, superheat, and operating conditions` 时，阀在指定的标称工况下提供指定的标称容量和过热度。当您选择 `Tabulated data - quadrant diagram` 时，您可以使用热力膨胀阀四象限图中的四条曲线中的三条来指定阀特性。

### **Capacity specification** — 容量指定方法 `Evaporator heat transfer`（默认）| `Mass flow rate`

指定蒸发器容量的方法。当您选择 `Evaporator heat transfer` 时，您可以指定标称和最大蒸发器传热值。当您选择 `Mass flow rate` 时，模块根据质量流量计算传热。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`。

### **Nominal evaporator heat transfer** — 标称工况下的蒸发器传热速率 `15` `kW`（默认）| 正标量

标称工况下系统蒸发器中的传热速率。此参数设置热力膨胀阀的运行工况。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **Capacity specification** 设置为 `Evaporator Heat transfer`。

### **Maximum evaporator heat transfer** — 最大蒸发器传热速率 `20` `kW`（默认）| 正标量

系统蒸发器中的最大传热速率。在大多数制冷循环中，此值比 **Nominal evaporator heat transfer** 参数的值大 20% 到 50%。此参数设置热力膨胀阀的最大运行工况。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **Capacity specification** 设置为 `Evaporator Heat transfer`。

### **Nominal mass flow rate** — 标称工况下的质量流量 `0.005` `kg/s`（默认）| 正标量

标称工况下系统蒸发器中的质量流量。模块使用此参数设置热力膨胀阀的运行工况。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **Capacity specification** 设置为 `Mass flow rate`。

### **Maximum mass flow rate** — 最大蒸发器传热速率 `0.008` `kg/s`（默认）| 正标量

系统蒸发器中的最大质量流量。模块使用此参数设置热力膨胀阀的最大运行工况。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **Capacity specification** 设置为 `Mass flow rate`。

### **Nominal pressure specification** — 指定标称压力的方法 `Specified pressure`（默认）| `Pressure at specified saturation temperature`

指定蒸发器和冷凝器标称压力的方法。当您选择 `Specified pressure` 时，您可以指定蒸发器和冷凝器出口压力。当您选择 `Pressure at specified saturation temperature` 时，您指定冷凝器和蒸发器中的饱和温度。模块使用制冷剂属性表计算相应的饱和温度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`。

### **Nominal condenser outlet pressure** — 标称工况下的冷凝器出口压力 `1.5` `MPa`（默认）| 正标量

标称工况下冷凝器中的制冷剂压力。模块使用制冷剂属性表计算相应的饱和温度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **Nominal pressure specification** 设置为 `Specific pressure`。

### **Nominal evaporator outlet pressure** — 标称工况下的蒸发器出口压力 `0.3` `MPa`（默认）| 正标量

标称工况下蒸发器中的制冷剂压力。模块使用制冷剂属性表计算相应的饱和温度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **Nominal pressure specification** 设置为 `Specific pressure`。

### **Nominal condensing (saturation) temperature** — 冷凝器中的制冷剂饱和温度 `313.15` `K`（默认）| 正标量

标称工况下冷凝器中的制冷剂饱和温度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **Nominal pressure specification** 设置为 `Pressure at specified saturation temperature`。

### **Nominal evaporating (saturation) temperature** — 标称工况下的蒸发器饱和温度 `273.15` `K`（默认）| 正标量

标称工况下蒸发器中的制冷剂饱和温度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **Nominal pressure specification** 设置为 `Pressure at specified saturation temperature`。

### **Nominal condenser subcooling** — 运行冷凝器出口温差 `5` `deltaK`（默认）| 正标量

标称工况下 **Nominal condensing (saturation) temperature** 参数值与冷凝器出口液体温度之间的差值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`。

### **Nominal (static + opening) evaporator superheat** — 运行蒸发器出口温差 `10` `deltaK`（默认）| 正标量

标称工况下蒸发器出口过热蒸气温度与 **Nominal evaporating (saturation) temperature** 参数值之间的差值。阀通过调节开启面积以允许更多或更少的流体进入蒸发器来维持此值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`。

### **Static (minimum) evaporator superheat** — 蒸发器出口处最小允许温差 `5` `deltaK`（默认）| 正标量

蒸发器出口处过热蒸气温度与 **Nominal evaporating (saturation) temperature** 参数值之间允许的最小差值。如果运行差值低于此值，阀门关闭。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`。

### **MOP limit** — 是否启用压力或温度限制 `Off`（默认）| `On - Specify maximum operating pressure` | `On - Specify maximum operating temperature`

是否在蒸发器中启用压力限制。选项包括：

- `Off`：无压力限制。阀门仅根据蒸发器过热度开启和关闭。
- `On - Specify maximum operating pressure`：此设置对蒸发压力和温度设置上限。当蒸发器压力达到此限制时，阀门关闭。
- `On - Specify maximum operating temperature`：此设置对蒸发压力和温度设置上限。当蒸发器温度达到此限制时，阀门关闭。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`。

### **Maximum evaporator outlet pressure** — 最大压力 `0.5` `MPa`（默认）| 正标量

当蒸发器压力限制开启时，蒸发器中允许的最大饱和压力。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **MOP limit** 设置为 `On - Specify maximum operating pressure`。

### **Maximum evaporating (saturation) temperature** — 最高温度 `288.15` `K`（默认）| 正标量

当蒸发器温度限制开启时，蒸发器中允许的最高饱和温度。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`，并将 **MOP limit** 设置为 `On - Specify maximum operating temperature`。

### **Closed valve leakage as a fraction of nominal flow** — 阀门始终存在的最小流量 `1e-6`（默认）| 正标量

阀门关闭时通过阀门的泄漏流量与额定流量之比。非零值可增强流体网络的数值稳定性。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，在阀门接近开启或接近关闭位置时为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Nominal capacity, superheat, and operating conditions`。

### **Quadrant 1 – Evaporator outlet temperature vector** — 蒸发器出口温度值向量 `0 : 10 : 40` `degC`（默认）| 向量

感温包的温度，感温包通常放置在蒸发器出口处。因此，此参数等效于蒸发器出口温度。模块在四象限图第 1 象限的 *x* 轴上使用此数据。此参数的长度必须与 **Quadrant 1 – Bulb pressure vector** 参数相同。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Quadrant 1 – Bulb pressure vector** — 感温包内流体压力值向量 `0.3 : 0.1 : 0.7` `MPa`（默认）| 向量

蒸发器出口处感温包内流体的压力。蒸发器出口处的制冷剂压力与感温包的内部流体压力无关。阀门使用感温包压力来开启。模块在四象限图第 1 象限的 *y* 轴上插值此数据。此参数的长度必须与 **Quadrant 1 – Evaporator outlet temperature vector** 参数相同。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Quadrant 2 – Valve lift vector** — 阀门升程值向量 `0 : 0.15 : 0.6` `mm`（默认）| 向量

阀门升程（即阀针位置）的向量。模块在四象限图第 2 象限的 *x* 轴上使用此数据。阀门升程在第 2 象限和第 3 象限之间的定义必须一致。模块使用阀门升程来关联第 2 象限中的压力和第 3 象限中的流量。如果数据不可用，您可以构造阀门升程值，例如 0 表示完全关闭，1 表示完全开启。此参数的长度必须与 **Quadrant 2 – Evaporator outlet pressure vector** 参数相同。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Quadrant 2 – Evaporator outlet pressure vector** — 蒸发器出口压力值向量 `0.3 : -0.05 : 0.1` `MPa`（默认）| 向量

均衡压力的向量，均衡压力是阀门蒸发器出口压力的度量。阀门使用均衡压力来关闭：

- 如果阀门具有内平衡，此参数为阀门出口处的压力，该出口连接到蒸发器入口。在这种情况下，模块假设蒸发器中的压力损失很小。
- 如果阀门具有外平衡，则此参数为连接到蒸发器出口的外部导压管所测得的值。

模块在四象限图第 2 象限的 *y* 轴上插值此数据。此参数的长度必须与 **Quadrant 2 – Valve lift vector** 参数相同。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Quadrant 3 – Valve lift vector** — 阀门升程值向量 `0 : 0.15 : 0.6` `mm`（默认）| 向量

阀门升程（即阀针位置）的向量。模块在四象限图第 3 象限的 *x* 轴上使用此数据。阀门升程在第 2 象限和第 3 象限之间的定义必须一致。模块使用阀门升程来关联第 2 象限中的压力和第 3 象限中的流量。如果数据不可用，您可以构造阀门升程值，例如 0 表示完全关闭，1 表示完全开启。此参数的长度必须与 **Quadrant 3 – Mass flow rate vector** 参数相同。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Quadrant 3 – Mass flow rate vector** — 通过阀门的质量流量值向量 `[1e-7,0.015 : 0.015 : 0.06]` `kg/s`（默认）| 向量

通过阀门的质量流量相对于不同阀门开度值的值。模块在四象限图第 3 象限的 *y* 轴上插值此数据。此参数的长度必须与 **Quadrant 3 – Valve lift vector** 参数相同。第一个元素对应于阀门关闭时的泄漏质量流量。为了数值鲁棒性，此值必须是一个较小的正值。

#### 依赖

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Reference condenser outlet pressure** — 冷凝器出口参考压力 `2` `MPa`（默认）| 标量

参考阀门入口压力。模块在四象限图第 3 象限中将阀门入口压力保持为此值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Reference evaporator outlet pressure** — 蒸发器出口参考压力 `0.3` `MPa`（默认）| 标量

蒸发器出口参考压力。该模块在四象限图的第 3 象限中将蒸发器出口压力保持在此值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Reference evaporator outlet temperature** — 蒸发器出口参考温度 `0` `degC`（默认）| 标量

蒸发器出口参考温度。该模块在四象限图的第 2 象限中将蒸发器出口温度保持在此值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Reference condenser subcooling** — 冷凝器出口参考温差 `5` `deltaK`（默认）| 标量

冷凝器出口温度与冷凝温度之间的差值。该模块在四象限图的第 3 象限中将阀入口温度保持在此值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data – quadrant diagram`。

### **Pressure equalization** — 压力测量位置 `Internal pressure equalization`（默认）| `External pressure equalization`

压力测量位置。将此参数设置为 `Internal pressure equalization` 以在端口 **B** 处测量蒸发器压力。将此参数设置为 `External pressure equalization` 以暴露蒸发器压力端口 **E**。将此端口连接到蒸发器出口。根据您的热力膨胀阀设计选择此参数的设置。

### **Bulb temperature dynamics** — 是否对热滞后建模 `off`（默认）| `on`

是否对温度测量中的热动力学建模。当您选择此参数时，感温包流体温度滞后于制冷温度。**Bulb thermal time constant** 参数决定滞后响应。

### **Bulb thermal time constant** — 热滞后时间常数 `20` s（默认）| 正标量

感温包流体温度延迟的一阶时间常数。该模块将测量温度相对于端口 **S** 处的制冷剂温度进行延迟。该时间常数与感温包的热质量（包括任何配重）成正比，与热接触表面的热导成反比。

#### 依赖关系

要启用此参数，请选择 **Bulb temperature dynamics**。

### **Cross-sectional area at ports A and B** — 端口面积 `0.01` `m^2`（默认）| 正标量

端口 **A** 和 **B** 处连接管道的横截面积。

### **Laminar flow pressure ratio** — 流态转变处的蒸发器压力比 `0.999`（默认）| 正标量

流体在层流和湍流之间转变时的蒸发器出口压力与蒸发器入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **Inlet phase change time constant** — 混合物比容的滞后 `0.1` `s`（默认）| 正标量

计算流体比容时液-汽混合物的时间滞后。当入口流体为完全过冷液体时，此参数不影响比容。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2022b：模块支持通过四象限图的表格数据进行参数化

您可以将新的 **Valve parameterization** 参数设置为：

- `Nominal capacity, superheat, and operating conditions` — 模块的行为与之前版本相同。
- `Tabulated data - quadrant diagram` — 模块启用用于指定四象限图中曲线的参数。

此外，您可以通过右键单击模块并选择 **Fluids** > **Plot 4-Quadrant Diagram** 来生成该图的绘图。

## 描述

维持蒸发器过热度的流量控制阀

Thermostatic Expansion Valve (2P) 模块对具有压力降的阀进行建模，该阀在两相流体网络中维持蒸发器过热度。您通常将此阀放置在制冷系统中冷凝器和蒸发器之间，通过调节进入蒸发器的流量来维持特定的温差。

阀的行为取决于*过热度*，即蒸发器出口处蒸汽温度与流体蒸发温度之间的差值。如果过热度增加，阀打开以允许更多流量通过；如果过热度降低，阀关闭以减少流量通过。当过热度降至或低于 **Static (minimum) evaporator superheat** 参数的值时，阀完全关闭。关闭的阀减少通过蒸发器的流量，从而减少热传递并提高出口温度。当您使用 **MOP limit** 参数启用最大压力或温度限制时，当温度或压力超过限制时阀关闭。

端口 **S** 处的感温包传感器测量蒸发器出口温度。如果您将 **Pressure equalization** 参数设置为 `External pressure equalization`，模块使用端口 **E** 处蒸发器的数据进行内部压力平衡。否则，模块使用端口 **B** 处的压力进行内部压力平衡。模块将作用于打开阀的感温包压力与作用于关闭阀的阀平衡压力进行平衡。

### 解析参数化

当您将 **Valve parameterization** 设置为 `Nominal capacity,
superheat, and operating conditions` 时，模块使用解析模型。在此设置下，模块将解析模型拟合到性能数据，以便当制冷系统在指定的标称蒸发温度、冷凝温度和冷凝器过冷度下运行时，模块计量足够的流量进入蒸发器以维持蒸发器过热度，同时模块以蒸发器容量传递热量。过冷度是冷凝器出口与冷凝温度之间的温差。

对于此参数化，模块假设为直充式感温包，并假设感温包包含与制冷剂相同的流体。要对交叉充注式感温包建模，请将 **Valve parameterization** 设置为 `Tabulated data
- quadrant diagram`。

**开口面积**

阀门通过调节有效开口面积 *Seff* 来控制冷凝器和蒸发器之间的质量流量。质量流量为

m˙=Seff2vinΔp(Δp2−Δplam2)0.25，

其中：

- *vin* 是入口比容，即单位质量的流体体积。
- *Δp* 是阀门上的压差，*pA* – *pB*。
- *Δplam* 是过渡流的压力阈值。低于此值时，流动为层流

  Δplam=pA+pB2(1−Blam)，

  其中 *B*lam 是 **Laminar flow pressure ratio** 参数的值。

有效阀门面积取决于测量压力 *p*bulb 与均衡压力 *p*eq 之间的压差

Seff=β[(pbulb−peq)−(psat(Tevap+ΔTstatic)−psat(Tevap))]，

其中：

- *β* 是根据标称运行条件确定的阀门常数。请参阅根据标称条件确定 β。
- *Tevap* 是蒸发温度。

  当 **Nominal pressure specification** 为 `Pressure at specified saturation
  temperature` 时，*Tevap* 是 **Nominal evaporating (saturation)
  temperature** 参数的值。

  当 **Nominal pressure specification** 为 `Specified pressure` 时，*Tevap* 是对应于 **Nominal evaporator outlet pressure** 参数值的饱和温度。
- *ΔTstatic* 是 **Static (minimum) evaporator superheat** 参数。
- *psat(Tevap)* 是作为 *Tevap* 函数的流体饱和压力。模块使用 `tablelookup` 函数来识别此值。
- *psat(Tevap+ΔTstatic)* 是作为 *Tevap+ΔTstatic* 函数的饱和压力。模块使用 `tablelookup` 函数来识别此值。
- *pbulb* 是感温包的流体压力。感温包压力为饱和压力 pbulb=psat(Tbulb)，除非您将 **MOP limit** 设置为 `On - Specify maximum operating
  pressure` 且压力达到最大压力。有关更多信息，请参阅最大出口压力限制。*Tbulb* 是感温包流体温度。
- *p*eq 取决于阀门压力均衡设置：

  - 当您将 **Pressure
    equalization** 设置为 `Internal
    pressure equalization` 时，*p*eq 是端口 **B** 处的压力。
  - 当您将 **Pressure
    equalization** 设置为 `External
    pressure equalization` 时，*p*eq 是端口 **E** 处的压力。

有效阀门面积有限制。最小有效阀门面积 *Seff,min* 为

Seff,min=fleakSeff,nom，

其中 *fleak* 是 **Closed valve leakage as a fraction of nominal
flow** 参数的值。要了解模块如何计算标称有效阀门面积 *Seff,nom* 和最大有效阀门面积，请参阅根据标称条件确定 β。

**根据标称条件确定 β**

*β* 表示标称蒸发器过热度与*标称蒸发器容量*之间的关系，即蒸发器中两种流体之间的传热速率：

β=Seff,nom[psat(Tevap+ΔTnom)−psat(Tevap)]，

其中 *psat(Tevap+ΔTnom)* 是蒸发器出口温度与 **Nominal (static + opening) evaporator superheat** 参数之和处的饱和压力。

模块根据标称冷凝器和蒸发器热力学计算标称有效阀门面积 *S*eff,nom。当 **Capacity
specification** 为 `Evaporator heat
transfer` 时，标称有效阀门面积为

Seff,nom=[Qnomcp,evapΔTnom+hevap−hcond+cp,condΔTsub]2vcond(psat(Tcond)−psat(Tevap))。

当 **Capacity specification** 为 `Mass flow
rate` 时，标称有效阀门面积为

Seff,nom=m˙nom2vcond(psat(Tcond)−psat(Tevap))，

其中：

- *Tcond* 是冷凝饱和温度。

  当 **Nominal pressure specification** 为 `Pressure at specified saturation
  temperature` 时，*Tcond* 是 **Nominal condensing (saturation) temperature** 参数的值。

  当 **Nominal pressure specification** 为 `Specified pressure` 时，*Tcond* 是对应于 **Nominal condenser outlet pressure** 参数值的饱和温度。
- *vcond* 是 *Tcond* 下的液体比容。
- *Qnom* 是 **Nominal evaporator heat transfer** 参数。
- *cp,evap* 是 *Tevap* 下的蒸汽比热。
- *hevap* 是 *Tevap* 下的蒸汽比焓。
- *cp,cond* 是 *Tcond* 下的液体比热。
- *hcond* 是 *Tcond* 下的液体比焓。
- *ΔTsub* 是 **Nominal condenser subcooling** 参数。
- m˙nom 是 **Nominal mass flow rate** 参数。

当 **Capacity specification** 为 `Evaporator heat transfer` 时，模块以与 *Seff,nom* 相同的方式确定阀门最大有效面积，但使用 **Maximum evaporator heat transfer** 参数的值代替 **Nominal evaporator heat transfer** 参数。当 **Capacity specification** 为 `Mass flow
rate` 时，模块使用 **Maximum mass flow rate** 参数的值代替 **Nominal mass flow
rate** 参数。

**最大出口压力限制**

您可以通过将 **MOP limit** 参数设置为 `On - Specify
maximum operating pressure` 或 `On - Specify
maximum operating temperature` 来限制蒸发器中的最大出口压力 (MOP)。当您使用其中一种设置时，当感温包温度或压力超过与最大感温包压力相关的温度或压力时，阀门关闭；一旦压力降低，阀门打开。如果您将 **MOP limit** 设置为 `Off`，或测量压力低于限制值，则 pbulb=psat(Tbulb)。否则，当测量值超过限制值时，感温包压力保持为

pbulb=pbulb,MOPTbulb,MOPTbulb，

其中：

- *p*bulb,MOP 是 **Maximum evaporator outlet pressure** 参数 *p*eq,MOP 或 **Maximum evaporating (saturation)
  temperature** 参数指定的压力以及标称蒸发器温度的函数：

  pbulb,MOP=peq,MOP+psat(Tevap+ΔTstatic)−psat(Tevap)。
- *T*bulb 是感温包流体温度。如果您清除 **Bulb
  temperature dynamics** 复选框，此值是端口 **S** 处的温度。如果您选择 **Bulb temperature dynamics**，模块对感温包温度应用一阶延迟。
- *T*bulb,MOP 是压力 *p*bulb,MOP 处的相关温度。

### 四象限图

要可视化四象限图，请右键点击该模块并选择 **Fluids** > **Plot 4-Quadrant Diagram**。

当 **Valve parameterization** 为 `Tabulated data - quadrant diagram` 时，该模块使用用户提供的数据在所有象限中绘图。请参阅表格数据参数化。

当 **Valve parameterization** 为 `Nominal capacity, superheat, and operating conditions` 时，该模块使用解析阀门模型计算所有象限中的数据，如解析参数化中所述。由于解析模型假设直充式感温包，图中象限 1 的两条曲线会相互重叠。

四象限图

该图显示了四个象限：

- **象限 1：** 当感温包连接到蒸发器出口时，感温包流体压力与蒸发器出口温度的关系图。在此图中，图形包含第二条线，表示循环中制冷剂的蒸气饱和曲线，即饱和压力与饱和温度的关系图。
- **象限 2：** 阀门升程与蒸发器出口压力的关系图。阀门升程是阀门针的位置。随着蒸发器出口压力降低，阀门打开，阀门升程增加。

  当 **Valve parameterization** 为 `Tabulated data - quadrant diagram` 时，该图将蒸发器出口温度保持恒定在 **Reference evaporator outlet temperature** 参数值。
- **象限 3：** 通过阀门的质量流量与阀门升程的关系图。

  当 **Valve parameterization** 为 `Tabulated data - quadrant diagram` 时，该图将阀门入口压力保持恒定在 **Reference condenser outlet pressure** 参数，入口温度保持恒定在 **Reference condenser subcooling** 参数，出口压力保持恒定在 **Reference evaporator outlet pressure parameter**。
- **象限 4：** 通过阀门的质量流量与蒸发器出口温度的关系图。

  当 **Valve parameterization** 为 `Tabulated data - quadrant diagram` 时，该图将阀门入口压力保持恒定在 **Reference condenser outlet pressure** 参数，入口温度保持恒定在 **Reference condenser subcooling** 参数，出口压力保持恒定在 **Reference evaporator outlet pressure parameter**。

### 表格数据参数化

当您将 **Valve parameterization** 设置为 `Tabulated data - quadrant diagram` 时，该模块使用表格数据。热力膨胀阀四象限图中的四条曲线中有三条指定了阀门特性。供应商通常会提供此图。

为了确定模块特性，该模块对您在参数 **Quadrant 1 - Evaporator outlet temperature vector**、**Quadrant 1 - Bulb pressure vector**、**Quadrant 2 - Valve lift vector**、**Quadrant 2 - Evaporator outlet pressure vector**、**Quadrant 3 - Valve lift vector** 和 **Quadrant 3 - Mass flow rate vector** 中提供的数据执行插值。

该模块通过使用象限 1 到象限 3 的数据以及一系列插值，根据入口压力、出口压力、平衡压力和感温包温度确定通过阀门的质量流量。该模块首先计算象限 2 蒸发器出口压力为

pevap,Q2=peq−pbulb(Tbulb)+pbulb(Tevap,ref)

其中：

- *p*eq 取决于阀门压力平衡设置：

  - 当您将 **Pressure equalization** 设置为 `Internal pressure equalization` 时，*p*eq 是端口 **B** 处的压力。
  - 当您将 **Pressure equalization** 设置为 `External pressure equalization` 时，*p*eq 是端口 **E** 处的压力。
- *pbulb(Tbulb)* 是在感温包流体温度 *Tbulb* 处插值得到的感温包流体压力。您在参数 **Quadrant 1 – Bulb pressure vector** 中指定感温包流体压力数据。
- *pbulb(Tevap,ref)* 是在参考蒸发器出口温度 *Tevap,ref* 处插值得到的感温包流体压力。

该模块使用来自 **Quadrant 2 – Valve lift vector** 参数的阀门升程数据 *L*，在 **Quadrant 2 – Evaporator outlet pressure vector** 中的值处插值阀门升程，得到 *L = L(pevap,Q2)*。然后，该模块使用来自 **Quadrant 3 – Mass flow rate vector** 的参考质量流量 m˙ref，在阀门升程值处插值质量流量 m˙ref=m˙ref(L)。该模块使用以下公式将参考质量流量缩放为实际质量流量

m˙=m˙ref2vinΔp(Δp2−Δplam2)0.252vref(pcond,ref−pevap,ref)

其中：

- *pcond,ref* 是 **Reference condenser outlet pressure** 参数。
- *pevap,ref* 是 **Reference evaporator outlet pressure** 参数。
- *vref* 是对应于 **Reference condenser outlet pressure** 和 **Reference condenser subcooling** 参数的比容。
- *vin* 是入口比容，即单位质量的流体体积。
- *Δp* 是阀门上的压差，*pA* – *pB*。
- *Δplam* 是过渡流的压力阈值。低于此值时，流动为层流。该模块按以下公式计算此值：

  Δplam=pA+pB2(1−Blam),

  其中 *B*lam 是 **Laminar flow pressure ratio** 参数的值。

### 压力平衡

平衡压力是控制阀门可操作性的蒸发器出口压力。在由于粘性摩擦导致蒸发器压力损失较低的物理系统中，压力平衡可以在内部发生，即端口 **B** 处的压力。这就是*内部压力平衡*。在损失较大的系统中，将蒸发器出口端口连接到阀门模块的端口 **E**。

### 感温包温度动态

您可以通过选择 **Bulb temperature dynamics** 来模拟感温包对温度变化的动态响应。这会在测量温度中引入一阶滞后

dTbulbdt=TS−Tbulbτbulb,

其中：

- *T*S 是端口 **S** 处的温度。如果您不模拟感温包动态，此值即为 *T*bulb。
- *τ*bulb 是 **Bulb thermal time constant** 参数的值。

### 流体比容动态

当阀门入口处的流体为液-气混合物时，该模块按以下公式计算比容

vin=(1−xdyn)vliq+xdynvvap,

其中：

- *xdyn* 是入口蒸气干度。该模块对混合物的入口蒸气干度应用一阶滞后。
- *vliq* 是流体的液体比容。
- *vvap* 是流体的蒸气比容。

如果入口流体为液体或蒸气，*vin* 分别为相应的液体或蒸气比容。

**蒸气干度滞后**

如果入口蒸气干度为液-气混合物，该模块应用一阶时间滞后

dxdyndt=xin−xdynτ,

其中：

- *xdyn* 是动态蒸气干度。
- *xin* 是当前入口蒸气干度。
- *τ* 是 **Inlet phase change time constant** 参数的值。

如果入口流体为过冷液体，*xdyn* 等于 *xin*。

### 守恒方程

通过阀门的质量守恒

m˙A+m˙B=0,

其中：

- m˙A 是端口 **A** 处的质量流量。
- m˙B 是端口 **B** 处的质量流量。

该模块在数值上支持反向流动，但是，该阀门模块并非为从端口 **B** 流向端口 **A** 的流动而设计。

该模块守恒通过阀门的能量流

ΦA+ΦB=0,

其中：

- *Φ*A 是端口 **A** 处的能量流率。
- *Φ*B 是端口 **B** 处的能量流率。
