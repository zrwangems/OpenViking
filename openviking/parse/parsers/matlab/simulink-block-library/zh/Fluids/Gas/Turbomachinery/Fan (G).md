---
type: simulink-block
title: 'Fan (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Turbomachinery'
documentation_page: 'fang'
documentation_source_path: 'ref/fang.html'
language: zh-CN
chinese_source: worker-translation
---

# Fan (G)

## 端口

### 守恒

### **A** — 流体入口气体

与流体关联的气体守恒端口。

### **B** — 流体出口气体

与流体关联的气体守恒端口。

### **R** — 轴机械旋转

与轴关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与壳体关联的机械旋转守恒端口。

## 参数

### **Fan parameterization** — 风扇性能模型 `Static pressure and flow rate at reference shaft speed`（默认）| `1D tabulated data - static pressure vs. flow rate at reference shaft speed` | `2D 表格数据 - 静压与轴转速和 flow rate` | `2D 表格数据 - 流量与轴转速和静压的关系 pressure`

风扇性能模型，指定为：

- `Static pressure and flow rate at reference shaft
  speed`：基于典型、标称或额定压力增益和体积流量指定风扇性能。
- `1D tabulated data – static pressure vs flow rate
  at reference shaft speed`：基于压力增益数据作为体积流量函数的插值指定风扇性能。
- `2D tabulated data – static pressure vs shaft
  speed and flow rate`：基于压力增益数据作为轴转速和体积流量函数的插值指定风扇性能。
- `2D tabulated data – flow rate vs
  shaft speed and static pressure`：基于体积流量数据作为轴转速和压力增益函数的插值指定风扇性能。

### **Shaft power specification** — 功率定义 `Fan efficiency`（默认）| `Brake power`

风扇功率规格，指定为：

- `Fan efficiency`：根据风扇效率推导机械功率。
- `Mechanical power`：直接指定机械功率。

### **Nominal volumetric flow rate** — 参考轴转速下的流量 `0.12` m^3/s（默认）| 正标量

在标称、典型或额定工况下，参考轴转速下通过风扇的体积流量。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `Static pressure and flow
rate at reference shaft speed`。

### **Nominal static pressure gain** — 参考轴转速下的压力增益 `5400` Pa（默认）| 正标量

在标称、典型或额定工况下，参考轴转速下从端口 **A** 到端口 **B** 的压力增加。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `Static pressure and flow
rate at reference shaft speed`。

### **Nominal efficiency** — 参考轴转速下的效率 `0.40`（默认）| 正标量

在标称、典型或额定工况下，参考轴转速下将轴功率转换为流体功率的效率。

#### 依赖关系

要启用此参数，请设置：

- **Fan parameterization** 为
  `Static pressure and flow rate at reference
  shaft speed`。
- **Shaft power specification** 为
  `Fan efficiency`。

### **Nominal mechanical power** — 标称效率下的功率 `1620` `W`（默认）| 正标量

在标称、典型或额定工况下，参考轴转速下驱动湿空气流动的机械功率。

#### 依赖关系

要启用此参数，请设置：

- **Fan parameterization** 为
  `Static pressure and flow rate at reference
  shaft speed`。
- **Shaft power specification** 为
  `Brake power`。

### **Maximum static pressure gain at zero flow** — 参考轴转速下的最大压力 `6400` `Pa`（默认）| 正标量

在参考轴转速下，当通过风扇的流量为零时，从端口 **A** 到端口 **B** 的压力增加。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `Static pressure and flow
rate at reference shaft speed`。

### **Maximum volumetric flow rate at zero pressure** — 参考轴转速下的最大流量 `0.24` `m^3/s`（默认）| 正标量

在参考轴转速和恒定压力下的自由输送体积流量。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `Static pressure and flow
rate at reference shaft speed`。

### **Reference shaft speed** — 风扇曲线参考转速 `3000` `rpm`（默认）| 正标量

