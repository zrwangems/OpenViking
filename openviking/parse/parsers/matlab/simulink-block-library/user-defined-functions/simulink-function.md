---
type: simulink-block
title: 'Simulink Function'
family: user-defined-functions
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'simulinkfunction'
---

# Simulink Function

Define a function using Simulink blocks

## 中文

使用 Simulink 模块定义函数

### 所属库

Simulink / User-Defined Functions

### 描述

Simulink Function 模块是预配置为能够使用 Simulink® 模块实现函数的 Subsystem 模块。要使用 Simulink Function 模块定义和调用函数，请执行以下操作：

- 指定包含函数名称以及输入和输出参量的函数原型，例如 `y = f(u)`。
- 使用 Simulink 库中的模块实现函数行为。
- 配置您的 Simulink Function 模块，以便在模型层次结构中的任何位置调用和重用。

Simulink Function block with view of inside the subsystem.

调用函数时，调用方通过输入参量向函数发送数据，根据实现的行为执行函数，然后通过输出参量从函数接收数据。

有关详细信息，请参阅 Simulink Functions Overview。

#### 指定函数原型

函数原型与函数的实现是分离的。它指定输入和输出参量，以及应该如何从模型层次结构中的其他模块调用该函数。函数原型中指定的每个输入或输出参量分别由 Argument Inport 模块或 Argument Outport 模块表示。您可以通过双击模块上显示的文本来编辑函数原型。

#### 实现函数行为

要实现所需的函数行为，请在子系统中添加任何必需的 Simulink 模块。除了 Argument Inport 和 Argument Outport 模块之外，Simulink Function 模块还可以使用 Inport 和 Outport 模块来输入和输出数据。

有关示例，请参阅Monitor Ink Status on Shared Printer Using Simulink Functions。

#### 配置 Simulink Function 模块

要配置 Simulink Function 模块，请打开位于 Simulink Function 模块内的 Trigger 模块的模块参数。

- **函数名称** - 指定 Simulink Function 模块的函数名称。
- **函数可见性** - 选择函数的作用域可见性。

  如果**函数可见性**设置为 `port`，您还可以指定以下参数：

  - **异步执行函数调用** - 指定函数是同步执行还是异步执行。
  - **示波器到端口** - 指定导出函数端口的名称。

#### 调用 Simulink 函数

您可以使用函数调用方和函数原型来调用和执行您的函数。在 Simulink Function 模块中定义的函数可以从 Function Caller 模块、Chart (Stateflow)、MATLAB Function 模块、MATLAB System 模块或 S-Function 模块中调用。

有关详细信息，请参阅Call a Simulink Function from a Model。

#### 模型注意事项

当使用 Simulink Function 模块时，考虑您的模型是否需要在函数调用之间的状态持久性或连续采样时间。

- 函数调用之间的状态持久性 - 如果 Simulink Function 模块包含任何带状态的模块（例如 Unit Delay 或 Memory 模块），则其状态值在函数调用之间是持久性的。如果存在对该函数的多次调用，状态值在来自不同调用方的调用之间也是持久性的。
- 无法继承连续采样时间 - Simulink Function 模块无法继承连续采样时间。

#### 使用 Simulink Function 模块的代码生成

如果您有 Simulink Coder™ 或 Embedded Coder®，您可以从包含 Simulink 函数的模型中生成代码。有关详细信息，请参阅 Simulink Function Blocks and Code Generation (Embedded Coder)和Configure Entry-Point Function Interfaces for Simulink Function and Function Caller Blocks (Embedded Coder)。

### 端口

#### 输入

#### **In** — 子系统模块的信号输入 标量 | 向量 | 矩阵

在子系统模块中放置一个 Inport 模块会向该模块添加一个外部输入端口。端口标签与 Inport 模块的名称相匹配。

使用 Inport 模块可以从局部环境中接收信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

#### **ArgIn** — 子系统模块的参量输入 标量 | 向量 | 矩阵

