---
type: simulink-block
title: 'System-Level Heat Exchanger (TL-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Moist Air'
documentation_page: 'systemlevelheatexchangertlma'
documentation_source_path: 'ref/systemlevelheatexchangertlma.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Heat Exchanger (TL-MA)

## 端口
```yaml
ports:
- name: Q1
  summary: 传递至热液的热流率，W 物理信号
  direction: output
- name: Q2
  summary: 传递至湿空气的热流率，W 物理信号
  direction: output
- name: W
  summary: 湿空气冷凝率，kg/s 物理信号
  direction: output
- name: A1
  summary: 热液端口 热液
  direction: output
- name: B1
  summary: 热液端口 热液
  direction: output
- name: A2
  summary: 湿空气端口 湿空气
  direction: output
- name: B2
  summary: 湿空气端口 湿空气
  direction: output
```

### 输出

### **Q1** — 传递至热液的热流率，W 物理信号

传递至热液的热流率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。

### **Q2** — 传递至湿空气的热流率，W 物理信号

传递至湿空气的热流率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。

### **W** — 湿空气冷凝率，kg/s 物理信号

离开湿空气流的水冷凝率，以物理信号形式返回。该端口的值不包括以水滴形式夹带的冷凝部分。冷凝液不会积聚在传热表面上。
### 守恒

### **A1** — 热液端口 热液

与热液相关的入口或出口端口。

### **B1** — 热液端口 热液

与热液相关的入口或出口端口。

### **A2** — 湿空气端口 湿空气

与湿空气相关的入口或出口端口。

### **B2** — 湿空气端口 湿空气

