---
type: simulink-block
title: 'System-Level Refrigeration Cycle (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Thermodynamic Cycles'
documentation_page: 'systemlevelrefrigerationcycle2p'
documentation_source_path: 'ref/systemlevelrefrigerationcycle2p.html'
language: zh-CN
chinese_source: worker-translation
---

# System-Level Refrigeration Cycle (2P)

## 端口

### 输入

### **S** — 用于操作压缩机的信号，无量纲物理信号

用于操作压缩机的物理信号输入。值 `0` 表示压缩机
关闭。值 `1` 表示压缩机以额定容量运行。
### 守恒

### **F** — 制冷剂属性两相流体

与制冷剂属性关联的两相流体守恒端口。将两相流体属性
(2P) 或两相流体预定义
属性 (2P) 模块连接到此端口。不要将
任何其他两相流体模块连接到端口 **F**，因为
此端口用作绝对参考。

### **Ac** — 冷凝器外部流体入口 气体 | 湿空气 | 热液体 | 两相流体

与冷凝器外部流体入口关联的气体、湿空气、热液体或两相流体守恒端口。
该模块假设冷凝器
外部流体从端口 **Ac** 流向端口
**Bc**。**冷凝器传热的外部流体**
参数控制端口流体。

### **Bc** — 冷凝器外部流体出口 气体 | 湿空气 | 热液体 | 两相流体

与冷凝器外部流体出口关联的气体、湿空气、热液体或两相流体守恒端口。
该模块假设冷凝器
外部流体从端口 **Ac** 流向端口
**Bc**。**冷凝器传热的外部流体**
参数控制端口流体。

### **Ae** — 蒸发器外部流体入口 气体 | 湿空气 | 热液体 | 两相流体

与蒸发器外部流体入口关联的气体、湿空气、热液体或两相流体守恒端口。
该模块假设蒸发器
外部流体从端口 **Ae** 流向端口
**Be**。**蒸发器传热的外部流体**
参数控制端口流体。

### **Be** — 蒸发器外部流体出口 气体 | 湿空气 | 热液体 | 两相流体

与蒸发器外部流体出口关联的气体、湿空气、热液体或两相流体守恒端口。
该模块假设蒸发器
外部流体从端口 **Ae** 流向端口
**Be**。**蒸发器传热的外部流体**
参数控制端口流体。
### 输出

### **Qc** — 冷凝器中排出的热量，W 物理信号

物理信号输出端口，测量制冷剂在
冷凝器中排出的热量，单位为 W。

### **Qe** — 蒸发器中吸收的热量，W 物理信号

物理信号输出端口，测量制冷剂在
蒸发器中吸收的热量，单位为 W。

### **Pwr** — 压缩机消耗的机械功率，W 物理信号

物理信号输出端口，测量压缩机消耗的
机械功率，单位为 W。

### **W** — 蒸发器中的冷凝速率，kg/s 物理信号

物理信号输出端口，测量蒸发器
外部流体中的冷凝速率，单位为 kg/s，如果 **蒸发器
传热的外部流体** 参数为 `Moist
air`。如果 **蒸发器传热的外部流体**
参数不是湿空气，此端口
输出 `0`。此端口的值不包括
作为水滴夹带的冷凝部分。

## 参数

### 制冷循环

### **容量规格** — 指定系统大小的方法 `Cooling load`（默认）| `Heating load` | `Refrigerant mass flow rate`

指定系统大小的方法。您可以指定
冷却负荷、加热负荷或制冷剂质量流量。

### **额定冷凝器传热** — 冷凝器中的传热速率 `15` `kW`（默认）| 正标量

在冷凝器中从制冷剂到外部流体的
传热速率。

#### 依赖关系

要启用此参数，请将 **容量
规格** 设置为 `Heating
load`。

### **额定蒸发器传热** — 蒸发器中的传热速率 `15` `kW`（默认）| 正标量

在蒸发器中从外部流体到制冷剂的
传热速率。

#### 依赖关系

要启用此参数，请将 **容量
规格** 设置为 `Cooling
load`。

### **额定质量流量** — 制冷剂质量流量 `0.005` `kg/s`（默认）| 正标量

通过循环的制冷剂质量流量。

#### 依赖关系

要启用此参数，请将 **容量
规格** 设置为 `Refrigerant mass flow
rate`。

### **压力规格** — 指定冷凝器和蒸发器压力的方法 `Specified pressure`（默认）| `Pressure at specified saturation temperature`

提供冷凝器和蒸发器压力的方法。选择
是直接提供压力还是提供相应的
饱和温度。

### **额定冷凝器压力** — 冷凝器中的制冷剂压力 `1` `MPa`（默认）| 正标量

冷凝器中制冷剂的压力。

#### 依赖关系

要启用此参数，请将 **压力
规格** 设置为 `Specified
pressure`。

### **额定蒸发器压力** — 蒸发器中的制冷剂压力 `0.1` `MPa`（默认）| 正标量

蒸发器中制冷剂的压力。

#### 依赖关系

要启用此参数，请将 **压力
规格** 设置为 `Specified
pressure`。

### **额定冷凝（饱和）温度** — 冷凝器制冷剂饱和温度 `333.15` `K`（默认）| 正标量

冷凝器中制冷剂的饱和温度。

#### 依赖关系

要启用此参数，请将 **压力
规格** 设置为 `Pressure at specified
saturation temperature`。

### **额定蒸发（饱和）温度** — 蒸发器制冷剂饱和温度 `273.15` `K`（默认）| 正标量

蒸发器中制冷剂的饱和温度。

#### 依赖关系

要启用此参数，请将 **压力
规格** 设置为 `Pressure at specified
saturation temperature`。

### **额定冷凝器过冷度** — 运行冷凝器出口温度差 `5` `deltaK`（默认）| 正标量

冷凝器出口处低于饱和温度的温度度数。

### **额定（静态 + 开启）蒸发器过热度** — 运行蒸发器出口温度差 `10` `deltaK`（默认）| 正标量

蒸发器出口处高于饱和温度的温度度数。膨胀阀调整其阀面积以尝试维持
此过热度。

### **静态（最小）蒸发器过热度** — 蒸发器出口处的最小允许温度差 `5` `deltaK`（默认）| 正标量

关闭膨胀阀的过热度阈值。

### **性能规格** — 指定制冷循环效率的方法 `Coefficient of performance for cooling`（默认）| `Coefficient of performance for heating` | `Compressor isentropic efficiency`

指定制冷循环效率的方法。根据循环的
制热性能系数、制冷性能系数或压缩机
效率进行选择。

### **额定工况下的性能系数** — 制冷或制热与压缩机消耗功率的比值 `3`（默认）| 正标量

制冷循环的有用制冷或制热与
压缩机消耗功率的比值。

#### 依赖关系

要启用此参数，请将 **性能
规格** 设置为 `Coefficient of
performance for cooling` 或
`Coefficient of performance for
heating`。

### **压缩机等熵效率** — 压缩机理想比焓变化与实际比焓变化的比值 `0.8`（默认）| 正标量

压缩机理想（即等熵）比焓变化与
实际比焓变化的比值。

#### 依赖关系

要启用此参数，请将 **性能
规格** 设置为 `Compressor isentropic
efficiency`。

### **Compressor volumetric efficiency at nominal conditions** — 实际体积流量与排量之比 `0.95`（默认）| 正标量

压缩机实际体积流量与排量之比。

### **Compressor mechanical efficiency** — 转换为扭矩的效率 `0.95`（默认）| 正标量

