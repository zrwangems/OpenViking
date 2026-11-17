---
type: simulink-block
title: 'System-Level Heat Exchanger (MA-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Moist Air'
documentation_page: 'systemlevelheatexchangermama'
documentation_source_path: 'ref/systemlevelheatexchangermama.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Heat Exchanger (MA-MA)

## 端口

### 输出

### **Q1** — 传递给湿空气 1 的热传递速率，W 物理信号

传递给湿空气 1 的热传递速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果选中 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分被传递的热量。

### **Q2** — 传递给湿空气 2 的热传递速率，W 物理信号

传递给湿空气 2 的热传递速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果选中 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分被传递的热量。

### **W1** — 湿空气 1 冷凝速率，kg/s 物理信号

离开湿空气 1 气流的冷凝水速率，以物理信号形式返回。该端口的值不包括以水滴形式夹带的那部分冷凝水。冷凝水不会积聚在传热表面上。

### **W2** — 湿空气 2 冷凝速率，kg/s 物理信号

离开湿空气 2 气流的冷凝水速率，以物理信号形式返回。该端口的值不包括以水滴形式夹带的那部分冷凝水。冷凝水不会积聚在传热表面上。
### 守恒

### **A1** — 侧 1 上的湿空气端口 湿空气

与侧 1 上的湿空气相关的入口或出口端口。

### **B1** — 侧 1 上的湿空气端口 湿空气

与侧 1 上的湿空气相关的入口或出口端口。

### **A2** — 侧 2 上的湿空气端口 湿空气

与侧 2 上的湿空气相关的入口或出口端口。

### **B2** — 侧 2 上的湿空气端口 湿空气

与侧 2 上的湿空气相关的入口或出口端口。

## 参数

### 配置

### **Flow arrangement at nominal operating conditions** — 流路排列 `Parallel flow - Both fluids flow from A to B`（默认）| `Counter flow - Moist Air 1 flows from A to B, Moist Air 2 flows from B to A` | `Cross flow - Both fluids flow from A to B`

在标称工况下换热器两侧之间的流路排列。可用的流动排列方式有：

- `Parallel flow - Both fluids flow from A to
  B` — 两股流体彼此平行流动，方向相反。
