---
type: simulink-block
title: 'CI Core Engine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components / Core Engine'
documentation_page: 'cicoreengine'
documentation_source_path: 'ref/cicoreengine.html'
language: zh-CN
chinese_source: worker-translation
---

# CI Core Engine

## 端口

### 输入

### **FuelMass** — 喷油器脉宽 `vector`

每次喷射的燃油质量，
*mfuel,inj*，单位为
mg per injection。

### **Soi** — 喷油开始时刻 `vector`

喷油时刻，*SOI*，单位为压缩上止点后曲轴转角
（degATDC）。第一个向量值，
`Soi(1)`，为主喷射时刻。

#### 依赖

要启用此参数，对于 **Torque model**，选择
`Torque Structure`。

### **EngSpd** — 发动机转速 `scalar`

发动机转速，*N*，单位为 rpm。

### **FuelPrs** — 燃油轨压力 `scalar`

燃油轨压力，*FUELP*，单位为 MPa。

#### 依赖

要启用此参数，对于 **Torque model**，选择
`Torque Structure`。

### **Ect** — 发动机冷却温度 `scalar`

发动机冷却温度，
*Tcoolant*，单位为 K。

#### 依赖

要启用此参数，对于 **Torque model**，选择
`Torque Structure`。

### **Intk** — 进气道压力、温度、焓、质量分数双向连接端口

包含上游的总线：

- `Prs` — 压力，单位为 Pa
- `Temp` — 温度，单位为 K
- `Enth` — 比焓，
  单位为 J/kg
- `MassFrac` —
  进气道质量分数，无量纲。进气道处的废气再循环
  (EGR) 质量流量为已燃气体。

  具体来说，是具有以下质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃燃油
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 已燃气体

### **Exh** — 排气道压力、温度、焓、质量分数双向连接端口

包含排气的总线：

- `Prs` — 压力，单位为 Pa
- `Temp` — 温度，单位为 K
- `Enth` — 比焓，
  单位为 J/kg
- `MassFrac` —
  排气道质量分数，无量纲。

  具体来说，是具有以下质量分数的总线：

  - `O2MassFrac` — 氧气
  - `N2MassFrac` — 氮气
  - `UnbrndFuelMassFrac` — 未燃燃油
  - `CO2MassFrac` — 二氧化碳
  - `H2OMassFrac` — 水
  - `COMassFrac` — 一氧化碳
  - `NOMassFrac` — 一氧化氮
  - `NO2MassFrac` — 二氧化氮
  - `NOxMassFrac` — 一氧化氮和二氧化氮
  - `PmMassFrac` — 颗粒物
  - `AirMassFrac` — 空气
  - `BrndGasMassFrac` — 已燃气体
### 输出

### **Info** — 总线信号总线

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `IntkGasMassFlw` | | | 发动机进气空气质量流量。 | m˙air | kg/s |
| `IntkAirMassFlw` | | | 发动机进气道质量流量。 | m˙intk | kg/s |
| `NrmlzdAirChrg` | | | 针对最终稳态凸轮相位角修正的发动机负荷（即归一化气缸空气质量） | L | N/A |
| `Afr` | | | 发动机排气口处的空燃比 | AFR | N/A |
| `FuelMassFlw` | | | 进入发动机的燃油流量 | m˙fuel | kg/s |
| `FuelVolFlw` | | | 体积燃油流量 | *Qfuel* | m3/s |
| `ExhManGasTemp` | | | 排气歧管入口处的排气温度 | Texh | K |
| `EngTrq` | | | 发动机制动扭矩 | Tbrake | N·m |
| `EngSpd` | | | 发动机转速 | N | rpm |
| `IntkCamPhase` | | | 进气凸轮相位器角度 | φICP i | degrees crank advance |
| `ExhCamPhase` | | | 排气凸轮相位器角度 | φECP | degrees crank retard |
| `CrkAng` | | | 发动机曲轴绝对角度 | ∫0(360)CpsEngSpd18030dθ  其中 Cps 为每动力冲程的曲轴转数 | degrees crank angle |
| `EgrPct` | | | EGR 百分比 | *EGRpct* | N/A |
| `EoAir` | | | EO 空气质量流量 | m˙exh | kg/s |
| `EoBrndGas` | | | EO 已燃气体质量流量 | *yexh,b* | kg/s |
| `EoHC` | | | EO 碳氢化合物排放质量流量 | *yexh,HC* | kg/s |
| `EoCO` | | | EO 一氧化碳排放质量流量 | *yexh,CO* | kg/s |
| `EoNOx` | | | EO 一氧化氮和二氧化氮排放质量流量 | *yexh,NOx* | kg/s |
| `EoCO2` | | | EO 二氧化碳排放质量流量 | *yexh,CO2* | kg/s |
| `EoPm` | | | EO 颗粒物排放质量流量 | *yexh,PM* | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrIntkHeatFlw` | 进气热流量 | m˙intkhintk | W |
| `PwrExhHeatFlw` | 排气热流量 | −m˙exhhexh | W |
| `PwrCrkshft` | 曲轴功率 | −Tbrakeω | W |
| `PwrNotTrnsfrd` | `PwrFuel` | 燃料输入功率 | m˙fuelLHV | W |
| `PwrLoss` | 对于 **Torque model** 设置为 `Simple Torque Lookup`：  所有损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh | W |
| `PwrFricLoss` | 对于 **Torque model** 设置为 `Torque Structure`：  摩擦损失 | −Tfricω | W |
| `PwrPumpLoss` | 对于 **Torque model** 设置为 `Torque Structure`：  泵气损失 | −Tpumpω | W |
| `PwrHeatTrnsfrLoss` | 对于 **Torque model** 设置为 `Torque Structure`：  传热损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh+Tfricω+Tpumpω | W |
| `PwrStored` | *未使用* | | | |

### **EngTrq** — 发动机制动扭矩 `scalar`

发动机制动扭矩，Tbrake，单位为 N·m。

### **Intk** — 进气道质量流量、热流量、温度、质量分数双向连接端口

包含以下内容的总线：

- `MassFlwRate` — 进气道
  质量流量，单位为 kg/s
- `HeatFlwRate` — 进气道
  热流量，单位为 J/s
- `ExhManGasTemp` — 进气道
  温度，单位为 K
- `MassFrac` —
  进气道质量分数，无量纲。

  具体来说，是一个包含以下质量分数的总线：

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
  - `BrndGasMassFrac` — 已燃气体

### **Exh** — 排气口质量流量、热流量、温度、质量分数双向连接端口

包含以下内容的总线：

- `MassFlwRate` — 排气口
  质量流量，单位为 kg/s
- `HeatFlwRate` — 排气热
  流量，单位为 J/s
- `ExhManGasTemp` — 排气
  口温度，单位为 K
- `MassFrac` —
  排气口质量分数，无量纲。

  具体来说，包含以下质量分数的总线：

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
  - `BrndGasMassFrac` — 已燃气体

## 参数

### 模块选项

### **Torque model** — 选择扭矩模型 `Torque Structure`（默认）| `Simple Torque Lookup`

要计算发动机扭矩，您可以将模块配置为
使用以下任一扭矩模型。

| 制动扭矩模型 | 描述 |
| --- | --- |
| CI Engine Torque Structure Model | CI 核心发动机扭矩结构模型通过在这些发动机条件偏离标称值时降低最大发动机扭矩潜力来确定发动机扭矩：  - 喷射开始（SOI）正时 - 排气背压 - 已燃燃料质量 - 进气歧管气体压力、温度和氧气百分比 - 燃油轨压力  为了考虑后喷射燃油对扭矩的影响，该模型使用标定的扭矩偏移表。 |
| CI Engine Simple Torque Model | 对于简单发动机扭矩计算，CI 发动机使用作为发动机转速和喷射燃料质量函数的扭矩查找表映射。 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrqOptionPopup` |
| **值：** | `Torque Structure`（默认）| `Simple Torque Lookup` |
| **数据类型：** | `character vector` |

