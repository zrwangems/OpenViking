---
type: simulink-block
title: '4-Way 2-Position Directional Valve (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid Library / Valves and Orifices'
documentation_page: '4way2positiondirectionalvalve2p'
documentation_source_path: 'ref/4way2positiondirectionalvalve2p.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 2-Position Directional Valve (2P)

## 端口

### 守恒

### **A** — 两相流体的入口或出口端口

与阀的入口或出口端口关联的两相流体守恒端口。

### **B** — 两相流体的入口或出口端口

与阀的入口或出口端口关联的两相流体守恒端口。

### **P** — 两相流体的入口或出口端口

与阀的入口或出口端口关联的两相流体守恒端口。

### **T** — 两相流体的入口或出口端口

与阀的入口或出口端口关联的两相流体守恒端口。
### 输入

### **S** — 阀芯位移，m 物理信号

与阀芯位移关联的物理信号，单位为 m。

## 参数

### **建模选项** — 流体相的建模选项 `Liquid operating condition`（默认）| `Vapor operating condition`

阀处流体相的建模选项。如果模块位置处的两相流体处于液态，则将此参数设置为 `Liquid operating condition`。如果模块位置处的两相流体处于蒸气态，则将此参数设置为 `Vapor operating condition`。

### 阀门配置

### **正向阀芯位置打开连接** — 阀芯处于正向位置时打开的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

阀芯处于正向位置时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### **负向阀芯位置打开连接** — 阀芯沿负方向运动时打开的流路 `P-B, A-T`（默认）| `P-A, B-T` | `P-A, P-B` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

阀芯沿负方向运动时打开的流路。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### 模型参数化

### **面积特性** — 节流孔的流动方程 `Identical for all flow paths`（默认）| `Different for each flow path`

是否对阀节流孔面积应用统一或单独的流动方程。当您将此参数设置为 `Identical for all flow paths` 时，模块对所有阀节流孔使用相同的节流孔和阀芯几何尺寸、流量、压力以及面积向量。当您将此参数设置为 `Different for each flow path` 时，您可以分别为每个节流孔指定这些参数。对于这两种设置，当您将 **节流孔参数化** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流孔 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **节流孔参数化** — 可变或恒定节流孔参数化 `Linear - Area vs. spool travel`（默认）| `Linear - Nominal mass flow rate vs. spool travel` | `Tabulated data - Area vs. spool travel` | `Cv flow coefficient` | `Kv flow coefficient` | `Orifice area`

模块用于根据节流孔两端压力差计算质量流量，或根据质量流量计算压力差的方法。

当 **建模选项** 为 `Liquid operating condition` 时，此参数的选项为：

- `Linear - Area vs. spool travel`
- `Linear - Nominal mass flow rate vs. spool travel`
- `Tabulated data - Area vs. spool travel`

当 **建模选项** 为 `Vapor operating condition` 时，此参数的选项为：

- `Cv flow coefficient`
- `Kv flow coefficient`
- `Orifice area`

### **关闭与打开节流孔之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **建模选项** 设置为 `Liquid operating condition`，且 **节流孔参数化** 设置为 `Linear - Area vs. spool travel`。
- **建模选项** 设置为 `Vapor operating condition`，且 **开度特性** 设置为 `Linear`。

### **最大节流孔面积** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间每个节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **建模选项** 设置为 `Liquid operating condition`，且 **节流孔参数化** 设置为 `Linear - Area vs. spool travel`。
- **建模选项** 设置为 `Vapor operating condition`，**节流孔参数化** 设置为 `Orifice area`，且 **开度特性** 设置为 `Linear`。

### **最大节流孔开口处的标称质量流量** — 额定质量流量 `0.1` kg/s（默认）| 正标量

节流孔最大开口位置处的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Identical for all flow paths`，并且 **节流孔参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **最大节流孔开口处的标称压降** — 额定压降 `0.001` MPa（默认）| 正标量

节流孔最大开口位置处的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Identical for all flow paths`，并且 **节流孔参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **标称入口条件规格** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定入口流体状态的方法。模块根据 **标称入口压力** 和 **标称入口条件规格** 参数的值，从表格化流体属性数据中确定节流孔标称入口比容。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Identical for all flow paths`，并且 **节流孔参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **标称入口压力** — 入口流体压力 `0.101325` MPa（默认）| 正标量

标称条件下的入口压力。模块根据 **标称入口压力** 和 **标称入口条件规格** 参数的值，从表格化流体属性数据中确定入口比容。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Identical for all flow paths`，并且 **节流孔参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`。

### **标称入口温度** — 流体温度 `293.15` K（默认）| 正标量

标称运行条件下的入口流体温度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Identical for all flow paths`，**节流孔参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并且 **标称入口条件规格** 设置为 `Temperature`。

### **标称入口蒸气干度** — 入口蒸气干度质量分数 `0`（默认）| 范围 [0,1] 内的正标量

标称运行条件下的入口混合物蒸气干度（按质量分数）。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸气。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Identical for all flow paths`，**节流孔参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并且 **标称入口条件规格** 设置为 `Vapor quality`。

### **标称入口蒸气空隙率** — 入口体积分数 `0`（默认）| 范围 [0,1] 内的正标量

标称运行条件下的入口混合物体积分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸气。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Identical for all flow paths`，**节流孔参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并且 **标称入口条件规格** 设置为 `Vapor void fraction`。

### **标称入口比焓** — 入口流体比焓 `400` kJ/kg（默认）| 正标量

标称运行条件下的入口比焓。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Identical for all flow paths`，**节流孔参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并且 **标称入口条件规格** 设置为 `Specific enthalpy`。

### **标称入口比内能** — 入口比内能 `400` kJ/kg（默认）| 正标量

标称运行条件下的入口比内能。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Identical for all flow paths`，**节流孔参数化** 设置为 `Linear - Nominal mass flow rate vs. spool travel`，并且 **标称入口条件规格** 设置为 `Specific internal energy`。

### **开度特性** — 将控制信号转换为流量能力度量的方法 `Linear`（默认）| `Tabulated`