- `Parallel flow - Both fluids flow from A to
  B` — 两股流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to
  B` — 两股流体彼此垂直流动。

平行流和逆流之间的选择会影响模块确定换热器尺寸的方式。逆流设置最为有效，满足指定性能所需的尺寸最小。相反，平行流效率最低，满足指定性能所需的尺寸最大。

标称工况下的流动方向（从 A 到 B，或从 B 到 A）仅在选中 **Initialize moist air 1 to nominal operating conditions** 或 **Initialize moist air 2 to nominal operating conditions** 时影响模型初始化。如果设置不同的初始工况，流动方向可以不同。

在模块确定换热器尺寸之后，此设置不再影响模块在仿真期间计算热传递的方式。相反，热传递取决于仿真期间的流动方向。例如，如果将该参数设置为平行流，但将模型设置为以逆流运行，则即使其余边界条件相同，仿真期间的热传递速率也不会与指定性能匹配。

如果将该参数设置为交叉流，则模块将换热器内部的流路建模为相互垂直，因此仿真期间的流动方向无关紧要。

### **Enable wall thermal mass** — 是否启用热质量对传热表面的影响 `off`（默认）| `on`

是否启用热质量对传热表面的影响。选中此参数时，模块会为仿真引入额外的动态特性，达到稳态需要更长时间，但此参数不影响稳态仿真结果。

### **Wall mass** — 传热表面的质量 `1 kg`（默认）| 正标量

传热表面的质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Wall specific heat** — 传热表面的比热 `490 J/(K*kg)`（默认）| 正标量

传热表面的比热。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Initialize wall temperature to nominal operating conditions** — 初始化壁面温度的选项 `on`（默认）| `off`

将壁面温度初始化为标称工况或指定值的选项。如果选中此参数，模块将根据为两侧流体指定的标称工况计算初始壁面温度。如果清除此参数，可以直接使用 **Initial wall temperature** 参数指定初始壁面温度。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Initial wall temperature** — 壁面的初始温度 `293.15 K`（默认）| 正标量或二元素向量

壁面的初始温度。如果指定标量，模块假定初始壁面温度均匀。如果指定二元素向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 之间以及端口 **B1** 和 **B2** 之间线性变化。第一个元素对应端口 **A1** 和 **A2** 处的温度，第二个元素对应端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **B2** 处的流通面积。

### Moist Air 1

### **Nominal operating condition** — 标称工况 `Heat transfer from Moist Air 1 to Moist Air 2`（默认）| `Heat transfer from Moist Air 2 to Moist Air 1`

标称工况：

- `Heat transfer from Moist Air 1 to Moist Air
  2` — 湿空气 1 被冷却，湿空气 2 被加热。
- `Heat transfer from Moist Air 2 to Moist Air
  1` — 湿空气 2 被冷却，湿空气 1 被加热。

此设置仅与标称工况参数相关。它并不意味着仿真期间热传递只能沿指定方向发生。

### **Nominal mass flow rate** — 标称工况下湿空气 1 端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1** 的质量流量。

### **Nominal pressure drop** — 标称工况下湿空气 1 端口之间的压降 `0.01 MPa`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1** 的压降。

### **Nominal inlet pressure** — 湿空气 1 入口处的压力 `0.101325 MPa`（默认）| 正标量

标称工况下换热器湿空气 1 入口处的压力。

### **Nominal inlet temperature** — 湿空气 1 入口处的温度 `333.15 K`（默认）| 正标量

标称工况下换热器湿空气 1 入口处的温度。

### **Inlet humidity specification** — 用于描述湿空气 1 侧入口处湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述标称工况下入口处湿度水平的量。

### **Nominal inlet relative humidity** — 入口处的相对湿度 `0.5`（默认）| [0,1] 范围内的标量

标称工况下换热器湿空气 1 入口处的相对湿度。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Relative humidity`。

### **Nominal inlet specific humidity** — 入口处的比湿度 `0.01`（默认）| [0,1] 范围内的标量

标称工况下换热器湿空气入口处的比湿度，定义为湿空气 1 混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Specific humidity`。

### **Nominal inlet water vapor mole fraction** — 入口处的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量

标称工况下换热器湿空气入口处湿空气 1 混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Mole fraction`。

### **Nominal inlet humidity ratio** — 入口处的湿度比 `0.01`（默认）| [0,1] 范围内的正标量

标称工况下换热器湿空气 1 入口处的湿度比，定义为水蒸气与干空气及微量气体的质量比。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Humidity ratio`。

### **Nominal inlet wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| [0,1] 范围内的正标量

标称工况下换热器湿空气 1 入口处的湿球温度。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Wet-bulb temperature`。

### **Inlet trace gas specification** — 用于描述入口处微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述标称工况下入口处微量气体水平的量：质量分数或摩尔分数。

### **Nominal inlet trace gas mass fraction** — 入口处微量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量

标称工况下换热器湿空气入口处湿空气 1 混合物中微量气体的质量分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Inlet trace gas specification** 设置为 `Mass fraction`。

### **Nominal inlet trace gas mole fraction** — 入口处微量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量

标称工况下换热器湿空气入口处湿空气 1 混合物中微量气体的摩尔分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Inlet trace gas specification** 设置为 `Mole fraction`。

### **Heat transfer capacity specification** — 如何指定湿空气 1 的热传递能力 `Rate of heat transfer`（默认）| `Outlet condition`

是直接通过热传递速率，还是间接通过出口条件来指定换热器在标称工况下对湿空气 1 的性能。

#### 依赖关系

