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

### 守恒

### **A** — 流体入口或出口 two-phase fluid

与流体入口或出口端口关联的 two-phase fluid 守恒端口。

### **B** — 流体入口或出口 two-phase fluid

与流体入口或出口端口关联的 two-phase fluid 守恒端口。

### 输入

### **Ps** — 设定压力，Pa physical signal

用于变化设定压力信号的输入端口。

#### 依赖关系

要启用此端口，请将 **设定压力控制** 设置为 `Controlled`。

## 参数

### **建模选项** — 流体相态的建模选项 `Liquid operating condition` (默认) | `Vapor operating condition`

阀口处流体相态的建模选项。如果模块位置处的 two-phase fluid 处于液态，则将此参数设置为 `Liquid operating condition`。如果模块位置处的 two-phase fluid 处于气态，则将此参数设置为 `Vapor operating condition`。

### 参数

### **阀参数化** — 阀参数化模型 `Linear - Area vs. pressure` (默认) | `Linear - Nominal mass flow rate vs. pressure` | `Tabulated data - Area vs. pressure` | `Cv flow coefficient` | `Kv flow coefficient` | `Orifice area`

模块用于根据阀两端压差计算质量流量或根据质量流量计算压差的方法。

当 **建模选项** 为 `Liquid operating condition` 时，此参数的选项为：

- `Linear - Area vs. pressure`
- `Linear - Nominal mass flow rate vs. pressure`
- `Tabulated data - Area vs. pressure`

当 **建模选项** 为 `Vapor operating condition` 时，此参数的选项为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **开启压力指定** — 控制压力 `Pressure differential` (默认) | `Gauge pressure at port A`

控制压力指定：

- 当此参数为 `Pressure differential` 时，当 *pA ̶ pB* 超过 **设定压差** 时，阀开启。
- 当此参数为 `Gauge pressure at port A` 时，当 *pA ̶ patm* 超过 **设定压力（表压）** 时，阀开启。

### **设定压力控制** — 可变或恒定设定压力 `Constant` (默认) | `Controlled`

压力阈值是恒定的还是可变的。将此参数设置为 `Controlled` 会公开 physical signal 端口 **Ps**。

### **设定压差** — 设定压力 `0.01` MPa (默认) | positive scalar

阀压力阈值。当控制压力 *pA ̶ pB* 超过设定压力时，阀开始开启。

#### 依赖关系

要启用此参数，请将 **开启压力指定** 设置为 `Pressure differential`，将 **设定压力控制** 设置为 `Constant`，并且满足以下任一条件：

- **建模选项** 为 `Liquid operating condition`，且 **阀参数化** 为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **建模选项** 为 `Vapor operating condition`，且 **开启特性** 为 `Linear`。

### **设定压力（表压）** — 设定压力 `0.1` MPa (默认) | positive scalar

阀压力阈值。当控制压力 *pA ̶ patm* 超过设定压力时，阀开始开启。

#### 依赖关系

要启用此参数，请将 **开启压力指定** 设置为 `Gauge pressure at port A`，将 **设定压力控制** 设置为 `Constant`，并且满足以下任一条件：

- **建模选项** 为 `Liquid operating condition`，且 **阀参数化** 为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **建模选项** 为 `Vapor operating condition`，且 **开启特性** 为 `Linear`。

### **压力调节范围** — 阀工作范围 `0.1` MPa (默认) | positive scalar

阀工作范围。阀在设定压力值处开始开启，并在 *pmax*（压力调节范围的终点）处完全开启，其中 *pmax = pset + prange*。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **建模选项** 为 `Liquid operating condition`，且 **阀参数化** 为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **建模选项** 为 `Vapor operating condition`，且 **开启特性** 为 `Linear`。

### **最大阀开度下的额定质量流量** — 额定质量流量 `0.1` kg/s (默认) | positive scalar

在典型、设计或额定条件下流经全开阀的质量流量。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **阀参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **最大阀开度下的额定压降** — 额定压降 `0.001` MPa (默认) | positive scalar

在典型、设计或额定条件下全开阀上的压降。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **阀参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **额定入口条件指定** — 确定入口流体状态的方法 `Temperature` (默认) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。模块根据 **额定入口压力** 参数的值和 **额定入口条件指定** 参数的设置，从表格化流体属性数据中确定孔口额定入口比容。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **阀参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **额定入口压力** — 入口流体压力 `0.101325` MPa (默认) | positive scalar

