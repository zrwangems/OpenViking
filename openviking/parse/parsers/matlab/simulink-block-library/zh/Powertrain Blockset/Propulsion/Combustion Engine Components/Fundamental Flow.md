---
type: simulink-block
title: 'Flow Restriction'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components'
documentation_page: 'flowrestriction'
documentation_source_path: 'ref/flowrestriction.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Restriction

## 端口

### 输入

### **A** — 入口孔口压力、温度、焓、质量分数双向连接端口

包含孔口的总线：

- `Prs` — 压力，单位为 Pa
- `Temp` — 温度，单位为 K
- `Enth` — 比焓，单位为 J/kg
- `MassFrac` — 入口质量分数，无量纲。

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
  - `BrndGasMassFrac` — 已燃气体

### **B** — 出口孔口压力、温度、焓、质量分数双向连接端口

包含孔口的总线：

- `Prs` — 压力，单位为 Pa
- `Temp` — 温度，单位为 K
- `Enth` — 比焓，单位为 J/kg
- `MassFrac` — 出口质量分数，无量纲。

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
  - `BrndGasMassFrac` — 已燃气体

### **Area** — 孔口面积 `scalar`

孔口面积的外部输入，Aorf\_ext，单位为 m^2。

#### 依赖项

要创建此端口，请为 **孔口面积模型** 参数选择 `External input`。

### **ThrPct** — 节气门体开启百分比 `scalar`

节气门体开启的百分比，Pctthr。

#### 依赖项

要创建此端口，请为 **孔口面积模型** 参数选择 `Throttle body geometry`。

### 输出

### **A** — 入口质量流率、热流率、温度双向连接端口

包含：

- `MassFlw` — 通过入口的质量流率，单位为 kg/s
- `HeatFlw` — 入口热流率，单位为 J/s
- `Temp` — 入口温度，单位为 K
- `MassFrac` — 入口质量分数，无量纲。

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
  - `BrndGasMassFrac` — 已燃气体

### **B** — 出口质量流率、热流率、温度双向连接端口

包含：

- `MassFlw` — 出口质量流率，单位为 kg/s
- `HeatFlw` — 出口热流率，单位为 J/s
- `Temp` — 出口温度，单位为 K
- `MassFrac` — 出口质量分数，无量纲。

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
  - `BrndGasMassFrac` — 已燃气体

### **Info** — 总线信号总线

包含这些模块计算的总线信号。

| 信号 | | | | 描述 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `Flw` | `PrsAdj` | | `DwnstrmPrs` | 下游压力 | Pa |
| `UpstrmPrs` | 上游压力 | Pa |
| `PrsRatio` | 压力比 | NA |
| `DwnstrmTemp` | 下游温度 | K |
| `UpstrmTemp` | 上游温度 | K |
| `OrfMassFlw` | | | 通过孔口的质量流率 | kg/s |
| `Species` | | `O2MassFlw` | 氧气质量流率 | kg/s |
| `N2MassFlw` | 氮气质量流率 | kg/s |
| `UnbrndFuelMassFlw` | 未燃气体质量流率 | kg/s |
| `CO2MassFlw` | 二氧化碳质量流率 | kg/s |
| `H2OMassFlw` | 水质量流率 | kg/s |
| `COMassFlw` | 一氧化碳质量流率 | kg/s |
| `NOMassFlw` | 一氧化氮质量流率 | kg/s |
| `NO2MassFlw` | 二氧化氮质量流率 | kg/s |
| `NOxMassFlw` | 一氧化氮和二氧化氮质量流率 | kg/s |
| `PmMassFlw` | 颗粒物质量流率 | kg/s |
| `AirMassFlw` | 空气质量流率 | kg/s |
| `BrnedGasMassFlw` | 已燃气体质量流率 | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrHeatFlwIn` | 端口 A 的热流率 | W |
| `PwrHeatFlwOut` | 端口 B 的热流率 | W |
| `PwrNotTrnsfrd` | | *未使用* | |
| `PwrStored` | | *未使用* | |
| `Area` | `FlwArea` | | | 横截流通面积 | m^2 |
| `EffctArea` | | | 有效孔口横截面积 | m^2 |
| `ThrAng` | | | 节气门面积（如果适用） | deg |

## 参数

#### 模块选项

### **孔口面积模型** — 选择模型 `Constant`（默认） | `External input` | `Throttle body geometry`

孔口面积模型。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AreaPopup` |
| **值：** | `Constant`（默认） | `External input` | `Throttle body geometry` |
| **数据类型：** | `character vector` |

#### 依赖项

孔口面积模型会启用 **Area Parameters** 选项卡上的参数。

### **图像类型** — 图标颜色 `Cold`（默认） | `Hot`

模块图标颜色：

