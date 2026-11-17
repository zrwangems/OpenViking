---
type: simulink-block
title: '4-Way 3-Position Directional Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way3positiondirectionalvalve2p'
documentation_source_path: 'ref/4way3positiondirectionalvalve2p.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 3-Position Directional Valve (2P)

## 端口

### 守恒端口

### **A** — 两相流体的入口或出口

与阀的入口或出口相关联的两相流体守恒端口。

### **B** — 两相流体的入口或出口

与阀的入口或出口相关联的两相流体守恒端口。

### **P** — 两相流体的入口或出口

与阀的入口或出口相关联的两相流体守恒端口。

### **T** — 两相流体的入口或出口

与阀的入口或出口相关联的两相流体守恒端口。

### 输入

### **S** — 阀芯位移，m，物理信号

与阀芯位移相关联的物理信号，单位为 m。

## 参数

### **Modeling option** — 流体相的建模选项 `Liquid operating condition`（默认）| `Vapor operating condition`

阀处流体相的建模选项。如果模块位置处的两相流体处于液态，则将此参数设置为 `Liquid operating condition`。如果模块位置处的两相流体处于气态，则将此参数设置为 `Vapor operating condition`。

### 阀配置

### **Positive spool position open connections** — 阀芯处于正位置时打开的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

阀芯处于正位置时打开的流路。此参数设置阀配置，并根据端口 **S** 处接收的信号定义阀芯运动方向。要检查参数设置与其他节流口的一致性，请将 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error`。

### **Neutral spool position open connections** — 阀芯处于中位时打开的流路 `All closed`（默认）| `P-A, P-B, A-T, B-T` | `A-T, B-T` | `P-A, A-T` | `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-B, B-T` | `A-T` | `B-T` | `P-A` | `P-B` | `P-T` | `P-A, A-T, P-T` | `P-A, P-B, A-B` | `P-B, B-T, P-T` | `P-A, P-B, A-T, B-T, P-T`

阀芯处于中位时打开的流路。此参数设置阀配置，并根据端口 **S** 处接收的信号定义阀芯运动方向。要检查参数设置与其他节流口的一致性，请将 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error`。

### **Negative spool position open connections** — 阀芯沿负方向运动时打开的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

阀芯沿负方向运动时打开的流路。此参数设置阀配置，并根据端口 **S** 处接收的信号定义阀芯运动方向。要检查参数设置与其他节流口的一致性，请将 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error`。

### **Consistency check for neutral spool position open connections** — 是否检查节流口设置的一致性 `Warning`（默认）| `Error` | `None`

是否检查 **Valve Configuration** 部分中的中位阀芯位置打开设置与最大节流口面积处指定的阀芯位置是否一致。对于每个启用的节流口，阀芯中位处的实际偏移应与每个单独节流口指定的阀芯偏移相匹配。

### 模型参数化

### **Area characteristics** — 节流口的流量方程 `Identical for all flow paths`（默认）| `每条流各不相同 path`

是对阀节流口面积应用统一的流量方程还是单独的流量方程。当将此参数设置为 `Identical for all flow paths` 时，模块对所有阀节流口使用相同的节流口和阀芯几何形状、流量、压力和面积向量。当将此参数设置为 `每条流各不相同 path` 时，可以为每个节流口单独指定这些参数。对于这两种设置，当将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流口 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **Orifice parameterization** — 可变或恒定节流口参数化 `Linear - Area vs. spool travel`（默认）| `Linear - Nominal mass flow rate vs. spool travel` | `Tabulated data - Area vs. spool travel` | `Cv flow coefficient` | `Kv flow coefficient` | `Orifice area`

模块用于根据节流口两端的压差计算质量流量或根据质量流量计算压差的方法。

当 **Modeling option** 为 `Liquid operating condition` 时，此参数的选项为：

- `Linear - Area vs. spool travel`
- `Linear - Nominal mass flow rate vs. spool travel`
- `Tabulated data - Area vs. spool travel`

当 **Modeling option** 为 `Vapor operating condition` 时，此参数的选项为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Linear`。

### **Maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀运行期间每个节流口的最大开口面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，且 **Opening characteristic** 设置为 `Linear`。

### **Nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` kg/s（默认）| 正标量

节流口最大开口位置处的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，且 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` MPa（默认）| 正标量

节流口最大开口位置处的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，且 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。模块根据 **Nominal inlet pressure** 和 **Nominal inlet condition specification** 参数的值，从表格化流体属性数据中确定节流口额定入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，且 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal inlet pressure** — 入口流体压力 `0.101325` MPa（默认）| 正标量

额定条件下的入口压力。模块根据 **Nominal inlet pressure** 和 **Nominal inlet condition specification** 参数的值，从表格化流体属性数据中确定入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，且 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal inlet temperature** — 流体温度 `293.15` K（默认）| 正标量

额定运行条件下的入口流体温度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Temperature`。

### **Nominal inlet vapor quality** — 入口蒸汽质量分数 `0`（默认）| [0,1] 范围内的正标量

额定运行条件下入口混合物的蒸汽质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Vapor quality`。

### **Nominal inlet vapor void fraction** — 入口体积分数 `0`（默认）| [0,1] 范围内的正标量

额定运行条件下入口混合物的体积分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Vapor void fraction`。

### **Nominal inlet specific enthalpy** — 入口流体比焓 `400` kJ/kg（默认）| 正标量

额定运行条件下的入口比焓。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet specific internal energy** — 入口比内能 `400` kJ/kg（默认）| 正标量

