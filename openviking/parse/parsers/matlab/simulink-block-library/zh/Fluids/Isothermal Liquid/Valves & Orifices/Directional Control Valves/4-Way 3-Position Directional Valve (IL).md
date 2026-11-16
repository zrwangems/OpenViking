---
type: simulink-block
title: '4-Way 3-Position Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way3positiondirectionalvalveil'
documentation_source_path: 'ref/4way3positiondirectionalvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 3-Position Directional Valve (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

液体进入或离开阀的端口。

### **B** — 液体端口 isothermal liquid

液体进入或离开阀的端口。

### **P** — 液体端口 isothermal liquid

液体进入或离开阀的端口。

### **T** — 液体端口 isothermal liquid

液体进入或离开阀的端口。
### 输入

### **S** — 阀芯位移，m physical signal

阀芯位移，以 m 为单位，指定为 physical signal。

## 参数

### 阀配置

### **Positive spool position open connections** — 当阀芯处于正位置时打开的流路 `P-A, B-T` (default) | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯处于正位置时打开的流路。此参数设置阀配置，并根据端口 **S** 接收到的信号定义阀芯运动方向。当 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error` 时，可以检查此参数的设置与其他节流孔定义的一致性。

### **Neutral spool position open connections** — 当阀芯处于中位时打开的流路 `All closed` (default) | `P-A, P-B, A-T, B-T` | `A-T, B-T` | `P-A, A-T` | `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-B, B-T` | `A-T` | `B-T` | `P-A` | `P-B` | `P-T` | `P-A, A-T, P-T` | `P-A, P-B, A-B` | `P-B, B-T, P-T` | `P-A, P-B, A-T, B-T, P-T`

当阀芯处于中位时打开的流路。此参数设置阀配置，并根据端口 **S** 接收到的信号定义阀芯运动方向。当 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error` 时，可以检查此参数的设置与其他节流孔定义的一致性。

### **Negative spool position open connections** — 当阀芯沿负方向移动时打开的流路 `P-A, B-T` (default) | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯沿负方向移动时打开的流路。此参数设置阀配置，并根据端口 **S** 接收到的信号定义阀芯运动方向。当 **Consistency check for neutral spool position open connections** 设置为 `Warning` 或 `Error` 时，可以检查此参数的设置与其他节流孔定义的一致性。

### **Consistency check for neutral spool position open connections** — 是否检查节流孔设置是否与指定的最大节流孔开度时的阀芯位置一致 `Warning` (default) | `Error` | `None`

是否检查 **Valve Configuration** 选项卡上的中位阀芯位置打开设置是否与最大节流孔面积时指定的阀芯位置一致。对于每个启用的节流孔，阀芯中位处的实际偏移应与每个单独节流孔指定的阀芯偏移相称。

### 模型参数化

### **Area characteristics** — 节流孔的流量方程 `Identical for all flow paths` (default) | `Different for each flow path`

为阀节流孔面积应用统一或单独的流量方程。`Identical for all flow paths` 对所有阀节流孔使用相同的节流孔和阀芯几何、流量、压力和面积向量。使用 `Different for each flow path` 时，这些参数为每个节流孔单独指定。在两种情况下，节流孔 **A**、**B**、**P** 和 **T** 在 `Linear - Area vs. spool travel` 和 `Tabulated data - Area vs. spool travel` 参数化中具有相同的横截面积、流量系数和雷诺数。相同的 **Orifice parameterization** 应用于所有流路。

### **Orifice parameterization** — 计算开口面积的方法 `Linear area vs. spool travel` (default) | `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

计算阀开口面积的方法。在表格数据参数化中，您可以为非线性阀开口剖面提供自己的阀面积和阀芯行程数据，或者以流路中的体积流量、阀芯行程和压力降的形式提供数据。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m` (default) | positive scalar

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2` (default) | positive scalar

阀运行期间每个节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Leakage area** — 节流孔完全关闭时的开口面积 `1e-9 m^2` (default) | positive scalar

节流孔完全关闭时的开口面积。任何小于此值的面积都保持为指定的泄漏面积。此参数通过保持流量连续性来帮助数值稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。值按升序排列，且第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Orifice area vector** — 阀开口面积向量 `[1e-09, 1e-05, 4e-05, 6e-05, .0001] m^2` (default) | 1-by-*n* vector

用于阀开口面积表格参数化的开口面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。元素按升序排列，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m` (default) | 1-by-*n* vector

用于体积流量表格参数化的阀芯行程距离向量。阀芯行程向量与 **Pressure drop vector, dp** 参数一起构成二维因变量 **Volumetric flow rate table, q(ds,dp)** 参数的独立轴。值按升序排列，且第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Pressure drop vector, dp** — 阀压力降值向量 `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

用于体积流量表格参数化的压力降值向量。压力降向量与 **Spool travel vector, ds** 参数一起构成二维因变量 **Volumetric flow rate table, q(ds,dp)** 参数的独立轴。值按升序排列，且必须大于 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Volumetric flow rate table, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (default) | *M*-by-*N* matrix

