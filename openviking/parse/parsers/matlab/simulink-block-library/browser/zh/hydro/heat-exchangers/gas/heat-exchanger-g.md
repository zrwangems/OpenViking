---
type: simulink-block
title: 'Heat Exchanger (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Gas'
documentation_page: 'heatexchangerg'
documentation_source_path: 'ref/heatexchangerg.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger (G)

## 端口

### 守恒

### **A1** — 气体端口 gas

用于气体进入和离开热交换器其侧的开口。

### **B1** — 气体端口 gas

用于气体进入和离开热交换器其侧的开口。

### **H2** — 受控流体 2 的入口温度 thermal

受控流体 2 的入口温度。

### 输入

### **C2** — 热容率 physical signal

受控流体的热容率的瞬时值。

### **HC2** — 传热系数 physical signal

受控流体与壁之间的传热系数的瞬时值。

## 参数

### 通用

### **Flow arrangement** — 流体在热交换器中排列的方式 `Parallel or counter flow`（默认） | `Shell and tube` | `Cross flow` | `Generic - effectiveness table`

流体在热交换器中排列的方式。流体可以彼此平行流动、彼此逆向流动或彼此交叉流动。它们还可以在加压壳体内流动，一种流体穿过封闭在壳体内的管，另一种流体围绕这些管流动。通过基于表格化效能数据的通用参数化，可以实现其他流动布置，并且几乎不需要热交换器的详细信息。

### **Number of shell passes** — 流体在离开前穿过壳体的次数 `1`（默认） | unitless scalar

流体在离开前穿过壳体的次数。

#### 依赖项

要启用此参数，请将 **Flow arrangement** 设为 `Shell and tube`。

### **Cross flow type** — 每个流动通道中的混合条件 `Both fluids mixed`（默认） | `Both fluids unmixed` | `Gas mixed & Controlled Fluid unmixed` | `Gas unmixed & Controlled Fluid mixed`

每个流动通道中的混合条件。此上下文中的混合是指流体沿其流动通道向出口前进时的横向运动。各流动彼此保持分离。未混合流动常见于带有板、折流板或翅片的通道中。此设置反映在热交换器的效能中，未混合流动效能最高，混合流动效能最低。

#### 依赖项

要启用此参数，请将 **Flow arrangement** 设为 `Shell and tube`。

### **Number of heat transfer units vector, NTU** — 热交换器效能查找表中每个断点处的传热单元数 unitless numerical array

热交换器效能数查找表中每个断点处的传热单元数。该表是二维的，传热单元数和热容量比都用作独立坐标。模块对断点进行内插和外推，以获得任意传热单元数下的效能。插值为 `linear`，外推为 `nearest`。

指定的数值必须大于零，并且从左到右单调递增。该向量的大小必须等于 **Effectiveness table** 参数的行数。如果该表有 *m* 行和 *n* 列，则传热单元数的向量长度必须为 *m* 个元素。

#### 依赖项

要启用此参数，请将 **Flow arrangement** 设为 `Generic - effectiveness table`。

### **Thermal capacity ratio vector, CR** — 热交换器效能查找表中每个断点处的热容量比 unitless numerical array

热交换器效能查找表中每个断点处的热容量比。该表是二维的，传热单元数和热容率比都用作独立坐标。模块对断点进行内插和外推，以获得任意热容量比下的效能。插值为 `linear`，外推为 `nearest`。

热容量比必须大于零，并且从左到右单调递增。该向量的大小必须等于 **Nusselt number table** 参数的列数。如果该表有 *m* 行和 *n* 列，则热容量比的向量长度必须为 *n* 个元素。热容量比是最小热容率与最大热容率的比值。

#### 依赖项

要启用此参数，请将 **Flow arrangement** 设为 `Generic - effectiveness table`。

### **Effectiveness table, E(NTU,CR)** — 在传热单元数和热容量比上的查找表中每个断点处的热交换器效能 unitless numerical array

