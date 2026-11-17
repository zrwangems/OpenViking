---
type: simulink-block
title: 'Pressure-Reducing Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereducingvalve2p'
documentation_source_path: 'ref/pressurereducingvalve2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure-Reducing Valve (2P)

## 端口
```yaml
ports:
- name: A
  summary: 流体入口或出口两相流体
  direction: input
- name: B
  summary: 流体入口或出口两相流体
  direction: input
- name: Ps
  summary: 设定压力，Pa 物理信号
  direction: input
```

### 守恒

### **A** — 流体入口或出口两相流体

与流体入口或出口端口关联的两相流体守恒端口。

### **B** — 流体入口或出口两相流体

与流体入口或出口端口关联的两相流体守恒端口。
### 输入

### **Ps** — 设定压力，Pa 物理信号

用于改变设定压力信号的输入端口。

#### 依赖

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 流体相的建模选项 Liquid operating condition（默认）| Vapor operating condition
  group: ''
- name: Valve parameterization
  summary: 阀门参数化模型 Linear - Area vs. pressure（默认）| Linear - Nominal mass flow rate vs. pressure | Tabulated data - Area vs.
    pressure | Cv flow coefficient | Kv flow coefficient | Orifice area
  group: 参数
- name: Set pressure control
  summary: 可变或恒定设定压力 Constant（默认）| Controlled
  group: 参数
- name: Set pressure (gauge)
  summary: 设定压力 0.1 MPa（默认）| 正标量
  group: 参数
- name: Pressure regulation range
  summary: 阀门工作范围 0.1 MPa（默认）| 正标量
  group: 参数
- name: Nominal mass flow rate at maximum valve opening
  summary: 额定质量流量 0.1 kg/s（默认）| 正标量
  group: 参数
- name: Nominal pressure drop at maximum valve opening
  summary: 额定压降 0.001 MPa（默认）| 正标量
  group: 参数
- name: Nominal inlet condition specification
  summary: 确定入口流体状态的方法 Temperature（默认）| Vapor quality | Vapor void fraction | Specific enthalpy | Specific internal energy
  group: 参数
- name: Nominal inlet pressure
  summary: 入口流体压力 0.101325 MPa（默认）| 正标量
  group: 参数
- name: Nominal inlet temperature
  summary: 流体温度 293.15 K（默认）| 正标量
  group: 参数
- name: Nominal inlet vapor quality
  summary: 入口蒸汽干度质量分数 0（默认）| [0,1] 范围内的正标量
  group: 参数
- name: Nominal inlet vapor void fraction
  summary: 入口体积分数 0（默认）| [0,1] 范围内的正标量
  group: 参数
- name: Nominal inlet specific enthalpy
  summary: 入口流体比焓 400 kJ/kg（默认）| 正标量
  group: 参数
- name: Nominal inlet specific internal energy
  summary: 入口比内能 400 kJ/kg（默认）| 正标量
  group: 参数
- name: Maximum valve area
  summary: 最大阀门开口面积 1e-4 m^2（默认）| 正标量
  group: 参数
- name: 端口 B 处的压力（表压）向量
  summary: '表压向量 [0.2 : 0.2 : 1.2] MPa（默认）| 1×*n* 向量'
  group: 参数
- name: 阀门面积向量
  summary: 阀门开度面积值向量 [1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05] m^2（默认）| 1×*n* 向量
  group: 参数
- name: 流量系数
  summary: 流量系数 0.64（默认）| 正标量
  group: 参数
- name: 压力恢复
  summary: 是否考虑面积扩大时的压力升高 off（默认）| on
  group: 参数
- name: 开度特性
  summary: 用于参数化流量能力度量的方法 Linear（默认）| Tabulated
  group: 参数
- name: 最大 Cv 流量系数
  summary: 对应于组件最大开度的 *Cv* 系数 4（默认）| 正标量
  group: 参数
- name: Cv 流量系数向量
  summary: 对应于构件位置向量中值的 *Cv* 系数 [1e-06, .8, 1.6, 2.4, 3.2, 4]（默认）| 1×*n* 向量
  group: 参数
- name: 最大 Kv 流量系数
  summary: 对应于组件最大开度的 *Kv* 系数 3.6（默认）| 正标量
  group: 参数
- name: Kv 流量系数向量
  summary: 对应于构件位置向量中值的 *Kv* 系数 [1e-06, .72, 1.44, 2.16, 2.88, 3.6]（默认）| 1×*n* 向量
  group: 参数
