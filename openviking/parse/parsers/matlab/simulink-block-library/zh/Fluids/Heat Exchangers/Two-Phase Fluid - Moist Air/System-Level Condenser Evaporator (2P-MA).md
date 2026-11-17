---
type: simulink-block
title: 'System-Level Condenser Evaporator (2P-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid - Moist Air'
documentation_page: 'systemlevelcondenserevaporator2pma'
documentation_source_path: 'ref/systemlevelcondenserevaporator2pma.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Condenser Evaporator (2P-MA)

## 端口

### 输出

### **Q1** — 传递给两相流体的传热速率，W physical signal

传递给两相流体的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。

### **Q2** — 传递给湿空气的传热速率，W physical signal

传递给湿空气的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。

### **W** — 湿空气冷凝速率，kg/s physical signal

离开湿空气流的水冷凝速率，以物理信号形式返回。该端口的值不包括以水滴形式夹带的冷凝部分。冷凝液不会在传热表面上积聚。
### 守恒端口

### **A1** — 两相流体端口 two-phase fluid

与两相流体相关的进口或出口端口。

### **B1** — 两相流体端口 two-phase fluid

与两相流体相关的进口或出口端口。

### **A2** — 湿空气端口 moist air

与湿空气相关的进口或出口端口。

### **B2** — 湿空气端口 moist air

与湿空气相关的进口或出口端口。

## 参数

### 配置

### **Flow arrangement at nominal operating conditions** — 流路对齐方式 `Counter flow - Two-Phase Fluid 1 flows from A to B, Moist Air 2 flows from B to A`（默认）| `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

在标称工况下换热器两侧之间的流路对齐方式。可用的流动布置为：

- `Counter flow - Two-Phase Fluid 1 flows from A to B, Moist Air 2
  flows from B to A` — 两股流体平行流动，方向相反。
- `Parallel flow - Both fluids flow from A to B` —
  两股流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to B` — 两股流体
  相互垂直流动。

平行流和逆流之间的选择会影响模块确定换热器尺寸的方式。逆流设置最为有效，满足指定性能所需的尺寸最小。相反，平行流效果最差，满足指定性能所需的尺寸最大。

标称工况下的流动方向（从 A 到 B，或从 B 到 A）仅在选择 **Initialize two-phase fluid to
nominal operating conditions** 或 **Initialize moist air to nominal
operating conditions** 时影响模型初始化。如果设置不同的初始工况，流动方向可以不同。

在模块确定换热器尺寸之后，此设置在仿真期间不影响模块计算传热的方式。相反，传热取决于仿真期间的流动方向。例如，如果将该参数设置为平行流，但将模型设置为以逆流运行，则即使其余边界条件相同，仿真期间的传热速率也不会与指定性能匹配。

如果将该参数设置为交叉流，则模块将换热器内部的流路建模为相互垂直，因此仿真期间的流动方向无关紧要。

### **Enable wall thermal mass** — 是否启用热质量对传热表面的影响 `off`（默认）| `on`

是否启用热质量对传热表面的影响。选择此参数时，模块会引入额外的动态特性，需要更长时间才能达到稳态，但此参数不影响稳态仿真结果。

如果出口处的流体属性（如流量方向或流体状态）在仿真期间出现意外振荡，选择此参数可能有助于稳定结果。

### **Wall mass** — 传热表面的质量 `1 kg`（默认）| 正标量

传热表面的质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal
mass**。

### **Wall specific heat** — 传热表面的比热 `490 J/(K*kg)`（默认）| 正标量

传热表面的比热。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal
mass**。

### **Initialize wall temperature to nominal operating conditions** — 初始化壁面温度的选项 `on`（默认）| `off`

将壁面温度初始化为标称工况或指定值的选项。如果选择此参数，模块将根据两侧流体指定的标称工况计算初始壁面温度。如果清除此参数，可以使用 **Initial wall temperature** 参数直接指定初始壁面温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal
mass**。

### **Initial wall temperature** — 壁面的初始温度 `293.15 K`（默认）| 正标量或二元素向量

壁面的初始温度。如果指定标量，模块假定初始壁面温度是均匀的。如果指定二元素向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 之间以及端口 **B1** 和 **B2** 之间线性变化。第一个元素对应端口 **A1** 和 **A2** 处的温度，第二个元素对应端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**
并清除 **Initialize wall temperature to nominal operating
conditions** 复选框。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

两相流体端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

两相流体端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **B2** 处的流通面积。

### 两相流体 1

### **Nominal operating condition** — 选择标称工况对应冷凝器还是蒸发器 `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air 2`（默认）| `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid 1`

标称工况：

- `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
  2` — 两相流体被冷却，湿空气被加热。
- `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid 1` — 湿空气被冷却，两相流体被加热。

此设置仅与标称工况参数相关。这并不意味着仿真期间传热只能沿指定方向发生。

### **Nominal mass flow rate** — 标称工况下两相端口之间的质量流量 `0.001 kg/s`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1**
的质量流量。

### **Nominal pressure drop** — 标称工况下两相端口之间的压降 `0.01 MPa`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1**
的压降。

### **Pressure specification** — 选择压力指定方法 `Inlet pressure`（默认）| `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

选择压力指定方法：

- `Inlet pressure` — 指定标称进口
  压力。
- `Saturation pressure at specified condensing
  temperature` — 指定标称冷凝温度。如果将 **Nominal operating condition** 设置为
  `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
  2`，则此选项可用。
