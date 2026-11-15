---
type: simulink-block
title: 'C Caller'
family: user-defined-functions
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'ccaller'
---

# C Caller

Integrate C code in Simulink

## 中文

在 Simulink 中集成 C 代码

### 所属库

Simulink / User-Defined Functions

### 描述

C Caller 模块将您的外部 C 代码集成到 Simulink® 中。此模块导入并列出您的外部 C 代码中的函数，并使您能够选择已解析的 C 函数以集成到您的 Simulink 模型中。C Caller 模块独立支持代码生成。对于更复杂的模型，代码生成取决于您的 Simulink 模型的能力。

要使用 C Caller 模块，请使用**配置参数**下的**仿真目标**定义您的源代码和任何支持文件。然后，使用**库浏览器** > **Simulink** > **用户定义函数**将 C Caller 模块置于 Simulink 画布上。要更改定义的源代码文件及其依赖关系，请通过点击模块对话框中的 Configure custom code settings button. 转至**配置参数**中的**仿真目标**选项卡。在更改源代码或任何依赖关系后，请通过点击模块对话框上的 Refresh custom code button. 刷新函数列表。要浏览源代码中的函数定义，请使用 Go to function button. 图标访问您的源文件。

您可以使用 `addGlobalArg` 函数将自定义代码中的全局变量作为全局参量添加到模块，或使用 `deleteGlobalArg` 函数从模块中删除全局参量。 *(自 R2024b 起)*

### 端口

#### 输入

#### **Port\_1** — 输入端口 标量 | 向量 | 矩阵

输入端口数量及其名称通过您的外部 C 代码中的选定函数推断。要向 C Caller 模块提供数据，请将输入信号连接到输入端口。

输入标签与输入端口名称相同，除非通过从**模块对话框**编辑**端口设定**下的**标签**列对其进行了更改。如果您将标签重命名为输入端口，C Caller 模块会更改端口名称。

对于输入变量，您可以使用**作用域**列将输入作用域更改为参数或常量。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
#### 输出

#### **Port\_1** — 输出端口 标量 | 向量 | 矩阵

输出端口数量及其名称通过您的外部 C 代码中的选定函数推断。要从您的 C Caller 模块发送数据，请将模块连接到您的 C Caller 模块的输出端口。

输出端口标签与输出端口名称相同，除非您通过从**模块对话框**编辑**端口设定**下的**标签**列对其进行了更改。如果您将标签重命名为输入端口，C Caller 模块会更改端口名称。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string`

### 参数

#### **函数名称** — 函数名称 字符向量 | 字符串标量

为 C Caller 模块解析的函数的名称，指定为字符向量或字符串标量。有关可用函数的列表，请参阅可用函数。

**可调:** Yes

##### 编程用法

|  |
| --- |
| **模块参数**：`FunctionName` |
| **类型：**字符向量或字符串标量 |

```
myFunctionName = get_param(gcb,"FunctionName")
```

```
myFunctionName =

    'mean_filter'
```

#### **端口设定** — 端口属性 表

端口属性，指定为表。该表指示模块的每个输入和输出元素的属性。如果作用域是**输入**，您可以将此变量修改为**参数**或**常量**。这些属性包括

**名称** - 演示从源代码推断的变量名称。

粗体参量名称指示端口或参数是全局参量。

**作用域** - 指示源代码中变量的角色。如果变量是 C Caller 模块源代码中的输入参量，您可以将作用域类型更改为常量或参数。如果变量是源代码中的输出参量，您无法更改作用域类型。

**标签** - 为 Simulink 模型的输入或输出变量加标签。您可以使用此表更改标签。如果作用域是参数，请在此字段中输入参数名称。如果作用域是常量，则输入常量值。

**类型** - 指示来自端口的数据类型。

**大小** - 指示输入和输出数据的大小。

名称、作用域、类型和大小从您的源代码推断。

##### 编程用法

|  |
| --- |
| **模块参数**：`FunctionPortSpecification` |
| **类型：**`FunctionPortSpecification` 对象 |

#### **可用函数** — 可用函数列表 元胞数组

可映射到 C Caller 模块的所有可用函数的列表，指定为元胞数组。

您模型中的 C Caller 模块导入外部源代码中的所有函数，并在模块对话框上的函数名称旁边显示函数名称。要在模块中选择和使用函数，请确认函数名称出现在**可用函数**表中。如果其中一个函数缺失，请通过点击模块对话框上的 Refresh custom code button. 重新加载源代码。要更改函数名称，请修改您的源代码并点击**刷新**按钮重新加载。

##### 编程用法

|  |
| --- |
| **模块参数**：`AvailableFunctions` |
| **类型：**元胞数组 |

```
allAvailableFunctions = get_param(gcb, "AvailableFunctions")
```

```
allAvailableFunctions =

  1×1 cell array

    {'add'}
