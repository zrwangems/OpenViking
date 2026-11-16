---
type: simulink-block
title: 'Power Accounting Bus Creator'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage'
documentation_page: 'poweraccountingbuscreator'
documentation_source_path: 'ref/poweraccountingbuscreator.html'
language: zh-CN
chinese_source: worker-translation
---

# Power Accounting Bus Creator

## 端口

### 输入

### **PwrTrnsfrd** — 模块之间传输的功率 `bus`

`PwrTrnsfrd` — 模块之间传输的功率

- 正信号表示流入模块
- 负信号表示流出模块

#### 依赖项

要创建此输入端口，请选择 **传输功率**。

### **PwrNotTrnsfrd** — 穿过模块边界但未传输的功率 `bus`

`PwrNotTrnsfrd` — 穿过模块边界但未传输的功率

- 正信号表示输入
- 负信号表示损耗

#### 依赖项

要创建此输入端口，请选择 **未传输功率**。

### **PwrStored** — 存储能量变化率 `bus`

`PwrStored` — 存储能量变化率

- 正信号表示增加
- 负信号表示减少

#### 依赖项

要创建此输入端口，请选择 **存储功率**。

### 输出

### **PwrInfo** — 功率信息总线 `bus`

功率信息总线

## 参数

#### 模块选项

### **关联模块** — 关联模块 `Parent`（默认） | `Parent reference block`

当您将 Power Accounting Bus Creator 添加到您的被控对象模块时，您将信号关联到父模块。有两种关联方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Parent` | Power Accounting Bus Creator 将功率总线信号与父模块关联。 | 在传统车辆参考应用中，导航到 `Passenger Car > Engine > SiMappedEngine > Accessory Load Model` 被控对象子系统。打开 Power Accounting Bus Creator。**关联模块** 参数设置为 `Parent`，因此 Power Accounting Bus Creator 将功率信号与 `Accessory Load Model` 被控对象子系统关联。Power Accounting Buss Creator 模块掩码，其中 **关联模块** 参数设置为 parent。 |
| `Parent reference block` | Power Accounting Bus Creator 将功率总线信号与参考模块关联。使用 **库模块名称** 参数指定该模块。 | 在 Ideal Fixed Gear Transmission 模块中，导航到 `Bus Creation` 子系统。打开 Power Accounting Bus Creator。Power Accounting Bus Creator 模块使用这些参数设置将功率信号关联到 Ideal Fixed Gear Transmission 模块。 - **关联模块** 参数设置为 `Parent reference block`。 - **库模块名称** 参数设置为 `'autolibsharedtransfixedgear/Ideal Fixed Gear Transmission'`。 Power Accounting Buss Creator 模块掩码，其中 **关联模块** 参数设置为 parent reference block。 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParameterGroupVar` |
| **值：** | `Parent`（默认） | `Parent reference block` |
| **数据类型：** | `character vector` |

### **库模块名称** — 模块名称 `Block name`

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `RefBlckName` |
| **值：** | `Block name` |
| **数据类型：** | `character vector` |

#### 依赖项

要创建此参数，请将 **关联模块** 设置为 `Parent reference block`。

#### 功率输入类型

### **传输功率** — 模块之间传输的功率 `on`（默认） | `off`

模块之间传输的功率。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PwrTrnsfrdCheckBox` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `character vector` |

#### 依赖项

要创建此参数，请将 **关联模块** 设置为 `Parent reference block`。

选择此参数将创建：

- `PwrTrnsfrd` 输入端口
- **已传输** 参数

### **未传输功率** — 穿过模块边界的功率 `on`（默认） | `off`

穿过模块边界但未传输的功率。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PwrNotTrnsfrdCheckBox` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `character vector` |

#### 依赖项

选择此参数将创建：

- `PwrNotTrnsfrd` 输入端口
- **未传输** 参数

### **存储功率** — 存储能量变化率 `on`（默认） | `off`