### 空气

### **Number of cylinders, NCyl** — 发动机气缸数 `4`（默认）| `scalar`

发动机气缸数，Ncyl。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NCyl` |
| **值：** | `4`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Air standard temperature, Pstd** — 温度 `293.15`（默认）| `scalar`

标准空气温度，
*Tstd*，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pstd` |
| **值：** | `293.15`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Crank revolutions per power stroke, Cps** — 每冲程 revolutions `2`（默认）| `scalar`

每动力冲程的曲轴转数，Cps，单位为 rev/stroke。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cps` |
| **值：** | `2`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Total displaced volume, Vd** — 体积 `0.0015`（默认）| `scalar`

排量，Vd，单位为 m^3。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.0015`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Ideal gas constant air, Rair** — 常量 `287.05`（默认）| `scalar`

理想气体常数 Rair，单位为 J/(kg·K)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rair` |
| **值：** | `287.05`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Air standard pressure, Pstd** — 压力 `101325`（默认）| `scalar`

标准空气压力 Pstd，单位为 Pa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pstd` |
| **值：** | `101325`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Speed-density volumetric efficiency, f\_nv** — 查找表 `array`

容积效率查找表是进气门关闭（IVC）时进气歧管绝对压力和发动机转速的函数

ηv=fηv(MAP,N)

其中：

- ηv 是发动机容积效率，无量纲。
- *MAP* 是进气歧管绝对压力，单位为 KPa。
- *N* 是发动机转速，单位为 rpm。

发动机容积效率与进气歧管绝对压力和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt** — 断点 `vector`

速度密度容积效率查找表的进气歧管压力断点，单位为 KPa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_prs_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** — 断点 `vector`

速度密度容积效率查找表的发动机转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### 扭矩

#### 扭矩 - 简单扭矩查找

### **Torque table, f\_tq\_nf** — 查找表 `array`

对于简单扭矩查找表模型，CI 发动机使用一个查找表，该查找表是发动机转速和喷射燃油质量的函数，Tbrake=fTnf(F,N)，
其中：

- *Tq* = *Tbrake* 是考虑发动机机械摩擦和泵气摩擦效应后的发动机制动扭矩，单位为 N·m。
- *F* 是喷射燃油质量，单位为 mg/次喷射。
- *N* 是发动机转速，单位为 rpm。

发动机制动扭矩与喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tq_nf` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖

要启用此参数，对于 **Torque model**，选择 `Simple Torque Lookup`。

### **Torque table fuel mass per injection breakpoints, f\_tq\_nf\_f\_bpt** — 断点 `[0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286 50]`（默认）| `vector`

扭矩表每次喷射燃油质量断点，单位为 mg/次喷射。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tq_nf_f_bpt` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Simple Torque Lookup`。

### **Torque table speed breakpoints, f\_tq\_nf\_n\_bpt** — 断点 `[1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429 5517.8571 5928.5714 6339.2857 6750]`（默认）| `vector`

发动机转速断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tq_nf_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Simple Torque Lookup`。

#### Torque - Torque Structure

### **Fuel mass per injection breakpoints, f\_tqs\_f\_bpt** — 断点 `vector`

每次喷射的燃油质量断点，单位为 mg per injection。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_f_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Engine speed breakpoints, f\_tqs\_n\_bpt** — 断点 `[500 750 1000 1250 1500 1750 2000 2250 2500 2750 3000 3250 3500 3750 4000]`（默认）| `vector`

