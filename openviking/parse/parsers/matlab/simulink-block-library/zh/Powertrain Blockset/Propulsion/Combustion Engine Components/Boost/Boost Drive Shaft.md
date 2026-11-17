---
type: simulink-block
title: 'Boost Drive Shaft'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components / Boost'
documentation_page: 'boostdriveshaft'
documentation_source_path: 'ref/boostdriveshaft.html'
language: zh-CN
chinese_source: worker-translation
---

# Boost Drive Shaft

## 端口
```yaml
ports:
- name: Cmprs
  summary: 压气机扭矩双向连接端口
  direction: input
- name: Turb
  summary: 涡轮扭矩双向连接端口
  direction: input
- name: ExtTrq
  summary: 外部施加扭矩 scalar
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: Cmprs
  summary: 压气机转速双向连接端口
  direction: output
- name: Turb
  summary: 涡轮转速双向连接端口
  direction: output
```

### 输入

### **Cmprs** — 压气机扭矩双向连接端口

压气机扭矩，*τcomp*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Configuration** 参数设置为 `Turbocharger` 或 `Compressor only`。

### **Turb** — 涡轮扭矩双向连接端口

涡轮扭矩，*τturb*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Configuration** 参数设置为 `Turbocharger` 或 `Turbine only`。

### **ExtTrq** — 外部施加扭矩 `scalar`

外部施加扭矩，*τext*，单位为 N·m。

#### 依赖

对于涡轮增压器配置，要创建此端口，请将 **Additional torque input** 设置为 `External torque input`。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `DriveshftSpd` | | | 轴转速 | rad/s |
| `MechPwrLoss` | | | 机械功率损失 | W |
| `ExtTrq` | | | 施加的外部扭矩 | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrCmpsr` | 来自压气机的轴功率 | W |
| `PwrTurb` | 来自涡轮的轴功率 | W |
| `PwrExt` | 外部施加的功率 | W |
| `PwrNotTrnsfrd` | `PwrMechLoss` | 机械功率损失 | W |
| `PwrStored` | `PwrStoredDriveshft` | 旋转动能变化率 | W |

### **Cmprs** — 压气机转速双向连接端口

压气机转速，*ω*，单位为 rad/s。

#### 依赖

要创建此端口，请将 **Configuration** 参数设置为 `Turbocharger` 或 `Compressor only`。

### **Turb** — 涡轮转速双向连接端口

涡轮转速，*ω*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Configuration** 参数设置为 `Turbocharger` 或 `Turbine only`。
## 参数
```yaml
parameters:
- name: Configuration
  summary: 指定配置 Turbocharger（默认）| Turbine only | Compressor only
  group: ''
  block_parameter: ShaftConfigPopup
  values: Turbocharger（默认）| Turbine only | Compressor only
- name: Additional torque input
  summary: 指定外部扭矩输入 External torque input（默认）| No external torque
  group: ''
  block_parameter: AddTrqTypePopup
  values: External torque input（默认）| No external torque
- name: Shaft inertia, J_shaft
  summary: 惯量 1.55e-5（默认）| scalar
  group: ''
  block_parameter: J_shaft
  values: 1.55e-5（默认）| scalar
- name: Initial shaft speed, w_0
  summary: 转速 1000（默认）| scalar
  group: ''
  block_parameter: w_0
  values: 1000（默认）| scalar
- name: Min shaft speed, w_min
  summary: 转速 100（默认）| scalar
  group: ''
  block_parameter: w_min
  values: 100（默认）| scalar
- name: Max shaft speed, w_max
  summary: 转速 20000（默认）| scalar
  group: ''
  block_parameter: w_max
  values: 20000（默认）| scalar
- name: Turbine mechanical efficiency, eta_mech
  summary: 效率 0.95（默认）| scalar
  group: ''
  block_parameter: eta_mech
  values: 0.95（默认）| scalar
```

#### 模块选项

### **Configuration** — 指定配置 `Turbocharger`（默认）| `Turbine only` | `Compressor only`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ShaftConfigPopup` |
| **值：** | `Turbocharger`（默认）| `Turbine only` | `Compressor only` |
| **数据类型：** | `character vector` |

