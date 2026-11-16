---
type: simulink-block
title: 'Heat Exchanger (G-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Gas'
documentation_page: 'heatexchangergg'
documentation_source_path: 'ref/heatexchangergg.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger (G-G)

## 端口

### 守恒

### **A1** — Gas 1 端口 gas

气体 1 进入和离开其热交换器一侧的开口。

### **B1** — Gas 1 端口 gas

气体 1 进入和离开其热交换器一侧的开口。

### **A2** — Gas 2 端口 gas

气体 2 进入和离开其热交换器一侧的开口。

### **B2** — Gas 2 端口 gas

气体 2 进入和离开其热交换器一侧的开口。

## 参数

### 通用

### **Flow arrangement** — 热交换器中流动排列的方式 `Parallel or counter flow`（默认） | `Shell and tube` | `Cross flow` | `Generic - effectiveness table`

热交换器中流动排列的方式。流体可以彼此平行流动、彼此逆向流动或彼此交叉流动。它们也可以在带压壳体中流动，其中一股流体流经壳体内部的管束，另一股流体在管束周围流动。其他流动排列可以通过基于表格化效能数据的通用参数化来实现，且只需热交换器的少量细节。

### **Wall thermal resistance** — 壁面通过热传导对热流的阻力 `0 K/W`（默认） | 正标量

分隔两种热交换器流体的界面壁的热阻。

### **Number of shell passes** — 流体在离开前穿过壳体的次数 `1`（默认） | 无量纲标量

流体在离开前穿过壳体的次数。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Cross flow type** — 每个流动通道中的混合条件 `Both fluids mixed`（默认） | `Both fluids unmixed` | `Gas 1 mixed & Gas 2 unmixed` | `Gas 1 unmixed & Gas 2 mixed`

每个流动通道中的混合条件。此处的混合是指流体沿其流动通道向出口前进时的横向运动。各流体彼此保持分离。未混合流动常见于带有板片、折流板或翅片的通道中。此设置会反映在热交换器的效能中，未混合流动效能最高，混合流动效能最低。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Number of heat transfer units vector, NTU** — 热交换器效能查找表中每个断点处的传热单元数 无量纲数值数组

热交换器效能数查找表中每个断点处的传热单元数。该表是双向的，传热单元数和热容率比均用作独立坐标。模块对断点进行内插和外推，以获得任意传热单元数下的效能。内插为 MATLAB `linear` 类型，外推为 `nearest`。

指定的数字必须大于零，并从左到右单调递增。向量的大小必须等于 **Effectiveness table** 参数的行数。如果该表有 *m* 行和 *n* 列，则传热单元数的向量长度必须为 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Thermal capacity ratio vector, CR** — 热交换器效能查找表中每个断点处的热容率比 无量纲数值数组

热交换器效能查找表中每个断点处的热容率比。该表是双向的，传热单元数和热容率比均用作独立坐标。模块对断点进行内插和外推，以获得任意热容率比下的效能。内插为 MATLAB `linear` 类型，外推为 `nearest`。

热容率比必须大于零，并从左到右单调递增。向量的大小必须等于 **Nusselt number table** 参数的列数。如果该表有 *m* 行和 *n* 列，则热容率比的向量长度必须为 *n* 个元素。热容率比是最小热容率与最大热容率的比值。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Effectiveness table, E(NTU,CR)** — 热交换器效能查找表中在传热单元数和热容率比上每个断点处的值 无量纲数值数组

热交换器效能在其查找表中于传热单元数和热容率比上的每个断点处。模块对断点进行内插和外推，以获得任意传热单元数和热容率比对下的效能。内插为 MATLAB `linear` 类型，外推为 `nearest`。

效能值不得为负。它们必须从上到下按传热单元数递增的顺序排列，并从左到右按热容率比递增的顺序排列。行数必须等于 **Number of heat transfer units vector** 参数的大小，列数必须等于 **Thermal capacity ratio vector** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Enable wall thermal mass** — 用于对壁面热质量建模的选项 `off`（默认） | `on`