发动机转速断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal main start of injection timing, f\_tqs\_mainsoi** — 最优 MAINSOI `array`

最优主喷射开始（SOI）正时查找表 *ƒSOIc* 是发动机转速和喷射燃油质量的函数，*SOIc = ƒSOIc(F,N)*，其中：

- *SOIc* 是最优 SOI 正时，单位为 degATDC。
- *F* 是压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 是发动机转速，单位为 rpm。

最优 SOI 正时与喷射燃油质量和发动机转速的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mainsoi` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal intake manifold gas pressure, f\_tqs\_map** — 最优 intake MAP `array`

最优进气歧管气体压力查找表 *ƒMAP* 是发动机转速和喷射燃油质量的函数，*MAP = ƒMAP(F,N)*，其中：

- *MAP* 是最优进气歧管气体压力，单位为 Pa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 是发动机转速，单位为 rpm。

最优进气歧管气体压力与喷射燃油质量和发动机转速的 3D 图

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_map` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal exhaust manifold gas pressure, f\_tqs\_emap** — Optimal exhaust MAP `array`

最优排气歧管气体压力查找表 *ƒEMAP* 是发动机转速和喷射燃油质量的函数，*EMAP = ƒEMAP(F,N)*，其中：

- *EMAP* 是最优排气歧管气体压力，单位为 Pa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 是发动机转速，单位为 rpm。

排气歧管气体压力与喷射燃油质量和发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_emap` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal intake manifold gas temperature, f\_tqs\_mat** — Optimal intake MAT `array`

最优进气歧管气体温度查找表 *ƒMAT* 是发动机转速和喷射燃油质量的函数，*MAT = ƒMAT(F,N)*，其中：

- *MAT* 是最优进气歧管气体温度，单位为 K。
- *F* 是压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 是发动机转速，单位为 rpm。

最优进气气体温度与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_mat` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal intake gas oxygen percent, f\_tqs\_o2pct** — Optimal intake gas oxygen `array`

最优进气气体氧气百分比查找表 *ƒO2* 是发动机转速和喷射燃油质量的函数，*O2PCT = ƒO2(F,N)*，其中：

- *O2PCT* 是最优进气气体氧气，单位为 percent。
- *F* 是压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 是发动机转速，单位为 rpm。

最优进气气体氧气与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_o2pct` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal fuel rail pressure, f\_tqs\_fuelpress** — Optimal fuel rail pressure `array`

最优燃油轨压力查找表 *ƒfuelp* 是发动机转速和喷射燃油质量的函数，*FUELP = ƒfuelp(F,N)*，其中：

- *FUELP* 是最优燃油轨压力，单位为 MPa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg per injection。
- *N* 是发动机转速，单位为 rpm。

最优燃油轨压力与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_fuelpress` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal gross indicated mean effective pressure, f\_tqs\_imepg** — 最优指示平均有效压力 `array`

最优指示平均有效压力查找表 *ƒimepg* 是发动机转速和喷射燃油质量的函数，*IMEPG = ƒimepg(F,N)*，其中：

- *IMEPG* 是最优指示平均有效压力，单位为 Pa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg/次喷射。
- *N* 是发动机转速，单位为 rpm。

最优指示平均有效压力与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_imepg` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal friction mean effective pressure, f\_tqs\_fmep** — 最优摩擦平均有效压力 `array`

最优摩擦平均有效压力查找表 *ƒfmep* 是发动机转速和喷射燃油质量的函数，*FMEP = ƒfmep(F,N)*，其中：

- *FMEP* 是最优摩擦平均有效压力，单位为 Pa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg/次喷射。
- *N* 是发动机转速，单位为 rpm。

最优摩擦平均有效压力与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fmep` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Optimal pumping mean effective pressure, f\_tqs\_pmep** — 最优泵气平均有效压力 `array`

最优泵气平均有效压力查找表 *ƒpmep* 是发动机转速和喷射燃油质量的函数，*PMEP = ƒpmep(F,N)*，其中：

- *PMEP* 是最优泵气平均有效压力，单位为 Pa。
- *F* 是压缩冲程喷射燃油质量，单位为 mg/次喷射。
- *N* 是发动机转速，单位为 rpm。

最优泵气平均有效压力与进气歧管气体压力比相对于压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_pmep` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Friction multiplier as a function of temperature, f\_tqs\_fric\_temp\_mod** — 摩擦乘数 `array`

摩擦乘数随温度变化的函数，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fric_temp_mod` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Friction multiplier temperature breakpoints, f\_tqs\_fric\_temp\_bpt** — 断点 `vector`

摩擦乘数温度断点，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fric_temp_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Main start of injection timing efficiency multiplier, f\_tqs\_mainsoi\_eff** — MAINSOI 效率乘数 `array`

主喷射开始（SOI）正时效率乘数查找表，*ƒSOIeff*，是发动机
转速和主 SOI 正时相对于最优正时的函数，*SOIeff =
ƒSOIeff(ΔSOI,N)*，其中：

- *SOIeff* 是主 SOI 正时效率
  乘数，无量纲。
- *ΔSOI* 是主 SOI 正时相对于最优正时的偏差，单位为
  degBTDC。
- *N* 是发动机转速，单位为 rpm。

SOI 正时效率乘数相对于主 SOI 正时相对于最优正时和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mainsoi_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Main start of injection timing relative to optimal timing breakpoints, f\_tqs\_mainsoi\_delta\_bpt** — 断点 `vector`

主喷射开始正时相对于最优正时的断点，单位为
degBTDC。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mainsoi_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intake manifold gas pressure efficiency multiplier, f\_tqs\_map\_eff** — 进气压力效率乘数 `array`

进气歧管气体压力效率乘数查找
表，*ƒMAPeff*，是进气歧管
气体压力比相对于最优压力比和 lambda 的函数，
*MAPeff =
ƒMAPeff(MAPratio,λ)*，其中：

- *MAPeff* 是进气歧管气体压力
  效率乘数，无量纲。
- *MAPratio* 是进气歧管气体压力
  比相对于最优压力比，无量纲。
- *λ* 是进气歧管气体 lambda，无量纲。

进气歧管气体压力效率乘数相对于进气歧管气体压力比相对于最优压力比和进气歧管气体 lambda 的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_map_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intake manifold gas pressure ratio relative to optimal pressure ratio breakpoints, f\_tqs\_map\_ratio\_bpt** — 断点 `[0.8;0.85;0.9;0.95;1;1.05;1.1;1.15;1.2;1.25;1.3;1.35;1.4;1.45;1.5]`（默认） | `vector`

进气歧管气体压力比相对于最优压力比的断点，
无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_map_ratio_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **进气歧管气体 lambda 断点，f\_tqs\_lambda\_bpt** — 断点 `[1.5 1.678571428571429 1.857142857142857 2.035714285714286 2.214285714285714 2.392857142857143 2.571428571428571 2.75 2.928571428571429 3.107142857142857 3.285714285714286 3.464285714285714 3.642857142857143 3.821428571428572 4]`（默认）| `vector`

进气歧管气体 lambda 断点，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_lambda_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体温度效率乘数，f\_tqs\_mat\_eff** — 进气温度效率乘数 `array`

进气歧管气体温度效率乘数查找表 *ƒMATeff* 是发动机转速和进气歧管气体温度相对于最优温度的函数，*MATeff = ƒMATeff(ΔMAT,N)*，其中：

- *MATeff* 是进气歧管气体温度效率乘数，无量纲。
- *ΔMAT* 是进气歧管气体温度相对于最优温度，单位为 K。
- *N* 是发动机转速，单位为 rpm。

进气歧管气体温度效率乘数相对于进气气体氧气百分比（相对于最优值）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mat_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体温度相对于最优气体温度的断点，f\_tqs\_mat\_delta\_bpt** — 断点 `[-55;-50;-45;-40;-35;-30;-25;-20;-15;-10;-5;0;5;10;15]`（默认）| `vector`

进气歧管气体温度相对于最优气体温度的断点，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mat_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体氧气效率乘数，f\_tqs\_o2pct\_eff** — 进气氧气效率乘数 `array`

进气歧管气体氧气效率乘数查找表 *ƒO2Peff* 是发动机转速和进气歧管气体氧气百分比相对于最优值的函数，*O2Peff = ƒO2Peff(ΔO2P,N)*，其中：

- *O2Peff* 是进气歧管气体氧气效率乘数，无量纲。
- *ΔO2P* 是进气气体氧气百分比相对于最优值，单位为百分比。
- *N* 是发动机转速，单位为 rpm。

最优进气歧管气体氧气效率乘数相对于进气气体氧气百分比（相对于最优值）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_o2pct_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气气体氧气百分比相对于最优值的断点，f\_tqs\_o2pct\_delta\_bpt** — 断点 `vector`

进气气体氧气百分比相对于最优值的断点，单位为百分比。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_o2pct_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

### **燃油轨压力效率乘数，f\_tqs\_fuelpress\_eff** — 效率乘数 `array`

燃油轨压力效率乘数查找表 *ƒFUELPeff* 是发动机转速和燃油轨压力相对于最优断点的函数，*FUELPeff = ƒFUELPeff(ΔFUELP,N)*，其中：

- *FUELPeff* 是燃油轨压力效率乘数，无量纲。
- *ΔFUELP* 是燃油轨压力相对于最优值，单位为 MPa。
- *N* 是发动机转速，单位为 rpm。

燃油轨压力效率乘数相对于最优燃油轨压力和发动机转速的 3D 图

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fuelpress_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

### **燃油轨压力相对于最优断点，f\_tqs\_fuelpress\_delta\_bpt** — 断点 `vector`

燃油轨压力相对于最优断点，单位为 MPa。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fuelpress_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

### **燃油质量喷射类型标识符，f\_tqs\_f\_inj\_type** — 类型标识符 `0`（默认） | `scalar`

燃油质量喷射类型标识符，无量纲。

在 CI Core Engine 和 CI Controller 模块中，您可以通过模型的喷射开始（SOI）和燃油质量输入来表示多次喷射。要指定喷射类型，请使用 **Fuel mass injection type identifier** 参数。

| 喷射类型 | 参数值 |
| --- | --- |
| Pilot | `0` |
| Main | `1` |
| Post | `2` |
| Passed | `3` |

模型将 `Passed` 燃油喷射以及晚于阈值喷射的燃油视为未燃烧燃油。使用 **Maximum start of injection angle for burned fuel, f\_tqs\_f\_burned\_soi\_limit** 参数来指定阈值。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_f_inj_type` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

### **指示平均有效压力后喷射修正，f\_tqs\_imep\_post\_corr** — 后喷射修正 `array`

指示平均有效压力后喷射修正查找表 *ƒIMEPpost* 是发动机转速和燃油轨压力相对于最优断点的函数，*ΔIMEPpost = ƒIMEPpost(ΔSOIpost,Fpost)*，其中：

- *ΔIMEPpost* 是指示平均有效压力后喷射修正，单位为 Pa。
- *ΔSOIpost* 是指示平均有效压力后喷射开始时刻质心，单位为 degATDC。
- *Fpost* 是指示平均有效压力后喷射质量总和，单位为 mg per injection。

指示平均有效压力相对于后喷射开始时刻和后喷射质量总和的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_imep_post_corr` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，请选择
`Torque Structure`。