与湿空气相关的入口或出口端口。
## 参数
```yaml
parameters:
- name: Flow arrangement at nominal operating conditions
  summary: 流路对齐方式 Counter flow - Thermal Liquid 1 flows from A to B, Moist Air 2 flows from B to A（默认）| Parallel flow - Both
    fluids flow from A to B | Cross flow - Both fluids flow from A to B
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
  summary: 初始化壁面温度的选项 on（默认）| off
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
  summary: 标称工况 Heat transfer from Thermal Liquid 1 to Moist Air 2（默认）| Heat transfer from Moist Air 2 to Thermal Liquid 1
  group: Thermal Liquid 1
- name: Nominal mass flow rate
  summary: 标称工况下热液端口之间的质量流量 0.1 kg/s（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal pressure drop
  summary: 标称工况下热液端口之间的压降 0.01 MPa（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal inlet pressure
  summary: 热液入口处的压力 0.101325 MPa（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal inlet temperature
  summary: 热液体入口处的温度 333.15 K（默认）| 正标量
  group: Thermal Liquid 1
- name: Heat transfer capacity specification
  summary: 如何指定热液体的换热能力 Rate of heat transfer（默认）| Outlet condition
  group: Thermal Liquid 1
- name: Nominal rate of heat transfer
  summary: 换热速率 1 kW（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal outlet temperature
  summary: 出口温度 323.15 K（默认）| 正标量
  group: Thermal Liquid 1
- name: Thermal liquid volume
  summary: 热液体总体积 0.001 m^3（默认）| 正标量
  group: Thermal Liquid 1
- name: Initialize thermal liquid to nominal operating conditions
  summary: 初始化热液体的选项 on（默认）| off
  group: Thermal Liquid 1
- name: Initial thermal liquid pressure
  summary: 仿真开始时的热液体压力 0.101325 MPa（默认）| 正标量
  group: Thermal Liquid 1
- name: Initial thermal liquid temperature
  summary: 仿真开始时的热液体温度 293.15 K（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal mass flow rate
  summary: 额定工况下湿空气端口之间的质量流量 0.1 kg/s（默认）| 正标量
  group: Moist Air 2
- name: Nominal pressure drop
  summary: 额定工况下湿空气端口之间的压降 0.001 MPa（默认）| 正标量
  group: Moist Air 2
- name: Nominal inlet pressure
  summary: 湿空气侧入口处的压力 0.101325 MPa（默认）| 正标量
  group: Moist Air 2
- name: Nominal inlet temperature
  summary: 湿空气侧入口处的温度 293.15 K（默认）| 正标量
  group: Moist Air 2
- name: Inlet humidity specification
  summary: 用于描述湿空气侧入口湿度水平的量 Relative humidity（默认）| Specific humidity | Mole fraction | Humidity ratio | Wet-bulb temperature
  group: Moist Air 2
- name: Nominal inlet relative humidity
  summary: 入口处的相对湿度 0.5（默认）| 范围 [0,1] 内的标量
  group: Moist Air 2
- name: Nominal inlet specific humidity
  summary: 入口处的比湿 0.01（默认）| 范围 [0,1] 内的标量
  group: Moist Air 2
- name: Nominal inlet water vapor mole fraction
  summary: 入口处水蒸气的摩尔分数 0.01（默认）| 范围 [0,1] 内的标量
  group: Moist Air 2
- name: Nominal inlet humidity ratio
  summary: 入口处的湿度比 0.01（默认）| 范围 [0,1] 内的正标量
  group: Moist Air 2
- name: Nominal inlet wet-bulb temperature
  summary: 仿真开始时的湿球温度 287 K（默认）| 范围 [0,1] 内的正标量
  group: Moist Air 2
- name: Inlet trace gas specification
  summary: 用于描述入口微量气体水平的量 Mass fraction（默认）| Mole fraction
  group: Moist Air 2
- name: Nominal inlet trace gas mass fraction
  summary: 入口处微量气体的质量分数 0.001（默认）| 范围 [0,1] 内的标量
  group: Moist Air 2
- name: Nominal inlet trace gas mole fraction
  summary: 入口处微量气体的摩尔分数 0.001（默认）| 范围 [0,1] 内的标量
  group: Moist Air 2
- name: Moist air volume
  summary: 换热器中湿空气的总体积 0.1 m^3（默认）| 正标量
  group: Moist Air 2
- name: Initialize moist air to nominal operating conditions
  summary: 初始化湿空气的选项 on（默认）| off
  group: Moist Air 2
- name: 初始湿空气压力
  summary: 仿真开始时的湿空气压力 0.101325 MPa（默认）| 正标量
  group: Moist Air 2
- name: 初始湿空气温度
  summary: 仿真开始时的湿空气温度 293.15 K（默认）| 正标量 | 二元素向量
  group: Moist Air 2
- name: 初始湿度设定
  summary: 用于描述初始湿度水平的量 Relative humidity（默认）| Specific humidity | Mole fraction | Humidity ratio | Wet-bulb temperature
  group: Moist Air 2
- name: 初始湿空气相对湿度
  summary: 仿真开始时的相对湿度 0.5（默认）| 范围 [0,1] 内的标量 | 二元素向量
  group: Moist Air 2
- name: 初始湿空气比湿度
  summary: 仿真开始时的比湿度 0.01（默认）| 范围 [0,1] 内的标量 | 二元素向量
  group: Moist Air 2
- name: 初始湿空气水蒸气摩尔分数
  summary: 仿真开始时的水蒸气摩尔分数 0.01（默认）| 范围 [0,1] 内的标量 | 二元素向量
  group: Moist Air 2
- name: 初始湿空气湿度比
  summary: 仿真开始时的湿度比 0.01（默认）| 范围 [0,1] 内的正标量 | 二元素向量
  group: Moist Air 2
- name: 初始湿空气湿球温度
  summary: 仿真开始时的湿球温度 287 K（默认）| 范围 [0,1] 内的正标量
  group: Moist Air 2
- name: 初始微量气体设定
  summary: 用于描述初始微量气体水平的量 Mass fraction（默认）| Mole fraction
  group: Moist Air 2
- name: 初始湿空气微量气体质量分数
  summary: 仿真开始时的微量气体质量分数 0.001（默认）| 范围 [0,1] 内的标量 | 二元素向量
  group: Moist Air 2
- name: 初始湿空气微量气体摩尔分数
  summary: 仿真开始时的微量气体摩尔分数 0.001（默认）| 范围 [0,1] 内的标量 | 二元素向量
  group: Moist Air 2
- name: 水滴与湿空气的初始质量比
  summary: 水滴与湿空气的比值 0（默认）| 正标量
  group: Moist Air 2
- name: Relative humidity at saturation
  summary: 冷凝相对湿度 1（默认）| 非负标量
  group: Moist Air 2
- name: Water vapor condensation time constant
  summary: 冷凝时间尺度 1e-3 s（默认）| 正标量
  group: Moist Air 2
- name: Water droplets evaporation time constant
  summary: 蒸发时间尺度 1e-3 s（默认）| 正标量
  group: Moist Air 2
- name: Fraction of condensate entrained as water droplets
  summary: 水滴中冷凝物的比例 1（默认）| 范围 [0,1] 内的标量
  group: Moist Air 2
- name: a in Nu = a\*Re^b\*Pr^c for thermal liquid
  summary: 热液体相关系数 0.023（默认）| 正标量
  group: 相关系数
- name: b in Nu = a\*Re^b\*Pr^c for thermal liquid
  summary: 热液体关联式中的雷诺数指数 0.8（默认）| 正标量
  group: 相关系数
- name: c in Nu = a\*Re^b\*Pr^c for thermal liquid
  summary: 热液体关联式中的普朗特数指数 0.33（默认）| 正标量
  group: 相关系数
- name: a in Nu = a\*Re^b\*Pr^c for moist air
  summary: 湿空气相关系数 0.023（默认）| 正标量
  group: 相关系数
- name: b in Nu = a\*Re^b\*Pr^c for moist air
  summary: 湿空气关联式中的雷诺数指数 0.8（默认）| 正标量
  group: 相关系数
- name: c in Nu = a\*Re^b\*Pr^c for moist air
  summary: 湿空气关联式中的普朗特数指数 0.33（默认）| 正标量
  group: 相关系数
```

### 配置

### **Flow arrangement at nominal operating conditions** — 流路对齐方式 `Counter flow - Thermal Liquid 1 flows from A to B, Moist Air 2 flows from B to A`（默认）| `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

