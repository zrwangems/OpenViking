---
type: simulink-block
title: 'Heat Exchanger Interface (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Fundamental Components'
documentation_page: 'heatexchangerinterfaceg'
documentation_source_path: 'ref/heatexchangerinterfaceg.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger Interface (G)

## 端口

### 守恒端口

### **A** — 气体端口 gas

换热器气体侧的入口或出口点。

### **B** — 气体端口 gas

换热器气体侧的入口或出口点。

### **H** — 热边界 thermal

被建模流体与换热器接口之间的热边界。
### 输入

### **C** — 热容率 physical signal

气体流量的热容率瞬时值，指定为物理信号。

### **HC** — 传热系数 physical signal

气体流量与壁面之间传热系数的瞬时值，指定为物理信号。

## 参数

### 参数

### **Minimum free-flow area** — 流道最窄点处的横截面积 `0.01 m^2`（默认）| 具有长度平方单位的标量

入口与出口之间最小的总横截流动面积。如果通道是由管道、管子、槽或沟组成的集合，则此参数的值是最小流动面积点处各最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是在某一横截面中管子之间间隙之和最小的那个横截面中管子之间间隙之和。

### **Hydraulic diameter** — 圆形通道的直径或等效直径 `0.1 m`（默认）| 具有长度单位的标量

流动的有效内径。如果横截面直径发生变化，则此参数的值是最窄点处的直径。对于非圆形通道，水力直径是与现有通道面积相同的圆的等效直径。

如果通道是由管道、管子、槽或沟组成的集合，则总周长是该集合中各周长之和。如果通道是具有圆形横截面的单根管道或管子，则水力直径等于真实直径。

### **Gas volume** — 流道中包含的流体总体积 `0.01 m^3`（默认）| 具有长度平方单位的标量

气体或热液体流道中包含的流体总体积。

### **Laminar flow upper Reynolds number limit** — 层流与湍流状态之间过渡的起点 `2000`（默认）| 标量

从层流状态过渡到湍流状态的起点。高于此数值时，惯性力逐渐占主导地位。默认值适用于表面光滑的圆形管道和管子。

### **Turbulent flow lower Reynolds number limit** — 层流与湍流状态之间过渡的终点 `4000`（默认）| 标量

从层流状态过渡到湍流状态的终点。低于此数值时，黏性力逐渐占主导地位。默认值适用于表面光滑的圆形管道和管子。

### **Pressure loss model** — 摩擦压降的数学模型 `Pressure loss coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

摩擦压降的数学模型。此设置决定用于计算的表达式以及需要指定为输入的模块参数。有关按参数化进行的计算，请参见 Heat Exchanger Interface (TL) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1`（默认）| 标量

流道中所有流动阻力的总损失系数，包括壁面摩擦（主要损失）以及由弯头、肘管和其他几何变化引起的局部阻力（次要损失）。

损失系数是用于表示摩擦压降的经验性无量纲数。它可以通过实验数据计算或从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从端口到端口行进的距离 `1 m`（默认）| 具有长度单位的标量

流体在端口之间必须行进的总距离。在多程管壳式换热器中，总距离是所有壳程距离之和。在管束、波纹板和其他流动被分成平行分支的通道中，它是单个分支中覆盖的距离。流动路径越长，壁面摩擦引起的主要压降越陡。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 以长度表示的局部次要压降总和 `0.1 m`（默认）| 具有长度单位的标量

以长度表示的局部次要压降总和。直通道的长度产生的损失等效于弯头、三通和接头等现有局部阻力之和。等效长度越大，局部阻力引起的次要压降越陡。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 导致摩擦损失的壁面表面变化平均高度 `15e-6 m`（默认）| 具有长度单位的标量

导致摩擦损失的壁面表面变化的平均高度。平均高度越大，壁面越粗糙，摩擦引起的压降越大。需要表面粗糙度以从 Haaland 关联式推导 Darcy 摩擦因子。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流动横截面的压降修正 `64`（默认）| 标量

层流的压降修正。此参数称为形状因子，可用于推导层流状态下压降计算的 Darcy 摩擦因子。默认值适用于圆柱形管道和管子。

一些非圆形横截面的附加形状因子可以从 Navier-Stokes 方程的解析解中确定。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`。平行板之间的细长导管也具有形状因子 `96`。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的 Reynolds 数 数值数组

