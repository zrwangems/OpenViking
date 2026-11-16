---
type: simulink-block
title: '3-Way Directional Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '3waydirectionalvalvetl'
documentation_source_path: 'ref/3waydirectionalvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# 3-Way Directional Valve (TL)

## 端口

### 输入

### **S** — 控制构件位移物理信号

阀控制构件的位移，单位为 m。这等效于滑阀位置。
### 守恒

### **P** — 热液体流道

流体可通过其进入或离开阀的开口。该端口通常连接到流体供应管路。

### **T** — 热液体流道

流体可通过其进入或离开阀的开口。该端口通常连接到流体回流管路。

### **A** — 热液体流道

流体可通过其进入或离开阀的开口。该端口通常连接到致动管路。

## 参数

### 模型参数化

### **Positive spool position open connections** — 当滑阀处于正位置时打开的流路 `P-A`（默认）| `All closed` | `P-A, A-T, P-T` | `P-T` | `A-T`

当滑阀处于正位置时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义滑阀运动方向。

### **Negative spool position open connections** — 当滑阀沿负方向移动时打开的流路 `A-T`（默认）| `All closed` | `P-A, A-T, P-T` | `P-A` | `P-T`

当滑阀沿负方向移动时打开的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义滑阀运动方向。

### **Area characteristics** — 节流口的流量方程 `Identical for all flow paths`（默认）| `Different for each flow path`

为阀节流口面积应用统一或单独的流量方程。`Identical for all flow paths` 对所有阀节流口使用相同的节流口和滑阀几何、流量、压力和面积向量。当使用 `Different for each flow path` 时，滑阀偏移和表格数据分配给端口 **P** 与 **A**、端口 **A** 与 **T**、以及端口 **P** 与 **T** 之间的节流口。在两种情况下，端口 **A**、**P** 和 **T** 具有相同的横截面积、流量系数和 Reynolds 数。相同的 **Orifice parameterization** 也应用于所有流路。

### **Orifice parameterization** — 计算开口面积的方法 `Linear area vs. spool travel`（默认）| `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop``Tabulated data - Mass flow rate vs. spool travel and pressure drop`

计算阀开口面积的方法。在表格数据参数化中，可为非线性阀开口曲线提供自己的阀面积和滑阀行程数据，或者以体积流量、滑阀行程和流路压降形式提供数据。热液体域允许使用表格质量流量数据参数化节流口。

### **Spool travel between closed and open orifice** — 最大滑阀行程 `5e-3 m`（默认）| 正标量

滑阀行程的最大距离。此值为计算提供上限，以便仿真不会返回非物理值。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`。

### **Maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀运行期间最大开口面积。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`。

### **Spool travel vector** — 阀开口距离向量 `[0, .00125, .0025, .00375, .005]`m（默认）| 1-by*n* 向量

用于阀面积表格参数化的控制构件行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。值按升序排列，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 8e-05, .0001]`m^2（默认）| 1-by*n* 向量

用于阀开口面积表格参数化的开口面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。元素按升序排列，且必须大于 0。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Opening parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持为指定的泄漏面积。这通过保持流动连续性有助于数值稳定性。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - area vs. spool travel`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，在阀接近打开和接近关闭位置时，基于流量响应引入一层逐渐变化。为提高这些工况下仿真的稳定性，将此参数设置为非零且小于一的值。

### **Spool travel vector, ds** — 阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* 向量

用于体积流量表格参数化的控制构件行程距离向量。滑阀行程向量与 **Pressure drop vector, dp** 参数一起构成独立轴，用于 3-D 因变量 **Volumetric flow rate table, q(ds,dp)** 或 **Mass flow rate table, mdot(ds,dp)** 参数。正位移对应于阀打开。值按升序排列，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Pressure drop vector, dp** — 阀压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* 向量

