---
type: simulink-block
title: 'Heat Exchanger (G-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Gas'
documentation_page: 'heatexchangergtl'
documentation_source_path: 'ref/heatexchangergtl.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger (G-TL)

## 端口

### 守恒

### **A1** — 气体端口 gas

气体进入和离开热交换器该侧的开口。

### **B1** — 气体端口 gas

气体进入和离开热交换器该侧的开口。

### **A2** — 热液体端口 thermal liquid

thermal liquid 进入和离开热交换器该侧的开口。

### **B2** — 热液体端口 thermal liquid

thermal liquid 进入和离开热交换器该侧的开口。

## 参数

### 通用

### **Flow arrangement** — 热交换器中流动排列的方式 `Parallel or counter flow` (默认) | `Shell and tube` | `Cross flow` | `Generic - effectiveness table`

热交换器中流动排列的方式。流动可以彼此平行、彼此逆流或彼此交叉。它们也可以在加压壳体中流动，一种流体穿过封闭在壳体内的管束，另一种流体在那些管束周围流动。通过基于表格化效能数据的通用参数化，还可以实现其他流动布置，并且只需很少的热交换器细节。

### **Wall thermal resistance** — 壁面通过热传导阻碍热流的阻力 `0 K/W` (默认) | positive scalar

分隔两种热交换器流体的界面壁的热阻。

### **Number of shell passes** — 流体在离开之前穿过壳体的次数 `1` (默认) | unitless scalar

流体在离开之前穿过壳体的次数。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Cross flow type** — 每个流动通道中的混合条件 `Both fluids mixed` (默认) | `Both fluids unmixed` | `Thermal Liquid 1 mixed & Thermal Liquid 2 unmixed` | `Thermal Liquid 1 unmixed & Thermal Liquid 2 mixed`

每个流动通道中的混合条件。在此上下文中，混合是指流体沿其流动通道向出口前进时的横向运动。各流体彼此保持分离。未混合流动常见于带有板、折流板或翅片的通道中。此设置反映在热交换器的效能中，未混合流动效能最高，混合流动效能最低。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Shell and tube`。

### **Number of heat transfer units vector, NTU** — 热交换器效能的查找表中每个断点处的传热单元数 unitless numerical array

热交换器效能数的查找表中每个断点处的传热单元数。该表是二维的，传热单元数和热容量比都用作独立坐标。该模块使用线性插值和最近外插来获得任意传热单元数下的效能。

指定的数字必须大于零，并且从左到右单调递增。向量的大小必须等于 **Effectiveness table** 参数中的行数。如果表有 *m* 行和 *n* 列，则传热单元数的向量长度必须为 *m* 个元素。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Thermal capacity ratio vector, CR** — 热交换器效能的查找表中每个断点处的热容量比 unitless numerical array

热交换器效能的查找表中每个断点处的热容量比。该表是二维的，传热单元数和热容量率比都用作独立坐标。该模块使用线性插值和最近外插来获得任意热容量比下的效能。

热容量比必须大于零，并且从左到右单调递增。向量的大小必须等于 **Nusselt number table** 参数中的列数。如果表有 *m* 行和 *n* 列，则热容量比的向量长度必须为 *n* 个元素。热容量比是最小热容量率与最大热容量率之比。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Effectiveness table, E(NTU,CR)** — 热交换器效能在其查找表中针对传热单元数和热容量比的每个断点处的值 unitless numerical array

热交换器效能在其查找表中针对传热单元数和热容量比的每个断点处的值。该模块使用线性插值和最近外插来获得任意传热单元数和热容量比组合下的效能。

效能值必须不为负。它们必须从上到下按传热单元数递增的顺序排列，并从左到右按热容量比递增的顺序排列。行数必须等于 **Number of heat transfer units vector** 参数的大小，列数必须等于 **Thermal capacity ratio vector** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Generic - effectiveness table`。

### **Enable wall thermal mass** — 对壁面热质量建模的选项 `off` (默认) | `on`

是否对热交换器壁面热质量建模。对壁面热质量建模会在壁面对温度或热流变化作出瞬态响应时引入延迟。如果清除 **Enable wall thermal mass**，则该模块假定壁面足够薄，以至于在传热的时间尺度上瞬态响应是瞬时的。

### **Wall mass** — 热交换器壁面的质量 `1 kg` (默认) | positive scalar

热交换器壁面的质量。该模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 热交换器壁面的比热 `490 J/(K*kg)` (默认) | positive scalar

热交换器壁面的比热。该模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### 气体 1

