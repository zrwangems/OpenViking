---
type: simulink-block
title: '4-Way 3-Position Directional Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way3positiondirectionalvalvetl'
documentation_source_path: 'ref/4way3positiondirectionalvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 3-Position Directional Valve (TL)

## 端口

### 输入

### **S** — 阀芯或阀控制构件，无量纲物理信号

阀控制构件的瞬时位移。
### 守恒

### **P** — 流动通道热液体

流体可以进入或离开阀的开口。该端口通常连接到流体供应管路。

### **T** — 流动通道热液体

流体可以进入或离开阀的开口。该端口通常连接到流体回流管路。

### **A** — 流动通道热液体

流体可以进入或离开阀的开口。该端口通常连接到执行管路。

### **B** — 流动通道热液体

流体可以进入或离开阀的开口。该端口通常连接到执行管路。

## 参数

### 阀配置

### **正阀芯位置开启连接** — 当阀芯处于正位置时打开的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯处于正位置时打开的流路。该参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置与其他节流口的一致性，请将 **中性阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error`。

### **中性阀芯位置开启连接** — 当阀芯处于中性位置时打开的流路 `All closed`（默认）| `P-A, P-B, A-T, B-T` | `A-T, B-T` | `P-A, A-T` | `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-B, B-T` | `A-T` | `B-T` | `P-A` | `P-B` | `P-T` | `P-A, A-T, P-T` | `P-A, P-B, A-B` | `P-B, B-T, P-T` | `P-A, P-B, A-T, B-T, P-T`

当阀芯处于中性位置时打开的流路。该参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置与其他节流口的一致性，请将 **中性阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error`。

### **负阀芯位置开启连接** — 当阀芯沿负方向运动时打开的流路 `P-A, B-T`（默认）| `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯沿负方向运动时打开的流路。该参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置与其他节流口的一致性，请将 **中性阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error`。

### **中性阀芯位置开启连接的一致性检查** — 是否检查节流口设置是否与指定的最大节流口开度阀芯位置一致 `Warning`（默认）| `Error` | `None`

是否检查 **阀配置** 选项卡上的中性阀芯位置开启设置是否与最大节流口面积处指定的阀芯位置一致。对于每个启用的节流口，阀芯中性位置处的实际偏移应与每个单独节流口指定的阀芯偏移相匹配。

### 模型参数化

### **面积特性** — 节流口的流量方程 `所有流路相同`（默认）| `每条流路不同`

为阀口面积应用统一或单独的流量方程。`所有流路相同` 对所有阀口使用相同的节流口和阀芯几何尺寸、流量、压力和面积向量。使用 `每条流路不同` 时，这些参数针对每个节流口单独指定。在两种情况下，所有节流口在 `线性 - 面积与阀芯行程的关系` 和 `表格数据 - 面积与阀芯行程的关系` 参数化中具有相同的横截面积、流量系数和雷诺数。相同的 **节流口参数化** 应用于所有流路。

### **节流口参数化** — 计算开口面积的方法 `线性 - 面积与阀芯行程的关系`（默认）| `表格数据 - 面积与阀芯行程的关系` | `表格数据 - 体积流量与阀芯行程和压降的关系` | `表格数据 - 质量流量与阀芯行程和压降的关系`

计算阀开口面积的方法。在表格数据参数化中，您可以为非线性阀开口轮廓提供自己的阀面积和阀芯行程数据，或者可以提供以体积流量、阀芯行程和流路压降表示的数据。

### **节流口关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `线性 - 面积与阀芯行程的关系`。

### **最大节流口面积** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀操作期间每个节流口的最大开口面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `线性 - 面积与阀芯行程的关系`。

### **泄漏面积** — 节流口完全关闭时的开口面积 `1e-9 m^2`（默认）| 正标量

节流口完全关闭时的开口面积。任何小于此值的面积都保持为指定的泄漏面积。此参数通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **节流口参数化** 设置为 `线性 - 面积与阀芯行程的关系`。

### **阀芯行程向量** — 相对于完全关闭位置的阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格参数化的阀芯行程距离向量。向量元素必须与 **节流口面积向量** 参数中的元素一一对应。这些值按升序列出，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 面积与阀芯行程的关系`。

### **节流口面积向量** — 阀开口面积向量 `[1e-09, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀开口面积表格参数化的开口面积向量。向量元素必须与 **阀芯行程向量** 参数中的元素一一对应。这些元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `所有流路相同`，并将 **节流口参数化** 设置为 `表格数据 - 面积与阀芯行程的关系`。

### **Spool travel vector, ds** — 阀芯开口距离相对于全关位置的向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **Pressure drop vector, dp** 参数共同构成二维因变量 **Volumetric flow rate table, q(ds,dp)** 或 **Mass flow rate table, mdot(ds,dp)** 参数的独立轴。这些值按升序排列，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Pressure drop vector, dp** — 阀门压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **Spool travel vector, ds** 参数共同构成二维因变量 **Volumetric flow rate table, q(ds,dp)** 或 **Mass flow rate table, mdot(ds,dp)** 参数的独立轴。这些值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Volumetric flow rate table, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中向量元素的个数。
- *N* 是 **Pressure drop vector, dp** 参数中向量元素的个数。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Mass flow rate table, mdot(ds,dp)** — 质量流量 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中向量元素的个数。
- *N* 是 **Pressure drop vector, dp** 参数中向量元素的个数。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Constant orifice area** — 相同流路的节流孔面积 `1e-4 m^2`（默认）| 正标量

