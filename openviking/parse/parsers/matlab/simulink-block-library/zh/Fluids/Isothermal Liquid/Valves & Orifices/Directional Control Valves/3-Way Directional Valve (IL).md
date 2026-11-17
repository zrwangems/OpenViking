---
type: simulink-block
title: '3-Way Directional Valve (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: '3waydirectionalvalveil'
documentation_source_path: 'ref/3waydirectionalvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# 3-Way Directional Valve (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

阀门出口。

### **P** — 液体端口 isothermal liquid

阀门入口。

### **T** — 液体端口 isothermal liquid

阀门的入口或出口。

### 输入

### **S** — 控制构件位移，m physical signal

阀芯位置位移，以 m 为单位，作为 physical signal 接收。对于在正阀芯位置打开的流路，正信号打开孔口。对于在负阀芯位置打开的流路，负信号打开孔口。

## 参数

### 模型参数化

### **正阀芯位置打开连接** — 当阀芯处于正位置时流路打开 `P-T`（默认） | `All closed` | `P-A, A-T, P-T` | `P-A` | `A-T`

当阀芯处于正位置时流路打开。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### **负阀芯位置打开连接** — 当阀芯沿负方向运动时流路打开 `P-A`（默认） | `All closed` | `P-A, A-T, P-T` | `A-T` | `P-T`

当阀芯沿负方向运动时流路打开。此参数设置阀门配置，并根据端口 **S** 接收的信号定义阀芯运动方向。

### **面积特性** — 孔口的流量方程 `Identical for all flow paths`（默认） | `Different for each flow path`

为阀门孔口面积应用统一或单独的流量方程。`Identical for all flow paths` 对所有阀门孔口使用相同的孔口和阀芯几何、流量、压力和面积向量。使用 `Different for each flow path` 时，会将不同的阀芯偏移和表格数据分配给端口 **P** 与 **A**、端口 **A** 与 **T**、以及端口 **P** 与 **T** 之间的孔口。在两种情况下，端口 **A**、**P** 和 **T** 具有相同的横截面积、流量系数和雷诺数。同样的 **孔口参数化** 也会应用于所有流路。

### **孔口参数化** — 计算开口面积的方法 `Linear area vs. spool travel`（默认） | `Tabulated data - Area vs. spool travel` | `Tabulated data - volumetric flow rate vs. spool travel and pressure drop`

计算阀门开口面积的方法。在表格数据参数化中，可以为非线性阀门开口曲线提供自己的阀门面积和阀芯行程数据，也可以提供以体积流量、阀芯行程和流路压降表示的数据。

### **关闭和打开孔口之间的阀芯行程** — 最大阀芯行程 `0.005` m（默认） | positive scalar

阀芯行程的最大距离。此值为计算提供上限，以便仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`。

### **最大孔口面积** — 最大孔口开口面积 `1e-4` m^2（默认） | positive scalar

阀门运行期间的最大开口面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`。

### **端口 A、P 和 T 处的横截面积** — 阀门入口或出口处的面积 `inf` m^2（默认） | positive scalar

入口和出口端口 **A**、**P** 和 **T** 处的横截面积。这些面积用于确定通过阀门的体积流量的压力-流量方程。

### **泄漏面积** — 完全关闭位置时的间隙面积 `1e-10` m^2（默认） | positive scalar

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持在指定的泄漏面积。这通过保持流量连续性来帮助数值稳定性。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Linear - area vs. spool travel`。

### **流量系数** — 流量系数 `0.64`（默认） | positive scalar

用于考虑理论流动中排出损失的修正因子。

### **临界雷诺数** — 层流的上限雷诺数 `150`（默认） | positive scalar

通过阀门的层流的上限雷诺数。

### **平滑因子** — 数值平滑因子 `0.01`（默认） | positive scalar in the range [0,1]

连续平滑因子，当阀门处于接近打开和接近关闭位置时，基于流量响应引入一层渐变变化。为了提高在这些工况下的仿真稳定性，请将此参数设置为小于 1 的非零值。

### **压力恢复** — 是否考虑面积扩大时的压力增加 `on`（默认） | `off`

选择此项以考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

### **阀芯行程向量** — 阀门开口距离向量 `[0, .00125, .0025, .00375, .005]`m（默认） | 1-by*n* vector

用于阀门面积表格参数化的控制构件行程距离向量。向量元素必须与 **孔口面积向量** 参数中的元素一一对应。这些值按升序列出，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **孔口面积向量** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 8e-05, .0001]`m^2（默认） | 1-by*n* vector

