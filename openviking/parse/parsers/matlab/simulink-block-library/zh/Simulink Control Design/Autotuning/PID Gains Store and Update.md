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

### 输入

### **tuned Gains** — 调优后的 PID 增益总线

指定要存储和路由的调优后的 PID 增益值。通常，您从 Closed-Loop PID Autotuner 模块获得这些调优后的增益。

此 4 元素总线信号必须包含调优后的 PID 增益 *P*、*I*、*D* 以及滤波系数 *N*。这些值对应于 **Controller type** 参数中给出的表达式中的 `P`、`I`、`D` 和 `N` 参数。在自动调优期间，初始时这些值分别为 0、0、0 和 100。Closed-Loop PID Autotuner 模块在实验结束时更新这些值。即使您未在调优 PIDN 控制器，此总线信号也始终具有四个元素。

### **scheduling Variable** — 调度变量标量

指定调度变量。此信号指示系统在给定时间处于运行范围内的位置。

在增益调度控制应用中，此信号还决定增益何时变化。

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

存储的 PID 增益数组。将此增益数组与断点数据一起使用，以实现基于查找表的增益调度。

使用此端口指定自定义逻辑来路由增益数组。

要启用此端口，请将 **Method of storing gains** 设置为 `Output from block`。

## 参数

### **Controller type** — PID 控制器类型 `P` (默认) | `I` | `PI` | `PD` | `PDN` | `PID` | `PIDN`

指定系统中 PID 控制器的类型。控制器类型指示控制器中存在哪些作用。以下控制器类型可用：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDN` — 带微分滤波的比例和微分
- `PID` — 比例、积分和微分
- `PIDN` — 带微分滤波的比例、积分和微分

当您使用调优后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保控制器类型匹配。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControllerType` |
| **类型：** string |
| **值：** `"P"` | `"I"` | `"PI"` | `"PD"` | `"PDN"` | `"PID"` | `"PIDN"` |
| **默认值：** `"PID"` |

### **Use for gain scheduling** — 启用模块以进行增益调度 `on` (默认) | `off`

使用此选项为增益调度应用启用模块。这样做允许您指定用于增益查找的断点。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseGainScheduling` |
| **类型：** string |
| **值** `"off"` | `"on"` |
| **默认值：** `"on"` |

### **Save breakpoints in gain array** — 将断点与 PID 增益一起保存 `off` (默认) | `on`

使用此选项将断点与存储的增益数组一起保存。PID Gain Scheduler 模块可以为增益调度应用解释此组合数据。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling**。

#### 编程用法

|  |
| --- |
| **模块参数：** `SaveBreakpoints` |
| **类型：** string |
| **值** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Breakpoints** — 增益调度断点 `[1 2 3]` (默认) | 向量

指定增益调度断点数据。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling**。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumBreakpoints` |
| **类型：** vector |
| **值：** 至少包含两个元素的向量 |
| **默认值：** `"[1 2 3]"` |

### **Number of breakpoints** — 断点数量 `3` (默认) | 正标量

指定外部断点信号中断点的数量。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling** 和 **Use external signal**。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumBreakpoints` |
| **类型：** scalar |
| **值：** 正标量 |
| **默认值：** `3` |

### **Use external signal** — 从输入端口指定断点 `off` (默认) | `on`

从模块输入端口指定断点。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling**。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseExternalBreakpoints` |
| **类型：** string |
| **值** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Gain index tolerance** — 增益索引容差 `1e-3` (默认) | 非负标量

指定调度变量与断点之间的容差。为了确定要更新数组中的哪个断点，模块将调度变量与断点数组进行比较，并使用此容差值确定最接近的值。

#### 依赖关系

要启用此参数，请选择 **Use for gain scheduling**。

#### 编程用法

|  |
| --- |
| **模块参数：** `GainIndexTolerance` |
| **类型：** scalar |
| **值：** 非负标量 |
| **默认值：** `1e-3` |

### **Method of storing gains** — 存储增益的方法 `Data store memory` (默认) | `Goto/from` | `Output from block`

指定存储增益的方法。

- `Data store memory` — 使用 Data Store Memory 模块存储增益。要创建数据存储模块，首先使用每个增益的 **Parameter Name** 参数指定数据存储的名称，然后单击 **Add Data Store Memory blocks to model** 按钮。PID Gains Store and Update 模块在模型的顶层创建 Data Store Memory 模块。您可以直接在 PID Gain Scheduler 模块中指定这些数据存储名称，以执行基于查找表的增益调度。
- `Goto/from` — 使用 Goto 和 From 模块路由增益。要指定 Goto 标签，请为每个增益使用 **Parameter Name** 参数。您可以直接在 PID Gain Scheduler 模块中指定这些 Goto 标签，以读取和查找增益。
- `Output from block` — 使用 **PID Gains Out** 输出端口。您可以将此输出信号直接馈入 PID Gain Scheduler 模块。

使用 **Gain initial conditions** 参数指定增益的初始值。当调优后的增益不可用时，模块使用这些初始值。

#### 编程用法

|  |
| --- |
| **模块参数：** `TriggerUpdateMethod` |
| **类型：** string |
| **值：** `"Data store memory"` | `"Goto/from"` | `"Output from block"` |
| **默认值：** `"Data store memory"` |

### **P Gain Parameter Name** — 比例增益数据名称 `PGain` (默认) | 字符串

