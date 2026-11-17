---
type: simulink-block
title: 'Heat Exchanger (TL-MA)'
family: 'hydro'
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
```yaml
ports:
- name: A1
  summary: 热液体端口 thermal liquid
  direction: conserving
- name: B1
  summary: 热液体端口 thermal liquid
  direction: conserving
- name: A2
  summary: 湿空气端口 moist air
  direction: conserving
- name: B2
  summary: 湿空气端口 moist air
  direction: conserving
- name: W
  summary: 湿空气冷凝速率 physical signal
  direction: output
```

### 守恒端口

### **A1** — 热液体端口 thermal liquid

与热液体相关的入口或出口端口。

### **B1** — 热液体端口 thermal liquid

与热液体相关的入口或出口端口。

### **A2** — 湿空气端口 moist air

与湿空气相关的入口或出口端口。

### **B2** — 湿空气端口 moist air

与湿空气相关的入口或出口端口。
### 输出

### **W** — 湿空气冷凝速率 physical signal

离开湿空气流的水冷凝速率，以物理信号形式返回。该端口的值不包括以水滴形式夹带的冷凝部分。冷凝物不会积聚在传热表面上。
## 参数
```yaml
parameters:
- name: Flow arrangement
  summary: 流路排列 Cross flow（默认）| Parallel flow | Counter flow
  group: 配置
- name: Cross flow arrangement
  summary: 每个流道中的热混合条件 Thermal Liquid 1 unmixed & Moist Air 2 mixed（默认）| Both fluids unmixed | Thermal Liquid 1 mixed & Moist
    Air 2 unmixed | Both fluids mixed
  group: 配置
- name: Wall thermal resistance
  summary: 壁面通过热传导对热流的阻力 0 K/W（默认）| 正标量
  group: 配置
- name: Cross-sectional area at port A1
  summary: 端口 A1 处的流通面积 0.01 m^2（默认）| 正标量
  group: 配置
- name: Cross-sectional area at port B1
  summary: 端口 B1 处的流通面积 0.01 m^2（默认）| 正标量
  group: 配置
- name: Cross-sectional area at port A2
  summary: 端口 A2 处的流通面积 0.01 m^2（默认）| 正标量
  group: 配置
- name: Cross-sectional area at port B2
  summary: 端口 B2 处垂直于流动方向的面积 0.01 m^2（默认）| 正标量
  group: 配置
- name: Enable wall thermal mass
  summary: 用于建模壁面热质量的选项 off（默认）| on
  group: 配置
- name: Wall mass
  summary: 换热器壁面质量 1 kg（默认）| 正标量
  group: 配置
- name: Wall specific heat
  summary: 换热器壁面比热 490 J/(K*kg)（默认）| 正标量
  group: 配置
- name: Flow geometry
  summary: 热液体流动配置 Flow inside one or more tubes（默认）| Flow perpendicular to bank of circular tubes | Generic
  group: Thermal Liquid 1
- name: Number of tubes
  summary: 热液体管数量 25（默认）| 正标量
  group: Thermal Liquid 1
- name: Total length of each tube
  summary: 每根热液体管的总长度 1 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Tube cross section
  summary: 管的横截面形状 Circular（默认）| Rectangular | Annular | Generic
  group: Thermal Liquid 1
- name: Tube inner diameter
  summary: 单根管的内径 0.05 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Tube width
  summary: 单根管的内部宽度 0.05 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Tube height
  summary: 单根管的内部高度 0.05 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Annulus inner diameter (heat transfer surface)
  summary: 环形横截面的较小直径 0.05 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Annulus outer diameter
  summary: 环形横截面的较大直径 0.1 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Cross-sectional area per tube
  summary: 每根管内的内部流通面积 0.002 m^2（默认）| 正标量
  group: Thermal Liquid 1
- name: Wetted perimeter of tube cross-section for pressure loss
  summary: 流体接触的管横截面周长 0.15 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Perimeter of tube cross-section for heat transfer
  summary: 用于传热计算的单根管周长 0.15 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Pressure loss model
  summary: 由粘性摩擦引起的压力损失计算方法 Correlation for flow inside tubes（默认）| Euler number per tube row | Pressure loss coefficient |
    Correlation for flow over tube bank
  group: Thermal Liquid 1
- name: Pressure loss coefficient, delta_p/(0.5\*rho\*v^2)
  summary: 通道中所有压力损失的经验损失系数 10（默认）| 正标量
  group: Thermal Liquid 1
- name: Local resistance specification
  summary: 量化压力损失的方法 Aggregate equivalent length（默认）| Local loss coefficient
  group: Thermal Liquid 1
- name: Aggregate equivalent length of local resistances
  summary: 每根管所有局部阻力的合计长度 0.1 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Total local loss coefficient
  summary: 压力损失系数 0.1（默认）| 正标量
  group: Thermal Liquid 1
- name: Internal surface absolute roughness
  summary: 平均表面粗糙度高度 15e-6 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Laminar flow upper Reynolds number limit
  summary: 指示层流的最大雷诺数 2000（默认）| 正标量
  group: Thermal Liquid 1
- name: Turbulent flow lower Reynolds number limit
  summary: 指示湍流的最小雷诺数 4000（默认）| 正标量
  group: Thermal Liquid 1
- name: Laminar friction constant for Darcy friction factor
  summary: 层流中粘性摩擦引起的压力损失系数 64（默认）| 正标量
  group: Thermal Liquid 1
- name: Heat transfer coefficient model
  summary: 计算流体与壁面之间传热系数的方法 Correlation for flow over tube bank（默认）| Colburn equation | Correlation for flow inside tubes
  group: Thermal Liquid 1
- name: Coefficients [a, b, c] for a\*Re^b\*Pr^c
  summary: Colburn 方程系数 [0.023, 0.8, 0.33]（默认）| 三元素向量
  group: Thermal Liquid 1
- name: Laminar flow Nusselt number
  summary: 层流流态下对流传热与导热传热之比 3.66（默认）| 正标量
  group: Thermal Liquid 1
- name: Tube bank grid arrangement
  summary: 管束中管排的几何排列方式 Inline（默认）| Staggered
  group: Thermal Liquid 1
- name: Number of tube rows along flow direction
  summary: 管束中湿空气管排数 5（默认）| 正标量
  group: Thermal Liquid 1
- name: Number of tube segments in each tube row
  summary: 管束每排中湿空气管道的数量 5（默认）| 正标量
  group: Thermal Liquid 1
- name: Length of each tube segment in a tube row
  summary: 每根湿空气管道的长度 1 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Tube outer diameter
  summary: 湿空气管道的外径 0.05 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Longitudinal tube pitch (along flow direction)
  summary: 湿空气管排之间的中心到中心距离 0.15 m（默认）| 正标量
  group: Thermal Liquid 1
- name: Transverse tube pitch (perpendicular to flow direction)
  summary: 一排中湿空气流体管道之间的中心到中心距离 0.15（默认）| 正标量
  group: Thermal Liquid 1
- name: Euler number per tube row, delta_p/(N\*0.5\*rho\*v^2)
  summary: 管束每排的欧拉数 10（默认）| 正标量
  group: Thermal Liquid 1
- name: Minimum free-flow area
  summary: 入口和出口之间的最小总流通面积 0.01 m^2（默认）| 正标量
  group: Thermal Liquid 1
- name: Heat transfer surface area without fins
  summary: 不包括翅片的传热表面积总和 2 m^2（默认）| 正标量
  group: Thermal Liquid 1
- name: Thermal liquid volume inside heat exchanger
  summary: 换热器内热液体的总体积 0.05 m^3（默认）| 正标量
  group: Thermal Liquid 1
- name: Fouling factor
  summary: 由于污垢沉积产生的附加热阻 0.1 m^2*K/kW（默认）| 正标量
  group: Thermal Liquid 1
- name: Total fin surface area
  summary: 所有翅片的传热表面积总和 0 m^2（默认）| 正标量
  group: Thermal Liquid 1
- name: Fin efficiency
  summary: 翅片实际传热速率与理想传热速率之比 0.5（默认）| [0,1] 范围内的正标量
  group: Thermal Liquid 1
- name: Initial thermal liquid pressure
  summary: 仿真开始时湿空气的压力 0.101325 MPa（默认）| 正标量
  group: Thermal Liquid 1
- name: 初始热液体温度
  summary: 仿真开始时的温度 293.15 K（默认）| 正标量 | 二元素向量
  group: Thermal Liquid 1
- name: 流动几何
  summary: 湿空气流动配置 Flow perpendicular to bank of circular tubes（默认）| Flow inside one or more tubes | Generic
  group: Moist Air 2
- name: 管数
  summary: 湿空气管数 25（默认）| 正标量
  group: Moist Air 2
- name: 每根管的总长度
  summary: 每根湿空气管的总长度 1 m（默认）| 正标量
  group: Moist Air 2
- name: 管横截面
  summary: 管的横截面形状 Circular（默认）| Rectangular | Annular | Generic
  group: Moist Air 2
- name: 管内径
  summary: 单根管的内径 0.05 m（默认）| 正标量
  group: Moist Air 2
- name: 管宽度
  summary: 单根管的内部宽度 0.05 m（默认）| 正标量
  group: Moist Air 2
- name: 管高度
  summary: 单根管横截面的内部高度 0.05 m（默认）| 正标量
  group: Moist Air 2
- name: 环隙内径（换热表面）
  summary: 环形横截面的较小直径 0.05 m（默认）| 正标量
  group: Moist Air 2
- name: 环隙外径
  summary: 环形横截面的较大直径 0.1 m（默认）| 正标量
  group: Moist Air 2
- name: 每根管的横截面积
  summary: 每根管内的内部流通面积 0.002 m^2（默认）| 正标量
  group: Moist Air 2
- name: 用于压力损失的管横截面湿周
  summary: 流体接触的管横截面周长 0.15 m（默认）| 正标量
  group: Moist Air 2
- name: 用于换热的管横截面周长
  summary: 用于换热计算的单根管周长 0.15 m（默认）| 正标量
  group: Moist Air 2
- name: 压力损失模型
  summary: 由粘性摩擦引起的压力损失计算方法 Correlation for flow inside tubes（默认）| Euler number per tube row | Pressure loss coefficient |
    Correlation for flow over tube bank
  group: Moist Air 2
- name: 压力损失系数，delta_p/(0.5\*rho\*v^2)
  summary: 通道中所有压力损失的经验损失系数 10（默认）| 正标量
  group: Moist Air 2
- name: 局部阻力设定
  summary: 量化压力损失的方法 Aggregate equivalent length（默认）| Local loss coefficient
  group: Moist Air 2
- name: 局部阻力总等效长度
  summary: 每根管中所有局部阻力的合计长度 0.1 m（默认）| 正标量
  group: Moist Air 2
- name: 总局部损失系数
  summary: 压力损失系数 0.1（默认）| 正标量
  group: Moist Air 2
- name: 内表面绝对粗糙度
  summary: 平均表面粗糙度高度 15e-6 m（默认）| 正标量
  group: Moist Air 2
- name: 层流上限雷诺数
  summary: 表示层流的最大雷诺数 2000（默认）| 正标量
  group: Moist Air 2
- name: 湍流下限雷诺数
  summary: 表示湍流的最小雷诺数 4000（默认）| 正标量
  group: Moist Air 2
- name: Darcy 摩擦因子的层流摩擦常数
  summary: 层流中黏性摩擦引起的压力损失系数 64（默认）| 正标量
  group: Moist Air 2
- name: 传热系数模型
  summary: 计算流体与壁面之间传热系数的方法 Correlation for flow over tube bank（默认）| Colburn equation | Correlation for flow inside tubes
  group: Moist Air 2
- name: a\*Re^b\*Pr^c 的系数 [a, b, c]
  summary: Colburn 方程系数 [0.023, 0.8, 0.33]（默认）| 三元素向量
  group: Moist Air 2
- name: 层流 Nusselt 数
  summary: 层流流态中对流与导热传热之比 3.66（默认）| 正标量
  group: Moist Air 2
- name: 管束网格排列
  summary: 管束中热液体行的几何布置 Inline（默认）| Staggered
  group: Moist Air 2
- name: 沿流动方向的管排数
  summary: 管束中热液体管排数 5（默认）| 正标量
  group: Moist Air 2
- name: 每个管排中的管段数
  summary: 管束每排中的热液体管数 5（默认）| 正标量
  group: Moist Air 2
- name: 管排中每个管段的长度
  summary: 每根热液体管的长度 1 m（默认）| 正标量
  group: Moist Air 2
- name: Tube outer diameter
  summary: 单根热液管的外径 0.05 m（默认）| 正标量
  group: Moist Air 2
- name: Longitudinal tube pitch (along flow direction)
  summary: 热液管排之间的中心到中心距离 0.15 m（默认）| 正标量
  group: Moist Air 2
- name: Transverse tube pitch (perpendicular to flow direction)
  summary: 一排热液管之间的中心到中心距离 0.15 m（默认）| 正标量
  group: Moist Air 2
- name: Euler number per tube row, delta_p/(N\*0.5\*rho\*v^2)
  summary: 管束每一排的欧拉数 10（默认）| 正标量
  group: Moist Air 2
- name: Minimum free-flow area
  summary: 入口和出口之间的最小总流通面积 0.01 m^2（默认）| 正标量
  group: Moist Air 2
- name: Heat transfer surface area without fins
  summary: 不包括翅片的换热表面积总和 2 m^2（默认）| 正标量
  group: Moist Air 2
- name: Moist air volume inside heat exchanger
  summary: 换热器内湿空气的总体积 0.05 m^3（默认）| 正标量
  group: Moist Air 2
- name: Fouling factor
  summary: 由于污垢沉积而产生的附加热阻 0.1 m^2*K/kW（默认）| 正标量
  group: Moist Air 2
- name: Total fin surface area
  summary: 所有翅片的换热表面积总和 0 m^2（默认）| 正标量
  group: Moist Air 2
- name: Fin efficiency
  summary: 翅片实际传热速率与理想传热速率之比 0.5（默认）| 范围 [0,1] 内的正标量
  group: Moist Air 2
- name: Initial moist air pressure
  summary: 仿真开始时的湿空气压力 0.101325 MPa（默认）| 正标量
  group: Moist Air 2
- name: Initial moist air temperature
  summary: 仿真开始时的温度 293.15 K（默认）| 正标量 | 双元素向量
  group: Moist Air 2
- name: Initial humidity specification
  summary: 湿度规格 Relative humidity（默认）| Specific humidity | Mole fraction | Humidity ratio | Wet-bulb temperature
  group: Moist Air 2
- name: Initial moist air relative humidity
  summary: 仿真开始时的相对湿度 0.5（默认）| 范围 [0,1] 内的正标量 | 双元素向量
  group: Moist Air 2
- name: Initial moist air specific humidity
  summary: 仿真开始时的比湿度 0.01（默认）| 范围 [0,1] 内的正标量 | 双元素向量
  group: Moist Air 2
- name: Initial moist air water vapor mole fraction
  summary: 仿真开始时的水蒸气摩尔分数 0.01（默认）| [0,1] 范围内的正标量 | 二元素向量
  group: Moist Air 2
- name: Initial moist air humidity ratio
  summary: 仿真开始时的湿度比 0.01（默认）| [0,1] 范围内的正标量 | 二元素向量
  group: Moist Air 2
- name: Initial moist air wet-bulb temperature
  summary: 仿真开始时的湿球温度 287 K（默认）| [0,1] 范围内的正标量
  group: Moist Air 2
- name: Initial trace gas specification
  summary: 微量气体的测量类型 Mass fraction（默认）| Mole fraction
  group: Moist Air 2
- name: Initial moist air trace gas mass fraction
  summary: 湿空气通道中微量气体的量 0.001（默认）| [0,1] 范围内的正标量 | 二元素向量
  group: Moist Air 2
- name: Initial moist air trace gas mole fraction
  summary: 仿真开始时的微量气体摩尔分数 0.001（默认）| [0,1] 范围内的正标量 | 二元素向量
  group: Moist Air 2
- name: Initial mass ratio of water droplets to moist air
  summary: 水滴与湿空气之比 0（默认）| 正标量
  group: Moist Air 2
- name: Relative humidity at saturation
  summary: 冷凝的相对湿度点 1（默认）| [0,1] 范围内的正标量
  group: Moist Air 2
- name: Water vapor condensation time constant
  summary: 冷凝时间尺度 1e-3 s（默认）| 正标量
  group: Moist Air 2
- name: Water droplets evaporation time constant
  summary: 蒸发时间尺度 1e-3 s（默认）| 正标量
  group: Moist Air 2
- name: Fraction of condensate entrained as water droplets
  summary: 水滴中冷凝物的比例 1（默认）| [0,1] 范围内的标量
  group: Moist Air 2
```

