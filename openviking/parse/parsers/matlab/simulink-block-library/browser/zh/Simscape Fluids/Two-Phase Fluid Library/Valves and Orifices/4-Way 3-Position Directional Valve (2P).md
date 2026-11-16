---
type: simulink-block
title: '4-Way 3-Position Directional Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid Library / Valves and Orifices'
documentation_page: '4way3positiondirectionalvalve2p'
documentation_source_path: 'ref/4way3positiondirectionalvalve2p.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 3-Position Directional Valve (2P)

## 端口

### 守恒

### **A** — 两相流体入口或出口端口

与阀的入口或出口端口关联的两相流体守恒端口。

### **B** — 两相流体入口或出口端口

与阀的入口或出口端口关联的两相流体守恒端口。

### **P** — 两相流体入口或出口端口

与阀的入口或出口端口关联的两相流体守恒端口。

### **T** — 两相流体入口或出口端口

与阀的入口或出口端口关联的两相流体守恒端口。
### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移关联的物理信号，单位为 m。

## 参数

### **Modeling option** — 用于流体相的建模选项 `Liquid operating condition`（默认） | `Vapor operating condition`

阀门处流体相的建模选项。如果模块位置处的两相流体处于液态，则将此参数设置为 `Liquid operating condition`。如果模块位置处的两相流体处于气态，则将此参数设置为 `Vapor operating condition`。

### 阀配置

### **Positive spool position open connections** — 当阀芯处于正位置时打开的流路 `P-A, B-T`（默认） | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯处于正位置时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置与其他节流孔的设置是否一致，请将 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error`。

### **Neutral spool position open connections** — 当阀芯处于中位时打开的流路 `All closed`（默认） | `P-A, P-B, A-T, B-T` | `A-T, B-T` | `P-A, A-T` | `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-B, B-T` | `A-T` | `B-T` | `P-A` | `P-B` | `P-T` | `P-A, A-T, P-T` | `P-A, P-B, A-B` | `P-B, B-T, P-T` | `P-A, P-B, A-T, B-T, P-T`

当阀芯处于中位时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置与其他节流孔的设置是否一致，请将 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error`。

### **Negative spool position open connections** — 当阀芯沿负方向移动时打开的流路 `P-A, B-T`（默认） | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯沿负方向移动时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置与其他节流孔的设置是否一致，请将 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error`。

### **Consistency check for neutral spool position open connections** — 是否检查节流孔设置是否一致 `Warning`（默认） | `Error` | `None`

是否检查 **阀配置** 部分中的中位阀芯位置打开设置是否与最大节流孔面积处指定的阀芯位置一致。对于每个启用的节流孔，阀芯中位处的实际偏移量应与每个单独节流孔指定的阀芯偏移量相匹配。

### 模型参数化

### **Area characteristics** — 节流孔的流量方程 `Identical for all flow paths`（默认） | `Different for each flow path`

是否为阀门节流孔面积应用统一或单独的流量方程。将此参数设置为 `Identical for all flow paths` 时，模块对所有阀门节流孔使用相同的节流孔和阀芯几何、流量、压力和面积向量。将此参数设置为 `Different for each flow path` 时，可以为每个节流孔单独指定这些参数。对于这两种设置，当您将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流孔 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **Orifice parameterization** — 可变或恒定节流孔参数化 `Linear - Area vs. spool travel`（默认） | `Linear - Nominal mass flow rate vs. spool travel` | `Tabulated data - Area vs. spool travel` | `Cv flow coefficient` | `Kv flow coefficient` | `Orifice area`

模块用于根据节流孔两端的压差计算质量流量，或根据质量流量计算压差的方法。

当 **Modeling option** 为 `Liquid operating condition` 时，此参数的选项为：

- `Linear - Area vs. spool travel`
- `Linear - Nominal mass flow rate vs. spool travel`
- `Tabulated data - Area vs. spool travel`

当 **Modeling option** 为 `Vapor operating condition` 时，此参数的选项为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **Spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认） | 正标量

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，且 **Opening characteristic** 为 `Linear`。

### **Maximum orifice area** — 最大节流孔开度面积 `1e-4 m^2`（默认） | 正标量

阀门运行期间每个节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Orifice parameterization** 为 `Orifice area`，且 **Opening characteristic** 为 `Linear`。

### **Nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` kg/s（默认） | 正标量

节流孔最大开度位置处的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` MPa（默认） | 正标量

节流孔最大开度位置处的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认） | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。模块根据 **Nominal inlet pressure** 和 **Nominal inlet condition specification** 参数的值，从制表流体属性数据中确定节流孔标称入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal inlet pressure** — 入口流体压力 `0.101325` MPa（默认） | 正标量

标称条件下的入口压力。模块根据 **Nominal inlet pressure** 和 **Nominal inlet condition specification** 参数的值，从制表流体属性数据中确定入口比容。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **Nominal inlet temperature** — 流体温度 `293.15` K（默认） | 正标量

标称运行条件下的入口流体温度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并将 **Nominal inlet condition specification** 设置为 `Temperature`。

### **Nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认） | 范围 [0,1] 内的正标量

标称运行条件下入口混合物的质量分数蒸汽干度。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并将 **Nominal inlet condition specification** 设置为 `Vapor quality`。

### **Nominal inlet vapor void fraction** — 入口体积分数 `0`（默认） | 范围 [0,1] 内的正标量

标称运行条件下入口混合物体积分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并将 **Nominal inlet condition specification** 设置为 `Vapor void fraction`。

### **Nominal inlet specific enthalpy** — 入口流体比焓 `400` kJ/kg（默认） | 正标量

标称运行条件下的入口比焓。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并将 **Nominal inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet specific internal energy** — 入口比内能 `400` kJ/kg（默认） | 正标量

标称运行条件下的入口比内能。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并将 **Nominal inlet condition specification** 设置为 `Specific internal energy`。

### **Opening characteristic** — 将控制信号转换为流量能力度量的方法 `Linear`（默认） | `Tabulated`

将端口 **S** 处指定的控制信号转换为所选流量能力度量的方法。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`。

### **Spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

根据制表阀门面积数据对节流孔进行参数化时的阀芯行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，且 **Opening characteristic** 为 `Tabulated`。

### **Orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1×*n* 向量

根据制表阀门面积数据对节流孔进行参数化时的开口面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。按升序列出值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **Modeling option** 为 `Liquid operating condition`，且 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 为 `Vapor operating condition`，**Orifice parameterization** 为 `Orifice area`，且 **Opening characteristic** 为 `Tabulated`。

### **Maximum Cv flow coefficient** — 对应最大开启组件的 *Cv* 系数 `4`（默认） | 正标量

当节流孔完全打开且可用于流动的面积达到最大时，*Cv* 流量系数的值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Cv flow coefficient vector** — 对应成员位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认） | 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **Control member position vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Cv flow coefficient`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **Maximum Kv flow coefficient** — 对应最大开启组件的 *Kv* 系数 `3.6`（默认） | 正标量

当节流孔完全打开且可用于流动的面积达到最大时，*Kv* 流量系数的值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Vapor operating condition`，将 **Area characteristics** 设置为 `Identical for all flow paths`，将 **Orifice parameterization** 设置为 `Kv flow coefficient`，并将 **Opening characteristic** 设置为 `Linear`。

### **Kv flow coefficient vector** — 对应成员位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认） | 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **Control member position vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **Control member position vector** 参数相同。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，将 **面积特性** 设置为 `Identical for all flow paths`，将 **孔口参数化** 设置为 `Kv flow coefficient`，并将 **开启特性** 设置为 `Tabulated`。

### **xT 阻塞流压差比因子** — 压差比 `0.7`（默认值） | 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中首次发生阻塞流。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **流量系数** — 流量系数 `0.64`（默认值） | 正标量

用于考虑理论流动中排放损失的修正因子。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，并将 **孔口参数化** 设置为 `Orifice area`；或者将 **建模选项** 设置为 `Liquid operating condition`，并将 **孔口参数化** 设置为以下任一项：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **泄漏流量分数** — 流量比 `1e-6`（默认值） | 正标量

孔口关闭时与打开时的流量之比。

#### 依赖项

要启用此参数，请设置以下任一项：

- 将 **建模选项** 设置为 `Liquid operating condition`，并将 **孔口参数化** 设置为 `Linear - Area vs. spool travel`。
- 将 **建模选项** 设置为 `Vapor operating condition`，并将 **开启特性** 设置为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01`（默认值） | [0,1] 范围内的正标量

连续平滑因子，根据阀处于接近打开和接近关闭位置时的流量响应引入一层逐步变化。为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **孔口参数化** 设置为 `Linear - area vs. spool travel`；或者将 **建模选项** 设置为 `Vapor operating condition`，并将 **开启特性** 设置为 `Linear`。

### **压力恢复** — 是否考虑面积扩大中的压力升高 `off`（默认值） | `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力升高。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **孔口参数化** 设置为以下任一项：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **层流流动压力比** — 层流-湍流过渡压力比 `0.999`（默认值） | 正标量