子系统模块中的 Argument Inport 模块提供了对应于输入参量的输入端口。子系统模块上不显示端口。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`
#### 输出

#### **Out** — 子系统的信号输出 标量 | 向量 | 矩阵

在子系统模块中放置一个 Outport 模块会添加该模块的输出端口。子系统模块上的端口标签是 Outport 模块的名称。

使用 Outport 模块可以向局部环境发送信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

#### **ArgOut** — 子系统模块的参量输出 标量 | 向量 | 矩阵

子系统模块中的 Argument Outport 模块提供对应于输出参量的输出端口。子系统模块上不显示端口。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

### 参数

#### 常设

#### **显示端口标签** — 端口标签的显示选项 **FromPortIcon** (默认) | **FromPortBlockName** | **SignalName** | **无**

选择如何在 Subsystem 模块图标上显示端口标签。

- **无** - 不显示端口标签。
- **FromPortIcon** - 如果对应的端口图标显示了信号名称，则在 Subsystem 模块上显示信号名称。否则，如果模块名称是默认名称，则显示端口模块名称或端口号。
- **FromPortBlockName** - 在 Subsystem 模块上显示对应端口模块的名称。
- **SignalName** - 如果连接到端口的信号已命名，则会在 Subsystem 模块上显示信号的名称。否则，显示相应端口模块的名称。

有关 Subsystem 模块上的端口标签编辑，请参阅编辑子系统模块上的端口标签。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ShowPortLabels` |
| **值:** | `'FromPortIcon'` (默认) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

#### **读取/写入权限** — 子系统内容的访问级别 **ReadWrite** (默认) | **ReadOnly** | **NoReadOrWrite**

控制用户对子系统内容的访问。

- **ReadWrite** - 允许打开和修改子系统内容。
- **ReadOnly** - 允许打开但不允许修改子系统。如果子系统在模块库中，您可以创建和打开该子系统的链接，创建和修改子系统的本地副本，但不能更改权限或修改原始模块库实例的内容。
- **NoReadOrWrite** - 禁止打开或修改子系统。如果子系统在模块库中，您可以在模型中创建该子系统的链接，但不能打开、修改、更改权限或创建子系统的本地副本。

如果您尝试查看其**读取/写入权限**参数设置为 **NoReadOrWrite** 的子系统的内容，将不会收到响应。例如，当您双击此类子系统时，软件不会打开该子系统，并且不显示任何消息。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Permissions` |
| **值:** | `'ReadWrite'` (默认) | `'ReadOnly'` | `'NoReadOrWrite'` |

#### **错误回调函数的名称** — 发生错误时要调用的函数的名称 无默认值

输入软件执行子系统时，如果发生错误要调用的函数的名称。

该软件向函数传递两个参量：子系统的句柄以及指定错误类型的字符向量。如果未指定任何函数，当执行子系统导致错误时，软件将显示常规错误消息。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ErrorFcn` |
| **值:** | `''` (默认) | function name in quotes |
| **数据类型:** | `char` | `string` |

#### **允许层次解析** — 工作区变量名称解析 **全部** (默认) | **ExplicitOnly** | **无**

选择是否解析此子系统引用的工作区变量的名称。

有关详细信息，请参阅符号解析和符号解析过程。

- **全部** - 解析此子系统使用的所有工作区变量的名称，包括用来指定模块参数值和 Simulink 数据对象（例如，`Simulink.Signal` 对象）的工作区变量的名称。
- **ExplicitOnly** - 只解析用来指定模块参数值、数据存储内存（不存在模块）、信号以及标有“must resolve”状态的工作区变量的名称。
- **无** - 不解析任何工作区变量名称。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `PermitHierarchicalResolution` |
| **值:** | `'All'` (默认) | `'ExplicitOnly'` | `'None'` |

**注意**

要配置 Simulink Function 模块的作用域可见性和同步性，请打开位于 Simulink Function 模块内的 Trigger 模块的模块参数。

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `imagea` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `否` |
| **多维信号** | `是a` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 实际支持的数据类型或功能取决于模块实施。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际代码生成支持取决于模块实现。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型支持取决于模块实现。

### 版本历史记录

**在 R2014b 中推出**

#### R2024a: 在封装工作区或模型工作区中定义 Simulink Function 模块的变体控制项变量

从 R2024a 开始，您可以在封装或模型工作区中使用更新图激活时间定义 Simulink Function 模块的变体控制项变量。

#### R2023b: 当作用域限于不同端口时支持不唯一函数名称

如果作用域限于不同端口，则模型根级的 Simulink 函数的函数名称不必唯一。

#### R2022b: 突出显示引用模型中的相关 Function Caller 模块

从 R2022b 开始，当您选择其相关的 Function Caller 模块位于引用模型中的 Simulink Function 模块时，引用模型的 Function Caller 模块和 Model 模块都会突出显示。

#### R2022b: 指定异步函数执行

从 R2022b 开始，您可以通过在 Simulink Function 模块内的 Trigger 模块中和 Function Caller 模块中选择新的**异步执行函数调用**参数，指定要异步执行的 Simulink 函数。

