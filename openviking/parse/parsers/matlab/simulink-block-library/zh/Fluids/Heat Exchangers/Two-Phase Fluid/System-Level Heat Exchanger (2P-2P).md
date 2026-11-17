---
type: simulink-block
title: 'System-Level Heat Exchanger (2P-2P)'
family: 'hydro'
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
```yaml
ports:
- name: Q1
  summary: 传递给两相流体 1 的传热速率，W 物理信号
  direction: output
- name: Q2
  summary: 传递给两相流体 2 的传热速率，W 物理信号
  direction: output
- name: A1
  summary: 侧 1 的两相流体端口 两相流体
  direction: conserving
- name: B1
  summary: 侧 1 的两相流体端口 两相流体
  direction: conserving
- name: A2
  summary: 侧 2 的两相流体端口 两相流体
  direction: conserving
- name: B2
  summary: 侧 2 的两相流体端口 两相流体
  direction: conserving
```

### 输出

### **Q1** — 传递给两相流体 1 的传热速率，W 物理信号

传递给第一个两相流体网络的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。

### **Q2** — 传递给两相流体 2 的传热速率，W 物理信号

传递给第二个两相流体网络的传热速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。
### 守恒端口

### **A1** — 侧 1 的两相流体端口 两相流体

与第一个两相流体网络关联的入口或出口端口。

### **B1** — 侧 1 的两相流体端口 两相流体

与第一个两相流体网络关联的入口或出口端口。

### **A2** — 侧 2 的两相流体端口 两相流体

与第二个两相流体网络关联的入口或出口端口。

### **B2** — 侧 2 的两相流体端口 两相流体

