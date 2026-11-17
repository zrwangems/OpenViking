---
type: simulink-block
title: 'Turbine (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Fluid Machines'
documentation_page: 'turbine2p'
documentation_source_path: 'ref/turbine2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Turbine (2P)

## 端口

### 输入

### **VN** — 喷嘴开度分数，无量纲物理信号

可变喷嘴开度分数，指定为无量纲物理信号。修正质量流量与 **VN** 的值成线性比例关系。分数 `1` 对应于表格数据。喷嘴开度分数不影响等熵效率。

#### 依赖关系

要启用此端口，请选择 **Model variable nozzle** 参数。
### 守恒

### **A** — 两相流体入口 两相流体

与流体入口端口关联的两相流体守恒端口。

### **B** — 两相流体出口 两相流体

与流体出口端口关联的两相流体守恒端口。

### **C** — 涡轮壳体 机械平移

与涡轮壳体关联的端口。

### **R** — 涡轮轴 机械平移

与涡轮轴扭矩和角速度关联的端口。

## 参数

### 涡轮特性图

### **Turbine map parameterization** — 性能参数化方式 `Analytical - Nominal pressure ratio and corrected mass flow rate`（默认）| `Tabulated data - Flow rate and efficiency vs. pressure ratio` | `Tabulated data - Flow rate and efficiency vs. corrected speed and pressure ratio`

性能参数化方式指定：

- `Analytical - Nominal pressure ratio and corrected mass flow
  rate`：以解析方式参数化涡轮等熵效率和修正质量流量。
- `表格数据 - 流量和效率与压力的关系
  ratio`：按压力比参数化涡轮等熵效率和修正质量流量。
- `表格数据 - 流量和效率与校正转速的关系
  and pressure ratio`：按修正转速和压力比参数化涡轮等熵效率和修正质量流量。

### **Model variable nozzle** — 是否启用可变喷嘴输入端口 `Off`（默认）| `On`

是否启用可变喷嘴输入端口 **VN**。当不启用 **VN** 端口时，喷嘴保持恒定值为 `1`。

### **Minimum nozzle opening fraction** — 最小开度分数 `1e-3`（默认）| (0,1] 范围内的正标量

最小喷嘴开度分数。该值是 **VN** 处信号的下边界。模块将该参数的值乘以质量流量，以获得通过涡轮的最小修正质量流量。

#### 依赖关系

要启用此参数，请选择 **Model variable
nozzle**。

### **Maximum nozzle opening fraction** — 最大开度分数 `1`（默认）| (0,1] 范围内的正标量

最大喷嘴开度分数。该值是 **VN** 处信号的上边界。模块将该参数的值乘以质量流量，以获得通过涡轮的最大修正质量流量。

#### 依赖关系

要启用此参数，请选择 **Model variable
nozzle**。

### **Report when fluid is not fully vapor** — 流体未完全汽化时的通知方式 `None`（默认）| `Warning` | `Error`

当模块检测到流体未完全汽化时，模块是不执行任何操作、生成警告还是生成错误。

### **Corrected speed index vector, N** — 表格数据轴转速索引 `250 .* [50, 60, 70, 80, 90, 100, 110]` rpm（默认）| 正标量向量

用于修正质量流量和等熵效率表格参数化的恒定轴转速向量。

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization**
设置为 `Tabulated data - Flow rate and efficiency vs. corrected speed and
pressure ratio`。

### 流量数据

### **Nominal pressure ratio** — 压力比值 `2`（默认）| 正标量

解析参数化中额定工况下的压力比值。

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization**
设置为 `Analytical - Nominal pressure ratio and corrected mass flow
rate`。

### **Nominal corrected mass flow rate** — 修正质量流量值 `0.48` kg/s（默认）| 正标量

解析参数化中额定工况下的修正质量流量值。

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization**
设置为 `Analytical - Nominal pressure ratio and corrected mass flow
rate`。

### **Pressure ratio vector, pr** — 压力比向量 `[1.251, 1.345, 1.442, 1.521, 1.596, 1.692, 1.849, 1.972, 2.1, 2.173, 2.259, 2.3424]`（默认）| 正标量向量

用于修正质量流量表格参数化的压力比值向量。该向量必须与 **Corrected mass flow rate vector, mdot(pr)** 参数具有相同数量的元素，且所有元素必须大于 1。最后一个元素必须是堵塞工况下的压力比。

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization**
设置为 `Tabulated data - Flow rate and efficiency vs. pressure
ratio`。

### **Corrected mass flow rate vector, mdot(pr)** — 修正质量流量值向量 `0.01.*[39.439, 43.01, 45.556, 46.801, 47.792, 48.388, 48.634, 48.67, 48.689, 48.747, 48.825, 48.912]` kg/s（默认）| 正标量向量

