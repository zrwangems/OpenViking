---
type: simulink-block
title: 'Control Volume System'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'controlvolumesystem'
documentation_source_path: 'ref/controlvolumesystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Control Volume System

## 端口

### 输入

### **C** — 入口质量流量、热流量、质量分数双向连接端口

总线包含：

- `MassFlw` — 通过入口的质量流量，单位为 kg/s
- `HeatFlw` — 入口热流量，单位为 J/s
- `MassFrac` — 入口质量分数，
  无量纲。

  具体而言，包含这些质量分数的总线：

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

#### 依赖关系

要创建输入端口，请指定 **入口端口数** 参数。

### **HeatTrnsfrRate** — 传热 `scalar`

外部传入控制体的传热输入，*qhe*，单位为 Kg/s。

#### 依赖关系

要创建此端口，请为 **传热模型** 参数选择 `External input`。

### **ExtnlFlwVel** — 外部流速标量

外部流速，*Flwspd*，单位为 m/s。

#### 依赖关系

要创建此端口，请为 **传热模型** 参数选择 `External wall convection`。

### **ExtnlTemp** — 环境温度，K `scalar`

#### 依赖关系

要创建此端口，请为 **传热模型** 参数选择 `External wall convection`。
### 输出

### **Info** — 总线信号 bus

总线信号包含以下模块计算。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `Vol` | `Prs` | | 容积压力 | Pa |
| `Temp` | | 容积温度 | K |
| `Enth` | | 容积比焓 | J/kg |
| `Species` | `O2MassFrac` | 氧气质量分数 | NA |
| `N2MassFrac` | 氮气质量分数 | NA |
| `UnbrndFuelMassFrac` | 未燃气体质量分数 | NA |
| `CO2MassFrac` | 二氧化碳质量分数 | NA |
| `H2OMassFrac` | 水质量分数 | NA |
| `COMassFrac` | 一氧化碳质量分数 | NA |
| `NOMassFrac` | 一氧化氮质量分数 | NA |
| `NO2MassFrac` | 二氧化氮质量分数 | NA |
| `NOxMassFrac` | 一氧化氮和二氧化氮质量分数 | NA |
| `PmMassFrac` | 颗粒物质量分数 | NA |
| `AirMassFrac` | 空气质量分数 | NA |
| `BrndGasMassFrac` | 已燃气体质量分数 | NA |
| `HeatTrnsfr` | `HeatTrnsfrRate` | | 壁传热速率 | J/s |
| `MassFlw` | | 平均内部质量流量 | kg/s |
| `IntrnTemp` | | 腔室内气体温度 | K |
| `PwrInfo` | `PwrTrnsfrd` | `PwrHeatFlwi` | 端口 *`i`* 热流量 | W |
| `PwrNotTrnsfrd` | `PwrHeatTrnsfr` | 从壁到控制体的传热速率 | W |
| `PwrStored` | `PwrHeatStored` | 控制体中存储的热量速率 | W |

### **C** — 出口压力、温度、焓、质量分数双向连接端口

总线包含出口控制体：

- `Prs` — 腔室压力，
  单位为 Pa
- `Temp` — 气体温度，
  单位为 K
- `Enth` — 比焓，
  单位为 J/kg
- `MassFrac` —
  质量分数，无量纲。

  具体而言，包含这些质量分数的总线：

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

#### 依赖关系

要创建输出端口，请指定 **出口端口数** 参数。

## 参数

#### 模块选项

### **入口端口数** — 端口数 `1` (default) | `0` | `2` | `3` | `4`

入口端口数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumInletPorts` |
| **值：** | `1` (default) | `0` | `2` | `3` | `4` |
| **数据类型：** | `double` |

#### 依赖关系

要创建入口端口，请指定数量。

### **出口端口数** — 端口数 `1` (default) | `0` | `2` | `3` | `4`

出口端口数。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumOutletPorts` |
| **值：** | `1` (default) | `0` | `2` | `3` | `4` |
| **数据类型：** | `double` |

#### 依赖关系

要创建出口端口，请指定数量。