在标称工况下换热器两侧之间的流路对齐方式。可用的流动布置方式有：

- `Counter flow - Thermal Liquid 1 flows from A to B, Moist Air 2
  flows from B to A` — 两股流体彼此平行流动，方向相反。
- `Parallel flow - Both fluids flow from A to B` —
  两股流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to B` — 两股流体彼此垂直流动。

平行流和逆流之间的选择会影响模块确定换热器尺寸的方式。逆流设置最为有效，满足指定性能所需的尺寸最小。相反，平行流效果最差，满足指定性能所需的尺寸最大。

标称工况下的流动方向（从 A 到 B，或从 B 到 A）仅在您选择 **Initialize thermal liquid to
nominal operating conditions** 或 **Initialize moist air to nominal
operating conditions** 时影响模型初始化。如果您设置了不同的初始工况，流动方向可以不同。

在模块确定换热器尺寸之后，此设置不再影响模块在仿真期间计算传热的方式。相反，传热取决于仿真期间的流动方向。例如，如果您将参数设置为平行流，但将模型设置为以逆流运行，则即使其余边界条件相同，仿真期间的传热率也不会与指定性能匹配。

如果您将参数设置为交叉流，则模块将换热器内部的流路建模为相互垂直，因此仿真期间的流动方向无关紧要。

### **Enable wall thermal mass** — 是否启用热质量对传热表面的影响 `off`（默认）| `on`

是否启用热质量对传热表面的影响。当您选择此参数时，模块会为仿真引入额外的动态特性，并且需要更长时间才能达到稳态，但此参数不会影响稳态仿真结果。

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

将壁面温度初始化为标称工况或指定值的选项。如果您选择此参数，模块将根据为两侧流体指定的标称工况计算初始壁面温度。如果您清除此参数，则可以直接使用 **Initial wall temperature** 参数指定初始壁面温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal
mass**。

### **Initial wall temperature** — 壁面的初始温度 `293.15 K`（默认）| 正标量或二元素向量

壁面的初始温度。如果您指定标量，模块假定初始壁面温度是均匀的。如果您指定二元素向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 之间以及端口 **B1** 和 **B2** 之间线性变化。第一个元素对应端口 **A1** 和 **A2** 处的温度，第二个元素对应端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**
并清除 **Initialize wall temperature to nominal operating
conditions** 复选框。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

湿空气端口 **B2** 处的流通面积。

### Thermal Liquid 1

### **Nominal operating condition** — 标称工况 `Heat transfer from Thermal Liquid 1 to Moist Air 2`（默认）| `Heat transfer from Moist Air 2 to Thermal Liquid 1`

标称工况：

- `Heat transfer from Thermal Liquid 1 to Moist Air 2`
  — 热液被冷却，湿空气被加热。
- `Heat transfer from Moist Air 2 to Thermal Liquid 1`
  — 湿空气被冷却，热液被加热。

此设置仅与标称工况参数相关。这并不意味着在仿真期间热量只能沿指定方向传递。

### **Nominal mass flow rate** — 标称工况下热液端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1**
的质量流量。

### **Nominal pressure drop** — 标称工况下热液端口之间的压降 `0.01 MPa`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1**
的压降。

### **Nominal inlet pressure** — 热液入口处的压力 `0.101325 MPa`（默认）| 正标量

标称工况下换热器热液入口处的压力。

### **Nominal inlet temperature** — 热液体入口处的温度 `333.15 K`（默认）| 正标量

换热器在额定工况下热液体入口处的温度。

### **Heat transfer capacity specification** — 如何指定热液体的换热能力 `Rate of heat transfer`（默认）| `Outlet condition`

是直接通过换热速率，还是间接通过出口条件，来指定换热器在额定工况下热液体的性能。

### **Nominal rate of heat transfer** — 换热速率 `1 kW`（默认）| 正标量

换热速率。**Nominal Operating condition** 参数决定热量传递所涉及的网络：

- 如果 **Nominal operating condition** 为 `Heat
  transfer from Thermal Liquid 1 to Moist Air 2`，则该参数为额定工况下从热液体传递到湿空气的换热速率。
- 如果 **Nominal operating condition** 为 `Heat
  transfer from Moist Air 2 to Thermal Liquid 1`，则该参数为额定工况下从湿空气传递到热液体的换热速率。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity
specification** 设置为 `Rate of heat
transfer`。

### **Nominal outlet temperature** — 出口温度 `323.15 K`（默认）| 正标量

换热器热液体侧出口在额定工况下的温度。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity
specification** 设置为 `Outlet condition`。

### **Thermal liquid volume** — 热液体总体积 `0.001 m^3`（默认）| 正标量

换热器内热液体的总体积。

### **Initialize thermal liquid to nominal operating conditions** — 初始化热液体的选项 `on`（默认）| `off`

用于将热液体初始化为额定工况或指定值的选项。如果选中此参数，模块会将热液体初始化为额定工况。如果清除此复选框，则可以通过附加参数直接指定初始条件。

### **Initial thermal liquid pressure** — 仿真开始时的热液体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时热液体的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize thermal liquid to
nominal operating conditions** 复选框。

### **Initial thermal liquid temperature** — 仿真开始时的热液体温度 `293.15 K`（默认）| 正标量

仿真开始时热液体的温度。

#### 依赖关系

要启用此参数，请清除 **Initialize thermal liquid to
nominal operating conditions** 复选框。

### Moist Air 2

### **Nominal mass flow rate** — 额定工况下湿空气端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的质量流量。

### **Nominal pressure drop** — 额定工况下湿空气端口之间的压降 `0.001 MPa`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的压降。

### **Nominal inlet pressure** — 湿空气侧入口处的压力 `0.101325 MPa`（默认）| 正标量

额定工况下换热器湿空气入口处的压力。

### **Nominal inlet temperature** — 湿空气侧入口处的温度 `293.15 K`（默认）| 正标量

额定工况下换热器湿空气入口处的温度。

### **Inlet humidity specification** — 用于描述湿空气侧入口湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述额定工况下入口湿度水平的量。

### **Nominal inlet relative humidity** — 入口处的相对湿度 `0.5`（默认）| 范围 [0,1] 内的标量

额定工况下换热器湿空气入口处的相对湿度。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification**
设置为 `Relative humidity`。

### **Nominal inlet specific humidity** — 入口处的比湿 `0.01`（默认）| 范围 [0,1] 内的标量

额定工况下换热器湿空气入口处的比湿，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification**
设置为 `Specific humidity`。

### **Nominal inlet water vapor mole fraction** — 入口处水蒸气的摩尔分数 `0.01`（默认）| 范围 [0,1] 内的标量

额定工况下换热器湿空气入口处湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification**
设置为 `Mole fraction`。

### **Nominal inlet humidity ratio** — 入口处的湿度比 `0.01`（默认）| 范围 [0,1] 内的正标量

额定工况下换热器湿空气入口处的湿度比，定义为水蒸气与干空气及微量气体的质量比。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification**
设置为 `Humidity ratio`。

### **Nominal inlet wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| 范围 [0,1] 内的正标量

额定工况下换热器湿空气入口处的湿球温度。

#### 依赖关系

要启用此参数，请将 **Inlet humidity specification**
设置为 `Wet-bulb temperature`。

### **Inlet trace gas specification** — 用于描述入口微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述额定工况下入口微量气体水平的量：质量分数或摩尔分数。

### **Nominal inlet trace gas mass fraction** — 入口处微量气体的质量分数 `0.001`（默认）| 范围 [0,1] 内的标量

额定工况下换热器湿空气入口处湿空气混合物中微量气体的质量分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Inlet trace gas specification**
设置为 `Mass fraction`。

### **Nominal inlet trace gas mole fraction** — 入口处微量气体的摩尔分数 `0.001`（默认）| 范围 [0,1] 内的标量

额定工况下换热器湿空气入口处湿空气混合物中微量气体的摩尔分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请将 **Inlet trace gas specification**
设置为 `Mole fraction`。

### **Moist air volume** — 换热器中湿空气的总体积 `0.1 m^3`（默认）| 正标量

换热器中湿空气的总体积。

### **Initialize moist air to nominal operating conditions** — 初始化湿空气的选项 `on`（默认）| `off`

用于将湿空气初始化为额定工况或指定值的选项。如果选中此参数，模块会将湿空气初始化为额定工况。如果清除此复选框，则可以通过附加参数直接指定初始条件。

### **初始湿空气压力** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的湿空气压力。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **初始湿空气温度** — 仿真开始时的湿空气温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时的湿空气温度。如果该值为标量，则假定初始温度均匀。如果该值为二元素向量，则假定初始温度在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **初始湿度设定** — 用于描述初始湿度水平的量 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

选择用于描述初始湿度水平的量：相对湿度、比湿度、水蒸气摩尔分数或湿度比。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **初始湿空气相对湿度** — 仿真开始时的相对湿度 `0.5`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时的湿空气相对湿度。如果该值为标量，则假定初始相对湿度均匀。如果该值为二元素向量，则假定初始相对湿度在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Relative humidity`。