Darcy 摩擦因子查找表中每个断点处的 Reynolds 数。该模块在断点之间进行插值并从断点外推，以获得任意 Reynolds 数下的 Darcy 摩擦因子。插值由 MATLAB® `linear` 估计器处理，外推由 `nearest` 函数处理。

Reynolds 数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡和湍流状态。此向量中的值数量必须等于 **Darcy friction factor vector** 参数的大小，以计算表格断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — 雷诺数查找表中每个断点处的 Darcy 摩擦因子 数值数组

雷诺数查找表中每个断点处的 Darcy 摩擦因子。该模块在断点之间进行插值，并从断点外推，以获得任意雷诺数下的 Darcy 摩擦因子。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

Darcy 摩擦因子不得为负，并且必须按雷诺数递增的顺序从左到右排列。此向量中的值数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，以计算表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — Euler 数查找表中每个断点处的雷诺数 数值数组

Euler 数查找表中每个断点处的雷诺数。该模块在断点之间进行插值，并从断点外推，以获得任意 Euler 数下的雷诺数。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

雷诺数必须大于零，并且必须从左到右单调递增。它们可以跨越层流、过渡流和湍流状态。此向量中的值数量必须等于 **Euler number vector** 参数的大小，以计算表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler number vector** — 雷诺数查找表中每个断点处的 Euler 数 数值数组

雷诺数查找表中每个断点处的 Euler 数。该模块在断点之间进行插值，并从断点外推，以获得任意雷诺数下的 Euler 数。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

Euler 数不得为负，并且必须按雷诺数递增的顺序从左到右排列。此向量中的值数量必须等于 **Reynolds number vector for Euler number** 参数的大小，以计算表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Heat transfer coefficient model** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定传热计算中应用哪些表达式以及指定哪些参数。有关按参数化进行的计算，请参见 E-NTU Heat Transfer 模块。

### **Gas-wall heat transfer coefficient** — 流体与壁面之间对流传热系数 `100 W/(m^2 * K)`（默认）| 标量

流体与壁面之间对流传热系数。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Constant heat transfer coefficient`。

### **Heat transfer surface area** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2`（默认）| 单位为长度平方的标量

流体与壁面之间传热所用的有效表面积。有效表面积是一次表面积和二次表面积之和，即壁面暴露于流体的面积以及翅片（如果使用）的面积。翅片表面积通常按翅片效率因子进行缩放。

### **Length of flow path for heat transfer** — 流体与壁面之间传热所经过的特征长度 `1 m`（默认）| 单位为长度的标量

流体与壁面之间传热的特征长度。此长度用于确定通道水力直径。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number for laminar flow heat transfer** — 层流中 Nusselt 数所采用的常数 `3.66`（默认）| 正标量

层流中 Nusselt 数的常数值。计算流体与壁面之间的传热系数需要 Nusselt 数。默认值适用于圆柱形管道和管件。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Colburn factor** — Colburn 因子查找表中每个断点处的雷诺数 数值数组

Colburn 因子查找表中每个断点处的雷诺数。该模块在断点之间进行插值，并从断点外推，以获得任意雷诺数下的 Colburn 因子。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

雷诺数必须大于零，并且必须从左到右单调递增。它们可以跨越层流、过渡流和湍流状态。此向量中的值数量必须等于 **Colburn factor vector** 参数的大小，以计算表格化断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn factor vector** — 雷诺数查找表中每个断点处的 Colburn 因子 数值数组

雷诺数查找表中每个断点处的 Colburn 因子。该模块在断点之间进行插值，并从断点外推，以获得任意雷诺数下的 Colburn 因子。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

Colburn 因子必须为零或正，并且必须按雷诺数递增的顺序从左到右排列。此向量中的值数量必须等于 **Reynolds number vector for Colburn factor** 参数的大小，以计算表格化断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Reynolds number vector for Nusselt number** — Nusselt 数查找表中每个断点处的雷诺数 数值数组

