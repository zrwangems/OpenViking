---
type: simulink-block
title: 'Fan (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Turbomachinery'
documentation_page: 'fanma'
documentation_source_path: 'ref/fanma.html'
language: zh-CN
chinese_source: worker-translation
---

# Fan (MA)

## 端口

### 守恒

### **A** — 流体入口湿空气

与流体关联的湿空气守恒端口。

### **B** — 流体出口湿空气

与流体关联的湿空气守恒端口。

### **R** — 轴机械旋转

与轴关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与壳体关联的机械旋转守恒端口。

## 参数

### **风机参数化** — 风机性能模型 `Static pressure and flow rate at reference shaft speed` (默认) | `1D tabulated data - static pressure vs. flow rate at reference shaft speed` | `2D tabulated data - static pressure vs. shaft speed and flow rate` | `2D tabulated data - flow rate vs. shaft speed and static pressure`

风机性能模型，指定为：

- `Static pressure and flow rate at reference shaft speed`：基于典型、标称或额定压力增益和体积流量指定风机性能。
- `1D tabulated data – static pressure vs flow rate at reference shaft speed`：基于压力增益数据作为体积流量的函数的插值指定风机性能。
- `2D tabulated data – static pressure vs shaft speed and flow rate`：基于压力增益数据作为轴转速和体积流量的函数的插值指定风机性能。
- `2D tabulated data – flow rate vs shaft speed and static pressure`：基于体积流量数据作为轴转速和压力增益的函数的插值指定风机性能。

### **轴功率指定** — 功率定义 `Fan efficiency` (默认) | `Brake power`

风机功率指定，指定为：

- `Fan efficiency`：根据风机效率推导机械功率。
- `Mechanical power`：直接指定机械功率。

### **标称体积流量** — 参考轴转速下的流量 `0.12` m^3/s (默认) | positive scalar

在标称、典型或额定工况下，风机在参考轴转速下通过的体积流量。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `Static pressure and flow rate at reference shaft speed`。

### **标称静压增益** — 参考轴转速下的压力增益 `5400` Pa (默认) | positive scalar

在标称、典型或额定工况下，参考轴转速下从端口 **A** 到端口 **B** 的压力增加。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `Static pressure and flow rate at reference shaft speed`。

### **标称效率** — 参考轴转速下的效率 `0.40` (默认) | positive scalar

在标称、典型或额定工况下，参考轴转速下将轴功率转换为流体功率的效率。

#### 依赖关系

要启用此参数，请将：

- **风机参数化** 设置为 `Static pressure and flow rate at reference shaft speed`。
- **轴功率指定** 设置为 `Fan efficiency`。

### **标称机械功率** — 标称效率下的功率 `1620` `W` (默认) | positive scalar

在标称、典型或额定工况下，参考轴转速下驱动湿空气流动的机械功率。

#### 依赖关系

要启用此参数，请将：

- **风机参数化** 设置为 `Static pressure and flow rate at reference shaft speed`。
- **轴功率指定** 设置为 `Brake power`。

### **零流量时的最大静压增益** — 参考轴转速下的最大压力 `6400` `Pa` (默认) | positive scalar

当通过风机的流量为零时，在参考轴转速下从端口 **A** 到端口 **B** 的压力增加。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `Static pressure and flow rate at reference shaft speed`。

### **零压力时的最大体积流量** — 参考轴转速下的最大流量 `0.24` `m^3/s` (默认) | positive scalar

在参考轴转速和恒定压力下的自由输送体积流量。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `Static pressure and flow rate at reference shaft speed`。

### **参考轴转速** — 风机曲线参考转速 `3000` `rpm` (默认) | positive scalar

与风机特性曲线数据对应的参考轴角速度。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `Static pressure and flow rate at reference shaft speed` 或 `1D tabulated data - static pressure vs. flow rate at reference shaft speed`。

### **最小轴转速阈值（相对于参考值的分数）** — 最小轴转速阈值 `1e-2` (默认) | positive scalar

最小轴转速阈值占参考轴转速的分数。该模块使用此值来防止轴转速变为零并导致 *qref* 表达式中的除零错误。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `Static pressure and flow rate at reference shaft speed` 或 `1D tabulated data - static pressure vs. flow rate at reference shaft speed`。

