---
type: simulink-block
title: 'Condenser Evaporator (2P-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid - Moist Air'
documentation_page: 'condenserevaporator2pma'
documentation_source_path: 'ref/condenserevaporator2pma.html'
language: zh-CN
chinese_source: worker-translation
---

# Condenser Evaporator (2P-MA)

## 端口

### 守恒端口

### **A1** — 两相流体端口 两相流体

与两相流体相关的入口或出口端口。

### **B1** — 两相流体端口 两相流体

与两相流体相关的入口或出口端口。

### **A2** — 湿空气端口 湿空气

与湿空气相关的入口或出口端口。

### **B2** — 湿空气端口 湿空气

与湿空气相关的入口或出口端口。

### 输出

### **Z** — 两相流体区长度分数 物理信号

两相流体通道中区长度分数的三元素向量，以物理信号形式返回。该向量形式为 [L, M, V]，其中 L 为过冷液体，M 为液-汽混合物，V 为过热蒸汽。

### **W** — 湿空气冷凝速率 物理信号

离开湿空气流的水冷凝速率，以物理信号形式返回。该端口的值不包括以水滴形式夹带的冷凝部分。冷凝物不会积聚在传热表面上。

## 参数

### 配置

### **Flow arrangement** — 流路排列 `Cross flow`（默认）| `Parallel flow` | `Counter flow`

换热器两侧之间的流路排列。可用的流动排列为：

- `Parallel flow`。流动方向相同。
- `Counter flow`。流动彼此平行，方向相反。
- `Cross flow`。流动彼此垂直。

### **Cross flow arrangement** — 热混合条件 `Two-Phase Fluid 1 unmixed & Moist Air 2 mixed`（默认）| `Both fluids unmixed` | `Two-phase fluid 1 mixed & Moist Air 2 unmixed` | `Both fluids mixed`

选择每种流体是否可以在其通道中混合。混合流意味着流体在沿流路行进时可以自由地沿横向移动。非混合流意味着流体被限制为仅沿流路行进。例如，带有翅片的一侧被视为非混合流。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Cross flow`。

### **Wall thermal resistance** — 壁面通过热传导对热流的阻力 `0 K/W`（默认）| 正标量

分隔两种换热器流体的界面壁的热阻。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

两相流体端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

两相流体端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

湿空气侧端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动的面积 `0.01 m^2`（默认）| 正标量

湿空气侧端口 **B2** 处的流通面积。

### **Enable wall thermal mass** — 用于建模壁面热质量的选项 `off`（默认）| `on`

是否对换热器壁面热质量进行建模。对壁面热质量进行建模会在壁面对温度或热流变化做出瞬态响应时引入延迟。如果清除 **Enable wall thermal mass**，则该模块假设壁面足够薄，以至于在传热的时间尺度上瞬态响应是瞬时的。

### **Wall mass** — 换热器壁面质量 `1 kg`（默认）| 正标量

换热器壁面的质量。该模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 换热器壁面比热 `490 J/(K*kg)`（默认）| 正标量

换热器壁面的比热。该模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### 两相流体 1

### **Number of tubes** — 两相流体管数量 `25`（默认）| 正标量

两相流体管数量。

### **Total length of each tube** — 每根两相流体管的总长度 `1 m`（默认）| 正标量

每根两相流体管的总长度。

### **Tube cross section** — 管的横截面形状 `Circular`（默认）| `Rectangular` | `Annular` | `Generic`

管的横截面形状。使用 `Generic` 指定任意横截面几何形状。

此参数指定一根管的横截面。

### **Tube inner diameter** — 单根管的内径 `0.05 m`（默认）| 正标量

一根管横截面的内径。横截面和直径沿管均匀一致。直径的大小会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **Tube cross-section** 设置为 `Circular`。

### **Tube width** — 单根管的内部宽度 `0.05 m`（默认）| 正标量

一根管横截面的内部宽度。横截面和宽度沿管均匀一致。宽度和高度会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **Tube cross-section** 设置为 `Rectangular`。

### **Tube height** — 单根管的内部高度 `0.05 m`（默认）| 正标量

一根管的内部高度。横截面和高度沿管均匀一致。宽度和高度会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **Tube cross-section** 设置为 `Rectangular`。

### **Annulus inner diameter (heat transfer surface)** — 环形横截面的较小直径 `0.05 m`（默认）| 正标量

一根管环形横截面的较小直径。横截面和内径沿管均匀一致。内径会影响压力损失和传热计算。传热通过环形的内表面发生。

#### 依赖关系

要启用此参数，请将 **Tube cross-section** 设置为 `Annular`。

### **Annulus outer diameter** — 环形横截面的较大直径 `0.1 m`（默认）| 正标量

一根管环形横截面的较大直径。横截面和外径沿管均匀一致。外径会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **Tube cross-section** 设置为 `Annular`。

### **Cross-sectional area per tube** — 单根管中垂直于流动的内部面积 `0.002 m^2`（默认）| 正标量

每根管的内部流通面积。

#### 依赖关系

要启用此参数，请将 **Tube cross-section** 设置为 `Generic`。

### **Wetted perimeter of tube cross-section for pressure loss** — 流体接触的管横截面周长 `0.15 m`（默认）| 正标量

流体接触的管横截面周长。横截面和周长沿管均匀一致。此值应用于压力损失计算。

#### 依赖关系

要启用此参数，请将 **Tube cross-section** 设置为 `Generic`。

### **Perimeter of tube cross-section for heat transfer** — 用于传热计算的单根管周长 `0.15 m`（默认）| 正标量

用于传热计算的管周长。这通常与管周长相同，但在诸如环形横截面的情况下，根据传热表面的不同，这可能仅为内径或外径。横截面和管周长沿管均匀一致。

#### 依赖关系

要启用此参数，请将 **Tube cross-section** 设置为 `Generic`。

### **Pressure loss model** — 由粘性摩擦引起的压力损失计算方法 `Correlation for flow inside tubes`（默认）| `Pressure loss coefficient`

由粘性摩擦引起的压力损失计算方法。设置为：

- `Pressure loss coefficient`。使用此设置基于经验损失系数计算压力损失。
- `Correlation for flow inside tubes`。使用此设置基于管流关联式计算压力损失。

### **Pressure loss coefficient, delta\_p/(0.5\*rho\*v^2)** — 通道中所有压力损失的经验损失系数 `10`（默认）

通道中所有压力损失的经验损失系数。此值考虑了壁面摩擦以及通道中弯头、弯管和其他几何变化引起的局部损失。

损失系数可以从标称工况计算得出，或进行调整以拟合实验数据。损失系数定义为：

ξ=Δp12ρv2，

其中 *Δp* 为压降，*ρ* 为两相流体密度，*v* 为流速。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Pressure loss coefficient`。

### **Local resistance specification** — 量化压力损失的方法 `Aggregate equivalent length`（默认）| `Local loss coefficient`

在 Haaland 关联式中量化压力损失的方法。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Total local loss coefficient** — 压力损失系数 `0.1`（默认）| 正标量

