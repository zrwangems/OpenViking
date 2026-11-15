---
type: simulink-block
title: 'S-Function Builder'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Environment Fundamentals / Block Libraries / User-Defined Functions'
documentation_page: 'sfunctionbuilder'
documentation_source_path: 'slref/sfunctionbuilder.html'
language: zh-CN
chinese_source: official
---

# S-Function Builder

## 端口

### 输入

### **Port\_1** — S-Function 输入 标量 | 向量 | 矩阵

S-Function Builder 模块可以接受实数和复数、一维或二维信号以及非虚拟总线。不管是哪一种情况，信号都必须具有 Simulink 支持的数据类型。

有关详细信息，请参阅 Simulink 文档中的 Simulink 支持的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### 输出

### **Out** — S-Function 输出 标量 | 向量 | 矩阵

S-Function Builder 可以产生实数和复数、一维或二维信号以及非虚拟总线。不管是哪一种情况，信号都必须具有 Simulink 支持的数据类型。

有关详细信息，请参阅 Simulink 文档中的 Simulink 支持的数据类型。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

## 参数

使用 S-Function Builder 编辑器创建用户定义的参数。有关从编辑器创建用户定义参数的详细信息，请参阅Specify Ports and Parameters for the S-Function。

**注意**

您不需要使用模块对话框为此模块设置这些列出的 Simulink 模块参数。使用 S-Function Builder 编辑器中的信息设置 Simulink 模块参数。

### **S-Function 名称** — S-Function 的名称 `system` (默认) | S-Function 名称

使用此参数指定 S-Function 的名称。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `FunctionName` |
| **值:** | `'system'` (默认) | S-function name in quotes |

### **S-Function 参数** — 其他 S-Function 参数。 MATLAB® 表达式 | 以逗号分隔的变量

指定其他 S-Function 参数。

函数参数可以指定为 MATLAB 表达式或以逗号分隔的变量。例如：

```
A, B, C, D, [eye(2,2);zeros(2,2)]
```

尽管单个参数可以用括号括起来，但参数列表一定不能用括号括起来。

#### 编程用法

|  |  |
| --- | --- |
| **参数:** | `Parameters` |
| **值:** | `''` (默认) | S-function parameters in quotes |

### **S-Function 模块** — 用于代码生成的其他文件 `''` (默认) | 文件名

仅当此模块代表 C MEX S-Function，并且您打算使用 Simulink Coder™ 软件从包含该模块的模型中生成代码时，此参数才适用。如果您使用此参数，当您准备好生成代码时，必须按照Control Regeneration of Top Model Code (Simulink Coder)中所述，强制代码生成器重新生成顶层模型。

有关使用此参数的详细信息，请参阅为 S-Function 指定其他源文件 (Simulink Coder)。

#### 编程用法

|  |  |
| --- | --- |
| **参数:** | `SFunctionModules` |
| **值:** | `''` (默认) | filenames in quotes |

## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

调用 MATLAB 的 S-Function 不支持代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

集成 C 或 C++ 代码以创建 S-Function

S-function Builder 模块集成新的或现有 C 或 C++ 代码，并根据您提供的设定创建 C MEX S-Function（系统函数）。C MEX S-Function 是用 C 或 C++ 编写的 Simulink® 模块的计算机语言描述。S-Function 使用一种称为 S-Function API 的特殊调用语法，使您能够与 Simulink 引擎进行交互。这种交互与该引擎和内置 Simulink 模块之间发生的交互非常相似。要了解有关 C MEX S-Function 的更多信息，请参阅什么是 S-Function。要了解有关使用 S-function Builder 模块编译 C MEX S-Function 的更多信息，请参阅Build S-Functions Automatically Using S-Function Builder。有关使用分步过程的示例，请参阅Use a Bus with S-Function Builder to Create an S-Function。

S-Function Builder 模块实例还作为 Simulink 模型中生成的 S-Function 的包装器。当对包含 S-Function Builder 模块实例的模型进行仿真时，Simulink 会调用生成的 C MEX S-Function，以调用 `mdlStart`、`mdlOutputs`、`mdlDerivatives`、`mdlUpdate` 和 `mdlTerminate` 方法实例中的 C 或 C++ 代码。要了解 Simulink 引擎如何与 S-Function 交互，请参阅 Simulink Engine Interaction with C S-Functions。

**注意**

S-Function Builder 模块不支持封装。但是，您可以封装包含 S-Function Builder 模块的 Subsystem 模块。有关详细信息，请参阅Create Library Blocks Using Self-Modifiable Masks and Variant Blocks。
