---
type: simulink-block
title: 'System-Level Condenser Evaporator (2P-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid - Gas'
documentation_page: 'systemlevelcondenserevaporator2pg'
documentation_source_path: 'ref/systemlevelcondenserevaporator2pg.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Condenser Evaporator (2P-G)

## 端口
```yaml
ports:
- name: Q1
  summary: 传递给两相流体的传热速率，W，物理信号
  direction: output
- name: Q2
  summary: 传递给气体的传热速率，W，物理信号
  direction: output
- name: A1
  summary: 两相流体端口，两相流体
  direction: conserving
- name: B1
  summary: 两相流体端口，两相流体
  direction: conserving
- name: A2
  summary: 气体端口，气体
  direction: conserving
- name: B2
  summary: 气体端口，气体
  direction: conserving
```

### 输出

### **Q1** — 传递给两相流体的传热速率，W，物理信号

传递给两相流体的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。

### **Q2** — 传递给气体的传热速率，W，物理信号

传递给气体的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。
### 守恒端口

### **A1** — 两相流体端口，两相流体

与两相流体相关的入口或出口端口。

### **B1** — 两相流体端口，两相流体

与两相流体相关的入口或出口端口。

### **A2** — 气体端口，气体

与气体相关的入口或出口端口。

### **B2** — 气体端口，气体