系统上的局部压力损失系数。您可以使用此参数校准系统以匹配实验结果。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`，并将 **Local resistance specification** 设置为 `Local loss coefficient`。

### **Aggregate equivalent length of local resistances** — 每根管所有局部阻力的合计长度 `0.1 m`（默认）| 正标量

每根管所有局部阻力的合计长度。此值是指产生与管中因弯头、三通或接头等阻力引起的所有局部损失之和相同压力损失的管长度。合计长度越长，压力损失越大。该模块在计算摩擦引起的压力损失时，将此参数的值加到 **Total length of each tube** 参数中。

#### 依赖关系

要启用此参数，请将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`，并将 **Local resistance specification** 设置为 `Aggregate equivalent length`。

### **Internal surface absolute roughness** — 平均表面粗糙度高度 `15e-6 m`（默认）| 正标量

管表面缺陷的平均高度。对于使用 Haaland 关联式计算的压力损失，壁面越粗糙，湍流区中的压力损失越大。

#### 依赖关系

要启用此参数，请将以下任一设置为 `Correlation for flow inside tubes`：

- **Pressure loss model**
- **Heat transfer model**

### **Laminar flow upper Reynolds number limit** — 指示层流的最大雷诺数 `2000`（默认）| 正标量

指示层流的最大雷诺数。在此值与 **Turbulent flow lower Reynolds number** 之间，流动状态为过渡流。

### **Turbulent flow lower Reynolds number limit** — 指示湍流的最小雷诺数 `4000`（默认）| 正标量

指示湍流的最小雷诺数。在此值与 **Laminar flow upper Reynolds number limit** 之间，流动状态为过渡流。

### **Laminar friction constant for Darcy friction factor** — 层流中由粘性摩擦引起的压力损失系数 `64`（默认）| 正标量

层流中粘性摩擦压力损失方程中的系数。此参数也称为*形状因子*。默认值对应于圆形管横截面。

#### 依赖关系

要启用此参数，请将 **Tube cross section** 设置为 `Generic`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Heat transfer coefficient model** — 计算流体与壁面之间传热系数的方法 `Correlation for flow inside tubes`（默认）| `Colburn equation`

计算流体与壁面之间传热系数的方法。可用的设置为：

- `Colburn equation`。使用此设置以用户定义的变量 *a*、*b* 和 *c* 计算传热系数。在液相区和蒸汽区，传热系数基于 Colburn 方程。在液-汽混合物区，传热系数基于 Cavallini-Zecchin 方程。
- `Correlation for flow inside tubes`。使用此设置计算管流的传热系数。在液相区和蒸汽区，传热系数使用 Gnielinski 关联式计算。在液-汽混合物区，传热系数使用 Cavallini-Zecchin 方程计算。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in liquid zone** — 液相区中 Colburn 方程系数 `[.023, .8, .33]`（默认）| 正标量的三元素向量

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的努塞尔数，该模块使用 Colburn 方程对每个区进行计算。Colburn 方程的一般形式为：

Nu=aRebPrc。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone** — 混合物区中 Cavallini-Zecchin 方程系数 `[.05, .8, .33]`（默认）| 正标量的三元素向量

包含 Cavallini-Zecchin 方程经验系数的三元素向量。每个流体区具有不同的努塞尔数，该模块在混合物区使用 Cavallini-Zecchin 方程进行计算：

Nu=aReSLbPrSLc{[(ρSLρSV−1)xOut+1]1+b−[(ρSLρSV−1)xIn+1]1+b}(1+b)(ρSLρSV−1)(xOut−xIn)。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c in vapor zone** — 蒸汽区中 Colburn 方程系数 `[.023, .8, .33]`（默认）| 正标量的三元素向量

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的努塞尔数，该模块使用 Colburn 方程对每个区进行计算。Colburn 方程的一般形式为：

Nu=aRebPrc。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Colburn equation`。

### **Laminar flow Nusselt number** — 层流状态下对流传热与导热传热之比 `3.66`（默认）| 正标量

层流状态下对流传热与导热传热之比。流体努塞尔数影响传热速率，并取决于管横截面。

#### 依赖关系

要启用此参数，请将 **Heat transfer coefficient model** 设置为 `Correlation for flow inside tubes`。

### **Fouling factor** — 由污垢沉积物引起的附加热阻 `0.1 m^2*K/kW`（默认）| 正标量

由壁面表面上的污垢层引起的附加热阻。在实际系统中，污垢沉积物会随时间增长。然而，其增长足够缓慢，可以在仿真期间假定为常数。

### **Total fin surface area** — 所有翅片的总传热表面积 `0 m^2`（默认）| 正标量

接触两相流体的所有翅片两侧的总传热表面积。例如，如果翅片是矩形的，则表面积为矩形面积的两倍。

总传热表面积是通道表面积与有效翅片表面积之和，有效翅片表面积是 **Fin efficiency** 与 **Total fin surface area** 的乘积。

### **Fin efficiency** — 翅片实际传热速率与理想传热速率之比 `0.5`（默认）| 范围 [0,1] 内的正标量

如果整个翅片处于主传热表面温度时，通过接触两相流体的翅片的实际传热量与理想传热量之比。

### **Initial fluid energy specification** — 两相流体的初始状态 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

用于描述流体初始状态的量。

**Initial fluid energy specification** 参数的值限制了两相流体可用的初始状态。当 **Initial fluid energy specification** 为：

- `Temperature` — 指定初始状态为过冷液体或过热蒸汽。不能指定液-汽混合物，因为在液-汽混合物区域温度是恒定的。
- `Vapor quality` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液相质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液相质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。该模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。该模块不限制初始状态。

### **Initial two-phase fluid pressure** — 仿真开始时的流体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的流体压力。

### **Initial two-phase fluid temperature** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道中的温度。该参数可以是标量或二元素向量。标量值表示通道中的平均初始温度。向量值表示入口和出口处的初始温度，形式为 [`inlet`，`outlet`]。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Temperature`。

### **Initial two-phase fluid vapor quality** — 仿真开始时的蒸汽质量分数 `0.5`（默认）| 范围 [0,1] 内的正标量 | 二元素向量

仿真开始时两相流体通道中的蒸汽质量分数。该参数可以是标量或二元素向量。标量值表示通道中的平均初始蒸汽干度。向量值表示入口和出口处的初始蒸汽干度，形式为 [`inlet`，`outlet`]。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Vapor quality`。

### **Initial two-phase fluid vapor void fraction** — 仿真开始时的蒸汽体积分数 `0.5`（默认）| 范围 [0,1] 内的正标量 | 二元素向量

仿真开始时两相流体通道中的蒸汽体积分数。该参数可以是标量或二元素向量。标量值表示通道中的平均初始空隙率。向量值表示入口和出口处的初始空隙率，形式为 [`inlet`，`outlet`]。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Vapor void fraction`。

### **Initial two-phase fluid specific enthalpy** — 仿真开始时的单位质量焓 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道中的单位质量焓。该参数可以是标量或二元素向量。标量值表示通道中的平均初始比焓。向量值表示入口和出口处的初始比焓，形式为 [`inlet`，`outlet`]。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。

### **Initial two-phase fluid specific internal energy** — 仿真开始时的单位质量内能 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道中的单位质量内能。该参数可以是标量或二元素向量。标量值表示通道中的平均初始比内能。向量值表示入口和出口处的初始比内能，形式为 [`inlet`，`outlet`]。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖

要启用此参数，请将 **Initial fluid energy specification** 设置为 `Specific internal energy`。

### Moist Air 2

### **Flow geometry** — 湿空气流动配置 `Flow perpendicular to bank of circular tubes`（默认）| `Flow inside one or more tubes` | `Generic`

湿空气流动路径。流动可以在管束外部流过，也可以在单根管或多根管内部流动。还可以基于经验值指定通用参数化。

### **Number of tubes** — 湿空气管数量 `25`（默认）| 正标量

湿空气管数量。更多的管会因粘性摩擦导致更高的压力损失，但提供更大的传热表面积。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`。

### **Total length of each tube** — 每根湿空气管的总长度 `1 m`（默认）| 正标量

每根湿空气管的总长度。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`。

### **Tube cross section** — 管的横截面形状 `Circular`（默认）| `Rectangular` | `Annular` | `Generic`

单根管的横截面形状。设置为 `Generic` 以指定任意横截面几何形状。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`。

### **Tube inner diameter** — 单根管的内径 `0.05 m`（默认）| 正标量

单根管横截面的内径。横截面和直径沿管均匀一致。直径的大小影响压力损失和传热计算。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Circular`。

### **Tube width** — 单根管的内部宽度 `0.05 m`（默认）| 正标量

单根管横截面的内部宽度。横截面和宽度沿管均匀一致。宽度和高度影响压力损失和传热计算。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Rectangular`。

### **Tube height** — 单根管的内部高度 `0.05 m`（默认）| 正标量

单根管横截面的内部高度。横截面和高度沿管均匀一致。宽度和高度影响压力损失和传热计算。

#### 依赖

要启用此参数，请将 **Flow geometry** 参数化设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Rectangular`。

### **Annulus inner diameter (heat transfer surface)** — 环形横截面的较小直径 `0.05 m`（默认）| 正标量

单根管环形横截面的较小直径。横截面和内径沿管均匀一致。内径影响压力损失和传热计算。传热通过环形的内表面进行。

#### 依赖

要启用此参数，请将 **Flow geometry** 参数化设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Annular`。

### **Annulus outer diameter** — 环形横截面的较大直径 `0.1 m`（默认）| 正标量

单根管环形横截面的较大直径。横截面和外径沿管均匀一致。外径影响压力损失和传热计算。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Annular`。

### **Cross-sectional area per tube** — 每根管的内部流通面积 `0.002 m^2`（默认）| 正标量

每根管的内部流通面积。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Generic`。

### **Wetted perimeter of tube cross-section for pressure loss** — 流体接触的管横截面周长 `0.15 m`（默认）| 正标量

流体接触的管横截面周长。横截面和周长沿管均匀一致。该值应用于压力损失计算。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Generic`。

### **Perimeter of tube cross-section for heat transfer** — 用于传热计算的单根管周长 `0.15 m`（默认）| 正标量

用于传热计算的管周长。这通常与管周长相同，但在诸如环形横截面的情况下，根据传热表面的不同，这可能仅为内径或外径。横截面和管周长沿管均匀一致。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Generic`。

### **Pressure loss model** — 粘性摩擦引起的压力损失计算方法 `Correlation for flow inside tubes`（默认）| `Euler number per tube row` | `Pressure loss coefficient` | `Correlation for flow over tube bank`

粘性摩擦引起的压力损失计算方法。不同的流动配置可使用不同的模型。设置为：

- `Correlation for flow inside tubes`。使用此设置通过 Haaland 关联式计算压力损失。
- `Pressure loss coefficient`。使用此设置基于经验损失系数计算压力损失。
- `Euler number per tube row`。使用此设置基于经验 Euler 数计算压力损失。
- `Correlation for flow over tube bank`。使用此设置基于 Hagen 数计算压力损失。

可用的压力损失模型取决于 **Flow geometry** 设置。

#### 依赖

当 **Flow geometry** 设置为 `Flow inside one or more tubes` 时，**Pressure loss model** 可以设置为：

- `Pressure loss coefficient`。
- `Correlation for flow inside tubes`。

当 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，**Pressure loss model** 可以设置为：

- `Correlation for flow over tube bank`。
- `Euler number per tube row`。

当 **Flow geometry** 设置为 `Generic` 时，**Pressure loss model** 参数被禁用。压力损失通过 **Pressure loss coefficient, delta\_p/(0.5\*rho\*v^2)** 参数经验计算。

### **Pressure loss coefficient, delta\_p/(0.5\*rho\*v^2)** — 通道中所有压力损失的经验损失系数 `10`（默认）| 正标量

通道中所有压力损失的经验损失系数。该值考虑了壁面摩擦以及通道中弯头、弯管和其他几何变化引起的局部损失。

损失系数可以从额定工况计算得出，也可以通过调优来拟合实验数据。压力损失系数定义为：

ξ=Δp12ρv2，

其中 *Δp* 是压降，*ρ* 是两相流体密度，*v* 是流速。

#### 依赖

要启用此参数，请设置以下任一：

- **Flow geometry** 为 `Generic`。
- **Pressure loss model** 为 `Pressure loss coefficient`。

### **Local resistance specification** — 量化压力损失的方法 `Aggregate equivalent length`（默认）| `Local loss coefficient`

在 Haaland 关联式中量化压力损失的方法。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Total local loss coefficient** — 压力损失系数 `0.1`（默认）| 正标量

系统上的局部压力损失系数。可以使用此参数来校准系统以匹配实验结果。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`，并将 **Local resistance specification** 设置为 `Local loss coefficient`。

### **Aggregate equivalent length of local resistances** — 每根管所有局部阻力的合计长度 `0.1 m`（默认）| 正标量

每根管所有局部阻力的合计长度。该值是产生与管中所有局部损失（如弯头、三通或接头引起的阻力）之和相同压力损失的管长。合计长度越长，压力损失越大。该模块在计算摩擦引起的压力损失时，将此参数的值加到 **Total length of each tube** 参数中。

#### 依赖

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Pressure loss model** 设置为 `Correlations for flow inside tubes`，并将 **Local resistance specification** 设置为 `Aggregate equivalent length`。

### **Internal surface absolute roughness** — 平均表面粗糙度高度 `15e-6 m`（默认）| 正标量

管表面缺陷的平均高度。在湍流区域，对于使用 Haaland 关联式计算的压力损失，更粗糙的壁面会导致更大的压力损失。

#### 依赖

要启用此参数，请设置以下任一：

- **Pressure loss model**
- **Heat transfer coefficient model**

为 `Correlation for flow inside tubes`。

### **Laminar flow upper Reynolds number limit** — 指示层流的最大 Reynolds 数 `2000`（默认）| 正标量

指示层流的最大 Reynolds 数。在该值与 **Turbulent flow lower Reynolds number limit** 之间，流动状态为过渡流。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Turbulent flow lower Reynolds number limit** — 指示湍流的最小雷诺数 `4000`（默认）| 正标量

指示湍流的最小雷诺数。在此值与 **Laminar flow upper Reynolds number limit** 之间，流态为层流与湍流之间的过渡流态。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流中粘性摩擦导致压力损失的系数 `64`（默认）| 正标量