在传热单元数和热容量比上的查找表中每个断点处的热交换器效能。模块对断点进行内插和外推，以获得任意传热单元数和热容量比组合下的效能。插值为 `linear`，外推为 `nearest`。

效能值不得为负。它们必须从上到下按传热单元数递增的顺序排列，并从左到右按热容量比递增的顺序排列。行数必须等于 **Number of heat transfer units vector** 参数的大小，列数必须等于 **Thermal capacity ratio vector** 参数的大小。

#### 依赖项

要启用此参数，请将 **Flow arrangement** 设为 `Generic - effectiveness table`。

### **Wall thermal resistance** — 壁对热传导热流的阻力 `0 K/W`（默认） | scalar with units of temperature over power

壁对热传导热流的阻力，也是热导的倒数，或热导率与表面积与长度之比的乘积。壁阻力与对流阻力和污垢阻力相加，以确定流体之间的总传热系数。

### **Enable wall thermal mass** — 对壁热质量建模的选项 `off`（默认） | `on`

是否对热交换器壁热质量建模。对壁热质量建模会引入壁对温度或热通量变化的瞬态响应延迟。如果清除 **Enable wall thermal mass**，模块将假定壁足够薄，以至于在传热的时间尺度上瞬态响应是瞬时的。

### **Wall mass** — 热交换器壁质量 `1 kg`（默认） | positive scalar

热交换器壁的质量。模块使用此值计算壁热质量。

#### 依赖项

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 热交换器壁比热 `490 J/(K*kg)`（默认） | positive scalar

热交换器壁的比热。模块使用此值计算壁热质量。

#### 依赖项

要启用此参数，请选择 **Enable wall thermal mass**。

### 气体

### **Minimum free-flow area** — 流动通道在其最窄点处的横截面积 `0.01 m^2`（默认） | scalar with units of length squared

入口和出口之间最小的总横截流动面积。如果通道是管道、管子、槽或沟槽的集合，则此参数的值为最小流动面积点处最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值为一个横截面中管子之间间隙之和最小处的间隙之和。

### **Gas volume** — 气体流动通道中流体的总体积 `0.01 m^3`（默认） | scalar with units of length squared

气体流动通道中包含的流体总体积。

### **Hydraulic diameter for pressure loss** — 流动通道在其最窄点处的有效直径 `0.1 m`（默认） | scalar with units of length

流动在其最窄点处的有效内径。对于横截面不是圆形的通道，该直径为与流动横截面积相等的假想圆的直径。其值为最小自由流动面积与其总周长四分之一之比。

如果通道是管道、管子、槽或沟槽的集合，则总周长为该集合中各周长之和。如果通道是单根管道或管子且横截面为圆形，则水力直径与真实直径相同。

### **Laminar flow upper Reynolds number limit** — 层流区和湍流区之间过渡的起点 `2000`（默认） | unitless scalar

层流区和湍流区之间过渡的起点。高于此数值时，惯性力占主导，流动逐渐变为湍流。默认值是具有光滑表面的圆管和管子的典型值。

### **Turbulent flow lower Reynolds number limit** — 层流区和湍流区之间过渡的终点 `4000`（默认） | unitless scalar

层流区和湍流区之间过渡的终点。低于此数值时，黏性力占主导，流动逐渐变为层流。默认值是具有光滑表面的圆管和管子的典型值。

### **Pressure loss model** — 由黏性摩擦引起的压力损失的数学模型 `Pressure loss coefficient`（默认） | `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

