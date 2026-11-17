---
type: simulink-block
title: 'PID Gains Store and Update'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Autotuning'
documentation_page: 'pidgainsstoreandupdate'
documentation_source_path: 'ug/pidgainsstoreandupdate.html'
language: zh-CN
chinese_source: worker-translation
---

# PID Gains Store and Update

## 端口
```yaml
ports:
- name: tuned Gains
  summary: 整定后的 PID 增益总线
  direction: input
- name: scheduling Variable
  summary: 调度变量标量
  direction: input
- name: Breakpoints
  summary: 断点数据向量
  direction: input
- name: Update Trigger
  summary: 触发控制信号标量
  direction: input
- name: PID Gains Out
  summary: PID 增益数组总线
  direction: output
```

### 输入

### **tuned Gains** — 整定后的 PID 增益总线

指定要存储和路由的整定后 PID 增益值。通常，这些整定后的增益来自 Closed-Loop PID Autotuner 模块。

该 4 元素总线信号必须包含整定后的 PID 增益 *P*、*I*、*D* 以及滤波器系数 *N*。这些值对应于 **Controller type** 参数中所给表达式中的 `P`、`I`、`D` 和 `N` 参数。在自动整定期间，初始时这些值分别为 0、0、0 和 100。Closed-Loop PID Autotuner 模块在实验结束时更新这些值。即使您未整定 PIDN 控制器，该总线信号也始终包含四个元素。

### **scheduling Variable** — 调度变量标量

指定调度变量。该信号指示系统在给定时刻处于运行范围内的位置。

在增益调度控制应用中，该信号还决定增益何时变化。

#### 依赖关系

要启用此端口，请选择 **Use for gain scheduling**。

### **Breakpoints** — 断点数据向量

用于增益调度的断点数据，指定为向量。

#### 依赖关系

要启用此端口，请选择 **Use external signal**。

### **Update Trigger** — 触发控制信号标量

用于触发增益更新的控制信号。

#### 依赖关系

要启用此端口，请将 **Method to trigger gain update** 设置为 **External trigger**。

### 输出

### **PID Gains Out** — PID 增益数组总线

存储的 PID 增益数组。将该增益数组与断点数据一起使用，以实现基于查找表的增益调度。

使用此端口可指定自定义逻辑来路由增益数组。