- `Cold` 表示蓝色。
- `Hot` 表示红色。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ImageTypePopup` |
| **值：** | `Cold`（默认） | `Hot` |
| **数据类型：** | `character vector` |

#### 常规

### **比热比, gamma** — 比值 `1.3998`（默认） | `scalar`

比热比，*γ*。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `gamma` |
| **值：** | `1.3998`（默认） | `scalar` |
| **数据类型：** | `double` |

### **理想气体常数, R** — 常数 `287.05`（默认） | `scalar`

理想气体常数，R，单位为 J/(kg·K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `R` |
| **值：** | `287.05`（默认） | `scalar` |
| **数据类型：** | `double` |

### **压力比线性化限值, Plim** — 限值 `0.95`（默认） | `scalar`

压力比限值，用于避免当压力比接近 1 时出现奇异，Plim。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Plim` |
| **值：** | `0.95`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 面积

### **恒定面积值, Aorf\_cnst** — 面积 `.1`（默认） | `scalar`

恒定面积值，Aorf\_cnst，单位为 m^2。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Aorf_cnst` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **孔口面积模型** 参数选择 `Constant`。

### **流量系数, Cd\_cnst** — 系数 `1`（默认） | `scalar`

恒定面积的流量系数，Cdcnst。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cd_cnst` |
| **值：** | `1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **孔口面积模型** 参数选择 `Constant`。

### **流量系数, Cd\_ext** — 系数 `1`（默认） | `scalar`

外部面积输入的流量系数，Cdext。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Cd_ext` |
| **值：** | `1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **孔口面积模型** 参数选择 `External input`。

### **节气门直径, Dthr** — 直径 `50`（默认） | `scalar`

开启时节气门体直径，Dthr，单位为 mm。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Dthr` |
| **值：** | `50`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **孔口面积模型** 参数选择 `Throttle body geometry`。

### **流量系数表, ThrCd** — 系数 `[0.001; 0.735]`（默认） | `vector`

流量系数表，*Cd\_thr*。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ThrCd` |
| **值：** | `[0.001; 0.735]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **孔口面积模型** 参数选择 `Throttle body geometry`。

### **角度断点, ThrAngBpts** — 角度 `[0; 90]`（默认） | `vector`

角度断点，Thrang\_bpts，单位为 deg。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ThrAngBpts` |
| **值：** | `[0; 90]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **孔口面积模型** 参数选择 `Throttle body geometry`。

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Fundamental Flow

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

通过孔口的等熵理想气体流动

Flow Restriction 模块对通过孔口的等熵理想气体流动进行建模。该模块使用质量和能量守恒来确定质量流率。流速受阻塞流限制。

您可以指定以下孔口面积模型：

- Constant
- External input
- Throttle body geometry

### 方程

Flow Restriction 模块实现以下方程。

| 计算 | 方程 |
| --- | --- |
| 标准孔口 | m˙orf=Γ⋅Ψ(Pratio)  Pratio=PdownstrPupstr  Γ=Aeff⋅PupstrR⋅Tupstr  Pcr=(2γ+1)γγ−1  Ψ={γ(2γ+1)γ+1γ−1Pratio<Pcr2γγ−1(Pratio2γ−Pratioγ+1γ)Pcr≤Pratio≤PlimPratio−1Plim−12γγ−1(Plim2γ−Plimγ+1γ)Plim<Pratio |
| 组分质量流率 | m˙i=m˙orfyupstr,i |
| 恒定孔口面积 | Aeff=Aorf\_cnst⋅Cdcnst |
| 外部输入孔口面积 | Aeff=Aorf\_ext⋅Cdext |
| 节气门体几何 | θthr=Pctthr⋅90100  Aeff\_thr=π4Dthr2Cd\_thr(θthr) |
| 热流率 | qorf=m˙orfhupstr |

方程使用以下变量。

|  |  |
| --- | --- |
| Aeff, Aeff\_thr | 有效孔口横截面积 |
| Aorf\_cnst, Aorf\_ext | 孔口面积 |
| Cdcnst, Cdext | 流量系数 |
| R | 理想气体常数 |
| Pcr | 发生阻塞流的临界压力 |
| *γ* | 比热比 |
| Γ | 基于压力比的流动函数 |
| Pratio | 压力比 |
| Pupstr | 上游孔口压力 |
| Pdownstr | 下游孔口压力 |
| Plim | 压力比限值，用于避免当压力比接近 1 时出现奇异 |
| *yupstr,i* | 上游组分质量分数，i = O2、N2、未燃燃料、CO2、H2O、CO、NO、NO2、PM、空气和已燃气体 |
| m˙i | 质量流率，i = O2、N2、未燃燃料、CO2、H2O、CO、NO、NO2、PM、空气和已燃气体 |
| θthr | 节气门角度 |
| Pctthr | 节气门体开启百分比 |
| *Cd\_thr* | 节气门流量系数 |
| Dthr | 开启时节气门体直径 |
| m˙orf | 孔口质量流量 |
| *hupstr* | 上游比焓 |
| *qorf* | 热流率 |

该模块使用内部信号 `FlwDir` 跟踪流动方向。

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrHeatFlwIn` | 端口 A 的热流率 | *qorf* |
| `PwrHeatFlwOut` | 端口 B 的热流率 | -*qorf* |
| `PwrNotTrnsfrd` — 穿过模块边界但不传递的功率  - 正信号表示输入 - 负信号表示损失 | *未使用* | | |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | |
