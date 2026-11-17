---
type: simulink-block
title: '4-Way 3-Position Directional Valve (TL)'
family: 'thermal-liquid'
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

### **S** — 阀芯或阀控制构件，unitless physical signal

阀控制构件的瞬时位移。
### 守恒

### **P** — 流道 thermal liquid

流体可以进入或离开阀的开口。此端口通常连接到流体供应管线。

### **T** — 流道 thermal liquid

流体可以进入或离开阀的开口。此端口通常连接到流体回流管线。

### **A** — 流道 thermal liquid

流体可以进入或离开阀的开口。此端口通常连接到致动管路。

### **B** — 流道 thermal liquid

流体可以进入或离开阀的开口。此端口通常连接到致动管路。

## 参数

### 阀配置

### **正阀芯位置开启连接** — 当阀芯处于正位置时开启的流路 `P-A, B-T`（默认） | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯处于正位置时，流路开启。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置是否与其他孔口一致，请将 **中位阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error`。

### **中位阀芯位置开启连接** — 当阀芯处于中位时开启的流路 `All closed`（默认） | `P-A, P-B, A-T, B-T` | `A-T, B-T` | `P-A, A-T` | `P-A, B-T` | `P-A, P-B` | `P-B, A-T` | `P-B, B-T` | `A-T` | `B-T` | `P-A` | `P-B` | `P-T` | `P-A, A-T, P-T` | `P-A, P-B, A-B` | `P-B, B-T, P-T` | `P-A, P-B, A-T, B-T, P-T`

当阀芯处于中位时，流路开启。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置是否与其他孔口一致，请将 **中位阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error`。

### **负阀芯位置开启连接** — 当阀芯沿负方向运动时开启的流路 `P-A, B-T`（默认） | `P-A, P-B` | `P-B, A-T` | `P-A` | `P-B` | `P-A, P-B, A-B`

当阀芯沿负方向运动时，流路开启。此参数设置阀配置，并根据端口 **S** 接收的信号定义阀芯运动方向。要检查参数设置是否与其他孔口一致，请将 **中位阀芯位置开启连接的一致性检查** 设置为 `Warning` 或 `Error`。

### **中位阀芯位置开启连接的一致性检查** — 是否检查孔口设置是否与最大孔口开启的指定阀芯位置一致 `Warning`（默认） | `Error` | `None`

是否检查 **阀配置** 选项卡上的中位阀芯位置开启设置是否与最大孔口面积处的指定阀芯位置一致。对于每个启用的孔口，阀芯中位处的实际偏移应与每个单独孔口的指定阀芯偏移相匹配。

### 模型参数化

### **面积特性** — 孔口的流量方程 `Identical for all flow paths`（默认） | `Different for each flow path`

为阀孔口面积应用统一或单独的流量方程。`Identical for all flow paths` 对所有阀孔口使用相同的孔口和阀芯几何、流量、压力和面积向量。使用 `Different for each flow path` 时，这些参数为每个孔口单独指定。在两种情况下，所有孔口在 `Linear - Area vs. spool travel` 和 `Tabulated data - Area vs. spool travel` 参数化中具有相同的横截面积、流量系数和雷诺数。相同的 **孔口参数化** 应用于所有流路。

### **孔口参数化** — 计算开启面积的方法 `Linear - Area vs. spool travel`（默认） | `Tabulated data - Area vs. spool travel` | `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` | `Tabulated data - Mass flow rate vs. spool travel and pressure drop`

计算阀开启面积的方法。在表格数据参数化中，可以为非线性阀开启特性提供自己的阀面积和阀芯行程数据，或者提供以体积流量、阀芯行程和流路压降表示的数据。

### **关闭与开启孔口之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认） | positive scalar

阀芯行程的最大距离。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Linear - Area vs. spool travel`。

### **最大孔口面积** — 最大孔口开启面积 `1e-4 m^2`（默认） | positive scalar

阀运行期间每个孔口最大的开启面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Linear - Area vs. spool travel`。

### **泄漏面积** — 孔口完全关闭时的开启面积 `1e-9 m^2`（默认） | positive scalar

孔口完全关闭时的开启面积。任何小于此值的面积都保持在指定的泄漏面积。此参数通过保持流动连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Linear - Area vs. spool travel`。

### **阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格参数化的阀芯行程距离向量。向量元素必须与 **孔口面积向量** 参数中的元素一一对应。值按升序列出，第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **孔口面积向量** — 阀开启面积向量 `[1e-09, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀开启面积表格参数化的开启面积向量。向量元素必须与 **阀芯行程向量** 参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **阀芯行程向量, ds** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于体积流量表格参数化的阀芯行程距离向量。阀芯行程向量与 **压降向量, dp** 参数构成独立轴，用于二维因变量 **体积流量表, q(ds,dp)** 或 **质量流量表, mdot(ds,dp)** 参数。值按升序列出，第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **压降向量, dp** — 阀压降值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **阀芯行程向量, ds** 参数构成独立轴，用于二维因变量 **体积流量表, q(ds,dp)** 或 **质量流量表, mdot(ds,dp)** 参数。值按升序列出，且必须大于 0。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **体积流量表, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; .00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*-by-*N* matrix

*M*-by-*N* matrix，包含基于压降和阀芯行程距离独立值的体积流量。*M* 和 *N* 是相关向量的大小：

- *M* 是 **阀芯行程向量, ds** 参数中向量元素的数量。
- *N* 是 **压降向量, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **质量流量表, mdot(ds,dp)** — 质量流量 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认） | *M*-by-*N* matrix

*M*-by-*N* matrix，包含基于压降和阀芯行程距离独立值的质量流量。*M* 和 *N* 是相关向量的大小：

- *M* 是 **阀芯行程向量, ds** 参数中向量元素的数量。
- *N* 是 **压降向量, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **恒定孔口面积** — 相同流路的孔口面积 `1e-4 m^2`（默认） | positive scalar

当正、中、负阀芯位置使用相同孔口时的孔口面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为以下之一：

- `Linear - Area vs. spool travel`.
- `Tabulated data - Area vs. spool travel`

必须在所有三个 **阀配置** 参数中选择相同的孔口：

- **正阀芯位置开启连接**
- **中位阀芯位置开启连接**
- **负阀芯位置开启连接**

### **恒定孔口压降向量** — 相同流路的压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

当正、中、负阀芯位置使用相同孔口时，阀上的压差值向量。向量元素与 **恒定孔口体积流量向量** 或 **恒定孔口质量流量表, mdot(ds,dp)** 参数中的元素一一对应。值按升序列出。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

必须在所有三个 **阀配置** 参数中选择相同的孔口：

- **正阀芯位置开启连接**
- **中位阀芯位置开启连接**
- **负阀芯位置开启连接**

### **恒定孔口体积流量向量** — 相同流路的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* vector

当正、中、负阀芯位置使用相同孔口时，恒定孔口的体积流量值向量。向量元素与 **恒定孔口压降向量** 参数中的元素一一对应。值按升序列出。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

必须在所有三个 **阀配置** 参数中选择相同的孔口：

- **正阀芯位置开启连接**
- **中位阀芯位置开启连接**
- **负阀芯位置开启连接**