### 配置

### **Flow arrangement** — 流路排列 `Cross flow`（默认）| `Parallel flow` | `Counter flow`

换热器两侧之间的流路排列。可用的流动布置为：

- `Parallel flow`。流体沿相同方向流动。
- `Counter flow`。流体彼此平行流动，方向相反。
- `Cross flow`。流体彼此垂直流动。

### **Cross flow arrangement** — 每个流道中的热混合条件 `Thermal Liquid 1 unmixed & Moist Air 2 mixed`（默认）| `Both fluids unmixed` | `Thermal Liquid 1 mixed & Moist Air 2 unmixed` | `Both fluids mixed`

选择每种流体是否可以在其通道中混合。混合流意味着流体在沿流路流动时可以自由地沿横向移动。非混合流意味着流体被限制为仅沿流路流动。例如，带有翅片的一侧被视为非混合流。

#### 依赖关系

要启用此参数，请将 **Flow arrangement** 设置为 `Cross flow`。

### **Wall thermal resistance** — 壁面通过热传导对热流的阻力 `0 K/W`（默认）| 正标量

分隔两种换热器流体的界面壁的热阻。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液体端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液体端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **B2** 处的流通面积。

### **Enable wall thermal mass** — 用于建模壁面热质量的选项 `off`（默认）| `on`