#### 依赖

- 选择 `Turbocharger` 或 `Compressor only` 会创建 `Cmprs` 端口。
- 选择 `Turbocharger` 或 `Turbine only` 会创建 `Turb` 端口。

### **Additional torque input** — 指定外部扭矩输入 `External torque input`（默认）| `No external torque`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `AddTrqTypePopup` |
| **值：** | `External torque input`（默认）| `No external torque` |
| **数据类型：** | `character vector` |

#### 依赖

- 要启用此参数，请选择 `Turbocharger` 配置。
- 要创建 `Trq` 端口，请选择 `External torque input`。

### **Shaft inertia, J\_shaft** — 惯量 `1.55e-5`（默认）| `scalar`

轴惯量，*Jshaft*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `J_shaft` |
| **值：** | `1.55e-5`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Initial shaft speed, w\_0** — 转速 `1000`（默认）| `scalar`

初始驱动轴转速，*ω0*，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_0` |
| **值：** | `1000`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Min shaft speed, w\_min** — 转速 `100`（默认）| `scalar`

最小驱动轴转速，*ωmin*，
单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `w_min` |
| **值**：| `100`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Max shaft speed, w\_max** — 转速 `20000`（默认）| `scalar`

最大驱动轴转速，*ωmax*，
单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `w_max` |
| **值**：| `20000`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Turbine mechanical efficiency, eta\_mech** — 效率 `0.95`（默认）| `scalar`

涡轮机械效率
*ηmax*。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `eta_mech` |
| **值**：| `0.95`（默认）| `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请选择
`Turbocharger` 或 `Turbine
only` 配置。
## 所属库

Powertrain Blockset / Propulsion / Combustion Engine Components / Boost

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

Boost 驱动轴转速

Boost Drive Shaft 模块使用压缩机、
涡轮和外部转矩来计算驱动轴转速。
使用该模块可在发动机
模型中建模涡轮增压器和机械增压器。

您可以指定以下配置：

- Turbocharger — 将压缩机连接到
  涡轮

  - 用于涡轮和压缩机连接的双向端口
  - 可选择添加外部施加的输入转矩
- Compressor only — 将驱动轴连接到
  压缩机

  - 用于压缩机连接的双向端口
  - 外部施加的输入转矩
- Turbine only — 将驱动轴连接到
  涡轮

  - 用于涡轮连接的双向端口
  - 外部施加的负载转矩

对于 `Turbine only` 和 `Turbocharger` 配置，
该模块使用机械效率修正涡轮转矩。

### 方程

Boost Drive Shaft 模块应用牛顿
第二旋转定律。正转矩使驱动轴
加速。负转矩施加负载并使驱动
轴减速。

该模块还计算由机械效率不足导致的功率损失。

| Calculation | Equations |
| --- | --- |
| Shaft dynamics | dωdt=1Jshaft(ηmechτturb+τcomp+τext) 初始转速为 *ω0* |
| Speed constraint | ωmin≤ω≤ωmax |
| Power loss | W˙loss=ωτturb(1−ηmech) |

### Power Accounting

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrCmpsr` | 来自压缩机的轴功率 | τcompω |
| `PwrTurb` | 来自涡轮的轴功率 | τturbω |
| `PwrExt` | 外部施加的功率 | τextω |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrMechLoss` | 机械功率损失 | −W˙turb |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredDriveshft` | 旋转动能的变化率 | (ηmechτturb+τcomp+τext)ω |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ω* | 轴转速 |
| *ω0* | 初始驱动轴转速 |
| *ωmin* | 最小驱动轴转速 |
| *ωmax* | 最大驱动轴转速 |
| *Jshaft* | 轴惯量 |
| *ηmax* | 涡轮的机械效率 |
| *τcomp* | 压缩机扭矩 |
| *τturb* | 涡轮扭矩 |
| *τext* | 外部施加的扭矩。 |
| W˙loss | 由于机械效率低下导致的功率损失 |
