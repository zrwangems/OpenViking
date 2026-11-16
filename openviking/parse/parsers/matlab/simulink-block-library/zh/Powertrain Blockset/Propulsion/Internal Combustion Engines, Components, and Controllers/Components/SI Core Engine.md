---
type: simulink-block
title: 'SI Core Engine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'sicoreengine'
documentation_source_path: 'ref/sicoreengine.html'
language: zh-CN
chinese_source: worker-translation
---

# SI Core Engine

## 端口

### 输入

### **InjPw** — Fuel injector pulse-width `scalar`

燃油喷射器脉宽，Pwinj，单位为 ms。

### **SpkAdv** — Spark advance `scalar`

点火提前角，*SA*，单位为曲轴转角，上止点前度数（degBTDC）。

#### 依赖关系

要创建此端口，对于 **Torque model** 参数，选择 `Torque Structure`。

### **ICP** — Intake cam phase angle command `scalar`

进气凸轮相位角命令，φICPCMD，单位为 degCrkAdv，或相对于进气相位器驻车位置的曲轴提前角度。

#### 依赖关系

要创建此端口，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **ECP** — Exhaust cam phase angle command `scalar`

排气凸轮相位角命令，φECPCMD，单位为 degCrkRet，或相对于排气相位器驻车位置的曲轴延迟角度。

#### 依赖关系

要创建此端口，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **AmbPrs** — Ambient pressure `scalar`

环境压力，PAmb，单位为 Pa。

#### 依赖关系

要创建此端口，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **EngSpd** — Engine speed `scalar`

发动机转速，*N*，单位为 rpm。

### **Ect** — Engine cooling temperature `scalar`

发动机冷却液温度，*Tcoolant*，单位为 K。

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

### **Intk** — Intake port pressure, temperature, enthalpy, mass fractions two-way connector port

包含上游的总线：

- `Prs` — 压力，单位为 Pa
- `Temp` — 温度，单位为 K
- `Enth` — 比焓，单位为 J/kg
- `MassFrac` — 进气口质量分数，无量纲。进气口处的 EGR 质量流量为已燃气。

  具体来说，是具有这些质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃烧燃料
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 已燃气

### **Exh** — Exhaust port pressure, temperature, enthalpy, mass fractions two-way connector port

包含排气的总线：

- `Prs` — 压力，单位为 Pa
- `Temp` — 温度，单位为 K
- `Enth` — 比焓，单位为 J/kg
- `MassFrac` — 排气口质量分数，无量纲。

  具体来说，是具有这些质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃烧燃料
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 已燃气

### 输出

### **Info** — Bus signal bus

包含这些模块计算的总线信号。

