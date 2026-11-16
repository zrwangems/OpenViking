---
type: simulink-block
title: 'System-Level Condenser Evaporator (2P-TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Heat Exchangers / Two-Phase Fluid - Thermal Liquid'
documentation_page: 'systemlevelcondenserevaporator2ptl'
documentation_source_path: 'ref/systemlevelcondenserevaporator2ptl.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Condenser Evaporator (2P-TL)

## 端口

### 输出

### **Q1** — 传递至两相流体的热速率，W physical signal

传递至两相流体的热速率，作为 physical signal 返回，单位为 W。端口 **Q1** 和 **Q2** 处的 physical signal 通常数值相等、符号相反。但是，如果选择 **启用壁面热质量**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。

### **Q2** — 传递至热液体的热速率，W physical signal

传递至热液体的热速率，作为 physical signal 返回，单位为 W。端口 **Q1** 和 **Q2** 处的 physical signal 通常数值相等、符号相反。但是，如果选择 **启用壁面热质量**，则这两个信号可能具有不同的值，因为壁面可能会吸收和释放部分传递的热量。
### 守恒

### **A1** — 两相流体端口 two-phase fluid

与两相流体相关的入口或出口端口。

### **B1** — 两相流体端口 two-phase fluid

与两相流体相关的入口或出口端口。

### **A2** — 热液体端口 thermal liquid

与热液体相关的入口或出口端口。

### **B2** — 热液体端口 thermal liquid

与热液体相关的入口或出口端口。

## 参数

### 配置

### **标称工况下的流动布置** — 流路对齐方式 `Counter flow - Two-Phase Fluid 1 flows from A to B, Thermal
  Liquid 2 flows from B to A`（默认） | `Parallel flow - Both fluids flow from A to B` | `Cross flow - Both fluids flow from A to B`

标称工况下换热器两侧之间的流路对齐方式。可用的流动布置包括：

- `Counter flow - Two-Phase Fluid 1 flows from A to B, Thermal
  Liquid 2 flows from B to A` — 流体彼此平行流动，方向相反。
- `Parallel flow - Both fluids flow from A to B` — 流体沿相同方向流动。
- `Cross flow - Both fluids flow from A to B` — 流体彼此垂直流动。

平行流与逆流之间的选择会影响模块确定换热器尺寸的方式。逆流设置最有效，并且满足指定性能所需的尺寸最小。相反，平行流效率最低，并且满足指定性能所需的尺寸最大。

标称工况下的流动方向（从 A 到 B，或从 B 到 A）仅当选择 **将两相流体初始化为标称工况** 或 **将热液体初始化为标称工况** 时影响模型初始化。如果设置不同的初始工况，流动方向可以不同。

在模块确定换热器尺寸后，此设置不会影响模块在仿真期间计算传热的方式。相反，传热取决于仿真期间的流动方向。例如，如果将该参数设置为平行流，但将模型设置为以逆流运行，则即使其余边界条件相同，仿真期间的传热速率也不会匹配指定的性能。

如果将该参数设置为交叉流，则模块会将换热器内部的流路建模为彼此垂直，因此仿真期间的流动方向无关紧要。

### **启用壁面热质量** — 是否启用热质量对传热表面的影响 `off`（默认） | `on`

是否启用热质量对传热表面的影响。选择此参数后，模块会向仿真中引入附加动态，并且需要更长时间达到稳态，但此参数不影响稳态仿真结果。

如果出口处的流体属性（例如流速方向或流体状态）在仿真期间意外振荡，选择此参数可能有助于稳定结果。

### **壁面质量** — 传热表面的质量 `1 kg`（默认） | positive scalar

传热表面的质量。

#### 依赖关系

要启用此参数，请选择 **启用壁面热质量**。

### **壁面比热容** — 传热表面的比热容 `490 J/(K*kg)`（默认） | positive scalar

传热表面的比热容。

#### 依赖关系

要启用此参数，请选择 **启用壁面热质量**。

### **将壁面温度初始化为标称工况** — 初始化壁面温度的选项 `on`（默认） | `off`

将壁面温度初始化为标称工况或指定值的选项。如果选择此参数，模块将根据为两侧流体指定的标称工况计算初始壁面温度。如果清除此参数，可以直接使用 **初始壁面温度** 参数指定初始壁面温度。

#### 依赖关系

要启用此参数，请选择 **启用壁面热质量**。

### **初始壁面温度** — 壁面的初始温度 `293.15 K`（默认） | positive scalar or two-element vector

壁面的初始温度。如果指定标量，模块假定初始壁面温度均匀。如果指定两个元素的向量，则模块假定初始壁面温度在端口 **A1** 和 **A2** 与端口 **B1** 和 **B2** 之间线性变化。第一个元素对应于端口 **A1** 和 **A2** 处的温度，第二个元素对应于端口 **B1** 和 **B2** 处的温度。

#### 依赖关系

要启用此参数，请选择 **启用壁面热质量** 并清除 **将壁面温度初始化为标称工况** 复选框。

### **端口 A1 处的横截面积** — 端口 A1 处的流通面积 `0.01 m^2`（默认） | positive scalar

两相流体端口 **A1** 处的流通面积。

### **端口 B1 处的横截面积** — 端口 B1 处的流通面积 `0.01 m^2`（默认） | positive scalar

两相流体端口 **B1** 处的流通面积。

### **端口 A2 处的横截面积** — 端口 A2 处的流通面积 `0.01 m^2`（默认） | positive scalar

热液体端口 **A2** 处的流通面积。

### **端口 B2 处的横截面积** — 端口 B2 处垂直于流动方向的面积 `0.01 m^2`（默认） | positive scalar

热液体端口 **B2** 处的流通面积。

### 两相流体 1

### **标称工况** — 选择标称工况对应于冷凝器还是蒸发器 `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal Liquid 2`（默认） | `Evaporator - heat transfer from Thermal Liquid 2 to Two-Phase Fluid 1`

标称工况：

- `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal
  Liquid 2` — 两相流体被冷却，热液体被加热。
- `Evaporator - heat transfer from Thermal Liquid 2 to Two-Phase
  Fluid 1` — 热液体被冷却，两相流体被加热。

此设置仅与标称工况参数相关。这并不意味着传热在仿真期间只能沿指定方向发生。

### **标称质量流量** — 标称工况下两相端口之间的质量流量 `0.001 kg/s`（默认） | positive scalar

标称工况下从端口 **A1** 到端口 **B1** 的质量流量。

### **标称压降** — 标称工况下两相端口之间的压降 `0.01 MPa`（默认） | positive scalar

标称工况下从端口 **A1** 到端口 **B1** 的压降。

### **压力指定** — 选择压力指定方法 `Inlet pressure`（默认） | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

选择压力指定方法：

- `Inlet pressure` — 指定标称入口压力。
- `Saturation pressure at specified condensing
  temperature` — 指定标称冷凝温度。如果将 **标称工况** 设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal Liquid
  2`，则此选项可用。