用于体积流量表格参数化的压降值向量。压降向量与 **Spool travel vector, s** 参数一起构成独立轴，用于 3-D 因变量 **Volumetric flow rate table, q(ds,dp)** 或 **Mass flow rate table, mdot(ds,dp)** 参数。值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Volumetric flow rate table, q(ds,dp)** — 体积流量数组 `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s`（默认）| *M*-by-*N* 矩阵

基于压降和滑阀行程距离独立值的 *M*-by-*N* 体积流量矩阵。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中的元素数量。
- *N* 是 **Pressure drop vector, dp** 参数中的元素数量。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Reference inflow temperature** — 指定压降数据时的温度 `293.15 K`（默认）| 正标量

指定表格压降数据时的温度。

#### 依赖

要启用此参数，将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Reference inflow pressure** — 指定压降表格数据时的压力 `0.101325 MPa`（默认）| 正标量

指定表格压降数据时的压力。模块使用此参数计算第三个参考参数，即参考密度。它使用的参考用于在压力和温度偏离参考条件时缩放表格压降数据。

#### 依赖

要启用此参数，将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Mass flow rate table, mdot(ds,dp)** — 质量流量 `1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s`（默认）| M-by-N 矩阵

对于 *M* 个给定控制构件位置和 *N* 个给定节流口压降的质量流量。控制构件位置表示控制开口面积的滑阀或其他机构。

#### 依赖

要启用此参数，将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

修正因子，用于考虑理论流动中的流量损失。

### **Critical Reynolds number** — 层流的上限 Reynolds 数 `150`（默认）| 正标量

通过阀的层流的 Reynolds 数上限。

### **Pressure recovery** — 是否考虑面积扩大中的压力增加 `on`（默认）| `off`

选择此项以考虑当流体从较小横截面积区域流向较大横截面积区域时的压力增加。

### **Cross-sectional area at ports A, P and T** — 阀入口或出口处的面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **A**、**P** 和 **T** 处的横截面积。这些面积用于确定通过阀的体积流量的压力-流量方程中。

### P-A 节流口

### **Spool position at maximum P-A orifice area** — 端口 P 和 A 之间最大面积时的滑阀偏移 `4.5e-3 m`（默认）| 标量

端口 **P** 和 **A** 之间的初始节流口开口距离。默认表示负重叠系统。

- 如果 **Spool position at maximum orifice area** 的幅值小于 **Spool travel between closed and open orifice** 的值，则节流口为负重叠，或者当滑阀位置等于 0 m 时部分打开。
- 如果 **Spool position at maximum orifice area** 的幅值大于 **Spool travel between closed and open orifice** 的值，则节流口为正重叠。这意味着阀在一定滑阀位置范围内保持关闭。
- 如果 **Spool position at maximum orifice area** 的幅值等于 **Spool travel between closed and open orifice** 的值，则节流口为零重叠。这意味着当滑阀位置等于 0 时阀关闭，并且一旦滑阀位置变化就开始打开。

### **P-A spool travel between closed and open orifice** — 端口 P 和 A 之间滑阀的最大行程 `0.005 m`（默认）| 正标量

端口 **P** 和 **A** 之间节流口的滑阀行程最大距离。此值为计算提供上限，以便仿真不会返回非物理值。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Different for each flow path`。

### **P-A maximum orifice area** — 端口 P 和 A 之间的最大面积 `1e-4 m^2`（默认）| 正标量

端口 **P** 和 **A** 之间节流口在其完全打开位置时的横截面积。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Linear - area vs. spool travel`。

### **P-A orifice spool travel vector** — 阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by*n* 向量

用于阀面积表格参数化的控制构件行程距离向量。向量元素必须与 **P-A orifice area vector** 参数中的元素一一对应。值按升序排列，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **P-A orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 8e-05, .0001] m^2`（默认）| 1-by-*n* 向量

用于阀开口面积表格参数化的开口面积向量。向量元素必须与 **P-A orifice spool travel vector** 参数中的元素一一对应。元素按升序排列，且必须大于 0。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Different for each flow path`，并将 **Opening parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **P-A orifice spool travel vector, ds** — 阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* 向量