额定条件下的入口压力。模块根据 **额定入口压力** 参数的值和 **额定入口条件指定** 参数的设置，从表格化流体属性数据中确定入口比容。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **阀参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **额定入口温度** — 流体温度 `293.15` K (默认) | positive scalar

额定工作条件下的入口流体温度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，将 **阀参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **额定入口条件指定** 设置为 `Temperature`。

### **额定入口蒸汽干度** — 入口蒸汽干度质量分数 `0` (默认) | positive scalar in the range [0,1]

额定工作条件下入口混合物的蒸汽干度（按质量分数）。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，将 **阀参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **额定入口条件指定** 设置为 `Vapor quality`。

### **额定入口蒸汽空隙率** — 入口体积分数 `0` (默认) | positive scalar in the range [0,1]

额定工作条件下入口混合物的体积分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，将 **阀参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **额定入口条件指定** 设置为 `Vapor void fraction`。

### **额定入口比焓** — 入口流体比焓 `400` kJ/kg (默认) | positive scalar

额定工作条件下的入口比焓。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，将 **阀参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **额定入口条件指定** 设置为 `Specific enthalpy`。

### **额定入口比内能** — 入口比内能 `400` kJ/kg (默认) | positive scalar

额定工作条件下的入口比内能。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，将 **阀参数化** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **额定入口条件指定** 设置为 `Specific internal energy`。

### **最大阀面积** — 最大阀开启面积 `1e-4 m^2` (默认) | positive scalar

阀完全开启时的最大阀面积。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **阀参数化** 设置为 `Linear – Area vs. pressure`。

### **开启压差向量** — 压差向量 `[0.2 : 0.2 : 1.2] MPa` (默认) | 1-by-*n* vector

用于阀面积表格化参数化的压差值向量。此向量中的值与 **阀面积向量**、**孔口面积向量**、**Cv 流量系数向量** 或 **Kv 流量系数向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **开启压力指定** 设置为 `Pressure differential`，并且满足以下任一条件：

- **建模选项** 为 `Liquid operating condition`，且 **阀参数化** 为 `Tabulated data - Area vs. pressure`
- **建模选项** 为 `Vapor operating condition`，且 **开启特性** 为 `Tabulated`。

### **开启压力（表压）向量** — 表压向量 `[0.2 : 0.2 : 1.2] MPa` (默认) | 1-by-*n* vector

用于阀面积表格化参数化的表压值向量。此向量中的值与 **阀面积向量**、**孔口面积向量**、**Cv 流量系数向量** 或 **Kv 流量系数向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **开启压力指定** 设置为 `Gauge pressure at port A`，并且满足以下任一条件：

- **建模选项** 为 `Liquid operating condition`，且 **阀参数化** 为 `Tabulated data - Area vs. pressure`
- **建模选项** 为 `Vapor operating condition`，**阀参数化** 为 `Orifice area`，且 **开启特性** 为 `Tabulated`。

### **阀面积向量** — 阀开启面积值向量 `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05] m^2` (默认) | 1-by-*n* vector

用于阀面积表格化参数化的孔口面积值向量。此向量中的值与 **开启压差向量** 或 **开启压力（表压）向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **阀参数化** 设置为 `Tabulated data - Area vs. pressure`。

### **流量系数** — 流量系数 `0.64` (默认) | positive scalar

实际流量与理想流量的比值。此参数考虑了孔口方程未捕获的实际损失。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **建模选项** 为 `Liquid operating condition`，且 **阀参数化** 为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。
- **建模选项** 为 `Vapor operating condition`，且 **阀参数化** 为 `Orifice area`。

### **压力恢复** — 是否考虑面积扩大中的压力升高 `off` (默认) | `on`

是否考虑从入口到孔口孔的压力下降后的小幅压力升高。当流体射流离开孔口孔时，它会耗散并膨胀以填充端口面积，从而导致此小幅压力升高。当清除 **压力恢复** 复选框时，模块不会对此压力升高建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **阀参数化** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **开启特性** — 参数化流量能力度量的方法 `Linear` (默认) | `Tabulated`