孔口出口压力与孔口入口压力之比，在该比值处流体在层流与湍流状态之间过渡。压力损失在层流中与质量流量成线性关系，在湍流中成二次关系。

### **入口相变时间常数** — 混合物比容的时间滞后 `0.1` `s`（默认值） | 正标量

计算流体比容时液-汽混合物的时间滞后。当入口流体为完全过冷液体或完全过热蒸汽时，此参数不影响比容。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`。

### **端口 P、T、A 和 B 处的横截面积** — 守恒端口处的面积 `0.01 m^2`（默认值） | 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀的质量流量的压力-流量方程中使用该面积。

### P-A Orifice

### **最大 P-A 孔口面积处的阀芯位置** — 完全打开 P-A 孔口时的阀芯偏移量 `5e-3 m`（默认值） | 正标量

完全打开 P-A 孔口时相对于中位位置的阀芯偏移量。

#### 依赖项

要启用此参数，请设置以下参数之一。

**正阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**注意：**

仅当 P-A 孔口设置未同时出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **关闭和打开孔口之间的 P-A 阀芯行程** — 最大阀芯行程 `0.005 m`（默认值） | 正标量

最大阀芯行程距离。此值为计算提供上限，使仿真不会返回非物理值。

#### 依赖项

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

并且满足以下任一项：

- 将 **建模选项** 设置为 `Liquid operating condition`，将 **面积特性** 设置为 `Different for each flow path`，并将 **孔口参数化** 设置为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- 将 **建模选项** 设置为 `Vapor operating condition`，将 **面积特性** 设置为 `Different for each flow path`，并将 **开启特性** 设置为 `Linear`。

### **最大孔口开度下的 P-A 标称质量流量** — 额定质量流量 `0.1` `kg/s`（默认值） | 正标量

通过最大开度 P-A 孔口的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. 将 **建模选项** 设置为 `Liquid operating condition`
2. 将 **面积特性** 设置为 `Different for each flow path`
3. 将 **孔口参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **最大孔口开度下的 P-A 标称压降** — 额定压降 `0.001` `MPa`（默认值） | 正标量

通过最大开度 P-A 孔口的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. 将 **建模选项** 设置为 `Liquid operating condition`
2. 将 **面积特性** 设置为 `Different for each flow path`
3. 将 **孔口参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 标称入口条件指定** — 确定入口流体状态的方法 `Temperature`（默认值） | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 P-A 孔口入口流体状态的方法。

#### 依赖项

要启用此参数，请设置：

1. 将 **建模选项** 设置为 `Liquid operating condition`
2. 将 **面积特性** 设置为 `Different for each flow path`
3. 将 **孔口参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中的至少一个：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 标称入口压力** — 入口流体压力 `0.101325` `MPa`（默认值） | 正标量

标称条件下 P-A 孔口的入口压力。

#### 依赖项

要启用此参数，请设置：

1. 将 **建模选项** 设置为 `Liquid operating condition`
2. 将 **面积特性** 设置为 `Different for each flow path`
3. 将 **孔口参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中的至少一个：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 标称入口温度** — 流体温度 `293.15` `K`（默认值） | 正标量

标称运行条件下 P-A 孔口的入口流体温度。

#### 依赖项

要启用此参数，请设置：

1. 将 **建模选项** 设置为 `Liquid operating condition`
2. 将 **面积特性** 设置为 `Different for each flow path`
3. 将 **孔口参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 将 **标称入口条件指定** 设置为 `Temperature`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 标称入口蒸汽干度** — 入口蒸汽干度质量分数 `0`（默认值） | [0,1] 范围内的正标量

标称运行条件下 P-A 孔口入口混合物的质量分数蒸汽干度。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. 将 **建模选项** 设置为 `Liquid operating condition`
2. 将 **面积特性** 设置为 `Different for each flow path`
3. 将 **孔口参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 将 **标称入口条件指定** 设置为 `Vapor quality`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 标称入口蒸汽空隙率** — 入口蒸汽空隙率 `0`（默认值） | [0,1] 范围内的正标量

标称运行条件下 P-A 孔口入口混合物的蒸汽空隙率。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. 将 **建模选项** 设置为 `Liquid operating condition`
2. 将 **面积特性** 设置为 `Different for each flow path`
3. 将 **孔口参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 将 **标称入口条件指定** 设置为 `Vapor void fraction`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 标称入口比焓** — 入口流体比焓 `400` `kJ/kg`（默认值） | 正标量

标称运行条件下 P-A 孔口的入口比焓。

#### 依赖项

要启用此参数，请设置：

1. 将 **建模选项** 设置为 `Liquid operating condition`
2. 将 **面积特性** 设置为 `Different for each flow path`
3. 将 **孔口参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 将 **标称入口条件指定** 设置为 `Specific enthalpy`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 标称入口比内能** — 入口比内能 `400` `kJ/kg`（默认值） | 正标量

标称运行条件下 P-A 孔口的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating
   condition`
2. **面积特性**为
   `Different for each flow
   path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **标称入口条件指定**为 `Specific
   internal energy`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A 恒定孔口标称质量流量** — 标称质量流量 `0.1` `kg/s` (默认) | positive scalar

通过恒定 P-A 孔口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating
   condition`
2. **面积特性**为
   `Different for each flow
   path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中采用以下设置之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 孔口设置出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 恒定孔口标称压降** — 标称压降 `0.001` `MPa` (默认) | positive scalar

通过恒定 P-A 孔口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating
   condition`
2. **面积特性**为
   `Different for each flow
   path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 每个参数中采用以下设置之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 孔口设置出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 恒定孔口 Cv 流量系数** — 流量系数 `4` (默认) | positive scalar

P-A 孔口的恒定 *Cv* 流量系数值。该参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating
   condition`
2. **面积特性**为
   `Different for each flow
   path`
3. **孔口参数化**为
   `Cv flow
   coefficient`
4. 每个参数中采用以下设置之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 孔口设置出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 孔口最大 Cv 流量系数** — 对应于组件最大开启的 *Cv* 系数 `4` (默认) | positive scalar

当 P-A 孔口完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。该参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating
   condition`
2. **面积特性**为
   `Different for each flow
   path`
3. **孔口参数化**为
   `Cv flow
   coefficient`
4. **开启特性**为
   `Linear`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A 孔口 Cv 流量系数向量** — 用于 member position vector 中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` (默认) | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应于 **P-A 孔口阀芯行程向量** 参数中的一个值。该参数衡量蒸气在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-A 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating
   condition`
2. **面积特性**为
   `Different for each flow
   path`
3. **孔口参数化**为
   `Cv flow
   coefficient`
4. **开启特性**为
   `Tabulated`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A 恒定孔口 Kv 流量系数** — 流量系数 `3.6` (默认) | positive scalar

P-A 孔口的恒定 *Kv* 流量系数值。该参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating
   condition`
2. **面积特性**为
   `Different for each flow
   path`
3. **孔口参数化**为
   `Kv flow
   coefficient`
4. 每个参数中采用以下设置之一：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

**注意：**

仅当 P-A 孔口设置出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 孔口最大 Kv 流量系数** — 对应于组件最大开启的 *Kv* 系数 `3.6` (默认) | positive scalar

当 P-A 孔口完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。该参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating
   condition`
2. **面积特性**为
   `Different for each flow
   path`
3. **孔口参数化**为
   `Kv flow
   coefficient`
4. **开启特性**为
   `Linear`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A 孔口 Kv 流量系数向量** — 用于 member position vector 中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` (默认) | 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应于 **P-A 孔口阀芯行程向量** 参数中的一个值。该参数衡量蒸气在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-A 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating
   condition`
2. **面积特性**为
   `Different for each flow
   path`
3. **孔口参数化**为
   `Kv flow
   coefficient`
4. **开启特性**为
   `Tabulated`
5. 以下参数中至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### **P-A 孔口阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m` (默认) | 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将以下参数之一设置为：

**正阀芯位置开启连接**为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接**为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T,
  P-T`

**负阀芯位置开启连接**为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **建模选项**为
  `Liquid operating condition`，
  **面积特性**为
  `Different for each flow path`，
  且 **孔口参数化**为
  `Tabulated data - Area vs. spool
  travel`。
- **建模选项**为 `Vapor
  operating condition`，**面积特性**
  为 `Different for
  each flow path`，且 **开启特性**
  为
  `Tabulated`。

### **P-A 最大孔口面积** — 最大孔口开启面积 `1e-4 m^2` (默认) | positive scalar

阀运行期间 P-A 孔口的最大开启面积。

#### 依赖关系

要启用此参数，请将以下参数之一设置为：

**正阀芯位置开启连接**为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接**为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T,
  P-T`

**负阀芯位置开启连接**为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

还要将 **面积特性** 设置为
`Different for each flow path`，并且满足以下任一条件：

