---
type: simulink-block
title: 'Condenser Evaporator (TL-2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid - Thermal Liquid'
documentation_page: 'condenserevaporatortl2p'
documentation_source_path: 'ref/condenserevaporatortl2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Condenser Evaporator (TL-2P)

## 端口

### 守恒

### **A1** — 热液体端口 thermal liquid

与热液体相关联的入口或出口端口。

### **B1** — 热液体端口 thermal liquid

与热液体相关联的入口或出口端口。

### **A2** — 两相流体端口 two-phase fluid

与两相流体相关联的入口或出口端口。

### **B2** — 两相流体端口 two-phase fluid

与两相流体相关联的入口或出口端口。

### 输出

### **Z** — 两相流体区域长度分数 physical signal

两相流体通道中区域长度分数的三元素向量，以 physical signal 返回。该向量采用 [L, M, V] 形式，其中 L 是过冷液体，M 是液-汽混合物，V 是过热蒸气。

## 参数

### 配置

### **Flow arrangement** — 流路对齐 `Cross flow` (默认) | `Parallel flow` | `Counter flow`

换热器两侧之间的流路对齐方式。可用的流动布置为：

- `Parallel flow`。流动沿同一方向。
- `Counter flow`。流动彼此平行，方向相反。
- `Cross flow`。流动彼此垂直。

### **Cross flow arrangement** — 每个流动通道中的热混合条件 `Both fluids unmixed` (默认) | `Both fluids mixed` | `Thermal Liquid 1 mixed & Two-Phase Fluid 2 unmixed` | `Thermal Liquid 1 unmixed & Two-Phase Fluid 2 mixed`

选择每种流体是否可在其通道中混合。混合流意味着流体在沿流路流动时可自由横向移动。非混合流意味着流体被限制为仅沿流路流动。例如，带翅片的一侧视为非混合流。

#### 依赖项

要启用此参数，请将 **Flow arrangement** 设置为 `Cross flow`。

### **Wall thermal resistance** — 壁通过热传导对热流的阻力 `0 K/W` (默认) | positive scalar

分隔两种换热器流体的界面壁的热阻。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2` (默认) | positive scalar

热液体端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2` (默认) | positive scalar

热液体端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01` m^2 (默认) | positive scalar

两相流体端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处的流通面积 `0.01 m^2` (默认) | positive scalar

两相流体端口 **B2** 处的流通面积。

### **Enable wall thermal mass** — 用于对壁热质量建模的选项 `off` (默认) | `on`

是否对换热器壁热质量建模。对壁热质量建模会引入壁对温度或热流变化瞬态响应的延迟。如果清除 **Enable wall thermal mass**，该模块会假定壁足够薄，以至于在传热时间尺度上瞬态响应是瞬时的。

### **Wall mass** — 换热器壁质量 `1 kg` (默认) | positive scalar

换热器壁的质量。该模块使用此值计算壁热质量。

#### 依赖项

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 换热器壁比热 `490 J/(K*kg)` (默认) | positive scalar

换热器壁的比热。该模块使用此值计算壁热质量。

#### 依赖项

要启用此参数，请选择 **Enable wall thermal mass**。

### Thermal Liquid 1

### **Flow geometry** — 热液体流动配置 `Flow inside one or more tubes` (默认) | `Flow perpendicular to bank of circular tubes` | `Generic`

热液体流路。流动可以在管组外部流过，或在单根管或管组内部流动。也可以基于经验值指定通用参数化。

### **Number of tubes** — 热液体管数量 `25` (默认) | positive scalar

热液体管数量。管数越多，由于黏性摩擦导致的压力损失越高，但传热表面积越大。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`。

### **Total length of each tube** — 每根热液体管的总长度 `1 m` (默认) | positive scalar

每根热液体管的总长度。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`。

### **Tube cross section** — 单根管的横截面形状 `Circular` (默认) | `Rectangular` | `Annular` | `Generic`

单根管的横截面形状。设置为 `Generic` 可指定任意横截面几何形状。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`。

### **Tube inner diameter** — 单根管的内径 `0.05 m` (默认) | positive scalar

单根管横截面的内径。横截面和直径沿管均匀。直径大小影响压力损失和传热计算。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Circular`。

### **Tube width** — 单根管的内部宽度 `0.05 m` (默认) | positive scalar

单根管横截面的内部宽度。横截面和宽度沿管均匀。宽度和高度影响压力损失和传热计算。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Rectangular`。

### **Tube height** — 单根管的内部高度 `0.05 m` (默认) | positive scalar

单根管的内部高度。横截面和高度沿管均匀。宽度和高度影响压力损失和传热计算。

#### 依赖项

要启用此参数，请将 **Flow geometry** 参数化设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Rectangular`。

### **Annulus inner diameter (heat transfer surface)** — 环形横截面的较小直径 `0.05 m` (默认) | positive scalar

单根管环形横截面的较小直径。横截面和内径沿管均匀。内径影响压力损失和传热计算。传热通过环形的内表面发生。

#### 依赖项

要启用此参数，请将 **Flow geometry** 参数化设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Annular`。

### **Annulus outer diameter** — 环形横截面的较大直径 `0.1 m` (默认) | positive scalar

单根管环形横截面的较大直径。横截面和外径沿管均匀。外径影响压力损失和传热计算。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Annular`。

### **Cross-sectional area per tube** — 每根管的内部流通面积 `0.002 m^2` (默认) | positive scalar

每根管的内部流通面积。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Generic`。

### **Wetted perimeter of tube cross-section for pressure loss** — 流体接触的管横截面周长 `0.15 m` (默认) | positive scalar

流体接触的管横截面周长。横截面和周长沿管均匀。此值用于压力损失计算。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Generic`。

### **Perimeter of tube cross-section for heat transfer** — 用于传热计算的单根管周长 `0.15 m` (默认) | positive scalar

用于传热计算的管周长。这通常与管周长相同，但在诸如环形横截面的情况下，根据传热表面，这可能仅为内径或外径。横截面和管周长沿管均匀。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Generic`。

