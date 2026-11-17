---
type: simulink-block
title: 'Heat Exchanger (TL-MA)'
family: 'heat-exchangers'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Moist Air'
documentation_page: 'heatexchangertlma'
documentation_source_path: 'ref/heatexchangertlma.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger (TL-MA)

## 端口

### 守恒

### **A1** — 热液体端口 thermal liquid

与热液体关联的入口或出口端口。

### **B1** — 热液体端口 thermal liquid

与热液体关联的入口或出口端口。

### **A2** — 湿空气端口 moist air

与湿空气关联的入口或出口端口。

### **B2** — 湿空气端口 moist air

与湿空气关联的入口或出口端口。

### 输出

### **W** — 湿空气冷凝速率 physical signal

离开湿空气流的冷凝水速率，以 physical signal 形式返回。该端口的值不包括以水滴形式夹带的冷凝部分。冷凝物不会积聚在传热表面上。

## 参数

### 配置

### **流动布置** — 流动路径对齐 `Cross flow`（默认） | `Parallel flow` | `Counter flow`

热交换器两侧之间的流动路径对齐方式。可用的流动布置包括：

- `Parallel flow`。流动沿相同方向流动。
- `Counter flow`。流动彼此平行，方向相反。
- `Cross flow`。流动彼此垂直。

### **交叉流布置** — 每个流动通道中的热混合条件 `Thermal Liquid 1 unmixed & Moist Air 2 mixed`（默认） | `Both fluids unmixed` | `Thermal Liquid 1 mixed & Moist Air 2 unmixed` | `Both fluids mixed`

选择每种流体是否能在其通道中混合。混合流意味着流体沿流动路径移动时可在横向自由移动。非混合流意味着流体被限制为仅沿流动路径移动。例如，带翅片的一侧被视为非混合流。

#### 依赖关系

要启用此参数，请将 **流动布置** 设置为 `Cross flow`。

### **壁热阻** — 壁通过热传导对热流的阻力 `0 K/W`（默认） | positive scalar

分隔两种热交换器流体的界面壁的热阻。

### **端口 A1 处的横截面积** — 端口 A1 处的流通面积 `0.01 m^2`（默认） | positive scalar

热液体端口 **A1** 处的流通面积。

### **端口 B1 处的横截面积** — 端口 B1 处的流通面积 `0.01 m^2`（默认） | positive scalar

热液体端口 **B1** 处的流通面积。

### **端口 A2 处的横截面积** — 端口 A2 处的流通面积 `0.01 m^2`（默认） | positive scalar

湿空气端口 **A2** 处的流通面积。

### **端口 B2 处的横截面积** — 端口 B2 处垂直于流动的面积 `0.01 m^2`（默认） | positive scalar

湿空气端口 **B2** 处的流通面积。

### **启用壁热质量** — 对壁热质量建模的选项 `off`（默认） | `on`

是否对热交换器壁热质量建模。对壁热质量建模会引入壁对温度或热通量变化的瞬态响应延迟。如果清除 **启用壁热质量**，模块会假定壁足够薄，使得在传热的时间尺度上瞬态响应是瞬时的。

### **壁质量** — 热交换器壁质量 `1 kg`（默认） | positive scalar

热交换器壁的质量。模块使用此值计算壁热质量。

#### 依赖关系

要启用此参数，请选择 **启用壁热质量**。

### **壁比热** — 热交换器壁比热 `490 J/(K*kg)`（默认） | positive scalar

热交换器壁的比热。模块使用此值计算壁热质量。

#### 依赖关系

要启用此参数，请选择 **启用壁热质量**。

### 热液体 1

### **流动几何** — 热液体流动配置 `Flow inside one or more tubes`（默认） | `Flow perpendicular to bank of circular tubes` | `Generic`

热液体流动路径。流动可以在管束外部流动，也可以在单根管或多根管内部流动。您还可以基于经验值指定通用参数化。

### **管数** — 热液体管数 `25`（默认） | positive scalar

热液体管数。更多的管会由于粘性摩擦导致更高的压损，但会提供更大的传热表面积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`。

### **每根管的总长度** — 每根热液体管的总长度 `1 m`（默认） | positive scalar

每根热液体管的总长度。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`。

### **管横截面** — 管的横截面形状 `Circular`（默认） | `Rectangular` | `Annular` | `Generic`

单根管的横截面形状。设置为 `Generic` 可指定任意横截面几何。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`。

### **管内径** — 单根管的内径 `0.05 m`（默认） | positive scalar

单根管横截面的内径。横截面和直径沿管均匀一致。直径的大小会影响压损和传热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Circular`。

### **管宽** — 单根管的内宽 `0.05 m`（默认） | positive scalar

单根管横截面的内宽。横截面和宽度沿管均匀一致。宽度和高度会影响压损和传热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Rectangular`。

### **管高** — 单根管的内高 `0.05 m`（默认） | positive scalar

单根管横截面的内高。横截面和高度沿管均匀一致。宽度和高度会影响压损和传热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 参数化设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Rectangular`。

### **环形内径（传热表面）** — 环形横截面的较小直径 `0.05 m`（默认） | positive scalar

单根管环形横截面的较小直径。横截面和内径沿管均匀一致。内径会影响压损和传热计算。传热通过环形的内表面发生。

#### 依赖关系

要启用此参数，请将 **流动几何** 参数化设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Annular`。

### **环形外径** — 环形横截面的较大直径 `0.1 m`（默认） | positive scalar

单根管环形横截面的较大直径。横截面和外径沿管均匀一致。外径会影响压损和传热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Annular`。

### **每根管的横截面积** — 每根管内的流通面积 `0.002 m^2`（默认） | positive scalar

每根管的内部流通面积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Generic`。

### **用于压损的管横截面湿周** — 流体接触的管横截面周长 `0.15 m`（默认） | positive scalar

流体接触的管横截面周长。横截面和周长沿管均匀一致。此值用于压损计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Generic`。

### **用于传热的管横截面周长** — 用于传热计算的单根管周长 `0.15 m`（默认） | positive scalar

用于传热计算的管周长。这通常与管周长相同，但在诸如环形横截面的情况下，根据传热表面的不同，这可能只是内径或外径。横截面和管周长沿管均匀一致。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Generic`。

### **压损模型** — 计算粘性摩擦导致压损的方法 `Correlation for flow inside tubes`（默认） | `Euler number per tube row` | `Pressure loss coefficient` | `Correlation for flow over tube bank`

计算粘性摩擦导致压损的方法。不同的流动配置可使用不同的模型。设置为：

- `Correlation for flow inside tubes`。使用此设置可通过 Haaland 关联式计算压损。
- `Pressure loss coefficient`。使用此设置可基于经验损失系数计算压损。
- `Euler number per tube row`。使用此设置可基于经验 Euler 数计算压损。
- `Correlation for flow over tube bank`。使用此设置可基于 Hagen 数计算压损。

可用的压损模型取决于 **流动几何** 设置。

#### 依赖关系

当 **流动几何** 设置为 `Flow inside one or more tubes` 时，**压损模型** 可设置为：

- `Pressure loss coefficient`。
- `Correlation for flow inside tubes`。

当 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes` 时，**压损模型** 可设置为：

- `Correlation for flow over tube bank`。
- `Euler number per tube row`。

当 **流动几何** 设置为 `Generic` 时，**压损模型** 参数被禁用。压损通过 **压损系数, delta\_p/(0.5\*rho\*v^2)** 参数经验计算。

