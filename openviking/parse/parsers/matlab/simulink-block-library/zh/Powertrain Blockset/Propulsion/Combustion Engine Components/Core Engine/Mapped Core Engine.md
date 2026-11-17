---
type: simulink-block
title: 'Mapped Core Engine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components / Core Engine'
documentation_page: 'mappedcoreengine'
documentation_source_path: 'ref/mappedcoreengine.html'
language: zh-CN
chinese_source: worker-translation
---

# Mapped Core Engine

## 端口
```yaml
ports:
- name: '*<TrqCmd>*'
  summary: 发动机负载 TrqCmd（默认）
  direction: input
- name: '*<EngSpd>*'
  summary: 发动机转速 EngSpd（默认）
  direction: input
- name: '*<EngTemp>*'
  summary: 发动机温度 EngTemp（默认）
  direction: input
- name: '*<EngTrq>*'
  summary: 功率 EngTrq（默认）
  direction: output
- name: '*<IntkAirMassFlw>*'
  summary: 空气质量流量 IntkAirMassFlw（默认）
  direction: output
- name: '*<FuelMassFlw>*'
  summary: 燃料流量 FuelMassFlw（默认）
  direction: output
- name: '*<ExhManGasTemp>*'
  summary: 排气温度 ExhManGasTemp（默认）
  direction: output
- name: '*<Bsfc>*'
  summary: 效率 Bsfc（默认）
  direction: output
- name: '*<EoHC>*'
  summary: 碳氢化合物排放 EoHC（默认）
  direction: output
- name: '*<EoCO>*'
  summary: 一氧化碳排放 EoCO（默认）
  direction: output
- name: '*<EoNOx>*'
  summary: 一氧化氮和二氧化氮排放 EoNOx（默认）
  direction: output
- name: '*<EoCO2>*'
  summary: 二氧化碳排放 EoCO2（默认）
  direction: output
- name: '*<EoPm>*'
  summary: 颗粒物排放 EoPm（默认）
  direction: output
```

### 输入

### ***`<TrqCmd>`*** — 发动机负载 `TrqCmd`（默认）

发动机负载，*L*。发动机负载的示例包括：

- 指令扭矩

- 发动机气缸中的指令指示平均有效压力（IMEP）

- 归一化气缸空气质量

- 喷射燃料质量

#### 依赖关系

要指定发动机负载端口名称，请在 **Configuration** 选项卡中，在 **Load input port name** 参数字段中输入名称。

### ***`<EngSpd>`*** — 发动机转速 `EngSpd`（默认）

发动机转速，*N*。

#### 依赖关系

要指定发动机负载端口名称，请在 **Configuration** 选项卡中，在 **Speed input port name** 参数字段中输入名称。

### ***`<EngTemp>`*** — 发动机温度 `EngTemp`（默认）

发动机温度，*T*。

#### 依赖关系

要创建发动机温度输入端口名称，请选择 **Input engine temperature** 参数字段。

要指定发动机负载端口名称，请在 **Configuration** 选项卡中，在 **Temperature input port name** 参数字段中输入名称。
### 输出

### ***`<EngTrq>`*** — 功率 `EngTrq`（默认）

发动机功率，Tbrake。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡中，选择 **Power**。
- 要指定端口名称，请在 **Power** 选项卡中，在 **Power output port name** 参数字段中输入名称。

### ***`<IntkAirMassFlw>`*** — 空气质量流量 `IntkAirMassFlw`（默认）

发动机空气质量流量，m˙intk。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡中，选择 **Air**。
- 要指定端口名称，请在 **Air** 选项卡中，在 **Air output port name** 参数字段中输入名称。

### ***`<FuelMassFlw>`*** — 燃料流量 `FuelMassFlw`（默认）

发动机燃料流量，m˙fuel。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡中，选择 **Fuel**。
- 要指定端口名称，请在 **Fuel** 选项卡中，在 **Fuel output port name** 参数字段中输入名称。

### ***`<ExhManGasTemp>`*** — 排气温度 `ExhManGasTemp`（默认）

发动机排气温度，Texh。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡中，选择 **Temperature**。
- 要指定端口名称，请在 **Temperature** 选项卡中，在 **Temperature output port name** 参数字段中输入名称。

