---
type: simulink-block
title: 'Heat Exchanger'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'heatexchanger'
documentation_source_path: 'ref/heatexchanger.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Exchanger

## 端口

### 输入

### **C** — 入口质量流量、热流率、温度、质量分数双向连接器端口

包含热交换器的总线：

- `MassFlwRate` — 入口质量流量，m˙，单位为 kg/s
- `HeatFlwRate` — 入口热流率，qin，单位为 J/s
- `Temp` — 入口温度，Tflw,in，单位为 K
- `MassFrac` — 入口质量分数，无量纲。

  具体来说，是具有以下质量分数的总线：

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
  - `BrndGasMassFrac` — 已燃气

### **B** — 出口体积压力、温度、焓、质量分数双向连接器端口

包含热交换器的总线：

- `Prs` — 出口压力，pvol,out，单位为 Pa
- `Temp` — 出口温度，Tvol,out，单位为 K
- `Enth` — 出口比焓，hvol,out，单位为 J/kg
- `MassFrac` — 出口质量分数，无量纲。

  具体来说，是具有以下质量分数的总线：

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
  - `BrndGasMassFrac` — 已燃气

### **Effct** — 热交换器效能 `scalar`

热交换器效能，εinput。

#### 依赖关系

要创建此端口，请将 **效能模型** 设置为 `External input`。

### **CoolTemp** — 冷却介质温度 scalar

冷却介质温度，Tcool,input。

#### 依赖关系

要创建此端口，请将 **冷却介质温度输入** 设置为 `External input`。

### 输出

### **Info** — 热交换器数据总线

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `InletTemp` | | | 热交换器入口温度 | K |
| `OutletTemp` | | | 热交换器出口温度 | K |
| `HeatTrnsfrRate` | | | 热交换器热传递速率 | J/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrHeatFlwIn` | 端口 C 的热流率 | W |
| `PwrHeatFlwOut` | 端口 B 的热流率 | W |
| `PwrNotTrnsfrd` | `PwrHeatTrnsfr` | 到冷却介质的热传递速率 | W |
| `PwrStored` | | *未使用* | |

### **C** — 入口流动压力、温度、焓、质量分数双向连接器端口

包含热交换器的总线：

- `Prs` — 入口压力，pflw,in，单位为 Pa
- `Temp` — 入口温度，Tin，单位为 K
- `Enth` — 入口比焓，hin，单位为 J/kg
- `MassFrac` — 入口质量分数，无量纲。

  具体来说，是具有以下质量分数的总线：

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
  - `BrndGasMassFrac` — 已燃气

### **B** — 出口体积质量流量、热流率、温度、质量分数双向连接器端口

包含热交换器的总线：

- `MassFlwRate` — 出口质量流量，m˙，单位为 kg/s
- `HeatFlwRate` — 出口热流率，qout，单位为 J/s
- `Temp` — 出口温度，Tout，单位为 K
- `MassFrac` — 出口质量分数，无量纲。

  具体来说，是具有以下质量分数的总线：

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
  - `BrndGasMassFrac` — 已燃气

## 参数

#### 模块选项

### **效能模型** — 用于热效能的模型类型 `Constant`（默认） | `External input`

用于计算热交换器效能的模型类型。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `EffctModelPopup` |
| **值:** | `Constant`（默认） | `External input` |
| **数据类型:** | `character vector` |

#### 依赖关系

选择：

- `External input` 会创建 `Effct` 端口。
- `Constant` 会启用 **热交换器效能, ep\_cnst** 参数。

### **冷却介质温度输入** — 指定类型 `Constant`（默认） | `External input`

冷却介质温度输入。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `CoolTempInputPopup` |
| **值:** | `Constant`（默认） | `External input` |
| **数据类型:** | `character vector` |

#### 依赖关系

选择：

- `External input` 会创建 `CoolTemp` 端口。
- `Constant` 会启用 **冷却介质温度, T\_cool\_cnst** 参数。

### **图像类型** — 图标颜色 `Intercooler`（默认） | `EGR cooler hot to cold` | `EGR cooler cold to hot`

模块图标颜色：

- `Intercooler` 为蓝色，用于指示中冷器
- `EGR cooler hot to cold` 为红色到蓝色，用于指示 EGR 从热到冷
- `EGR cooler cold to hot` 为蓝色到红色，用于指示 EGR 从冷到热

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ImageTypePopup` |
| **值:** | `Cold`（默认） | `Hot` |
| **数据类型:** | `character vector` |

