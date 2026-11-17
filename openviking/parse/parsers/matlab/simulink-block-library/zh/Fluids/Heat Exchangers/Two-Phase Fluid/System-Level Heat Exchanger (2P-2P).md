---
type: simulink-block
title: 'System-Level Heat Exchanger (2P-2P)'
family: 'heat-exchangers'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid'
documentation_page: 'systemlevelheatexchanger2p2p'
documentation_source_path: 'ref/systemlevelheatexchanger2p2p.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Heat Exchanger (2P-2P)

## 端口

### 输出

### **Q1** — 传递到两相流体 1 的传热速率，W physical signal

传递到第一个两相流体网络的传热速率，以 physical signal 形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的 physical signal 通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分正在传递的热量。

### **Q2** — 传递到两相流体 2 的传热速率，W physical signal

传递到第二个两相流体网络的传热速率，以 physical signal 形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的 physical signal 通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分正在传递的热量。

### 守恒

### **A1** — 侧 1 上的两相流体端口 two-phase fluid

与第一个两相流体网络关联的入口或出口端口。

### **B1** — 侧 1 上的两相流体端口 two-phase fluid

与第一个两相流体网络关联的入口或出口端口。

### **A2** — 侧 2 上的两相流体端口 two-phase fluid

与第二个两相流体网络关联的入口或出口端口。

### **B2** — 侧 2 上的两相流体端口 two-phase fluid

与第二个两相流体网络关联的入口或出口端口。

## 参数

### 配置

### **Flow arrangement at nominal operating conditions** — 额定工作条件下的流动路径对齐 `Counter flow - Two-Phase Fluid 1 flows from A to B, Two-Phase Fluid 2 flows from B to A` (默认) | `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

额定工作条件下换热器两侧之间的流动路径对齐。可用的流动布置包括：

- `Counter flow - Two-Phase Fluid 1 flows from A to B, Two-Phase Fluid 2 flows from B to A` — 流动彼此平行，方向相反。
- `Parallel flow - Both fluids flow from A to B` — 流动方向相同。
- `Cross flow - Both fluids flow from A to B` — 流动彼此垂直。

在平行流和逆流之间进行选择会影响模块确定换热器尺寸的方式。逆流设置最有效，达到指定性能所需的尺寸最小。相反，平行流效率最低，达到指定性能所需的尺寸最大。

额定条件下的流动方向（从 A 到 B，或从 B 到 A）仅在您选择 **Initialize two-phase fluid 1 to nominal operating conditions** 或 **Initialize two-phase fluid 2 to nominal operating conditions** 时影响模型初始化。如果您设置不同的初始工作条件，流动方向可以不同。

模块确定换热器尺寸后，此设置不再影响模块在仿真期间计算传热的方式。相反，传热取决于仿真期间的流动方向。例如，如果您将参数设置为平行流，但将模型设置为以逆流运行，那么即使其余边界条件相同，仿真期间的传热速率也将与指定的性能不匹配。

如果您将参数设置为交叉流，则模块会将换热器内部的流动路径建模为彼此垂直，因此仿真期间的流动方向无关紧要。

### **Enable wall thermal mass** — 是否启用热质量对传热表面的影响 `off` (默认) | `on`

是否启用热质量对传热表面的影响。当您选择此参数时，模块会向仿真引入额外动态，并且需要更长时间达到稳态，但此参数不影响稳态仿真结果。

如果出口处的流体属性（例如流速方向或流体状态）在仿真期间意外振荡，选择此参数可能有助于稳定结果。

### **Wall mass** — 传热表面的质量 `1 kg` (默认) | 正标量

传热表面的质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 传热表面的比热容 `490 J/(K*kg)` (默认) | 正标量

传热表面的比热容。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Initialize wall temperature to nominal operating conditions** — 用于初始化壁面温度的选项 `on` (默认) | `off`

用于将壁面温度初始化为额定工作条件或指定值的选项。如果您选择此参数，模块将根据为两侧流体指定的额定工作条件计算初始壁面温度。如果您清除此参数，可以直接使用 **Initial wall temperature** 参数指定初始壁面温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Initial wall temperature** — 壁面的初始温度 `293.15 K` (默认) | 正标量或二元素向量

壁面的初始温度。如果您指定标量，模块假定初始壁面温度均匀。如果您指定二元素向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 之间以及端口 **B1** 和 **B2** 之间线性变化。第一个元素对应于端口 **A1** 和 **A2** 处的温度，第二个元素对应于端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**，并清除 **Initialize wall temperature to nominal operating conditions** 复选框。

### **Cross-sectional area at port A1** — 端口 A1 处的流动面积 `0.01 m^2` (默认) | 正标量

两相流体 1 端口 **A1** 处的流动面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流动面积 `0.01 m^2` (默认) | 正标量

两相流体 1 端口 **B1** 处的流动面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流动面积 `0.01 m^2` (默认) | 正标量