对应于风扇特性曲线数据的参考轴角速度。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `Static pressure and flow
rate at reference shaft speed` 或 `1D
tabulated data - static pressure vs. flow rate at reference shaft
speed`。

### **Minimum shaft speed threshold as fraction of reference** — 最小轴转速阈值 `1e-2`（默认）| 正标量

最小轴转速作为参考轴转速分数的阈值。该模块使用此值来防止轴转速变为零，从而导致 *qref* 表达式中的除零错误。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `Static pressure and flow
rate at reference shaft speed` 或 `1D
tabulated data - static pressure vs. flow rate at reference shaft
speed`。

### **Volumetric flow rate vector** — 风扇曲线流量向量 `[.0278, .0556, .0833, .111, .139, .167]` `m^3/s`（默认）| 向量

用于风扇特性曲线一维插值的体积流量网格点向量。当 **Shaft power specification** 为 `Brake power` 时，风扇数据可以超出正常工作区域，这些值可以为负。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `1D tabulated data -
static pressure vs. flow rate at reference shaft
speed`。

### **Static pressure gain vector** — 给定体积流量下的压力增益 `[6410, 6375, 6018, 5366, 4501, 3609]` `Pa`（默认）| 向量

压力增益数据点向量。向量中的每个元素对应于 **Volumetric flow rate vector** 参数中的一个元素。压力增益是在参考轴转速下从端口 **A** 到端口 **B** 的压力增加。当 **Shaft power specification** 为 `Brake power` 时，风扇数据可以超出正常工作区域，这些值可以为负。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `1D tabulated data -
static pressure vs. flow rate at reference shaft
speed`。

### **Efficiency vector** — 给定体积流量下的效率 `[.257, .394, .453, .47, .459, .415]`（默认）| 向量

风扇效率数据点向量。向量中的每个元素对应于 **Volumetric flow rate vector** 参数中的一个元素。效率是在参考轴转速下流体功率与轴机械功率的比值。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `1D tabulated data -
static pressure vs. flow rate at reference shaft speed`
并将 **Shaft power specification** 设置为 `Fan
efficiency`。

### **Mechanical power vector** — 用于扭矩参数化的功率 `[693, 900, 1107, 1267, 1363, 1452]` W（默认）| 1×*n* 向量

轴机械功率数据点向量。向量中的每个元素对应于 **Volumetric flow rate vector** 参数中的一个元素。机械功率是在参考轴转速下驱动风扇的功率。如果风扇数据超出正常工作区域，这些值可以为负。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `1D tabulated data -
static pressure vs. flow rate at reference shaft speed`
并将 **Shaft power specification** 设置为 `Brake
power`。

### **Reference density** — 与风扇曲线数据关联的密度 `1.2` kg/m^3（默认）| 正标量

给定特性风扇曲线的湿空气密度。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `1D tabulated data -
static pressure vs. flow rate at reference shaft
speed`、`2D tabulated data - static pressure
vs. shaft speed and flow rate` 或 `2D
表格数据 - 流量与轴转速和静压的关系
pressure`。

### **Shaft speed vector, w** — 给定条件下的轴角速度 `[2400; 3000; 3600]` rpm（默认）| 向量

用于风扇特性曲线二维插值的轴角速度网格点向量。

#### 依赖关系

要启用此参数，请将 **Fan parameterization** 设置为
`2D 表格数据 - 静压与轴转速和
flow rate` 或 `2D tabulated data - flow
rate vs. shaft speed and static pressure`。

### **Volumetric flow rate vector, q** — 用于压力增益参数化的流量 `[.0278, .0556, .0833, .111, .139, .167]` m^3/s（默认）| 1×*n* 向量

用于风扇特性曲线二维插值的体积流量网格点向量。当 **Shaft power specification** 为 `Brake power` 时，风扇数据可以超出正常工作区域，这些值可以为负。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `2D tabulated data -
static pressure vs. shaft speed and flow rate`。