基于压力降和阀芯行程距离独立值的体积流量 *M*-by-*N* 矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **Pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Constant orifice area** — 相同流路的节流孔面积 `1e-4 m^2` (default) | positive scalar

当正、中、负阀芯位置具有相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为以下之一：

- `Linear - area vs. spool travel`。
- `Tabulated data - Area vs. spool travel`

必须在以下三个 **Valve Configuration** 参数中选择相同的节流孔：

- **Positive spool position open connections**
- **Neutral spool position open connections**
- **Negative spool position open connections**

### **Constant orifice pressure drop vector** — 相同流路的压力差值向量 `[-.1, .3, .5, .7] MPa` (default) | 1-by-*n* vector

当正、中、负阀芯位置具有相同节流孔时，阀上的压力差值向量。向量元素与 **Constant orifice volumetric flow rate vector** 参数中的元素一一对应。值按升序排列。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

必须在以下三个 **Valve Configuration** 参数中选择相同的节流孔：

- **Positive spool position open connections**
- **Neutral spool position open connections**
- **Negative spool position open connections**

### **Constant orifice volumetric flow rate vector** — 相同流路的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s` (default) | 1-by-*n* vector

当正、中、负阀芯位置具有相同节流孔时，恒定节流孔的体积流量值向量。向量元素与 **Constant orifice pressure drop vector** 参数中的元素一一对应。值按升序排列。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

必须在以下三个 **Valve Configuration** 参数中选择相同的节流孔：

- **Positive spool position open connections**
- **Neutral spool position open connections**
- **Negative spool position open connections**

### **Cross-sectional area at ports P, T, A and B** — 守恒端口处的面积 `inf m^2` (default) | positive scalar

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，用于确定通过阀的质量流量的压力-流量方程中。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为以下之一：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Discharge coefficient** — 流量系数 `0.64` (default) | positive scalar

考虑理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为以下之一：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Critical Reynolds number** — 层流的上限雷诺数 `150` (default) | positive scalar

通过节流孔的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Smoothing factor** — 数值平滑因子 `0.01` (default) | positive scalar in the range of [0,1]

连续平滑因子，当阀处于接近打开和接近关闭位置时，基于流量响应引入渐进变化层。为了提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. spool travel`。

### **Pressure recovery** — 是否考虑面积扩张中的压力增加 `off` (default) | `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### P-A 节流孔

### **Spool position at maximum P-A orifice area** — 完全打开的 P-A 节流孔的阀芯偏移 `7.5e-3 m` (default) | positive scalar

完全打开的 P-A 节流孔的阀芯从中位起的偏移。如果不一致或不符合其他节流孔阀芯位置的物理意义，**Consistency check for neutral spool position open connections** 参数会通知您。要可视化定义的偏移，请参阅 Visualize Orifice Openings。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`

**注意：**

仅当 P-A 节流孔设置未同时出现在所有三个阀芯位置参数中时，才启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-A spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m` (default) | positive scalar

阀芯行程的最大距离。此值提供计算的上限，以使仿真不返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认） | positive scalar

在阀工作期间 P-A 节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格化参数化的阀芯行程距离向量。向量元素必须与 **P-A orifice area vector** 参数中的元素一一对应。值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀开口面积表格化参数化的开口面积向量。向量元素必须与 **P-A spool travel vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **P-A orifice pressure drop vector, dp** 参数一起，为二维因变量 **P-A orifice volumetric flow rate table, q(ds,dp)** 参数构成一个独立轴。值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice pressure drop vector, dp** — 压降值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

用于体积流量表格化参数化的压降值向量。压降向量与 **P-A orifice spool travel vector, ds** 参数一起，为二维因变量 **P-A orifice volumetric flow rate table, q(ds,dp)** 参数构成一个独立轴。值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*-by-*N* matrix

基于压降和阀芯行程距离独立值的体积流量 *M*-by-*N* matrix。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **P-A orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A constant orifice area** — 恒定节流孔的横截面积 `1e-4 m^2`（默认） | positive scalar

当正、中、负阀芯位置具有相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A constant orifice pressure drop vector** — 恒定节流孔的压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

当正、中、负阀芯位置具有相同节流孔时，阀上的压差值向量。向量元素必须与 **P-A constant orifice volumetric flow rate vector** 参数中的元素一一对应。值按升序列出。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### **P-A constant orifice volumetric flow rate vector** — 恒定节流孔的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* vector

当正、中、负阀芯位置具有相同节流孔时，阀上的压差值向量。向量元素必须与 **P-A constant orifice pressure drop vector** 参数中的元素一一对应。值按升序列出。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`

### P-B 节流孔

### **Spool position at maximum P-B orifice area** — 完全打开 P-B 节流孔时阀芯相对中位的偏移量 `7.5e-3 m`（默认） | positive scalar

完全打开 P-B 节流孔时阀芯相对中位的偏移量。**Consistency check for neutral spool position open connections** 参数将通知您，如果为此阀芯位置设置的值根据其他节流孔阀芯位置是不一致或不物理的。要可视化定义的偏移量，请参阅 Visualize Orifice Openings。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`

