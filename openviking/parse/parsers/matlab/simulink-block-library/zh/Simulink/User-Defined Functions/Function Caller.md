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
chinese_source: worker-translation
---

# Function Caller

## 端口

### 输入

### **Input argument** — 输入参数的输入信号 标量 | 向量 | 矩阵

发送给函数的输入参数的输入信号。

函数原型决定了 Function Caller 模块上出现的输入端口数量和名称。将信号线连接到输入端口，以通过函数输入参数向函数发送数据。

例如，`y = myfunction(u)` 在 Function Caller 模块上创建一个输入端口（`u`）。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Output argument** — 输出参数的输出信号或消息 标量 | 向量 | 矩阵 | 消息

函数返回的输出参数的输出信号。

函数原型决定了 Function Caller 模块上出现的输出端口数量和名称。将信号线或消息线连接到输出端口，以通过函数输出参数从函数接收数据。当您选中 **Execute function call asynchronously** 复选框时，Function Caller 模块输出消息。

例如，`y = myfunction(u)` 在 Function Caller 模块上创建一个输出端口（`y`）。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Function prototype** — 指定函数原型 `y=f(u)`（默认）| 字符向量 | 字符串

指定 Function Caller 模块与 Simulink 函数之间的函数原型。

**注意**

要调用 Simulink Function 模块中定义的函数：

- 函数调用参数名称必须与函数参数匹配。
- 函数名称、输入参数和输出参数必须是有效的 MATLAB® 标识符。

#### 编程使用

|  |
| --- |
| **模块参数**：`FunctionPrototype` |
| **类型**：character vector |
| **值**：`'y=f(u)'` | *`function prototype`* |
| **默认值**：`'y=f(u)'` |

### **Function name** — 限定函数名称 `f`（默认）| 字符向量 | 字符串

限定函数名称，指定为字符向量或字符串。

函数名称显示在模块图标上。您可以通过点击模块图标上的参数值并输入新值来编辑名称。

**注意**

此参数与 Function Caller 模块的 **Function prototype** 参数自动同步。

有关通过限定解析函数的详细信息，请参阅 Scoped Simulink Function Blocks in Models 和 Scoped Simulink Function Blocks in Subsystems。

#### 编程使用

|  |
| --- |
| **模块参数**：`ScopedFunctionName` |
| **类型**：character vector |
| **值**：`'f'` | `'Client.f'` | *`function name`* |
| **默认值**：`'f'` |

### **Input argument specifications** — 指定输入参数数据类型、维度和复数性 `<Enter example>`（默认）| MATLAB 表达式

指定一个以逗号分隔的 MATLAB 表达式列表，这些表达式为每个输入参数组合了数据类型、维度和复数性（实数或虚数）。有关示例，请参阅 Argument Specification for Simulink Function Blocks。

**注意**

此规范必须与 Argument Inport 模块的 **Data type** 参数指定的 Simulink Function 模块数据类型匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputArgumentSpecifications` |
| **类型**：character vector |
| **值**：`''` | *`MATLAB expression`* |
| **默认值**：`''` |

### **Output argument specifications** — 指定输出参数数据类型、维度和复数性 `<Enter example>`（默认）| MATLAB 表达式

指定一个以逗号分隔的 MATLAB 表达式列表，这些表达式为每个输出参数组合了数据类型、维度和复数性（实数或虚数）。有关示例，请参阅 Argument Specification for Simulink Function Blocks。

**注意**

此规范必须与 Argument Outport 模块的 **Data type** 参数指定的 Simulink Function 模块数据类型匹配。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutputArgumentSpecifications` |
| **类型**：character vector |
| **值**：`''` | *`MATLAB expression`* |
| **默认值**：`''` |

### **Sample time** — 函数调用之间的时间间隔 `-1`（默认）| 标量 | 向量

指定调用 Simulink 函数之间的时间间隔。

默认情况下，模块根据模型中模块的上下文继承其采样时间。要设置不同的采样时间，请使用 Specify Sample Time 中表格的采样时间格式输入一个值。

如果 Function Caller 模块有任何输入，则它是非源模块，您必须将采样时间设置为 `-1`。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：string | character vector |
| **值**：scalar | vector | *`sample time`* |
| **默认值**：`'-1'` |