传递给流体流的功率与驱动机械轴的功率之比。

### **Ratio of maximum to nominal expansion valve opening** — 维持过热度所需开阀面积之比 `1.5`（默认）| 正标量

全开阀面积与在标称工况下维持过热度所需阀面积之比。

### **Ratio of leakage to nominal expansion valve opening** — 维持过热度所需闭阀面积之比 `1e-6`（默认）| 正标量

关闭阀面积与在标称工况下维持过热度所需阀面积之比

### **Expansion valve smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

平滑因子，当阀处于接近打开或接近关闭位置时，为流量响应引入一层渐变。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Condenser refrigerant volume** — 冷凝器制冷剂体积 `0.001` `m^3`（默认）| 正标量

冷凝器中制冷剂的体积。

### **Evaporator refrigerant volume** — 蒸发器制冷剂体积 `0.001` `m^3`（默认）| 正标量

蒸发器中制冷剂的体积。

### **Liquid receiver tank volume** — 储液罐中液相和气相的体积 `0.01` `m^3`（默认）| 正标量

储液罐的总物理体积，包括液相和气相的体积。

### **Initial receiver liquid level** — 罐中初始液体体积分数 `0.5`（默认）| 正标量

仿真开始时储液罐中的液体体积分数。

### **Initialize refrigerant to nominal operating conditions** — 是否指定制冷剂初始条件 `on`（默认）| `off`

循环中的制冷剂是在仿真开始时基于标称运行参数处于标称运行工况，还是使用初始条件参数显式指定。

### **Initial condenser pressure** — 冷凝器中制冷剂初始压力 `1` `MPa`（默认）| 正标量

仿真开始时冷凝器和储液罐中制冷剂的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize
refrigerant to nominal operating conditions** 复选框。

### **Initial evaporator pressure** — 蒸发器中制冷剂初始压力 `0.1` `MPa`（默认）| 正标量

仿真开始时蒸发器中制冷剂的压力。

#### 依赖关系

要启用此参数，请清除 **Initialize
refrigerant to nominal operating conditions** 复选框。

### **Initial condenser specific enthalpy [inlet, outlet]** — 冷凝器中制冷剂初始比能 `[450, 250]` `kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时冷凝器中制冷剂的比焓。如果将此参数指定为包含两个值的向量，则第一个元素是入口比焓值，第二个元素是出口比焓值。如果输入标量，则该模块假定入口和出口比焓为相同值。

#### 依赖关系

要启用此参数，请清除 **Initialize
refrigerant to nominal operating conditions** 复选框。

### **Initial evaporator specific enthalpy [inlet, outlet]** — 蒸发器中制冷剂初始比能 `[250, 400]` `kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时蒸发器中制冷剂的比焓。如果将此参数指定为包含两个值的向量，则第一个元素是入口比焓值，第二个元素是出口比焓值。如果输入标量，则该模块假定入口和出口比焓为相同值。

#### 依赖关系

要启用此参数，请清除 **Initialize
refrigerant to nominal operating conditions** 复选框。

### **Initial receiver liquid and vapor fully saturated** — 是否指定储液罐初始条件 `on`（默认）| `off`

储液罐是在饱和平衡状态下开始仿真（即液相和气相体积均处于饱和状态），还是使用显式指定的初始条件。

#### 依赖关系

要启用此参数，请清除 **Initialize
refrigerant to nominal operating conditions** 复选框。

### **Initial receiver liquid specific enthalpy** — 储液罐初始液体比焓 `500` `kJ/kg`（默认）| 正标量

仿真开始时储液罐中制冷剂液体部分的比焓。

#### 依赖关系

要启用此参数，请清除 **Initialize
refrigerant to nominal operating conditions** 和
**Initial receiver liquid and vapor fully
saturated** 复选框。

### **Initial receiver vapor specific enthalpy** — 储液罐初始气体比焓 `3500` `kJ/kg`（默认）| 正标量

仿真开始时储液罐中制冷剂气体部分的比焓。

#### 依赖关系

要启用此参数，请清除 **Initialize
refrigerant to nominal operating conditions** 和
**Initial receiver liquid and vapor fully
saturated** 复选框。

### Condenser External Fluid

### **External fluid for condenser heat transfer** — 冷凝器中用于传热的外部流体 `Moist air`（默认）| `Gas` | `Thermal liquid` | `Two-phase fluid`

冷凝器中用于传热的外部流体。

### **Nominal mass flow rate** — 冷凝器端口之间的质量流量 `0.5` `kg/s`（默认）| 正标量

标称运行工况期间从端口 **Ac** 到端口 **Bc** 的质量流量。

### **Nominal pressure drop** — 冷凝器端口之间的压降 `0.001` `MPa`（默认）| 正标量

标称运行工况期间从端口 **Ac** 到端口 **Bc** 的压降。

### **Pressure specification** — 压力指定方法 `Specified pressure`（默认）| `Pressure at specified saturation temperature`

压力指定方法：

- `Specified pressure` — 指定标称入口压力。
- `Pressure at specified saturation
  temperature` — 指定与入口压力对应的标称饱和温度。

#### 依赖关系

要启用此参数，请将 **External fluid for
condenser heat transfer** 设置为 `Two-phase
fluid`。

### **Nominal inlet pressure** — 冷凝器外部流体侧入口处的压力 `0.101325` `MPa`（默认）| 正标量

标称运行工况期间热交换器外部流体侧冷凝器入口处的压力。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- 将 **External fluid for condenser heat
  transfer** 设置为
  `Gas`、`Moist
  air` 或 `Thermal
  liquid`。
- 将 **External fluid for condenser heat
  transfer** 设置为 `Two-phase
  fluid`，并将 **Pressure
  specification** 设置为 `Specific
  pressure`。

### **Nominal saturation temperature** — 用于指定压力的标称饱和温度 `400` `K`（默认）| 正标量

标称运行工况期间热交换器冷凝器外部流体侧出口处的饱和温度。冷凝器中的压力为对应的饱和压力。

#### 依赖关系

要启用此参数，请将 **External fluid for
condenser heat transfer** 设置为 `Two-phase
fluid`，并将 **Pressure
specification** 设置为 `Pressure at specified
saturation temperature`。

### **入口条件设定** — 描述流体入口条件的方法 `比焓`（默认）| `温度` | `蒸气干度`

模块用于描述冷凝器外部流体在额定工况下入口条件的方法。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`两相流体`。

### **额定入口温度** — 冷凝器外部流体侧入口处的温度 `400` `K`（默认）| 正标量

额定工况下冷凝器外部流体侧入口处的温度。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- **冷凝器换热的外部流体**设置为`气体`。
- **冷凝器换热的外部流体**设置为`两相流体`，且**初始条件设定**设置为`温度`。

### **额定入口比焓** — 冷凝器外部流体侧入口处的比焓 `500` `kJ/kg`（默认）| 正标量

额定工况下冷凝器外部流体侧入口处的比焓。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`两相流体`，且**初始条件设定**设置为`比焓`。

### **额定入口蒸气干度** — 冷凝器外部流体侧入口处的蒸气干度 `1`（默认）| 正标量

额定工况下冷凝器外部流体侧入口处的蒸气干度，定义为液-气混合物中蒸气的质量分数。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`两相流体`，且**初始条件设定**设置为`蒸气干度`。

### **入口湿度设定** — 描述冷凝器外部流体侧入口处湿度水平的方法 `相对湿度`（默认）| `比湿度` | `摩尔分数` | `湿度比` | `湿球温度`