### **Pressure loss model** — 计算由黏性摩擦引起的压力损失的方法 `Correlation for flow inside tubes` (默认) | `Euler number per tube row` | `Pressure loss coefficient` | `Correlation for flow over tube bank`

计算由黏性摩擦引起的压力损失的方法。不同流动配置可使用不同模型。设置为：

- `Correlation for flow inside tubes`。使用此设置通过 Haaland 关联式计算压力损失。
- `Pressure loss coefficient`。使用此设置基于经验损失系数计算压力损失。
- `Euler number per tube row`。使用此设置基于经验 Euler 数计算压力损失。
- `Correlation for flow over tube bank`。使用此设置基于 Hagen 数计算压力损失。

可用的压力损失模型取决于 **Flow geometry** 设置。

#### 依赖项

当 **Flow geometry** 设置为 `Flow inside one or more tubes` 时，**Pressure loss model** 可以设置为以下任一项：

- `Pressure loss coefficient`。
- `Correlation for flow inside tubes`。

当 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，**Pressure loss model** 可以设置为以下任一项：

- `Correlation for flow over tube bank`。
- `Euler number per tube row`。

当 **Flow geometry** 设置为 `Generic` 时，**Pressure loss model** 参数被禁用。压力损失使用 **Pressure loss coefficient, delta\_p/(0.5\*rho\*v^2)** 参数根据经验计算。

### **Pressure loss coefficient, delta\_p/(0.5\*rho\*v^2)** — 通道中所有压力损失的经验损失系数 `10` (默认) | positive scalar

通道中所有压力损失的经验损失系数。此值考虑壁面摩擦以及由于通道中的弯头、弯管和其他几何变化引起的局部损失。

损失系数可根据标称工况计算，或进行调整以拟合实验数据。其定义为：

ξ=Δp12ρv2,

其中 *Δp* 是压降，*ρ* 是热液体密度，*v* 是流速。

#### 依赖项

要启用此参数，请设置以下任一项：

- 将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Pressure loss coefficient`。
- 将 **Flow geometry** 设置为 `Generic`。

### **Local resistance specification** — 用于量化压力损失的方法 `Aggregate equivalent length` (默认) | `Local loss coefficient`

用于量化 Haaland 关联式中压力损失的方法。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Aggregate equivalent length of local resistances** — 每根管所有局部阻力的合计长度 `0.1 m` (默认) | positive scalar

每根管所有局部阻力的合计长度。此值是使压力损失与管中因弯头、三通或接头等阻力引起的所有局部损失之和相同的管长度。合计长度越长，压力损失越大。该模块在计算摩擦引起的压力损失时，将此参数的值加到 **Total length of each tube** 参数中。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Pressure loss model** 设置为 `Correlations for flow inside tubes`，并将 **Local resistance specification** 设置为 `Aggregate equivalent length`。

### **Total local loss coefficient** — 压力损失系数 `0.1` (默认) | positive scalar

系统上的局部压力损失系数。可使用此参数校准系统以匹配实验结果。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`，并将 **Local resistance specification** 设置为 `Local loss coefficient`。

### **Internal surface absolute roughness** — 平均表面粗糙度高度 `15e-6 m` (默认) | positive scalar

管表面缺陷的平均高度。对于使用 Haaland 关联式计算的压力损失，壁面越粗糙，湍流区压力损失越大。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将以下任一项：

- **Pressure loss model**
- **Heat transfer coefficient model**

设置为 `Correlation for flow inside tubes`。

### **Laminar flow upper Reynolds number limit** — 表示层流的最大 Reynolds 数 `2000` (默认) | positive scalar

表示层流的最大 Reynolds 数。介于该值与 **Turbulent flow lower Reynolds number limit** 之间时，流态为过渡流。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Turbulent flow lower Reynolds number limit** — 表示湍流的最小 Reynolds 数 `4000` (默认) | positive scalar

表示湍流的最小 Reynolds 数。介于该值与 **Laminar flow upper Reynolds number limit** 之间时，流态为层流和湍流之间的过渡流。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流中黏性摩擦压力损失方程中的系数 `64` (默认) | positive scalar

层流中黏性摩擦压力损失方程中的系数。此参数也称为 *shape factor*。默认值对应于圆管横截面。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为 `Correlation for flow inside tubes`，将 **Tube cross section** 设置为 `Generic`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Heat transfer coefficient model** — 计算流体与壁之间传热系数的方法 `Correlation for flow over tube bank` (默认) | `Colburn equation` | `Correlation for flow inside tubes`

计算流体与壁之间传热系数的方法。可用设置为：

- `Colburn equation`。使用此设置通过用户定义的变量 *a*、*b* 和 *c* 按 Colburn 方程计算传热系数。
- `Correlation for flow over tube bank`。使用此设置基于管束关联式使用 Hagen 数计算传热系数。
- `Correlation for flow inside tubes`。使用此设置通过 Gnielinski 关联式计算管流的传热系数。

#### 依赖项

要启用此参数，请将 **Flow geometry** 设置为以下任一项：

- `Flow perpendicular to bank of circular tubes`。
- `Flow inside one or more tubes`。

### **系数 [a, b, c]（用于 a\*Re^b\*Pr^c）** — Colburn equation 系数 `[0.023, 0.8, 0.33]`（默认）| 三元素向量

包含 Colburn equation 经验系数的三元素向量。Colburn equation 是用于计算 Nusselt 数的一种公式。Colburn equation 的一般形式为：

Nu=aRebPrc.

当 **传热系数模型** 设置为 `Colburn equation`，且 **流动几何** 设置为 `Flow inside one or more tubes`，或者 **流动几何** 设置为 `Generic` 时，默认的 Colburn equation 为：

Nu=0.023Re0.8Pr1/3.

