---
type: simulink-block
title: 'System-Level Heat Exchanger (TL-G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Thermal Liquid - Gas'
documentation_page: 'systemlevelheatexchangertlg'
documentation_source_path: 'ref/systemlevelheatexchangertlg.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Heat Exchanger (TL-G)

## 端口
```yaml
ports:
- name: Q1
  summary: 传递到热液的热传递速率，W 物理信号
  direction: output
- name: Q2
  summary: 传递到气体的热传递速率，W 物理信号
  direction: output
- name: A1
  summary: 热液端口 热液
  direction: output
- name: B1
  summary: 热液端口 热液
  direction: output
- name: A2
  summary: 气体端口 气体
  direction: output
- name: B2
  summary: 气体端口 气体
  direction: output
```

### 输出

### **Q1** — 传递到热液的热传递速率，W 物理信号

传递到热液的热传递速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分被传递的热量。

### **Q2** — 传递到气体的热传递速率，W 物理信号

传递到气体的热传递速率，以物理信号形式返回，单位为 W。端口 **Q1** 和 **Q2** 处的物理信号通常数值相等、符号相反。但是，如果您选择 **Enable wall thermal mass**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分被传递的热量。
### 守恒

### **A1** — 热液端口 热液

与热液网络相关的入口或出口端口。

### **B1** — 热液端口 热液

与热液网络相关的入口或出口端口。

### **A2** — 气体端口 气体

与气体网络相关的入口或出口端口。

### **B2** — 气体端口 气体

与气体网络相关的入口或出口端口。
## 参数
```yaml
parameters:
- name: Flow arrangement at nominal operating conditions
  summary: 额定工况下的流路对齐方式 Counter flow - Thermal Liquid 1 flows from A to B, Gas 2 flows from B to A（默认）| Parallel flow - Both
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
  summary: 壁面温度初始化选项 on（默认）| off
  group: 配置
- name: Initial wall temperature
  summary: 壁面初始温度 293.15 K（默认）| 正标量或双元素向量
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
  summary: 额定工况 Heat transfer from Thermal Liquid 1 to Gas 2（默认）| Heat transfer from Gas 2 to Thermal Liquid 1
  group: Thermal Liquid 1
- name: Nominal mass flow rate
  summary: 额定工况下热液端口之间的质量流量 0.1 kg/s（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal pressure drop
  summary: 额定工况下热液端口之间的压降 0.01 MPa（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal inlet pressure
  summary: 热液入口处的压力 0.101325 MPa（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal inlet temperature
  summary: 热液入口处的温度 333.15 K（默认）| 正标量
  group: Thermal Liquid 1
- name: Heat transfer capacity specification
  summary: 如何指定热液的传热能力 Rate of heat transfer（默认）| Outlet condition
  group: Thermal Liquid 1
- name: Nominal rate of heat transfer
  summary: 热传递速率 1 kW（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal outlet temperature
  summary: 出口温度 323.15 K（默认）| 正标量
  group: Thermal Liquid 1
- name: Thermal liquid volume
  summary: 热液总体积 0.001 m^3（默认）| 正标量
  group: Thermal Liquid 1
- name: Initialize thermal liquid to nominal operating conditions
  summary: 热液初始化选项 on（默认）| off
  group: Thermal Liquid 1
- name: Initial thermal liquid pressure
  summary: 仿真开始时的热液压力 0.101325 MPa（默认）| 正标量
  group: Thermal Liquid 1
- name: Initial thermal liquid temperature
  summary: 仿真开始时的热液温度 293.15 K（默认）| 正标量
  group: Thermal Liquid 1
- name: Nominal mass flow rate
  summary: 额定工况下气体端口之间的质量流量 0.1 kg/s（默认）| 正标量
  group: Gas 2
- name: Nominal pressure drop
  summary: 额定工况下气体端口之间的压降 0.001 MPa（默认）| 正标量
  group: Gas 2
- name: Nominal inlet pressure
  summary: 气体入口处的压力 0.101325 MPa（默认）| 正标量
  group: Gas 2
- name: Nominal inlet temperature
  summary: 气体入口处的温度 293.15 K（默认）| 正标量
  group: Gas 2
- name: Gas volume
  summary: 换热器中气体的总体积 0.1 m^3（默认）| 正标量
  group: Gas 2
- name: Initialize gas to nominal operating conditions
  summary: 气体初始化选项 on（默认）| off
  group: Gas 2
- name: Initial gas pressure
  summary: 仿真开始时的气体压力 0.101325 MPa（默认）| 正标量
  group: Gas 2
- name: Initial gas temperature
  summary: 仿真开始时的气体温度 293.15 K（默认）| 正标量
  group: Gas 2
- name: a in Nu = a\*Re^b\*Pr^c for thermal liquid
  summary: 热液的关联式系数 0.023（默认）| 正标量
  group: 关联式系数
- name: b in Nu = a\*Re^b\*Pr^c for thermal liquid
  summary: 热液关联式中的雷诺数指数 0.8（默认）| 正标量
  group: 关联式系数
- name: c in Nu = a\*Re^b\*Pr^c for thermal liquid
  summary: 热液关联式中的普朗特数指数 0.33（默认）| 正标量
  group: 关联式系数
- name: a in Nu = a\*Re^b\*Pr^c for gas
  summary: 气体的关联式系数 0.023（默认）| 正标量
  group: 关联式系数
- name: b in Nu = a\*Re^b\*Pr^c for gas
  summary: 气体关联式中的雷诺数指数 0.8（默认）| 正标量
  group: 关联式系数
- name: c in Nu = a\*Re^b\*Pr^c for gas
  summary: 气体关联式中的普朗特数指数 0.33（默认）| 正标量
  group: 关联式系数
```

