---
type: simulink-block
title: '4-Way 2-Position Directional Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way2positiondirectionalvalvetl'
documentation_source_path: 'ref/4way2positiondirectionalvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 2-Position Directional Valve (TL)

## 端口

### 守恒

### **A** — 入口或出口端口 thermal liquid

液体进入或离开阀的端口。

### **B** — 入口或出口端口 thermal liquid

液体进入或离开阀的端口。

### **P** — 入口或出口端口 thermal liquid

液体进入或离开阀的端口。

### **T** — 入口或出口端口 thermal liquid

液体进入或离开阀的端口。

### 输入

### **S** — 滑阀位移，m physical signal

与滑阀位移关联的 physical signal，单位为 m。

## 参数

### 阀配置

### **Positive spool position open connections** — 当滑阀处于正位置时打开的流动路径 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

当滑阀处于正位置时打开的流动路径。此参数设置阀配置，并根据端口 **S** 处接收的信号定义滑阀运动方向。

### **Negative spool position open connections** — 当滑阀沿负方向运动时打开的流动路径 `P-B, A-T`（默认）| `P-A, B-T` | `P-A, P-B` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

当滑阀沿负方向运动时打开的流动路径。此参数设置阀配置，并根据端口 **S** 处接收的信号定义滑阀运动方向。

### 模型参数化

### **Area characteristics** — 节流孔的流量方程 `Identical for all flow paths`（默认）| `Different for each flow path`

是否为阀节流孔面积应用统一或单独的流量方程。将此参数设置为 `Identical for all flow paths` 时，模块对所有阀节流孔使用相同的节流孔和滑阀几何、流量、压力和面积向量。将此参数设置为 `Different for each flow path` 时，可为每个节流孔分别指定这些参数。对于这两种设置，当将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流孔 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **Orifice parameterization** — 计算开口面积的方法 `Linear area vs. spool travel`（默认）| `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | `Tabulated data - Mass flow rate vs. spool travel and pressure drop`

计算阀开口面积的方法。如果将此参数设置为某个表格数据参数化，则可为非线性阀开口剖面提供自己的阀面积和滑阀行程数据，或提供以流量、滑阀行程和流路压降表示的数据。

### **Spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认）| positive scalar

滑阀行程的最大距离。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认）| positive scalar

阀运行期间每个节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Leakage area** — 当节流孔完全关闭时的开口面积 `1e-10 m^2`（默认）| positive scalar

当节流孔完全关闭时的开口面积。模块会将任何小于此值的面积保持为指定的泄漏面积。此参数通过保持流动连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Spool travel vector** — 相对于完全关闭位置的滑阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

根据表格阀面积数据参数化节流孔时的滑阀行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

根据表格阀面积数据参数化节流孔时的开口面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。按升序列出值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Spool travel vector, ds** — 相对于完全关闭位置的滑阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

根据表格体积流量数据参数化节流孔时的滑阀行程距离向量。滑阀行程向量与 **Pressure drop vector, dp** 参数一起构成 2-D 因变量 **Volumetric flow rate table, q(ds,dp)** 参数的独立轴。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Pressure drop vector, dp** — 阀压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* vector

根据表格流量数据参数化节流孔时的压降值向量。压降向量与 **Spool travel vector, ds** 参数一起构成 2-D 因变量 **Volumetric flow rate table, q(ds,dp)** 参数的独立轴。按升序列出值。值必须大于 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Volumetric flow rate table, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*-by-*N* matrix

基于压降和滑阀行程距离独立值的体积流量 *M*-by-*N* matrix。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中的向量元素数。
- *N* 是 **Pressure drop vector, dp** 参数中的向量元素数。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Mass flow rate table, mdot(ds,dp)** — 质量流量数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*-by-*N* matrix

基于压降和滑阀行程距离独立值的质量流量 *M*-by-*N* matrix。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中的向量元素数。
- *N* 是 **Pressure drop vector, dp** 参数中的向量元素数。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Reference inflow temperature** — 指定质量流量数据时的温度 `293.15 K`（默认）| positive scalar

指定表格质量流量数据时的温度。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Reference inflow pressure** — 指定表格质量流量数据时的压力 `0.101325 MPa`（默认）| positive scalar

指定表格质量流量数据时的压力。模块使用此参数计算第三个参考参数，即参考密度，模块使用该参数按偏离参考条件的压力和温度缩放表格压降数据。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Constant orifice area** — 相同流路的节流孔面积 `1e-4 m^2`（默认）| positive scalar

当正和负滑阀位置包含相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为以下之一：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

在 **Valve Configuration** 部分的两个参数中选择相同的节流孔：

- **Positive spool position open connections**
- **Negative spool position open connections**

### **Constant orifice pressure drop vector** — 相同流路的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* vector

当正和负滑阀位置包含相同节流孔时，阀上的压差值向量。向量元素与 **Constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出值。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

在 **Valve Configuration** 部分的两个参数中选择相同的节流孔：

- **Positive spool position open connections**
- **Negative spool position open connections**

### **Constant orifice volumetric flow rate vector** — 相同流路的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1-by-*n* vector

当正和负滑阀位置包含相同节流孔时，恒定节流孔的体积流量值向量。向量元素与 **Constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出值。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

在 **Valve Configuration** 部分的两个参数中选择相同的节流孔：

- **Positive spool position open connections**
- **Negative spool position open connections**

### **Cross-sectional area at ports P, T, A and B** — 守恒端口处的面积 `0.01 m^2`（默认）| positive scalar

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀的质量流量的压力-流量方程中使用该面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| positive scalar

用于考虑理论流动中流量损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为以下之一：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| positive scalar

通过节流孔的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| positive scalar in the range of [0,1]

连续平滑因子，当阀处于接近打开和接近关闭位置时，会基于流量响应引入一层渐变变化。为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. spool travel`。