当 **传热系数模型** 设置为 `Colburn equation`，且 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes` 时，默认的 Colburn equation 为：

Nu=0.27Re0.63Pr0.36.

#### 依赖关系

要启用此参数，请设置：

1. 将 **流动几何** 设置为以下任一值：

   - `Flow inside one or more tubes`
   - `Flow perpendicular to bank of circular tubes`

   并将 **传热系数模型** 设置为 `Colburn equation`。

2. 将 **流动几何** 设置为 `Generic`。

### **层流 Nusselt 数** — 层流状态下对流传热与导热传热之比 `3.66`（默认）| 正标量

层流状态下对流传热与导热传热之比。流体 Nusselt 数影响传热速率，并取决于管横截面。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，将 **管横截面** 设置为 `Generic`，并将 **传热参数化** 设置为 `Correlation for flow inside tubes`。

### **管束栅格排列** — 管束中管排的几何放置方式 `Inline`（默认）| `Staggered`

管束中管子的对齐方式。各排要么与其相邻排成一线，要么错列。

- `Inline`：所有管排均直接位于彼此后方。
- `Staggered`：某一管排的管子位于上一管排管子的间隙处。

管对齐方式会影响 Nusselt 数和传热速率。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **沿流动方向的管排数** — 管束中两相流体管排的数量 `5`（默认）| 正标量

管束中两相流体管排的数量。这些排与热液体流动方向对齐。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **每个管排中的管段数** — 管束每一排中两相流体管的数量 `5`（默认）| 正标量

管束每一排中两相流体管的数量。该测量方向垂直于热液体流动方向。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **管排中每个管段的长度** — 每根两相流体管的长度 `1 m`（默认）| 正标量

跨越一个管排的每根管的长度。管束中的所有管长度相同。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **管外径** — 单根两相流体管的外径 `0.05 m`（默认）| 正标量

两相流体管的外径。横截面沿管均匀，因此直径处处恒定。该值会影响流体横掠管束时由于黏性摩擦造成的损失。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **纵向管间距（沿流动方向）** — 两相流体管排之间的中心距 `0.15 m`（默认）| 正标量

两相流体管中心之间的距离，与热液体流动方向对齐。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **横向管间距（垂直于流动方向）** — 一排中两相流体管之间的中心距 `0.15` m（默认）| 正标量

一排两相流体管中各管中心之间的距离。该测量方向垂直于热液体流动方向。有关详细信息，请参阅 Heat Transfer Coefficient for Flows Across a Tube Bank。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **每管排的 Euler 数, delta\_p/(N\*0.5\*rho\*v^2)** — 管束每一排的 Euler 数 `10`（默认）| 正标量

每管排压降的经验系数。Euler 数是压降与流体动量之比：

Eu=ΔpN12ρv2,

其中 *N* 是 **沿流动方向的管排数**，*Δp* 是压降，*ρ* 是热液体混合物密度，*v* 是流速。

每个管排位于垂直于热液体流动的平面内。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`，并将 **压力损失模型** 设置为 `Euler number per tube row`。

### **最小自由流动面积** — 入口与出口之间的最小总流动面积 `0.01 m^2`（默认）| 正标量

入口与出口之间的最小总横截流动面积。如果通道是管道、管子、槽或凹槽的集合，则此参数的值为最小流动面积点处最小面积之和。该参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值为一个横截面中管间间隙之和最小处的间隙之和。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Generic`。

### **无翅片传热表面积** — 不包括翅片的传热表面总面积 `2 m^2`（默认）| 正标量

不包括翅片的传热表面总面积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Generic`。

### **换热器内热液体体积** — 换热器中热液体的总体积 `0.05 m^3`（默认）| 正标量

换热器中热液体的总体积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Generic`。

### **污垢系数** — 由污垢沉积物引起的附加热阻 `0.1 m^2*K/kW`（默认）| 正标量

壁面上污垢层引起的附加热阻。在实际系统中，污垢沉积物会随时间增长。然而，其增长足够缓慢，可假设在仿真期间保持不变。

### **翅片总表面积** — 所有翅片的传热表面积总和 `0 m^2`（默认）| 正标量

接触热液体的所有翅片两侧的传热表面积总和。例如，如果翅片为矩形，则表面积为矩形面积的两倍。

总传热表面积是通道表面积与有效翅片表面积之和，有效翅片表面积是 **翅片效率** 与 **翅片总表面积** 的乘积。

### **翅片效率** — 翅片实际传热率与理想传热率之比 `0.5`（默认）| 范围 [0,1] 内的正标量

如果整个翅片均处于主传热表面温度，则接触热液体的翅片的实际传热量与理想传热量之比。

### **初始热液体压力** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的热液体压力。

### **初始热液体温度** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 二元向量

仿真开始时热液体通道中的温度。此参数可以是标量或二元向量。标量值表示通道中的平均初始温度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始温度。模块计算两个端口之间的线性梯度。入口端口和出口端口根据初始流动方向确定。

### Two-Phase Fluid 2

### **管数** — 两相流体管数量 `25`（默认）| 正标量

两相流体管数量。

### **每根管的总长度** — 每根两相流体管的总长度 `1 m`（默认）| 正标量

每根两相流体管的总长度。

### **管横截面** — 管的横截面形状 `Circular`（默认）| `Rectangular` | `Annular` | `Generic`

管的横截面形状。使用 `Generic` 指定任意横截面几何形状。

### **管内径** — 单根管的内径 `0.05 m`（默认）| 正标量

一根管横截面的内径。横截面和直径沿管均匀。直径大小会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **管横截面** 设置为 `Circular`。

### **管宽度** — 单根管的内部宽度 `0.05 m`（默认）| 正标量

一根管横截面的内部宽度。横截面和宽度沿管均匀。宽度和高度会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **管横截面** 设置为 `Rectangular`。

### **管高度** — 单根管的内部高度 `0.05 m`（默认）| 正标量

一根管的内部高度。横截面和高度沿管均匀。宽度和高度会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **管横截面** 设置为 `Rectangular`。

### **环隙内径（传热表面）** — 环形横截面的较小直径 `0.05 m`（默认）| 正标量

一根管环形横截面的较小直径。横截面和内径沿管均匀。内径会影响压力损失和传热计算。传热通过环隙内表面发生。

#### 依赖关系

要启用此参数，请将 **管横截面** 设置为 `Annular`。

### **环隙外径** — 环形横截面的较大直径 `0.1 m`（默认）| 正标量

一根管环形横截面的较大直径。横截面和外径沿管均匀。外径会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **管横截面** 设置为 `Annular`。

### **每根管的横截面积** — 单根管中垂直于流动的内部面积 `0.002 m^2`（默认）| 正标量

每根管的内部流动面积。

#### 依赖关系

要启用此参数，请将 **管横截面** 设置为 `Generic`。

### **用于压力损失的管横截面湿周** — 流体接触的管横截面周长 `0.15 m`（默认）| 正标量

流体接触的管横截面周长。横截面和周长沿管均匀。该值应用于压力损失计算。

#### 依赖关系

要启用此参数，请将 **管横截面** 设置为 `Generic`。

### **用于传热的管横截面周长** — 单根管用于传热计算的周长 `0.15 m`（默认）| 正标量

用于传热计算的管周长。这通常与管周长相同，但在环形横截面等情况下，根据传热表面，这可能只是内径或外径。横截面和管周长沿管均匀。

#### 依赖关系

要启用此参数，请将 **管横截面** 设置为 `Generic`。

### **压力损失模型** — 由黏性摩擦引起的压力损失计算方法 `Correlation for flow inside tubes`（默认）| `Pressure loss coefficient`

由黏性摩擦引起的压力损失计算方法。设置为：

- `Pressure loss coefficient`。使用此设置基于经验损失系数计算压力损失。
- `Correlation for flow inside tubes`。使用此设置基于管流关联式计算压力损失。

### **压力损失系数, delta\_p/(0.5\*rho\*v^2)** — 通道中所有压力损失的经验损失系数 `10`（默认）

通道中所有压力损失的经验损失系数。该值考虑壁面摩擦以及通道中弯曲、弯头和其他几何变化引起的局部损失。

损失系数可根据额定工况计算，或调整为拟合实验数据。其定义为：

ξ=Δp12ρv2,

其中 *Δp* 是压降，*ρ* 是两相流体密度，*v* 是流速。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Pressure loss coefficient`。