### **Static pressure gain table, dp(w,q)** — 用于压力参数化的压力 `[4111, 4010, 3551, 2881, 2167, 1453; 6410, 6375, 6018, 5366, 4501, 3609; 9217, 9285, 9022, 8428, 7552, 6482]` `Pa`（默认）| *M*×*N* 矩阵

用于压力增益二维插值的 *M*×*N* 压力增益数据点矩阵。压力增益是从端口 **A** 到端口 **B** 的压力增加。当 **Shaft power specification** 为 `Brake power` 时，风扇数据可以超出正常工作区域，这些值可以为负。*M* 和 *N* 是对应向量的尺寸：

- *M* 是 **Shaft speed vector, w** 参数中的元素数量。对应于零流量的元素必须严格按升序排列。
- *N* 是 **Volumetric flow rate vector, q** 参数中的元素数量。

如果表中包含未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风扇曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲风扇行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **Static pressure gain table, dp(w,q)**、**Efficiency table, eta(w,q)** 和 **Mechanical power table, W(w,q)** 参数中 `NaN` 元素的位置必须相互匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `2D tabulated data -
static pressure vs. shaft speed and flow rate`。

### **Efficiency table, eta(w,q)** — 用于扭矩参数化的效率 `[.3, .434, .468, .459, .4, .3; .257, .394, .453, .47, .459, .415; .225, .359, .434, .461, .47, .459]` 1（默认）| *M*×*N* 矩阵

用于扭矩二维插值的 *M*×*N* 效率数据点矩阵。效率是流体功率与轴机械功率的比值。*M* 和 *N* 是对应向量的尺寸：

- *M* 是 **Shaft speed vector, w** 参数中的元素数量。
- *N* 是 **Volumetric flow rate vector, q** 参数中的元素数量。

如果表中包含未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风扇曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲风扇行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **Static pressure gain table, dp(w,q)**、**Efficiency table, eta(w,q)** 和 **Mechanical power table, W(w,q)** 参数中 `NaN` 元素的位置必须相互匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `2D tabulated data -
static pressure vs. shaft speed and flow rate` 并将
**Shaft power specification** 设置为 `Fan
efficiency`。

### **Mechanical power table, W(w,q)** — 用于扭矩参数化的机械功率 `[381, 514, 632, 697, 753, 809; 693, 900, 1107, 1267, 1363, 1452; 1139, 1438, 1732, 2029, 2233, 2358]` W（默认）| *M*×*N* 矩阵

用于扭矩二维插值的 *M*×*N* 机械功率数据点表。如果风扇数据超出正常工作区域，这些值可以为负。机械功率是驱动风扇的功率。*M* 和 *N* 是对应向量的尺寸：

- *M* 是 **Shaft speed vector, w** 参数中的元素数量。对应于零流量的元素必须严格按升序排列。
- *N* 是 **Volumetric flow rate vector, q** 参数中的元素数量。

如果表中包含未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风扇曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲风扇行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **Static pressure gain table, dp(w,q)**、**Efficiency table, eta(w,q)** 和 **Mechanical power table, W(w,q)** 参数中 `NaN` 元素的位置必须相互匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `2D tabulated data -
static pressure vs. shaft speed and flow rate` 并将
**Shaft power specification** 设置为 `Brake
power`。

### **Static pressure gain vector, dp** — 用于流量参数化的压力 `[31, 62, 93, 124]` Pa（默认）| 1×*N* 向量

用于风扇特性曲线二维插值的压力增益网格点向量。当 **Shaft power specification** 为 `Brake power` 时，风扇数据可以超出正常工作区域，这些值可以为负。

#### 依赖关系

要启用此参数，请将 **Fan
parameterization** 设置为 `2D tabulated data - flow
rate vs. shaft speed and static pressure`。

### **Volumetric flow rate table, q(w,dp)** — 用于流量参数化的流量 `[.802, .759, .703, .611; .936, .902, .862, .81; 1.056, 1.027, .994, .956]` m^3/s（默认）| *M*×*N* 矩阵

