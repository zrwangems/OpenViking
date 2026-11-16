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

### 守恒

### **A** — 气体端口 gas

热交换器气体侧的入口或出口点。

### **B** — 气体端口 gas

热交换器气体侧的入口或出口点。

### **H** — 热边界 thermal

建模流体与热交换器接口之间的热边界。
### 输入

### **C** — 热容率 physical signal

气体流的热容率的瞬时值，指定为 physical signal。

### **HC** — 传热系数 physical signal

气体流与壁面之间的传热系数的瞬时值，指定为 physical signal。

## 参数

### 参数

### **最小自由流通面积** — 流道最窄处的横截面积 `0.01 m^2`（默认）| scalar with units of length squared

入口与出口之间最小的总流通横截面积。如果通道是管道、管、槽或沟槽的集合，则此参数的值是最小流通面积点处最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是某一横截面中管间间隙之和，其中间隙之和最小。

### **水力直径** — 圆形通道的直径或等效直径 `0.1 m`（默认）| scalar with units of length

流动的有效内径。如果横截面直径变化，则此参数的值是其最窄点处的直径。对于非圆形通道，水力直径是与现有通道面积相同的圆的等效直径。

如果通道是管道、管、槽或沟槽的集合，则总周长是该集合中各周长之和。如果通道是具有圆形横截面的单根管道或管，则水力直径等于真实直径。

### **气体体积** — 流道中包含的流体总体积 `0.01 m^3`（默认）| scalar with units of length squared

气体或热液体流道中包含的流体总体积。

### **层流上限雷诺数** — 层流与湍流状态之间过渡的起点 `2000`（默认）| scalar

从层流状态过渡到湍流状态的起点。高于此数值时，惯性力变得越来越占主导。默认值适用于表面光滑的圆形管道和管。

### **湍流下限雷诺数** — 层流与湍流状态之间过渡的终点 `4000`（默认）| scalar

从层流状态过渡到湍流状态的终点。低于此数值时，黏性力变得越来越占主导。默认值适用于表面光滑的圆形管道和管。

### **压降模型** — 由摩擦引起的压降的数学模型 `Pressure loss coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

由摩擦引起的压降的数学模型。此设置决定用于计算的表达式以及要指定为输入的模块参数。有关按参数化进行的计算，请参见 Heat Exchanger Interface (TL) 模块。

### **压降系数** — 端口之间所有流动阻力的总损失系数 `0.1`（默认）| scalar

流道中所有流动阻力的总损失系数，包括壁面摩擦（主要损失）以及由弯曲、弯头和其他几何变化引起的局部阻力（次要损失）。

损失系数是用于表示由摩擦引起的压降的经验性无量纲数。它可以根据实验数据计算，或从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **压降模型** 设置为 `Pressure loss coefficient`。

### **从入口到出口的流动路径长度** — 端口之间行进的距离 `1 m`（默认）| scalar with units of length

流动在端口之间必须行进的总距离。在多程壳管式交换器中，总距离是所有壳程的总和。在管束、波纹板和其他流动被分成并联分支的通道中，它是在单个分支中覆盖的距离。流动路径越长，壁面摩擦引起的主要压降越陡峭。

#### 依赖关系

要启用此参数，请将 **压降模型** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **局部阻力的总等效长度** — 以长度表示的次要压降总和 `0.1 m`（默认）| scalar with units of length

以长度表示的次要压降总和。直通道的长度会产生与弯头、三通和管接头现有局部阻力之和相等的损失。等效长度越大，局部阻力引起的次要压降越陡峭。

#### 依赖关系

要启用此参数，请将 **压降模型** 设置为 `Correlation for flow inside tubes`。

### **内表面绝对粗糙度** — 导致摩擦损失的壁面表面变化的平均高度 `15e-6 m`（默认）| scalar with units of length

导致摩擦损失的壁面表面变化的平均高度。平均高度越大，壁面越粗糙，由摩擦引起的压降越大。需要使用表面粗糙度来从 Haaland 关联式计算 Darcy 摩擦因子。

#### 依赖关系

要启用此参数，请将 **压降模型** 设置为 `Correlation for flow inside tubes`。

### **Darcy 摩擦因子的层流摩擦常数** — 层流条件下流通截面的压降修正 `64`（默认）| scalar

层流的压降修正。此参数称为形状因子，可用于推导层流状态中压降计算的 Darcy 摩擦因子。默认值适用于圆柱形管道和管。