两相流体 2 端口 **A2** 处的流动面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2` (默认) | 正标量

两相流体 2 端口 **B2** 处的流动面积。

### 两相流体 1

### **Nominal operating condition** — 额定工作条件 `Heat transfer from Two-Phase Fluid 1 to Two-Phase Fluid 2` (默认) | `Heat transfer from Two-Phase Fluid 2 to Two-Phase Fluid 1`

额定工作条件：

- `Heat transfer from Two-Phase Fluid 1 to Two-Phase Fluid 2` — 侧 1 被冷却，侧 2 被加热。
- `Heat transfer from Two-Phase Fluid 2 to Two-Phase Fluid 1` — 侧 2 被冷却，侧 1 被加热。

此设置仅与额定工作条件参数相关。它并不意味着仿真期间传热只能按指定方向发生。

### **Nominal mass flow rate** — 额定工作条件下两相流体 1 端口之间的质量流量 `0.001 kg/s` (默认) | 正标量

额定工作条件下从端口 **A1** 到端口 **B1** 的质量流量。

### **Nominal pressure drop** — 额定工作条件下两相流体 1 端口之间的压降 `0.01 MPa` (默认) | 正标量

额定工作条件下从端口 **A1** 到端口 **B1** 的压降。

### **Pressure specification** — 选择压力指定方法 `Inlet pressure` (默认) | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

选择压力指定方法：

- `Inlet pressure` — 指定额定入口压力。
- `Saturation pressure at specified saturation temperature` — 指定额定饱和温度。

### **Nominal inlet pressure** — 两相流体 1 入口处的压力 `1 MPa` (默认) | 正标量

额定工作条件下换热器两相流体 1 入口处的压力。

#### 依赖关系

要启用此参数，请将 **Pressure specification** 设置为 `Inlet pressure`。

### **Nominal saturation temperature** — 使用额定饱和温度指定压力 `313.15 K` (默认) | 正标量

额定工作条件下换热器两相流体 1 出口处的饱和温度。换热器中的压力为对应的饱和压力。额定饱和温度必须小于临界温度。

#### 依赖关系

要启用此参数，请将 **Pressure specification** 设置为 `Saturation pressure at specified saturation temperature`。

### **Inlet condition specification** — 选择用于描述两相流体 1 入口条件的量 `Specific enthalpy` (默认) | `Temperature` | `Vapor quality`

用于描述额定工作条件下流体入口条件的量：温度、比焓或蒸汽干度。

### **Nominal inlet specific enthalpy** — 两相流体 1 入口处的比焓 `440 kJ/kg` (默认) | 正标量

额定工作条件下换热器两相流体 1 入口处的比焓。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet temperature** — 两相流体 1 入口处的温度 `313.15 K` (默认) | 正标量

额定工作条件下换热器两相流体 1 入口处的温度。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification** 设置为 `Temperature`。

### **Nominal inlet vapor quality** — 两相流体 1 入口处的蒸汽干度 `1` (默认) | 正标量

额定工作条件下换热器两相流体 1 入口处的蒸汽干度，定义为液-汽混合物中蒸汽的质量分数。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification** 设置为 `Vapor quality`。

### **Heat transfer capacity specification** — 如何指定两相流体 1 的传热能力 `Rate of heat transfer` (默认) | `Outlet condition`

是直接通过传热速率，还是间接通过出口条件来指定额定工作条件下两相流体 1 的换热器性能。

### **Nominal rate of heat transfer** — 传热速率 `0.1 kW` (默认) | 正标量

传热速率。**Nominal Operating condition** 参数确定热量传入和传出的网络：

- 如果 **Nominal operating condition** 为 `Heat transfer from two-phase fluid 1 to two-phase fluid 2`，则此参数是额定工作条件下从两相流体侧 1 到侧 2 的传热速率。
- 如果 **Nominal operating condition** 为 `Heat transfer from two-phase fluid 2 to two-phase fluid 1`，则此参数是额定工作条件下从两相流体侧 2 到侧 1 的传热速率。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Rate of heat transfer`。

### **Outlet condition specification** — 选择用于出口条件指定的量 `Specific enthalpy` (默认) | `Subcooling` | `Superheating` | `Vapor quality`

选择用于出口条件指定的量：

- `Specific enthalpy` — 指定额定比焓。
- `Subcooling` — 指定额定过冷度。如果您将 **Nominal operating condition** 设置为 `Heat transfer from two-phase fluid 1 to two-phase fluid 2`，则此选项可用。
- `Superheating` — 指定额定过热度。如果您将 **Nominal operating condition** 设置为 `Heat transfer from two-phase fluid 2 to two-phase fluid 1`，则此选项可用。
- `Vapor quality` — 指定额定蒸汽干度。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Outlet condition`。

### **Nominal outlet specific enthalpy** — 两相流体 1 出口处的比焓 `250 kJ/kg` (默认) | 正标量 | 二元素向量

额定工作条件下换热器两相流体 1 出口处的比焓。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal subcooling** — 两相流体 1 出口处低于液体饱和温度的温度差 `5 deltaK` (默认) | 正标量

额定工作条件下换热器两相流体 1 出口处低于液体饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Subcooling`。

### **Nominal superheating** — 两相流体 1 出口处高于蒸汽饱和温度的温度差 `5 deltaK` (默认) | 正标量

额定工作条件下换热器两相流体 1 出口处高于蒸汽饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Superheating`。

### **Nominal outlet vapor quality** — 两相流体 1 出口处的蒸汽质量分数 `0` (默认) | 范围 [0,1] 内的标量

额定工作条件下换热器两相流体 1 出口处的两相流体蒸汽干度，定义为液-汽混合物中蒸汽的质量分数。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Vapor quality`。

### **Two-phase fluid 1 volume** — 两相流体 1 的总体积 `0.001 m^3` (默认) | 正标量

换热器内部两相流体 1 的总体积。

### **Initialize two-phase fluid 1 to nominal operating conditions** — 用于初始化两相流体 1 的选项 `on` (默认) | `off`

用于将两相流体初始化为额定工作条件或指定值的选项。如果您选择此参数，模块会将两相流体初始化为额定工作条件。如果您清除此复选框，可以直接使用其他参数指定初始条件。

### **初始流体能量设定** — 两相流体 1 的初始状态 `Specific enthalpy`（默认） | `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