### **压损系数, delta\_p/(0.5\*rho\*v^2)** — 通道中所有压损的经验损失系数 `10`（默认） | positive scalar

通道中所有压损的经验损失系数。此值考虑壁面摩擦以及通道中弯头、弯曲和其他几何变化引起的局部损失。

损失系数可根据标称工作条件计算，或进行调整以拟合实验数据。其定义为：

ξ=Δp12ρv2,

其中 *Δp* 是压降，*ρ* 是热液体密度，*v* 是流速。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **流动几何** 设置为 `Flow inside one or more tubes`，且 **压损模型** 设置为 `Pressure loss coefficient`。
- **流动几何** 设置为 `Generic`。

### **局部阻力规格** — 量化压损的方法 `Aggregate equivalent length`（默认） | `Local loss coefficient`

量化 Haaland 关联式中压损的方法。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **压损模型** 设置为 `Correlation for flow inside tubes`。

### **局部阻力的总等效长度** — 每根管所有局部阻力的组合长度 `0.1 m`（默认） | positive scalar

每根管所有局部阻力的组合长度。此值是指与管中由弯头、三通或接头等阻力引起的所有局部损失之和产生相同压损的管道长度。组合长度越长，压损越大。模块在摩擦压损计算中会将此参数的值加到 **每根管的总长度** 参数中。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，将 **压损模型** 设置为 `Correlations for flow inside tubes`，并将 **局部阻力规格** 设置为 `Aggregate equivalent length`。

### **总局部损失系数** — 压损系数 `0.1`（默认） | positive scalar

系统上的局部压损系数。您可以使用此参数校准系统以匹配实验结果。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，将 **压损模型** 设置为 `Correlation for flow inside tubes`，并将 **局部阻力规格** 设置为 `Local loss coefficient`。

### **内表面绝对粗糙度** — 平均表面粗糙度高度 `15e-6 m`（默认） | positive scalar

管表面缺陷的平均高度。对于使用 Haaland 关联式计算的压损，较粗糙的壁会导致湍流区更大的压损。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将以下任一参数：

- **压损模型**
- **传热系数模型**

设置为 `Correlation for flow inside tubes`。

### **层流雷诺数上限** — 指示层流的最大雷诺数 `2000`（默认） | positive scalar

指示层流的最大雷诺数。在此值和 **湍流雷诺数下限** 之间，流态为过渡态。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将以下任一参数：

- **压损模型**
- **传热模型**

设置为 `Correlation for flow inside tubes`。

### **湍流雷诺数下限** — 指示湍流的最小雷诺数 `4000`（默认） | positive scalar

指示湍流的最小雷诺数。在此值和 **层流雷诺数上限** 之间，流态为层流和湍流之间的过渡态。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **压损模型** 设置为 `Correlation for flow inside tubes`。

### **Darcy 摩擦因子的层流摩擦常数** — 层流中粘性摩擦导致压损的系数 `64`（默认） | positive scalar

层流中粘性摩擦的压损方程中的系数。此参数也称为 *形状因子*。默认值对应于圆管横截面。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Correlation for flow inside tubes`，将 **管横截面** 设置为 `Generic`，并将 **压损模型** 设置为 `Correlation for flow inside tubes`。

### **传热系数模型** — 计算流体与壁之间传热系数的方法 `Correlation for flow over tube bank`（默认） | `Colburn equation` | `Correlation for flow inside tubes`

计算流体与壁之间传热系数的方法。可用设置为：

- `Colburn equation`。使用此设置可通过 Colburn 方程的用户定义变量 *a*、*b* 和 *c* 计算传热系数。
- `Correlation for flow over tube bank`。使用此设置可基于管束关联式并使用 Hagen 数计算传热系数。
- `Correlation for flow inside tubes`。使用此设置可通过 Gnielinski 关联式计算管道流动的传热系数。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为以下任一值：

- `Flow perpendicular to bank of circular tubes`。
- `Flow inside one or more tubes`。

### **a\*Re^b\*Pr^c 的系数 [a, b, c]** — Colburn 方程系数 `[0.023, 0.8, 0.33]`（默认）| 三元素向量

三元素向量，包含 Colburn 方程的经验系数。Colburn 方程是计算 Nusselt 数的公式。Colburn 方程的一般形式为：

Nu=aRe^bPr^c.

当 **传热系数模型** 设置为 **Colburn equation** 且 **流动几何** 设置为 `Flow inside one or more tubes`，或 **流动几何** 设置为 `Generic` 时，默认 Colburn 方程为：

Nu=0.023Re^0.8Pr^(1/3).

当 **传热系数模型** 设置为 **Colburn equation** 且 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes` 时，默认 Colburn 方程为：

Nu=0.27Re^0.63Pr^0.36.

#### 依赖关系

要启用此参数，请设置：

1. 将 **流动几何** 设置为以下任一项：

   - `Flow inside one or more tubes`
   - `Flow perpendicular to bank of circular tubes`

   并将 **传热系数模型** 设置为 `Colburn equation`。
2. 将 **流动几何** 设置为 `Generic`。

### **层流 Nusselt 数** — 层流流态下对流传热与导热传热之比 `3.66`（默认）| 正标量

层流流态下对流传热与导热传热之比。流体 Nusselt 数会影响传热速率，并取决于管横截面。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，将 **管横截面** 设置为 `Generic`，并将 **传热参数化** 设置为 `Correlation for flow inside tubes`。

### **管束网格排列** — 管束中管排的几何布置 `Inline`（默认）| `Staggered`

管束中管的对齐方式。管排可以与其相邻管排对齐，也可以交错排列。

- `Inline`：所有管排都直接位于彼此后方。
- `Staggered`：一个管排的管位于前一管排的管之间的间隙处。

管对齐方式会影响 Nusselt 数和传热速率。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **沿流动方向的管排数** — 管束中湿空气管排数 `5`（默认）| 正标量

管束中湿空气管排的数量。这些管排沿热液体流动方向排列。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **每个管排中的管段数** — 管束每一排中的湿空气管数 `5`（默认）| 正标量

管束每一排中的湿空气管数。该测量方向垂直于热液体流动方向。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **管排中每个管段的长度** — 每根湿空气管的长度 `1 m`（默认）| 正标量

跨一个管排的每根湿空气管的长度。管束中的所有管长度相同。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **管外径** — 湿空气管的外径 `0.05 m`（默认）| 正标量

湿空气管的外径。管的横截面沿管长均匀，因此直径处处恒定。该值会影响由于黏性摩擦引起的横掠管束流动中的损失。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **纵向管间距（沿流动方向）** — 湿空气管排之间的中心距 `0.15 m`（默认）| 正标量

沿热液体流动方向排列的湿空气管束的管中心之间的距离。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **横向管间距（垂直于流动方向）** — 一排中湿空气流体管之间的中心距 `0.15`（默认）| 正标量

一排湿空气管中管中心之间的距离。该测量方向垂直于热液体流动方向。更多信息请参阅传热系数。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **每排管的 Euler 数，delta\_p/(N\*0.5\*rho\*v^2)** — 管束每一排的 Euler 数 `10`（默认）| 正标量

一排管上压降的经验系数。Euler 数是压降与流体动量之比：

Eu=Δp/(N*0.5*ρ*v^2)，

其中 *N* 是 **沿流动方向的管排数**，*Δp* 是压降，*ρ* 是热液体密度，*v* 是流速。

