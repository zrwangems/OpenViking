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

### **Q1** — 两相流体的传热速率，W 物理信号

两相流体的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 的物理信号通常数值相等且符号相反。但是，如果选择 **启用壁面热质量**，则这两个信号可能具有不同的值，因为壁面可能会吸收并释放部分传递的热量。

### **Q2** — 湿空气的传热速率，W 物理信号

湿空气的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 的物理信号通常数值相等且符号相反。但是，如果选择 **启用壁面热质量**，则这两个信号可能具有不同的值，因为壁面可能会吸收并释放部分传递的热量。

### **W** — 湿空气冷凝速率，kg/s 物理信号

离开湿空气流的冷凝水速率，以物理信号形式返回。此端口的值不包括以水滴形式夹带的冷凝部分。冷凝物不会积聚在换热表面上。
### 守恒

### **A1** — 两相流体端口 两相流体

与两相流体关联的入口或出口端口。

### **B1** — 两相流体端口 两相流体

与两相流体关联的入口或出口端口。

### **A2** — 湿空气端口 湿空气

与湿空气关联的入口或出口端口。

### **B2** — 湿空气端口 湿空气

与湿空气关联的入口或出口端口。

## 参数

### 配置

### **标称工况下的流动布置** — 流道对齐方式 `Counter flow - Two-Phase Fluid 1 flows from A to B, Moist Air 2 flows from B to A` （默认） | `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

标称工况下换热器两侧之间的流道对齐方式。可用的流动布置包括：

- `Counter flow - Two-Phase Fluid 1 flows from A to B, Moist Air 2
  flows from B to A` — 流体彼此平行流动，方向相反。
- `Parallel flow - Both fluids flow from A to B` —
  流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to B` — 流体彼此垂直流动。

平行流与逆流之间的选择会影响该模块确定换热器尺寸的方式。逆流设置最有效，并且满足指定性能所需尺寸最小。相反，平行流效果最差，并且满足指定性能所需尺寸最大。

标称工况下的流动方向（从 A 到 B，或从 B 到 A）仅在您选择 **将两相流体初始化为标称工况** 或 **将湿空气初始化为标称工况** 时影响模型初始化。如果设置不同的初始工况，流动方向可以不同。

在模块确定换热器尺寸之后，此设置不再影响模块在仿真期间计算传热的方式。相反，传热取决于仿真期间的流动方向。例如，如果您将该参数设置为平行流，但将模型设置为以逆流运行，则即使其余边界条件相同，仿真期间的传热速率也将与指定性能不匹配。

如果将该参数设置为交叉流，则该模块会将换热器内部的流道建模为垂直，因此仿真期间的流动方向无关紧要。

### **启用壁面热质量** — 是否启用热质量对换热表面的影响 `off` （默认） | `on`

是否启用热质量对换热表面的影响。当您选择此参数时，该模块会为仿真引入额外的动态特性，并且需要更长时间才能达到稳态，但此参数不会影响稳态仿真结果。

如果出口处的流体属性（例如流量方向或流体状态）在仿真期间意外振荡，选择此参数可能有助于稳定结果。

### **壁面质量** — 换热表面的质量 `1 kg` （默认） | 正标量

换热表面的质量。

#### 依赖关系

要启用此参数，请选择 **启用壁面热质量**。

### **壁面比热容** — 换热表面的比热容 `490 J/(K*kg)` （默认） | 正标量

换热表面的比热容。

#### 依赖关系

要启用此参数，请选择 **启用壁面热质量**。

### **将壁面温度初始化为标称工况** — 用于初始化壁面温度的选项 `on` （默认） | `off`

用于将壁面温度初始化为标称工况或指定值的选项。如果选择此参数，则该模块会根据为两侧流体指定的标称工况计算初始壁面温度。如果清除此参数，则可以直接使用 **初始壁面温度** 参数指定初始壁面温度。

#### 依赖关系

要启用此参数，请选择 **启用壁面热质量**。

### **初始壁面温度** — 壁面的初始温度 `293.15 K` （默认） | 正标量或二元素向量

壁面的初始温度。如果指定标量，则该模块假定初始壁面温度均匀。如果指定二元素向量，则该模块假定初始壁面温度在端口 **A1** 和 **A2** 之间以及端口 **B1** 和 **B2** 之间线性变化。第一个元素对应于端口 **A1** 和 **A2** 处的温度，第二个元素对应于端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选择 **启用壁面热质量**，并清除 **将壁面温度初始化为标称工况** 复选框。

### **端口 A1 处的横截面积** — 端口 A1 处的流通面积 `0.01 m^2` （默认） | 正标量

两相流体端口 **A1** 处的流通面积。

### **端口 B1 处的横截面积** — 端口 B1 处的流通面积 `0.01 m^2` （默认） | 正标量

两相流体端口 **B1** 处的流通面积。

### **端口 A2 处的横截面积** — 端口 A2 处的流通面积 `0.01 m^2` （默认） | 正标量

湿空气端口 **A2** 处的流通面积。

### **端口 B2 处的横截面积** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2` （默认） | 正标量

湿空气端口 **B2** 处的流通面积。

### 两相流体 1

### **标称工况** — 选择标称工况对应于冷凝器还是蒸发器 `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air 2` （默认） | `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid 1`

标称工况：

- `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
  2` — 两相流体被冷却，湿空气被加热。
- `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid 1` — 湿空气被冷却，两相流体被加热。

此设置仅与标称工况参数相关。它并不意味着在仿真期间传热只能沿指定方向发生。

### **标称质量流量** — 标称工况下两相端口之间的质量流量 `0.001 kg/s` （默认） | 正标量

标称工况下从端口 **A1** 到端口 **B1** 的质量流量。

### **标称压降** — 标称工况下两相端口之间的压降 `0.01 MPa` （默认） | 正标量

标称工况下从端口 **A1** 到端口 **B1** 的压降。

### **压力指定** — 选择压力指定方法 `Inlet pressure` （默认） | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

选择压力指定方法：

