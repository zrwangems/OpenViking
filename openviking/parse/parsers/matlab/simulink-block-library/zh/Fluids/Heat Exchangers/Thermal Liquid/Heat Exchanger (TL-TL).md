---
type: simulink-block
title: 'Heat Exchanger (TL-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'heatexchangertltl'
documentation_source_path: 'ref/heatexchangertltl.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger (TL-TL)

## 端口

### 守恒

### **A1** — Thermal liquid 1 端口 thermal liquid

供 Thermal liquid 1 进入和离开其热交换器一侧的开口。

### **B1** — Thermal liquid 1 端口 thermal liquid

供 Thermal liquid 1 进入和离开其热交换器一侧的开口。

### **A2** — Thermal liquid 2 端口 thermal liquid

供 Thermal liquid 2 进入和离开其热交换器一侧的开口。

### **B2** — Thermal liquid 2 端口 thermal liquid

供 Thermal liquid 2 进入和离开其热交换器一侧的开口。

## 参数

### 通用

### **Flow arrangement** — 热交换器中流动的排列方式 `Parallel or counter flow`（默认） | `Shell and tube` | `Cross flow` | `Generic - effectiveness table`

热交换器中流动的排列方式。流动可以彼此平行、彼此逆流或彼此交叉。它们也可以在加压壳体中流动，一股流经封闭在壳体中的管子，另一股绕这些管子流动。其他流动布置可以通过基于表格化效能数据的通用参数化实现，且只需很少的热交换器细节。

### **Wall thermal resistance** — 壁对通过热传导进行的热流的阻力 `0 K/W`（默认） | positive scalar

分隔两种热交换器流体的界面壁的热阻。

### **Number of shell passes** — 流体在离开前穿过壳体的次数 `1`（默认） | unitless scalar

流体在离开前穿过壳体的次数。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Cross flow type** — 每个流动通道中的混合条件 `Both fluids mixed`（默认） | `Both fluids unmixed` | `Thermal Liquid 1 mixed & Thermal Liquid 2 unmixed` | `Thermal Liquid 1 unmixed & Thermal Liquid 2 mixed`

每个流动通道中的混合条件。此上下文中的混合是指流体沿其流动通道向出口前进时的横向运动。各流动彼此保持分离。未混合流动常见于带有板、折流板或翅片的通道中。此设置会反映在热交换器的效能中，未混合流动效能最高，混合流动效能最低。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Number of heat transfer units vector, NTU** — 热交换器效能查找表中每个断点处的传热单元数 unitless numerical array

热交换器效能数查找表中每个断点处的传热单元数。该表是二维的，以传热单元数和热容比作为独立坐标。该模块对断点进行内插和外推，以获取任意传热单元数下的效能。插值为 MATLAB `linear` 类型，外推为 `nearest`。

指定的数必须大于零，并从左到右单调递增。向量的大小必须等于 **Effectiveness table** 参数中的行数。如果表有 *m* 行和 *n* 列，则传热单元数向量必须为 *m* 个元素长。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Thermal capacity ratio vector, CR** — 热交换器效能查找表中每个断点处的热容比 unitless numerical array

热交换器效能查找表中每个断点处的热容比。该表是二维的，以传热单元数和热容率比作为独立坐标。该模块对断点进行内插和外推，以获取任意热容比下的效能。插值为 MATLAB `linear` 类型，外推为 `nearest`。

热容比必须大于零，并从左到右单调递增。向量的大小必须等于 **Nusselt number table** 参数中的列数。如果表有 *m* 行和 *n* 列，则热容比向量必须为 *n* 个元素长。热容比是最小热容率与最大热容率的比值。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Effectiveness table, E(NTU,CR)** — 在传热单元数和热容比上的查找表中每个断点处的热交换器效能 unitless numerical array

热交换器效能在其关于传热单元数和热容比的查找表中每个断点处的值。该模块对断点进行内插和外推，以获取任意传热单元数和热容比组合下的效能。插值为 MATLAB `linear` 类型，外推为 `nearest`。