要启用此参数，请将 **Nominal operating condition** 设置为 `Heat transfer from Moist Air 2 to Moist Air 1`。

### **Nominal rate of heat transfer** — 热传递速率 `1 kW`（默认）| 正标量

热传递速率。**Nominal Operating condition** 参数决定热量从哪个网络传递到哪个网络：

- 如果 **Nominal operating condition** 为 `Heat transfer from Moist Air 1 to Moist Air 2`，则此参数为标称工况下从湿空气 1 到湿空气 2 的热传递速率。
- 如果 **Nominal operating condition** 为 `Heat transfer from Moist Air 2 to Moist Air 1`，则此参数为标称工况下从湿空气 1 到湿空气 2 的热传递速率。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **Nominal operating condition** 为 `Heat transfer from Moist Air 1 to Moist Air 2`。
- **Nominal operating condition** 为 `Heat transfer from Moist Air 2 to Moist Air 1` 且 **Heat transfer capacity specification** 为 `Rate of heat transfer`。

### **Nominal outlet temperature** — 出口温度 `323.15 K`（默认）| 正标量

标称工况下换热器湿空气 1 侧出口处的温度。

#### 依赖关系

要启用此参数，请将 **Nominal operating condition** 设置为 `Heat transfer from Moist Air 2 to Moist Air 1` 并将 **Heat transfer capacity specification** 设置为 `Outlet condition`。

### **Moist air 1 volume** — 换热器侧 1 上湿空气的总体积 `0.1 m^3`（默认）| 正标量

换热器侧 1 上湿空气的总体积。

### **Initialize moist air 1 to nominal operating conditions** — 初始化湿空气 1 的选项 `on`（默认）| `off`

将湿空气 1 初始化为标称工况或指定值的选项。如果选中此参数，模块将湿空气 1 初始化为标称工况。如果清除此复选框，可以直接使用附加参数指定初始条件。

### **Initial moist air 1 pressure** — 仿真开始时湿空气 1 的压力 `0.101325 MPa`（默认）| 正标量

仿真开始时湿空气 1 的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框。

### **Initial moist air 1 temperature** — 仿真开始时湿空气的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时湿空气 1 的温度。如果该值为标量，则假定初始温度均匀。如果该值为二元素向量，则假定初始温度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框。

### **Initial humidity specification** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述初始湿度水平的量：相对湿度、比湿度、水蒸气摩尔分数或湿度比。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框。

### **Initial moist air 1 relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时的湿空气 1 相对湿度。如果该值为标量，则假定初始相对湿度均匀。如果该值为二元素向量，则假定初始相对湿度在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial moist air 1 specific humidity** — 仿真开始时的比湿 `0.01`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时的湿空气 1 比湿，定义为湿空气混合物中水蒸气的质量分数。如果该值为标量，则假定初始比湿均匀。如果该值为二元素向量，则假定初始比湿在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial moist air 1 water vapor mole fraction** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气 1 混合物中水蒸气的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀。如果该值为二元素向量，则假定初始摩尔分数在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial moist air 1 humidity ratio** — 仿真开始时的湿度比 `0.01`（默认）| [0,1] 范围内的正标量 | 二元素向量

仿真开始时的湿空气 1 湿度比，定义为水蒸气与干空气和微量气体的质量比。如果该值为标量，则假定初始湿度比均匀。如果该值为二元素向量，则假定初始湿度比在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial moist air 1 wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| [0,1] 范围内的正标量

仿真开始时的湿球温度。该模块使用此值计算湿度。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始湿球温度。向量值表示入口和出口处的初始湿球温度，形式为 [`inlet`, `outlet`]。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial trace gas specification** — 用于描述初始微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述仿真开始时微量气体水平的量：质量分数或摩尔分数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框。

