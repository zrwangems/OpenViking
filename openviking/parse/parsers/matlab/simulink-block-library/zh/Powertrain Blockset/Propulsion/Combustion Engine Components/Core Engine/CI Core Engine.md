---
type: simulink-block
title: 'CI Core Engine'
family: 'propulsion'
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

### **FuelMass** — Fuel injector pulse-width `vector`

每次喷射的燃油质量，
*mfuel,inj*，单位
mg per injection。

### **Soi** — Start of fuel injection timing `vector`

燃油喷射正时，*SOI*，单位曲轴转角
在上止点后度数 (degATDC)。第一个向量值，
`Soi(1)`，是主喷射正时。

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **EngSpd** — Engine speed `scalar`

发动机转速，*N*，单位 rpm。

### **FuelPrs** — Fuel rail pressure `scalar`

燃油轨压力，*FUELP*，单位 MPa。

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Ect** — Engine cooling temperature `scalar`

发动机冷却液温度，
*Tcoolant*，单位 K。

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intk** — Intake port pressure, temperature, enthalpy, mass fractions two-way connector port

总线包含上游：

- `Prs` — 压力，单位 Pa
- `Temp` — 温度，单位 K
- `Enth` — 比焓，
  单位 J/kg
- `MassFrac` —
  进气口质量分数，无量纲。进气口处的废气再循环
  (EGR) 质量流量为已燃气体。

  具体而言，一个具有以下质量分数的总线：

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

### **Exh** — Exhaust port pressure, temperature, enthalpy, mass fractions two-way connector port

总线包含排气：

- `Prs` — 压力，单位 Pa
- `Temp` — 温度，单位 K
- `Enth` — 比焓，
  单位 J/kg
- `MassFrac` —
  排气口质量分数，无量纲。

  具体而言，一个具有以下质量分数的总线：

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

### **Info** — Bus signal bus

总线信号包含这些模块计算。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `IntkGasMassFlw` | | | 发动机进气空气质量流量。 | m˙air | kg/s |
| `IntkAirMassFlw` | | | 发动机进气口质量流量。 | m˙intk | kg/s |
| `NrmlzdAirChrg` | | | 针对最终稳态凸轮相位角校正后的发动机负荷（即归一化气缸空气质量） | L | N/A |
| `Afr` | | | 发动机排气口处的空燃比 | AFR | N/A |
| `FuelMassFlw` | | | 进入发动机的燃油流量 | m˙fuel | kg/s |
| `FuelVolFlw` | | | 体积燃油流量 | *Qfuel* | m3/s |
| `ExhManGasTemp` | | | 排气歧管入口处的排气温度 | Texh | K |
| `EngTrq` | | | 发动机制动扭矩 | Tbrake | N·m |
| `EngSpd` | | | 发动机转速 | N | rpm |
| `IntkCamPhase` | | | 进气凸轮相位器角度 | φICP i | degrees crank advance |
| `ExhCamPhase` | | | 排气凸轮相位器角度 | φECP | degrees crank retard |
| `CrkAng` | | | 发动机曲轴绝对角度 | ∫0(360)CpsEngSpd18030dθ  其中 Cps 是每动力冲程的曲轴转数 | degrees crank angle |
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
| `PwrNotTrnsfrd` | `PwrFuel` | 燃油输入功率 | m˙fuelLHV | W |
| `PwrLoss` | 对于 **Torque model** 设置为 `Simple Torque Lookup`：所有损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh | W |
| `PwrFricLoss` | 对于 **Torque model** 设置为 `Torque Structure`：摩擦损失 | −Tfricω | W |
| `PwrPumpLoss` | 对于 **Torque model** 设置为 `Torque Structure`：泵气损失 | −Tpumpω | W |
| `PwrHeatTrnsfrLoss` | 对于 **Torque model** 设置为 `Torque Structure`：传热损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh+Tfricω+Tpumpω | W |
| `PwrStored` | *未使用* | | | |

### **EngTrq** — Engine brake torque `scalar`

发动机制动扭矩，Tbrake，单位 N·m。

### **Intk** — Intake port mass flow rate, heat flow rate, temperature, mass fraction two-way connector port

总线包含：

- `MassFlwRate` — 进气口
  质量流量，单位 kg/s
- `HeatFlwRate` — 进气口
  热流量，单位 J/s
- `ExhManGasTemp` — 进气口
  温度，单位 K
- `MassFrac` —
  进气口质量分数，无量纲。

  具体而言，一个具有以下质量分数的总线：

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

### **Exh** — Exhaust port mass flow rate, heat flow rate, temperature, mass fraction two-way connector port

总线包含：

- `MassFlwRate` — 排气口
  质量流量，单位 kg/s
- `HeatFlwRate` — 排气
  热流量，单位 J/s
- `ExhManGasTemp` — 排气口
  温度，单位 K
- `MassFrac` —
  排气口质量分数，无量纲。

  具体而言，一个具有以下质量分数的总线：

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

## 参数

### 模块选项

### **Torque model** — 选择扭矩模型 `Torque Structure` (default) | `Simple Torque Lookup`

为计算发动机扭矩，您可以将模块配置为使用以下任一扭矩模型。