与气体相关的入口或出口端口。
## 参数
```yaml
parameters:
- name: Flow arrangement at nominal operating conditions
  summary: 流路对齐方式 Counter flow - Two-Phase Fluid 1 flows from A to B, Gas 2 flows from B to A（默认）| Parallel flow - Both fluids
    flow from A to B | Cross flow - Both fluids flow from A to B
  group: 配置
- name: Enable wall thermal mass
  summary: 是否启用热质量对传热表面的影响 off（默认）| on
  group: 配置
- name: Wall mass
  summary: 传热表面的质量 1 kg（默认）| 正标量
  group: 配置
- name: Wall specific heat
  summary: 传热表面的比热 490 J/(K*kg)（默认）| 正标量
  group: 配置
- name: Initialize wall temperature to nominal operating conditions
  summary: 壁面温度初始化选项 on（默认）| off
  group: 配置
- name: Initial wall temperature
  summary: 壁面的初始温度 293.15 K（默认）| 正标量或二元素向量
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
- name: Nominal operating condition
  summary: 选择标称工况对应冷凝器还是蒸发器 Condenser - heat transfer from Two-Phase Fluid 1 to Gas 2（默认）| Evaporator - heat transfer from
    Gas 2 to Two-Phase Fluid 1
  group: 两相流体 1
- name: Nominal mass flow rate
  summary: 标称工况下两相端口之间的质量流量 0.001 kg/s（默认）| 正标量
  group: 两相流体 1
- name: Nominal pressure drop
  summary: 标称工况下两相端口之间的压降 0.01 MPa（默认）| 正标量
  group: 两相流体 1
- name: Pressure specification
  summary: 选择压力指定方法 Inlet pressure（默认）| Saturation pressure at specified condensing temperature | Saturation pressure at specified
    evaporating temperature
  group: 两相流体 1
- name: Nominal inlet pressure
  summary: 两相流体侧入口处的压力 1 MPa（默认）| 正标量
  group: 两相流体 1
- name: Nominal condensing temperature
  summary: 使用标称冷凝温度指定压力 313.15 K（默认）| 正标量
  group: 两相流体 1
- name: Nominal evaporating temperature
  summary: 使用标称蒸发温度指定压力 243.15 K（默认）| 正标量
  group: 两相流体 1
- name: Inlet condition specification
  summary: 选择用于描述两相流体入口条件的量 Specific enthalpy（默认）| Temperature | Vapor quality
  group: 两相流体 1
- name: Nominal inlet specific enthalpy
  summary: 两相流体侧入口处的比焓 440 kJ/kg（默认）| 正标量
  group: 两相流体 1
- name: Nominal inlet temperature
  summary: 两相流体侧入口处的温度 313.15 K（默认）| 正标量
  group: 两相流体 1
- name: Nominal inlet vapor quality
  summary: 两相流体侧入口处的蒸气干度 1（默认）| 正标量
  group: 两相流体 1
- name: Heat transfer capacity specification
  summary: 如何指定两相流体的传热能力 Rate of heat transfer（默认）| Outlet condition
  group: 两相流体 1
- name: Nominal rate of heat transfer
  summary: 传热速率 0.1 kW（默认）| 正标量
  group: 两相流体 1
- name: Outlet condition specification
  summary: 选择用于出口条件指定的量 Specific enthalpy（默认）| Subcooling | Superheating | Vapor quality
  group: 两相流体 1
- name: Nominal outlet specific enthalpy
  summary: 两相流体侧出口处的比焓 250 kJ/kg（默认）| 正标量 | 二元素向量
  group: 两相流体 1
- name: Nominal subcooling
  summary: 两相流体侧出口处低于液体饱和温度的温度差 5 deltaK（默认）| 正标量
  group: 两相流体 1
- name: Nominal superheating
  summary: 两相流体侧出口处高于蒸气饱和温度的温度差 5 deltaK（默认）| 正标量
  group: 两相流体 1
- name: Nominal outlet vapor quality
  summary: 两相流体侧出口处的蒸气质量分数 0（默认）| [0,1] 范围内的标量
  group: 两相流体 1
- name: Two-phase fluid volume
  summary: 两相流体的总体积 0.001 m^3（默认）| 正标量
  group: 两相流体 1
- name: Initialize two-phase fluid to nominal operating conditions
  summary: 两相流体初始化选项 on（默认）| off
  group: 两相流体 1
- name: 初始流体能量规格
  summary: 两相流体初始状态 比焓（默认）| 温度 | 蒸气干度 | 蒸气空隙率 | 比内能
  group: 两相流体 1
- name: 初始两相流体压力
  summary: 仿真开始时的流体压力 0.101325 MPa（默认）| 正标量
  group: 两相流体 1
- name: 初始两相流体比焓
  summary: 仿真开始时的单位质量焓 1500 kJ/kg（默认）| 正标量 | 二元素向量
  group: 两相流体 1
- name: 初始两相流体温度
  summary: 仿真开始时的温度 293.15 K（默认）| 正标量 | 二元素向量
  group: 两相流体 1
- name: 初始两相流体蒸气干度
  summary: 仿真开始时的蒸气质量分数 0.5（默认）| [0,1] 范围内的标量 | 二元素向量
  group: 两相流体 1
- name: 初始两相流体蒸气空隙率
  summary: 仿真开始时的蒸气体积分数 0.5（默认）| [0,1] 范围内的标量 | 二元素向量
  group: 两相流体 1
- name: 初始两相流体比内能
  summary: 仿真开始时的单位质量内能 1500 kJ/kg（默认）| 正标量 | 二元素向量
  group: 两相流体 1
- name: 额定质量流量
  summary: 额定工况下气体端口之间的质量流量 0.1 kg/s（默认）| 正标量
  group: 气体 2
- name: 额定压降
  summary: 额定工况下气体端口之间的压降 0.01 MPa（默认）| 正标量
  group: 气体 2
- name: 额定入口压力
  summary: 气体侧入口处的压力 0.101325 MPa（默认）| 正标量
  group: 气体 2
- name: 额定入口温度
  summary: 气体侧入口处的温度 293.15 K（默认）| 正标量
  group: 气体 2
- name: 气体体积
  summary: 热交换器中气体的总体积 0.1 m^3（默认）| 正标量
  group: 气体 2
- name: 将气体初始化为额定工况
  summary: 气体初始化选项 on（默认）| off
  group: 气体 2
- name: 初始气体压力
  summary: 仿真开始时的气体压力 0.101325 MPa（默认）| 正标量
  group: 气体 2
- name: 初始气体温度
  summary: 仿真开始时的气体温度 293.15 K（默认）| 正标量 | 二元素向量
  group: 气体 2
- name: 两相流体液相 Nu = a\*Re^b\*Pr^c 中的 a
  summary: 两相流体中过冷液体的关联系数 0.023（默认）| 正标量
  group: 关联系数
- name: 两相流体混合物 Nu = a\*Re^b\*Pr^c 中的 a
  summary: 两相流体中液-气混合物的关联系数 0.005（默认）| 正标量
  group: 关联系数
- name: 两相流体蒸气 Nu = a\*Re^b\*Pr^c 中的 a
  summary: 两相流体中过热蒸气的关联系数 0.023（默认）| 正标量
  group: 关联系数
- name: 两相流体 Nu = a\*Re^b\*Pr^c 中的 b
  summary: 两相流体关联式中的雷诺数指数 0.8（默认）| 正标量
  group: 关联系数
- name: 两相流体 Nu = a\*Re^b\*Pr^c 中的 c
  summary: 两相流体关联式中的普朗特数指数 0.33（默认）| 正标量
  group: 关联系数
- name: 气体 Nu = a\*Re^b\*Pr^c 中的 a
  summary: 气体的关联系数 0.005（默认）| 正标量
  group: 关联系数
- name: 气体 Nu = a\*Re^b\*Pr^c 中的 b
  summary: 气体关联式中的雷诺数指数 0.8（默认）| 正标量
  group: 关联系数
- name: 气体 Nu = a\*Re^b\*Pr^c 中的 c
  summary: 气体关联式中的普朗特数指数 0.33（默认）| 正标量
  group: 关联系数
```

### 配置

### **Flow arrangement at nominal operating conditions** — 流路对齐方式 `Counter flow - Two-Phase Fluid 1 flows from A to B, Gas 2 flows from B to A`（默认）| `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

在标称工况下换热器两侧之间的流路对齐方式。可用的流动布置方式有：

- `Counter flow - Two-Phase Fluid 1 flows from A to B, Gas 2 flows from B to A` — 两股流体彼此平行流动，方向相反。
- `Parallel flow - Both fluids flow from A to B` — 两股流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to B` — 两股流体彼此垂直流动。

平行流与逆流的选择会影响模块确定换热器尺寸的方式。逆流设置最为有效，满足指定性能所需的尺寸最小。相反，平行流效果最差，满足指定性能所需的尺寸最大。

标称工况下的流动方向（从 A 到 B，或从 B 到 A）仅在您选择 **Initialize two-phase fluid to nominal operating conditions** 或 **Initialize gas to nominal operating conditions** 时影响模型初始化。如果您设置了不同的初始工况，流动方向可以不同。

在模块确定换热器尺寸之后，此设置在仿真期间不影响模块计算传热的方式。相反，传热取决于仿真期间的流动方向。例如，如果您将参数设置为平行流，但将模型设置为以逆流运行，则即使其余边界条件相同，仿真期间的传热速率也不会与指定性能匹配。

如果您将参数设置为叉流，则模块将换热器内部的流路建模为相互垂直，因此仿真期间的流动方向无关紧要。

### **Enable wall thermal mass** — 是否启用热质量对传热表面的影响 `off`（默认）| `on`

是否启用热质量对传热表面的影响。当您选择此参数时，模块会为仿真引入额外的动态特性，达到稳态所需的时间更长，但此参数不影响稳态仿真结果。

如果出口处的流体属性（如流量方向或流体状态）在仿真期间出现意外振荡，选择此参数可能有助于稳定结果。

### **Wall mass** — 传热表面的质量 `1 kg`（默认）| 正标量

传热表面的质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 传热表面的比热 `490 J/(K*kg)`（默认）| 正标量

传热表面的比热。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Initialize wall temperature to nominal operating conditions** — 壁面温度初始化选项 `on`（默认）| `off`

将壁面温度初始化为标称工况或指定值的选项。如果您选择此参数，模块将根据两侧流体指定的标称工况计算初始壁面温度。如果您清除此参数，可以直接使用 **Initial wall temperature** 参数指定初始壁面温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Initial wall temperature** — 壁面的初始温度 `293.15 K`（默认）| 正标量或二元素向量

壁面的初始温度。如果您指定标量，模块假定初始壁面温度是均匀的。如果您指定二元素向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 与端口 **B1** 和 **B2** 之间线性变化。第一个元素对应端口 **A1** 和 **A2** 处的温度，第二个元素对应端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

两相流体端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

两相流体端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

气体端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

气体端口 **B2** 处的流通面积。

### 两相流体 1

### **Nominal operating condition** — 选择标称工况对应冷凝器还是蒸发器 `Condenser - heat transfer from Two-Phase Fluid 1 to Gas 2`（默认）| `Evaporator - heat transfer from Gas 2 to Two-Phase Fluid 1`

标称工况：

- `Condenser - heat transfer from Two-Phase Fluid 1 to Gas 2` — 两相流体被冷却，气体被加热。
- `Evaporator - heat transfer from Gas 2 to Two-Phase Fluid 1` — 气体被冷却，两相流体被加热。

此设置仅与标称工况参数相关。它并不意味着仿真期间传热只能沿指定方向发生。

### **Nominal mass flow rate** — 标称工况下两相端口之间的质量流量 `0.001 kg/s`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1** 的质量流量。

### **Nominal pressure drop** — 标称工况下两相端口之间的压降 `0.01 MPa`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1** 的压降。

### **Pressure specification** — 选择压力指定方法 `Inlet pressure`（默认）| `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

选择压力指定方法：

- `Inlet pressure` — 指定标称入口压力。
- `Saturation pressure at specified condensing temperature` — 指定标称冷凝温度。如果您将 **Nominal operating condition** 设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Gas 2`，则此选项可用。
- `Saturation pressure at specified evaporating temperature` — 指定标称蒸发温度。如果您将 **Nominal operating condition** 设置为 `Evaporator - heat transfer from Gas 2 to Two-Phase Fluid 1`，则此选项可用。

### **Nominal inlet pressure** — 两相流体侧入口处的压力 `1 MPa`（默认）| 正标量

标称工况下换热器两相流体入口处的压力。

#### 依赖关系

要启用此参数，请将 **Pressure specification** 设置为 `Inlet pressure`。

### **Nominal condensing temperature** — 使用标称冷凝温度指定压力 `313.15 K`（默认）| 正标量

标称工况下换热器两相流体出口处的液体饱和温度。换热器中的压力为对应的饱和压力。标称冷凝温度必须低于临界温度。

#### 依赖关系

要启用此参数，请将 **Nominal operating condition** 设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Gas 2`，并将 **Pressure specification** 设置为 `Saturation pressure at specified condensing temperature`。

### **Nominal evaporating temperature** — 使用标称蒸发温度指定压力 `243.15 K`（默认）| 正标量

标称工况下换热器两相流体出口处的蒸气饱和温度。换热器中的压力为对应的饱和压力。标称蒸发温度必须低于临界温度。

#### 依赖关系

