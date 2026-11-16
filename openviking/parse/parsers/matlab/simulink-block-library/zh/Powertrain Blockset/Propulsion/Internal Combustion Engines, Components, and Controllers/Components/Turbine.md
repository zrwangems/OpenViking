---
type: simulink-block
title: 'Turbine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'turbine'
documentation_source_path: 'ref/turbine.html'
language: zh-CN
chinese_source: worker-translation
---

# Turbine

## 端口

### 输入

### **Ds** — 驱动轴转速双向连接端口

`ShaftSpd` — 包含驱动轴角速度 ω 的信号，单位为 rad/s。

### **A** — 入口压力、温度、焓、质量分数双向连接端口

包含入口控制体积的总线：

- `InPrs` — 压力，pinlet，单位 Pa
- `InTemp` — 温度，Tinlet，单位 K
- `InEnth` — 比焓，hinlet，单位 J/kg

### **B** — 出口压力、温度、焓、质量分数双向连接端口

包含出口控制体积的总线：

- `OutPrs` — 压力，poutlet，单位 Pa
- `OutTemp` — 温度，Toutlet，单位 K
- `OutEnth` — 比焓，houtlet，单位 J/kg

### **RackPos** — 齿条位置 `scalar`

可变几何涡轮齿条位置，Lrack。

#### 依赖关系

要创建此端口，请为 **Turbine type** 参数选择 `Variable geometry`。

### **WgAreaPct** — 废气门面积百分比 `scalar`

废气门阀面积百分比，Awgpctcmd。

#### 依赖关系

要创建此端口，请选择 **Include wastegate**。

### 输出

### **Info** — 总线信号 bus

包含以下模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `TurbOutletTemp` | | | 离开涡轮的温度 | K |
| `DriveshftPwr` | | | 驱动轴功率 | W |
| `DriveshftTrq` | | | 驱动轴扭矩 | N·m |
| `TurbMassFlw` | | | 涡轮质量流量 | kg/s |
| `PrsRatio` | | | 压力比 | N/A |
| `DriveshftCorrSpd` | | | 校正驱动轴转速 | rad/s |
| `TurbEff` | | | 涡轮等熵效率 | N/A |
| `CorrMassFlw` | | | 校正质量流量 | kg/s |
| `WgArea` | | | 废气门阀面积 | m^2 |
| `WgMassFlw` | | | 通过废气门阀的质量流量 | kg/s |
| `WgOutletTemp` | | | 离开废气门阀的温度 | K |
| `PwrInfo` | `PwrTrnsfrd` | `PwrDriveshft` | 从轴传输的功率 | W |
| `PwrHeatFlwIn` | 端口 A 的热流量 | W |
| `PwrHeatFlwOut` | 端口 B 的热流量 | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 功率损失 | W |
| `PwrStored` | | *未使用* | |

### **Ds** — 驱动轴扭矩双向连接端口

`Trq` — 包含驱动轴扭矩 τturb 的信号，单位为 N·m。

### **A** — 入口质量流量、热流量、温度、质量分数双向连接端口

包含：

- `MassFlwRate` — 通过废气门阀和涡轮的总质量流量，–m˙total，单位 kg/s
- `HeatFlwRate` — 总入口热流量，–qinlet，单位 J/s
- `Temp` — 总入口温度，Tinlet，单位 K
- `MassFrac` — 质量分数，无量纲。

  具体而言，包含以下质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃燃料
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 燃烧气体

### **B** — 出口质量流量、热流量、温度、质量分数双向连接端口

包含：

- `MassFlwRate` — 通过废气门阀和涡轮的涡轮质量流量，m˙turb，单位 kg/s
- `HeatFlwRate` — 总出口热流量，qoutlet，单位 J/s
- `Temp` — 总出口温度，Toutflw，单位 K
- `MassFrac` — 质量分数，无量纲。

  具体而言，包含以下质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃燃料
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 燃烧气体

## 参数

#### 模块选项

### **Turbine type** — 选择涡轮类型 `Fixed geometry` (默认) | `Variable geometry`

涡轮类型。

#### 依赖关系

下表总结了参数和端口依赖关系。