当正、中、负阀芯位置具有相同节流孔时的节流孔面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为以下之一：

- `Linear - Area vs. spool travel`。
- `Tabulated data - Area vs. spool travel`

必须在以下三个 **Valve Configuration** 参数中选择相同的节流孔：

- **Positive spool position open connections**
- **Neutral spool position open connections**
- **Negative spool position open connections**

### **Constant orifice pressure drop vector** — 相同流路压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中、负阀芯位置具有相同节流口时，阀门上的压差值向量。向量元素与 **Constant orifice volumetric flow rate vector** 或 **Constant orifice mass flow rate table, mdot(ds,dp)** 参数中的元素一一对应。数值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

必须在以下三个 **Valve Configuration** 参数中选择相同的节流口：

- **Positive spool position open connections**
- **Neutral spool position open connections**
- **Negative spool position open connections**

### **Constant orifice volumetric flow rate vector** — 相同流路的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中、负阀芯位置使用相同节流口时，恒定节流口的体积流量值向量。向量元素与 **Constant orifice pressure drop vector** 参数中的元素一一对应。数值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

必须在以下三个 **Valve Configuration** 参数中选择相同的节流口：

- **Positive spool position open connections**
- **Neutral spool position open connections**
- **Negative spool position open connections**

### **Constant orifice mass flow rate vector** — 恒定节流口质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正、中、负阀芯位置使用相同节流口时，阀门上的质量流量值向量。向量元素与 **Constant orifice pressure drop vector** 参数中的元素一一对应。数值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

必须在以下三个 **Valve Configuration** 参数中选择相同的节流口：

- **Positive spool position open connections**
- **Neutral spool position open connections**
- **Negative spool position open connections**

### **Reference inflow temperature** — 指定质量流量数据时的温度 `293.15 K`（默认）| 正标量

指定表格化质量流量数据时的温度。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Reference inflow pressure** — 指定质量流量表格数据时的压力 `0.101325 MPa`（默认）| 正标量

指定表格化质量流量数据时的压力。该模块使用此参数计算第三个参考参数，即参考密度。它使用该参考值来缩放表格化压降数据，以适应偏离参考条件的压力和温度。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **Cross-sectional area at ports P, T, A and B** — 守恒端口处的面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，用于确定通过阀门的质量流量的压力-流量方程以及能量流率平滑。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

修正系数，用于考虑理论流动中的排放损失。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为以下之一：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀门处于接近打开和接近关闭位置时，基于流量响应引入一层渐变变化。为提高这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Pressure recovery** — 是否考虑面积扩大时的压力升高 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力升高。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### P-A Orifice

### **Spool position at maximum P-A orifice area** — 完全打开 P-A 孔口时的阀芯偏移 `7.5e-3 m`（默认）| 正标量

完全打开 P-A 孔口时阀芯从中位开始的偏移量。如果为此阀芯位置设置的值与其他孔口阀芯位置不一致或不符合物理规律，**Consistency check for neutral spool position open connections** 参数将通知您。

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

**注意：**

仅当 P-A 孔口设置未同时出现在以下三个阀芯位置参数中时，此参数才启用：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **P-A spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回不符合物理规律的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

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

### **P-A maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 P-A 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

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

### **P-A orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门开口面积表格化参数化的开口面积向量。向量元素必须与 **P-A spool travel vector** 参数中的元素一一对应。
元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

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

### **P-A orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **P-A orifice pressure drop vector, dp** 参数构成独立轴，用于二维因变量 **P-A orifice volumetric flow rate table, q(ds,dp)** 或 **P-A orifice mass flow rate table, mdot(ds,dp)** 参数。值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

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

### **P-A 节流口压降向量，dp** — 压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格参数化的压降值向量。压降向量与 **P-A 节流口阀芯行程向量，ds** 参数一起构成独立轴，用于二维因变量 **P-A 节流口体积流量表，q(ds,dp)** 或 **P-A 节流口质量流量表，mdot(ds,dp)** 参数。这些值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

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

### **P-A 节流口体积流量表，q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A 节流口阀芯行程向量，ds** 参数中向量元素的数量。
- *N* 是 **P-A 节流口压降向量，dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

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

### **P-A orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和滑阀行程距离独立值的 *M*×*N* 质量流量矩阵。
*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A orifice spool travel vector,
  ds** 参数中向量元素的数量。
- *N* 是 **P-A orifice pressure drop vector,
  dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

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

### **P-A constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正、中和负滑阀位置使用相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - Area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的以下设置之一：

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

### **P-A constant orifice pressure drop vector** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中和负滑阀位置使用相同节流口时，阀门上的压差值向量。
向量元素与 **P-A constant orifice volumetric flow rate
vector** 或 **P-A orifice mass flow rate table,
mdot(ds,dp)** 参数中的元素一一对应。值按升序排列。
表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

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

### **P-A constant orifice volumetric flow rate vector** — 恒定节流孔体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中、负阀芯位置使用相同节流孔时，通过阀的体积流量值向量。向量元素与 **P-A constant orifice pressure drop vector** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 每个参数中的以下设置之一：

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

