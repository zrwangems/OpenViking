---
type: simulink-block
title: 'System-Level Heat Exchanger (TL-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid'
documentation_page: 'systemlevelheatexchangertltl'
documentation_source_path: 'ref/systemlevelheatexchangertltl.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Heat Exchanger (TL-TL)

## 端口
```yaml
ports:
- name: Q1
  summary: 传递到热液体 1 的热传递速率，W 物理信号
  direction: output
- name: Q2
  summary: 传递到热液体 2 的热传递速率，W 物理信号
  direction: output
- name: A1
  summary: 侧 1 的热液体端口 热液体
  direction: output
- name: B1
  summary: 侧 1 的热液体端口 热液体
  direction: output
- name: A2
  summary: 侧 2 的热液体端口 热液体
  direction: output
- name: B2
  summary: 侧 2 的热液体端口 热液体
  direction: output
```

### 输出

### **Q1** — 传递到热液体 1 的热传递速率，W 物理信号

传递到热液体 1 的热传递速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果选中 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分被传递的热量。

### **Q2** — 传递到热液体 2 的热传递速率，W 物理信号

传递到热液体 2 的热传递速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果选中 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分被传递的热量。
### 守恒

### **A1** — 侧 1 的热液体端口 热液体

与第一个热液体网络相关联的入口或出口端口。

### **B1** — 侧 1 的热液体端口 热液体

与第一个热液体网络相关联的入口或出口端口。

### **A2** — 侧 2 的热液体端口 热液体

与第二个热液体网络相关联的入口或出口端口。

### **B2** — 侧 2 的热液体端口 热液体

与第二个热液体网络相关联的入口或出口端口。
## 参数
```yaml
parameters:
- name: Flow arrangement at nominal operating conditions
  summary: 流路对齐方式 Counter flow - Thermal Liquid 1 flows from A to B, Thermal Liquid 2 flows from B to A（默认）| Parallel flow
    - Both fluids flow from A to B | Cross flow - Both fluids flow from A to B
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
  summary: 标称工况 Heat transfer from Thermal Liquid 1 to Thermal Liquid 2（默认）| Heat transfer from Thermal Liquid 2 to Thermal
    Liquid 1
  group: 热液体 1
- name: Nominal mass flow rate
  summary: 标称工况下热液体 1 端口之间的质量流量 0.1 kg/s（默认）| 正标量
  group: 热液体 1
- name: Nominal pressure drop
  summary: 标称工况下热液体 1 端口之间的压降 0.01 MPa（默认）| 正标量
  group: 热液体 1
- name: Nominal inlet pressure
  summary: 热液体 1 入口处的压力 0.101325 MPa（默认）| 正标量
  group: 热液体 1
- name: Nominal inlet temperature
  summary: 热液体 1 入口处的温度 333.15 K（默认）| 正标量
  group: 热液体 1
- name: Heat transfer capacity specification
  summary: 如何指定热液体 1 的热传递能力 Rate of heat transfer（默认）| Outlet condition
  group: 热液体 1
- name: Nominal rate of heat transfer
  summary: 热传递速率 1 kW（默认）| 正标量
  group: 热液体 1
- name: Nominal outlet temperature
  summary: 出口温度 323.15 K（默认）| 正标量
  group: 热液体 1
- name: Thermal liquid 1 volume
  summary: 热液体 1 的总体积 0.001 m^3（默认）| 正标量
  group: 热液体 1
- name: Initialize thermal liquid 1 to nominal operating conditions
  summary: 初始化热液体 1 的选项 on（默认）| off
  group: 热液体 1
- name: Initial thermal liquid 1 pressure
  summary: 仿真开始时热液体 1 的压力 0.101325 MPa（默认）| 正标量
  group: 热液体 1
- name: Initial thermal liquid 1 temperature
  summary: 仿真开始时热液体 1 的温度 293.15 K（默认）| 正标量
  group: 热液体 1
- name: Nominal mass flow rate
  summary: 标称工况下热液体 2 端口之间的质量流量 0.1 kg/s（默认）| 正标量
  group: 热液体 2
- name: Nominal pressure drop
  summary: 标称工况下热液体 2 端口之间的压降 0.01 MPa（默认）| 正标量
  group: 热液体 2
- name: Nominal inlet pressure
  summary: 热液体 2 入口处的压力 0.101325 MPa（默认）| 正标量
  group: 热液体 2
- name: Nominal inlet temperature
  summary: 热液体 2 入口处的温度 293.15 K（默认）| 正标量
  group: 热液体 2
- name: Thermal liquid 2 volume
  summary: 换热器中热液体 2 的总体积 0.001 m^3（默认）| 正标量
  group: 热液体 2
- name: Initialize thermal liquid 2 to nominal operating conditions
  summary: 初始化热液体 2 的选项 on（默认）| off
  group: 热液体 2
- name: Initial thermal liquid 2 pressure
  summary: 仿真开始时热液体 2 的压力 0.101325 MPa（默认）| 正标量
  group: 热液体 2
- name: Initial thermal liquid 2 temperature
  summary: 仿真开始时热液体 2 的温度 293.15 K（默认）| 正标量 | 二元素向量
  group: 热液体 2
- name: a in Nu = a\*Re^b\*Pr^c for thermal liquid 1
  summary: 热液体 1 的关联式系数 0.023（默认）| 正标量
  group: 关联式系数
- name: b in Nu = a\*Re^b\*Pr^c for thermal liquid 1
  summary: 热液体 1 关联式中的雷诺数指数 0.8（默认）| 正标量
  group: 关联式系数
- name: c in Nu = a\*Re^b\*Pr^c for thermal liquid 1
  summary: 热液体 1 关联式中的普朗特数指数 0.33（默认）| 正标量
  group: 关联式系数
- name: a in Nu = a\*Re^b\*Pr^c for thermal liquid 2
  summary: 热液体 2 的关联式系数 0.023（默认）| 正标量
  group: 关联式系数
- name: b in Nu = a\*Re^b\*Pr^c for thermal liquid 2
  summary: 热液体 2 关联式中的雷诺数指数 0.8（默认）| 正标量
  group: 关联式系数
- name: c in Nu = a\*Re^b\*Pr^c for thermal liquid 2
  summary: 热液体 2 关联式中的普朗特数指数 0.33（默认）| 正标量
  group: 关联式系数
```