| Signal | | | Description | Variable | Units |
| --- | --- | --- | --- | --- | --- |
| `IntkGasMassFlw` | | | 发动机进气空气质量流量 | m˙air | kg/s |
| `IntkAirMassFlw` | | | 发动机进气口质量流量 | m˙intk | kg/s |
| `NrmlzdAirChrg` | | | 针对最终稳态凸轮相位角校正后的发动机负荷（即归一化气缸空气量） | L | N/A |
| `Afr` | | | 发动机排气口处的空燃比 | AFR | N/A |
| `FuelMassFlw` | | | 进入发动机的燃料流量 | m˙fuel | kg/s |
| `FuelVolFlw` | | | 体积燃料流量 | *Qfuel* | m3/s |
| `ExhManGasTemp` | | | 排气歧管入口处的排气温度 | Texh | K |
| `EngTrq` | | | 发动机制动扭矩 | Tbrake | N·m |
| `EngSpd` | | | 发动机转速 | N | rpm |
| `IntkCamPhase` | | | 进气凸轮相位器角度 | φICP i | 相对于驻车位置的曲轴提前角度 |
| `ExhCamPhase` | | | 排气凸轮相位器角度 | φECP | 相对于驻车位置的曲轴延迟角度 |
| `CrkAng` | | | 发动机曲轴绝对角 | ∫0(360)CpsEngSpd18030dθ  其中 Cps 是每做功冲程的曲轴转数 | 曲轴角度 |
| `EgrPct` | | | EGR 百分比 | *EGRpct* | N/A |
| `EoAir` | | | EO 空气质量流量 | m˙exh | kg/s |
| `EoBrndGas` | | | EO 已燃气质量流量 | *yexh,b* | kg/s |
| `EoHC` | | | EO 碳氢化合物排放质量流量 | *yexh,HC* | kg/s |
| `EoCO` | | | EO 一氧化碳排放质量流量 | *yexh,CO* | kg/s |
| `EoNOx` | | | EO 一氧化氮和二氧化氮排放质量流量 | *yexh,NOx* | kg/s |
| `EoCO2` | | | EO 二氧化碳排放质量流量 | *yexh,CO2* | kg/s |
| `EoPm` | | | EO 颗粒物排放质量流量 | *yexh,PM* | kg/s |
| `CylPrs` | | | 气缸压力 | N/A | Pa |
| `EngTrqCrk` | | | 基于曲轴角度的发动机扭矩 | N/A | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrIntkHeatFlw` | 进气热流量 | m˙intkhintk | W |
| `PwrExhHeatFlw` | 排气热流量 | −m˙exhhexh | W |
| `PwrCrkshft` | 曲轴功率 | −Tbrakeω | W |
| `PwrNotTrnsfrd` | `PwrFuel` | 燃料输入功率 | m˙fuelLHV | W |
| `PwrLoss` | 对于 **Torque model** 设置为 `Simple Torque Lookup`：所有损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh | W |
| `PwrFricLoss` | 对于 **Torque model** 设置为 `Torque Structure`：摩擦损失 | −Tfricω | W |
| `PwrPumpLoss` | 对于 **Torque model** 设置为 `Torque Structure`：泵气损失 | −Tpumpω | W |
| `PwrHeatTrnsfrLoss` | 对于 **Torque model** 设置为 `Torque Structure`：传热损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh+Tfricω+Tpumpω | W |
| `PwrStored` | *未使用* | | | |

### **EngTrq** — Engine brake torque `scalar`

发动机制动扭矩，Tbrake，单位为 N·m。

### **Intk** — Intake port mass flow rate, heat flow rate, temperature, mass fraction two-way connector port

包含以下内容的总线：

- `MassFlwRate` — 进气口质量流量，单位为 kg/s
- `HeatFlwRate` — 进气口热流量，单位为 J/s
- `Temp` — 进气口温度，单位为 K
- `MassFrac` — 进气口质量分数，无量纲。

  具体来说，是具有这些质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃烧燃料
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 已燃气

### **Exh** — Exhaust port mass flow rate, heat flow rate, temperature, mass fraction two-way connector port

包含以下内容的总线：

- `MassFlwRate` — 排气口质量流量，单位为 kg/s
- `HeatFlwRate` — 排气热流量，单位为 J/s
- `Temp` — 排气温度，单位为 K
- `MassFrac` — 排气口质量分数，无量纲。

  具体来说，是具有这些质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃烧燃料
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 已燃气

## 参数

#### 模块选项

### **Air mass flow model** — Select air mass flow model `Dual-Independent Variable Cam Phasing`（默认） | `Simple Speed-Density`

要计算发动机空气质量流量，将 SI 发动机配置为使用以下任一空气流量模型。

| Air Mass Flow Model | Description |
| --- | --- |
| SI Engine Speed-Density Air Mass Flow Model | 使用速度-密度方程计算发动机空气质量流量，将发动机空气质量流量与进气歧管压力和发动机转速关联。对于固定气门机构设计的发动机，可考虑使用此空气流量模型。 |
| SI Engine Dual-Independent Cam Phaser Air Mass Flow Model | 为计算发动机空气质量流量，双独立凸轮相位器模型使用：  - 根据发动机映射测量开发的经验校准参数 - 根据发动机计算机辅助设计（CAD）数据得出的桌面校准参数  与基于使用空气质量流量（MAF）传感器直接测量空气质量流量的典型嵌入式空气质量流量计算相比，此空气流量模型具有以下优势：  - 在双凸轮相位气门机构应用中无需 MAF 传感器 - 在海拔变化时具有合理精度 - 半物理建模方法 - 有界行为 - 适合电子控制单元（ECU）实现的执行时间 - 系统性地开发相对较少的校准参数 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AirMassFlowOptionPopup` |
| **值：** | `Dual-Independent Variable Cam Phasing`（默认） | `Simple Speed-Density` |
| **数据类型：** | `character vector` |

#### 依赖关系

下表汇总了参数依赖关系。

| Air Mass Flow Model | Enables Parameters |
| --- | --- |
| `Dual-Independent Variable Cam Phasing` | **Cylinder volume at intake valve close table, f\_vivc**  **Cylinder volume intake cam phase breakpoints, f\_vivc\_icp\_bpt**  **Cylinder trapped mass correction factor, f\_tm\_corr**  **Normalized density breakpoints, f\_tm\_corr\_nd\_bpt**  **Engine speed breakpoints, f\_tm\_corr\_n\_bpt**  **Air mass flow, f\_mdot\_air**  **Exhaust cam phase breakpoints, f\_mdot\_air\_ecp\_bpt**  **Trapped mass flow breakpoints, f\_mdot\_trpd\_bpt**  **Air mass flow correction factor, f\_mdot\_air\_corr**  **Engine load breakpoints for air mass flow correction, f\_mdot\_air\_corr\_ld\_bpt**  **Engine speed breakpoints for air mass flow correction, f\_mdot\_air\_n\_bpt** |
| `Simple Speed Density` | **Speed-density volumetric efficiency, f\_nv**  **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt**  **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** |

### **Torque model** — Select torque model `Torque Structure`（默认） | `Simple Torque Lookup`

要计算制动扭矩，将 SI 发动机配置为使用以下任一扭矩模型。