### **Pressure recovery** — 是否考虑面积扩张中的压力增加 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### P-A 节流孔

### **Spool position at maximum P-A orifice area** — P-A 节流孔完全打开时的滑阀偏移 `5e-3 m`（默认）| positive scalar

P-A 节流孔完全打开时相对于中位位置的滑阀偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一。

将 **Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

将 **Negative spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-A spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认）| positive scalar

滑阀行程的最大距离。此值提供计算的上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

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

### **P-A maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认）| positive scalar

阀运行期间 P-A 节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

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

### **P-A orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m` （默认） | 1-by-*n* vector

用于阀面积的表格参数化的阀芯行程距离向量。向量元素必须与 **P-A orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` （默认） | 1-by-*n* vector

用于阀面积的表格参数化的开口面积向量。向量元素必须与 **P-A spool travel vector** 参数中的元素一一对应。这些元素按升序列出。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m` （默认） | 1-by-*n* vector

用于体积流量的表格参数化的阀芯行程距离向量。阀芯行程向量与 **P-A orifice pressure drop vector, dp** 参数一起构成独立轴，用于二维因变量 **P-A orifice volumetric flow rate table, q(ds,dp)** 和 **P-A orifice mass flow rate table, mdot(ds,dp)** 参数。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice pressure drop vector, dp** — 压降值向量 `[-.1, .3, .5, .7] MPa` （默认） | 1-by-*n* vector

用于体积流量的表格参数化的压降值向量。压降向量与 **P-A orifice spool travel vector, ds** 参数一起构成独立轴，用于二维因变量 **P-A orifice volumetric flow rate table, q(ds,dp)** 和 **P-A orifice mass flow rate table, mdot(ds,dp)** 参数。按升序列出这些值。元素必须大于 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` （默认） | *M*-by-*N* matrix

基于压降和阀芯行程距离独立值的体积流量 *M*-by-*N* matrix。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **P-A orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s` （默认） | *M*-by-*N* matrix

基于压降和阀芯行程距离独立值的质量流量 *M*-by-*N* matrix。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A orifice pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **P-A orifice spool travel vector, ds** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

### **P-A constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2` （默认） | positive scalar