### 配置

### **Flow arrangement at nominal operating conditions** — 额定工况下的流路对齐方式 `Counter flow - Thermal Liquid 1 flows from A to B, Gas 2 flows from B to A`（默认）| `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

额定工况下换热器两侧之间的流路对齐方式。可用的流动布置方式有：

- `Counter flow - Thermal Liquid 1 flows from A
  to B, Gas 2 flows from B to A` — 两股流体彼此平行流动，方向相反。
- `Parallel flow - Both fluids flow from A to
  B` — 两股流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to
  B` — 两股流体彼此垂直流动。

平行流和逆流之间的选择会影响模块确定换热器尺寸的方式。逆流设置最为有效，满足指定性能所需的尺寸最小。相反，平行流效果最差，满足指定性能所需的尺寸最大。

额定工况下的流动方向（从 A 到 B，或从 B 到 A）仅在您选择 **Initialize thermal liquid to nominal operating conditions** 或 **Initialize gas to nominal operating conditions** 时影响模型初始化。如果您设置了不同的初始工况，则流动方向可以不同。

在模块确定换热器尺寸之后，此设置在仿真期间不影响模块计算热传递的方式。相反，热传递取决于仿真期间的流动方向。例如，如果您将参数设置为平行流，但将模型设置为以逆流方式运行，则即使其余边界条件相同，仿真期间的热传递速率也不会与指定性能匹配。

如果您将参数设置为交叉流，则模块将换热器内部的流路建模为垂直，因此仿真期间的流动方向无关紧要。

### **Enable wall thermal mass** — 是否启用热质量对传热表面的影响 `off`（默认）| `on`

是否启用热质量对传热表面的影响。当您选择此参数时，模块会为仿真引入额外的动态特性，达到稳态所需的时间更长，但此参数不影响稳态仿真结果。

### **Wall mass** — 传热表面的质量 `1 kg`（默认）| 正标量

传热表面的质量。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Wall specific heat** — 传热表面的比热 `490 J/(K*kg)`（默认）| 正标量

传热表面的比热。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Initialize wall temperature to nominal operating conditions** — 壁面温度初始化选项 `on`（默认）| `off`

将壁面温度初始化为额定工况或指定值的选项。如果您选择此参数，模块将根据为两侧流体指定的额定工况计算初始壁面温度。如果您清除此参数，则可以直接使用 **Initial wall temperature** 参数指定初始壁面温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass**。

### **Initial wall temperature** — 壁面初始温度 `293.15 K`（默认）| 正标量或双元素向量

壁面的初始温度。如果您指定标量，模块假定初始壁面温度是均匀的。如果您指定双元素向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 之间以及端口 **B1** 和 **B2** 之间线性变化。第一个元素对应端口 **A1** 和 **A2** 处的温度，第二个元素对应端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选择 **Enable wall thermal mass** 并清除 **Initialize wall temperature to nominal operating conditions** 复选框。

### **Cross-sectional area at port A1** — 端口 A1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液端口 **A1** 处的流通面积。

### **Cross-sectional area at port B1** — 端口 B1 处的流通面积 `0.01 m^2`（默认）| 正标量

热液端口 **B1** 处的流通面积。

### **Cross-sectional area at port A2** — 端口 A2 处的流通面积 `0.01 m^2`（默认）| 正标量

气体端口 **A2** 处的流通面积。

### **Cross-sectional area at port B2** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认）| 正标量

气体端口 **B2** 处的流通面积。

### Thermal Liquid 1

### **Nominal operating condition** — 额定工况 `Heat transfer from Thermal Liquid 1 to Gas 2`（默认）| `Heat transfer from Gas 2 to Thermal Liquid 1`

用于热液网络的额定工况：

- `Heat transfer from Thermal Liquid 1 to Gas
  2` — 热液被冷却，气体被加热。
- `Heat transfer from Gas 2 to Thermal Liquid
  1` — 气体被冷却，热液被加热。

此设置仅与额定工况参数相关。这并不意味着仿真期间热传递只能沿指定方向发生。

### **Nominal mass flow rate** — 额定工况下热液端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

额定工况下从端口 **A1** 到端口 **B1** 的质量流量。

### **Nominal pressure drop** — 额定工况下热液端口之间的压降 `0.01 MPa`（默认）| 正标量

额定工况下从端口 **A1** 到端口 **B1** 的压降。

### **Nominal inlet pressure** — 热液入口处的压力 `0.101325 MPa`（默认）| 正标量

额定工况下换热器热液入口处的压力。

### **Nominal inlet temperature** — 热液入口处的温度 `333.15 K`（默认）| 正标量

额定工况下换热器热液入口处的温度。

### **Heat transfer capacity specification** — 如何指定热液的传热能力 `Rate of heat transfer`（默认）| `Outlet condition`

是直接通过热传递速率，还是间接通过出口条件来指定换热器在额定工况下对热液的性能。

### **Nominal rate of heat transfer** — 热传递速率 `1 kW`（默认）| 正标量

热传递速率。**Nominal Operating condition** 参数决定热量从哪个网络传递到哪个网络：

- 如果 **Nominal operating condition** 为 `Heat transfer from Thermal Liquid 1 to Gas
  2`，则此参数为额定工况下从热液到气体的热传递速率。
- 如果 **Nominal operating condition** 为 `Heat transfer from Gas 2 to Thermal Liquid
  1`，则此参数为额定工况下从气体到热液的热传递速率。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Rate of heat
transfer`。