**Neutral spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`

**Negative spool position open connections** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`

**注意：**

仅当 P-B 节流孔设置未出现在以下全部三个阀芯位置参数中时，才启用此参数：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

最大阀芯行程距离。该值提供计算上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   或将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   或将 **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B maximum orifice area** — 最大节流孔开口面积 `1e-4 m^2`（默认） | positive scalar

在阀工作期间 P-B 节流孔的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格化参数化的阀芯行程距离向量。向量元素必须与 **P-B orifice area vector** 参数中的元素一一对应。值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀开口面积表格化参数化的开口面积向量。向量元素必须与 **P-B spool travel vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **Negative spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B 节流口阀芯行程向量, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m` (默认) | 1-by-*n* vector

用于体积流量表格参数化的阀芯行程距离向量。阀芯行程向量与 **P-T 节流口压降向量, dp** 参数形成独立轴，用于二维因变量 **P-T 节流口体积流量表, q(ds,dp)** 参数。值按升序列出，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`.

   **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B 节流口压降向量, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa` (默认) | 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **P-B 节流口阀芯行程向量, ds** 参数形成独立轴，用于二维因变量 **P-B 节流口体积流量表, q(ds,dp)** 参数。值按升序列出，且必须大于 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B 节流口体积流量表, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (默认) | *M*-by-*N* matrix

*M*-by-*N* 体积流量矩阵，基于压降和阀芯行程距离的独立值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B 节流口阀芯行程向量, ds** 参数中向量元素的数量。
- *N* 是 **P-B 节流口压降向量, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B 恒定节流口面积** — 恒定节流口的横截面积 `1e-4 m^2` (默认) | positive scalar

当正、中、负阀芯位置具有相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为以下之一：

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的以下设置之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B 恒定节流口压降向量** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa` (默认) | 1-by-*n* vector

当正、中、负阀芯位置具有相同节流口时，阀上的压差值向量。向量元素与 **P-B 恒定节流口体积流量向量** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. 每个参数中的以下设置之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### **P-B 恒定节流口体积流量向量** — 恒定节流口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s` (默认) | 1-by-*n* vector

当正、中、负阀芯位置具有相同节流口时，阀上的体积流量值向量。向量元素与 **P-B 恒定节流口压降向量** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. 每个参数中的以下设置之一：

   **正阀芯位置打开连接** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

   **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`

### A-T 节流口

### **最大 A-T 节流口面积时的阀芯位置** — 完全打开 A-T 节流口时，阀芯从中位偏移的距离 `7.5e-3 m` (默认) | positive scalar

完全打开 A-T 节流口时，阀芯从中位偏移的距离。**中位阀芯位置打开连接一致性检查** 参数将在此阀芯位置设置的值根据其他节流口阀芯位置不一致或不物理时通知您。要直观查看定义的偏移量，请参阅 Visualize Orifice Openings。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置打开连接** 设置为 `P-B,
  A-T`。
- **中位阀芯位置打开连接** 设置为：

  - `P-A, P-B, A-T,
    B-T`
  - `P-B, A-T`
  - `A-T, B-T`
  - `P-A, A-T`
  - `A-T`
- **负阀芯位置打开连接** 设置为 `P-B,
  A-T`。

**注意：**

仅当 A-T 节流口设置未出现在所有三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中位阀芯位置打开连接** 和 **负阀芯位置打开连接**。

### **A-T 节流口关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m` (默认) | positive scalar

阀芯行程的最大距离。此值提供计算上限，使仿真不返回不物理的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Linear - Area vs. spool
   travel`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为 `P-B,
   A-T`

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置打开连接** 设置为 `P-B,
   A-T`.

### **A-T 最大节流口面积** — 最大节流口开口面积 `1e-4 m^2` (默认) | positive scalar

阀门操作期间 A-T 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Linear - Area vs. spool
   travel`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为 `P-B,
   A-T`

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置打开连接** 设置为 `P-B,
   A-T`.

### **A-T 节流口阀芯行程向量** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m` (默认) | 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。向量元素必须与 **A-T 节流口面积向量** 参数中的元素一一对应。值按升序列出，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Area vs. spool
   travel`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为 `P-B,
   A-T`.

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置打开连接** 设置为 `P-B,
   A-T`.

### **A-T 节流口面积向量** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (默认) | 1-by-*n* vector

用于阀开口面积表格参数化的开口面积向量。向量元素必须与 **A-T 阀芯行程向量** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Area vs. spool
   travel`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为 `P-B,
   A-T`.

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置打开连接** 设置为 `P-B,
   A-T`.

### **A-T 节流口阀芯行程向量, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m` (默认) | 1-by-*n* vector