是否对换热器壁面热质量进行建模。对壁面热质量进行建模会在壁面对温度或热流变化做出瞬态响应时引入延迟。如果清除 **Enable wall thermal mass**，则该模块假定壁面足够薄，以至于在传热的时间尺度上瞬态响应是即时的。

### **Wall mass** — 换热器壁面质量 `1 kg`（默认）| 正标量

换热器壁面的质量。该模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 换热器壁面比热 `490 J/(K*kg)`（默认）| 正标量

换热器壁面的比热。该模块使用此值计算壁面热质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### Thermal Liquid 1

### **Flow geometry** — 热液体流动配置 `Flow inside one or more tubes`（默认）| `Flow perpendicular to bank of circular tubes` | `Generic`

热液体流路。流体可以在管束外部流动，也可以在单根管或多根管内部流动。您还可以基于经验值指定通用参数化。

### **Number of tubes** — 热液体管数量 `25`（默认）| 正标量

热液体管数量。更多的管会由于黏性摩擦而导致更高的压降，但会提供更大的传热表面积。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`。

### **Total length of each tube** — 每根热液体管的总长度 `1 m`（默认）| 正标量

每根热液体管的总长度。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`。

### **Tube cross section** — 管的横截面形状 `Circular`（默认）| `Rectangular` | `Annular` | `Generic`

单根管的横截面形状。设置为 `Generic` 可指定任意横截面几何形状。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`。

### **Tube inner diameter** — 单根管的内径 `0.05 m`（默认）| 正标量

单根管横截面的内径。横截面和直径沿管均匀一致。直径大小会影响压降和传热计算。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Circular`。

### **Tube width** — 单根管的内部宽度 `0.05 m`（默认）| 正标量

单根管横截面的内部宽度。横截面和宽度沿管均匀一致。宽度和高度会影响压降和传热计算。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Rectangular`。

### **Tube height** — 单根管的内部高度 `0.05 m`（默认）| 正标量

单根管横截面的内部高度。横截面和高度沿管均匀一致。宽度和高度会影响压降和传热计算。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 参数化设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Rectangular`。

### **Annulus inner diameter (heat transfer surface)** — 环形横截面的较小直径 `0.05 m`（默认）| 正标量

单根管环形横截面的较小直径。横截面和内径沿管均匀一致。内径会影响压降和传热计算。传热通过环形内表面发生。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 参数化设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Annular`。

### **Annulus outer diameter** — 环形横截面的较大直径 `0.1 m`（默认）| 正标量

单根管环形横截面的较大直径。横截面和外径沿管均匀一致。外径会影响压降和传热计算。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Annular`。

### **Cross-sectional area per tube** — 每根管内的内部流通面积 `0.002 m^2`（默认）| 正标量

每根管的内部流通面积。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Generic`。

### **Wetted perimeter of tube cross-section for pressure loss** — 流体接触的管横截面周长 `0.15 m`（默认）| 正标量

流体接触的管横截面周长。横截面和周长沿管均匀一致。该值用于压降计算。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Generic`。

### **Perimeter of tube cross-section for heat transfer** — 用于传热计算的单根管周长 `0.15 m`（默认）| 正标量

用于传热计算的管周长。这通常与管周长相同，但在诸如环形横截面等情况下，根据传热表面的不同，这可能仅为内径或外径。横截面和管周长沿管长方向均匀一致。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Tube cross-section** 设置为 `Generic`。

### **Pressure loss model** — 由粘性摩擦引起的压力损失计算方法 `Correlation for flow inside tubes`（默认）| `Euler number per tube row` | `Pressure loss coefficient` | `Correlation for flow over tube bank`

由粘性摩擦引起的压力损失计算方法。针对不同的流动配置提供了不同的模型。设置选项包括：

- `Correlation for flow inside tubes`。使用此设置可通过 Haaland 关联式计算压力损失。
- `Pressure loss coefficient`。使用此设置可基于经验损失系数计算压力损失。
- `Euler number per tube row`。使用此设置可基于经验欧拉数计算压力损失。
- `Correlation for flow over tube bank`。使用此设置可基于 Hagen 数计算压力损失。

可用的压力损失模型取决于 **Flow geometry** 设置。

#### 依赖关系

当 **Flow geometry** 设置为 `Flow inside one or more tubes` 时，**Pressure loss model** 可以设置为以下任一选项：

- `Pressure loss coefficient`。
- `Correlation for flow inside tubes`。

当 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，**Pressure loss model** 可以设置为以下任一选项：

- `Correlation for flow over tube bank`。
- `Euler number per tube row`。

当 **Flow geometry** 设置为 `Generic` 时，**Pressure loss model** 参数被禁用。压力损失通过 **Pressure loss coefficient, delta\_p/(0.5\*rho\*v^2)** 参数以经验方式计算。

### **Pressure loss coefficient, delta\_p/(0.5\*rho\*v^2)** — 通道中所有压力损失的经验损失系数 `10`（默认）| 正标量

通道中所有压力损失的经验损失系数。该值考虑了壁面摩擦以及由于通道中的弯头、弯管和其他几何变化引起的局部损失。

损失系数可以根据额定工况计算，也可以通过调参来拟合实验数据。其定义为：

ξ=Δp12ρv2，

其中 *Δp* 为压降，*ρ* 为热液体密度，*v* 为流速。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Flow geometry** 设置为 `Flow inside one or more tubes`，且 **Pressure loss model** 设置为 `Pressure loss coefficient`。
- **Flow geometry** 设置为 `Generic`。

### **Local resistance specification** — 量化压力损失的方法 `Aggregate equivalent length`（默认）| `Local loss coefficient`

在 Haaland 关联式中量化压力损失的方法。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Aggregate equivalent length of local resistances** — 每根管所有局部阻力的合计长度 `0.1 m`（默认）| 正标量

每根管所有局部阻力的合计长度。该值是指与管中由于弯头、三通或接头等阻力引起的所有局部损失之和产生相同压力损失的管道长度。合计长度越长，压力损失越大。该模块在计算摩擦引起的压力损失时，将此参数的值加到 **Total length of each tube** 参数中。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Pressure loss model** 设置为 `Correlations for flow inside tubes`，并将 **Local resistance specification** 设置为 `Aggregate equivalent length`。

### **Total local loss coefficient** — 压力损失系数 `0.1`（默认）| 正标量

系统中的局部压力损失系数。您可以使用此参数来校准系统以匹配实验结果。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`，并将 **Local resistance specification** 设置为 `Local loss coefficient`。

### **Internal surface absolute roughness** — 平均表面粗糙度高度 `15e-6 m`（默认）| 正标量

管表面缺陷的平均高度。在通过 Haaland 关联式计算压力损失时，管壁越粗糙，湍流 regime 中的压力损失越大。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将以下任一参数：

- **Pressure loss model**
- **Heat transfer coefficient model**

设置为 `Correlation for flow inside tubes`。

### **Laminar flow upper Reynolds number limit** — 指示层流的最大雷诺数 `2000`（默认）| 正标量

指示层流的最大雷诺数。在此值与 **Turbulent flow lower Reynolds number limit** 之间，流动 regime 为过渡态。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将以下任一参数：

- **Pressure loss model**
- **Heat transfer model**

设置为 `Correlation for flow inside tubes`。

### **Turbulent flow lower Reynolds number limit** — 指示湍流的最小雷诺数 `4000`（默认）| 正标量

指示湍流的最小雷诺数。在此值与 **Laminar flow upper Reynolds number limit** 之间，流动 regime 处于层流与湍流之间的过渡态。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Laminar friction constant for Darcy friction factor** — 层流中粘性摩擦引起的压力损失系数 `64`（默认）| 正标量

层流中粘性摩擦压力损失方程中的系数。此参数也称为*形状因子*。默认值对应于圆形管横截面。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Correlation for flow inside tubes`，将 **Tube cross section** 设置为 `Generic`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Heat transfer coefficient model** — 计算流体与壁面之间传热系数的方法 `Correlation for flow over tube bank`（默认）| `Colburn equation` | `Correlation for flow inside tubes`

计算流体与壁面之间传热系数的方法。可用的设置包括：

- `Colburn equation`。使用此设置可通过用户定义的 Colburn 方程变量 *a*、*b* 和 *c* 计算传热系数。
- `Correlation for flow over tube bank`。使用此设置可基于管束关联式使用 Hagen 数计算传热系数。
- `Correlation for flow inside tubes`。使用此设置可通过 Gnielinski 关联式计算管道流动的传热系数。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为以下任一选项：

- `Flow perpendicular to bank of circular tubes`。
- `Flow inside one or more tubes`。

### **Coefficients [a, b, c] for a\*Re^b\*Pr^c** — Colburn 方程系数 `[0.023, 0.8, 0.33]`（默认）| 三元素向量

包含 Colburn 方程经验系数的三元素向量。Colburn 方程是计算努塞尔数的一种公式。Colburn 方程的一般形式为：

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

### **Laminar flow Nusselt number** — 层流流态下对流传热与导热传热之比 `3.66`（默认）| 正标量

层流流态下对流传热与导热传热之比。流体努塞尔数影响传热速率，并取决于管道横截面。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，**Tube cross-section** 设置为 `Generic`，并将 **Heat transfer parameterization** 设置为 `Correlation for flow inside tubes`。