### **Minimum free-flow area** — 流动通道在其最窄点处的横截面积 `0.01 m^2` (默认) | scalar with units of length squared

入口和出口之间最小的总流通截面积。如果通道是管道、管子、槽或沟槽的集合，则此参数的值是在最小流通面积点处最小面积的总和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是在一个横截面中管子之间间隙总和最小的那些间隙的总和。

### **Hydraulic diameter for pressure loss** — 流动通道在其最窄点处的有效直径 `0.1 m` (默认) | scalar with units of length

流动在其最窄点处的有效内径。对于横截面非圆形的通道，该直径为与流通截面积相等的假想圆的直径。其值为最小自由流通面积与其总周长的四分之一之比。

如果通道是管道、管子、槽或沟槽的集合，则总周长是该集合中各周长的总和。如果通道是单根管道或管子且横截面为圆形，则水力直径与真实直径相同。

### **Gas volume** — 流动通道中包含的流体总体积 `0.01 m^3` (默认) | scalar with units of length squared

气体流动通道中包含的流体总体积。

### **Laminar flow upper Reynolds number limit** — 层流区和湍流区之间过渡的起点 `2000` (默认) | unitless scalar

层流区和湍流区之间过渡的起点。高于此数字时，惯性力占主导，流动逐渐变为湍流。默认值对于表面光滑的圆管和管子具有代表性。

### **Turbulent flow lower Reynolds number limit** — 层流区和湍流区之间过渡的终点 `4000` (默认) | unitless scalar

层流区和湍流区之间过渡的终点。低于此数字时，黏性力占主导，流动逐渐变为层流。默认值对于表面光滑的圆管和管子具有代表性。

### **Pressure loss model** — 由黏性摩擦引起的压力损失的数学模型 `Pressure loss coefficient` (默认) | `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

由黏性摩擦引起的压力损失的数学模型。此设置确定用于计算的表达式以及要指定为输入的模块参数。有关按参数化进行的计算，请参阅 Heat Exchanger Interface (G) 和 Heat Exchanger Interface (TL) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1` (默认) | unitless scalar

流动通道中所有流动阻力的总损失系数，包括造成主要损失的壁面摩擦，以及造成次要损失的由弯头、肘管和其他几何变化引起的局部阻力。

损失系数是常用于表示由黏性摩擦引起的压力损失的经验无量纲数。它可以根据实验数据计算，或者在某些情况下从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从端口到端口行进的距离 `1 m` (默认) | scalar with units of length

流体必须穿过端口所经过的总距离。在多程管壳式交换器中，总距离是所有壳程的总和。在管束、波纹板和其他将流动分成并联支路的通道中，它是单个支路中经过的距离。流动路径越长，由壁面黏性摩擦引起的主要压力损失越陡。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 表示为长度的总次要压力损失 `0.1 m` (默认) | scalar with units of length

表示为长度的总次要压力损失。该长度是如果将所有局部阻力（例如弯头、三通和管接头）替换为简单的壁面延伸段，它们会向流动路径增加的长度。等效长度越大，由局部阻力引起的次要压力损失越陡。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 产生壁面摩擦的表面凸起的平均高度 `15e-6 m` (默认) | scalar with units of length

产生壁面摩擦的表面凸起的平均高度。凸起越高意味着壁面越粗糙，摩擦越大，因此压力损失越陡。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由该关联式导出，压力损失计算也依赖于该关联式。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流通截面的压力损失修正 `64` (默认) | unitless scalar

层流条件下流通截面的压力损失修正。此参数通常称为形状因子。其与 Reynolds 数的比值给出层流区压力损失计算所用的 Darcy 摩擦因子。默认值适用于圆柱形管道和管子。

对于某些形状，形状因子由 Navier-Stokes 方程的解导出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长导管也是如此。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的 Reynolds 数 unitless numerical array

Darcy 摩擦因子查找表中每个断点处的 Reynolds 数。该模块使用线性插值和最近外插来获得任意 Reynolds 数下的 Darcy 摩擦因子。

Reynolds 数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。它们的数量必须等于 **Darcy friction factor vector** 参数的大小，并与该参数结合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — Darcy 摩擦因子在其针对 Reynolds 数的查找表中每个断点处的值 unitless numerical array

Darcy 摩擦因子在其针对 Reynolds 数的查找表中每个断点处的值。该模块使用线性插值和最近外插来获得任意 Reynolds 数下的 Darcy 摩擦因子。

Darcy 摩擦因子必须不为负，并且必须从左到右按 Reynolds 数递增的顺序排列。它们的数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，并与该参数结合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — Euler 数查找表中每个断点处的 Reynolds 数 unitless numerical array

Euler 数查找表中每个断点处的 Reynolds 数。该模块使用线性插值和最近外插来获得任意 Reynolds 数下的 Euler 数。

Reynolds 数必须大于零，并且从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。它们的数量必须等于 **Euler number vector** 参数的大小，并与该参数结合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Euler number vector** — Euler 数在其针对 Reynolds 数的查找表中每个断点处的值 unitless numerical array

Euler 数在其针对 Reynolds 数的查找表中每个断点处的值。该模块使用线性插值和最近外插来获得任意 Reynolds 数下的 Euler 数。

Euler 数必须不为负，并且必须从左到右按 Reynolds 数递增的顺序排列。它们的数量必须等于 **Reynolds number vector for Euler number** 参数的大小，并与该参数结合以完成表格化断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number vs. Reynolds number`。