| 值 | 启用参数 | 创建端口 |
| --- | --- | --- |
| `Fixed geometry` | **Corrected mass flow rate table, mdot\_corrfx\_tbl**  **Efficiency table, eta\_turbfx\_tbl**  **Corrected speed breakpoints, w\_corrfx\_bpts1**  **Pressure ratio breakpoints, Pr\_fx\_bpts2** | 无 |
| `Variable geometry` | **Corrected mass flow rate table, mdot\_corrvr\_tbl**  **Efficiency table, eta\_turbvr\_tbl**  **Corrected speed breakpoints, w\_corrvr\_bpts2**  **Pressure ratio breakpoints, Pr\_vr\_bpts2**  **Rack breakpoints, L\_rack\_bpts3** | `RP` |

### **Include wastegate** — 选择 on (默认) | off

#### 依赖关系

选择 **Include wastegate** 参数会启用：

- **Wastegate flow area, A\_wgopen**
- **Pressure ratio linearize limit, Plim\_wg**

#### 性能表

### **Calibrate Performance Maps** — 使用测量数据校准表 `selection`

如果你有 Model-Based Calibration Toolbox，点击 **Calibrate Performance Maps** 使用测量数据虚拟校准校正质量流量和涡轮效率查找表。该对话框按以下任务逐步操作。

| 任务 | 描述 |
| --- | --- |
| 导入涡轮数据 | 从文件导入此涡轮数据。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。  | **Turbine type** | 数据 | | --- | --- | | `Fixed geometry` | - 速度，Spd，单位 rad/s - 校正质量流量，MassFlwRate，单位 kg/s - 压力比，PrsRatio，无量纲 - 效率，Eff，无量纲  速度、校正质量流量、压力比和效率分别位于数据文件的第 2-5 列。数据文件的第一行和第二行提供变量名称和单位。例如，使用此格式。  |  |  |  |  |  | | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  | | Data: | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... | | | `Variable geometry` | - 速度，Spd，单位 rad/s - 校正质量流量，MassFlwRate，单位 kg/s - 齿条位置，RackPos，无量纲 - 压力比，PrsRatio，无量纲 - 效率，Eff，无量纲  在每个齿条位置工况点包含若干测试点的数据。  速度、校正质量流量、齿条位置、压力比和效率分别位于数据文件的第 2-6 列。数据文件的第一行和第二行提供变量名称和单位。例如，使用此格式。  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | RackPos | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  |  | | Data: | `8373.3` | `0.02` | `1` | `1.21` | `0.44` | |  | ... | ... |  | ... | ... | |    Model-Based Calibration Toolbox 将速度和压力比断点值限制为文件中的最大值。  要筛选或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 拟合导入的数据并生成响应模型。  | **Turbine type** | 描述 | | --- | --- | | `Fixed geometry` | | 数据 | 响应模型 | | --- | --- | | 校正质量流量 | *Modeling and Control of Engines and Drivelines*2 中描述的平方根涡轮流量模型 | | 效率 | *Modeling and Control of Engines and Drivelines*2 中描述的叶片速度比 (BSR) 模型 | | | `Variable geometry` | Model-Based Calibration Toolbox 使用逐点测试计划拟合数据。对于每个齿条位置，该模块使用这些响应模型拟合校正质量流量和效率数据。  | 数据 | 响应模型 | | --- | --- | | 校正质量流量 | *Modeling and Control of Engines and Drivelines*2 中描述的平方根涡轮流量模型 | | 效率 | *Modeling and Control of Engines and Drivelines*2 中描述的叶片速度比 (BSR) 模型 | |  要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成校准 | Model-Based Calibration Toolbox 校准响应模型并生成校准表。  | **Turbine type** | 描述 | | --- | --- | | `Fixed geometry` | Model-Based Calibration Toolbox 使用响应模型生成校正质量流量和效率表。 | | `Variable geometry` | Model-Based Calibration Toolbox 为每个齿条位置填充校正质量流量和效率表。然后，Model-Based Calibration Toolbox 将依赖于齿条位置的表合并为校正质量流量和效率的 3D 查找表。 |  要评估或调整校准，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用校准更新这些校正质量流量和效率参数。  | **Turbine type** | 参数 | | --- | --- | | `Fixed geometry` | - **Corrected mass flow rate table,   mdot\_corrfx\_tbl** - **Efficiency table,   eta\_turbfx\_tbl** - **Corrected speed breakpoints,   w\_corrfx\_bpts1** - **Pressure ratio breakpoints,   Pr\_fx\_bpts2** | | `Variable geometry` | - **Corrected mass flow rate table,   mdot\_corrvr\_tbl** - **Efficiency table,   eta\_turbvr\_tbl** - **Corrected speed breakpoints,   w\_corrvr\_bpts2** - **Pressure ratio breakpoints,   Pr\_vr\_bpts2** - **Rack breakpoints,   L\_rack\_bpts3** | |