### **Tube bank grid arrangement** — 管束中管排的几何排列方式 `Inline`（默认）| `Staggered`

管束中管道的排列方式。管排要么与相邻管排对齐，要么交错排列。

- `Inline`：所有管排直接位于彼此后方。
- `Staggered`：某一管排的管道位于前一管排管道的间隙处。

管道排列方式影响努塞尔数和传热速率。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Number of tube rows along flow direction** — 管束中湿空气管排数 `5`（默认）| 正标量

管束中湿空气管排的数量。管排与热液体流动方向对齐。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Number of tube segments in each tube row** — 管束每排中湿空气管道的数量 `5`（默认）| 正标量

管束每排中湿空气管道的数量。该测量方向垂直于热液体流动方向。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Length of each tube segment in a tube row** — 每根湿空气管道的长度 `1 m`（默认）| 正标量

跨越一个管排的每根湿空气管道的长度。管束中所有管道的长度相同。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Tube outer diameter** — 湿空气管道的外径 `0.05 m`（默认）| 正标量

湿空气管道的外径。管道横截面沿管道均匀，因此直径在整个管道中恒定。该值影响由于粘性摩擦导致的横掠管束流动的损失。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Longitudinal tube pitch (along flow direction)** — 湿空气管排之间的中心到中心距离 `0.15 m`（默认）| 正标量

与热液体流动方向对齐的湿空气管束的管道中心之间的距离。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Transverse tube pitch (perpendicular to flow direction)** — 一排中湿空气流体管道之间的中心到中心距离 `0.15`（默认）| 正标量

一排湿空气管道中管道中心之间的距离。该测量方向垂直于热液体流动方向。更多信息请参见 Heat Transfer Coefficients。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **Euler number per tube row, delta\_p/(N\*0.5\*rho\*v^2)** — 管束每排的欧拉数 `10`（默认）| 正标量

单排管道的压降经验系数。欧拉数是压降与流体动量之比：

Eu=ΔpN12ρv2，

其中 *N* 是 **Number of tube rows along flow direction**，*Δp* 是压降，*ρ* 是热液体密度，*v* 是流速。

每个管排位于垂直于热液体流动的平面内。

#### 依赖关系

要启用此参数，请设置以下之一：

- **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`，并将 **Pressure loss model** 设置为 `Euler number per tube row`。
- **Flow geometry** 设置为 `Generic`。

### **Minimum free-flow area** — 入口和出口之间的最小总流通面积 `0.01 m^2`（默认）| 正标量

入口和出口之间的最小总横截流通面积。如果通道是由管道、管子、槽或凹槽组成的集合，则此参数的值为最小流通面积点处最小面积之和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值为一个横截面中管道之间间隙之和最小的那个横截面中所有间隙之和。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Generic`。

### **Heat transfer surface area without fins** — 不包括翅片的传热表面积总和 `2 m^2`（默认）| 正标量

传热表面积的总和，不包括翅片。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Generic`。

### **Thermal liquid volume inside heat exchanger** — 换热器内热液体的总体积 `0.05 m^3`（默认）| 正标量

换热器内热液体的总体积。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Generic`。

### **Fouling factor** — 由于污垢沉积产生的附加热阻 `0.1 m^2*K/kW`（默认）| 正标量

由于壁面表面上的污垢层产生的附加热阻。在实际系统中，污垢沉积会随时间增长。然而，其增长速度足够慢，可以在仿真期间假定为常数。

### **Total fin surface area** — 所有翅片的传热表面积总和 `0 m^2`（默认）| 正标量

接触热液体的所有翅片两侧的传热表面积总和。例如，如果翅片是矩形的，则表面积为矩形面积的两倍。

总传热表面积是通道表面积与有效翅片表面积之和，有效翅片表面积是 **Fin efficiency** 与 **Total fin surface area** 的乘积。

### **Fin efficiency** — 翅片实际传热速率与理想传热速率之比 `0.5`（默认）| [0,1] 范围内的正标量

如果整个翅片处于主传热表面温度时，通过接触热液体的翅片的实际传热量与理想传热量之比。

### **Initial thermal liquid pressure** — 仿真开始时湿空气的压力 `0.101325 MPa`（默认）| 正标量

仿真开始时热液体的压力。

### **初始热液体温度** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时热液体通道中的温度。此参数可以是标量或二元素向量。标量值表示通道中的平均初始温度。向量值以 [`inlet`， `outlet`] 的形式表示入口和出口处的初始温度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

### Moist Air 2

### **流动几何** — 湿空气流动配置 `Flow perpendicular to bank of circular tubes`（默认）| `Flow inside one or more tubes` | `Generic`

湿空气流动路径。流动可以在管束外部流过，也可以在单根管或多根管内部流动。您还可以基于经验值指定通用参数化。

### **管数** — 湿空气管数 `25`（默认）| 正标量

湿空气管数。更多的管会因粘性摩擦导致更高的压力损失，但提供更大的换热表面积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`。

### **每根管的总长度** — 每根湿空气管的总长度 `1 m`（默认）| 正标量

每根湿空气管的总长度。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`。

### **管横截面** — 管的横截面形状 `Circular`（默认）| `Rectangular` | `Annular` | `Generic`

单根管的横截面形状。设置为 `Generic` 以指定任意横截面几何形状。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`。

### **管内径** — 单根管的内径 `0.05 m`（默认）| 正标量

单根管横截面的内径。横截面和直径沿管均匀一致。直径的大小影响压力损失和换热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Circular`。

### **管宽度** — 单根管的内部宽度 `0.05 m`（默认）| 正标量

单根管横截面的内部宽度。横截面和宽度沿管均匀一致。宽度和高度影响压力损失和换热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Rectangular`。

### **管高度** — 单根管横截面的内部高度 `0.05 m`（默认）| 正标量

单根管横截面的内部高度。横截面和高度沿管均匀一致。宽度和高度影响压力损失和换热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 参数化设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Rectangular`。

### **环隙内径（换热表面）** — 环形横截面的较小直径 `0.05 m`（默认）| 正标量

单根管环形横截面的较小直径。横截面和内径沿管均匀一致。内径影响压力损失和换热计算。换热通过环隙的内表面发生。

#### 依赖关系

要启用此参数，请将 **流动几何** 参数化设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Annular`。

### **环隙外径** — 环形横截面的较大直径 `0.1 m`（默认）| 正标量

单根管环形横截面的较大直径。横截面和外径沿管均匀一致。外径影响压力损失和换热计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Annular`。

### **每根管的横截面积** — 每根管内的内部流通面积 `0.002 m^2`（默认）| 正标量

每根管的内部流通面积。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Generic`。

### **用于压力损失的管横截面湿周** — 流体接触的管横截面周长 `0.15 m`（默认）| 正标量

流体接触的管横截面周长。横截面和周长沿管均匀一致。此值应用于压力损失计算。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Generic`。

### **用于换热的管横截面周长** — 用于换热计算的单根管周长 `0.15 m`（默认）| 正标量

用于换热计算的管周长。这通常与管周长相同，但在诸如环形横截面的情况下，根据换热表面的不同，这可能仅为内径或外径。横截面和管周长沿管均匀一致。

#### 依赖关系

要启用此参数，请将 **流动几何** 设置为 `Flow inside one or more tubes`，并将 **管横截面** 设置为 `Generic`。

### **压力损失模型** — 由粘性摩擦引起的压力损失计算方法 `Correlation for flow inside tubes`（默认）| `Euler number per tube row` | `Pressure loss coefficient` | `Correlation for flow over tube bank`

由粘性摩擦引起的压力损失计算方法。不同的流动配置可使用不同的模型。设置为：

- `Correlation for flow inside tubes`。使用此设置通过 Haaland 关联式计算压力损失。
- `Pressure loss coefficient`。使用此设置基于经验损失系数计算压力损失。
- `Euler number per tube row`。使用此设置基于经验欧拉数计算压力损失。
- `Correlation for flow over tube bank`。使用此设置基于 Hagen 数计算压力损失。

可用的压力损失模型取决于 **流动几何** 设置。

#### 依赖关系

当 **流动几何** 设置为 `Flow inside one or more tubes` 时，**压力损失模型** 可以设置为：

- `Pressure loss coefficient`。
- `Correlation for flow inside tubes`。

当 **流动几何** 设置为 `Flow perpendicular to bank of circular tubes` 时，**压力损失模型** 可以设置为：

- `Correlation for flow over tube bank`。
- `Euler number per tube row`。

当 **流动几何** 设置为 `Generic` 时，**压力损失模型** 参数被禁用。压力损失通过 **压力损失系数，delta\_p/(0.5\*rho\*v^2)** 参数经验计算。

### **压力损失系数，delta\_p/(0.5\*rho\*v^2)** — 通道中所有压力损失的经验损失系数 `10`（默认）| 正标量

通道中所有压力损失的经验损失系数。此值考虑了壁面摩擦以及通道中弯头、弯管和其他几何变化引起的局部损失。

损失系数可以从额定工况计算得出，也可以通过调整来拟合实验数据。该系数定义为：

ξ=Δp12ρv2，

其中 *Δp* 是压降，*ρ* 是湿空气密度，*v* 是流速。

#### 依赖关系