### **Heat transfer coefficient model** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient` (默认) | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定要应用哪些表达式以及要为传热计算指定哪些参数。有关按参数化进行的计算，请参见 E-NTU Heat Transfer 模块。

### **Heat transfer surface area** — 流体与壁面之间传热所用的有效表面积 `0.4 m^2` (默认) | 具有长度平方单位的标量

流体与壁面之间传热所用的有效表面积。有效表面积是一次表面积与二次表面积之和，即暴露于流体的壁面表面积与所用翅片（如果有）的表面积之和。翅片表面积通常按翅片效率因子进行缩放。

### **Gas-wall heat transfer coefficient** — 气体与壁面之间对流传热的传热系数 `100 W/(K*m^2)` (默认) | 标量

气体与壁面之间对流传热的传热系数。由结垢引起的热阻在 **Fouling factor** 参数中单独体现。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Constant heat transfer coefficient`。

### **Length of flow path for heat transfer** — 流体与壁面之间传热所经过的特征长度 `1 m` (默认) | 具有长度单位的标量

流体与壁面之间传热所经过的特征长度。该长度参与水力直径的计算，而水力直径又用于推导传热系数和 Reynolds 数，如表格化传热参数化中所定义。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number` 或 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number for laminar flow heat transfer** — 层流传热中假定的 Nusselt 数常量 `3.66` (默认) | 正的无量纲标量

层流传热中假定的 Nusselt 数常量。Nusselt 数参与流体与壁面之间传热系数的计算，传热速率取决于该系数。默认值属于圆柱形管道和管子。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Colburn factor** — 用于指定 Colburn 因子数据的 Reynolds 数值 无量纲数值数组

Colburn 因子查找表中每个断点处的 Reynolds 数。该模块使用线性插值和最近邻外插来获得任意 Reynolds 数下的 Colburn 因子。

Reynolds 数必须大于零，并从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Colburn factor vector** 参数的大小，与后者结合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Colburn factor vector** — 在 Reynolds 数查找表中每个断点处的 Colburn 因子 无量纲数值数组

在 Reynolds 数查找表中每个断点处的 Colburn 因子。该模块使用线性插值和最近邻外插来获得任意 Reynolds 数下的 Euler 数。

Colburn 因子不得为负，并且必须按 Reynolds 数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Colburn factor** 参数的大小，与后者结合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor vs. Reynolds number`。

### **Reynolds number vector for Nusselt number** — Nusselt 数查找表中每个断点处的 Reynolds 数 无量纲数值数组

Nusselt 数查找表中每个断点处的 Reynolds 数。该表是二维的，Reynolds 数和 Prandtl 数都用作独立坐标。该模块使用线性插值和最近邻外插来获得任意 Reynolds 数下的 Nusselt 数。

Reynolds 数必须大于零，并从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。向量的大小必须等于 **Nusselt number table** 参数中的行数。如果表有 *m* 行和 *n* 列，则 Reynolds 数向量必须为 *m* 个元素长。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Prandtl number vector for Nusselt number** — Nusselt 数查找表中每个断点处的 Prandtl 数 无量纲数值数组

Nusselt 数查找表中每个断点处的 Prandtl 数。该表是二维的，Reynolds 数和 Prandtl 数都用作独立坐标。该模块使用线性插值和最近邻外插来获得任意 Prandtl 数下的 Nusselt 数。

Prandtl 数必须大于零，并从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。向量的大小必须等于 **Nusselt number table** 参数中的列数。如果表有 *m* 行和 *n* 列，则 Prandtl 数向量必须为 *n* 个元素长。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Nusselt number table, Nu (Re,Pr)** — 在 Reynolds 数和 Prandtl 数查找表中每个断点处的 Nusselt 数 无量纲数值数组

在 Reynolds 数和 Prandtl 数查找表中每个断点处的 Nusselt 数。该模块使用线性插值和最近邻外插来获得任意一对 Reynolds 数和 Prandtl 数下的 Nusselt 数。通过确定 Nusselt 数，该表为计算提供输入，从而推导出流体与壁面之间的传热系数。

Nusselt 数必须大于零。它们必须按 Reynolds 数递增的顺序从上到下排列，并按 Prandtl 数递增的顺序从左到右排列。行数必须等于 **Reynolds number vector for Nusselt number** 参数的大小，列数必须等于 **Prandtl number vector for Nusselt number** 参数的大小。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`。