用于体积流量表格参数化的阀芯行程距离向量。阀芯行程向量与 **A-T 节流口压降向量, dp** 参数形成独立轴，用于二维因变量 **A-T 节流口体积流量表, q(ds,dp)** 参数。值按升序列出，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为 `P-B,
   A-T`.

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置打开连接** 设置为 `P-B,
   A-T`.

### **A-T 节流口压降向量, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa` (默认) | 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **A-T 节流口阀芯行程向量, ds** 参数形成独立轴，用于二维因变量 **A-T 节流口体积流量表, q(ds,dp)** 参数。值按升序列出，且必须大于 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为 `P-B,
   A-T`.

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置打开连接** 设置为 `P-B,
   A-T`.

### **A-T 节流口体积流量表, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (默认) | *M*-by-*N* matrix

*M*-by-*N* 体积流量矩阵，基于压降和阀芯行程距离的独立值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T 节流口阀芯行程向量, ds** 参数中向量元素的数量。
- *N* 是 **A-T 节流口压降向量, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设置为
   `Different for each flow
   path`.
2. **节流口参数化** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`.
3. 以下参数之一：

   **正阀芯位置打开连接** 设置为 `P-B,
   A-T`.

   **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   **负阀芯位置打开连接** 设置为 `P-B,
   A-T`.

### **A-T 恒定节流口面积** — 恒定节流口的横截面积 `1e-4 m^2` (默认) | positive scalar

当正、中、负阀芯位置具有相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 在以下每个参数中设置以下之一：

   将 **Positive spool position open connections** 设置为 `P-B, A-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   将 **Negative spool position open connections** 设置为 `P-B, A-T`。

### **A-T constant orifice pressure drop vector** — 恒定节流口的压差取值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

当正、中、负滑阀位置具有相同节流口时，阀门上的压差取值向量。向量元素与 **A-T constant orifice volumetric flow rate vector** 参数中的元素一一对应。取值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 在以下每个参数中设置以下之一：

   将 **Positive spool position open connections** 设置为 `P-B, A-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   将 **Negative spool position open connections** 设置为 `P-B, A-T`。

### **A-T constant orifice volumetric flow rate vector** — 恒定节流口的体积流量取值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* vector

当正、中、负滑阀位置具有相同节流口时的体积流量取值向量。向量元素与 **Constant orifice volumetric flow rate vector** 参数中的元素一一对应。取值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 在以下每个参数中设置以下之一：

   将 **Positive spool position open connections** 设置为 `P-B, A-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`

   将 **Negative spool position open connections** 设置为 `P-B, A-T`。

### B-T Orifice

### **Spool position at maximum B-T orifice area** — 完全打开 B-T 节流口时相对于中位的滑阀偏移 `7.5e-3 m`（默认） | positive scalar

完全打开 B-T 节流口时相对于中位的滑阀偏移。如果为此滑阀位置设置的值根据其他节流口滑阀位置不一致或不符合物理意义，**Consistency check for neutral spool position open connections** 参数会通知你。要可视化定义的偏移，请参阅 Visualize Orifice Openings。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- 将 **Positive spool position open connections** 设置为 `P-A, B-T`。
- 将 **Neutral spool position open connections** 设置为：

  - `P-A, P-B, A-T, B-T`
  - `A-T, B-T`
  - `P-A, B-T`
  - `P-B, B-T`
  - `B-T`
- 将 **Negative spool position open connections** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 节流口设置未同时出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **B-T spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认） | positive scalar

滑阀行程的最大距离。此值为计算提供上限，使仿真不会返回不符合物理意义的值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
3. 设置以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认） | positive scalar

阀门操作期间 B-T 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
3. 设置以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice spool travel vector** — 相对于完全关闭位置的滑阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀门面积表格参数化的滑阀行程距离向量。向量元素必须与 **B-T orifice area vector** 参数中的元素一一对应。取值按升序列出，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
3. 设置以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀门开口面积表格参数化的开口面积向量。向量元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
3. 设置以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice spool travel vector, ds** — 相对于完全关闭位置的滑阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于体积流量表格参数化的控制构件行程距离向量。滑阀行程向量与 **B-T orifice pressure drop vector, dp** 参数一起构成二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 参数的独立轴。取值按升序列出，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 设置以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

用于体积流量表格参数化的压力降取值向量。压力降向量与 **B-T orifice spool travel vector, ds** 参数一起构成二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 参数的独立轴。取值按升序列出，且必须大于 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 设置以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*-by-*N* matrix

基于压力降和滑阀行程距离独立值的体积流量 *M*-by-*N* 矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **B-T orifice spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **B-T orifice pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 设置以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认） | positive scalar

当正、中、负滑阀位置具有相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 在以下每个参数中设置以下之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T constant orifice pressure drop vector** — 恒定节流口的压差取值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

当正、中、负滑阀位置具有相同节流口时，阀门上的压差取值向量。向量元素与 **B-T constant orifice volumetric flow rate vector** 参数中的元素一一对应。取值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 在以下每个参数中设置以下之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T constant orifice volumetric flow rate vector** — 恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* vector