- **建模选项**为
  `Liquid operating condition`
  且 **孔口参数化**为
  `Linear - Area vs. spool
  travel`。
- **建模选项**为 `Vapor
  operating condition`，**孔口参数化**
  为 `Orifice
  area`，且 **开启特性**
  为
  `Linear`。

### **P-A 孔口面积向量** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (默认) | 1-by-*n* vector

用于阀面积表格参数化的开启面积向量。向量元素必须与 **P-A 孔口阀芯行程向量** 参数中的元素一一对应。这些元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请将以下参数之一设置为：

**正阀芯位置开启连接**为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接**为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T,
  P-T`

**负阀芯位置开启连接**为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

还要将 **面积特性** 设置为
`Different for each flow path`，并且满足以下任一条件：

- **建模选项**为
  `Liquid operating condition`
  且 **孔口参数化**为
  `Tabulated data - Area vs. spool
  travel`。
- **建模选项**为 `Vapor
  operating condition`，**孔口参数化**
  为 `Orifice
  area`，且 **开启特性**
  为
  `Tabulated`。

### **P-A 恒定孔口面积** — 恒定孔口的横截面积 `1e-4 m^2` (默认) | positive scalar

当正和负阀芯位置包含相同孔口时的孔口面积。

#### 依赖项

要启用此参数，请在以下每个参数中设置以下设置之一：

**正阀芯位置开启连接** 为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接** 为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **建模选项** 为 `Liquid operating condition`，**面积特性** 为 `Different for each flow path`，并且 **节流口参数化** 为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- **建模选项** 为 `Vapor operating condition`，**面积特性** 为 `Different for each flow path`，并且 **开启特性** 为 `Tabulated`。

**注意：**

仅当 P-A 节流口设置出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-A 节流口阻塞流时的 xT 压差比因子** — 压差之比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-A 节流口首次发生阻塞。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Vapor operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Kv flow coefficient` 或 `Cv flow coefficient`
4. 以下参数中的至少一个：

   **正阀芯位置开启连接** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### P-B 节流口

### **P-B 节流口面积最大时的阀芯位置** — 完全打开 P-B 节流口时的阀芯偏移 `5e-3 m`（默认）| 正标量

完全打开的 P-B 节流口相对于中位位置的阀芯偏移。

#### 依赖项

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**注意：**

仅当 P-B 节流口设置未同时出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **P-B 节流口从关闭到打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以使仿真不会返回非物理值。

#### 依赖项

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**负阀芯位置开启连接** 为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **建模选项** 为 `Liquid operating condition`，**面积特性** 为 `Different for each flow path`，并且 **节流口参数化** 为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **建模选项** 为 `Vapor operating condition`，**面积特性** 为 `Different for each flow path`，并且 **开启特性** 为 `Linear`。

### **最大节流口开度下的 P-B 标称质量流量** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大开度 P-B 节流口的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **最大节流口开度下的 P-B 标称压降** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大开度 P-B 节流口的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B 标称入口条件指定** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 P-B 节流口入口流体状态的方法。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中的至少一个：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B 标称入口压力** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

标称条件下 P-B 节流口的入口压力。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中的至少一个：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B 标称入口温度** — 流体温度 `293.15` `K`（默认）| 正标量

标称运行条件下 P-B 节流口的入口流体温度。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定** 为 `Temperature`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B 标称入口蒸汽干度** — 入口蒸汽干度质量分数 `0`（默认）| 范围 [0,1] 内的正标量

标称运行条件下 P-B 节流口入口混合物的蒸汽干度（按质量分数）。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定** 为 `Vapor quality`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B 标称入口蒸汽空隙率** — 入口蒸汽空隙率 `0`（默认）| 范围 [0,1] 内的正标量

标称运行条件下 P-B 节流口入口混合物的蒸汽空隙率。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定** 为 `Vapor void fraction`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B 标称入口比焓** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

标称运行条件下 P-B 节流口的入口比焓。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定** 为 `Specific enthalpy`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B 标称入口比内能** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

标称运行条件下 P-B 节流口的入口比内能。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定** 为 `Specific internal energy`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B 恒定节流口标称质量流量** — 标称质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 P-B 节流口的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 在以下每个参数中设置以下某一项：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-B 节流口设置出现在以下全部三个阀芯位置参数中时，才会启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B constant orifice nominal pressure drop** — 公称压降 `0.001` `MPa`（默认）| positive scalar

通过恒定 P-B 节流口的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 在以下每个参数中设置以下某一项：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-B 节流口设置出现在以下全部三个阀芯位置参数中时，才会启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| positive scalar

P-B 节流口的恒定 *Cv* 流量系数值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Cv flow coefficient`
4. 在以下每个参数中设置以下某一项：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-B 节流口设置出现在以下全部三个阀芯位置参数中时，才会启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum Cv flow coefficient** — 对应最大开度组件的 *Cv* 系数 `4`（默认）| positive scalar

当 P-B 节流口完全打开且可用于流动的面积达到最大时的 *Cv* 流量系数值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Cv flow coefficient`
4. **Opening characteristic** 设置为 `Linear`
5. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice Cv flow coefficient vector** — 对应构件位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` 中值的 *Cv* 系数（默认）| 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应于 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Cv flow coefficient`
4. **Opening characteristic** 设置为 `Tabulated`
5. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| positive scalar

P-B 节流口的恒定 *Kv* 流量系数值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient`
4. 在以下每个参数中设置以下某一项：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

**注意：**

仅当 P-B 节流口设置出现在以下全部三个阀芯位置参数中时，才会启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice maximum Kv flow coefficient** — 对应最大开度组件的 *Kv* 系数 `3.6`（默认）| positive scalar

当 P-B 节流口完全打开且可用于流动的面积达到最大时的 *Kv* 流量系数值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient`
4. **Opening characteristic** 设置为 `Linear`
5. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice Kv flow coefficient vector** — 对应构件位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` 中值的 *Kv* 系数（默认）| 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应于 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient`
4. **Opening characteristic** 设置为 `Tabulated`
5. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表数据点之间使用线性插值。

#### 依赖项

要启用此参数，请将以下参数之一设置为：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Different for each flow path`，并且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Different for each flow path`，并且 **Opening characteristic** 设置为 `Tabulated`。

### **P-B maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| positive scalar

阀运行期间 P-B 节流口的最大开口面积。

#### 依赖项

要启用此参数，请将以下参数之一设置为：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

还要将 **Area characteristics** 设置为 `Different for each flow path`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，并且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，并且 **Opening characteristic** 设置为 `Linear`。

### **P-B orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀面积表格化参数化的开口面积向量。向量元素必须与 **P-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0，并按升序列出。

#### 依赖项

要启用此参数，请将以下参数之一设置为：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

还要将 **Area characteristics** 设置为 `Different for each flow path`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，并且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，并且 **Opening characteristic** 设置为 `Tabulated`。

### **P-B constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| positive scalar

当正阀芯位置和负阀芯位置包含同一节流口时的节流口面积。

#### 依赖项

要启用此参数，请在以下每个参数中设置以下某一项：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Different for each flow path`，并且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Different for each flow path`，并且 **Opening characteristic** 设置为 `Tabulated`。

**注意：**

仅当 P-B 节流口设置出现在以下全部三个阀芯位置参数中时，才会启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-B 节流口首次发生阻塞流。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Kv flow coefficient` 或
   `Cv flow coefficient`
4. 以下参数中的至少一个：

   **正阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### A-B 孔口

### **最大 A-B 孔口面积处的阀芯位置** — 完全打开 A-B 孔口时的阀芯偏移 `5e-3 m`（默认）| 正标量

从中位到完全打开 A-B 孔口时的阀芯偏移。

#### 依赖项

要启用此参数，请设置以下参数之一。

**正阀芯位置开启连接**为：

- `P-A, P-B, A-B`

**中位阀芯位置开启连接**为：

- `P-A, P-B, A-B`

**负阀芯位置开启连接**为：

- `P-A, P-B, A-B`

**注意：**

仅当 A-B 孔口设置未同时出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **A-B 孔口关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值提供计算的上限，以便仿真不会返回非物理值。

#### 依赖项

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接**为：

- `P-A, P-B, A-B`

**中位阀芯位置开启连接**为：

- `P-A, P-B, A-B`

**负阀芯位置开启连接**为：

- `P-A, P-B, A-B`

并且满足以下任一项：

- **建模选项**为
  `Liquid operating condition`，
  **面积特性**为
  `Different for each flow path`，
  且 **孔口参数化**为
  `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **建模选项**为 `Vapor operating condition`，**面积特性**为 `Different for each flow path`，且 **开启特性**为
  `Linear`。

### **最大孔口开度下的 A-B 标称质量流量** — 额定质量流量 `0.1` `kg/s`（默认）| 正标量

通过最大打开 A-B 孔口的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **最大孔口开度下的 A-B 标称压降** — 额定压降 `0.001` `MPa`（默认）| 正标量