### **局部阻力规范** — 量化压力损失的方法 `Aggregate equivalent length`（默认）| `Local loss coefficient`

在 Haaland 关联式中量化压力损失的方法。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlation for flow inside tubes`。

### **局部阻力的总等效长度** — 每根管所有局部阻力的组合长度 `0.1 m`（默认）| 正标量

每根管所有局部阻力的组合长度。该值是指与管中由弯头、三通或管接头等阻力引起的所有局部损失之和产生相同压力损失的管长。组合长度越长，压力损失越大。模块在计算摩擦引起的压力损失时，将此参数的值加到 **每根管的总长度** 参数中。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlation for flow inside tubes`，并将 **局部阻力规范** 设置为 `Aggregate equivalent length`。

### **总局部损失系数** — 压力损失系数 `0.1`（默认）| 正标量

系统上的局部压力损失系数。您可以使用此参数校准系统，以匹配实验结果。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlation for flow inside tubes`，并将 **局部阻力规范** 设置为 `Local loss coefficient`。

### **内表面绝对粗糙度** — 平均表面粗糙度高度 `15e-6 m`（默认）| 正标量

管表面缺陷的平均高度。对于使用 Haaland 关联式计算的压力损失，壁面越粗糙，湍流状态下的压力损失越大。

#### 依赖关系

要启用此参数，请将以下任一项：

- **压力损失模型**
- **传热系数模型**

设置为 `Correlation for flow inside tubes`。

### **层流上限 Reynolds 数** — 指示层流的最大 Reynolds 数 `2000`（默认）| 正标量

指示层流的最大 Reynolds 数。在此值与 **湍流下限 Reynolds 数** 之间，流态为过渡流。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlations for tubes`。

### **湍流下限雷诺数** — 指示湍流流动的最小雷诺数 `4000`（默认）| 正标量

指示湍流流动的最小雷诺数。在此值与 **层流上限雷诺数** 之间，流态为过渡态。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlations for tubes`。

### **Darcy 摩擦因子的层流摩擦常数** — 层流中由于粘性摩擦导致的压力损失系数 `64`（默认）| 正标量

层流中粘性摩擦的压力损失方程中的系数。此参数也称为 *形状因子*。默认值对应于圆管横截面。

#### 依赖关系

要启用此参数，请将 **压力损失模型** 设置为 `Correlations for tubes`。

### **传热系数模型** — 计算流体与壁面之间传热系数的方法 `Correlation for flow inside tubes`（默认）| `Colburn equation`

计算流体与壁面之间传热系数的方法。可用设置为：

- `Colburn equation`。使用此设置以用户定义的变量 *a*、*b* 和 *c* 计算传热系数。在液体区和蒸汽区，传热系数基于 Colburn 方程。在液体-蒸汽混合物区，传热系数基于 Cavallini-Zecchin 方程。
- `Correlation for flow inside tubes`。使用此设置计算管内流动的传热系数。在液体区和蒸汽区，传热系数使用 Gnielinski 关联式计算。在液体-蒸汽混合物区，传热系数使用 Cavallini-Zecchin 方程计算。

### **液体区中 a\*Re^b\*Pr^c 的系数 [a, b, c]** — 液体区中的 Colburn 方程系数 `[.023, .8, .33]`（默认）| 三元素正标量向量

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，该数按区域由 Colburn 方程计算。Colburn 方程的一般形式为：

Nu=aRe^bPr^c。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Colburn equation`。

### **混合物区中 a\*Re^b\*Pr^c 的系数 [a, b, c]** — 混合物区中的 Cavallini-Zecchin 方程系数 `[.05, .8, .33]`（默认）| 三元素正标量向量

包含 Cavallini-Zecchin 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，该数在混合物区由 Cavallini-Zecchin 方程计算：

