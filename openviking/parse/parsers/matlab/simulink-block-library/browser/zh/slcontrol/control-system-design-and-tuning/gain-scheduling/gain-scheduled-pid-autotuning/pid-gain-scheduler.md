---
type: simulink-block
title: 'PID Gain Scheduler'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / PID Controller Tuning / Real-Time PID Autotuning'
documentation_page: 'pidgainscheduler'
documentation_source_path: 'ug/pidgainscheduler.html'
language: zh-CN
chinese_source: worker-translation
---

# PID Gain Scheduler

## 端口

### 输入

### **scheduling Variable** — 调度变量标量

指定调度变量。此信号指示系统在给定时间处于运行范围内的位置。查找表使用此信号确定 PID 增益的值。

### **Breakpoints** — 断点数据向量

用于增益调度的断点数据，指定为向量。

#### 依赖关系

要启用此端口，请选择 **使用外部信号**。

### **PID Gains** — PID 增益数组总线

存储的 PID 增益数组。将此增益数组与断点数据结合使用，以实现基于查找表的增益调度。

此 4 元素总线信号必须包含整定后的 PID 增益 *P*、*I*、*D* 以及滤波器系数 *N*。这些值对应于 **控制器类型** 参数中给出的表达式中的 `P`、`I`、`D` 和 `N` 参数。即使您没有整定 PIDN 控制器，此总线信号也始终具有四个元素。

通常，您使用 PID Gains Store and Update 模块获得此类数组。

#### 依赖关系

要启用此端口，请将 **获取增益的方法** 设置为 `Input to block`
### 输出

### **P** — 比例增益向量

该模块使用断点向量和 PID 增益输入数组计算增益。查找方法可以使用插值、外插或输入增益的原始值。

#### 依赖关系

要启用此端口，请将 **控制器类型** 设置为具有比例作用的控制器类型。

### **I** — 积分增益向量

该模块使用断点向量和 PID 增益输入数组计算增益。查找方法可以使用插值、外插或输入增益的原始值。

#### 依赖关系

要启用此端口，请将 **控制器类型** 设置为具有积分作用的控制器类型。

### **D** — 微分增益向量

该模块使用断点向量和 PID 增益输入数组计算增益。查找方法可以使用插值、外插或输入增益的原始值。

#### 依赖关系

要启用此端口，请将 **控制器类型** 设置为具有微分作用的控制器类型。

### **N** — 微分滤波器增益向量

该模块使用断点向量和 PID 增益输入数组计算增益。查找方法可以使用插值、外插或输入增益的原始值。

#### 依赖关系

要启用此端口，请将 **控制器类型** 设置为具有滤波微分作用的控制器类型。

## 参数

### **控制器类型** — PID 控制器类型 `P` (默认) | `I` | `PI` | `PD` | `PDN` | `PID` | `PIDN`

指定系统中 PID 控制器的类型。控制器类型指示控制器中存在的动作。以下控制器类型可用：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDN` — 比例和微分，带微分滤波器
- `PID` — 比例、积分和微分
- `PIDN` — 比例、积分和微分，带微分滤波器

当您使用整定后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保控制器类型匹配。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControllerType` |
| **类型：** string |
| **值：** `"P"` | `"I"` | `"PI"` | `"PD"` | `"PDN"` | `"PID"` | `"PIDN"` |
| **默认值：** `"PID"` |

### **保存在增益数组中的断点** — 读取保存在增益数组中的断点 `off` (默认) | `on`

当增益数组还包含断点数据时，启用此选项。通常，当您使用 PID Gains Store and Update 模块存储 PID 增益并启用 **在增益数组中保存断点** 时，会获得此类数组。

#### 编程用法

|  |
| --- |
| **模块参数：** `BPsInGainArray` |
| **类型：** string |
| **值** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **断点** — 增益调度断点 `[1 2 3]` (默认) | vector

指定增益调度断点数据。

#### 依赖关系

要启用此参数，请禁用 **保存在增益数组中的断点**。

#### 编程用法

|  |
| --- |
| **模块参数：** `GainArrayBreakpoints` |
| **类型：** string |
| **值：** 至少包含两个元素的向量 |
| **默认值：** `"[1 2 3]"` |

### **使用外部信号** — 从输入端口指定断点 `off` (默认) | `on`

从模块输入端口指定断点。

#### 依赖关系

要启用此参数，请禁用 **保存在增益数组中的断点**。

#### 编程用法

|  |
| --- |
| **模块参数：** `UseExternalBreakpoints` |
| **类型：** string |
| **值** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **获取增益的方法** — 获取增益的方法 `Data store memory` (默认) | `Goto/from` | `Input to block`

指定获取增益的方法。

- `Data store memory` — 使用 Data Store Memory 模块读取增益。为此，请使用与使用 PID Gains Store and Update 模块创建的 Data Store Memory 模块中的数据存储名称相同的名称。
- `Goto/from` — 使用 From 模块标签读取增益。要指定标签名称，请为每个增益使用 **参数名称** 参数。您可以指定使用 PID Gain Scheduler 模块创建的这些 Goto 标签，以读取和查找增益。
- `Input to block` — 使用 **PID Gains** 输入端口。您可以将 PID Gain Scheduler 模块的输出信号馈送到此输入。

#### 编程用法

|  |
| --- |
| **模块参数：** `GainSourceMethod` |
| **类型：** string |
| **值：** `"Data store memory"` | `"Goto/from"` | `"Input to block"` |
| **默认值：** `"Data store memory"` |

