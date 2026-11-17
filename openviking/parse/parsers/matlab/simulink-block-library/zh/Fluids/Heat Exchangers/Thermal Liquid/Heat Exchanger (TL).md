---
type: simulink-block
title: 'Heat Exchanger (TL)'
family: 'hydro'
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

### 守恒端口

### **A1** — 热液体端口 thermal liquid

热液体进入和离开换热器其所在侧的开口。

### **B1** — 热液体端口 thermal liquid

热液体进入和离开换热器其所在侧的开口。

### **H2** — 受控流体 2 的入口温度 thermal

受控流体 2 的入口温度。
### 输入

### **C2** — 热容率 physical signal

受控流热容率的瞬时值。

### **HC2** — 传热系数 physical signal

受控流与壁面之间传热系数的瞬时值。

## 参数

### 通用

### **Flow arrangement** — 换热器中流动的排列方式 `Parallel or counter flow`（默认）| `Shell and tube` | `Cross flow` | `Generic - effectiveness table`

换热器中流动的排列方式。流动可以彼此平行、彼此逆向或彼此交叉。它们也可以在加压壳体内流动，一股通过封闭在壳体内的管束，另一股围绕这些管束流动。通过基于表格化效能数据的通用参数化方法，还可以实现其他流动排列方式，且只需很少的换热器细节。

### **Number of shell passes** — 流体在离开之前穿过壳体的次数 `1`（默认）| 无量纲标量

流体在离开之前穿过壳体的次数。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Cross flow type** — 每个流动通道中的混合条件 `Both fluids mixed`（默认）| `Both fluids unmixed` | `Thermal liquid mixed & Controlled Fluid unmixed` | `Thermal liquid unmixed & Controlled Fluid mixed`

每个流动通道中的混合条件。此处的混合是指流体沿其流动通道向出口前进时的横向运动。各流动彼此保持分离。未混合流动常见于带有板片、折流板或翅片的通道中。此设置会影响换热器的效能，未混合流动效能最高，混合流动效能最低。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Number of heat transfer units vector, NTU** — 换热器效能查找表中每个断点处的传热单元数 无量纲数值数组

换热器效能数查找表中每个断点处的传热单元数。该表是二维的，传热单元数和热容比均作为独立坐标。模块对断点进行内插和外推，以获得任意传热单元数下的效能。插值为 `linear`，外推为 `nearest`。

指定的数值必须大于零，并且从左到右单调递增。向量的大小必须等于 **Effectiveness table** 参数的行数。如果表有 *m* 行和 *n* 列，则传热单元数的向量长度必须为 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Thermal capacity ratio vector, CR** — 换热器效能查找表中每个断点处的热容比 无量纲数值数组

换热器效能查找表中每个断点处的热容比。该表是二维的，传热单元数和热容率比均作为独立坐标。模块对断点进行内插和外推，以获得任意热容比下的效能。插值为 `linear`，外推为 `nearest`。

热容比必须大于零，并且从左到右单调递增。向量的大小必须等于 **Nusselt number table** 参数的列数。如果表有 *m* 行和 *n* 列，则热容比的向量长度必须为 *n* 个元素。热容比是最小热容率与最大热容率的比值。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Effectiveness table, E(NTU,CR)** — 换热器效能查找表中每个断点处基于传热单元数和热容比的效能 无量纲数值数组

换热器效能查找表中每个断点处基于传热单元数和热容比的效能。模块对断点进行内插和外推，以获得任意传热单元数和热容比组合下的效能。插值为 `linear`，外推为 `nearest`。

效能值必须为非负。它们必须按照传热单元数递增的顺序从上到下排列，并按照热容比递增的顺序从左到右排列。行数必须等于 **Number of heat transfer units vector** 参数的大小，列数必须等于 **Thermal capacity ratio vector** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Wall thermal resistance** — 壁面对热传导流动的阻力 `0 K/W`（默认）| 单位为温度除以功率的标量

壁面对热传导流动的阻力，也是热导的倒数，即热导率与表面积与长度之比的乘积。壁面阻力与对流阻力和污垢阻力相加，以确定各流动之间的总传热系数。

### **Enable wall thermal mass** — 用于对壁面热质量建模的选项 `off`（默认）| `on`

是否对换热器壁面热质量建模。对壁面热质量建模会在壁面对温度或热流变化做出响应时引入瞬态延迟。如果清除 **Enable wall thermal mass**，模块将假定壁面足够薄，以至于在传热的时间尺度上瞬态响应是即时的。