用于阀门开口面积表格参数化的开口面积向量。向量元素必须与 **阀芯行程向量** 参数中的元素一一对应。这些元素按升序列出，并且必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **开口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **阀芯行程向量, ds** — 阀门开口距离向量 `[0, .00125, .0025, .00375, .005]`m（默认） | 1-by-*n* vector

用于体积流量表格参数化的控制构件行程距离向量。阀芯行程向量与 **压降向量, dp** 参数一起为三维因变量 **体积流量表, q(ds,dp)** 参数构成一个独立轴。正位移对应于阀门打开。这些值按升序列出，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Volumetric flow rate vs. spool travel and pressure drop`。

### **压降向量, dp** — 阀门压降值向量 `[-.1, .3, .5, .7]` MPa（默认） | 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **阀芯行程向量, s** 参数一起为三维因变量 **体积流量表, q(ds,dp)** 参数构成一个独立轴。这些值按升序列出，并且必须大于 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Volumetric flow rate vs. spool travel and pressure drop`。

### **体积流量表, q(ds,dp)** — 体积流量数组 `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239]` m^3/s（默认） | *M*-by-*N* matrix

基于压降和阀芯行程距离独立值的 *M*-by-*N* matrix，包含体积流量。*M* 和 *N* 是相应向量的大小：

- *M* 是 **阀芯行程向量, ds** 参数中的元素数。
- *N* 是 **压降向量, dp** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Identical for all flow paths`，并将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### P-A 孔口

### **最大 P-A 孔口面积处的阀芯位置** — 端口 P 和 A 之间最大面积处的阀芯偏移 `4.5e-3` m（默认） | scalar

端口 **P** 和 **A** 之间的初始孔口打开距离。默认值表示一个负重叠系统。

- 如果 **最大孔口面积处的阀芯位置** 的幅值小于 **关闭和打开孔口之间的阀芯行程** 的值，则孔口为负重叠，即当阀芯位置等于 0 m 时部分打开。
- 如果 **最大孔口面积处的阀芯位置** 的幅值大于 **关闭和打开孔口之间的阀芯行程** 的值，则孔口为正重叠。这意味着阀门在一段阀芯位置范围内保持关闭。
- 如果 **最大孔口面积处的阀芯位置** 的幅值等于 **关闭和打开孔口之间的阀芯行程** 的值，则孔口为零重叠。这意味着当阀芯位置等于 0 时阀门关闭，并且一旦阀芯位置改变就开始打开。

### **P-A 关闭和打开孔口之间的阀芯行程** — 端口 P 和 A 之间阀芯的最大行程 `0.005` m（默认） | positive scalar

端口 **P** 和 **A** 之间孔口的阀芯行程最大距离。此值为计算提供上限，以便仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`。

### **P-A 最大孔口面积** — 端口 P 和 A 之间的最大面积 `1e-4` m^2（默认） | positive scalar

端口 **P** 和 **A** 之间孔口在完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **孔口参数化** 设置为 `Linear - area vs. spool travel`。

### **P-A 孔口阀芯行程向量** — 阀门开口距离向量 `[0, .00125, .0025, .00375, .005]`m（默认） | 1-by*n* vector

用于阀门面积表格参数化的控制构件行程距离向量。向量元素必须与 **P-A 孔口面积向量** 参数中的元素一一对应。这些值按升序列出，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **孔口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **P-A 孔口面积向量** — 阀门开口面积向量 `[1e-10, 1e-05, 4e-05, 8e-05, .0001]`m^2（默认） | 1-by-*n* vector

用于阀门开口面积表格参数化的开口面积向量。向量元素必须与 **P-A 孔口阀芯行程向量** 参数中的元素一一对应。这些元素按升序列出，并且必须大于 0。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **开口参数化** 设置为 `Tabulated data - Area vs. spool travel`。

### **P-A 孔口阀芯行程向量, ds** — 阀门开口距离向量 `[0, .00125, .0025, .00375, .005]`m（默认） | 1-by-*n* vector