### **Nominal outlet temperature** — 出口温度 `323.15 K`（默认）| 正标量

额定工况下换热器热液出口处的温度。

#### 依赖关系

要启用此参数，请将 **Heat transfer capacity specification** 设置为 `Outlet
condition`。

### **Thermal liquid volume** — 热液总体积 `0.001 m^3`（默认）| 正标量

换热器内部热液的总体积。

### **Initialize thermal liquid to nominal operating conditions** — 热液初始化选项 `on`（默认）| `off`

将热液初始化为额定工况或指定值的选项。如果您选择此参数，模块将热液初始化为额定工况。如果您清除此复选框，则可以使用附加参数直接指定初始条件。

### **Initial thermal liquid pressure** — 仿真开始时的热液压力 `0.101325 MPa`（默认）| 正标量

仿真开始时热液的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize thermal liquid to nominal operating conditions** 复选框。

### **Initial thermal liquid temperature** — 仿真开始时的热液温度 `293.15 K`（默认）| 正标量

仿真开始时热液的温度。

#### 依赖关系

要启用此参数，请清除 **Initialize thermal liquid to nominal operating conditions** 复选框。

### Gas 2

### **Nominal mass flow rate** — 额定工况下气体端口之间的质量流量 `0.1 kg/s`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的质量流量。

### **Nominal pressure drop** — 额定工况下气体端口之间的压降 `0.001 MPa`（默认）| 正标量

额定工况下从端口 **A2** 到端口 **B2** 的压降。