### **热交换器效能, ep\_cnst** — 效能 `0.7`（默认） | `scalar`

常量热交换器效能，εcnst。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ep_cnst` |
| **值:** | `0.7`（默认） | `scalar` |
| **数据类型:** | `double` |

#### 依赖关系

要启用此参数，请为 **效能模型** 参数选择 `Constant`。

### **冷却介质温度, T\_cool\_cnst** — 温度 `300`（默认） | `scalar`

常量冷却介质温度，Tcool,cnst，单位为 K。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `T_cool_cnst` |
| **值:** | `300`（默认） | `scalar` |
| **数据类型:** | `double` |

#### 依赖关系

要启用此参数，请为 **冷却介质温度输入** 参数选择 `Constant`。

### **定压比热, cp** — 比热 `1005`（默认） | `scalar`

定压比热，cp，单位为 J/(kg\*K)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `cp` |
| **值:** | `1005`（默认） | `scalar` |
| **数据类型:** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Fundamental Flow

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

中冷器或废气再循环 (EGR) 冷却器

Heat Exchanger 模块对热交换器建模，例如中冷器或废气再循环 (EGR) 冷却器。入口（端口 C）连接到发动机流动组件（流动限制、压气机、涡轮或发动机缸体）。出口（端口 B）连接到体积（控制体积或环境）。基于上游温度、热交换器效能和冷却介质温度，模块确定热传递速率和下游温度。

对于热交换器效能和冷却介质温度，可以指定常量值或外部输入。例如，如果指定热交换器效能为：

- 等于 1，则下游温度等于冷却介质温度。
- 等于 0，则没有热传递到冷却介质。下游温度等于上游温度。

模块假设无压降。要对压力损失建模，请使用 Flow Restriction 模块。

### 方程

Heat Exchanger 模块实现使用这些变量的方程。

|  |  |
| --- | --- |
| Tupstr | 上游温度 |
| Tdnstr | 下游温度 |
| Tcool | 冷却介质温度 |
| Tcool,cnst | 常量冷却介质温度 |
| Tcool,input | 外部输入冷却介质温度 |
| ε | 热交换器效能 |
| εcnst | 常量热交换器效能 |
| εinput | 输入热交换器效能 |
| cp | 定压比热 |
| qht | 热交换器热传递速率 |
| pflw,in | 入口压力 |
| pvol,out | 出口压力 |
| Tvol,out | 出口温度 |
| hvol,out | 出口比焓 |
| qin | 入口热流率 |
| qout | 出口热流率 |
| m˙ | 热交换器质量流量 |
| Tflw,in | 入口温度 |
| Tin | 热交换器入口温度 |
| Tout | 热交换器出口温度 |
| hin | 入口比焓 |

**热交换器效能**

热交换器效能衡量从进入的热流体到冷却介质的热传递效能：

ε=Tupstr−TdnstrTupstr−Tcool

在理想热交换器中，下游温度等于冷却温度。效能等于 1。

Tdnstr=Tcoolε=1

Heat Exchanger 模块使用效能来确定下游温度和热传递速率。

Tdnstr=Tupstr−ε(Tupstr−Tcool)qht=m˙cp(Tupstr−Tdnstr)

**流体流动**

由于模块假设无压降，Pflw,in=Pvol,out。

流动组件与热交换器入口的连接决定质量流的方向。基于质量流率方向，应用以下温度和热流方程。

| 流体流动 | 质量流率 | 温度和热流 |
| --- | --- | --- |
| 正向 — 从发动机流动组件到出口体积 | m˙≥0 | Tupstr=Tflw,inTin=TupstrTout=Tdnstrqout=m˙cpTdnstr |
| 反向 — 从出口体积到发动机流动组件 | m˙<0 | Tupstr=Tvol,outTin=TdnstrTout=Tvol,outhin=cpTdnstrqout=m˙hvol,out |

模块使用内部信号 `FlwDir` 跟踪流动方向。

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrHeatFlwIn` | 端口 C 的热流率 | *qin* |
| `PwrHeatFlwOut` | 端口 B 的热流率 | -*qout* |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrHeatTrnsfr` | 到冷却介质的热传递速率 | -*qht* |
| `PwrStored` — 储存能量的变化率  - 正信号表示增加 - 负信号表示减少 | | *未使用* | | |