用于体积流量表格参数化的控制构件行程距离向量。阀芯行程向量与 **P-A 孔口压降向量, dp** 参数一起为三维因变量 **P-A 孔口体积流量表, q(s,dp)** 参数构成一个独立轴。正位移对应于阀门打开。这些值按升序列出，第一个元素必须为 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **P-A 孔口压降向量, dp** — 阀门上的压降值向量 `[-.1, .3, .5, .7]` MPa（默认） | 1-by-*n* vector

用于体积流量表格参数化的压降值向量。压降向量与 **P-A 孔口阀芯行程向量, s** 参数一起为三维因变量 **P-A 孔口体积流量表, q(s,dp)** 参数构成一个独立轴。这些值按升序列出，并且必须大于 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### **P-A 孔口体积流量表, q(ds,dp)** — 阀门体积流量向量 `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239]` m^3/s（默认） | *M*-by-*N* matrix

基于压降和阀芯行程距离独立值的 *M*-by-*N* matrix，包含体积流量。*M* 和 *N* 是相应向量的大小：

- *M* 是 **P-A 孔口阀芯行程向量, ds** 参数中的元素数。
- *N* 是 **P-A 孔口压降向量, dp** 参数中的元素数。

#### 依赖关系

要启用此参数，请将 **面积特性** 设置为 `Different for each flow path`，并将 **孔口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. spool travel and pressure drop`。

### A-T 孔口

### **最大 A-T 孔口面积处的阀芯位置** — 端口 A 和 T 之间最大面积处的阀芯偏移 `-4.5e-3` m（默认） | scalar

端口 **A** 和 **T** 之间的初始孔口打开距离。默认值表示一个负重叠系统。

- 如果 **最大孔口面积处的阀芯位置** 的幅值小于 **关闭和打开孔口之间的阀芯行程** 的值，则孔口为负重叠，即当阀芯位置等于 0 m 时部分打开。
- 如果 **最大孔口面积处的阀芯位置** 的幅值大于 **关闭和打开孔口之间的阀芯行程** 的值，则孔口为正重叠。这意味着阀门在一段阀芯位置范围内保持关闭。
- 如果 **最大孔口面积处的阀芯位置** 的幅值等于 **关闭和打开孔口之间的阀芯行程** 的值，则孔口为零重叠。这意味着当阀芯位置等于 0 时阀门关闭，并且一旦阀芯位置改变就开始打开。

### **A-T 关闭和打开孔口之间的阀芯行程** — 端口 A 和 T 之间阀芯的最大行程 `0.005` m（默认） | positive scalar

端口 **A** 和 **T** 之间孔口的阀芯行程最大距离。此值为计算提供上限，以便仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **面积特性** 类型设置为 `Different for each flow path`。

### **A-T maximum orifice area** — 端口 A 和 T 之间的最大面积 `1e-4` m^2（默认）| 正标量

节流孔在完全打开位置时端口
**A** 和 **T** 之间的横截面积。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Linear - area vs.
spool travel`。

### **A-T orifice spool travel vector** — 阀门打开距离向量 `[0, .00125, .0025, .00375, .005]`m（默认）| 1×*n* 向量

用于阀门面积表格参数化的控制构件行程距离向量。向量元素必须与
**A-T orifice area vector** 参数中的元素一一对应。这些值按升序列出，
第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Area vs. spool travel`。

### **A-T orifice area vector** — 阀门打开面积向量 `[1e-10, 1e-05, 4e-05, 8e-05, .0001]`m^2（默认）| 1×*n* 向量

用于阀门打开面积表格参数化的打开面积向量。向量元素必须与
**A-T orifice spool travel vector** 参数中的元素一一对应。这些元素按升序列出，
且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Opening
parameterization** 设置为 `Tabulated data -
Area vs. spool travel`。

### **A-T orifice spool travel vector, ds** — 阀门打开距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格参数化的控制构件行程距离向量。阀芯行程向量与
**A-T orifice pressure drop vector, dp** 参数一起构成
3-D 因变量 **A-T orifice volumetric flow rate table,
q(ds,dp)** 参数的独立轴。正位移对应于阀门打开。这些值按升序列出，
第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`。