### **初始湿空气比湿度** — 仿真开始时的比湿度 `0.01`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时湿空气的比湿度，定义为湿空气混合物中水蒸气的质量分数。如果该值为标量，则假定初始比湿度均匀。如果该值为二元素向量，则假定初始比湿度在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Specific humidity`。

### **初始湿空气水蒸气摩尔分数** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时湿空气混合物中水蒸气的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀。如果该值为二元素向量，则假定初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Mole fraction`。

### **初始湿空气湿度比** — 仿真开始时的湿度比 `0.01`（默认）| 范围 [0,1] 内的正标量 | 二元素向量

仿真开始时湿空气的湿度比，定义为水蒸气与干空气和微量气体的质量比。如果该值为标量，则假定初始湿度比均匀。如果该值为二元素向量，则假定初始湿度比在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **初始湿空气湿球温度** — 仿真开始时的湿球温度 `287 K`（默认）| 范围 [0,1] 内的正标量

仿真开始时的湿球温度。该模块使用此值计算湿度。

此参数可以是标量或二元素向量。标量值表示通道中的平均初始湿球温度。向量值以 [`inlet`，`outlet`] 形式表示入口和出口处的初始湿球温度。该模块计算两个端口之间的线性梯度。入口和出口端口根据初始流动方向确定。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **初始微量气体设定** — 用于描述初始微量气体水平的量 `Mass fraction`（默认）| `Mole fraction`