额定运行条件下的入口比内能。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，且 **Nominal inlet condition specification** 设置为 `Specific internal energy`。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 处指定的控制信号转换为所选流量能力度量的方法。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`。

### **Spool travel vector** — 相对于全关位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

根据表格化阀面积数据参数化节流口时的阀芯行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

根据表格化阀面积数据参数化节流口时的开口面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。按升序列出值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应最大开度组件的 *Cv* 系数 `4`（默认）| 正标量

节流口完全打开且可用流动面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Cv flow coefficient`，且 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 构件位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **Control member position vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Cv flow coefficient`，且 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应最大开度组件的 *Kv* 系数 `3.6`（默认）| 正标量

节流口完全打开且可用流动面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Identical for all flow paths`，**Orifice parameterization** 设置为 `Kv flow coefficient`，且 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 构件位置向量中各值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **Control member position vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，即首次发生阻塞流时的值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正系数。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition` 并将 **Orifice parameterization** 设置为 `Orifice area`，或者将 **Modeling option** 设置为 `Liquid operating condition` 并将 **Orifice parameterization** 设置为以下之一：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Leakage flow fraction** — 流量比 `1e-6`（默认）| 正标量

节流口关闭时与打开时的流量之比。

#### 依赖关系

要启用此参数，请设置以下之一：

- **Modeling option** 设置为 `Liquid operating condition`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，并将 **Opening characteristic** 设置为 `Linear`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，基于阀门接近打开和接近关闭位置时的流量响应引入一层渐变。为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition` 并将 **Orifice parametrization** 设置为 `Linear - area vs. spool travel`，或者将 **Modeling option** 设置为 `Vapor operating condition` 并将 **Opening characteristic** 设置为 `Linear`。

### **Pressure recovery** — 是否考虑面积扩大时的压力升高 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力升高。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition` 并将 **Orifice parameterization** 设置为以下之一：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Laminar flow pressure ratio** — 层流-湍流过渡压力比 `0.999`（默认）| 正标量

流体在层流和湍流之间过渡时的节流口出口压力与入口压力之比。在层流中，压力损失与质量流量成线性关系；在湍流中，压力损失与质量流量成二次关系。

### **Inlet phase change time constant** — 混合物比容时间滞后 `0.1` `s`（默认）| 正标量

计算流体比容时液-汽混合物的时间滞后。当入口流体为完全过冷液体或完全过热蒸汽时，此参数不影响比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`。

### **Cross-sectional area at ports P, T, A and B** — 守恒端口处的面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀门的质量流量的压力-流量方程中使用该值。

### P-A Orifice

### **Spool position at maximum P-A orifice area** — P-A 节流口完全打开时的阀芯偏移 `5e-3 m`（默认）| 正标量

P-A 节流口完全打开时阀芯从中位开始的偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一。

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**注意：**

仅当 P-A 节流口设置未同时出现在全部三个阀芯位置参数中时，此参数才启用：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-A spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

并且满足以下之一：

- **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `每条流各不相同 path`，**Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `每条流各不相同 path`，**Opening characteristic** 设置为 `Linear`。

### **P-A nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大开度 P-A 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流各不相同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大开度 P-A 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流各不相同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 P-A 节流口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流各不相同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

P-A 节流口在额定工况下的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流各不相同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

P-A 节流口在额定工况下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流各不相同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Temperature`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| [0,1] 范围内的正标量

P-A 节流口在额定工况下入口混合物的蒸汽干度质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流各不相同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Vapor quality`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A nominal inlet vapor void fraction** — 入口蒸汽空泡率 `0`（默认）| [0,1] 范围内的正标量

P-A 节流口在额定工况下入口混合物的蒸汽空泡率。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流各不相同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Vapor void fraction`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

P-A 节流口在额定工况下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `每条流各不相同 path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Specific enthalpy`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

P-A 节流口在额定工况下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Specific
   internal energy`
5. 以下参数中的至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A constant orifice nominal mass flow rate** — 标称质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 P-A 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 节流口设置出现在所有三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-A constant orifice nominal pressure drop** — 标称压降 `0.001` `MPa`（默认）| 正标量

通过恒定 P-A 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 节流口设置出现在所有三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-A constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

P-A 节流口的恒定 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 节流口设置出现在所有三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-A orifice maximum Cv flow coefficient** — 对应最大开启组件的 *Cv* 系数 `4`（默认）| 正标量

P-A 节流口完全打开且可用流动面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice Cv flow coefficient vector** — 成员位置向量中值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数的向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

P-A 节流口的恒定 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 节流口设置出现在所有三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-A orifice maximum Kv flow coefficient** — 对应最大开启组件的 *Kv* 系数 `3.6`（默认）| 正标量

P-A 节流口完全打开且可用流动面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice Kv flow coefficient vector** — 成员位置向量中值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T,
     P-T`
   - `P-A, P-B,
     A-B`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A orifice spool travel vector** — 相对于全关位置的滑阀开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的滑阀行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **P-A maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-A 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Linear`。

### **P-A orifice area vector** — 阀口开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的开启面积向量。向量元素必须与 **P-A orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **P-A constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正负滑阀位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下设置之一：

**正阀芯位置开启连接**设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **建模选项**设置为 `Liquid operating condition`，**面积特性**设置为 `每条流各不相同 path`，且**孔口参数化**设置为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- **建模选项**设置为 `Vapor operating condition`，**面积特性**设置为 `每条流各不相同 path`，且**开启特性**设置为 `Tabulated`。

**注意：**

仅当 P-A 孔口设置出现在全部三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **P-A orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-A 孔口首次发生阻塞流。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Vapor operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
4. 以下参数中至少一个：

   **正阀芯位置开启连接**设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### P-B Orifice

### **Spool position at maximum P-B orifice area** — 完全打开 P-B 孔口时的阀芯偏移 `5e-3 m`（默认）| 正标量

完全打开 P-B 孔口时阀芯相对于中位位置的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接**设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**注意：**

仅当 P-B 孔口设置未出现在全部三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接**设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接**设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **建模选项**设置为 `Liquid operating condition`，**面积特性**设置为 `每条流各不相同 path`，且**孔口参数化**设置为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **建模选项**设置为 `Vapor operating condition`，**面积特性**设置为 `每条流各不相同 path`，且**开启特性**设置为 `Linear`。

### **P-B nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大开启 P-B 孔口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Liquid operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大开启 P-B 孔口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Liquid operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 P-B 孔口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Liquid operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

P-B 孔口在额定条件下的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Liquid operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

P-B 孔口在额定运行条件下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Liquid operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件规格**设置为 `Temperature`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B nominal inlet vapor quality** — 入口蒸汽质量分数 `0`（默认）| [0,1] 范围内的正标量

P-B 孔口在额定运行条件下的入口混合物蒸汽质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Liquid operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件规格**设置为 `Vapor quality`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B nominal inlet vapor void fraction** — 入口蒸汽空隙率 `0`（默认）| [0,1] 范围内的正标量

P-B 孔口在额定运行条件下的入口混合物蒸汽空隙率。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Liquid operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件规格**设置为 `Vapor void fraction`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

P-B 孔口在额定运行条件下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Liquid operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件规格**设置为 `Specific enthalpy`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

P-B 孔口在额定运行条件下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**设置为 `Liquid operating condition`
2. **面积特性**设置为 `每条流各不相同 path`
3. **孔口参数化**设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件规格**设置为 `Specific internal energy`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B constant orifice nominal mass flow rate** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 P-B 孔口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-B 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-B constant orifice nominal pressure drop** — 标称压降 `0.001` `MPa`（默认）| 正标量

通过恒定 P-B 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-B 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-B constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

P-B 节流口的恒定 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-B 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum Cv flow coefficient** — 对应最大开度的 *Cv* 系数 `4`（默认）| 正标量

P-B 节流口完全打开且可用流通面积为最大值时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice Cv flow coefficient vector** — 对应构件位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

P-B 节流口的恒定 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-B 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum Kv flow coefficient** — 对应最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

P-B 节流口完全打开且可用流通面积为最大值时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice Kv flow coefficient vector** — 对应构件位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B orifice spool travel vector** — 相对于全关位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的滑阀行程距离向量。按升序列出各值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **P-B maximum orifice area** — 最大节流口开度面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-B 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Linear`。