### **A-T orifice pressure drop vector, dp** — 阀门上的压降值向量 `[-.1, .3, .5, .7]` MPa（默认）| 1×*n* 向量

用于体积流量表格参数化的压降值向量。压降向量与 **A-T
orifice spool travel vector, s** 参数一起构成
3-D 因变量 **A-T orifice volumetric flow rate table,
q(ds,dp)** 参数的独立轴。这些值按升序列出，
且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`。

### **A-T orifice volumetric flow rate table, q(ds,dp)** — 用于表格参数化的体积流量向量 - 不同流路 `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239]` m^3/s（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。
*M* 和 *N* 是相应向量的大小：

- *M* 是 **A-T orifice spool travel vector,
  ds** 参数中的元素数量。
- *N* 是 **A-T orifice pressure drop vector,
  dp** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`。

### P-T 节流孔

### **Spool position at maximum P-T orifice area** — 端口 P 和 T 之间最大面积时的阀芯偏移 `4.5e-3` m（默认）| 标量

端口 **P** 和 **T** 之间的初始节流孔打开距离。默认值表示一个负重叠系统。

- 如果 **Spool position at maximum
  orifice area** 的幅值小于
  **Spool travel between closed and open
  orifice** 的值，则节流孔为负重叠，即当阀芯位置等于 0 m 时部分打开。
- 如果 **Spool position at maximum
  orifice area** 的幅值大于
  **Spool travel between closed and open
  orifice** 的值，则节流孔为正重叠。这意味着阀门在一段阀芯位置范围内保持关闭。
- 如果 **Spool position at maximum
  orifice area** 的幅值等于
  **Spool travel between closed and open
  orifice** 的值，则节流孔为零重叠。这意味着当阀芯位置等于 0 时阀门关闭，
  并且一旦阀芯位置变化就开始打开。

### **P-T spool travel between closed and open orifice** — 端口 P 和 T 之间阀芯的最大行程 `0.005` m（默认）| 正标量

端口 **P** 和 **T** 之间节流孔的阀芯行程最大距离。
此值提供计算的上限，以使仿真不会返回非物理值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 类型设置为 `Different for
each flow path`。

### **P-T maximum orifice area** — 端口 P 和 T 之间的最大面积 `1e-4` m^2（默认）| 正标量

节流孔在完全打开位置时端口
**P** 和 **T** 之间的横截面积。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Linear - area vs.
spool travel`。

### **P-T orifice spool travel vector** — 阀门打开距离向量 `[0, .00125, .0025, .00375, .005]`m（默认）| 1×*n* 向量

用于阀门面积表格参数化的控制构件行程距离向量。向量元素必须与
**P-T orifice area vector** 参数中的元素一一对应。这些值按升序列出，
第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Area vs. spool travel`。

### **P-T orifice area vector** — 阀门打开面积向量 `[1e-10, 1e-05, 4e-05, 8e-05, .0001]`m^2（默认）| 1×*n* 向量

用于阀门打开面积表格参数化的打开面积向量。向量元素必须与
**P-T orifice spool travel vector** 参数中的元素一一对应。这些元素按升序列出，
且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Opening
parameterization** 设置为 `Tabulated data -
Area vs. spool travel`。

### **P-T orifice spool travel vector, ds** — 阀门打开距离向量 `[0, .00125, .0025, .00375, .005] m`（默认）| 1×*n* 向量

用于体积流量表格参数化的控制构件行程距离向量。阀芯行程向量与
**P-T orifice pressure drop vector, dp** 参数一起构成
3-D 因变量 **P-T orifice volumetric flow rate table,
q(ds,dp)** 参数的独立轴。正位移对应于阀门打开。这些值按升序列出，
第一个元素必须为 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`。

### **P-T orifice pressure drop vector, dp** — 阀门上的压降值向量 `[-.1, .3, .5, .7]` MPa（默认）| 1×*n* 向量

用于体积流量表格参数化的压降值向量。压降向量与 **P-T
orifice spool travel vector, ds** 参数一起构成
3-D 因变量 **P-T orifice volumetric flow rate table,
q(ds,dp)** 参数的独立轴。这些值按升序列出，
且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`。