是否对热交换器壁面热质量建模。对壁面热质量建模会在壁面对温度或热通量变化的瞬态响应中引入延迟。如果清除 **Enable wall thermal mass**，模块假定壁面足够薄，以至于在传热的时间尺度上瞬态响应是瞬时的。

### **Wall mass** — 热交换器壁面质量 `1 kg`（默认） | 正标量

热交换器壁面的质量。模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 热交换器壁面比热 `490 J/(K*kg)`（默认） | 正标量

热交换器壁面的比热。模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### Gas 1|2

### **Minimum free-flow area** — 流动通道在其最窄点处的横截面积 `0.01 m^2`（默认） | 具有长度平方单位的标量

入口和出口之间最小的总横截流动面积。如果通道是管道、管子、槽或凹槽的集合，则此参数的值是在最小流动面积点处各最小面积的总和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是在一个横截面中管间间隙总和为最小的间隙总和。

### **Gas volume** — Gas 1 或 Gas 2 流动通道中流体的总体积 `0.01 m^3`（默认） | 具有长度平方单位的标量

Gas 1 或 Gas 2 流动通道中包含的流体总体积。

### **Hydraulic diameter for pressure loss** — 流动通道在其最窄点处的有效直径 `0.1 m`（默认） | 具有长度单位的标量

流动在其最窄点处的有效内径。对于横截面非圆形的通道，该直径为与流动横截面积相等的假想圆的直径。其值为最小自由流动面积与其总周长四分之一的比值。

如果通道是管道、管子、槽或凹槽的集合，则总周长为该集合中各周长的总和。如果通道是单根管道或管子且横截面为圆形，则水力直径与真实直径相同。

### **Laminar flow upper Reynolds number limit** — 层流区与湍流区之间过渡的起点 `2000`（默认） | 无量纲标量

层流区与湍流区之间过渡的起点。高于此数值时，惯性力占主导，流动逐渐变为湍流。默认值对于表面光滑的圆形管道和管子具有代表性。

### **Turbulent flow lower Reynolds number limit** — 层流区与湍流区之间过渡的终点 `4000`（默认） | 无量纲标量

层流区与湍流区之间过渡的终点。低于此数值时，黏性力占主导，流动逐渐变为层流。默认值对于表面光滑的圆形管道和管子具有代表性。

### **Pressure loss model** — 由黏性摩擦引起的压力损失的数学模型 `Pressure loss coefficient`（默认） | `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