选择用于描述仿真开始时微量气体水平的量：质量分数或摩尔分数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **初始湿空气微量气体质量分数** — 仿真开始时的微量气体质量分数 `0.001`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时湿空气混合物中微量气体的质量分数。如果该值为标量，则假定初始质量分数均匀。如果该值为二元素向量，则假定初始质量分数在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **初始湿空气微量气体摩尔分数** — 仿真开始时的微量气体摩尔分数 `0.001`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时湿空气混合物中微量气体的摩尔分数。如果该值为标量，则假定初始摩尔分数均匀。如果该值为二元素向量，则假定初始摩尔分数在端口 **A2** 和 **B2** 之间线性变化，其中第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数设置为 `None`，则忽略此参数。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **水滴与湿空气的初始质量比** — 水滴与湿空气的比值 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

#### 依赖关系

要启用此参数，请清除 **Initialize moist air to nominal operating conditions** 复选框。

### **Relative humidity at saturation** — 冷凝相对湿度 `1`（默认）| 非负标量

冷凝相对湿度。高于此值时发生冷凝。大多数情况下，该值为 1，即 100%。大于 1 的值表示过饱和蒸汽。

### **Water vapor condensation time constant** — 冷凝时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气通过冷凝多余水分回到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸汽的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 水滴中冷凝物的比例 `1`（默认）| 范围 [0,1] 内的标量

湿空气中以水滴形式夹带的冷凝物比例。

### 相关系数

### **a in Nu = a\*Re^b\*Pr^c for thermal liquid** — 热液体相关系数 `0.023`（默认）| 正标量

热液体努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for thermal liquid** — 热液体关联式中的雷诺数指数 `0.8`（默认）| 正标量

热液体努塞尔数作为雷诺数和普朗特数函数的关联式中的雷诺数指数。

### **c in Nu = a\*Re^b\*Pr^c for thermal liquid** — 热液体关联式中的普朗特数指数 `0.33`（默认）| 正标量

热液体努塞尔数作为雷诺数和普朗特数函数的关联式中的普朗特数指数。

### **a in Nu = a\*Re^b\*Pr^c for moist air** — 湿空气相关系数 `0.023`（默认）| 正标量

湿空气努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for moist air** — 湿空气关联式中的雷诺数指数 `0.8`（默认）| 正标量

湿空气努塞尔数作为雷诺数和普朗特数函数的关联式中的雷诺数指数。默认值基于 Colburn 方程。

### **c in Nu = a\*Re^b\*Pr^c for moist air** — 湿空气关联式中的普朗特数指数 `0.33`（默认）| 正标量

湿空气努塞尔数作为雷诺数和普朗特数函数的关联式中的普朗特数指数。默认值基于 Colburn 方程。
## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Moist Air

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024b：模拟悬浮在湿空气流中的水滴

湿空气域中的模块现在可以模拟悬浮在湿空气流中的水滴。要模拟水滴，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

### R2024a：新的湿度指定选项

该模块为 **Inlet humidity specification** 和 **Initial humidity specification** 参数提供了新选项。该选项称为 `Wet-bulb temperature`，允许您以湿球温度的形式输入数据。

### R2023b：指定初始壁温

如果您选择 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框，则可以使用新的 **Initial wall temperature** 参数直接指定初始条件。

## 描述

基于热液体与湿空气网络之间性能数据的换热器

System-Level Heat Exchanger (TL-MA) 模块基于热液体网络与湿空气网络之间的性能数据来模拟换热器。

该模块使用换热器数据表中的性能数据，而非换热器的详细几何结构。您可以在设计迭代期间调整换热器的尺寸和性能，或对具有不常见几何结构的换热器进行建模。您还可以在早期设计阶段使用此模块对具有一定性能水平的换热器进行建模，此时详细的几何数据尚不可用。

您通过额定工况对模块进行参数化。换热器经过尺寸设计，以在稳态额定工况下匹配指定的性能。

Moist Air 2 侧基于与换热表面的对流水蒸气质量传递来模拟水蒸气冷凝。冷凝水从湿空气流中移除。

此模块与 Heat Exchanger (TL-MA) 模块类似，但使用不同的参数化模型。下表比较了这两个模块：