用于描述侧 1 流体初始状态的量：温度、蒸气干度、蒸气空隙率、比焓或比内能。

**初始流体能量设定**参数的值限制了两相流体可用的初始状态。当 **初始流体能量设定** 为：

- `Temperature` — 指定为过冷液体或过热蒸气的初始状态。不能指定液-汽混合物，因为在液-汽混合物区域内温度恒定。
- `Vapor quality` — 指定为液-汽混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域内液体质量分数分别为 0 和 1。此外，模块将压力限制为低于临界压力。
- `Vapor void fraction` — 指定为液-汽混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域内液体质量分数分别为 0 和 1。此外，模块将压力限制为低于临界压力。
- `Specific enthalpy` — 指定流体的比焓。模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。模块不限制初始状态。

#### 依赖关系

要启用此参数，请清除 **将两相流体 1 初始化为额定工况** 复选框。

### **初始两相流体 1 压力** — 仿真开始时的流体 1 压力 `0.101325 MPa`（默认） | positive scalar

仿真开始时两相流体 1 的压力。

#### 依赖关系

要启用此参数，请清除 **将两相流体 1 初始化为额定工况** 复选框。

### **初始两相流体 1 比焓** — 仿真开始时的单位质量焓 `1500 kJ/kg`（默认） | positive scalar | two-element vector

仿真开始时两相流体 1 的比焓。如果该值为 scalar，则初始比焓假定为均匀。如果该值为 two-element vector，则初始比焓假定为在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **将两相流体 1 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Specific enthalpy`。

### **初始两相流体 1 温度** — 仿真开始时的温度 `293.15 K`（默认） | positive scalar | two-element vector

仿真开始时两相流体 1 的温度。如果该值为 scalar，则初始温度假定为均匀。如果该值为 two-element vector，则初始温度假定为在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **将两相流体 1 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Temperature`。

### **初始两相流体 1 蒸气干度** — 仿真开始时的蒸气质量分数 `0.5`（默认） | scalar in the range [0,1] | two-element vector

仿真开始时两相流体 1 的蒸气干度，定义为液-汽混合物中蒸气的质量分数。如果该值为 scalar，则初始蒸气干度假定为均匀。如果该值为 two-element vector，则初始蒸气干度假定为在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除 **将两相流体 1 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Vapor quality`。

### **初始两相流体 1 蒸气空隙率** — 仿真开始时的蒸气体积分数 `0.5`（默认） | scalar in the range [0,1] | two-element vector

仿真开始时两相流体 1 的蒸气空隙率，定义为液-汽混合物中蒸气的体积分数。如果该值为 scalar，则初始蒸气空隙率假定为均匀。如果该值为 two-element vector，则初始蒸气空隙率假定为在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除 **将两相流体 1 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Vapor void fraction`。

### **初始两相流体 1 比内能** — 仿真开始时的单位质量内能 `1500 kJ/kg`（默认） | positive scalar | two-element vector

仿真开始时两相流体 1 的比内能。如果该值为 scalar，则初始比内能假定为均匀。如果该值为 two-element vector，则初始比内能假定为在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **将两相流体 1 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Specific internal energy`。

### Two-Phase Fluid 2

### **额定质量流量** — 额定工况期间两相流体 2 端口之间的质量流量 `0.001 kg/s`（默认） | positive scalar

额定工况期间，从端口 **A2** 到端口 **B2** 的质量流量。

### **额定压降** — 额定工况期间两相流体 2 端口之间的压降 `0.01 MPa`（默认） | positive scalar

额定工况期间，从端口 **A2** 到端口 **B2** 的压降。

### **压力指定** — 选择压力指定的方法 `Inlet pressure`（默认） | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

选择压力指定的方法：

- `Inlet pressure` — 指定额定入口压力。
- `Saturation pressure at specified saturation temperature` — 指定额定饱和温度。

### **额定入口压力** — 两相流体侧入口处的压力 `1 MPa`（默认） | positive scalar

额定工况期间，热交换器两相流体 2 入口处的压力。

#### 依赖关系

要启用此参数，请将 **压力指定** 设置为 `Inlet pressure`。

### **额定饱和温度** — 使用额定饱和温度指定压力 `243.15 K`（默认） | positive scalar

额定工况期间，热交换器两相流体 2 出口处的饱和温度。热交换器中的压力为对应的饱和压力。额定饱和温度必须低于临界温度。

#### 依赖关系

要启用此参数，请将 **压力指定** 设置为 `Saturation pressure at specified saturation temperature`。

### **入口条件指定** — 选择用于描述两相流体 2 入口条件的量 `Specific enthalpy`（默认） | `Temperature` | `Vapor quality`

用于描述额定工况下流体入口条件的量：温度、比焓或蒸气干度。

### **额定入口比焓** — 两相流体 2 入口处的比焓 `250 kJ/kg`（默认） | positive scalar

额定工况期间，热交换器两相流体 2 入口处的比焓。

#### 依赖关系

要启用此参数，请将 **入口条件指定** 设置为 `Specific enthalpy`。

### **额定入口温度** — 两相流体 2 入口处的温度 `237.15 K`（默认） | positive scalar

额定工况期间，热交换器两相流体 2 入口处的温度。

#### 依赖关系

要启用此参数，请将 **入口条件指定** 设置为 `Temperature`。

### **额定入口蒸气干度** — 两相流体 2 入口处的蒸气干度 `0.1`（默认） | positive scalar

额定工况期间，热交换器两相流体 2 入口处的蒸气干度，定义为液-汽混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **入口条件指定** 设置为 `Vapor quality`。

### **两相流体 2 体积** — 两相流体 2 的总体积 `0.001 m^3`（默认） | positive scalar

热交换器内两相流体 2 的总体积。

### **将两相流体 2 初始化为额定工况** — 用于初始化两相流体 2 的选项 `on`（默认） | `off`

用于将两相流体初始化为额定工况或指定值的选项。如果选中此参数，模块会将两相流体初始化为额定工况。如果清除此复选框，可以使用其他参数直接指定初始条件。

### **初始流体能量设定** — 两相流体 2 的初始状态 `Specific enthalpy`（默认） | `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