将端口 **S** 指定的控制信号转换为所选流量能力度量的方法。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`。

### **阀芯行程向量** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

根据表格化阀面积数据对节流孔进行参数化时的阀芯行程距离向量。向量元素必须与 **节流孔面积向量** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。模块使用表数据点之间的线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **建模选项** 设置为 `Liquid operating condition`，且 **节流孔参数化** 设置为 `Tabulated data - Area vs. spool travel`。
- **建模选项** 设置为 `Vapor operating condition`，且 **开度特性** 设置为 `Tabulated`。

### **节流孔面积向量** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

根据表格化阀面积数据对节流孔进行参数化时的开口面积向量。向量元素必须与 **阀芯行程向量** 参数中的元素一一对应。按升序列出这些值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并且满足以下任一条件：

- **建模选项** 设置为 `Liquid operating condition`，且 **节流孔参数化** 设置为 `Tabulated data - Area vs. spool travel`。
- **建模选项** 设置为 `Vapor operating condition`，**节流孔参数化** 设置为 `Orifice area`，且 **开度特性** 设置为 `Tabulated`。

### **最大 Cv 流量系数** — 对应最大开度组件的 *Cv* 系数 `4`（默认）| 正标量

当节流孔完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数度量在压差驱动下蒸气通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，**面积特性** 设置为 `Identical for all flow paths`，**节流孔参数化** 设置为 `Cv flow coefficient`，并且 **开度特性** 设置为 `Linear`。

### **Cv 流量系数向量** — 成员位置向量中各值的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1×*n* 向量

*Cv* 流量系数向量。每个系数对应 **控制构件位置向量** 参数中的一个值。此参数度量在压差驱动下蒸气通过阻力元件的难易程度。向量的大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，**面积特性** 设置为 `Identical for all flow paths`，**节流孔参数化** 设置为 `Cv flow coefficient`，并且 **开度特性** 设置为 `Tabulated`。

### **最大 Kv 流量系数** — 对应最大开度组件的 *Kv* 系数 `3.6`（默认）| 正标量

当节流孔完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数度量在压差驱动下蒸气通过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，**面积特性** 设置为 `Identical for all flow paths`，**节流孔参数化** 设置为 `Kv flow coefficient`，并且 **开度特性** 设置为 `Linear`。

### **Kv 流量系数向量** — 成员位置向量中各值的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1×*n* 向量

*Kv* 流量系数向量。每个系数对应 **控制构件位置向量** 参数中的一个值。此参数度量在压差驱动下蒸气通过阻力元件的难易程度。向量的大小必须与 **控制构件位置向量** 参数相同。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，**面积特性** 设置为 `Identical for all flow paths`，**节流孔参数化** 设置为 `Kv flow coefficient`，并且 **开度特性** 设置为 `Tabulated`。

### **阻塞流时的 xT 压差比系数** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，在该处首次发生阻塞。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，**面积特性** 设置为 `Identical for all flow paths`，并且 **节流孔参数化** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **流量系数** — 流量系数 `0.64`（默认）| 正标量

用于考虑理论流动中排出损失的修正系数。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Vapor operating condition`，并将 **节流孔参数化** 设置为 `Orifice area`；或者将 **建模选项** 设置为 `Liquid operating condition`，并将 **节流孔参数化** 设置为以下任一值：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **泄漏流量分数** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时的流量与打开时的流量之比。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **建模选项** 设置为 `Liquid operating condition`，且 **节流孔参数化** 设置为 `Linear - Area vs. spool travel`。
- **建模选项** 设置为 `Vapor operating condition`，且 **开度特性** 设置为 `Linear`。

### **平滑因子** — 数值平滑因子 `0.01`（默认） | 范围 [0,1] 内的正标量

连续平滑因子，当阀处于接近打开和接近关闭位置时，基于流量响应引入一层渐变。
为提高这些工况下仿真的稳定性，将此参数设置为非零且小于 1 的值。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **节流孔参数化** 设置为 `Linear - area vs. spool travel`；或者将 **建模选项** 设置为 `Vapor operating condition`，并将 **开启特性** 设置为 `Linear`。

### **压力恢复** — 是否考虑面积扩大时的压力升高 `off`（默认） | `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力升高。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`，并将 **节流孔参数化** 设置为以下任一项：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **层流压力比** — 层流-湍流转换压力比 `0.999`（默认） | 正标量

节流孔出口压力与节流孔入口压力之比，在该比值下流体在层流和湍流状态之间转换。
在层流中，压力损失与质量流量成线性关系，在湍流中则成二次关系。

### **入口相变时间常数** — 混合物比容的时间滞后 `0.1` `s`（默认） | 正标量