| Heat Exchanger (TL-MA) | System-Level Heat Exchanger (TL-MA) |
| --- | --- |
| 模块参数基于换热器几何结构 | 模块参数基于性能和工况 |
| 换热器几何结构可能受可用几何参数选项的限制 | 模型独立于特定换热器几何结构 |
| 您可以通过调整几何参数（如翅片尺寸和管长）来调整模块以满足不同的性能要求 | 您可以通过直接指定所需的热流量和质量流量来调整模块以满足不同的性能要求 |
| 您可以在平行流、逆流或交叉流配置之间进行选择 | 您可以在额定工况下在平行流、逆流或交叉流布置之间进行选择，以帮助进行尺寸设计 |
| 在广泛工况范围内具有预测准确性，取决于 E-NTU 方程和传热系数关联式的适用性 | 在指定工况附近结果非常准确；远离指定工况时准确性可能降低 |
| 传热计算通过使用 E-NTU 模型考虑温度沿流动路径的变化 | 传热计算通过将流动路径分为三段来近似温度沿流动路径的变化 |
| 考虑湿空气流中的水蒸气冷凝和潜热 | 考虑湿空气流中的水蒸气冷凝和潜热 |

### Heat Transfer

该模块将湿空气流和热液体流各分为三段等长的段，并计算每段内流体之间的热传递。为简单起见，本节中的方程针对一个段。

如果清除 **Enable wall thermal mass** 复选框，则换热器中的热平衡为

Qseg,TL+Qseg,MA=0，

其中：

- *Q*seg,TL 是从壁面（即换热表面）到段内热液体的热流率。
- *Q*seg,MA 是从壁面到段内湿空气的热流率。

如果选中 **Enable wall thermal mass**，则换热器中的热平衡为

Qseg,TL+Qseg,MA=−MwallcpwallNdTseg,walldt，

其中：

- *M*wall 是壁面的质量。
- *c*pwall 是壁面的比热。
- *N* = 3 是段数。
- *T*seg,wall 是段内的平均壁面温度。
- *t* 是时间。

从壁面到段内热液体的热流率为

Qseg,TL=UAseg,TL(Tseg,wall−Tseg,TL)，

其中：

- *UA*seg,TL 是段内热液体的传热导。
- *T*seg,TL 是段内的平均液体温度。

从壁面到段内湿空气的热流率为

Qseg,MA=UAseg,MAc¯pseg,MA(h¯seg,wall−h¯seg,MA)+m˙w,seg,condhl,wall，

其中：

- *UA*seg,MA 是段内湿空气的传热导。
- c¯pseg,MA 是段内每单位质量干空气和微量气体的湿空气混合物比热。
- h¯seg,wall 是在平均壁面段温度下每单位质量干空气和微量气体的湿空气混合物焓。
- h¯seg,MA 是段内每单位质量干空气和微量气体的湿空气混合物焓。
- m˙w,seg,cond 是壁面上的水蒸气冷凝速率。
- *h*l,wall 是在平均壁面段温度下液态水的比焓。

在该方程中使用混合物焓同时考虑了温度差异和由于冷凝引起的湿度差异 [3]。

模块在传热计算中使用的流体属性是入口值与流体体积内值的平均值。

**注意**

对于湿空气量，符号上方的横线表示它们是混合物量除以仅干空气和微量气体的质量，而不是除以整个混合物的质量。整个混合物包括干空气、水蒸气和微量气体。

### Thermal Liquid Heat Transfer Correlation

传热导为

UAseg,TL=aTL(Reseg,TL)bTL(Prseg,TL)cTLkseg,TLGTLN，

其中：

- *a*TL、*b*TL 和 *c*TL 是 Nusselt 数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Re*seg,TL 是段内的平均 Reynolds 数。
- *Pr*seg,TL 是段内的平均 Prandtl 数。
- *k*seg,TL 是段内的平均热导率。
- *G*TL 是换热器热液体侧的几何比例因子。模块计算几何比例因子，使得所有段上的总传热量与标称工况下指定的性能相匹配。

平均 Reynolds 数为

Reseg,TL=m˙seg,TLDref,TLμseg,TLSref,TL，

其中：

- m˙seg,TL 是通过该段的质量流量。
- *μ*seg,TL 是段内的平均动力粘度。
- *D*ref,TL 是任意参考直径。
- *S*ref,TL 是任意参考流通面积。

**注意**

*D*ref,TL 和 *S*ref,TL 项包含在此方程中仅用于单位计算目的，以使 *Re*seg,TL 无量纲。*D*ref,TL 和 *S*ref,TL 的值是任意的，因为 *G*TL 的计算会覆盖这些值。

### Moist Air Heat Transfer Correlation

传热导为

UAseg,MA=aMA(Reseg,MA)bMA(Prseg,MA)cMAkseg,MAGMAN，

其中：

- *a*MA、*b*MA 和 *c*MA 是 Nusselt 数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Re*seg,MA 是段内的平均 Reynolds 数。
- *Pr*seg,MA 是段内的平均 Prandtl 数。
- *k*seg,MA 是段内的平均热导率。
- *G*MA 是换热器湿空气侧的几何比例因子。模块计算几何比例因子，使得所有段上的总传热量与标称工况下指定的性能相匹配。

平均 Reynolds 数为

Reseg,MA=m˙seg,MADref,MAμseg,MASref,MA，

其中：

- m˙seg,MA 是通过该段的质量流量。
- *μ*seg,MA 是段内的平均动力粘度。
- *D*ref,MA 是任意参考直径。
- *S*ref,MA 是任意参考流通面积。