用于描述侧 2 流体初始状态的量。

**初始流体能量设定**参数的值限制了两相流体可用的初始状态。当 **初始流体能量设定** 为：

- `Temperature` — 指定为过冷液体或过热蒸气的初始状态。不能指定液-汽混合物，因为在液-汽混合物区域内温度恒定。
- `Vapor quality` — 指定为液-汽混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域内液体质量分数分别为 0 和 1。此外，模块将压力限制为低于临界压力。
- `Vapor void fraction` — 指定为液-汽混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域内液体质量分数分别为 0 和 1。此外，模块将压力限制为低于临界压力。
- `Specific enthalpy` — 指定流体的比焓。模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。模块不限制初始状态。

#### 依赖关系

要启用此参数，请清除 **将两相流体 2 初始化为额定工况** 复选框。

### **初始两相流体 2 压力** — 仿真开始时的流体 2 压力 `0.101325 MPa`（默认） | positive scalar

仿真开始时两相流体 2 的压力。

#### 依赖关系

要启用此参数，请清除 **将两相流体 2 初始化为额定工况** 复选框。

### **初始两相流体 2 比焓** — 仿真开始时的单位质量焓 `1500 kJ/kg`（默认） | positive scalar | two-element vector

仿真开始时两相流体 2 的比焓。如果该值为 scalar，则初始比焓假定为均匀。如果该值为 two-element vector，则初始比焓假定为在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **将两相流体 2 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Specific enthalpy`。

### **初始两相流体 2 温度** — 仿真开始时的温度 `293.15 K`（默认） | positive scalar | two-element vector

仿真开始时两相流体 2 的温度。如果该值为 scalar，则初始温度假定为均匀。如果该值为 two-element vector，则初始温度假定为在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **将两相流体 2 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Temperature`。

### **初始两相流体 2 蒸气干度** — 仿真开始时的蒸气质量分数 `0.5`（默认） | scalar in the range [0,1] | two-element vector

仿真开始时两相流体 2 的蒸气干度，定义为液-汽混合物中蒸气的质量分数。如果该值为 scalar，则初始蒸气干度假定为均匀。如果该值为 two-element vector，则初始蒸气干度假定为在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除 **将两相流体 2 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Vapor quality`。

### **初始两相流体 2 蒸气空隙率** — 仿真开始时的蒸气体积分数 `0.5`（默认） | scalar in the range [0,1] | two-element vector

仿真开始时两相流体 2 的蒸气空隙率，定义为液-汽混合物中蒸气的体积分数。如果该值为 scalar，则初始蒸气空隙率假定为均匀。如果该值为 two-element vector，则初始蒸气空隙率假定为在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除 **将两相流体 2 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Vapor void fraction`。

### **初始两相流体 2 比内能** — 仿真开始时的单位质量内能 `1500 kJ/kg`（默认） | positive scalar | two-element vector

仿真开始时两相流体 2 的比内能。如果该值为 scalar，则初始比内能假定为均匀。如果该值为 two-element vector，则初始比内能假定为在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **将两相流体 2 初始化为额定工况** 复选框，并将 **初始流体能量设定** 设置为 `Specific internal energy`。

### 相关系数

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 1 liquid** — 两相流体 1 中过冷液体的关联式系数 `0.023`（默认） | positive scalar

两相流体 1 中过冷液体的努塞尔数关联式中的比例常数，该关联式是雷诺数和普朗特数的函数。默认值基于 Colburn 方程。

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 1 mixture** — 两相流体 1 中液-蒸气混合物的关联式系数 `0.005`（默认） | positive scalar

两相流体 1 中液-蒸气混合物的努塞尔数关联式中的比例常数，该关联式是雷诺数和普朗特数的函数。默认值基于 Cavallini 和 Zecchin 关联式。

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 1 vapor** — 两相流体 1 中过热蒸气的关联式系数 `0.023`（默认） | positive scalar

两相流体 1 中过热蒸气的努塞尔数关联式中的比例常数，该关联式是雷诺数和普朗特数的函数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for two-phase fluid 1** — 两相流体 1 关联式中的雷诺数指数 `0.8`（默认） | positive scalar

两相流体 1 的努塞尔数关联式中的雷诺数指数，该关联式是雷诺数和普朗特数的函数。同一值适用于过冷液体、液-蒸气混合物和过热蒸气。

### **c in Nu = a\*Re^b\*Pr^c for two-phase fluid 1** — 两相流体 1 关联式中的普朗特数指数 `0.33`（默认） | positive scalar

两相流体 1 的努塞尔数关联式中的普朗特数指数，该关联式是雷诺数和普朗特数的函数。同一值适用于过冷液体、液-蒸气混合物和过热蒸气。

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 2 liquid** — 两相流体 2 中过冷液体的关联式系数 `0.023`（默认） | positive scalar

两相流体 2 中过冷液体的努塞尔数关联式中的比例常数，该关联式是雷诺数和普朗特数的函数。默认值基于 Colburn 方程。

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 2 mixture** — 两相流体 2 中液-蒸气混合物的关联式系数 `0.005`（默认） | positive scalar