| Brake Torque Model | Description |
| --- | --- |
| SI Engine Torque Structure Model | 对于结构化制动扭矩计算，SI 发动机使用内扭矩、摩擦扭矩、最佳点火、点火效率和 lambda 效率的表。  如果在模块 **Torque** 选项卡上选择 **Crank angle pressure and torque**，则可以：  - 基于模型或实验室测试记录的气缸压力随曲轴角变化的函数，在桌面仿真和 HIL 台架上仿真高级闭环发动机控制。 - 仿真由于高频曲轴扭转而导致发动机下游的动力传动系振动。 - 通过使用喷射器脉宽输入，仿真由于稀薄运行或火花塞积垢导致的发动机失火。 - 仿真气缸停用效果（进气和排气门关闭、不喷射燃料）对单个气缸压力、均值空气流量、均值扭矩和基于曲轴角度的扭矩的影响。 - 仿真断油效果对单个气缸压力、均值扭矩和基于曲轴角度的扭矩的影响。 |
| SI Engine Simple Torque Model | 对于简单制动扭矩计算，SI Engine 模块使用作为发动机转速和负荷函数的扭矩查找表映射。 |

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrqOptionPopup` |
| **值：** | `Torque Structure`（默认） | `Simple Torque Lookup` |
| **数据类型：** | `character vector` |

#### 依赖关系

下表汇总了参数依赖关系。

| Torque Model | Enables Parameters |
| --- | --- |
| `Torque Structure` | **Inner torque table, f\_tq\_inr**  **Friction torque table, f\_tq\_fric**  **Engine temperature modifier on friction torque, f\_fric\_temp\_mod**  **Engine temperature modifier breakpoints, f\_fric\_temp\_bpt**  **Pumping work table, f\_tq\_pump**  **Optimal spark table, f\_sa\_opt**  **Inner torque load breakpoints, f\_tq\_inr\_l\_bpt**  **Inner torque speed breakpoints, f\_tq\_inr\_n\_bpt**  **Spark efficiency table, f\_m\_sa**  **Spark retard from optimal, f\_del\_sa\_bpt**  **Lambda efficiency, f\_m\_lam**  **Lambda breakpoints, f\_m\_lam\_bpt** |
| `Simple Torque Lookup` | **Torque table, f\_tq\_nl**  **Torque table load breakpoints, f\_tq\_nl\_l\_bpt**  **Torque table speed breakpoints, f\_tq\_nl\_n\_bpt** |

#### 空气

### **Number of cylinders, NCyl** — Engine cylinders `4`（默认） | `scalar`

发动机气缸数，Ncyl。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NCyl` |
| **值：** | `4`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Crank revolutions per power stroke, Cps** — Revolutions per stroke `2`（默认） | `scalar`

每做功冲程的曲轴转数，Cps，单位为 rev/stroke。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cps` |
| **值：** | `2`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Total displaced volume, Vd** — Volume `0.0015`（默认） | `scalar`

排量，Vd，单位为 m^3。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.0015`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Ideal gas constant air, Rair** — Constant `287`（默认） | `scalar`

理想气体常数，Rair，单位为 J/(kg·K)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rair` |
| **值：** | `287`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Air standard pressure, Pstd** — Pressure `101325`（默认） | `scalar`

标准空气压力，Pstd，单位为 Pa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pstd` |
| **值：** | `101325`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Air standard temperature, Tstd** — Temperature `293.15`（默认） | `scalar`

标准空气温度，Tstd，单位为 K。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tstd` |
| **值：** | `293.15`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Speed-density volumetric efficiency, f\_nv** — Lookup table `array`

发动机容积效率查找表 fηv 是进气歧管绝对压力和发动机转速的函数

ηv=fηv(MAP,N)

其中：

- ηv 是发动机容积效率，无量纲。
- *MAP* 是进气歧管绝对压力，单位为 KPa。
- *N* 是发动机转速，单位为 rpm。

发动机容积效率与进气歧管绝对压力和发动机转速的 3D 图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Simple Speed-Density`。

### **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt** — Breakpoints `[31 40.6428571428571 50.2857142857143 59.9285714285714 69.5714285714286 79.2142857142857 88.8571428571429 98.5 108.142857142857 117.785714285714 127.428571428571 137.071428571429 146.714285714286 156.357142857143 166]`（默认） | `array`

用于速度-密度容积效率查找表的进气歧管压力断点，单位为 KPa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_prs_bpt` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Simple Speed-Density`。

### **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]`（默认） | `array`

用于速度-密度容积效率查找表的发动机转速断点，单位为 rpm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_n_bpt` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Simple Speed-Density`。

### **Cylinder volume at intake valve close table, f\_vivc** — 2-D lookup table `array`

进气门关闭（IVC）时的气缸容积表 fVivc 是进气凸轮相位器角度的函数

VIVC=fVivc(φICP)

其中：

- VIVC 是 IVC 时的气缸容积，单位为 L。
- φICP 是相对于进气相位器驻车位置的曲轴提前角度中的进气凸轮相位器角度。

气缸容积与进气凸轮相位器角度的图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_vivc` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Cylinder volume intake cam phase breakpoints, f\_vivc\_icp\_bpt** — Breakpoints `[0 2.6316 5.2632 7.8947 10.5263 13.1579 15.7895 18.4211 21.0526 23.6842 26.3158 28.9474 31.5789 34.2105 36.8421 39.4737 42.1053 44.7368 47.3684 50]`（默认） | `vector`

气缸容积进气凸轮相位断点，单位为 L。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_vivc_icp_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Cylinder trapped mass correction factor, f\_tm\_corr** — Lookup table `array`

截留质量修正因子表 fTMcorr 是归一化密度和发动机转速的函数

TMcorr=fTMcorr(ρnorm, N)

其中：

- TMcorr 是截留质量修正乘数，无量纲。
- ρnorm 是归一化密度，无量纲。
- *N* 是发动机转速，单位为 rpm。

截留质量修正乘数与归一化密度和发动机转速的 3D 图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tm_corr` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Normalized density breakpoints, f\_tm\_corr\_nd\_bpt** — Breakpoints `[0.3 0.38947 0.47895 0.56842 0.65789 0.74737 0.83684 0.92632 1.0158 1.1053 1.1947 1.2842 1.3737 1.4632 1.5526 1.6421 1.7316 1.8211 1.9105 2]`（默认） | `vector`

归一化密度断点，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tm_corr_nd_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Engine speed breakpoints, f\_tm\_corr\_n\_bpt** — Breakpoints `[750 973.6842 1197.3684 1421.0526 1644.7368 1868.4211 2092.1053 2315.7895 2539.4737 2763.1579 2986.8421 3210.5263 3434.2105 3657.8947 3881.5789 4105.2632 4328.9474 4552.6316 4776.3158 5000]`（默认） | `vector`