### **Indicated mean effective pressure post inject mass sum breakpoints, f\_tqs\_f\_post\_sum\_bpt** — 断点 `[0 3.571428571428572 7.142857142857143 10.71428571428571 14.28571428571429 17.85714285714286 21.42857142857143 25 28.57142857142857 32.14285714285715 35.71428571428572 39.28571428571428 42.85714285714285 46.42857142857143 50]`（默认）| `vector`

指示平均有效压力后喷射质量总和断点，单位为 mg per
injection。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_f_post_sum_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，请选择
`Torque Structure`。

### **Indicated mean effective pressure post inject start of inject timing centroid breakpoints, f\_tqs\_soi\_post\_cent\_bpt** — 断点 `[150 160.7142857142857 171.4285714285714 182.1428571428571 192.8571428571429 203.5714285714286 214.2857142857143 225 235.7142857142857 246.4285714285714 257.1428571428571 267.8571428571429 278.5714285714286 289.2857142857143 300]`（默认）| `vector`

指示平均有效压力后喷射喷射开始时刻质心
断点，单位为 degATDC。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_soi_post_cent_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，请选择
`Torque Structure`。

### **Maximum start of injection angle for burned fuel, f\_tqs\_f\_burned\_soi\_limit** — 已燃燃油最大 SOI 角度 `500`（默认）| `scalar`

已燃燃油最大喷射开始角度，单位为 degATDC。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_f_bpt` |
| **值：** | `500`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，请选择
`Torque Structure`。

### 排气

#### 排气温度 - 简单扭矩查找

### **Exhaust temperature table, f\_t\_exh** — 查找表 `array`

排气温度查找表是喷射燃油质量和发动机
转速的函数

Texh=fTexh(F,N)

其中：

- Texh 为
  排气温度，单位为 K。
- *F* 为喷射燃油质量，单位为 mg
  per injection。
- *N* 为发动机转速，单位为 rpm。

排气温度与发动机转速和发动机扭矩的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，请选择
`Simple Torque Lookup`。

### **Fuel mass per injection breakpoints, f\_t\_exh\_f\_bpt** — 断点 `[0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286 50]`（默认）| `vector`

用于排气温度查找表的发动机负荷断点，单位为 mg per
injection。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh_f_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Simple Torque Lookup`。

### **Speed breakpoints, f\_t\_exh\_n\_bpt** — 断点 `[1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429 5517.8571 5928.5714 6339.2857 6750]`（默认）| `vector`

用于排气温度查找表的发动机转速断点，单位为 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Simple Torque Lookup`。

#### 排气温度 - 扭矩结构

### **Optimal exhaust manifold gas temperature, f\_tqs\_exht** — 最佳排气歧管气体温度 `array`

最佳排气歧管气体温度查找表 *ƒTexh* 是发动机转速和喷射燃油质量的函数，*Texhopt = ƒTexh(F,N)*，其中：

- *Texhopt* 是最佳排气歧管气体温度，单位为 K。
- *F* 是压缩冲程喷射燃油质量，单位为 mg/次喷射。
- *N* 是发动机转速，单位为 rpm。

最佳排气歧管气体温度与压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Main start of injection timing exhaust temperature efficiency multiplier, f\_tqs\_exht\_mainsoi\_eff** — 主 SOI 正时效率乘数 `array`

主喷射开始（SOI）正时排气温度效率乘数查找表 *ƒSOIexhteff* 是发动机转速和喷射燃油质量的函数，*SOIexhteff = ƒSOIexhteff(ΔSOI,N)*，其中：

- *SOIexhteff* 是主 SOI 排气温度效率乘数，无量纲。
- *ΔSOI* 是主 SOI 正时相对于最佳正时，单位为 degBTDC。
- *N* 是发动机转速，单位为 rpm。

SOI 排气温度效率乘数与主 SOI 正时相对于最佳正时和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_mainsoi_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体压力排气温度效率乘数，f\_tqs\_exht\_map\_eff** — 进气歧管效率乘数 `array`

进气歧管气体压力排气温度效率乘数查找表，*ƒMAPexheff*，是进气歧管气体压力比相对于最优压力比和 lambda 的函数，*MAPexheff = ƒMAPexheff(MAPratio,λ)*，其中：

- *MAPexheff* 是进气歧管气体压力排气温度效率乘数，无量纲。
- *MAPratio* 是进气歧管气体压力比相对于最优压力比，无量纲。
- *λ* 是进气歧管气体 lambda，无量纲。

进气歧管气体压力排气温度效率乘数相对于进气歧管气体压力比与最优压力比及进气歧管气体 lambda 的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_map_eff` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体温度排气温度效率乘数，f\_tqs\_exht\_mat\_eff** — 进气歧管效率乘数 `array`

进气歧管气体温度排气温度效率乘数查找表，*ƒMATexheff*，是发动机转速和进气歧管气体温度相对于最优温度的函数，*MATexheff = ƒMATexheff(ΔMAT,N)*，其中：

- *MATexheff* 是进气歧管气体温度排气温度效率乘数，无量纲。
- *ΔMAT* 是进气歧管气体温度相对于最优温度，单位为 K。
- *N* 是发动机转速，单位为 rpm。