两相流体 2 中液-蒸气混合物的努塞尔数关联式中的比例常数，该关联式是雷诺数和普朗特数的函数。默认值基于 Cavallini 和 Zecchin 关联式。

### **a in Nu = a\*Re^b\*Pr^c for two-phase fluid 2 vapor** — 两相流体 2 中过热蒸气的关联式系数 `0.023`（默认） | positive scalar

两相流体 2 中过热蒸气的努塞尔数关联式中的比例常数，该关联式是雷诺数和普朗特数的函数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for two-phase fluid 2** — 两相流体 2 关联式中的雷诺数指数 `0.8`（默认） | positive scalar

两相流体 2 的努塞尔数关联式中的雷诺数指数，该关联式是雷诺数和普朗特数的函数。同一值适用于过冷液体、液-蒸气混合物和过热蒸气。

### **c in Nu = a\*Re^b\*Pr^c for two-phase fluid 2** — 两相流体 2 关联式中的普朗特数指数 `0.33`（默认） | positive scalar

两相流体 2 的努塞尔数关联式中的普朗特数指数，该关联式是雷诺数和普朗特数的函数。同一值适用于过冷液体、液-蒸气混合物和过热蒸气。

## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2023b: 指定初始壁温

如果选中 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框，则可以使用新的 **Initial wall temperature** 参数直接指定初始条件。

## 描述

基于两个两相流体网络之间性能数据的换热器

System-Level Heat Exchanger (2P-2P) 模块对两个不同的两相流体网络之间的换热器进行建模。每个网络都有自己的一组流体属性。

该模块使用换热器数据表中的性能数据，而不是换热器的详细几何结构。由于换热，换热器的任一侧或两侧都可以冷凝或汽化流体。您还可以将此模块用作制冷系统中的内部换热器。内部换热器通过在冷凝器出口和蒸发器出口之间提供额外换热，提高制冷系统效率。

您通过标称工况对模块进行参数化。换热器的尺寸设置为在稳态下匹配标称工况下的指定性能。

换热器的每一侧基于沿流动路径的焓变来近似液体区、混合物区和蒸气区。

### 传热

该模块将两相流体 1 流和两相流体 2 流分别划分为三个大小相等的段，并计算每个段内流体之间的传热。为简单起见，本节中的方程针对一个段。

如果清除 **Enable wall thermal mass** 复选框，则换热器中的热平衡为

Qseg,2P1+Qseg,2P2=0,

其中：

- *Q*seg,2P1 是从作为传热表面的壁面到该段中两相流体 1 的热流率。
- *Q*seg,2P2 是从壁面到该段中两相流体 2 的热流率。

如果选中 **Enable wall thermal mass**，则换热器中的热平衡为

Qseg,2P1+Qseg,2P2=−MwallcpwallNdTseg,walldt,

其中：

- *M*wall 是壁面的质量。
- *c*pwall 是壁面的比热容。
- *N* = 3 是段数。
- *T*seg,wall 是该段中的平均壁温。
- *t* 是时间。

从壁面到该段中两相流体 1 的热流率为

Qseg,2P1=UAseg,2P1(Tseg,wall−Tseg,2P1),

其中：

- *UAseg,2P1* 是该段中两相流体 1 的加权平均传热导。
- *Tseg,2P1* 是该段中两相流体 1 的加权平均流体温度。

从壁面到该段中两相流体 2 的热流率为

Qseg,2P2=UAseg,2P2(Tseg,wall−Tseg,2P2),

其中：

- *UAseg,2P2* 是该段中两相流体 2 的加权平均传热导。
- *Tseg,2P2* 是该段中两相流体 2 的加权平均流体温度。

模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 两相流体 1 传热关联式

该模块使用相同的表达式计算两种两相流体中的传热导。

如果该段为过冷液体，则传热导为

UAseg,L,2P1=aL,2P1(Reseg,L,2P1)b2P1(Prseg,L,2P1)c2P1kseg,L,2P1G2P1N,

其中：

- *a*L,2P1、*b*2P1 和 *c*2P1 是努塞尔数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Re*seg,L,2P1 是该段中液体的平均雷诺数。
- *Pr*seg,L,2P1 是该段中液体的平均普朗特数。
- *k*seg,L,2P1 是该段中液体的平均热导率。
- *G*2P1 是换热器两相流体 1 侧的几何比例因子。该模块计算几何比例因子，以使所有段上的总传热量与标称工况下的指定性能匹配。

平均液体雷诺数为

Reseg,L,2P1=m˙seg,2P1Dref,2P1μseg,L,2P1Sref,2P1,

其中：

- m˙seg,2P1 是通过该段的质量流量。
- *μ*seg,L,2P1 是该段中液体的平均动力黏度。
- *D*ref,2P1 是任意参考直径。
- *S*ref,2P1 是任意参考流通面积。

**注意**

此方程中包含 *D*ref,2P1 和 *S*ref,2P1 项仅用于单位计算目的，以使 *Re*seg,L,2P1 无量纲。*D*ref,2P1 和 *S*ref,2P1 的值是任意的，因为 *G*2P1 的计算会覆盖这些值。

类似地，如果该段为过热蒸气，则传热导为

UAseg,V,2P1=aV,2P1(Reseg,V,2P1)b2P1(Prseg,V,2P1)c2P1kseg,V,2P1G2P1N,

其中：