发动机转速断点，单位为 rpm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tm_corr_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Intake mass flow, f\_mdot\_intk** — Lookup table `array`

相位器进气质量流量模型查找表是排气凸轮相位器角度和截留空气质量流量的函数

m˙intkideal=fintkideal(φECP,TMflow)

其中：

- m˙intkideal 是任意凸轮相位器角度下的发动机进气口质量流量，单位为 g/s。
- φECP 是相对于排气相位器驻车位置的曲轴延迟角度中的排气凸轮相位器角度。
- TMflow 是在当前发动机转速下相当于校正后截留质量的流量，单位为 g/s。

空气质量流量与排气凸轮相位器角度和流量当量的 3D 图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_intk` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Exhaust cam phase breakpoints, f\_mdot\_air\_ecp\_bpt** — Breakpoints `[0 2.6316 5.2632 7.8947 10.5263 13.1579 15.7895 18.4211 21.0526 23.6842 26.3158 28.9474 31.5789 34.2105 36.8421 39.4737 42.1053 44.7368 47.3684 50]`（默认） | `vector`

用于空气质量流量查找表的排气凸轮相位器断点，单位为相对于驻车位置的曲轴延迟角度。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_ecp_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Trapped mass flow breakpoints, f\_mdot\_trpd\_bpt** — Breakpoints `[0 5.7895 11.5789 17.3684 23.1579 28.9474 34.7368 40.5263 46.3158 52.1053 57.8947 63.6842 69.4737 75.2632 81.0526 86.8421 92.6316 98.4211 104.2105 110]`（默认） | `vector`

用于空气质量流量查找表的截留质量流量断点，单位为 g/s。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_trpd_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Air mass flow correction factor, f\_mdot\_air\_corr** — Lookup table `array`

进气空气质量流量修正查找表 faircorr 是理想负荷和发动机转速的函数

m˙air=m˙intkidealfaircorr(Lideal,N)

其中：

- Lideal 是任意凸轮相位器角度下的发动机负荷（归一化气缸空气量），未针对最终稳态凸轮相位器角度校正，无量纲。
- *N* 是发动机转速，单位为 rpm。
- m˙air 是稳态凸轮相位器角度下的发动机进气空气质量流量最终修正，单位为 g/s。
- m˙intkideal 是任意凸轮相位器角度下的发动机进气口质量流量，单位为 g/s。

发动机进气空气质量流量最终修正与发动机负荷和发动机转速的 3D 图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_corr` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Engine load breakpoints for air mass flow correction, f\_mdot\_air\_corr\_ld\_bpt** — Breakpoints `vector`

用于空气质量流量最终修正的发动机负荷断点，无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_corr_ld_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

### **Engine speed breakpoints for air mass flow correction, f\_mdot\_air\_n\_bpt** — Breakpoints `vector`

用于空气质量流量最终修正的发动机转速断点，单位为 rpm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_mdot_air_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Air mass flow model** 参数，选择 `Dual-Independent Variable Cam Phasing`。

#### 扭矩

### **Torque table, f\_tq\_nl** — Lookup table `[L x N] array`

对于简单扭矩查找表模型，SI 发动机使用作为发动机转速和负荷函数的查找表映射，Tbrake=fTnL(L,N)，其中：

- Tbrake 是考虑点火提前角、AFR 和摩擦影响后的发动机制动扭矩，单位为 N·m。
- *L* 是发动机负荷，作为归一化气缸空气量，无量纲。
- *N* 是发动机转速，单位为 rpm。

考虑点火提前角后的发动机制动扭矩与发动机负荷和发动机转速的 3D 图

简单扭矩查找模型假设校准具有负扭矩值，以指示不点火发动机负荷（L）与转速（N）条件。校准表（L-by-N）在第一表行（1-by-N）中包含不点火数据。当输送到发动机的燃料为零时，模型使用第一表行（1-by-N）中在 100 AFR 或以上的数据。100 AFR 由断油或无法发生燃烧的极稀运行产生。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Simple Torque Lookup`。

### **Torque table load breakpoints, f\_tq\_nl\_l\_bpt** — Breakpoints `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认） | `vector` | `[1 x L] vector`

发动机负荷断点，*L*，无量纲。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Simple Torque Lookup`。

### **Torque table speed breakpoints, f\_tq\_nl\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]`（默认） | `vector` | `[1 x N] vector`