每个管排位于垂直于热液体流动的平面内。

#### 依赖关系

要启用此参数，请设置以下任一项：

- 将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`，并将 **压力损失模型** 设置为 `Euler number per tube row`。
- 将 **流动几何** 设置为 `Generic`。

### **最小自由流通面积** — 入口与出口之间的最小总流通面积 `0.01 m^2`（默认）| 正标量

入口与出口之间的最小总横截流通面积。如果通道由多个管道、管、槽或沟槽组成，则该参数的值为最小流通面积点处最小面积之和。该参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则该参数的值是间隙之和最小的一个横截面中管间间隙之和。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Generic`。

### **不包括翅片的传热表面积** — 不包括翅片的传热表面总面积 `2 m^2`（默认）| 正标量

传热表面的总面积，不包括翅片。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Generic`。

### **换热器内热液体体积** — 换热器中热液体的总体积 `0.05 m^3`（默认）| 正标量

换热器中热液体的总体积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Generic`。

### **污垢系数** — 因污垢沉积引起的附加热阻 `0.1 m^2*K/kW`（默认）| 正标量

因壁面上的污垢层引起的附加热阻。在实际系统中，污垢沉积会随时间增长。然而，其增长足够缓慢，可假定在仿真期间保持不变。

### **翅片总表面积** — 所有翅片的传热表面积总和 `0 m^2`（默认）| 正标量

接触热液体的所有翅片两侧的传热表面积总和。例如，如果翅片为矩形，则表面积为矩形面积的两倍。

总传热表面积是通道表面积与有效翅片表面积之和，有效翅片表面积是 **翅片效率** 与 **翅片总表面积** 的乘积。

### **翅片效率** — 翅片的实际传热速率与理想传热速率之比 `0.5`（默认）| 范围 [0,1] 内的正标量

如果整个翅片都处于主传热表面温度时，接触热液体的翅片的实际传热量与理想传热量之比。

### **热液体初始压力** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的热液体压力。

### **热液体初始温度** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时热液体通道中的温度。该参数可以是标量或二元素向量。标量值表示通道中的平均初始温度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始温度。模块会在两个端口之间计算线性梯度。入口和出口端口根据初始流动方向确定。

### Moist Air 2

### **流动几何** — 湿空气流动配置 `Flow perpendicular to bank of circular tubes`（默认）| `Flow inside one or more tubes` | `Generic`

湿空气流动路径。流动可以在管组外部掠过，也可以在单根管或管组内部流动。您还可以基于经验值指定通用参数化。

### **管数** — 湿空气管数 `25`（默认）| 正标量

湿空气管数。更多的管会因黏性摩擦导致更高的压力损失，但会提供更大的传热表面积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`。

### **每根管的总长度** — 每根湿空气管的总长度 `1 m`（默认）| 正标量

每根湿空气管的总长度。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`。

### **管横截面** — 管的横截面形状 `Circular`（默认）| `Rectangular` | `Annular` | `Generic`

一根管的横截面形状。设置为 `Generic` 可指定任意横截面几何形状。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`。

### **管内径** — 单根管的内径 `0.05 m`（默认）| 正标量

一根管横截面的内径。横截面和直径沿管长均匀。直径大小会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Circular`。

### **管宽** — 单根管的内宽 `0.05 m`（默认）| 正标量

一根管横截面的内宽。横截面和宽度沿管长均匀。宽度和高度会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Rectangular`。

### **管高** — 单根管的内高 `0.05 m`（默认）| 正标量

一根管横截面的内高。横截面和高度沿管长均匀。宽度和高度会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 参数化设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Rectangular`。

### **环形内径（传热表面）** — 环形横截面的较小直径 `0.05 m`（默认）| 正标量

一根管的环形横截面的较小直径。横截面和内径沿管长均匀。内径会影响压力损失和传热计算。传热通过环形的内表面发生。

#### 依赖关系

要启用此参数，请将 **流动几何** 参数化设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Annular`。

### **环形外径** — 环形横截面的较大直径 `0.1 m`（默认）| 正标量

一根管的环形横截面的较大直径。横截面和外径沿管长均匀。外径会影响压力损失和传热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Annular`。

### **每根管的横截面积** — 每根管内的流通面积 `0.002 m^2`（默认）| 正标量

每根管的内部流通面积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Generic`。

### **用于压力损失的管横截面湿周** — 流体接触的管横截面周长 `0.15 m`（默认）| 正标量

流体接触的管横截面周长。横截面和周长沿管长均匀。该值用于压力损失计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Generic`。

### **用于传热的管横截面周长** — 用于传热计算的单根管周长 `0.15 m`（默认）| 正标量

用于传热计算的管周长。这通常与管周长相同，但在环形横截面等情况下，根据传热表面，这可能仅是内径或外径对应的周长。横截面和管周长沿管长均匀。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Generic`。

### **压力损失模型** — 计算黏性摩擦引起的压力损失的方法 `Correlation for flow inside tubes`（默认）| `Euler number per tube row` | `Pressure loss coefficient` | `Correlation for flow over tube bank`

计算黏性摩擦引起的压力损失的方法。不同流动配置可使用不同的模型。设置包括：

- `Correlation for flow inside tubes`。使用此设置可通过 Haaland 关联式计算压力损失。
- `Pressure loss coefficient`。使用此设置可基于经验损失系数计算压力损失。
- `Euler number per tube row`。使用此设置可基于经验 Euler 数计算压力损失。
- `Correlation for flow over tube bank`。使用此设置可基于 Hagen 数计算压力损失。

可用的压力损失模型取决于 **流动几何** 设置。

#### 依赖关系

当 **流动几何** 设置为 `Flow inside one or more tubes` 时，**压力损失模型** 可以设置为以下任一项：

- `Pressure loss coefficient`。
- `Correlation for flow inside tubes`。

当 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes` 时，**压力损失模型** 可以设置为以下任一项：

- `Correlation for flow over tube bank`。
- `Euler number per tube row`。

当 **流动几何** 设置为 `Generic` 时，**压力损失模型** 参数被禁用。压力损失使用 **压力损失系数，delta\_p/(0.5\*rho\*v^2)** 参数按经验计算。

### **压力损失系数，delta\_p/(0.5\*rho\*v^2)** — 通道中所有压力损失的经验损失系数 `10`（默认）| 正标量

通道中所有压力损失的经验损失系数。该值考虑了壁面摩擦以及通道中弯头、肘部和其他几何变化引起的局部损失。

损失系数可由额定工况计算得出，或调整以拟合实验数据。该系数定义为：

ξ=Δp/(0.5*ρ*v^2)，

其中 *Δp* 是压降，*ρ* 是湿空气密度，*v* 是流速。

#### 依赖关系

要启用此参数，请设置以下任一项：

- 将 **流动几何** 设置为 `Generic`。
- 将 **压力损失模型** 设置为 `Pressure loss coefficient`。

### **局部阻力规格** — 用于量化压力损失的方法 `Aggregate equivalent length` (default) | `Local loss coefficient`

用于量化 Haaland 关联式中压力损失的方法。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **压力损失模型** 设置为 `Correlation for flow inside tubes`。

### **局部阻力的总等效长度** — 每根管所有局部阻力的组合长度 `0.1 m` (default) | positive scalar