- *a*V,2P1、*b*2P1 和 *c*2P1 是努塞尔数关联式的系数。这些系数在 **Correlation Coefficients** 部分中显示为模块参数。
- *Re*seg,V,2P1 是该段中蒸气的平均雷诺数。
- *Pr*seg,V,2P1 是该段中蒸气的平均普朗特数。
- *k*seg,V,2P1 是该段中蒸气的平均热导率。

平均蒸气雷诺数为

Reseg,V,2P1=m˙seg,2P1Dref,2P1μseg,V,2P1Sref,2P1,

其中 *μ*seg,V,2P1 是该段中蒸气的平均动力黏度。

如果该段为液-蒸气混合物，则传热导为

UAseg,M,2P1=aM,2P1(Reseg,SL,2P1)b2P1CZ(Prseg,SL,2P1)c2P1kseg,SL,2P1G2P1N,

其中：

- *a*M,2P1、*b*2P1 和 *c*2P1 是努塞尔数关联式的系数。这些系数在 **Correlation Coefficients** 部分中显示为模块参数。
- *Re*seg,SL,2P1 是该段中饱和液体的雷诺数。
- *Pr*seg,SL,2P1 是该段中饱和液体的普朗特数。
- *k*seg,SL,2P1 是该段中饱和液体的热导率。
- *CZ* 是 Cavallini 和 Zecchin 项。

饱和液体雷诺数为

Reseg,SL,2P1=m˙seg,2P1Dref,2P1μseg,SL,2P1Sref,2P1,

其中 *μ*seg,SL,2P1 是该段中饱和液体的动力黏度。

Cavallini 和 Zecchin 项为

CZ=((νseg,SV,2P1νseg,SL,2P1−1)(xseg,out,2P1+1))1+b2P1−((νseg,SV,2P1νseg,SL,2P1−1)(xseg,in,2P1+1))1+b2P1(1+b2P1)(νseg,SV,2P1νseg,SL,2P1−1)(xseg,out,2P1−xseg,in,2P1),

其中：

- *ν*seg,SL,2P1 是该段中饱和液体的比体积。
- *ν*seg,SV,2P1 是该段中饱和蒸气的比体积。
- *x*seg,in,2P1 是该段入口处的蒸气干度。
- *x*seg,out,2P1 是该段出口处的蒸气干度。

该表达式基于 Cavallini 和 Zecchin [5] 的工作，其推导了局部蒸气干度 *x* 下的传热系数关联式。液-蒸气混合物的方程是通过在从 *x*seg,in,2P1 到 *x*seg,out,2P1 的段上对 Cavallini 和 Zecchin 关联式取平均得到的。

### 两相流体 1 加权平均

通过一段的两相流体可能并不完全表示为过冷液体、过热蒸气或液-蒸气混合物。相反，每个段可能由这些的组合构成。该模块通过基于该段上的比焓变化以及饱和液体和蒸气比焓计算加权因子（*w*L、*w*V 和 *w*M）来近似此情况。该模块假设该段上的比焓从入口到出口呈分段线性变化，断点对应于液体和蒸气的饱和边界。传热系数较大的区域比传热系数较小的区域具有更陡的斜率。

wL=ΔLΔL+ΔM+ΔVwV=ΔVΔL+ΔM+ΔVwM=1−wL−wV

ΔL=|min(hseg,out,2P1,hseg,SL,2P1)−min(hseg,in,2P1,hseg,SL,2P1)|⋅UAseg,M,2P1⋅UAseg,V,2P1ΔM=|min(max(hseg,out,2P1,hseg,SL,2P1),hseg,SV,2P1)−min(max(hseg,in,2P1,hseg,SL,2P1),hseg,SV,2P1)|⋅UAseg,L,2P1⋅UAseg,V,2P1ΔV=|max(hseg,out,2P1,hseg,SV,2P1)−max(hseg,in,2P1,hseg,SV,2P1)|⋅UAseg,L,2P1⋅UAseg,M,2P1

其中：

- *h*seg,in,2P1 是该段入口处的比焓。
- *h*seg,out,2P1 是该段出口处的比焓。
- *h*seg,SL,2P1 是该段中饱和液体的比焓。
- *h*seg,SV,2P1 是该段中饱和蒸气的比焓。

因此，该段中两相流体 1 的加权平均传热导为

UAseg,2P1=wL(UAseg,L,2P1)+wV(UAseg,V,2P1)+wM(UAseg,M,2P1).

该段中流体 1 的加权平均温度为

Tseg,2P1=wL(UAseg,L,2P1)Tseg,L,2P1+wV(UAseg,V,2P1)Tseg,V,2P1+wM(UAseg,M,2P1)Tseg,M,2P1UAseg,2P1,

其中：

- *T*seg,L,2P1 是该段中液体的平均温度。
- *T*seg,V,2P1 是该段中蒸气的平均温度。
- *T*seg,M,2P1 是该段中混合物的平均温度，即饱和液体温度。

### Two-Phase Fluid 2 传热关联式

如果该段是过冷液体，则传热导为

UAseg,L,2P2=aL,2P2(Reseg,L,2P2)b2P2(Prseg,L,2P2)c2P2kseg,L,2P2G2P2N,

其中：

- *a*L,2P2、
  *b*L,2P2 和
  *c*L,2P2 是 Nusselt
  数关联式的系数。这些系数是 **关联式系数**
  节中的模块参数。
- *Re*seg,L,2P2 是该段的平均液体 Reynolds
  数。
- *Pr*seg,L,2P2 是该段的平均液体 Prandtl
  数。
- *k*seg,L,2P2 是该段的平均液体热
  导率。
- *G*2P2 是热交换器 Two-Phase Fluid 2 侧的几何比例因子。模块计算该几何比例
  因子，以使所有段上的总传热与标称工况下指定的性能匹配。