要启用此端口，请将 **Method of storing gains** 设置为 `Output from block`。
## 参数
```yaml
parameters:
- name: Controller type
  summary: PID 控制器类型 P（默认）| I | PI | PD | PDN | PID | PIDN
  group: ''
  block_parameter: ControllerType
  type: string
  values: '"P" | "I" | "PI" | "PD" | "PDN" | "PID" | "PIDN"'
  default: '"PID"'
- name: Use for gain scheduling
  summary: 启用模块以进行增益调度 on（默认）| off
  group: ''
  block_parameter: UseGainScheduling
  type: string
  values: '"off" | "on"'
  default: '"on"'
- name: Save breakpoints in gain array
  summary: 将断点与 PID 增益一起保存 off（默认）| on
  group: ''
  block_parameter: SaveBreakpoints
  type: string
  values: '"off" | "on"'
  default: '"off"'
- name: Breakpoints
  summary: 增益调度断点 [1 2 3]（默认）| 向量
  group: ''
  block_parameter: NumBreakpoints
  type: vector
  values: vector of at least two elements
  default: '"[1 2 3]"'
- name: Number of breakpoints
  summary: 断点数量 3（默认）| 正标量
  group: ''
  block_parameter: NumBreakpoints
  type: 标量
  values: 正标量
  default: '3'
- name: Use external signal
  summary: 从输入端口指定断点 off（默认）| on
  group: ''
  block_parameter: UseExternalBreakpoints
  type: 字符串
  values: '"off" | "on"'
  default: '"off"'
- name: Gain index tolerance
  summary: 增益索引容差 1e-3（默认）| 非负标量
  group: ''
  block_parameter: GainIndexTolerance
  type: 标量
  values: 非负标量
  default: 1e-3
- name: Method of storing gains
  summary: 增益存储方法 Data store memory（默认）| Goto/from | Output from block
  group: ''
  block_parameter: TriggerUpdateMethod
  type: 字符串
  values: '"Data store memory" | "Goto/from" | "Output from block"'
  default: '"Data store memory"'
- name: P Gain Parameter Name
  summary: 比例增益数据名称 PGain（默认）| 字符串
  group: ''
  block_parameter: StoreGainsPParamName
  type: 字符串
  default: '"PGain"'
- name: P Gain initial conditions
  summary: 比例增益初始值 0（默认）| 标量 | 向量
  group: ''
  block_parameter: PGainInitialConditions
  type: scalar | vector
  default: '0'
- name: I Gain Parameter Name
  summary: 积分增益数据名称 IGain（默认）| string
  group: ''
  block_parameter: StoreGainsIParamName
  type: string
  default: '"IGain"'
- name: I Gain initial conditions
  summary: 积分增益初始值 0（默认）| scalar | vector
  group: ''
  block_parameter: IGainInitialConditions
  type: scalar | vector
  default: '0'
- name: D Gain Parameter Name
  summary: 微分增益数据名称 DGain（默认）| string
  group: ''
  block_parameter: StoreGainsDParamName
  type: string
  default: '"DGain"'
- name: D Gain initial conditions
  summary: 微分增益初始值 0（默认）| scalar | vector
  group: ''
  block_parameter: DGainInitialConditions
  type: scalar | vector
  default: '0'
- name: N Gain Parameter Name
  summary: 滤波器增益数据名称 NGain（默认）| string
  group: ''
  block_parameter: StoreGainsNParamName
  type: string
  default: '"NGain"'
- name: N Gain initial conditions
  summary: 滤波器增益初始值 100（默认）| scalar | vector
  group: ''
  block_parameter: NGainInitialConditions
  type: scalar | vector
  default: '100'
- name: 触发增益更新的方法
  summary: 更新触发方法 检测 PID 增益变化（默认）| 外部触发
  group: ''
  block_parameter: TriggerUpdateMethod
  type: string
  values: '"Detect change in PID gains" | "External trigger"'
  default: '"Detect change in PID gains"'
- name: 延迟更新的采样数
  summary: 延迟更新的采样数 1（默认）| 非负标量
  group: ''
  block_parameter: NumUpdateDelays
  type: scalar
  values: 非负标量
  default: '1'
- name: 采样时间（-1 表示继承）
  summary: 采样时间 -1（默认）| 正标量
  group: ''
  block_parameter: SampleTime
  type: scalar
  values: 正标量 | –1
  default: –1
- name: 数据类型
  summary: 浮点精度 Double（默认）| Single
  group: ''
  block_parameter: BlockDataType
  type: string
  values: '"Double" | "Single"'
  default: '"Double"'
```

### **Controller type** — PID 控制器类型 `P`（默认）| `I` | `PI` | `PD` | `PDN` | `PID` | `PIDN`

指定系统中 PID 控制器的类型。控制器类型指示控制器中存在的动作。以下控制器类型可用：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDN` — 带微分滤波器的比例和微分
- `PID` — 比例、积分和微分
- `PIDN` — 带微分滤波器的比例、积分和微分

当您使用整定后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保控制器类型匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`ControllerType` |
| **类型**：string |
| **值**：`"P"` | `"I"` | `"PI"` | `"PD"` | `"PDN"` | `"PID"` | `"PIDN"` |
| **默认值**：`"PID"` |

### **Use for gain scheduling** — 启用模块以进行增益调度 `on`（默认）| `off`

使用此选项可启用模块以用于增益调度应用。这样做允许您指定与增益查找一起使用的断点。

#### 编程使用

|  |
| --- |
| **模块参数**：`UseGainScheduling` |
| **类型**：string |
| **Value** `"off"` | `"on"` |
| **默认值**：`"on"` |

### **Save breakpoints in gain array** — 将断点与 PID 增益一起保存 `off`（默认）| `on`

使用此选项可将断点与存储的增益数组一起保存。PID Gain Scheduler 模块可以解释此组合数据以用于增益调度应用。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling**。

#### 编程使用

|  |
| --- |
| **模块参数**：`SaveBreakpoints` |
| **类型**：string |
| **Value** `"off"` | `"on"` |
| **默认值**：`"off"` |

### **Breakpoints** — 增益调度断点 `[1 2 3]`（默认）| 向量

指定增益调度断点数据。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling**。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumBreakpoints` |
| **类型**：vector |
| **值**：vector of at least two elements |
| **默认值**：`"[1 2 3]"` |