模块用于描述额定工况下入口处湿度水平的方法。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`湿空气`。

### **额定入口相对湿度** — 入口处的相对湿度 `0.1`（默认）| 范围 [0,1] 内的标量

额定工况下冷凝器外部流体侧入口处的相对湿度。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`湿空气`，且**入口湿度设定**设置为`相对湿度`。

### **额定入口比湿度** — 入口处的比湿度 `0.01`（默认）| 范围 [0,1] 内的标量

额定工况下冷凝器外部流体侧入口处的比湿度，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`湿空气`，且**入口湿度设定**设置为`比湿度`。

### **额定入口水蒸气摩尔分数** — 入口处水蒸气的摩尔分数 `0.01`（默认）| 范围 [0,1] 内的标量

额定工况下冷凝器外部流体侧入口处湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`湿空气`，且**入口湿度设定**设置为`摩尔分数`。

### **额定入口湿度比** — 入口处的湿度比 `0.01`（默认）| 范围 [0,1] 内的标量

额定工况下冷凝器外部流体侧入口处的湿度比，定义为水蒸气与干空气及微量气体的质量比。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`湿空气`，且**入口湿度设定**设置为`湿度比`。

### **额定入口湿球温度** — 仿真开始时的湿球温度 `287 K`（默认）| 范围 [0,1] 内的正标量

额定工况下冷凝器外部流体侧入口处的湿球温度。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`湿空气`，且**入口湿度设定**设置为`湿球温度`。

### **入口微量气体设定** — 描述入口处微量气体水平的方法 `质量分数`（默认）| `摩尔分数`

模块用于描述额定工况下冷凝器外部流体侧入口处微量气体水平的方法。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`湿空气`。

### **额定入口微量气体质量分数** — 入口处微量气体的质量分数 `0.001`（默认）| 范围 [0,1] 内的标量

额定工况下冷凝器外部流体侧入口处湿空气混合物中微量气体的质量分数。

如果 Moist Air Properties (MA) 模块中的**微量气体模型**参数为`None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`湿空气`，且**入口微量气体设定**设置为`质量分数`。

### **额定入口微量气体摩尔分数** — 入口处微量气体的摩尔分数 `0.001`（默认）| 范围 [0,1] 内的标量

额定工况下冷凝器外部流体侧入口处湿空气混合物中微量气体的摩尔分数。

如果 Moist Air Properties (MA) 模块中的**微量气体模型**参数为`None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将**冷凝器换热的外部流体**设置为`湿空气`，且**入口微量气体设定**设置为`摩尔分数`。

### **外部流体体积** — 冷凝器中流体的体积 `0.1` `m^3`（默认）| 正标量

冷凝器中外部流体的总体积。

### **端口 Ac 处的横截面积** — 端口 Ac 处的流通面积 `0.01` `m^2`（默认）| 正标量

冷凝器外部流体端口 **Ac** 处的流通面积。

### **端口 Bc 处的横截面积** — 端口 Bc 处的流通面积 `0.01` `m^2`（默认）| 正标量

冷凝器外部流体端口 **Bc** 处的流通面积。

### **启用冷凝器壁热质量** — 建模冷凝器壁传热的选项 `Off`（默认）| `On`

是否包含换热表面的温度动态特性。

### **冷凝器壁质量** — 冷凝器换热质量 `1` `kg`（默认）| 正标量

冷凝器换热表面的总质量。

#### 依赖关系

要启用此参数，请选中**启用冷凝器壁热质量**。

### **冷凝器壁比热** — 冷凝器换热表面的比热 `490` `J/(K*kg)`（默认）| 正标量

冷凝器换热表面的比热。

#### 依赖关系

要启用此参数，请选中**启用冷凝器壁热质量**。

### **初始化到额定工况** — 是否指定冷凝器初始条件 `On`（默认）| `Off`

是否在额定工况下开始仿真，或使用附加参数指定一组不同的初始条件。

### **初始压力** — 仿真开始时的流体压力 `0.101325` `MPa`（默认）| 正标量

仿真开始时冷凝器外部流体的压力。

#### 依赖关系

要启用此参数，请清除**初始化到额定工况**复选框。

### **Initial fluid energy specification** — 冷凝器外部流体的初始状态 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

用于描述冷凝器外部流体初始状态的量。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Two-phase fluid`，并清除 **Initialize to nominal operating conditions** 复选框。

### **Initial temperature** — 仿真开始时的温度 `293.15` `K`（默认）| 正标量 | 二元素向量

仿真开始时的温度。如果该值为标量，则模块假定初始温度是均匀的。如果该值为二元素向量，则模块假定初始温度在冷凝器端口之间线性变化，第一个元素对应于端口 **Ac**，第二个元素对应于端口 **Bc**。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- 将 **External fluid for condenser heat transfer** 设置为 `Gas`、`Moist air` 或 `Thermal liquid`，并清除 **Initialize to nominal operating conditions** 复选框。
- 将 **External fluid for condenser heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Temperature`。

### **Initial vapor quality** — 仿真开始时的蒸汽质量分数 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

冷凝器外部流体在仿真开始时的蒸汽品质，定义为液-汽混合物中蒸汽的质量分数。如果该值为标量，则模块假定初始蒸汽品质是均匀的。如果该值为二元素向量，则模块假定初始蒸汽品质在冷凝器端口之间变化，第一个元素对应于端口 **Ac**，第二个元素对应于端口 **Bc**。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor quality`。

### **Initial vapor void fraction** — 仿真开始时的蒸汽空隙率 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

冷凝器外部流体在仿真开始时的蒸汽空隙率，定义为液-汽混合物中蒸汽的体积分数。如果该值为标量，则模块假定初始蒸汽空隙率是均匀的。如果该值为二元素向量，则模块假定初始蒸汽空隙品质在冷凝器端口之间变化，第一个元素对应于端口 **Ac**，第二个元素对应于端口 **Bc**。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor void fraction`。

### **Initial specific enthalpy** — 仿真开始时的单位质量焓 `1500` `kJ/kg`（默认）| 正标量 | 二元素向量

冷凝器外部流体在仿真开始时的比焓。如果该值为标量，则模块假定初始比焓是均匀的。如果该值为二元素向量，则模块假定初始比焓在冷凝器端口之间变化，第一个元素对应于端口 **Ac**，第二个元素对应于端口 **Bc**。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。

### **Initial specific internal energy** — 仿真开始时的单位质量内能 `1500` `kJ/kg`（默认）| 正标量 | 二元素向量