### **Fouling factor** — 由结垢沉积物引起的热阻度量 `1e-4 K*m^2/W` (默认) | 具有温度除以功率单位的标量

由结垢沉积物引起的热阻度量，这些沉积物随时间推移倾向于在壁面的暴露表面上积聚。这些沉积物在流体与壁面之间形成一层新的固体层，热量必须穿过该层，从而在传热路径中增加额外热阻。结垢沉积物增长缓慢，因此假定其引起的热阻在仿真期间恒定。

### **Minimum gas-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)` (默认) | 具有功率/面积/温度单位的标量

流体与壁面之间传热系数的下界。如果计算返回的传热系数更低，则此边界将替换计算值。

### Thermal Liquid 2

### **Minimum free-flow area** — 流动通道最窄点处的横截面积 `0.01 m^2` (默认) | 具有长度平方单位的标量

入口与出口之间最小的总横截面流动面积。如果通道是由管道、管子、槽或凹槽组成的集合，则此参数的值是在最小流动面积点处的最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是在一个横截面中管间间隙之和最小的那些间隙之和。

### **Hydraulic diameter for pressure loss** — 流动通道最窄点处的有效直径 `0.1 m` (默认) | 具有长度单位的标量

流动在其最窄点处的有效内径。对于横截面不是圆形的通道，该直径是一个假想圆的直径，该圆的面积等于流动横截面面积。其值是最小自由流动面积与其总周长四分之一之比。

如果通道是由管道、管子、槽或凹槽组成的集合，则总周长是集合中各周长的总和。如果通道是单根管道或管子且横截面为圆形，则水力直径与真实直径相同。

### **Liquid volume** — 流动通道中包含的流体总体积 `0.01 m^3` (默认) | 具有长度平方单位的标量

热液体流动通道中包含的流体总体积。

### **Laminar flow upper Reynolds number limit** — 层流区与湍流区之间过渡的起点 `2000` (默认) | 无量纲标量

层流区与湍流区之间过渡的起点。高于此数值时，惯性力起主导作用，流动逐渐变为湍流。默认值是表面光滑的圆管和管子的典型值。

### **Turbulent flow lower Reynolds number limit** — 层流区与湍流区之间过渡的终点 `4000` (默认) | 无量纲标量

层流区与湍流区之间过渡的终点。低于此数值时，黏性力起主导作用，流动逐渐变为层流。默认值是表面光滑的圆管和管子的典型值。

### **Pressure loss model** — 黏性摩擦引起压力损失的数学模型 `Pressure loss coefficient` (默认) | `Correlation for flow inside tubes` | `Tabulated data - Darcy friction factor vs. Reynolds number` | `Tabulated data - Euler number vs. Reynolds number`

黏性摩擦引起压力损失的数学模型。此设置决定计算时使用哪些表达式以及将哪些模块参数指定为输入。有关按参数化进行的计算，请参见 Heat Exchanger Interface (G) 和 Heat Exchanger Interface (TL) 模块。

### **Pressure loss coefficient** — 端口之间所有流动阻力的总损失系数 `0.1` (默认) | 无量纲标量

流动通道中所有流动阻力的总损失系数，包括造成沿程损失的壁面摩擦，以及由弯头、肘管和其他几何变化引起、造成局部损失的局部阻力。

损失系数是一个经验无量纲数，常用于表示黏性摩擦引起的压力损失。它可以根据实验数据计算，或者在某些情况下从产品数据表中获得。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Length of flow path from inlet to outlet** — 从端口到端口经过的距离 `1 m` (默认) | 具有长度单位的标量