### **P-B orifice area vector** — 阀口开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的开度面积向量。向量元素必须与 **P-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **P-B constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正滑阀位置和负滑阀位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel` 或 `Linear - Area vs.
  spool travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

**注意：**

仅当 P-B 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **P-B orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-B 节流口首次发生阻塞流。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
4. 以下参数中的至少一个：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### A-B Orifice

### **Spool position at maximum A-B orifice area** — 完全打开 A-B 节流口的滑阀偏移 `5e-3 m`（默认）| 正标量

从中间位置到完全打开 A-B 节流口的滑阀偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-B`

**注意：**

仅当 A-B 节流口设置未同时出现在以下三个滑阀位置参数中时，才启用此参数：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-B spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认）| 正标量

滑阀行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-B`

并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel` 或 `Linear - Nominal
  mass flow rate vs. spool travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Linear`。

### **A-B nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大打开 A-B 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大打开 A-B 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 A-B 节流口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中的至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

A-B 节流口在额定条件下的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中的至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

A-B 节流口在额定工况下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为
   `Temperature`
5. 以下参数中的至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| [0,1] 范围内的正标量

A-B 节流口在额定工况下的入口混合物蒸汽干度质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Vapor
   quality`
5. 以下参数中的至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B nominal inlet vapor void fraction** — 入口蒸汽空泡率 `0`（默认）| [0,1] 范围内的正标量

A-B 节流口在额定工况下的入口混合物蒸汽空泡率。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Vapor void
   fraction`
5. 以下参数中的至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

A-B 节流口在额定工况下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Specific
   enthalpy`
5. 以下参数中的至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

A-B 节流口在额定工况下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Specific
   internal energy`
5. 以下参数中的至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B constant orifice nominal mass flow rate** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 A-B 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

**注意：**

仅当 A-B 节流口设置同时出现在以下三个滑阀位置参数中时，才启用此参数：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-B constant orifice nominal pressure drop** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过恒定 A-B 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

**注意：**

仅当 A-B 节流口设置同时出现在以下三个滑阀位置参数中时，才启用此参数：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-B constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

A-B 节流口的恒定 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. 每个参数中的以下设置之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

**注意：**

仅当 A-B 节流口设置同时出现在以下三个滑阀位置参数中时，才启用此参数：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-B orifice maximum Cv flow coefficient** — 对应于组件最大打开状态的 *Cv* 系数 `4`（默认）| 正标量

A-B 节流口完全打开且可用流动面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B orifice Cv flow coefficient vector** — 成员位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数的向量。每个系数对应于 **A-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-B orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

A-B 节流口的恒定 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

**注意：**

仅当 A-B 节流口设置出现在全部三个阀芯位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-B orifice maximum Kv flow coefficient** — 对应最大开度组件的 *Kv* 系数 `3.6`（默认）| 正标量

当 A-B 节流口完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B orifice Kv flow coefficient vector** — 成员位置向量中值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应 **A-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-B orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### **A-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-B`

并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **A-B maximum orifice area** — 最大节流口开度面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 A-B 节流口的最大开度面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-B`

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Linear`。

### **A-B orifice area vector** — 阀口开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的开度面积向量。向量元素必须与 **A-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-B`

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **A-B constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正阀芯位置和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-B`

并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel` 或 `Linear - Area vs.
  spool travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

**注意：**

仅当 A-B 节流口设置出现在全部三个阀芯位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-B orifice xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

A-B 节流口首次发生阻塞流时的入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
4. 以下参数中至少一个：

   **Positive spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Neutral spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

   **Negative spool position open
   connections** 为：

   - `P-A, P-B,
     A-B`

### A-T 节流口

### **Spool position at maximum A-T orifice area** — 完全打开 A-T 节流口时的阀芯偏移 `5e-3 m`（默认）| 正标量

完全打开 A-T 节流口时阀芯相对于中位位置的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- **Positive spool position open
  connections** 为 `P-B,
  A-T`。
- **Neutral spool position open
  connections** 为：

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 为 `P-B,
  A-T`。

**注意：**

仅当 A-T 节流口设置未出现在全部三个阀芯位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-B,
  A-T`。