### **Initial moist air 1 trace gas mass fraction** — 仿真开始时微量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气 1 混合物中微量气体的质量分数。如果该值为标量，则假定初始质量分数均匀。如果该值为二元素向量，则假定初始质量分数在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial moist air 1 trace gas mole fraction** — 仿真开始时微量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气 1 混合物中微量气体的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀。如果该值为二元素向量，则假定初始摩尔分数在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气的质量比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 1 to nominal operating conditions** 复选框。

### **Relative humidity at saturation** — 冷凝的相对湿度点 `1`（默认）| 非负标量

冷凝的相对湿度点。高于此值时发生冷凝。在大多数情况下，该值为 1，即 100%。大于 1 的值表示过饱和蒸汽。

### **Water vapor condensation time constant** — 冷凝时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝多余湿度恢复到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸气的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 水滴中冷凝物的比例 `1`（默认）| [0,1] 范围内的标量

湿空气中作为水滴夹带的冷凝物比例。

### Moist Air 2

### **Nominal mass flow rate** — 标称工况期间湿空气 2 端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

标称工况期间从端口 **A2** 到端口 **B2** 的质量流量。

### **Nominal pressure drop** — 标称工况期间湿空气 2 端口之间的压降 `0.001 MPa`（默认）| 正标量

标称工况期间从端口 **A2** 到端口 **B2** 的压降。

### **Nominal inlet pressure** — 湿空气 2 侧入口处的压力 `0.101325 MPa`（默认）| 正标量

标称工况期间热交换器湿空气 2 入口处的压力。

### **Nominal inlet temperature** — 湿空气 2 侧入口处的温度 `293.15 K`（默认）| 正标量

标称工况期间热交换器湿空气 2 入口处的温度。

### **Inlet humidity specification** — 用于描述湿空气侧入口处湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述标称工况期间入口处湿度水平的量。

### **Nominal inlet relative humidity** — 入口处的相对湿度 `0.5`（默认）| [0,1] 范围内的标量

标称工况期间热交换器湿空气 2 入口处的相对湿度。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Relative humidity`。

### **Nominal inlet specific humidity** — 入口处的比湿 `0.01`（默认）| [0,1] 范围内的标量

标称工况期间热交换器湿空气 2 入口处的比湿，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Specific humidity`。

### **Nominal inlet water vapor mole fraction** — 入口处水蒸气的摩尔分数 `0.01`（默认）| [0,1] 范围内的标量

标称工况期间热交换器湿空气 2 入口处湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Mole fraction`。

### **Nominal inlet humidity ratio** — 入口处的湿度比 `0.01`（默认）| [0,1] 范围内的正标量

标称工况期间热交换器湿空气 2 入口处的湿度比，定义为水蒸气与干空气和微量气体的质量比。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Humidity ratio`。

### **Nominal inlet wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| [0,1] 范围内的正标量

标称工况期间热交换器湿空气 2 入口处的湿球温度。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification** 设置为 `Wet-bulb temperature`。

### **Inlet trace gas specification** — 用于描述入口处微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述标称工况期间入口处微量气体水平的量：质量分数或摩尔分数。

### **Nominal inlet trace gas mass fraction** — 入口处微量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量

标称工况期间热交换器湿空气 2 入口处湿空气混合物中微量气体的质量分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Inlet trace gas specification** 设置为 `Mass fraction`。

### **Nominal inlet trace gas mole fraction** — 入口处微量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量

标称工况期间热交换器湿空气 2 入口处湿空气混合物中微量气体的摩尔分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Inlet trace gas specification** 设置为 `Mole fraction`。

### **Moist air 2 volume** — 热交换器侧 2 湿空气的总体积 `0.1 m^3`（默认）| 正标量

热交换器侧 2 湿空气的总体积。

### **Initialize moist air 2 to nominal operating conditions** — 初始化湿空气的选项 `on`（默认）| `off`

将湿空气 2 初始化为标称工况或指定值的选项。如果选择此参数，该模块将湿空气初始化为标称工况。如果清除此复选框，则可以使用附加参数直接指定初始条件。