### **P-A constant orifice mass flow rate vector** — 恒定节流孔质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正、中、负阀芯位置使用相同节流孔时，通过阀的质量流量值向量。向量元素与 **P-A constant orifice pressure drop vector** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

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

### P-B Orifice

### **Spool position at maximum P-B orifice area** — P-B 节流孔完全打开时阀芯偏离中位的位置 `7.5e-3 m`（默认）| 正标量

P-B 节流孔完全打开时阀芯偏离中位的位置。**Consistency check for neutral spool position open connections** 参数将根据其他节流孔阀芯位置通知您为此阀芯位置设置的值是否不一致或不符合物理规律。

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

**注意：**

仅当 P-B 节流孔设置未同时出现在所有三个阀芯位置参数中时，此参数才启用：**Positive spool position
open connections**、**Neutral spool
position open connections** 和 **Negative spool position open
connections**。

### **P-B 阀芯在关闭与打开节流口之间的行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值对计算设置上限，以避免仿真返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 最大节流口面积** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门工作期间 P-B 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 节流口阀芯行程向量** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **P-B 节流口面积向量**参数中的元素一一对应。
这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 节流口面积向量** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门开口面积表格化参数化的开口面积向量。向量元素必须与 **P-B 阀芯行程向量**参数中的元素一一对应。
这些元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

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

### **P-B orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **P-B orifice pressure drop vector, dp** 参数构成独立轴，用于二维因变量 **P-B orifice volumetric flow rate table, q(ds,dp)** 或 **P-B orifice mass flow rate table, mdot(ds,dp)** 参数。这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

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

### **P-B orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **P-B orifice spool travel vector, ds** 参数构成独立轴，用于二维因变量 **P-B orifice volumetric flow rate table, q(ds,dp)** 或 **P-B orifice mass flow rate table, mdot(ds,dp)** 参数。这些值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为
   `每条流各不相同
   path`。
2. **Orifice parameterization** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

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

### **P-B orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **P-B orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程独立值的 *M*×*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **P-B orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正、中和负阀芯位置使用相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - Area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B constant orifice pressure drop vector** — 恒定节流口压降向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中、负阀芯位置使用同一节流口时，阀门上的压差值的向量。向量元素与 **P-B constant orifice volumetric flow rate vector** 或 **P-B orifice mass flow rate table, mdot(ds,dp)** 参数中的元素一一对应。这些值按升序排列。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 在每个参数中设置以下之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B constant orifice volumetric flow rate vector** — 恒定节流口体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中、负阀芯位置使用同一节流口时，阀门上的体积流量值的向量。向量元素与 **P-B constant orifice pressure drop vector** 参数中的元素一一对应。这些值按升序排列。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 在每个参数中设置以下之一：

   **Positive spool position open connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-B`

### **P-B constant orifice mass flow rate vector** — 恒定节流口质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正、中、负阀芯位置使用同一节流口时，阀门上的质量流量值的向量。向量元素与 **P-B constant orifice pressure drop vector** 参数中的元素一一对应。这些值按升序排列。在表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### A-B 节流口

### **A-B 节流口最大面积处的阀芯位置** — 完全打开 A-B 节流口时阀芯偏离中位的偏移量 `7.5e-3 m`（默认）| 正标量

完全打开 A-B 节流口时阀芯偏离中位的偏移量。
**中位阀芯位置开启连接一致性检查**参数将根据其他节流口阀芯位置通知您，为此阀芯位置设置的值是否不一致或不符合物理规律。

#### 依赖项

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接**为：

- `P-A, P-B, A-B`

**中位阀芯位置开启连接**为：

- `P-A, P-B, A-B`

**负阀芯位置开启连接**为：

- `P-A, P-B, A-B`

**注意：**

仅当 P-A 节流口设置未同时出现在以下三个阀芯位置参数中时，此参数才启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **A-B 节流口关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以避免仿真返回不符合物理规律的值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

### **A-B 最大节流口面积** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 A-B 节流口的最大开口面积。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

### **A-B 节流口阀芯行程向量** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格参数化的阀芯行程距离向量。向量元素必须与 **A-B 节流口面积向量**参数中的元素一一对应。
这些值按升序排列，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

### **A-B orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门开口面积表格化参数化的开口面积向量。向量元素必须与 **A-B spool travel vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

### **A-B orifice spool travel vector, ds** — 相对于全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **A-B orifice pressure drop vector, dp** 参数构成独立轴。值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

### **A-B orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **A-B orifice spool travel vector, ds** 参数构成独立轴，用于二维因变量 **A-B orifice volumetric flow rate table, q(ds,dp)** 或 **A-B orifice mass flow rate table, mdot(ds,dp)** 参数。值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

### **A-B orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*-by-*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*-by-*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-B orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **A-B orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*-by-*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*-by-*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-B orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **A-B orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B constant orifice area** — 恒定孔口的横截面积 `1e-4 m^2`（默认）| 正标量

当正、中和负阀芯位置使用相同孔口时的孔口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   **Positive spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-B`

   **Negative spool position open connections** 为：

   - `P-A, P-B, A-B`

### **A-B constant orifice pressure drop vector** — 恒定孔口的压差向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* 向量

当正、中和负阀芯位置使用相同孔口时，阀门上的压差值向量。向量元素与 **A-B constant orifice volumetric flow rate vector** 或 **A-B orifice mass flow rate table, mdot(ds,dp)** 参数中的元素一一对应。这些值按升序列出。在表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