由黏性摩擦引起的压力损失的数学模型。此设置确定计算时使用哪些表达式以及将哪些模块参数指定为输入。有关按参数化进行的计算，请参阅 Heat Exchanger Interface (G) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1`（默认） | 无量纲标量

流动通道中所有流动阻力的总损失系数，包括导致沿程损失（主要损失）的壁面摩擦，以及由弯头、弯管和其他几何变化导致、造成局部损失（次要损失）的局部阻力。

损失系数是一个经验无量纲数，通常用于表示由黏性摩擦引起的压力损失。它可以通过实验数据计算，或者在某些情况下从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从端口到端口经过的距离 `1 m`（默认） | 具有长度单位的标量

流体跨越端口必须经过的总距离。在多程管壳式交换器中，总距离是所有壳程的总和。在管束、波纹板和其他流动被分成平行分支的通道中，它是在单个分支中经过的距离。流动路径越长，由壁面处黏性摩擦引起的沿程压力损失越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 和 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 以长度表示的局部压力损失总和 `0.1 m`（默认） | 具有长度单位的标量

以长度表示的局部压力损失总和。该长度是指所有局部阻力（如弯头、三通和管接头）在若由简单壁面延长代替时会给流动路径增加的长度。等效长度越大，由局部阻力引起的局部压力损失越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 引起壁面摩擦的表面凸起的平均高度 `15e-6 m`（默认） | 具有长度单位的标量

产生壁面摩擦的表面凸起的平均高度。凸起越高，壁面越粗糙，摩擦越大，因此压力损失越大。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由该关联式导出，压力损失计算也依赖于该关联式。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流动截面的压力损失修正 `64`（默认） | 无量纲标量

层流条件下流动截面的压力损失修正。此参数通常称为形状因子。其与 Reynolds 数的比值给出层流区中用于压力损失计算的 Darcy 摩擦因子。默认值属于圆柱形管道和管子。

对于某些形状，形状因子由 Navier-Stokes 方程的解导出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长导管也是如此。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的 Reynolds 数 无量纲数值数组

Darcy 摩擦因子查找表中每个断点处的 Reynolds 数。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Darcy 摩擦因子。内插为 MATLAB `linear` 类型，外推为 `nearest`。

Reynolds 数必须大于零，并从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Darcy friction factor vector** 参数的大小，并与该参数结合以补全表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — Darcy 摩擦因子在 Reynolds 数上的查找表中每个断点处的值 无量纲数值数组

Darcy 摩擦因子在其关于 Reynolds 数的查找表中每个断点处的值。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Darcy 摩擦因子。内插为 MATLAB `linear` 类型，外推为 `nearest`。

Darcy 摩擦因子不得为负，并且必须从左到右按 Reynolds 数递增的顺序排列。其数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，并与该参数结合以补全表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — Euler 数查找表中每个断点处的 Reynolds 数 无量纲数值数组

Euler 数查找表中每个断点处的 Reynolds 数。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Euler 数。内插为 MATLAB `linear` 类型，外推为 `nearest`。

Reynolds 数必须大于零，并从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Euler number vector** 参数的大小，并与该参数结合以补全表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler number vector** — Euler 数在 Reynolds 数上的查找表中每个断点处的值 无量纲数值数组

Euler 数在其关于 Reynolds 数的查找表中每个断点处的值。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Euler 数。内插为 MATLAB `linear` 类型，外推为 `nearest`。

Euler 数不得为负，并且必须从左到右按 Reynolds 数递增的顺序排列。其数量必须等于 **Reynolds number vector for Euler number** 参数的大小，并与该参数结合以补全表格化断点。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Tabulated data - Euler number
vs. Reynolds number`。

### **传热系数模型** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient`（默认） | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定要应用哪些表达式以及要为传热计算指定哪些参数。有关按参数化进行的计算，请参见 E-NTU Heat Transfer 模块。

### **传热表面积** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2`（默认） | scalar with units of length squared

流体与壁面之间传热所用的有效表面积。有效表面积是一次和二次表面积之和，即壁面暴露于流体处的表面积，以及翅片（如果使用）的表面积之和。翅片表面积通常按翅片效率因子缩放。

### **气体-壁面传热系数** — 流体与壁面之间对流传热的传热系数 `100 W/(K*m^2)`（默认） | scalar

流体与壁面之间对流传热的传热系数。由污垢引起的热阻在 **污垢系数** 参数中单独考虑。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Constant heat transfer
coefficient`。

### **传热流动路径长度** — 管道或通道的长度 `1 m`（默认） | scalar with units of length

管道或通道从入口到出口的长度。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor
vs. Reynolds number` 或 `Tabulated data
- Nusselt number vs. Reynolds number and Prandtl
number`。

### **层流流动传热的 Nusselt 数** — 层流中 Nusselt 数假定的常数 `3.66`（默认） | positive unitless scalar

层流中 Nusselt 数假定的常数。Nusselt 数参与流体与壁面之间传热系数的计算，传热速率取决于该系数。默认值适用于圆柱形管道和管。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Correlation for flow inside
tubes`。

### **用于 Colburn 因子的 Reynolds 数向量** — 用于指定 Colburn 因子数据的 Reynolds 数取值 unitless numerical array

Colburn 因子查找表中每个断点处的 Reynolds 数。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Colburn 因子。插值为 MATLAB `linear` 类型，外推为 `nearest`。

Reynolds 数必须大于零，并从左到右单调增加。它们可以跨越层流、过渡和湍流区。它们的数量必须等于 **Colburn 因子向量** 参数的大小，以与其组合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor
vs. Reynolds number`。

### **Colburn 因子向量** — Reynolds 数查找表中每个断点处的 Colburn 因子 unitless numerical array

Reynolds 数查找表中每个断点处的 Colburn 因子。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Euler 数。插值为 MATLAB `linear` 类型，外推为 `nearest`。