### **Initial moist air 2 pressure** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的湿空气 2 压力。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框。

### **Initial moist air 2 temperature** — 仿真开始时的湿空气温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时的湿空气 2 温度。如果该值为标量，则假定初始温度均匀。如果该值为二元素向量，则假定初始温度在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框。

### **Initial humidity specification** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述初始湿度水平的量：相对湿度、比湿、水蒸气摩尔分数或湿度比。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框。

### **Initial moist air 2 relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时的湿空气 2 相对湿度。如果该值为标量，则假定初始相对湿度均匀。如果该值为二元素向量，则假定初始相对湿度在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial moist air 2 specific humidity** — 仿真开始时的比湿 `0.01`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时的湿空气 2 比湿，定义为湿空气混合物中水蒸气的质量分数。如果该值为标量，则假定初始比湿均匀。如果该值为二元素向量，则假定初始比湿在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial moist air 2 water vapor mole fraction** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气 2 混合物中水蒸气的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀。如果该值为二元素向量，则假定初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial moist air 2 humidity ratio** — 仿真开始时的湿度比 `0.01`（默认）| [0,1] 范围内的正标量 | 双元素向量

仿真开始时湿空气 2 的湿度比，定义为水蒸气与干空气和微量气体的质量比。如果该值为标量，则假定初始湿度比均匀分布。如果该值为双元素向量，则假定初始湿度比在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial moist air 2 wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| [0,1] 范围内的正标量

仿真开始时的湿球温度。模块使用此值计算湿度。

此参数可以是标量或双元素向量。标量值表示通道中的平均初始湿球温度。向量值表示入口和出口处的初始湿球温度，形式为 [`inlet`、`outlet`]。模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial trace gas specification** — 用于描述初始微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述仿真开始时微量气体水平的量：质量分数或摩尔分数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框。

### **Initial moist air 2 trace gas mass fraction** — 仿真开始时微量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量 | 双元素向量

仿真开始时湿空气混合物中微量气体的质量分数。如果该值为标量，则假定初始质量分数均匀分布。如果该值为双元素向量，则假定初始质量分数在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial moist air 2 trace gas mole fraction** — 仿真开始时微量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量 | 双元素向量

仿真开始时湿空气 2 混合物中微量气体的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀分布。如果该值为双元素向量，则假定初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气的比率 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air 2 to nominal operating conditions** 复选框。

### **Relative humidity at saturation** — 冷凝的相对湿度点 `1`（默认）| 非负标量

冷凝的相对湿度点。高于此值时发生冷凝。在大多数情况下，此值为 1，即 100%。大于 1 的值表示过饱和蒸汽。

### **Water vapor condensation time constant** — 冷凝时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝多余水分回到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸汽的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 水滴中冷凝物的分数 `1`（默认）| [0,1] 范围内的标量

湿空气中被夹带为水滴的冷凝物分数。

### 关联系数

### **a in Nu = a\*Re^b\*Pr^c for moist air 1** — 湿空气 1 的关联系数 `0.023`（默认）| 正标量

湿空气 1 的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for moist air 1** — 湿空气 1 关联式中的 Reynolds 数指数 `0.8`（默认）| 正标量

湿空气 1 的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的 Reynolds 数指数。默认值基于 Colburn 方程。

### **c in Nu = a\*Re^b\*Pr^c for moist air 1** — 湿空气 1 关联式中的 Prandtl 数指数 `0.33`（默认）| 正标量

湿空气 1 的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的 Prandtl 数指数。默认值基于 Colburn 方程。

### **a in Nu = a\*Re^b\*Pr^c for moist air 2** — 湿空气 2 的关联系数 `0.023`（默认）| 正标量

湿空气 2 的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for moist air 2** — 湿空气 2 关联式中的 Reynolds 数指数 `0.8`（默认）| 正标量

湿空气 2 的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的 Reynolds 数指数。默认值基于 Colburn 方程。