### **A-B constant orifice volumetric flow rate vector** — 恒定节流口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中位和负阀芯位置使用相同节流口时，通过阀门的体积流量值向量。向量元素与 **A-B constant orifice pressure drop vector** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

### **A-B constant orifice mass flow rate vector** — 恒定节流口质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正、中位和负阀芯位置使用相同节流口时，通过阀门的质量流量值向量。向量元素与 **A-B constant orifice pressure drop vector** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接**为：

   - `P-A, P-B,
     A-B`

### A-T 节流口

### **Spool position at maximum A-T orifice area** — 完全打开 A-T 节流口时阀芯从中位偏移量 `7.5e-3 m`（默认）| 正标量

完全打开 A-T 节流口时阀芯从中位的偏移量。**Consistency check for neutral spool position open connections** 参数将根据其他节流口阀芯位置通知您为此阀芯位置设置的值是否不一致或不符合物理规律。

#### 依赖项

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接**为 `P-B,
  A-T`。
- **中位阀芯位置开启连接**为：

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
- **负阀芯位置开启连接**为 `P-B,
  A-T`。

**注意：**

仅当 A-T 节流口设置未同时出现在以下三个阀芯位置参数中时，此参数才启用：**Positive spool position
open connections**、**Neutral spool
position open connections** 和 **Negative spool position open
connections**。

### **A-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以避免仿真返回不符合物理规律的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-B,
   A-T`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-B,
   A-T`。

### **A-T maximum orifice area** — 最大节流口开口面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 A-T 节流口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-B,
   A-T`

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-B,
   A-T`。

### **A-T orifice spool travel vector** — 相对于全关位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀门面积表格化参数化的阀芯行程距离向量。向量元素必须与 **A-T orifice area vector** 参数中的元素一一对应。
这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-B,
   A-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-B,
   A-T`。

### **A-T orifice area vector** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门开口面积表格化参数化的开口面积向量。向量元素必须与 **A-T spool travel vector** 参数中的元素一一对应。
这些元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-B,
   A-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-B,
   A-T`。

### **A-T orifice spool travel vector, ds** — 阀芯开口距离相对于完全关闭位置的向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **A-T orifice pressure drop vector, dp** 参数共同构成独立轴，用于二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 或 **A-T orifice mass flow rate table, mdot(ds,dp)** 参数。这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-B, A-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为 `P-B, A-T`。

### **A-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **A-T orifice spool travel vector, ds** 参数共同构成独立轴，用于二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 或 **A-T orifice mass flow rate table, mdot(ds,dp)** 参数。这些值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-B, A-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为 `P-B, A-T`。

### **A-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **A-T orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-B, A-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为 `P-B, A-T`。

### **A-T orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和滑阀行程距离独立值的 *M*×*N* 质量流量矩阵。
*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **A-T orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   **Positive spool position open connections** 为 `P-B, A-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为 `P-B, A-T`。

### **A-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正、中和负滑阀位置使用相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为以下之一：

   - `Linear - Area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为 `P-B, A-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为 `P-B, A-T`。

### **A-T constant orifice pressure drop vector** — 恒定节流口的压差向量值 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中和负滑阀位置使用相同节流口时，阀门上的压差向量。
向量元素与 **A-T constant orifice volumetric flow rate vector** 或 **A-T orifice mass flow rate table, mdot(ds,dp)** 参数中的元素一一对应。值按升序列出。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **Positive spool position open connections** 为 `P-B, A-T`。

   **Neutral spool position open connections** 为：

   - `P-A, P-B, A-T, B-T`
   - `P-B, A-T`
   - `A-T, B-T`
   - `P-A, A-T`
   - `A-T`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **Negative spool position open connections** 为 `P-B, A-T`。

### **A-T constant orifice volumetric flow rate vector** — 恒定节流口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中和负滑阀位置使用相同节流口时的体积流量值向量。向量元素与 **A-T constant orifice pressure drop vector** 参数中的元素一一对应。值按升序列出。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**为 `P-B,
   A-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-B,
   A-T`。

### **A-T constant orifice mass flow rate vector** — 恒定节流口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正、中、负阀芯位置使用同一节流口时，通过阀门的质量流量值向量。向量元素与 **A-T constant orifice pressure drop vector** 参数中的元素一一对应。数值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 在每个参数中设置以下之一：

   **正阀芯位置开启连接**为 `P-B,
   A-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-B,
   A-T`。

### B-T 节流口

### **Spool position at maximum B-T orifice area** — B-T 节流口完全开启时的阀芯偏离中位位置的偏移量 `7.5e-3 m`（默认）| 正标量

B-T 节流口完全开启时阀芯偏离中位位置的偏移量。**Consistency check for neutral spool position open connections** 参数将根据其他节流口阀芯位置通知您为此阀芯位置设置的值是否不一致或不符合物理规律。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接**为 `P-A,
  B-T`。
- **中位阀芯位置开启连接**为：

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
- **负阀芯位置开启连接**为 `P-A,
  B-T`。

**注意：**

仅当 B-T 节流口设置未同时出现在以下三个阀芯位置参数中时，此参数才会启用：**正阀芯位置开启连接**、**中位阀芯位置开启连接**和**负阀芯位置开启连接**。

### **B-T spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。此值为计算提供上限，以确保仿真不会返回不符合物理规律的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认）| 正标量

阀门运行期间 B-T 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T orifice spool travel vector** — 相对于全关位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。向量元素必须与 **B-T orifice area vector** 参数中的元素一一对应。这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T orifice area vector** — 阀口开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀口开启面积表格化参数化的开启面积向量。向量元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。这些元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T orifice spool travel vector, ds** — 相对于全关位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的控制构件行程距离向量。阀芯行程向量与 **B-T orifice pressure drop vector, dp** 参数构成独立轴，用于二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 或 **B-T orifice mass flow rate table, mdot(ds,dp)** 参数。这些值按升序列出，且第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T 节流孔压降向量，dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **B-T 节流孔阀芯行程向量，ds** 参数构成独立轴，用于二维因变量 **B-T 节流孔体积流量表，q(ds,dp)** 或 **B-T 节流孔质量流量表，mdot(ds,dp)** 参数。这些值按升序排列，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T 节流孔体积流量表，q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **B-T 节流孔阀芯行程向量，ds** 参数中向量元素的数量。
- *N* 是 **B-T 节流孔压降向量，dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   **正阀芯位置开启连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启连接**为：

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

   **负阀芯位置开启连接**为 `P-A,
   B-T`。

### **B-T 节流孔质量流量表，mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **B-T 节流孔阀芯行程向量，ds** 参数中向量元素的数量。
- *N* 是 **B-T 节流孔压降向量，dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   **正阀芯位置开启
   连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启
   连接**为：

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

   **负阀芯位置开启
   连接**为 `P-A,
   B-T`。

### **B-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| 正标量

当正、中位和负阀芯位置使用同一节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为以下之一：

   - `Linear - Area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的以下设置之一：

   **正阀芯位置开启
   连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启
   连接**为：

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

   **负阀芯位置开启
   连接**为 `P-A,
   B-T`。