冷凝器外部流体在仿真开始时的比内能。如果该值为标量，则模块假定初始比内能是均匀的。如果该值为二元素向量，则模块假定初始比内能在冷凝器端口之间变化，第一个元素对应于端口 **Ac**，第二个元素对应于端口 **Bc**。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific internal energy`。

### **Initial humidity specification** — 用于描述初始湿度水平的方法 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

用于描述冷凝器外部流体初始湿度水平的方法。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，并清除 **Initialize to nominal operating conditions** 复选框。

### **Initial relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| [0,1] 范围内的标量 | 二元素向量

冷凝器外部流体在仿真开始时的相对湿度。如果该值为标量，则模块假定初始相对湿度是均匀的。如果该值为二元素向量，则模块假定初始相对湿度在端口之间线性变化，第一个元素对应于端口 **Ac**，第二个元素对应于端口 **Bc**。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial specific humidity** — 仿真开始时的比湿 `0.01`（默认）| [0,1] 范围内的标量 | 二元素向量

冷凝器外部流体在仿真开始时的比湿，定义为湿空气混合物中水蒸气的质量分数。如果该值为标量，则模块假定初始比湿是均匀的。如果该值为二元素向量，则模块假定初始比湿在端口之间线性变化，第一个元素对应于端口 **Ac**，第二个元素对应于端口 **Bc**。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial water vapor mole fraction** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量 | 二元素向量

冷凝器外部流体中水蒸气在仿真开始时的摩尔分数。如果该值为标量，则模块假定初始水蒸气摩尔分数是均匀的。如果该值为二元素向量，则模块假定初始水蒸气摩尔分数在端口之间线性变化，第一个元素对应于端口 **Ac**，第二个元素对应于端口 **Bc**。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial humidity ratio** — 仿真开始时的湿度比 `0.01`（默认）| [0,1] 范围内的标量 | 二元素向量

冷凝器外部流体湿度比，定义为仿真开始时水蒸气与干空气及微量气体的质量比。如果该值为标量，则模块假定初始湿度比均匀。如果该值为二元素向量，则模块假定初始湿度比在端口之间线性变化，第一个元素对应端口 **Ac**，第二个元素对应端口 **Bc**。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial moist air wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| [0,1] 范围内的正标量

仿真开始时冷凝器的湿球温度。

如果该值为标量，则模块假定初始湿球温度均匀。如果该值为二元素向量，则模块假定初始湿球温度在端口之间线性变化，第一个元素对应端口 **Ac**，第二个元素对应端口 **Bc**。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial trace gas specification** — 描述初始微量气体水平的方法 `Mass fraction`（默认）| `Mole fraction`

用于描述仿真开始时微量气体水平的方法。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，并清除 **Initialize to nominal operating conditions** 复选框。

### **Initial trace gas mass fraction** — 仿真开始时微量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气混合物中微量气体的质量分数。如果该值为标量，则模块假定初始质量分数均匀。如果该值为二元素向量，则模块假定初始质量分数在端口之间线性变化，第一个元素对应端口 **Ac**，第二个元素对应端口 **Bc**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial trace gas mole fraction** — 仿真开始时微量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气混合物中微量气体的摩尔分数。如果该值为标量，则模块假定初始摩尔分数均匀。如果该值为二元素向量，则模块假定初始摩尔分数在端口之间线性变化，第一个元素对应端口 **Ac**，第二个元素对应端口 **Bc**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气的比值 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`，并清除 **Initialize to nominal operating conditions** 复选框。

### **Initial condenser wall temperature** — 仿真开始时的冷凝器表面温度 `293.15` `K`（默认）| 正标量 | 二元素向量

仿真开始时的传热表面温度。如果该值为标量，则模块假定初始温度均匀。如果该值为二元素向量，则模块假定温度在端口 **Ac** 和 **Bc** 之间线性变化，第一个元素对应 **Ac**，第二个元素对应 **Bc**。

#### 依赖关系

要启用此参数，请清除 **Initialize to nominal operating conditions** 和 **Enable condenser wall thermal mass** 复选框。

### **Relative humidity at saturation** — 冷凝的相对湿度点 `1`（默认）| 非负标量

冷凝的相对湿度点。高于此值时发生冷凝。在大多数情况下，该值为 1，相当于 100%。大于 1 的值表示过饱和蒸汽。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`。

### **Water vapor condensation time constant** — 冷凝的时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝多余水分回到饱和状态的特征时间尺度。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`。

### **Water droplets evaporation time constant** — 蒸发的时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸汽的特征时间尺度。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`。

### **Fraction of condensate entrained as water droplets** — 水滴中冷凝物的分数 `1`（默认）| [0,1] 范围内的标量

湿空气中作为水滴夹带的冷凝物分数。

#### 依赖关系

要启用此参数，请将 **External fluid for condenser heat transfer** 设置为 `Moist air`。

### Evaporator External Fluid

### **External fluid for evaporator heat transfer** — 蒸发器中用于传热的外部流体 `Moist air`（默认）| `Gas` | `Thermal liquid` | `Two-phase fluid`

蒸发器中用于传热的外部流体。

### **Nominal mass flow rate** — 蒸发器端口之间的质量流量 `0.5` `kg/s`（默认）| 正标量

标称工况下从端口 **Ae** 到端口 **Be** 的质量流量。

### **Nominal pressure drop** — 蒸发器端口之间的压降 `0.001` `MPa`（默认）| 正标量

标称工况下从端口 **Ae** 到端口 **Be** 的压降。

### **Pressure specification** — 压力指定方法 `Specified pressure`（默认）| `Pressure at specified saturation temperature`

压力指定方法：

- `Specified pressure` — 指定标称入口压力。
- `Pressure at specified saturation temperature` — 指定与入口压力对应的标称饱和温度。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`。

### **Nominal inlet pressure** — 蒸发器外部流体侧入口处的压力 `0.101325` `MPa`（默认）| 正标量

标称工况下换热器外部流体侧蒸发器入口处的压力。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- 将 **External fluid for evaporator heat transfer** 设置为 `Gas`、`Moist air` 或 `Thermal liquid`。
- 将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，并将 **Pressure specification** 设置为 `Specific pressure`。

### **Nominal saturation temperature** — 用于指定压力的标称饱和温度 `400` `K`（默认）| 正标量

在标称工况下，蒸发器外部流体侧出口处的饱和温度。蒸发器中的压力为对应的饱和压力。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，并将 **Pressure specification** 设置为 `Pressure at specified saturation temperature`。

### **Inlet condition specification** — 描述流体入口条件的方法 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality`

模块用于描述标称工况下蒸发器外部流体入口条件的方法。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`。

### **Nominal inlet temperature** — 蒸发器外部流体侧入口处的温度 `400` `K`（默认）| 正标量

在标称工况下，蒸发器外部流体侧入口处的温度。

#### 依赖关系

要启用此参数，请设置以下任一条件：

- 将 **External fluid for evaporator heat transfer** 设置为 `Gas`。
- 将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，并将 **Initial condition specification** 设置为 `Temperature`。

### **Nominal inlet specific enthalpy** — 蒸发器外部流体侧入口处的比焓 `500` `kJ/kg`（默认）| 正标量

在标称工况下，蒸发器外部流体侧入口处的比焓。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，并将 **Initial condition specification** 设置为 `Specific enthalpy`。

### **Nominal inlet vapor quality** — 蒸发器外部流体侧入口处的蒸汽干度 `1`（默认）| 正标量

在标称工况下，蒸发器外部流体侧入口处的蒸汽干度，定义为液-汽混合物中蒸汽的质量分数。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，并将 **Initial condition specification** 设置为 `Vapor quality`。

### **Inlet humidity specification** — 描述蒸发器外部流体侧入口处湿度水平的方法 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

模块用于描述标称工况下入口处湿度水平的方法。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`。

### **Nominal inlet relative humidity** — 入口处的相对湿度 `0.1`（默认）| 范围 [0,1] 内的标量

在标称工况下，蒸发器外部流体侧入口处的相对湿度。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并将 **Inlet humidity specification** 设置为 `Relative humidity`。

### **Nominal inlet specific humidity** — 入口处的比湿度 `0.01`（默认）| 范围 [0,1] 内的标量

在标称工况下，蒸发器外部流体侧入口处的比湿度，定义为湿空气混合物中水蒸气的质量分数。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并将 **Inlet humidity specification** 设置为 `Specific humidity`。