| 制动扭矩模型 | 描述 |
| --- | --- |
| CI Engine Torque Structure Model | CI 核心发动机扭矩结构模型通过在这些发动机条件偏离标称值时降低最大发动机扭矩潜力来确定发动机扭矩：  - 喷射开始 (SOI) 正时 - 排气背压 - 已燃燃油质量 - 进气歧管气体压力、温度和氧气百分比 - 燃油轨压力  为考虑后喷射燃油对扭矩的影响，模型使用校准的扭矩偏移表。 |
| CI Engine Simple Torque Model | 对于简单发动机扭矩计算，CI 发动机使用作为发动机转速和喷射燃油质量函数的扭矩查找表映射。 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TrqOptionPopup` |
| **值：** | `Torque Structure` (default) | `Simple Torque Lookup` |
| **数据类型：** | `character vector` |

### 空气

### **Number of cylinders, NCyl** — Engine cylinders `4` (default) | `scalar`

发动机气缸数，Ncyl。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NCyl` |
| **值：** | `4` (default) | `scalar` |
| **数据类型：** | `double` |

### **Air standard temperature, Pstd** — Temperature `293.15` (default) | `scalar`

标准空气温度，
*Tstd*，单位 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pstd` |
| **值：** | `293.15` (default) | `scalar` |
| **数据类型：** | `double` |

### **Crank revolutions per power stroke, Cps** — Revolutions per stroke `2` (default) | `scalar`

每动力冲程的曲轴转数，Cps，单位 rev/stroke。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cps` |
| **值：** | `2` (default) | `scalar` |
| **数据类型：** | `double` |

### **Total displaced volume, Vd** — Volume `0.0015` (default) | `scalar`

排量，Vd，单位 m^3。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.0015` (default) | `scalar` |
| **数据类型：** | `double` |

### **Ideal gas constant air, Rair** — Constant `287.05` (default) | `scalar`

理想气体常数，Rair，单位 J/(kg·K)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rair` |
| **值：** | `287.05` (default) | `scalar` |
| **数据类型：** | `double` |

### **Air standard pressure, Pstd** — Pressure `101325` (default) | `scalar`

标准空气压力，Pstd，单位 Pa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pstd` |
| **值：** | `101325` (default) | `scalar` |
| **数据类型：** | `double` |

### **Speed-density volumetric efficiency, f\_nv** — Lookup table `array`

容积效率查找表是进气门关闭 (IVC) 时进气歧管绝对压力和发动机转速的函数

ηv=fηv(MAP,N)

其中：

- ηv 是发动机容积效率，无量纲。
- *MAP* 是进气歧管绝对压力，单位 KPa。
- *N* 是发动机转速，单位 rpm。

发动机容积效率相对于进气歧管绝对压力和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv` |
| **值：** | `array` |
| **数据类型：** | `double` |

### **Speed-density intake manifold pressure breakpoints, f\_nv\_prs\_bpt** — Breakpoints `vector`

用于速度密度容积效率查找表的进气歧管压力断点，单位 KPa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_prs_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Speed-density engine speed breakpoints, f\_nv\_n\_bpt** — Breakpoints `vector`

用于速度密度容积效率查找表的发动机转速断点，单位 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_nv_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### 扭矩

#### 扭矩 - Simple Torque Lookup

### **Torque table, f\_tq\_nf** — Lookup table `array`

对于简单扭矩查找表模型，CI 发动机使用一个查找表，该查找表是发动机转速和喷射燃油质量的函数，Tbrake=fTnf(F,N)，
其中：

- *Tq* = *Tbrake* 是考虑发动机机械和泵气摩擦效应后的发动机制动扭矩，单位 N·m。
- *F* 是喷射燃油质量，单位 mg per injection。
- *N* 是发动机转速，单位 rpm。

发动机制动扭矩相对于喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tq_nf` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Simple Torque Lookup`。

### **Torque table fuel mass per injection breakpoints, f\_tq\_nf\_f\_bpt** — Breakpoints `[0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286 50]` (default) | `vector`

扭矩表每次喷射燃油质量断点，单位 mg per injection。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tq_nf_f_bpt` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Simple Torque Lookup`。

### **Torque table speed breakpoints, f\_tq\_nf\_n\_bpt** — Breakpoints `[1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429 5517.8571 5928.5714 6339.2857 6750]` (default) | `vector`

发动机转速断点，单位 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tq_nf_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Simple Torque Lookup`。

#### 扭矩 - Torque Structure

### **Fuel mass per injection breakpoints, f\_tqs\_f\_bpt** — Breakpoints `vector`

每次喷射燃油质量断点，单位 mg per injection。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_f_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Engine speed breakpoints, f\_tqs\_n\_bpt** — Breakpoints `[500 750 1000 1250 1500 1750 2000 2250 2500 2750 3000 3250 3500 3750 4000]` (default) | `vector`

发动机转速断点，单位 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Optimal main start of injection timing, f\_tqs\_mainsoi** — Optimal MAINSOI `array`

最优主喷射开始 (SOI) 正时查找表，
*ƒSOIc*，是发动机转速和
喷射燃油质量的函数，*SOIc =
ƒSOIc(F,N)*，其中：

- *SOIc* 是最优 SOI 正时，单位
  degATDC。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

最优 SOI 正时相对于喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mainsoi` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Optimal intake manifold gas pressure, f\_tqs\_map** — Optimal intake MAP `array`

最优进气歧管气体压力查找表，
*ƒMAP*，是发动机转速和
喷射燃油质量的函数，*MAP = ƒMAP(F,N)*，其中：

- *MAP* 是最优进气歧管气体压力，单位 Pa。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