发动机转速断点，*N*，单位为 rpm。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Simple Torque Lookup`。

### **Crank angle pressure and torque** — Enable Crank angle signals `off`（默认） | `on`

如果在模块 **Torque** 选项卡上选择 **Crank angle pressure and torque**，则可以：

- 基于模型或实验室测试记录的气缸压力随曲轴角变化的函数，在桌面仿真和 HIL 台架上仿真高级闭环发动机控制。
- 仿真由于高频曲轴扭转而导致发动机下游的动力传动系振动。
- 通过使用喷射器脉宽输入，仿真由于稀薄运行或火花塞积垢导致的发动机失火。
- 仿真气缸停用效果（进气和排气门关闭、不喷射燃料）对单个气缸压力、均值空气流量、均值扭矩和基于曲轴角度的扭矩的影响。
- 仿真断油效果对单个气缸压力、均值扭矩和基于曲轴角度的扭矩的影响。

#### 依赖关系

要启用此参数，将 **Torque model** 设置为 `Torque Structure`。

### **Cylinder pressure, f\_crk\_prs** — Cylinder pressure table `L x M x N` array

气缸压力表 *Prs*，作为转速 *N*、负荷 *L* 和曲轴角 *M* 的函数，单位为 Pa。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。选择 **Crank angle pressure and torque**。

### **Brake torque, f\_crk\_btq** — Brake torque table `L x M x N` array

制动扭矩表 *Tbrake*，作为转速 *N*、负荷 *L* 和曲轴角 *M* 的函数，单位为 N·m。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。选择 **Crank angle pressure and torque**。

### **Speed breakpoints, f\_crk\_n\_bpt** — Speed breakpoints `[750 5000]`（默认） | `1 x N` vector

转速断点，*N*，单位为 rpm。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。选择 **Crank angle pressure and torque**。

### **Load breakpoints, f\_crk\_l\_bpt** — Load breakpoints `[0.2 1.4]`（默认） | `1 x L` vector

负荷断点，*L*。无量纲。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。选择 **Crank angle pressure and torque**。

### **Crank angle breakpoints, f\_crk\_ang\_bpt** — Crank angle breakpoints `[60 660]`（默认） | `1 x M` vector

曲轴角断点，*M*，单位为 deg。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。选择 **Crank angle pressure and torque**。

### **TDC compression angles by cylinder, f\_crk\_tdc\_ang** — TDC compression angles by cylinder `[0 540 180 360]`（默认） | vector

按气缸的压缩上止点（TDC）角度，单位为 deg。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。选择 **Crank angle pressure and torque**。

### **Inner torque table, f\_tq\_inr** — Lookup table `array`

内扭矩查找表 fTqinr 是发动机转速和发动机负荷的函数，Tqinr=fTqinr(L,N)，其中：

- Tqinr 是基于总指示平均有效压力的内扭矩，单位为 N·m。
- *L* 是在任意凸轮相位器角度下、针对最终稳态凸轮相位器角度校正后的发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

基于总指示平均有效压力的内扭矩与任意凸轮相位器角度下的发动机负荷和发动机转速的 3D 图

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Friction torque table, f\_tq\_fric** — Lookup table `array`

摩擦扭矩查找表 fTfric 是发动机转速和发动机负荷的函数，Tfric=fTfric(L,N)，其中：

- Tfric 是内扭矩的摩擦扭矩偏移，单位为 N·m。
- *L* 是在任意凸轮相位器角度下、针对最终稳态凸轮相位器角度校正后的发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

内扭矩的摩擦扭矩偏移与任意凸轮相位器角度下的发动机负荷和发动机转速的 3D 图

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Engine temperature modifier on friction torque, f\_fric\_temp\_mod** — Lookup table `[3.96 3.22 2.56 2.26 2.11 2 1.9 1.83 1.76 1.7 1.65 1.6 1.55 1.49 1.44 1.41 1.38 1.35 1.32 1.3 1.27 1.25 1.24 1.21 1.2 1.18 1.16 1.15 1.13 1.12 1.11 1.1 1.09 1.08 1.07 1.06 1.05 1.05 1.04 1.03 1.02 1.02 1.01 1.01 1 1 1 0.999 0.997 0.995 0.993 0.991 0.989 0.987]`（默认） | `vector` | `vector`

摩擦扭矩上的发动机温度修正因子，*ƒfric,temp*，无量纲。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Engine temperature modifier breakpoints, f\_fric\_temp\_bpt** — Breakpoints `[274 276 278 280 282 284 286 288 290 292 294 296 298 300 302 304 306 308 310 312 314 316 318 320 322 324 326 328 330 332 334 336 338 340 342 344 346 348 350 352 354 356 358 360 362 364 366 368 370 372 374 376 378 380]`（默认） | `vector` | `vector`

发动机温度修正因子断点，单位为 K。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Pumping torque table, f\_tq\_pump** — Lookup table `array`

泵气扭矩查找表 *ƒTpump* 是发动机负荷和发动机转速的函数，`Tpump=ƒTpump(L,N)`，其中：

- *Tpump* 是泵气扭矩，单位为 N·m。
- *L* 是发动机负荷，作为归一化气缸空气量，无量纲。
- *N* 是发动机转速，单位为 rpm。

泵气扭矩与发动机负荷和发动机转速的 3D 图

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Optimal spark table, f\_sa\_opt** — Lookup table `array`

最佳点火查找表 fSAopt 是发动机转速和发动机负荷的函数，SAopt=fSAopt(L,N)，其中：

- *SAopt* 是在化学计量空燃比（AFR）下为获得最大内扭矩的最佳点火提前正时，单位为 deg。
- *L* 是在任意凸轮相位器角度下、针对最终稳态凸轮相位器角度校正后的发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

在化学计量空燃比（AFR）下为获得最大内扭矩的最佳点火提前正时与发动机负荷和发动机转速的 3D 图

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Inner torque load breakpoints, f\_tq\_inr\_l\_bpt** — Breakpoints `[0.2 0.28571 0.37143 0.45714 0.54286 0.62857 0.71429 0.8 0.88571 0.97143 1.0571 1.1429 1.2286 1.3143 1.4]`（默认） | `vector`

内扭矩负荷断点，无量纲。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Inner torque speed breakpoints, f\_tq\_inr\_n\_bpt** — Breakpoints `[750 1053.5714 1357.1429 1660.7143 1964.2857 2267.8571 2571.4286 2875 3178.5714 3482.1429 3785.7143 4089.2857 4392.8571 4696.4286 5000]`（默认） | `vector`

内扭矩转速断点，单位为 rpm。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Spark efficiency table, f\_m\_sa** — Lookup table `array`

点火效率查找表 fMsa 是相对于最佳点火的点火延迟的函数

Msa=fMsa(ΔSA) ΔSA=SAopt−SA

其中：

- Msa 是点火延迟效率乘数，无量纲。
- ΔSA 是相对于最佳点火提前角的点火延迟正时距离，单位为 deg。

点火延迟效率与点火延迟正时距离的关系图

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Spark retard from optimal, f\_del\_sa\_bpt** — Breakpoints `[0 0.75 1.5 2.25 3 3.75 4.5 5.25 6 6.75 7.5 8.25 9 9.75 10.5 11.25 12 12.75 13.5 14.25 15 15.75 16.5 17.25 18 18.75 19.5 20.25 21 21.75 22.5 23.25 24 24.75 25.5 26.25 27 27.75 28.5 29.25 30 30.75 31.5 32.25 33 33.75 34.5 35.25 36 36.75 37.5 38.25 39 39.75 40.5 41.25 42 42.75 43.5 44.25 45 45.75 46.5 47.25 48]`（默认） | `vector`

相对于最佳内扭矩正时的点火延迟断点，单位为 deg。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Lambda efficiency, f\_m\_lam** — Lookup table `array`

lambda 效率查找表 fMλ 是 lambda 的函数，Mλ=fMλ(λ)，其中：

- Mλ 是用于考虑空燃比（AFR）影响的内扭矩 lambda 乘数，无量纲。
- λ 是 lambda，即 AFR 相对于化学计量燃料 AFR 归一化，无量纲。

lambda 乘数与 lambda 的关系图

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

### **Lambda breakpoints, f\_m\_lam\_bpt** — Breakpoints `[0.65 0.7 0.75 0.8 0.85 0.9 0.95 1 1.05 1.1]`（默认） | `vector`

lambda 对内扭矩影响的 lambda 断点，无量纲。

#### 依赖关系

要启用此参数，对于 **Torque model** 参数，选择 `Torque Structure`。

#### 排气

### **Exhaust temperature table, f\_t\_exh** — Lookup table `array`

排气温度查找表 fTexh 是发动机负荷和发动机转速的函数

Texh=fTexh(L,N)

其中：

- *Texh* 是发动机排气温度，单位为 K。
- *L* 是归一化气缸空气量或发动机负荷，无量纲。
- *N* 是发动机转速，单位为 rpm。

发动机排气温度与发动机转速和发动机负荷的 3D 图

### **Load breakpoints, f\_t\_exh\_l\_bpt** — Breakpoints `[0.2 0.275 0.35 0.425 0.5 0.575 0.65 0.725 0.8 0.875 0.95 1.025 1.1 1.175 1.25]`（默认） | `vector`

用于排气温度查找表的发动机负荷断点，无量纲。

### **Speed breakpoints, f\_t\_exh\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]`（默认） | `vector`