### **c in Nu = a\*Re^b\*Pr^c for moist air 2** — 湿空气 2 关联式中的 Prandtl 数指数 `0.33`（默认）| 正标量

湿空气 2 的 Nusselt 数作为 Reynolds 数和 Prandtl 数函数的关联式中的 Prandtl 数指数。默认值基于 Colburn 方程。

## 所属库

Simscape / Fluids / Heat Exchangers / Moist Air

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

基于两个湿空气网络之间性能数据的热交换器

System-Level Heat Exchanger (MA-MA) 模块基于两个不同湿空气网络之间的性能数据对热交换器进行建模。每个网络都有自己的一组流体属性。

该模块使用热交换器数据表中的性能数据，而非热交换器的详细几何结构。您可以在设计迭代期间调整热交换器的尺寸和性能，或对具有不常见几何结构的热交换器进行建模。您还可以在早期设计阶段使用此模块对具有一定性能水平的热交换器进行建模，此时详细的几何数据尚不可用。您通过标称工况对模块进行参数化。热交换器的尺寸设定为在稳态标称工况下匹配指定的性能。

两个湿空气侧均基于与传热表面的对流水蒸气质量传递来建模水蒸气冷凝。模块从湿空气流中去除冷凝水。

### 传热

模块将每个湿空气流分成三个等大小的段，并计算每个段中流体之间的传热。为简单起见，本节中的方程针对一个段。

如果清除 **Enable wall thermal mass** 复选框，则热交换器中的热平衡为

Qseg,MA1+Qseg,MA2=0，

其中：

- *Qseg,MA1* 是从壁面（即传热表面）到段中湿空气侧 1 的热流率。
- *Qseg,MA2* 是从壁面到段中湿空气侧 2 的热流率。

如果选中 **Enable wall thermal mass**，则热交换器中的热平衡为

Qseg,MA1+Qseg,MA2=−MwallcpwallNdTseg,walldt，

其中：

- *M*wall 是壁面的质量。
- *c*pwall 是壁面的比热。
- *N* = 3 是段数。
- *T*seg,wall 是段中的平均壁面温度。
- *t* 是时间。

从壁面到每个段的热流率为

Qseg,MA=UAseg,MAc¯pseg,MA(h¯seg,wall−h¯seg,MA)+m˙w,seg,condhl,wall，

其中：

- *UA*seg,MA 是段中湿空气的传热导率。
- c¯pseg,MA 是段中每单位质量干空气和微量气体的湿空气混合物比热。
- h¯seg,wall 是在平均壁面段温度下每单位质量干空气和微量气体的湿空气混合物焓。
- h¯seg,MA 是段中每单位质量干空气和微量气体的湿空气混合物焓。
- m˙w,seg,cond 是壁面上的水蒸气冷凝速率。
- *h*l,wall 是在平均壁面段温度下液态水的比焓。

在此方程中使用混合物焓同时考虑了温度差异和由于冷凝引起的湿度差异 [3]。

模块在传热计算中使用的流体属性是入口值与流体体积中值的平均值。

**注意**

在方程中，变量上方的横线表示它们是湿空气混合物的量除以干空气和微量气体的质量，而非除以整个混合物的质量。整个混合物包括干空气、水蒸气和微量气体。

### 湿空气传热关联式

热交换器每一侧的传热导率为

UAseg,MA=aMA(Reseg,MA)bMA(Prseg,MA)cMAkseg,MAGMAN，

其中：

- *a*MA、*b*MA 和 *c*MA 是 Nusselt 数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Reseg,MA* 是段中的平均 Reynolds 数。
- *Prseg,MA* 是段中的平均 Prandtl 数。
- *kseg,MA* 是段中的平均热导率。
- *GMA* 是热交换器湿空气侧的几何比例因子。模块计算几何比例因子，使得所有段的总传热在标称工况下匹配指定的性能。

平均 Reynolds 数为