效能值不得为负。它们必须从上到下按传热单元数递增的顺序排列，并从左到右按热容比递增的顺序排列。行数必须等于 **Number of heat transfer units vector** 参数的大小，列数必须等于 **Thermal capacity ratio vector** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Enable wall thermal mass** — 用于对壁热质量建模的选项 `off`（默认） | `on`

是否对热交换器壁热质量建模。对壁热质量建模会在壁对温度或热流变化的瞬态响应中引入延迟。如果清除 **Enable wall thermal mass**，该模块会假定壁足够薄，以至于在传热的时间尺度上瞬态响应是瞬时的。

### **Wall mass** — 热交换器壁质量 `1 kg`（默认） | positive scalar

热交换器壁的质量。该模块使用此值计算壁热质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Wall specific heat** — 热交换器壁比热 `490 J/(K*kg)`（默认） | positive scalar

热交换器壁的比热。该模块使用此值计算壁热质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### Thermal Liquid 1|2 选项卡

### **Minimum free-flow area** — 流动通道在其最窄点处的横截面积 `0.01 m^2`（默认） | scalar with units of length squared

入口与出口之间最小的总横截流动面积。如果通道是管道、管子、槽或沟槽的集合，则此参数的值为最小流动面积点处的最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是某个横截面中管间间隙之和，该横截面中的间隙之和最小。

### **Hydraulic diameter for pressure loss** — 流动通道在其最窄点处的有效直径 `0.1 m`（默认） | scalar with units of length

流动在其最窄点处的有效内径。对于横截面非圆形的通道，该直径为与流动横截面积相等的假想圆的直径。其值为最小自由流动面积与其总周长的四分之一之比。

如果通道是管道、管子、槽或沟槽的集合，则总周长为该集合中各周长之和。如果通道是单根管道或管子且横截面为圆形，则水力直径与真实直径相同。

### **Thermal liquid volume** — thermal liquid 1 或 thermal liquid 2 流动通道中流体的总体积 `0.01 m^3`（默认） | scalar with units of length squared

thermal liquid 1 或 thermal liquid 2 流动通道中包含的流体总体积。

### **Laminar flow upper Reynolds number limit** — 层流与湍流区之间过渡的起点 `2000`（默认） | unitless scalar

层流与湍流区之间过渡的起点。高于此数时，惯性力开始占主导，流动逐渐变为湍流。默认值对应于表面光滑的圆管和管子的特征。

### **Turbulent flow lower Reynolds number limit** — 层流与湍流区之间过渡的终点 `4000`（默认） | unitless scalar

层流与湍流区之间过渡的终点。低于此数时，黏性力开始占主导，流动逐渐变为层流。默认值对应于表面光滑的圆管和管子的特征。

### **Pressure loss model** — 黏性摩擦导致的压力损失的数学模型 `Pressure loss coefficient`（默认） | `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

