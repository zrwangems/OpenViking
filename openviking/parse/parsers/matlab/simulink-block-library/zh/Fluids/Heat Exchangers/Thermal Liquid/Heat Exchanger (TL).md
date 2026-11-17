---
type: simulink-block
title: 'Heat Exchanger (TL)'
family: 'heat-exchangers'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'heatexchangertl'
documentation_source_path: 'ref/heatexchangertl.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger (TL)

## 端口

### 守恒

### **A1** — 热液体端口 thermal liquid

热液体进入和离开换热器其侧的开口。

### **B1** — 热液体端口 thermal liquid

热液体进入和离开换热器其侧的开口。

### **H2** — 受控流体 2 的入口温度 thermal

受控流体 2 的入口温度。

### 输入

### **C2** — 热容率 physical signal

受控流的热容率的瞬时值。

### **HC2** — 传热系数 physical signal

受控流与壁面之间的传热系数的瞬时值。

## 参数

### 通用

### **Flow arrangement** — 流体在换热器中对齐的方式 `Parallel or counter flow` (默认) | `Shell and tube` | `Cross flow` | `Generic - effectiveness table`

流体在换热器中对齐的方式。流体可以彼此平行、彼此逆向或彼此交叉流动。它们还可以在加压壳体中流动，一种流体穿过封闭在壳体内的管，另一种流体围绕这些管流动。通过基于表格化效能数据的通用参数化，其他流动布置也是可能的，并且几乎不需要换热器的详细信息。

### **Number of shell passes** — 流体在离开之前穿过壳体的次数 `1` (默认) | unitless scalar

流体在离开之前穿过壳体的次数。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Cross flow type** — 每个流动通道中的混合条件 `Both fluids mixed` (默认) | `Both fluids unmixed` | `Thermal liquid mixed & Controlled Fluid unmixed` | `Thermal liquid unmixed & Controlled Fluid mixed`

每个流动通道中的混合条件。这里的混合是指流体沿其流动通道向出口前进时的横向运动。流动彼此保持分离。未混合流动常见于带有板、折流板或翅片的通道中。此设置会影响换热器的效能，未混合流动效能最高，混合流动效能最低。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Number of heat transfer units vector, NTU** — 换热器效能查找表中每个断点处的传递单元数 unitless numerical array

换热器效能数的查找表中每个断点处的传递单元数。该表是二维的，传递单元数和热容比都用作独立坐标。模块对断点进行内插和外推，以获得任意传递单元数下的效能。插值为 `linear`，外推为 `nearest`。

指定的数必须大于零，并从左到右单调递增。向量的大小必须等于 **Effectiveness table** 参数中的行数。如果表有 *m* 行和 *n* 列，则传递单元数的向量长度必须为 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Thermal capacity ratio vector, CR** — 换热器效能查找表中每个断点处的热容比 unitless numerical array

换热器效能查找表中每个断点处的热容比。该表是二维的，传递单元数和热容率比都用作独立坐标。模块对断点进行内插和外推，以获得任意热容比下的效能。插值为 `linear`，外推为 `nearest`。

热容比必须大于零，并从左到右单调递增。向量的大小必须等于 **Nusselt number table** 参数中的列数。如果表有 *m* 行和 *n* 列，则热容比的向量长度必须为 *n* 个元素。热容比是最小热容率与最大热容率的比值。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Effectiveness table, E(NTU,CR)** — 换热器效能在其查找表中每个断点处相对于传递单元数和热容比的值 unitless numerical array

换热器效能在其查找表中每个断点处相对于传递单元数和热容比的值。模块对断点进行内插和外推，以获得任意传递单元数和热容比对下的效能。插值为 `linear`，外推为 `nearest`。

效能值不得为负。它们必须从上到下按传递单元数递增的顺序排列，并从左到右按热容比递增的顺序排列。行数必须等于 **Number of heat transfer units vector** 参数的大小，列数必须等于 **Thermal capacity ratio vector** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Wall thermal resistance** — 壁面对热传导热流的阻力 `0 K/W` (默认) | scalar with units of temperature over power