Nusselt 数查找表中每个断点处的雷诺数。雷诺数或 Prandtl 数均可作为自变量。该模块在断点之间进行插值，并从断点外推，以获得任意雷诺数下的 Nusselt 数。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

雷诺数必须大于零，并且必须从左到右单调递增。它们可以跨越层流、过渡流和湍流状态。向量的大小必须等于 **Nusselt number table, Nu(Re,Pr)** 参数中的行数。如果表有 *m* 行和 *n* 列，则雷诺数向量必须包含 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt 数对应的 Prandtl 数向量** — Nusselt 数查找表中每个断点处的 Prandtl 数数值数组

Nusselt 数查找表中每个断点处的 Prandtl 数。
Prandtl 数或 Reynolds 数均可作为自变量。该模块在断点之间进行插值并从断点外推，以获得任意 Prandtl 数下的 Nusselt 数。
插值由 MATLAB 的 `linear` 估计器处理，外推由 `nearest` 函数处理。

Prandtl 数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡和湍流区域。该向量的大小必须等于 **Nusselt 数表** 参数中的列数。如果该表有 *m* 行和 *n* 列，则 Prandtl 数向量的长度必须为 *n* 个元素。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt 数表，Nu(Re,Pr)** — Reynolds-Prandtl 数查找表中每个断点处的 Nusselt 数数值数组

Reynolds-Prandtl 数查找表中每个断点处的 Nusselt 数。该模块在断点之间进行插值并从断点外推，以获得任意一对 Reynolds 数和 Prandtl 数下的 Nusselt 数。Nusselt 数用于计算传热系数。

Nusselt 数必须大于零。每个值必须按 Reynolds 数递增的顺序从上到下排列，并按 Prandtl 数递增的顺序从左到右排列。行数必须等于 **Nusselt 数对应的 Reynolds 数向量** 参数的大小，列数必须等于 **Nusselt 数对应的 Prandtl 数向量** 参数的大小。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **流动反向的阈值质量流量** — 质量流量数值平滑区域的上界 `1e-4 kg/s`（默认）| 单位为质量每单位时间的标量

低于该质量流量时应用数值平滑。这样做是为了避免流动停滞期间出现不连续。有关这些计算的更多信息，请参见 Specific Dissipation Heat Exchanger Interface (G) 模块。

### 效应和初始条件

### **启用动态可压缩性** — 用于对气体通道中的压力动态建模的选项 `On`（默认）| `Off`

用于对气体通道中的压力动态建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **标称温度** — 标称工况下的温度 `293.15 K`（默认）| 标量

标称工况下的气体温度。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程中的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

### **标称压力** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的气体压力。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程中的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

### **初始压力** — 仿真开始时的压力 `0.101325 MPa`（默认）| 标量

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**。

### **初始压力优先级** — 压力参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化该模块时分配给 **初始压力** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请选择 **启用动态可压缩性**。

### **初始温度** — 仿真开始时的温度 `293.15 K`（默认）| 标量

仿真开始时气体通道中的温度。

### **初始温度优先级** — 温度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化该模块时分配给 **初始温度** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

## 所属库

Simscape / Fluids / Heat Exchangers / Fundamental Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2025a：可选地对动态可压缩性建模

Heat Exchanger Interface (G) 模块现在可以通过 **启用动态可压缩性** 参数可选地对动态可压缩性建模。此前，该模块始终对压力动态建模，这可能导致模型需要更长时间才能达到稳态。清除 **启用动态可压缩性** 参数可防止动态可压缩性建模。

## 描述

气体与其周围环境之间的热接口

Heat Exchanger Interface (G) 模块对热交换器内气体流动的热传递进行建模。使用第二个热交换器模块对流体对进行建模。这些接口可以位于不同的流体域中，例如一个在液体中，一个在气体中。使用 E-NTU Heat Transfer 模块耦合这些接口并捕获流体之间的热交换。

### 质量平衡

该模块的固定体积构造使您能够捕获由于可压缩性引起的流体质量流量变化。总质量累积速率等于通过端口的质量流量之和：