进气歧管气体温度排气温度效率乘数相对于进气歧管气体温度与最优温度之差及发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_mat_eff` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **进气歧管气体氧气排气温度效率乘数，f\_tqs\_exht\_o2pct\_eff** — 进气歧管效率乘数 `array`

进气歧管气体氧气排气温度效率乘数查找表，*ƒO2Pexheff*，是发动机转速和进气歧管气体氧气百分比相对于最优值的函数，*O2Pexheff = ƒO2Pexheff(ΔO2P,N)*，其中：

- *O2Pexheff* 是进气歧管气体氧气排气温度效率乘数，无量纲。
- *ΔO2P* 是进气气体氧气百分比相对于最优值，单位为百分比。
- *N* 是发动机转速，单位为 rpm。

最优进气歧管气体氧气排气温度效率乘数相对于进气气体氧气百分比与最优值之差及发动机转速的 3D 图

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `f_tqs_exht_o2pct_eff` |
| **值**：| `array` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择 `Torque Structure`。

### **Fuel rail pressure exhaust temperature efficiency multiplier, f\_tqs\_exht\_fuelpress\_eff** — 燃油轨压排气温度效率乘数 `array`

燃油轨压效率排气温度乘数查找表，*ƒFUELPexheff*，是发动机转速和燃油轨压相对于最优断点的函数，*FUELPexheff = ƒFUELPexheff(ΔFUELP,N)*，其中：

- *FUELPexheff* 是燃油轨压排气温度效率乘数，无量纲。
- *ΔFUELP* 是燃油轨压相对于最优值，单位为 MPa。
- *N* 是发动机转速，单位为 rpm。

燃油轨压排气温度效率乘数相对于燃油轨压相对于最优值和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_fuelpress_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

### **Post-injection cylinder wall heat loss transfer coefficient, f\_tqs\_exht\_post\_inj\_wall\_htc** — 后喷射偏移 `0`（默认） | `scalar`

后喷射缸壁热损失传热系数，单位为 W/K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_post_inj_wall_htc` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，对于 **Torque model**，选择 `Torque Structure`。

#### 排放

### **CO2 mass fraction table, f\_CO2\_frac** — 二氧化碳（CO2）排放查找表 `array`

CI Core Engine CO2 排放质量分数查找表是发动机扭矩和发动机转速的函数，*CO2 Mass Fraction* = ƒ(*Speed*, *Torque*)，其中：

- *CO2 Mass Fraction* 是 CO2 排放质量分数，无量纲。
- *Speed* 是发动机转速，单位为 rpm。
- *Torque* 是发动机扭矩，单位为 N·m。

CO2 排放质量分数相对于发动机转速和发动机扭矩的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_CO2_frac` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，在 **Exhaust** 选项卡上，选择 **CO2**。

### **CO mass fraction table, f\_CO\_frac** — 一氧化碳（CO）排放查找表 `array`

CI Core Engine CO 排放质量分数查找表是发动机扭矩和发动机转速的函数，*CO Mass Fraction* = ƒ(*Speed*, *Torque*)，其中：

- *CO Mass Fraction* 是 CO 排放质量分数，无量纲。
- *Speed* 是发动机转速，单位为 rpm。
- *Torque* 是发动机扭矩，单位为 N·m。

CO 排放质量分数相对于发动机转速和发动机扭矩的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_CO_frac` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，在 **Exhaust** 选项卡上，选择 **CO**。

### **HC 质量分数表，f\_HC\_frac** — 碳氢化合物（HC）排放查找表 `array`

CI 核心发动机 HC 排放质量分数查找表是发动机扭矩和发动机转速的函数，*HC 质量分数* = ƒ(*转速*, *扭矩*)，
其中：

- *HC 质量分数* 是 HC 排放质量分数，无量纲。
- *转速* 是发动机转速，单位为 rpm。
- *扭矩* 是发动机扭矩，单位为 N·m。

HC 排放质量分数随发动机转速和发动机扭矩变化的三维图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_HC_frac` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Exhaust** 选项卡上选择
**HC**。

### **NOx 质量分数表，f\_NOx\_frac** — 一氧化氮和二氧化氮（NOx）排放查找表 `array`

CI 核心发动机 NOx
排放质量分数查找表是发动机扭矩
和发动机转速的函数，*NOx 质量分数* = ƒ(*转速*, *扭矩*)，
其中：

- *NOx 质量分数* 是 NOx 排放
  质量分数，无量纲。
- *转速* 是发动机转速，单位为 rpm。
- *扭矩* 是发动机扭矩，单位为 N·m。

NOx 排放质量分数随发动机转速和发动机扭矩变化的三维图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_NOx_frac` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Exhaust** 选项卡上选择
**NOx**。

### **PM 质量分数表，f\_PM\_frac** — 颗粒物（PM）排放查找表 `array`

CI 核心发动机 PM 排放质量分数
查找表是发动机扭矩和发动机转速的函数，其中：

- *PM* 是 PM 排放质量分数，
  无量纲。
- *转速* 是发动机转速，单位为 rpm。
- *扭矩* 是发动机扭矩，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_PM_frac` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Exhaust** 选项卡上选择
**PM**。

### **发动机转速断点，f\_exhfrac\_n\_bpt** — 断点 `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]`（默认） | `vector`

用于排放质量分数查找表的发动机转速断点，单位为
rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_exhfrac_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Exhaust** 选项卡上选择
**CO2**、**CO**、**NOx**、
**HC** 或 **PM**。

### **发动机扭矩断点，f\_exhfrac\_trq\_bpt** — 断点 `[0 15 26.4285714285714 37.8571428571429 49.2857142857143 60.7142857142857 72.1428571428571 83.5714285714286 95 106.428571428571 117.857142857143 129.285714285714 140.714285714286 152.142857142857 163.571428571429 175]`（默认） | `vector`

用于排放质量分数查找表的发动机扭矩断点，单位为
N·m。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_exhfrac_trq_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Exhaust** 选项卡上，选择
**CO2**、**CO**、**NOx**、
**HC** 或 **PM**。

### **Exhaust gas specific heat at constant pressure, cp\_exh** — 比热 `1005`（默认）| `scalar`

排气气体比热，Cpexh，单位为 J/(kg·K)。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `cp_exh` |
| **值：** | `1005`（默认）| `scalar` |
| **数据类型：** | `double` |

### 燃料

### **Stoichiometric air-fuel ratio, afr\_stoich** — 空燃比 `14.6`（默认）| `scalar`

空燃比，AFR。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `afr_stoich` |
| **值：** | `14.6`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Fuel lower heating value, fuel\_lhv** — 热值 `42e6`（默认）| `scalar`

燃料低热值，*LHV*，单位为 J/kg。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `fuel_lhv` |
| **值：** | `42e6`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Fuel specific gravity, fuel\_sg** — 比重 `0.832`（默认）| `scalar`

燃料比重，
*Sgfuel*，
无量纲。

#### 程序化使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `fuel_sg` |
| **值：** | `0.832`（默认）| `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Core Engine

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