### 配置

### **Flow arrangement at nominal operating conditions** — 流路对齐方式 `Counter flow - Thermal Liquid 1 flows from A to B, Thermal Liquid 2 flows from B to A`（默认）| `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

在标称工况下换热器两侧之间的流路对齐方式。可用的流动布置方式有：

- `Counter flow - Thermal Liquid 1 flows from A
  to B, Thermal Liquid 2 flows from B to A` —
  两股流体彼此平行流动，方向相反。
- `Parallel flow - Both fluids flow from A to
  B` — 两股流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to
  B` — 两股流体彼此垂直流动。

平行流和逆流之间的选择会影响模块确定换热器尺寸的方式。逆流设置最为有效，满足指定性能所需的尺寸最小。相反，平行流效果最差，满足指定性能所需的尺寸最大。

标称工况下的流动方向（从 A 到 B，或从 B 到 A）仅在选中 **Initialize thermal liquid 1 to nominal operating conditions** 或 **Initialize thermal liquid 2 to nominal operating conditions** 时影响模型初始化。如果设置了不同的初始工况，流动方向可以不同。

在模块确定换热器尺寸之后，此设置不再影响模块在仿真期间计算热传递的方式。相反，热传递取决于仿真期间的流动方向。例如，如果将该参数设置为平行流，但将模型设置为以逆流方式运行，则即使其余边界条件相同，仿真期间的热传递速率也不会与指定性能匹配。

如果将该参数设置为交叉流，则模块将换热器内部的流路建模为相互垂直，因此仿真期间的流动方向无关紧要。

### **Enable wall thermal mass** — 是否启用热质量对传热表面的影响 `off`（默认）| `on`

是否启用热质量对传热表面的影响。选中此参数时，模块会为仿真引入额外的动态特性，达到稳态所需的时间更长，但此参数不会影响稳态仿真结果。

### **Wall mass** — 传热表面的质量 `1 kg`（默认）| 正标量

传热表面的质量。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Wall specific heat** — 传热表面的比热 `490 J/(K*kg)`（默认）| 正标量

传热表面的比热。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Initialize wall temperature to nominal operating conditions** — 初始化壁面温度的选项 `on`（默认）| `off`

将壁面温度初始化为标称工况或指定值的选项。如果选中此参数，模块将根据为两侧流体指定的标称工况计算初始壁面温度。如果清除此参数，则可以使用 **Initial wall temperature** 参数直接指定初始壁面温度。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass**。

### **Initial wall temperature** — 壁面的初始温度 `293.15 K`（默认）| 正标量或二元素向量

壁面的初始温度。如果指定标量，模块假定初始壁面温度是均匀的。如果指定二元素向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 之间以及端口 **B1** 和 **B2** 之间线性变化。第一个元素对应端口 **A1** 和 **A2** 处的温度，第二个元素对应端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选中 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液体 1 端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液体 1 端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

热液体 2 端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

热液体 2 端口 **B2** 处的流通面积。

### 热液体 1

### **Nominal operating condition** — 标称工况 `Heat transfer from Thermal Liquid 1 to Thermal Liquid 2`（默认）| `Heat transfer from Thermal Liquid 2 to Thermal Liquid 1`

用于热液体 1 网络的标称工况：

- `Heat transfer from Thermal Liquid 1 to Thermal
  Liquid 2` — 侧 1 被冷却，侧 2 被加热。
- `Heat transfer from Thermal Liquid 2 to Thermal
  Liquid 1` — 侧 2 被冷却，侧 1 被加热。

此设置仅与标称工况参数相关。它并不意味着在仿真期间热传递只能沿指定方向发生。

### **Nominal mass flow rate** — 标称工况下热液体 1 端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1** 的质量流量。

### **Nominal pressure drop** — 标称工况下热液体 1 端口之间的压降 `0.01 MPa`（默认）| 正标量

标称工况下从端口 **A1** 到端口 **B1** 的压降。

### **Nominal inlet pressure** — 热液体 1 入口处的压力 `0.101325 MPa`（默认）| 正标量

标称工况下换热器热液体 1 入口处的压力。

### **Nominal inlet temperature** — 热液体 1 入口处的温度 `333.15 K`（默认）| 正标量

标称工况下换热器热液体 1 入口处的温度。

### **Heat transfer capacity specification** — 如何指定热液体 1 的热传递能力 `Rate of heat transfer`（默认）| `Outlet condition`

是直接通过热传递速率，还是间接通过出口工况来指定换热器在标称工况下对热液体 1 的性能。

### **Nominal rate of heat transfer** — 热传递速率 `1 kW`（默认）| 正标量

热传递速率。**Nominal Operating condition** 参数决定热量从哪个热液体网络传递以及传递到哪个热液体网络：

- 如果 **Nominal operating condition** 为 `Heat transfer from Thermal Liquid 1 to Thermal
  Liquid 2`，则此参数为标称工况下从热液体侧 1 传递到热液体侧 2 的热传递速率。
- 如果 **Nominal operating condition** 为 `Heat transfer from Thermal Liquid 2 to Thermal
  Liquid 1`，则此参数为标称工况下从热液体侧 1 传递到热液体侧 1 的热传递速率。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Rate of heat
transfer`。