### **传热模型** — 选择模型 `Constant` (default) | `External input` | `External wall convection`

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `HeatTransferModelPopup` |
| **值：** | `Constant` (default) | `External input` | `External wall convection` |
| **数据类型：** | `character vector` |

#### 依赖关系

选择 `Constant` 或 `External wall convection` 将启用 **传热** 参数。

### **图像类型** — 图标颜色 `Cold` (default) | `Hot`

为模块图标选择颜色：

- `Cold` 表示蓝色
- `Hot` 表示红色

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ImageTypePopup` |
| **值：** | `Cold` (default) | `Hot` |
| **数据类型：** | `character vector` |

#### 常规

### **腔室容积, Vch** — 容积 `0.0029` (default) | `scalar`

腔室容积，*Vch*，单位为
m^3。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vch` |
| **值：** | `0.0029` (default) | `scalar` |
| **数据类型：** | `double` |

### **初始腔室压力, Pinit** — 压力 `101325` (default) | `scalar`

初始腔室压力，*Pvol*，单位为 Pa。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pinit` |
| **值：** | `101325` (default) | `scalar` |
| **数据类型：** | `double` |

### **初始腔室温度, Tinit** — 温度 `298` (default) | `scalar`

初始腔室温度，*Tvol*，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tinit` |
| **值：** | `298` (default) | `scalar` |
| **数据类型：** | `double` |

### **理想气体常数, R** — 理想气体常数 `287` (default) | `scalar`