### **Number of breakpoints** — 断点数量 `3`（默认）| 正标量

指定外部断点信号中的断点数量。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling** 和 **Use external signal**。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumBreakpoints` |
| **类型：** 标量 |
| **值：** 正标量 |
| **默认值：** `3` |

### **Use external signal** — 从输入端口指定断点 `off`（默认）| `on`

从模块输入端口指定断点。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling**。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseExternalBreakpoints` |
| **类型：** 字符串 |
| **值** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Gain index tolerance** — 增益索引容差 `1e-3`（默认）| 非负标量

指定调度变量与断点之间的容差。为了确定数组中要更新哪个断点，模块将调度变量与断点数组进行比较，并使用此容差值来确定最接近的值。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling**。

#### 编程用法

|  |
| --- |
| **模块参数：** `GainIndexTolerance` |
| **类型：** 标量 |
| **值：** 非负标量 |
| **默认值：** `1e-3` |

### **Method of storing gains** — 增益存储方法 `Data store memory`（默认）| `Goto/from` | `Output from block`

指定增益的存储方法。

- `Data store memory` — 使用 Data Store Memory 模块存储增益。要创建数据存储模块，首先使用每个增益的 **Parameter Name** 参数为数据存储指定名称，然后单击 **Add Data Store Memory blocks to model** 按钮。PID Gains Store and Update 模块在模型的顶层创建 Data Store Memory 模块。您可以直接在 PID Gain Scheduler 模块中指定这些数据存储名称，以执行基于查找表的增益调度。
- `Goto/from` — 使用 Goto 和 From 模块来路由增益。要指定 Goto 标记，请使用每个增益的 **Parameter Name** 参数。您可以直接在 PID Gain Scheduler 模块中指定这些 Goto 标记，以读取和查找增益。
- `Output from block` — 使用 **PID Gains Out** 输出端口。您可以将此输出信号直接馈入 PID Gain Scheduler 模块。

使用 **Gain initial conditions** 参数指定增益的初始值。当调谐增益不可用时，模块使用这些初始值。

#### 编程用法

|  |
| --- |
| **模块参数：** `TriggerUpdateMethod` |
| **类型：** 字符串 |
| **值：** `"Data store memory"` | `"Goto/from"` | `"Output from block"` |
| **默认值：** `"Data store memory"` |

### **P Gain Parameter Name** — 比例增益数据名称 `PGain`（默认）| 字符串

指定比例增益数据的数据存储或 goto 标记的名称。

#### 依赖关系

要启用此参数，请将

- **Controller type** 设置为具有比例作用的控制器类型。
- **Method of obtaining gains** 设置为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StoreGainsPParamName` |
| **类型：** 字符串 |
| **默认值：** `"PGain"` |

### **P Gain initial conditions** — 比例增益初始值 `0`（默认）| 标量 | 向量

将比例增益的初始值指定为标量或向量。当来自外部源（如 Closed-Loop PID Autotuner）的调谐增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定一个与 **Breakpoints** 长度相同的向量。模块使用与当前断点对应的索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有比例作用的控制器类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `PGainInitialConditions` |
| **类型：** scalar | vector |
| **默认值：** 0 |

### **I Gain Parameter Name** — 积分增益数据名称 `IGain`（默认）| string

指定积分增益数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有积分作用的控制器类型。
- **Method of obtaining gains** 为
  `Data store memory` 或
  `Goto/from`。

#### 编程使用

|  |
| --- |
| **模块参数：** `StoreGainsIParamName` |
| **类型：** string |
| **默认值：** `"IGain"` |

### **I Gain initial conditions** — 积分增益初始值 `0`（默认）| scalar | vector

以标量或向量形式指定积分增益的初始值。当来自外部源（如 Closed-Loop PID Autotuner）的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用与当前断点对应索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有积分作用的控制器类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `IGainInitialConditions` |
| **类型：** scalar | vector |
| **默认值：** 0 |

### **D Gain Parameter Name** — 微分增益数据名称 `DGain`（默认）| string

指定微分增益数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有微分作用的控制器类型。
- **Method of obtaining gains** 为
  `Data store memory` 或
  `Goto/from`。

#### 编程使用

|  |
| --- |
| **模块参数：** `StoreGainsDParamName` |
| **类型：** string |
| **默认值：** `"DGain"` |

### **D Gain initial conditions** — 微分增益初始值 `0`（默认）| scalar | vector

以标量或向量形式指定微分增益的初始值。当来自外部源（如 Closed-Loop PID Autotuner）的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用与当前断点对应索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有微分作用的控制器类型。

#### 编程使用

|  |
| --- |
| **模块参数：** `DGainInitialConditions` |
| **类型：** scalar | vector |
| **默认值：** 0 |

### **N Gain Parameter Name** — 滤波器增益数据名称 `NGain`（默认）| string

指定微分滤波器增益数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有滤波微分的控制器类型。
- **Method of obtaining gains** 为
  `Data store memory` 或
  `Goto/from`。

#### 编程使用

|  |
| --- |
| **模块参数：** `StoreGainsNParamName` |
| **类型：** string |
| **默认值：** `"NGain"` |

### **N Gain initial conditions** — 滤波器增益初始值 `100`（默认）| scalar | vector

以标量或向量形式指定微分滤波器增益的初始值。当来自外部源（如 Closed-Loop PID Autotuner）的整定增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用与当前断点对应索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有滤波微分的控制器类型。

#### 依赖关系

要启用此参数，请将 **Method of storing gains** 设置为 `Data store memory` 或
`Goto/from`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NGainInitialConditions` |
| **类型：** scalar | vector |
| **默认值：** 100 |