流动跨越各端口所必须经过的总距离。在多程管壳式换热器中，总距离是所有壳程的之和。在管束、波纹板以及其他流动被分成并联支路的通道中，它是在单个支路中经过的距离。流动路径越长，壁面处黏性摩擦引起的沿程压力损失越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes` 或 `Tabulated data - Darcy friction factor vs Reynolds number`。

### **Aggregate equivalent length of local resistances** — 以长度表示的局部压力损失总和 `0.1 m` (默认) | 具有长度单位的标量

以长度表示的局部压力损失总和。该长度是如果所有局部阻力（如弯头、三通和管接头）都由简单的壁面延伸代替时，它们会为流动路径增加的长度。等效长度越大，局部阻力引起的局部压力损失越大。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Internal surface absolute roughness** — 壁面摩擦所对应的表面凸起平均高度 `15e-6 m` (默认) | 具有长度单位的标量

引起壁面摩擦的表面凸起平均高度。凸起越高，壁面越粗糙，摩擦越大，因此压力损失越大。表面粗糙度出现在 Haaland 关联式中，Darcy 摩擦因子由该关联式推导，压力损失计算依赖于该摩擦因子。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流条件下流动横截面的压力损失修正 `64` (默认) | 无量纲标量

层流条件下流动横截面的压力损失修正。此参数通常称为形状因子。其与 Reynolds 数的比值给出层流区压力损失计算所用的 Darcy 摩擦因子。默认值属于圆柱形管道和管子。

对于某些形状，形状因子由 Navier-Stokes 方程的解推导得出。方形管道的形状因子为 `56`，长宽比为 2:1 的矩形管道的形状因子为 `62`，环形管的形状因子为 `96`，平行板之间的细长导管也是如此。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Reynolds number vector for Darcy friction factor** — Darcy 摩擦因子查找表中每个断点处的 Reynolds 数 无量纲数值数组

Darcy 摩擦因子查找表中每个断点处的 Reynolds 数。该模块使用线性插值和最近邻外插来获得任意 Reynolds 数下的 Darcy 摩擦因子。

Reynolds 数必须大于零，并从左到右单调递增。它们可以跨越层流区、过渡区和湍流区。其数量必须等于 **Darcy friction factor vector** 参数的大小，与后者结合以构成完整的表格断点。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction factor vs. Reynolds number`。

### **Darcy friction factor vector** — Reynolds 数查找表中每个断点处的 Darcy 摩擦因子 无量纲数值数组

在 Reynolds 数查找表中每个断点处的 Darcy 摩擦因子。该模块使用线性插值和最近邻外插来获得任意 Reynolds 数下的 Darcy 摩擦因子。

Darcy 摩擦因子不得为负，并且必须按 Reynolds 数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Darcy friction factor** 参数的大小，与后者结合以构成完整的表格断点。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Darcy friction
factor vs. Reynolds number`。

### **Reynolds number vector for Euler number** — 欧拉数查找表中每个断点处的雷诺数 unitless numerical array

欧拉数查找表中每个断点处的雷诺数。该模块使用线性插值和最近邻外插来获得任意雷诺数下的欧拉数。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区。其数量必须等于 **Euler number vector** 参数的大小，并与该参数结合以完成表格化断点。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number
vs. Reynolds number`。

### **Euler number vector** — 雷诺数查找表中每个断点处的欧拉数 unitless numerical array

欧拉数在其基于雷诺数的查找表中每个断点处的值。该模块使用线性插值和最近邻外插来获得任意雷诺数下的欧拉数。

欧拉数不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Euler number** 参数的大小，并与该参数结合以完成表格化断点。

#### 依赖项

要启用此参数，请将 **Pressure loss model** 设置为 `Tabulated data - Euler number
vs. Reynolds number`。

### **Heat transfer coefficient model** — 流体与壁面之间传热的数学模型 `Constant heat transfer coefficient` (default) | `Correlation for flow inside tubes` | `Tabulated data - Colburn factor vs. Reynolds number` | `Tabulated data - Nusselt number vs. Reynolds number and Prandtl number`

流体与壁面之间传热的数学模型。模型的选择决定要应用哪些表达式以及要为传热计算指定哪些参数。有关按参数化进行的计算，请参见 E-NTU Heat Transfer 模块。

### **Heat transfer surface area** — 流体与壁面之间传热所使用的有效表面积 `0.4 m^2` (default) | scalar with units of length squared

流体与壁面之间传热所使用的有效表面积。有效表面积是主表面积和次表面积之和，即壁面暴露于流体的表面积，以及如果使用了翅片时的翅片表面积。翅片表面积通常按翅片效率因子缩放。

### **Liquid-wall heat transfer coefficient** — 流体与壁面之间对流的传热系数 `100 W/(K*m^2)` (default) | scalar