通过最大打开 A-B 孔口的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 标称入口条件指定** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 A-B 孔口入口流体状态的方法。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中的至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 标称入口压力** — 入口流体压力 `0.101325` `MPa`（默认）| 正标量

A-B 孔口在标称条件下的入口压力。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中的至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 标称入口温度** — 流体温度 `293.15` `K`（默认）| 正标量

A-B 孔口在标称操作条件下的入口流体温度。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定**为
   `Temperature`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 标称入口蒸汽干度** — 入口蒸汽干度质量分数 `0`（默认）| [0,1] 范围内的正标量

按质量分数计，A-B 孔口在标称操作条件下的入口混合物蒸汽干度。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定**为 `Vapor quality`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 标称入口蒸汽空泡率** — 入口蒸汽空泡率 `0`（默认）| [0,1] 范围内的正标量

A-B 孔口在标称操作条件下的入口混合物蒸汽空泡率。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定**为 `Vapor void fraction`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 标称入口比焓** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

A-B 孔口在标称操作条件下的入口比焓。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定**为 `Specific enthalpy`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 标称入口比内能** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

A-B 孔口在标称操作条件下的入口比内能。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定**为 `Specific internal energy`
5. 以下参数中的至少一个：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 恒定孔口标称质量流量** — 标称质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 A-B 孔口的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 孔口设置出现在以下全部三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **A-B 恒定孔口标称压降** — 标称压降 `0.001` `MPa`（默认）| 正标量

通过恒定 A-B 孔口的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Liquid operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 孔口设置出现在以下全部三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **A-B 恒定孔口 Cv 流量系数** — 流量系数 `4`（默认）| 正标量

A-B 孔口的恒定 *Cv* 流量系数的值。此参数度量当由压差驱动时，蒸汽穿过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Cv flow coefficient`
4. 每个参数中的以下设置之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

**注意：**

仅当 A-B 孔口设置出现在以下全部三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **A-B 孔口最大 Cv 流量系数** — 对应最大打开组件的 *Cv* 系数 `4`（默认）| 正标量

当 A-B 孔口完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数度量当由压差驱动时，蒸汽穿过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Cv flow coefficient`
4. **开启特性**为
   `Linear`
5. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 孔口 Cv 流量系数向量** — 用于 member position vector 中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1-by-*n* 向量

*Cv* 流量系数向量。每个系数对应于 **A-B 孔口阀芯行程向量**参数中的一个值。此参数度量当由压差驱动时，蒸汽穿过阻力元件的难易程度。向量的大小必须与 **A-B 孔口阀芯行程向量**参数相同。

#### 依赖项

要启用此参数，请设置：

1. **建模选项**为
   `Vapor operating condition`
2. **面积特性**为
   `Different for each flow path`
3. **孔口参数化**为
   `Cv flow coefficient`
4. **开启特性**为
   `Tabulated`
5. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-B`

### **A-B 恒定孔口 Kv 流量系数** — 流量系数 `3.6`（默认）| 正标量

A-B 孔口的恒定 *Kv* 流量系数的值。此参数度量当由压差驱动时，蒸汽穿过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
   path`
3. **Orifice parameterization** 为
   `Kv flow
   coefficient`
4. 每个参数中的以下某一设置：

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

仅当 A-B 节流孔设置出现在全部三个阀芯位置参数中时，才会启用此参数：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-B orifice maximum Kv flow coefficient** — 与最大开度组件对应的 *Kv* 系数 `3.6`（默认值）| 正标量

当 A-B 节流孔完全打开且可用于流动的面积为最大时，*Kv* 流量系数的值。此参数衡量蒸气在压差驱动下通过阻力元件的容易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
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

### **A-B orifice Kv flow coefficient vector** — 成员位置向量中值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认值）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应于 **A-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸气在压差驱动下通过阻力元件的容易程度。向量的大小必须与 **A-B orifice spool travel
vector** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
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

### **A-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认值）| 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖项

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
  `Different for each flow path`，
  且 **Orifice parameterization** 为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 为 `Vapor
  operating condition`，**Area
  characteristics** 为 `Different for
  each flow path`，且 **Opening
  characteristic** 为
  `Tabulated`。

### **A-B maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认值）| 正标量

阀操作期间 A-B 节流孔的最大开口面积。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-B`

还要将 **Area characteristics** 设置为
`Different for each flow path`，并且满足以下任一条件：

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

### **A-B orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认值）| 1×*n* 向量

用于阀面积表格化参数化的开口面积向量。向量元素必须与 **A-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 且按升序列出。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-A, P-B, A-B`

**Neutral spool position open
connections** 为：

- `P-A, P-B, A-B`

**Negative spool position open
connections** 为：

- `P-A, P-B, A-B`

还要将 **Area characteristics** 设置为
`Different for each flow path`，并且满足以下任一条件：

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

### **A-B constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2`（默认值）| 正标量

当正阀芯位置和负阀芯位置包含同一节流孔时的节流孔面积。

#### 依赖项

要启用此参数，请在每个参数中设置以下某一设置：

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
  `Different for each flow path`，
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

仅当 A-B 节流孔设置出现在全部三个阀芯位置参数中时，才会启用此参数：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-B orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认值）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的压差比，定义为 (pin−pout)/pin，此时 A-B 节流孔首次发生阻塞。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
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

### A-T 节流孔

### **Spool position at maximum A-T orifice area** — 完全打开 A-T 节流孔时的阀芯偏移 `5e-3 m`（默认值）| 正标量

完全打开 A-T 节流孔时，阀芯相对于中位位置的偏移。

#### 依赖项

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

仅当 A-T 节流孔设置未出现在全部三个阀芯位置参数中时，才会启用此参数：**Positive spool position open
connections**、**Neutral spool position
open connections** 和 **Negative spool position open connections**。

### **A-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认值）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以便仿真不会返回非物理值。

#### 依赖项

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
  `Different for each flow path`，
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

### **A-T nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认值）| 正标量

通过最大开度 A-T 节流孔的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
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

### **A-T nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认值）| 正标量

通过最大开度 A-T 节流孔的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
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

### **A-T nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认值）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 A-T 节流孔入口流体状态的方法。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
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

### **A-T nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认值）| 正标量

标称条件下 A-T 节流孔的入口压力。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
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

### **A-T nominal inlet temperature** — 流体温度 `293.15` `K`（默认值）| 正标量

标称操作条件下 A-T 节流孔的入口流体温度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
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

### **A-T nominal inlet vapor quality** — 入口蒸气干度质量分数 `0`（默认值）| 范围 [0,1] 内的正标量

标称操作条件下 A-T 节流孔入口混合物的蒸气干度（质量分数）。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸气。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 为
   `Liquid operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
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

### **A-T nominal inlet vapor void fraction** — 入口蒸气空泡份额 `0`（默认值）| 范围 [0,1] 内的正标量

标称操作条件下 A-T 节流孔入口混合物的蒸气空泡份额。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸气。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定** 为 `Vapor void fraction`
5. 以下参数中至少一个：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

### **A-T 标称入口比焓** — 入口流体比焓 `400` `kJ/kg`（默认）| positive scalar

A-T 孔口在标称工况下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定** 为 `Specific enthalpy`
5. 以下参数中至少一个：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

### **A-T 标称入口比内能** — 入口比内能 `400` `kJ/kg`（默认）| positive scalar

A-T 孔口在标称工况下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **标称入口条件指定** 为 `Specific internal energy`
5. 以下参数中至少一个：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

### **A-T 恒定孔口标称质量流量** — 标称质量流量 `0.1` `kg/s`（默认）| positive scalar

通过恒定 A-T 孔口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 恒定孔口标称压降** — 标称压降 `0.001` `MPa`（默认）| positive scalar

通过恒定 A-T 孔口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 恒定孔口 Cv 流量系数** — 流量系数 `4`（默认）| positive scalar

A-T 孔口的恒定 *Cv* 流量系数值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Vapor operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Cv flow coefficient`
4. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 孔口最大 Cv 流量系数** — 对应于组件最大开启状态的 *Cv* 系数 `4`（默认）| positive scalar

A-T 孔口完全开启且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Vapor operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Cv flow coefficient`
4. **开启特性** 为 `Linear`
5. 以下参数之一：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

### **A-T 孔口 Cv 流量系数向量** — 用于构件位置向量中值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1-by-*n* vector

由 *Cv* 流量系数组成的向量。每个系数对应于 **A-T 孔口阀芯行程向量** 参数中的一个值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **A-T 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Vapor operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Cv flow coefficient`
4. **开启特性** 为 `Tabulated`
5. 以下参数之一：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

### **A-T 恒定孔口 Kv 流量系数** — 流量系数 `3.6`（默认）| positive scalar