当正、中、负滑阀位置具有相同节流口时，阀门上的压差取值向量。向量元素与 **B-T constant orifice pressure drop vector** 参数中的元素一一对应。取值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 在以下每个参数中设置以下之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Neutral spool position open connections** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### P-T Orifice

### **Spool position at maximum P-T orifice area** — 完全打开 P-T 节流口时相对于中位的滑阀偏移 `0 m`（默认） | positive scalar

完全打开 P-T 节流口时相对于中位的滑阀偏移。如果为此滑阀位置设置的值根据其他节流口滑阀位置不一致或不符合物理意义，**Consistency check for neutral spool position open connections** 参数会通知你。要可视化定义的偏移，请参阅 Visualize Orifice Openings。

#### 依赖关系

要启用此参数，请将 **Neutral spool position open connections** 设置为

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

。

### **P-T spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认） | positive scalar

滑阀行程的最大距离。此值为计算提供上限，使仿真不会返回不符合物理意义的值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
3. 将 **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认） | positive scalar

阀门操作期间 P-T 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
3. 将 **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 节流孔阀芯行程向量** — 阀芯开口距离相对于全关位置的向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于阀门面积表格参数化的控制构件行程距离向量。该向量的元素必须与 **P-T 节流孔面积向量** 参数中的元素一一对应。这些值按升序列出，且第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow
   path`.
2. 将 **节流孔参数化** 设置为
   `Tabulated data - Area vs. spool
   travel`.
3. 将 **中位阀芯位置开启连接** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 节流孔阀芯行程向量, ds** — 阀芯开口距离相对于全关位置的向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1×*n* 向量

用于体积流量表格参数化的控制构件行程距离向量。对于二维因变量 **P-T 节流孔体积流量表, q(ds,dp)** 参数，阀芯行程向量与 **P-T 节流孔压降向量, dp** 参数构成独立轴。这些值按升序列出，且第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow
   path`.
2. 将 **节流孔参数化** 设置为
   `Tabulated data - Area vs. spool
   travel`.
3. 将 **中位阀芯位置开启连接** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 节流孔压降向量, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1×*n* 向量