### **体积流量向量** — 风机曲线流量向量 `[.0278, .0556, .0833, .111, .139, .167]` `m^3/s` (默认) | vector

用于风机特性曲线一维插值的体积流量网格点向量。当 **轴功率指定** 为 `Brake power` 时，风机数据可以超出正常工作区域，且这些值可以为负。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `1D tabulated data - static pressure vs. flow rate at reference shaft speed`。

### **静压增益向量** — 给定体积流量下的压力增益 `[6410, 6375, 6018, 5366, 4501, 3609]` `Pa` (默认) | vector

压力增益数据点向量。向量中的每个元素对应于 **体积流量向量** 参数中的一个元素。压力增益是在参考轴转速下从端口 **A** 到端口 **B** 的压力增加。当 **轴功率指定** 为 `Brake power` 时，风机数据可以超出正常工作区域，且这些值可以为负。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `1D tabulated data - static pressure vs. flow rate at reference shaft speed`。

### **效率向量** — 给定体积流量下的效率 `[.257, .394, .453, .47, .459, .415]` (默认) | vector

风机效率数据点向量。向量中的每个元素对应于 **体积流量向量** 参数中的一个元素。效率是在参考轴转速下流体功率与轴机械功率之比。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `1D tabulated data - static pressure vs. flow rate at reference shaft speed`，并将 **轴功率指定** 设置为 `Fan efficiency`。

### **机械功率向量** — 用于转矩参数化的功率 `[693, 900, 1107, 1267, 1363, 1452]` W (默认) | 1-by-*n* vector

轴机械功率数据点向量。向量中的每个元素对应于 **体积流量向量** 参数中的一个元素。机械功率是在参考轴转速下驱动风机的功率。如果风机数据超出正常工作区域，这些值可以为负。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `1D tabulated data - static pressure vs. flow rate at reference shaft speed`，并将 **轴功率指定** 设置为 `Brake power`。

### **参考密度** — 与风机曲线数据关联的密度 `1.2` kg/m^3 (默认) | positive scalar

给定特性风机曲线的湿空气密度。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `1D tabulated data - static pressure vs. flow rate at reference shaft speed`、`2D tabulated data - static pressure vs. shaft speed and flow rate` 或 `2D tabulated data - flow rate vs. shaft speed and static pressure`。

### **轴转速向量, w** — 给定值的轴角速度 `[2400; 3000; 3600]` rpm (默认) | vector

用于风机特性曲线二维插值的轴角速度网格点向量。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `2D tabulated data - static pressure vs. shaft speed and flow rate` 或 `2D tabulated data - flow rate vs. shaft speed and static pressure`。

### **体积流量向量, q** — 用于压力增益参数化的流量 `[.0278, .0556, .0833, .111, .139, .167]` m^3/s (默认) | 1-by-*n* vector

用于风机特性曲线二维插值的体积流量网格点向量。当 **轴功率指定** 为 `Brake power` 时，风机数据可以超出正常工作区域，且这些值可以为负。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `2D tabulated data - static pressure vs. shaft speed and flow rate`。

### **静压增益表, dp(w,q)** — 用于压力参数化的压力 `[4111, 4010, 3551, 2881, 2167, 1453; 6410, 6375, 6018, 5366, 4501, 3609; 9217, 9285, 9022, 8428, 7552, 6482]` `Pa` (默认) | *M*-by-*N* matrix

*M*-by-*N* 压力增益数据点矩阵，用于压力增益的二维插值。压力增益是从端口 **A** 到端口 **B** 的压力增加。当 **轴功率指定** 为 `Brake power` 时，风机数据可以超出正常工作区域，且这些值可以为负。*M* 和 *N* 是相应向量的大小：

- *M* 是 **轴转速向量, w** 参数中的元素数。零流量对应的元素必须按严格升序排列。
- *N* 是 **体积流量向量, q** 参数中的元素数。

如果表中包含未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风机曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会扭曲风机在该区域运行时的行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **静压增益表, dp(w,q)**、**效率表, eta(w,q)** 和 **机械功率表, W(w,q)** 参数中 `NaN` 元素的位置必须相互匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `2D tabulated data - static pressure vs. shaft speed and flow rate`。

