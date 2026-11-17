---
type: simulink-block
title: 'Simulink Function'
family: 'simevents'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: ''
documentation_page: 'simulinkfunction'
documentation_source_path: 'slref/simulinkfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulink Function

## 端口
```yaml
ports:
- name: In
  summary: 子系统的信号输入 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image | struct
- name: ArgIn
  summary: 子系统的参数输入 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image | struct
- name: Out
  summary: 子系统的信号输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image | struct
- name: ArgOut
  summary: 子系统的参数输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image | struct
```

### 输入

### **In** — 子系统的信号输入 标量 | 向量 | 矩阵

在子系统模块中放置一个 Inport 模块会为该模块添加一个外部输入端口。端口标签与 Inport 模块的名称匹配。

使用 Inport 模块从局部环境接收信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

### **ArgIn** — 子系统的参数输入 标量 | 向量 | 矩阵

子系统中的 Argument Inport 模块提供一个与输入参数对应的输入端口。该端口不会显示在子系统模块上。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`
### 输出

### **Out** — 子系统的信号输出 标量 | 向量 | 矩阵

在子系统模块中放置一个 Outport 模块会从该模块添加一个输出端口。子系统模块上的端口标签是 Outport 模块的名称。

使用 Outport 模块向局部环境发送信号。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

### **ArgOut** — 子系统的参数输出 标量 | 向量 | 矩阵

子系统中的 Argument Outport 模块提供一个与输出参数对应的输出端口。该端口不会显示在子系统模块上。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`
## 参数
```yaml
parameters:
- name: Show port labels
  summary: 端口标签的显示选项 FromPortIcon（默认）| FromPortBlockName | SignalName | none
  group: 主要
  block_parameter: ShowPortLabels
  values: '''FromPortIcon''（默认）| ''FromPortBlockName'' | ''SignalName'' | ''none'''
- name: Read/Write permissions
  summary: 对子系统内容的访问级别 ReadWrite（默认）| ReadOnly | NoReadOrWrite
  group: 主要
  block_parameter: Permissions
  values: '''ReadWrite''（默认）| ''ReadOnly'' | ''NoReadOrWrite'''
- name: Name of error callback function
  summary: 发生错误时要调用的函数名称 无默认值
  group: 主要
  block_parameter: ErrorFcn
  values: '''''（默认）| 带引号的函数名称'
- name: Permit hierarchical resolution
  summary: 工作区变量名称的解析方式 All（默认）| ExplicitOnly | None
  group: 主要
  block_parameter: PermitHierarchicalResolution
  values: '''All''（默认）| ''ExplicitOnly'' | ''None'''
```

### 主要

### **Show port labels** — 端口标签的显示选项 `FromPortIcon`（默认）| `FromPortBlockName` | `SignalName` | `none`

选择如何在 Subsystem 模块图标上显示端口标签。

- `none` — 不显示端口标签。
- `FromPortIcon` — 如果对应端口图标显示信号名称，则在 Subsystem 模块上显示该信号名称。否则，显示端口模块名称，或者如果模块名称为默认名称，则显示端口编号。
- `FromPortBlockName` — 在 Subsystem 模块上显示对应端口模块的名称。
- `SignalName` — 如果连接到该端口的信号已命名，则在 Subsystem 模块上显示该信号的名称。否则，显示对应端口模块的名称。

有关在 Subsystem 模块上编辑端口标签的信息，请参阅 Edit Port Labels on Subsystem Blocks。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ShowPortLabels` |
| **值**：| `'FromPortIcon'`（默认）| `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **Read/Write permissions** — 对子系统内容的访问级别 `ReadWrite`（默认）| `ReadOnly` | `NoReadOrWrite`

控制用户对子系统内容的访问。

- `ReadWrite` — 允许打开和修改子系统内容。
- `ReadOnly` — 允许打开子系统但不允许修改。如果子系统位于模块库中，您可以创建并打开指向该子系统的链接，可以制作和修改该子系统的本地副本，但不能更改权限或修改原始库实例的内容。
- `NoReadOrWrite` — 禁止打开或修改子系统。如果子系统位于库中，您可以在模型中创建指向该子系统的链接，但不能打开、修改、更改权限或创建该子系统的本地副本。