用于体积流量表格参数化的压降值向量。对于二维因变量 **P-T 节流孔体积流量表, q(ds,dp)** 参数，压降向量与 **P-T 节流孔阀芯行程向量, ds** 参数构成独立轴。这些值按升序列出，且必须大于 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow
   path`.
2. 将 **节流孔参数化** 设置为
   `Tabulated data - Area vs. spool
   travel`.
3. 将 **中位阀芯位置开启连接** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T 节流孔体积流量表, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*×*N* 矩阵

*M*×*N* 体积流量矩阵，基于压降和阀芯行程距离的独立值。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-T 节流孔阀芯行程向量, ds** 参数中的向量元素数量。
- *N* 是 **P-T 节流孔压降向量, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. 将 **面积特性** 设置为
   `Different for each flow
   path`.
2. 将 **节流孔参数化** 设置为
   `Tabulated data - Area vs. spool
   travel`.
3. 将 **中位阀芯位置开启连接** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### 故障

### **4-Way 3-Position Directional Valve 面积故障** — 用于对阀门面积故障建模的选项 `Add fault`

用于在模块中对阀门面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。发生故障时，通常由开口参数化设置的阀门面积将根据 **发生故障时的阀芯位置** 参数中指定的值进行设置。

### **发生故障时的阀芯位置** — 故障阀门特性 `Positive`（默认） | `Neutral` | `Negative` | `Maintain last value`

发生故障时的阀门阀芯位置。您可以选择阀门在阀芯处于正位置、负位置或故障触发时所在位置时卡滞。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

4-Way 3-Position Directional Valve (IL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

等温液体系统中的四通三位方向阀

4-Way 3-Position Directional Valve (IL) 模块对等温液体网络中的具有四个开口的阀门进行建模，通常位于执行器、泵和油箱之间。阀门操作由单个阀芯控制，该阀芯根据端口 **S** 处的信号发生位移。您可以通过以下方式设置阀门的基线配置：在 **中位阀芯位置开启连接** 参数中指定阀芯处于中位（以 0 m 为中心）时开启的节流孔，在 **正阀芯位置开启连接** 参数中指定阀芯沿正方向移动时开启的节流孔，以及在 **负阀芯位置开启连接** 参数中指定阀芯沿负方向移动时开启的节流孔。

您可以在 **节流孔参数化** 参数中将阀门开口的模型设置为线性关系或用户提供数据的函数，该模型可应用于阀门中的一个或所有流动路径。

**阀门设置示例**

在此示例配置中，**中位阀芯位置开启连接** 设置为 `All closed`。当阀芯处于中位时，所有节流孔均关闭以阻止流动：

在此配置中，**负阀芯位置开启连接** 设置为 `P-A, B-T`。当端口 **S** 处的信号使阀芯移动到负位置时，端口 **P** 和 **A** 之间以及端口 **B** 和 **T** 之间的路径开启以允许流动。端口 **P** 和 **B** 之间以及端口 **A** 和 **T** 之间的路径关闭以阻止流动：

在此配置中，**正阀芯位置开启连接** 设置为 `P-B, A-T`。当端口 **S** 处的信号使阀芯移动到正位置时，端口 **P** 和 **B** 之间以及端口 **A** 和 **T** 之间的路径开启以允许流动，端口 **P** 和 **A** 之间以及端口 **B** 和 **T** 之间的路径关闭以阻止流动：

示意性地，此配置如下所示：

左侧对应正位置，右侧对应负位置。

### 滑阀位移和阀门配置

*滑阀行程* 是节流口从关闭位置到完全打开所需的滑阀位移量，并且针对 **Valve Configuration** 选项卡上选择的每个节流口定义。下表显示了如何根据阀门节流口参数化和流路特性计算该行程。

**基于参数化和流路特性的滑阀行程**

| 节流口参数化 | 所有流路相同 | 每条流路不同 |
| --- | --- | --- |
| Linear - Area vs. spool travel | 由 **Spool travel between closed and open orifice** 参数定义 | 由每个节流口的 Spool travel between closed and open orifice 参数定义 |
| Tabulated data - Area vs. spool travel | **Spool travel vector** 参数的第一个和最后一个元素之间的差值 | 每个节流口的 spool travel vector 参数的第一个和最后一个元素之间的差值 |
| Tabulated data - Volumetric flow rate vs. spool travel and pressure drop | **Spool travel vector, ds** 参数的第一个和最后一个元素之间的差值 | 每个节流口的 spool travel vector, ds 参数的第一个和最后一个元素之间的差值 |

Visualize Orifice Openings 一节详细介绍了如何查看所有阀门节流口的方向。

在端口 **S** 处发出信号的滑阀运动方向取决于滑阀行程和节流口方向：

**节流口定义和滑阀位移方向**

| 节流口打开时的滑阀位置 | 滑阀位移，*ΔS* |
| --- | --- |
| 始终关闭（未在任何滑阀位置配置中选择该节流口） | N/A |
| 始终打开（在正、中位和负滑阀位置配置中选择该节流口） | N/A |
| 负 | *S*orifice\_max + 滑阀行程 – **S** |
| 负和中位 | *S*orifice\_max + 滑阀行程 – **S** |
| 正 | *S*orifice\_max – 滑阀行程 + **S** |
| 正和中位 | *S*orifice\_max – 滑阀行程 + **S** |
| 中位 | \|*S*orifice\_max\| + 滑阀行程 – \|**S**\| |
| 正和负 | –\|*S*orifice\_max\| + 滑阀行程 – \|**S**\| |

其中 *S*orifice\_max 是为每个节流口定义的最大节流口面积处的滑阀位置。当 *ΔS* 为负时，节流口面积在泄漏面积处饱和；当节流口完全打开时，节流口面积在最大节流口面积处饱和。当节流口完全打开时，*ΔS* 等于滑阀行程，因此大于滑阀行程的 *ΔS* 不会进一步增大节流口面积。

**Consistency check for neutral spool position open connections** 参数验证：

- **Neutral spool position open connections** 中列出的任何节流口在端口 **S** 处的信号为 0 时均打开。
- 任何未在 **Neutral spool position open connections** 中列出的节流口在端口 **S** 处的信号为 0 时均关闭。

可以选择在此检查被违反时接收警告或错误。

下面显示了 4-Way 3-Position Directional Valve (IL) 模块的可能配置。

**4-Way 3-Position Directional Valve 配置**

| 配置 | 参数值 |
| --- | --- |
|  | 所有四个节流口在中位时关闭。（默认）  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `All   closed` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
|  | 所有四个节流口在中位时打开。  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** < B-T 滑阀行程 |
|  | 节流口 A-T 和 B-T 关闭。节流口 P-A 和 P-B 重叠。  - **Positive spool position open connections**: `P-A` - **Neutral spool position open connections**: `All   closed` - **Negative spool position open connections**: `P-B`    - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 |
|  | 节流口 A-T 和 B-T 打开。节流口 P-A 和 P-B 重叠。  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `A-T,   B-T` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** < B-T 滑阀行程 |
|  | 节流口 P-A 和 A-T 在中位时打开。节流口 P-B 和 B-T 重叠。  - **Positive spool position open connections**: `P-B,   A-T` - **Neutral spool position open connections**: `P-A,   A-T` - **Negative spool position open connections**: `P-A,   B-T`    - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > A-T 滑阀行程 - **Spool position at maximum B-T orifice area** < –B-T 滑阀行程 |
|  | 节流口 A-T 在中位时打开。节流口 P-B、A-T 和 B-T 重叠。  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `A-T` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
|  | 节流口 B-T 在中位时打开。节流口 P-A、P-B 和 A-T 重叠。  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `B-T` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** < B-T 滑阀行程 |
|  | 节流口 P-A、P-B 打开。节流口 A-T 和 B-T 重叠。  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `P-A,   P-B` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
|  | 节流口 P-A 在中位时打开。节流口 P-B、A-T 和 B-T 重叠。  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `P-A` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
|  | 节流口 P-B 在中位时打开。节流口 P-A、A-T 和 B-T 重叠。  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `P-B` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 |
|  | 节流口 P-B 和 B-T 在中位时打开。节流口 P-A 和 A-T 重叠。  - **Positive spool position open connections**: `P-B,   A-T` - **Neutral spool position open connections**: `P-B,   B-T` - **Negative spool position open connections**: `P-A,   B-T`    - **Spool position at maximum P-A orifice area** < –P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > –B-T 滑阀行程 |
|  | 节流口 P-A、P-B、A-T 和 B-T 在中位时关闭。P-T 在中位时打开，并在滑阀位移时关闭。  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `P-T` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < –A-T 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 - **Spool position at maximum P-T orifice area** = 任意值 |
|  | 节流口 P-A 是恒定节流口。节流口 P-B、A-T 和 B-T 在中位时打开。  - **Positive spool position open connections**: `P-A,   P-B` - **Neutral spool position open connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open connections**: `P-A,   B-T`    - **Spool position at maximum P-A orifice area** < P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < P-B 滑阀行程 - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T 滑阀行程 |
|  | 节流口 P-B 是恒定节流口。节流口 P-A、A-T、B-T 在中位时打开。  - **Positive spool position open connections**: `P-B,   A-T` - **Neutral spool position open connections**: `P-A, P-B,   A-T, B-T` - **Negative spool position open connections**: `P-A,   P-B`    - **Spool position at maximum P-A orifice area** > –P-A 滑阀行程 - **Spool position at maximum A-T orifice area** < A-T 滑阀行程 - **Spool position at maximum B-T orifice area** = 任意值 |
|  | 节流口 P-A 在中位时关闭。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open connections**: `P-A,   P-B` - **Neutral spool position open connections**: `All   closed` - **Negative spool position open connections**: `P-A,   B-T`    - \|**Spool position at maximum P-A orifice area**\| > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum B-T orifice area** < –B-T 滑阀行程 |
|  | 节流口 P-B 在中位时关闭。端口 **B** 和 **T** 不构成流路。  - **Positive spool position open connections**: `P-B,   A-T` - **Neutral spool position open connections**: `All   closed` - **Negative spool position open connections**: `P-A,   P-B`    - **Spool position at maximum P-A orifice area** < –P-A 滑阀行程 - \|**Spool position at maximum P-B orifice area**\| > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** > A-T 滑阀行程 |
|  | 节流口 P-A 在中位时关闭。节流口 A-T 在中位时打开。  - **Positive spool position open connections**: `P-A,   P-B` - **Neutral spool position open connections**: `A-T,   B-T` - **Negative spool position open connections**: `P-A,   B-T`    - \|**Spool position at maximum P-A orifice area**\| > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T 滑阀行程 |
|  | 节流口 P-B 在中位时关闭。节流口 B-T 在中位时打开。  - **Positive spool position open connections**: `P-B,   A-T` - **Neutral spool position open connections**: `A-T,   B-T` - **Negative spool position open connections**: `P-A,   P-B`    - **Spool position at maximum P-A orifice area** < –P-A 滑阀行程 - \|**Spool position at maximum P-B orifice area**\| > P-B 滑阀行程 - **Spool position at maximum A-T orifice area** < A-T 滑阀行程 - **Spool position at maximum B-T orifice area** = 任意值 |
|  | 节流口 P-B 在中位时关闭。节流口 P-T 在中位时打开。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open connections**: `P-A,   P-B` - **Neutral spool position open connections**: `P-T` - **Negative spool position open connections**: `P-B,   A-T`    - **Spool position at maximum P-A orifice area** > P-A 滑阀行程 - \|**Spool position at maximum P-B orifice area**\| > P-B 滑阀行程 - **Spool position at maximum B-T orifice area** < –B-T 滑阀行程 - **Spool position at maximum P-T orifice area** = 任意值 |
|  | 节流口 P-A 在中位时关闭。节流口 P-T 在中位时打开。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open connections**: `P-A,   B-T` - **Neutral spool position open connections**: `P-T` - **Negative spool position open connections**: `P-A,   P-B`    - \|**Spool position at maximum P-A orifice area**\| > P-A 滑阀行程 - **Spool position at maximum P-B orifice area** < –P-B 滑阀行程 - **Spool position at maximum B-T orifice area** > B-T 滑阀行程 - **Spool position at maximum P-T orifice area** = 任意值 |

### 阀门孔口参数化

**Orifice parameterization** 参数设置通过一个或所有阀门孔口的开口面积或体积流量的模型。如果 **Area characteristics** 设置为 `Identical for all flow paths`，则该模块对所有流路应用相同数据；否则，对于 `Different for all flow paths` 设置，将应用单独的参数化。您可以通过三种方式对阀门开度建模：

- `Linear - area vs. spool travel`

  开口面积是作为端口 **S** 处信号接收的滑阀位置的线性函数：

  Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

  其中：

  - *ΔS* 是在 Orifice Definition and Spool Travel Direction 中定义的滑阀行程。
  - *ΔSmax* 是 **Spool travel between closed and open orifice**。
  - *Amax* 是 **Maximum orifice area**。
  - *Aleak* 是 **Leakage area**。

  当 *ΔS* 为负时，*Aorifice* 在 *Aleak* 处饱和；当孔口完全打开时，*Aorifice* 在 *Amax* 处饱和。当孔口完全打开时，*ΔS* 等于滑阀行程，因此 *ΔS* 大于滑阀行程不会进一步增大孔口面积。

  当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，模块将在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关详细信息，请参阅数值平滑。
- `Tabulated data - Area vs. spool travel`

  为您的系统或端口 **P**、**A**、**B** 和 **T** 之间的各个流路提供滑阀行程向量。此数据将用于计算孔口面积与滑阀位移之间的关系。插值用于确定给定数据点之间的开口面积。*A*leak 和 *A*max 分别是开口面积向量的第一个和最后一个参数。
- `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

  提供滑阀行程和压降向量，以及一个相关的二维体积流量数组。插值用于确定给定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