用于体积流量二维插值的 *M*×*N* 体积流量数据点矩阵。当 **Shaft power specification** 为 `Brake power` 时，风机数据可以超出正常工作区域，这些值可以为负。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Shaft speed vector, w** 参数中元素的数量。对应于零流量的元素必须严格按升序排列。
- *N* 是 **Static pressure gain vector, Dp** 参数中元素的数量。

如果表中存在未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风机曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲风机行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **Volumetric flow rate table, q(w,dp)**、**Efficiency table, eta(w,dp)** 和 **Mechanical power table, W(w,dp)** 参数中 `NaN` 元素的位置必须彼此匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Fan parameterization** 设置为 `2D 表格数据 - 流量与轴转速和静压的关系 pressure`。

### **Efficiency table, eta(w,dp)** — 用于扭矩参数化的效率 `[.088, .162, .22, .261; .068, .128, .18, .222; .055, .105, .148, .188]`（默认）| *M*×*N* 矩阵

用于扭矩二维插值的 *M*×*N* 效率数据点矩阵。效率是流体功率与轴机械功率之比。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Shaft speed vector, w** 参数中元素的数量。
- *N* 是 **Static pressure gain vector, Dp** 参数中元素的数量。

如果表中存在未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风机曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲风机行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **Volumetric flow rate table, q(w,dp)**、**Efficiency table, eta(w,dp)** 和 **Mechanical power table, W(w,dp)** 参数中 `NaN` 元素的位置必须彼此匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Fan parameterization** 设置为 `2D 表格数据 - 流量与轴转速和静压的关系 pressure`，并将 **Shaft power specification** 设置为 `Fan efficiency`。

### **Mechanical power table, W(w,dp)** — 用于扭矩参数化的机械功率 `[283, 290, 297, 290; 427, 437, 445, 452; 595, 606, 625, 631]` `W`（默认）| *M*×*N* 矩阵

用于扭矩二维插值的 *M*×*N* 机械功率数据点矩阵。如果风机数据超出正常工作区域，这些值可以为负。机械功率是驱动风机的功率。*M* 和 *N* 是相应向量的大小：

- *M* 是 **Shaft speed vector, w** 参数中元素的数量。对应于零流量的元素必须严格按升序排列。
- *N* 是 **Static pressure gain vector, Dp** 参数中元素的数量。

如果表中存在未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风机曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲风机行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **Volumetric flow rate table, q(w,dp)**、**Efficiency table, eta(w,dp)** 和 **Mechanical power table, W(w,dp)** 参数中 `NaN` 元素的位置必须彼此匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

#### 依赖关系

要启用此参数，请将 **Fan parameterization** 设置为 `2D 表格数据 - 流量与轴转速和静压的关系 pressure`，并将 **Shaft power specification** 设置为 `Brake power`。

### **Fan diameter scale factor** — 模型到参考的比例因子 `1`（默认）| 正标量

用于相对于给定风机参数化增大或减小所模拟风机尺寸的几何比例因子。对于远大于或远小于 1 的比例因子，缩放可能不准确。

### **Mechanical orientation** — 旋转方向 `Positive angular velocity of port R relative to port C corresponds to normal fan operation`（默认）| `Negative angular velocity of port R relative to port C corresponds to normal fan operation`

正常工作轴方向。默认情况下，流量和压力增益从端口 **A** 到端口 **B**。

### **Inlet flow area (port A)** — 端口 A 面积 `0.01` `m^2`（默认）| 正标量

风机入口处湿空气流的横截面积。

### **Outlet flow area (port B)** — 端口 B 面积 `0.01` `m^2`（默认）| 正标量

风机出口处湿空气流的横截面积。

## 所属库

Simscape / Fluids / Gas / Turbomachinery

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2023a：公开低轴转速阈值

使用 **Minimum shaft speed threshold as fraction of reference** 参数将最低轴转速阈值控制为参考轴转速的分数。当 **Fan parameterization** 参数为 `Static pressure and flow rate at reference shaft speed` 或 `1D tabulated data – static pressure vs flow rate at reference shaft speed` 时，模块中提供 **Minimum shaft speed threshold as fraction of reference** 参数。