用于修正质量流量表格参数化的修正质量流量值向量。该向量必须与 **Pressure ratio vector, pr** 参数具有相同数量的元素，且所有元素必须大于 0。最后一个元素必须是堵塞工况下的修正质量流量。

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization**
设置为 `Tabulated data - Flow rate and efficiency vs. pressure
ratio`。

### **Pressure ratio table, pr(N,beta)** — 涡轮特性图压力比数据 *M*×*N* 矩阵（默认）

在指定修正轴转速和 β 值下的涡轮出口-入口压力比 *M*×*N* 矩阵。模块在表格元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Corrected speed index vector, N** 参数中向量元素的数量。
- *N* 是表格中 β 索引的数量。

默认表格值为：

`[1.217, 1.285, 1.323, 1.363, 1.402, 1.427, 1.495, 1.545, 1.6, 1.687,
1.747, 1.8074; 1.231, 1.302, 1.356, 1.404, 1.443, 1.473, 1.525, 1.577, 1.635, 1.709,
1.782, 1.845; 1.242, 1.328, 1.388, 1.437, 1.528, 1.617, 1.704, 1.811, 1.915, 1.979,
2.053, 2.1226; 1.244, 1.339, 1.417, 1.465, 1.528, 1.584, 1.692, 1.787, 1.899, 2,
2.075, 2.1492; 1.245, 1.34, 1.425, 1.492, 1.546, 1.684, 1.748, 1.882, 1.987, 2.084,
2.167, 2.2458; 1.251, 1.345, 1.442, 1.521, 1.596, 1.692, 1.849, 1.972, 2.1, 2.173,
2.259, 2.3424; 1.248, 1.348, 1.447, 1.516, 1.581, 1.651, 1.749, 1.839, 1.93, 2.024,
2.154, 2.242]`

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization**
设置为 `Tabulated data - Flow rate and efficiency vs. corrected speed and
pressure ratio`。

### **Corrected mass flow rate table, mdot(N,beta)** — 涡轮特性图修正质量流量数据 *M*×*N* 矩阵（默认）

在指定的修正轴转速和 β 值下的修正质量流量 *M*×*N* 矩阵。该模块在表格元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Constant speed index vector, N** 参数中向量元素的数量。
- *N* 是表格中 β 索引的数量。

默认表格值为：

`0.01.*[40.403, 44.417, 46.653, 47.966, 48.97, 49.544, 50.001, 50.081,
50.086, 50.095, 50.09, 50.0922; 40.044, 43.754, 46.125, 47.626, 48.513, 49.105,
49.481, 49.58, 49.597, 49.624, 49.638, 49.633; 39.941, 43.795, 46.017, 47.335,
48.795, 49.199, 49.279, 49.27, 49.248, 49.23, 49.255, 49.2428; 39.896, 43.512,
45.914, 47.061, 48.011, 48.558, 48.943, 49.042, 49.069, 49.01, 49.046, 49.0266;
39.524, 42.934, 45.686, 46.743, 47.715, 48.67, 48.777, 48.836, 48.876, 48.836,
48.845, 48.8184; 39.439, 43.01, 45.556, 46.801, 47.792, 48.388, 48.634, 48.67,
48.639, 48.647, 48.625, 48.5912; 39.502, 42.849, 45.336, 46.385, 47.312, 47.877,
48.222, 48.397, 48.459, 48.482, 48.455, 48.414]` kg/s

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization** 设置为 `Tabulated data - Flow rate and efficiency vs. corrected speed and
pressure ratio`。

### 效率数据

### **Constant isentropic efficiency** — 等熵效率值 `0.8`（默认）| 正标量

解析参数化在标称工况下的等熵效率。

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization** 设置为 `Analytical - Nominal pressure ratio and corrected mass flow
rate`。

### **Pressure ratio vector, pr** — 压比向量 `[1.252, 1.328, 1.425, 1.544, 1.642, 1.757, 1.873, 2.005, 2.1, 2.204, 2.248, 2.28]`（默认）| 正标量向量

用于等熵效率表格化参数化的压比值向量。此向量的元素数量必须与 **Isentropic efficiency vector, eta(pr))** 参数相同，且所有元素必须大于 1。

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization** 设置为 `Tabulated data - Flow rate and efficiency vs. pressure
ratio`。

### **Isentropic efficiency vector, eta(pr)** — 等熵效率向量 `[.559, .61, .673, .741, .788, .835, .869, .895, .908, .899, .854, .751]`（默认）| 取值范围为 (0,1] 的元素向量

用于等熵效率表格化参数化的等熵效率值向量。此向量的元素数量必须与 **Pressure ratio vector, pr** 参数相同，且所有元素必须大于 0 且小于或等于 1。

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization** 设置为 `Tabulated data - Flow rate and efficiency vs. pressure
ratio`。