与第二个两相流体网络关联的入口或出口端口。
## 参数
```yaml
parameters:
- name: Flow arrangement at nominal operating conditions
  summary: 额定工况下的流路对齐方式 Counter flow - Two-Phase Fluid 1 flows from A to B, Two-Phase Fluid 2 flows from B to A（默认）| Parallel
    flow - Both fluids flow from A to B | Cross flow - Both fluids flow from A to B
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
  summary: 额定工况 Heat transfer from Two-Phase Fluid 1 to Two-Phase Fluid 2（默认）| Heat transfer from Two-Phase Fluid 2 to Two-Phase
    Fluid 1
  group: 两相流体 1
- name: Nominal mass flow rate
  summary: 额定工况下两相流体 1 端口之间的质量流量 0.001 kg/s（默认）| 正标量
  group: 两相流体 1
- name: Nominal pressure drop
  summary: 额定工况下两相流体 1 端口之间的压降 0.01 MPa（默认）| 正标量
  group: 两相流体 1
- name: Pressure specification
  summary: 选择压力指定方法 Inlet pressure（默认）| Saturation pressure at specified condensing temperature | Saturation pressure at specified
    evaporating temperature
  group: 两相流体 1
- name: Nominal inlet pressure
  summary: 两相流体 1 入口处的压力 1 MPa（默认）| 正标量
  group: 两相流体 1
- name: Nominal saturation temperature
  summary: 使用额定饱和温度指定压力 313.15 K（默认）| 正标量
  group: 两相流体 1
- name: Inlet condition specification
  summary: 选择描述两相流体 1 入口条件的量 Specific enthalpy（默认）| Temperature | Vapor quality
  group: 两相流体 1
- name: Nominal inlet specific enthalpy
  summary: 两相流体 1 入口处的比焓 440 kJ/kg（默认）| 正标量
  group: 两相流体 1
- name: Nominal inlet temperature
  summary: 两相流体 1 入口处的温度 313.15 K（默认）| 正标量
  group: 两相流体 1
- name: Nominal inlet vapor quality
  summary: 两相流体 1 入口处的蒸汽干度 1（默认）| 正标量
  group: 两相流体 1
- name: Heat transfer capacity specification
  summary: 如何指定两相流体 1 的传热能力 Rate of heat transfer（默认）| Outlet condition
  group: 两相流体 1
- name: Nominal rate of heat transfer
  summary: 传热速率 0.1 kW（默认）| 正标量
  group: 两相流体 1
- name: Outlet condition specification
  summary: 选择出口条件指定的量 Specific enthalpy（默认）| Subcooling | Superheating | Vapor quality
  group: 两相流体 1
- name: Nominal outlet specific enthalpy
  summary: 两相流体 1 出口处的比焓 250 kJ/kg（默认）| 正标量 | 二元素向量
  group: 两相流体 1
- name: Nominal subcooling
  summary: 两相流体 1 出口处低于液体饱和温度的温度差 5 deltaK（默认）| 正标量
  group: 两相流体 1
- name: Nominal superheating
  summary: 两相流体 1 出口处高于蒸汽饱和温度的温度差 5 deltaK（默认）| 正标量
  group: 两相流体 1
- name: Nominal outlet vapor quality
  summary: 两相流体 1 出口处的蒸汽质量分数 0（默认）| [0,1] 范围内的标量
  group: 两相流体 1
- name: Two-phase fluid 1 volume
  summary: 两相流体 1 的总体积 0.001 m^3（默认）| 正标量
  group: 两相流体 1
- name: Initialize two-phase fluid 1 to nominal operating conditions
  summary: 两相流体 1 初始化选项 on（默认）| off
  group: 两相流体 1
- name: Initial fluid energy specification
  summary: 两相流体 1 的初始状态 Specific enthalpy（默认）| Temperature | Vapor quality | Vapor void fraction | Specific internal energy
  group: 两相流体 1
- name: Initial two-phase fluid 1 pressure
  summary: 仿真开始时的流体 1 压力 0.101325 MPa（默认）| 正标量
  group: 两相流体 1
- name: Initial two-phase fluid 1 specific enthalpy
  summary: 仿真开始时的单位质量焓 1500 kJ/kg（默认）| 正标量 | 二元素向量
  group: 两相流体 1
- name: Initial two-phase fluid 1 temperature
  summary: 仿真开始时的温度 293.15 K（默认）| 正标量 | 二元素向量
  group: 两相流体 1
- name: Initial two-phase fluid 1 vapor quality
  summary: 仿真开始时的蒸汽质量分数 0.5（默认）| [0,1] 范围内的标量 | 二元素向量
  group: 两相流体 1
- name: Initial two-phase fluid 1 vapor void fraction
  summary: 仿真开始时的蒸汽体积分数 0.5（默认）| [0,1] 范围内的标量 | 二元素向量
  group: 两相流体 1
- name: Initial two-phase fluid 1 specific internal energy
  summary: 仿真开始时的单位质量内能 1500 kJ/kg（默认）| 正标量 | 二元素向量
  group: 两相流体 1
- name: Nominal mass flow rate
  summary: 标称工况下两相流体 2 端口之间的质量流量 0.001 kg/s（默认）| 正标量
  group: Two-Phase Fluid 2
- name: Nominal pressure drop
  summary: 标称工况下两相流体 2 端口之间的压降 0.01 MPa（默认）| 正标量
  group: Two-Phase Fluid 2
- name: Pressure specification
  summary: 选择压力指定方法 Inlet pressure（默认）| Saturation pressure at specified condensing temperature | Saturation pressure at specified
    evaporating temperature
  group: Two-Phase Fluid 2
- name: Nominal inlet pressure
  summary: 两相流体侧入口处的压力 1 MPa（默认）| 正标量
  group: Two-Phase Fluid 2
- name: Nominal saturation temperature
  summary: 使用标称饱和温度指定压力 243.15 K（默认）| 正标量
  group: Two-Phase Fluid 2
- name: Inlet condition specification
  summary: 选择用于描述两相流体 2 入口条件的量 Specific enthalpy（默认）| Temperature | Vapor quality
  group: Two-Phase Fluid 2
- name: Nominal inlet specific enthalpy
  summary: 两相流体 2 入口处的比焓 250 kJ/kg（默认）| 正标量
  group: Two-Phase Fluid 2
- name: Nominal inlet temperature
  summary: 两相流体 2 入口处的温度 237.15 K（默认）| 正标量
  group: Two-Phase Fluid 2
- name: Nominal inlet vapor quality
  summary: 两相流体 2 入口处的蒸汽干度 0.1（默认）| 正标量
  group: Two-Phase Fluid 2
- name: Two-phase fluid 2 volume
  summary: 两相流体 2 的总体积 0.001 m^3（默认）| 正标量
  group: Two-Phase Fluid 2
- name: Initialize two-phase fluid 2 to nominal operating conditions
  summary: 用于初始化两相流体 2 的选项 on（默认）| off
  group: Two-Phase Fluid 2
- name: Initial fluid energy specification
  summary: 两相流体 2 的初始状态 Specific enthalpy（默认）| Temperature | Vapor quality | Vapor void fraction | Specific internal energy
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 pressure
  summary: 仿真开始时的流体 2 压力 0.101325 MPa（默认）| 正标量
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 specific enthalpy
  summary: 仿真开始时的单位质量焓 1500 kJ/kg（默认）| 正标量 | 二元素向量
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 temperature
  summary: 仿真开始时的温度 293.15 K（默认）| 正标量 | 二元素向量
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 vapor quality
  summary: 仿真开始时的蒸汽质量分数 0.5（默认）| [0,1] 范围内的标量 | 二元素向量
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 vapor void fraction
  summary: 仿真开始时的蒸汽体积分数 0.5（默认）| [0,1] 范围内的标量 | 二元素向量
  group: Two-Phase Fluid 2
- name: Initial two-phase fluid 2 specific internal energy
  summary: 仿真开始时的单位质量内能 1500 kJ/kg（默认）| 正标量 | 二元素向量
  group: Two-Phase Fluid 2
- name: 两相流体 1 液体中 Nu = a\*Re^b\*Pr^c 的 a
  summary: 两相流体 1 中过冷液体的关联式系数 0.023（默认）| 正标量
  group: Correlation Coefficients
- name: 两相流体 1 混合物中 Nu = a\*Re^b\*Pr^c 的 a
  summary: 两相流体 1 中液-汽混合物的关联式系数 0.005（默认）| 正标量
  group: Correlation Coefficients
- name: 两相流体 1 蒸汽中 Nu = a\*Re^b\*Pr^c 的 a
  summary: 两相流体 1 中过热蒸汽的关联式系数 0.023（默认）| 正标量
  group: Correlation Coefficients
- name: 两相流体 1 中 Nu = a\*Re^b\*Pr^c 的 b
  summary: 两相流体 1 关联式中的雷诺数指数 0.8（默认）| 正标量
  group: Correlation Coefficients
- name: 两相流体 1 中 Nu = a\*Re^b\*Pr^c 的 c
  summary: 两相流体 1 关联式中的普朗特数指数 0.33（默认）| 正标量
  group: Correlation Coefficients
- name: 两相流体 2 液体中 Nu = a\*Re^b\*Pr^c 的 a
  summary: 两相流体 2 中过冷液体的关联式系数 0.023（默认）| 正标量
  group: Correlation Coefficients
- name: 两相流体 2 混合物中 Nu = a\*Re^b\*Pr^c 的 a
  summary: 两相流体 2 中液-汽混合物的关联式系数 0.005（默认）| 正标量
  group: Correlation Coefficients
- name: 两相流体 2 蒸汽中 Nu = a\*Re^b\*Pr^c 的 a
  summary: 两相流体 2 中过热蒸汽的关联式系数 0.023（默认）| 正标量
  group: Correlation Coefficients
- name: 两相流体 2 中 Nu = a\*Re^b\*Pr^c 的 b
  summary: 两相流体 2 关联式中的雷诺数指数 0.8（默认）| 正标量
  group: Correlation Coefficients
- name: 两相流体 2 中 Nu = a\*Re^b\*Pr^c 的 c
  summary: 两相流体 2 关联式中的普朗特数指数 0.33（默认）| 正标量
  group: Correlation Coefficients
```

### 配置

### **Flow arrangement at nominal operating conditions** — 额定工况下的流路对齐方式 `Counter flow - Two-Phase Fluid 1 flows from A to B, Two-Phase Fluid 2 flows from B to A`（默认）| `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

额定工况下换热器两侧之间的流路对齐方式。可用的流动布置方式有：

- `Counter flow - Two-Phase Fluid 1 flows from A to B, Two-Phase
  Fluid 2 flows from B to A` — 两股流体平行流动，方向相反。