- **Neutral spool position open
  connections** 为：

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 为 `P-B,
  A-T`。

并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel` 或 `Linear - Nominal
  mass flow rate vs. spool travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Linear`。

### **A-T nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大开度 A-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大开度 A-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 A-T 节流口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

A-T 节流口在额定工况下的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

A-T 节流口在额定工况下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为
   `Temperature`
5. 以下参数中至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| [0,1] 范围内的正标量

A-T 节流口在额定工况下的入口混合物蒸汽干度质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Vapor
   quality`
5. 以下参数中至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T nominal inlet vapor void fraction** — 入口蒸汽空隙率 `0`（默认）| [0,1] 范围内的正标量

A-T 节流口在额定工况下的入口混合物蒸汽空隙率。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Vapor void
   fraction`
5. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

A-T 节流口在标称工况下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Specific
   enthalpy`
5. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

A-T 节流口在标称工况下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Specific
   internal energy`
5. 以下参数中的至少一个：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T constant orifice nominal mass flow rate** — 标称质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 A-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

**注意：**

仅当 A-T 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-T constant orifice nominal pressure drop** — 标称压降 `0.001` `MPa`（默认）| 正标量

通过恒定 A-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

**注意：**

仅当 A-T 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

A-T 节流口的恒定 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

**注意：**

仅当 A-T 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-T orifice maximum Cv flow coefficient** — 对应组件最大开度的 *Cv* 系数 `4`（默认）| 正标量

A-T 节流口完全打开且可用流通面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T orifice Cv flow coefficient vector** — 对应构件位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **A-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-T orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

A-T 节流口的恒定 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

**注意：**

仅当 A-T 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-T orifice maximum Kv flow coefficient** — 对应组件最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

A-T 节流口完全打开且可用流通面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T orifice Kv flow coefficient vector** — 对应构件位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **A-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **A-T orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-B,
     A-T`。

### **A-T orifice spool travel vector** — 相对于全关位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格化参数化的滑阀行程距离向量。按升序列出各值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-B,
  A-T`。
- **Neutral spool position open
  connections** 为：

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 为 `P-B,
  A-T`。

并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **A-T maximum orifice area** — 最大节流口开度面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 A-T 节流口的最大开度面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-B,
  A-T`。
- **Neutral spool position open
  connections** 为：

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 为 `P-B,
  A-T`。

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Linear`。

### **A-T orifice area vector** — 阀开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀面积表格化参数化的开度面积向量。向量元素必须与 **A-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-B,
  A-T`。
- **Neutral spool position open
  connections** 为：

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 为 `P-B,
  A-T`。

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **A-T constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正负滑阀位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下设置之一：

- **Positive spool position open
  connections** 设为 `P-B,
  A-T`。
- **Neutral spool position open
  connections** 设为：

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 设为 `P-B,
  A-T`。

并且满足以下任一条件：

- **Modeling option** 设为
  `Liquid operating condition`，
  **Area characteristics** 设为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 设为
  `Tabulated data - Area vs. spool
  travel` 或 `Linear - Area vs.
  spool travel`。
- **Modeling option** 设为 `Vapor
  operating condition`，**Area
  characteristics** 设为 `Different for
  each flow path`，且 **Opening
  characteristic** 设为
  `Tabulated`。

**注意：**

仅当 A-T 节流口设置出现在全部三个阀芯位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-T orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

A-T 节流口首次发生阻塞流时，入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Vapor operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
4. 以下参数中至少一个：

   - **Positive spool position open
     connections** 设为 `P-B,
     A-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-B,
     A-T`。

### B-T Orifice

### **Spool position at maximum B-T orifice area** — 完全打开 B-T 节流口的阀芯偏移量 `5e-3 m`（默认）| 正标量

完全打开 B-T 节流口时阀芯相对于中位位置的偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- **Positive spool position open
  connections** 设为 `P-A,
  B-T`。
- **Neutral spool position open
  connections** 设为：

  - `P-A, P-B, A-T,
    B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 设为 `P-A,
  B-T`。

**注意：**

仅当 B-T 节流口设置未出现在全部三个阀芯位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 设为 `P-A,
  B-T`。
- **Neutral spool position open
  connections** 设为：

  - `P-A, P-B, A-T,
    B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 设为 `P-A,
  B-T`。

并且满足以下任一条件：

- **Modeling option** 设为
  `Liquid operating condition`，
  **Area characteristics** 设为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 设为
  `Linear - Area vs. spool
  travel` 或 `Linear - Nominal
  mass flow rate vs. spool travel`。
- **Modeling option** 设为 `Vapor
  operating condition`，**Area
  characteristics** 设为 `Different for
  each flow path`，且 **Opening
  characteristic** 设为
  `Linear`。

### **B-T nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大开度 B-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

### **B-T nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大开度 B-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

### **B-T nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 B-T 节流口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中至少一个：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

### **B-T nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

B-T 节流口在额定工况下的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中至少一个：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

### **B-T nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

B-T 节流口在额定工况下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 设为
   `Temperature`
5. 以下参数中至少一个：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

### **B-T nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| [0,1] 范围内的正标量

B-T 节流口在额定工况下的入口混合物蒸汽干度质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 设为 `Vapor
   quality`
5. 以下参数中至少一个：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

### **B-T nominal inlet vapor void fraction** — 入口蒸汽空泡率 `0`（默认）| [0,1] 范围内的正标量

B-T 节流口在额定工况下的入口混合物蒸汽空泡率。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 设为 `Vapor void
   fraction`