最优进气歧管气体压力相对于喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_map` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Optimal exhaust manifold gas pressure, f\_tqs\_emap** — Optimal exhaust MAP `array`

最优排气歧管气体压力查找表，
*ƒEMAP*，是发动机转速和
喷射燃油质量的函数，*EMAP = ƒEMAP(F,N)*，其中：

- *EMAP* 是最优排气歧管气体压力，单位 Pa。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

排气歧管气体压力相对于喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_emap` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Optimal intake manifold gas temperature, f\_tqs\_mat** — Optimal intake MAT `array`

最优进气歧管气体温度查找表，
*ƒMAT*，是发动机转速和
喷射燃油质量的函数，*MAT = ƒMAT(F,N)*，其中：

- *MAT* 是最优进气歧管气体温度，单位 K。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

最优进气气体温度相对于压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mat` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Optimal intake gas oxygen percent, f\_tqs\_o2pct** — Optimal intake gas oxygen `array`

最优进气气体氧气百分比查找表，
*ƒO2*，是发动机转速和
喷射燃油质量的函数，*O2PCT = ƒO2(F,N)*，其中：

- *O2PCT* 是最优进气气体氧气，单位 percent。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

最优进气气体氧气相对于压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_o2pct` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Optimal fuel rail pressure, f\_tqs\_fuelpress** — Optimal fuel rail pressure `array`

最优燃油轨压力查找表，
*ƒfuelp*，是发动机转速和
喷射燃油质量的函数，*FUELP = ƒfuelp(F,N)*，其中：

- *FUELP* 是最优燃油轨压力，单位 MPa。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

最优燃油轨压力相对于压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fuelpress` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Optimal gross indicated mean effective pressure, f\_tqs\_imepg** — Optimal mean effective pressure `array`

最优总指示平均有效压力查找表，
*ƒimepg*，是发动机转速和
喷射燃油质量的函数，*IMEPG = ƒimepg(F,N)*，其中：

- *IMEPG* 是最优总指示平均有效压力，单位
  Pa。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

最优总指示平均有效压力相对于压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_imepg` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Optimal friction mean effective pressure, f\_tqs\_fmep** — Optimal friction mean effective pressure `array`

最优摩擦平均有效压力查找表，
*ƒfmep*，是发动机转速和
喷射燃油质量的函数，*FMEP = ƒfmep(F,N)*，其中：

- *FMEP* 是最优摩擦平均有效压力，单位 Pa。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

最优摩擦平均有效压力相对于压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fmep` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Optimal pumping mean effective pressure, f\_tqs\_pmep** — Optimal pumping mean effective pressure `array`

最优泵气平均有效压力查找表，
*ƒpmep*，是发动机转速和
喷射燃油质量的函数，*PMEP = ƒpmep(F,N)*，其中：

- *PMEP* 是最优泵气平均有效压力，单位 Pa。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

最优泵气平均有效压力相对于进气歧管气体压力比（相对于压缩冲程喷射燃油质量和发动机转速）的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_pmep` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Friction multiplier as a function of temperature, f\_tqs\_fric\_temp\_mod** — Friction multiplier `array`