Colburn 因子不得为负，并且必须按 Reynolds 数递增的顺序从左到右排列。它们的数量必须等于 **用于 Colburn 因子的 Reynolds 数向量** 参数的大小，以与其组合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor
vs. Reynolds number`。

### **用于 Nusselt 数的 Reynolds 数向量** — Nusselt 数查找表中每个断点处的 Reynolds 数 unitless numerical array

Nusselt 数查找表中每个断点处的 Reynolds 数。该表是双向的，Reynolds 数和 Prandtl 数都用作独立坐标。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Nusselt 数。插值为 MATLAB `linear` 类型，外推为 `nearest`。

Reynolds 数必须大于零，并从左到右单调增加。它们可以跨越层流、过渡和湍流区。向量的大小必须等于 **Nusselt 数表** 参数中的行数。如果该表有 *m* 行和 *n* 列，则 Reynolds 数向量必须为 *m* 个元素长。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number
vs. Reynolds number and Prandtl number`。

### **用于 Nusselt 数的 Prandtl 数向量** — Nusselt 数查找表中每个断点处的 Prandtl 数 unitless numerical array

Nusselt 数查找表中每个断点处的 Prandtl 数。该表是双向的，Reynolds 数和 Prandtl 数都用作独立坐标。模块对断点进行内插和外推，以获得任意 Prandtl 数下的 Nusselt 数。插值为 MATLAB `linear` 类型，外推为 `nearest`。

Prandtl 数必须大于零，并从左到右单调增加。它们可以跨越层流、过渡和湍流区。向量的大小必须等于 **Nusselt 数表** 参数中的列数。如果该表有 *m* 行和 *n* 列，则 Prandtl 数向量必须为 *n* 个元素长。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number
vs. Reynolds number and Prandtl number`。

### **Nusselt 数表, Nu (Re,Pr)** — 在 Reynolds 数和 Prandtl 数上的查找表中每个断点处的 Nusselt 数 unitless numerical array

在 Reynolds 数和 Prandtl 数上的查找表中每个断点处的 Nusselt 数。模块对断点进行内插和外推，以获得任意 Reynolds 数和 Prandtl 数对下的 Nusselt 数。插值为 MATLAB `linear` 类型，外推为 `nearest`。通过确定 Nusselt 数，该表为计算提供输入，流体与壁面之间的传热系数由此推导。

Nusselt 数必须大于零。它们必须按 Reynolds 数递增的顺序从上到下排列，并按 Prandtl 数递增的顺序从左到右排列。行数必须等于 **用于 Nusselt 数的 Reynolds 数向量** 参数的大小，列数必须等于 **用于 Nusselt 数的 Prandtl 数向量** 参数的大小。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number
vs. Reynolds number and Prandtl number`。

### **污垢系数** — 由污垢沉积物引起的热阻度量 `1e-4 K*m^2/W`（默认） | scalar with units of temperature over power

由污垢沉积物引起的热阻度量，这些沉积物随时间倾向于在壁面的暴露表面上积聚。这些沉积物在流体与壁面之间形成一层新的固体层，热量必须穿过该层，从而为传热路径增加了额外的热阻。污垢沉积物增长缓慢，因此由它们引起的热阻在仿真期间假定为常数。

### **最小气体-壁面传热系数** — 传热系数的下界 `1 W/(m^2 * K)`（默认） | scalar with units of power/area/temperature

流体与壁面之间传热系数的下界。如果计算返回更低的传热系数，则此下界替换计算值。

### 影响与初始条件

### **启用 Gas 1 动态可压缩性** — 对气体通道中压力动态进行建模的选项 `On`（默认） | `Off`

对气体通道中压力动态进行建模的选项。如果清除此复选框，模块会从组件能量和质量守恒方程中移除压力导数项。

### **Gas 1 标称温度** — 标称工况下的温度 `293.15 K`（默认） | scalar

标称工况下的气体温度。当动态可压缩性被禁用时，模块使用此值计算标称密度，以用于质量与能量守恒方程。

#### 依赖关系

要启用此参数，请清除 **启用 Gas 1 动态可压缩性** 复选框。