**注意**

*D*ref,MA 和 *S*ref,MA 项包含在此方程中仅用于单位计算目的，以使 *Re*seg,MA 无量纲。*D*ref,MA 和 *S*ref,MA 的值是任意的，因为 *G*MA 的计算会覆盖这些值。

### Moist Air Condensation

描述从壁面到段内湿空气的热流率的方程（Heat Transfer 部分中的最后一个方程）使用平均湿空气混合物焓 h¯seg,MA 和壁面段湿空气混合物焓 h¯seg,wall。

平均湿空气混合物焓基于通过该段的湿空气流的温度和湿度：

h¯seg,MA=hseg,ag,MA+Wseg,MAhseg,w,MA，

其中：

- *h*seg,ag,MA 是段内干空气和微量气体的平均比焓。
- *h*seg,w,MA 是段内水蒸气的平均比焓。
- *W*seg,MA 是段内的湿度比。

壁面段湿空气混合物焓基于壁面段处的温度和湿度：

h¯seg,wall=hseg,ag,wall+Wseg,wallhseg,w,wall，

其中：

- *h*seg,ag,wall 是在壁面段温度下干空气和微量气体的比焓。
- *h*seg,w,wall 是在壁面段温度下水蒸气的比焓。
- *W*seg,wall 是壁面段处的湿度比：

  Wseg,wall=min(Wseg,MA,Wseg,s,wall)，

  其中 *W*seg,s,wall 是在壁面段温度下的饱和湿度比。换句话说，壁面处的湿度比与湿空气流的湿度比相同，但不超过在壁面段温度下所能支持的最大值。

当 *W*seg,s,wall < *W*seg,MA 时，壁面上发生水蒸气冷凝。水蒸气冷凝速率为

m˙w,seg,cond=UAseg,MAc¯pseg,MA(Wseg,MA−Wseg,wall)。

模块假设冷凝水从壁面排出，因此从下游湿空气流中移除。

### Pressure Loss

热液侧的压力损失为

pA,TL−pTL=KTL2m˙A,TLm˙2A,TL+m˙2thres,TL2ρavg,TLpB,TL−pTL=KTL2m˙B,TLm˙2B,TL+m˙2thres,TL2ρavg,TL

其中：

- *p*A,TL 和
  *p*B,TL 分别是端口
  **A2** 和 **B2** 处的压力。
- *p*TL 是用于计算传热的内部热液压力。
- m˙A,TL 和 m˙B,TL 分别是流入端口 **A2** 和
  **B2** 的质量流量。
- *ρ*avg,TL 是所有分段上的平均热液
  密度。
- m˙thres,TL 是压力损失的层流阈值，近似为
  额定质量流量的 1e-4。该模块计算压力损失系数
  *K*TL，使得
  *p*A,TL –
  *p*B,TL 在额定质量流量下与额定压力损失相匹配。

湿空气侧的压力损失为

pA,MA−pMA=KMA2m˙A,MAm˙2A,MA+m˙2thres,MA2ρavg,2PpB,MA−pMA=KMA2m˙B,MAm˙2B,MA+m˙2thres,MA2ρavg,MA

其中：

- *p*A,MA 和
  *p*B,MA 分别是端口
  **A2** 和 **B2** 处的压力。
- *p*MA 是用于计算传热的内部湿空气压力。
- m˙A,MA 和 m˙B,MA 分别是流入端口 **A2** 和
  **B2** 的质量流量。
- *ρ*avg,MA 是所有分段上的平均湿空气
  密度。
- m˙thres,MA 是压力损失的层流阈值，近似为
  额定质量流量的 1e-4。该模块计算压力损失系数
  *K*MA，使得
  *p*A,MA –
  *p*B,MA 在额定质量流量下与额定压力损失相匹配。

### Thermal Liquid Mass and Energy Conservation

整体热液流动的质量守恒为

(dpTLdt∑segments(∂ρseg,TL∂p)+∑segments(dTseg,TLdt∂ρseg,TL∂T))VTLN=m˙A,TL+m˙B,TL,

其中：

- ∂ρseg,TL∂p 是分段密度对压力的偏导数。
- ∂ρseg,TL∂T 是分段密度对温度的偏导数。
- *T*seg,TL 是分段的温度。
- *V*TL 是热液总体积。

求和针对所有分段。

**注意**

尽管该模块将热液流动划分为 *N*=3
个分段以进行传热计算，但它假设所有分段处于相同的内部
压力 *pTL*。因此，
*pTL* 在求和之外。

每个分段的能量守恒方程为

(dpTLdt∂useg,TL∂p+dTseg,TLdt∂useg,TL∂T)MTLN+useg,TL(m˙seg,in,TL−m˙seg,out,TL)=Φseg,in,TL−Φseg,out,TL+Qseg,TL,

其中：

- ∂useg,TL∂p 是分段比内能对压力的偏导数。
- ∂useg,TL∂T 是分段比内能对温度的偏导数。
- *M*TL 是热液总质量。
- m˙seg,in,TL 和 m˙seg,out,TL 是流入和流出分段的质量流量。
- *Φ*seg,in,TL 和
  *Φ*seg,out,TL 是流入和流出分段的能量流量。