### **P-T orifice volumetric flow rate table, q(ds,dp)** — 用于表格参数化的体积流量向量 - 不同流路 `[-9.05e-10, 1.57e-09, 2.02e-09, 2.39e-09; -9.05e-05, .000157, .000202, .000239; -.000362, .000627, .00081, .000958; -.000724, .00125, .00162, .00192; -.000905, .00156, .002, .00239]` m^3/s（默认）| *M*×*N* 矩阵

基于压降和阀芯行程距离独立值的 *M*×*N* 体积流量矩阵。
*M* 和 *N* 是相应向量的大小：

- *M* 是 **P-T orifice spool travel vector,
  ds** 参数中的元素数量。
- *N* 是 **P-T orifice pressure drop vector,
  dp** 参数中的元素数量。

#### 依赖关系

要启用此参数，请将 **Area
characteristics** 设置为 `Different for each
flow path`，并将 **Orifice
parameterization** 设置为 `Tabulated data -
Volumetric flow rate vs. spool travel and pressure
drop`。

### 故障

### **3-Way Directional Valve Area fault** — 用于对阀门面积故障建模的选项 `Add fault`

用于在该模块中对阀门面积故障建模的选项。要添加故障，请点击 **Add
fault** 超链接。发生故障时，通常由开度参数化设置的阀门面积将基于
**Spool position when faulted**
参数中指定的值进行设置。

### **Spool position when faulted** — 故障时阀门特性 `Positive`（默认）| `Negative` | `Maintain last value`

故障时的阀门阀芯位置。您可以选择让阀门在阀芯处于正位置、负位置或
故障触发时的位置时锁止。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