### 可视化孔口开度

要可视化滑阀偏移和最大位移，请右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**。绘图显示在 **Valve Configuration** 设置中选定的孔口。孔口参数化设置坐标轴，坐标轴为以下之一：

- 孔口面积与滑阀位置的关系
- 在特定压差下查询的体积流量与滑阀位置的关系

当 **Valve Configuration** 中的正、中、负设置使用同一孔口时，绘图将孔口开度显示为常量。

更改模块参数后，要更新数据，请在图形窗口中点击 **Reload Data**。

此图显示了一个示例阀门配置。在 **Valve Configuration** 设置中：

- **Positive spool position open connections** 为 `P-A, B-T`。
- **Neutral spool position open connections** 为 `P-T`。
- **Negative spool position open connections** 为 `P-B, A-T`。

在 **P-A Orifice** 设置中：

- **Spool position at maximum P-A orifice area** 为 `2.5e-3 m`。

所有其他滑阀位置均为默认值。

**滑阀位置可视化示例**

可视化显示，P-A 孔口在滑阀位置 `-2.53e-3` 和 `2.53e-3` m 之间打开。由于 P-A 孔口仅在滑阀沿正方向位移时打开，将 **Consistency check for neutral spool and position open connections** 参数设置为 `Warning` 会返回：