壁面对热传导热流的阻力，并且是热导的倒数，或热导率与表面积与长度之比的乘积。壁面阻力与对流阻力和污垢阻力相加，以确定流体之间的总传热系数。

### **Enable wall thermal mass** — 对壁面热质量建模的选项 `off` (默认) | `on`

是否对换热器壁面热质量建模。对壁面热质量建模会在壁面对温度或热流变化作出响应时在瞬态响应中引入延迟。如果清除 **Enable wall thermal mass**，模块假定壁面足够薄，以至于在传热的时间尺度上瞬态响应是瞬时的。

### **Wall mass** — 换热器壁面的质量 `1 kg` (默认) | positive scalar

换热器壁面的质量。模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Wall specific heat** — 换热器壁面的比热 `490 J/(K*kg)` (默认) | positive scalar

换热器壁面的比热。模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### 热液体

### **Minimum free-flow area** — 流动通道在其最窄点处的横截面积 `0.01 m^2` (默认) | scalar with units of length squared

入口和出口之间最小的总横截流面积。如果通道是管道、管子、槽或凹槽的集合，则此参数的值是最小流动面积点处最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是一个横截面中管间间隙之和最小的那些间隙之和。

### **Thermal liquid volume** — 热液体流动通道中流体的总体积 `0.01 m^3` (默认) | scalar with units of length squared

热液体流动通道中包含的流体总体积。

### **Hydraulic diameter for pressure loss** — 流动通道在其最窄点处的有效直径 `0.1 m` (默认) | scalar with units of length

流动在其最窄点处的有效内径。对于非圆形横截面的通道，该直径为与流动横截面积相等的假想圆的直径。其值是最小自由流动面积与其总周长四分之一的比值。

如果通道是管道、管子、槽或凹槽的集合，则总周长是该集合中周长的总和。如果通道是单根管道或管子，并且其横截面为圆形，则水力直径与真实直径相同。

### **Laminar flow upper Reynolds number limit** — 层流区和湍流区之间过渡的起点 `2000` (默认) | unitless scalar

层流区和湍流区之间过渡的起点。高于此数值时，惯性力占据主导，流动逐渐变为湍流。默认值是具有光滑表面的圆管和管子的特征值。

### **Turbulent flow lower Reynolds number limit** — 层流区和湍流区之间过渡的终点 `4000` (默认) | unitless scalar

层流区和湍流区之间过渡的终点。低于此数值时，黏性力占据主导，流动逐渐变为层流。默认值是具有光滑表面的圆管和管子的特征值。

### **Pressure loss model** — 由黏性摩擦引起的压力损失的数学模型 `Pressure loss coefficient` (默认) | `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