要启用此参数，请设置以下任一：

- **流动几何** 为 `Generic`。
- **压力损失模型** 为 `Pressure loss coefficient`。

### **局部阻力设定** — 量化压力损失的方法 `Aggregate equivalent length`（默认）| `Local loss coefficient`

用于在 Haaland 关联式中量化压力损失的方法。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **局部阻力总等效长度** — 每根管中所有局部阻力的合计长度 `0.1 m`（默认）| 正标量

每根管中所有局部阻力的合计长度。该值是指能够产生与管中因弯头、三通或接头等阻力引起的所有局部损失之和相同压力损失的管长。合计长度越长，压力损失越大。在计算由摩擦引起的压力损失时，模块会将此参数的值加到 **Total length of each tube** 参数中。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Pressure loss model** 设置为 `Correlations for flow inside tubes`，并将 **Local resistance specification** 设置为 `Aggregate equivalent length`。

### **总局部损失系数** — 压力损失系数 `0.1`（默认）| 正标量

系统中的局部压力损失系数。您可以使用此参数校准系统，使其与实验结果匹配。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`，并将 **Local resistance specification** 设置为 `Local loss coefficient`。

### **内表面绝对粗糙度** — 平均表面粗糙度高度 `15e-6 m`（默认）| 正标量

管表面缺陷的平均高度。对于使用 Haaland 关联式计算的压力损失，管壁越粗糙，湍流区中的压力损失越大。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将以下任一参数：

- **Pressure loss model**
- **Heat transfer coefficient model**

设置为 `Correlation for flow inside tubes`。

### **层流上限雷诺数** — 表示层流的最大雷诺数 `2000`（默认）| 正标量

表示层流的最大雷诺数。在此值与 **Turbulent flow lower Reynolds number limit** 之间，流态为过渡流。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **湍流下限雷诺数** — 表示湍流的最小雷诺数 `4000`（默认）| 正标量

表示湍流的最小雷诺数。在此值与 **Laminar flow upper Reynolds number limit** 之间，流态为层流与湍流之间的过渡流。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **Darcy 摩擦因子的层流摩擦常数** — 层流中黏性摩擦引起的压力损失系数 `64`（默认）| 正标量

层流中黏性摩擦压力损失方程中的系数。此参数也称为*形状因子*。默认值对应于圆管横截面。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Correlation for flow inside tubes`，将 **Tube cross section** 设置为 `Generic`，并将 **Pressure loss model** 设置为 `Correlation for flow inside tubes`。

### **传热系数模型** — 计算流体与壁面之间传热系数的方法 `Correlation for flow over tube bank`（默认）| `Colburn equation` | `Correlation for flow inside tubes`

计算流体与壁面之间传热系数的方法。可用设置包括：

- `Colburn equation`。使用此设置可通过用户定义的 Colburn 方程变量 *a*、*b* 和 *c* 计算传热系数。
- `Correlation for flow over tube bank`。使用此设置可基于使用 Hagen 数的管束关联式计算传热系数。
- `Correlation for flow inside tubes`。使用此设置可通过 Gnielinski 关联式计算管道流动的传热系数。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为以下任一值：

- `Flow perpendicular to bank of circular tubes`。
- `Flow inside one or more tubes`。

### **a\*Re^b\*Pr^c 的系数 [a, b, c]** — Colburn 方程系数 `[0.023, 0.8, 0.33]`（默认）| 三元素向量

包含 Colburn 方程经验系数的三元素向量。Colburn 方程是计算 Nusselt 数的一种公式。Colburn 方程的一般形式为：

Nu=aRebPrc。

当 **Heat transfer coefficient model** 设置为 `Colburn equation` 且 **Flow geometry** 设置为 `Flow inside one or more tubes`，或者 **Flow geometry** 设置为 `Generic` 时，默认 Colburn 方程为：

Nu=0.023Re0.8Pr1/3。

当 **Heat transfer coefficient model** 设置为 `Colburn equation` 且 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，默认 Colburn 方程为：

Nu=0.27Re0.63Pr0.36。

#### 依赖关系

要启用此参数，请设置：

1. **Flow geometry** 为以下任一值：

   - `Flow inside one or more tubes`
   - `Flow perpendicular to bank of circular tubes`

   并将 **Heat transfer coefficient model** 设置为 `Colburn equation`。
2. **Flow geometry** 为 `Generic`。

### **层流 Nusselt 数** — 层流流态中对流与导热传热之比 `3.66`（默认）| 正标量

层流流态中对流与导热传热之比。流体 Nusselt 数会影响传热速率，并取决于管横截面。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow inside one or more tubes`，将 **Tube cross-section** 设置为 `Generic`，并将 **Heat transfer parameterization** 设置为 `Correlation for flow inside tubes`。

### **管束网格排列** — 管束中热液体行的几何布置 `Inline`（默认）| `Staggered`

管束中管子的排列方式。各行要么与其相邻行对齐，要么交错排列。

- `Inline`：所有管行都直接位于彼此后方。
- `Staggered`：某一管行的管子位于前一管行管子之间的间隙处。

管子排列会影响 Nusselt 数和传热速率。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **沿流动方向的管排数** — 管束中热液体管排数 `5`（默认）| 正标量

管束中热液体流体管排数。这些管排与湿空气流方向对齐。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **每个管排中的管段数** — 管束每排中的热液体管数 `5`（默认）| 正标量

管束每排中的热液体管数。该测量方向垂直于湿空气流。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。

### **管排中每个管段的长度** — 每根热液体管的长度 `1 m`（默认）| 正标量

跨越一个管排的每根热液体管的长度。管束中的所有管子长度相同。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular
tubes`。

### **Tube outer diameter** — 单根热液管的外径 `0.05 m`（默认）| 正标量

热液管的外径。横截面沿管子均匀，因此直径在整个管子上是恒定的。该值会影响由于粘性摩擦而导致的横穿管束流动中的损失。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular
tubes`。

### **Longitudinal tube pitch (along flow direction)** — 热液管排之间的中心到中心距离 `0.15 m`（默认）| 正标量

热液管束的管中心之间的距离，与湿空气的流动方向对齐。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular
tubes`。

### **Transverse tube pitch (perpendicular to flow direction)** — 一排热液管之间的中心到中心距离 `0.15 m`（默认）| 正标量

一排热液管中管中心之间的距离。该测量值垂直于湿空气流动方向。有关更多信息，请参见 Heat Transfer Coefficients。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular
tubes`。

### **Euler number per tube row, delta\_p/(N\*0.5\*rho\*v^2)** — 管束每一排的欧拉数 `10`（默认）| 正标量

一排管子上压降的经验系数。欧拉数是压降与流体动量之间的比值：

Eu=ΔpN12ρv2，

其中 *N* 是 **Number of
tube rows along flow direction**，*Δp* 是压降，*ρ* 是湿空气混合物密度，*v* 是流速。

每一排管子位于垂直于湿空气流动的平面内。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Flow perpendicular to bank of circular
tubes`，并将 **Pressure loss model** 设置为 `Euler number per tube row`。

### **Minimum free-flow area** — 入口和出口之间的最小总流通面积 `0.01 m^2`（默认）| 正标量

入口和出口之间的最小总横截流通面积。如果通道是管道、管子、狭槽或凹槽的集合，则此参数的值是最小流通面积点处最小面积的总和。此参数是流体速度最高的面积。例如，如果流体垂直于管束流动，则此参数的值是在一个横截面中管子之间的间隙之和最小的那些间隙的总和。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Generic`。

### **Heat transfer surface area without fins** — 不包括翅片的换热表面积总和 `2 m^2`（默认）| 正标量

换热表面积的总和，不包括翅片。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Generic`。

### **Moist air volume inside heat exchanger** — 换热器内湿空气的总体积 `0.05 m^3`（默认）| 正标量

换热器内湿空气的总体积。

#### 依赖关系

要启用此参数，请将 **Flow geometry** 设置为 `Generic`。

### **Fouling factor** — 由于污垢沉积而产生的附加热阻 `0.1 m^2*K/kW`（默认）| 正标量

由于壁面上的污垢层而产生的附加热阻。在实际系统中，污垢沉积会随时间增长。然而，其增长足够缓慢，可以在仿真期间假定为恒定值。

### **Total fin surface area** — 所有翅片的换热表面积总和 `0 m^2`（默认）| 正标量

与湿空气接触的所有翅片两侧的换热表面积总和。例如，如果翅片是矩形的，则表面积为矩形面积的两倍。

总换热表面积是通道表面积与有效翅片表面积之和，有效翅片表面积是 **Fin efficiency** 与 **Total fin
surface area** 的乘积。

### **Fin efficiency** — 翅片实际传热速率与理想传热速率之比 `0.5`（默认）| 范围 [0,1] 内的正标量

如果整个翅片处于主换热表面温度时，与湿空气接触的翅片的实际传热量与理想传热量之比。

### **Initial moist air pressure** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| 正标量

仿真开始时湿空气的压力。

### **Initial moist air temperature** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 双元素向量

仿真开始时湿空气流体通道中的温度。此参数可以是标量或双元素向量。标量值表示通道中的平均初始温度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始温度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

### **Initial humidity specification** — 湿度规格 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