当正和负阀芯位置包含相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-A constant orifice pressure drop vector** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa` （默认） | 1-by-*n* vector

当正和负阀芯位置包含相同节流口时，阀两端的压差值向量。向量元素必须与 **P-A constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-A constant orifice volumetric flow rate vector** — 恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s` （默认） | 1-by-*n* vector

当正和负阀芯位置包含相同节流口时，阀两端的压差值向量。向量元素必须与 **P-A constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-A constant orifice mass flow rate vector** — 恒定节流口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s` （默认） | 1-by-*n* vector

当正和负阀芯位置使用相同节流口时，阀的质量流量值向量。向量元素必须与 **P-A constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-A 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### P-B 节流口

### **Spool position at maximum P-B orifice area** — 完全打开 P-B 节流口时的阀芯偏移 `-5e-3` （默认） | positive scalar

完全打开 P-B 节流口时，阀芯相对于中位位置的偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**Negative spool position open connections** 为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流口设置没有同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m` （默认） | positive scalar

阀芯行程的最大距离。该值提供计算的上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   或将 **Negative spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B maximum orifice area** — 最大节流口开口面积 `1e-4 m^2` （默认） | positive scalar

阀运行期间 P-B 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m` （默认） | 1-by-*n* vector

用于阀面积的表格参数化的阀芯行程距离向量。向量元素必须与 **P-B orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` （默认） | 1-by-*n* vector

用于阀面积的表格参数化的开口面积向量。向量元素必须与 **P-B spool travel vector** 参数中的元素一一对应。按升序列出这些元素。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **Negative spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流口滑阀行程向量, ds** — 相对于完全关闭位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于体积流量表格化参数化的滑阀行程距离向量。滑阀行程向量与 **P-B 节流口压降向量, dp** 参数构成独立轴，用于二维因变量 **P-B 节流口体积流量表, q(ds,dp)** 和 **P-B 节流口质量流量表, mdot(ds,dp)** 参数。按升序列出值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **正滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流口压降向量, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **P-B 节流口滑阀行程向量, ds** 参数构成独立轴，用于二维因变量 **P-B 节流口体积流量表, q(ds,dp)** 和 **P-B 节流口质量流量表, mdot(ds,dp)** 参数。按升序列出值。元素必须大于 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **正滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流口体积流量表, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*×*N* 矩阵

基于压降和滑阀行程距离的独立值的体积流量 *M*×*N* 矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B 节流口滑阀行程向量, ds** 参数中向量元素的数目。
- *N* 是 **P-B 节流口压降向量, dp** 参数中向量元素的数目。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **正滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 节流口质量流量表, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认） | *M*×*N* 矩阵

基于压降和滑阀行程距离的独立值的质量流量 *M*×*N* 矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B 节流口滑阀行程向量, ds** 参数中向量元素的数目。
- *N* 是 **P-B 节流口压降向量, dp** 参数中向量元素的数目。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **正滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

### **P-B 恒定节流口面积** — 恒定节流口的横截面积 `1e-4 m^2`（默认） | 正标量

当正滑阀位置和负滑阀位置包含同一节流口时的节流口面积。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   **正滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流口设置同时出现在 **正滑阀位置开启连接** 和 **负滑阀位置开启连接** 参数中时，才启用此参数。

### **P-B 恒定节流口压降向量** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1×*n* 向量

当正滑阀位置和负滑阀位置包含同一节流口时，阀上的压差值向量。向量元素与 **P-B 恒定节流口体积流量向量** 参数中的元素一一对应。按升序列出值。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **正滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流口设置同时出现在 **正滑阀位置开启连接** 和 **负滑阀位置开启连接** 参数中时，才启用此参数。

### **P-B 恒定体积流量向量** — 恒定节流口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1×*n* 向量

当正滑阀位置和负滑阀位置包含同一节流口时，阀上的体积流量值向量。向量元素与 **P-B 恒定节流口压降向量** 参数中的元素一一对应。按升序列出值。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **正滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流口设置同时出现在 **正滑阀位置开启连接** 和 **负滑阀位置开启连接** 参数中时，才启用此参数。

### **P-B 恒定节流口质量流量向量** — 恒定节流口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认） | 1×*n* 向量