计算流体比容时液-汽混合物的时间滞后。当入口流体为完全过冷液体或完全过热蒸汽时，此参数不影响比容。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Liquid operating condition`。

### **端口 P、T、A 和 B 处的横截面积** — 守恒端口处的面积 `0.01 m^2`（默认） | 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在用于确定通过阀的质量流量的压力-流量方程中使用该面积。

### P-A 节流孔

### **最大 P-A 节流孔面积处的阀芯位置** — 完全打开的 P-A 节流孔的阀芯偏移 `5e-3 m`（默认） | 正标量

完全打开的 P-A 节流孔相对于中位位置的阀芯偏移。

#### 依赖项

要启用此参数，请设置以下参数之一。

将 **正阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

或将 **负阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流孔设置未同时出现在 **正阀芯位置开启连接** 和 **负阀芯位置开启连接** 参数中时，才启用此参数。

### **关闭和打开节流孔之间的 P-A 阀芯行程** — 最大阀芯行程 `0.005 m`（默认） | 正标量

阀芯行程的最大距离。此值为计算提供上限，以使仿真不会返回非物理值。

#### 依赖项

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**负阀芯位置开启连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

并且满足以下任一条件：

- **建模选项** 设置为 `Liquid operating condition`，**面积特性** 设置为 `Different for each flow path`，且 **节流孔参数化** 设置为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **建模选项** 设置为 `Vapor operating condition`，**面积特性** 设置为 `Different for each flow path`，且 **开启特性** 设置为 `Linear`。

### **最大节流孔开度处的 P-A 额定质量流量** — 额定质量流量 `0.1` `kg/s`（默认） | 正标量

通过最大打开的 P-A 节流孔的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **最大节流孔开度处的 P-A 额定压降** — 额定压降 `0.001` `MPa`（默认） | 正标量

通过最大打开的 P-A 节流孔的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 额定入口条件指定** — 确定入口流体状态的方法 `Temperature`（默认） | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

用于确定 P-A 节流孔入口流体状态的方法。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下至少一个参数：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 额定入口压力** — 入口流体压力 `0.101325` `MPa`（默认） | 正标量

P-A 节流孔在额定条件下的入口压力。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下至少一个参数：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 额定入口温度** — 流体温度 `293.15` `K`（默认） | 正标量

P-A 节流孔在额定工况下的入口流体温度。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件指定** 为 `Temperature`
5. 以下至少一个参数：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 额定入口蒸汽干度** — 入口蒸汽干度质量分数 `0`（默认） | 范围 [0,1] 内的正标量

P-A 节流孔在额定工况下入口混合物的蒸汽干度质量分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件指定** 为 `Vapor quality`
5. 以下至少一个参数：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 额定入口蒸汽空泡分数** — 入口蒸汽空泡分数 `0`（默认） | 范围 [0,1] 内的正标量

P-A 节流孔在额定工况下入口混合物的蒸汽空泡分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件指定** 为 `Vapor void fraction`
5. 以下至少一个参数：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 额定入口比焓** — 入口流体比焓 `400` `kJ/kg`（默认） | 正标量

P-A 节流孔在额定工况下的入口比焓。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件指定** 为 `Specific enthalpy`
5. 以下至少一个参数：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 额定入口比内能** — 入口比内能 `400` `kJ/kg`（默认） | 正标量

P-A 节流孔在额定工况下的入口比内能。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. **额定入口条件指定** 为 `Specific internal energy`
5. 以下至少一个参数：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A 恒定节流孔额定质量流量** — 额定质量流量 `0.1` `kg/s`（默认） | 正标量

通过恒定 P-A 节流孔的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流孔设置同时出现在 **正阀芯位置开启连接** 和 **负阀芯位置开启连接** 参数中时，才启用此参数。

### **P-A 恒定节流孔额定压降** — 额定压降 `0.001` `MPa`（默认） | 正标量

通过恒定 P-A 节流孔的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Liquid operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Linear - Nominal mass flow rate vs. spool travel`
4. 每个参数中的以下设置之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流孔设置同时出现在 **正阀芯位置开启连接** 和 **负阀芯位置开启连接** 参数中时，才启用此参数。

### **P-A 恒定节流孔 Cv 流量系数** — 流量系数 `4`（默认） | 正标量

P-A 节流孔的恒定 *Cv* 流量系数值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Vapor operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Cv flow coefficient`
4. 每个参数中的以下设置之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流孔设置同时出现在 **正阀芯位置开启连接** 和 **负阀芯位置开启连接** 参数中时，才启用此参数。

### **P-A 节流孔最大 Cv 流量系数** — 对应于最大开启组件的 *Cv* 系数 `4`（默认） | 正标量

当 P-A 节流孔完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数衡量在压差驱动下蒸汽穿过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **建模选项** 为 `Vapor operating condition`
2. **面积特性** 为 `Different for each flow path`
3. **节流孔参数化** 为 `Cv flow coefficient`
4. **开启特性** 为 `Linear`
5. 以下参数之一：

   **正阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **负阀芯位置开启连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice Cv flow coefficient vector** — *Cv* 系数，用于成员位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）中的值 | 1-by-*n* vector

*Cv* 流量系数的向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel vector** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Cv flow coefficient`
4. **Opening characteristic** 设置为 `Tabulated`
5. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| positive scalar

P-A 孔口的恒定 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下穿过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient`
4. 每个参数中的以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 孔口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-A orifice maximum Kv flow coefficient** — 对应最大开启组件的 *Kv* 系数 `3.6`（默认）| positive scalar

P-A 孔口全开且可用流动面积最大时的 *Kv* 流量系数值。该参数衡量蒸汽在压差驱动下穿过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient`
4. **Opening characteristic** 设置为 `Linear`
5. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice Kv flow coefficient vector** — *Kv* 系数，用于成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）中的值 | 1-by-*n* vector

*Kv* 流量系数的向量。每个系数对应 **P-A orifice spool travel vector** 参数中的一个值。该参数衡量蒸汽在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **P-A orifice spool travel vector** 参数相同。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient`
4. **Opening characteristic** 设置为 `Tabulated`
5. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice spool travel vector** — 相对于全关位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀门面积表格化参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

并且满足以下任一情况：

- **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Different for each flow path`，且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Different for each flow path`，且 **Opening characteristic** 设置为 `Tabulated`。

### **P-A maximum orifice area** — 最大孔口开启面积 `1e-4 m^2`（默认）| positive scalar

阀门运行期间 P-A 孔口的最大开启面积。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

还要将 **Area characteristics** 设置为 `Different for each flow path`，并且满足以下任一情况：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，且 **Opening characteristic** 设置为 `Linear`。

### **P-A orifice area vector** — 阀门开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀门面积表格化参数化的开启面积向量。向量元素必须与 **P-A orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 并按升序列出。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

还要将 **Area characteristics** 设置为 `Different for each flow path`，并且满足以下任一情况：

- **Modeling option** 设置为 `Liquid operating condition`，且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，且 **Opening characteristic** 设置为 `Tabulated`。

### **P-A constant orifice area** — 恒定孔口的横截面积 `1e-4 m^2`（默认）| positive scalar

当正、负阀芯位置包含同一孔口时的孔口面积。

#### 依赖项

要启用此参数，请在每个参数中设置以下设置之一：

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

并且满足以下任一情况：

- **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Different for each flow path`，且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Different for each flow path`，且 **Opening characteristic** 设置为 `Tabulated`。

**注意：**

仅当 P-A 孔口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-A orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-A 孔口首次发生阻塞。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
4. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### P-B 孔口

### **Spool position at maximum P-B orifice area** — 全开 P-B 孔口的阀芯偏移 `5e-3 m`（默认）| positive scalar

全开 P-B 孔口时阀芯从中位开始的偏移。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

或将 **Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 孔口设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| positive scalar

阀芯行程的最大距离。该值为计算提供上限，以使仿真不返回非物理值。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

并且满足以下任一情况：

- **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Different for each flow path`，且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Different for each flow path`，且 **Opening characteristic** 设置为 `Linear`。

### **P-B nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认）| positive scalar

通过最大开启 P-B 孔口的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认）| positive scalar

通过最大开启 P-B 孔口的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 P-B 孔口入口流体状态的方法。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认）| positive scalar

额定工况下 P-B 孔口的入口压力。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet temperature** — 流体温度 `293.15` `K`（默认）| positive scalar

额定工况下 P-B 孔口的入口流体温度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Temperature`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet vapor quality** — 入口蒸汽干度质量分数 `0`（默认）| positive scalar in the range [0,1]