用于指定换热器湿空气侧初始湿度的方法。

### **Initial moist air relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| 范围 [0,1] 内的正标量 | 双元素向量

仿真开始时湿空气通道中的相对湿度。相对湿度是水蒸气分压与水蒸气饱和压力之比，或水蒸气摩尔分数与饱和时水蒸气摩尔分数之比。

此参数可以是标量或双元素向量。标量值表示通道中的平均初始相对湿度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始相对湿度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity
specification** 设置为 `Relative
humidity`。

### **Initial moist air specific humidity** — 仿真开始时的比湿度 `0.01`（默认）| 范围 [0,1] 内的正标量 | 双元素向量

仿真开始时湿空气通道中的比湿度。比湿度是水蒸气质量与水蒸气、微量气体和干空气总质量之比。

此参数可以是标量或双元素向量。标量值表示通道中的平均初始比湿度。向量值以 [`inlet`, `outlet`] 形式表示入口和出口处的初始比湿度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity
specification** 设置为 `Specific
humidity`。

### **Initial moist air water vapor mole fraction** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的正标量 | 二元素向量

仿真开始时湿空气通道中水蒸气的摩尔分数。水蒸气摩尔分数是相对于水蒸气、微量气体和干空气的组合摩尔量而言的。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始蒸气摩尔分数。向量值以 [`inlet`, `outlet`] 的形式表示入口和出口处的初始蒸气摩尔分数。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial moist air humidity ratio** — 仿真开始时的湿度比 `0.01`（默认）| [0,1] 范围内的正标量 | 二元素向量

仿真开始时湿空气通道中的湿度比。湿度比是水蒸气质量与干空气和微量气体质量之比。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始湿度比。向量值以 [`inlet`, `outlet`] 的形式表示入口和出口处的初始湿度比。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial moist air wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| [0,1] 范围内的正标量

仿真开始时的湿球温度。该模块使用此值来计算湿度。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始湿球温度。向量值以 [`inlet`, `outlet`] 的形式表示入口和出口处的初始湿球温度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial trace gas specification** — 微量气体的测量类型 `Mass fraction`（默认）| `Mole fraction`

微量气体的测量类型。

### **Initial moist air trace gas mass fraction** — 湿空气通道中微量气体的量 `0.001`（默认）| [0,1] 范围内的正标量 | 二元素向量

仿真开始时湿空气通道中微量气体的质量分数。质量分数是相对于水蒸气、微量气体和干空气的组合总质量而言的。

此参数可以是标量或二元素向量。标量值表示通道中的平均微量气体质量分数。向量值以 [`inlet`, `outlet`] 的形式表示入口和出口处的初始微量气体质量分数。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial moist air trace gas mole fraction** — 仿真开始时的微量气体摩尔分数 `0.001`（默认）| [0,1] 范围内的正标量 | 二元素向量

仿真开始时湿空气通道中微量气体的摩尔分数。摩尔分数是相对于水蒸气、微量气体和干空气的组合摩尔总量而言的。

此参数可以是标量或二元素向量。标量值表示通道中的平均微量气体摩尔分数。向量值以 [`inlet`, `outlet`] 的形式表示入口和出口处的初始微量气体摩尔分数。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气之比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

### **Relative humidity at saturation** — 冷凝的相对湿度点 `1`（默认）| [0,1] 范围内的正标量

冷凝的相对湿度点。高于此值时发生冷凝。大于 1 的值表示过饱和蒸气。

### **Water vapor condensation time constant** — 冷凝时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝多余水分恢复到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸气的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 水滴中冷凝物的比例 `1`（默认）| [0,1] 范围内的标量

湿空气中以水滴形式夹带的冷凝物比例。
## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Moist Air

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2025a：对换热器壁的热质量建模

选择 **Wall thermal dynamics** 对换热器壁的热质量建模。

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

### R2024a：自由流通面积计算的更新

当 **Flow geometry** 为 `Flow perpendicular to bank of circular tubes` 时，该模块现在使用不同的方法计算自由流通面积。如果 **Number of tube segments in each tube row** 参数的值较小，该模块可能会显示压力损失和传热略有增加。

### R2024a：新的湿度指定选项

该模块为 **Initial humidity specification** 参数新增了一个选项。此选项称为 `Wet-bulb temperature`，允许您以湿球温度的形式输入数据。

### R2023a：使用局部损失系数对附加压力损失建模

将 **Local resistance specification** 参数设置为 `Local loss coefficient` 以指定量化压力损失的新方法。此选项允许您对超出管道长度所致损失之外的附加摩擦损失建模。

## 描述

模拟湿空气网络与热液体网络之间的热交换

Heat Exchanger (TL-MA) 模块模拟一个热交换器，其中包含一个湿空气网络，在端口 **A2** 和 **B2** 之间流动，以及一个热液体网络，在端口 **A1** 和 **B1** 之间流动。流体流可以布置为平行流、逆流或交叉流配置。

热液体-湿空气热交换器不适用于制冷冷却系统。有关可用于制冷应用的热交换器，请参见 Condenser Evaporator (2P-MA) 或 Condenser Evaporator (TL-2P)。

您可以将湿空气侧建模为管内流动、绕热液体管束流动，或通过经验的通用参数化建模。湿空气侧包含空气、微量气体和水蒸气，水蒸气在整个热交换循环中可能凝结。该模块模型考虑了水在传热表面上凝结时释放的潜热。该液层不会在表面积聚，并假定完全从下游湿空气流中移除。湿度凝结速率作为物理信号在端口 **W** 返回。

该模块使用效能-NTU（E-NTU）方法对通过共享壁面的传热进行建模。交换器壁面上的污垢会增加热阻并减少两种流体之间的热交换，该模块也对其进行了建模。您还可以选择性地对湿空气侧和热液体侧的翅片进行建模。交换器两侧由于粘性摩擦导致的压力损失可以通过解析方法或通用参数化建模，您可以使用后者根据自身数据进行调整。

您可以将热液体侧建模为管内流动、绕湿空气管束流动，或通过经验的通用参数化建模。

### 热交换器配置

热交换器效能基于所选的热交换器配置、流体属性、交换器各侧的管几何形状和流动配置，以及翅片的使用和尺寸。

**流动布置**

**Flow arrangement** 参数指定两侧之间的相对流动路径：

- `Parallel flow` 表示流体沿相同方向流动。
- `Counter flow` 表示流体平行但沿相反方向流动。
- `Cross flow` 表示流体彼此垂直流动。

**热混合**

当 **Flow arrangement** 设置为 `Cross flow` 时，使用 **Cross flow arrangement** 参数指示热液体流或湿空气流是否被折流板或壁面分隔为多条路径。如果没有这些分隔，流体可以自由混合，被视为*混合*。在交叉流布置中，两种流体、一种流体或两种流体都不混合。混合使流体温度沿第二流体的流动方向均匀化，并沿垂直于第二流体流动的方向变化。

非混合流的温度沿第二流体的流动路径以及垂直于该路径的方向均发生变化。

**交叉流配置示例**

请注意，仿真期间的流动方向不影响所选的流动布置设置。模块上的端口不反映物理热交换系统中端口的物理位置。

所有流动布置均为单程，这意味着流体在交换器中不会进行多次折返以增加传热点。要对多程热交换器进行建模，您可以将多个 Heat Exchanger (TL-MA) 模块串联或并联布置。

例如，要在湿空气侧实现双程配置并在热液体侧实现单程配置，您可以将湿空气侧串联连接，并将热液体侧并联连接到同一输入（例如两个 Mass Flow Rate Source 模块，各承担总质量流量的一半），如下所示。

**流动几何形状**

**Flow geometry** 参数将相应对话框选项卡中流体的流动布置设置为在管内或管组内流动，或垂直于管束流动。您还可以指定经验的通用配置。

当 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，使用 **Tube bank grid arrangement** 参数将另一种流体的管束排列定义为 `Inline` 或 `Staggered`。下图中红色的向下箭头表示在管束外部流动的流体方向。Inline 图还显示了 **Number of tube rows along flow direction** 和 **Number of tube segments in each tube row** 参数。此处，*流动方向*指的是相应对话框选项卡中的流体，*管*指的是另一种流体的管道。**Length of each tube segment in a tube row** 参数在 Staggered 图中标示。