### **Pressure ratio table, pr(N,beta)** — 涡轮特性图压比数据 *M*×*N* 矩阵（默认）

在指定的修正轴转速和 β 值下的涡轮出口-入口压比 *M*×*N* 矩阵。该模块在表格元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Constant speed index vector, N** 参数中向量元素的数量。
- *N* 是表格中 β 索引的数量。

默认表格值为：

`[1.224, 1.246, 1.292, 1.387, 1.457, 1.534, 1.61, 1.686, 1.743, 1.79,
1.871, 1.914; 1.237, 1.25, 1.28, 1.369, 1.459, 1.553, 1.629, 1.716, 1.799, 1.846,
1.927, 1.97; 1.241, 1.255, 1.283, 1.326, 1.401, 1.509, 1.591, 1.704, 1.806, 1.913,
1.994, 2.037; 1.25, 1.265, 1.308, 1.364, 1.456, 1.532, 1.637, 1.739, 1.851, 1.934,
2.042, 2.085; 1.281, 1.314, 1.371, 1.425, 1.498, 1.574, 1.647, 1.749, 1.878, 1.979,
2.091, 2.18; 1.252, 1.328, 1.425, 1.544, 1.642, 1.757, 1.873, 2.005, 2.1, 2.204,
2.248, 2.28; 1.382, 1.43, 1.495, 1.586, 1.688, 1.791, 1.887, 1.99, 2.079, 2.158,
2.249, 2.217]`

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization** 设置为 `Tabulated data - Flow rate and efficiency vs. corrected speed and
pressure ratio`。

### **Isentropic efficiency table, eta(N,beta)** — 涡轮特性图等熵效率数据 *M*×*N* 矩阵（默认）

在指定的恒定轴转速和 β 值下的涡轮等熵效率 *M*×*N* 矩阵。该模块在表格元素之间采用线性插值。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Constant speed index vector, N** 参数中向量元素的数量。
- *N* 是表格中 β 索引的数量。

默认表格值为：

`[.72, .754, .759, .739, .714, .679, .643, .603, .554, .524, .494, .48;
.716, .757, .794, .819, .812, .788, .761, .728, .692, .662, .632, .618; .629, .691,
.775, .831, .858, .869, .859, .842, .816, .782, .752, .738; .594, .668, .757, .804,
.857, .883, .892, .893, .884, .865, .835, .821; .664, .72, .779, .823, .858, .883,
.897, .905, .904, .896, .883, .868; .559, .61, .673, .741, .788, .835, .869, .895,
.908, .899, .854, .751; .718, .785, .824, .855, .882, .9, .908, .906, .884, .857,
.804, .701]`

#### 依赖关系

要启用此参数，请将 **Turbine map parameterization** 设置为 `Tabulated data - Flow rate and efficiency vs. corrected speed and
pressure ratio`。

### 参数

### **Reference pressure for corrected flow** — 修正压力 `0.101325` MPa（默认）| 正标量

涡轮数据整合为修正趋势线时的压力。

### **Reference temperature for corrected flow** — 修正温度 `373.15` K（默认）| 正标量

涡轮数据整合为修正趋势线时的温度。

### **Mechanical efficiency** — 扭矩转换效率 `0.9`（默认）| 取值范围为 [0,1] 的正标量

从比焓降低转换为轴扭矩的效率。

### **Inlet area at port A** — 涡轮入口面积 `0.01` m^2（默认）| 正标量

涡轮入口横截面积。

### **Outlet area at port B** — 涡轮出口面积 `0.01` m^2（默认）| 正标量

涡轮出口横截面积。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Fluid Machines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2023a：控制端口 VN 的可见性

使用 **Model variable nozzle** 参数启用可变喷嘴控制端口 **VN**。

## 描述

热力学循环中的两相涡轮

Turbine (2P) 模块对两相流体网络中的涡轮进行建模。您可以将该模块参数化为表格化涡轮特性图，其可以是压比的 1-D 函数，也可以是压比和修正质量流量的 2-D 函数。流体从端口 **A** 流向端口 **B** 产生扭矩。端口 **R** 报告相对于端口 **C**（表示涡轮壳体）的轴扭矩和角速度。

启用时，端口 **VN** 表示喷嘴开度分数。该值线性缩放修正质量流量，但不影响涡轮效率。值 `1` 对应于涡轮特性图中的数据。

Turbine (2P) 模块假定过热流体进入入口。您可以使用 **Report when fluid is not fully vapor** 参数来选择当流体不满足过热条件时模块的行为。

### Turbine Map

要将模块映射可视化，请右键单击该模块并选择 **Fluids** > **Plot Turbine Map**。