### **Gas 1 标称压力** — 标称工况下的压力 `0.101325 MPa`（默认） | scalar

标称工况下的气体压力。当动态可压缩性被禁用时，模块使用此值计算标称密度，以用于质量与能量守恒方程。

#### 依赖关系

要启用此参数，请清除 **启用 Gas 1 动态可压缩性** 复选框。

### **Gas 1 初始温度** — 仿真开始时气体通道中的温度 `293.15 K`（默认） | scalar with units of temperature

仿真开始时气体通道中的温度

### **Gas 1 初始压力** — 仿真开始时气体通道中的压力 `0.101325 MPa`（默认） | scalar with units of pressure

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **启用 Gas 1 动态可压缩性** 。

### **启用 Gas 2 动态可压缩性** — 对气体通道中压力动态进行建模的选项 `On`（默认） | `Off`

对气体通道中压力动态进行建模的选项。如果清除此复选框，模块会从组件能量和质量守恒方程中移除压力导数项。

### **Gas 2 标称温度** — 标称工况下的温度 `293.15 K`（默认） | scalar

标称工况下的气体温度。当动态可压缩性被禁用时，模块使用此值计算标称密度，以用于质量与能量守恒方程。

#### 依赖关系

要启用此参数，请清除 **启用 Gas 2 动态可压缩性** 复选框。

### **Gas 2 标称压力** — 标称工况下的压力 `0.101325 MPa`（默认） | scalar

标称工况下的气体压力。当动态可压缩性被禁用时，模块使用此值计算标称密度，以用于质量与能量守恒方程。

#### 依赖关系

要启用此参数，请清除 **启用 Gas 2 动态可压缩性** 复选框。

### **Gas 2 初始温度** — 仿真开始时 gas 2 通道中的温度 `293.15 K`（默认） | scalar with units of temperature

仿真开始时 gas 2 通道中的温度。

### **Gas 2 初始压力** — 仿真开始时 gas 2 通道中的压力 `0.101325 MPa`（默认） | scalar with units of pressure

仿真开始时 gas 2 通道中的压力。

#### 依赖关系

要启用此参数，请选择 **启用 Gas 2 动态可压缩性** 。

## 所属库

Simscape / Fluids / Heat Exchangers / Gas

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a: 可选地对动态可压缩性建模

Heat Exchanger (G-G) 模块现在可以通过 **启用动态可压缩性** 参数可选地对动态可压缩性建模。以前，此模块总是对压力动态建模，这可能导致模型需要更长时间达到稳态。清除 **启用动态可压缩性** 参数以防止动态可压缩性建模。

### R2024a: Heat Exchanger (G-G) 模块仅对 E-NTU 建模选项建模

**建模选项** 参数已移除，建模选项现在分为两个单独的模块。Heat Exchanger (G-G) 模块使用以前当 **建模选项** 为 `E-NTU Model` 时使用的传热模型。要使用以前当 **建模选项** 为 `Simple model` 时使用的模块模型，请参见 Specific Dissipation Heat Exchanger (G-G) 模块。

## 描述

用于具有两股气体流的系统的换热器

Heat Exchanger (G-G) 模块对气-气换热器建模。壁面可以在其边界内储存热量，为传热增加轻微的瞬态延迟，该延迟与其热质量成比例。流体为单相，且每种流体都是气体。两种流体都不能相变，因此，由于从不会释放潜热，交换严格为显热交换。

### 传热模型

模块传热模型源自 Effectiveness-NTU 方法。稳态下的传热随后以理想速率的一部分进行；如果各股流体保持在其入口温度，并清除其间的所有热阻，理论上可支持该理想速率：

Q=ϵ QMax,

其中 *Q* 是实际传热速率，*Q*Max 是理想传热速率，*ε* 是在带有损失的實際换热器中实际观测到的理想速率的分数。该分数是换热器效能，并且是传热单元数（即 NTU）的函数；NTU 衡量热量在流体之间移动的容易程度相对于流体吸收该热量的容易程度：

NTU=1RCMin,

其中该分数是流体之间的总热导，*C*Min 是各流体热容量率中的最小值，属于最不能吸收热量的流体。一股流体的热容量率取决于流体的比热（*c*p）及其通过换热器的质量流量（m˙）：

