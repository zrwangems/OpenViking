---
type: simulink-block
title: 'Flow Boundary'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'flowboundary'
documentation_source_path: 'ref/flowboundary.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Boundary

## 端口

### 输入

### **Prs** — 压力 `scalar`

外部输入压力，*P*，单位为 Pa。

#### 依赖关系

要创建此端口，请为 **压力和温度源** 参数选择 `External input`。

### **Temp** — 温度 `scalar`

外部输入温度，*T*，单位为 K。

#### 依赖关系

要创建此端口，请为 **压力和温度源** 参数选择 `External input`。
### 输出

### **Info** — 总线信号 bus

包含以下模块计算的总线信号。

| 信号 | | | 说明 | 单位 |
| --- | --- | --- | --- | --- |
| `BndryPrs` | | | 边界压力 | Pa |
| `BndryTemp` | | | 边界温度 | K |
| `BndryEnth` | | | 边界比焓 | J/kg |
| `PwrInfo` | `PwrTrnsfrd` | `PwrBndryFlw` | 至流动限制的热流率 | W |
| `PwrNotTrnsfrd` | `PwrEnv` | 至环境的热流率 | W |
| `PwrStored` | | *未使用* | |

### **C** — 边界压力、温度、焓、质量分数双向连接器端口

包含流动边界的总线：

- `Prs` — 压力，*P*，
  单位为 Pa
- `Temp` — 温度，*T*，
  单位为 K
- `Enth` — 比焓，*h*，
  单位为 J/kg
- `MassFrac` — 质量分数，
  无量纲。

  具体而言，是包含以下质量分数的总线：

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

### **压力和温度源** — 选择源 `External input` (默认) | `Constant`

压力和温度源。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PrsTempSrcPopup` |
| **值：** | `External input` (默认) | `Constant` |
| **数据类型：** | `character vector` |

#### 依赖关系

下表汇总了参数和端口依赖关系。

| 值 | 启用的参数 | 创建的端口 |
| --- | --- | --- |
| `Constant` | **压力，Pcnst**  **温度，Tcnst** | 无 |
| `External input` | 无 | `Prs`  `Temp` |

### **图像类型** — 图标颜色 `Cold` (默认) | `Hot`

选择模块图标的颜色：

- `Cold` 表示蓝色
- `Hot` 表示红色

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ImageTypePopup` |
| **值：** | `Cold` (默认) | `Hot` |
| **数据类型：** | `character vector` |

### **压力，Pcnst** — 常量 `101325` (默认) | `scalar`

恒定压力，*P*，单位为 Pa。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Pcnst` |
| **值：** | `101325` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **压力和温度源** 参数选择 `Constant`。

### **温度，Tcnst** — 常量 `298.15` (默认) | `scalar`

恒定温度，*T*，单位为 K。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tcnst` |
| **值：** | `298.15` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **压力和温度源** 参数选择 `Constant`。

### **定压比热容，cp** — 常量 `1005` (默认) | `scalar`

定压比热容，单位为 J/(kg·K)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `cp` |
| **值：** | `1005` (默认) | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Fundamental Flow

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

用于环境温度和压力的流动边界

Flow Boundary 模块实现流动边界，通常表示环境温度和压力。发动机模型需要在进气口入口和排气口出口处设置流动边界。在动态发动机模型中，改变流动的组件（例如，流动限制、涡轮和压缩机）连接到控制体和流动边界。

您可以指定以下模块配置：

- 恒定压力和温度
- 外部输入压力和温度

Flow Boundary 模块输出压力、温度和比焓：

h=cpT

该模块将质量分数建模为干空气，从而得到以下质量分数：

- *yN2* = 0.767
- *yO2* = .233

方程使用以下变量。

|  |  |
| --- | --- |
| *T* | 温度 |
| *h* | 比焓 |
| *cp* | 定压比热容 |
| *yN2* | 氮气质量分数 |
| *yO2* | 氧气质量分数 |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 说明 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 在模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrBndrFlw` | 至流动限制的热流率 | *qorf* |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrEnv` | 至环境的热流率 | -*qorf* |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | *未使用* | | | |