- `Saturation pressure at specified evaporating
  temperature` — 指定标称蒸发温度。如果将 **Nominal operating condition** 设置为
  `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid
  1`，则此选项可用。

### **Nominal inlet pressure** — 两相流体侧进口处的压力 `1 MPa`（默认）| 正标量

标称工况下换热器两相流体进口处的压力。

#### 依赖关系

要启用此参数，请将 **Pressure specification** 设置为
`Inlet pressure`。

### **Nominal condensing temperature** — 使用标称冷凝温度指定压力 `313.15 K`（默认）| 正标量

标称工况下换热器两相流体出口处的液体饱和温度。换热器中的压力为相应的饱和压力。标称冷凝温度必须低于临界温度。

#### 依赖关系

要启用此参数，请将 **Nominal operating condition**
设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
2`，并将 **Pressure specification** 设置为
`Saturation pressure at specified condensing
temperature`。

### **Nominal evaporating temperature** — 使用标称蒸发温度指定压力 `243.15 K`（默认）| 正标量

标称工况下换热器两相流体出口处的蒸气饱和温度。换热器中的压力为相应的饱和压力。标称蒸发温度必须低于临界温度。

#### 依赖关系

要启用此参数，请将 **Nominal operating condition**
设置为 `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid
1`，并将 **Pressure specification** 设置为
`Saturation pressure at specified evaporating
temperature`。

### **Inlet condition specification** — 选择用于描述两相流体进口条件的量 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality`

用于描述标称工况下流体进口条件的量：温度、比焓或蒸气干度。

### **Nominal inlet specific enthalpy** — 两相流体侧进口处的比焓 `440 kJ/kg`（默认）| 正标量

标称工况下换热器两相流体进口处的比焓。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification**
设置为 `Specific enthalpy`。

### **Nominal inlet temperature** — 两相流体侧进口处的温度 `313.15 K`（默认）| 正标量

标称工况下换热器两相流体进口处的温度。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification**
设置为 `Temperature`。

### **Nominal inlet vapor quality** — 两相流体侧进口处的蒸气干度 `1`（默认）| 正标量

标称工况下换热器两相流体进口处的蒸气干度，定义为液-气混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification**
设置为 `Vapor quality`。

### **Heat transfer capacity specification** — 如何指定两相流体的传热能力 `Rate of heat transfer`（默认）| `Outlet condition`

是直接通过传热速率指定标称工况下换热器对两相流体的性能，还是通过出口条件间接指定。

### **Nominal rate of heat transfer** — 传热速率 `0.1 kW`（默认）| 正标量

传热速率。**Nominal Operating condition**
参数决定热量传入和传出的网络：

- 如果 **Nominal operating condition** 为 `Condenser
  - heat transfer from Two-Phase Fluid 1 to Moist Air 2`，则此
  参数为标称工况下从两相流体传递到湿空气的热量速率。
- 如果 **Nominal operating condition** 为 `Evaporator
  - heat transfer from Moist Air 2 to Two-Phase Fluid 1`，则此
  参数为标称工况下从湿空气传递到两相流体的热量速率。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity
specification** 设置为 `Rate of heat
transfer`。

### **Outlet condition specification** — 选择用于出口条件指定的量 `Specific enthalpy`（默认）| `Subcooling` | `Superheating` | `Vapor quality`

选择用于出口条件指定的量：

- `Specific enthalpy` — 指定标称比焓。
- `Subcooling` — 指定标称过冷度。如果将 **Nominal operating condition** 设置为
  `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
  2`，则此选项可用。
- `Superheating` — 指定标称过热度。如果将 **Nominal operating
  condition** 设置为 `Evaporator - heat transfer from Moist Air 2
  to Two-Phase Fluid 1`，则此选项可用。
- `Vapor quality` — 指定标称蒸气
  干度。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity
specification** 设置为 `Outlet condition`。

### **Nominal outlet specific enthalpy** — 两相流体侧出口处的比焓 `250 kJ/kg`（默认）| 正标量 | 二元素向量

标称工况下换热器两相流体出口处的比焓。

#### 依赖关系

要启用此参数，请将 **Outlet condition
specification** 设置为 `Specific enthalpy`。

### **Nominal subcooling** — 两相流体侧出口处低于液体饱和温度的温度差 `5 deltaK`（默认）| 正标量

标称工况下换热器两相流体出口处低于液体饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **Outlet condition
specification** 设置为 `Subcooling`。

### **Nominal superheating** — 两相流体侧出口处高于蒸气饱和温度的温度差 `5 deltaK`（默认）| 正标量

标称工况下换热器两相流体出口处高于蒸气饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **Outlet condition
specification** 设置为 `Superheating`。

### **Nominal outlet vapor quality** — 两相流体侧出口处的蒸气质量分数 `0`（默认）| [0,1] 范围内的标量

标称工况下换热器两相流体出口处的两相流体蒸气干度，定义为液-气混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **Outlet condition
specification** 设置为 `Vapor quality`。

### **Two-phase fluid volume** — 两相流体的总体积 `0.001 m^3`（默认）| 正标量

换热器内两相流体的总体积。

### **Initialize two-phase fluid to nominal operating conditions** — 将两相流体初始化为额定工况的选项 `on`（默认）| `off`

将两相流体初始化为额定工况或指定值的选项。如果选中此参数，模块会将两相流体初始化为额定工况。如果清除此复选框，则可以通过附加参数直接指定初始条件。