由黏性摩擦引起的压力损失的数学模型。此设置确定用于计算的表达式以及要指定为输入的模块参数。有关按参数化进行的计算，请参见 Heat Exchanger Interface (G) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1`（默认） | unitless scalar

流动通道中所有流动阻力的总损失系数，包括造成主要损失的壁摩擦，以及由弯曲、弯头和几何形状变化等造成次要损失的局部阻力。

损失系数是通常用于表示由黏性摩擦引起的压力损失的经验无量纲数。它可以根据实验数据计算，或者在某些情况下从产品数据表中获得。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从一个端口到另一个端口行进的距离 `1 m`（默认） | scalar with units of length

流体必须穿过各端口所经过的总距离。在多程壳管式交换器中，总距离是所有壳程的总和。在管束、波纹板和其他流动被分成并行分支的通道中，它是在单个分支中经过的距离。流动路径越长，由壁处黏性摩擦引起的主要压力损失越大。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设为 `Correlation for flow inside tubes` 和 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 以长度表示的局部阻力总次要压力损失 `0.1 m`（默认） | scalar with units of length

以长度表示的局部阻力总次要压力损失。此长度是如果所有局部阻力（如弯头、三通和管接头）的位置都由一段简单壁延伸代替时，它们将增加到流动路径上的长度。当量长度越大，由局部阻力引起的次要压力损失越大。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 引起壁摩擦的表面凸起平均高度 `15e-6 m`（默认） | scalar with units of length

引起壁摩擦的表面凸起平均高度。凸起越高，壁越粗糙，摩擦越大，因此压力损失越大。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由该关联式导出，压力损失计算也依赖于该关联式。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流动横截面的压力损失修正 `64`（默认） | unitless scalar

层流条件下流动横截面的压力损失修正。此参数通常称为形状因子。其与雷诺数的比值给出层流区压力损失计算的 Darcy 摩擦因子。默认值属于圆柱形管道和管子。

对于某些形状，形状因子由 Navier-Stokes 方程的解导出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长导管也是如此。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的雷诺数 unitless numerical array

Darcy 摩擦因子查找表中每个断点处的雷诺数。模块对断点进行内插和外推，以获得任意雷诺数下的 Darcy 摩擦因子。插值为 `linear`，外推为 `nearest`。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Darcy friction factor vector** 参数的大小，并将与其组合以完成表格化断点。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — 在雷诺数上的查找表中每个断点处的 Darcy 摩擦因子 unitless numerical array

在雷诺数上的查找表中每个断点处的 Darcy 摩擦因子。模块对断点进行内插和外推，以获得任意雷诺数下的 Darcy 摩擦因子。插值为 `linear`，外推为 `nearest`。

Darcy 摩擦因子不得为负，并且必须从左到右按雷诺数递增的顺序排列。其数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，并将与其组合以完成表格化断点。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — Euler 数查找表中每个断点处的雷诺数 unitless numerical array

Euler 数查找表中每个断点处的雷诺数。模块对断点进行内插和外推，以获得任意雷诺数下的 Euler 数。插值为 `linear`，外推为 `nearest`。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Euler number vector** 参数的大小，并将与其组合以完成表格化断点。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler number vector** — 在基于雷诺数的查找表中每个断点处的欧拉数 unitless numerical array

欧拉数位于其基于雷诺数的查找表中的每个断点处。该模块对断点进行内插和外推，以获得任意雷诺数下的欧拉数。插值为 `linear`，外推为 `nearest`。

欧拉数不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Euler number** 参数的大小，并与其组合以补全表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Heat transfer coefficient model** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient` (default) | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定要应用哪些表达式以及要为传热计算指定哪些参数。关于按参数化进行的计算，请参阅 E-NTU Heat Transfer 模块。

### **Heat transfer surface area** — 用于流体与壁面之间传热的有效表面积 `0.4 m^2` (default) | scalar with units of length squared

用于流体与壁面之间传热的有效表面积。有效表面积是主表面积和次表面积之和，即壁面暴露于流体处的面积以及使用的任何翅片的面积之和。翅片表面积通常按翅片效率因子进行缩放。

### **Gas-wall heat transfer coefficient** — 流体与壁面之间对流的传热系数 `100 W/(K*m^2)` (default) | scalar