存储能量变化率。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PwrStoredCheckBox` |
| **值：** | `on`（默认） | `off` |
| **数据类型：** | `character vector` |

#### 依赖项

选择此参数将创建：

- `PwrStored` 输入端口
- **存储** 参数

#### 已传输

### **信号名称** — 信号名称 `char`

信号名称。

例如，下表总结了所列模块的 Power Accounting Bus Creator 参数 **已传输** 参数值。

| 模块 | Power Accounting Bus Creator 参数值 | | |
| --- | --- | --- | --- |
| **信号名称** | **关联端口** | **描述** |
| Ideal Fixed Gear Transmission | `PwrTrnsfrd.PwrDiffrntl` | `{'DiffTrq','DiffSpd'}` | `Differential` |
| `PwrTrnsfrd.PwrEng` | `{'EngTrq','EngSpd'}` | `Engine` |
| Gearbox | `PwrTrnsfrd.PwrBase` | `{{'BTrq','BSpd'}'B'}` | `Base input` |
| `PwrTrnsfrd.PwrFlwr` | `{{'FTrq','FSpd'}'F'}` | `Follower output` |
| Boost Drive Shaft | `PwrTrnsfrd.PwrCmpsr` | `'Cmpsr'` | `Compressor` |
| `PwrTrnsfrd.PwrExt` | `'ExtTrq'` | `External` |
| `PwrTrnsfrd.Turb` | `'Turb'` | `Turbine` |

### **关联端口** — 传输功率的端口名称 `{'PortA','PortB','PortC'}`

传输功率的端口名称。

例如，下表总结了所列模块的 Power Accounting Bus Creator 参数 **已传输** 参数值。

| 模块 | Power Accounting Bus Creator 参数值 | | |
| --- | --- | --- | --- |
| **信号名称** | **关联端口** | **描述** |
| Ideal Fixed Gear Transmission | `PwrTrnsfrd.PwrDiffrntl` | `{'DiffTrq','DiffSpd'}` | `Differential` |
| `PwrTrnsfrd.PwrEng` | `{'EngTrq','EngSpd'}` | `Engine` |
| Gearbox | `PwrTrnsfrd.PwrBase` | `{{'BTrq','BSpd'}'B'}` | `Base input` |
| `PwrTrnsfrd.PwrFlwr` | `{{'FTrq','FSpd'}'F'}` | `Follower output` |
| Boost Drive Shaft | `PwrTrnsfrd.PwrCmpsr` | `'Cmpsr'` | `Compressor` |
| `PwrTrnsfrd.PwrExt` | `'ExtTrq'` | `External` |
| `PwrTrnsfrd.Turb` | `'Turb'` | `Turbine` |

### **描述** — 信号描述 `char`

信号描述。

例如，下表总结了所列模块的 Power Accounting Bus Creator 参数 **已传输** 参数值。

| 模块 | Power Accounting Bus Creator 参数值 | | |
| --- | --- | --- | --- |
| **信号名称** | **关联端口** | **描述** |
| Ideal Fixed Gear Transmission | `PwrTrnsfrd.PwrDiffrntl` | `{'DiffTrq','DiffSpd'}` | `Differential` |
| `PwrTrnsfrd.PwrEng` | `{'EngTrq','EngSpd'}` | `Engine` |
| Gearbox | `PwrTrnsfrd.PwrBase` | `{{'BTrq','BSpd'}'B'}` | `Base input` |
| `PwrTrnsfrd.PwrFlwr` | `{{'FTrq','FSpd'}'F'}` | `Follower output` |
| Boost Drive Shaft | `PwrTrnsfrd.PwrCmpsr` | `'Cmpsr'` | `Compressor` |
| `PwrTrnsfrd.PwrExt` | `'ExtTrq'` | `External` |
| `PwrTrnsfrd.Turb` | `'Turb'` | `Turbine` |

#### 未传输

### **信号名称** — 信号名称 `char`

信号名称。

例如，下表总结了所列模块的 Power Accounting Bus Creator 参数 **未传输** 参数值。

| 模块 | Power Accounting Bus Creator 参数值 | |
| --- | --- | --- |
| **信号名称** | **描述** |
| Ideal Fixed Gear Transmission | `PwrNotTrnsfrd.PwrDampLoss` | `Damping loss` |
| `PwrNotTrnsfrd.PwrEffLoss` | `Efficiency loss` |
| Gearbox | `PwrNotTrnsfrd.PwrDampLoss` | `Damping loss` |
| `PwrNotTrnsfrd.PwrMechLoss` | `Mechanical loss` |
| Boost Drive Shaft | `PwrNotTrnsfrd.PwrMechLoss` | `Mechanical loss` |

### **描述** — 信号描述 `char`

信号描述。

例如，下表总结了所列模块的 Power Accounting Bus Creator 参数 **未传输** 参数值。

| 模块 | Power Accounting Bus Creator 参数值 | |
| --- | --- | --- |
| **信号名称** | **描述** |
| Ideal Fixed Gear Transmission | `PwrNotTrnsfrd.PwrDampLoss` | `Damping loss` |
| `PwrNotTrnsfrd.PwrEffLoss` | `Efficiency loss` |
| Gearbox | `PwrNotTrnsfrd.PwrDampLoss` | `Damping loss` |
| `PwrNotTrnsfrd.PwrMechLoss` | `Mechanical loss` |
| Boost Drive Shaft | `PwrNotTrnsfrd.PwrMechLoss` | `Mechanical loss` |

#### 存储

### **信号名称** — 信号名称 `char`

信号名称。

例如，下表总结了所列模块的 Power Accounting Bus Creator 参数 **存储** 参数值。

| 模块 | Power Accounting Bus Creator 参数值 | |
| --- | --- | --- |
| **信号名称** | **描述** |
| Ideal Fixed Gear Transmission | `PwrStored.PwrStoredTrans` | `Rotational` |
| Control Volume System | `PwrStored.PwrHeatStored` | `Stored heat` |
| Datasheet Battery | `PwrStored.PwrStoredBatt` | `Battery stored` |

### **描述** — 信号描述 `char`

信号描述。

例如，下表总结了所列模块的 Power Accounting Bus Creator 参数 **存储** 参数值。

| 模块 | Power Accounting Bus Creator 参数值 | |
| --- | --- | --- |
| **信号名称** | **描述** |
| Ideal Fixed Gear Transmission | `PwrStored.PwrStoredTrans` | `Rotational` |
| Control Volume System | `PwrStored.PwrHeatStored` | `Stored heat` |
| Datasheet Battery | `PwrStored.PwrStoredBatt` | `Battery stored` |

## 所属库

Powertrain Blockset / Utilities / Power Accounting

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

创建功率信息总线

为报告系统功率和能量消耗创建功率信息总线。您可以将该模块关联到父系统，选择要跟踪的功率信号类型，并添加信号描述。如果要生成功率和能量报告，必须使用此模块在被控对象模型模块中记录功率信号。Powertrain Blockset™ 被控对象模块使用 Power Accounting Bus Creator 记录功率信号。每个模块的文档包含有关记录的功率总线信号的信息。

系统级功率和能量核算满足能量守恒。

∑​Ptrans+∑​Pnottrans=∑​Pstore

要将 Power Accounting Bus Creator 添加到您的被控对象模块，请按照以下步骤操作：

1. 将 Power Accounting Bus Creator 模块添加到您的模块中。
2. 选择要记录的功率信号类型。请参阅功率信号。
3. 将 Power Accounting Bus Creator 与父子系统关联。请参阅模块关联。
4. 将功率信号连接到 Power Accounting Bus Creator。

   - 遵循符号约定。
   - 为确保您的被控对象模块守恒能量，包含与该模块关联的所有功率。
5. 在 Power Accounting Bus Creator 中：

   - 在 **已传输** 功率选项卡上，指定以下参数：

     - **关联端口**
     - **描述**
   - 在 **未传输** 功率选项卡上，指定 **描述** 参数：
6. 在被控对象模块中，将传输的功率信号连接到使用 **关联端口** 参数指定的 Power Accounting Bus Creator 端口。

### 功率信号

Power Accounting Bus Creator 将信号分为三种功率类型。

| 功率类型 | | 描述 | 示例 |
| --- | --- | --- | --- |
| *Ptrans* | 已传输 | 模块之间传输的功率： - 正信号表示流入模块 - 负信号表示流出模块 | - 从映射发动机传输到变速器的曲轴功率。 - 从车轮传输到车辆的道路负载功率。 - 从节气门传输到歧管容积的热流率。 |
| *Pnottrans* | 未传输 | 穿过模块边界但未传输的功率： - 正信号表示输入 - 负信号表示损耗 | - 与环境的热传递率。 - 来自环境为输入（正信号） - 到环境为损耗（负信号） - 与环境的流动边界。 - 来自环境为输入（正信号） - 到环境为损耗（负信号） - 映射发动机燃料流量。 |
| *Pstore* | 存储 | 存储能量变化率： - 正信号表示增加 - 负信号表示减少 | 能量变化率： - 电池存储 - 传动系统组件中的动能 - 车辆势能 - 车辆速度 |

### 模块关联

当您将 Power Accounting Bus Creator 添加到您的被控对象模块时，您将信号关联到父模块。有两种关联方法。

| 方法 | 描述 | 示例 |
| --- | --- | --- |
| `Parent` | Power Accounting Bus Creator 将功率总线信号与父模块关联。 | 在传统车辆参考应用中，导航到 `Passenger Car > Engine > SiMappedEngine > Accessory Load Model` 被控对象子系统。打开 Power Accounting Bus Creator。**关联模块** 参数设置为 `Parent`，因此 Power Accounting Bus Creator 将功率信号与 `Accessory Load Model` 被控对象子系统关联。Power Accounting Buss Creator 模块掩码，其中 **关联模块** 参数设置为 parent。 |
| `Parent reference block` | Power Accounting Bus Creator 将功率总线信号与参考模块关联。使用 **库模块名称** 参数指定该模块。 | 在 Ideal Fixed Gear Transmission 模块中，导航到 `Bus Creation` 子系统。打开 Power Accounting Bus Creator。Power Accounting Bus Creator 模块使用这些参数设置将功率信号关联到 Ideal Fixed Gear Transmission 模块。 - **关联模块** 参数设置为 `Parent reference block`。 - **库模块名称** 参数设置为 `'autolibsharedtransfixedgear/Ideal Fixed Gear Transmission'`。 Power Accounting Buss Creator 模块掩码，其中 **关联模块** 参数设置为 parent reference block。 |