### **Nominal inlet pressure** — 气体入口处的压力 `0.101325 MPa`（默认）| 正标量

额定工况下换热器气体入口处的压力。

### **Nominal inlet temperature** — 气体入口处的温度 `293.15 K`（默认）| 正标量

额定工况下换热器气体入口处的温度。

### **Gas volume** — 换热器中气体的总体积 `0.1 m^3`（默认）| 正标量

换热器内部气体的总体积。

### **Initialize gas to nominal operating conditions** — 气体初始化选项 `on`（默认）| `off`

将气体初始化为额定工况或指定值的选项。如果您选择此参数，模块将气体初始化为额定工况。如果您清除此复选框，则可以使用附加参数直接指定初始条件。

### **Initial gas pressure** — 仿真开始时的气体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时气体的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize gas to nominal operating conditions** 复选框。

### **Initial gas temperature** — 仿真开始时的气体温度 `293.15 K`（默认）| 正标量

仿真开始时气体的温度。

#### 依赖关系

要启用此参数，请清除 **Initialize gas to nominal operating conditions** 复选框。

### 关联式系数

### **a in Nu = a\*Re^b\*Pr^c for thermal liquid** — 热液的关联式系数 `0.023`（默认）| 正标量

热液的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for thermal liquid** — 热液关联式中的雷诺数指数 `0.8`（默认）| 正标量

热液的努塞尔数作为雷诺数和普朗特数的函数关联式中的雷诺数指数。

### **c in Nu = a\*Re^b\*Pr^c for thermal liquid** — 热液关联式中的普朗特数指数 `0.33`（默认）| 正标量

热液的努塞尔数作为雷诺数和普朗特数的函数关联式中的普朗特数指数。

### **a in Nu = a\*Re^b\*Pr^c for gas** — 气体的关联式系数 `0.023`（默认）| 正标量

气体的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

### **b in Nu = a\*Re^b\*Pr^c for gas** — 气体关联式中的雷诺数指数 `0.8`（默认）| 正标量

气体的努塞尔数作为雷诺数和普朗特数的函数关联式中的雷诺数指数。默认值基于 Colburn 方程。

### **c in Nu = a\*Re^b\*Pr^c for gas** — 气体关联式中的普朗特数指数 `0.33`（默认）| 正标量

气体的努塞尔数作为雷诺数和普朗特数的函数关联式中的普朗特数指数。默认值基于 Colburn 方程。
## 所属库

Simscape / Fluids / Heat Exchangers / Thermal Liquid - Gas

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

基于热液体与气体网络之间性能数据的换热器

System-Level Heat Exchanger (TL-G) 模块基于热液体与气体网络之间的性能数据对换热器进行建模。

该模块使用换热器数据表中的性能数据，而非换热器的详细几何结构。您可以在设计迭代过程中调整换热器的尺寸和性能，或对具有特殊几何结构的换热器进行建模。您还可以在早期设计阶段使用该模块对具有一定性能水平的换热器进行建模，此时详细的几何数据尚不可用。

您通过额定工况对模块进行参数化。模块对换热器进行尺寸设定，使其在稳态额定工况下匹配指定的性能。

该模块与 Heat Exchanger (G-TL) 模块类似，但使用不同的参数化模型。下表比较了这两个模块：

| Heat Exchanger (G-TL) | System-Level Heat Exchanger (TL-G) |
| --- | --- |
| 模块参数基于换热器几何结构 | 模块参数基于性能和工况 |
| 换热器几何结构可能受可用几何参数选项的限制 | 模型独立于特定换热器几何结构 |
| 您可以通过调整几何参数（如翅片尺寸和管长）来使模块适应不同的性能要求 | 您可以通过直接指定所需的热流量和质量流量来使模块适应不同的性能要求 |
| 您可以在平行流、逆流、管壳式或交叉流配置之间进行选择 | 您可以在额定工况下在平行流、逆流或交叉流布置之间进行选择，以帮助进行尺寸设定 |
| 在广泛工况范围内具有预测准确性，取决于 E-NTU 方程和传热系数关联式的适用性 | 在指定工况附近非常准确；远离指定工况时准确性可能降低 |
| 传热计算通过使用 E-NTU 模型考虑温度沿流动路径的变化 | 传热计算通过将流动路径分为三段来近似温度沿流动路径的变化 |