### **Initial fluid energy specification** — 两相流体的初始状态 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

用于描述流体初始状态的量。

**Initial fluid energy specification** 参数的值限制了两相流体可用的初始状态。当 **Initial fluid energy specification** 为：

- `Temperature` — 指定初始状态为过冷液体或过热蒸气。不能指定液-气混合物，因为在液-气混合物区域内温度是恒定的。
- `Vapor quality` — 指定初始状态为液-气混合物。不能指定过冷液体或过热蒸气，因为在整个区域内液相质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定初始状态为液-气混合物。不能指定过冷液体或过热蒸气，因为在整个区域内液相质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。模块不限制初始状态。

#### 依赖关系

要启用此参数，请清除 **Initialize two-phase fluid to nominal operating conditions** 复选框。

### **Initial two-phase fluid pressure** — 仿真开始时的流体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的两相流体压力。

#### 依赖关系

要启用此参数，请清除 **Initialize two-phase fluid to nominal operating conditions** 复选框。

### **Initial two-phase fluid specific enthalpy** — 仿真开始时的单位质量焓 `1500 kJ/kg`（默认）| 正标量 | 双元素向量

仿真开始时的两相流体比焓。如果该值为标量，则假定初始比焓均匀。如果该值为双元素向量，则假定初始比焓在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **Initialize two-phase fluid to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。

### **Initial two-phase fluid temperature** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 双元素向量

仿真开始时的两相流体温度。如果该值为标量，则假定初始温度均匀。如果该值为双元素向量，则假定初始温度在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **Initialize two-phase fluid to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Temperature`。

### **Initial two-phase fluid vapor quality** — 仿真开始时的蒸气质量分数 `0.5`（默认）| [0,1] 范围内的标量 | 双元素向量

仿真开始时的两相流体蒸气干度，定义为液-气混合物中蒸气的质量分数。如果该值为标量，则假定初始蒸气干度均匀。如果该值为双元素向量，则假定初始蒸气干度在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除 **Initialize two-phase fluid to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor quality`。

### **Initial two-phase fluid vapor void fraction** — 仿真开始时的蒸气空隙率 `0.5`（默认）| [0,1] 范围内的标量 | 双元素向量

仿真开始时的两相流体蒸气空隙率，定义为液-气混合物中蒸气的体积分数。如果该值为标量，则假定初始蒸气空隙率均匀。如果该值为双元素向量，则假定初始蒸气空隙率在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除 **Initialize two-phase fluid to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor void fraction`。

### **Initial two-phase fluid specific internal energy** — 仿真开始时的单位质量内能 `1500 kJ/kg`（默认）| 正标量 | 双元素向量

仿真开始时的两相流体比内能。如果该值为标量，则假定初始比内能均匀。如果该值为双元素向量，则假定初始比内能在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **Initialize two-phase fluid to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific internal energy`。

### Moist Air 2

### **Nominal mass flow rate** — 额定工况下湿空气端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的质量流量。

### **Nominal pressure drop** — 额定工况下湿空气端口之间的压降 `0.001 MPa`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的压降。

### **Nominal inlet pressure** — 湿空气侧入口处的压力 `0.101325 MPa`（默认）| 正标量

额定工况下换热器湿空气入口处的压力。

### **Nominal inlet temperature** — 湿空气侧入口处的温度 `293.15 K`（默认）| 正标量

额定工况下换热器湿空气入口处的温度。

### **Inlet humidity specification** — 用于描述湿空气侧入口处湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述额定工况下入口处湿度水平的量。

### **Nominal inlet relative humidity** — 入口处的相对湿度 `0.5`（默认）| [0,1] 范围内的标量

额定工况下换热器湿空气入口处的相对湿度。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Relative humidity`。

### **Nominal inlet specific humidity** — 入口处的比湿 `0.01`（默认）| [0,1] 范围内的标量

额定工况下换热器湿空气入口处的比湿，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Specific humidity`。

### **Nominal inlet water vapor mole fraction** — 入口处水蒸气的摩尔分数 `0.01`（默认）| [0,1] 范围内的标量

额定工况下换热器湿空气入口处湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Mole fraction`。

### **Nominal inlet humidity ratio** — 入口处的含湿量 `0.01`（默认）| [0,1] 范围内的正标量

额定工况下换热器湿空气入口处的含湿量，定义为水蒸气与干空气及微量气体的质量比。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Humidity ratio`。

### **Nominal inlet wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| [0,1] 范围内的正标量