### **P 增益参数名称** — 比例增益数据名称 `PGain` (默认) | string

指定此模块从中读取比例增益参数数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **控制器类型** 为具有比例作用的控制器类型。
- **获取增益的方法** 为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StoreGainsPParamName` |
| **类型：** string |
| **默认值：** `"PGain"` |

### **I 增益参数名称** — 积分增益数据名称 `IGain` (默认) | string

指定此模块从中读取积分增益参数数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **控制器类型** 为具有积分作用的控制器类型。
- **获取增益的方法** 为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StoreGainsIParamName` |
| **类型：** string |
| **默认值：** `"IGain"` |

### **D 增益参数名称** — 微分增益数据名称 `DGain` (默认) | string

指定此模块从中读取微分增益参数数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **控制器类型** 为具有微分作用的控制器类型。
- **获取增益的方法** 为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StoreGainsDParamName` |
| **类型：** string |
| **默认值：** `"DGain"` |

### **N 增益参数名称** — 滤波器增益数据名称 `NGain` (默认) | string

指定此模块从中读取滤波器增益参数数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **控制器类型** 为具有滤波微分作用的控制器类型。
- **获取增益的方法** 为 `Data store memory` 或 `Goto/from`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StoreGainsNParamName` |
| **类型：** string |
| **默认值：** `"NGain"` |

### **数据类型** — 浮点精度 `Double` (默认) | `Single`

根据仿真环境或硬件要求指定浮点精度。

#### 编程用法

|  |
| --- |
| **模块参数：** `BlockDataType` |
| **类型：** string |
| **值：** `"Double"` | `"Single"` |
| **默认值：** `"Double"` |

### **P 增益查找方法** — 比例增益查找方法 `Interpolation-Use End Values` (默认) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅模块如何生成输出。

#### 依赖关系

要启用此端口，请将 **控制器类型** 设置为具有比例作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `PGainLookUpMeth` |
| **类型：** string |
| **值：** `"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **默认值：** `"Use Input Above"` |

### **I 增益查找方法** — 积分增益查找方法 `Interpolation-Use End Values` (默认) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅模块如何生成输出。

#### 依赖关系

要启用此端口，请将 **控制器类型** 设置为具有积分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `IGainLookUpMeth` |
| **类型：** string |
| **值：** `"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **默认值：** `"Use Input Above"` |

### **D 增益查找方法** — 微分增益查找方法 `Interpolation-Use End Values` (默认) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅模块如何生成输出。

#### 依赖关系

要启用此端口，请将 **控制器类型** 设置为具有微分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `DGainLookUpMeth` |
| **类型：** string |
| **值：** `"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **默认值：** `"Use Input Above"` |

### **N 增益查找方法** — 微分滤波器增益查找方法 `Interpolation-Use End Values` (默认) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅模块如何生成输出。

#### 依赖关系

要启用此端口，请将 **控制器类型** 设置为具有滤波微分作用的控制器类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `NGainLookUpMeth` |
| **类型：** string |
| **值：** `"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **默认值：** `"Use Input Above"` |

### **发生溢出时饱和到最大值或最小值** — 溢出操作的方法 `off` (默认) | `on`

当您选中此复选框时，溢出会饱和到数据类型可以表示的最大值或最小值。否则，溢出将回绕。

当您选中此复选框时，饱和会应用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

|  |
| --- |
| **模块参数：** `DoSatur` |
| **类型：** string |
| **值：** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **锁定输出数据类型设置，防止定点工具更改** — 防止定点工具覆盖输出数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **输出** 数据类型。有关详细信息，请参阅使用锁定输出数据类型设置（Fixed-Point Designer）。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** string |
| **值：** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式（Fixed-Point Designer）。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **值：** `"Ceiling"` | `"Convergent"` | `"Floor"` | `"Nearest"` | `"Round"` | `"Simplest"` | `"Zero"` |
| **默认值：** `"Floor"` |

## 所属库

Simulink Control Design / Autotuning

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

基于查找表的 PID 数组增益调度

PID Gain Scheduler 模块允许您根据增益数组、对应的断点数据和调度变量查找系统当前状态的 PID 增益。该模块使用查找表将特定 PID 增益与对应的断点值关联，并根据当前工作点（调度变量）提供动态调整的 PID 增益。您可以将这些增益用作模型中 PID 控制器或其他相关模块的输入。查找方法可以使用插值、外插或输入增益的原始值。

通常，整定增益调度控制器是一个复杂的过程。它要求您在每个工作点运行多次仿真进行整定，并提供在该工作点存储 PID 增益的逻辑。将此模块与 Change Operating Points 和 PID Gains Store and Update 模块一起使用，有助于您实现在单次仿真中跨运行范围自动整定增益调度 PID 控制器的简化工作流。为此，请使用以下工作流。

1. 在仿真期间使用 Change Operating Points 模块在预定义或快照工作点数据之间切换。
2. 使用 Closed-Loop PID Autotuner 在工作点执行自动整定。
3. 使用 PID Gains Store and Update 模块将与工作点对应的 PID 增益存储在数组中。
4. 使用 PID Gain Scheduler 模块从数组执行基于查找表的增益调度。

在高层面上，您可以使用这些模块实现如图所示增益调度工作流。

增益调度系统图，包含 Closed-Loop PID Autotuner、PID Controller、Change Operating Points、Gain Scheduler 和 PID Gains Store and Update 模块。