要启用此参数，请将 **Nominal operating condition** 设置为 `Evaporator - heat transfer from Gas 2 to Two-Phase Fluid 1`，并将 **Pressure specification** 设置为 `Saturation pressure at specified evaporating temperature`。

### **Inlet condition specification** — 选择用于描述两相流体入口条件的量 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality`

用于描述标称工况下流体入口条件的量：温度、比焓或蒸气干度。

### **Nominal inlet specific enthalpy** — 两相流体侧入口处的比焓 `440 kJ/kg`（默认）| 正标量

标称工况下换热器两相流体入口处的比焓。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet temperature** — 两相流体侧入口处的温度 `313.15 K`（默认）| 正标量

标称工况下换热器两相流体入口处的温度。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification** 设置为 `Temperature`。

### **Nominal inlet vapor quality** — 两相流体侧入口处的蒸气干度 `1`（默认）| 正标量

标称工况下换热器两相流体入口处的蒸气干度，定义为液-气混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification** 设置为 `Vapor quality`。

### **Heat transfer capacity specification** — 如何指定两相流体的传热能力 `Rate of heat transfer`（默认）| `Outlet condition`

是直接通过传热速率指定标称工况下两相流体的换热器性能，还是通过出口条件间接指定。

### **Nominal rate of heat transfer** — 传热速率 `0.1 kW`（默认）| 正标量

传热速率。**Nominal Operating condition** 参数决定热量传递的来源和去向：

- 如果 **Nominal operating condition** 为 `Condenser - heat transfer from Two-Phase Fluid 1 to Gas 2`，则此参数为标称工况下从两相流体传递给气体的传热速率。
- 如果 **Nominal operating condition** 为 `Evaporator - heat transfer from Gas 2 to Two-Phase Fluid 1`，则此参数为标称工况下从气体传递给两相流体的传热速率。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Rate of heat transfer`。

### **Outlet condition specification** — 选择用于出口条件指定的量 `Specific enthalpy`（默认）| `Subcooling` | `Superheating` | `Vapor quality`

选择用于出口条件指定的量：

- `Specific enthalpy` — 指定标称比焓。
- `Subcooling` — 指定标称过冷度。如果您将 **Nominal operating condition** 设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Gas 2`，则此选项可用。
- `Superheating` — 指定标称过热度。如果您将 **Nominal operating condition** 设置为 `Evaporator - heat transfer from Gas 2 to Two-Phase Fluid 1`，则此选项可用。
- `Vapor quality` — 指定标称蒸气干度。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Outlet condition`。

### **Nominal outlet specific enthalpy** — 两相流体侧出口处的比焓 `250 kJ/kg`（默认）| 正标量 | 二元素向量

标称工况下换热器两相流体出口处的比焓。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal subcooling** — 两相流体侧出口处低于液体饱和温度的温度差 `5 deltaK`（默认）| 正标量

标称工况下换热器两相流体出口处低于液体饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Subcooling`。

### **Nominal superheating** — 两相流体侧出口处高于蒸气饱和温度的温度差 `5 deltaK`（默认）| 正标量

标称工况下换热器两相流体出口处高于蒸气饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Superheating`。

### **Nominal outlet vapor quality** — 两相流体侧出口处的蒸气质量分数 `0`（默认）| [0,1] 范围内的标量

标称工况下换热器两相流体出口处的两相流体蒸气干度，定义为液-气混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Vapor quality`。

### **Two-phase fluid volume** — 两相流体的总体积 `0.001 m^3`（默认）| 正标量

换热器内两相流体的总体积。

### **Initialize two-phase fluid to nominal operating conditions** — 两相流体初始化选项 `on`（默认）| `off`

将两相流体初始化为标称工况或指定值的选项。如果您选择此参数，模块将两相流体初始化为标称工况。如果您清除此复选框，可以使用附加参数直接指定初始条件。

### **初始流体能量规格** — 两相流体初始状态 `比焓`（默认）| `温度` | `蒸气干度` | `蒸气空隙率` | `比内能`

用于描述流体初始状态的量。

**初始流体能量规格**参数的值限制了两相流体可用的初始状态。当**初始流体能量规格**为：

- `温度` — 指定初始状态为过冷液体或过热蒸气。不能指定液-气混合物，因为在液-气混合物区域温度是恒定的。
- `蒸气干度` — 指定初始状态为液-气混合物。不能指定过冷液体或过热蒸气，因为在整个区域内液相质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `蒸气空隙率` — 指定初始状态为液-气混合物。不能指定过冷液体或过热蒸气，因为在整个区域内液相质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `比焓` — 指定流体的比焓。该模块不限制初始状态。
- `比内能` — 指定流体的比内能。该模块不限制初始状态。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为额定工况**复选框。

### **初始两相流体压力** — 仿真开始时的流体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的两相流体压力。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为额定工况**复选框。

### **初始两相流体比焓** — 仿真开始时的单位质量焓 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时的两相流体比焓。如果该值为标量，则假定初始比焓均匀。如果该值为二元素向量，则假定初始比焓在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为额定工况**复选框，并将**初始流体能量规格**设置为 `比焓`。