5. 以下参数中至少一个：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

### **B-T nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

B-T 节流口在额定工况下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 设为 `Specific
   enthalpy`
5. 以下参数中至少一个：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

### **B-T nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

B-T 节流口在额定工况下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 设为 `Specific
   internal energy`
5. 以下参数中至少一个：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

### **B-T constant orifice nominal mass flow rate** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 B-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在全部三个阀芯位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T constant orifice nominal pressure drop** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过恒定 B-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设为
   `Liquid operating
   condition`
2. **Area characteristics** 设为
   `每条流各不相同
   path`
3. **Orifice parameterization** 设为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中的以下设置之一：

   - **Positive spool position open
     connections** 设为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 设为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 设为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在全部三个阀芯位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

B-T 节流口的恒定 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T orifice maximum Cv flow coefficient** — 对应最大开度 component `4` 的 *Cv* 系数（默认）| 正标量

当 B-T 节流口完全打开且可用流动面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T orifice Cv flow coefficient vector** — 对应成员位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数的向量。每个系数对应 **B-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **B-T orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

B-T 节流口的恒定 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T orifice maximum Kv flow coefficient** — 对应最大开度 component `3.6` 的 *Kv* 系数（默认）| 正标量

当 B-T 节流口完全打开且可用流动面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T orifice Kv flow coefficient vector** — 对应成员位置向量中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数的向量。每个系数对应 **B-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **B-T orifice spool travel
vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### **B-T orifice spool travel vector** — 相对于全闭位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的滑阀行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T`。
- **Neutral spool position open
  connections** 为：

  - `P-A, P-B, A-T,
    B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 为 `P-A,
  B-T`。

并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **B-T maximum orifice area** — 最大节流口开度面积 `1e-4 m^2`（默认）| 正标量

阀门工作期间 B-T 节流口的最大开度面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T`。
- **Neutral spool position open
  connections** 为：

  - `P-A, P-B, A-T,
    B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 为 `P-A,
  B-T`。

同时设置 **Area characteristics** 为
`每条流各不相同 path`，并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Linear`。

### **B-T orifice area vector** — 阀口开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的开度面积向量。向量元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T`。
- **Neutral spool position open
  connections** 为：

  - `P-A, P-B, A-T,
    B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 为 `P-A,
  B-T`。

同时设置 **Area characteristics** 为
`每条流各不相同 path`，并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **B-T constant orifice area** — 恒定节流口横截面积 `1e-4 m^2`（默认）| 正标量

当正负滑阀位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T`。
- **Neutral spool position open
  connections** 为：

  - `P-A, P-B, A-T,
    B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T,
    P-T`
  - `P-A, P-B, A-T, B-T,
    P-T`
- **Negative spool position open
  connections** 为 `P-A,
  B-T`。

并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel` 或 `Linear - Area vs.
  spool travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

**注意：**

仅当 B-T 节流口设置出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **B-T orifice xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 B-T 节流口首次发生阻塞流。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
4. 以下参数中至少一个：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T`。
   - **Neutral spool position open
     connections** 为：

     - `P-A, P-B, A-T,
       B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T,
       P-T`
     - `P-A, P-B, A-T, B-T,
       P-T`
   - **Negative spool position open
     connections** 为 `P-A,
     B-T`。

### P-T Orifice

### **Spool position at maximum P-T orifice area** — P-T 节流口完全打开时的滑阀偏移 `5e-3 m`（默认）| 正标量

P-T 节流口完全打开时相对于中位位置的滑阀偏移。

#### 依赖关系

要启用此参数，请设置 **Neutral spool position
open connections** 为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

### **P-T spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认）| 正标量

滑阀行程的最大距离。此值为计算提供上限，以确保仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置 **Neutral spool position
open connections** 为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

并且满足以下之一：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel` 或 `Linear - Nominal
  mass flow rate vs. spool travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Linear`。

### **P-T nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大开度 P-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大开度 P-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 P-T 节流口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

P-T 节流口在额定条件下的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

P-T 节流口在标称工况下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为
   `Temperature`
5. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet vapor quality** — 入口蒸汽质量分数 `0`（默认）| [0,1] 范围内的正标量

P-T 节流口在标称工况下的入口混合物蒸汽质量分数。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Vapor
   quality`
5. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet vapor void fraction** — 入口蒸汽空泡率 `0`（默认）| [0,1] 范围内的正标量

P-T 节流口在标称工况下的入口混合物蒸汽空泡率。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Vapor void
   fraction`
5. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

P-T 节流口在标称工况下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Specific
   enthalpy`
5. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

P-T 节流口在标称工况下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition
   specification** 为 `Specific
   internal energy`
5. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice maximum Cv flow coefficient** — 对应最大开度的 *Cv* 系数 `4`（默认）| 正标量

P-T 节流口完全打开且流通面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice Cv flow coefficient vector** — 对应构件位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **P-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice maximum Kv flow coefficient** — 对应最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

P-T 节流口完全打开且流通面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice Kv flow coefficient vector** — 对应构件位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **P-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice spool travel vector** — 相对于全关位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的阀芯行程距离向量。按升序列出各值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Neutral spool position
open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  **Area characteristics** 为
  `每条流各不相同 path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **P-T maximum orifice area** — 最大节流口开度面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-T 节流口的最大开度面积。

#### 依赖关系

要启用此参数，请将 **Neutral spool position
open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  且 **Orifice parameterization** 为
  `Linear - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Linear`。

### **P-T orifice area vector** — 阀口开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀口面积表格化参数化的开度面积向量。向量元素必须与 **P-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请将 **Neutral spool position
open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

同时将 **Area characteristics** 设置为
`每条流各不相同 path`，并且满足以下任一条件：

- **Modeling option** 为
  `Liquid operating condition`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Orifice
  parameterization** 为 `Orifice
  area`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **P-T orifice xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