### ***`<Bsfc>`*** — 效率 `Bsfc`（默认）

制动比燃料消耗（BSFC），*Eff*。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡中，选择 **Efficiency**。
- 要指定端口名称，请在 **Efficiency** 选项卡中，在 **Efficiency output port name** 参数字段中输入名称。

### ***`<EoHC>`*** — 碳氢化合物排放 `EoHC`（默认）

碳氢化合物排放，*HC*。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡中，选择 **HC**。
- 要指定端口名称，请在 **HC** 选项卡中，在 **HC output port name** 参数字段中输入名称。

### ***`<EoCO>`*** — 一氧化碳排放 `EoCO`（默认）

一氧化碳排放，*CO*。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡中，选择 **CO**。
- 要指定端口名称，请在 **CO** 选项卡中，在 **CO output port name** 参数字段中输入名称。

### ***`<EoNOx>`*** — 一氧化氮和二氧化氮排放 `EoNOx`（默认）

一氧化氮和二氧化氮排放，*NOx*。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡中，选择 **NOx**。
- 要指定端口名称，请在 **NOx** 选项卡中，在 **NOx output port name** 参数字段中输入名称。

### ***`<EoCO2>`*** — 二氧化碳排放 `EoCO2`（默认）

二氧化碳排放，*CO2*。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡中，选择 **CO2**。
- 要指定端口名称，请在 **CO2** 选项卡中，在 **CO2 output port name** 参数字段中输入名称。

### ***`<EoPm>`*** — 颗粒物排放 `EoPm`（默认）

颗粒物排放，*PM*。

#### 依赖关系

- 要创建此端口，请在 **Configuration** 选项卡上选择 **PM**。
- 要指定端口名称，请在 **PM** 选项卡上，在 **PM output port name** 参数字段中输入名称。
## 参数
```yaml
parameters:
- name: Engine Type
  summary: 发动机类型图像 Compression-ignition (CI)（默认）| Spark-ignition (SI)
  group: ''
  block_parameter: EngineType
  values: Compression-ignition (CI)（默认）| Spark-ignition (SI)
- name: Load input port name
  summary: 名称 TrqCmd（默认）
  group: ''
  block_parameter: rowVarName
  values: TrqCmd（默认）
- name: Breakpoints for load input
  summary: 断点 vector
  group: ''
  block_parameter: rowbreakpoints
  values: vector
- name: Speed input port name
  summary: 名称 EngSpd（默认）
  group: ''
  block_parameter: colVarName
  values: EngSpd（默认）
- name: Breakpoints for speed input
  summary: 断点 vector
  group: ''
  block_parameter: colbreakpoints
  values: vector
- name: Temperature input port name
  summary: 名称 EngTemp（默认）
  group: ''
  block_parameter: TmpVarName
  values: EngTemp（默认）
- name: Breakpoints for temperature input
  summary: 断点 [233.15 273.15 373.15]（默认）| vector
  group: ''
  block_parameter: Tmpbreakpoints
  values: '[233.15 273.15 373.15]（默认）| vector'
- name: Output Configuration
  summary: 创建输出端口 on（默认）| off
  group: ''
- name: Power 输出端口名称
  summary: Power EngTrq（默认）
  group: ''
  block_parameter: Name1
  values: EngTrq（默认）
- name: Power 表
  summary: Power array
  group: ''
  block_parameter: Name1_z
  values: array
- name: Air 输出端口名称
  summary: Air IntkAirMassFlw（默认）
  group: ''
  block_parameter: Name2
  values: IntkAirMassFlw（默认）
- name: Air 表
  summary: Air array
  group: ''
  block_parameter: Name2_z
  values: array
- name: Fuel 输出端口名称
  summary: Fuel FuelMassFlw（默认）
  group: ''
  block_parameter: Name3
  values: FuelMassFlw（默认）
- name: Fuel 表
  summary: Fuel array
  group: ''
  block_parameter: Name3_z
  values: array
- name: Temperature 输出端口名称
  summary: Temperature ExhManGasTemp（默认）
  group: ''
  block_parameter: Name4
  values: ExhManGasTemp（默认）
- name: Temperature table
  summary: Temperature array
  group: ''
  block_parameter: Name4_z
  values: array
- name: 效率输出端口名称
  summary: 效率 Bsfc（默认）
  group: ''
  block_parameter: Name5
  values: Bsfc (default)
- name: Efficiency table
  summary: Efficiency array
  group: ''
  block_parameter: Name5_z
  values: array
- name: HC 输出端口名称
  summary: 碳氢化合物 EoHC（默认）
  group: ''
  block_parameter: Name6
  values: EoHC (default)
- name: HC table
  summary: Hydrocarbon array
  group: ''
  block_parameter: Name6_z
  values: array
- name: CO 输出端口名称
  summary: 二氧化碳 EoCO（默认）
  group: ''
  block_parameter: Name7
  values: EoCO (default)
- name: CO table
  summary: Carbon dioxide array
  group: ''
  block_parameter: Name7_z
  values: array
- name: NOx 输出端口名称
  summary: 一氧化氮 *NO* 和二氧化氮 *NO2* EoNOx（默认）
  group: ''
  block_parameter: Name8
  values: EoNOx (default)
- name: NOx table
  summary: 一氧化氮 *NO* 和二氧化氮 *NO2* array
  group: ''
  block_parameter: Name8_z
  values: array
- name: CO2 输出端口名称
  summary: 二氧化碳 EoCO2（默认）
  group: ''
  block_parameter: Name9
  values: EoCO2（默认）
- name: CO2 表
  summary: 二氧化碳 array
  group: ''
  block_parameter: Name9_z
  values: array
- name: PM 输出端口名称
  summary: 颗粒物 EoPm（默认）
  group: ''
  block_parameter: Name10
  values: EoPm（默认）
- name: PM 表
  summary: 颗粒物 array
  group: ''
  block_parameter: Name10_z
  values: array
```