M˙=m˙A+m˙B，

其中 M˙ 是质量累积速率，m˙ 是质量流量。下标表示端口 **A** 和 **B**。当质量流量导入气体通道时，其为正值。

当您选择 **启用动态可压缩性** 时，质量累积速率会考虑密度变化：

M˙=[(∂ρ∂p)udpdt+(∂ρ∂u)pdudt]V，

其中：

- *ρ* 是密度。
- *p* 是压力。
- *u* 是比内能。
- *V* 是体积。

当您清除 **启用动态可压缩性** 复选框时，质量累积速率 M˙ 为零。

### Momentum Balance

热交换器入口和出口端口之间的动量平衡决定了交换器内的流动方向和速度。动量变化主要归因于管道转弯处的摩擦损失，这些损失转化为压力变化。局部阻力，如弯管、弯头和T形管，可能导致流动分离，从而产生较小的附加压力损失。对于稳态流动，质量流量保持恒定。

动量平衡应用于气体（管道）体积的每一段。该图显示了一个分为两个体积和三个节点的管束。节点对应于端口 **A**、**B** 以及流体体积 `I`。流体状态（如压力和温度）以及流体属性（如密度和粘度）在这些节点处定义。

注意，流动惯性可忽略不计，流动被视为准稳态。瞬态向质量流量的转换可能存在偏移：由于密度、压力和温度之间的耦合，变化在整个系统中的传播并非瞬时。不考虑其他动量源和汇，例如端口之间的水头差或通道壁的径向变形。端口 **A** 处半体积的动量平衡为：

pA−pI=Δpf,A，

其中 *p* 是下标所示节点处的压力。*Δp*f,A 是由于摩擦在端口节点和内部节点之间的总压力损失。总压力损失包括沿程损失和局部损失。对于端口 **B** 处的半体积，动量平衡为：

pB−pI=Δpf,B。

### Friction

由于摩擦引起的压力变化，对于湍流，与质量流量的平方成正比；对于层流，与质量流量的大小成正比。这种压力变化由三个无量纲参数表征：Darcy 摩擦因子、压力损失系数和 Euler 数。根据 **Pressure loss model** 参数，这些数值由经验关联式计算或从查找表中估算。

“层流”或“湍流”的分类基于 Reynolds 数。当 Reynolds 数高于 **Turbulent flow lower Reynolds number limit** 参数时，流动为完全湍流。低于 **Laminar flow upper Reynolds number limit** 参数时，流动为完全层流。介于这些值之间的 Reynolds 数表示过渡流。过渡流表现出层流和湍流的双重特性。在 Simscape™ Fluids™ 语言中，在这些边界值之间应用数值混合。

**`Correlation for flow inside tubes`**

对于管道，使用 Darcy 摩擦因子 *f*D。在端口 **A** 处的半体积中，动量平衡为：

pA−pI=fD,Am˙A|m˙A|2ρADHAMin2(L+LAdd2)，

其中 *L* 是管道长度，*L*Add 是附加管道长度，如果用来代替弯头、T形管、管接头或其他局部阻力，将再现局部粘性损失。*A* 是管道横截面积；在横截面积不均匀的情况下，应使用 *A*min。*D*H 是管道水力直径，即与管道横截面积相等的圆的直径：

DH=4AMinπ。

如果管道具有圆形横截面，则水力直径与管道直径相同。

对于端口 **B** 处的半体积，动量平衡为：

pB−pI=fD,Bm˙B|m˙B|2ρBDHAMin2(L+LAdd2)。

对于湍流，Darcy 摩擦因子使用 Haaland 关联式计算。Reynolds 数在边界端口处确定：

fD={−1.8log10[6.9Re+(ϵR3.7DH)1.11]}-2，

其中 *ε*R 是壁面粗糙度，取为特征高度。该参数在 **Internal surface absolute roughness** 参数中指定。

对于层流，摩擦因子取决于管道形状，并使用管道形状因子计算：

fD=λRe，

其中 *λ* 是形状因子。Reynolds 数在边界端口处计算为：

Re=DHm˙μAMin。