`Warning: P-A orifice must be closed when the spool is in the neutral position. Adjust Spool position at maximum P-A orifice area, Neutral spool position open connections, or Consistency check for neutral spool position open connections. Right-click on the block and select Fluids > Plot Valve Characteristics to view the area or flow of each connection versus spool position.`

要解决此警告，您可以更改：

- **Spool position at maximum P-A orifice area** 为大于 0.005 m 的值。
- **Consistency check for neutral spool position open connections** 为 `None`。
- 通过将 **Neutral spool position open connections** 设置为 `P-A` 来更改阀门配置。

### 故障

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Simscape 故障简介。

**Spool position when faulted** 参数有四个故障选项：

- `Positive` — 滑阀位置冻结在正位置，将 **Positive spool position open connections** 参数指定的流路打开到其最大值。由 **Negative spool position open connections** 和 **Neutral spool position open connections** 参数指定的流路关闭。
- `Neutral` — 滑阀位置冻结在中位，将所有流路打开到其在 0 m 处的指定值。
- `Negative` — 滑阀位置冻结在负位置，将 **Negative spool position open connections** 参数指定的流路打开到其最大值。由 **Positive spool position open connections** 和 **Neutral spool position open connections** 参数指定的流路关闭。
- `Maintain last value` — 触发发生时，阀门冻结在当时的滑阀位置。

由于阀门面积极值处的数值平滑，在线性参数化中，模块使用的最小面积大于 **Leakage area**，最大面积小于 **Maximum orifice area**，其比例与 **Smoothing factor** 值成比例。有关详细信息，请参阅数值平滑。

故障触发后，在仿真的其余时间内，阀门保持在故障时的面积。

### 复合结构

此模块是一个复合组件，包含 Orifice (IL) 模块的多个实例。有关阀门参数化和模块计算的更多详细信息，请参阅 Orifice (IL) 模块。

### 预定义参数化

您可以使用预参数化的制造数据填充模块，从而对特定供应商组件建模。

要加载预定义参数化：

1. 在模块对话框中，**Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的 "<click to select>" 超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。模块现在具有您指定的参数化。
4. 您可以选择一个部件并查看 **Compare selected part with block** 部分中的数据，从而在 Block Parameterization Manager 窗口中将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。模块对缺失数据使用工程判断和简化假设。因此，仿真行为与实际物理行为之间可能会出现一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要改进组件模型。

要了解更多信息，请参阅预参数化组件列表。