### **Wall mass** — 换热器壁面质量 `1 kg`（默认）| 正标量

换热器壁面的质量。模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Wall specific heat** — 换热器壁面比热 `490 J/(K*kg)`（默认）| 正标量

换热器壁面的比热。模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### 热液体

### **Minimum free-flow area** — 流动通道在其最窄点处的横截面积 `0.01 m^2`（默认）| 单位为长度平方的标量

入口和出口之间最小的总横截流动面积。如果通道是管道、管子、槽或沟的集合，则此参数的值是最小流动面积点处最小面积的总和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是某一横截面中管子之间间隙的总和，其中间隙总和最小。

### **Thermal liquid volume** — 热液体流动通道中流体的总体积 `0.01 m^3`（默认）| 单位为长度平方的标量

热液体流动通道中包含的流体总体积。

### **Hydraulic diameter for pressure loss** — 流道最窄处的有效直径 `0.1 m`（默认）| 带长度单位的标量

流动在最窄处的有效内径。对于非圆形横截面的通道，该直径为与流动横截面积相等的假想圆的直径。其值为最小自由流动面积与其总周长四分之一之比。

如果通道是由管道、管子、槽或沟组成的集合，则总周长为该集合中各周长的总和。如果通道是单根管道或管子且横截面为圆形，则水力直径与真实直径相同。

### **Laminar flow upper Reynolds number limit** — 层流区与湍流区之间过渡的起点 `2000`（默认）| 无量纲标量

层流区与湍流区之间过渡的起点。高于此数值时，惯性力占主导，流动逐渐变为湍流。默认值为表面光滑的圆形管道和管子的特征值。

### **Turbulent flow lower Reynolds number limit** — 层流区与湍流区之间过渡的终点 `4000`（默认）| 无量纲标量

层流区与湍流区之间过渡的终点。低于此数值时，黏性力占主导，流动逐渐变为层流。默认值为表面光滑的圆形管道和管子的特征值。

### **Pressure loss model** — 黏性摩擦压降的数学模型 `Pressure loss coefficient`（默认）| `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

黏性摩擦压降的数学模型。此设置决定用于计算的表达式以及需要作为输入指定的模块参数。有关各参数化方式的计算方法，请参阅 Heat Exchanger Interface (TL) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1`（默认）| 无量纲标量

流道中所有流动阻力的总损失系数，包括造成沿程损失（major loss）的壁面摩擦以及由弯头、肘管和其他几何变化引起的造成局部损失（minor loss）的局部阻力。

损失系数是一个经验无量纲数，常用于表示黏性摩擦引起的压降。它可以通过实验数据计算得出，在某些情况下也可以从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从端口到端口所经过的距离 `1 m`（默认）| 带长度单位的标量

流动跨越端口所需经过的总距离。在多程管壳式换热器中，总距离为所有壳程距离之和。在管束、波纹板和其他流动被分成并联支路的通道中，该距离为单个支路中经过的距离。流动路径越长，壁面黏性摩擦引起的沿程压降越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 以长度表示的局部压降总和 `0.1 m`（默认）| 带长度单位的标量

以长度表示的局部压降总和。该长度是指所有局部阻力（如弯头、三通和管接头）在流动路径中所增加的等效长度，相当于用一段直壁延伸替代这些局部阻力。等效长度越大，局部阻力引起的局部压降越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 壁面摩擦所对应的表面凸起平均高度 `15e-6 m`（默认）| 带长度单位的标量

产生壁面摩擦的表面凸起平均高度。凸起越高，壁面越粗糙，摩擦越大，压降越大。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由该关联式导出，压降计算依赖于该摩擦因子。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流动横截面的压降修正 `64`（默认）| 无量纲标量

层流条件下流动横截面的压降修正。此参数通常称为形状因子。其与雷诺数之比给出层流区压降计算所用的 Darcy 摩擦因子。默认值属于圆柱形管道和管子。

对于某些形状，形状因子可由 Navier-Stokes 方程的解导出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长通道也是如此。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的雷诺数 无量纲数值数组

Darcy 摩擦因子查找表中每个断点处的雷诺数。模块对这些断点进行内插和外推，以获得任意雷诺数下的 Darcy 摩擦因子。插值方式为 `linear`，外推方式为 `nearest`。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Darcy friction factor vector** 参数的大小，两者结合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — 随雷诺数变化的查找表中每个断点处的 Darcy 摩擦因子 无量纲数值数组

Darcy 摩擦因子在其随雷诺数变化的查找表中每个断点处的值。模块对这些断点进行内插和外推，以获得任意雷诺数下的 Darcy 摩擦因子。插值方式为 `linear`，外推方式为 `nearest`。

Darcy 摩擦因子不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，两者结合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — Euler 数查找表中每个断点处的雷诺数 无量纲数值数组

Euler 数查找表中每个断点处的雷诺数。模块对这些断点进行内插和外推，以获得任意雷诺数下的 Euler 数。插值方式为 `linear`，外推方式为 `nearest`。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Euler number vector** 参数的大小，两者结合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler number vector** — 查找表中每个断点处的欧拉数，基于雷诺数 无量纲数值数组

查找表中每个断点处的欧拉数，基于雷诺数。该模块对断点进行内插和外推，以获得任意雷诺数下的欧拉数。插值方法为 `linear`，外推方法为 `nearest`。

欧拉数不得为负值，且必须按雷诺数递增的顺序从左到右排列。其数量必须与 **Reynolds number vector for Euler number** 参数的大小相等，两者结合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Heat transfer coefficient model** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient`（默认） | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定了传热计算中应用哪些表达式以及指定哪些参数。有关按参数化方式进行的计算，请参见 E-NTU Heat Transfer 模块。