为所选流量能力度量对蒸汽阀进行参数化的方法。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`。

### **最大 Cv 流量系数** — 对应最大开启组件的 *Cv* 系数 `4` (默认) | positive scalar

当可用于流动的限制面积最大时，*Cv* 流量系数的值。此参数衡量蒸汽在压差驱动下穿过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，将 **阀参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Cv 流量系数向量** — 对应成员位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (默认) | 1-by-*n* vector

*Cv* 流量系数的向量。每个系数对应 **开启压差向量** 或 **开启压力（表压）向量** 参数中的一个值。此参数衡量蒸汽在压差驱动下穿过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，将 **阀参数化** 设置为 `Cv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **最大 Kv 流量系数** — 对应最大开启组件的 *Kv* 系数 `3.6` (默认) | positive scalar

当可用于流动的限制面积最大时，*Kv* 流量系数的值。此参数衡量蒸汽在压差驱动下穿过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，将 **阀参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Linear`。

### **Kv 流量系数向量** — 对应成员位置向量中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (默认) | 1-by-*n* vector

*Kv* 流量系数的向量。每个系数对应 **开启压差向量** 或 **开启压力（表压）向量** 参数中的一个值。此参数衡量蒸汽在压差驱动下穿过阻力元件的容易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，将 **阀参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **阻塞流下的 xT 压差比因子** — 压差比 `0.7` (默认) | positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中发生阻塞。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，并将 **阀参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **最大孔口面积** — 最大阀开启面积 `1e-4 m^2` (默认) | positive scalar

阀完全开启时的最大阀面积。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **Orifice area vector** — 阀开启面积值的向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于蒸气阀门面积的表格化参数化的孔口面积值向量。此向量中的值与 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Valve parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| positive scalar

阀门关闭时流量与打开时流量的比值。

#### 依赖关系

要启用此参数，请设置以下任一项：

- 将 **Modeling option** 设置为
  `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear -
  Nominal mass flow rate vs. pressure` 或
  `Linear - Area vs. pressure`。
- 将 **Modeling option** 设置为
  `Vapor operating condition`，并将 **Opening characteristic** 设置为
  `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| positive scalar in the range [0,1]

连续平滑因子，当阀门处于接近打开或接近关闭的位置时，该因子为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，以提高仿真在这些区域中的稳定性。

#### 依赖关系

要启用此参数，请设置以下任一项：

- 将 **Modeling option** 设置为
  `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear -
  Nominal mass flow rate vs. pressure` 或
  `Linear - Area vs. pressure`。
- 将 **Modeling option** 设置为
  `Vapor operating condition`，并将 **Opening characteristic** 设置为
  `Linear`。

### **Inlet phase change time constant** — 液体比容的滞后 `0.1` s（默认）| positive scalar