用于排气温度查找表的发动机转速断点，单位为 rpm。

### **Exhaust gas specific heat at constant pressure, cp\_exh** — Specific heat `1005`（默认） | `scalar`

排气气体比热，Cpexh，单位为 J/(kg·K)。

### **CO2 mass fraction table, f\_CO2\_frac** — Carbon dioxide (CO2) emission lookup table `array`

SI Core Engine CO2 排放质量分数查找表是发动机扭矩和发动机转速的函数，*CO2 Mass Fraction* = ƒ(*Speed*, *Torque*)，其中：

- *CO2 Mass Fraction* 是 CO2 排放质量分数，无量纲。
- *Speed* 是发动机转速，单位为 rpm。
- *Torque* 是发动机扭矩，单位为 N·m。

CO2 排放质量分数与发动机转速和发动机扭矩的 3D 图

#### 依赖关系

要启用此参数，在 **Exhaust** 选项卡上选择 **CO2**。

### **CO mass fraction table, f\_CO\_frac** — Carbon monoxide (CO) emission lookup table `array`

SI Core Engine CO 排放质量分数查找表是发动机扭矩和发动机转速的函数，*CO Mass Fraction* = ƒ(*Speed*, *Torque*)，其中：

- *CO Mass Fraction* 是 CO 排放质量分数，无量纲。
- *Speed* 是发动机转速，单位为 rpm。
- *Torque* 是发动机扭矩，单位为 N·m。

CO 排放质量分数与发动机转速和发动机扭矩的 3D 图

#### 依赖关系

要启用此参数，在 **Exhaust** 选项卡上选择 **CO**。

### **HC mass fraction table, f\_HC\_frac** — Hydrocarbon (HC) emission lookup table `array`

SI Core Engine HC 排放质量分数查找表是发动机扭矩和发动机转速的函数，*HC Mass Fraction* = ƒ(*Speed*, *Torque*)，其中：

- *HC Mass Fraction* 是 HC 排放质量分数，无量纲。
- *Speed* 是发动机转速，单位为 rpm。
- *Torque* 是发动机扭矩，单位为 N·m。

HC 排放质量分数与发动机转速和发动机扭矩的 3D 图

#### 依赖关系

要启用此参数，在 **Exhaust** 选项卡上选择 **HC**。

### **NOx mass fraction table, f\_NOx\_frac** — Nitric oxide and nitrogen dioxide (NOx) emission lookup table `array`

SI Core Engine NOx 排放质量分数查找表是发动机扭矩和发动机转速的函数，*NOx Mass Fraction* = ƒ(*Speed*, *Torque*)，其中：

- *NOx Mass Fraction* 是 NOx 排放质量分数，无量纲。
- *Speed* 是发动机转速，单位为 rpm。
- *Torque* 是发动机扭矩，单位为 N·m。