- `Parallel flow - Both fluids flow from A to B` —
  两股流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to B` — 两股流体
  相互垂直流动。

平行流和逆流之间的选择会影响模块确定换热器尺寸的方式。逆流设置最为有效，满足指定性能所需的尺寸最小。相反，平行流效果最差，满足指定性能所需的尺寸最大。

额定工况下的流动方向（从 A 到 B，或从 B 到 A）仅在您选择 **Initialize two-phase fluid 1 to nominal operating conditions** 或 **Initialize two-phase fluid 2 to nominal operating conditions** 时影响模型初始化。如果您设置了不同的初始工况，流动方向可以不同。

在模块确定换热器尺寸之后，此设置不再影响模块在仿真期间计算传热的方式。相反，传热取决于仿真期间的流动方向。例如，如果您将参数设置为平行流，但将模型设置为以逆流方式运行，则即使其余边界条件相同，仿真期间的传热速率也不会与指定性能匹配。

如果您将参数设置为交叉流，则模块将换热器内部的流路建模为相互垂直，因此仿真期间的流动方向无关紧要。

### **Enable wall thermal mass** — 是否启用热质量对传热表面的影响 `off`（默认）| `on`

是否启用热质量对传热表面的影响。当您选择此参数时，模块会引入额外的动态特性，需要更长时间才能达到稳态，但此参数不影响稳态仿真结果。

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

将壁面温度初始化为额定工况或指定值的选项。如果您选择此参数，模块将根据两侧流体指定的额定工况计算初始壁面温度。如果您清除此参数，则可以使用 **Initial wall temperature** 参数直接指定初始壁面温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Initial wall temperature** — 壁面的初始温度 `293.15 K`（默认）| 正标量或二元素向量

壁面的初始温度。如果您指定标量，模块假定初始壁面温度是均匀的。如果您指定二元素向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 之间以及端口 **B1** 和 **B2** 之间线性变化。第一个元素对应端口 **A1** 和 **A2** 处的温度，第二个元素对应端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

两相流体 1 端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

两相流体 1 端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

两相流体 2 端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

两相流体 2 端口 **B2** 处的流通面积。

### 两相流体 1

### **Nominal operating condition** — 额定工况 `Heat transfer from Two-Phase Fluid 1 to Two-Phase Fluid 2`（默认）| `Heat transfer from Two-Phase Fluid 2 to Two-Phase Fluid 1`

额定工况：

- `Heat transfer from Two-Phase Fluid 1 to Two-Phase Fluid
  2` — 侧 1 被冷却，侧 2 被加热。
- `Heat transfer from Two-Phase Fluid 2 to Two-Phase Fluid
  1` — 侧 2 被冷却，侧 1 被加热。

此设置仅与额定工况参数相关。它并不意味着在仿真期间传热只能沿指定方向发生。

### **Nominal mass flow rate** — 额定工况下两相流体 1 端口之间的质量流量 `0.001 kg/s`（默认）| 正标量

额定工况下从端口 **A1** 到端口 **B1** 的质量流量。

### **Nominal pressure drop** — 额定工况下两相流体 1 端口之间的压降 `0.01 MPa`（默认）| 正标量

额定工况下从端口 **A1** 到端口 **B1** 的压降。

### **Pressure specification** — 选择压力指定方法 `Inlet pressure`（默认）| `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

选择压力指定方法：

- `Inlet pressure` — 指定额定入口压力。
- `Saturation pressure at specified saturation
  temperature` — 指定额定饱和温度。

### **Nominal inlet pressure** — 两相流体 1 入口处的压力 `1 MPa`（默认）| 正标量

额定工况下换热器两相流体 1 入口处的压力。

#### 依赖关系

要启用此参数，请将 **Pressure specification** 设置为 `Inlet pressure`。

### **Nominal saturation temperature** — 使用额定饱和温度指定压力 `313.15 K`（默认）| 正标量

额定工况下换热器两相流体 1 出口处的饱和温度。换热器中的压力为对应的饱和压力。额定饱和温度必须低于临界温度。

#### 依赖关系

要启用此参数，请将 **Pressure specification** 设置为 `Saturation pressure at specified saturation temperature`。

### **Inlet condition specification** — 选择描述两相流体 1 入口条件的量 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality`

用于描述额定工况下流体入口条件的量：温度、比焓或蒸汽干度。

### **Nominal inlet specific enthalpy** — 两相流体 1 入口处的比焓 `440 kJ/kg`（默认）| 正标量

额定工况下换热器两相流体 1 入口处的比焓。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet temperature** — 两相流体 1 入口处的温度 `313.15 K`（默认）| 正标量

额定工况下换热器两相流体 1 入口处的温度。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification** 设置为 `Temperature`。

### **Nominal inlet vapor quality** — 两相流体 1 入口处的蒸汽干度 `1`（默认）| 正标量

额定工况下换热器两相流体 1 入口处的蒸汽干度，定义为液-汽混合物中蒸汽的质量分数。

#### 依赖关系

要启用此参数，请将 **Inlet condition specification** 设置为 `Vapor quality`。

### **Heat transfer capacity specification** — 如何指定两相流体 1 的传热能力 `Rate of heat transfer`（默认）| `Outlet condition`

是直接通过传热速率指定额定工况下两相流体 1 的换热器性能，还是通过出口条件间接指定。

### **Nominal rate of heat transfer** — 传热速率 `0.1 kW`（默认）| 正标量

传热速率。**Nominal Operating condition** 参数决定热量从哪个网络传递到哪个网络：

- 如果 **Nominal operating condition** 为 `Heat
  transfer from two-phase fluid 1 to two-phase fluid 2`，此参数
  为额定工况下从两相流体侧 1 传递到侧 2 的传热速率。
- 如果 **Nominal operating condition** 为 `Heat
  transfer from two-phase fluid 2 to two-phase fluid 1`，此参数
  为额定工况下从两相流体侧 2 传递到侧 1 的传热速率。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Rate of heat transfer`。

### **Outlet condition specification** — 选择出口条件指定的量 `Specific enthalpy`（默认）| `Subcooling` | `Superheating` | `Vapor quality`

选择出口条件指定的量：

- `Specific enthalpy` — 指定额定比焓。
- `Subcooling` — 指定额定过冷度。如果您将 **Nominal operating condition** 设置为 `Heat transfer from two-phase fluid 1 to two-phase fluid 2`，则此选项可用。
- `Superheating` — 指定额定过热度。如果您将 **Nominal operating condition** 设置为 `Heat transfer from two-phase fluid 2 to two-phase fluid 1`，则此选项可用。
- `Vapor quality` — 指定额定蒸汽干度。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Outlet condition`。

### **Nominal outlet specific enthalpy** — 两相流体 1 出口处的比焓 `250 kJ/kg`（默认）| 正标量 | 二元素向量

额定工况下换热器两相流体 1 出口处的比焓。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal subcooling** — 两相流体 1 出口处低于液体饱和温度的温度差 `5 deltaK`（默认）| 正标量