### R2022b：将性能扩展到正常工作条件之外

一维和二维参数化现在都允许负值。当仿真超出所提供表的范围时，模块会基于风机曲线的平均斜率外推压力。

现在可以在数据不可用的位置使用 `NaN` 元素。这些二维表格化风机参数支持表中右上部分的连续 `NaN` 元素：

- **Static pressure gain table, dp(w,q)**
- **Efficiency table, eta(w,q)**
- **Mechanical power table, W(w,q)**
- **Volumetric flow rate table, q(w,dp)**
- **Efficiency table, eta(w,dp)**
- **Mechanical power table, W(w,dp)**

对于每个模块，如果轴按照与指定机械方向相反的方向旋转，则模块两端的压差降至零，结果可能不准确。

### R2021b：二维表格化数据参数化：流量作为轴转速和压力比的函数

在 R2021b 中，该模块不再支持 `2-D Tabulated Data Parameterization: Flow Rate as a Function of Shaft Speed and Pressure Ratio` 参数化。在 R2021b 及更高版本中，如果打开在先前版本中创建且包含 Fan (G) 模块的模型，Simscape™ Fluids™ 会将该模块替换为 Fan (MA) - Legacy 模块。此模块支持 `2-D Tabulated Data Parameterization: Flow Rate as a Function of Shaft Speed and Pressure Ratio` 设置。

您可以通过将 **Fan parameterization** 设置为 `2D 表格数据 - 流量与轴转速和静压的关系 pressure`1 并将比率转换为绝对值，来保留使用此参数化的模型功能。执行此转换的示例脚本接收旧参数 `omega_DpMax_TLU`、`DpMax_TLU`、`omega_flow_TLU`、`Dp_DpMax_TLU`、`flow_rate_TLU` 和 `eta_flow_TLU`，并返回转换后的参数 `omega_g_TLU`、`pressure_g_TLU`、`pressure_g_TLU` 和 `eta_g_TLU`：

```
% Shaft speed vector for maximum pressure rise vector
omega_DpMax_TLU = [1800, 2400, 3000];

% Maximum pressure rise vector
DpMax_TLU       = [400, 1200, 2000];

% Shaft speed vector, omega
omega_flow_TLU  = [1800, 2400, 3000];

% Static pressure rise ratio vector, Dp/DpMax
Dp_DpMax_TLU    = linspace(0, 1, 4);

% Flow rate table, q(omega,Dp/DpMax)
flow_rate_TLU   = [
    0.33    0.26    0.18    0.07
    1.20    0.91    0.64    0.26
    1.84    1.61    1.13    0.46];

% Total efficiency table, Eta(omega,Dp/DpMax)
eta_flow_TLU    = [
    0.22    0.25    0.27    0.28
    0.48    0.52    0.55    0.53
    0.42    0.45    0.49    0.44];

% Create interpolants of the tables
DpMax_TLU_interp = griddedInterpolant(omega_DpMax_TLU, DpMax_TLU, ...
    'linear', 'linear');

flow_rate_TLU_interp = griddedInterpolant({omega_flow_TLU, Dp_DpMax_TLU}, flow_rate_TLU, ...
    'linear', 'linear');

eta_flow_TLU_interp = griddedInterpolant({omega_flow_TLU, Dp_DpMax_TLU}, eta_flow_TLU, ...
    'linear', 'nearest');

% Maximum pressure rise
DpMax = DpMax_TLU_interp(max(omega_flow_TLU, omega_DpMax_TLU(1)));

% Shaft speed vector, w
omega_q_TLU = omega_flow_TLU;

% Static pressure gain vector, Dp
pressure_q_TLU = unique(DpMax(:)*Dp_DpMax_TLU(:)');

% Interpolation query points as full grid arrays
omega_grid = omega_q_TLU(:)*ones(1, length(pressure_q_TLU));

Dp_DpMax_grid = pressure_q_TLU(:)' ./ DpMax(:);

% Volumetric flow rate table, q(w,Dp)
flow_rate_q_TLU = flow_rate_TLU_interp(omega_grid, Dp_DpMax_grid);

flow_rate_q_TLU = max(flow_rate_q_TLU, 1e-4*flow_rate_TLU(1,1)); % keep it > 0

% Efficiency table, eta(w,Dp)
eta_q_TLU = eta_flow_TLU_interp(omega_grid, Dp_DpMax_grid);
```