### **初始两相流体温度** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时的两相流体温度。如果该值为标量，则假定初始温度均匀。如果该值为二元素向量，则假定初始温度在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为额定工况**复选框，并将**初始流体能量规格**设置为 `温度`。

### **初始两相流体蒸气干度** — 仿真开始时的蒸气质量分数 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时两相流体的蒸气干度，定义为液-气混合物中蒸气的质量分数。如果该值为标量，则假定初始蒸气干度均匀。如果该值为二元素向量，则假定初始蒸气干度在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为额定工况**复选框，并将**初始流体能量规格**设置为 `蒸气干度`。

### **初始两相流体蒸气空隙率** — 仿真开始时的蒸气体积分数 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时两相流体的蒸气空隙率，定义为液-气混合物中蒸气的体积分数。如果该值为标量，则假定初始蒸气空隙率均匀。如果该值为二元素向量，则假定初始蒸气空隙率在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为额定工况**复选框，并将**初始流体能量规格**设置为 `蒸气空隙率`。

### **初始两相流体比内能** — 仿真开始时的单位质量内能 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时的两相流体比内能。如果该值为标量，则假定初始比内能均匀。如果该值为二元素向量，则假定初始比内能在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除**将两相流体初始化为额定工况**复选框，并将**初始流体能量规格**设置为 `比内能`。

### 气体 2

### **额定质量流量** — 额定工况下气体端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的质量流量。

### **额定压降** — 额定工况下气体端口之间的压降 `0.01 MPa`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的压降。

### **额定入口压力** — 气体侧入口处的压力 `0.101325 MPa`（默认）| 正标量

额定工况下热交换器气体入口处的压力。

### **额定入口温度** — 气体侧入口处的温度 `293.15 K`（默认）| 正标量

额定工况下热交换器气体入口处的温度。

### **气体体积** — 热交换器中气体的总体积 `0.1 m^3`（默认）| 正标量

热交换器中气体的总体积。

### **将气体初始化为额定工况** — 气体初始化选项 `on`（默认）| `off`

将气体初始化为额定工况或指定值的选项。如果选择此参数，该模块将气体初始化为额定工况。如果清除此复选框，则可以通过附加参数直接指定初始条件。

### **初始气体压力** — 仿真开始时的气体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的气体压力。

#### 依赖关系

要启用此参数，请清除**将气体初始化为额定工况**复选框。

### **初始气体温度** — 仿真开始时的气体温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时的气体温度。如果该值为标量，则假定初始温度均匀。如果该值为二元素向量，则假定初始温度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除**将气体初始化为额定工况**复选框。

### 关联系数

### **两相流体液相 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过冷液体的关联系数 `0.023`（默认）| 正标量

两相流体中过冷液体的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

### **两相流体混合物 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中液-气混合物的关联系数 `0.005`（默认）| 正标量

两相流体中液-气混合物的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Cavallini 和 Zecchin 关联式。

### **两相流体蒸气 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过热蒸气的关联系数 `0.023`（默认）| 正标量

两相流体中过热蒸气的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

### **两相流体 Nu = a\*Re^b\*Pr^c 中的 b** — 两相流体关联式中的雷诺数指数 `0.8`（默认）| 正标量

两相流体的努塞尔数作为雷诺数和普朗特数的函数关联式中的雷诺数指数。相同的值适用于过冷液体、液-气混合物和过热蒸气。

### **两相流体 Nu = a\*Re^b\*Pr^c 中的 c** — 两相流体关联式中的普朗特数指数 `0.33`（默认）| 正标量

两相流体的努塞尔数作为雷诺数和普朗特数的函数关联式中的普朗特数指数。相同的值适用于过冷液体、液-气混合物和过热蒸气。

### **气体 Nu = a\*Re^b\*Pr^c 中的 a** — 气体的关联系数 `0.005`（默认）| 正标量

气体的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

### **气体 Nu = a\*Re^b\*Pr^c 中的 b** — 气体关联式中的雷诺数指数 `0.8`（默认）| 正标量

气体的努塞尔数作为雷诺数和普朗特数的函数关联式中的雷诺数指数。默认值基于 Colburn 方程。

### **气体 Nu = a\*Re^b\*Pr^c 中的 c** — 气体关联式中的普朗特数指数 `0.33`（默认）| 正标量

气体的努塞尔数作为雷诺数和普朗特数的函数关联式中的普朗特数指数。默认值基于 Colburn 方程。
## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

基于两相流体和气体网络之间性能数据的热交换器

System-Level Condenser Evaporator (2P-G) 模块对两相流体网络和气体网络之间的热交换器进行建模。

根据热传递的方向，该模块可以在制冷系统中充当冷凝器或蒸发器。该模块使用热交换器数据表中的性能数据，而不是交换器的详细几何结构。您可以在设计迭代期间调整热交换器的尺寸和性能，或对具有不常见几何结构的热交换器进行建模。您还可以在早期设计阶段使用此模块对具有一定性能水平的热交换器进行建模，此时详细的几何数据尚不可用。