每根管所有局部阻力的组合长度。该值是指产生与管中所有由弯头、三通或接头等阻力导致的次要损失之和相同压力损失的管道长度。组合长度越长，压力损失越大。在计算摩擦导致的压力损失时，模块将此参数的值加到 **每根管的总长度** 参数中。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，将 **压力损失模型** 设置为 `Correlations for flow inside tubes`，并将 **局部阻力规格** 设置为 `Aggregate equivalent length`。

### **总局部损失系数** — 压力损失系数 `0.1` (default) | positive scalar

系统上的局部压力损失系数。您可以使用此参数校准系统以匹配实验结果。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，将 **压力损失模型** 设置为 `Correlation for flow inside tubes`，并将 **局部阻力规格** 设置为 `Local loss coefficient`。

### **内表面绝对粗糙度** — 平均表面粗糙度高度 `15e-6 m` (default) | positive scalar

管表面缺陷的平均高度。对于使用 Haaland 关联式计算的压力损失，壁面越粗糙，湍流区中的压力损失越大。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将以下任一项设置为 `Correlation for flow inside tubes`：

- **压力损失模型**
- **传热系数模型**

### **层流上雷诺数极限** — 指示层流的最大雷诺数 `2000` (default) | positive scalar

指示层流的最大雷诺数。在此值与 **湍流下雷诺数极限** 之间，流态为过渡态。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **压力损失模型** 设置为 `Correlation for flow inside tubes`。

### **湍流下雷诺数极限** — 指示湍流的最小雷诺数 `4000` (default) | positive scalar

指示湍流的最小雷诺数。在此值与 **层流上雷诺数极限** 之间，流态为层流和湍流之间的过渡态。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **压力损失模型** 设置为 `Correlation for flow inside tubes`。

### **Darcy 摩擦因子的层流摩擦常数** — 层流中黏性摩擦导致的压力损失系数 `64` (default) | positive scalar

层流中黏性摩擦的压力损失方程中的系数。此参数也称为 *形状因子*。默认值对应于圆管横截面。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Correlation for flow inside tubes`，将 **管横截面** 设置为 `Generic`，并将 **压力损失模型** 设置为 `Correlation for flow inside tubes`。

### **传热系数模型** — 计算流体与壁面之间传热系数的方法 `Correlation for flow over tube bank` (default) | `Colburn equation` | `Correlation for flow inside tubes`

计算流体与壁面之间传热系数的方法。可用设置包括：

- `Colburn equation`。使用此设置通过用户定义的变量 *a*、*b* 和 *c* 按 Colburn 方程计算传热系数。
- `Correlation for flow over tube bank`。使用此设置基于管束关联式并使用 Hagen 数计算传热系数。
- `Correlation for flow inside tubes`。使用此设置通过 Gnielinski 关联式计算管道流的传热系数。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为以下任一项：

- `Flow perpendicular to bank of circular tubes`。
- `Flow inside one or more tubes`。

### **用于 a\*Re^b\*Pr^c 的系数 [a, b, c]** — Colburn 方程系数 `[0.023, 0.8, 0.33]` (default) | three-element vector

three-element vector，包含 Colburn 方程的经验系数。Colburn 方程是计算 Nusselt 数的公式。Colburn 方程的一般形式为：

Nu=aRebPrc.

当 **传热系数模型** 设置为 `Colburn equation`，且 **流动几何** 设置为 `Flow inside one or more tubes`，或 **流动几何** 设置为 `Generic` 时，默认 Colburn 方程为：

Nu=0.023Re0.8Pr1/3.

当 **传热系数模型** 设置为 `Colburn equation`，且 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes` 时，默认 Colburn 方程为：

Nu=0.27Re0.63Pr0.36.

#### 依赖关系

要启用此参数，请设置：

1. **流动几何** 为以下任一项：

   - `Flow inside one or more tubes`
   - `Flow perpendicular to bank of circular tubes`

   并将 **传热系数模型** 设置为 `Colburn equation`。
2. **流动几何** 设置为 `Generic`。

### **层流 Nusselt 数** — 层流区中对流与传导传热之比 `3.66` (default) | positive scalar

层流区中对流与传导传热之比。流体 Nusselt 数影响传热速率，并取决于管横截面。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，将 **管横截面** 设置为 `Generic`，并将 **传热参数化** 设置为 `Correlation for flow inside tubes`。

### **管束网格排列** — 管束中热液体行的几何布置 `Inline` (default) | `Staggered`

管束中管的排列。各行与其相邻行对齐或交错排列。

- `Inline`：所有管排直接位于彼此后方。
- `Staggered`：一个管排的管位于前一个管排的管之间的间隙处。

管排列会影响 Nusselt 数和传热速率。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **沿流动方向的管排数** — 管束中热液体管排数 `5` (default) | positive scalar

管束中热液体流体管排数。这些管排沿湿空气流动方向排列。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **每个管排中的管段数** — 管束每一排中热液体管数 `5` (default) | positive scalar

管束每一排中热液体管数。该测量垂直于湿空气流。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **管排中每个管段的长度** — 每根热液体管的长度 `1 m` (default) | positive scalar

跨一个管排的每根热液体管的长度。管束中的所有管长度相同。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **管外径** — 单根热液体管的外径 `0.05 m` (default) | positive scalar

热液体管的外径。横截面沿管均匀，因此直径始终不变。该值会影响由于黏性摩擦而流过管束时的损失。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **纵向管间距（沿流动方向）** — 热液体管排之间的中心距 `0.15 m` (default) | positive scalar

热液体管束的管中心之间的距离，沿湿空气流动方向对齐。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **横向管间距（垂直于流动方向）** — 一排中热液体管之间的中心距 `0.15 m` (default) | positive scalar

一排热液体管中管中心之间的距离。该测量垂直于湿空气流动方向。有关更多信息，请参见 Heat Transfer Coefficients。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。

### **每管排欧拉数，delta\_p/(N\*0.5\*rho\*v^2)** — 管束每一排的欧拉数 `10` (default) | positive scalar

单管排压降的经验系数。欧拉数是压降与流体动量之比：

Eu=ΔpN12ρv2,

其中 *N* 是 **沿流动方向的管排数**，*Δp* 是压降，*ρ* 是湿空气混合物密度，*v* 是流速。

每个管排位于垂直于湿空气流的平面中。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`，并将 **压力损失模型** 设置为 `Euler number per tube row`。

### **最小自由流动面积** — 入口与出口之间最小总流动面积 `0.01 m^2` (default) | positive scalar

入口与出口之间最小总横截流动面积。如果通道是管道、管、槽或沟的集合，则此参数的值是最小流动面积点处最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是一个横截面中管间间隙之和最小处的间隙之和。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Generic`。

### **不带翅片的传热表面积** — 不包括翅片的传热表面总面积 `2 m^2` (default) | positive scalar

传热表面的总面积，不包括翅片。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Generic`。

### **换热器内湿空气体积** — 换热器中湿空气的总体积 `0.05 m^3` (default) | positive scalar

换热器中湿空气的总体积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Generic`。

### **污垢系数** — 因污垢沉积物导致的附加热阻 `0.1 m^2*K/kW` (default) | positive scalar

因壁面表面上的污垢层导致的附加热阻。在实际系统中，污垢沉积物会随时间增长。但是，增长足够慢，可在仿真期间假定为常数。

### **总翅片表面积** — 所有翅片的总传热表面积 `0 m^2` (default) | positive scalar

接触湿空气的所有翅片两侧的总传热表面积。例如，如果翅片是矩形的，则表面积为矩形面积的两倍。