A-T 孔口的恒定 *Kv* 流量系数值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Vapor operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Kv flow coefficient`
4. 每个参数中的以下设置之一：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

**注意：**

仅当 A-T 孔口设置出现在所有三个阀芯位置参数中时，才会启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 孔口最大 Kv 流量系数** — 对应于组件最大开启状态的 *Kv* 系数 `3.6`（默认）| positive scalar

A-T 孔口完全开启且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Vapor operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Kv flow coefficient`
4. **开启特性** 为 `Linear`
5. 以下参数之一：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

### **A-T 孔口 Kv 流量系数向量** — 用于构件位置向量中值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1-by-*n* vector

由 *Kv* 流量系数组成的向量。每个系数对应于 **A-T 孔口阀芯行程向量** 参数中的一个值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **A-T 孔口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为 `Vapor operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **孔口参数化** 为 `Kv flow coefficient`
4. **开启特性** 为 `Tabulated`
5. 以下参数之一：

   - **正阀芯位置开启连接** 为 `P-B, A-T`。
   - **中位阀芯位置开启连接** 为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **负阀芯位置开启连接** 为 `P-B, A-T`。

### **A-T 孔口阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀门面积表格参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接** 为 `P-B, A-T`。
- **中位阀芯位置开启连接** 为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **负阀芯位置开启连接** 为 `P-B, A-T`。

并且满足以下任一条件：

- **建模选项** 为 `Liquid operating condition`，**面积特性** 为 `Different for each flow path`，并且 **孔口参数化** 为 `Tabulated data - Area vs. spool travel`。
- **建模选项** 为 `Vapor operating condition`，**面积特性** 为 `Different for each flow path`，并且 **开启特性** 为 `Tabulated`。

### **A-T 最大孔口面积** — 最大孔口开启面积 `1e-4 m^2`（默认）| positive scalar

阀门运行期间 A-T 孔口的最大开启面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接** 为 `P-B, A-T`。
- **中位阀芯位置开启连接** 为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **负阀芯位置开启连接** 为 `P-B, A-T`。

同时将 **面积特性** 设置为 `Different for each flow path`，并满足以下任一条件：

- **建模选项** 为 `Liquid operating condition`，并且 **孔口参数化** 为 `Linear - Area vs. spool travel`。
- **建模选项** 为 `Vapor operating condition`，**孔口参数化** 为 `Orifice area`，并且 **开启特性** 为 `Linear`。

### **A-T 孔口面积向量** — 阀门开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀门面积表格参数化的开启面积向量。向量元素必须与 **A-T 孔口阀芯行程向量** 参数中的元素一一对应。这些元素必须大于 0，并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接** 为 `P-B, A-T`。
- **中位阀芯位置开启连接** 为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **负阀芯位置开启连接** 为 `P-B, A-T`。

同时将 **面积特性** 设置为 `Different for each flow path`，并满足以下任一条件：

- **建模选项** 为 `Liquid operating condition`，并且 **孔口参数化** 为 `Tabulated data - Area vs. spool travel`。
- **建模选项** 为 `Vapor operating condition`，**孔口参数化** 为 `Orifice area`，并且 **开启特性** 为 `Tabulated`。

### **A-T 恒定孔口面积** — 恒定孔口的横截面积 `1e-4 m^2`（默认）| positive scalar

当正阀芯位置和负阀芯位置包含同一孔口时的孔口面积。

#### 依赖项

要启用此参数，请在每个参数中设置以下之一：

- **Positive spool position open connections** 设为 `P-B, A-T`。
- **Neutral spool position open connections** 设为：

  - `P-A, P-B, A-T, B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
  - `P-A, A-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设为 `P-B, A-T`。

并且满足以下任一条件：

- **Modeling option** 设为 `Liquid operating condition`，**Area characteristics** 设为 `Different for each flow path`，并且 **Orifice parameterization** 设为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- **Modeling option** 设为 `Vapor operating condition`，**Area characteristics** 设为 `Different for each flow path`，并且 **Opening characteristic** 设为 `Tabulated`。

**注意：**

仅当 A-T 节流孔设置出现在所有三个阀芯位置参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections** 中时，此参数才启用。

### **A-T orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 A-T 节流孔首次发生阻塞流。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Vapor operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Kv flow coefficient` 或 `Cv flow coefficient`
4. 以下参数中至少一个：

   - **Positive spool position open connections** 设为 `P-B, A-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `P-B, A-T`
     - `A-T, B-T`
     - `P-A, A-T`
     - `A-T`
     - `P-A, A-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-B, A-T`。

### B-T 节流孔

### **Spool position at maximum B-T orifice area** — 完全打开 B-T 节流孔时的阀芯偏移 `5e-3 m`（默认）| positive scalar

完全打开 B-T 节流孔时偏离中位位置的阀芯偏移。

#### 依赖项

要启用此参数，请设置以下参数之一。

- **Positive spool position open connections** 设为 `P-A, B-T`。
- **Neutral spool position open connections** 设为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置未出现在所有三个阀芯位置参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections** 中时，此参数才启用。

### **B-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| positive scalar

阀芯行程的最大距离。此值为计算提供上限，使仿真不会返回非物理值。

#### 依赖项

要启用此参数，请设置以下参数之一：

- **Positive spool position open connections** 设为 `P-A, B-T`。
- **Neutral spool position open connections** 设为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
  - `P-B, B-T, P-T`
  - `P-A, P-B, A-T, B-T, P-T`
- **Negative spool position open connections** 设为 `P-A, B-T`。

并且满足以下任一条件：

- **Modeling option** 设为 `Liquid operating condition`，**Area characteristics** 设为 `Different for each flow path`，并且 **Orifice parameterization** 设为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **Modeling option** 设为 `Vapor operating condition`，**Area characteristics** 设为 `Different for each flow path`，并且 **Opening characteristic** 设为 `Linear`。

### **B-T nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| positive scalar

通过最大打开 B-T 节流孔的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

### **B-T nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| positive scalar

通过最大打开 B-T 节流孔的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

### **B-T nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 B-T 节流孔入口流体状态的方法。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

### **B-T nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| positive scalar

标称条件下 B-T 节流孔的入口压力。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

### **B-T nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| positive scalar

标称工况下 B-T 节流孔的入口流体温度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设为 `Temperature`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

### **B-T nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| positive scalar in the range [0,1]

标称工况下 B-T 节流孔入口混合物的质量分数蒸汽干度。`0` 值表示入口流体为过冷液体。`1` 值表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设为 `Vapor quality`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

### **B-T nominal inlet vapor void fraction** — 入口蒸汽空隙率 `0`（默认）| positive scalar in the range [0,1]

标称工况下 B-T 节流孔入口混合物的蒸汽空隙率。`0` 值表示入口流体为过冷液体。`1` 值表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设为 `Vapor void fraction`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

### **B-T nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| positive scalar

标称工况下 B-T 节流孔的入口比焓。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设为 `Specific enthalpy`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

### **B-T nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| positive scalar

标称工况下 B-T 节流孔的入口比内能。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设为 `Specific internal energy`
5. 以下参数中至少一个：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

### **B-T constant orifice nominal mass flow rate** — 标称质量流量 `0.1` `kg/s`（默认）| positive scalar

通过恒定 B-T 节流孔的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. 在每个参数中设置以下之一：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置出现在所有三个阀芯位置参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections** 中时，此参数才启用。

### **B-T constant orifice nominal pressure drop** — 标称压降 `0.001` `MPa`（默认）| positive scalar

通过恒定 B-T 节流孔的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设为 `Liquid operating condition`
2. **Area characteristics** 设为 `Different for each flow path`
3. **Orifice parameterization** 设为 `Linear - Nominal mass flow rate vs. spool travel`
4. 在每个参数中设置以下之一：

   - **Positive spool position open connections** 设为 `P-A, B-T`。
   - **Neutral spool position open connections** 设为：

     - `P-A, P-B, A-T, B-T`
     - `A-T, B-T`
     - `P-A, B-T`
     - `P-B, B-T`
     - `B-T`
     - `P-B, B-T, P-T`
     - `P-A, P-B, A-T, B-T, P-T`
   - **Negative spool position open connections** 设为 `P-A, B-T`。

**注意：**

仅当 B-T 节流孔设置出现在所有三个阀芯位置参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections** 中时，此参数才启用。

### **B-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| positive scalar

B-T 节流孔的恒定 *Cv* 流量系数值。此参数衡量在压差驱动下蒸汽通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Vapor operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Cv flow
   coefficient`
4. 在每个参数中进行以下设置之一：

   - **正阀芯位置打开连接** 为 `P-A,
     B-T`。
   - **中位阀芯位置打开连接** 为：

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
   - **负阀芯位置打开连接** 为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在所有三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中位阀芯位置打开连接** 和 **负阀芯位置打开连接**。

### **B-T 节流口最大 Cv 流量系数** — 对应最大打开组件 `4` 的 *Cv* 系数（默认）| positive scalar