- `Saturation pressure at specified evaporating
  temperature` — 指定标称蒸发温度。如果将 **标称工况** 设置为 `Evaporator - heat transfer from Thermal Liquid 2 to Two-Phase Fluid
  1`，则此选项可用。

### **标称入口压力** — 两相流体侧入口处的压力 `1 MPa`（默认） | positive scalar

标称工况下换热器两相流体入口处的压力。

#### 依赖关系

要启用此参数，请将 **压力指定** 设置为 `Inlet pressure`。

### **标称冷凝温度** — 使用标称冷凝温度指定压力 `313.15 K`（默认） | positive scalar

标称工况下换热器两相流体出口处的液体饱和温度。换热器中的压力为对应的饱和压力。标称冷凝温度必须小于临界温度。

#### 依赖关系

要启用此参数，请将 **标称工况** 设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal Liquid
2`，并将 **压力指定** 设置为 `Saturation pressure at specified condensing
  temperature`。

### **标称蒸发温度** — 使用标称蒸发温度指定压力 `243.15 K`（默认） | positive scalar

标称工况下换热器两相流体出口处的蒸气饱和温度。换热器中的压力为对应的饱和压力。标称蒸发温度必须小于临界温度。

#### 依赖关系

要启用此参数，请将 **标称工况** 设置为 `Evaporator - heat transfer from Thermal Liquid 2 to Two-Phase Fluid
1`，并将 **压力指定** 设置为 `Saturation pressure at specified evaporating
  temperature`。

### **入口条件指定** — 选择用于描述两相流体入口条件的量 `Specific enthalpy`（默认） | `Temperature` | `Vapor quality`

用于描述标称工况下流体入口条件的量：温度、比焓或蒸气干度。

### **标称入口比焓** — 两相流体侧入口处的比焓 `440 kJ/kg`（默认） | positive scalar

标称工况下换热器两相流体入口处的比焓。

#### 依赖关系

要启用此参数，请将 **入口条件指定** 设置为 `Specific enthalpy`。

### **标称入口温度** — 两相流体侧入口处的温度 `313.15 K`（默认） | positive scalar

标称工况下换热器两相流体入口处的温度。

#### 依赖关系

要启用此参数，请将 **入口条件指定** 设置为 `Temperature`。

### **标称入口蒸气干度** — 两相流体侧入口处的蒸气干度 `1`（默认） | positive scalar

标称工况下换热器两相流体入口处的蒸气干度，定义为液-气混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **入口条件指定** 设置为 `Vapor quality`。

### **传热能力指定** — 如何指定两相流体的传热能力 `Rate of heat transfer`（默认） | `Outlet condition`

是否直接通过传热速率或间接通过出口条件来指定标称工况下换热器针对两相流体的性能。

### **标称传热速率** — 传热速率 `0.1 kW`（默认） | positive scalar

传热速率。**标称工况** 参数确定热量传入和传出的网络：

- 如果 **标称工况** 为 `Condenser
  - heat transfer from Two-Phase Fluid 1 to Thermal Liquid 2`，则此参数是标称工况下从两相流体到热液体的传热速率。
- 如果 **标称工况** 为 `Evaporator
  - heat transfer from Thermal Liquid 2 to Two-Phase Fluid 1`，则此参数是标称工况下从热液体到两相流体的传热速率。

#### 依赖关系

要启用此参数，请将 **传热能力指定** 设置为 `Rate of heat
transfer`。

### **出口条件指定** — 选择用于出口条件指定的量 `Specific enthalpy`（默认） | `Subcooling` | `Superheating` | `Vapor quality`

选择用于出口条件指定的量：

- `Specific enthalpy` — 指定标称比焓。
- `Subcooling` — 指定标称过冷度。如果将 **标称工况** 设置为 `Condenser - heat transfer from Two-Phase Fluid 1 to Thermal Liquid
  2`，则此选项可用。
- `Superheating` — 指定标称过热度。如果将 **标称工况** 设置为 `Evaporator - heat transfer from Thermal
  Liquid 2 to Two-Phase Fluid 1`，则此选项可用。
- `Vapor quality` — 指定标称蒸气干度。

#### 依赖关系

要启用此参数，请将 **传热能力指定** 设置为 `Outlet condition`。

### **标称出口比焓** — 两相流体侧出口处的比焓 `250 kJ/kg`（默认） | positive scalar | two-element vector

标称工况下换热器两相流体出口处的比焓。

#### 依赖关系

要启用此参数，请将 **出口条件指定** 设置为 `Specific enthalpy`。

### **标称过冷度** — 两相流体侧出口处低于液体饱和温度的温度差 `5 deltaK`（默认） | positive scalar

标称工况下换热器两相流体出口处低于液体饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **出口条件指定** 设置为 `Subcooling`。

### **标称过热度** — 两相流体侧出口处高于蒸气饱和温度的温度差 `5 deltaK`（默认） | positive scalar

标称工况下换热器两相流体出口处高于蒸气饱和温度的温度差。

#### 依赖关系

要启用此参数，请将 **出口条件指定** 设置为 `Superheating`。

### **标称出口蒸气干度** — 两相流体侧出口处的蒸气质量分数 `0`（默认） | scalar in the range [0,1]

标称工况下换热器两相流体出口处的两相流体蒸气干度，定义为液-气混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **出口条件指定** 设置为 `Vapor quality`。

### **两相流体体积** — 两相流体的总体积 `0.001 m^3`（默认） | positive scalar

换热器内部两相流体的总体积。

### **将两相流体初始化为标称工况** — 初始化两相流体的选项 `on`（默认） | `off`

将两相流体初始化为标称工况或指定值的选项。如果选择此参数，模块会将两相流体初始化为标称工况。如果清除此复选框，则可以使用其他参数直接指定初始条件。

### **初始流体能量规格** — 两相流体的初始状态 `Specific enthalpy` (默认) | `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