## 描述

气体网络中的风机

Fan (G) 模块表示气体网络中的风机。您可以将风机上的扭矩和压力增益建模为静压力和流量的函数，或使用一维或二维表格化参考压力、轴转速和流量数据。

默认情况下，流量和压力增益从端口 **A** 到端口 **B**。端口 **C** 表示风机壳体，端口 **R** 表示风机轴。您可以在 **Mechanical orientation** 参数中指定正常工作轴方向。如果轴开始沿相反方向旋转，风机两端的压差降至零。

### 按标称压力、流量和轴转速参数化

当您将 **Fan parameterization** 参数设置为 `Static pressure and flow rate at reference shaft speed` 时，模块使用解析风机相似定律和参考压差来计算从端口 **A** 到端口 **B** 的压力增益：

pB−pA=Δpref(ωωref)2(DDref)2,

其中：

- *Δpref* 是参考压差。模块使用 **Maximum static pressure gain at zero flow**、**Nominal static pressure gain** 和 **Maximum volumetric flow rate at zero pressure** 参数处风机压差值的二次拟合。
- *ω* 是轴角速度，*ωR* – *ωC*。
- *ωref* 是 **Reference shaft speed** 参数。
- DDref 是 **Fan diameter scale factor** 参数。

模块根据参考机械功率和风机相似定律计算轴扭矩：

τ=Φrefω2ωref3(DDref)5.

其中 *Φref* 是压力增益与风机效率之比：

Φref=qrefΔprefηref.

当您将 **Shaft power specification** 参数设置为 `Fan efficiency` 时，模块使用风机峰值性能 *ηnom* 与 0 之间效率的二次拟合。*ηnom* 等同于 **Nominal efficiency** 参数，模块将其解释为峰值效率。如果您将 **Shaft power specification** 参数设置为 `Brake power`，模块会根据峰值或标称条件下的标称制动功率 *Φnom* 推导标称风机效率：

ηnom=qnomΔpnomΦnom.

模块假定当没有流量或当流量达到零压力下的最大体积流量时效率为零。模块使用当前流量 *q* 计算参考流量：

qref=qωrefω(DrefD)3.

### 一维表格化数据参数化：压力作为参考轴转速下流量的函数

当您将 **Fan parameterization** 参数设置为 `1D tabulated data - static pressure vs. flow rate at reference shaft speed` 时，您可以将风机性能建模为体积流量的函数。模块从一维 **Static pressure gain vector** 参数 *Δpref(qref)* 插值从端口 **A** 到端口 **B** 的压力增益：

pB−pA=Δpref(qref)(ρρref)(ωωref)2(DDref)2.

这里，*ρ* 是湿空气密度，*ρref* 是参考密度，等同于 **Reference density** 参数。模块根据参考机械功率和风机相似定律计算轴扭矩：

τ=Φref(qref)ω2ωref3(ρρref)(DDref)5,

其中 *ρref* 是 **Reference density**。

模块使用当前流量 *q* 计算参考流量：

qref=qωrefω(DrefD)3.

当仿真超出所提供表的范围时，模块会基于风机曲线的平均斜率和到最近点的参考扭矩外推压力。

### 二维表格化数据参数化：压力作为轴转速和流量的函数

当您将 **Fan parameterization** 参数设置为 `2D 表格数据 - 静压与轴转速和 flow rate` 时，您可以将风机性能建模为体积流量和角速度的二维函数。模块从二维 **Static pressure gain table, dp(w,q)** 参数插值从端口 **A** 到端口 **B** 的压力增益。模块将参考压力增益 *Δpref(qref,ω)* 定义为

