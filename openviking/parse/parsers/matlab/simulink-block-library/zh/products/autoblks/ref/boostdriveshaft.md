---
type: simulink-block
title: 'Boost Drive Shaft'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Components'
documentation_page: 'boostdriveshaft'
documentation_source_path: 'ref/boostdriveshaft.html'
language: zh-CN
chinese_source: worker-translation
---

# Boost Drive Shaft

## 端口

### 输入

### **Cmprs** — 压缩机扭矩双向连接器端口

压缩机扭矩，*τcomp*，单位为 N·m。

#### 依赖关系

要创建此端口，对于**配置**参数，选择 `Turbocharger` 或 `Compressor only`。

### **Turb** — 涡轮扭矩双向连接器端口

涡轮扭矩，*τturb*，单位为 N·m。

#### 依赖关系

要创建此端口，对于**配置**参数，选择 `Turbocharger` 或 `Turbine only`。

### **ExtTrq** — 外部施加扭矩 `scalar`

外部施加扭矩，*τext*，单位为 N·m。

#### 依赖关系

对于涡轮增压器配置，要创建此端口，请将**附加扭矩输入**设置为 `External torque input`。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `DriveshftSpd` | | | 传动轴速度 | rad/s |
| `MechPwrLoss` | | | 机械功率损失 | W |
| `ExtTrq` | | | 施加的外部扭矩 | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrCmpsr` | 来自压缩机的轴功率 | W |
| `PwrTurb` | 来自涡轮的轴功率 | W |
| `PwrExt` | 外部施加功率 | W |
| `PwrNotTrnsfrd` | `PwrMechLoss` | 机械功率损失 | W |
| `PwrStored` | `PwrStoredDriveshft` | 旋转动能变化率 | W |

### **Cmprs** — 压缩机速度双向连接器端口

压缩机速度，*ω*，单位为 rad/s。

#### 依赖关系

要创建此端口，对于**配置**参数，选择 `Turbocharger` 或 `Compressor only`。

### **Turb** — 涡轮速度双向连接器端口

涡轮速度，*ω*，单位为 N·m。

#### 依赖关系

要创建此端口，对于**配置**参数，选择 `Turbocharger` 或 `Turbine only`。

## 参数

#### 模块选项

### **配置** — 指定配置 `Turbocharger` (默认) | `Turbine only` | `Compressor only`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShaftConfigPopup` |
| **值：** | `Turbocharger` (默认) | `Turbine only` | `Compressor only` |
| **数据类型：** | `character vector` |

#### 依赖关系

- 选择 `Turbocharger` 或 `Compressor only` 会创建 `Cmprs` 端口。
- 选择 `Turbocharger` 或 `Turbine only` 会创建 `Turb` 端口。

### **附加扭矩输入** — 指定外部扭矩输入 `External torque input` (默认) | `No external torque`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AddTrqTypePopup` |
| **值：** | `External torque input` (默认) | `No external torque` |
| **数据类型：** | `character vector` |

#### 依赖关系

- 要启用此参数，请选择 `Turbocharger` 配置。
- 要创建 `Trq` 端口，请选择 `External torque input`。

### **轴惯量, J\_shaft** — 惯量 `1.55e-5` (默认) | `scalar`

轴惯量，*Jshaft*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J_shaft` |
| **值：** | `1.55e-5` (默认) | `scalar` |
| **数据类型：** | `double` |

### **初始传动轴速度, w\_0** — 速度 `1000` (默认) | `scalar`

初始传动轴速度，*ω0*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_0` |
| **值：** | `1000` (默认) | `scalar` |
| **数据类型：** | `double` |

### **最小传动轴速度, w\_min** — 速度 `100` (默认) | `scalar`

最小传动轴速度，*ωmin*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_min` |
| **值：** | `100` (默认) | `scalar` |
| **数据类型：** | `double` |

### **最大传动轴速度, w\_max** — 速度 `20000` (默认) | `scalar`

最大传动轴速度，*ωmax*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_max` |
| **值：** | `20000` (默认) | `scalar` |
| **数据类型：** | `double` |

### **涡轮机械效率, eta\_mech** — 效率 `0.95` (默认) | `scalar`

涡轮的机械效率 *ηmax*。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `eta_mech` |
| **值：** | `0.95` (默认) | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 `Turbocharger` 或 `Turbine only` 配置。

## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Boost

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

Boost 传动轴速度

Boost Drive Shaft 模块使用压缩机扭矩、涡轮扭矩和外部扭矩来计算传动轴速度。使用该模块在发动机模型中为涡轮增压器和机械增压器建模。

您可以指定以下配置：

- Turbocharger — 将压缩机连接到涡轮

  - 用于涡轮和压缩机连接的双向端口
  - 添加外部施加输入扭矩的选项
- Compressor only — 将传动轴连接到压缩机

  - 用于压缩机连接的双向端口
  - 外部施加输入扭矩
- Turbine only — 将传动轴连接到涡轮

  - 用于涡轮连接的双向端口
  - 外部施加负载扭矩

对于 `Turbine only` 和 `Turbocharger` 配置，模块使用机械效率修正涡轮扭矩。

### 方程

Boost Drive Shaft 模块应用牛顿第二旋转定律。正扭矩使传动轴加速。负扭矩施加负载并使传动轴减速。

该模块还计算由机械效率不足引起的功率损失。

| 计算 | 方程 |
| --- | --- |
| 轴动力学 | dωdt=1Jshaft(ηmechτturb+τcomp+τext)，初始速度为 *ω0* |
| 速度约束 | ωmin≤ω≤ωmax |
| 功率损失 | W˙loss=ωτturb(1−ηmech) |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrCmpsr` | 来自压缩机的轴功率 | τcompω |
| `PwrTurb` | 来自涡轮的轴功率 | τturbω |
| `PwrExt` | 外部施加功率 | τextω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrMechLoss` | 机械功率损失 | −W˙turb |
| `PwrStored` — 储能变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredDriveshft` | 旋转动能变化率 | (ηmechτturb+τcomp+τext)ω |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ω* | 传动轴速度 |
| *ω0* | 初始传动轴速度 |
| *ωmin* | 最小传动轴速度 |
| *ωmax* | 最大传动轴速度 |
| *Jshaft* | 传动轴惯量 |
| *ηmax* | 涡轮的机械效率 |
| *τcomp* | 压缩机扭矩 |
| *τturb* | 涡轮扭矩 |
| *τext* | 外部施加扭矩。 |
| W˙loss | 由机械效率不足引起的功率损失 |