理想气体常数，*R*，单位为 J/(kg\*K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `R` |
| **值：** | `287` (default) | `scalar` |
| **数据类型：** | `double` |

### **比热容, cp** — 比热 `1005` (default) | `scalar`

比热容，*cp*，单位为 J/(kg·K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `cp` |
| **值：** | `1005` (default) | `scalar` |
| **数据类型：** | `double` |

#### 传热

### **传热速率, q\_he** — 速率 `0` (default) | `scalar`

恒定传热速率，*qhe*，单位为 J/s。

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `Constant`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `q_he` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

### **外部对流传热系数, ext\_tbl** — 歧管外部空气 `[40 160 740 2000]` (default) | `vector`

外部对流传热系数，*hext*，单位为 W/(m^2K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ext_tbl` |
| **值：** | `[40 160 740 2000]` (default) | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **外部速度断点, ext\_bpts** — 歧管外部空气 `linspace(0,180,4)` (default) | `vector`

外部速度断点，*xext*，单位为 m/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ext_bpts` |
| **值：** | `linspace(0,180,4)` (default) | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **外部对流面积, Aext\_conv** — 歧管外部空气 `0.125` (default) | `scalar`

外部对流面积，*Aext\_conv*，单位为 m^2。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Aext_conv` |
| **值：** | `0.125` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **热质量, m\_wall** — 歧管壁通用 `7` (default) | `scalar`

热质量，*mwall*，单位为 kg。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `m_wall` |
| **值：** | `7` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **壁热容, cp\_wall** — 歧管壁通用 `900` (default) | `scalar`

壁热容，*cp\_wall*，单位为 J/(kg·K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `cp_wall` |
| **值：** | `900` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **初始质量温度, Tmass** — 歧管壁通用 `293.15` (default) | `scalar`

初始质量温度，*Tmass*，单位为 K。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tmass` |
| **值：** | `293.15` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **外部壁厚, Dext\_cond** — 歧管壁外部 `0.004` (default) | `scalar`

外部壁厚，*Dext\_cond*，单位为 m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Em` |
| **值：** | `1`-by-`P` matrix |
| **数据类型：** | `double` |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Dext_cond` |
| **值：** | `0.004` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **外部导热面积, Aext\_cond** — 歧管壁外部 `0.003` (default) | `scalar`

外部导热面积，*Aext\_cond*，单位为 m^2。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Aext_cond` |
| **值：** | `0.003` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **外部壁导热系数, kext** — 歧管壁外部 `25` (default) | `scalar`

外部壁导热系数，*kext*，单位为 W/(m·K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `kext` |
| **值：** | `25` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **内部壁厚, Dint\_cond** — 歧管壁内部 `0.004` (default) | `scalar`

内部壁厚，*Dint\_cond*，单位为 m。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Dint_cond` |
| **值：** | `0.004` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **内部导热面积, Aint\_cond** — 歧管壁内部 `0.003` (default) | `scalar`

内部导热面积，*Aint\_cond*，单位为 m^2。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Aint_cond` |
| **值：** | `0.003` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **内部壁导热系数, kint** — 歧管壁内部 `25` (default) | `scalar`

内部壁导热系数，*kint*，单位为 W/(m·K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `kint` |
| **值：** | `25` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **内部对流传热系数, int\_tbl** — 歧管内部空气 `[40 160 740 2000]` (default) | `vector`

内部对流传热系数，*hint*，单位为 W/(m^2K)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `int_tbl` |
| **值：** | `[40 160 740 2000]` (default) | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **内部质量流量断点, int\_bpts** — 歧管内部空气 `linspace(0.0020,0.1100,4)` (default) | `vector`

内部速度断点，*xint*，单位为 kg/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `int_bpts` |
| **值：** | `linspace(0.0020,0.1100,4)` (default) | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

### **内部流动对流面积, Aint\_conv** — 歧管内部空气 `0.125` (default) | `scalar`

内部对流面积，*Aint\_conv*，单位为 m^2。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Aint_conv` |
| **值：** | `0.125` (default) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **传热模型** 参数选择 `External wall convection`。

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Fundamental Flow

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2017a 中引入**

## 描述

带传热的定容开放热力学系统

Control Volume System 模块对带传热的定容开放热力学系统进行建模。该模块使用质量守恒和能量守恒，并假设理想气体，来确定压力和温度。该模块实现了一个汽车专用的 Constant Volume Pneumatic Chamber 模块，其中包含与乘用车发动机舱内相关的热效应。您可以指定传热模型：

- Constant
- External input
- External wall convection

您可以使用 Control Volume System 模块来表示包含容积的发动机部件，包括管道和歧管。

### 热力学

Control Volume System 模块实现一个包含理想气体的定容腔室。为了确定温度和压力的变化率，该模块使用连续性方程和热力学第一定律。

dTvoldt=RTvolcvVchPvol(∑(qi−Tvolcvm˙i)−Qwall)dPvoldt=PvolTvoldTvoldt+RTvolVch∑m˙i

该模块使用此方程计算体积比焓。

hvol=cpTvol

这些方程使用以下变量。

|  |  |
| --- | --- |
| m˙i | 端口处的质量流量 |
| *qi* | 端口处的热流量 |
| *Vch* | 腔室容积 |
| *Pvol* | 腔室中的绝对压力 |
| *R* | 理想气体常数 |
| *cv* | 定容比热 |
| *Tvol* | 气体绝对温度 |
| *Qwall* | 壁传热速率 |
| *hvol* | 体积比焓 |
| *cp* | 比热容 |

### 质量分数

Control Volume Source 模块是流量网络的一部分。网络中的模块确定该模块在仿真期间将跟踪的质量分数。该模块可以跟踪以下质量分数：

- `O2` — 氧气
- `N2` — 氮气
- `UnburnedFuel` — 未燃燃料
- `CO2` — 二氧化碳
- `H2O` — 水
- `CO` — 一氧化碳
- `NO` — 一氧化氮
- `NO2` — 二氧化氮
- `PM` — 颗粒物
- `Air` — 空气
- `BurnedGas` — 已燃气体

使用每种气体组分的质量守恒，此方程确定变化率：

dyvol,jdt=RTvolPvolVch(∑m˙iyi,j+yvol,j∑m˙i)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Vch* | 腔室容积 |
| *Pvol* | 腔室中的绝对压力 |
| *R* | 理想气体常数 |
| *Tvol* | 气体绝对温度 |
| *yi,j* | 第 i 个端口的质量分数，其中 j = O2、N2、未燃燃料、CO2、H2O、CO、NO、NO2、PM、空气和已燃气体 |
| *yvol,j* | 控制体质量分数，其中 j = O2、N2、未燃燃料、CO2、H2O、CO、NO、NO2、PM、空气和已燃气体 |
| m˙i | 质量流量，其中 i = O2、N2、未燃燃料、CO2、H2O、CO、NO、NO2、PM、空气和已燃气体 |

### 外部壁对流传热模型

为了计算传热，您可以将 Control Volume Source 模块配置为计算穿过控制体壁的传热。

该模块实现以下方程来计算从内部控制体气体到内部壁深 *Dint\_cond* 的传热 *Q1*。

Q1=Q1,conv=Q1,cond

Q1,conv=hint(xint)•Aint\_conv•(Tint\_gas−Tw\_int)

Q1,cond=kint•Aint\_condDint\_cond•(Tw\_int−Tmass)

该模块实现以下方程来计算从外部壁深 *Dext\_cond* 到外部气体的传热 *Q2*。

Q2=Q2,conv=hext(xext)•Aext\_conv•(Tw\_ext−Text\_gas)

Q2,cond=kext•Aext\_condDext\_cond•(Tmass−Tw\_ext)

此方程表示存储在热质量中的热量。

dTmassdt=Q1−Q2cpwallmwall

该模块使用查找表确定内部对流传热系数，该查找表是平均质量流量的函数。

m˙int\_gas=12∑|m˙i|

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Q1* | 从内部气体到指定壁深的热流 |
| *Q1,conv* | 从内部气体到内部壁的对流热流 |
| *Q1,cond* | 导热传热速率 |
| *Q2* | 传热速率 |
| *Q2,conv* | 对流传热 |
| *Q2,cond* | 从壁的外部中间部分到外部壁的导热热流 |
| *Qmass* | 存储在热质量中的热量 |
| *hint* | 内部对流传热系数 |
| *xint* | 内部质量流量断点 |
| *Aint\_conv* | 内部流动对流面积 |
| *Tint\_gas* | 腔室内气体的温度 |
| *Tw\_int* | 腔室内壁的温度 |
| *kint* | 内部壁导热系数 |
| *Aint\_cond* | 内部导热面积 |
| *Dint\_cond* | 内部壁厚 |
| *hext* | 外部对流传热系数 |
| *xext* | 外部速度断点 |
| *Aext\_conv* | 外部对流面积 |
| *Text\_gas* | 外部气体温度 |
| *Tw\_ext* | 腔室外壁的温度 |
| *kext* | 外部壁导热系数 |
| *Aext\_cond* | 外部导热面积 |
| *Dext\_cond* | 外部壁厚 |
| *Tmass* | 热质量的温度 |
| *cp\_wall* | 壁热容 |
| *mwall* | 热质量 |
| *Flwspd* | 外部流速 |
| m˙int\_gas | 平均内部质量流量 |

### 功率核算

对于功率核算，该模块根据入口和出口端口的数量实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrHeatFlwi` | 端口 *`i`* 热流量 | *qi* |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrHeatTrnsfr` | 从壁到控制体的传热速率 | -*Qwall* |
| `PwrStored` — 储能变化率  - 正信号表示增加 - 负信号表示减少 | `PwrHeatStored` | 控制体中存储的热量速率 | (∑​(qi)−Qwall) |

例如，如果您将模块配置为 3 个输入端口和 2 个出口端口，则该模块实现以下方程

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrHeatFlw1` | 入口端口 1 热流量 | *q1* |
| `PwrHeatFlw2` | 入口端口 2 热流量 | *q2* |
| `PwrHeatFlw3` | 入口端口 3 热流量 | *q3* |
| `PwrHeatFlw4` | 出口端口 4 热流量 | *q4* |
| `PwrHeatFlw5` | 出口端口 5 热流量 | *q5* |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrHeatTrnsfr` | 从壁到控制体的传热速率 | -*Qwall* |
| `PwrStored` — 储能变化率  - 正信号表示增加 - 负信号表示减少 | `PwrHeatStored` | 控制体中存储的热量速率 | (∑​(qi)−Qwall) |