由黏性摩擦引起的压力损失的数学模型。此设置确定用于计算的表达式以及要作为输入指定的模块参数。有关按参数化进行的计算，请参见 Heat Exchanger Interface (TL) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1` (默认) | unitless scalar

端口之间所有流动阻力的总损失系数，包括造成主要损失的壁面摩擦，以及由弯头、弯管和其他几何变化引起、造成次要损失的局部阻力。

损失系数是经验无量纲数，通常用于表示由黏性摩擦引起的压力损失。它可以从实验数据计算得出，或者在某些情况下从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从入口到出口的流动路径长度 `1 m` (默认) | scalar with units of length

流体必须跨越端口所经过的总距离。在多程壳管式换热器中，总距离是所有壳程的总和。在管束、波纹板和其他流动被分成平行分支的通道中，它是在单个分支中经过的距离。流动路径越长，壁面处黏性摩擦造成的主要压力损失越陡峭。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 以长度表示的局部阻力总次要压力损失 `0.1 m` (默认) | scalar with units of length

以长度表示的局部阻力总次要压力损失。此长度是所有局部阻力（如弯头、三通和管接头）如果由简单壁面延伸代替它们时会增加到流动路径中的长度。等效长度越大，局部阻力造成的次要压力损失越陡峭。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 引起壁面摩擦的表面凸起平均高度 `15e-6 m` (默认) | scalar with units of length

引起壁面摩擦的表面凸起平均高度。凸起越高，壁面越粗糙，摩擦越大，因此压力损失越陡峭。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由该关联式导出，并且压力损失计算依赖于该关联式。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流动横截面的压力损失修正 `64` (默认) | unitless scalar

层流条件下流动横截面的压力损失修正。此参数通常称为形状因子。其与 Reynolds 数的比值给出层流区域中压力损失计算的 Darcy 摩擦因子。默认值属于圆柱形管道和管子。

对于某些形状，形状因子从 Navier-Stokes 方程的解推导得出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长导管也是如此。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的 Reynolds 数 unitless numerical array

Darcy 摩擦因子查找表中每个断点处的 Reynolds 数。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Darcy 摩擦因子。插值为 `linear`，外推为 `nearest`。

Reynolds 数必须大于零，并从左到右单调递增。它们可以跨越层流、过渡和湍流区域。它们的数量必须等于 **Darcy friction factor vector** 参数的大小；它们将与该参数结合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — Darcy 摩擦因子在其相对于 Reynolds 数的查找表中每个断点处的值 unitless numerical array

Darcy 摩擦因子在其相对于 Reynolds 数的查找表中每个断点处的值。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Darcy 摩擦因子。插值为 `linear`，外推为 `nearest`。

Darcy 摩擦因子不得为负，并且必须从左到右按 Reynolds 数递增的顺序排列。它们的数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小；它们将与该参数结合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — Euler 数查找表中每个断点处的 Reynolds 数 unitless numerical array

Euler 数查找表中每个断点处的 Reynolds 数。模块对断点进行内插和外推，以获得任意 Reynolds 数下的 Euler 数。插值为 `linear`，外推为 `nearest`。

Reynolds 数必须大于零，并从左到右单调递增。它们可以跨越层流、过渡和湍流区域。它们的数量必须等于 **Euler number vector** 参数的大小；它们将与该参数结合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **欧拉数向量** — 基于 Reynolds number 的查找表中每个断点处的 Euler number unitless numerical array

基于 Reynolds number 的查找表中每个断点处的 Euler number。该模块对断点进行内插和外推，以获得任意 Reynolds number 下的 Euler number。插值为 `linear`，外推为 `nearest`。

Euler number 不得为负，并且必须按 Reynolds number 递增的顺序从左到右排列。其数量必须等于 **Euler number 对应的 Reynolds number 向量** 参数的大小，它们将与该参数结合以构成表格化的断点。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **传热系数模型** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient` (默认) | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定了要应用哪些表达式以及要为传热计算指定哪些参数。有关按参数化进行的计算，请参见 E-NTU Heat Transfer 模块。

### **传热表面积** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2` (默认) | scalar with units of length squared

流体与壁面之间传热所用的有效表面积。有效表面积是主表面积与次表面积之和，或者是壁面暴露于流体处的表面积与翅片（如果使用）的表面积之和。翅片表面积通常按翅片效率因子进行缩放。

### **液体-壁面传热系数** — 流体与壁面之间对流传热的传热系数 `100 W/(K*m^2)` (默认) | scalar

流体与壁面之间对流传热的传热系数。污垢引起的热阻在 **污垢系数** 参数中单独考虑。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Constant heat transfer coefficient`。

### **传热流路长度** — 流体与壁面之间传热所经过的特征长度 `1 m` (默认) | scalar with units of length

流体与壁面之间传热所经过的特征长度。该长度用于计算水力直径，而传热系数以及表格化传热参数化中定义的 Reynolds number 均由水力直径推导得出。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **层流传热的 Nusselt number** — 层流中假定的 Nusselt number 常数 `3.66` (默认) | positive unitless scalar

层流中假定的 Nusselt number 常数。Nusselt number 用于计算流体与壁面之间的传热系数，而传热速率取决于该传热系数。默认值适用于圆柱形管道和管。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Correlation for flow inside tubes`。