### **B-T constant orifice pressure drop vector** — 恒定节流口的压差向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

当正、中位和负阀芯位置使用同一节流口时，阀门上的压差值向量。
向量元素与 **B-T constant orifice volumetric flow rate
vector** 或 **B-T orifice mass flow rate table,
mdot(ds,dp)** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   **正阀芯位置开启
   连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启
   连接**为：

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

   **负阀芯位置开启
   连接**为 `P-A,
   B-T`。

### **B-T constant orifice volumetric flow rate vector** — 恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1×*n* 向量

当正、中位和负阀芯位置使用同一节流口时，阀门上的体积流量值向量。
向量元素与 **B-T constant orifice pressure drop vector**
参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流口参数化**为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 每个参数中的以下设置之一：

   **正阀芯位置开启
   连接**为 `P-A,
   B-T`。

   **中位阀芯位置开启
   连接**为：

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

   **负阀芯位置开启
   连接**为 `P-A,
   B-T`。

### **B-T 恒定孔口质量流量向量** — 恒定孔口质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1×*n* 向量

当正、中、负阀芯位置使用同一孔口时，流经阀的质量流量值向量。向量元素与 **P-B 恒定孔口压降向量** 参数中的元素一一对应。这些值按升序排列。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为 `每条流各不相同 path`。
2. **孔口参数化** 为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 每个参数中的一项设置：

   **正阀芯位置开启连接** 为 `P-A, B-T`。

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B, A-T, B-T`
   - `A-T, B-T`
   - `P-A, B-T`
   - `P-B, B-T`
   - `B-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

   **负阀芯位置开启连接** 为 `P-A, B-T`。

### P-T 孔口

### **最大 P-T 孔口面积处的阀芯位置** — P-T 孔口完全打开时阀芯偏离中位的偏移量 `0 m`（默认）| 正标量

P-T 孔口完全打开时阀芯偏离中位的偏移量。**中位阀芯位置开启连接一致性检查** 参数将根据其他孔口阀芯位置通知您，为此阀芯位置设置的值是否不一致或不符合物理规律。

#### 依赖关系

要启用此参数，请将 **中位阀芯位置开启连接** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

阀芯行程的最大距离。该值为计算提供上限，以避免仿真返回不符合物理规律的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为 `每条流各不相同 path`。
2. **孔口参数化** 为 `Linear - Area vs. spool travel`。
3. **中位阀芯位置开启连接** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 最大孔口面积** — 最大孔口开口面积 `1e-4 m^2`（默认）| 正标量