作为温度函数的摩擦乘数，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fric_temp_mod` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Friction multiplier temperature breakpoints, f\_tqs\_fric\_temp\_bpt** — Breakpoints `vector`

摩擦乘数温度断点，单位 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fric_temp_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Main start of injection timing efficiency multiplier, f\_tqs\_mainsoi\_eff** — MAINSOI efficiency multiplier `array`

主喷射开始 (SOI) 正时效率乘数查找表，
*ƒSOIeff*，是发动机转速和主 SOI 正时相对于最优正时的函数，*SOIeff =
ƒSOIeff(ΔSOI,N)*，其中：

- *SOIeff* 是主 SOI 正时效率
  乘数，无量纲。
- *ΔSOI* 是主 SOI 正时相对于最优正时，单位
  degBTDC。
- *N* 是发动机转速，单位 rpm。

SOI 正时效率乘数相对于主 SOI 正时（相对于最优正时）和发动机转速的 3D 图

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

### **Main start of injection timing relative to optimal timing breakpoints, f\_tqs\_mainsoi\_delta\_bpt** — Breakpoints `vector`

主喷射开始正时相对于最优正时的断点，单位
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

### **Intake manifold gas pressure efficiency multiplier, f\_tqs\_map\_eff** — Intake pressure efficiency multiplier `array`

进气歧管气体压力效率乘数查找表，
*ƒMAPeff*，是进气歧管气体压力比（相对于最优压力比）和 lambda 的函数，*MAPeff =
ƒMAPeff(MAPratio,λ)*，其中：

- *MAPeff* 是进气歧管气体压力
  效率乘数，无量纲。
- *MAPratio* 是进气歧管气体压力
  比（相对于最优压力比），无量纲。
- *λ* 是进气歧管气体 lambda，无量纲。

进气歧管气体压力效率乘数相对于进气歧管气体压力比（相对于最优压力比）和进气歧管气体 lambda 的 3D 图

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

### **Intake manifold gas pressure ratio relative to optimal pressure ratio breakpoints, f\_tqs\_map\_ratio\_bpt** — Breakpoints `[0.8;0.85;0.9;0.95;1;1.05;1.1;1.15;1.2;1.25;1.3;1.35;1.4;1.45;1.5]` (default) | `vector`

进气歧管气体压力比（相对于最优压力比）断点，
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

### **Intake manifold gas lambda breakpoints, f\_tqs\_lambda\_bpt** — Breakpoints `[1.5 1.678571428571429 1.857142857142857 2.035714285714286 2.214285714285714 2.392857142857143 2.571428571428571 2.75 2.928571428571429 3.107142857142857 3.285714285714286 3.464285714285714 3.642857142857143 3.821428571428572 4]` (default) | `vector`

进气歧管气体 lambda 断点，无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_lambda_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intake manifold gas temperature efficiency multiplier, f\_tqs\_mat\_eff** — Intake temperature efficiency multiplier `array`

进气歧管气体温度效率乘数查找表，
*ƒMATeff*，是发动机转速和进气歧管气体温度（相对于最优温度）的函数，
*MATeff =
ƒMATeff(ΔMAT,N)*，其中：

- *MATeff* 是进气歧管气体
  温度效率乘数，无量纲。
- *ΔMAT* 是进气歧管气体温度相对于最优
  温度，单位 K。
- *N* 是发动机转速，单位 rpm。

进气歧管气体温度效率乘数相对于进气气体氧气百分比（相对于最优）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mat_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intake manifold gas temperature relative to optimal gas temperature breakpoints, f\_tqs\_mat\_delta\_bpt** — Breakpoints `[-55;-50;-45;-40;-35;-30;-25;-20;-15;-10;-5;0;5;10;15]` (default) | `vector`

进气歧管气体温度相对于最优气体温度的断点，
单位 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_mat_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intake manifold gas oxygen efficiency multiplier, f\_tqs\_o2pct\_eff** — Intake oxygen efficiency multiplier `array`

进气歧管气体氧气效率乘数查找表，
*ƒO2Peff*，是发动机转速和进气歧管气体氧气百分比（相对于最优）的函数，*O2Peff =
ƒO2Peff(ΔO2P,N)*，其中：

- *O2Peff* 是进气歧管气体氧气
  效率乘数，无量纲。
- *ΔO2P* 是进气气体氧气百分比相对于最优，单位
  percent。
- *N* 是发动机转速，单位 rpm。

最优进气歧管气体氧气效率乘数相对于进气气体氧气百分比（相对于最优）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_o2pct_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intake gas oxygen percent relative to optimal breakpoints, f\_tqs\_o2pct\_delta\_bpt** — Breakpoints `vector`

进气气体氧气百分比相对于最优的断点，单位 percent。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_o2pct_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Fuel rail pressure efficiency multiplier, f\_tqs\_fuelpress\_eff** — Efficiency multiplier `array`

燃油轨压力效率乘数查找表，
*ƒFUELPeff*，是发动机转速
和燃油轨压力（相对于最优断点）的函数，*FUELPeff
= ƒFUELPeff(ΔFUELP,N)*，其中：

- *FUELPeff* 是燃油轨压力
  效率乘数，无量纲。
- *ΔFUELP* 是燃油轨压力相对于最优，单位
  MPa。
- *N* 是发动机转速，单位 rpm。

燃油轨压力效率乘数相对于燃油轨压力（相对于最优）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fuelpress_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Fuel rail pressure relative to optimal breakpoints, f\_tqs\_fuelpress\_delta\_bpt** — Breakpoints `vector`

燃油轨压力相对于最优的断点，单位 MPa。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_fuelpress_delta_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Fuel mass injection type identifier, f\_tqs\_f\_inj\_type** — Type identifier `0` (default) | `scalar`

燃油质量喷射类型标识符，无量纲。

在 CI Core Engine 和 CI
Controller 模块中，您可以使用喷射开始
(SOI) 和燃油质量输入向模型表示多次喷射。要指定喷射类型，请使用
**Fuel mass injection type identifier** 参数。

| 喷射类型 | 参数值 |
| --- | --- |
| Pilot | `0` |
| Main | `1` |
| Post | `2` |
| Passed | `3` |

模型将 `Passed` 燃油喷射和在阈值之后喷射的燃油视为未燃燃油。使用 **Maximum start of injection angle
for burned fuel, f\_tqs\_f\_burned\_soi\_limit** 参数指定
阈值。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_f_inj_type` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Indicated mean effective pressure post inject correction, f\_tqs\_imep\_post\_corr** — Post inject correction `array`

指示平均有效压力后喷射校正
查找表，*ƒIMEPpost*，是发动机
转速和燃油轨压力（相对于最优断点）的函数，
*ΔIMEPpost =
ƒIMEPpost(ΔSOIpost,Fpost)*，其中：

- *ΔIMEPpost* 是指示平均有效
  压力后喷射校正，单位 Pa。
- *ΔSOIpost* 是指示平均有效
  压力后喷射开始正时质心，单位 degATDC。
- *Fpost* 是指示平均有效
  压力后喷射质量总和，单位 mg per injection。

指示平均有效压力相对于压力后喷射开始正时和压力后喷射质量总和的 3D 图

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

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Indicated mean effective pressure post inject mass sum breakpoints, f\_tqs\_f\_post\_sum\_bpt** — Breakpoints `[0 3.571428571428572 7.142857142857143 10.71428571428571 14.28571428571429 17.85714285714286 21.42857142857143 25 28.57142857142857 32.14285714285715 35.71428571428572 39.28571428571428 42.85714285714285 46.42857142857143 50]` (default) | `vector`

指示平均有效压力后喷射质量总和断点，单位 mg per
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

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Indicated mean effective pressure post inject start of inject timing centroid breakpoints, f\_tqs\_soi\_post\_cent\_bpt** — Breakpoints `[150 160.7142857142857 171.4285714285714 182.1428571428571 192.8571428571429 203.5714285714286 214.2857142857143 225 235.7142857142857 246.4285714285714 257.1428571428571 267.8571428571429 278.5714285714286 289.2857142857143 300]` (default) | `vector`