### **Colburn 因子对应的 Reynolds number 向量** — 用于指定 Colburn 因子数据的 Reynolds number 值 unitless numerical array

Colburn 因子查找表中每个断点处的 Reynolds number。该模块对断点进行内插和外推，以获得任意 Reynolds number 下的 Colburn 因子。插值为 `linear`，外推为 `nearest`。

Reynolds number 必须大于零，并且必须从左到右单调递增。它们可以跨越层流、过渡流和湍流区域。其数量必须等于 **Colburn 因子向量** 参数的大小，它们将与该参数结合以构成表格化的断点。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn 因子向量** — 基于 Reynolds number 的查找表中每个断点处的 Colburn 因子 unitless numerical array

Colburn 因子查找表中每个断点处的 Colburn 因子。该模块对断点进行内插和外推，以获得任意 Reynolds number 下的 Euler number。插值为 `linear`，外推为 `nearest`。

Colburn 因子不得为负，并且必须按 Reynolds number 递增的顺序从左到右排列。其数量必须等于 **Colburn 因子对应的 Reynolds number 向量** 参数的大小，它们将与该参数结合以构成表格化的断点。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Nusselt number 对应的 Reynolds number 向量** — Nusselt number 查找表中每个断点处的 Reynolds number unitless numerical array

Nusselt number 查找表中每个断点处的 Reynolds number。该表是二维的，以 Reynolds number 和 Prandtl number 作为独立坐标。该模块对断点进行内插和外推，以获得任意 Reynolds number 下的 Nusselt number。插值为 `linear`，外推为 `nearest`。

Reynolds number 必须大于零，并且必须从左到右单调递增。它们可以跨越层流、过渡流和湍流区域。向量的大小必须等于 **Nusselt number 表** 参数中的行数。如果表有 *m* 行和 *n* 列，则 Reynolds number 向量的长度必须为 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number 对应的 Prandtl number 向量** — Nusselt number 查找表中每个断点处的 Prandtl number unitless numerical array

Nusselt number 查找表中每个断点处的 Prandtl number。该表是二维的，以 Reynolds number 和 Prandtl number 作为独立坐标。该模块对断点进行内插和外推，以获得任意 Prandtl number 下的 Nusselt number。插值为 `linear`，外推为 `nearest`。

Prandtl number 必须大于零，并且必须从左到右单调递增。它们可以跨越层流、过渡流和湍流区域。向量的大小必须等于 **Nusselt number 表** 参数中的列数。如果表有 *m* 行和 *n* 列，则 Prandtl number 向量的长度必须为 *n* 个元素。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number 表, Nu (Re,Pr)** — 基于 Reynolds number 和 Prandtl number 的查找表中每个断点处的 Nusselt number unitless numerical array

Nusselt number 在其基于 Reynolds number 和 Prandtl number 的查找表中每个断点处的值。该模块对断点进行内插和外推，以获得任意 Reynolds number 和 Prandtl number 组合下的 Nusselt number。插值为 `linear`，外推为 `nearest`。通过确定 Nusselt number，该表为计算提供输入，流体与壁面之间的传热系数由该计算推导得出。

Nusselt number 必须大于零。它们必须按 Reynolds number 递增的顺序从上到下排列，并按 Prandtl number 递增的顺序从左到右排列。行数必须等于 **Nusselt number 对应的 Reynolds number 向量** 参数的大小，列数必须等于 **Nusselt number 对应的 Prandtl number 向量** 参数的大小。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **污垢系数** — 由污垢沉积引起的热阻度量 `1e-4 K*m^2/W` (默认) | scalar with units of temperature over power