阀门工作期间 P-T 孔口的最大开口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为 `每条流各不相同 path`。
2. **孔口参数化** 为 `Linear - Area vs. spool travel`。
3. **中位阀芯位置开启连接** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T 孔口阀芯行程向量** — 相对于完全关闭位置的阀芯开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于阀面积表格参数化的控制构件行程距离向量。向量元素必须与 **P-T 孔口面积向量** 参数中的元素一一对应。这些值按升序排列，且第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为 `每条流各不相同 path`。
2. **孔口参数化** 为 `Tabulated data - Area vs. spool travel`。
3. **中位阀芯位置开启连接** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice spool travel vector, ds** — 阀芯开口距离相对于全闭位置的向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格化参数化的控制构件行程距离向量。阀芯行程向量与 **P-T orifice pressure drop vector, dp** 参数构成独立轴，用于二维因变量 **P-T orifice volumetric flow rate table, q(ds,dp)** 或 **P-T orifice mass flow rate table, mdot(ds,dp)** 参数。值按升序列出，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **P-T orifice spool travel vector, ds** 参数构成独立轴，用于二维因变量 **P-T orifice volumetric flow rate table, q(ds,dp)** 或 **P-T orifice mass flow rate table, mdot(ds,dp)** 参数。值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-T orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **P-T orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **Area characteristics** 为 `每条流各不相同 path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-T orifice pressure drop vector, dp** 参数中向量元素的数量。
- *N* 是 **P-T orifice spool travel vector, ds** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性**为
   `每条流各不相同
   path`。
2. **节流孔参数化**为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. **中位阀芯位置开启
   连接**为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### 故障

### **4-Way 3-Position Directional Valve Area fault** — 用于对阀面积故障建模的选项 `Add fault`

用于在模块中对阀面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。当故障发生时，通常由开度参数化设置的阀面积将根据 **Spool position when faulted** 参数中指定的值进行设置。

### **Spool position when faulted** — 故障时的阀特性 `Positive`（默认）| `Neutral` | `Negative` | `Maintain last value`

故障时的阀芯位置。您可以选择阀在阀芯处于正位置、负位置或故障触发时所处位置时卡滞。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

4-Way 3-Position Directional Valve (TL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2022b：右键点击模块以查看开度特性图

您可以通过右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**，查看每个节流孔的面积或体积流量相对于阀芯位置的图。

## 描述

用于在热液体网络中的四条管路交汇处引导流量的阀

4-Way 3-Position Directional Valve (TL) 模块对热液体网络中具有四个开口的阀进行建模，通常位于执行器、泵与油箱之间。阀的操作由单个阀芯控制，该阀芯根据端口 **S** 处的信号而位移。您可以通过在 **Neutral spool position open connections** 参数中指定当阀芯处于中位（以 0 m 为中心）时打开的节流孔，在 **Positive spool position open connections** 参数中指定当阀芯向正方向移动时打开的节流孔，以及在 **Negative spool position open connections** 参数中指定当阀芯向负方向移动时打开的节流孔，来设置阀的基线配置。

您可以在 **Orifice parameterization** 参数中将阀开度的模型设置为线性关系或用户提供数据的函数，该模型可应用于阀中的一个或所有流路。

**阀设置示例**

在此示例配置中，**Neutral spool position open connections** 设置为 `All closed`。当阀芯处于中位时，所有节流孔都关闭，不导通流量：

在此配置中，**Negative spool position open connections** 设置为 `P-A, B-T`。当端口 **S** 处的信号使阀芯移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径打开，允许流量通过。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径关闭，不导通流量：

在此配置中，**Positive spool position open connections** 设置为 `P-B, A-T`。当端口 **S** 处的信号使阀芯移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径打开，允许流量通过，而端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径关闭：

在示意图中，此配置表示为：

左侧对应正位置，右侧对应负位置。

### 滑阀位移与阀配置

*滑阀行程*是节流口从关闭位置到完全打开所需的滑阀移动量，并且针对在**阀配置**选项卡上选择的每个节流口进行定义。下表显示了如何根据阀节流口参数化和流路特性计算行程。

在端口 **S** 处发出信号的滑阀移动方向取决于滑阀行程和节流口方向：

**节流口定义与滑阀移动方向**

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

其中 *S*orifice\_max 是为每个节流口定义的最大节流口面积处的滑阀位置。当 *ΔS* 为负时，节流口面积饱和为泄漏面积；当节流口完全打开时，节流口面积饱和为最大节流口面积。当节流口完全打开时，*ΔS* 等于滑阀行程，因此 *ΔS* 大于滑阀行程不会进一步增加节流口面积。

**中性滑阀位置打开连接的一致性检查**参数验证

- 在**中性滑阀位置打开连接**中列出的任何节流口在 **S** 处信号为 0 时均打开。
- 未在**中性滑阀位置打开连接**中列出的任何节流口在 **S** 处信号为 0 时均关闭。

您可以选择在此检查被违反时接收警告或错误。

4-Way 3-Position Directional Valve (TL) 模块的可能配置如下所示。

**4-Way 3-Position Directional Valve 配置**

| 配置 | 参数值 |
| --- | --- |
|  | 在中位时四个节流口全部关闭。（默认）  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时四个节流口全部开启。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-A, P-B, A-T, B-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < B-T 阀芯行程 |
|  | 节流口 A-T 和 B-T 关闭。节流口 P-A 和 P-B 有重叠。  - **正阀芯位置开启连接**：`P-A` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-B`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 |
|  | 节流口 A-T 和 B-T 开启。节流口 P-A 和 P-B 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`A-T, B-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < B-T 阀芯行程 |
|  | 在中位时节流口 P-A 和 A-T 开启。节流口 P-B 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`P-A, A-T` - **负阀芯位置开启连接**：`P-A, B-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < –B-T 阀芯行程 |
|  | 在中位时节流口 A-T 开启。节流口 P-B、A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`A-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 B-T 开启。节流口 P-A、P-B 和 A-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`B-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < B-T 阀芯行程 |
|  | 节流口 P-A、P-B 开启。节流口 A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-A, P-B` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 P-A 开启。节流口 P-B、A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-A` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 P-B 开启。节流口 P-A、A-T 和 B-T 有重叠。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-B` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 |
|  | 在中位时节流口 P-B 和 B-T 开启。节流口 P-A 和 A-T 有重叠。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`P-B, B-T` - **负阀芯位置开启连接**：`P-A, B-T`    - **P-A 节流口最大面积处的阀芯位置** < –P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > –B-T 阀芯行程 |
|  | 在中位时节流口 P-A、P-B、A-T 和 B-T 关闭。P-T 在中位时开启，并在阀芯位移时关闭。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-T` - **负阀芯位置开启连接**：`P-B, A-T`    - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < –A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 - **P-T 节流口最大面积处的阀芯位置** = any value |
|  | 节流口 P-A 是恒定节流口。节流口 P-B、A-T 和 B-T 在中位时开启。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`P-A, P-B, A-T, B-T` - **负阀芯位置开启连接**：`P-A, B-T`    - **P-A 节流口最大面积处的阀芯位置** < P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** = any value - **B-T 节流口最大面积处的阀芯位置** > –B-T 阀芯行程 |
|  | 节流口 P-B 是恒定节流口。节流口 P-A、A-T、B-T 在中位时开启。    - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`P-A, P-B, A-T, B-T` - **负阀芯位置开启连接**：`P-A, P-B`    - **P-A 节流口最大面积处的阀芯位置** > –P-A 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** = any value |
|  | 在中位时节流口 P-A 关闭。端口 **A** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-A, B-T`  - |**P-A 节流口最大面积处的阀芯位置**| > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > P-B 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < –B-T 阀芯行程 |
|  | 在中位时节流口 P-B 关闭。端口 **B** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`All closed` - **负阀芯位置开启连接**：`P-A, P-B`  - **P-A 节流口最大面积处的阀芯位置** < –P-A 阀芯行程 - |**P-B 节流口最大面积处的阀芯位置**| > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** > A-T 阀芯行程 |
|  | 在中位时节流口 P-A 关闭。在中位时节流口 A-T 开启。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`A-T, B-T` - **负阀芯位置开启连接**：`P-A, B-T`  - |**P-A 节流口最大面积处的阀芯位置**| > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** = any value - **B-T 节流口最大面积处的阀芯位置** > –B-T 阀芯行程 |
|  | 在中位时节流口 P-B 关闭。在中位时节流口 B-T 开启。  - **正阀芯位置开启连接**：`P-B, A-T` - **中位阀芯位置开启连接**：`A-T, B-T` - **负阀芯位置开启连接**：`P-A, P-B`  - **P-A 节流口最大面积处的阀芯位置** < –P-A 阀芯行程 - |**P-B 节流口最大面积处的阀芯位置**| > P-B 阀芯行程 - **A-T 节流口最大面积处的阀芯位置** < A-T 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** = any value |
|  | 在中位时节流口 P-B 关闭。在中位时节流口 P-T 开启。端口 **A** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-A, P-B` - **中位阀芯位置开启连接**：`P-T` - **负阀芯位置开启连接**：`P-B, A-T`  - **P-A 节流口最大面积处的阀芯位置** > P-A 阀芯行程 - |**P-B 节流口最大面积处的阀芯位置**| > P-B 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** < –B-T 阀芯行程 - **P-T 节流口最大面积处的阀芯位置** = any value |
|  | 在中位时节流口 P-A 关闭。在中位时节流口 P-T 开启。端口 **A** 和 **T** 不形成流动路径。  - **正阀芯位置开启连接**：`P-A, B-T` - **中位阀芯位置开启连接**：`P-T` - **负阀芯位置开启连接**：`P-A, P-B`  - |**P-A 节流口最大面积处的阀芯位置**| > P-A 阀芯行程 - **P-B 节流口最大面积处的阀芯位置** < –P-B 阀芯行程 - **B-T 节流口最大面积处的阀芯位置** > B-T 阀芯行程 - **P-T 节流口最大面积处的阀芯位置** = any value |