Nu=aReSL^bPrSL^c{[(ρSL/ρSV−1)xOut+1]^(1+b)−[(ρSL/ρSV−1)xIn+1]^(1+b)} / ((1+b)(ρSL/ρSV−1)(xOut−xIn))。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Colburn equation`。

### **蒸汽区中 a\*Re^b\*Pr^c 的系数 [a, b, c]** — 蒸汽区中的 Colburn 方程系数 `[.023, .8, .33]`（默认）| 三元素正标量向量

包含 Colburn 方程经验系数的三元素向量。每个流体区具有不同的 Nusselt 数，该数按区域由 Colburn 方程计算。Colburn 方程的一般形式为：

Nu=aRe^bPr^c。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Colburn equation`。

### **层流 Nusselt 数** — 层流流态中对流传热与传导传热之比 `3.66`（默认）| 正标量

层流流态中对流传热与传导传热之比。流体 Nusselt 数影响传热速率，并取决于管横截面。

#### 依赖关系

要启用此参数，请将 **传热系数模型** 设置为 `Correlation for flow inside tubes`。

### **污垢因子** — 由于污垢沉积物导致的附加热阻 `0.1 m^2*K/kW`（默认）| 正标量

由于壁面上的污垢层导致的附加热阻。在实际系统中，污垢沉积物会随时间增长，然而，其增长足够缓慢，以至于可以在仿真期间假定为常数。

### **总翅片表面积** — 翅片的总传热表面积 `0 m^2`（默认）| 正标量

接触两相流体的所有翅片两侧的总传热表面积。例如，如果翅片是矩形的，则表面积是该矩形面积的两倍。

总传热表面积是通道表面积与有效翅片表面积之和，其中有效翅片表面积是 **翅片效率** 与 **总翅片表面积** 的乘积。

### **翅片效率** — 翅片实际传热速率与理想传热速率之比 `0.5`（默认）| 位于范围 [0,1] 内的正标量

如果整个翅片处于主传热表面温度，则通过接触两相流体的翅片的实际传热与理想传热之比。

### **初始流体能量规范** — 两相流体的初始状态 `Temperature`（默认）| `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy`

用于描述流体初始状态的量。

**初始流体能量规范** 参数的值限制了两相流体可用的初始状态。当 **初始流体能量规范** 为：

- `Temperature` — 指定为过冷液体或过热蒸汽的初始状态。您不能指定液体-蒸汽混合物，因为在液体-蒸汽混合物区域中温度是恒定的。
- `Vapor quality` — 指定为液体-蒸汽混合物的初始状态。您不能指定过冷液体或过热蒸汽，因为在整个区域中液体质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定为液体-蒸汽混合物的初始状态。您不能指定过冷液体或过热蒸汽，因为在整个区域中液体质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。模块不限制初始状态。

### **初始两相流体压力** — 仿真开始时的流体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的流体压力。

### **初始两相流体温度** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道中的温度。此参数可以是标量或二元素向量。标量值表示通道中的平均初始温度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始温度。模块计算两个端口之间的线性梯度。入口端口和出口端口根据初始流动方向识别。

#### 依赖关系

要启用此参数，请将 **初始流体能量规范** 设置为 `Temperature`。

### **初始两相流体蒸汽干度** — 仿真开始时的蒸汽质量分数 `0.5`（默认）| 位于范围 [0,1] 内的正标量 | 二元素向量

仿真开始时两相流体通道中的蒸汽质量分数。此参数可以是标量或二元素向量。标量值表示通道中的平均初始蒸汽干度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始蒸汽干度。模块计算两个端口之间的线性梯度。入口端口和出口端口根据初始流动方向识别。

#### 依赖关系

要启用此参数，请将 **初始流体能量规范** 设置为 `Vapor quality`。

### **初始两相流体蒸汽空隙率** — 仿真开始时的蒸汽体积分数 `0.5`（默认）| 位于范围 [0,1] 内的正标量 | 二元素向量

仿真开始时两相流体通道中的蒸汽体积分数。此参数可以是标量或二元素向量。标量值表示通道中的平均初始空隙率。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始空隙率。模块计算两个端口之间的线性梯度。入口端口和出口端口根据初始流动方向识别。

#### 依赖关系

要启用此参数，请将 **初始流体能量规范** 设置为 `Vapor void fraction`。

### **初始两相流体比焓** — 仿真开始时的单位质量焓 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道中的单位质量焓。此参数可以是标量或二元素向量。标量值表示通道中的平均初始比焓。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始比焓。模块计算两个端口之间的线性梯度。入口端口和出口端口根据初始流动方向识别。

#### 依赖关系

要启用此参数，请将 **初始流体能量规范** 设置为 `Specific enthalpy`。

### **初始两相流体比内能** — 仿真开始时的单位质量内能 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时两相流体通道中的单位质量内能。此参数可以是标量或二元素向量。标量值表示通道中的平均初始比内能。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始比内能。模块计算两个端口之间的线性梯度。入口端口和出口端口根据初始流动方向识别。

#### 依赖关系

要启用此参数，请将 **初始流体能量规范** 设置为 `Specific internal energy`。

## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Thermal Liquid

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2025a：对换热器壁面的热质量建模

选择 **壁面热动力学** 来对换热器壁面的热质量建模。

### R2024a：自由流动面积计算更新

当 **流动几何** 为 `Flow perpendicular to bank of circular tubes` 时，模块现在使用不同的方法计算自由流动面积。如果 **每排管中的管段数** 参数的值较小，模块可能会显示压力损失和传热的轻微增加。

### R2023a：通过使用局部损失系数对附加压力损失建模

将 **局部阻力规范** 参数设置为 `Local loss coefficient`，以指定量化压力损失的新方法。此选项允许您对超出管道长度所致损失之外的附加摩擦损失进行建模。

## 描述

对热液体网络与两相流体网络之间的热交换进行建模

Condenser Evaporator (TL-2P) 模块对热交换器建模，该热交换器具有一个在端口 **A1** 和 **B1** 之间流动的热液体网络，以及一个在端口 **A2** 和 **B2** 之间流动的两相流体网络。换热器可用作冷凝器或蒸发器。流体流可布置为并流、逆流或错流配置。