- `Inlet pressure` — 指定标称入口压力。
- `Saturation pressure at specified condensing
  temperature` — 指定标称冷凝温度。如果将 **标称工况** 设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
  2`，则此选项可用。
- `Saturation pressure at specified evaporating
  temperature` — 指定标称蒸发温度。如果将 **标称工况** 设置为 `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid
  1`，则此选项可用。

### **标称入口压力** — 两相流体侧入口处的压力 `1 MPa` （默认） | 正标量

标称工况下换热器两相流体入口处的压力。

#### 依赖关系

要启用此参数，请将 **压力指定** 设置为 `Inlet pressure`。

### **标称冷凝温度** — 使用标称冷凝温度指定压力 `313.15 K` （默认） | 正标量

标称工况下换热器两相流体出口处的液体饱和温度。换热器中的压力为对应的饱和压力。标称冷凝温度必须低于临界温度。

#### 依赖关系

要启用此参数，请将 **标称工况** 设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
2`，并将 **压力指定** 设置为 `Saturation pressure at specified condensing
temperature`。

### **标称蒸发温度** — 使用标称蒸发温度指定压力 `243.15 K` （默认） | 正标量

标称工况下换热器两相流体出口处的蒸气饱和温度。换热器中的压力为对应的饱和压力。标称蒸发温度必须低于临界温度。

#### 依赖关系

要启用此参数，请将 **标称工况** 设置为 `Evaporator - heat transfer from Moist Air 2 to Two-Phase Fluid
1`，并将 **压力指定** 设置为 `Saturation pressure at specified evaporating
temperature`。

### **入口条件指定** — 选择用于描述两相流体入口条件的量 `Specific enthalpy` （默认） | `Temperature` | `Vapor quality`

用于描述标称工况下流体入口条件的量：温度、比焓或蒸气干度。

### **标称入口比焓** — 两相流体侧入口处的比焓 `440 kJ/kg` （默认） | 正标量

标称工况下换热器两相流体入口处的比焓。

#### 依赖关系

要启用此参数，请将 **入口条件指定** 设置为 `Specific enthalpy`。

### **标称入口温度** — 两相流体侧入口处的温度 `313.15 K` （默认） | 正标量

标称工况下换热器两相流体入口处的温度。

#### 依赖关系

要启用此参数，请将 **入口条件指定** 设置为 `Temperature`。

### **标称入口蒸气干度** — 两相流体侧入口处的蒸气干度 `1` （默认） | 正标量

标称工况下换热器两相流体入口处的蒸气干度，定义为液-气混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **入口条件指定** 设置为 `Vapor quality`。

### **传热能力指定** — 如何指定两相流体的传热能力 `Rate of heat transfer` （默认） | `Outlet condition`

是直接通过传热速率，还是间接通过出口条件来指定标称工况下两相流体的换热器性能。

### **标称传热速率** — 传热速率 `0.1 kW` （默认） | 正标量

传热速率。**标称工况** 参数确定热量从何处向何处传递：

- 如果 **标称工况** 为 `Condenser
  - heat transfer from Two-Phase Fluid 1 to Moist Air 2`，则此参数为标称工况下从两相流体到湿空气的传热速率。
- 如果 **标称工况** 为 `Evaporator
  - heat transfer from Moist Air 2 to Two-Phase Fluid 1`，则此参数为标称工况下从湿空气到两相流体的传热速率。

#### 依赖关系

要启用此参数，请将 **传热能力指定** 设置为 `Rate of heat
transfer`。

### **出口条件指定** — 选择用于出口条件指定的量 `Specific enthalpy` （默认） | `Subcooling` | `Superheating` | `Vapor quality`

选择用于出口条件指定的量：