黏性摩擦导致的压力损失的数学模型。此设置确定用于计算的表达式以及要将哪些模块参数指定为输入。有关按参数化进行的计算，请参阅 Heat Exchanger Interface (TL) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1`（默认） | unitless scalar

流动通道中所有流动阻力的总损失系数，包括造成主要损失的壁面摩擦，以及由弯头、弯管和其他几何变化造成次要损失的局部阻力。

损失系数是常用于表示黏性摩擦导致的压力损失的经验无量纲数。它可以根据实验数据计算，或在某些情况下从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从端口到端口行进的距离 `1 m`（默认） | scalar with units of length

流动跨过端口必须行进的总距离。在多程管壳式交换器中，总距离是所有壳程距离之和。在管束、波纹板以及流动被分成平行支路的其他通道中，它是单个支路中经过的距离。流动路径越长，由壁面黏性摩擦造成的主要压力损失越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 以长度表示的次要压力损失总和 `0.1 m`（默认） | scalar with units of length

以长度表示的次要压力损失总和。该长度是所有这些局部阻力（例如弯头、三通和管接头）在由简单壁面延伸代替时会给流动路径增加的长度。等效长度越大，由局部阻力造成的次要压力损失越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 壁面摩擦背后表面凸起的平均高度 `15e-6 m`（默认） | scalar with units of length

产生壁面摩擦的表面凸起的平均高度。凸起越高，壁面越粗糙，摩擦越大，因此压力损失越大。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由该关联式导出，压力损失计算也依赖于该关联式。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流动横截面的压力损失修正 `64`（默认） | unitless scalar

层流条件下流动横截面的压力损失修正。此参数通常称为形状因子。它与雷诺数的比值给出层流区压力损失计算所用的 Darcy 摩擦因子。默认值适用于圆柱形管道和管子。

对于某些形状，形状因子由 Navier-Stokes 方程的解导出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长导管也是如此。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的雷诺数 unitless numerical array

Darcy 摩擦因子查找表中每个断点处的雷诺数。该模块对断点进行内插和外推，以获取任意雷诺数下的 Darcy 摩擦因子。插值为 MATLAB `linear` 类型，外推为 `nearest`。

雷诺数必须大于零，并从左到右单调递增。它们可以跨越层流、过渡和湍流区。它们的数量必须等于 **Darcy friction factor vector** 参数的大小，二者结合以构成表格化的断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — Darcy 摩擦因子在其关于雷诺数的查找表中每个断点处的值 unitless numerical array

Darcy 摩擦因子在其关于雷诺数的查找表中每个断点处的值。该模块对断点进行内插和外推，以获取任意雷诺数下的 Darcy 摩擦因子。插值为 MATLAB `linear` 类型，外推为 `nearest`。

Darcy 摩擦因子不得为负，并且必须从左到右按雷诺数递增的顺序排列。它们的数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，二者结合以构成表格化的断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — Euler 数查找表中每个断点处的雷诺数 unitless numerical array

Euler 数查找表中每个断点处的雷诺数。该模块对断点进行内插和外推，以获取任意雷诺数下的 Euler 数。插值为 MATLAB `linear` 类型，外推为 `nearest`。

雷诺数必须大于零，并从左到右单调递增。它们可以跨越层流、过渡和湍流区。它们的数量必须等于 **Euler number vector** 参数的大小，二者结合以构成表格化的断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **欧拉数向量** — 基于雷诺数的查找表中每个断点处的欧拉数 无量纲数值数组

基于雷诺数的查找表中每个断点处的欧拉数。模块对这些断点进行内插和外推，以获得任意雷诺数下的欧拉数。插值为 MATLAB `linear` 类型，外推为 `nearest`。

欧拉数不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **欧拉数的雷诺数向量** 参数的大小，它们将与该参数结合以构成表格化断点。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **传热系数模型** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient`（默认） | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定要应用哪些表达式以及要为传热计算指定哪些参数。关于按参数化进行的计算，请参阅 E-NTU Heat Transfer 模块。

### **传热表面积** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2`（默认） | 具有长度平方单位的标量

流体与壁面之间传热所用的有效表面积。有效表面积是主表面积和次表面积之和，或者说是壁面暴露于流体的表面积与所使用的任何翅片的表面积之和。翅片表面积通常按翅片效率因子缩放。

### **液体-壁面传热系数** — 流体与壁面之间对流传热的传热系数 `100 W/(K*m^2)`（默认） | 标量

流体与壁面之间对流传热的传热系数。由污垢引起的热阻单独在 **污垢系数** 参数中体现。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Constant heat transfer coefficient`。

### **传热流动路径长度** — 流体与壁面之间传热所经过的特征长度 `1 m`（默认） | 具有长度单位的标量

流体与壁面之间传热所经过的特征长度。该长度参与水力直径的计算，而传热系数和雷诺数（在表格化传热参数化中定义）由该水力直径得出。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **层流传热的努塞尔数** — 层流中努塞尔数所假设的常数 `3.66`（默认） | 正无量纲标量

层流中努塞尔数所假设的常数。努塞尔数参与流体与壁面之间传热系数的计算，而传热速率取决于该传热系数。默认值适用于圆柱形管道和管束。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Correlation for flow inside tubes`。

### **Colburn 因子的雷诺数向量** — 指定 Colburn 因子数据时的雷诺数取值 无量纲数值数组

Colburn 因子查找表中每个断点处的雷诺数。模块对这些断点进行内插和外推，以获得任意雷诺数下的 Colburn 因子。插值为 MATLAB `linear` 类型，外推为 `nearest`。