#### 配置

### **Engine Type** — 发动机类型图像 `Compression-ignition (CI)`（默认）| `Spark-ignition (SI)`

要在模块中使用的已映射内燃机图像类型。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EngineType` |
| **值：** | `Compression-ignition (CI)`（默认）| `Spark-ignition (SI)` |
| **数据类型：** | `character vector` |

### **Load input port name** — 名称 `TrqCmd`（默认）

发动机负荷输入端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rowVarName` |
| **值：** | `TrqCmd`（默认） |
| **数据类型：** | `character vector` |

### **Breakpoints for load input** — 断点 `vector`

发动机负荷输入的断点。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `rowbreakpoints` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Speed input port name** — 名称 `EngSpd`（默认）

转速输入端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `colVarName` |
| **值：** | `EngSpd`（默认） |
| **数据类型：** | `character vector` |

### **Breakpoints for speed input** — 断点 `vector`

发动机转速输入的断点。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `colbreakpoints` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Temperature input port name** — 名称 `EngTemp`（默认）

温度输入端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `TmpVarName` |
| **值：** | `EngTemp`（默认） |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

### **Breakpoints for temperature input** — 断点 `[233.15 273.15 373.15]`（默认）| `vector`

发动机温度输入的断点。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tmpbreakpoints` |
| **值：** | `[233.15 273.15 373.15]`（默认）| `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 **Input engine temperature**。

### **Output Configuration** — 创建输出端口 `on`（默认）| `off`

创建输出端口。

#### 依赖关系

下表总结了为每个 **Output** 参数选择所创建的输出端口。

| 输出选择 | 创建端口 | 创建选项卡 |
| --- | --- | --- |
| **Power** | `EngTrq` | **Power** |
| **Air** | `IntkAirMassFlw` | **Air** |
| **Fuel** | `FuelMassFlw` | **Fuel** |
| **Temperature** | `ExhManGasTemp` | **Temperature** |
| **Efficiency** | `Bsfc` | **Efficiency** |
| **HC** | `EoHC` | **HC** |
| **CO** | `EoCO` | **CO** |
| **NOx** | `EoNOx` | **NOx** |
| **CO2** | `EoCO2` | **CO2** |
| **PM** | `EoPm` | **PM** |

#### Power

### **Power 输出端口名称** — Power `EngTrq`（默认）