### **效率表, eta(w,q)** — 用于转矩参数化的效率 `[.3, .434, .468, .459, .4, .3; .257, .394, .453, .47, .459, .415; .225, .359, .434, .461, .47, .459]` 1 (默认) | *M*-by-*N* matrix

*M*-by-*N* 效率数据点矩阵，用于转矩的二维插值。效率是流体功率与轴机械功率之比。*M* 和 *N* 是相应向量的大小：

- *M* 是 **轴转速向量, w** 参数中的元素数。
- *N* 是 **体积流量向量, q** 参数中的元素数。

如果表中包含未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风机曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会扭曲风机在该区域运行时的行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **静压增益表, dp(w,q)**、**效率表, eta(w,q)** 和 **机械功率表, W(w,q)** 参数中 `NaN` 元素的位置必须相互匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `2D tabulated data - static pressure vs. shaft speed and flow rate`，并将 **轴功率指定** 设置为 `Fan efficiency`。

### **机械功率表, W(w,q)** — 用于转矩参数化的机械功率 `[381, 514, 632, 697, 753, 809; 693, 900, 1107, 1267, 1363, 1452; 1139, 1438, 1732, 2029, 2233, 2358]` W (默认) | *M*-by-*N* matrix

*M*-by-*N* 机械功率数据点表，用于转矩的二维插值。如果风机数据超出正常工作区域，这些值可以为负。机械功率是驱动风机的功率。*M* 和 *N* 是相应向量的大小：

- *M* 是 **轴转速向量, w** 参数中的元素数。零流量对应的元素必须按严格升序排列。
- *N* 是 **体积流量向量, q** 参数中的元素数。

如果表中包含未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风机曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会扭曲风机在该区域运行时的行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **静压增益表, dp(w,q)**、**效率表, eta(w,q)** 和 **机械功率表, W(w,q)** 参数中 `NaN` 元素的位置必须相互匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `2D tabulated data - static pressure vs. shaft speed and flow rate`，并将 **轴功率指定** 设置为 `Brake power`。

### **静压增益向量, dp** — 用于流量参数化的压力 `[31, 62, 93, 124]` Pa (默认) | 1-by-*N* vector

用于风机特性曲线二维插值的压力增益网格点向量。当 **轴功率指定** 为 `Brake power` 时，风机数据可以超出正常工作区域，且这些值可以为负。

#### 依赖关系

要启用此参数，请将 **风机参数化** 设置为 `2D tabulated data - flow rate vs. shaft speed and static pressure`。

### **Volumetric flow rate table, q(w,dp)** — 用于流量参数化的流量 `[.802, .759, .703, .611; .936, .902, .862, .81; 1.056, 1.027, .994, .956]` m^3/s（默认） | *M*×*N* 矩阵

*M*×*N* 矩阵，包含用于体积流量 2-D 插值的体积流量数据点。当 **Shaft power specification** 为 `Brake power` 时，风机数据可以延伸到正常工作区域之外，这些值可以为负。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Shaft speed vector, w** 参数中的元素数。对应零流量的元素必须严格按升序排列。
- *N* 是 **Static pressure gain vector, Dp** 参数中的元素数。

如果表格中有未知数据点，请在这些值的位置使用 `NaN`。模块基于风机曲线的平均斜率进行外推来填充 `NaN` 元素。不要使用人工数值，因为这些值会扭曲风机在该区域运行时的行为。使用未知数据时：

- 表格中的 `NaN` 元素必须连续。
- **Volumetric flow rate table, q(w,dp)**、**Efficiency table, eta(w,dp)** 和 **Mechanical power table, W(w,dp)** 参数中 `NaN` 元素的位置必须彼此匹配。
- `NaN` 元素必须位于表格的右上部分，该部分对应最高体积流量和最低轴转速。

#### 依赖项

要启用此参数，请将 **Fan parameterization** 设置为 `2D tabulated data - flow rate vs. shaft speed and static pressure`。