流体与壁面之间对流的传热系数。由污垢引起的阻力在 **Fouling factor** 参数中单独捕获。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Constant heat transfer
coefficient`。

### **Length of flow path for heat transfer** — 流体与壁面之间传热所经过的特征长度 `1 m` (default) | scalar with units of length

流体与壁面之间传热所经过的特征长度。此长度参与水力直径的计算，而传热系数和雷诺数（如表格化传热参数化中所定义）由水力直径导出。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor
vs. Reynolds number` 或 `Tabulated data
- Nusselt number vs. Reynolds number and Prandtl
number`。

### **Nusselt number for laminar flow heat transfer** — 层流中努塞尔数的假定常数 `3.66` (default) | positive unitless scalar

层流中努塞尔数的假定常数。努塞尔数参与流体与壁面之间传热系数的计算，而传热速率取决于该传热系数。默认值适用于圆柱形管道和管子。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow inside
tubes`。

### **Reynolds number vector for Colburn factor** — 用于指定 Colburn 因子数据的雷诺数值 unitless numerical array

Colburn 因子查找表中每个断点处的雷诺数。该模块使用线性插值和最近邻外插来获得任意雷诺数下的 Colburn 因子。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区。其数量必须等于 **Colburn factor vector** 参数的大小，并与该参数结合以完成表格化断点。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor
vs. Reynolds number`。

### **Colburn factor vector** — 雷诺数查找表中每个断点处的 Colburn 因子 unitless numerical array

Colburn 因子在其基于雷诺数的查找表中每个断点处的值。该模块使用线性插值和最近邻外插来获得任意雷诺数下的欧拉数。

Colburn 因子不得为负，并且必须按雷诺数递增的顺序从左到右排列。其数量必须等于 **Reynolds number vector for Colburn factor** 参数的大小，并与该参数结合以完成表格化断点。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Colburn factor
vs. Reynolds number`。

### **Reynolds number vector for Nusselt number** — 努塞尔数查找表中每个断点处的雷诺数 unitless numerical array

努塞尔数查找表中每个断点处的雷诺数。该表是二维的，雷诺数和普朗特数都作为独立坐标。该模块使用线性插值和最近邻外插来获得任意雷诺数下的努塞尔数。

雷诺数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区。向量的大小必须等于 **Nusselt number table** 参数的行数。如果表有 *m* 行和 *n* 列，则雷诺数向量必须为 *m* 个元素长。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number
vs. Reynolds number and Prandtl number`。

### **Prandtl number vector for Nusselt number** — 努塞尔数查找表中每个断点处的普朗特数 unitless numerical array

努塞尔数查找表中每个断点处的普朗特数。该表是二维的，雷诺数和普朗特数都作为独立坐标。该模块使用线性插值和最近邻外插来获得任意普朗特数下的努塞尔数。

普朗特数必须大于零，并且从左到右单调递增。它们可以跨越层流、过渡流和湍流区。向量的大小必须等于 **Nusselt number table** 参数的列数。如果表有 *m* 行和 *n* 列，则普朗特数向量必须为 *n* 个元素长。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number
vs. Reynolds number and Prandtl number`。

### **Nusselt number table, Nu (Re,Pr)** — 雷诺数和普朗特数查找表中每个断点处的努塞尔数 unitless numerical array

努塞尔数在其基于雷诺数和普朗特数的查找表中每个断点处的值。该模块使用线性插值和最近邻外插来获得任意雷诺数和普朗特数对下的努塞尔数。通过确定努塞尔数，该表为流体与壁面之间传热系数的计算提供输入。

努塞尔数必须大于零。它们必须按雷诺数递增的顺序从上到下排列，并按普朗特数递增的顺序从左到右排列。行数必须等于 **Reynolds number vector for Nusselt number** 参数的大小，列数必须等于 **Prandtl number vector for Nusselt number** 参数的大小。

#### 依赖项

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Tabulated data - Nusselt number
vs. Reynolds number and Prandtl number`。

### **Fouling factor** — 污垢沉积引起热阻的度量 `1e-4 K * m^2 / W` (default) | scalar with units of temperature over power

污垢沉积引起热阻的度量，这些沉积随时间倾向于在壁面的暴露表面上积聚。这些沉积在流体与壁面之间强加了一个新的固体层，热量必须穿过该层，从而为传热路径增加了额外的热阻。污垢沉积增长缓慢，因此其在仿真期间引起的阻力相应假定为常数。

### **Minimum liquid-wall heat transfer coefficient** — 传热系数的下界 `1 W/(m^2 * K)` (default) | scalar with units of power/area/temperature

流体与壁面之间传热系数的下界。如果计算返回更低的传热系数，则此下界将替换计算值。

### Effects and Initial Conditions