**制冷应用示例换热器**

您可以将热液体侧建模为管内流动、绕两相流体管道的流动，或通过经验性通用参数化进行建模。

模块使用效能-NTU（E-NTU）方法对通过共享壁面的传热进行建模。还建模了换热器壁面上的污垢，它会增加热阻并减少两种流体之间的热交换。您还可以选择对热液体侧和两相流体侧的翅片进行建模。换热器两侧因粘性摩擦导致的压力损失可以通过解析方法或通用参数化进行建模，后者可用于根据您自己的数据调整。

您可以将两相流体侧建模为单管内流动或一组管内的流动。两相流体管使用边界跟随模型来跟踪三个区域中的过冷液体（L）、汽液混合物（M）和过热蒸汽（V）。区域在系统中所占空间的相对量称为*区域长度分数*。

**两相流体管路中的区域长度分数**

两相流体管道中各区域长度分数之和等于 `1`。端口 **Z** 将区域长度分数作为物理信号向量返回，对应三个相中的每一个：[L, M, V]。

### 换热器配置

换热器效能基于所选换热器配置、各相的流体属性、换热器每侧的管几何和流动配置，以及翅片的使用和尺寸。

**流动布置**

**流动布置**参数指定两侧之间的相对流动路径：

- `Parallel flow` 表示流体沿相同方向流动。
- `Counter flow` 表示流体平行但方向相反地流动。
- `Cross flow` 表示流体彼此垂直流动。

**热混合**

当**流动布置**设置为 `Cross flow` 时，使用**交叉流布置**参数指示两相流体或热液体流动是否被折流板或壁分隔成多条路径。没有这些分隔时，流动可自由混合，并被视为*混合*。在交叉流布置中，两种流体、一种流体或两种都不混合。混合会使流体温度沿第二流体的流动方向均匀化，并沿垂直于第二流体流动的方向变化。

非混合流动的温度沿第二流体的流动路径以及垂直于该路径的方向都会变化。

**交叉流配置示例**

注意，仿真期间的流动方向不影响所选的流动布置设置。模块上的端口不反映物理换热系统中端口的物理位置。

所有流动布置均为单程，这意味着流体在换热器中不会多次转弯以增加传热点。要对多程换热器建模，可以将多个 Condenser Evaporator (TL-2P) 模块串联或并联布置。

例如，要在两相流体侧实现双程配置并在热液体侧实现单程配置，可以将两相流体侧串联，并将热液体侧并联到同一输入（例如两个 Mass Flow Rate Source 模块，其质量流量为总质量流量的一半），如下所示。

**流动几何**

**流动几何**参数将热液体流动布置设置为在管或管组内部，或垂直于管束。您还可以指定经验性、通用配置。两相流体始终在管或管组内部流动。

当**流动几何**设置为 `Flow perpendicular to bank of circular tubes` 时，使用**管束栅格布置**参数将两相流体管束排列定义为 `Inline` 或 `Staggered`。红色向下箭头表示热液体流动方向。Inline 图还显示了**沿流动方向的管排数**和**每排管中的管段数**参数。这里，*流动方向*指热液体流动，*管*指两相流体管道。**一排管中每个管段的长度**参数在 Staggered 图中示出。

**翅片**

当**总翅片表面积**参数为 `0 m^2` 时，换热器配置没有翅片。翅片引入额外的传热表面积。每个流体侧都有单独的翅片面积和描述该流体中翅片的参数。例如，当热液体在管内流动且两相流体在管外流动时，**热液体 1** 部分中的**总翅片表面积**和**翅片效率**参数描述伸入管内的翅片。**两相流体 2** 部分中的**总翅片表面积**和**翅片效率**参数描述管外的翅片。

### 效能-NTU 传热

针对每个流体相计算传热速率。根据换热器两相流体侧出现的三个流体区，传热速率分三个部分计算。

区内的对流传热为

Qzone=ϵCMin(TIn,2P−TIn,TL),

其中：

- *C*Min 是该区中两种流体热容率中的较小者。热容率是流体比热 *c*p 与流体质量流量的乘积。*C*Min 始终为正。
- *T*In,2P 是两相流体的区入口温度。
- *T*In,TL 是热液体的区入口温度。
- *ε* 是换热器效能。

效能是热容率和传热单元数 *NTU* 的函数，并且还随换热器流动布置而变化，这在按流动布置的效能中有更详细讨论。*NTU* 计算如下：

NTU=zCMinR,

其中：

- *z* 是单个区的长度分数。
- *R* 是两股流动之间的总热阻，由对流、导热以及管壁上的任何污垢引起：

  R=1U2PATh,2P+F2PATh,2P+RW+FTLATh,TL+1UTLATh,TL,

  其中：

  - *U* 是相应流体的对流传热系数。该系数在两相流体关联式和热液体关联式中有更详细讨论。
  - *F* 分别是两相流体侧或热液体侧的**污垢系数**。
  - *R*W 是**通过传热表面的热阻**。
  - *A*Th 是换热器相应侧的传热表面积。*A*Th 是壁表面积 *A*W 与**总翅片表面积** *A*F 之和：

    ATh=AW+ηFAF,

    其中 *η*F 是**翅片效率**。

流体之间的总对流传热速率是过冷液体 (*QL*)、液-汽混合物 (*QM*) 和过热蒸气 (*QV*) 在三个区中传递的热量之和：

Q=∑QZ=QL+QM+QV.

模块在传热计算中使用的流体属性是入口值与流体体积中值的平均值。

**按流动布置的效能**

换热器效能根据其流动配置和每种流体中的混合情况而变化。以下是每种配置在液体区和蒸气区计算的效能公式。对于混合物区中的所有配置，效能为 ε=1−exp(−NTU)。

- 当**流动布置**设置为 `Parallel flow` 时：

  ϵ=1−exp[−NTU(1+CR)]1+CR
- 当**流动布置**设置为 `Counter flow` 时：

  ϵ=1−exp[−NTU(1−CR)]1−CRexp[−NTU(1−CR)]