3-Way Directional Valve (IL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

等温液体系统中的三通流量控制阀

3-Way Directional Valve (IL) 模块对等温液体网络中的具有三个开口的阀门进行建模，
通常位于执行器、泵和油箱之间。阀门操作由单个阀芯控制，该阀芯根据端口
**S** 处的信号发生位移。您可以通过分别在
**Positive spool position open connections**
和 **Negative spool position open connections** 参数中指定当阀芯沿正方向和
负方向移动时打开的节流孔，来设置阀门的基准配置。

您可以在 **Orifice parameterization**
参数中将阀门开度模型设置为线性关系或用户提供数据的函数，该模型可应用于阀门中的一个或所有流路。

示例阀门配置示意图

在此配置中，**Positive spool position open connections** 设置为
`A-T`。当端口 **S** 处的信号使阀芯移动到正位置时，端口 **A** 和
**T** 之间的路径打开以允许流动。端口
**P** 和 **A** 之间以及端口
**P** 和 **T** 之间的路径关闭：

显示端口 A 和 T 之间流动且端口 P 关闭的示意图

在此配置中，**Negative spool position open connections** 设置为
`P-A`。当端口 **S** 处的信号使阀芯移动到负位置时，端口 **P** 和
**A** 之间的路径打开以允许流动，端口
**T** 和 **A** 之间以及端口
**P** 和 **T** 之间的路径关闭：

显示端口 A 和 P 之间流动且端口 T 关闭的示意图

您可以通过将 **Positive spool position open connections** 或
**Negative spool position open connections** 设置为
`P-T` 或 `P-A, A-T, P-T` 来打开端口 **P** 和 **T** 之间的路径。

一个流路可以在正或负阀芯位置打开，但不能同时在两者中打开。

### 阀门节流孔参数化

**Orifice parameterization** 设置用于计算阀门打开面积的方法。
计算基于节流孔参数或 **Model Parameterization** 选项卡中指定的表格数据集。
如果 **Area characteristics** 设置为 `Identical for all flow
paths`，则该模块对所有流路使用相同数据；否则，在
`Different for all flow paths` 设置中应用各自的值。节流孔参数化包括：

- `Linear - area vs. spool travel`

  打开面积是阀芯行程距离和端口 **S** 处接收到的信号的线性函数：

  Aorifice=(Amax−Aleak)ΔSmaxΔS+Aleak,

  其中：

  - *A*max 是
    **Maximum orifice area**。
  - *A*leak 是
    **Leakage area**。
  - *ΔS*max 是
    **Spool travel between closed and open
    orifice**。
  - *ΔS* 是阀芯行程距离。对于在正位置打开的流路：

    ΔS=Sorifice\_max−ΔSmax+S,

    对于在负位置打开的流路：

    ΔS=Sorifice\_max+ΔSmax−S,

    其中
    *Sorifice\_max*
    是 **Spool position at maximum orifice
    area**。

  在线性参数化中，当阀门处于接近打开或接近关闭位置时，您可以通过调整
  **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing
  factor** 参数非零，则该模块会在 *Aleak* 和
  *Amax* 之间平滑地饱和打开面积。有关详细信息，请参阅 Numerical Smoothing。
- `Tabulated data - Area vs. spool travel`

  为您的系统或端口 **P** 和 **A**、
  **A** 和 **T**、以及
  **P** 和 **T** 之间的各个流路提供阀芯行程向量。此数据将用于计算
  节流孔打开面积与阀芯行程距离之间的关系。插值用于确定给定数据点之间的打开面积。
  *A*leak 和 *A*max 分别是
  **Opening area vector** 的第一个和最后一个参数。
- `Tabulated data - Volumetric flow rate vs. spool travel and
  pressure drop`

  提供阀芯行程和压降向量。体积流量基于压力变化与阀芯行程距离之间的关系计算。
  插值用于确定给定数据点之间的流量。质量流量是体积流量与局部密度的乘积。

### 可视化孔口开度

要可视化阀芯偏移量和位移，请右键单击该模块，然后选择 **Fluids** > **Plot Valve Characteristics**。该图显示在 **Valve Configuration** 设置中选择的孔口。参数化选择设置坐标轴，坐标轴为以下之一：

- 孔口面积与阀芯位置的关系
- 体积流量与阀芯位置的关系，在特定压差下查询

更改模块参数后，要更新数据，请单击图形窗口上的 **Reload Data**。

此图显示一个示例阀配置。在 **Valve Configuration** 设置中：

- **Positive spool position open connections** 为 `P-A`。
- **Negative spool position open connections** 为 `A-T`。

所有其他阀芯位置均为默认值。

每个孔口的面积与阀芯位置关系图

### 故障

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

**Spool position when faulted** 参数有三个故障选项：

- `Positive` — 阀芯位置冻结在正位置，并且由 **Positive spool position open connections** 参数指定的流动路径打开到其最大值。由 **Negative spool position open connections** 参数指定的流动路径关闭。
- `Negative` — 阀芯位置冻结在正位置，并且由 **Negative spool position open connections** 参数指定的流动路径打开到其最大值。由 **Positive spool position open connections** 参数指定的流动路径关闭。
- `Maintain last value` — 触发发生时，阀冻结在阀芯位置。

由于在阀面积极值处进行数值平滑，在线性参数化中，该模块使用的最小面积大于 **Leakage area**，最大面积小于 **Maximum orifice area**，其差值与 **Smoothing factor** 值成比例。有关详细信息，请参阅 Numerical Smoothing。

故障触发后，阀在仿真的剩余时间内保持在故障面积。

### 预定义参数化

提供带有制造商数据的 3-Way Directional Valve (IL) 模块预参数化。此数据允许您对特定供应商组件进行建模。

要加载预定义参数化：

1. 单击 3-Way Directional Valve (IL) 模块对话框描述中的 "Select a predefined parameterization" 超链接。
2. 从下拉菜单中选择一个部件，然后单击 **Update block with selected part**。
3. 如果在加载参数化后更改任何参数设置，您可以通过单击 **Compare block settings with selected part** 检查所做更改。模块与预定义参数化之间的任何设置差异都将显示在 MATLAB® 命令窗口中。

请注意，对于控制元件的正位移和负位移，无法为同一孔口设置不同的值。此外，开口面积围绕中立位置镜像。

**注意**

Simscape™ 组件的预定义参数化使用可用的数据源来提供参数值。使用工程判断和简化假设来填补缺失数据。因此，应预期仿真行为与实际物理行为之间存在偏差。为确保所需精度，您应根据实验数据验证仿真行为，并根据需要细化组件模型。

### 假设

- 忽略流体惯性。
- 忽略由惯性力、弹簧力和其他力引起的阀芯载荷。
- 除非另有指定，否则假定所有阀孔口尺寸相同。