P-T 节流口首次发生阻塞流时入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `每条流各不相同
   path`
3. **Orifice parameterization** 为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
4. **Neutral spool position open
   connections** 为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

两相流体域中的四通三位方向阀

4-Way 3-Position Directional Valve (2P) 模块对两相流体网络中具有四个开口的阀门进行建模，通常位于执行器、泵和油箱之间。单个阀芯根据端口 **S** 处的信号控制阀门操作。您可以通过在 **Neutral spool position open connections** 参数中指定阀芯处于中位（居中于 0 m）时打开的节流口、在 **Positive spool position open connections** 参数中指定阀芯向正方向移动时打开的节流口、在 **Negative spool position open connections** 参数中指定阀芯向负方向移动时打开的节流口，来设置阀门的基线配置。您可以使用 **Orifice parameterization** 参数将阀门模型指定为线性关系或用户提供数据的函数。

此模块是一个复合组件，由多个 Orifice (2P) 模块实例组成。有关阀门参数化和模块计算的更多信息，请参阅 Orifice (2P) 模块。

在此示例配置中，**Neutral spool position open connections** 参数为 `All closed`。当阀芯处于中位时，所有节流口均关闭，无流量通过：

在此配置中，**Negative spool position open connections** 为 `P-A, B-T`。当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径打开，允许流量通过。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径关闭，无流量通过：

在此配置中，**Positive spool position open connections** 为 `P-B, A-T`。当端口 **S** 处的信号将阀芯移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径打开，允许流量通过，而端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径关闭：

此示意图展示了此配置：

左侧对应正位置，右侧对应负位置。

### 滑阀位移与阀配置

*滑阀行程*是指节流口从关闭位置到完全打开所需的滑阀移动量。您可以使用**阀配置**部分中的参数来定义滑阀行程。下表显示了模块如何根据阀节流口参数化和流路特性来计算行程。

由端口 **S** 指定的滑阀移动方向取决于滑阀行程和节流口方向。

| 节流口打开时的滑阀位置 | 滑阀移动量，*ΔS* |
| --- | --- |
| 始终关闭（在任何滑阀位置配置中均未选择该节流口） | 不适用 |
| 始终打开（在正、中性和负滑阀位置配置中均选择了该节流口） | 不适用 |
| 负 | *S*orifice\_max + 滑阀行程 – **S** |
| 负和中性 | *S*orifice\_max + 滑阀行程 – **S** |
| 正 | *S*orifice\_max – 滑阀行程 + **S** |
| 正和中性 | *S*orifice\_max – 滑阀行程 + **S** |
| 中性 | \|*S*orifice\_max\| + 滑阀行程 – \|**S**\| |
| 正和负 | –\|*S*orifice\_max\| + 滑阀行程 – \|**S**\| |

*S*orifice\_max 是为每个节流口定义的最大节流口面积处的滑阀位置。当 *ΔS* 为负时，节流口面积饱和于泄漏面积；当节流口完全打开时，节流口面积饱和于最大节流口面积。当节流口完全打开时，*ΔS* 等于滑阀行程，因此 *ΔS* 大于滑阀行程的值不会进一步增大节流口面积。

**中性滑阀位置打开连接的一致性检查**参数验证以下内容：

- 在**中性滑阀位置打开连接**中列出的任何节流口在 **S** 处信号为 0 时打开
- 未在**中性滑阀位置打开连接**中列出的任何节流口在 **S** 处信号为 0 时关闭

您可以选择在任何滑阀位置违反此检查时接收警告或错误。

下表显示了 4-Way 3-Position Directional Valve (TL) 模块的可能配置。