额定工况下 P-B 孔口入口混合物的质量分数蒸汽干度。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Vapor quality`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet vapor void fraction** — 入口蒸汽空泡份额 `0`（默认）| 范围 [0,1] 内的正标量

P-B 节流孔在名义工况下的入口混合物蒸汽空泡份额。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Vapor void fraction`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认）| 正标量

P-B 节流孔在名义工况下的入口比焓。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Specific enthalpy`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认）| 正标量

P-B 节流孔在名义工况下的入口比内能。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. **Nominal inlet condition specification** 设置为 `Specific internal energy`
5. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B constant orifice nominal mass flow rate** — 名义质量流量 `0.1` `kg/s`（默认）| 正标量

通过恒定 P-B 节流孔的典型、额定或设计质量流量。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 在每个参数中设置以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **P-B constant orifice nominal pressure drop** — 名义压降 `0.001` `MPa`（默认）| 正标量

通过恒定 P-B 节流孔的典型、额定或设计压降。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Liquid operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 在每个参数中设置以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **P-B constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| 正标量

P-B 节流孔的恒定 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Cv flow coefficient`
4. 在每个参数中设置以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **P-B orifice maximum Cv flow coefficient** — 对应于组件最大开度的 *Cv* 系数 `4`（默认）| 正标量

P-B 节流孔完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

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
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice Cv flow coefficient vector** — 构件位置向量中各值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认）| 1-by-*n* vector

*Cv* 流量系数的向量。每个系数对应于 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

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
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| 正标量

P-B 节流孔的恒定 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient`
4. 在每个参数中设置以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **P-B orifice maximum Kv flow coefficient** — 对应于组件最大开度的 *Kv* 系数 `3.6`（默认）| 正标量

P-B 节流孔完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。

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
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice Kv flow coefficient vector** — 构件位置向量中各值对应的 *Kv* 系数 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]`（默认）| 1-by-*n* vector

*Kv* 流量系数的向量。每个系数对应于 **P-B orifice spool travel vector** 参数中的一个值。此参数衡量蒸汽在压差驱动下通过阻力元件的难易程度。向量的大小必须与 **P-B orifice spool travel vector** 参数相同。

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
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Different for each flow path`，并且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Different for each flow path`，并且 **Opening characteristic** 设置为 `Tabulated`。

### **P-B maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-B 节流孔的最大开口面积。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

还要将 **Area characteristics** 设置为 `Different for each flow path`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition` 并且 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，并且 **Opening characteristic** 设置为 `Linear`。

### **P-B orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀面积表格参数化的开口面积向量。向量元素必须与 **P-B orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0，并按升序列出。

#### 依赖项

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

还要将 **Area characteristics** 设置为 `Different for each flow path`，并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition` 并且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Orifice parameterization** 设置为 `Orifice area`，并且 **Opening characteristic** 设置为 `Tabulated`。

### **P-B constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2`（默认）| 正标量

当正和负阀芯位置包含同一节流孔时的节流孔面积。

#### 依赖项

要启用此参数，请在每个参数中设置以下设置之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

并且满足以下任一条件：

- **Modeling option** 设置为 `Liquid operating condition`，**Area characteristics** 设置为 `Different for each flow path`，并且 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- **Modeling option** 设置为 `Vapor operating condition`，**Area characteristics** 设置为 `Different for each flow path`，并且 **Opening characteristic** 设置为 `Tabulated`。

**注意：**

仅当 P-B 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **P-B orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| 正标量

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 P-B 节流孔首次发生阻塞。

#### 依赖项

要启用此参数，请设置：

1. **Modeling option** 设置为 `Vapor operating condition`
2. **Area characteristics** 设置为 `Different for each flow path`
3. **Orifice parameterization** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
4. 以下参数中至少一个：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### A-T Orifice

### **A-T 节流口最大面积处的阀芯位置** — 完全打开 A-T 节流口时的阀芯偏移 `5e-3 m`（默认值） | positive scalar

完全打开 A-T 节流口时相对于中位的阀芯偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- **正阀芯位置开启连接** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。
- **负阀芯位置开启连接** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。

**注意：**

仅当 A-T 节流口设置未同时出现在 **正阀芯位置开启连接** 和
**负阀芯位置开启连接** 参数中时，才会启用此参数。

### **A-T 节流口在关闭和开启之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认值） | positive scalar

阀芯行程的最大距离。此值提供计算的上限，以便仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。
- **负阀芯位置开启连接** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。

并且满足以下任一条件：

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

### **A-T 节流口最大开度下的额定质量流量** — 额定质量流量 `0.1` `kg/s`（默认值） | positive scalar

通过最大开度 A-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 节流口最大开度下的额定压降** — 额定压降 `0.001` `MPa`（默认值） | positive scalar

通过最大开度 A-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数之一：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 额定入口条件规格** — 确定入口流体状态的方法 `Temperature`（默认值） | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 A-T 节流口入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中的至少一个：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 额定入口压力** — 入口流体压力 `0.101325` `MPa`（默认值） | positive scalar