您通过额定工况对该模块进行参数化。热交换器的尺寸设定为在稳态下额定工况时匹配指定的性能。

Two-Phase Fluid 1 侧根据沿流动路径的焓变来近似液相区、混合物区和蒸气区。

该模块与 Condenser Evaporator (2P-G) 模块类似，但使用不同的参数化模型。下表比较了这两个模块：

| Condenser Evaporator (2P-G) | System-Level Condenser Evaporator (2P-G) |
| --- | --- |
| 模块参数基于热交换器几何结构 | 模块参数基于性能和工况 |
| 热交换器几何结构可能受可用几何参数选项的限制 | 模型独立于特定的热交换器几何结构 |
| 您可以通过调整几何参数（如翅片尺寸和管长）来调整模块以满足不同的性能要求 | 您可以通过直接指定所需的热量和质量流量来调整模块以满足不同的性能要求 |
| 您可以在平行流、逆流或交叉流配置之间进行选择 | 您可以在额定工况下在平行流、逆流或交叉流布置之间进行选择，以帮助进行尺寸设定 |
| 在广泛的工况范围内具有预测准确性，受 E-NTU 方程和传热系数关联式适用性的约束 | 在指定工况附近结果非常准确；远离指定工况时准确性可能降低 |
| 传热计算使用 E-NTU 模型考虑沿流动路径的温度变化 | 传热计算通过将流动路径分为三段来近似温度变化 |
| 考虑过冷液体、液-气混合物和过热蒸气的不同流体属性和传热系数 | 考虑过冷液体、液-气混合物和过热蒸气的不同流体属性和传热系数 |
| 根据几何结构跟踪过冷液体、液-气混合物和过热蒸气区域的可变区域长度分数 | 使用基于入口和出口之间焓差的加权因子来近似过冷液体、液-气混合物和过热蒸气区域的影响 |

### Heat Transfer

该模块将两相流体流和气体流各分为三个大小相等的段，并计算各段中流体之间的传热。为简单起见，本节中的方程针对一个段。

如果清除 **Enable wall thermal mass** 复选框，则热交换器中的热平衡为

Qseg,2P+Qseg,G=0，

其中：

- *Q*seg,2P 是从壁面（即传热表面）到该段中两相流体的热流率。
- *Q*seg,G 是从壁面到该段中气体的热流率。

如果选中 **Enable wall thermal mass**，则热交换器中的热平衡为

Qseg,2P+Qseg,G=−MwallcpwallNdTseg,walldt，

其中：

- *M*wall 是壁面的质量。
- *c*pwall 是壁面的比热。
- *N* = 3 是段数。
- *T*seg,wall 是该段的平均壁温。
- *t* 是时间。

从壁面到该段中两相流体的热流率为

Qseg,2P=UAseg,2P(Tseg,wall−Tseg,2P)，

其中：

- *UA*seg,2P 是该段中两相流体的加权平均传热导。
- *T*seg,2P 是该段中两相流体的加权平均流体温度。

从壁面到该段中气体的热流率为

Qseg,G=UAseg,G(Tseg,wall−Tseg,G)，

其中：

- *UA*seg,G 是该段中气体的传热导。
- *T*seg,G 是该段中的平均气体温度。

模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### Two-Phase Fluid Heat Transfer Correlation

如果该段为过冷液体，则传热导为

UAseg,L,2P=aL,2P(Reseg,L,2P)b2P(Prseg,L,2P)c2Pkseg,L,2PG2PN，

其中：

- *a*L,2P、*b*2P 和 *c*2P 是 Nusselt 数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Re*seg,L,2P 是该段的平均液体 Reynolds 数。
- *Pr*seg,L,2P 是该段的平均液体 Prandtl 数。
- *k*seg,L,2P 是该段的平均液体热导率。
- *G*2P 是热交换器两相流体侧的几何比例因子。模块计算该几何比例因子，以使所有段的总传热在标称工况下与指定性能匹配。

平均液体 Reynolds 数为

Reseg,L,2P=m˙seg,2PDref,2Pμseg,L,2PSref,2P，

其中：

- m˙seg,2P 是通过该段的质量流率。
- *μ*seg,L,2P 是该段的平均液体动力粘度。
- *D*ref,2P 是任意参考直径。
- *S*ref,2P 是任意参考流通面积。

**Note**

此方程中包含 *D*ref,2P 和 *S*ref,2P 项仅用于单位计算目的，以使 *Re*seg,L,2P 无量纲。*D*ref,2P 和 *S*ref,2P 的值是任意的，因为 *G*2P 的计算会覆盖这些值。

类似地，如果该段为过热蒸气，则传热导为

UAseg,V,2P=aV,2P(Reseg,V,2P)b2P(Prseg,V,2P)c2Pkseg,V,2PG2PN，

其中：