### **Efficiency table, eta(w,dp)** — 用于转矩参数化的效率 `[.088, .162, .22, .261; .068, .128, .18, .222; .055, .105, .148, .188]`（默认） | *M*×*N* 矩阵

*M*×*N* 矩阵，包含用于转矩 2-D 插值的效率数据点。效率是流体功率与轴机械功率之比。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Shaft speed vector, w** 参数中的元素数。
- *N* 是 **Static pressure gain vector, Dp** 参数中的元素数。

如果表格中有未知数据点，请在这些值的位置使用 `NaN`。模块基于风机曲线的平均斜率进行外推来填充 `NaN` 元素。不要使用人工数值，因为这些值会扭曲风机在该区域运行时的行为。使用未知数据时：

- 表格中的 `NaN` 元素必须连续。
- **Volumetric flow rate table, q(w,dp)**、**Efficiency table, eta(w,dp)** 和 **Mechanical power table, W(w,dp)** 参数中 `NaN` 元素的位置必须彼此匹配。
- `NaN` 元素必须位于表格的右上部分，该部分对应最高体积流量和最低轴转速。

#### 依赖项

要启用此参数，请将 **Fan parameterization** 设置为 `2D tabulated data - flow rate vs. shaft speed and static pressure`，并将 **Shaft power specification** 设置为 `Fan efficiency`。

### **Mechanical power table, W(w,dp)** — 用于转矩参数化的机械功率 `[283, 290, 297, 290; 427, 437, 445, 452; 595, 606, 625, 631]` `W`（默认） | *M*×*N* 矩阵

*M*×*N* 矩阵，包含用于转矩 2-D 插值的机械功率数据点。如果风机数据延伸到正常工作区域之外，这些值可以为负。机械功率是驱动风机的功率。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Shaft speed vector, w** 参数中的元素数。对应零流量的元素必须严格按升序排列。
- *N* 是 **Static pressure gain vector, Dp** 参数中的元素数。

如果表格中有未知数据点，请在这些值的位置使用 `NaN`。模块基于风机曲线的平均斜率进行外推来填充 `NaN` 元素。不要使用人工数值，因为这些值会扭曲风机在该区域运行时的行为。使用未知数据时：

- 表格中的 `NaN` 元素必须连续。
- **Volumetric flow rate table, q(w,dp)**、**Efficiency table, eta(w,dp)** 和 **Mechanical power table, W(w,dp)** 参数中 `NaN` 元素的位置必须彼此匹配。
- `NaN` 元素必须位于表格的右上部分，该部分对应最高体积流量和最低轴转速。

#### 依赖项

要启用此参数，请将 **Fan parameterization** 设置为 `2D tabulated data - flow rate vs. shaft speed and static pressure`，并将 **Shaft power specification** 设置为 `Brake power`。

### **Fan diameter scale factor** — 模型到参考的缩放因子 `1`（默认） | 正标量

几何缩放因子，用于相对于给定风机参数化增大或减小仿真风机的尺寸。对于远大于或远小于 1 的缩放因子，缩放可能不准确。

### **Mechanical orientation** — 旋转方向 `Positive angular velocity of port R relative to port C corresponds to normal fan operation`（默认） | `Negative angular velocity of port R relative to port C corresponds to normal fan operation`

正常运行的轴方向。默认情况下，流量和压力增益从端口 **A** 到端口 **B**。

### **Inlet flow area (port A)** — 端口 A 面积 `0.01` `m^2`（默认） | 正标量

风机入口处湿空气流的横截面积。

### **Outlet flow area (port B)** — 端口 B 面积 `0.01` `m^2`（默认） | 正标量

风机出口处湿空气流的横截面积。

## 所属库

Simscape / Fluids / Moist Air / Turbomachinery

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2024b：对湿空气流中悬浮的水滴进行建模

湿空气域中的模块现在可以对湿空气流中悬浮的水滴进行建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

### R2023a：公开低轴转速阈值

使用 **Minimum shaft speed threshold as fraction of reference** 参数，将最小轴转速阈值控制为参考轴转速的分数。当 **Fan parameterization** 参数为 `Static pressure and flow rate at reference shaft speed` 或 `1D tabulated data – static pressure vs flow rate at reference shaft speed` 时，模块中提供 **Minimum shaft speed threshold as fraction of reference** 参数。