### **Enable Gas 1 dynamic compressibility** — 对气体通道中的压力动态建模的选项 `On` (default) | `Off`

对气体通道中的压力动态建模的选项。如果清除此复选框，则该模块从组件能量和质量守恒方程中移除压力导数项。

### **Gas 1 nominal temperature** — 标称工作条件下的温度 `293.15 K` (default) | scalar

标称工作条件下的气体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖项

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 nominal pressure** — 标称工作条件下的压力 `0.101325 MPa` (default) | scalar

标称工作条件下的气体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖项

要启用此参数，请清除 **Enable Gas 1 dynamic compressibility** 复选框。

### **Gas 1 initial temperature** — 仿真开始时气体通道中的温度 `293.15 K` (default) | scalar with units of temperature

仿真开始时气体通道中的温度

### **Gas 1 initial pressure** — 仿真开始时气体通道中的压力 `0.101325 MPa` (default) | scalar with units of pressure

仿真开始时气体通道中的压力。

#### 依赖项

要启用此参数，请选择 **Enable Gas 1 dynamic compressibility** 。

### **Enable Thermal Liquid 2 dynamic compressibility** — 对热液体通道中的压力动态建模的选项 `On` (default) | `Off`

对热液体通道中的压力动态建模的选项。如果清除此复选框，则该模块从组件能量和质量守恒方程中移除压力导数项。换热器内部的压力随后降为两个端口压力的加权平均值。

### **Thermal Liquid 2 nominal temperature** — 标称工作条件下的温度 `293.15 K` (default) | scalar

标称工作条件下的热液体温度。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖项

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 nominal pressure** — 标称工作条件下的压力 `0.101325 MPa` (default) | scalar

标称工作条件下的热液体压力。当动态可压缩性被禁用时，该模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖项

要启用此参数，请清除 **Enable Thermal Liquid 2 dynamic compressibility** 复选框。

### **Thermal Liquid 2 initial temperature** — 仿真开始时热液体通道中的温度 `293.15 K` (default) | scalar with units of temperature

仿真开始时热液体通道中的温度

### **Thermal Liquid 2 initial pressure** — 仿真开始时热液体通道中的压力 `0.101325 MPa` (default) | scalar with units of pressure

仿真开始时热液体通道中的压力。

#### 依赖项

要启用此参数，请选择 **Enable Thermal Liquid 2 dynamic compressibility** 。

## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2025a：可选地对动态可压缩性建模

Heat Exchanger (G-TL) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性建模。以前，此模块始终对压力动态建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

### R2024a：Heat Exchanger (G-TL) 模块仅对 E-NTU 建模选项建模

**Modeling option** 参数已移除，建模选项现在是两个单独的模块。Heat Exchanger (G-TL) 模块使用先前当 **Modeling option** 为 `E-NTU Model` 时所使用的传热模型。若要使用先前当 **Modeling option** 为 `Simple model` 时所用的模块模型，请参见 Specific Dissipation Heat Exchanger (G-TL) 模块。

## 描述

用于气体和热液体流动系统的换热器

Heat Exchanger (G-TL) 模块对短暂保持热接触的流体通过薄导热壁进行的互补冷却和加热建模。壁面能够在其边界内存储热量，从而为传热增加轻微的瞬态延迟，该延迟与其热质量成比例。流体为单相，一侧为纯气体，另一侧为纯液体。两种流体都不能相变，因此由于潜热永远不会释放，交换严格是显热交换。

显热换热器在机械中广泛存在。某些喷气式飞机中的燃油加热器通过将来自压缩机仍热的引气吹过燃油管路，防止冰在燃油管路中析出并堵塞燃油滤网。某些摩托车中的机油冷却器同样通过将环境温度的冲压空气吹过机油管路，防止润滑油过热。引气和冲压空气是气体流，燃油和机油是热液体流。

### Heat Transfer Model

该模块的 heat transfer model 源自 Effectiveness-NTU 方法。稳态下的传热随后以理想速率的一个分数进行；如果两股流动各自保持其入口温度，并且清除其间所有热阻，则理论上可支持该理想速率：

Q=ϵ QMax,

其中 *Q* 是实际传热速率，*Q*Max 是理想传热速率，*ε* 是在带有损失的真实换热器中实际观察到的理想速率分数。该分数是换热器效能，并且它是传热单元数（或 NTU）的函数；NTU 衡量热量在流动之间传递的容易程度相对于流动吸收该热量的容易程度：

NTU=1RCMin,

其中该分数是流动之间的总热导，*C*Min 是各流动热容率中的最小值，这些流动属于最不能吸收热量的流动。流动的热容率取决于流体的比热（*c*p）和其通过换热器的质量流率（m˙）：

