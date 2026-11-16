---
type: simulink-block
title: 'Function Caller'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'functioncaller'
documentation_source_path: 'slref/functioncaller.html'
language: zh-CN
chinese_source: official
---

# Function Caller

## 端口

### 输入

### **Input argument** — 输入参量的输入信号 标量 | 向量 | 矩阵

发送给函数的输入参量的输入信号。

函数原型决定 Function Caller 模块上显示的输入端口的数量和名称。将信号线连接到输入端口，以便通过函数输入参量将数据发送给函数。

例如，`y = myfunction(u)` 将在 Function Caller 模块上创建一个输入端口 (`u`)。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Output argument** — 输出参量的输出信号或消息 标量 | 向量 | 矩阵 | 消息

函数返回的输出参量的输出信号。

函数原型决定 Function Caller 模块上显示的输出端口的数量和名称。将信号线或消息线连接到输出端口，以便通过函数输出参量接收函数返回的数据。当您选中**异步执行函数调用**复选框时，Function Caller 模块输出消息。

例如，`y = myfunction(u)` 在 Function Caller 模块上创建一个输出端口 (`y`)。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **函数原型** — 指定函数原型 `y=f(u)` (默认) | 字符向量 | 字符串

指定 Function Caller 模块和 Simulink 函数之间的函数原型。

**注意**

要调用在 Simulink Function 模块中定义的函数，需要满足以下条件：

- 函数调用参量名称必须与函数参量匹配。
- 函数名称、输入参量和输出参量必须是有效的 MATLAB® 标识符。

#### 编程用法

|  |
| --- |
| **模块参数**：`FunctionPrototype` |
| **类型：**字符向量 |
| **值：**`'y=f(u)'` | *`function prototype`* |
| **默认值：**`'y=f(u)'` |

### **函数名称** — 限定函数名称 `f` (默认) | 字符向量 | 字符串

限定函数名称，指定为字符向量或字符串。

函数名称显示在模块图标上。您可以通过点击模块图标上的参数值并输入新值来编辑名称。

**注意**

此参数与 Function Caller 模块的**函数原型**参数自动同步。

有关通过限定解析函数的详细信息，请参阅Scoped Simulink Function Blocks in Models和Scoped Simulink Function Blocks in Subsystems。

#### 编程用法

|  |
| --- |
| **模块参数**：`ScopedFunctionName` |
| **类型：**字符向量 |
| **值**：`'f'` | `'Client.f'` | *`function name`* |
| **默认值**：`'f'` |

### **输入参量设定** — 指定输入参量的数据类型、维数和复/实性 `<Enter example>` (默认) | MATLAB 表达式

指定以逗号分隔的 MATLAB 表达式列表，表达式中包含每个输入参量的数据类型、维度和复/实性（实数或虚数）。有关示例，请参阅 Argument Specification for Simulink Function Blocks。

**注意**

此设定必须与使用 Argument Inport 模块的**数据类型**参数指定的 Simulink Function 模块的数据类型匹配。

#### 编程用法

|  |
| --- |
| **模块参数**：`InputArgumentSpecifications` |
| **类型：**字符向量 |
| **值：**`''` | *`MATLAB expression`* |
| **默认值**：`''` |

### **输出参量设定** — 指定输出参量的数据类型、维数和复/实性 `<Enter example>` (默认) | MATLAB 表达式

指定以逗号分隔的 MATLAB 表达式列表，表达式中包含每个输出参量的数据类型、维度和复/实性（实数或虚数）。有关示例，请参阅 Argument Specification for Simulink Function Blocks。

**注意**

