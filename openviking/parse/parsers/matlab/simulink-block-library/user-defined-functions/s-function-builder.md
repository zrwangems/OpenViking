---
type: simulink-block
title: 'S-Function Builder'
family: user-defined-functions
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'sfunctionbuilder'
---

# S-Function Builder

Integrate C or C++ code to create S-functions

## 中文

集成 C 或 C++ 代码以创建 S-Function

### 所属库

Simulink / User-Defined Functions

### 描述

S-function Builder 模块集成新的或现有 C 或 C++ 代码，并根据您提供的设定创建 C MEX S-Function（系统函数）。C MEX S-Function 是用 C 或 C++ 编写的 Simulink® 模块的计算机语言描述。S-Function 使用一种称为 S-Function API 的特殊调用语法，使您能够与 Simulink 引擎进行交互。这种交互与该引擎和内置 Simulink 模块之间发生的交互非常相似。要了解有关 C MEX S-Function 的更多信息，请参阅什么是 S-Function。要了解有关使用 S-function Builder 模块编译 C MEX S-Function 的更多信息，请参阅Build S-Functions Automatically Using S-Function Builder。有关使用分步过程的示例，请参阅Use a Bus with S-Function Builder to Create an S-Function。

S-Function Builder 模块实例还作为 Simulink 模型中生成的 S-Function 的包装器。当对包含 S-Function Builder 模块实例的模型进行仿真时，Simulink 会调用生成的 C MEX S-Function，以调用 `mdlStart`、`mdlOutputs`、`mdlDerivatives`、`mdlUpdate` 和 `mdlTerminate` 方法实例中的 C 或 C++ 代码。要了解 Simulink 引擎如何与 S-Function 交互，请参阅 Simulink Engine Interaction with C S-Functions。

**注意**

S-Function Builder 模块不支持封装。但是，您可以封装包含 S-Function Builder 模块的 Subsystem 模块。有关详细信息，请参阅Create Library Blocks Using Self-Modifiable Masks and Variant Blocks。

### 端口

#### 输入

#### **Port\_1** — S-Function 输入 标量 | 向量 | 矩阵

S-Function Builder 模块可以接受实数和复数、一维或二维信号以及非虚拟总线。不管是哪一种情况，信号都必须具有 Simulink 支持的数据类型。

有关详细信息，请参阅 Simulink 文档中的 Simulink 支持的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
#### 输出

#### **Out** — S-Function 输出 标量 | 向量 | 矩阵

S-Function Builder 可以产生实数和复数、一维或二维信号以及非虚拟总线。不管是哪一种情况，信号都必须具有 Simulink 支持的数据类型。

有关详细信息，请参阅 Simulink 文档中的 Simulink 支持的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### 参数

使用 S-Function Builder 编辑器创建用户定义的参数。有关从编辑器创建用户定义参数的详细信息，请参阅Specify Ports and Parameters for the S-Function。

**注意**

您不需要使用模块对话框为此模块设置这些列出的 Simulink 模块参数。使用 S-Function Builder 编辑器中的信息设置 Simulink 模块参数。

#### **S-Function 名称** — S-Function 的名称 `system` (默认) | S-Function 名称