从进气口到排气口的压燃式发动机

CI Core Engine 模块实现了从进气口到排气口的压燃式
（CI）发动机。您可以将该模块
用于硬件在环（HIL）发动机控制设计或车辆级
燃油经济性和性能仿真。

CI Core Engine 模块计算：

- 制动扭矩
- 排气温度
- 空燃比（AFR）
- 燃油轨压力
- 发动机出口（EO）排气排放：

  - 碳氢化合物（HC）
  - 一氧化碳（CO）
  - 一氧化氮和二氧化氮（NOx）
  - 二氧化碳（CO2）
  - 颗粒物（PM）

### 空气质量流量

为了计算空气质量流量，压燃式（CI）
发动机使用 CI Engine Speed-Density Air Mass Flow Model。速度密度
模型使用速度密度方程来计算发动机空气
质量流量，将发动机进气口质量流量与进气
歧管压力、进气歧管温度和发动机转速相关联。

### Brake Torque

要计算发动机扭矩，您可以将该模块配置为使用以下任一扭矩模型。

| 制动扭矩模型 | 描述 |
| --- | --- |
| CI Engine Torque Structure Model | CI 核心发动机扭矩结构模型通过在这些发动机条件偏离标称值时降低最大发动机扭矩潜力来确定发动机扭矩：  - 喷射开始 (SOI) 正时 - 排气背压 - 已燃烧燃料质量 - 进气歧管气体压力、温度和氧气百分比 - 燃油轨压力  为了考虑后喷射燃油对扭矩的影响，该模型使用校准的扭矩偏移表。 |
| CI Engine Simple Torque Model | 对于简单发动机扭矩计算，CI 发动机使用作为发动机转速和喷射燃油质量函数的扭矩查找表映射。 |

### Fuel Flow

在 CI Core Engine 和 CI Controller 模块中，您可以使用模型的喷射开始 (SOI) 和燃油质量输入来表示多次喷射。要指定喷射类型，请使用 **Fuel mass injection type identifier** 参数。

| 喷射类型 | 参数值 |
| --- | --- |
| Pilot | `0` |
| Main | `1` |
| Post | `2` |
| Passed | `3` |

该模型将 `Passed` 燃油喷射以及晚于某个阈值的燃油喷射视为未燃烧燃油。使用 **Maximum start of injection angle for burned fuel, f\_tqs\_f\_burned\_soi\_limit** 参数来指定该阈值。

为了计算发动机燃油质量流量，CI Core Engine 模块使用喷油器输送的燃油质量流量和发动机空气流量。

m˙fuel=N⋅NcylCps(60smin)(1000mgg)∑mfuel,inj

为了计算高保真模型的燃油经济性，该模块使用体积燃油流量。

Qfuel=m˙fuel(1000kgm3)Sgfuel

该方程使用以下变量。

|  |  |
| --- | --- |
| m˙fuel | 燃油质量流量，g/s |
| *mfuel,inj* | 每次喷射的燃油质量 |
| Cps | 每个动力冲程的曲轴转数，rev/stroke |
| Ncyl | 发动机气缸数 |
| *N* | 发动机转速，rpm |
| *Qfuel* | 体积燃油流量 |
| *Sgfuel* | 燃油比重 |

该模块使用内部信号 `FlwDir` 来跟踪流动方向。

### Air-Fuel Ratio

为了计算空燃比 (AFR)，CI Core Engine 和 SI Core Engine 模块实现以下方程。

AFR=m˙airm˙fuel

CI Core Engine 使用以下方程来计算相对 AFR。

λ=AFRAFRs

为了计算废气再循环 (EGR)，这些模块实现以下方程。该计算将 EGR 表示为总进气口流量的百分比。

EGRpct=100m˙intk,bm˙intk=100yintk,b

这些方程使用以下变量。

|  |  |
| --- | --- |
| AFR | 空燃比 |
| *AFRs* | 化学计量空燃比 |
| m˙intk | 发动机空气质量流量 |
| m˙fuel | 燃油质量流量 |
| λ | 相对 AFR |
| *yintk,b* | 进气已燃烧质量分数 |
| *EGRpct* | EGR 百分比 |
| m˙intk,b | 再循环已燃烧气体质量流量 |

### Exhaust Temperature

排气温度的计算取决于扭矩模型。对于两种扭矩模型，该模块均实现查找表。