由污垢沉积引起的热阻度量，这些沉积物随时间倾向于在壁面的暴露表面上积聚。这些沉积物在流体与壁面之间施加了一个新的固体层，热量必须穿过该层，从而为传热路径增加了额外的热阻。污垢沉积物生长缓慢，因此其在仿真期间引起的热阻被相应地假定为常数。

### **最小液体-壁面传热系数** — 传热系数的下界 `1 W/(m^2 * K)` (默认) | scalar with units of power/area/temperature

流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则用此下界替换计算值。

### 受控流体

### **传热表面积** — 受控流体侧的合计传热表面积 `0.4 m^2` (默认) | scalar with units of length squared

受控流体侧的合计传热表面积

### **污垢系数** — 由污垢沉积引起的热阻度量 `1e-4 K*m^2/W` (默认) | scalar with units of length squared times temperature over power

由污垢沉积引起的热阻度量，这些沉积物随时间倾向于在壁面的暴露表面上积聚。这些沉积物在受控流体与壁面之间施加了一个新的固体层，热量必须穿过该层，从而为传热路径增加了额外的热阻。污垢沉积物生长缓慢，因此其在仿真期间引起的热阻被相应地假定为常数。

### **最小流体-壁面传热系数** — 传热系数的下界 `1 W/(m^2 * K)` (默认) | scalar with units of power/area/temperature

受控流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则用此下界替换计算值。

### 效应和初始条件

### **启用 Thermal Liquid 动态可压缩性** — 热交换器中液体可压缩性的设置 `On` (默认) | `Off` | scalar

用于对热交换器内部压力动态进行建模的选项。将此参数设置为 `Off` 会从组件能量和质量守恒方程中移除压力导数项。热交换器内部的压力随后被简化为两个端口压力的加权平均值。

### **Thermal Liquid 标称温度** — 标称工况下的温度 `293.15 K` (默认) | scalar

标称工况下的 Thermal liquid 温度。当动态可压缩性禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用 Thermal Liquid 动态可压缩性** 复选框。

### **Thermal Liquid 标称压力** — 标称工况下的压力 `0.101325 MPa` (默认) | scalar

标称工况下的 Thermal liquid 压力。当动态可压缩性禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用 Thermal Liquid 动态可压缩性** 复选框。

### **Thermal Liquid 初始温度** — 仿真开始时 thermal liquid 通道内的温度 `293.15 K` (默认) | scalar with units of temperature

仿真开始时 thermal liquid 通道内的温度

### **Thermal Liquid 初始压力** — 仿真开始时 thermal liquid 通道内的压力 `0.101325 MPa` (默认) | scalar with units of pressure

仿真开始时 thermal liquid 通道内的压力。

#### 依赖关系

要启用此参数，请选择 **启用 Thermal Liquid 动态可压缩性**。

## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2025a: 对热交换器壁面的热质量建模

选择 **壁面热动态** 以对热交换器壁面的热质量建模。

### R2024a: Heat Exchanger (TL) 模块仅对 E-NTU 建模选项进行建模

**建模选项** 参数已被移除，建模选项现在是两个独立的模块。Heat Exchanger (TL) 模块使用以前在 **建模选项** 为 `E-NTU Model` 时使用的传热模型。若要使用以前在 **建模选项** 为 `Simple model` 时使用的模块模型，请参见 Specific Dissipation Heat Exchanger (TL) 模块。

## 描述

用于具有 thermal liquid 和受控流的系统的热交换器

Heat Exchanger (TL) 模块通过薄壁上的传导对流体进行冷却和加热建模。单相 thermal liquid 的属性在 **Thermal Liquid** 选项卡上定义。第二种流体是受控流体，仅由 **受控流体** 选项卡上的用户定义参数指定。它不从域流体网络接收任何属性。流体之间的热交换基于 thermal liquid 的显热。

### 传热模型

该模块的传热模型源自 Effectiveness-NTU 方法。稳态传热基于一个将系统理想损失与实际损失联系起来的系数来确定：