用于体积流量表格参数化的控制构件行程距离向量。滑阀行程向量与 **P-A orifice pressure drop vector, dp** 参数一起构成独立轴，用于 3-D 因变量 **P-A orifice volumetric flow rate table, q(s,dp)** 或 **Mass flow rate table, mdot(ds,dp)** 参数。正位移对应于阀打开。值按升序排列，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **P-A orifice pressure drop vector, dp** — 阀上压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* 向量

用于体积流量表格参数化的压降值向量。压降向量与 **P-A orifice spool travel vector, s** 参数一起构成独立轴，用于 3-D 因变量 **P-A orifice volumetric flow rate table, q(s,dp)** 或 **Mass flow rate table, mdot(ds,dp)** 参数。值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖

要启用此参数，将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **P-A 节流孔 (ds,dp)** — 阀体积流量向量 `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s`（默认）| *M*-by-*N* matrix

*M*-by-*N* matrix，表示基于压降和滑阀行程距离的独立值的体积流量。*M* 和 *N* 是相应向量的大小：

- *M* 是
  **P-A 节流孔滑阀行程向量, ds** 参数中的元素数。
- *N* 是
  **P-A 节流孔压降向量, dp** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **P-A 节流孔质量流量表, mdot(ds,dp)** — 阀质量流量向量 `1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s`（默认）| *M*-by-*N* matrix

*M*-by-*N* matrix，表示基于压降和滑阀行程距离的独立值的质量流量。*M* 和 *N* 是相应向量的大小：

- *M* 是
  **P-A 节流孔滑阀行程向量, ds** 参数中的元素数。
- *N* 是
  **P-A 节流孔压降向量, dp** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### A-T 节流孔

### **在最大 A-T 节流孔面积处的滑阀位置** — 端口 A 和 T 之间最大面积处的滑阀偏移 `-4.5e-3 m`（默认）| scalar

端口 **A** 和 **T** 之间的初始节流孔开口距离。默认值表示一个负重叠（underlapped）系统。

- 如果 **在最大节流孔面积处的滑阀位置** 的幅值小于 **关闭与打开节流孔之间的滑阀行程** 的值，则节流孔为负重叠，即当滑阀位置等于 0 m 时部分打开。
- 如果 **在最大节流孔面积处的滑阀位置** 的幅值大于 **关闭与打开节流孔之间的滑阀行程** 的值，则节流孔为正重叠。这意味着阀在一段滑阀位置范围内保持关闭。
- 如果 **在最大节流孔面积处的滑阀位置** 的幅值等于 **关闭与打开节流孔之间的滑阀行程** 的值，则节流孔为零重叠。这意味着当滑阀位置等于 0 时阀关闭，并且一旦滑阀位置变化就开始打开。

### **A-T 滑阀在关闭与打开节流孔之间的行程** — 端口 A 和 T 之间滑阀的最大行程 `0.005 m`（默认）| positive scalar

端口 **A** 和 **T** 之间节流孔的滑阀最大行程距离。该值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 类型设置为 `Different for each flow path`。

### **A-T 最大节流孔面积** — 端口 A 和 T 之间的最大面积 `1e-4 m^2`（默认）| positive scalar

