---
type: simulink-block
title: '4-Way 2-Position Directional Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '4way2positiondirectionalvalveil'
documentation_source_path: 'ref/4way2positiondirectionalvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Way 2-Position Directional Valve (IL)

## 端口

### 守恒端口

### **A** — 入口或出口端口 isothermal liquid

通往阀的液体入口或出口端口。

### **B** — 入口或出口端口 isothermal liquid

通往阀的液体入口或出口端口。

### **P** — 入口或出口端口 isothermal liquid

通往阀的液体入口或出口端口。

### **T** — 入口或出口端口 isothermal liquid

通往阀的液体入口或出口端口。
### 输入

### **S** — 阀芯位移，m physical signal

与阀芯位移关联的 physical signal，单位为 m。

## 参数

### 阀配置

### **Positive spool position open connections** — 当阀芯处于正位置时开启的流路 `P-A, B-T`（默认） | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

当阀芯处于正位置时开启的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯移动方向。

### **Negative spool position open connections** — 当阀芯沿负方向移动时开启的流路 `P-B, A-T`（默认） | `P-A, B-T` | `P-A, P-B` | `P-A` | `P-B` | `P-A, P-B, A-T, B-T`

当阀芯沿负方向移动时开启的流路。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯移动方向。

### 模型参数化

### **Area characteristics** — 节流口的流量方程 `Identical for all flow paths`（默认） | `Different for each flow path`

是否对阀节流口面积应用统一的或各自的流量方程。当将此参数设置为 `Identical for all flow paths` 时，模块对所有阀节流口使用相同的节流口和阀芯几何、流量、压力和面积向量。当将此参数设置为 `Different for each flow path` 时，可以为每个节流口单独指定这些参数。对于这两种设置，当将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel` 或 `Tabulated data - Area vs. spool travel` 时，节流口 **A**、**B**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。

### **Orifice parameterization** — 计算开启面积的方法 `Linear area vs. spool travel`（默认） | `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

计算阀开启面积的方法。如果将此参数设置为一种表格数据参数化，则可以提供自己的阀面积和阀芯位移数据以描述非线性阀开启特性曲线，或者提供以体积流量、阀芯位移和流路上的压降表示的数据。

### **Spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

阀芯位移的最大距离。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认） | positive scalar

阀运行期间每个节流口的最大开启面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Leakage area** — 节流口完全关闭时的开启面积 `1e-10 m^2`（默认） | positive scalar

节流口完全关闭时的开启面积。模块将任何小于此值的面积保持为指定的泄漏面积。此参数通过保持流量连续性来提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。

### **Spool travel vector** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

根据表格化阀面积数据对节流口进行参数化时的阀芯位移距离向量。向量元素必须与 **Orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Orifice area vector** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

根据表格化阀面积数据对节流口进行参数化时的开启面积向量。向量元素必须与 **Spool travel vector** 参数中的元素一一对应。按升序列出值。元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。

### **Spool travel vector, ds** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

根据表格化体积流量数据对节流口进行参数化时的阀芯位移距离向量。阀芯位移向量与 **Pressure drop vector, dp** 参数构成独立轴，用于二维因变量 **Volumetric flow rate table, q(ds,dp)** 参数。按升序列出值。第一个元素必须为 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Pressure drop vector, dp** — 阀压降值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

根据表格化流量数据对节流口进行参数化时的压降值向量。压降向量与 **Spool travel vector, ds** 参数构成独立轴，用于二维因变量 **Volumetric flow rate table, q(ds,dp)** 参数。按升序列出值。值必须大于 0。模块在表格数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Volumetric flow rate table, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*-by-*N* matrix

基于压降和阀芯位移距离独立值的 *M*-by-*N* matrix 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **Spool travel vector, ds** 参数中向量元素的个数。
- *N* 是 **Pressure drop vector, dp** 参数中向量元素的个数。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **Constant orifice area** — 相同流路的节流口面积 `1e-4 m^2`（默认） | positive scalar

当正阀芯位置和负阀芯位置包含同一个节流口时的节流口面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为以下之一：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

在 **阀配置** 部分中为以下两个参数选择同一个节流口：

- **Positive spool position open connections**
- **Negative spool position open connections**

### **Constant orifice pressure drop vector** — 相同流路的压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

当正阀芯位置和负阀芯位置包含同一个节流口时，阀上的压差值向量。向量元素与 **Constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出值。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

在 **阀配置** 部分中为以下两个参数选择同一个节流口：

- **Positive spool position open connections**
- **Negative spool position open connections**

### **Constant orifice volumetric flow rate vector** — 相同流路的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* vector

当正阀芯位置和负阀芯位置包含同一个节流口时，恒定节流口的体积流量值向量。向量元素与 **Constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出值。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

在 **阀配置** 部分中为以下两个参数选择同一个节流口：

- **Positive spool position open connections**
- **Negative spool position open connections**

### **Cross-sectional area at ports P, T, A and B** — 守恒端口处的面积 `inf m^2`（默认） | positive scalar

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，模块在确定通过阀的质量流量的压力-流量方程中使用该面积。

#### 依赖关系

要启用此参数，请将 **Area characteristics** 设置为 `Identical for all flow paths`，并将 **Orifice parameterization** 设置为以下之一：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Discharge coefficient** — 流量系数 `0.64`（默认） | positive scalar

用于考虑理论流量中流量损失的修正系数。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为以下之一：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认） | positive scalar

通过节流口的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **Smoothing factor** — 数值平滑因子 `0.01`（默认） | positive scalar in the range of [0,1]

连续平滑因子，当阀处于接近开启和接近关闭位置时，基于流量响应引入一层渐变变化。为了提高在这些工况下仿真的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为 `Linear - area vs. spool travel`。

### **Pressure recovery** — 是否考虑面积扩大中的压力增加 `off`（默认） | `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **Orifice parameterization** 设置为：

- `Linear - area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### P-A 节流口

### **Spool position at maximum P-A orifice area** — 完全开启 P-A 节流口时的阀芯偏移 `5e-3 m`（默认） | positive scalar

完全开启 P-A 节流口时阀芯从中位偏移的距离。

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

仅当 P-A 节流口设置未同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才启用此参数。

### **P-A spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

阀芯位移的最大距离。此值提供计算的上限，以便仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

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

### **P-A maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认） | positive scalar

阀运行期间 P-A 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

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

### **P-A orifice spool travel vector** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格参数化的阀芯位移距离向量。向量元素必须与 **P-A orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

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

### **P-A orifice area vector** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀面积表格参数化的开启面积向量。向量元素必须与 **P-A spool travel vector** 参数中的元素一一对应。元素按升序列出。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m` (默认) | 1-by-*n* vector

用于体积流量表格参数化的阀芯移动距离向量。阀芯移动向量与
**P-A orifice pressure drop vector, dp** 参数构成独立轴，
用于二维因变量 **P-A orifice volumetric flow rate table,
q(ds,dp)** 参数。按升序列出这些值。
第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice pressure drop vector, dp** — 压力降值向量 `[-.1, .3, .5, .7] MPa` (默认) | 1-by-*n* vector

用于体积流量表格参数化的压力降值向量。压力降向量与
**P-A orifice spool travel vector, ds** 参数构成独立轴，
用于二维因变量 **P-A orifice volumetric flow rate table,
q(ds,dp)** 参数。按升序列出这些值。
元素必须大于 0。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (默认) | *M*-by-*N* matrix

基于压力降和阀芯移动距离独立值的 *M*-by-*N* 体积流量矩阵。
*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A orifice spool travel vector,
  ds** 参数中向量元素的数量。
- *N* 是 **P-A orifice pressure drop vector,
  dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

### **P-A constant orifice area** — 恒定孔口的横截面积 `1e-4 m^2` (默认) | positive scalar

当正阀芯位置和负阀芯位置包含同一孔口时的孔口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为以下之一：

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 在每个参数中进行以下设置之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A 孔口设置同时出现在 **Positive
spool position open connections** 和 **Negative spool position open
connections** 参数中时，此参数才启用。

### **P-A constant orifice pressure drop vector** — 恒定孔口的压差值向量 `[-.1, .3, .5, .7] MPa` (默认) | 1-by-*n* vector

当正阀芯位置和负阀芯位置包含同一孔口时，用于恒定孔口的阀两端压差值向量。
向量元素与 **P-A constant orifice volumetric flow rate
vector** 参数中的元素一一对应。按升序列出这些值。该模块
在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中进行以下设置之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A 孔口设置同时出现在 **Positive
spool position open connections** 和 **Negative spool position open
connections** 参数中时，此参数才启用。

### **P-A constant orifice volumetric flow rate vector** — 恒定孔口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s` (默认) | 1-by-*n* vector

当正阀芯位置和负阀芯位置包含同一孔口时，阀两端的压差值向量。
向量元素与 **P-A constant orifice pressure drop vector**
参数中的元素一一对应。按升序列出这些值。该模块使用线性
插值 between 数据点。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中进行以下设置之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-A orifice settings 同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，此参数才启用。

### P-B 孔口

### **Spool position at maximum P-B orifice area** — 完全打开 P-B 孔口的阀芯偏移 `-5e-3` (默认) | positive scalar

完全打开 P-B 孔口时相对于中位位置的阀芯偏移。

#### 依赖关系

要启用此参数，请设置以下参数之一：

将 **Positive spool position open connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

将 **Negative spool position open
connections** 设置为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-T, B-T`

**注意：**

仅当 P-B 孔口设置不同时出现在 **Positive spool position open connections** 和
**Negative spool position open
connections** 参数中时，此参数才启用。

### **P-B spool travel between closed and open orifice** — 最大阀芯行程 `0.005 m` (默认) | positive scalar

阀芯移动的最大距离。此值提供计算上限，使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   或将 **Negative spool position
   open connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B maximum orifice area** — 最大孔口开启面积 `1e-4 m^2` (默认) | positive scalar

阀运行期间 P-B 孔口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice spool travel vector** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m` (默认) | 1-by-*n* vector

用于阀面积表格参数化的阀芯移动距离向量。向量元素必须与
**P-B orifice area vector** 参数中的元素一一对应。按升序列出
这些值。第一个元素必须为 0。该模块在数据点之间使用
线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice area vector** — 阀开口面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2` (默认) | 1-by-*n* vector

用于阀面积表格参数化的开口面积向量。向量元素必须与
**P-B spool travel vector** 参数中的元素一一对应。按升序
列出元素。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice spool travel vector, ds** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m` (默认) | 1-by-*n* vector

用于体积流量表格参数化的阀芯移动距离向量。阀芯移动向量与
**P-B orifice pressure drop vector, dp** 参数构成独立轴，
用于二维因变量 **P-B orifice volumetric flow rate table,
q(ds,dp)** 参数。按升序列出这些值。
第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice pressure drop vector, dp** — 压力降值向量 `[-.1, .3, .5, .7] MPa` (默认) | 1-by*n* vector

用于体积流量表格参数化的压力降值向量。压力降向量与
**P-B orifice spool travel vector, ds** 参数构成独立轴，
用于二维因变量 **P-B orifice volumetric flow rate table,
q(ds,dp)** 参数。按升序列出这些值。
元素必须大于 0。该模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s` (默认) | *M*-by-*N* matrix

基于压力降和阀芯移动距离独立值的 *M*-by-*N* 体积流量矩阵。
*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B orifice spool travel vector,
  ds** 参数中向量元素的数量。
- *N* 是 **P-B orifice pressure drop vector,
  dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

### **P-B constant orifice area** — 恒定孔口的横截面积 `1e-4 m^2` (默认) | positive scalar

当正阀芯位置和负阀芯位置包含同一孔口时的孔口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为以下之一：

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 在每个参数中进行以下设置之一：

   将 **Positive spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   将 **Negative spool position open
   connections** 设置为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-B 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，此参数才启用。

### **P-B constant orifice pressure drop vector** — 恒定孔口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* 向量

当正负滑阀位置包含同一孔口时，阀上的压差值向量。向量元素与 **P-B constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-B 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **P-B constant volumetric flow rate vector** — 恒定孔口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* 向量

当正负滑阀位置包含同一孔口时，阀上的体积流量值向量。向量元素与 **P-B
constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   **Positive spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

   **Negative spool position open
   connections** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B, A-T,
     B-T`

**注意：**

仅当 P-B 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### A-T 孔口

### **Spool position at maximum A-T orifice area** — 完全打开 A-T 孔口时的滑阀偏移 `-5e-3 m`（默认） | 正标量

完全打开 A-T 孔口时，从中位开始的滑阀偏移。

#### 依赖

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。
- **Negative spool position open
  connections** 为 `P-B,
  A-T` 或 `P-A, P-B, A-T,
  B-T`。

**注意：**

仅当 A-T 孔口设置未同时出现在 **Positive spool position open connections** 和
**Negative spool position open
connections** 参数中时，才启用此参数。

### **A-T spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认） | 正标量

滑阀行程的最大距离。此值提供计算上限，以便仿真不会返回非物理值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 设置以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T maximum orifice area** — 最大孔口开启面积 `1e-4 m^2`（默认） | 正标量

阀运行期间 A-T 孔口的最大开启面积。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 设置以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice spool travel vector** — 相对于完全关闭位置的滑阀开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* 向量

用于阀面积表格化参数化的滑阀行程距离向量。向量元素必须与 **A-T orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 设置以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice spool travel vector** — 相对于完全关闭位置的滑阀开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* 向量

用于阀面积表格化参数化的滑阀行程距离向量。向量元素必须与 **A-T orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 设置以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice spool travel vector, ds** — 相对于完全关闭位置的滑阀开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* 向量

用于体积流量表格化参数化的滑阀行程距离向量。滑阀行程向量与 **A-T orifice pressure drop vector, dp** 参数共同构成独立轴，用于二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 参数。按升序列出值。第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 设置以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **A-T orifice spool travel vector, ds** 参数共同构成独立轴，用于二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 参数。按升序列出值。元素必须大于 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 设置以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*-by-*N* 矩阵

基于压降和滑阀行程距离独立值的 *M*-by-*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T orifice spool travel vector,
  ds** 参数中向量元素的数量。
- *N* 是 **A-T orifice pressure drop vector,
  dp** 参数中向量元素的数量。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 设置以下参数之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

### **A-T constant orifice area** — 恒定孔口的横截面积 `1e-4 m^2`（默认） | 正标量

当正负滑阀位置包含同一孔口时的孔口面积。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为以下之一：

   - `Linear - area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **A-T constant orifice pressure drop vector** — 恒定孔口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* 向量

当正负滑阀位置包含同一孔口时，阀上的压差值向量。向量元素与 **A-T constant orifice volumetric flow rate
vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### **A-T constant orifice volumetric flow rate vector** — 恒定孔口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* 向量

当正负滑阀位置包含同一孔口时的体积流量值向量。向量元素与 **A-T constant orifice
pressure drop vector** 参数中的元素一一对应。按升序列出值。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中设置以下之一：

   - **Positive spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。
   - **Negative spool position open
     connections** 为 `P-B,
     A-T` 或 `P-A, P-B, A-T,
     B-T`。

**注意：**

仅当 A-T 孔口设置同时出现在 **Positive spool position
open connections** 和 **Negative spool position open connections**
参数中时，才启用此参数。

### B-T 孔口

### **Spool position at maximum B-T orifice area** — 完全打开 B-T 孔口时的滑阀偏移 `5e-3 m`（默认） | 正标量

完全打开 B-T 孔口时，从中位开始的滑阀偏移。

#### 依赖

要启用此参数，请设置以下参数之一：

- **Positive spool position open
  connections** 为 `P-A,
  B-T`。
- **Negative spool position open
  connections** 为 `P-A,
  B-T`。

**注意：**

仅当 B-T 孔口设置未同时出现在 **Positive spool position open connections** 和
**Negative spool position open
connections** 参数中时，才启用此参数。

### **B-T spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认） | 正标量

滑阀行程的最大距离。此值提供计算上限，以便仿真不会返回非物理值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 设置以下参数之一：

   **Positive spool position open connections** 为 `P-A,
   B-T`。

   **Negative spool position open connections** 为 `P-A,
   B-T`。

### **B-T maximum orifice area** — 最大孔口开启面积 `1e-4 m^2`（默认） | 正标量

阀运行期间 B-T 孔口的最大开启面积。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 设置以下参数之一：

   **Positive spool position open connections** 为 `P-A,
   B-T`。

   **Negative spool position open connections** 为 `P-A,
   B-T`。

### **B-T orifice spool travel vector** — 相对于完全关闭位置的滑阀开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* 向量

用于阀面积表格化参数化的滑阀行程距离向量。向量元素必须与 **B-T orifice area vector** 参数中的元素一一对应。按升序列出值。第一个元素必须为 0。该模块在数据点之间使用线性插值。

#### 依赖

要启用此参数，请设置：

1. **Area characteristics** 设置为
   `Different for each flow
   path`。
2. **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 设置以下参数之一：

   **Positive spool position open connections** 为 `P-A,
   B-T`。

   **Negative spool position open connections** 为 `P-A,
   B-T`。

### **B-T orifice area vector** — 阀开口面积的向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀面积表格参数化的阀开口面积向量。向量元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。元素按升序列出。元素必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice spool travel vector, ds** — 相对于完全关闭位置的滑阀开口距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于体积流量表格参数化的控制元件行程距离向量。滑阀行程向量与 **B-T orifice pressure drop vector, dp** 参数一起，为二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 参数构成独立轴。按升序列出值。第一个元素必须为 0。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **B-T orifice spool travel vector, ds** 参数一起，为二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 参数构成独立轴。按升序列出值。元素必须大于 0。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*-by-*N* matrix

基于压降和滑阀行程距离独立值的 *M*-by-*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **B-T orifice spool travel vector, ds** 参数中的向量元素数。
- *N* 是 **B-T orifice pressure drop vector, dp** 参数中的向量元素数。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

### **B-T constant orifice area** — 恒定孔口的孔口横截面积 `1e-4 m^2`（默认） | positive scalar

当正负滑阀位置包含同一孔口时的孔口面积。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为以下之一：

   - `Linear - area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 孔口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **B-T constant orifice pressure drop vector** — 恒定孔口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

当正负滑阀位置包含同一孔口时，阀上的压差值向量。向量元素与 **B-T constant orifice volumetric flow rate vector** 参数中的元素一一对应。按升序列出值。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 孔口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### **B-T constant volumetric flow rate vector** — 恒定孔口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* vector

当正负滑阀位置包含同一孔口时，阀上的体积流量值向量。向量元素与 **B-T constant orifice pressure drop vector** 参数中的元素一一对应。按升序列出值。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为 `Different for each flow path`。
2. 将 **Orifice parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   将 **Positive spool position open connections** 设置为 `P-A, B-T`。

   将 **Negative spool position open connections** 设置为 `P-A, B-T`。

**注意：**

仅当 B-T 孔口设置同时出现在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中时，才会启用此参数。

### 故障

### **4-Way 2-Position Directional Valve Area fault** — 对阀面积故障建模的选项 `Add fault`

对模块中的阀面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。发生故障时，通常由开口参数化设置的阀面积将根据 **Spool position when faulted** 参数中指定的值进行设置。

### **Spool position when faulted** — 故障阀特性 `Positive`（默认） | `Negative` | `Maintain last value`

故障状态下的阀滑阀位置。您可以选择让阀在滑阀处于正位置、负位置或故障触发时的位置时卡滞。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024a: 使用 Simscape 故障接口对故障建模

4-Way 2-Position Directional Valve (IL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

等温液体网络中的四通两位方向阀

4-Way 2-Position Directional Valve (IL) 模块对等温液体网络中具有四个开口的阀进行建模——例如执行器、泵和油箱之间的阀。阀操作由单个滑阀控制，该滑阀根据端口 **S** 处的信号移动。您可以通过分别在 **Positive spool position open connections** 和 **Negative spool position open connections** 参数中指定滑阀沿正方向和负方向移动时打开的孔口，来设置阀的基准配置。您可以在 **Orifice parameterization** 参数中将阀开口模型设置为线性关系或用户提供数据的函数，并将其应用于阀中的一个或所有流动路径。

此模块是一个复合组件，包含多个 Orifice (IL) 模块实例。有关阀参数化和模块计算的更多详细信息，请参阅 Orifice (IL) 模块。在某些配置中，此阀类似于三通阀。要在滑阀处于中位时设置额外的流动路径，请参阅 4-Way 3-Position Directional Valve (IL) 模块。

此图显示了一个示例阀设置，其中阀连接到油箱、执行器和泵，并且 **Positive spool position open connections** 参数为 `P-B, A-T`：

此图显示了当 **Negative spool position open connections** 参数为 `P-A, B-T` 时的阀：

在此配置中，当端口 **S** 处的信号将滑阀移动到负位置时，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径对流动打开。端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径对流动关闭。

此图显示了当 **Positive spool position open connections** 参数为 `P-B, A-T` 时的阀：

在此配置中，当端口 **S** 处的信号将滑阀移动到正位置时，端口 **P** 与 **B** 之间以及端口 **A** 与 **T** 之间的路径对流动打开，端口 **P** 与 **A** 之间以及端口 **B** 与 **T** 之间的路径关闭。

表示此配置的示意图为：

左侧对应正位置，右侧对应负位置。阀通过中间中性区段中的位置进行过渡。

### 阀芯位移和阀配置

*阀芯行程* 是孔口从关闭位置完全打开所需的阀芯移动量。您可以使用 **Orifice
parameterization** 和 **Area characteristics**
参数来指定流路特性：

| 孔口参数化 | 所有流路相同 | 每条流路不同 |
| --- | --- | --- |
| `Linear - Area vs. spool travel` | **Spool travel between closed and open orifice** 参数定义阀芯行程 | **Spool travel between closed and open orifice** 参数定义每个孔口的阀芯行程 |
| `Tabulated data - Area vs. spool travel` | **Spool travel vector** 参数的第一个和最后一个元素之差定义阀芯行程 | **Spool travel vector** 参数的第一个和最后一个元素之差为每个孔口定义阀芯行程 |
| `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | **Spool travel vector, ds** 参数的第一个和最后一个元素之差定义阀芯行程 | **Spool travel vector, ds** 参数的第一个和最后一个元素之差为每个孔口定义阀芯行程 |

阀芯移动方向取决于阀芯行程、孔口方向以及端口 **S** 处的信号。下表显示了孔口的阀芯行程，具体取决于 **Positive spool
position open connection** 和 **Negative spool position open
connection** 参数的选择：

| 孔口打开时的阀芯位置 | 阀芯行程，*ΔS* |
| --- | --- |
| 孔口始终关闭：孔口未针对 **Positive spool position open connection** 或 **Negative spool position open connection** 参数选择 | N/A |
| 孔口始终打开：孔口同时针对 **Positive spool position open connection** 和 **Negative spool position open connection** 参数选择 | N/A |
| Negative：孔口仅针对 **Negative spool position open connection** 参数选择 | *S*orifice\_max + 阀芯行程 – **S** |
| Positive：孔口仅针对 **Positive spool position open connection** 参数选择 | *S*orifice\_max – 阀芯行程 + **S** |

其中 *S*orifice\_max 是为每个孔口定义的最大孔口面积处的阀芯位置。当 *ΔS* 为负时，孔口面积饱和于泄漏面积；当孔口完全打开时，饱和于最大孔口面积。当孔口完全打开时，*ΔS* 等于阀芯行程，因此 *ΔS* 大于阀芯行程不会进一步增大孔口面积。

下表显示了 4-Way 2-Position Directional Valve
(IL) 的可能配置：

| 配置 | 参数值 |
| --- | --- |
| 过渡期间所有四条路径均关闭。 | - **Positive spool position open   connections**：`P-A,   B-T` - **Negative spool position open   connections**：`P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < –P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** < –A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** > B-T 阀芯行程 |
| 过渡期间所有四条路径均打开。 | - **Positive spool position open   connections**：`P-A,   B-T` - **Negative spool position open   connections**：`P-B,   A-T`  - **Spool position at maximum P-A orifice   area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > –P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > –A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** < B-T 阀芯行程 |
| 过渡期间 A-T 和 B-T 关闭。 | - **Positive spool position open   connections**：`P-A,   B-T` - **Negative spool position open   connections**：`P-B,   A-T`  - **Spool position at maximum P-A orifice   area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > –P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** < –A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** > B-T 阀芯行程 |
| 过渡期间 P-A 和 P-B 关闭。 | - **Positive spool position open   connections**：  `P-A` - **Negative spool position open   connections**：  `P-B`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < –P-B 阀芯行程 |
| 过渡期间 P-B 和 B-T 关闭。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** < –B-T 阀芯行程 |
| 过渡期间 P-A 和 A-T 关闭。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** > –B-T 阀芯行程 |
| 过渡期间 P-A、P-B 和 B-T 打开。 | - **Positive spool position open   connections**：`P-A,   P-B` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-A orifice   area** < P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** = 任意值 - **Spool position at maximum B-T orifice   area** > –B-T 阀芯行程 |
| 过渡期间 P-A、A-T 和 B-T 打开。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   P-B`  - **Spool position at maximum P-A orifice   area** > –P-A 阀芯行程 - **Spool position at maximum A-T orifice   area** < A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** = 任意值 |
| 过渡期间 P-A 和 P-B 关闭。A-T 始终关闭。 | - **Positive spool position open   connections**：`P-A,   P-B` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum B-T orifice   area** < –B-T 阀芯行程 |
| 过渡期间所有路径均关闭。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > A-T 阀芯行程 |
| 过渡期间 A-T 打开。过渡期间 P-A 关闭。 | - **Positive spool position open   connections**：`P-A,   P-B` - **Negative spool position open   connections**：`P-A,   B-T`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** = 任意值 - **Spool position at maximum B-T orifice   area** > –B-T 阀芯行程 |
| 过渡期间 B-T 打开。过渡期间 P-B 关闭。 | - **Positive spool position open   connections**：`P-B,   A-T` - **Negative spool position open   connections**：`P-A,   P-B`  - **Spool position at maximum P-A orifice   area** < –P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** < A-T 阀芯行程 - **Spool position at maximum B-T orifice   area** = 任意值 |
| 过渡期间 P-A 关闭。 | - **Positive spool position open   connections**：`P-A,   B-T` - **Negative spool position open   connections**：`P-A,   P-B`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** < –P-B 阀芯行程 - **Spool position at maximum B-T orifice   area** > B-T 阀芯行程 |
| 过渡期间 P-B 关闭。 | - **Positive spool position open   connections**：`P-A,   P-B` - **Negative spool position open   connections**：`P-B,   A-T`  - **Spool position at maximum P-A orifice   area** > P-A 阀芯行程 - **Spool position at maximum P-B orifice   area** > P-B 阀芯行程 - **Spool position at maximum A-T orifice   area** > –A-T 阀芯行程 |

### 阀孔口参数化

**Orifice parameterization** 参数指定通过一个或所有阀门孔口的开口面积或体积流量的模型。如果您将 **Area characteristics** 设置为 `Identical for all flow
paths`，则模块对所有流路应用相同数据。当您选择 `Different for all flow paths` 时，模块对每条流路使用单独的参数化。

当 **Orifice parameterization** 为 `Linear - area
vs. spool travel` 时，开口面积是端口 **S** 处作为信号接收的阀芯位置的线性函数

Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

其中：

- *ΔS* 是阀芯行程。

  *Aorifice* 在
  *ΔS* 为负时饱和于
  *Aleak*，并且在孔口完全打开时饱和于
  *Amax*。当孔口完全打开时，*ΔS* 等于阀芯行程，因此大于阀芯行程的 *ΔS* 值不会增大孔口面积。
- *ΔSmax* 是
  **Spool travel between closed and open orifice**
  参数的值。
- *Amax* 是
  **Maximum orifice area** 参数的值。
- *Aleak* 是
  **Leakage area** 参数的值。

  当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整
  **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing
  factor** 参数非零，模块会在 *Aleak* 和
  *Amax* 之间平滑地饱和开口面积。有关更多信息，请参阅数值平滑。

当 **Orifice parameterization** 为 `Tabulated data
- Area vs. spool travel` 时，您可以为系统或端口 **P**、
**A**、**B** 和 **T** 之间的各条流路提供阀芯行程向量。模块使用此数据计算孔口面积与阀芯位移之间的关系。模块使用插值确定数据点之间的开口面积。*A*leak 和
*A*max 分别是开口面积向量的第一个和最后一个参数。

当 **Orifice parameterization** 为 `Tabulated data
- Volumetric flow rate vs. spool travel and pressure drop` 时，您可以提供阀芯行程和压降向量以及相关的二维体积流量数组。模块使用插值确定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

### 可视化孔口开口

要可视化阀芯偏移和最大位移，请右键单击模块并选择 **Fluids** > **Plot Valve Characteristics**。绘图显示 **Valve Configuration** 部分中参数指定的孔口。坐标轴为以下之一：

- 孔口面积与阀芯位置
- 体积流量与阀芯位置，在特定压差下查询

当您将 **Valve
Configuration** 选项卡中的参数设置为同一孔口时，孔口开度为常数。

单击 **Reload Data** 以更新图中的数据。

下图显示了模块的默认配置：

- **Positive spool position open connections** 为
  `P-A, B-T`。
- **Negative spool position open connections** 为
  `P-B, A-T`。

所有其他阀芯位置均为默认值。

**阀芯位置可视化示例**

### 故障

要对故障建模，请在 **Faults** 部分中单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Simscape 故障简介。

**Spool position when faulted** 参数具有三个故障选项：

- `Positive` — 阀芯位置冻结在正位置，将 **Positive spool position open connections**
  参数指定的流路打开至其最大值。**Negative spool position open connections**
  参数指定的流路关闭。
- `Negative` — 阀芯位置冻结在负位置，将 **Negative spool position open connections**
  参数指定的流路打开至其最大值。**Positive spool position open connections**
  参数指定的流路关闭。
- `Maintain last value` — 触发发生时，阀门冻结在阀芯位置。

由于阀门面积极值处的数值平滑，在线性参数化中，模块使用的最小面积大于
**Leakage area**，最大面积小于
**Maximum orifice area**，与
**Smoothing factor** 值成比例。有关更多信息，请参阅数值平滑。

故障触发后，阀门在仿真的剩余时间内保持故障面积。

### 预定义参数化

您可以使用预参数化制造数据填充模块，从而对特定供应商组件建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的
   "<click to select>" 超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后单击 **Apply all**。您可以使用
   **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。
   模块现在具有您指定的参数化。
4. 您可以通过选择部件并查看
   **Compare selected part with block**
   部分中的数据，在 Block Parameterization Manager 窗口中将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用数据源提供参数值。对于缺失数据，模块会使用工程判断和简化假设替代。因此，仿真与实际物理行为之间可能会出现一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅预参数化组件列表。