额定条件下 A-T 节流口的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 以下参数中的至少一个：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 额定入口温度** — 流体温度 `293.15` `K`（默认值） | positive scalar

额定工况下 A-T 节流口的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **额定入口条件规格** 为
   `Temperature`
5. 以下参数中的至少一个：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 额定入口蒸汽干度** — 入口蒸汽干度质量分数 `0`（默认值） | positive scalar in the range [0,1]

额定工况下 A-T 节流口的入口混合物蒸汽干度质量分数。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **额定入口条件规格** 为 `Vapor
   quality`
5. 以下参数中的至少一个：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 额定入口蒸汽空隙率** — 入口蒸汽空隙率 `0`（默认值） | positive scalar in the range [0,1]

额定工况下 A-T 节流口的入口混合物蒸汽空隙率。值 `0` 表示入口流体为过冷液体。值 `1` 表示入口流体为过热蒸汽。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **额定入口条件规格** 为 `Vapor void
   fraction`
5. 以下参数中的至少一个：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 额定入口比焓** — 入口流体比焓 `400` `kJ/kg`（默认值） | positive scalar

额定工况下 A-T 节流口的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **额定入口条件规格** 为 `Specific
   enthalpy`
5. 以下参数中的至少一个：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 额定入口比内能** — 入口比内能 `400` `kJ/kg`（默认值） | positive scalar

额定工况下 A-T 节流口的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. **额定入口条件规格** 为 `Specific
   internal energy`
5. 以下参数中的至少一个：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 恒定节流口额定质量流量** — 额定质量流量 `0.1` `kg/s`（默认值） | positive scalar

通过恒定 A-T 节流口的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 在每个参数中满足以下设置之一：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流口设置同时出现在 **正阀芯位置
开启连接** 和 **负阀芯位置开启连接** 参数中时，才会启用此参数。

### **A-T 恒定节流口额定压降** — 额定压降 `0.001` `MPa`（默认值） | positive scalar

通过恒定 A-T 节流口的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Liquid operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Linear - Nominal mass flow rate vs.
   spool travel`
4. 在每个参数中满足以下设置之一：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流口设置同时出现在 **正阀芯位置
开启连接** 和 **负阀芯位置开启连接** 参数中时，才会启用此参数。

### **A-T 恒定节流口 Cv 流量系数** — 流量系数 `4`（默认值） | positive scalar

A-T 节流口的恒定 *Cv* 流量系数的值。此参数衡量蒸汽在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Vapor operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Cv flow
   coefficient`
4. 在每个参数中满足以下设置之一：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流口设置同时出现在 **正阀芯位置
开启连接** 和 **负阀芯位置开启连接** 参数中时，才会启用此参数。

### **A-T 节流口最大 Cv 流量系数** — 对应于最大开度组件的 *Cv* 系数 `4`（默认值） | positive scalar

当 A-T 节流口完全打开且可用于流动的面积最大时，*Cv* 流量系数的值。此参数衡量蒸汽在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Vapor operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Cv flow
   coefficient`
4. **开启特性** 为
   `Linear`
5. 以下参数之一：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 节流口 Cv 流量系数向量** — 成员位置向量中值对应的 *Cv* 系数 `[1e-06, .8, 1.6, 2.4, 3.2, 4]`（默认值） | 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应于 **A-T 节流口阀芯行程向量** 参数中的一个值。此参数衡量蒸汽在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **A-T 节流口阀芯行程向量** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Vapor operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Cv flow
   coefficient`
4. **开启特性** 为
   `Tabulated`
5. 以下参数之一：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T 恒定节流口 Kv 流量系数** — 流量系数 `3.6`（默认值） | positive scalar

A-T 节流口的恒定 *Kv* 流量系数的值。此参数衡量蒸汽在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Vapor operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Kv flow
   coefficient`
4. 在每个参数中满足以下设置之一：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流口设置同时出现在 **正阀芯位置
开启连接** 和 **负阀芯位置开启连接** 参数中时，才会启用此参数。

### **A-T 节流口最大 Kv 流量系数** — 对应于最大开度组件的 *Kv* 系数 `3.6`（默认值） | positive scalar

当 A-T 节流口完全打开且可用于流动的面积最大时，*Kv* 流量系数的值。此参数衡量蒸汽在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **建模选项** 为
   `Vapor operating
   condition`
2. **面积特性** 为
   `Different for each flow
   path`
3. **节流口参数化** 为
   `Kv flow
   coefficient`
4. **开启特性** 为
   `Linear`
5. 以下参数之一：

   - **正阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **负阀芯位置开启连接** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice Kv flow coefficient vector** — 成员位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` 中值的 *Kv* 系数（默认） | 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应于 **A-T orifice spool travel vector** 参数中的一个值。此参数衡量当受到压差驱动时，蒸气穿过阻力元件的容易程度。该向量的大小必须与 **A-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Vapor operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Kv flow coefficient`
4. 将 **Opening characteristic** 设置为 `Tabulated`
5. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T orifice spool travel vector** — 滑阀开启距离相对于完全关闭位置的向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格参数化的滑阀行程距离向量。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

并且满足以下任一条件：

- 将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- 将 **Modeling option** 设置为 `Vapor operating condition`，将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **A-T maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认） | positive scalar

阀运行期间 A-T 节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

同时将 **Area characteristics** 设置为 `Different for each flow path`，并且满足以下任一条件：

- 将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
- 将 **Modeling option** 设置为 `Vapor operating condition`，将 **Orifice parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Linear`。

### **A-T orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀面积表格参数化的开口面积向量。向量元素必须与 **A-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0 且按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

同时将 **Area characteristics** 设置为 `Different for each flow path`，并且满足以下任一条件：

- 将 **Modeling option** 设置为 `Liquid operating condition`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
- 将 **Modeling option** 设置为 `Vapor operating condition`，将 **Orifice parameterization** 设置为 `Orifice area`，并将 **Opening characteristic** 设置为 `Tabulated`。

### **A-T constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2`（默认） | positive scalar

当正和负滑阀位置包括同一节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下之一：

- 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

并且满足以下任一条件：