### **触发增益更新的方法** — 更新触发方法 **检测 PID 增益变化**（默认）| **外部触发**

指定触发增益更新的方法。

- **检测 PID 增益变化** — 当输入增益发生变化时自动更新增益。
- **外部触发** — 使用外部信号触发增益更新。

#### 程序化使用

|  |
| --- |
| **模块参数：** `TriggerUpdateMethod` |
| **类型：** string |
| **值：** `"Detect change in PID gains"` | `"External trigger"` |
| **默认值：** `"Detect change in PID gains"` |

### **延迟更新的采样数** — 延迟更新的采样数 `1`（默认）| 非负标量

触发事件后延迟增益更新的采样数。使用此选项可延迟更新增益，以便为自整定算法提供足够的时间来计算增益。

#### 程序化使用

|  |
| --- |
| **模块参数：** `NumUpdateDelays` |
| **类型：** scalar |
| **值：** 非负标量 |
| **默认值：** `1` |

### **采样时间（-1 表示继承）** — 采样时间 `-1`（默认）| 正标量

指定采样时间。在自整定应用中，此采样时间必须与 PID Controller 和 Closed-Loop PID Autotuner 模块中指定的控制器采样时间一致。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** scalar |
| **值：** 正标量 | –1 |
| **默认值：** `–1` |

### **数据类型** — 浮点精度 `Double`（默认）| `Single`

根据仿真环境或硬件要求指定浮点精度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `BlockDataType` |
| **类型：** string |
| **值：** `"Double"` | `"Single"` |
| **默认值：** `"Double"` |
## 所属库

Simulink Control Design / Autotuning

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

存储并更新使用 Closed-Loop PID Autotuner 整定的 PID 增益

PID Gains Store and Update 模块允许您将 Closed-Loop PID Autotuner 模块获得的增益写入内存位置或将其作为信号输出。使用此模块可以管理自整定过程中在不同工作点获得的增益。

通常，整定增益调度控制器是一个复杂的过程。它需要您在每個工作点运行多次仿真进行整定，并提供逻辑来存储该工作点的 PID 增益。使用此模块以及 Change Operating Points 和 PID Gain Scheduler 模块，可以帮助您在单次运行中实现一个简化的ワークフロー，用于在工作范围内对增益调度 PID 控制器进行自整定。为此，请使用以下工作流程。

1. 使用 Change Operating Points 模块在仿真期间切换预定义或快照工作点数据。
2. 使用 Closed-Loop PID Autotuner 在工作点执行自整定。
3. 使用 PID Gains Store and Update 模块将对应于工作点的 PID 增益存储到数组中。
4. 使用 PID Gain Scheduler 模块从数组执行基于查找表的增益调度。

在高层面上，您可以使用这些模块实现增益调度工作流程，如下图所示。

增益调度系统示意图，包含 Closed-Loop PID Autotuner、PID Controller、Change Operating Points、Gain Scheduler 和 PID Gains Store and Update 模块。