#### R2022a: 作用域限于端口的 Simulink Function 模块

为 R2022a 添加了新的适用于 Simulink Function 模块的作用域限于端口的可见性选项。要创建一个作用域限于端口的 Simulink Function 模块，请将 Simulink Function 模块内 Trigger 模块的**函数可见性**参数设置为**端口**，并在**示波器到端口**字段中输入端口名称。使用作用域限于端口的 Simulink Function 模块实现通过导出由 Function Element 模块创建的函数端口调用的函数。请参阅Model Client and Server Components Using Function Ports。

## Libraries

Simulink / User-Defined Functions

## Description

A Simulink Function block is a Subsystem block preconfigured to enable implementation of a function using
Simulink® blocks. To define and call a function using a Simulink
Function block:

- Specify the function prototype, which includes the function name and input
  and output arguments, for example, `y = f(u)`.
- Implement function behavior using blocks from the Simulink library.
- Configure your Simulink Function block to be called and
  reused anywhere in the model hierarchy.

Simulink Function block with view of inside the subsystem.

When a function is called, the caller sends data through input arguments to the
function, executes the function based on the implemented behavior, and then receives
data back from the function through output arguments.

For more information, see Simulink Functions Overview.

### Specify Function Prototype

The function prototype is separate from the implementation of the function. It
specifies the input and output arguments and how the function should be called from
other blocks in the model hierarchy. Each input or output argument specified in the
function prototype is represented by an Argument Inport block or Argument Outport block,
respectively. You can edit the function prototype by double-clicking the text
displayed on the block.

### Implement Function Behavior

To implement the desired behavior of your function, add any necessary Simulink blocks inside the subsystem. In addition to Argument
Inport and Argument Outport blocks, a Simulink
Function block can use Inport and Outport blocks to input and output data.

For an example, see Monitor Ink Status on Shared Printer Using Simulink Functions.

### Configure Simulink Function Block

To configure a Simulink Function block, open the block parameters
of the Trigger block located inside of the
Simulink Function block.

- **Function name** –
  Specify the function name for the Simulink Function
  block.
- **Function visibility** – Select the scope visibility of
  the function.

  If **Function visibility** is set to
  `port`, you can also specify these
  parameters:

  - **Execute function call asynchronously** – Specify
    whether the function executes synchronously or
    asynchronously.
  - **Scope to port** – Specify the name of the
    exporting function port.

### Call a Simulink Function

You can use a function caller and the function prototype to call and execute your
function. A function defined in a Simulink Function block can be
called from a Function
Caller block, a Chart (Stateflow), a MATLAB Function block, a MATLAB System block, or an S-Function block.

For more information, see Call a Simulink Function from a Model.

### Model Considerations

When using a Simulink Function block, consider whether your model
requires persistence of states between functions calls or a continuous sample
time.

- Persistence of state between function calls – If a Simulink
  Function block contains any blocks with state (for example,
  Unit Delay or Memory blocks), then their
  state values are persistent between calls to the function. If there are
  multiple calls to that function, the state values are also persistent
  between the calls originating from different callers.
- Unable to inherit continuous sample time – A Simulink
  Function block cannot inherit a continuous sample time.

### Code Generation with Simulink Function Blocks

If you have Simulink
Coder™ or Embedded Coder®, you can generate code from models containing Simulink functions. For more information, see Simulink Function Blocks and Code Generation (Embedded Coder) and Configure Entry-Point Function Interfaces for Simulink Function and Function Caller Blocks (Embedded Coder).

## Ports

### Input

### **In** — Signal input to a subsystem block scalar | vector | matrix

Placing an Inport block in a subsystem block adds an
external input port to the block. The port label matches the name of the
Inport block.

Use Inport blocks to receive signals from the local
environment.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

### **ArgIn** — Argument input to a subsystem block scalar | vector | matrix