- 将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel` 或 `Linear - Area vs. spool travel`。
- 将 **Modeling option** 设置为 `Vapor operating condition`，将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Opening characteristic** 设置为 `Tabulated`。

**注意：**

仅当 A-T 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **A-T orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认） | positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 A-T 节流孔首次发生阻塞。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Vapor operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Kv flow coefficient` 或 `Cv flow coefficient`
4. 以下参数中的至少一个：

   - 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### B-T Orifice

### **Spool position at maximum B-T orifice area** — 完全打开 B-T 节流孔时的滑阀偏移量 `5e-3 m`（默认） | positive scalar

B-T 节流孔完全打开时，滑阀相对于中立位置的偏移量。

#### 依赖关系

要启用此参数，请设置以下参数之一。

- 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **B-T spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认） | positive scalar

滑阀行程的最大距离。该值为计算提供上限，以避免仿真返回非物理值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
- 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

并且满足以下任一条件：

- 将 **Modeling option** 设置为 `Liquid operating condition`，将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Linear - Nominal mass flow rate vs. spool travel`。
- 将 **Modeling option** 设置为 `Vapor operating condition`，将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Opening characteristic** 设置为 `Linear`。

### **B-T nominal mass flow rate at maximum orifice opening** — 额定质量流量 `0.1` `kg/s`（默认） | positive scalar

通过最大开启 B-T 节流孔的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal pressure drop at maximum orifice opening** — 额定压降 `0.001` `MPa`（默认） | positive scalar

通过最大开启 B-T 节流孔的典型、额定或设计压降。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet condition specification** — 确定入口流体状态的方法 `Temperature`（默认） | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

确定 B-T 节流孔入口流体状态的方法。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中的至少一个：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet pressure** — 入口流体压力 `0.101325` `MPa`（默认） | positive scalar

B-T 节流孔在标称条件下的入口压力。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 以下参数中的至少一个：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet temperature** — 流体温度 `293.15` `K`（默认） | positive scalar

B-T 节流孔在标称工况下的入口流体温度。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 将 **Nominal inlet condition specification** 设置为 `Temperature`
5. 以下参数中的至少一个：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet vapor quality** — 入口蒸气质量分数干度 `0`（默认） | positive scalar in the range [0,1]

B-T 节流孔在标称工况下的入口混合物蒸气质量分数干度。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸气。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 将 **Nominal inlet condition specification** 设置为 `Vapor quality`
5. 以下参数中的至少一个：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet vapor void fraction** — 入口蒸气空泡份额 `0`（默认） | positive scalar in the range [0,1]

B-T 节流孔在标称工况下的入口混合物蒸气空泡份额。值为 `0` 表示入口流体为过冷液体。值为 `1` 表示入口流体为过热蒸气。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 将 **Nominal inlet condition specification** 设置为 `Vapor void fraction`
5. 以下参数中的至少一个：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet specific enthalpy** — 入口流体比焓 `400` `kJ/kg`（默认） | positive scalar

B-T 节流孔在标称工况下的入口比焓。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 将 **Nominal inlet condition specification** 设置为 `Specific enthalpy`
5. 以下参数中的至少一个：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T nominal inlet specific internal energy** — 入口比内能 `400` `kJ/kg`（默认） | positive scalar

B-T 节流孔在标称工况下的入口比内能。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 将 **Nominal inlet condition specification** 设置为 `Specific internal energy`
5. 以下参数中的至少一个：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

### **B-T constant orifice nominal mass flow rate** — 标称质量流量 `0.1` `kg/s`（默认） | positive scalar

通过恒定 B-T 节流孔的典型、额定或设计质量流量。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Modeling option** 设置为 `Liquid operating condition`
2. 将 **Area characteristics** 设置为 `Different for each flow path`
3. 将 **Orifice parameterization** 设置为 `Linear - Nominal mass flow rate vs. spool travel`
4. 在每个参数中设置以下之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 B-T 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **B-T constant orifice nominal pressure drop** — 标称压降 `0.001` `MPa`（默认） | positive scalar

通过恒定 B-T 节流孔的典型、额定或设计压降。

#### 依赖关系

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
4. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **B-T constant orifice Cv flow coefficient** — 流量系数 `4`（默认）| positive scalar

B-T 孔口的常量 *Cv* 流量系数值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **B-T orifice maximum Cv flow coefficient** — 最大开度组件对应的 *Cv* 系数 `4`（默认）| positive scalar

当 B-T 孔口完全打开且可用于流动的面积最大时的 *Cv* 流量系数值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Linear`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice Cv flow coefficient vector** — 用于构件位置向量 `[1e-06, .8, 1.6, 2.4, 3.2, 4]` 中各值的 *Cv* 系数（默认）| 1-by-*n* vector

*Cv* 流量系数向量。每个系数对应 **B-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **B-T orifice spool travel vector** 参数相同。

#### 依赖关系

要启用此参数，请设置：

1. **Modeling option** 为
   `Vapor operating
   condition`
2. **Area characteristics** 为
   `Different for each flow
   path`
3. **Orifice parameterization** 为
   `Cv flow
   coefficient`
4. **Opening characteristic** 为
   `Tabulated`
5. 以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T constant orifice Kv flow coefficient** — 流量系数 `3.6`（默认）| positive scalar

B-T 孔口的常量 *Kv* 流量系数值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

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
4. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **B-T orifice maximum Kv flow coefficient** — 最大开度组件对应的 *Kv* 系数 `3.6`（默认）| positive scalar

当 B-T 孔口完全打开且可用于流动的面积最大时的 *Kv* 流量系数值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。

#### 依赖关系

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

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice Kv flow coefficient vector** — 用于构件位置向量 `[1e-06, .72, 1.44, 2.16, 2.88, 3.6]` 中各值的 *Kv* 系数（默认）| 1-by-*n* vector

*Kv* 流量系数向量。每个系数对应 **B-T orifice spool travel vector** 参数中的一个值。此参数衡量蒸气在压差驱动下穿过阻力元件的难易程度。向量的大小必须与 **B-T orifice spool travel vector** 参数相同。