### **Heat transfer surface area** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2`（默认） | 具有长度平方单位的标量

流体与壁面之间传热所用的有效表面积。有效表面积是一次表面积和二次表面积之和，即壁面暴露于流体的表面积与翅片（如有使用）的表面积之和。翅片表面积通常按翅片效率因子进行缩放。

### **Liquid-wall heat transfer coefficient** — 流体与壁面之间对流传热系数 `100 W/(K*m^2)`（默认） | 标量

流体与壁面之间对流传热系数。污垢热阻在 **Fouling factor** 参数中单独体现。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Constant heat transfer coefficient`。

### **Length of flow path for heat transfer** — 流体与壁面之间传热所经过的特征长度 `1 m`（默认） | 具有长度单位的标量

流体与壁面之间传热所经过的特征长度。该长度参与水力直径的计算，而传热系数和雷诺数（如表格化传热参数化中所定义）均由水力直径推导得出。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number for laminar flow heat transfer** — 层流传热中努塞尔数的假定常数值 `3.66`（默认） | 正的无量纲标量

层流传热中努塞尔数的假定常数值。努塞尔数参与流体与壁面之间传热系数的计算，传热速率取决于该传热系数。默认值适用于圆柱形管道和管子。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Colburn factor** — 指定科尔本因子数据时的雷诺数值 无量纲数值数组

科尔本因子查找表中每个断点处的雷诺数。该模块对断点进行内插和外推，以获得任意雷诺数下的科尔本因子。插值方法为 `linear`，外推方法为 `nearest`。

雷诺数必须大于零，且从左到右单调递增。它们可以跨越层流、过渡和湍流区域。其数量必须与 **Colburn factor vector** 参数的大小相等，两者结合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn factor vector** — 查找表中每个断点处的科尔本因子，基于雷诺数 无量纲数值数组

查找表中每个断点处的科尔本因子，基于雷诺数。该模块对断点进行内插和外推，以获得任意雷诺数下的欧拉数。插值方法为 `linear`，外推方法为 `nearest`。

科尔本因子不得为负值，且必须按雷诺数递增的顺序从左到右排列。其数量必须与 **Reynolds number vector for Colburn factor** 参数的大小相等，两者结合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Reynolds number vector for Nusselt number** — 努塞尔数查找表中每个断点处的雷诺数 无量纲数值数组

努塞尔数查找表中每个断点处的雷诺数。该表是二维的，以雷诺数和普朗特数作为独立坐标。该模块对断点进行内插和外推，以获得任意雷诺数下的努塞尔数。插值方法为 `linear`，外推方法为 `nearest`。

雷诺数必须大于零，且从左到右单调递增。它们可以跨越层流、过渡和湍流区域。向量的大小必须等于 **Nusselt number table** 参数的行数。如果该表有 *m* 行和 *n* 列，则雷诺数向量的长度必须为 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Prandtl number vector for Nusselt number** — 努塞尔数查找表中每个断点处的普朗特数 无量纲数值数组

努塞尔数查找表中每个断点处的普朗特数。该表是二维的，以雷诺数和普朗特数作为独立坐标。该模块对断点进行内插和外推，以获得任意普朗特数下的努塞尔数。插值方法为 `linear`，外推方法为 `nearest`。

普朗特数必须大于零，且从左到右单调递增。它们可以跨越层流、过渡和湍流区域。向量的大小必须等于 **Nusselt number table** 参数的列数。如果该表有 *m* 行和 *n* 列，则普朗特数向量的长度必须为 *n* 个元素。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number table, Nu (Re,Pr)** — 在雷诺数和普朗特数查找表中每个断点处的努塞尔数 无量纲数值数组

在雷诺数和普朗特数查找表中每个断点处的努塞尔数。该模块对断点进行内插和外推，以获得任意一对雷诺数和普朗特数下的努塞尔数。插值方法为 `linear`，外推方法为 `nearest`。通过确定努塞尔数，该表为流体与壁面之间传热系数的计算提供输入。

努塞尔数必须大于零。它们必须从上到下按雷诺数递增的顺序排列，从左到右按普朗特数递增的顺序排列。行数必须等于 **Reynolds number vector for Nusselt number** 参数的大小，列数必须等于 **Prandtl number vector for Nusselt number** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Fouling factor** — 由污垢沉积引起的热阻度量 `1e-4 K*m^2/W`（默认）| 单位为温度除以功率的标量

由污垢沉积引起的热阻度量，污垢随时间倾向于在壁面的暴露表面上积聚。这些沉积物在流体与壁面之间形成新的固体层，热量必须穿过该层，从而在传热路径中增加了额外的热阻。污垢沉积物增长缓慢，因此其引起的热阻在仿真期间假定为常数。

### **Minimum liquid-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)`（默认）| 单位为功率/面积/温度的标量