端口 **A** 和 **T** 之间节流孔在完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Linear - area vs. spool travel`。

### **A-T 节流孔滑阀行程向量** — 阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀面积表格参数化的控制构件行程距离向量。向量元素必须与 **A-T 节流孔面积向量** 参数中的元素一一对应。这些值按升序列出，第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **A-T 节流孔面积向量** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 8e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀开口面积表格参数化的开口面积向量。向量元素必须与 **A-T 节流孔滑阀行程向量** 参数中的元素一一对应。这些元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **开口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **A-T 节流孔滑阀行程向量, ds** — 阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于体积流量表格参数化的控制构件行程距离向量。滑阀行程向量与 **A-T 节流孔压降向量, dp** 参数构成独立轴，用于三维因变量 **A-T 节流孔 (ds,dp)** 或 **质量流量表, mdot(ds,dp)** 参数。正位移对应于阀打开。这些值按升序列出，第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **节流孔参数化** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **A-T 节流孔压降向量, dp** — 阀上的压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **A-T 节流孔滑阀行程向量, s** 参数构成独立轴，用于三维因变量 **A-T 节流孔 (ds,dp)** 或 **质量流量表, mdot(ds,dp)** 参数。这些值按升序列出，且必须大于 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **节流孔参数化** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **A-T 节流孔体积流量表, q(ds,dp)** — 用于表格参数化的体积流量向量 - 不同流路 `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s`（默认）| *M*-by-*N* matrix

*M*-by-*N* matrix，表示基于压降和滑阀行程距离的独立值的体积流量。*M* 和 *N* 是相应向量的大小：

- *M* 是
  **A-T 节流孔滑阀行程向量, ds** 参数中的元素数。
- *N* 是
  **A-T 节流孔压降向量, dp** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **A-T 节流孔质量流量表, mdot(ds,dp)** — 用于表格参数化的质量流量向量 - 不同流路 `1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s`（默认）| *M*-by-*N* matrix

*M*-by-*N* matrix，表示基于压降和滑阀行程距离的独立值的质量流量。*M* 和 *N* 是相应向量的大小：

- *M* 是
  **A-T 节流孔滑阀行程向量, ds** 参数中的元素数。
- *N* 是
  **A-T 节流孔压降向量, dp** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### P-T 节流孔

### **在最大 P-T 节流孔面积处的滑阀位置** — 端口 P 和 T 之间最大面积处的滑阀偏移 `4.5e-3 m`（默认）| scalar

端口 **P** 和 **T** 之间的初始节流孔开口距离。默认值表示一个负重叠（underlapped）系统。

- 如果 **在最大节流孔面积处的滑阀位置** 的幅值小于 **关闭与打开节流孔之间的滑阀行程** 的值，则节流孔为负重叠，即当滑阀位置等于 0 m 时部分打开。
- 如果 **在最大节流孔面积处的滑阀位置** 的幅值大于 **关闭与打开节流孔之间的滑阀行程** 的值，则节流孔为正重叠。这意味着阀在一段滑阀位置范围内保持关闭。
- 如果 **在最大节流孔面积处的滑阀位置** 的幅值等于 **关闭与打开节流孔之间的滑阀行程** 的值，则节流孔为零重叠。这意味着当滑阀位置等于 0 时阀关闭，并且一旦滑阀位置变化就开始打开。

### **P-T 滑阀在关闭与打开节流孔之间的行程** — 端口 P 和 T 之间滑阀的最大行程 `0.005 m`（默认）| positive scalar

端口 **P** 和 **T** 之间节流孔的滑阀最大行程距离。该值为计算提供上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 类型设置为 `Different for each flow path`。

### **P-T 最大节流孔面积** — 端口 P 和 T 之间的最大面积 `1e-4 m^2`（默认）| positive scalar

端口 **P** 和 **T** 之间节流孔在完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Linear - area vs. spool travel`。