当 B-T 节流口完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Vapor operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Cv flow
   coefficient`
4. **开启特性** 设置为
   `Linear`
5. 以下参数之一：

   - **正阀芯位置打开连接** 为 `P-A,
     B-T`。
   - **中位阀芯位置打开连接** 为：

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
   - **负阀芯位置打开连接** 为 `P-A,
     B-T`。

### **B-T 节流口 Cv 流量系数向量** — 成员位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` 中的值对应的 *Cv* 系数（默认）| 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应 **B-T 节流口阀芯行程向量** 参数中的一个值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **B-T 节流口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Vapor operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Cv flow
   coefficient`
4. **开启特性** 设置为
   `Tabulated`
5. 以下参数之一：

   - **正阀芯位置打开连接** 为 `P-A,
     B-T`。
   - **中位阀芯位置打开连接** 为：

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
   - **负阀芯位置打开连接** 为 `P-A,
     B-T`。

### **B-T 常数节流口 Kv 流量系数** — 流量系数 `3.6`（默认）| positive scalar

B-T 节流口的常数 *Kv* 流量系数值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Vapor operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Kv flow
   coefficient`
4. 在每个参数中进行以下设置之一：

   - **正阀芯位置打开连接** 为 `P-A,
     B-T`。
   - **中位阀芯位置打开连接** 为：

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
   - **负阀芯位置打开连接** 为 `P-A,
     B-T`。

**注意：**

仅当 B-T 节流口设置出现在所有三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中位阀芯位置打开连接** 和 **负阀芯位置打开连接**。

### **B-T 节流口最大 Kv 流量系数** — 对应最大打开组件 `3.6` 的 *Kv* 系数（默认）| positive scalar

当 B-T 节流口完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Vapor operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Kv flow
   coefficient`
4. **开启特性** 设置为
   `Linear`
5. 以下参数之一：

   - **正阀芯位置打开连接** 为 `P-A,
     B-T`。
   - **中位阀芯位置打开连接** 为：

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
   - **负阀芯位置打开连接** 为 `P-A,
     B-T`。

### **B-T 节流口 Kv 流量系数向量** — 成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` 中的值对应的 *Kv* 系数（默认）| 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应 **B-T 节流口阀芯行程向量** 参数中的一个值。此参数衡量蒸气在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **B-T 节流口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Vapor operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Kv flow
   coefficient`
4. **开启特性** 设置为
   `Tabulated`
5. 以下参数之一：

   - **正阀芯位置打开连接** 为 `P-A,
     B-T`。
   - **中位阀芯位置打开连接** 为：

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
   - **负阀芯位置打开连接** 为 `P-A,
     B-T`。

### **B-T 节流口阀芯行程向量** — 相对于完全关闭位置的阀芯打开距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。按升序列出值。第一个元素必须为 0。模块在表数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置打开连接** 为 `P-A,
  B-T`。
- **中位阀芯位置打开连接** 为：

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
- **负阀芯位置打开连接** 为 `P-A,
  B-T`。

并且满足以下任一情况：

- **建模选项** 为
  `Liquid operating condition`，
  **面积特性** 为
  `Different for each flow path`，
  并且 **节流口参数化** 为
  `Tabulated data - Area vs. spool
  travel`。
- **建模选项** 为 `Vapor
  operating condition`，**面积
  特性** 为 `Different for
  each flow path`，并且 **开启
  特性** 为
  `Tabulated`。

### **B-T 最大节流口面积** — 最大节流口打开面积 `1e-4 m^2`（默认）| positive scalar

阀操作期间 B-T 节流口最大的打开面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置打开连接** 为 `P-A,
  B-T`。
- **中位阀芯位置打开连接** 为：

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
- **负阀芯位置打开连接** 为 `P-A,
  B-T`。

还需将 **面积特性** 设置为
`Different for each flow path`，并且满足以下任一情况：

- **建模选项** 为
  `Liquid operating condition`
  并且 **节流口参数化** 为
  `Linear - Area vs. spool
  travel`。
- **建模选项** 为 `Vapor
  operating condition`，**节流口
  参数化** 为 `Orifice
  area`，并且 **开启
  特性** 为
  `Linear`。

### **B-T 节流口面积向量** — 阀打开面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀面积表格参数化的打开面积向量。向量元素必须与 **B-T 节流口阀芯行程向量** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置打开连接** 为 `P-A,
  B-T`。
- **中位阀芯位置打开连接** 为：

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
- **负阀芯位置打开连接** 为 `P-A,
  B-T`。

还需将 **面积特性** 设置为
`Different for each flow path`，并且满足以下任一情况：

- **建模选项** 为
  `Liquid operating condition`
  并且 **节流口参数化** 为
  `Tabulated data - Area vs. spool
  travel`。
- **建模选项** 为 `Vapor
  operating condition`，**节流口
  参数化** 为 `Orifice
  area`，并且 **开启
  特性** 为
  `Tabulated`。

### **B-T 常数节流口面积** — 常数节流口的横截面积 `1e-4 m^2`（默认）| positive scalar

正阀芯位置和负阀芯位置包含同一节流口时的节流口面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下设置之一：

- **正阀芯位置打开连接** 为 `P-A,
  B-T`。
- **中位阀芯位置打开连接** 为：

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
- **负阀芯位置打开连接** 为 `P-A,
  B-T`。

并且满足以下任一情况：

- **建模选项** 为
  `Liquid operating condition`，
  **面积特性** 为
  `Different for each flow path`，
  并且 **节流口参数化** 为
  `Tabulated data - Area vs. spool
  travel` 或 `Linear - Area vs.
  spool travel`。
- **建模选项** 为 `Vapor
  operating condition`，**面积
  特性** 为 `Different for
  each flow path`，并且 **开启
  特性** 为
  `Tabulated`。

**注意：**

仅当 B-T 节流口设置出现在所有三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中位阀芯位置打开连接** 和 **负阀芯位置打开连接**。

### **B-T 节流口阻塞流下的 xT 压差比因子** — 压差比 `0.7`（默认）| positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 B-T 节流口首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Vapor operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
4. 以下参数中的至少一个：

   - **正阀芯位置打开连接** 为 `P-A,
     B-T`。
   - **中位阀芯位置打开连接** 为：

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
   - **负阀芯位置打开连接** 为 `P-A,
     B-T`。

### P-T 节流口

### **最大 P-T 节流口面积时的阀芯位置** — 完全打开 P-T 节流口的阀芯偏移 `5e-3 m`（默认）| positive scalar

完全打开 P-T 节流口时，阀芯相对于中位位置的偏移。

#### 依赖关系

要启用此参数，请将 **中位阀芯位置打开连接** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

### **P-T 节流口关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| positive scalar

阀芯行程的最大距离。此值提供计算的上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **中位阀芯位置打开连接** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

并且满足以下任一情况：

- **建模选项** 为
  `Liquid operating condition`，
  **面积特性** 为
  `Different for each flow path`，
  并且 **节流口参数化** 为
  `Linear - Area vs. spool
  travel` 或 `Linear - Nominal
  mass flow rate vs. spool travel`。
- **建模选项** 为 `Vapor
  operating condition`，**面积
  特性** 为 `Different for
  each flow path`，并且 **开启
  特性** 为
  `Linear`。

### **最大节流口开度时的 P-T 额定质量流量** — 额定质量流量 `0.1` `kg/s`（默认）| positive scalar

通过最大打开 P-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Liquid operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **最大节流口开度时的 P-T 额定压降** — 额定压降 `0.001` `MPa`（默认）| positive scalar

通过最大打开 P-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Liquid operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 额定入口条件指定** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 P-T 节流口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 设置为
   `Liquid operating
   condition`
2. **面积特性** 设置为
   `Different for each flow
   path`
3. **节流口参数化** 设置为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **中位阀芯位置打开连接** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 额定入口压力** — 入口流体压力 `0.101325` `MPa`（默认）| positive scalar

额定条件下 P-T 节流口的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Liquid operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| 正标量

P-T 节流孔在额定运行条件下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Liquid operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition specification** 设置为
   `Temperature`
5. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| 范围 [0,1] 内的正标量

P-T 节流孔在额定运行条件下入口混合物的蒸汽质量分数干度。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Liquid operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition specification** 设置为 `Vapor
   quality`
5. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet vapor void fraction** — 入口蒸汽空泡份额 `0`（默认）| 范围 [0,1] 内的正标量

P-T 节流孔在额定运行条件下入口混合物的蒸汽空泡份额。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Liquid operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition specification** 设置为 `Vapor void
   fraction`
5. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

P-T 节流孔在额定运行条件下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Liquid operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition specification** 设置为 `Specific
   enthalpy`
5. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

P-T 节流孔在额定运行条件下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Liquid operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **Nominal inlet condition specification** 设置为 `Specific
   internal energy`
5. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice maximum Cv flow coefficient** — 对应最大开度组件的 *Cv* 系数 `4`（默认）| 正标量

当 P-T 节流孔完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Vapor operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Cv flow
   coefficient`
4. **Opening characteristic** 设置为
   `Linear`
5. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice Cv flow coefficient vector** — 成员位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **P-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Vapor operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Cv flow
   coefficient`
4. **Opening characteristic** 设置为
   `Tabulated`
5. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice maximum Kv flow coefficient** — 对应最大开度组件的 *Kv* 系数 `3.6`（默认）| 正标量

当 P-T 节流孔完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Vapor operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Kv flow
   coefficient`
4. **Opening characteristic** 设置为
   `Linear`
5. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice Kv flow coefficient vector** — 成员位置向量中各值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **P-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Vapor operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Kv flow
   coefficient`
4. **Opening characteristic** 设置为
   `Tabulated`
5. **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Neutral spool position open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

并且满足以下任一条件：

- **Modeling option** 设置为
  `Liquid operating condition`，
  **Area characteristics** 设置为
  `Different for each flow path`，
  且 **Orifice parameterization** 设置为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 设置为 `Vapor
  operating condition`，**Area
  characteristics** 设置为 `Different for
  each flow path`，且 **Opening
  characteristic** 设置为
  `Tabulated`。

### **P-T maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀运行期间 P-T 节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请将 **Neutral spool position open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

还要将 **Area characteristics** 设置为
`Different for each flow path`，并且满足以下任一条件：

- **Modeling option** 设置为
  `Liquid operating condition`，
  且 **Orifice parameterization** 设置为
  `Linear - Area vs. spool
  travel`。
- **Modeling option** 设置为 `Vapor
  operating condition`，**Orifice
  parameterization** 设置为 `Orifice
  area`，且 **Opening
  characteristic** 设置为
  `Linear`。

### **P-T orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀面积表格参数化的开口面积向量。向量元素必须与 **P-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖关系

要启用此参数，请将 **Neutral spool position open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

还要将 **Area characteristics** 设置为
`Different for each flow path`，并且满足以下任一条件：

- **Modeling option** 设置为
  `Liquid operating condition`，
  且 **Orifice parameterization** 设置为
  `Tabulated data - Area vs. spool
  travel`。
- **Modeling option** 设置为 `Vapor
  operating condition`，**Orifice
  parameterization** 设置为 `Orifice
  area`，且 **Opening
  characteristic** 设置为
  `Tabulated`。

### **P-T orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 和出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-T 节流孔首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 设置为
   `Vapor operating
   condition`
2. **Area characteristics** 设置为
   `Different for each flow
   path`
3. **Orifice parameterization** 设置为
   `Kv flow coefficient` 或
   `Cv flow
   coefficient`
4. **Neutral spool position open connections** 设置为：

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

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

两相流体域中的四通三位方向阀

`4-Way 3-Position Directional Valve (2P)` 模块对两相流体网络中具有四个开口的阀进行建模，通常位于执行器、泵和油箱之间。单个阀芯根据端口 **S** 处的信号控制阀操作。您可以通过在 **Neutral spool position open connections** 参数中指定阀芯处于中性位置（居中于 0 m）时打开的节流孔、在 **Positive spool position open connections** 参数中指定阀芯沿正方向移动时的情况，以及在 **Negative spool position open connections** 参数中指定阀芯沿负方向移动时的情况，来设置阀的基线配置。您可以使用 **Orifice parameterization** 参数将阀模型指定为线性关系或用户提供数据的函数。

此模块是一个复合组件，包含多个 Orifice (2P) 模块实例。有关阀参数化和模块计算的更多信息，请参阅 Orifice (2P) 模块。

在此示例配置中，**Neutral spool position open connections** 参数为 `All closed`。当阀芯处于中性位置时，所有节流孔都关闭，无流动：

在此配置中，**Negative spool position open connections** 为 `P-A, B-T`。当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 和 **A** 之间以及端口 **B** 和 **T** 之间的路径打开，允许流动。端口 **P** 和 **B** 之间以及端口 **A** 和 **T** 之间的路径关闭，不允许流动：

在此配置中，**Positive spool position open connections** 为 `P-B, A-T`。当端口 **S** 处的信号将阀芯移动到正位置时，端口 **P** 和 **B** 之间以及端口 **A** 和 **T** 之间的路径打开，允许流动，端口 **P** 和 **A** 之间以及端口 **B** 和 **T** 之间的路径关闭：

此示意图显示此配置：

左侧对应正位置，右侧对应负位置。

### 滑阀位移和阀配置

*spool stroke* 是节流口从关闭位置完全打开所需的滑阀行程量。您可以使用 **Valve Configuration** 部分中的参数定义 spool stroke。下表显示了该模块如何根据阀节流口参数化和流路特性计算行程。

由端口 **S** 指定的滑阀运动方向取决于 spool stroke 和节流口方向。

| 节流口打开时的滑阀位置 | 滑阀行程, *ΔS* |
| --- | --- |
| Always closed (orifice is not selected in any spool position configuration) | N/A |
| Always open (orifice is selected in positive, neutral, and negative spool position configurations) | N/A |
| Negative | *S*orifice\_max + spool stroke – **S** |
| Negative and Neutral | *S*orifice\_max + spool stroke – **S** |
| Positive | *S*orifice\_max – spool stroke + **S** |
| Positive and Neutral | *S*orifice\_max – spool stroke + **S** |
| Neutral | |*S*orifice\_max| + spool stroke – |**S**| |
| Positive and Negative | –|*S*orifice\_max| + spool stroke – |**S**| |

*S*orifice\_max 是为每个节流口定义的最大节流口面积处的滑阀位置。当 *ΔS* 为负时，节流口面积饱和到泄漏面积；当节流口完全打开时，节流口面积饱和到最大节流口面积。当节流口完全打开时，*ΔS* 等于 spool stroke，因此大于 spool stroke 的 *ΔS* 值不会进一步增大节流口面积。

**Consistency check for neutral spool position open connections** 参数验证：

- 当 **S** 处信号为 0 时，**Neutral spool position open connections** 中列出的任何节流口均打开
- 当 **S** 处信号为 0 时，未在 **Neutral spool position open connections** 中列出的任何节流口均关闭

当任何滑阀位置违反此检查时，您可以选择接收警告或错误。

下表显示了 4-Way 3-Position Directional Valve (TL) block 的可能配置。

| 配置 | 参数值 |
| --- | --- |
|  | 所有四个节流口在 neutral 位置均关闭。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 所有四个节流口在 neutral 位置均打开。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** > –P-B spool stroke - **Spool position at maximum A-T   orifice area** > –A-T spool stroke - **Spool position at maximum B-T   orifice area** < B-T spool   stroke |
|  | 节流口 A-T 和 B-T 关闭。节流口 P-A 和 P-B 重叠。  - **Positive spool position open   connections**:   `P-A` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**:   `P-B`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke |
|  | 节流口 A-T 和 B-T 打开。节流口 P-A 和 P-B 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `A-T,   B-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** > –A-T spool stroke - **Spool position at maximum B-T   orifice area** < B-T spool   stroke |
|  | 节流口 P-A 和 A-T 在 neutral 位置打开。节流口 P-B 和 B-T 重叠。  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `P-A,   A-T` - **Negative spool position open   connections**: `P-A,   B-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** > P-B spool stroke - **Spool position at maximum A-T   orifice area** > A-T spool stroke - **Spool position at maximum B-T   orifice area** < –B-T spool   stroke |
|  | 节流口 A-T 在 neutral 位置打开。节流口 P-B、A-T 和 B-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `A-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** > –A-T spool stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 节流口 B-T 在 neutral 位置打开。节流口 P-A、P-B 和 A-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `B-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** < B-T spool   stroke |
|  | 节流口 P-A 和 P-B 打开。节流口 A-T 和 B-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**: `P-A,   P-B` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** > –P-B spool stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 节流口 P-A 在 neutral 位置打开。节流口 P-B、A-T 和 B-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-A` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 节流口 P-B 在 neutral 位置打开。节流口 P-A、A-T 和 B-T 重叠。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-B` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** > –P-B spool stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke |
|  | 节流口 P-B 和 B-T 在 neutral 位置打开。节流口 P-A 和 A-T 重叠。  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `P-B,   B-T` - **Negative spool position open   connections**: `P-A,   B-T`    - **Spool position at maximum P-A   orifice area** < –P-A spool   stroke - **Spool position at maximum P-B   orifice area** < P-B spool   stroke - **Spool position at maximum A-T   orifice area** > A-T spool stroke - **Spool position at maximum B-T   orifice area** > –B-T spool stroke |
|  | 节流口 P-A、P-B、A-T 和 B-T 在 neutral 位置关闭。P-T 在 neutral 位置打开，并在滑阀位移时关闭。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-T` - **Negative spool position open   connections**: `P-B,   A-T`    - **Spool position at maximum P-A   orifice area** > P-A spool stroke - **Spool position at maximum P-B   orifice area** < –P-B spool   stroke - **Spool position at maximum A-T   orifice area** < –A-T spool   stroke - **Spool position at maximum B-T   orifice area** > B-T spool stroke - **Spool position at maximum P-T   orifice area** = any value |
|  | 节流口 P-A 是恒定节流口。节流口 P-B、A-T 和 B-T 在 neutral 位置打开。  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open   connections**: `P-A,   B-T`    - **Spool position at maximum P-A   orifice area** < P-A spool   stroke - **Spool position at maximum P-B   orifice area** < P-B spool   stroke - **Spool position at maximum A-T   orifice area** = any value - **Spool position at maximum B-T   orifice area** > –B-T spool stroke |
|  | 节流口 P-B 是恒定节流口。节流口 P-A、A-T、B-T 在 neutral 位置打开。    - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open   connections**: `P-A,   P-B`    - **Spool position at maximum P-A   orifice area** > –P-A spool stroke - **Spool position at maximum A-T   orifice area** < A-T spool   stroke - **Spool position at maximum B-T   orifice area** = any value |
|  | 节流口 P-A 在 neutral 位置关闭。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**: `P-A,   B-T`  - |**Spool position at maximum P-A orifice   area**| > P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum B-T orifice   area** < –B-T spool stroke |
|  | 节流口 P-B 在 neutral 位置关闭。端口 **B** 和 **T** 不构成流路。  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `All   closed` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A spool stroke - |**Spool position at maximum P-B orifice   area**| > P-B spool stroke - **Spool position at maximum A-T orifice   area** > A-T spool stroke |
|  | 节流口 P-A 在 neutral 位置关闭。节流口 A-T 在 neutral 位置打开。  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**: `A-T,   B-T` - **Negative spool position open   connections**: `P-A,   B-T`  - |**Spool position at maximum P-A orifice   area**| > P-A spool stroke - **Spool position at maximum P-B orifice   area** > P-B spool stroke - **Spool position at maximum A-T orifice   area** = any value - **Spool position at maximum B-T orifice   area** > –B-T spool stroke |
|  | 节流口 P-B 在 neutral 位置关闭。节流口 B-T 在 neutral 位置打开。  - **Positive spool position open   connections**: `P-B,   A-T` - **Neutral spool position open   connections**: `A-T,   B-T` - **Negative spool position open   connections**: `P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A spool stroke - |**Spool position at maximum P-B orifice   area**| > P-B spool stroke - **Spool position at maximum A-T orifice   area** < A-T spool stroke - **Spool position at maximum B-T orifice   area** = any value |
|  | 节流口 P-B 在 neutral 位置关闭。节流口 P-T 在 neutral 位置打开。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open   connections**: `P-A,   P-B` - **Neutral spool position open   connections**:   `P-T` - **Negative spool position open   connections**: `P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A spool stroke - |**Spool position at maximum P-B orifice   area**| > P-B spool stroke - **Spool position at maximum B-T orifice   area** < –B-T spool stroke - **Spool position at maximum P-T orifice   area** = any value |
|  | 节流口 P-A 在 neutral 位置关闭。节流口 P-T 在 neutral 位置打开。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open   connections**: `P-A,   B-T` - **Neutral spool position open   connections**:   `P-T` - **Negative spool position open   connections**: `P-A,   P-B`  - |**Spool position at maximum P-A orifice   area**| > P-A spool stroke - **Spool position at maximum P-B orifice   area** < –P-B spool stroke - **Spool position at maximum B-T orifice   area** > B-T spool stroke - **Spool position at maximum P-T orifice   area** = any value |