### **Nominal outlet temperature** — 出口温度 `323.15 K`（默认）| 正标量

标称工况下换热器热液体 1 出口处的温度。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Outlet
condition`。

### **Thermal liquid 1 volume** — 热液体 1 的总体积 `0.001 m^3`（默认）| 正标量

换热器内热液体 1 的总体积。

### **Initialize thermal liquid 1 to nominal operating conditions** — 初始化热液体 1 的选项 `on`（默认）| `off`

将热液体 1 初始化为标称工况或指定值的选项。如果选中此参数，模块将热液体 1 初始化为标称工况。如果清除此复选框，则可以使用附加参数直接指定初始条件。

### **Initial thermal liquid 1 pressure** — 仿真开始时热液体 1 的压力 `0.101325 MPa`（默认）| 正标量

仿真开始时热液体 1 的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize thermal liquid 1 to nominal operating conditions** 复选框。

### **Initial thermal liquid 1 temperature** — 仿真开始时热液体 1 的温度 `293.15 K`（默认）| 正标量

仿真开始时热液体 1 的温度。

#### 依赖关系

要启用此参数，请清除 **Initialize thermal liquid 1 to nominal operating conditions** 复选框。

### 热液体 2

### **Nominal mass flow rate** — 标称工况下热液体 2 端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

标称工况下从端口 **A2** 到端口 **B2** 的质量流量。

### **Nominal pressure drop** — 标称工况下热液体 2 端口之间的压降 `0.01 MPa`（默认）| 正标量

标称工况下从端口 **A2** 到端口 **B2** 的压降。

### **Nominal inlet pressure** — 热液体 2 入口处的压力 `0.101325 MPa`（默认）| 正标量

标称工况下换热器热液体 2 入口处的压力。

### **Nominal inlet temperature** — 热液体 2 入口处的温度 `293.15 K`（默认）| 正标量

标称工况下换热器热液体 2 入口处的温度。

### **Thermal liquid 2 volume** — 换热器中热液体 2 的总体积 `0.001 m^3`（默认）| 正标量

换热器中热液体 2 的总体积。

### **Initialize thermal liquid 2 to nominal operating conditions** — 初始化热液体 2 的选项 `on`（默认）| `off`

将热液体 2 初始化为标称工况或指定值的选项。如果选中此参数，模块将热液体 2 初始化为标称工况。如果清除此复选框，则可以使用附加参数直接指定初始条件。

### **Initial thermal liquid 2 pressure** — 仿真开始时热液体 2 的压力 `0.101325 MPa`（默认）| 正标量

仿真开始时热液体 2 的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize thermal liquid 2 to nominal operating conditions** 复选框。

### **Initial thermal liquid 2 temperature** — 仿真开始时热液体 2 的温度 `293.15 K`（默认）| 正标量 | 二元素向量

仿真开始时热液体 2 的温度。如果该值为标量，则模块假定初始温度是均匀的。如果该值为二元素向量，则模块假定初始温度在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **Initialize thermal liquid 2 to nominal operating conditions** 复选框。

### 关联式系数

### **a in Nu = a\*Re^b\*Pr^c for thermal liquid 1** — 热液体 1 的关联式系数 `0.023`（默认）| 正标量

热液体 1 的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for thermal liquid 1** — 热液体 1 关联式中的雷诺数指数 `0.8`（默认）| 正标量

热液体 1 的努塞尔数作为雷诺数和普朗特数函数的关联式中的雷诺数指数。

### **c in Nu = a\*Re^b\*Pr^c for thermal liquid 1** — 热液体 1 关联式中的普朗特数指数 `0.33`（默认）| 正标量

热液体 1 的努塞尔数作为雷诺数和普朗特数函数的关联式中的普朗特数指数。

### **a in Nu = a\*Re^b\*Pr^c for thermal liquid 2** — 热液体 2 的关联式系数 `0.023`（默认）| 正标量

热液体 2 的努塞尔数作为雷诺数和普朗特数函数的关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for thermal liquid 2** — 热液体 2 关联式中的雷诺数指数 `0.8`（默认）| 正标量

热液体 2 的努塞尔数作为雷诺数和普朗特数函数的关联式中的雷诺数指数。默认值基于 Colburn 方程。

### **c in Nu = a\*Re^b\*Pr^c for thermal liquid 2** — 热液体 2 关联式中的普朗特数指数 `0.33`（默认）| 正标量

热液体 2 的努塞尔数作为雷诺数和普朗特数函数的关联式中的普朗特数指数。默认值基于 Colburn 方程。
## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

基于两个热液体网络之间的性能数据的换热器

System-Level Heat Exchanger (TL-TL) 模块基于两个热液体网络之间的性能数据来建模换热器。每个网络都有自己的一组流体属性。

该模块使用换热器数据表中的性能数据，而不是换热器的详细几何结构。您可以在设计迭代期间调整换热器的尺寸和性能，或者对具有不常见几何结构的换热器进行建模。您还可以在早期设计阶段使用此模块来建模具有一定性能水平的换热器，此时详细的几何数据尚不可用。

您通过额定工况来参数化该模块。该模块对换热器进行 sizing，以在稳态下匹配额定工况下的指定性能。

该模块与 Heat Exchanger (TL-TL) 模块类似，但使用不同的参数化模型。下表比较了这两个模块：

| Heat Exchanger (TL-TL) | System-Level Heat Exchanger (TL-TL) |
| --- | --- |
| 模块参数基于换热器几何结构 | 模块参数基于性能和工况 |
| 换热器几何结构可能受可用几何参数选项的限制 | 模型独立于特定的换热器几何结构 |
| 您可以通过调整几何参数（如翅片尺寸和管长）来使模块适应不同的性能要求 | 您可以通过直接指定所需的热流量和质量流量来使模块适应不同的性能要求 |
| 您可以在平行流、逆流、壳管式或交叉流配置之间进行选择 | 您可以在额定工况下在平行流、逆流或交叉流布置之间进行选择，以帮助进行 sizing |
| 在广泛的工况范围内具有预测性准确的结果，取决于 E-NTU 方程和传热系数关联式的适用性 | 在指定工况附近结果非常准确；远离指定工况时精度可能会降低 |
| 传热计算通过使用 E-NTU 模型来考虑温度沿流动路径的变化 | 传热计算通过将流动路径分为三段来近似温度沿流动路径的变化 |

### 传热

该模块将模块中的两股热液流（热液体 1 和热液体 2）分为三个大小相等的段。该模块计算每个段中流体之间的传热。为简单起见，本节中的方程针对一个段。

如果您清除 **Enable wall thermal mass** 复选框，则换热器中的热平衡为

Qseg,TL1+Qseg,TL2=0，

其中：

- *Qseg,TL1* 是从壁面（即传热表面）到段中热液体 1 的热流量。
- *Qseg,TL2* 是从壁面到段中热液体 2 的热流量。

如果您选择 **Enable wall thermal mass**，则换热器中的热平衡为

Qseg,TL1+Qseg,TL2=−MwallcpwallNdTseg,walldt，

其中：

- *Mwall* 是壁面的质量。
- *cpwall* 是壁面的比热。
- *N* = 3 是段数。
- *Tseg,wall* 是段中的平均壁面温度。
- *t* 是时间。

从壁面到段中热液体 1 的热流量为

Qseg,TL1=UAseg,TL1(Tseg,wall−Tseg,TL1)，

其中：

- *UAseg,TL1* 是段中热液体 1 的传热导。
- *Tseg,TL1* 是段中的平均液体温度。

从壁面到段中热液体 2 的热流量为

Qseg,TL2=UAseg,TL2(Tseg,wall−Tseg,TL2)，

其中：

- *UAseg,TL2* 是段中热液体 2 的传热导。
- *Tseg,TL2* 是段中热液体 2 的平均温度。

该模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 热液体传热关联式

该模块使用相同的表达式计算两种热液体中的传热导。为简单起见，本节中显示的方程针对一侧，但适用于两侧。传热导方程为：

UAseg,TL=aTL(Reseg,TL)bTL(Prseg,TL)cTLkseg,TLGTLN，

其中：

- *aTL*、*bTL* 和 *cTL* 是努塞尔数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Reseg,TL* 是段中的平均雷诺数。
- *Prseg,TL* 是段中的平均普朗特数。
- *kseg,TL* 是段中的平均热导率。
- *GTL* 是换热器热液体侧的几何比例因子。该模块计算几何比例因子，使得所有段上的总传热在额定工况下与指定性能匹配。

平均雷诺数为

Reseg,TL=m˙seg,TLDref,TLμseg,TLSref,TL，

其中：

- m˙seg,TL 是通过该段的质量流量。
- *μseg,TL* 是段中的平均动力粘度。
- *Dref,TL* 是任意参考直径。
- *Sref,TL* 是任意参考流通面积。

**注意**

*Dref,TL* 和 *Sref,TL* 项包含在此方程中仅用于单位计算目的，以使 *Reseg,TL* 无量纲。*Dref,TL* 和 *Sref,TL* 的值是任意的，因为 *GTL* 计算会覆盖这些值。

### 压力损失

热液体 1 侧的压力损失为

pA,TL1−pTL1=KTL12m˙A,TL1m˙2A,TL1+m˙2thres,TL12ρavg,TL1pB,TL1−pTL1=KTL12m˙B,TL1m˙2B,TL1+m˙2thres,TL12ρavg,TL1

其中：

- *pA,TL1* 和 *pB,TL1* 分别是端口 **A1** 和 **B1** 处的压力。
- *pTL1* 是该模块计算传热时的内部热液体 1 压力。
- *ṁA,TL1* 和 *ṁB,TL1* 分别是流入端口 **A1** 和 **B1** 的质量流量。
- *ρavg,TL1* 是所有段上的平均热液体 1 密度。
- *ṁthres,TL1* 是压力损失的层流阈值，近似为额定质量流量的 1e-4。该模块计算压力损失系数 *KTL1*，使得 *pA,TL1* – *pB,TL1* 在额定质量流量下与额定压力损失匹配。

热液体 2 侧的压力损失为

pA,TL2−pTL2=KTL22m˙A,TL2m˙2A,TL2+m˙2thres,TL22ρavg,TL2pB,TL2−pTL2=KTL22m˙B,TL2m˙2B,TL2+m˙2thres,TL22ρavg,TL2

其中：

- *pA,TL2* 和 *pB,TL2* 分别是端口 **A2** 和 **B2** 处的压力。
- *pTL2* 是该模块计算传热时的内部热液体 2 压力。
- *ṁA,TL2* 和 *ṁB,TL2* 分别是流入端口 **A2** 和 **B2** 的质量流量。
- *ρavg,TL2* 是所有段上的平均热液体密度。
- *ṁthres,TL2* 是压力损失的层流阈值，近似为额定质量流量的 1e-4。该模块计算压力损失系数 *KTL2*，使得 *pA,TL2* – *pB,TL2* 在额定质量流量下与额定压力损失匹配。

### 热液体质量和能量守恒

该模块对两种热液体使用相同的质量和能量守恒表达式。为简单起见，本节中显示的方程针对一侧，但适用于两侧。

(dpTLdt∑segments(∂ρseg,TL∂p)+∑segments(dTseg,TLdt∂ρseg,TL∂T))VTLN=m˙A,TL+m˙B,TL，

其中：

- ∂ρseg,TL∂p 是段中密度对压力的偏导数。
- ∂ρseg,TL∂T 是段中密度对温度的偏导数。
- *Tseg,TL* 是段的温度。
- *VTL* 是总热液体体积。

求和是对所有段进行的。

**注意**

尽管该模块将两股热液流都分为 *N*=3 个段进行传热计算，但它假设所有段都处于相同的内部压力 *pTL*。因此，*pTL* 在求和之外。

每个段的能量守恒方程为

(dpTLdt∂useg,TL∂p+dTseg,TLdt∂useg,TL∂T)MTLN+useg,TL(m˙seg,in,TL−m˙seg,out,TL)=Φseg,in,TL−Φseg,out,TL+Qseg,TL，

其中：

- ∂useg,TL∂p 是段中比内能对压力的偏导数。
- ∂useg,TL∂T 是段中比内能对温度的偏导数。
- *MTL* 是一侧的总热液体质量。
- m˙seg,in,TL 和 m˙seg,out,TL 是流入和流出该段的质量流量。
- *Φseg,in,TL* 和 *Φseg,out,TL* 是流入和流出该段的能量流量。

该模块假设段之间的质量流量在 m˙A,TL 和 m˙B,TL 的值之间线性分布。