如果您尝试查看 **Read/Write permissions** 参数设置为 `NoReadOrWrite` 的子系统的内容，您不会收到任何响应。例如，当双击此类子系统时，软件不会打开该子系统，也不会显示任何消息。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Permissions` |
| **值**：| `'ReadWrite'`（默认）| `'ReadOnly'` | `'NoReadOrWrite'` |

### **Name of error callback function** — 发生错误时要调用的函数名称 无默认值

输入一个函数的名称，当软件执行子系统期间发生错误时将调用该函数。

软件向该函数传递两个参数：子系统的句柄和一个指定错误类型的字符向量。如果未指定函数，则当执行子系统导致错误时，软件会显示一条通用错误消息。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `ErrorFcn` |
| **值**：| `''`（默认）| 带引号的函数名称 |
| **Data Types:** | `char` | `string` |

### **Permit hierarchical resolution** — 工作区变量名称的解析方式 `All`（默认）| `ExplicitOnly` | `None`

选择是否解析此子系统引用的工作区变量名称。

有关详细信息，请参阅 Symbol Resolution 和 Symbol Resolution Process。

- `All` — 解析此子系统使用的所有工作区变量名称，包括用于指定模块参数值和 Simulink 数据对象（例如 `Simulink.Signal` 对象）的名称。
- `ExplicitOnly` — 仅解析用于指定模块参数值、数据存储内存（不存在对应模块时）、信号以及标记为“must resolve”的状态的工作区变量名称。
- `None` — 不解析任何工作区变量名称。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `PermitHierarchicalResolution` |
| **值**：| `'All'`（默认）| `'ExplicitOnly'` | `'None'` |

**注意**

要配置 Simulink Function 模块的作用域可见性和同步性，请打开位于 Simulink Function 模块内部的 Trigger 模块的模块参数。
## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `imagea` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际代码生成支持取决于模块实现。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

## 版本历史

**在 R2014b 中引入**

### R2024a：在掩码或模型工作区中定义 Simulink Function 模块的变体控制变量

从 R2024a 开始，您可以在掩码或模型工作区中定义具有更新图激活时间的 Simulink Function 模块的变体控制变量。

### R2023b：当作用域为不同端口时支持非唯一函数名称

如果作用域为不同端口，则模型根级别的 Simulink 函数的函数名称不必唯一。

### R2022b：在引用模型中高亮显示相关的 Function Caller 模块

从 R2022b 开始，当您选择其相关 Function Caller 模块位于引用模型中的 Simulink Function 模块时，Function Caller 模块和引用模型的 Model 模块都会被高亮显示。

### R2022b：指定异步函数执行

从 R2022b 开始，您可以通过在 Simulink Function 模块内部的 Trigger 模块中以及在 Function Caller 模块中选择新的 **Execute function call asynchronously** 参数，将 Simulink 函数指定为异步执行。

### R2022a：端口作用域 Simulink Function 模块

R2022a 新增了 Simulink Function 模块的端口作用域可见性选项。要创建端口作用域 Simulink Function 模块，请将 Simulink Function 模块内部 Trigger 模块的 **Function visibility** 参数设置为 `port`，并在 **Scope to port** 字段中输入端口名称。使用端口作用域 Simulink Function 模块来实现通过 Function Element 模块创建的导出函数端口所调用的函数。请参阅 Model Client and Server Components Using Function Ports。

## 描述

使用 Simulink 模块定义函数

Simulink Function 模块是一个预配置的 Subsystem 模块，用于支持使用 Simulink® 模块实现函数。要使用 Simulink Function 模块定义和调用函数：

- 指定函数原型，其中包括函数名称以及输入和输出参数，例如 `y = f(u)`。
- 使用 Simulink 库中的模块实现函数行为。
- 将您的 Simulink Function 模块配置为可在模型层次结构中的任何位置调用和重用。

Simulink Function 模块及其子系统内部视图。

当函数被调用时，调用方通过输入参数向函数发送数据，函数根据所实现的行为执行，然后通过输出参数从函数接收数据。

有关详细信息，请参阅 Simulink Functions Overview。

### 指定函数原型

函数原型与函数的实现是分开的。它指定输入和输出参数，以及应如何从模型层次结构中的其他模块调用该函数。函数原型中指定的每个输入或输出参数分别由 Argument Inport 模块或 Argument Outport 模块表示。您可以通过双击模块上显示的文本来编辑函数原型。

### 实现函数行为

要实现函数的所需行为，请在子系统内添加任何必要的 Simulink 模块。除了 Argument Inport 和 Argument Outport 模块外，Simulink Function 模块还可以使用 Inport 和 Outport 模块来输入和输出数据。

有关示例，请参阅 Monitor Ink Status on Shared Printer Using Simulink Functions。

### 配置 Simulink Function 模块

要配置 Simulink Function 模块，请打开位于 Simulink Function 模块内部的 Trigger 模块的模块参数。

- **Function name** — 指定 Simulink Function 模块的函数名称。
- **Function visibility** — 选择函数的作用域可见性。

  如果 **Function visibility** 设置为 `port`，您还可以指定以下参数：

  - **Execute function call asynchronously** — 指定函数是同步执行还是异步执行。
  - **Scope to port** — 指定导出函数端口的名称。

### 调用 Simulink 函数

您可以使用函数调用方和函数原型来调用和执行您的函数。在 Simulink Function 模块中定义的函数可以从 Function Caller 模块、Chart (Stateflow)、MATLAB Function 模块、MATLAB System 模块或 S-Function 模块中调用。

有关详细信息，请参阅 Call a Simulink Function from a Model。

### 模型注意事项

使用 Simulink Function 模块时，请考虑您的模型是否需要在函数调用之间保持状态，或者是否需要连续采样时间。

- 函数调用之间的状态保持 — 如果 Simulink Function 模块包含任何带状态的模块（例如 Unit Delay 或 Memory 模块），则其状态值在函数调用之间是持久的。如果对该函数有多次调用，则来自不同调用方的调用之间的状态值也是持久的。
- 无法继承连续采样时间 — Simulink Function 模块无法继承连续采样时间。

### 使用 Simulink Function 模块进行代码生成

如果您拥有 Simulink Coder™ 或 Embedded Coder®，您可以从包含 Simulink 函数的模型生成代码。有关详细信息，请参阅 Simulink Function Blocks and Code Generation (Embedded Coder) 和 Configure Entry-Point Function Interfaces for Simulink Function and Function Caller Blocks (Embedded Coder)。