#### 依赖关系

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

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。按升序列出这些值。第一个元素必须为 0。模块在表数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。

并且满足以下任一情况：

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

### **B-T maximum orifice area** — 最大孔口开度面积 `1e-4 m^2`（默认）| positive scalar

阀操作期间 B-T 孔口的最大打开面积。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。

还要将 **Area characteristics** 设置为
`Different for each flow path`，并且满足以下任一情况：

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

### **B-T orifice area vector** — 阀开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀面积表格参数化的开度面积向量。向量元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。元素必须大于 0，并按升序列出。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。

还要将 **Area characteristics** 设置为
`Different for each flow path`，并且满足以下任一情况：

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

### **B-T constant orifice area** — 常量孔口的横截面积 `1e-4 m^2`（默认）| positive scalar

当正和负阀芯位置包含同一孔口时的孔口面积。

#### 依赖关系

要启用此参数，请在每个参数中设置以下之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-A,
  B-T` 或 `P-A, P-B, A-T,
  B-T`。

并且满足以下任一情况：

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

仅当 B-T 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **B-T orifice xT pressure differential ratio factor at choked flow** — 压差比 `0.7`（默认）| positive scalar

入口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，其中 B-T 孔口首次发生阻塞。

#### 依赖关系

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
4. 至少以下参数之一：

   - **Positive spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-A,
     B-T` 或 `P-A, P-B, A-T,
     B-T`。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Valves & Orifices / Directional Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

两相流体域中的 4-Way 2-Position Directional Valve

4-Way 2-Position Directional Valve (2P) 对一个两相流体网络中具有四个开口的阀进行建模——例如执行器、泵和油箱之间的阀。单个阀芯根据端口 **S** 处的信号控制阀操作。您可以通过在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中分别指定当阀芯沿正方向和负方向移动时打开的孔口，来设置阀的基线配置。您可以将 **Orifice parameterization** 参数中的阀开度模型设置为线性关系或用户提供数据的函数，并可将其应用于阀中的一个或所有流路。

此模块是一个复合组件，由多个 Orifice (2P) 模块实例组成。有关阀参数化和模块计算的更多详细信息，请参阅 Orifice (2P) 模块。在某些配置中，此阀类似于一个三通阀。要设置阀芯处于中位时的附加流路，请参阅 4-Way 3-Position Directional Valve (2P) 模块。

此图显示了一个示例阀设置，其中阀连接到油箱、执行器和泵，并且 **Positive spool position open connections** 参数为 `P-B, A-T`：

此图显示了当 **Negative spool position open connections** 参数为 `P-A, B-T` 时的阀：

在此配置中，当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 和 **A** 之间以及端口 **B** 和 **T** 之间的路径对流动打开。端口 **P** 和 **B** 之间以及端口 **A** 和 **T** 之间的路径对流动关闭。

此图显示了当 **Positive spool position open connections** 参数为 `P-B, A-T` 时的阀：

在此配置中，当端口 **S** 处的信号将阀芯移动到正位置时，端口 **P** 和 **B** 之间以及端口 **A** 和 **T** 之间的路径对流动打开，端口 **P** 和 **A** 之间以及端口 **B** 和 **T** 之间的路径关闭。

表示此配置的示意图为：

左侧对应正位置，右侧对应负位置。阀通过中位中间段中的位置进行切换。

### 滑阀位移与阀配置

*滑阀行程* 是孔口从关闭位置完全打开所需的滑阀位移量。您可以使用 **Orifice parameterization** 和 **Area characteristics** 参数来指定流路特性：

| 孔口参数化 | 所有流路相同 | 每条流路不同 |
| --- | --- | --- |
| `Linear - Area vs. spool travel` | **Spool travel between closed and open orifice** 参数定义滑阀行程 | **Spool travel between closed and open orifice** 参数为每个孔口定义滑阀行程 |
| `Tabulated data - Area vs. spool travel` | **Spool travel vector** 参数的首元素和末元素之差定义滑阀行程 | 每个孔口的 **Spool travel vector** 参数的首元素和末元素之差定义滑阀行程 |
| `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`or `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | **Spool travel vector, ds** 参数的首元素和末元素之差定义滑阀行程 | **Spool travel vector, ds** 参数的首元素和末元素之差为每个孔口定义滑阀行程 |

滑阀运动方向取决于滑阀行程、孔口方向和端口 **S** 处的信号。下表显示了孔口的滑阀位移，取决于 **Positive spool position open connection** 和 **Negative spool position open connection** 参数的选择：

| 当孔口打开时的滑阀位置 | 滑阀位移，*ΔS* |
| --- | --- |
| 孔口始终关闭：孔口未在 **Positive spool position open connection** 或 **Negative spool position open connection** 参数中选择 | N/A |
| 孔口始终打开：孔口同时被 **Positive spool position open connection** 和 **Negative spool position open connection** 参数选择 | N/A |
| 负：孔口仅被 **Negative spool position open connection** 参数选择 | *S*orifice\_max + 滑阀行程 – **S** |
| 正：孔口仅被 **Positive spool position open connection** 参数选择 | *S*orifice\_max – 滑阀行程 + **S** |

其中 *S*orifice\_max 是为每个孔口定义的最大孔口面积处的滑阀位置。当 *ΔS* 为负时，孔口面积饱和至泄漏面积；当孔口完全打开时，饱和至最大孔口面积。当孔口完全打开时，*ΔS* 等于滑阀行程，因此大于滑阀行程的 *ΔS* 不会进一步增大孔口面积。

下表显示了 4-Way 2-Position Directional Valve (TL) 的可能配置：

| 配置 | 参数值 |
| --- | --- |
| 过渡期间所有四条流路均关闭。 | - **Positive spool position open connections**: `P-A,   B-T` - **Negative spool position open connections**: `P-B,   A-T` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
| 过渡期间所有四条流路均打开。 | - **Positive spool position open connections**: `P-A, B-T` - **Negative spool position open connections**: `P-B, A-T` - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** < B-T 滑阀行程 |
| 过渡期间 A-T 和 B-T 关闭。 | - **Positive spool position open connections**: `P-A, B-T` - **Negative spool position open connections**: `P-B, A-T` - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
| 过渡期间 P-A 和 P-B 关闭。 | - **Positive spool position open connections**: `P-A` - **Negative spool position open connections**: `P-B` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 |
| 过渡期间 P-B 和 B-T 关闭。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > A-T 滑阀行程 - **Spool position at maximum B-T orifice area** < –B-T 滑阀行程 |
| 过渡期间 P-A 和 A-T 关闭。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-A orifice area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > –B-T 滑阀行程 |
| 过渡期间 P-A、P-B 和 B-T 打开。 | - **Positive spool position open connections**: `P-A, P-B` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < P-B 滑阀行程 - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T 滑阀行程 |
| 过渡期间 P-A、A-T 和 B-T 打开。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, P-B` - **Spool position at maximum P-A orifice area** > –P-A 滑阀行程 - **Spool position at maximum A-T orifice area** < A-T 滑阀行程 - **Spool position at maximum B-T orifice area** = 任意值 |
| 过渡期间 P-A 和 P-B 关闭。A-T 始终关闭。 | - **Positive spool position open connections**: `P-A, P-B` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum B-T orifice area** < –B-T 滑阀行程 |
| 过渡期间所有路径均关闭。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, P-B` - **Spool position at maximum P-A orifice area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > A-T 滑阀行程 |
| 过渡期间 A-T 打开。过渡期间 P-A 关闭。 | - **Positive spool position open connections**: `P-A, P-B` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T 滑阀行程 |
| 过渡期间 B-T 打开。过渡期间 P-B 关闭。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, P-B` - **Spool position at maximum P-A orifice area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < A-T 滑阀行程 - **Spool position at maximum B-T orifice area** = 任意值 |
| 过渡期间 P-A 关闭。 | - **Positive spool position open connections**: `P-A, B-T` - **Negative spool position open connections**: `P-A, P-B` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
| 过渡期间 P-B 关闭。 | - **Positive spool position open connections**: `P-A, P-B` - **Negative spool position open connections**: `P-B, A-T` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > –A-T 滑阀行程 |