额定工况下换热器两相流体 1 出口处低于液体饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Subcooling`。

### **Nominal superheating** — 两相流体 1 出口处高于蒸汽饱和温度的温度差 `5 deltaK`（默认）| 正标量

额定工况下换热器两相流体 1 出口处高于蒸汽饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Superheating`。

### **Nominal outlet vapor quality** — 两相流体 1 出口处的蒸汽质量分数 `0`（默认）| [0,1] 范围内的标量

额定工况下换热器两相流体 1 出口处的两相流体蒸汽干度，定义为液-汽混合物中蒸汽的质量分数。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请将 **Outlet condition specification** 设置为 `Vapor quality`。

### **Two-phase fluid 1 volume** — 两相流体 1 的总体积 `0.001 m^3`（默认）| 正标量

换热器内两相流体 1 的总体积。

### **Initialize two-phase fluid 1 to nominal operating conditions** — 两相流体 1 初始化选项 `on`（默认）| `off`

将两相流体初始化为额定工况或指定值的选项。如果您选择此参数，模块将两相流体初始化为额定工况。如果您清除此复选框，则可以使用附加参数直接指定初始条件。

### **Initial fluid energy specification** — 两相流体 1 的初始状态 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

用于描述侧 1 流体初始状态的量：温度、蒸汽干度、蒸汽空隙率、比焓或比内能。

**Initial fluid energy specification** 参数的值限制了两相流体可用的初始状态。当 **Initial fluid energy specification** 为：

- `Temperature` — 指定初始状态为过冷液体或过热蒸汽。不能指定液-汽混合物，因为在液-汽混合物区域内温度是恒定的。
- `Vapor quality` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液体质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液体质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。该模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。该模块不限制初始状态。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 1 to nominal operating conditions** 复选框。

### **Initial two-phase fluid 1 pressure** — 仿真开始时的流体 1 压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的两相流体 1 压力。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 1 to nominal operating conditions** 复选框。

### **Initial two-phase fluid 1 specific enthalpy** — 仿真开始时的单位质量焓 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时的两相流体 1 比焓。如果该值为标量，则假定初始比焓均匀。如果该值为二元素向量，则假定初始比焓在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 1 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。

### **Initial two-phase fluid 1 temperature** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时的两相流体 1 温度。如果该值为标量，则假定初始温度均匀。如果该值为二元素向量，则假定初始温度在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 1 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Temperature`。

### **Initial two-phase fluid 1 vapor quality** — 仿真开始时的蒸汽质量分数 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时的两相流体 1 蒸汽干度，定义为液-汽混合物中蒸汽的质量分数。如果该值为标量，则假定初始蒸汽干度均匀。如果该值为二元素向量，则假定初始蒸汽干度在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 1 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor quality`。

### **Initial two-phase fluid 1 vapor void fraction** — 仿真开始时的蒸汽体积分数 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时的两相流体 1 蒸汽空隙率，定义为液-汽混合物中蒸汽的体积分数。如果该值为标量，则假定初始蒸汽空隙率均匀。如果该值为二元素向量，则假定初始蒸汽空隙率在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 1 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor void fraction`。

### **Initial two-phase fluid 1 specific internal energy** — 仿真开始时的单位质量内能 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时的两相流体 1 比内能。如果该值为标量，则假定初始比内能均匀。如果该值为二元素向量，则假定初始比内能在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 1 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific internal energy`。

### Two-Phase Fluid 2

### **Nominal mass flow rate** — 标称工况下两相流体 2 端口之间的质量流量 `0.001 kg/s`（默认）| 正标量

标称工况下从端口 **A2** 到端口 **B2** 的质量流量。

### **Nominal pressure drop** — 标称工况下两相流体 2 端口之间的压降 `0.01 MPa`（默认）| 正标量

标称工况下从端口 **A2** 到端口 **B2** 的压降。

### **Pressure specification** — 选择压力指定方法 `Inlet pressure`（默认）| `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

选择压力指定方法：

- `Inlet pressure` — 指定标称入口压力。
- `Saturation pressure at specified saturation temperature` — 指定标称饱和温度。

### **Nominal inlet pressure** — 两相流体侧入口处的压力 `1 MPa`（默认）| 正标量

标称工况下换热器两相流体 2 入口处的压力。

#### 依赖

要启用此参数，请将 **Pressure specification** 设置为 `Inlet pressure`。

### **Nominal saturation temperature** — 使用标称饱和温度指定压力 `243.15 K`（默认）| 正标量

标称工况下换热器两相流体 2 出口处的饱和温度。换热器中的压力为相应的饱和压力。标称饱和温度必须低于临界温度。

#### 依赖

要启用此参数，请将 **Pressure specification** 设置为 `Saturation pressure at specified saturation temperature`。

### **Inlet condition specification** — 选择用于描述两相流体 2 入口条件的量 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality`

用于描述标称工况下流体入口条件的量：温度、比焓或蒸汽干度。

### **Nominal inlet specific enthalpy** — 两相流体 2 入口处的比焓 `250 kJ/kg`（默认）| 正标量

标称工况下换热器两相流体 2 入口处的比焓。

#### 依赖

要启用此参数，请将 **Inlet condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet temperature** — 两相流体 2 入口处的温度 `237.15 K`（默认）| 正标量

标称工况下换热器两相流体 2 入口处的温度。

#### 依赖

要启用此参数，请将 **Inlet condition specification** 设置为 `Temperature`。

### **Nominal inlet vapor quality** — 两相流体 2 入口处的蒸汽干度 `0.1`（默认）| 正标量

标称工况下换热器两相流体 2 入口处的蒸汽干度，定义为液-汽混合物中蒸汽的质量分数。

#### 依赖

要启用此参数，请将 **Inlet condition specification** 设置为 `Vapor quality`。

### **Two-phase fluid 2 volume** — 两相流体 2 的总体积 `0.001 m^3`（默认）| 正标量

换热器内两相流体 2 的总体积。

### **Initialize two-phase fluid 2 to nominal operating conditions** — 用于初始化两相流体 2 的选项 `on`（默认）| `off`

用于将两相流体初始化为标称工况或指定值的选项。如果选择此参数，该模块将两相流体初始化为标称工况。如果清除此复选框，则可以使用附加参数直接指定初始条件。

### **Initial fluid energy specification** — 两相流体 2 的初始状态 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

用于描述侧 2 流体初始状态的量。

**Initial fluid energy specification** 参数的值限制了两相流体可用的初始状态。当 **Initial fluid energy specification** 为：