非圆形横截面的一些附加形状因子可以由 Navier-Stokes 方程的解析解确定。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`。平行板之间的细长导管也具有形状因子 `96`。

#### 依赖关系

要启用此参数，请将 **压降模型** 设置为 `Correlation for flow inside tubes`。

### **Darcy 摩擦因子的雷诺数向量** — Darcy 摩擦因子查找表中每个断点处的雷诺数 numerical array

Darcy 摩擦因子查找表中每个断点处的雷诺数。该模块在断点之间插值并从断点外推，以获得任意雷诺数下的 Darcy 摩擦因子。插值由 MATLAB® `linear` 估计器处理，外推由 `nearest` 函数处理。

雷诺数必须大于零，并且从左到右单调增加。它们可以跨越层流、过渡和湍流状态。此向量中的值数必须等于 **Darcy 摩擦因子向量** 参数的大小，以计算表格断点。

#### 依赖关系

要启用此参数，请将 **压降模型** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy 摩擦因子向量** — 雷诺数查找表中每个断点处的 Darcy 摩擦因子 numerical array

雷诺数查找表中每个断点处的 Darcy 摩擦因子。该模块在断点之间插值并从断点外推，以获得任意雷诺数下的 Darcy 摩擦因子。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

Darcy 摩擦因子不得为负，并且必须按雷诺数递增的顺序从左到右排列。此向量中的值数必须等于 **Darcy 摩擦因子的雷诺数向量** 参数的大小，以计算表格断点。

#### 依赖关系

要启用此参数，请将 **压降模型** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Euler 数的雷诺数向量** — Euler 数查找表中每个断点处的雷诺数 numerical array

Euler 数查找表中每个断点处的雷诺数。该模块在断点之间插值并从断点外推，以获得任意 Euler 数下的雷诺数。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

雷诺数必须大于零，并且从左到右单调增加。它们可以跨越层流、过渡和湍流状态。此向量中的值数必须等于 **Euler 数向量** 参数的大小，以计算表格断点。

#### 依赖关系

要启用此参数，请将 **压降模型** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler 数向量** — 雷诺数查找表中每个断点处的 Euler 数 numerical array

雷诺数查找表中每个断点处的 Euler 数。该模块在断点之间插值并从断点外推，以获得任意雷诺数下的 Euler 数。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

Euler 数不得为负，并且必须按雷诺数递增的顺序从左到右排列。此向量中的值数必须等于 **Euler 数的雷诺数向量** 参数的大小，以计算表格断点。

#### 依赖关系

要启用此参数，请将 **压降模型** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **传热系数模型** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定要应用哪些表达式以及要为传热计算指定哪些参数。有关按参数化进行的计算，请参见 E-NTU Heat Transfer 模块。

### **气体-壁面传热系数** — 流体与壁面之间对流传热的传热系数 `100 W/(m^2 * K)`（默认）| scalar

流体与壁面之间对流传热的传热系数。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Constant heat transfer coefficient`。

### **传热表面积** — 流体与壁面之间传热所使用的有效表面积 `0.4 m^2`（默认）| scalar with units of length squared

流体与壁面之间传热所使用的有效表面积。有效表面积是一次和二次表面积之和，即壁面暴露于流体的面积以及翅片（如果使用）的面积。翅片表面积通常按翅片效率因子缩放。

### **传热流动路径长度** — 流体与壁面之间传热中经过的特征长度 `1 m`（默认）| scalar with units of length

流体与壁面之间传热的特征长度。此长度用于确定通道水力直径。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **层流传热的 Nusselt 数** — 层流中假定为常数的 Nusselt 数 `3.66`（默认）| positive scalar