平均液体 Reynolds 数为

Reseg,L,2P2=m˙seg,2P2Dref,2P2μseg,L,2P2Sref,2P2,

其中：

- m˙seg,2P2 是通过该段的质量流量。
- *μ*seg,L,2P2 是该段的平均液体动力
  黏度。
- *D*ref,2P2 是任意参考
  直径。
- *S*ref,2P2 是任意参考流通
  面积。

**注意**

*D*ref,2P2 和
*S*ref,2P2 项仅出于单位计算目的包含在此方程中，以使
*Re*seg,L,2P2 无量纲。
*D*ref,2P 和
*S*ref,2P2 的值是任意的，因为
*G*2P2 计算会覆盖这些值。

类似地，如果该段是过热蒸气，则传热导为

UAseg,V,2P2=aV,2P2(Reseg,V,2P2)b2P2(Prseg,V,2P2)c2P2kseg,V,2P2G2P2N,

其中：

- *a*V,2P2、
  *b*V,2P2 和
  *c*V,2P2 是 Nusselt
  数关联式的系数。这些系数作为模块参数出现在
  **关联式系数** 节中。
- *Re*seg,V,2P2 是该段的平均蒸气 Reynolds
  数。
- *Pr*seg,V,2P2 是该段的平均蒸气 Prandtl
  数。
- *k*seg,V,2P2 是该段的平均蒸气热
  导率。

平均蒸气 Reynolds 数为

Reseg,V,2P2=m˙seg,2P2Dref,2P2μseg,V,2P2Sref,2P2,

其中 *μ*seg,V,2P2 是该段的平均蒸气动力
黏度。

如果该段是液-蒸气混合物，则传热导为

UAseg,M,2P2=aM,2P2(Reseg,SL,2P2)b2P2CZ(Prseg,SL,2P2)c2P2kseg,SL,2P2G2P2N,

其中：

- *a*M,2P2、
  *b*L,2P2 和
  *c*L,2P2 是 Nusselt
  数关联式的系数。这些系数作为模块参数出现在
  **关联式系数** 节中。
- *Re*seg,SL,2P2 是该段的饱和液体
  Reynolds 数。
- *Pr*seg,SL,2P2 是该段的饱和液体
  Prandtl 数。
- *k*seg,SL,2P2 是该段的饱和液体
  热导率。
- *CZ* 是 Cavallini and Zecchin 项。

饱和液体 Reynolds 数为

Reseg,SL,2P2=m˙seg,2P2Dref,2P2μseg,SL,2P2Sref,2P2,

其中 *μ*seg,SL,2P2 是该段的饱和液体
动力黏度。

Cavallini and Zecchin 项为

CZ=((νseg,SV,2P2νseg,SL,2P2−1)(xseg,out,2P2+1))1+b2P2−((νseg,SV,2P2νseg,SL,2P2−1)(xseg,in,2P2+1))1+b2P2(1+b2P2)(νseg,SV,2P2νseg,SL,2P2−1)(xseg,out,2P2−xseg,in,2P2),

其中：

- *ν*seg,SL,2P2 是该段的饱和液体
  比容。
- *ν*seg,SV,2P2 是该段的饱和蒸气
  比容。
- *x*seg,in,2P2 是该段入口处的蒸气干度。
- *x*seg,out,2P2 是该段出口处的蒸气干度。

该表达式基于 Cavallini and Zecchin [5] 的工作，其推导出局部蒸气干度
*x* 处的传热系数关联式。液-蒸气混合物的方程通过将
Cavallini and Zecchin 的关联式在该段上从
*x*seg,in,2P2 到
*x*seg,out,2P2 求平均得到。

### Two-Phase Fluid 2 加权平均

通过一个段的两相流体流动可能无法完全表示为过冷液体、过热蒸气或液-蒸气混合物中的任一种。相反，每个段可能由这些的组合构成。模块通过基于段内比焓变化以及饱和液体和饱和蒸气比焓计算权重因子（*w*L、
*w*V 和
*w*M）来近似此情况。模块假设段内比焓从入口到出口呈分段线性变化，断点对应于液体和蒸气的饱和边界。传热系数较大的区域比传热系数较低的区域具有更陡的斜率。

wL=ΔLΔL+ΔM+ΔVwV=ΔVΔL+ΔM+ΔVwM=1−wL−wV

ΔL=|min(hseg,out,2P2,hseg,SL,2P2)−min(hseg,in,2P2,hseg,SL,2P2)|⋅UAseg,M,2P2⋅UAseg,V,2P2ΔM=|min(max(hseg,out,2P2,hseg,SL,2P2),hseg,SV,2P2)−min(max(hseg,in,2P2,hseg,SL,2P2),hseg,SV,2P2)|⋅UAseg,L,2P2⋅UAseg,V,2P2ΔV=|max(hseg,out,2P2,hseg,SV,2P2)−max(hseg,in,2P2,hseg,SV,2P2)|⋅UAseg,L,2P2⋅UAseg,M,2P2

其中：

- *h*seg,in,2P2 是该段入口处的比焓。
- *h*seg,out,2P2 是该段出口处的比焓。
- *h*seg,SL,2P2 是该段的饱和液体
  比焓。
- *h*seg,SV,2P2 是该段的饱和蒸气
  比焓。

因此，该段的加权平均 Two-Phase Fluid 2 传热导为

UAseg,2P2=wL(UAseg,L,2P2)+wV(UAseg,V,2P2)+wM(UAseg,M,2P2)。

该段的加权平均流体 2 温度为