### **恒定孔口质量流量向量** — 恒定孔口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认） | 1-by-*n* vector

当正、中、负阀芯位置使用相同孔口时，阀上的质量流量值向量。向量元素与 **恒定孔口压降向量** 参数中的元素一一对应。值按升序列出。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

必须在所有三个 **阀配置** 参数中选择相同的孔口：

- **正阀芯位置开启连接**
- **中位阀芯位置开启连接**
- **负阀芯位置开启连接**

### **参考流入温度** — 指定质量流量数据时的温度 `293.15 K`（默认） | positive scalar

指定表格质量流量数据时的温度。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **参考流入压力** — 指定质量流量表格数据时的压力 `0.101325 MPa`（默认） | positive scalar

指定表格质量流量数据时的压力。模块使用此参数计算第三个参考参数，即参考密度。它使用该参考来缩放当压力和温度偏离参考条件时的表格压降数据。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。

### **端口 P、T、A 和 B 处的横截面积** — 守恒端口处的面积 `0.01 m^2`（默认） | positive scalar

入口和出口端口 **P**、**T**、**A** 和 **B** 处的最大横截面积，用于确定通过阀的质量流量和能量流率平滑的压力-流量方程中。

### **流量系数** — 流量系数 `0.64`（默认） | positive scalar

用于考虑理论流动中流出损失的修正因子。

#### 依赖关系

要启用此参数，请将 **孔口参数化** 设置为以下之一：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **临界雷诺数** — 层流的上限雷诺数 `150`（默认） | positive scalar

通过孔口的层流的上限雷诺数。

#### 依赖项

要启用此参数，请将 **节流口参数化** 设置为：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### **平滑因子** — 数值平滑因子 `0.01`（默认）| positive scalar，范围为 [0,1]

连续平滑因子，在阀处于接近打开和接近关闭位置时，基于流量响应引入一层渐变。为了提高仿真在这些工况下的稳定性，请将此参数设置为小于 1 的非零值。

#### 依赖项

要启用此参数，请将 **节流口参数化** 设置为 `Linear - Area vs. spool travel`。

### **压力恢复** — 是否考虑面积扩张中的压力增加 `off`（默认）| `on`

当流体从较小横截面积区域流向较大横截面积区域时，是否考虑压力增加。

#### 依赖项

要启用此参数，请将 **节流口参数化** 设置为：

- `Linear - Area vs. spool travel`
- `Tabulated data - Area vs. spool travel`

### P-A Orifice

### **最大 P-A 节流口面积时的阀芯位置** — 完全打开 P-A 节流口时的阀芯偏移 `7.5e-3 m`（默认）| positive scalar

完全打开 P-A 节流口时相对于中位位置的阀芯偏移。**中位阀芯位置打开连接的一致性检查**参数将通知您，根据其他节流口阀芯位置，为此阀芯位置设置的值是否不一致或不符合物理规律。

#### 依赖项

要启用此参数，请设置以下参数之一：

将 **正阀芯位置打开连接** 设置为：

- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

将 **中位阀芯位置打开连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, A-T, P-T`
- `P-A, P-B, A-B`
- `P-A, P-B, A-T, B-T, P-T`

将 **负阀芯位置打开连接** 设置为：

- `P-A, P-B, A-T, B-T`
- `P-A, A-T`
- `P-A, B-T`
- `P-A, P-B`
- `P-A`
- `P-A, P-B, A-B`

**注意：**

仅当 P-A 节流口设置未出现在全部三个阀芯位置参数中时，才启用此参数：**正阀芯位置打开连接**、**中位阀芯位置打开连接**和**负阀芯位置打开连接**。

### **P-A 节流口关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| positive scalar

阀芯行程的最大距离。此值提供计算上限，以便仿真不返回不符合物理规律的值。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 最大节流口面积** — 最大节流口打开面积 `1e-4 m^2`（默认）| positive scalar

阀操作期间 P-A 节流口的最大打开面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为 `Linear - Area vs. spool travel`。
3. 以下参数之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 节流口面积向量** — 阀打开面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀打开面积表格参数化的打开面积向量。向量元素必须与 **P-A 阀芯行程向量** 参数中的元素一一对应。元素按升序列出，并且必须大于 0。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为 `Tabulated data - Area vs. spool travel`。
3. 以下参数之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 节流口阀芯行程向量, ds** — 相对于完全关闭位置的阀芯打开距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于体积流量表格参数化的阀芯行程距离向量。阀芯行程向量与 **P-A 节流口压降向量, dp** 参数一起，为二维因变量 **P-A 节流口体积流量表, q(ds,dp)** 或 **P-A 节流口质量流量表, mdot(ds,dp)** 参数形成独立轴。值按升序列出，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 节流口压降向量, dp** — 压降值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **P-A 节流口阀芯行程向量, ds** 参数一起，为二维因变量 **P-A 节流口体积流量表, q(ds,dp)** 或 **P-A 节流口质量流量表, mdot(ds,dp)** 参数形成独立轴。值按升序列出，并且必须大于 0。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 节流口体积流量表, q(ds,dp)** — 体积流量值的数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*-by-*N* matrix

*M*-by-*N* matrix，表示基于压降和阀芯行程距离独立值的体积流量。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A 节流口阀芯行程向量, ds** 参数中向量元素的数量。
- *N* 是 **P-A 节流口压降向量, dp** 参数中向量元素的数量。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 节流口质量流量表, mdot(ds,dp)** — 质量流量值的数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*-by-*N* matrix

*M*-by-*N* matrix，表示基于压降和阀芯行程距离独立值的质量流量。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-A 节流口阀芯行程向量, ds** 参数中向量元素的数量。
- *N* 是 **P-A 节流口压降向量, dp** 参数中向量元素的数量。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 以下参数之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 恒定节流口面积** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| positive scalar

当正、中、负阀芯位置使用同一节流口时的节流口面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为以下两者之一：

   - `Linear - Area vs. spool travel`
   - `Tabulated data - Area vs. spool travel`
3. 每个参数中的以下设置之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 恒定节流口压降向量** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* vector

当正、中、负阀芯位置使用同一节流口时，阀门上的压差值向量。向量元素与 **P-A 恒定节流口体积流量向量** 或 **P-A 节流口质量流量表, mdot(ds,dp)** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop` 或 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 恒定节流口体积流量向量** — 恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1-by-*n* vector

当正、中、负阀芯位置使用同一节流口时，阀门上的体积流量值向量。向量元素与 **P-A 恒定节流口压降向量** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **面积特性** 设置为 `Different for each flow path`。
2. 将 **节流口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   将 **正阀芯位置打开连接** 设置为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

   将 **中位阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, A-T, P-T`
   - `P-A, P-B, A-B`
   - `P-A, P-B, A-T, B-T, P-T`

   将 **负阀芯位置打开连接** 设置为：

   - `P-A, P-B, A-T, B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B, A-B`

### **P-A 恒定节流口质量流量向量** — 恒定节流口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1-by-*n* vector

当正、中、负阀芯位置使用同一节流口时，阀门上的质量流量值向量。向量元素与 **P-A 恒定节流口压降向量** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 每个参数中采用以下设置之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-A, A-T`
   - `P-A, B-T`
   - `P-A, P-B`
   - `P-A`
   - `P-A, P-B,
     A-B`

### P-B Orifice

### **最大 P-B 节流口面积处的阀芯位置** — 完全打开的 P-B 节流口相对于中位的位置偏移 `7.5e-3 m`（默认）| positive scalar

完全打开的 P-B 节流口相对于中位的位置偏移。
**中位阀芯位置开启连接一致性检查**参数将通知您，根据其他节流口阀芯位置，为此阀芯位置设置的值是否不一致或不符合物理规律。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接** 设为：

- `P-B, A-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**中位阀芯位置开启
连接** 设为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T,
  P-T`

**负阀芯位置开启
连接** 设为：

- `P-A, P-B, A-T, B-T`
- `P-B, A-T`
- `P-B, B-T`
- `P-A, P-B`
- `P-B`
- `P-A, P-B, A-B`

**注意：**

仅当 P-B 节流口设置未同时出现在以下三个阀芯位置参数中时，此参数才启用：**正阀芯位置
开启连接**、**中位阀芯
位置开启连接**和**负阀芯位置开启
连接**。

### **关闭和打开节流口之间的 P-B 阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| positive scalar

阀芯行程的最大距离。此值为计算提供上限，以便仿真不会返回不符合物理规律的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 最大节流口面积** — 最大节流口开启面积 `1e-4 m^2`（默认）| positive scalar

阀门运行期间 P-B 节流口的最大开启面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 节流口阀芯行程向量** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀门面积表格化参数化的阀芯行程距离向量。该向量的元素必须与 **P-B 节流口面积向量**参数中的元素一一对应。这些值按升序列出，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 节流口面积向量** — 阀门开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀门开启面积表格化参数化的开启面积向量。该向量的元素必须与 **P-B 阀芯行程向量**参数中的元素一一对应。元素按升序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 节流口阀芯行程向量, ds** — 相对于完全关闭位置的阀芯开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **P-B 节流口压降向量, dp** 参数一起构成独立轴，用于二维因变量 **P-B 节流口体积流量表, q(ds,dp)** 或 **P-B 节流口质量流量表, mdot(ds,dp)** 参数。这些值按升序列出，第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 节流口压降向量, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by*n* vector

用于体积流量表格化参数化的压降值向量。压降向量与 **P-B 节流口阀芯行程向量, ds** 参数一起构成独立轴，用于二维因变量 **P-B 节流口体积流量表, q(ds,dp)** 或 **P-B 节流口质量流量表, mdot(ds,dp)** 参数。这些值按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 节流口体积流量表, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*-by-*N* matrix

基于压降和阀芯行程距离独立值的 *M*-by-*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B 节流口阀芯行程向量, ds** 参数中向量元素的数量。
- *N* 是 **P-B 节流口压降向量, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 以下参数之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 节流口质量流量表, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*-by-*N* matrix

基于压降和阀芯行程距离独立值的 *M*-by-*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-B 节流口阀芯行程向量, ds** 参数中向量元素的数量。
- *N* 是 **P-B 节流口压降向量, dp** 参数中向量元素的数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 恒定节流口面积** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| positive scalar

当正、中、负阀芯位置使用相同节流口时的节流口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为以下之一：

   - `Linear - Area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中采用以下设置之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 恒定节流口压降向量** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* vector

当正、中、负阀芯位置使用相同节流口时，阀门两端的压差值向量。该向量的元素与 **P-B 恒定节流口体积流量向量**或 **P-B 节流口质量流量表, mdot(ds,dp)** 参数中的元素一一对应。这些值按升序列出。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 设为
   `Different for each flow
   path`。
2. **节流口参数化** 设为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 每个参数中采用以下设置之一：

   **正阀芯位置开启
   连接** 设为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启
   连接** 设为：

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

   **负阀芯位置开启
   连接** 设为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 恒定节流口体积流量向量** — 恒定节流口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1-by-*n* vector

当正、中、负阀芯位置使用相同节流口时，阀门两端的体积流量值向量。该向量的元素与 **P-B 恒定节流口压降向量**参数中的元素一一对应。这些值按升序列出。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 在每个参数中进行以下设置之一：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

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

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### **P-B 恒定孔口质量流量向量** — 用于恒定孔口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1-by-*n* 向量

当正、中位和负阀芯位置使用同一孔口时，通过阀的质量流量值向量。向量元素与 **P-B 恒定孔口压降向量** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 在每个参数中进行以下设置之一：

   **正阀芯位置开启连接** 为：

   - `P-B, A-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

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

   **负阀芯位置开启连接** 为：

   - `P-A, P-B, A-T,
     B-T`
   - `P-B, A-T`
   - `P-B, B-T`
   - `P-A, P-B`
   - `P-B`
   - `P-A, P-B,
     A-B`

### A-B 孔口

### **最大 A-B 孔口面积时的阀芯位置** — 完全打开 A-B 孔口时阀芯从中位偏移 `7.5e-3 m`（默认）| 正标量

完全打开 A-B 孔口时阀芯从中位偏移。**中位阀芯位置开启连接一致性检查** 参数将通知您，如果为此阀芯位置设置的值与其他孔口阀芯位置不一致或不符合物理规律。

#### 依赖关系

要启用此参数，请设置以下参数之一：

**正阀芯位置开启连接** 为：

- `P-A, P-B, A-B`

**中位阀芯位置开启连接** 为：

- `P-A, P-B, A-B`

**负阀芯位置开启连接** 为：

- `P-A, P-B, A-B`

**注意：**

仅当 P-A 孔口设置未出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-B 孔口在关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

最大阀芯行程距离。该值为计算提供上限，使仿真不会返回不符合物理规律的值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 最大孔口面积** — 最大孔口开度面积 `1e-4 m^2`（默认）| 正标量

阀运行期间 A-B 孔口的最大开度面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 孔口阀芯行程向量** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* 向量

用于阀面积表格化参数化的阀芯行程距离向量。向量元素必须与 **A-B 孔口面积向量** 参数中的元素一一对应。值按升序列出，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 孔口面积向量** — 阀开度面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* 向量

用于阀开度面积表格化参数化的开度面积向量。向量元素必须与 **A-B 阀芯行程向量** 参数中的元素一一对应。元素按升序列出，并且必须大于 0。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 孔口阀芯行程向量, ds** — 相对于完全关闭位置的阀芯开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* 向量

用于体积流量表格化参数化的阀芯行程距离向量。阀芯行程向量与 **A-B 孔口压降向量, dp** 参数构成独立轴。值按升序列出，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 孔口压降向量, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* 向量

用于体积流量表格化参数化的压降值向量。压降向量与 **A-B 孔口阀芯行程向量, ds** 参数构成独立轴，用于二维因变量 **A-B 孔口体积流量表, q(ds,dp)** 或 **A-B 孔口质量流量表, mdot(ds,dp)** 参数。值按升序列出，并且必须大于 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 孔口体积流量表, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*-by-*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*-by-*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-B 孔口阀芯行程向量, ds** 参数中的向量元素数量。
- *N* 是 **A-B 孔口压降向量, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 孔口质量流量表, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*-by-*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*-by-*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-B 孔口阀芯行程向量, ds** 参数中的向量元素数量。
- *N* 是 **A-B 孔口压降向量, dp** 参数中的向量元素数量。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 恒定孔口面积** — 恒定孔口的横截面积 `1e-4 m^2`（默认）| 正标量

当正、中位和负阀芯位置使用同一孔口时的孔口面积。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 恒定孔口压降向量** — 恒定孔口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* 向量

当正、中位和负阀芯位置使用同一孔口时，阀上的压差值向量。向量元素必须与 **A-B 恒定孔口体积流量向量** 或 **A-B 孔口质量流量表, mdot(ds,dp)** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 恒定孔口体积流量向量** — 恒定孔口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1-by-*n* 向量

当正、中位和负阀芯位置使用同一孔口时，通过阀的体积流量值向量。向量元素必须与 **A-B 恒定孔口压降向量** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### **A-B 恒定孔口质量流量向量** — 恒定孔口质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1-by-*n* 向量

当正、中位和负阀芯位置使用同一孔口时，通过阀的质量流量值向量。向量元素必须与 **A-B 恒定孔口压降向量** 参数中的元素一一对应。值按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

1. **面积特性** 为
   `Different for each flow
   path`。
2. **孔口参数化** 为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   **正阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **中位阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

   **负阀芯位置开启连接** 为：

   - `P-A, P-B,
     A-B`

### A-T 孔口

### **最大 A-T 孔口面积时的阀芯位置** — 完全打开 A-T 孔口时阀芯从中位偏移 `7.5e-3 m`（默认）| 正标量

完全打开 A-T 孔口时阀芯从中位偏移。**中位阀芯位置开启连接一致性检查** 参数将通知您，如果为此阀芯位置设置的值与其他孔口阀芯位置不一致或不符合物理规律。

#### 依赖关系

要启用此参数，请设置以下参数之一：

- **正阀芯位置开启连接** 为 `P-B,
  A-T`。
- **中位阀芯位置开启连接** 为：

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
- **负阀芯位置开启连接** 为 `P-B,
  A-T`。

**注意：**

仅当 A-T 孔口设置未出现在以下三个阀芯位置参数中时，才启用此参数：**正阀芯位置开启连接**、**中位阀芯位置开启连接** 和 **负阀芯位置开启连接**。

### **A-T 孔口在关闭与打开之间的阀芯行程** — 最大阀芯行程 `0.005 m`（默认）| 正标量

最大阀芯行程距离。该值为计算提供上限，使仿真不会返回不符合物理规律的值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认）| positive scalar

A-T 节流口在阀运行期间的最大开启面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T orifice spool travel vector** — 相对于完全关闭位置的滑阀开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于阀面积表格化参数化的滑阀行程距离向量。向量元素必须与 **A-T orifice area vector** 参数中的元素一一对应。值按升序列出，第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T orifice area vector** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认）| 1-by-*n* vector

用于阀开启面积表格化参数化的开启面积向量。向量元素必须与 **A-T spool travel vector** 参数中的元素一一对应。元素按升序列出，并且必须大于 0。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T orifice spool travel vector, ds** — 相对于完全关闭位置的滑阀开启距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1-by-*n* vector

用于体积流量表格化参数化的滑阀行程距离向量。滑阀行程向量与 **A-T orifice pressure drop vector, dp** 参数一起，为二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 或 **A-T orifice mass flow rate table, mdot(ds,dp)** 参数构成独立轴。值按升序列出，第一个元素必须为 0。在表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* vector

用于体积流量表格化参数化的压降值向量。压降向量与 **A-T orifice spool travel vector, ds** 参数一起，为二维因变量 **A-T orifice volumetric flow rate table, q(ds,dp)** 或 **A-T orifice mass flow rate table, mdot(ds,dp)** 参数构成独立轴。值按升序列出，并且必须大于 0。在表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*-by-*N* matrix

基于压降和滑阀行程距离独立值的 *M*-by-*N* 体积流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T orifice spool travel vector, ds** 参数中向量元素的数目。
- *N* 是 **A-T orifice pressure drop vector, dp** 参数中向量元素的数目。

#### 依赖项

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
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*-by-*N* matrix

基于压降和滑阀行程距离独立值的 *M*-by-*N* 质量流量矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **A-T orifice spool travel vector, ds** 参数中向量元素的数目。
- *N* 是 **A-T orifice pressure drop vector, dp** 参数中向量元素的数目。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认）| positive scalar

当正、中、负滑阀位置使用同一节流口时的节流口面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为以下之一：

   - `Linear - Area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的以下设置之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T constant orifice pressure drop vector** — 用于恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1-by-*n* vector

当正、中、负滑阀位置使用同一节流口时，阀上的压差值向量。向量元素与 **A-T constant orifice volumetric flow rate vector** 或 **A-T orifice mass flow rate table, mdot(ds,dp)** 参数中的元素一一对应。值按升序列出。在表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T constant orifice volumetric flow rate vector** — 用于恒定节流口的体积流量值向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认）| 1-by-*n* vector

当正、中、负滑阀位置使用同一节流口时的体积流量值向量。向量元素与 **A-T constant orifice pressure drop vector** 参数中的元素一一对应。值按升序列出。在表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 每个参数中的以下设置之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### **A-T constant orifice mass flow rate vector** — 用于恒定节流口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认）| 1-by-*n* vector

当正、中、负滑阀位置使用同一节流口时，阀上的质量流量值向量。向量元素与 **A-T constant orifice pressure drop vector** 参数中的元素一一对应。值按升序列出。在表格数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 每个参数中的以下设置之一：

   将 **Positive spool position open
   connections** 设置为 `P-B,
   A-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-B,
   A-T`。

### B-T 节流口

### **Spool position at maximum B-T orifice area** — 用于完全打开的 B-T 节流口的、从中间位置的滑阀偏移量 `7.5e-3 m`（默认）| positive scalar

用于完全打开的 B-T 节流口的、从中间位置的滑阀偏移量。如果为该滑阀位置设置的值与其他节流口滑阀位置不一致或不合理，**Consistency check for neutral spool position open connections** 参数将通知您。

#### 依赖项

要启用此参数，请设置以下参数之一：

- 将 **Positive spool position open
  connections** 设置为 `P-A,
  B-T`。
- 将 **Neutral spool position open
  connections** 设置为：

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
- 将 **Negative spool position open
  connections** 设置为 `P-A,
  B-T`。

**注意：**

仅当 B-T 节流口设置未出现在全部三个滑阀位置参数中时，此参数才启用：**Positive spool position open connections**、**Neutral spool position open connections** 和 **Negative spool position open connections**。

### **B-T spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认）| positive scalar

滑阀行程的最大距离。此值为计算提供上限，以便仿真不会返回不合理的值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认）| positive scalar

B-T 节流口在阀运行期间的最大开启面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T orifice spool travel vector** — 相对于完全关闭位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积的表格化参数化的滑阀行程距离向量。向量元素必须与 **B-T orifice area vector** 参数中的元素一一对应。值按升序排列，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T orifice area vector** — 阀开启面积向量 `[1e-10, 1e-05, 4e-05, 6e-05, .0001] m^2`（默认） | 1-by-*n* vector

用于阀开启面积表格化参数化的开启面积向量。向量元素必须与 **B-T orifice spool travel vector** 参数中的元素一一对应。元素按升序排列，且必须大于 0。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T orifice spool travel vector, ds** — 相对于完全关闭位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于体积流量表格化参数化的控制构件行程距离向量。滑阀行程向量与 **B-T orifice pressure drop vector, dp** 参数一起构成独立轴，用于二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 或 **B-T orifice mass flow rate table, mdot(ds,dp)** 参数。值按升序排列，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

用于体积流量表格化参数化的压降值向量。压降向量与 **B-T orifice spool travel vector, ds** 参数一起构成独立轴，用于二维因变量 **B-T orifice volumetric flow rate table, q(ds,dp)** 或 **B-T orifice mass flow rate table, mdot(ds,dp)** 参数。值按升序排列，且必须大于 0。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量值数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认） | *M*-by-*N* matrix

基于压降和滑阀行程距离独立值的体积流量的 *M*-by-*N* matrix。*M* 和 *N* 是相关向量的大小：

- *M* 是 **B-T orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **B-T orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖项

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
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认） | *M*-by-*N* matrix

基于压降和滑阀行程距离独立值的质量流量的 *M*-by-*N* matrix。*M* 和 *N* 是相关向量的大小：

- *M* 是 **B-T orifice spool travel vector, ds** 参数中向量元素的数量。
- *N* 是 **B-T orifice pressure drop vector, dp** 参数中向量元素的数量。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 以下参数之一：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T constant orifice area** — 恒定节流口的横截面积 `1e-4 m^2`（默认） | positive scalar

当正、中、负滑阀位置使用同一节流口时的节流口面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为以下之一：

   - `Linear - Area vs. spool
     travel`
   - `Tabulated data - Area vs. spool
     travel`
3. 每个参数中的某一设置：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T constant orifice pressure drop vector** — 恒定节流口的压差值向量 `[-.1, .3, .5, .7] MPa`（默认） | 1-by-*n* vector

当正、中、负滑阀位置使用同一节流口时，阀门上的压差值向量。向量元素与 **B-T constant orifice volumetric flow rate vector** 或 **B-T orifice mass flow rate table, mdot(ds,dp)** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure drop` 或
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 每个参数中的某一设置：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T constant orifice volumetric flow rate vector** — 恒定节流口的体积流量向量 `[-.0009, .0016, .002, .0024] m^3/s`（默认） | 1-by-*n* vector

当正、中、负滑阀位置使用同一节流口时，阀门上的体积流量值向量。向量元素与 **B-T constant orifice pressure drop vector** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Volumetric flow rate
   vs. spool travel and pressure
   drop`。
3. 每个参数中的某一设置：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### **B-T constant orifice mass flow rate vector** — 恒定节流口的质量流量向量 `[-.9, 1.6, 2, 2.4] kg/s`（默认） | 1-by-*n* vector

当正、中、负滑阀位置使用同一节流口时，阀门上的质量流量值向量。向量元素与 **P-B constant orifice pressure drop vector** 参数中的元素一一对应。值按升序排列。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Mass flow rate vs.
   spool travel and pressure drop`。
3. 每个参数中的某一设置：

   将 **Positive spool position open
   connections** 设置为 `P-A,
   B-T`。

   将 **Neutral spool position open
   connections** 设置为：

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

   将 **Negative spool position open
   connections** 设置为 `P-A,
   B-T`。

### P-T Orifice

### **Spool position at maximum P-T orifice area** — P-T 节流口完全打开时滑阀从中位偏移的距离 `0 m`（默认） | positive scalar

P-T 节流口完全打开时滑阀从中位偏移的距离。如果为此滑阀位置设置的值根据其他节流口滑阀位置不一致或不符合物理，**Consistency check for neutral spool position open connections** 参数将通知您。

#### 依赖项

要启用此参数，请将 **Neutral spool position open connections** 设置为：

- `P-T`
- `P-A, A-T, P-T`
- `P-B, B-T, P-T`
- `P-A, P-B, A-T, B-T, P-T`

### **P-T spool travel between closed and open orifice** — 最大滑阀行程 `0.005 m`（默认） | positive scalar

滑阀行程的最大距离。此值为计算提供上限，以便仿真不会返回非物理值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 将 **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T maximum orifice area** — 最大节流口开启面积 `1e-4 m^2`（默认） | positive scalar

阀门运行期间 P-T 节流口的最大开启面积。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Linear - Area vs. spool
   travel`。
3. 将 **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice spool travel vector** — 相对于完全关闭位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于阀面积表格化参数化的控制构件行程距离向量。向量元素必须与 **P-T orifice area vector** 参数中的元素一一对应。值按升序排列，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 将 **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice spool travel vector, ds** — 相对于完全关闭位置的滑阀开度距离向量 `[0, .00125, .0025, .00375, .005] m`（默认） | 1-by-*n* vector

用于体积流量表格化参数化的控制构件行程距离向量。滑阀行程向量与 **P-T orifice pressure drop vector, dp** 参数一起构成独立轴，用于二维因变量 **P-T orifice volumetric flow rate table, q(ds,dp)** 或 **P-T orifice mass flow rate table, mdot(ds,dp)** 参数。值按升序排列，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. 将 **Area characteristics** 设置为
   `Different for each flow
   path`。
2. 将 **Orifice parameterization** 设置为
   `Tabulated data - Area vs. spool
   travel`。
3. 将 **Neutral spool position open connections** 设置为：

   - `P-T`
   - `P-A, A-T,
     P-T`
   - `P-B, B-T,
     P-T`
   - `P-A, P-B, A-T, B-T,
     P-T`

### **P-T orifice pressure drop vector, dp** — 压差值向量 `[-.1, .3, .5, .7] MPa`（默认）| 1×*n* 向量

用于体积流量表格化参数化的压降值向量。该压降向量与 **P-T orifice spool travel vector, ds** 参数一起形成独立轴，用于二维因变量 **P-T orifice volumetric flow rate table, q(ds,dp)** 或 **P-T orifice mass flow rate table, mdot(ds,dp)** 参数。值按升序列出，且必须大于 0。表数据点之间采用线性插值。

#### 依赖项

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice volumetric flow rate table, q(ds,dp)** — 体积流量数组 `[-1e-08, 2.2e-08, 2.8e-08, 3.4e-08; -9e-06, .00015, .0002, .00024; -.00036, .00063, .00081, .00096; -.00054, .00094, .0012, .0014; -.00091, .0016, .002, .0024] m^3/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离的独立值的体积流量 *M*×*N* 矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-T orifice spool travel vector, ds** 参数中的向量元素数量。
- *N* 是 **P-T orifice pressure drop vector, dp** 参数中的向量元素数量。

#### 依赖项

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Area vs. spool travel`。
3. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### **P-T orifice mass flow rate table, mdot(ds,dp)** — 质量流量值数组 `[-1e-05, 1.7e-05, 2e-05, 2.6e-05; -.009, .0035, .0045, .0053; -.36, .7, .9, 1.06; -.54, 1.96, 2.5, 3; -.91, 6, 7.7, 9.13] kg/s`（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离的独立值的质量流量 *M*×*N* 矩阵。*M* 和 *N* 是相关向量的大小：

- *M* 是 **P-T orifice pressure drop vector, dp** 参数中的向量元素数量。
- *N* 是 **P-T orifice spool travel vector, ds** 参数中的向量元素数量。

#### 依赖项

要启用此参数，请设置：

1. **Area characteristics** 为 `Different for each flow path`。
2. **Orifice parameterization** 为 `Tabulated data - Mass flow rate vs. spool travel and pressure drop`。
3. **Neutral spool position open connections** 为：

   - `P-T`
   - `P-A, A-T, P-T`
   - `P-B, B-T, P-T`
   - `P-A, P-B, A-T, B-T, P-T`

### 故障

### **4-Way 3-Position Directional Valve Area fault** — 对阀门面积故障建模的选项 `Add fault`

对模块中的阀门面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。发生故障时，通常由开口参数化设置的阀门面积将基于 **Spool position when faulted** 参数中指定的值进行设置。

### **Spool position when faulted** — 故障阀门特性 `Positive`（默认）| `Neutral` | `Negative` | `Maintain last value`

故障阀门阀芯位置。您可以选择让阀门在阀芯处于正位置、负位置或故障触发时的位置时卡死。

#### 依赖项

要启用此参数，请点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

4-Way 3-Position Directional Valve (TL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2022b：右键点击模块以查看开口特性图

您可以右键点击模块并选择 **Fluids** > **Plot Valve Characteristics**，查看每个节流口的面积或体积流量相对于阀芯位置的图。

## 描述

用于在热液体网络的四条线路交汇处引导流动的阀

4-Way 3-Position Directional Valve (TL) 模块在热液体网络中为一个具有四个开口的阀建模，通常位于执行器、泵和油箱之间。阀门操作由单个阀芯控制，该阀芯根据端口 **S** 处的信号发生位移。您可以通过在 **Neutral spool position open connections** 参数中指定当阀芯处于中位（以 0 m 为中心）时打开的节流口，在 **Positive spool position open connections** 参数中指定当阀芯向正方向移动时打开的节流口，以及在 **Negative spool position open connections** 参数中指定当阀芯向负方向移动时打开的节流口，来设置阀门的基线配置。

您可以在 **Orifice parameterization** 参数中将阀门开口模型设置为线性关系或用户提供数据的函数，该模型可应用于阀门中的一个或所有流动路径。

**示例阀门设置**

在此示例配置中，**Neutral spool position open connections** 设置为 `All closed`。当阀芯处于中位时，所有节流口都关闭，无流动：

在此配置中，**Negative spool position open connections** 设置为 `P-A, B-T`。当端口 **S** 处的信号使阀芯移动到负位置时，端口 **P** 和 **A** 之间以及端口 **B** 和 **T** 之间的路径打开，允许流动。端口 **P** 和 **B** 之间以及端口 **A** 和 **T** 之间的路径关闭，不允许流动：

在此配置中，**Positive spool position open connections** 设置为 `P-B, A-T`。当端口 **S** 处的信号使阀芯移动到正位置时，端口 **P** 和 **B** 之间以及端口 **A** 和 **T** 之间的路径打开，允许流动，而端口 **P** 和 **A** 之间以及端口 **B** 和 **T** 之间的路径关闭：

示意性地，此配置如下所示：

左侧对应正位置，右侧对应负位置。

### 阀芯位移和阀配置

*阀芯行程* 是节流口从关闭位置到完全打开所需的阀芯移动量，并针对 **Valve Configuration** 选项卡上选择的每个节流口定义。下表显示了如何根据阀节流口参数化和流路特性计算该行程。

端口 **S** 处信号表示的阀芯运动方向取决于阀芯行程和节流口方向：

**节流口定义和阀芯移动方向**

| 节流口打开时的阀芯位置 | 阀芯移动量，*ΔS* |
| --- | --- |
| 始终关闭（节流口未在任何阀芯位置配置中选择） | N/A |
| 始终打开（节流口在正位、中位和负位阀芯位置配置中均被选择） | N/A |
| 负位 | *S*orifice\_max + 阀芯行程 – **S** |
| 负位和中位 | *S*orifice\_max + 阀芯行程 – **S** |
| 正位 | *S*orifice\_max – 阀芯行程 + **S** |
| 正位和中位 | *S*orifice\_max – 阀芯行程 + **S** |
| 中位 | |*S*orifice\_max| + 阀芯行程 – |**S**| |
| 正位和负位 | –|*S*orifice\_max| + 阀芯行程 – |**S**| |

其中 *S*orifice\_max 是为每个节流口定义的最大节流口面积处的阀芯位置。当 *ΔS* 为负时，节流口面积饱和至泄漏面积；当节流口完全打开时，节流口面积饱和至最大节流口面积。当节流口完全打开时，*ΔS* 等于阀芯行程，因此 *ΔS* 大于阀芯行程不会进一步增大节流口面积。

**Consistency check for neutral spool position open connections** 参数验证：

- 在 **Neutral spool position open connections** 中列出的任何节流口在 **S** 处信号为 0 时均打开。
- 未在 **Neutral spool position open connections** 中列出的任何节流口在 **S** 处信号为 0 时均关闭。

你可以选择在此检查被违反时接收警告或错误。

4-Way 3-Position Directional Valve (TL) 模块的可能配置如下所示。

**4-Way 3-Position Directional Valve 配置**

| 配置 | 参数值 |
| --- | --- |
|  | 在中位时四个节流口均关闭。（默认）  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `All closed` - **Negative spool position open connections**: `P-B, A-T`    - **Spool position at maximum P-A orifice area** > P-A spool stroke - **Spool position at maximum P-B orifice area** < –P-B spool stroke - **Spool position at maximum A-T orifice area** < –A-T spool stroke - **Spool position at maximum B-T orifice area** > B-T spool stroke |
|  | 在中位时四个节流口均打开。  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `P-A, P-B, A-T, B-T` - **Negative spool position open connections**: `P-B, A-T`    - **Spool position at maximum P-A orifice area** < P-A spool stroke - **Spool position at maximum P-B orifice area** > –P-B spool stroke - **Spool position at maximum A-T orifice area** > –A-T spool stroke - **Spool position at maximum B-T orifice area** < B-T spool stroke |
|  | 节流口 A-T 和 B-T 关闭。节流口 P-A 和 P-B 重叠。  - **Positive spool position open connections**: `P-A` - **Neutral spool position open connections**: `All closed` - **Negative spool position open connections**: `P-B`    - **Spool position at maximum P-A orifice area** > P-A spool stroke - **Spool position at maximum P-B orifice area** < –P-B spool stroke |
|  | 节流口 A-T 和 B-T 打开。节流口 P-A 和 P-B 重叠。  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `A-T, B-T` - **Negative spool position open connections**: `P-B, A-T`    - **Spool position at maximum P-A orifice area** > P-A spool stroke - **Spool position at maximum P-B orifice area** < –P-B spool stroke - **Spool position at maximum A-T orifice area** > –A-T spool stroke - **Spool position at maximum B-T orifice area** < B-T spool stroke |
|  | 在中位时节流口 P-A 和 A-T 打开。节流口 P-B 和 B-T 重叠。  - **Positive spool position open connections**: `P-B, A-T` - **Neutral spool position open connections**: `P-A, A-T` - **Negative spool position open connections**: `P-A, B-T`    - **Spool position at maximum P-A orifice area** < P-A spool stroke - **Spool position at maximum P-B orifice area** > P-B spool stroke - **Spool position at maximum A-T orifice area** > A-T spool stroke - **Spool position at maximum B-T orifice area** < –B-T spool stroke |
|  | 在中位时节流口 A-T 打开。节流口 P-B、A-T 和 B-T 重叠。  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `A-T` - **Negative spool position open connections**: `P-B, A-T`    - **Spool position at maximum P-A orifice area** > P-A spool stroke - **Spool position at maximum P-B orifice area** < –P-B spool stroke - **Spool position at maximum A-T orifice area** > –A-T spool stroke - **Spool position at maximum B-T orifice area** > B-T spool stroke |
|  | 在中位时节流口 B-T 打开。节流口 P-A、P-B 和 A-T 重叠。  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `B-T` - **Negative spool position open connections**: `P-B, A-T`    - **Spool position at maximum P-A orifice area** > P-A spool stroke - **Spool position at maximum P-B orifice area** < –P-B spool stroke - **Spool position at maximum A-T orifice area** < –A-T spool stroke - **Spool position at maximum B-T orifice area** < B-T spool stroke |
|  | 节流口 P-A、P-B 打开。节流口 A-T 和 B-T 重叠。  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `P-A, P-B` - **Negative spool position open connections**: `P-B, A-T`    - **Spool position at maximum P-A orifice area** < P-A spool stroke - **Spool position at maximum P-B orifice area** > –P-B spool stroke - **Spool position at maximum A-T orifice area** < –A-T spool stroke - **Spool position at maximum B-T orifice area** > B-T spool stroke |
|  | 在中位时节流口 P-A 打开。节流口 P-B、A-T 和 B-T 重叠。  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `P-A` - **Negative spool position open connections**: `P-B, A-T`    - **Spool position at maximum P-A orifice area** < P-A spool stroke - **Spool position at maximum P-B orifice area** < –P-B spool stroke - **Spool position at maximum A-T orifice area** < –A-T spool stroke - **Spool position at maximum B-T orifice area** > B-T spool stroke |
|  | 在中位时节流口 P-B 打开。节流口 P-A、A-T 和 B-T 重叠。  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `P-B` - **Negative spool position open connections**: `P-B, A-T`    - **Spool position at maximum P-A orifice area** > P-A spool stroke - **Spool position at maximum P-B orifice area** > –P-B spool stroke - **Spool position at maximum A-T orifice area** < –A-T spool stroke - **Spool position at maximum B-T orifice area** > B-T spool stroke |
|  | 在中位时节流口 P-B 和 B-T 打开。节流口 P-A 和 A-T 重叠。  - **Positive spool position open connections**: `P-B, A-T` - **Neutral spool position open connections**: `P-B, B-T` - **Negative spool position open connections**: `P-A, B-T`    - **Spool position at maximum P-A orifice area** < –P-A spool stroke - **Spool position at maximum P-B orifice area** < P-B spool stroke - **Spool position at maximum A-T orifice area** > A-T spool stroke - **Spool position at maximum B-T orifice area** > –B-T spool stroke |
|  | 在中位时节流口 P-A、P-B、A-T 和 B-T 关闭。P-T 在中位时打开，并在阀芯移动时关闭。  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `P-T` - **Negative spool position open connections**: `P-B, A-T`    - **Spool position at maximum P-A orifice area** > P-A spool stroke - **Spool position at maximum P-B orifice area** < –P-B spool stroke - **Spool position at maximum A-T orifice area** < –A-T spool stroke - **Spool position at maximum B-T orifice area** > B-T spool stroke - **Spool position at maximum P-T orifice area** = 任意值 |
|  | 节流口 P-A 是恒定节流口。在中位时节流口 P-B、A-T 和 B-T 打开。  - **Positive spool position open connections**: `P-A, P-B` - **Neutral spool position open connections**: `P-A, P-B, A-T, B-T` - **Negative spool position open connections**: `P-A, B-T`    - **Spool position at maximum P-A orifice area** < P-A spool stroke - **Spool position at maximum P-B orifice area** < P-B spool stroke - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T spool stroke |
|  | 节流口 P-B 是恒定节流口。在中位时节流口 P-A、A-T、B-T 打开。    - **Positive spool position open connections**: `P-B, A-T` - **Neutral spool position open connections**: `P-A, P-B, A-T, B-T` - **Negative spool position open connections**: `P-A, P-B`    - **Spool position at maximum P-A orifice area** > –P-A spool stroke - **Spool position at maximum A-T orifice area** < A-T spool stroke - **Spool position at maximum B-T orifice area** = 任意值 |
|  | 在中位时节流口 P-A 关闭。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open connections**: `P-A, P-B` - **Neutral spool position open connections**: `All closed` - **Negative spool position open connections**: `P-A, B-T`  - |**Spool position at maximum P-A orifice area**| > P-A spool stroke - **Spool position at maximum P-B orifice area** > P-B spool stroke - **Spool position at maximum B-T orifice area** < –B-T spool stroke |
|  | 在中位时节流口 P-B 关闭。端口 **B** 和 **T** 不构成流路。  - **Positive spool position open connections**: `P-B, A-T` - **Neutral spool position open connections**: `All closed` - **Negative spool position open connections**: `P-A, P-B`  - **Spool position at maximum P-A orifice area** < –P-A spool stroke - |**Spool position at maximum P-B orifice area**| > P-B spool stroke - **Spool position at maximum A-T orifice area** > A-T spool stroke |
|  | 在中位时节流口 P-A 关闭。在中位时节流口 A-T 打开。  - **Positive spool position open connections**: `P-A, P-B` - **Neutral spool position open connections**: `A-T, B-T` - **Negative spool position open connections**: `P-A, B-T`  - |**Spool position at maximum P-A orifice area**| > P-A spool stroke - **Spool position at maximum P-B orifice area** > P-B spool stroke - **Spool position at maximum A-T orifice area** = 任意值 - **Spool position at maximum B-T orifice area** > –B-T spool stroke |
|  | 在中位时节流口 P-B 关闭。在中位时节流口 B-T 打开。  - **Positive spool position open connections**: `P-B, A-T` - **Neutral spool position open connections**: `A-T, B-T` - **Negative spool position open connections**: `P-A, P-B`  - **Spool position at maximum P-A orifice area** < –P-A spool stroke - |**Spool position at maximum P-B orifice area**| > P-B spool stroke - **Spool position at maximum A-T orifice area** < A-T spool stroke - **Spool position at maximum B-T orifice area** = 任意值 |
|  | 在中位时节流口 P-B 关闭。在中位时节流口 P-T 打开。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open connections**: `P-A, P-B` - **Neutral spool position open connections**: `P-T` - **Negative spool position open connections**: `P-B, A-T`  - **Spool position at maximum P-A orifice area** > P-A spool stroke - |**Spool position at maximum P-B orifice area**| > P-B spool stroke - **Spool position at maximum B-T orifice area** < –B-T spool stroke - **Spool position at maximum P-T orifice area** = 任意值 |
|  | 在中位时节流口 P-A 关闭。在中位时节流口 P-T 打开。端口 **A** 和 **T** 不构成流路。  - **Positive spool position open connections**: `P-A, B-T` - **Neutral spool position open connections**: `P-T` - **Negative spool position open connections**: `P-A, P-B`  - |**Spool position at maximum P-A orifice area**| > P-A spool stroke - **Spool position at maximum P-B orifice area** < –P-B spool stroke - **Spool position at maximum B-T orifice area** > B-T spool stroke - **Spool position at maximum P-T orifice area** = 任意值 |

### 阀门孔口参数化

**Orifice parameterization** 参数设置通过一个或所有阀门孔口的开口面积或体积流量的模型。该模块在 **Area characteristics** 设置为 `Identical for all flow paths` 时对所有流路应用相同数据；否则，对于 `Different for all flow paths` 设置，应用各自的参数化。您可以通过三种方式对阀门开度建模：

- `Linear - Area vs. spool travel`

  开口面积是作为端口 **S** 处信号接收的阀芯位置的线性函数：

  Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

  其中：

  - *ΔS* 是 Spool Displacement and Valve Configuration 中定义的阀芯行程。

    *Aorifice* 在 *ΔS* 为负时饱和于 *Aleak*，并在孔口完全打开时饱和于 *Amax*。当孔口完全打开时，*ΔS* 等于阀芯行程，因此 *ΔS* 大于阀芯行程不会进一步增大孔口面积。
  - *ΔS*max 是 **Spool travel between closed and open orifice**。
  - *A*max 是 **Maximum orifice area**。
  - *A*leak 是 **Leakage area**。

  当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，该模块会在 *Aleak* 和 *Amax* 之间平滑地饱和开口面积。有关详细信息，请参阅 Numerical Smoothing。
- `Tabulated data - Area vs. spool travel`

  为您的系统或端口 **P**、**A**、**B** 和 **T** 之间的各个流路提供阀芯行程向量。此数据将用于计算孔口面积与阀芯位移之间的关系。插值用于确定给定数据点之间的开口面积。*A*leak 和 *A*max 分别是开口面积向量的第一个和最后一个参数。
- `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`

  提供阀芯行程和压降向量以及一个相关的二维体积流量数组。插值用于确定给定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

- `Tabulated data - Mass flow rate vs. spool travel and pressure drop`

  根据控制构件位置和阀门两端压降直接计算质量流量。这三个变量之间的关系可以是非线性的，该模块根据 **Spool travel vector, ds**,**Pressure drop vector, dp**, and **Mass flow rate table, mdot(ds,dp)** 参数中的表格数据计算该关系。

### 可视化孔口开度

要可视化阀芯偏移和最大位移，请右键单击该模块并选择 **Fluids** > **Plot Valve Characteristics**。该图显示在 **Valve Configuration** 设置中选择的孔口。孔口参数化设置坐标轴，坐标轴为以下之一：

- 孔口面积与阀芯位置的关系
- 体积流量与阀芯位置的关系，在特定压差下查询
- 参考流入温度和参考流入压力下的质量流量与阀芯位置的关系，在特定压差下查询

当 **Valve Configuration** 中的 positive、neutral 和 negative 设置使用相同孔口时，该图将孔口开度显示为常量。

更改模块参数后要更新数据，请在图窗上单击 **Reload Data**。

此图像显示了一个示例阀门配置。在 **Valve Configuration** 设置中：

- **Positive spool position open connections** 为 `P-A, B-T`。
- **Neutral spool position open connections** 为 `P-T`。
- **Negative spool position open connections** 为 `P-B, A-T`。

在 **P-A Orifice** 设置中：

- **Spool position at maximum P-A orifice area** 为 `2.5e-3 m`。

所有其他阀芯位置均采用默认值。

每个孔口的面积与阀芯位置关系图。

可视化显示，P-A 孔口在阀芯位置位于 `-2.53e-3` 和 `2.53e-3` m 之间时打开。由于 P-A 孔口仅在阀芯沿正方向位移时打开，将 **Consistency check for neutral spool and position open connections** 参数设置为 `Warning` 会返回：

`Warning: P-A orifice must be closed when the spool is in the
neutral position. Adjust Spool position at maximum P-A orifice area, Neutral
spool position open connections, or Consistency check for neutral spool position
open connections. Right-click on the block and select Fluids > Plot Valve
Characteristics to view the area or flow of each connection versus spool
position.`

要解决此警告，您可以更改：

- 将 **Spool position at maximum P-A orifice area** 改为大于 0.005 m 的值。
- 将 **Consistency check for neutral spool position open connections** 设置为 `None`。
- 通过将 **Neutral spool position open connections** 设置为 `P-A` 来更改阀门配置。

### 复合结构

此模块是一个复合组件，由多个 Orifice (TL) 模块实例组成。有关阀门参数化和模块计算的更多详细信息，请参阅 Orifice (TL) 模块。

### 泄漏流量

关闭阀门的泄漏流量的主要目的是确保热液体网络的任何部分在任何时候都不会与模型的其余部分隔离。此类隔离部分会降低模型的数值稳健性，并可能减慢仿真速度或导致仿真失败。实际阀门中通常存在泄漏流量，但在模型中，其确切值不如它是一个大于零的小数值重要。泄漏流量由 **Leakage area** 模块参数确定。

### 故障

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

**Spool position when faulted** 参数有四个故障选项：

- `Positive` — 阀芯位置冻结在正位置，将 **Positive spool position open connections** 参数指定的流路打开到其最大值。由 **Negative spool position open connections** 和 **Neutral spool position open connections** 参数指定的流路关闭。
- `Neutral` — 阀芯位置冻结在中位，将所有流路打开到其在 0 m 处的指定值。
- `Negative` — 阀芯位置冻结在负位置，将 **Negative spool position open connections** 参数指定的流路打开到其最大值。由 **Positive spool position open connections** 和 **Neutral spool position open connections** 参数指定的流路关闭。
- `Maintain last value` — 触发发生时，阀门冻结在当时的阀芯位置。

由于在线性参数化中阀门面积极值处进行了数值平滑，该模块使用的最小面积大于 **Leakage area**，最大面积小于 **Maximum orifice area**，与 **Smoothing factor** 值成比例。有关详细信息，请参阅 Numerical Smoothing。

故障触发后，阀门在其后整个仿真过程中保持处于故障面积。

### 预定义参数化

您可以使用预参数化的制造数据填充该模块，这允许您对特定供应商组件建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的 "<click to select>" 超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个零件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。该模块现在具有您指定的参数化。
4. 您可以通过在 Block Parameterization Manager 窗口中选择一个零件并在 **Compare selected part with block** 部分查看数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用数据源提供参数值。该模块用工程判断和简化假设替代缺失数据。因此，预期仿真与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并按需细化组件模型。

要了解更多信息，请参阅 List of Pre-Parameterized Components。