pB−pA=Δpref(qref,ω)(ρρref)(DDref)2.

模块根据参考机械功率和风机相似定律计算轴扭矩：

τ=Φref(qref,ω)ω(ρρref)(DDref)5,

其中参考机械功率是参考流量和当前轴转速的函数。

模块使用当前流量 *q* 计算参考流量：

qref=q(DrefD)3.

当仿真超出所提供表的范围时，模块会基于风机曲线的平均斜率和到最近点的参考扭矩外推压力。

**缺失数据**

如果表中存在未知数据点，请使用 `NaN` 代替这些值。该模块通过基于风机曲线平均斜率进行外推来填充 `NaN` 元素。不要使用人为数值，因为这些值会在该区域运行时扭曲风机行为。使用未知数据时：

- 表中的 `NaN` 元素必须连续。
- **Static pressure gain table, dp(w,q)**、**Efficiency table, eta(w,q)** 和 **Mechanical power table, W(w,q)** 参数中 `NaN` 元素的位置必须彼此匹配。
- `NaN` 元素必须位于表的右上部分，这对应于最高体积流量和最低轴转速。

### 二维表格数据参数化：流量作为轴转速和压力的函数

当您将 **Fan parameterization** 参数设置为 `2D
表格数据 - 流量与轴转速和静压的关系 pressure` 时，
您可以将通过风机的流量建模为压力和角速度的二维函数。体积流量从二维
**Volumetric flow rate table, q(w,dp)** 参数
*qref* 插值得到。参考流量是
参考压力增益
*Δpref* 和当前轴转速
*ω* 的函数：

q=qref(Δpref,ω)(DDref)3,

其中参考压力增益由风机上的压力
差推导得到：

Δpref=(pB−pA)(ρrefρ)(DrefD)2.

轴扭矩由参考机械功率和风机相似定律推导得到：

τ=Φref(Δpref,ω)ω(ρρref)(DDref)5,

其中参考机械功率是参考流量和
当前轴转速的函数。

当仿真超出所提供表格的范围时，该模块会基于风机曲线的平均斜率和参考
扭矩外推到最近点来计算压力。

**缺失数据**

如果您的表格中有未知数据点，请使用 `NaN` 代替这些
值。该模块会基于风机曲线的平均斜率通过外推来填充 `NaN` 元素。不要使用人为的数值，
因为这些值会在该区域运行时扭曲风机行为。
使用未知数据时：

- 表格中的 `NaN` 元素必须
  连续。
- **Volumetric flow rate table, q(w,dp)**、
  **Efficiency table, eta(w,dp)** 和
  **Mechanical power table, W(w,dp)**
  参数中 `NaN` 元素的位置
  必须彼此匹配。
- `NaN` 元素必须位于表格的右上
  部分，这对应于最高体积
  流量和最低轴转速。

### Power and Efficiency

您可以将轴功率指定为风机效率或制动功率。

该模块按如下公式计算效率

η=ΦfluidΦbrake,

其中 *制动功率*，即在轴处
测得的机械功率，为

Φbrake=τω.

该模块按如下公式计算流体功率

Φfluid=q(pB−pA).

该模块按如下公式计算扭矩

τ=Φbrakeω.

### Visualizing the Fan Curve

您可以通过绘制压力、功率、
效率和扭矩随流量变化的曲线来检查参数化后的风机性能。要生成当前
风机设置的图，请右键单击该模块并选择 **Fluids** > **Plot Fan Characteristics**。如果您更改设置或数据，请单击模块参数上的 **Apply**，然后单击风机曲线
图上的 **Reload Data**。

默认模块参数化会生成以下图：

风机特性曲线图

### 假设和限制

- 如果轴按照与指定机械方向相反的方向旋转，
  模块两端的压力差会降为零，结果可能不
  准确。
- 该模块假设风机是准稳态的。
- 该模块根据静压升来仿真风机性能，
  而不是风机全压。