| 配置 | 参数值 |
| --- | --- |
|  | 在中性位置，所有四个节流口均关闭。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：`All   closed` - **负滑阀位置打开连接**：`P-B,   A-T`    - **最大 P-A 节流口面积处的滑阀位置** > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < –P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** < –A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** > B-T 滑阀行程 |
|  | 在中性位置，所有四个节流口均打开。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：`P-A, P-B,   A-T, B-T` - **负滑阀位置打开连接**：`P-B,   A-T`    - **最大 P-A 节流口面积处的滑阀位置** < P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** > –P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** > –A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** < B-T 滑阀行程 |
|  | 节流口 A-T 和 B-T 关闭。节流口 P-A 和 P-B 重叠。  - **正滑阀位置打开连接**：  `P-A` - **中性滑阀位置打开连接**：`All   closed` - **负滑阀位置打开连接**：  `P-B`    - **最大 P-A 节流口面积处的滑阀位置** > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < –P-B 滑阀行程 |
|  | 节流口 A-T 和 B-T 打开。节流口 P-A 和 P-B 重叠。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：`A-T,   B-T` - **负滑阀位置打开连接**：`P-B,   A-T`    - **最大 P-A 节流口面积处的滑阀位置** > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < –P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** > –A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** < B-T 滑阀行程 |
|  | 在中性位置，节流口 P-A 和 A-T 打开。节流口 P-B 和 B-T 重叠。  - **正滑阀位置打开连接**：`P-B,   A-T` - **中性滑阀位置打开连接**：`P-A,   A-T` - **负滑阀位置打开连接**：`P-A,   B-T`    - **最大 P-A 节流口面积处的滑阀位置** < P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** > P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** > A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** < –B-T 滑阀行程 |
|  | 在中性位置，节流口 A-T 打开。节流口 P-B、A-T 和 B-T 重叠。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：  `A-T` - **负滑阀位置打开连接**：`P-B,   A-T`    - **最大 P-A 节流口面积处的滑阀位置** > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < –P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** > –A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** > B-T 滑阀行程 |
|  | 在中性位置，节流口 B-T 打开。节流口 P-A、P-B 和 A-T 重叠。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：  `B-T` - **负滑阀位置打开连接**：`P-B,   A-T`    - **最大 P-A 节流口面积处的滑阀位置** > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < –P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** < –A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** < B-T 滑阀行程 |
|  | 节流口 P-A 和 P-B 打开。节流口 A-T 和 B-T 重叠。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：`P-A,   P-B` - **负滑阀位置打开连接**：`P-B,   A-T`    - **最大 P-A 节流口面积处的滑阀位置** < P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** > –P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** < –A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** > B-T 滑阀行程 |
|  | 在中性位置，节流口 P-A 打开。节流口 P-B、A-T 和 B-T 重叠。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：  `P-A` - **负滑阀位置打开连接**：`P-B,   A-T`    - **最大 P-A 节流口面积处的滑阀位置** < P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < –P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** < –A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** > B-T 滑阀行程 |
|  | 在中性位置，节流口 P-B 打开。节流口 P-A、A-T 和 B-T 重叠。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：  `P-B` - **负滑阀位置打开连接**：`P-B,   A-T`    - **最大 P-A 节流口面积处的滑阀位置** > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** > –P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** < –A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** > B-T 滑阀行程 |
|  | 在中性位置，节流口 P-B 和 B-T 打开。节流口 P-A 和 A-T 重叠。  - **正滑阀位置打开连接**：`P-B,   A-T` - **中性滑阀位置打开连接**：`P-B,   B-T` - **负滑阀位置打开连接**：`P-A,   B-T`    - **最大 P-A 节流口面积处的滑阀位置** < –P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** > A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** > –B-T 滑阀行程 |
|  | 在中性位置，节流口 P-A、P-B、A-T 和 B-T 关闭。P-T 在中性位置打开，并在滑阀位移时关闭。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：  `P-T` - **负滑阀位置打开连接**：`P-B,   A-T`    - **最大 P-A 节流口面积处的滑阀位置** > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < –P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** < –A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** > B-T 滑阀行程 - **最大 P-T 节流口面积处的滑阀位置** = 任意值 |
|  | 节流口 P-A 是恒定节流口。节流口 P-B、A-T 和 B-T 在中性位置打开。  - **正滑阀位置打开连接**：`P-A,   P-B` - **中性滑阀位置打开连接**：`P-A, P-B,   A-T, B-T` - **负滑阀位置打开连接**：`P-A,   B-T`    - **最大 P-A 节流口面积处的滑阀位置** < P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** = 任意值 - **最大 B-T 节流口面积处的滑阀位置** > –B-T 滑阀行程 |
|  | 节流口 P-B 是恒定节流口。节流口 P-A、A-T、B-T 在中性位置打开。    - **正滑阀位置打开连接**：`P-B,   A-T` - **中性滑阀位置打开连接**：`P-A, P-B,   A-T, B-T` - **负滑阀位置打开连接**：`P-A,   P-B`    - **最大 P-A 节流口面积处的滑阀位置** > –P-A 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** < A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** = 任意值 |
|  | 在中性位置，节流口 P-A 关闭。端口 **A** 和 **T** 不形成流路。  - **正滑阀位置打开连接**：`P-A,   P-B` - **中性滑阀位置打开连接**：`All   closed` - **负滑阀位置打开连接**：`P-A,   B-T`  - \|**最大 P-A 节流口面积处的滑阀位置**\| > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** > P-B 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** < –B-T 滑阀行程 |
|  | 在中性位置，节流口 P-B 关闭。端口 **B** 和 **T** 不形成流路。  - **正滑阀位置打开连接**：`P-B,   A-T` - **中性滑阀位置打开连接**：`All   closed` - **负滑阀位置打开连接**：`P-A,   P-B`  - **最大 P-A 节流口面积处的滑阀位置** < –P-A 滑阀行程 - \|**最大 P-B 节流口面积处的滑阀位置**\| > P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** > A-T 滑阀行程 |
|  | 在中性位置，节流口 P-A 关闭。在中性位置，节流口 A-T 打开。  - **正滑阀位置打开连接**：`P-A,   P-B` - **中性滑阀位置打开连接**：`A-T,   B-T` - **负滑阀位置打开连接**：`P-A,   B-T`  - \|**最大 P-A 节流口面积处的滑阀位置**\| > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** > P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** = 任意值 - **最大 B-T 节流口面积处的滑阀位置** > –B-T 滑阀行程 |
|  | 在中性位置，节流口 P-B 关闭。在中性位置，节流口 B-T 打开。  - **正滑阀位置打开连接**：`P-B,   A-T` - **中性滑阀位置打开连接**：`A-T,   B-T` - **负滑阀位置打开连接**：`P-A,   P-B`  - **最大 P-A 节流口面积处的滑阀位置** < –P-A 滑阀行程 - \|**最大 P-B 节流口面积处的滑阀位置**\| > P-B 滑阀行程 - **最大 A-T 节流口面积处的滑阀位置** < A-T 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** = 任意值 |
|  | 在中性位置，节流口 P-B 关闭。在中性位置，节流口 P-T 打开。端口 **A** 和 **T** 不形成流路。  - **正滑阀位置打开连接**：`P-A,   P-B` - **中性滑阀位置打开连接**：  `P-T` - **负滑阀位置打开连接**：`P-B,   A-T`  - **最大 P-A 节流口面积处的滑阀位置** > P-A 滑阀行程 - \|**最大 P-B 节流口面积处的滑阀位置**\| > P-B 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** < –B-T 滑阀行程 - **最大 P-T 节流口面积处的滑阀位置** = 任意值 |
|  | 在中性位置，节流口 P-A 关闭。在中性位置，节流口 P-T 打开。端口 **A** 和 **T** 不形成流路。  - **正滑阀位置打开连接**：`P-A,   B-T` - **中性滑阀位置打开连接**：  `P-T` - **负滑阀位置打开连接**：`P-A,   P-B`  - \|**最大 P-A 节流口面积处的滑阀位置**\| > P-A 滑阀行程 - **最大 P-B 节流口面积处的滑阀位置** < –P-B 滑阀行程 - **最大 B-T 节流口面积处的滑阀位置** > B-T 滑阀行程 - **最大 P-T 节流口面积处的滑阀位置** = 任意值 |