### **P-T 节流孔滑阀行程向量** — 阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀面积表格参数化的控制构件行程距离向量。向量元素必须与 **P-T 节流孔面积向量** 参数中的元素一一对应。这些值按升序列出，第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **P-T 节流孔面积向量** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 8e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀开口面积表格参数化的开口面积向量。向量元素必须与 **P-T 节流孔滑阀行程向量** 参数中的元素一一对应。这些元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **开口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **P-T 节流孔滑阀行程向量, ds** — 阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于体积流量表格参数化的控制构件行程距离向量。滑阀行程向量与 **P-T 节流孔压降向量, dp** 参数构成独立轴，用于三维因变量 **P-T 节流孔体积流量表, q(ds,dp)** 或 **质量流量表, mdot(ds,dp)** 参数。正位移对应于阀打开。这些值按升序列出，第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **节流孔参数化** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **P-T 节流孔压降向量, dp** — 阀上的压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **P-T 节流孔滑阀行程向量, ds** 参数构成独立轴，用于三维因变量 **P-T 节流孔体积流量表, q(ds,dp)** 或 **质量流量表, mdot(ds,dp)** 参数。这些值按升序列出，且必须大于 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **节流孔参数化** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **P-T 节流孔体积流量表, q(ds,dp)** — 用于表格参数化的体积流量向量 - 不同流路 `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] m^3/s`（默认）| *M*-by-*N* matrix

*M*-by-*N* matrix，表示基于压降和滑阀行程距离的独立值的体积流量。*M* 和 *N* 是相应向量的大小：

- *M* 是
  **P-T 节流孔滑阀行程向量, ds** 参数中的元素数。
- *N* 是
  **P-T 节流孔压降向量, dp** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **P-T 节流孔质量流量表, mdot(ds,dp)** — 用于表格参数化的质量流量向量 - 不同流路 `1e3 * [-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239] kg/s`（默认）| *M*-by-*N* matrix

*M*-by-*N* matrix，表示基于压降和滑阀行程距离的独立值的质量流量。*M* 和 *N* 是相应向量的大小：

- *M* 是
  **P-T 节流孔滑阀行程向量, ds** 参数中的元素数。
- *N* 是
  **P-T 节流孔压降向量, dp** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **节流孔参数化** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### 故障

### **3-Way Directional Valve Area fault** — 用于对阀面积故障建模的选项 `Add fault`

用于在模块中对阀面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。当发生故障时，通常由开口参数化设置的阀面积将根据 **故障时的滑阀位置** 参数中指定的值进行设置。

### **Spool position when faulted** — 故障阀门特性 `Positive`（默认） | `Negative` | `Maintain last value`

故障阀门阀芯位置。您可以选择让阀门在阀芯处于正位置、负位置或故障触发时的位置时卡住。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用 Simscape faults 接口对故障建模

3-Way Directional Valve (TL) 模块现在支持 Simscape™ faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2022b：右键点击模块查看开口特性图

您可以通过右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**，查看每个孔口的面积或体积流量随阀芯位置变化的图。

## 描述

热液网络中的三位方向阀

3-Way Directional Valve (TL) 模块表示热液网络中的一个具有三个开口的阀门，通常位于执行器、泵和储液罐之间。阀门操作由单个阀芯控制，该阀芯根据端口 **S** 处的信号发生位移。您可以通过分别在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中指定当阀芯沿正方向和负方向移动时打开的孔口，来设置阀门的基线配置。

您可以在 **Orifice parameterization** 参数中将阀门开口模型设置为线性关系或用户提供数据的函数，该模型可应用于阀门中的一个或所有流路。

示例阀门配置图

在此配置中，**Positive spool position open connections** 设置为 `A-T`。当端口 **S** 处的信号将阀芯移动到正位置时，端口 **A** 和 **T** 之间的路径打开以允许流动。端口 **P** 和 **A** 之间以及端口 **P** 和 **T** 之间的路径关闭：

显示端口 A 和 T 之间有流动且端口 P 关闭的图

在此配置中，**Negative spool position open connections** 设置为 `P-A`。当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 和 **A** 之间的路径打开以允许流动，并且端口 **T** 和 **A** 之间以及端口 **P** 和 **T** 之间的路径关闭：

显示端口 A 和 P 之间有流动且端口 T 关闭的图

您可以通过将 **Positive spool position open connections** 或 **Negative spool position open connections** 设置为 `P-T` 或 `P-A, A-T, P-T`，来打开端口 **P** 和 **T** 之间的路径。

流路可以在正阀芯位置或负阀芯位置打开，但不能同时在两者中打开。