### **Execute function call asynchronously** — 异步执行函数调用的选项 `off`（默认）| `on`

指定是否异步执行与此 Function Caller 模块关联的 Simulink Function 模块。

- 选中 **Execute function call asynchronously** 以启用异步执行。

  *异步执行*是指调用方调用函数时，函数根据优先级顺序执行，并将输出参数返回给调用方。函数根据 Schedule Editor 中定义的顺序执行，然后将输出参数返回给调用方。模块使用消息输出端口输出这些参数。

  - 如果只有一个函数输出参数，则该输出参数成为消息负载。
  - 如果有多个函数输出参数，则 Function Caller 模块将输出参数捆绑为一个结构体，该结构体成为消息负载。

  将消息输出端口连接到立即模式的 Message Triggered Subsystem 模块。Message Triggered Subsystem 模块充当函数的回调。
- 清除 **Execute function call asynchronously** 以启用同步执行。

  *同步执行*是指调用方调用函数时，函数立即运行，并将输出参数返回给调用方。

#### 编程使用

|  |
| --- |
| **模块参数**：`AsynchronousCaller` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为使用 Function Caller 模块异步调用和执行 Simulink 函数的模型生成代码：

- 在 Function Caller 模块参数中选中 **Execute function call asynchronously** 参数。
- 在配置参数中设置 **System target file** 参数。有关详细信息，请参阅 Configure a System Target File (Embedded Coder)。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2014b 中引入**

### R2025a：从 Function Caller 模块编辑限定函数名称

从 R2025a 开始，Function Caller 模块支持使用 **Function name** 参数编辑限定函数名称。使用以下方法之一。

- 使用 `set_param` 设置 `ScopedFunctionName` 模块参数。
- 点击模块图标上的参数值并输入新值。

  模块图标上选中了限定函数名称的 Function Caller 模块。用户正在输入新值 client.f1。

### R2022b：在引用模型中高亮显示相关的 Simulink Function 模块

从 R2022b 开始，当您选择其相关 Simulink Function 模块位于引用模型中的 Function Caller 模块时，Simulink Function 模块和引用模型的 Model 模块都会被高亮显示。

### R2022b：指定异步函数执行

从 R2022b 开始，您可以通过在 Simulink Function 模块内的 Trigger 模块中和 Function Caller 模块中选中新的 **Execute function call asynchronously** 参数，指定 Simulink 函数异步执行。

## 描述

调用 Simulink 函数

Function Caller 模块调用并执行 Simulink® 函数。Simulink 函数指定函数原型，其中包括函数名称以及输入和输出参数。例如，当 Function Caller 模块调用原型为 `y = f(u)` 的函数时，Function Caller 模块的输入是 Simulink 函数的输入参数 `u`，而 Simulink 函数的输出参数 `y` 是 Function Caller 模块的输出。

在此示例中，Function Caller 模块配置为调用并执行 Simulink Function 模块中定义的 Simulink 函数 `y = timestwo(x)`。为测试函数调用，Sine Wave 模块连接到输入端口 `x` 以提供输入数据，Scope 模块连接到输出端口 `y` 以查看输出结果。

Sine Wave 模块是 Function Caller 模块的输入，该模块将输出发送到 Scope 模块。

您可以调用 Simulink Function 模块中定义的 Simulink 函数、Stateflow® Chart（Stateflow）中作为导出函数定义的函数，或 S-Function 模块。有关定义 Simulink 函数的详细信息，请参阅 Define a Simulink Function in a Model。

有关详细信息，请参阅 Simulink Functions Overview。

**提示**

您可以使用 Function Caller 模块调用模型层次结构外部的函数。

有关详细信息，请参阅 Simulink Function Blocks in Referenced Models。

### 使用 Simulink Function 和 Function Caller 模块进行代码生成

如果您拥有 Simulink Coder™ 或 Embedded Coder®，可以从包含 Simulink 函数的模型生成代码。有关详细信息，请参阅 Simulink Function Blocks and Code Generation (Embedded Coder) 和 Configure Entry-Point Function Interfaces for Simulink Function and Function Caller Blocks (Embedded Coder)。