### **Corrected mass flow rate table, mdot\_corrfx\_tbl** — 查找表 `array`

固定几何的校正质量流量查找表，m˙corrfx,tbl，作为校正驱动轴转速 *ωcorr* 和压力比 *pr* 的函数，单位为 kg/s。

质量流量与校正驱动轴转速和压力比的关系。

#### 依赖关系

要启用此参数，请为 **Turbine type** 参数选择 `Fixed geometry`。

### **Efficiency table, eta\_turbfx\_tb** — 查找表 `array`

固定几何的效率查找表，ηturbfx,tbl，作为校正驱动轴转速 *ωcorr* 和压力比 *pr* 的函数，无量纲。

效率与校正驱动轴转速和压力比的关系。

#### 依赖关系

要启用此参数，请为 **Turbine type** 参数选择 `Fixed geometry`。

### **Corrected speed breakpoints, w\_corrfx\_bpts1** — 固定几何 `[0 1552 3104 4657 6209 7761 9313 1.087e+04 1.242e+04 1.397e+04]` (默认) | `vector`

固定几何的校正驱动轴转速断点，ωcorrfx,bpts1，单位为 rad/s。

#### 依赖关系

要启用此参数，请为 **Turbine type** 参数选择 `Fixed geometry`。

### **Pressure ratio breakpoints, Pr\_fx\_bpts2** — 固定几何 `[1 1.333 1.667 2 2.333 2.667 3 3.333 3.667 4]` (默认) | `vector`

固定几何的压力比断点，prfx,bpts2。

#### 依赖关系

要启用此参数，请为 **Turbine type** 参数选择 `Fixed geometry`。

### **Corrected mass flow rate table, mdot\_corrvr\_tbl** — 查找表 `array`

可变几何的校正质量流量查找表，m˙corrvr,tbl，作为校正驱动轴转速 *ωcorr* 和压力比 *pr* 的函数，单位为 kg/s。

质量流量与校正驱动轴转速和压力比的关系。

#### 依赖关系

要启用此参数，请为 **Turbine type** 参数选择 `Variable geometry`。

### **Efficiency table, eta\_turbvr\_tbl** — 查找表 `array`

可变几何的效率查找表，ηturbvr,tbl，作为校正驱动轴转速 *ωcorr* 和压力比 *pr* 的函数，无量纲。

效率与校正驱动轴转速和压力比的关系。

#### 依赖关系

要启用此参数，请为 **Turbine type** 参数选择 `Variable geometry`。

### **Corrected speed breakpoints, w\_corrvr\_bpts2** — 可变几何 `[0 1752 3504 5257 7009 8761 1.051e+04 1.227e+04 1.402e+04 1.577e+04]` (默认) | `vector`

可变几何的校正驱动轴转速断点，ωcorrvr,bpts1，单位为 rad/s。

#### 依赖关系

要启用此参数，请为 **Turbine type** 参数选择 `Variable geometry`。

### **Pressure ratio breakpoints, Pr\_vr\_bpts2** — 可变几何 `[1 1.306 1.611 1.917 2.222 2.528 2.833 3.139 3.444 3.75]` (默认) | `vector`

可变几何的压力比断点。

#### 依赖关系

要启用此参数，请为 **Turbine type** 参数选择 `Variable geometry`。

### **Rack breakpoints, L\_rack\_bpts3** — 可变几何 `[0 0.2 0.3 0.5 0.7 1]` (默认) | `vector`

可变几何的齿条位置断点，Lrack,bpts3。

#### 依赖关系