- 当**流动布置**设置为 `Cross flow` 且**交叉流布置**设置为 `Both fluids unmixed` 时：

  ϵ=1−exp{NTU0.22CR[exp(−CRNTU0.78)−1]}
- 当**流动布置**设置为 `Cross flow` 且**交叉流布置**设置为 `Both fluids mixed` 时：

  ϵ=[11−exp(−NTU)+CR1−exp(−CRNTU)−1NTU]−1

当一种流体混合而另一种流体非混合时，效能方程取决于流体的相对热容率。当**流动布置**设置为 `Cross flow` 且**交叉流布置**设置为 `Thermal Liquid 1 mixed & Two-Phase Fluid 2 unmixed` 或 `Thermal Liquid 1 unmixed & Two-Phase Fluid 2 mixed` 时：

- 当具有 Cmax 的流体混合且具有 Cmin 的流体非混合时：

  ϵ=1CR(1−exp{−CR{1−exp(−NTU)}})
- 当具有 Cmin 的流体混合且具有 Cmax 的流体非混合时：

  ϵ=1−exp{−1CR[1−exp(−CRNTU)]}

*C*R 表示两种流体热容率之比：

CR=CMinCMax.

### 导热传热

区内的导热传热为

Qcond=Tout,TL−Tout,2PRcond,

其中：

- *Tout,2P* 是两相流体的区出口温度。
- *Tout,TL* 是热液体的区出口温度。
- *Rcond* 是两股流动之间的总导热热阻，

  Rcond=Dhk2PAW,2P+F2PAW,2P+RW+FTLAW,TL+DhkTLAW,TL,

  其中：

  - *AW* 是壁表面积。
  - *k* 是每种流体的导热率。
  - *DH* 是水力直径。

总传热是对流传热与导热传热之和。与对流传热相比，导热传热可忽略不计。当流量为零时，对流传热也为零。然而，由于对流传热和导热传热彼此独立运行，即使对流传热为零，仍然存在导热传热。

### 两相流体关联式

**传热系数**

对流传热系数根据流体 Nusselt 数变化：

U=NukDH,

其中：

- *Nu* 是区平均 Nusselt 数，取决于流态。
- *k* 是流体相的导热率。
- *D*H 是管水力直径。

对于过冷液体或过热蒸气区中的湍流，Nusselt 数用 Gnielinski 关联式计算：

Nu=fD8(Re−1000)Pr1+12.7f8(Pr2/3−1),

其中：

- *Re* 是流体 Reynolds 数。
- *Pr* 是流体 Prandtl 数。

对于液-汽混合物区中的湍流，Nusselt 数用 Cavallini-Zecchin 关联式计算：

Nu=aReSLbPrSLc{[(ρSLρSV−1)xOut+1]1+b−[(ρSLρSV−1)xIn+1]1+b}(1+b)(ρSLρSV−1)(xOut−xIn).

其中：

- *Re*SL 是饱和液体的 Reynolds 数。
- *Pr*SL 是饱和液体的 Prandtl 数。
- *ρ*SL 是饱和液体的密度。
- *ρ*SV 是饱和蒸气的密度。
- *a*= 0.05，*b* = 0.8，*c*= 0.33。

对于层流，Nusselt 数由**层流 Nusselt 数**参数设置。

对于过渡流，Nusselt 数是层流与湍流 Nusselt 数之间的混合。

**经验 Nusselt 数公式**

当**传热系数模型**参数设置为 `Colburn equation` 时，过冷液体和过热蒸气区的 Nusselt 数由经验 Colburn 方程计算：

Nu=aRebPrc,

其中 *a*、*b* 和 *c* 在**液体区中 a\*Re^b\*Pr^c 的系数 [a, b, c]**和**蒸气区中 a\*Re^b\*Pr^c 的系数 [a, b, c]**参数中定义。

液-汽混合物区的 Nusselt 数用 Cavallini-Zecchin 方程计算，系数在**混合物区中 a\*Re^b\*Pr^c 的系数 [a, b, c]**参数中指定。

**压力损失**

由粘性摩擦引起的压力损失随流态和配置而变化。压力损失计算使用总密度，即总流体质量除以总流体体积。当**压力损失模型**参数为 `Correlation for flow inside tubes` 时，由摩擦引起的压力损失取决于 Darcy 摩擦因子。

对于湍流，当 Reynolds 数高于**湍流下限 Reynolds 数**参数时，模块根据计算出的 Darcy 摩擦因子来计算由摩擦引起的压力损失。端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=fD,Am˙A1|m˙A1|2ρDHACS2(L+LAdd2),

其中：

- m˙A1 是通过端口 **A1** 的总流量。
- *fD,A* 是根据 Haaland 关联式的 Darcy 摩擦因子。当**局部阻力规格**参数为 `Aggregate equivalent length` 时，

  fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2,

  其中 *ε*R 是**内表面绝对粗糙度**参数的值。摩擦因子取决于 Reynolds 数，模块针对每种液体在两个端口处计算该值。
- *L* 是**每根管的总长度**参数的值。
- *L*Add 是**局部阻力总等效长度**参数的值，即一根管的等效长度，该管引入的损失与管中其他局部阻力引起的损失总和相同。
- *ACS* 是管横截面积。

端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=fD,Bm˙B1|m˙B1|2ρDHACS2(L+LAdd2),

其中 m˙B1 是通过端口 **B1** 的总流量。

当**局部阻力规格**参数为 `Aggregate equivalent length` 时，端口 **B1** 处的 Darcy 摩擦因子为：

fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2.

当**局部阻力规格**参数为 `Local loss coefficient` 时，端口 **A1** 和 **B1** 处的 Darcy 摩擦因子为

fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)

其中 *Clocalloss* 是**总局部损失系数**参数的值。

对于层流，当 Reynolds 数低于**层流上限 Reynolds 数**参数时，模块根据**Darcy 摩擦因子的层流摩擦常数**参数 *λ* 计算由摩擦引起的压力损失。当**管横截面**为 `Generic` 时，*λ* 是用户定义参数。否则，模块在内部计算该值。端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=λμm˙A12ρDH2ACS(L+LAdd2),