### 阀门孔口参数化

**Orifice parameterization** 设置用于计算阀门开口面积的方法。计算基于孔口参数或 **Model Parameterization** 选项卡中指定的表格数据。如果 **Area characteristics** 设置为 `Identical for all flow paths`，则模块对所有流路使用相同数据；否则，在 `Different for all flow paths` 设置中应用单独的值。孔口参数化包括：

- `Linear - area vs. spool travel`

  开口面积是阀芯移动距离和端口 **S** 处接收到的信号的线性函数：

  Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

  其中：

  - *A*max 是 **Maximum orifice area**。
  - *A*leak 是 **Leakage area**。
  - *ΔS*max 是 **Spool travel between closed and open orifice**。
  - *ΔS* 是阀芯移动距离。对于在正位置打开的流路：

    ΔS=Sorifice\_max−ΔSmax+S,

    对于在负位置打开的流路：

    ΔS=Sorifice\_max+ΔSmax−S,

    其中 *Sorifice\_max* 是 **Spool position at maximum orifice area**。

  当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关更多信息，请参阅 Numerical Smoothing。

- `Tabulated data - Area vs. spool travel`

  为您的系统或端口 **P** 和 **A**、**A** 和 **T**、**P** 和 **T** 之间的单独流路提供阀芯移动向量。此数据将用于计算孔口开口面积与阀芯移动距离之间的关系。插值用于确定给定数据点之间的开口面积。*A*leak 和 *A*max 分别是 **Opening area vector** 的第一个和最后一个参数。

- `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

  提供阀芯移动和压降向量。体积流量基于压力变化与阀芯移动距离之间的关系计算。插值用于确定给定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

  当您将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop` 时，模块会直接根据控制构件位置和阀门两端的压降计算质量流量。这三个变量之间的关系可以是非线性的，并由 **Spool travel vector, ds**、**Pressure drop vector, dp** 和 **Mass flow rate table, mdot(ds,dp)** 参数中的表格数据给出。

### 可视化孔口开度

要可视化阀芯偏移和位移，请右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示在 **Valve Configuration** 设置中选择的孔口。参数化选择决定坐标轴，坐标轴为以下之一：

- 孔口面积随阀芯位置变化
- 在特定压差下查询的体积流量随阀芯位置变化
- 在参考流入温度和参考流入压力下，并在特定压差下查询的质量流量随阀芯位置变化

更改模块参数后，要更新数据，请在图窗上点击 **Reload Data**。

此图显示一个示例阀门配置。在 **Valve Configuration** 设置中：

- **Positive spool position open connections** 为 `P-A`。
- **Negative spool position open connections** 为 `A-T`。

所有其他阀芯位置均为默认值。

每个孔口的面积随阀芯位置变化图。

### 故障

要对故障建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Introduction to Simscape Faults。

**Spool position when faulted** 参数有三个故障选项：

- `Positive` — 阀芯位置冻结在正位置，并且由 **Positive spool position open connections** 参数指定的流路打开到其最大值。由 **Negative spool position open connections** 参数指定的流路关闭。
- `Negative` — 阀芯位置冻结在正位置，并且由 **Negative spool position open connections** 参数指定的流路打开到其最大值。由 **Positive spool position open connections** 参数指定的流路关闭。
- `Maintain last value` — 当触发发生时，阀门冻结在阀芯位置。

由于在阀门面积极值处的数值平滑，在线性参数化中，模块使用的最小面积大于 **Leakage area**，最大面积小于 **Maximum orifice area**，其大小与 **Smoothing factor** 值成比例。有关更多信息，请参阅 Numerical Smoothing。

故障触发后，阀门在仿真的剩余时间内保持在故障时的面积。

### 假设

- 忽略流体惯性。
- 忽略由惯性力、弹簧力和其他力引起的阀芯载荷。
- 除非另有指定，假设所有阀门孔口尺寸相同。