使用此参数指定 S-Function 的名称。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FunctionName` |
| **值:** | `'system'` (默认) | S-function name in quotes |

#### **S-Function 参数** — 其他 S-Function 参数。 MATLAB® 表达式 | 以逗号分隔的变量

指定其他 S-Function 参数。

函数参数可以指定为 MATLAB 表达式或以逗号分隔的变量。例如：

```
A, B, C, D, [eye(2,2);zeros(2,2)]
```

尽管单个参数可以用括号括起来，但参数列表一定不能用括号括起来。

##### 编程用法

|  |  |
| --- | --- |
| **参数:** | `Parameters` |
| **值:** | `''` (默认) | S-function parameters in quotes |

#### **S-Function 模块** — 用于代码生成的其他文件 `''` (默认) | 文件名

仅当此模块代表 C MEX S-Function，并且您打算使用 Simulink Coder™ 软件从包含该模块的模型中生成代码时，此参数才适用。如果您使用此参数，当您准备好生成代码时，必须按照Control Regeneration of Top Model Code (Simulink Coder)中所述，强制代码生成器重新生成顶层模型。

有关使用此参数的详细信息，请参阅为 S-Function 指定其他源文件 (Simulink Coder)。

##### 编程用法

|  |  |
| --- | --- |
| **参数:** | `SFunctionModules` |
| **值:** | `''` (默认) | filenames in quotes |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

调用 MATLAB 的 S-Function 不支持代码生成。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / User-Defined Functions

## Description

The S-function Builder block integrates new or existing C or C++ code
and creates a C MEX S-function (system-function) from specifications you provide. A C
MEX S-function is a computer language description of a Simulink® block written in C or C++. S-functions use a special calling syntax called
the S-function API that enables you to interact with the Simulink engine. This interaction is very similar to the interaction that takes
place between the engine and built-in Simulink blocks. To learn more about C MEX S-functions, see What Is an S-Function?.
To learn more about building C MEX S-Functions using the S-function
Builder block, see Build S-Functions Automatically Using S-Function Builder. For an example with a step-by-step procedure,
see Use a Bus with S-Function Builder to Create an S-Function.

Instances of the S-Function Builder block also serve as wrappers for
generated S-functions in Simulink models. When simulating a model that contains instances of an
S-Function Builder block, Simulink invokes the generated C MEX S-function to call your C or C++ code in the
instances of `mdlStart`, `mdlOutputs`,
`mdlDerivatives`, `mdlUpdate` and
`mdlTerminate` methods. To learn how Simulink engine interacts with S-functions, see Simulink Engine Interaction with C S-Functions.

**Note**

The S-Function Builder block does not support masking. However, you
can mask a Subsystem block that contains an
S-Function Builder block. For more information, see Create Library Blocks Using Self-Modifiable Masks and Variant Blocks.

## Ports

### Input

### **Port\_1** — S-function input scalar | vector | matrix

The S-Function Builder block can accept real and
complex, 1-D, or 2-D signals and nonvirtual buses. For each of these
cases, the signals must have a data type that Simulink supports.

For more information, see Data Types Supported by Simulink in the Simulink documentation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### Output

### **Out** — S-function output scalar | vector | matrix

The S-Function Builder can produce real and complex,
1-D, or 2-D signals and nonvirtual buses. For each of these cases, the
signals must have a data type that Simulink supports.

For more information, see Data Types Supported by Simulink in the Simulink documentation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

## Parameters

Use the S-Function Builder editor to create user-defined parameters.
For more information on creating user-defined parameters from the editor, see Specify Ports and Parameters for the S-Function.

**Note**

You do not need to set these listed Simulink block parameters for this block using the block dialog. The
Simulink block parameters are set using the information from the
S-Function Builder editor.

### **S-function name** — Name of the S-function `system` (default) | S-function name

Use this parameter to specify the name of your S-function.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FunctionName` |
| **Values:** | `'system'` (default) | S-function name in quotes |

### **S-function parameters** — Additional S-function parameters MATLAB® expressions | comma-separated variables

Specify the additional S-function parameters.

The function parameters can be specified as MATLAB expressions or as variables separated by commas. For
example:

```
A, B, C, D, [eye(2,2);zeros(2,2)]
```

Although individual parameters can be enclosed in brackets, the list of
parameters must not be enclosed in brackets.

#### Programmatic Use

|  |  |
| --- | --- |
| **Parameter:** | `Parameters` |
| **Values:** | `''` (default) | S-function parameters in quotes |

### **S-function modules** — Additional files for code generation `''` (default) | filenames

This parameter applies only if this block represents a C MEX S-function
and you intend to use the Simulink
Coder™ software to generate code from the model containing the block.
If you use it, when you are ready to generate code, you must force the coder
to rebuild the top model as explained in Control Regeneration of Top Model Code (Simulink Coder).

For more information on using this parameter, see Specify Additional Source Files for an S-Function (Simulink Coder).

#### Programmatic Use

|  |  |
| --- | --- |
| **Parameter:** | `SFunctionModules` |
| **Values:** | `''` (default) | filenames in quotes |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

S-functions that call into MATLAB are not supported for code generation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