NOx 排放质量分数与指令发动机扭矩和发动机转速的 3D 图

#### 依赖关系

要启用此参数，在 **Exhaust** 选项卡上选择 **NOx**。

### **PM mass fraction table, f\_PM\_frac** — Particulate matter (PM) emission lookup table `array`

SI Core Engine PM 排放质量分数查找表是发动机扭矩和发动机转速的函数，其中：

- *PM* 是 PM 排放质量分数，无量纲。
- *Speed* 是发动机转速，单位为 rpm。
- *Torque* 是发动机扭矩，单位为 N·m。

#### 依赖关系

要启用此参数，在 **Exhaust** 选项卡上选择 **PM**。

### **Engine speed breakpoints, f\_exhfrac\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]`（默认） | `vector`

用于排放质量分数查找表的发动机转速断点，单位为 rpm。

#### 依赖关系

要启用此参数，在 **Exhaust** 选项卡上选择 **CO2**、**CO**、**NOx**、**HC** 或 **PM**。

### **Engine torque breakpoints, f\_exhfrac\_trq\_bpt** — Breakpoints `[0 15 26.4285714285714 37.8571428571429 49.2857142857143 60.7142857142857 72.1428571428571 83.5714285714286 95 106.428571428571 117.857142857143 129.285714285714 140.714285714286 152.142857142857 163.571428571429 175]`（默认） | `vector`

用于排放质量分数查找表的发动机扭矩断点，单位为 N·m。

#### 依赖关系

要启用此参数，在 **Exhaust** 选项卡上选择 **CO2**、**CO**、**NOx**、**HC** 或 **PM**。

#### 燃料

### **Injector slope, Sinj** — Slope `6.45161290322581`（默认） | `scalar`

燃油喷射器斜率，Sinj，mg/ms。

### **Stoichiometric air-fuel ratio, afr\_stoich** — Air-fuel ratio `14.6`（默认） | `scalar`

空燃比，AFR。

### **Fuel lower heating value, fuel\_lhv** — Heating value `46e6`（默认） | `scalar`

燃料低热值，*LHV*，单位为 J/kg。

### **Fuel specific gravity, fuel\_sg** — Specific gravity `0.745`（默认） | `scalar`

燃料比重，*Sgfuel*，无量纲。

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Core Engine

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

火花点火发动机，从进气口到排气口

SI Core Engine 模块实现从进气口到排气口的火花点火（SI）发动机。该模块可用于更大的车辆模型、硬件在环（HIL）发动机控制设计，或车辆级燃油经济性和性能仿真。

SI Core Engine 模块计算：

- 制动扭矩
- 燃料流量
- 端口气体质量流量，包括排气再循环（EGR）
- 空燃比（AFR）
- 排气温度和排气质量流量
- 发动机出口（EO）排放：

  - 碳氢化合物（HC）
  - 一氧化碳（CO）
  - 一氧化氮和二氧化氮（NOx）
  - 二氧化碳（CO2）
  - 颗粒物（PM）

### 空气质量流量

要计算发动机空气质量流量，将 SI 发动机配置为使用以下任一空气质量流量模型。

| Air Mass Flow Model | Description |
| --- | --- |
| SI Engine Speed-Density Air Mass Flow Model | 使用速度-密度方程计算发动机空气质量流量，将发动机空气质量流量与进气歧管压力和发动机转速关联。对于固定气门机构设计的发动机，可考虑使用此空气质量流量模型。 |
| SI Engine Dual-Independent Cam Phaser Air Mass Flow Model | 为计算发动机空气质量流量，双独立凸轮相位器模型使用：  - 根据发动机映射测量开发的经验校准参数 - 根据发动机计算机辅助设计（CAD）数据得出的桌面校准参数  与基于使用空气质量流量（MAF）传感器直接测量空气质量流量的典型嵌入式空气质量流量计算相比，此空气质量流量模型具有以下优势：  - 在双凸轮相位气门机构应用中无需 MAF 传感器 - 在海拔变化时具有合理精度 - 半物理建模方法 - 有界行为 - 适合电子控制单元（ECU）实现的执行时间 - 系统性地开发相对较少的校准参数 |

### 制动扭矩

要计算制动扭矩，将 SI 发动机配置为使用以下任一扭矩模型。

| Brake Torque Model | Description |
| --- | --- |
| SI Engine Torque Structure Model | 对于结构化制动扭矩计算，SI 发动机使用内扭矩、摩擦扭矩、最佳点火、点火效率和 lambda 效率的表。  如果在模块 **Torque** 选项卡上选择 **Crank angle pressure and torque**，则可以：  - 基于模型或实验室测试记录的气缸压力随曲轴角变化的函数，在桌面仿真和 HIL 台架上仿真高级闭环发动机控制。 - 仿真由于高频曲轴扭转而导致发动机下游的动力传动系振动。 - 通过使用喷射器脉宽输入，仿真由于稀薄运行或火花塞积垢导致的发动机失火。 - 仿真气缸停用效果（进气和排气门关闭、不喷射燃料）对单个气缸压力、均值空气流量、均值扭矩和基于曲轴角度的扭矩的影响。 - 仿真断油效果对单个气缸压力、均值扭矩和基于曲轴角度的扭矩的影响。 |
| SI Engine Simple Torque Model | 对于简单制动扭矩计算，SI Engine 模块使用作为发动机转速和负荷函数的扭矩查找表映射。 |

### 燃料流量