### 阀门节流孔参数化

**Modeling option** 参数控制对建模为蒸气或液体的阀门可用的参数化选项，但不会影响流体属性。该模块根据入口条件计算阀门内部的流体属性。

**Orifice parameterization** 参数指定通过一个或所有阀门节流孔的开度面积或流量的模型。如果将 **Area characteristics** 设置为 `Identical for all flow paths`，则该模块对所有流路应用相同数据。当选择 `Different for all flow paths` 时，该模块对每条流路使用单独的参数化。

**液体阀门参数化**

当 **Modeling option** 为 `Liquid operating condition` 时，模块参数化用于对控制液体流量的阀门建模。

当 **Orifice parameterization** 为 `Linear - Area vs. spool travel` 时，开口面积是在端口 **S** 处作为信号接收的阀芯位置的线性函数

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

其中：

- *ΔS* 是阀芯行程。

  *Aorifice* 在 *ΔS* 为负时饱和于 *Aleak*，并在节流孔完全打开时饱和于 *Amax*。当节流孔完全打开时，*ΔS* 等于阀芯行程，因此大于阀芯行程的 *ΔS* 值不会增大节流孔面积。
- *ΔSmax* 是 **Spool travel between closed and open orifice** 参数的值。
- *Amax* 是 **Maximum orifice area** 参数的值。
- *Aleak* 是 **Leakage area** 参数的值。

  当阀门在线性参数化中处于接近打开或接近关闭的位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，则该模块在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关详细信息，请参阅数值平滑。

当 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel` 时，您可以为系统或端口 **P**、**A**、**B** 和 **T** 之间的各条流路提供阀芯行程向量。该模块使用这些数据计算节流孔面积与阀芯位移之间的关系。该模块使用插值确定给定数据点之间的开口面积。*Aleak* 和 *Amax* 分别是开口面积向量的第一个和最后一个参数。

当 **Orifice parameterization** 为 `Tabulated data - Nominal mass flow rate vs. spool travel` 时，该模块根据您在模块参数中指定的标称条件计算每个节流孔的质量流量。来自端口 **S** 的阀芯位置信号缩放节流孔开口面积，这也可以缩放质量流量。

**蒸气阀门参数化**

当 **Modeling option** 为 `Vapor operating condition` 时，模块参数化设计用于对控制蒸气流动的阀门建模。

该模块用于控制每个节流孔的方法取决于 **Opening characteristic** 参数：

- `Linear` — 流通能力的度量取决于端口 **S** 处的阀芯位置。随着阀芯位移以打开节流孔，流通能力的度量从指定的最小值缩放到指定的最大值。
- `Tabulated` — 该模块将流通能力的度量计算为端口 **S** 处阀芯位置的函数。此函数使用一维查找表。

**Orifice parameterization** 参数决定该模块如何计算每个节流孔中的流量：

- `Cv flow coefficient` — 流量系数 *C*v 缩放每个节流孔中的流量。流量系数衡量流体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，缩放每个节流孔中的流量。流量系数衡量流体在特定压差驱动下流动的难易程度。
- `Orifice area` — 节流孔面积的大小缩放每个节流孔中的流量。

### 可视化节流孔开口

要可视化阀芯偏移和最大位移，请右键单击该模块并选择 **Fluids** > **Plot Valve Characteristics**。绘图显示在 **Valve Configuration** 设置中选择的节流孔。节流孔参数化设置坐标轴，坐标轴为以下之一：

- *Kv* 流量系数、*Cv* 流量系数或节流孔面积对阀芯位置。
- 在特定压差下查询的体积流量对阀芯位置。
- 对于参考流入温度和参考流入压力，在特定压差下查询的质量流量对阀芯位置。

当 **Valve Configuration** 参数中的正、中、负设置具有相同的节流孔时，绘图将节流孔开口显示为常量。

更改模块参数后，要更新数据，请在图窗上点击 **Reload Data**。

此图显示了一个阀门配置示例。在 **Valve Configuration** 设置中：

- **Positive spool position open connections** 为 `P-A, B-T`
- **Neutral spool position open connections** 为 `P-T`
- **Negative spool position open connections** 为 `P-B, A-T`

在 **P-A Orifice** 设置中：

- **Spool position at maximum P-A orifice area** 为 `2.5e-3 m`

所有其他阀芯位置均为默认值。

每个节流孔的面积对阀芯位置的绘图。

可视化显示，P-A 节流孔在阀芯位置 `-2.53e-3` 和 `2.53e-3` m 之间打开。由于 P-A 节流孔仅在阀芯沿正方向位移时打开，将 **Consistency check for neutral spool and position open connections** 参数设置为 `Warning` 会返回：

`Warning: P-A orifice must be closed when the spool is in
the neutral position. Adjust Spool position at maximum P-A orifice area, Neutral
spool position open connections, or Consistency check for neutral spool position
open connections. Right-click on the block and select Fluids > Plot Valve
Characteristics to view the area or flow of each connection versus spool
position.`

要解决此警告，您可以更改：

- 将 **Spool position at maximum P-A orifice area** 改为大于 0.005 m 的值
- 将 **Consistency check for neutral spool position open connections** 改为 `None`
- 通过将 **Neutral spool position open connections** 设置为 `P-A` 来更改阀门配置

### 假设和限制

- 阀门与环境之间没有热交换。
- 当 **Modeling option** 为 `Liquid operating condition` 时，结果在过冷液体区域之外可能不准确。当 **Modeling option** 为 `Vapor operating condition` 时，结果在过热蒸气区域之外可能不准确。要对液-气混合物中的阀门建模，请将 **Modeling option** 设置为 `Liquid operating condition`。