层流中粘性摩擦压力损失方程中的系数。此参数也称为*形状因子*。默认值对应于圆形管横截面。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Correlation for flow inside tubes`，将 **Tube cross section** 设置为 `Generic`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Heat transfer coefficient model** — 计算流体与壁面之间传热系数的方法 `Correlation for flow over tube bank`（默认）| `Colburn equation` | `Correlation for flow inside tubes`

计算流体与壁面之间传热系数的方法。可用的设置包括：

- `Colburn equation`。使用此设置可通过用户定义的 Colburn 方程变量 *a*、*b* 和 *c* 计算传热系数。
- `Correlation for flow over tube bank`。使用此设置可基于管束关联式使用 Hagen 数计算传热系数。
- `Correlation for flow inside tubes`。使用此设置可通过 Gnielinski 关联式计算管道流动的传热系数。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为以下之一：

- `Flow perpendicular to bank of circular tubes`。
- `Flow inside one or more tubes`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c** — Colburn 方程系数 `[0.023, 0.8, 0.33]`（默认）| 三元素向量

包含 Colburn 方程经验系数的三元素向量。Colburn 方程是计算 Nusselt 数的公式。Colburn 方程的一般形式为：

Nu=aRebPrc。

当 **Heat transfer coefficient model** 设置为 **Colburn equation** 且 **Flow geometry** 设置为 `Flow inside one or more tubes`，或者 **Flow geometry** 设置为 `Generic` 时，默认的 Colburn 方程为：

Nu=0.023Re0.8Pr1/3。

当 **Heat transfer coefficient model** 设置为 **Colburn equation** 且 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，默认的 Colburn 方程为：

Nu=0.27Re0.63Pr0.36。

#### 依赖关系

要启用此参数，请设置：

1. **Flow geometry** 为以下之一：

   - `Flow inside one or more tubes`
   - `Flow perpendicular to bank of circular tubes`

   并将 **Heat transfer coefficient model** 设置为 `Colburn equation`。
2. **Flow geometry** 设置为 `Generic`。

### **Laminar flow Nusselt number** — 层流流态中对流与导热传热之比 `3.66`（默认）| 正标量

层流流态中对流与导热传热之比。流体 Nusselt 数影响传热速率，并取决于管横截面。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Tube cross-section** 设置为 `Generic`，并将 **Heat transfer parameterization** 设置为 `Correlation for flow inside tubes`。

### **Tube bank grid arrangement** — 管束中管排的几何布置 `Inline`（默认）| `Staggered`

管束中管子的排列方式。管排要么与其相邻管排对齐，要么交错排列。

- `Inline`：所有管排直接位于彼此后方。
- `Staggered`：一个管排的管子位于前一管排管子的间隙处。

管子排列方式影响 Nusselt 数和传热速率。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Number of tube rows along flow direction** — 管束中的管排数 `5`（默认）| 正标量

管束中两相流体管排的数量。这些管排与湿空气流方向对齐。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Number of tube segments in each tube row** — 管束每一排中两相流体管子的数量 `5`（默认）| 正标量

管束每一排中两相流体管子的数量。该测量方向垂直于湿空气流。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Length of each tube segment in a tube row** — 每根两相流体管子的长度 `1 m`（默认）| 正标量

跨越一个管排的每根两相流体管子的长度。管束中的所有管子长度相同。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Tube outer diameter** — 单根两相流体管子的外径 `0.05 m`（默认）| 正标量

两相流体管子的外径。横截面沿管子均匀，因此直径在整个管子中恒定。该值影响由于粘性摩擦而导致的横掠管束流动中的损失。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Longitudinal tube pitch (along flow direction)** — 两相流体管排之间的中心到中心距离 `0.15 m`（默认）| 正标量

两相流体管子的管中心之间的距离，与湿空气流动方向对齐。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Transverse tube pitch (perpendicular to flow direction)** — 一排中两相流体管子之间的中心到中心距离 `0.15 m`（默认）| 正标量

一排两相流体管子中管中心之间的距离。该测量方向垂直于湿空气流动方向。有关更多信息，请参见 Heat Transfer Coefficient for Flows Across a Tube Bank。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Euler number per tube row, delta\_p/(N\*0.5\*rho\*v^2)** — 管束每一排的 Euler 数 `10`（默认）| 正标量

单排管子压降的经验系数。Euler 数是压降与流体动量之比：

Eu=ΔpN12ρv2，

其中 *N* 是 **Number of tube rows along flow direction**，*Δp* 是压降，*ρ* 是湿空气混合物密度，*v* 是流速。

每个管排位于垂直于湿空气流的平面内。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`，并将 **Pressure loss model** 设置为 `Euler number per tube row`。

### **Minimum free-flow area** — 入口与出口之间的最小总流通面积 `0.01 m^2`（默认）| 正标量

入口与出口之间的最小总横截流通面积。如果通道是管道、管子、狭槽或凹槽的集合，则此参数的值是最小流通面积点处最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是在一个横截面中管子之间间隙之和最小的那些间隙之和。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Generic`。

### **Heat transfer surface area without fins** — 不包括翅片的传热表面总面积 `2 m^2`（默认）| 正标量

传热表面的总面积，不包括翅片。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Generic`。

### **Moist air volume inside heat exchanger** — 换热器内湿空气的总体积 `0.05 m^3`（默认）| 正标量