当正滑阀位置和负滑阀位置使用同一节流口时，阀上的质量流量值向量。向量元素与 **P-B 恒定节流口压降向量** 参数中的元素一一对应。按升序列出值。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **正滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

   **负滑阀位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 节流口设置同时出现在 **正滑阀位置开启连接** 和 **负滑阀位置开启连接** 参数中时，才启用此参数。

### A-T 节流口

### **最大 A-T 节流口面积处的滑阀位置** — 完全打开 A-T 节流口时的滑阀偏移 `-5e-3 m`（默认） | 正标量

完全打开 A-T 节流口时相对于中位位置的滑阀偏移。

#### 依赖项

要启用此参数，请设置以下参数之一：

- **正滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
- **负滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

**注意：**

仅当 A-T 节流口设置未同时出现在 **正滑阀位置开启连接** 和 **负滑阀位置开启连接** 参数中时，才启用此参数。

### **关闭与开启节流口之间的 A-T 滑阀行程** — 最大滑阀行程 `0.005 m`（默认） | 正标量

滑阀行程的最大距离。此值对计算提供上限，以便仿真不会返回非物理值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   - **正滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **负滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 最大节流口面积** — 最大节流口开度面积 `1e-4 m^2`（默认） | 正标量

阀运行期间 A-T 节流口的最大开启面积。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   - **正滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **负滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流口滑阀行程向量** — 相对于完全关闭位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于阀面积表格化参数化的滑阀行程距离向量。向量元素必须与 **A-T 节流口面积向量** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   - **正滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **负滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流口滑阀行程向量** — 相对于完全关闭位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于阀面积表格化参数化的滑阀行程距离向量。向量元素必须与 **A-T 节流口面积向量** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   - **正滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **负滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流口滑阀行程向量, ds** — 相对于完全关闭位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于体积流量表格化参数化的滑阀行程距离向量。滑阀行程向量与 **A-T 节流口压降向量, dp** 参数构成独立轴，用于二维因变量 **A-T 节流口体积流量表, q(ds,dp)** 和 **A-T 节流口质量流量表, mdot(ds,dp)** 参数。按升序列出值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   - **正滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **负滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T 节流口压降向量, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **A-T 节流口滑阀行程向量, ds** 参数构成独立轴，用于二维因变量 **A-T 节流口体积流量表, q(ds,dp)** 和 **A-T 节流口质量流量表, mdot(ds,dp)** 参数。按升序列出值。元素必须大于 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性** 为 `Different for each flow path`。
2. **节流口参数化** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   - **正滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。
   - **负滑阀位置开启连接** 为 `P-B, A-T` 或 `P-A, P-B, A-T, B-T`。

### **A-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*-by-*N* matrix

*M*-by-*N* matrix，包含基于压降和阀芯行程距离独立值的体积流量。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T orifice spool travel vector, ds** 参数中的向量元素数。
- *N* 是 **A-T orifice pressure drop vector, dp** 参数中的向量元素数。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Volumetric flow rate vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认） | *M*-by-*N* matrix

*M*-by-*N* matrix，包含基于压降和阀芯行程距离独立值的质量流量。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T orifice spool travel vector, ds** 参数中的向量元素数。
- *N* 是 **A-T orifice pressure drop vector, dp** 参数中的向量元素数。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Mass flow rate vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2`（默认） | positive scalar

当正阀芯位置和负阀芯位置包括同一节流孔时的节流孔面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 在每个参数中满足以下设置之一：

   - 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **A-T constant orifice pressure drop vector** — 恒定节流孔的压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

当正阀芯位置和负阀芯位置包括同一节流孔时，阀门两端的压差值向量。向量元素与 **A-T constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Volumetric flow rate vs. spool travel and pressure drop`
   或 `Tabulated data - Mass flow rate vs. spool travel and pressure
   drop`。
3. 在每个参数中满足以下设置之一：

   - 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **A-T constant orifice volumetric flow rate vector** — 恒定节流孔的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* vector