流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则此下界将替代计算值。

### Controlled Fluid

### **Heat transfer surface area** — 受控流体侧的总传热表面积 `0.4 m^2`（默认）| 单位为长度平方的标量

受控流体侧的传热表面积总和

### **Fouling factor** — 由污垢沉积引起的热阻度量 `1e-4 K*m^2/W`（默认）| 单位为长度平方乘以温度除以功率的标量

由污垢沉积引起的热阻度量，污垢随时间倾向于在壁面的暴露表面上积聚。这些沉积物在受控流体与壁面之间形成新的固体层，热量必须穿过该层，从而在传热路径中增加了额外的热阻。污垢沉积物增长缓慢，因此其引起的热阻在仿真期间假定为常数。

### **Minimum fluid-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)`（默认）| 单位为功率/面积/温度的标量

受控流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则此下界将替代计算值。

### Effects and Initial Conditions

### **Enable Thermal Liquid dynamic compressibility** — 热交换器中液体可压缩性的设置 `On`（默认）| `Off` | 标量

用于对热交换器内部压力动态进行建模的选项。将此参数设置为 `Off` 会从组件能量和质量守恒方程中移除压力导数项。热交换器内部的压力随后被简化为两个端口压力的加权平均值。

### **Thermal Liquid nominal temperature** — 标称工况下的温度 `293.15 K`（默认）| 标量

标称工况下的热液体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid dynamic compressibility** 复选框。

### **Thermal Liquid nominal pressure** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的热液体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable Thermal Liquid dynamic compressibility** 复选框。

### **Thermal Liquid initial temperature** — 仿真开始时热液体通道中的温度 `293.15 K`（默认）| 单位为温度的标量

仿真开始时热液体通道中的温度

### **Thermal Liquid initial pressure** — 仿真开始时热液体通道中的压力 `0.101325 MPa`（默认）| 单位为压力的标量

仿真开始时热液体通道中的压力。

#### 依赖关系

要启用此参数，请选择 **Enable Thermal Liquid dynamic compressibility**。

## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2025a：对热交换器壁面的热质量进行建模

选择 **Wall thermal dynamics** 以对热交换器壁面的热质量进行建模。

### R2024a：Heat Exchanger (TL) 模块仅对 E-NTU 建模选项进行建模

**Modeling option** 参数已被移除，建模选项现在为两个独立的模块。Heat Exchanger (TL) 模块使用先前在 **Modeling option** 为 `E-NTU Model` 时使用的传热模型。要使用 **Modeling option** 为 `Simple model` 时使用的模块模型，请参见 Specific Dissipation Heat Exchanger (TL) 模块。

## 描述

用于具有热液体和受控流体的系统的热交换器