C=cpm˙.

效能还取决于流体的相对布置、流体之间的程数以及各自的混合条件。这种依赖关系反映在所使用的效能表达式中，不同的流动布置对应不同的表达式。有关效能表达式的列表，请参见 E-NTU Heat Transfer 模块。

模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 流动布置

使用 **流动布置** 模块参数设置流体在换热器中如何相遇。流体可以彼此平行流动、彼此逆流流动或彼此交叉流动。它们也可以在加压壳体中流动，一股流经封闭在壳体内的管，另一股绕这些相同的管流动。图中显示了一个示例。管程流动可以单程通过壳程流动（右图），或者为了提高换热器效能，多程通过（左图）。

通过基于表格化效能数据的通用参数化，可以实现其他流动布置，并且几乎不需要换热器的详细信息。流动布置、混合条件以及壳程或管程程数（如果与换热器相关）假定体现在表格数据中。

### 混合条件

使用 **Cross flow type** 参数来混合两股流动均混合、仅一股流动混合或两股流动均不混合。在此上下文中，混合是指流体在无内部屏障（通常为导板、折流板、翅片或壁面）的通道中的横向运动。这种运动用于均匀化横向平面中的温度变化。混合流的温度仅在纵向平面内可变。未混合流的温度在横向和纵向平面内均可变。图示显示了混合流（**i**）和未混合流（**ii**）。

混合流与未混合流之间的区别仅在交叉流布置中考虑。在那里，一种流体的纵向温度变化会在第二种流体中产生横向温度变化，而混合可以将其均匀化。在逆流和顺流布置中，一种流体的纵向温度变化会在第二种流体中产生纵向温度变化，而混合在此处影响很小，因此忽略。

### 效能曲线

多程的壳管式换热器（图中 **iv.b**-**e** 对应 2、3 和 4 程）最有效。在单程换热器中，逆流者（**ii**）最有效，而顺流者（**i**）最无效。

交叉流换热器的效能介于其间，混合条件起一定作用。当两股流动均未混合（**iii.a**）时最有效，当两股流动均混合（**iii.b**）时最无效。仅混合热容率最小的流动（**iii.c**）比仅混合热容率最大的流动（**iii.d**）更能降低效能。

### 热阻

总热阻 *R* 是沿传热路径的局部热阻之和。局部热阻来自壁面表面的对流、通过壁面的导热，以及如果壁面两侧结垢，则通过污垢层的导热。按从 gas side 1 到 gas side 2 的顺序表示为：

R=1U1A1+F1A1+RW+F2A2+1U2A2,

其中 *U* 是对流传热系数，*F* 是污垢系数，*A* 是传热表面积，各自对应于下标所示的流动。*R*W 是壁面的热阻。

壁面热阻和污垢系数是从模块参数获得的简单常数。传热系数是流体属性、流动几何和壁面摩擦的复杂函数，并且来自 Reynolds、Nusselt 和 Prandtl 数之间的标准经验关联式。这些关联式取决于流动布置和混合条件，并针对每种情况在 E-NTU Heat Transfer 模块中详细说明，该模块是此模块模型的基础。

### 壁面热质量

如果选择 **Enable wall thermal mass**，模块会对换热器壁热质量建模，这会在壁面对温度或热通量变化的瞬态响应中引入延迟。如果对热质量建模，壁面会在其边界内储存热量。这种热量储存会减慢稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率平衡为止。

如果选择 **Enable wall thermal mass**，壁面能量守恒为

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁温。模块使用此值对瞬态响应建模。你无法测量此值。

传递到每种流体的热量为

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容率。

每一侧流体与壁面之间的传热单元数为

NTU1=U1A1C1NTU2=U2A2C2

其中 *A* 是壁面表面积，*U* 是传热系数。

### 复合结构

该模块是一个由更简单的模块构建而成的复合组件。一个 Heat Exchanger Interface (G) 模块对换热器 side 1 上的气体流动建模。另一个对 side 2 上的气体流动建模。一个 E-NTU Heat Transfer 模块对两股流动之间通过壁面交换的热量建模。