当正阀芯位置和负阀芯位置包括同一节流孔时的体积流量值向量。向量元素与 **A-T constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Volumetric flow rate vs. spool travel and pressure
   drop`。
3. 在每个参数中满足以下设置之一：

   - 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **A-T constant orifice mass flow rate vector** — 恒定节流孔的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认） | 1-by-*n* vector

当正阀芯位置和负阀芯位置使用同一节流孔时，阀门上的质量流量值向量。向量元素与 **P-B constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。该模块在数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Mass flow rate vs. spool travel and pressure
   drop`。
3. 在每个参数中满足以下设置之一：

   - 将 **Positive spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-B, A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 节流孔设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### B-T 节流孔

### **Spool position at maximum B-T orifice area** — B-T 节流孔完全打开时的阀芯偏移量 `5e-3 m`（默认） | positive scalar

B-T 节流孔完全打开时，阀芯从中位起的偏移量。

#### 依赖项

要启用此参数，请设置以下参数之一：

- 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
  B-T`。
- 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
  B-T`。

**注意：**

仅当 B-T 节流孔设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **B-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

阀芯行程的最大距离。此值提供计算的上限，以避免仿真返回非物理值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear -
   Area vs. spool travel`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认） | positive scalar

阀门运行期间 B-T 节流孔的最大开口面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear -
   Area vs. spool travel`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀门面积表格参数化的阀芯行程距离向量。向量元素必须与 **B-T orifice area vector** 参数中的元素一一对应。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Area vs. spool travel`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀门面积表格参数化的开口面积向量。向量元素必须与 **B-T
orifice spool travel vector** 参数中的元素一一对应。这些元素按升序列出。这些元素必须大于 0。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Area vs. spool travel`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于体积流量表格参数化的控制构件行程距离向量。阀芯行程向量与 **B-T orifice pressure drop vector, dp** 参数形成独立轴，用于二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 和 **B-T orifice mass flow rate table, mdot(ds,dp)** 参数。按升序列出这些值。第一个元素必须为 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Volumetric flow rate vs. spool travel and pressure drop`
   或 `Tabulated data - Mass flow rate vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **B-T
orifice spool travel vector, ds** 参数形成独立轴，用于二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 和 **B-T orifice mass flow rate table, mdot(ds,dp)** 参数。按升序列出这些值。这些元素必须大于 0。该模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Volumetric flow rate vs. spool travel and pressure drop`
   或 `Tabulated data - Mass flow rate vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*-by-*N* matrix

*M*-by-*N* matrix，包含基于压降和阀芯行程距离独立值的体积流量。*M* 和 *N* 是相关向量的大小：

- *M* 是 **B-T
  orifice spool travel vector, ds** 参数中的向量元素数。
- *N* 是 **B-T
  orifice pressure drop vector, dp** 参数中的向量元素数。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Volumetric flow rate vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认） | *M*-by-*N* matrix

*M*-by-*N* matrix，包含基于压降和阀芯行程距离独立值的质量流量。*M* 和 *N* 是相关向量的大小：

- *M* 是 **B-T
  orifice spool travel vector, ds** 参数中的向量元素数。
- *N* 是 **B-T
  orifice pressure drop vector, dp** 参数中的向量元素数。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for
   each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated
   data - Mass flow rate vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   - 将 **Positive spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - 将 **Negative spool position open connections** 设置为 `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

### **B-T constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2`（默认） | positive scalar

当正阀芯位置和负阀芯位置包括同一节流孔时的节流孔面积。

#### 依赖项

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 在每个参数中设置以下之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **B-T constant orifice pressure drop vector** — 用于恒定节流口的压差向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

当正和负阀芯位置包含相同节流口时，阀上的压差值的向量。向量元素与 **B-T constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出这些值。模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Tabulated
   data - Volumetric flow rate vs. spool travel and pressure drop`
   或 `Tabulated data - Mass flow rate vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **B-T constant volumetric flow rate vector** — 用于恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* vector