雷诺数必须大于零，并从左到右单调递增。它们可以跨越层流、过渡流和湍流区。其数量必须等于 **Colburn 因子向量** 参数的大小，它们将与该参数结合以构成表格化断点。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn 因子向量** — 基于雷诺数的查找表中每个断点处的 Colburn 因子 无量纲数值数组

基于雷诺数的查找表中每个断点处的 Colburn 因子。模块对这些断点进行内插和外推，以获得任意雷诺数下的欧拉数。插值为 MATLAB `linear` 类型，外推为 `nearest`。

Colburn 因子不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Colburn 因子的雷诺数向量** 参数的大小，它们将与该参数结合以构成表格化断点。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **努塞尔数的雷诺数向量** — 努塞尔数查找表中每个断点处的雷诺数 无量纲数值数组

努塞尔数查找表中每个断点处的雷诺数。该表是二维的，以雷诺数和普朗特数作为独立坐标。模块对这些断点进行内插和外推，以获得任意雷诺数下的努塞尔数。插值为 MATLAB `linear` 类型，外推为 `nearest`。

雷诺数必须大于零，并从左到右单调递增。它们可以跨越层流、过渡流和湍流区。向量的大小必须等于 **努塞尔数表** 参数中的行数。如果该表有 *m* 行和 *n* 列，则雷诺数向量必须为 *m* 个元素长。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **努塞尔数的普朗特数向量** — 努塞尔数查找表中每个断点处的普朗特数 无量纲数值数组

努塞尔数查找表中每个断点处的普朗特数。该表是二维的，以雷诺数和普朗特数作为独立坐标。模块对这些断点进行内插和外推，以获得任意普朗特数下的努塞尔数。插值为 MATLAB `linear` 类型，外推为 `nearest`。

普朗特数必须大于零，并从左到右单调递增。它们可以跨越层流、过渡流和湍流区。向量的大小必须等于 **努塞尔数表** 参数中的列数。如果该表有 *m* 行和 *n* 列，则普朗特数向量必须为 *n* 个元素长。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **努塞尔数表，Nu (Re,Pr)** — 基于雷诺数和普朗特数的查找表中每个断点处的努塞尔数 无量纲数值数组

基于雷诺数和普朗特数的查找表中每个断点处的努塞尔数。模块对这些断点进行内插和外推，以获得任意雷诺数和普朗特数组合下的努塞尔数。插值为 MATLAB `linear` 类型，外推为 `nearest`。通过确定努塞尔数，该表为流体与壁面之间传热系数的计算提供输入。

努塞尔数必须大于零。它们必须按雷诺数递增的顺序从上到下排列，并按普朗特数递增的顺序从左到右排列。行数必须等于 **努塞尔数的雷诺数向量** 参数的大小，列数必须等于 **努塞尔数的普朗特数向量** 参数的大小。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **污垢系数** — 由污垢沉积引起的热阻量度 `1e-4 K*m^2/W`（默认） | 具有温度/功率单位的标量

由污垢沉积引起的热阻量度，污垢沉积随时间推移倾向于在壁面的暴露表面上积聚。这些沉积物在流体与壁面之间形成一层新的固体层，热量必须穿过该层，从而为传热路径增加额外的热阻。污垢沉积增长缓慢，因此假定其引起的热阻在仿真期间恒定。

### **最小液体-壁面传热系数** — 传热系数的下界 `1 W/(m^2 * K)`（默认） | 具有功率/面积/温度单位的标量

流体与壁面之间传热系数的下界。如果计算得到的传热系数更低，则用此下界替换计算值。

### 效应和初始条件

### **启用 Thermal Liquid 1 动态可压缩性** — 换热器中液体可压缩性的设置 `On`（默认） | `Off` | 标量

用于对换热器内部压力动态进行建模的选项。将此参数设置为 `Off` 会从组件能量和质量守恒方程中移除压力导数项。此时换热器内部的压力简化为两个端口压力的加权平均值。

### **Thermal Liquid 1 标称温度** — 标称工况下的温度 `293.15 K`（默认） | 标量

标称工况下的热液体温度。当禁用动态可压缩性时，模块使用该值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用 Thermal Liquid 1 动态可压缩性** 复选框。