总传热表面积是通道表面积与有效翅片表面积之和，有效翅片表面积是 **翅片效率** 与 **总翅片表面积** 的乘积。

### **翅片效率** — 翅片的实际传热率与理想传热率之比 `0.5` (default) | positive scalar in the range [0,1]

如果整个翅片处于主传热表面温度，则通过接触湿空气的翅片的实际传热与理想传热之比。

### **初始湿空气压力** — 仿真开始时的湿空气压力 `0.101325 MPa` (default) | positive scalar

仿真开始时的湿空气压力。

### **初始湿空气温度** — 仿真开始时的温度 `293.15 K` (default) | positive scalar | two-element vector

仿真开始时湿空气流体通道中的温度。此参数可以是标量或 two-element vector。标量值表示通道中的平均初始温度。向量值表示入口和出口处的初始温度，形式为 [`inlet`, `outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

### **初始湿度规格** — 湿度规格 `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

指定换热器湿空气侧初始湿度的方法。

### **初始湿空气相对湿度** — 仿真开始时的相对湿度 `0.5` (default) | positive scalar in the range of [0,1] | two-element vector

仿真开始时湿空气通道中的相对湿度。相对湿度是水蒸气分压与水蒸气饱和压力之比，或水蒸气摩尔分数与饱和时水蒸气摩尔分数之比。

此参数可以是标量或 two-element vector。标量值表示通道中的平均初始相对湿度。向量值表示入口和出口处的初始相对湿度，形式为 [`inlet`, `outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **初始湿度规格** 设置为 `Relative humidity`。

### **初始湿空气比湿度** — 仿真开始时的比湿度 `0.01` (default) | positive scalar in the range of [0,1] | two-element vector

仿真开始时湿空气通道中的比湿度。比湿度是水蒸气质量与包括水蒸气、微量气体和干空气的总质量之比。

此参数可以是标量或 two-element vector。标量值表示通道中的平均初始比湿度。向量值表示入口和出口处的初始比湿度，形式为 [`inlet`, `outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **初始湿度规格** 设置为 `Specific humidity`。

### **初始湿空气水蒸气摩尔分数** — 仿真开始时水蒸气的摩尔分数 `0.01`（默认） | 取值范围 [0,1] 的正标量 | 双元素向量

仿真开始时湿空气通道中水蒸气的摩尔分数。水蒸气摩尔分数相对于水蒸气、示踪组分和干空气的总摩尔量。

此参数可以是标量或双元素向量。标量值表示通道中的平均初始蒸气摩尔分数。向量值表示入口和出口处的初始蒸气摩尔分数，形式为 [`inlet`, `outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **初始湿度设定** 设置为 `Mole fraction`。

### **初始湿空气湿度比** — 仿真开始时的湿度比 `0.01`（默认） | 取值范围 [0,1] 的正标量 | 双元素向量

仿真开始时湿空气通道中的湿度比。湿度比是水蒸气质量与干空气和示踪气体质量之比。

此参数可以是标量或双元素向量。标量值表示通道中的平均初始湿度比。向量值表示入口和出口处的初始湿度比，形式为 [`inlet`, `outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **初始湿度设定** 设置为 `Humidity ratio`。

### **初始湿空气湿球温度** — 仿真开始时的湿球温度 `287 K`（默认） | 取值范围 [0,1] 的正标量

仿真开始时的湿球温度。模块使用此值计算湿度。

此参数可以是标量或双元素向量。标量值表示通道中的平均初始湿球温度。向量值表示入口和出口处的初始湿球温度，形式为 [`inlet`, `outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **初始湿度设定** 设置为 `Wet-bulb temperature`。

### **初始示踪气体设定** — 示踪气体的测量类型 `Mass fraction`（默认） | `Mole fraction`

示踪气体的测量类型。

### **初始湿空气示踪气体质量分数** — 湿空气通道中示踪气体的量 `0.001`（默认） | 取值范围 [0,1] 的正标量 | 双元素向量

仿真开始时湿空气通道中示踪气体的量（按质量分数计）。质量分数相对于水蒸气、示踪气体和干空气的总质量。

此参数可以是标量或双元素向量。标量值表示通道中的平均示踪气体质量分数。向量值表示入口和出口处的初始示踪气体质量分数，形式为 [`inlet`, `outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

如果 Moist Air Properties (MA) 模块中的 **示踪气体模型** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **初始示踪气体设定** 设置为 `Mass fraction`。

### **初始湿空气示踪气体摩尔分数** — 仿真开始时示踪气体的摩尔分数 `0.001`（默认） | 取值范围 [0,1] 的正标量 | 双元素向量

仿真开始时湿空气通道中示踪气体的量（按摩尔分数计）。摩尔分数相对于水蒸气、示踪气体和干空气的总摩尔数。

此参数可以是标量或双元素向量。标量值表示通道中的平均示踪气体摩尔分数。向量值表示入口和出口处的初始示踪气体摩尔分数，形式为 [`inlet`, `outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

如果 Moist Air Properties (MA) 模块中的 **示踪气体模型** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **初始示踪气体设定** 设置为 `Mole fraction`。

### **水滴与湿空气的初始质量比** — 水滴与湿空气之比 `0`（默认） | 正标量

水滴与湿空气的初始质量比。

### **饱和时的相对湿度** — 凝结的相对湿度点 `1`（默认） | 取值范围 [0,1] 的正标量

凝结的相对湿度点。高于此值时发生凝结。大于 1 的值表示过饱和蒸气。

### **水蒸气凝结时间常数** — 凝结的时间尺度 `1e-3 s`（默认） | 正标量

过饱和湿空气体积通过凝结析出过量湿气而恢复到饱和的特征时间尺度。

### **水滴蒸发时间常数** — 蒸发的时间尺度 `1e-3 s`（默认） | 正标量

水滴蒸发为蒸气的特征时间尺度。

### **夹带为水滴的凝结物分数** — 水滴中凝结物的分数 `1`（默认） | 取值范围 [0,1] 的标量

湿空气中夹带为水滴的凝结物分数。

## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Moist Air

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2025a: 对换热器壁面的热质量建模

选择 **壁面热动态** 以对换热器壁面的热质量建模。

### R2024b: 对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **启用夹带水滴**。

### R2024a: 更新自由流通面积计算

当 **流动几何** 为 `Flow perpendicular to bank of circular tubes` 时，模块现在使用不同方法计算自由流通面积。如果 **每个管排中的管段数** 参数值较小，模块可能会显示压力损失和传热略有增加。

### R2024a: 新的湿度设定选项

模块为 **初始湿度设定** 参数新增了一个选项。此选项称为 `Wet-bulb temperature`，允许您以湿球温度形式输入数据。

### R2023a: 使用局部损失系数对附加压力损失建模

将 **局部阻力设定** 参数设置为 `Local loss coefficient`，以指定量化压力损失的新方法。此选项允许您对超出管道长度所致损失的附加摩擦损失建模。

## 描述

对湿空气网络和热液体网络之间的热交换进行建模

Heat Exchanger (TL-MA) 模块对热交换器建模，该热交换器具有一个湿空气网络（在端口 **A2** 和 **B2** 之间流动）和一个热液体网络（在端口 **A1** 和 **B1** 之间流动）。流体流可采用平行流、逆流或错流配置排列。

热液体-湿空气热交换器不适合制冷冷却系统。有关可用于制冷应用的热交换器，请参见 Condenser Evaporator (2P-MA) 或 Condenser Evaporator (TL-2P)。

您可以将湿空气侧建模为管内流动、绕热液体管束流动，或通过经验性的通用参数化建模。湿空气侧包含空气、示踪气体和水蒸气，水蒸气在整个热交换循环中可能凝结。模块模型考虑了水在传热表面上凝结时释放的潜热。该液层不会在表面上积聚，并假定其从下游湿空气流中完全移除。湿气凝结速率作为物理信号在端口 **W** 返回。

模块使用效能-NTU (E-NTU) 方法对通过共享壁面的传热建模。还会对换热器壁面上的污垢建模；污垢会增加热阻并降低两种流体之间的热交换。您还可以选择对湿空气侧和热液体侧的翅片建模。换热器两侧由黏性摩擦引起的压力损失可以通过解析方法或通用参数化建模，您可以使用后者根据自己的数据进行调整。

您可以将热液体侧建模为管内流动、绕湿空气管束流动，或通过经验性的通用参数化建模。

### 热交换器配置

热交换器效能基于所选的热交换器配置、流体属性、换热器每一侧的管几何和流动配置，以及翅片的使用和尺寸。

**流动布置**

**流动布置** 参数指定两侧之间的相对流动路径：

- `Parallel flow` 表示流体沿相同方向流动。
- `Counter flow` 表示流体平行但沿相反方向流动。
- `Cross flow` 表示流体彼此垂直流动。

**热混合**

当 **流动布置** 设置为 `Cross flow` 时，使用 **错流布置** 参数来指示热液体流或湿空气流是否被折流板或壁面分隔成多个路径。如果没有这些分隔，流动可以自由混合，并被视为 *混合*。在错流布置中，两种流体、一种流体或两种流体都不混合。混合会使流体温度沿第二流体的流动方向均匀化，并沿垂直于第二流体流动的方向变化。

非混合流体的温度沿第二流体的流动路径及其垂直方向均会变化。

**错流配置示例**

请注意，仿真期间的流动方向不会影响所选的流动布置设置。模块上的端口不反映物理热交换系统中端口的物理位置。

所有流动布置均为单程，这意味着流体在换热器中不会多次转向以增加传热点。要对多程热交换器建模，您可以将多个 Heat Exchanger (TL-MA) 模块串联或并联布置。

例如，要在湿空气侧实现双程配置，并在热液体侧实现单程配置，您可以将湿空气侧串联，并将热液体侧并联连接到同一输入（例如两个 Mass Flow Rate Source 模块，各自具有总质量流量的一半），如下所示。

**流动几何**

**流动几何** 参数将相应对话框选项卡中流体的流动布置设置为在管或管束内部，或者垂直于管束。您还可以指定经验性的通用配置。

当 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes` 时，使用 **管束网格布置** 参数将另一种流体的管束排列定义为 `Inline` 或 `Staggered`。下图中的红色向下箭头表示在管束外部流动的流体方向。Inline 图还显示了 **沿流动方向的管排数** 和 **每个管排中的管段数** 参数。此处，*流动方向* 指相应对话框选项卡中的流体，*管* 指另一种流体的管道。**管排中每个管段的长度** 参数在 Staggered 图中指示。

一次只能有一种流体将 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes`。另一种流体必须配置为 `Flow inside one or more tubes` 或 `Generic`。如果两种流体的 **流动几何** 都设置为 `Flow perpendicular to bank of circular tubes`，您将收到错误。

**翅片**

当 **总翅片表面积** 参数为 `0 m^2` 时，热交换器配置没有翅片。翅片增加用于传热的额外表面积。每个流体侧都有单独的翅片面积和描述该流体中翅片的参数。例如，当热液体在管内流动且湿空气在管外流动时，**Thermal Liquid 1** 部分中的 **总翅片表面积** 和 **翅片效率** 参数描述伸入管内的翅片。**Moist Air 2** 部分中的 **总翅片表面积** 和 **翅片效率** 参数描述管外的翅片。

### Effectiveness-NTU Heat Transfer

传热速率基于两种流体的平均属性计算。

对流传热为

Q=ϵCMin(TIn,TL−TIn,MA),

其中：

- *C*Min 是两种流体热容率中较小的一个。热容率是流体比热 *c*p 与流体质量流量的乘积。*C*Min 始终为正。
- *T*In,TL 是热液体的入口温度。
- *T*In,MA 是湿空气的入口温度。
- *ε* 是换热器效能。

效能是热容率和传热单元数 *NTU* 的函数，并且还随换热器流动布置变化，这在 Effectiveness by Flow Arrangement 中有更详细讨论。*NTU* 计算如下：

NTU=1CMinR,

其中 *R* 是两股流体之间的总热阻，由对流、传导以及管壁上的任何污垢导致：

R=1UTLATh,TL+FTLATh,TL+RW+FMAATh,MA+1UMAATh,MA,

并且其中：

- *U* 是相应流体的对流传热系数。该系数在 Heat Transfer Coefficients 中有更详细讨论。
- *F* 分别是热液体侧或湿空气侧的 **污垢系数**。
- *R*W 是 **通过传热表面的热阻**。
- *A*Th 是换热器相应侧的传热表面积。*A*Th 是壁面表面积 *A*W 与 **总翅片表面积** *A*F 之和：

  ATh=AW+ηFAF,

  其中 *η*F 是 **翅片效率**。

模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

**按流动布置的效能**

换热器效能根据其流动配置和每种流体的混合情况而变化。

- 当 **流动布置** 设置为 `Parallel flow` 时：

  ϵ=1−exp[−NTU(1+CR)]1+CR
- 当 **流动布置** 设置为 `Counter flow` 时：

  ϵ=1−exp[−NTU(1−CR)]1−CRexp[−NTU(1−CR)]
- 当 **流动布置** 设置为 `Cross flow` 且 **横流布置** 设置为 `Both fluids unmixed` 时：

  ϵ=1−exp{NTU0.22CR[exp(−CRNTU0.78)−1]}
- 当 **流动布置** 设置为 `Cross flow` 且 **横流布置** 设置为 `Both fluids mixed` 时：

  ϵ=[11−exp(−NTU)+CR1−exp(−CRNTU)−1NTU]−1

当一种流体混合而另一种流体不混合时，效能方程取决于流体的相对热容率。当 **流动布置** 设置为 `Cross flow` 且 **横流布置** 设置为 `Thermal Liquid 1 mixed & Moist Air 2 unmixed` 或 `Thermal Liquid 1 unmixed & Moist Air 2 mixed` 时：

- 当具有 Cmax 的流体混合且具有 Cmin 的流体不混合时：

  ϵ=1CR(1−exp{−CR{1−exp(−NTU)}})
- 当具有 Cmin 的流体混合且具有 Cmax 的流体不混合时：

  ϵ=1−exp{−1CR[1−exp(−CRNTU)]}

*C*R 表示两种流体的热容率之比：

CR=CMinCMax.

### 传导传热

某个区域内的传导传热为

Qcond=Tout,TL−Tout,MARcond,

其中：

- *Tout,TL* 是热液体的区域出口温度。
- *Tout,MA* 是湿空气的区域出口温度。
- *Rcond* 是两股流体之间的总传导热阻，

  Rcond=DhkTLAW,TL+FTLAW,TL+RW+FMAAW,MA+DhkMAAW,MA,

  其中：

  - *AW* 是壁面表面积。
  - *k* 是每种流体的导热系数。
  - *DH* 是水力直径。

总传热是对流传热与传导传热之和。与对流传热相比，传导传热可忽略不计。当流量为零时，对流传热也为零。但是，由于对流和传导传热彼此独立运行，即使对流传热为零，仍然存在传导传热。

### 冷凝

在湿空气侧，传热表面上可能形成一层冷凝物。该液体层会影响湿空气与热液体之间传递的热量。上文的 E-NTU 传热方程针对 *干* 传热给出。为修正冷凝的影响，还需使用下面列出的湿参数额外计算 E-NTU 方程。两个计算得到的热流量中，导致湿空气侧冷却量更大的那个用于热计算 [1] [2]。要使用此方法，假定 Lewis 数接近 1，这对湿空气成立 [1][2]。

**用于传热速率计算的 E-NTU 量**

|  | 干计算 | 湿计算 |
| --- | --- | --- |
| 湿空气区域入口温度 | *Tin,MA* | *Tin,wb,MA* |
| 热容率 | m˙¯MAc¯p,MA | m˙¯MAc¯eq,MA |
| 传热系数 | *UMA* | UMAc¯eq,MAc¯p,MA |

其中：

- *Tin,MA* 是湿空气入口温度。
- *Tin,wb,MA* 是与 *Tin,MA* 相关联的湿空气湿球温度。
- m˙¯MA 是干空气质量流量。
- c¯p,MA 是单位质量干空气的湿空气热容。
- c¯eq,MA 是等效热容。*等效热容* 是湿空气比焓（每单位干空气）h¯MA 在饱和湿空气条件下随温度的变化：

  c¯eq,MA=(∂h¯MA∂TMA)s.

离开湿空气质量流量的冷凝水蒸气的质量流量取决于湿空气入口与通道壁之间的相对湿度以及换热器 NTU：

m˙cond=−m˙¯MA(Wwall,MA−Win,MA)(1−e−NTUMA),

其中：

- *W*wall,MA 是传热表面处的湿度比。
- *W*in,MA 是湿空气流入口处的湿度比。
- *NTU*MA 是湿空气侧的传热单元数，计算如下：

  NTUMA=UMAc¯eq,MAc¯p,MAATh,MAm˙¯MAc¯eq,MA.

与水蒸气冷凝相关的能量流基于水蒸气比焓 *h*water, wall 与水的汽化比焓 *h*fg 之差：

ϕCond=m˙cond(hwater,wall−hfg).

假定冷凝物不会积聚在传热表面上，并且不会影响诸如管径之类的几何参数。

### 传热系数

以下方程适用于热液体侧和湿空气侧，并使用各自的流体属性。

**管内流动**

对流传热系数根据流体 Nusselt 数变化：

U=NukDH,

其中：

- *Nu* 是平均 Nusselt 数，取决于流态。
- *k* 是流体导热系数。
- *D*H 是管水力直径。

对于湍流，Nusselt 数使用 Gnielinski 关联式计算：

Nu=fD8(Re−1000)Pr1+12.7f8(Pr2/3−1),

其中：

- *Re* 是流体 Reynolds 数。
- *Pr* 是流体 Prandtl 数。

对于层流，Nusselt 数由 **层流 Nusselt 数** 参数设置。

对于过渡流，Nusselt 数是层流与湍流 Nusselt 数之间的混合。

**横掠管束的流动**

当 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes` 时，Nusselt 数基于 Hagen 数 Hg 计算，并取决于 **管束网格布置** 设置：

Nu={0.404Lq1/3(Re+1Re+1000)0.1,Inline0.404Lq1/3,Staggered

其中

Lq={1.18Pr(4lT/π−DlL)Hg(Re),Inline0.92Pr(4lT/π−DlD)Hg(Re),Staggered with lL≥D0.92Pr(4lTlL/π−D2lLlD)Hg(Re),Staggered with lL<D

- *D* 是 **管外径**。
- *lL* 是 **纵向管间距（沿流动方向）**，即沿流动方向的管中心之间的距离。*流动方向* 是外部流体的流动方向。
- *lT* 是 **横向管间距（垂直于流动方向）**，即另一流体一行中管中心之间的距离。
- *l*D 是对角管间距，计算为 lD=(lT2)2+lL2。

有关计算 Hagen 数的更多信息，请参见 [6]。

测量值 *l*L 和 *l*T 如下方管束横截面所示。对于两种网格管束布置类型，这些距离相同。

**带间距测量值的管道横截面**

**经验 Nusselt 数公式**

当 **传热系数模型** 参数设置为 `Colburn equation` 或当 **流动几何** 设置为 `Generic` 时，Nusselt 数由经验 Colburn 方程计算：

Nu=aRebPrc,

其中 *a*、*b* 和 *c* 在 **用于 a\*Re^b\*Pr^c 的系数 [a, b, c]** 参数中定义。

### 压力损失

以下方程适用于热液体侧和湿空气侧，并使用各自的流体属性。

**管内流动**

由黏性摩擦引起的压力损失随流态和配置而变化。

对于湍流，当 Reynolds 数高于 **湍流下限 Reynolds 数** 参数，并且当 **压力损失模型** 设置为 `Correlations for flow inside tubes` 时，由摩擦引起的压力损失以 Darcy 摩擦因子表示计算。

对于热液体侧，端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=fD,Am˙A1|m˙A1|2ρDHACS2(L+LAdd2),

其中：

- m˙A1 是通过端口 **A1** 的总流量。
- *fD,A* 是根据 Haaland 关联式得到的 Darcy 摩擦因子。当 **局部阻力设定** 参数为 `Aggregate equivalent length` 时，

  fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2,

  其中 *ε*R 是热液体管道的 **内表面绝对粗糙度**。摩擦因子取决于 Reynolds 数，模块会为每种液体计算两个端口处的该值。
- *L* 是热液体侧的 **每根管的总长度**。
- *L*Add 是热液体侧的 **局部阻力的总等效长度**，即一根管子的等效长度，该长度引入的损失与管中其他局部阻力造成的损失总和相同。
- *A*CS 是管的总横截面积。

端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=fD,Bm˙B1|m˙B1|2ρDHACS2(L+LAdd2),

其中 m˙B1 是通过端口 **B1** 的总流量。

当 **局部阻力设定** 参数为 `Aggregate equivalent length` 时，端口 **B1** 处的 Darcy 摩擦因子为：

fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2.

当 **局部阻力设定** 参数为 `Local loss coefficient` 时，端口 **A1** 和 **B1** 处的 Darcy 摩擦因子为

fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)

其中 *Clocalloss* 是 **总局部损失系数** 参数的值。

对于层流，当 Reynolds 数低于 **层流上限 Reynolds 数** 参数，并且当 **压力损失模型** 设置为 `Correlations for flow inside tubes` 时，模块根据 **Darcy 摩擦因子的层流摩擦常数** 参数 *λ* 计算由摩擦引起的压力损失。当 **管横截面** 为 `Generic` 时，*λ* 是用户定义的参数。否则，模块在内部计算该值。

端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=λμm˙A12ρDH2ACS(L+LAdd2),

其中 μ 是流体动力黏度。端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=λμm˙B12ρDH2ACS(L+LAdd2).

对于过渡流，当 **压力损失模型** 设置为 `Correlations for flow inside tubes` 时，由黏性摩擦引起的压差是层流和湍流压力损失值之间的平滑混合。

**管内流动的经验公式**

当 **压力损失模型** 设置为 `Pressure loss coefficient` 或当 **流动几何** 设置为 `Generic` 时，由黏性摩擦引起的压力损失使用经验压力损失系数 *ξ* 计算。相同的方程适用于湿空气侧和热液体侧，并使用各自的流体属性。

对于热液体侧，端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=12ξm˙A1|m˙A1|2ρACS2.

端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=12ξm˙B1|m˙B1|2ρACS2.

**横掠管束流动的压力损失**

当 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes` 时，Hagen 数用于计算由黏性摩擦引起的压力损失。相同的方程适用于湿空气侧和热液体侧，并使用各自的流体属性。

对于湿空气侧，端口 **A2** 与内部节点 I2 之间的压差为：

pA2−pI2=12μ2NRρD2Hg(Re),

其中：

- *μ* 是湿空气流体动力黏度。
- *N*R 是 **沿流动方向的管排数**。当湿空气在管束外部流动时，这是沿湿空气流动方向的热液体管排数。

端口 **B2** 与内部节点 I2 之间的压差为：

pB2−pI2=12μ2NRρD2Hg(Re).

**横掠管流动的经验公式**

当 **压力损失模型** 设置为 `Euler number per tube row` 或当 **流动几何** 设置为 `Generic` 时，由黏性摩擦引起的压力损失使用压力损失系数以 Euler 数 *Eu* 表示计算：

Eu=ξNR,

其中 *ξ* 是经验压力损失系数。

端口 **A2** 与内部节点 I2 之间的压差为：

pA2−pI2=12NREum˙A2|m˙A2|2ρACS2.

端口 **B2** 与内部节点 I2 之间的压差为：

pB2−pI2=12NREum˙B2|m˙B2|2ρACS2.

### 壁面热质量

如果选择 **启用壁面热质量**，模块会建模换热器壁面热质量，这会引入壁面对温度或热流变化瞬态响应的延迟。如果建模热质量，壁面会在其边界内存储热量。这种热量存储会减慢稳态之间的过渡，使得一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流量达到平衡。

如果选择 **启用壁面热质量**，壁面能量守恒为

(Mwallcp,wall2)dTwallTLdt=−QTL−Q(Mwallcp,wall2)dTwallMAdt=−QMA+Q

其中：

- *Mwall* 是 **壁面质量** 参数的值。
- *cp,wall* 是 **壁面比热** 参数的值。
- *Twall* 是每一侧的有效壁面温度。模块使用该值来建模瞬态响应。无法测量该值。

传递到每种流体的热量为

QTL=CTL(TwallTL−TinTL)(1−e−NTUTL)QMA=CMA(TwallMA−TinMA)(1−e−NTUMA)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容率。

每一侧流体与壁面之间的传热单元数为

NTUTL=UTLATLCTLNTUMA=UMAAMACMA

其中 *A* 是壁面表面积，*U* 是传热系数。

### 守恒方程

**Thermal Liquid**

热液体的总质量累积速率定义为：

dMTLdt=m˙A1+m˙B1,

其中：

- *MTL* 是热液体的总质量。
- m˙A1 是端口 **A1** 处流体的质量流量。
- m˙B1 是端口 **B1** 处流体的质量流量。

当流体通过端口流入模块时，流量为正。

能量守恒方程将比内能的变化与流体传递的热量关联起来

MTLduTLdt+uTL(m˙A1+m˙B1)=ϕA1+ϕB1−Q,

其中：

- *uTL* 是热液体的比内能。
- *φA1* 是端口 **A1** 处的能量流率。
- *φB1* 是端口 **B1** 处的能量流率。
- *Q* 是传热速率，当热量离开热液体体积时为正。

**Moist Air**

该模块具有湿空气混合物、水蒸气、微量气体和水滴的质量守恒方程。

**注意**

如果在 Moist Air Properties (MA) 模块中，**Trace gas model** 参数为 `None`，则湿空气网络不会对微量气体建模。在这种情况下，在 Heat Exchanger (TL-MA) 模块中，微量气体的守恒方程设置为 0。

如果在 Moist Air Properties (MA) 模块中清除 **Enable entrained water droplets**，则湿空气网络不会对夹带水滴建模。在这种情况下，在 Heat Exchanger (TL-MA) 模块中，水滴的守恒方程设置为 0。

湿空气混合物的累积速率考虑了通过换热器端口的湿空气质量流量的变化以及冷凝质量流量，

m˙MA,net=m˙A2+m˙B2−m˙w,cond−m˙w,conv+m˙d,evap,

其中：

- m˙A2 是端口 **A2** 处湿空气质量流量。
- m˙A2 是端口 **B2** 处湿空气质量流量。
- m˙w,cond 是由于流体体积饱和而发生的水蒸气冷凝速率。
- m˙w,conv 是壁面上的冷凝速率。
- m˙d,evap 是水滴蒸发速率。

水蒸气的质量守恒方程为

dxwdtρMAIV+xwm˙MA,net=m˙w,net,

其中 *xw* 是蒸气的质量分数，*ρMAI* 是流体体积中湿空气的密度，*V* 是湿空气总体积。

m˙*w,net* 是净水蒸气质量流量，

m˙w,net=m˙w,A2+m˙w,B2−m˙w,cond−m˙w,conv+m˙d,evap,

其中：

- m˙w,A2 是端口 **A2** 处水蒸气质量流量。
- m˙w,B2 是端口 **B2** 处水蒸气质量流量。

微量气体的质量平衡为

dxgdtρMAIV+xgm˙MA,net=m˙g,A2+m˙g,B2,

其中：

- *xg* 是微量气体的质量分数。
- m˙g,A2 是端口 **A2** 处微量气体质量流量。
- m˙g,B2 是端口 **B2** 处微量气体质量流量。

水滴的质量平衡为

drdIdtρMAIV+rdIm˙MA,net=m˙d,net,

其中
*rdI* 是流体体积中水滴与湿空气的质量比。

m˙dnet 是净水滴质量流量，

m˙d,net=m˙d,A2+m˙d,B2+λd(m˙w,cond+m˙w,conv)−m˙d,evap,

其中：

- m˙d,A2 是端口 **A2** 处水滴质量流量。
- m˙d,A2 是端口 **B2** 处水滴质量流量。
- *λd* 是 **Fraction of condensate entrained as water droplets** 参数的值。

在湿空气侧，能量守恒考虑了因传热和水蒸气从湿空气质量中冷凝析出而引起的比内能变化，

(cpI−RI+rdcpdI)VρMAIdTIdt+uaIm˙MA,net+(uwI−uaI)m˙w,net+(ugI−uaI)m˙g,net+hdIm˙d,net=      ϕA2+ϕB2+Q−(1−λd)(m˙w,condhdI+m˙w,convhdH)−pIdVdt,

其中：

- *ua,I*、*uw,I* 和 *ug,I* 分别是空气、水蒸气和气体的内能。
- *cpI* 是湿空气比热。
- *cpdI* 是水滴比热。
- *rd* 是水滴与湿空气的质量比。
- *pI* 是内部体积的压力。
- *TI* 是内部体积的温度。
- *RI* 是内部体积的比气体常数。
- *hdI* 是流体体积中水滴的比焓。
- *hdH* 是壁面上水滴的比焓。
- *ϕA2* 是端口 **A2** 处的能量流率。
- *ϕB2* 是端口 **B2** 处的能量流率。

传入湿空气或从湿空气传出的热量 *Q*，等于从热液体传出或传入热液体的热量。