- *a*V,2P、*b*2P 和 *c*2P 是 Nusselt 数关联式的系数。这些系数作为模块参数出现在 **Correlation Coefficients** 部分中。
- *Re*seg,V,2P 是该段的平均蒸气 Reynolds 数。
- *Pr*seg,V,2P 是该段的平均蒸气 Prandtl 数。
- *k*seg,V,2P 是该段的平均蒸气热导率。

平均蒸气 Reynolds 数为

Reseg,V,2P=m˙seg,2PDref,2Pμseg,V,2PSref,2P，

其中 *μ*seg,V,2P 是该段的平均蒸气动力粘度。

如果该段为液-汽混合物，则传热导为

UAseg,M,2P=aM,2P(Reseg,SL,2P)b2PCZ(Prseg,SL,2P)c2Pkseg,SL,2PG2PN，

其中：

- *a*M,2P、*b*2P 和 *c*2P 是 Nusselt 数关联式的系数。这些系数作为模块参数出现在 **Correlation Coefficients** 部分中。
- *Re*seg,SL,2P 是该段的饱和液体 Reynolds 数。
- *Pr*seg,SL,2P 是该段的饱和液体 Prandtl 数。
- *k*seg,SL,2P 是该段的饱和液体热导率。
- *CZ* 是 Cavallini 和 Zecchin 项。

饱和液体 Reynolds 数为

Reseg,SL,2P=m˙seg,2PDref,2Pμseg,SL,2PSref,2P，

其中 *μ*seg,SL,2P 是该段的饱和液体动力粘度。

Cavallini 和 Zecchin 项为

CZ=((νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P+1))1+b2P−((νseg,SV,2Pνseg,SL,2P−1)(xseg,in,2P+1))1+b2P(1+b2P)(νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P−xseg,in,2P)，

其中：

- *ν*seg,SL,2P 是该段的饱和液体比体积。
- *ν*seg,SV,2P 是该段的饱和蒸气比体积。
- *x*seg,in,2P 是该段入口处的蒸气干度。
- *x*seg,out,2P 是该段出口处的蒸气干度。

该表达式基于 Cavallini 和 Zecchin [5] 的工作，其中推导了局部蒸气干度 *x* 下的传热系数关联式。液-汽混合物的方程是通过在从 *x*seg,in,2P 到 *x*seg,out,2P 的段上对 Cavallini 和 Zecchin 关联式取平均得到的。

### Two-Phase Fluid Weighted Average

通过某段的两相流体流可能无法完全表示为过冷液体、过热蒸气或液-汽混合物中的任一种。相反，每个段可能由这些的组合构成。模块通过基于该段比焓变化以及饱和液体和蒸气比焓计算权重因子（*w*L、*w*V 和 *w*M）来近似此情况。模块假设该段的比焓从入口到出口呈分段线性变化，其断点对应于液体和蒸气的饱和边界。传热系数较大的区域比传热系数较低的区域具有更陡的斜率。

wL=ΔLΔL+ΔM+ΔVwV=ΔVΔL+ΔM+ΔVwM=1−wL−wV