### **Nominal inlet water vapor mole fraction** — 入口处水蒸气的摩尔分数 `0.01`（默认）| 范围 [0,1] 内的标量

在标称工况下，蒸发器外部流体侧入口处湿空气混合物中水蒸气的摩尔分数。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并将 **Inlet humidity specification** 设置为 `Mole fraction`。

### **Nominal inlet humidity ratio** — 入口处的湿度比 `0.01`（默认）| 范围 [0,1] 内的标量

在标称工况下，蒸发器外部流体侧入口处的湿度比，定义为水蒸气与干空气及微量气体的质量比。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并将 **Inlet humidity specification** 设置为 `Humidity ratio`。

### **Nominal inlet wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认）| 范围 [0,1] 内的正标量

在标称工况下，蒸发器外部流体侧入口处湿空气混合物中的蒸发器湿球温度。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并将 **Inlet humidity specification** 设置为 `Wet-bulb temperature`。

### **Inlet trace gas specification** — 描述入口处微量气体水平的方法 `Mass fraction`（默认）| `Mole fraction`

模块用于描述标称工况下蒸发器外部流体侧入口处微量气体水平的方法。

### **Nominal inlet trace gas mass fraction** — 入口处微量气体的质量分数 `0.001`（默认）| 范围 [0,1] 内的标量

在标称工况下，蒸发器外部流体侧入口处湿空气混合物中微量气体的质量分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并将 **Inlet trace gas specification** 设置为 `Mass fraction`。

### **Nominal inlet trace gas mole fraction** — 入口处微量气体的摩尔分数 `0.001`（默认）| 范围 [0,1] 内的标量

在标称工况下，蒸发器外部流体侧入口处湿空气混合物中微量气体的摩尔分数。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并将 **Inlet trace gas specification** 设置为 `Mole fraction`。

### **External fluid volume** — 蒸发器中流体的体积 `0.1` `m^3`（默认）| 正标量

蒸发器中外部流体的总体积。

### **Cross-sectional area at port Ae** — 端口 Ae 处的流通面积 `0.01` `m^2`（默认）| 正标量

蒸发器外部流体端口 **Ae** 处的流通面积。

### **Cross-sectional area at port Be** — 端口 Be 处的流通面积 `0.01` `m^2`（默认）| 正标量

蒸发器外部流体端口 **Be** 处的流通面积。

### **Enable evaporator wall thermal mass** — 用于建模蒸发器壁面传热的选项 `Off`（默认）| `On`

是否包含传热表面的温度动态特性。

### **Evaporator wall mass** — 蒸发器传热质量 `1` `kg`（默认）| 正标量

蒸发器传热表面的总质量。

#### 依赖关系

要启用此参数，请选中 **Enable evaporator wall thermal mass**。

### **Evaporator wall specific heat** — 蒸发器传热表面的比热容 `490` `J/(K*kg)`（默认）| 正标量

蒸发器传热表面的比热容。

#### 依赖关系

要启用此参数，请选中 **Enable evaporator wall thermal mass**。

### **Initialize to nominal operating conditions** — 是否指定蒸发器初始条件 `On`（默认）| `Off`

是否在标称工况下开始仿真，还是使用附加参数指定一组不同的初始条件。

### **Initial pressure** — 仿真开始时的流体压力 `0.101325` `MPa`（默认）| 正标量

仿真开始时蒸发器外部流体压力。

#### 依赖关系

要启用此参数，请清除 **Initialize to nominal operating conditions** 复选框。

### **Initial fluid energy specification** — 蒸发器外部流体的初始状态 `Specific enthalpy`（默认）| `Temperature` | `Vapor quality` | `Vapor void fraction` | `Specific internal energy`

用于描述蒸发器外部流体初始状态的量。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，并清除 **Initialize to nominal operating conditions** 复选框。

### **Initial temperature** — 仿真开始时的温度 `293.15` `K`（默认）| 正标量 | 二元素向量

仿真开始时的温度。如果该值为标量，则模块假定初始温度是均匀的。如果该值为二元素向量，则模块假定初始温度在蒸发器端口之间线性变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- 将 **External fluid for evaporator heat transfer** 设置为 `Gas`、`Moist air` 或 `Thermal liquid`，并清除 **Initialize to nominal operating conditions** 复选框。
- 将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Temperature`。

### **Initial vapor quality** — 仿真开始时的蒸气质量分数 `0.5`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时蒸发器外部流体的蒸气干度，定义为液-气混合物中蒸气的质量分数。如果该值为标量，则模块假定初始蒸气干度是均匀的。如果该值为二元素向量，则模块假定初始蒸气干度在蒸发器端口之间变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor quality`。

### **Initial vapor void fraction** — 仿真开始时的蒸气空泡份额 `0.5`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时蒸发器外部流体的蒸气空泡份额，定义为液-气混合物中蒸气的体积分数。如果该值为标量，则模块假定初始蒸气空泡份额是均匀的。如果该值为二元素向量，则模块假定初始蒸气空泡份额在蒸发器端口之间变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Vapor void fraction`。

### **Initial specific enthalpy** — 仿真开始时的单位质量焓 `1500` `kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时蒸发器外部流体的比焓。如果该值为标量，则模块假定初始比焓是均匀的。如果该值为二元素向量，则模块假定初始比焓在蒸发器端口之间变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific enthalpy`。

### **Initial specific internal energy** — 仿真开始时的单位质量内能 `1500` `kJ/kg`（默认）| 正标量 | 二元素向量

仿真开始时蒸发器外部流体的比内能。如果该值为标量，则模块假定初始比内能是均匀的。如果该值为二元素向量，则模块假定初始比内能在蒸发器端口之间变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial fluid energy specification** 设置为 `Specific internal energy`。

### **Initial humidity specification** — 用于描述初始湿度水平的方法 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

用于描述蒸发器外部流体初始湿度水平的方法。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并清除 **Initialize to nominal operating conditions** 复选框。

### **Initial relative humidity** — 仿真开始时的相对湿度 `0.5`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时蒸发器外部流体的相对湿度。如果该值为标量，则模块假定初始相对湿度是均匀的。如果该值为二元素向量，则模块假定初始相对湿度在端口之间线性变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial specific humidity** — 仿真开始时的比湿 `0.01`（默认）| 范围 [0,1] 内的标量 | 二元素向量

仿真开始时蒸发器外部流体的比湿，定义为湿空气混合物中水蒸气的质量分数。如果该值为标量，则模块假定初始比湿是均匀的。如果该值为二元素向量，则模块假定初始比湿在端口之间线性变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Specific humidity`。

### **初始水蒸气摩尔分数** — 仿真开始时的水蒸气摩尔分数 `0.01`（默认）| [0,1] 范围内的标量 | 二元素向量

蒸发器外部流体在仿真开始时的水蒸气摩尔分数。如果该值为标量，则模块假定初始水蒸气摩尔分数是均匀的。如果该值为二元素向量，则模块假定初始水蒸气摩尔分数在端口之间线性变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Mole fraction`。

### **初始湿度比** — 仿真开始时的湿度比 `0.01`（默认）| [0,1] 范围内的标量 | 二元素向量

蒸发器外部流体在仿真开始时的湿度比，定义为水蒸气与干空气和微量气体的质量比。如果该值为标量，则模块假定初始湿度比是均匀的。如果该值为二元素向量，则模块假定初始湿度比在端口之间线性变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **初始湿空气湿球温度** — 仿真开始时的湿球温度 `287 K`（默认）| [0,1] 范围内的正标量