### **Thermal Liquid 1 标称压力** — 标称工况下的压力 `0.101325 MPa`（默认） | 标量

标称工况下的热液体压力。当禁用动态可压缩性时，模块使用该值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用 Thermal Liquid 1 动态可压缩性** 复选框。

### **Thermal Liquid 1 初始温度** — 仿真开始时 Thermal Liquid 1 中的温度 `293.15 K`（默认） | 具有温度单位的标量

仿真开始时 Thermal Liquid 1 通道中的温度。

### **Thermal Liquid 1 初始压力** — 仿真开始时 Thermal Liquid 1 通道中的压力 `0.101325 MPa`（默认） | 具有压力单位的标量

仿真开始时 Thermal Liquid 1 通道中的压力。

#### 依赖关系

要启用此参数，请选中 **启用 Thermal Liquid 1 动态可压缩性**。

### **启用 Thermal Liquid 2 动态可压缩性** — 用于对 Thermal Liquid 2 通道中的压力动态进行建模的选项 `On`（默认） | `Off`

用于对 Thermal Liquid 2 通道中的压力动态进行建模的选项。如果清除此复选框，模块会从组件能量和质量守恒方程中移除压力导数项。此时换热器内部的压力简化为两个端口压力的加权平均值。

### **Thermal Liquid 2 标称温度** — 标称工况下的温度 `293.15 K`（默认） | 标量

标称工况下的热液体温度。当禁用动态可压缩性时，模块使用该值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用 Thermal Liquid 2 动态可压缩性** 复选框。

### **Thermal Liquid 2 标称压力** — 标称工况下的压力 `0.101325 MPa`（默认） | 标量

标称工况下的热液体压力。当禁用动态可压缩性时，模块使用该值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用 Thermal Liquid 2 动态可压缩性** 复选框。

### **Thermal Liquid 2 初始温度** — 仿真开始时 Thermal Liquid 1 中的温度 `293.15 K`（默认） | 具有温度单位的标量

仿真开始时 Thermal Liquid 2 通道中的温度。

### **Thermal Liquid 2 初始压力** — 仿真开始时 Thermal Liquid 1 通道中的压力 `0.101325 MPa`（默认） | 具有压力单位的标量

仿真开始时 Thermal Liquid 2 通道中的压力。

#### 依赖关系

要启用此参数，请选中 **启用 Thermal Liquid 2 动态可压缩性**。

## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024a: Heat Exchanger (TL-TL) 模块仅对 E-NTU 建模选项进行建模

**建模选项** 参数已被移除，建模选项现在为两个单独的模块。Heat Exchanger (TL-TL) 模块使用以前在 **建模选项** 为 `E-NTU Model` 时所用的传热模型。若要使用以前在 **建模选项** 为 `Simple model` 时所用的模块模型，请参阅 Specific Dissipation Heat Exchanger (TL-TL) 模块。

## 描述

用于具有两股热液体流的系统的换热器

Heat Exchanger (TL-TL) 模块对短暂热接触、通过薄导热壁隔开的两股流体之间的互补冷却和加热进行建模。壁面可以在其边界内存储热量，从而为传热增加轻微的瞬态延迟，该延迟与其热质量成比例。流体为单相，且各为一种热液体。两种流体均不能发生相变，因此由于潜热从不释放，交换严格来说是显热交换。

### Heat Transfer Model

该模块的传热模型源自 Effectiveness-NTU 方法。稳态下的传热随后以理想速率的一个分数进行；如果各股流体均保持其入口温度，并且清除其间所有热阻，则这些流体理论上可支持该理想速率：

Q=ϵ QMax,

其中 *Q* 是实际传热速率，*Q*Max 是理想传热速率，而 *QAct* 是在存在损失的真实热交换器中实际观察到的理想速率的分数。该分数是热交换器效能，并且是传热单元数（或 NTU）的函数；NTU 衡量热量在流体之间传递的容易程度相对于流体吸收该热量的容易程度：

NTU=1RCMin,

其中该分数是两股流体之间的总热导，而 *CMin* 是属于最不能吸收热量的流体的各热容率中的最小值。一股流体的热容率取决于流体的比热（*c*p）及其通过换热器的质量流率（m˙）：