- `Temperature` — 指定初始状态为过冷液体或过热蒸汽。不能指定液-汽混合物，因为在液-汽混合物区域内温度是恒定的。
- `Vapor quality` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液体质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定初始状态为液-汽混合物。不能指定过冷液体或过热蒸汽，因为在整个区域内液体质量分数分别为 0 和 1。此外，该模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。该模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。该模块不限制初始状态。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 2 to nominal operating conditions** 复选框。

### **Initial two-phase fluid 2 pressure** — 仿真开始时的流体 2 压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的两相流体 2 压力。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 2 to nominal operating conditions** 复选框。

### **Initial two-phase fluid 2 specific enthalpy** — 仿真开始时的单位质量焓 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时的两相流体 2 比焓。如果该值为标量，则假定初始比焓均匀。如果该值为二元素向量，则假定初始比焓在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 2 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。

### **Initial two-phase fluid 2 temperature** — 仿真开始时的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时的两相流体 2 温度。如果该值为标量，则假定初始温度均匀。如果该值为二元素向量，则假定初始温度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 2 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Temperature`。

### **Initial two-phase fluid 2 vapor quality** — 仿真开始时的蒸汽质量分数 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时的两相流体 2 蒸汽干度，定义为液-汽混合物中蒸汽的质量分数。如果该值为标量，则假定初始蒸汽干度均匀。如果该值为二元素向量，则假定初始蒸汽干度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 2 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor quality`。

### **Initial two-phase fluid 2 vapor void fraction** — 仿真开始时的蒸汽体积分数 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时的两相流体 2 蒸汽空隙率，定义为液-汽混合物中蒸汽的体积分数。如果该值为标量，则假定初始蒸汽空隙率均匀。如果该值为二元素向量，则假定初始蒸汽空隙率在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 2 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor void fraction`。

### **Initial two-phase fluid 2 specific internal energy** — 仿真开始时的单位质量内能 `1500 kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时的两相流体 2 比内能。如果该值为标量，则假定初始比内能均匀。如果该值为二元素向量，则假定初始比内能在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖

要启用此参数，请清除 **Initialize two-phase fluid 2 to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific internal energy`。

### Correlation Coefficients

### **两相流体 1 液体中 Nu = a\*Re^b\*Pr^c 的 a** — 两相流体 1 中过冷液体的关联式系数 `0.023`（默认）| 正标量

两相流体 1 中过冷液体的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **两相流体 1 混合物中 Nu = a\*Re^b\*Pr^c 的 a** — 两相流体 1 中液-汽混合物的关联式系数 `0.005`（默认）| 正标量

两相流体 1 中液-汽混合物的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Cavallini 和 Zecchin 关联式。

### **两相流体 1 蒸汽中 Nu = a\*Re^b\*Pr^c 的 a** — 两相流体 1 中过热蒸汽的关联式系数 `0.023`（默认）| 正标量

两相流体 1 中过热蒸汽的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **两相流体 1 中 Nu = a\*Re^b\*Pr^c 的 b** — 两相流体 1 关联式中的雷诺数指数 `0.8`（默认）| 正标量

两相流体 1 的努塞尔数作为雷诺数和普朗特数函数的关联式中的雷诺数指数。相同的值适用于过冷液体、液-汽混合物和过热蒸汽。

### **两相流体 1 中 Nu = a\*Re^b\*Pr^c 的 c** — 两相流体 1 关联式中的普朗特数指数 `0.33`（默认）| 正标量

两相流体 1 的努塞尔数作为雷诺数和普朗特数函数的关联式中的普朗特数指数。相同的值适用于过冷液体、液-汽混合物和过热蒸汽。

### **两相流体 2 液体中 Nu = a\*Re^b\*Pr^c 的 a** — 两相流体 2 中过冷液体的关联式系数 `0.023`（默认）| 正标量

两相流体 2 中过冷液体的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **两相流体 2 混合物中 Nu = a\*Re^b\*Pr^c 的 a** — 两相流体 2 中液-汽混合物的关联式系数 `0.005`（默认）| 正标量

两相流体 2 中液-汽混合物的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Cavallini 和 Zecchin 关联式。

### **两相流体 2 蒸汽中 Nu = a\*Re^b\*Pr^c 的 a** — 两相流体 2 中过热蒸汽的关联式系数 `0.023`（默认）| 正标量

两相流体 2 中过热蒸汽的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **两相流体 2 中 Nu = a\*Re^b\*Pr^c 的 b** — 两相流体 2 关联式中的雷诺数指数 `0.8`（默认）| 正标量

两相流体 2 的努塞尔数作为雷诺数和普朗特数函数的关联式中的雷诺数指数。相同的值适用于过冷液体、液-汽混合物和过热蒸汽。

### **两相流体 2 中 Nu = a\*Re^b\*Pr^c 的 c** — 两相流体 2 关联式中的普朗特数指数 `0.33`（默认）| 正标量

两相流体 2 的努塞尔数作为雷诺数和普朗特数函数的关联式中的普朗特数指数。相同的值适用于过冷液体、液-汽混合物和过热蒸汽。
## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2023b：指定初始壁温

如果选择 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框，则可以使用新的 **Initial wall temperature** 参数直接指定初始条件。

## 描述

基于两个两相流体网络之间性能数据的换热器

System-Level Heat Exchanger (2P-2P) 模块对两个不同的两相流体网络之间的换热器进行建模。每个网络都有自己的一组流体属性。

该模块使用换热器数据表中的性能数据，而不是换热器的详细几何结构。换热器的任一侧或两侧都可以因热交换而冷凝或蒸发流体。您也可以将此模块用作制冷系统中的内部换热器。内部换热器通过在冷凝器出口和蒸发器出口之间提供额外的热交换来提高制冷系统的效率。

您通过额定工况来参数化该模块。换热器 sized 以在稳态下匹配额定工况下的指定性能。

换热器的每一侧根据沿流动路径的焓变来近似液体区、混合物区和蒸汽区。

### 传热

该模块将两相流体 1 流和两相流体 2 流各分为三个大小相等的段，并计算每个段中流体之间的传热。为简单起见，本节中的方程针对一个段。

如果清除 **Enable wall thermal mass** 复选框，则换热器中的热平衡为

Qseg,2P1+Qseg,2P2=0，

其中：

- *Q*seg,2P1 是从作为传热表面的壁面到该段中两相流体 1 的热流率。
- *Q*seg,2P2 是从壁面到该段中两相流体 2 的热流率。

如果选择 **Enable wall thermal mass**，则换热器中的热平衡为

Qseg,2P1+Qseg,2P2=−MwallcpwallNdTseg,walldt，

其中：

- *M*wall 是壁面的质量。
- *c*pwall 是壁面的比热。
- *N* = 3 是段数。
- *T*seg,wall 是该段中的平均壁温。
- *t* 是时间。

从壁面到该段中两相流体 1 的热流率为

Qseg,2P1=UAseg,2P1(Tseg,wall−Tseg,2P1)，

其中：

- *UAseg,2P1* 是该段中两相流体 1 的加权平均传热导。
- *Tseg,2P1* 是该段中两相流体 1 的加权平均流体温度。

从壁面到该段中两相流体 2 的热流率为

Qseg,2P2=UAseg,2P2(Tseg,wall−Tseg,2P2)，

其中：

- *UAseg,2P2* 是该段中两相流体 2 的加权平均传热导。
- *Tseg,2P2* 是该段中两相流体 2 的加权平均流体温度。

模块在传热计算中使用的流体属性是入口值与流体体积中值的平均值。

### 两相流体 1 传热关联式

该模块使用相同的表达式计算两种两相流体中的传热导。

如果该段是过冷液体，则传热导为

UAseg,L,2P1=aL,2P1(Reseg,L,2P1)b2P1(Prseg,L,2P1)c2P1kseg,L,2P1G2P1N，

其中：

- *a*L,2P1、*b*2P1 和 *c*2P1 是努塞尔数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Re*seg,L,2P1 是该段的平均液体雷诺数。
- *Pr*seg,L,2P1 是该段的平均液体普朗特数。
- *k*seg,L,2P1 是该段的平均液体热导率。
- *G*2P1 是换热器两相流体 1 侧的几何比例因子。模块计算几何比例因子，使得所有段的总传热量在额定工况下与指定性能匹配。

平均液体雷诺数为

Reseg,L,2P1=m˙seg,2P1Dref,2P1μseg,L,2P1Sref,2P1，

其中：

- m˙seg,2P1 是通过该段的质量流量。
- *μ*seg,L,2P1 是该段的平均液体动力粘度。
- *D*ref,2P1 是任意参考直径。
- *S*ref,2P1 是任意参考流通面积。

**注意**

*D*ref,2P1 和 *S*ref,2P1 项仅出于单位计算目的包含在此方程中，以使 *Re*seg,L,2P1 无量纲。*D*ref,2P1 和 *S*ref,2P1 的值是任意的，因为 *G*2P1 的计算会覆盖这些值。

类似地，如果该段是过热蒸汽，则传热导为

UAseg,V,2P1=aV,2P1(Reseg,V,2P1)b2P1(Prseg,V,2P1)c2P1kseg,V,2P1G2P1N，

其中：

- *a*V,2P1、*b*2P1 和 *c*2P1 是努塞尔数关联式的系数。这些系数在 **Correlation Coefficients** 部分中显示为模块参数。
- *Re*seg,V,2P1 是该段的平均蒸汽雷诺数。
- *Pr*seg,V,2P1 是该段的平均蒸汽普朗特数。
- *k*seg,V,2P1 是该段的平均蒸汽热导率。

平均蒸汽雷诺数为

Reseg,V,2P1=m˙seg,2P1Dref,2P1μseg,V,2P1Sref,2P1，

其中 *μ*seg,V,2P1 是该段的平均蒸汽动力粘度。

如果该段是液-汽混合物，则传热导为

UAseg,M,2P1=aM,2P1(Reseg,SL,2P1)b2P1CZ(Prseg,SL,2P1)c2P1kseg,SL,2P1G2P1N，

其中：

- *a*M,2P1、*b*2P1 和 *c*2P1 是努塞尔数关联式的系数。这些系数在 **Correlation Coefficients** 部分中显示为模块参数。
- *Re*seg,SL,2P1 是该段的饱和液体雷诺数。
- *Pr*seg,SL,2P1 是该段的饱和液体普朗特数。
- *k*seg,SL,2P1 是该段的饱和液体热导率。
- *CZ* 是 Cavallini 和 Zecchin 项。

饱和液体雷诺数为

Reseg,SL,2P1=m˙seg,2P1Dref,2P1μseg,SL,2P1Sref,2P1，

其中 *μ*seg,SL,2P1 是该段的饱和液体动力粘度。

Cavallini 和 Zecchin 项为

CZ=((νseg,SV,2P1νseg,SL,2P1−1)(xseg,out,2P1+1))1+b2P1−((νseg,SV,2P1νseg,SL,2P1−1)(xseg,in,2P1+1))1+b2P1(1+b2P1)(νseg,SV,2P1νseg,SL,2P1−1)(xseg,out,2P1−xseg,in,2P1)，

其中：

- *ν*seg,SL,2P1 是该段的饱和液体比容。
- *ν*seg,SV,2P1 是该段的饱和蒸汽比容。
- *x*seg,in,2P1 是该段入口处的蒸汽干度。
- *x*seg,out,2P1 是该段出口处的蒸汽干度。

该表达式基于 Cavallini 和 Zecchin [5] 的工作，其推导了局部蒸汽干度 *x* 处的传热系数关联式。液-汽混合物的方程是通过在从 *x*seg,in,2P1 到 *x*seg,out,2P1 的段上对 Cavallini 和 Zecchin 关联式取平均得到的。

### 两相流体 1 加权平均

通过一个段的两相流体流动可能不完全表现为过冷液体、过热蒸汽或液-汽混合物中的任何一种。相反，每个段可能由这些的组合组成。模块通过基于该段上的比焓变化以及饱和液体和蒸汽比焓计算加权因子（*w*L、*w*V 和 *w*M）来近似这种情况。模块假设该段上的比焓从入口到出口呈分段线性变化，其断点对应于液体和蒸汽的饱和边界。传热系数较大的区域比传热系数较低的区域具有更陡的斜率。

wL=ΔLΔL+ΔM+ΔVwV=ΔVΔL+ΔM+ΔVwM=1−wL−wV

ΔL=|min(hseg,out,2P1,hseg,SL,2P1)−min(hseg,in,2P1,hseg,SL,2P1)|⋅UAseg,M,2P1⋅UAseg,V,2P1ΔM=|min(max(hseg,out,2P1,hseg,SL,2P1),hseg,SV,2P1)−min(max(hseg,in,2P1,hseg,SL,2P1),hseg,SV,2P1)|⋅UAseg,L,2P1⋅UAseg,V,2P1ΔV=|max(hseg,out,2P1,hseg,SV,2P1)−max(hseg,in,2P1,hseg,SV,2P1)|⋅UAseg,L,2P1⋅UAseg,M,2P1

其中：

- *h*seg,in,2P1 是该段入口处的比焓。
- *h*seg,out,2P1 是该段出口处的比焓。
- *h*seg,SL,2P1 是该段的饱和液体比焓。
- *h*seg,SV,2P1 是该段的饱和蒸汽比焓。

因此，该段的加权平均两相流体 1 传热导为

UAseg,2P1=wL(UAseg,L,2P1)+wV(UAseg,V,2P1)+wM(UAseg,M,2P1)。

该段的加权平均流体 1 温度为

Tseg,2P1=wL(UAseg,L,2P1)Tseg,L,2P1+wV(UAseg,V,2P1)Tseg,V,2P1+wM(UAseg,M,2P1)Tseg,M,2P1UAseg,2P1，

其中：

- *T*seg,L,2P1 是该段的平均液体温度。
- *T*seg,V,2P1 是该段的平均蒸汽温度。
- *T*seg,M,2P1 是该段的平均混合物温度，即饱和液体温度。

### Two-Phase Fluid 2 Heat Transfer Correlation

如果分段为过冷液体，则传热导为

UAseg,L,2P2=aL,2P2(Reseg,L,2P2)b2P2(Prseg,L,2P2)c2P2kseg,L,2P2G2P2N,

其中：

- *a*L,2P2、
  *b*L,2P2 和
  *c*L,2P2 是 Nusselt
  数关联式的系数。这些系数是 **Correlation
  Coefficients** 部分中的模块参数。
- *Re*seg,L,2P2 是该分段的平均液体 Reynolds
  数。
- *Pr*seg,L,2P2 是该分段的平均液体 Prandtl
  数。
- *k*seg,L,2P2 是该分段的平均液体热导率。
- *G*2P2 是热交换器两相流体 2 侧的几何比例因子。模块会计算几何比例
  因子，以使所有分段上的总传热量与标称工况下指定的性能相匹配。

平均液体 Reynolds 数为

Reseg,L,2P2=m˙seg,2P2Dref,2P2μseg,L,2P2Sref,2P2,

其中：

- m˙seg,2P2 是通过该分段的质量流量。
- *μ*seg,L,2P2 是该分段的平均液体动力
  黏度。
- *D*ref,2P2 是任意参考
  直径。
- *S*ref,2P2 是任意参考流通
  面积。

**注意**

此方程中包含 *D*ref,2P2 和
*S*ref,2P2 项仅用于单位计算目的，以使
*Re*seg,L,2P2 无量纲。*D*ref,2P 和
*S*ref,2P2 的值是任意的，因为
*G*2P2 的计算会覆盖这些值。

类似地，如果分段为过热蒸气，则传热导为

UAseg,V,2P2=aV,2P2(Reseg,V,2P2)b2P2(Prseg,V,2P2)c2P2kseg,V,2P2G2P2N,

其中：

- *a*V,2P2、
  *b*V,2P2 和
  *c*V,2P2 是 Nusselt
  数关联式的系数。这些系数在
  **Correlation Coefficients** 部分中显示为模块参数。
- *Re*seg,V,2P2 是该分段的平均蒸气 Reynolds
  数。
- *Pr*seg,V,2P2 是该分段的平均蒸气 Prandtl
  数。
- *k*seg,V,2P2 是该分段的平均蒸气热导率。

平均蒸气 Reynolds 数为

Reseg,V,2P2=m˙seg,2P2Dref,2P2μseg,V,2P2Sref,2P2,

其中 *μ*seg,V,2P2 是该分段的平均蒸气动力
黏度。

如果分段为液-汽混合物，则传热导为

UAseg,M,2P2=aM,2P2(Reseg,SL,2P2)b2P2CZ(Prseg,SL,2P2)c2P2kseg,SL,2P2G2P2N,

其中：

- *a*M,2P2、
  *b*L,2P2 和
  *c*L,2P2 是 Nusselt
  数关联式的系数。这些系数在
  **Correlation Coefficients** 部分中显示为模块参数。
- *Re*seg,SL,2P2 是该分段的饱和液体
  Reynolds 数。
- *Pr*seg,SL,2P2 是该分段的饱和液体
  Prandtl 数。
- *k*seg,SL,2P2 是该分段的饱和液体
  热导率。
- *CZ* 是 Cavallini 和 Zecchin 项。

饱和液体 Reynolds 数为

Reseg,SL,2P2=m˙seg,2P2Dref,2P2μseg,SL,2P2Sref,2P2,

其中 *μ*seg,SL,2P2 是该分段的饱和液体
动力黏度。

Cavallini 和 Zecchin 项为

CZ=((νseg,SV,2P2νseg,SL,2P2−1)(xseg,out,2P2+1))1+b2P2−((νseg,SV,2P2νseg,SL,2P2−1)(xseg,in,2P2+1))1+b2P2(1+b2P2)(νseg,SV,2P2νseg,SL,2P2−1)(xseg,out,2P2−xseg,in,2P2),

其中：

- *ν*seg,SL,2P2 是该分段的饱和液体
  比体积。
- *ν*seg,SV,2P2 是该分段的饱和蒸气
  比体积。
- *x*seg,in,2P2 是该分段入口处的
  蒸气干度。
- *x*seg,out,2P2 是该分段出口处的
  蒸气干度。

该表达式基于 Cavallini 和 Zecchin [5] 的工作，其中推导了局部蒸气干度
*x* 下的传热系数关联式。液-汽混合物的方程是通过在从
*x*seg,in,2P2 到
*x*seg,out,2P2 的分段上对
Cavallini 和 Zecchin 关联式取平均得到的。

### Two-Phase Fluid 2 Weighted Average

通过分段的两相流体流动可能无法完全表示为过冷液体、过热蒸气或液-汽混合物中的
任一种。相反，每个分段可能由这些状态的组合组成。模块通过基于分段上的比焓变化
以及饱和液体和蒸气比焓来计算权重因子（*w*L、
*w*V 和
*w*M），从而近似此条件。模块假设分段上的比焓从入口到
出口呈分段线性变化，其断点对应于液体和蒸气的饱和边界。传热系数较大的区域比
传热系数较低的区域具有更陡的斜率。

wL=ΔLΔL+ΔM+ΔVwV=ΔVΔL+ΔM+ΔVwM=1−wL−wV

ΔL=|min(hseg,out,2P2,hseg,SL,2P2)−min(hseg,in,2P2,hseg,SL,2P2)|⋅UAseg,M,2P2⋅UAseg,V,2P2ΔM=|min(max(hseg,out,2P2,hseg,SL,2P2),hseg,SV,2P2)−min(max(hseg,in,2P2,hseg,SL,2P2),hseg,SV,2P2)|⋅UAseg,L,2P2⋅UAseg,V,2P2ΔV=|max(hseg,out,2P2,hseg,SV,2P2)−max(hseg,in,2P2,hseg,SV,2P2)|⋅UAseg,L,2P2⋅UAseg,M,2P2

其中：

- *h*seg,in,2P2 是该分段入口处的
  比焓。
- *h*seg,out,2P2 是该分段出口处的
  比焓。
- *h*seg,SL,2P2 是该分段的饱和液体
  比焓。
- *h*seg,SV,2P2 是该分段的饱和蒸气
  比焓。

因此，该分段的加权平均两相流体 2 传热导为

UAseg,2P2=wL(UAseg,L,2P2)+wV(UAseg,V,2P2)+wM(UAseg,M,2P2).

该分段的加权平均流体 2 温度为

Tseg,2P2=wL(UAseg,L,2P2)Tseg,L,2P2+wV(UAseg,V,2P2)Tseg,V,2P2+wM(UAseg,M,2P2)Tseg,M,2P2UAseg,2P2,

其中：

- *T*seg,L,2P2 是该分段的平均液体
  温度。
- *T*seg,V,2P2 是该分段的平均蒸气
  温度。
- *T*seg,M,2P2 是该分段的平均混合物
  温度，即饱和液体温度。

### Pressure Loss

两相流体 1 侧的压降为

pA,2P1−p2P1=K2P12m˙A,2P1m˙2A,2P1+m˙2thres,2P12ρavg,2P1pB,2P1−p2P1=K2P12m˙B,2P1m˙2B,2P1+m˙2thres,2P12ρavg,2P1

其中：

- *p*A,2P1 和
  *p*B,2P1 分别是端口
  **A1** 和 **B1** 处的压力。
- *p*2P1 是用于计算传热的内部两相流体 1
  压力。
- m˙A,2P1 和 m˙B,2P1 分别是流入端口 **A1** 和
  **B1** 的质量流量。
- *ρ*avg,2P1 是所有分段上的平均两相流体 1
  密度。
- m˙thres,2P1 是压降的层流阈值，近似为标称质量流量的 1e-4。
  模块会计算压降系数
  *K*2P1，以使
  *p*A,2P1 –
  *p*B,2P1 与标称质量流量下的
  标称压降相匹配。

两相流体 2 侧的压降为

pA,2P2−p2P2=K2P22m˙A,2P2m˙2A,2P2+m˙2thres,2P22ρavg,2P2pB,2P2−p2P2=K2P22m˙B,2P2m˙2B,2P2+m˙2thres,2P22ρavg,2P2

其中：

- *p*A,2P2 和
  *p*B,2P2 分别是端口
  **A2** 和 **B2** 处的压力。
- *p*2P2 是用于计算传热的内部两相流体 2
  压力。
- m˙A,2P2 和 m˙B,2P2 分别是流入端口 **A2** 和
  **B2** 的质量流量。
- *ρ*avg,2P2 是所有分段上的平均两相流体 2
  密度。
- m˙thres,2P2 是压降的层流阈值，近似为标称质量流量的 1e-4。
  模块会计算压降系数
  *K*2P2，以使
  *p*A,2P2 –
  *p*B,2P2 与标称质量流量下的
  标称压降相匹配。

### Two-Phase Fluid 1 Mass and Energy Conservation

整体两相流体 1 流动的质量守恒方程为

(dp2P1dt∑segments(∂ρseg,2P1∂p)+∑segments(duseg,2P1dt∂ρseg,2P1∂u))V2P1N=m˙A,2P1+m˙B,2P1,

其中：

- ∂ρseg,2P1∂p 是该分段的密度对压力的偏导数。
- ∂ρseg,2P1∂u 是该分段的密度对比内能的偏导数。
- *u*seg,2P1 是该分段的比内能。
- *V*2P1 是两相流体 1 的总
  体积。

求和针对所有分段。

**注意**

尽管模块将两相流体 1 流动划分为 *N*=3
个分段以进行传热计算，但它假设所有分段都处于相同的内部
压力 *p*2P1。因此，
*p*2P1 位于求和之外。

每个分段的能量守恒方程为

duseg,2P1dtM2P1N+useg,2P1(m˙seg,in,2P1−m˙seg,out,2P1)=Φseg,in,2P1−Φseg,out,2P1+Qseg,2P1,

其中：

- *M*2P1 是两相流体 1 的总
  质量。
- m˙seg,in,2P1 和 m˙seg,out,2P1 是流入和流出该分段的质量流量。
- *Φ*seg,in,2p1 和
  *Φ*seg,out,2p1 是流入和流出该分段的
  能量流量。

模块假设各分段之间的质量流量在
m˙A,2P1 和 m˙B,2P1 的值之间线性分布。

### Two-Phase Fluid 2 Mass and Energy Conservation

整体两相流体 2 流动的质量守恒方程为

(dp2P2dt∑segments(∂ρseg,2P2∂p)+∑segments(duseg,2P2dt∂ρseg,2P2∂u))V2P2N=m˙A,2P2+m˙B,2P2,

其中：

- ∂ρseg,2P2∂p 是该分段的密度对压力的偏导数。
- ∂ρseg,2P2∂u 是该分段的密度对比内能的偏导数。
- *u*seg,2P2 是该分段的比内能。
- *V*2P2 是两相流体 2 的总
  体积。

求和针对所有分段。

**注意**

尽管模块将两相流体 2 流动划分为 *N*=3
个分段以进行传热计算，但它假设所有分段都处于相同的内部
压力 *p*2P2。因此，
*p*2P2 位于求和之外。

每个分段的能量守恒方程为

duseg,2P2dtM2P2N+useg,2P2(m˙seg,in,2P2−m˙seg,out,2P2)=Φseg,in,2P2−Φseg,out,2P2+Qseg,2P2,

其中：

- *M*2P2 是两相流体 2 的总
  质量。
- m˙seg,in,2P2 和 m˙seg,out,2P2 是流入和流出该分段的质量流量。
- *Φ*seg,in,2p2 和
  *Φ*seg,out,2p2 是流入和流出该分段的
  能量流量。

模块假设各分段之间的质量流量在
m˙A,2P2 和 m˙B,2P2 的值之间线性分布。