Heat Exchanger (TL) 模块通过薄壁导热对流体进行冷却和加热进行建模。单相热液体的属性在 **Thermal Liquid** 选项卡上定义。第二种流体是受控流体，仅由用户在 **Controlled Fluid** 选项卡上定义的参数指定。它不从域流体网络接收任何属性。流体之间的热交换基于热液体显热。

### 传热模型

该模块的传热模型源自 Effectiveness-NTU 方法。稳态传热基于将理想损失与系统实际损失关联的系数确定：

Q=ϵ QMax，

其中

- *Q* 为实际传热速率。
- *Q*Max 为理想传热速率。
- *ε* 为热交换器效能，它基于热容量率之比 CMinCMax 和交换器传热单元数：

  NTU=1RCMin，

  其中 *R* 为总热阻，将在下文热阻部分讨论。
  *C*Min 为两种流体中较小的热容量率，*C*Max 为两种流体中较大的热容量率。热容量率计算为 C=cpm˙。

此外，交换器效能取决于流体之间的通道数和流体混合条件。有关效能表达式的列表，请参见 E-NTU Heat Transfer 模块。将 E-NTU Heat Transfer 模块连接到 Heat Exchanger (TL) 模块，以使用 E-NTU 方法指定传热属性。

模块在传热计算中使用的流体属性为入口值与流体体积中值的平均值。

### 流动布置

使用 **Flow arrangement** 参数来定义管道方向或效能表方面的流动配置。使用管壳式配置时，可以选择换热器中的程数。多程换热器如下图所示。

单程换热器如下图所示。

其他流动布置可以通过表格化效能数据进行通用参数化来实现。该表不需要具体的换热器配置细节，例如流动布置、混合和程数，即可对流体之间的传热进行建模。

### 混合条件

使用 **Cross flow type** 参数来对不受折流板或壁面限制的流动进行建模，这种流动会使第二流体沿流动方向的温度均匀化，并在垂直于第二流体流动的方向上发生变化。未混合流动的温度沿第二流体流动方向以及垂直于该方向都会变化。一个混合流体与一个未混合流体的换热器示例如下图所示。

两种流体均未混合的换热器如下图所示。

在逆流和平流布置中，一种流体的纵向温度变化会导致第二种流体的纵向温度变化，并且不考虑混合。

### 效能曲线

多程管壳式换热器（图中 **iv.b**-**e** 分别对应 2、3 和 4 程）是最有效的换热器类型。对于单程换热器，逆流配置（**ii**）最有效，平流（**i**）最差。

交叉流换热器的效能介于两者之间，其中混合条件是一个影响因素。当两种流动均未混合（**iii.a**）时最有效，当两种流动均混合（**iii.b**）时最差。仅混合热容量率最小的流动（**iii.c**）比仅混合热容量率最大的流动（**iii.d**）更能降低效能。

### 热阻

总热阻 *R* 是沿换热器壁面由于对流、传导和污垢引起的局部传热阻力之和。

R=1U1A1+F1A1+RW+F2A2+1U2A2,

其中：

- *U*1 是热流体与壁面之间的传热系数。
- *U*2 是受控流体与壁面之间的传热系数，该系数以物理信号形式在端口 **HC2** 接收。
- *F*1 是热流体的 **Fouling factor**。
- *F*2 是受控流体的 **Fouling factor**。
- *A*1 是热流体的 **Heat transfer surface area**。
- *A*2 是受控流体的 **Heat transfer surface area**。
- *R*W 是 **Wall thermal resistance**。

传热系数取决于换热器配置和流体属性。有关更多信息，请参阅 E-NTU Heat Transfer 参考页。

### 壁面热质量

如果选择 **Enable wall thermal mass**，则该模块会对换热器壁面热质量进行建模，这会引入壁面对温度或热通量变化的瞬态响应延迟。如果对热质量进行建模，则壁面会在其边界内储存热量。这种热量储存会减缓稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续存在，直到两侧的热流率达到平衡。

如果选择 **Enable wall thermal mass**，则壁面能量守恒为

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁面温度。该模块使用此值来对瞬态响应进行建模。无法测量该值。

传递到每种流体的热量为

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容量率。

每一侧流体与壁面之间的传热单元数为

NTU1=U1A1C1NTU2=U2A2C2

其中 *A* 是壁面表面积，*U* 是传热系数。

### 复合结构

当 Heat Exchanger (TL) 模块是 Heat Exchanger Interface (TL) 和 E-NTU Heat Transfer 模块的复合体时：