Reseg,MA=m˙seg,MADref,MAμseg,MASref,MA，

其中：

- m˙seg,MA 是通过该段的质量流率。
- *μseg,MA* 是段中的平均动力粘度。
- *Dref,MA* 是任意参考直径。
- *Sref,MA* 是任意参考流通面积。

**注意**

此方程中包含 *Dref,MA* 和 *Sref,MA* 项仅用于单位计算目的，以使 *Reseg,MA* 无量纲。*Dref,MA* 和 *Sref,MA* 的值是任意的，因为 *GMA* 的计算会覆盖这些值。

### 冷凝

描述从壁面到段中湿空气的热流率的方程使用平均湿空气混合物焓 h¯seg,MA 和壁面段湿空气混合物焓 h¯seg,wall。

平均湿空气混合物焓基于通过该段的湿空气流的温度和湿度

h¯seg,MA=hseg,ag,MA+Wseg,MAhseg,w,MA，

其中：

- *h*seg,ag,MA 是段中干空气和微量气体的平均比焓。
- *h*seg,w,MA 是段中水蒸气的平均比焓。
- *W*seg,MA 是段的湿度比。

壁面段湿空气混合物焓基于壁面段的温度和湿度

h¯seg,wall=hseg,ag,wall+Wseg,wallhseg,w,wall，

其中：

- *h*seg,ag,wall 是在壁面段温度下干空气和微量气体的比焓。
- *h*seg,w,wall 是在壁面段温度下水蒸气的比焓。
- *W*seg,wall 是壁面段的湿度比：

  Wseg,wall=min(Wseg,MA,Wseg,s,wall)，

  其中 *W*seg,s,wall 是在壁面段温度下的饱和湿度比。换言之，壁面处的湿度比与湿空气流的湿度比相同，但不超过在壁面段温度下所能支持的最大值。

当 *W*seg,s,wall < *W*seg,MA 时，壁面上发生水蒸气冷凝。水蒸气冷凝速率为

m˙w,seg,cond=UAseg,MAc¯pseg,MA(Wseg,MA−Wseg,wall)。

模块假定冷凝水从壁面排出，因此从下游湿空气流中去除。

### 压力损失

热交换器每一侧的压力损失为

pA,MA−pMA=KMA2m˙A,MAm˙2A,MA+m˙2thres,MA2ρavg,2PpB,MA−pMA=KMA2m˙B,MAm˙2B,MA+m˙2thres,MA2ρavg,MA

其中：

- *pA,MA* 和 *pB,MA* 是端口 **A1** 和 **B1** 或 **A2** 和 **B2** 处的压力。
- *pMA* 是计算传热时的内部湿空气压力。
- m˙A,MA 和 m˙B,MA 是流入端口 **A1** 和 **B1** 或 **A2** 和 **B2** 的质量流率。
- *ρ*avg,MA 是所有段的平均湿空气密度。
- m˙thres,MA 是压力损失的层流阈值，近似为标称质量流率的 1e-4。模块计算压力损失系数 *K*MA，使得 *p*A,MA – *p*B,MA 在标称质量流率下匹配标称压力损失。

### Moist Air Mass and Energy Conservation

换热器每一侧的湿空气混合物总流量的质量守恒方程为

(dpMAdt∑segments(∂ρseg,MA∂p)+∑segments(dTseg,MAdt∂ρseg,MA∂T+dxw,seg,MAdt∂ρseg,MA∂xw+dxg,seg,MAdt∂ρseg,MA∂xg))VMAN=m˙A,MA+m˙B,MA−∑segments(m˙w,seg,cond+m˙w,seg,conv)+∑segmentsm˙d,seg,evap,

其中：