当正和负阀芯位置包含相同节流口时，阀上的压差值的向量。向量元素与 **B-T constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。模块在表格数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Tabulated
   data - Volumetric flow rate vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **B-T constant orifice mass flow rate vector** — 用于恒定节流口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认） | 1-by-*n* vector

当正和负阀芯位置使用相同节流口时，通过阀的质量流量值的向量。向量元素与 **P-B constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出这些值。模块在数据点之间使用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **Area characteristics** 设置为 `Different for
   each flow path`。
2. **Orifice parameterization** 设置为 `Tabulated
   data - Mass flow rate vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   - **Positive spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open connections** 设置为
     `P-A, B-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 B-T 节流口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### 故障

### **4-Way 2-Position Directional Valve Area fault** — 为阀面积故障建模的选项 `Add fault`

用于在模块中为阀面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。发生故障时，原本由开口参数化设置的阀面积将根据 **Spool position when faulted** 参数中指定的值进行设置。

### **Spool position when faulted** — 发生故障时的阀特性 `Positive`（默认） | `Negative` | `Maintain last value`

故障时的阀芯位置。您可以选择让阀在阀芯处于正位置、负位置或故障触发时的位置时卡滞。

#### 依赖项

要启用此参数，请通过点击 **Add fault** 超链接为模块启用故障。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