```

#### **采样时间** — 采样周期 `-1` (默认) | 标量 | 向量

采样周期，以秒为单位指定。请参阅 采样时间的类型 和指定采样时间。

##### 编程用法

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符串标量或字符向量 |
| **默认值**：`"-1"` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `否` |
| **多维信号** | `是a` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 实际支持的数据类型或功能取决于模块实施。 | |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2018b 中推出**

#### R2024b: 与模块和函数接口相关的增强功能

- 当模块调用使用字符指针 (`char*`) 或字符数组 (`char[]`) 作为输入或输出数据类型的 C 函数时，现在模块在其端口接受 Simulink 字符串。
- 您现在可以使用命令行 API 手动将自定义代码中的全局变量作为全局参量添加到模块，或从模块中删除现有全局参量。此增强功能使您能够更直接地控制由模块调用的自定义代码中全局变量的行为。

## Libraries

Simulink / User-Defined Functions

## Description

The C Caller block integrates your external C code into Simulink®. This block imports and lists the functions in your external C code, and enables
you to select your resolved C functions to integrate in your Simulink models. The C Caller block standalone supports code generation.
For more complex models, code generation depends on the capabilities of your Simulink model.

To use the C Caller block, define your source code and any supporting files
using **Simulation Target** under **Configuration
Parameters**. Then, bring a C Caller block to the Simulink canvas, using **Library Browser** > **Simulink** > **User Defined Functions**. To change the defined source code file and its dependencies, go to
**Simulation Target** tab in **Configuration
Parameters** by clicking the Configure custom code settings button. from the block dialog. After changing your source code or any
of its dependencies, refresh the list of functions by clicking the Refresh custom code button. on the block dialog. To browse the function definitions in
your source code, use the Go to function button. icon to access your source files.

You can use the `addGlobalArg`
function to add global variables from custom code as global arguments to the block, or use the
`deleteGlobalArg`
function to delete global arguments from the block. *(since R2024b)*

## Ports

### Input

### **Port\_1** — Input port scalar | vector | matrix

The number of input ports and their names are inferred through the selected
function in your external C code. To provide data to a C Caller block,
connect an input signal to the input ports.

The input label has the same name as your input port unless changed by editing the
**Label** column under **Port
Specification** from the **Block Dialog**. If you
rename the label to an input port, the C Caller block changes the name
of the port.

For input variables, you can change the input scope to parameters or constants
using the **Scope** column.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### Output

### **Port\_1** — Output port scalar | vector | matrix

The number of output ports and their names are inferred through the selected
function in your external C code. To send data from your C Caller
block, connect a block to the output port of your C Caller
block.

The output port label has the same name as your output port unless you change it
by editing the **Label** column under **Port
Specification** from the **Block Dialog**. If you
rename the label to an input port, the C Caller block changes the name
of the port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string`

## Parameters

### **Function name** — Name of function character vector | string scalar

Name of the function parsed for the C Caller block, specified as a
character vector or string scalar. For a list of available functions, see Available Functions.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FunctionName` |
| **Type:** character vector or string scalar |

```
myFunctionName = get_param(gcb,"FunctionName")
```

```
myFunctionName =

    'mean_filter'
```

### **Port specification** — Port properties table

Port properties, specified as a table. The table indicates the attributes of each
input and output element of the block. If the scope is an
`input`, you can modify this variable to a
`parameter` or a `constant`. These
properties include

**Name** — Demonstrates the variable name inferred from
your source code.

A bold argument name indicates that the port or parameter is a global
argument.

**Scope** — Indicates the role of the variables from
your source code. If the variable is an input argument in the C Caller
block source code, you can change the scope type to a constant or a parameter. If the
variable is an output argument in the source code, you cannot change the scope
type.

**Label** — Labels the input or output variable for the
Simulink model. You can change the labels using this table. If the scope is a
parameter, enter the parameter name in this field. If the scope is a constant, enter the
constant value.

**Type** — Indicates the data type coming from the
ports.

**Size** — Indicates the size of the input and output
data.

Name, scope, type, and size are inferred from your source code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FunctionPortSpecification` |
| **Type:** `FunctionPortSpecification` object |

### **Available Functions** — List of available functions cell array

List of all available functions that can be mapped to a C Caller
block, specified as a cell array.

The C Caller block in your model imports all functions in your
external source code, and shows the function names next to the Function name on the block
dialog. To select and use a function in your block, confirm that the function name
appears in the `Available Functions` table. If you are missing
one of the functions, reload the source code by clicking Refresh custom code button. on the block dialog. To change the names of functions,
modify your source code and click the **Refresh** button to reload.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AvailableFunctions` |
| **Type:** cell array |

```
allAvailableFunctions = get_param(gcb, "AvailableFunctions")
```

```
allAvailableFunctions =

  1×1 cell array

    {'add'}
```

### **Sample time** — Sample period `-1` (default) | scalar | vector

Sample period, specified in seconds. See Types of Sample Time
and Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: string scalar or character vector |
| **Default**: `"-1"` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2018b**

### R2024b: Enhancements related to block and function interface

- The block now accepts Simulink strings at its ports when the block calls a C
  function that uses character pointer (`char*`) or character array
  (`char[]`) as input or output data types.
- You can now use command line APIs to manually add global variables from custom code
  to the block as global arguments or delete existing global arguments from the block.
  This enhancement enables you to more directly control the behavior of global variables
  in the custom code called by the block.