指示平均有效压力后喷射开始正时质心
断点，单位 degATDC。

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

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Maximum start of injection angle for burned fuel, f\_tqs\_f\_burned\_soi\_limit** — Maximum SOI angle for burned fuel `500` (default) | `scalar`

已燃燃油的最大喷射开始角度，单位 degATDC。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_f_bpt` |
| **值：** | `500` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### 排气

#### 排气温度 - Simple Torque Lookup

### **Exhaust temperature table, f\_t\_exh** — Lookup table `array`

排气温度查找表是喷射燃油质量和发动机
转速的函数

Texh=fTexh(F,N)

其中：

- Texh 是
  排气温度，单位 K。
- *F* 是喷射燃油质量，单位 mg
  per injection。
- *N* 是发动机转速，单位 rpm。

排气温度相对于发动机转速和发动机扭矩的 3D 图

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

要启用此参数，请在 **Torque model** 中选择
`Simple Torque Lookup`。

### **Fuel mass per injection breakpoints, f\_t\_exh\_f\_bpt** — Breakpoints `[0 3.5714 7.1429 10.7143 14.2857 17.8571 21.4286 25 28.5714 32.1429 35.7143 39.2857 42.8571 46.4286 50]` (default) | `vector`

用于排气温度查找表的发动机负荷断点，单位 mg per
injection。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh_f_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Simple Torque Lookup`。

### **Speed breakpoints, f\_t\_exh\_n\_bpt** — Breakpoints `[1000 1410.7143 1821.4286 2232.1429 2642.8571 3053.5714 3464.2857 3875 4285.7143 4696.4286 5107.1429 5517.8571 5928.5714 6339.2857 6750]` (default) | `vector`

用于排气温度查找表的发动机转速断点，单位 rpm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_t_exh_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Simple Torque Lookup`。

#### 排气温度 - Torque Structure

### **Optimal exhaust manifold gas temperature, f\_tqs\_exht** — Optimal exhaust manifold gas temperature `array`

最优排气歧管气体温度查找表，
*ƒTexh*，是发动机转速
和喷射燃油质量的函数，*Texhopt =
ƒTexh(F,N)*，其中：

- *Texhopt* 是最优排气歧管气体
  温度，单位 K。
- *F* 是压缩冲程喷射燃油质量，单位 mg per
  injection。
- *N* 是发动机转速，单位 rpm。

最优排气歧管气体温度相对于压缩冲程喷射燃油质量和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Main start of injection timing exhaust temperature efficiency multiplier, f\_tqs\_exht\_mainsoi\_eff** — Main SOI timing efficiency multiplier `array`

主喷射开始 (SOI) 正时排气温度
效率乘数查找表，*ƒSOIexhteff*，是
发动机转速和喷射燃油质量的函数，
*SOIexhteff =
ƒSOIexhteff(ΔSOI,N)*，其中：

- *SOIexhteff* 是主 SOI 排气
  温度效率乘数，无量纲。
- *ΔSOI* 是主 SOI 正时相对于最优正时，单位
  degBTDC。
- *N* 是发动机转速，单位 rpm。

SOI 排气温度效率乘数相对于主 SOI 正时（相对于最优正时）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_mainsoi_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intake manifold gas pressure exhaust temperature efficiency multiplier, f\_tqs\_exht\_map\_eff** — Intake manifold efficiency multiplier `array`

进气歧管气体压力排气温度效率
乘数查找表，*ƒMAPexheff*，是
进气歧管气体压力比（相对于最优压力比）和 lambda 的函数，
*MAPexheff =
ƒMAPexheff(MAPratio,λ)*，其中：

- *MAPexheff* 是进气歧管气体
  压力排气温度效率乘数，无量纲。
- *MAPratio* 是进气歧管气体压力
  比（相对于最优压力比），无量纲。
- *λ* 是进气歧管气体 lambda，无量纲。

进气歧管气体压力排气温度效率乘数相对于进气歧管气体压力比（相对于最优压力比）和进气歧管气体 lambda 的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_map_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intake manifold gas temperature exhaust temperature efficiency multiplier, f\_tqs\_exht\_mat\_eff** — Intake manifold efficiency multiplier `array`

进气歧管气体温度排气温度
效率乘数查找表，*ƒMATexheff*，是
发动机转速和进气歧管气体温度（相对于最优温度）的函数，
*MATexheff =
ƒMATexheff(ΔMAT,N)*，其中：

- *MATexheff* 是进气歧管气体
  温度排气温度效率乘数，无量纲。
- *ΔMAT* 是进气歧管气体温度相对于最优
  温度，单位 K。
- *N* 是发动机转速，单位 rpm。

进气歧管气体温度排气温度效率乘数相对于进气歧管气体温度（相对于最优温度）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_mat_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Intake manifold gas oxygen exhaust temperature efficiency multiplier, f\_tqs\_exht\_o2pct\_eff** — Intake manifold efficiency multiplier `array`

进气歧管气体氧气排气温度效率
乘数查找表，*ƒO2Pexheff*，是
发动机转速和进气歧管气体氧气百分比（相对于最优）的函数，
*O2Pexheff =
ƒO2Pexheff(ΔO2P,N)*，其中：

- *O2Pexheff* 是进气歧管气体氧气
  排气温度效率乘数，无量纲。
- *ΔO2P* 是进气气体氧气百分比相对于最优，单位
  percent。
- *N* 是发动机转速，单位 rpm。

最优进气歧管气体氧气排气温度效率乘数相对于进气气体氧气百分比（相对于最优）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_o2pct_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Fuel rail pressure exhaust temperature efficiency multiplier, f\_tqs\_exht\_fuelpress\_eff** — Fuel rail pressure exhaust temperature efficiency multiplier `array`

燃油轨压力排气温度效率
乘数查找表，*ƒFUELPexheff*，是
发动机转速和燃油轨压力（相对于最优断点）的函数，
*FUELPexheff =
ƒFUELPexheff(ΔFUELP,N)*，其中：

- *FUELPexheff* 是燃油轨压力
  排气温度效率乘数，无量纲。
- *ΔFUELP* 是燃油轨压力相对于最优，单位
  MPa。
- *N* 是发动机转速，单位 rpm。

燃油轨压力排气温度效率乘数相对于燃油轨压力（相对于最优）和发动机转速的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_fuelpress_eff` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