其中 *μ* 是流体动力粘度。端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=λμm˙B12ρDH2ACS(L+LAdd2).

对于过渡流，由粘性摩擦引起的压差是层流与湍流压力损失值之间的平滑混合。

**经验压力损失公式**

当**压力损失模型**设置为 `Pressure loss coefficient` 时，由粘性摩擦引起的压力损失用经验压力损失系数 *ξ* 计算。

端口 **A2** 与内部节点 I2 之间的压差为：

pA2−pI2=12ξm˙A2|m˙A2|2ρACS2.

端口 **B2** 与内部节点 I2 之间的压差为：

pB2−pI2=12ξm˙B2|m˙B2|2ρACS2.

### Thermal Liquid Correlations

**一个或多个管内流动的传热系数**

当热液体 **Flow geometry** 设置为 `Flow inside one or more tubes` 时，Nusselt 数根据 Gnielinski 关联式计算，方式与两相过冷液体或过热蒸气相同。有关更多信息，请参见 Heat Transfer Coefficient。

**横掠管束流动的传热系数**

当热液体 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，Nusselt 数基于 Hagen 数 Hg 计算，并取决于 **Tube bank grid arrangement** 设置：

Nu={0.404Lq1/3(Re+1Re+1000)0.1,Inline0.404Lq1/3,Staggered

其中：

Lq={1.18Pr(4lT/π−DlL)Hg(Re),Inline0.92Pr(4lT/π−DlD)Hg(Re),Staggered with lL≥D0.92Pr(4lTlL/π−D2lLlD)Hg(Re),Staggered with lL<D

- *D* 是 **Tube outer diameter**。
- *l*L 是 **Longitudinal tube pitch (along flow direction)**，即沿流动方向管中心之间的距离。*Flow direction* 指热液体流动。
- *l*T 是 **Transverse tube pitch (perpendicular to flow direction)**，如下图所示。横向节距是一行中两相流体管中心之间的距离。
- *l*D 是对角管间距，计算为 lD=(lT2)2+lL2。

有关计算 Hagen 数的更多信息，请参见 [3]。

对于两种管束网格排列类型，纵向和横向节距距离相同。

**带节距测量的两相流体管横截面**

**经验 Nusselt 数公式**

当 **Heat transfer coefficient model** 设置为 `Colburn equation` 或 **Flow geometry** 设置为 `Generic` 时，Nusselt 数由经验 Colburn 方程计算：

Nu=aRebPrc,

其中 *a*、*b* 和 *c* 是在 **Coefficients [a, b, c] for a\*Re^b\*Pr^c** 参数中定义的值。

**管内流动的压力损失**

当热液体 **Flow geometry** 参数为 `Flow inside one or more tubes` 时，压力损失的计算方式与两相流相同，使用热液体侧各自的 Darcy 摩擦因子、密度、质量流量和管长。有关更多信息，请参见 Pressure Loss。

**横掠管束流动的压力损失**

当热液体 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，Hagen 数用于计算由黏性摩擦引起的压力损失。端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=12μ2NRρD2Hg(Re),

其中：

- *μ*TL 是流体动力黏度。
- *N*R 是 **Number of tube rows along flow direction**。这是沿热液体流动方向的两相流体管排数。

端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=12μ2NRρD2Hg(Re).

**经验压力损失公式**

当 **Pressure loss model** 参数为 `Euler number per tube row` 或 **Flow geometry** 参数为 `Generic` 时，由黏性摩擦引起的压力损失通过压力损失系数（以 Euler 数 *Eu* 表示）计算：

Eu=ξNR,

其中 *ξ* 是经验压力损失系数。

端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=12NREum˙A1|m˙A1|2ρACS2.

端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=12NREum˙B1|m˙B1|2ρACS2.

### 壁面热质量

如果选择 **Enable wall thermal mass**，该模块会对换热器壁面热质量建模，这会引入壁面对温度或热通量变化的瞬态响应延迟。如果对热质量建模，壁面会在其边界内储存热量。这种热量储存会减缓稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率平衡为止。

如果选择 **Enable wall thermal mass**，壁面能量守恒为

(Mwallcp,wall2)dTwallTLdt=−QTL−Q(Mwallcp,wall2)dTwall2Pdt=−Q2P+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁温。该模块使用此值对瞬态响应建模。无法测量此值。

传递到每种流体的热量为

QTL=CTL(TwallTL−TinTL)(1−e−NTUTL)Q2P=C2P(Twall2P−Tin2P)(1−e−NTU2P)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容流率。

每一侧流体与壁面之间的传热单元数为

NTUTL=UTLATLCTLNTU2P=U2PA2PC2P

其中 *A* 是壁面表面积，*U* 是传热系数。

### 守恒方程

**两相流体**

两相流体中的总质量积聚率定义为：

dM2Pdt=m˙A2+m˙B2,

其中：

- *M2P* 是两相流体的总质量。
- m˙A2 是端口 **A2** 处流体的质量流量。
- m˙B2 是端口 **B2** 处流体的质量流量。

当流体通过端口流入模块时，流量为正。

能量守恒方程将比内能的变化与流体传递的热量联系起来：

M2Pdu2Pdt+u2P(m˙A2+m˙B2)=ϕA2+ϕB2−Q,

其中：

- *u*2P 是两相流体的比内能。
- *φ*A1 是端口 **A1** 处的能量流率。
- *φ*B1 是端口 **B1** 处的能量流率。
- *Q* 是传热率，当离开两相流体体积时为正。

**热液体**

热液体中的总质量积聚率定义为：

dMTLdt=m˙A1+m˙B1.

能量守恒方程为：

MTLduTLdt+uTL(m˙A1+m˙B1)=ϕA1+ϕB1+Q,

其中：

- *ϕ*A1 是端口 **A1** 处的能量流率。
- *ϕ*B1 是端口 **B1** 处的能量流率。

传入或传出热液体的热量 *Q*，等于从两相流体传出或传入两相流体的热量。