### R2022b：将性能扩展到正常工作条件之外

1-D 和 2-D 参数化现在都允许负值。当仿真超出所提供表格的范围时，模块基于风机曲线的平均斜率外推压力。

现在可以在数据不可用的位置使用 `NaN` 元素。这些 2-D 表格化风机参数支持表格右上部分的连续 `NaN` 元素：

- **Static pressure gain table, dp(w,q)**
- **Efficiency table, eta(w,q)**
- **Mechanical power table, W(w,q)**
- **Volumetric flow rate table, q(w,dp)**
- **Efficiency table, eta(w,dp)**
- **Mechanical power table, W(w,dp)**

对于每个模块，如果轴按与指定机械方向相反的方向旋转，则模块两端的压差降为零，结果可能不准确。

## 描述

湿空气网络中的风机

Fan (MA) 模块表示湿空气网络中的风机。可以将风机上的转矩和压力增益建模为静压和流量的函数，或使用 1D 或 2D 表格化参考压力、轴转速和流量数据来建模。

默认情况下，流量和压力增益从端口 **A** 到端口 **B**。端口 **C** 表示风机机壳，端口 **R** 表示风机轴。可以在 **Mechanical orientation** 参数中指定正常运行的轴方向。如果轴开始沿相反方向旋转，则风机两端的压差降为零。

### 按标称压力、流量和轴转速进行参数化

当将 **Fan parameterization** 参数设置为 `Static pressure and flow rate at reference shaft speed` 时，模块使用解析风机相似定律和参考压差来计算从端口 **A** 到端口 **B** 的压力增益：

pB−pA=Δpref(ωωref)2(DDref)2,

其中：

- *Δpref* 是参考压差。模块使用在 **Maximum static pressure gain at zero flow**、**Nominal static pressure gain** 和 **Maximum volumetric flow rate at zero pressure** 参数处的风机压差值的二次拟合。
- *ω* 是轴角速度，*ωR* – *ωC*。
- *ωref* 是 **Reference shaft speed** 参数。
- DDref 是 **Fan diameter scale factor** 参数。

模块根据参考机械功率和风机相似定律计算轴转矩：

τ=Φrefω2ωref3(DDref)5.

其中 *Φref* 是压力增益与风机效率的比例：

Φref=qrefΔprefηref.

当将 **Shaft power specification** 参数设置为 `Fan efficiency` 时，模块在风机峰值性能 *ηnom* 与 0 之间使用效率的二次拟合。*ηnom* 等效于 **Nominal efficiency** 参数，模块将其解释为峰值效率。如果将 **Shaft power specification** 参数设置为 `Brake power`，则模块根据峰值或标称条件下的标称制动功率 *Φnom* 推导标称风机效率：

ηnom=qnomΔpnomΦnom.

模块假设当无流量或流量达到零压力下的最大体积流量时，效率为零。模块使用当前流量 *q* 计算参考流量：

qref=qωrefω(DrefD)3.

### 1-D 表格化数据参数化：压力作为参考轴转速下流量的函数

当将 **Fan parameterization** 参数设置为 `1D tabulated data - static pressure vs. flow rate at reference shaft speed` 时，可以将风机性能建模为体积流量的函数。模块从 1-D **Static pressure gain vector** 参数 *Δpref(qref)* 中插值计算从端口 **A** 到端口 **B** 的压力增益：

pB−pA=Δpref(qref)(ρρref)(ωωref)2(DDref)2.

这里，*ρ* 是湿空气密度，*ρref* 是参考密度，等效于 **Reference density** 参数。模块根据参考机械功率和风机相似定律计算轴转矩：

τ=Φref(qref)ω2ωref3(ρρref)(DDref)5,

其中 *ρref* 是 **Reference density**。

模块使用当前流量 *q* 计算参考流量：

qref=qωrefω(DrefD)3.

当仿真超出所提供表格的范围时，模块基于风机曲线的平均斜率将压力和参考转矩外推到最近点。

### 2-D 表格化数据参数化：压力作为轴转速和流量的函数