要计算燃料流量，SI Core Engine 模块使用燃油喷射器特性和燃油喷射器脉宽。

m˙fuel=NSinjPwinjNcylCps(60smin)(1000mgg)

要计算高保真模型的燃油经济性，模块使用体积燃料流量。

Qfuel=m˙fuel(1000kgm3)Sgfuel

该方程使用这些变量。

|  |  |
| --- | --- |
| m˙fuel | 燃料质量流量，g/s |
| ω | 发动机转速，rad/s |
| Cps | 每做功冲程的曲轴转数，rev/stroke |
| Sinj | 燃油喷射器斜率，mg/ms |
| Pwinj | 燃油喷射器脉宽，ms |
| Ncyl | 发动机气缸数 |
| *N* | 发动机转速，rpm |
| *Sgfuel* | 燃料比重 |
| *Qfuel* | 体积燃料流量 |

模块使用内部信号 `FlwDir` 跟踪流动方向。

### 空燃比

要计算空燃比（AFR），CI Core Engine 和 SI Core Engine 模块实现此方程。

AFR=m˙airm˙fuel

CI Core Engine 使用此方程计算相对 AFR。

λ=AFRAFRs

要计算排气再循环（EGR），模块实现此方程。该计算将 EGR 表示为总进气口流量的百分比。

EGRpct=100m˙intk,bm˙intk=100yintk,b

这些方程使用这些变量。

|  |  |
| --- | --- |
| AFR | 空燃比 |
| *AFRs* | 化学计量空燃比 |
| m˙intk | 发动机空气质量流量 |
| m˙fuel | 燃料质量流量 |
| λ | 相对 AFR |
| *yintk,b* | 进气已燃质量分数 |
| *EGRpct* | EGR 百分比 |
| m˙intk,b | 再循环已燃气质量流量 |

### 排气

模块计算：

- 排气温度
- 排气气体比焓
- 排气质量流量
- 发动机出口（EO）排放：

  - 碳氢化合物（HC）
  - 一氧化碳（CO）
  - 一氧化氮和二氧化氮（NOx）
  - 二氧化碳（CO2）
  - 颗粒物（PM）

排气温度决定比焓。

hexh=CpexhTexh

排气质量流量是进气口空气质量和燃料质量流量之和。

m˙exh=m˙intake+m˙fuel

要计算排放，模块将排放质量分数乘以排气质量流量。为确定排放质量分数，模块使用作为发动机扭矩和转速函数的查找表。

yexh,i=fi_frac(Tbrake,N)m˙exh,i=m˙exhyexh,i

进入进气口的空气和燃料比例、喷射燃料和化学计量 AFR 决定离开排气的空气质量分数。

yexh,air=max[yin,air−m˙fuel+yin,fuelm˙intakem˙fuel+m˙intakeAFRs]

如果发动机在化学计量或燃料过浓 AFR 下运行，则没有空气离开排气。未燃烧碳氢化合物和已燃气构成排气气体的剩余部分。此方程确定排气已燃质量分数。

yexh,b=max[(1−yexh,air−yexh,HC),0]

这些方程使用这些变量。

|  |  |
| --- | --- |
| Texh | 发动机排气温度 |
| hexh | 排气歧管入口比焓 |
| Cpexh | 排气气体比热 |
| m˙intk | 进气口空气质量流量 |
| m˙fuel | 燃料质量流量 |
| m˙exh | 排气质量流量 |
| yin,fuel | 进气燃料质量分数 |
| *yexh,i* | 对于 i = CO2、CO、HC、NOx、空气、已燃气和 PM 的排气质量分数 |
| m˙exh,i | 对于 i = CO2、CO、HC、NOx、空气、已燃气和 PM 的排气质量流量 |
| *Tbrake* | 发动机制动扭矩 |
| *N* | 发动机转速 |
| *yexh,air* | 排气空气质量分数 |
| *yexh,b* | 排气已燃质量分数 |

### 功率核算

对于功率核算，模块实现的方程取决于 **Torque model**。

当将 **Torque model** 设置为 `Simple Torque Lookup` 时，模块实现这些方程。

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrIntkHeatFlw` | 进气热流量 | m˙intkhintk |
| `PwrExhHeatFlw` | 排气热流量 | −m˙exhhexh |
| `PwrCrkshft` | 曲轴功率 | −Tbrakeω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFuel` | 燃料输入功率 | m˙fuelLHV |
| `PwrLoss` | 所有损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |

当将 **Torque model** 设置为 `Torque Structure` 时，模块实现这些方程。

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrIntkHeatFlw` | 进气热流量 | m˙intkhintk |
| `PwrExhHeatFlw` | 排气热流量 | −m˙exhhexh |
| `PwrCrkshft` | 曲轴功率 | −Tbrakeω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFuel` | 燃料输入功率 | m˙fuelLHV |
| `PwrFricLoss` | 摩擦损失 | −Tfricω |
| `PwrPumpLoss` | 泵气损失 | −Tpumpω |
| `PwrHeatTrnsfrLoss` | 传热损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh+Tfricω+Tpumpω |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |

|  |  |
| --- | --- |
| *hexh* | 排气歧管入口比焓 |
| *hintk* | 进气口比焓 |
| m˙intk | 进气口空气质量流量 |
| m˙fuel | 燃料质量流量 |
| m˙exh | 排气质量流量 |
| *ω* | 发动机转速 |
| *Tbrake* | 制动扭矩 |
| *Tpump* | 发动机泵气功对内扭矩的偏移 |
| *Tfric* | 发动机摩擦扭矩 |
| *LHV* | 燃料低热值 |