Tseg,2P2=wL(UAseg,L,2P2)Tseg,L,2P2+wV(UAseg,V,2P2)Tseg,V,2P2+wM(UAseg,M,2P2)Tseg,M,2P2UAseg,2P2,

其中：

- *T*seg,L,2P2 是该段的平均液体
  温度。
- *T*seg,V,2P2 是该段的平均蒸气
  温度。
- *T*seg,M,2P2 是该段的平均混合物
  温度，即饱和液体温度。

### 压力损失

Two-Phase Fluid 1 侧的压力损失为

pA,2P1−p2P1=K2P12m˙A,2P1m˙2A,2P1+m˙2thres,2P12ρavg,2P1pB,2P1−p2P1=K2P12m˙B,2P1m˙2B,2P1+m˙2thres,2P12ρavg,2P1

其中：

- *p*A,2P1 和
  *p*B,2P1 分别是端口
  **A1** 和 **B1** 处的压力。
- *p*2P1 是计算传热时所用的内部 Two-Phase Fluid 1
  压力。
- m˙A,2P1 和 m˙B,2P1 分别是流入端口 **A1** 和
  **B1** 的质量流量。
- *ρ*avg,2P1 是所有段上的平均 Two-Phase Fluid 1
  密度。
- m˙thres,2P1 是压力损失的层流阈值，近似为标称质量流量的 1e-4。
  模块计算压力损失系数，
  *K*2P1，使得
  *p*A,2P1 –
  *p*B,2P1 在标称质量流量下与
  标称压力损失匹配。

Two-Phase Fluid 2 侧的压力损失为

pA,2P2−p2P2=K2P22m˙A,2P2m˙2A,2P2+m˙2thres,2P22ρavg,2P2pB,2P2−p2P2=K2P22m˙B,2P2m˙2B,2P2+m˙2thres,2P22ρavg,2P2

其中：

- *p*A,2P2 和
  *p*B,2P2 分别是端口
  **A2** 和 **B2** 处的压力。
- *p*2P2 是计算传热时所用的内部 Two-Phase Fluid 2
  压力。
- m˙A,2P2 和 m˙B,2P2 分别是流入端口 **A2** 和
  **B2** 的质量流量。
- *ρ*avg,2P2 是所有段上的平均 Two-Phase Fluid 2
  密度。
- m˙thres,2P2 是压力损失的层流阈值，近似为标称质量流量的 1e-4。
  模块计算压力损失系数，
  *K*2P2，使得
  *p*A,2P2 –
  *p*B,2P2 在标称质量流量下与
  标称压力损失匹配。

### Two-Phase Fluid 1 质量和能量守恒

整体 Two-Phase Fluid 1 流动的质量守恒方程为

(dp2P1dt∑segments(∂ρseg,2P1∂p)+∑segments(duseg,2P1dt∂ρseg,2P1∂u))V2P1N=m˙A,2P1+m˙B,2P1,

其中：

- ∂ρseg,2P1∂p 是该段的密度对压力的偏导数。
- ∂ρseg,2P1∂u 是该段的密度对比内能的偏导数。
- *u*seg,2P1 是该段的比内能。
- *V*2P1 是 Two-Phase Fluid 1
  总体积。

求和针对所有段。

**注意**

尽管模块为传热计算将 Two-Phase Fluid 1 流分成 *N*=3
个段，但它假设所有段处于相同的内部压力，*p*2P1。因此，
*p*2P1 在求和之外。

每个段的能量守恒方程为

duseg,2P1dtM2P1N+useg,2P1(m˙seg,in,2P1−m˙seg,out,2P1)=Φseg,in,2P1−Φseg,out,2P1+Qseg,2P1,

其中：

- *M*2P1 是 Two-Phase Fluid 1
  总质量。
- m˙seg,in,2P1 和 m˙seg,out,2P1 是流入和流出该段的质量流量。
- *Φ*seg,in,2p1 和
  *Φ*seg,out,2p1 是流入和流出该段的能量流率。

模块假设各段之间的质量流量在
m˙A,2P1 和 m˙B,2P1 的值之间线性分布。

### Two-Phase Fluid 2 质量和能量守恒

整体 Two-Phase Fluid 2 流动的质量守恒方程为

(dp2P2dt∑segments(∂ρseg,2P2∂p)+∑segments(duseg,2P2dt∂ρseg,2P2∂u))V2P2N=m˙A,2P2+m˙B,2P2,

其中：

- ∂ρseg,2P2∂p 是该段的密度对压力的偏导数。
- ∂ρseg,2P2∂u 是该段的密度对比内能的偏导数。
- *u*seg,2P2 是该段的比内能。
- *V*2P2 是 Two-Phase Fluid 2
  总体积。

求和针对所有段。

**注意**

尽管模块为传热计算将 Two-Phase Fluid 2 流分成 *N*=3
个段，但它假设所有段处于相同的内部压力，*p*2P2。因此，
*p*2P2 在求和之外。

每个段的能量守恒方程为

duseg,2P2dtM2P2N+useg,2P2(m˙seg,in,2P2−m˙seg,out,2P2)=Φseg,in,2P2−Φseg,out,2P2+Qseg,2P2,

其中：

- *M*2P2 是 Two-Phase Fluid 2
  总质量。
- m˙seg,in,2P2 和 m˙seg,out,2P2 是流入和流出该段的质量流量。
- *Φ*seg,in,2p2 和
  *Φ*seg,out,2p2 是流入和流出该段的能量流率。

模块假设各段之间的质量流量在
m˙A,2P2 和 m˙B,2P2 的值之间线性分布。