Power 输出端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name1` |
| **值：** | `EngTrq`（默认） |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在 **Configuration** 选项卡上选择 **Power**。

### **Power 表** — Power `array`

Power 表。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name1_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **Configuration** 选项卡上选择 **Power**。

#### Air

### **Air 输出端口名称** — Air `IntkAirMassFlw`（默认）

空气质量流量输出端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name2` |
| **值：** | `IntkAirMassFlw`（默认） |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在 **Configuration** 选项卡上选择 **Air**。

### **Air 表** — Air `array`

空气质量流量表。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name2_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **Configuration** 选项卡上选择 **Air**。

#### Fuel

### **Fuel 输出端口名称** — Fuel `FuelMassFlw`（默认）

Fuel 输出端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name3` |
| **值：** | `FuelMassFlw`（默认） |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在 **Configuration** 选项卡上选择 **Fuel**。

### **Fuel 表** — Fuel `array`

Fuel 表。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name3_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在 **Configuration** 选项卡上选择 **Fuel**。

#### Temperature

### **Temperature 输出端口名称** — Temperature `ExhManGasTemp`（默认）

Temperature 输出端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name4` |
| **值：** | `ExhManGasTemp`（默认） |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在 **Configuration** 选项卡上选择 **Temperature**。

### **Temperature table** — Temperature `array`

Temperature table.

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name4_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **Temperature**。

#### Efficiency

### **效率输出端口名称** — 效率 `Bsfc`（默认）

效率输出端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name5` |
| **值：** | `Bsfc` (default) |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **Efficiency**。

### **Efficiency table** — Efficiency `array`

Efficiency table.

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name5_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **Efficiency**。

#### HC

### **HC 输出端口名称** — 碳氢化合物 `EoHC`（默认）

碳氢化合物输出端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name6` |
| **值：** | `EoHC` (default) |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **HC**。

### **HC table** — Hydrocarbon `array`

Hydrocarbon table.

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name6_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **HC**。

#### CO

### **CO 输出端口名称** — 二氧化碳 `EoCO`（默认）

一氧化碳输出端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name7` |
| **值：** | `EoCO` (default) |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **CO**。

### **CO table** — Carbon dioxide `array`

Carbon dioxide table.

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name7_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **CO**。

#### NOx

### **NOx 输出端口名称** — 一氧化氮 *NO* 和二氧化氮 *NO2* `EoNOx`（默认）

NOx 输出端口名称。NOx 是一氧化氮 *NO* 和
nitrogen dioxide *NO2*.

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name8` |
| **值：** | `EoNOx` (default) |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **NOx**。

### **NOx table** — 一氧化氮 *NO* 和二氧化氮 *NO2* `array`

NOx 排放表。NOx 是一氧化氮 *NO* 和二氧化氮 *NO2*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name8_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **NOx**。

#### CO2

### **CO2 输出端口名称** — 二氧化碳 `EoCO2`（默认）

二氧化碳输出端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name9` |
| **值：** | `EoCO2`（默认） |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **CO2**。

### **CO2 表** — 二氧化碳 `array`

二氧化碳表。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name9_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **CO2**。

#### PM

### **PM 输出端口名称** — 颗粒物 `EoPm`（默认）

颗粒物输出端口名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name10` |
| **值：** | `EoPm`（默认） |
| **数据类型：** | `character vector` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **PM**。

### **PM 表** — 颗粒物 `array`

颗粒物表。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Name10_z` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请在**配置**选项卡上选择 **PM**。
## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Core Engine

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

使用查找表的稳态核心发动机模型

Mapped Core Engine 模块使用功率、空气质量流量、燃料流量、排气温度、效率和排放性能查找表实现稳态核心发动机模型。您可以将该模块用于：

- 硬件在环（HIL）发动机控制设计。
- 车辆级燃油经济性和性能仿真。

该模块使您能够为这些发动机特性指定查找表。查找表是发动机负载 *L* 和发动机转速 *N* 的函数。如果您选择 **Input engine temperature**，则这些表还是发动机温度 *T* 的函数。

- 功率
- 空气
- 燃料
- 温度
- 效率
- 排放

  - 碳氢化合物（HC）
  - 一氧化碳（CO）
  - 一氧化氮和二氧化氮（NOx）
  - 二氧化碳（CO2）
  - 颗粒物（PM）排放

为了约束 Mapped Core Engine 模块输出，该模块不会外推查找表数据。
