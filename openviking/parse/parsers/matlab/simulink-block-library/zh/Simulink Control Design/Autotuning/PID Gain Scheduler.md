---
type: simulink-block
title: 'PID Gain Scheduler'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Autotuning'
documentation_page: 'pidgainscheduler'
documentation_source_path: 'ug/pidgainscheduler.html'
language: zh-CN
chinese_source: worker-translation
---

# PID Gain Scheduler

## 端口
```yaml
ports:
- name: scheduling Variable
  summary: 调度变量标量
  direction: input
- name: Breakpoints
  summary: 断点数据向量
  direction: input
- name: PID Gains
  summary: PID 增益数组总线
  direction: input
- name: P
  summary: 比例增益向量
  direction: output
- name: I
  summary: 积分增益向量
  direction: output
- name: D
  summary: 微分增益向量
  direction: output
- name: N
  summary: 微分滤波器增益向量
  direction: output
```

### 输入

### **scheduling Variable** — 调度变量标量

指定调度变量。此信号指示系统在给定时刻处于运行范围内的位置。查找表使用此信号来确定 PID 增益的值。

### **Breakpoints** — 断点数据向量

用于增益调度的断点数据，指定为向量。

#### 依赖关系

要启用此端口，请选择 **Use external signal**。

### **PID Gains** — PID 增益数组总线

存储的 PID 增益数组。将此增益数组与断点数据一起使用，以实现基于查找表的增益调度。

此 4 元素总线信号必须包含整定后的 PID 增益 *P*、*I*、*D* 以及滤波器系数 *N*。这些值对应于 **Controller type** 参数中所给表达式中的 `P`、`I`、`D` 和 `N` 参数。此总线信号始终具有四个元素，即使您未整定 PIDN 控制器。

通常，您使用 PID Gains Store and Update 模块获得此类数组。

#### 依赖关系

要启用此端口，请将 **Method of obtaining gains** 设置为 `Input to block`。

### 输出

### **P** — 比例增益向量

该模块使用断点向量和 PID 增益输入数组计算增益。查找方法可以使用插值、外推或输入增益的原始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有比例作用的控制器类型。

### **I** — 积分增益向量

该模块使用断点向量和 PID 增益输入数组计算增益。查找方法可以使用插值、外推或输入增益的原始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有积分作用的控制器类型。

### **D** — 微分增益向量

该模块使用断点向量和 PID 增益输入数组计算增益。查找方法可以使用插值、外推或输入增益的原始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有微分作用的控制器类型。

### **N** — 微分滤波器增益向量

该模块使用断点向量和 PID 增益输入数组计算增益。查找方法可以使用插值、外推或输入增益的原始值。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有滤波微分作用的控制器类型。
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
- name: Breakpoints saved in gain array
  summary: 读取保存在增益数组中的断点 off（默认）| on
  group: ''
  block_parameter: BPsInGainArray
  type: string
  values: '"off" | "on"'
  default: '"off"'
- name: Breakpoints
  summary: 增益调度断点 [1 2 3]（默认）| 向量
  group: ''
  block_parameter: GainArrayBreakpoints
  type: string
  values: 至少包含两个元素的向量
  default: '"[1 2 3]"'
- name: Use external signal
  summary: 从输入端口指定断点 off（默认）| on
  group: ''
  block_parameter: UseExternalBreakpoints
  type: string
  values: '"off" | "on"'
  default: '"off"'
- name: Method of obtaining gains
  summary: 获取增益的方法 Data store memory（默认）| Goto/from | Input to block
  group: ''
  block_parameter: GainSourceMethod
  type: string
  values: '"Data store memory" | "Goto/from" | "Input to block"'
  default: '"Data store memory"'
- name: P Gain Parameter Name
  summary: 比例增益数据名称 PGain（默认）| string
  group: ''
  block_parameter: StoreGainsPParamName
  type: string
  default: '"PGain"'
- name: I Gain Parameter Name
  summary: 积分增益数据名称 IGain（默认）| string
  group: ''
  block_parameter: StoreGainsIParamName
  type: string
  default: '"IGain"'
- name: D Gain Parameter Name
  summary: 微分增益数据名称 DGain（默认）| string
  group: ''
  block_parameter: StoreGainsDParamName
  type: string
  default: '"DGain"'
- name: N Gain Parameter Name
  summary: 滤波器增益数据名称 NGain（默认）| string
  group: ''
  block_parameter: StoreGainsNParamName
  type: string
  default: '"NGain"'
- name: Data type
  summary: 浮点精度 Double（默认）| Single
  group: ''
  block_parameter: BlockDataType
  type: string
  values: '"Double" | "Single"'
  default: '"Double"'
- name: P gain lookup method
  summary: 比例增益查找方法 Interpolation-Use End Values（默认）| Interpolation-Extrapolation | Use Input Nearest | Use Input Below |
    Use Input Above
  group: ''
  block_parameter: PGainLookUpMeth
  type: string
  values: '"Interpolation-Use End Values" | "Interpolation-Extrapolation" | "Use Input Nearest" | "Use Input Below" | "Input
    to block"'
  default: '"Use Input Above"'