### 阀门孔口参数化

**孔口参数化**参数设置通过一个或所有阀门孔口的开口面积或体积流量的模型。如果**面积特性**设置为`所有流路相同`，则该模块对所有流路应用相同的数据；否则，对于`所有流路不同`设置，将应用各自的参数化。您可以通过三种方式对阀门开度进行建模：

- `线性 - 面积与阀芯行程的关系`

  开口面积是作为端口 **S** 处信号接收的阀芯位置的线性函数：

  Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak，

  其中：

  - *ΔS* 是阀芯位移与阀门配置中定义的阀芯行程。

    当*ΔS*为负时，*Aorifice*饱和于*Aleak*；当孔口完全打开时，*Aorifice*饱和于*Amax*。当孔口完全打开时，*ΔS*等于阀芯行程，因此*ΔS*大于阀芯行程不会进一步增大孔口面积。
  - *ΔS*max 是**关闭与打开孔口之间的阀芯行程**。
  - *A*max 是**最大孔口面积**。
  - *A*leak 是**泄漏面积**。

  当阀门在线性参数化下处于接近打开或接近关闭位置时，您可以通过调整**平滑因子**参数来保持仿真中的数值鲁棒性。如果**平滑因子**参数非零，则该模块在*Aleak*和*Amax*之间平滑地饱和开口面积。有关详细信息，请参阅数值平滑。