流体与壁面之间对流的传热系数。由污垢引起的热阻在 **Fouling factor** 参数中单独捕获。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Constant heat transfer coefficient`。

### **Length of flow path for heat transfer** — 流体与壁面之间传热所经过的特征长度 `1 m` (default) | scalar with units of length

流体与壁面之间传热所经过的特征长度。此长度参与水力直径的计算；表列传热参数化中定义的传热系数和雷诺数由该水力直径导出。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number for laminar flow heat transfer** — 层流传热中努塞尔数的假定常数 `3.66` (default) | positive unitless scalar

层流中努塞尔数的假定常数。努塞尔数参与流体与壁面之间传热系数的计算，传热速率取决于该传热系数。默认值适用于圆柱形管道和管子。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Colburn factor** — 用于指定 Colburn 因子数据的雷诺数值 unitless numerical array

用于 Colburn 因子的查找表中每个断点处的雷诺数。该模块对断点进行内插和外推，以获得任意雷诺数下的 Colburn 因子。插值为 `linear`，外推为 `nearest`。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Colburn factor vector** 参数的大小，并与其组合以补全表格化断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn factor vector** — 在基于雷诺数的查找表中每个断点处的 Colburn 因子 unitless numerical array

Colburn 因子位于其基于雷诺数的查找表中的每个断点处。该模块对断点进行内插和外推，以获得任意雷诺数下的欧拉数。插值为 `linear`，外推为 `nearest`。

Colburn 因子不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Colburn factor** 参数的大小，并与其组合以补全表格化断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Reynolds number vector for Nusselt number** — 用于努塞尔数的查找表中每个断点处的雷诺数 unitless numerical array

用于努塞尔数的查找表中每个断点处的雷诺数。该表是双向的，雷诺数和普朗特数都用作独立坐标。该模块对断点进行内插和外推，以获得任意雷诺数下的努塞尔数。插值为 `linear`，外推为 `nearest`。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。向量的大小必须等于 **Nusselt number table** 参数中的行数。如果表有 *m* 行和 *n* 列，则雷诺数向量必须为 *m* 个元素长。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Prandtl number vector for Nusselt number** — 用于努塞尔数的查找表中每个断点处的普朗特数 unitless numerical array

用于努塞尔数的查找表中每个断点处的普朗特数。该表是双向的，雷诺数和普朗特数都用作独立坐标。该模块对断点进行内插和外推，以获得任意普朗特数下的努塞尔数。插值为 `linear`，外推为 `nearest`。

普朗特数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。向量的大小必须等于 **Nusselt number table** 参数中的列数。如果表有 *m* 行和 *n* 列，则普朗特数向量必须为 *n* 个元素长。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number table, Nu (Re,Pr)** — 在基于雷诺数和普朗特数的查找表中每个断点处的努塞尔数 unitless numerical array

努塞尔数位于其基于雷诺数和普朗特数的查找表中的每个断点处。该模块对断点进行内插和外推，以获得任意一对雷诺数和普朗特数下的努塞尔数。插值为 `linear`，外推为 `nearest`。通过确定努塞尔数，该表为计算提供输入，流体与壁面之间的传热系数由该计算导出。

努塞尔数必须大于零。它们必须按雷诺数递增的顺序从上到下排列，并按普朗特数递增的顺序从左到右排列。行数必须等于 **Reynolds number vector for Nusselt number** 参数的大小，列数必须等于 **Prandtl number vector for Nusselt number** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Fouling factor** — 由污垢沉积物引起的热阻度量 `1e-4 K*m^2/W` (default) | scalar with units of temperature over power

由污垢沉积物引起的热阻度量，这些沉积物随时间往往会在壁面的暴露表面上积聚。沉积物在流体与壁面之间形成新的固体层，热量必须穿过该层，从而为传热路径增加额外的热阻。污垢沉积物生长缓慢，因此假设其引起的热阻在仿真期间恒定。

### **Minimum gas-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)` (default) | scalar with units of power/area/temperature