计算流体比容时，用于液体-蒸气混合物的时间滞后。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`。

### **Laminar flow pressure ratio** — 层流-湍流转变压力比 `0.999`（默认）| positive scalar

流体在层流和湍流状态之间转变时的阀门出口压力与阀门入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成平方关系。

### **Cross-sectional area at ports A and B** — 阀门端口面积 `0.01` m^2（默认）| positive scalar

端口 **A** 和 **B** 的面积。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024a：为蒸气阀或液体阀建模

现在可以使用 **Modeling option** 参数来指定两相流体处于蒸气态或液态时的阀门。两种建模选项还包括新的阀门参数化。

当 **Modeling option** 为 `Liquid operating condition` 时，现在可以将 **Valve parameterization** 设置为：

- `Linear - Area vs. pressure`
- `Tabulated data - Area vs. pressure`

当 **Modeling option** 为 `Vapor operating condition` 时，现在可以将 **Valve parameterization** 设置为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

要保留以前版本的模块行为，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

## 描述

两相流体网络中的泄压阀

Pressure Relief Valve (2P) 模块对两相流体网络中的压力控制泄压阀进行建模。当压力超过设定压力时，阀门打开。在 **Set pressure specification** 参数中指定打开阀门的压差，该压差可以是端口 **A** 和 **B** 之间的压力差，也可以是端口 **A** 处的表压。当将 **Set pressure control** 设置为 `Controlled` 时，设定压力根据端口 **Ps** 处的输入信号变化。

**Modeling option** 参数控制用于对蒸气或液体建模的阀门的参数化选项，但不影响流体属性。模块根据入口条件计算阀门内部的流体属性。流体与环境之间没有热交换，因此孔口内部的相变仅由压降或从模型另一部分传播而来的相变引起。

### 压力控制

当阀门中的压力 *pcontrol* 超过设定压力 *pset* 时，阀门打开。当控制压力达到 *pset* + *prange* 时，阀门完全打开，其中 *prange* 是 **Pressure regulation range** 参数的值。

对于线性参数化，模块计算阀门的开启比例 *λ*。当将 **Set pressure control** 设置为 `Constant` 时，*λ* 为

λ=(1−fleak)(pcontrol−pset)prange+fleak,

其中：

- *fleak* 是 **Leakage flow fraction** 参数的值。
- *pcontrol* 是控制压力，取决于 **Set pressure specification** 参数的值。

  当将 **Set pressure specification** 设置为 `Pressure differential` 时，控制压力为 *pA ̶ pB*。

  当将 **Set pressure specification** 设置为 `Gauge pressure at port A` 时，控制压力为端口 **A** 处的压力与大气压之间的差值。
- *pset* 是设定压力，取决于 **Set pressure specification** 参数的值。

  当将 **Set pressure specification** 设置为 `Pressure differential` 时，*pset* 是 **Set pressure differential** 参数的值。

  当将 **Set pressure specification** 设置为 `Gauge pressure at port A` 时，*pset* 是 **Set pressure (gauge)** 参数的值。

当将 **Set pressure control** 设置为 `Controlled` 时，阀门开启比例为

λ=(1−fleak)(pcontrol−ps)prange+fleak,

其中 *ps* 是端口 **Ps** 处信号的值。如果控制压力超过阀门压力调节范围，则阀门开启比例为 1。

### 液体阀

当 **Modeling option** 为 `Liquid operating condition` 时，模块参数化取决于 **Valve parameterization** 参数的值。对于所有液体参数化选项，模块以相同方式计算压力损失和压力恢复。

临界压差 *Δpcrit* 是流动在层流和湍流之间转变时的压差。对于所有液体参数化，*Δpcrit* 为

Δpcrit=(pA+pB)2(1−Blam),

其中：

- *pA* 和 *pB* 分别是端口 **A** 和 **B** 处的压力。
- *Blam* 是 **Laminar flow pressure ratio** 参数的值。

模块通过使用整个阀门的压力损失与阀门节流区域两端的即时压降之比来考虑压力损失。该比值 *PRloss* 为

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport,

其中：

- *Aport* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *Avalve* 是阀门面积。

压力恢复是由于孔口之后面积增加而在阀门中产生的正压力变化。如果不想捕获此压力升高，请清除 **Pressure recovery** 复选框。在这种情况下，*PRloss* 为 1，这会降低模型复杂度。如果孔口相对于端口面积非常小，或者下游相邻组件靠近模块且任何射流都没有空间消散，请清除此设置。

**Linear - Nominal Mass Flow Rate vs. Pressure 参数化**

当将 **Valve Parameterization** 设置为 `Nominal mass flow rate vs. pressure` 时，通过阀门的质量流量为

m˙=λm˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25,

其中：

- *Δp* 是阀门上的压降，*pA ̶ pB*。
- m˙nom 是 **Nominal mass flow rate at maximum valve opening** 参数的值。
- *Δpnom* 是 **Nominal pressure drop rate at maximum valve opening** 参数的值。
- *vnom* 是额定入口比容。模块根据 **Nominal inlet specific enthalpy** 和 **Nominal inlet pressure** 参数，从表格化流体属性数据确定此值。
- *vin* 是入口比容。

**Linear - Area vs. Pressure 参数化**

当将 **Valve parameterization** 设置为 `Linear - area vs. pressure` 时，阀门面积为

Avalve=λAmax,

其中 *Amax* 是 **Maximum valve area** 参数的值。

质量流量为

m˙=CdAvalve2vinPRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4.

当阀门处于接近打开或接近关闭的位置时，可以通过调整 **Smoothing factor** 参数来维持仿真的数值稳健性。如果 **Smoothing factor** 参数非零，模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开启面积，其中 *Aleak = fleakAmax*。有关详细信息，请参阅 Numerical Smoothing。

**Tabulated Data - Area vs. Pressure 参数化**

当将 **Valve Parameterization** 设置为 `Tabulated data - area vs. pressure` 时，模块根据 **Valve area vector** 以及 **Opening pressure differential vector** 或 **Opening pressure (gauge) vector** 参数对阀门面积进行插值。

模块使用与 `Linear - Area vs. pressure` 设置相同的方程来计算体积流量。

**流体比容动态特性**

对于所有参数化，模块在仿真期间基于液体状态计算流体比容。

如果阀门入口处的流体是液体-蒸气混合物，则模块按如下方式计算比容：

vin=(1−xdyn)vliq+xdynvvap,

其中：

- *xdyn* 是入口蒸气干度。模块对混合物的入口蒸气干度应用一阶滞后。
- *vliq* 是流体的液体比容。
- *vvap* 是流体的蒸气比容。

如果入口流体是液体或蒸气，*vin* 是对应的液体或蒸气比容。

如果入口蒸气干度是液体-蒸气混合物，模块应用一阶时间滞后：

dxdyndt=xin−xdynτ,

其中：

- *xdyn* 是动态蒸气干度。
- *xin* 是当前入口蒸气干度。
- *τ* 是 **Inlet phase change time constant** 参数的值。

如果入口流体是过冷液体，*xin = 0*。如果入口流体是过热蒸气，*xin = 1*。

### 蒸气阀

当 **Modeling option** 为 `Vapor operating condition` 时，模块行为取决于 **Valve parameterization** 和 **Opening characteristic** 参数。

阀门中的流量取决于 **Opening characteristic** 参数：

- `Linear` — 模块通过 *λ* 缩放流通能力的度量，以考虑阀门开启面积。
- `Tabulated` — 模块根据 **Cv flow coefficient vector**、**Kv flow coefficient vector** 或 **Orifice area vector** 参数对流通能力的度量进行插值。此函数使用一维查找表。

**Cv Flow Coefficient 参数化**

当将 **Valve parametrization** 设置为 `Cv flow coefficient` 时，质量流量为

m˙=CvN6Y(pin−pout)vin,

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量以 kg/hr 为单位、压力以 bar 为单位、密度以 kg/m3 为单位时，其等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *vin* 是入口比容。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 之比。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升高到高于 **Laminar flow pressure ratio** 参数的值 *Blam* 时，模块平滑过渡到方程的线性化形式：

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降到低于 1−FγxT 时，阀门变为阻塞，模块使用以下方程：

m˙=23CvN6FγxTpinvin.

**Kv Flow Coefficient 参数化**

当将 **Valve parametrization** 设置为 `Kv flow coefficient` 时，模块使用与 `Cv flow coefficient` 参数化相同的方程，但使用关系 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。

**Valve Area 参数化**

当将 **Valve parametrization** 设置为 `Orifice area` 时，质量流量为

m˙=CdAvalve2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AvalveAport)2(poutpin)2γ],

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升高到高于 **Laminar flow pressure ratio** 参数的值 *Blam* 时，模块平滑过渡到方程的线性化形式：

m˙=CdAvalve2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AvalveAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降到低于 (2γ+1)γγ−1 时，阀门变为阻塞，模块使用以下方程：

m˙=CdAvalve2γγ+1pin1vin1(γ+12)2γ−1−(AvalveAport)2.

### 质量平衡

阀内质量守恒，

m˙A+m˙B=0,

其中：

- m˙A 是端口 **A** 处的质量流量。
- m˙B 是端口 **B** 处的质量流量。

### 能量平衡

阀内能量守恒，

ΦA+ΦB=0,

其中：

- *ΦA* 是端口 **A** 处的能量流。
- *ΦB* 是端口 **B** 处的能量流。

### 假设和限制

- 阀门与环境之间没有热交换。
- 当 **Modeling option** 为 `Liquid operating condition` 时，在过冷液体区域之外结果可能不准确。当 **Modeling option** 为 `Vapor operating condition` 时，在过热蒸气区域之外结果可能不准确。要对液体-蒸气混合物中的阀门建模，请将 **Modeling option** 设置为 `Liquid operating condition`。