### 阀孔口参数化

**Modeling option** 参数控制为建模蒸气或液体而设计的阀的参数化选项，但不影响流体属性。模块根据入口条件计算阀内流体属性。

**Orifice parameterization** 参数指定通过一个或所有阀孔口的开口面积或流量的模型。如果将 **Area characteristics** 设置为 `Identical for all flow paths`，模块对所有流路应用相同数据。当选择 `Different for all flow paths` 时，模块对每条流路使用单独参数化。

**液体阀参数化**

当 **Modeling option** 为 `Liquid operating condition` 时，模块参数化设计用于控制液体流量的阀。

当 **Orifice parameterization** 为 `Linear - Area vs. spool travel` 时，开口面积是端口 **S** 处作为信号接收的滑阀位置的线性函数

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

其中：

- *ΔS* 是滑阀位移。

  *Aorifice* 在 *ΔS* 为负时饱和至 *Aleak*，在孔口完全打开时饱和至 *Amax*。当孔口完全打开时，*ΔS* 等于滑阀行程，因此大于滑阀行程的 *ΔS* 值不会增大孔口面积。
- *ΔSmax* 是 **Spool travel between closed and open orifice** 参数的值。
- *Amax* 是 **Maximum orifice area** 参数的值。
- *Aleak* 是 **Leakage area** 参数的值。

  当阀在线性参数化中处于接近打开或接近关闭位置时，可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关详细信息，请参阅 Numerical Smoothing。

当 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel` 时，可以为系统或端口 **P**、**A**、**B** 和 **T** 之间的各条流路提供滑阀位移向量。模块使用此数据计算孔口面积与滑阀位移之间的关系。模块使用插值确定给定数据点之间的开口面积。*A*leak 和 *A*max 分别是开口面积向量的第一个和最后一个参数。

当 **Orifice parameterization** 为 `Tabulated data - Nominal mass flow rate vs. spool travel` 时，模块根据您在模块参数中指定的标称条件计算每个孔口的质量流量。来自端口 **S** 的滑阀位置信号缩放孔口开口面积，这也可以缩放质量流量。

**蒸气阀参数化**

当 **Modeling option** 为 `Vapor operating condition` 时，模块参数化设计用于建模控制蒸气流动的阀。

模块用于控制每个孔口的方法取决于 **Opening characteristic** 参数：

- `Linear` — 流量能力的度量取决于端口 **S** 处的滑阀位置。当滑阀位移以打开孔口时，流量能力的度量从指定的最小值缩放到指定的最大值。
- `Tabulated` — 模块将流量能力的度量计算为端口 **S** 处滑阀位置的函数。此函数使用一维查找表。

**Orifice parameterization** 参数确定模块如何计算每个孔口中的流量：

- `Cv flow coefficient` — 流量系数 *C*v 缩放每个孔口中的流量。流量系数衡量流体在特定压差驱动下流动的容易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，缩放每个孔口中的流量。流量系数衡量流体在特定压差驱动下流动的容易程度。
- `Orifice area` — 孔口面积的尺寸缩放每个孔口中的流量。

### 可视化孔口开度

要可视化滑阀偏移和最大位移，请右键单击模块，然后选择 **Fluids** > **Plot Valve Characteristics**。绘图显示 **Valve Configuration** 部分中的参数所指定的孔口。当将 **Valve Configuration** 选项卡中的参数设置为同一孔口时，孔口开度为常量。

单击 **Reload Data** 以更新图中的数据。

此图像显示模块的默认配置：

- **Positive spool position open connections** 为 `P-A, B-T`
- **Negative spool position open connections** 为 `P-B, A-T`

所有其他滑阀位置均为默认值。

### 假设与限制

- 阀与环境之间没有热交换。
- 当 **Modeling option** 为 `Liquid operating condition` 时，在过冷液体区域之外结果可能不准确。当 **Modeling option** 为 `Vapor operating condition` 时，在过热蒸气区域之外结果可能不准确。要对液-蒸气混合物中的阀建模，请将 **Modeling option** 设置为 `Liquid operating condition`。