层流的 Nusselt 数常数值。需要 Nusselt 数来计算流体与壁面之间的传热系数。默认值适用于圆柱形管道和管。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Correlation for flow inside tubes`。

### **Colburn 因子的雷诺数向量** — Colburn 因子查找表中每个断点处的雷诺数 numerical array

Colburn 因子查找表中每个断点处的雷诺数。该模块在断点之间插值并从断点外推，以获得任意雷诺数下的 Colburn 因子。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

雷诺数必须大于零，并且从左到右单调增加。它们可以跨越层流、过渡和湍流状态。此向量中的值数必须等于 **Colburn 因子向量** 参数的大小，以计算表格断点。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn 因子向量** — 雷诺数查找表中每个断点处的 Colburn 因子 numerical array

雷诺数查找表中每个断点处的 Colburn 因子。该模块在断点之间插值并从断点外推，以获得任意雷诺数下的 Colburn 因子。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

Colburn 因子必须为零或正数，并且必须按雷诺数递增的顺序从左到右排列。此向量中的值数必须等于 **Colburn 因子的雷诺数向量** 参数的大小，以计算表格断点。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Nusselt 数的雷诺数向量** — Nusselt 数查找表中每个断点处的雷诺数 numerical array

Nusselt 数查找表中每个断点处的雷诺数。雷诺数或 Prandtl 数均可作为自变量。该模块在断点之间插值并从断点外推，以获得任意雷诺数下的 Nusselt 数。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

雷诺数必须大于零，并且从左到右单调增加。它们可以跨越层流、过渡和湍流状态。向量的大小必须等于 **Nusselt number table, Nu(Re,Pr)** 参数中的行数。如果表有 *m* 行和 *n* 列，则雷诺数向量必须为 *m* 个元素长。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Prandtl number vector for Nusselt number** — 努塞尔数查找表中每个断点处的 Prandtl 数数值数组

努塞尔数查找表中每个断点处的 Prandtl 数。
Prandtl 数或 Reynolds 数均可作为自变量。模块在断点之间进行插值，并从断点外推，以获得任意 Prandtl 数下的努塞尔数。插值由 MATLAB `linear` 估计器处理，外推由 `nearest` 函数处理。

Prandtl 数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡和湍流状态。向量的大小必须等于 **Nusselt number table** 参数中的列数。如果表有 *m* 行和 *n* 列，则 Prandtl 数向量必须为 *n* 个元素长。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number table, Nu(Re,Pr)** — Reynolds-Prandtl 数查找表中每个断点处的努塞尔数数值数组

Reynolds-Prandtl 数查找表中每个断点处的努塞尔数。模块在断点之间进行插值，并从断点外推，以获得任意一对 Reynolds 数和 Prandtl 数下的努塞尔数。努塞尔数用于计算传热系数。

努塞尔数必须大于零。每个值必须按 Reynolds 数递增的顺序从上到下排列，并按 Prandtl 数递增的顺序从左到右排列。行数必须等于 **Reynolds number vector for Nusselt number** 参数的大小，列数必须等于 **Prandtl number vector for Nusselt number** 参数的大小。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Threshold mass flow rate for flow reversal** — 质量流率数值平滑区域的上界 `1e-4 kg/s`（默认）| 具有每单位时间质量单位的标量

应用数值平滑处理的质量流率下限。这样做是为了避免流动停滞期间出现不连续性。有关这些计算的详细信息，请参阅 Specific Dissipation Heat Exchanger Interface (G) 模块。

### 效应和初始条件

### **Enable dynamic compressibility** — 对气体通道中压力动态进行建模的选项 `On`（默认）| `Off`

对气体通道中压力动态进行建模的选项。如果清除此复选框，模块将从组件能量和质量守恒方程中移除压力导数项。

### **Nominal temperature** — 额定工况下的温度 `293.15 K`（默认）| 标量

额定工况下的气体温度。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖项

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal pressure** — 额定工况下的压力 `0.101325 MPa`（默认）| 标量

额定工况下的气体压力。当禁用动态可压缩性时，模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖项

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Initial pressure** — 仿真开始时的压力 `0.101325 MPa`（默认）| 标量

仿真开始时气体通道中的压力。

#### 依赖项

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Initial pressure priority** — 压力参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial pressure** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖项

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Initial temperature** — 仿真开始时的温度 `293.15 K`（默认）| 标量

仿真开始时气体通道中的温度。

### **Initial temperature priority** — 温度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial temperature** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

## 所属库

Simscape / Fluids / Heat Exchangers / Fundamental Components

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2025a：可选地对动态可压缩性建模

Heat Exchanger Interface (G) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性建模。以前，此模块始终对压力动态建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

## 描述

气体与其周围环境之间的热界面

Heat Exchanger Interface (G) 模块对热交换器内气体流的热传递进行建模。使用第二个热交换器模块对流体对进行建模。这些界面可以位于不同的流体域中，例如一个在液体中，一个在气体中。使用 E-NTU Heat Transfer 模块耦合这些界面并捕获流体之间的热交换。

### 质量平衡

模块的固定体积构造允许捕获由于可压缩性引起的流体质量流率变化。总质量累积速率等于通过端口的质量流率之和：

M˙=m˙A+m˙B,

其中 M˙ 是质量累积速率，m˙ 是质量流率。下标表示端口 **A** 和 **B**。当质量流率指向气体通道内部时为正。

当选择 **Enable dynamic compressibility** 时，质量累积速率会考虑密度的变化：

M˙=[(∂ρ∂p)udpdt+(∂ρ∂u)pdudt]V,

其中：

- *ρ* 是密度。
- *p* 是压力。
- *u* 是比内能。
- *V* 是体积。

当清除 **Enable dynamic compressibility** 复选框时，质量累积速率 M˙ 为零。

### 动量平衡

在热交换器的进口和出口端口之间平衡动量决定交换器内的流动方向和速度。动量变化主要由于管道转弯产生的摩擦损失，这些损失转化为压力变化。局部阻力，如弯头、肘管和三通，可能导致流动分离，从而造成额外的次要压力损失。对于稳态流动，质量流率保持恒定。

对气体（管道）体积的每个分段应用动量平衡。此图显示了一个分为两个体积和三个节点的管束。节点对应于端口 **A**、**B** 和流体体积 `I`。流体状态（如压力和温度）以及流体属性（如密度和粘度）在这些节点处定义。

请注意，流动惯性可忽略不计，并且流动被视为准稳态。瞬态向质量流率的转换可能被偏移：由于密度、压力和温度之间的耦合，变化在整个系统中的传播并非瞬时。不考虑其他动量源和汇，例如端口之间的水头差或通道壁的径向变形。端口 **A** 处半体积的动量平衡为：

pA−pI=Δpf,A,

其中 *p* 是下标所示节点处的压力。*Δp*f,A 是由于摩擦在端口节点和内部节点之间的总压力损失。总压力损失包括主要损失和次要损失。对于端口 **B** 处的半体积，动量平衡为：

pB−pI=Δpf,B.

### 摩擦

由于摩擦引起的压力变化在湍流中与质量流率的平方成正比，在层流中与质量流率的幅值成正比。这种压力变化由三个无量纲参数表征：Darcy 摩擦因子、压力损失系数和 Euler 数。根据 **Pressure loss model** 参数，这些数值通过经验关联式计算，或从查找表估算。

“层流”或“湍流”的分类基于 Reynolds 数。当 Reynolds 数高于 **Turbulent flow lower Reynolds number limit** 参数时，流动为完全湍流。低于 **Laminar flow upper Reynolds number limit** 参数时，流动为完全层流。介于这些值之间的 Reynolds 数表示过渡流。过渡流同时表现出层流和湍流的特征。在 Simscape™ Fluids™ 语言中，在这些边界值之间应用数值混合。

**`Correlation for flow inside tubes`**

对于管道，使用 Darcy 摩擦因子 *f*D。在端口 **A** 处的半体积中，动量平衡为：

pA−pI=fD,Am˙A|m˙A|2ρADHAMin2(L+LAdd2),

其中 *L* 是管道长度，*L*Add 是添加的管道长度，如果用它代替肘管、三通、管接头或其他局部阻力，将重现次要粘性损失。*A* 是管道横截面积；在横截面积不均匀的情况下，应使用 *A*min。*D*H 是管道水力直径，即面积等于管道横截面的圆的直径：

DH=4AMinπ.

如果管道具有圆形横截面，则水力直径与管道直径相同。

对于端口 **B** 处的半体积，动量平衡为：

pB−pI=fD,Bm˙B|m˙B|2ρBDHAMin2(L+LAdd2).

对于湍流，Darcy 摩擦因子使用 Haaland 关联式计算。Reynolds 数在边界端口处确定：

fD={−1.8log10[6.9Re+(ϵR3.7DH)1.11]}-2,

其中 *ε*R 是壁面粗糙度，取为特征高度。此参数在 **Internal surface absolute roughness** 参数中指定。

对于层流，摩擦因子取决于管道形状，并使用管道形状因子计算：

fD=λRe,

其中 *λ* 是形状因子。Reynolds 数在边界端口处计算为：

Re=DHm˙μAMin.

将 Re 代入端口 **A** 处的压力损失方程，动量平衡重新表述为：

pA−pI=λAμAm˙A2ρADH2AMin(L+LAdd2),

同样，对于端口 **B** 处的半体积，动量平衡为：

pB−pI=λBμBm˙B2ρBDH2AMin(L+LAdd2).

**使用压力损失系数**

对于非管道通道，使用压力损失系数 *ξ*。对于端口 **A** 处半体积中的湍流，动量平衡为：

pA−pI=12ξm˙A|m˙A|2ρAAMin2,

对于端口 **B** 处半体积中的湍流，动量平衡为：

pB−pI=12ξm˙B|m˙B|2ρBAMin2,

对于端口 **A** 处半体积中的层流，动量平衡为：

pA−pI=12ξReLm˙AμA2DHρAAMin,

其中 ReL 是 **Laminar flow upper Reynolds number limit** 模块参数。对于端口 **B** 处半体积中的层流，动量平衡为：

pB−pI=12ξReLm˙BμB2DHρBAMin

**使用 `Tabulated data - Darcy friction factor vs. Reynolds number`**

您可以使用表格数据根据 Reynolds 数确定管道流动的 Darcy 摩擦因子。对于端口 **A** 处的半体积，动量平衡为：

pA−pI=fD,Am˙A|m˙A|2ρADHAMin2(L+LAdd2).

对于端口 **B** 处的半体积，动量平衡为：

pB−pI=fD,Bm˙B|m˙B|2ρBDHAMin2(L+LAdd2).

对于湍流状态，摩擦因子由 Reynolds 数的表格函数确定：

fD=fD(Re).

表格函数的断点来自向量模块参数。**Reynolds number vector for Darcy friction factor** 参数指定自变量，**Darcy friction factor vector** 参数指定因变量。在断点之间应用线性插值。在表格数据范围之外，最近断点决定摩擦因子。

在层流状态中，摩擦因子由形状因子 *λ* 计算：

fD=λRe.

**使用 `Tabulated data - Euler number vs. Reynolds number`**

您可以使用表格数据根据 Reynolds 数确定 Euler 数。此计算取决于流态，Euler 数表示为 Reynolds 数的表格函数：

Eu=Eu(Re).

`Tabulated data - Euler number vs. Reynolds number` 中的断点由 Reynolds 数向量和 Euler 数向量指定。**Reynolds number vector for Euler number** 参数指定自变量，即 Reynolds 数，**Euler number vector** 参数指定因变量，即每个 Reynolds 数处的 Euler 数。线性插值用于确定断点之间的值。在表格数据范围之外，使用最近断点处的值。

对于湍流，端口 **A** 处半体积的动量平衡为：

pA−pI=EuAm˙A|m˙A|ρAAMin2,

其中 Eu 是端口 **A** 处的 Euler 数。对于湍流，端口 **B** 处半体积的动量平衡为：

pB−pI=EuAm˙B|m˙B|ρBAMin2.

对于端口 **A** 处半体积中的层流，动量平衡为：

pA−pI=EuLReLm˙AμA4DHρAAMin,

其中 ReL 是 **Laminar flow upper Reynolds number limit** 参数，EuL 是在该 Reynolds 数处从表格数据评估的 Euler 数。对于端口 **B** 处半体积中的层流，动量平衡为：

pB−pI=EuLReLm˙BμB4DHρBAMin,

### 能量平衡

能量可以通过两种方式进入和离开热界面：通过端口 **A** 和 **B** 的流体流动，以及通过端口 **H** 的热流。当选择 **Enable dynamic compressibility** 时，能量平衡为

∂E∂pdpdt+∂E∂TdTdt=ϕA+ϕB+QH,

其中：

- *E* 是热界面内部流体体积中的总能量。
- *ϕ*\* 是通过气体端口进入的能量流率。
- *Q* 是通过热端口进入的热流率。

如果清除 **Enable dynamic compressibility** 复选框，则能量平衡为

dEdt=ϕA+ϕB+QH,

其中总内部能量为

E=ρ0uV.

模块根据 **Nominal liquid temperature** 和 **Nominal liquid pressure** 参数计算常数 *ρ0*。

### Heat Transfer Rate

热交换器的两种流体之间的传热通过多种方式发生：在流体界面处的对流、通过积聚污垢层的导热，以及通过壁厚的导热。

传热延伸到气体通道之外，因此需要其他模块来对整个热交换器系统建模。第二个 heat exchanger interface 模块对第二流动通道建模，而 E-NTU Heat Transfer 模块对穿过壁面的热流建模。特定于气体通道、但 E-NTU Heat Transfer 模块所需的传热参数可通过物理信号端口获得：

- 端口 **C** 输出热容率，它衡量气体吸收热量的能力，并且是计算传热单元数 (NTU) 所必需的。热容率计算为：

  \(C_R = c_p \dot{m},\)

  其中 \(C_R\) 是热容率，\(c_p\) 是比热。

- 端口 **HC** 输出传热系数 \(U\)。

  如果将传热系数视为常数，则其值在整个流动通道内均匀。如果传热系数可变，则在每个端口根据以下表达式计算：

  \(U = \frac{\mathrm{Nu} \, k}{D_{H,Q}},\)

  其中 Nu 是努塞尔数，\(k\) 是导热系数，\(D_{H,Q}\) 是用于传热的水力直径。水力直径 \(D_{H,Q}\) 计算为：

  \(D_{H,Q} = \frac{4 A_{\mathrm{Min}} L_Q}{S_Q},\)

  其中 \(S_Q\) 是 **Heat transfer surface area** 参数，\(L_Q\) 是 **Length of flow path for heat transfer** 参数。

  平均传热系数的下界是 **Minimum gas-wall heat transfer coefficient** 参数。

### 努塞尔数

努塞尔数由与雷诺数和普朗特数的经验关联式导出。使用 **Heat transfer parametrization** 参数为您的仿真选择最合适的公式。

最简单的参数化 `Constant heat transfer coefficient` 直接从 **Gas-wall heat transfer coefficient** 参数的值获得传热系数。
`Correlation for flow inside tubes` 使用带有常数或计算参数的解析表达式来捕捉管内流动中努塞尔数对流态的依赖性。

其余参数化是雷诺数的表格函数。这些对于在不同流态下改变努塞尔数或传热系数很有用。这些函数由将雷诺数与 Colburn 因子关联起来，或将雷诺数和普朗特数与努塞尔数关联起来的实验数据生成。

**`Constant heat transfer coefficient`**

使用在 **Gas-wall heat transfer coefficient** 参数中指定的 `Constant heat transfer coefficient`，将传热系数设为常数，并且在计算中不使用努塞尔数。将此参数化用作局限于层流流态的气体流动的简单近似。

**`Correlation for tubes`**

使用 `Correlation for tubes` 时，努塞尔数取决于流态。对于湍流，其值随雷诺数成比例变化，并根据 Gnielinski 关联式计算：

\[
Nu = \frac{\frac{f}{8}(Re - 1000)Pr}{1 + 12.7 \sqrt{\frac{f}{8}}(Pr^{2/3} - 1)},
\]

其中 Re 是雷诺数，Nu 是努塞尔数，Pr 是普朗特数。摩擦因子 \(f\) 与管压降计算中使用的因子相同。对于层流，努塞尔数为常数。其值从 **Nusselt number for laminar flow heat transfer** 参数 \(Nu_L\) 获得：

\[
Nu = Nu_L.
\]

**使用 `Tabulated data - Colburn factor vs. Reynolds number`**

您可以使用表格数据根据雷诺数确定 Colburn 因子。Colburn 方程用于确定努塞尔数，努塞尔数与雷诺数成比例变化。Colburn \(j\) 因子是雷诺数、普朗特数和努塞尔数之间比例关系的度量：

\[
Nu = j(Re_Q) Re_Q Pr^{1/3}.
\]

\(Re_Q\) 是基于用于传热的水力直径 \(D_{H,Q}\) 和通道最小自由流动面积 \(A_{\mathrm{Min}}\) 的雷诺数：

\[
Re_Q = \frac{\dot{m} D_{H,Q}}{A_{\mathrm{Min}} \mu}
\]

**使用 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`**

您可以使用表格函数根据普朗特数和雷诺数确定努塞尔数。线性插值用于确定断点之间的值。努塞尔数是 Re 和 Pr 两者的函数，因此 **Reynolds number vector for Nusselt number**、**Prandtl number vector for Nusselt number** 和 **Nusselt number table, Nu(Re,Pr)** 参数定义表格断点：

\[
Nu = Nu(Re_Q, Pr).
\]

表格中的雷诺数必须使用用于传热的水力直径 \(D_{H,Q}\) 计算。