- `表格数据 - 面积与阀芯行程的关系`

  为您的系统或端口 **P**、**A**、**B** 和 **T** 之间的各条流路提供阀芯行程向量。该数据将用于计算孔口面积与阀芯位移之间的关系。插值用于确定给定数据点之间的开口面积。*A*leak 和 *A*max 分别是开口面积向量的第一个和最后一个参数。
- `表格数据 - 体积流量与阀芯行程和压降的关系`

  提供阀芯行程和压降向量以及一个相关的二维体积流量数组。插值用于确定给定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

- `表格数据 - 质量流量与阀芯行程和压降的关系`

  直接从控制构件位置和阀门两端的压降计算质量流量。这三个变量之间的关系可以是非线性的，该模块根据**阀芯行程向量, ds**、**压降向量, dp**和**质量流量表, mdot(ds,dp)**参数中的表格数据计算该关系。

### 可视化节流口开度

要可视化阀芯偏移和最大位移，请右键点击该模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示在 **Valve Configuration** 设置中选择的节流口。节流口参数化决定了坐标轴，坐标轴可以是：

- 节流口面积与阀芯位置的关系
- 体积流量与阀芯位置的关系，在特定压差下查询
- 质量流量与阀芯位置的关系，针对参考流入温度和参考流入压力，在特定压差下查询

当 **Valve Configuration** 中的正、中性和负设置对应同一个节流口时，该图将节流口开度显示为常数。

更改模块参数后要更新数据，请点击图形窗口上的 **Reload Data**。

此图显示了一个阀门配置示例。在 **Valve Configuration** 设置中：

- **Positive spool position open connections** 为 `P-A, B-T`。
- **Neutral spool position open connections** 为 `P-T`。
- **Negative spool position open connections** 为 `P-B, A-T`。

在 **P-A Orifice** 设置中：

- **Spool position at maximum P-A orifice area** 为 `2.5e-3 m`。

所有其他阀芯位置均为默认值。

每个节流口的面积与阀芯位置关系图。

可视化结果显示，P-A 节流口在阀芯位置 `-2.53e-3` 到 `2.53e-3` m 之间打开。由于 P-A 节流口仅在阀芯向正方向位移时打开，将 **Consistency check for neutral spool and position open connections** 参数设置为 `Warning` 会返回：

`Warning: P-A orifice must be closed when the spool is in the neutral position. Adjust Spool position at maximum P-A orifice area, Neutral spool position open connections, or Consistency check for neutral spool position open connections. Right-click on the block and select Fluids > Plot Valve Characteristics to view the area or flow of each connection versus spool position.`

要解决此警告，您可以更改：

- **Spool position at maximum P-A orifice area** 为大于 0.005 m 的值。
- **Consistency check for neutral spool position open connections** 为 `None`。
- 通过将 **Neutral spool position open connections** 设置为 `P-A` 来更改阀门配置。

### 复合结构

该模块是一个复合组件，由多个 Orifice (TL) 模块实例组成。有关阀门参数化和模块计算的更多详细信息，请参阅 Orifice (TL) 模块。

### 泄漏流量

关闭阀门泄漏流量的主要目的是确保热液体网络的任何部分在任何时候都不会与模型的其余部分隔离。这种隔离部分会降低模型的数值鲁棒性，并可能减慢仿真速度或导致仿真失败。泄漏流量在实际阀门中通常存在，但在模型中，其确切值不如其为一个大于零的小数值重要。泄漏流量由 **Leakage area** 模块参数确定。

### 故障

要对故障建模，请在**故障**部分中，单击要建模的故障旁边的**添加故障**超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Simscape 故障简介。

**故障时的滑阀位置**参数有四个故障选项：

- `Positive` — 滑阀位置冻结在正位置，将**正滑阀位置开启连接**参数指定的流路打开到其最大值。**负滑阀位置开启连接**和**中位滑阀位置开启连接**参数指定的流路关闭。
- `Neutral` — 滑阀位置冻结在中位，将所有流路打开到其在 0 m 处的指定值。
- `Negative` — 滑阀位置冻结在负位置，将**负滑阀位置开启连接**参数指定的流路打开到其最大值。**正滑阀位置开启连接**和**中位滑阀位置开启连接**参数指定的流路关闭。
- `Maintain last value` — 触发发生时，阀冻结在当时的滑阀位置。

由于阀面积极值处的数值平滑，在线性参数化中，模块使用的最小面积大于**泄漏面积**，最大面积小于**最大孔口面积**，其比例与**平滑因子**值成正比。有关更多信息，请参阅数值平滑。

故障触发后，阀在仿真的剩余时间内保持在故障面积处。

### 预定义参数化

您可以使用预参数化的制造数据填充模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，单击**选定部件**旁边的“<click to select>”超链接。
2. 打开“模块参数化管理器”窗口。从菜单中选择一个部件，然后单击**全部应用**。您可以使用**制造商**下拉菜单缩小选择范围。
3. 您可以关闭**模块参数化管理器**菜单。模块现在具有您指定的参数化。
4. 您可以通过在“模块参数化管理器”窗口中选择一个部件并查看**比较选定部件与模块**部分中的数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。模块对缺失数据使用工程判断和简化假设进行替代。因此，预期仿真行为与实际物理行为之间会存在一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅预参数化组件列表。