将 Re 代入端口 **A** 处的压力损失方程，动量平衡重新表述为：

pA−pI=λAμAm˙A2ρADH2AMin(L+LAdd2)，

同样，对于端口 **B** 处的半体积，动量平衡为：

pB−pI=λBμBm˙B2ρBDH2AMin(L+LAdd2)。

**使用压力损失系数**

对于管道以外的通道，使用压力损失系数 *ξ*。对于端口 **A** 处半体积中的湍流，动量平衡为：

pA−pI=12ξm˙A|m˙A|2ρAAMin2，

对于端口 **B** 处半体积中的湍流，动量平衡为：

pB−pI=12ξm˙B|m˙B|2ρBAMin2，

对于端口 **A** 处半体积中的层流，动量平衡为：

pA−pI=12ξReLm˙AμA2DHρAAMin，

其中 ReL 是 **Laminar flow upper Reynolds number limit** 模块参数。对于端口 **B** 处半体积中的层流，动量平衡为：

pB−pI=12ξReLm˙BμB2DHρBAMin

**Using `Tabulated data - Darcy friction factor vs. Reynolds number`**

您可以使用表格数据来确定管流中基于 Reynolds 数的 Darcy 摩擦因子。对于端口 **A** 处的半体积，动量平衡为：

pA−pI=fD,Am˙A|m˙A|2ρADHAMin2(L+LAdd2)。

对于端口 **B** 处的半体积，动量平衡为：

pB−pI=fD,Bm˙B|m˙B|2ρBDHAMin2(L+LAdd2)。

对于湍流区域，摩擦因子由 Reynolds 数的表格函数确定：

fD=fD(Re)。

表格函数的断点来自向量模块参数。**Reynolds number vector for Darcy friction factor** 参数指定自变量，**Darcy friction factor vector** 参数指定因变量。断点之间应用线性插值。在表格数据范围之外，最近的断点决定摩擦因子。

在层流区域，摩擦因子由形状因子 *λ* 计算：

fD=λRe。

**Using `Tabulated data - Euler number vs. Reynolds number`**

您可以使用表格数据来确定基于 Reynolds 数的 Euler 数。该计算取决于流态，Euler 数表示为 Reynolds 数的表格函数：

Eu=Eu(Re)。

`Tabulated data - Euler number vs. Reynolds number` 中的断点由 Reynolds 数向量和 Euler 数向量指定。**Reynolds number vector for Euler number** 参数指定自变量，即 Reynolds 数，**Euler number vector** 参数指定因变量，即每个 Reynolds 数处的 Euler 数。使用线性插值确定断点之间的值。在表格数据范围之外，使用最近断点处的值。

对于湍流，端口 **A** 处半体积的动量平衡为：

pA−pI=EuAm˙A|m˙A|ρAAMin2，

其中 Eu 是端口 **A** 处的 Euler 数。对于湍流，端口 **B** 处半体积的动量平衡为：

pB−pI=EuAm˙B|m˙B|ρBAMin2。

对于端口 **A** 处半体积中的层流，动量平衡为：

pA−pI=EuLReLm˙AμA4DHρAAMin，

其中 ReL 是 **Laminar flow upper Reynolds number limit** 参数，EuL 是在该 Reynolds 数处从表格数据评估的 Euler 数。对于端口 **B** 处半体积中的层流，动量平衡为：

pB−pI=EuLReLm˙BμB4DHρBAMin，

### Energy Balance

能量可以通过两种方式进入和离开热接口：通过端口 **A** 和 **B** 的流体流动，以及通过端口 **H** 的热流。当您选中 **Enable dynamic compressibility** 时，能量平衡为

∂E∂pdpdt+∂E∂TdTdt=ϕA+ϕB+QH,

其中：

- *E* 是热接口内部流体体积中的总能量。
- *ϕ*\* 是通过气体端口进入的能量流率。
- *Q* 是通过热端口进入的热流率。

如果您清除 **Enable dynamic compressibility** 复选框，能量平衡为

dEdt=ϕA+ϕB+QH,

其中总内能为

E=ρ0uV.

该模块根据 **Nominal liquid temperature** 和 **Nominal liquid pressure** 参数计算常数 *ρ0*。