要启用此参数，请为 **Turbine type** 参数选择 `Variable geometry`。

### **Reference temperature, T\_ref** — 温度 `293.15` (默认) | `scalar`

性能图参考温度，Tref，单位 K。

### **Reference pressure, P\_ref** — 压力 `101325` (默认) | `scalar`

性能图参考压力，Pref，单位 Pa。

#### 废气门

### **Wastegate flow area, A\_wgopen** — 面积 `0.0003` (默认) | `scalar`

完全打开的废气门阀面积，Awgopen，单位 m^2。

#### 依赖关系

要启用 **Wastegate flow area, A\_wgopen**，请选择 **Include wastegate** 参数。

### **Pressure ratio linearize limit, Plim\_wg** — 面积，m^2 `0.95` (默认) | `scalar`

#### 依赖关系

流量限制线性化限制，plim,wg。

要启用 **Pressure ratio linearize limit, Plim\_wg**，请选择 **Include wastegate** 参数。

#### 属性

### **Ideal gas constant, R** — 常数 `287` (默认) | `scalar`

理想气体常数 R，单位 J/(kg·K)。

### **Specific heat at constant pressure, cp** — 比热 `1005` (默认) | `scalar`

定压比热，cp，单位 J/(kg·K)。

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Boost

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

用于增压发动机的涡轮

Turbine 模块使用质量和能量守恒来计算固定几何或可变几何涡轮的质量流量和热流量。你可以配置该模块，使用废气门阀绕过涡轮。该模块使用双向端口连接到入口和出口控制体积以及驱动轴。你可以指定查找表来计算质量流量和涡轮效率。通常，涡轮制造商提供作为校正转速和压力比函数的质量流量和效率表。该模块不支持反向质量流量。

如果你有 Model-Based Calibration Toolbox™，点击 **Calibrate Performance Maps** 使用测量数据虚拟校准质量流量和涡轮效率查找表。

质量流量从入口控制体积流向出口控制体积。

显示废气门和涡轮的示意图。

Turbine 模块实现方程以建模性能、废气门流量和组合流量。

### 虚拟校准

如果你有 Model-Based Calibration Toolbox，点击 **Calibrate Performance Maps** 使用测量数据虚拟校准校正质量流量和涡轮效率查找表。该对话框按以下任务逐步操作。