C=cpm˙.

该效能还取决于流动的相对布置、它们之间的程数以及每侧的混合条件。这种依赖关系反映在所使用的效能表达式中，不同流动布置对应不同的表达式。有关效能表达式列表，请参见 E-NTU Heat Transfer 模块。

模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 流动布置

使用 **Flow arrangement** 模块参数设置这些流动在换热器中如何相遇。流动可以彼此平行、彼此逆向或彼此交叉。它们也可以在加压壳体中流动，一股通过封装在壳体内的管，另一股围绕这些相同的管。图中展示了一个示例。管内流动可以单程通过壳程流动（如右图所示），或者为了提高换热器效能，进行多程（如左图所示）。

其他流动布置可通过基于表格化效能数据的通用参数化实现，并且对换热器的细节要求很少。如果与换热器相关，流动布置、混合条件以及壳程或管程程数假定体现在表格化数据中。

### 混合条件

使用 **Cross flow arrangement** 参数来混合每一股流动、其中一股流动，或者不混合任何流动。此上下文中的混合是指流体在没有内部屏障的通道中的横向运动，这些屏障通常是导流板、折流板、翅片或壁面。这种运动用于消除横向平面中的温度变化。混合流动仅在纵向平面中具有变化的温度。未混合流动在横向和纵向平面中均具有变化的温度。图中展示了一个混合流动（**i**）和一个未混合流动（**ii**）。

混合流动与未混合流动之间的区别仅在交叉流布置中考虑。在那里，一种流体中的纵向温度变化会在第二种流体中产生横向温度变化，而混合可以消除这种变化。在逆流和平行流布置中，一种流体中的纵向温度变化会在第二种流体中产生纵向温度变化，而混合由于在此处影响很小而被忽略。

### 效能曲线

具有多程的壳管式换热器（图中 **iv.b**-**e** 分别对应 2、3 和 4 程）最有效。在单程换热器中，逆流（**ii**）最有效，平行流（**i**）最无效。

交叉流换热器的效能介于两者之间，混合条件起一定作用。当两股流动都未混合（**iii.a**）时最有效，当两股流动都混合（**iii.b**）时最无效。仅混合具有最小热容率的流动（**iii.c**）比仅混合具有最大热容率的流动（**iii.d**）更降低效能。

### 热阻

总热阻 *R* 是沿传热路径排列的局部热阻之和。局部热阻来自壁面表面的对流传热、通过壁面的传导，以及如果壁面两侧有污垢，通过污垢层的传导。按从气体侧（侧 1）到热液体侧（侧 2）的顺序表示：

R=1U1A1+F1A1+RW+F2A2+1U2A2,

其中 *U* 是对流传热系数，*F* 是污垢系数，*A* 是传热表面积，每个都对应下标所指示的流动。*R*W 是壁面的热阻。

壁面热阻和污垢系数是从模块参数获得的简单常数。传热系数是流体属性、流动几何和壁面摩擦的复杂函数，并源自 Reynolds、Nusselt 和 Prandtl 数之间的标准经验关联式。这些关联式取决于流动布置和混合条件，并且在 E-NTU Heat Transfer 模块中针对每种情况进行了详细说明，该模块模型基于此模块。

### 壁面热质量

如果选择 **Enable wall thermal mass**，模块会建模换热器壁面热质量，这会在壁面对温度或热流变化作出瞬态响应时引入延迟。如果建模热质量，壁面会在其边界内存储热量。这种热量存储会减慢稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续，直到来自两侧的热流率平衡为止。

如果选择 **Enable wall thermal mass**，壁面能量守恒为

(Mwallcp,wall2)dTwall1dt=−Q1−Q(Mwallcp,wall2)dTwall2dt=−Q2+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每侧的有效壁面温度。模块使用此值来建模瞬态响应。您无法测量此值。

对每种流体的传热为

Q1=C1(Twall1−Tin1)(1−e−NTU1)Q2=C2(Twall2−Tin2)(1−e−NTU2)

其中：

- *Tin* 是每侧的流体入口温度。
- *C* 是每种流体的热容率。

每侧流体与壁面之间的传热单元数为

NTU1=U1A1C1NTU2=U2A2C2

其中 *A* 是壁面表面积，*U* 是传热系数。

### 复合结构

该模块是由更简单的模块构建的复合组件。Heat Exchanger Interface (G) 模块建模气体流动，Heat Exchanger Interface (TL) 模块建模热液体流动，E-NTU Heat Transfer 模块建模流动之间跨壁面交换的热量。