换热器内湿空气的总体积。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Generic`。

### **Fouling factor** — 由于污垢沉积物导致的附加热阻 `0.1 m^2*K/kW`（默认）| 正标量

由于壁面表面上的污垢层导致的附加热阻。在实际系统中，污垢沉积物会随时间增长。然而，其增长足够缓慢，可以在仿真期间假定为恒定。

### **Total fin surface area** — 所有翅片的传热表面总面积 `0 m^2`（默认）| 正标量

与湿空气接触的所有翅片两侧的传热表面总面积。例如，如果翅片是矩形的，则表面积为矩形面积的两倍。

总传热表面积是通道表面积与有效翅片表面积之和，有效翅片表面积是 **Fin efficiency** 与 **Total fin surface area** 的乘积。

### **Fin efficiency** — 翅片实际传热速率与理想传热速率之比 `0.5`（默认）| 范围 [0,1] 内的正标量

如果整个翅片都处于主传热表面温度，则与湿空气接触的翅片的实际传热与理想传热之比。

### **Initial moist air pressure** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的湿空气压力。

### **Initial moist air temperature** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时湿空气流体通道中的温度。此参数可以是标量或二元素向量。标量值表示通道中的平均初始温度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始温度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

### **Initial humidity specification** — 湿度规格 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

湿空气侧的初始湿度规格。

### **Initial moist air relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| 范围 [0,1] 内的正标量 | 二元素向量

仿真开始时湿空气通道中的相对湿度。相对湿度是水蒸气分压与水蒸气饱和压力之比，或者水蒸气摩尔分数与饱和时水蒸气摩尔分数之比。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始相对湿度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始相对湿度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial moist air specific humidity** — 仿真开始时的比湿度 `0.01`（默认）| 范围 [0,1] 内的正标量 | 二元素向量

仿真开始时湿空气通道中的比湿度。比湿度是水蒸气质量与水蒸气、示踪气体和干空气总质量之比。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始比湿度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始比湿度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial moist air water vapor mole fraction** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| 范围 [0,1] 内的正标量 | 二元素向量

仿真开始时湿空气通道中水蒸气的摩尔分数。水蒸气摩尔分数是相对于水蒸气、示踪物质和干空气的总摩尔量而言的。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始蒸气摩尔分数。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始蒸气摩尔分数。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial moist air humidity ratio** — 仿真开始时的湿度比 `0.01`（默认）| 范围 [0,1] 内的正标量 | 二元素向量

仿真开始时湿空气通道中的湿度比。湿度比是水蒸气质量与干空气和示踪气体质量之比。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始湿度比。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始湿度比。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial moist air wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| 范围 [0,1] 内的正标量

仿真开始时的湿球温度。该模块使用此值计算湿度。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始湿球温度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始湿球温度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial trace gas specification** — 示踪气体的测量类型 `Mass fraction`（默认）| `Mole fraction`

示踪气体的测量类型。

### **Initial moist air trace gas mass fraction** — 湿空气通道中痕量气体的量 `0.001`（默认值）| [0,1] 范围内的正标量 | 双元素向量

仿真开始时湿空气通道中痕量气体的质量分数。质量分数是相对于水蒸气、痕量气体和干空气的总质量而言的。

此参数可以是标量或双元素向量。标量值表示通道中痕量气体的平均质量分数。向量值以 [`inlet`, `outlet`] 的形式表示入口和出口处的初始痕量气体质量分数。模块在两个端口之间计算线性梯度。入口和出口端口根据初始流动方向确定。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial moist air trace gas mole fraction** — 仿真开始时痕量气体的摩尔分数 `0.001`（默认值）| [0,1] 范围内的正标量 | 双元素向量

仿真开始时湿空气通道中痕量气体的摩尔分数。摩尔分数是相对于水蒸气、痕量气体和干空气的总摩尔量而言的。

此参数可以是标量或双元素向量。标量值表示通道中痕量气体的平均摩尔分数。向量值以 [`inlet`, `outlet`] 的形式表示入口和出口处的初始痕量气体摩尔分数。模块在两个端口之间计算线性梯度。入口和出口端口根据初始流动方向确定。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气的质量比 `0`（默认值）| 正标量

水滴与湿空气的初始质量比。

### **Relative humidity at saturation** — 凝结的相对湿度点 `1`（默认值）| [0,1] 范围内的正标量

凝结的相对湿度点。高于此值时发生凝结。大于 1 的值表示过饱和蒸汽。

### **Water vapor condensation time constant** — 凝结的时间尺度 `1e-3 s`（默认值）| 正标量

过饱和湿空气体积通过凝结多余水分恢复到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发的时间尺度 `1e-3 s`（默认值）| 正标量

水滴蒸发为蒸汽的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 水滴中凝结物的比例 `1`（默认值）| [0,1] 范围内的标量

湿空气中被夹带为水滴的凝结物比例。

## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Moist Air

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2025a: 换热器壁面的热质量建模

选择 **Wall thermal dynamics** 以对换热器壁面的热质量进行建模。

### R2024b: 对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

### R2024a: 自由流通面积计算的更新

当 **Flow geometry** 为 `Flow perpendicular to bank of circular tubes` 时，模块现在使用不同的方法计算自由流通面积。如果 **Number of tube segments in each tube row** 参数的值较小，模块可能会显示压力损失和传热略有增加。

### R2024a: 新增湿度指定选项

模块为 **Initial humidity specification** 参数新增了一个选项。此选项称为 `Wet-bulb temperature`，允许您以湿球温度的形式输入数据。

### R2023a: 使用局部损失系数对附加压力损失进行建模

将 **Local resistance specification** 参数设置为 `Local loss coefficient` 以指定量化压力损失的新方法。此选项允许您对超出管道长度所致损失之外的附加摩擦损失进行建模。

## 描述

湿空气与两相流体网络之间的换热器

Condenser Evaporator (2P-MA) 模块对具有一个湿空气网络和一个两相流体网络的换热器进行建模，湿空气网络在端口 **A2** 和 **B2** 之间流动，两相流体网络在端口 **A1** 和 **B1** 之间流动。该换热器可以用作冷凝器或蒸发器。流体流可以布置为平行流、逆流或交叉流配置。

**制冷应用换热器示例**

您可以将湿空气侧建模为管内流动、绕两相流体管流动，或通过经验性通用参数化进行建模。湿空气侧包含空气、痕量气体和水蒸气，这些水蒸气在整个换热循环中可能发生凝结。模块模型考虑了从空气到液态水凝结层的能量传递。该液体层不会积聚在换热表面上，并假定其完全从下游湿空气流中移除。湿度凝结速率作为物理信号在端口 **W** 返回。

模块使用效能-NTU (E-NTU) 方法对通过共享壁面的传热进行建模。换热器壁面上的污垢会增加热阻并减少两种流体之间的热交换，模块也对其进行了建模。您还可以选择性地对湿空气侧和两相流体侧的翅片进行建模。换热器两侧由粘性摩擦引起的压力损失可以通过解析方法或通用参数化进行建模，您可以使用后者根据自身数据进行调整。

您可以将两相流体侧建模为管内流动或管束内流动。两相流体管使用边界跟随模型来跟踪三个区域中的过冷液体 (L)、气液混合物 (M) 和过热蒸汽 (V)。某个区域在系统中所占的相对空间量称为系统中的*区域长度分数*。

**两相流体管道中的区域长度分数**

两相流体管道中各区域长度分数之和等于 `1`。端口 **Z** 将区域长度分数作为物理信号向量返回，分别对应三个相：[L, M, V]。

### 换热器配置

换热器效能基于所选的换热器配置、各相中的流体属性、换热器各侧的管几何形状和流动配置，以及翅片的使用和尺寸。

**流动布置**

**Flow arrangement** 参数指定两侧之间的相对流动路径：

- `Parallel flow` 表示流体沿相同方向流动。
- `Counter flow` 表示流体平行但沿相反方向流动。
- `Cross flow` 表示流体沿彼此垂直的方向流动。

**热混合**

当 **Flow arrangement** 设置为 `Cross flow` 时，使用 **Cross flow arrangement** 参数来指示两相流体或湿空气流是否被折流板或壁面分隔为多条路径。如果没有这些分隔，流体可以自由混合，被视为*混合*。在交叉流布置中，两种流体、一种流体或两种流体都可以是混合的。混合使流体温度沿第二流体的流动方向均匀化，并沿垂直于第二流体流动的方向变化。

非混合流的温度沿第二流体的流动路径和垂直于流动路径的方向均发生变化。

**交叉流配置示例**

请注意，仿真期间的流动方向不影响所选的流动布置设置。模块上的端口不反映物理换热系统中端口的物理位置。

所有流动布置均为单程，这意味着流体在换热器中不会多次折返以增加传热点。要对多程换热器进行建模，您可以将多个 Condenser Evaporator (2P-MA) 模块串联或并联布置。

例如，要在两相流体侧实现双程配置并在湿空气侧实现单程配置，您可以将两相流体侧串联连接，并将湿空气侧并联连接到同一输入（例如两个各占总质量流量一半的 Mass Flow Rate Source 模块），如下所示。

**流动几何形状**

**Flow geometry** 参数将湿空气流动布置设置为管内或管束内流动，或垂直于管束的流动。您还可以指定经验性通用配置。两相流体始终在管内或管束内流动。

当 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，使用 **Tube bank grid arrangement** 参数将两相流体管束排列定义为 `Inline` 或 `Staggered`。红色向下箭头表示湿空气流动方向。Inline 图中还标出了 **Number of tube rows along flow direction** 和 **Number of tube segments in each tube row** 参数。此处，*流动方向*指湿空气流动方向，*管*指两相流体管道。**Length of each tube segment in a tube row** 参数在 Staggered 图中标出。

**翅片**

当 **Total fin surface area** 参数为 `0 m^2` 时，换热器配置没有翅片。翅片引入额外的换热表面积。每个流体侧有单独的翅片面积和描述该流体中翅片的参数。例如，当两相流体在管内流动而湿空气在管外流动时，**Two-Phase Fluid 1** 部分中的 **Total fin surface area** 和 **Fin efficiency** 参数描述伸入管内的翅片。**Moist Air 2** 部分中的 **Total fin surface area** 和 **Fin efficiency** 参数描述管外的翅片。

### 效能-NTU 传热

传热速率针对每个流体相进行计算。根据换热器两相流体侧出现的三个流体区域，传热速率分三个部分计算。

区域中的对流传热为

Qzone=ϵCMin(TIn,2P−TIn,MA),

其中：

- *C*Min 是该区域中两种流体热容率的较小值。热容率是流体比热 *c*p 与流体质量流量的乘积。*C*Min 始终为正。
- *TIn,2P* 是两相流体的区域入口温度。
- *TIn,MA* 是湿空气的区域入口温度。
- *ε* 是换热器效能。

效能是热容率和传热单元数 *NTU* 的函数，并且还随换热器流动布置而变化，这将在按流动布置的效能中更详细地讨论。*NTU* 计算如下：

NTU=zCMinR,

其中：

- *z* 是各个区域长度分数。
- *R* 是两种流体之间的总热阻，由对流、传导以及管壁上的任何污垢引起。

  R=1U2PATh,2P+F2PATh,2P+RW+FMAATh,MA+1UMAATh,MA,

  其中：

  - *U* 是相应流体的对流换热系数。该系数将在两相流体关联式和湿空气关联式中更详细地讨论。
  - *F* 分别是两相流体侧或湿空气侧的 **Fouling factor** 参数值。
  - *RW* 是 **Thermal resistance through heat transfer surface** 参数的值。
  - *A*Th 是换热器相应侧的换热表面积。*A*Th 是壁面表面积 *AW* 和 **Total fin surface area** *AF* 之和：

    ATh=AW+ηFAF,

    其中 *ηF* 是 **Fin efficiency**。

流体之间的总对流传热速率是三个区域中过冷液体 (*QL*)、气液混合物 (*QM*) 和过热蒸汽 (*QV*) 传热量之和：

Q=∑QZ=QL+QM+QV.

模块在传热计算中使用的流体属性是入口值与流体体积中值的平均值。

**按流动布置的效能**

换热器效能随其流动配置和每种流体中的混合情况而变化。以下是每种配置在液体和蒸汽区域中计算的效能公式。在混合物区域中，所有配置的效能均为 ε=1−exp(−NTU)。

- 当 **Flow arrangement** 设置为 `Parallel flow` 时：

  ϵ=1−exp[−NTU(1+CR)]1+CR
- 当 **Flow arrangement** 设置为 `Counter flow` 时：

  ϵ=1−exp[−NTU(1−CR)]1−CRexp[−NTU(1−CR)]
- 当 **Flow arrangement** 设置为 `Cross flow` 且 **Cross flow arrangement** 设置为 `Both fluids unmixed` 时：

  ϵ=1−exp{NTU0.22CR[exp(−CRNTU0.78)−1]}
- 当 **Flow arrangement** 设置为 `Cross flow` 且 **Cross flow arrangement** 设置为 `Both fluids mixed` 时：

  ϵ=[11−exp(−NTU)+CR1−exp(−CRNTU)−1NTU]−1

当一种流体混合而另一种不混合时，效能方程取决于流体的相对热容率。当 **Flow arrangement** 设置为 `Cross flow` 且 **Cross flow arrangement** 设置为 `Two-Phase Fluid 1 mixed & Moist Air 2 unmixed` 或 `Two-Phase Fluid 1 unmixed & Moist Air 2 mixed` 时：

- 当 Cmax 的流体混合而 Cmin 的流体不混合时：

  ϵ=1CR(1−exp{−CR{1−exp(−NTU)}})
- 当 Cmin 的流体混合而 Cmax 的流体不混合时：

  ϵ=1−exp{−1CR[1−exp(−CRNTU)]}

*CR* 表示两种流体热容率之比：

CR=CMinCMax.

### 传导传热

区域中的传导传热为

Qcond=Tout,2P−Tout,MARcond,

其中：

- *Tout,2P* 是两相流体的区域出口温度。
- *Tout,MA* 是湿空气的区域出口温度。
- *Rcond* 是两种流体之间的总传导热阻，

  Rcond=Dhk2PAW,2P+F2PAW,2P+RW+FMAAW,MA+DhkMAAW,MA,

  其中：

  - *AW* 是壁面表面积。
  - *k* 是每种流体的导热系数。
  - *DH* 是水力直径。

总传热量是对流传热和传导传热之和。与对流传热相比，传导传热可以忽略不计。当流量为零时，对流传热也为零。然而，由于对流传热和传导传热彼此独立运行，即使对流传热为零，仍然存在传导传热。

### 冷凝

在湿空气侧，换热表面可能形成一层冷凝水。该液层会影响湿空气与两相流体之间的换热量。上述 E-NTU 传热方程是针对*干*传热给出的。为修正冷凝的影响，额外使用下面列出的湿参数计算 E-NTU 方程。两种计算得到的传热速率中，导致湿空气侧冷却量更大的那个用于传热计算 [1][2]。使用此方法时，假定 Lewis 数接近 1，这对于湿空气是成立的 [1][2]。

**用于传热速率计算的 E-NTU 量**

|  | 干计算 | 湿计算 |
| --- | --- | --- |
| 湿空气区域入口温度 | *Tin,MA* | *Tin,wb,MA* |
| 热容率 | m˙¯MAc¯p,MA | m˙¯MAc¯eq,MA |
| 传热系数 | *UMA* | UMAc¯eq,MAc¯p,MA |

其中：

- *Tin,MA* 是湿空气区域入口温度。
- *Tin,wb,MA* 是与 *Tin,MA* 相关的湿空气湿球温度。
- m˙¯MA 是干空气质量流量。
- c¯p,MA 是单位干空气质量的湿空气热容。
- c¯eq,MA 是等效热容。*等效热容*是饱和湿空气条件下湿空气比焓（每单位干空气）h¯MA 随温度的变化：

  c¯eq,MA=(∂h¯MA∂TMA)s。

离开湿空气质量流量的冷凝水蒸气质量流量取决于湿空气入口与通道壁之间的相对湿度以及换热器 NTU：

m˙cond=−m˙¯MA(Wwall,MA−Win,MA)(1−e−NTUMA)，

其中：

- *W*wall,MA 是换热表面处的湿度比。
- *W*in,MA 是湿空气流入口处的湿度比。
- *NTU*MA 是湿空气侧的传热单元数，计算为：

  NTUMA=UMAc¯eq,MAc¯p,MAATh,MAm˙¯MAc¯eq,MA。

与水蒸气冷凝相关的能量流基于水蒸气的比焓 *h*water, wall 与汽化比焓 *h*fg 之间的差值：

ϕCond=m˙cond(hwater,wall−hfg)。

假定冷凝液不在换热表面上积聚，并且不影响诸如管径之类的几何参数。假定冷凝水完全从下游湿空气流中移除。

### 两相流体关联式

**传热系数**

对流换热系数根据流体 Nusselt 数变化：

U=NukDH，

其中：

- *Nu* 是区域平均 Nusselt 数，取决于流态。
- *k* 是流体相热导率。
- *DH* 是管水力直径。

对于过冷液体或过热蒸气区域中的湍流，Nusselt 数使用 Gnielinski 关联式计算：

Nu=fD8(Re−1000)Pr1+12.7f8(Pr2/3−1)，

其中：

- *Re* 是流体 Reynolds 数。
- *Pr* 是流体 Prandtl 数。

对于液-汽混合物区域中的湍流，Nusselt 数使用 Cavallini-Zecchin 关联式计算：

Nu=aReSLbPrSLc{[(ρSLρSV−1)xOut+1]1+b−[(ρSLρSV−1)xIn+1]1+b}(1+b)(ρSLρSV−1)(xOut−xIn)。

其中：

- *Re*SL 是饱和液体的 Reynolds 数。
- *Pr*SL 是饱和液体的 Prandtl 数。
- *ρ*SL 是饱和液体的密度。
- *ρ*SV 是饱和蒸气的密度。
- *a*= 0.05，*b* = 0.8，*c*= 0.33。

对于层流，Nusselt 数由 **Laminar flow Nusselt number** 参数设置。

对于过渡流，Nusselt 数是层流和湍流 Nusselt 数之间的混合值。

**经验 Nusselt 数公式**

当 **Heat transfer coefficient model** 参数为 `Colburn equation` 时，模块使用经验 Colburn 方程计算过冷液体和过热蒸气区域的 Nusselt 数

Nu=aRebPrc，

其中 *a*、*b* 和 *c* 是 **Coefficients [a, b, c] for a\*Re^b\*Pr^c in liquid zone** 和 **Coefficients [a, b, c] for a\*Re^b\*Pr^c in vapor zone** 参数中的值。

模块使用 Cavallini-Zecchin 方程计算液-汽混合物区域的 Nusselt 数，其中变量位于 **Coefficients [a, b, c] for a\*Re^b\*Pr^c in mixture zone** 参数中。

**压力损失**

由粘性摩擦引起的压力损失随流态和配置而变化。压力损失计算使用总密度，即流体总质量除以流体总体积。当 **Pressure loss model** 参数为 `Correlation for flow inside tubes` 时，摩擦引起的压力损失取决于 Darcy 摩擦因子。

对于湍流，当 Reynolds 数高于 **Turbulent flow lower Reynolds number limit** 参数时，模块根据计算得到的 Darcy 摩擦因子计算摩擦引起的压力损失。端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=fD,Am˙A1|m˙A1|2ρDHACS2(L+LAdd2)，

其中：

- m˙A1 是通过端口 **A1** 的总流量。
- *fD,A* 是根据 Haaland 关联式得到的 Darcy 摩擦因子。当 **Local resistance specification** 参数为 `Aggregate equivalent length` 时，

  fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2，

  其中 *ε*R 是 **Internal surface absolute roughness** 参数的值。摩擦因子取决于 Reynolds 数，模块对每种液体在两个端口处计算该值。
- *L* 是 **Total length of each tube** 参数的值。
- *L*Add 是 **Aggregate equivalent length of local resistances** 参数的值，即一根管的等效长度，该管引入的损失与管中其他局部阻力损失之和相同。
- *ACS* 是管横截面积。

端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=fD,Bm˙B1|m˙B1|2ρDHACS2(L+LAdd2)，

其中 m˙B1 是通过端口 **B1** 的总流量。

当 **Local resistance specification** 参数为 `Aggregate equivalent length` 时，端口 **B1** 处的 Darcy 摩擦因子为：

fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2。

当 **Local resistance specification** 参数为 `Local loss coefficient` 时，端口 **A1** 和 **B1** 处的 Darcy 摩擦因子为

fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)

其中 *Clocalloss* 是 **Total local loss coefficient** 参数的值。

对于层流，当 Reynolds 数低于 **Laminar flow upper Reynolds number limit** 参数时，模块根据 **Laminar friction constant for Darcy friction factor** 参数 *λ* 计算摩擦引起的压力损失。当 **Tube cross-section** 为 `Generic` 时，*λ* 是用户定义参数。否则，模块在内部计算该值。端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=λμm˙A12ρDH2ACS(L+LAdd2)，

其中 *μ* 是流体动力粘度。端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=λμm˙B12ρDH2ACS(L+LAdd2)。

对于过渡流，粘性摩擦引起的压差是层流和湍流压力损失值之间的平滑混合。

**经验压力损失公式**

当 **Pressure loss model** 设置为 `Pressure loss coefficient` 时，粘性摩擦引起的压力损失使用经验压力损失系数 *ξ* 计算。

端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=12ξm˙A1|m˙A1|2ρACS2。

端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=12ξm˙B1|m˙B1|2ρACS2。

### 湿空气关联式

**一根或多根管内流动的传热系数**

当湿空气 **Flow geometry** 设置为 `Flow inside one or more tubes` 时，Nusselt 数按照 Gnielinski 关联式计算，方式与两相过冷液体或过热蒸气相同。更多信息请参见传热系数。

**横掠管束流动的传热系数**

当湿空气 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，Nusselt 数基于 Hagen 数 Hg 计算，并取决于 **Tube bank grid arrangement** 设置：

Nu={0.404Lq1/3(Re+1Re+1000)0.1,Inline0.404Lq1/3,Staggered

其中：

Lq={1.18Pr(4lT/π−DlL)Hg(Re),Inline0.92Pr(4lT/π−DlD)Hg(Re),Staggered with lL≥D0.92Pr(4lTlL/π−D2lLlD)Hg(Re),Staggered with lL<D

- *D* 是 **Tube outer diameter**。
- *l*L 是 **Longitudinal tube pitch (along flow direction)**，即沿流动方向的管中心之间的距离。*流动方向*指湿空气流动。
- *l*T 是 **Transverse tube pitch (perpendicular to flow direction)**，如下图所示。横向间距是一排中两相流体管中心之间的距离。
- *l*D 是对角管间距，计算为 lD=(lT2)2+lL2。

有关计算 Hagen 数的更多信息，请参见 [6]。

两种管束网格排列类型的纵向和横向间距相同。

**带间距测量的两相流体管横截面**

**经验 Nusselt 数公式**

当 **Heat transfer coefficient model** 设置为 `Colburn equation` 或 **Flow geometry** 设置为 `Generic` 时，Nusselt 数由经验 Colburn 方程计算：

Nu=aRebPrc，

其中 *a*、*b* 和 *c* 是 **Coefficients [a, b, c] for a\*Re^b\*Pr^c** 参数中定义的值。

**管内流动的压力损失**

当湿空气 **Flow geometry** 设置为 `Flow inside one or more tubes` 时，压力损失的计算方式与两相流相同，使用湿空气侧各自的 Darcy 摩擦因子、密度、质量流量和管长。更多信息请参见压力损失。

**横掠管束流动的压力损失**

当湿空气 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，Hagen 数用于计算粘性摩擦引起的压力损失。端口 **A2** 与内部节点 I2 之间的压差为：

pA2−pI2=12μ2NRρD2Hg(Re)，

其中：

- *μ*MA 是流体动力粘度。
- *N*R 是 **Number of tube rows along flow direction**。这是沿湿空气流动方向的两相流体管排数。

端口 **B2** 与内部节点 I2 之间的压差为：

pB2−pI2=12μ2NRρD2Hg(Re)。

**经验压力损失公式**

当 **Pressure loss model** 设置为 `Euler number per tube row` 或 **Flow geometry** 设置为 `Generic` 时，粘性摩擦引起的压力损失使用压力损失系数计算，以 Euler 数 *Eu* 表示：

Eu=ξNR，

其中 *ξ* 是经验压力损失系数。

端口 **A2** 与内部节点 I2 之间的压差为：

pA2−pI2=12NREum˙A2|m˙A2|2ρACS2。

端口 **B2** 与内部节点 I2 之间的压差为：

pB2−pI2=12NREum˙B2|m˙B2|2ρACS2。

### 壁面热质量

如果选择 **Enable wall thermal mass**，模块会建模换热器壁面热质量，这会引入壁面对温度或热流变化瞬态响应的延迟。如果建模热质量，壁面会在其边界内储存热量。这种热量储存会减缓稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率平衡为止。

如果选择 **Enable wall thermal mass**，壁面能量守恒为

(Mwallcp,wall2)dTwall2Pdt=−Q2P−Q(Mwallcp,wall2)dTwallMAdt=−QMA+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁温。模块使用该值来建模瞬态响应。无法测量该值。

传递到每种流体的热量为

Q2P=C2P(Twall2P−Tin2P)(1−e−NTU2P)QMA=CMA(TwallMA−TinMA)(1−e−NTUMA)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容率。

每一侧流体与壁面之间的传热单元数为

NTU2P=U2PA2PC2PNTUMA=UMAAMACMA

其中 *A* 是壁面表面积，*U* 是传热系数。

### 守恒方程

**两相流体**

两相流体中的总质量累积速率定义为：

dM2Pdt=m˙A1+m˙B1，

其中：

- *M2P* 是两相流体的总质量。
- m˙A1 是端口 **A1** 处流体的质量流量。
- m˙B1 是端口 **B1** 处流体的质量流量。

当流体通过端口流入模块时，流量为正。

能量守恒方程将比内能的变化与流体的传热联系起来：

M2Pdu2Pdt+u2P(m˙A1+m˙B1)=ϕA1+ϕB1−Q，

其中：

- *u*2P 是两相流体的比内能。
- *φ*A1 是端口 **A1** 处的能量流率。
- *φ*B1 是端口 **B1** 处的能量流率。
- *Q* 是传热速率，当热量离开两相流体体积时为正。

**湿空气**

该模块具有湿空气混合物、水蒸气、微量气体和水滴的质量转换方程。

**注意**

如果湿空气属性 (MA) 模块中的 **Trace gas model** 参数为 `None`，则湿空气网络不建模微量气体。在这种情况下，在冷凝器蒸发器 (2P-MA) 模块中，微量气体的守恒方程设置为 0。

如果在湿空气属性 (MA) 模块中清除 **Enable entrained water droplets**，则湿空气网络不建模夹带的水滴。在这种情况下，在冷凝器蒸发器 (2P-MA) 模块中，水滴的守恒方程设置为 0。

湿空气混合物的累积速率考虑了通过换热器端口的湿空气质量流量的变化以及冷凝质量流量，

m˙MA,net=m˙A2+m˙B2−m˙w,cond−m˙w,conv+m˙d,evap，

其中：

- m˙A2 是端口 **A2** 处的湿空气质量流量。
- m˙A2 是端口 **B2** 处的湿空气质量流量。
- m˙w,cond 是由于流体体积饱和而导致的水蒸气冷凝速率。
- m˙w,conv 是壁面上的冷凝速率。
- m˙d,evap 是水滴蒸发速率。

水蒸气的质量守恒方程为

dxwdtρMAIV+xwm˙MA,net=m˙w,net，

其中 *xw* 是蒸汽的质量分数，*ρMAI* 是流体体积中湿空气的密度，*V* 是湿空气总体积。

m˙*w,net* 是净水蒸气质量流量，

m˙w,net=m˙w,A2+m˙w,B2−m˙w,cond−m˙w,conv+m˙d,evap，

其中：

- m˙w,A2 是端口 **A2** 处的水蒸气质量流量。
- m˙w,B2 是端口 **B2** 处的水蒸气质量流量。

微量气体质量平衡为

dxgdtρMAIV+xgm˙MA,net=m˙g,A2+m˙g,B2，

其中：

- *xg* 是微量气体的质量分数。
- m˙g,A2 是端口 **A2** 处的微量气体质量流量。
- m˙g,B2 是端口 **B2** 处的微量气体质量流量。

水滴质量平衡为

drdIdtρMAIV+rdIm˙MA,net=m˙d,net，

其中 *rdI* 是流体体积中水滴与湿空气的质量比。

m˙dnet 是净水滴质量流量，

m˙d,net=m˙d,A2+m˙d,B2+λd(m˙w,cond+m˙w,conv)−m˙d,evap，

其中：

- m˙d,A2 是端口 **A2** 处的水滴质量流量。
- m˙d,A2 是端口 **B2** 处的水滴质量流量。
- *λd* 是 **Fraction of condensate entrained as water droplets** 参数的值。

在湿空气侧，能量守恒考虑了由于传热和水蒸气从湿空气质量中冷凝出来而引起的比内能变化，

(cpI−RI+rdcpdI)VρMAIdTIdt+uaIm˙MA,net+(uwI−uaI)m˙w,net+(ugI−uaI)m˙g,net+hdIm˙d,net=      ϕA2+ϕB2+Q−(1−λd)(m˙w,condhdI+m˙w,convhdH)−pIdVdt，

其中：

- *ua,I*、*uw,I* 和 *ug,I* 分别是空气、水蒸气和气体的内能。
- *cpI* 是湿空气比热。
- *cpdI* 是水滴比热。
- *rd* 是水滴与湿空气的质量比。
- *pI* 是内部体积的压力。
- *TI* 是内部体积的温度。
- *RI* 是内部体积比气体常数。
- *hdI* 是流体体积中水滴的比焓。
- *hdH* 是壁面上水滴的比焓。
- *ϕA2* 是端口 **A2** 处的能量流率。
- *ϕB2* 是端口 **B2** 处的能量流率。

传入或传出湿空气的热量 *Q* 等于从热液体传入或传出的热量。