ΔL=|min(hseg,out,2P,hseg,SL,2P)−min(hseg,in,2P,hseg,SL,2P)|⋅UAseg,M,2P⋅UAseg,V,2PΔM=|min(max(hseg,out,2P,hseg,SL,2P),hseg,SV,2P)−min(max(hseg,in,2P,hseg,SL,2P),hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,V,2PΔV=|max(hseg,out,2P,hseg,SV,2P)−max(hseg,in,2P,hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,M,2P

其中：

- *h*seg,in,2P 是该段入口处的比焓。
- *h*seg,out,2P 是该段出口处的比焓。
- *h*seg,SL,2P 是该段的饱和液体比焓。
- *h*seg,SV,2P 是该段的饱和蒸气比焓。

因此，该段的加权平均两相流体传热导为

UAseg,2P=wL(UAseg,L,2P)+wV(UAseg,V,2P)+wM(UAseg,M,2P)。

该段的加权平均流体温度为

Tseg,2P=wL(UAseg,L,2P)Tseg,L,2P+wV(UAseg,V,2P)Tseg,V,2P+wM(UAseg,M,2P)Tseg,M,2PUAseg,2P，

其中：

- *T*seg,L,2P 是该段的平均液体温度。
- *T*seg,V,2P 是该段的平均蒸气温度。
- *T*seg,M,2P 是该段的平均混合物温度，即饱和液体温度。

### Gas Heat Transfer Correlation

传热导为

UAseg,G=aG(Reseg,G)bG(Prseg,G)cGkseg,GGGN，

其中：

- *a*G、*b*G 和 *c*G 是 Nusselt 数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Re*seg,G 是该段的平均 Reynolds 数。
- *Pr*seg,G 是该段的平均 Prandtl 数。
- *k*seg,G 是该段的平均热导率。
- *G*G 是热交换器气体侧的几何比例因子。模块计算该几何比例因子，以使所有段的总传热在标称工况下与指定性能匹配。

平均 Reynolds 数为

Reseg,G=m˙seg,GDref,Gμseg,Sref,G，

其中：

- *ṁseg,G* 是通过该段的质量流率。
- *μ*seg,G 是该段的平均动力粘度。
- *D*ref,G 是任意参考直径。
- *S*ref,G 是任意参考流通面积。

**Note**

此方程中包含 *D*ref,G 和 *S*ref,G 项仅用于单位计算目的，以使 *Re*seg,G 无量纲。*D*ref,G 和 *S*ref,G 的值是任意的，因为 *G*G 的计算会覆盖这些值。

### Pressure Loss

两相流体侧的压降为

pA,2P−p2P=K2P2m˙A,2Pm˙2A,2P+m˙2thres,2P2ρavg,2PpB,2P−p2P=K2P2m˙B,2Pm˙2B,2P+m˙2thres,2P2ρavg,2P

其中：

- *p*A,2P 和 *p*B,2P 分别是端口 **A1** 和 **B1** 处的压力。
- *p*2P 是计算传热时的内部两相流体压力。
- m˙A,2P 和 m˙B,2P 分别是流入端口 **A1** 和 **B1** 的质量流率。
- *ρ*avg,2P 是所有段上的平均两相流体密度。
- m˙thres,2P 是压降的层流阈值，近似为标称质量流率的 1e-4。模块计算压降系数 *K*2P，以使 *p*A,2P – *p*B,2P 在标称质量流率下与标称压降匹配。

气体侧的压降为

pA,G−pG=KG2m˙A,Gm˙2A,G+m˙2thres,G2ρavg,GpB,G−pG=KG2m˙B,Gm˙2B,G+m˙2thres,G2ρavg,G

其中：

- *p*A,G 和 *p*B,G 分别是端口 **A2** 和 **B2** 处的压力。
- *p*G 是计算传热时的内部气体压力。
- *ṁA,G* 和 *ṁB,G* 分别是流入端口 **A2** 和 **B2** 的质量流率。
- *ρ*avg,G 是所有段上的平均气体密度。
- *ṁthres,G* 是压降的层流阈值，近似为标称质量流率的 1e-4。模块计算压降系数 *K*G，以使 *p*A,G – *p*B,G 在标称质量流率下与标称压降匹配。

### Two-Phase Fluid Mass and Energy Conservation

整体两相流体流的质量守恒方程为

(dp2Pdt∑segments(∂ρseg,2P∂p)+∑segments(duseg,2Pdt∂ρseg,2P∂u))V2PN=m˙A,2P+m˙B,2P，

其中：

- ∂ρseg,2P∂p 是该段密度对压力的偏导数。
- ∂ρseg,2P∂u 是该段密度对比内能的偏导数。
- *u*seg,2P 是该段的比内能。
- *V*2P 是两相流体总体积。

求和针对所有段。

**Note**

尽管模块为传热计算将两相流体流分为 *N*=3 个段，但它假设所有段处于相同的内部压力 *p*2P。因此，*p*2P 位于求和之外。

每个段的能量守恒方程为

duseg,2PdtM2PN+useg,2P(m˙seg,in,2P−m˙seg,out,2P)=Φseg,in,2P−Φseg,out,2P+Qseg,2P，

其中：

- *M*2P 是两相流体总质量。
- m˙seg,in,2P 和 m˙seg,out,2P 是流入和流出该段的质量流率。
- *Φ*seg,in,2p 和 *Φ*seg,out,2p 是流入和流出该段的能量流率。

模块假设各段之间的质量流率在 m˙A,2P 和 m˙B,2P 的值之间线性分布。

### Gas Mass and Energy Conservation

整体气体流的质量守恒为

(dpGdt∑segments(∂ρseg,G∂p)+∑segments(dTseg,Gdt∂ρseg,G∂T))VGN=m˙A,G+m˙B,G，

其中：

- ∂ρseg,G∂p 是该段密度对压力的偏导数。
- ∂ρseg,G∂T 是该段密度对温度的偏导数。
- *T*seg,G 是该段的温度。
- *V*G 是气体总体积。

求和针对所有段。

**Note**

尽管模块为传热计算将气体流分为 *N*=3 个段，但它假设所有段处于相同的内部压力 *pG*。因此，*pG* 位于求和之外。

每个段的能量守恒方程为

(dpGdt∂useg,G∂p+dTseg,Gdt∂useg,G∂T)MGN+useg,G(m˙seg,in,G−m˙seg,out,G)=Φseg,in,G−Φseg,out,G+Qseg,G，

其中：

- ∂useg,G∂p 是该段比内能对压力的偏导数。
- ∂useg,G∂T 是该段比内能对温度的偏导数。
- *M*G 是气体总质量。
- m˙seg,in,G 和 m˙seg,out,G 是流入和流出该段的质量流率。
- *Φ*seg,in,G 和 *Φ*seg,out,G 是流入和流出该段的能量流率。

模块假设各段之间的质量流率在 *ṁA,G* 和 *ṁB,G* 的值之间线性分布。