### 阀门节流口参数化

**建模选项**参数控制对建模为蒸汽或液体的阀门进行参数化的选项，但不会影响流体属性。该模块根据入口条件计算阀门内部的流体属性。

**节流口参数化**参数指定一个或所有阀门节流口的开口面积或流量的模型。如果将**面积特性**设置为`所有流路相同`，则该模块对所有流路应用相同的数据。当选择`所有流路不同`时，该模块对每条流路使用单独的参数化。

**液体阀门参数化**

当**建模选项**为`液体工况`时，该模块参数化对控制液体流量的阀门进行建模。

当**节流口参数化**为`线性 - 面积与阀芯行程的关系`时，开口面积是作为端口 **S** 处信号接收的阀芯位置的线性函数

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak，

其中：

- *ΔS* 是阀芯行程。

  *Aorifice* 在 *ΔS* 为负时饱和于 *Aleak*，在节流口完全打开时饱和于 *Amax*。当节流口完全打开时，*ΔS* 等于阀芯行程，因此大于阀芯行程的 *ΔS* 值不会增加节流口面积。
- *ΔSmax* 是**节流口关闭与打开之间的阀芯行程**参数的值。
- *Amax* 是**最大节流口面积**参数的值。
- *Aleak* 是**泄漏面积**参数的值。

  当阀门在线性参数化中处于接近打开或接近关闭的位置时，可以通过调整**平滑因子**参数来保持仿真中的数值鲁棒性。如果**平滑因子**参数非零，则该模块在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关详细信息，请参阅数值平滑。

当**节流口参数化**为`表格数据 - 面积与阀芯行程的关系`时，可以为系统或端口 **P**、**A**、**B** 和 **T** 之间的各条流路提供阀芯行程向量。该模块使用此数据计算节流口面积与阀芯位移之间的关系。该模块使用插值来确定给定数据点之间的开口面积。*Aleak* 和 *Amax* 分别是开口面积向量的第一个和最后一个参数。

当**节流口参数化**为`表格数据 - 额定质量流量与阀芯行程的关系`时，该模块根据在模块参数中指定的额定条件计算每个节流口的质量流量。来自端口 **S** 的阀芯位置信号对节流口开口面积进行缩放，这也可以缩放质量流量。

**蒸汽阀门参数化**

当**建模选项**为`蒸汽工况`时，该模块参数化设计用于对控制蒸汽流量的阀门进行建模。

该模块用于控制每个节流口的方法取决于**开口特性**参数：

- `线性` — 流量能力的度量取决于端口 **S** 处的阀芯位置。当阀芯位移以打开节流口时，流量能力的度量从指定的最小值缩放到指定的最大值。
- `表格` — 该模块将流量能力的度量计算为端口 **S** 处阀芯位置的函数。此函数使用一维查找表。

**节流口参数化**参数决定该模块如何计算每个节流口中的流量：

- `Cv 流量系数` — 流量系数 *C*v 对每个节流口中的流量进行缩放。流量系数衡量流体在一定压差驱动下流动的难易程度。
- `Kv 流量系数` — 流量系数 *K*v，其中 Kv=0.865Cv，对每个节流口中的流量进行缩放。流量系数衡量流体在一定压差驱动下流动的难易程度。
- `节流口面积` — 节流口面积的大小对每个节流口中的流量进行缩放。

### 可视化节流口开口

要可视化阀芯偏移和最大位移，请右键单击该模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示在**阀门配置**设置中选择的节流口。节流口参数化设置坐标轴，坐标轴为以下之一：

- *Kv* 流量系数、*Cv* 流量系数或节流口面积与阀芯位置的关系。
- 在特定压差下查询的体积流量与阀芯位置的关系。
- 在特定压差下查询的参考入口温度和参考入口压力下的质量流量与阀芯位置的关系。

当**阀门配置**参数中的正、中性和负设置具有相同的节流口时，该图将节流口开口显示为常数。

要在更改模块参数后更新数据，请单击图形窗口上的 **Reload Data**。

此图显示了一个阀门配置示例。在**阀门配置**设置中：

- **正阀芯位置打开连接**为`P-A, B-T`
- **中性阀芯位置打开连接**为`P-T`
- **负阀芯位置打开连接**为`P-B, A-T`

在 **P-A 节流口**设置中：

- **最大 P-A 节流口面积处的阀芯位置**为`2.5e-3 m`

所有其他阀芯位置均为默认值。

每个节流口的面积与阀芯位置的关系图。

可视化显示 P-A 节流口在阀芯位置 `-2.53e-3` 和 `2.53e-3` m 之间打开。由于 P-A 节流口仅在阀芯沿正方向位移时打开，将**中性阀芯和位置打开连接的一致性检查**参数设置为`警告`会返回：

`Warning: P-A orifice must be closed when the spool is in the neutral position. Adjust Spool position at maximum P-A orifice area, Neutral spool position open connections, or Consistency check for neutral spool position open connections. Right-click on the block and select Fluids > Plot Valve Characteristics to view the area or flow of each connection versus spool position.`

要解决此警告，可以更改：

- **最大 P-A 节流口面积处的阀芯位置**为大于 0.005 m 的值
- **中性阀芯位置打开连接的一致性检查**为`无`
- 通过将**中性阀芯位置打开连接**设置为`P-A`来更改阀门配置

### 假设和限制

- 阀门与环境之间没有热交换。
- 当**建模选项**为`液体工况`时，结果在过冷液体区域之外可能不准确。当**建模选项**为`蒸汽工况`时，结果在过热蒸汽区域之外可能不准确。要对液-汽混合物中的阀门进行建模，请将**建模选项**设置为`液体工况`。