### **Post-injection cylinder wall heat loss transfer coefficient, f\_tqs\_exht\_post\_inj\_wall\_htc** — Post-injection offset `0` (default) | `scalar`

后喷射气缸壁热损失传热系数，单位 W/K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqs_exht_post_inj_wall_htc` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Torque model** 中选择
`Torque Structure`。

#### 排放

### **CO2 mass fraction table, f\_CO2\_frac** — Carbon dioxide (CO2) emission lookup table `array`

CI Core Engine CO2 排放
质量分数查找表是发动机扭矩和发动机
转速的函数，*CO2 Mass Fraction* = ƒ(*Speed*, *Torque*)，
其中：

- *CO2 Mass Fraction* 是 CO2 排放
  质量分数，无量纲。
- *Speed* 是发动机转速，单位 rpm。
- *Torque* 是发动机扭矩，单位 N·m。

CO2 排放质量分数相对于发动机转速和发动机扭矩的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_CO2_frac` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Exhaust** 选项卡上，选择
**CO2**。

### **CO mass fraction table, f\_CO\_frac** — Carbon monoxide (CO) emission lookup table `array`

CI Core Engine CO 排放
质量分数查找表是发动机扭矩和发动机
转速的函数，*CO Mass Fraction* = ƒ(*Speed*, *Torque*)，
其中：

- *CO Mass Fraction* 是 CO 排放
  质量分数，无量纲。
- *Speed* 是发动机转速，单位 rpm。
- *Torque* 是发动机扭矩，单位 N·m。