当将 **Fan parameterization** 参数设置为 `2D tabulated data - static pressure vs. shaft speed and flow rate` 时，可以将风机性能建模为体积流量和角速度的 2-D 函数。模块从 2-D **Static pressure gain table, dp(w,q)** 参数中插值计算从端口 **A** 到端口 **B** 的压力增益。模块将参考压力增益 *Δpref(qref,ω)* 定义为

pB−pA=Δpref(qref,ω)(ρρref)(DDref)2.

模块根据参考机械功率和风机相似定律计算轴转矩：

τ=Φref(qref,ω)ω(ρρref)(DDref)5,

其中参考机械功率是参考流量和当前轴转速的函数。

模块使用当前流量 *q* 计算参考流量：

qref=q(DrefD)3.

当仿真超出所提供表格的范围时，模块基于风机曲线的平均斜率将压力和参考转矩外推到最近点。

**缺失数据**

如果表格中有未知数据点，请在这些值的位置使用 `NaN`。模块基于风机曲线的平均斜率进行外推来填充 `NaN` 元素。不要使用人工数值，因为这些值会扭曲风机在该区域运行时的行为。使用未知数据时：

- 表格中的 `NaN` 元素必须连续。
- **Static pressure gain table, dp(w,q)**、**Efficiency table, eta(w,q)** 和 **Mechanical power table, W(w,q)** 参数中 `NaN` 元素的位置必须彼此匹配。
- `NaN` 元素必须位于表格的右上部分，该部分对应最高体积流量和最低轴转速。

### 2-D 表格化数据参数化：流量作为轴转速和压力的函数

当将 **Fan parameterization** 参数设置为 `2D tabulated data - flow rate vs. shaft speed and static pressure` 时，可以将通过风机的流量建模为压力和角速度的 2-D 函数。体积流量从 2-D **Volumetric flow rate table, q(w,dp)** 参数 *qref* 插值得到。参考流量是参考压力增益 *Δpref* 和当前轴转速 *ω* 的函数：

q=qref(Δpref,ω)(DDref)3,

其中参考压力增益由风机两端的压差得出：

Δpref=(pB−pA)(ρrefρ)(DrefD)2.

轴转矩由参考机械功率和风机相似定律得出：

τ=Φref(Δpref,ω)ω(ρρref)(DDref)5,

其中参考机械功率是参考流量和当前轴转速的函数。

当仿真超出所提供表格的范围时，模块基于风机曲线的平均斜率将压力和参考转矩外推到最近点。

**缺失数据**

如果表格中有未知数据点，请在这些值的位置使用 `NaN`。模块基于风机曲线的平均斜率进行外推来填充 `NaN` 元素。不要使用人工数值，因为这些值会扭曲风机在该区域运行时的行为。使用未知数据时：

- 表格中的 `NaN` 元素必须连续。
- **Volumetric flow rate table, q(w,dp)**、**Efficiency table, eta(w,dp)** 和 **Mechanical power table, W(w,dp)** 参数中 `NaN` 元素的位置必须彼此匹配。
- `NaN` 元素必须位于表格的右上部分，该部分对应最高体积流量和最低轴转速。

### 功率与效率

可以将轴功率指定为风机效率或制动功率。

模块按以下方式计算效率

η=ΦfluidΦbrake,

其中 *制动功率*，即在轴处测得的机械功率，为

Φbrake=τω.

模块按以下方式计算流体功率

Φfluid=q(pB−pA).

模块按以下方式计算转矩

τ=Φbrakeω.

### 可视化风机曲线

可以通过绘制压力、功率、效率和转矩随流量变化的曲线来检查参数化的风机性能。要生成当前风机设置的图，请右键单击模块，然后选择 **Fluids** > **Plot Fan Characteristics**。如果更改设置或数据，请在模块参数上单击 **Apply**，并在风机曲线图上单击 **Reload Data**。

默认模块参数化会生成以下图：

风机特性曲线图

### 假设和限制

- 如果轴沿与指定的机械方向相反的方向旋转，则模块两端的压差降至零，结果可能不准确。
- 该模块假设风扇是准稳态的。
- 该模块依据静压升而非风扇总压来模拟风扇性能。