流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则此下界将替换计算值。

### 受控流体

### **Heat transfer surface area** — 受控流体侧的总传热表面积 `0.4 m^2` (default) | scalar with units of length squared

受控流体侧的总传热表面积

### **Fouling factor** — 由污垢沉积物引起的热阻度量 `1e-4 K*m^2/W` (default) | scalar with units of length squared times temperature over power

由污垢沉积物引起的热阻度量，这些沉积物随时间往往会在壁面的暴露表面上积聚。沉积物在受控流体与壁面之间形成新的固体层，热量必须穿过该层，从而为传热路径增加额外的热阻。污垢沉积物生长缓慢，因此假设其引起的热阻在仿真期间恒定。

### **Minimum fluid-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)` (default) | scalar with units of power/area/temperature

受控流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则此下界将替换计算值。

### 影响和初始条件

### **Enable Gas dynamic compressibility** — 对气体通道中的压力动态建模的选项 `On` (default) | `Off`

对气体通道中的压力动态建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **Gas nominal temperature** — 标称工作条件下的温度 `293.15 K` (default) | scalar

标称工作条件下的气体温度。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程中的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas dynamic compressibility** 复选框。

### **Gas nominal pressure** — 标称工作条件下的压力 `0.101325 MPa` (default) | scalar

标称工作条件下的气体压力。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程中的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Gas dynamic compressibility** 复选框。

### **Gas initial temperature** — 仿真开始时气体通道中的温度 `293.15 K` (default) | scalar

仿真开始时气体通道中的温度。

### **Gas initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa` (default) | scalar

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Gas dynamic compressibility**。

## 所属库

Simscape / Fluids / Heat Exchangers / Gas

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：可选地建模动态可压缩性

Heat Exchanger (G) 模块现在可以通过使用 **Enable dynamic compressibility** 参数可选地建模动态可压缩性。此前，该模块始终建模压力动态，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

### R2025a：建模热交换器壁面的热质量

选择 **Wall thermal dynamics** 以建模热交换器壁面的热质量。

### R2024a：Heat Exchanger (G) 模块仅建模 E-NTU 建模选项

**Modeling option** 参数已移除，建模选项现在是两个单独的模块。Heat Exchanger (G) 模块使用先前当 **Modeling option** 为 `E-NTU Model` 时使用的传热模型。若要使用先前当 **Modeling option** 为 `Simple model` 时使用的模块模型，请参阅 Specific Dissipation Heat Exchanger (G) 模块。

## 描述

用于具有气体和受控流的系统的热交换器

Heat Exchanger (G) 模块对气体与外部 *受控* 流体之间通过物理信号进行的热交换进行建模；气体在端口 **A1** 和 **B1** 之间流动。

### 传热模型

该模块的传热模型源自 Effectiveness-NTU 方法。稳态传热以理想速率的一定比例进行；如果各流体都保持在其入口温度，并且清除其间的所有热阻，则理论上可支持该理想速率：

Q=ϵ QMax,

其中 *Q* 是实际传热速率，*Q*Max 是理想传热速率，*ε* 是在带有损失的真实热交换器中实际观测到的理想速率比例。该比例是热交换器效能，并且是传热单元数（即 NTU）的函数；NTU 衡量热量在流体之间传递的容易程度相对于流体吸收该热量的容易程度：

NTU=1RCMin,

其中该比值是流体之间的总热导，*C*Min 是各流体热容量率中的最小值，属于吸收热量能力最弱的流体。流体的热容量率取决于流体比热 (*c*p) 以及其通过交换器的质量流率 (m˙)：

C=cpm˙.

效能还取决于流体的相对布置、它们之间的程数以及每种流体的混合条件。这种依赖性反映在所使用的效能表达式中，不同的流动布置对应不同的表达式。有关效能表达式列表，请参阅 E-NTU Heat Transfer 模块。