指定比例增益数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有比例作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StoreGainsPParamName` |
| **类型：** string |
| **默认值：** `"PGain"` |

### **P Gain initial conditions** — 比例增益初始值 `0` (默认) | 标量 | 向量

将比例增益的初始值指定为标量或向量。当来自外部源（如 Closed-Loop PID Autotuner）的调优增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用当前断点对应索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有比例作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `PGainInitialConditions` |
| **类型：** scalar | vector |
| **默认值：** 0 |

### **I Gain Parameter Name** — 积分增益数据名称 `IGain` (默认) | 字符串

指定积分增益数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有积分作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StoreGainsIParamName` |
| **类型：** string |
| **默认值：** `"IGain"` |

### **I Gain initial conditions** — 积分增益初始值 `0` (默认) | 标量 | 向量

将积分增益的初始值指定为标量或向量。当来自外部源（如 Closed-Loop PID Autotuner）的调优增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用当前断点对应索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有积分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `IGainInitialConditions` |
| **类型：** scalar | vector |
| **默认值：** 0 |

### **D Gain Parameter Name** — 微分增益数据名称 `DGain` (默认) | 字符串

指定微分增益数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有微分作用的控制器类型。
- **Method of obtaining gains** 为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StoreGainsDParamName` |
| **类型：** string |
| **默认值：** `"DGain"` |

### **D Gain initial conditions** — 微分增益初始值 `0` (默认) | 标量 | 向量

将微分增益的初始值指定为标量或向量。当来自外部源（如 Closed-Loop PID Autotuner）的调优增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用当前断点对应索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有微分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `DGainInitialConditions` |
| **类型：** scalar | vector |
| **默认值：** 0 |

### **N Gain Parameter Name** — 滤波器增益数据名称 `NGain` (默认) | 字符串

指定微分滤波器增益数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有滤波微分的控制器类型。
- **Method of obtaining gains** 为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StoreGainsNParamName` |
| **类型：** string |
| **默认值：** `"NGain"` |

### **N Gain initial conditions** — 滤波器增益初始值 `100` (默认) | 标量 | 向量

将微分滤波器增益的初始值指定为标量或向量。当来自外部源（如 Closed-Loop PID Autotuner）的调优增益数据不可用时，模块使用此值。

- 标量 — 模块对所有断点使用此值。
- 向量 — 指定与 **Breakpoints** 长度相同的向量。模块使用当前断点对应索引处的初始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有滤波微分的控制器类型。

#### 依赖关系

要启用此参数，请将 **Method of storing gains** 设置为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `NGainInitialConditions` |
| **类型：** scalar | vector |
| **默认值：** 100 |

### **Method to trigger gain update** — 触发增益更新的方法 **Detect change in PID gains** (默认) | **External trigger**

指定触发增益更新的方法。

- **Detect change in PID gains** — 当输入增益发生变化时自动更新增益。
- **External trigger** — 使用外部信号触发增益更新。

#### 编程用法

|  |
| --- |
| **模块参数：** `TriggerUpdateMethod` |
| **类型：** string |
| **值：** `"Detect change in PID gains"` | `"External trigger"` |
| **默认值：** `"Detect change in PID gains"` |

### **Number of samples to delay update** — 延迟更新的采样数 `1` (默认) | 非负标量

在触发事件后延迟增益更新的采样数。使用此选项延迟更新增益，以便为自动调优算法留出足够的时间来计算增益。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumUpdateDelays` |
| **类型：** scalar |
| **值：** 非负标量 |
| **默认值：** `1` |

### **Sample time (-1 for inherited)** — 采样时间 `-1` (默认) | 正标量

指定采样时间。在自动调优应用中，此采样时间必须与 PID Controller 和 Closed-Loop PID Autotuner 模块中指定的控制器采样时间匹配。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** scalar |
| **值：** 正标量 | –1 |
| **默认值：** `–1` |

### **Data Type** — 浮点精度 `Double` (默认) | `Single`

根据仿真环境或硬件要求指定浮点精度。

#### 编程用法

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

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

存储和更新使用 Closed-Loop PID Autotuner 调优后的 PID 增益

PID Gains Store and Update 模块允许您将来自 Closed-Loop PID Autotuner 模块的增益写入内存位置，或将它们作为信号路由。使用此模块管理在自动调优过程中各个操作点获得的增益。

通常，调优增益调度控制器是一个复杂过程。它要求您在每个操作点运行多次仿真来进行调优，并提供逻辑来存储该操作点的 PID 增益。将此模块与 Change Operating Points 和 PID Gain Scheduler 模块一起使用，可帮助您在单次运行中针对整个运行范围内自动调优增益调度 PID 控制器实现简化的工作流。为此，请使用此工作流。

1. 使用 Change Operating Points 模块在仿真期间切换预定义或快照操作点数据。
2. 使用 Closed-Loop PID Autotuner 在操作点执行自动调优。
3. 使用 PID Gains Store and Update 模块将对应于操作点的 PID 增益存储在数组中。
4. 使用 PID Gain Scheduler 模块从数组执行基于查找表的增益调度。

从高层次看，您可以使用这些模块实现如图所示增益调度工作流。

增益调度系统图，包含 Closed-Loop PID Autotuner、PID Controller、Change Operating Points、Gain Scheduler 和 PID Gains Store and Update 模块。