仿真开始时的湿球温度。模块使用此值计算湿度。

如果该值为标量，则模块假定初始湿球温度是均匀的。如果该值为二元素向量，则模块假定初始湿球温度在端口之间线性变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **初始微量气体规格** — 描述初始微量气体水平的方法 `Mass fraction`（默认）| `Mole fraction`

用于描述仿真开始时微量气体水平的方法。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并清除 **Initialize to nominal operating conditions** 复选框。

### **初始微量气体质量分数** — 仿真开始时微量气体的质量分数 `0.001`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气混合物中微量气体的质量分数。如果该值为标量，则模块假定初始质量分数是均匀的。如果该值为二元素向量，则模块假定初始质量分数在端口之间线性变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **初始微量气体摩尔分数** — 仿真开始时微量气体的摩尔分数 `0.001`（默认）| [0,1] 范围内的标量 | 二元素向量

仿真开始时湿空气混合物中微量气体的摩尔分数。如果该值为标量，则模块假定初始摩尔分数是均匀的。如果该值为二元素向量，则模块假定初始摩尔分数在端口之间线性变化，第一个元素对应端口 **Ae**，第二个元素对应端口 **Be**。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，清除 **Initialize to nominal operating conditions** 复选框，并将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **水滴与湿空气的初始质量比** — 水滴与湿空气的比值 `0`（默认）| 正标量

水滴与湿空气的初始质量比。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`，并清除 **Initialize to nominal operating conditions** 复选框。

### **初始蒸发器壁温** — 仿真开始时的蒸发器表面温度 `293.15` `K`（默认）| 正标量 | 二元素向量

仿真开始时的传热表面温度。如果该值为标量，则模块假定初始温度是均匀的。如果该值为二元素向量，则模块假定温度在端口 **Ae** 和 **Be** 之间线性变化，第一个元素对应 **Ae**，第二个元素对应 **Be**。

#### 依赖关系

要启用此参数，请清除 **Initialize to nominal operating conditions** 和 **Enable evaporator wall thermal mass** 复选框。

### **饱和时的相对湿度** — 冷凝的相对湿度点 `1`（默认）| 非负标量

冷凝的相对湿度点。冷凝发生在此值以上。在大多数情况下，该值为 1，相当于 100%。大于 1 的值表示过饱和蒸汽。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`。

### **水蒸气冷凝时间常数** — 冷凝的时间尺度 `1e-3 s`（默认）| 正标量

过饱和湿空气体积通过冷凝多余水分回到饱和状态的特征时间尺度。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`。

### **水滴蒸发时间常数** — 蒸发的时间尺度 `1e-3 s`（默认）| 正标量

水滴蒸发为蒸汽的特征时间尺度。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`。

### **作为水滴夹带的冷凝物比例** — 水滴中冷凝物的比例 `1`（默认）| [0,1] 范围内的标量

湿空气中作为水滴夹带的冷凝物比例。

#### 依赖关系

要启用此参数，请将 **External fluid for evaporator heat transfer** 设置为 `Moist air`。

### 相关系数

### **修改冷凝器努塞尔数相关系数** — 是否修改冷凝器努塞尔数相关系数 `Off`（默认）| `On`

是否手动修改冷凝器努塞尔数相关系数。选择此参数以调整冷凝器的非设计性能。

### **制冷剂、液体区中 Nu = a\*Re^b\*Pr^c 中的 a** — 制冷剂过冷液体的关联式系数 `0.023`（默认值）| 正标量

冷凝器过冷液体的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**。

### **制冷剂、混合物区中 Nu = a\*Re^b\*Pr^c 中的 a** — 制冷剂液-汽混合物的关联式系数 `0.005`（默认值）| 正标量

冷凝器液-汽混合物的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Cavallini 和 Zecchin 关联式。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**。

### **制冷剂、蒸汽区中 Nu = a\*Re^b\*Pr^c 中的 a** — 制冷剂过热蒸汽的关联式系数 `0.023`（默认值）| 正标量

冷凝器过热蒸汽的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**。

### **制冷剂中 Nu = a\*Re^b\*Pr^c 中的 b** — 制冷剂关联式中的雷诺数指数 `0.8`（默认值）| 正标量

冷凝器制冷剂的努塞尔数作为雷诺数和普朗特数的函数关联式中的雷诺数指数。相同的值适用于过冷液体、液-汽混合物和过热蒸汽。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**。

### **制冷剂中 Nu = a\*Re^b\*Pr^c 中的 c** — 制冷剂关联式中的普朗特数指数 `0.33`（默认值）| 正标量

冷凝器制冷剂的努塞尔数作为雷诺数和普朗特数的函数关联式中的普朗特数指数。相同的值适用于过冷液体、液-汽混合物和过热蒸汽。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**。

### **外部流体、液体区中 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过冷液体的关联式系数 `0.023`（默认值）| 正标量

冷凝器外部流体过冷液体的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**，并将
**External fluid for condenser heat transfer**
设置为 `Two-phase fluid`。

### **外部流体、混合物区中 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中液-汽混合物的关联式系数 `0.005`（默认值）| 正标量

冷凝器外部流体中液-汽混合物的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Cavallini 和 Zecchin 关联式。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**，并将
**External fluid for condenser heat transfer**
设置为 `Two-phase fluid`。

### **外部流体、蒸汽区中 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过热蒸汽的关联式系数 `0.023`（默认值）| 正标量

冷凝器外部流体中过热蒸汽的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**，并将
**External fluid for condenser heat transfer**
设置为 `Two-phase fluid`。

### **外部流体中 Nu = a\*Re^b\*Pr^c 中的 a** — 冷凝器外部流体的关联式系数 `0.023`（默认值）| 正标量

冷凝器外部流体的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**，并将
**External fluid for condenser heat transfer**
设置为 `Moist air` 或 `Thermal
liquid`。

### **外部流体中 Nu = a\*Re^b\*Pr^c 中的 b** — 冷凝器外部流体关联式中的雷诺数指数 `0.8`（默认值）| 正标量

冷凝器外部流体的努塞尔数作为雷诺数和普朗特数的函数关联式中的雷诺数指数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**。

### **外部流体中 Nu = a\*Re^b\*Pr^c 中的 c** — 冷凝器外部流体关联式中的普朗特数指数 `0.33`（默认值）| 正标量

冷凝器外部流体的努塞尔数作为雷诺数和普朗特数的函数关联式中的普朗特数指数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选择 **Modify condenser
Nusselt number correlation coefficients**。

### **Modify evaporator Nusselt number correlation coefficients** — 是否修改蒸发器努塞尔数关联式系数 `Off`（默认值）| `On`

是否手动修改蒸发器努塞尔数关联式系数。选择此参数以调整蒸发器的非设计性能。

### **制冷剂、液体区中 Nu = a\*Re^b\*Pr^c 中的 a** — 制冷剂过冷液体的关联式系数 `0.023`（默认值）| 正标量

蒸发器过冷液体的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选择 **Modify evaporator
Nusselt number correlation coefficients**。

### **制冷剂、混合物区中 Nu = a\*Re^b\*Pr^c 中的 a** — 制冷剂液-汽混合物的关联式系数 `0.005`（默认值）| 正标量

蒸发器液-汽混合物的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Cavallini 和 Zecchin 关联式。

#### 依赖关系

要启用此参数，请选择 **Modify evaporator
Nusselt number correlation coefficients**。