### Heat Transfer Rate

两种热交换器流体之间的热传递以多种方式发生：通过流体界面处的对流、通过积聚污垢层的传导，以及通过壁厚的传导。

热传递超出气体通道范围，因此需要其他模块来建模整个热交换器系统。第二个热交换器接口模块对第二个流动通道建模，而 E-NTU Heat Transfer 模块对穿过壁面的热流建模。特定于气体通道但 E-NTU Heat Transfer 模块所需的热传递参数可通过物理信号端口获得：

- 端口 **C** 输出热容率，它衡量气体吸收热量的能力，并且是计算传热单元数 (NTU) 所需的。热容率计算如下：

  CR=cpm˙,

  其中 *C*R 是热容率，*c*p 是比热。
- 端口 **HC** 输出传热系数 *U*。

  如果传热系数被视为常数，则其值在整个流动通道内是均匀的。如果传热系数是可变的，则在每个端口根据以下表达式计算：

  U=NukDH,Q,

  其中 Nu 是努塞尔数，*k* 是热导率，*D*H,Q 是用于热传递的水力直径。水力直径 *D*H,Q 计算如下：

  DH,Q=4AMinLQSQ,

  其中 *S*Q 是 **Heat transfer surface area** 参数，*L*Q 是 **Length of flow path for heat transfer** 参数。

  平均传热系数的下界是 **Minimum gas-wall heat transfer coefficient** 参数。

### Nusselt Number

努塞尔数由与雷诺数和普朗特数的经验关联式导出。使用 **Heat transfer parametrization** 参数为您的仿真选择最合适的公式。

最简单的参数化 `Constant heat transfer coefficient` 直接从 **Gas-wall heat transfer coefficient** 参数的值获得传热系数。`Correlation for flow inside tubes` 使用带有常数或计算参数的分析表达式来捕捉管流中努塞尔数对流态的依赖性。

其余参数化是雷诺数的表格函数。这些对于在流态之间变化的努塞尔数或传热系数很有用。这些函数由将雷诺数与科尔本因子关联，或将雷诺数和普朗特数与努塞尔数关联的实验数据生成。

**`Constant heat transfer coefficient`**

使用在 **Gas-wall heat transfer coefficient** 参数中指定的 `Constant heat transfer coefficient`，将传热系数设置为常数，并且在计算中不使用努塞尔数。使用此参数化作为限制在层流状态的气体流动的简单近似。

**`Correlation for tubes`**

当使用 `Correlation for tubes` 时，努塞尔数取决于流态。对于湍流，其值与雷诺数成比例变化，并根据 Gnielinski 关联式计算：

Nu=f8(Re−1000)Pr1+12.7f8(Pr2/3−1),

其中 Re 是雷诺数，Nu 是努塞尔数，Pr 是普朗特数。摩擦因子 *f* 与管压降计算中使用的因子相同。对于层流，努塞尔数是常数。其值从 **Nusselt number for laminar flow heat transfer** 参数 NuL 获得：

Nu=NuL.

**使用 `Tabulated data - Colburn factor vs. Reynolds number`**

您可以使用表格数据根据雷诺数确定科尔本因子。科尔本方程用于确定努塞尔数，其与雷诺数成比例变化。科尔本 *j* 因子是雷诺数、普朗特数和努塞尔数之间比例关系的度量：

Nu=j(ReQ)ReQPr1/3.

ReQ 是基于用于热传递的水力直径 *D*H, Q 以及通道最小自由流动面积 *A*Min 的雷诺数：

ReQ=m˙DH,QAMinμ

**使用 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`**

您可以使用表格函数根据普朗特数和雷诺数确定努塞尔数。线性插值用于确定断点之间的值。努塞尔数是 Re 和 Pr 两者的函数，因此 **Reynolds number vector for Nusselt number**、**Prandtl number vector for Nusselt number** 和 **Nusselt number table, Nu(Re,Pr)** 参数定义表格断点：

Nu=Nu(ReQ,Pr).

表格中的雷诺数必须使用用于热传递的水力直径 *D*H,Q 计算。