Q=ϵ QMax,

其中

- *Q* 是实际传热速率。
- *Q*Max 是理想传热速率。
- *ε* 是热交换器效能，基于热容量率之比 CMinCMax 以及交换器传热单元数：

  NTU=1RCMin,

  其中 *R* 是总热阻，将在下文的热阻部分讨论。
  *C*Min 是两种流体中较小的热容量率，*C*Max 是两种流体中较大的热容量率。热容量率按 C=cpm˙ 计算。

此外，交换器效能取决于流体之间的程数以及流体混合条件。有关效能表达式列表，请参见 E-NTU Heat Transfer 模块。将 E-NTU Heat Transfer 模块连接到 Heat Exchanger (TL) 模块，以使用 E-NTU 方法指定传热属性。

该模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 流动布置

使用 **流动布置** 参数以管道方向或效能表的形式定义流动配置。使用管壳式配置时，可以选择交换器中的程数。多程交换器类似于下图。

单程交换器类似于下图。

通过表格化效能数据的通用参数化，可以实现其他流动布置。该表不需要特定的热交换器配置细节（例如流动布置、混合和程数）来对流体之间的传热建模。

### 混合条件

使用 **Cross flow type** 参数对不受折流板或壁面限制的流动建模，其使流体温度沿第二流体流动方向均匀，并沿垂直于第二流体流动的方向发生变化。非混合流动的温度沿第二流体流动方向以及垂直于第二流体流动方向均会变化。一个具有一种混合流体和一种非混合流体的换热器示例类似于以下配置。

具有两种非混合流体的换热器类似于以下配置。

在逆流和平行流布置中，一种流体的纵向温度变化会导致第二种流体的温度变化发生纵向变化，并且不考虑混合。

### 效能曲线

多程管壳式换热器（图中 **iv.b**-**e**，对应 2、3 和 4 程）是最高效的换热器类型。对于单程换热器，逆流配置（**ii**）最有效，平行流（**i**）最低效。

交叉流换热器的效能介于中间，混合条件是一个影响因素。当两种流动均非混合（**iii.a**）时它们最有效，当两种流动均混合（**iii.b**）时最低效。仅混合热容量速率最小的流动（**iii.c**）比仅混合热容量速率最大的流动（**iii.d**）更降低效能。

### 热阻

总热阻 *R* 是沿换热器壁面的因对流、导热和污垢而产生的传热局部热阻之和。

R=1U1A1+F1A1+RW+F2A2+1U2A2,

其中：

- *U*1 是热液体与壁面之间的传热系数。
- *U*2 是受控流体与壁面之间的传热系数，它在端口 **HC2** 处以物理信号形式接收。
- *F*1 是热液体的 **Fouling factor**。
- *F*2 是受控流体的 **Fouling factor**。
- *A*1 是热液体的 **Heat transfer surface area**。
- *A*2 是受控流体的 **Heat transfer surface area**。
- *R*W 是 **Wall thermal resistance**。

传热系数取决于换热器配置和流体属性。有关详细信息，请参阅 E-NTU Heat Transfer 参考页。

### 壁面热质量

如果选择 **Enable wall thermal mass**，该模块会对换热器壁面热质量建模，这会为壁面对温度或热流变化的瞬态响应引入延迟。如果对热质量建模，壁面会在其边界内存储热量。这种热量存储会减慢稳态之间的过渡，使一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率达到平衡为止。

如果选择 **Enable wall thermal mass**，壁面能量守恒为

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁面温度。该模块使用此值对瞬态响应建模。无法测量此值。

对每种流体的传热为

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容量速率。

每一侧流体与壁面之间的传热单元数为

NTU1=U1A1C1NTU2=U2A2C2

其中 *A* 是壁面表面积，*U* 是传热系数。

### 复合结构

当 Heat Exchanger (TL) 模块是 Heat Exchanger Interface (TL) 和 E-NTU Heat Transfer 模块的复合体时：