额定工况下换热器湿空气入口处的湿球温度。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Wet-bulb temperature`。

### **Inlet trace gas specification** — 用于描述入口处微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述额定工况下入口处微量气体水平的量：质量分数或摩尔分数。

### **Nominal inlet trace gas mass fraction** — 入口处微量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量

额定工况下换热器湿空气入口处湿空气混合物中微量气体的质量分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Inlet trace gas specification** 设置为 `Mass fraction`。

### **Nominal inlet trace gas mole fraction** — 入口处微量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量

额定工况下换热器湿空气入口处湿空气混合物中微量气体的摩尔分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Inlet trace gas specification** 设置为 `Mole fraction`。

### **Moist air volume** — 换热器中湿空气的总体积 `0.1 m^3`（默认）| 正标量

换热器中湿空气的总体积。

### **Initialize moist air to nominal operating conditions** — 将湿空气初始化为额定工况的选项 `on`（默认）| `off`

将湿空气初始化为额定工况或指定值的选项。如果选中此参数，模块会将湿空气初始化为额定工况。如果清除此复选框，则可以通过附加参数直接指定初始条件。

### **Initial moist air pressure** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的湿空气压力。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Initial moist air temperature** — 仿真开始时的湿空气温度 `293.15 K`（默认）| 正标量 | 双元素向量

仿真开始时的湿空气温度。如果该值为标量，则假定初始温度均匀。如果该值为双元素向量，则假定初始温度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Initial humidity specification** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述初始湿度水平的量：相对湿度、比湿、水蒸气摩尔分数或含湿量。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Initial moist air relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| [0,1] 范围内的标量 | 双元素向量

仿真开始时的湿空气相对湿度。如果该值为标量，则假定初始相对湿度均匀。如果该值为双元素向量，则假定初始相对湿度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial moist air specific humidity** — 仿真开始时的比湿 `0.01`（默认）| [0,1] 范围内的标量 | 双元素向量

仿真开始时的湿空气比湿，定义为湿空气混合物中水蒸气的质量分数。如果该值为标量，则假定初始比湿均匀。如果该值为双元素向量，则假定初始比湿在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial moist air water vapor mole fraction** — 仿真开始时水蒸气的摩尔分数 `0.01`（默认）| [0,1] 范围内的标量 | 双元素向量

仿真开始时湿空气混合物中水蒸气的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀。如果该值为双元素向量，则假定初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial moist air humidity ratio** — 仿真开始时的含湿量 `0.01`（默认）| [0,1] 范围内的正标量 | 双元素向量

仿真开始时的湿空气含湿量，定义为水蒸气与干空气及微量气体的质量比。如果该值为标量，则假定初始含湿量均匀。如果该值为双元素向量，则假定初始含湿量在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial moist air wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| 范围 [0,1] 内的正标量

仿真开始时的湿球温度。模块使用此值计算湿度。

此参数可以是标量或二元素向量。标量值表示通道内的平均初始湿球温度。向量值表示入口和出口处的初始湿球温度，形式为 [`inlet`，`outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial trace gas specification** — 用于描述初始微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述仿真开始时微量气体水平的量：质量分数或摩尔分数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Initial moist air trace gas mass fraction** — 仿真开始时微量气体的质量分数 `0.001`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时湿空气混合物中微量气体的质量分数。如果该值为标量，则假定初始质量分数均匀。如果该值为二元素向量，则假定初始质量分数在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial moist air trace gas mole fraction** — 仿真开始时微量气体的摩尔分数 `0.001`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时湿空气混合物中微量气体的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀。如果该值为二元素向量，则假定初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气的质量比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Relative humidity at saturation** — 冷凝的相对湿度点 `1`（默认）| 非负标量

冷凝的相对湿度点。高于此值时发生冷凝。在大多数情况下，此值为 1，即 100%。大于 1 的值表示过饱和蒸汽。

### **Water vapor condensation time constant** — 冷凝的时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝多余水分回到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发的时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸汽的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 水滴中冷凝物的比例 `1`（默认）| 范围 [0,1] 内的标量

湿空气中被夹带为水滴的冷凝物比例。

### Correlation Coefficients

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid liquid** — 两相流体中过冷液体的关联式系数 `0.023`（默认）| 正标量

两相流体中过冷液体的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid mixture** — 两相流体中液-汽混合物的关联式系数 `0.005`（默认）| 正标量

两相流体中液-汽混合物的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的比例常数。默认值基于 Cavallini 和 Zecchin 关联式。

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid vapor** — 两相流体中过热蒸汽的关联式系数 `0.023`（默认）| 正标量

两相流体中过热蒸汽的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for two-phase fluid** — 两相流体关联式中的 Reynolds 数指数 `0.8`（默认）| 正标量

两相流体的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的 Reynolds 数指数。相同的值适用于过冷液体、液-汽混合物和过热蒸汽。

### **c in Nu = a\*Re^b\*Pr^c for two-phase fluid** — 两相流体关联式中的 Prandtl 数指数 `0.33`（默认）| 正标量

两相流体的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的 Prandtl 数指数。相同的值适用于过冷液体、液-汽混合物和过热蒸汽。

### **a in Nu = a\*Re^b\*Pr^c for moist air** — 湿空气的关联式系数 `0.005`（默认）| 正标量

湿空气的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for moist air** — 湿空气关联式中的 Reynolds 数指数 `0.8`（默认）| 正标量

湿空气的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的 Reynolds 数指数。默认值基于 Colburn 方程。

### **c in Nu = a\*Re^b\*Pr^c for moist air** — 湿空气关联式中的 Prandtl 数指数 `0.33`（默认）| 正标量

湿空气的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的 Prandtl 数指数。默认值基于 Colburn 方程。

## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Moist Air

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2024b: Model water droplets suspended in moist air flow

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

### R2024a: New moisture specification options

该模块为 **Inlet humidity specification** 和 **Initial humidity specification** 参数提供了新选项。此选项称为 `Wet-bulb temperature`，允许您以湿球温度的形式输入数据。

### R2023b: Specify initial wall temperature

如果您选择 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框，则可以使用新的 **Initial wall temperature** 参数直接指定初始条件。

## 描述

基于两相流体和湿空气网络之间性能数据的换热器