### **制冷剂、蒸汽区中 Nu = a\*Re^b\*Pr^c 中的 a** — 制冷剂过热蒸汽的关联式系数 `0.023`（默认值）| 正标量

冷凝器过热蒸汽的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选择 **Modify evaporator
Nusselt number correlation coefficients**。

### **制冷剂 Nu = a\*Re^b\*Pr^c 中的 b** — 制冷剂关联式中的雷诺数指数 `0.8`（默认）| 正标量

蒸发器制冷剂的努塞尔数作为雷诺数和普朗特数的函数关联式中的雷诺数指数。同一值适用于过冷液体、气液混合物和过热蒸气。

#### 依赖关系

要启用此参数，请选中 **Modify evaporator Nusselt number correlation coefficients**。

### **制冷剂 Nu = a\*Re^b\*Pr^c 中的 c** — 制冷剂关联式中的普朗特数指数 `0.33`（默认）| 正标量

蒸发器制冷剂的努塞尔数作为雷诺数和普朗特数的函数关联式中的普朗特数指数。同一值适用于过冷液体、气液混合物和过热蒸气。

#### 依赖关系

要启用此参数，请选择 **External fluid for evaporator heat transfer**。

### **外部流体液相区 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过冷液体的关联式系数 `0.023`（默认）| 正标量

蒸发器外部流体中过冷液体的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选中 **Modify evaporator Nusselt number correlation coefficients** 并将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`。

### **外部流体混合物区 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中气液混合物的关联式系数 `0.005`（默认）| 正标量

蒸发器外部流体中气液混合物的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Cavallini 和 Zecchin 关联式。

#### 依赖关系

要启用此参数，请选中 **Modify evaporator Nusselt number correlation coefficients** 并将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`。

### **外部流体蒸气区 Nu = a\*Re^b\*Pr^c 中的 a** — 两相流体中过热蒸气的关联式系数 `0.023`（默认）| 正标量

蒸发器外部流体中过热蒸气的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选中 **Modify evaporator Nusselt number correlation coefficients** 并将 **External fluid for evaporator heat transfer** 设置为 `Two-phase fluid`。

### **外部流体 Nu = a\*Re^b\*Pr^c 中的 a** — 蒸发器外部流体的关联式系数 `0.023`（默认）| 正标量

蒸发器外部流体的努塞尔数作为雷诺数和普朗特数的函数关联式中的比例常数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选中 **Modify evaporator Nusselt number correlation coefficients** 并将 **External fluid for evaporator heat transfer** 设置为 `Moist air` 或 `Thermal liquid`。

### **外部流体 Nu = a\*Re^b\*Pr^c 中的 b** — 蒸发器外部流体关联式中的雷诺数指数 `0.8`（默认）| 正标量

蒸发器外部流体的努塞尔数作为雷诺数和普朗特数的函数关联式中的雷诺数指数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选中 **Modify evaporator Nusselt number correlation coefficients**。

### **外部流体 Nu = a\*Re^b\*Pr^c 中的 c** — 蒸发器外部流体关联式中的普朗特数指数 `0.33`（默认）| 正标量

蒸发器外部流体的努塞尔数作为雷诺数和普朗特数的函数关联式中的普朗特数指数。默认值基于 Colburn 方程。

#### 依赖关系

要启用此参数，请选中 **Modify evaporator Nusselt number correlation coefficients**。

## 所属库

Simscape / Fluids / Two-Phase Fluid / Thermodynamic Cycles

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2025a：选择气体作为冷凝器和蒸发器外部流体

将 **External fluid for condenser heat transfer** 或 **External fluid for evaporator heat transfer** 参数设置为 `Gas`，以将冷凝器或蒸发器外部流体建模为气体。

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要启用液滴跟踪，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选中 **Enable entrained water droplets**。

### R2024a：新增湿度指定选项

该模块为冷凝器和蒸发器外部流体的 **Inlet humidity specification** 和 **Initial humidity specification** 参数提供了新选项。此选项称为 `Wet-bulb temperature`，允许您以湿球温度的形式输入数据。

## 描述

气体、湿空气、热液体或两相流体网络中的系统级两相制冷模块

System-Level Refrigeration Cycle (2P) 模块对基本制冷循环进行建模，该循环由压缩机、冷凝器、储液器、热力膨胀阀和蒸发器组成。该模块使用端口 **F** 处指定的流体属性，在两相流体域中对模块内的制冷剂回路进行建模。冷凝器和蒸发器外部流体可以是气体、湿空气、热液体或两相流体网络的一部分。外部流体是冷凝器和蒸发器中与制冷剂相对的流体。

当压缩机开启时，制冷循环消耗功率，将热量从蒸发器外部流体传递到冷凝器外部流体。各子组件在标称运行条件下提供指定的标称传热量。

### 模块结构

此模块的行为是此制冷循环的简化版本，该制冷循环由 Simscape™ Fluids™ 模块构建，用于对冷凝器、压缩机、蒸发器、膨胀装置和储液器进行建模：

由冷凝器、压缩机、蒸发器、膨胀装置和储液器组成的制冷循环示意图

制冷剂沿逆时针方向流过回路。由端口 **S** 处信号控制的压缩机吸入制冷剂蒸气并产生高温高压蒸气，该蒸气流向冷凝器。冷凝器将制冷剂的热量排至外部流体，使制冷剂冷凝。储液器用作制冷剂的储罐，并且仅允许液体流出，这有助于在外部条件波动导致冷凝器输出变化时仍维持正常运行。制冷剂从储罐流向膨胀装置，膨胀装置通常是阀门或毛细管，会产生较大的压降。压力下降使制冷剂部分汽化，从而使其降温。制冷剂流向蒸发器，蒸发器从外部流体吸收热量传递给低温制冷剂，使制冷剂汽化。

System-Level Refrigeration Cycle (2P) 模块的子组件行为与此模型中的这些 Simscape Fluids 模块相同，但容积式压缩机、膨胀阀、储液器组件以及冷凝器和蒸发器子组件的方程有所不同。有关制冷系统各个组件的更多信息，请参阅：

- Compressor (2P)
- Thermostatic Expansion Valve (2P)
- Receiver Accumulator (2P)

压缩机和蒸发器组件取决于 **External fluid for condenser heat transfer** 和 **External fluid for evaporator heat transfer** 参数。有关更多信息，请参阅：

- System-Level Condenser Evaporator (2P-G)
- System-Level Condenser Evaporator (2P-MA)
- System-Level Condenser Evaporator (2P-TL)
- System-Level Heat Exchanger (2P-2P)

**容积式压缩机子组件**

压缩机子组件确定系统的制冷剂质量流量。物理信号输入端口 **S** 控制压缩机运行。当端口 **S** 处的值为 `0` 时，压缩机关闭，质量流量为 `0`。当端口 **S** 处的值为 `1` 时，压缩机以额定轴转速运行，在额定工况下产生额定质量流量。为防止逆流，**S** 的值必须大于或等于 `0`。

压缩机中的质量流量为

m˙=ηvV˙nominalSvin,

其中：