用于描述流体初始状态的量。

**初始流体能量规格**参数的值会限制两相流体可用的初始状态。当**初始流体能量规格**为：

- `Temperature` — 指定一个为过冷液体或过热蒸气的初始状态。不能指定液-蒸气混合物，因为温度在液-蒸气混合物区域保持不变。
- `Vapor quality` — 指定一个为液-蒸气混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域中液体质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Vapor void fraction` — 指定一个为液-蒸气混合物的初始状态。不能指定过冷液体或过热蒸气，因为在整个区域中液体质量分数分别为 0 和 1。此外，模块将压力限制在临界压力以下。
- `Specific enthalpy` — 指定流体的比焓。模块不限制初始状态。
- `Specific internal energy` — 指定流体的比内能。模块不限制初始状态。

#### 依赖关系

要启用此参数，请清除 **将两相流体初始化为标称操作条件** 复选框。

### **初始两相流体压力** — 仿真开始时的流体压力 `0.101325 MPa` (默认) | positive scalar

仿真开始时的两相流体压力。

#### 依赖关系

要启用此参数，请清除 **将两相流体初始化为标称操作条件** 复选框。

### **初始两相流体比焓** — 仿真开始时单位质量的焓 `1500 kJ/kg` (默认) | positive scalar | two-element vector

仿真开始时的两相流体比焓。如果该值是 scalar，则初始比焓假定为均匀。如果该值是 two-element vector，则初始比焓假定在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **将两相流体初始化为标称操作条件** 复选框并将 **初始流体能量规格** 设置为 `Specific enthalpy`。

### **初始两相流体温度** — 仿真开始时的温度 `293.15 K` (默认) | positive scalar | two-element vector

仿真开始时的两相流体温度。如果该值是 scalar，则初始温度假定为均匀。如果该值是 two-element vector，则初始温度假定在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **将两相流体初始化为标称操作条件** 复选框并将 **初始流体能量规格** 设置为 `Temperature`。

### **初始两相流体蒸气干度** — 仿真开始时的蒸气质量分数 `0.5` (默认) | scalar in the range [0,1] | two-element vector

仿真开始时的两相流体蒸气干度，定义为液-蒸气混合物中蒸气的质量分数。如果该值是 scalar，则初始蒸气干度假定为均匀。如果该值是 two-element vector，则初始蒸气干度假定在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除 **将两相流体初始化为标称操作条件** 复选框并将 **初始流体能量规格** 设置为 `Vapor quality`。

### **初始两相流体蒸气空泡份额** — 仿真开始时的蒸气体积分数 `0.5` (默认) | scalar in the range [0,1] | two-element vector

仿真开始时的两相流体蒸气空泡份额，定义为液-蒸气混合物中蒸气的体积分数。如果该值是 scalar，则初始蒸气空泡份额假定为均匀。如果该值是 two-element vector，则初始蒸气空泡份额假定在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

如果使用此选项，初始压力不能高于临界压力。

#### 依赖关系

要启用此参数，请清除 **将两相流体初始化为标称操作条件** 复选框并将 **初始流体能量规格** 设置为 `Vapor void fraction`。

### **初始两相流体比内能** — 仿真开始时单位质量的内能 `1500 kJ/kg` (默认) | positive scalar | two-element vector

仿真开始时的两相流体比内能。如果该值是 scalar，则初始比内能假定为均匀。如果该值是 two-element vector，则初始比内能假定在端口 **A1** 和 **B1** 之间线性变化，第一个元素对应端口 **A1**，第二个元素对应端口 **B1**。

#### 依赖关系

要启用此参数，请清除 **将两相流体初始化为标称操作条件** 复选框并将 **初始流体能量规格** 设置为 `Specific internal energy`。

### 热液体 2

### **标称质量流量** — 标称操作条件下热液体端口之间的质量流量 `0.1 kg/s` (默认) | positive scalar

标称操作条件下从端口 **A2** 到端口 **B2** 的质量流量。

### **标称压降** — 标称操作条件下热液体端口之间的压降 `0.01 MPa` (默认) | positive scalar

标称操作条件下从端口 **A2** 到端口 **B2** 的压降。

### **标称入口压力** — 热液体侧入口处的压力 `0.101325 MPa` (默认) | positive scalar

标称操作条件下换热器热液体入口处的压力。

### **标称入口温度** — 热液体侧入口处的温度 `293.15 K` (默认) | positive scalar

标称操作条件下换热器热液体入口处的温度。

### **热液体体积** — 换热器中热液体的总体积 `0.001 m^3` (默认) | positive scalar

换热器中热液体的总体积。

### **将热液体初始化为标称操作条件** — 用于初始化热液体的选项 `on` (默认) | `off`

将热液体初始化为标称操作条件或指定值的选项。如果选择此参数，模块将热液体初始化为标称操作条件。如果清除此复选框，可以使用其他参数直接指定初始条件。

### **初始热液体压力** — 仿真开始时的热液体压力 `0.101325 MPa` (默认) | positive scalar

仿真开始时的热液体压力。

#### 依赖关系

要启用此参数，请清除 **将热液体初始化为标称操作条件** 复选框。

### **初始热液体温度** — 仿真开始时的热液体温度 `293.15 K` (默认) | positive scalar | two-element vector

仿真开始时的热液体温度。如果该值是 scalar，则初始温度假定为均匀。如果该值是 two-element vector，则初始温度假定在端口 **A2** 和 **B2** 之间线性变化，第一个元素对应端口 **A2**，第二个元素对应端口 **B2**。

#### 依赖关系

要启用此参数，请清除 **将热液体初始化为标称操作条件** 复选框。

### 相关系数

### **两相流体液体的 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过冷液体的相关系数 `0.023` (默认) | positive scalar

两相流体中过冷液体的努塞尔数与雷诺数和普朗特数关系式中的比例常数。默认值基于 Colburn 方程。

### **两相流体混合物的 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中液-蒸气混合物的相关系数 `0.005` (默认) | positive scalar

两相流体中液-蒸气混合物的努塞尔数与雷诺数和普朗特数关系式中的比例常数。默认值基于 Cavallini 和 Zecchin 关联式。

### **两相流体蒸气的 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过热蒸气的相关系数 `0.023` (默认) | positive scalar

两相流体中过热蒸气的努塞尔数与雷诺数和普朗特数关系式中的比例常数。默认值基于 Colburn 方程。

### **两相流体的 Nu = a\*Re^b\*Pr^c 中的 b** — 两相流体关联式中的雷诺数指数 `0.8` (默认) | positive scalar

两相流体的努塞尔数与雷诺数和普朗特数关系式中的雷诺数指数。同一值适用于过冷液体、液-蒸气混合物和过热蒸气。

### **两相流体的 Nu = a\*Re^b\*Pr^c 中的 c** — 两相流体关联式中的普朗特数指数 `0.33` (默认) | positive scalar

两相流体的努塞尔数与雷诺数和普朗特数关系式中的普朗特数指数。同一值适用于过冷液体、液-蒸气混合物和过热蒸气。

### **热液体的 Nu = a\*Re^b\*Pr^c 中的 a** — 热液体的相关系数 `0.005` (默认) | positive scalar

热液体的努塞尔数与雷诺数和普朗特数关系式中的比例常数。默认值基于 Colburn 方程。

### **热液体的 Nu = a\*Re^b\*Pr^c 中的 b** — 热液体关联式中的雷诺数指数 `0.8` (默认) | positive scalar

热液体的努塞尔数与雷诺数和普朗特数关系式中的雷诺数指数。默认值基于 Colburn 方程。

### **热液体的 Nu = a\*Re^b\*Pr^c 中的 c** — 热液体关联式中的普朗特数指数 `0.33` (默认) | positive scalar

热液体的努塞尔数与雷诺数和普朗特数关系式中的普朗特数指数。默认值基于 Colburn 方程。

## 所属库

Simscape / Fluids / Heat Exchangers / Two-Phase Fluid - Thermal Liquid

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2023b：指定初始壁温

如果选择 **启用壁热质量** 并清除 **将壁温初始化为标称操作条件** 复选框，可以使用新的 **初始壁温** 参数直接指定初始条件。

## 描述

基于两相流体与热液体网络之间性能数据的换热器

System-Level Condenser Evaporator (2P-TL) 模块对两相流体网络与热液体网络之间的换热器建模。

该模块可在制冷系统中充当冷凝器或蒸发器，具体取决于传热方向。该模块使用换热器数据表中的性能数据，而不是换热器的详细几何结构。您可以在设计迭代期间调整换热器的尺寸和性能，或对具有不常见几何结构的换热器建模。还可以在早期设计阶段使用此模块对具有一定性能水平的换热器建模，此时尚无详细几何数据。

您通过标称操作条件对该模块进行参数化。换热器按稳态下标称操作条件下匹配指定性能来确定尺寸。

Two-Phase Fluid 1 侧根据沿流动路径的焓变近似表示液体区、混合物区和蒸气区。

该模块与 Condenser Evaporator (TL-2P) 模块类似，但使用不同的参数化模型。下表比较这两个模块：

| Condenser Evaporator (TL-2P) | System-Level Condenser Evaporator (2P-TL) |
| --- | --- |
| 模块参数基于换热器几何结构 | 模块参数基于性能和操作条件 |
| 换热器几何结构可能受可用几何参数选项限制 | 模型独立于具体换热器几何结构 |
| 可以通过调整几何参数（例如翅片尺寸和管长）来调整模块以满足不同性能要求 | 可以通过直接指定所需的热流量和质量流量来调整模块以满足不同性能要求 |
| 可以在平行流、逆流或交叉流配置之间选择 | 可以在标称操作条件下在平行流、逆流或交叉流布置之间选择，以帮助确定尺寸 |
| 在广泛操作条件下具有预测准确性，但受 E-NTU 方程和传热系数关联式适用性的约束 | 在指定操作条件附近结果非常准确；远离指定操作条件时准确性可能降低 |
| 传热计算通过使用 E-NTU 模型考虑沿流动路径的温度变化 | 传热计算通过将流动路径分成三段来近似表示沿流动路径的温度变化 |
| 考虑过冷液体、液-蒸气混合物和过热蒸气的不同流体属性和传热系数 | 考虑过冷液体、液-蒸气混合物和过热蒸气的不同流体属性和传热系数 |
| 根据几何结构跟踪过冷液体、液-蒸气混合物和过热蒸气区域的可变区域长度分数 | 使用基于入口与出口之间焓差的加权因子近似表示过冷液体、液-蒸气混合物和过热蒸气区域的影响 |

### 传热

该模块将两相流体流和热液体流分别分成三段大小相等的段，并计算每个段内流体之间的传热。为简单起见，本节中的方程针对一个段。

如果清除 **启用壁面热质量** 复选框，则换热器中的热平衡为

Qseg,2P+Qseg,TL=0,

其中：

- *Q*seg,2P 是从壁面（即传热表面）到该段内两相流体的热流率。
- *Q*seg,TL 是从壁面到该段内热液体的热流率。

如果选中 **启用壁面热质量**，则换热器中的热平衡为

Qseg,2P+Qseg,TL=−MwallcpwallNdTseg,walldt,

其中：

- *M*wall 是壁面的质量。
- *c*pwall 是壁面的比热容。
- *N* = 3 是段的数量。
- *T*seg,wall 是该段的平均壁面温度。
- *t* 是时间。

从壁面到该段内两相流体的热流率为

Qseg,2P=UAseg,2P(Tseg,wall−Tseg,2P),

其中：

- *UA*seg,2P 是该段内两相流体的加权平均传热导。
- *T*seg,2P 是该段内两相流体的加权平均流体温度。

从壁面到该段内热液体的热流率为

Qseg,TL=UAseg,TL(Tseg,wall−Tseg,TL),

其中：

- *UA*seg,TL 是该段内热液体的传热导。
- *T*seg,TL 是该段内的平均液体温度。

模块在传热计算中使用的流体属性是入口处的值与流体体积中的值之间的平均值。

### 两相流体传热关联式

如果该段为过冷液体，则传热导为

UAseg,L,2P=aL,2P(Reseg,L,2P)b2P(Prseg,L,2P)c2Pkseg,L,2PG2PN,

其中：

- *a*L,2P、*b*2P 和 *c*2P 是 Nusselt 数关联式的系数。这些系数是 **关联系数** 部分中的模块参数。
- *Re*seg,L,2P 是该段的平均液体 Reynolds 数。
- *Pr*seg,L,2P 是该段的平均液体 Prandtl 数。
- *k*seg,L,2P 是该段的平均液体热导率。
- *G*2P 是换热器两相流体侧的几何尺度因子。模块计算几何尺度因子，以使所有段上的总传热在标称工况下与指定性能匹配。

平均液体 Reynolds 数为

Reseg,L,2P=m˙seg,2PDref,2Pμseg,L,2PSref,2P,

其中：

- m˙seg,2P 是通过该段的质量流量。
- *μ*seg,L,2P 是该段的平均液体动力粘度。
- *D*ref,2P 是任意参考直径。
- *S*ref,2P 是任意参考流通面积。

**注意**

方程中包含 *D*ref,2P 和 *S*ref,2P 项仅用于单位计算，以使 *Re*seg,L,2P 无量纲。*D*ref,2P 和 *S*ref,2P 的值是任意的，因为 *G*2P 的计算会覆盖这些值。

类似地，如果该段为过热蒸气，则传热导为

UAseg,V,2P=aV,2P(Reseg,V,2P)b2P(Prseg,V,2P)c2Pkseg,V,2PG2PN,

其中：

- *a*V,2P、*b*2P 和 *c*2P 是 Nusselt 数关联式的系数。这些系数作为模块参数出现在 **关联系数** 部分中。
- *Re*seg,V,2P 是该段的平均蒸气 Reynolds 数。
- *Pr*seg,V,2P 是该段的平均蒸气 Prandtl 数。
- *k*seg,V,2P 是该段的平均蒸气热导率。

平均蒸气 Reynolds 数为

Reseg,V,2P=m˙seg,2PDref,2Pμseg,V,2PSref,2P,

其中 *μ*seg,V,2P 是该段的平均蒸气动力粘度。

如果该段为液-蒸气混合物，则传热导为

UAseg,M,2P=aM,2P(Reseg,SL,2P)b2PCZ(Prseg,SL,2P)c2Pkseg,SL,2PG2PN,

其中：

- *a*M,2P、*b*2P 和 *c*2P 是 Nusselt 数关联式的系数。这些系数作为模块参数出现在 **关联系数** 部分中。
- *Re*seg,SL,2P 是该段的饱和液体 Reynolds 数。
- *Pr*seg,SL,2P 是该段的饱和液体 Prandtl 数。
- *k*seg,SL,2P 是该段的饱和液体热导率。
- *CZ* 是 Cavallini 和 Zecchin 项。

饱和液体 Reynolds 数为

Reseg,SL,2P=m˙seg,2PDref,2Pμseg,SL,2PSref,2P,

其中 *μ*seg,SL,2P 是该段的饱和液体动力粘度。

Cavallini 和 Zecchin 项为

CZ=((νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P+1))1+b2P−((νseg,SV,2Pνseg,SL,2P−1)(xseg,in,2P+1))1+b2P(1+b2P)(νseg,SV,2Pνseg,SL,2P−1)(xseg,out,2P−xseg,in,2P),

其中：

- *ν*seg,SL,2P 是该段的饱和液体比体积。
- *ν*seg,SV,2P 是该段的饱和蒸气比体积。
- *x*seg,in,2P 是该段入口处的蒸气干度。
- *x*seg,out,2P 是该段出口处的蒸气干度。

该表达式基于 Cavallini 和 Zecchin [5] 的工作，其中推导了局部蒸气干度 *x* 下的传热系数关联式。通过将 Cavallini 和 Zecchin 的关联式在从 *x*seg,in,2P 到 *x*seg,out,2P 的段上平均，得到液-蒸气混合物的方程。

### 两相流体加权平均

通过一个段的两相流体流动可能不能完全表示为过冷液体、过热蒸气或液-蒸气混合物中的一种。相反，每个段可能由这些的组合组成。模块通过基于该段上的比焓变化以及饱和液体和蒸气比焓来计算加权因子（*w*L、*w*V 和 *w*M），从而近似此情况。模块假设该段上的比焓从入口到出口分段线性变化，转折点对应于液体和蒸气的饱和边界。传热系数较大的区域比传热系数较小的区域具有更陡的斜率。

wL=ΔLΔL+ΔM+ΔVwV=ΔVΔL+ΔM+ΔVwM=1−wL−wV

ΔL=|min(hseg,out,2P,hseg,SL,2P)−min(hseg,in,2P,hseg,SL,2P)|⋅UAseg,M,2P⋅UAseg,V,2PΔM=|min(max(hseg,out,2P,hseg,SL,2P),hseg,SV,2P)−min(max(hseg,in,2P,hseg,SL,2P),hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,V,2PΔV=|max(hseg,out,2P,hseg,SV,2P)−max(hseg,in,2P,hseg,SV,2P)|⋅UAseg,L,2P⋅UAseg,M,2P

其中：

- *h*seg,in,2P 是该段入口处的比焓。
- *h*seg,out,2P 是该段出口处的比焓。
- *h*seg,SL,2P 是该段的饱和液体比焓。
- *h*seg,SV,2P 是该段的饱和蒸气比焓。

因此，该段的两相流体加权平均传热导为

UAseg,2P=wL(UAseg,L,2P)+wV(UAseg,V,2P)+wM(UAseg,M,2P).

该段的加权平均流体温度为

Tseg,2P=wL(UAseg,L,2P)Tseg,L,2P+wV(UAseg,V,2P)Tseg,V,2P+wM(UAseg,M,2P)Tseg,M,2PUAseg,2P,

其中：

- *T*seg,L,2P 是该段的平均液体温度。
- *T*seg,V,2P 是该段的平均蒸气温度。
- *T*seg,M,2P 是该段的平均混合物温度，即饱和液体温度。

### 热液体传热关联式

传热导为

UAseg,TL=aTL(Reseg,TL)bTL(Prseg,TL)cTLkseg,TLGTLN,

其中：

- *a*TL、*b*TL 和 *c*TL 是 Nusselt 数关联式的系数。这些系数是 **关联系数** 部分中的模块参数。
- *Re*seg,TL 是该段的平均 Reynolds 数。
- *Pr*seg,TL 是该段的平均 Prandtl 数。
- *k*seg,TL 是该段的平均热导率。
- *G*TL 是换热器热液体侧的几何尺度因子。模块计算几何尺度因子，以使所有段上的总传热在标称工况下与指定性能匹配。

平均 Reynolds 数为

Reseg,TL=m˙seg,TLDref,TLμseg,TLSref,TL,

其中：

- m˙seg,TL 是通过该段的质量流量。
- *μ*seg,TL 是该段的平均动力粘度。
- *D*ref,TL 是任意参考直径。
- *S*ref,TL 是任意参考流通面积。

**注意**

方程中包含 *D*ref,TL 和 *S*ref,TL 项仅用于单位计算，以使 *Re*seg,TL 无量纲。*D*ref,TL 和 *S*ref,TL 的值是任意的，因为 *G*TL 的计算会覆盖这些值。

### 压力损失

两相流体侧的压力损失为

pA,2P−p2P=K2P2m˙A,2Pm˙2A,2P+m˙2thres,2P2ρavg,2PpB,2P−p2P=K2P2m˙B,2Pm˙2B,2P+m˙2thres,2P2ρavg,2P

其中：

- *p*A,2P 和 *p*B,2P 分别是端口 **A1** 和 **B1** 处的压力。
- *p*2P 是计算传热时的内部两相流体压力。
- m˙A,2P 和 m˙B,2P 分别是流入端口 **A1** 和 **B1** 的质量流量。
- *ρ*avg,2P 是所有段上的平均两相流体密度。
- m˙thres,2P 是压力损失的层流阈值，近似为标称质量流量的 1e-4。模块计算压力损失系数 *K*2P，使 *p*A,2P – *p*B,2P 在标称质量流量下与标称压力损失匹配。

热液体侧的压力损失为

pA,TL−pTL=KTL2m˙A,TLm˙2A,TL+m˙2thres,TL2ρavg,TLpB,TL−pTL=KTL2m˙B,TLm˙2B,TL+m˙2thres,TL2ρavg,TL

其中：

- *p*A,TL 和 *p*B,TL 分别是端口 **A2** 和 **B2** 处的压力。
- *p*TL 是计算传热时的内部热液体压力。
- m˙A,TL 和 m˙B,TL 分别是流入端口 **A2** 和 **B2** 的质量流量。
- *ρ*avg,TL 是所有段上的平均热液体密度。
- m˙thres,TL 是压力损失的层流阈值，近似为标称质量流量的 1e-4。模块计算压力损失系数 *K*TL，使 *p*A,TL – *p*B,TL 在标称质量流量下与标称压力损失匹配。

### 两相流体质量与能量守恒

整体两相流体流动的质量守恒方程为

(dp2Pdt∑segments(∂ρseg,2P∂p)+∑segments(duseg,2Pdt∂ρseg,2P∂u))V2PN=m˙A,2P+m˙B,2P,

其中：

- ∂ρseg,2P∂p 是该段的密度对压力的偏导数。
- ∂ρseg,2P∂u 是该段的密度对比内能的偏导数。
- *u*seg,2P 是该段的比内能。
- *V*2P 是两相流体的总体积。

求和针对所有段。

**注意**

尽管模块为了传热计算将两相流体流分成 *N*=3 个段，但它假设所有段都处于相同的内部压力 *p*2P。因此，*p*2P 在求和之外。

每个段的能量守恒方程为

duseg,2PdtM2PN+useg,2P(m˙seg,in,2P−m˙seg,out,2P)=Φseg,in,2P−Φseg,out,2P+Qseg,2P,

其中：

- *M*2P 是两相流体的总质量。
- m˙seg,in,2P 和 m˙seg,out,2P 是流入和流出该段的质量流量。
- *Φ*seg,in,2p 和 *Φ*seg,out,2p 是流入和流出该段的能量流率。

模块假设段之间的质量流量在 m˙A,2P 和 m˙B,2P 的值之间线性分布。

### 热液体质量与能量守恒

整体热液体流动的质量守恒为

(dpTLdt∑segments(∂ρseg,TL∂p)+∑segments(dTseg,TLdt∂ρseg,TL∂T))VTLN=m˙A,TL+m˙B,TL,

其中：

- ∂ρseg,TL∂p 是该段的密度对压力的偏导数。
- ∂ρseg,TL∂T 是该段的密度对温度的偏导数。
- *T*seg,TL 是该段的温度。
- *V*TL 是热液体的总体积。

求和针对所有段。

**注意**

尽管模块为了传热计算将热液体流分成 *N*=3 个段，但它假设所有段都处于相同的内部压力 *pTL*。因此，*pTL* 在求和之外。

每个段的能量守恒方程为

(dpTLdt∂useg,TL∂p+dTseg,TLdt∂useg,TL∂T)MTLN+useg,TL(m˙seg,in,TL−m˙seg,out,TL)=Φseg,in,TL−Φseg,out,TL+Qseg,TL,

其中：

- ∂useg,TL∂p 是该段的比内能对压力的偏导数。
- ∂useg,TL∂T 是该段的比内能对温度的偏导数。
- *M*TL 是热液体的总质量。
- m˙seg,in,TL 和 m˙seg,out,TL 是流入和流出该段的质量流量。
- *Φ*seg,in,TL 和 *Φ*seg,out,TL 是流入和流出该段的能量流率。

模块假设段之间的质量流量在 m˙A,TL 和 m˙B,TL 的值之间线性分布。