该模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 流动布置

使用 **Flow arrangement** 模块参数设置流体在热交换器中的相遇方式。流体可以彼此平行、逆流或交叉流动。它们还可以在加压壳体中流动，一种流体流过封装在壳体中的管，另一种流体围绕这些相同的管流动。图中显示了一个示例。管程流体可以单程通过壳程流体（如右图所示），或者为了获得更高的交换器效能而进行多程流动（如左图所示）。

通过基于表格化效能数据的通用参数化，还可以实现其他流动布置，并且几乎不需要有关热交换器的详细信息。如果与热交换器相关，则假定流动布置、混合条件以及壳程或管程程数体现在表格化数据中。

### 混合条件

使用 **Cross flow type** 参数可混合每个流动、其中一个流动或不混合任何流动。此上下文中的混合是指流体在无内部屏障（通常为导流板、折流板、翅片或壁面）的通道中的横向运动。此类运动用于消除横向平面内的温度变化。混合流动仅在纵向平面内温度可变。未混合流动在横向和纵向平面内温度均可变。图中展示了混合流动（**i**）和未混合流动（**ii**）。

混合流与未混合流的区别仅在交叉流布置中考虑。在那里，一种流体的纵向温度变化会在第二种流体中产生横向温度变化，而混合可消除这种变化。在逆流和平行流布置中，一种流体的纵向温度变化会在第二种流体中产生纵向温度变化，而混合在此处影响很小，因此忽略。

### 效能曲线

具有多流程的管壳式换热器（图中 **iv.b**-**e**，对应 2、3 和 4 流程）最有效。在单流程换热器中，逆流（**ii**）的最有效，平行流（**i**）的最无效。

交叉流换热器的效能介于两者之间，混合条件是一个影响因素。当两种流动均未混合（**iii.a**）时最有效，当两种流动均混合（**iii.b**）时最无效。仅混合热容流率最小的流动（**iii.c**）比仅混合热容流率最大的流动（**iii.d**）更降低效能。

### 热阻

总热阻 *R* 是沿传热路径的局部热阻之和。局部热阻来自壁面表面的对流传热、穿过壁面的导热，以及如果壁面两侧有污垢，则还包括穿过污垢层的导热。按从气体侧（下标 1）到受控流体侧（下标 2）的顺序表示：

R=1U1A1+F1A1+RW+F2A2+1U2A2,

其中 *U* 是对流传热系数，*F* 是污垢系数，*A* 是传热表面积，各自对应下标所指示的流动。*RW* 是壁面的热阻。

壁面热阻和污垢系数是从模块参数获得的简单常量。传热系数是流体属性、流动几何和壁面摩擦的复杂函数，并源自雷诺数、努塞尔数和普朗特数之间的标准经验关联式。这些关联式取决于流动布置和混合条件，并且在模块模型所基于的 E-NTU Heat Transfer 模块中针对每种情况进行了详细说明。

### 壁面热质量

如果您选择 **Enable wall thermal mass**，模块会对换热器壁面热质量建模，这会引入壁面对温度或热通量变化的瞬态响应的延迟。如果您对热质量建模，壁面会在其边界内存储热量。这种热量存储会减慢稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率平衡为止。

如果您选择 **Enable wall thermal mass**，壁面能量守恒为

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁面温度。模块使用此值对瞬态响应建模。您无法测量此值。

对每种流体的传热为

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容流率。

每一侧流体与壁面之间的传热单元数为

NTU1=U1A1C1NTU2=U2A2C2

其中 *A* 是壁面表面积，*U* 是传热系数。

### 复合结构

该模块是由更简单的模块构建而成的复合组件。Heat Exchanger Interface (G) 模块对气体流建模。用于热容流率和传热系数的物理信号，以及用于温度的热端口，捕获受控流动。E-NTU Heat Transfer 模块对流动之间穿过壁面交换的热量建模。