- *ηv* 是容积效率。
- *S* 是端口 **S** 处信号的值。
- *vin* 是入口比体积。
- V˙nominal 是额定体积流量，模块根据额定质量流量 m˙nominal 确定，而额定质量流量取决于 **Capacity specification** 参数的设置：

  - 当 **Capacity specification** 参数为 `Cooling load` 时，

    m˙nominal=Qcoolingh1−h4,

    其中 *Qcooling* 是 **Nominal evaporator heat transfer** 参数，*h1* 是蒸发器出口比焓，*h4* 是阀出口比焓。
  - 当 **Capacity specification** 参数为 `Heating load` 时，

    m˙nominal=Qheatingh2−h3,

    其中 *Qcooling* 是 **Nominal condenser heat transfer** 参数，*h2* 是压缩机出口比焓，*h3* 是冷凝器出口比焓。
  - 当 **Capacity specification** 参数为 `Refrigerant mass flow rate` 时，m˙nominal 是 **Nominal mass flow rate** 参数的值。

压缩机向流体添加的流体功率为

Φfluid=m˙hout,isen−hinηs,

其中：

- *hout,isem* 是在等熵过程的输出压力下评估的比焓。
- *hin* 是入口比焓。
- *ηs* 是等熵效率。

  - 当 **Performance specification** 为 `Coefficient of performance for cooling` 或 `Coefficient of performance for heating` 时，模块通过计算 *h2* 并使用以下关系式求解 *ηs*

    h2=h2isen−h1ηs+h1,

    其中 *h2isen* 是假设等熵过程时压缩机出口比焓。

    - 当 **Performance specification** 为 `Coefficient of performance for cooling` 时，模块使用 CoPcooling=h1−h4h2−h1 求解 *h2*，其中 *CoPcooling* 是 **Coefficient of performance at nominal conditions** 参数。
    - 当 **Performance specification** 为 `Coefficient of performance for heating` 时，模块使用 CoPheating=h2−h3h2−h1=h2−h4h2−h1=CoPcooling+1 求解 *h2*，其中 *CoPheating* 是 **Coefficient of performance at nominal conditions** 参数。
  - 当 **Performance specification** 为 `Compressor isentropic efficiency` 时，*ηs* 是 **Compressor isentropic efficiency** 参数的值。

模块根据入口和出口比体积直接计算容积效率

ηv=1+C−Cvinvout,

其中：

- *C* 是模块根据额定工况确定的余隙容积分数。
- *vin* 和 *vout* 是在入口和出口压力下评估的入口和出口比体积。

压缩机子组件没有机械旋转端口，也不需要计算轴扭矩。机械功率为

Φmech=Φfluidηm,

其中 *ηm* 是机械效率。

**膨胀阀子组件**

由压缩机确定的质量流量与恒温膨胀阀子组件两端压降之间的关系为

m˙=Seff2vinΔp(Δp2−Δplam2)0.25,

其中：

- *vin* 是入口比体积。
- *Δp* 是阀两端压差。
- *Δplam* 是过渡流的压力阈值。低于此值时，流动为层流。

有效阀面积取决于测量压力 *pbulb* 与均衡压力 *peq* 之间的压差

Seff=β[(pbulb−peq)−(psat(Tevap+ΔTstatic)−psat(Tevap))],

其中：

- *β* 是模块根据额定工况确定的阀常数。
- *Tevap* 是蒸发温度，取决于 **Pressure specification** 设置：

  - 当 **Pressure specification** 为 `Pressure at specified saturation temperature` 时，*Tevap* 是 **Nominal evaporating (saturation) temperature** 参数的值。
  - 当 **Pressure specification** 为 `Specified pressure` 时，*Tevap* 是对应于 **Nominal evaporator pressure** 参数值的饱和温度。
- *ΔTstatic* 是 **Static (minimum) evaporator superheat** 参数。
- *psat(Tevap)* 是作为 *Tevap* 函数的流体饱和压力。
- *psat(Tevap+ΔTstatic)* 是作为 *Tevap+ΔTstatic* 函数的流体饱和压力。
- *pbulb* 是感温包中的流体压力。该压力是蒸发器出口温度下的饱和压力。
- *peq* 是均衡压力，对于此模块即为蒸发器压力。

有效阀面积存在限制。最小有效阀面积 *Seff,min* 为

Seff,min=fleakSeff,nom,

其中 *fleak* 是 **Ratio of leakage to nominal expansion valve opening** 参数的值。最大有效阀面积 *Seff,mmax* 为

Seff,max=fmaxSeff,nom,

其中 *fmax* 是 **Ratio of maximum to nominal expansion valve opening** 参数的值。

**储液器子组件**

除接收器外，该模块假设制冷剂质量流量在整个回路中为同一值。在接收器中，总质量基于压缩机产生的质量流量与膨胀阀计量的质量流量之间的平衡。接收器子组件的流出物始终为液体，并且与环境完全绝热。

接收器子组件中的液体质量分数为

M dxliqdt=m˙liq,in−m˙out−m˙vaporization+m˙condensation，

其中：

- *xliq* 是液体质量分数。
- m˙liq,in 是流入物流中为液体的部分。
- m˙out 是流出接收器的质量流量。
- m˙vaporization 是从液体体积到蒸气体积的汽化速率。
- m˙condensation 是从蒸气体积到液体体积的冷凝速率。

压力通过比体积与总质量相关联，关系为

M(xliqvliq+(1−xliq)vvap)=V，

其中：

- *V* 是接收器总体积。
- *vliq* 是液体体积的比体积。
- *vvap* 是蒸气体积的比体积。

**冷凝器和蒸发器子组件**

冷凝器和蒸发器子组件对制冷剂热质量进行建模，但不对流体体积进行建模。对于冷凝器和蒸发器，能量守恒方程为

M dhIdt=m˙(hin−hout)+Q，

其中：

- *M* 是组件中制冷剂的恒定质量。
- *hI* 是组件内部节点处的制冷剂比焓。
- m˙ 是制冷剂质量流量。
- *Q* 是从外部流体到制冷剂的传热速率。
- *hin* 和 *hout* 是流入和流出组件的制冷剂比焓。

### 可视化 P-H 图

要可视化制冷循环，请使用 Simscape > Utilities 库中的 Probe 模块输出变量 `p_cycle` 和 `h_cycle`。这些变量包含制冷循环的四个压力和比焓点。将变量连接到 P-H Diagram (2P) 模块以可视化制冷循环。

此图显示了制冷剂 R-410a 在整个系统中的流体属性。段 1 到 2 是压缩机，段 2 到 3 是冷凝器，点 3 是接收器，段 3 到 4 是膨胀阀，段 4 到 1 是蒸发器。

制冷循环的 P-H 图

### 假设和限制

- 该模块不对反向流动建模，并将制冷循环限制为零流量和正向流动。为防止反向流动，该模块将压缩机控制限制为零或正向运行，并且仅在液体接收器子组件中对流体体积建模。
- 除液体接收器外，各子组件不对制冷剂流体体积建模，这防止了子组件中的质量积累。因此，制冷剂质量流量在蒸发器、压缩机和冷凝器子组件中相同。
- 蒸发器或冷凝器中不存在制冷剂压力损失。
- 该模块不对制冷剂流动中的动能变化建模。
- 蒸发器子组件对近似压力动态建模，以保持数值鲁棒性。然而，冷凝器子组件不对近似压力动态建模，因为冷凝器压力等于接收器压力，而接收器压力确实对压力动态建模。
- 冷凝器和蒸发器子组件仅对逆流建模，因为制冷剂在冷凝器和蒸发器内主要处于两相混合物状态。因此，在冷凝器和蒸发器的大部分区域温度是均匀的，逆流和交叉流之间没有显著差异。
- 在确定换热器尺寸时，该模块忽略 **Fraction of condensate entrained as water droplets** 参数的值，并假设冷凝液不以液滴形式夹带。