- ∂ρseg,MA∂p 是区段密度对压力的偏导数。
- ∂ρseg,MA∂T 是区段密度对温度的偏导数。
- ∂ρseg,MA∂xw 是区段密度对比湿度的偏导数。
- ∂ρseg,MA∂xg 是区段密度对痕量气体质量分数的偏导数。
- *xw,seg,MA* 是区段的*比湿度*，也称为水蒸气质量分数。
- *xg,seg,MA* 是区段的痕量气体质量分数。
- *VMA* 是湿空气总体积。
- m˙w,seg,conv 是区段壁面上的冷凝速率。
- m˙d,seg,evap 是区段水滴蒸发速率。

求和是对所有区段进行的。

**注意**

尽管该模块在传热计算中将每侧湿空气流分为 *N*=3 个区段，但它假设一侧的所有区段处于相同的内部压力 *p*MA 下。因此，*p*MA 位于求和符号之外。

每个区段的能量守恒方程为

dTseg,MAdt(c¯seg,MA−Rseg)MMAN+ua,seg,MA(m˙seg,in,MA−m˙seg,out,MA)+(uw,seg,MA−ua,seg,MA)(m˙w,seg,in,MA−m˙w,seg,out,MA)+(ug,seg,MA−ua,seg,MA)(m˙g,seg,in,MA−m˙g,seg,out,MA)+hd(m˙d,seg,in,MA−m˙d,seg,out,MA)=Φseg,in,MA−Φseg,out,MA+Qseg,MA−(1−λd)(m˙w,seg,condhd+m˙w,seg,convhl,wall),

其中：

- *ua,seg,MA* 是区段的干空气比内能。
- *ug,seg,MA* 是区段的痕量气体比内能。
- *uw,seg,MA* 是区段的水蒸气比内能。
- *MMA* 是湿空气总质量。
- m˙seg,in,MA 和 m˙seg,out,MA 是流入和流出区段的湿空气质量流量。
- m˙w,seg,in,MA 和 m˙w,seg,out,MA 是流入和流出区段的水蒸气质量流量。
- m˙g,seg,in,MA 和 m˙g,seg,out,MA 是流入和流出区段的痕量气体质量流量。
- m˙d,seg,in,MA 和 m˙d,seg,out,MA 是流入和流出区段的水滴质量流量。
- *Rseg* 是区段体积比气体常数。
- *Φ*seg,in,MA 和 *Φ*seg,out,MA 是流入和流出区段的能量流率。
- *hd* 是区段中水滴的比焓。
- *λd* 是 **Fraction of condensate entrained as water droplets** 参数的值。

该模块假设区段之间的质量流量在 m˙A,MA 和 m˙B,MA 的值之间线性分布。

每个区段的水蒸气质量守恒方程为

dxw,seg,MAdtMMAN+xw,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙w,seg,in,MA−m˙w,seg,out,MA−m˙w,seg,cond−m˙w,seg,conv+m˙d,seg,evap.

每个区段的痕量气体质量守恒方程为

dxg,seg,MAdtMMAN+xg,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙g,seg,in,MA−m˙g,seg,out,MA.

每个区段的水滴质量平衡守恒方程为

drd,segdtMMAN+rd,seg(m˙seg,in,MA−m˙seg,out,MA)=m˙d,seg,in−m˙d,seg,out+λd(m˙w,seg,cond+m˙w,seg,conv)−m˙d,seg,evap,

其中 *rd,seg* 是区段流体体积中水滴与湿空气的质量比。

**注意**

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则湿空气网络不建模痕量气体。在这种情况下，在换热器对应侧的 System-Level Heat Exchanger (MA-MA) 模块中，痕量气体的守恒方程设置为 0。

如果在 Moist Air Properties (MA) 模块中清除 **Enable entrained water droplets**，则湿空气网络不建模夹带水滴。在这种情况下，在换热器对应侧的 System-Level Heat Exchanger (MA-MA) 模块中，水滴的守恒方程设置为 0。

### 假设和限制

- 在确定换热器尺寸时，该模块忽略 **Fraction of condensate entrained as water droplets** 参数的值，并假设冷凝物不以液滴形式夹带。