An Argument Inport block in a subsystem block provides
an input port corresponding to an input argument. A port is not
displayed on the subsystem block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`
### Output

### **Out** — Signal output from a subsystem scalar | vector | matrix

Placing an Outport block in a subsystem block adds an
output port from the block. The port label on the subsystem block is the
name of the Outport block.

Use Outport blocks to send signals to the local
environment.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

### **ArgOut** — Argument output from a subsystem block scalar | vector | matrix

An Argument Outport block in a subsystem block provides
an output port corresponding to an output argument. A port is not
displayed on the subsystem block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

## Parameters

### Main

### **Show port labels** — Display options for port labels `FromPortIcon` (default) | `FromPortBlockName` | `SignalName` | `none`

Select how to display port labels on the Subsystem block icon.

- `none` — Do not display port labels.
- `FromPortIcon` — If the corresponding port icon displays a signal name, display the signal name on the Subsystem block. Otherwise, display the port block name or the port number if the block name is a default name.
- `FromPortBlockName` — Display the name of the corresponding port block on the Subsystem block.
- `SignalName` — If the signal connected to the port is named, display the name of the signal on the Subsystem block. Otherwise, display the name of the corresponding port block.

For port label editing on Subsystem blocks, see Edit Port Labels on Subsystem Blocks.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowPortLabels` |
| **Values:** | `'FromPortIcon'` (default) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **Read/Write permissions** — Levels of access to contents of subsystem `ReadWrite` (default) | `ReadOnly` | `NoReadOrWrite`

Control user access to the contents of the subsystem.

- `ReadWrite` — Enable opening and modification of subsystem contents.
- `ReadOnly` — Enable opening but not modification of the subsystem. If the subsystem resides in a block library, you can create and open links to the subsystem and can make and modify local copies of the subsystem but cannot change the permissions or modify the contents of the original library instance.
- `NoReadOrWrite` — Disable opening or modification of subsystem. If the subsystem resides in a library, you can create links to the subsystem in a model but cannot open, modify, change permissions, or create local copies of the subsystem.

You do not receive a response if you attempt to view the contents of a subsystem whose **Read/Write permissions** parameter is set to `NoReadOrWrite`. For example, when double-clicking such a subsystem, the software does not open the subsystem and does not display any messages.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Permissions` |
| **Values:** | `'ReadWrite'` (default) | `'ReadOnly'` | `'NoReadOrWrite'` |

### **Name of error callback function** — Name of function to be called if error occurs no default

Enter the name of a function to be called if an error occurs while the software executes the
subsystem.

The software passes two arguments to the function: the handle of the subsystem and a
character vector that specifies the error type. If no function is specified, the software
displays a generic error message if executing the subsystem causes an error.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ErrorFcn` |
| **Values:** | `''` (default) | function name in quotes |
| **Data Types:** | `char` | `string` |

### **Permit hierarchical resolution** — Resolution for workspace variable names `All` (default) | `ExplicitOnly` | `None`

Select whether to resolve names of workspace variables referenced by this subsystem.

For more information, see Symbol Resolution and Symbol Resolution Process.

- `All` — Resolve all names of workspace variables used by this subsystem, including those used to specify block parameter values and Simulink data objects (for example, `Simulink.Signal` objects).
- `ExplicitOnly` — Resolve only names of workspace variables used to specify block parameter values, data store memory (where no block exists), signals, and states marked as “must resolve”.
- `None` — Do not resolve any workspace variable names.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PermitHierarchicalResolution` |
| **Values:** | `'All'` (default) | `'ExplicitOnly'` | `'None'` |

**Note**

To configure the scope visibility and synchronicity of a Simulink
Function block, open the block parameters of the Trigger block located inside of
the Simulink Function block.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `imagea` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced in R2014b**

### R2024a: Define variant control variables of a Simulink Function block in the mask or model workspace

Starting in R2024a, you can define the variant control variables of a
Simulink Function block with update diagram activation time in
the mask or model workspace.

### R2023b: Support nonunique function names when scoped to different ports

If scoped to different ports, function names of Simulink functions at the model
root level do not have to be unique.

### R2022b: Highlight related Function Caller blocks in referenced model

Starting in R2022b, when you select a Simulink Function block whose
related Function Caller block is in a referenced model, both the
Function Caller block and the Model block of the
referenced model are highlighted.

### R2022b: Specify asynchronous function execution

Starting in R2022b, you can specify a Simulink function to be executed asynchronously by selecting the new
**Execute function call asynchronously** parameter in the
Trigger block inside of the Simulink Function
block and in the Function Caller block.

### R2022a: Port-scoped Simulink Function blocks

A new port-scoped visibility option for the Simulink Function block
is added for R2022a. To create a port-scoped Simulink Function block,
set the **Function visibility** parameter of the Trigger block inside the
Simulink Function block to `port` and
enter the port name in the **Scope to port** field. Use
port-scoped Simulink Function blocks to implement functions called
through exporting function ports created by Function Element blocks.
See Model Client and Server Components Using Function Ports.