该模块假设分段之间的质量流量在
m˙A,TL 和 m˙B,TL 的值之间线性分布。

### Moist Air Mass and Energy Conservation

整体湿空气混合物流动的质量守恒为

(dpMAdt∑segments(∂ρseg,MA∂p)+∑segments(dTseg,MAdt∂ρseg,MA∂T+dxw,seg,MAdt∂ρseg,MA∂xw+dxg,seg,MAdt∂ρseg,MA∂xg))VMAN=m˙A,MA+m˙B,MA−∑segments(m˙w,seg,cond+m˙w,seg,conv)+∑segmentsm˙d,seg,evap,

其中：

- ∂ρseg,MA∂p 是分段密度对压力的偏导数。
- ∂ρseg,MA∂T 是分段密度对温度的偏导数。
- ∂ρseg,MA∂xw 是分段密度对比湿度的偏导数。
- ∂ρseg,MA∂xg 是分段密度对痕量气体质量分数的偏导数。
- *x*w,seg,MA 是分段的*比湿度*，也称为水蒸气质量分数。
- *x*g,seg,MA 是分段的痕量气体质量分数。
- *V*MA 是湿空气总体积。
- m˙w,seg,conv 是分段壁面上的冷凝速率。
- m˙d,seg,evap 是分段水滴蒸发速率。

求和针对所有分段。

**注意**

尽管该模块将湿空气流动划分为 *N*=3 个分段以进行
传热计算，但它假设所有分段处于相同的内部压力
*p*MA。因此，
*p*MA 在求和之外。

每个分段的能量守恒方程为

dTseg,MAdt(c¯seg,MA−Rseg)MMAN+ua,seg,MA(m˙seg,in,MA−m˙seg,out,MA)+(uw,seg,MA−ua,seg,MA)(m˙w,seg,in,MA−m˙w,seg,out,MA)+(ug,seg,MA−ua,seg,MA)(m˙g,seg,in,MA−m˙g,seg,out,MA)+hd(m˙d,seg,in,MA−m˙d,seg,out,MA)=Φseg,in,MA−Φseg,out,MA+Qseg,MA−(1−λd)(m˙w,seg,condhd+m˙w,seg,convhl,wall),

其中：

- *ua,seg,MA* 是分段的干空气比内能。
- *ug,seg,MA* 是分段的痕量气体比内能。
- *uw,seg,MA* 是分段的水蒸气比内能。
- *MMA* 是湿空气总质量。
- m˙seg,in,MA 和 m˙seg,out,MA 是流入和流出分段的湿空气质量流量。
- m˙w,seg,in,MA 和 m˙w,seg,out,MA 是流入和流出分段的水蒸气质量流量。
- m˙g,seg,in,MA 和 m˙g,seg,out,MA 是流入和流出分段的痕量气体质量流量。
- m˙d,seg,in,MA 和 m˙d,seg,out,MA 是流入和流出分段的水滴质量流量。
- *Rseg* 是分段体积比气体常数。
- *Φ*seg,in,MA 和
  *Φ*seg,out,MA 是流入和流出分段的能量流量。
- *hd* 是分段中水滴的比焓。
- *λd* 是 **Fraction
  of condensate entrained as water droplets** 参数的值。

该模块假设分段之间的质量流量在
m˙A,MA 和 m˙B,MA 的值之间线性分布。

每个分段的水蒸气质量守恒方程为

dxw,seg,MAdtMMAN+xw,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙w,seg,in,MA−m˙w,seg,out,MA−m˙w,seg,cond−m˙w,seg,conv+m˙d,seg,evap.

每个分段的痕量气体质量守恒方程为

dxg,seg,MAdtMMAN+xg,seg,MA(m˙seg,in,MA−m˙seg,out,MA)=m˙g,seg,in,MA−m˙g,seg,out,MA.

每个分段的水滴质量平衡守恒方程为

drd,segdtMMAN+rd,seg(m˙seg,in,MA−m˙seg,out,MA)=m˙d,seg,in−m˙d,seg,out+λd(m˙w,seg,cond+m˙w,seg,conv)−m˙d,seg,evap,

其中 *rd,seg* 是分段流体体积中水滴与湿空气的质量比。

**注意**

如果 Moist Air Properties
(MA) 模块中的 **Trace gas model** 参数为
`None`，则湿空气网络不建模痕量气体。在这种
情况下，在 System-Level Heat Exchanger (TL-MA) 模块中，痕量气体的守恒方程设置为
0。

如果在 Moist Air Properties (MA) 模块中清除 **Enable entrained water droplets**，则湿空气网络
不建模夹带水滴。在这种情况下，在 System-Level Heat Exchanger (TL-MA) 模块中，
水滴的守恒方程设置为 0。

### 假设和限制

- 在确定换热器尺寸时，该模块忽略 **Fraction of condensate entrained as water droplets** 参数的值，并假设冷凝物不作为液滴夹带。