### 传热

模块将气体流和热液体流各分为三个等大小的段。模块计算每个段中流体之间的传热。为简单起见，本节中的方程针对一个段。

如果清除 **Enable wall thermal mass** 复选框，则换热器中的热平衡为

Qseg,G+Qseg,TL=0，

其中：

- *Qseg,G* 是从壁面（即传热表面）到段中气体的热流量。
- *Qseg,TL* 是从壁面到段中热液体的热流量。

如果选中 **Enable wall thermal mass**，则换热器中的热平衡为

Qseg,G+Qseg,TL=−MwallcpwallNdTseg,walldt，

其中：

- *Mwall* 是壁面的质量。
- *cpwall* 是壁面的比热。
- *N* = 3 是段数。
- *Tseg,wall* 是段中壁面的平均温度。
- *t* 是时间。

从壁面到段中气体的热流量为

Qseg,G=UAseg,G(Tseg,wall−Tseg,G)，

其中：

- *UAseg,G* 是段中气体的传热导。
- *Tseg,G* 是段中气体的平均温度。

从壁面到段中热液体的热流量为

Qseg,TL=UAseg,TL(Tseg,wall−Tseg,TL)，

其中：

- *UAseg,TL* 是段中热液体的传热导。
- *Tseg,TL* 是段中液体的平均温度。

模块在传热计算中使用的流体属性是入口值与流体体积中值的平均值。

### 热液体传热关联式

换热器热液体侧的传热导为

UAseg,TL=aTL(Reseg,TL)bTL(Prseg,TL)cTLkseg,TLGTLN，

其中：

- *a*TL、*b*TL 和 *c*TL 是努塞尔数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Re*seg,TL 是段的平均雷诺数。
- *Pr*seg,TL 是段的平均普朗特数。
- *k*seg,TL 是段的平均热导率。
- *G*TL 是换热器热液体侧的几何比例因子。模块计算几何比例因子，使得所有段的总传热量在额定工况下匹配指定的性能。

平均雷诺数为

Reseg,TL=m˙seg,TLDref,TLμseg,TLSref,TL，

其中：

- m˙seg,TL 是通过该段的质量流量。
- *μ*seg,TL 是段的平均动力粘度。
- *D*ref,TL 是任意参考直径。
- *S*ref,TL 是任意参考流通面积。

**注意**

*D*ref,TL 和 *S*ref,TL 项仅出于单位计算目的包含在此方程中，以使 *Re*seg,TL 无量纲化。*D*ref,TL 和 *S*ref,TL 的值是任意的，因为 *G*TL 的计算会覆盖这些值。

### 气体传热关联式

换热器气体侧的传热导为

UAseg,G=aG(Reseg,G)bG(Prseg,G)cGkseg,GGGN，

其中：

- *aG*、*bG* 和 *cG* 是努塞尔数关联式的系数。这些系数是 **Correlation Coefficients** 部分中的模块参数。
- *Reseg,G* 是段的平均雷诺数。
- *Prseg,G* 是段的平均普朗特数。
- *kseg,G* 是段的平均热导率。
- *GG* 是换热器气体侧的几何比例因子。模块计算几何比例因子，使得所有段的总传热量在额定工况下匹配指定的性能。

平均雷诺数为

Reseg,G=m˙seg,GDref,Gμseg,GSref,G，

其中：

- *ṁseg,G* 是通过该段的质量流量。
- *μseg,G* 是段的平均动力粘度。
- *Dref,G* 是任意参考直径。
- *Sref,G* 是任意参考流通面积。

**注意**

*Dref,G* 和 *Sref,G* 项仅出于单位计算目的包含在此方程中，以使 *Reseg,G* 无量纲化。*Dref,G* 和 *Sref,G* 的值是任意的，因为 *GG* 的计算会覆盖这些值。

### 压力损失

热液体侧的压力损失为

pA,TL−pTL=KTL2m˙A,TLm˙2A,TL+m˙2thres,TL2ρavg,TLpB,TL−pTL=KTL2m˙B,TLm˙2B,TL+m˙2thres,TL2ρavg,TL

其中：