CO 排放质量分数相对于发动机转速和发动机扭矩的 3D 图

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_CO_frac` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请在 **Exhaust** 选项卡上，选择
**CO**。

### **HC mass fraction table, f\_HC\_frac** — Hydrocarbon (HC) emission lookup table `array`

CI Core Engine HC 排放
质量分数查找表是发动机扭矩和发动机
转速的函数，*HC Mass Fraction* = ƒ(*Speed*, *Torque*)，
其中：

- *HC Mass Fraction* 是 HC 排放
  质量分数，无量纲。
- *Speed* 是发动机转速，单位 rpm。
- *Torque* 是发动机扭矩，单位 N·m。

HC 排放质量分数相对于发动机转速和发动机扭矩的 3D 图

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

要启用此参数，请在 **Exhaust** 选项卡上，选择
**HC**。

### **NOx mass fraction table, f\_NOx\_frac** — Nitric oxide and nitrogen dioxide (NOx) emission lookup table `array`

CI Core Engine NOx
排放质量分数查找表是发动机扭矩
和发动机转速的函数，*NOx Mass Fraction* = ƒ(*Speed*, *Torque*)，
其中：

- *NOx Mass Fraction* 是 NOx 排放
  质量分数，无量纲。
- *Speed* 是发动机转速，单位 rpm。
- *Torque* 是发动机扭矩，单位 N·m。

NOx 排放质量分数相对于发动机转速和发动机扭矩的 3D 图

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

要启用此参数，请在 **Exhaust** 选项卡上，选择
**NOx**。

### **PM mass fraction table, f\_PM\_frac** — Particulate matter (PM) emission lookup table `array`

CI Core Engine PM 排放质量分数
查找表是发动机扭矩和发动机转速的函数，其中：

- *PM* 是 PM 排放质量分数，
  无量纲。
- *Speed* 是发动机转速，单位 rpm。
- *Torque* 是发动机扭矩，单位 N·m。

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

要启用此参数，请在 **Exhaust** 选项卡上，选择
**PM**。

### **Engine speed breakpoints, f\_exhfrac\_n\_bpt** — Breakpoints `[750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]` (default) | `vector`

用于排放质量分数查找表的发动机转速断点，单位
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

要启用此参数，请在 **Exhaust** 选项卡上，选择
**CO2**、**CO**、**NOx**、
**HC** 或 **PM**。

### **Engine torque breakpoints, f\_exhfrac\_trq\_bpt** — Breakpoints `[0 15 26.4285714285714 37.8571428571429 49.2857142857143 60.7142857142857 72.1428571428571 83.5714285714286 95 106.428571428571 117.857142857143 129.285714285714 140.714285714286 152.142857142857 163.571428571429 175]` (default) | `vector`

用于排放质量分数查找表的发动机扭矩断点，单位
N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
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

### **Exhaust gas specific heat at constant pressure, cp\_exh** — Specific heat `1005` (default) | `scalar`

排气气体定压比热，Cpexh，单位 J/(kg·K)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `cp_exh` |
| **值：** | `1005` (default) | `scalar` |
| **数据类型：** | `double` |

### 燃料

### **Stoichiometric air-fuel ratio, afr\_stoich** — Air-fuel ratio `14.6` (default) | `scalar`

空燃比，AFR。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `afr_stoich` |
| **值：** | `14.6` (default) | `scalar` |
| **数据类型：** | `double` |

### **Fuel lower heating value, fuel\_lhv** — Heating value `42e6` (default) | `scalar`

燃油低热值，*LHV*，单位 J/kg。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `fuel_lhv` |
| **值：** | `42e6` (default) | `scalar` |
| **数据类型：** | `double` |

### **Fuel specific gravity, fuel\_sg** — Specific gravity `0.832` (default) | `scalar`

燃油比重，
*Sgfuel*，
无量纲。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `fuel_sg` |
| **值：** | `0.832` (default) | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Core Engine

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

从进气口到排气口的压燃式发动机

CI Core Engine 模块实现从进气口到排气口的压燃式
(CI) 发动机。您可以将该模块
用于硬件在环 (HIL) 发动机控制设计或车辆级
燃油经济性和性能仿真。

CI Core Engine 模块计算：

- 制动扭矩
- 排气温度
- 空燃比 (AFR)
- 燃油轨压力
- 发动机原始 (EO) 排气排放：

  - 碳氢化合物 (HC)
  - 一氧化碳 (CO)
  - 一氧化氮和二氧化氮 (NOx)
  - 二氧化碳 (CO2)
  - 颗粒物 (PM)

### 空气质量流量

为计算空气质量流量，压燃式 (CI)
发动机使用 CI Engine Speed-Density Air Mass Flow Model。速度密度
模型使用速度密度方程计算发动机空气
质量流量，将发动机进气口质量流量与进气
歧管压力、进气歧管温度和发动机转速相关联。

### 制动扭矩

为计算发动机扭矩，您可以将模块配置为
使用以下任一扭矩模型。

| 制动扭矩模型 | 描述 |
| --- | --- |
| CI Engine Torque Structure Model | CI 核心发动机扭矩结构模型通过在这些发动机条件偏离标称值时降低最大发动机扭矩潜力来确定发动机扭矩：  - 喷射开始 (SOI) 正时 - 排气背压 - 已燃燃油质量 - 进气歧管气体压力、温度和氧气百分比 - 燃油轨压力  为考虑后喷射燃油对扭矩的影响，模型使用校准的扭矩偏移表。 |
| CI Engine Simple Torque Model | 对于简单发动机扭矩计算，CI 发动机使用作为发动机转速和喷射燃油质量函数的扭矩查找表映射。 |

### 燃油流量

在 CI Core Engine 和 CI
Controller 模块中，您可以使用喷射开始
(SOI) 和燃油质量输入向模型表示多次喷射。要指定喷射类型，请使用
**Fuel mass injection type identifier** 参数。

| 喷射类型 | 参数值 |
| --- | --- |
| Pilot | `0` |
| Main | `1` |
| Post | `2` |
| Passed | `3` |

模型将 `Passed` 燃油喷射和在阈值之后喷射的燃油视为未燃燃油。使用 **Maximum start of injection angle
for burned fuel, f\_tqs\_f\_burned\_soi\_limit** 参数指定
阈值。

为计算发动机
燃油质量流量，CI Core Engine 模块使用由喷油器输送的燃油质量流量和
发动机空气流量。

m˙fuel=N⋅NcylCps(60smin)(1000mgg)∑mfuel,inj

为计算高保真模型的燃油经济性，模块使用
体积燃油流量。

Qfuel=m˙fuel(1000kgm3)Sgfuel

方程使用这些变量。

|  |  |
| --- | --- |
| m˙fuel | 燃油质量流量，g/s |
| *mfuel,inj* | 每次喷射燃油质量 |
| Cps | 每动力冲程的曲轴转数，rev/stroke |
| Ncyl | 发动机气缸数 |
| *N* | 发动机转速，rpm |
| *Qfuel* | 体积燃油流量 |
| *Sgfuel* | 燃油比重 |

模块使用内部信号 `FlwDir` 跟踪流动方向。

### 空燃比

为计算空燃 (AFR) 比，CI Core
Engine 和 SI Core Engine 模块实现此方程。

AFR=m˙airm˙fuel

CI Core Engine 使用此方程计算
相对 AFR。

λ=AFRAFRs

为计算废气再循环 (EGR)，模块实现此
方程。该计算将 EGR 表示为总进气口流量的百分比。

EGRpct=100m˙intk,bm˙intk=100yintk,b

方程使用这些变量。

|  |  |
| --- | --- |
| AFR | 空燃比 |
| *AFRs* | 化学计量空燃比 |
| m˙intk | 发动机空气质量流量 |
| m˙fuel | 燃油质量流量 |
| λ | 相对 AFR |
| *yintk,b* | 进气已燃质量分数 |
| *EGRpct* | EGR 百分比 |
| m˙intk,b | 再循环已燃气体质量流量 |

### 排气温度

排气温度计算取决于扭矩模型。对于两种扭矩模型，模块都实现查找表。

| 扭矩模型 | 描述 | 方程 |
| --- | --- | --- |
| `Simple Torque Lookup` | 排气温度查找表是喷射燃油质量和发动机转速的函数。 | Texh=fTexh(F,N) |
| `Torque Structure` | 标称排气温度 *Texhnom* 是这些排气温度效率的乘积：  - SOI 正时 - 进气歧管气体压力 - 进气歧管气体温度 - 进气歧管气体氧气百分比 - 燃油轨压力 - 最优温度  排气温度 *Texhnom* 由后温度效应 *ΔTpost* 偏移，该效应考虑膨胀和排气冲程期间的后喷射和晚喷射。 | Texhnom=SOIexhteffMAPexhteffMATexhteffO2pexhteffFUELPexhteffTexhoptTexh=Texhnom+ΔTpostSOIexhteff=fSOIexhteff(ΔSOI,N)MAPexhteff=fMAPexhteff(MAPratio,λ)MATexhteff=fMATexhteff(ΔMAT,N)O2pexhteff=fO2pexhteff(ΔO2p,N)Texhopt=fTexh(F,N) |

方程使用这些变量。

|  |  |
| --- | --- |
| *F* | 压缩冲程喷射燃油质量 |
| *N* | 发动机转速 |
| *Texh* | 排气歧管气体温度 |
| *Texhopt* | 最优排气歧管气体温度 |
| *ΔTpost* | 后喷射温度效应 |
| *Texhnom* | 标称排气温度 |
| *SOIexhteff* | 主 SOI 排气温度效率乘数 |
| *ΔSOI* | 主 SOI 正时相对于最优正时 |
| *MAPexheff* | 进气歧管气体压力排气温度效率乘数 |
| *MAPratio* | 进气歧管气体压力比（相对于最优压力比） |
| *λ* | 进气歧管气体 lambda |
| *MATexheff* | 进气歧管气体温度排气温度效率乘数 |
| *ΔMAT* | 进气歧管气体温度相对于最优温度 |
| *O2Pexheff* | 进气歧管气体氧气排气温度效率乘数 |
| *ΔO2P* | 进气气体氧气百分比相对于最优 |
| *FUELPexheff* | 燃油轨压力排气温度效率乘数 |
| *ΔFUELP* | 燃油轨压力相对于最优 |

### EO 排气排放

模块计算这些发动机原始 (EO) 排气排放：

- 碳氢化合物 (HC)
- 一氧化碳 (CO)
- 一氧化氮和二氧化氮 (NOx)
- 二氧化碳 (CO2)
- 颗粒物 (PM)

排气温度决定比焓。

hexh=CpexhTexh

排气质量流量是进气口空气
质量流量和燃油质量流量之和。

m˙exh=m˙intake+m˙fuel

为计算排气排放，模块将
排放质量分数乘以排气质量流量。为确定
排放质量分数，模块使用作为
发动机扭矩和转速函数的查找表。

yexh,i=fi\_frac(Tbrake,N)m˙exh,i=m˙exhyexh,i

进入进气口的空气和燃油分数、喷射
燃油以及化学计量 AFR 决定离开排气的空气质量分数。

yexh,air=max[yin,air−m˙fuel+yin,fuelm˙intakem˙fuel+m˙intakeAFRs]

如果发动机在化学计量或富燃
AFR 下运行，则没有空气离开排气。未燃碳氢化合物和已燃气体
构成排气气体的剩余部分。此方程确定
排气已燃气体质量分数。

yexh,b=max[(1−yexh,air−yexh,HC),0]

方程使用这些变量。

|  |  |
| --- | --- |
| Texh | 发动机排气温度 |
| hexh | 排气歧管入口比焓 |
| Cpexh | 排气气体比热 |
| m˙intk | 进气口空气质量流量 |
| m˙fuel | 燃油质量流量 |
| m˙exh | 排气质量流量 |
| yin,fuel | 进气燃油质量分数 |
| *yexh,i* | 排气质量分数，其中 i = CO2、CO、HC、NOx、air、burned gas 和 PM |
| m˙exh,i | 排气质量流量，其中 i = CO2、CO、HC、NOx、air、burned gas 和 PM |
| *Tbrake* | 发动机制动扭矩 |
| *N* | 发动机转速 |
| *yexh,air* | 排气空气质量分数 |
| *yexh,b* | 排气已燃空气质量分数 |

### 功率核算

对于功率核算，模块实现的方程取决于 **Torque model**。

当您将 **Torque model** 设置为 `Simple Torque Lookup` 时，模块实现这些方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrIntkHeatFlw` | 进气热流量 | m˙intkhintk |
| `PwrExhHeatFlw` | 排气热流量 | −m˙exhhexh |
| `PwrCrkshft` | 曲轴功率 | −Tbrakeω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFuel` | 燃油输入功率 | m˙fuelLHV |
| `PwrLoss` | 所有损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh |
| `PwrStored` — 存储能量变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |

当您将 **Torque model** 设置为 `Torque Structure` 时，模块实现这些方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrIntkHeatFlw` | 进气热流量 | m˙intkhintk |
| `PwrExhHeatFlw` | 排气热流量 | −m˙exhhexh |
| `PwrCrkshft` | 曲轴功率 | −Tbrakeω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrFuel` | 燃油输入功率 | m˙fuelLHV |
| `PwrFricLoss` | 摩擦损失 | −Tfricω |
| `PwrPumpLoss` | 泵气损失 | −Tpumpω |
| `PwrHeatTrnsfrLoss` | 传热损失 | Tbrakeω−m˙fuelLHV−m˙intkhintk+m˙exhhexh+Tfricω+Tpumpω |
| `PwrStored` — 存储能量变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |

|  |  |
| --- | --- |
| *hexh* | 排气歧管入口比焓 |
| *hintk* | 进气口比焓 |
| m˙intk | 进气口空气质量流量 |
| m˙fuel | 燃油质量流量 |
| m˙exh | 排气质量流量 |
| *ω* | 发动机转速 |
| *Tbrake* | 制动扭矩 |
| *Tpump* | 发动机泵气功偏移至内部扭矩 |
| *Tfric* | 发动机摩擦扭矩 |
| *LHV* | 燃油低热值 |