| 任务 | 描述 |
| --- | --- |
| 导入涡轮数据 | 从文件导入此涡轮数据。有关详细信息，请参阅 Using Data (Model-Based Calibration Toolbox)。  | **Turbine type** | 数据 | | --- | --- | | `Fixed geometry` | - 速度，Spd，单位 rad/s - 校正质量流量，MassFlwRate，单位 kg/s - 压力比，PrsRatio，无量纲 - 效率，Eff，无量纲  速度、校正质量流量、压力比和效率分别位于数据文件的第 2-5 列。数据文件的第一行和第二行提供变量名称和单位。例如，使用此格式。  |  |  |  |  |  | | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  | | Data: | `8373.3` | `0.02` | `1.21` | `0.44` | |  | ... | ... | ... | ... | | | `Variable geometry` | - 速度，Spd，单位 rad/s - 校正质量流量，MassFlwRate，单位 kg/s - 齿条位置，RackPos，无量纲 - 压力比，PrsRatio，无量纲 - 效率，Eff，无量纲  在每个齿条位置工况点包含若干测试点的数据。  速度、校正质量流量、齿条位置、压力比和效率分别位于数据文件的第 2-6 列。数据文件的第一行和第二行提供变量名称和单位。例如，使用此格式。  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Name: | Spd | MassFlwRate | RackPos | PrsRatio | Eff | | Unit: | rad/s | kg/s |  |  |  | | Data: | `8373.3` | `0.02` | `1` | `1.21` | `0.44` | |  | ... | ... |  | ... | ... | |    Model-Based Calibration Toolbox 将速度和压力比断点值限制为文件中的最大值。  要筛选或编辑数据，请选择 **Edit in Application**。Model-Based Calibration Toolbox Data Editor 打开。 |
| 生成响应模型 | Model-Based Calibration Toolbox 拟合导入的数据并生成响应模型。  | **Turbine type** | 描述 | | --- | --- | | `Fixed geometry` | | 数据 | 响应模型 | | --- | --- | | 校正质量流量 | *Modeling and Control of Engines and Drivelines*2 中描述的平方根涡轮流量模型 | | 效率 | *Modeling and Control of Engines and Drivelines*2 中描述的叶片速度比 (BSR) 模型 | | | `Variable geometry` | Model-Based Calibration Toolbox 使用逐点测试计划拟合数据。对于每个齿条位置，该模块使用这些响应模型拟合校正质量流量和效率数据。  | 数据 | 响应模型 | | --- | --- | | 校正质量流量 | *Modeling and Control of Engines and Drivelines*2 中描述的平方根涡轮流量模型 | | 效率 | *Modeling and Control of Engines and Drivelines*2 中描述的叶片速度比 (BSR) 模型 | |  要评估或调整响应模型拟合，请选择 **Edit in Application**。Model-Based Calibration Toolbox Model Browser 打开。有关详细信息，请参阅 Model Assessment (Model-Based Calibration Toolbox)。 |
| 生成校准 | Model-Based Calibration Toolbox 校准响应模型并生成校准表。  | **Turbine type** | 描述 | | --- | --- | | `Fixed geometry` | Model-Based Calibration Toolbox 使用响应模型生成校正质量流量和效率表。 | | `Variable geometry` | Model-Based Calibration Toolbox 为每个齿条位置填充校正质量流量和效率表。然后，Model-Based Calibration Toolbox 将依赖于齿条位置的表合并为校正质量流量和效率的 3D 查找表。 |  要评估或调整校准，请选择 **Edit in Application**。Model-Based Calibration Toolbox CAGE Browser 打开。有关详细信息，请参阅 Calibration Lookup Tables (Model-Based Calibration Toolbox)。 |
| 更新模块参数 | 使用校准更新这些校正质量流量和效率参数。  | **Turbine type** | 参数 | | --- | --- | | `Fixed geometry` | - **Corrected mass flow rate table,   mdot\_corrfx\_tbl** - **Efficiency table,   eta\_turbfx\_tbl** - **Corrected speed breakpoints,   w\_corrfx\_bpts1** - **Pressure ratio breakpoints,   Pr\_fx\_bpts2** | | `Variable geometry` | - **Corrected mass flow rate table,   mdot\_corrvr\_tbl** - **Efficiency table,   eta\_turbvr\_tbl** - **Corrected speed breakpoints,   w\_corrvr\_bpts2** - **Pressure ratio breakpoints,   Pr\_vr\_bpts2** - **Rack breakpoints,   L\_rack\_bpts3** | |

### 热力学

该模块使用这些方程来建模热力学。

| 计算 | 方程 |
| --- | --- |
| 正向质量流量 | m˙turb>0  p01=pinlet  p02=poutlet  T01=Tinlet  h01=hinlet |
| 热力学第一定律 | W˙turb=m˙turbcp(T01−T02) |
| 等熵效率 | ηturb=h01−h02h01−h02s=T01−T02T01−T02s |
| 等熵出口温度，假设理想气体和恒定比热 | T02s=T01(p02p01)γ−1γ |
| 比热比 | γ=cpcp−R |
| 出口温度 | T02=T01+ηturbT01{1−(p02p01)γ−1γ} |
| 热流量 | qin,turb=m˙turbcpT01  qout,turb=m˙turbcpT02 |
| 驱动轴扭矩 | τturb=W˙turbω |

方程使用这些变量。

|  |  |
| --- | --- |
| pinlet,p01 | 入口控制体积总压力 |
| Tinlet, T01 | 入口控制体积总温度 |
| hinlet, h01 | 入口控制体积总比焓 |
| poutlet, p02 | 出口控制体积总压力 |
| Toutlet | 出口控制体积总温度 |
| houtlet | 出口控制体积总比焓 |
| W˙turb | 驱动轴功率 |
| T02 | 离开涡轮的温度 |
| h02 | 出口总比焓 |
| m˙turb | 涡轮质量流量 |
| qin,turb | 涡轮入口热流量 |
| qout,turb | 涡轮出口热流量 |
| ηturb | 涡轮等熵效率 |
| T02s | 等熵出口总温度 |
| h02s | 等熵出口总比焓 |
| R | 理想气体常数 |
| cp | 定压比热 |
| γ | 比热比 |
| τturb | 驱动轴扭矩 |