此设定必须与使用 Argument Outport 模块的**数据类型**参数指定的 Simulink Function 模块的数据类型匹配。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputArgumentSpecifications` |
| **类型：**字符向量 |
| **值：**`''` | *`MATLAB expression`* |
| **默认值**：`''` |

### **采样时间** — 函数调用之间的时间间隔 `-1` (默认) | 标量 | 向量

指定在对 Simulink 函数的各次调用之间的时间间隔。

默认情况下，模块根据模型中的模块上下文继承其采样时间。要设置不同采样时间，请使用指定采样时间中的表提供的采样时间格式输入值。

如果 Function Caller 模块有任何输入，则它是非源模块，您必须将采样时间设置为 `-1`。

#### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符串 | 字符向量 |
| **值**：标量 | 向量 | *`sample time`* |
| **默认值**：`'-1'` |

### **异步执行函数调用** — 异步执行函数调用的选项 `off` (默认) | `on`

指定是否异步执行与此 Function Caller 模块关联的 Simulink Function 模块。

- 选择**异步执行函数调用**以启用异步执行。

  *异步执行*是指当调用方调用函数时，该函数根据优先顺序执行并将输出参量返回给调用方。该函数根据在调度编辑器中定义的顺序执行，然后将输出参量返回到调用方。该模块使用消息输出端口输出这些参量。

  - 如果只有一个函数输出参量，该输出参量将成为消息有效负载。
  - 如果有多个函数输出参量，Function Caller 模块将这些输出参量捆绑成一个结构体，该结构体为消息有效负载。

  在即时模式下将消息输出端口连接到一个 Message Triggered Subsystem 模块。Message Triggered Subsystem 模块充当函数的回调。
- 清除**异步执行函数调用**以启用同步执行。

  *同步执行*是指当调用方调用函数时，该函数立即运行并将输出参量返回给调用方。

#### 编程用法

|  |
| --- |
| **模块参数**：`AsynchronousCaller` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

要为使用 Function Caller 模块异步调用和执行 Simulink 函数的模型生成代码，请执行以下操作：

- 在 Function Caller 模块参数中选择**异步执行函数调用**参数。
- 在配置参数中设置**系统目标文件**参数。有关详细信息，请参阅配置系统目标文件 (Embedded Coder)。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2014b 中推出**

### R2025a: 从 Function Caller 模块编辑限定函数名称

从 R2025a 开始，Function Caller 模块支持使用**函数名称**参数编辑限定函数名称。使用以下方法之一。

- 使用 `set_param` 设置 `ScopedFunctionName` 模块参数。
- 点击模块图标上的参数值并输入新值。

  Function Caller block with qualified function name selected on the block icon. User is typing a new value, client.f1.

### R2022b: 突出显示引用模型中的相关 Simulink Function 模块

从 R2022b 开始，当您选择其相关的 Function Caller 模块位于引用模型中的 Simulink Function 模块时，引用模型的 Simulink Function 模块和 Model 模块都会突出显示。

### R2022b: 指定异步函数执行

从 R2022b 开始，您可以通过在 Simulink Function 模块内的 Trigger 模块中和 Function Caller 模块中选择新的**异步执行函数调用**参数，指定要异步执行的 Simulink 函数。

## 描述

调用 Simulink 函数

Function Caller 模块调用并执行 Simulink® 函数。Simulink 函数指定函数原型，其中包括函数名称以及输入和输出参量。例如，当 Function Caller 模块调用原型为 `y = f(u)` 的函数时，Function Caller 模块的输入是 Simulink 函数的输入参量 `u`，而 Simulink 函数的输出参量 `y` 是 Function Caller 模块的输出。

在此示例中，Function Caller 模块配置为调用和执行在 Simulink Function 模块中定义的 Simulink 函数 `y = timestwo(x)`。为了测试函数调用，Sine Wave 模块连接到输入端口 `x` 以提供输入数据，Scope 模块连接到输出端口 `y` 以查看输出结果。

A Sine Wave block is the input to the Function Caller block which sends output to a Scope block.

您可以调用通过以下方式定义的 Simulink 函数：Simulink Function 模块、作为导出函数的 Stateflow® Chart (Stateflow)，或 S-Function 模块。有关定义 Simulink 函数的详细信息，请参阅在模型中定义 Simulink 函数。

有关详细信息，请参阅 Simulink Functions Overview。

**提示**

您可以使用 Function Caller 模块来调用模型层次结构之外的函数。

有关详细信息，请参阅Simulink Function Blocks in Referenced Models。

### 使用 Simulink Function 和 Function Caller 模块的代码生成

如果您有 Simulink Coder™ 或 Embedded Coder®，您可以从包含 Simulink 函数的模型中生成代码。有关详细信息，请参阅 Simulink Function Blocks and Code Generation (Embedded Coder)和Configure Entry-Point Function Interfaces for Simulink Function and Function Caller Blocks (Embedded Coder)。