- name: I gain lookup method
  summary: 积分增益查找方法 Interpolation-Use End Values（默认）| Interpolation-Extrapolation | Use Input Nearest | Use Input Below |
    Use Input Above
  group: ''
  block_parameter: IGainLookUpMeth
  type: string
  values: '"Interpolation-Use End Values" | "Interpolation-Extrapolation" | "Use Input Nearest" | "Use Input Below" | "Input
    to block"'
  default: '"Use Input Above"'
- name: D gain lookup method
  summary: 微分增益查找方法 Interpolation-Use End Values（默认）| Interpolation-Extrapolation | Use Input Nearest | Use Input Below |
    Use Input Above
  group: ''
  block_parameter: DGainLookUpMeth
  type: string
  values: '"Interpolation-Use End Values" | "Interpolation-Extrapolation" | "Use Input Nearest" | "Use Input Below" | "Input
    to block"'
  default: '"Use Input Above"'
- name: N gain lookup method
  summary: 微分滤波器增益查找方法 Interpolation-Use End Values（默认）| Interpolation-Extrapolation | Use Input Nearest | Use Input Below
    | Use Input Above
  group: ''
  block_parameter: NGainLookUpMeth
  type: string
  values: '"Interpolation-Use End Values" | "Interpolation-Extrapolation" | "Use Input Nearest" | "Use Input Below" | "Input
    to block"'
  default: '"Use Input Above"'
- name: 发生溢出时饱和至最大值或最小值
  summary: 溢出操作方式 off（默认）| on
  group: ''
  block_parameter: DoSatur
  type: string
  values: '"off" | "on"'
- name: 锁定输出数据类型设置以防止被定点工具更改
  summary: 用于防止定点工具覆盖输出数据类型的选项 off（默认）| on
  group: ''
  block_parameter: LockScale
  type: string
  values: '"off" | "on"'
- name: 整数舍入模式
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: ''
  block_parameter: RndMeth
  type: character vector
  values: '"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
```

### **Controller type** — PID 控制器类型 `P`（默认）| `I` | `PI` | `PD` | `PDN` | `PID` | `PIDN`

指定系统中 PID 控制器的类型。控制器类型指示控制器中存在哪些作用。以下控制器类型可用：

- `P` — 仅比例
- `I` — 仅积分
- `PI` — 比例和积分
- `PD` — 比例和微分
- `PDN` — 比例和带微分滤波器的微分
- `PID` — 比例、积分和微分
- `PIDN` — 比例、积分和带微分滤波器的微分

当您使用整定后的参数值更新 PID Controller 模块或自定义 PID 控制器时，请确保控制器类型匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`ControllerType` |
| **类型**：string |
| **值**：`"P"` | `"I"` | `"PI"` | `"PD"` | `"PDN"` | `"PID"` | `"PIDN"` |
| **默认值**：`"PID"` |

### **Breakpoints saved in gain array** — 读取保存在增益数组中的断点 `off`（默认）| `on`

当增益数组还包含断点数据时，启用此选项。通常，当您使用 PID Gain Store and Update 模块存储 PID 增益并启用 **Save breakpoints in gain array** 时，会获得此类数组。

#### 编程使用

|  |
| --- |
| **模块参数**：`BPsInGainArray` |
| **类型**：string |
| **Value** `"off"` | `"on"` |
| **默认值**：`"off"` |

### **Breakpoints** — 增益调度断点 `[1 2 3]`（默认）| 向量

指定增益调度断点数据。

#### 依赖关系

要启用此参数，请禁用 **Breakpoints saved in gain
array**。

#### 编程使用

|  |
| --- |
| **模块参数：** `GainArrayBreakpoints` |
| **类型：** string |
| **值：** 至少包含两个元素的向量 |
| **默认值：** `"[1 2 3]"` |

### **Use external signal** — 从输入端口指定断点 `off`（默认）| `on`

从模块输入端口指定断点。

#### 依赖关系

要启用此参数，请禁用 **Breakpoints saved in gain
array**。

#### 编程使用

|  |
| --- |
| **模块参数：** `UseExternalBreakpoints` |
| **类型：** string |
| **值** `"off"` | `"on"` |
| **默认值：** `"off"` |

### **Method of obtaining gains** — 获取增益的方法 `Data store memory`（默认）| `Goto/from` | `Input to block`

指定获取增益的方法。

- `Data store memory` — 使用 Data
  Store Memory 模块读取增益。为此，请使用与
  PID Gains Store and Update 模块创建的 Data Store
  Memory 模块中数据存储名称相同的名称。
- `Goto/from` — 使用 From
  模块标签读取增益。要指定标签名称，请为每个增益使用
  **Parameter Name** 参数。您可以指定由
  PID Gain Scheduler 模块创建的这些 Goto 标签来读取和查找
  增益。
- `Input to block` — 使用 **PID
  Gains** 输入端口。您可以将
  PID Gain Scheduler 模块的输出信号馈送到此输入。

#### 编程使用

|  |
| --- |
| **模块参数：** `GainSourceMethod` |
| **类型：** string |
| **值：** `"Data store memory"` | `"Goto/from"` | `"Input to block"` |
| **默认值：** `"Data store memory"` |

### **P Gain Parameter Name** — 比例增益数据名称 `PGain`（默认）| string

指定此模块从中读取比例增益参数数据的数据存储或 goto 标签的名称。

#### 依赖关系

要启用此参数，请设置

- **Controller type** 为具有比例作用的控制器类型。
- **Method of obtaining gains** 为
  `Data store memory` 或
  `Goto/from`。

#### 编程使用

|  |
| --- |
| **模块参数：** `StoreGainsPParamName` |
| **类型：** string |
| **默认值：** `"PGain"` |

### **I Gain Parameter Name** — 积分增益数据名称 `IGain`（默认）| string

指定此模块从中读取积分增益参数数据的数据存储或 goto 标签的名称。

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

### **D Gain Parameter Name** — 微分增益数据名称 `DGain`（默认）| string

指定此模块从中读取微分增益参数数据的数据存储或 goto 标签的名称。

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

### **N Gain Parameter Name** — 滤波器增益数据名称 `NGain`（默认）| string

指定此模块从中读取滤波器增益参数数据的数据存储或 goto 标签的名称。

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

### **Data type** — 浮点精度 `Double`（默认）| `Single`

根据仿真环境或硬件要求指定浮点精度。

#### 编程使用

|  |
| --- |
| **模块参数**：`BlockDataType` |
| **类型**：string |
| **值**：`"Double"` | `"Single"` |
| **默认值**：`"Double"` |

### **P gain lookup method** — 比例增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有比例作用的控制器类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`PGainLookUpMeth` |
| **类型**：string |
| **值**：`"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **默认值**：`"Use Input Above"` |