System-Level Condenser Evaporator (2P-MA) 模块对两相流体网络和湿空气网络之间的换热器进行建模。

根据热传递方向，该模块可以在制冷系统中充当冷凝器或蒸发器。该模块使用换热器数据表中的性能数据，而不是换热器的详细几何结构。您可以在设计迭代期间调整换热器的尺寸和性能，或对具有不常见几何结构的换热器进行建模。您还可以在早期设计阶段使用此模块对具有一定性能水平的换热器进行建模，此时详细的几何数据尚不可用。

您通过额定工况对模块进行参数化。换热器的尺寸设定为在稳态额定工况下匹配指定的性能。

Two-Phase Fluid 1 侧根据沿流动路径的焓变近似计算液相区、混合物区和气相区。Moist Air 2 侧基于与换热表面的对流水分质量传递对水蒸气冷凝进行建模。冷凝水从湿空气流中去除。

此模块与 Condenser Evaporator (2P-MA) 模块类似，但使用不同的参数化模型。下表比较了这两个模块：

| Condenser Evaporator (2P-MA) | System-Level Condenser Evaporator (2P-MA) |
| --- | --- |
| 模块参数基于换热器几何结构 | 模块参数基于性能和工况 |
| 换热器几何结构可能受可用几何参数选项的限制 | 模型独立于特定换热器几何结构 |
| 您可以通过调整几何参数（如翅片尺寸和管长）来调整模块以满足不同的性能要求 | 您可以通过直接指定所需的热量和质量流量来调整模块以满足不同的性能要求 |
| 您可以在平行流、逆流或交叉流配置之间进行选择 | 您可以在额定工况下在平行流、逆流或交叉流布置之间进行选择，以帮助进行尺寸设定 |
| 在广泛的工况范围内提供预测性准确的结果，受 E-NTU 方程和传热系数关联式适用性的约束 | 在指定工况附近结果非常准确；远离指定工况时精度可能降低 |
| 传热计算通过使用 E-NTU 模型考虑沿流动路径的温度变化 | 传热计算通过将流动路径分为三段来近似温度变化 |
| 考虑过冷液体、液-汽混合物和过热蒸汽的不同流体属性和传热系数 | 考虑过冷液体、液-汽混合物和过热蒸汽的不同流体属性和传热系数 |
| 根据几何结构跟踪过冷液体、液-汽混合物和过热蒸汽区域的可变区域长度分数 | 使用基于入口和出口之间焓差的加权因子近似过冷液体、液-汽混合物和过热蒸汽区域的影响 |
| 考虑湿空气流上的水蒸气冷凝和潜热 | 考虑湿空气流上的水蒸气冷凝和潜热 |

### Heat Transfer

该模块将两相流体流和湿空气流各分为三个大小相等的段，并计算每段中流体之间的热传递。为简单起见，本节中的方程针对一个段。

如果您清除 **Enable wall thermal mass** 复选框，则换热器中的热平衡为

Qseg,2P+Qseg,MA=0，

其中：

- *Q*seg,2P 是从壁面（即换热表面）到段中两相流体的热流率。
- *Q*seg,MA 是从壁面到段中湿空气的热流率。

如果您选择 **Enable wall thermal mass**，则换热器中的热平衡为

Qseg,2P+Qseg,MA=−MwallcpwallNdTseg,walldt，

其中：

- *M*wall 是壁面的质量。
- *c*pwall 是壁面的比热。
- *N* = 3 是段数。
- *T*seg,wall 是段中的平均壁面温度。
- *t* 是时间。

从壁面到段中两相流体的热流率为

Qseg,2P=UAseg,2P(Tseg,wall−Tseg,2P)，

其中：

- *UA*seg,2P 是段中两相流体的加权平均传热导。
- *T*seg,2P 是段中两相流体的加权平均流体温度。

从壁面到段中湿空气的热流率为

Qseg,MA=UAseg,MAc¯pseg,MA(h¯seg,wall−h¯seg,MA)+m˙w,seg,condhl,wall，

其中：

- *UA*seg,MA 是段中湿空气的传热导。
- c¯pseg,MA 是段中每单位质量干空气和微量气体的湿空气混合物比热。
- h¯seg,wall 是在平均壁面段温度下每单位质量干空气和微量气体的湿空气混合物焓。
- h¯seg,MA 是段中每单位质量干空气和微量气体的湿空气混合物焓。
- m˙w,seg,cond 是壁面上的水蒸气冷凝速率。
- *h*l,wall 是在平均壁面段温度下液态水的比焓。

在此方程中使用混合物焓同时考虑了温度差异和由于冷凝引起的湿度差异 [3]。

模块在传热计算中使用的流体属性是入口值和流体体积中值的平均值。

**Note**

对于湿空气量，符号上方的横线表示它们是混合物量除以仅干空气和微量气体的质量，而不是除以整个混合物的质量。整个混合物包括干空气、水蒸气和微量气体。

### 两相流体传热关联式

如果该段为过冷液体，则传热导为

UAseg,L,2P=aL,2P(Reseg,L,2P)b2P(Prseg,L,2P)c2Pkseg,L,2PG2PN,

其中：

- *a*L,2P、
  *b*2P 和
  *c*2P 是努塞尔数关联式的系数。这些系数是 **Correlation
  Coefficients** 部分中的模块参数。