同一时间只能有一种流体的 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes`。另一种流体必须配置为 `Flow inside one or more tubes` 或 `Generic`。如果两种流体的 **Flow geometry** 都设置为 `Flow perpendicular to bank of circular tubes`，您将收到错误。

**翅片**

当 **Total fin surface area** 参数为 `0 m^2` 时，热交换器配置没有翅片。翅片引入额外的传热表面积。每种流体侧有单独的翅片面积和描述该流体中翅片的参数。例如，当热液体在管内流动而湿空气在管外流动时，**Thermal Liquid 1** 部分中的 **Total fin surface area** 和 **Fin efficiency** 参数描述伸入管内的翅片。**Moist Air 2** 部分中的 **Total fin surface area** 和 **Fin efficiency** 参数描述管外的翅片。

### Effectiveness-NTU Heat Transfer

传热速率基于两种流体的平均属性计算。

对流换热为

Q=ϵCMin(TIn,TL−TIn,MA),

其中：

- *C*Min 是两种流体热容率中较小的一个。热容率是流体比热
  *c*p 与流体质量流量的乘积。*C*Min 始终为正。
- *T*In,TL 是热液体的入口温度。
- *T*In,MA 是湿空气的入口温度。
- *ε* 是换热器效能。

效能是热容率和传热单元数 *NTU* 的函数，并且还随换热器流动布置而变化，这将在按流动布置计算的效能中更详细地讨论。*NTU* 计算为：

NTU=1CMinR,

其中 *R* 是两种流体之间的总热阻，由对流、导热以及管壁上的任何污垢引起：

R=1UTLATh,TL+FTLATh,TL+RW+FMAATh,MA+1UMAATh,MA,

并且其中：

- *U* 是相应流体的对流换热系数。该系数将在换热系数中更详细地讨论。
- *F* 分别是热液体侧或湿空气侧的**污垢系数**。
- *R*W 是**通过换热表面的热阻**。
- *A*Th 是换热器相应侧的换热表面积。*A*Th 是壁表面积 *A*W 与**总翅片表面积** *A*F 之和：

  ATh=AW+ηFAF,

  其中 *η*F 是**翅片效率**。

模块在传热计算中使用的流体属性是入口值与流体体积内值的平均值。

**按流动布置计算的效能**

换热器效能根据其流动配置以及每种流体中的混合情况而变化。

- 当 **Flow arrangement** 设置为 `Parallel flow` 时：

  ϵ=1−exp[−NTU(1+CR)]1+CR
- 当 **Flow arrangement** 设置为 `Counter flow` 时：

  ϵ=1−exp[−NTU(1−CR)]1−CRexp[−NTU(1−CR)]
- 当 **Flow arrangement** 设置为 `Cross flow` 且 **Cross flow arrangement** 设置为 `Both fluids unmixed` 时：

  ϵ=1−exp{NTU0.22CR[exp(−CRNTU0.78)−1]}
- 当 **Flow arrangement** 设置为 `Cross flow` 且 **Cross flow arrangement** 设置为 `Both fluids mixed` 时：

  ϵ=[11−exp(−NTU)+CR1−exp(−CRNTU)−1NTU]−1

当一种流体混合而另一种流体不混合时，效能方程取决于流体的相对热容率。当 **Flow arrangement** 设置为 `Cross flow` 且 **Cross flow arrangement** 设置为 `Thermal Liquid 1 mixed & Moist Air 2 unmixed` 或 `Thermal Liquid 1 unmixed & Moist Air 2 mixed` 时：

- 当具有 Cmax 的流体混合且具有 Cmin 的流体不混合时：

  ϵ=1CR(1−exp{−CR{1−exp(−NTU)}})
- 当具有 Cmin 的流体混合且具有 Cmax 的流体不混合时：

  ϵ=1−exp{−1CR[1−exp(−CRNTU)]}

*C*R 表示两种流体热容率之比：

CR=CMinCMax.

### Conductive Heat Transfer

区域内的导热传热为

Qcond=Tout,TL−Tout,MARcond,

其中：

- *Tout,TL* 是热液体的区域出口温度。
- *Tout,MA* 是湿空气的区域出口温度。
- *Rcond* 是两种流体之间的总导热热阻，

  Rcond=DhkTLAW,TL+FTLAW,TL+RW+FMAAW,MA+DhkMAAW,MA,

  其中：

  - *AW* 是壁表面积。
  - *k* 是每种流体的导热系数。
  - *DH* 是水力直径。

总传热是对流传热与导热传热之和。与对流传热相比，导热传热可以忽略不计。当流量为零时，对流传热也为零。然而，由于对流传热和导热传热彼此独立运行，即使对流传热为零，仍然存在导热传热。

### Condensation

在湿空气侧，换热表面上可能形成冷凝层。该液层会影响湿空气与热液体之间传递的热量。上述 E-NTU 传热方程是针对*干*传热给出的。为修正冷凝的影响，还需使用下面列出的湿参数额外计算 E-NTU 方程。两个计算得到的热流量中，导致湿空气侧冷却量更大的那一个将用于热计算 [1] [2]。要使用此方法，假定 Lewis 数接近 1，这对于湿空气成立 [1][2]。

**用于传热速率计算的 E-NTU 量**

|  | 干计算 | 湿计算 |
| --- | --- | --- |
| 湿空气区域入口温度 | *Tin,MA* | *Tin,wb,MA* |
| 热容率 | m˙¯MAc¯p,MA | m˙¯MAc¯eq,MA |
| 换热系数 | *UMA* | UMAc¯eq,MAc¯p,MA |

其中：

- *Tin,MA* 是湿空气入口温度。
- *Tin,wb,MA* 是与 *Tin,MA* 相关的湿空气湿球温度。
- m˙¯MA 是干空气质量流量。
- c¯p,MA 是每单位干空气质量的湿空气热容。
- c¯eq,MA 是等效热容。*等效热容*是湿空气比焓（每单位干空气）h¯MA 在饱和湿空气条件下随温度的变化：

  c¯eq,MA=(∂h¯MA∂TMA)s.

离开湿空气质量流量的冷凝水蒸气质量流量取决于湿空气入口与通道壁之间的相对湿度以及换热器 NTU：

m˙cond=−m˙¯MA(Wwall,MA−Win,MA)(1−e−NTUMA),

其中：

- *W*wall,MA 是换热表面处的湿度比。
- *W*in,MA 是湿空气流入口处的湿度比。
- *NTU*MA 是湿空气侧的传热单元数，计算为：

  NTUMA=UMAc¯eq,MAc¯p,MAATh,MAm˙¯MAc¯eq,MA.

与水蒸气冷凝相关的能量流基于水蒸气比焓 *h*water, wall 与水的汽化比焓 *h*fg 之间的差值：

ϕCond=m˙cond(hwater,wall−hfg).

假定冷凝物不会积聚在换热表面上，并且不会影响诸如管径之类的几何参数。

### 传热系数

以下方程同时适用于热液体侧和湿空气侧，并使用各自的流体属性。

**管内流动**

对流换热系数根据流体努塞尔数变化：

U=NukDH，

其中：

- *Nu* 是平均努塞尔数，取决于流态。
- *k* 是流体导热率。
- *D*H 是管道水力直径。

对于湍流，努塞尔数使用 Gnielinski 关联式计算：

Nu=fD8(Re−1000)Pr1+12.7f8(Pr2/3−1)，

其中：

- *Re* 是流体雷诺数。
- *Pr* 是流体普朗特数。

对于层流，努塞尔数由 **Laminar flow Nusselt number** 参数设置。

对于过渡流，努塞尔数是层流和湍流努塞尔数之间的混合值。

**横掠管束流动**

当 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，努塞尔数基于 Hagen 数 Hg 计算，并取决于 **Tube bank grid arrangement** 设置：

Nu={0.404Lq1/3(Re+1Re+1000)0.1,Inline0.404Lq1/3,Staggered

其中：

Lq={1.18Pr(4lT/π−DlL)Hg(Re),Inline0.92Pr(4lT/π−DlD)Hg(Re),Staggered with lL≥D0.92Pr(4lTlL/π−D2lLlD)Hg(Re),Staggered with lL<D

- *D* 是 **Tube outer diameter**。
- *lL* 是 **Longitudinal tube pitch (along flow direction)**，即沿流动方向的管中心之间的距离。*Flow direction* 是外部流体的流动方向。
- *lT* 是 **Transverse tube pitch (perpendicular to flow direction)**，即另一种流体的一排管中管道中心之间的距离。
- *l*D 是对角管间距，计算为 lD=(lT2)2+lL2。

有关计算 Hagen 数的更多信息，请参见 [6]。

测量值 *l*L 和 *l*T 如下方管束横截面所示。这些距离对于两种网格管束排列类型都相同。

**带节距测量值的管道横截面**

**经验努塞尔数公式**

当 **Heat transfer coefficient model** 参数设置为 `Colburn equation` 或当 **Flow geometry** 设置为 `Generic` 时，努塞尔数由经验 Colburn 方程计算：

Nu=aRebPrc，

其中 *a*、*b* 和 *c* 在 **Coefficients [a, b, c] for a\*Re^b\*Pr^c** 参数中定义。

### 压力损失

以下方程同时适用于热液体侧和湿空气侧，并使用各自的流体属性。

**管内流动**

由于粘性摩擦引起的压力损失随流态和配置而变化。

对于湍流，当雷诺数高于 **Turbulent flow lower Reynolds number limit** 参数，并且当 **Pressure loss model** 设置为 `Correlations for flow inside tubes` 时，由于摩擦引起的压力损失以 Darcy 摩擦因子表示。

对于热液体侧，端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=fD,Am˙A1|m˙A1|2ρDHACS2(L+LAdd2)，

其中：

- m˙A1 是通过端口 **A1** 的总流量。
- *fD,A* 是根据 Haaland 关联式得到的 Darcy 摩擦因子。当 **Local resistance specification** 参数为 `Aggregate equivalent length` 时，

  fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2，

  其中 *ε*R 是热液体管道 **Internal surface absolute roughness**。摩擦因子取决于雷诺数，模块会为每种液体在两个端口处计算该值。
- *L* 是热液体侧的 **Total length of each tube**。
- *L*Add 是热液体侧的 **Aggregate equivalent length of local resistances**，即一根管道的等效长度，该管道引入的损失与管道中其他局部阻力损失之和相同。
- *A*CS 是管道总横截面积。

端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=fD,Bm˙B1|m˙B1|2ρDHACS2(L+LAdd2)，

其中 m˙B1 是通过端口 **B1** 的总流量。

当 **Local resistance specification** 参数为 `Aggregate equivalent length` 时，端口 **B1** 处的 Darcy 摩擦因子为：

fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2。

当 **Local resistance specification** 参数为 `Local loss coefficient` 时，端口 **A1** 和 **B1** 处的 Darcy 摩擦因子为

fD,A1={−1.8log10[6.9ReA1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)fD,B1={−1.8log10[6.9ReB1+(ϵR3.7DH)1.11]}-2+Clocalloss(DHL)

其中 *Clocalloss* 是 **Total local loss coefficient** 参数的值。

对于层流，当雷诺数低于 **Laminar flow upper Reynolds number limit** 参数，并且当 **Pressure loss model** 设置为 `Correlations for flow inside tubes` 时，模块根据 **Laminar friction constant for Darcy friction factor** 参数 *λ* 计算由于摩擦引起的压力损失。当 **Tube cross-section** 为 `Generic` 时，*λ* 是用户定义的参数。否则，模块会在内部计算该值。

端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=λμm˙A12ρDH2ACS(L+LAdd2)，

其中 μ 是流体动力粘度。端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=λμm˙B12ρDH2ACS(L+LAdd2)。

对于过渡流，当 **Pressure loss model** 设置为 `Correlations for flow inside tubes` 时，由于粘性摩擦引起的压差是层流和湍流压力损失值之间的平滑混合。

**管内流动的经验公式**

当 **Pressure loss model** 设置为 `Pressure loss coefficient` 或当 **Flow geometry** 设置为 `Generic` 时，由于粘性摩擦引起的压力损失使用经验压力损失系数 *ξ* 计算。相同的方程适用于湿空气侧和热液体侧，并使用各自的流体属性。

对于热液体侧，端口 **A1** 与内部节点 I1 之间的压差为：

pA1−pI1=12ξm˙A1|m˙A1|2ρACS2。

端口 **B1** 与内部节点 I1 之间的压差为：

pB1−pI1=12ξm˙B1|m˙B1|2ρACS2。

**横掠管束流动的压力损失**

当 **Flow geometry** 设置为 `Flow perpendicular to bank of circular tubes` 时，Hagen 数用于计算由于粘性摩擦引起的压力损失。相同的方程适用于湿空气侧和热液体侧，并使用各自的流体属性。

对于湿空气侧，端口 **A2** 与内部节点 I2 之间的压差为：

pA2−pI2=12μ2NRρD2Hg(Re)，

其中：

- *μ* 是湿空气流体动力粘度。
- *N*R 是 **Number of tube rows along flow direction**。当湿空气在管束外部流动时，这是沿湿空气流动方向的热液体管排数。

端口 **B2** 与内部节点 I2 之间的压差为：

pB2−pI2=12μ2NRρD2Hg(Re)。

**横掠管束流动的经验公式**

当 **Pressure loss model** 设置为 `Euler number per tube row` 或当 **Flow geometry** 设置为 `Generic` 时，由于粘性摩擦引起的压力损失使用压力损失系数，以 Euler 数 *Eu* 表示：

Eu=ξNR，

其中 *ξ* 是经验压力损失系数。

端口 **A2** 与内部节点 I2 之间的压差为：

pA2−pI2=12NREum˙A2|m˙A2|2ρACS2。

端口 **B2** 与内部节点 I2 之间的压差为：

pB2−pI2=12NREum˙B2|m˙B2|2ρACS2。

### Wall Thermal Mass

如果选择 **Enable wall thermal mass**，该模块会对换热器壁面热质量进行建模，这会在壁面对温度或热流变化作出瞬态响应时引入延迟。如果对热质量进行建模，壁面会在其边界内储存热量。这种热量储存会减缓稳态之间的过渡，因此一侧的热扰动不会立即在另一侧显现。该滞后会持续到两侧的热流率平衡为止。

如果选择 **Enable wall thermal mass**，则壁面能量守恒为

(Mwallcp,wall2)dTwallTLdt=−QTL−Q(Mwallcp,wall2)dTwallMAdt=−QMA+Q

其中：

- *Mwall* 是 **Wall mass** 参数的值。
- *cp,wall* 是 **Wall specific heat** 参数的值。
- *Twall* 是每一侧的有效壁温。该模块使用此值来建模瞬态响应。你无法测量此值。

传递到每种流体的热量为

QTL=CTL(TwallTL−TinTL)(1−e−NTUTL)QMA=CMA(TwallMA−TinMA)(1−e−NTUMA)

其中：

- *Tin* 是每一侧的流体入口温度。
- *C* 是每种流体的热容率。

每一侧流体与壁面之间的传热单元数为

NTUTL=UTLATLCTLNTUMA=UMAAMACMA

其中 *A* 是壁面表面积，*U* 是传热系数。

### Conservation Equations

**Thermal Liquid**

热液体的总质量累积速率定义为：

dMTLdt=m˙A1+m˙B1,

其中：

- *MTL* 是热液体的总质量。
- m˙A1 是端口 **A1** 处流体的质量流量。
- m˙B1 是端口 **B1** 处流体的质量流量。

当流体通过端口流入模块时，流量为正。

能量守恒方程将比内能的变化与流体传递的热量联系起来

MTLduTLdt+uTL(m˙A1+m˙B1)=ϕA1+ϕB1−Q,

其中：

- *uTL* 是热液体的比内能。
- *φA1* 是端口 **A1** 处的能量流率。
- *φB1* 是端口 **B1** 处的能量流率。
- *Q* 是传热速率，当其离开热液体体积时为正。

**Moist Air**

该模块具有针对湿空气混合物、水蒸气、示踪气体和水滴的质量换算方程。

**Note**

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则湿空气网络不会对示踪气体建模。在这种情况下，在 Heat Exchanger (TL-MA) 模块中，示踪气体的守恒方程设置为 0。

如果在 Moist Air Properties (MA) 模块中清除 **Enable entrained water droplets**，则湿空气网络不会对夹带水滴建模。在这种情况下，在 Heat Exchanger (TL-MA) 模块中，水滴的守恒方程设置为 0。

湿空气混合物的累积速率考虑了通过换热器端口的湿空气质量流量的变化以及冷凝质量流量，

m˙MA,net=m˙A2+m˙B2−m˙w,cond−m˙w,conv+m˙d,evap,

其中：

- m˙A2 是端口 **A2** 处的湿空气质量流量。
- m˙A2 是端口 **B2** 处的湿空气质量流量。
- m˙w,cond 是由于流体体积饱和而导致的水蒸气冷凝速率。
- m˙w,conv 是壁面上的冷凝速率。
- m˙d,evap 是水滴蒸发速率。

水蒸气的质量守恒方程为

dxwdtρMAIV+xwm˙MA,net=m˙w,net,

其中 *xw* 是蒸汽的质量分数，*ρMAI* 是流体体积中湿空气的密度，*V* 是湿空气总体积。

m˙*w,net* 是净水蒸气质量流量，

m˙w,net=m˙w,A2+m˙w,B2−m˙w,cond−m˙w,conv+m˙d,evap,

其中：

- m˙w,A2 是端口 **A2** 处的水蒸气质量流量。
- m˙w,B2 是端口 **B2** 处的水蒸气质量流量。

示踪气体质量平衡为

dxgdtρMAIV+xgm˙MA,net=m˙g,A2+m˙g,B2,

其中：

- *xg* 是示踪气体的质量分数。
- m˙g,A2 是端口 **A2** 处的示踪气体质量流量。
- m˙g,B2 是端口 **B2** 处的示踪气体质量流量。

水滴质量平衡为

drdIdtρMAIV+rdIm˙MA,net=m˙d,net,

其中 *rdI* 是流体体积中水滴与湿空气的质量比。

m˙dnet 是净水滴质量流量，

m˙d,net=m˙d,A2+m˙d,B2+λd(m˙w,cond+m˙w,conv)−m˙d,evap,

其中：

- m˙d,A2 是端口 **A2** 处的水滴质量流量。
- m˙d,A2 是端口 **B2** 处的水滴质量流量。
- *λd* 是 **Fraction of condensate entrained as water droplets** 参数的值。

在湿空气侧，能量守恒考虑了由于传热和水蒸气从湿空气质量中冷凝出来而引起的比内能变化，

(cpI−RI+rdcpdI)VρMAIdTIdt+uaIm˙MA,net+(uwI−uaI)m˙w,net+(ugI−uaI)m˙g,net+hdIm˙d,net=      ϕA2+ϕB2+Q−(1−λd)(m˙w,condhdI+m˙w,convhdH)−pIdVdt,

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

传递到湿空气或从湿空气传递出的热量 *Q* 等于从热液体传递出或传递到热液体的热量。