### **I gain lookup method** — 积分增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有积分作用的控制器类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`IGainLookUpMeth` |
| **类型**：string |
| **值**：`"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **默认值**：`"Use Input Above"` |

### **D gain lookup method** — 微分增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有微分作用的控制器类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`DGainLookUpMeth` |
| **类型**：string |
| **值**：`"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **默认值**：`"Use Input Above"` |

### **N gain lookup method** — 微分滤波器增益查找方法 `Interpolation-Use End Values`（默认）| `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

该模块通过将您选择的查找方法应用于断点数据（**Breakpoints**）和表数据（**PID Gains**）的输入向量来计算输出。有关详细信息，请参阅 How the Block Generates Output。

#### 依赖关系

要启用此端口，请将 **Controller type** 设置为具有滤波微分的控制器类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`NGainLookUpMeth` |
| **类型**：string |
| **值**：`"Interpolation-Use End Values"` | `"Interpolation-Extrapolation"` | `"Use Input Nearest"` | `"Use Input Below"` | `"Input to block"` |
| **默认值**：`"Use Input Above"` |

### **发生溢出时饱和至最大值或最小值** — 溢出操作方式 `off`（默认）| `on`

选中此复选框时，溢出将饱和至该数据类型所能表示的最大值或最小值。否则，溢出将回绕。

选中此复选框时，饱和将应用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

|  |
| --- |
| **模块参数：** `DoSatur` |
| **类型：** string |
| **值：** `"off"` | `"on"` |
| **默认：** `"off"` |

### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** string |
| **值：** `"off"` | `"on"` |
| **默认：** `"off"` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **值：** `"Ceiling"` | `"Convergent"` | `"Floor"` | `"Nearest"` | `"Round"` | `"Simplest"` | `"Zero"` |
| **默认：** `"Floor"` |
## 所属库

Simulink Control Design / Autotuning

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

基于查找表的 PID 数组增益调度

PID Gain Scheduler 模块允许您从增益数组、对应的断点数据以及调度变量中查找系统当前状态的 PID 增益。该模块使用查找表将特定 PID 增益与对应的断点值关联起来，并根据当前工作点（调度变量）提供动态调整的 PID 增益。您可以将这些增益用作模型中 PID 控制器或其他相关模块的输入。查找方法可以使用插值、外插或输入增益的原始值。

通常，调整增益调度控制器是一个复杂的过程。它要求您在每个工作点运行多次仿真以进行整定，并提供在该工作点存储 PID 增益的逻辑。使用此模块以及 Change Operating Points 和 PID Gains Store and Update 模块，可帮助您在单次仿真中实现跨运行范围自动整定增益调度 PID 控制器的简化工作流。为此，请使用此工作流。

1. 使用 Change Operating Points 模块在仿真期间切换预定义或快照工作点数据。
2. 使用 Closed-Loop PID Autotuner 在工作点执行自动整定。
3. 使用 PID Gains Store and Update 模块将对应于工作点的 PID 增益存储在数组中。
4. 使用 PID Gain Scheduler 模块从数组执行基于查找表的增益调度。

从高层次来看，您可以使用这些模块实现增益调度工作流，如下图所示。

增益调度系统图，包含 Closed-Loop PID Autotuner、PID Controller、Change Operating Points、Gain Scheduler 和 PID Gains Store and Update 模块。