### 性能查找表

该模块基于这些方程实现查找表。

| 计算 | 方程 | |
| --- | --- | --- |
| 校正质量流量 | m˙corr=m˙turbT01/Trefp01/pref | |
| 校正转速 | ωcorr=ωT01/Tref | |
| 压力膨胀比 | pr=p01p02 | |
| 效率查找表 | 固定几何 (3-D 表) | ηturbfx,tbl=f(ωcorr,pr) |
| 可变几何 (3-D 表) | ηturbvr,tbl=f(ωcorr,pr,Lrack) |
| 校正质量流量查找表 | 固定几何 (3-D 表) | m˙corrfx,tbl=f(ωcorr,pr) |
| 可变几何 (3-D 表) | m˙corrvr,tbl=f(ωcorr,pr,Lrack) |

方程使用这些变量。

|  |  |
| --- | --- |
| p01 | 入口控制体积总压力 |
| pr | 压力膨胀比 |
| p02 | 出口控制体积总压力 |
| Pref | 查找表参考压力 |
| T01 | 入口控制体积总温度 |
| Tref | 查找表参考温度 |
| m˙turb | 涡轮质量流量 |
| ω | 驱动轴转速 |
| ωcorr | 校正驱动轴转速 |
| Lrack | 可变几何涡轮齿条位置 |
| ηturbfx,tbl | 固定几何的效率 3-D 查找表 |
| m˙corrfx,tbl | 固定几何的校正质量流量 3-D 查找表 |
| ηturbvr,tbl | 可变几何的效率 3-D 查找表 |
| m˙corrvr,tbl | 可变几何的校正质量流量 3-D 查找表 |

### 废气门

为了计算废气门的热流量和质量流量，Turbine 模块使用 Flow Restriction 模块。Flow Restriction 模块使用废气门流通面积。

Awg=AwgpctcmdAwgopen100

方程使用这些变量。

|  |  |
| --- | --- |
| Awgpctcmd | 废气门阀面积百分比命令 |
| Awg | 废气门阀面积 |
| Awgopen | 完全打开时的废气门阀面积 |

### 组合流量

为了表示通过废气门阀和涡轮的流量，该模块使用这些方程。

| 计算 | 方程 | |
| --- | --- | --- |
| 未配置废气门阀的模块 | m˙wg=qwg=0 | |
| 总质量流量 | m˙total=m˙turb+m˙wg | |
| 总热流量 | qinlet=qin,turb+qwg  qoutlet=qout,turb+qwg | |
| 离开废气门阀和涡轮的组合温度 | Toutflw={qoutletm˙totalcpm˙total>m˙threshT02+Toutflw,wg2else | |

该模块使用内部信号 `FlwDir` 来跟踪流动方向。

方程使用这些变量。

|  |  |
| --- | --- |
| m˙total | 通过废气门阀和涡轮的总质量流量 |
| m˙turb | 涡轮质量流量 |
| m˙wg | 通过废气门阀的质量流量 |
| qinlet | 总入口热流量 |
| qoutlet | 总出口热流量 |
| qin,turb | 涡轮入口热流量 |
| qout,turb | 涡轮出口热流量 |
| qwg | 废气门阀热流量 |
| T02 | 离开涡轮的温度 |
| Toutflw | 离开模块的总温度 |
| Toutflw,wg | 离开废气门阀的温度 |
| m˙thresh | 防止除以零的质量流量阈值 |
| cp | 定压比热 |

### 功率核算

对于功率核算，该模块实现这些方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrDriveshft` | 从轴传输的功率 | −W˙turb |
| `PwrHeatFlwIn` | 端口 A 的热流量 | qoutlet |
| `PwrHeatFlwOut` | 端口 B 的热流量 | qoutlet |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrLoss` | 功率损失 | −qinlet−qoutlet+W˙turb |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |

方程使用这些变量。

|  |  |
| --- | --- |
| W˙turb | 驱动轴功率 |
| qoutlet | 总出口热流量 |
| qinlet | 总入口热流量 |