C=cpm˙.

效能还取决于流体的相对布置、它们之间的程数以及每者的混合条件。这种依赖性体现在所使用的效能表达式中，不同的流动布置对应不同的表达式。有关效能表达式的列表，请参阅 E-NTU Heat Transfer 模块。

模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 流动布置

使用 **Flow arrangement** 参数设置流体在热交换器中如何相遇。流体可以彼此平行、彼此逆流或彼此交叉流动。它们也可以在带压壳体中流动，一股流经封闭在壳体中的管，另一股围绕这些相同的管流动。图中展示了一个示例。管程流体可以单程通过壳程流体（右侧所示），或者为获得更高的换热器效能而多程通过（左侧）。

还可以通过基于表格化效能数据的通用参数化实现其他流动布置，并且几乎不需要热交换器的细节。若与热交换器相关，流动布置、混合条件以及壳程或管程数假定体现在表格化数据中。

### 混合条件

使用 **Cross flow type** 参数混合两股流体中的每一股、其中一股或所有流体都不混合。此上下文中的混合是指流体在无内部屏障（通常为导流板、折流板、翅片或壁）的通道中的横向运动。此类运动用于消除横向平面内的温度变化。混合流仅在纵向平面内具有可变温度。非混合流在横向和纵向平面内均具有可变温度。图中展示了混合流（**i**）和非混合流（**ii**）。

混合流与非混合流之间的区别仅在交叉流布置中考虑。在那里，一种流体中的纵向温度变化会在第二种流体中产生横向温度变化，而混合可以消除该变化。在逆流和平行流布置中，一种流体中的纵向温度变化会在第二种流体中产生纵向温度变化，而混合在此影响很小，因此忽略。

### 效能曲线

具有多程的壳管式换热器（图中 **iv.b**-**e** 对应 2、3 和 4 程）最有效。在单程换热器中，逆流（**ii**）最有效，平行流（**i**）最低。

交叉流换热器的效能居中，混合条件起作用。当两股流体均非混合（**iii.a**）时最有效，当两股流体均混合（**iii.b**）时最低效。仅混合具有最小热容率的流体（**iii.c**）比仅混合具有最大热容率的流体（**iii.d**）更降低效能。

### 热阻

总热阻 *R* 是沿传热路径排列的局部热阻之和。局部热阻来自壁面表面的对流、通过壁面的传导，以及如果壁面两侧结垢，则来自结垢层的传导。按从热液体侧 1 到热液体侧 2 的顺序表示：

R=1U1A1+F1A1+RW+F2A2+1U2A2,

其中 *U* 是对流换热系数，*F* 是污垢系数，*A* 是传热表面积，各自对应下标所示的流体。*R*W 是壁面的热阻。

壁面热阻和污垢系数是从模块参数获得的简单常数。换热系数是流体属性、流动几何和壁面摩擦的复杂函数，并源自 Reynolds、Nusselt 和 Prandtl 数之间的标准经验关联式。这些关联式取决于流动布置和混合条件，并在模型所基于的 E-NTU Heat Transfer 模块中针对每种情况详细说明。

### 壁面热质量

如果选择 **Enable wall thermal mass**，模块将对热交换器壁面热质量建模，这会引入壁面对温度或热流变化瞬态响应的延迟。如果对热质量建模，壁面会在其边界内储存热量。这种热量储存会减慢稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续，直到两侧的热流率平衡。

如果选择 **Enable wall thermal mass**，壁面能量守恒为

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁面温度。模块使用该值来建模瞬态响应。你无法测量该值。

向每种流体的传热为

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容率。

每一侧流体与壁面之间的传热单元数为

NTU1=U1A1C1NTU2=U2A2C2

其中 *A* 是壁面表面积，*U* 是换热系数。

### 复合结构

该模块是由更简单模块构建的复合组件。一个 Heat Exchanger Interface (TL) 模块对热交换器侧 1 的热液体流动建模。另一个模块对侧 2 的热液体流动建模。一个 E-NTU Heat Transfer 模块对跨壁面在流体之间交换的热量建模。