每次修改模块设置时，请单击图形窗口上的 **Reload Data**。

涡轮映射将涡轮性能（作为压力比的函数）与修正质量流量和等熵效率关联起来。压力比是涡轮进口压力与出口压力之比。

涡轮映射绘制两个单独的图：修正质量流量与压力比，以及等熵效率与压力比。当您将 **Turbine map parameterization** 设置为 `Tabulated data - flow rate and efficiency vs. corrected speed and pressure ratio` 时，这些图还取决于修正转子速度 *N*。索引变量 β 在质量流量表和效率表之间不必相同。

**Corrected Mass Flow Rate**

由于涡轮内部压力和温度变化很大，涡轮映射以修正质量流量的形式绘制性能。该模块通过使用修正压力和温度，根据进口质量流量调整修正质量流量

m˙ATATcorr=m˙corrpApcorr,

其中：

- m˙*A* 是端口 **A** 处的质量流量。
- *TA* 是端口 **A** 处的温度。
- *Tcorr* 是 **Reference temperature for corrected flow** 参数。有关此值，请参阅您涡轮的数据表。
- m˙*corr* 是修正质量流量。

  当 **Turbine map parameterization** 为 `Analytical - nominal pressure ratio and corrected mass flow rate` 时，这是 **Nominal corrected mass flow rate** 参数的值。

  当 **Turbine map parameterization** 为 `Tabulated data - Flow rate and efficiency vs. pressure ratio` 时，这是 **Corrected mass flow rate vector, mdot(pr)** 参数的值。

  当 **Turbine map parameterization** 为 `Tabulated data - Flow rate and efficiency vs. corrected speed and pressure ratio` 时，这是 **Corrected mass flow rate table, mdot(N,beta)** 参数的值。
- *pA* 是端口 **A** 处的压力。
- *pcorr* 是 **Reference pressure for corrected flow** 参数。有关此值，请参阅您涡轮的数据表。

**Corrected Speed**

该模块还根据参考温度调整轴速度 *ω*，使得修正轴速度为

ωcorr=ωTATref.

### Shaft Torque

该模块计算轴扭矩 *τ* 为

τ=ηmm˙AΔhtotalω,

其中：

- *Δhtotal* 是流体比焓的总变化。
- *ηm* 是 **Mechanical efficiency** 参数的值。
- *ω* 是相对轴角速度，*ωR - ωC*。

从端口 **B** 到端口 **A** 的反向流超出了典型涡轮运行模式，可能不会返回准确结果。当流量接近零时的阈值区域确保当流量接近零或反向时，该模块不产生扭矩。

### Analytical Parametrization

使用解析参数化根据预期的标称运行条件创建涡轮。当 **Turbine map parameterization** 为 `Analytical – nominal pressure ratio and corrected mass flow rate` 时，涡轮等熵效率恒定，质量流量是压力比的函数。

此图显示了使用解析参数化时的默认涡轮映射。

Analytical Turbine map

### Parameterization by Pressure Ratio

当 **Turbine map parameterization** 为 `Tabulated data - Flow rate and efficiency vs. pressure ratio` 时，涡轮等熵效率和质量流量是压力比的函数，并且不考虑涡轮转速的任何变化。

**Corrected mass flow rate vector, mdot(pr)** 和 **Pressure ratio vector, pr** 参数的最后一个元素表示阻塞流条件下的修正质量流量和压力比。

此图显示了使用一维参数化时的默认涡轮映射。

1D Turbine map

### Parameterization by Pressure Ratio and Corrected Mass Flow Rate

当 **Turbine map parameterization** 设置为 `Tabulated data - Flow rate and efficiency vs. corrected speed and pressure ratio` 时，涡轮等熵效率、压力比和修正质量流量是修正速度 *N* 和映射索引 *β* 的函数。该模块对效率、压力比和修正质量流量参数的数据点之间使用线性插值。

**Corrected mass flow rate table, mdot(N,beta)** 和 **Pressure ratio table, pr(N,beta)** 的最后一列表示阻塞流条件下的修正质量流量和压力比。

此图显示了使用二维参数化时的默认涡轮映射。

2D Turbine map

### Continuity Equations

质量在该模块上守恒：

m˙A+m˙B=0,

其中 m˙*B* 是端口 **B** 处的质量流量。

该模块计算能量平衡为

ΦA+ΦB−Pfluid=0,

其中：

- *ΦA* 是端口 **A** 处的能量流率。
- *ΦB* 是端口 **B** 处的能量流率。
- *Pfluid* 是流体所做的功，该模块根据流体总比焓的变化确定，Pfluid=m˙AΔhtotal。

### 假设和限制

- 在反向流条件下，轴不旋转。反向流期间的结果可能不准确。