- name: 阻塞流时的 xT 压差比系数
  summary: 压差比 0.7（默认）| 正标量
  group: 参数
- name: 最大孔口面积
  summary: 最大阀门开度面积 1e-4 m^2（默认）| 正标量
  group: 参数
- name: 孔口面积向量
  summary: 阀门开度面积值向量 [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 参数
- name: 泄漏流量分数
  summary: 流量比 1e-6（默认）| 正标量
  group: 参数
- name: 平滑因子
  summary: 数值平滑因子 0.01（默认）| 范围 [0,1] 内的正标量
  group: 参数
- name: 入口相变时间常数
  summary: 液体比容的滞后 0.1 s（默认）| 正标量
  group: 参数
- name: Laminar flow pressure ratio
  summary: 层流-湍流过渡压力比 0.999（默认值） | 正标量
  group: 参数
- name: Cross-sectional area at ports A and B
  summary: 阀端口面积 0.01 m^2（默认值） | 正标量
  group: 参数
```

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

### **Set pressure control** — 可变或恒定设定压力 `Constant`（默认）| `Controlled`

压力阈值是恒定的还是可变的。将此参数设置为 `Controlled` 将暴露物理信号端口 **Ps**。

### **Set pressure (gauge)** — 设定压力 `0.1` MPa（默认）| 正标量

阀门压力阈值。当控制压力 *pA ̶ patm* 超过设定压力时，阀门开始关闭。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition` 且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition` 且 **Opening characteristic** 设置为 `Linear`。

### **Pressure regulation range** — 阀门工作范围 `0.1` MPa（默认）| 正标量

阀门工作范围。阀门在设定压力值处开始关闭，并在 *pmax*（压力调节范围的终点）处完全打开：*pmax = pset + prange*。

#### 依赖

要启用此参数，请设置以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition` 且 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Linear - Nominal mass flow rate vs. pressure`。
- **Modeling option** 设置为 `Vapor operating condition` 且 **Opening characteristic** 设置为 `Linear`。

### **Nominal mass flow rate at maximum valve opening** — 额定质量流量 `0.1` kg/s（默认）| 正标量

在典型、设计或额定条件下通过完全打开阀门的质量流量。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **Nominal pressure drop at maximum valve opening** — 额定压降 `0.001` MPa（默认）| 正标量

在典型、设计或额定条件下完全打开阀门两端的压降。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **Nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。模块根据 **Nominal inlet pressure** 参数的值和 **Nominal inlet condition specification** 参数的设置，从表格化流体属性数据中确定孔口额定入口比容。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **Nominal inlet pressure** — 入口流体压力 `0.101325` MPa（默认）| 正标量

额定条件下的入口压力。模块根据 **Nominal inlet pressure** 参数的值和 **Nominal inlet condition specification** 参数的设置，从表格化流体属性数据中确定入口比容。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

### **Nominal inlet temperature** — 流体温度 `293.15` K（默认）| 正标量

额定运行条件下的入口流体温度。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Temperature`。

### **Nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| [0,1] 范围内的正标量

额定运行条件下入口混合物的质量分数蒸汽干度。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Vapor quality`。

### **Nominal inlet vapor void fraction** — 入口体积分数 `0`（默认）| [0,1] 范围内的正标量

额定运行条件下入口混合物的体积分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Vapor void fraction`。

### **Nominal inlet specific enthalpy** — 入口流体比焓 `400` kJ/kg（默认）| 正标量

额定运行条件下的入口比焓。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet specific internal energy** — 入口比内能 `400` kJ/kg（默认）| 正标量

额定运行条件下的入口比内能。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`，并将 **Nominal inlet condition specification** 设置为 `Specific internal energy`。

### **Maximum valve area** — 最大阀门开口面积 `1e-4 m^2`（默认）| 正标量

阀门完全打开时的最大阀门面积。

#### 依赖

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear – Area vs. pressure`。

### **端口 B 处的压力（表压）向量** — 表压向量 `[0.2 : 0.2 : 1.2] MPa`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的端口 **B** 处表压值向量。此向量中的值与 **阀门面积向量**、**孔口面积向量**、**Cv 流量系数向量** 或 **Kv 流量系数向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **建模选项** 设为 `Liquid operating condition`，且 **阀门参数化** 设为 `Tabulated data - Area vs. pressure`
- **建模选项** 设为 `Vapor operating condition`，**阀门参数化** 设为 `Orifice area`，且 **开度特性** 设为 `Tabulated`。

### **阀门面积向量** — 阀门开度面积值向量 `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05] m^2`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的孔口面积值向量。此向量中的值与 **端口 B 处的压力（表压）向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Liquid operating condition`，并将 **阀门参数化** 设为 `Tabulated data - Area vs. pressure`。

### **流量系数** — 流量系数 `0.64`（默认）| 正标量

实际流量与理想流量之比。此参数用于考虑孔口方程中未捕获的实际损耗。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **建模选项** 设为 `Liquid operating condition`，且 **阀门参数化** 设为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。
- **建模选项** 设为 `Vapor operating condition`，且 **阀门参数化** 设为 `Orifice area`。

### **压力恢复** — 是否考虑面积扩大时的压力升高 `off`（默认）| `on`

是否考虑从入口到孔口孔的压力降之后压力的微小上升。当流体射流离开孔口孔时，它会耗散并膨胀以充满端口面积，从而导致这一微小的压力上升。当您清除 **压力恢复** 复选框时，该模块不会对此压力升高进行建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Liquid operating condition`，并将 **阀门参数化** 设为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **开度特性** — 用于参数化流量能力度量的方法 `Linear`（默认）| `Tabulated`

用于对所选的流量能力度量进行蒸汽阀门参数化的方法。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Vapor operating condition`。

### **最大 Cv 流量系数** — 对应于组件最大开度的 *Cv* 系数 `4`（默认）| 正标量

当可用于流动的节流面积达到最大值时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Vapor operating condition`，**阀门参数化** 设为 `Cv flow coefficient`，并将 **开度特性** 设为 `Linear`。

### **Cv 流量系数向量** — 对应于构件位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应于 **端口 B 处的压力（表压）向量** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Vapor operating condition`，**阀门参数化** 设为 `Cv flow coefficient`，并将 **开度特性** 设为 `Tabulated`。

### **最大 Kv 流量系数** — 对应于组件最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

当可用于流动的节流面积达到最大值时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Vapor operating condition`，**阀门参数化** 设为 `Kv flow coefficient`，并将 **开度特性** 设为 `Linear`。

### **Kv 流量系数向量** — 对应于构件位置向量中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **端口 B 处的压力（表压）向量** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Vapor operating condition`，**阀门参数化** 设为 `Kv flow coefficient`，并将 **开度特性** 设为 `Tabulated`。

### **阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞时的值。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Vapor operating condition`，并将 **阀门参数化** 设为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **最大孔口面积** — 最大阀门开度面积 `1e-4 m^2`（默认）| 正标量

阀门完全打开时的最大阀门面积。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Vapor operating condition`，**阀门参数化** 设为 `Orifice area`，并将 **开度特性** 设为 `Linear`。

### **孔口面积向量** — 阀门开度面积值向量 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2`（默认）| 1×*n* 向量

用于蒸汽阀门面积表格化参数化的孔口面积值向量。此向量中的值与 **端口 B 处的压力（表压）向量** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **建模选项** 设为 `Vapor operating condition`，**阀门参数化** 设为 `Orifice area`，并将 **开度特性** 设为 `Tabulated`。

### **泄漏流量分数** — 流量比 `1e-6`（默认）| 正标量

阀门关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **建模选项** 设为 `Liquid operating condition`，且 **阀门参数化** 设为 `Linear - Nominal mass flow rate vs. pressure` 或 `Linear - Area vs. pressure`。
- **建模选项** 设为 `Vapor operating condition`，且 **开度特性** 设为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，在阀门接近打开或接近关闭位置时为流量响应引入一层渐变。将此参数设置为小于 1 的非零值，可提高这些区域中仿真的稳定性。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **建模选项** 设为 `Liquid operating condition`，且 **阀门参数化** 设为 `Linear - Nominal mass flow rate vs. pressure` 或 `Linear - Area vs. pressure`。
- **建模选项** 设为 `Vapor operating condition`，且 **开度特性** 设为 `Linear`。

### **入口相变时间常数** — 液体比容的滞后 `0.1` s（默认）| 正标量

计算流体比容时液-汽混合物的时间滞后。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`。

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认值） | 正标量

流体在层流和湍流状态之间过渡时的阀出口压力与阀入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **Cross-sectional area at ports A and B** — 阀端口面积 `0.01` m^2（默认值） | 正标量

端口 **A** 和 **B** 的面积。
## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024a: 对蒸气或液体阀进行建模

现在，当两相流体处于蒸气或液体状态时，您可以使用 **Modeling option** 参数来指定阀。两种建模选项还包含新的阀参数化方式。

当 **Modeling option** 为 `Liquid operating condition` 时，您现在可以将 **Valve parameterization** 设置为：

- `Linear - Area vs. pressure`
- `Tabulated data - Area vs. pressure`

当 **Modeling option** 为 `Vapor operating condition` 时，您现在可以将 **Valve parameterization** 设置为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

要保留以前版本的模块行为，请将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Valve parameterization** 设置为 `Linear - Nominal mass flow rate vs. pressure`。

## 描述

两相流体网络中的减压阀

Pressure-Reducing Valve (2P) 模块用于对两相流体网络中的压力控制减压阀进行建模。当端口 **B** 处的压力低于设定压力时，阀打开；当压力超过该值时，阀关闭。控制压力可以是常数，或者，当您将 **Set pressure control** 设置为 `Controlled` 时，设定压力可以根据端口 **Ps** 处的输入信号而变化。

**Modeling option** 参数控制针对蒸气或液体建模而设计的阀的参数化选项，但不会影响流体属性。该模块根据入口条件计算阀内部的流体属性。流体与环境之间没有热交换，因此节流孔内部的相变仅由压降或从模型其他部分传播的相变引起。

### 压力控制

当阀内压力 *pcontrol* 超过设定压力 *pset* 时，阀关闭。当控制压力达到 *pset* + *prange* 时，阀完全关闭，其中 *prange* 是 **Pressure regulation range** 参数的值。

对于线性参数化，该模块计算阀的开度分数 *λ*。当您将 **Set pressure control** 设置为 `Constant` 时，*λ* 为

λ=1−(1−fleak)(pcontrol−pset)prange，

其中：

- *fleak* 是 **Leakage flow fraction** 参数的值。
- *pcontrol* 是控制压力，即端口 **B** 处的压力与大气压之差。
- *pset* 是 **Set pressure (gauge)** 参数的值。

当您将 **Set pressure control** 设置为 `Controlled` 时，阀开度分数为

λ=1−(1−fleak)(pcontrol−ps)prange，

其中 *ps* 是端口 **Ps** 处信号的值。如果控制压力超过阀压力范围，则阀开度分数为 *fleak*。

### Liquid Valve

当 **Modeling option** 为 `Liquid operating
condition` 时，模块参数化取决于 **Valve parameterization** 参数的值。对于所有液体参数化选项，模块以相同方式计算压力损失和压力恢复。

临界压差 *Δpcrit* 是流动在层流和湍流之间过渡时的压差。对于所有液体参数化，*Δpcrit* 为

Δpcrit=(pA+pB)2(1−Blam),

其中：

- *pA* 和 *pB* 分别是端口 **A** 和 **B** 处的压力。
- *Blam* 是 **Laminar flow pressure ratio** 参数的值。

模块通过使用整个阀上的压力损失与紧邻阀节流面积处的压降之比来考虑压力损失。该比值 *PRloss* 为

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport,

其中：

- *Aport* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- *Avalve* 是阀面积。

压力恢复是由于孔口后面积增加而在阀中产生的正压力变化。如果你不希望捕获这种压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PRloss* 为 1，这会降低模型复杂度。如果孔口相对于端口面积非常小，或者紧邻的下游组件靠近该模块且任何射流都没有空间耗散，请清除此设置。

**Linear - Nominal Mass Flow Rate vs. Pressure Parameterization**

当你将 **Valve Parameterization** 设置为 `Nominal mass flow rate vs. pressure` 时，通过阀的质量流量为

m˙=λm˙nom[vnom2Δpnom]2vinΔp(Δp2+Δpcrit2)0.25,

其中：

- *Δp* 是阀上的压降，*pA ̶ pB*。
- m˙nom 是 **Nominal mass flow rate at maximum valve opening** 参数的值。
- *Δpnom* 是 **Nominal pressure drop rate at maximum valve opening** 参数的值。
- *vnom* 是标称入口比容。模块根据 **Nominal inlet specific enthalpy** 和 **Nominal inlet pressure** 参数，从表格化流体属性数据中确定该值。
- *vin* 是入口比容。

**Linear - Area vs. Pressure Parameterization**

当你将 **Valve parameterization** 设置为 `Linear - area vs. pressure` 时，阀面积为

Avalve=λAmax,

其中 *Amax* 是 **Maximum valve area** 参数的值。

质量流量为

m˙=CdAvalve2vinPRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4.

当阀处于接近打开或接近关闭位置时，你可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积，其中 *Aleak = fleakAmax*。有关更多信息，请参阅 Numerical Smoothing。

**Tabulated Data - Area vs. Pressure Parameterization**

当你将 **Valve Parameterization** 设置为 `Tabulated data - area vs. pressure` 时，模块从 **Valve area vector** 和 **Pressure at port B (gauge) vector** 参数中插值阀面积。

模块使用与 `Linear - Area vs. pressure` 设置相同的方程来计算体积流量。

**Fluid Specific Volume Dynamics**

对于所有参数化，模块在仿真期间基于液体状态计算流体比容。

如果阀入口处的流体是液-汽混合物，模块将比容计算为

vin=(1−xdyn)vliq+xdynvvap,

其中：

- *xdyn* 是入口蒸汽质量分数。模块对混合物的入口蒸汽质量分数应用一阶滞后。
- *vliq* 是流体的液体比容。
- *vvap* 是流体的蒸汽比容。

如果入口流体是液体或蒸汽，*vin* 是相应的液体或蒸汽比容。

如果入口蒸汽质量分数是液-汽混合物，模块应用一阶时间滞后，

dxdyndt=xin−xdynτ,

其中：

- *xdyn* 是动态蒸汽质量分数。
- *xin* 是当前入口蒸汽质量分数。
- *τ* 是 **Inlet phase change time constant** 参数的值。

如果入口流体是过冷液体，*xin = 0*。如果入口流体是过热蒸汽，*xin = 1*。

### Vapor Valve

当 **Modeling option** 为 `Vapor operating condition` 时，模块行为取决于 **Valve parameterization** 和 **Opening characteristic** 参数。

阀中的流量取决于 **Opening characteristic** 参数：

- `Linear` — 模块将流量容量的度量按 *λ* 缩放，以考虑阀开口面积。
- `Tabulated` — 模块从 **Cv flow coefficient vector**、**Kv flow coefficient vector** 或 **Orifice area vector** 参数中插值流量容量的度量。此函数使用一维查找表。

**Cv Flow Coefficient Parameterization**

当你将 **Valve parametrization** 设置为 `Cv flow coefficient` 时，质量流量为

m˙=CvN6Y(pin−pout)vin,

其中：

- *Cv* 是流量系数。
- *N6* 是常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为 kg/m3 时，其等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口压力。
- *pout* 是出口压力。
- *vin* 是入口比容。

膨胀系数为

Y=1−pin−pout3pinFγxT,

其中：

- *Fγ* 是等熵指数与 1.4 的比值。
- *xT* 是 **xT pressure differential ratio factor at choked flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CvN6Ylam1pavg(1−Blam)vavg(pin−pout),

其中：

Ylam=1−1−Blam3FγxT.

当压力比 pout/pin 降至 1−FγxT 以下时，阀发生阻塞，模块使用方程

m˙=23CvN6FγxTpinvin.

**Kv Flow Coefficient Parameterization**

当你将 **Valve parametrization** 设置为 `Kv flow coefficient` 时，模块使用与 `Cv flow coefficient` 参数化相同的方程，但使用关系 Kv=0.865Cv 将 *Cv* 替换为 *Kv*。

**Valve Area Parameterization**

当你将 **Valve parametrization** 设置为 `Orifice area` 时，质量流量为

m˙=CdAvalve2γγ−1pin1vin(poutpin)2γ[1−(poutpin)γ−1γ1−(AvalveAport)2(poutpin)2γ],

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure ratio** 参数 *Blam* 的值以上时，模块平滑过渡到方程的线性化形式，

m˙=CdAvalve2γγ−1pavg2−γγ1vavgBlam2γ[1− Blamγ−1γ1−(AvalveAport)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ).

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，阀发生阻塞，模块使用方程

m˙=CdAvalve2γγ+1pin1vin1(γ+12)2γ−1−(AvalveAport)2.

### Mass Balance

阀中质量守恒，

m˙A+m˙B=0,

其中：

- m˙A 是端口 **A** 处的质量流量。
- m˙B 是端口 **B** 处的质量流量。

### Energy Balance

阀中能量守恒，

ΦA+ΦB=0,

其中：

- *ΦA* 是端口 **A** 处的能量流。
- *ΦB* 是端口 **B** 处的能量流。

### 假设和限制

- 阀与环境之间没有热交换。
- 当 **Modeling option** 为 `Liquid operating condition` 时，结果在过冷液体区域之外可能不准确。当 **Modeling option** 为 `Vapor operating condition` 时，结果在过热蒸汽区域之外可能不准确。要对液-汽混合物中的阀建模，请将 **Modeling option** 设置为 `Liquid operating condition`。