- *Re*seg,L,2P 是该段的平均液体雷诺数。
- *Pr*seg,L,2P 是该段的平均液体普朗特数。
- *k*seg,L,2P 是该段的平均液体热导率。
- *G*2P 是换热器两相流体侧的几何比例因子。该模块计算几何比例因子，使得所有段上的总传热量在标称工况下与指定性能匹配。

平均液体雷诺数为

Reseg,L,2P=m˙seg,2PDref,2Pμseg,L,2PSref,2P,

其中：

- m˙seg,2P 是通过该段的质量流量。
- *μ*seg,L,2P 是该段的平均液体动力黏度。
- *D*ref,2P 是任意参考直径。
- *S*ref,2P 是任意参考流通面积。

**注意**

此方程中包含 *D*ref,2P 和
*S*ref,2P 项仅用于单位计算目的，以使
*Re*seg,L,2P 无量纲。*D*ref,2P 和
*S*ref,2P 的值是任意的，因为
*G*2P 的计算会覆盖这些值。

类似地，如果该段为过热蒸气，则传热导为

UAseg,V,2P=aV,2P(Reseg,V,2P)b2P(Prseg,V,2P)c2Pkseg,V,2PG2PN,

其中：

- *a*V,2P、
  *b*2P 和
  *c*2P 是努塞尔数关联式的系数。这些系数作为模块参数出现在
  **Correlation Coefficients** 部分中。
- *Re*seg,V,2P 是该段的平均蒸气雷诺数。
- *Pr*seg,V,2P 是该段的平均蒸气普朗特数。
- *k*seg,V,2P 是该段的平均蒸气热导率。

平均蒸气雷诺数为

Reseg,V,2P=m˙seg,2PDref,2Pμseg,V,2PSref,2P,

其中 *μ*seg,V,2P 是该段的平均蒸气动力黏度。

如果该段为液-气混合物，则传热导为

UAseg,M,2P=aM,2P(Reseg,SL,2P)b2PCZ(Prseg,SL,2P)c2Pkseg,SL,2PG2PN,

其中：

- *a*M,2P、
  *b*2P 和
  *c*2P 是努塞尔数关联式的系数。这些系数作为模块参数出现在
  **Correlation Coefficients** 部分中。
- *Re*seg,SL,2P 是该段的饱和液体雷诺数。
- *Pr*seg,SL,2P 是该段的饱和液体普朗特数。
- *k*seg,SL,2P 是该段的饱和液体热导率。
- *CZ* 是 Cavallini 和 Zecchin 项。

饱和液体雷诺数为

Reseg,SL,2P=m˙seg,2PDref,2Pμseg,SL,2PSref,2P,

其中 *μ*seg,SL,2P 是该段的饱和液体动力黏度。

Cavallini 和 Zecchin 项为

CZ=((νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P+1))1+b2P−((νseg,SV,2Pνseg,SL,2P−1)(xseg,in,2P+1))1+b2P(1+b2P)(νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P−xseg,in,2P),

其中：

- *ν*seg,SL,2P 是该段的饱和液体比容。
- *ν*seg,SV,2P 是该段的饱和蒸气比容。
- *x*seg,in,2P 是该段入口处的蒸气干度。
- *x*seg,out,2P 是该段出口处的蒸气干度。

该表达式基于 Cavallini 和 Zecchin [5] 的工作，其中推导了局部蒸气干度
*x* 下的传热系数关联式。液-气混合物的方程是通过在从
*x*seg,in,2P 到
*x*seg,out,2P 的段上对 Cavallini 和 Zecchin 关联式取平均得到的。

### 两相流体加权平均

通过某段的两相流体流动可能无法完全表示为过冷液体、过热蒸气或液-气混合物中的任一种。相反，每个段可能由这些的组合构成。该模块通过基于该段比焓变化以及饱和液体和蒸气比焓计算加权因子（*w*L、
*w*V 和
*w*M）来近似此条件。该模块假设该段内的比焓从入口到出口呈分段线性变化，其断点对应于液体和蒸气的饱和边界。传热系数较大的区域比传热系数较低的区域具有更陡的斜率。

wL=ΔLΔL+ΔM+ΔVwV=ΔVΔL+ΔM+ΔVwM=1−wL−wV