4-Way 2-Position Directional Valve (TL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2022b：右键点击模块以查看开口特性图

您可以通过右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**，查看每个节流口的面积或体积流量相对于阀芯位置的图。

## 描述

热液体网络中的四通二位方向阀

4-Way 2-Position Directional Valve (TL) 对热液体网络中的具有四个开口的阀进行建模——例如执行器、泵和油箱之间的阀。单个阀芯根据端口 **S** 处的信号控制阀的操作。您可以通过在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中分别指定当阀芯沿正方向和负方向移动时打开的节流口，来设置阀的基准配置。您可以将 **Orifice parameterization** 参数中的阀开口模型设置为线性关系或用户提供数据的函数，并可将该模型应用于阀中的一个或所有流路。

此模块是一个复合组件，包含多个 Orifice (TL) 模块实例。有关阀参数化和模块计算的更多详细信息，请参阅 Orifice (TL) 模块。在某些配置中，此阀类似于三通阀。要设置当阀芯处于中位时的附加流路，请参阅 4-Way 3-Position Directional Valve (TL) 模块。

此图显示了一个示例阀设置，其中阀连接到油箱、执行器和泵，并且 **Positive spool position open connections** 参数为 `P-B, A-T`：

此图显示了当 **Negative spool position open connections** 参数为 `P-A, B-T` 时的阀：

在此配置中，当端口 **S** 处的信号将阀芯移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径对流动打开。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径对流动关闭。

此图显示了当 **Positive spool position open connections** 参数为 `P-B, A-T` 时的阀：

在此配置中，当端口 **S** 处的信号将阀芯移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径对流动打开，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径关闭。

表示此配置的原理图是：

左侧对应正位置，右侧对应负位置。阀在中间中位段中经过各位置进行过渡。

### 滑阀位移和阀门配置

*滑阀行程* 是孔口从关闭位置完全打开所需的滑阀位移量。您可以使用 **Orifice parameterization** 和 **Area characteristics** 参数来指定流路特性：

| 孔口参数化 | 所有流路相同 | 每条流路不同 |
| --- | --- | --- |
| `Linear - Area vs. spool travel` | **Spool travel between closed and open orifice** 参数定义滑阀行程 | **Spool travel between closed and open orifice** 参数为每个孔口定义滑阀行程 |
| `Tabulated data - Area vs. spool travel` | **Spool travel vector** 参数的第一个和最后一个元素之差定义滑阀行程 | **Spool travel vector** 参数的第一个和最后一个元素之差为每个孔口定义滑阀行程 |
| `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop` | **Spool travel vector, ds** 参数的第一个和最后一个元素之差定义滑阀行程 | **Spool travel vector, ds** 参数的第一个和最后一个元素之差为每个孔口定义滑阀行程 |

滑阀运动的方向取决于滑阀行程、孔口方向以及端口 **S** 处的信号。下表显示了取决于 **Positive spool position open connection** 和 **Negative spool position open connection** 参数选择的孔口滑阀位移：

| 孔口打开时的滑阀位置 | 滑阀位移，*ΔS* |
| --- | --- |
| 孔口始终关闭：未为 **Positive spool position open connection** 或 **Negative spool position open connection** 参数选择孔口 | N/A |
| 孔口始终打开：为 **Positive spool position open connection** 和 **Negative spool position open connection** 参数都选择了孔口 | N/A |
| 负：仅为 **Negative spool position open connection** 参数选择孔口 | *S*orifice\_max + 滑阀行程 – **S** |
| 正：仅为 **Positive spool position open connection** 参数选择孔口 | *S*orifice\_max – 滑阀行程 + **S** |

其中 *S*orifice\_max 是为每个孔口定义的最大孔口面积处的滑阀位置。当 *ΔS* 为负时，孔口面积饱和为泄漏面积；当孔口完全打开时，饱和为最大孔口面积。当孔口完全打开时，*ΔS* 等于滑阀行程，因此 *ΔS* 大于滑阀行程不会进一步增加孔口面积。

下表显示了 4-Way 2-Position Directional Valve (TL) 的可能配置：

| 配置 | 参数值 |
| --- | --- |
| 所有四条流路在过渡期间关闭。 | - **Positive spool position open connections**: `P-A, B-T` - **Negative spool position open connections**: `P-B, A-T` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
| 所有四条流路在过渡期间打开。 | - **Positive spool position open connections**: `P-A, B-T` - **Negative spool position open connections**: `P-B, A-T` - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** < B-T 滑阀行程 |
| A-T 和 B-T 在过渡期间关闭。 | - **Positive spool position open connections**: `P-A, B-T` - **Negative spool position open connections**: `P-B, A-T` - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
| P-A 和 P-B 在过渡期间关闭。 | - **Positive spool position open connections**: `P-A` - **Negative spool position open connections**: `P-B` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 |
| P-B 和 B-T 在过渡期间关闭。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > A-T 滑阀行程 - **Spool position at maximum B-T orifice area** < –B-T 滑阀行程 |
| P-A 和 A-T 在过渡期间关闭。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-A orifice area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > –B-T 滑阀行程 |
| P-A、P-B 和 B-T 在过渡期间打开。 | - **Positive spool position open connections**: `P-A, P-B` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < P-B 滑阀行程 - **Spool position at maximum A-T orifice area** = any value - **Spool position at maximum B-T orifice area** > –B-T 滑阀行程 |
| P-A、A-T 和 B-T 在过渡期间打开。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, P-B` - **Spool position at maximum P-A orifice area** > –P-A 滑阀行程 - **Spool position at maximum A-T orifice area** < A-T 滑阀行程 - **Spool position at maximum B-T orifice area** = any value |
| P-A 和 P-B 在过渡期间关闭。A-T 始终关闭。 | - **Positive spool position open connections**: `P-A, P-B` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum B-T orifice area** < –B-T 滑阀行程 |
| 所有流路在过渡期间关闭。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, P-B` - **Spool position at maximum P-A orifice area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > A-T 滑阀行程 |
| A-T 在过渡期间打开。P-A 在过渡期间关闭。 | - **Positive spool position open connections**: `P-A, P-B` - **Negative spool position open connections**: `P-A, B-T` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** = any value - **Spool position at maximum B-T orifice area** > –B-T 滑阀行程 |
| B-T 在过渡期间打开。P-B 在过渡期间关闭。 | - **Positive spool position open connections**: `P-B, A-T` - **Negative spool position open connections**: `P-A, P-B` - **Spool position at maximum P-A orifice area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < A-T 滑阀行程 - **Spool position at maximum B-T orifice area** = any value |
| P-A 在过渡期间关闭。 | - **Positive spool position open connections**: `P-A, B-T` - **Negative spool position open connections**: `P-A, P-B` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
| P-B 在过渡期间关闭。 | - **Positive spool position open connections**: `P-A, P-B` - **Negative spool position open connections**: `P-B, A-T` - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > –A-T 滑阀行程 |

### 阀门孔口参数化

**Orifice parameterization** 参数指定通过一个或所有阀门孔口的开口面积或流量的模型。如果将 **Area characteristics** 设置为 `Identical for all flow paths`，则模块对所有流路应用相同数据。当选择 `Different for all flow paths` 时，模块为每条流路使用单独的参数化。

当 **Orifice parameterization** 为 `Linear - area vs. spool travel` 时，开口面积是作为端口 **S** 处信号接收的滑阀位置的线性函数

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

其中：

- *ΔS* 是滑阀位移。

  *Aorifice* 在 *ΔS* 为负时饱和为 *Aleak*，在孔口完全打开时饱和为 *Amax*。当孔口完全打开时，*ΔS* 等于滑阀行程，因此 *ΔS* 大于滑阀行程的值不会增加孔口面积。
- *ΔSmax* 是 **Spool travel between closed and open orifice** 参数的值。
- *Amax* 是 **Maximum orifice area** 参数的值。
- *Aleak* 是 **Leakage area** 参数的值。

  当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关详细信息，请参阅数值平滑。

当 **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel` 时，您可以为系统或端口 **P**、**A**、**B** 和 **T** 之间的各条流路提供滑阀位移向量。模块使用此数据计算孔口面积与滑阀位移之间的关系。模块使用插值来确定给定数据点之间的开口面积。*A*leak 和 *A*max 分别是开口面积向量的第一个和最后一个参数。

当 **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 时，您可以提供滑阀位移和压降向量以及相关的二维体积流量数组。模块使用插值来确定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

当 **Orifice parameterization** 为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop` 时，您可以提供滑阀位移和压降向量以及相关的二维质量流量数组。模块使用插值来确定数据点之间的流量。模块根据 **Spool travel vector, ds**、**Pressure drop vector, dp** 和 **Mass flow rate table, mdot(ds,dp)** 参数中的表格数据计算这三个变量之间的关系。

### 可视化孔口开度

要可视化滑阀偏移和最大位移，请右键单击模块，然后选择 **Fluids** > **Plot Valve Characteristics**。绘图显示由 **Valve Configuration** 部分中的参数指定的孔口。坐标轴为以下之一：

- 孔口面积对滑阀位置
- 体积流量对滑阀位置，在特定压差下查询

当您将 **Valve Configuration** 选项卡中的参数设置为同一孔口时，孔口开度为常数。

单击 **Reload Data** 以更新图中的数据。

此图显示了模块的默认配置：

- **Positive spool position open connections** 为 `P-A, B-T`。
- **Negative spool position open connections** 为 `P-B, A-T`。

所有其他滑阀位置均为默认值。

### 故障

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Simscape 故障简介。

**Spool position when faulted** 参数有三个故障选项：

- `Positive` — 滑阀位置冻结在正位置，将 **Positive spool position open connections** 参数指定的流路打开到其最大值。**Negative spool position open connections** 参数指定的流路关闭。
- `Negative` — 滑阀位置冻结在负位置，将 **Negative spool position open connections** 参数指定的流路打开到其最大值。**Positive spool position open connections** 参数指定的流路关闭。
- `Maintain last value` — 阀门在触发发生时的滑阀位置冻结。

由于阀门面积极值处的数值平滑，在线性参数化中，模块使用的最小面积大于 **Leakage area**，最大面积小于 **Maximum orifice area**，其比例与 **Smoothing factor** 值成比例。有关详细信息，请参阅数值平滑。

故障触发后，阀门在仿真的剩余时间内保持在故障面积。

### 预定义参数化

您可以使用预参数化的制造数据填充模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的 "<click to select>" 超链接。
2. **Block Parameterization Manager** 窗口打开。从菜单中选择一个零件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。模块现在具有您指定的参数化。
4. 您可以通过选择零件并查看 **Compare selected part with block** 部分中的数据，在 **Block Parameterization Manager** 窗口中将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。模块对缺失数据用工程判断和简化假设代替。因此，预期仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

要了解更多信息，请参阅预参数化组件列表。