- *pA,TL* 和 *pB,TL* 分别是端口 **A1** 和 **B1** 处的压力。
- *pTL* 是模块计算传热时的内部热液体压力。
- m˙A,TL 和 m˙B,TL 分别是流入端口 **A1** 和 **B1** 的质量流量。
- *ρavg,TL* 是所有段的平均热液体密度。
- m˙thres,TL 是压力损失的层流阈值，近似为额定质量流量的 1e-4。模块计算压力损失系数 *KTL*，使得在额定质量流量下 *pA,TL* – *pB,TL* 匹配额定压力损失。

气体侧的压力损失为

pA,G−pG=KG2m˙A,Gm˙2A,G+m˙2thres,G2ρavg,GpB,G−pG=KG2m˙B,Gm˙2B,G+m˙2thres,G2ρavg,G

其中：

- *pA,G* 和 *p*B,G 分别是端口 **A2** 和 **B2** 处的压力。
- *pG* 是模块计算传热时的内部气体压力。
- *ṁA,G* 和 *ṁB,G* 分别是流入端口 **A2** 和 **B2** 的质量流量。
- *ρavg,G* 是所有段的平均气体密度。
- *ṁthres,G* 是压力损失的层流阈值，近似为额定质量流量的 1e-4。模块计算压力损失系数 *KG*，使得在额定质量流量下 *pA,G* – *pB,G* 匹配额定压力损失。

### 热液体质量与能量守恒

整体热液体流动的质量守恒为

(dpTLdt∑segments(∂ρseg,TL∂p)+∑segments(dTseg,TLdt∂ρseg,TL∂T))VTLN=m˙A,TL+m˙B,TL，

其中：

- ∂ρseg,TL∂p 是段中密度对压力的偏导数。
- ∂ρseg,TL∂T 是段中密度对温度的偏导数。
- *T*seg,TL 是段的温度。
- *V*TL 是热液体总体积。

求和遍历所有段。

**注意**

尽管模块将热液体流分为 *N*=3 个段进行传热计算，但假设所有段处于相同的内部压力 *p*TL。因此，*p*TL 在求和之外。

每个段的能量守恒方程为

(dpTLdt∂useg,TL∂p+dTseg,TLdt∂useg,TL∂T)MTLN+useg,TL(m˙seg,in,TL−m˙seg,out,TL)=Φseg,in,TL−Φseg,out,TL+Qseg,TL，

其中：

- ∂useg,TL∂p 是段中比内能对压力的偏导数。
- ∂useg,TL∂T 是段中比内能对温度的偏导数。
- *M*TL 是热液体总质量。
- m˙seg,in,TL 和 m˙seg,out,TL 是流入和流出该段的质量流量。
- *Φ*seg,in,TL 和 *Φ*seg,out,TL 是流入和流出该段的能量流量。

模块假设段之间的质量流量在 m˙A,TL 和 m˙B,TL 的值之间线性分布。

### 气体质量与能量守恒

整体气体流动的质量守恒为

(dpGdt∑segments(∂ρseg,G∂p)+∑segments(dTseg,Gdt∂ρseg,G∂T))VGN=m˙A,G+m˙B,G，

其中：

- ∂ρseg,G∂p 是段中密度对压力的偏导数。
- ∂ρseg,G∂T 是段中密度对温度的偏导数。
- *Tseg,G* 是段的温度。
- *VG* 是气体总体积。

求和遍历所有段。

**注意**

尽管模块将气体流分为 *N*=3 个段进行传热计算，但假设所有段处于相同的内部压力 *pG*。因此，*pG* 在求和之外。

每个段的能量守恒方程为

(dpGdt∂useg,G∂p+dTseg,Gdt∂useg,G∂T)MGN+useg,G(m˙seg,in,G−m˙seg,out,G)=Φseg,in,G−Φseg,out,G+Qseg,G，

其中：

- ∂useg,G∂p 是段中比内能对压力的偏导数。
- ∂useg,G∂T 是段中比内能对温度的偏导数。
- *MG* 是气体总质量。
- *ṁseg,in,G* 和 *ṁseg,out,G* 是流入和流出该段的质量流量。
- *Φseg,in,G* 和 *Φseg,out,G* 是流入和流出该段的能量流量。

模块假设段之间的质量流量在 *ṁA,G* 和 *ṁB,G* 的值之间线性分布。