| 扭矩模型 | 描述 | 方程 |
| --- | --- | --- |
| `Simple Torque Lookup` | 排气温度查找表是喷射燃油质量和发动机转速的函数。 | Texh=fTexh(F,N) |
| `Torque Structure` | 名义排气温度 *Texhnom* 是以下排气温度效率的乘积：  - SOI 正时 - 进气歧管气体压力 - 进气歧管气体温度 - 进气歧管气体氧气百分比 - 燃油轨压力 - 最佳温度  排气温度 *Texhnom* 由后温度效应 *ΔTpost* 偏移，该效应考虑了膨胀和排气冲程期间的后喷射和晚喷射。 | Texhnom=SOIexhteffMAPexhteffMATexhteffO2pexhteffFUELPexhteffTexhoptTexh=Texhnom+ΔTpostSOIexhteff=fSOIexhteff(ΔSOI,N)MAPexhteff=fMAPexhteff(MAPratio,λ)MATexhteff=fMATexhteff(ΔMAT,N)O2pexhteff=fO2pexhteff(ΔO2p,N)Texhopt=fTexh(F,N) |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *F* | 压缩冲程喷射燃油质量 |
| *N* | 发动机转速 |
| *Texh* | 排气歧管气体温度 |
| *Texhopt* | 最佳排气歧管气体温度 |
| *ΔTpost* | 后喷射温度效应 |
| *Texhnom* | 名义排气温度 |
| *SOIexhteff* | 主 SOI 排气温度效率乘数 |
| *ΔSOI* | 主 SOI 正时相对于最佳正时 |
| *MAPexheff* | 进气歧管气体压力排气温度效率乘数 |
| *MAPratio* | 进气歧管气体压力相对于最佳压力比 |
| *λ* | 进气歧管气体 lambda |
| *MATexheff* | 进气歧管气体温度排气温度效率乘数 |
| *ΔMAT* | 进气歧管气体温度相对于最佳温度 |
| *O2Pexheff* | 进气歧管气体氧气排气温度效率乘数 |
| *ΔO2P* | 进气气体氧气百分比相对于最佳值 |
| *FUELPexheff* | 燃油轨压力排气温度效率乘数 |
| *ΔFUELP* | 燃油轨压力相对于最佳值 |

### EO Exhaust Emissions

该模块计算以下发动机原始（EO）排放：

- 碳氢化合物（HC）
- 一氧化碳（CO）
- 一氧化氮和二氧化氮（NOx）
- 二氧化碳（CO2）
- 颗粒物（PM）

排气温度决定比焓。

hexh=CpexhTexh

排气质量流量是进气口空气
质量流量与燃料质量流量之和。

m˙exh=m˙intake+m˙fuel

为计算排放，该模块将排放质量分数乘以排气质量流量。为确定
排放质量分数，该模块使用作为发动机扭矩和转速函数的查找表。

yexh,i=fi\_frac(Tbrake,N)m˙exh,i=m˙exhyexh,i

进入进气口的空气和燃料分数、喷射
燃料以及化学计量空燃比决定离开排气的空气质量分数。

yexh,air=max[yin,air−m˙fuel+yin,fuelm˙intakem˙fuel+m˙intakeAFRs]

如果发动机在化学计量或富燃
空燃比下运行，则没有空气从排气排出。未燃烧的碳氢化合物和已燃气体
构成排气的其余部分。该方程确定
排气已燃气体质量分数。

yexh,b=max[(1−yexh,air−yexh,HC),0]

这些方程使用以下变量。

|  |  |
| --- | --- |
| Texh | 发动机排气温度 |
| hexh | 排气歧管入口比焓 |
| Cpexh | 排气比热 |
| m˙intk | 进气口空气质量流量 |
| m˙fuel | 燃料质量流量 |
| m˙exh | 排气质量流量 |
| yin,fuel | 进气燃料质量分数 |
| *yexh,i* | i = CO2、CO、HC、NOx、空气、已燃气体和 PM 的排气质量分数 |
| m˙exh,i | i = CO2、CO、HC、NOx、空气、已燃气体和 PM 的排气质量流量 |
| *Tbrake* | 发动机制动扭矩 |
| *N* | 发动机转速 |
| *yexh,air* | 排气空气质量分数 |
| *yexh,b* | 排气已燃空气质量分数 |

### 功率核算

对于功率核算，该模块实现的方程取决于 **Torque model**。

当您将 **Torque model** 设置为 `Simple Torque Lookup` 时，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrIntkHeatFlw` | 进气热流 | m˙intkhintk |
| `PwrExhHeatFlw` | 排气热流 | −m˙exhhexh |
| `PwrCrkshft` | 曲轴功率 | −Tbrakeω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFuel` | 燃料输入功率 | m˙fuelLHV |
| `PwrLoss` | 所有损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh |
| `PwrStored` — 储能变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |

当您将 **Torque model** 设置为 `Torque Structure` 时，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrIntkHeatFlw` | 进气热流 | m˙intkhintk |
| `PwrExhHeatFlw` | 排气热流 | −m˙exhhexh |
| `PwrCrkshft` | 曲轴功率 | −Tbrakeω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFuel` | 燃料输入功率 | m˙fuelLHV |
| `PwrFricLoss` | 摩擦损失 | −Tfricω |
| `PwrPumpLoss` | 泵气损失 | −Tpumpω |
| `PwrHeatTrnsfrLoss` | 传热损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh+Tfricω+Tpumpω |
| `PwrStored` — 储能变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |

|  |  |
| --- | --- |
| *hexh* | 排气歧管入口比焓 |
| *hintk* | 进气口比焓 |
| m˙intk | 进气口空气质量流量 |
| m˙fuel | 燃料质量流量 |
| m˙exh | 排气质量流量 |
| *ω* | 发动机转速 |
| *Tbrake* | 制动扭矩 |
| *Tpump* | 发动机泵气功相对于内部扭矩的偏移 |
| *Tfric* | 发动机摩擦扭矩 |
| *LHV* | 燃料低热值 |