- `Specific enthalpy` — 指定标称比焓。
- `Subcooling` — 指定标称过冷度。如果将 **标称工况** 设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Moist Air
  2`，则此选项可用。
- `Superheating` — 指定标称过热度。如果将 **标称工况** 设置为 `Evaporator - heat transfer from Moist Air 2
  to Two-Phase Fluid 1`，则此选项可用。
- `Vapor quality` — 指定标称蒸气干度。

#### 依赖关系

要启用此参数，请将 **传热能力指定** 设置为 `Outlet condition`。

### **标称出口比焓** — 两相流体侧出口处的比焓 `250 kJ/kg` （默认） | 正标量 | 二元素向量

标称工况下换热器两相流体出口处的比焓。

#### 依赖关系

要启用此参数，请将 **出口条件指定** 设置为 `Specific enthalpy`。

### **标称过冷度** — 两相流体侧出口处低于液体饱和温度的温度差 `5 deltaK` （默认） | 正标量

标称工况下换热器两相流体出口处低于液体饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **出口条件指定** 设置为 `Subcooling`。

### **标称过热度** — 两相流体侧出口处高于蒸气饱和温度的温度差 `5 deltaK` （默认） | 正标量

标称工况下换热器两相流体出口处高于蒸气饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **出口条件指定** 设置为 `Superheating`。

### **标称出口蒸气干度** — 两相流体侧出口处的蒸气质量分数 `0` （默认） | 范围 [0,1] 内的标量

标称工况下换热器两相流体出口处的两相流体蒸气干度，定义为液-气混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **出口条件指定** 设置为 `Vapor quality`。

### **两相流体体积** — 两相流体的总体积 `0.001 m^3` （默认） | 正标量

换热器内部两相流体的总体积。

### **将两相流体初始化为名义工况** — 用于将两相流体初始化为名义工况或指定值的选项 `on`（默认）| `off`

用于将两相流体初始化为名义工况或指定值的选项。如果选中此参数，模块会将两相流体初始化为名义工况。如果清除此复选框，则可以使用其他参数直接指定初始条件。

### **初始流体能量规格** — 两相流体的初始状态 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

用于描述流体初始状态的量。

**初始流体能量规格**参数的值限制了两相流体可用的初始状态。当**初始流体能量规格**为：

- `Temperature` — 指定初始状态为过冷液体或过热蒸气。不能指定液-蒸气混合物，因为在液-蒸气混合物区域温度是恒定的。
- `Vapor quality` — 指定初始状态为液-蒸气混合物。不能指定过冷液体或过热蒸气，因为在整个区域内液体质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定初始状态为液-蒸气混合物。不能指定过冷液体或过热蒸气，因为在整个区域内液体质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。模块不限制初始状态。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为名义工况**复选框。

### **初始两相流体压力** — 仿真开始时的流体压力 `0.101325 MPa`（默认）| positive scalar

仿真开始时的两相流体压力。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为名义工况**复选框。

### **初始两相流体比焓** — 仿真开始时的单位质量焓 `1500 kJ/kg`（默认）| positive scalar | two-element vector

仿真开始时的两相流体比焓。如果该值为标量，则假定初始比焓均匀。如果该值为 two-element vector，则假定初始比焓在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为名义工况**复选框，并将**初始流体能量规格**设置为 `Specific enthalpy`。

### **初始两相流体温度** — 仿真开始时的温度 `293.15 K`（默认）| positive scalar | two-element vector

仿真开始时的两相流体温度。如果该值为标量，则假定初始温度均匀。如果该值为 two-element vector，则假定初始温度在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为名义工况**复选框，并将**初始流体能量规格**设置为 `Temperature`。

### **初始两相流体蒸气干度** — 仿真开始时的蒸气质量分数 `0.5`（默认）| scalar in the range [0,1] | two-element vector

仿真开始时的两相流体蒸气干度，定义为液-蒸气混合物中蒸气的质量分数。如果该值为标量，则假定初始蒸气干度均匀。如果该值为 two-element vector，则假定初始蒸气干度在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为名义工况**复选框，并将**初始流体能量规格**设置为 `Vapor quality`。

### **初始两相流体蒸气空隙率** — 仿真开始时的蒸气体积分数 `0.5`（默认）| scalar in the range [0,1] | two-element vector

仿真开始时的两相流体蒸气空隙率，定义为液-蒸气混合物中蒸气的体积分数。如果该值为标量，则假定初始蒸气空隙率均匀。如果该值为 two-element vector，则假定初始蒸气空隙率在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为名义工况**复选框，并将**初始流体能量规格**设置为 `Vapor void fraction`。

### **初始两相流体比内能** — 仿真开始时的单位质量内能 `1500 kJ/kg`（默认）| positive scalar | two-element vector

仿真开始时的两相流体比内能。如果该值为标量，则假定初始比内能均匀。如果该值为 two-element vector，则假定初始比内能在端口 **A1** 和 **B1** 之间线性变化，其中第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为名义工况**复选框，并将**初始流体能量规格**设置为 `Specific internal energy`。

### Moist Air 2

### **名义质量流量** — 名义工况期间湿空气端口之间的质量流量 `0.1 kg/s`（默认）| positive scalar

名义工况期间从端口 **A2** 到端口 **B2** 的质量流量。

### **名义压降** — 名义工况期间湿空气端口之间的压降 `0.001 MPa`（默认）| positive scalar

名义工况期间从端口 **A2** 到端口 **B2** 的压降。

### **名义入口压力** — 湿空气侧入口处的压力 `0.101325 MPa`（默认）| positive scalar

名义工况期间换热器湿空气入口处的压力。

### **名义入口温度** — 湿空气侧入口处的温度 `293.15 K`（默认）| positive scalar

名义工况期间换热器湿空气入口处的温度。

### **入口湿度规格** — 用于描述湿空气侧入口处湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述名义工况期间入口处湿度水平的量。

### **名义入口相对湿度** — 入口处的相对湿度 `0.5`（默认）| scalar in the range [0,1]

名义工况期间换热器湿空气入口处的相对湿度。

#### 依赖关系

要启用此参数，请将**入口湿度规格**设置为 `Relative humidity`。

### **名义入口比湿** — 入口处的比湿 `0.01`（默认）| scalar in the range [0,1]

名义工况期间换热器湿空气入口处的比湿，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请将**入口湿度规格**设置为 `Specific humidity`。

### **名义入口水蒸气摩尔分数** — 入口处水蒸气的摩尔分数 `0.01`（默认）| scalar in the range [0,1]

名义工况期间换热器湿空气入口处湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请将**入口湿度规格**设置为 `Mole fraction`。

### **名义入口含湿量** — 入口处的含湿量 `0.01`（默认）| positive scalar in the range [0,1]

名义工况期间换热器湿空气入口处的含湿量，定义为水蒸气与干空气和微量气体的质量比。

#### 依赖关系

要启用此参数，请将**入口湿度规格**设置为 `Humidity ratio`。

### **名义入口湿球温度** — 仿真开始时的湿球温度 `287 K`（默认）| positive scalar in the range [0,1]

名义工况期间换热器湿空气入口处的湿球温度。

#### 依赖关系

要启用此参数，请将**入口湿度规格**设置为 `Wet-bulb temperature`。

### **入口微量气体规格** — 用于描述入口处微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述名义工况期间入口处微量气体水平的量：质量分数或摩尔分数。

### **名义入口微量气体质量分数** — 入口处微量气体的质量分数 `0.001`（默认）| scalar in the range [0,1]

名义工况期间换热器湿空气入口处湿空气混合物中微量气体的质量分数。

如果 Moist Air Properties (MA) 模块中的**微量气体模型**参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将**入口微量气体规格**设置为 `Mass fraction`。

### **名义入口微量气体摩尔分数** — 入口处微量气体的摩尔分数 `0.001`（默认）| scalar in the range [0,1]

名义工况期间换热器湿空气入口处湿空气混合物中微量气体的摩尔分数。

如果 Moist Air Properties (MA) 模块中的**微量气体模型**参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将**入口微量气体规格**设置为 `Mole fraction`。

### **湿空气体积** — 换热器中湿空气的总体积 `0.1 m^3`（默认）| positive scalar

换热器中湿空气的总体积。

### **将湿空气初始化为名义工况** — 用于初始化湿空气的选项 `on`（默认）| `off`

用于将湿空气初始化为名义工况或指定值的选项。如果选中此参数，模块会将湿空气初始化为名义工况。如果清除此复选框，则可以使用其他参数直接指定初始条件。

### **初始湿空气压力** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| positive scalar

仿真开始时的湿空气压力。

#### 依赖关系

要启用此参数，请清除**将湿空气初始化为名义工况**复选框。

### **初始湿空气温度** — 仿真开始时的湿空气温度 `293.15 K`（默认）| positive scalar | two-element vector

仿真开始时的湿空气温度。如果该值为标量，则假定初始温度均匀。如果该值为 two-element vector，则假定初始温度在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除**将湿空气初始化为名义工况**复选框。

### **初始湿度规格** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述初始湿度水平的量：相对湿度、比湿、水蒸气摩尔分数或含湿量。

#### 依赖关系

要启用此参数，请清除**将湿空气初始化为名义工况**复选框。

### **初始湿空气相对湿度** — 仿真开始时的相对湿度 `0.5`（默认）| scalar in the range [0,1] | two-element vector

仿真开始时的湿空气相对湿度。如果该值为标量，则假定初始相对湿度均匀。如果该值为 two-element vector，则假定初始相对湿度在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除**将湿空气初始化为名义工况**复选框，并将**初始湿度规格**设置为 `Relative humidity`。

### **初始湿空气比湿** — 仿真开始时的比湿 `0.01`（默认）| scalar in the range [0,1] | two-element vector

仿真开始时的湿空气比湿，定义为湿空气混合物中水蒸气的质量分数。如果该值为标量，则假定初始比湿均匀。如果该值为 two-element vector，则假定初始比湿在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除**将湿空气初始化为名义工况**复选框，并将**初始湿度规格**设置为 `Specific humidity`。

### **初始湿空气水蒸气摩尔分数** — 仿真开始时水蒸气的摩尔分数 `0.01`（默认）| scalar in the range [0,1] | two-element vector

仿真开始时湿空气混合物中水蒸气的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀。如果该值为 two-element vector，则假定初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除**将湿空气初始化为名义工况**复选框，并将**初始湿度规格**设置为 `Mole fraction`。

### **初始湿空气含湿量** — 仿真开始时的含湿量 `0.01`（默认）| positive scalar in the range [0,1] | two-element vector

仿真开始时的湿空气含湿量，定义为水蒸气与干空气和微量气体的质量比。如果该值为标量，则假定初始含湿量均匀。如果该值为 two-element vector，则假定初始含湿量在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除**将湿空气初始化为名义工况**复选框，并将**初始湿度规格**设置为 `Humidity ratio`。

### **初始湿空气湿球温度** — 仿真开始时的湿球温度 `287 K`（默认）| [0,1] 范围内的正标量

仿真开始时的湿球温度。模块使用此值计算湿度。

此参数可以是标量或二元素向量。标量值表示通道内的平均初始湿球温度。向量值以 [`inlet`, `outlet`] 的形式表示入口和出口处的初始湿球温度。模块计算两个端口之间的线性梯度。入口端口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请清除 **将湿空气初始化为标称运行条件** 复选框，并将 **初始湿度指定** 设置为 `Wet-bulb temperature`。

### **初始痕量气体指定** — 用于描述初始痕量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述仿真开始时痕量气体水平的量：质量分数或摩尔分数。

#### 依赖关系

要启用此参数，请清除 **将湿空气初始化为标称运行条件** 复选框。

### **初始湿空气痕量气体质量分数** — 仿真开始时痕量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气混合物中痕量气体的质量分数。如果该值为标量，则假定初始质量分数均匀。如果该值为二元素向量，则假定初始质量分数在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应于端口 **A2**，第二个元素对应于端口 **B2**。

如果 Moist Air Properties (MA) 模块中的 **痕量气体模型** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **将湿空气初始化为标称运行条件** 复选框，并将 **初始痕量气体指定** 设置为 `Mass fraction`。

### **初始湿空气痕量气体摩尔分数** — 仿真开始时痕量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气混合物中痕量气体的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀。如果该值为二元素向量，则假定初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应于端口 **A2**，第二个元素对应于端口 **B2**。

如果 Moist Air Properties (MA) 模块中的 **痕量气体模型** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **将湿空气初始化为标称运行条件** 复选框，并将 **初始痕量气体指定** 设置为 `Mole fraction`。

### **水滴与湿空气的初始质量比** — 水滴与湿空气之比 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

#### 依赖关系

要启用此参数，请清除 **将湿空气初始化为标称运行条件** 复选框。

### **饱和时的相对湿度** — 凝结的相对湿度点 `1`（默认）| 非负标量

凝结的相对湿度点。高于此值时会发生凝结。在大多数情况下，此值为 1，即 100%。大于 1 的值表示过饱和蒸气。

### **水蒸气凝结时间常数** — 凝结的时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过凝结析出多余水分而恢复到饱和状态的特征时间尺度。

### **水滴蒸发时间常数** — 蒸发的时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸气的特征时间尺度。

### **作为水滴夹带的凝结物分数** — 水滴中凝结物的分数 `1`（默认）| [0,1] 范围内的标量

湿空气中作为水滴夹带的凝结物分数。

### 关联式系数

### **两相流体中的液体在 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过冷液体的关联式系数 `0.023`（默认）| 正标量

两相流体中过冷液体的 Nusselt 数作为 Reynolds 数和 Prandtl 数的函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **两相流体中的混合物在 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中液-汽混合物的关联式系数 `0.005`（默认）| 正标量

两相流体中液-汽混合物的 Nusselt 数作为 Reynolds 数和 Prandtl 数的函数的关联式中的比例常数。默认值基于 Cavallini and Zecchin 关联式。

### **两相流体中的蒸气在 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过热蒸气的关联式系数 `0.023`（默认）| 正标量

两相流体中过热蒸气的 Nusselt 数作为 Reynolds 数和 Prandtl 数的函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **两相流体在 Nu = a\*Re^b\*Pr^c 中的 b** — 两相流体关联式中的 Reynolds 数指数 `0.8`（默认）| 正标量

两相流体的 Nusselt 数作为 Reynolds 数和 Prandtl 数的函数的关联式中的 Reynolds 数指数。同一值适用于过冷液体、液-汽混合物和过热蒸气。

### **两相流体在 Nu = a\*Re^b\*Pr^c 中的 c** — 两相流体关联式中的 Prandtl 数指数 `0.33`（默认）| 正标量

两相流体的 Nusselt 数作为 Reynolds 数和 Prandtl 数的函数的关联式中的 Prandtl 数指数。同一值适用于过冷液体、液-汽混合物和过热蒸气。

### **湿空气在 Nu = a\*Re^b\*Pr^c 中的 a** — 湿空气的关联式系数 `0.005`（默认）| 正标量

湿空气的 Nusselt 数作为 Reynolds 数和 Prandtl 数的函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **湿空气在 Nu = a\*Re^b\*Pr^c 中的 b** — 湿空气关联式中的 Reynolds 数指数 `0.8`（默认）| 正标量

湿空气的 Nusselt 数作为 Reynolds 数和 Prandtl 数的函数的关联式中的 Reynolds 数指数。默认值基于 Colburn 方程。

### **湿空气在 Nu = a\*Re^b\*Pr^c 中的 c** — 湿空气关联式中的 Prandtl 数指数 `0.33`（默认）| 正标量

湿空气的 Nusselt 数作为 Reynolds 数和 Prandtl 数的函数的关联式中的 Prandtl 数指数。默认值基于 Colburn 方程。

## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Moist Air

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **启用夹带水滴**。

### R2024a：新的湿度指定选项

该模块为 **入口湿度指定** 和 **初始湿度指定** 参数增加了新选项。此选项称为 `Wet-bulb temperature`，允许您以湿球温度的形式输入数据。

### R2023b：指定初始壁温

如果选择 **启用壁面热质量** 并清除 **将壁温初始化为标称运行条件** 复选框，则可以使用新的 **初始壁温** 参数直接指定初始条件。

## 描述

基于性能数据的两相流体与湿空气网络之间的热交换器

System-Level Condenser Evaporator (2P-MA) 模块对两相流体网络与湿空气网络之间的热交换器建模。

该模块可根据传热方向在制冷系统中充当冷凝器或蒸发器。该模块使用热交换器数据表中的性能数据，而不是交换器的详细几何结构。您可以在设计迭代期间调整热交换器的尺寸和性能，或对具有不常见几何结构的热交换器建模。您还可以在设计早期阶段使用此模块对具有一定性能水平的热交换器建模，此时详细几何数据尚不可用。

您通过标称运行条件来参数化该模块。热交换器的尺寸设计为在稳态下匹配标称运行条件时的指定性能。

Two-Phase Fluid 1 侧根据沿流动路径的焓变近似表示液体区、混合物区和蒸气区。Moist Air 2 侧基于与传热表面的对流水蒸气质量传递来对水蒸气凝结建模。凝结水从湿空气流中移除。

此模块与 Condenser Evaporator (2P-MA) 模块相似，但使用不同的参数化模型。下表比较了这两个模块：

| Condenser Evaporator (2P-MA) | System-Level Condenser Evaporator (2P-MA) |
| --- | --- |
| 模块参数基于热交换器几何结构 | 模块参数基于性能和运行条件 |
| 热交换器几何结构可能受可用的几何参数选项限制 | 模型与特定热交换器几何结构无关 |
| 您可以通过调整几何参数（例如翅片尺寸和管长）来针对不同性能要求调整模块 | 您可以通过直接指定所需的热和质量流率来针对不同性能要求调整模块 |
| 您可以在并流、逆流或交叉流配置之间选择 | 您可以在标称运行条件下在并流、逆流或交叉流布置之间选择，以帮助确定尺寸 |
| 在广泛的运行条件范围内具有预测准确的结果，前提是 E-NTU 方程和传热系数关联式适用 | 在指定运行条件附近非常准确；远离指定运行条件时准确性可能降低 |
| 传热计算通过使用 E-NTU 模型考虑温度沿流动路径的变化 | 传热计算通过将流动路径分成三段来近似表示温度沿流动路径的变化 |
| 考虑过冷液体、液-汽混合物和过热蒸气的不同流体属性和传热系数 | 考虑过冷液体、液-汽混合物和过热蒸气的不同流体属性和传热系数 |
| 根据几何结构跟踪过冷液体、液-汽混合物和过热蒸气区域的可变区域长度分数 | 使用基于入口和出口之间焓差的加权因子来近似表示过冷液体、液-汽混合物和过热蒸气区域的影响 |
| 考虑湿空气流中的水蒸气凝结和潜热 | 考虑湿空气流中的水蒸气凝结和潜热 |

### 传热

该模块将两相流体流和湿空气流各自分成三个大小相等的段，并计算每个段中流体之间的传热。为简单起见，本节中的方程针对一个段。

如果清除 **启用壁面热质量** 复选框，则热交换器中的热平衡为

Qseg,2P+Qseg,MA=0,

其中：

- *Q*seg,2P 是从作为传热表面的壁面到段内两相流体的热流率。
- *Q*seg,MA 是从壁面到段内湿空气的热流率。

如果选择 **启用壁面热质量**，则热交换器中的热平衡为

Qseg,2P+Qseg,MA=−MwallcpwallNdTseg,walldt,

其中：

- *M*wall 是壁面的质量。
- *c*pwall 是壁面的比热。
- *N* = 3 是段数。
- *T*seg,wall 是段内的平均壁温。
- *t* 是时间。

从壁面到段内两相流体的热流率为

Qseg,2P=UAseg,2P(Tseg,wall−Tseg,2P),

其中：

- *UA*seg,2P 是段内两相流体的加权平均传热导率。
- *T*seg,2P 是段内两相流体的加权平均流体温度。

从壁面到段内湿空气的热流率为

Qseg,MA=UAseg,MAc¯pseg,MA(h¯seg,wall−h¯seg,MA)+m˙w,seg,condhl,wall,

其中：

- *UA*seg,MA 是段内湿空气的传热导率。
- c¯pseg,MA 是段内湿空气混合物的比热，按单位质量干空气和痕量气体计。
- h¯seg,wall 是在平均壁段温度下湿空气混合物的焓，按单位质量干空气和痕量气体计。
- h¯seg,MA 是段内湿空气混合物的焓，按单位质量干空气和痕量气体计。
- m˙w,seg,cond 是壁面上的水蒸气凝结速率。
- *h*l,wall 是在平均壁段温度下液态水的比焓。

在此方程中使用混合物焓，可同时考虑温度差异和因凝结引起的湿度差异 [3]。

模块在传热计算中使用的流体属性是入口处的值与流体体积内的值之间的平均值。

**注意**

对于湿空气量，符号上方的横线表示这些量是混合物量除以仅干空气和痕量气体的质量，而不是除以整个混合物的质量。整个混合物包括干空气、水蒸气和痕量气体。

### 两相流体传热关联式

如果分段是过冷液体，则传热热导为

UAseg,L,2P=aL,2P(Reseg,L,2P)b2P(Prseg,L,2P)c2Pkseg,L,2PG2PN,

其中：

- *a*L,2P、*b*2P 和 *c*2P 是 Nusselt 数关联式的系数。这些系数是 **Correlation Coefficients** 区段中的模块参数。
- *Re*seg,L,2P 是分段的平均液体 Reynolds 数。
- *Pr*seg,L,2P 是分段的平均液体 Prandtl 数。
- *k*seg,L,2P 是分段的平均液体热导率。
- *G*2P 是换热器两相流体侧的几何尺度因子。模块计算几何尺度因子，使所有分段上的总传热量与标称工况下指定性能匹配。

平均液体 Reynolds 数为

Reseg,L,2P=m˙seg,2PDref,2Pμseg,L,2PSref,2P,

其中：

- m˙seg,2P 是通过分段的质量流率。
- *μ*seg,L,2P 是分段的平均液体动力黏度。
- *D*ref,2P 是任意参考直径。
- *S*ref,2P 是任意参考流通面积。

**注意**

*D*ref,2P 和 *S*ref,2P 项包含在此方程中仅用于单位计算目的，以使 *Re*seg,L,2P 无量纲化。*D*ref,2P 和 *S*ref,2P 的值是任意的，因为 *G*2P 计算会覆盖这些值。

类似地，如果分段是过热蒸气，则传热热导为

UAseg,V,2P=aV,2P(Reseg,V,2P)b2P(Prseg,V,2P)c2Pkseg,V,2PG2PN,

其中：

- *a*V,2P、*b*2P 和 *c*2P 是 Nusselt 数关联式的系数。这些系数出现在 **Correlation Coefficients** 区段中作为模块参数。
- *Re*seg,V,2P 是分段的平均蒸气 Reynolds 数。
- *Pr*seg,V,2P 是分段的平均蒸气 Prandtl 数。
- *k*seg,V,2P 是分段的平均蒸气热导率。

平均蒸气 Reynolds 数为

Reseg,V,2P=m˙seg,2PDref,2Pμseg,V,2PSref,2P,

其中 *μ*seg,V,2P 是分段的平均蒸气动力黏度。

如果分段是液-蒸气混合物，则传热热导为

UAseg,M,2P=aM,2P(Reseg,SL,2P)b2PCZ(Prseg,SL,2P)c2Pkseg,SL,2PG2PN,

其中：

- *a*M,2P、*b*2P 和 *c*2P 是 Nusselt 数关联式的系数。这些系数出现在 **Correlation Coefficients** 区段中作为模块参数。
- *Re*seg,SL,2P 是分段的饱和液体 Reynolds 数。
- *Pr*seg,SL,2P 是分段的饱和液体 Prandtl 数。
- *k*seg,SL,2P 是分段的饱和液体热导率。
- *CZ* 是 Cavallini 和 Zecchin 项。

饱和液体 Reynolds 数为

Reseg,SL,2P=m˙seg,2PDref,2Pμseg,SL,2PSref,2P,

其中 *μ*seg,SL,2P 是分段的饱和液体动力黏度。

Cavallini 和 Zecchin 项为

CZ=((νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P+1))1+b2P−((νseg,SV,2Pνseg,SL,2P−1)(xseg,in,2P+1))1+b2P(1+b2P)(νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P−xseg,in,2P),

其中：

- *ν*seg,SL,2P 是分段的饱和液体比容。
- *ν*seg,SV,2P 是分段的饱和蒸气比容。
- *x*seg,in,2P 是分段入口处的蒸气干度。
- *x*seg,out,2P 是分段出口处的蒸气干度。

该表达式基于 Cavallini 和 Zecchin [5] 的工作，其推导了局部蒸气干度 *x* 下的传热系数关联式。液-蒸气混合物的方程通过将 Cavallini 和 Zecchin 的关联式沿分段从 *x*seg,in,2P 到 *x*seg,out,2P 求平均得到。

### 两相流体加权平均

通过分段的两相流体流动可能无法完全表示为过冷液体、过热蒸气或液-蒸气混合物之一。相反，每个分段可能由这些组合构成。模块基于分段上比焓变化以及饱和液体和饱和蒸气比焓计算加权因子（*w*L、*w*V 和 *w*M），以近似此条件。模块假设分段上的比焓从入口到出口呈分段线性变化，拐点对应于液体和蒸气的饱和边界。传热系数较大的区域比传热系数较小的区域具有更陡的斜率。

wL=ΔLΔL+ΔM+ΔVwV=ΔVΔL+ΔM+ΔVwM=1−wL−wV

ΔL=|min(hseg,out,2P,hseg,SL,2P)−min(hseg,in,2P,hseg,SL,2P)|⋅UAseg,M,2P⋅UAseg,V,2PΔM=|min(max(hseg,out,2P,hseg,SL,2P),hseg,SV,2P)−min(max(hseg,in,2P,hseg,SL,2P),hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,V,2PΔV=|max(hseg,out,2P,hseg,SV,2P)−max(hseg,in,2P,hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,M,2P

其中：

- *h*seg,in,2P 是分段入口处的比焓。
- *h*seg,out,2P 是分段出口处的比焓。
- *h*seg,SL,2P 是分段的饱和液体比焓。
- *h*seg,SV,2P 是分段的饱和蒸气比焓。

因此，分段的两相流体加权平均传热热导为

UAseg,2P=wL(UAseg,L,2P)+wV(UAseg,V,2P)+wM(UAseg,M,2P).

分段的加权平均流体温度为

Tseg,2P=wL(UAseg,L,2P)Tseg,L,2P+wV(UAseg,V,2P)Tseg,V,2P+wM(UAseg,M,2P)Tseg,M,2PUAseg,2P,

其中：

- *T*seg,L,2P 是分段的平均液体温度。
- *T*seg,V,2P 是分段的平均蒸气温度。
- *T*seg,M,2P 是分段的平均混合物温度，即饱和液体温度。

### 湿空气传热关联式

传热热导为

UAseg,MA=aMA(Reseg,MA)bMA(Prseg,MA)cMAkseg,MAGMAN,

其中：

- *a*MA、*b*MA 和 *c*MA 是 Nusselt 数关联式的系数。这些系数是 **Correlation Coefficients** 区段中的模块参数。
- *Re*seg,MA 是分段的平均 Reynolds 数。
- *Pr*seg,MA 是分段的平均 Prandtl 数。
- *k*seg,MA 是分段的平均热导率。
- *G*MA 是换热器湿空气侧的几何尺度因子。模块计算几何尺度因子，使所有分段上的总传热量与标称工况下指定性能匹配。

平均 Reynolds 数为

Reseg,MA=m˙seg,MADref,MAμseg,MASref,MA,

其中：

- m˙seg,MA 是通过分段的质量流率。
- *μ*seg,MA 是分段的平均动力黏度。
- *D*ref,MA 是任意参考直径。
- *S*ref,MA 是任意参考流通面积。

**注意**

*D*ref,MA 和 *S*ref,MA 项包含在此方程中仅用于单位计算目的，以使 *Re*seg,MA 无量纲化。*D*ref,MA 和 *S*ref,MA 的值是任意的，因为 *G*MA 计算会覆盖这些值。

### 湿空气冷凝

描述从壁面到分段中湿空气的热流率的方程（Heat Transfer 节中的最后一个方程）使用平均湿空气混合物比焓 h¯seg,MA 和壁面分段湿空气混合物比焓 h¯seg,wall。

平均湿空气混合物比焓基于通过分段的湿空气流的温度和湿度：

h¯seg,MA=hseg,ag,MA+Wseg,MAhseg,w,MA,

其中：

- *h*seg,ag,MA 是分段干空气和微量气体的平均比焓。
- *h*seg,w,MA 是分段水蒸气的平均比焓。
- *W*seg,MA 是分段的含湿量。

壁面分段湿空气混合物比焓基于壁面分段处的温度和湿度：

h¯seg,wall=hseg,ag,wall+Wseg,wallhseg,w,wall,

其中：

- *h*seg,ag,wall 是壁面分段温度下干空气和微量气体的比焓。
- *h*seg,w,wall 是壁面分段温度下水蒸气的比焓。
- *W*seg,wall 是壁面分段处的含湿量：

  Wseg,wall=min(Wseg,MA,Wseg,s,wall),

  其中 *W*seg,s,wall 是壁面分段温度下的饱和含湿量。换句话说，壁面处的含湿量与湿空气流的含湿量相同，但不超过壁面分段温度下可支撑的最大值。

当 *W*seg,s,wall < *W*seg,MA 时，壁面表面发生水蒸气冷凝。水蒸气冷凝速率为

m˙w,seg,cond=UAseg,MAc¯pseg,MA(Wseg,MA−Wseg,wall).

模块假设冷凝水从壁面表面排出，因此从下游湿空气流中移除。

### 压力损失

两相流体侧的压力损失为

pA,2P−p2P=K2P2m˙A,2Pm˙2A,2P+m˙2thres,2P2ρavg,2PpB,2P−p2P=K2P2m˙B,2Pm˙2B,2P+m˙2thres,2P2ρavg,2P

其中：

- *p*A,2P 和 *p*B,2P 分别是端口 **A1** 和 **B1** 处的压力。
- *p*2P 是计算传热时的内部两相流体压力。
- m˙A,2P 和 m˙B,2P 分别是流入端口 **A1** 和 **B1** 的质量流率。
- *ρ*avg,2P 是所有分段上的平均两相流体密度。
- m˙thres,2P 是压力损失的层流阈值，近似为标称质量流率的 1e-4。模块计算压力损失系数 *K*2P，使 *p*A,2P – *p*B,2P 在标称质量流率下与标称压力损失匹配。

湿空气侧的压力损失为

pA,MA−pMA=KMA2m˙A,MAm˙2A,MA+m˙2thres,MA2ρavg,2PpB,MA−pMA=KMA2m˙B,MAm˙2B,MA+m˙2thres,MA2ρavg,MA

其中：

- *p*A,MA 和 *p*B,MA 分别是端口 **A2** 和 **B2** 处的压力。
- *p*MA 是计算传热时的内部湿空气压力。
- m˙A,MA 和 m˙B,MA 分别是流入端口 **A2** 和 **B2** 的质量流率。
- *ρ*avg,MA 是所有分段上的平均湿空气密度。
- m˙thres,MA 是压力损失的层流阈值，近似为标称质量流率的 1e-4。模块计算压力损失系数 *K*MA，使 *p*A,MA – *p*B,MA 在标称质量流率下与标称压力损失匹配。

### 两相流体质量和能量守恒

整体两相流体流动的质量守恒方程为

(dp2Pdt∑segments(∂ρseg,2P∂p)+∑segments(duseg,2Pdt∂ρseg,2P∂u))V2PN=m˙A,2P+m˙B,2P,

其中：

- ∂ρseg,2P∂p 是分段密度对压力的偏导数。
- ∂ρseg,2P∂u 是分段密度对比内能的偏导数。
- *u*seg,2P 是分段的比内能。
- *V*2P 是总两相流体体积。

求和针对所有分段。

**注意**

尽管模块为传热计算将两相流体流动划分为 *N*=3 个分段，但它假设所有分段处于相同内部压力 *p*2P。因此，*p*2P 在求和之外。

每个分段的能量守恒方程为

duseg,2PdtM2PN+useg,2P(m˙seg,in,2P−m˙seg,out,2P)=Φseg,in,2P−Φseg,out,2P+Qseg,2P,

其中：

- *M*2P 是总两相流体质量。
- m˙seg,in,2P 和 m˙seg,out,2P 是流入和流出分段的质量流率。
- *Φ*seg,in,2p 和 *Φ*seg,out,2p 是流入和流出分段的能量流率。

模块假设分段之间的质量流率在 m˙A,2P 和 m˙B,2P 的值之间线性分布。

### 湿空气质量与能量守恒

整体湿空气混合物流动的质量守恒为

(dpMAdt∑segments(∂ρseg,MA∂p)+∑segments(dTseg,MAdt∂ρseg,MA∂T+dxw,seg,MAdt∂ρseg,MA∂xw+dxg,seg,MAdt∂ρseg,MA∂xg))VMAN=m˙A,MA+m˙B,MA−∑segments(m˙w,seg,cond+m˙w,seg,conv)+∑segmentsm˙d,seg,evap,

其中：

- ∂ρseg,MA∂p 是分段密度对压力的偏导数。
- ∂ρseg,MA∂T 是分段密度对温度的偏导数。
- ∂ρseg,MA∂xw 是分段密度对比湿度的偏导数。
- ∂ρseg,MA∂xg 是分段密度对微量气体质量分数的偏导数。
- *x*w,seg,MA 是分段的 *specific humidity*，也称为水蒸气质量分数。
- *x*g,seg,MA 是分段的微量气体质量分数。
- *V*MA 是总湿空气体积。
- m˙w,seg,conv 是分段壁面表面上的冷凝速率。
- m˙d,seg,evap 是分段水滴蒸发速率。

求和针对所有分段。

**注意**

尽管模块为传热计算将湿空气流划分为 *N*=3 个分段，但它假设所有分段处于相同内部压力 *p*MA。因此，*p*MA 在求和之外。

每个分段的能量守恒方程为

dTseg,MAdt(c¯seg,MA−Rseg)MMAN+ua,seg,MA(m˙seg,in,MA−m˙seg,out,MA)+(uw,seg,MA−ua,seg,MA)(m˙w,seg,in,MA−m˙w,seg,out,MA)+(ug,seg,MA−ua,seg,MA)(m˙g,seg,in,MA−m˙g,seg,out,MA)+hd(m˙d,seg,in,MA−m˙d,seg,out,MA)=Φseg,in,MA−Φseg,out,MA+Qseg,MA−(1−λd)(m˙w,seg,condhd+m˙w,seg,convhl,wall),

其中：

- *ua,seg,MA* 是分段干空气的比内能。
- *ug,seg,MA* 是分段微量气体的比内能。
- *uw,seg,MA* 是分段水蒸气的比内能。
- *MMA* 是总湿空气质量。
- m˙seg,in,MA 和 m˙seg,out,MA 是流入和流出分段的湿空气质量流率。
- m˙w,seg,in,MA 和 m˙w,seg,out,MA 是流入和流出分段的水蒸气质量流率。
- m˙g,seg,in,MA 和 m˙g,seg,out,MA 是流入和流出分段的微量气体质量流率。
- m˙d,seg,in,MA 和 m˙d,seg,out,MA 是流入和流出分段的水滴质量流率。
- *Rseg* 是分段体积比气体常数。
- *Φ*seg,in,MA 和 *Φ*seg,out,MA 是流入和流出分段的能量流率。
- *hd* 是分段中水滴的比焓。
- *λd* 是 **Fraction of condensate entrained as water droplets** 参数的值。

模块假设分段之间的质量流率在 m˙A,MA 和 m˙B,MA 的值之间线性分布。

每个分段的水蒸气质量守恒方程为

dxw,seg,MAdtMMAN+xw,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙w,seg,in,MA−m˙w,seg,out,MA−m˙w,seg,cond−m˙w,seg,conv+m˙d,seg,evap.

每个分段的微量气体质量守恒方程为

dxg,seg,MAdtMMAN+xg,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙g,seg,in,MA−m˙g,seg,out,MA.

每个分段的水滴质量平衡守恒方程为

drd,segdtMMAN+rd,seg(m˙seg,in,MA−m˙seg,out,MA)=m˙d,seg,in−m˙d,seg,out+λd(m˙w,seg,cond+m˙w,seg,conv)−m˙d,seg,evap,

其中 *rd,seg* 是分段流体体积中水滴与湿空气的质量比。

**注意**

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则湿空气网络不对微量气体建模。在这种情况下，在 System-Level Condenser Evaporator (2P-MA) 模块中，微量气体的守恒方程设为 0。

如果在 Moist Air Properties (MA) 模块中清除 **Enable entrained water droplets**，则湿空气网络不对夹带的水滴建模。在这种情况下，在 System-Level Condenser Evaporator (2P-MA) 模块中，水滴的守恒方程设为 0。

### 假设和限制

- 在确定换热器尺寸时，模块忽略 **Fraction of condensate entrained as water droplets** 参数的值，并假设冷凝液不以液滴形式被夹带。