ΔL=|min(hseg,out,2P,hseg,SL,2P)−min(hseg,in,2P,hseg,SL,2P)|⋅UAseg,M,2P⋅UAseg,V,2PΔM=|min(max(hseg,out,2P,hseg,SL,2P),hseg,SV,2P)−min(max(hseg,in,2P,hseg,SL,2P),hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,V,2PΔV=|max(hseg,out,2P,hseg,SV,2P)−max(hseg,in,2P,hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,M,2P

其中：

- *h*seg,in,2P 是该段入口处的比焓。
- *h*seg,out,2P 是该段出口处的比焓。
- *h*seg,SL,2P 是该段的饱和液体比焓。
- *h*seg,SV,2P 是该段的饱和蒸气比焓。

因此，该段的加权平均两相流体传热导为

UAseg,2P=wL(UAseg,L,2P)+wV(UAseg,V,2P)+wM(UAseg,M,2P).

该段的加权平均流体温度为

Tseg,2P=wL(UAseg,L,2P)Tseg,L,2P+wV(UAseg,V,2P)Tseg,V,2P+wM(UAseg,M,2P)Tseg,M,2PUAseg,2P,

其中：

- *T*seg,L,2P 是该段的平均液体温度。
- *T*seg,V,2P 是该段的平均蒸气温度。
- *T*seg,M,2P 是该段的平均混合物温度，即饱和液体温度。

### 湿空气传热关联式

传热导为

UAseg,MA=aMA(Reseg,MA)bMA(Prseg,MA)cMAkseg,MAGMAN,

其中：

- *a*MA、
  *b*MA 和
  *c*MA 是努塞尔数关联式的系数。这些系数是 **Correlation
  Coefficients** 部分中的模块参数。
- *Re*seg,MA 是该段的平均雷诺数。
- *Pr*seg,MA 是该段的平均普朗特数。
- *k*seg,MA 是该段的平均热导率。
- *G*MA 是换热器湿空气侧的几何比例因子。该模块计算几何比例因子，使得所有段上的总传热量在标称工况下与指定性能匹配。

平均雷诺数为

Reseg,MA=m˙seg,MADref,MAμseg,MASref,MA,

其中：

- m˙seg,MA 是通过该段的质量流量。
- *μ*seg,MA 是该段的平均动力黏度。
- *D*ref,MA 是任意参考直径。
- *S*ref,MA 是任意参考流通面积。

**注意**

此方程中包含 *D*ref,MA 和
*S*ref,MA 项仅用于单位计算目的，以使
*Re*seg,MA 无量纲。*D*ref,MA 和
*S*ref,MA 的值是任意的，因为
*G*MA 的计算会覆盖这些值。

### 湿空气冷凝

描述从壁面到该段湿空气的热流率的方程（Heat Transfer 部分中的最后一个方程）使用平均湿空气混合物焓 h¯seg,MA 和壁面段湿空气混合物焓 h¯seg,wall。

平均湿空气混合物焓基于通过该段的湿空气流的温度和湿度：

h¯seg,MA=hseg,ag,MA+Wseg,MAhseg,w,MA,

其中：

- *h*seg,ag,MA 是该段干空气和痕量气体的平均比焓。
- *h*seg,w,MA 是该段水蒸气的平均比焓。
- *W*seg,MA 是该段的湿度比。

壁面段湿空气混合物焓基于壁面段处的温度和湿度：

h¯seg,wall=hseg,ag,wall+Wseg,wallhseg,w,wall,

其中：

- *h*seg,ag,wall 是壁面段温度下干空气和痕量气体的比焓。
- *h*seg,w,wall 是壁面段温度下水蒸气的比焓。
- *W*seg,wall 是壁面段处的湿度比：

  Wseg,wall=min(Wseg,MA,Wseg,s,wall),

  其中 *W*seg,s,wall 是壁面段温度下的饱和湿度比。换句话说，壁面处的湿度比与湿空气流的湿度比相同，但不超过壁面段温度下可支持的最大值。

当 *W*seg,s,wall <
*W*seg,MA 时，壁面上会发生水蒸气冷凝。水蒸气冷凝速率为

m˙w,seg,cond=UAseg,MAc¯pseg,MA(Wseg,MA−Wseg,wall).

该模块假设冷凝水从壁面排出，因此从下游湿空气流中移除。

### 压力损失

两相流体侧的压力损失为

pA,2P−p2P=K2P2m˙A,2Pm˙2A,2P+m˙2thres,2P2ρavg,2PpB,2P−p2P=K2P2m˙B,2Pm˙2B,2P+m˙2thres,2P2ρavg,2P

其中：

- *p*A,2P 和
  *p*B,2P 分别是端口
  **A1** 和 **B1** 处的压力。
- *p*2P 是计算传热时的内部两相流体压力。
- m˙A,2P 和 m˙B,2P 分别是流入端口 **A1** 和
  **B1** 的质量流量。
- *ρ*avg,2P 是所有段上的平均两相流体密度。
- m˙thres,2P 是压力损失的层流阈值，近似为标称质量流量的 1e-4。该模块计算压力损失系数
  *K*2P，使得
  *p*A,2P –
  *p*B,2P 在标称质量流量下与标称压力损失匹配。

湿空气侧的压力损失为

pA,MA−pMA=KMA2m˙A,MAm˙2A,MA+m˙2thres,MA2ρavg,2PpB,MA−pMA=KMA2m˙B,MAm˙2B,MA+m˙2thres,MA2ρavg,MA

其中：

- *p*A,MA 和
  *p*B,MA 分别是端口
  **A2** 和 **B2** 处的压力。
- *p*MA 是计算传热时的内部湿空气压力。
- m˙A,MA 和 m˙B,MA 分别是流入端口 **A2** 和
  **B2** 的质量流量。
- *ρ*avg,MA 是所有段上的平均湿空气密度。
- m˙thres,MA 是压力损失的层流阈值，近似为标称质量流量的 1e-4。该模块计算压力损失系数
  *K*MA，使得
  *p*A,MA –
  *p*B,MA 在标称质量流量下与标称压力损失匹配。

### 两相流体质量和能量守恒

整体两相流体流动的质量守恒方程为

(dp2Pdt∑segments(∂ρseg,2P∂p)+∑segments(duseg,2Pdt∂ρseg,2P∂u))V2PN=m˙A,2P+m˙B,2P,

其中：

- ∂ρseg,2P∂p 是该段密度对压力的偏导数。
- ∂ρseg,2P∂u 是该段密度对比内能的偏导数。
- *u*seg,2P 是该段的比内能。
- *V*2P 是两相流体总体积。

求和针对所有段。

**注意**

尽管该模块将两相流体流划分为 *N*=3 个段以进行传热计算，但它假设所有段处于相同的内部压力
*p*2P。因此，
*p*2P 位于求和之外。

每个段的能量守恒方程为

duseg,2PdtM2PN+useg,2P(m˙seg,in,2P−m˙seg,out,2P)=Φseg,in,2P−Φseg,out,2P+Qseg,2P,

其中：

- *M*2P 是两相流体总质量。
- m˙seg,in,2P 和 m˙seg,out,2P 是流入和流出该段的质量流量。
- *Φ*seg,in,2p 和
  *Φ*seg,out,2p 是流入和流出该段的能量流率。

该模块假设各段之间的质量流量在 m˙A,2P 和 m˙B,2P 的值之间线性分布。

### 湿空气质量与能量守恒

整体湿空气混合物流动的质量守恒为

(dpMAdt∑segments(∂ρseg,MA∂p)+∑segments(dTseg,MAdt∂ρseg,MA∂T+dxw,seg,MAdt∂ρseg,MA∂xw+dxg,seg,MAdt∂ρseg,MA∂xg))VMAN=m˙A,MA+m˙B,MA−∑segments(m˙w,seg,cond+m˙w,seg,conv)+∑segmentsm˙d,seg,evap,

其中：

- ∂ρseg,MA∂p 是该段密度对压力的偏导数。
- ∂ρseg,MA∂T 是该段密度对温度的偏导数。
- ∂ρseg,MA∂xw 是该段密度对比湿度的偏导数。
- ∂ρseg,MA∂xg 是该段密度对痕量气体质量分数的偏导数。
- *x*w,seg,MA 是该段的*比湿度*，也称为水蒸气质量分数。
- *x*g,seg,MA 是该段的痕量气体质量分数。
- *V*MA 是湿空气总体积。
- m˙w,seg,conv 是该段壁面上的冷凝速率。
- m˙d,seg,evap 是该段的水滴蒸发速率。

求和针对所有段。

**注意**

尽管该模块将湿空气流划分为 *N*=3 个段以进行传热计算，但它假设所有段处于相同的内部压力
*p*MA。因此，
*p*MA 位于求和之外。

每个段的能量守恒方程为

dTseg,MAdt(c¯seg,MA−Rseg)MMAN+ua,seg,MA(m˙seg,in,MA−m˙seg,out,MA)+(uw,seg,MA−ua,seg,MA)(m˙w,seg,in,MA−m˙w,seg,out,MA)+(ug,seg,MA−ua,seg,MA)(m˙g,seg,in,MA−m˙g,seg,out,MA)+hd(m˙d,seg,in,MA−m˙d,seg,out,MA)=Φseg,in,MA−Φseg,out,MA+Qseg,MA−(1−λd)(m˙w,seg,condhd+m˙w,seg,convhl,wall),

其中：

- *ua,seg,MA* 是该段的干空气比内能。
- *ug,seg,MA* 是该段的痕量气体比内能。
- *uw,seg,MA* 是该段的水蒸气比内能。
- *MMA* 是湿空气总质量。
- m˙seg,in,MA 和 m˙seg,out,MA 是流入和流出该段的湿空气质量流量。
- m˙w,seg,in,MA 和 m˙w,seg,out,MA 是流入和流出该段的水蒸气质量流量。
- m˙g,seg,in,MA 和 m˙g,seg,out,MA 是流入和流出该段的痕量气体质量流量。
- m˙d,seg,in,MA 和 m˙d,seg,out,MA 是流入和流出该段的水滴质量流量。
- *Rseg* 是该段的体积比气体常数。
- *Φ*seg,in,MA 和
  *Φ*seg,out,MA 是流入和流出该段的能量流率。
- *hd* 是该段中水滴的比焓。
- *λd* 是 **Fraction
  of condensate entrained as water droplets** 参数的值。

该模块假设各段之间的质量流量在 m˙A,MA 和 m˙B,MA 的值之间线性分布。

每个段的水蒸气质量守恒方程为

dxw,seg,MAdtMMAN+xw,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙w,seg,in,MA−m˙w,seg,out,MA−m˙w,seg,cond−m˙w,seg,conv+m˙d,seg,evap.

每个段的痕量气体质量守恒方程为

dxg,seg,MAdtMMAN+xg,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙g,seg,in,MA−m˙g,seg,out,MA.

每个段的水滴质量平衡守恒方程为

drd,segdtMMAN+rd,seg(m˙seg,in,MA−m˙seg,out,MA)=m˙d,seg,in−m˙d,seg,out+λd(m˙w,seg,cond+m˙w,seg,conv)−m˙d,seg,evap,

其中 *rd,seg* 是该段流体体积中水滴与湿空气的质量比。

**注意**

如果 Moist Air Properties
(MA) 模块中的 **Trace gas model** 参数为
`None`，则湿空气网络不建模痕量气体。在这种情况下，在 System-Level Condenser Evaporator (2P-MA) 模块中，痕量气体的守恒方程设置为
0。

如果在 Moist Air Properties (MA) 模块中清除 **Enable entrained water droplets**，则湿空气网络不建模夹带水滴。在这种情况下，在 System-Level Condenser Evaporator (2P-MA) 模块中，水滴的守恒方程设置为 0。

### 假设和限制

- 在确定换热器尺寸时，该模块忽略 **Fraction of condensate entrained as water droplets** 参数的值，并假设冷凝物不夹带为水滴。
